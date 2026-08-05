#!/usr/bin/env python3
"""
vocab_check.py

Checks every closed enum declared in pipeline_vocabulary.yaml against every
*.schema.json file in the repo (excluding working/) and reports divergences.

Per vocabulary field, the following optional keys change how it is checked:
  match: exact|subset   (default: exact)
      exact   -> report both values the schema is missing and values the
                 schema has that the vocabulary doesn't recognize.
      subset  -> only report values the schema has that the vocabulary
                 doesn't recognize ("valores que sobran").
  schema_field: name | [name, ...]
      Property name(s) to look for in schemas. Defaults to the vocabulary
      key itself.
  in_schemas: [glob, ...]
      Restricts which schema files this field is checked against. Matched
      against both the file's path relative to the repo root and its
      basename. Defaults to all schema files.
  optional: [value, ...]
      Values a schema is allowed to omit without that counting as a
      divergence (only relevant in 'exact' mode).

Enums are resolved by walking the whole schema document (properties,
oneOf/anyOf branches, array items, and local $ref/$defs), so nested enums
are found regardless of how deep they sit. Multiple occurrences of the same
resolved enum (e.g. a oneOf[string, array-of-string] pair, or the same field
repeated across schema files) are deduplicated before comparison. Fields the
vocabulary defines as a closed enum but which a schema declares as a free
string (no enum anywhere) are reported in a separate section.
"""

import fnmatch
import json
import sys
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent
VOCAB_PATH = ROOT / "pipeline_vocabulary.yaml"

META_KEYS = {
    "notes", "deprecated", "phase", "source", "match",
    "schema_field", "in_schemas", "optional", "assignment_rule",
}


def load_vocab():
    with VOCAB_PATH.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def resolved_values(entry):
    """Union of all list-valued keys in a vocab entry, excluding meta keys."""
    values = set()
    for key, val in entry.items():
        if key in META_KEYS:
            continue
        if isinstance(val, list):
            values.update(v for v in val if isinstance(v, str))
    return values


def find_schema_files():
    files = []
    for path in ROOT.rglob("*.schema.json"):
        relparts = path.relative_to(ROOT).parts
        if "working" in relparts:
            continue
        files.append(path)
    return sorted(files)


def matches_in_schemas(path, patterns):
    if not patterns:
        return True
    relpath = path.relative_to(ROOT).as_posix()
    name = path.name
    return any(fnmatch.fnmatch(relpath, pat) or fnmatch.fnmatch(name, pat) for pat in patterns)


def resolve_pointer(ref, doc):
    if not ref.startswith("#/"):
        return None
    node = doc
    for part in ref[2:].split("/"):
        if not isinstance(node, dict) or part not in node:
            return None
        node = node[part]
    return node


def resolve_node(node, doc, seen):
    """Returns (enum_values: set[str], found_string_leaf: bool, found_object_leaf: bool)."""
    enums = set()
    found_string_leaf = False
    found_object_leaf = False

    if not isinstance(node, dict):
        return enums, found_string_leaf, found_object_leaf

    ref = node.get("$ref")
    if isinstance(ref, str) and ref not in seen:
        target = resolve_pointer(ref, doc)
        if target is not None:
            e, s, o = resolve_node(target, doc, seen | {ref})
            enums |= e
            found_string_leaf |= s
            found_object_leaf |= o

    enum_list = node.get("enum")
    if isinstance(enum_list, list):
        enums.update(v for v in enum_list if isinstance(v, str))

    for key in ("oneOf", "anyOf"):
        branches = node.get(key)
        if isinstance(branches, list):
            for branch in branches:
                e, s, o = resolve_node(branch, doc, seen)
                enums |= e
                found_string_leaf |= s
                found_object_leaf |= o

    if "items" in node:
        e, s, o = resolve_node(node["items"], doc, seen)
        enums |= e
        found_string_leaf |= s
        found_object_leaf |= o

    node_type = node.get("type")
    types = node_type if isinstance(node_type, list) else ([node_type] if node_type else [])
    if "string" in types and not enum_list:
        found_string_leaf = True
    if "object" in types:
        found_object_leaf = True

    return enums, found_string_leaf, found_object_leaf


