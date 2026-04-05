#!/usr/bin/env python3
"""
URL Normalization — execution script.

Reads card_index.jsonl, applies the 4 strict pattern rules defined in
url_normalization_design.md, and writes normalized_source_refs.jsonl.

Non-destructive: card_index.jsonl is never modified.
Idempotent: running twice produces identical output.

Implementation note on "segment":
  Sources often carry a human label followed by a URL, separated by
  comma+space, an em/en-dash with spaces, a pipe, or semicolon.
  Rules 2 and 3 (which use anchored patterns) are applied to each
  segment independently. Rule 1 scans the whole string.
"""

import json
import re
import sys
from collections import Counter
from pathlib import Path

# Paths
REPO_ROOT = Path(__file__).resolve().parents[3]
CARD_INDEX = REPO_ROOT / "working" / "index" / "card_index.jsonl"
OUTPUT_FILE = Path(__file__).resolve().parent / "normalized_source_refs.jsonl"

# ── Regex patterns ──────────────────────────────────────────────────────────

# Rule 1: already has a protocol anywhere in the string
RE_HAS_PROTOCOL = re.compile(r'https?://\S+')

# Segment delimiter: comma+space, em/en-dash surrounded by spaces, pipe,
# or semicolon+space. Matches the delimiters used in legacy source strings.
RE_SEG_SPLIT = re.compile(r',\s+|\s+[—–|]\s+|;\s+')

# Rule 2 (anchored): domain immediately at start of segment, followed by
# at least one path component.  Strict pattern from design spec §Rule 2.
RE_DOMAIN_WITH_PATH = re.compile(
    r'^([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}'
    r'(/[^\s,;—()\"\'\u2014]+)'
)

# Rule 3 (anchored): segment is *exactly* a bare domain name, nothing else.
# No URL constructed — a bare domain name is not a stable URL (design §Rule 3).
RE_DOMAIN_ONLY = re.compile(
    r'^([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$'
)


# ── Core classification ──────────────────────────────────────────────────────

def split_segments(source: str) -> list[str]:
    """Return non-empty stripped segments from a source string."""
    return [s.strip() for s in RE_SEG_SPLIT.split(source) if s.strip()]


def classify(source: str) -> dict:
    """
    Apply rules 1–4 from the design spec. Returns the classification fields
    that will be written alongside signal_id and original_source.
    """
    # Rule 1: any protocol already present → extract it, no transformation
    m = RE_HAS_PROTOCOL.search(source)
    if m:
        return {
            "normalized_url": m.group(0),
            "normalization_applied": False,
            "pattern_matched": "https_already_present",
            "normalization_confidence": "strict",
        }

    segments = split_segments(source)

    # Rule 2: domain + path segment, no protocol → prepend https://
    for seg in segments:
        m = RE_DOMAIN_WITH_PATH.match(seg)
        if m:
            return {
                "normalized_url": "https://" + seg,
                "normalization_applied": True,
                "pattern_matched": "https_prepend",
                "normalization_confidence": "strict",
            }

    # Rule 3: bare domain only → record but do NOT construct a URL
    for seg in segments:
        if RE_DOMAIN_ONLY.match(seg):
            return {
                "normalized_url": None,
                "normalization_applied": False,
                "pattern_matched": "domain_name_only",
                "normalization_confidence": "domain_only",
            }

    # Rule 4: no identifiable URL or domain pattern
    return {
        "normalized_url": None,
        "normalization_applied": False,
        "pattern_matched": "url_not_identified",
        "normalization_confidence": "strict",
    }


# ── Main ─────────────────────────────────────────────────────────────────────

def main() -> tuple[list, Counter]:
    if not CARD_INDEX.exists():
        print(f"ERROR: card_index.jsonl not found at {CARD_INDEX}", file=sys.stderr)
        sys.exit(1)

    records: list[dict] = []
    with CARD_INDEX.open(encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            card = json.loads(line)
            result = classify(card.get("source", ""))
            records.append({
                "signal_id": card["id"],
                "original_source": card.get("source", ""),
                **result,
            })

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_FILE.open("w", encoding="utf-8") as fh:
        for rec in records:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")

    counts = Counter(r["pattern_matched"] for r in records)
    print(f"Total records written: {len(records)}")
    for pattern in [
        "https_already_present",
        "https_prepend",
        "domain_name_only",
        "url_not_identified",
    ]:
        print(f"  {pattern}: {counts[pattern]}")

    return records, counts


if __name__ == "__main__":
    main()
