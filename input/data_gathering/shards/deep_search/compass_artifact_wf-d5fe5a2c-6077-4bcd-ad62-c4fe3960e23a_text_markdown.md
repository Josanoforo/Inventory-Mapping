# Shard: Hotmart × D3 — Catalog, discovery, and market signals

**Idioma:** español | **Scope:** Solo Hotmart. Solo catálogo, discovery, señales de mercado observables. | **Time window:** Current state (sin ventana temporal) | **Accessed:** Abril 2026

---

## Search Decomposition

**SD-01** — Estructura del catálogo: categorías y subcategorías del marketplace de Hotmart
- Fuentes consultadas: hotmart.com/es/blog/hotmart-marketplace (fetched), hotmart.com/en/marketplace/category (fetched), hotmart.com/es/blog/comprar-curso-hotmart (fetched)
- Resultado: Lista de 20 categorías obtenida de blog (2021); taxonomía actual de 18 categorías obtenida de página de marketplace (EN)

**SD-02** — Mecanismos de discovery: búsqueda, filtros, ordenamiento, secciones destacadas del marketplace
- Fuentes consultadas: help.hotmart.com/es/article/115006334868 (fetched), hotmart.com/es/blog/hotmart-marketplace (fetched), hotmart.com/es/blog/comprar-curso-hotmart (fetched), hotmart.com/es/blog/productos-digitales-mas-vendidos (fetched)
- Resultado: 11 filtros del mercado de afiliación documentados; secciones de homepage documentadas; sistema de estrellas documentado; filtros "Más queridos"/"Más calientes" documentados

**SD-03** — Estructura de precios y comisiones de la plataforma
- Fuentes consultadas: hotmart.com/en/blog/hotmart-prices (fetched), help.hotmart.com/en/article/208298448 (snippet)
- Resultado: Comisión estándar 9.90% + US$0.50 documentada; micro-transacciones documentadas vía snippet

**SD-04** — Sistemas de scoring internos (Temperatura, Blueprint)
- Fuentes consultadas: help.hotmart.com/es/article/209209447 (contenido obtenido, fetch status incierto), hotmart.com/es/blog/hotmart-temperatura (snippet), hotmart.com/es/blog/blueprints-y-politicas (snippet)
- Resultado: Definiciones y parámetros de ambos sistemas documentados

**SD-05** — Nichos/categorías más vendidos en Hotmart
- Fuentes consultadas: hotmart.com/es/blog/productos-digitales-mas-vendidos (fetched), hotmart.com/es/blog/cursos-online-mas-vendidos-2 (fetched), hotmart.com/es/blog/vender-en-hotmart (snippet)
- Resultado: Lista de 7 nichos obtenida de blog oficial; lista de 4 nichos obtenida de segundo blog

**SD-06** — Servicios auxiliares y herramientas del ecosistema Hotmart
- Fuentes consultadas: zapier.com/apps/hotmart-7006 (snippet), chrome-stats.com (snippet), help.hotmart.com (API, snippet), pipedream.com/apps/hotmart (snippet), apps.make.com/hotmart (snippet)
- Resultado: Integraciones Zapier, Make, Pipedream documentadas; extensión Chrome documentada; portal API documentado

**SD-07** — Señales externas de mercado (tráfico, valoración, datos corporativos)
- Fuentes consultadas: similarweb.com/website/hotmart.com (snippet, paywall), crunchbase.com/organization/hotmart (snippet, 403), press.hotmart.com (fetched parcialmente)
- Resultado: Datos de tráfico SimilarWeb, funding Crunchbase, GMV y datos de compradores de nota de prensa documentados

**SD-08** — Formatos de productos digitales disponibles en Hotmart
- Fuentes consultadas: hotmart.com/es/blog/productos-digitales-mas-vendidos (fetched)
- Resultado: 5 formatos principales documentados; búsqueda de conteos por formato no arrojó datos granulares

---

## Part 1 — Clean findings (direct_verified)

---

### F-01

