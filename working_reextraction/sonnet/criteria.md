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
