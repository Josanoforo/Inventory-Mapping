# Checkpoint 0001 — tras batch_008 (200 skeletons procesados)

## Conteo
- Procesados: 200 / 1178
- Escritos en records/: 199
- Rechazados (rejected_archive/): 1
  - `ER-SP-compass_artifact_wf-0ffe7308-...-012-SNP-002` — required_field_unfillable
    (fila de tabla sin encabezados; contenido del claim indeterminable sin inferencia)
- Batches completados: batch_001 – batch_008

## Distribución de out_of_enum por campo
- metric_type: 28 records
  - tax_withholding_rate: 7
  - creator_count: 3
  - "Paid Members": 2
  - profile_category_share / profile_count_by_category / "Number of Paid Creators" /
    "plazo máximo de activación" / "web traffic change" / "global ranking" /
    "top country desktop traffic" / "Bounce Rate" / "royalty percentages" /
    "petition signatures" / "affiliate commission rate" / "royalty rate" /
    "unpaid instructor count" / "employee count" / "complaint count" /
    "tiempo estándar de envío": 1 cada uno
- product_type_if_explicit: 1 record ("digital items")

## schema_enum_conflict
- snippet_needs_reopen (vocab phase-1, no en schema): 4 records

## Issues contract_case_uncovered
- actor_level: 109 records — la assignment_rule del vocabulario no mapea los
  source_type report / news / unknown / buyer_review / interview / database_profile,
  ni los casos blog-de-plataforma, blog-de-competidor, seller_forum con autor=platform.
  Asignación por "quién habla" en cada caso, documentada por record.
- product_type_if_explicit: 2 records — ítem promocionado es un servicio, fuera del enum.

## Patrones de ambigüedad NUEVOS
Ver adiciones marcadas [batch_008] en criteria.md. Resumen:
1. Fechas de página: "accessed" no normaliza; fecha de contenido sí (para claims de estado).
2. Claims de estado vs eventos narrados: solo los primeros toman normalized de source_date.
3. source_date_unclear se aplica cuando la página está sin fechar o la fecha es aproximada (~).
4. Menciones no-plataforma (categoría, tema de curso, nombre de creador) no entran en platforms.
5. author_conflict_of_interest_possible para voz promocional en primera persona
   (vendor listings, blogs de plataforma/competidor, afiliados).
6. Etiqueta observada para metric_type out-of-enum: verbatim si la fuente da etiqueta;
   descriptor mínimo + cita en parser_notes si no.
