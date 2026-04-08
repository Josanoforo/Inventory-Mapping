# Pipeline Flow Map: DG Shards → Inventory Mapping Input

Este documento mapea el flujo de información desde los shards crudos de Data Gathering hasta el punto donde la información está lista para entrar al Entry Gate de Inventory Mapping. Es una revisión de arquitectura read-only; no propone rediseños ni ejecuta nada.

Fuentes autoritativas: contratos en `upstream/`, schemas en `upstream/`, `scripts/parse_dg_shard.py`, `modules/01_entry_gate.md`, y archivos en `reference/`.

---

## Sección 1 — Diagrama de flujo

```
PUNTO DE ENTRADA
────────────────
input/data_gathering/shards/deep_search/DX-2_gumroad_v2.md
input/data_gathering/shards/gpt_custom/policy_etsy_fees_v1.md
input/data_gathering/shards/gpt_custom/reddit_buyer_pain_planners_v1.md
         │
         │  PHASE 0 — DATA GATHERING
         │  Proceso: scripts/parse_dg_shard.py
         │  source_tool derivado del nombre del directorio padre
         │  (parse_dg_shard.py líneas 438–447)
         │
         ▼
    ┌────┴─────────────────────────────────────────────┐
    │                                                   │
    ▼  verification_status = direct_verified            │
    │  verification_status = blocked_url_index_verified │
    ▼                                                   ▼
working/data_gathering/findings/                 working/data_gathering/diagnostics/
  <shard_id>__<finding_id>.json                   part_4/<shard_id>__<item_id>.json
  (Part 1: F-NN; Part 2: F-PNN)                  qa_notes/<shard_id>_qa.json
  [8 campos requeridos por finding]               (could_not_verify → diagnostics only)
    │                                                   │
    │  Part 1 + Part 2 únicamente                       │  STOP — no se pasan downstream
    │  Part 4 excluida                                  ✗
    │
    │  PHASE 1a — SOURCE INTAKE
    │  Proceso: MANUAL
    │  Guía: reference/source_packet_conversion_template.md
    │  Múltiples findings del mismo URL → 1 Source Packet con N snippets
    │  Sin script automatizado (template línea 1)
    │
    ▼
    ┌─ GATE 1: Source Intake Validator ──────────────────────────────────┐
    │  Contrato: upstream/source-intake/contracts/source_intake_validator.md │
    │  9 checks; 5 statuses; 14 failure codes                            │
    │  Schema de resultado: upstream/source-intake/schemas/              │
    │                        source_intake_validation.schema.json        │
    └────────────────────────────────────────────────────────────────────┘
         │
    ┌────┴──────────────────────────────────────┐
    │              │                            │
    ▼ pass /        ▼ rework                    ▼ parking_lot / reject
    pass_with_flags │                            │
    │               │ retorno para reparación    │ sin proceso downstream
    │               │ [path no especificado]     │ [path no especificado]
    ▼               ✗ (recoverable)             ✗
working/source_intake/packets/<packet_id>.json
  [20 campos requeridos por Source Packet]
    │
    │  PHASE 1b — DATA EXTRACTION
    │  Proceso: MANUAL
    │  Contrato: upstream/data-extraction/contracts/data_extraction_contract.md
    │  1 Extraction Record = 1 assertion localmente coherente
    │  Notes scrubbing si notas contienen contenido interpretivo →
    │    working/notes_scrubbing/scrubbing_log.jsonl
    │    (validator líneas 406–415; directorio no existe actualmente)
    │
    ▼
    ┌─ GATE 2: Data Extraction Validator ────────────────────────────────┐
    │  Contrato: upstream/data-extraction/contracts/data_extraction_validator.md │
    │  13 checks; 4 statuses (sin parking_lot); 20 failure codes         │
    │  Schema de resultado: upstream/data-extraction/schemas/            │
    │                        data_extraction_validator.schema.json       │
    └────────────────────────────────────────────────────────────────────┘
         │
    ┌────┴──────────────────────────────┐
    │              │                   │
    ▼ pass /        ▼ rework            ▼ reject
    pass_with_flags │                   │
    │               │ retorno           │ working/data_extraction/rejected_archive/
    │               │ [path no espec.]  │ (INFERIDO — no declarado en contrato)
    │               ✗                  ✗
    ▼
working/data_extraction/<record_id>.json
  [28 campos requeridos por Extraction Record]
  [PATH INFERIDO — no declarado en contrato]
    │
    │  PHASE 2 — SIGNAL EXTRACTION
    │  Proceso: MANUAL
    │  Contrato: upstream/signal-extraction/contracts/signal_extraction_contract.md
    │  Consolidación permitida: mismo source o mismo local fact
    │  Consolidación prohibida: cross-source
    │  Notes scrubbing → working/notes_scrubbing/scrubbing_log.jsonl
    │    (validator líneas 354–363; directorio no existe actualmente)
    │
    ▼
    ┌─ GATE 3: Signal Extraction Validator ──────────────────────────────┐
    │  Contrato: upstream/signal-extraction/contracts/                   │
    │             signal_extraction_validator.md                         │
    │  11 checks; 4 statuses; 19 failure codes                           │
    │  Schema de resultado: upstream/signal-extraction/schemas/          │
    │                        signal_validation.schema.json               │
    └────────────────────────────────────────────────────────────────────┘
         │
    ┌────┴──────────────────────────────┐
    │              │                   │
    ▼ pass /        ▼ rework            ▼ reject
    pass_with_flags │                   │
    │               │ [path no espec.]  │ [path no especificado]
    │               ✗                  ✗
    ▼
    ┌─ GATE 4: Signal-to-Inventory Entry Gate ───────────────────────────┐
    │  Contrato: upstream/signal-extraction/contracts/                   │
    │             signal_to_inventory_entry_gate.md                      │
    │  8 checks; 4 routing decisions; 14 failure reasons (schema) /      │
    │  11 (contrato) — divergencia reportada en Sección 5               │
    │  Schema de resultado: upstream/signal-extraction/schemas/          │
    │                        signal_inventory_gate.schema.json           │
    └────────────────────────────────────────────────────────────────────┘
         │
    ┌────┼────────────────────────────────────┐
    │    │                                    │
    ▼    ▼ preserve_as_isolated_signal        ▼ return_to_signal_rework /
    │    │   [PATH NO ESPECIFICADO]            │   reject_from_inventory_input
    │    │                                    │   [PATH NO ESPECIFICADO]
    │    ✗ (guardado, no activo en IM)        ✗
    ▼
  pass_to_inventory_mapping
  Signal Cards JSON (signal_id: SC-R<round>-<NNN>)
  [PATH DE ESCRITURA NO ESPECIFICADO]
    │
    │  [PROCESO NO IDENTIFICADO]
    │  Conversión JSON → Markdown
    │  Signal Cards en JSON (signal_card.schema.json)
    │  IM Entry Gate espera Markdown (modules/01_entry_gate.md línea 9)
    │  No existe contrato, script, ni proceso documentado para esta conversión
    │
    ▼
PUNTO FINAL
──────────────────────────────────────────────────────────────────────────
input/signal_cards_round_*.md
  (10 archivos, 1,560 cards — Markdown)
  (archivos no existen actualmente en el repo)
    │
    ▼  ════════════ HANDOFF A INVENTORY MAPPING ════════════
       modules/01_entry_gate.md — 5 checks
       Output: working/entry_gate/entry_gate_report.json
```