def collect_property_index(doc):
    """Maps property name -> list of (schema_node, json_path) found anywhere in the doc."""
    index = defaultdict(list)

    def walk(node, path):
        if isinstance(node, dict):
            props = node.get("properties")
            if isinstance(props, dict):
                for name, subnode in props.items():
                    index[name].append((subnode, path + ["properties", name]))
            for key, val in node.items():
                walk(val, path + [key])
        elif isinstance(node, list):
            for i, item in enumerate(node):
                walk(item, path + [str(i)])

    walk(doc, [])
    return index


def classify(node, doc):
    enums, found_string_leaf, found_object_leaf = resolve_node(node, doc, set())
    if enums:
        return ("enum", frozenset(enums))
    if found_string_leaf:
        return ("open_string", None)
    return ("skip", None)


def check_field(field_name, entry, schema_files, schema_docs, schema_prop_index):
    match_mode = entry.get("match", "exact")
    schema_field = entry.get("schema_field", field_name)
    if isinstance(schema_field, str):
        schema_field = [schema_field]
    in_schemas = entry.get("in_schemas")
    optional = set(entry.get("optional", []))
    vocab_values = resolved_values(entry)

    # occurrence_key -> {'files': set(), 'declared': frozenset|None}
    enum_occurrences = defaultdict(set)   # declared_set -> set of files
    open_string_files = set()

    for path in schema_files:
        if not matches_in_schemas(path, in_schemas):
            continue
        doc = schema_docs[path]
        index = schema_prop_index[path]
        for name in schema_field:
            for node, _json_path in index.get(name, []):
                kind, declared = classify(node, doc)
                relpath = path.relative_to(ROOT).as_posix()
                if kind == "enum":
                    enum_occurrences[declared].add(relpath)
                elif kind == "open_string":
                    open_string_files.add(relpath)
                # kind == "skip" -> not a comparable value field here, ignore

    divergences = []
    subset_blind_missing = []
    for declared_set, files in enum_occurrences.items():
        missing = (vocab_values - optional) - declared_set
        extra = declared_set - vocab_values
        if match_mode == "subset":
            if missing:
                # E6b/S38: this is the direction the veredict below discards.
                # Captured here, before the zeroing, purely for the informational
                # report — does not feed `divergences` / has_issues / exit code.
                subset_blind_missing.append({
                    "files": sorted(files),
                    "declared": sorted(declared_set),
                    "missing": sorted(missing),
                })
            missing = set()
        if missing or extra:
            divergences.append({
                "files": sorted(files),
                "declared": sorted(declared_set),
                "missing": sorted(missing),
                "extra": sorted(extra),
            })

    total_enum_occurrences = sum(len(files) for files in enum_occurrences.values())
    return {
        "field": field_name,
        "match_mode": match_mode,
        "divergences": divergences,
        "subset_blind_missing": subset_blind_missing,
        "open_string_files": sorted(open_string_files),
        "occurrences_found": total_enum_occurrences + len(open_string_files),
    }


def known_field_names(vocab):
    """Property names already covered by some vocab entry's schema_field (or its own key)."""
    names = set()
    for field_name, entry in vocab.items():
        if not isinstance(entry, dict):
            continue
        schema_field = entry.get("schema_field", field_name)
        if isinstance(schema_field, str):
            schema_field = [schema_field]
        names.update(schema_field)
    return names


def discover_unconfigured_enums(known_names, schema_files, schema_docs, schema_prop_index):
    """Enum-bearing properties whose name is never visited by the vocab.items() loop.

    Discovery mode only: does not feed has_issues / the exit code (D-240 precedent
    — an inapplicable red check teaches ignoring checks; this pass reports).
    """
    found = []
    for path in schema_files:
        doc = schema_docs[path]
        index = schema_prop_index[path]
        relpath = path.relative_to(ROOT).as_posix()
        for name in sorted(index):
            if name in known_names:
                continue
            values = set()
            for node, _json_path in index[name]:
                kind, declared = classify(node, doc)
                if kind == "enum":
                    values |= declared
            if values:
                found.append((relpath, name, sorted(values)))
    return sorted(found)


