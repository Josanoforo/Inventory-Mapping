# Checkpoint 0600 — batches 001-024

Re-extracción independiente y paralela (ejercicio, no corrida oficial de pipeline).
Este checkpoint cierra la tercera llamada de la serie (batches 017-024), acumulando
sobre el estado dejado por las dos llamadas previas (batches 001-016).

## Conteo acumulado total (batches 1-24)

- Skeletons procesados: 600
- Records escritos a `records/`: 600
- Records rechazados a `rejected_archive/`: 0
- status del manifest: `in_progress` (se mantiene; batch_048 es quien lo cierra)

## Distribución de out_of_enum por campo (acumulada, batches 1-24)

- `metric_type`: 5 ocurrencias (sin cambios respecto al checkpoint anterior)
  - `paid_creator_count`: 2
  - `content_category_distribution`: 2
  - `complaint_count`: 1

Todas las 5 ocurrencias provienen de batches 001-008 (primera llamada). El rango de
esta llamada (batch_017 a batch_024) no produjo ningún valor out_of_enum nuevo, pese a
contener bloques con métricas potencialmente atípicas (p.ej. estimaciones de conteo de
vendedores "thousands, maybe tens of thousands", conteos de cuentas de terceros, cifras
de indemnización legal en dólares) — todos se resolvieron con `metric_type: unknown` +
`metric_value_raw` string descriptivo, o con `metric_type` array cuando el bloque
combinaba 2-3 métricas explícitas sin dominancia, sin necesitar un valor fuera de enum.

## Distribución de schema_enum_conflict (acumulada, batches 1-24)

- 1 ocurrencia (sin cambios), campo `uncertainties`, valor de vocabulario deseado
  `metric_type_unclear`, registrado en batch_010. El rango de esta llamada (017-024) no
  produjo ninguna ocurrencia nueva.

## Patrones de ambigüedad en batches 017-024

No se encontraron patrones genuinamente nuevos que requieran una regla adicional en
`criteria.md`. Los patrones observados en este rango ya estaban cubiertos por reglas
existentes (incluyendo las agregadas tras batch_008 y batch_016):

- Múltiples reviews de Hotmart/Payhip en Trustpilot con truncamiento por elipsis final:
  resueltas con la regla de batch_016 (preservar, marcar `context_insufficient`, nota en
  `parser_notes`, sin rechazar salvo que el sujeto mismo sea indeterminable).
- Varias reviews de terceros (source_type `buyer_review`) donde quien habla es
  explícitamente un vendedor/creador ("Como productor...", "I am a seller...",
  referencias a "mi cuenta de productor"): resueltas con la regla de batch_016
  (actor_level según quién habla, no según la etiqueta mecánica de source_type).
  Aplicada de forma extensa en el bloque Hotmart (batch_018) y Payhip (batch_023-024).
  Se registró explícitamente en `parser_notes` cada vez que se aplicó.
- Nombre de documento de identidad local ("CURP") o nombre de país explícito en el
  título de la fuente ("Hotmart Brasil") usado como señal geográfica explícita distinta
  de un simple nombre de moneda: consistente con la regla de batch_016 sobre monedas
  (el gentilicio/nombre de país explícito sí cuenta; el nombre de moneda solo, no).
- Bloques de política de plataforma con 2-3 cifras de fee combinadas en un solo párrafo
  (Etsy legal/fees, Patreon creator-fees-overview): resueltos con `metric_type` en array
  y `metric_value_raw` combinado en un string, conforme a la regla de batch_008.
- Contenido puramente promocional de terceros construido sobre una plataforma estudiada
  (herramientas de IA para Gumroad, datasets, dashboards de analítics): se etiquetó
  `actor_level: third_party` (voz en primera persona vendiendo su propio producto/
  servicio) siguiendo `pipeline_vocabulary.yaml` (`assignment_rule` de `actor`), no
  `seller` del marketplace estudiado.

No se agregó ninguna regla nueva a `criteria.md` en este rango.

## Notas adicionales de ejecución

- Se procesaron 200 skeletons nuevos (batch_017 a batch_024), en orden numérico de
  batch y alfabético de filename dentro de cada batch, sin reprocesar ninguno de los 400
  ya registrados por las llamadas anteriores.
- 0 records rechazados en este rango (subject_exact fue llenable en los 200 casos).
- No se leyó, abrió ni hizo grep sobre `working/data_extraction/records/` (el corpus ya
  poblado por el otro proceso) en ningún momento de esta llamada.
- Todos los 200 records nuevos fueron validados programáticamente contra
  `data_extraction_record.schema.json` (jsonschema) antes de este checkpoint; 0 errores
  de validación en el rango nuevo.