---

## Sección 2 — Detalle por fase

### 2.1 Phase 0 — Data Gathering

#### Input esperado

| Campo | Detalle |
|-------|---------|
| Formato | Markdown estructurado en 4 partes: Part 1 (clean findings), Part 2 (provisional findings), Part 3 (pattern candidates, sellado), Part 4 (could not verify) |
| Origen | Ejecución manual de shards de investigación por agente |
| Archivos actuales | `input/data_gathering/shards/deep_search/DX-2_gumroad_v2.md`, `input/data_gathering/shards/gpt_custom/policy_etsy_fees_v1.md`, `input/data_gathering/shards/gpt_custom/reddit_buyer_pain_planners_v1.md` |
| Estructura del shard | Definida en `reference/research_directions_protocol.md` Sección 9 (líneas 188–272): subject, direction, language, time window, allowed source_type, unit of observation, qualifiers, exclusions, delivery format, scope reminder |
| IDs de findings | Part 1: `F-NN`; Part 2: `F-PNN`; Part 4: `F-XNN` — por shard, no globales (`reference/research_directions_protocol.md` líneas 224–238) |
| Referencia de contrato | `reference/data_gathering_project_instructions_v4_5.md` (19 reglas + acceptance test 10 puntos); `reference/research_directions_protocol.md` |

#### Proceso

| Campo | Detalle |
|-------|---------|
| Implementación | `scripts/parse_dg_shard.py` — único paso automatizado en todo el pipeline |
| `source_tool` | Derivado del nombre del directorio padre del shard: `deep_search` o `gpt_custom` (líneas 438–447); cae a `"unknown"` con warning a stderr si no reconoce |
| Campos requeridos (8) | `what`, `verbatim_snippet`, `source`, `source_type`, `verification_status`, `date`, `signal_type`, `notes` — definidos en `REQUIRED_FIELD_MAP` (líneas 41–51) |
| Matching de labels | Regex acepta formato bold (`**Label:**`) o plain (`Label:`) (líneas 64–67) |
| Campos faltantes | Warning a stderr (línea 241); no lanza excepción, no suprime output |
| Part 3 | Sellado — no se parsea a findings individuales (contrato `reference/research_directions_protocol.md` línea 85) |

