# Sección 1 — Mapa de flujo de Inventory Mapping

## Punto de entrada

Signal Cards en `input/signal_cards_round_*.md` (10 archivos, 1,561 cards en el run actual).
Provienen del upstream (Signal Extraction). El contrato de entrada está en
`upstream/signal-extraction/contracts/signal_to_inventory_entry_gate.md`.

---

## Flujo completo

```
input/signal_cards_round_*.md (10 archivos, 1,561 cards)
        │
        ▼
┌─────────────────────────────────────────────────────────────┐
│  MÓDULO 01 — Entry Gate                                     │
│  Skill: .claude/skills/entry-gate/SKILL.md                 │
│  Input:  input/signal_cards_round_*.md                      │
│  Output: working/entry_gate/entry_gate_report.json          │
│  Checks: 5 (discrete, no interpretation, no meta-obs,       │
│           evidence preserved, IDs traceable)                │
│  Fail → pipeline se detiene                                 │
└─────────────────────────────────────────────────────────────┘
        │
        │ si status = "pass"
        ▼
┌─────────────────────────────────────────────────────────────┐
│  MÓDULO 02 — Splitter                                       │
│  Skill: .claude/skills/split-cards/SKILL.md                │
│  Input:  input/signal_cards_round_*.md                      │
│  Output: working/split/card_batches/batch_RNN_BBB.md (80)  │
│          working/split/split_manifest.json                  │
│  Lote: ~25 cards por batch                                  │
│  Resumable desde split_manifest.json                        │
└─────────────────────────────────────────────────────────────┘
        │
        ▼
┌─────────────────────────────────────────────────────────────┐
│  MÓDULO 03 — Indexer                                        │
│  Skill: .claude/skills/index-cards/SKILL.md                │
│  Input:  working/split/card_batches/batch_*.md              │
│          working/split/split_manifest.json                  │
│  Output: working/index/card_index.jsonl (1 línea/card)      │
│          working/index/index_manifest.json                   │
│  Campos por card: id, round, observation, source, date,     │
│    source_type, domain, evidence_base, extraction_status,   │
│    entities[], figures[]                                     │
│  Resumable desde index_manifest.json                        │
└─────────────────────────────────────────────────────────────┘
        │
        ▼
┌─────────────────────────────────────────────────────────────┐
│  MÓDULO 04 — Scanner (7 operaciones independientes)         │
│                                                             │
│  Input para todas: working/index/card_index.jsonl           │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ scan-contradictions  → working/scans/contradictions │   │
│  │ .json  (9 patrones)                                 │   │
│  ├─────────────────────────────────────────────────────┤   │
│  │ scan-asymmetries     → working/scans/asymmetries    │   │
│  │ .json  (14 patrones)                                │   │
│  ├─────────────────────────────────────────────────────┤   │
│  │ scan-frictions       → working/scans/frictions      │   │
│  │ .json  (35 patrones)                                │   │
│  ├─────────────────────────────────────────────────────┤   │
│  │ scan-co-occurrences  → working/scans/co_occurrences │   │
│  │ .json  (8 patrones)                                 │   │
│  ├─────────────────────────────────────────────────────┤   │
│  │ scan-gaps            → working/scans/gaps.json      │   │
│  │ (7 patrones)                                        │   │
│  ├─────────────────────────────────────────────────────┤   │
│  │ scan-opposite-dirs   → working/scans/opposite       │   │
│  │ _directions.json (11 patrones)                      │   │
│  ├─────────────────────────────────────────────────────┤   │
│  │ scan-lexical-overlap → working/scans/lexical        │   │
│  │ _overlap.json (77 patrones)                         │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  Cada patrón recibe routing a uno de 5 destinos:           │
│    tension_candidate | needs_audit | rejected_grouping      │
│    coverage_gap | isolated_signal                           │
│                                                             │
│  Totales por routing (run actual):                          │
│    tension_candidate : 47 patrones                         │
│    needs_audit       : 85 patrones (77 LEX + 5 CON + 3 FRI)│
│    rejected_grouping :  1 patrón  (COO-007)                │
│    coverage_gap      :  7 patrones (todos de gaps)         │
│    isolated_signal   :  0 patrones                         │
└─────────────────────────────────────────────────────────────┘
        │
        ▼ (todos los scan artifacts)
┌─────────────────────────────────────────────────────────────┐
│  MÓDULO 05 — Candidate Builder                              │
│  Skill: .claude/skills/build-candidate/SKILL.md            │
│  Input:  working/scans/*.json (7 archivos)                  │
│          input/signal_cards_round_*.md (verificación IDs)   │
│          reference/TC-001.md (formato)                      │
│          reference/protocol_canonical.md                    │
│                                                             │
│  Pre-build filter:                                          │
│    LEX + <3 IDs → rejected_grouping (sin construir TC)     │
│    LEX + 3+ IDs sin fricción explícita → rejected_grouping │
│    no-LEX + <3 IDs → TC con "minimal support" en risk      │
│                                                             │
│  Deduplicación:                                             │
│    >70% IDs compartidos + mismo mecanismo → merge           │
│                                                             │
│  Outputs:                                                   │
│    output/tension_candidates/TC-NNN.md  (74 archivos)      │
│    output/tension_candidates/TC-NNN.json (74 archivos)     │
│    output/rejected_groupings.md                            │
│    output/coverage_gaps.md                                 │
│    output/isolated_signals.md                              │
│    output/review_queue.md                                  │
└─────────────────────────────────────────────────────────────┘
        │
        ▼
┌─────────────────────────────────────────────────────────────┐
│  MÓDULO 06 — Validator                                      │
│  Skill: .claude/skills/validate-candidate/SKILL.md         │
│  Input:  output/tension_candidates/TC-*.md                  │
│          reference/protocol_canonical.md                    │
│          schemas/tension_candidate.schema.json              │
│                                                             │
│  16 checks por TC                                           │
│  No descarta. Solo reporta.                                 │
│                                                             │
│  Output:                                                    │
│    working/validation/candidate_reports/TC-NNN_validation   │
│    .json (74 archivos)                                      │
│    working/validation/validation_summary.json               │
│    output/review_queue.md (actualizado)                     │
└─────────────────────────────────────────────────────────────┘
        │
        ▼
PUNTO FINAL — Listo para revisión humana

  output/tension_candidates/   74 TCs (71 pass, 3 fail mecánico)
  output/rejected_groupings.md  COO-007 + 77 LEX (78 entradas)
  output/coverage_gaps.md       7 gaps
  output/isolated_signals.md    vacío (0 señales aisladas)
  output/review_queue.md        índice con estado de validación
```

