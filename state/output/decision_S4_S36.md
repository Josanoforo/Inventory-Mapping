# E-VAL3-S36 — Resolución de la contradicción #108 vs #109 y decisión de retirada

BASE: `c7127d92bc02f021dd753e7e80d95f3f4b745332` (`origin/main`, tras `git fetch --prune origin`).

Estado shallow: al iniciar, `git rev-parse --is-shallow-repository` → `true`. Se
ejecutó `git fetch --unshallow origin`; tras eso, `git rev-parse
--is-shallow-repository` → `false`. Todo lo que sigue corre sobre historia
completa, no shallow.

Rama de trabajo: `claude/resolve-s36-contradiction-ds3l38`. El nombre no existía en
`origin` al empezar (`git log -1 origin/claude/resolve-s36-contradiction-ds3l38` →
`fatal: ambiguous argument ... unknown revision`, exit 128); existía localmente ya
posicionada en BASE, y se crea/empuja a `origin` en este mismo encargo.

**Si el BASE de arriba no es el vigente, este archivo es procedencia, no
evidencia.**

Capa de cada hallazgo: todo lo que sigue es **[medido-por-mí]** — cada comando de
este archivo se ejecutó directamente en esta sesión. Se leyó el contenido íntegro
de las PR #108 (`state/output/mapa_validacion_S36.md`, no mergeada,
`origin/claude/eval-s36-reconocimiento-eqg3qs`) y #109
(`state/output/productores_validacion_S36.md`, no mergeada,
`origin/claude/inventory-mapping-execution-czdib2`) vía la API de GitHub — su
contenido se trata como **procedencia** (son insumo del encargo, no verdad
heredada); cada afirmación suya usada abajo fue re-verificada de forma
independiente contra el árbol en BASE antes de citarse. Ninguna de las dos PR
está mergeada a `main`; por eso sus archivos no aparecen en este árbol.

**Corrección de rumbo registrada, no oculta**: la primera pasada de este encargo
identificó "los cuatro schemas de validador" por coincidencia de nombre
(`*validat*.schema.json`), lo cual incluía por error
`phases/03-inventory-mapping/schemas/validation_report.schema.json` (Fase 3) y
excluía `phases/02-signal-extraction/schemas/signal_inventory_gate.schema.json`
(G1). Leer el cuerpo completo de #108 y #109 mostró que ambas definen "los
cuatro" como `signal_validation.schema.json`, `signal_inventory_gate.schema.json`,
`source_intake_validation.schema.json`, `data_extraction_validator.schema.json` —
los cuatro que declaran el campo `validation_status` con el mismo tipo de enum
cerrado. `validation_report.schema.json` (Fase 3) usa un campo `passed` booleano,
no `validation_status`, y ambas PR previas lo excluyen explícitamente. La prueba
empírica del Punto 1 se rehizo con el conjunto correcto antes de escribir este
archivo; no queda ningún resultado del conjunto incorrecto en este documento.

---

## Punto 1 — Resolver la contradicción

### 1.a — ¿`vocab_check.py` abre, carga o hace glob sobre los cuatro schemas?

**Sí, dos mecanismos independientes, ambos citados con línea exacta:**

**Mecanismo 1 — glob universal, incondicional.** `vocab_check.py:67-74`:
```python
def find_schema_files():
    files = []
    for path in ROOT.rglob("*.schema.json"):
        relparts = path.relative_to(ROOT).parts
        if "working" in relparts:
            continue
        files.append(path)
    return sorted(files)
```
`ROOT.rglob("*.schema.json")` (línea 69) recorre todo el árbol del repo (excepto
`working/`) buscando cualquier archivo cuyo nombre termine en `.schema.json`. Los
cuatro schemas en cuestión terminan en `.schema.json`, así que el patrón los
alcanza sin excepción ni condición — no depende de ningún campo del vocabulario.
Luego, en `main()`, `vocab_check.py:230-238`:
```python
    for path in schema_files:
        try:
            with path.open(encoding="utf-8") as f:
                doc = json.load(f)
        except (OSError, json.JSONDecodeError) as e:
            print(f"WARNING: could not parse {path.relative_to(ROOT)}: {e}", file=sys.stderr)
            continue
        schema_docs[path] = doc
        schema_prop_index[path] = collect_property_index(doc)
```
cada archivo devuelto por el glob se **abre y se parsea como JSON**
(`path.open()` + `json.load()`, línea 233-234). Esto ocurre para los cuatro
schemas en cada corrida de `vocab_check.py`, sin relación con `jsonschema` ni con
ningún campo específico del vocabulario.

