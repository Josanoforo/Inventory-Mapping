# DATA GATHERING — Shard: Kichink × D1 — Platform mechanics and fee structure

---

## 1. Search Decomposition

| ID | Sub-búsqueda | Tipo esperado |
|---|---|---|
| SD-01 | ¿Qué comisión por transacción cobra Kichink a vendedores? | pricing_page, policy_page |
| SD-02 | ¿Existe costo fijo (apertura, mensualidad, anualidad) para abrir tienda en Kichink? | pricing_page |
| SD-03 | ¿Cuál es el plazo de pago/liquidación a vendedores tras solicitud de depósito? | pricing_page, policy_page |
| SD-04 | ¿Cuál es el monto mínimo de venta acumulado para solicitar liquidación? | policy_page |
| SD-05 | ¿Qué cargo aplica si se solicita pago por debajo del mínimo? | policy_page |
| SD-06 | ¿Qué métodos de pago acepta Kichink de compradores? | pricing_page, policy_page |
| SD-07 | ¿Cuáles son las tarifas de envío nacional e internacional de Kichink? | pricing_page |
| SD-08 | ¿Cuánto cuesta la forma de pago "pago en puerta"? | policy_page |
| SD-09 | ¿Qué comisión cobra la cadena de conveniencia al comprador por pago en efectivo? | pricing_page |
| SD-10 | ¿Existe límite de monto para pagos con tarjeta de crédito/débito vía Agregador (BIP)? | policy_page |
| SD-11 | ¿Cuáles son los tiempos de procesamiento de reembolsos? | policy_page |
| SD-12 | ¿Cuál es la política de contracargos de Kichink? | policy_page |
| SD-13 | ¿Puede Kichink modificar comisiones y bajo qué mecanismo? | policy_page |
| SD-14 | ¿Cómo se factura la comisión de Kichink? | policy_page |
| SD-15 | ¿Qué es la "cuota de administración de prevención de fraudes"? | policy_page |
| SD-16 | ¿Retiene Kichink ventas de eventos/servicios/productos digitales de forma distinta? | policy_page |
| SD-17 | ¿Existe sistema de tiers/calificación de vendedor que modifique la comisión? | pricing_page |
| SD-18 | ¿Qué contiene la sección "Precios &amp; Planes" del menú de navegación de kichink.com? | pricing_page |

---

## 2. Part 1 — Clean findings (direct_verified)

**No valid clean findings captured.**

Justificación: Todas las URLs de kichink.com devolvieron HTTP 403 (Forbidden) en acceso directo. Ninguna página pudo ser leída en vivo por el agente. Todos los contenidos recuperados provienen del índice de búsqueda de Google sobre las mismas URLs exactas.

---

## 3. Part 2 — Provisional findings (blocked_url_index_verified)

---

### F-P01

**Finding ID:** F-P01
**What:** Kichink no cobra costo por abrir tienda. La comisión por transacción parte del 15%.
**Verbatim snippet:** "Abrir tu tienda NO TIENE COSTO. Kichink sólo cobra una comisión por transacción a partir del 15%."
**Source:** https://www.kichink.com/crea-tu-tienda
**source_type:** pricing_page
**verification_status:** blocked_url_index_verified
**Date:** Accessed April 2026; page undated
**Notes:** URL confirmada en índice de Google (título: "Crea Tu Tienda | Kichink"). Fetch directo devolvió 403. Snippet recuperado del índice de búsqueda de Google para la misma URL exacta. No se especifica moneda ni si el 15% incluye IVA.

---

### F-P02

**Finding ID:** F-P02
**What:** El pago a la tienda tras solicitar depósito se refleja en un plazo de 10 a 90 días naturales, descontando la comisión de Kichink.
**Verbatim snippet:** "Dentro de Kontrol podrás solicitar el depósito de las órdenes que se encuentren Entregadas. El pago se hace descontando la comisión que Kichink cobra por transacción y se verá reflejado en tu cuenta en un plazo de 10 a 90 días naturales."
**Source:** https://www.kichink.com/crea-tu-tienda
**source_type:** pricing_page
**verification_status:** blocked_url_index_verified
**Date:** Accessed April 2026; page undated
**Notes:** URL confirmada en índice de Google. Fetch directo devolvió 403. Snippet recuperado del índice de búsqueda de Google. El texto dice "días naturales" (no hábiles).