#### Output producido

| Artefacto | Path | Campos required | Referencia |
|-----------|------|-----------------|------------|
| Findings Part 1 + Part 2 | `working/data_gathering/findings/<shard_id>__<finding_id>.json` | 8 campos de `REQUIRED_FIELD_MAP` + extra fields | `scripts/parse_dg_shard.py` líneas 13–14 |
| Part 4 diagnostics | `working/data_gathering/diagnostics/part_4/<shard_id>__<item_id>.json` | `item_id`, `seller_or_subject`, `attempted`, `why_failed`, `urls_mentioned` | `scripts/parse_dg_shard.py` líneas 265–310 |
| QA notes | `working/data_gathering/diagnostics/qa_notes/<shard_id>_qa.json` | Secciones QA del shard | `scripts/parse_dg_shard.py` líneas 318–413 |
| Estado actual | 28 finding JSONs (25 Part 1 + 3 Part 2); 13 Part-4 items (solo de DX-2_gumroad_v2); 3 QA files | — | — |

#### Gates de validación

No existe gate formal en Phase 0. `parse_dg_shard.py` es el único procesador. Advertencias de campos faltantes van a stderr sin interrumpir la ejecución. No se produce artifact de validación.

#### Campos de juicio humano

Todos los campos del shard son producidos por el agente de investigación siguiendo las reglas de `reference/data_gathering_project_instructions_v4_5.md`. El campo `notes` contiene observaciones locales del agente, no input humano externo.

---

### 2.2 Phase 1a — Source Intake

#### Input esperado

| Campo | Detalle |
|-------|---------|
| Formato | JSON de findings — output de `parse_dg_shard.py` |
| Origen | `working/data_gathering/findings/*.json` — Part 1 (F-NN) y Part 2 (F-PNN) únicamente |
| Part 4 excluida | Confirmado por `upstream/source-intake/contracts/source_intake_contract.md` línea 22 |
| Campos required del finding | `what`, `verbatim_snippet`, `source`, `source_type`, `verification_status`, `date`, `signal_type` |
| Referencia | `reference/source_packet_conversion_template.md` Sección 1 |

#### Proceso

| Campo | Detalle |
|-------|---------|
| Implementación | **MANUAL** — sin script automatizado. Template: `reference/source_packet_conversion_template.md` línea 1: "Para usar mientras no exista un script automatizado" |
| Regla de colapso | Múltiples findings del mismo URL → 1 Source Packet con N snippets. Template líneas 8–9: "50 findings de DG probablemente producen 30–40 packets, no 50" |
| Operaciones internas | (1) Agrupar findings por URL; (2) llenar 11 campos mecánicos; (3) llenar 8 campos de clasificación; (4) verificar `traceability_status`; (5) guardar JSON — template líneas 11–23 |
| Findings Part 2 (provisional) | Heredan `traceability_status = weak` + incertidumbre `snippet_needs_reopen` (template líneas 168–172) |

#### Output producido

| Campo | Detalle |
|-------|---------|
| Formato | JSON per `upstream/source-intake/schemas/source_packet.schema.json` |
| Path | `working/source_intake/packets/<packet_id>.json` (template línea 23) |
| Campos required (20) | `packet_id`, `source_id`, `source_title`, `source_type`, `source_ref`, `source_date_if_available`, `author_or_actor_if_available`, `retrieval_method`, `retrieved_from`, `raw_search_context`, `snippets[]`, `possible_subjects[]`, `possible_actor_levels[]`, `possible_metric_types[]`, `possible_time_scopes[]`, `possible_geographies[]`, `uncertainties[]`, `priority_for_source_first`, `intake_notes`, `traceability_status` |
| Convención de IDs | `packet_id`: `SP-<batch>-<###>`; `source_id`: `SRC-<batch>-<###>`; `snippet_id`: `SNP-<###>` por packet (template líneas 282–288) |
| Sub-schema snippets | Cada snippet requiere: `snippet_id`, `snippet_text`, `context_before`, `context_after`, `location_pointer` — `location_pointer` requiere `pointer_type` y `pointer_value` (`source_packet.schema.json` líneas 233–293) |
| Estado actual | `working/source_intake/packets/` vacío — fase no iniciada |

#### Gates de validación