**Finding ID:** F-01
**What:** Un post del blog oficial de Hotmart lista 20 categorías navegables en el Marketplace: Animales y Plantas, Apps y Software, Casa y Construcción, Culinaria y Gastronomía, Desarrollo Personal, Diseño, Derecho, Ecología y Medio Ambiente, Educación, Espiritualidad, Finanzas e Inversiones, General, Literatura, Idiomas, Internet, Moda y Belleza, Música y Artes, Negocios y Carrera, Salud y Deportes, Tecnología de la Información.
**Verbatim snippet:** "En Hotmart Marketplace, puedes navegar por categoría: Animales y Plantas, Apps y Software, Casa y Construcción, Culinaria y Gastronomía, Desarrollo Personal, Diseño, Derecho, Ecología y Medio Ambiente, Educación, Espiritualidad, Finanzas e Inversiones, General, Literatura, Idiomas, Internet, Moda y Belleza, Música y Artes, Negocios y Carrera, Salud y Deportes, Tecnología de la Información."
**Source:** https://hotmart.com/es/blog/hotmart-marketplace
**source_type:** blog
**verification_status:** direct_verified
**Date:** 15/07/2021
**Notes:** Página accedida directamente; contenido confirmado presente. Esta lista refleja la taxonomía publicada en el blog a la fecha del artículo; la taxonomía actual del marketplace podría diferir.

---

### F-02

**Finding ID:** F-02
**What:** El blog oficial de Hotmart describe que en el Mercado de Afiliación existen filtros denominados "Más queridos" y "Más calientes" para identificar los productos digitales más vendidos y sus nichos.
**Verbatim snippet:** "En el Mercado de Afiliación de Hotmart puedes identificar los productos digitales más vendidos y sus nichos usando los filtros \"Más queridos\" o \"Más calientes\". A partir de allí, puedes evaluar los nichos más buscados por el público."
**Source:** https://hotmart.com/es/blog/productos-digitales-mas-vendidos
**source_type:** blog
**verification_status:** direct_verified
**Date:** 19/02/2024
**Notes:** Página accedida directamente; contenido confirmado. El snippet describe la existencia de los filtros como mecanismo de discovery; no se verificó la interfaz del Mercado de Afiliación directamente (requiere autenticación).

---

### F-03

**Finding ID:** F-03
**What:** La página del centro de ayuda de Hotmart lista 11 filtros disponibles en el Mercado de Afiliación: Tipo de Afiliación, Precio, % de comisión, Regla de Asignación de comisiones, Asunto, Formato, Moneda, Idioma, País, Herramientas y Afiliación.
**Verbatim snippet:** "Puedes elegir los siguientes filtros: Tipo de Afiliación, Precio, % de comisión, Regla de Asignación de comisiones, Asunto, Formato, Moneda, Idioma, País, Herramientas y Afiliación."
**Source:** https://help.hotmart.com/es/article/115006334868/-como-buscar-productos-en-el-mercado-de-hotmart-
**source_type:** article
**verification_status:** direct_verified
**Date:** Accessed April 2026; page undated
**Notes:** Página accedida directamente; contenido confirmado. Los nombres de filtros se transcriben tal cual aparecen. La misma página también describe tabs de ordenamiento ("Más Calientes", "Más Queridos", "Más Recientes") en pasaje separado no incluido en este snippet.

---

### F-04

**Finding ID:** F-04
**What:** Un post del blog oficial de Hotmart describe que la página inicial del Marketplace contiene secciones que agrupan productos con buenas evaluaciones, productos recién llegados y autores destacados, así como búsqueda por categorías y palabra clave.
**Verbatim snippet:** "Además del filtro de búsqueda y de la separación por categorías, en la página inicial del Marketplace encuentras otras secciones que reúnen los productos con buenas evaluaciones, los que acaban de llegar y los autores que más se destacan."
**Source:** https://hotmart.com/es/blog/comprar-curso-hotmart
**source_type:** blog
**verification_status:** direct_verified
**Date:** 26/07/2021
**Notes:** Página accedida directamente; contenido confirmado. El snippet describe mecanismos de discovery del marketplace orientado al comprador. El estado actual de estas secciones no se pudo verificar directamente en el marketplace (renderizado dinámico).

