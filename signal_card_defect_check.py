#!/usr/bin/env python3
"""
signal_card_defect_check.py

Deterministic mechanical defect detector for Signal Cards (Phase 2 output).
New standalone script, no relation to the pipeline: reads Signal Cards and
their source Extraction Records, reports defects, writes nothing, decides
nothing. Same pattern as vocab_check.py at the repo root — deterministic,
runs in seconds, produces a readable report, does not modify any data.

Source of the check definitions: task instructions given directly to the
operator (no Blueprint document exists in the repo or was made available for
this task; Phase 2's `phases/02-signal-extraction/modules/signal_converter.md`
and `phases/02-signal-extraction/contracts/signal_extraction_validator.md`
were read only to confirm field names/semantics, not to derive thresholds).

Four checks, all mechanical (no judgment, no field-filling):

  1. qualifier_overfill        — a local_qualifiers entry reads as source
                                  content (a claim, a policy clause) rather
                                  than a scope-limiting condition. Signal:
                                  character length and sentence count.
  2. time_scope_contamination  — time_scope_raw is non-null but does not
                                  appear verbatim in the source snippet.
                                  Likely bled in from record metadata
                                  (e.g. source_date_if_available).
  3. partial_discreteness      — the snippet contains 2+ distinct numeric
                                  facts and the card expresses only one,
                                  with no sibling split card and no
                                  normalization_notes entry.
  4. time_scope_loss           — inverse of (2): time_scope_raw is null but
                                  the snippet contains recognizable temporal
                                  wording. Possible over-correction dropping
                                  a legitimate value instead of just
                                  quarantining a contaminated one.

Flags are reported per card with the evidence fragment that triggered them.
This script never decides whether a flag is a true defect — that judgment,
especially for check 3 (does the second claim deserve its own card?), is the
operator's. False positives on check 3 in particular are expected and are
not a failure of the corpus or the script.

Usage:
    python signal_card_defect_check.py
        Runs against the real pipeline output:
        working/signal_extraction/cards/*.json
        working/data_extraction/records/*.json

    python signal_card_defect_check.py --fixtures
        Runs against the calibration fixture set in
        signal_card_defect_check_fixtures/{cards,records}/ and additionally
        checks the fixture results against the hardcoded gate expectations
        in EXPECTED_GATE below (see "Calibration gate" section of the
        report).

    python signal_card_defect_check.py --cards-dir DIR --records-dir DIR
        Runs against an arbitrary card/record pair of directories.
"""

import argparse
import json
import re
import statistics
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DEFAULT_CARDS_DIR = ROOT / "working" / "signal_extraction" / "cards"
DEFAULT_RECORDS_DIR = ROOT / "working" / "data_extraction" / "records"
FIXTURES_CARDS_DIR = ROOT / "signal_card_defect_check_fixtures" / "cards"
FIXTURES_RECORDS_DIR = ROOT / "signal_card_defect_check_fixtures" / "records"


# ---------------------------------------------------------------------------
# Thresholds — named constants, not inlined, per the task's explicit
# instruction not to invent defaults. Derivation is documented next to each
# one. CAVEAT, still true as of this writing even though real cards now exist
# on disk: these thresholds were derived from the calibration fixture set
# (signal_card_defect_check_fixtures/), which is small and synthetic by
# construction (it was built to reproduce three known defect patterns plus
# hand-picked negatives), not sampled from production data. The real corpus
# in working/signal_extraction/cards/ was formulated under the corrected
# Stage 2 rules, so it contains no confirmed qualifier-overfill defects to
# calibrate against either — a real run producing zero qualifier_overfill
# flags is not itself calibration data, just an absence of known-bad
# examples. The script prints the live qualifier-length/sentence-count
# distribution and a +/-50% sensitivity table on every run (see
# report_qualifier_distribution) so recalibration is immediate and visible
# whenever a real defective example turns up, rather than requiring a code
# change to discover.