---

### F-P03

**Finding ID:** F-P03
**What:** Las tarifas de envío nacional comienzan en $79 pesos. Los envíos internacionales comienzan en $30 USD. Los costos varían por peso y destino.
**Verbatim snippet:** "Kichink tiene las tarifas más bajas del mercado, empezando en $79 pesos. También hacemos envíos internacionales, empezando en $30 USD. Los costos varían dependiendo del peso y el lugar al que se envían."
**Source:** https://www.kichink.com/crea-tu-tienda
**source_type:** pricing_page
**verification_status:** blocked_url_index_verified
**Date:** Accessed April 2026; page undated
**Notes:** URL confirmada en índice de Google. Fetch directo devolvió 403. "$79 pesos" implica MXN por contexto pero no se explicita "MXN". Estos son costos de envío al comprador, no comisiones al vendedor.

---

### F-P04

**Finding ID:** F-P04
**What:** La tienda recibe pagos con tarjeta de crédito, efectivo en tiendas de conveniencia, transferencia bancaria y tarjeta de prepago Kash.
**Verbatim snippet:** "Tu tienda recibe pagos con tarjeta de crédito, efectivo en tiendas de conveniencia, transferencia bancaria o con nuestra tarjeta de pre pago Kash."
**Source:** https://www.kichink.com/crea-tu-tienda
**source_type:** pricing_page
**verification_status:** blocked_url_index_verified
**Date:** Accessed April 2026; page undated
**Notes:** URL confirmada en índice de Google. Fetch directo devolvió 403. No especifica marcas de tarjeta ni disponibilidad geográfica.

---

### F-P05

**Finding ID:** F-P05
**What:** Para solicitar liquidación, la tienda debe acumular un mínimo de venta de $150.00 MN netos (después de descuentos y/o comisiones).
**Verbatim snippet:** "Para efectos de realizar la liquidación anteriormente referida por parte de KICHINK o del Agregador a favor de La TIENDA, ésta última deberá acumular un mínimo de venta de $150.00 (Ciento cincuenta pesos 00/100 MN) netos (después de descuentos y/o comisiones)."
**Source:** https://www.kichink.com/legales/terminos
**source_type:** policy_page
**verification_status:** blocked_url_index_verified
**Date:** Accessed April 2026; page undated
**Notes:** URL confirmada en índice de Google (título: "Términos y Condiciones para Compradores | Kichink"). Fetch directo devolvió 403. Snippet recuperado del índice de Google. Moneda explícita: MN (Moneda Nacional).

---

### F-P06

**Finding ID:** F-P06
**What:** Si el monto mínimo de $150 MN no es alcanzado, el Agregador puede procesar el pago con un cargo administrativo adicional del 10% con un mínimo de $10.00 MN más IVA.
**Verbatim snippet:** "Si el monto mínimo no es alcanzado, El Agregador podrá procesar el pago a petición de La Tienda con un cargo adicional por concepto administrativo del 10% (diez por ciento) con un mínimo a cobrar de $10.00 (diez pesos 00/100 moneda nacional) más IVA sobre el valor de la transacción."
**Source:** https://www.kichink.com/legales/terminos
**source_type:** policy_page
**verification_status:** blocked_url_index_verified
**Date:** Accessed April 2026; page undated
**Notes:** URL confirmada en índice de Google. Fetch directo devolvió 403. Moneda explícita: moneda nacional. IVA explícitamente adicional al 10%.

---

### F-P07

**Finding ID:** F-P07
**What:** Kichink o el Agregador descuentan el porcentaje de comisión del monto de ventas. El descuento se factura mensualmente; si la tienda no proporciona datos fiscales, el ingreso se factura como venta al público general y no podrá refacturarse posteriormente.
**Verbatim snippet:** "KICHINK o el Agregador designado, descontarán del monto de ventas realizadas por La TIENDA el porcentaje de comisión. El descuento realizado por KICHINK será facturado de manera mensual, por lo que La TIENDA deberá proporcionar sus datos fiscales para la facturación correspondiente durante el mes en curso, de lo contrario el ingreso será facturado como venta al público en General y no podrá re facturarse posteriormente."
**Source:** https://www.kichink.com/legales/terminos
**source_type:** policy_page
**verification_status:** blocked_url_index_verified
**Date:** Accessed April 2026; page undated
**Notes:** URL confirmada en índice de Google. Fetch directo devolvió 403. El snippet no especifica el porcentaje exacto de comisión; solo dice "el porcentaje de comisión" sin cuantificarlo en este pasaje.