---

## Tabla de destinos por scan (run actual)

| Scan | Total patrones | tension_candidate | needs_audit | rejected_grouping | coverage_gap | isolated_signal |
|------|---------------|-------------------|-------------|-------------------|--------------|-----------------|
| contradictions | 9 | 4 | 5 | 0 | 0 | 0 |
| asymmetries | 14 | 14 | 0 | 0 | 0 | 0 |
| frictions | 35 | 32 | 3 | 0 | 0 | 0 |
| co_occurrences | 8 | 7 | 0 | 1 | 0 | 0 |
| gaps | 7 | 0 | 0 | 0 | 7 | 0 |
| opposite_directions | 11 | 11 | 0 | 0 | 0 | 0 |
| lexical_overlap | 77 | 0 | 77 | 0 | 0 | 0 |
| **Total** | **161** | **68** | **85** | **1** | **7** | **0** |

Los 85 `needs_audit` pasaron por el pre-build filter del builder:
- 77 LEX → todos a `rejected_groupings.md`
- 5 CON → todos a TCs con status `needs_audit_before_classification`
- 3 FRI → todos a TCs con status `needs_audit_before_classification`

---

## TCs por scan de origen (run actual)

| Scan origen | TCs producidos | Rango ID |
|-------------|---------------|----------|
| CON (contradicciones) | 9 | TC-002 a TC-005, TC-031 a TC-035 |
| OPP (direcciones opuestas) | 11 | TC-006 a TC-017 |
| ASY (asimetrías) | 14 | TC-018 a TC-030 |
| FRI (fricciones) | 35 | TC-036 a TC-068, TC-040* |
| COO (co-ocurrencias) | 7 | TC-069 a TC-075 |

*TC-040 tiene source_patterns `['FRI-005', 'FRI-029']` (merge).
*TC-037 tiene source_patterns `['FRI-002', 'FRI-034']` (merge).

TC-001 preexiste. El builder empieza en TC-002.

---

## Notas sobre la implementación

El pipeline no está implementado como código ejecutable (no hay scripts Python
para los pasos 01–06). La implementación es el agente `inventory-mapping`
(`.claude/agents/inventory-mapping.md`) operando como LLM que lee cada módulo
y ejecuta la skill correspondiente. No hay proceso autónomo — cada paso es una
invocación del agente siguiendo instrucciones escritas en markdown.

El único script presente en el repo es `scripts/parse_dg_shard.py`, que
corresponde a un paso upstream (data gathering) y no participa en el pipeline
de Inventory Mapping.

[proceso no identificado]: No existe código que valide que el entry gate se
ejecutó antes del splitter más allá de la lectura del report en el módulo.
La secuencia es declarativa, no enforced por un orquestador.
