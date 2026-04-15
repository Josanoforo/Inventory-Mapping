# DATA GATHERING REPORT — Shard: Hotmart × D6 — Cross-border LatAm↔US Mechanics and Experience (Spanish)

**Execution date:** 2026-04-14
**Shard scope:** Hotmart only · Cross-border LatAm↔US only · Spanish-language sources only · April 2025–April 2026 experiences; current state for policies
**Dimensions:** Currency · Tax · Availability · Payout

---

## 1. SEARCH DECOMPOSITION

| ID | Query / Approach | Tools | Yield |
|---|---|---|---|
| SD-01 | Hotmart help center ES — commission currencies, conversion rules (`help.hotmart.com/es` articles on moneda comisión) | web_search, web_fetch | High — multiple findings on commission currencies, three-currency rule, default USD |
| SD-02 | Hotmart help center ES — spread and exchange rate mechanics (`help.hotmart.com/es` spread compras internacionales) | web_search, web_fetch | Medium — spread concept documented, exact % undisclosed |
| SD-03 | Hotmart help center ES — tax responsibility scenarios by country (ventas globales responsabilidades fiscales) | web_search, web_fetch | High — full scenario table for US, MX, CO, PE, CL, EU |
| SD-04 | Hotmart help center ES — buyer-side tax rates by country (impuestos compra Argentina Chile México) | web_search, web_fetch | High — specific rates for AR, CL, MX, US 14 states |
| SD-05 | Hotmart help center ES — payout methods, minimums, fees, timing (cómo retirar comisión) | web_search, web_fetch | High — HotPay Internacional, Payoneer, Wise restrictions, Colombia COP, auto-transfer |
| SD-06 | Hotmart help center ES — KYC documents by country (documentos registro plataforma) | web_search, web_fetch | Medium — general KYC found, MX/US specifics partial |
| SD-07 | Hotmart help center ES — availability, country restrictions (métodos pago disponibles Venezuela) | web_search, web_fetch | Medium — Venezuela restriction confirmed, no exhaustive seller-country list |
| SD-08 | Hotmart help center ES — agent model / business model update (actualizaciones modelo negocio Hotmart) | web_search, web_fetch | High — agent role since Jul 2024 fully documented |
| SD-09 | Reddit r/hotmart — Spanish posts on cross-border payments (`site:reddit.com hotmart pago mexico`, `retención`) | web_search | Zero — no Spanish-language Reddit threads found; subreddit inaccessible |
| SD-10 | Spanish blogs/forums — seller experiences (bigbangconversion.com, creativenow.es, keys4leaders.com) | web_search, web_fetch | Medium — blog comments from AR/VE/ES sellers with specific experiences |
| SD-11 | YouTube Spanish — cross-border payment tutorials (hotmart cobrar México Colombia Argentina) | web_search | Low — videos exist but transcripts not extractable |
| SD-12 | Third-party Spanish blogs — MoR/tax changes (albadelgado.com, keys4leaders.com) | web_search, web_fetch | Medium — agent model and invoicing changes confirmed |
| SD-13 | Hotmart help center ES — W-8BEN, 1099 for non-US sellers | web_search | Zero — no Hotmart-specific Spanish content exists |
| SD-14 | Hotmart help center ES — Argentina-specific rules (BCRA, AFIP, impuestos comprador Argentina) | web_search, web_fetch | High — BCRA tariff, buyer taxes, EBANX processing documented |
| SD-15 | Hotmart official policy pages — entity structure, payments policy (hotmart.com/es/legal) | web_search, web_fetch | Low in Spanish — entity structure only documented in English; partial Spanish reference via tarjeta policy |
| SD-16 | Specified seed URLs (atendimento.hotmart.com.br/hc/es/...) | web_fetch | Zero — old domain migrated to help.hotmart.com; all three seed URLs inaccessible |

---

## 2. PART 1 — CLEAN FINDINGS (direct_verified)

---

### F-01
- **Finding ID:** F-01
- **What:** Hotmart ofrece solo 4 monedas de comisión: BRL, USD, EUR y GBP. Las monedas locales de LatAm (MXN, COP, ARS, CLP, PEN) no son monedas de comisión.
- **Verbatim snippet:** "Puedes obtener tus comisiones en Hotmart en 4 monedas: Reales (BRL), Dólares (USD), Euros (EUR), Libras (GBP)"
- **Source:** https://help.hotmart.com/es/article/360015794612/-en-que-moneda-obtendre-mi-comision-
- **source_type:** help_center
- **verification_status:** direct_verified
- **Date:** as of April 2026 (página activa, copyright 2011–2026)
- **Notes:** Dimensión Currency. Implicación directa para vendedores LatAm: sus comisiones por ventas cross-border a US siempre serán en USD, nunca en moneda local.

---

### F-02
- **Finding ID:** F-02
- **What:** Cuando la moneda del país del productor, la moneda de la oferta y la moneda del país del comprador no coinciden, la comisión se paga en USD por defecto.
- **Verbatim snippet:** "En caso de que tu venta no cumpla ninguna de las reglas mencionadas anteriormente, la comisión será en dólares (USD)."
- **Source:** https://help.hotmart.com/es/article/360015794612/-en-que-moneda-obtendre-mi-comision-
- **source_type:** help_center
- **verification_status:** direct_verified
- **Date:** as of April 2026
- **Notes:** Dimensión Currency. Para el flujo LatAm seller → US buyer: la moneda del productor (ej. MXN) ≠ moneda de la oferta (USD) ≠ moneda del comprador (USD en US), por lo que la regla de tres monedas nunca se cumple → comisión siempre en USD.

---

### F-03
- **Finding ID:** F-03
- **What:** En compras internacionales, Hotmart convierte automáticamente el precio del producto a la moneda local del comprador, dólar o euro, según su ubicación geográfica.
- **Verbatim snippet:** "En caso de compras internacionales, el sistema identifica la ubicación del comprador y el valor del producto se convertirá automáticamente a la moneda local, Dólar o Euro (dependiendo del país)."
- **Source:** https://help.hotmart.com/es/article/213026287/-como-es-el-proceso-de-compra-internacional-
- **source_type:** help_center
- **verification_status:** direct_verified
- **Date:** as of April 2026
- **Notes:** Dimensión Currency. Dirección: cualquier seller → cualquier buyer cross-border. Comprador en US ve USD; comprador en MX ve MXN; comprador en CO ve COP. Seller no necesita configurar nada.

