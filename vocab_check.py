#!/usr/bin/env python3
"""
vocab_check.py — Cross-check pipeline_vocabulary.yaml against all *.schema.json
files outside working/, and report enum divergences.

pipeline_vocabulary.yaml is the source of truth (see its own header). This
script does not fix anything — it only reports where a schema has drifted
from the vocabulary, so drift can be fixed deliberately instead of silently.

How a vocabulary field declares its own check (all keys optional):

    match: exact | subset
        exact (default) — report values the vocab has that the schema is
            missing, AND values the schema has that the vocab doesn't.
        subset — the schema is allowed to declare fewer values than the
            vocab; only report values the schema has that the vocab doesn't
            ("en subset solo se reporta lo que sobra").

    schema_field: name | [name, ...]
        The property name(s) to look for in schemas. Defaults to the
        vocabulary field's own key. Use this when a schema calls the field
        something else (e.g. actor is called actor_level in Phase 1-2
        schemas).

    in_schemas: [glob, ...]
        Restrict the check to schema files matching these globs (relative
        to repo root). Needed for generic property names like "type" or
        "status" that appear, unrelated, all over the repo's manifest and
        validator schemas.

    optional: [value, ...]
        Vocab values a schema is allowed to omit without it being reported
        as missing, even under match: exact (e.g. 'unknown' is legitimately
        absent from Phase 3 schemas).

The `uncertainties` field is shaped differently (a `core` list plus
phase-specific extension lists rather than a flat `values` list) and is
special-cased rather than run through the generic engine above.

Also reported, separately: vocab fields declared as a closed enum whose
matching schema property has no `enum` at all (a free string).

Traversal: every property occurrence is found by walking the full schema
tree (oneOf/anyOf/items/$defs, any nesting), and every `enum` array found
under that property is collected and deduplicated — a property declared as
`oneOf: [{enum: [...]}, {type: array, items: {enum: [...]}}]` with the same
enum in both branches counts once, not twice.

Usage:
    python3 vocab_check.py
"""

import sys
import json
import fnmatch
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required (pip install pyyaml)", file=sys.stderr)
    sys.exit(2)

REPO_ROOT = Path(__file__).resolve().parent
VOCAB_PATH = REPO_ROOT / "pipeline_vocabulary.yaml"

# uncertainties is shaped as core + phase extensions, not a flat values list.
# Mapped here to the schemas that carry each phase's combined enum.
UNCERTAINTIES_PHASE_SCHEMAS = {
    "phase_1_only": [
        "phases/01-source-intake/schemas/source_packet.schema.json",
        "phases/01-source-intake/data-extraction/schemas/data_extraction_record.schema.json",
    ],
    "phase_2_only": [
        "phases/02-signal-extraction/schemas/signal_card.schema.json",
    ],
}


def load_vocab():
    with open(VOCAB_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)


def find_schema_files():
    files = []
    for p in REPO_ROOT.rglob("*.schema.json"):
        rel = p.relative_to(REPO_ROOT)
        if "working" in rel.parts:
            continue
        files.append(rel)
    return sorted(files)


def load_schema_files(rel_paths):
    cache = []
    for rel in rel_paths:
        try:
            cache.append((rel, json.loads((REPO_ROOT / rel).read_text(encoding="utf-8"))))
        except json.JSONDecodeError as e:
            print(f"WARNING: could not parse {rel}: {e}", file=sys.stderr)
    return cache


def matches_any_glob(rel_path, globs):
    if not globs:
        return True
    rel_str = str(rel_path)
    return any(fnmatch.fnmatch(rel_str, g) for g in globs)


def is_bare_ref(node):
    """
    True for placeholder properties like {"$ref": "#/$defs/checkResult"} —
    these share a name with a vocab field (actor_level, status, ...) in
    validator/manifest schemas but describe an unrelated validator-check
    status, not the vocab field itself. Never treat these as free-string
    or enum divergence findings.
    """
    return isinstance(node, dict) and set(node.keys()) <= {"$ref", "description"}


def collect_enum_sets(node):
    """Recursively collect every distinct 'enum' array under a schema subtree."""
    sets = []

    def walk(o):
        if isinstance(o, dict):
            if "enum" in o and isinstance(o["enum"], list):
                sets.append(frozenset(x for x in o["enum"] if isinstance(x, str)))
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)

    walk(node)
    return sets


def find_property_occurrences(schema_json, names):
    """Find every 'properties' dict anywhere in the tree (incl. $defs/oneOf/
    items) and yield (name, node) for any property key matching `names`."""
    found = []

    def walk(o):
        if isinstance(o, dict):
            props = o.get("properties")
            if isinstance(props, dict):
                for name in names:
                    if name in props:
                        found.append((name, props[name]))
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)

    walk(schema_json)
    return found


