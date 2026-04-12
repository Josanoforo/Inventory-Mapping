# Kichink × D3 — Catálogo, descubrimiento y señales de mercado

---

## Descomposición de búsqueda

**SD-01:** Verificar accesibilidad directa del sitio kichink.com y sus páginas principales (/explorar, /categorias, /productos, /tiendas).  
**SD-02:** Documentar productos observables con precios en la plataforma Kichink.  
**SD-03:** Documentar mecanismos de búsqueda y descubrimiento disponibles en la plataforma.  
**SD-04:** Documentar categorías de productos existentes en la plataforma y en perfiles de bases de datos.  
**SD-05:** Identificar presencia de productos digitales en el catálogo de Kichink.  
**SD-06:** Buscar servicios auxiliares de terceros construidos alrededor de Kichink (herramientas SEO, generadores de plantillas, consultorías).  
**SD-07:** Buscar señales de mercado observables: estado operativo actual, perfiles en bases de datos, disponibilidad geográfica.  
**SD-08:** Documentar estructura de páginas de producto individual (opciones, formas de pago, campos disponibles).

---

## Part 1 — Hallazgos limpios (direct_verified)

**F-01**  
**What:** Blog de ecommerce caracteriza a Kichink como un marketplace comparable a Mercado Libre o Amazon a menor escala, no como una plataforma para crear tienda en línea propia.  
**Verbatim snippet:** "Kichink no es una verdadera plataforma para crear una tienda en línea. Se trata más bien de un marketplace tal como lo es Mercado Libre o Amazon pero a menor escala, desde aquí podemos adelantar que simplemente por eso no podría ser comparado con Woocommerce o Shopify, donde si puedes crear una verdadera tienda en línea."  
**Source:** https://markethax.com/kichink-opinion/  
**source_type:** blog  
**verification_status:** direct_verified  
**Date:** 01/06/2023 (fecha visible en la página)  
**Notes:** Página accedida directamente mediante web_fetch. Blog tiene carácter promocional (enlaza a cursos propios y alternativas como Shopify y WooCommerce). Podría clasificarse como affiliate review bajo criterio de exclusión del shard; se incluye como señal de mercado observable (caracterización competitiva de la plataforma por tercero). Dato representa la afirmación del autor del blog.

---

## Part 2 — Hallazgos provisionales (blocked_url_index_verified)

**F-P01**  
**What:** La página principal de Kichink muestra productos con precios de $220.00 MXN y $80.00 MXN, cada uno con nombre de producto, nombre de tienda vendedora, selectores de opciones y botón "Agregar al carrito".  
**Verbatim snippet:** "Ver más productos · Ramones Libreta Pasta Dura 1/2 carta por Ed Vill $220.00 MXN · Ramones Libreta Pasta Dura 1/2 carta · option 1 · option 2 · Cantidad · Agregar al carrito · papá Star Wars por El Regalito $80.00 MXN"  
**Source:** https://www.kichink.com/  
**source_type:** product_listing  
**verification_status:** blocked_url_index_verified  
**Date:** Accedido abril 2026; copyright del sitio @2025  
**Notes:** Acceso directo a www.kichink.com retorna HTTP 403 Forbidden. Snippet recuperado del índice de búsqueda de Google para la misma URL exacta (búsqueda "kichink tienda exitosa"). Contenido de la página es JS-rendered; los productos visibles en el snippet del índice no representan la totalidad del catálogo. Los precios no muestran descuentos ni precios originales tachados.

**F-P02**  
**What:** La página principal de Kichink muestra productos adicionales con precios de $500.00 MXN, $1,200.00 MXN, $60.00 MXN, $529.00 MXN y $820.00 MXN, de tiendas como The Wizard Shop, Lacayo Pez, sinolorperruno.com.mx, TEQUILA ORENDAIN y Serpentina Shop.  
**Verbatim snippet:** "YO CREO MI REALIDAD. por The Wizard Shop $500.00 MXN · YO CREO MI REALIDAD. option 1 · option 2 · Cantidad · Agregar al carrito · Falda Orion por Lacayo Pez $1200.00 MXN · Falda Orion · option 1 · option 2 · Cantidad · Agregar al carrito · Jabón Menta & Romero Aceite Coco Orgánico por sinolorperruno.com.mx $60.00 MXN · Jabón Menta & Romero Aceite Coco Orgánico · option 1 · option 2 · Cantidad · Agregar al carrito · GRAN ORENDAIN BLANCO TEQUILA 100% AGAVE por TEQUILA ORENDAIN $529.00 MXN · GRAN ORENDAIN BLANCO TEQUILA 100% AGAVE · option 1 · option 2 · Cantidad · Agregar al carrito · Frutero por Serpentina Shop $820.00 MXN"  
**Source:** https://www.kichink.com/  
**source_type:** product_listing  
**verification_status:** blocked_url_index_verified  
**Date:** Accedido abril 2026; copyright del sitio @2025  
**Notes:** Acceso directo a www.kichink.com retorna HTTP 403 Forbidden. Snippet recuperado por subagente de investigación del índice de Google para la misma URL exacta; presentado como texto continuo del índice. Los precios observados no incluyen indicación de descuento o precio original.

