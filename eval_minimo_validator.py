#!/usr/bin/env python3
"""
eval_minimo_validator.py — D-270, E-VAL minimal validator.

Mechanical producer of `validation_status` for the current corpus (Source
Packets, Data Extraction Records, Signal Cards). Two things only, per layer:

  1. Structural conformance of the artifact against its OWN schema
     (source_packet.schema.json / data_extraction_record.schema.json /
     signal_card.schema.json) — required fields, types, patterns, enums,
     array constraints. A small self-contained JSON Schema subset
     interpreter (no `jsonschema` dependency: no script in this repo
     imports that library, and CI does not install it — see
     state/output/productores_validacion_S36.md §9).
  2. Membership of every enum-bearing field against the corresponding
     `pipeline_vocabulary.yaml` entry (reusing vocab_check.py's own
     loading/matching helpers), checked against the actual instance
     VALUE — not just the schema's declared enum shape, which is what
     vocab_check.py already checks and is a different question.

This is NOT the semantic validator described in
phases/{01-source-intake,01-source-intake/data-extraction,02-signal-extraction}/contracts/*_validator.md
(traceability, single-claim-boundary, cross-source-synthesis, etc.) — those
require judgment this script does not have. It never emits `rework`,
`reject`, or `parking_lot`: those are validation_status values reserved for
a human/LLM judgment step this script is not.

Two outcomes only, per artifact:
  pass              — structurally valid, all checked enum fields in vocab.
  pass_with_flags    — structurally valid, but >=1 enum field value outside
                       the vocabulary's declared set for that field. Each
                       flag records which field and which value.

An artifact that fails structural validation is NOT assigned a
validation_status (this script cannot decide pass/fail on a broken
artifact — that needs judgment). It is instead recorded as a row in
state/output/eval_candidatos_juicio.md for operator disposal.

Layers (the four surfaces mapped in state/output/mapa_validacion_S36.md
Pregunta 1 / productores_validacion_S36.md §1-2):

  source_intake          working/source_intake/packets/*.json
                          vs phases/01-source-intake/schemas/source_packet.schema.json
  data_extraction         working/data_extraction/records/*.json
                          vs phases/01-source-intake/data-extraction/schemas/data_extraction_record.schema.json
  signal_extraction       working/signal_extraction/cards/*.json
                          vs phases/02-signal-extraction/schemas/signal_card.schema.json
  signal_inventory_gate   no corpus exists today (G1 never ran: no
                          executor, no input artifact — see
                          productores_validacion_S36.md §5). Layer is
                          declared for completeness; it always reports
                          zero items until a gate-report corpus exists.

Output: one summary file per layer under working/validation/mechanical/
(a directory distinct from working/validation/candidate_reports/ and
working/validation/validation_summary.json, which already belong to the
Phase 3 `validate-candidate` skill — a different validator, different
schema, different meaning; writing to those paths would collide with an
already-registered producer). See resources.yaml for registration.
"""

import argparse
import datetime
import json
import re
import sys
from pathlib import Path

import vocab_check

ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = ROOT / "working" / "validation" / "mechanical"
JUDGMENT_PATH = ROOT / "state" / "output" / "eval_candidatos_juicio.md"

LAYERS = {
    "source_intake": {
        "corpus_dir": ROOT / "working" / "source_intake" / "packets",
        "artifact_schema": ROOT / "phases" / "01-source-intake" / "schemas" / "source_packet.schema.json",
        "id_field": "packet_id",
    },
    "data_extraction": {
        "corpus_dir": ROOT / "working" / "data_extraction" / "records",
        "artifact_schema": ROOT / "phases" / "01-source-intake" / "data-extraction" / "schemas" / "data_extraction_record.schema.json",
        "id_field": "extraction_id",
    },
    "signal_extraction": {
        "corpus_dir": ROOT / "working" / "signal_extraction" / "cards",
        "artifact_schema": ROOT / "phases" / "02-signal-extraction" / "schemas" / "signal_card.schema.json",
        "id_field": "signal_id",
    },
    "signal_inventory_gate": {
        # No corpus: G1 has no executor and no input artifact today
        # (productores_validacion_S36.md §5). Declared for completeness
        # against the four surfaces mapped in Paso 2; always reports 0.
        "corpus_dir": None,
        "artifact_schema": ROOT / "phases" / "02-signal-extraction" / "schemas" / "signal_card.schema.json",
        "id_field": "signal_id",
    },
}


