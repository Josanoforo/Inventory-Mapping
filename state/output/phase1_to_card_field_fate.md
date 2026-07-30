# Destino de campos Phase 1 → Signal Card — batch_001, round 1

Medicion mecanica, solo lectura, fecha 2026-07-30. Corpus: 25 skeletons de
`working/signal_extraction/skeleton_batches/batch_001/` y 29 Signal Cards de `working/signal_extraction/cards/`.
El origen Phase 1 de cada par es el bloque `_extraction_context` del skeleton,
que replica los campos del Extraction Record (26 de los 27 campos del schema;
`traceability_pointer` no aparece bajo `_extraction_context` en ninguno de los 25 skeletons).

## Reglas mecanicas aplicadas

- Vacio = `null`, clave ausente, `""`, `[]` o `{}`. `"unknown"` y `"none"` son valores, no vacio.
- Orden de evaluacion por (card, campo): (1) `traceability_pointer` → NO-CLASIFICABLE
  (origen no presente en el skeleton); (2) origen vacio → ORIGEN-VACIO; (3) sin campo
  equivalente declarado en el schema de la card → SIN-DESTINO; (4) destino vacio → PERDIDO;
  (5) valor identico y dentro del enum de la card → LIMPIO; identico y fuera → SUCIO;
  (6) valor distinto y no vacio → NORMALIZADO.
- Identidad = igualdad JSON exacta. Para `extraction_id` → `source_record_ids` y
  `source_id` → `source_ids` (escalar → array declarado por el schema de la card),
  identico = el array de la card es exactamente `[valor_del_skeleton]`.
- `parser_notes` → `extraction_notes` se trata como destino nominal: la descripcion del
  schema de la card (signal_card.schema.json:322, "Carryover or local notes from extraction")
  y el modulo (phases/02-signal-extraction/modules/signal_converter.md:187) declaran el
  carryover. El modulo lo condiciona a "that remain useful for audit"; la categoria PERDIDO
  aqui registra el hecho mecanico (origen con valor, destino vacio), no un juicio sobre esa condicion.

## Bloque 0 — Inventario y mapeo

| Objeto | Ruta | Conteo |
|---|---|---|
| Skeletons batch_001 | `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-*.json` | 25 |
| Signal Cards | `working/signal_extraction/cards/SC-R1-*.json` | 29 |
| Schema Extraction Record | `phases/01-source-intake/data-extraction/schemas/data_extraction_record.schema.json` | 1 |
| Schema Signal Card | `phases/02-signal-extraction/schemas/signal_card.schema.json` | 1 |

El manifest (`working/signal_extraction/signal_converter_manifest.json`) declara
`skeletons_processed: 25` y `cards_written: 29`; coincide con los archivos en disco.

### Mapeo card → skeleton

Derivado de `source_record_ids` de cada card contra `_source_extraction_id` de cada
skeleton. Las 29 cards mapean a exactamente un skeleton cada una. El mapeo coincide
con `processed_skeletons[].cards_produced` del manifest (verificacion, no fuente): coincide.

| Card | Skeleton de origen | extraction_id compartido |
|---|---|---|
| SC-R1-001 | SC-R1-001 | `ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-001-SNP-001` |
| SC-R1-002 | SC-R1-002 | `ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-002-SNP-001` |
| SC-R1-003 | SC-R1-003 | `ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-002-SNP-002` |
| SC-R1-004 | SC-R1-004 | `ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-003-SNP-001` |
| SC-R1-005 | SC-R1-005 | `ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-004-SNP-001` |
| SC-R1-006 | SC-R1-006 | `ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-005-SNP-001` |
| SC-R1-007 | SC-R1-007 | `ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-006-SNP-001` |
| SC-R1-008 | SC-R1-008 | `ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-006-SNP-002` |
| SC-R1-009 | SC-R1-009 | `ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-007-SNP-001` |
| SC-R1-010 | SC-R1-010 | `ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-007-SNP-002` |
| SC-R1-011 | SC-R1-011 | `ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-007-SNP-003` |
| SC-R1-012 | SC-R1-012 | `ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-008-SNP-001` |
| SC-R1-013 | SC-R1-013 | `ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-008-SNP-002` |
| SC-R1-014 | SC-R1-014 | `ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-009-SNP-001` |
| SC-R1-015 | SC-R1-015 | `ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-010-SNP-001` |
| SC-R1-016 | SC-R1-016 | `ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-011-SNP-001` |
| SC-R1-017 | SC-R1-017 | `ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-012-SNP-001` |
| SC-R1-018 | SC-R1-018 | `ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-013-SNP-001` |
| SC-R1-019 | SC-R1-019 | `ER-SP-compass_artifact_wf-0ffe7308-62e3-4530-ae68-93720df60f34_text_markdown-001-SNP-001` |
| SC-R1-020 | SC-R1-020 | `ER-SP-compass_artifact_wf-0ffe7308-62e3-4530-ae68-93720df60f34_text_markdown-002-SNP-001` |
| SC-R1-021 | SC-R1-021 | `ER-SP-compass_artifact_wf-0ffe7308-62e3-4530-ae68-93720df60f34_text_markdown-003-SNP-001` |
| SC-R1-022 | SC-R1-022 | `ER-SP-compass_artifact_wf-0ffe7308-62e3-4530-ae68-93720df60f34_text_markdown-004-SNP-001` |
| SC-R1-023 | SC-R1-023 | `ER-SP-compass_artifact_wf-0ffe7308-62e3-4530-ae68-93720df60f34_text_markdown-005-SNP-001` |
| SC-R1-024 | SC-R1-024 | `ER-SP-compass_artifact_wf-0ffe7308-62e3-4530-ae68-93720df60f34_text_markdown-006-SNP-001` |
| SC-R1-025 | SC-R1-025 | `ER-SP-compass_artifact_wf-0ffe7308-62e3-4530-ae68-93720df60f34_text_markdown-007-SNP-001` |
| SC-R1-1179 | SC-R1-002 | `ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-002-SNP-001` |
| SC-R1-1180 | SC-R1-003 | `ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-002-SNP-002` |
| SC-R1-1181 | SC-R1-014 | `ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-009-SNP-001` |
| SC-R1-1182 | SC-R1-014 | `ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-009-SNP-001` |

### Cards por skeleton

| Skeleton | Cards producidas | IDs |
|---|---|---|
| SC-R1-001 | 1 | SC-R1-001 |
| SC-R1-002 | 2 | SC-R1-002, SC-R1-1179 |
| SC-R1-003 | 2 | SC-R1-003, SC-R1-1180 |
| SC-R1-004 | 1 | SC-R1-004 |
| SC-R1-005 | 1 | SC-R1-005 |
| SC-R1-006 | 1 | SC-R1-006 |
| SC-R1-007 | 1 | SC-R1-007 |
| SC-R1-008 | 1 | SC-R1-008 |
| SC-R1-009 | 1 | SC-R1-009 |
| SC-R1-010 | 1 | SC-R1-010 |
| SC-R1-011 | 1 | SC-R1-011 |
| SC-R1-012 | 1 | SC-R1-012 |
| SC-R1-013 | 1 | SC-R1-013 |
| SC-R1-014 | 3 | SC-R1-014, SC-R1-1181, SC-R1-1182 |
| SC-R1-015 | 1 | SC-R1-015 |
| SC-R1-016 | 1 | SC-R1-016 |
| SC-R1-017 | 1 | SC-R1-017 |
| SC-R1-018 | 1 | SC-R1-018 |
| SC-R1-019 | 1 | SC-R1-019 |
| SC-R1-020 | 1 | SC-R1-020 |
| SC-R1-021 | 1 | SC-R1-021 |
| SC-R1-022 | 1 | SC-R1-022 |
| SC-R1-023 | 1 | SC-R1-023 |
| SC-R1-024 | 1 | SC-R1-024 |
| SC-R1-025 | 1 | SC-R1-025 |

Los skeletons SC-R1-002 y SC-R1-003 se separan en 2 cards cada uno; SC-R1-014 se separa
en 3 cards. Los 22 restantes producen 1 card cada uno. 25 skeletons → 29 cards.

## Bloque 1 — Lista de campos, derivada de los schemas

### Campos del Extraction Record (data_extraction_record.schema.json)

