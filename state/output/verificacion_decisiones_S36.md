# E-VER-S36 — Verificación de 14 decisiones con trabajo pendiente

Generado sobre BASE `4f5ceed916fda9aaed798db0310ba6c5e62bff09` (origin/main, post
`git fetch --prune origin`). `git rev-parse --is-shallow-repository` → `true`.

Si el BASE de arriba no es el vigente, este archivo es procedencia, no evidencia.

Toda pregunta que dependiera de historia (qué se borró, cuándo, en qué commit)
se responde INDETERMINADA-SHALLOW cuando aplica — no se infiere.

Capa de cada cita: los textos de decisión citados en el encargo son
[PROJECT FILES] — procedencia, no evidencia. El árbol decide.

---

## D-063 — Review App local (React + Vite + Express)

**Pregunta:** ¿existe en el árbol algún artefacto de esa app?

```
$ find . -iname "package.json" -not -path "./node_modules/*"
(0 resultados)
$ find . -iname "vite.config*"
(0 resultados)
$ find . -iname "decisions.json"
(0 resultados)
$ find . -type d -iname "review-data"
(0 resultados)
```

Búsqueda de "express" en el árbol no arroja ningún servidor Express real (los
matches son texto narrativo tipo "expressed"/"impresión", no código).

**Veredicto: VIVA** — cero artefactos de la app. Ninguna pieza (package.json,
config de Vite, servidor, `review-data/`, `decisions.json`) existe.

---

## D-102 — Limpieza de artefactos legacy

**Pregunta:** ¿cuáles rutas existen HOY en main? ¿alguna rama viva reintrodujo el material?

```
$ find input -maxdepth 1 -iname "signal_cards_round_*.md"
(0 resultados)
$ for d in entry_gate split index scans validation; do ls working/$d; done
(cada uno solo contiene .gitkeep)
$ git ls-tree -r origin/main --name-only | grep -E "^input/signal_cards_round_|^working/(entry_gate|split|index|scans|validation)/|^output/(tension_candidates/|coverage_gaps.md|isolated_signals.md|lex_review_25.json|rejected_groupings.md|review_queue.md)"
output/tension_candidates/.gitkeep
working/entry_gate/.gitkeep
working/index/.gitkeep
working/scans/.gitkeep
working/split/.gitkeep
working/validation/.gitkeep
```

Ninguna de las 10 rutas `input/signal_cards_round_*.md` ni los 5 archivos
sueltos de `output/` (`coverage_gaps.md`, `isolated_signals.md`,
`lex_review_25.json`, `rejected_groupings.md`, `review_queue.md`) existe en
main. Los working dirs y `output/tension_candidates/` existen pero solo con
`.gitkeep`.

Pero — ramas vivas en `origin` reintrodujeron ese material:

```
$ git branch -r | grep -E "legacy/|preserve/"
  origin/legacy/s12-im-artifacts
  origin/preserve/s12-round1-75-cards
  origin/preserve/s12-round1-orphan-chain

$ git ls-tree -r origin/legacy/s12-im-artifacts --name-only | grep -E "^input/signal_cards_round_|^working/(entry_gate|split|index|scans|validation)/|^output/(tension_candidates/|...)" | wc -l
64
$ git ls-tree -r origin/preserve/s12-round1-75-cards --name-only | grep -E "(mismo patrón)" | wc -l
66
$ git ls-tree -r origin/preserve/s12-round1-orphan-chain --name-only | grep -E "(mismo patrón)" | wc -l
1
```
`legacy/s12-im-artifacts` contiene, entre otros, `output/tension_candidates/TC-002.md`
a `TC-024.md` (23 archivos) y `working/entry_gate/entry_gate_report.json`,
`working/index/card_index.jsonl`, `working/index/index_manifest.json`.

