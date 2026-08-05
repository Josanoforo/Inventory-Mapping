# Auditoría de clase P-153 (D-283(c)) — E-S41-POST Paso 5

Solo reporte. Ninguna reescritura de este archivo se aplica en este PR; el operador ratifica
antes de que cualquiera de estas propuestas toque un documento rector.

## Método y superficie de arranque

D-283(c) pide barrer skills y contratos buscando restricciones enumeradas por superficie (una
lista fija y concreta) donde el enunciado real es una clase (una propiedad estructural que
generaliza sobre esa lista) — y proponer la reescritura.

**Superficie de arranque:** archivos con serie `Rule 1..N` propia. Glob usado (verificado antes
de reportar cifras, por el error de S32 — su glob no alcanzaba
`phases/01-source-intake/data-extraction/`, un nivel más profundo que `phases/01-source-intake/`):

```
phases/*/contracts   phases/*/modules   phases/*/*/contracts   phases/*/*/modules   .claude/skills
```

7 archivos confirmados con serie propia (prefijo-R1..RN), verificado por grep sobre cada uno,
no solo por nombre de archivo:

| Archivo | Prefijo |
|---|---|
| `.claude/skills/p1-convert-findings/SKILL.md` | PCF-R1..R5 |
| `.claude/skills/p1-extract-records/SKILL.md` | PER-R1..R6+ |
| `.claude/skills/p2-extract-signals/SKILL.md` | PES-R1..R6+ |
| `phases/01-source-intake/contracts/source_intake_contract.md` | SIC-R1..R6+ |
| `phases/01-source-intake/data-extraction/contracts/data_extraction_contract.md` | DEC-R1..R6+ |
| `phases/01-source-intake/data-extraction/modules/extraction_converter.md` | EXC-R1..R6 |
| `phases/02-signal-extraction/contracts/signal_extraction_contract.md` | SEC-R1..R5+ |

Estos 7 son el punto de partida para leer reglas individuales en busca del patrón, no el
universo completo de instancias — la búsqueda se extendió más allá de estos 7 archivos
(scripts en `state/scripts/` y en la raíz) para no repetir el error de S32 de confundir el
glob de arranque con el alcance final.

**Instancias ya documentadas en la fila P-153 (no redescubiertas aquí):** `vocab_check.py`
(cobertura por campos del vocabulario, no por propiedades con enum) · `field_population_audit.py:266-273`
(7 campos hardcodeados) · `field_lifecycle_trace.py:46-62` (8 consumidores hardcodeados) ·
`ledger_path_check.py:25` (extensiones fijas de `PATH_EXTENSIONS`) ·
`signal_card_defect_check.py:229-233` (7 campos de texto enumerados) · `CLAUDE.md:73-75`
(regla "sin adjetivos valorativos" aplicada como lista de 9 palabras).

---

## Instancia 1 — `.claude/skills/p2-extract-signals/SKILL.md:58` (PES-R3)

**Qué superficie enumera:** la regla "Avoid red-flag wording" rechaza `signal_text` que
contenga una de 11 frases fijas, tipeadas directamente en la prosa de la regla:
`reveals, demonstrates, suggests that, confirms that, implies that, shows a tension, indicates
a market need, many sellers report, the corpus shows, platforms split into, sources converge`.
A diferencia de `CLAUDE.md:73-75`/`protocol_canonical.md` (que sí tienen respaldo en
`pipeline_vocabulary.yaml: forbidden_language`), esta lista de 11 frases no vive en ningún
lugar más que en esta línea — no hay clase que la respalde en absoluto.

**Qué clase debería definir esto:** "lenguaje interpretativo/causal no permitido en
`signal_text`" — la misma clase que ya cubre `forbidden_language`/`allowed_verbs` en
`pipeline_vocabulary.yaml`, pero un campo propio (`signal_text` tiene su propio registro de
riesgo — frases que anticipan la conclusión de Design Thinking, no solo adjetivos valorativos
de Phase 3). Un valor de vocabulario nuevo, con un checker que lo lea, generaliza sobre
"cualquier frase de esta clase", no solo sobre las 11 ya tipeadas.

