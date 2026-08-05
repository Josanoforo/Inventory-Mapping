#!/usr/bin/env python3
"""scan_router.py — single writer for Phase 3 scan routing (E-RUT-2, S38).

Reads the 7 scan artifacts (`working/scans/*.json`) plus the card index
(`working/index/card_index.jsonl`) and produces one authoritative routing
decision per pattern. Routing is a pure function of (patterns, index,
rules): given the same inputs, it always produces the same outputs. No
scan skill writes a final routing decision anymore for the two mechanical
rules below — the router computes them and overwrites whatever the skill
wrote. For every other case, the skill's judgment routing is transported
as-is (or, for historical artifacts that predate the `reason_code` schema
field, inferred from `routing_rationale` text against the closed enum).

Mechanical rules
----------------
`same_actor` — applies ONLY to the 4 scans whose skills declare a
same-actor filter (asymmetries, contradictions, frictions,
opposite_directions; see D-... / PR #117 M2 for why the other 3 scans —
co_occurrences, gaps, lexical_overlap — are excluded by design, not
omission). A pattern in one of these 4 scans is rejected with
reason_code=same_actor when ALL of its signal_ids resolve against the
index to a single actor value and there is more than one signal_id. If
any signal_id does NOT resolve against the index, that is reported as an
anomaly and the pattern is NOT judged by this rule (neither routed nor
rejected on same-actor grounds — it falls through to transport/inference
instead).

`insufficient_ids` — applies to ALL scans. Fires when the count of
signal_ids that resolve against the index is <2 (any scan), or <3 when
scan_type == lexical_overlap.

These two rules are mutually exclusive per pattern and checked in the
order above (same_actor first). Whichever fires first wins; if neither
fires, the pattern falls through to transport/inference below.

Transport / inference
----------------------
If neither mechanical rule fires, the router transports the skill's own
`routing`. If the pattern already carries an explicit `reason_code` field
(schema field added in #123; only artifacts produced after that PR will
have it), that value is transported verbatim. If the skill's routing is
`rejected_grouping` and no `reason_code` field is present (artifacts from
before #123), the router classifies `routing_rationale` text against the
closed enum using the deterministic, ordered rules in `classify_text()`
below and sets `reason_code_inferred: true`. Patterns whose rationale
matches none of the classifier's patterns are left with reason_code=null
and are listed in the run summary as unclassified — never silently
dropped.

`coverage_signal` re-route
---------------------------
Whenever the applicable reason_code (transported or inferred) equals
`coverage_signal`, the pattern's final routing becomes `coverage_gap`
regardless of what routing the skill (or the same_actor/insufficient_ids
check) produced. This is the one case where a reason_code can change the
routing rather than just annotate it.

Overrides
---------
If `routing_overrides.json` exists alongside the scan artifacts, it is
applied AFTER the mechanical rules and AFTER transport/inference. Each
entry requires pattern_id, routing, reason_code, and decision (a D-NNN
operator decision reference). Absence of the file is not an error — it
is simply not applied.

Determinism
-----------
Patterns are processed in a fixed scan order (the 7-operation order from
`modules/04_scanner.md`: contradictions, asymmetries, frictions,
co_occurrences, gaps, opposite_directions, lexical_overlap), then sorted
by pattern_id within each scan. Scan files are read by their known,
hardcoded filename — never via directory listing — so output ordering
never depends on `os.listdir` order. No wall-clock timestamp is written
into any output file's content.

Barrier
-------
With a single writer, a producer that silently fails to write its
pattern is structurally impossible to hide: every pattern read from the
7 scan files is accounted for in exactly one output bucket (see
`build_bijection_report()`), and the router's own summary reports the
input/output pattern counts every run. This does not mean silent
discards cannot be caused upstream (a scan skill could still fail to
write a pattern into its own artifact) — only that once a pattern is in
a scan artifact, the router can no longer lose it between scan and
routed output the way independent per-scan writers historically did
(see d745a58f: 33 lost LEX patterns recovered by hand). The router turns
"detectable after the fact" into "impossible at the routing step."

Usage
-----
    python phases/03-inventory-mapping/scripts/scan_router.py
    python phases/03-inventory-mapping/scripts/scan_router.py \\
        --scans-dir working/scans --index working/index/card_index.jsonl \\
        --output-dir output
"""

