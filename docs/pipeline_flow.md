# Pipeline Flow — Phase 0 → IM

Estudio del pipeline real de Inventory Mapping. Todos los paths verificados contra el repo en branch `claude/analyze-pipeline-phases-xsgSn` (contiene el merge de `claude/phase-1b-extraction-bridge-eChp8`).

Notación del pipeline mapeada al repo:

| Notación | Directorio real | Función |
|---|---|---|
| **Phase 0** | `upstream/data-gathering/` | Raw data gathering desde fuentes |
| **Phase 1a** | `upstream/source-intake/` | Separación por source, preservando contexto local |
| **Phase 1b** | `upstream/data-extraction/` | Extracción de claims discretas por source |
| **Phase 2** | `upstream/signal-extraction/` | Conversión de extraction records a Signal Cards observacionales |
| **G1** | `upstream/signal-extraction/contracts/signal_to_inventory_entry_gate.md` | Gate Signal → IM |
| **IM** | `.claude/skills/` + `modules/` | Inventory Mapping (6 steps) |

Confirmado por referencias explícitas dentro de los module files:
- `upstream/source-intake/modules/converter.md` — "sits between **Phase 0** and **Phase 1 Source Intake**"
- `upstream/data-extraction/modules/extraction_converter.md` — "sits between **Phase 1** and **Phase 2**"
- `upstream/signal-extraction/modules/signal_converter.md` — "sits between **Phase 2** and the **Inventory Mapping entry gate**"

---

## 1. Flujo de directorios: shard → TC

```
input shard (Phase 0)
    │
    ▼
upstream/data-gathering/scripts/parse_dg_shard.py
    │
    ▼
working/data_gathering/findings/*.json
    │
    ▼
upstream/source-intake/scripts/converter_prepare.py              [Phase 1a Stage 1]
    │
    ▼
working/source_intake/skeleton_batches/batch_NNN/skeleton_*.json
    │
    ▼
.claude/skills/convert-findings/SKILL.md                         [Phase 1a Stage 2]
 → upstream/source-intake/modules/converter.md
    │
    ▼
working/source_intake/packets/<packet_id>.json
    │
    ▼
upstream/data-extraction/scripts/extraction_prepare.py           [Phase 1b Stage 1]
    │
    ▼
working/data_extraction/skeleton_batches/batch_NNN/skeleton_*.json
    │
    ▼
.claude/skills/extract-records/SKILL.md                          [Phase 1b Stage 2]
 → upstream/data-extraction/modules/extraction_converter.md
    │
    ▼
working/data_extraction/records/<extraction_id>.json
    │
    ▼
upstream/signal-extraction/scripts/signal_prepare.py             [Phase 2 Stage 1]
    │
    ▼
working/signal_extraction/skeleton_batches/batch_NNN/skeleton_*.json
    │
    ▼
.claude/skills/extract-signals/SKILL.md                          [Phase 2 Stage 2]
 → upstream/signal-extraction/modules/signal_converter.md
    │
    ▼
working/signal_extraction/cards/<signal_id>.json
    │
    ▼
[G1] upstream/signal-extraction/contracts/signal_to_inventory_entry_gate.md
    │
    ▼
upstream/signal-extraction/scripts/signal_to_markdown.py         [Bridge Phase 2 → IM]
    │
    ▼
input/signal_cards_round_*.md                                    [entrada del IM]
    │
    ▼
.claude/skills/entry-gate/SKILL.md        → working/entry_gate/entry_gate_report.json
    │
    ▼
.claude/skills/split-cards/SKILL.md       → working/split/card_batches/*.md
    │
    ▼
.claude/skills/index-cards/SKILL.md       → working/index/card_index.jsonl
    │
    ▼
.claude/skills/scan-*/SKILL.md (×7)       → working/scans/*.json
    │
    ▼
.claude/skills/build-candidate/SKILL.md   → output/tension_candidates/TC-NNN.md
    │
    ▼
.claude/skills/validate-candidate/SKILL.md → working/validation/candidate_reports/*.json
    │
    ▼
output/tension_candidates/TC-NNN.md (final, con validation aplicada)
```

---

## 2. Phase 0 — Data Gathering

**Script/módulo que lo ejecuta:**
- `upstream/data-gathering/scripts/parse_dg_shard.py`

**Input:**
- Directorio: `input/data_gathering/` (o shards directos)
- Formato: Shards markdown de investigación

**Output:**
- Directorio: `working/data_gathering/findings/*.json`
- Formato: JSON findings + carpeta de recovery `working/data_gathering/phase0_part4_gpt_recovery/`

