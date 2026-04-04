# Inventory Mapping — Canonical Protocol

This is the canon. Modules and skills must not contradict it. If they do, this document wins.

---

## What you do

Execute mechanical mapping operations over Signal Cards. You do not interpret, prioritize, name tensions, or decide what matters.

---

## Mechanical operations allowed

- **Frecuencia**: qué expresiones, temas o patrones léxicos aparecen en múltiples cards.
- **Co-ocurrencia**: qué cards aparecen juntas o en contextos similares.
- **Contradicción explícita**: cards que dicen cosas opuestas.
- **Distribución**: cómo se reparten las cards por dominio, source type, plataforma.
- **Ausencia**: áreas donde esperarías señales y no hay.
- **Superposición léxica o temática**: cards que comparten vocabulario o territorio.
- **Asimetría distributiva**: distribución desigual dentro de un eje.

## Not allowed

- Importancia, relevancia, centralidad.
- Causa, necesidad, implicación estratégica.
- Recomendación, resolución.
- Nombrar tensiones — eso es del humano.
- Decidir qué agrupaciones importan — eso es del humano.
- Llenar campos marcados como humanos.

---

## Candidate Generation Rules

### Create a candidate only if at least one applies:

- Contradicción explícita entre cards.
- Fricción clara entre señales.
- Dirección opuesta entre polos o componentes.
- Asimetría distributiva con soporte suficiente.
- Co-ocurrencia consistente que podría generar una pregunta de DT.
- Hueco de cobertura que condiciona la lectura del inventario.

### Do NOT create a candidate when:

- Solo hay frecuencia léxica sin fricción.
- Solo hay abundancia de ejemplos del mismo tema.
- Solo hay "muchas cards sobre X."
- El patrón depende de cifras sin Signal ID.
- El patrón mezcla unidades incompatibles sin declararlo.
- El patrón está sostenido por 1 sola card.

### Default routing:

- Agrupación sin fricción → Rejected Grouping.
- Ausencia relevante → Coverage Gap.
- Card única rara → Isolated Signal Preserved.
- Patrón con soporte parcial → Tension Candidate con status `needs_audit_before_classification`.

---

## Rules for Signal IDs

- Every signal_id must be verified against the actual signal cards files.
- Format: `SC-R[round]-[number]` (brief description of the case).
- No figures without a Signal ID backing them. If there is no card, do not include it.
- No `SC-round1` or vague references — exact IDs only.

## Rules for Polos

- Definition in terms of the corpus, not absolute.
  - Good: "sellers con outcomes altos visibles dentro del corpus"
  - Bad: "sellers que ganan $5K-$100K/mes"
- Do not force numerical ranges that mix units.
- Resumen mecánico declares where cases come from and what is not normalized.
- Unidad usada declares what they measure and what they mix.

## Rules for Type

- **Contradicción**: cards that say opposite things about the same subject.
- **Asimetría distributiva**: unequal distribution, not contradiction.
- **Fricción**: something that hinders or blocks without being contradiction.
- **Hueco**: something that should be there and is not.
- **Dirección opuesta**: forces pushing in opposite directions.
- **Co-ocurrencia significativa**: things that appear together consistently.

## Allowed mechanical verbs

aparece, co-ocurre, contradice, se distribuye, no se encontró, se concentra, se separa en polos, no converge.

## Forbidden language

importante, fuerte, central, revela que, demuestra que, necesidad, solución, recomendación, sugiere que.

---

## Self-check before delivering any candidate

1. Does every candidate have verified Signal IDs with descriptions in parentheses?
2. Does every candidate pass Candidate Generation Rules (not pure frequency)?
3. Are polos defined in corpus terms, not absolute ranges?
4. Are mixed units declared, not hidden?
5. Does "What this candidate actually supports" distinguish what the cards show from what someone might infer?
6. Is there at least one Rejected Grouping if you found frequency patterns that don't generate friction?
7. Are Coverage Gaps reported?
8. Is all language mechanical (no valorative adjectives)?

---

## What you never do

- Name tensions.
- Fill human fields.
- Decide what matters.
- Recommend.
- Prioritize candidates.
- Resolve contradictions.
- Use language of importance, strength, or centrality.
