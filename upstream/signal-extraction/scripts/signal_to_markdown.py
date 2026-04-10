"""
signal_to_markdown.py — Signal Cards JSON → Markdown for IM Entry Gate.

Lee todas las Signal Cards JSON de working/signal_extraction/cards/*.json,
las agrupa por round, y escribe un archivo Markdown por round en
input/signal_cards_round_[N].md con el formato que el Entry Gate
(modules/01_entry_gate.md) y el Splitter (modules/02_splitter.md) esperan.

Formato de cada card en el Markdown:

    ---

    **SC-R[round]-[number]**

    Observation: [signal_text]

    Source: [URL del primer traceability_pointer de tipo url]

    Date: [time_scope_normalized_if_safe o time_scope_raw o ""]

    Source type: [source_type del Extraction Record de origen, o "unknown"]

    Domain: [derivado de actor_level]

    Evidence base: [evidence_role]

El separador --- es interpretado por el Splitter como delimitador entre
cards. Cada bloque delimitado por --- que contenga **SC-R es una card.

Campos derivados:

  source_type: No está en el schema de Signal Card (additionalProperties: false).
    El script busca el Extraction Record en working/data_extraction/records/
    usando source_record_ids[0] para recuperar source_type. Si no se encuentra,
    usa "unknown".

  domain: Derivado de actor_level según el mapping:
    buyer      → buyer
    seller     → seller
    product    → product
    marketplace → platform
    mixed      → market
    source     → not_specified
    unknown    → not_specified
    array      → el valor mapeado del primer elemento, o "market" si hay varios

  date: time_scope_normalized_if_safe si está disponible, si no time_scope_raw,
    si no "". No inventa fecha.

  source URL: El pointer_value del primer traceability_pointer con
    pointer_type == "url". Si no hay ninguno, usa el pointer_value del primero
    disponible. Si no hay ninguno, "".

Idempotente: re-correr sobreescribe los archivos de output (no hay estado).
Sin manifest: es una pasada de formateo, no un pipeline incremental.

Uso:
    python upstream/signal-extraction/scripts/signal_to_markdown.py
    python upstream/signal-extraction/scripts/signal_to_markdown.py --cards-dir working/signal_extraction/cards
    python upstream/signal-extraction/scripts/signal_to_markdown.py --output-dir input
"""

import sys
import json
import re
import argparse
from pathlib import Path
from collections import defaultdict


# ====================================================================
# Constantes
# ====================================================================

DEFAULT_CARDS_DIR = Path("working/signal_extraction/cards")
DEFAULT_RECORDS_DIR = Path("working/data_extraction/records")
DEFAULT_OUTPUT_DIR = Path("input")

# Mapa de actor_level → domain (enum del card_record schema)
ACTOR_LEVEL_TO_DOMAIN = {
    "buyer": "buyer",
    "seller": "seller",
    "product": "product",
    "marketplace": "platform",
    "mixed": "market",
    "source": "not_specified",
    "unknown": "not_specified",
}

# Pattern del signal_id para extraer round y número
SIGNAL_ID_PATTERN = re.compile(r"^SC-R(\d+)-(\d+)$")


# ====================================================================
# Extracción de campos de la Signal Card
# ====================================================================

def extract_source_url(traceability_pointers):
    """
    Devuelve el pointer_value del primer pointer de tipo 'url'.
    Si no hay ninguno, devuelve el pointer_value del primero disponible.
    Si no hay ninguno, devuelve "".
    """
    if not traceability_pointers:
        return ""

    # Primero: buscar pointer de tipo url
    for pointer in traceability_pointers:
        if isinstance(pointer, dict) and pointer.get("pointer_type") == "url":
            return pointer.get("pointer_value", "")

    # Fallback: primer pointer disponible que no sea source_record_ref
    for pointer in traceability_pointers:
        if isinstance(pointer, dict) and pointer.get("pointer_type") != "source_record_ref":
            return pointer.get("pointer_value", "")

    # Último recurso
    first = traceability_pointers[0]
    if isinstance(first, dict):
        return first.get("pointer_value", "")
    return ""


