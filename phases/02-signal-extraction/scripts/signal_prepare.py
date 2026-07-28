"""
signal_prepare.py — Signal Extraction stage 1 (preparación mecánica).

Lee Extraction Records validados de working/data_extraction/records/*.json
y para cada record genera un skeleton de Signal Card en
working/signal_extraction/skeleton_batches/ para que el stage 2 (skill LLM)
formule la señal observacional y llene los campos de juicio.

Autoridad contractual declarada:
- phases/02-signal-extraction/contracts/signal_extraction_contract.md
- phases/02-signal-extraction/schemas/signal_card.schema.json

Este script hace solo trabajo mecánico: lectura de records, asignación de
signal_id (patrón SC-R1-NNN), construcción de traceability_pointers desde el
record, y copia de contexto de extracción para uso del stage 2. Los campos de
juicio (signal_text, subject_exact, actor_level, platforms,
product_type_if_explicit, metric_type, metric_value_raw, metric_unit,
time_scope_raw, time_scope_normalized_if_safe, geography_if_explicit,
evidence_role, local_qualifiers, uncertainties, normalization_notes,
extraction_notes) quedan vacíos o null — son trabajo del stage 2.

Nota sobre round: este script asigna round=1 porque estos skeletons
pertenecen al primer round del pipeline nuevo derivado de Source Packets
procesados. Si en el futuro se procesan rounds adicionales, se añadirá
--round como argumento.

Nota sobre splitting: un Extraction Record produce un skeleton de Signal Card
(relación 1:1). Si el record contiene múltiples claims discretos, el stage 2
puede dividirlo en múltiples Signal Cards usando IDs adicionales asignados
durante el stage 2. El manifest del stage 2 lleva el contador global de IDs.

Idempotente: re-correr con el mismo input produce el mismo output.
Retomable: lee el manifest al arrancar y continúa desde el último batch escrito.

Uso:
    python phases/02-signal-extraction/scripts/signal_prepare.py
    python phases/02-signal-extraction/scripts/signal_prepare.py --batch-size 50
    python phases/02-signal-extraction/scripts/signal_prepare.py --input-dir working/data_extraction/records
"""

import sys
import json
import hashlib
import argparse
from pathlib import Path
from datetime import datetime, timezone


# ====================================================================
# Constantes
# ====================================================================

DEFAULT_INPUT_DIR = Path("working/data_extraction/records")
DEFAULT_OUTPUT_ROOT = Path("working/signal_extraction")
DEFAULT_BATCH_SIZE = 25
DEFAULT_ROUND = 1

SKELETON_BATCHES_DIR = "skeleton_batches"
MANIFEST_FILENAME = "signal_prepare_manifest.json"

# Campos requeridos en un Extraction Record validado para poder construir
# el skeleton. Los demás se copian opcionalmente al _extraction_context.
REQUIRED_RECORD_FIELDS = (
    "extraction_id",
    "source_id",
    "traceability_pointer",
    "snippet_primary",
)

# Campos del Extraction Record que se copian al _extraction_context para
# uso del stage 2. El stage 2 los lee para formular la señal observacional
# y rellenar los campos de juicio.
EXTRACTION_CONTEXT_FIELDS = (
    "extraction_id",
    "source_packet_id",
    "source_id",
    "source_type",
    "source_title",
    "source_ref",
    "source_date_if_available",
    "author_or_actor_if_available",
    "snippet_primary",
    "snippet_context_before",
    "snippet_context_after",
    "claim_type",
    "subject_exact",
    "actor_level",
    "platforms",
    "product_type_if_explicit",
    "metric_type",
    "metric_value_raw",
    "metric_unit",
    "time_scope_raw",
    "time_scope_normalized_if_safe",
    "geography_if_explicit",
    "evidence_role",
    "local_qualifiers",
    "uncertainties",
    "parser_notes",
)


# ====================================================================
# Lectura y validación de Extraction Records
# ====================================================================

def read_all_records(input_dir: Path):
    """
    Lee todos los .json en el directorio de Extraction Records.
    Devuelve (records_válidos, issues).
    """
    records = []
    issues = []

    if not input_dir.exists():
        print(f"ERROR: input directory does not exist: {input_dir}", file=sys.stderr)
        sys.exit(1)

    json_files = sorted(input_dir.glob("*.json"))
    if not json_files:
        print(f"ERROR: no records found in {input_dir}", file=sys.stderr)
        sys.exit(1)

    for f in json_files:
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            issues.append({
                "record_id": f.stem,
                "issue_type": "json_parse_error",
                "detail": str(e),
            })
            continue

        # Validación mínima: campos mecánicos requeridos presentes y no vacíos
        missing = []
        for field in REQUIRED_RECORD_FIELDS:
            val = data.get(field)
            if val is None or val == "":
                missing.append(field)

        if missing:
            issues.append({
                "record_id": data.get("extraction_id", f.stem),
                "issue_type": "required_field_missing",
                "detail": f"Missing or empty fields: {', '.join(missing)}",
            })
            continue

        # Validación mínima del traceability_pointer
        tp = data.get("traceability_pointer")
        if not isinstance(tp, dict) or not tp.get("pointer_type") or not tp.get("pointer_value"):
            issues.append({
                "record_id": data.get("extraction_id", f.stem),
                "issue_type": "traceability_pointer_malformed",
                "detail": "traceability_pointer must be an object with pointer_type and pointer_value.",
            })
            continue

        records.append(data)

    return records, issues