---

### F-P08

**Finding ID:** F-P08
**What:** Los pagos a la tienda se realizan por medio de transferencia bancaria a la cuenta registrada por el administrador, una vez que la tienda haya solicitado la acción desde el portal de administrador (Kontrol).
**Verbatim snippet:** "KICHINK o el Agregador que designe realizará los pagos a La TIENDA, correspondientes a las órdenes de venta concretadas una vez que La TIENDA haya solicitado esta acción desde el portal de administrador; los pagos se realizan por medio de transferencia bancaria a la cuenta registrada por el administrador de La TIENDA."
**Source:** https://www.kichink.com/legales/terminos
**source_type:** policy_page
**verification_status:** blocked_url_index_verified
**Date:** Accessed April 2026; page undated
**Notes:** URL confirmada en índice de Google. Fetch directo devolvió 403. Establece que el pago NO es automático: la tienda debe solicitarlo.

---

### F-P09

**Finding ID:** F-P09
**What:** Kichink puede modificar las comisiones notificando a la tienda mediante aviso por medio electrónico.
**Verbatim snippet:** "La TIENDA acepta que las comisiones antes descritas por concepto de contraprestación por los servicios prestados por parte de KICHINK, podrán ser modificadas, para lo cual, KICHINK deberá comunicar a La TIENDA los cambios que se realicen en las comisiones mediante un aviso por medio electrónico."
**Source:** https://www.kichink.com/legales/terminos
**source_type:** policy_page
**verification_status:** blocked_url_index_verified
**Date:** Accessed April 2026; page undated
**Notes:** URL confirmada en índice de Google. Fetch directo devolvió 403. No especifica plazo de antelación para la notificación ni mecanismo de aceptación.

---

### F-P10

**Finding ID:** F-P10
**What:** El costo de la forma de pago "pago en puerta" es de $10.00 MXP (diez pesos) por envío.
**Verbatim snippet:** "El costo de la forma de pago, pago en puerta es de $10.00 MXP (diez pesos 00/100 moneda nacional) por envío"
**Source:** https://www.kichink.com/legales/terminos
**source_type:** policy_page
**verification_status:** blocked_url_index_verified
**Date:** Accessed April 2026; page undated
**Notes:** URL confirmada en índice de Google. Fetch directo devolvió 403. Moneda explícita: MXP (moneda nacional). Este cargo es por la forma de pago, no por la mensajería.

---

### F-P11

**Finding ID:** F-P11
**What:** El pago con tarjeta de crédito/débito procesado por un Agregador (en la opción de entrega BIP) está limitado a un monto máximo de $10,000 MX.
**Verbatim snippet:** "El pago con Tarjeta de Crédito/Débito procesado por un Agregador, está limitada a un monto máximo de $10,000 MX (diez mil pesos 00/100 moneda nacional)"
**Source:** https://www.kichink.com/legales/terminos
**source_type:** policy_page
**verification_status:** blocked_url_index_verified
**Date:** Accessed April 2026; page undated
**Notes:** URL confirmada en índice de Google. Fetch directo devolvió 403. Este límite aplica específicamente a la opción de entrega BIP® con pago en puerta, según el contexto circundante en el snippet.

---

### F-P12

**Finding ID:** F-P12
**What:** Los métodos de pago ofrecidos son: cuenta Kash®, tarjeta de crédito o débito, depósito bancario, depósito en tiendas con convenio, y pago en puerta (sujeto a disponibilidad BIP®).
**Verbatim snippet:** "El apartado Forma de pago pide seleccionar como medio de pago cualquiera de las opciones que se ofrecen: cuenta Kash®; Tarjeta de crédito o débito; Depósito Bancario; Depósito en Tiendas con convenio; Pago en Puerta (sujeto a la disponibilidad de acuerdo con la opción de entrega BIP®)."
**Source:** https://www.kichink.com/legales/terminos
**source_type:** policy_page
**verification_status:** blocked_url_index_verified
**Date:** Accessed April 2026; page undated
**Notes:** URL confirmada en índice de Google. Fetch directo devolvió 403. Esta lista es más detallada que la de /crea-tu-tienda (F-P04), incluyendo "Depósito en Tiendas con convenio" y la condicionalidad de "Pago en Puerta".