**Reescritura propuesta (texto listo para pegar):**

> **PES-R3 (Rule 3): Avoid red-flag wording.** The validator will reject any `signal_text`
> containing a phrase from `pipeline_vocabulary.yaml: signal_text_red_flags` (interpretive or
> causal-conclusion language — the class this rule protects, not a fixed list). Check the
> current registry before committing the text; do not rely on memory of past instances.

---

## Instancia 2 — el mismo léxico "sin adjetivos valorativos" reescrito de forma independiente
tres veces más allá de `CLAUDE.md:73-75`

**Archivos y líneas:**
- `phases/03-inventory-mapping/reference/protocol_canonical.md:89-93` (`## Forbidden language`,
  los mismos 9 términos)
- `phases/03-inventory-mapping/modules/06_validator.md:18` (regla de word-boundary +
  whitelist `"resolución", "valor central"`)
- `.claude/skills/validate-candidate/SKILL.md:16` (misma regla de word-boundary + mismo
  whitelist, texto casi idéntico a `06_validator.md:18`)

**Qué superficie enumeran:** las cuatro ubicaciones (contando `CLAUDE.md:73-75`, ya
documentada) tipean el mismo léxico de 9 palabras de forma independiente, en vez de citar el
campo que ya existe para esto: `pipeline_vocabulary.yaml: forbidden_language` /
`allowed_verbs`. A diferencia de la Instancia 1, aquí la clase **ya existe** — el vocabulario
ya es la fuente única — pero cuatro documentos la ignoran y mantienen su propia copia.

**Qué clase debería definir esto:** ninguna clase nueva — el vocabulario ya la tiene. Lo que
falta es que las cuatro ubicaciones *citen* `pipeline_vocabulary.yaml` en vez de reproducir el
léxico, y que un check (ya existe la maquinaria en `vocab_check.py` para comparar contra
schemas; aquí el "schema" es prosa, no JSON, así que no es candidato natural a ese script —
pero si las cuatro copias divergen entre sí, nada lo detecta hoy) verifique que las cuatro
copias no divergen del vocabulario.

**Reescritura propuesta (texto listo para pegar, aplicar a las tres ubicaciones nuevas):**

> Mechanical language: no valorative adjectives. Léxico exacto en
> `pipeline_vocabulary.yaml: forbidden_language` / `allowed_verbs` — no reproducir la lista
> aquí. Match forbidden words at word boundaries only (ver excepciones de falso positivo en
> el propio campo del vocabulario, no en este archivo).

---

## Instancia 3 — "N judgment fields" como número/orden fijo en prosa, no derivado del schema

**Archivos y líneas:**
- `.claude/skills/p1-convert-findings/SKILL.md:5,34,45` — "the 8 judgment fields", listados
  por nombre en el orden del template
- `.claude/skills/p1-extract-records/SKILL.md:5,30,56` — "the 15 judgment fields"
- `.claude/skills/p2-extract-signals/SKILL.md:5,66,72` — "the 16 judgment fields", con
  posiciones ordinales citadas directamente ("fields 2–16", "field 3")

**Qué superficie enumeran:** cada skill tipea un conteo fijo ("8"/"15"/"16") y, en el caso de
Signal Extraction, posiciones ordinales específicas (`field 3` = `actor_level`) directamente
en prosa. Si el schema correspondiente (`source_packet.schema.json`,
`data_extraction_record.schema.json`, `signal_card.schema.json`) gana o pierde un campo
requerido, o cambia el orden de sus propiedades, estos números y posiciones quedan
desincronizados sin que nada lo señale — el mismo modo de falla que motiva P-153 en general,
aplicado a un conteo en vez de a una lista de valores.

**Qué clase debería definir esto:** el conteo y el orden de "judgment fields" de cada capa ya
están definidos estructuralmente por el propio `*.schema.json` (su arreglo `required`, en el
orden en que declara `properties`). La prosa debería referirse a esa fuente, no repetir un
número ni una posición ordinal de memoria.

