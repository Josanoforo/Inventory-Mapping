"""
extraction_prepare.py — Extraction stage 1 (preparación mecánica).

Lee Source Packets validados de working/source_intake/packets/*.json,
y para cada snippet en cada packet genera un skeleton de Extraction Record
en working/data_extraction/skeleton_batches/ para que el stage 2 (skill LLM)
llene los campos de juicio.

Autoridad contractual declarada:
- phases/01-source-intake/data-extraction/contracts/data_extraction_contract.md
- phases/01-source-intake/data-extraction/schemas/data_extraction_record.schema.json

Este script hace solo trabajo mecánico: lectura de packets, expansión por
snippets, llenado de los campos mecánicos del Extraction Record. Los campos
de juicio (claim_type, subject_exact, actor_level, platforms,
product_type_if_explicit, metric_type, metric_value_raw, metric_unit,
time_scope_raw, time_scope_normalized_if_safe, geography_if_explicit,
evidence_role, local_qualifiers, uncertainties, parser_notes) quedan
vacíos o null — son trabajo del stage 2.

Idempotente: re-correr con el mismo input produce el mismo output.
Retomable: lee el manifest al arrancar y continúa desde el último batch escrito.

Uso:
    python phases/01-source-intake/data-extraction/scripts/extraction_prepare.py
    python phases/01-source-intake/data-extraction/scripts/extraction_prepare.py --batch-size 50
    python phases/01-source-intake/data-extraction/scripts/extraction_prepare.py --input-dir working/source_intake/packets
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

DEFAULT_INPUT_DIR = Path("working/source_intake/packets")
DEFAULT_OUTPUT_ROOT = Path("working/data_extraction")
DEFAULT_BATCH_SIZE = 25

SKELETON_BATCHES_DIR = "skeleton_batches"
MANIFEST_FILENAME = "extraction_prepare_manifest.json"

# Campos mecánicos requeridos en un Source Packet validado
REQUIRED_PACKET_FIELDS = (
    "packet_id",
    "source_id",
    "source_type",
    "source_title",
    "source_ref",
    "source_date_if_available",
    "author_or_actor_if_available",
    "snippets",
)

# Campos requeridos en cada snippet
REQUIRED_SNIPPET_FIELDS = (
    "snippet_id",
    "snippet_text",
    "context_before",
    "context_after",
    "location_pointer",
)


# ====================================================================
# Lectura y validación de packets
# ====================================================================

def read_all_packets(input_dir: Path):
    """
    Lee todos los .json en el directorio de Source Packets.
    Devuelve (packets_válidos, issues).
    """
    packets = []
    issues = []

    if not input_dir.exists():
        print(f"ERROR: input directory does not exist: {input_dir}", file=sys.stderr)
        sys.exit(1)

    json_files = sorted(input_dir.glob("*.json"))
    if not json_files:
        print(f"ERROR: no packets found in {input_dir}", file=sys.stderr)
        sys.exit(1)

    for f in json_files:
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            issues.append({
                "packet_id": f.stem,
                "issue_type": "json_parse_error",
                "detail": str(e),
            })
            continue

        # Validación mínima: campos mecánicos requeridos presentes
        missing = [field for field in REQUIRED_PACKET_FIELDS if field not in data]
        if missing:
            issues.append({
                "packet_id": data.get("packet_id", f.stem),
                "issue_type": "required_field_missing",
                "detail": f"Missing packet fields: {', '.join(missing)}",
            })
            continue

        snippets = data.get("snippets")
        if not isinstance(snippets, list) or len(snippets) == 0:
            issues.append({
                "packet_id": data["packet_id"],
                "issue_type": "no_snippets",
                "detail": "Packet has no snippets; cannot build any Extraction Record skeletons.",
            })
            continue

        packets.append(data)

    return packets, issues


# ====================================================================
# Construcción de skeletons
# ====================================================================

def build_skeletons_for_packet(packet: dict) -> tuple:
    """
    Para un Source Packet, construye un skeleton de Extraction Record por
    cada snippet. Devuelve (skeletons, snippet_issues).

    Campos mecánicos se copian directamente del packet/snippet.
    Campos de juicio se dejan vacíos o null para el stage 2.
    """
    skeletons = []
    snippet_issues = []

    packet_id = packet["packet_id"]
    source_id = packet["source_id"]
    source_type = packet["source_type"]
    source_title = packet.get("source_title") or ""
    source_ref = packet["source_ref"]
    source_date_if_available = packet.get("source_date_if_available")
    author_or_actor_if_available = packet.get("author_or_actor_if_available")

    for snippet in packet.get("snippets", []):
        # Validación mínima del snippet
        missing_snp = [f for f in REQUIRED_SNIPPET_FIELDS if f not in snippet]
        if missing_snp:
            snippet_issues.append({
                "packet_id": packet_id,
                "snippet_id": snippet.get("snippet_id", "unknown"),
                "issue_type": "snippet_field_missing",
                "detail": f"Missing snippet fields: {', '.join(missing_snp)}",
            })
            continue

        snippet_id = snippet["snippet_id"]
        extraction_id = f"ER-{packet_id}-{snippet_id}"

        # location_pointer del snippet sirve como traceability_pointer del record
        location_pointer = snippet["location_pointer"]

        skeleton = {
            # Identificación
            "extraction_id": extraction_id,

            # Campos mecánicos — copiados del packet/snippet
            "source_packet_id": packet_id,
            "source_id": source_id,
            "source_type": source_type,
            "source_title": source_title,
            "source_ref": source_ref,
            "source_date_if_available": source_date_if_available,
            "author_or_actor_if_available": author_or_actor_if_available,
            "snippet_primary": snippet["snippet_text"],
            "snippet_context_before": snippet.get("context_before"),
            "snippet_context_after": snippet.get("context_after"),
            "traceability_pointer": {
                "pointer_type": location_pointer.get("pointer_type"),
                "pointer_value": location_pointer.get("pointer_value"),
                "secondary_pointer": location_pointer.get("secondary_pointer"),
            },

            # Campos de juicio — vacíos; stage 2 los llena
            "claim_type": None,
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
            "parser_notes": [],

            # Metadata del stage 1
            "_extraction_stage": 1,
            "_source_snippet_id": snippet_id,
            "_source_finding_ids": packet.get("_source_finding_ids"),
        }
        skeletons.append(skeleton)

    return skeletons, snippet_issues


# ====================================================================
# Manifest
# ====================================================================

def compute_input_fingerprint(input_dir: Path) -> str:
    """
    Hash de los nombres y tamaños de todos los packets. Detecta si el
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
        filename = f"skeleton_{skeleton['extraction_id']}.json"
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
        description="Extraction stage 1 — prepare Extraction Record skeletons from Source Packets."
    )
    parser.add_argument(
        "--input-dir",
        type=Path,
        default=DEFAULT_INPUT_DIR,
        help=f"Directory with validated Source Packet JSONs (default: {DEFAULT_INPUT_DIR})",
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
    args = parser.parse_args()

    input_dir = args.input_dir
    output_root = args.output_root
    batch_size = args.batch_size
    manifest_path = output_root / MANIFEST_FILENAME

    # Calcular fingerprint del input actual
    current_fingerprint = compute_input_fingerprint(input_dir)

    # Leer manifest existente
    existing_manifest = load_manifest(manifest_path)

    if existing_manifest:
        status = existing_manifest.get("status")
        stored_fingerprint = existing_manifest.get("input_fingerprint")

        if status == "complete" and stored_fingerprint == current_fingerprint:
            print("Extraction stage 1 already complete for this input. Nothing to do.")
            print(f"  skeletons_written: {existing_manifest.get('skeletons_written')}")
            print(f"  batches_written:   {existing_manifest.get('batches_written')}")
            return 0

        if stored_fingerprint and stored_fingerprint != current_fingerprint:
            print(
                "WARNING: input fingerprint has changed since last run. "
                "The packets in the input directory are not the same as when "
                "the manifest was written. Refusing to run.",
                file=sys.stderr,
            )
            print(
                "To start fresh, delete working/data_extraction/skeleton_batches/ "
                "and working/data_extraction/extraction_prepare_manifest.json, then re-run.",
                file=sys.stderr,
            )
            return 2

    # Leer todos los packets
    packets, read_issues = read_all_packets(input_dir)
    print(f"Read {len(packets)} valid packets from {input_dir}")
    if read_issues:
        print(f"  ({len(read_issues)} packets had issues and were skipped)")

    # Construir skeletons en orden determinístico (orden alfabético de packet_id)
    all_skeletons = []
    all_snippet_issues = []

    for packet in sorted(packets, key=lambda p: p["packet_id"]):
        skeletons, snippet_issues = build_skeletons_for_packet(packet)
        all_skeletons.extend(skeletons)
        all_snippet_issues.extend(snippet_issues)

    print(f"Built {len(all_skeletons)} skeletons from {len(packets)} packets")
    if all_snippet_issues:
        print(f"  ({len(all_snippet_issues)} snippets had issues and were skipped)")

    # Determinar desde qué batch retomar
    start_batch = 1
    if existing_manifest and existing_manifest.get("status") == "in_progress":
        last_batch_written = existing_manifest.get("last_batch_written", 0)
        start_batch = last_batch_written + 1
        print(f"Resuming from batch {start_batch}")

    # Agregar todos los issues
    all_issues = list(read_issues) + all_snippet_issues

    # Inicializar manifest
    manifest = {
        "status": "in_progress",
        "packets_read": len(packets),
        "snippets_found": len(all_skeletons) + len(all_snippet_issues),
        "total_skeletons": len(all_skeletons),
        "skeletons_written": 0,
        "batches_written": 0,
        "batch_size": batch_size,
        "last_batch_written": 0,
        "issues": all_issues,
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

    print(f"\nExtraction stage 1 complete.")
    print(f"  Total skeletons written: {manifest['skeletons_written']}")
    print(f"  Total batches:           {manifest['batches_written']}")
    print(f"  Issues registered:       {len(manifest['issues'])}")
    print(f"  Manifest:                {manifest_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