# QUALIFIER_MAX_CHARS: NOT CALIBRATED AGAINST REAL DEFECT DATA. In the
# calibration negatives (well-formed qualifiers, e.g. "in the US", "for shops
# with more than $10,000 in annual revenue"), length ranges 9-53 characters.
# In the calibration positives (a comparative claim sentence, two full policy
# paragraphs), length is 180+ characters. Set at 90: roughly 1.7x the longest
# observed legitimate qualifier, and
# less than half the shortest observed defective one.
QUALIFIER_MAX_CHARS = 90

# QUALIFIER_MAX_SENTENCES: a scope-limiting qualifier is a phrase, not an
# independent clause, and should not span more than one sentence. This
# catches multi-sentence policy-paragraph qualifiers even in the case where
# a single instance is (implausibly) short enough to dodge the length
# threshold. Set at 1: more than one sentence-ending mark is already outside
# what any calibration negative does (all negatives are 0-1 sentence
# fragments with no internal terminal punctuation).
QUALIFIER_MAX_SENTENCES = 1

# DISCRETENESS_MIN_DIGITS: minimum digit count (after stripping commas/%)
# for a numeric token in the snippet to be treated as a candidate discrete
# fact. Sub-2-digit figures (single digits, e.g. "6" in "first 6 months")
# are excluded to reduce noise from incidental counts that are not
# plausible standalone claims. This is a documented simplification: it will
# miss genuinely discrete single-digit claims. That is an accepted
# trade-off given check 3 is explicitly allowed to both over- and
# under-fire (false positives are expected; this constant only trims some
# of the noise, it does not eliminate it).
DISCRETENESS_MIN_DIGITS = 2

SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+")
NUMERIC_TOKEN_RE = re.compile(r"\d[\d,]*(?:\.\d+)?%?")
QUOTE_CHARS = "\"'“”‘’"

# TEMPORAL_PATTERNS: heuristic keyword/pattern list for check 4, not an
# exhaustive grammar of temporal expression. Deliberately narrow (explicit
# months, explicit years, explicit update/recency phrasing) to avoid
# treating duration qualifiers ("first 6 months") as temporal signals —
# those are qualifiers, not time_scope. False negatives (temporal wording
# phrased in a way this list doesn't recognize) are possible and are a
# known limitation, not silently claimed to be covered.
#
# Month names are matched case-sensitively (capitalized, as a calendar month
# normally appears in prose) and kept in a separate pattern from the rest:
# a case-insensitive match on "May" also matches the common auxiliary verb
# "may" ("charges may apply"), which is not a temporal signal. Caught during
# calibration (SC-FX-003 false-fired on "may apply").
MONTH_RE = re.compile(
    r"\b(January|February|March|April|May|June|July|August|September|October|November|December)\b"
)
TEMPORAL_PATTERNS = [
    r"\b(19|20)\d{2}\b",
    r"\bas of\b",
    r"\bcurrent as of\b",
    r"\blast updated\b",
    r"\bsince\s+\w+\s+\d{4}\b",
    r"\b(daily|weekly|monthly|quarterly|annually)\b",
]
TEMPORAL_RE = re.compile("|".join(TEMPORAL_PATTERNS), re.IGNORECASE)


# ---------------------------------------------------------------------------
# Calibration gate — expected outcomes for the synthetic fixture set. Only
# meaningful against signal_card_defect_check_fixtures/, never against real
# cards. This is a self-test of the detector (does it fire where it must,
# stay silent where it must not), not a corpus-level accept/reject
# judgment: the fixtures' expected defects are known by construction
# because this script's author wrote them to reproduce specific patterns.
EXPECTED_GATE = {
    "SC-FX-001": {"partial_discreteness"},
    "SC-FX-002": {"qualifier_overfill"},
    "SC-FX-003": {"qualifier_overfill"},
    "SC-FX-004": {"time_scope_loss"},
    "SC-FX-005": {"time_scope_contamination"},
    "SC-FX-N01": set(),
    "SC-FX-N02": set(),
    "SC-FX-N03": set(),
    "SC-FX-N04A": set(),
    "SC-FX-N04B": set(),
    "SC-FX-N05": set(),
}
# The three cases named in the task as the required calibration gate
# (human-audited defects from batch_001 corrida 1): SC-R1-003 (discreteness),
# SC-R1-002 (comparative claim in local_qualifiers), SC-R1-022 (DDP/DDU
# paragraphs in local_qualifiers). They are reproduced here as SC-FX-001,
# SC-FX-002, SC-FX-003 respectively, since the real cards (corrida 2) no
# longer carry these defects and are not usable as known-positives.
REQUIRED_GATE_IDS = {"SC-FX-001", "SC-FX-002", "SC-FX-003"}