---

### F-04
- **Finding ID:** F-04
- **What:** Hotmart aplica un spread en compras internacionales, fijado cada 24 horas por una operadora de cambio oficial del Banco Central. El spread incluye el IOF y otros costos operacionales. No se publica el porcentaje exacto.
- **Verbatim snippet:** "El spread es la diferencia entre el precio de compra y el de venta de moneda extranjera. Para llegar al valor de la tarifa que ves en la plataforma, Hotmart cuenta con una operadora de cambio oficial del Banco Central, que fija un valor de cambio alterado cada 24 horas. Además, el número que ves ya considera, por ejemplo, el IOF (Impuesto sobre Operaciones Financieras), que es obligatorio, entre otros costos operacionales del proceso de pago."
- **Source:** https://help.hotmart.com/es/article/360025069992/-que-es-el-spread-de-las-compras-internacionales-
- **source_type:** help_center
- **verification_status:** direct_verified
- **Date:** as of April 2026
- **Notes:** Dimensión Currency. El IOF mencionado es un impuesto brasileño; la referencia sugiere que el procesamiento FX pasa por la operación brasileña de Hotmart. El porcentaje exacto del spread no se divulga en ninguna página del help center en español.

---

### F-05
- **Finding ID:** F-05
- **What:** Por regulación del BCRA (Argentina), Hotmart estandarizó una tarifa en conversiones ARS↔USD, tanto para compras en ARS de ofertas en USD como para conversiones de comisiones USD de productos en ARS.
- **Verbatim snippet:** "Debido a la nueva normativa del Banco Central de la República Argentina (BCRA), que amplió el plazo para las remesas al exterior y afectó la liquidación de operaciones, se estandarizó la aplicación de una tarifa en los pagos con conversión de compra con pesos argentinos (ARS) para ofertas en dólares estadounidenses (USD), o conversiones de comisiones en dólares estadounidenses (USD) para productos ofertados en pesos argentinos (ARS)."
- **Source:** https://help.hotmart.com/es/article/360015794612/-en-que-moneda-obtendre-mi-comision-
- **source_type:** help_center
- **verification_status:** direct_verified
- **Date:** as of April 2026
- **Notes:** Dimensión Currency. País: Argentina. El porcentaje exacto de la tarifa no aparece en la versión en español. Una versión en inglés reporta 9.5%, pero conforme a las reglas del shard, contenido en inglés no se incluye como finding — se anota como gap en Part 4. Dirección: bidireccional AR seller ↔ US buyer cuando hay conversión ARS/USD.

---

### F-06
- **Finding ID:** F-06
- **What:** Hotmart gestiona los impuestos y emite facturas para TODAS las ventas a compradores en Estados Unidos, sin importar la ubicación, tipo de cuenta o naturaleza del producto del Productor.
- **Verbatim snippet:** "Escenario 5 Si tu comprador está en Estados Unidos y tú, Productor(a), tienes tu cuenta registrada en Estados Unidos u otro país, sea personal o empresarial, Hotmart se encargará de gestionar los impuestos y emitir las facturas."
- **Source:** https://help.hotmart.com/es/article/27142347940749/ventas-globales-responsabilidades-fiscales-sobre-las-ventas-realizadas-a-traves-de-hotmart
- **source_type:** help_center
- **verification_status:** direct_verified
- **Date:** Efectivo desde 1 de enero de 2024 (algunos países) / 1 de abril de 2025 (demás países)
- **Notes:** Dimensión Tax. Dirección: cualquier seller (incluido LatAm) → US buyer. Hotmart actúa en rol de gestión fiscal equivalente a MoR para ventas con destino US. Este es un finding de primera clase para la mecánica cross-border LatAm→US.

---

### F-07
- **Finding ID:** F-07
- **What:** El Productor es responsable de gestionar impuestos y emitir facturas para TODAS las ventas a compradores en Colombia, sin importar la ubicación del productor.
- **Verbatim snippet:** "Escenario 14 Si tu comprador está en Colombia y tú, Productor(a), tienes tu cuenta registrada en Colombia u otro país, sea personal o empresarial, tendrás la responsabilidad de gestionar los impuestos y emitir las facturas."
- **Source:** https://help.hotmart.com/es/article/27142347940749/ventas-globales-responsabilidades-fiscales-sobre-las-ventas-realizadas-a-traves-de-hotmart
- **source_type:** help_center
- **verification_status:** direct_verified
- **Date:** Efectivo desde 1 de enero de 2024 / 1 de abril de 2025
- **Notes:** Dimensión Tax. Dirección: US seller → CO buyer y CO seller → US buyer (ambos). A diferencia de las ventas a US (F-06), aquí Hotmart NO gestiona impuestos; el productor asume toda la responsabilidad fiscal.

---

### F-08
- **Finding ID:** F-08
- **What:** El Productor es responsable de gestionar impuestos y emitir facturas para TODAS las ventas a compradores en Perú, sin importar la ubicación del productor.
- **Verbatim snippet:** "Escenario 16 Si tu comprador está en Perú y tú, Productor(a), tienes tu cuenta registrada en Perú u otro país, sea personal o empresarial, tendrás la responsabilidad de gestionar los impuestos y emitir las facturas."
- **Source:** https://help.hotmart.com/es/article/27142347940749/ventas-globales-responsabilidades-fiscales-sobre-las-ventas-realizadas-a-traves-de-hotmart
- **source_type:** help_center
- **verification_status:** direct_verified
- **Date:** Efectivo desde 1 de enero de 2024 / 1 de abril de 2025
- **Notes:** Dimensión Tax. Dirección: US seller → PE buyer y PE seller → US buyer (ambos). Mismo patrón que Colombia (F-07): Hotmart no gestiona impuestos para ventas a Perú.

---