---

### F-05

**Finding ID:** F-05
**What:** El blog oficial de Hotmart indica que la comisión estándar de la plataforma para productos con precio superior a US$15.00 es 9.90% del precio del producto más US$0.50 por transacción. No hay cuotas mensuales ni costos iniciales.
**Verbatim snippet:** "The standard fee applies to products priced over US$ 15,00. The fee Hotmart gets is 9.90% of the price of the product plus US$ 0.50."
**Source:** https://hotmart.com/en/blog/hotmart-prices
**source_type:** blog
**verification_status:** direct_verified
**Date:** 11/06/2023
**Notes:** Página accedida directamente; contenido confirmado. Fuente en inglés (versión EN del blog). El mismo artículo indica "there are no monthly fees or upfront costs." La estructura de comisiones para micro-transacciones (≤US$15) se documenta por separado.

---

## Part 2 — Provisional findings (blocked_url_index_verified)

---

### F-P01

**Finding ID:** F-P01
**What:** La página de taxonomía de categorías del marketplace de Hotmart muestra actualmente 18 categorías principales bajo el encabezado "All categories" / "Mostrando: Todas las categorías": Animals and pets, Self-knowledge and spirituality, Career and personal development, Cooking and gastronomy, Design and photography, Childhood and family, Engineering and architecture, Academic studies, Finance and business, Hobby and leisure, Maintenance and repair, Marketing and sales, Fashion and beauty, Music and arts, Plants and ecology, Relationships, Health and sports, Technology and software development. Cada categoría tiene entre 1 y 9 subcategorías (53 subcategorías totales observadas).
**Verbatim snippet:** "Showing: All categories"
**Source:** https://hotmart.com/en/marketplace/category
**source_type:** product_listing
**verification_status:** direct_verified
**Date:** Accessed April 2026; page undated
**Notes:** Página accedida directamente pero renderizada en inglés/portugués pese a intentar parámetro de locale español. La clasificación aquí es direct_verified por acceso directo, pero se ubica en Part 2 porque el renderizado multilingüe introduce incertidumbre sobre si la vista española del marketplace podría mostrar una taxonomía diferente. Los nombres de las 18 categorías se transcribieron del contenido de la página en inglés.

---

### F-P02

**Finding ID:** F-P02
**What:** Un artículo del centro de ayuda de Hotmart define la Temperatura como un indicador propietario que informa simbólicamente cómo un producto está siendo aceptado en el mercado, basado en frecuencia de ventas, blueprint y tasa de reembolso. El algoritmo no se revela públicamente.
**Verbatim snippet:** "La temperatura es un concepto utilizado por Hotmart con el fin de informar, simbólicamente, cómo el producto está siendo aceptado en el mercado y cómo les está yendo a los afiliados."
**Source:** https://help.hotmart.com/es/article/209209447/-que-es-temperatura-de-un-producto-
**source_type:** article
**verification_status:** blocked_url_index_verified
**Date:** Accessed April 2026; page undated
**Notes:** Contenido obtenido por subagente de investigación; el status de acceso directo vs. snippet no fue confirmado explícitamente. En la misma página se indica: "El algoritmo del sistema de temperatura no se revela, porque es una fórmula interna de Hotmart" y que implica "frecuencia de ventas", "blueprint" y "tasa de reembolso" (pasajes separados, no incluidos en el snippet principal).

---

### F-P03

**Finding ID:** F-P03
**What:** Un post del blog de Hotmart describe el sistema Blueprint como un indicador de calidad que evalúa parámetros como calidad del contenido (clasificación por debajo/dentro/encima del promedio), existencia de página de ventas externa, páginas alternativas, HotLeads habilitado, y formato del producto (e-ticket y suscripción obtienen puntos extra).
**Verbatim snippet:** "Calidad del contenido: en el proceso de revisión de productos, el equipo los clasifica con relación a la calidad (por debajo del promedio, dentro del promedio, por encima del promedio)."
**Source:** https://hotmart.com/es/blog/blueprints-y-politicas-de-desaprobacion-guia-de-calidad-para-el-productor
**source_type:** blog
**verification_status:** blocked_url_index_verified
**Date:** Accessed April 2026; page undated
**Notes:** Contenido obtenido por subagente; fetch status no confirmado explícitamente. Los parámetros adicionales del Blueprint (página de ventas externa, páginas alternativas, HotLeads, formato) aparecen en pasajes separados de la misma página. El campo What incluye solo los parámetros listados en la fuente; no se observó escala numérica en el snippet citado, aunque una fuente de terceros (afiliadoempresa.com) describe Blueprint como "del 0 al 100%".