**Mecanismo 2 — glob dirigido, vía el campo `check_status`.**
`pipeline_vocabulary.yaml:315-321`:
```yaml
check_status:
  # Called "status" inside each checks.<check_name> entry (checkResult.$defs)
  # in the Phase 1/2 validator and gate schemas.
  schema_field: status
  in_schemas:
    - "**/*validat*.schema.json"
    - "**/*gate*.schema.json"
```
`in_schemas` restringe, **dentro del conjunto ya abierto por el Mecanismo 1**, en
qué archivos se busca el campo `status`. Verificado con `fnmatch` (la función que
usa `vocab_check.py:77-82`) que los cuatro nombres matchean uno u otro patrón:
`signal_validation.schema.json`, `source_intake_validation.schema.json`,
`data_extraction_validator.schema.json` → `*validat*.schema.json`;
`signal_inventory_gate.schema.json` → `*gate*.schema.json`.

**Los dos mecanismos alcanzan los cuatro archivos. El Mecanismo 1 es
incondicional (ocurre aunque `check_status` no existiera); el Mecanismo 2 es lo
que hace que esa lectura tenga efecto sobre el resultado reportado.**

### 1.b — ¿Qué pasa si los cuatro no existen? Prueba, no especulación

Clon desechable creado **fuera del árbol de trabajo**
(`/tmp/.../scratchpad/disposable_clone2`, descartado al terminar), posicionado en
BASE:
```
$ git clone --quiet /home/user/Inventory-Mapping <scratch>/disposable_clone2
$ cd <scratch>/disposable_clone2 && git checkout --quiet c7127d92bc02f021dd753e7e80d95f3f4b745332
$ git log -1 --oneline
c7127d92 state: snapshot automático de STATE.md y MAP.md
```

**Baseline (los cuatro presentes, árbol real, sin modificar):**
```
$ python3 vocab_check.py
============================================================================
VOCAB CHECK — pipeline_vocabulary.yaml vs *.schema.json (excl. working/)
============================================================================
Schema files scanned: 20
Vocabulary fields checked: 20 (with schema occurrences), 3 with no matching schema field
...
CLEAN FIELDS (schema occurrences found, no divergence)
----------------------------------------------------------------------------
actor, metric_type, evidence_role, source_type, product_type_if_explicit, pointer_type, uncertainties, claim_type, retrieval_method, priority_for_source_first, traceability_status, tension_type, tension_status, classification_risk, scan_routing, scan_type, domain, extraction_status, check_status, manifest_status
...
VOCAB FIELDS WITH NO MATCHING SCHEMA FIELD FOUND
----------------------------------------------------------------------------
verification_status, allowed_verbs, forbidden_language

$ echo $?
0
```
`check_status` aparece en CLEAN FIELDS. Exit code `0`.

**Borrado de los cuatro, en el clon desechable:**
```
$ rm -f phases/02-signal-extraction/schemas/signal_validation.schema.json \
        phases/02-signal-extraction/schemas/signal_inventory_gate.schema.json \
        phases/01-source-intake/schemas/source_intake_validation.schema.json \
        phases/01-source-intake/data-extraction/schemas/data_extraction_validator.schema.json
$ ls <cada una de las 4 rutas>
ls: cannot access '...': No such file or directory   [×4, confirmado]
$ ls phases/03-inventory-mapping/schemas/validation_report.schema.json
phases/03-inventory-mapping/schemas/validation_report.schema.json   [confirmado NO borrado — no es uno de los 4]
```