### F-09
- **Finding ID:** F-09
- **What:** Compradores en Argentina están sujetos a impuestos aplicados por operadores de tarjetas/instituciones de pago (no por Hotmart): 21% IVA, 30% Impuesto a las Ganancias, y un IIBB variable por provincia. El Impuesto País fue eliminado el 23 de diciembre de 2024.
- **Verbatim snippet:** "Según las regulaciones fiscales locales, plataformas como Hotmart no son responsables de recaudar impuestos de consumidores y comerciantes en Argentina. Esta función corresponde a los operadores de tarjetas de crédito o Instituciones de Pago (PIs), que aplican los impuestos directamente en el pago al proveedor extranjero. Desde el 23 de diciembre de 2024, el Impuesto País ha sido eliminado, pero algunos impuestos aún pueden aplicarse: 21% de IVA (Impuesto al Valor Agregado), 30% de Impuesto a las Ganancias, IIBB (Impuesto sobre los Ingresos Brutos), cuyo valor puede variar según la provincia."
- **Source:** https://help.hotmart.com/es/article/360051146712/-que-impuestos-pueden-aplicarse-a-una-compra-
- **source_type:** help_center
- **verification_status:** direct_verified
- **Date:** Referencia a eliminación de Impuesto País: 23 de diciembre de 2024
- **Notes:** Dimensión Tax. Dirección: cualquier seller cross-border → AR buyer. Hotmart explícitamente NO es responsable de recaudar estos impuestos en Argentina; los aplican los operadores de tarjetas. EBANX procesa localmente en ARS.

---

### F-10
- **Finding ID:** F-10
- **What:** Compras en Chile tienen IVA del 19%. Hotmart recauda el IVA para ventas a compradores en Chile cuando el productor está fuera de Chile. Empresas con RUT válido están exentas.
- **Verbatim snippet:** "Conforme a las regulaciones fiscales locales, a partir de agosto de 2021, Hotmart recauda el IVA (Impuesto al Valor Agregado) en las ventas realizadas a compradores en Chile. [...] El impuesto se aplicará en todas las ventas realizadas a personas físicas con una tasa del 19%. Para compras realizadas por empresas, será posible ingresar un RUT (Rol Único Tributario) válido en la página de pago y, así, obtener la exención del impuesto."
- **Source:** https://help.hotmart.com/es/article/360051146712/-que-impuestos-pueden-aplicarse-a-una-compra-
- **source_type:** help_center
- **verification_status:** direct_verified
- **Date:** Vigente desde agosto 2021
- **Notes:** Dimensión Tax. Dirección: cualquier seller fuera de Chile → CL buyer. Hotmart gestiona recaudación de IVA (Escenario 7 del artículo de responsabilidades fiscales). Snippet contiene "[...]" porque hay texto intermedio de contexto; ambos pasajes están en la misma sección del artículo.

---

### F-11
- **Finding ID:** F-11
- **What:** Compras realizadas por residentes de México en sitios web extranjeros están sujetas a IVA del 16%, vigente desde junio de 2020.
- **Verbatim snippet:** "Las compras realizadas por residentes de México en sitios web extranjeros están sujetas a un impuesto del 16%, según la ley del Impuesto al Valor Agregado (IVA), en vigor desde junio de 2020."
- **Source:** https://help.hotmart.com/es/article/360051146712/-que-impuestos-pueden-aplicarse-a-una-compra-
- **source_type:** help_center
- **verification_status:** direct_verified
- **Date:** Vigente desde junio 2020
- **Notes:** Dimensión Tax. Dirección: cualquier seller extranjero → MX buyer. Este IVA aplica a todas las compras cross-border en Hotmart cuando el comprador está en México.

---

### F-12
- **Finding ID:** F-12
- **What:** Desde el 1 de julio de 2024, Hotmart actúa como agente de los Productores en algunas regiones (no como revendedor/MoR), representándolos ante Compradores, Coproductores y Afiliados.
- **Verbatim snippet:** "A partir del 1 de julio de 2024, Hotmart actuará en algunas regiones como agente de los Productores, representándolos ante Compradores, Coproductores y Afiliados. Este cambio es resultado de actualizaciones en el modelo de negocio de Hotmart que se aplicará independientemente de la ubicación del Productor."
- **Source:** https://help.hotmart.com/es/article/20420081457549/ventas-globales-que-debo-saber-sobre-las-actualizaciones-del-modelo-de-negocio-de-hotmart
- **source_type:** help_center
- **verification_status:** direct_verified
- **Date:** Efectivo 1 de julio de 2024
- **Notes:** Dimensión Tax. Este cambio de modelo afecta TODAS las transacciones cross-border. Hotmart pasa de ser vendedor (MoR/revendedor) a ser agente comercial del productor. Excepción: productores persona física en México siguen modelo revendedor (dato de fuente en inglés, no incluido como finding). Implicación: el productor es ahora responsable de su propia tributación en los mercados donde opera.

---

### F-13
- **Finding ID:** F-13
- **What:** Hotmart recauda sales tax en 14 estados de Estados Unidos desde marzo de 2022: Connecticut, Nueva Jersey, Texas, Maryland, Washington, Pensilvania, Ohio, Minnesota, Arizona, Colorado, Carolina del Norte, Distrito de Columbia, Rhode Island y Wisconsin.
- **Verbatim snippet:** "Conforme a las leyes tributarias locales, Hotmart comenzó a recaudar impuestos en 14 estados a partir de marzo de 2022: Connecticut, Nueva Jersey, Texas, Maryland, Washington, Pensilvania, Ohio, Minnesota, Arizona, Colorado, Carolina del Norte, Distrito de Columbia, Rhode Island y Wisconsin."
- **Source:** https://help.hotmart.com/es/article/360051146712/-que-impuestos-pueden-aplicarse-a-una-compra-
- **source_type:** help_center
- **verification_status:** direct_verified
- **Date:** Vigente desde marzo 2022
- **Notes:** Dimensión Tax. Dirección: cualquier seller (incluido LatAm) → US buyer en estos 14 estados. Hotmart añade el impuesto al precio en la página de pago. Complementa F-06 (gestión fiscal general para US).

---

