"""
converter_prepare.py — Converter stage 1 (preparación mecánica).

Lee findings producidos por parse_dg_shard.py desde
working/data_gathering/findings/*.json, los agrupa por URL de fuente, y
escribe esqueletos de Source Packet en working/source_intake/skeleton_batches/
para que el stage 2 (skill LLM) llene los campos de juicio.

Autoridad contractual declarada:
- upstream/source-intake/reference/source_packet_conversion_template.md
- upstream/source-intake/contracts/source_intake_contract.md

Este script hace solo trabajo mecánico: agrupación, normalización de URL,
llenado de los 11 campos mecánicos del Source Packet. Los 8 campos de juicio
(possible_subjects, possible_actor_levels, possible_metric_types,
possible_time_scopes, possible_geographies, uncertainties,
priority_for_source_first, traceability_status) quedan vacíos o null — son
trabajo del stage 2.

Idempotente: re-correr con el mismo input produce el mismo output.
Retomable: lee el manifest al arrancar y continúa desde el último batch escrito.

Uso:
    python upstream/source-intake/scripts/converter_prepare.py
    python upstream/source-intake/scripts/converter_prepare.py --batch-size 50
    python upstream/source-intake/scripts/converter_prepare.py --input-dir working/data_gathering/findings
"""

import sys
import json
import hashlib
import argparse
from pathlib import Path
from datetime import datetime, timezone
from collections import defaultdict


# ====================================================================
# Constantes
# ====================================================================

DEFAULT_INPUT_DIR = Path("working/data_gathering/findings")
DEFAULT_OUTPUT_ROOT = Path("working/source_intake")
DEFAULT_BATCH_SIZE = 25

SKELETON_BATCHES_DIR = "skeleton_batches"
MANIFEST_FILENAME = "converter_prepare_manifest.json"

# Valores válidos de source_tool heredados del parser de Phase 0
VALID_RETRIEVAL_METHODS = {"deep_search", "gpt_custom", "unknown"}

# Enum cerrado de source_type definido en source_packet.schema.json
SOURCE_TYPE_ENUM = {
    "platform_doc", "help_center", "pricing_page", "policy_page",
    "blog", "article", "report", "news", "reddit", "seller_forum",
    "buyer_review", "product_listing", "interview", "video_transcript",
    "pdf", "database_profile", "search_results_page", "unknown",
}

# Sinónimos: valores no estándar que aparecen en findings → valor canónico del enum
SOURCE_TYPE_SYNONYMS = {
    "help_article":          "help_center",
    "blog_post":             "blog",
    "marketplace_tool":      "platform_doc",
    "investigative_report":  "report",
    "industry_news":         "news",
    "review_platform":       "buyer_review",
    "social_media":          "unknown",
    "feature_page":          "platform_doc",
    "platform_help":         "help_center",
    "faq_page":              "help_center",
    "privacy_page":          "policy_page",
    "terms_page":            "policy_page",
    "developer_community":   "seller_forum",
}

# Nota estándar que se inserta en intake_notes cuando un packet viene de
# findings Part 2. El stage 2 la lee y aplica las consecuencias:
# - traceability_status -> weak
# - snippet_needs_reopen en uncertainties
# - priority_for_source_first capped at medium
PART_2_INHERITED_NOTE = (
    "Derived from Part 2 provisional findings; stage 2 must downgrade "
    "traceability_status to weak, add snippet_needs_reopen to uncertainties, "
    "and cap priority_for_source_first at medium."
)


# ====================================================================
# Normalización de source_type
# ====================================================================

