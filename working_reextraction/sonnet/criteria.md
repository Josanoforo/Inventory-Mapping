uncertainties — enum del vocab (core + phase_1_only = 17 valores);
no usar metric_unit_unclear ni platform_scope_unclear aunque el
schema los permita (el vocab los marca phase_2_only).

time_scope_normalized_if_safe — normalizar SOLO fecha completa
(día/mes/año o mes/año explícitos) o timeframe inequívoco
("Q1 2026", "as of April 2026" → ISO parcial: 2026-04, 2026).
Relativos ("currently", "at this time") → van a time_scope_raw
sin normalizar; normalized queda null.

actor_level / product_type_if_explicit / metric_type en forma
array — SOLO si el snippet mismo mezcla explícitamente dos valores
sin que uno sea dominante. Por defecto, single.

metric_value_raw — preservar el valor tal como aparece en el
snippet (string); nunca castear a number; no normalizar comas ni
decimales.

geography_if_explicit — preservar el wording del snippet verbatim;
sin normalizar a código ISO ni gentilicio.

Campos enum no determinables → "unknown" (valor legal) + código de
uncertainties correspondiente. Campos libres no determinables →
null o [], con nota en parser_notes explicando por qué. Nunca
inferencia. El contrato manda primero; si el contrato calla, aplica
estas reglas.

--- Agregado tras batch_008: Métricas de agregadores/bases de datos que no
mapean a ningún valor del enum metric_type (p.ej. conteo de creadores con
al menos un pagador, distribución de perfiles por categoría de contenido,
conteo agregado de quejas en una plataforma de terceros) se escriben como
string descriptivo literal (out_of_enum), nunca forzadas al valor "menos
malo" del enum (p.ej. active_buyers colapsaría conteo de creadores con
conteo de compradores). ---

--- Agregado tras batch_008: Bloques de estadísticas de ranking/database_profile
que combinan 2-3 métricas explícitas en un solo bloque visual sin que ninguna
domine (p.ej. paid-member count + monthly payout de una misma entidad rankeada)
se registran como metric_type en array con un solo metric_value_raw combinado
en string, no se separan en registros distintos si llegaron como una sola
unidad de snippet. ---

--- Agregado tras batch_008: Respuestas en foros de vendedores donde no es
determinable si quien responde es staff de la plataforma o un vendedor par
(p.ej. respuestas de soporte dirigidas por nombre de usuario en foros de
Domestika) se resuelven por defecto como actor_level "seller" (regla por
defecto del contrato para seller_forum), agregando actor_level_unclear a
uncertainties y una nota en parser_notes explicando la ambigüedad — nunca se
asume "platform" sin evidencia explícita de que quien habla es la plataforma
misma. ---

--- Agregado tras batch_016: source_type "buyer_review" no determina por sí
solo actor_level "buyer". Reseñas en sitios de terceros (Trustpilot, BBB) que
mecánicamente llevan source_type=buyer_review pueden estar escritas por
sellers/creators quejándose de payouts, suspensiones de cuenta o fees — el
texto mismo revela quién habla ("I am a seller on Gumroad...", "sells items
with full resale rights"). Se aplica la regla general del contrato ("quién
habla, no source_type") y se asigna actor_level "seller" cuando el hablante se
identifica explícitamente como vendedor/creador, independientemente de la
etiqueta mecánica de source_type. ---

--- Agregado tras batch_016: Snippets truncados con elipsis final ("...") en
reviews de terceros (Trustpilot) o en listados/tablas parcialmente capturados
(listas de países, monedas) no se rechazan por esta razón sola. Se preservan
como aparecen, se registra uncertainties: context_insufficient, y se agrega
una nota en parser_notes indicando que el fragmento está incompleto y que el
valor final (p.ej. cifra exacta, país completo de la lista) no está
disponible en el snippet capturado. Solo se rechaza (subject_exact
unfillable) si el truncamiento deja el sujeto mismo indeterminable, no solo
un detalle secundario. ---

--- Agregado tras batch_040: Skeletons cuyo snippet_primary es enteramente un
placeholder de recuperación fallida (p.ej. "n/a — content recovered via research
subagent's direct fetch of X; verbatim character-for-character accuracy cannot be
independently confirmed") sin ningún texto real de la página capturado, se rechazan
por subject_exact_unfillable — no hay afirmación real que sostenga un sujeto. No
confundir con snippets truncados con "..." (batch_016), que sí preservan texto real
parcial y no se rechazan por esa razón sola. ---

--- Agregado tras batch_040: Cifras de CTR o de variación porcentual que exceden el
rango normal 0-100% (p.ej. "12-mo average CTR is 127%", "monthly CTR up 892%") se
preservan verbatim tal como las reporta la fuente de terceros, sin corregir ni
reinterpretar. No se usa metric_unit_unclear (phase_2_only, prohibido en Fase 1);
se usa methodology_unclear si se necesita marcar la anomalía. ---

--- Agregado tras batch_040: Nombres de moneda (p.ej. "mexican peso",
"Brazilian Real", "Colombian Pesos", "Argentine Pesos") implican geografía
pero no son, por sí mismos, un nombre de lugar explícito en el snippet.
geography_if_explicit se deja null cuando la única señal geográfica es el
nombre de una moneda, con nota en parser_notes explicando la inferencia
implícita descartada; se prioriza esta regla sobre inferir el país a partir
del gentilicio de la moneda, salvo que el mismo snippet nombre el país o
gentilicio de forma independiente (p.ej. "Argentine Pesos" Y "Argentina" both
appearing, or an adjective form like "mexicano/mexican" modifying a noun
directly, en cuyo caso el adjetivo sí cuenta como explícito). ---