def check_generic_field(field_name, field_cfg, schema_files_cache):
    values = set(field_cfg["values"])
    match = field_cfg.get("match", "exact")
    schema_field = field_cfg.get("schema_field", field_name)
    optional = set(field_cfg.get("optional", []))
    in_schemas = field_cfg.get("in_schemas")

    names = [schema_field] if isinstance(schema_field, str) else list(schema_field)

    results = []
    for rel_path, schema_json in schema_files_cache:
        if not matches_any_glob(rel_path, in_schemas):
            continue
        for prop_name, node in find_property_occurrences(schema_json, names):
            results.append(evaluate_property(rel_path, prop_name, node, values, match, optional))
    return [r for r in results if r is not None]


def evaluate_property(rel_path, prop_name, node, expected_values, match, optional):
    if is_bare_ref(node):
        return None

    distinct = set(collect_enum_sets(node))

    if not distinct:
        return {"type": "free_string", "schema_file": str(rel_path), "property": prop_name}

    schema_values = set().union(*distinct)
    result = None
    if len(distinct) > 1:
        result = {
            "type": "internal_inconsistency",
            "schema_file": str(rel_path),
            "property": prop_name,
            "distinct_sets": [sorted(s) for s in distinct],
        }

    missing = (expected_values - schema_values) - optional
    if match == "subset":
        missing = set()
    extra = schema_values - expected_values

    if missing or extra:
        divergence = {
            "type": "enum_divergence",
            "schema_file": str(rel_path),
            "property": prop_name,
            "missing_from_schema": sorted(missing),
            "extra_in_schema": sorted(extra),
        }
        # An internal inconsistency and an enum divergence can both be true
        # for the same property; report the inconsistency (more specific)
        # and fold the divergence detail into it.
        if result is not None:
            result["missing_from_schema"] = divergence["missing_from_schema"]
            result["extra_in_schema"] = divergence["extra_in_schema"]
            return result
        return divergence

    return result


def check_uncertainties(vocab, schema_files_cache):
    core = set(vocab["uncertainties"]["core"])
    results = []
    for phase_key, schema_rel_paths in UNCERTAINTIES_PHASE_SCHEMAS.items():
        extension = set(vocab["uncertainties"].get(phase_key, []))
        expected = core | extension
        for rel_path, schema_json in schema_files_cache:
            if str(rel_path) not in schema_rel_paths:
                continue
            for prop_name, node in find_property_occurrences(schema_json, ["uncertainties"]):
                r = evaluate_property(rel_path, prop_name, node, expected, "exact", set())
                if r is not None:
                    r["property"] = f"{prop_name} (core + {phase_key})"
                    results.append(r)
    return results


def main():
    vocab = load_vocab()
    schema_rel_paths = find_schema_files()
    schema_files_cache = load_schema_files(schema_rel_paths)

    all_results = []  # list of (field_name, result_dict)

    for field_name, field_cfg in vocab.items():
        if not isinstance(field_cfg, dict):
            continue
        if field_name == "uncertainties" and "core" in field_cfg:
            for r in check_uncertainties(vocab, schema_files_cache):
                all_results.append((field_name, r))
        elif "values" in field_cfg:
            for r in check_generic_field(field_name, field_cfg, schema_files_cache):
                all_results.append((field_name, r))
        # else: not a checkable enum field (plain notes/reference section) -> skip

    divergences = [r for r in all_results if r[1]["type"] in ("enum_divergence", "internal_inconsistency")]
    free_strings = [r for r in all_results if r[1]["type"] == "free_string"]

    print(f"vocab_check.py — {len(schema_rel_paths)} schema file(s) scanned outside working/\n")

    if divergences:
        print(f"ENUM DIVERGENCES ({len(divergences)})")
        print("-" * 72)
        for field_name, r in divergences:
            tag = " [internal inconsistency: schema declares this enum differently in two places]" if r["type"] == "internal_inconsistency" else ""
            print(f"[{field_name}] {r['schema_file']} :: {r['property']}{tag}")
            if r.get("missing_from_schema"):
                print(f"    missing from schema: {r['missing_from_schema']}")
            if r.get("extra_in_schema"):
                print(f"    extra in schema:     {r['extra_in_schema']}")
            if r["type"] == "internal_inconsistency":
                for s in r["distinct_sets"]:
                    print(f"    variant: {s}")
        print()
    else:
        print("ENUM DIVERGENCES: none\n")

    if free_strings:
        print(f"CLOSED IN VOCAB BUT FREE STRING IN SCHEMA ({len(free_strings)})")
        print("-" * 72)
        for field_name, r in free_strings:
            print(f"[{field_name}] {r['schema_file']} :: {r['property']} (no enum constraint)")
        print()
    else:
        print("CLOSED-ENUM-BUT-FREE-STRING FIELDS: none\n")

    failed = bool(divergences or free_strings)
    print(f"Result: {'FAIL' if failed else 'OK'}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