**Corrida tras el borrado:**
```
$ python3 vocab_check.py
============================================================================
VOCAB CHECK — pipeline_vocabulary.yaml vs *.schema.json (excl. working/)
============================================================================
Schema files scanned: 16
Vocabulary fields checked: 19 (with schema occurrences), 4 with no matching schema field
...
CLEAN FIELDS (schema occurrences found, no divergence)
----------------------------------------------------------------------------
actor, metric_type, evidence_role, source_type, product_type_if_explicit, pointer_type, uncertainties, claim_type, retrieval_method, priority_for_source_first, traceability_status, tension_type, tension_status, classification_risk, scan_routing, scan_type, domain, extraction_status, manifest_status
...
VOCAB FIELDS WITH NO MATCHING SCHEMA FIELD FOUND
----------------------------------------------------------------------------
verification_status, check_status, allowed_verbs, forbidden_language

$ echo $?
0
```
`check_status` se movió de CLEAN FIELDS a VOCAB FIELDS WITH NO MATCHING SCHEMA
FIELD FOUND. `Schema files scanned` bajó de 20 a 16 (los 4 borrados, exacto).
**Exit code sigue siendo `0`.**

**CI equivalente.** `.github/workflows/ci.yml:51-52`, job `vocab-check`:
```yaml
      - name: Run vocab_check.py
        run: python3 vocab_check.py
```
Es exactamente el comando ya ejecutado arriba (mismo Python 3.11.15, mismo
PyYAML 6.0.1 pinneado en `ci.yml:50` y ya presente en este entorno). No hay paso
adicional de CI sobre estos archivos que ejecutar aparte.

Clon desechable descartado (`rm -rf`) al finalizar esta verificación.

### 1.c — Veredicto

**¿Retirar los cuatro rompe CI? NO.** Exit code `0` antes del borrado, exit code
`0` después del borrado — mismo resultado, verificado por ejecución directa dos
veces (Punto 1.b). Lo que cambia es el **contenido reportado**, no el resultado
pass/fail: `check_status` pasa de la sección "CLEAN FIELDS" a "NO MATCHING SCHEMA
FIELD FOUND", y `Schema files scanned` baja de 20 a 16. Esto no activa
`has_issues` (`vocab_check.py:248-249`: un campo con `occurrences_found == 0` se
clasifica como `untouched_fields`, que nunca fija `has_issues = True` — solo
`divergences` u `open_string_files` lo hacen, líneas 261-296).

**Contradicción #108 vs #109 — resuelta:**

- **#108** (`mapa_validacion_S36.md`, Pregunta 5) define "vivo" como *"código que
  carga jsonschema programáticamente"* y busca referencias por **grep del string
  literal del nombre de archivo** contra todo el repo. Bajo esa definición,
  concluye "cero referencias vivas". Verificado por mí, independientemente: cero
  `.py` en el repo importa `jsonschema` —
  ```
  $ grep -rn "^import jsonschema\|from jsonschema" --include="*.py" .
  (sin resultados, exit 1)
  ```
  — así que esa mitad de #108 es correcta. Pero su método (grep del nombre de
  archivo) es ciego por construcción a un lector que nunca cita el nombre y solo
  usa un patrón genérico. Verificado por mí:
  ```
  $ grep -n "signal_validation\.schema\.json\|signal_inventory_gate\.schema\.json\|source_intake_validation\.schema\.json\|data_extraction_validator\.schema\.json" vocab_check.py
  (sin resultados, exit 1)
  ```
  `vocab_check.py` nunca nombra ninguno de los cuatro archivos — solo usa
  `"*.schema.json"` (línea 69). El método de #108 no podía encontrarlo aunque lo
  buscara correctamente.
- **#109** (`productores_validacion_S36.md`, §9) define "vivo" como *"consumido
  por una ruta de código que efectivamente corre"*, y lo verifica simulando el
  glob (`fnmatch` sobre los patrones de `check_status.in_schemas`) en vez de
  grepear el nombre literal. Encuentra el Mecanismo 2 de 1.a y concluye
  correctamente que hay una dependencia. Su propio texto ya matiza la
  conclusión: *"Esto no cambia el exit code del job (...) pero sí cambia (...)
  el contenido que el job `vocab-check` (...) reporta"* — es decir, #109 nunca
  afirmó que retirar rompería CI; esa lectura más fuerte pertenece al resumen del
  encargo, no al cuerpo de #109.

