# OUTPUT_TEMPLATE

Este documento es el template base del shard markdown que cada agente Codex de Phase 0 produce. Tiene 4 Parts. Agentes específicos que requieren Parts adicionales (ej. recovery con Parts 1B/2B) declaran su template extendido en su propio `CONTRACT.md`.

Reglas de los campos, convenciones de ID, taxonomías y QA viven en los documentos hermanos:
- `core_protocol.md` — principios, edge cases, `source_type`, `verification_status`, guardrails
- `output_contract.md` — estructura, reglas por sección, campos, QA, absence format
- `search_decomposition_rules.md` — cómo partir el input

---

## Template base

~~~
# Research Shard: <subject identifier>

**Direction statement:** <resumen breve del input de research>

---

## Search decomposition

- SD-01: <sub-búsqueda verificable>
- SD-02: <sub-búsqueda verificable>
- SD-NN: <sub-búsqueda verificable>

---

## Part 1 — Clean findings (direct_verified)

### F-01

**What:** <claim totalmente sostenido por el snippet>
**Verbatim snippet:** "<character-for-character, passage continuo>"
**Source:** <URL completa: protocolo + dominio + ruta>
**source_type:** <uno de los 18 valores del enum>
**verification_status:** direct_verified
**Date:** <fecha visible en página, o "Accessed [Month Year]; page undated">
**Notes:** <solo limitación local de verificación>

### F-02

(mismo formato)

Si no hay clean findings: None.

---

## Part 2 — Provisional findings (indirect_verified)

### F-P01

**What:** <claim>
**Verbatim snippet:** "<character-for-character>"
**Source:** <URL completa>
**source_type:** <enum value>
**verification_status:** indirect_verified
**Date:** <fecha o accessed date>
**Notes:** <método de recuperación: mirror, cache, archive, re-búsqueda>

### F-P02

(mismo formato)

Si no hay provisional findings: None.

---

## Part 3 — Pattern candidates (sealed)

### PC-01

**Pattern Candidate ID:** PC-01
**Candidate statement:** <descriptivo, no causal, sin lenguaje de fuerza de señal>
**Related Finding IDs:** F-01, F-03, F-P02
**Status:** sealed; not validated

### PC-02

(mismo formato)

Si no hay pattern candidates: None.

---

## Part 4 — Absence findings (opcional según agente)

### F-X01: <subject identifier para el absence>

**What:** No data found on <X>
**Verbatim snippet:** n/a — absence finding
**Source:** Searches: "<q1>"; "<q2>". Locations attempted: <list of URLs/domains checked>
**source_type:** unknown
**verification_status:** unrecoverable
**Date:** <search date>
**Notes:** searched locations only

### F-X02: <subject>

(mismo formato)

Si no hay absence findings o el agente no los produce: None.

**Recordatorio:** Part 4 contiene exclusivamente absence findings con `verification_status = unrecoverable`. Findings rechazados por edge case 2, 3 o 5, fetch failures de URLs, o queries exploratorias vacías NO van aquí — van a Research QA Notes. Ver `output_contract.md` Part 4 rules.

---

## Research QA Notes

- Findings rejected due to verification edge case: <list IDs intentados y razones (edge case 2/3/5), o "None">
- Multi-speaker pages split into separate findings: <list o "None applicable">
- Truncated or partial sources: <list o "None">
- source_type ambiguities: <list o "None">
- Coverage gaps where findings expected but not found: <list o "None">
- Cases where input could not be decomposed without interpretation: <list o "None">
- Strategies attempted by sub-búsqueda: <summary per SD-NN, si el agente específico lo requiere>
~~~

---

## Recordatorios sobre el template

**Finding ID convention (base):**
- Part 1 → `F-NN` (F-01, F-02, F-03...)
- Part 2 → `F-PNN` (F-P01, F-P02...)
- Part 4 → `F-XNN: <subject>` (F-X01: Kichink fees, F-X02: Gumroad LatAm...)
- Part 3 → `PC-NN` (referencia findings de Parts 1/2 por sus IDs)
- Secuencia por-Part, cada Part empieza en 01.

**Campos obligatorios por finding:**
Finding ID, What, Verbatim snippet, Source, source_type, verification_status, Date, Notes. Ver `output_contract.md` para reglas de cada campo. Los valores de `verification_status` son los tres activos: `direct_verified`, `indirect_verified`, `unrecoverable`. El valor `could_not_verify` está deprecated — ver `core_protocol.md` sección "Valor histórico deprecated" y `pipeline_vocabulary.yaml` en la raíz del repo.

**Antes de cerrar el output, ejecuta:**
1. QA de 12 puntos por finding (ver `output_contract.md`).
2. QA de shard completo (ver `output_contract.md`).

**Si no hay findings válidos:** entrega la estructura completa con `None` en cada Part. Nunca inventes findings para llenar la salida.

**Agentes con Parts adicionales:** el recovery agent extiende este template con Parts 1B y 2B para adjacent findings. Ver `agents/codex/phase0-recovery/CONTRACT.md` para el template extendido. Agentes nuevos deben declarar explícitamente cualquier extensión en su propio contrato.
