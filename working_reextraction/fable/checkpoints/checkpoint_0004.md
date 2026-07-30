# Checkpoint 0004 — tras batch_032

## Conteo acumulado
- Skeletons procesados: 800 / 1178
- Records escritos: 799
- Rechazados: 1 (sin cambios desde batch_002)
- Records con out_of_enum: 102
- Records con schema_enum_conflict: 4 (sin cambios desde checkpoint 0002)

## Distribución de out_of_enum por campo
- metric_type: 93 — familias previas (conteos de entidades, retenciones, compensación,
  umbrales de payout, plazos, misceláneos) más las nuevas de los batches 025-032:
  conteos de suscriptores/patrons/podcasters/creators (paying subscribers, podcasters,
  patrons, subscribers, creators), conteos de inventario/adopción (productos
  registrados, digital products, products, new products, websites, apps, applications,
  customers, companies, live stores, active stores, usuarios, outstanding orders),
  GMS y métricas de engagement corporativo (GMS, push and email clicks, audience),
  límites técnicos (file size), comisión de partners (commission), y share de formato
  (digital downloads, buyers pay above the minimum price).
- product_type_if_explicit: 9 — "digital journal" ×2, "digital guide",
  "Framer templates" ×2, "Canva template", "Figma Slides Template",
  "payhip template", "resume templates".

## Patrones nuevos desde checkpoint 0003
Registrados en criteria.md con marcador de batch:
- Capturas de layout de páginas propias de marketplace (Kichink, Payhip, Gumroad):
  actor marketplace; claim unknown para chrome puro, availability_statement para
  inventario/categorías; "Cargando..." es estado observado, no snippet_needs_reopen.
- Normalización temporal anclada a etiquetas de dato en source_date_if_available
  ("data labeled March 2026" → 2026-03; mes nombrado + fecha de actualización).
- Fechas DD/MM con día >12 (sin ambigüedad posible) se normalizan; ambiguas no.
- Listas de pares valor·cifra sin etiqueta de métrica → metric_type unknown +
  context_insufficient, cifras preservadas.
- Tablas de distribución multi-métrica → metric_type unknown, "sin métrica principal
  única"; series temporales de una métrica etiquetada → out_of_enum con el valor
  más reciente como principal.
- Nombres de herramientas en títulos de productos (Canva, Figma, Goodnotes, VRChat,
  Procreate...) se incluyen en platforms (precedente Framer); marcas en rol de
  categoría temática (Lego) no.
- Capturas vía índice de Google o con narración/comentario editorial del packet →
  issue skeleton_artifact.
- Voz de plataforma en directorios externos (plugin propio en wordpress.com) →
  actor platform.
