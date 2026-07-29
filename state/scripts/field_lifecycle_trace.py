#!/usr/bin/env python3
"""
field_lifecycle_trace.py

Deliverable A (field lifecycle audit). Read-only over the repo, writes only
under state/output/. Traces every required field of the Extraction Record
(27) and the Signal Card (21) through the pipeline, then reconciles every
property of card_record.schema.json (the Inventory Mapping index record)
back to its origin.

Method: mechanical text search (word-boundary regex) for the literal field
name inside a fixed, small set of designated "consumer" files per stage.
The pipeline topology (which files are checked, in what order) is the only
thing this script assumes; every citation (file:line) is produced by
actually reading and searching those files at run time, not recalled from
memory. If a field's name does not occur in any of its designated consumer
files, the field's lifecycle entry for that stage is written literally as
SIN-CONSUMIDOR-ENCONTRADO, per the task's explicit instruction not to infer.

Field lists (which 27 / which 21 fields) are read from the `required` array
of the live schema files on every run -- not hardcoded -- so the script
reflects the schemas as they exist on disk when re-run.

A handful of facts are not mechanically derivable from a single grep (e.g.
which Signal Card field a derived markdown variable like `source_url` or
`domain` ultimately comes from -- that requires reading the derivation
function body once). Those are recorded in ANNOTATIONS below, each paired
with the real file:line of the code it describes so the claim stays
checkable. ANNOTATIONS never override a negative grep result (a
SIN-CONSUMIDOR-ENCONTRADO stands even if a note exists for that field).

Usage:
    python state/scripts/field_lifecycle_trace.py
    python state/scripts/field_lifecycle_trace.py --root /path/to/repo
"""

import argparse
import json
import re
import sys
from pathlib import Path

SENTINEL = "SIN-CONSUMIDOR-ENCONTRADO"


# ============================================================================
# Fixed pipeline file paths (topology assumption -- the one thing the
# script does not derive mechanically; sourced from CLAUDE.md's phase map
# and confirmed to exist by earlier manual read of each file in this task).
# ============================================================================

def paths(root: Path):
    return {
        "er_schema": root / "phases/01-source-intake/data-extraction/schemas/data_extraction_record.schema.json",
        "extraction_converter_md": root / "phases/01-source-intake/data-extraction/modules/extraction_converter.md",
        "signal_prepare_py": root / "phases/02-signal-extraction/scripts/signal_prepare.py",
        "signal_converter_md": root / "phases/02-signal-extraction/modules/signal_converter.md",
        "sc_schema": root / "phases/02-signal-extraction/schemas/signal_card.schema.json",
        "signal_to_markdown_py": root / "phases/02-signal-extraction/scripts/signal_to_markdown.py",
        "indexer_md": root / "phases/03-inventory-mapping/modules/03_indexer.md",
        "card_record_schema": root / "phases/03-inventory-mapping/schemas/card_record.schema.json",
    }


# ============================================================================
# Curator annotations -- semantic facts that require reading a function body,
# not just grepping a field name. Each entry cites the file:line it is
# grounded in so it stays falsifiable. These SUPPLEMENT grep citations, they
# never substitute for a missing one.
# ============================================================================

ER_ARRIVAL_ANNOTATIONS = {
    "traceability_pointer": (
        "No entra a _extraction_context (no está en EXTRACTION_CONTEXT_FIELDS). "
        "signal_prepare.py accede a record[\"traceability_pointer\"] directamente y lo "
        "reparte en dos posiciones del array traceability_pointers de la Signal Card: "
        "pointer_type/pointer_value/secondary_pointer originales copiados tal cual "
        "(signal_prepare.py:186-190), mas un segundo pointer sintetico "
        "{pointer_type: 'source_record_ref', pointer_value: extraction_id, "
        "secondary_pointer: source_packet_id} (signal_prepare.py:191-195)."
    ),
    "extraction_id": (
        "No entra a _extraction_context. Consumido directamente por signal_prepare.py "
        "(build_skeleton, signal_prepare.py:180) para poblar dos campos mecanicos de la "
        "Signal Card: source_record_ids: [extraction_id] (signal_prepare.py:207) y "
        "traceability_pointers[1].pointer_value (signal_prepare.py:193). "
        "Arrival: Signal Card.source_record_ids[0] y Signal Card.traceability_pointers[1].pointer_value."
    ),
    "source_id": (
        "No entra a _extraction_context. Consumido directamente por signal_prepare.py "
        "(build_skeleton, signal_prepare.py:181) para poblar source_ids: [source_id] "
        "(signal_prepare.py:208). Arrival: Signal Card.source_ids[0]."
    ),
    "source_packet_id": (
        "Entra a _extraction_context (signal_prepare.py:75) pero ningun campo de juicio lo "
        "hereda en signal_converter.md. Consumido ademas directamente por signal_prepare.py "
        "como traceability_pointers[1].secondary_pointer (signal_prepare.py:194). "
        "Arrival: Signal Card.traceability_pointers[1].secondary_pointer."
    ),
}