| Campo ER | Linea schema ER | Enum ER | Destino nominal en card | Linea schema card |
|---|---|---|---|---|
| `extraction_id` | data_extraction_record.schema.json:38 | sin enum | `source_record_ids` | signal_card.schema.json:37 |
| `source_packet_id` | data_extraction_record.schema.json:43 | sin enum | (ninguno) | — |
| `source_id` | data_extraction_record.schema.json:48 | sin enum | `source_ids` | signal_card.schema.json:47 |
| `source_type` | data_extraction_record.schema.json:53 | 18 valores (L54-74) | (ninguno) | — |
| `source_title` | data_extraction_record.schema.json:76 | sin enum | (ninguno) | — |
| `source_ref` | data_extraction_record.schema.json:80 | sin enum | (ninguno) | — |
| `source_date_if_available` | data_extraction_record.schema.json:85 | sin enum | (ninguno) | — |
| `author_or_actor_if_available` | data_extraction_record.schema.json:89 | sin enum | (ninguno) | — |
| `snippet_primary` | data_extraction_record.schema.json:93 | sin enum | (ninguno) | — |
| `snippet_context_before` | data_extraction_record.schema.json:98 | sin enum | (ninguno) | — |
| `snippet_context_after` | data_extraction_record.schema.json:102 | sin enum | (ninguno) | — |
| `claim_type` | data_extraction_record.schema.json:106 | 11 valores (L108-120) | (ninguno) | — |
| `subject_exact` | data_extraction_record.schema.json:122 | sin enum | `subject_exact` | signal_card.schema.json:67 |
| `actor_level` | data_extraction_record.schema.json:127 | 9 valores (L131-141) | `actor_level` | signal_card.schema.json:72 |
| `platforms` | data_extraction_record.schema.json:165 | sin enum | `platforms` | signal_card.schema.json:109 |
| `product_type_if_explicit` | data_extraction_record.schema.json:173 | 12 valores (L177-190) | `product_type_if_explicit` | signal_card.schema.json:117 |
| `metric_type` | data_extraction_record.schema.json:216 | 21 valores (L220-242) | `metric_type` | signal_card.schema.json:160 |
| `metric_value_raw` | data_extraction_record.schema.json:277 | sin enum | `metric_value_raw` | signal_card.schema.json:221 |
| `metric_unit` | data_extraction_record.schema.json:281 | sin enum | `metric_unit` | signal_card.schema.json:225 |
| `time_scope_raw` | data_extraction_record.schema.json:285 | sin enum | `time_scope_raw` | signal_card.schema.json:229 |
| `time_scope_normalized_if_safe` | data_extraction_record.schema.json:289 | sin enum | `time_scope_normalized_if_safe` | signal_card.schema.json:233 |
| `geography_if_explicit` | data_extraction_record.schema.json:293 | sin enum | `geography_if_explicit` | signal_card.schema.json:237 |
| `evidence_role` | data_extraction_record.schema.json:311 | 12 valores (L313-326) | `evidence_role` | signal_card.schema.json:255 |
| `local_qualifiers` | data_extraction_record.schema.json:328 | sin enum | `local_qualifiers` | signal_card.schema.json:272 |
| `uncertainties` | data_extraction_record.schema.json:336 | 16 valores (L340-357) | `uncertainties` | signal_card.schema.json:280 |
| `parser_notes` | data_extraction_record.schema.json:361 | sin enum | `extraction_notes` | signal_card.schema.json:317 |
| `traceability_pointer` | data_extraction_record.schema.json:368 | pointer_type: 7 valores (L378-387) | `traceability_pointers` | signal_card.schema.json:302 |

### Campos de la Signal Card (signal_card.schema.json)

| Campo card | Linea schema | Enum |
|---|---|---|
| `signal_id` | signal_card.schema.json:32 | sin enum (pattern L34) |
| `source_record_ids` | signal_card.schema.json:37 | sin enum |
| `source_ids` | signal_card.schema.json:47 | sin enum |
| `round` | signal_card.schema.json:57 | sin enum |
| `signal_text` | signal_card.schema.json:62 | sin enum |
| `subject_exact` | signal_card.schema.json:67 | sin enum |
| `actor_level` | signal_card.schema.json:72 | 9 valores (L76-86) |
| `platforms` | signal_card.schema.json:109 | sin enum |
| `product_type_if_explicit` | signal_card.schema.json:117 | 12 valores (L121-133) |
| `metric_type` | signal_card.schema.json:160 | 21 valores (L164-185) |
| `metric_value_raw` | signal_card.schema.json:221 | sin enum |
| `metric_unit` | signal_card.schema.json:225 | sin enum |
| `time_scope_raw` | signal_card.schema.json:229 | sin enum |
| `time_scope_normalized_if_safe` | signal_card.schema.json:233 | sin enum |
| `geography_if_explicit` | signal_card.schema.json:237 | sin enum |
| `evidence_role` | signal_card.schema.json:255 | 12 valores (L257-269) |
| `local_qualifiers` | signal_card.schema.json:272 | sin enum |
| `uncertainties` | signal_card.schema.json:280 | 13 valores (L284-297) |
| `traceability_pointers` | signal_card.schema.json:302 | pointer_type: 8 valores (L336-345) |
| `normalization_notes` | signal_card.schema.json:310 | sin enum |
| `extraction_notes` | signal_card.schema.json:317 | sin enum |

### Diferencias de enums entre los dos schemas (campos homonimos)

- `uncertainties`: el enum del ER (16 valores) contiene 3 valores que el enum de la card
  (13 valores) no declara: `methodology_unclear`, `anecdotal_single_source`,
  `author_conflict_of_interest_possible` (data_extraction_record.schema.json:353-355 vs
  signal_card.schema.json:284-297). Un valor de ese subconjunto copiado identico a la card saldria SUCIO.
- `traceability_pointers[].pointer_type` de la card declara `source_record_ref`
  (signal_card.schema.json:344), ausente en el enum del ER (data_extraction_record.schema.json:378-387).
- `actor_level`, `product_type_if_explicit`, `metric_type`, `evidence_role`: enums identicos en ambos schemas.

### Verificacion de campos nombrados

Los 10 campos requeridos aparecen en la lista: `author_or_actor_if_available` (ER:89),
`snippet_context_before` (ER:98), `snippet_context_after` (ER:102),
`product_type_if_explicit` (ER:173), `metric_type` (ER:216), `actor_level` (ER:127),
`uncertainties` (ER:336), `geography_if_explicit` (ER:293),
`source_date_if_available` (ER:85), `time_scope_raw` (ER:285). Ninguno falta.

Campos de la card sin origen en Phase 1 (fuera de la clasificacion, que opera sobre
campos del ER): `signal_id`, `round`, `signal_text`, `normalization_notes`.
`signal_text` se redacta en Phase 2; `snippet_primary` del ER no tiene campo equivalente
declarado en la card (la descripcion de `signal_text`, signal_card.schema.json:65, declara
redaccion observacional, no carryover). `source_ref` del ER no tiene campo homonimo en la
card; su valor aparece de facto dentro de `traceability_pointers` como pointer `url`.

## Bloque 2/3 — Tabla resumen (n=29 pares card→skeleton)

| Campo ER | ORIGEN-VACIO | SIN-DESTINO | LIMPIO | SUCIO | NORMALIZADO | PERDIDO | NO-CLASIFICABLE |
|---|---|---|---|---|---|---|---|
| `extraction_id` | 0 | 0 | 29 | 0 | 0 | 0 | 0 |
| `source_packet_id` | 0 | 29 | 0 | 0 | 0 | 0 | 0 |
| `source_id` | 0 | 0 | 29 | 0 | 0 | 0 | 0 |
| `source_type` | 0 | 29 | 0 | 0 | 0 | 0 | 0 |
| `source_title` | 0 | 29 | 0 | 0 | 0 | 0 | 0 |
| `source_ref` | 0 | 29 | 0 | 0 | 0 | 0 | 0 |
| `source_date_if_available` | 0 | 29 | 0 | 0 | 0 | 0 | 0 |
| `author_or_actor_if_available` | 29 | 0 | 0 | 0 | 0 | 0 | 0 |
| `snippet_primary` | 0 | 29 | 0 | 0 | 0 | 0 | 0 |
| `snippet_context_before` | 29 | 0 | 0 | 0 | 0 | 0 | 0 |
| `snippet_context_after` | 29 | 0 | 0 | 0 | 0 | 0 | 0 |
| `claim_type` | 0 | 29 | 0 | 0 | 0 | 0 | 0 |
| `subject_exact` | 0 | 0 | 17 | 0 | 12 | 0 | 0 |
| `actor_level` | 0 | 0 | 1 | 0 | 28 | 0 | 0 |
| `platforms` | 0 | 0 | 29 | 0 | 0 | 0 | 0 |
| `product_type_if_explicit` | 0 | 0 | 29 | 0 | 0 | 0 | 0 |
| `metric_type` | 0 | 0 | 28 | 0 | 1 | 0 | 0 |
| `metric_value_raw` | 16 | 0 | 8 | 0 | 5 | 0 | 0 |
| `metric_unit` | 12 | 0 | 11 | 0 | 6 | 0 | 0 |
| `time_scope_raw` | 11 | 0 | 4 | 0 | 3 | 11 | 0 |
| `time_scope_normalized_if_safe` | 13 | 0 | 4 | 0 | 0 | 12 | 0 |
| `geography_if_explicit` | 24 | 0 | 5 | 0 | 0 | 0 | 0 |
| `evidence_role` | 0 | 0 | 28 | 0 | 1 | 0 | 0 |
| `local_qualifiers` | 3 | 0 | 15 | 0 | 10 | 1 | 0 |
| `uncertainties` | 4 | 0 | 15 | 0 | 10 | 0 | 0 |
| `parser_notes` | 0 | 0 | 0 | 0 | 0 | 29 | 0 |
| `traceability_pointer` | 0 | 0 | 0 | 0 | 0 | 0 | 29 |