**Stage 1 + Stage 2:**
- Phase 0 **no sigue** el patrón Stage 1 + Stage 2 de las otras fases.
- `parse_dg_shard.py` es el único script; Stage 2 es manual/humano (o vía recovery agent).

**Validators / gates:**
- **No existe** contract ni validator file en `upstream/data-gathering/contracts/` (dicho directorio no existe)
- **No existe** module spec en `upstream/data-gathering/modules/` (dicho directorio no existe)
- `upstream/data-gathering/reference/` contiene solo `data_gathering_project_instructions_v4_5.md` y `research_directions_protocol.md`

**Rechazos / recovery:**
- Recovery agent: `agents/codex/phase0-recovery/CONTRACT.md` (215 líneas)
- Working recovery: `working/data_gathering/phase0_part4_gpt_recovery/`

**Gap reportado:** Phase 0 es la única fase sin contrato formal, sin módulo Stage 2, y sin schema declarado. El único artefacto normativo es el recovery CONTRACT del agente codex.

---

## 3. Phase 1a — Source Intake

### Stage 1 — Preparación mecánica (Python)

**Script:**
- `upstream/source-intake/scripts/converter_prepare.py` (543 líneas)

**Input:**
- Directorio: `working/data_gathering/findings/*.json`
- Formato: JSON findings desde Phase 0

**Output:**
- Directorio: `working/source_intake/skeleton_batches/batch_NNN/skeleton_*.json`
- Manifest: `working/source_intake/skeleton_batches/converter_prepare_manifest.json`
- Formato: JSON skeletons con **11 campos mecánicos prellenados** (packet_id, source_id, source_type, source_ref, snippets, etc.) y los **8 campos de juicio vacíos** para Stage 2

**Schema manifest:** `upstream/source-intake/schemas/converter_prepare_manifest.schema.json`

### Stage 2 — Conversión con juicio (Claude skill)

**Skill:**
- `.claude/skills/convert-findings/SKILL.md`

**Módulo que gobierna el Stage 2:**
- `upstream/source-intake/modules/converter.md` (217 líneas)

**Contrato normativo:**
- `upstream/source-intake/contracts/source_intake_contract.md` (425 líneas)

**Input:**
- `working/source_intake/skeleton_batches/batch_NNN/skeleton_*.json`

**Output:**
- Directorio: `working/source_intake/packets/<packet_id>.json`
- Manifest: `working/source_intake/converter_manifest.json`
- Formato: JSON Source Packets con los 8 campos de juicio llenados — possible_subjects, possible_actor_levels, possible_metric_types, possible_time_scopes, possible_geographies, uncertainties, priority_for_source_first, traceability_status

**Schema packet:** `upstream/source-intake/schemas/source_packet.schema.json`
**Schema converter manifest:** `upstream/source-intake/schemas/converter_manifest.schema.json`

### Validators / gates

- **Validator file:** `upstream/source-intake/contracts/source_intake_validator.md`
- **Schema validator:** `upstream/source-intake/schemas/source_intake_validation.schema.json`
- Los checks están definidos en §9 del contract (Validation Checklist) — verifica traceabilidad, no fusión cross-source, snippets literales, etc.

### Rechazos / recovery

- Working recovery: `working/source_intake/source_intake_gpt_recovery/`
- Recovery agent: `agents/codex/source-intake-recovery/CONTRACT.md` (184 líneas)
- Patrón de recovery: skeleton original + partial output + failure detail + recovery guidance

---

---

## 4. Phase 1b — Data Extraction

### Stage 1 — Preparación mecánica (Python)

**Script:**
- `upstream/data-extraction/scripts/extraction_prepare.py` (419 líneas)

**Input:**
- Directorio: `working/source_intake/packets/*.json`
- Formato: Source Packets desde Phase 1a

**Output:**
- Directorio: `working/data_extraction/skeleton_batches/batch_NNN/skeleton_*.json`
- Manifest: `working/data_extraction/skeleton_batches/extraction_prepare_manifest.json`
- Formato: JSON Extraction Record skeletons. Cada snippet de un Source Packet se expande en un skeleton individual. **10 campos mecánicos prellenados**, 15 campos de juicio vacíos.

**Schema manifest:** `upstream/data-extraction/schemas/extraction_prepare_manifest.schema.json`

### Stage 2 — Conversión con juicio (Claude skill)

**Skill:**
- `.claude/skills/extract-records/SKILL.md`

**Módulo que gobierna el Stage 2:**
- `upstream/data-extraction/modules/extraction_converter.md` (259 líneas)

