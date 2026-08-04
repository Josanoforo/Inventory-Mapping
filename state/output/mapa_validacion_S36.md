# E-VAL-S36 — Mapa de la capa de validación

Generado sobre BASE `3d6b24339dbebed8ea30bab06d96f8b2aee477df` (origin/main,
2026-08-04). Estado del clon: se inició shallow; se ejecutó
`git fetch --unshallow origin` y a partir de ese punto el clon es completo
(`git rev-parse --is-shallow-repository` → `false`). La pregunta 9 (historia)
se responde con historial completo, no INDETERMINADA-SHALLOW.

Si el BASE de arriba no es el vigente, este archivo es procedencia, no
evidencia.

Este documento es un mapa de lectura. No recomienda qué retirar, qué
conservar ni qué construir; no declara nada "obsoleto" o "muerto"; no
redacta filas de ledger. Toda cita de código o commit fue verificada
directamente contra el árbol en esta sesión (no solo reportada por un
subagente).

---

## Ancla de partida — verificación

**Afirmación previa [CONVERSACIÓN DSC — procedencia, no evidencia]:** exactamente
cuatro schemas declaran los cuatro estados (`pass`, `pass_with_flags`, `rework`,
`reject`) — `signal_validation.schema.json`, `signal_inventory_gate.schema.json`,
`source_intake_validation.schema.json`, `data_extraction_validator.schema.json`
— y cero scripts los escriben.

```
$ grep -rn "validation_status" --include="*.json" .
```
Confirma que son exactamente esos cuatro archivos los que declaran un campo
`validation_status`. Pero **la afirmación de "los cuatro estados" no es exacta
para los cuatro archivos por igual**: `source_intake_validation.schema.json`
declara **cinco** valores, no cuatro (agrega `parking_lot`). Ver Pregunta 1
para el detalle línea por línea. Esta divergencia ya está documentada en el
árbol en `state/output/vocab_check_blind_spots.md:225-229`:

> "Nota: `validation_status` aparece en cuatro archivos distintos (...) con
> conjuntos de valores que no son idénticos entre sí (p. ej.
> `source_intake_validation.schema.json` incluye `parking_lot`, los otros
> tres no) — observación mecánica, sin evaluar cuál lado tiene razón."

La parte "cero scripts los escriben" **sí coincide** con lo verificado en
esta sesión (Pregunta 2).

**Discrepancia → hallazgo, no error**: la afirmación de origen trata a los
cuatro schemas como declarando el mismo conjunto de cuatro estados; el árbol
muestra que uno de los cuatro declara cinco.

---

## Pregunta 1 — Declaración

Comando:
```
$ grep -rn "validation_status" --include="*.json" --include="*.md" --include="*.py" --include="*.yaml" .
$ grep -rln "pass_with_flags" .
```

Cuatro archivos de schema declaran un campo `validation_status` con enum
cerrado. Verificado con `cat -n` sobre cada archivo:

| Archivo | Campo (línea) | Enum literal (líneas) | `additionalProperties: false` |
|---|---|---|---|
| `phases/01-source-intake/data-extraction/schemas/data_extraction_validator.schema.json` | `validation_status` (31) | líneas 33-38: `["pass","pass_with_flags","rework","reject"]` | Sí — raíz línea 7; también en `checks` (línea 41) y `$defs.checkResult` |
| `phases/01-source-intake/schemas/source_intake_validation.schema.json` | `validation_status` (31) | líneas 33-39: `["pass","pass_with_flags","rework","parking_lot","reject"]` — **5 valores** | Sí — raíz línea 7; también en `checks` (línea 42) |
| `phases/02-signal-extraction/schemas/signal_inventory_gate.schema.json` | `validation_status` (32) | líneas 34-39: `["pass","pass_with_flags","rework","reject"]`; descripción línea 40: "Signal validation status inherited from Signal Extraction Validator" | Sí — raíz línea 7 |
| `phases/02-signal-extraction/schemas/signal_validation.schema.json` | `validation_status` (31) | líneas 33-38: `["pass","pass_with_flags","rework","reject"]` | Sí — raíz línea 7 |