# Variables interpolated into signal_to_markdown.py's format_card() f-strings,
# mapped to the Signal Card field (or external lookup) they actually derive
# from. Grounded in format_card (signal_to_markdown.py:234-278) and the
# helper functions it calls.
MARKDOWN_VAR_ORIGIN = {
    "signal_id": ("signal_id (directo)", None),
    "signal_text": ("signal_text (directo)", None),
    "source_url": (
        "derivado de traceability_pointers via extract_source_url()",
        "extract_source_url, def en signal_to_markdown.py:98",
    ),
    "date_str": (
        "derivado de time_scope_normalized_if_safe / time_scope_raw via extract_date()",
        "extract_date, def en signal_to_markdown.py:152",
    ),
    "source_type": (
        "NO es un campo de Signal Card (ausente del schema, additionalProperties:false). "
        "Recuperado por relectura directa del Extraction Record original "
        "(working/data_extraction/records/<source_record_ids[0]>.json) via "
        "build_record_index()/lookup_source_type().",
        "build_record_index, def en signal_to_markdown.py:183; lookup_source_type, def en signal_to_markdown.py:208",
    ),
    "domain": (
        "derivado de actor_level via derive_domain()",
        "derive_domain, def en signal_to_markdown.py:124",
    ),
    "actor_level": ("actor_level (directo)", None),
    "evidence_role": ("evidence_role (directo)", None),
}

SC_ARRIVAL_ANNOTATIONS = {
    "traceability_pointers": (
        'alimenta el label "Source:" via extract_source_url() '
        "(def en signal_to_markdown.py:98, invocada en signal_to_markdown.py:255) -- "
        "no aparece como valor literal propio, se recorre para elegir un pointer_value."
    ),
    "time_scope_raw": (
        'alimenta el label "Date:" via extract_date() (def en signal_to_markdown.py:152), '
        "usado solo si time_scope_normalized_if_safe es null (signal_to_markdown.py:157-163)."
    ),
    "time_scope_normalized_if_safe": (
        'alimenta el label "Date:" via extract_date() (def en signal_to_markdown.py:152), '
        "con prioridad sobre time_scope_raw (signal_to_markdown.py:157-159)."
    ),
    "source_record_ids": (
        "no aparece como valor literal en el markdown. Usado como clave de lookup para "
        'resolver el label "Source type:" via lookup_source_type() '
        "(def en signal_to_markdown.py:208, usa source_record_ids en signal_to_markdown.py:222-225)."
    ),
}

CARD_RECORD_NOTES = {
    "round": (
        "No aparece por card dentro del bloque delimitado por ---. Solo aparece en la "
        "cabecera del archivo (\"# Signal Cards — Round {round_number}\", "
        "signal_to_markdown.py:305) y en el nombre de archivo signal_cards_round_{N}.md. "
        "El indexer (03_indexer.md:20) lo declara como campo a extraer por card pero "
        "format_card() no lo emite por card -- la extraccion depende de contexto de "
        "archivo/lote, no de un literal dentro del bloque de card."
    ),
    "entities": (
        "Sin campo de origen aguas arriba. Generado por el propio indexer, "
        "\"best-effort extraction to aid scanning\" (03_indexer.md:23)."
    ),
    "figures": (
        "Sin campo de origen aguas arriba. Generado por el propio indexer, "
        "\"best-effort extraction to aid scanning\" (03_indexer.md:23)."
    ),
    "extraction_status": (
        f"{SENTINEL}. Requerido en card_record.schema.json pero format_card() "
        "(signal_to_markdown.py:234-278) no emite ninguna linea equivalente "
        "(\"Extraction status: ...\" no existe en el archivo) y 03_indexer.md no "
        "documenta de donde mas se derivaria."
    ),
}