**Contrato normativo:**
- `upstream/data-extraction/contracts/data_extraction_contract.md` (486 líneas)

**Input:**
- `working/data_extraction/skeleton_batches/batch_NNN/skeleton_*.json`

**Output:**
- Directorio: `working/data_extraction/records/<extraction_id>.json`
- Manifest: `working/data_extraction/extraction_converter_manifest.json`
- Formato: JSON Extraction Records con los 15 campos de juicio llenos — claim_type, subject_exact, actor_level, platforms, product_type_if_explicit, metric_type, metric_value_raw, metric_unit, time_scope_raw, time_scope_normalized_if_safe, geography_if_explicit, evidence_role, local_qualifiers, uncertainties, parser_notes

**Schema record:** `upstream/data-extraction/schemas/data_extraction_record.schema.json`
**Schema converter manifest:** `upstream/data-extraction/schemas/extraction_converter_manifest.schema.json`

### Validators / gates

- **Validator file:** `upstream/data-extraction/contracts/data_extraction_validator.md`
- **Schema validator:** `upstream/data-extraction/schemas/data_extraction_validator.schema.json`
- Los checks están definidos en §11 del contract (Validation Checklist) — verifica claim discreteness, observabilidad, taxonomía de fallos

### Rechazos / recovery

- Working recovery: `working/data_extraction/extraction_gpt_recovery/`
- No hay recovery agent dedicado en `agents/codex/` para Phase 1b → **gap parcial**

---

## 5. Phase 2 — Signal Extraction

### Stage 1 — Preparación mecánica (Python)

**Script:**
- `upstream/signal-extraction/scripts/signal_prepare.py` (447 líneas)

**Input:**
- Directorio: `working/data_extraction/records/*.json`
- Formato: Extraction Records desde Phase 1b

**Output:**
- Directorio: `working/signal_extraction/skeleton_batches/batch_NNN/skeleton_*.json`
- Manifest: `working/signal_extraction/skeleton_batches/signal_prepare_manifest.json`
- Formato: JSON Signal Card skeletons 1:1 desde Extraction Records. **5 campos mecánicos prellenados** (signal_id, source_record_ids, source_ids, round, traceability_pointers). Incluye `_extraction_context` con todos los campos del extraction record para que Stage 2 pueda decidir split.

**Schema manifest:** `upstream/signal-extraction/schemas/signal_prepare_manifest.schema.json`

### Stage 2 — Conversión con juicio (Claude skill)

**Skill:**
- `.claude/skills/extract-signals/SKILL.md`

**Módulo que gobierna el Stage 2:**
- `upstream/signal-extraction/modules/signal_converter.md` (304 líneas)

**Contrato normativo:**
- `upstream/signal-extraction/contracts/signal_extraction_contract.md` (357 líneas)

**Input:**
- `working/signal_extraction/skeleton_batches/batch_NNN/skeleton_*.json`

**Output:**
- Directorio: `working/signal_extraction/cards/<signal_id>.json`
- Manifest: `working/signal_extraction/signal_converter_manifest.json`
- Formato: JSON Signal Cards con `signal_text` observacional formulado + 16 campos de juicio llenos
- **Puede dividir un skeleton en múltiples Signal Cards** si detecta múltiples claims discretas dentro del mismo extraction record

**Schema card:** `upstream/signal-extraction/schemas/signal_card.schema.json`
**Schema converter manifest:** `upstream/signal-extraction/schemas/signal_converter_manifest.schema.json`

### Validators / gates

- **Validator file:** `upstream/signal-extraction/contracts/signal_extraction_validator.md` — **11 checks** definidos
- **Schema validator:** `upstream/signal-extraction/schemas/signal_validation.schema.json`

### Bridge Phase 2 → IM

- **Script:** `upstream/signal-extraction/scripts/signal_to_markdown.py` (427 líneas)
- Convierte `working/signal_extraction/cards/*.json` en `input/signal_cards_round_*.md`
- Este es el único puente entre las fases upstream (formato JSON) y el IM (formato markdown)

### Rechazos / recovery

- Working recovery: `working/signal_extraction/signal_gpt_recovery/`
- No hay recovery agent dedicado en `agents/codex/` para Phase 2 → **gap parcial**

---

## 6. G1 — Entry Gate Signal → IM

**Contrato:**
- `upstream/signal-extraction/contracts/signal_to_inventory_entry_gate.md` (414 líneas)

**Schema:**
- `upstream/signal-extraction/schemas/signal_inventory_gate.schema.json`

**Propósito:** Gate que previene que señales "cocinadas" (sintetizadas, cross-source, interpretativas) entren al IM.