def count_sentences(text):
    parts = SENTENCE_SPLIT_RE.split(text.strip())
    return len([p for p in parts if p.strip()])


def normalize_snippet_text(text):
    if not text:
        return ""
    stripped = text.strip().strip(QUOTE_CHARS).strip()
    return re.sub(r"\s+", " ", stripped)


def numeric_tokens(text):
    tokens = set()
    for match in NUMERIC_TOKEN_RE.finditer(text or ""):
        digits = match.group(0).rstrip("%").replace(",", "")
        if len(digits) >= DISCRETENESS_MIN_DIGITS:
            tokens.add(digits)
    return tokens


def load_json_dir(directory):
    items = {}
    errors = []
    if not directory.exists():
        return items, errors
    for path in sorted(directory.glob("*.json")):
        try:
            with path.open(encoding="utf-8") as f:
                items[path.stem] = json.load(f)
        except (OSError, json.JSONDecodeError) as e:
            errors.append(f"{path}: {e}")
    return items, errors


def snippet_text_for_record(record):
    parts = [
        record.get("snippet_context_before"),
        record.get("snippet_primary"),
        record.get("snippet_context_after"),
    ]
    return " ".join(normalize_snippet_text(p) for p in parts if p)


def card_own_text(card):
    """All text fields the card itself could carry a fact in."""
    parts = []
    for field in ("signal_text", "subject_exact", "time_scope_raw", "time_scope_normalized_if_safe"):
        val = card.get(field)
        if isinstance(val, str):
            parts.append(val)
    for field in ("local_qualifiers", "normalization_notes", "extraction_notes"):
        for val in card.get(field) or []:
            if isinstance(val, str):
                parts.append(val)
    mv = card.get("metric_value_raw")
    if mv is not None:
        parts.append(str(mv))
    return " ".join(parts)


def check_qualifier_overfill(card, snippet_text):
    flags = []
    for i, qualifier in enumerate(card.get("local_qualifiers") or []):
        if not isinstance(qualifier, str):
            continue
        length = len(qualifier)
        sentences = count_sentences(qualifier)
        if length > QUALIFIER_MAX_CHARS or sentences > QUALIFIER_MAX_SENTENCES:
            flags.append({
                "defect": "qualifier_overfill",
                "evidence": qualifier[:200] + ("..." if len(qualifier) > 200 else ""),
                "measured": f"length={length} chars (threshold {QUALIFIER_MAX_CHARS}), "
                            f"sentences={sentences} (threshold {QUALIFIER_MAX_SENTENCES})",
                "index": i,
            })
    return flags


def check_time_scope_contamination(card, snippet_text):
    raw = card.get("time_scope_raw")
    if not raw or not isinstance(raw, str):
        return []
    normalized_raw = re.sub(r"\s+", " ", raw.strip())
    if normalized_raw.lower() in snippet_text.lower():
        return []
    return [{
        "defect": "time_scope_contamination",
        "evidence": raw,
        "measured": "not found verbatim in snippet_primary/context",
    }]


def check_time_scope_loss(card, snippet_text):
    if card.get("time_scope_raw"):
        return []
    match = TEMPORAL_RE.search(snippet_text) or MONTH_RE.search(snippet_text)
    if not match:
        return []
    return [{
        "defect": "time_scope_loss",
        "evidence": snippet_text[max(0, match.start() - 30):match.end() + 30],
        "measured": f"time_scope_raw=null, matched temporal pattern: '{match.group(0)}'",
    }]


