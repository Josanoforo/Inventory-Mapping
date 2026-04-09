# Seccion 1 — Mapa de infraestructura

## A) Scripts en scripts/

| Path | Primera linea del docstring |
|---|---|
| `scripts/parse_dg_shard.py` | `parse_dg_shard.py — Data Gathering shard parser.` |

Total: 1 script Python.

## B) Skills en .claude/skills/*/SKILL.md

| Path | Primera linea |
|---|---|
| `.claude/skills/entry-gate/SKILL.md` | `# Entry Gate — Skill` |
| `.claude/skills/split-cards/SKILL.md` | `# Split Cards — Skill` |
| `.claude/skills/index-cards/SKILL.md` | `# Index Cards — Skill` |
| `.claude/skills/scan-contradictions/SKILL.md` | `# Scan Contradictions — Skill` |
| `.claude/skills/scan-asymmetries/SKILL.md` | `# Scan Asymmetries — Skill` |
| `.claude/skills/scan-frictions/SKILL.md` | `# Scan Frictions — Skill` |
| `.claude/skills/scan-co-occurrences/SKILL.md` | `# Scan Co-occurrences — Skill` |
| `.claude/skills/scan-gaps/SKILL.md` | `# Scan Gaps — Skill` |
| `.claude/skills/scan-opposite-directions/SKILL.md` | `# Scan Opposite Directions — Skill` |
| `.claude/skills/scan-lexical-overlap/SKILL.md` | `Scan Lexical Overlap — Skill` |
| `.claude/skills/build-candidate/SKILL.md` | `Build Candidate — Skill` |
| `.claude/skills/validate-candidate/SKILL.md` | `Validate Candidate — Skill` |

Total: 12 skills.

## C) Modulos en modules/*.md

| Path | H1 title |
|---|---|
| `modules/01_entry_gate.md` | Module 01 — Entry Gate |
| `modules/02_splitter.md` | Module 02 — Splitter |
| `modules/03_indexer.md` | Module 03 — Indexer |
| `modules/04_scanner.md` | Module 04 — Scanner |
| `modules/05_candidate_builder.md` | Module 05 — Candidate Builder |
| `modules/06_validator.md` | Module 06 — Validator |

Total: 6 modulos.

## D) Referencias en reference/*.md

| Path | H1 title |
|---|---|
| `reference/protocol_canonical.md` | Inventory Mapping — Canonical Protocol |
| `reference/data_gathering_project_instructions_v4_5.md` | Project Instructions — Data Gathering (v4.5) |
| `reference/research_directions_protocol.md` | Research Directions Protocol |
| `reference/source_packet_conversion_template.md` | Source Packet conversion template |
| `reference/TC-001.md` | Tension Candidate TC-001 |

Total: 5 archivos de referencia.

## E) Schemas en schemas/*.json

| Path |
|---|
| `schemas/split_manifest.schema.json` |
| `schemas/index_manifest.schema.json` |
| `schemas/card_record.schema.json` |
| `schemas/scan_artifact.schema.json` |
| `schemas/tension_candidate.schema.json` |
| `schemas/validation_report.schema.json` |

Total: 6 schemas JSON.

## F) Nota sobre input/

No existen archivos `input/signal_cards_round_*.md` en el repo actualmente. El directorio de input esta vacio o no contiene los archivos fuente esperados por el pipeline.
