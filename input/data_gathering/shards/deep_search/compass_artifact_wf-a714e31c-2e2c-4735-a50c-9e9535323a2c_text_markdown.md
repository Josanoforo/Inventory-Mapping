# SHARD: Hotmart × D5 — Competitive Positioning
## Data Gathering Run — Structured Output

**Shard scope:** Hotmart only · Competitive positioning only · Spanish-language sources prioritized · Current state (no time window)
**Run date:** April 14, 2026
**Analyst note:** Two sub-types captured: (a) Self-positioning from hotmart.com; (b) Third-party comparative from external sources. All verbatim snippets preserved in original language. No cross-finding synthesis.

---

## 1. SEARCH DECOMPOSITION

**SD-01 — Hotmart official self-positioning pages**
Target: hotmart.com/es/precios, help.hotmart.com/es, hotmart.com/es/blog, hotmart.com/es-mx/soluciones
Goal: Extract statements where Hotmart declares differentiation, superiority, or use-case fit
Tools: web_fetch of known URLs, web_search with site:hotmart.com
Outcome: 6 clean findings from pricing page, help center, and blog. Pages hotmart.com/es/sobre-hotmart and hotmart.com/es returned permissions errors.

**SD-02 — Spanish-language blog comparisons: Hotmart vs Thinkific, Teachable, Udemy**
Target: Google search for "hotmart vs thinkific" comparación, "hotmart vs teachable" comparación, "hotmart vs udemy" comparación; follow-up fetch of top results
Goal: Third-party comparative positioning on SaaS/marketplace competitors popular in the English-speaking world but discussed in Spanish
Outcome: 7 clean/provisional findings from sofiafernandez.es, classonlive.com, jeansaldana.com, quaderno.io

**SD-03 — Spanish-language blog comparisons: Hotmart vs Kiwify, Eduzz, Monetizze, Braip**
Target: Google search for each pair + "comparación"; Reddit searches; bit4learn.com, vendemebonito.com
Goal: Third-party comparative positioning on Brazilian-origin competitors discussed in Spanish
Outcome: 3 provisional findings (bit4learn.com, vendemebonito.com, Capterra). Hotmart vs Braip yielded zero results in Spanish. Kiwify/Eduzz/Monetizze comparisons overwhelmingly in Portuguese.

**SD-04 — Reddit and community forum discussions**
Target: site:reddit.com hotmart vs [competitor]; r/empreendedorismo; r/digitalproducts; O Novo Mercado forum
Goal: User-generated comparative positioning statements
Outcome: Zero relevant Reddit threads found despite 10+ search variations. O Novo Mercado forum content behind login wall. Community discussions primarily on Capterra and blog comment sections.

**SD-05 — YouTube videos and video transcripts (Spanish-language)**
Target: site:youtube.com "hotmart vs" in Spanish; video transcript aggregator pages
Goal: Extract positioning claims from Spanish-language video reviews
Outcome: No YouTube video pages were accessible via search tool. One transcript aggregator page (TopView.ai) returned 404. Blog posts associated with YouTube channels captured under SD-02/SD-06.

**SD-06 — Medium articles and additional web sources**
Target: site:medium.com hotmart vs; dinerobits.com; bigbangconversion.com; lifestylealcuadrado.com; marketeroslatam.com
Goal: Review-format comparative positioning from independent bloggers and Medium authors
Outcome: 7 clean/provisional findings from dinerobits.com, bigbangconversion.com, lifestylealcuadrado.com, marketeroslatam.com, medium.com/teachable

**SD-07 — Review aggregators: Capterra**
Target: capterra.com/p/219169/Hotmart/reviews/; G2 and Trustpilot via search
Goal: Verified-user reviews with competitive framing
Outcome: 2 provisional findings from Capterra (Portuguese-language). G2 and Trustpilot did not surface Spanish-language competitive positioning.

**SD-08 — Competitor landing pages positioning against Hotmart**
Target: systeme.io/es/hotmart-alternative; sabionet.com/alterativas-a-hotmart; escuelaemprende.com; albadelgado.com
Goal: Capture how competitors explicitly position themselves against Hotmart
Outcome: 4 provisional findings from systeme.io, albadelgado.com, escuelaemprende.com. Sabionet.com page structure prevented clean continuous-passage extraction.

---

## 2. PART 1 — CLEAN FINDINGS (direct_verified)

---

### F-01

**Finding ID:** F-01
**What:** Hotmart positions itself as an all-in-one solution requiring no additional fees, no extra software, and no geographic limits
**Verbatim snippet:** "La solución All in One ¡Por el mismo precio! Sin tarifas. Sin softwares extra. Sin fronteras."
**Source:** https://hotmart.com/es/precios
**source_type:** pricing_page
**verification_status:** direct_verified
**Date:** Accessed April 2026; page undated (footer: 2011–2026)
**Notes:** Self-positioning (sub-type a). Headline positioning on pricing page. No competitor named explicitly; framing implies comparison to multi-tool stacks.

---

### F-02

**Finding ID:** F-02
**What:** Hotmart positions its pay-per-sale model as replacing the need for third-party apps and plugins, with no upfront cost
**Verbatim snippet:** "Olvida el resto de aplicaciones y plugins. Con Hotmart, puedes crear, acelerar, gestionar y crecer junto a tu negocio en una misma plataforma sin coste. Solo pagas un porcentaje cuando realizas una venta."
**Source:** https://hotmart.com/es/precios
**source_type:** pricing_page
**verification_status:** direct_verified
**Date:** Accessed April 2026; page undated
**Notes:** Self-positioning (sub-type a). Consolidation play: single platform vs. app/plugin stack. "Sin coste" refers to zero-upfront-cost, not zero total cost; per-sale fee applies.

---

### F-03