**Reescritura propuesta (texto listo para pegar, patrón aplicable a las tres skills):**

> Executes Module — Converter (Source Intake stage 2). Reads skeleton files produced by
> stage 1 and fills the judgment fields declared by `source_packet.schema.json` (see that
> schema for the current count and order — do not hardcode a number here) to produce
> complete, validated Source Packets.

(Para `p2-extract-signals/SKILL.md:72`, reemplazar `field 3` por una referencia directa a
`actor_level` sin el número ordinal: "Exception: `actor_level`. Applying the assignment table
...")

---

## Instancia 4 — dos enumeraciones fijas más en `state/scripts/ledger_path_check.py`, distintas
de la ya citada (`:25`, extensiones)

**Archivo y líneas:**
- `state/scripts/ledger_path_check.py:68` (`GIT_REF_RE`) — namespaces de ref reconocidos como
  lista fija: `claude|legacy|preserve|origin|upstream`
- `state/scripts/ledger_path_check.py:81-89` (`PROJECT_FILE_PREFIXES`) — 7 prefijos fijos de
  nombre de documento de la capa project-files: `Blueprint_, DSC_, Decision_Log_, Handoff_,
  System_Registry_, Indice_, Decision_Router_`

**Qué superficie enumeran:** dos clases distintas de superficie (namespaces de ref de git;
familias de nombre de documento de project-files), cada una hardcodeada en su propia
constante, dentro del mismo archivo que ya tiene una instancia documentada (`PATH_EXTENSIONS`
en `:25`) pero en líneas y superficies diferentes — no es la misma instancia repetida, son dos
más.

**Qué clase debería definir esto:** "prefijos de ref de git que este repo reconoce" y
"familias de documento de la capa project-files" son ambas listas que ya existen en otro
lugar del proyecto de forma más autorizada — la primera en la práctica establecida de nombrar
ramas (`claude/*`, `legacy/*`, `preserve/*`) y remotos (`origin`, `upstream`); la segunda en
`project_files_check.py`, que ya cubre la capa project-files contra su propio almacén. Ninguna
de las dos necesita una segunda fuente de verdad en `ledger_path_check.py`.

**Reescritura propuesta (texto listo para pegar):**

> ```python
> # (c) origin/... and upstream/... are remote refs, not filesystem paths, same as the
> # claude/legacy/preserve branch-name refs already excluded here. Namespace list is
> # authoritative in docs/pipeline_flow.md's branch-naming section -- import/derive from
> # there rather than re-declaring it if that section becomes machine-readable.
> GIT_REF_RE = re.compile(r"^(claude|legacy|preserve|origin|upstream)/")
> ```
>
> Para `PROJECT_FILE_PREFIXES`: derivar la lista de la misma fuente que usa
> `project_files_check.py` para reconocer documentos de esa capa (si ese script expone una
> lista importable), en vez de mantener una copia paralela aquí.

---

## Resumen

| # | Archivo:línea | Clase que falta o se ignora |
|---|---|---|
| 1 | `.claude/skills/p2-extract-signals/SKILL.md:58` | Nueva: `signal_text_red_flags` en `pipeline_vocabulary.yaml` |
| 2 | `protocol_canonical.md:89-93`, `06_validator.md:18`, `validate-candidate/SKILL.md:16` | Existente: citar `pipeline_vocabulary.yaml: forbidden_language`/`allowed_verbs` en vez de reproducirlo |
| 3 | `p1-convert-findings/SKILL.md`, `p1-extract-records/SKILL.md`, `p2-extract-signals/SKILL.md` (conteos "N judgment fields") | Existente: derivar de `required`/orden de propiedades del `*.schema.json` correspondiente |
| 4 | `ledger_path_check.py:68,81-89` | Existente (git ref namespaces, prefijos project-files) o por crear si no hay fuente machine-readable |

Ninguna de estas cuatro reescrituras se aplica en este PR (D-283(c) es solo reporte). Quedan
para que el operador las ratifique antes de tocar los documentos rectores que enumeran.