# ---------------------------------------------------------------------------
# Minimal JSON Schema subset interpreter.
#
# Covers exactly the keywords used across the three artifact schemas
# (verified by walking all three documents): type, required, properties,
# additionalProperties (bool), enum, pattern, items, minItems, minLength,
# minimum, oneOf, uniqueItems, $ref (local "#/$defs/..." only).
# ---------------------------------------------------------------------------

def _check_type(instance, t):
    if t == "string":
        return isinstance(instance, str)
    if t == "integer":
        return isinstance(instance, int) and not isinstance(instance, bool)
    if t == "number":
        return isinstance(instance, (int, float)) and not isinstance(instance, bool)
    if t == "boolean":
        return isinstance(instance, bool)
    if t == "object":
        return isinstance(instance, dict)
    if t == "array":
        return isinstance(instance, list)
    if t == "null":
        return instance is None
    return True


def _resolve_ref(ref, root_schema):
    if not ref.startswith("#/"):
        raise ValueError(f"unsupported $ref (not local): {ref}")
    node = root_schema
    for part in ref[2:].split("/"):
        node = node[part]
    return node


def validate_instance(instance, schema, root_schema, path="$"):
    """Returns a list of human-readable violation strings. Empty = valid."""
    errors = []

    if "$ref" in schema:
        target = _resolve_ref(schema["$ref"], root_schema)
        return validate_instance(instance, target, root_schema, path)

    if "oneOf" in schema:
        branch_errors = [validate_instance(instance, b, root_schema, path) for b in schema["oneOf"]]
        passing = [e for e in branch_errors if not e]
        if len(passing) != 1:
            errors.append(f"{path}: fails oneOf ({len(passing)} of {len(branch_errors)} branches matched, need exactly 1)")
        return errors

    if "type" in schema:
        types = schema["type"] if isinstance(schema["type"], list) else [schema["type"]]
        if not any(_check_type(instance, t) for t in types):
            errors.append(f"{path}: type mismatch — expected {types}, got {type(instance).__name__}")
            return errors

    if "enum" in schema and instance not in schema["enum"]:
        errors.append(f"{path}: value {instance!r} not in schema enum {schema['enum']}")

    if isinstance(instance, str):
        if "minLength" in schema and len(instance) < schema["minLength"]:
            errors.append(f"{path}: length {len(instance)} < minLength {schema['minLength']}")
        if "pattern" in schema and re.search(schema["pattern"], instance) is None:
            errors.append(f"{path}: does not match pattern {schema['pattern']!r}")

    if isinstance(instance, (int, float)) and not isinstance(instance, bool):
        if "minimum" in schema and instance < schema["minimum"]:
            errors.append(f"{path}: {instance} < minimum {schema['minimum']}")

    if isinstance(instance, list):
        if "minItems" in schema and len(instance) < schema["minItems"]:
            errors.append(f"{path}: {len(instance)} items < minItems {schema['minItems']}")
        if schema.get("uniqueItems"):
            seen = []
            for item in instance:
                key = json.dumps(item, sort_keys=True)
                if key in seen:
                    errors.append(f"{path}: uniqueItems violated")
                    break
                seen.append(key)
        if "items" in schema:
            for i, item in enumerate(instance):
                errors.extend(validate_instance(item, schema["items"], root_schema, f"{path}[{i}]"))

    if isinstance(instance, dict):
        for req in schema.get("required", []):
            if req not in instance:
                errors.append(f"{path}: missing required property '{req}'")
        props = schema.get("properties", {})
        for key, val in instance.items():
            if key in props:
                errors.extend(validate_instance(val, props[key], root_schema, f"{path}.{key}"))
            elif schema.get("additionalProperties") is False:
                errors.append(f"{path}: unexpected additional property '{key}' (additionalProperties: false)")

    return errors


