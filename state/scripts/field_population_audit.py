#!/usr/bin/env python3
"""
field_population_audit.py

Deliverable B (real population audit). Read-only over working/, writes only
under state/output/. For every required field of the Extraction Record (27)
and the Signal Card (21), over the corpus currently on disk:

  - total records
  - how many have the field populated (present, non-null, non-empty)
  - how many are "vacio" (missing key / null / empty string / empty array),
    broken down by which of those it is
  - for fields with a closed enum: how many populated values fall outside
    the enum declared in the *.schema.json file, and separately how many
    fall outside the value set declared in pipeline_vocabulary.yaml
  - the static (per-field, not per-record) set difference between the
    schema's enum and the vocabulary's value set, in both directions

Per the operator's explicit correction: "el enum sale del schema, no de tu
criterio" was about not inventing enum values, not about picking schema
over pipeline_vocabulary.yaml. This script measures against BOTH and
reports where they disagree. It does not resolve the disagreement -- that
divergence is itself the deliverable.

working/index/card_index.jsonl does not exist in the current corpus (the
Inventory Mapping bridge has never run). That gap is reported by
field_lifecycle_trace.py (Deliverable A) and is intentionally NOT
reproduced or generated here.

Usage:
    python state/scripts/field_population_audit.py
    python state/scripts/field_population_audit.py --root /path/to/repo
"""

import argparse
import json
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required (pip install pyyaml).", file=sys.stderr)
    sys.exit(1)

MISSING = object()  # sentinel distinct from None: key absent from the JSON at all


# ============================================================================
# Schema enum resolution (walks $ref / oneOf / anyOf / items, same shape as
# the resolver already used by vocab_check.py at the repo root).
# ============================================================================

def resolve_ref(doc, ref):
    if not ref.startswith("#/"):
        return None
    node = doc
    for part in ref[2:].split("/"):
        if not isinstance(node, dict) or part not in node:
            return None
        node = node[part]
    return node


def resolve_schema_enum(doc, node, seen=None):
    seen = seen or set()
    enums = set()
    if not isinstance(node, dict):
        return enums
    ref = node.get("$ref")
    if isinstance(ref, str) and ref not in seen:
        target = resolve_ref(doc, ref)
        if target is not None:
            enums |= resolve_schema_enum(doc, target, seen | {ref})
    if isinstance(node.get("enum"), list):
        enums.update(v for v in node["enum"] if isinstance(v, str))
    for key in ("oneOf", "anyOf"):
        for branch in node.get(key) or []:
            enums |= resolve_schema_enum(doc, branch, seen)
    if "items" in node:
        enums |= resolve_schema_enum(doc, node["items"], seen)
    return enums


def schema_enum_for(doc, prop_name):
    node = (doc.get("properties") or {}).get(prop_name)
    if node is None:
        return None
    enums = resolve_schema_enum(doc, node)
    return enums or None


# ============================================================================
# pipeline_vocabulary.yaml resolution -- per field, per record-type scope.
# Only the fields that actually carry a closed enum in the two schemas are
# listed here. `vocab_key` / `scope_keys` name where in the YAML the
# applicable value set lives; `exclude` removes values documented in the
# YAML as not applicable to this record type.
# ============================================================================

def load_vocab(root):
    with (root / "pipeline_vocabulary.yaml").open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def vocab_values_actor(vocab):
    return set(vocab["actor"]["values"])


def vocab_values_simple(vocab, key):
    return set(vocab[key]["values"])


def vocab_values_uncertainties(vocab, phase_only_key):
    entry = vocab["uncertainties"]
    return set(entry["core"]) | set(entry[phase_only_key])


def vocab_values_pointer_type(vocab, include_source_record_ref):
    values = set(vocab["pointer_type"]["values"])
    if not include_source_record_ref:
        values = values - {"source_record_ref"}
    return values


# ============================================================================
# Value classification
# ============================================================================

def classify(value):
    if value is MISSING:
        return "missing_key"
    if value is None:
        return "null"
    if isinstance(value, str) and value == "":
        return "empty_string"
    if isinstance(value, list) and len(value) == 0:
        return "empty_array"
    if isinstance(value, dict) and len(value) == 0:
        return "empty_object"
    return "populated"


EMPTY_CLASSES = {"missing_key", "null", "empty_string", "empty_array", "empty_object"}


def as_items(value):
    """Normalize a populated enum-bearing value (string or array-of-string) to a list."""
    if isinstance(value, list):
        return value
    return [value]


# ============================================================================
# Corpus loading
# ============================================================================

def load_json_dir(directory: Path):
    records = []
    errors = []
    if not directory.exists():
        return records, errors
    for f in sorted(directory.glob("*.json")):
        try:
            records.append(json.loads(f.read_text(encoding="utf-8")))
        except (OSError, json.JSONDecodeError) as e:
            errors.append(f"{f}: {e}")
    return records, errors


