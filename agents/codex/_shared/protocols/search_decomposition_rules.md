# SEARCH_DECOMPOSITION_RULES

Este documento define cómo partir un input de research en sub-búsquedas verificables sin introducir interpretación adicional. Es hermano de `core_protocol.md`, `output_contract.md` y `output_template.md`.

Cada agente específico describe en su `CONTRACT.md` qué constituye "el input" para su operación (ej. para recovery es el `original_finding_content` del packet; para eje4-discovery es una query del xlsx catálogo). Las reglas de descomposición aplican igual una vez identificado el input.

---

## Objetivo

Tomar un input de research y partirlo en sub-búsquedas verificables sin introducir interpretación adicional.

## Regla central

**Descomponer sí. Reinterpretar no.**

La descomposición puede:
- separar claims distintos contenidos en el mismo input
- normalizar claims implícitos en explícitos cuando ya están en el texto
- volver explícitas restricciones ya presentes en el input

La descomposición no puede:
- agregar afirmaciones nuevas
- fortalecer una hipótesis del input
- inventar subclaims implícitos
- convertir una sospecha amplia en una tesis operativa más fuerte

---

## Cuándo dividir el input

Parte el input en sub-búsquedas separadas cuando contenga:

- múltiples claims
- múltiples preguntas
- múltiples entidades
- múltiples mecanismos
- múltiples periodos de tiempo
- múltiples geografías
- múltiples políticas
- múltiples features
- múltiples eventos
- múltiples condiciones materiales

## Cuándo no dividir por reflejo

- No dividas solo porque el input sea largo o narrativo.
- No dividas por estilo de redacción.
- No dividas si la separación exige agregar supuestos que el input no contiene.

---

## Unidad correcta de sub-búsqueda

Cada sub-búsqueda debe apuntar a:
- una sola pregunta verificable, **o**
- un solo claim verificable.

## No combinar dentro de una misma sub-búsqueda

No combines:
- dos plataformas distintas
- dos políticas distintas
- dos eventos distintos
- dos speakers distintos
- dos periodos distintos si el cambio temporal altera materialmente el claim
- dos mecanismos distintos si eso obliga a interpretación
- dos geografías distintas si eso cambia el contenido verificable

---

## Manejo de hipótesis amplias

Si el input contiene una hipótesis amplia:
- no la investigues como hipótesis global
- conviértela en preguntas verificables o claims verificables separados

Si no puedes descomponerla sin interpretar de más:
- conserva una versión más amplia
- no inventes subclaims implícitos
- documéntalo en Research QA Notes ("Cases where input could not be decomposed without interpretation")

## Manejo de claims composite

Si el input contiene un claim composite (ej. "tiers de comisión 8.5%–15.25% por rating de vendedor 4.0–5.0"), descomponlo en componentes verificables independientemente:

- SD-NN: verificar el claim sobre la comisión base
- SD-NN+1: verificar el claim sobre el sistema de tiers por rating
- SD-NN+2: verificar el rango específico

Cada componente puede terminar en una Part distinta. Una parte del claim composite puede confirmarse como `direct_verified` mientras otra termina como absence finding. Eso es comportamiento correcto.

---

## Search decomposition obligatorio en el output

Antes de los findings, el shard debe incluir el bloque `Search decomposition` con la lista de SD-NN ejecutadas:

~~~
Search decomposition
- SD-01: <sub-búsqueda verificable>
- SD-02: <sub-búsqueda verificable>
- SD-NN: <sub-búsqueda verificable>
~~~

Los SD-IDs son referenciables internamente durante la búsqueda pero no aparecen como campos del finding mismo. Cada finding queda implícitamente atado a la sub-búsqueda que lo produjo. Si el operador downstream necesita rastrear qué SD produjo qué finding, eso vive en Research QA Notes, no en los campos del finding.

---

## Decomposición y absences

Si una sub-búsqueda no rindió ningún finding válido después de búsqueda activa **en fuentes primarias de cualquier tipo (oficiales y terceros)**, repórtala como absence finding en Part 4 con `verification_status: unrecoverable`. Ver formato en `output_contract.md`.

- No infieras absence solo por una página inaccesible — documenta el fetch failure en Research QA Notes bajo "Strategies attempted", no como absence finding.
- No declares absence sin haber buscado en fuentes primarias de terceros además de oficiales.
- `unrecoverable` es solo para "busqué activamente y no encontré" — y solo si el agente específico produce absence findings (ver contrato del agente; eje4-discovery no los produce, recovery sí).

---

## Casos de cautela

### Caso 1: Input con sospecha amplia

**Input:**
"La plataforma castiga listings viejos y además favorece anuncios pagados"

**Salida correcta:**
- SD-01: verificar claims oficiales o reportes sobre tratamiento de listings viejos
- SD-02: verificar claims oficiales o reportes sobre anuncios pagados

**No correcto:**
- SD-01: verificar que la plataforma reduce artificialmente el alcance orgánico para empujar ads

Porque eso fortalece la hipótesis del input en lugar de conservarla.

### Caso 2: Input con múltiples tiempos

**Input:**
"Quiero saber si cambió la política de reservas entre 2023 y 2025"

**Salida correcta:**
- SD-01: política de reservas en 2023
- SD-02: política de reservas en 2025

### Caso 3: Input con múltiples entidades

**Input:**
"Compara cómo Etsy y Amazon manejan suspensiones"

**No correcto** como una sola búsqueda. Debe separarse por entidad:
- SD-01: políticas o reportes verificables sobre suspensiones en Etsy
- SD-02: políticas o reportes verificables sobre suspensiones en Amazon

---

## Regla de cierre

Si el input no puede descomponerse sin introducir interpretación:
- dilo en Research QA Notes bajo "Cases where input could not be decomposed without interpretation"
- conserva la descomposición más conservadora posible
- no inventes subclaims para rellenar