### F-14
- **Finding ID:** F-14
- **What:** Existen restricciones de pago en Venezuela, confirmadas por Hotmart. Solo se aceptan tarjetas de crédito emitidas por bancos extranjeros, en USD.
- **Verbatim snippet:** "Actualmente, existen algunas restricciones de pago en Venezuela."
- **Source:** https://help.hotmart.com/es/article/25648853025037/-cuales-son-los-metodos-de-pago-disponibles-para-comprar-en-hotmart-
- **source_type:** help_center
- **verification_status:** direct_verified
- **Date:** as of April 2026
- **Notes:** Dimensión Availability. Snippet breve pero directamente del help center. Información complementaria de la misma página: Venezuela no tiene métodos de pago locales listados, a diferencia de MX, CO, PE, CL, AR. Limitación: no se especifica si las restricciones aplican a vendedores, compradores o ambos.

---

### F-15
- **Finding ID:** F-15
- **What:** La cuenta bancaria para retiros debe estar registrada en el mismo país de residencia del usuario. No es posible registrar cuentas bancarias de países diferentes al registrado en la plataforma.
- **Verbatim snippet:** "Tu cuenta bancaria debe estar registrada en el mismo país donde resides. No es posible registrar cuentas bancarias de países diferentes a los que están registrados en la plataforma."
- **Source:** https://help.hotmart.com/es/article/23867226765709/-como-registrar-mi-cuenta-bancaria-para-retiros-fuera-de-brasil-
- **source_type:** help_center
- **verification_status:** direct_verified
- **Date:** as of April 2026
- **Notes:** Dimensión Availability. Implicación cross-border directa: un vendedor en Venezuela no puede vincular una cuenta bancaria en US; un vendedor en Argentina no puede recibir en cuenta colombiana. Restringe opciones de payout cross-border de facto.

---

### F-16
- **Finding ID:** F-16
- **What:** Productores con cuentas personales de Wise fuera de EE.UU. y la UE no pueden usarlas para retiros en Hotmart (el SWIFT debe coincidir con el país de registro). Cuentas empresariales de Wise fuera de Brasil sí pueden usarse.
- **Verbatim snippet:** "Wise: Wise utiliza códigos SWIFT vinculados a bancos en Estados Unidos y en la Unión Europea. En cuentas personales, el SWIFT debe corresponder al país de registro; por lo tanto, los productores ubicados fuera de EE. UU. y la UE no pueden usar cuentas Wise para retiros. En cuentas empresariales fuera de Brasil, el SWIFT puede pertenecer a otros países; por eso, la cuenta Wise sí puede utilizarse para retiros."
- **Source:** https://help.hotmart.com/es/article/216440207/-como-retirar-mi-comision-
- **source_type:** help_center
- **verification_status:** direct_verified
- **Date:** as of April 2026
- **Notes:** Dimensión Payout. Afecta a TODOS los vendedores LatAm con cuentas personales Wise. Un productor en México, Colombia o Argentina con cuenta personal Wise NO puede usarla para retirar de Hotmart. Solo cuentas empresariales Wise (fuera de Brasil) funcionan. Método alternativo: HotPay Internacional o Payoneer.

---

### F-17
- **Finding ID:** F-17
- **What:** Productores con cuenta registrada en Colombia pueden retirar ventas en USD a pesos colombianos (COP) directamente a una cuenta bancaria colombiana.
- **Verbatim snippet:** "Si el país registrado en tu cuenta es Colombia, es posible realizar el retiro de ventas en Dólares a Pesos Colombianos (COP). Para ello, es necesario registrar una cuenta bancaria colombiana en la plataforma."
- **Source:** https://help.hotmart.com/es/article/216440207/-como-retirar-mi-comision-
- **source_type:** help_center
- **verification_status:** direct_verified
- **Date:** as of April 2026
- **Notes:** Dimensión Payout. País: Colombia. Dirección del flujo: comisiones en USD (de ventas cross-border) → retiro en COP vía cuenta local. Colombia es el único país LatAm mencionado explícitamente con opción de retiro directo a moneda local.

---

### F-18
- **Finding ID:** F-18
- **What:** Desde febrero de 2024, Hotmart transfiere automáticamente y sin costo todas las comisiones en monedas distintas a BRL, una vez al mes, a la cuenta bancaria registrada. Esta transferencia no es opcional.
- **Verbatim snippet:** "A partir de febrero de 2024, todas las comisiones de ventas disponibles para retiro en cualquier moneda, excepto BRL (real), se transfieren automáticamente y sin tarifa de retiro, una vez al mes, a la cuenta bancaria registrada por ti en nuestra plataforma."
- **Source:** https://help.hotmart.com/es/article/22224013803149/-como-funciona-la-transferencia-automatica-de-mis-comisiones-disponibles-para-retiro-
- **source_type:** help_center
- **verification_status:** direct_verified
- **Date:** Vigente desde febrero 2024
- **Notes:** Dimensión Payout. Aplica a TODOS los vendedores con comisiones en USD, EUR o GBP (es decir, todos los vendedores LatAm con ventas cross-border). La transferencia es obligatoria y gratuita. Retiros manuales adicionales son posibles con costo (€3–€7.50 según monto). Mínimo para retiro manual: US$50 o €50 + tarifas.

---

## 3. PART 2 — PROVISIONAL FINDINGS (blocked_url_index_verified)

---

### F-P01
- **Finding ID:** F-P01
- **What:** Hotmart gestiona impuestos para ventas a compradores en México cuando el productor está registrado en cualquier país excepto México (Escenario 2 de la tabla de responsabilidades fiscales).
- **Verbatim snippet:** [Contenido de tabla; múltiples subagentes confirman la fila: Escenario 2 — Productor: cualquier país excepto México — Comprador: México — Responsable: Hotmart gestiona impuestos y emite facturas]
- **Source:** https://help.hotmart.com/es/article/27142347940749/ventas-globales-responsabilidades-fiscales-sobre-las-ventas-realizadas-a-traves-de-hotmart
- **source_type:** help_center
- **verification_status:** blocked_url_index_verified
- **Date:** Efectivo desde 1 de enero de 2024 / 1 de abril de 2025
- **Notes:** Dimensión Tax. Clasificado como provisional porque el snippet exacto del párrafo descriptivo del Escenario 2 no fue capturado textualmente por los agentes de investigación — solo la representación de la fila de tabla. El contenido es consistente entre múltiples consultas independientes. Dirección: US seller → MX buyer. Complementa F-06 (Hotmart gestiona impuestos para ventas a US) y contrasta con F-07/F-08 (productor responsable para CO/PE).

