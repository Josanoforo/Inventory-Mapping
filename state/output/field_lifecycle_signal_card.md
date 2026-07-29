# Ciclo de vida — Signal Card (21 campos)

Consumidor unico documentado: `phases/02-signal-extraction/scripts/signal_to_markdown.py` (unico puente JSON -> Markdown hacia IM, per CLAUDE.md / modules/01_entry_gate.md).

| Campo | Producido en | Ocurrencias en signal_to_markdown.py | Llegada al markdown |
|---|---|---|---|
| `signal_id` | phases/02-signal-extraction/schemas/signal_card.schema.json:9,32 | phases/02-signal-extraction/scripts/signal_to_markdown.py:90,168,173,249,260,298 (+3 more) | card id line "**{signal_id}**" (signal_to_markdown.py:260) |
| `source_record_ids` | phases/02-signal-extraction/schemas/signal_card.schema.json:10,37 | phases/02-signal-extraction/scripts/signal_to_markdown.py:34,221,222,223 | no aparece como valor literal en el markdown. Usado como clave de lookup para resolver el label "Source type:" via lookup_source_type() (def en signal_to_markdown.py:208, usa source_record_ids en signal_to_markdown.py:222-225). |
| `source_ids` | phases/02-signal-extraction/schemas/signal_card.schema.json:11,47 | (sin ocurrencia) | SIN-CONSUMIDOR-ENCONTRADO |
| `round` | phases/02-signal-extraction/schemas/signal_card.schema.json:12,57,60 | phases/02-signal-extraction/scripts/signal_to_markdown.py:5,13,90,170,239,282 (+5 more) | SIN-CONSUMIDOR-ENCONTRADO |
| `signal_text` | phases/02-signal-extraction/schemas/signal_card.schema.json:13,62 | phases/02-signal-extraction/scripts/signal_to_markdown.py:15,250,262 | markdown label "Observation:" (signal_to_markdown.py:262) |
| `subject_exact` | phases/02-signal-extraction/schemas/signal_card.schema.json:14,67 | (sin ocurrencia) | SIN-CONSUMIDOR-ENCONTRADO |
| `actor_level` | phases/02-signal-extraction/schemas/signal_card.schema.json:15,72 | phases/02-signal-extraction/scripts/signal_to_markdown.py:23,37,79,124,126,128 (+10 more) | markdown label "Actor:" (signal_to_markdown.py:272) |
| `platforms` | phases/02-signal-extraction/schemas/signal_card.schema.json:16,109,115 | (sin ocurrencia) | SIN-CONSUMIDOR-ENCONTRADO |
| `product_type_if_explicit` | phases/02-signal-extraction/schemas/signal_card.schema.json:17,117 | (sin ocurrencia) | SIN-CONSUMIDOR-ENCONTRADO |
| `metric_type` | phases/02-signal-extraction/schemas/signal_card.schema.json:18,160 | (sin ocurrencia) | SIN-CONSUMIDOR-ENCONTRADO |
| `metric_value_raw` | phases/02-signal-extraction/schemas/signal_card.schema.json:19,221 | (sin ocurrencia) | SIN-CONSUMIDOR-ENCONTRADO |
| `metric_unit` | phases/02-signal-extraction/schemas/signal_card.schema.json:20,225 | (sin ocurrencia) | SIN-CONSUMIDOR-ENCONTRADO |
| `time_scope_raw` | phases/02-signal-extraction/schemas/signal_card.schema.json:21,229 | phases/02-signal-extraction/scripts/signal_to_markdown.py:19,47,155,161 | alimenta el label "Date:" via extract_date() (def en signal_to_markdown.py:152), usado solo si time_scope_normalized_if_safe es null (signal_to_markdown.py:157-163). |
| `time_scope_normalized_if_safe` | phases/02-signal-extraction/schemas/signal_card.schema.json:22,233 | phases/02-signal-extraction/scripts/signal_to_markdown.py:19,47,155,157 | alimenta el label "Date:" via extract_date() (def en signal_to_markdown.py:152), con prioridad sobre time_scope_raw (signal_to_markdown.py:157-159). |
| `geography_if_explicit` | phases/02-signal-extraction/schemas/signal_card.schema.json:23,237 | (sin ocurrencia) | SIN-CONSUMIDOR-ENCONTRADO |
| `evidence_role` | phases/02-signal-extraction/schemas/signal_card.schema.json:24,255 | phases/02-signal-extraction/scripts/signal_to_markdown.py:25,251,274 | markdown label "Evidence base:" (signal_to_markdown.py:274) |
| `local_qualifiers` | phases/02-signal-extraction/schemas/signal_card.schema.json:25,272 | (sin ocurrencia) | SIN-CONSUMIDOR-ENCONTRADO |
| `uncertainties` | phases/02-signal-extraction/schemas/signal_card.schema.json:26,280 | (sin ocurrencia) | SIN-CONSUMIDOR-ENCONTRADO |
| `traceability_pointers` | phases/02-signal-extraction/schemas/signal_card.schema.json:27,302 | phases/02-signal-extraction/scripts/signal_to_markdown.py:98,104,108,113,118,252 (+1 more) | alimenta el label "Source:" via extract_source_url() (def en signal_to_markdown.py:98, invocada en signal_to_markdown.py:255) -- no aparece como valor literal propio, se recorre para elegir un pointer_value. |
| `normalization_notes` | phases/02-signal-extraction/schemas/signal_card.schema.json:28,310 | (sin ocurrencia) | SIN-CONSUMIDOR-ENCONTRADO |
| `extraction_notes` | phases/02-signal-extraction/schemas/signal_card.schema.json:29,317 | (sin ocurrencia) | SIN-CONSUMIDOR-ENCONTRADO |

## Campos que mueren en el puente JSON -> Markdown (12 de 21)

- `source_ids` -> SIN-CONSUMIDOR-ENCONTRADO (ninguna ocurrencia del nombre en signal_to_markdown.py)
- `subject_exact` -> SIN-CONSUMIDOR-ENCONTRADO (ninguna ocurrencia del nombre en signal_to_markdown.py)
- `platforms` -> SIN-CONSUMIDOR-ENCONTRADO (ninguna ocurrencia del nombre en signal_to_markdown.py)
- `product_type_if_explicit` -> SIN-CONSUMIDOR-ENCONTRADO (ninguna ocurrencia del nombre en signal_to_markdown.py)
- `metric_type` -> SIN-CONSUMIDOR-ENCONTRADO (ninguna ocurrencia del nombre en signal_to_markdown.py)
- `metric_value_raw` -> SIN-CONSUMIDOR-ENCONTRADO (ninguna ocurrencia del nombre en signal_to_markdown.py)
- `metric_unit` -> SIN-CONSUMIDOR-ENCONTRADO (ninguna ocurrencia del nombre en signal_to_markdown.py)
- `geography_if_explicit` -> SIN-CONSUMIDOR-ENCONTRADO (ninguna ocurrencia del nombre en signal_to_markdown.py)
- `local_qualifiers` -> SIN-CONSUMIDOR-ENCONTRADO (ninguna ocurrencia del nombre en signal_to_markdown.py)
- `uncertainties` -> SIN-CONSUMIDOR-ENCONTRADO (ninguna ocurrencia del nombre en signal_to_markdown.py)
- `normalization_notes` -> SIN-CONSUMIDOR-ENCONTRADO (ninguna ocurrencia del nombre en signal_to_markdown.py)
- `extraction_notes` -> SIN-CONSUMIDOR-ENCONTRADO (ninguna ocurrencia del nombre en signal_to_markdown.py)
