# Checkpoint 0002 — tras batch_016 (400 skeletons procesados)

## Conteo
- Procesados: 400 / 1178
- Escritos: 399 · Rechazados: 1 (sin cambios desde checkpoint 0001)
- Batches completados: batch_001 – batch_016

## Distribución de out_of_enum por campo (acumulado)
- metric_type: 53 records. Valores más repetidos:
  tax_withholding_rate (7), creator_count (4), "minimum payout" (4),
  "affiliate commission rate" (3), "discount rate" (3), "Paid Members" (2),
  "subscription credits granted" (2); resto valores únicos (umbrales de payout,
  duraciones, cuotas, conteos — ver manifest).
- product_type_if_explicit: 4 records ("digital items", "digital journal",
  "digital guide", "guides").

## schema_enum_conflict
- snippet_needs_reopen: 10 records (snippets truncados o listas cortadas).

## Issues contract_case_uncovered
- actor_level: 144 · product_type_if_explicit: 3

## Patrones NUEVOS desde checkpoint 0001
Ver adiciones [batch_016] en criteria.md:
- K8: snippets truncados (elipsis, corte a media palabra, listas con "...")
  → snippet_needs_reopen; el contenido no capturado nunca se completa por inferencia.
- K9: buyer_review con voz de vendedor (quejas de payout en Trustpilot/BBB)
  → actor seller por "quién habla" (extiende K7); el source_type prefijado no se toca.
