# Checkpoint 0005 — tras batch_040

## Conteo acumulado
- Skeletons procesados: 1000 / 1178
- Records escritos: 994
- Rechazados: 6 (1 previo + 5 nuevos en batch_038)
- Records con out_of_enum: 122
- Records con schema_enum_conflict: 4 (sin cambios desde checkpoint 0002)

## Rechazos nuevos (batch_038)
Cinco skeletons cuyo snippet_primary contiene únicamente una nota del packet
("n/a — content recovered via research subagent...") sin contenido de la fuente:
subject_exact no rellenable → required_field_unfillable. IDs:
de144e73-...-008-SNP-001, 011-SNP-001, 012-SNP-001, 015-SNP-001, 016-SNP-001.

## Distribución de out_of_enum por campo
- metric_type: 111 — nuevas etiquetas de los batches 033-040: customer retention,
  GMV, GMS, funding raised, comisión/commission, search volume, CTR, listings,
  sellers, music & sound effects, assets and templates, website templates and
  themes, AI generations, apps.
- product_type_if_explicit: 11 — nuevas: "Shopify Theme", "WordPress Theme"
  (familia plantillas/temas por herramienta destino).

## Patrones nuevos desde checkpoint 0004
Registrados en criteria.md con marcador de batch:
- Snippets cuyo contenido es solo una nota del packet sin texto fuente →
  rechazo required_field_unfillable (batch_038).
- Fees de procesadores de pago relayadas por el help center de una plataforma:
  claim pricing_statement, actor platform, evidencia direct_claim (fee de un
  tercero, no official_policy de la plataforma); nota de capas "no van a la
  plataforma" (batch_039).
- Placeholders de plantilla sin sustituir en el texto fuente ('[Gateway name]')
  → preservados verbatim + issue skeleton_artifact (batch_039).
- Autopromoción comparativa de plataforma ("Unlike other platforms", "leading
  the charge") → author_conflict_of_interest_possible también en blogs y
  pricing pages propios (batch_036-037).
- Listas largas de rails de pago soportados → payment_method_availability con
  rails nombrados incluidos en platforms de forma representativa y lista
  completa preservada en snippet (batch_040).
