#!/usr/bin/env python3
"""
vocab_usage_check.py

D-282(b) / P-191. Static invariant: no value actually used anywhere in the
corpus (packets, records, cards, skeletons) may be missing from
pipeline_vocabulary.yaml. This is the inverse direction of vocab_check.py,
which compares the vocabulary against *.schema.json structure (and
explicitly excludes working/). Retiring a vocabulary value that still has
real uses in the corpus is the failure mode this catches -- on every run
over whatever is on disk, with no diff inspection needed.

Why a separate script, not a new mode of vocab_check.py: vocab_check.py's
whole traversal is schema documents (walk $ref/oneOf/anyOf/items over
*.schema.json, "excl. working/" per its own docstring). This check walks
JSON data instances under working/ across several directory trees per
field -- a different data source, a different failure meaning (a value
about to be silently dropped from real data, not a schema/vocab enum
mismatch), and a different exit condition. Folding it into vocab_check.py
would contradict that script's stated scope for no benefit; keeping it
separate keeps each check's red state legible on its own.

Why this exists (E1, replicated with two independent methods -- python and
jq -- against a second base commit, same result both times): three
pipeline_vocabulary.yaml values were reported as "0 usos" ahead of a
proposed retirement. Measured against working/source_intake/packets/*.json,
`.uncertainties[]`, the real counts were source_type_unclear=2,
metric_type_unclear=35, snippet_needs_reopen=355 -- all three retirements
would have silently dropped populated data with no signal at retirement
time. A per-diff trigger to catch this was estimated and rejected as too
costly to build; this static invariant catches it on every run instead,
regardless of what the diff touched.

Layers checked: working/source_intake/packets, working/data_extraction/
records, working/signal_extraction/cards, and the three skeleton_batches
trees (source_intake, data_extraction, signal_extraction) that feed them --
the four layers D-282(b) names ("packets, records, cards, skeletons").
Not in scope: working/data_gathering/findings (verification_status, phase
0) and working/data_extraction/rejected_archive_phase1b/
(phase1b_rejection_reason) -- neither is one of those four layers.

EXCEPTIONS below are declared with a citation each, not a bare note:
  - product_type_if_explicit: known-broken field (state/output/
    etapa3_veredictos.md, "## Campo roto que esta adjudicacion no toca").
    849/1,178 extraction records are already null (schema-invalid, no
    `null` branch in the oneOf) or out-of-enum for this field -- free-text
    values here are the pre-existing break the recovery arm (P-196
    candidate) is meant to fix, not a new regression this check should
    flag.

Usage:
    python3 vocab_usage_check.py
"""

import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent
VOCAB_PATH = ROOT / "pipeline_vocabulary.yaml"

# Same shape as vocab_check.py's META_KEYS, minus "deprecated": a deprecated
# value is still a declared member of the vocabulary (see P-187 / CLAUDE.md
# authority hierarchy) -- it stays a valid target for the reverse-direction
# "is this used value in the vocabulary at all" check this script runs.
META_KEYS = {
    "notes", "phase", "source", "match",
    "schema_field", "in_schemas", "optional", "assignment_rule",
}

EXCEPTIONS = {
    "product_type_if_explicit": (
        "Campo roto, no regresion nueva (state/output/etapa3_veredictos.md, "
        "'## Campo roto que esta adjudicacion no toca'): 849/1,178 extraction "
        "records ya son invalidos para este campo (642 null + 207 fuera de "
        "enum). El brazo de recuperacion (candidata P-196) es quien corrige "
        "esto; este check no lo gatea mientras tanto."
    ),
}


def load_vocab():
    with VOCAB_PATH.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def vocab_values(entry):
    """Union of every list-valued key in a vocab entry, excluding meta keys.
    Includes 'deprecated' (unlike vocab_check.py's resolved_values) since a
    deprecated value is still part of the declared vocabulary here."""
    values = set()
    for key, val in entry.items():
        if key in META_KEYS:
            continue
        if isinstance(val, list):
            values.update(v for v in val if isinstance(v, str))
    return values


def iter_json_files(*dir_parts, recursive=False):
    d = ROOT.joinpath(*dir_parts)
    if not d.exists():
        return []
    pattern = "**/*.json" if recursive else "*.json"
    return sorted(d.glob(pattern))


def load_json(path):
    import json
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, Exception):
        return None


def as_list(val):
    if val is None:
        return []
    if isinstance(val, list):
        return [v for v in val if isinstance(v, str)]
    if isinstance(val, str):
        return [val]
    return []


def collect_scalar(files, field):
    """field -> {value: set(files_using_it)}"""
    usage = {}
    for path in files:
        doc = load_json(path)
        if not isinstance(doc, dict):
            continue
        for v in as_list(doc.get(field)):
            usage.setdefault(v, set()).add(str(path.relative_to(ROOT)))
    return usage


def collect_nested_pointer_type(files, container_field, is_array):
    usage = {}
    for path in files:
        doc = load_json(path)
        if not isinstance(doc, dict):
            continue
        container = doc.get(container_field)
        pointers = container if is_array and isinstance(container, list) else (
            [container] if not is_array and isinstance(container, dict) else []
        )
        for ptr in pointers:
            if not isinstance(ptr, dict):
                continue
            v = ptr.get("pointer_type")
            if isinstance(v, str):
                usage.setdefault(v, set()).add(str(path.relative_to(ROOT)))
    return usage