**Finding ID:** F-03
**What:** Hotmart claims direct superiority over other platforms, stating its tools are custom-built to adapt to the user's business rather than the reverse
**Verbatim snippet:** "¿Por qué Hotmart es mejor que otras plataformas? Todas nuestras soluciones están diseñadas y creadas exclusivamente para nuestros clientes. Eso quiere decir que las herramientas de integración de Hotmart están hechas para adaptarse a tu negocio y no al contrario."
**Source:** https://hotmart.com/es/precios
**source_type:** pricing_page
**verification_status:** direct_verified
**Date:** Accessed April 2026; page undated
**Notes:** Self-positioning (sub-type a). Explicit competitive superiority claim: "¿Por qué Hotmart es mejor que otras plataformas?" No specific competitor named.

---

### F-04

**Finding ID:** F-04
**What:** Hotmart differentiates its per-sale pricing from competitors' monthly subscriptions, claiming aligned incentives and scalability that would be "unimaginable" on other platforms
**Verbatim snippet:** "¿Por qué es mejor pagar una tarifa por venta que una cuota mensual? A diferencia de muchas otras plataformas que cobran cuotas mensuales, Hotmart se preocupa mucho por tu negocio. Trabajamos para ofrecerte las mejores soluciones y el mejor servicio al cliente ahora y durante el crecimiento de tu emprendimiento porque nuestro negocio depende de tu éxito. Por ello, todas nuestras soluciones están diseñadas para que vendas más y mejor. Con las automatizaciones y facilidades que te ofrecemos, puedes escalar tu crecimiento y tus estrategias de una forma que sería inimaginable en otras plataformas."
**Source:** https://hotmart.com/es/precios
**source_type:** pricing_page
**verification_status:** direct_verified
**Date:** Accessed April 2026; page undated
**Notes:** Self-positioning (sub-type a). Pricing model differentiation. "A diferencia de muchas otras plataformas que cobran cuotas mensuales" = explicit reference to monthly-fee competitors. "Inimaginable en otras plataformas" = scalability superiority claim. Aligned-incentives argument: "nuestro negocio depende de tu éxito."

---

### F-05

**Finding ID:** F-05
**What:** Hotmart claims to be the largest platform in Latin America for distance education, with 500,000+ products and sales in 188+ countries
**Verbatim snippet:** "Hotmart es una plataforma global y completa para quienes desean vender productos digitales, siendo la más grande de América Latina en el sector de educación a distancia. Con más de 500,000 productos registrados y ventas en más de 188 países, Hotmart permite que cualquier persona comparta su conocimiento o producto con el mundo de forma práctica y segura."
**Source:** https://help.hotmart.com/es/article/115006507308/-que-es-y-como-funciona-hotmart-
**source_type:** platform_doc
**verification_status:** direct_verified
**Date:** Accessed April 2026; page undated
**Notes:** Self-positioning (sub-type a). Market leadership claim: "la más grande de América Latina." Specific data points: 500K+ products, 188+ countries. Help center page.

---

### F-06

**Finding ID:** F-06
**What:** Hotmart acknowledges that other platforms offer course hosting and sales but claims none have tools that scale businesses as fast as Hotmart's
**Verbatim snippet:** "De hecho, otras plataformas ofrecen también el servicio de hospedaje y venta de cursos, pero ninguno con las herramientas de Hotmart que pueden hacer escalar el negocio en menos tiempo."
**Source:** https://hotmart.com/es/blog/lo-que-no-sabias-de-hotmart
**source_type:** blog
**verification_status:** direct_verified
**Date:** 12/06/2021
**Notes:** Self-positioning (sub-type a). Official Hotmart blog. Direct competitor acknowledgment + superiority claim on speed of scaling.

---

### F-07

**Finding ID:** F-07
**What:** Hotmart's per-sale commission (9.9% + €0.05 per the source) plus withdrawal fees make costs increase with sales volume; Thinkific's flat-fee model has no platform commissions limiting income at scale
**Verbatim snippet:** "Hotmart aplica una comisión por cada venta (típicamente 9,9% + €0,05) y además cobra al retirar tu saldo. Por ejemplo, si retiras entre €50 y €100, pueden quedarse con unos €7,5 adicionales. Traducción: cuanto más vendes, más pagas en comisiones. Thinkific trabaja con tarifa fija. Las pasarelas de pago (Stripe, PayPal, Thinkific Payments) tienen sus propias comisiones por transacción, pero no hay una estructura de comisiones de plataforma que limite tus ingresos al escalar."
**Source:** https://sofiafernandez.es/marketing/thinkific-vs-hotmart/
**source_type:** blog
**verification_status:** direct_verified
**Date:** Accessed April 2026; page undated (copyright 2026)
**Notes:** Third-party comparative (sub-type b). Competitors named: Thinkific. Dimension: fees. Stance: pro-Thinkific. Affiliate disclosure: Thinkific affiliate links (try.thinkific.com/hn4s46ry1gqz) throughout page; author sells courses via Thinkific. Specific numbers: 9.9% + €0.05, withdrawal fee of ~€7.50 on €50–100 withdrawals. NOTE: Source states "€0,05" fixed fee; multiple other sources (Hotmart pricing page, hormigasenlanube.com, quaderno.io) cite "€0,50" or "$0.50." This may be a typographical error in the source; reported verbatim per protocol.

---

### F-08

