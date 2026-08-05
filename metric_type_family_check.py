#!/usr/bin/env python3
"""
metric_type_family_check.py

D-287: every value of the metric_type enum — in pipeline_vocabulary.yaml and
in both schemas that declare it (data_extraction_record.schema.json,
signal_card.schema.json), across both branches of the oneOf (string and
array-items) — must carry a mag_ or qual_ prefix, with "unknown" as the sole
declared exemption (sentinel).

Exit 0 if every source agrees; exit 1 and report offending values otherwise.
"""

import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent
VOCAB_PATH = ROOT / "pipeline_vocabulary.yaml"
SCHEMA_PATHS = {
    "data_extraction_record.schema.json": ROOT
    / "phases/01-source-intake/data-extraction/schemas/data_extraction_record.schema.json",
    "signal_card.schema.json": ROOT
    / "phases/02-signal-extraction/schemas/signal_card.schema.json",
}

SENTINEL = "unknown"


def is_prefixed(value):
    return value == SENTINEL or value.startswith("mag_") or value.startswith("qual_")


def vocab_values():
    with VOCAB_PATH.open(encoding="utf-8") as f:
        vocab = yaml.safe_load(f)
    return set(vocab["metric_type"]["values"])


def schema_branch_values(node):
    """metric_type property node -> {branch_label: set(values)}."""
    branches = {}
    for branch in node.get("oneOf", []):
        if branch.get("type") == "string" and isinstance(branch.get("enum"), list):
            branches["string"] = set(branch["enum"])
        elif branch.get("type") == "array":
            items = branch.get("items", {})
            if isinstance(items.get("enum"), list):
                branches["array"] = set(items["enum"])
    return branches


def schema_values(path):
    with path.open(encoding="utf-8") as f:
        schema = json.load(f)
    node = schema.get("properties", {}).get("metric_type", {})
    return schema_branch_values(node)


def main():
    offenders = []

    vv = vocab_values()
    bad = sorted(v for v in vv if not is_prefixed(v))
    if bad:
        offenders.append(("pipeline_vocabulary.yaml", "values", bad))

    for label, path in SCHEMA_PATHS.items():
        branches = schema_values(path)
        if not branches:
            offenders.append((label, "metric_type", ["<no oneOf enum branches found>"]))
            continue
        for branch_name, values in branches.items():
            bad = sorted(v for v in values if not is_prefixed(v))
            if bad:
                offenders.append((label, branch_name, bad))

    if offenders:
        print("FAIL: values without mag_/qual_ prefix (unknown is the only exempt sentinel):")
        for source, branch, bad in offenders:
            print(f"  {source} [{branch}]: {bad}")
        return 1

    print("OK: every metric_type value across vocab and both schema branches "
          "carries mag_/qual_, except the unknown sentinel.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
