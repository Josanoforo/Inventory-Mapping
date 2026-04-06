#!/usr/bin/env python3
"""
parse_dg_shard.py — Data Gathering shard parser.

Usage:
    python scripts/parse_dg_shard.py input/data_gathering/shards/<filename>.md

Outputs (written relative to repo root, i.e. the directory two levels above scripts/):
    working/data_gathering/findings/<ID>.json        — one per finding (Part 1 + Part 2)
    working/data_gathering/diagnostics/part_4/<shard_id>_<item_id>.json
    working/data_gathering/diagnostics/qa_notes/<shard_id>_qa.json

Idempotent: re-running produces identical output.
"""

import sys
import re
import json
import os
import urllib.parse
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
FINDINGS_DIR = REPO_ROOT / "working" / "data_gathering" / "findings"
PART4_DIR = REPO_ROOT / "working" / "data_gathering" / "diagnostics" / "part_4"
QA_DIR = REPO_ROOT / "working" / "data_gathering" / "diagnostics" / "qa_notes"

# ---------------------------------------------------------------------------
# Field names expected inside a finding block
# ---------------------------------------------------------------------------

FINDING_FIELDS = [
    "Seller",
    "Product type",
    "AI tool(s)",
    "Workflow claim (What)",
    "Verbatim snippet",
    "Source URL",
    "Source type",
    "Date",
    "Verification state",
    "Notes",
]

# Pre-compiled pattern to detect the start of any bold field label on a line.
# Handles colon/dash either inside the ** markers ("**Seller:**") or outside ("**Seller**:").
_FIELD_LABEL_PAT = re.compile(
    r"^\s*\*\*(" + "|".join(re.escape(f) for f in FINDING_FIELDS) + r")[:\-]?\*\*\s*[:\-]?\s*(.*)",
    re.IGNORECASE,
)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _slug(text: str) -> str:
    """Lower-case, whitespace→underscore, strip non-alphanum/underscore."""
    text = text.strip().lower()
    text = re.sub(r"\s+", "_", text)
    text = re.sub(r"[^\w]", "", text)
    return text


def _extract_urls(text: str) -> list[str]:
    """Return all http/https URLs found in text."""
    return re.findall(r"https?://[^\s\)\]\"']+", text)


def _clean(text: str) -> str:
    """Strip surrounding whitespace and internal consecutive blank lines."""
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def _warn(msg: str) -> None:
    print(f"WARNING: {msg}", file=sys.stderr)


# ---------------------------------------------------------------------------
# Section splitter
# ---------------------------------------------------------------------------

PART_HEADERS = {
    "part1": re.compile(r"^##\s+Part\s+1\b", re.IGNORECASE | re.MULTILINE),
    "part2": re.compile(r"^##\s+Part\s+2\b", re.IGNORECASE | re.MULTILINE),
    "part3": re.compile(r"^##\s+Part\s+3\b", re.IGNORECASE | re.MULTILINE),
    "part4": re.compile(r"^##\s+Part\s+4\b", re.IGNORECASE | re.MULTILINE),
    "qa":    re.compile(r"^##\s+Research\s+QA\s+Notes", re.IGNORECASE | re.MULTILINE),
}


def split_sections(text: str) -> dict[str, str]:
    """Return a dict with keys part1..part4, qa, header."""
    # Collect all match positions
    anchors: list[tuple[int, str]] = []
    for key, pat in PART_HEADERS.items():
        for m in pat.finditer(text):
            anchors.append((m.start(), key))
    anchors.sort()

    sections: dict[str, str] = {}

    # Everything before the first ## Part is the header
    if anchors:
        sections["header"] = text[: anchors[0][0]]
    else:
        sections["header"] = text

    for i, (start, key) in enumerate(anchors):
        end = anchors[i + 1][0] if i + 1 < len(anchors) else len(text)
        sections[key] = text[start:end]

    return sections


# ---------------------------------------------------------------------------
# Header parsing
# ---------------------------------------------------------------------------

def parse_header(header_text: str) -> tuple[str, str]:
    """Return (shard_title, direction_statement)."""
    title = ""
    direction = ""

    m = re.search(r"^#\s+Research\s+Shard\s*[:\-]?\s*(.+)$", header_text, re.MULTILINE | re.IGNORECASE)
    if m:
        title = m.group(1).strip()

    m = re.search(r"\*\*Direction\s+statement\s*[:\-]?\*\*\s*(.+)", header_text, re.IGNORECASE)
    if m:
        direction = m.group(1).strip()

    return title, direction