# ============================================================================
# Field audit
# ============================================================================

def audit_scalar_field(records, field, schema_enum, vocab_values):
    """Audit a top-level field across all records. Returns a result dict."""
    class_counts = {c: 0 for c in ("missing_key", "null", "empty_string", "empty_array", "empty_object", "populated")}
    out_of_schema = 0
    out_of_vocab = 0
    for rec in records:
        val = rec.get(field, MISSING) if isinstance(rec, dict) else MISSING
        cls = classify(val)
        class_counts[cls] += 1
        if cls == "populated" and schema_enum is not None:
            items = as_items(val)
            if any(str(item) not in schema_enum for item in items):
                out_of_schema += 1
            if vocab_values is not None and any(str(item) not in vocab_values for item in items):
                out_of_vocab += 1
    total = len(records)
    vacios = sum(class_counts[c] for c in EMPTY_CLASSES)
    divergence = None
    if schema_enum is not None and vocab_values is not None:
        divergence = {
            "schema_only": sorted(schema_enum - vocab_values),
            "vocab_only": sorted(vocab_values - schema_enum),
        }
    return {
        "field": field,
        "total": total,
        "populated": class_counts["populated"],
        "vacios": vacios,
        "vacios_breakdown": {c: class_counts[c] for c in EMPTY_CLASSES},
        "has_enum": schema_enum is not None,
        "out_of_schema_enum": out_of_schema if schema_enum is not None else None,
        "out_of_vocab_enum": out_of_vocab if vocab_values is not None else None,
        "schema_enum": sorted(schema_enum) if schema_enum is not None else None,
        "vocab_enum": sorted(vocab_values) if vocab_values is not None else None,
        "schema_vocab_divergence": divergence,
    }


def audit_nested_pointer_type(records, get_pointer_objs, schema_enum, vocab_values, label):
    """Audit pointer_type across all pointer objects nested under `field` (object or array)."""
    class_counts = {c: 0 for c in ("missing_key", "null", "empty_string", "empty_array", "empty_object", "populated")}
    out_of_schema = 0
    out_of_vocab = 0
    total_instances = 0
    for rec in records:
        for ptr in get_pointer_objs(rec):
            total_instances += 1
            val = ptr.get("pointer_type", MISSING) if isinstance(ptr, dict) else MISSING
            cls = classify(val)
            class_counts[cls] += 1
            if cls == "populated" and schema_enum is not None:
                if str(val) not in schema_enum:
                    out_of_schema += 1
                if vocab_values is not None and str(val) not in vocab_values:
                    out_of_vocab += 1
    vacios = sum(class_counts[c] for c in EMPTY_CLASSES)
    divergence = None
    if schema_enum is not None and vocab_values is not None:
        divergence = {
            "schema_only": sorted(schema_enum - vocab_values),
            "vocab_only": sorted(vocab_values - schema_enum),
        }
    return {
        "field": label,
        "total": total_instances,
        "populated": class_counts["populated"],
        "vacios": vacios,
        "vacios_breakdown": {c: class_counts[c] for c in EMPTY_CLASSES},
        "has_enum": True,
        "out_of_schema_enum": out_of_schema,
        "out_of_vocab_enum": out_of_vocab,
        "schema_enum": sorted(schema_enum) if schema_enum is not None else None,
        "vocab_enum": sorted(vocab_values) if vocab_values is not None else None,
        "schema_vocab_divergence": divergence,
        "unit": "pointer instances (not records)",
    }


# ============================================================================
# Extraction Record audit
# ============================================================================

