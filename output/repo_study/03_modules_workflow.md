# Seccion 3 — Como operan los modulos de IM

## Module 01 — Entry Gate

- **Archivo:** `modules/01_entry_gate.md`
- **Proposito:** Verifica que el inventario de signal cards es apto para mapping. Si falla, nada mas corre. Actua como puerta de entrada al pipeline.
- **Input:** `input/signal_cards_round_*.md` (10 archivos, 1,560 cards esperadas). Formato: markdown raw.
- **Output:** `working/entry_gate/entry_gate_report.json`. Formato: JSON con status pass/fail, conteo de cards por round, y resultado de 5 checks (discrete_cards, no_interpretation, no_meta_observations, evidence_preserved, ids_traceable).
- **Manifests/estado intermedio:** No. Produce un unico reporte.
- **Retomable:** No. No hay menciones de "resume", "skip if exists", "manifest", "pending", "complete", ni "checkpoint". Es una pasada unica de validacion.
- **Skill que lo ejecuta:** `entry-gate` (declarado implicitamente por la estructura del repo; el SKILL.md referencia `modules/01_entry_gate.md`).

---

## Module 02 — Splitter

- **Archivo:** `modules/02_splitter.md`
- **Proposito:** Divide los archivos raw de rounds en batches discretos de cards, adecuados para indexacion incremental.
- **Input:** `input/signal_cards_round_*.md` (10 archivos). Formato: markdown, cards delimitadas por `---` conteniendo `**SC-R*`.
- **Output:**
  - `working/split/card_batches/` — archivos batch nombrados `batch_RNN_BBB.md` (20-30 cards por batch)
  - `working/split/split_manifest.json` — valida contra `schemas/split_manifest.schema.json`
- **Manifests/estado intermedio:** SI. `split_manifest.json` registra por cada round: cards_found, batches_written, status. Actualizado despues de procesar cada round (linea 22 del modulo).
- **Retomable:** SI. Linea 32: "If interrupted, read split_manifest.json. Resume from first round with status `pending`."
- **Skill que lo ejecuta:** `split-cards` (SKILL.md referencia `modules/02_splitter.md`).

---

## Module 03 — Indexer

- **Archivo:** `modules/03_indexer.md`
- **Proposito:** Transforma batches de cards en un indice JSONL estructurado para scanning mecanico. Extrae campos de cada card.
- **Input:**
  - `working/split/card_batches/batch_*.md`
  - `working/split/split_manifest.json` (para saber que procesar)
- **Output:**
  - `working/index/card_index.jsonl` — una linea JSON por card. Valida contra `schemas/card_record.schema.json`.
  - `working/index/index_manifest.json` — valida contra `schemas/index_manifest.schema.json`
- **Manifests/estado intermedio:** SI. `index_manifest.json` registra: batches_processed, cards_indexed, last_batch_processed, issues, status.
- **Retomable:** SI. Linea 35: "Read index_manifest.json. Resume from `last_batch_processed`. Do not reprocess already-indexed batches." Linea 39: cuando termina, status = `complete`.
- **Skill que lo ejecuta:** `index-cards` (SKILL.md referencia `modules/03_indexer.md`).

---

## Module 04 — Scanner

- **Archivo:** `modules/04_scanner.md`
- **Proposito:** Corre 7 operaciones mecanicas independientes sobre el card index. Cada una produce un scan artifact. Los artifacts alimentan al candidate builder.
- **Input:** `working/index/card_index.jsonl`. Formato: JSONL.
- **Output:** 7 archivos en `working/scans/`:

  | Archivo | Operacion |
  |---|---|
  | `contradictions.json` | Pares que afirman cosas opuestas sobre el mismo sujeto |
  | `asymmetries.json` | Ejes con distribucion desigual |
  | `frictions.json` | Algo documentado bloquea algo documentado |
  | `co_occurrences.json` | 3+ cards co-ocurriendo consistentemente |
  | `gaps.json` | Areas donde esperarias cards y no hay |
  | `opposite_directions.json` | Fuerzas contrarias sobre el mismo sistema |
  | `lexical_overlap.json` | Cards que comparten vocabulario/territorio |

  Todos validan contra `schemas/scan_artifact.schema.json`.