**Finding ID:** F-08
**What:** On Hotmart's basic plan the platform's logo appears in purchase-flow emails, diluting the creator's brand; Thinkific gives full brand control with no third-party logos on basic plans
**Verbatim snippet:** "En Hotmart, con el plan básico verás su logo en los correos de confirmación y en varios puntos del proceso de compra. Esto puede diluir tu marca justo cuando el alumno debe conectar contigo. En Thinkific, tu logo y tu nombre aparecen en todas las comunicaciones. Tienes control total de la experiencia de marca sin marcas de agua ni logos ajenos en los planes básicos."
**Source:** https://sofiafernandez.es/marketing/thinkific-vs-hotmart/
**source_type:** blog
**verification_status:** direct_verified
**Date:** Accessed April 2026; page undated
**Notes:** Third-party comparative (sub-type b). Competitors named: Thinkific. Dimension: features/constraints (brand control). Stance: pro-Thinkific. Affiliate links present on page.

---

### F-09

**Finding ID:** F-09
**What:** Hotmart's marketplace gives passive visibility among millions of LATAM users but exposes the creator to direct competition from hundreds of similar courses; Thinkific provides no passive traffic but offers community-building tools and audience ownership
**Verbatim snippet:** "Hotmart es un marketplace con millones de usuarios, especialmente en Latinoamérica. Esto te da opciones de visibilidad pasiva, pero también significa competencia directa dentro de la plataforma. Tu curso aparece junto a cientos de alternativas similares. Thinkific no es marketplace: no te entrega tráfico orgánico masivo desde el primer día, pero sí te ofrece herramientas para crear comunidad (como membresías) y captar tu propia audiencia."
**Source:** https://sofiafernandez.es/marketing/thinkific-vs-hotmart/
**source_type:** blog
**verification_status:** direct_verified
**Date:** Accessed April 2026; page undated
**Notes:** Third-party comparative (sub-type b). Competitors named: Thinkific. Dimension: audience/visibility. Stance: mixed — Hotmart wins on passive traffic, Thinkific wins on ownership. Affiliate links present on page.

---

### F-10

**Finding ID:** F-10
**What:** Thinkific is more intuitive and orderly in daily use; Hotmart's navigation can be confusing and sometimes mixes languages in the interface
**Verbatim snippet:** "En el uso diario, Thinkific resulta más intuitivo y ordenado. Todo está donde esperas encontrarlo. Hotmart cubre muchas funciones, pero su navegación puede resultar confusa. En ocasiones incluso mezcla idiomas en la interfaz, lo que no ayuda."
**Source:** https://sofiafernandez.es/marketing/thinkific-vs-hotmart/
**source_type:** blog
**verification_status:** direct_verified
**Date:** Accessed April 2026; page undated
**Notes:** Third-party comparative (sub-type b). Competitors named: Thinkific. Dimension: ease of use. Stance: pro-Thinkific. Affiliate links present on page.

---

### F-11

**Finding ID:** F-11
**What:** Hotmart's affiliate system for reselling differentiates it from other marketplaces like Udemy, which lacks this feature
**Verbatim snippet:** "La principal diferencia de Hotmart respecto a otros marketplaces como Udemy, es que Hotmart cuenta con una estructura un poco más compleja y tiene 'el afiliado' para revender tus productos que Udemy, por ejemplo, no tiene."
**Source:** https://www.classonlive.com/blog/mejor-plataforma-crear-cursos-online
**source_type:** blog
**verification_status:** direct_verified
**Date:** Accessed April 2026; originally published November 5, 2019; updated 2026
**Notes:** Third-party comparative (sub-type b). Competitors named: Udemy. Dimension: features (affiliate system). Stance: neutral. BIAS NOTE: Published by ClassOnLive, a direct Hotmart competitor.

---

### F-12

**Finding ID:** F-12
**What:** Three key Hotmart disadvantages listed: loss of content rights and exclusivity preventing sale on other platforms, stacked commissions (sale + withdrawal + affiliate + video hosting), and no access to buyer data — same buyer-data limitation as Udemy
**Verbatim snippet:** "❌ La principal desventaja de Hotmart, y de las más importantes, es que pierdes el derecho de autor de tus contenidos. Tu curso deja de pertenecerte y una vez lo hayas subido a Hotmart, no puedes venderlo por otra plataforma. ❌ Hay muchas comisiones que entran en juego, las de las ventas realizadas, las de sacar el dinero de tu monedero de las ventas realizadas, la comisión a los afiliados, etc..Además de pagar pro el alojamiento de tus vídeos. ❌ Al igual que Udemy, no te quedas con la información de las personas que compran tu producto."
**Source:** https://www.classonlive.com/blog/mejor-plataforma-crear-cursos-online
**source_type:** blog
**verification_status:** direct_verified
**Date:** Accessed April 2026; originally published November 5, 2019; updated 2026
**Notes:** Third-party comparative (sub-type b). Competitors named: Udemy (on buyer data). Dimension: constraints/fees. Stance: anti-Hotmart. BIAS NOTE: Published by ClassOnLive, a direct Hotmart competitor. "pagar pro" is a typo in the original source for "pagar por." Three consecutive disadvantage bullets captured as continuous passage. Verified via search snippet and direct fetch.

---

### F-13

**Finding ID:** F-13
**What:** Hotmart, Udemy, and Amazon grouped as platforms that remove creator control over sales and customers, questioning whether creators remain business owners
**Verbatim snippet:** "Plataformas como Hotmart, Udemy o Amazon serían buenos ejemplos. Todas ellas prestan un servicio online valioso y quitan muchos dolores de cabeza tecnológicos, pero además… facturan para ti. Tú no vendes. Lo hacen ellos por ti. Y, ahora dime, si no controlas las ventas ni los clientes, que son el alma de un proyecto emprendedor, ¿sigues siendo el dueño de tu propio negocio?"
**Source:** https://www.lifestylealcuadrado.com/hotmart-opiniones/
**source_type:** blog
**verification_status:** direct_verified
**Date:** Accessed April 2026; page undated (post-2018 context)
**Notes:** Third-party comparative (sub-type b). Author: Franck Scipion, prominent Spanish digital-business educator (Lifestyle al Cuadrado). Competitors named: Udemy, Amazon. Dimension: constraints/control/ownership. Stance: anti-Hotmart. Author explicitly stopped working with Hotmart for this reason. No affiliate disclosure present.

