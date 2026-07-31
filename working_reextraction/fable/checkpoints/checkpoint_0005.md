# Checkpoint 0005 — tras batch_040

## Conteo
- Procesados: 1000 / 1178
- Escritos: 994
- Rechazados: 6 (todos required_field_unfillable: 1 en batch_002; 5 en batch_038 —
  skeletons cuyo snippet_primary contiene solo una nota de recuperación
  "n/a — content recovered via research subagent..." sin contenido de fuente)
- Batches completados: batch_001 – batch_040

## Distribución out_of_enum (records con al menos un valor fuera de enum: 162)
Por campo:
- metric_type: 139 records
- product_type_if_explicit: 24 records

Valores más frecuentes: payout delay (13), minimum payout (8), curso (8, product),
creator_count (7), tax_withholding_rate (7), catalog size (7), affiliate commission
rate (6), payout schedule (6), discount rate (5), traffic source share (5),
audience demographics (4), customer_count (4), product count by category (4),
subscription credits granted (3), integration count (3), más valores únicos
(GMV, GMS share, retention increase, funding raised, keyword ranking, search
volume change, average CTR, dispute response window, etc.).

Valores product fuera de enum nuevos en este tramo: curso (x8), course, digital
course, eCourses, stickers, necklace, engagement ring, Shopify theme,
WordPress theme, payhip template, resume template.

## schema_enum_conflict
- 32 records (todos snippet_needs_reopen, valor phase_1_only del vocabulario;
  criterio A).

## Issues acumulados
- contract_case_uncovered: actor_level — 392 records.
- contract_case_uncovered: product_type — 3 records.

## Patrones nuevos de ambigüedad (añadidos a criteria.md como K13–K14, marca [batch_040])
1. Skeletons sin contenido de fuente (snippet_primary = nota "n/a — content
   recovered via research subagent..."): subject_exact es irrellenable sin
   inferencia → rechazo con required_field_unfillable citando la nota. El
   contenido nunca se reconstruye desde el título o la URL.
2. Fees de pasarelas de pago de terceros relatadas por la plataforma
   (help-center "Connect your X account"): claim pricing_statement con
   metric_type fee_rate, la pasarela se excluye de platforms (convención de
   métodos de pago K3), y el descargo "collected by X and do not go to Payhip"
   se copia como qualifier. Las listas de países soportados van como
   payment_method_availability con geography verbatim.

Ninguna regla aplicada retroactivamente; K13–K14 describen la práctica usada en
batches 038–040 donde surgió y rigen desde batch_041.
