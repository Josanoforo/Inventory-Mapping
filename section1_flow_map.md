# Sección 1 — Mapa de flujo
## Upstream Pipeline Map Part 1: Phase 0 → Phase 2 Signal Extraction

---

## Nota estructural previa

Este repo contiene dos pipelines que conviven y tienen puntos de entrada
distintos al mismo destino (Inventory Mapping). El mapa los distingue explícitamente
porque confundirlos genera errores de interpretación sobre qué está implementado.

- **Pipeline A (Legacy)**: produjo las 1,561 Signal Cards que viven en `input/`.
  El proceso que las generó no está documentado en este repo.
- **Pipeline B (Upstream nuevo)**: definido en `upstream/` con contratos y schemas.
  Solo Phase 0 tiene automatización. Source Intake, Data Extraction y Signal Extraction
  tienen contratos y schemas pero ningún script de ejecución.

El mapa cubre Pipeline B de punta a punta, y señala dónde se conecta con Pipeline A.

---

## Diagrama principal — Pipeline B (nuevo upstream)

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  PHASE 0 — DATA GATHERING                                                  ║
║  Contrato: reference/data_gathering_project_instructions_v4_5.md           ║
║            reference/research_directions_protocol.md                       ║
╚══════════════════════════════════════════════════════════════════════════════╝

  [Entrada manual — uploads del operador]
        │
        │  Shards .md depositados en:
        │    input/data_gathering/shards/deep_search/<shard>.md
        │    input/data_gathering/shards/gpt_custom/<shard>.md
        │
        ▼
  ┌─────────────────────────────────────────────────────────────┐
  │  scripts/parse_dg_shard.py                                  │
  │  - Lee el archivo shard desde el path dado                  │
  │  - Determina source_tool desde el nombre del directorio     │
  │    padre (deep_search | gpt_custom | → "unknown" + warning) │
  │  - Parsea las 4 partes del shard + sección QA Notes         │
  │  - Extrae 8 campos requeridos por Rule 4 del contrato       │
  └──────────────┬──────────────────────────────────────────────┘
                 │
        ┌────────┴───────────────────────────────────────────────┐
        │                                                         │
        ▼                                                         ▼
  Part 1 + Part 2 findings                          Part 4 + QA Notes
  (direct_verified + provisional)                   (could_not_verify)
        │                                                         │
        ▼                                                         ▼
  working/data_gathering/findings/            working/data_gathering/diagnostics/
    <shard_id>__<finding_id>.json               part_4/<shard_id>__<item_id>.json
    (un archivo JSON por finding)               qa_notes/<shard_id>_qa.json
        │
        │  [Punto de retención — decisión humana requerida]
        │  Part 2 (provisional/blocked_url) NO pasa downstream
        │  automáticamente. Requiere disposición humana:
        │    → Promote to Clean
        │    → Quarantine (default si no se resuelve)
        │    → Downgrade to could_not_verify
        │
        │  Solo findings con verification_status = direct_verified
        │  pasan a Source Intake sin acción manual.


╔══════════════════════════════════════════════════════════════════════════════╗
║  PHASE 1 — SOURCE INTAKE                                                   ║
║  Contrato:   upstream/source-intake/contracts/source_intake_contract.md    ║
║  Validador:  upstream/source-intake/contracts/source_intake_validator.md   ║
║  Schema:     upstream/source-intake/schemas/source_packet.schema.json      ║
╚══════════════════════════════════════════════════════════════════════════════╝

        │
        │  Entrada: findings de working/data_gathering/findings/
        │           (solo Part 1 direct_verified, o Part 2 promovidos)
        │
        ▼
  ┌─────────────────────────────────────────────────────────────┐
  │  [proceso no identificado]                                  │
  │  Guía de conversión manual disponible en:                   │
  │  reference/source_packet_conversion_template.md             │
  │                                                             │
  │  Operación declarada: múltiples findings de la misma URL    │
  │  se colapsan en un solo Source Packet con múltiples         │
  │  snippets. 50 findings → ~30-40 packets.                    │
  └──────────────┬──────────────────────────────────────────────┘
                 │
        ┌────────┴──────────────────────────────┐
        │                                        │
        ▼                                        ▼
  [proceso no identificado]              Packets con problemas
  Source Packet Validator                       │
  (definido en contrato,                        │
   no automatizado)                    ┌────────▼──────────────┐
        │                              │  Parking Lot          │
        │                              │  (recuperables con    │
        │                              │   follow-up acotado)  │
        │                              └───────────────────────┘
        │
  ┌─────┴──────────────────────┐
  │  Statuses posibles:        │
  │  pass                      │
  │  pass_with_flags           │──────────────────────────────────────────────┐
  │  rework → regresa al       │                                              │
  │           productor        │                                              │
  │  parking_lot (ver arriba)  │                                              │
  │  reject                    ├──────────────────────────────────────────────┘
  └─────┬──────────────────────┘
        │  pass | pass_with_flags
        ▼
  working/source_intake/packets/       ← VACÍO al momento de esta revisión
    <packet_id>.json                      (solo .gitkeep)
        │
  working/source_intake/rejected_archive/   ← rejects y reworks finales
                                              VACÍO al momento de esta revisión