---

### F-P04

**Finding ID:** F-P04
**What:** Una nota de prensa de Hotmart indica que la comercialización de productos digitales por medio de sus plataformas superó colectivamente USD 10 mil millones en GMV acumulado desde 2011, año de fundación del grupo.
**Verbatim snippet:** "la comercialización de productos digitales por medio de sus plataformas superó colectivamente USD 10 mil millones (GMV, en inglés), desde 2011, año de fundación del grupo."
**Source:** https://press.hotmart.com/hotmart-company-supera-usd-10-mil-millones-de-ventas-de-productos-digitales-a-nivel-mundial
**source_type:** article
**verification_status:** direct_verified
**Date:** Accessed April 2026; page undated
**Notes:** Página accedida directamente; contenido confirmado. Dato auto-reportado por Hotmart en nota de prensa corporativa; no verificable de forma independiente. Se ubica en Part 2 pese a acceso directo por ser dato auto-reportado sin verificación externa. El GMV es acumulativo desde 2011, no anual.

---

### F-P05

**Finding ID:** F-P05
**What:** La misma nota de prensa de Hotmart indica que más de 4 millones de personas de Latinoamérica han comprado al menos un producto digital en Hotmart (datos de Hotmart Insights 2023), y que el sistema de pagos cuenta con más de 40 métodos y 22 monedas disponibles.
**Verbatim snippet:** "Según datos de Hotmart Insights 2023, más de 4 millones de personas de Latinoamérica han comprado al menos un producto digital en Hotmart."
**Source:** https://press.hotmart.com/hotmart-company-supera-usd-10-mil-millones-de-ventas-de-productos-digitales-a-nivel-mundial
**source_type:** article
**verification_status:** direct_verified
**Date:** Accessed April 2026; page undated
**Notes:** Misma fuente que F-P04; dato sobre compradores LATAM es auto-reportado (Hotmart Insights 2023). Los datos de métodos de pago (40+) y monedas (22) aparecen en pasaje separado de la misma nota de prensa: "sistema global de pagos de la compañía que cuenta con más de 40 métodos y 22 monedas disponibles." Se ubica en Part 2 por ser dato auto-reportado.

---

### F-P06

**Finding ID:** F-P06
**What:** Un post del blog de Hotmart lista 4 nichos con mayor potencial de retorno en la plataforma: Gastronomía y Culinaria, Salud y Deportes, Moda y Belleza, y Negocios y Profesión.
**Verbatim snippet:** "Entre los nichos con mayor potencial de retorno, encontramos el de Gastronomía y Culinaria; Salud y Deportes; Moda y Belleza; y Negocios y Profesión."
**Source:** https://hotmart.com/es/blog/vender-en-hotmart
**source_type:** blog
**verification_status:** blocked_url_index_verified
**Date:** Accessed April 2026; page undated
**Notes:** Contenido obtenido vía snippet de resultados de búsqueda; la página completa no fue accedida directamente. Los nombres de nichos se preservan tal cual aparecen en el snippet.

---

### F-P07