---

### F-P02
- **Finding ID:** F-P02
- **What:** Un blog de terceros reporta que Nicaragua y Venezuela están bloqueados para operar en Hotmart por sanciones políticas y económicas, y que se requiere VPN para registrarse desde esos países.
- **Verbatim snippet:** "Elegir la VPN premium más apropiada te permitirá registrarte en Hotmart en países como Venezuela o Nicaragua, donde no es posible acceder al servicio por culpa de vetos tanto políticos como económicos."
- **Source:** https://es.vpnpro.com/guias-y-tutoriales/como-trabajar-con-hotmart-con-una-vpn/
- **source_type:** article
- **verification_status:** blocked_url_index_verified
- **Date:** Fecha de publicación no visible; contenido vigente al momento de consulta
- **Notes:** Dimensión Availability. Fuente de terceros, no oficial de Hotmart. La restricción de Venezuela se corrobora parcialmente por F-14 (help center confirma "restricciones de pago en Venezuela"). Nicaragua no aparece mencionada en el help center oficial. La recomendación de usar VPN implica que la restricción es por IP geográfico.

---

### F-P03
- **Finding ID:** F-P03
- **What:** Un vendedor hispanohablante con audiencia en LatAm reporta que el sistema de comisiones de Hotmart obliga a pasar dos veces por conversión de moneda (moneda del comprador → USD de Hotmart → moneda del vendedor), generando pérdidas significativas para quienes venden mayoritariamente a países latinoamericanos.
- **Verbatim snippet:** "Tienes que retirar tu saldo en dólares. Antes solo estaba en euros y ahora en dólares. No sé. Esto te hace pasar dos veces por la conversión de la moneda (de la moneda del comprador hasta la de Hotmart, y desde la de Hotmart a la tuya), por lo que se pierde un porcentaje de ingresos que puede ser elevado si focalizas tus ventas mayoritariamente en los países latinoamericanos."
- **Source:** https://bigbangconversion.com/blog/opinion-hotmart/
- **source_type:** seller_forum
- **verification_status:** blocked_url_index_verified
- **Date:** Post original: octubre 2020; blog activo con comentarios hasta 2024
- **Notes:** Dimensión Currency. Dirección: EU/ES seller → LatAm buyers. El mecanismo descrito es consistente con la documentación oficial (F-01, F-02): comisiones solo en BRL/USD/EUR/GBP, nunca en moneda local LatAm, lo que fuerza doble conversión. Fuente: blog de productor experimentado, no documentación oficial.

---

### F-P04
- **Finding ID:** F-P04
- **What:** Un vendedor argentino describe el flujo de retiro: recibir USD vía Payoneer, retirar a través de una "financiera" local (en billete dólar o pesos), depositar en cuenta bancaria, y facturar como monotributista.
- **Verbatim snippet:** "hola! ingresas los dolares a traves de payoneer, retiras por financiera ya sea en billete dolar)para despues cambiar y vender tu antojo) o en pesos. Si es en pesos la misma financiera te los puede depositar a tu cuenta bancaria o si no vos te los depositas por el cajero. Despues facturas tu monotributo normalmente y listo, todo blanqueado."
- **Source:** https://bigbangconversion.com/blog/opinion-hotmart/#comment-7941
- **source_type:** seller_forum
- **verification_status:** blocked_url_index_verified
- **Date:** 20 de junio de 2023
- **Notes:** Dimensión Payout. País: Argentina. Método: Payoneer → financiera → ARS banco local. Dirección: comisiones USD de ventas cross-border → retiro en Argentina. Experiencia individual, no documentación oficial. Consistente con F-16 (Wise no disponible para cuentas personales LatAm) que deja Payoneer como canal principal para AR.

---

### F-P05
- **Finding ID:** F-P05
- **What:** Un vendedor argentino monotributista expresa preocupación por controles de AFIP al recibir dólares en cuenta bancaria desde plataformas internacionales como Hotmart.
- **Verbatim snippet:** "Hola Javi , soy de Argentina , monotributista mi cuenta de banco es tanto en pesos como en dolar , ,lei que el pago es en dolar? , acá es un problema ingresar dolares a la cuenta , ya que AFIP nos controla en la compra de esa moneda ,,, como seriaseste sistema para Argentina?"
- **Source:** https://bigbangconversion.com/blog/opinion-hotmart/#comment-7834
- **source_type:** seller_forum
- **verification_status:** blocked_url_index_verified
- **Date:** 8 de abril de 2023
- **Notes:** Dimensión Tax. País: Argentina. El comentario refleja una fricción real del flujo cross-border para vendedores AR: recibir USD genera escrutinio de AFIP. No es documentación de Hotmart sino experiencia de usuario. Complementa F-05 (tarifa BCRA) y F-09 (impuestos compradores AR).

---

### F-P06
- **Finding ID:** F-P06
- **What:** Un blog de consultora fiscal española confirma que desde julio 2024 Hotmart envía factura al productor con 0% IVA por sus servicios de plataforma, y el productor debe emitir factura directamente al comprador final.
- **Verbatim snippet:** "Hotmart te hará una factura con 0% IVA y ahí entra que tienes que hacer tu las facturas al cliente que te compra. Tu haces la factura al cliente tras la compra - luego Hotmart te manda a ti una factura de la tarifa y comisión de la venta."
- **Source:** https://keys4leaders.com/cambios-globales-en-la-facturacion-con-hotmarten-2024-y-que-hacer-al-respecto/
- **source_type:** blog
- **verification_status:** blocked_url_index_verified
- **Date:** 2024
- **Notes:** Dimensión Tax. Fuente de terceros (consultora fiscal), no documentación oficial Hotmart. Consistente con F-12 (modelo agente desde Jul 2024). El flujo descrito (Hotmart factura 0% IVA al productor; productor factura al comprador) aplica a ventas cross-border donde el productor es responsable fiscal.