def normalize_source_type(raw: str) -> str:
    """
    Normaliza un valor de source_type al enum cerrado del schema.

    Orden de resolución:
    1. Si ya está en el enum → devolver tal cual.
    2. Si tiene sufijo parentético (ej. "platform_doc (official forum response)"),
       quitar el paréntesis y verificar el stem contra el enum.
    3. Buscar en SOURCE_TYPE_SYNONYMS (valor completo y stem sin paréntesis).
    4. Si no hay match → emitir warning a stderr y devolver el valor original
       (para que Stage 2 o el operador lo detecte como schema_validation_failed).
    """
    if not raw:
        return "unknown"
    if raw in SOURCE_TYPE_ENUM:
        return raw
    # Quitar sufijo parentético
    stem = raw.split("(")[0].strip()
    if stem in SOURCE_TYPE_ENUM:
        return stem
    # Buscar en sinónimos (valor completo primero, luego stem)
    canonical = SOURCE_TYPE_SYNONYMS.get(raw) or SOURCE_TYPE_SYNONYMS.get(stem)
    if canonical:
        return canonical
    print(
        f"WARNING: source_type '{raw}' not in schema enum and not in synonym map; "
        "keeping original value. Add to SOURCE_TYPE_SYNONYMS if recurrent.",
        file=sys.stderr,
    )
    return raw


# ====================================================================
# Normalización de URL (mínima)
# ====================================================================

def normalize_url(url: str) -> str:
    """
    Normalización mínima de URL:
    - strip whitespace
    - lowercase del host (no del path)
    - quitar trailing slash del path
    - quitar fragmento (#anchor)
    - mantener query params intactos
    - mantener esquema (http vs https) intacto

    No quita 'www.'. No resuelve redirects. No canonicaliza paths relativos.
    Dos URLs ligeramente distintas producen dos packets distintos.
    """
    if not url:
        return ""

    url = url.strip()

    # Quitar fragmento
    if "#" in url:
        url = url.split("#", 1)[0]

    # Separar esquema, host, path
    if "://" in url:
        scheme, rest = url.split("://", 1)
        scheme = scheme.lower()
    else:
        scheme = ""
        rest = url

    # Separar host del path
    if "/" in rest:
        host, path = rest.split("/", 1)
        path = "/" + path
    else:
        host = rest
        path = ""

    host = host.lower()

    # Quitar trailing slash del path (pero no si path es solo "/")
    if len(path) > 1 and path.endswith("/"):
        path = path.rstrip("/")

    if scheme:
        return f"{scheme}://{host}{path}"
    return f"{host}{path}"


# ====================================================================
# Lectura y validación de findings
# ====================================================================

def read_all_findings(input_dir: Path):
    """
    Lee todos los .json en el directorio de findings.
    Devuelve (findings_válidos, issues).
    """
    findings = []
    issues = []

    if not input_dir.exists():
        print(f"ERROR: input directory does not exist: {input_dir}", file=sys.stderr)
        sys.exit(1)

    json_files = sorted(input_dir.glob("*.json"))
    if not json_files:
        print(f"ERROR: no findings found in {input_dir}", file=sys.stderr)
        sys.exit(1)

    for f in json_files:
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            issues.append({
                "finding_id": f.stem,
                "issue_type": "json_parse_error",
                "detail": str(e),
            })
            continue

        # Validación mínima de campos requeridos
        missing = []
        for required in ("finding_id", "source", "source_type", "shard_id"):
            if not data.get(required):
                missing.append(required)

        if missing:
            issues.append({
                "finding_id": data.get("finding_id", f.stem),
                "issue_type": "required_field_missing",
                "detail": f"Missing: {', '.join(missing)}",
            })
            continue

        if not data.get("verbatim_snippet"):
            issues.append({
                "finding_id": data["finding_id"],
                "issue_type": "snippet_missing",
                "detail": "Finding has no verbatim_snippet; cannot build packet snippet entry.",
            })
            continue

        findings.append(data)

    return findings, issues


# ====================================================================
# Agrupación
# ====================================================================