**Input:** `working/signal_extraction/cards/*.json` (Signal Cards validadas de Phase 2)

**Output:** Routing decision por signal card. El output físico al IM es `input/signal_cards_round_*.md` (vía `signal_to_markdown.py`), pero solo las cards con decisión `pass_to_inventory_mapping`.

**Checks obligatorios (8):**
1. validation_status — card pasó validators de Phase 2
2. discreteness — una sola claim por card, no compuesta
3. observational_boundary — describe lo observado, no lo inferido
4. subject_exactness — el sujeto es el exacto de la fuente, no generalizado
5. actor_level — nivel de actor preservado (individual, platform, market)
6. time/qualifier preservation — qualifiers temporales y contextuales preservados
7. cross-source contamination — no hay síntesis entre sources
8. pattern-readiness — card puede participar en un pattern sin ser interpretada

**Routing de output (4 decisiones):**
- `pass_to_inventory_mapping` → entra a IM (via `signal_to_markdown.py`)
- `preserve_as_isolated_signal` → archivo (señal demasiado débil para pattern detection, se preserva)
- `return_to_signal_rework` → cola de recovery de Phase 2
- `reject_from_inventory_input` → rechazada (síntesis cross-source, intrazable, etc.)

---

---

## 7. IM — Inventory Mapping (6 steps)

Cada step del IM es sequencial. Cada step lee de `working/` y escribe en `working/`. Solo el step 5 (Candidate Builder) escribe a `output/`.

Authority hierarchy (de `CLAUDE.md`):
1. `reference/protocol_canonical.md` — canon supremo
2. `modules/*.md` — specs normativas por step
3. `.claude/skills/*/SKILL.md` — routines ejecutables

### 7.1 — Step 1: Entry Gate

**Skill:** `.claude/skills/entry-gate/SKILL.md`
**Módulo:** `modules/01_entry_gate.md`

**Input:** `input/signal_cards_round_*.md` (markdown desde G1)

**Output:** `working/entry_gate/entry_gate_report.json`

**Stage 1 + Stage 2:** No aplica — single-stage gate.

**Checks (5):**
1. Discrete cards — una observación por card
2. No strategic interpretation — solo observaciones, no estrategia
3. No cross-source meta-observations — no agregación
4. Evidence base preserved — todas las cards tienen `evidence_base`
5. IDs present and traceable — formato `SC-R[round]-[number]`

**Rechazos:** Fallas detienen el pipeline completo. No hay routing de recovery — el report reporta IDs específicos y violations.

**Schema:** **Gap** — no hay schema declarado para `entry_gate_report.json` en `schemas/`

### 7.2 — Step 2: Split Cards

**Skill:** `.claude/skills/split-cards/SKILL.md`
**Módulo:** `modules/02_splitter.md`

**Input:** `input/signal_cards_round_*.md`

**Output:**
- `working/split/card_batches/batch_R{round}_{n}.md` (20-30 cards por batch)
- `working/split/split_manifest.json`

**Stage 1 + Stage 2:** No aplica — single-stage.

**Gates / fail states:**
- Card count mismatch
- Delimiter (`---` con `**SC-R*`) no encontrado
- Schema manifest invalida

**Schema manifest:** `schemas/split_manifest.schema.json`

**Resumability:** Lee `split_manifest.json`, salta rounds completados.

### 7.3 — Step 3: Index Cards

**Skill:** `.claude/skills/index-cards/SKILL.md`
**Módulo:** `modules/03_indexer.md`

**Input:**
- `working/split/card_batches/batch_*.md`
- `working/split/split_manifest.json`

**Output:**
- `working/index/card_index.jsonl` (una línea JSON por card)
- `working/index/index_manifest.json`

**Stage 1 + Stage 2:** No aplica — single-stage secuencial.

**Campos extraídos por record:**
- Required: `id`, `round`, `observation`, `source`, `source_type`, `domain`, `extraction_status`
- Optional: `date`, `evidence_base`
- Best-effort: `entities[]`, `figures[]`

**Validators:**
- Cada record valida contra `schemas/card_record.schema.json`
- Records que fallan se loguean en `index_manifest.issues[]` pero no detienen el proceso

**Schemas:**
- Record: `schemas/card_record.schema.json`
- Manifest: `schemas/index_manifest.schema.json`

**Resumability:** Lee `index_manifest.json`, salta batches ya procesados.

### 7.4 — Step 4: Scanner (7 operaciones paralelas)

**Módulo:** `modules/04_scanner.md`

**Input:** `working/index/card_index.jsonl` (single source para los 7 scans)