**F-P03**  
**What:** La página de búsqueda de Kichink (/search/ropa) presenta filtros por Categorias, Sub categorias, Precio, Pais y Otros, con pestañas para resultados de PRODUCTOS, TIENDAS y COLECCIONES.  
**Verbatim snippet:** [Stated in layout: "Categorias · Sub categorias · Precio · Pais · Otros · Filtros · PRODUCTOS · TIENDAS · COLECCIONES · Done"]  
**Source:** https://www.kichink.com/search/ropa  
**source_type:** search_results_page  
**verification_status:** blocked_url_index_verified  
**Date:** Accedido abril 2026; copyright de la página @2024  
**Notes:** Acceso directo a www.kichink.com/search/ropa retorna HTTP 403 Forbidden. Snippet recuperado del índice de Google para la misma URL exacta. Los filtros aparecen como elementos de UI en layout estructurado; no es observable si los filtros despliegan opciones funcionales con contenido dinámico. Método de recuperación: búsqueda Google "kichink tienda exitosa".

**F-P04**  
**What:** La página /productos de Kichink presenta navegación por categorías con opción "Navegar por tienda" y controles de paginación para mostrar 24, 36 o 48 resultados. Muestra texto "Cargando productos" sin productos individuales visibles en el índice.  
**Verbatim snippet:** [Stated in layout: "Categorías · Encuentra el producto perfecto para ti · Navegar por tienda · Sin Filtros · Cargando productos · Navegar por tienda · Mostrar: 24 · 36 · 48"]  
**Source:** https://www.kichink.com/productos  
**source_type:** search_results_page  
**verification_status:** blocked_url_index_verified  
**Date:** Accedido abril 2026; copyright de la página @2024  
**Notes:** Acceso directo a esta URL específica no se intentó, pero 7 URLs probadas en kichink.com retornan HTTP 403 Forbidden. Snippet del índice de Google para la misma URL. El texto "Cargando productos" indica contenido JS-rendered no capturado en el indexado estático. Los nombres de categorías específicas no son visibles.

**F-P05**  
**What:** La página /colecciones de Kichink describe sus colecciones como curadas y ofrece navegación por producto y por colección, con opción de filtrar sólo productos disponibles. Muestra textos "Cargando artículos...", "Cargando tiendas..." y "Cargando colecciones..." sin contenido cargado.  
**Verbatim snippet:** "Una Colección por Kichink · Mostrar sólo productos disponibles · Cargando artículos... Navegar por producto · Navegar por coleccion · Cargando tiendas... Cargando colecciones... Regresar a colecciones"  
**Source:** https://www.kichink.com/colecciones/4819  
**source_type:** search_results_page  
**verification_status:** blocked_url_index_verified  
**Date:** Accedido abril 2026; página sin fecha visible  
**Notes:** Acceso directo a esta URL específica no se intentó, pero 7 URLs probadas en kichink.com retornan HTTP 403. Snippet del índice de Google para la misma URL. Los textos "Cargando..." indican contenido JS-rendered no cargado en el indexado.