**Veredicto: CONSUMADA** (en `main`) — pero con matiz: el material declarado
borrado sigue vivo en `origin/legacy/s12-im-artifacts` y
`origin/preserve/s12-round1-*`. "Borrado" es cierto solo para `main`; el
repo como conjunto de refs todavía lo preserva.

---

## D-106 — Colisión de `signal_type`

**Pregunta:** ¿en qué archivos rastreados aparece hoy `signal_type`, con qué enums?

```
$ git grep -n "signal_type" -- .
output/repo_study/02_parser_analysis.md:23: ... signal_type, notes.
output/repo_study/02_parser_analysis.md:33: ... signal_type, notes, extra_fields?}` |

$ git grep -c "signal_type" -- . | wc -l
1

$ git grep -n "signal_type" -- 'phases/*'
(exit code 1 — sin matches)
```

Única aparición en `output/repo_study/02_parser_analysis.md` (self-analysis
histórico, explícitamente "reference only" según CLAUDE.md), listando el
campo dentro de un contrato de Part 1/2 findings, sin enum adjunto. Cero
apariciones en `phases/*` (contratos, módulos, schemas).

**Veredicto: SUPERADA** — el campo no aparece en ningún contrato o schema
vigente de las fases activas; la única mención está en un documento de
análisis histórico marcado como no autoritativo. No hay colisión de enums
verificable en el árbol hoy.

---

## D-108 — Flujo Part 4 → GPT recovery

**Pregunta:** ¿existe el directorio? ¿README? ¿contenido? ¿código que rutee ahí?

```
$ find . -path "*/phase0_part4_gpt_recovery*"
(0 resultados)
$ git ls-tree -r origin/main --name-only | grep -i "phase0_part4_gpt_recovery"
(0 resultados)
$ git grep -n "route_unrecoverable\|phase0_part4_gpt_recovery" -- .
docs/pipeline_flow.md:120: ... carpeta de recovery `working/data_gathering/phase0_part4_gpt_recovery/`
docs/pipeline_flow.md:133: Working recovery: `working/data_gathering/phase0_part4_gpt_recovery/`
phases/00-data-gathering/scripts/parse_dg_shard.py:265: (route_unrecoverable.py) expects `attempted` and `why_failed`, ...
phases/01-source-intake/scripts/route_unrecoverable.py: (script real, existe)
```

El directorio no existe. `route_unrecoverable.py` sí existe
(`phases/01-source-intake/scripts/route_unrecoverable.py`) pero escribe a
`working/source_intake/rejected_archive/`, una ruta distinta a la declarada
en D-108. Las únicas menciones del directorio `phase0_part4_gpt_recovery/`
son en `docs/pipeline_flow.md` (documentación) y como referencia comparativa
en otros módulos de Phase 1/2 — ninguna es código que lo cree o le escriba.

**Veredicto: VIVA** — el directorio declarado no existe, y el código de
routing existente apunta a otra ruta.

---

## D-109 — `reference/access_retry_strategies.md`

**Pregunta:** ¿existe ese archivo o cualquier otro con la tabla de los 7 failure modes?

```
$ find . -iname "access_retry_strategies*"
(0 resultados)
$ for term in paywall 404 robots_txt login_wall rate_limit dead_link structural_block; do
    echo "$term: $(git grep -c "$term" -- . | wc -l) files"; done