**Output:** 7 artifacts independientes en `working/scans/`:

| Scan | Skill path | Output file |
|---|---|---|
| Contradictions | `.claude/skills/scan-contradictions/SKILL.md` | `working/scans/contradictions.json` |
| Asymmetries | `.claude/skills/scan-asymmetries/SKILL.md` | `working/scans/asymmetries.json` |
| Frictions | `.claude/skills/scan-frictions/SKILL.md` | `working/scans/frictions.json` |
| Co-occurrences | `.claude/skills/scan-co-occurrences/SKILL.md` | `working/scans/co_occurrences.json` |
| Gaps | `.claude/skills/scan-gaps/SKILL.md` | `working/scans/gaps.json` |
| Opposite directions | `.claude/skills/scan-opposite-directions/SKILL.md` | `working/scans/opposite_directions.json` |
| Lexical overlap | `.claude/skills/scan-lexical-overlap/SKILL.md` | `working/scans/lexical_overlap.json` |

**Stage 1 + Stage 2:** No aplica — cada scan es single-stage. Los 7 scans son independientes y pueden correr en paralelo.

**Routing por patrón (5 opciones):**
- `tension_candidate` — cumple al menos una Candidate Generation Rule del canon
- `rejected_grouping` — frecuencia sin fricción
- `coverage_gap` — ausencia relevante
- `isolated_signal` — card única rara, se preserva
- `needs_audit` — soporte parcial, clasificación unclear

**Cap rule:** Si un patrón tiene >30 Signal IDs → split en sub-mecanismos (platform-specific, mechanism-specific) antes de routing.

**Routing-specific rules por scan:**
- **Contradictions**: ambos polos con 2+ cards → `tension_candidate`; un polo con 1 card → `needs_audit`
- **Asymmetries**: ambos polos con 2+ cards; definidos en términos del corpus, no rangos absolutos
- **Frictions**: blocker documentado + blocked documentado, ambos con card support (mín 2 total)
- **Co-occurrences**: 3+ cards cross-round o cross-source; debe generar DT question plausible
- **Gaps**: todas routed como `coverage_gap`
- **Opposite directions**: fuerzas documentadas actuando sobre el mismo sistema, ambas con 2+ cards
- **Lexical overlap**: **default = `rejected_grouping`** — solo `tension_candidate` si hay fricción explícita

**Schema:** `schemas/scan_artifact.schema.json` (todos los 7 validan contra el mismo)

**Gates:** Sin gate propio; la validación ocurre en Step 5 (pre-build filter).

### 7.5 — Step 5: Candidate Builder

**Skill:** `.claude/skills/build-candidate/SKILL.md`
**Módulo:** `modules/05_candidate_builder.md`

**Contratos normativos que gobiernan este step:**
- `reference/protocol_canonical.md` (canon)
- `reference/TC-001.md` (template de formato)
- `modules/05_candidate_builder.md` (spec normativo)

**Input:**
- `working/scans/*.json` (los 7 artifacts)
- `input/signal_cards_round_*.md` (para verificación de Signal IDs)
- `reference/TC-001.md` (formato)
- `reference/protocol_canonical.md` (rules)

**Output:**
- `output/tension_candidates/TC-NNN.md` (uno por candidate, NNN empieza en 002)
- `output/rejected_groupings.md`
- `output/coverage_gaps.md`
- `output/isolated_signals.md`
- `output/review_queue.md`

**Stage 1 — Pre-build filter:**
- Lexical overlap con <3 Signal IDs → `rejected_grouping` (stop, no build)
- Lexical overlap con 3+ IDs sin fricción explícita → `rejected_grouping` (stop, no build)
- Otros scans con <3 IDs → proceder pero añadir "minimal support" a `classification_risk`
- **Todo pattern descartado DEBE escribirse en `rejected_groupings.md`**
- Verification: `(rejected count) + (passed count) = (total needs_audit count)`

**Stage 2 — TC construction:**
- Verificar cada Signal ID contra source files (`input/signal_cards_round_*.md`); si card no existe, excluir
- Si <2 Signal IDs verificados después de verificación → demote a `rejected_grouping`
- Card-polo relevance check: cada card se relaciona directamente con la definición de su polo
- Deduplicación: si dos patterns comparten >70% Signal IDs **y** mismo mecanismo → merge con `source_patterns` notado
- Build TC markdown siguiendo `reference/TC-001.md`
- Validar contra `schemas/tension_candidate.schema.json`
- Escribir a `output/tension_candidates/TC-NNN.md`

**Schemas:**
- TC: `schemas/tension_candidate.schema.json`

