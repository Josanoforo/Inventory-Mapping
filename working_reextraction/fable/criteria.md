# CRITERIA — Etapa 2 (reglas de Etapa 1, literales)

=== CRITERIA (tus reglas de Etapa 1, literales) ===

A. uncertainties: vocab gana sobre schema. Uso el enum vocab phase-1
(core + source_type_unclear, metric_type_unclear, snippet_needs_reopen
= 17 valores); no uso metric_unit_unclear ni platform_scope_unclear
aunque el schema los permita. Cada valor vocab-only → manifest como
schema_enum_conflict; no es out_of_enum.

B. metric_type: enum cerrado per vocab (20 valores). Si el valor real
no está, valor observado + out_of_enum.

C. product_type_if_explicit: si no es explícito → "unknown", nunca
null.

D. actor_level: enum de 9 valores + assignment_rule del vocabulario
("quién habla, no quién es afectado"; pipeline_vocabulary.yaml:30-39).

E. claim_type y evidence_role se asignan independientemente según cada
enum, sin forzar coherencia entre ambos.

F. platforms: solo del texto de snippet_primary + contextos. Plataforma
que solo aparece en URL o título no se lista.

G. time_scope_normalized_if_safe: ISO-8601 truncado a la granularidad
declarada (2026-04, 2026), solo con fecha explícita en snippet,
contexto o source_date_if_available; relativos ("currently") → raw sí,
normalized null.

H. Multiplicidad métrica: la métrica del claim principal va en
metric_type/metric_value_raw/metric_unit; las adicionales en
parser_notes.

I. uncertainties sin incertidumbres → [] (array vacío), no ["none"].

J. subject_exact es frase libre fiel al claim; parser_notes son notas
operativas, nunca interpretación estratégica.

Arrays en actor_level / product_type_if_explicit / metric_type: SOLO si
el snippet mismo mezcla explícitamente dos valores sin dominante; por
defecto, single.

metric_value_raw: preservar como string tal cual aparece; nunca castear
a number; sin normalizar comas ni decimales.

geography_if_explicit: wording del snippet verbatim; sin ISO ni
gentilicio.

Política de no determinable: campos enum → "unknown" + código de
uncertainties del vocab phase-1, nunca el enum menos malo. Campos
libres → null o [], nota en parser_notes solo si la causa no es obvia.
subject_exact infillable → rejected_archive con
required_field_unfillable, no se inventa. Caso no cubierto por el
contrato → valor más conservador o unknown + issue
contract_case_uncovered en manifest con campo y caso. Nunca inferencia:
plataformas no nombradas en el texto no se listan; geografía no
explícita no se llena. El contrato manda primero (Rule 4, §16); si
calla, aplican estas reglas.

=== FIN CRITERIA ===