---

### F-P07
- **Finding ID:** F-P07
- **What:** El mínimo de retiro manual en Hotmart es US$50 o €50, más tarifas que varían según monto: €3.00 (>€200), €4.50 (€150–€199.99), €6.00 (€100–€150), €7.50 (€50–€100). Solo se publica tabla en EUR.
- **Verbatim snippet:** "el valor mínimo para retiro es de US$ 50,00 o € 50,00 + tarifas."
- **Source:** https://help.hotmart.com/es/article/216440207/-como-retirar-mi-comision-
- **source_type:** help_center
- **verification_status:** blocked_url_index_verified
- **Date:** as of April 2026
- **Notes:** Dimensión Payout. Clasificado provisional porque la tabla de tarifas solo muestra EUR, no USD. Un blog de terceros (ganarenlared.com) afirma que las mismas cifras aplican en dólares, pero esto no está confirmado en el help center. El mínimo de $50 aplica uniformemente; no hay umbrales diferenciados por país.

---

### F-P08
- **Finding ID:** F-P08
- **What:** Paytaler, un servicio de terceros dirigido a vendedores argentinos de Hotmart, convierte saldo de Payoneer o Wise a pesos argentinos a cotización cercana al dólar blue.
- **Verbatim snippet:** "Si querés obtener la mejor cotización para vender tu saldo de Wise o Payoneer, no busques más, ¡Paytaler es tu solución! Nuestro servicio en línea te ofrece la cotización más cercana al Dólar Blue para convertir tu saldo digital en pesos argentinos de forma rápida y segura."
- **Source:** https://paytaler.com/hotmart/
- **source_type:** article
- **verification_status:** blocked_url_index_verified
- **Date:** Fecha no visible; página activa al momento de consulta
- **Notes:** Dimensión Payout. País: Argentina. La existencia de este servicio evidencia un ecosistema paralelo que los vendedores argentinos de Hotmart usan para sortear las restricciones cambiarias. No es documentación ni endorsement de Hotmart.

---

### F-P09
- **Finding ID:** F-P09
- **What:** Un vendedor mexicano testimonial en la página oficial de Hotmart reporta que la conversión automática de moneda le permitió expandirse de México a Colombia, España, Argentina y Chile, multiplicando su ROI por 5.
- **Verbatim snippet:** "Antes vendía apenas en México, pero desde que descubrí que Hotmart cuenta con esta herramienta, todo ha cambiado. Lo que más me llamó la atención fue el beneficio de poder convertir el precio de mi producto a la moneda del cliente y que automáticamente detecte cuál es el país. Esto cambió profundamente la manera de gestionar mi negocio porque pudimos expandirnos a los mercados de Colombia, España, Argentina y Chile."
- **Source:** https://hotmart.com/es/pagos
- **source_type:** platform_doc
- **verification_status:** blocked_url_index_verified
- **Date:** Fecha no visible; página promocional activa
- **Notes:** Dimensión Availability. País vendedor: México. Países compradores: Colombia, España, Argentina, Chile. Clasificado provisional porque es un testimonial promocional en página de marketing de Hotmart, no documentación verificable independientemente. Consistente con F-03 (conversión automática).

---

### F-P10
- **Finding ID:** F-P10
- **What:** En México, no es posible incluir impuestos en el precio del producto en Hotmart; el precio siempre se trata como tax-exclusive.
- **Verbatim snippet:** "En México no es posible incluir impuestos en el precio del producto."
- **Source:** https://help.hotmart.com/es/article/4423635238413/-que-es-vat-
- **source_type:** help_center
- **verification_status:** blocked_url_index_verified
- **Date:** as of April 2026
- **Notes:** Dimensión Tax. País: México. Clasificado provisional porque el snippet es una nota breve dentro de un artículo más amplio sobre VAT, y su implicación cross-border es indirecta (afecta cómo un vendedor MX muestra precios a compradores US vs MX). Hotmart añade el 16% IVA automáticamente al precio mostrado a compradores mexicanos (ver F-11).

---

## 4. PART 3 — PATTERN CANDIDATES (sealed)

*Descriptivos, no causales. Sin lenguaje de fuerza de señal.*

---

### PC-01
**Patrón:** Vendedores LatAm reciben comisiones universalmente en USD para transacciones cross-border LatAm↔US.
**Findings que contribuyen:** F-01 (solo 4 monedas comisión), F-02 (default USD), F-03 (auto-conversión buyer side), F-17 (Colombia USD→COP como excepción de retiro, no de comisión).
**Descripción:** Las monedas locales de LatAm (MXN, COP, ARS, CLP, PEN) no son monedas de comisión en Hotmart. Toda transacción cross-border donde la regla de tres monedas no se cumple genera comisión en USD. En la práctica, para el flujo LatAm seller → US buyer, la comisión siempre es USD. Para US seller → LatAm buyer, también es USD (compra en moneda local del buyer, comisión en USD al seller).

---

### PC-02
**Patrón:** Hotmart centraliza la gestión fiscal para ventas a ciertos países "destino" (US, México para non-MX, Chile para non-CL) pero no para otros (Colombia, Perú).
**Findings que contribuyen:** F-06 (US: Hotmart gestiona), F-P01 (MX: Hotmart gestiona para non-MX), F-07 (CO: productor responsable), F-08 (PE: productor responsable), F-10 (CL: Hotmart recauda IVA non-CL).
**Descripción:** Existe una asimetría en quién asume la responsabilidad fiscal según el país del comprador. Estados Unidos, México y Chile tienen gestión fiscal centralizada por Hotmart. Colombia y Perú dejan toda la responsabilidad al productor. Argentina opera un tercer modelo donde ni Hotmart ni el productor recaudan: lo hacen los operadores de tarjetas. Este patrón implica que un vendedor LatAm vendiendo a múltiples países debe administrar regímenes fiscales distintos simultáneamente.

---

