# Seccion 5 — Patrones de descomposicion

## 1. Patron de division en batches

**SI existe.** El repo tiene un patron explicito de batching en las fases tempranas del pipeline.

**Como funciona:**
- `split-cards` divide los 10 archivos de rounds en batches de ~25 cards cada uno, nombrados `batch_R{round}_{batch_num}.md`.
- `index-cards` luego procesa esos batches uno a uno, extrayendo campos y appendeando a `card_index.jsonl`.

**Ejemplo concreto:** Un round con 200 cards produce ~8 batches (`batch_R05_001.md` a `batch_R05_008.md`). El indexer los procesa secuencialmente, actualizando `last_batch_processed` en el manifest despues de cada uno.

**Donde NO se aplica:** Los 7 scans, build-candidate, y validate-candidate trabajan sobre el indice completo o todos los TCs de una vez. No subdividen su trabajo en batches.

## 2. Patron de manifests como checkpoint

**SI existe.** Dos modulos lo usan:

**split_manifest.json** (modulo 02):
- Registra por round: `cards_found`, `batches_written`, `status` (pending/complete).
- Escrito despues de procesar cada round.
- Si el proceso se interrumpe: la retoma lee el manifest y busca el primer round con status `pending`.
- Valida contra `schemas/split_manifest.schema.json`.

**index_manifest.json** (modulo 03):
- Registra: `batches_processed`, `cards_indexed`, `last_batch_processed`, `issues`, `status` (complete/failed).
- Actualizado despues de procesar cada batch.
- Si el proceso se interrumpe: la retoma lee `last_batch_processed` y continua desde el siguiente batch.
- Valida contra `schemas/index_manifest.schema.json`.

**Patron comun:** ambos manifests son JSON, validan contra un schema, se actualizan granularmente (por round o por batch), y almacenan un campo de status que permite determinar si hay trabajo pendiente.

## 3. Patron de retoma cross-module

**SI existe**, pero solo en una transicion:

- `index-cards` lee `working/split/split_manifest.json` (output del modulo anterior) para obtener la lista de batches que debe procesar.
- Esto crea una dependencia de datos donde el output de un modulo informa al siguiente sobre que trabajo hay que hacer.

**Donde NO existe:** Los scans no leen ningun manifest — simplemente cargan `card_index.jsonl` completo. `build-candidate` lee los 7 JSONs de scan sin ningun mecanismo de tracking. `validate-candidate` lee todos los TCs del directorio output. No hay manifest que encadene los pasos del 04 en adelante.

## 4. Operaciones aritmeticas vs semanticas

**Aritmeticas (ejecutadas por scripts Python):**
- `scripts/parse_dg_shard.py`: parsing deterministico de markdown a JSON. Regex, splitting, field extraction. Sin juicio ni interpretacion.

**Semanticas (ejecutadas por agentes LLM via skills):**
- Los 7 scans (`scan-contradictions`, `scan-asymmetries`, etc.): requieren juicio para determinar si dos cards contradicen, si una distribucion es asimetrica, si una co-ocurrencia genera pregunta DT.
- `build-candidate`: requiere juicio para deduplicar patrones (>70% overlap + mismo mecanismo), verificar card-polo relevance, redactar definiciones y mechanical_summaries.
- `validate-candidate`: requiere juicio para spot-checks (card-polo relevance), verificar lenguaje mecanico, determinar si what_it_supports es template.

**Mixtas (tareas estructurales ejecutadas por agentes pero con logica mecanica):**
- `entry-gate`: los 5 checks son verificaciones mecanicas (presencia de campos, formato de IDs, ausencia de palabras estrategicas), pero los ejecuta un agente LLM, no un script Python.
- `split-cards`: dividir por delimitador `---` es mecanico, pero lo ejecuta un agente.
- `index-cards`: extraer campos de markdown es mecanico en su mayoria, pero la extraccion de `entities` y `figures` se declara como "best-effort", lo que implica juicio.

## 5. Tareas que hoy viven como operacion unica

Las siguientes tareas operan actualmente como una sola invocacion sin subdivision interna:

1. **build-candidate:** Recolecta los 7 scan artifacts, aplica pre-build filter, deduplica, construye todos los TCs, y escribe todos los outputs secundarios en una sola pasada. No tiene checkpoint intermedio. Si se cae construyendo el TC numero 15 de 30, hay que re-ejecutar todo.

2. **validate-candidate:** Valida todos los TCs en una sola pasada. Produce reportes por TC pero no tiene logica para saltar TCs ya validados. Si se cae validando el TC 20 de 30, hay que re-ejecutar todo.

3. **Cada scan individual** (los 7): Cada uno procesa el card_index.jsonl completo (~1,560 cards) en una pasada sin subdivision. Para corpus de este tamano probablemente no es problema, pero no hay mecanismo de checkpoint si el proceso es lento o se interrumpe.

4. **entry-gate:** Valida las 1,560 cards en una sola pasada. No tiene subdivision ni checkpoint, aunque para una operacion de validacion pura esto es esperable.