SUCIO: 0 casos en todo el corpus. Ningun NORMALIZADO cae fuera del enum de la card.

## Detalle por card — SUCIO, NORMALIZADO y NO-CLASIFICABLE

Para NO-CLASIFICABLE (`traceability_pointer`, 29/29) la razon es identica en todos los
pares y se enuncia una vez: el skeleton no conserva el objeto `traceability_pointer` del
Extraction Record bajo `_extraction_context` (verificado en los 25 skeletons); el skeleton
trae un array top-level `traceability_pointers` construido en la preparacion
(`phases/02-signal-extraction/scripts/signal_prepare.py`). El valor de origen Phase 1 no
aparece en el skeleton y la clasificacion se define sobre el valor del skeleton. Se lista
el lado card con su ruta:linea; el lado skeleton no tiene literal que reportar.

### SC-R1-001 (skeleton SC-R1-001)

- `actor_level` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-001.json:54`: "source"
  - card `working/signal_extraction/cards/SC-R1-001.json:12`: "third_party"
- `uncertainties` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-001.json:67`: ["source_date_unclear"]
  - card `working/signal_extraction/cards/SC-R1-001.json:25`: ["source_date_unclear", "context_insufficient"]
- `traceability_pointer` — **NO-CLASIFICABLE**
  - skeleton: `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-001.json (clave `traceability_pointer` ausente bajo `_extraction_context`)`
  - card `working/signal_extraction/cards/SC-R1-001.json:29`: [{"pointer_type": "url", "pointer_value": "https://apify.com/easyapi/patreon-analytic", "secondary_pointer": null}, {"pointer_type": "source_record_ref", "pointer_value": "ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-001-SNP-001", "secondary_pointer": "SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-001"}]

### SC-R1-002 (skeleton SC-R1-002)

- `actor_level` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-002.json:54`: "seller"
  - card `working/signal_extraction/cards/SC-R1-002.json:12`: "source"
- `local_qualifiers` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-002.json:66`: ["as of February 2026", "Based on Graphtreon data", "That's a drop of around 5% since June 2025"]
  - card `working/signal_extraction/cards/SC-R1-002.json:24`: ["as of February 2026", "Based on Graphtreon data"]
- `traceability_pointer` — **NO-CLASIFICABLE**
  - skeleton: `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-002.json (clave `traceability_pointer` ausente bajo `_extraction_context`)`
  - card `working/signal_extraction/cards/SC-R1-002.json:29`: [{"pointer_type": "url", "pointer_value": "https://backlinko.com/patreon-users", "secondary_pointer": null}, {"pointer_type": "source_record_ref", "pointer_value": "ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-002-SNP-001", "secondary_pointer": "SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-002"}]

### SC-R1-003 (skeleton SC-R1-003)

- `actor_level` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-003.json:54`: "seller"
  - card `working/signal_extraction/cards/SC-R1-003.json:12`: "source"
- `time_scope_raw` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-003.json:62`: "Currently (article last updated Feb. 25, 2026)"
  - card `working/signal_extraction/cards/SC-R1-003.json:20`: "Currently"
- `traceability_pointer` — **NO-CLASIFICABLE**
  - skeleton: `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-003.json (clave `traceability_pointer` ausente bajo `_extraction_context`)`
  - card `working/signal_extraction/cards/SC-R1-003.json:31`: [{"pointer_type": "url", "pointer_value": "https://backlinko.com/patreon-users", "secondary_pointer": null}, {"pointer_type": "source_record_ref", "pointer_value": "ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-002-SNP-002", "secondary_pointer": "SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-002"}]

### SC-R1-004 (skeleton SC-R1-004)

- `actor_level` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-004.json:54`: "buyer"
  - card `working/signal_extraction/cards/SC-R1-004.json:12`: "third_party"
- `uncertainties` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-004.json:70`: ["source_date_unclear"]
  - card `working/signal_extraction/cards/SC-R1-004.json:28`: ["source_date_unclear", "context_insufficient"]
- `traceability_pointer` — **NO-CLASIFICABLE**
  - skeleton: `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-004.json (clave `traceability_pointer` ausente bajo `_extraction_context`)`
  - card `working/signal_extraction/cards/SC-R1-004.json:32`: [{"pointer_type": "url", "pointer_value": "https://chromewebstore.google.com/detail/patreon-assistant/plfnafajhhphflcaonfmgllfoofciild", "secondary_pointer": null}, {"pointer_type": "source_record_ref", "pointer_value": "ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-003-SNP-001", "secondary_pointer": "SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-003"}]

### SC-R1-005 (skeleton SC-R1-005)

- `actor_level` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-005.json:54`: "source"
  - card `working/signal_extraction/cards/SC-R1-005.json:12`: "third_party"
- `metric_value_raw` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-005.json:60`: "18.99"
  - card `working/signal_extraction/cards/SC-R1-005.json:18`: 18.99
- `traceability_pointer` — **NO-CLASIFICABLE**
  - skeleton: `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-005.json (clave `traceability_pointer` ausente bajo `_extraction_context`)`
  - card `working/signal_extraction/cards/SC-R1-005.json:33`: [{"pointer_type": "url", "pointer_value": "https://chromewebstore.google.com/detail/patreon-scraper/cofdkjlleejhgmhacajalbhedbdncgki", "secondary_pointer": null}, {"pointer_type": "source_record_ref", "pointer_value": "ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-004-SNP-001", "secondary_pointer": "SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-004"}]

### SC-R1-006 (skeleton SC-R1-006)

- `actor_level` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-006.json:54`: "seller"
  - card `working/signal_extraction/cards/SC-R1-006.json:12`: "third_party"
- `uncertainties` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-006.json:70`: ["source_date_unclear"]
  - card `working/signal_extraction/cards/SC-R1-006.json:28`: ["source_date_unclear", "context_insufficient"]
- `traceability_pointer` — **NO-CLASIFICABLE**
  - skeleton: `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-006.json (clave `traceability_pointer` ausente bajo `_extraction_context`)`
  - card `working/signal_extraction/cards/SC-R1-006.json:32`: [{"pointer_type": "url", "pointer_value": "https://creatormetrics.io/", "secondary_pointer": null}, {"pointer_type": "source_record_ref", "pointer_value": "ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-005-SNP-001", "secondary_pointer": "SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-005"}]

### SC-R1-007 (skeleton SC-R1-007)

- `actor_level` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-007.json:54`: "seller"
  - card `working/signal_extraction/cards/SC-R1-007.json:12`: "source"
- `metric_value_raw` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-007.json:60`: "25.88% of all profiles (54,582 creators)"
  - card `working/signal_extraction/cards/SC-R1-007.json:18`: "25.88%"
- `metric_unit` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-007.json:61`: "percent of all Patreon profiles; count in creators"
  - card `working/signal_extraction/cards/SC-R1-007.json:19`: "percent of all Patreon profiles"
- `local_qualifiers` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-007.json:66`: ["as of January 2025", "most popular genre"]
  - card `working/signal_extraction/cards/SC-R1-007.json:24`: ["as of January 2025", "most popular genre", "54,582 creators (absolute count equivalent of the 25.88% figure)"]
- `traceability_pointer` — **NO-CLASIFICABLE**
  - skeleton: `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-007.json (clave `traceability_pointer` ausente bajo `_extraction_context`)`
  - card `working/signal_extraction/cards/SC-R1-007.json:30`: [{"pointer_type": "url", "pointer_value": "https://earthweb.com/patreon-statistics", "secondary_pointer": null}, {"pointer_type": "source_record_ref", "pointer_value": "ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-006-SNP-001", "secondary_pointer": "SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-006"}]

### SC-R1-008 (skeleton SC-R1-008)

- `subject_exact` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-008.json:53`: "Patreon creator profile counts by category (music, gaming, writing, adult categories) as of January 2025"
  - card `working/signal_extraction/cards/SC-R1-008.json:11`: "Patreon creator profile counts by category (music, gaming, writing, adult categories)"
- `actor_level` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-008.json:54`: "seller"
  - card `working/signal_extraction/cards/SC-R1-008.json:12`: "source"
- `traceability_pointer` — **NO-CLASIFICABLE**
  - skeleton: `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-008.json (clave `traceability_pointer` ausente bajo `_extraction_context`)`
  - card `working/signal_extraction/cards/SC-R1-008.json:30`: [{"pointer_type": "url", "pointer_value": "https://earthweb.com/patreon-statistics", "secondary_pointer": null}, {"pointer_type": "source_record_ref", "pointer_value": "ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-006-SNP-002", "secondary_pointer": "SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-006"}]

### SC-R1-009 (skeleton SC-R1-009)