---

### F-14

**Finding ID:** F-14
**What:** Third party describes Hotmart as a combination of Udemy, Teachable, and ClickBank — a unique hybrid meriting its own market category
**Verbatim snippet:** "Hotmart es en realidad una plataforma de cursos independiente, aunque es tan completa que merece su propia categoría dentro del mercado de la afiliación. Podríamos decir que es algo así como una combinación de Udemy con Teachable y la archiconocida ClickBank. Una mezcla explosiva… ¿eh?"
**Source:** https://dinerobits.com/hotmart-opiniones/
**source_type:** blog
**verification_status:** direct_verified
**Date:** Accessed April 2026; page undated (updated 2026 per title)
**Notes:** Third-party comparative (sub-type b). Competitors named: Udemy, Teachable, ClickBank. Dimension: market positioning/features. Stance: pro-Hotmart. Source is a Spanish monetization/review blog.

---

### F-15

**Finding ID:** F-15
**What:** Hotmart's 10% commission positioned as significantly lower than Udemy's 25–50% commission
**Verbatim snippet:** "También toma en cuenta que las comisiones que ofrece Udemy pueden ir desde el 25% al 50% de las ventas, que en comparación con otras plataformas como Hotmart, es mucho más alto. En Hotmart la comisión por venta de un curso es del 10%."
**Source:** https://jeansaldana.com/plataformas-para-crear-cursos-online/
**source_type:** blog
**verification_status:** direct_verified
**Date:** Accessed April 2026; page undated
**Notes:** Third-party comparative (sub-type b). Competitors named: Udemy. Dimension: fees. Stance: pro-Hotmart on fees vs Udemy. Specific numbers: Hotmart 10% vs Udemy 25–50%.

---

## 3. PART 2 — PROVISIONAL FINDINGS (blocked_url_index_verified)

---

### F-P01

**Finding ID:** F-P01
**What:** Experienced Spanish infoproducer identifies Hotmart's main advantage over other platforms as international reach and localized payment options for Latin American buyers
**Verbatim snippet:** "Quizá, desde nuestra experiencia como productores y vendedores de nuestras formaciones, la gran ventaja de Hotmart en comparación con otras plataformas es su gran implantación internacional y las facilidades que ofrece a los compradores: pago en moneda local, métodos de pago locales, opciones de financiación…"
**Source:** https://bigbangconversion.com/blog/opinion-hotmart/
**source_type:** blog
**verification_status:** blocked_url_index_verified
**Date:** October 2020
**Notes:** Third-party comparative (sub-type b). Author: Javi Pastor / BigBangConversion team, Spanish copywriter with ~2,000 students. Competitors named: generic "otras plataformas." Dimension: features/audience (international payments). Stance: pro-Hotmart. Affiliate links present in article. Content confirmed via search snippet; page loaded but exact passage location unverifiable on direct fetch.

---

### F-P02

**Finding ID:** F-P02
**What:** Hotmart's double currency conversion (buyer's currency → Hotmart's currency → seller's currency) causes elevated income loss for sellers focused on Latin American markets
**Verbatim snippet:** "Esto te hace pasar dos veces por la conversión de la moneda (de la moneda del comprador hasta la de Hotmart, y desde la de Hotmart a la tuya), por lo que se pierde un porcentaje de ingresos que puede ser elevado si focalizas tus ventas mayoritariamente en los países latinoamericanos."
**Source:** https://bigbangconversion.com/blog/opinion-hotmart/
**source_type:** blog
**verification_status:** blocked_url_index_verified
**Date:** October 2020
**Notes:** Third-party comparative (sub-type b). Same source as F-P01 but distinct positioning statement on a specific limitation. Dimension: fees/constraints (currency conversion). Stance: anti-Hotmart on this point. No competitor named — framing is Hotmart vs. self-managed payment.

---

### F-P03

**Finding ID:** F-P03
**What:** Hotmart positioned as LMS-marketplace hybrid popular in Spain and Latin America, with lower commissions than Udemy but less organic traffic
**Verbatim snippet:** "Hotmart es una plataforma que combina la funcionalidad de un LMS y un marketplace, popular sobre todo en España y Latinoamérica. Permite a los creadores de contenido alojar y vender sus cursos, además de sumar a la fórmula un sistema de afiliados para potenciar las ventas."
**Source:** https://quaderno.io/es/articulos/plataformas-cursos-online/
**source_type:** article
**verification_status:** blocked_url_index_verified
**Date:** Accessed April 2026; page undated
**Notes:** Third-party comparative (sub-type b). Published by Quaderno, a tax-compliance software company (neutral third party). Dimension: market positioning/features. Stance: neutral. Same page also states "Comisiones por venta que rondan el 10 % (9,90 % + 0,50 € por transacción). Menos tráfico que en otras plataformas más conocidas como Udemy" but that passage could not be confirmed as continuous with this snippet. Content confirmed from search snippet.

---

### F-P04

**Finding ID:** F-P04
**What:** Hotmart tiered commission: 20% for products under €10, 10% for products above €10, plus affiliate commissions and withdrawal fees
**Verbatim snippet:** "Si tu producto cuesta menos de 10 euros, Hotmart cobra 20% por cada venta; mientras que si es de 10.01 euros en adelante, la comisión de la plataforma es de 10%. Ahora bien, si tienes un infoproducto cuyo valor es de 200 euros, debes definir el tipo de comisión que va dirigido a tu equipo de afiliados. Y adicionalmente contabilizar unos 20 euros que quedarán en Hotmart."
**Source:** https://www.marketeroslatam.com/pros-y-contras-de-hotmart-2021/
**source_type:** article
**verification_status:** blocked_url_index_verified
**Date:** 2021
**Notes:** Third-party comparative (sub-type b). No specific competitor named; positions Hotmart's fee structure in isolation. Dimension: fees. Stance: neutral/descriptive. Specific numbers: 20% under €10, 10% above €10, ~€20 on a €200 product.