def check_partial_discreteness(card, snippet_text, sibling_cards):
    if not snippet_text:
        return []
    snippet_numbers = numeric_tokens(snippet_text)
    if len(snippet_numbers) < 2:
        return []
    own_text = card_own_text(card)
    own_numbers = numeric_tokens(own_text)
    missing = snippet_numbers - own_numbers
    if not missing:
        return []
    if card.get("normalization_notes"):
        return []
    source_ids = set(card.get("source_record_ids") or [])
    for other in sibling_cards:
        if other.get("signal_id") == card.get("signal_id"):
            continue
        if not source_ids.intersection(other.get("source_record_ids") or []):
            continue
        other_numbers = numeric_tokens(card_own_text(other))
        missing -= other_numbers
    if not missing:
        return []
    return [{
        "defect": "partial_discreteness",
        "evidence": f"snippet contains numeric facts {sorted(snippet_numbers)}; "
                    f"card/siblings do not express {sorted(missing)}",
        "measured": f"{len(snippet_numbers)} distinct numeric facts in snippet, "
                    f"{len(missing)} unexpressed, no split sibling, no normalization_notes",
    }]


def run_checks(cards_by_id, records_by_id):
    all_cards = list(cards_by_id.values())
    results = {}
    missing_records = []
    for signal_id, card in cards_by_id.items():
        source_record_ids = card.get("source_record_ids") or []
        snippet_parts = []
        for rid in source_record_ids:
            record = records_by_id.get(rid)
            if record is None:
                missing_records.append((signal_id, rid))
                continue
            snippet_parts.append(snippet_text_for_record(record))
        snippet_text = " ".join(snippet_parts)

        flags = []
        flags += check_qualifier_overfill(card, snippet_text)
        flags += check_time_scope_contamination(card, snippet_text)
        flags += check_time_scope_loss(card, snippet_text)
        flags += check_partial_discreteness(card, snippet_text, all_cards)
        results[signal_id] = flags
    return results, missing_records


def report_qualifier_distribution(cards_by_id):
    lengths = []
    sentence_counts = []
    for card in cards_by_id.values():
        for qualifier in card.get("local_qualifiers") or []:
            if isinstance(qualifier, str):
                lengths.append(len(qualifier))
                sentence_counts.append(count_sentences(qualifier))

    print("-" * 78)
    print("QUALIFIER LENGTH / SENTENCE-COUNT DISTRIBUTION (this run)")
    print("-" * 78)
    if not lengths:
        print("(no local_qualifiers entries found in this card set)")
        print()
        return

    def stats_line(label, values):
        print(f"  {label}: n={len(values)} min={min(values)} max={max(values)} "
              f"mean={statistics.mean(values):.1f} median={statistics.median(values)}")

    stats_line("char length", lengths)
    stats_line("sentence count", sentence_counts)
    print()

    print(f"  Threshold sensitivity (QUALIFIER_MAX_CHARS={QUALIFIER_MAX_CHARS}, "
          f"+/-50%):")
    for label, factor in (("-50%", 0.5), ("current", 1.0), ("+50%", 1.5)):
        threshold = QUALIFIER_MAX_CHARS * factor
        flagged = sum(1 for l in lengths if l > threshold)
        print(f"    {label:>8} (>{threshold:.0f} chars): {flagged}/{len(lengths)} qualifiers flagged")
    print()
    print(f"  Threshold sensitivity (QUALIFIER_MAX_SENTENCES={QUALIFIER_MAX_SENTENCES}, "
          f"+/-50%, rounded):")
    for label, factor in (("-50%", 0.5), ("current", 1.0), ("+50%", 1.5)):
        threshold = max(1, round(QUALIFIER_MAX_SENTENCES * factor))
        flagged = sum(1 for s in sentence_counts if s > threshold)
        print(f"    {label:>8} (>{threshold} sentences): {flagged}/{len(sentence_counts)} qualifiers flagged")
    print()