def audit_extraction_records(root, vocab):
    schema_path = root / "phases/01-source-intake/data-extraction/schemas/data_extraction_record.schema.json"
    schema_doc = json.loads(schema_path.read_text(encoding="utf-8"))
    fields = list(schema_doc["required"])

    records_dir = root / "working/data_extraction/records"
    records, load_errors = load_json_dir(records_dir)

    # field -> vocab value set (or None if the field has no vocab-registered enum)
    vocab_map = {
        "source_type": vocab_values_simple(vocab, "source_type"),
        "claim_type": vocab_values_simple(vocab, "claim_type"),
        "actor_level": vocab_values_actor(vocab),
        "product_type_if_explicit": vocab_values_simple(vocab, "product_type_if_explicit"),
        "metric_type": vocab_values_simple(vocab, "metric_type"),
        "evidence_role": vocab_values_simple(vocab, "evidence_role"),
        "uncertainties": vocab_values_uncertainties(vocab, "phase_1_only"),
    }

    results = []
    for field in fields:
        if field == "traceability_pointer":
            continue  # handled separately below (nested pointer_type)
        schema_enum = schema_enum_for(schema_doc, field)
        vocab_values = vocab_map.get(field)
        results.append(audit_scalar_field(records, field, schema_enum, vocab_values))

    # traceability_pointer itself: populated/empty at the object level (no enum)
    results.append(audit_scalar_field(records, "traceability_pointer", None, None))

    # nested: traceability_pointer.pointer_type
    ptr_schema_enum = None
    tp_node = schema_doc["properties"]["traceability_pointer"]
    ptr_schema_enum = resolve_schema_enum(schema_doc, tp_node["properties"]["pointer_type"])
    ptr_vocab_values = vocab_values_pointer_type(vocab, include_source_record_ref=False)

    def get_ptrs(rec):
        tp = rec.get("traceability_pointer") if isinstance(rec, dict) else None
        return [tp] if isinstance(tp, dict) else []

    results.append(audit_nested_pointer_type(
        records, get_ptrs, ptr_schema_enum, ptr_vocab_values,
        "traceability_pointer.pointer_type"
    ))

    return results, records, load_errors


# ============================================================================
# Signal Card audit
# ============================================================================

def audit_signal_cards(root, vocab):
    schema_path = root / "phases/02-signal-extraction/schemas/signal_card.schema.json"
    schema_doc = json.loads(schema_path.read_text(encoding="utf-8"))
    fields = list(schema_doc["required"])

    cards_dir = root / "working/signal_extraction/cards"
    records, load_errors = load_json_dir(cards_dir)

    vocab_map = {
        "actor_level": vocab_values_actor(vocab),
        "product_type_if_explicit": vocab_values_simple(vocab, "product_type_if_explicit"),
        "metric_type": vocab_values_simple(vocab, "metric_type"),
        "evidence_role": vocab_values_simple(vocab, "evidence_role"),
        "uncertainties": vocab_values_uncertainties(vocab, "phase_2_only"),
    }

    results = []
    for field in fields:
        if field == "traceability_pointers":
            continue  # handled separately below (nested pointer_type, array)
        schema_enum = schema_enum_for(schema_doc, field)
        vocab_values = vocab_map.get(field)
        results.append(audit_scalar_field(records, field, schema_enum, vocab_values))

    results.append(audit_scalar_field(records, "traceability_pointers", None, None))

    ptr_def = schema_doc["$defs"]["traceabilityPointer"]
    ptr_schema_enum = resolve_schema_enum(schema_doc, ptr_def["properties"]["pointer_type"])
    ptr_vocab_values = vocab_values_pointer_type(vocab, include_source_record_ref=True)

    def get_ptrs(rec):
        arr = rec.get("traceability_pointers") if isinstance(rec, dict) else None
        return [p for p in arr if isinstance(p, dict)] if isinstance(arr, list) else []

    results.append(audit_nested_pointer_type(
        records, get_ptrs, ptr_schema_enum, ptr_vocab_values,
        "traceability_pointers[].pointer_type"
    ))

    return results, records, load_errors


# ============================================================================
# Rendering
# ============================================================================

def render_markdown(title, results, total_records, load_errors, unit_label="registros"):
    out = [f"# {title}", ""]
    out.append(f"Corpus auditado: {total_records} {unit_label} en disco.")
    if load_errors:
        out.append(f"Archivos no parseables (excluidos del conteo): {len(load_errors)}")
        for e in load_errors:
            out.append(f"  - {e}")
    out.append("")
    out.append("Enum del schema = *.schema.json. Enum del vocabulario = pipeline_vocabulary.yaml, "
                "resuelto al scope de fase aplicable (phase_1 para Extraction Record, phase_2 para "
                "Signal Card en `uncertainties`; `pointer_type` excluye/incluye `source_record_ref` "
                "segun el tipo de registro, per nota del vocabulario). Divergencia = diferencia de "
                "conjuntos entre ambos enums, no resuelta.")
    out.append("")
    out.append("| Campo | N | Poblado | Vacio | Fuera de enum (schema) | Fuera de enum (vocab) | Divergencia schema<->vocab |")
    out.append("|---|---|---|---|---|---|---|")
    for r in results:
        if not r["has_enum"]:
            oos, oov, div = "N/A (sin enum)", "N/A (sin enum)", "N/A"
        else:
            oos = r["out_of_schema_enum"]
            oov = r["out_of_vocab_enum"] if r["out_of_vocab_enum"] is not None else "N/A (sin registro en vocab)"
            if r["schema_vocab_divergence"] is None:
                div = "N/A (campo sin registro en pipeline_vocabulary.yaml)"
            else:
                so = r["schema_vocab_divergence"]["schema_only"]
                vo = r["schema_vocab_divergence"]["vocab_only"]
                if not so and not vo:
                    div = "(ninguna)"
                else:
                    parts = []
                    if so:
                        parts.append(f"solo en schema: {so}")
                    if vo:
                        parts.append(f"solo en vocab: {vo}")
                    div = "; ".join(parts)
        field_label = r["field"] + (f" [{r['unit']}]" if r.get("unit") else "")
        out.append(f"| `{field_label}` | {r['total']} | {r['populated']} | {r['vacios']} | {oos} | {oov} | {div} |")
    out.append("")
    out.append("## Desglose de 'vacio' por campo")
    out.append("")
    out.append("| Campo | missing_key | null | empty_string | empty_array | empty_object |")
    out.append("|---|---|---|---|---|---|")
    for r in results:
        b = r["vacios_breakdown"]
        out.append(f"| `{r['field']}` | {b['missing_key']} | {b['null']} | {b['empty_string']} | {b['empty_array']} | {b['empty_object']} |")
    out.append("")
    return "\n".join(out)


