# Poblado real — Signal Card

Corpus auditado: 29 registros en disco.

Enum del schema = *.schema.json. Enum del vocabulario = pipeline_vocabulary.yaml, resuelto al scope de fase aplicable (phase_1 para Extraction Record, phase_2 para Signal Card en `uncertainties`; `pointer_type` excluye/incluye `source_record_ref` segun el tipo de registro, per nota del vocabulario). Divergencia = diferencia de conjuntos entre ambos enums, no resuelta.

| Campo | N | Poblado | Vacio | Fuera de enum (schema) | Fuera de enum (vocab) | Divergencia schema<->vocab |
|---|---|---|---|---|---|---|
| `signal_id` | 29 | 29 | 0 | N/A (sin enum) | N/A (sin enum) | N/A |
| `source_record_ids` | 29 | 29 | 0 | N/A (sin enum) | N/A (sin enum) | N/A |
| `source_ids` | 29 | 29 | 0 | N/A (sin enum) | N/A (sin enum) | N/A |
| `round` | 29 | 29 | 0 | N/A (sin enum) | N/A (sin enum) | N/A |
| `signal_text` | 29 | 29 | 0 | N/A (sin enum) | N/A (sin enum) | N/A |
| `subject_exact` | 29 | 29 | 0 | N/A (sin enum) | N/A (sin enum) | N/A |
| `actor_level` | 29 | 29 | 0 | 0 | 0 | (ninguna) |
| `platforms` | 29 | 29 | 0 | N/A (sin enum) | N/A (sin enum) | N/A |
| `product_type_if_explicit` | 29 | 29 | 0 | 0 | 0 | (ninguna) |
| `metric_type` | 29 | 29 | 0 | 0 | 0 | (ninguna) |
| `metric_value_raw` | 29 | 16 | 13 | N/A (sin enum) | N/A (sin enum) | N/A |
| `metric_unit` | 29 | 17 | 12 | N/A (sin enum) | N/A (sin enum) | N/A |
| `time_scope_raw` | 29 | 7 | 22 | N/A (sin enum) | N/A (sin enum) | N/A |
| `time_scope_normalized_if_safe` | 29 | 4 | 25 | N/A (sin enum) | N/A (sin enum) | N/A |
| `geography_if_explicit` | 29 | 5 | 24 | N/A (sin enum) | N/A (sin enum) | N/A |
| `evidence_role` | 29 | 29 | 0 | 0 | 0 | (ninguna) |
| `local_qualifiers` | 29 | 25 | 4 | N/A (sin enum) | N/A (sin enum) | N/A |
| `uncertainties` | 29 | 27 | 2 | 0 | 0 | (ninguna) |
| `normalization_notes` | 29 | 29 | 0 | N/A (sin enum) | N/A (sin enum) | N/A |
| `extraction_notes` | 29 | 0 | 29 | N/A (sin enum) | N/A (sin enum) | N/A |
| `traceability_pointers` | 29 | 29 | 0 | N/A (sin enum) | N/A (sin enum) | N/A |
| `traceability_pointers[].pointer_type [pointer instances (not records)]` | 58 | 58 | 0 | 0 | 0 | (ninguna) |

## Desglose de 'vacio' por campo

| Campo | missing_key | null | empty_string | empty_array | empty_object |
|---|---|---|---|---|---|
| `signal_id` | 0 | 0 | 0 | 0 | 0 |
| `source_record_ids` | 0 | 0 | 0 | 0 | 0 |
| `source_ids` | 0 | 0 | 0 | 0 | 0 |
| `round` | 0 | 0 | 0 | 0 | 0 |
| `signal_text` | 0 | 0 | 0 | 0 | 0 |
| `subject_exact` | 0 | 0 | 0 | 0 | 0 |
| `actor_level` | 0 | 0 | 0 | 0 | 0 |
| `platforms` | 0 | 0 | 0 | 0 | 0 |
| `product_type_if_explicit` | 0 | 0 | 0 | 0 | 0 |
| `metric_type` | 0 | 0 | 0 | 0 | 0 |
| `metric_value_raw` | 0 | 13 | 0 | 0 | 0 |
| `metric_unit` | 0 | 12 | 0 | 0 | 0 |
| `time_scope_raw` | 0 | 22 | 0 | 0 | 0 |
| `time_scope_normalized_if_safe` | 0 | 25 | 0 | 0 | 0 |
| `geography_if_explicit` | 0 | 24 | 0 | 0 | 0 |
| `evidence_role` | 0 | 0 | 0 | 0 | 0 |
| `local_qualifiers` | 0 | 0 | 0 | 4 | 0 |
| `uncertainties` | 0 | 0 | 0 | 2 | 0 |
| `normalization_notes` | 0 | 0 | 0 | 0 | 0 |
| `extraction_notes` | 0 | 0 | 0 | 29 | 0 |
| `traceability_pointers` | 0 | 0 | 0 | 0 | 0 |
| `traceability_pointers[].pointer_type` | 0 | 0 | 0 | 0 | 0 |