| Campo | Detalle |
|-------|---------|
| Validador | `upstream/source-intake/contracts/source_intake_validator.md` |
| Checks (9) | `single_source_boundary`, `source_metadata`, `traceability`, `local_snippets_present`, `snippet_context_sufficient`, `no_cross_source_summary`, `possible_fields_non_interpretive`, `uncertainties_preserved`, `priority_assignment_reasonable` |
| Statuses | `pass`, `pass_with_flags`, `rework`, `parking_lot`, `reject` |
| Failure codes (14) | `multiple_sources_fused`, `no_local_snippets`, `traceability_weak`, `cross_source_summary_carried_over`, `source_metadata_missing`, `snippet_context_missing`, `possible_subject_overinterpreted`, `possible_metric_overinterpreted`, `uncertainty_hidden`, `location_pointer_missing`, `packet_too_cooked_for_extraction`, `source_ref_missing`, `source_type_unclear`, `voice_container_mismatch` — `source_intake_validation.schema.json` líneas 71–86 |
| Destino de rejects | Path no especificado en contrato; `working/source_intake/rejected_archive/` existe vacío en el repo |
| Destino de rework | Path no especificado en contrato |
| Destino de parking_lot | Path no especificado en contrato |
| Schema de resultado | `upstream/source-intake/schemas/source_intake_validation.schema.json` |

#### Campos de juicio humano

`possible_subjects`, `possible_actor_levels`, `possible_metric_types`, `possible_time_scopes`, `possible_geographies`, `uncertainties`, `priority_for_source_first`, `traceability_status` — todos requieren juicio humano según `reference/source_packet_conversion_template.md` Sección 2. Los campos mecánicos (`packet_id`, `source_id`, `source_title`, `source_type`, `source_ref`, `retrieval_method`, `retrieved_from`, `raw_search_context`, `snippets`, `intake_notes`) se derivan directamente de los findings de entrada.

---

### 2.3 Phase 1b — Data Extraction

#### Input esperado

| Campo | Detalle |
|-------|---------|
| Formato | JSON Source Packets con `validation_status = pass` o `pass_with_flags` |
| Origen | `working/source_intake/packets/*.json` |
| Enlace a upstream | Campo `source_packet_id` en el Extraction Record referencia el `packet_id` del Source Packet (`data_extraction_record.schema.json` línea 47) |
| Referencia | `upstream/data-extraction/contracts/data_extraction_contract.md` líneas 23–43 |

#### Proceso

| Campo | Detalle |
|-------|---------|
| Implementación | **MANUAL** — sin script identificado |
| Operaciones permitidas | Registrar metadata de fuente, segmentar fuente en fragmentos, identificar fragmentos relevantes, construir Extraction Records, validar completitud/trazabilidad, exportar registros estructurados (`data_extraction_contract.md` líneas 64–77) |
| Unidad canónica | 1 Extraction Record = 1 assertion localmente coherente + contexto mínimo necesario (contrato línea 51) |
| Notes scrubbing | Si `parser_notes` contiene contenido interpretivo: (1) scrub con regex-replace; (2) log a `working/notes_scrubbing/scrubbing_log.jsonl`; (3) scrubber no re-ejecuta validador ni modifica otros campos — `data_extraction_validator.md` líneas 406–415. Directorio `working/notes_scrubbing/` no existe actualmente |
| Reglas de calidad | No colapsar capas funcionales (checkout ≠ payout); no convertir contexto en claim; preservar qualifiers; no resolver ambigüedad; 1 record = 1 fuente (contrato líneas 310–346) |

#### Output producido

| Campo | Detalle |
|-------|---------|
| Formato | JSON per `upstream/data-extraction/schemas/data_extraction_record.schema.json` |
| Path | **No declarado en contrato**. Inferido como `working/data_extraction/` por estructura de directorio existente |
| Campos required (28) | `extraction_id`, `source_packet_id`, `source_id`, `source_type`, `source_title`, `source_ref`, `source_date_if_available`, `author_or_actor_if_available`, `snippet_primary`, `snippet_context_before`, `snippet_context_after`, `claim_type`, `subject_exact`, `actor_level`, `platforms`, `product_type_if_explicit`, `metric_type`, `metric_value_raw`, `metric_unit`, `time_scope_raw`, `time_scope_normalized_if_safe`, `geography_if_explicit`, `evidence_role`, `local_qualifiers`, `uncertainties`, `parser_notes`, `signal_type`, `traceability_pointer` — schema líneas 8–37 |
| Divergencia contrato/schema | El contrato Sección 6 lista 25 campos; el schema requiere 28. `source_packet_id` y `signal_type` aparecen en `required[]` del schema pero están ausentes de la lista del contrato |
| Estado actual | `working/data_extraction/` contiene solo `rejected_archive/` vacío — fase no iniciada |

#### Gates de validación