def derive_domain(actor_level):
    """
    Deriva el domain (enum del card_record schema) desde actor_level.

    actor_level puede ser un string o un array (el schema permite ambos).
    En caso de array:
    - Un solo elemento: aplica el mapa directamente.
    - Múltiples elementos distintos: retorna "market" si contiene buyer/seller/marketplace,
      o "not_specified" si solo contiene source/unknown.
    """
    if actor_level is None:
        return "not_specified"

    if isinstance(actor_level, list):
        if len(actor_level) == 0:
            return "not_specified"
        if len(actor_level) == 1:
            return ACTOR_LEVEL_TO_DOMAIN.get(actor_level[0], "not_specified")
        # Múltiples niveles: si hay algún nivel sustantivo → market
        substantive = {"buyer", "seller", "marketplace", "product", "mixed"}
        if any(a in substantive for a in actor_level):
            return "market"
        return "not_specified"

    # String
    return ACTOR_LEVEL_TO_DOMAIN.get(str(actor_level), "not_specified")


def extract_date(card):
    """
    Extrae el campo de fecha para el markdown.
    Prioridad: time_scope_normalized_if_safe → time_scope_raw → "".
    """
    normalized = card.get("time_scope_normalized_if_safe")
    if normalized:
        return str(normalized)

    raw = card.get("time_scope_raw")
    if raw:
        return str(raw)

    return ""


def parse_signal_id(signal_id):
    """
    Parsea SC-R[round]-[number] y devuelve (round_int, number_int).
    Devuelve None si el ID no coincide con el patrón.
    """
    m = SIGNAL_ID_PATTERN.match(signal_id)
    if not m:
        return None
    return int(m.group(1)), int(m.group(2))


# ====================================================================
# Lookup de source_type desde Extraction Records
# ====================================================================

def build_record_index(records_dir: Path) -> dict:
    """
    Lee todos los Extraction Records disponibles y construye un índice
    {extraction_id: source_type}.

    El índice se construye una sola vez al arrancar. Si el directorio
    no existe o está vacío, devuelve un diccionario vacío (graceful
    degradation — las cards tendrán source_type "unknown").
    """
    index = {}
    if not records_dir.exists():
        return index

    for f in records_dir.glob("*.json"):
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
            extraction_id = data.get("extraction_id") or f.stem
            source_type = data.get("source_type", "unknown")
            index[extraction_id] = source_type
        except (json.JSONDecodeError, OSError):
            continue

    return index


def lookup_source_type(card: dict, record_index: dict) -> str:
    """
    Recupera source_type para una Signal Card.

    Orden de preferencia:
    1. Si la card tiene source_type directamente (campo no canónico preservado).
    2. Busca el primer source_record_id en el record_index.
    3. Fallback: "unknown".
    """
    # 1. Campo directo (schema non-canonical but defensive)
    if card.get("source_type"):
        return str(card["source_type"])

    # 2. Lookup via source_record_ids
    source_record_ids = card.get("source_record_ids") or []
    for record_id in source_record_ids:
        if record_id in record_index:
            return record_index[record_id]

    return "unknown"


# ====================================================================
# Formateo de una card
# ====================================================================

def format_card(card: dict, source_type: str) -> str:
    """
    Formatea una Signal Card como bloque Markdown delimitado por ---.

    El bloque empieza con --- y contiene:
      **SC-R[round]-[number]**
      Observation: ...
      Source: ...
      Date: ...
      Source type: ...
      Domain: ...
      Evidence base: ...

    El --- final lo escribe el caller al concatenar los bloques.
    """
    signal_id = card.get("signal_id", "")
    signal_text = card.get("signal_text") or ""
    evidence_role = card.get("evidence_role") or ""
    traceability_pointers = card.get("traceability_pointers") or []
    actor_level = card.get("actor_level")

    source_url = extract_source_url(traceability_pointers)
    date_str = extract_date(card)
    domain = derive_domain(actor_level)

    lines = [
        f"**{signal_id}**",
        "",
        f"Observation: {signal_text}",
        "",
        f"Source: {source_url}",
        "",
        f"Date: {date_str}",
        "",
        f"Source type: {source_type}",
        "",
        f"Domain: {domain}",
        "",
        f"Evidence base: {evidence_role}",
        "",
    ]

    return "\n".join(lines)


# ====================================================================
# Escritura del archivo de round
# ====================================================================

