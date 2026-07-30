# CRITERIA — Etapa 2 re-extracción independiente (fable)

Copia literal del bloque CRITERIA aprobado en Etapa 1. Estas reglas se aplican
tal cual y no se renegocian. Los patrones nuevos detectados durante la corrida
se agregan al final, con marca del batch donde aparecieron; nunca se cambian
retroactivamente las reglas ya aplicadas.

=== CRITERIA (tus reglas de Etapa 1, literales) ===

uncertainties — enum del vocab phase-1 (core + phase_1_only = 17
valores). Valores vocab-only → schema_enum_conflict en manifest.

actor_level — enum de 9 valores del vocab. Aplica el
assignment_rule del vocabulario (pipeline_vocabulary.yaml:30-39):
actor = quién habla, no quién es afectado. help_center /
pricing_page / platform_doc / policy_page → platform, según la
regla del vocab.

platforms — SOLO plataformas nombradas en el texto de
snippet_primary + contextos. No listar plataformas que solo
aparecen en URL o título de la fuente. No inferir.

claim_type y evidence_role — se asignan independientemente según
su propio enum; no se fuerza coherencia entre ambos.

Multiplicidad de métricas — si el snippet trae más de una métrica:
la del claim principal va en metric_type / metric_value_raw /
metric_unit; las adicionales se anotan en parser_notes.

time_scope_normalized_if_safe — ISO-8601 truncado a la granularidad
declarada (2026-04, 2026). Solo con fecha explícita en snippet,
contexto o source_date_if_available. Qualifiers relativos
("currently") → raw sí, normalized null.

uncertainties vacío — [] cuando no hay incertidumbres (no ["none"]).

product_type_if_explicit — si no es explícito → "unknown", nunca
null (el oneOf del schema no admite null).

metric_value_raw — preservar como aparece; sin castear ni
normalizar formato.

geography_if_explicit — wording verbatim del snippet, sin
normalizar a ISO ni gentilicio.

Política de no determinable: campos enum → "unknown" + código de
uncertainties del vocab phase-1. Campos libres opcionales → null,
nota en parser_notes solo si la causa no es obvia. Caso no cubierto
por el contrato y sin fallback → valor más conservador o unknown +
issue contract_case_uncovered en manifest con campo y caso. Nunca
inferencia. El contrato manda primero (Regla 4, §16); si calla,
aplican estas reglas.

=== FIN CRITERIA ===

## Patrones nuevos (agregados durante la corrida)

Reglas operativas surgidas de casos no cubiertos por el bloque CRITERIA. Se
aplican desde el batch donde aparecieron en adelante; nunca retroactivamente.

- [batch_001] Métrica ausente vs no determinable: si el claim no contiene
  métrica alguna, metric_type = "unknown" SIN código de uncertainties (no hay
  ambigüedad, hay ausencia). El código (p. ej. metric_type_unclear) se reserva
  para métrica presente pero de naturaleza ambigua.
- [batch_001] metric_type out-of-enum solo cuando hay dimensión métrica
  observable con valor; la etiqueta usa el wording observado de la fuente.
  Sin valor numérico/observable → "unknown", no etiqueta out-of-enum.
- [batch_001] source_type database_profile → actor_level "source" (publicación
  de datos sin actor en primera persona; no cubierto por el assignment_rule).
- [batch_001] Stats vivos transcritos de layout ("Updated daily", agregados de
  reviews) → time_scope_raw null + uncertainty time_scope_unclear; la fecha de
  acceso queda solo en source_date_if_available.
- [batch_001] Menciones con rol no-plataforma (etiqueta de categoría, tema del
  curso, marca de tarjeta del comprador, nombre de persona) NO entran en
  platforms; se explica en parser_notes.
- [batch_002] Rieles de pago nombrados en el texto (PayPal, Payoneer, Stripe,
  dLocal, Wise, Visa/MasterCard/Amex como métodos aceptados) SÍ entran en
  platforms.
- [batch_002] Voz de plataforma en canal informal (respuesta de staff en foro,
  notificación citada): actor_level = platform; evidence_role = direct_claim
  (official_policy se reserva para documentos formales). Si el autor no está
  identificado, se agrega actor_level_unclear.
- [batch_002] pricing_page de terceros: aplica la cláusula más específica del
  assignment_rule (proveedor externo hablando de su propio producto →
  third_party); si no aplica, mapeo mecánico → platform + actor_level_unclear
  + parser_note.