| Campo | Detalle |
|-------|---------|
| Validador | `upstream/data-extraction/contracts/data_extraction_validator.md` |
| Checks (13) | `traceability`, `subject_exact`, `actor_level`, `claim_type`, `metric_and_unit`, `time_scope`, `evidence_role`, `qualifiers`, `uncertainties`, `no_cross_source_synthesis`, `single_claim_boundary`, `claim_snippet_token_alignment`, `notes_locality` |
| Statuses (4) | `pass`, `pass_with_flags`, `rework`, `reject` — **sin `parking_lot`**, a diferencia del Source Intake Validator |
| Failure codes | Schema: 20 (`data_extraction_validator.schema.json` líneas 79–99); Contrato: 19 — `notes_interpretive_content` aparece en schema pero no listado por separado en contrato (divergencia reportada en Sección 5) |
| Destino de rejects | `working/data_extraction/rejected_archive/validator/` (INFERIDO — existe vacío; no declarado en contrato) |
| Destino de rework | Path no especificado en contrato; `working/data_extraction/rejected_archive/extraction/` existe vacío (convención inferida) |
| Schema de resultado | `upstream/data-extraction/schemas/data_extraction_validator.schema.json` |

#### Campos de juicio humano

`subject_exact`, `actor_level`, `claim_type`, `evidence_role`, `local_qualifiers`, `uncertainties`, `parser_notes` requieren juicio humano. `snippet_primary`, `snippet_context_before`, `snippet_context_after`, `metric_value_raw`, `metric_unit`, `time_scope_raw`, `traceability_pointer` se derivan directamente de la fuente.

---

### 2.4 Phase 2 — Signal Extraction

#### Input esperado

| Campo | Detalle |
|-------|---------|
| Formato | JSON Extraction Records con `validation_status = pass` o `pass_with_flags` |
| Rework aceptado | Solo si explícitamente corregido y revalidado (`signal_extraction_contract.md` línea 34) |
| No aceptado | Records con `reject`, sin trazabilidad, con cross-source synthesis, `subject_exact` destruido, niveles colapsados, interpretación downstream ya hecha (contrato líneas 36–41) |
| Referencia | `upstream/signal-extraction/contracts/signal_extraction_contract.md` líneas 30–42 |

#### Proceso

| Campo | Detalle |
|-------|---------|
| Implementación | **MANUAL** — sin script identificado |
| Unidad canónica | Signal Card = 1 observación discreta, trazable, formulada observacionalmente, derivada de 1 o más Extraction Records del mismo source o mismo local fact (contrato líneas 50–58) |
| Fusión permitida | Misma fuente local + mismo `subject_exact` + mismo local fact + sin interpretación añadida (contrato líneas 214–224) |
| Fusión prohibida | Múltiples fuentes, diferentes sellers, múltiples plataformas, diferentes momentos históricos, claims que requieren comparación (contrato líneas 226–230) |
| Notes scrubbing | Igual que Phase 1b: scrub + log a `working/notes_scrubbing/scrubbing_log.jsonl` si `notes_interpretive_content` flagged (`signal_extraction_validator.md` líneas 354–363) |
| Operaciones prohibidas | Comparar fuentes, declarar contradicción, agrupar por tema, formular tensiones, priorizar, interpretar causas, proponer oportunidades, convertir ausencia en gap, resumir "el mercado" (contrato líneas 80–92) |

#### Output producido

| Campo | Detalle |
|-------|---------|
| Formato | JSON per `upstream/signal-extraction/schemas/signal_card.schema.json` |
| Path | **No especificado en contrato ni schema**. No existe directorio `working/signal_extraction/` en el repo |
| Campos required (22) | `signal_id`, `source_record_ids[]`, `source_ids[]`, `round`, `signal_text`, `signal_type`, `subject_exact`, `actor_level`, `platforms`, `product_type_if_explicit`, `metric_type`, `metric_value_raw`, `metric_unit`, `time_scope_raw`, `time_scope_normalized_if_safe`, `geography_if_explicit`, `evidence_role`, `local_qualifiers[]`, `uncertainties[]`, `traceability_pointers[]`, `normalization_notes[]`, `extraction_notes[]` — schema líneas 8–31 |
| Patrón de signal_id | `^SC-R\d+-\d+$` p.ej. `SC-R1-001` (schema líneas 33–37) |
| `signal_type` enum (12) | `policy_signal`, `pricing_signal`, `availability_signal`, `seller_outcome_signal`, `buyer_experience_signal`, `discoverability_signal`, `traffic_signal`, `requirement_signal`, `review_signal`, `refund_signal`, `comparative_local_signal`, `unknown` — schema líneas 68–83 |

#### Gates de validación

**Gate 3 — Signal Extraction Validator**