- **Manifests/estado intermedio:** No. Ninguno de los 7 scans usa manifest.
- **Retomable:** No. No hay menciones de "resume", "manifest", "checkpoint", "pending", ni "complete". Cada scan es una pasada completa sobre el indice. Nota: los 7 scans corren independientemente y en cualquier orden (linea 68).
- **Skills que lo ejecutan:** 7 skills separados, uno por operacion: `scan-contradictions`, `scan-asymmetries`, `scan-frictions`, `scan-co-occurrences`, `scan-gaps`, `scan-opposite-directions`, `scan-lexical-overlap`.

---

## Module 05 — Candidate Builder

- **Archivo:** `modules/05_candidate_builder.md`
- **Proposito:** Transforma patrones escaneados con routing `tension_candidate` o `needs_audit` en archivos TC completos. Tambien produce rejected_groupings.md, coverage_gaps.md, e isolated_signals.md.
- **Input:**
  - `working/scans/*.json` (los 7 scan artifacts)
  - `input/signal_cards_round_*.md` (para verificar Signal IDs)
  - `reference/TC-001.md` (formato de referencia)
  - `reference/protocol_canonical.md` (reglas)
- **Output:**
  - `output/tension_candidates/TC-NNN.md` — un archivo por candidato (numeracion empieza en TC-002)
  - `output/rejected_groupings.md`
  - `output/coverage_gaps.md`
  - `output/isolated_signals.md`
  - `output/review_queue.md` — indice de todos los TCs con status
- **Manifests/estado intermedio:** No. No hay manifest formal. `review_queue.md` funciona como indice pero no como checkpoint de estado.
- **Retomable:** No. No hay menciones de "resume", "skip if exists", "manifest", "last_processed", ni "checkpoint". Construye todos los TCs desde cero en cada ejecucion.
- **Skill que lo ejecuta:** `build-candidate` (SKILL.md referencia `modules/05_candidate_builder.md`).

---

## Module 06 — Validator

- **Archivo:** `modules/06_validator.md`
- **Proposito:** Corre checks del protocolo canonico contra cada TC producido. Marca fallos sin descartar TCs. Reporta, no arregla.
- **Input:**
  - `output/tension_candidates/TC-*.md` (todos los TCs producidos)
  - `reference/protocol_canonical.md` (los 8 checks canonicos)
- **Output:**
  - `working/validation/candidate_reports/TC-NNN_validation.json` — reporte por candidato. Valida contra `schemas/validation_report.schema.json`.
  - `working/validation/validation_summary.json` — resultados agregados (total_candidates, passed, failed, checks_most_failed, candidates_needing_attention)
- **Manifests/estado intermedio:** No. Aunque produce reportes por TC, no tiene logica de "skip if already validated".
- **Retomable:** No. No hay menciones de "resume", "manifest", "checkpoint", "pending", ni "skip if exists". Valida todos los TCs desde cero.
- **Skill que lo ejecuta:** `validate-candidate` (SKILL.md referencia `modules/06_validator.md`).

---

## Resumen de retomabilidad

| Modulo | Manifest | Retomable | Mecanismo |
|---|---|---|---|
| 01 Entry Gate | No | No | Pasada unica |
| 02 Splitter | `split_manifest.json` | SI | Resume from first round with status `pending` |
| 03 Indexer | `index_manifest.json` | SI | Resume from `last_batch_processed` |
| 04 Scanner | No | No | 7 operaciones independientes, sin checkpoint |
| 05 Candidate Builder | No | No | Construye todo desde cero |
| 06 Validator | No | No | Valida todo desde cero |