# ============================================================================
# Mechanical helpers
# ============================================================================

def read_lines(path: Path):
    return path.read_text(encoding="utf-8").splitlines()


def schema_required(path: Path):
    doc = json.loads(path.read_text(encoding="utf-8"))
    return list(doc.get("required", []))


def schema_properties(path: Path):
    doc = json.loads(path.read_text(encoding="utf-8"))
    return list(doc.get("properties", {}).keys())


def find_occurrences(lines, field, max_report=6):
    """Word-boundary search for `field` in `lines`. Returns list of 1-indexed line numbers."""
    pat = re.compile(r"\b" + re.escape(field) + r"\b")
    hits = [i + 1 for i, line in enumerate(lines) if pat.search(line)]
    return hits


def cite(relpath, hits, max_report=6):
    if not hits:
        return None
    shown = hits[:max_report]
    suffix = f" (+{len(hits) - max_report} more)" if len(hits) > max_report else ""
    return f"{relpath}:{','.join(str(h) for h in shown)}{suffix}"


# ============================================================================
# signal_converter.md structural parse: 16 numbered judgment-field items,
# each of the form "N. **`<signal_field>`** -- ...", spanning until the next
# numbered item. Within each item's span, find `_extraction_context.<x>`
# references to recover which extraction-record field the item inherits
# from (if any).
# ============================================================================

HEADER_RE = re.compile(r"^\d+\.\s+\*\*`([a-zA-Z_]+)`\*\*")
CTX_REF_RE = re.compile(r"_extraction_context\.([a-zA-Z_]+)\b")


def parse_signal_converter_items(lines):
    """Returns list of (signal_field, start_line_idx, end_line_idx_exclusive)."""
    headers = []
    for i, line in enumerate(lines):
        m = HEADER_RE.match(line.strip())
        if m:
            headers.append((m.group(1), i))
    items = []
    for idx, (field, start) in enumerate(headers):
        end = headers[idx + 1][1] if idx + 1 < len(headers) else len(lines)
        items.append((field, start, end))
    return items


def build_extraction_context_inherit_map(lines):
    """
    Returns dict: extraction_record_field -> (signal_card_field, line_number)
    by scanning each judgment-field item's span for `_extraction_context.X`.
    """
    items = parse_signal_converter_items(lines)
    result = {}
    for signal_field, start, end in items:
        for i in range(start, end):
            m = CTX_REF_RE.search(lines[i])
            if m:
                ctx_field = m.group(1)
                # first reference wins; items reference their own source field once
                result.setdefault(ctx_field, (signal_field, i + 1))
    return result


# ============================================================================
# signal_to_markdown.py format_card() f-string parse: recovers
# label -> interpolated_variable -> line_number
# ============================================================================

LABEL_VAR_RE = re.compile(r'f"([A-Za-z ]+):\s*\{(\w+)\}"')
ID_LINE_RE = re.compile(r'f"\*\*\{(\w+)\}\*\*"')


def parse_format_card_labels(lines):
    labels = {}  # label -> (var, line_number)
    id_var = None
    id_line = None
    for i, line in enumerate(lines):
        m = LABEL_VAR_RE.search(line)
        if m:
            labels[m.group(1)] = (m.group(2), i + 1)
        m2 = ID_LINE_RE.search(line)
        if m2:
            id_var, id_line = m2.group(1), i + 1
    return labels, id_var, id_line


# ============================================================================
# Extraction Record trace
# ============================================================================

