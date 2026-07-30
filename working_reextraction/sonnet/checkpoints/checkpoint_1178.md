# Checkpoint — FINAL — 1178 skeletons acumulados (batches 001–048)

## Conteo total acumulado (run completo)
- Skeletons totales encontrados en `working/data_extraction/skeleton_batches/`: 1178
- Skeletons procesados: 1178
- Escritos a `records/`: 1173
- Escritos a `rejected_archive/`: 5
- Status del manifest: `complete` (`completed_at`: "batch_048 final")

## Rango de este bloque final (batches 041–048)
- Skeletons: 178 (batch_041–047: 25 c/u; batch_048: 3 — último batch existente, no hay batch_049)
- Escritos a `records/`: 178
- Rechazados: 0

## Distribución out_of_enum acumulada COMPLETA (campo `metric_type`, único campo con out_of_enum en todo el corpus 1–1178)
Total acumulado: 22 valores out_of_enum.

- `paid_creator_count` x2
- `content_category_distribution` x2
- `complaint_count` x1
- `customer_retention_uplift` x1
- `audiojungle_category_item_count` x2
- `themeforest_category_item_count` x2
- `fee_calculation_component` x1
- `gross_merchandise_value` x1
- `funding_round_amount` x1
- `fan_network_origin_share` x1
- `creator_platform_preference_poll` x1
- `third_party_tracked_listing_count` x3
- `etsy_keyword_search_ranking` x1
- `category_share_of_gms` x1
- `tool_user_count` x1
- `vat_calculation_example` x1
- `data_retention_duration` x1 — **nuevo en este bloque** (batch_041, Payhip privacy policy: 10-year transaction data retention period for EU VAT purposes; no metric_type enum value covers data-retention durations)

Todos siguen el patrón establecido tras batch_008: cifras/duraciones que no mapean a ningún valor del enum cerrado se registran como string descriptivo literal, nunca forzadas al valor "menos malo" del enum.

## Distribución schema_enum_conflict acumulada COMPLETA
Total acumulado: 2.

- `uncertainties` con valor de vocabulario `metric_type_unclear` (phase_1_only, ausente del enum del schema) — 2 ocurrencias:
  1. batch_010 (bloque anterior, ya documentado)
  2. batch_047 (este bloque): comparación Sellfy-vs-Gumroad publicada por Sellfy citando "9% transaction fee" para Gumroad, mientras el resto del corpus documenta consistentemente la tarifa oficial de Gumroad como 10% flat — discrepancia de tasa entre fuentes no resuelta aquí (Data Extraction no compara fuentes), marcada con `metric_type_unclear` a nivel de incertidumbre.

## Resumen de patrones agregados a criteria.md durante todo el run
1. **Tras batch_008**: métricas de agregadores/bases de datos sin mapeo directo → string descriptivo literal (out_of_enum); bloques de 2–3 métricas combinadas sin dominancia → `metric_type` array con `metric_value_raw` combinado; autoría no determinable en foros de vendedores → default `actor_level: seller` + `actor_level_unclear`.
2. **Tras batch_016**: `source_type: buyer_review` no determina por sí solo `actor_level: buyer` (se prioriza quién habla); snippets truncados con "..." se preservan (no se rechazan por esa razón sola), con `context_insufficient` + nota, salvo que el truncamiento deje el sujeto mismo indeterminable.
3. **Tras batch_040**: placeholders de recuperación fallida (sin texto real capturado) → rechazo por `subject_exact_unfillable`/`required_field_unfillable`; cifras de CTR/variación porcentual fuera de 0–100% → preservadas verbatim, `methodology_unclear` (nunca `metric_unit_unclear`, prohibido en Fase 1); nombres de moneda solos (sin adjetivo de país ni topónimo independiente) no cuentan como geografía explícita.
4. **Este bloque (batches 041–048)**: sin reglas nuevas obligatorias agregadas a `criteria.md` — los casos encontrados (retención de datos como out_of_enum, fragmentos de UI/navegación de catálogo sin claim explícito, reseñas de Trustpilot truncadas en bloque, testimonios alojados en páginas propias del vendedor) ya estaban cubiertos por patrones existentes. Nota operativa (no normativa) para futuras corridas: fragmentos de UI de catálogo (`product_listing`/`search_results_page`) sin ninguna afirmación real (solo etiquetas de navegación, contadores en cero, cajas de búsqueda vacías) se aceptaron con `subject_exact` describiendo el elemento de UI observado, `evidence_role: observed_platform_state`, y `context_insufficient` en `uncertainties`, en vez de rechazarlos — se consideró que la presencia mecánica del elemento en la página es en sí un hecho observable, no una inferencia. Testimonios/reseñas de vendedores alojados en la página promocional del propio proveedor (p.ej. página "Gumroad alternative" de Lemon Squeezy citando testimonios de vendedores) se marcaron con `author_conflict_of_interest_possible` además de `anecdotal_single_source`.

## Incidente operativo durante este bloque (reportado por transparencia)
Al limpiar un archivo de registro previo a una regeneración, se ejecutó por error un comando de borrado con comodín
(`rm -f .../ER-SP-compass_artifact_wf-e33b0dbb*`) que coincidió con el prefijo de un **source packet completo
(`e33b0dbb-828e-4221-b8c5-7bf05bddcdba`) ya procesado en batches 001–040**, borrando 53 records ya escritos y
committeados de ese packet (no pertenecientes al rango asignado 041–048). El incidente se detectó de inmediato
mediante verificación cruzada manifest-vs-disco (995 registros esperados en el rango 1–1000 vs 942 encontrados
tras el borrado accidental). Como el directorio `working_reextraction/sonnet/` está bajo control de versiones con
commits por bloque de 200, los 53 archivos se restauraron sin pérdida de datos mediante
`git checkout HEAD -- <paths>`. Verificación final: manifest vs disco coincide exactamente (1173 records + 5
rejected = 1178, sin duplicados ni faltantes). No se fabricó ni reconstruyó contenido — la recuperación fue
una restauración literal desde el commit existente.

## Independencia del corpus
No se leyó, abrió ni se hizo grep sobre `working/data_extraction/records/` (el corpus paralelo de otro proceso)
en ningún momento de este bloque ni de todo el run. Todas las lecturas de skeletons se limitaron a
`working/data_extraction/skeleton_batches/batch_041` a `batch_048`, el contrato, el schema,
`pipeline_vocabulary.yaml`, y los artefactos propios en `working_reextraction/sonnet/` (incluyendo, tras el
incidente anterior, una restauración vía git de archivos propios ya existentes — no una lectura del corpus ajeno).