**Ninguna de las dos PR se equivocó en un hecho verificable de forma aislada.**
El punto de fricción es la definición de "referencia viva" que cada una adoptó:
#108 = citada por nombre en código ejecutable; #109 = leída en tiempo de
ejecución, sin importar si se cita el nombre. Bajo la definición de #109 (la más
amplia, y la que empíricamente se sostiene: Punto 1.b la reproduce por ejecución
directa, no por lectura de código), hay una dependencia real. Bajo la definición
operativa que de verdad importa para la pregunta de este encargo — **¿retirar
rompe el exit code de CI?** — ambas PR, leídas en su texto completo y no en
resumen, son consistentes con la respuesta medida aquí: NO.

---

## Punto 2 — Consecuencias de retirar los cuatro schemas

Comando por archivo:
`grep -rln -- "<nombre>" --include="*.md" --include="*.json" --include="*.py" --include="*.yaml" . | grep -v "^\./working/"`

| Schema | Referenciado por (fuera de sí mismo) |
|---|---|
| `signal_validation.schema.json` | `state/MAP.md`, `state/output/vocab_check_blind_spots.md`, `state/pendientes_ledger.md`, `docs/pipeline_flow.md` |
| `signal_inventory_gate.schema.json` | `state/MAP.md`, `state/output/vocab_check_blind_spots.md`, `state/pendientes_ledger.md`, `docs/pipeline_flow.md` |
| `source_intake_validation.schema.json` | `output/diagnostics/phase1_inventory_report.md`, `state/MAP.md`, `state/output/vocab_check_blind_spots.md`, `state/pendientes_ledger.md`, `docs/pipeline_flow.md` |
| `data_extraction_validator.schema.json` | `output/diagnostics/phase1_inventory_report.md`, `state/MAP.md`, `state/output/vocab_check_blind_spots.md`, `state/pendientes_ledger.md`, `docs/pipeline_flow.md` |

**Referencias que quedarían apuntando a un archivo inexistente:**

- `state/MAP.md` — generado por `state/scripts/generate_state.py`, corrido en
  cada push vía `.github/workflows/state-snapshot.yml`. Consecuencia mecánica:
  el próximo snapshot dejaría de listar esas 4 rutas (no falla, se regenera).
- `state/output/vocab_check_blind_spots.md:199-229` — reporte de medición
  congelado (no se re-ejecuta solo). Quedaría citando 4 rutas retiradas, sin que
  nada lo señale automáticamente.
- `state/pendientes_ledger.md` (filas existentes que citan estas rutas como
  evidencia) — prosa estática, no se rompe mecánicamente, pero separaría el
  ledger de lo que el árbol contiene. **No se toca este archivo en este encargo
  (R-G)**; se cita solo como consecuencia, no se edita.
- `output/diagnostics/phase1_inventory_report.md` — diagnóstico histórico
  (`CLAUDE.md` clasifica `output/` como "reference only" para el estudio
  histórico); prosa estática, no ejecuta nada.