**Gates (reglas obligatorias del TC):**
- `id`: formato `TC-NNN`
- `status`: `pending_review` o `needs_audit_before_classification`
- `type`: enum de 6 tipos (contradicción, fricción, hueco, dirección opuesta, co-ocurrencia significativa, asimetría distributiva)
- `structured_support.poles[]` siempre usado (nunca top-level `polo_a`/`polo_b`)
- `definition` ≠ `mechanical_summary` (mandatory)
- `unit_used` debe listar unidades específicas, nunca solo "mixed"
- Human fields siempre vacíos

**Rechazos / recovery:**
- Patterns descartados → `output/rejected_groupings.md` (con rationale)
- Coverage gaps → `output/coverage_gaps.md`
- Isolated signals → `output/isolated_signals.md`

### 7.6 — Step 6: Validate Candidate

**Skill:** `.claude/skills/validate-candidate/SKILL.md`
**Módulo:** `modules/06_validator.md`

**Input:**
- `output/tension_candidates/TC-*.md` (todos los TCs producidos)
- `reference/protocol_canonical.md` (los checks canónicos)
- `schemas/tension_candidate.schema.json`

**Output:**
- `working/validation/candidate_reports/TC-NNN_validation.json` (uno por TC)
- `working/validation/validation_summary.json` (aggregate)
- `output/review_queue.md` actualizado

**Stage 1 + Stage 2:** No aplica — single-stage validator.

**Checks (16):**
1. Signal IDs verified — cada ID con descripción parentética
2. Candidate Generation Rules met — no es pura frecuencia
3. Corpus-term polos — definiciones en términos del corpus, no rangos absolutos
4. Units declared — mixed units flagged, specific units listed
5. Supports distinction — yes/no distinguen evidencia de inferencia
6. Rejected Groupings exist — `rejected_groupings.md` no-vacío
7. Coverage Gaps reported — `coverage_gaps.md` no-vacío
8. Mechanical language — no adjetivos valorativos (word-boundary match, whitelist: "resolución", "valor central")
9. Type matches relation — TC type corresponde al pattern real
10. Signal IDs verified against source — spot-check 3 IDs random por TC en `input/`
11. Human fields empty — todos los human fields son strings vacíos
12. Schema valid — TC valida contra `tension_candidate.schema.json`
13. `mechanical_summary` ≠ `definition` — ningún polo tiene texto idéntico en ambos
14. `unit_used` specific — ningún polo dice "mixed" sin listar unidades
15. `what_it_supports` not template — no es "Coexistencia de los patrones documentados…" genérico
16. Card-polo relevance spot check — para TCs con >15 Signal IDs, spot-check 2 cards random por polo

**Schema:** `schemas/validation_report.schema.json`

**Behavior:** Reporta todas las fallas, **NO descarta TCs**. Los flags van en validation report y `review_queue.md`.

---

---

## 8. Schemas — tabla de referencia

### Schemas del IM (core pipeline)

| Schema | Path | Valida |
|---|---|---|
| card_record | `schemas/card_record.schema.json` | Una línea JSON en `card_index.jsonl` |
| index_manifest | `schemas/index_manifest.schema.json` | `working/index/index_manifest.json` |
| split_manifest | `schemas/split_manifest.schema.json` | `working/split/split_manifest.json` |
| scan_artifact | `schemas/scan_artifact.schema.json` | Los 7 archivos `working/scans/*.json` |
| tension_candidate | `schemas/tension_candidate.schema.json` | `output/tension_candidates/TC-*.md` (parsed) |
| validation_report | `schemas/validation_report.schema.json` | `working/validation/candidate_reports/*.json` |

### Schemas upstream (Phase 1a / 1b / 2)