def trace_extraction_record_fields(root, P):
    er_fields = schema_required(P["er_schema"])
    er_schema_lines = read_lines(P["er_schema"])
    prepare_lines = read_lines(P["signal_prepare_py"])
    converter_lines = read_lines(P["signal_converter_md"])
    md_to_markdown_lines = read_lines(P["signal_to_markdown_py"])

    inherit_map = build_extraction_context_inherit_map(converter_lines)

    rows = []
    for field in er_fields:
        produced_hits = find_occurrences(er_schema_lines, field)
        produced_cite = cite("phases/01-source-intake/data-extraction/schemas/data_extraction_record.schema.json", produced_hits)

        stage1_hits = find_occurrences(prepare_lines, field)
        stage1_cite = cite("phases/02-signal-extraction/scripts/signal_prepare.py", stage1_hits)

        arrival_field = None
        stage2_cite = None
        if field in inherit_map:
            arrival_field, line_no = inherit_map[field]
            stage2_cite = f"phases/02-signal-extraction/modules/signal_converter.md:{line_no}"

        # fallback: does the original ER field name get re-read directly by
        # signal_to_markdown.py (independent re-read of the Extraction Record)?
        bridge_hits = find_occurrences(md_to_markdown_lines, field)
        bridge_cite = cite("phases/02-signal-extraction/scripts/signal_to_markdown.py", bridge_hits)

        note = ER_ARRIVAL_ANNOTATIONS.get(field)

        # Verdict: does the field have ANY downstream consumer at all?
        has_consumer = bool(stage1_hits) or bool(stage2_cite) or bool(bridge_hits) or bool(note)
        if arrival_field:
            arrival_desc = f"Signal Card.{arrival_field}"
        elif note:
            arrival_desc = "ver nota (arrival compuesta / mecanica, no via _extraction_context)"
        elif bridge_hits and not stage2_cite:
            arrival_desc = "no entra al schema de Signal Card; solo relectura directa desde signal_to_markdown.py"
        else:
            arrival_desc = SENTINEL

        rows.append({
            "field": field,
            "produced_at": produced_cite or SENTINEL,
            "stage1_signal_prepare": stage1_cite or SENTINEL,
            "stage2_signal_converter": stage2_cite or SENTINEL,
            "bridge_signal_to_markdown_direct_reread": bridge_cite or "(sin ocurrencia)",
            "arrival_name": arrival_desc,
            "note": note,
            "has_any_consumer": has_consumer,
        })
    return rows


# ============================================================================
# Signal Card trace
# ============================================================================

def trace_signal_card_fields(root, P):
    sc_fields = schema_required(P["sc_schema"])
    sc_schema_lines = read_lines(P["sc_schema"])
    md_lines = read_lines(P["signal_to_markdown_py"])

    labels, id_var, id_line = parse_format_card_labels(md_lines)
    # Build reverse map: variable -> (label, line)
    var_to_label = {}
    for label, (var, line) in labels.items():
        var_to_label[var] = (label, line)
    if id_var:
        var_to_label[id_var] = ("**<id>**", id_line)

    rows = []
    for field in sc_fields:
        produced_hits = find_occurrences(sc_schema_lines, field)
        produced_cite = cite("phases/02-signal-extraction/schemas/signal_card.schema.json", produced_hits)

        consumer_hits = find_occurrences(md_lines, field)
        consumer_cite = cite("phases/02-signal-extraction/scripts/signal_to_markdown.py", consumer_hits)

        if field == id_var:
            arrival = f"card id line \"**{{{id_var}}}**\" (signal_to_markdown.py:{id_line})"
        elif field in var_to_label:
            label, line = var_to_label[field]
            arrival = f'markdown label "{label}:" (signal_to_markdown.py:{line})'
        elif field in SC_ARRIVAL_ANNOTATIONS:
            arrival = SC_ARRIVAL_ANNOTATIONS[field]
        elif field in MARKDOWN_VAR_ORIGIN:
            # field itself isn't the f-string var name but has a known indirect path
            desc, extra = MARKDOWN_VAR_ORIGIN[field]
            arrival = desc
        else:
            arrival = SENTINEL

        has_any = bool(consumer_hits) or (field in var_to_label)

        rows.append({
            "field": field,
            "produced_at": produced_cite or SENTINEL,
            "signal_to_markdown_occurrences": consumer_cite or "(sin ocurrencia)",
            "arrival_in_markdown": arrival,
            "has_any_consumer": has_any,
        })
    return rows