---

### F-P13

**Finding ID:** F-P13
**What:** Kichink define una "Cuota de administración de prevención de fraudes" como cuota por controles humanos y tecnológicos para prevenir transacciones de cargo no reconocido. No se especifica monto en este pasaje.
**Verbatim snippet:** "Cuota de administración de prevención de fraudes.- Cuota que cobra Kichink por los controles humanos y tecnológicos que se implementan para prevenir operaciones que deriven en transacciones de cargo no reconocido."
**Source:** https://www.kichink.com/legales/terminos
**source_type:** policy_page
**verification_status:** blocked_url_index_verified
**Date:** Accessed April 2026; page undated
**Notes:** URL confirmada en índice de Google. Fetch directo devolvió 403. Este es un término definido en la sección de definiciones de los T&C. El porcentaje o monto específico de esta cuota NO aparece en el snippet recuperado.

---

### F-P14

**Finding ID:** F-P14
**What:** En caso de contracargo (cargo no reconocido por el comprador), Kichink se reserva el derecho a iniciar acción legal coadyuvando con el Ministerio Público y la Institución Financiera.
**Verbatim snippet:** "En caso de que se presente una reclamación por cargo a tarjeta de crédito o débito no reconocida por El COMPRADOR (denominado Contracargo), KICHINK se reserva el derecho de iniciar la acción legal, coadyuvando con el Ministerio Público y la Institución Financiera para iniciar la Averiguación Previa por la comisión de un delito."
**Source:** https://www.kichink.com/legales/terminos
**source_type:** policy_page
**verification_status:** blocked_url_index_verified
**Date:** Accessed April 2026; page undated
**Notes:** URL confirmada en índice de Google. Fetch directo devolvió 403. El snippet no detalla quién absorbe el costo del contracargo (tienda o Kichink), solo la acción legal.

---

### F-P15

**Finding ID:** F-P15
**What:** Para ventas de eventos, servicios o archivos digitales, Kichink puede retener la totalidad de las ventas y solicitar confirmación de la realización del evento/servicio/descarga antes de pagar a la tienda.
**Verbatim snippet:** "Cuando las ventas realizadas por La TIENDA se deriven de la realización de un evento; la prestación de un servicio y/o la descarga de un archivo digital en cualquier formato, KICHINK podrá retener la cantidad total de las ventas realizadas por La TIENDA y solicitar a los usuarios la confirmación de la realización del evento; la prestación del servicio y/o la descarga del archivo digital previo al pago solicitado por La TIENDA."
**Source:** https://www.kichink.com/legales/terminos
**source_type:** policy_page
**verification_status:** blocked_url_index_verified
**Date:** Accessed April 2026; page undated
**Notes:** URL confirmada en índice de Google. Fetch directo devolvió 403. Esto implica un mecanismo de retención adicional al plazo de 10-90 días para productos digitales/servicios/eventos.

---

### F-P16

**Finding ID:** F-P16
**What:** La tienda libera de responsabilidad a Kichink por pagos no solicitados con antigüedad mayor a 1 año.
**Verbatim snippet:** "La TIENDA acepta y libera de responsabilidad a KICHINK por pagos no solicitados con antigüedad mayor a 1 (un) año."
**Source:** https://www.kichink.com/legales/terminos
**source_type:** policy_page
**verification_status:** blocked_url_index_verified
**Date:** Accessed April 2026; page undated
**Notes:** URL confirmada en índice de Google. Fetch directo devolvió 403. Esto significa que si la tienda no solicita cobrar sus ventas en un año, pierde el derecho a reclamarlas.

---

### F-P17

