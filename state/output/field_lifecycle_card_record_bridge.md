# Puente Signal Card -> Markdown -> card_record.schema.json

Reconciliacion inversa: para cada propiedad de `card_record.schema.json` (consumida por el Indexer, `phases/03-inventory-mapping/modules/03_indexer.md`), de donde viene.

Lista de campos a extraer declarada en `03_indexer.md:20`.
`entities`/`figures` como extraccion best-effort declarados en `03_indexer.md:22`.

| Campo (card_record) | Declarado en | Origen |
|---|---|---|
| `id` | phases/03-inventory-mapping/schemas/card_record.schema.json:6,8 | markdown card id line "**{signal_id}**" (signal_to_markdown.py:260) |
| `round` | phases/03-inventory-mapping/schemas/card_record.schema.json:6,12 | No aparece por card dentro del bloque delimitado por ---. Solo aparece en la cabecera del archivo ("# Signal Cards — Round {round_number}", signal_to_markdown.py:305) y en el nombre de archivo signal_cards_round_{N}.md. El indexer (03_indexer.md:20) lo declara como campo a extraer por card pero format_card() no lo emite por card -- la extraccion depende de contexto de archivo/lote, no de un literal dentro del bloque de card. |
| `observation` | phases/03-inventory-mapping/schemas/card_record.schema.json:6,13,60 | markdown label "Observation:" <- signal_text (directo) (signal_to_markdown.py:262) |
| `source` | phases/03-inventory-mapping/schemas/card_record.schema.json:6,14,45 | markdown label "Source:" <- derivado de traceability_pointers via extract_source_url() (signal_to_markdown.py:264) |
| `date` | phases/03-inventory-mapping/schemas/card_record.schema.json:15 | markdown label "Date:" <- derivado de time_scope_normalized_if_safe / time_scope_raw via extract_date() (signal_to_markdown.py:266) |
| `source_type` | phases/03-inventory-mapping/schemas/card_record.schema.json:6,16 | markdown label "Source type:" <- NO es un campo de Signal Card (ausente del schema, additionalProperties:false). Recuperado por relectura directa del Extraction Record original (working/data_extraction/records/<source_record_ids[0]>.json) via build_record_index()/lookup_source_type(). (signal_to_markdown.py:268) |
| `domain` | phases/03-inventory-mapping/schemas/card_record.schema.json:6,39 | markdown label "Domain:" <- derivado de actor_level via derive_domain() (signal_to_markdown.py:270) |
| `actor` | phases/03-inventory-mapping/schemas/card_record.schema.json:6,43 | markdown label "Actor:" <- actor_level (signal_to_markdown.py:272) |
| `evidence_base` | phases/03-inventory-mapping/schemas/card_record.schema.json:47 | markdown label "Evidence base:" <- evidence_role (signal_to_markdown.py:274) |
| `extraction_status` | phases/03-inventory-mapping/schemas/card_record.schema.json:6,48 | SIN-CONSUMIDOR-ENCONTRADO. Requerido en card_record.schema.json pero format_card() (signal_to_markdown.py:234-278) no emite ninguna linea equivalente ("Extraction status: ..." no existe en el archivo) y 03_indexer.md no documenta de donde mas se derivaria. |
| `entities` | phases/03-inventory-mapping/schemas/card_record.schema.json:52,55 | Sin campo de origen aguas arriba. Generado por el propio indexer, "best-effort extraction to aid scanning" (03_indexer.md:23). |
| `figures` | phases/03-inventory-mapping/schemas/card_record.schema.json:57,60 | Sin campo de origen aguas arriba. Generado por el propio indexer, "best-effort extraction to aid scanning" (03_indexer.md:23). |

## Campos de card_record.schema.json sin origen localizado (1)

- `extraction_status`: SIN-CONSUMIDOR-ENCONTRADO. Requerido en card_record.schema.json pero format_card() (signal_to_markdown.py:234-278) no emite ninguna linea equivalente ("Extraction status: ..." no existe en el archivo) y 03_indexer.md no documenta de donde mas se derivaria.