import argparse
import json
import re
import sys
from pathlib import Path

# ====================================================================
# Constantes
# ====================================================================

DEFAULT_SCANS_DIR = Path("working/scans")
DEFAULT_INDEX_PATH = Path("working/index/card_index.jsonl")
DEFAULT_OUTPUT_DIR = Path("output")

# Orden canónico de las 7 operaciones (modules/04_scanner.md). Fijo, no se
# deriva de os.listdir: determinismo de orden depende de esto, no del
# filesystem.
SCAN_ORDER = [
    "contradictions",
    "asymmetries",
    "frictions",
    "co_occurrences",
    "gaps",
    "opposite_directions",
    "lexical_overlap",
]

# Los 4 scans cuyas skills declaran el filtro same-actor (grep verificado
# en .claude/skills/scan-{asymmetries,contradictions,frictions,
# opposite-directions}/SKILL.md). co_occurrences, gaps y lexical_overlap
# quedan fuera por diseño declarado (commit bbda31a9, PR #117 M2), no por
# omisión.
SAME_ACTOR_SCANS = {"asymmetries", "contradictions", "frictions", "opposite_directions"}

REASON_CODES = {
    "same_actor",
    "insufficient_ids",
    "no_dt_question",
    "no_explicit_friction",
    "dedup_same_source",
    "overlap_existing_tc",
    "coverage_signal",
}

ROUTING_VALUES = {
    "tension_candidate",
    "rejected_grouping",
    "coverage_gap",
    "isolated_signal",
    "needs_audit",
}

ROUTING_TABLE_FILENAME = "routing_table.json"
REJECTED_GROUPINGS_FILENAME = "rejected_groupings.md"
COVERAGE_GAPS_FILENAME = "coverage_gaps.md"
ISOLATED_SIGNALS_FILENAME = "isolated_signals.md"
TC_LIST_FILENAME = "tension_candidates_for_builder.json"
ROUTING_DIFF_FILENAME = "routing_diff.md"
OVERRIDES_FILENAME = "routing_overrides.json"


# ====================================================================
# Clasificador de texto (solo para reason_code faltante en patrones con
# routing=rejected_grouping heredados de antes de #123). Determinista:
# mismo texto de entrada -> misma salida, siempre. Orden de reglas
# importa -- ver docstring del módulo, sección "Transport / inference".
# same_actor e insufficient_ids NUNCA se infieren por texto: son
# exclusivamente mecánicos (nota en pipeline_vocabulary.yaml).
# ====================================================================

_CLASSIFY_RULES = [
    ("overlap_existing_tc", re.compile(
        r"already captured in|already covers?|overlaps? substantially with",
        re.IGNORECASE,
    )),
    ("dedup_same_source", re.compile(r"dedup(e|lication)?", re.IGNORECASE)),
    ("coverage_signal", re.compile(r"coverage gap", re.IGNORECASE)),
    ("no_explicit_friction", re.compile(r"no explicit friction", re.IGNORECASE)),
    ("no_dt_question", re.compile(r"no dt question", re.IGNORECASE)),
]


def classify_text(routing_rationale):
    """Return the first matching non-mechanical reason_code, or None."""
    if not routing_rationale:
        return None
    for code, pattern in _CLASSIFY_RULES:
        if pattern.search(routing_rationale):
            return code
    return None


# ====================================================================
# Carga de datos
# ====================================================================

def load_index(index_path):
    """id -> actor, from card_index.jsonl."""
    index = {}
    if not index_path.exists():
        return index
    with index_path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rec = json.loads(line)
            index[rec["id"]] = rec.get("actor")
    return index