| Campo | Detalle |
|-------|---------|
| Validador | `upstream/signal-extraction/contracts/signal_extraction_validator.md` |
| Checks (11) | `observational_wording`, `subject_exact`, `actor_level`, `time_scope`, `qualifiers`, `evidence_role`, `single_claim_discreteness`, `no_cross_source_meta_observation`, `traceability`, `no_tension_smuggling`, `notes_locality` |
| Statuses (4) | `pass`, `pass_with_flags`, `rework`, `reject` |
| Failure codes (19) | `signal_not_observational`, `downstream_interpretation_smuggled`, `subject_exact_lost`, `actor_level_collapsed`, `platform_vs_seller_level_collapsed`, `time_scope_dropped`, `normalized_time_unsafe`, `current_vs_historical_ambiguity`, `qualifier_dropped`, `context_promoted_to_signal`, `evidence_role_unclear`, `multiple_records_fused_unsafely`, `local_claim_boundary_broken`, `insufficient_discreteness`, `cross_source_meta_observation`, `traceability_weakened`, `checkout_vs_payout_collapsed`, `net_vs_gross_collapsed`, `notes_interpretive_content` — schema líneas 96–116 |
| Destino de rejects/rework | Path no especificado |
| Schema de resultado | `upstream/signal-extraction/schemas/signal_validation.schema.json` |

**Gate 4 — Signal-to-Inventory Entry Gate**

| Campo | Detalle |
|-------|---------|
| Contrato | `upstream/signal-extraction/contracts/signal_to_inventory_entry_gate.md` |
| Checks (8) | `validation_status_check`, `discreteness_check`, `observational_boundary_check`, `subject_exactness_check`, `actor_level_check`, `time_and_qualifier_check`, `cross_source_contamination_check`, `pattern_readiness_check` |
| Routing decisions (4) | `pass_to_inventory_mapping`, `preserve_as_isolated_signal`, `return_to_signal_rework`, `reject_from_inventory_input` |
| Failure reasons | Contrato lista 11 (líneas 278–292); schema lista 14 — divergencia declarada en Sección 5 |
| Artefactos opcionales | `entry_gate_report.json`, `isolated_signals.json`, `rework_queue.json`, `rejected_signals.json` — paths no especificados en contrato ni schema |
| Schema de resultado | `upstream/signal-extraction/schemas/signal_inventory_gate.schema.json` |

#### Campos de juicio humano

`signal_text`, `subject_exact`, `actor_level`, `normalization_notes`, `extraction_notes` requieren juicio humano. `source_record_ids`, `source_ids`, `traceability_pointers`, `metric_value_raw`, `time_scope_raw` se derivan de los Extraction Records de entrada.

---

## Sección 3 — Tabla resumen de gates

| # | Fase | Gate | Contrato | Checks | Statuses posibles | Failure codes | Destino de rejects | Destino de rework |
|---|------|------|----------|--------|-------------------|---------------|--------------------|-------------------|
| 1 | 1a | Source Intake Validator | `upstream/source-intake/contracts/source_intake_validator.md` | 9 | pass, pass_with_flags, rework, parking_lot, reject | 14 (`source_intake_validation.schema.json` líneas 71–86) | No especificado en contrato | No especificado en contrato |
| 2 | 1b | Data Extraction Validator | `upstream/data-extraction/contracts/data_extraction_validator.md` | 13 | pass, pass_with_flags, rework, reject *(sin parking_lot)* | Schema: 20; Contrato: 19 (`data_extraction_validator.schema.json` líneas 79–99) | `working/data_extraction/rejected_archive/validator/` (INFERIDO) | No especificado en contrato |
| 3 | 2 | Signal Extraction Validator | `upstream/signal-extraction/contracts/signal_extraction_validator.md` | 11 | pass, pass_with_flags, rework, reject | 19 (`signal_validation.schema.json` líneas 96–116) | No especificado | No especificado |
| 4 | 2 | Signal-to-Inventory Entry Gate | `upstream/signal-extraction/contracts/signal_to_inventory_entry_gate.md` | 8 | pass_to_inventory_mapping, preserve_as_isolated_signal, return_to_signal_rework, reject_from_inventory_input | Schema: 14 / Contrato: 11 *(divergencia — ver Sección 5)* | `rejected_signals.json` — PATH NO ESPECIFICADO | `rework_queue.json` — PATH NO ESPECIFICADO |
| 5 | IM | IM Entry Gate | `modules/01_entry_gate.md` | 5 | pass / fail (pipeline se detiene en fail) | No enumerados — se reportan card IDs específicos | Pipeline se detiene; IDs y violaciones reportados en `working/entry_gate/entry_gate_report.json` | N/A — no hay rework, solo pass o halt |

**Nota:** El Gate 1 (Source Intake) es el único que incluye `parking_lot` como status. Los Gates 2, 3 y 4 usan únicamente 4 statuses. El Gate 5 (IM Entry Gate) opera en modo binario: pass o fail total del pipeline.

---

## Sección 4 — Tabla resumen de inputs y outputs por fase

