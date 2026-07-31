# Checkpoint 0006 (final) — tras batch_048

## Conteo final
- Procesados: 1178 / 1178 (batch_001 – batch_048, corrida completa)
- Escritos: 1172
- Rechazados: 6, todos con required_field_unfillable:
  - 1 en batch_002 (fila de tabla de fees de México sin encabezados de columna)
  - 5 en batch_038 (skeletons cuyo snippet_primary contiene solo una nota de
    recuperación "n/a — content recovered via research subagent..." sin
    contenido de fuente; K13)

## Distribución out_of_enum (191 records con al menos un valor fuera de enum)
Por campo:
- metric_type: 164 records
- product_type_if_explicit: 30 records

metric_type — valores más frecuentes: payout delay (16), minimum payout (9),
catalog size (9), payout schedule (8), creator_count (7), tax_withholding_rate
(7), affiliate commission rate (6), discount rate (6), traffic source share (5),
audience demographics (4), customer_count (4), product count by category (4),
VAT rate (3), subscription credits granted (3), integration count (3), más ~65
valores de baja frecuencia (GMV, GMS, GMS share, Market Share (Est.), funding
raised, keyword ranking, search volume change, average CTR, retention increase,
tax rates on purchases, download speed, student count, platform fees paid,
approval time, revenue increase, shipping rate, data retention period, dispute
response window, tablas analíticas K10, etc.).

product_type_if_explicit — valores: curso (10), digital journal (2), course (2),
y unitarios: digital items, digital guide, guides, classes, resume template,
payhip template, digital course, eCourses, Shopify theme, WordPress theme,
stickers, necklace, engagement ring, piano sheet + MIDI, albums, Especialización.

## schema_enum_conflict
- 38 records, todos por snippet_needs_reopen (valor phase_1_only del
  vocabulario; criterio A). Nunca se usaron metric_unit_unclear ni
  platform_scope_unclear.

## Issues acumulados
- contract_case_uncovered: actor_level — 468 records (source_types no mapeados
  en la assignment_rule: article, report, database_profile, buyer_review,
  unknown, interview; y autores atípicos: blogs de plataforma, páginas de
  comparación de competidores, testimonios en páginas de marketing, posts de
  creadores bajo platform_doc, emails de plataforma citados en foros).
- contract_case_uncovered: product_type — 3 records.

## Patrones nuevos de ambigüedad (añadidos a criteria.md como K15–K16, marca [batch_048])
1. Testimonios de vendedores curados en páginas de marketing de la plataforma
   (gumroad.com, lemonsqueezy.com/gumroad-alternative, hotmart.com/es/pagos):
   actor "seller" por quién habla + issue K7, evidence seller_self_claim, y
   uncertainties anecdotal_single_source + author_conflict_of_interest_possible
   (contexto promocional curado).
2. Páginas de comparación "X-alternative" alojadas por la plataforma
   competidora (polar.sh, sellfy.com, thrivecart, lemonsqueezy, podia, ko-fi):
   actor "platform" por quién habla (K11) + issue + K4; los vendedores
   terceros que comparan a otros sin ser sujeto de la comparación (whop,
   dodopayments, wise, noda) → "third_party" + K4.

Ninguna regla aplicada retroactivamente; K15–K16 describen la práctica usada en
los batches 041–048 donde surgió.

## Cierre
Manifest marcado como complete. PARADA DURA: no se ejecuta ninguna comparación
con otro corpus.