def load_scan(scans_dir, scan_type):
    """Load one scan artifact by its known filename. Returns (patterns, status) or (None, None) if absent."""
    path = scans_dir / f"{scan_type}.json"
    if not path.exists():
        return None, None
    with path.open(encoding="utf-8") as f:
        data = json.load(f)
    return data.get("patterns", []), data.get("status")


def load_overrides(scans_dir):
    path = scans_dir / OVERRIDES_FILENAME
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as f:
        data = json.load(f)
    entries = data if isinstance(data, list) else data.get("overrides", [])
    for entry in entries:
        missing = [k for k in ("pattern_id", "routing", "reason_code", "decision") if k not in entry]
        if missing:
            raise ValueError(f"routing_overrides.json entry missing required keys {missing}: {entry}")
    return entries


# ====================================================================
# Ruteo mecánico + transporte/inferencia por patrón
# ====================================================================

def route_pattern(scan_type, pattern, index):
    pattern_id = pattern["pattern_id"]
    signal_ids = list(pattern.get("signal_ids", []))
    input_routing = pattern.get("routing")
    input_reason_code = pattern.get("reason_code")
    routing_rationale = pattern.get("routing_rationale", "")

    resolved = {sid: index[sid] for sid in signal_ids if sid in index}
    unresolved = [sid for sid in signal_ids if sid not in index]
    resolved_count = len(set(resolved.keys()))
    distinct_actors = sorted(set(resolved.values()))

    same_actor_scope = scan_type in SAME_ACTOR_SCANS
    same_actor_hit = (
        same_actor_scope
        and not unresolved
        and len(signal_ids) > 1
        and len(distinct_actors) == 1
    )

    insufficient_hit = False
    if not same_actor_hit:
        if scan_type == "lexical_overlap" and resolved_count < 3:
            insufficient_hit = True
        elif resolved_count < 2:
            insufficient_hit = True

    if same_actor_hit:
        reason_code = "same_actor"
        reason_source = "mechanical"
        reason_inferred = False
        routing = "rejected_grouping"
    elif insufficient_hit:
        reason_code = "insufficient_ids"
        reason_source = "mechanical"
        reason_inferred = False
        routing = "rejected_grouping"
    else:
        routing = input_routing
        if input_reason_code:
            reason_code = input_reason_code
            reason_source = "transported"
            reason_inferred = False
        elif input_routing == "rejected_grouping":
            reason_code = classify_text(routing_rationale)
            reason_inferred = reason_code is not None
            reason_source = "inferred" if reason_code else "unclassified"
        else:
            reason_code = None
            reason_source = "transported"
            reason_inferred = False

        if reason_code == "coverage_signal":
            routing = "coverage_gap"

    return {
        "scan": scan_type,
        "pattern_id": pattern_id,
        "signal_ids": signal_ids,
        "input_routing": input_routing,
        "output_routing": routing,
        "reason_code": reason_code,
        "reason_source": reason_source,  # mechanical | transported | inferred | unclassified
        "reason_code_inferred": reason_inferred,
        "distinct_actors": distinct_actors,
        "unresolved_ids": unresolved,
        "routing_rationale": routing_rationale,
        "description": pattern.get("description", ""),
        "signal_summaries": pattern.get("signal_summaries", {}),
        "components": pattern.get("components", []),
        "override_applied": False,
        "override_decision": None,
    }


def apply_overrides(routed, overrides):
    if not overrides:
        return routed
    by_pattern_id = {r["pattern_id"]: r for r in routed}
    for entry in overrides:
        pid = entry["pattern_id"]
        if pid not in by_pattern_id:
            continue
        rec = by_pattern_id[pid]
        rec["output_routing"] = entry["routing"]
        rec["reason_code"] = entry["reason_code"]
        rec["reason_source"] = "override"
        rec["reason_code_inferred"] = False
        rec["override_applied"] = True
        rec["override_decision"] = entry["decision"]
    return routed