# ---------------------------------------------------------------------------
# Finding parser (Part 1 and Part 2)
# ---------------------------------------------------------------------------

FINDING_ID_PAT = re.compile(r"^###\s+([A-Z0-9]+-[CP]\d+)", re.MULTILINE | re.IGNORECASE)


def parse_findings(section_text: str, part_number: int, shard_id: str) -> list[dict]:
    """Parse all findings in a Part 1 or Part 2 section."""
    findings: list[dict] = []

    # Split on ### <ID> headers
    splits = list(FINDING_ID_PAT.finditer(section_text))
    if not splits:
        return findings

    for i, m in enumerate(splits):
        finding_id = m.group(1).strip()
        block_start = m.end()
        block_end = splits[i + 1].start() if i + 1 < len(splits) else len(section_text)
        block = section_text[block_start:block_end]

        try:
            record = _parse_finding_block(block)
        except Exception as exc:
            _warn(f"Could not parse finding {finding_id}: {exc}")
            continue

        record["finding_id"] = finding_id
        record["shard_id"] = shard_id
        record["part"] = part_number
        # Ensure verification_state is present at top level even if already in record
        if "verification_state" not in record:
            record["verification_state"] = ""
        findings.append(record)

    return findings


def _parse_finding_block(block: str) -> dict:
    """Extract bold-label fields from a finding block using line-by-line accumulation."""
    record: dict = {}
    current_key: str | None = None
    current_lines: list[str] = []

    def _flush():
        if current_key is not None:
            record[current_key] = _clean("\n".join(current_lines))

    for line in block.splitlines():
        m = _FIELD_LABEL_PAT.match(line)
        if m:
            _flush()
            current_key = _slug(m.group(1))
            current_lines = [m.group(2).strip()]
        else:
            if current_key is not None:
                current_lines.append(line)

    _flush()
    return record


# ---------------------------------------------------------------------------
# Part 4 parser
# ---------------------------------------------------------------------------

# Item header: **4-01. Seller name** or **4-01. Subject**
PART4_ITEM_PAT = re.compile(
    r"\*\*(\d+-\d+)\.\s+([^\*]+)\*\*", re.MULTILINE
)
ATTEMPTED_PAT = re.compile(r"Attempted\s*[:\-]\s*(.*?)(?=Why\s+failed|$)", re.IGNORECASE | re.DOTALL)
WHY_FAILED_PAT = re.compile(r"Why\s+failed\s*[:\-]\s*(.*?)$", re.IGNORECASE | re.DOTALL)


def parse_part4(section_text: str, shard_id: str) -> list[dict]:
    items: list[dict] = []

    splits = list(PART4_ITEM_PAT.finditer(section_text))
    if not splits:
        return items

    for i, m in enumerate(splits):
        raw_num = m.group(1).strip()       # e.g. "4-01"
        subject = m.group(2).strip()
        block_start = m.end()
        block_end = splits[i + 1].start() if i + 1 < len(splits) else len(section_text)
        block = section_text[block_start:block_end]

        item_id = raw_num  # "4-01"

        attempted = ""
        ma = ATTEMPTED_PAT.search(block)
        if ma:
            attempted = _clean(ma.group(1))

        why_failed = ""
        mw = WHY_FAILED_PAT.search(block)
        if mw:
            why_failed = _clean(mw.group(1))

        if not attempted and not why_failed:
            _warn(f"Part 4 item {item_id} ({subject}): could not extract Attempted/Why failed — storing raw block")
            attempted = _clean(block)

        urls = _extract_urls(block)

        items.append(
            {
                "shard_id": shard_id,
                "item_id": item_id,
                "seller_or_subject": subject,
                "attempted": attempted,
                "why_failed": why_failed,
                "urls_mentioned": urls,
            }
        )

    return items


# ---------------------------------------------------------------------------
# QA Notes parser
# ---------------------------------------------------------------------------

# Each subsection starts with ### or a bold line that acts as a heading
QA_SUBSECTION_PAT = re.compile(
    r"^(?:###\s+(.+)|[-–]\s*\*\*([^\*]+)\*\*\s*[:\-]?\s*(.*))", re.MULTILINE
)