# ====================================================================
# Construcción de skeletons
# ====================================================================

def build_skeleton(signal_id: str, record: dict, round_number: int) -> dict:
    """
    Construye un skeleton de Signal Card desde un Extraction Record.

    Campos mecánicos se llenan desde el record.
    Campos de juicio quedan vacíos o null para el stage 2.

    El _extraction_context copia los campos del record que el stage 2
    necesita para formular la señal y rellenar los campos de juicio,
    sin requerir que busque el record original.
    """
    extraction_id = record["extraction_id"]
    source_id = record["source_id"]
    tp = record["traceability_pointer"]

    # Construir traceability_pointers: origen de la fuente + referencia al record
    traceability_pointers = [
        {
            "pointer_type": tp.get("pointer_type"),
            "pointer_value": tp.get("pointer_value"),
            "secondary_pointer": tp.get("secondary_pointer"),
        },
        {
            "pointer_type": "source_record_ref",
            "pointer_value": extraction_id,
            "secondary_pointer": record.get("source_packet_id"),
        },
    ]

    # Copiar contexto de extracción para Stage 2
    extraction_context = {
        field: record.get(field)
        for field in EXTRACTION_CONTEXT_FIELDS
    }

    skeleton = {
        # Identificación (mecánica)
        "signal_id": signal_id,
        "source_record_ids": [extraction_id],
        "source_ids": [source_id],
        "round": round_number,
        "traceability_pointers": traceability_pointers,

        # Campos de juicio — vacíos; stage 2 los llena
        "signal_text": None,
        "subject_exact": None,
        "actor_level": None,
        "platforms": [],
        "product_type_if_explicit": None,
        "metric_type": None,
        "metric_value_raw": None,
        "metric_unit": None,
        "time_scope_raw": None,
        "time_scope_normalized_if_safe": None,
        "geography_if_explicit": None,
        "evidence_role": None,
        "local_qualifiers": [],
        "uncertainties": [],
        "normalization_notes": [],
        "extraction_notes": [],

        # Metadata del stage 1
        "_signal_stage": 1,
        "_source_extraction_id": extraction_id,
        "_extraction_context": extraction_context,
    }

    return skeleton


# ====================================================================
# Manifest
# ====================================================================

def compute_input_fingerprint(input_dir: Path) -> str:
    """
    Hash de los nombres y tamaños de todos los records. Detecta si el
    input cambió entre corridas.
    """
    h = hashlib.sha256()
    for f in sorted(input_dir.glob("*.json")):
        h.update(f.name.encode("utf-8"))
        h.update(str(f.stat().st_size).encode("utf-8"))
    return h.hexdigest()


def load_manifest(manifest_path: Path):
    if not manifest_path.exists():
        return None
    try:
        return json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None


def save_manifest(manifest_path: Path, manifest: dict):
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def now_iso():
    return datetime.now(timezone.utc).isoformat()


# ====================================================================
# Escritura de batches
# ====================================================================