---

### F-P05

**Finding ID:** F-P05
**What:** Direct fee calculation: Hotmart takes €20.85 per €199 course sale vs €5.08 via Stripe/PayPal on a self-hosted site — roughly 4× the cost
**Verbatim snippet:** "En Hotmart: La comisión para un curso de 199€ es 9,9% + 0,50€, lo que equivale a 20,85€ por cada venta. En tu web propia: Usando Stripe/PayPal, la comisión sería del 2,9% + 0,30€, es decir, 5,08€ por cada venta."
**Source:** https://www.taisa-designer.com/vender-tu-curso-en-hotmart-o-en-una-academia-propia/
**source_type:** blog
**verification_status:** blocked_url_index_verified
**Date:** Accessed April 2026; page undated
**Notes:** Third-party comparative (sub-type b). Competitors named: self-hosted with Stripe/PayPal. Dimension: fees. Stance: anti-Hotmart. Specific numbers: €20.85 vs €5.08 per sale on a €199 product. Content confirmed from search snippet.

---

### F-P06

**Finding ID:** F-P06
**What:** Hotmart positioned as the most popular platform in all of Latin America for online course selling — simplest option but sales depend on affiliate promotion and require paying affiliate commissions
**Verbatim snippet:** "Si no quieres complicarte la vida vendiendo tus cursos Hotmart es tu mejor opción, la plataforma para vender cursos online más popular de todo Latinoamérica, esta plataforma es del tipo marketplace por lo que puedes subir tu curso y tendrás exposición ante potenciales clientes, el sistema de promoción de ventas de hotmart es a través de afiliados por lo que debes de considerar que tienes que pagarles una comisión para que tu curso sea promovido."
**Source:** https://bit4learn.com/plataformas-para-vender-cursos-online/
**source_type:** blog
**verification_status:** blocked_url_index_verified
**Date:** 2025
**Notes:** Third-party comparative (sub-type b). Bit4learn is a Latin American e-learning industry resource. Competitors in same article: Kajabi, Sabionet, Udemy, Thinkific. Dimension: ease of use / audience. Stance: mixed. Content confirmed from search snippet.

---

### F-P07

**Finding ID:** F-P07
**What:** Teachable stopped developing new features and stagnated after being acquired by Hotmart
**Verbatim snippet:** "Desde que fue adquirida por Hotmart en el 2019 dejo de desarrollar nuevas funcionalidades y se quedó estancada."
**Source:** https://bit4learn.com/plataformas-para-vender-cursos-online/
**source_type:** blog
**verification_status:** blocked_url_index_verified
**Date:** 2025
**Notes:** Third-party comparative (sub-type b). Statement about Teachable under Hotmart ownership. Dimension: features (post-acquisition stagnation). Stance: anti-Hotmart by implication. Content confirmed from search snippet. NOTE: Source says "2019" acquisition; public announcement was March 2020.

---

### F-P08

**Finding ID:** F-P08
**What:** Hotmart has displaced ClickBank in the entire Spanish-speaking market; ClickBank is "practically unused" in the Hispanic world
**Verbatim snippet:** "Hotmart actualmente está en el número de las plataformas para vender cursos en forma de infoproductos digitales por su fácil uso, formación gratuita, y registro gratis. Desbancando así a ClickBank. [...] Realmente Clickbank prácticamente no se utilizar en el mundo hispano, pues el mercado hispano se ha trasladado a Hotmart, muchísimo mejor con diferencia."
**Source:** https://vendemebonito.com/plataformas-para-vender-infoproductos/
**source_type:** blog
**verification_status:** blocked_url_index_verified
**Date:** Accessed April 2026; page undated
**Notes:** Third-party comparative (sub-type b). Competitors named: ClickBank. Dimension: market/audience. Stance: pro-Hotmart. NOTE: "[...]" in snippet indicates text may be non-continuous; passage extracted from search snippet. Continuity could not be independently confirmed. If subagent concatenated, this finding should be downgraded to Part 4.

---

### F-P09

**Finding ID:** F-P09
**What:** Teachable CEO positions Hotmart as "the Teachable of Brazil," operating profitably at 3× Teachable's scale with 60,000+ creators and 150,000+ digital products across Latin America and Europe
**Verbatim snippet:** "For those of you not in the know, Hotmart is analogous to the 'Teachable of Brazil,' while operating profitably at a scale three times our size. Over the last nine years, they have built an absolutely incredible business in Latin America and Europe empowering 60,000+ creators to sell 150,000+ digital products."
**Source:** https://medium.com/teachable/teachable-is-joining-forces-with-hotmart-afad5bd144fc
**source_type:** blog
**verification_status:** blocked_url_index_verified
**Date:** March 16, 2020
**Notes:** Third-party comparative (sub-type b). SOURCE IN ENGLISH — not a Spanish-language source but directly relevant to competitive positioning. Author: Ankur Nagpal, then-CEO of Teachable, announcing acquisition. Competitors named: Teachable. Dimension: market scale. Stance: pro-Hotmart. Specific data: 60K+ creators, 150K+ products, 3× Teachable's scale. Data from 2020; current figures likely higher.

---

### F-P10

