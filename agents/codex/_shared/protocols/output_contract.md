# OUTPUT_CONTRACT

Este documento define la estructura obligatoria del output (shard markdown), los campos por finding, las reglas por sección, el formato de absence findings, y el QA obligatorio antes de cerrar cada finding y el shard completo.

Es hermano de `core_protocol.md` (principios, taxonomías, edge cases), `search_decomposition_rules.md` (cómo partir el input) y `output_template.md` (template literal del shard).

---

## Estructura obligatoria del shard

La entrega debe contener siempre estas secciones, en este orden:

1. **Search decomposition** — lista de SD-NN ejecutadas
2. **Part 1 — Clean findings** (solo `direct_verified`)
3. **Part 2 — Provisional findings** (solo `indirect_verified`)
4. **Part 3 — Pattern candidates (sealed)** — único lugar donde se permite pattern language
5. **Part 4 — Absence findings** (solo `unrecoverable`, si el agente los produce)
6. **Research QA Notes**

Los agentes específicos pueden agregar Parts adicionales entre Part 1 y Part 4 (ej. Part 1B/2B para adjacent findings en el recovery agent). Cuando lo hagan, está declarado explícitamente en su `CONTRACT.md`. El recovery agent es el único caso actual. Part 4 puede estar marcada `None` si el agente no produce absence findings (ej. eje4-discovery) o si en este run no hubo ninguno.

---

## Reglas por sección

### Part 1 — Clean findings
Solo findings con `verification_status = direct_verified`.

### Part 2 — Provisional findings
Solo findings con `verification_status = indirect_verified`.

### Part 3 — Pattern candidates (sealed)
Único lugar donde se permite pattern language en todo el output.

Debe contener solo:
- Pattern Candidate ID
- Candidate statement
- Related Finding IDs
- Status: `sealed; not validated`

El Candidate statement debe ser **descriptivo y no causal**.

No puede contener:
- recomendaciones
- conclusiones
- prioridad
- magnitud
- implicación
- lenguaje estratégico
- lenguaje de fuerza de señal (*high*, *moderate*, *low*, *strong*, *weak*, *supported by N findings*, *narrows to*, *converges on*)

Si no hay pattern candidates válidos: `None`.

### Part 4 — Absence findings (opcional según agente)
Part 4 contiene exclusivamente **absence findings** con `verification_status = unrecoverable`: casos donde el agente buscó activamente evidencia de algo que debería existir epistémicamente y no la encontró. Cada agente específico define en su `CONTRACT.md` si produce absence findings o no — no todos los agentes los producen.

**Qué NO va en Part 4:**

- **Findings rechazados por edge case** (2, 3 o 5 — secondary retelling, intermediary verification, ambiguous URL). Estos van a Research QA Notes bajo "Findings rejected due to verification edge case", no a Part 4. El finding no califica como finding; no debe aparecer en ninguna Part.
- **Fetch failures de URLs** (una URL que no pudo abrirse). Eso se registra en Research QA Notes bajo "Strategies attempted by sub-búsqueda". El failure de una URL es el trigger para descomponer el claim en sub-búsquedas alternativas y/o buscar en otras fuentes, no un claim en sí mismo.
- **Queries exploratorias que no rindieron** (aplica específicamente a agentes tipo discovery). Si una query del catálogo no rinde evidencia, eso se registra en Research QA Notes, no como absence finding en Part 4. Los shards vacíos existen pero no contaminan el pipeline como findings. El contrato del agente específico lo declara.
- **Pattern naming, thesis statements, o categorizaciones cross-finding.** Ver guardrails anti-drift en `core_protocol.md`.

**Regla de inclusión de absence findings:** para que una ausencia califique como Part 4, tiene que tener estatus epistémico de "esperábamos encontrar algo específico y no lo encontramos tras búsqueda exhaustiva". El recovery agent produce absence findings legítimos porque procesa claims preexistentes que deberían ser verificables; un agente de discovery exploratoria no, porque una query que no rinde solo dice "este pattern no está aquí", no "esto debería existir y no existe".

### Research QA Notes
Notas breves sobre calidad, límites y degradaciones del run. Contenido permitido al final de este documento.

---

## Finding ID convention

Cada finding declara un ID en el header de la sección. Patrón base compartido por todos los agentes:

