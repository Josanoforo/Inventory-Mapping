# Checkpoint 0800 — batches 001-032

Re-extracción independiente y paralela (ejercicio, no corrida oficial de pipeline).
Este checkpoint cierra la cuarta llamada de la serie (batches 025-032), acumulando
sobre el estado dejado por las tres llamadas previas (batches 001-024).

## Conteo acumulado total (batches 1-32)

- Skeletons procesados: 800
- Records escritos a `records/`: 800
- Records rechazados a `rejected_archive/`: 0
- status del manifest: `in_progress` (se mantiene; batch_048 es quien lo cierra)

## Distribución de out_of_enum por campo (acumulada, batches 1-32)

- `metric_type`: 5 ocurrencias (sin cambios respecto al checkpoint anterior)
  - `paid_creator_count`: 2
  - `content_category_distribution`: 2
  - `complaint_count`: 1

Todas las 5 ocurrencias provienen de batches 001-008 (primera llamada). El rango de
esta llamada (batch_025 a batch_032) no produjo ningún valor out_of_enum nuevo, pese a
contener material con métricas potencialmente atípicas (conteos de productos por
etiqueta de búsqueda en Gumroad Discover, conteo de sitios usando Lemon Squeezy,
market-share estimado de un proveedor de datos B2B) — todos se resolvieron con
`metric_type: unknown` + `metric_value_raw` string descriptivo verbatim, sin necesitar
un valor fuera de enum.

## Distribución de schema_enum_conflict (acumulada, batches 1-32)

- 1 ocurrencia (sin cambios), campo `uncertainties`, valor de vocabulario deseado
  `metric_type_unclear`, registrado en batch_010. El rango de esta llamada (025-032) no
  produjo ninguna ocurrencia nueva.

## Patrones de ambigüedad en batches 025-032

No se encontraron patrones genuinamente nuevos que requieran una regla adicional en
`criteria.md`. Los patrones observados en este rango ya estaban cubiertos por reglas
existentes (incluyendo las agregadas tras batch_008 y batch_016):

- Gran volumen de bloques de estadísticas de agregadores de datos (semrush, similarweb,
  marketplacepulse, storeleads, gumtrends, tracxn, 6sense, insightraider, electroiq,
  whop) combinando 2-4 métricas explícitas en un solo snippet sin dominancia (p.ej.
  tabla de Gumroad por rango de precio con # productos + % revenue + avg sales + total
  revenue; tabla PWYW vs fixed price de Gumroad): resueltos con `metric_type` en array y
  `metric_value_raw` combinado en un string, condensando tablas largas (8-19 filas) a los
  extremos representativos en `metric_value_raw` con nota en `parser_notes` señalando que
  el snippet_primary preserva la tabla completa verbatim. Consistente con la regla de
  batch_008.
- `actor_level` para páginas de listado de productos (`product_listing`) distinguido por
  quién efectivamente habla: tiendas de un vendedor individual (Payhip/Lemon Squeezy
  storefronts como `purgeitwithpatti`, `NTTsolmare`, `idearupt`, `laragon`,
  `notioneverything`, `uipress`, `amdesigns`) → `seller`; páginas de exploración
  agregada multi-vendedor (Gumroad Discover, Kichink homepage/búsqueda, Payhip
  marketplace por categoría) → `marketplace`; herramientas/plugins/integraciones de
  terceros promocionando su propio servicio sobre la plataforma estudiada (Pipedream,
  Pabbly, Zapier, plugins de WordPress, extensiones de Chrome, apps de terceros) →
  `third_party`, conforme a `assignment_rule` de `actor` en `pipeline_vocabulary.yaml`.
- Múltiples reviews de Trustpilot (Patreon, Etsy, Hotmart ES) con quejas de cobros no
  autorizados, "cuentas fantasma" de suscripción, o disputas de reembolso: se mantuvo
  `actor_level: buyer` (quien habla es el comprador/suscriptor afectado, no un vendedor),
  `evidence_role: anecdotal_example`, sin inferir intención fraudulenta de la plataforma
  como hecho verificado — solo se registró la queja tal como aparece.
  Un fragmento truncado de una sola línea sin contexto ("Ni devolución, de mi dinero, ni
  respuesta de mi petición") se preservó con `uncertainties: context_insufficient` y nota
  en `parser_notes`, sin rechazar, siguiendo la regla de batch_016 (el sujeto — queja de
  reembolso/respuesta — seguía siendo determinable).
- Snippets que citan directamente a un ejecutivo de la plataforma estudiada dentro de un
  artículo de un tercero (transcripciones de earnings calls de Etsy en fool.com,
  retaildive, digitalcommerce360) se etiquetaron `actor_level: platform` porque quien
  habla en la cita es la plataforma misma, no el medio que la reporta — consistente con
  la regla general del contrato ("quién habla, no source_type/medio contenedor").
- Cifras de precio en múltiples monedas dentro de un mismo snippet (TZS, MXN, EUR, GBP,
  USD) declaradas explícitamente como mixtas en `metric_unit` (p.ej. "USD and EUR (mixed,
  declared)"), sin normalizar ni convertir, conforme a la regla transversal de "mixed
  units must be declared, not hidden".

No se agregó ninguna regla nueva a `criteria.md` en este rango.

## Notas adicionales de ejecución

- Se procesaron 200 skeletons nuevos (batch_025 a batch_032), en orden numérico de
  batch y alfabético de filename dentro de cada batch, sin reprocesar ninguno de los 600
  ya registrados por las llamadas anteriores.
- 0 records rechazados en este rango (subject_exact fue llenable en los 200 casos).
- No se leyó, abrió ni hizo grep sobre `working/data_extraction/records/` (el corpus ya
  poblado por el otro proceso) en ningún momento de esta llamada.
- Todos los 200 records nuevos fueron validados programáticamente contra
  `data_extraction_record.schema.json` (jsonschema) antes de este checkpoint; 0 errores
  de validación en el rango nuevo.