╔══════════════════════════════════════════════════════════════════════════════╗
║  PHASE 1 — DATA EXTRACTION                                                 ║
║  Contrato:  upstream/data-extraction/contracts/data_extraction_contract.md ║
║  Validador: upstream/data-extraction/contracts/data_extraction_validator.md║
║  Schema:    upstream/data-extraction/schemas/                               ║
╚══════════════════════════════════════════════════════════════════════════════╝

        │
        │  Entrada: Source Packets con validation_status = pass | pass_with_flags
        │
        ▼
  ┌─────────────────────────────────────────────────────────────┐
  │  [proceso no identificado]                                  │
  │  No hay script. Operación declarada:                        │
  │  segmentar cada Source Packet en Extraction Records         │
  │  (un record por claim localmente coherente)                 │
  └──────────────┬──────────────────────────────────────────────┘
                 │
        ┌────────┴──────────────────────────────┐
        │                                        │
        ▼                                        ▼
  [proceso no identificado]              Records con problemas
  Data Extraction Validator                     │
  (definido en contrato,                working/data_extraction/
   no automatizado)                     rejected_archive/
        │                               extraction/   ← VACÍO
        │                               validator/    ← VACÍO
        │
        │  [Paso intermedio declarado en validador:]
        │  Si notes_locality falla → scrubbing obligatorio de
        │  parser_notes antes de pasar a Signal Extraction.
        │  Log en: working/notes_scrubbing/scrubbing_log.jsonl
        │  [directorio no encontrado en repo actual]
        │
  ┌─────┴──────────────────────┐
  │  Statuses posibles:        │
  │  pass                      │
  │  pass_with_flags           │
  │  rework → regresa          │
  │  reject                    │
  └─────┬──────────────────────┘
        │  pass | pass_with_flags (+ rework corregido y revalidado)
        ▼
  [directorio de Extraction Records no identificado en repo]
  Los records validados no tienen ubicación working/ explícita
  en la implementación actual.


