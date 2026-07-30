# Poblado real — Extraction Record

Corpus auditado: 1178 registros en disco.

Enum del schema = *.schema.json. Enum del vocabulario = pipeline_vocabulary.yaml, resuelto al scope de fase aplicable (phase_1 para Extraction Record, phase_2 para Signal Card en `uncertainties`; `pointer_type` excluye/incluye `source_record_ref` segun el tipo de registro, per nota del vocabulario). Divergencia = diferencia de conjuntos entre ambos enums, no resuelta.

| Campo | N | Poblado | Vacio | Fuera de enum (schema) | Fuera de enum (vocab) | Divergencia schema<->vocab |
|---|---|---|---|---|---|---|
| `extraction_id` | 1178 | 1178 | 0 | N/A (sin enum) | N/A (sin enum) | N/A |
| `source_packet_id` | 1178 | 1178 | 0 | N/A (sin enum) | N/A (sin enum) | N/A |
| `source_id` | 1178 | 1178 | 0 | N/A (sin enum) | N/A (sin enum) | N/A |
| `source_type` | 1178 | 1178 | 0 | 0 | 0 | (ninguna) |
| `source_title` | 1178 | 1178 | 0 | N/A (sin enum) | N/A (sin enum) | N/A |
| `source_ref` | 1178 | 1178 | 0 | N/A (sin enum) | N/A (sin enum) | N/A |
| `source_date_if_available` | 1178 | 1178 | 0 | N/A (sin enum) | N/A (sin enum) | N/A |
| `author_or_actor_if_available` | 1178 | 0 | 1178 | N/A (sin enum) | N/A (sin enum) | N/A |
| `snippet_primary` | 1178 | 1178 | 0 | N/A (sin enum) | N/A (sin enum) | N/A |
| `snippet_context_before` | 1178 | 0 | 1178 | N/A (sin enum) | N/A (sin enum) | N/A |
| `snippet_context_after` | 1178 | 0 | 1178 | N/A (sin enum) | N/A (sin enum) | N/A |
| `claim_type` | 1178 | 1178 | 0 | 0 | 90 | solo en schema: ['statistical_data'] |
| `subject_exact` | 1178 | 1178 | 0 | N/A (sin enum) | N/A (sin enum) | N/A |
| `actor_level` | 1178 | 1178 | 0 | 15 | 15 | (ninguna) |
| `platforms` | 1178 | 1175 | 3 | N/A (sin enum) | N/A (sin enum) | N/A |
| `product_type_if_explicit` | 1178 | 536 | 642 | 207 | 207 | (ninguna) |
| `metric_type` | 1178 | 1178 | 0 | 186 | 186 | (ninguna) |
| `metric_value_raw` | 1178 | 473 | 705 | N/A (sin enum) | N/A (sin enum) | N/A |
| `metric_unit` | 1178 | 473 | 705 | N/A (sin enum) | N/A (sin enum) | N/A |
| `time_scope_raw` | 1178 | 820 | 358 | N/A (sin enum) | N/A (sin enum) | N/A |
| `time_scope_normalized_if_safe` | 1178 | 402 | 776 | N/A (sin enum) | N/A (sin enum) | N/A |
| `geography_if_explicit` | 1178 | 314 | 864 | N/A (sin enum) | N/A (sin enum) | N/A |
| `evidence_role` | 1178 | 1178 | 0 | 0 | 0 | (ninguna) |
| `local_qualifiers` | 1178 | 1171 | 7 | N/A (sin enum) | N/A (sin enum) | N/A |
| `uncertainties` | 1178 | 821 | 357 | 0 | 155 | solo en schema: ['anecdotal_single_source', 'author_conflict_of_interest_possible', 'methodology_unclear', 'metric_unit_unclear', 'platform_scope_unclear']; solo en vocab: ['metric_type_unclear', 'snippet_needs_reopen', 'source_type_unclear'] |
| `parser_notes` | 1178 | 1178 | 0 | N/A (sin enum) | N/A (sin enum) | N/A |
| `traceability_pointer` | 1178 | 1178 | 0 | N/A (sin enum) | N/A (sin enum) | N/A |
| `traceability_pointer.pointer_type [pointer instances (not records)]` | 1178 | 1178 | 0 | 0 | 0 | (ninguna) |

## Desglose de 'vacio' por campo

| Campo | missing_key | null | empty_string | empty_array | empty_object |
|---|---|---|---|---|---|
| `extraction_id` | 0 | 0 | 0 | 0 | 0 |
| `source_packet_id` | 0 | 0 | 0 | 0 | 0 |
| `source_id` | 0 | 0 | 0 | 0 | 0 |
| `source_type` | 0 | 0 | 0 | 0 | 0 |
| `source_title` | 0 | 0 | 0 | 0 | 0 |
| `source_ref` | 0 | 0 | 0 | 0 | 0 |
| `source_date_if_available` | 0 | 0 | 0 | 0 | 0 |
| `author_or_actor_if_available` | 0 | 1178 | 0 | 0 | 0 |
| `snippet_primary` | 0 | 0 | 0 | 0 | 0 |
| `snippet_context_before` | 0 | 1178 | 0 | 0 | 0 |
| `snippet_context_after` | 0 | 1178 | 0 | 0 | 0 |
| `claim_type` | 0 | 0 | 0 | 0 | 0 |
| `subject_exact` | 0 | 0 | 0 | 0 | 0 |
| `actor_level` | 0 | 0 | 0 | 0 | 0 |
| `platforms` | 0 | 0 | 0 | 3 | 0 |
| `product_type_if_explicit` | 0 | 642 | 0 | 0 | 0 |
| `metric_type` | 0 | 0 | 0 | 0 | 0 |
| `metric_value_raw` | 0 | 705 | 0 | 0 | 0 |
| `metric_unit` | 0 | 705 | 0 | 0 | 0 |
| `time_scope_raw` | 0 | 358 | 0 | 0 | 0 |
| `time_scope_normalized_if_safe` | 0 | 776 | 0 | 0 | 0 |
| `geography_if_explicit` | 0 | 864 | 0 | 0 | 0 |
| `evidence_role` | 0 | 0 | 0 | 0 | 0 |
| `local_qualifiers` | 0 | 0 | 0 | 7 | 0 |
| `uncertainties` | 0 | 0 | 0 | 357 | 0 |
| `parser_notes` | 0 | 0 | 0 | 0 | 0 |
| `traceability_pointer` | 0 | 0 | 0 | 0 | 0 |
| `traceability_pointer.pointer_type` | 0 | 0 | 0 | 0 | 0 |