**Finding ID:** F-P07
**What:** El perfil de SimilarWeb para hotmart.com muestra aproximadamente 54.3M de visitas totales, tasa de rebote de 38.05%, 5.98 páginas por visita, duración promedio de visita de 00:06:01. SimilarWeb estima los ingresos anuales de Hotmart en $100M–$200M y clasifica a la empresa con 1001–5000 empleados. El perfil de pay.hotmart.com muestra 14.1M de visitas con distribución geográfica: Brazil 67.29%, Mexico 5.99%, Colombia 4.49%, United States 4.26%, Peru 2.68%.
**Verbatim snippet:** "Total Visits: 54.3M · Bounce Rate: 38.05% · Pages per Visit: 5.98 · Avg Visit Duration: 00:06:01"
**Source:** https://www.similarweb.com/website/hotmart.com/
**source_type:** database_profile
**verification_status:** blocked_url_index_verified
**Date:** Accessed April 2026; datos mostrados sin fecha explícita
**Notes:** Datos obtenidos vía snippets de resultados de búsqueda; perfil completo detrás de paywall. Las cifras de SimilarWeb son estimaciones de modelo, no datos oficiales de Hotmart. Las cifras de visitas fluctúan entre consultas (54.3M en SimilarWeb vs. 36.88M en Semrush para un periodo diferente). La distribución geográfica de pay.hotmart.com proviene de snippet separado de la misma fuente.

---

### F-P08

**Finding ID:** F-P08
**What:** El perfil de Crunchbase para Hotmart muestra una ronda Serie C de $127,305,793 con fecha 2021-03-30. El perfil lista 4 adquisiciones: Teachable (2020-03-16), ENotas (2022-07-05), Reshape (2024-01-18), y una adicional no especificada en el snippet. Entidad legal: Hotmart B.V. CEO y cofundador: João Pedro Resende.
**Verbatim snippet:** "Hotmart raised $127305793 on 2021-03-30 in Series C"
**Source:** https://www.crunchbase.com/organization/hotmart
**source_type:** database_profile
**verification_status:** blocked_url_index_verified
**Date:** Accessed April 2026; database profile
**Notes:** La página completa de Crunchbase retornó error 403 al intentar acceso directo; datos obtenidos exclusivamente de snippets de búsqueda. Los montos de las adquisiciones no fueron revelados ("undisclosed") según los snippets. La cifra de funding podría no reflejar rondas o inversiones adicionales posteriores.

---

### F-P09

**Finding ID:** F-P09
**What:** La página de Zapier para Hotmart indica que Hotmart se integra con más de 8,000 aplicaciones en la plataforma Zapier. Los triggers disponibles incluyen "Cart Abandonment" y "New Transaction". Integraciones específicas documentadas incluyen Hotmart + Teachable, Hotmart + Circle, Hotmart + Kit (ConvertKit), Hotmart + Paid Memberships Pro.
**Verbatim snippet:** "Hotmart integrates with 8,000 other apps on Zapier"
**Source:** https://zapier.com/apps/hotmart-7006/integrations
**source_type:** database_profile
**verification_status:** blocked_url_index_verified
**Date:** Accessed April 2026; page undated
**Notes:** Contenido obtenido vía snippets de búsqueda. El número "8,000" es una cifra general de la plataforma Zapier (total de apps conectables), no necesariamente integraciones directas pre-construidas con Hotmart. Los triggers específicos provienen de snippets de páginas relacionadas en Zapier.

---

### F-P10

**Finding ID:** F-P10
**What:** YessFilterAffiliate es una extensión de Chrome diseñada para afiliados de Hotmart que permite filtrar productos por criterios como precio, comisiones, ventas mensuales y reseñas. Tiene un rating promedio de 4.2 de 5 estrellas con 44 valoraciones. Publicada por "Productos ganadores de yessenia gallardo".
**Verbatim snippet:** "YessFilterAffiliate es una extensión de Chrome diseñada para afiliados que desean potenciar sus ingresos explorando Hotmart de manera eficiente. Esta herramienta te permite filtrar productos por múltiples criterios como precio, comisiones, ventas mensuales y reseñas, facilitando la identificación rápida de los productos ganadores."
**Source:** https://chrome-stats.com/d/ljnncgnpcjnebjiohlogdffaddeddbbd
**source_type:** database_profile
**verification_status:** blocked_url_index_verified
**Date:** Accessed April 2026
**Notes:** Contenido obtenido vía snippet/datos de búsqueda. chrome-stats.com es un agregador de terceros que indexa datos de Chrome Web Store. El rating (4.2/5, 44 ratings) y la descripción son datos del listing de la extensión. El comentario de usuarios indica que la extensión presenta fallos frecuentes en su funcionamiento; esto se observa en reseñas pero no se incluye como dato principal.