- `actor_level` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-009.json:54`: "seller"
  - card `working/signal_extraction/cards/SC-R1-009.json:12`: "source"
- `traceability_pointer` — **NO-CLASIFICABLE**
  - skeleton: `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-009.json (clave `traceability_pointer` ausente bajo `_extraction_context`)`
  - card `working/signal_extraction/cards/SC-R1-009.json:30`: [{"pointer_type": "url", "pointer_value": "https://graphtreon.com/patreon-stats", "secondary_pointer": null}, {"pointer_type": "source_record_ref", "pointer_value": "ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-007-SNP-001", "secondary_pointer": "SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-007"}]

### SC-R1-010 (skeleton SC-R1-010)

- `subject_exact` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-010.json:53`: "Graphtreon estimated total monthly payouts across all Patreon creators as accessed April 14, 2026"
  - card `working/signal_extraction/cards/SC-R1-010.json:11`: "Graphtreon estimated total monthly payouts across all Patreon creators"
- `actor_level` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-010.json:54`: "seller"
  - card `working/signal_extraction/cards/SC-R1-010.json:12`: "source"
- `traceability_pointer` — **NO-CLASIFICABLE**
  - skeleton: `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-010.json (clave `traceability_pointer` ausente bajo `_extraction_context`)`
  - card `working/signal_extraction/cards/SC-R1-010.json:32`: [{"pointer_type": "url", "pointer_value": "https://graphtreon.com/patreon-stats", "secondary_pointer": null}, {"pointer_type": "source_record_ref", "pointer_value": "ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-007-SNP-002", "secondary_pointer": "SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-007"}]

### SC-R1-011 (skeleton SC-R1-011)

- `subject_exact` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-011.json:53`: "Graphtreon creator category taxonomy as shown in navigation as accessed April 14, 2026"
  - card `working/signal_extraction/cards/SC-R1-011.json:11`: "Graphtreon creator category taxonomy as shown in navigation"
- `actor_level` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-011.json:54`: "marketplace"
  - card `working/signal_extraction/cards/SC-R1-011.json:12`: "third_party"
- `uncertainties` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-011.json:67`: ["source_date_unclear"]
  - card `working/signal_extraction/cards/SC-R1-011.json:25`: ["source_date_unclear", "actor_level_unclear", "context_insufficient"]
- `traceability_pointer` — **NO-CLASIFICABLE**
  - skeleton: `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-011.json (clave `traceability_pointer` ausente bajo `_extraction_context`)`
  - card `working/signal_extraction/cards/SC-R1-011.json:30`: [{"pointer_type": "url", "pointer_value": "https://graphtreon.com/patreon-stats", "secondary_pointer": null}, {"pointer_type": "source_record_ref", "pointer_value": "ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-007-SNP-003", "secondary_pointer": "SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-007"}]

### SC-R1-012 (skeleton SC-R1-012)

- `subject_exact` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-012.json:53`: "Patreon rank 1 creator paid member count (Matt and Shane's Secret Podcast) as accessed April 14, 2026"
  - card `working/signal_extraction/cards/SC-R1-012.json:11`: "Patreon rank 1 creator paid member count (Matt and Shane's Secret Podcast)"
- `actor_level` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-012.json:54`: "seller"
  - card `working/signal_extraction/cards/SC-R1-012.json:12`: "source"
- `traceability_pointer` — **NO-CLASIFICABLE**
  - skeleton: `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-012.json (clave `traceability_pointer` ausente bajo `_extraction_context`)`
  - card `working/signal_extraction/cards/SC-R1-012.json:31`: [{"pointer_type": "url", "pointer_value": "https://graphtreon.com/top-patreon-creators", "secondary_pointer": null}, {"pointer_type": "source_record_ref", "pointer_value": "ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-008-SNP-001", "secondary_pointer": "SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-008"}]

### SC-R1-013 (skeleton SC-R1-013)

- `subject_exact` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-013.json:53`: "Graphtreon-estimated monthly earnings and paid member count for 'the yard' podcast (Patreon rank 9) as accessed April 14, 2026"
  - card `working/signal_extraction/cards/SC-R1-013.json:11`: "Graphtreon-estimated monthly earnings and paid member count for 'the yard' podcast (Patreon rank 9)"
- `actor_level` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-013.json:54`: "seller"
  - card `working/signal_extraction/cards/SC-R1-013.json:12`: "source"
- `traceability_pointer` — **NO-CLASIFICABLE**
  - skeleton: `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-013.json (clave `traceability_pointer` ausente bajo `_extraction_context`)`
  - card `working/signal_extraction/cards/SC-R1-013.json:34`: [{"pointer_type": "url", "pointer_value": "https://graphtreon.com/top-patreon-creators", "secondary_pointer": null}, {"pointer_type": "source_record_ref", "pointer_value": "ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-008-SNP-002", "secondary_pointer": "SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-008"}]

### SC-R1-014 (skeleton SC-R1-014)

- `subject_exact` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-014.json:53`: "Graphtreon top Patreon podcast creator rankings with paid member counts and monthly earnings as accessed April 2026"
  - card `working/signal_extraction/cards/SC-R1-014.json:11`: "Matt and Shane's Secret Podcast paid member count on Graphtreon's podcast rankings page"
- `actor_level` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-014.json:54`: "seller"
  - card `working/signal_extraction/cards/SC-R1-014.json:12`: "source"
- `metric_type` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-014.json:59`: "revenue"
  - card `working/signal_extraction/cards/SC-R1-014.json:17`: "unknown"
- `metric_unit` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-014.json:61`: "USD/month and paid members (multiple creators)"
  - card `working/signal_extraction/cards/SC-R1-014.json:19`: "paid members"
- `uncertainties` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-014.json:69`: ["net_vs_gross_ambiguity", "time_scope_unclear"]
  - card `working/signal_extraction/cards/SC-R1-014.json:27`: ["time_scope_unclear"]
- `traceability_pointer` — **NO-CLASIFICABLE**
  - skeleton: `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-014.json (clave `traceability_pointer` ausente bajo `_extraction_context`)`
  - card `working/signal_extraction/cards/SC-R1-014.json:30`: [{"pointer_type": "url", "pointer_value": "https://graphtreon.com/top-patreon-creators/podcasts", "secondary_pointer": null}, {"pointer_type": "source_record_ref", "pointer_value": "ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-009-SNP-001", "secondary_pointer": "SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-009"}]

### SC-R1-015 (skeleton SC-R1-015)

- `actor_level` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-015.json:54`: "seller"
  - card `working/signal_extraction/cards/SC-R1-015.json:12`: "third_party"
- `uncertainties` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-015.json:71`: ["source_date_unclear"]
  - card `working/signal_extraction/cards/SC-R1-015.json:29`: ["source_date_unclear", "context_insufficient"]
- `traceability_pointer` — **NO-CLASIFICABLE**
  - skeleton: `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-015.json (clave `traceability_pointer` ausente bajo `_extraction_context`)`
  - card `working/signal_extraction/cards/SC-R1-015.json:33`: [{"pointer_type": "url", "pointer_value": "https://impact.hypable.com/patreon-consultation", "secondary_pointer": null}, {"pointer_type": "source_record_ref", "pointer_value": "ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-010-SNP-001", "secondary_pointer": "SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-010"}]

### SC-R1-016 (skeleton SC-R1-016)

- `actor_level` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-016.json:54`: "seller"
  - card `working/signal_extraction/cards/SC-R1-016.json:12`: "third_party"
- `traceability_pointer` — **NO-CLASIFICABLE**
  - skeleton: `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-016.json (clave `traceability_pointer` ausente bajo `_extraction_context`)`
  - card `working/signal_extraction/cards/SC-R1-016.json:35`: [{"pointer_type": "url", "pointer_value": "https://stealthagents.com/patreon-growth-agency", "secondary_pointer": null}, {"pointer_type": "source_record_ref", "pointer_value": "ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-011-SNP-001", "secondary_pointer": "SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-011"}]

### SC-R1-017 (skeleton SC-R1-017)

- `subject_exact` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-017.json:53`: "Patreon search interface primary category filter options as observed April 2026"
  - card `working/signal_extraction/cards/SC-R1-017.json:11`: "Patreon search interface primary category filter options"
- `uncertainties` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-017.json:67`: ["source_date_unclear"]
  - card `working/signal_extraction/cards/SC-R1-017.json:25`: ["source_date_unclear", "context_insufficient"]
- `traceability_pointer` — **NO-CLASIFICABLE**
  - skeleton: `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-017.json (clave `traceability_pointer` ausente bajo `_extraction_context`)`
  - card `working/signal_extraction/cards/SC-R1-017.json:29`: [{"pointer_type": "url", "pointer_value": "https://www.patreon.com/search", "secondary_pointer": null}, {"pointer_type": "source_record_ref", "pointer_value": "ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-012-SNP-001", "secondary_pointer": "SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-012"}]

### SC-R1-018 (skeleton SC-R1-018)