**Otro vocabulario de validación de la misma clase, encontrado dentro de la
lista cerrada de estos cuatro archivos (no en otros):**

- `signal_inventory_gate.schema.json` declara además, en el mismo archivo,
  un segundo campo enum a nivel de decisión de compuerta:
  `entry_gate_decision` (líneas 42-49), enum:
  `["pass_to_inventory_mapping","preserve_as_isolated_signal","return_to_signal_rework","reject_from_inventory_input"]`.
  Ese mismo archivo declara también `isolated_signal_reason` (enum
  nullable, ~líneas 126-139).
- Los cuatro schemas comparten un enum anidado `$defs.checkResult.status`:
  `["pass","flag","fail","not_applicable"]` — estado por-check individual,
  distinto del `validation_status` a nivel de card/record/packet completo.

**Archivo que NO pertenece a esta clase pese al nombre similar:**
`phases/03-inventory-mapping/schemas/validation_report.schema.json` — su
único campo relevante es `passed` (booleano), gobernado por
`phases/03-inventory-mapping/modules/06_validator.md`. No declara
`pass`/`pass_with_flags`/`rework`/`reject`. Es un concepto de validación
estructuralmente separado (validación de un tension candidate de Fase 3,
no de un card/record/packet upstream).

`working/validation/` existe como directorio pero:
```
$ ls -la working/validation
total 8
drwxr-xr-x  2 root root 4096 Jul 31 18:56 .
drwxr-xr-x 12 root root 4096 Jul 31 18:56 ..
-rw-r--r--  1 root root    0 Jul 31 18:56 .gitkeep
```
Solo contiene `.gitkeep` (0 bytes).

---

## Pregunta 2 — Productores

Comandos:
```
$ grep -rn "validation_status" --include="*.py" .
(0 resultados)
$ grep -rn "pass_with_flags" --include="*.py" .
(0 resultados)
$ git log -p --all -S'validation_status' --format="COMMIT %H %ad" --date=short -- '*.py'
(0 resultados — historial completo, ningún commit)
```

Se enumeraron los 18 archivos `.py` presentes hoy en el árbol
(`find . -name "*.py" -not -path "./.git/*"`): ninguno contiene
`validation_status` ni `pass_with_flags`.

Únicas dos apariciones de `pass_with_flags` fuera de schemas/contratos son
prosa de instrucción, no código:

