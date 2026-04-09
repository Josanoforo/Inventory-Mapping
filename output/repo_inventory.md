# Repo Inventory — 2026-04-09

---

## 1. Estructura de carpetas (primer y segundo nivel)

```
/home/user/Inventory-Mapping/
├── .claude/
│   ├── agents/
│   └── skills/
│       ├── build-candidate/
│       ├── entry-gate/
│       ├── index-cards/
│       ├── scan-asymmetries/
│       ├── scan-co-occurrences/
│       ├── scan-contradictions/
│       ├── scan-frictions/
│       ├── scan-gaps/
│       ├── scan-lexical-overlap/
│       ├── scan-opposite-directions/
│       ├── split-cards/
│       └── validate-candidate/
├── input/
│   └── data_gathering/
│       └── shards/
│           ├── deep_search/
│           └── gpt_custom/
├── modules/
├── output/
├── reference/
├── schemas/
├── scripts/
├── upstream/
│   ├── data-extraction/
│   │   ├── contracts/
│   │   └── schemas/
│   ├── signal-extraction/
│   │   ├── contracts/
│   │   └── schemas/
│   └── source-intake/
│       ├── contracts/
│       └── schemas/
└── working/
    ├── data_extraction/
    │   └── rejected_archive/
    │       ├── extraction/
    │       └── validator/
    ├── data_gathering/
    │   ├── diagnostics/
    │   │   ├── part_4/
    │   │   └── qa_notes/
    │   └── findings/
    └── source_intake/
        ├── packets/
        └── rejected_archive/
```

---

## 2. Archivos .json — path completo y propósito aparente

schemas/card_record.schema.json — Schema JSON: CardRecord — una línea de card_index.jsonl (signal card indexada)
schemas/index_manifest.schema.json — Schema JSON: IndexManifest — rastrea progreso de indexación de card batches
schemas/scan_artifact.schema.json — Schema JSON: ScanArtifact — output de una operación de escaneo mecánico
schemas/split_manifest.schema.json — Schema JSON: SplitManifest — rastrea progreso de splitting de archivos round en card batches
schemas/tension_candidate.schema.json — Schema JSON: TensionCandidate — candidato de tensión producido por candidate builder
schemas/validation_report.schema.json — Schema JSON: ValidationReport — resultado de validar un tension candidate

upstream/data-extraction/schemas/data_extraction_record.schema.json — Schema JSON: Data Extraction Record — schema canónico de un registro de extracción
upstream/data-extraction/schemas/data_extraction_validator.schema.json — Schema JSON: Data Extraction Validation Result — resultado de validación de un Data Extraction Record
upstream/signal-extraction/schemas/signal_card.schema.json — Schema JSON: Signal Card — schema canónico de una Signal Card producida por Signal Extraction
upstream/signal-extraction/schemas/signal_inventory_gate.schema.json — Schema JSON: Signal to Inventory Gate Result — resultado del entry-gate al pasar de Signal Extraction a Inventory Mapping
upstream/signal-extraction/schemas/signal_validation.schema.json — Schema JSON: Signal Validation Result — resultado de validación de una Signal Card
upstream/source-intake/schemas/source_intake_validation.schema.json — Schema JSON: Source Intake Validation Result — resultado de validación de un Source Packet
upstream/source-intake/schemas/source_packet.schema.json — Schema JSON: Source Packet — schema canónico de un source-local packet producido por Source Intake

---

## 3. Archivos .md en carpetas específicas — path completo y título H1

### reference/

reference/protocol_canonical.md — # Inventory Mapping — Canonical Protocol
reference/source_packet_conversion_template.md — # Source Packet conversion template
reference/TC-001.md — ### Tension Candidate TC-001  (no tiene H1, usa H3)
reference/data_gathering_project_instructions_v4_5.md — # Project Instructions — Data Gathering (v4.5)
reference/research_directions_protocol.md — # Research Directions Protocol