**F-P06**  
**What:** Tienda "ORIGINAL MX" en Kichink se describe como tienda de suministros para manualidades, empresa 100% mexicana, que ofrece "productos digitales para descarga y fisicos".  
**Verbatim snippet:** "Original es una tienda de suministros para manualidades, de marca propia como de otras marcas, empresa 100% mexicana que nace bajo la necesidad de brindar alternativas de desarrollo a procesos creativos con calidad. Aqui en encontraras productos digitales para descarga y fisicos."  
**Source:** https://www.kichink.com/stores/original-1/category/312954/tenis-1  
**source_type:** product_listing  
**verification_status:** blocked_url_index_verified  
**Date:** Accedido abril 2026; página sin fecha visible  
**Notes:** Acceso directo a esta URL específica no se intentó, pero 7 URLs probadas en kichink.com retornan HTTP 403. Snippet del índice de Google para la misma URL. La descripción es texto visible de la tienda en el snippet. La tienda explicita la coexistencia de productos digitales y físicos en su oferta.

**F-P07**  
**What:** Las páginas de producto individual en Kichink muestran campos de Categorías, Tamaño, Color, Cantidad, Disponibilidad, "Compra segura con Garantía Kichink" y formas de pago aceptadas: Tarjetas de Crédito, Débito, efectivo y Kash.  
**Verbatim snippet:** [Stated in layout: "Categorías · Todos · Tamaño · Color · Cantidad · Comprar · Disponibilidad · Compra segura con Garantía Kichink · FORMAS DE PAGO · Tarjetas de Crédito, Débito, efectivo y Kash. Compartir en"]  
**Source:** https://www.kichink.com/buy/213967/caleidoscopio/imagen-digital  
**source_type:** product_listing  
**verification_status:** blocked_url_index_verified  
**Date:** Accedido abril 2026; página sin fecha visible  
**Notes:** Acceso directo a esta URL específica no se intentó, pero 7 URLs probadas en kichink.com retornan HTTP 403. Snippet del índice de Google para la misma URL. "Kash" es un sistema de prepago propio de Kichink. La estructura de campos se observa idéntica en múltiples páginas de producto indexadas en Google (ej. /buy/994311/, /buy/912794/, /buy/1541421/, /buy/1327779/).

**F-P08**  
**What:** Perfil de Tracxn describe a Kichink como marketplace abierto con categorías: fashion, health, beauty, food and drinks, home, pets; comisión de 7.5% por transacción a vendedores.  
**Verbatim snippet:** "Kichink is an online marketplace offering products across categories such as fashion, health, beauty, food and drinks, home, pets etc. It is an open marketplace allowing sellers to open their storefront for free. It charges a commission of 7.5% on the transaction from the sellers."  
**Source:** https://tracxn.com/d/companies/kichink/__55XJaGryqsaDerfyeMYva7TNaVBopJLuDHPrshUsUGc  
**source_type:** database_profile  
**verification_status:** blocked_url_index_verified  
**Date:** Accedido abril 2026; perfil titulado "2025 Company Profile"  
**Notes:** Acceso directo a tracxn.com bloqueado por robots.txt. Snippet del índice de Google para la misma URL exacta. Las categorías listadas son la caracterización de Tracxn, no necesariamente los nombres de categoría tal como aparecen en la interfaz de usuario de Kichink. La comisión de 7.5% es dato del perfil de Tracxn.

**F-P09**  
**What:** La página principal de Kichink presenta un selector de país con opciones "KICHINK México" y "KICHINK United States".  
**Verbatim snippet:** [Stated in layout: "Por favor seleccione un país · KICHINK México · KICHINK United States"]  
**Source:** https://www.kichink.com/  
**source_type:** product_listing  
**verification_status:** blocked_url_index_verified  
**Date:** Accedido abril 2026; copyright @2025  
**Notes:** Acceso directo a www.kichink.com retorna HTTP 403 Forbidden. Snippet del índice de Google para la misma URL. El selector de país aparece como elemento de UI en la parte superior de la página.

**F-P10**  
**What:** La página principal de Kichink muestra sección "Ver más tiendas" con tiendas destacadas: zona organikum ("Ser sano sí es una opción"), Conejo en la Luna ("Productos sanos y artesanales"), juanfutbol ("DESDE EUROPA, UNA INCREÍBLE COLECCIÓN") y STEVIA SUPER LIFE® ("ENDULZANTES NATURALES").  
**Verbatim snippet:** "Ver más tiendas · zona organikum · Ser sano sí es una opción · Conejo en la Luna · Productos sanos y artesanales · juanfutbol · DESDE EUROPA, UNA INCREÍBLE COLECCIÓN · STEVIA SUPER LIFE® · ENDULZANTES NATURALES"  
**Source:** https://www.kichink.com/  
**source_type:** product_listing  
**verification_status:** blocked_url_index_verified  
**Date:** Accedido abril 2026; copyright @2025  
**Notes:** Acceso directo a www.kichink.com retorna HTTP 403 Forbidden. Snippet del índice de Google para la misma URL. Las frases entre comillas bajo cada tienda son eslóganes o descripciones cortas de la tienda. Las tiendas visibles incluyen categorías de productos orgánicos/saludables, deportes, y endulzantes naturales — estas categorías son inferidas de los eslóganes, no de la clasificación formal de la plataforma.