def render_bridge_note():
    return (
        "# Nota — working/index/card_index.jsonl\n\n"
        "No existe en el corpus vigente (Inventory Mapping no se ha corrido). No se genera desde "
        "este script. Reportado como hallazgo en Deliverable A: "
        "`state/output/field_lifecycle_corpus_state_note.md`.\n"
    )


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    ap.add_argument("--out-dir", type=Path, default=None)
    args = ap.parse_args()

    root = args.root
    out_dir = args.out_dir or (root / "state" / "output")
    out_dir.mkdir(parents=True, exist_ok=True)

    vocab = load_vocab(root)

    er_results, er_records, er_errors = audit_extraction_records(root, vocab)
    sc_results, sc_records, sc_errors = audit_signal_cards(root, vocab)

    (out_dir / "field_population_extraction_records.md").write_text(
        render_markdown("Poblado real — Extraction Record", er_results, len(er_records), er_errors),
        encoding="utf-8",
    )
    (out_dir / "field_population_signal_cards.md").write_text(
        render_markdown("Poblado real — Signal Card", sc_results, len(sc_records), sc_errors),
        encoding="utf-8",
    )
    (out_dir / "field_population_card_index_note.md").write_text(render_bridge_note(), encoding="utf-8")

    raw = {
        "extraction_records": {
            "total": len(er_records),
            "load_errors": er_errors,
            "fields": er_results,
        },
        "signal_cards": {
            "total": len(sc_records),
            "load_errors": sc_errors,
            "fields": sc_results,
        },
    }
    (out_dir / "field_population_raw.json").write_text(json.dumps(raw, indent=2, ensure_ascii=False), encoding="utf-8")

    print("=" * 78)
    print("FIELD POPULATION AUDIT")
    print("=" * 78)
    print(f"Extraction Records: {len(er_records)} ({len(er_errors)} unparseable)")
    print(f"Signal Cards:       {len(sc_records)} ({len(sc_errors)} unparseable)")
    print()
    print("Fields with any out-of-schema-enum values (Extraction Record):")
    for r in er_results:
        if r["has_enum"] and r["out_of_schema_enum"]:
            print(f"  {r['field']}: {r['out_of_schema_enum']} / {r['total']}")
    print("Fields with any out-of-vocab-enum values (Extraction Record):")
    for r in er_results:
        if r["has_enum"] and r["out_of_vocab_enum"]:
            print(f"  {r['field']}: {r['out_of_vocab_enum']} / {r['total']}")
    print()
    print("Fields with any out-of-schema-enum values (Signal Card):")
    for r in sc_results:
        if r["has_enum"] and r["out_of_schema_enum"]:
            print(f"  {r['field']}: {r['out_of_schema_enum']} / {r['total']}")
    print("Fields with any out-of-vocab-enum values (Signal Card):")
    for r in sc_results:
        if r["has_enum"] and r["out_of_vocab_enum"]:
            print(f"  {r['field']}: {r['out_of_vocab_enum']} / {r['total']}")
    print()
    print("Static schema<->vocab divergences (Extraction Record):")
    for r in er_results:
        d = r.get("schema_vocab_divergence")
        if d and (d["schema_only"] or d["vocab_only"]):
            print(f"  {r['field']}: schema_only={d['schema_only']} vocab_only={d['vocab_only']}")
    print("Static schema<->vocab divergences (Signal Card):")
    for r in sc_results:
        d = r.get("schema_vocab_divergence")
        if d and (d["schema_only"] or d["vocab_only"]):
            print(f"  {r['field']}: schema_only={d['schema_only']} vocab_only={d['vocab_only']}")
    print()
    print(f"Output written to: {out_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