- `actor_level` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-018.json:54`: "seller"
  - card `working/signal_extraction/cards/SC-R1-018.json:12`: "third_party"
- `traceability_pointer` — **NO-CLASIFICABLE**
  - skeleton: `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-018.json (clave `traceability_pointer` ausente bajo `_extraction_context`)`
  - card `working/signal_extraction/cards/SC-R1-018.json:31`: [{"pointer_type": "url", "pointer_value": "https://www.sodaspoon.com/blogs/agency/patreon-agency", "secondary_pointer": null}, {"pointer_type": "source_record_ref", "pointer_value": "ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-013-SNP-001", "secondary_pointer": "SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-013"}]

### SC-R1-019 (skeleton SC-R1-019)

- `actor_level` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-019.json:54`: ["marketplace", "seller"]
  - card `working/signal_extraction/cards/SC-R1-019.json:12`: "platform"
- `local_qualifiers` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-019.json:71`: ["Starting Jan 1, 2023", "to comply with local laws", "impuesto sobre la renta (ISR) and impuesto al valor agregado (IVA)", "The amount Etsy is required to withhold can be as high as 36% of the order total", "if you register for a Registro Federal de Contribuyentes (RFC) identification number and add it to your Etsy account, significantly less tax will be withheld"]
  - card `working/signal_extraction/cards/SC-R1-019.json:26`: ["Starting Jan 1, 2023", "to comply with local laws", "impuesto sobre la renta (ISR) and impuesto al valor agregado (IVA)"]
- `uncertainties` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-019.json:78`: ["current_vs_historical_ambiguity"]
  - card `working/signal_extraction/cards/SC-R1-019.json:31`: ["current_vs_historical_ambiguity", "context_insufficient"]
- `traceability_pointer` — **NO-CLASIFICABLE**
  - skeleton: `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-019.json (clave `traceability_pointer` ausente bajo `_extraction_context`)`
  - card `working/signal_extraction/cards/SC-R1-019.json:35`: [{"pointer_type": "url", "pointer_value": "https://community.etsy.com/t5/Announcements/Important-New-tax-requirements-for-sellers-in-Mexico/td-p/140124123", "secondary_pointer": null}, {"pointer_type": "source_record_ref", "pointer_value": "ER-SP-compass_artifact_wf-0ffe7308-62e3-4530-ae68-93720df60f34_text_markdown-001-SNP-001", "secondary_pointer": "SP-compass_artifact_wf-0ffe7308-62e3-4530-ae68-93720df60f34_text_markdown-001"}]

### SC-R1-020 (skeleton SC-R1-020)

- `subject_exact` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-020.json:53`: "Craftybase Etsy fee calculator country expansion: 9 Payoneer-based countries added as of March 2026 changelog"
  - card `working/signal_extraction/cards/SC-R1-020.json:11`: "Craftybase Etsy fee calculator country expansion: 9 Payoneer-based countries added"
- `actor_level` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-020.json:54`: "marketplace"
  - card `working/signal_extraction/cards/SC-R1-020.json:12`: "source"
- `metric_value_raw` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-020.json:61`: "9"
  - card `working/signal_extraction/cards/SC-R1-020.json:19`: 9
- `uncertainties` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-020.json:81`: ["context_insufficient"]
  - card `working/signal_extraction/cards/SC-R1-020.json:39`: ["time_scope_unclear", "context_insufficient"]
- `traceability_pointer` — **NO-CLASIFICABLE**
  - skeleton: `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-020.json (clave `traceability_pointer` ausente bajo `_extraction_context`)`
  - card `working/signal_extraction/cards/SC-R1-020.json:43`: [{"pointer_type": "url", "pointer_value": "https://craftybase.com/etsy/fee-calculator", "secondary_pointer": null}, {"pointer_type": "source_record_ref", "pointer_value": "ER-SP-compass_artifact_wf-0ffe7308-62e3-4530-ae68-93720df60f34_text_markdown-002-SNP-001", "secondary_pointer": "SP-compass_artifact_wf-0ffe7308-62e3-4530-ae68-93720df60f34_text_markdown-002"}]

### SC-R1-021 (skeleton SC-R1-021)

- `actor_level` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-021.json:54`: "mixed"
  - card `working/signal_extraction/cards/SC-R1-021.json:12`: "platform"
- `traceability_pointer` — **NO-CLASIFICABLE**
  - skeleton: `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-021.json (clave `traceability_pointer` ausente bajo `_extraction_context`)`
  - card `working/signal_extraction/cards/SC-R1-021.json:60`: [{"pointer_type": "url", "pointer_value": "https://help.etsy.com/hc/en-us/articles/115015587567-How-VAT-Works-on-Digital-Items", "secondary_pointer": null}, {"pointer_type": "source_record_ref", "pointer_value": "ER-SP-compass_artifact_wf-0ffe7308-62e3-4530-ae68-93720df60f34_text_markdown-003-SNP-001", "secondary_pointer": "SP-compass_artifact_wf-0ffe7308-62e3-4530-ae68-93720df60f34_text_markdown-003"}]

### SC-R1-022 (skeleton SC-R1-022)

- `actor_level` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-022.json:54`: ["buyer", "seller"]
  - card `working/signal_extraction/cards/SC-R1-022.json:12`: "platform"
- `local_qualifiers` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-022.json:71`: ["As of August 29, 2025", "most packages shipped to the US", "Delivered Duty Paid (DDP): The seller pays the tariffs up front, and the cost is included in the total at checkout", "Delivered Duty Unpaid (DDU): The buyer is responsible for paying any tariffs and associated fees directly to the shipping carrier upon delivery"]
  - card `working/signal_extraction/cards/SC-R1-022.json:26`: ["As of August 29, 2025", "most packages shipped to the US"]
- `traceability_pointer` — **NO-CLASIFICABLE**
  - skeleton: `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-022.json (clave `traceability_pointer` ausente bajo `_extraction_context`)`
  - card `working/signal_extraction/cards/SC-R1-022.json:33`: [{"pointer_type": "url", "pointer_value": "https://help.etsy.com/hc/en-us/articles/115015691007-Will-I-Have-to-Pay-for-Tax-Customs-or-Tariffs-on-My-Order", "secondary_pointer": null}, {"pointer_type": "source_record_ref", "pointer_value": "ER-SP-compass_artifact_wf-0ffe7308-62e3-4530-ae68-93720df60f34_text_markdown-004-SNP-001", "secondary_pointer": "SP-compass_artifact_wf-0ffe7308-62e3-4530-ae68-93720df60f34_text_markdown-004"}]

### SC-R1-023 (skeleton SC-R1-023)

- `actor_level` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-023.json:54`: "seller"
  - card `working/signal_extraction/cards/SC-R1-023.json:12`: "platform"
- `local_qualifiers` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-023.json:67`: ["Sellers in countries with * next to their names can accept Etsy Payments with a Payoneer Payment Account", "Etsy can only offer payment services in certain countries at this time", "We are working to support additional countries in the future"]
  - card `working/signal_extraction/cards/SC-R1-023.json:25`: ["only in certain countries at this time", "working to support additional countries in the future"]
- `uncertainties` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-023.json:72`: ["source_date_unclear"]
  - card `working/signal_extraction/cards/SC-R1-023.json:29`: ["source_date_unclear", "context_insufficient"]
- `traceability_pointer` — **NO-CLASIFICABLE**
  - skeleton: `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-023.json (clave `traceability_pointer` ausente bajo `_extraction_context`)`
  - card `working/signal_extraction/cards/SC-R1-023.json:33`: [{"pointer_type": "url", "pointer_value": "https://help.etsy.com/hc/en-us/articles/115015710408-Countries-Eligible-for-Etsy-Payments", "secondary_pointer": null}, {"pointer_type": "source_record_ref", "pointer_value": "ER-SP-compass_artifact_wf-0ffe7308-62e3-4530-ae68-93720df60f34_text_markdown-005-SNP-001", "secondary_pointer": "SP-compass_artifact_wf-0ffe7308-62e3-4530-ae68-93720df60f34_text_markdown-005"}]

### SC-R1-024 (skeleton SC-R1-024)

- `actor_level` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-024.json:54`: "seller"
  - card `working/signal_extraction/cards/SC-R1-024.json:12`: "platform"
- `local_qualifiers` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-024.json:66`: ["At this time", "sellers in certain locations where Etsy Payments isn't available won't be able to sign up to sell on Etsy", "If you don't see your country in the dropdown menu during the shop opening process, then selling on Etsy isn't available in your country at this time", "We're working on expanding the availability of Etsy Payments so we can offer the benefits Etsy Payments provides to sellers in more countries"]
  - card `working/signal_extraction/cards/SC-R1-024.json:24`: ["At this time"]
