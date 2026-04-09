# Seccion 4 — Como operan los skills

## 1. entry-gate

- **Path:** `.claude/skills/entry-gate/SKILL.md`
- **Primera linea:** `# Entry Gate — Skill`
- **Modulo que ejecuta:** `modules/01_entry_gate.md`
- **Instrucciones principales:** Listar los 10 archivos signal_cards_round_*.md, parsear cards por delimitador `---`, contar cards por round, correr 5 checks del modulo, escribir `working/entry_gate/entry_gate_report.json`. Si status es "fail", parar el pipeline.
- **Incrementalidad/retoma/checkpoints:** No menciona ninguno.

## 2. split-cards

- **Path:** `.claude/skills/split-cards/SKILL.md`
- **Primera linea:** `# Split Cards — Skill`
- **Modulo que ejecuta:** `modules/02_splitter.md`
- **Instrucciones principales:** Leer `split_manifest.json` si existe (retoma), procesar cada round file splitting cards en batches de ~25, escribir batches a `working/split/card_batches/batch_R{round}_{batch_num}.md`, actualizar manifest con cards_found/batches_written/status. Verificar total = 1,560.
- **Incrementalidad/retoma/checkpoints:** SI.
  - Lee manifest al inicio para retomar.
  - Si un round ya tiene status `complete`, lo salta.
  - Actualiza manifest despues de cada round.
  - Granularidad de checkpoint: **por round**.

## 3. index-cards

- **Path:** `.claude/skills/index-cards/SKILL.md`
- **Primera linea:** `# Index Cards — Skill`
- **Modulo que ejecuta:** `modules/03_indexer.md`
- **Instrucciones principales:** Leer `index_manifest.json` si existe (retoma), leer `split_manifest.json` para obtener lista de batches, procesar cada batch extrayendo campos (id, round, observation, source, date, source_type, domain, evidence_base, extraction_status, entities, figures), validar contra schema, appendear a `card_index.jsonl`, actualizar manifest.
- **Incrementalidad/retoma/checkpoints:** SI.
  - Lee manifest al inicio para retomar.
  - Salta batches ya procesados segun manifest.
  - Registra `last_batch_processed`, `batches_processed`, `cards_indexed`.
  - Registra errores en manifest issues sin detener el proceso.
  - Granularidad de checkpoint: **por batch**.

## 4. scan-contradictions

- **Path:** `.claude/skills/scan-contradictions/SKILL.md`
- **Primera linea:** `# Scan Contradictions — Skill`
- **Modulo que ejecuta:** `modules/04_scanner.md` (seccion: Contradictions)
- **Instrucciones principales:** Cargar card_index.jsonl, agrupar cards por entidades/topics compartidos, encontrar pares con observaciones opuestas explicitas sobre el mismo sujeto. Routing: 2+ cards por lado → `tension_candidate`; un lado con 1 card → `needs_audit`; overlap tematico sin oposicion → `rejected_grouping`. Escribir `working/scans/contradictions.json`.
- **Incrementalidad/retoma/checkpoints:** No menciona ninguno. Pasada unica.

## 5. scan-asymmetries

- **Path:** `.claude/skills/scan-asymmetries/SKILL.md`
- **Primera linea:** `# Scan Asymmetries — Skill`
- **Modulo que ejecuta:** `modules/04_scanner.md` (seccion: Asymmetries)
- **Instrucciones principales:** Cargar card_index.jsonl, identificar ejes con distribucion desigual (seller outcomes, platform fees, product pricing, category volume, geographic coverage), encontrar cards en ambos extremos (min 2 per polo), definir polos en terminos del corpus. Nota: TC-001 ya cubre seller income asymmetry; no producir duplicado.
- **Incrementalidad/retoma/checkpoints:** No menciona ninguno. Pasada unica.

## 6. scan-frictions

- **Path:** `.claude/skills/scan-frictions/SKILL.md`
- **Primera linea:** `# Scan Frictions — Skill`
- **Modulo que ejecuta:** `modules/04_scanner.md` (seccion: Frictions)
- **Instrucciones principales:** Cargar card_index.jsonl, encontrar patrones donde algo documentado bloquea/encarece algo documentado. Identificar blocker y blocked con soporte de cards (min 2 total). Routing: ambos lados documentados + mecanismo claro → `tension_candidate`; mecanismo unclear o single-card → `needs_audit`; quejas sin mecanismo → `rejected_grouping`.
- **Incrementalidad/retoma/checkpoints:** No menciona ninguno. Pasada unica.

## 7. scan-co-occurrences

- **Path:** `.claude/skills/scan-co-occurrences/SKILL.md`
- **Primera linea:** `# Scan Co-occurrences — Skill`
- **Modulo que ejecuta:** `modules/04_scanner.md` (seccion: Co-occurrences)
- **Instrucciones principales:** Cargar card_index.jsonl, encontrar sets de 3+ cards co-ocurriendo alrededor del mismo topic/entity en 2+ rounds/sources. Test DT: si el cluster genera pregunta DT → `tension_candidate`; si no → `rejected_grouping`. Frecuencia pura no cuenta.
- **Incrementalidad/retoma/checkpoints:** No menciona ninguno. Pasada unica.