def main():
    vocab = load_vocab()
    schema_files = find_schema_files()

    schema_docs = {}
    schema_prop_index = {}
    for path in schema_files:
        try:
            with path.open(encoding="utf-8") as f:
                doc = json.load(f)
        except (OSError, json.JSONDecodeError) as e:
            print(f"WARNING: could not parse {path.relative_to(ROOT)}: {e}", file=sys.stderr)
            continue
        schema_docs[path] = doc
        schema_prop_index[path] = collect_property_index(doc)

    schema_files = [p for p in schema_files if p in schema_docs]

    results = []
    untouched_fields = []
    for field_name, entry in vocab.items():
        if not isinstance(entry, dict):
            continue
        result = check_field(field_name, entry, schema_files, schema_docs, schema_prop_index)
        if result["occurrences_found"] == 0:
            untouched_fields.append(field_name)
        else:
            results.append(result)

    known_names = known_field_names(vocab)
    discovered = discover_unconfigured_enums(known_names, schema_files, schema_docs, schema_prop_index)

    print("=" * 78)
    print("VOCAB CHECK — pipeline_vocabulary.yaml vs *.schema.json (excl. working/)")
    print("=" * 78)
    print(f"Schema files scanned: {len(schema_files)}")
    print(f"Vocabulary fields checked: {len(results)} (with schema occurrences), "
          f"{len(untouched_fields)} with no matching schema field")
    print()

    has_issues = False

    print("-" * 78)
    print("DIVERGENCES (enum mismatches)")
    print("-" * 78)
    any_divergence = False
    for result in results:
        if not result["divergences"]:
            continue
        any_divergence = True
        has_issues = True
        print(f"\n[{result['field']}] (match={result['match_mode']})")
        for d in result["divergences"]:
            print(f"  files: {', '.join(d['files'])}")
            if d["missing"]:
                print(f"    missing in schema (vocab has, schema doesn't): {d['missing']}")
            if d["extra"]:
                print(f"    extra in schema (schema has, not in vocab):    {d['extra']}")
    if not any_divergence:
        print("(none)")

    print()
    print("-" * 78)
    print("OPEN-STRING FIELDS (vocab defines a closed enum, schema declares free string)")
    print("-" * 78)
    any_open = False
    for result in results:
        if not result["open_string_files"]:
            continue
        any_open = True
        has_issues = True
        print(f"\n[{result['field']}]")
        for f in result["open_string_files"]:
            print(f"  {f}")
    if not any_open:
        print("(none)")

    print()
    print("-" * 78)
    print("CLEAN FIELDS (schema occurrences found, no divergence)")
    print("-" * 78)
    clean = [r["field"] for r in results if not r["divergences"] and not r["open_string_files"]]
    print(", ".join(clean) if clean else "(none)")

    print()
    print("-" * 78)
    print("VOCAB FIELDS WITH NO MATCHING SCHEMA FIELD FOUND")
    print("-" * 78)
    print(", ".join(untouched_fields) if untouched_fields else "(none)")
    print()

    print("-" * 78)
    print("SCHEMA ENUM PROPERTIES WITH NO VOCAB CONFIGURATION (discovery mode, E6/S38)")
    print("-" * 78)
    print("(reporting only — not gated into the exit code; see D-240 precedent)")
    if discovered:
        for relpath, name, values in discovered:
            print(f"\n[{name}] {relpath}")
            print(f"  declared: {values}")
        distinct_names = sorted({name for _, name, _ in discovered})
        print()
        print(f"Pairs (file, property): {len(discovered)}   Distinct property names: {len(distinct_names)}")
    else:
        print("(none)")
    print()

    print("-" * 78)
    print("SUBSET FIELDS — BLIND MISSING DIRECTION (informational, E6b/S38)")
    print("-" * 78)
    print("(reporting only — not gated into the exit code; `match: subset` still")
    print(" suppresses this direction from DIVERGENCES/the veredict by design;")
    print(" see D-240 precedent)")
    any_blind = False
    for result in results:
        blind = result.get("subset_blind_missing")
        if not blind:
            continue
        any_blind = True
        print(f"\n[{result['field']}] (match=subset)")
        for d in blind:
            print(f"  files: {', '.join(d['files'])}")
            print(f"    missing in schema (vocab has, schema doesn't, suppressed by subset): {d['missing']}")
    if not any_blind:
        print("(none)")
    print()

    sys.exit(1 if has_issues else 0)


if __name__ == "__main__":
    main()