def print_card_report(results, cards_by_id):
    print("-" * 78)
    print("PER-CARD FLAGS")
    print("-" * 78)
    any_flags = False
    for signal_id in sorted(results):
        flags = results[signal_id]
        if not flags:
            continue
        any_flags = True
        print(f"\n[{signal_id}]")
        for flag in flags:
            print(f"  defect: {flag['defect']}")
            print(f"  evidence: {flag['evidence']}")
            print(f"  measured: {flag['measured']}")
    if not any_flags:
        print("(no flags)")
    print()


def print_summary(results):
    counts = defaultdict(int)
    for flags in results.values():
        for flag in flags:
            counts[flag["defect"]] += 1
    print("-" * 78)
    print("SUMMARY — counts by defect type")
    print("-" * 78)
    print(f"  Cards processed: {len(results)}")
    print(f"  Cards with >=1 flag: {sum(1 for f in results.values() if f)}")
    for defect in ("qualifier_overfill", "time_scope_contamination",
                   "partial_discreteness", "time_scope_loss"):
        print(f"  {defect}: {counts.get(defect, 0)}")
    print()


def print_gate(results):
    print("=" * 78)
    print("CALIBRATION GATE (signal_card_defect_check_fixtures/ only)")
    print("=" * 78)
    all_pass = True
    required_pass = True
    for signal_id in sorted(EXPECTED_GATE):
        expected = EXPECTED_GATE[signal_id]
        actual = {f["defect"] for f in results.get(signal_id, [])}
        ok = expected.issubset(actual) if expected else not actual
        status = "PASS" if ok else "FAIL"
        if not ok:
            all_pass = False
            if signal_id in REQUIRED_GATE_IDS:
                required_pass = False
        note = ""
        if not expected and actual:
            note = f" (unexpected extra flags: {sorted(actual)})"
        elif expected and not expected.issubset(actual):
            note = f" (expected {sorted(expected)}, got {sorted(actual)})"
        print(f"  [{status}] {signal_id}: expected={sorted(expected) or 'none'}{note}")
    print()
    print(f"  Required 3-case gate (SC-R1-003 / SC-R1-002 / SC-R1-022 pattern "
          f"reproductions): {'PASS' if required_pass else 'FAIL'}")
    print(f"  Full fixture gate (positives + negatives): {'PASS' if all_pass else 'FAIL'}")
    print()
    return all_pass


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--cards-dir", type=Path, default=None)
    parser.add_argument("--records-dir", type=Path, default=None)
    parser.add_argument("--fixtures", action="store_true",
                         help="Run against signal_card_defect_check_fixtures/ and check the calibration gate")
    args = parser.parse_args()

    if args.fixtures:
        cards_dir = FIXTURES_CARDS_DIR
        records_dir = FIXTURES_RECORDS_DIR
    else:
        cards_dir = args.cards_dir or DEFAULT_CARDS_DIR
        records_dir = args.records_dir or DEFAULT_RECORDS_DIR

    print("=" * 78)
    print("SIGNAL CARD DEFECT CHECK")
    print("=" * 78)
    print(f"Cards dir:   {cards_dir}")
    print(f"Records dir: {records_dir}")
    print()

    cards_by_id, card_errors = load_json_dir(cards_dir)
    records_by_id, record_errors = load_json_dir(records_dir)

    for e in card_errors:
        print(f"WARNING: could not parse card {e}", file=sys.stderr)
    for e in record_errors:
        print(f"WARNING: could not parse record {e}", file=sys.stderr)

    if not cards_by_id:
        print("No cards found in cards dir. Nothing to check.")
        if args.fixtures:
            sys.exit(1)
        sys.exit(0)

    results, missing_records = run_checks(cards_by_id, records_by_id)

    if missing_records:
        print("-" * 78)
        print("MISSING SOURCE RECORDS (card references a source_record_id with no matching file)")
        print("-" * 78)
        for signal_id, rid in missing_records:
            print(f"  {signal_id} -> {rid}")
        print()

    print_card_report(results, cards_by_id)
    print_summary(results)
    report_qualifier_distribution(cards_by_id)

    if args.fixtures:
        gate_ok = print_gate(results)
        sys.exit(0 if gate_ok else 1)

    sys.exit(0)


if __name__ == "__main__":
    main()