## 8. scan-gaps

- **Path:** `.claude/skills/scan-gaps/SKILL.md`
- **Primera linea:** `# Scan Gaps — Skill`
- **Modulo que ejecuta:** `modules/04_scanner.md` (seccion: Gaps)
- **Instrucciones principales:** Cargar card_index.jsonl, analizar cobertura por dominio/plataforma/product type/perspectiva (seller/buyer/platform), identificar areas con ausencia esperada. Verificar contra 7 dimensiones: buyer perspective, geographic, product types, platforms, income range, temporal, post-purchase. Todas las gaps se routean como `coverage_gap`.
- **Incrementalidad/retoma/checkpoints:** No menciona ninguno. Pasada unica.

## 9. scan-opposite-directions

- **Path:** `.claude/skills/scan-opposite-directions/SKILL.md`
- **Primera linea:** `# Scan Opposite Directions — Skill`
- **Modulo que ejecuta:** `modules/04_scanner.md` (seccion: Opposite directions)
- **Instrucciones principales:** Cargar card_index.jsonl, encontrar pares de fuerzas/tendencias empujando en direcciones contrarias sobre el mismo sistema. Ambas fuerzas deben actuar sobre el mismo dominio con min 2 cards soporte. Distinguir de contradiccion: no es sobre el mismo hecho sino sobre fuerzas diferentes actuando en el mismo sistema.
- **Incrementalidad/retoma/checkpoints:** No menciona ninguno. Pasada unica.

## 10. scan-lexical-overlap

- **Path:** `.claude/skills/scan-lexical-overlap/SKILL.md`
- **Primera linea:** `Scan Lexical Overlap — Skill`
- **Modulo que ejecuta:** `modules/04_scanner.md` (seccion: Lexical overlap)
- **Instrucciones principales:** Cargar card_index.jsonl, encontrar cards que comparten vocabulario/entidades significativas. Regla critica: el default es `rejected_grouping`, NO `needs_audit`. Solo `tension_candidate` si hay friccion explicita entre las cards. Cards repitiendo la misma cifra de distintos rounds son senales de deduplicacion, no tensiones. Existe para awareness de deduplicacion.
- **Incrementalidad/retoma/checkpoints:** No menciona ninguno. Pasada unica.

## 11. build-candidate

- **Path:** `.claude/skills/build-candidate/SKILL.md`
- **Primera linea:** `Build Candidate — Skill`
- **Modulo que ejecuta:** `modules/05_candidate_builder.md`
- **Instrucciones principales:** Recolectar patrones ruteados de todos los `working/scans/*.json`. Pre-build filter para needs_audit (lexical_overlap con <3 IDs o sin friccion → rejected). Deduplicar (>70% overlap de signal_ids + mismo mecanismo → merge). Construir cada TC: verificar Signal IDs contra input/, card-polo relevance check, construir markdown con formato TC-001, validar contra schema, escribir a `output/tension_candidates/TC-NNN.md`. Construir outputs secundarios (rejected_groupings.md, coverage_gaps.md, isolated_signals.md, review_queue.md). Reglas detalladas campo por campo (definition vs mechanical_summary, unit_used, analytical_unit, signal ID descriptions, what_it_supports, additional_context).
- **Incrementalidad/retoma/checkpoints:** No menciona ninguno. Construye todos los TCs desde cero en cada ejecucion. No hay logica de "skip if TC already exists".

## 12. validate-candidate

- **Path:** `.claude/skills/validate-candidate/SKILL.md`
- **Primera linea:** `Validate Candidate — Skill`
- **Modulo que ejecuta:** `modules/06_validator.md`
- **Instrucciones principales:** Cargar `reference/protocol_canonical.md` y schema. Para cada TC en `output/tension_candidates/`, correr 16 checks (signal_ids verified, candidate generation rules, corpus-term polos, units declared, supports distinction, rejected_groupings exist, coverage_gaps reported, mechanical language, type matches relation, signal IDs spot-check, human fields empty, schema valid, mechanical_summary != definition, unit_used specific, what_it_supports not template, card-polo relevance spot check). Escribir reporte por TC y summary agregado. No arregla, solo reporta.
- **Incrementalidad/retoma/checkpoints:** Produce reportes por TC (`TC-NNN_validation.json`), pero no tiene logica para saltar TCs ya validados. No menciona "resume", "manifest", ni "checkpoint".

---

## Resumen de incrementalidad

| Skill | Checkpoint | Granularidad |
|---|---|---|
| entry-gate | No | N/A |
| split-cards | SI (manifest) | Por round |
| index-cards | SI (manifest) | Por batch |
| scan-contradictions | No | N/A |
| scan-asymmetries | No | N/A |
| scan-frictions | No | N/A |
| scan-co-occurrences | No | N/A |
| scan-gaps | No | N/A |
| scan-opposite-directions | No | N/A |
| scan-lexical-overlap | No | N/A |
| build-candidate | No | N/A |
| validate-candidate | No | N/A |

Solo 2 de 12 skills tienen soporte de retoma: `split-cards` y `index-cards`.
