# Phase 0 Recovery Agent — Guía operativa

## Qué hace este agente

Recibe recovery packets que describen findings de Part 4 que no pudieron verificarse en la primera pasada de Phase 0 Data Gathering. Intenta recuperar cada finding via URL alternativa (cache, archive, mirrors) o re-búsqueda reconstruida desde el contenido original. Produce un shard markdown estándar que re-entra al pipeline por `input/data_gathering/shards/gpt_custom/`.

El agente no corre el shard automáticamente. Un humano deposita el shard y ejecuta `parse_dg_shard.py`.

---

## Arquitectura del contrato

**A partir de D-167, el contrato de este agente es modular compartido.** El `CONTRACT.md` específico del recovery es corto (~310 líneas) y hereda los protocolos base desde `agents/codex/_shared/protocols/`:

- `_shared/protocols/core_protocol.md` — rol base, principios no negociables, single-source, multi-speaker, Clarificaciones 1-3, edge cases de verificación, `source_type`, `verification_status`, herramientas de acceso web, guardrails anti-drift.
- `_shared/protocols/output_contract.md` — estructura obligatoria, Finding ID convention, campos por finding, absence findings format, QA.
- `_shared/protocols/search_decomposition_rules.md` — reglas de descomposición del input en sub-búsquedas.
- `_shared/protocols/output_template.md` — template base con 4 Parts.

**Lo que vive solo en `phase0-recovery/CONTRACT.md`:**
- Estructura del recovery packet JSON y cómo tratar `original_finding_content` como input de research.
- Clarificación 4 (qué significa "recuperar" en contexto recovery).
- Regla 15 (test operativo de scope contra el claim del packet).
- Template extendido con Parts 1B/2B para adjacent findings (`F-ANN`, `F-APNN`).
- QA adicional del recovery (4 puntos específicos).
- Convención de naming del shard output.

Si hay contradicción entre `CONTRACT.md` y cualquier protocolo compartido, los protocolos compartidos mandan salvo que la excepción esté declarada explícitamente en el CONTRACT (dos excepciones declaradas: Parts 1B/2B y el test de scope de Regla 15).

---

## Formato del recovery packet

Ver `CONTRACT.md` — sección "Qué recibes". No se duplica aquí.

---

## Paso 1 — Generar los recovery packets

### Comando

~~~bash
python phases/00-data-gathering/scripts/part4_to_recovery_packets.py
~~~

### Output esperado

~~~
Part 4 total: 142 | excluidos (no_url_inferred): 11 | elegibles: 131
Done — batch: batch_YYYYMMDD_HHMMSS | packets: 131 | dir: working/data_gathering/recovery_packets/batch_YYYYMMDD_HHMMSS
~~~

Los archivos se escriben en:

~~~
working/data_gathering/recovery_packets/
└── batch_YYYYMMDD_HHMMSS/
    ├── packet_001.json
    ├── packet_002.json
    │   ...
    ├── packet_131.json
    └── manifest.json
~~~

### Verificación

~~~bash
# Debe retornar 131
ls working/data_gathering/recovery_packets/<batch_id>/packet_*.json | wc -l

# Debe retornar 131
python3 -c "import json,sys; m=json.load(open('working/data_gathering/recovery_packets/<batch_id>/manifest.json')); print(m['packet_count'])"

# No debe retornar nada (excluidos no entran al batch)
grep -r "91f3e7a0" working/data_gathering/recovery_packets/<batch_id>/
~~~

---

## Paso 2 — El agente procesa los packets

El agente Codex recibe los packets del batch y produce un shard markdown por batch (o por subconjunto, según la capacidad del run). Ver `CONTRACT.md` para la estructura de output del shard, incluyendo el template extendido con Parts 1B/2B.

**Importante para el primer run con la nueva arquitectura modular:** el agente debe tener acceso a `agents/codex/_shared/protocols/` además de `agents/codex/phase0-recovery/CONTRACT.md`. El CONTRACT referencia los protocolos compartidos — sin ellos, el CONTRACT es incompleto.

---

## Paso 3 — Depositar el shard de recovery

### Directorio de destino

~~~
input/data_gathering/shards/gpt_custom/
~~~

`parse_dg_shard.py` determina `source_tool` desde el nombre del directorio padre. Los shards en `gpt_custom/` reciben `source_tool = "gpt_custom"`.

### Convención de nombre de archivo

~~~
compass_artifact_recovery_<batch_id>_text_markdown.md
~~~

**Ejemplo:**

~~~
compass_artifact_recovery_batch_20260412_143000_text_markdown.md
~~~

**Rationale:**
- `compass_artifact_` — prefijo consistente con todos los shards existentes en `deep_search/`; `parse_dg_shard.py` no impone restricción de nombre pero el prefijo mantiene consistencia visual en los listados de directorio.
- `recovery_` — distingue los shards de recovery de los shards de investigación (que usan UUID o nombres como `domestika_d3_output`); permite grep fácil para auditoría.
- `_text_markdown` — convención de sufijo presente en todos los shards normalizados; `parse_dg_shard.py` deriva `shard_id` del stem del archivo (`Path(file).stem`), que se convierte en la clave para todos los archivos de output downstream. El sufijo preserva alineación con los demás shard IDs del pipeline.

