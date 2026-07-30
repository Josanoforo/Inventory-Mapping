# Checkpoint — 1000 skeletons acumulados (batches 001–040)

## Conteo total acumulado
- Skeletons procesados: 1000
- Escritos a `records/`: 995
- Escritos a `rejected_archive/`: 5
- Status del manifest: `in_progress` (se mantiene hasta batch_048)

## Rango de este bloque (batches 033–040)
- Skeletons: 200
- Escritos a `records/`: 195
- Rechazados: 5 (ver detalle abajo)

## Distribución out_of_enum acumulada (campo `metric_type`, único campo con out_of_enum en todo el corpus 1–1000)
Total acumulado: 21 valores out_of_enum, todos en `metric_type` (ningún otro campo ha requerido out_of_enum hasta ahora).

Valores acumulados (batches 001–032, 5 previos):
- `paid_creator_count` (x2)
- `content_category_distribution` (x2)
- `complaint_count` (x1)

Valores nuevos de este bloque (batches 033–040, 16):
- `customer_retention_uplift` (x1)
- `audiojungle_category_item_count` (x2)
- `themeforest_category_item_count` (x2)
- `fee_calculation_component` (x1) — coincide con el ejemplo ilustrativo de la Sección 15 del contrato
- `gross_merchandise_value` (x1)
- `funding_round_amount` (x1)
- `fan_network_origin_share` (x1)
- `creator_platform_preference_poll` (x1)
- `third_party_tracked_listing_count` (x3)
- `etsy_keyword_search_ranking` (x1)
- `category_share_of_gms` (x1)
- `tool_user_count` (x1)
- `vat_calculation_example` (x1)

Todos siguen el patrón establecido tras batch_008: cifras de agregadores/bases de datos/terceros sin mapeo directo al enum cerrado se registran como string descriptivo literal, nunca forzadas al valor "menos malo".

## Distribución schema_enum_conflict acumulada
Total acumulado: 1 (sin cambios en este bloque — la única ocurrencia sigue siendo
el caso de batch_010: `uncertainties` con valor de vocabulario `metric_type_unclear`,
válido en `pipeline_vocabulary.yaml` como `phase_1_only` pero ausente del enum del
schema). Este bloque (033–040) no generó ningún schema_enum_conflict nuevo.

## Rechazados de este bloque (5, todos en batch_038, packet `de144e73` — Etsy tools)
Los 5 comparten la misma causa raíz: el `snippet_primary` del skeleton no contiene
texto real de la página, sino una nota de placeholder de recuperación fallida
("n/a — content recovered via research subagent's [...] fetch of <URL>; verbatim
character-for-character accuracy cannot be independently confirmed"). Sin
afirmación real capturada, `subject_exact` no es determinable.

1. `...de144e73..._text_markdown-008-SNP-001` — marmalead.com (database_profile)
2. `...de144e73..._text_markdown-011-SNP-001` — etsy.com/c/jewelry (search_results_page)
3. `...de144e73..._text_markdown-012-SNP-001` — etsy.com/categories (search_results_page)
4. `...de144e73..._text_markdown-015-SNP-001` — etsy.com/trends (search_results_page)
5. `...de144e73..._text_markdown-016-SNP-001` — similarweb.com/website/etsy.com (database_profile)

## Patrones nuevos detectados en batches 033–040

1. **Placeholder de recuperación fallida → rechazo.** Nueva regla agregada a
   `criteria.md`: cuando `snippet_primary` es enteramente una nota de "no se pudo
   confirmar verbatim" sin texto real de la página, el record se rechaza por
   `required_field_unfillable` (no por truncamiento — eso ya estaba cubierto desde
   batch_016 y no se rechaza por esa razón sola).

2. **CTR/variación porcentual fuera de rango 0-100%.** Dos snippets de un blog de
   terceros (erank) reportan CTR de 127% y variación de 892%, fuera del rango
   normal de una tasa de conversión. Se preservaron verbatim sin corrección.
   Se agregó regla explícita a `criteria.md` prohibiendo el uso de
   `metric_unit_unclear` (phase_2_only) para marcar esta anomalía; se usa
   `methodology_unclear` en su lugar.

3. **Confirmación de la regla de geografía por adjetivo de moneda (batch_016).**
   Un skeleton de Domestika (lista de monedas locales: "Mexican peso", "Argentine
   peso", "Colombian peso", etc.) fue el primer caso real de aplicación positiva de
   esa regla: los adjetivos de país modifican directamente el sustantivo de moneda,
   por lo que SÍ cuentan como geografía explícita (a diferencia del caso base de
   batch_016, donde el nombre de moneda solo, sin adjetivo de país, no cuenta). No
   se requiere nueva regla — el caso ya estaba previsto por la excepción existente.

4. Sin patrones adicionales que ameriten nueva regla más allá de los dos puntos 1–2
   arriba, ya incorporados a `criteria.md` con la marca
   `--- Agregado tras batch_040: ... ---`.

## Independencia del corpus
No se leyó, abrió ni se hizo grep sobre `working/data_extraction/records/` en
ningún momento de este bloque. Todas las lecturas se limitaron a
`working/data_extraction/skeleton_batches/batch_033` a `batch_040`, el contrato,
el schema, `pipeline_vocabulary.yaml`, y los artefactos propios en
`working_reextraction/sonnet/`.