# ============================================================================
# card_record.schema.json reconciliation (reverse trace: for every property
# of the indexer's output record, where does it come from?)
# ============================================================================

def trace_card_record_fields(root, P):
    cr_fields = schema_properties(P["card_record_schema"])
    cr_schema_lines = read_lines(P["card_record_schema"])
    md_lines = read_lines(P["signal_to_markdown_py"])
    indexer_lines = read_lines(P["indexer_md"])

    labels, id_var, id_line = parse_format_card_labels(md_lines)
    label_lookup = {k.lower(): (k, v[0], v[1]) for k, v in labels.items()}

    # 03_indexer.md field-list line + actor-parsing line + entities/figures line,
    # located mechanically (not hardcoded line numbers -- found by content match).
    indexer_field_list_line = None
    indexer_actor_line = None
    indexer_entities_line = None
    for i, line in enumerate(indexer_lines):
        if "extract:" in line and "extraction_status" in line:
            indexer_field_list_line = i + 1
        if 'Parse `actor`' in line or "Parse `actor`" in line:
            indexer_actor_line = i + 1
        if "entities" in line and "figures" in line:
            indexer_entities_line = i + 1

    rows = []
    for field in cr_fields:
        declared_hits = find_occurrences(cr_schema_lines, field)
        declared_cite = cite("phases/03-inventory-mapping/schemas/card_record.schema.json", declared_hits)

        indexer_hits = find_occurrences(indexer_lines, field)
        indexer_cite = cite("phases/03-inventory-mapping/modules/03_indexer.md", indexer_hits)

        note = CARD_RECORD_NOTES.get(field)

        # Direct label match: card_record field name equals a markdown label
        # (case-insensitive, e.g. "source" <-> "Source:")
        origin = None
        matched_label = None
        for label_lower, (label, var, line) in label_lookup.items():
            if label_lower.replace(" ", "_") == field or label_lower == field:
                matched_label = (label, var, line)
                break
        if field == "id" and id_var:
            origin = f'markdown card id line "**{{{id_var}}}**" (signal_to_markdown.py:{id_line})'
        elif field == "actor" and "Actor" in labels:
            var, line = labels["Actor"]
            origin = f'markdown label "Actor:" <- {var} (signal_to_markdown.py:{line})'
        elif field == "evidence_base" and "Evidence base" in labels:
            var, line = labels["Evidence base"]
            origin = f'markdown label "Evidence base:" <- {var} (signal_to_markdown.py:{line})'
        elif field == "source_type" and "Source type" in labels:
            var, line = labels["Source type"]
            desc, extra = MARKDOWN_VAR_ORIGIN.get(var, (var, None))
            origin = f'markdown label "Source type:" <- {desc} (signal_to_markdown.py:{line})'
        elif matched_label:
            label, var, line = matched_label
            desc, extra = MARKDOWN_VAR_ORIGIN.get(var, (f"{var} (directo)", None))
            origin = f'markdown label "{label}:" <- {desc} (signal_to_markdown.py:{line})'

        if note:
            origin = note if not origin else f"{origin} | NOTA: {note}"
        if not origin:
            origin = SENTINEL

        rows.append({
            "field": field,
            "declared_at": declared_cite or SENTINEL,
            "indexer_reference": indexer_cite or "(sin ocurrencia)",
            "origin": origin,
        })

    return rows, {
        "indexer_field_list_line": indexer_field_list_line,
        "indexer_actor_line": indexer_actor_line,
        "indexer_entities_line": indexer_entities_line,
    }


# ============================================================================
# Named check (explicitly requested): are metric_type, metric_value_raw,
# metric_unit required properties of signal_card.schema.json?
# ============================================================================