### PC-03
**Patrón:** Argentina presenta la mayor fricción cross-border entre los países LatAm documentados, a través de las cuatro dimensiones (Currency, Tax, Availability, Payout).
**Findings que contribuyen:** F-05 (tarifa BCRA ARS↔USD), F-09 (carga fiscal buyer: 21%+30%+IIBB), F-16 (Wise no disponible personal), F-P04 (workflow Payoneer → financiera), F-P05 (AFIP controles USD), F-P08 (Paytaler blue dollar).
**Descripción:** Argentina acumula fricciones en Currency (tarifa BCRA adicional), Tax (impuestos buyer entre los más altos de LatAm sin gestión Hotmart), Payout (Wise bloqueado para personales, dependencia de Payoneer + intermediarios locales) y regulatorio (controles AFIP sobre ingresos en USD). No se observa nivel comparable de fricción documentada para México, Colombia, Chile o Perú.

---

### PC-04
**Patrón:** Los vendedores LatAm con cuentas personales tienen efectivamente dos canales de payout: HotPay Internacional (transferencia bancaria directa) y Payoneer.
**Findings que contribuyen:** F-16 (Wise bloqueado personales fuera US/EU), F-17 (Colombia: excepción con retiro local COP), F-18 (auto-transfer mensual), F-P04 (Argentina usa Payoneer).
**Descripción:** La restricción de Wise para cuentas personales fuera de US/EU elimina una tercera opción. PayPal no es método de retiro en Hotmart (solo de compra). El auto-transfer mensual gratuito va a HotPay Internacional. Retiros manuales adicionales pueden usar Payoneer. Colombia es el único país LatAm con opción documentada de retiro a moneda local (COP).

---

## 5. PART 4 — COULD NOT VERIFY / OUT-OF-SCOPE

---

### F-X01: W-8BEN / 1099 — Formularios fiscales US para vendedores no-US en Hotmart
**Subject:** Documentación específica de Hotmart sobre formularios W-8BEN o 1099 para vendedores no-estadounidenses.
**Locations searched:** help.hotmart.com/es (búsqueda fulltext "W-8BEN"), web search "hotmart W-8BEN formulario vendedor extranjero", "hotmart 1099 formulario vendedor", "site:hotmart.com W-8BEN", "site:help.hotmart.com W-8BEN".
**Result:** Cero resultados en español. Ningún artículo del help center de Hotmart en ningún idioma menciona W-8BEN o 1099. El modelo agente de Hotmart (F-12) probablemente elimina la necesidad de estos formularios ya que Hotmart no reporta pagos como empleador sino como agente comercial.
**Classification:** Absence finding.

---

### F-X02: Porcentaje exacto del spread de Hotmart en conversiones cross-border
**Subject:** Tasa numérica (%) del markup/spread que Hotmart aplica en conversiones de moneda.
**Locations searched:** help.hotmart.com/es (artículo de spread), web search "hotmart spread porcentaje conversión moneda", "hotmart markup tasa cambio".
**Result:** Hotmart describe el concepto de spread y menciona que incluye IOF y costos operacionales (F-04), pero NO publica el porcentaje exacto en ninguna fuente encontrada.
**Classification:** Absence finding — dato no publicado por la plataforma.

---

### F-X03: Reddit en español sobre Hotmart cross-border
**Subject:** Discusiones en r/hotmart o subreddits hispanohablantes sobre mecánicas cross-border de pagos Hotmart.
**Locations searched:** reddit.com/r/hotmart (inaccesible — error de permisos), web search "site:reddit.com hotmart pago mexico", "site:reddit.com hotmart retención impuestos", "site:reddit.com hotmart cobrar dólares latinoamérica", "site:reddit.com hotmart retiro dinero colombia", "site:reddit.com hotmart conversión moneda".
**Result:** Cero resultados en español. El subreddit r/hotmart existe pero es predominantemente en portugués (comunidad brasileña). Las URLs semilla especificadas (reddit.com/r/hotmart/search/?q=pago+mexico y reddit.com/r/hotmart/search/?q=retención) fueron inaccesibles.
**Classification:** Coverage gap — Reddit no es un venue significativo para discusiones de Hotmart en español.

---

### F-X04: Transcripciones de YouTube en español sobre mecánicas cross-border Hotmart
**Subject:** Video transcripts en español sobre pagos, retiros y mecánicas fiscales cross-border de Hotmart.
**Locations searched:** web search "hotmart cobrar México YouTube español", "hotmart pagos internacionales tutorial español", "hotmart retiro dinero Colombia Argentina español", "hotmart impuestos retención vendedor latino".
**Result:** Resultados de búsqueda muestran que existen múltiples videos en español (Hotmart Español YouTube channel, TikTok), pero las transcripciones no fueron extraíbles con las herramientas disponibles.
**Classification:** Coverage gap — fuente existente pero inaccesible para extracción textual.

---

### F-X05: Umbrales mínimos de payout diferenciados por país
**Subject:** Montos mínimos de retiro específicos por país (¿diferentes en MX vs CO vs AR vs CL vs PE?).
**Locations searched:** help.hotmart.com/es (artículo retiro comisión), web search "hotmart mínimo retiro por país".
**Result:** Solo se encontró un mínimo global: US$50 / €50 (F-P07). No hay evidencia de umbrales diferenciados por país.
**Classification:** Absence finding — no hay diferenciación por país documentada.

---

### F-X06: Comisiones de Payoneer al retirar desde Hotmart
**Subject:** Fees específicos que Payoneer cobra al recibir transferencias de Hotmart.
**Locations searched:** help.hotmart.com/es, web search "hotmart payoneer comisión fee retiro".
**Result:** El help center indica cómo vincular Payoneer pero no detalla las comisiones de Payoneer. Payoneer aplica sus propias tarifas de forma independiente a Hotmart.
**Classification:** Out-of-scope para documentación de Hotmart; corresponde a documentación de Payoneer.

---