| Fase | Input (formato + path) | Output (formato + path) | Validador (schema) |
|------|------------------------|-------------------------|--------------------|
| 0 — DG Parsing | Markdown 4-partes · `input/data_gathering/shards/{deep_search,gpt_custom}/*.md` | JSON findings · `working/data_gathering/findings/<shard_id>__<finding_id>.json` | Ninguno — warnings a stderr únicamente |
| 0 — Part 4 Diagnostics | (mismos shards) | JSON · `working/data_gathering/diagnostics/part_4/<shard_id>__<item_id>.json` | Ninguno |
| 0 — QA Notes | (mismos shards) | JSON · `working/data_gathering/diagnostics/qa_notes/<shard_id>_qa.json` | Ninguno |
| 1a — Source Intake | JSON findings (Part 1+2) · `working/data_gathering/findings/*.json` | JSON Source Packets · `working/source_intake/packets/<packet_id>.json` | `upstream/source-intake/schemas/source_intake_validation.schema.json` |
| 1b — Data Extraction | JSON Source Packets (pass/pass_with_flags) · `working/source_intake/packets/*.json` | JSON Extraction Records · `working/data_extraction/` **PATH INFERIDO** | `upstream/data-extraction/schemas/data_extraction_validator.schema.json` |
| 1b — Notes Scrubbing | Notas interpretivas en `parser_notes` | JSONL · `working/notes_scrubbing/scrubbing_log.jsonl` *(directorio no existe actualmente)* | Ninguno |
| 2 — Signal Extraction | JSON Extraction Records (pass/pass_with_flags) · path inferido | JSON Signal Cards · **PATH NO ESPECIFICADO** | `upstream/signal-extraction/schemas/signal_validation.schema.json` |
| 2 — SI-IM Entry Gate | JSON Signal Cards + resultados de validación | JSON gate records · paths no especificados (opcional: `entry_gate_report.json`, `isolated_signals.json`, `rework_queue.json`, `rejected_signals.json`) | `upstream/signal-extraction/schemas/signal_inventory_gate.schema.json` |
| 2 — Notes Scrubbing | Notas interpretivas en `normalization_notes` / `extraction_notes` | JSONL · `working/notes_scrubbing/scrubbing_log.jsonl` *(directorio no existe actualmente)* | Ninguno |
| IM — Entry Gate | Markdown Signal Cards · `input/signal_cards_round_*.md` (10 archivos, 1,560 cards) *(archivos no existen actualmente)* | JSON report · `working/entry_gate/entry_gate_report.json` | No enumerado en `modules/01_entry_gate.md` |

**Estado actual del pipeline (2026-04-08):**
- Phase 0: completa (28 findings, 13 Part-4, 3 QA files)
- Phase 1a en adelante: no iniciadas (`working/source_intake/packets/` vacío)

---

## Sección 5 — Lo que no pudiste mapear

### Gaps entre contrato y código, o entre fases

**1. Conversión JSON → Markdown no documentada.**
Signal Extraction produce Signal Cards en formato JSON (schema: `upstream/signal-extraction/schemas/signal_card.schema.json`). Inventory Mapping Entry Gate consume `input/signal_cards_round_*.md` en formato Markdown (`modules/01_entry_gate.md` línea 9). No existe contrato, script, ni proceso documentado en ningún archivo del repo que defina esta conversión de formato. Los archivos `input/signal_cards_round_*.md` no existen actualmente.

**2. Path de output de Signal Extraction no especificado.**
`upstream/signal-extraction/contracts/signal_extraction_contract.md` y `upstream/signal-extraction/schemas/signal_card.schema.json` no nombran ningún path de filesystem para el output de Signal Cards. No existe directorio `working/signal_extraction/` en el repo.

**3. Path de output de Data Extraction no especificado.**
`upstream/data-extraction/contracts/data_extraction_contract.md` no declara dónde se escriben los Extraction Records. El directorio `working/data_extraction/` existe pero contiene únicamente `rejected_archive/` (vacío). El path se infiere de la estructura de directorios, no de un contrato.

**4. Paths de destino para rework/parking_lot/reject en Source Intake no especificados.**
`upstream/source-intake/contracts/source_intake_validator.md` describe las disposiciones `rework`, `parking_lot` y `reject` conceptualmente pero no nombra ningún path de filesystem para sus artefactos. No se define ningún archivo de rework queue.

**5. Paths de destino para rework/reject en Data Extraction no especificados.**
`upstream/data-extraction/contracts/data_extraction_validator.md` describe las disposiciones sin especificar paths de output. `working/data_extraction/rejected_archive/extraction/` y `working/data_extraction/rejected_archive/validator/` existen vacíos — convención inferida, no declarada.