╔══════════════════════════════════════════════════════════════════════════════╗
║  PHASE 2 — SIGNAL EXTRACTION                                               ║
║  Contrato:   upstream/signal-extraction/contracts/signal_extraction_contract.md  ║
║  Validador:  upstream/signal-extraction/contracts/signal_extraction_validator.md ║
║  Entry Gate: upstream/signal-extraction/contracts/signal_to_inventory_entry_gate.md ║
║  Schema:     upstream/signal-extraction/schemas/signal_card.schema.json    ║
╚══════════════════════════════════════════════════════════════════════════════╝

        │
        │  Entrada: Extraction Records con
        │           validation_status = pass | pass_with_flags
        │           (rework aceptado solo si hubo corrección + revalidación)
        │
        ▼
  ┌─────────────────────────────────────────────────────────────┐
  │  [proceso no identificado]                                  │
  │  No hay script. Operación declarada:                        │
  │  convertir cada Extraction Record en Signal Card            │
  │  observacional, discreta y trazable.                        │
  └──────────────┬──────────────────────────────────────────────┘
                 │
        ┌────────┴──────────────────────────────┐
        │                                        │
        ▼                                        ▼
  [proceso no identificado]              Cards con problemas
  Signal Extraction Validator
  (definido en contrato,
   no automatizado)
        │
        │  [Paso intermedio declarado en validador:]
        │  Si notes_locality falla → scrubbing obligatorio de
        │  normalization_notes y extraction_notes.
        │  Log en: working/notes_scrubbing/scrubbing_log.jsonl
        │  [directorio no encontrado en repo actual]
        │
  ┌─────┴──────────────────────┐
  │  Statuses posibles:        │
  │  pass                      │
  │  pass_with_flags           │
  │  rework → regresa          │
  │  reject                    │
  └─────┬──────────────────────┘
        │  pass | pass_with_flags
        ▼
  ┌─────────────────────────────────────────────────────────────┐
  │  Signal to Inventory Entry Gate                             │
  │  upstream/signal-extraction/contracts/                      │
  │         signal_to_inventory_entry_gate.md                   │
  │                                                             │
  │  8 checks sobre la Signal Card (discreteness,              │
  │  observational boundary, subject exactness,                 │
  │  actor level, time/qualifier, cross-source,                 │
  │  pattern-readiness, validation status)                      │
  └──────────┬──────────────────────────────────────────────────┘
             │
    ┌────────┼──────────────┬──────────────────────┐
    │        │              │                       │
    ▼        ▼              ▼                       ▼
pass_to_  preserve_as_  return_to_          reject_from_
inventory isolated_     signal_             inventory_
mapping   signal        rework              input

    │
    ▼
════════════════════════════════════════════
  PUNTO FINAL DEL MAPA:
  Signal Cards listas para entrar al Entry Gate de IM
  (en formato signal_card.schema.json)
════════════════════════════════════════════
```

---

## Diagrama complementario — Pipeline A (Legacy) y su conexión con IM

```
  [Proceso externo al repo — blueprints no viven aquí]
        │
        │  Signal Cards producidas antes del rediseño upstream,
        │  bajo enums y criterios distintos al nuevo sistema.
        │
        ▼
  input/signal_cards_round_1.md  ... input/signal_cards_round_10.md
  (1,561 cards en formato legacy: observation, source, date,
   source_type, domain, evidence_base, extraction_status)
        │
        ▼
  ┌─────────────────────────────────────────────────────────────┐
  │  IM Entry Gate (legacy)                                     │
  │  modules/01_entry_gate.md                                   │
  │  .claude/skills/entry-gate/SKILL.md                         │
  │                                                             │
  │  5 checks sobre el formato legacy:                          │
  │  - discrete_cards                                           │
  │  - no_interpretation                                        │
  │  - no_meta_observations                                     │
  │  - evidence_preserved                                       │
  │  - ids_traceable                                            │
  └──────────────┬──────────────────────────────────────────────┘
                 │
                 ▼
  working/entry_gate/entry_gate_report.json
  (status: pass, 1,561 cards, todos los checks passed)
                 │
                 ▼
════════════════════════════════════════════
  Signal Cards legacy entran al pipeline de IM
  (Split → Index → Scanner → Candidate Builder → Validator)
════════════════════════════════════════════
```

---

## Diagrama complementario — Legacy Migration (puente entre pipelines)

```
  working/index/card_index.jsonl
  (1,561 cards indexadas en formato legacy)
        │
        ▼
  ┌─────────────────────────────────────────────────────────────┐
  │  Legacy Signal Card Migration                               │
  │  legacy-migration/contracts/                                │
  │         legacy_signal_card_migration.md                     │
  │  legacy-migration/.claude/skills/                           │
  │         legacy-signal-card-migration/SKILL.md               │
  │                                                             │
  │  Diagnóstico por card: clean_mappable | mappable_with_flags │
  │  | schema_gap | needs_source_recovery | unrecoverable       │
  └──────────────┬──────────────────────────────────────────────┘
                 │
                 ▼
  legacy-migration/working/migrations/
    legacy_signal_card_migrations.jsonl
  (20 de 1,561 cards procesadas al momento de esta revisión)