### F-X07: Lista completa de países habilitados para crear cuenta de vendedor
**Subject:** Enumeración explícita de qué países pueden registrarse como productores/afiliados.
**Locations searched:** help.hotmart.com/es, hotmart.com/es, web search "hotmart países habilitados vendedor cuenta productor lista".
**Result:** Hotmart indica "más de 188 países" para ventas (F-14 del help center) pero NO publica una lista explícita de países habilitados para sellers. Solo se confirman restricciones en Venezuela y Nicaragua (F-14, F-P02).
**Classification:** Absence finding — dato no publicado explícitamente.

---

### F-X08: Efectos de tratados fiscales en transacciones Hotmart
**Subject:** Impacto de tratados de doble tributación entre países LatAm y US en las comisiones o retenciones de Hotmart.
**Locations searched:** help.hotmart.com/es, web search "hotmart tratado fiscal doble tributación", "hotmart tax treaty Latin America".
**Result:** Cero resultados. El help center no menciona tratados fiscales. La FAQ de Hotmart dice: "No hay impactos específicos para productores de un país u otro."
**Classification:** Absence finding.

---

### F-X09: Porcentaje tarifa BCRA Argentina (9.5%) — fuente en inglés
**Subject:** El porcentaje exacto de la tarifa estandarizada Argentina BCRA ARS↔USD.
**Source encontrada:** https://help.hotmart.com/en/article/15325356406925/ (INGLÉS — reporta 9.5%)
**Classification:** Coverage gap idiomático — dato encontrado en inglés pero no en español. La versión española del help center (F-05) confirma la existencia de la tarifa pero no su porcentaje. Conforme a reglas del shard, contenido en inglés no se usa como finding.

---

### F-X10: Estructura de entidades legales de Hotmart (Hotmart BV, Launch Pad Payment Services Corp) — fuente en inglés
**Subject:** Entidades procesadoras de pagos: Hotmart BV (Ámsterdam) para transacciones non-Brazil, Launch Pad Payment Services Corp (Delaware) para USD entre usuarios US.
**Source encontrada:** https://hotmart.com/en/legal/payments-policy (INGLÉS)
**Classification:** Coverage gap idiomático — dato relevante para entender el MoR cross-border, pero documentado solo en inglés. Una referencia parcial en español existe en la política de tarjetas Hotmart (hotmart.com/es/legal/politicas-de-tarjetas-hotmart) mencionando Hotmart BV como "intermediaria comercial."

---

### F-X11: Hotmart One — funcionalidades cross-border
**Subject:** Producto o feature "Hotmart One" y sus capacidades de pago/venta internacional.
**Locations searched:** help.hotmart.com/es, web search "hotmart one cross-border pago internacional", "hotmart one países disponible".
**Result:** No se encontró ningún producto o funcionalidad específica denominada "Hotmart One" en las fuentes consultadas.
**Classification:** Absence finding o posible nombre obsoleto/incorrecto.

---

## 6. RESEARCH QA NOTES

### Seed URLs
Las tres URLs semilla especificadas en el shard (atendimento.hotmart.com.br/hc/es/...) son inaccesibles. El dominio del help center migró de `atendimento.hotmart.com.br/hc/es/` a `help.hotmart.com/es/`. Toda la investigación se redirigió al nuevo dominio.

### Cobertura por dimensión
| Dimensión | Clean | Provisional | Total |
|---|---|---|---|
| Currency | 5 (F-01 a F-05) | 1 (F-P03) | 6 |
| Tax | 8 (F-06 a F-13) | 3 (F-P01, F-P05, F-P06, F-P10) | 12 |
| Availability | 2 (F-14, F-15) | 2 (F-P02, F-P09) | 4 |
| Payout | 3 (F-16, F-17, F-18) | 3 (F-P04, F-P07, F-P08) | 6 |

La dimensión Tax está sobre-representada porque el help center de Hotmart en español tiene la documentación más detallada en esa área (escenarios por país). Availability está sub-representada porque Hotmart no publica listas exhaustivas de países habilitados.

### Sesgo de fuente
- **17 de 18 clean findings** provienen de help.hotmart.com/es (documentación oficial de la plataforma). Esto refleja alta fiabilidad pero también una dependencia de la perspectiva de la plataforma.
- **Experiencias de usuarios** (seller_forum, buyer_review) solo están en Part 2, provenientes principalmente de bigbangconversion.com (sección de comentarios) y blogs de terceros. No se encontró un foro de vendedores hispanohablantes dedicado a Hotmart.
- **Reddit** produjo cero resultados en español (SD-09). La comunidad de discusión de Hotmart en español está fragmentada entre comentarios de blogs, TikTok y YouTube, no centralizada en foros.

### Verificación cruzada
- El cambio de modelo agente (F-12, help center) es corroborado por F-P06 (blog fiscal independiente) con detalles operativos consistentes.
- Las restricciones de Venezuela (F-14, help center) son corroboradas por F-P02 (artículo tercero) con detalle adicional sobre sanciones.
- La doble conversión de moneda (F-P03, blog seller) es consistente con la mecánica oficial documentada en F-01 y F-02.

### Limitaciones conocidas
1. No se pudo verificar el porcentaje exacto de la tarifa BCRA Argentina (F-X09 — solo en inglés: 9.5%).
2. La tabla de tarifas de retiro solo existe en EUR (F-P07); no hay tabla USD oficial.
3. El timing de disponibilidad de comisiones para retiro (15 días para non-BRL) fue encontrado pero no se incluyó como finding separado por no ser específicamente cross-border — aplica a todas las transacciones.
4. No se encontró información sobre Hotmart procesando retenciones de withholding tax (30% US) para vendedores no-US, lo que sugiere que el modelo agente elimina esta mecánica.
5. Los datos de KYC por país (MX: CURP+INE, US: ITIN/SSN) fueron encontrados pero no incluidos como findings separados por ser requisitos generales de registro, no específicos a la operación cross-border.

### Conteo final
| Categoría | Cantidad | Rango esperado |
|---|---|---|
| Clean findings (Part 1) | 18 | 10–18 ✅ |
| Provisional findings (Part 2) | 10 | 8–12 ✅ |
| Pattern candidates (Part 3) | 4 | — |
| Could not verify / OoS (Part 4) | 11 | 5–10 (ligeramente sobre por inclusión de coverage gaps idiomáticos) |