### modules/

modules/01_entry_gate.md — # Module 01 — Entry Gate
modules/02_splitter.md — # Module 02 — Splitter
modules/03_indexer.md — # Module 03 — Indexer
modules/04_scanner.md — Module 04 — Scanner  (primera línea, sin marcador #)
modules/05_candidate_builder.md — Module 05 — Candidate Builder  (primera línea, sin marcador #)
modules/06_validator.md — Module 06 — Validator  (primera línea, sin marcador #)

### upstream/

upstream/data-extraction/contracts/data_extraction_contract.md — # Data Extraction Contract v0.1
upstream/data-extraction/contracts/data_extraction_validator.md — # Data Extraction Validator
upstream/signal-extraction/contracts/signal_extraction_contract.md — # Signal Extraction Contract v0.1
upstream/signal-extraction/contracts/signal_to_inventory_entry_gate.md — # Signal to Inventory Entry Gate
upstream/signal-extraction/contracts/signal_extraction_validator.md — # Signal Extraction Validator
upstream/source-intake/contracts/source_intake_contract.md — # Source Intake Contract v0.1
upstream/source-intake/contracts/source_intake_validator.md — # Source Intake Validator

### schemas/

No hay archivos .md en schemas/.

### .claude/

.claude/agents/inventory-mapping.md — (frontmatter YAML, sin H1; name: inventory-mapping)
.claude/skills/build-candidate/SKILL.md — Build Candidate — Skill  (primera línea, sin marcador #)
.claude/skills/entry-gate/SKILL.md — # Entry Gate — Skill
.claude/skills/index-cards/SKILL.md — # Index Cards — Skill
.claude/skills/scan-asymmetries/SKILL.md — # Scan Asymmetries — Skill
.claude/skills/scan-co-occurrences/SKILL.md — # Scan Co-occurrences — Skill
.claude/skills/scan-contradictions/SKILL.md — # Scan Contradictions — Skill
.claude/skills/scan-frictions/SKILL.md — # Scan Frictions — Skill
.claude/skills/scan-gaps/SKILL.md — # Scan Gaps — Skill
.claude/skills/scan-lexical-overlap/SKILL.md — Scan Lexical Overlap — Skill  (primera línea, sin marcador #)
.claude/skills/scan-opposite-directions/SKILL.md — # Scan Opposite Directions — Skill
.claude/skills/split-cards/SKILL.md — # Split Cards — Skill
.claude/skills/validate-candidate/SKILL.md — Validate Candidate — Skill  (primera línea, sin marcador #)

### contracts/ (standalone)

No hay carpeta contracts/ de primer nivel. Los contracts están bajo upstream/*/contracts/.

---

## 4. Búsqueda de archivos específicos

FOUND: upstream/source-intake/schemas/source_packet.schema.json
FOUND: upstream/source-intake/contracts/source_intake_contract.md
FOUND: upstream/data-extraction/schemas/data_extraction_record.schema.json
FOUND: upstream/data-extraction/contracts/data_extraction_contract.md
FOUND: upstream/signal-extraction/schemas/signal_card.schema.json
FOUND: upstream/signal-extraction/contracts/signal_extraction_contract.md
FOUND: upstream/signal-extraction/schemas/signal_inventory_gate.schema.json
FOUND: reference/source_packet_conversion_template.md
FOUND: reference/protocol_canonical.md

---

## 5. Detalle de archivos encontrados en tarea 4

### upstream/source-intake/schemas/source_packet.schema.json
- path: upstream/source-intake/schemas/source_packet.schema.json
- líneas: 296
- propiedades de primer nivel del objeto raíz: $schema, $id, title, description, type, additionalProperties, required, properties, $defs
- propiedades del dominio (bajo "properties"): packet_id, source_id, source_title, source_type, source_ref, source_date_if_available, author_or_actor_if_available, retrieval_method, retrieved_from, raw_search_context, snippets, possible_subjects, possible_actor_levels, possible_metric_types, possible_time_scopes, possible_geographies, uncertainties, priority_for_source_first, intake_notes, traceability_status

### upstream/source-intake/contracts/source_intake_contract.md
- path: upstream/source-intake/contracts/source_intake_contract.md
- líneas: 424
- headers H2 en orden:
  ## 1. Purpose
  ## 2. Inputs
  ## 3. Output
  ## 4. Qué sí hace
  ## 5. Qué no hace
  ## 6. Canonical Output Schema (conceptual)
  ## 7. Field Definitions
  ## 8. Quality Rules
  ## 9. Validation Checklist
  ## 10. Failure Reasons
  ## 11. Parking Lot Boundary
  ## 12. Priority Rules for Source-First
  ## 13. Success Criterion
  ## 14. Human Audit Questions
  ## 15. Minimal Example

### upstream/data-extraction/schemas/data_extraction_record.schema.json
- path: upstream/data-extraction/schemas/data_extraction_record.schema.json
- líneas: 390
- propiedades de primer nivel del objeto raíz: $schema, $id, title, description, type, additionalProperties, required, properties
- propiedades del dominio (bajo "properties"): extraction_id, source_packet_id, source_id, source_type, source_title, source_ref, source_date_if_available, author_or_actor_if_available, snippet_primary, snippet_context_before, snippet_context_after, claim_type, subject_exact, actor_level, platforms, product_type_if_explicit, metric_type, metric_value_raw, metric_unit, time_scope_raw, time_scope_normalized_if_safe, geography_if_explicit, evidence_role, local_qualifiers, uncertainties, parser_notes, traceability_pointer

### upstream/data-extraction/contracts/data_extraction_contract.md
- path: upstream/data-extraction/contracts/data_extraction_contract.md
- líneas: 485
- headers H2 en orden:
  ## 1. Purpose
  ## 2. Inputs
  ## 3. Output
  ## 4. Qué sí hace
  ## 5. Qué no hace
  ## 6. Canonical Output Schema
  ## 7. Field Definitions
  ## 8. Allowed Operations
  ## 9. Forbidden Operations
  ## 10. Extraction Quality Rules
  ## 11. Validation Checklist
  ## 12. Failure Reasons
  ## 13. Failure Taxonomy to Track
  ## 14. Upstream / Downstream Boundaries
  ## 15. Minimal Example
  ## 16. Decision Boundary
  ## 17. Success Criterion
  ## 18. Human Audit Questions

### upstream/signal-extraction/schemas/signal_card.schema.json
- path: upstream/signal-extraction/schemas/signal_card.schema.json
- líneas: 353
- propiedades de primer nivel del objeto raíz: $schema, $id, title, description, type, additionalProperties, required, properties, $defs
- propiedades del dominio (bajo "properties"): signal_id, source_record_ids, source_ids, round, signal_text, subject_exact, actor_level, platforms, product_type_if_explicit, metric_type, metric_value_raw, metric_unit, time_scope_raw, time_scope_normalized_if_safe, geography_if_explicit, evidence_role, local_qualifiers, uncertainties, traceability_pointers, normalization_notes, extraction_notes

### upstream/signal-extraction/contracts/signal_extraction_contract.md
- path: upstream/signal-extraction/contracts/signal_extraction_contract.md
- líneas: 356
- headers H2 en orden:
  ## 1. Purpose
  ## 2. Inputs
  ## 3. Output
  ## 4. Qué sí hace
  ## 5. Qué no hace
  ## 6. Canonical Output Schema (conceptual)
  ## 7. Signal Card principles
  ## 9. Decision boundary
  ## 10. Qué sí puede fusionar y qué no
  ## 11. Validation Checklist
  ## 12. Failure reasons
  ## 13. Quality rules
  ## 14. Handoff to Inventory Mapping
  ## 15. Success criterion
  ## 16. Human audit questions
  ## 17. Minimal examples
  ## 18. Global rule

### upstream/signal-extraction/schemas/signal_inventory_gate.schema.json
- path: upstream/signal-extraction/schemas/signal_inventory_gate.schema.json
- líneas: 176
- propiedades de primer nivel del objeto raíz: $schema, $id, title, description, type, additionalProperties, required, properties, $defs
- propiedades del dominio (bajo "properties"): gate_id, signal_id, gate_version, validation_status, entry_gate_decision, checks, failure_reasons, notes, rework_instructions, isolated_signal_reason, gated_at, gated_by

### reference/source_packet_conversion_template.md
- path: reference/source_packet_conversion_template.md
- líneas: 301
- headers H2 en orden:
  ## Qué es esto
  ## El workflow de conversión
  ## El template
  ## Field-by-field guidance — los 8 campos de juicio
  ## Fallback rules
  ## Worked example — DX-1 Finding 1 (Devrim Ozcay)
  ## Sidebar — workflow findings (caso DX-2)
  ## Convenciones de IDs sugeridas
  ## Tiempo estimado

### reference/protocol_canonical.md
- path: reference/protocol_canonical.md
- líneas: 119
- headers H2 en orden:
  ## What you do
  ## Mechanical operations allowed
  ## Not allowed
  ## Candidate Generation Rules
  ## Rules for Signal IDs
  ## Rules for Polos
  ## Rules for Type
  ## Allowed mechanical verbs
  ## Forbidden language
  ## Self-check before delivering any candidate
  ## What you never do

---

## 6. Archivos en input/

input/dg6_etsy_fees.md — 868 líneas — primera línea: # Etsy Platform Fees — Data Gathering Research Pack
input/dg7_gumroad_dx2.md — 207 líneas — primera línea: # Research Shard: Gumroad × DX-2 — AI-Assisted Production Workflows for Digital Products
input/data_gathering/shards/.gitkeep — 0 líneas — (archivo vacío, placeholder de directorio)
input/data_gathering/shards/deep_search/.gitkeep — 0 líneas — (archivo vacío, placeholder de directorio)
input/data_gathering/shards/gpt_custom/.gitkeep — 0 líneas — (archivo vacío, placeholder de directorio)

---

## 7. Directorios especiales — existencia y contenido inmediato

### working/
EXISTE.
Contenido inmediato: data_extraction/, data_gathering/, source_intake/

  working/data_extraction/
    rejected_archive/
      extraction/  — contiene .gitkeep
      validator/   — contiene .gitkeep

  working/data_gathering/
    diagnostics/
      part_4/    — contiene .gitkeep
      qa_notes/  — contiene .gitkeep
    findings/    — contiene .gitkeep

  working/source_intake/
    packets/          — contiene .gitkeep
    rejected_archive/ — contiene .gitkeep

Todos los subdirectorios contienen solo archivos .gitkeep (vacíos). No hay datos de trabajo activos.

### output/
EXISTE. Vacío (sin archivos ni subdirectorios, excepto este reporte en curso).

### scripts/
EXISTE.
Contenido: parse_dg_shard.py — 495 líneas — parse_dg_shard.py — Data Gathering shard parser (script Python)

### .claude/skills/
EXISTE.
Contenido (subdirectorios, uno por skill):
  build-candidate/
  entry-gate/
  index-cards/
  scan-asymmetries/
  scan-co-occurrences/
  scan-contradictions/
  scan-frictions/
  scan-gaps/
  scan-lexical-overlap/
  scan-opposite-directions/
  split-cards/
  validate-candidate/

Cada subdirectorio contiene un archivo SKILL.md.

### .claude/agents/
EXISTE.
Contenido: inventory-mapping.md — agente con frontmatter YAML (name: inventory-mapping, tools: Read/Write/Edit/Bash/Grep/Glob, model: sonnet). Descripción: runs the Inventory Mapping pipeline over Signal Cards.