**Finding ID:** F-P17
**What:** Si las ventas acumuladas no superan el mínimo de $150 MN, se acumulan sin generar comisión, intereses ni cantidad adicional por el resguardo de fondos.
**Verbatim snippet:** "La TIENDA está de acuerdo en que, en el supuesto de que sus ventas realizadas no superen el mínimo de venta establecido, estas se acumularan hasta que el monto sea igual o superior al mínimo establecido para hacer la liquidación correspondiente sin que este hecho implique el pago adicional de comisión, intereses o alguna otra cantidad derivada del resguardo de fondos por parte de KICHINK."
**Source:** https://www.kichink.com/legales/terminos
**source_type:** policy_page
**verification_status:** blocked_url_index_verified
**Date:** Accessed April 2026; page undated
**Notes:** URL confirmada en índice de Google. Fetch directo devolvió 403. Este pasaje es continuación lógica de F-P05 pero constituye una regla de política distinta (no se generan intereses por acumulación).

---

### F-P18

**Finding ID:** F-P18
**What:** La cadena de conveniencia cobra al comprador una comisión de $8.00 por pago en efectivo.
**Verbatim snippet:** "Recuerda que la cadena te cobra una comisión de $8.00"
**Source:** https://www.kichink.com/pagos
**source_type:** pricing_page
**verification_status:** blocked_url_index_verified
**Date:** Accessed April 2026; page undated
**Notes:** URL confirmada en índice de Google (título: "Pagos | Kichink"). Fetch directo devolvió 403. Snippet muy corto/truncado por el índice. No se explicita moneda (MXN inferible por contexto pero NO PRESENTE en el snippet). No se especifica a qué cadena(s) aplica.

---

### F-P19

**Finding ID:** F-P19
**What:** Kichink no tiene cuotas fijas: no signup, no mensualidad, no anualidad.
**Verbatim snippet:** "Kichink is the only fully managed service that does not have Signup, Monthly, Yearly, Bianual, centennial, millennial fees... we repeat, NO FIXED FEES, so you can spend in actually growing your business"
**Source:** https://www.kichink.com/create-your-store
**source_type:** pricing_page
**verification_status:** blocked_url_index_verified
**Date:** Accessed April 2026; page undated
**Notes:** URL confirmada en índice de Google (título: "Create your store | Kichink"). Fetch directo devolvió 403. Contenido en inglés (versión en inglés de la página de alta de tienda). Complementa F-P01 que dice "NO TIENE COSTO" en español.

---

### F-P20

**Finding ID:** F-P20
**What:** Los tiempos estimados de procesamiento de reembolso (una vez autorizado) son: pago con TDC 5 días hábiles, pago con banca por internet 5 días hábiles, depósito bancario 5 días hábiles.
**Verbatim snippet:** "Los tiempos estimados para el procesamiento de un Reembolso una vez autorizado el mismo son los siguientes: Pago con TDC tiempo de 5 días hábiles. Pago con Banca por internet 5 días hábiles. Depósito Bancario 5 días hábiles."
**Source:** https://www.kichink.com/legales/politicacambiosydevoluciones
**source_type:** policy_page
**verification_status:** blocked_url_index_verified
**Date:** Accessed April 2026; page undated
**Notes:** URL confirmada en índice de Google (título: "Políticas de Devolución y Cancelación | Kichink"). Fetch directo devolvió 403. TDC = Tarjeta de Crédito. El snippet añade que "el tiempo de espera para que el reembolso se vea reflejado estará sujeto a lo establecido por el banco emisor" pero este pasaje no fue incluido por ser un passage separado.

---

### F-P21

**Finding ID:** F-P21
**What:** Las opciones de reembolso para el comprador son: abono a cuenta Kash® (sin reembolso de envío), transferencia bancaria por el total de la compra, o cupón por el monto total con vigencia máxima de 90 días.
**Verbatim snippet:** "Abono a su Cuenta Kash®: El COMPRADOR, podrá solicitar el abono del importe del producto devuelto a su Cuenta Kash®; sin embargo, el costo del envió no podrá ser reembolsado y en ningún caso será absorbido por KICHINK. Transferencia bancaria: El Comprador podrá solicitar la devolución mediante transferencia bancaria por el total de la compra. Cupón: Si así lo desea, El Comprador podrá solicitar un cupón por el monto total de su compra, mismo que podrá ser utilizado por El Comprador para realizar cualquier otra compra en Las Tiendas afiliadas con Kichink, en un plazo no mayor a 90 días."
**Source:** https://www.kichink.com/legales/terminos
**source_type:** policy_page
**verification_status:** blocked_url_index_verified
**Date:** Accessed April 2026; page undated
**Notes:** URL confirmada en índice de Google. Fetch directo devolvió 403. El pasaje lista tres opciones consecutivas. No se pudo verificar si es un solo bloque continuo en la página original ya que no se tuvo acceso directo; sin embargo, aparece como pasaje consecutivo en el snippet del índice de Google.