```

---

## Inventario de transformaciones identificadas

| Transformación | Input | Script/Proceso | Output | Estado |
|---|---|---|---|---|
| DG Shard parsing | `input/data_gathering/shards/**/*.md` | `scripts/parse_dg_shard.py` | `working/data_gathering/findings/*.json` + diagnostics | Implementado |
| Provisional lifecycle resolution | Part 2 findings en `working/data_gathering/findings/` | [proceso no identificado] — decisión humana | findings promovidos / quarantined / downgraded | No automatizado |
| Source Packet conversion | DG findings | [proceso no identificado] — manual con template en `reference/source_packet_conversion_template.md` | `working/source_intake/packets/*.json` | No automatizado — dir vacío |
| Source Packet validation | Source Packets | [proceso no identificado] — contrato en `upstream/source-intake/contracts/source_intake_validator.md` | resultado de validación + rejects en `working/source_intake/rejected_archive/` | No automatizado — dir vacío |
| Data Extraction | Source Packets validados | [proceso no identificado] | Extraction Records (directorio no identificado) | No automatizado — sin output |
| Data Extraction validation + scrubbing | Extraction Records | [proceso no identificado] — contrato en `upstream/data-extraction/contracts/data_extraction_validator.md` | resultados validación + rejects en `working/data_extraction/rejected_archive/` | No automatizado — dir vacío |
| Signal Extraction | Extraction Records validados | [proceso no identificado] | Signal Cards en formato `signal_card.schema.json` | No automatizado — sin output |
| Signal validation + scrubbing | Signal Cards | [proceso no identificado] — contrato en `upstream/signal-extraction/contracts/signal_extraction_validator.md` | resultados validación | No automatizado |
| Signal to IM Entry Gate | Signal Cards + resultados validación | [proceso no identificado] — contrato en `upstream/signal-extraction/contracts/signal_to_inventory_entry_gate.md` | routing decisions | No automatizado |
| IM Entry Gate (legacy) | `input/signal_cards_round_*.md` | `.claude/skills/entry-gate/SKILL.md` ejecutando `modules/01_entry_gate.md` | `working/entry_gate/entry_gate_report.json` | Implementado — ejecutado — passed |

---

## Inventario de reject archives y quarantine points

| Punto | Qué se rechaza | Dónde van los rejects |
|---|---|---|
| DG — Part 2 (provisional) | findings con `verification_status = blocked_url_index_verified` | `working/data_gathering/findings/<shard>__F-P*.json` (no se propagan, se quarantine por default) |
| DG — Part 4 | findings con `verification_status = could_not_verify` | `working/data_gathering/diagnostics/part_4/<shard>__F-X*.json` |
| Source Intake Validator — reject | multiple_sources_fused, cross_source_summary_carried_over, packet_too_cooked_for_extraction | `working/source_intake/rejected_archive/` (vacío) |
| Source Intake Validator — parking_lot | recuperables con follow-up acotado | destino no identificado en implementación actual |
| Data Extraction Validator — reject | source_not_traceable, cross_source_synthesis_smuggled, claim_type_interpretive | `working/data_extraction/rejected_archive/validator/` (vacío) |
| Data Extraction — extracted records reject | record no supera validación | `working/data_extraction/rejected_archive/extraction/` (vacío) |
| Signal Extraction Validator — reject | cross_source_meta_observation, signal_not_observational, traceability_weakened | destino no identificado en implementación actual |
| Signal to IM Entry Gate — reject | reject_from_inventory_input | `rejected_signals.json` (declarado en contrato, no creado) |
| Signal to IM Entry Gate — isolated | preserve_as_isolated_signal | `isolated_signals.json` (declarado en contrato, no creado) |
| Signal to IM Entry Gate — rework | return_to_signal_rework | `rework_queue.json` (declarado en contrato, no creado) |

---

## Punto final del mapa

Signal Cards en formato `upstream/signal-extraction/schemas/signal_card.schema.json`
con `entry_gate_decision = pass_to_inventory_mapping`, listas para entrar al Entry Gate
de Inventory Mapping.

**Nota**: Ese Entry Gate de IM en la implementación actual opera sobre el formato legacy
(`modules/01_entry_gate.md`), no sobre el formato canónico del upstream. La conexión entre
Pipeline B y el IM actual requeriría o bien la ejecución de legacy-migration sobre los outputs
de Signal Extraction, o bien la actualización del IM Entry Gate para aceptar el nuevo formato.
