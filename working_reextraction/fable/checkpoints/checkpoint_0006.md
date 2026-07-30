# Checkpoint 0006 — tras batch_048 (FINAL)

## Conteo acumulado final
- Skeletons procesados: 1178 / 1178 (48 batches, status: complete)
- Records escritos: 1172
- Rechazados: 6 (todos con required_field_unfillable)
- Records con out_of_enum: 133
- Records con schema_enum_conflict: 5

## Rechazos (6)
- batch_002: 0ffe7308-...-012-SNP-002 — fila de tabla sin encabezados; subject_exact
  no rellenable.
- batch_038 (×5): de144e73-...-008/011/012/015/016-SNP-001 — snippet_primary con
  solo nota del packet ("n/a — content recovered via research subagent..."), sin
  contenido de la fuente.

## schema_enum_conflict (5 records; usos legítimos del vocabulario fase 1
no presentes en el enum del schema)
- metric_type_unclear ×3: tarifa "$79 pesos" de Kichink (batches 008, 013 y su
  tercera captura en batch_041).
- snippet_needs_reopen ×2: listas de layout elididas por el packet (Lemon Squeezy,
  batch_010).

## Distribución de out_of_enum por campo
- metric_type: 122 usos en 111 records — familias: conteos de entidades y
  catálogo (creators, sellers, subscribers, patrons, podcasters, estudiantes,
  usuarios, customers, companies, websites, apps, listings, products, digital
  products, cursos, live/active stores...), retenciones y impuestos (IVA, VAT,
  tax/royalty withholding), compensación (commission/comisión, royalties,
  savings, credits, discount), umbrales de payout (minimum payout threshold/
  balance, retiro mínimo, valor mínimo para retiro), plazos (plazo de depósito,
  plazo máximo, credit validity), métricas corporativas (GMS, GMV, funding
  raised, customer retention, push and email clicks), métricas de tráfico y
  búsqueda no cubiertas (Bounce Rate, audience, search volume, search score,
  CTR, global ranking, download speed) y misceláneos.
- product_type_if_explicit: 11 usos — familia de plantillas/temas por herramienta
  destino (Framer templates ×2, Canva template, Figma Slides Template, payhip
  template, resume templates, WordPress Theme, Shopify Theme) y digitales no
  mapeados (digital journal ×2, digital guide).

## Patrones nuevos desde checkpoint 0005 (batches 041-048)
- [batch_041] Capturas del mismo texto fuente en distintos artifacts del corpus:
  se registran en todos con nota de duplicación e issue skeleton_artifact, sin
  reconciliar (aplicado también a los duplicados de pricing de Gumroad en
  batches 044, 046 y 047).
- [batch_043] Testimonios de sellers curados en páginas de marketing de una
  plataforma → actor seller + seller_self_claim + anecdotal_single_source +
  author_conflict_of_interest_possible.
- [batch_044] Emails/anuncios de una plataforma citados por usuarios en foros →
  voz de plataforma relayada: actor platform + direct_claim con nota del canal.
- [batch_045] Vigencias duales declaradas ("2024-01-01 algunos países /
  2025-04-01 los demás") → no se normaliza; nota explicativa.
