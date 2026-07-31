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

---

# Adiciones (patrones no cubiertos por CRITERIA; nunca retroactivas)

## [batch_008] — registradas en checkpoint_0001
K1. Normalización temporal desde metadata de página (extiende G): una fecha de
    contenido explícita en source_date_if_available (publicado / last updated /
    reviewed / effective / changelog / fecha de post) normaliza el time_scope de
    claims que describen ESTADO vigente (política, pricing, disponibilidad,
    comparativa) cuando time_scope_raw es null. Fechas solo de acceso
    ("Accessed ...") NUNCA normalizan. Eventos o anécdotas narradas NO toman la
    fecha de publicación; solo normalizan si el propio claim trae fecha
    explícita. Si raw es relativo ("currently", "now") → normalized null (G literal).
K2. Fechas aproximadas ("~2025", "circa") no normalizan y añaden source_date_unclear.
    Mes sin año en snippet no se normaliza aunque la fecha de página permita
    inferir el año.
K3. platforms (afina F): una mención textual solo cuenta si nombra la
    plataforma/servicio como tal; etiquetas de categoría, temas de curso o
    nombres de creadores que coinciden con nombres de plataforma se excluyen
    con parser_note.
K4. author_conflict_of_interest_possible se asigna a voz promocional en primera
    persona sobre producto/servicio propio (vendor listings, blogs de plataforma
    sobre sí misma o competidores, posts con link de afiliado).
K5. metric_type out-of-enum: si la fuente da una etiqueta ("Paid Members",
    "Number of Paid Creators", "plazo máximo de activación") se copia verbatim;
    si no hay etiqueta, descriptor mínimo en snake/espacios + cita del wording
    en parser_notes.
K6. evidence_role para voz de plataforma: official_policy solo para documentos
    de política/help/legal/pricing formales y anuncios de política; respuestas
    de soporte en foros y copy de marketing → direct_claim.
K7. actor_level para source_types no mapeados por la assignment_rule
    (report, news, unknown, buyer_review, interview, database_profile) y para
    autores atípicos (blog de plataforma, blog de competidor, staff en foro):
    se asigna por "quién habla" (regla D) y se registra issue
    contract_case_uncovered por record. Rol del hablante indeterminable →
    unknown + actor_level_unclear.

## [batch_016] — registradas en checkpoint_0002
K8. Snippets truncados (elipsis final, corte a media palabra, listas de layout
    con "...") → uncertainties += snippet_needs_reopen y parser_note; el
    contenido faltante no se reconstruye ni se infiere.
K9. buyer_review con voz de vendedor (quejas de cuenta/payout de creadores en
    sitios de reseñas) → actor_level seller por "quién habla" (extiende K7),
    con issue contract_case_uncovered; el source_type prefijado se preserva.

## [batch_032] — registradas en checkpoint_0004
K10. Capturas de tablas/layout de sitios analíticos ("[Stated in layout: ...]"):
     la tabla completa se preserva verbatim en metric_value_raw en orden de
     listado, las unidades mixtas se declaran en metric_unit ("mixed: ..."), y
     metric_type recibe descriptor mínimo K5 (p. ej. "revenue by category",
     "store count by category"). La anotación de captura ("[Stated in layout:",
     "[From Google search index snippet") se registra en parser_notes y no se
     trata como truncación K8.
K11. Páginas con voz de plataforma prefijadas con source_type de vendedor
     (product_listing de páginas de features/pricing/partner/navegación, blog
     corporativo, article de help-center): actor_level por "quién habla"
     (platform) + issue contract_case_uncovered (extiende K7). Los listados
     genuinos de productos de vendedores mantienen third_party según la
     assignment_rule sin issue.
K12. Proveedores de datos/analítica reportando estimaciones sobre una
     plataforma (Semrush, SimilarWeb, 6sense, Storeleads, Gumtrends,
     Wappalyzer, ful.io) → actor "source" + methodology_unclear si la cifra es
     estimación sin metodología declarada. Proveedores de
     integraciones/herramientas promocionando su propia integración con la
     plataforma (Zapier, Pipedream, Pabbly, Make, widgets, apps) → actor
     "third_party" + author_conflict_of_interest_possible (K4).

## [batch_040] — registradas en checkpoint_0005
K13. Skeletons sin contenido de fuente (snippet_primary consiste solo en una
     nota de recuperación tipo "n/a — content recovered via research
     subagent..."): subject_exact es irrellenable sin inferencia → destino
     rejected_archive con required_field_unfillable, citando la nota en el
     detalle. El contenido nunca se reconstruye desde source_title ni la URL.
K14. Fees de pasarelas de pago de terceros relatadas por la plataforma en
     help-center ("Connect your X account"): claim pricing_statement con
     metric_type fee_rate (unidades mixtas declaradas), la pasarela y demás
     métodos de pago se excluyen de platforms (extiende K3), y el descargo
     "collected by X and do not go to [platform]" se copia como qualifier.
     Las listas de países soportados van como payment_method_availability
     con geography verbatim y el listado completo preservado.

## [batch_048] — registradas en checkpoint_0006 (final)
K15. Testimonios de vendedores curados en páginas de marketing de la
     plataforma: actor "seller" por quién habla + issue K7, evidence
     seller_self_claim, y uncertainties anecdotal_single_source +
     author_conflict_of_interest_possible por el contexto promocional curado.
K16. Páginas de comparación/"alternative" alojadas por una plataforma
     competidora que se compara a sí misma: actor "platform" por quién habla
     (K11) + issue + author_conflict_of_interest_possible (K4). Vendedores
     que comparan a terceros sin ser sujeto de la comparación → "third_party"
     + K4. Emails o anuncios de plataforma citados dentro de foros → actor
     "platform" + evidence reported_event.
