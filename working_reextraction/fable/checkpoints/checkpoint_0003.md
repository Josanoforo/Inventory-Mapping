# Checkpoint 0003 — tras batch_024

## Conteo acumulado
- Skeletons procesados: 600 / 1178
- Records escritos: 599
- Rechazados: 1 (sin cambios)
- Records con out_of_enum: 69
- Records con schema_enum_conflict: 4 (sin cambios desde checkpoint 0002)

## Distribución de out_of_enum por campo
- metric_type: 65 — familias: conteos de entidades (creators/sellers/subscribers/
  products/assets/images/complaints/followers/generations), retenciones fiscales,
  compensación (royalties/commission/discount/savings/credits), umbrales de payout
  (minimum payout threshold, retiro mínimo, payout requirement), plazos (plazo de
  depósito, plazo máximo), y misceláneos (audience, legal coverage, potential
  customers, global ranking, Bounce Rate).
- product_type_if_explicit: 4 ("digital journal", "digital guide", "Framer
  templates" ×2).

## Patrones nuevos desde checkpoint 0002
- Sin reglas nuevas: los batches 017-024 se resolvieron con las reglas ya
  registradas en criteria.md (policy de plataforma, cuentas de sellers,
  herramientas third-party con COI, capturas duplicadas del packet marcadas
  como issue skeleton_artifact).
