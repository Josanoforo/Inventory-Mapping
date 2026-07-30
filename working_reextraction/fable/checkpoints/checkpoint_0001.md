# Checkpoint 0001 — tras batch_008

## Conteo acumulado
- Skeletons procesados: 200 / 1178
- Records escritos: 199
- Rechazados: 1 (`ER-SP-compass_artifact_wf-0ffe7308-...-012-SNP-002`, required_field_unfillable: fila de tabla sin headers)
- Records con out_of_enum: 27
- Records con schema_enum_conflict: 1 (uso de `metric_type_unclear`, vocab phase-1, ausente del enum del schema)

## Distribución de out_of_enum por campo
- metric_type: 27 (único campo con out-of-enum hasta ahora)
  - Conteos de entidades (creators, profiles, Paid Members, empleados, instructors no pagados, signatures, total complaints): 12
  - Retenciones fiscales (tax withholding, royalty withholding tax): 7
  - Compensación de instructores (royalties, royalty percentages, commission): 4
  - Otros (global ranking, Bounce Rate, plazo máximo de activación, tiempo estándar de envío, % of all profiles): 4

## Patrones de ambigüedad NUEVOS detectados (agregados a criteria.md)
Ver criteria.md, sección "Patrones nuevos", entradas marcadas batch_001–batch_008.
Los más frecuentes: métrica ausente vs no-determinable; voz de plataforma fuera de
source_type de plataforma (foros, notificaciones citadas); menciones con rol
no-plataforma (categorías, temas, marcas de tarjeta); artefactos de skeleton en
source_date_if_available.