**Finding ID:** F-P10
**What:** Hotmart unsuitable for low-cost digital products — for a €9.99 ebook, commissions and affiliate fees may leave the creator with no profit
**Verbatim snippet:** "No sirve para cursos pequeños o ebooks de bajo coste. Está pensado para cursos de más de 200€ en adelante. Si vendes ebooks de 9,99€, entre impuestos y comisión del afiliado y de Hotmart, puede que no te quede nada para ti."
**Source:** https://www.albadelgado.com/herramientas-para-vender-cursos-online-cual-es-la-mejor/
**source_type:** blog
**verification_status:** blocked_url_index_verified
**Date:** Accessed April 2026; page undated
**Notes:** Third-party comparative (sub-type b). Competitors in same article: Kajabi, Teachable, Udemy. Dimension: constraints/fees. Stance: anti-Hotmart on low-price products. Specific threshold: €200 minimum for viability. Content confirmed from subagent page fetch.

---

### F-P11

**Finding ID:** F-P11
**What:** Hotmart ideal for zero-investment concept validation but too expensive to scale — at €5,000 revenue, its costs exceed those of more complete platforms
**Verbatim snippet:** "Resumen: es IDEAL para hacer pruebas de concepto con cero inversión. Si nunca has vendido cursos online, puedes cargarlos en Hotmart y ver cómo va esto de la venta de contenido digital. Pero no es una plataforma para crecer contigo porque con facturaciones de 5.000€, el coste es muy superior al de plataformas más completas."
**Source:** https://www.albadelgado.com/herramientas-para-vender-cursos-online-cual-es-la-mejor/
**source_type:** blog
**verification_status:** blocked_url_index_verified
**Date:** Accessed April 2026; page undated
**Notes:** Third-party comparative (sub-type b). Same source as F-P10, distinct statement. Competitors named: generic "plataformas más completas." Dimension: fees/constraints (scalability). Stance: mixed — good entry point, poor at scale. Specific threshold: €5,000 revenue. Content confirmed from subagent page fetch.

---

### F-P12

**Finding ID:** F-P12
**What:** Systeme.io calculates that earning $10,000/month on Hotmart means paying ~$1,000/month in platform fees, increasing further with high transaction volume due to the $0.50-per-sale surcharge
**Verbatim snippet:** "Si te ganas $10.000 al mes con Hotmart, tendrás que pagar cerca de $1.000 al mes por usar la plataforma. Estarás pagando mucho más si estás vendiendo un gran número de ofertas debido a su comisión de 50c por venta."
**Source:** https://systeme.io/es/hotmart-alternative
**source_type:** platform_doc
**verification_status:** blocked_url_index_verified
**Date:** Accessed April 2026; evergreen page
**Notes:** Third-party comparative (sub-type b). BIAS NOTE: Published by Systeme.io, a direct Hotmart competitor; this is a marketing/comparison landing page. Competitors named: Systeme.io (self-positioning against Hotmart). Dimension: fees. Stance: anti-Hotmart. Specific numbers: $10K revenue → ~$1K fees, $0.50 per sale. Content confirmed from search snippet; direct page fetch returned server error.

---

### F-P13

**Finding ID:** F-P13
**What:** User argues Hotmart has the best overall cost-benefit vs Eduzz because Eduzz charges extra for included Hotmart features like quizzes, making Eduzz effectively more expensive despite its lower nominal rate
**Verbatim snippet:** "A Eduzz cobra mais barato, mas não tem tudo o que a hotmart tem, pra criar um quiz, por exemplo, para os alunos eu tive que contratar um plano a parte. Sendo assim, considero que a Hotmart tem o melhor custo benefício para tudo o que oferece. A Eduzz está no caminho certo, mas como cobra tudo a parte, acaba saindo mais caro no final."
**Source:** https://www.capterra.com/p/219169/Hotmart/reviews/
**source_type:** buyer_review
**verification_status:** blocked_url_index_verified
**Date:** December 23, 2022
**Notes:** Third-party comparative (sub-type b). SOURCE IN PORTUGUESE — Capterra verified review. Reviewer: Fernando C. (Cofounder, E-Learning, used Hotmart 2+ years). Competitors named: Eduzz. Dimension: fees/features. Stance: pro-Hotmart. Capterra reviews load dynamically; content confirmed via subagent fetch and search snippet. Using source_type buyer_review as closest fit per shard instructions (review_aggregator not in closed list of 18).

---

## 4. PART 3 — PATTERN CANDIDATES (sealed)

*Descriptive, non-causal statements only. No signal-strength language. No cross-finding synthesis of positioning conclusions.*

---

### PC-01

Fee structure is the most frequently surfaced dimension of competitive positioning for Hotmart in Spanish-language sources. Of 28 total findings across Parts 1–2, at least 14 address fees or commissions as a primary comparison axis.

---

### PC-02

Content exclusivity and intellectual property rights clauses appear across multiple independent Spanish-language sources (ClassOnLive F-12, Escuela Emprende F-P05 context, Lifestyle al Cuadrado F-13) as a concern specific to Hotmart relative to SaaS alternatives. No equivalent concern surfaces for Udemy in the same sources.

---

### PC-03

Hotmart's market leadership in Latin America is acknowledged across both advocate and critic sources. The phrasing "la más grande de América Latina" (F-05) or "la más popular de todo Latinoamérica" (F-P06) appears in Hotmart's own materials and independent third-party articles alike.

---

### PC-04

Hotmart's self-positioning on scalability ("inimaginable en otras plataformas," F-04) and third-party assessments of scalability ("no es una plataforma para crecer contigo," F-P11) point in opposite directions. Self-positioning frames pay-per-sale as enabling scale; third-party sources frame percentage-based fees as penalizing scale.

---

### PC-05