# ---------------------------------------------------------------------------
# Vocabulary enum-membership check (instance-level, distinct from
# vocab_check.py which only compares schema-declared shapes).
# ---------------------------------------------------------------------------

def _flatten_strings(value, path):
    if isinstance(value, str):
        yield path, value
    elif isinstance(value, list):
        for i, item in enumerate(value):
            yield from _flatten_strings(item, f"{path}[{i}]")


def _collect_by_key(instance, key_names, path="$"):
    """Recursively find every value under any of key_names, anywhere in the
    instance (handles both top-level scalar/array fields like
    `uncertainties` and fields nested inside objects/arrays of objects like
    `traceability_pointers[].pointer_type`)."""
    found = []
    if isinstance(instance, dict):
        for k, v in instance.items():
            child_path = f"{path}.{k}"
            if k in key_names:
                found.extend(_flatten_strings(v, child_path))
            found.extend(_collect_by_key(v, key_names, child_path))
    elif isinstance(instance, list):
        for i, item in enumerate(instance):
            found.extend(_collect_by_key(item, key_names, f"{path}[{i}]"))
    return found


def applicable_vocab_fields(vocab, artifact_schema_relpath):
    """Vocab entries whose in_schemas (if any) matches this artifact schema."""
    fields = []
    for field_name, entry in vocab.items():
        if not isinstance(entry, dict):
            continue
        in_schemas = entry.get("in_schemas")
        if in_schemas and not vocab_check.matches_in_schemas(ROOT / artifact_schema_relpath, in_schemas):
            continue
        schema_field = entry.get("schema_field", field_name)
        if isinstance(schema_field, str):
            schema_field = [schema_field]
        values = vocab_check.resolved_values(entry)
        if not values:
            continue
        fields.append({"field_name": field_name, "key_names": schema_field, "values": values})
    return fields


def check_vocab_membership(instance, vocab_fields):
    """Returns a list of flags: {field, key, path, value}."""
    flags = []
    for vf in vocab_fields:
        for path, value in _collect_by_key(instance, vf["key_names"]):
            if value not in vf["values"]:
                flags.append({
                    "vocab_field": vf["field_name"],
                    "path": path,
                    "value": value,
                })
    return flags


# ---------------------------------------------------------------------------
# Per-layer run
# ---------------------------------------------------------------------------

def run_layer(name, cfg, vocab, generated_at):
    artifact_schema_path = cfg["artifact_schema"]
    artifact_schema_relpath = artifact_schema_path.relative_to(ROOT).as_posix()
    result = {
        "layer": name,
        "artifact_schema": artifact_schema_relpath,
        "corpus_dir": None,
        "generated_at": generated_at,
        "generated_by": "eval_minimo_validator.py",
        "vocab_fields_checked": [],
        "counts": {"total": 0, "pass": 0, "pass_with_flags": 0, "judgment_candidates": 0},
        "pass_ids": [],
        "pass_with_flags": [],
        "judgment_candidate_ids": [],
        "notes": [],
    }

    corpus_dir = cfg["corpus_dir"]
    if corpus_dir is None:
        result["notes"].append(
            "No corpus exists for this layer today: G1 (signal_to_inventory_entry_gate) "
            "has no executor and its input artifact (input/signal_cards_round_*.md) does "
            "not exist in the tree. See state/output/productores_validacion_S36.md §5."
        )
        return result, []

    result["corpus_dir"] = corpus_dir.relative_to(ROOT).as_posix()

    with artifact_schema_path.open(encoding="utf-8") as f:
        artifact_schema = json.load(f)

    vocab_fields = applicable_vocab_fields(vocab, artifact_schema_relpath)
    result["vocab_fields_checked"] = sorted(vf["field_name"] for vf in vocab_fields)

    judgment_rows = []
    files = sorted(corpus_dir.glob("*.json"))
    for path in files:
        artifact_id = path.stem
        try:
            with path.open(encoding="utf-8") as f:
                instance = json.load(f)
        except (OSError, json.JSONDecodeError) as e:
            result["counts"]["total"] += 1
            result["counts"]["judgment_candidates"] += 1
            result["judgment_candidate_ids"].append(artifact_id)
            judgment_rows.append({
                "id": artifact_id,
                "layer": name,
                "failed": f"file unreadable / invalid JSON: {e}",
                "points_to": "rework",
            })
            continue

        if isinstance(instance, dict) and cfg["id_field"] in instance:
            artifact_id = instance[cfg["id_field"]]

        result["counts"]["total"] += 1

        schema_errors = validate_instance(instance, artifact_schema, artifact_schema)
        if schema_errors:
            result["counts"]["judgment_candidates"] += 1
            result["judgment_candidate_ids"].append(artifact_id)
            judgment_rows.append({
                "id": artifact_id,
                "layer": name,
                "failed": "; ".join(schema_errors[:5]) + (" ..." if len(schema_errors) > 5 else ""),
                "points_to": "rework",
            })
            continue

        flags = check_vocab_membership(instance, vocab_fields)
        if flags:
            result["counts"]["pass_with_flags"] += 1
            result["pass_with_flags"].append({"id": artifact_id, "flags": flags})
        else:
            result["counts"]["pass"] += 1
            result["pass_ids"].append(artifact_id)

    return result, judgment_rows