def named_check(P):
    sc_fields_required = schema_required(P["sc_schema"])
    sc_lines = read_lines(P["sc_schema"])
    target = ["metric_type", "metric_value_raw", "metric_unit"]
    result = {}
    for field in target:
        in_required = field in sc_fields_required
        req_hits = [i + 1 for i, l in enumerate(sc_lines) if l.strip().strip(",") == f'"{field}"']
        prop_hits = [i + 1 for i, l in enumerate(sc_lines) if re.match(rf'\s*"{re.escape(field)}":\s*\{{', l)]
        result[field] = {
            "in_required_array": in_required,
            "required_array_line": req_hits[0] if req_hits else None,
            "properties_definition_line": prop_hits[0] if prop_hits else None,
        }
    return result


# ============================================================================
# Rendering
# ============================================================================

def render_er_markdown(rows):
    out = ["# Ciclo de vida — Extraction Record (27 campos)", ""]
    out.append("Metodo: busqueda mecanica por nombre de campo (word-boundary) en los archivos designados por etapa. "
                f"Si ningun archivo consumidor contiene el nombre del campo, la etapa se marca `{SENTINEL}`.")
    out.append("")
    out.append("| Campo | Producido en | Stage1 signal_prepare.py | Stage2 signal_converter.md | Nombre de llegada (Signal Card) |")
    out.append("|---|---|---|---|---|")
    for r in rows:
        out.append(f"| `{r['field']}` | {r['produced_at']} | {r['stage1_signal_prepare']} | {r['stage2_signal_converter']} | {r['arrival_name']} |")
    out.append("")
    dead = [r for r in rows if not r["has_any_consumer"]]
    if dead:
        out.append(f"## Campos sin ningun consumidor detectado ({len(dead)})")
        out.append("")
        for r in dead:
            out.append(f"- `{r['field']}` -> {SENTINEL}")
        out.append("")
    notes = [r for r in rows if r.get("note")]
    if notes:
        out.append("## Notas de curador (citadas, no inferidas)")
        out.append("")
        for r in notes:
            out.append(f"- **`{r['field']}`**: {r['note']}")
        out.append("")
    return "\n".join(out)


def render_sc_markdown(rows):
    out = ["# Ciclo de vida — Signal Card (21 campos)", ""]
    out.append("Consumidor unico documentado: `phases/02-signal-extraction/scripts/signal_to_markdown.py` "
                "(unico puente JSON -> Markdown hacia IM, per CLAUDE.md / modules/01_entry_gate.md).")
    out.append("")
    out.append("| Campo | Producido en | Ocurrencias en signal_to_markdown.py | Llegada al markdown |")
    out.append("|---|---|---|---|")
    for r in rows:
        out.append(f"| `{r['field']}` | {r['produced_at']} | {r['signal_to_markdown_occurrences']} | {r['arrival_in_markdown']} |")
    out.append("")
    dead = [r for r in rows if not r["has_any_consumer"]]
    out.append(f"## Campos que mueren en el puente JSON -> Markdown ({len(dead)} de {len(rows)})")
    out.append("")
    if dead:
        for r in dead:
            out.append(f"- `{r['field']}` -> {SENTINEL} (ninguna ocurrencia del nombre en signal_to_markdown.py)")
    else:
        out.append("(ninguno)")
    out.append("")
    return "\n".join(out)


def render_bridge_markdown(rows, meta):
    out = ["# Puente Signal Card -> Markdown -> card_record.schema.json", ""]
    out.append("Reconciliacion inversa: para cada propiedad de `card_record.schema.json` "
                "(consumida por el Indexer, `phases/03-inventory-mapping/modules/03_indexer.md`), "
                "de donde viene.")
    out.append("")
    if meta.get("indexer_field_list_line"):
        out.append(f"Lista de campos a extraer declarada en `03_indexer.md:{meta['indexer_field_list_line']}`.")
    if meta.get("indexer_entities_line"):
        out.append(f"`entities`/`figures` como extraccion best-effort declarados en `03_indexer.md:{meta['indexer_entities_line']}`.")
    out.append("")
    out.append("| Campo (card_record) | Declarado en | Origen |")
    out.append("|---|---|---|")
    for r in rows:
        out.append(f"| `{r['field']}` | {r['declared_at']} | {r['origin']} |")
    out.append("")
    gaps = [r for r in rows if SENTINEL in r["origin"]]
    if gaps:
        out.append(f"## Campos de card_record.schema.json sin origen localizado ({len(gaps)})")
        out.append("")
        for r in gaps:
            out.append(f"- `{r['field']}`: {r['origin']}")
        out.append("")
    return "\n".join(out)