# Known section title → canonical key mapping (partial, for normalization)
_QA_KEY_MAP: dict[str, str] = {
    "findings forced to provisional": "findings_forced_to_provisional",
    "findings degraded to could not verify": "findings_degraded_to_could_not_verify",
    "multi-speaker pages split": "multi_speaker_pages_split",
    "multi speaker pages split": "multi_speaker_pages_split",
    "source type distribution": "source_type_distribution",
    "source_type distribution": "source_type_distribution",
    "categories expected no findings": "categories_expected_no_findings",
    "gumroad store verification gap": "gumroad_store_verification_gap",
    "medium access barriers": "medium_access_barriers",
    "yield vs expected shape": "yield_vs_expected_shape",
    "yield vs. expected shape": "yield_vs_expected_shape",
    "yield": "yield_vs_expected_shape",
    "gaps by category": "categories_expected_no_findings",
}


def _canonical_qa_key(title: str) -> str:
    slug = title.strip().lower()
    # Try exact map
    if slug in _QA_KEY_MAP:
        return _QA_KEY_MAP[slug]
    # Partial match
    for pattern, canonical in _QA_KEY_MAP.items():
        if pattern in slug:
            return canonical
    # Fallback: slugify
    return _slug(title)


def parse_qa_notes(section_text: str, shard_id: str) -> dict:
    """Parse QA Notes section into a flat dict of sections."""
    record: dict = {"shard_id": shard_id}

    # Split into subsections by ### headings
    subsection_re = re.compile(r"^(#{2,4})\s+(.+)$", re.MULTILINE)
    splits = list(subsection_re.finditer(section_text))

    if not splits:
        # No subsections — try bold bullet items
        record.update(_parse_qa_bullet_style(section_text))
        return record

    # Skip the first match if it's the ## Research QA Notes header itself
    start_idx = 0
    if splits and re.match(r"Research\s+QA\s+Notes", splits[0].group(2), re.IGNORECASE):
        start_idx = 1

    for i in range(start_idx, len(splits)):
        title = splits[i].group(2).strip()
        content_start = splits[i].end()
        content_end = splits[i + 1].start() if i + 1 < len(splits) else len(section_text)
        content = _clean(section_text[content_start:content_end])
        key = _canonical_qa_key(title)
        record[key] = content

    return record


def _parse_qa_bullet_style(text: str) -> dict:
    """Fallback: parse **Bold label:** value lines."""
    result: dict = {}
    pat = re.compile(r"\*\*([^\*]+)\*\*\s*[:\-]\s*(.*?)(?=\*\*[^\*]+\*\*|\Z)", re.DOTALL)
    for m in pat.finditer(text):
        key = _canonical_qa_key(m.group(1))
        value = _clean(m.group(2))
        result[key] = value
    return result


# ---------------------------------------------------------------------------
# Writer
# ---------------------------------------------------------------------------

def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main(shard_path: str) -> None:
    p = Path(shard_path).resolve()
    if not p.exists():
        print(f"ERROR: file not found: {p}", file=sys.stderr)
        sys.exit(1)

    text = p.read_text(encoding="utf-8")

    # Derive shard_id from filename stem (e.g. "DX-2_gumroad" → "DX-2_gumroad")
    shard_id = p.stem

    sections = split_sections(text)

    # Parse findings
    findings_written = 0
    for part_num, section_key in [(1, "part1"), (2, "part2")]:
        sec = sections.get(section_key, "")
        if not sec:
            continue
        for finding in parse_findings(sec, part_num, shard_id):
            fid = finding.get("finding_id", "UNKNOWN")
            out_path = FINDINGS_DIR / f"{fid}.json"
            write_json(out_path, finding)
            findings_written += 1

    # Parse Part 4
    part4_written = 0
    sec4 = sections.get("part4", "")
    if sec4:
        for item in parse_part4(sec4, shard_id):
            item_id_clean = item["item_id"].replace("-", "-")  # already clean
            filename = f"{shard_id}_{item_id_clean}.json"
            out_path = PART4_DIR / filename
            write_json(out_path, item)
            part4_written += 1

    # Parse QA Notes
    qa_written = 0
    sec_qa = sections.get("qa", "")
    if sec_qa:
        qa_record = parse_qa_notes(sec_qa, shard_id)
        qa_keys = len(qa_record) - 1  # subtract shard_id itself
        out_path = QA_DIR / f"{shard_id}_qa.json"
        write_json(out_path, qa_record)
        qa_written = 1
    else:
        qa_keys = 0

    print(
        f"Done — shard: {shard_id} | findings: {findings_written} | part4 items: {part4_written} | qa file: {qa_written} ({qa_keys} sections)"
    )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <shard.md>", file=sys.stderr)
        sys.exit(1)
    main(sys.argv[1])
