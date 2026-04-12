#!/usr/bin/env python3
"""
part4_to_recovery_packets.py — Genera recovery packets desde los diagnósticos Part 4.

Lee todos los JSON de working/data_gathering/diagnostics/part_4/, excluye los 11 items
del shard con bug de normalizer (wf-91f3e7a0), y escribe un recovery packet JSON por
cada item elegible en un directorio de batch con timestamp.

Autoridad contractual:
    agents/codex/phase0-recovery/CONTRACT.md

Fuente:
    working/data_gathering/diagnostics/part_4/*.json

Salida:
    working/data_gathering/recovery_packets/batch_YYYYMMDD_HHMMSS/packet_NNN.json
    working/data_gathering/recovery_packets/batch_YYYYMMDD_HHMMSS/manifest.json

Output esperado: 131 packets (142 total - 11 excluidos).

Uso:
    python phases/00-data-gathering/scripts/part4_to_recovery_packets.py
"""

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent.parent
PART4_DIR = REPO_ROOT / "working" / "data_gathering" / "diagnostics" / "part_4"
RECOVERY_DIR = REPO_ROOT / "working" / "data_gathering" / "recovery_packets"

# ---------------------------------------------------------------------------
# Exclusión — shard con bug de normalizer (failure_mode = no_url_inferred)
# Los 11 items de este shard no entran al agente de recovery.
# Se resuelven en una iteración separada del skill p0-normalize-shard.
# ---------------------------------------------------------------------------

EXCLUDED_SHARD_ID = (
    "compass_artifact_wf-91f3e7a0-e214-48ce-917e-bc6552ab2ae7_text_markdown_normalized"
)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

_UUID_PAT = re.compile(
    r"wf-([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})",
    re.IGNORECASE,
)


def _shard_id_abbrev(shard_id: str) -> str:
    """Extrae los últimos 8 caracteres del UUID del shard_id para recovery_id.

    Ejemplo: 'compass_artifact_wf-63c228bc-...' → '3f62e873' (últimos 8 del UUID sin guiones).
    Si no hay UUID (shard_id legacy), usa los últimos 8 caracteres alfanuméricos del stem.
    """
    m = _UUID_PAT.search(shard_id)
    if m:
        uuid_stripped = m.group(1).replace("-", "")
        return uuid_stripped[-8:]
    safe = re.sub(r"[^a-zA-Z0-9]", "", shard_id)
    return safe[-8:] if len(safe) >= 8 else safe


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


# ---------------------------------------------------------------------------
# Core
# ---------------------------------------------------------------------------


def load_eligible_items() -> tuple[list[dict], int, int]:
    """Carga todos los Part 4 JSON y filtra los excluidos.

    Returns: (eligible_items, total_count, excluded_count)
    """
    if not PART4_DIR.exists():
        print(f"ERROR: directorio no encontrado: {PART4_DIR}", file=sys.stderr)
        sys.exit(1)

    all_files = sorted(PART4_DIR.glob("*.json"))
    total = len(all_files)
    items = []
    excluded = 0

    for path in all_files:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            print(f"WARNING: JSON inválido en {path.name}: {e}", file=sys.stderr)
            continue

        if data.get("shard_id") == EXCLUDED_SHARD_ID:
            excluded += 1
            continue

        items.append(data)

    print(
        f"Part 4 total: {total} | excluidos (no_url_inferred): {excluded} "
        f"| elegibles: {len(items)}",
        file=sys.stderr,
    )
    return items, total, excluded


def make_recovery_packet(item: dict, packet_num: int) -> dict:
    """Convierte un Part 4 JSON en un recovery packet según CONTRACT.md."""
    shard_id = item["shard_id"]
    abbrev = _shard_id_abbrev(shard_id)
    recovery_id = f"REC-{abbrev}-{packet_num:03d}"

    urls = item.get("urls_mentioned") or []
    # Usar la primera URL mencionada; null si no hay ninguna.
    # Nota: algunas URLs pueden tener trailing commas por el extractor del parser —
    # se pasan tal cual; el agente de recovery evaluará la URL.
    original_url = urls[0] if urls else None

    why_failed = item.get("why_failed", "").strip()
    failure_mode = why_failed if why_failed else None

    return {
        "recovery_id": recovery_id,
        "finding_id": item["item_id"],
        "shard_id": shard_id,
        "original_url": original_url,
        "failure_mode": failure_mode,
        "original_finding_content": {
            "subject": item.get("seller_or_subject", ""),
            "raw_text": item.get("attempted", ""),
        },
    }


def make_manifest(
    batch_id: str,
    total: int,
    excluded: int,
    items: list[dict],
    packets_index: dict[str, str],
) -> dict:
    return {
        "batch_id": batch_id,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_part4_items": total,
        "excluded_count": excluded,
        "excluded_shard_id": EXCLUDED_SHARD_ID,
        "packet_count": len(items),
        "packets": packets_index,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    batch_id = datetime.now(timezone.utc).strftime("batch_%Y%m%d_%H%M%S")
    batch_dir = RECOVERY_DIR / batch_id

    items, total, excluded = load_eligible_items()

    packets_index: dict[str, str] = {}
    for num, item in enumerate(items, start=1):
        packet = make_recovery_packet(item, num)
        filename = f"packet_{num:03d}.json"
        write_json(batch_dir / filename, packet)
        key = f"{item['item_id']} (from {item['shard_id']})"
        packets_index[key] = filename

    manifest = make_manifest(batch_id, total, excluded, items, packets_index)
    write_json(batch_dir / "manifest.json", manifest)

    print(
        f"Done — batch: {batch_id} | packets: {len(items)} | dir: {batch_dir}"
    )


if __name__ == "__main__":
    main()