- `.claude/skills/p2-extract-signals/SKILL.md:46` — `"pass` or
  `pass_with_flags` from validator AND schema passes → write to
  `working/signal_extraction/cards/<signal_id>.json`` — instrucción en
  lenguaje natural para un paso ejecutado por humano/IA, condicionada a un
  resultado de validador que (ver más abajo) ningún código produce.
- `phases/02-signal-extraction/modules/signal_converter.md:209` — mismo
  texto, también prosa.

**Cero productores en el árbol actual y en el historial completo de git.**

---

## Pregunta 3 — Consumidores

Comando:
```
$ grep -rn "if.*validation_status\|validation_status ==\|validation_status ===\|validation_status !=" . --include="*.py" --include="*.md" --include="*.json"
```
Único resultado: `state/pendientes_ledger.md:46` (fila P-151), que es prosa
de ledger describiendo el problema del punto ciego, no código.

`phases/02-signal-extraction/contracts/signal_to_inventory_entry_gate.md:318-330`
lista `validation_status` como campo del "Gate report structure" (prosa de
contrato, no ejecutable). `.claude/skills/p2-extract-signals/SKILL.md:46`
describe una condición ("pass o pass_with_flags → escribir card") en
lenguaje natural, no como rama de código.

**Cero consumidores ejecutables** (`if`/filtro/gate dentro de `.py` o lógica
imperativa de skill) encontrados. Toda "rama" sobre `validation_status`
existe únicamente como instrucción en Markdown de contrato/módulo.

---

## Pregunta 4 — Datos reales

Comandos:
```
$ find working output input -type f \( -name "*.json" -o -name "*.jsonl" -o -name "*.md" \) | wc -l
6924
$ grep -rl "validation_status" working output input
(vacío)
$ grep -rl "pass_with_flags" working output input
(vacío)
$ grep -rl '"rework"' working output input
(vacío)
$ grep -rl '"reject"' working output input
(vacío)
```

Capas revisadas: `working/` (`data_extraction`, `data_gathering`,
`entry_gate`, `index`, `notes_scrubbing`, `scans`, `signal_extraction`,
`source_intake`, `split`, `validation`), `output/` (`diagnostics`,
`repo_study`, `tension_candidates`), `input/` (`data_gathering`).

De los 6,924 archivos JSON/JSONL/MD bajo esas tres raíces, **cero**
contienen `validation_status`, `pass_with_flags`, `"rework"` o `"reject"`.

Conteo por valor y por capa para el campo `validation_status`:

| Capa | `pass` | `pass_with_flags` | `rework` | `reject` | `parking_lot` |
|---|---|---|---|---|---|
| findings / packets (source_intake) | 0 | 0 | 0 | 0 | 0 |
| records (data_extraction) | 0 | 0 | 0 | 0 | 0 |
| skeletons / cards (signal_extraction) | 0 | 0 | 0 | 0 | 0 |
| manifests (todos) | 0 | 0 | 0 | 0 | 0 |
| output/ (tension_candidates, diagnostics) | 0 | 0 | 0 | 0 | 0 |

El campo está totalmente ausente de los datos reales — no simplemente
despoblado dentro de registros existentes.

Manifiestos revisados con el mismo grep (sin coincidencias):
`working/signal_extraction/signal_prepare_manifest.json`,
`working/signal_extraction/signal_converter_manifest.json`,
`working/data_extraction/extraction_prepare_manifest.json`,
`working/data_extraction/extraction_converter_manifest.json`,
`working/source_intake/converter_prepare_manifest.json`,
`working/source_intake/converter_manifest.json`.

---

## Pregunta 5 — Referencias entre archivos

Comando por schema: `grep -rn "<nombre_archivo>" . --include="*.py" --include="*.md" --include="*.json" --include="*.yml" --include="*.yaml"`.

Para los cuatro schemas, toda referencia encontrada es:

- **Auto-referencia**: la línea `"$id": "https://inventory-mapping.local/schemas/<nombre>"` (línea 3 de cada archivo). No hay `$ref` cruzado entre los cuatro schemas ni desde ningún otro `*.schema.json` del repo — confirmado repitiendo el grep sobre todos los `*.schema.json` del árbol: las únicas coincidencias de los cuatro nombres de archivo son dentro de los propios schemas (`$id`), nunca `$ref`.
- **Referencias inertes** (prosa/documentación, ninguna dentro de código que cargue o parsee el archivo programáticamente):
  - `output/diagnostics/phase1_inventory_report.md:22,35,133,143,153`
  - `state/MAP.md` (líneas 95,150,155,157) — mapa auto-generado por `state/scripts/generate_state.py`, que solo lista rutas, no valida contra ellas.
  - `state/output/vocab_check_blind_spots.md:199-227`
  - `state/pendientes_ledger.md:105,106` (filas P-181, P-182)
  - `docs/pipeline_flow.md:182,238,292,313,585,589,593,594` — usa rutas obsoletas `upstream/...` que ya no existen (`ls upstream` → "No such file or directory"; ruta vigente es `phases/...`).

Verificación de "vivo" (código que carga jsonschema programáticamente):
```
$ grep -rln "^import jsonschema\|from jsonschema" --include="*.py" .
(0 resultados)
```
Ningún `.py` del repo importa la librería `jsonschema`.

**Clasificación: todas las referencias a los cuatro schemas son inertes.
Cero referencias vivas encontradas.**

---

## Pregunta 6 — Contratos y módulos

Tres contratos de validador declaran explícitamente el flujo previsto, cada
uno con una lista "Allowed validation statuses":

- `phases/01-source-intake/contracts/source_intake_validator.md:39-44` —
  Propósito declara que el validador decide "pass, pass with flags, rework,
  parking lot, o reject". Lista de estados permitidos (líneas 39-44):
  `pass, pass_with_flags, rework, parking_lot, reject` (5 valores, coincide
  con el enum de 5 de ese schema).
- `phases/01-source-intake/data-extraction/contracts/data_extraction_validator.md:37-41`
  — "Allowed validation statuses: pass / pass_with_flags / rework / reject"
  (4 valores), para Data Extraction Records, "before it can pass downstream
  to Signal Extraction" (línea 5).
- `phases/02-signal-extraction/contracts/signal_extraction_validator.md:38-42`
  — misma lista de 4 valores, para Signal Cards.
- `phases/02-signal-extraction/contracts/signal_to_inventory_entry_gate.md:318-336`
  — el "Gate report structure" describe la compuerta G1 leyendo
  `validation_status` de un card como check 1 de 8; incluye un ejemplo JSON
  trabajado con `"validation_status": "pass_with_flags"` (línea 330).
  Ecoado en `docs/pipeline_flow.md:322`: "1. validation_status — card pasó
  validators de Phase 2."
- `phases/02-signal-extraction/contracts/signal_extraction_contract.md:34` —
  "records con `validation_status = pass`" (referencia en prosa para el
  filtrado corriente abajo).
- `.claude/skills/p2-extract-signals/SKILL.md:46` y
  `phases/02-signal-extraction/modules/signal_converter.md:209` — instruyen
  proceder con `pass`/`pass_with_flags`; no especifican como código el
  ruteo para los otros estados.

**Señal explícita:** la prosa de los tres contratos de validador (arriba)
describe un paso de decisión "pass / pass_with_flags / rework / reject (/
parking_lot)" que las Preguntas 2 y 3 muestran que nadie ejecuta — ningún
script ni skill contiene código imperativo que implemente esa decisión.

---

## Pregunta 7 — Flujo

Reconstrucción solo a partir de citas ya dadas; sin cita, "no declarado".

```
Source Packet (working/source_intake/packets/*.json)
  → [Source Intake Validator — source_intake_validator.md]
      escribe: resultado con forma source_intake_validation.schema.json
      → destino de persistencia: no declarado (Pregunta 4: nada poblado
        en working/validation/; Pregunta 2: sin productor)
  → Data Extraction Record (working/data_extraction/records/*.json)
      → [Data Extraction Validator — data_extraction_validator.md]
          escribe: resultado con forma data_extraction_validator.schema.json
          → destino de persistencia: no declarado (mismo patrón de ausencia)
  → Signal Card (working/signal_extraction/cards/*.json)
      → [Signal Extraction Validator — signal_extraction_validator.md]
          escribe: resultado con forma signal_validation.schema.json
          → destino de persistencia: no declarado
      → [G1 Entry Gate — signal_to_inventory_entry_gate.md]
          lee validation_status como check 1/8 (docs/pipeline_flow.md:322)
          escribe: resultado con forma signal_inventory_gate.schema.json,
          incluye entry_gate_decision
          → destino de persistencia: no declarado
  → input/signal_cards_round_*.md (puente vía signal_to_markdown.py,
      docs/pipeline_flow.md:296-299) — no se encontró lógica de
      validation_status en ese script (Pregunta 2, grep sobre .py)
  → Fase 3 Inventory Mapping — usa un schema de validación DISTINTO
      (validation_report.schema.json, campo `passed`), no la clase de
      cuatro estados de esta pregunta (Pregunta 1).
```

Todo destino de persistencia de los cuatro validadores es "no declarado":
ninguna cita en el árbol muestra una ruta de destino siendo poblada.

---

## Pregunta 8 — CI

Archivos revisados completos: `.github/workflows/ci.yml`,
`.github/workflows/state-snapshot.yml`.

`ci.yml` ejecuta exactamente tres jobs: `vocab-check` (`python3
vocab_check.py`), `signal-card-defect-check` (`python3
signal_card_defect_check.py --fixtures`), `ledger-check` (`python3
state/scripts/ledger_check.py`). Su comentario de cabecera declara
explícitamente que `field_lifecycle_trace.py` y `field_population_audit.py`
quedan "deliberately excluded: they are measurements, not checks." Ningún
job menciona `validation_status` ni ninguno de los cuatro schemas.

```
$ grep -n "validation" .github/workflows/state-snapshot.yml
(0 resultados, exit 1)
```

**Ningún workflow de CI gatea sobre estado de validación en ninguna forma.**

---

## Pregunta 9 — Historia (clon completo, no shallow)

Comandos y resultados, verificados individualmente por archivo:

```
$ git log --all --follow --diff-filter=A --format="%H %ad %s" --date=short -- <cada uno de los 4 schemas, ruta actual>
```
Los cuatro devuelven el mismo commit de creación:
`089d71b22887327dc02fe98d46204a3ca852b734` — 2026-04-05 — "Add upstream
contracts and schemas for source-type separation pipeline" (crea los 14
archivos de esa entrega, incluidos los cuatro schemas, en rutas antiguas
`upstream/...`).

```
$ git log -1 --format="%H %ad %s" --date=short -- <cada uno de los 4 schemas, ruta actual>
```
Los cuatro devuelven el mismo último commit que los tocó:
`242318bfebe732c17252aa1886dc74b490d3517c` — 2026-04-11 — "Restructure repo
into phases/ layout" — verificado con `git show --stat` que es un rename
puro (`| 0` líneas de cambio) de `upstream/*` → `phases/00-02-*`.

**Desde el 2026-04-11 ninguno de los cuatro schemas ha sido modificado ni
una vez** (mismo hash de último-touch para los cuatro, y ese commit es un
rename sin cambio de contenido).

Búsqueda pickaxe de código productor, historial completo:
```
$ git log --all -S'validation_status' --format="%H %ad %s" --date=short
ea6c5a251687e3c67c11c70735ee94b9c862d897 2026-07-30 Ledger: corregir P-149 con medición de vocab_check_blind_spots.md, agregar P-151
377136d9a33ef1477897ab6546e449912df85153 2026-07-30 Measure vocab_check.py blind spots for match:subset fields
f5640c0aa97761f109b679b48356de3d87c1e564 2026-07-29 state: ledger de pendientes S29 (Run 1)
de3502eadfcd9d071ddc3630156723402c50bdc5 2026-04-11 docs: add pipeline flow study from Phase 0 to IM
03fc22e202e070c6c2da6e2ba2d13c69ed13c871 2026-04-09 Delete pipeline_flow_map.md
04a674440a15d9a982bf7877dfef139a843c7b3b 2026-04-08 Add pipeline_flow_map.md: DG shards → IM input flow (read-only architecture review)
089d71b22887327dc02fe98d46204a3ca852b734 2026-04-05 Add upstream contracts and schemas for source-type separation pipeline
```
7 commits en total tocan la cadena `validation_status` en toda la historia.
Cada uno es de creación de schema, documentación, o ledger/medición —
ninguno es código productor/consumidor.

```
$ git log --all -p -S'validation_status' --format="COMMIT %H %ad" --date=short -- '*.py'
(0 resultados — vacío)
```
Confirmado: ningún commit, en ningún momento de la historia, agregó manejo
de `validation_status` a un archivo `.py`.

Verificación adicional de archivos `.py` borrados (para descartar
"se construyó y se borró" en un archivo que ya no existe):
```
$ git log --all --diff-filter=A --name-only --format="" -- '*.py' | sort -u
```
comparado contra el árbol actual, el único `.py` genuinamente eliminado (no
explicado por un rename) es `legacy-migration/working/preprocessing/run_url_normalization.py`.
Su contenido en el último commit que lo tocó (`git show <hash>:<ruta>`) no
contiene `validation_status` ni `pass_with_flags`.

**Conclusión Pregunta 9: los cuatro schemas nunca tuvieron un productor
construido y luego removido — es ausencia desde el origen, no remoción.**
Esto es consistente con `state/pendientes_ledger.md:90` (fila P-097): "no
existir no es una decisión tomada, es ausencia sin resolver", que cita como
vía de verificación `git log --all` / `git fsck` sobre objetos unreachable,
y encuentra solo contrato+schema+`.gitkeep` vacío. Reproducido de forma
independiente en esta sesión.

---

## Pregunta 10 — Ramas

Ramas remotas vivas además de `main`:
`claude/etapa-2-extraccion-juicio-gwnfk4`,
`claude/etapa-2-field-extraction-jyqwwj`,
`claude/etapa-2-reextraccion-campos-cnb8bh`, `legacy/s12-im-artifacts`,
`preserve/s12-round1-75-cards`, `preserve/s12-round1-orphan-chain`.

```
$ for b in <6 ramas>; do git grep -l "validation_status" "$b" -- '*.py'; done
(las 6: vacío, exit 1 — sin coincidencias)

$ for b in <6 ramas>; do git diff origin/main "$b" -- '*.py' | grep -i "validation_status\|pass_with_flags"; done
(las 6: vacío, exit 1)
```

**Ninguna rama — incluidas `legacy/*` y `preserve/*` — contiene productor o
consumidor de estado de validación en archivos `.py` que difiera de
`main`.** `preserve/s12-round1-*` y `legacy/s12-im-artifacts` son anteriores
al rename de 2026-04-11 (aún usan rutas `upstream/...`) pero muestran el
mismo patrón de solo-referencias-inertes que `main`.

---

## Pregunta 11 — Vocabulario

```
$ grep -n "validation_status\|^validation" pipeline_vocabulary.yaml
(0 resultados)
$ grep -n "^[a-zA-Z_]" pipeline_vocabulary.yaml
13:actor:
47:metric_type:
71:evidence_role:
86:source_type:
107:product_type_if_explicit:
122:pointer_type:
138:uncertainties:
172:verification_status:
193:claim_type:
208:retrieval_method:
219:priority_for_source_first:
223:traceability_status:
231:tension_type:
245:tension_status:
255:classification_risk:
268:scan_routing:
281:scan_type:
292:domain:
305:extraction_status:
315:check_status:
328:manifest_status:
346:allowed_verbs:
357:forbidden_language:
```
23 claves de nivel superior. `validation_status` **no está** entre ellas —
ausente de `pipeline_vocabulary.yaml` por completo. `entry_gate_decision`
(el otro campo enum encontrado en la Pregunta 1) tampoco está.

```
$ sed -n '225,255p' vocab_check.py
    vocab = load_vocab()
    schema_files = find_schema_files()
    ...
    results = []
    untouched_fields = []
    for field_name, entry in vocab.items():
        if not isinstance(entry, dict):
            continue
        result = check_field(field_name, entry, schema_files, schema_docs, schema_prop_index)
        ...
```
`vocab_check.py:244` (`for field_name, entry in vocab.items():`) itera
únicamente sobre las claves de `pipeline_vocabulary.yaml`. Como
`validation_status` no es una clave, `vocab_check.py` nunca la visita —
confirma lo ya registrado en `state/pendientes_ledger.md:46` (fila P-151):
"cero direcciones verificadas (ni `missing` ni `extra`)" para este y otros
23 campos enum declarados en schema, y lo ya tabulado en
`state/output/vocab_check_blind_spots.md:199-224`.

---

## Tabla de cierre

| Schema / campo | Declara | Escribe (productores) | Lee (consumidores) | Datos poblados | Referenciado por | En CI |
|---|---|---|---|---|---|---|
| `data_extraction_validator.schema.json` / `validation_status` | 1 | 0 | 0 | 0 | 6 (inertes) / 0 (vivas) | 0 |
| `source_intake_validation.schema.json` / `validation_status` (5 valores) | 1 | 0 | 0 | 0 | 6 (inertes) / 0 (vivas) | 0 |
| `signal_inventory_gate.schema.json` / `validation_status` | 1 | 0 | 0 | 0 | 6 (inertes) / 0 (vivas) | 0 |
| `signal_inventory_gate.schema.json` / `entry_gate_decision` | 1 | 0 | 0 | 0 | 1 (inerte) / 0 (vivas) | 0 |
| `signal_validation.schema.json` / `validation_status` | 1 | 0 | 0 | 0 | 6 (inertes) / 0 (vivas) | 0 |
| `pipeline_vocabulary.yaml` (cobertura de `validation_status`) | 0 (ausente como clave) | — | — | — | — | 0 |