- `traceability_pointer` — **NO-CLASIFICABLE**
  - skeleton: `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-024.json (clave `traceability_pointer` ausente bajo `_extraction_context`)`
  - card `working/signal_extraction/cards/SC-R1-024.json:31`: [{"pointer_type": "url", "pointer_value": "https://help.etsy.com/hc/en-us/articles/1500006519562-Why-Can-t-I-Open-a-Shop-in-My-Country", "secondary_pointer": null}, {"pointer_type": "source_record_ref", "pointer_value": "ER-SP-compass_artifact_wf-0ffe7308-62e3-4530-ae68-93720df60f34_text_markdown-006-SNP-001", "secondary_pointer": "SP-compass_artifact_wf-0ffe7308-62e3-4530-ae68-93720df60f34_text_markdown-006"}]

### SC-R1-025 (skeleton SC-R1-025)

- `actor_level` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-025.json:54`: "seller"
  - card `working/signal_extraction/cards/SC-R1-025.json:12`: "platform"
- `local_qualifiers` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-025.json:67`: ["Etsy only supports deposits in United States Dollars (USD) to your Payoneer Payment Account", "you can withdraw earnings from your Payoneer Payment Account to your local bank account in over 150 countries and currencies", "with Payoneer's bank transfer withdrawal service", "Payoneer may charge a fee for this service"]
  - card `working/signal_extraction/cards/SC-R1-025.json:25`: ["Payoneer may charge a fee for this service"]
- `traceability_pointer` — **NO-CLASIFICABLE**
  - skeleton: `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-025.json (clave `traceability_pointer` ausente bajo `_extraction_context`)`
  - card `working/signal_extraction/cards/SC-R1-025.json:31`: [{"pointer_type": "url", "pointer_value": "https://help.etsy.com/hc/en-us/articles/16999319005207-How-Do-I-Use-a-Payoneer-Account-With-Etsy-Payments", "secondary_pointer": null}, {"pointer_type": "source_record_ref", "pointer_value": "ER-SP-compass_artifact_wf-0ffe7308-62e3-4530-ae68-93720df60f34_text_markdown-007-SNP-001", "secondary_pointer": "SP-compass_artifact_wf-0ffe7308-62e3-4530-ae68-93720df60f34_text_markdown-007"}]

### SC-R1-1179 (skeleton SC-R1-002)

- `subject_exact` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-002.json:53`: "Number of Patreon creators with at least one paying member as of February 2026"
  - card `working/signal_extraction/cards/SC-R1-1179.json:11`: "Change in the number of Patreon creators with at least one paying member between June 2025 and February 2026"
- `actor_level` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-002.json:54`: "seller"
  - card `working/signal_extraction/cards/SC-R1-1179.json:12`: "source"
- `metric_value_raw` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-002.json:60`: "286,287"
  - card `working/signal_extraction/cards/SC-R1-1179.json:18`: "around 5%"
- `metric_unit` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-002.json:61`: "creators with at least one paying member"
  - card `working/signal_extraction/cards/SC-R1-1179.json:19`: "approximate percent decline in creator count"
- `time_scope_raw` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-002.json:62`: "as of February 2026"
  - card `working/signal_extraction/cards/SC-R1-1179.json:20`: "since June 2025"
- `evidence_role` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-002.json:65`: "database_fact"
  - card `working/signal_extraction/cards/SC-R1-1179.json:23`: "comparative_commentary"
- `local_qualifiers` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-002.json:66`: ["as of February 2026", "Based on Graphtreon data", "That's a drop of around 5% since June 2025"]
  - card `working/signal_extraction/cards/SC-R1-1179.json:24`: ["Based on Graphtreon data"]
- `traceability_pointer` — **NO-CLASIFICABLE**
  - skeleton: `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-002.json (clave `traceability_pointer` ausente bajo `_extraction_context`)`
  - card `working/signal_extraction/cards/SC-R1-1179.json:30`: [{"pointer_type": "url", "pointer_value": "https://backlinko.com/patreon-users", "secondary_pointer": null}, {"pointer_type": "source_record_ref", "pointer_value": "ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-002-SNP-001", "secondary_pointer": "SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-002"}]

### SC-R1-1180 (skeleton SC-R1-003)

- `subject_exact` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-003.json:53`: "Concentration of Patreon creators with more than 20,000 paying members"
  - card `working/signal_extraction/cards/SC-R1-1180.json:11`: "Patreon's top creator by paid member count (Matt and Shane's Secret Podcast) and its paid member total"
- `actor_level` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-003.json:54`: "seller"
  - card `working/signal_extraction/cards/SC-R1-1180.json:12`: "source"
- `metric_value_raw` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-003.json:60`: "31"
  - card `working/signal_extraction/cards/SC-R1-1180.json:18`: "124,452"
- `metric_unit` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-003.json:61`: "creators with more than 20,000 paying members"
  - card `working/signal_extraction/cards/SC-R1-1180.json:19`: "paid members"
- `time_scope_raw` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-003.json:62`: "Currently (article last updated Feb. 25, 2026)"
  - card `working/signal_extraction/cards/SC-R1-1180.json:20`: "Currently"
- `traceability_pointer` — **NO-CLASIFICABLE**
  - skeleton: `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-003.json (clave `traceability_pointer` ausente bajo `_extraction_context`)`
  - card `working/signal_extraction/cards/SC-R1-1180.json:28`: [{"pointer_type": "url", "pointer_value": "https://backlinko.com/patreon-users", "secondary_pointer": null}, {"pointer_type": "source_record_ref", "pointer_value": "ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-002-SNP-002", "secondary_pointer": "SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-002"}]

### SC-R1-1181 (skeleton SC-R1-014)

- `subject_exact` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-014.json:53`: "Graphtreon top Patreon podcast creator rankings with paid member counts and monthly earnings as accessed April 2026"
  - card `working/signal_extraction/cards/SC-R1-1181.json:11`: "Chapo Trap House podcast paid member count and estimated monthly earnings on Graphtreon's podcast rankings page"
- `actor_level` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-014.json:54`: "seller"
  - card `working/signal_extraction/cards/SC-R1-1181.json:12`: "source"
- `metric_unit` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-014.json:61`: "USD/month and paid members (multiple creators)"
  - card `working/signal_extraction/cards/SC-R1-1181.json:19`: "USD/month"
- `local_qualifiers` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-014.json:66`: ["Updated daily"]
  - card `working/signal_extraction/cards/SC-R1-1181.json:24`: ["47,046 Paid Members", "Updated daily"]
- `traceability_pointer` — **NO-CLASIFICABLE**
  - skeleton: `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-014.json (clave `traceability_pointer` ausente bajo `_extraction_context`)`
  - card `working/signal_extraction/cards/SC-R1-1181.json:32`: [{"pointer_type": "url", "pointer_value": "https://graphtreon.com/top-patreon-creators/podcasts", "secondary_pointer": null}, {"pointer_type": "source_record_ref", "pointer_value": "ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-009-SNP-001", "secondary_pointer": "SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-009"}]

### SC-R1-1182 (skeleton SC-R1-014)

- `subject_exact` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-014.json:53`: "Graphtreon top Patreon podcast creator rankings with paid member counts and monthly earnings as accessed April 2026"
  - card `working/signal_extraction/cards/SC-R1-1182.json:11`: "TrueAnon Podcast paid member count and estimated monthly earnings on Graphtreon's podcast rankings page"
- `actor_level` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-014.json:54`: "seller"
  - card `working/signal_extraction/cards/SC-R1-1182.json:12`: "source"
- `metric_unit` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-014.json:61`: "USD/month and paid members (multiple creators)"
  - card `working/signal_extraction/cards/SC-R1-1182.json:19`: "USD/month"
- `local_qualifiers` — **NORMALIZADO**
  - skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-014.json:66`: ["Updated daily"]
  - card `working/signal_extraction/cards/SC-R1-1182.json:24`: ["45,985 Paid Members", "Updated daily"]
- `traceability_pointer` — **NO-CLASIFICABLE**
  - skeleton: `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-014.json (clave `traceability_pointer` ausente bajo `_extraction_context`)`
  - card `working/signal_extraction/cards/SC-R1-1182.json:32`: [{"pointer_type": "url", "pointer_value": "https://graphtreon.com/top-patreon-creators/podcasts", "secondary_pointer": null}, {"pointer_type": "source_record_ref", "pointer_value": "ER-SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-009-SNP-001", "secondary_pointer": "SP-compass_artifact_wf-02711d62-b64f-4287-b85f-3f3a57c9da67_text_markdown-009"}]

## Anexo A — Detalle PERDIDO

No requerido por el encargo; se incluye para auditabilidad de los conteos PERDIDO.

### SC-R1-001 (skeleton SC-R1-001)

- `parser_notes`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-001.json:70`: ["Marketing copy for third-party Patreon analytics scraping tool; no quantitative claims present"] → card `working/signal_extraction/cards/SC-R1-001.json:44`: []

### SC-R1-002 (skeleton SC-R1-002)

- `parser_notes`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-002.json:72`: ["Secondary reporting: Backlinko article reports Graphtreon database data; the ~5% drop since June 2025 is comparative context, not the primary metric of this record"] → card `working/signal_extraction/cards/SC-R1-002.json:45`: []