- **Part 1** (clean / `direct_verified`): `F-NN` secuencial empezando en 01 (ej: F-01, F-02, F-03)
- **Part 2** (provisional / `indirect_verified`): `F-PNN` secuencial empezando en 01 (ej: F-P01, F-P02)
- **Part 4** (absence findings con `unrecoverable`, opcional según agente): `F-XNN: <subject>` secuencial empezando en 01

Part 3 no introduce IDs nuevos. Referencia findings de Parts 1/2 por sus IDs existentes.

**Secuencia por-Part, no global.** Cada Part empieza en 01.

### Header format
- Part 1 y Part 2: `### F-NN` o `### F-PNN`
- Part 4: `### F-XNN: <subject>` — los items de Part 4 incluyen subject en el header line, separado por colon, porque no tienen verbatim snippet para identificarse por contenido.

Agentes específicos pueden extender esta convención con IDs adicionales para Parts suyas (ej. `F-ANN`, `F-APNN` para Parts 1B/2B del recovery). Cuando lo hagan, queda declarado en su `CONTRACT.md`.

---

## Campos obligatorios por finding

Cada finding debe incluir exactamente estos campos:

- **Finding ID** (en el header)
- **What** — totalmente sostenido por el Verbatim snippet (ver Regla 4 de `core_protocol.md`)
- **Verbatim snippet** — copiado literalmente, passage continuo
- **Source** — URL completa (protocolo + dominio + ruta)
- **source_type** — uno de los 18 valores del enum cerrado (ver `core_protocol.md`)
- **verification_status** — `direct_verified` | `indirect_verified` | `unrecoverable` (ver `core_protocol.md` y `pipeline_vocabulary.yaml` para semántica de cada valor y el estatus deprecated de `could_not_verify`)
- **Date** — fecha visible en página, o `Accessed [Month Year]; page undated`
- **Notes** — solo limitación local de verificación

Los campos What, Verbatim snippet, Source, source_type, verification_status, fecha y Notes siguen las reglas definidas en `core_protocol.md` (principios no negociables 4-8, regla de Source, regla de fecha, Notes permitidas/prohibidas, taxonomía de source_type, verification_status). Este documento no duplica esas reglas — las referencia.

---

## Absence findings — formato

Si una sub-búsqueda no rindió evidencia **después de búsqueda activa en fuentes primarias de cualquier tipo** (oficiales y terceros), reporta como absence finding en Part 4:

~~~
### F-XNN: <absence subject>

**What:** No data found on <X>
**Verbatim snippet:** n/a — absence finding
**Source:** Searches: "<query 1>"; "<query 2>"; "<query 3>". Locations attempted: <list of URLs/domains checked>
**source_type:** unknown
**verification_status:** unrecoverable
**Date:** <search date>
**Notes:** searched locations only
~~~

### Distinciones críticas

- **Absence finding (`unrecoverable`)** = "busqué activamente con queries específicas en locations específicas incluyendo fuentes primarias de terceros, y no encontré evidencia de algo que debería existir epistémicamente".
- **Finding rechazado por edge case** = "el finding no califica como finding válido (fuente ambigua, secondary retelling, intermediary verification, URL no fijable, u otra condición que rompe single-source)". No va a Part 4; va a Research QA Notes bajo "Findings rejected due to verification edge case".

Son fallas distintas con destinos distintos en el output. Ninguna de las dos es `could_not_verify` — ese valor es legacy y no se produce en agentes post-recovery.

### Reglas

- No las omitas cuando apliquen. Las absences son información valiosa downstream — dicen qué no encontramos y dónde re-dirigir esfuerzos.
- No las infieras de páginas inaccesibles. Una página inaccesible no es absence — documenta el fetch failure en Research QA Notes bajo "Strategies attempted", no como absence.
- No las declares sin haber buscado en fuentes primarias de terceros además de oficiales — búsqueda solo en oficiales no es búsqueda exhaustiva para efectos de absence.
- El campo Source de una absence debe listar búsquedas específicas y locations atacadas. NO "multiple searches" genérico.
- Solo algunos agentes producen absence findings (ej. recovery sí porque procesa claims preexistentes; eje4-discovery no porque procesa queries exploratorias). Ver contrato de cada agente.

---

## QA obligatorio antes de cerrar cada finding