# Each entry: vocab field name -> list of (label, files, extractor) probes.
# Layers: packets, records, cards, and the three skeleton_batches trees that
# feed them (source_intake, data_extraction, signal_extraction).
def build_field_usage():
    packets = iter_json_files("working", "source_intake", "packets")
    packets_skel = iter_json_files("working", "source_intake", "skeleton_batches", recursive=True)
    records = iter_json_files("working", "data_extraction", "records")
    records_skel = iter_json_files("working", "data_extraction", "skeleton_batches", recursive=True)
    cards = iter_json_files("working", "signal_extraction", "cards")
    cards_skel = iter_json_files("working", "signal_extraction", "skeleton_batches", recursive=True)

    field_usage = {}

    def merge(field, *usages):
        combined = field_usage.setdefault(field, {})
        for usage in usages:
            for value, files in usage.items():
                combined.setdefault(value, set()).update(files)

    # packets carry pre-triage `possible_actor_levels` / `possible_metric_types`
    # candidate lists -- their own local schema enum (source_packet.schema.json),
    # not the vocab-governed `actor` / `metric_type` fields (vocab_check.py's
    # own discovery mode reports both as unconfigured against any vocab field).
    # Not probed here; only the post-triage `actor_level` / `metric_type` on
    # records and cards are.
    merge(
        "actor",
        collect_scalar(records, "actor_level"),
        collect_scalar(records_skel, "actor_level"),
        collect_scalar(cards, "actor_level"),
        collect_scalar(cards_skel, "actor_level"),
    )
    merge(
        "source_type",
        collect_scalar(packets, "source_type"),
        collect_scalar(packets_skel, "source_type"),
        collect_scalar(records, "source_type"),
        collect_scalar(records_skel, "source_type"),
    )
    merge(
        "metric_type",
        collect_scalar(records, "metric_type"),
        collect_scalar(records_skel, "metric_type"),
        collect_scalar(cards, "metric_type"),
        collect_scalar(cards_skel, "metric_type"),
    )
    merge(
        "product_type_if_explicit",
        collect_scalar(records, "product_type_if_explicit"),
        collect_scalar(records_skel, "product_type_if_explicit"),
        collect_scalar(cards, "product_type_if_explicit"),
        collect_scalar(cards_skel, "product_type_if_explicit"),
    )
    merge(
        "evidence_role",
        collect_scalar(records, "evidence_role"),
        collect_scalar(records_skel, "evidence_role"),
        collect_scalar(cards, "evidence_role"),
        collect_scalar(cards_skel, "evidence_role"),
    )
    merge(
        "uncertainties",
        collect_scalar(packets, "uncertainties"),
        collect_scalar(packets_skel, "uncertainties"),
        collect_scalar(records, "uncertainties"),
        collect_scalar(records_skel, "uncertainties"),
        collect_scalar(cards, "uncertainties"),
        collect_scalar(cards_skel, "uncertainties"),
    )
    merge(
        "claim_type",
        collect_scalar(records, "claim_type"),
        collect_scalar(records_skel, "claim_type"),
    )
    merge(
        "retrieval_method",
        collect_scalar(packets, "retrieval_method"),
        collect_scalar(packets_skel, "retrieval_method"),
    )
    merge(
        "priority_for_source_first",
        collect_scalar(packets, "priority_for_source_first"),
        collect_scalar(packets_skel, "priority_for_source_first"),
    )
    merge(
        "traceability_status",
        collect_scalar(packets, "traceability_status"),
        collect_scalar(packets_skel, "traceability_status"),
    )
    merge(
        "pointer_type",
        collect_nested_pointer_type(records, "traceability_pointer", is_array=False),
        collect_nested_pointer_type(records_skel, "traceability_pointer", is_array=False),
        collect_nested_pointer_type(cards, "traceability_pointers", is_array=True),
        collect_nested_pointer_type(cards_skel, "traceability_pointers", is_array=True),
    )

    counts = {
        "packets": len(packets), "packets_skeletons": len(packets_skel),
        "records": len(records), "records_skeletons": len(records_skel),
        "cards": len(cards), "cards_skeletons": len(cards_skel),
    }
    return field_usage, counts


def main():
    vocab = load_vocab()
    field_usage, counts = build_field_usage()

    print("=" * 78)
    print("VOCAB USAGE CHECK — corpus usage vs pipeline_vocabulary.yaml (D-282(b)/P-191)")
    print("=" * 78)
    print(f"Corpus scanned: packets={counts['packets']} "
          f"(+{counts['packets_skeletons']} skeletons), "
          f"records={counts['records']} (+{counts['records_skeletons']} skeletons), "
          f"cards={counts['cards']} (+{counts['cards_skeletons']} skeletons)")
    print()

    has_issues = False

    for field_name in sorted(field_usage):
        entry = vocab.get(field_name)
        if not isinstance(entry, dict):
            print(f"[{field_name}] WARNING: not declared in pipeline_vocabulary.yaml at all "
                  f"— every used value is missing.")
            has_issues = True
            continue

        declared = vocab_values(entry)
        usage = field_usage[field_name]
        used_values = set(usage)
        missing = used_values - declared

        if field_name in EXCEPTIONS:
            if missing:
                print(f"[{field_name}] EXCEPTION applied — {len(missing)} value(s) not in "
                      f"vocabulary, not gated: {sorted(missing)}")
                print(f"    reason: {EXCEPTIONS[field_name]}")
            continue

        if missing:
            has_issues = True
            print(f"[{field_name}] MISSING FROM VOCABULARY:")
            for v in sorted(missing):
                files = sorted(usage[v])
                sample = ", ".join(files[:3]) + (f", … (+{len(files) - 3} more)" if len(files) > 3 else "")
                print(f"    '{v}' — used in {len(files)} file(s): {sample}")
        else:
            print(f"[{field_name}] OK — {len(used_values)} distinct value(s) used, all in vocabulary")

    print()
    if has_issues:
        print("FAIL: at least one corpus-used value is missing from pipeline_vocabulary.yaml.")
        return 1
    print("PASS: every value used anywhere in the corpus is declared in pipeline_vocabulary.yaml.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