---

## Part 3 — Candidatos de patrón (sealed)

**PC-01**  
**Candidate statement:** Múltiples páginas de catálogo de Kichink presentan textos de estado "Cargando" (productos, tiendas, artículos, colecciones) en el índice de Google, sin productos ni tiendas individuales visibles en dichas páginas de navegación.  
**Related Finding IDs:** F-P04, F-P05  
**Status:** sealed; not validated.

**PC-02**  
**Candidate statement:** El catálogo de Kichink incluye tanto productos físicos (con opciones de Tamaño y Color) como productos digitales para descarga, según lo observable en descripciones de tiendas y la estructura de páginas de producto.  
**Related Finding IDs:** F-P06, F-P07  
**Status:** sealed; not validated.

**PC-03**  
**Candidate statement:** Los precios observados en la página principal de Kichink abarcan desde $60.00 MXN hasta $1,200.00 MXN, distribuidos entre 7 productos de distintas tiendas vendedoras.  
**Related Finding IDs:** F-P01, F-P02  
**Status:** sealed; not validated.

---

## Part 4 — No se pudo verificar / Fuera de alcance

**F-X01: Número total de productos activos en el catálogo**  
**What:** No se encontraron datos sobre el número total de productos activos actualmente en el catálogo de Kichink.  
**Verbatim snippet:** n/a — absence finding  
**Source:** www.kichink.com (HTTP 403), www.kichink.com/productos (índice Google, muestra "Cargando productos"), búsqueda Google "kichink catálogo", búsqueda Google "site:kichink.com categorias"  
**source_type:** unknown  
**verification_status:** could_not_verify  
**Date:** Abril 2026  
**Notes:** Buscado en las ubicaciones listadas en Source. Las páginas de catálogo retornan HTTP 403 en acceso directo. En el índice de Google muestran "Cargando productos" sin conteos observables.

**F-X02: Nombres específicos de categorías de productos en la plataforma**  
**What:** No se pudieron verificar los nombres específicos de las categorías de productos tal como aparecen en la interfaz de usuario de Kichink.  
**Verbatim snippet:** n/a — absence finding  
**Source:** www.kichink.com/productos (índice Google), www.kichink.com/productos/categoria/3 (índice Google), www.kichink.com/search/ropa (índice Google, muestra "Categorias" como filtro sin listar opciones)  
**source_type:** unknown  
**verification_status:** could_not_verify  
**Date:** Abril 2026  
**Notes:** Buscado en las ubicaciones listadas en Source. El filtro "Categorias" existe en la interfaz de búsqueda (F-P03) pero las opciones que despliega no son visibles en el snippet del índice.

**F-X03: Patrones de descuento observables**  
**What:** No se encontraron datos sobre patrones de descuento (precio original tachado vs. precio de oferta) en productos de Kichink.  
**Verbatim snippet:** n/a — absence finding  
**Source:** www.kichink.com (índice Google), búsqueda Google "kichink productos digitales", búsqueda Google "kichink precios productos"  
**source_type:** unknown  
**verification_status:** could_not_verify  
**Date:** Abril 2026  
**Notes:** Buscado en las ubicaciones listadas en Source. Los precios observados en F-P01 y F-P02 aparecen como precios únicos sin indicación de descuento.

**F-X04: Servicios auxiliares de terceros construidos alrededor de Kichink**  
**What:** No se encontraron servicios auxiliares de terceros (herramientas SEO, generadores de plantillas, consultorías, optimizadores de listados) construidos específicamente alrededor de Kichink.  
**Verbatim snippet:** n/a — absence finding  
**Source:** Búsqueda Google "kichink herramientas consultoría optimización tienda", búsqueda Google "kichink SEO plantillas", búsqueda Google "kichink optimización ventas"  
**source_type:** unknown  
**verification_status:** could_not_verify  
**Date:** Abril 2026  
**Notes:** Buscado en las ubicaciones listadas en Source. Las búsquedas retornaron comparativas de plataformas (Kichink vs. Shopify), perfiles de empresa y artículos genéricos de ecommerce, pero ningún servicio auxiliar de terceros construido específicamente para Kichink.

