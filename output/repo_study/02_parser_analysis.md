# Seccion 2 — Como funciona el parser

Archivo analizado: `scripts/parse_dg_shard.py` (496 lineas).

## 1. Proposito declarado

Del docstring (lineas 2-18):

> parse_dg_shard.py — Data Gathering shard parser.

Parsea archivos markdown de shards de Data Gathering y produce archivos JSON estructurados. Autoridad contractual declarada: `reference/data_gathering_project_instructions_v4_5.md` (Rule 4 + Rule 7) y `reference/research_directions_protocol.md` (Sections 3, 4, 5, 9).

## 2. Input esperado

- **Formato:** un archivo Markdown (`.md`), recibido como argumento de linea de comandos.
- **Path esperado:** `input/data_gathering/shards/<filename>.md`
- **Estructura del contenido:** jerarquica con secciones identificadas por regex:
  - Header: contiene "Research Shard:" y opcionalmente "Direction statement:"
  - Part 1: bloques de findings identificados por `### [A-Z][A-Z0-9]*-[CP]?\d+`
  - Part 2: misma estructura que Part 1
  - Part 4: items de failure analysis identificados por `### F-X\d+: <subject>`
  - Research QA Notes: subsecciones en 3 formatos posibles (### headers, **bold labels:**, o bullet lists)
- **Campos requeridos por finding (Rule 4):** what, verbatim_snippet, source, source_type, verification_status, date, signal_type, notes.
- **Variantes de labels:** el parser acepta multiples grafias por campo (case-insensitive, espacios/underscores intercambiables). Definidas en `REQUIRED_FIELD_MAP` (lineas 41-51).
- **source_tool:** se infiere del nombre del directorio padre del archivo (debe ser `deep_search` o `gpt_custom`).

## 3. Output producido

Tres tipos de output, todos escritos relativo a la raiz del repo:

| Output | Path | Formato | Estructura |
|---|---|---|---|
| Findings (Part 1 + Part 2) | `working/data_gathering/findings/<shard_id>__<finding_id>.json` | JSON, un archivo por finding | `{finding_id, shard_id, source_tool, part, what, verbatim_snippet, source, source_type, verification_status, date, signal_type, notes, extra_fields?}` |
| Part 4 diagnostics | `working/data_gathering/diagnostics/part_4/<shard_id>__<item_id>.json` | JSON, un archivo por item | `{shard_id, source_tool, item_id, seller_or_subject, attempted, why_failed, urls_mentioned}` |
| QA Notes | `working/data_gathering/diagnostics/qa_notes/<shard_id>_qa.json` | JSON, un archivo por shard | `{shard_id, source_tool, <secciones_qa_como_keys>}` |

## 4. Manejo de errores

| Situacion | Comportamiento | Lineas |
|---|---|---|
| Archivo no encontrado | Imprime ERROR a stderr, `sys.exit(1)` | 430-432 |
| Finding no parseable | `try/except` por finding, warn a stderr, **continua** con el siguiente | 186-190 |
| Campo requerido faltante | Warn a stderr por cada campo faltante, **produce el JSON igual** (sin ese campo) | 239-241 |
| source_tool invalido (directorio padre no es deep_search/gpt_custom) | Warn a stderr, usa `source_tool='unknown'`, **continua** | 443-447 |
| Part 4 sin Attempted/Why failed | Warn a stderr, almacena el bloque raw como `attempted`, **continua** | 289-294 |
| Seccion vacia o inexistente (Part 1, Part 2, Part 4, QA) | Silenciosamente se salta, no produce output para esa seccion | 454-456, 466, 476 |

Patron general: errores fatales solo cuando el archivo no existe. Todo lo demas es warn + continuar.

## 5. Idempotencia

**SI.** Declarado explicitamente en el docstring (linea 17): "Idempotent: re-running produces identical output."

Verificado en el codigo:
- `write_json()` usa `path.write_text()` que sobreescribe el archivo completo (linea 421).
- No hay generacion de timestamps, UUIDs, ni valores aleatorios.
- Todo el parsing es deterministico (regex sobre texto fijo).
- No mantiene estado entre ejecuciones.
- Correrlo dos veces sobre el mismo input produce exactamente los mismos archivos.

## 6. Retomabilidad

**NO.** No hay mecanismo de retoma:
- No existe archivo manifest que registre progreso.
- No hay logica "skip if exists" — siempre sobreescribe todos los archivos de output.
- No hay checkpoint ni estado persistente.
- Si se interrumpe a medio camino, los archivos ya escritos quedan en disco pero los pendientes se pierden.
- Para completar, hay que re-ejecutar desde el principio (lo cual es seguro porque es idempotente).

## 7. Dependencias externas

| Libreria | Tipo | Uso |
|---|---|---|
| `sys` | stdlib | stderr, argv, exit codes |
| `re` | stdlib | regex para parsing de secciones, labels, IDs, URLs |
| `json` | stdlib | serializacion JSON |
| `os` | stdlib | importado pero **no usado** en el codigo |
| `pathlib.Path` | stdlib | operaciones de filesystem |

**Cero dependencias externas.** Solo stdlib de Python.
No importa ni llama a ningun otro script del repo.
No lee archivos de configuracion.
