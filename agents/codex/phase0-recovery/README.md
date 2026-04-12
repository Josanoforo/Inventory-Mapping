# Phase 0 Recovery Agent — Guía operativa

## Qué hace este agente

Recibe recovery packets que describen findings de Part 4 que no pudieron verificarse en la primera pasada de Phase 0 Data Gathering. Intenta recuperar cada finding via URL alternativa (cache, archive, mirrors) o re-búsqueda reconstruida desde el contenido original. Produce un shard markdown estándar que re-entra al pipeline por `input/data_gathering/shards/gpt_custom/`.

El agente no corre el shard automáticamente. Un humano deposita el shard y ejecuta `parse_dg_shard.py`.

## Formato del recovery packet

Ver `CONTRACT.md` — sección "Qué recibes". No se duplica aquí.

---

## Paso 1 — Generar los recovery packets

### Comando

```bash
python phases/00-data-gathering/scripts/part4_to_recovery_packets.py
```

### Output esperado

```
Part 4 total: 142 | excluidos (no_url_inferred): 11 | elegibles: 131
Done — batch: batch_YYYYMMDD_HHMMSS | packets: 131 | dir: working/data_gathering/recovery_packets/batch_YYYYMMDD_HHMMSS
```

Los archivos se escriben en:
```
working/data_gathering/recovery_packets/
└── batch_YYYYMMDD_HHMMSS/
    ├── packet_001.json
    ├── packet_002.json
    │   ...
    ├── packet_131.json
    └── manifest.json
```

### Verificación

```bash
# Debe retornar 131
ls working/data_gathering/recovery_packets/<batch_id>/packet_*.json | wc -l

# Debe retornar 131
python3 -c "import json,sys; m=json.load(open('working/data_gathering/recovery_packets/<batch_id>/manifest.json')); print(m['packet_count'])"

# No debe retornar nada (excluidos no entran al batch)
grep -r "91f3e7a0" working/data_gathering/recovery_packets/<batch_id>/
```

---

## Paso 2 — El agente procesa los packets

El agente Codex recibe los packets del batch y produce un shard markdown por batch (o por subconjunto, según la capacidad del run). Ver `CONTRACT.md` para la estructura de output del shard.

---

## Paso 3 — Depositar el shard de recovery

### Directorio de destino

```
input/data_gathering/shards/gpt_custom/
```

`parse_dg_shard.py` determina `source_tool` desde el nombre del directorio padre. Los shards en `gpt_custom/` reciben `source_tool = "gpt_custom"`.

### Convención de nombre de archivo

```
compass_artifact_recovery_<batch_id>_text_markdown.md
```

**Ejemplo:**
```
compass_artifact_recovery_batch_20260412_143000_text_markdown.md
```

**Rationale:**
- `compass_artifact_` — prefijo consistente con todos los shards existentes en `deep_search/`; `parse_dg_shard.py` no impone restricción de nombre pero el prefijo mantiene consistencia visual en los listados de directorio.
- `recovery_` — distingue los shards de recovery de los shards de investigación (que usan UUID o nombres como `domestika_d3_output`); permite grep fácil para auditoría.
- `_text_markdown` — convención de sufijo presente en todos los shards normalizados; `parse_dg_shard.py` deriva `shard_id` del stem del archivo (`Path(file).stem`), que se convierte en la clave para todos los archivos de output downstream. El sufijo preserva alineación con los demás shard IDs del pipeline.

Esta convención no existía antes. Este documento es su definición canónica.

---

## Paso 4 — Ejecutar parse_dg_shard.py

```bash
python phases/00-data-gathering/scripts/parse_dg_shard.py \
  input/data_gathering/shards/gpt_custom/compass_artifact_recovery_batch_YYYYMMDD_HHMMSS_text_markdown.md
```

**Output del parser:**
```
working/data_gathering/findings/<shard_id>__<finding_id>.json     ← Part 1 + Part 2
working/data_gathering/diagnostics/part_4/<shard_id>__<item_id>.json  ← Part 4 (unrecoverable)
working/data_gathering/diagnostics/qa_notes/<shard_id>_qa.json
```

Donde `shard_id = "compass_artifact_recovery_batch_YYYYMMDD_HHMMSS_text_markdown"`.

---

## Flujo completo de re-entrada al pipeline

```
1. Script genera packets
   working/data_gathering/recovery_packets/<batch_id>/packet_NNN.json

2. Agente Codex procesa packets → produce shard markdown

3. Humano deposita shard
   input/data_gathering/shards/gpt_custom/compass_artifact_recovery_<batch_id>_text_markdown.md

4. parse_dg_shard.py procesa el shard
   ├── direct_verified   → working/data_gathering/findings/  (Part 1)
   ├── indirect_verified → working/data_gathering/findings/  (Part 2)
   └── unrecoverable     → working/data_gathering/diagnostics/part_4/

5. Phase 1 (converter_prepare.py) recoge los findings de working/data_gathering/findings/
   junto con todos los demás findings — sin routing especial para recovery.
```

---

## Items excluidos del batch

**11 items** del shard `compass_artifact_wf-91f3e7a0-e214-48ce-917e-bc6552ab2ae7_text_markdown_normalized` están excluidos de los recovery packets.

**Razón:** `failure_mode = no_url_inferred`. El normalizer no preservó la URL por bloque cuando el shard original organizaba findings por categorías agregadas. La estrategia de recovery por URL no aplica, y la re-búsqueda no tiene contexto suficiente sin la URL de la fuente. Este bug se resuelve en una iteración separada del skill `p0-normalize-shard`.

La exclusión se aplica comparando el campo `shard_id` en el JSON (no el nombre de archivo), que es la fuente de verdad.

---

## Nota downstream: verification_status en shards de recovery

Los shards producidos por este agente usan tres valores para `verification_status`:

| Valor en shard | Significado | Equivalente anterior |
|---|---|---|
| `direct_verified` | Acceso directo a la fuente original | `direct_verified` (sin cambio) |
| `indirect_verified` | Recuperado vía cache/archive/mirror/re-búsqueda | `blocked_url_index_verified` |
| `unrecoverable` | Todas las estrategias fallaron | `could_not_verify` |

`parse_dg_shard.py` pasa `verification_status` como string sin validación — los nuevos valores no causan errores de parseo.

**Pre-flight antes del primer run del agente:** verificar que el template de Phase 1 en `phases/01-source-intake/reference/source_packet_conversion_template.md` mapea `indirect_verified` (equivalente semántico de `blocked_url_index_verified`). Si no existe entrada explícita para `indirect_verified`, agregarla antes de procesar los findings de recovery con el converter de Phase 1.