---

### F-P22

**Finding ID:** F-P22
**What:** La tienda debe confirmar la orden de compra y programar la recolección del producto en un plazo máximo de 72 horas hábiles posteriores a la compra.
**Verbatim snippet:** "La TIENDA debe confirmar la orden de compra y programar la recolección del producto o los productos comprados en un plazo máximo de 72 horas hábiles posteriores a la compra por parte del COMPRADOR."
**Source:** https://www.kichink.com/legales/terminos
**source_type:** policy_page
**verification_status:** blocked_url_index_verified
**Date:** Accessed April 2026; page undated
**Notes:** URL confirmada en índice de Google. Fetch directo devolvió 403. Esto es un plazo operativo, no un fee, pero constituye una mecánica de plataforma relevante para el flujo de pago.

---

## 4. Part 3 — Pattern candidates (sealed)

### PC-01
El menú de navegación de kichink.com incluye una sección denominada "Precios &amp; Planes", lo que sugiere la existencia de una página con información de pricing/tiers que no pudo ser localizada ni accedida en ninguna URL probada.

### PC-02
La infraestructura de help center de Kichink (ayuda.kichink.com y kichinkservicios.zendesk.com) no devuelve resultados en ningún motor de búsqueda ni responde a peticiones directas, indicando que no hay contenido indexado accesible de ninguno de los dos dominios al momento de la investigación.

### PC-03
Todas las páginas de kichink.com (al menos las 6 URLs intentadas) devolvieron HTTP 403 (Forbidden) en acceso directo, aunque el contenido de estas páginas sigue siendo indexado por Google con snippets extensos y títulos actualizados que incluyen "© 2025 Kichink Servicios S.A. de C.V."

---

## 5. Part 4 — Could not verify / Out-of-scope

### F-X01: Sistema de tiers de comisión basado en calificación de vendedor (escala 4.0–5.0)

Múltiples fuentes de terceros (EstiloMXMedia, MarketHax, Terrabionic, comentarios de vendedores) describen un sistema de tiers donde la comisión varía de 8.5% (vendedor experto, calificación 5.0) a 15.25% (principiante, calificación 4.0). Sin embargo, **ninguna página oficial de Kichink** accedida o recuperada del índice de Google contiene estos porcentajes específicos. La página /crea-tu-tienda dice "a partir del 15%" sin detallar tiers. Fuentes de terceros no son source_type permitido → excluido de clean/provisional.

### F-X02: Contenido de la página "Precios &amp; Planes"

El menú de navegación de kichink.com incluye un enlace a "Precios &amp; Planes" pero la URL exacta no pudo ser determinada (se probaron /precios, /planes sin éxito). Si esta página existe, podría contener la tabla de tiers de comisión. **Búsqueda activa realizada; resultado: ausencia confirmada de contenido accesible.**

### F-X03: Contenido del help center (ayuda.kichink.com / kichinkservicios.zendesk.com)

La URL de Garantía KICHINK referenciada en los T&C (kichinkservicios.zendesk.com/hc/es) no devuelve resultados en buscadores ni responde a fetch directo. El subdominio ayuda.kichink.com tampoco tiene contenido indexado. **Help center aparentemente defunct.**

### F-X04: Monto/porcentaje específico de la "Cuota de administración de prevención de fraudes"

La definición de este fee aparece en los T&C (ver F-P13) pero el monto o porcentaje específico **no aparece en ningún snippet recuperado**. Es posible que esté en una sección del T&C no capturada por el índice de Google.

### F-X05: Comisión diferenciada para productos digitales (reportada como 3.8%)

Un artículo de prensa de 2013 (365historiasdeexito/blogspot) y una fuente de prensa posterior citan "3.8% para productos digitales" vs. "7.5% para mercancía física". Esta diferenciación no aparece en ninguna página oficial de Kichink actualmente accesible o indexada. **Fuente de terceros; no verificable contra fuente oficial actual.**

---

## 6. Research QA Notes

### 6.1 Findings forzados a provisional y razones

