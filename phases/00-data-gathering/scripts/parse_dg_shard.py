#!/usr/bin/env python3
"""
parse_dg_shard.py — Data Gathering shard parser.

Contract authority:
  phases/00-data-gathering/reference/data_gathering_project_instructions_v4_5.md  (DGI-R4 + DGI-R7)
  phases/00-data-gathering/reference/research_directions_protocol.md              (Sections 3, 4, 5, 9)

Usage:
    python phases/00-data-gathering/scripts/parse_dg_shard.py input/data_gathering/shards/<filename>.md

Outputs (written relative to repo root):
    working/data_gathering/findings/<ID>.json               — one per finding (Part 1 + Part 2)
    working/data_gathering/diagnostics/part_4/<shard_id>_<item_id>.json
    working/data_gathering/diagnostics/qa_notes/<shard_id>_qa.json

Idempotent: re-running produces identical output.
"""

import sys
import re
import json
import os
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent.parent
FINDINGS_DIR = REPO_ROOT / "working" / "data_gathering" / "findings"
PART4_DIR = REPO_ROOT / "working" / "data_gathering" / "diagnostics" / "part_4"
QA_DIR = REPO_ROOT / "working" / "data_gathering" / "diagnostics" / "qa_notes"

# ---------------------------------------------------------------------------
# Contract: 8 required fields from DGI-R4
# canonical_key → list of acceptable label spellings (lower-cased, stripped)
# ---------------------------------------------------------------------------

REQUIRED_FIELD_MAP: dict[str, list[str]] = {
    "what":                ["workflow claim (what)", "what", "workflow claim"],
    "verbatim_snippet":    ["verbatim snippet", "verbatim", "snippet"],
    "source":              ["source url", "source"],
    "source_type":         ["source type", "source_type"],
    "verification_status": ["verification status", "verification_status",
                            "verification state", "verification_state",
                            "verification"],
    "date":                ["date"],
    "notes":               ["notes"],
}

# Reverse map: label → canonical key
_LABEL_TO_CANONICAL: dict[str, str] = {}
for _canon, _variants in REQUIRED_FIELD_MAP.items():
    for _v in _variants:
        _LABEL_TO_CANONICAL[_v] = _canon

REQUIRED_KEYS = set(REQUIRED_FIELD_MAP.keys())