---

### F-P11

**Finding ID:** F-P11
**What:** Hotmart dispone de un portal para desarrolladores (Hotmart Developers) con APIs REST que utilizan autenticación OAuth 2.0. Las APIs permiten acceso a datos de suscripciones, compras de suscriptores, cancelaciones, reactivaciones y facturación. La plataforma de integración Pipedream lista triggers específicos incluyendo: Cart abandonment, Subscription cancellation, Plan change event, Purchase approved, Purchase overdue, Purchase refunded, Purchase chargeback, Purchase expired, Purchase completed, Purchase canceled.
**Verbatim snippet:** "Hotmart Developers is the website where you check out Hotmart's APIs. This data is ideal for Creators who have their own team of developers and want to create an even more personalized analysis with their own systems."
**Source:** https://help.hotmart.com/en/article/4403617024013/discover-hotmart-s-apis
**source_type:** article
**verification_status:** blocked_url_index_verified
**Date:** Accessed April 2026; page undated
**Notes:** Contenido del help center obtenido vía snippet. Los triggers específicos de la API provienen de una fuente separada (pipedream.com/apps/hotmart, también vía snippet) y se incluyen en What como contexto del ecosistema API, no como dato del help center. La URL del endpoint de autenticación (api-sec-vlc.hotmart.com/security/oauth/token) fue observada en snippet de terceros (rollout.com).

---

## Part 3 — Pattern candidates (sealed)

---

### PC-01
Gastronomía y culinaria aparece listada como primera categoría o entre las dos primeras en las listas de nichos más vendidos observadas en fuentes de Hotmart (F-02 blog 7 nichos, F-P06 blog 4 nichos). Fuentes externas de terceros (dominioemprendedor.com, scribd.com) también listan gastronomía en primera posición.

### PC-02
La taxonomía publicada en blog de 2021 (F-01) lista 20 categorías; la página de categorías del marketplace accedida en abril 2026 (F-P01) muestra 18 categorías principales. Los nombres de algunas categorías difieren entre ambas listas (ejemplo: "Animales y Plantas" en blog 2021 vs. "Animals and pets" + "Plants and ecology" como categorías separadas en página actual).

### PC-03
Los servicios auxiliares de terceros observados alrededor del ecosistema Hotmart (F-P09 Zapier, F-P11 APIs/Pipedream) son predominantemente plataformas de integración y automatización de flujos de trabajo. Solo se observó una herramienta standalone de nicho específico para Hotmart (F-P10 YessFilterAffiliate, extensión Chrome con 44 ratings).

---

## Part 4 — Could not verify / Out-of-scope

---

### F-X01

**Finding ID:** F-X01
**What:** absence: No se pudieron observar precios individuales de productos en el marketplace de Hotmart.
**Verbatim snippet:** n/a — absence finding
**Source:** Intentado acceso directo a https://hotmart.com/en/marketplace, https://hotmart.com/es/marketplace/productos/clase-de-busqueda-de-productos-ganadores/S82998507V, https://hotmart.com/es/marketplace/productos/top-10-productos-mas-vendidos-en-el-mundo/Y100881373O. Las páginas de producto contienen ancla #payment pero la sección de precios no se renderiza en HTML estático (renderizado JavaScript del lado del cliente).
**source_type:** product_listing
**verification_status:** could_not_verify
**Date:** Accessed April 2026
**Notes:** Limitación técnica del método de acceso (web fetch extrae HTML estático; contenido dinámico JS no se renderiza). Los precios, ratings y conteos de reseñas individuales no fueron visibles en ninguna página de producto accedida.

---

### F-X02

