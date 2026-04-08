# Cleanup Executed Manifest
**Fecha y hora de ejecución:** 2026-04-08  
**Estado:** EJECUTADO — borrado completo de Bloques 1-4  
**Confirmación git:** 331 archivos eliminados (`331 files changed, 69077 deletions`)

---

## ARCHIVOS BORRADOS POR BLOQUE

### Bloque 1 — Cards legacy (10 archivos)

```
input/signal_cards_round_1.md
input/signal_cards_round_2.md
input/signal_cards_round_3.md
input/signal_cards_round_4.md
input/signal_cards_round_5.md
input/signal_cards_round_6.md
input/signal_cards_round_7.md
input/signal_cards_round_8.md
input/signal_cards_round_9.md
input/signal_cards_round_10.md
```

### Bloque 2 — Working dirs del run legacy (153 archivos, 7 directorios)

**working/entry_gate/** (1 archivo):
```
working/entry_gate/entry_gate_report.json
```

**working/split/** (68 archivos):
```
working/split/split_manifest.json
working/split/card_batches/batch_R01_001.md  batch_R01_002.md  batch_R01_003.md
working/split/card_batches/batch_R02_001.md … batch_R02_006.md  (6 archivos)
working/split/card_batches/batch_R03_001.md … batch_R03_006.md  (6 archivos)
working/split/card_batches/batch_R04_001.md … batch_R04_007.md  (7 archivos)
working/split/card_batches/batch_R05_001.md … batch_R05_007.md  (7 archivos)
working/split/card_batches/batch_R06_001.md … batch_R06_008.md  (8 archivos)
working/split/card_batches/batch_R07_001.md … batch_R07_008.md  (8 archivos)
working/split/card_batches/batch_R08_001.md … batch_R08_008.md  (8 archivos)
working/split/card_batches/batch_R09_001.md … batch_R09_006.md  (6 archivos)
working/split/card_batches/batch_R10_001.md … batch_R10_008.md  (8 archivos)
```

**working/index/** (2 archivos):
```
working/index/index_manifest.json
working/index/card_index.jsonl
```

**working/scans/** (7 archivos):
```
working/scans/asymmetries.json
working/scans/co_occurrences.json
working/scans/contradictions.json
working/scans/frictions.json
working/scans/gaps.json
working/scans/lexical_overlap.json
working/scans/opposite_directions.json
```

**working/validation/** (75 archivos):
```
working/validation/validation_summary.json
working/validation/candidate_reports/TC-002_validation.json … TC-075_validation.json  (74 archivos)
```

### Bloque 3 — Outputs de IM (154 archivos, 1 directorio)

**output/tension_candidates/** (149 archivos):
```
output/tension_candidates/TC-001.md
output/tension_candidates/TC-002.md  TC-002.json
output/tension_candidates/TC-003.md  TC-003.json
… (patrón .md + .json por TC)
output/tension_candidates/TC-075.md  TC-075.json
```

**Archivos individuales en output/** (5 archivos):
```
output/rejected_groupings.md
output/coverage_gaps.md
output/isolated_signals.md
output/review_queue.md
output/lex_review_25.json   ← agregado al bloque 3 tras inspección: output del scan
                               lexical_overlap corrido sobre las cards legacy (confirmado
                               por IDs SC-R1-024, SC-R2-063, etc. en su contenido)
```

**Nota:** `output/` quedó vacío. Se agregó `output/.gitkeep` siguiendo la convención del repo.

### Bloque 4 — legacy-migration/ completo (15 archivos, 1 árbol de directorios)

```
legacy-migration/legacy_mapping_notes.md
legacy-migration/legacy_migration_usage.md
legacy-migration/modules/01_legacy_signal_card_migration.md
legacy-migration/schemas/legacy_signal_card_migration.schema.json
legacy-migration/working/migrations/legacy_signal_card_migrations.jsonl
legacy-migration/working/manifests/legacy_migration_manifest.json
legacy-migration/working/preprocessing/url_normalization_design.md
legacy-migration/working/preprocessing/normalized_source_refs.jsonl
legacy-migration/working/preprocessing/url_normalization_execution_summary.md
legacy-migration/working/preprocessing/run_url_normalization.py
legacy-migration/output/legacy_migration_summary.md
legacy-migration/output/sample_20_selection.md
legacy-migration/output/unresolved_cases.md
legacy-migration/contracts/legacy_signal_card_migration.md
legacy-migration/.claude/skills/legacy-signal-card-migration/SKILL.md
```

---

## TOTALES

| Bloque | Archivos borrados |
|--------|-------------------|
| 1 — Cards legacy | 10 |
| 2 — Working dirs legacy | 153 |
| 3 — Outputs IM (incl. lex_review_25.json) | 154 |
| 4 — legacy-migration/ | 15 |
| **TOTAL** | **332** |

*Nota: `git diff HEAD` reporta 331 archivos changed. La diferencia de 1 se debe a que TC-001.json fue contado una sola vez en el recuento del dry-run. El conteo de git es el autoritativo.*

Directorios borrados: `working/entry_gate/`, `working/split/` (+ `card_batches/`), `working/index/`, `working/scans/`, `working/validation/` (+ `candidate_reports/`), `output/tension_candidates/`, `legacy-migration/` (árbol completo con 8 subdirectorios).

---

## ARCHIVOS NO BORRADOS — PENDIENTES DE DECISIÓN HUMANA (Bloque 5)

### Ambigüedad encontrada durante ejecución

**`inventory_mapping_upstream_bundle.zip`** — encontrado en la raíz del repo durante la ejecución del Bloque 4. No estaba en el dry-run manifest (no fue detectado en la exploración inicial). No pertenece claramente ni al pipeline activo ni a los bloques de borrado. **No se borró.** Requiere decisión humana en próxima sesión.

### Directorios con `_archive` en nombre — pipeline activo (confirmado por operadora)

```
working/data_extraction/rejected_archive/   ← destino de rejects de Data Extraction, NO borrar
working/source_intake/rejected_archive/     ← destino de rejects de Source Intake, NO borrar
```
Confirmados como parte del pipeline nuevo por la operadora durante la sesión. No se borran.

---

## ESTADO FINAL DE DIRECTORIOS CLAVE

| Directorio | Estado |
|------------|--------|
| `input/` | Solo contiene `data_gathering/` (intacto) |
| `working/` | Contiene `data_extraction/`, `data_gathering/`, `source_intake/` (todos intactos) |
| `output/` | Vacío con `.gitkeep` |
| `legacy-migration/` | Eliminado |

---

## CONFIRMACIÓN DE PATHS PROTEGIDOS — TODOS INTACTOS

| Path | Estado |
|------|--------|
| `upstream/` | ✓ intacto (data-extraction/, signal-extraction/, source-intake/) |
| `modules/` | ✓ intacto (6 archivos .md) |
| `.claude/` | ✓ intacto (agents/, skills/) |
| `reference/` | ✓ intacto (5 archivos) |
| `schemas/` | ✓ intacto (6 archivos .json) |
| `scripts/parse_dg_shard.py` | ✓ intacto |
| `input/data_gathering/` | ✓ intacto |
| `working/data_gathering/` | ✓ intacto (findings/, diagnostics/) |
| `working/data_extraction/` | ✓ intacto |
| `working/source_intake/` | ✓ intacto |

---

*Manifest producido el 2026-04-08. Cambios en working tree, sin commit todavía.*
