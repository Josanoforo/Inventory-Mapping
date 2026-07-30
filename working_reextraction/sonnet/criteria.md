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