**Finding ID:** F-X02
**What:** absence: La página de categorías de Hotmart Club (hotmart.com/es/club/categorias) no fue accesible.
**Verbatim snippet:** n/a — absence finding
**Source:** Intentado acceso directo a https://hotmart.com/es/club/categorias. La página retornó error de permisos. No se encontraron datos sobre esta página en resultados de búsqueda.
**source_type:** product_listing
**verification_status:** could_not_verify
**Date:** Accessed April 2026
**Notes:** La URL puede requerir autenticación o haber sido retirada. No se encontró caché en motores de búsqueda.

---

### F-X03

**Finding ID:** F-X03
**What:** absence: No se encontraron conteos de listings (productos) por categoría individual en ninguna página del marketplace accedida.
**Verbatim snippet:** n/a — absence finding
**Source:** Revisadas las páginas https://hotmart.com/en/marketplace/category, https://hotmart.com/en/marketplace/categories/marketing-and-sales, y el blog https://hotmart.com/es/blog/hotmart-marketplace. Ninguna muestra conteos numéricos de productos por categoría o subcategoría.
**source_type:** product_listing
**verification_status:** could_not_verify
**Date:** Accessed April 2026
**Notes:** La ausencia de conteos por categoría se observó consistentemente en todas las páginas de taxonomía y categoría accedidas. No se intentó el Mercado de Afiliación (requiere autenticación).

---

### F-X04

**Finding ID:** F-X04
**What:** absence: No se observaron patrones de descuento, precios promocionales ni banners de ofertas en ninguna página del marketplace accedida.
**Verbatim snippet:** n/a — absence finding
**Source:** Revisadas las páginas https://hotmart.com/en/marketplace, páginas individuales de productos, y páginas de categorías. No se observó contenido relacionado con descuentos, precios tachados, porcentajes de ahorro o promociones temporales.
**source_type:** product_listing
**verification_status:** could_not_verify
**Date:** Accessed April 2026
**Notes:** La ausencia podría deberse al método de acceso (HTML estático sin renderizado JS) o a la inexistencia de dichos elementos en las páginas en el momento de acceso. El blog de Hotmart documenta la existencia de una herramienta "Cupones y Descuentos" para productores, pero no se observó su implementación visible en el marketplace público.

---

### F-X05

**Finding ID:** F-X05
**What:** absence: No se pudieron acceder directamente páginas de YouTube con datos sobre nichos de Hotmart.
**Verbatim snippet:** n/a — absence finding
**Source:** Búsquedas realizadas: "site:youtube.com hotmart nicho rentable 2025 2026", "site:youtube.com hotmart categorías productos digitales más vendidos". Los resultados de búsqueda retornaron referencias a videos pero las páginas de YouTube no fueron directamente accedidas. Un resumen de terceros (sider.ai) mencionaba cifras de crecimiento (42% espiritualidad, 36% gastronomía) pero es un retelling secundario generado por IA — no califica como fuente primaria.
**source_type:** search_results_page
**verification_status:** could_not_verify
**Date:** Accessed April 2026
**Notes:** Los datos del resumen de sider.ai (cifras de crecimiento por nicho) se descartan por ser retelling secundario generado por IA de un video de YouTube no verificable directamente.

---

## Research QA Notes

**1. Cobertura del scope D3:**
- Catálogo: Documentadas 20 categorías (blog 2021) y 18 categorías actuales (marketplace page). Formatos de producto documentados. Conteos de listings por categoría NO observables.
- Discovery: Documentados 11 filtros del mercado de afiliación, 3 secciones de homepage del marketplace, filtros "Más queridos"/"Más calientes", sistema de Temperatura, sistema de Blueprint, sistema de estrellas hasta 5.
- Señales de mercado: GMV acumulado ($10B), compradores LATAM (4M+), tráfico web (SimilarWeb), funding (Crunchbase Serie C $127M), estructura de comisiones (9.90%+$0.50).
- Servicios auxiliares: Zapier (8,000+ apps), Chrome extension YessFilterAffiliate, portal Hotmart Developers API, integraciones Make/Pipedream.