**6. Paths de artefactos opcionales del Signal-to-IM Entry Gate no especificados.**
`upstream/signal-extraction/contracts/signal_to_inventory_entry_gate.md` Sección 3 lista cuatro artefactos opcionales (`entry_gate_report.json`, `isolated_signals.json`, `rework_queue.json`, `rejected_signals.json`) sin asignarles ningún path de filesystem.

**7. Directorio de notes scrubbing no existe.**
Tanto `upstream/data-extraction/contracts/data_extraction_validator.md` (líneas 406–415) como `upstream/signal-extraction/contracts/signal_extraction_validator.md` (líneas 354–363) requieren que el scrubbing de notas interpretivas produzca logs en `working/notes_scrubbing/scrubbing_log.jsonl`. Ese directorio no existe en el repo actual.

**8. Divergencia entre contrato y schema en Data Extraction — count de campos.**
`upstream/data-extraction/contracts/data_extraction_contract.md` Sección 6 lista 25 campos para el Extraction Record. `upstream/data-extraction/schemas/data_extraction_record.schema.json` líneas 8–37 requiere 28 campos en `required[]`. Los campos `source_packet_id` y `signal_type` aparecen en el schema `required[]` pero están ausentes de la lista del contrato. No existe nota de reconciliación.

**9. Divergencia entre contrato y schema en Signal-to-IM Gate — count de failure reasons.**
`upstream/signal-extraction/contracts/signal_to_inventory_entry_gate.md` Sección 7 (líneas 278–292) enumera 11 failure reasons. `upstream/signal-extraction/schemas/signal_inventory_gate.schema.json` líneas 94–109 enumera 14 — los valores adicionales aparecen en el schema pero están ausentes de la sección de failure reasons del contrato.

**10. Part 3 (Pattern candidates) — handling downstream no declarado.**
Los shards producen Part 3 (pattern candidates, sellado). El contrato `reference/research_directions_protocol.md` línea 85 dice que Part 3 está sellado y no se parsea. Ningún contrato del pipeline downstream (Source Intake, Data Extraction, Signal Extraction) menciona qué ocurre con el contenido de Part 3. No existe proceso ni artefacto documentado para este material.

### Archivos activos en el repo no incluidos en la lista de referencia

**11. `section1_flow_map.md`**
Archivo de arquitectura en español ubicado en la raíz del repo. Cubre el pipeline interno de Inventory Mapping (Módulos 01–06), no el pipeline upstream. Contiene datos de ejecución específicos (referencia a 74 TCs, 1,561 cards — diverge de `modules/01_entry_gate.md` línea 9 que declara 1,560 cards). No está referenciado en ningún índice ni instrucción de referencia del repo.

**12. `reference/TC-001.md`**
Archivo en el directorio `reference/` no incluido en la lista de referencia proporcionada. Su nombre sugiere un test case o contrato. No fue leído para este mapeo.

**13. `reference/protocol_canonical.md`**
Mencionado en `CLAUDE.md` como la fuente autoritativa máxima del proyecto. No incluido en la lista de referencia de la tarea. No fue leído para este mapeo.

**14. `working/data_gathering/diagnostics/qa_notes/policy_etsy_fees_v1_qa.json` y `reddit_buyer_pain_planners_v1_qa.json`**
Archivos de output QA activos para los dos shards `gpt_custom`. No están referenciados en ningún contrato ni instrucción de pipeline.

**15. `working/data_extraction/rejected_archive/extraction/` y `working/data_extraction/rejected_archive/validator/`**
Directorios vacíos cuya convención de nombres implica una ruta de almacenamiento para artefactos rechazados de Data Extraction, pero esta ruta no está declarada en ningún contrato.

**16. `working/source_intake/rejected_archive/`**
Directorio vacío con la misma observación: convención de naming no declarada en contrato de Source Intake.

### Ambigüedades sin resolver

**17. Ausencia de Part 4 en shards gpt_custom.**
Los 13 archivos en `working/data_gathering/diagnostics/part_4/` provienen únicamente de `DX-2_gumroad_v2` (deep_search). Los dos shards gpt_custom (`policy_etsy_fees_v1`, `reddit_buyer_pain_planners_v1`) no tienen archivos Part-4 ni Part-2 en `working/`. Si esto refleja el contenido de los shards (todos sus findings son `direct_verified`) o un comportamiento del parser no puede determinarse sin leer los archivos fuente directamente.

**18. Discrepancia en conteo de cards entre `section1_flow_map.md` y `modules/01_entry_gate.md`.**
`modules/01_entry_gate.md` línea 9 declara "1,560 cards expected". `section1_flow_map.md` línea 5 (archivo activo no en lista de referencia) menciona 1,561 cards. La fuente autoritativa según `CLAUDE.md` es `modules/*.md`, por lo que 1,560 es el valor canónico — pero la discrepancia se registra sin resolverla.