| Phase | Schema | Path | Valida |
|---|---|---|---|
| 1a | source_packet | `upstream/source-intake/schemas/source_packet.schema.json` | Source Packets de Stage 2 |
| 1a | converter_manifest | `upstream/source-intake/schemas/converter_manifest.schema.json` | Manifest Stage 2 |
| 1a | converter_prepare_manifest | `upstream/source-intake/schemas/converter_prepare_manifest.schema.json` | Manifest Stage 1 |
| 1a | source_intake_validation | `upstream/source-intake/schemas/source_intake_validation.schema.json` | Validator reports |
| 1b | data_extraction_record | `upstream/data-extraction/schemas/data_extraction_record.schema.json` | Extraction Records Stage 2 |
| 1b | extraction_converter_manifest | `upstream/data-extraction/schemas/extraction_converter_manifest.schema.json` | Manifest Stage 2 |
| 1b | extraction_prepare_manifest | `upstream/data-extraction/schemas/extraction_prepare_manifest.schema.json` | Manifest Stage 1 |
| 1b | data_extraction_validator | `upstream/data-extraction/schemas/data_extraction_validator.schema.json` | Validator reports |
| 2 | signal_card | `upstream/signal-extraction/schemas/signal_card.schema.json` | Signal Cards Stage 2 |
| 2 | signal_converter_manifest | `upstream/signal-extraction/schemas/signal_converter_manifest.schema.json` | Manifest Stage 2 |
| 2 | signal_prepare_manifest | `upstream/signal-extraction/schemas/signal_prepare_manifest.schema.json` | Manifest Stage 1 |
| 2 | signal_validation | `upstream/signal-extraction/schemas/signal_validation.schema.json` | Validator reports |
| G1 | signal_inventory_gate | `upstream/signal-extraction/schemas/signal_inventory_gate.schema.json` | G1 gate decisions |

### Schemas faltantes (gaps)

- Phase 0: **no hay schemas** en `upstream/data-gathering/` (no existe el subdirectorio `schemas/`)
- IM Entry Gate: **no hay schema** para `entry_gate_report.json`

---

## 9. Skills — tabla de referencia

Todas en `.claude/skills/`. 15 skills totales.

### Skills upstream (Stage 2 de cada phase)

| Phase | Skill | Path |
|---|---|---|
| 1a | convert-findings | `.claude/skills/convert-findings/SKILL.md` |
| 1b | extract-records | `.claude/skills/extract-records/SKILL.md` |
| 2 | extract-signals | `.claude/skills/extract-signals/SKILL.md` |

### Skills IM

| Step | Skill | Path |
|---|---|---|
| 1 | entry-gate | `.claude/skills/entry-gate/SKILL.md` |
| 2 | split-cards | `.claude/skills/split-cards/SKILL.md` |
| 3 | index-cards | `.claude/skills/index-cards/SKILL.md` |
| 4 | scan-contradictions | `.claude/skills/scan-contradictions/SKILL.md` |
| 4 | scan-asymmetries | `.claude/skills/scan-asymmetries/SKILL.md` |
| 4 | scan-frictions | `.claude/skills/scan-frictions/SKILL.md` |
| 4 | scan-co-occurrences | `.claude/skills/scan-co-occurrences/SKILL.md` |
| 4 | scan-gaps | `.claude/skills/scan-gaps/SKILL.md` |
| 4 | scan-opposite-directions | `.claude/skills/scan-opposite-directions/SKILL.md` |
| 4 | scan-lexical-overlap | `.claude/skills/scan-lexical-overlap/SKILL.md` |
| 5 | build-candidate | `.claude/skills/build-candidate/SKILL.md` |
| 6 | validate-candidate | `.claude/skills/validate-candidate/SKILL.md` |

### Skills faltantes (gaps)

- Phase 0: **no hay skill** para data gathering Stage 2 (el flow se hace vía recovery agent o manualmente)

---

## 10. Módulos y contratos — tabla de referencia

### Upstream (contratos + módulos Stage 2)

| Phase | Contract | Module (Stage 2 spec) | Validator spec |
|---|---|---|---|
| 0 | **— (no existe)** | **— (no existe)** | **— (no existe)** |
| 1a | `upstream/source-intake/contracts/source_intake_contract.md` (425 líneas) | `upstream/source-intake/modules/converter.md` (217 líneas) | `upstream/source-intake/contracts/source_intake_validator.md` |
| 1b | `upstream/data-extraction/contracts/data_extraction_contract.md` (486 líneas) | `upstream/data-extraction/modules/extraction_converter.md` (259 líneas) | `upstream/data-extraction/contracts/data_extraction_validator.md` |
| 2 | `upstream/signal-extraction/contracts/signal_extraction_contract.md` (357 líneas) | `upstream/signal-extraction/modules/signal_converter.md` (304 líneas) | `upstream/signal-extraction/contracts/signal_extraction_validator.md` |
| G1 | `upstream/signal-extraction/contracts/signal_to_inventory_entry_gate.md` (414 líneas) | — (no Stage 2; es gate puro) | — (los checks están en el contract) |

### IM (módulos)

| Step | Module | Gobierna |
|---|---|---|
| 1 | `modules/01_entry_gate.md` | Entry Gate skill |
| 2 | `modules/02_splitter.md` | Split Cards skill |
| 3 | `modules/03_indexer.md` | Index Cards skill |
| 4 | `modules/04_scanner.md` | Los 7 scan skills |
| 5 | `modules/05_candidate_builder.md` | Build Candidate skill (Stage 1 pre-filter + Stage 2 construction) |
| 6 | `modules/06_validator.md` | Validate Candidate skill |