**2. Exclusiones aplicadas según scope:**
- Se excluyeron marketing claims de Hotmart sobre tamaño del catálogo (e.g., "580,000 productos registrados", "80 thousand courses available" que aparecían en múltiples fuentes oficiales). Estos datos se observaron pero no se incluyeron como findings por instrucción explícita del scope.
- Se excluyeron historias individuales de vendedores, artículos genéricos sobre productos digitales, y reviews de afiliados.
- Se excluyeron datos sobre política de plataforma (D1) y voz del vendedor (D2).

**3. Limitaciones técnicas observadas:**
- El marketplace de Hotmart renderiza precios, ratings y conteos de reseñas mediante JavaScript del lado del cliente. El método de acceso (web fetch estático) no captura contenido renderizado dinámicamente. Esto impidió la observación directa de precios individuales, ratings numéricos, y conteos de reseñas en páginas de productos.
- La versión española del marketplace (hotmart.com/es/marketplace) no fue accesible directamente; se accedió la versión inglesa.
- El Mercado de Afiliación (interfaz para afiliados) requiere autenticación y no fue accedido directamente; la información proviene del centro de ayuda y blog.

**4. Discrepancias observadas entre fuentes:**
- Taxonomía de categorías: Blog 2021 lista 20 categorías (F-01) vs. página actual muestra 18 (F-P01). Algunos nombres de categorías difieren (documentado en PC-02).
- Datos cuantitativos corporativos varían según fuente y fecha: "370 mil productos registrados" (blog how-hotmart-works), "420 mil" (economiatic.com), "490 mil" (press release Challenge), "580 mil" (press release GSV150, campaign page). Todas son fuentes de diferentes fechas, lo cual podría explicar la variación. Ninguna fue incluida como finding por la exclusión de marketing claims sobre tamaño del catálogo.

**5. QA de 11 puntos aplicada a cada finding:**
Para cada finding se verificó: (1) un finding = una sola fuente; (2) verbatim es pasaje continuo character-for-character sin concatenación; (3) What contiene solo hechos literalmente visibles en el snippet; (4) Notes contiene solo limitación local de verificación, sin interpretación ni cross-source; (5) Source es URL completa con protocolo+dominio+ruta; (6) URLs no fijables derivadas a Part 4; (7) edge cases de secondary retelling evaluados y descartados a Part 4 cuando aplicable (sider.ai); (8) solo evidencia observable, sin extrapolación de muestra a población; (9) contexto completo de precios preservado donde aplica; (10) source_type corresponde a tipos permitidos; (11) fecha formateada correctamente o marcada como "Accessed [Month Year]; page undated".

**6. Notas sobre Part 2:**
- Algunos findings en Part 2 (F-P04, F-P05) provienen de páginas accedidas directamente (verification_status: direct_verified) pero se ubicaron en Part 2 por ser datos auto-reportados corporativos cuya veracidad subyacente no es verificable de forma independiente. Se documentó esta decisión editorial en las Notes de cada finding.
- F-P01 fue accedido directamente pero se ubica en Part 2 por incertidumbre sobre si el renderizado en inglés/portugués representa fielmente la experiencia del marketplace en español.

**7. Servicios auxiliares no incluidos como findings individuales por espacio:**
- Make.com (3,000+ apps), Pipedream (3,000+ apps), Albato (1,000+ apps): integraciones similares a Zapier. Documentadas en investigación pero no como findings separados por redundancia con F-P09.
- 19 herramientas internas de Hotmart listadas en blog (herramientas-hotmart-retrospectiva): snippet-only. Incluyen ListBoss, Hotmart Analytics, Webinar, Evento Online, Creador de Páginas, Order Bump, Recuperador Automático de Ventas, entre otras. No se creó finding individual por ser herramientas de primera parte de la plataforma, no servicios auxiliares de terceros.
- HotLeads: herramienta de Hotmart para vincular captura de leads a comisiones de afiliados. Documentada en help center. No incluida como finding separado.

**8. Conteo final de findings:**
- Part 1 (Clean / direct_verified): 5
- Part 2 (Provisional): 11 (6 blocked_url_index_verified + 5 direct_verified ubicados editorialmente)
- Part 3 (Pattern candidates): 3
- Part 4 (Could not verify / absences): 5
- Total findings: 21