---

## Paso 4 — Ejecutar parse_dg_shard.py

~~~bash
python phases/00-data-gathering/scripts/parse_dg_shard.py \
  input/data_gathering/shards/gpt_custom/compass_artifact_recovery_batch_YYYYMMDD_HHMMSS_text_markdown.md
~~~

**Output del parser:**

~~~
working/data_gathering/findings/<shard_id>__<finding_id>.json     ← Part 1 + Part 1B + Part 2 + Part 2B
working/data_gathering/diagnostics/part_4/<shard_id>__<item_id>.json  ← Part 4 (absence findings con unrecoverable)
working/data_gathering/diagnostics/qa_notes/<shard_id>_qa.json
~~~

Donde `shard_id = "compass_artifact_recovery_batch_YYYYMMDD_HHMMSS_text_markdown"`.

El parser trata Part 1B y Part 2B como findings válidos (mismo routing que Part 1 y Part 2) — el marcador de adjacency vive en el Finding ID (`F-ANN` / `F-APNN`), no en un campo separado, y downstream puede distinguirlos por el prefijo del ID. Part 4 en shards del recovery post-P101 contiene exclusivamente absence findings con `verification_status: unrecoverable`. Los findings rechazados por edge case 2/3/5 viven en `qa_notes`, no en `part_4/`.

---

## Flujo completo de re-entrada al pipeline

~~~
1. Script genera packets
   working/data_gathering/recovery_packets/<batch_id>/packet_NNN.json

2. Agente Codex procesa packets → produce shard markdown
   (con CONTRACT.md modular + _shared/protocols/)

3. Humano deposita shard
   input/data_gathering/shards/gpt_custom/compass_artifact_recovery_<batch_id>_text_markdown.md

4. parse_dg_shard.py procesa el shard
   ├── direct_verified    → working/data_gathering/findings/  (Part 1 + Part 1B)
   ├── indirect_verified  → working/data_gathering/findings/  (Part 2 + Part 2B)
   ├── unrecoverable      → working/data_gathering/diagnostics/part_4/  (absence findings)
   └── Research QA Notes  → working/data_gathering/diagnostics/qa_notes/
                             (incluye findings rechazados por edge case 2/3/5)

5. Phase 1 (converter_prepare.py) recoge los findings de working/data_gathering/findings/
   junto con todos los demás findings — sin routing especial para recovery.
~~~

---

## Items excluidos del batch

**11 items** del shard `compass_artifact_wf-91f3e7a0-e214-48ce-917e-bc6552ab2ae7_text_markdown_normalized` están excluidos de los recovery packets.

**Razón:** `failure_mode = no_url_inferred`. El normalizer no preservó la URL por bloque cuando el shard original organizaba findings por categorías agregadas. La estrategia de recovery por URL no aplica, y la re-búsqueda no tiene contexto suficiente sin la URL de la fuente. Este bug se resuelve en una iteración separada del skill `p0-normalize-shard`.

La exclusión se aplica comparando el campo `shard_id` en el JSON (no el nombre de archivo), que es la fuente de verdad.

---

## Notas downstream sobre `verification_status`

Los shards producidos por este agente usan tres valores activos de `verification_status` (los mismos que definen los protocolos compartidos y `pipeline_vocabulary.yaml`):

| Valor en shard | Significado | Status |
|---|---|---|
| `direct_verified` | Acceso directo a la fuente original | Activo |
| `indirect_verified` | Recuperado vía cache/archive/mirror/re-búsqueda | Activo (reemplaza a `blocked_url_index_verified`) |
| `unrecoverable` | Búsqueda activa que no rindió evidencia (absence finding) | Activo (reemplaza a `could_not_verify` para el recovery) |
| `could_not_verify` | — | **Deprecated** — no producido por el recovery agent; solo aparece en shards pre-recovery de `deep_search` |
| `blocked_url_index_verified` | — | **Deprecated** — reemplazado por `indirect_verified` |

`parse_dg_shard.py` pasa `verification_status` como string sin validación — los valores activos y los deprecated pasan igual. La fuente canónica de valores vive en `pipeline_vocabulary.yaml` en la raíz del repo.

**Pre-flight antes del primer run con la nueva arquitectura:** verificar que el template de Phase 1 en `phases/01-source-intake/reference/source_packet_conversion_template.md` mapea `indirect_verified` (equivalente semántico de `blocked_url_index_verified`). Si no existe entrada explícita para `indirect_verified`, agregarla antes de procesar los findings de recovery con el converter de Phase 1.

---

## Auditoría del output

Ver guardrails anti-drift en `_shared/protocols/core_protocol.md`. Los tres patrones prohibidos (pattern naming inventado en Part 4, thesis statements en Part 4, categorizaciones cross-finding fuera de Part 3) aplican a los shards del recovery igual que al resto de los agentes Phase 0. Si al auditar un shard detectas cualquiera de los tres, el shard no está listo para entrar al pipeline — devuélvelo al agente o al operador para reproceso.

Pregunta primaria de auditoría (heredada del handoff de sesión 16): **"¿esto trajo información que podemos usar?"**, no "¿esto cumple el contrato?". El contrato es infraestructura que soporta la recuperación. Confundir las dos es failure mode #7 del Blueprint_DSC.