def write_judgment_file(all_judgment_rows, generated_at):
    lines = [
        "# eval_candidatos_juicio.md — candidatos a estado de juicio (D-270)",
        "",
        "Generado por `eval_minimo_validator.py`. Cada fila es un artefacto que",
        "no validó estructuralmente contra el schema de su propia capa. El script",
        "no decide `rework` / `reject` / `parking_lot` — esos son estados de juicio",
        "del operador (Paso 4, D-270). \"Apunta a\" es una lectura mecánica por",
        "defecto (fallo estructural recuperable → `rework`), no un veredicto:",
        "el operador puede redirigir cualquier fila a `reject` o, exclusivamente",
        "en la capa `source_intake`, a `parking_lot`.",
        "",
        f"Generado: {generated_at}",
        f"Total candidatos: {len(all_judgment_rows)}",
        "",
        "| id | capa | qué falló | apunta a |",
        "|---|---|---|---|",
    ]
    for row in all_judgment_rows:
        failed = row["failed"].replace("|", "\\|").replace("\n", " ")
        lines.append(f"| {row['id']} | {row['layer']} | {failed} | {row['points_to']} |")
    if not all_judgment_rows:
        lines.append("| (ninguno) | — | — | — |")
    lines.append("")
    JUDGMENT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--layer", choices=list(LAYERS) + ["all"], default="all")
    args = parser.parse_args()

    vocab = vocab_check.load_vocab()
    generated_at = datetime.datetime.now(datetime.timezone.utc).isoformat()

    layer_names = list(LAYERS) if args.layer == "all" else [args.layer]

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    all_judgment_rows = []
    grand_totals = {"pass": 0, "pass_with_flags": 0, "judgment_candidates": 0}

    for name in layer_names:
        result, judgment_rows = run_layer(name, LAYERS[name], vocab, generated_at)
        all_judgment_rows.extend(judgment_rows)
        for k in grand_totals:
            grand_totals[k] += result["counts"][k]

        out_path = OUTPUT_DIR / f"{name}.json"
        with out_path.open("w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
            f.write("\n")

        print(f"[{name}] total={result['counts']['total']} "
              f"pass={result['counts']['pass']} "
              f"pass_with_flags={result['counts']['pass_with_flags']} "
              f"judgment_candidates={result['counts']['judgment_candidates']}")

    if args.layer == "all":
        write_judgment_file(all_judgment_rows, generated_at)
        print(f"Wrote {JUDGMENT_PATH.relative_to(ROOT)} ({len(all_judgment_rows)} rows)")

    print(f"TOTAL pass={grand_totals['pass']} "
          f"pass_with_flags={grand_totals['pass_with_flags']} "
          f"judgment_candidates={grand_totals['judgment_candidates']}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