def group_findings_by_shard_and_url(findings):
    """
    Agrupa findings por (shard_id, URL normalizada).

    Devuelve un dict ordenado: {(shard_id, normalized_url): [findings...]}
    Los shards se procesan en orden alfabético. Dentro de cada shard, los
    URLs se procesan en orden alfabético. Esto garantiza ordering determinístico.

    Si el mismo URL aparece en múltiples shards, cada (shard, URL) es un
    grupo distinto y se registra un issue multi_shard_url.
    """
    # Primero: detectar URLs que aparecen en múltiples shards
    url_to_shards = defaultdict(set)
    for f in findings:
        normalized = normalize_url(f["source"])
        url_to_shards[normalized].add(f["shard_id"])

    multi_shard_urls = {u: s for u, s in url_to_shards.items() if len(s) > 1}

    # Agrupar por (shard, URL) en orden determinístico
    groups = defaultdict(list)
    for f in findings:
        normalized = normalize_url(f["source"])
        key = (f["shard_id"], normalized)
        groups[key].append(f)

    # Ordenar: primero por shard_id, luego por URL normalizada
    ordered_keys = sorted(groups.keys(), key=lambda k: (k[0], k[1]))
    ordered_groups = {k: groups[k] for k in ordered_keys}

    return ordered_groups, multi_shard_urls


# ====================================================================
# Derivación de source_title desde URL
# ====================================================================

def derive_title_from_url(url: str) -> str:
    """
    Deriva un source_title legible desde el path del URL.

    Lógica:
    1. Toma el último segmento significativo del path (ignorando segmentos
       vacíos y segmentos puramente numéricos de un solo componente).
    2. Quita prefijo numérico del estilo "32-" (número + guión al inicio).
    3. Reemplaza guiones y underscores por espacios.
    4. Title-case.
    5. Fallback al dominio si el path es vacío o solo "/".

    Ejemplos:
      https://help.payhip.com/article/32-getting-started → "Getting Started"
      https://backlinko.com/patreon-users               → "Patreon Users"
      https://reddit.com/r/Etsy/                        → "R Etsy"
      https://example.com/                              → "example.com"
    """
    if not url:
        return "Unknown Source"

    # Separar esquema + host + path
    if "://" in url:
        _, rest = url.split("://", 1)
    else:
        rest = url

    if "/" in rest:
        host, path = rest.split("/", 1)
        path = "/" + path
    else:
        host = rest
        path = ""

    # Quitar query params del path para este propósito
    if "?" in path:
        path = path.split("?", 1)[0]

    import re as _re

    # Extraer segmentos no vacíos del path
    segments = [s for s in path.split("/") if s.strip()]

    def _domain_fallback():
        domain = host.lower()
        if domain.startswith("www."):
            domain = domain[4:]
        return domain

    if not segments:
        return _domain_fallback()

    # Buscar el último segmento significativo (no puramente numérico,
    # no un dominio embebido en el path como "www.etsy.com")
    chosen = None
    for seg in reversed(segments):
        # Saltar segmentos puramente numéricos
        if _re.fullmatch(r"\d+", seg):
            continue
        # Saltar segmentos que parecen dominios (contienen punto + al menos 2 chars después)
        if _re.search(r"\.\w{2,}", seg):
            continue
        chosen = seg
        break

    if not chosen:
        return _domain_fallback()

    # Quitar prefijo numérico tipo "32-" o "123_"
    chosen = _re.sub(r"^\d+[-_]", "", chosen)

    # Reemplazar guiones y underscores por espacios
    chosen = chosen.replace("-", " ").replace("_", " ")

    # Limpiar espacios múltiples
    chosen = " ".join(chosen.split())

    if not chosen:
        return _domain_fallback()

    return chosen.title()


# ====================================================================
# Construcción de skeleton
# ====================================================================

