# E-VAL2-S36 — Productores de `validation_status` (superficie completa de ejecutores)

BASE: `af27ae95f97d58990bd8fbd2747822777ddbfcec` (`origin/main`, tras `git fetch --prune origin`).

Estado shallow: al iniciar, `git rev-parse --is-shallow-repository` → `true`. Se ejecutó
`git fetch --unshallow origin`; tras eso, `git rev-parse --is-shallow-repository` → `false`.
Todo lo que sigue (incluida la Pregunta 8) corre sobre historia completa, no shallow.

**Si el BASE de arriba no es el vigente, este archivo es procedencia, no evidencia.**

Rama de trabajo: `claude/inventory-mapping-execution-czdib2`. El nombre no existía en
`origin` al empezar (`git log -1 origin/claude/inventory-mapping-execution-czdib2` →
`unknown revision`); se creó localmente desde BASE (`git checkout -B
claude/inventory-mapping-execution-czdib2 af27ae95f97d58990bd8fbd2747822777ddbfcec`).

Capa de cada hallazgo: **[medido-por-mí]** en todo el archivo. Se lanzó un
sub-agente en paralelo sobre la misma pregunta (mismo BASE, mismo árbol). Su salida
se trató como procedencia, no como evidencia: cada afirmación suya que este archivo
incorpora fue re-ejecutada de forma independiente por esta sesión antes de citarse
(la cobertura de ramas `etapa-2` en la Pregunta 8, la confirmación de rename puro
vía `-M` en la Pregunta 8, la ausencia de `input/signal_cards_round_*.md` en la
Pregunta 5, y la ausencia de imports de `jsonschema` en la Pregunta 9). El resto del
sub-agente convergió con lo ya medido de forma independiente en este archivo, sin
contradicción, y no se cita porque no agrega nada no re-derivado ya aquí. Ningún
hallazgo de este archivo queda en la categoría "de sub-agente, no re-medido" — esa
categoría no aparece porque nada quedó sin re-medir.