- [batch_002] Snippet truncado a mitad de claim (o que responde a una pregunta
  no capturada) → context_insufficient.
- [batch_003] Cuentas de experiencia única en primera persona (reviews,
  quejas, posts de instructores) → anecdotal_single_source.
- [batch_003] Citas directas en primera persona dentro de journalism → actor
  del hablante citado (seller/buyer); narración en tercera persona → source +
  evidence_role reported_event.
- [batch_004] Roundups/comparativas publicadas por plataformas competidoras →
  author_conflict_of_interest_possible.
- [batch_004] Artefactos de skeleton (contenido extra del packet dentro de
  source_date_if_available u otros campos pre-poblados) → se copian verbatim y
  se registra issue "skeleton_artifact" en el manifest.
- [batch_005] Reviews de uso: comprador → evidence_role anecdotal_example;
  vendedor sobre su propia operación/resultados → seller_self_claim.
- [batch_006] Nombres de plataforma normalizados a la marca (Domestika,
  Payhip, PayPal) aunque la fuente use variantes (domestika.org, PayHip,
  Paypal); la variante verbatim se anota en parser_notes si difiere. (Los
  records previos con dominio, p. ej. kichink.com en batch_003, no se
  modifican retroactivamente.)
- [batch_008] Actor "mixed" cuando el snippet mezcla narración del medio y
  cita de otro actor, con claims de ambas voces.
- [batch_008] metric_type_unclear (vocab-only, phase_1_only) para métrica
  presente pero de referente ambiguo (qué cubre la tarifa); cada uso queda
  como schema_enum_conflict en el manifest.
- [batch_009] product_type_if_explicit out-of-enum: si la fuente nombra el
  tipo de producto explícitamente pero no mapea al enum sin ambigüedad
  ("digital journal", "digital guide"), el valor observado va en el campo y
  se flaggea out_of_enum. Tipos genéricos ("digital products") → unknown.
- [batch_009] time_scope_normalized_if_safe puede anclarse a fecha efectiva
  explícita registrada por el packet en source_date_if_available (permitido
  por CRITERIA), con parser_note del origen.
- [batch_010] snippet_needs_reopen (vocab-only, phase_1_only) cuando el
  packet elide/resume listas de layout y el contenido completo requeriría
  reabrir la fuente; cada uso queda como schema_enum_conflict.
- [batch_016] No se construyen etiquetas out-of-enum que no estén observadas
  (verbatim o cuasi-verbatim) en la fuente: si la métrica existe pero la
  fuente no la nombra de forma etiquetable, metric_type = unknown y el valor
  queda en qualifiers/parser_notes.

### Patrones nuevos — batches 025-032 (checkpoint 0004)
- [batch_027] Capturas de layout de páginas propias de un marketplace (portadas,
  categorías, filtros, selectores): actor marketplace; claim_type unknown si es puro
  chrome de UI, availability_statement si lista inventario/categorías/métodos de pago;
  evidencia observed_platform_state. Contenido dinámico no cargado ("Cargando...",
  "Loading results...") se registra como estado observado con nota — snippet_needs_reopen
  queda reservado a elisiones del lado del packet.
