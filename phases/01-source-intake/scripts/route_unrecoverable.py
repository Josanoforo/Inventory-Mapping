"""
route_unrecoverable.py

Routes unrecoverable findings from working/data_gathering/diagnostics/part_4/
to working/source_intake/rejected_archive/, creating RejectedArchiveRecord JSON
files validated against rejected_archive_record.schema.json.

Run this BEFORE converter_prepare.py. Reads all part_4 JSON files but only
archives those whose source_tool matches RECOVERY_AGENT_SOURCE_TOOLS.
Other files are silently skipped (they are pending input for the recovery
agent, not output from it).

Usage:
    python route_unrecoverable.py [--part4-dir PATH] [--archive-dir PATH] [--dry-run]
"""

import argparse
import json
import sys
from datetime import date
from pathlib import Path

# ---------------------------------------------------------------------------
# Whitelist of source_tool values produced by recovery agents.
# Items in part_4/ whose source_tool is NOT in this list are silently skipped
# (they are pending input for the recovery agent, not output from it).
# To add a new recovery agent source_tool, append to this list.
# ---------------------------------------------------------------------------
RECOVERY_AGENT_SOURCE_TOOLS = ["gpt_custom"]

# ---------------------------------------------------------------------------
# Default paths (relative to repo root, resolved from this script's location)
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[2]  # phases/01-source-intake/scripts -> repo root

DEFAULT_PART4_DIR = REPO_ROOT / "working" / "data_gathering" / "diagnostics" / "part_4"
DEFAULT_ARCHIVE_DIR = REPO_ROOT / "working" / "source_intake" / "rejected_archive"


def load_part4_file(path: Path) -> dict | None:
    """Load and return a part_4 JSON file. Returns None on parse error."""
    try:
        with path.open(encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        print(f"  [ERROR] Cannot read {path.name}: {e}", file=sys.stderr)
        return None


def build_archive_record(finding: dict, today: str) -> dict:
    """Construct a RejectedArchiveRecord from a part_4 finding."""
    return {
        "reason_code": "unrecoverable_after_recovery",
        "source_finding_id": finding.get("item_id", ""),
        "shard_id": finding.get("shard_id", ""),
        "source_tool": finding.get("source_tool", ""),
        "seller_or_subject": finding.get("seller_or_subject", ""),
        "attempted": finding.get("attempted", ""),
        "why_failed": finding.get("why_failed") or None,
        "urls_mentioned": finding.get("urls_mentioned", []),
        "archived_at": today,
    }


def archive_filename(shard_id: str, item_id: str) -> str:
    """Derive archive filename from shard_id and item_id."""
    safe_shard = shard_id.replace(" ", "_").replace("/", "_")
    return f"{safe_shard}__{item_id}.json"


def run(part4_dir: Path, archive_dir: Path, dry_run: bool) -> None:
    today = date.today().isoformat()

    part4_files = sorted(part4_dir.glob("*.json"))
    if not part4_files:
        print(f"No JSON files found in {part4_dir}. Nothing to process.")
        return

    processed = 0
    skipped_not_recovery = 0
    errors = 0

    archive_dir.mkdir(parents=True, exist_ok=True)

    for path in part4_files:
        finding = load_part4_file(path)
        if finding is None:
            errors += 1
            continue

        source_tool = finding.get("source_tool", "")
        if source_tool not in RECOVERY_AGENT_SOURCE_TOOLS:
            skipped_not_recovery += 1
            continue

        record = build_archive_record(finding, today)
        out_name = archive_filename(record["shard_id"], record["source_finding_id"])
        out_path = archive_dir / out_name

        if dry_run:
            print(f"  [DRY-RUN] Would write: {out_name}")
        else:
            with out_path.open("w", encoding="utf-8") as f:
                json.dump(record, f, ensure_ascii=False, indent=2)
            print(f"  [ARCHIVED] {out_name}")

        processed += 1

    print()
    print("=== route_unrecoverable summary ===")
    print(f"  Total files in part_4/  : {len(part4_files)}")
    print(f"  Skipped (not recovery)  : {skipped_not_recovery}")
    print(f"  Processed               : {processed}")
    print(f"  Errors                  : {errors}")
    if dry_run:
        print("  Mode: DRY-RUN (no files written)")
    else:
        print(f"  Archive dir             : {archive_dir}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Route unrecoverable findings from part_4/ to rejected_archive/."
    )
    parser.add_argument(
        "--part4-dir",
        type=Path,
        default=DEFAULT_PART4_DIR,
        help="Path to working/data_gathering/diagnostics/part_4/ (default: auto-detected)",
    )
    parser.add_argument(
        "--archive-dir",
        type=Path,
        default=DEFAULT_ARCHIVE_DIR,
        help="Path to working/source_intake/rejected_archive/ (default: auto-detected)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would be written without creating files.",
    )
    args = parser.parse_args()

    print(f"part_4 dir  : {args.part4_dir}")
    print(f"archive dir : {args.archive_dir}")
    print(f"dry-run     : {args.dry_run}")
    print(f"whitelist   : {RECOVERY_AGENT_SOURCE_TOOLS}")
    print()

    if not args.part4_dir.is_dir():
        print(f"[ERROR] part_4 dir does not exist: {args.part4_dir}", file=sys.stderr)
        sys.exit(1)

    run(args.part4_dir, args.archive_dir, args.dry_run)


if __name__ == "__main__":
    main()