# ====================================================================
# Construcción de la tabla de ruteo (orden determinístico)
# ====================================================================

def build_routing_table(scans_dir, index_path):
    index = load_index(index_path)
    overrides = load_overrides(scans_dir)

    routed = []
    scans_seen = []
    for scan_type in SCAN_ORDER:
        patterns, status = load_scan(scans_dir, scan_type)
        if patterns is None:
            continue
        scans_seen.append((scan_type, status))
        for pattern in sorted(patterns, key=lambda p: p["pattern_id"]):
            routed.append(route_pattern(scan_type, pattern, index))

    routed = apply_overrides(routed, overrides)
    return routed, scans_seen, index, overrides


def bijection_report(routed):
    buckets = {v: 0 for v in sorted(ROUTING_VALUES)}
    for r in routed:
        buckets[r["output_routing"]] = buckets.get(r["output_routing"], 0) + 1
    return buckets


# ====================================================================
# Salidas
# ====================================================================

def write_routing_table(output_dir, routed):
    path = output_dir / ROUTING_TABLE_FILENAME
    payload = {
        "patterns": routed,
        "summary": {
            "patterns_total": len(routed),
            "by_routing": bijection_report(routed),
        },
    }
    path.write_text(json.dumps(payload, indent=2, sort_keys=False, ensure_ascii=False) + "\n", encoding="utf-8")
    return path


def write_rejected_groupings(output_dir, routed):
    lines = ["# Rejected Groupings", "", "Generated by scan_router.py (single writer, deterministic)."]
    entries = [r for r in routed if r["output_routing"] == "rejected_grouping"]
    for r in entries:
        lines.append("")
        lines.append(f"## {r['pattern_id']} ({r['scan']})")
        lines.append(f"- signal_ids: {', '.join(r['signal_ids'])}")
        lines.append(f"- reason_code: {r['reason_code']} ({r['reason_source']})")
        if r["unresolved_ids"]:
            lines.append(f"- unresolved_ids (anomaly): {', '.join(r['unresolved_ids'])}")
        lines.append(f"- routing_rationale: {r['routing_rationale']}")
    if not entries:
        lines.append("")
        lines.append("(no patterns routed to rejected_grouping in this run)")
    (output_dir / REJECTED_GROUPINGS_FILENAME).write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_coverage_gaps(output_dir, routed):
    lines = ["# Coverage Gaps", "", "Generated by scan_router.py (single writer, deterministic)."]
    entries = [r for r in routed if r["output_routing"] == "coverage_gap"]
    for r in entries:
        lines.append("")
        lines.append(f"## {r['pattern_id']} ({r['scan']})")
        lines.append(f"- signal_ids_if_any: {', '.join(r['signal_ids']) if r['signal_ids'] else '(none)'}")
        lines.append(f"- description: {r['description']}")
        origin = "native gaps scan" if r["scan"] == "gaps" else f"re-routed from {r['scan']} (reason_code={r['reason_code']})"
        lines.append(f"- why_it_limits_reading_of_the_inventory / origin: {origin}")
    if not entries:
        lines.append("")
        lines.append("(no patterns routed to coverage_gap in this run)")
    (output_dir / COVERAGE_GAPS_FILENAME).write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_isolated_signals(output_dir, routed):
    lines = ["# Isolated Signals", "", "Generated by scan_router.py (single writer, deterministic)."]
    entries = [r for r in routed if r["output_routing"] == "isolated_signal"]
    for r in entries:
        lines.append("")
        lines.append(f"## {r['pattern_id']} ({r['scan']})")
        lines.append(f"- signal_ids: {', '.join(r['signal_ids'])}")
        lines.append(f"- why_preserved: {r['routing_rationale']}")
    if not entries:
        lines.append("")
        lines.append("(no isolated signals in this run)")
    (output_dir / ISOLATED_SIGNALS_FILENAME).write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_tc_list(output_dir, routed):
    entries = [r for r in routed if r["output_routing"] in ("tension_candidate", "needs_audit")]
    path = output_dir / TC_LIST_FILENAME
    path.write_text(json.dumps(entries, indent=2, sort_keys=False, ensure_ascii=False) + "\n", encoding="utf-8")
    return path