- `docs/pipeline_flow.md` — ya marcado obsoleto en su propia cabecera
  (`docs/pipeline_flow.md:3-4`: *"OBSOLETO — describe la estructura
  pre-restructure 242318b. CLAUDE.md es el mapa vivo."*) y ya usa rutas
  `upstream/...` que no existen en el árbol actual. Retirar los 4 schemas no
  cambia su estado (ya desactualizado).

**Checks de CI afectados:** solo `vocab-check` (Punto 1). Verificado que los
otros dos jobs no tocan estos archivos:
```
$ grep -n "validation_report\|signal_validation\|source_intake_validation\|data_extraction_validator\|signal_inventory_gate" signal_card_defect_check.py state/scripts/ledger_check.py
(sin resultados, exit 1)
```
`signal-card-defect-check` y `ledger-check` no se ven afectados en absoluto.

**Lo que NO cambiaría:**

- Los 4 schemas de **artefacto** (`signal_card`, `card_record`, `source_packet`,
  `data_extraction_record`) — ninguno tiene `$ref` hacia ninguno de los 4
  schemas de validador/gate; son estructuralmente independientes (verificado
  leyendo los cuatro completos: cero apariciones de `$ref` cruzado).
- Los tres skills convertidores (`p1-convert-findings`, `p1-extract-records`,
  `p2-extract-signals`) — ninguno abre estos 4 archivos; solo validan contra el
  schema de artefacto correspondiente (`source_packet.schema.json`,
  `data_extraction_record.schema.json`, `signal_card.schema.json`).
- El exit code de `vocab-check` (Punto 1.c).
- La ausencia de validación `jsonschema` en tiempo de ejecución — ya es cero hoy
  (Punto 1.c), retirar los schemas no la reduce más.

**Pregunta sin hacer: si los schemas se retiran pero los tres contratos de
validador (`source_intake_validator.md`, `data_extraction_validator.md`,
`signal_extraction_validator.md`) y el contrato de compuerta
(`signal_to_inventory_entry_gate.md`, "G1") se quedan, ¿queda el repo coherente
o peor?**

Verificado con cita: ninguno de los cuatro contratos nombra el archivo de su
propio schema de salida:
```
$ grep -n "schema" phases/01-source-intake/contracts/source_intake_validator.md
30:- `source_packet.schema.json`
$ grep -n "schema" phases/01-source-intake/data-extraction/contracts/data_extraction_validator.md
28:- `data_extraction_record.schema.json`
$ grep -n "schema" phases/02-signal-extraction/contracts/signal_extraction_validator.md
29:- `signal_card.schema.json`
$ grep -n "\.schema\.json" phases/02-signal-extraction/contracts/signal_to_inventory_entry_gate.md
27:- `signal_card.schema.json`
```
Los cuatro solo citan el schema del **artefacto que validan** (como "optional
reference" de entrada), nunca el schema de su propio resultado. Así que no
habría un enlace roto literal dentro de esos cuatro documentos.

Pero los cuatro sí describen, en prosa, la forma del resultado que producen —
por ejemplo `signal_extraction_validator.md:38-48`: *"Allowed validation
statuses: pass / pass_with_flags / rework / reject. Allowed check statuses:
pass / flag / fail / not_applicable"* — sin listar los nombres exactos de campo
(`validation_id`, `validator_version`, `checks.<name>.$ref: checkResult`,
`failures`, `notes`, `validated_at`) que solo existen, hoy, en el JSON Schema.
Retirar el schema no rompe una referencia, pero sí elimina la única definición
formal y verificable-por-máquina de esa estructura, dejando la prosa —más
gruesa, sin enum ligado a cada campo— como única fuente. **Es un estado peor en
precisión, no un estado roto en ejecución**: ningún proceso falla, pero el
repo pasa de tener una fuente de verdad formal para "qué forma tiene un
resultado de validación de Fase 1a/1b/2/G1" a no tener ninguna. El caso de G1
es el menos severo de los cuatro: su contrato (`signal_to_inventory_entry_gate.md:64-236`)
ya detalla los 8 checks uno por uno en prosa extensa, más cerca de lo que el
schema formaliza que los otros tres contratos.

---

## Punto 3 — El paso que sí corre

**¿Es cierto que `p2-extract-signals` ejecuta los 11 checks de
`signal_extraction_validator.md` dentro de su loop de conversión?** Sí.

- `.claude/skills/p2-extract-signals/SKILL.md:42` (paso 7 del "Core loop", líneas
  27-50): *"**Apply validator checks** (all 11 from
  signal_extraction_validator.md). If check 11 (Notes Locality) triggers, apply
  the mandatory scrubbing step before routing. Record all flag codes and
  failure codes in issues."*
- `phases/02-signal-extraction/modules/signal_converter.md:191`: *"**4.5 Apply
  validator checks.** Run the completed card through all 11 checks in
  `phases/02-signal-extraction/contracts/signal_extraction_validator.md`"* —
  dentro del mismo loop por-skeleton que formula la card (§4.4) y la escribe
  (§4.7-4.8), no en un paso posterior separado.
- `phases/02-signal-extraction/contracts/signal_extraction_validator.md` declara
  exactamente 11 checks numerados (## Validation checks, secciones 1-11, líneas
  91-367: Observational wording, Subject exactness, Actor level, Time scope,
  Qualifiers, Evidence role, Single-claim discreteness, No cross-source
  meta-observation, Traceability, No tension-smuggling, Notes Locality).

**¿Dónde queda el resultado de esos 11 checks — se escribe, se refleja en un
campo, o se pierde?**

Se pierde como estructura; sobrevive solo como decisión de ruteo + códigos
sueltos. `signal_converter.md:205-211`:
```
For checks 1–10, apply the validator's pass/flag/fail/not_applicable logic.
...
After all checks:
- `pass` — proceed to schema validation
- `pass_with_flags` — proceed to schema validation; record all flag codes in issues
- `rework` — do not write to `cards/`. Route to `signal_gpt_recovery/`...
- `reject` — do not write to `cards/`. Route to `signal_gpt_recovery/`...
```
El veredicto por-check (11 valores `pass/flag/fail/not_applicable`, uno por
check nombrado) se calcula y se usa una sola vez, para decidir a qué carpeta se
escribe la card — y ahí muere. Confirmado que no hay campo destino:

- `phases/02-signal-extraction/schemas/signal_card.schema.json:7,8-30,31-324` —
  `additionalProperties: false`; `required` (21 campos) y `properties` no
  incluyen `checks` ni `validation_status` ni ningún campo de veredicto.
- `phases/02-signal-extraction/schemas/signal_converter_manifest.schema.json:128-145`
  (`$defs.processedEntry.issues_for_this_skeleton`) — el único lugar donde el
  manifest registra algo por-skeleton es un array de **8 códigos de tipo de
  problema** (`skeleton_invalid, contract_case_uncovered, needs_human_review,
  schema_validation_failed, required_field_unfillable,
  multiple_required_fields_unfillable, split_performed,
  below_signal_threshold`) — ninguno de estos 8 códigos corresponde a los 11
  checks nombrados del validador, y el manifest nunca usa el vocabulario
  `pass/flag/fail/not_applicable`.

El resultado estructurado de los 11 checks (la forma que
`signal_validation.schema.json` define: `validation_id`, `signal_id`,
`validator_version`, `validation_status`, `checks.<name>.status`, `failures`,
`notes`, `validated_at`) **nunca se instancia** — ni en la card, ni en el
manifest, ni en ningún archivo bajo `working/`. Muere en
`signal_converter.md:205-211`, convertido en una decisión binaria de carpeta
destino más una lista plana de códigos.

**Phase 1a y 1b — ¿sus contratos de validador tienen ejecutor?**

```
$ grep -n -i "validator" .claude/skills/p1-convert-findings/SKILL.md
(sin resultados, exit 1)
$ grep -n -i "validator" .claude/skills/p1-extract-records/SKILL.md
(sin resultados, exit 1)
```

- **`source_intake_validator.md` (Phase 1a): NO.** `p1-convert-findings/SKILL.md`
  (116 líneas, leído completo) solo valida contra `source_packet.schema.json`
  (líneas 17, 36, 98) — cero mención del contrato validador. Ningún `.py` bajo
  `phases/01-source-intake/scripts/` lo referencia
  (`route_unrecoverable.py`, `converter_prepare.py` — sin coincidencias de
  "validator").
- **`data_extraction_validator.md` (Phase 1b): NO.** `p1-extract-records/SKILL.md`
  (135 líneas, leído completo) solo valida contra
  `data_extraction_record.schema.json` (líneas 17, 47) — cero mención del
  contrato validador. Ningún `.py` bajo
  `phases/01-source-intake/data-extraction/scripts/` lo referencia
  (`bulk_extract.py`, `extraction_prepare.py`, `test_e5_fixtures.py` — sin
  coincidencias de "validator").

Contraste directo, mismo grep, Phase 2:
```
$ grep -n "signal_extraction_validator" .claude/skills/p2-extract-signals/SKILL.md
17: 3. `phases/02-signal-extraction/contracts/signal_extraction_validator.md` — all 11 validator checks...
42: 7. **Apply validator checks** (all 11 from signal_extraction_validator.md)...
```

---

## Punto 4 — La contradicción de contratos

**Mitad 1 — schemas de artefacto: ¿declaran `validation_status`? ¿declaran
`additionalProperties: false`?**

| Schema | `additionalProperties` | `validation_status` en `required`/`properties` |
|---|---|---|
| `signal_card.schema.json` | `false` (línea 7) | No (`required`: líneas 8-30, 21 campos; `properties`: 31-324) |
| `card_record.schema.json` | **no declarado** (draft-07, sin la clave en absoluto) | No (`required`: línea 6, 8 campos; `properties`: 7-62) |
| `source_packet.schema.json` | `false` (línea 7) | No (`required`: líneas 8-29, 20 campos; `properties`: 30-231) |
| `data_extraction_record.schema.json` | `false` (línea 7) | No (`required`: líneas 8-36, 27 campos; `properties`: 37-397) |

Tres de los cuatro (`signal_card`, `source_packet`, `data_extraction_record`)
confirman exactamente la premisa: no declaran el campo y sí cierran
`additionalProperties`. El cuarto (`card_record.schema.json`) no declara el
campo, pero **tampoco** declara `additionalProperties: false` — es un schema
draft-07 que simplemente nunca incluye esa clave, así que no prohíbe
propiedades extra por schema (aunque tampoco lo declara ni lo exige). Esto
rompe la generalización "los cuatro declaran additionalProperties: false" tal
como está escrita: son tres de cuatro, no cuatro de cuatro.

**Mitad 2 — ¿la compuerta G1 lo lee como check 1 de 8?**

`phases/02-signal-extraction/contracts/signal_to_inventory_entry_gate.md:64-82`
("Required checks", check 1 de 8): *"### 1. Validation status check ... The
Signal Card validation result is: `pass` / `pass_with_flags`"*.
`phases/02-signal-extraction/schemas/signal_inventory_gate.schema.json:51-64`
confirma 8 checks requeridos en el objeto `checks`
(`validation_status_check, discreteness_check, observational_boundary_check,
subject_exactness_check, actor_level_check, time_and_qualifier_check,
cross_source_contamination_check, pattern_readiness_check`) — 8, y el primero
es `validation_status_check`. Ambas mitades verificadas: **cierto**.

**Matiz medido, no opinión — de dónde lee G1 el campo:** el contrato de G1
declara explícitamente, en su propia sección de Inputs
(`signal_to_inventory_entry_gate.md:20-29`), que lee **dos documentos
separados**: `Signal Cards` y `Signal Extraction Validation Results`. El check 1
lee el campo desde el segundo (el resultado del validador de Fase 2, forma
`signal_validation.schema.json`, que sí declara `validation_status` como
`required` — `signal_validation.schema.json:8-12,31-39`), no desde
`signal_card.schema.json` (el primero, que no lo declara). Bajo esa lectura, G1
no exige un campo inexistente sobre el mismo objeto — exige cruzar dos objetos,
tal como su propio contrato ya especifica.

**Para que G1 fuera ejecutable tal como está escrita, ¿qué tendría que
cambiar?** — enumerado, sin recomendar ninguno:

1. **Cambiar el schema del artefacto** (`signal_card.schema.json`): añadir
   `validation_status` a `properties`/`required`, lo que implicaría que cada
   Signal Card cargue su propio veredicto de validación embebido, en vez de
   depender de un segundo documento (`signal_validation.schema.json`) que hoy
   nadie produce (Punto 3).
2. **Cambiar el contrato de la compuerta**
   (`signal_to_inventory_entry_gate.md`): reescribir el check 1 para leer
   explícitamente desde el "Signal Extraction Validation Results" ya declarado
   en Inputs, en vez de dejar ambigua la fuente ("The Signal Card validation
   result" es leíble como propiedad de la card o como resultado externo);
   implicaría dejar explícito que G1 depende de un artefacto
   (`signal_validation.schema.json`) que hoy no tiene productor (Punto 3),
   dejando esa dependencia bloqueada hasta que exista un ejecutor de Fase 2 que
   sí lo persista.
3. **Ambos**: el schema ganaría el campo y el contrato ganaría precisión sobre
   la fuente; implicaría además construir el ejecutor de Fase 2 que persista
   `signal_validation.schema.json` (hoy inexistente, Punto 3) para que haya algo
   real que G1 pueda leer, sea desde el mismo objeto o desde uno externo.

Sin esos cambios, G1 hoy es ejecutable **solo como lectura cruzada de dos
documentos**, uno de los cuales (`signal_validation.schema.json` con contenido
real) nunca se produce en el árbol actual (confirmado en el Punto 3: cero
ejecutor para Phase 2 que persista esa forma; el veredicto se calcula y se
descarta). El bloqueo real no es el schema de la card — es la ausencia de
productor del documento que G1 declara leer.