def build_skeleton(packet_id, source_id, shard_id, normalized_url, findings_in_group, multi_shard_urls):
    """
    Construye un skeleton de Source Packet.
    Los 11 campos mecánicos se llenan, los 8 de juicio quedan vacíos/null.
    """
    # Heredar source_type del primer finding; normalizar al enum; detectar inconsistencias
    source_types = {f.get("source_type") for f in findings_in_group}
    if len(source_types) > 1:
        source_type = normalize_source_type(findings_in_group[0].get("source_type") or "")
        source_type_conflict = True
    else:
        source_type = normalize_source_type(findings_in_group[0].get("source_type") or "")
        source_type_conflict = False

    # source_date: la más antigua disponible, o null
    dates = [f.get("date") for f in findings_in_group if f.get("date")]
    source_date = min(dates) if dates else None

    # author: del primer finding que lo tenga (orden alfabético por finding_id)
    sorted_findings = sorted(findings_in_group, key=lambda x: x.get("finding_id", ""))
    author = None
    for f in sorted_findings:
        candidate = f.get("author_or_actor") or f.get("author")
        if candidate:
            author = candidate
            break

    # retrieval_method desde source_tool
    source_tool = sorted_findings[0].get("source_tool", "unknown")
    if source_tool not in VALID_RETRIEVAL_METHODS:
        retrieval_method = "unknown"
    else:
        retrieval_method = source_tool

    # Detectar si hay findings Part 2 en el grupo
    has_part_2 = any(
        (f.get("part") == 2 or f.get("part") == "2")
        and f.get("verification_status") != "indirect_verified"
        for f in findings_in_group
    )

    # Construir snippets
    snippets = []
    for i, f in enumerate(sorted_findings, start=1):
        snippet_id = f"SNP-{i:03d}"
        snippets.append({
            "snippet_id": snippet_id,
            "snippet_text": f.get("verbatim_snippet", ""),
            "context_before": None,
            "context_after": None,
            "location_pointer": {
                "pointer_type": "url",
                "pointer_value": normalized_url,
            },
            "source_finding_id": f.get("finding_id"),
            "finding_part": f.get("part"),
        })

    # intake_notes
    intake_notes = []
    if has_part_2:
        intake_notes.append(PART_2_INHERITED_NOTE)
    if source_type_conflict:
        intake_notes.append(
            f"Source type conflict across findings in same URL: {sorted(source_types)}. "
            f"Using first finding's value. Stage 2 should verify."
        )
    if normalized_url in multi_shard_urls:
        other_shards = sorted(multi_shard_urls[normalized_url] - {shard_id})
        intake_notes.append(
            f"URL also appears in other shards: {', '.join(other_shards)}. "
            f"Packet assigned to this shard by alphabetical order."
        )

    # Skeleton final
    skeleton = {
        # Identificación
        "packet_id": packet_id,
        "source_id": source_id,

        # Campos mecánicos
        "source_title": derive_title_from_url(normalized_url),
        "source_type": source_type,
        "source_ref": normalized_url,
        "source_date_if_available": source_date,
        "author_or_actor_if_available": author,
        "retrieval_method": retrieval_method,
        "retrieved_from": shard_id,
        "raw_search_context": None,
        "snippets": snippets,
        "intake_notes": intake_notes,

        # Campos de juicio (vacíos — stage 2 los llena)
        "possible_subjects": [],
        "possible_actor_levels": [],
        "possible_metric_types": [],
        "possible_time_scopes": [],
        "possible_geographies": None,
        "uncertainties": [],
        "priority_for_source_first": None,
        "traceability_status": None,

        # Metadata del converter
        "_converter_stage": 1,
        "_source_finding_ids": [f.get("finding_id") for f in sorted_findings],
    }

    return skeleton


# ====================================================================
# Manifest
# ====================================================================