def write_routing_diff(output_dir, routed, previous_table_path):
    if not previous_table_path.exists():
        return None
    with previous_table_path.open(encoding="utf-8") as f:
        previous = json.load(f)
    previous_by_key = {(r["scan"], r["pattern_id"]): r for r in previous.get("patterns", [])}
    current_by_key = {(r["scan"], r["pattern_id"]): r for r in routed}

    lines = ["# Routing Diff", "", "Generated by scan_router.py against the previous routing_table.json."]
    changed = []
    for key in sorted(set(previous_by_key) | set(current_by_key)):
        prev = previous_by_key.get(key)
        curr = current_by_key.get(key)
        if prev is None:
            changed.append((key, "added", None, curr))
        elif curr is None:
            changed.append((key, "removed", prev, None))
        elif prev.get("output_routing") != curr.get("output_routing") or prev.get("reason_code") != curr.get("reason_code"):
            changed.append((key, "changed", prev, curr))

    if not changed:
        lines.append("")
        lines.append("(no routing changes since previous run)")
    for key, kind, prev, curr in changed:
        scan, pattern_id = key
        lines.append("")
        lines.append(f"## {pattern_id} ({scan}) — {kind}")
        if prev is not None:
            lines.append(f"- previous: routing={prev.get('output_routing')} reason_code={prev.get('reason_code')}")
        if curr is not None:
            lines.append(f"- current:  routing={curr.get('output_routing')} reason_code={curr.get('reason_code')}")

    path = output_dir / ROUTING_DIFF_FILENAME
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


# ====================================================================
# Main
# ====================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Phase 3 scan routing — single writer (E-RUT-2, S38)."
    )
    parser.add_argument(
        "--scans-dir", type=Path, default=DEFAULT_SCANS_DIR,
        help=f"Directory with the 7 scan artifacts (default: {DEFAULT_SCANS_DIR})",
    )
    parser.add_argument(
        "--index", type=Path, default=DEFAULT_INDEX_PATH,
        help=f"Path to card_index.jsonl (default: {DEFAULT_INDEX_PATH})",
    )
    parser.add_argument(
        "--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR,
        help=f"Directory to write routing outputs to (default: {DEFAULT_OUTPUT_DIR})",
    )
    args = parser.parse_args()

    routed, scans_seen, index, overrides = build_routing_table(args.scans_dir, args.index)

    args.output_dir.mkdir(parents=True, exist_ok=True)

    previous_table_path = args.output_dir / ROUTING_TABLE_FILENAME
    diff_path = write_routing_diff(args.output_dir, routed, previous_table_path) if previous_table_path.exists() else None

    table_path = write_routing_table(args.output_dir, routed)
    write_rejected_groupings(args.output_dir, routed)
    write_coverage_gaps(args.output_dir, routed)
    write_isolated_signals(args.output_dir, routed)
    tc_path = write_tc_list(args.output_dir, routed)

    buckets = bijection_report(routed)
    unresolved_total = sum(len(r["unresolved_ids"]) for r in routed)
    unclassified = [r["pattern_id"] for r in routed if r["reason_source"] == "unclassified"]

    print(f"Scans read: {[s for s, _ in scans_seen]}")
    print(f"Index size: {len(index)}")
    print(f"Overrides applied: {sum(1 for r in routed if r['override_applied'])}")
    print(f"Patterns processed: {len(routed)}")
    print(f"By routing: {buckets}")
    print(f"Unresolved signal_ids across all patterns: {unresolved_total}")
    print(f"Unclassified (rejected_grouping, no reason_code): {unclassified}")
    print(f"Wrote: {table_path}")
    print(f"Wrote: {tc_path}")
    if diff_path:
        print(f"Wrote: {diff_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