def write_batch(output_root: Path, batch_num: int, skeletons_in_batch: list):
    """Escribe todos los skeletons de un batch a su subdirectorio."""
    batch_dir = output_root / SKELETON_BATCHES_DIR / f"batch_{batch_num:03d}"
    batch_dir.mkdir(parents=True, exist_ok=True)

    for skeleton in skeletons_in_batch:
        filename = f"skeleton_{skeleton['signal_id']}.json"
        path = batch_dir / filename
        path.write_text(
            json.dumps(skeleton, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )


# ====================================================================
# Main
# ====================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Signal Extraction stage 1 — prepare Signal Card skeletons from Extraction Records."
    )
    parser.add_argument(
        "--input-dir",
        type=Path,
        default=DEFAULT_INPUT_DIR,
        help=f"Directory with validated Extraction Record JSONs (default: {DEFAULT_INPUT_DIR})",
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT,
        help=f"Output root directory (default: {DEFAULT_OUTPUT_ROOT})",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=DEFAULT_BATCH_SIZE,
        help=f"Number of skeletons per batch (default: {DEFAULT_BATCH_SIZE})",
    )
    parser.add_argument(
        "--round",
        type=int,
        default=DEFAULT_ROUND,
        help=f"Round number to assign to Signal Card skeletons (default: {DEFAULT_ROUND})",
    )
    args = parser.parse_args()

    input_dir = args.input_dir
    output_root = args.output_root
    batch_size = args.batch_size
    round_number = args.round
    manifest_path = output_root / MANIFEST_FILENAME

    # Calcular fingerprint del input actual
    current_fingerprint = compute_input_fingerprint(input_dir)

    # Leer manifest existente
    existing_manifest = load_manifest(manifest_path)

    if existing_manifest:
        status = existing_manifest.get("status")
        stored_fingerprint = existing_manifest.get("input_fingerprint")

        if status == "complete" and stored_fingerprint == current_fingerprint:
            print("Signal Extraction stage 1 already complete for this input. Nothing to do.")
            print(f"  skeletons_written: {existing_manifest.get('skeletons_written')}")
            print(f"  batches_written:   {existing_manifest.get('batches_written')}")
            return 0

        if stored_fingerprint and stored_fingerprint != current_fingerprint:
            print(
                "WARNING: input fingerprint has changed since last run. "
                "The records in the input directory are not the same as when "
                "the manifest was written. Refusing to run.",
                file=sys.stderr,
            )
            print(
                "To start fresh, delete working/signal_extraction/skeleton_batches/ "
                "and working/signal_extraction/signal_prepare_manifest.json, then re-run.",
                file=sys.stderr,
            )
            return 2

    # Leer todos los records
    records, read_issues = read_all_records(input_dir)
    print(f"Read {len(records)} valid records from {input_dir}")
    if read_issues:
        print(f"  ({len(read_issues)} records had issues and were skipped)")

    # Construir skeletons en orden determinístico (orden alfabético de extraction_id)
    all_skeletons = []
    sorted_records = sorted(records, key=lambda r: r["extraction_id"])

    for seq, record in enumerate(sorted_records, start=1):
        signal_id = f"SC-R{round_number}-{seq:03d}"
        skeleton = build_skeleton(signal_id, record, round_number)
        all_skeletons.append(skeleton)

    print(f"Built {len(all_skeletons)} skeletons from {len(records)} records")

    # Determinar desde qué batch retomar
    start_batch = 1
    if existing_manifest and existing_manifest.get("status") == "in_progress":
        last_batch_written = existing_manifest.get("last_batch_written", 0)
        start_batch = last_batch_written + 1
        print(f"Resuming from batch {start_batch}")

    # Inicializar manifest
    manifest = {
        "status": "in_progress",
        "round": round_number,
        "records_read": len(records),
        "total_skeletons": len(all_skeletons),
        "skeletons_written": 0,
        "batches_written": 0,
        "batch_size": batch_size,
        "last_batch_written": 0,
        "signal_id_counter_at_stage1": len(all_skeletons),
        "issues": list(read_issues),
        "input_fingerprint": current_fingerprint,
        "started_at": existing_manifest.get("started_at") if existing_manifest else now_iso(),
        "completed_at": None,
    }

    save_manifest(manifest_path, manifest)

    # Escribir batches
    total_batches = (len(all_skeletons) + batch_size - 1) // batch_size if all_skeletons else 0

    for batch_num in range(1, total_batches + 1):
        if batch_num < start_batch:
            continue

        start_idx = (batch_num - 1) * batch_size
        end_idx = start_idx + batch_size
        batch_skeletons = all_skeletons[start_idx:end_idx]

        write_batch(output_root, batch_num, batch_skeletons)

        # Actualizar manifest después de cada batch
        manifest["batches_written"] = batch_num
        manifest["last_batch_written"] = batch_num
        manifest["skeletons_written"] = min(batch_num * batch_size, len(all_skeletons))
        save_manifest(manifest_path, manifest)

        print(f"Wrote batch {batch_num:03d} ({len(batch_skeletons)} skeletons)")

    # Finalizar
    manifest["status"] = "complete"
    manifest["skeletons_written"] = len(all_skeletons)
    manifest["completed_at"] = now_iso()
    save_manifest(manifest_path, manifest)

    print(f"\nSignal Extraction stage 1 complete.")
    print(f"  Round:                   {round_number}")
    print(f"  Total skeletons written: {manifest['skeletons_written']}")
    print(f"  Total batches:           {manifest['batches_written']}")
    print(f"  Signal ID range:         SC-R{round_number}-001 … SC-R{round_number}-{len(all_skeletons):03d}")
    print(f"  Issues registered:       {len(manifest['issues'])}")
    print(f"  Manifest:                {manifest_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