**Sobre el ANCLA A FALSEAR** ([CONVERSACIÓN DSC] — procedencia, no evidencia: "se
afirmó cero productores y cero consumidores en todo el historial"): no se hereda.
Ver contraste explícito al cierre de la Pregunta 8 y en VEREDICTO — la respuesta
medida coincide en el campo literal (nunca escrito, por nadie, en ningún tipo de
archivo) pero la matiza: uno de los tres validadores de juicio semántico sí tiene
ejecutor implementado hoy (Fase 2), aunque ese ejecutor nunca persiste el campo bajo
ese nombre. "Cero productores del campo" es correcto; "cero ejecución de trabajo de
validación" no lo es.

---

## 1. Superficie de ejecutores

Comando base:
```
$ find .claude/skills -name "SKILL.md" | sort
$ find . -name "*.py" -not -path "./.git/*" | sort
$ find agents -type f | sort
$ cat .github/workflows/ci.yml .github/workflows/state-snapshot.yml
```

### 1.1 — Skills (`.claude/skills/*/SKILL.md`, 16 archivos — LLM, no código)

| Ruta | Fase / propósito (una línea) |
|---|---|
| `.claude/skills/p0-normalize-shard/SKILL.md` | Phase 0 — normaliza un shard de deep_search a findings |
| `.claude/skills/p1-convert-findings/SKILL.md` | Phase 1a stage 2 — skeleton → Source Packet completo (ejecuta `modules/converter.md`) |
| `.claude/skills/p1-extract-records/SKILL.md` | Phase 1b stage 2 — skeleton → Extraction Record completo (ejecuta `modules/extraction_converter.md`) |
| `.claude/skills/p2-extract-signals/SKILL.md` | Phase 2 stage 2 — skeleton → Signal Card completo; **incluye la ejecución embebida de los 11 checks de `signal_extraction_validator.md`** (ver Pregunta 2) |
| `.claude/skills/entry-gate/SKILL.md` | IM step 1 — gate sobre `input/signal_cards_round_*.md` (markdown); 5 checks propios, ninguno es `validation_status` (ver Pregunta 5) |
| `.claude/skills/split-cards/SKILL.md` | IM step 2 — divide cards en unidades atómicas |
| `.claude/skills/index-cards/SKILL.md` | IM step 3 — construye `working/index/card_index.jsonl` |
| `.claude/skills/scan-asymmetries/SKILL.md` | IM step 4 — scan de asimetrías |
| `.claude/skills/scan-co-occurrences/SKILL.md` | IM step 4 — scan de co-ocurrencias |
| `.claude/skills/scan-contradictions/SKILL.md` | IM step 4 — scan de contradicciones |
| `.claude/skills/scan-frictions/SKILL.md` | IM step 4 — scan de fricciones |
| `.claude/skills/scan-gaps/SKILL.md` | IM step 4 — scan de vacíos |
| `.claude/skills/scan-lexical-overlap/SKILL.md` | IM step 4 — scan de solapamiento léxico |
| `.claude/skills/scan-opposite-directions/SKILL.md` | IM step 4 — scan de direcciones opuestas |
| `.claude/skills/build-candidate/SKILL.md` | IM step 5 — construye Tension Candidates en `output/` |
| `.claude/skills/validate-candidate/SKILL.md` | IM step 6 — valida TCs contra `validation_report.schema.json` (campo `passed`, booleano — **no** `validation_status`; ver nota Pregunta 4) |

### 1.2 — Scripts Python (18 archivos)

| Ruta | Fase / propósito |
|---|---|
| `phases/00-data-gathering/scripts/eje4_xlsx_to_json_batch.py` | Phase 0 — xlsx Eje4 → JSON por batch |
| `phases/00-data-gathering/scripts/parse_dg_shard.py` | Phase 0 — parser de shards → findings |
| `phases/00-data-gathering/scripts/part4_to_recovery_packets.py` | Phase 0 — diagnósticos Part 4 → recovery packets |
| `phases/01-source-intake/scripts/converter_prepare.py` | Phase 1a stage 1 — findings → skeletons |
| `phases/01-source-intake/scripts/route_unrecoverable.py` | Phase 1a — rutea findings irrecuperables |
| `phases/01-source-intake/data-extraction/scripts/extraction_prepare.py` | Phase 1b stage 1 — Source Packets → skeletons |
| `phases/01-source-intake/data-extraction/scripts/bulk_extract.py` | Phase 1b — llena 15 campos de juicio algorítmicamente (implementa `data_extraction_contract.md`, no el validador) |
| `phases/01-source-intake/data-extraction/scripts/test_e5_fixtures.py` | Phase 1b — fixtures de regresión FICHA E5a/E5b |
| `phases/02-signal-extraction/scripts/signal_prepare.py` | Phase 2 stage 1 — Extraction Records → skeletons |
| `phases/02-signal-extraction/scripts/signal_to_markdown.py` | Phase 2 → IM — Signal Cards JSON → `input/signal_cards_round_*.md`. **Sin filtro por `validation_status` ni por decisión de gate** (ver Pregunta 5/6) |
| `signal_card_defect_check.py` (raíz) | Phase 2, QA mecánica standalone — 4 checks (`qualifier_overfill`, `time_scope_contamination`, `partial_discreteness`, `time_scope_loss`); ninguno es `validation_status` |
| `vocab_check.py` (raíz) | Cross-phase — compara `pipeline_vocabulary.yaml` contra todo `*.schema.json` |
| `state/scripts/etapa3_compare.py` | Meta/state — comparación determinista de dos corpus de re-extracción |
| `state/scripts/field_lifecycle_trace.py` | Meta/state — auditoría de ciclo de vida de campos (medición, no check) |
| `state/scripts/field_population_audit.py` | Meta/state — auditoría de población real de campos (medición, no check) |
| `state/scripts/generate_state.py` | Meta/state — genera `state/STATE.md` / `state/MAP.md` |
| `state/scripts/ledger_check.py` | Meta/state — invariantes estructurales de `state/pendientes_ledger.md` |
| `state/scripts/ledger_path_check.py` | Meta/state — verifica que rutas citadas en el ledger existan |

### 1.3 — Agentes (`agents/codex/**`, 11 archivos — contratos para agente Codex externo, no skills de Claude Code)

| Ruta | Fase / propósito |
|---|---|
| `agents/codex/phase0-eje4-discovery/{README,CONTRACT}.md` | Phase 0 — discovery Eje4 |
| `agents/codex/phase0-recovery/{README,CONTRACT}.md` + `prompts/production_v1.md` | Phase 0 — recovery de findings Part 4 |
| `agents/codex/phase1b-recovery/CONTRACT.md` | Phase 1b — recovery de Extraction Records |
| `agents/codex/source-intake-recovery/CONTRACT.md` | Phase 1a — recovery de Source Packets |
| `agents/codex/_shared/protocols/*.md` (4 archivos) | Protocolos compartidos de Phase 0, no específicos de una fase |

Ninguno de los 11 archivos bajo `agents/` menciona `validation_status` (confirmado en
Pregunta 3 vía grep de todo el árbol).

### 1.4 — CI / workflows (`.github/workflows/*.yml`, 2 archivos)

| Ruta | Jobs |
|---|---|
| `.github/workflows/ci.yml` | `vocab-check` (`vocab_check.py`), `signal-card-defect-check` (`signal_card_defect_check.py --fixtures`), `ledger-check` (`state/scripts/ledger_check.py`) |
| `.github/workflows/state-snapshot.yml` | Regenera `state/STATE.md`/`state/MAP.md` vía `generate_state.py` en cada push |

No se encontró ningún otro ejecutor invocable (sin `Makefile`, sin `package.json`,
sin otros directorios `scripts/` fuera de los listados):
```
$ find . -iname "Makefile" -o -iname "package.json" -not -path "./.git/*"
(0 resultados)
```

Esta es la lista contra la que se responden las Preguntas 2 y 3.

---

## 2. ¿Existe un validador ejecutable?

Comando:
```
$ grep -rn "source_intake_validator\|data_extraction_validator\|signal_extraction_validator" --include="*" . --exclude-dir=.git
$ grep -n -i "validat" .claude/skills/p1-convert-findings/SKILL.md .claude/skills/p1-extract-records/SKILL.md .claude/skills/p2-extract-signals/SKILL.md
$ grep -n -i "validat" phases/01-source-intake/modules/converter.md phases/01-source-intake/data-extraction/modules/extraction_converter.md phases/02-signal-extraction/modules/signal_converter.md
$ grep -rln "pass_with_flags\|parking_lot" --include="*" . --exclude-dir=.git
```

### 2.1 `phases/01-source-intake/contracts/source_intake_validator.md` — **NO EXISTE ejecutor**

El nombre del archivo aparece solo en: el propio contrato, `state/MAP.md` (índice de
rutas), `output/diagnostics/phase1_inventory_report.md` (diagnóstico histórico,
"solo documentado, no implementado como script", `output/diagnostics/phase1_inventory_report.md:209`),
`docs/pipeline_flow.md` (marcado OBSOLETO), y `state/output/verificacion_decisiones_S36.md:599`
(cita de una línea del contrato, no una referencia de ejecución).

`.claude/skills/p1-convert-findings/SKILL.md` y `phases/01-source-intake/modules/converter.md`
—el skill y módulo que sí corren Phase 1a stage 2— solo mencionan validación **de
schema** (`source_packet.schema.json`, `converter.md:113,115-117`). Cero ocurrencias
de la cadena `source_intake_validator` en ninguno de los dos. El vocabulario propio
del validador (`parking_lot`, único entre los 4 schemas de validador —
`source_intake_validation.schema.json:37`) no aparece en ningún skill/módulo/script.

**Veredicto: NO EXISTE ejecutor**, ni embebido ni standalone, para este contrato.

### 2.2 `phases/01-source-intake/data-extraction/contracts/data_extraction_validator.md` — **NO EXISTE ejecutor**

Mismo patrón que 2.1. `.claude/skills/p1-extract-records/SKILL.md` y
`phases/01-source-intake/data-extraction/modules/extraction_converter.md` solo
validan contra `data_extraction_record.schema.json` (schema del artefacto, no el
validador de 13 checks). Cero ocurrencias de `data_extraction_validator` en skill o
módulo. `output/diagnostics/phase1_inventory_report.md:210`: "Solo documentado, no
implementado como script" — confirmado, y ampliado aquí: tampoco como skill.

**Veredicto: NO EXISTE ejecutor.**

### 2.3 `phases/02-signal-extraction/contracts/signal_extraction_validator.md` — **EXISTE, embebido (no standalone)**

`.claude/skills/p2-extract-signals/SKILL.md:17,42`:
```
17: 3. `phases/02-signal-extraction/contracts/signal_extraction_validator.md` — all 11 validator checks, decision rules, failure severity guide, and the mandatory notes scrubbing step
42: 7. **Apply validator checks** (all 11 from signal_extraction_validator.md). If check 11 (Notes Locality) triggers, apply the mandatory scrubbing step before routing. Record all flag codes and failure codes in issues.
```
`phases/02-signal-extraction/modules/signal_converter.md:191`:
```
191: **4.5 Apply validator checks.** Run the completed card through all 11 checks in `phases/02-signal-extraction/contracts/signal_extraction_validator.md`:
```
El skill lee el contrato del validador como lectura obligatoria (§"Mandatory
reading") y ejecuta sus 11 checks como paso 7 de su loop (`SKILL.md:42-49`), dentro
del mismo run que produce la card (no un paso posterior ni un script separado).

**Veredicto: EXISTE, pero embebido dentro de `p2-extract-signals`, no como
validador standalone.** Es el único de los tres contratos con ejecutor real. Ver
Pregunta 6 para qué pasa con el veredicto que ese ejecutor calcula.

---

## 3. Productores declarados

Comando:
```
$ grep -rn "validation_status" --include="*" . --exclude-dir=.git
```

Salida completa (14 líneas, ya deduplicada por archivo):

```
phases/02-signal-extraction/schemas/signal_inventory_gate.schema.json:12,32,55,65
phases/02-signal-extraction/schemas/signal_validation.schema.json:12,31
phases/02-signal-extraction/contracts/signal_to_inventory_entry_gate.md:320,330
phases/02-signal-extraction/contracts/signal_extraction_contract.md:34
phases/01-source-intake/schemas/source_intake_validation.schema.json:12,31
phases/01-source-intake/data-extraction/schemas/data_extraction_validator.schema.json:12,31
state/output/vocab_check_blind_spots.md:199,209,215,220,224
state/pendientes_ledger.md:46,90
docs/pipeline_flow.md:322
```

Declaraciones normativas (no schema, no ledger/medición) que nombran `validation_status`:

1. **`phases/02-signal-extraction/contracts/signal_extraction_contract.md:34`**
   (Phase 2, condición de entrada): *"Solo deben entrar: records con
   `validation_status = pass`, o `pass_with_flags`."* — declara que Phase 2 espera
   recibir el campo ya poblado desde Phase 1b. **Declarado, no implementado**: el
   productor que este consumidor asume (Pregunta 2.2) no existe.

2. **`phases/02-signal-extraction/contracts/signal_to_inventory_entry_gate.md:315-337`**
   ("Gate report structure", check 1 = "Validation status check", líneas 66-82):
   declara que G1 debe leer `validation_status` de la Signal Card y reproducirlo en
   su propio reporte (`"validation_status": "pass_with_flags"` en el ejemplo, línea
   330). **Declarado, no implementado**: G1 no tiene ejecutor (Pregunta 5).

3. Los 4 schemas de validador (`signal_inventory_gate.schema.json`,
   `signal_validation.schema.json`, `source_intake_validation.schema.json`,
   `data_extraction_validator.schema.json`) declaran el campo como `required` en su
   propia forma de salida — pero un schema que declara la forma de su propia salida
   no es, por sí mismo, una declaración de quién produce esa salida. Es forma sin
   productor nombrado.

No se encontró ningún módulo, skill o README que nombre explícitamente **qué script
o skill concreto** debe escribir el campo, más allá de referirse genéricamente a "el
validador" o "Signal Extraction Validation Results". Para Phase 2, "el validador" sí
tiene ejecutor (§2.3) pero ese ejecutor no persiste el campo (§6). Para Phase 1a/1b,
ni siquiera hay ejecutor al que atribuirle la omisión.

`state/pendientes_ledger.md:90` (P-097, fila existente, citada aquí solo como
[repo@BASE] — archivo en el árbol, no como verdad heredada): *"Phase 1b corrió sin
validador (D-140). Diagnóstico corregido en S28: la ausencia de `validation_status`
es conformidad con el schema"* — consistente con lo medido de forma independiente
en la Pregunta 4.

---

## 4. El schema del artefacto

Comando:
```
$ find . -name "signal_card.schema.json" -o -name "card_record.schema.json" -o -name "source_packet.schema.json" -o -name "data_extraction_record.schema.json"
```

Las 4 rutas existen:
- `phases/02-signal-extraction/schemas/signal_card.schema.json`
- `phases/03-inventory-mapping/schemas/card_record.schema.json`
- `phases/01-source-intake/schemas/source_packet.schema.json`
- `phases/01-source-intake/data-extraction/schemas/data_extraction_record.schema.json`

| Schema | `additionalProperties` | `validation_status` en `required`? | `validation_status` en `properties`? |
|---|---|---|---|
| `signal_card.schema.json` | `false` (línea 7) | No (required: líneas 8-30, 21 campos, no incluye el campo) | No (properties: líneas 31-324) |
| `card_record.schema.json` | **no declarado** (schema draft-07, sin la key en absoluto — por omisión, JSON Schema permite propiedades extra) | No (required: línea 6, 8 campos) | No (properties: líneas 7-61) |
| `source_packet.schema.json` | `false` (línea 7) | No (required: líneas 8-29, 20 campos) | No (properties: líneas 30-230) |
| `data_extraction_record.schema.json` | `false` (línea 7) | No (required: líneas 8-36, 27 campos) | No (properties: líneas 37-396) |

Fragmento literal, `signal_card.schema.json:6-30`:
```json
  "type": "object",
  "additionalProperties": false,
  "required": [
    "signal_id", "source_record_ids", "source_ids", "round", "signal_text",
    "subject_exact", "actor_level", "platforms", "product_type_if_explicit",
    "metric_type", "metric_value_raw", "metric_unit", "time_scope_raw",
    "time_scope_normalized_if_safe", "geography_if_explicit", "evidence_role",
    "local_qualifiers", "uncertainties", "traceability_pointers",
    "normalization_notes", "extraction_notes"
  ],
```

**Lo que se juega, medido:** confirmado. `signal_card.schema.json` declara
`additionalProperties: false` y no incluye `validation_status` en ninguna parte de
`properties`. Una Signal Card que valide contra su propio schema **no puede** llevar
ese campo — no es una omisión de implementación, es una prohibición estructural. G1
check 1 (Pregunta 5) lee un campo que la card no puede portar legalmente. Confirmado
también de forma empírica sobre los datos reales (no solo el schema): `grep -l
validation_status working/signal_extraction/cards/*.json` → 0 archivos, sobre 29
cards existentes.

`card_record.schema.json` es el único de los cuatro sin `additionalProperties:
false` explícito — técnicamente no *prohíbe* el campo por schema, pero tampoco lo
declara, documenta ni lo tiene como `required`. Esto es una asimetría real entre los
cuatro schemas de artefacto que vale la pena registrar sin resolver: los otros tres
cierran la puerta; este la deja sin marco.

`card_record.schema.json` es, además, un artefacto de un momento distinto del
pipeline (indexado por `.claude/skills/index-cards/SKILL.md`, IM step 3, ya dentro
de Inventory Mapping) — no recibe directamente el Signal Card de Phase 2, sino una
proyección de él (`id, round, observation, source, ...`), así que su falta de
`additionalProperties: false` no reabre una vía para que `validation_status`
sobreviva desde Phase 2: nada en el índice copia ese campo porque nada lo produce
antes.

---

## 5. La compuerta (G1)

Comando:
```
$ grep -rln "signal_to_inventory_entry_gate" --include="*" . --exclude-dir=.git
$ cat phases/02-signal-extraction/schemas/signal_inventory_gate.schema.json   # checks.required
$ cat .claude/skills/entry-gate/SKILL.md phases/03-inventory-mapping/modules/01_entry_gate.md
```

**¿Existe ejecutor de G1?** Referencias al nombre exacto del contrato
(`signal_to_inventory_entry_gate`):
```
./state/MAP.md
./docs/pipeline_flow.md
```
Solo un índice de rutas auto-generado y un documento marcado OBSOLETO
(`docs/pipeline_flow.md:3-4`: *"OBSOLETO — describe la estructura pre-restructure
242318b. CLAUDE.md es el mapa vivo."*). **Ningún skill, script o agente referencia
este contrato por nombre. NO EXISTE ejecutor de G1**, ni embebido ni standalone.

Existe un skill llamado `entry-gate` (`.claude/skills/entry-gate/SKILL.md`), pero es
**un gate distinto**: opera sobre `input/signal_cards_round_*.md` (markdown, ya
post-bridge), no sobre las Signal Cards JSON de `working/signal_extraction/cards/`
que G1 tendría que gatear. Sus 5 checks (`discrete_cards`, `no_interpretation`,
`no_meta_observations`, `evidence_preserved`, `ids_traceable` —
`.claude/skills/entry-gate/SKILL.md:18-24`) no incluyen `validation_status`. Es el
Entry Gate de **Inventory Mapping** (step 1 de 6, per `CLAUDE.md`), corriente abajo
de donde G1 debería correr — no es G1.

Confirmado además que el puente mecánico real (`signal_to_markdown.py`, el único
script que convierte JSON → markdown) no aplica ningún filtro equivalente a G1:
```
$ grep -n "validation_status\|filter\|pass_to_inventory\|entry_gate" phases/02-signal-extraction/scripts/signal_to_markdown.py
(0 resultados en ninguna de esas cadenas)
$ grep -n "cards_dir.glob" phases/02-signal-extraction/scripts/signal_to_markdown.py
363:    json_files = sorted(cards_dir.glob("*.json"))
```
El script toma **todas** las cards de `cards/` sin condición. La función de gateo
que G1 describe no se ejecuta en ningún punto del pipeline mecánico actual.

**Los 8 checks — campo, existencia en schema, población en las 29 cards reales:**

Comando de población:
```python
python3 -c "
import json, glob
cards = sorted(glob.glob('working/signal_extraction/cards/*.json'))
... # ver campos citados abajo
"
```

| # | Check | Campo(s) que lee | ¿Existe en `signal_card.schema.json`? | Población en 29 cards reales |
|---|---|---|---|---|
| 1 | `validation_status_check` | `validation_status` | **No** | 0/29 (la clave no existe en ningún archivo) |
| 2 | `discreteness_check` | (sin campo único — juicio estructural sobre la card completa) | N/A | N/A |
| 3 | `observational_boundary_check` | `signal_text` | Sí (required) | 29/29 no-nulo |
| 4 | `subject_exactness_check` | `subject_exact` | Sí (required) | 29/29 no-nulo |
| 5 | `actor_level_check` | `actor_level` | Sí (required) | 29/29 no-nulo |
| 6 | `time_and_qualifier_check` | `time_scope_raw`, `local_qualifiers` | Sí (ambos required, `time_scope_raw` nullable) | `time_scope_raw`: 7/29 no-nulo, 22/29 `null` (válido por schema); `local_qualifiers`: 29/29 presente como array |
| 7 | `cross_source_contamination_check` | (sin campo único — juicio semántico sobre `signal_text`/`source_ids`) | N/A | N/A |
| 8 | `pattern_readiness_check` | (sin campo único — juicio holístico) | N/A | N/A |

Adicional, verificado directamente: el output físico que G1 debería gatear —
`input/signal_cards_round_*.md`— **no existe hoy en el árbol de trabajo**:
```
$ find . -iname "signal_cards_round_*.md" -not -path "./.git/*"
(0 resultados)
$ ls input/
data_gathering
$ ls working/entry_gate/
.gitkeep
```
Consistente con que G1 nunca corrió en el ciclo actual: no solo no hay ejecutor
(arriba), tampoco hay el artefacto que ese ejecutor tendría que producir/filtrar.
(`working/entry_gate/entry_gate_report.json` tampoco existe — el skill downstream de
IM step 1 tampoco ha corrido sobre este corpus.)

**Lectura:** el check 1 es el único de los 8 cuyo campo nombrado está enteramente
ausente del schema de la card. Los otros tres checks con campo identificable (3, 4,
5, y parcialmente 6) tienen su campo declarado y poblado en el 100% de los casos
existentes (con la excepción esperada y válida de `time_scope_raw` nulo cuando el
snippet no trae fecha). Los tres restantes (2, 7, 8) no se atan a un campo único —
son juicio sobre la card completa, no lecturas de una propiedad. **El check 1 es un
caso aislado, no el patrón general** de los 8 checks de G1.

---

## 6. Fase a medias — ¿la reanudación escribiría el campo?

Comando:
```
$ cat working/signal_extraction/signal_converter_manifest.json | head -15
```
```json
{
  "status": "in_progress",
  "round": 1,
  "total_skeletons_found": 1178,
  "skeletons_processed": 25,
  "cards_written": 29,
  ...
}
```

`phases/02-signal-extraction/modules/signal_converter.md` describe el paso de
validador (§4.5, línea 191) **dentro del mismo loop por skeleton** que produce la
card (§4.4 formula la card, §4.5 valida, §4.7 valida contra schema, §4.8 escribe).
No es una fase posterior separada — es el mismo paso, en la misma corrida, para cada
skeleton. La sección "Resumability" (`signal_converter.md:313-324`,
`p2-extract-signals/SKILL.md:111-119`) especifica que reanudar significa: leer el
manifest, saltar skeletons ya en `processed_skeletons`, y continuar **el mismo
loop** (pasos 4.1 a 4.9 / pasos 1 a 12) sobre los skeletons restantes.

La tabla de Outputs del módulo (`signal_converter.md:25-31`) declara exactamente 3
artefactos de salida: `cards/<signal_id>.json`, `signal_gpt_recovery/<signal_id>.json`,
y `signal_converter_manifest.json`. Ninguno de los tres es un archivo con la forma
de `signal_validation.schema.json` (`validation_id`, `signal_id`, `validator_version`,
`validation_status`, `checks`, `failures`, `notes`, `validated_at`). El veredicto que
el paso 4.5 calcula (`pass`/`pass_with_flags`/`rework`/`reject`) se usa únicamente
para decidir el routing del paso 4.7-4.8 (`signal_converter.md:207-211`:
*"After all checks: `pass` → proceed to schema validation; ... `rework` → do not
write to `cards/`..."*) y luego se descarta — no hay instrucción, en ningún paso del
1 al 12 del skill o del 4.1 al 4.9 del módulo, de persistir ese veredicto en un
campo `validation_status` en ningún archivo.

**Respuesta explícita:** no, la ausencia de `validation_status` hoy **no** es "aún
no le toca" en el sentido de una fase de validación planeada para después de la
conversión. La validación semántica (paso 4.5) ya corre, hoy, por cada una de las 25
skeletons procesadas — es concurrente con la escritura de la card, no posterior.
Reanudar la corrida (25 → 1178) ejecutaría el mismo paso 4.5 sobre los skeletons
restantes, con el mismo resultado: el veredicto se calcula y se consume para
enrutar, pero nunca se escribe bajo el nombre `validation_status` en ningún
artefacto. Reanudar perpetuaría el patrón actual, no lo cerraría.

---

## 7. Vocabulario y cobertura

Comando:
```
$ grep -n "validation_status\|validator" pipeline_vocabulary.yaml
$ python3 vocab_check.py
```

`pipeline_vocabulary.yaml` **no** declara `validation_status` como key de primer
nivel. Las únicas dos ocurrencias de la cadena "validat" en el archivo son
comentarios explicativos del campo `check_status` (líneas 310-311, 316-317):
```yaml
310: # =============================================================================
311: # CROSS-PHASE OPERATIONAL FIELDS
...
316: check_status:
317:   # Called "status" inside each checks.<check_name> entry (checkResult.$defs)
318:   # in the Phase 1/2 validator and gate schemas.
```
`check_status` (el `status` interno de cada `checkResult`, valores
`pass|flag|fail|not_applicable`) **no es el mismo campo** que `validation_status`
(el veredicto agregado por card, valores `pass|pass_with_flags|rework|reject|
parking_lot`). Son dos campos distintos con vocabularios distintos; solo el primero
está en `pipeline_vocabulary.yaml`.

`vocab_check.py:244`, `for field_name, entry in vocab.items()` — el loop principal
solo visita keys que existen en `pipeline_vocabulary.yaml`. Como `validation_status`
no es una key ahí, **nunca se visita**, en ninguna dirección. Confirmado
ejecutando el script en vivo sobre el árbol en BASE:
```
$ python3 vocab_check.py
Schema files scanned: 20
Vocabulary fields checked: 20 (with schema occurrences), 3 with no matching schema field
...
CLEAN FIELDS: actor, metric_type, ..., check_status, manifest_status
VOCAB FIELDS WITH NO MATCHING SCHEMA FIELD FOUND: verification_status, allowed_verbs, forbidden_language
(exit code 0)
```
`validation_status` no aparece en ninguna de las cuatro secciones de salida — ni
siquiera en "sin schema field", porque esa lista solo contiene *keys del vocabulario*
sin ocurrencia en schemas, y `validation_status` nunca fue una key del vocabulario
para empezar. Es invisible al script de una forma más completa que "no cubierto":
no existe como concepto para la herramienta.

**Reporte de puntos ciegos ya existente:** `state/output/vocab_check_blind_spots.md`,
Bloque 2 (líneas 191-229), lista 24 propiedades con `enum` en 13 schemas que
`vocab_check.py` no visita porque no son key del vocabulario. `validation_status` es
una de las 24, citada explícitamente en 4 archivos (líneas 199, 209, 215, 220), con
nota (línea 224-229) de que los 4 no declaran el mismo conjunto de valores
(`source_intake_validation.schema.json` incluye `parking_lot`; los otros tres no).

`state/pendientes_ledger.md:46` (P-151, fila existente, [repo@BASE]): nombra
`validation_status` explícitamente como parte del grupo de 24 propiedades sin
cobertura, y describe extender `vocab_check.py` como la reparación de mayor retorno
del grupo.

---

## 8. Historia completa (repo no-shallow, confirmado en cabecera)

Comando:
```
$ git log --all --oneline -S "validation_status"
$ git fsck --full --unreachable --dangling
$ git branch -a --contains <cada commit>
$ git merge-base --is-ancestor <cada commit> origin/main
```

**8 commits tocan la cadena `validation_status` en toda la historia (`--all`, sin
filtro de extensión):**

| Commit | Fecha | Archivo(s) tocado(s) que mencionan el campo | ¿Ancestro de `origin/main`? |
|---|---|---|---|
| `089d71b2` | 2026-04-05 | `upstream/data-extraction/schemas/data_extraction_validator.schema.json`, `upstream/signal-extraction/contracts/signal_extraction_contract.md`, `upstream/signal-extraction/contracts/signal_to_inventory_entry_gate.md`, `upstream/signal-extraction/schemas/signal_inventory_gate.schema.json`, `upstream/signal-extraction/schemas/signal_validation.schema.json`, `upstream/source-intake/schemas/source_intake_validation.schema.json` | Sí |
| `04a67444` | 2026-04-08 | `pipeline_flow_map.md` | Sí |
| `03fc22e2` | 2026-04-09 | `pipeline_flow_map.md` (delete) | Sí |
| `de3502ea` | 2026-04-11 | `docs/pipeline_flow.md` | Sí |
| `377136d9` | 2026-07-30 | `state/output/vocab_check_blind_spots.md` | Sí |
| `ea6c5a25` | 2026-07-30 | `state/pendientes_ledger.md` | Sí |
| `f5640c0a` | 2026-07-29 | `state/pendientes_ledger.md` | Sí |
| `0e591caf` | 2026-08-04 | `state/output/mapa_validacion_S36.md` | **No** — vive solo en `origin/claude/eval-s36-reconocimiento-eqg3qs`, no es ancestro de `origin/main` |

`089d71b2` es la **primera y única introducción** del campo en toda la historia:
crea de una vez los 4 schemas de validador y los 2 contratos que lo declaran, bajo
la estructura de rutas antigua (`upstream/...`, pre-restructure). Ningún commit
posterior lo introduce en un archivo nuevo de tipo script/skill/agente — todos los
commits posteriores son documentación (`pipeline_flow*.md`), medición
(`vocab_check_blind_spots.md`), o ledger.

**Cero de los 8 commits toca un archivo `.py`, un `SKILL.md`, o cualquier ruta bajo
`agents/`.** Confirmado también con `--diff-filter=A` (solo adiciones): mismo
resultado, 6 de los 8 commits (los que efectivamente agregan la cadena en vez de
solo citarla en un mensaje o mover el archivo).

**`git fsck --full --unreachable --dangling` → salida vacía.** Cero objetos
inalcanzables o dangling en todo el repositorio. No hay historia purgada u orfanada
que pudiera esconder un ejecutor eliminado.

**Ramas `legacy/`/`preserve/` (contenido del árbol en esas puntas, no solo mensajes
de commit):**
```
$ git grep -n "validation_status" origin/legacy/s12-im-artifacts
$ git grep -n "validation_status" origin/preserve/s12-round1-75-cards
$ git grep -n "validation_status" origin/preserve/s12-round1-orphan-chain
```
Las tres ramas muestran el campo en el mismo patrón: los 4 schemas de validador +
`docs/pipeline_flow.md` + `signal_extraction_contract.md` +
`signal_to_inventory_entry_gate.md`. Ningún `.py`, `SKILL.md` ni archivo bajo
`agents/` en ninguna de las tres.

**Cobertura de ramas ampliada.** Las 3 ramas `legacy/`/`preserve/` ya cubiertas
arriba se verificaron por contenido completo del árbol (`git grep`, cualquier tipo
de archivo). Las 3 ramas restantes vivas en `origin`
(`claude/etapa-2-extraccion-juicio-gwnfk4`, `claude/etapa-2-field-extraction-jyqwwj`,
`claude/etapa-2-reextraccion-campos-cnb8bh` — un benchmark de re-extracción no
relacionado con Phase 2/G1) se verificaron para `.py`:
```
$ for b in claude/etapa-2-extraccion-juicio-gwnfk4 claude/etapa-2-field-extraction-jyqwwj claude/etapa-2-reextraccion-campos-cnb8bh; do
    git grep -l "validation_status" "origin/$b" -- '*.py'; done
(0 resultados en las 3 ramas)
```
Las 6 ramas no-`main` que existen hoy en `origin` quedan así cubiertas.

**Confirmación de que el rename no tocó contenido.** `242318bf` ("Restructure repo
into phases/ layout", 2026-04-11) mueve los 4 schemas de validador (y los 3
contratos de validador) de `upstream/...` a `phases/0X-.../...`. Sin `-M` (detección
de rename) git lo cuenta como delete+add; con `-M` se confirma rename puro:
```
$ git show --stat -M 242318bf | grep -i "validat"
 .../01-source-intake}/contracts/source_intake_validator.md                | 0
 .../data-extraction/contracts/data_extraction_validator.md                | 0
 .../data-extraction/schemas/data_extraction_validator.schema.json         | 0
 .../01-source-intake}/schemas/source_intake_validation.schema.json        | 0
 .../02-signal-extraction}/contracts/signal_extraction_validator.md        | 0
 .../02-signal-extraction}/schemas/signal_inventory_gate.schema.json       | 0
 .../02-signal-extraction}/schemas/signal_validation.schema.json           | 0
```
0 líneas cambiadas en los 7 archivos. Confirmado también que ningún commit posterior
a `242318bf` vuelve a tocar ninguno de los 4 schemas (`git log -1 --format="%h %ad %s" -- <ruta>`
para cada uno → `242318bf 2026-04-11` en los 4 casos). Su contenido es idéntico al
escrito en `089d71b2` (2026-04-05); el único evento intermedio es el movimiento de
ruta.

**Conclusión medida:** un ejecutor de cualquier clase que escriba el campo
`validation_status` **nunca existió**, en ningún punto de la historia completa del
repositorio, bajo ningún tipo de archivo. El campo entró al árbol una sola vez, como
declaración de forma (schemas + contratos), y solo ha sido citado —nunca
implementado— desde entonces.

**Contraste con el ANCLA A FALSEAR:** coincide en el campo literal — cero
productores del campo `validation_status`, en cualquier tipo de archivo, en toda la
historia. No coincide, o más bien matiza, si se lee el ancla como "cero ejecución de
trabajo de validación": el commit `089d71b2` y la cadena de Phase 2 (Pregunta 2.3,
Pregunta 6) muestran que sí existe, hoy, un ejecutor real (`p2-extract-signals`) que
corre el juicio semántico del validador de Phase 2 — simplemente nunca lo persiste
bajo ese nombre de campo. La nota al pie de `0e591caf` (rama
`origin/claude/eval-s36-reconocimiento-eqg3qs`, no fusionada a `main`, contenido no
leído en este encargo por instrucción explícita de derivar desde cero) se reporta
aquí únicamente porque `git log --all -S` la sacó a la superficie como hecho
literal — no se usó como fuente para ninguna respuesta de este archivo.

---

## 9. Riesgo de retirada (enumeración, sin juicio)

Comando:
```
$ grep -rn "source_intake_validation\.schema\.json\|data_extraction_validator\.schema\.json\|signal_inventory_gate\.schema\.json\|signal_validation\.schema\.json" --include="*" . --exclude-dir=.git
```

Los cuatro schemas de validador en cuestión:
`data_extraction_validator.schema.json`, `source_intake_validation.schema.json`,
`signal_inventory_gate.schema.json`, `signal_validation.schema.json`.

**Referencias encontradas, por archivo que las contiene:**

| Referencia | Naturaleza | ¿Se rompería al retirar los 4 schemas? |
|---|---|---|
| El propio `$id` interno de cada schema | Auto-referencia cosmética | No — no depende de otro archivo |
| `output/diagnostics/phase1_inventory_report.md:22,35,133,143,153` | Diagnóstico histórico. Alcance del `CLAUDE.md`: `output/repo_study/` es "reference only"; este diagnóstico es de la misma clase | No — es prosa estática, no se re-genera ni se ejecuta |
| `state/MAP.md:95,150,155,157` | Índice de rutas auto-generado por `state/scripts/generate_state.py`, corrido en cada push vía `state-snapshot.yml` | El próximo snapshot dejaría de listar esas 4 rutas silenciosamente (mecánico, no falla el job) |
| `state/output/vocab_check_blind_spots.md:199,209,215,220,225-227` | Reporte de medición congelado (histórico) | No se re-ejecuta solo; quedaría desactualizado en ese punto, sin que nada lo señale |
| `state/pendientes_ledger.md:105-106` (P-181, P-182) | Filas de ledger citando las rutas como evidencia | No se rompe mecánicamente (prosa estática); quedaría citando rutas retiradas. (R-G: este archivo no se toca en este encargo) |
| `docs/pipeline_flow.md:182,238,292,313,585,589,593,594` | Documento marcado OBSOLETO, rutas ya bajo el layout antiguo `upstream/` que no coincide con las rutas actuales | No — ya está desactualizado y marcado como tal |
| `pipeline_vocabulary.yaml` → `vocab_check.py`, campo `check_status`, `in_schemas: ["**/*validat*.schema.json", "**/*gate*.schema.json"]` (`pipeline_vocabulary.yaml:319-321`) | **Dependencia viva, ejecutada en CI** (`ci.yml`, job `vocab-check`) | **Sí, cambia el comportamiento del job.** Ver detalle abajo |

**Detalle de la única dependencia viva:** se verificó por glob directo (no por
suposición) qué archivos matchean hoy los dos patrones que `check_status` usa:

```python
$ python3 -c "
import fnmatch
from pathlib import Path
files = sorted(p for p in Path('.').rglob('*.schema.json') if 'working' not in p.parts and '.git' not in p.parts)
patterns = ['**/*validat*.schema.json', '**/*gate*.schema.json']
for p in files:
    rel = p.relative_to('.').as_posix()
    if any(fnmatch.fnmatch(rel, pat) or fnmatch.fnmatch(p.name, pat) for pat in patterns):
        print(rel)
"
phases/01-source-intake/data-extraction/schemas/data_extraction_validator.schema.json
phases/01-source-intake/schemas/source_intake_validation.schema.json
phases/02-signal-extraction/schemas/signal_inventory_gate.schema.json
phases/02-signal-extraction/schemas/signal_validation.schema.json
phases/03-inventory-mapping/schemas/validation_report.schema.json
```

5 archivos matchean hoy, no 4: los 4 en cuestión más
`phases/03-inventory-mapping/schemas/validation_report.schema.json` (el validador
propio de Phase 3, IM step 6, campo `passed` booleano — no `status`, ver Pregunta 4
sección `validate-candidate`). Confirmado que este quinto archivo **no** declara un
`checkResult.status`:
```
$ grep -n "status\|required" phases/03-inventory-mapping/schemas/validation_report.schema.json
6:  "required": ["candidate_id", "passed", "checks", "timestamp"],
14:        "required": ["check", "passed"],
```
— usa `passed` (booleano), no `status` (enum). Es decir, de los 5 archivos que
matchean el glob de `check_status`, los 4 en cuestión son los que efectivamente
aportan ocurrencias de un campo `status` de tipo enum; el quinto no aporta ninguna.
Retirar los 4 dejaría a `check_status` con **cero** ocurrencias de schema, moviendo
ese campo, en la salida de `vocab_check.py`, de la sección "CLEAN FIELDS" a "VOCAB
FIELDS WITH NO MATCHING SCHEMA FIELD FOUND". Esto no cambia el exit code del job
(confirmado leyendo la lógica: un campo sin ocurrencias no activa `has_issues`,
`vocab_check.py` líneas ~230 en adelante) pero sí cambia, de forma real y
mecánica, el contenido que el job `vocab-check` de `ci.yml` reporta en cada corrida
futura.

**Lo que NO se rompería:** ninguno de los 4 schemas de artefacto
(`signal_card.schema.json`, `card_record.schema.json`, `source_packet.schema.json`,
`data_extraction_record.schema.json`) referencia ni hace `$ref` a ninguno de los 4
schemas de validador — son estructuralmente independientes. Ningún script de los 18
listados en la Pregunta 1 abre estos 4 archivos por ruta explícita (solo
`vocab_check.py` los toca, y de forma incidental vía glob, no por nombre). Ningún
skill los referencia por nombre de archivo (los skills que sí ejecutan trabajo de
validación —`p2-extract-signals`— referencian el contrato `.md`, nunca el
`.schema.json`). Los otros dos jobs de CI (`signal-card-defect-check`,
`ledger-check`) no los tocan en absoluto.

Verificado además, de forma más general: ningún script del repositorio importa la
librería `jsonschema`:
```
$ grep -rln "import jsonschema\|from jsonschema" --include="*.py" . --exclude-dir=.git
(0 resultados)
```
Ningún `.py` de los 18 listados en la Pregunta 1 es mecánicamente capaz de validar
contra ningún `*.schema.json` del repo — ni los 4 de validador, ni los 4 de
artefacto de la Pregunta 4. Donde los módulos/skills dicen "validate against
schema" (Preguntas 2, 6), esa validación es juicio del ejecutor LLM, no una
llamada a una librería de JSON Schema.

---

## VEREDICTO

| Pregunta | Valor | Cita |
|---|---|---|
| ¿Existe ejecutor implementado que escriba el campo? | **NO** | §2 (3 contratos, 0 implementaciones que persistan el campo bajo ese nombre), §6 (Phase 2 lo calcula pero nunca lo escribe) |
| ¿Existe ejecutor declarado sin implementar? | **SÍ** | §2.1, §2.2 (`source_intake_validator.md`, `data_extraction_validator.md`: cero ejecutor de ningún tipo); §5 (G1 mismo: cero ejecutor) |
| ¿El schema del artefacto admite el campo? | **NO** | §4 — `signal_card.schema.json:7` (`additionalProperties:false`), `source_packet.schema.json:7`, `data_extraction_record.schema.json:7` (ídem); `card_record.schema.json` no lo declara ni lo prohíbe explícitamente (sin `additionalProperties:false`), pero tampoco lo admite en su `properties`/`required` — no hay ninguno de los 4 que lo declare |
| ¿La fase en curso lo escribiría al reanudarse? | **NO** | §6 — `signal_converter.md` Outputs (líneas 25-31) y Resumability (líneas 313-324): reanudar repite el mismo paso 4.5 sin instrucción de persistencia |
| ¿Existió alguna vez y se removió? | **NO** | §8 — 1 sola introducción (`089d71b2`, 2026-04-05), nunca implementado desde entonces; `git fsck` sin objetos inalcanzables que sugieran una remoción oculta |
| ¿Alguna referencia viva se rompería al retirar los schemas? | **SÍ** | §9 — `pipeline_vocabulary.yaml:319-321` (`check_status.in_schemas`) hace que `vocab_check.py`, corrido en CI (`ci.yml`, job `vocab-check`), use hoy los 4 archivos; retirarlos cambia el contenido reportado por ese job (no su exit code) |