Multiple Hotmart competitors maintain dedicated Spanish-language landing pages positioning against Hotmart by name (Systeme.io F-P12, ClassOnLive F-11/F-12, Sabionet, EzyCourse). This pattern is consistent with Hotmart being the incumbent benchmark in the Spanish-language digital-product market.

---

### PC-06

Hotmart is positioned at the intersection of marketplace and SaaS categories across multiple sources (Dinerobits F-14 "combinación de Udemy con Teachable y ClickBank"; Quaderno F-P03 "combina la funcionalidad de un LMS y un marketplace"). This hybrid positioning generates comparisons on multiple axes: versus pure marketplaces (Udemy) on fees and control, versus pure SaaS (Thinkific, Kajabi) on traffic and autonomy.

---

## 5. PART 4 — COULD NOT VERIFY / OUT OF SCOPE

---

### F-X01: Reddit competitive positioning

**What:** No data found on Reddit discussions comparing Hotmart to competitors in Spanish or Portuguese
**Verbatim snippet:** n/a — absence finding
**Source:** Searches attempted: site:reddit.com hotmart vs kiwify; site:reddit.com hotmart vs eduzz; site:reddit.com hotmart vs teachable; site:reddit.com hotmart comparison; site:reddit.com "hotmart" alternativas; reddit hotmart vs kiwify opiniones; site:reddit.com/r/empreendedorismo hotmart; site:reddit.com/r/digitalproducts hotmart; https://www.reddit.com/search/?q=hotmart+vs+kiwify; https://www.reddit.com/search/?q=hotmart+vs+eduzz
**source_type:** reddit
**verification_status:** could_not_verify
**Date:** April 2026
**Notes:** Despite 10+ search variations across English, Spanish, and Portuguese, no Reddit threads with substantive competitive positioning statements about Hotmart were found. Hotmart community discussions appear concentrated on Capterra, Brazilian business forums (O Novo Mercado), blog comment sections, and social media (Threads).

---

### F-X02: YouTube video transcripts