- [batch_027] Normalización temporal anclada a etiquetas de dato declaradas en
  source_date_if_available ("data labeled March 2026" → 2026-03; "data context
  November 2024" → 2024-11). [batch_031] Extiende a mes nombrado en el snippet +
  fecha de actualización de la fuente ("In February" + updated 2026-03-12 → 2026-02).
- [batch_028] Fechas numéricas DD/MM/AAAA con día >12 (sin lectura MM/DD posible) se
  consideran no ambiguas y se normalizan; con día ≤12 se preservan sin normalizar
  con nota de formato ambiguo.
- [batch_028] Listas de pares etiqueta·cifra sin etiqueta de métrica en el texto
  capturado (países·porcentaje, tags·conteo) → metric_type unknown +
  context_insufficient; cifras preservadas en snippet/notas.
- [batch_029] Voz de plataforma en directorios externos (descripción en primera
  persona del plugin propio en wordpress.com) → actor platform, direct_claim.
- [batch_030] Nombres de herramientas destino en títulos de productos o taglines de
  categorías (Canva, Figma, Goodnotes, VRChat, Procreate, Lightroom, Photoshop,
  Premiere, Final Cut) se incluyen en platforms — precedente Framer (batch pre-025).
  Marcas en rol de categoría temática (Lego) o nombres dentro de un título de
  producto sin rol de herramienta ("Apple Slides") no se incluyen.
- [batch_030] Plantillas para herramientas nombradas → product_type fuera de enum con
  etiqueta observada ("Canva template", "Figma Slides Template", "payhip template",
  "resume templates"), familia iniciada con "Framer templates".
- [batch_032] Tablas de distribución multi-métrica capturadas como layout →
  metric_type unknown con nota "sin métrica principal única" (cifras quedan verbatim
  en snippet_primary). Series temporales de una sola métrica etiquetada →
  metric_type fuera de enum con el valor más reciente como principal y la serie
  preservada en el snippet.
- [batch_032] Capturas obtenidas vía índice de Google o con narración/comentario
  editorial insertado por el packet ("[From Google search index snippet...]",
  "(likely a bug or unlimited stock indicator)") → se preservan tal cual + issue
  skeleton_artifact en el manifest.

### Patrones nuevos — batches 033-040 (checkpoint 0005)
- [batch_038] Skeletons cuyo snippet_primary es solo una nota del packet sin texto
  de la fuente ("n/a — content recovered via research subagent...") → rechazo con
  required_field_unfillable (subject_exact no rellenable).
- [batch_036] La autopromoción comparativa de una plataforma sobre sí misma
  ("Unlike other platforms", "leading the charge", "than anywhere else") lleva
  author_conflict_of_interest_possible también cuando aparece en blogs
  corporativos, portadas o pricing pages propios.
- [batch_037] Posts de creadores individuales alojados en el dominio de la
  plataforma (patreon.com/posts/...) → actor seller aunque el source_type del
  skeleton sea platform_doc; la voz manda sobre el tipo de fuente.
- [batch_039] Fees de procesadores de pago de terceros relayadas por el help
  center de una plataforma → pricing_statement + actor platform + direct_claim
  (no official_policy: la tarifa no es política de la plataforma); siempre con
  nota de capas ("collected by X and do not go to Y").
- [batch_039] Placeholders de plantilla sin sustituir en el texto fuente
  ('[Gateway name]') → se preservan verbatim + issue skeleton_artifact.
- [batch_039] Redes de tarjeta (Visa, Mastercard, American Express) nombradas en
  rol de rail de pago → se incluyen en platforms; como mera categoría temática no.
- [batch_040] Listas extensas de métodos/rails de pago soportados →
  payment_method_availability; los rails nombrados se incluyen en platforms de
  forma representativa (redes, wallets y rails ya presentes en el corpus) y la
  lista completa queda verbatim en snippet_primary.
- [batch_033] Referencias legales citadas por reclamantes (Artigo 49 CDC) se
  preservan como qualifiers sin valoración; nombres propios de reclamantes solo
  quedan en snippet_primary, no en subject_exact.

### Patrones nuevos — batches 041-048 (checkpoint 0006, final)
- [batch_041] Mismo texto fuente capturado en múltiples artifacts del corpus →
  se registra en cada artifact con nota de duplicación cruzada + issue
  skeleton_artifact; nunca se reconcilia ni se descarta ninguna captura.
- [batch_043] Testimonios de sellers curados por una plataforma en sus páginas
  de marketing ("Gumroad Alternative", portada de gumroad.com, hotmart.com/es/
  pagos) → actor seller, evidencia seller_self_claim, uncertainties
  anecdotal_single_source + author_conflict_of_interest_possible (contexto
  promocional curado).
- [batch_044] Comunicaciones oficiales de una plataforma citadas por terceros
  (email de Gumroad citado en foro Polycount) → voz de plataforma relayada:
  actor platform, direct_claim, con nota del canal de relay.
- [batch_044] Cifras "$79 pesos" y equivalentes ya tratados con
  metric_type_unclear en capturas previas del mismo texto → se replica el mismo
  tratamiento en capturas posteriores (consistencia intra-fuente).
- [batch_045] Fechas de vigencia duales o condicionales ("efectivo 2024-01-01 en
  algunos países / 2025-04-01 en los demás") → time_scope_normalized_if_safe
  null con nota; solo se normaliza vigencia única y explícita.
- [batch_046] Libros digitales comprados/descargados en plataformas de productos
  digitales ("book" con entrega digital, envío a Kindle, descarga) → ebook;
  "book" con entrega física pendiente o formato indeterminado → unknown.