def compute_input_fingerprint(input_dir: Path) -> str:
    """
    Hash de los nombres y tamaños de todos los findings. Detecta si el
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
        filename = f"skeleton_{skeleton['packet_id']}.json"
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
        description="Converter stage 1 — prepare Source Packet skeletons from Data Gathering findings."
    )
    parser.add_argument(
        "--input-dir",
        type=Path,
        default=DEFAULT_INPUT_DIR,
        help=f"Directory with finding JSONs (default: {DEFAULT_INPUT_DIR})",
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
            print("Converter stage 1 already complete for this input. Nothing to do.")
            print(f"  skeletons_written: {existing_manifest.get('skeletons_written')}")
            print(f"  batches_written: {existing_manifest.get('batches_written')}")
            return 0

        if stored_fingerprint and stored_fingerprint != current_fingerprint:
            print(
                "WARNING: input fingerprint has changed since last run. "
                "The findings in the input directory are not the same as when "
                "the manifest was written. Refusing to run.",
                file=sys.stderr,
            )
            print(
                "To start fresh, delete working/source_intake/skeleton_batches/ "
                "and working/source_intake/converter_prepare_manifest.json, then re-run.",
                file=sys.stderr,
            )
            return 2

    # Leer todos los findings
    findings, read_issues = read_all_findings(input_dir)
    print(f"Read {len(findings)} valid findings from {input_dir}")
    if read_issues:
        print(f"  ({len(read_issues)} findings had issues and were skipped)")

    # Agrupar
    groups, multi_shard_urls = group_findings_by_shard_and_url(findings)
    print(f"Grouped into {len(groups)} unique (shard, URL) combinations")
    if multi_shard_urls:
        print(f"  ({len(multi_shard_urls)} URLs appeared in multiple shards)")

    # Asignar IDs y construir skeletons en orden determinístico
    all_skeletons = []
    packet_counter_per_shard = defaultdict(int)

    for (shard_id, normalized_url), findings_in_group in groups.items():
        packet_counter_per_shard[shard_id] += 1
        seq = packet_counter_per_shard[shard_id]
        packet_id = f"SP-{shard_id}-{seq:03d}"
        source_id = f"SRC-{shard_id}-{seq:03d}"

        skeleton = build_skeleton(
            packet_id=packet_id,
            source_id=source_id,
            shard_id=shard_id,
            normalized_url=normalized_url,
            findings_in_group=findings_in_group,
            multi_shard_urls=multi_shard_urls,
        )
        all_skeletons.append(skeleton)

    # Determinar desde qué batch retomar
    start_batch = 1
    if existing_manifest and existing_manifest.get("status") == "in_progress":
        last_batch_written = existing_manifest.get("last_batch_written", 0)
        start_batch = last_batch_written + 1
        print(f"Resuming from batch {start_batch}")

    # Inicializar manifest
    manifest = {
        "status": "in_progress",
        "findings_read": len(findings),
        "unique_urls": len({normalize_url(f["source"]) for f in findings}),
        "total_skeletons": len(all_skeletons),
        "skeletons_written": 0,
        "batches_written": 0,
        "batch_size": batch_size,
        "last_batch_written": 0,
        "issues": list(read_issues),
        "input_fingerprint": current_fingerprint,
        "started_at": existing_manifest.get("started_at") if existing_manifest else now_iso(),
        "completed_at": None,
    }

    # Agregar issues por URLs multi-shard
    for url, shards in multi_shard_urls.items():
        manifest["issues"].append({
            "finding_id": None,
            "issue_type": "multi_shard_url",
            "detail": f"URL {url} appears in shards: {sorted(shards)}",
        })

    save_manifest(manifest_path, manifest)

    # Escribir batches
    total_batches = (len(all_skeletons) + batch_size - 1) // batch_size

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
    manifest["completed_at"] = now_iso()
    save_manifest(manifest_path, manifest)

    print(f"\nConverter stage 1 complete.")
    print(f"  Total skeletons written: {manifest['skeletons_written']}")
    print(f"  Total batches: {manifest['batches_written']}")
    print(f"  Issues registered: {len(manifest['issues'])}")
    print(f"  Manifest: {manifest_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