Todos los findings (F-P01 a F-P22) fueron clasificados como `blocked_url_index_verified` en lugar de `direct_verified` porque **todas las URLs de kichink.com devolvieron HTTP 403 (Forbidden)** en acceso directo. El contenido fue recuperado exclusivamente de snippets del índice de búsqueda de Google, que muestran la URL exacta, título de página y extractos extensos del contenido. Las URLs están fijadas con certeza (coinciden con dominio, path y título esperado).

### 6.2 Degradaciones

- **F-P18** (comisión $8.00 de la cadena): el snippet es extremadamente corto ("Recuerda que la cadena te cobra una comisión de $8.00") y no explicita moneda. Se mantuvo como provisional por la URL exacta confirmada (kichink.com/pagos), pero la ausencia de moneda explícita es una limitación.
- **F-P21** (opciones de reembolso): el snippet contiene tres métodos consecutivos. No se pudo verificar si es un pasaje continuo en la página original. Se mantuvo como un solo finding provisional pero con nota de incertidumbre sobre continuidad del passage.
- **F-X01 a F-X05**: todos degradados a "could not verify" por provenir de fuentes de terceros (no permitidas como source_type) o por ausencia de contenido oficial accesible.

### 6.3 Multi-speaker splits

No aplica. Todas las fuentes son páginas oficiales de Kichink (un solo emisor institucional).

### 6.4 Ambigüedades de source_type

- **kichink.com/crea-tu-tienda**: clasificada como `pricing_page` porque describe costos, comisiones y tarifas de envío para vendedores, aunque también funciona como landing page de registro.
- **kichink.com/legales/terminos**: clasificada como `policy_page`. Nota: el título de Google dice "Términos y Condiciones para Compradores" pero el contenido incluye extensas cláusulas sobre comisiones, pagos y obligaciones de la tienda (vendedor). Es posible que exista un documento separado de T&C para tiendas no localizado.
- **kichink.com/create-your-store**: clasificada como `pricing_page` (versión en inglés de crea-tu-tienda).

### 6.5 Coverage gaps identificados

1. **Porcentaje exacto de comisión por transacción**: La página /crea-tu-tienda dice "a partir del 15%" pero no detalla la tabla completa de tiers. La página "Precios &amp; Planes" (referenciada en el menú de navegación) no pudo ser localizada. El rango 8.5%–15.25% solo aparece en fuentes de terceros.
2. **Comisión diferenciada para productos digitales**: no verificable contra fuentes oficiales actuales.
3. **Calendario específico de pagos**: los T&C dicen "10 a 90 días naturales" pero no establecen un calendario fijo (ej. primer y tercer viernes del mes).
4. **Métodos de pago disponibles por región/país**: no se encontró información oficial que detalle qué métodos están disponibles en México vs. otros países, excepto la mención general de envíos internacionales.
5. **Help center completo**: todo el contenido del help center de Kichink es inaccesible, lo que probablemente elimina múltiples findings potenciales sobre mecánicas operativas, FAQ de comisiones, etc.
6. **Monto de la cuota de prevención de fraudes**: definida en los T&C como concepto pero sin cuantificar en los snippets recuperados.

### 6.6 Casos no descomponibles

SD-17 (sistema de tiers de comisión) y SD-18 (contenido de "Precios &amp; Planes") no pudieron resolverse con las fuentes oficiales accesibles. La información de tiers solo existe en fuentes de terceros que están excluidas del scope de este shard.

### 6.7 Nota metodológica

Dado que el sitio kichink.com bloquea acceso directo con HTTP 403, todos los verbatim snippets fueron extraídos del índice de búsqueda de Google. Estos snippets representan lo que Google ha indexado de las páginas oficiales de Kichink y corresponden a las URLs exactas indicadas. Sin embargo, es posible que: (a) el contenido indexado por Google no esté actualizado al momento de acceso; (b) los snippets sean fragmentarios y no capturen el contenido completo de la página; (c) existan secciones de las páginas (especialmente tablas, accordions, contenido dinámico o detrás de login) que Google no haya indexado. El footer "© 2025 Kichink Servicios S.A. de C.V." visible en los resultados sugiere que las páginas estaban activas al menos hasta 2025.

---

*Fin del output de Data Gathering — Shard Kichink × D1*