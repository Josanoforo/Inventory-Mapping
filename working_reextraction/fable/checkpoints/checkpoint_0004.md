# Checkpoint 0004 — tras batch_032

## Conteo
- Procesados: 800 / 1178
- Escritos: 799
- Rechazados: 1 (required_field_unfillable, batch_002)
- Batches completados: batch_001 – batch_032

## Distribución out_of_enum (records con al menos un valor fuera de enum: 116)
Por campo:
- metric_type: 106 records
- product_type_if_explicit: 10 records

Valores más frecuentes (metric_type): minimum payout (8), payout delay (8), creator_count (7),
tax_withholding_rate (7), discount rate (5), payout schedule (5), traffic source share (5),
affiliate commission rate (4), audience demographics (4), catalog size (3), customer_count (3),
integration count (2), más valores únicos de tablas analíticas (revenue by category,
revenue share by price range, pricing model comparison, store count by category, etc.).

Valores product_type_if_explicit fuera de enum acumulados: classes, digital guide, digital items,
digital journal (x2), guides, resume template, payhip template, curso (x2).

## schema_enum_conflict
- 25 records (todos por uso de valores phase_1_only del vocabulario:
  snippet_needs_reopen; criterio A).

## Issues acumulados
- contract_case_uncovered: actor_level — 316 records (source_types no mapeados en assignment_rule:
  article, report, database_profile, buyer_review, blog de plataforma, product_listing con voz de
  plataforma).
- contract_case_uncovered: product_type — 3 records.

## Patrones nuevos de ambigüedad (añadidos a criteria.md como K10–K12, marca [batch_032])
1. Capturas de tablas/layout de sitios analíticos (insightraider, storeleads, gumtrends, 6sense):
   la tabla completa se preserva verbatim en metric_value_raw, las unidades mixtas se declaran en
   metric_unit, y el metric_type recibe un descriptor mínimo K5 (p. ej. "revenue by category").
2. Páginas con voz de plataforma prefijadas como product_listing/blog/article (features, pricing,
   partner program, navegación, blog corporativo): actor por "quién habla" (platform) + issue K7;
   los listados genuinos de vendedores mantienen third_party según assignment_rule.
3. Proveedores de datos/analítica (Semrush, SimilarWeb, 6sense, Storeleads, Gumtrends, Wappalyzer,
   ful.io) → actor "source" + methodology_unclear cuando la cifra es estimación sin metodología;
   proveedores de integraciones promocionando su propia integración (Zapier, Pipedream, Pabbly,
   Make, widgets) → actor "third_party" + author_conflict_of_interest_possible (K4).

Ninguna regla aplicada retroactivamente; K10–K12 rigen desde batch_033 (y describen la práctica
ya usada en batches 029–032 donde surgió).