**F-X05: Conteo de reseñas por producto**  
**What:** No se encontraron datos sobre conteos de reseñas en productos individuales de Kichink.  
**Verbatim snippet:** n/a — absence finding  
**Source:** www.kichink.com/buy/213967/ (índice Google), www.kichink.com/buy/994311/ (índice Google), www.kichink.com/buy/1541421/ (índice Google), búsqueda Google "site:kichink.com categorias"  
**source_type:** unknown  
**verification_status:** could_not_verify  
**Date:** Abril 2026  
**Notes:** Buscado en las ubicaciones listadas en Source. Las páginas de producto indexadas muestran campos de Categorías, Tamaño, Color, Cantidad, Disponibilidad y Formas de pago, pero no contienen campos de reseñas ni calificaciones visibles en los snippets.

---

## Research QA Notes

1. **Bloqueo de dominio completo:** Todas las URLs probadas en kichink.com (7 URLs: /, /explorar, /categorias, /search/ropa, /stores/libros-digitales-1, /crea-tu-tienda, kichink.com sin www) retornan HTTP 403 Forbidden. El servidor está activo pero bloquea acceso público. Esto forzó todos los hallazgos de kichink.com a Parte 2 (blocked_url_index_verified) con recuperación vía índice de Google.

2. **Container limitation — JS rendering:** Las páginas de catálogo de Kichink (/productos, /tiendas, /colecciones, /search/) son JS-rendered. Los snippets del índice de Google capturan la estructura de UI (botones, filtros, texto estático) pero no el contenido dinámico (listas de productos, nombres de categorías, conteos de resultados). Esto impide documentar el catálogo completo.

3. **Findings forzados a Provisional:** F-P01 a F-P10 forzados a blocked_url_index_verified por bloqueo HTTP 403 del dominio kichink.com. F-P08 (Tracxn) forzado a provisional por bloqueo de robots.txt en tracxn.com.

4. **URLs no probadas individualmente:** F-P04 (/productos), F-P05 (/colecciones/4819), F-P06 (/stores/original-1/...), F-P07 (/buy/213967/...) no fueron intentadas en acceso directo individualmente, pero se incluyen como blocked_url_index_verified basándose en la evidencia de bloqueo generalizado del dominio (7/7 URLs probadas retornaron 403). Limitación documentada en Notes de cada hallazgo.

5. **Subagente intermediación en F-P02:** El snippet de precios adicionales ($500, $1200, $60, $529, $820 MXN) fue recuperado por un subagente de investigación del índice de Google para la misma URL (www.kichink.com). El subagente presentó el texto como continuo. El texto no fue independientemente verificado en una búsqueda propia separada.

6. **URLs del shard no existentes:** Las URLs /explorar y /categorias especificadas en la instrucción del shard no existen como páginas independientes en el índice de Google de kichink.com. Las funciones equivalentes de exploración se encuentran en /productos, /tiendas, /colecciones y /search/[término].

7. **source_type ambiguity:** F-P09 y F-P10 clasificados como product_listing (elementos de la homepage que funciona como escaparate); la homepage podría también clasificarse como search_results_page.

8. **F-01 borderline affiliate review:** El hallazgo F-01 proviene de markethax.com, blog con carácter promocional que enlaza a cursos y herramientas propias. Bajo el criterio de exclusión "affiliate reviews" del shard, este hallazgo podría ser excluido. Se incluyó con nota explícita por contener una caracterización observable del posicionamiento competitivo de la plataforma, no una recomendación de compra.

9. **Coverage gaps principales:** No se pudo documentar: (a) número total de productos o tiendas activas, (b) nombres de categorías tal como aparecen en la interfaz, (c) distribución de productos por categoría, (d) patrones de descuento, (e) conteo de reseñas, (f) servicios auxiliares de terceros. Los precios observados se limitan a 7 productos visibles en la página principal vía índice de Google.

10. **Copyright dates:** La homepage muestra @2025 Kichink Servicios S.A. de C.V. La página /search/ropa muestra @2024. La página /productos muestra @2024. Estos son datos observados, no fechas de última actualización de contenido.