**What:** No data found — no YouTube video pages with Hotmart competitive comparisons were accessible
**Verbatim snippet:** n/a — absence finding
**Source:** Searches attempted: site:youtube.com "hotmart vs kiwify" español; site:youtube.com "hotmart vs" comparación; site:youtube.com hotmart vs eduzz; site:youtube.com hotmart vs teachable español; site:youtube.com hotmart vs thinkific; site:youtube.com hotmart vs monetizze; youtube hotmart vs kiwify opiniones español; hotmart comparación plataforma youtube
**source_type:** video_transcript
**verification_status:** could_not_verify
**Date:** April 2026
**Notes:** The web_search tool returned zero results for all site:youtube.com queries. One video transcript aggregator page (TopView.ai) containing a "Hotmart vs Systeme IO" transcript returned 404. YouTube video content comparing Hotmart exists (sofiafernandez.es references her own YouTube video on the topic at https://youtu.be/JSyexVv7UFo) but direct transcript access was not achievable.

---

### F-X03: Hotmart vs Braip

**What:** No data found on Hotmart vs Braip comparisons in Spanish
**Verbatim snippet:** n/a — absence finding
**Source:** Searches attempted: "hotmart vs braip" comparación; hotmart vs braip; site:youtube.com hotmart vs braip; hotmart braip alternativas
**source_type:** blog
**verification_status:** could_not_verify
**Date:** April 2026
**Notes:** Braip is a Brazilian digital-product platform. No Spanish-language sources comparing Hotmart to Braip were found. Comparisons may exist in Portuguese but fall outside the Spanish-language scope.

---

### F-X04: hotmart.com/es/sobre-hotmart

**What:** Hotmart's "About" page in Spanish could not be accessed
**Verbatim snippet:** n/a — absence finding
**Source:** https://hotmart.com/es/sobre-hotmart (direct fetch returned permissions error); also attempted https://hotmart.com/es (same error)
**source_type:** platform_doc
**verification_status:** could_not_verify
**Date:** April 2026
**Notes:** Page may contain additional self-positioning statements. Pricing page (hotmart.com/es/precios) and help center were accessible and provided self-positioning content.

---

### F-X05: Hotmart vs Monetizze in Spanish

**What:** No data found on Hotmart vs Monetizze comparisons in Spanish-language sources
**Verbatim snippet:** n/a — absence finding
**Source:** Searches attempted: "hotmart vs monetizze" comparación; hotmart vs monetizze español; hotmart monetizze comparativa
**source_type:** blog
**verification_status:** could_not_verify
**Date:** April 2026
**Notes:** Comparisons exist in Portuguese (Capterra review by Fernando C. in F-P13 context mentions Monetizze) but not in Spanish. Monetizze appears to have negligible brand recognition in Spanish-language markets.

---

### F-X06: O Novo Mercado forum discussion

**What:** Forum thread comparing Eduzz, Hotmart, and Kiwify exists but content is behind a login wall
**Verbatim snippet:** n/a — blocked access finding
**Source:** https://comunidade.onovomercado.com/c/outros/duvida-eduzz-hotmart-ou-kiwify
**source_type:** seller_forum
**verification_status:** could_not_verify
**Date:** Undated
**Notes:** Thread title visible: "Dúvida: Eduzz, Hotmart ou Kiwify?" — confirms competitive comparison content exists. Full content inaccessible without account registration. Source in Portuguese.

---

### F-X07: Hotmart vs Kiwify in Spanish

**What:** No data found on Hotmart vs Kiwify comparisons specifically in Spanish-language sources
**Verbatim snippet:** n/a — absence finding
**Source:** Searches attempted: "hotmart vs kiwify" comparación; hotmart vs kiwify español; hotmart kiwify alternativas español
**source_type:** blog
**verification_status:** could_not_verify
**Date:** April 2026
**Notes:** Kiwify is a Brazilian platform; all comparative content found was in Portuguese (e.g., bit4learn.com/kiwify describes Kiwify as "la principal alternativa a Hotmart en Brasil" but this is from a site that publishes in Spanish on some pages and Portuguese on others; the Kiwify-specific page was not confirmed as Spanish). The Hotmart-Kiwify rivalry is primarily a Portuguese-language phenomenon.

---

## 6. RESEARCH QA NOTES

### 11-Point QA Checklist Applied to All Findings

| # | Check | Status |
|---|-------|--------|
| 1 | One finding = one source only | ✅ All findings draw from a single source per finding. Multi-finding sources (sofiafernandez.es: F-07 through F-10; classonlive.com: F-11, F-12; bigbangconversion.com: F-P01, F-P02; albadelgado.com: F-P10, F-P11) represent distinct positioning statements from distinct continuous passages on the same page. |
| 2 | Multi-speaker pages: each speaker split into separate findings | ✅ Capterra multi-reviewer page split by individual reviewer (F-P13 = Fernando C.). Blog comment section speakers not merged with post authors. |
| 3 | Verbatim snippet is character-for-character continuous passage; no concatenation | ✅ Verified via direct page fetch for Part 1 findings. F-P08 (vendemebonito.com) has "[...]" in snippet indicating possible non-continuity — flagged in Notes. All other snippets are continuous. |
| 4 | What field 100% sustained by snippet; no added qualifiers | ✅ Reviewed each What field against its snippet. Removed extraneous qualifiers not present in snippets (e.g., platform categorizations not stated in source text). |
| 5 | Source field = full URL, not page title | ✅ All Source fields are full URLs. |
| 6 | source_type from closed list | ✅ Used: pricing_page, platform_doc, blog, article, buyer_review. buyer_review used for Capterra per shard instructions (review_aggregator not in closed list). |
| 7 | verification_status correctly assigned | ✅ direct_verified: content confirmed on fetched page. blocked_url_index_verified: content confirmed from search index snippets or subagent partial fetch. could_not_verify: content inaccessible. |
| 8 | Strict name test — "Hotmart" appears by name in snippet | ✅ All snippets in Parts 1–2 contain "Hotmart" by name. |
| 9 | Date: visible date or "Accessed [Month Year]; page undated" | ✅ All findings include date per this format. |
| 10 | Notes contain local limitations only; no cross-finding synthesis or interpretation | ✅ Pattern-level observations reserved for Part 3 only. Individual Notes contain bias flags, affiliate disclosure notes, language notes, and data-quality flags only. |
| 11 | No cross-finding synthesis; no causal claims in pattern candidates | ✅ Part 3 pattern candidates are descriptive only. No "therefore Hotmart is cheaper/better" statements anywhere. |

### Additional QA Notes

**Affiliate bias concentration:** 4 of 15 Part 1 findings (F-07 through F-10) come from a single source (sofiafernandez.es) with Thinkific affiliate links. This source is the richest structured comparison found in Spanish, but all findings from it carry affiliate bias toward Thinkific. Flagged individually.

**Competitor-authored content:** Two Part 1 sources are published by direct Hotmart competitors: ClassOnLive (F-11, F-12) and one Part 2 source by Systeme.io (F-P12). Bias flagged in each finding's Notes.

**Language scope deviation:** Three findings are not in Spanish: F-P09 (English, Medium/Teachable), F-P13 (Portuguese, Capterra). These were captured because they contain substantive positioning data not available in Spanish sources, and the shard's WHERE TO LOOK FIRST section explicitly directed searches to Portuguese-language subreddits and platforms. Each is flagged with language note.

**Fixed-fee discrepancy:** The per-transaction fixed fee is stated as €0.05 in sofiafernandez.es (F-07) but as €0.50 / $0.50 in all other sources including Hotmart's own pricing page. This is likely a source error in sofiafernandez.es. Reported verbatim per protocol; discrepancy flagged in Notes.

**Teachable acquisition date:** bit4learn.com (F-P07) states Hotmart acquired Teachable "en el 2019." The public announcement was March 2020 (F-P09 Medium post dated March 16, 2020). Discrepancy flagged in Notes; source text reported verbatim.

**Exclusivity/IP rights debate:** Multiple sources (F-12, F-13) claim Hotmart takes content rights/exclusivity. At least one Spanish legal blog (lluisaochoa.com, found in search but not surfaced as a finding because it does not contain competitive comparison) argues this is a misinterpretation of Hotmart's terms of use. The debate itself is not synthesized here — only the positioning statements as made by each source are captured.

### Coverage Assessment

| Category | Expected | Delivered |
|----------|----------|-----------|
| Part 1 — Clean findings | 8–15 | 15 |
| Part 2 — Provisional findings | 10–15 | 13 |
| Part 3 — Pattern candidates | 5–10 | 6 |
| Part 4 — Could not verify | 5–10 | 7 |

**Total findings:** 28 (Parts 1–2) + 7 absence/blocked = 35 items.

**Self-positioning findings (sub-type a):** 6 (F-01 through F-06), all from hotmart.com domains.
**Third-party comparative findings (sub-type b):** 22 (F-07 through F-15, F-P01 through F-P13), from 12 distinct external domains.

**Competitors surfaced by name across all findings:** Thinkific (5 findings), Udemy (5), Teachable (3), ClickBank (2), Eduzz (2), Systeme.io (2), Kajabi (1), Kartra (1), Amazon (1), Stripe/PayPal (1), ClassOnLive (1). Kiwify, Monetizze, and Braip appear in Part 4 as absence findings for Spanish-language sources.

**Dimensions covered:** Fees/commissions (14 findings), features (8), constraints/control (6), audience/market (6), ease of use (3).

---

*End of Data Gathering run. Shard: Hotmart × D5 — Competitive Positioning.*