### SC-R1-003 (skeleton SC-R1-003)

- `parser_notes`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-003.json:73`: ["Two metrics in snippet: 31 creators with >20,000 members (primary claim) and 124,452 paid members for top creator Matt and Shane's Secret Podcast (contextual); 'Currently' is undated relative to the article update date Feb 25 2026"] → card `working/signal_extraction/cards/SC-R1-003.json:48`: []

### SC-R1-004 (skeleton SC-R1-004)

- `parser_notes`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-004.json:73`: ["Chrome Web Store product listing for Patreon tracking browser extension; no quantitative claims; mentions STL miniature creators as primary use case; targets patrons/buyers not creators"] → card `working/signal_extraction/cards/SC-R1-004.json:47`: []

### SC-R1-005 (skeleton SC-R1-005)

- `parser_notes`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-005.json:75`: ["Chrome Web Store listing for Patreon scraper extension; pricing is the primary extractable structured claim; full feature list and usage instructions also present in snippet"] → card `working/signal_extraction/cards/SC-R1-005.json:48`: []

### SC-R1-006 (skeleton SC-R1-006)

- `parser_notes`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-006.json:73`: ["Marketing copy for third-party Patreon analytics SaaS tool targeting creators; 'You're losing patrons every month' is rhetorical framing, not a factual metric claim; no quantitative data present"] → card `working/signal_extraction/cards/SC-R1-006.json:47`: []

### SC-R1-007 (skeleton SC-R1-007)

- `parser_notes`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-007.json:71`: ["Two metrics in snippet: percentage share (25.88%) and absolute creator count (54,582); both refer to the Video category; article titled 'Patreon Statistics 2025'"] → card `working/signal_extraction/cards/SC-R1-007.json:46`: []

### SC-R1-008 (skeleton SC-R1-008)

- `time_scope_raw`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-008.json:62`: "as of January 2025 (from article context)" → card `working/signal_extraction/cards/SC-R1-008.json:20`: null
- `time_scope_normalized_if_safe`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-008.json:63`: "2025-01" → card `working/signal_extraction/cards/SC-R1-008.json:21`: null
- `parser_notes`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-008.json:72`: ["Time scope (January 2025) inferred from article title and SNP-001 in same source packet; this snippet contains counts across 9 categories; no single primary metric_value_raw applicable; snippet_context_before is null so date cannot be confirmed from this snippet alone"] → card `working/signal_extraction/cards/SC-R1-008.json:47`: []

### SC-R1-009 (skeleton SC-R1-009)

- `time_scope_raw`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-009.json:62`: "Accessed April 14, 2026; Updated daily" → card `working/signal_extraction/cards/SC-R1-009.json:20`: null
- `time_scope_normalized_if_safe`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-009.json:63`: "2026-04-14" → card `working/signal_extraction/cards/SC-R1-009.json:21`: null
- `parser_notes`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-009.json:72`: ["Live database figure from Graphtreon stats page; 'Updated daily' qualifier means exact date of underlying data may lag; figure differs from Backlinko Feb 2026 figure (286,287) reflecting different time points"] → card `working/signal_extraction/cards/SC-R1-009.json:46`: []

### SC-R1-010 (skeleton SC-R1-010)

- `time_scope_raw`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-010.json:62`: "Accessed April 14, 2026; Updated daily" → card `working/signal_extraction/cards/SC-R1-010.json:20`: null
- `time_scope_normalized_if_safe`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-010.json:63`: "2026-04" → card `working/signal_extraction/cards/SC-R1-010.json:21`: null
- `parser_notes`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-010.json:74`: ["'Estimated' qualifier and 'excludes hidden earnings' are critical — figure underestimates total payouts; unclear whether Patreon platform fees are already deducted from this figure; 'Updated daily' qualifier means exact date may lag"] → card `working/signal_extraction/cards/SC-R1-010.json:48`: []

### SC-R1-011 (skeleton SC-R1-011)

- `time_scope_raw`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-011.json:62`: "Accessed April 14, 2026" → card `working/signal_extraction/cards/SC-R1-011.json:20`: null
- `time_scope_normalized_if_safe`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-011.json:63`: "2026-04-14" → card `working/signal_extraction/cards/SC-R1-011.json:21`: null
- `parser_notes`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-011.json:70`: ["Navigation layout extracted from Graphtreon stats page; represents category taxonomy tracked by Graphtreon for Patreon creators; includes adult subcategories; no quantitative data; navigation may change over time"] → card `working/signal_extraction/cards/SC-R1-011.json:46`: []

### SC-R1-012 (skeleton SC-R1-012)

- `time_scope_raw`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-012.json:62`: "Accessed April 14, 2026; Updated daily" → card `working/signal_extraction/cards/SC-R1-012.json:20`: null
- `time_scope_normalized_if_safe`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-012.json:63`: "2026-04-14" → card `working/signal_extraction/cards/SC-R1-012.json:21`: null
- `parser_notes`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-012.json:73`: ["Creator: Matt and Shane's Secret Podcast, described as 'Creating Hot Casts'; rank 1 as of access date; member count (127,986) differs from Backlinko Feb 2026 figure (124,452) due to different access dates"] → card `working/signal_extraction/cards/SC-R1-012.json:47`: []

### SC-R1-013 (skeleton SC-R1-013)

- `time_scope_raw`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-013.json:62`: "Accessed April 14, 2026; Updated daily" → card `working/signal_extraction/cards/SC-R1-013.json:20`: null
- `time_scope_normalized_if_safe`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-013.json:63`: "2026-04" → card `working/signal_extraction/cards/SC-R1-013.json:21`: null
- `parser_notes`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-013.json:76`: ["Two metrics: monthly earnings ($269,922) and paid member count (42,523); 'the yard' is a podcast; Graphtreon dollar figure likely represents gross patron pledges before Patreon platform fee deduction"] → card `working/signal_extraction/cards/SC-R1-013.json:51`: []

### SC-R1-014 (skeleton SC-R1-014)

- `time_scope_raw`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-014.json:62`: "Accessed April 2026; Updated daily" → card `working/signal_extraction/cards/SC-R1-014.json:20`: null
- `time_scope_normalized_if_safe`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-014.json:63`: "2026-04" → card `working/signal_extraction/cards/SC-R1-014.json:21`: null
- `parser_notes`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-014.json:73`: ["Three top podcast creators listed with mixed metrics; Matt and Shane's shows 118,491 members here vs 127,986 on main top-creators page (same source, different pages, slight discrepancy possibly due to different cached values or access timing); dollar amounts likely represent gross patron pledges before Patreon fee"] → card `working/signal_extraction/cards/SC-R1-014.json:47`: []

### SC-R1-015 (skeleton SC-R1-015)

- `parser_notes`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-015.json:74`: ["Marketing copy for Patreon consultation service; no quantitative claims; page references March 2022 for an online course launch but page itself is undated"] → card `working/signal_extraction/cards/SC-R1-015.json:48`: []

### SC-R1-016 (skeleton SC-R1-016)

- `parser_notes`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-016.json:77`: ["Marketing copy for Patreon growth agency; multiple metrics: service price ($1,600/mo), in-house equivalent ($71,500/yr), claimed savings ($52,300/yr), speed claim (3x), subscriber growth rate (40-60%); the growth rate claim has no methodology or evidentiary basis stated"] → card `working/signal_extraction/cards/SC-R1-016.json:51`: []

### SC-R1-017 (skeleton SC-R1-017)

- `time_scope_raw`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-017.json:62`: "Accessed April 2026" → card `working/signal_extraction/cards/SC-R1-017.json:20`: null
- `time_scope_normalized_if_safe`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-017.json:63`: "2026-04" → card `working/signal_extraction/cards/SC-R1-017.json:21`: null
- `parser_notes`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-017.json:70`: ["Patreon search interface navigation extracted; shows 6 primary category filters: Art, Podcast, Music, Games, Writing, Photography; no quantitative data"] → card `working/signal_extraction/cards/SC-R1-017.json:44`: []

### SC-R1-018 (skeleton SC-R1-018)

- `parser_notes`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-018.json:73`: ["Marketing/editorial blog post describing Patreon agency services; no quantitative data; 'invaluable' is subjective marketing language not a measurable claim; no basis or evidence cited for the retention/acquisition assertion"] → card `working/signal_extraction/cards/SC-R1-018.json:46`: []

### SC-R1-019 (skeleton SC-R1-019)