# Regex: match field label at start of a line.
# Handles both bold ("**Label:**", "**Label**:") and plain ("Label:") formats.
# Bold markers are fully optional — both formats are valid per contract.
_FIELD_LABEL_PAT = re.compile(
    r"^\s*(?:[-*]\s+)?(?:\*\*)?([A-Za-z][A-Za-z0-9_ ()/]+?)(?:\*\*)?[:\-](?:\*\*)?\s*(.*)",
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


def _canonical_key(raw_label: str) -> tuple[str, bool]:
    """
    Return (canonical_key, is_required).
    Falls back to slugified label if not in REQUIRED_FIELD_MAP.
    """
    probe = raw_label.strip().lower()
    if probe in _LABEL_TO_CANONICAL:
        return _LABEL_TO_CANONICAL[probe], True
    return _slug(raw_label), False


def _extract_urls(text: str) -> list[str]:
    """Return all http/https URLs found in text."""
    return re.findall(r"https?://[^\s\)\]\"']+", text)


def _clean(text: str) -> str:
    """Strip surrounding whitespace, remove trailing horizontal rules, collapse blank lines."""
    text = re.sub(r"\n{3,}", "\n\n", text)
    # Remove trailing --- separators (Markdown HR)
    text = re.sub(r"\n---\s*$", "", text.strip())
    return text.strip()


def _warn(msg: str) -> None:
    print(f"WARNING: {msg}", file=sys.stderr)


# ---------------------------------------------------------------------------
# Section splitter
# ---------------------------------------------------------------------------

PART_HEADERS = {
    "part1":  re.compile(r"^#{0,3}\s*(?:\d+\s*[.·•]\s*)?Part\s+1\b", re.IGNORECASE | re.MULTILINE),
    "part1b": re.compile(r"^#{0,3}\s*(?:\d+\s*[.·•]\s*)?Part\s+1\s*B\b", re.IGNORECASE | re.MULTILINE),
    "part2":  re.compile(r"^#{0,3}\s*(?:\d+\s*[.·•]\s*)?Part\s+2\b", re.IGNORECASE | re.MULTILINE),
    "part2b": re.compile(r"^#{0,3}\s*(?:\d+\s*[.·•]\s*)?Part\s+2\s*B\b", re.IGNORECASE | re.MULTILINE),
    "part3":  re.compile(r"^#{0,3}\s*(?:\d+\s*[.·•]\s*)?Part\s+3\b", re.IGNORECASE | re.MULTILINE),
    "part4":  re.compile(r"^#{0,3}\s*(?:\d+\s*[.·•]\s*)?Part\s+4\b", re.IGNORECASE | re.MULTILINE),
    "qa":     re.compile(r"^#{0,3}\s*(?:\d+\s*[.·•]\s*)?Research\s+QA\s+Notes", re.IGNORECASE | re.MULTILINE),
}


def split_sections(text: str) -> dict[str, str]:
    """Return dict with keys part1..part4, qa, header."""
    anchors: list[tuple[int, str]] = []
    for key, pat in PART_HEADERS.items():
        for m in pat.finditer(text):
            anchors.append((m.start(), key))
    anchors.sort()

    sections: dict[str, str] = {}
    if anchors:
        sections["header"] = text[: anchors[0][0]]
    else:
        sections["header"] = text

    for i, (start, key) in enumerate(anchors):
        end = anchors[i + 1][0] if i + 1 < len(anchors) else len(text)
        if key not in sections:  # only use first occurrence; ignore duplicates in prose
            sections[key] = text[start:end]

    return sections


# ---------------------------------------------------------------------------
# Header parsing
# ---------------------------------------------------------------------------

def parse_header(header_text: str) -> tuple[str, str]:
    """Return (shard_title, direction_statement)."""
    title = ""
    direction = ""

    m = re.search(r"^#\s+Research\s+Shard\s*[:\-]?\s*(.+)$", header_text,
                  re.MULTILINE | re.IGNORECASE)
    if m:
        title = m.group(1).strip()

    m = re.search(r"\*\*Direction\s+statement\s*[:\-]?\*\*\s*(.+)", header_text,
                  re.IGNORECASE)
    if m:
        direction = m.group(1).strip()

    return title, direction


# ---------------------------------------------------------------------------
# Finding parser (Part 1 and Part 2)
# ---------------------------------------------------------------------------

FINDING_ID_PAT = re.compile(r"^(?:#{1,3}\s+|\*\*)([A-Z][A-Z0-9]*-[A-Z]{0,2}\d+)", re.MULTILINE | re.IGNORECASE)


def parse_findings(section_text: str, part_number: int | str, shard_id: str, source_tool: str) -> list[dict]:
    """Parse all findings in a Part 1 or Part 2 section."""
    findings: list[dict] = []

    splits = list(FINDING_ID_PAT.finditer(section_text))
    if not splits:
        return findings

    for i, m in enumerate(splits):
        finding_id = m.group(1).strip()
        block_start = m.end()
        block_end = splits[i + 1].start() if i + 1 < len(splits) else len(section_text)
        block = section_text[block_start:block_end]

        try:
            record = _parse_finding_block(block, finding_id)
        except Exception as exc:
            _warn(f"Could not parse finding {finding_id}: {exc}")
            continue

        record["finding_id"] = finding_id
        record["shard_id"] = shard_id
        record["source_tool"] = source_tool
        record["part"] = part_number
        findings.append(record)

    return findings


def _parse_finding_block(block: str, finding_id: str) -> dict:
    """
    Extract fields from a finding block.

    - Required fields (DGI-R4) → top-level keys using canonical names.
    - Unknown / domain-specific fields → nested under extra_fields.
    - Warns to stderr for each missing required field.
    """
    required: dict[str, str] = {}
    extra: dict[str, str] = {}

    current_key: str | None = None
    is_required: bool = False
    current_lines: list[str] = []

    def _flush() -> None:
        if current_key is None:
            return
        value = _clean("\n".join(current_lines))
        if is_required:
            required[current_key] = value
        else:
            extra[current_key] = value

    for line in block.splitlines():
        m = _FIELD_LABEL_PAT.match(line)
        if m:
            _flush()
            raw_label = m.group(1)
            current_key, is_required = _canonical_key(raw_label)
            current_lines = [m.group(2).strip()]
        else:
            if current_key is not None:
                current_lines.append(line)

    _flush()

    # Warn on missing required fields
    for req_key in REQUIRED_KEYS:
        if req_key not in required:
            _warn(f"Finding {finding_id}: missing required field '{req_key}'")

    record: dict = dict(required)
    if extra:
        record["extra_fields"] = extra
    return record


# ---------------------------------------------------------------------------
# Part 4 parser
# ---------------------------------------------------------------------------

PART4_ITEM_PAT = re.compile(r"^(?:#{1,3}\s+|\*\*)(F-X\d+)(?:\*\*)?:[ \t]*(?:\*\*)?\s*(.+?)(?:\*\*)?$", re.MULTILINE | re.IGNORECASE)


def parse_part4(section_text: str, shard_id: str, source_tool: str) -> list[dict]:
    """
    Parse Part 4 absence findings.

    Part 4 items use the same 7 field labels as Part 1/2 findings, so the block
    is parsed with _parse_finding_block instead of dedicated regex. The consumer
    (route_unrecoverable.py) expects `attempted` and `why_failed`, which the
    contract template does not emit as labels:

      attempted  <- Source field ("Searches: ...; Locations attempted: ...")
      why_failed <- None. An absence finding has no per-item failure mode;
                    the absence is the result, not an error.

    Legacy shards using literal `Attempted:` / `Reason:` labels land in
    extra_fields and are picked up as a fallback.
    """
    items: list[dict] = []

    splits = list(PART4_ITEM_PAT.finditer(section_text))
    if not splits:
        return items

    for i, m in enumerate(splits):
        item_id = m.group(1).strip()
        subject = m.group(2).strip()
        block_start = m.end()
        block_end = splits[i + 1].start() if i + 1 < len(splits) else len(section_text)
        block = section_text[block_start:block_end]

        try:
            parsed = _parse_finding_block(block, item_id)
        except Exception as exc:
            _warn(f"Part 4 item {item_id} ({subject}): could not parse block: {exc}")
            parsed = {}

        extra = parsed.get("extra_fields", {})

        # Legacy sub-formats: "Attempted:" (BUG-S23-02 format 2) and
        # "Searched for:" / "Where searched:" (format 3, absence findings).
        attempted = parsed.get("source", "") or extra.get("attempted", "")
        if not attempted:
            searched_for = extra.get("searched_for", "")
            where_searched = extra.get("where_searched", "")
            parts = [p for p in (searched_for, where_searched) if p]
            attempted = " | ".join(parts)
        # The contract puts "Searches: ...; Locations attempted: ..." on the
        # Source line. If that line wrapped, _parse_finding_block split it into
        # a separate field; re-join so `attempted` is not silently truncated.
        if "locations_attempted" in extra:
            attempted = f"{attempted} Locations attempted: {extra['locations_attempted']}".strip()

        why_failed = (extra.get("why_failed") or extra.get("reason")
                      or extra.get("result") or None)

        if not attempted:
            _warn(
                f"Part 4 item {item_id} ({subject}): no Source field and no "
                f"legacy Attempted field — 'attempted' will be empty"
            )

        item = {
            "shard_id": shard_id,
            "source_tool": source_tool,
            "item_id": item_id,
            "seller_or_subject": subject,
            "attempted": attempted,
            "why_failed": why_failed,
            "urls_mentioned": _extract_urls(block),
        }

        # Preserve the contract's 7 canonical fields for downstream traceability.
        for key in ("what", "verbatim_snippet", "source", "source_type",
                    "verification_status", "date", "notes"):
            if key in parsed:
                item[key] = parsed[key]
        if extra:
            item["extra_fields"] = extra

        items.append(item)

    return items


# ---------------------------------------------------------------------------
# QA Notes parser
# ---------------------------------------------------------------------------

# Known section title → canonical key mapping
_QA_KEY_MAP: dict[str, str] = {
    "findings forced to provisional":              "findings_forced_to_provisional",
    "findings degraded to could not verify":       "findings_degraded_to_could_not_verify",
    "multi-speaker pages split":                   "multi_speaker_pages_split",
    "multi speaker pages split":                   "multi_speaker_pages_split",
    "source type distribution":                    "source_type_distribution",
    "source_type distribution":                    "source_type_distribution",
    "categories expected to have findings but returned none": "categories_expected_no_findings",
    "categories expected no findings":             "categories_expected_no_findings",
    "gumroad store verification gap":              "gumroad_store_verification_gap",
    "medium access barriers":                      "medium_access_barriers",
    "yield vs expected shape":                     "yield_vs_expected_shape",
    "yield vs. expected shape":                    "yield_vs_expected_shape",
    "yield":                                       "yield_vs_expected_shape",
    "gaps by category":                            "categories_expected_no_findings",
    "inputs that could not be searched without interpretation":
        "inputs_not_searched_without_interpretation",
}


def _canonical_qa_key(title: str) -> str:
    slug = title.strip().lower()
    if slug in _QA_KEY_MAP:
        return _QA_KEY_MAP[slug]
    for pattern, canonical in _QA_KEY_MAP.items():
        if pattern in slug:
            return canonical
    return _slug(title)


def parse_qa_notes(section_text: str, shard_id: str, source_tool: str) -> dict:
    """Parse QA Notes section into a flat dict of sections."""
    record: dict = {"shard_id": shard_id, "source_tool": source_tool}

    # --- Strategy 1: ### subsections ---
    subsection_re = re.compile(r"^(#{2,4})\s+(.+)$", re.MULTILINE)
    splits = list(subsection_re.finditer(section_text))

    # Skip the ## Research QA Notes header itself
    start_idx = 0
    if splits and re.match(r"Research\s+QA\s+Notes", splits[0].group(2), re.IGNORECASE):
        start_idx = 1

    if start_idx < len(splits):
        # There are real subsections beyond the header
        for i in range(start_idx, len(splits)):
            title = splits[i].group(2).strip()
            content_start = splits[i].end()
            content_end = splits[i + 1].start() if i + 1 < len(splits) else len(section_text)
            content = _clean(section_text[content_start:content_end])
            key = _canonical_qa_key(title)
            record[key] = content
        return record

    # --- Strategy 2: **Bold label:** value lines (no ### subsections) ---
    bold_result = _parse_qa_bold_labels(section_text)
    if bold_result:
        record.update(bold_result)
        return record

    # --- Strategy 3: - Key: Value bullet list ---
    bullet_re = re.compile(r"^\s*[-*]\s+([^:\n]+?):\s*(.+)$", re.MULTILINE)
    for m in bullet_re.finditer(section_text):
        key = _canonical_qa_key(m.group(1).strip())
        record[key] = _clean(m.group(2))
    return record


def _parse_qa_bold_labels(text: str) -> dict:
    """
    Parse QA sections written as bold-label paragraphs:
        **Label:** multi-line content...    (colon inside **)
        **Label**: multi-line content...    (colon outside **)
        **Next label:** ...
    """
    result: dict = {}

    # Match **Label:** or **Label**: patterns at the start of a line.
    # Colon may be inside (**Label:**) or outside (**Label**:).
    # The label group captures the clean label text (no trailing colon).
    label_re = re.compile(
        r"(?:^|\n)\s*\*\*([^\*\n]+?):?\*\*:?\s*",
        re.MULTILINE,
    )
    matches = list(label_re.finditer(text))

    for i, m in enumerate(matches):
        raw_label = m.group(1).strip()
        content_start = m.end()
        content_end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        content = _clean(text[content_start:content_end])
        key = _canonical_qa_key(raw_label)
        result[key] = content

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
    shard_id = p.stem  # e.g. "DX-2_gumroad_v2"

    # Determine source_tool from the parent directory name
    VALID_SOURCE_TOOLS = {"deep_search", "gpt_custom", "eje4_discovery"}
    parent_dir_name = p.parent.name
    if parent_dir_name in VALID_SOURCE_TOOLS:
        source_tool = parent_dir_name
    else:
        _warn(
            f"Shard '{p.name}' is not in a valid source_tool subdirectory "
            f"(parent dir: '{parent_dir_name}'). Using source_tool='unknown'."
        )
        source_tool = "unknown"

    sections = split_sections(text)

    # Parse findings (Part 1 + Part 2)
    findings_written = 0
    for part_num, section_key in [(1, "part1"), ("1b", "part1b"), (2, "part2"), ("2b", "part2b")]:
        sec = sections.get(section_key, "")
        if not sec:
            continue
        for finding in parse_findings(sec, part_num, shard_id, source_tool):
            fid = finding.get("finding_id", "UNKNOWN")
            out_path = FINDINGS_DIR / f"{shard_id}__{fid}.json"
            write_json(out_path, finding)
            findings_written += 1

    # Parse Part 4
    part4_written = 0
    sec4 = sections.get("part4", "")
    if sec4:
        for item in parse_part4(sec4, shard_id, source_tool):
            filename = f"{shard_id}__{item['item_id']}.json"
            out_path = PART4_DIR / filename
            write_json(out_path, item)
            part4_written += 1

    # Parse QA Notes
    qa_written = 0
    sec_qa = sections.get("qa", "")
    if sec_qa:
        qa_record = parse_qa_notes(sec_qa, shard_id, source_tool)
        qa_keys = len(qa_record) - 2  # subtract shard_id and source_tool
        out_path = QA_DIR / f"{shard_id}_qa.json"
        write_json(out_path, qa_record)
        qa_written = 1
    else:
        qa_keys = 0

    print(
        f"Done — shard: {shard_id} | findings: {findings_written} "
        f"| part4 items: {part4_written} | qa file: {qa_written} ({qa_keys} sections)"
    )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <shard.md>", file=sys.stderr)
        sys.exit(1)
    main(sys.argv[1])
