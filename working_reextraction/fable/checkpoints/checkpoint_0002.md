# Checkpoint 0002 — tras batch_016

## Conteo acumulado
- Skeletons procesados: 400 / 1178
- Records escritos: 399
- Rechazados: 1 (sin cambios desde checkpoint 0001)
- Records con out_of_enum: 55
- Records con schema_enum_conflict: 4 (metric_type_unclear ×2, snippet_needs_reopen ×2)

## Distribución de out_of_enum por campo
- metric_type: 53 — familias dominantes: conteos de entidades (creators/sellers/
  members/complaints/followers/empleados), retenciones fiscales (tax withholding,
  royalty withholding tax, VAT), compensación de creadores (royalties, commission,
  discount, savings, credits), umbrales de payout (minimum withdrawal/payout,
  payout requirement, mínimo de venta), y plazos (plazo de depósito, plazo máximo,
  tiempo de envío).
- product_type_if_explicit: 2 ("digital journal", "digital guide" — batch_009).

## Patrones nuevos desde checkpoint 0001 (agregados a criteria.md)
- [batch_009] product_type out-of-enum cuando la fuente nombra el tipo
  explícitamente pero no mapea al enum sin ambigüedad.
- [batch_009] Normalización de fecha desde source_date_if_available cuando el
  packet registra fecha efectiva explícita.
- [batch_010] snippet_needs_reopen (vocab-only) para listas de layout elididas
  por el packet.
- [batch_016] Umbral mencionado sin etiqueta métrica verbatim en la fuente →
  metric unknown + parser_note (no se construyen etiquetas out-of-enum no
  observadas).