- `parser_notes`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-019.json:81`: ["Official Etsy community announcement about Mexico tax withholding; source_type is seller_forum per stage 1 but this is an official platform announcement; 36% is the maximum withholding rate; actual reduced rate with RFC registration is not stated in this snippet; page now behind login wall"] → card `working/signal_extraction/cards/SC-R1-019.json:51`: []

### SC-R1-020 (skeleton SC-R1-020)

- `time_scope_raw`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-020.json:63`: "March 2026" → card `working/signal_extraction/cards/SC-R1-020.json:21`: null
- `time_scope_normalized_if_safe`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-020.json:64`: "2026-03" → card `working/signal_extraction/cards/SC-R1-020.json:22`: null
- `parser_notes`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-020.json:84`: ["Third-party Etsy fee calculator tool (Craftybase) reporting 9 new Payoneer-supported countries; primary Etsy announcement for this expansion is not available in this snippet; countries listed: Argentina, Brazil, Chile, China, Egypt, India, Japan, South Korea, Thailand"] → card `working/signal_extraction/cards/SC-R1-020.json:59`: []

### SC-R1-021 (skeleton SC-R1-021)

- `parser_notes`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-021.json:102`: ["Etsy help center policy on VAT collection for digital items; 27 jurisdictions listed; 'the EU' represents multiple countries; page undated, URL returned 403; country list may have changed since publication; 'digital items' encompasses all digital product types not one specific category"] → card `working/signal_extraction/cards/SC-R1-021.json:75`: []

### SC-R1-022 (skeleton SC-R1-022)

- `parser_notes`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-022.json:78`: ["Etsy help center explanation of tariff responsibility; two distinct payment structures (DDP and DDU) described; tariff amounts not specified; policy applies to packages shipped to the US; cost structure differs by shipping method chosen by seller"] → card `working/signal_extraction/cards/SC-R1-022.json:49`: []

### SC-R1-023 (skeleton SC-R1-023)

- `parser_notes`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-023.json:75`: ["Etsy help center describes Payoneer-based Etsy Payments access for countries marked with asterisk; specific country list not included in this snippet; page undated; URL returned 403 on direct fetch"] → card `working/signal_extraction/cards/SC-R1-023.json:49`: []

### SC-R1-024 (skeleton SC-R1-024)

- `parser_notes`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-024.json:76`: ["Etsy help center explaining that Etsy Payments availability is a prerequisite for opening a shop; no specific countries listed; 'at this time' language indicates this is a current state subject to change; page undated"] → card `working/signal_extraction/cards/SC-R1-024.json:47`: []

### SC-R1-025 (skeleton SC-R1-025)

- `parser_notes`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-025.json:76`: ["Etsy help center describes Payoneer payout rail: Etsy deposits in USD, Payoneer offers withdrawal in local currency to local bank in 150+ countries; Payoneer fee applies to the bank transfer withdrawal step; exact Payoneer fee amount not stated"] → card `working/signal_extraction/cards/SC-R1-025.json:47`: []

### SC-R1-1179 (skeleton SC-R1-002)

- `time_scope_normalized_if_safe`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-002.json:63`: "2026-02" → card `working/signal_extraction/cards/SC-R1-1179.json:21`: null
- `parser_notes`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-002.json:72`: ["Secondary reporting: Backlinko article reports Graphtreon database data; the ~5% drop since June 2025 is comparative context, not the primary metric of this record"] → card `working/signal_extraction/cards/SC-R1-1179.json:47`: []

### SC-R1-1180 (skeleton SC-R1-003)

- `local_qualifiers`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-003.json:66`: ["Currently", "only 31 creators"] → card `working/signal_extraction/cards/SC-R1-1180.json:24`: []
- `parser_notes`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-003.json:73`: ["Two metrics in snippet: 31 creators with >20,000 members (primary claim) and 124,452 paid members for top creator Matt and Shane's Secret Podcast (contextual); 'Currently' is undated relative to the article update date Feb 25 2026"] → card `working/signal_extraction/cards/SC-R1-1180.json:45`: []

### SC-R1-1181 (skeleton SC-R1-014)

- `time_scope_raw`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-014.json:62`: "Accessed April 2026; Updated daily" → card `working/signal_extraction/cards/SC-R1-1181.json:20`: null
- `time_scope_normalized_if_safe`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-014.json:63`: "2026-04" → card `working/signal_extraction/cards/SC-R1-1181.json:21`: null
- `parser_notes`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-014.json:73`: ["Three top podcast creators listed with mixed metrics; Matt and Shane's shows 118,491 members here vs 127,986 on main top-creators page (same source, different pages, slight discrepancy possibly due to different cached values or access timing); dollar amounts likely represent gross patron pledges before Patreon fee"] → card `working/signal_extraction/cards/SC-R1-1181.json:50`: []

### SC-R1-1182 (skeleton SC-R1-014)

- `time_scope_raw`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-014.json:62`: "Accessed April 2026; Updated daily" → card `working/signal_extraction/cards/SC-R1-1182.json:20`: null
- `time_scope_normalized_if_safe`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-014.json:63`: "2026-04" → card `working/signal_extraction/cards/SC-R1-1182.json:21`: null
- `parser_notes`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-014.json:73`: ["Three top podcast creators listed with mixed metrics; Matt and Shane's shows 118,491 members here vs 127,986 on main top-creators page (same source, different pages, slight discrepancy possibly due to different cached values or access timing); dollar amounts likely represent gross patron pledges before Patreon fee"] → card `working/signal_extraction/cards/SC-R1-1182.json:50`: []

## Anexo B — ORIGEN-VACIO con card no vacia

Casos donde el skeleton no tenia valor y la card contiene valor (el valor no viajo desde
Phase 1; aparece en Phase 2). La categoria asignada sigue siendo ORIGEN-VACIO porque la
definicion opera sobre el estado del origen. Se listan para que el conteo no se lea como
card vacia:

- SC-R1-014, `metric_value_raw` → `metric_value_raw`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-014.json:60`: null → card `working/signal_extraction/cards/SC-R1-014.json:18`: "118,491"
- SC-R1-022, `uncertainties` → `uncertainties`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-022.json:77`: [] → card `working/signal_extraction/cards/SC-R1-022.json:30`: ["context_insufficient"]
- SC-R1-1179, `uncertainties` → `uncertainties`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-002.json:71`: [] → card `working/signal_extraction/cards/SC-R1-1179.json:27`: ["metric_unit_unclear"]
- SC-R1-1181, `metric_value_raw` → `metric_value_raw`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-014.json:60`: null → card `working/signal_extraction/cards/SC-R1-1181.json:18`: "$199,298 per month"
- SC-R1-1182, `metric_value_raw` → `metric_value_raw`: skeleton `working/signal_extraction/skeleton_batches/batch_001/skeleton_SC-R1-014.json:60`: null → card `working/signal_extraction/cards/SC-R1-1182.json:18`: "$203,188 per month"

## Anexo C — traceability_pointers top-level (suplementario)

Comparacion del array top-level `traceability_pointers` del skeleton (construido en la
preparacion, no es el campo del ER) contra el de la card: identico en 29/29 pares
.

## Bloque 4 — Cruce con state/output/field_population_signal_cards.md

Afirmacion citada en el encargo: `product_type_if_explicit`, `metric_type` y
`uncertainties` "estan 0/29 en Signal Card" (state/output/field_population_signal_cards.md:17,18,26).

Contenido literal de esas lineas: fila `product_type_if_explicit` (linea 17): N=29,
Poblado=29, Vacio=0, Fuera de enum (schema)=0, Fuera de enum (vocab)=0. Fila `metric_type`
(linea 18): N=29, Poblado=29, Vacio=0, Fuera de enum=0/0. Fila `uncertainties` (linea 26):
N=29, Poblado=27, Vacio=2, Fuera de enum=0/0. El unico "0 sobre 29" que esas tres lineas
afirman en comun es "Fuera de enum = 0".

Cruce con esta medicion:

| Campo | Esta medicion (lado card) | Lineas citadas | ¿Coincide? |
|---|---|---|---|
| `product_type_if_explicit` | 0 fuera de enum (SUCIO=0, ningun NORMALIZADO fuera de enum); 0 vacios; 29 con valor (27 `"unknown"`, 2 `"software"`) | Fuera de enum=0; Vacio=0; Poblado=29 | coincide |
| `metric_type` | 0 fuera de enum; 0 vacios; 29 con valor (18 `"unknown"`, 11 con valor distinto de `"unknown"`) | Fuera de enum=0; Vacio=0; Poblado=29 | coincide |
| `uncertainties` | 0 fuera de enum; 2 vacios (SC-R1-002, SC-R1-007); 27 con valor | Fuera de enum=0; Vacio=2; Poblado=27 | coincide |

La lectura "0/29 poblado" no coincide ni con el contenido literal de las lineas citadas
(que declaran Poblado=29, 29 y 27) ni con esta medicion (29, 29 y 27 cards con valor).
La cifra del archivo cuenta `"unknown"` como poblado; en esta medicion
`product_type_if_explicit` contiene `"unknown"` en 27/29 y `metric_type` en 18/29.
Ambas cifras quedan reportadas con sus fuentes; ninguna se ajusto.

Nota de alcance: el archivo citado mide la card aislada; esta medicion mide el par
skeleton→card. Las columnas comparadas (vacio, fuera de enum, con valor, lado card)
son las unicas comunes a ambas mediciones.

