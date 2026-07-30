# Checkpoint 0400 — batches 001-016

Re-extracción independiente y paralela (ejercicio, no corrida oficial de pipeline).
Este checkpoint cierra la segunda llamada de la serie (batches 009-016), acumulando
sobre el estado dejado por la primera llamada (batches 001-008).

## Conteo acumulado total (batches 1-16)

- Skeletons procesados: 400
- Records escritos a `records/`: 400
- Records rechazados a `rejected_archive/`: 0
- status del manifest: `in_progress` (se mantiene; batch_048 es quien lo cierra)

## Distribución de out_of_enum por campo (acumulada, batches 1-16)

- `metric_type`: 5 ocurrencias
  - `paid_creator_count`: 2
  - `content_category_distribution`: 2
  - `complaint_count`: 1

Todas las 5 ocurrencias provienen de batches 001-008 (llamada anterior). El rango de
esta llamada (batch_009 a batch_016) no produjo ningún valor out_of_enum nuevo.

## Distribución de schema_enum_conflict (acumulada, batches 1-16)

- 1 ocurrencia, campo `uncertainties`, valor de vocabulario deseado
  `metric_type_unclear` (phase_1_only en pipeline_vocabulary.yaml, ausente del
  enum cerrado del schema). Registrado en batch_010
  (`ER-SP-compass_artifact_wf-394dae4a-...-006-SNP-001`): el record usa
  `context_insufficient` (valor legal del schema) en su lugar, con nota en
  parser_notes explicando la intención original.

## Patrones de ambigüedad nuevos encontrados en batches 009-016

Sí se encontraron patrones no cubiertos por criteria.md (incluyendo lo agregado
tras batch_008). Los tres se agregaron a `criteria.md` con la marca
"--- Agregado tras batch_016: ... ---":

1. **source_type "buyer_review" no implica actor_level "buyer".** Varias reviews
   de Trustpilot/BBB sobre Gumroad (batch_016, principalmente) están escritas por
   vendedores/creadores quejándose de payouts retenidos, suspensiones de cuenta o
   fees — el propio texto se autoidentifica ("I am a seller on Gumroad...", "I
   sell items with full resale rights"). Se resolvió asignando actor_level
   "seller" según quién habla, no según la etiqueta mecánica de source_type,
   extendiendo el principio ya establecido para seller_forum en la adición de
   batch_008 a un source_type distinto.

2. **Snippets truncados con elipsis final ("...").** Recurrente en reviews de
   Trustpilot y en listados parcialmente capturados (países, monedas). Se
   resolvió preservando el fragmento tal cual, marcando context_insufficient, y
   dejando nota explícita en parser_notes de que el valor final no está
   disponible — sin rechazar el record salvo que el truncamiento afecte al
   sujeto mismo (subject_exact), no solo a un detalle secundario.

3. **Nombres de moneda como señal geográfica implícita pero no explícita**
   (mexican peso, Brazilian Real, Colombian Pesos, Argentine Pesos). Se resolvió
   dejando geography_if_explicit en null cuando la única señal es el nombre de
   una moneda, con nota explicando la inferencia descartada — salvo que el
   snippet nombre el país/gentilicio de forma independiente.

## Notas adicionales de ejecución

- Se procesaron 200 skeletons nuevos (batch_009 a batch_016), en orden alfabético
  de filename dentro de cada batch, sin reprocesar ninguno de los 200 ya
  registrados por la llamada anterior.
- 0 records rechazados en este rango (subject_exact fue llenable en los 200
  casos).
- No se leyó, abrió ni hizo grep sobre `working/data_extraction/records/` (el
  corpus ya poblado por el otro proceso) en ningún momento de esta llamada.