paywall: 39 files
404: 160 files
robots_txt: 0 files
login_wall: 0 files
rate_limit: 0 files
dead_link: 0 files
structural_block: 0 files
```

`paywall` y `404` aparecen dispersos en shards y contratos (prosa, no tabla).
Los otros cuatro valores exactos declarados (`robots_txt`, `login_wall`,
`rate_limit`, `dead_link`, `structural_block`) tienen **cero** ocurrencias en
todo el árbol, bajo cualquier nombre de archivo.

**Veredicto: VIVA** — ni el archivo con ese nombre ni una tabla equivalente
bajo otro nombre existen. Coincide con "creación física pendiente".

---

## D-110 — Sidecar de metadata de shards

**Pregunta:** ¿`parse_dg_shard.py` emite sidecar? ¿existe shard template?

```
$ find . -iname "parse_dg_shard.py"
./phases/00-data-gathering/scripts/parse_dg_shard.py
$ grep -n "sidecar" phases/00-data-gathering/scripts/parse_dg_shard.py
(0 resultados)
$ find . -iname "*shard_template*"
(0 resultados)
$ grep -n "shard_template" state/pendientes_ledger.md
160:- **P-096** — Iterar `shard_template_v3`. Sin movimiento desde S15 — condición de desparqueo: idem P-095
```

El parser existe y corre, pero no emite ningún sidecar de metadata. El
shard template no existe como archivo; el ledger (`state/pendientes_ledger.md`,
P-096) confirma que sigue pendiente ("sin movimiento desde S15").

**Veredicto: VIVA** — ambas precondiciones declaradas ausentes siguen
ausentes; el ledger corrobora el bloqueo, no lo contradice.

---

## D-112 — Scanner colapsa Trabajos B y C

**Pregunta:** ¿existe el módulo 04 Scanner? ¿su texto vigente describe la operación colapsada?

```
$ find . -path "*inventory-mapping/modules/04_scanner.md"
./phases/03-inventory-mapping/modules/04_scanner.md
$ wc -l phases/03-inventory-mapping/modules/04_scanner.md
70 phases/03-inventory-mapping/modules/04_scanner.md
$ grep -n -i "colaps\|trabajo b\|trabajo c\|una sola pasada" phases/03-inventory-mapping/modules/04_scanner.md
(0 resultados)
$ git grep -n "Trabajo B\|Trabajo C\|D-112" -- .
(0 resultados)
```

El módulo existe y describe 7 operaciones de scan, cada una con su propio
artefacto (`working/scans/*.json`). Texto vigente, líneas 68-70: "Each scan
runs independently... Do not merge scans. Each produces its own artifact
file." — lo opuesto de un colapso en una sola pasada. No hay ninguna
referencia en el árbol a "Trabajo B"/"Trabajo C" que permita mapear la
terminología de la decisión a operaciones específicas; el mapeo es
inferencia sobre el texto anti-fusión, no una cita directa.

**Veredicto: CONSUMADA** — el módulo vigente exige explícitamente scans
separados y artefactos separados; no describe ni permite la colapsada
declarada. Nota: no hay cita en el árbol que use el vocabulario "Trabajo
B/C", así que el mapeo decisión→módulo depende de inferencia, no de cita
literal.

---

## D-115 — Converter Phase 0 → Phase 1

**Pregunta:** ¿existen los 5 artefactos en rutas actuales? ¿hay evidencia de corrida real?

```
$ find . -iname "converter_prepare.py"
./phases/01-source-intake/scripts/converter_prepare.py
$ find . -iname "converter.md"
./phases/01-source-intake/modules/converter.md
$ find . -iname "*manifest*schema*" -path "*01-source-intake*"
./phases/01-source-intake/schemas/converter_prepare_manifest.schema.json
./phases/01-source-intake/schemas/converter_manifest.schema.json
$ find . -path "*skills*convert-findings*"
./.claude/skills/p1-convert-findings
./.claude/skills/p1-convert-findings/SKILL.md
$ find working/source_intake -iname "*manifest*"
working/source_intake/converter_prepare_manifest.json
working/source_intake/converter_manifest.json
$ head -c 400 working/source_intake/converter_manifest.json
{"status": "complete", ..., "total_skeletons": 688, "skeletons_processed": 688,
 "packets_written": 688, "recovery_staged": 0, "needs_human_review_count": 10, ...}
```

Los 5 artefactos existen en rutas post-reestructuración. `converter_manifest.json`
declara `status: "complete"`, 688/688 skeletons procesados, 688 packets
escritos — evidencia directa de al menos una corrida real completa.

**Veredicto: CONSUMADA** — implementación completa Y evidencia de corrida
real con conteos y status, más allá de lo declarado ("pendiente: primera
corrida real").

---

## D-119 — Contratos de agentes Codex Recovery

**Pregunta:** ¿existen los dos contratos? ¿hay material real en los directorios de recovery?

```
$ find agents/codex -type f
agents/codex/phase0-eje4-discovery/README.md
agents/codex/phase0-eje4-discovery/CONTRACT.md
agents/codex/phase1b-recovery/CONTRACT.md
agents/codex/_shared/protocols/*.md (4 archivos)
agents/codex/phase0-recovery/README.md
agents/codex/phase0-recovery/prompts/production_v1.md
agents/codex/phase0-recovery/CONTRACT.md
agents/codex/source-intake-recovery/CONTRACT.md

$ for d in working/source_intake/source_intake_gpt_recovery working/data_gathering/phase0_part4_gpt_recovery; do
    find "$d" -type f; done
working/source_intake/source_intake_gpt_recovery/.gitkeep
find: 'working/data_gathering/phase0_part4_gpt_recovery': No such file or directory

$ find working/data_gathering/recovery_packets -type f | wc -l
127
```

`agents/codex/phase0-recovery/CONTRACT.md` y
`agents/codex/source-intake-recovery/CONTRACT.md` existen, completos (no
stubs) — ambos definen rol, input JSON, protocolos heredados. La
precondición de bloqueo declarada ("material real en los directorios de
recovery") está resuelta parcialmente: `working/data_gathering/recovery_packets/`
tiene 127 packets reales (`packet_001.json` etc., con
`recovery_id`/`finding_id`/`original_finding_content` que calzan con el
input esperado por `phase0-recovery/CONTRACT.md`). Pero
`working/source_intake/source_intake_gpt_recovery/` sigue vacío (solo
`.gitkeep`), y `phase0_part4_gpt_recovery/` no existe (ver D-108).

**Veredicto: CONSUMADA** (contratos) con matiz — ambos contratos están
escritos e implementados como documento, contra "no implementados"
declarado. La precondición de material real se cumple para
phase0-recovery (127 packets) pero no para source-intake-recovery
(directorio vacío).

---

## D-120 — `signal_type` eliminado de 4 contratos base de Data Gathering

**Pregunta:** ¿existen esos 4 contratos en el árbol?

```
$ find . -iname "02_DG_CORE_PROTOCOL*" -o -iname "03_DG_OUTPUT_CONTRACT*" -o -iname "04_DG_SEARCH_DECOMPOSITION_RULES*" -o -iname "05_OUTPUT_TEMPLATE*"
(0 resultados)
$ grep -n "signal_type" agents/codex/_shared/protocols/*.md phases/00-data-gathering/reference/*.md
(0 resultados)
```

Ningún archivo con esos nombres numerados existe en el árbol — los
contratos compartidos de Phase 0 viven hoy en
`agents/codex/_shared/protocols/` (`core_protocol.md`, `output_contract.md`,
`search_decomposition_rules.md`, `output_template.md`), sin `signal_type` en
ninguno.

**Veredicto: FUERA-DEL-ÁRBOL** — la decisión declara explícitamente que el
paso pendiente es subir los contratos a project files de un proyecto de deep
research externo, no al repo. Coherente: no existen en el árbol bajo ningún
nombre, y su destino declarado nunca fue el repo.

---

## D-125 — Primera revisión de TCs

**Pregunta:** ¿cuántos TC existen hoy y dónde? ¿registro de estado por TC?

```
$ find . -iname "TC-*.md"
./phases/03-inventory-mapping/reference/TC-001.md
$ git ls-tree -r origin/main --name-only | grep -c "TC-"
1
$ head -5 phases/03-inventory-mapping/reference/TC-001.md
### Tension Candidate TC-001
**Status**
- pending_review
...
```

El único `TC-*.md` en main es `phases/03-inventory-mapping/reference/TC-001.md`
— un ejemplo de referencia del formato (vive en `reference/`, no en
`output/tension_candidates/`), no un TC real producido por el pipeline.
`output/tension_candidates/` solo tiene `.gitkeep` (ver D-102). No existe
ningún archivo de registro approved/rejected/parked en `output/` o `state/`.

**Veredicto: CONSUMADA** (en el sentido de que el pendiente "18 TCs
pendientes de revisión" ya no aplica — no hay TCs reales que revisar en
main) — conteo real: **0 TC reales**, 1 archivo de referencia/ejemplo. Nota:
23 TCs reales (TC-002 a TC-024) sí existen en `origin/legacy/s12-im-artifacts`
(ver D-102), fuera de main.

---

## D-174 — Recovery de findings bloqueados antes de Phase 2

**Pregunta:** ¿corrió Phase 2? Evidencia de Signal Cards y manifest con conteos.

```
$ find working/signal_extraction/cards -type f | wc -l
30
$ cat working/signal_extraction/signal_converter_manifest.json | head -15
{
  "status": "in_progress",
  "round": 1,
  "total_skeletons_found": 1178,
  "skeletons_processed": 25,
  "cards_written": 29,
  "cards_recovery_staged": 0,
  "skeleton_failures": 0,
  "needs_human_review_count": 0,
  "splits_performed": 3,
  ...
}
```

Phase 2 ya corrió parcialmente: 25/1178 skeletons procesados, 29 Signal
Cards escritas, `status: "in_progress"`. Esto contradice la premisa de
D-174 ("ejecución bloqueada por el arreglo del parser") — la ejecución no
está bloqueada, está en curso.

**Veredicto: SUPERADA** — los hechos (corrida parcial real de Phase 2, con
manifest y conteos) rebasaron la decisión declarada. La decisión asumía P2
bloqueada; el árbol muestra P2 corriendo.

---

## D-180 — Arreglo de `parse_part4()`

**Pregunta:** ¿existe `parse_part4()`? ¿conserva regex de contenido? ¿schema de `route_unrecoverable` con additionalProperties: false?

```
$ git grep -n "def parse_part4" -- .
phases/00-data-gathering/scripts/parse_dg_shard.py:259:def parse_part4(section_text: str, shard_id: str, source_tool: str) -> list[dict]:
```

Docstring (líneas 260-274) declara: "Part 4 items use the same 7 field
labels as Part 1/2 findings, so the block is parsed with
`_parse_finding_block` instead of dedicated regex." La función usa
`PART4_ITEM_PAT` (regex estructural, solo para delimitar ítems `F-Xnn`) y
delega la extracción de campos al parser genérico compartido
`_parse_finding_block`; conserva fallbacks por nombre de campo
(`extra_fields.get("attempted")`, `"searched_for"`, `"where_searched"`) para
formatos legacy, pero sin regex de contenido dedicadas por formato.

```
$ grep -n "additionalProperties" phases/01-source-intake/schemas/rejected_archive_record.schema.json
56:  "additionalProperties": false
```
Campos requeridos: `reason_code`, `source_finding_id`, `shard_id`,
`source_tool`, `seller_or_subject`, `attempted`, `archived_at`. `reason_code`
es enum cerrado de un solo valor: `unrecoverable_after_recovery`.

**Veredicto: CONSUMADA** — `parse_part4()` existe y ya no usa regex de
contenido por formato (usa el parser genérico de field-labels + fallback de
nombres de campo para legacy). El schema que consume `route_unrecoverable`
sí declara `additionalProperties: false` con los 7 campos citados. Nota:
esto contradice "implementación no escrita" declarado; el gate previo (recon
de mapeo campo-por-campo) no tiene rastro en el árbol (shallow) para
verificar si corrió antes.

---

## D-194 — Aplanamiento de listas, abierto hasta bloque 2

**Pregunta:** ¿evidencia de "bloque 2" y de un segundo caso del mismo defecto?

```
$ git grep -in "bloque 2\|block 2\|segundo caso\|aplanamiento\|flatten\|aplanar" -- .
phases/01-source-intake/contracts/source_intake_validator.md:19: verify that uncertainties are preserved instead of flattened
phases/01-source-intake/data-extraction/contracts/data_extraction_contract.md:385: `official_vs_anecdotal_flattened`
phases/02-signal-extraction/contracts/signal_extraction_validator.md:168: seller-level and marketplace-level are flattened
(y más matches de "flattened" como término genérico de validación, no
como referencia a F-02 ni a un "bloque 2")
$ git grep -n "D-194" -- .
(0 resultados)
```

Ningún archivo en el árbol usa la etiqueta "bloque 2" ni referencia un
segundo caso del defecto de aplanamiento de listas ligado a F-02. Las
apariciones de "flattened" son términos genéricos de checklist de
validadores (preservar distinciones, no aplanar niveles de actor), sin
relación con el caso concreto declarado.

**Veredicto: INDETERMINADA** — el repo no contiene un registro de sesiones
o bloques de revisión numerados ("bloque 1", "bloque 2", etc.) ni un
rastreo de defectos por finding que permita confirmar o descartar un
segundo caso. Para resolver esto haría falta: (a) un registro explícito de
qué sesión/rango de trabajo constituye "bloque 2" en este pipeline, y (b)
un hallazgo específico documentado como recurrencia del mismo defecto de
aplanamiento que afectó a F-02. Ninguno existe en el árbol.

---

## Resumen

| ID | Veredicto |
|---|---|
| D-063 | VIVA |
| D-102 | CONSUMADA (en main; material sigue vivo en ramas legacy/preserve) |
| D-106 | SUPERADA |
| D-108 | VIVA |
| D-109 | VIVA |
| D-110 | VIVA |
| D-112 | CONSUMADA |
| D-115 | CONSUMADA |
| D-119 | CONSUMADA (contratos; precondición de material real solo cumplida a medias) |
| D-120 | FUERA-DEL-ÁRBOL |
| D-125 | CONSUMADA (0 TCs reales en main; 23 reales solo en rama legacy) |
| D-174 | SUPERADA |
| D-180 | CONSUMADA |
| D-194 | INDETERMINADA |

**Conteo por veredicto:**
- CONSUMADA: 6 (D-102, D-112, D-115, D-119, D-125, D-180)
- SUPERADA: 2 (D-106, D-174)
- VIVA: 4 (D-063, D-108, D-109, D-110)
- FUERA-DEL-ÁRBOL: 1 (D-120)
- INDETERMINADA: 1 (D-194)

**Contraste con la hipótesis [CONVERSACIÓN DSC]:**

La hipótesis proponía: D-102, D-106, D-112, D-115, D-119 → CONSUMADA/SUPERADA;
D-063, D-109 → VIVA.

- **Coincide** en las 7 direcciones propuestas: D-102 (CONSUMADA), D-106
  (SUPERADA), D-112 (CONSUMADA), D-115 (CONSUMADA), D-119 (CONSUMADA), D-063
  (VIVA), D-109 (VIVA).
- **No hay discrepancia** en el sentido binario CONSUMADA/SUPERADA vs
  VIVA para estos 7 ítems. Sí hay matices que la hipótesis no capturaba:
  D-102 "CONSUMADA" es cierto solo para `main` — el material declarado
  borrado sigue vivo en ramas `legacy/`/`preserve/`, lo cual cambia el
  sentido de "borrado" que la hipótesis no distinguía. D-119 "CONSUMADA"
  también es parcial: los contratos existen pero la precondición de
  material real solo se cumple para uno de los dos directorios de
  recovery.
- Los 7 ítems fuera de la hipótesis (D-108, D-110, D-120, D-125, D-174,
  D-180, D-194) no tenían predicción declarada; se derivaron desde cero
  como pedía el encargo.