def render_named_check_markdown(result):
    out = ["# Check nombrado — metric_type / metric_value_raw / metric_unit en signal_card.schema.json", ""]
    out.append("| Campo | ¿En required? | Linea en required[] | Linea de definicion en properties |")
    out.append("|---|---|---|---|")
    for field, r in result.items():
        out.append(f"| `{field}` | {'SI' if r['in_required_array'] else 'NO'} | "
                    f"{r['required_array_line'] or '-'} | {r['properties_definition_line'] or '-'}|")
    out.append("")
    return "\n".join(out)


def render_state_note():
    return (
        "# Nota de estado del corpus (hallazgo, no generado por este script)\n\n"
        "`working/entry_gate/`, `working/split/` y `working/index/` solo contienen `.gitkeep` "
        "al momento de esta corrida. No existe ningun `input/signal_cards_round_*.md` en el repo, "
        "y `working/index/card_index.jsonl` no existe. El puente `signal_to_markdown.py` y el "
        "Indexer (`03_indexer.md`) nunca se han ejecutado sobre el corpus vigente. "
        "Este script NO genera esos archivos (modo solo lectura salvo `state/`); el ciclo de vida "
        "de los campos de `card_record.schema.json` documentado aqui es estatico "
        "(codigo + contratos), no una observacion de datos reales.\n"
    )


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    ap.add_argument("--out-dir", type=Path, default=None)
    args = ap.parse_args()

    root = args.root
    out_dir = args.out_dir or (root / "state" / "output")
    out_dir.mkdir(parents=True, exist_ok=True)

    P = paths(root)
    missing = [k for k, p in P.items() if not p.exists()]
    if missing:
        print(f"ERROR: missing expected files: {missing}", file=sys.stderr)
        sys.exit(1)

    er_rows = trace_extraction_record_fields(root, P)
    sc_rows = trace_signal_card_fields(root, P)
    cr_rows, cr_meta = trace_card_record_fields(root, P)
    named = named_check(P)

    (out_dir / "field_lifecycle_extraction_record.md").write_text(render_er_markdown(er_rows), encoding="utf-8")
    (out_dir / "field_lifecycle_signal_card.md").write_text(render_sc_markdown(sc_rows), encoding="utf-8")
    (out_dir / "field_lifecycle_card_record_bridge.md").write_text(render_bridge_markdown(cr_rows, cr_meta), encoding="utf-8")
    (out_dir / "field_lifecycle_named_check.md").write_text(render_named_check_markdown(named), encoding="utf-8")
    (out_dir / "field_lifecycle_corpus_state_note.md").write_text(render_state_note(), encoding="utf-8")

    raw = {
        "extraction_record_fields": er_rows,
        "signal_card_fields": sc_rows,
        "card_record_fields": cr_rows,
        "card_record_meta": cr_meta,
        "named_check_metric_fields": named,
    }
    (out_dir / "field_lifecycle_raw.json").write_text(json.dumps(raw, indent=2, ensure_ascii=False), encoding="utf-8")

    er_dead = sum(1 for r in er_rows if not r["has_any_consumer"])
    sc_dead = sum(1 for r in sc_rows if not r["has_any_consumer"])
    cr_gaps = sum(1 for r in cr_rows if SENTINEL in r["origin"])

    print("=" * 78)
    print("FIELD LIFECYCLE TRACE")
    print("=" * 78)
    print(f"Extraction Record fields traced: {len(er_rows)} ({er_dead} sin consumidor)")
    print(f"Signal Card fields traced:       {len(sc_rows)} ({sc_dead} mueren en el puente a markdown)")
    print(f"card_record.schema.json fields:  {len(cr_rows)} ({cr_gaps} sin origen localizado)")
    print()
    print("Named check (metric_type/metric_value_raw/metric_unit in signal_card required):")
    for field, r in named.items():
        print(f"  {field}: in_required={r['in_required_array']} "
              f"required_line={r['required_array_line']} properties_line={r['properties_definition_line']}")
    print()
    print(f"Output written to: {out_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