### Autoridad suprema

- `reference/protocol_canonical.md` — canon, override de todo
- `reference/TC-001.md` — template de formato TC (usado por `build-candidate`)

### Recovery agents

| Phase | Recovery agent | Path |
|---|---|---|
| 0 | phase0-recovery | `agents/codex/phase0-recovery/CONTRACT.md` (215 líneas) |
| 1a | source-intake-recovery | `agents/codex/source-intake-recovery/CONTRACT.md` (184 líneas) |
| 1b | — (no recovery agent) | **gap** |
| 2 | — (no recovery agent) | **gap** |

---

## 11. Gaps detectados

Los siguientes gaps están verificados contra el filesystem actual:

### Phase 0 — estructura incompleta

- **Sin contract:** no existe `upstream/data-gathering/contracts/`
- **Sin módulo Stage 2:** no existe `upstream/data-gathering/modules/`
- **Sin schemas:** no existe `upstream/data-gathering/schemas/`
- **Sin skill de Claude:** no hay `.claude/skills/` para Phase 0
- El único artefacto normativo para Phase 0 es el recovery CONTRACT del agente codex (`agents/codex/phase0-recovery/CONTRACT.md`), que no es un contrato de phase sino de recovery

### IM Entry Gate — sin schema de output

- `modules/01_entry_gate.md` declara el output `working/entry_gate/entry_gate_report.json` pero no hay schema para él en `schemas/`

### Recovery agents incompletos

- **Phase 1b (data-extraction)** tiene working recovery dir (`working/data_extraction/extraction_gpt_recovery/`) pero **no** recovery agent en `agents/codex/`
- **Phase 2 (signal-extraction)** tiene working recovery dir (`working/signal_extraction/signal_gpt_recovery/`) pero **no** recovery agent en `agents/codex/`

### Inventario de datos incompleto (no es gap estructural, es estado del corpus)

- Solo `input/signal_cards_round_1.md` está presente (76 cards de las 1,560 esperadas)
- Rounds 2-10 pendientes
- Pipeline corrió end-to-end sobre Round 1: 76 → 4 batches → 76 indexed → 34 scan patterns → 23 TCs → 23 validated
- Todos los TCs tienen human fields vacíos (esperando revisión humana)

---

## 12. Patrón Stage 1 + Stage 2 — síntesis

Las phases upstream (1a, 1b, 2) comparten una arquitectura consistente:

```
Stage 1 (Python script, mecánico)
 ├─ Input: output de la phase anterior (JSON)
 ├─ Output: skeleton_batches/batch_NNN/skeleton_*.json
 │   └─ Skeletons con campos mecánicos prellenados, campos de juicio vacíos
 └─ Manifest: <phase>_prepare_manifest.json
      │
      ▼
Stage 2 (Claude skill, juicio)
 ├─ Input: skeletons de Stage 1
 ├─ Módulo normativo: upstream/<phase>/modules/*.md
 ├─ Contrato: upstream/<phase>/contracts/*_contract.md
 ├─ Validator: upstream/<phase>/contracts/*_validator.md
 ├─ Output: records finales en working/<phase>/<records_dir>/
 │   └─ JSON con campos de juicio llenos
 ├─ Manifest: <phase>_converter_manifest.json
 └─ Recovery: working/<phase>/<phase>_gpt_recovery/
```

**Phase 0** NO sigue este patrón: solo tiene Stage 1 (`parse_dg_shard.py`) y el Stage 2 es manual/humano.

**IM** NO sigue este patrón: es una secuencia lineal de 6 steps, donde cada step tiene un solo skill (excepto Step 4 que tiene 7 scan skills paralelas). Solo el Step 5 (Candidate Builder) tiene estructura Stage 1 (pre-build filter) + Stage 2 (TC construction) dentro del mismo skill.

---

## 13. Verificación

Todos los paths referenciados en este documento fueron verificados contra el filesystem del repo en el commit actual del branch `claude/analyze-pipeline-phases-xsgSn`. Los gaps marcados como "no existe" fueron confirmados por listado del directorio padre.

Para re-verificar:
```bash
# Verificar upstream structure
ls upstream/*/{contracts,modules,schemas,scripts} 2>/dev/null

# Verificar skills
ls .claude/skills/

# Verificar módulos IM
ls modules/

# Verificar schemas IM
ls schemas/

# Verificar estado working
ls working/
```