def write_round_file(output_path: Path, round_number: int, cards_for_round: list, record_index: dict):
    """
    Escribe el archivo Markdown para un round dado.

    Formato del archivo:
    - Cabecera con round y conteo de cards.
    - Cards separadas por ---.
    - El archivo termina con ---.

    La secuencia --- (card block) --- es la que el Splitter identifica.
    """
    cards_sorted = sorted(
        cards_for_round,
        key=lambda c: parse_signal_id(c.get("signal_id", "SC-R0-000")) or (0, 0),
    )

    sections = []

    # Cabecera del archivo
    header = (
        f"# Signal Cards — Round {round_number}\n"
        f"\n"
        f"Total cards: {len(cards_sorted)}\n"
    )
    sections.append(header)

    # Una sección por card
    for card in cards_sorted:
        source_type = lookup_source_type(card, record_index)
        card_body = format_card(card, source_type)
        # Cada card está precedida y seguida por ---
        sections.append(f"---\n\n{card_body}")

    # Delimitador final
    sections.append("---\n")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(sections), encoding="utf-8")


# ====================================================================
# Main
# ====================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Convert Signal Card JSONs to Markdown files for IM Entry Gate."
    )
    parser.add_argument(
        "--cards-dir",
        type=Path,
        default=DEFAULT_CARDS_DIR,
        help=f"Directory with validated Signal Card JSONs (default: {DEFAULT_CARDS_DIR})",
    )
    parser.add_argument(
        "--records-dir",
        type=Path,
        default=DEFAULT_RECORDS_DIR,
        help=f"Directory with Extraction Records for source_type lookup (default: {DEFAULT_RECORDS_DIR})",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help=f"Output directory for signal_cards_round_N.md files (default: {DEFAULT_OUTPUT_DIR})",
    )
    args = parser.parse_args()

    cards_dir = args.cards_dir
    records_dir = args.records_dir
    output_dir = args.output_dir

    # Verificar directorio de input
    if not cards_dir.exists():
        print(f"ERROR: cards directory does not exist: {cards_dir}", file=sys.stderr)
        sys.exit(1)

    # Leer todas las Signal Cards
    json_files = sorted(cards_dir.glob("*.json"))
    if not json_files:
        print(f"ERROR: no Signal Card JSONs found in {cards_dir}", file=sys.stderr)
        sys.exit(1)

    print(f"Reading Signal Cards from {cards_dir}")

    cards_by_round = defaultdict(list)
    skipped = []

    for f in json_files:
        try:
            card = json.loads(f.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            skipped.append((f.name, f"json_parse_error: {e}"))
            continue

        signal_id = card.get("signal_id", "")
        parsed = parse_signal_id(signal_id)
        if not parsed:
            skipped.append((f.name, f"invalid signal_id: {signal_id!r}"))
            continue

        round_number, _ = parsed
        cards_by_round[round_number].append(card)

    total_cards = sum(len(v) for v in cards_by_round.values())
    print(f"  Found {total_cards} valid cards across {len(cards_by_round)} round(s)")
    if skipped:
        print(f"  Skipped {len(skipped)} files:")
        for name, reason in skipped:
            print(f"    {name}: {reason}")

    if total_cards == 0:
        print("ERROR: no valid Signal Cards found. Nothing to write.", file=sys.stderr)
        sys.exit(1)

    # Construir índice de source_type desde Extraction Records
    print(f"Building source_type index from {records_dir}")
    record_index = build_record_index(records_dir)
    if record_index:
        print(f"  Indexed {len(record_index)} extraction records for source_type lookup")
    else:
        print(f"  No extraction records found — source_type will be 'unknown' for all cards")

    # Escribir un archivo por round
    print(f"Writing Markdown files to {output_dir}")
    output_dir.mkdir(parents=True, exist_ok=True)

    for round_number in sorted(cards_by_round.keys()):
        cards_for_round = cards_by_round[round_number]
        output_path = output_dir / f"signal_cards_round_{round_number}.md"

        write_round_file(output_path, round_number, cards_for_round, record_index)

        print(f"  Wrote round {round_number}: {len(cards_for_round)} cards → {output_path}")

    print(f"\nDone.")
    print(f"  Total cards written: {total_cards}")
    print(f"  Round files written: {len(cards_by_round)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
