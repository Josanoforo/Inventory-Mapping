#!/usr/bin/env python3
"""
manifest_archive.py

D-283(a) / P-121. Mechanizes the archiving clause of
.claude/skills/p2-extract-signals/SKILL.md's "## Resumability" section
(the Phase 2 / stage 2 manifest,
working/signal_extraction/signal_converter_manifest.json), implemented
literal, verbatim:

  If status == complete and a new run is intended, archive this manifest
  first -- copy it, unmodified, to
  working/signal_extraction/signal_converter_manifest.<archived_at>.json
  (<archived_at> = ISO 8601 UTC timestamp of the archive action, ':'
  replaced by '-') -- then initialize a fresh manifest as in the "manifest
  does not exist" case. Never delete or overwrite a complete manifest
  without archiving it first.

  If manifest does not exist: read signal_id_counter_at_stage1 from stage 1
  manifest; initialize with status: in_progress, next_signal_id_counter set
  to that value, empty arrays, and proceed.

"A new run is intended" is a call the skill makes (e.g. stage 1 produced
additional skeletons) -- this script does not infer it. It exposes the two
mechanical halves as separate actions (archive, init) plus rotate() for the
skill to call once it has already decided a new run starts; it never
decides that on its own.

The remaining fields the fresh manifest's schema requires but the quoted
prose doesn't name (round, total_skeletons_found, and the run counters) are
filled from the schema's own field descriptions
(phases/02-signal-extraction/schemas/signal_converter_manifest.schema.json),
not invented: round and next_signal_id_counter come from the stage 1
manifest ("Round number from stage 1", "Initialized from
signal_id_counter_at_stage1 in the stage 1 manifest"); total_skeletons_found
is a live count ("Total number of skeleton files enumerated across all
batch directories at startup"); the run counters
(skeletons_processed/cards_written/cards_recovery_staged/skeleton_failures/
needs_human_review_count/splits_performed) are 0 and processed_skeletons/
issues are [] because nothing has run yet in a fresh manifest.

Scope note (D-283(a)): this covers only the Phase 2 signal_converter
manifest. Five other scripts write a per-run manifest of their own
(eje4_xlsx_to_json_batch.py, part4_to_recovery_packets.py, bulk_extract.py,
extraction_prepare.py, converter_prepare.py, signal_prepare.py) and are out
of scope for this decision.

Usage:
    python3 manifest_archive.py archive   # archive the complete manifest, no reinit
    python3 manifest_archive.py init      # create a fresh manifest (requires none exists)
    python3 manifest_archive.py rotate    # archive (requires complete) + init, in one call
"""

import argparse
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MANIFEST_PATH = ROOT / "working" / "signal_extraction" / "signal_converter_manifest.json"
STAGE1_MANIFEST_PATH = ROOT / "working" / "signal_extraction" / "signal_prepare_manifest.json"
SKELETON_DIR = ROOT / "working" / "signal_extraction" / "skeleton_batches"


def archived_at_timestamp():
    return datetime.now(timezone.utc).isoformat().replace(":", "-")


def archive_manifest(manifest_path=MANIFEST_PATH):
    """Copy a status==complete manifest, byte-for-byte unmodified, to
    signal_converter_manifest.<archived_at>.json. Refuses if the manifest
    is missing, not complete, or an archive for this instant already
    exists (never overwrites an existing archive)."""
    if not manifest_path.exists():
        raise FileNotFoundError(f"no manifest at {manifest_path}")

    raw = manifest_path.read_bytes()
    data = json.loads(raw)
    if data.get("status") != "complete":
        raise ValueError(
            f"refusing to archive: status is {data.get('status')!r}, not 'complete'"
        )

    dest = manifest_path.parent / f"signal_converter_manifest.{archived_at_timestamp()}.json"
    if dest.exists():
        raise FileExistsError(f"archive destination already exists: {dest}")

    shutil.copy2(manifest_path, dest)
    # copy2 preserves bytes exactly ("unmodified") -- verify, don't just assume.
    assert dest.read_bytes() == raw
    return dest


def build_fresh_manifest(stage1_path=STAGE1_MANIFEST_PATH, skeleton_dir=SKELETON_DIR):
    stage1 = json.loads(stage1_path.read_text(encoding="utf-8"))
    total_skeletons_found = len(list(skeleton_dir.glob("*/*.json")))
    return {
        "status": "in_progress",
        "round": stage1["round"],
        "total_skeletons_found": total_skeletons_found,
        "skeletons_processed": 0,
        "cards_written": 0,
        "cards_recovery_staged": 0,
        "skeleton_failures": 0,
        "needs_human_review_count": 0,
        "splits_performed": 0,
        "next_signal_id_counter": stage1["signal_id_counter_at_stage1"],
        "processed_skeletons": [],
        "issues": [],
        "started_at": datetime.now(timezone.utc).isoformat(),
        "completed_at": None,
    }


def initialize_fresh_manifest(manifest_path=MANIFEST_PATH, stage1_path=STAGE1_MANIFEST_PATH,
                               skeleton_dir=SKELETON_DIR):
    """The 'manifest does not exist' case. Refuses if a manifest is already
    at manifest_path -- callers must archive_manifest() it out of the way
    first (rotate() does both in the right order)."""
    if manifest_path.exists():
        raise FileExistsError(
            f"{manifest_path} already exists; archive it first, or use rotate()"
        )
    manifest = build_fresh_manifest(stage1_path, skeleton_dir)
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return manifest


def rotate(manifest_path=MANIFEST_PATH, stage1_path=STAGE1_MANIFEST_PATH, skeleton_dir=SKELETON_DIR):
    """The full sequence for 'status == complete and a new run is intended':
    archive the complete manifest, then initialize a fresh one in its place.
    Callers decide "a new run is intended" before calling this -- it is not
    inferred here."""
    archived_to = archive_manifest(manifest_path)
    manifest_path.unlink()  # safe: archived_to is a verified byte-identical copy
    manifest = initialize_fresh_manifest(manifest_path, stage1_path, skeleton_dir)
    return archived_to, manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="action", required=True)
    sub.add_parser("archive", help="Archive the manifest at MANIFEST_PATH (requires status == complete).")
    sub.add_parser("init", help="Initialize a fresh manifest (requires none exists at MANIFEST_PATH).")
    sub.add_parser("rotate", help="Archive the complete manifest, then initialize a fresh one.")
    args = parser.parse_args()

    try:
        if args.action == "archive":
            dest = archive_manifest()
            print(f"Archived to: {dest.relative_to(ROOT)}")
        elif args.action == "init":
            manifest = initialize_fresh_manifest()
            print(f"Initialized fresh manifest at {MANIFEST_PATH.relative_to(ROOT)}: "
                  f"round={manifest['round']} total_skeletons_found={manifest['total_skeletons_found']} "
                  f"next_signal_id_counter={manifest['next_signal_id_counter']}")
        elif args.action == "rotate":
            dest, manifest = rotate()
            print(f"Archived to: {dest.relative_to(ROOT)}")
            print(f"Initialized fresh manifest: round={manifest['round']} "
                  f"total_skeletons_found={manifest['total_skeletons_found']} "
                  f"next_signal_id_counter={manifest['next_signal_id_counter']}")
    except (FileNotFoundError, FileExistsError, ValueError) as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