1. ¿Todo lo importante del What está visible en el snippet?
2. ¿El What añade calificadores contextuales (scope, temporales, regulatorios, geográficos, causales) que no estén literales en el snippet? ¿Depende de aritmética o cálculo sobre los valores del snippet? Si cualquiera aplica, re-extrae snippet adicional o reformula el What con valores literales. Ver Regla 4 de `core_protocol.md`.
3. ¿El campo Source es URL completa y no un título?
4. ¿El finding contiene una sola identidad de fuente?
5. ¿Si la página tenía múltiples speakers/accounts, este finding quedó separado por speaker/account?
6. ¿Las Notes son solo limitación local y no evidencia extra?
7. ¿`source_type` está dentro del enum de 18 valores?
8. ¿`verification_status` fue asignado correctamente? Específicamente: si es un blog/news/article de terceros con URL accesible y snippet literal, ¿lo clasifiqué como `direct_verified` en lugar de degradarlo por ser third-party? (Ver Clarificaciones 1-2 en `core_protocol.md`.)
9. ¿Edge cases de verificación aplicados? Específicamente: si apliqué edge case 2 (secondary retelling), ¿verifiqué que efectivamente hay una fuente primaria externa que el blog está citando, no solo reporte directo del blog?
10. ¿Algún qualifier visible fue omitido?
11. ¿Este finding debería degradarse o excluirse por ambigüedad?
12. ¿Este finding está limpio de los tres patrones de drift prohibidos (pattern naming inventado, thesis statements, categorizaciones cross-finding fuera de Part 3)? Ver guardrails anti-drift en `core_protocol.md`.

---

## QA obligatorio antes de cerrar el shard completo

Además del QA por finding, antes de entregar el shard verifica:

1. ¿Busqué en fuentes primarias de terceros además de oficiales para cada sub-búsqueda, o solo en oficiales? Si solo en oficiales, la búsqueda no está completa y los absence findings no son válidos.
2. ¿Hay findings que encontré en blogs/news/reviews de terceros con URL fija y snippet literal que degradé a Part 4 o rechacé por ser third-party? Si sí, revisa — probablemente son válidos para Part 1 (`direct_verified` con `source_type: blog`).
3. ¿Algún finding en Part 4 documenta algo que NO sea un absence finding legítimo (fetch failure de URL, finding rechazado por edge case, query exploratoria vacía)? Si sí, mueve el registro a Research QA Notes en la sección correspondiente.
4. ¿Part 4 contiene pattern naming inventado, thesis statements, o categorizaciones que cruzan múltiples findings? Si sí, elimínalos. Part 4 es exclusivamente para absence findings con búsquedas específicas ejecutadas y locations atacadas.
5. ¿Part 3 contiene lenguaje de fuerza de señal, recomendaciones, implicaciones, o lenguaje causal? Si sí, reformula a descriptivo no-causal o elimínalos.
6. ¿Los findings rechazados por edge case 2, 3 o 5 quedaron documentados en Research QA Notes bajo "Findings rejected due to verification edge case" con la razón específica? Si los omití silenciosamente, el registro diagnóstico del run está incompleto.

---

## Research QA Notes — contenido permitido

Reporta solo:

- ambigüedad de contenedor
- **findings rejected due to verification edge case** (2, 3 o 5 — secondary retelling, intermediary verification, ambiguous URL) con razón específica por rechazo
- páginas multi-speaker separadas en findings distintos
- fuentes truncadas o parciales
- ambigüedades restantes de `source_type`
- coverage gaps por categoría (cuando una categoría esperada no rindió findings)
- casos donde el input no pudo descomponerse sin introducir interpretación
- strategies attempted by sub-búsqueda (cuando el agente específico lo requiera)
- metadatos de trazabilidad (recovery_id, shard_id, query_id, etc., según el agente)
- fetch failures de URLs específicas bajo "Strategies attempted"
- clasificación de adyacencia contra el claim del packet, cuando el agente específico produce Parts 1B/2B (ver `phase0-recovery/CONTRACT.md`). Esto es comparación contra el input del run, no entre findings.

No reportes:
- interpretación del contenido de los findings
- comparación entre findings
- narrativa conclusiva
- recomendaciones downstream

---

## Comportamiento si no hay findings válidos

Si no hay findings válidos después de procesar todas las sub-búsquedas (buscando tanto en fuentes oficiales como en fuentes primarias de terceros):

- Conserva la estructura completa del shard.
- Marca cada Part como `None`.
- Completa Research QA Notes con la trazabilidad de búsquedas intentadas.

Nunca inventes findings para llenar la salida.
