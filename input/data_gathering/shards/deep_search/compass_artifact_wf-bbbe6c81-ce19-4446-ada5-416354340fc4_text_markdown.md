# Hotmart × D4 (Buyer Behavior) — Data Gathering Run

**Shard:** Hotmart × D4 (Buyer behavior)
**Direction:** Capture what buyers do in and around Hotmart — how they find products, purchase experience reports, observable behavioral patterns. Buyer voice and buyer activity only.
**Language:** Spanish / Portuguese (original language preserved)
**Time window:** April 2025 — April 2026
**Executed:** April 14, 2026

---

## Search Decomposition

**SD-01:** Reclameaqui individual buyer complaints — `site:reclameaqui.com.br hotmart compra reembolso` — Portuguese buyer voice on Brazil's primary consumer complaint platform.

**SD-02:** Trustpilot buyer reviews (English) — `site:trustpilot.com hotmart buyer review` + direct fetch of `trustpilot.com/review/hotmart.com` — English-language buyer reviews on global review platform.

**SD-03:** Trustpilot buyer reviews (Spanish) — `site:es.trustpilot.com hotmart compré` + direct fetch of `es.trustpilot.com/review/hotmart.com` pages 2, 9 — Spanish-language buyer reviews.

**SD-04:** Reddit buyer experience reports — `site:reddit.com hotmart compré experiencia`, `site:reddit.com hotmart bought course review`, `site:reddit.com hotmart estafa comprador`, `reddit hotmart comprei curso` — buyer posts across subreddits (r/hotmart, r/desabafos, r/brasil).

**SD-05:** YouTube buyer opinion videos — `youtube hotmart opinión comprador experiencia`, `youtube hotmart compré curso reseña`, `youtube hotmart vale la pena comprar` — Spanish/Portuguese buyer review videos.

**SD-06:** Hotmart traffic and engagement analytics — `hotmart.com similarweb traffic 2025`, `hotmart traffic analytics 2025` + direct fetch of `similarweb.com/website/hotmart.com/` — third-party analytics on visitor behavior (SimilarWeb, Semrush).

**SD-07:** Hotmart aggregate buyer data — `hotmart buyer behavior report`, `hotmart conversion rate data`, `hotmart cart abandonment rate`, `hotmart número de compradores 2025`, `hotmart dados compradores relatório` — platform-published or analyst-published buyer statistics.

**SD-08:** Spanish-language buyer experience articles/blogs — `Hotmart compré experiencia`, `Hotmart estafa comprador`, `Hotmart reembolso comprador experiencia`, `Hotmart opinión curso compré`, `Hotmart es seguro comprar cursos` — buyer voice in blogs, forums, articles.

**SD-09:** Hotmart buyer discovery channels — `hotmart how buyers discover products`, `hotmart TikTok buyers`, `hotmart afiliado descubrí` — how buyers report finding Hotmart products.

**SD-10:** Buyer comparisons Hotmart vs. other platforms — `comprar en Hotmart vs Udemy experiencia`, `Hotmart o Domestika comprador` — buyer-voice comparisons of purchase experience across platforms.

---

## Part 1 — Clean Findings (direct_verified)

---

**F-01**
**What:** Buyer in Argentina could not download an e-book purchased on the platform; received no support response. Reports previous purchases on the platform went well.
**Verbatim snippet:** "No pude bajar un e book que compre en la plataforma y no me respondieron aún. Compre en otras ocasiones y fue todo bien pero en esta compra al contrario."
**Source:** https://es.trustpilot.com/review/hotmart.com?page=9
**source_type:** buyer_review
**verification_status:** direct_verified
**Date:** 24 Mar 2026 (experience dated 16 Mar 2026)
**Notes:** Page directly fetched. Verified Trustpilot review. Speaker: Susana. Location: AR. Product type: e-book. Outcome: product not delivered, no support. Buyer tenure: repeat buyer (previous purchases successful).

---

**F-02**
**What:** Buyer in Colombia did not receive last product purchased (anatomy product); sent multiple emails with no resolution or refund.
**Verbatim snippet:** "No llegó el último producto, es de anatomía, envié varios correos y nadie dio solución, y tampoco devolución del dinero."
**Source:** https://es.trustpilot.com/review/hotmart.com?page=9
**source_type:** buyer_review
**verification_status:** direct_verified
**Date:** 24 Mar 2026 (experience dated 16 Mar 2026)
**Notes:** Page directly fetched. Verified Trustpilot review. Speaker: Nidya. Location: CO. Product type: anatomy material. Outcome: product not delivered, no refund.

---

**F-03**
**What:** Buyer in Spain was sold a high-ticket course she found mediocre; cancelled on second day and received full refund within approximately 10 days.
**Verbatim snippet:** "Me quisieron vender un curso de alto ticket, siendo mediocre. Al segundo día lo cancelé. Un gran ayuda su respuesta e inmediatez de devolución de mi dinero en cuestión de unos 10 dias."
**Source:** https://es.trustpilot.com/review/hotmart.com?page=9
**source_type:** buyer_review
**verification_status:** direct_verified
**Date:** 23 Mar 2026 (experience dated 12 Mar 2026)
**Notes:** Page directly fetched. Verified Trustpilot review. Speaker: Maria. Location: ES. Product type: high-ticket course. Outcome: refund in ~10 days. 5-star review.

---

**F-04**
**What:** Repeat buyer in Mexico over several years reports that Hotmart always honored refunds when products did not meet expectations and cancellation was requested within the guarantee period.
**Verbatim snippet:** "A lo largo de algunos años, he adquirido diferentes productos y servicios a través de hotmart y siempre he sentido la tranquilidad de que hotmart me respalda si por alguna razón el producto no es lo que esperaba y si cancelo en tiempo y forma, siempre he obtenido la devolución de mi dinero."
**Source:** https://es.trustpilot.com/review/hotmart.com?page=2
**source_type:** buyer_review
**verification_status:** direct_verified
**Date:** ~9 Apr 2026 (experience dated 13 Mar 2026)
**Notes:** Page directly fetched. Verified Trustpilot review. Speaker: mario. Location: MX. Product type: multiple products and services. Outcome: refunds always obtained. Buyer tenure: multi-year. 5-star review.

---

**F-05**
**What:** Buyer in Colombia reports no refund and no response to petition for purchased products. Hotmart response confirms 3 product transactions.
**Verbatim snippet:** "Ni devolución, de mi dinero, ni respuesta de mi petición"
**Source:** https://es.trustpilot.com/review/hotmart.com?page=2
**source_type:** buyer_review
**verification_status:** direct_verified
**Date:** ~10 Apr 2026 (experience dated 12 Mar 2026)
**Notes:** Page directly fetched. Verified Trustpilot review. Speaker: Gustavo. Location: CO. 3 transactions confirmed by Hotmart reply (HP1774165903, HP1750696220, HP1759160696). Outcome: no refund, no response. 1-star review. Title: "Estafado."

---

**F-06**
**What:** Buyer purchased a program on Facebook for $37 claiming they could make money rating YouTube videos; was subsequently billed $46, $97, and $67 for gardening content.
**Verbatim snippet:** "I purchased a program on Facebook. They claimed that I could make money rating videos on YouTube. I paid them $37 . They ended up billing me for $46 , $97, and $67 dollars for some sort of gardening c..."
**Source:** https://www.trustpilot.com/review/hotmart.com
**source_type:** buyer_review
**verification_status:** direct_verified
**Date:** 22 Dec 2025
**Notes:** Page directly fetched. Speaker: Crystal Boyd. Truncated at "c..." — Trustpilot listing page display truncation, not editorial. Discovery channel: Facebook ad. Prices: $37 + $46 + $97 + $67 USD. Product type: "make money rating YouTube videos" program. 2-star review.

---

**F-07**
**What:** Buyer ordered a digital course from a creator via Hotmart; course was empty upon access. Requested refund same day; bot processed it. Refund showed pending but was not completed.
**Verbatim snippet:** "Ordered digital course from creator via Hotmart platform. When accessing the course it was empty. Asked for a refund same day. Which the bot processed straight away. Refund showed pending on my accoun..."
**Source:** https://www.trustpilot.com/review/hotmart.com
**source_type:** buyer_review
**verification_status:** direct_verified
**Date:** 9 Feb 2026
**Notes:** Page directly fetched. Speaker: Jaco van Dam. Truncated at "accoun..." — Trustpilot display truncation. Product type: digital course. Outcome: refund pending. 1-star review.

---

**F-08**
**What:** Buyer reports multiple positive purchase experiences acquiring digital products using credit card and other payment methods.
**Verbatim snippet:** "Hotmart is a great company, I've had awesome experiences every time I acquired digital products using credit card and other payment methods. Trustworthy!"
**Source:** https://www.trustpilot.com/review/hotmart.com
**source_type:** buyer_review
**verification_status:** direct_verified
**Date:** 31 Oct 2025
**Notes:** Page directly fetched. Speaker: Frederico Montezuma. Trustpilot-verified purchase. Product type: digital products (multiple). Payment: credit card + other methods. Outcome: positive. 5-star review.

---

**F-09**
**What:** Buyer ordered a qigong course; found additional charges for 3 other courses and a membership. Course was advertised in English but processed in Portuguese, making navigation impossible.
**Verbatim snippet:** "I ordered their qigong course and when I checked my account they has taken payment for 3 other courses and memebership. They advertise course in English then process it in Portuguese so its impossible..."
**Source:** https://www.trustpilot.com/review/hotmart.com
**source_type:** buyer_review
**verification_status:** direct_verified
**Date:** 20 Nov 2025
**Notes:** Page directly fetched. Speaker: martin forrest. Truncated at "impossible..." — Trustpilot display truncation. Product type: qigong course + 3 additional courses + membership (not ordered). Language barrier: English ad → Portuguese platform. 1-star review.

---

**F-10**
**What:** Buyer made initial US$27 payment via PayPal; received 2 additional non-authorized payments of US$67 and US$19.90. Digital product received had nothing to do with the Facebook ad.
**Verbatim snippet:** "An initial payment of US$ 27.00 was done by paypall, followed by 2 extra (non-autorized) payments of US$ 67.00 and US$ 19.90\nDigital product received had nothing to do with the add on Facebook. Tried..."
**Source:** https://www.trustpilot.com/review/hotmart.com
**source_type:** buyer_review
**verification_status:** direct_verified
**Date:** 21 Oct 2025
**Notes:** Page directly fetched. Speaker: Reinder. Truncated at "Tried..." — Trustpilot display truncation. Discovery channel: Facebook ad. Prices: US$27 + US$67 + US$19.90. Payment: PayPal. Outcome: product mismatch + unauthorized charges. 1-star review.

---

**F-11**
**What:** Buyer ordered something for under $3.00; by next day began receiving charges from $9.99 to $89.99. Got partial refund by showing PayPal evidence of contact attempts.
**Verbatim snippet:** "I ordered something for under $3.00 and by the next day I began receiving charges from $9.99 to $89.99. I was able to get a partial refund because I showed PayPal how many times I tried to contact th..."
**Source:** https://www.trustpilot.com/review/hotmart.com
**source_type:** buyer_review
**verification_status:** direct_verified
**Date:** 3 Dec 2025
**Notes:** Page directly fetched. Speaker: Christina Boyd George. Truncated — Trustpilot display truncation. Prices: under $3.00 initial → $9.99 to $89.99 subsequent. Payment: PayPal. Outcome: partial refund. 1-star review.

---

**F-12**
**What:** Buyer did not know the site was for eCourses; expected to make money on TikTok. Waiting for refund. States this is not what she signed up for.
**Verbatim snippet:** "I didn't know that this site was for some eCourses instead of making money on TikTok. I'm still Waiting on my refund. This isn't what I was signing up for. Now I have to wait to be able to buy groceri..."
**Source:** https://www.trustpilot.com/review/hotmart.com
**source_type:** buyer_review
**verification_status:** direct_verified
**Date:** 3 Nov 2025
**Notes:** Page directly fetched. Speaker: Gwendolyn "MzGigi" Woodall. Truncated at "groceri..." — Trustpilot display truncation. Discovery channel: TikTok-related marketing. Product expectation mismatch: expected TikTok income, received eCourses. Outcome: refund pending. 3-star review.

---

**F-13**
**What:** Digital product buyers on Hotmart in Latin America grew from 140,000 in 2018 to 4.13 million in 2022, representing 2.5% of the region's economically active population.
**Verbatim snippet:** "en cuatro años, los compradores de productos digitales en Hotmart crecieron casi 3 mil por ciento, al pasar de 140 mil en 2018 a 4.13 millones en 2022"
**Source:** https://dplnews.com/compradores-productos-digitales-crecen-300-hotmart/
**source_type:** article
**verification_status:** direct_verified
**Date:** 20 Mar 2024
**Notes:** Page directly fetched and verbatim confirmed. Data from Hotmart Insights 2023 study, presented by VP Pablo Mondragón. Scope: Latin America. Article predates April 2025–April 2026 time window; no newer aggregate buyer volume data found. Data period: 2018–2022.

---

**F-14**
**What:** Typical Hotmart digital product buyer is aged 40–59, has higher education or postgraduate degree, and income between $500 and $1,000 USD per month.
**Verbatim snippet:** "El perfil típico de los compradores de productos digitales oscila entre 40 y 59 años, con educación superior o posgrado y cuyos ingresos van de los 500 a los mil dólares."
**Source:** https://dplnews.com/compradores-productos-digitales-crecen-300-hotmart/
**source_type:** article
**verification_status:** direct_verified
**Date:** 20 Mar 2024
**Notes:** Page directly fetched and verbatim confirmed. Same source as F-13; distinct data point (demographics vs. volume). Data from Hotmart Insights 2023. Scope: LATAM buyers. Article predates time window. Top 5 purchase categories listed separately in same article: 1) Finance & Investments, 2) Marketing & Sales, 3) Career & Professional Development, 4) Health & Sports, 5) Teaching & Academic Study.

---

**F-15**
**What:** 78% of Hotmart purchases are via mobile devices, 20% on desktop computers, and 2% on tablets.
**Verbatim snippet:** "el 78 por ciento se realiza a través de dispositivos móviles, el 20 por ciento en computadoras y el 2 por ciento restante en tabletas"
**Source:** https://dplnews.com/compradores-productos-digitales-crecen-300-hotmart/
**source_type:** article
**verification_status:** direct_verified
**Date:** 20 Mar 2024
**Notes:** Page directly fetched and verbatim confirmed. Same source as F-13, F-14; distinct data point (device breakdown). Data from Hotmart Insights 2023. Scope: LATAM. Article predates time window.

---

**F-16**
**What:** Hotmart reported a 32 percentage point uplift in customer retention for recurring payments via Pix following the launch of Pix Automático on June 16, 2025. Hotmart is converting more than four times the number of recurring payments that previously failed with Pix into continued subscriptions. One in four new subscription buyers chose Pix Automático.
**Verbatim snippet:** "Hotmart revealed a 32 percentage point uplift in customer retention for recurring payments via Pix following the launch of Pix Automático."
**Source:** https://www.prnewswire.com/news-releases/ebanx-enables-pix-recurring-payments-for-hotmart-leading-to-a-32-point-retention-increase-302565939.html
**source_type:** report
**verification_status:** direct_verified
**Date:** 24 Sep 2025
**Notes:** Page directly fetched and verbatim confirmed. Joint Hotmart/EBANX press release. Presented by Allana Braga, Head of Payments at Hotmart, at EBANX Payments Summit. Data scope: Brazil, recurring Pix payments. Data period: June 16 – ~September 2025 (first ~3 months of Pix Automático). What field limited to facts in cited snippet; "4× conversion" and "1 in 4 subscribers" appear in other passages on same page.

---

**F-17**
**What:** Hotmart's autofill feature (Fast Buy) at checkout reduces buyer time at checkout, decreases cart abandonment, and can increase the final conversion rate by up to 7%.
**Verbatim snippet:** "By simplifying the purchasing process, autofill reduces the time the buyer spends at checkout, decreases cart abandonment, and can increase the final conversion rate by up to 7%."
**Source:** https://help.hotmart.com/en/article/36730202370701/how-can-the-autofill-feature-fast-buy-on-the-payment-page-help-my-sales-
**source_type:** platform_doc
**verification_status:** direct_verified
**Date:** Accessed April 2026; page undated
**Notes:** Page directly fetched and verbatim confirmed. Hotmart official Help Center documentation. Feature being rolled out across Brazil, Mexico, Colombia, Argentina, Chile, Peru, Bolivia, Ecuador. Missing time period for the 7% figure — "up to" qualifier suggests internal benchmark, no sample or period specified.

---

## Part 2 — Provisional Findings (blocked_url_index_verified)

---

**F-P01**
**What:** Buyer purchased a product on Hotmart described as not matching what was proposed. Immediately requested refund. Reports refund not processed; received a satisfaction survey instead. Product: FORMAÇÃO EM AROMATERAPIA CLÍNICA. Payment via PIX.
**Verbatim snippet:** "Fiz uma compra na Hortmart que não era o proposto. Imediatamente, pedi o reembolso do valor. Porém, até agora nada foi feito, inclusive recebi um quiz se havia gostado da compra (???). Espero que façam meu ressarcimento o quanto antes."
**Source:** https://www.reclameaqui.com.br/hotmart/reembolso-nao-efetuado-apos-solicitacao-de-cancelamento-na-hotmart_hTghWtroaKLOLtCq/
**source_type:** buyer_review
**verification_status:** blocked_url_index_verified
**Date:** March 2026 (refund solicited 07/03/2026 per Hotmart response)
**Notes:** Specific complaint URL returned 403 on direct fetch; verbatim extracted from Google search snippet reproducing complaint text. Speaker: Janaina. Product type: clinical aromatherapy course. Payment: PIX. Outcome: refund pending at time of complaint.

---

**F-P02**
**What:** Buyer requested refund citing consumer right of regret (Art. 49 CDC). Reports more than 7 days passed with no refund. Credit card bill approaching due date. Purchase was installment-based.
**Verbatim snippet:** "Solicitei o reembolso, pois se trata de ARREPENDIMENTO DE COMPRA e de acordo com a LEI NO ARTIGO 49 o estorno do cartão deve ser feito IMEDIATAMENTE. Mas, já se passaram mais de 7 dias e não obtive nenhum estorno. A minha fatura do cartão irá vencer em breve vocês acham justo eu ter que pagar por algo que não estou tendo acesso?"
**Source:** https://www.reclameaqui.com.br/hotmart/reembolso-hotmart_Sr3qxsTnWOacpfcW/
**source_type:** buyer_review
**verification_status:** blocked_url_index_verified
**Date:** Hotmart response states refund released 25/07; year not confirmed in snippet
**Notes:** Specific complaint URL returned 403; verbatim from Google search snippet. Speaker: Kauane. Payment: credit card installment. Outcome: refund eventually released per Hotmart response. Reason: buyer regret (arrependimento). Exact year uncertain.

---

**F-P03**
**What:** Buyer reports being unable to purchase any new courses on Hotmart for several months. Payment fails across all methods (PIX, boleto, credit card). Card operator confirmed no payment request received. AI support unhelpful.
**Verbatim snippet:** "Estou há alguns meses sem conseguir comprar nenhum curso da hotmart, consigo acessar os que estão ativos, mas não consigo comprar novos. Ele diz que há uma falha no pagamento, mas não há, pois tento trocar para outras opções de pagamento e continua dando o mesmo erro. Nesse meio tempo já tentei comprar cursos de vários valores e todos dão esse mesmo erro. Mesmo tendo limite/dinheiro, não consigo efetuar a compra no pix, no boleto, no cartão e nenhuma outra forma. Quando tento pedir ajuda no site, sou respondida por inteligência artificial."
**Source:** https://www.reclameaqui.com.br/hotmart/nao-consigo-comprar-produtos-na-hotmart_vYIQ1Ww5qZY4_drr/
**source_type:** buyer_review
**verification_status:** blocked_url_index_verified
**Date:** 02/02/2025
**Notes:** Specific complaint URL returned 403; verbatim from Google search snippet. Speaker: Laura. Existing buyer with active courses. All payment methods fail (PIX, boleto, cartão). Complaint date slightly before April 2025 time window start. Outcome: resolved after Reclameaqui complaint.

---

**F-P04**
**What:** Buyer purchased course "ADS LUCRATIVO" by producer Maria Virgínia. Ad promised 12-month refund guarantee. When buyer tried to request refund, system showed guarantee period expired. Hotmart confirms only 7-day guarantee exists. Purchase used "parcelamento inteligente" (smart installment).
**Verbatim snippet:** "Foi comprado um curso da Maria Virgínia ads lucrativo falando comprando o curso tinha garantia de 12 meses para o reembolso ao tentar solicitar o reembolso já mostra como o prazo do reembolso fora do prazo sendo que no anúncio garantia o prazo de 12 meses gostaria do meu reembolso pois não me identifiquei com o curso"
**Source:** https://www.reclameaqui.com.br/hotmart/compra-do-curso-ads-lucrativo_Us_CQl4UBDtb09EV/
**source_type:** buyer_review
**verification_status:** blocked_url_index_verified
**Date:** Purchase 06/02/2025; guarantee expired 13/02/2025 per Hotmart response
**Notes:** Specific complaint URL returned 403; verbatim from Google search snippet. Speaker: Raisa. Product: ADS LUCRATIVO course. Producer: Maria Virgínia. Payment: parcelamento inteligente. Outcome: refund denied (guarantee expired). Reason: buyer did not identify with the course. Seller's ad falsely promised 12-month guarantee vs. platform's 7-day. Complaint predates time window.

---

**F-P05**
**What:** Buyer purchased "Mestres do Algoritmo" course on 20/10, reports the course does not deliver what it promises. Requested refund on 21/10, seller agreed, but refund via PIX not received by 23/10.
**Verbatim snippet:** "Fiz uma compra pela hotmart do Mestres do Algoritmo dia 20/10 e o curso não tem o q promete,pedi o reembolso no dia 21/10 o vendedor entrou em contato comigo e falei paracele q queria o reembolso ele aceitou e até hoje o reembolso não caiu ,fiz o pagamento via pix e a hotmart não me devolveu o dinheiro ,gostaria q vcs resolvessem isso para mim obrigado."
**Source:** https://www.reclameaqui.com.br/hotmart/reembolso-nao-efetuado-do-curso-mestres-do-algoritmo-comprado-pela-hotmart_ZRL1wuflMgBGnNNO/
**source_type:** buyer_review
**verification_status:** blocked_url_index_verified
**Date:** 23/10/2025
**Notes:** Specific complaint URL returned 403; verbatim from Google search snippet. Speaker: Agnaldo. Product: Mestres do Algoritmo. Payment: PIX. Outcome: refund eventually completed per Hotmart response. Purchase 20/10/2025.

---

**F-P06**
**What:** Buyer purchased "Ruptura Viral IA" course on 25/04. Course is incomplete — missing lesson "Vídeo Dark Horizontal - Animando e Gerando Narração (Parte 04)." Other students also complained in the course description comments. Producer and Hotmart unresponsive.
**Verbatim snippet:** "No dia 25/04 comprei o curso, Ruptura Viral IA, do produtor *****, esse curso veio incompleto, está faltando a aula \"Vídeo Dark Horizontal - Animando e Gerando Narração (Parte 04)\", na descrição das aulas tem vários comentários de outros alunos relatando a falta da aula, eu mandei mensagem e email para o ***** e suporte, sem resposta, tentei contato com a Hotmart que também não dá suporte a esse tipo de problema, a Hotmart apenas passa o email do produtor, que não responde ninguém, vi reclamação de outras pessoas com o mesmo relato, o curso está incompleto."
**Source:** https://www.reclameaqui.com.br/hotmart/curso-incompleto-comprado-na-hotmart-do-produtor_i5KZXHDIhQ7SroMo/
**source_type:** buyer_review
**verification_status:** blocked_url_index_verified
**Date:** 19/05/2025 (complaint posted); purchase 25/04/2025
**Notes:** Specific complaint URL returned 403; verbatim from Google search snippet. Speaker: Frank. Product: Ruptura Viral IA (AI course). Outcome: Hotmart states it is only a payment processor and redirects to producer. Incomplete content. Producer name redacted in snippet.

---

**F-P07**
**What:** Buyer stopped purchasing courses because Hotmart removed course expiration date visibility. Reports worsened platform usability. Now records and saves all course content out of fear of losing access.
**Verbatim snippet:** "Estou sem comprar mais cursos da Hotmart pq simplesmente retiraram as datas dos vencimentos de cada curso comprado, e para piorar, falam que temos que enviar e-mail para cada vendedor do curso para sabermos isso, sendo que é algo fácil de ser implementado, e antes havia na plataforma. Agora querem dar trabalho à toa para o vendedor e para o comprador. Além de terem piorado toda a usabilidade da plataforma, agora temos que dar jeito de gravar todos os cursos por receio de perdermos o prazo de aprendizado"
**Source:** https://www.reclameaqui.com.br/hotmart/nao-e-possivel-ver-o-prazo-de-validade-do-curso_G1Vbv3D-c2GSW105/
**source_type:** buyer_review
**verification_status:** blocked_url_index_verified
**Date:** Accessed April 2026; page undated in snippet
**Notes:** Specific complaint URL returned 403; verbatim from Google search snippet. Speaker: Patrícia. Outcome: buyer abandoned (stopped buying courses). Reason: removed expiration date visibility, worsened usability. Behavioral adaptation: records all course content.

---

**F-P08**
**What:** Buyer in Lauro de Freitas, BA purchased 2 courses but cannot access them. Platform says buyer needs to pay again.
**Verbatim snippet:** "Comprei 02 cursos. Porém, não consigo acessar. A plataforma de ensino. O mesmo informa que preciso pagar o curso novamente."
**Source:** https://www.reclameaqui.com.br/hotmart/dificuldade-de-acesso-a-cursos-comprados_V4bQ18gNaA0emX2y/
**source_type:** buyer_review
**verification_status:** blocked_url_index_verified
**Date:** 01/08/2025
**Notes:** Specific complaint URL returned 403; verbatim from Google search snippet. Speaker: Tamires. Location: Lauro de Freitas - BA. Product type: 2 courses. Outcome: resolved (email mismatch issue — different email used at purchase vs. login).

---

**F-P09**
**What:** Buyer reports Hotmart is obstructing refund requests. The "I can't find my transaction code" workflow on refund.hotmart.com returned no eligible purchases, but entering the code manually worked. Accuses Hotmart of deliberately hiding eligible purchases.
**Verbatim snippet:** "Hotmart está dificultando a solicitação de reembolso! Muito me impressiona que a Hotmart não está ajudando o comprador a solicitar o reembolso da compra feita! O processo é bem simples, basta ir no link: https://refund.hotmart.com/, clicar em Não encontrei o código da transação, digitar seu email, digitar o código de 6 dígitos que chega no email e pronto, aparecem as compras elegíveis para reembolso. Fiz este procedimento e pasmem, ele retornou a mensagem que não há compras disponíveis para reembolso!"
**Source:** https://www.reclameaqui.com.br/hotmart/dificuldade-em-solicitar-reembolso-na-hotmart-e-possivel-ocultacao-de-compras-elegiveis_MGEwiV_0kqFRmGE0/
**source_type:** buyer_review
**verification_status:** blocked_url_index_verified
**Date:** Refund approved 21/11/2025; refund processed 28/11/2025
**Notes:** Specific complaint URL returned 403; verbatim from Google search snippet. Speaker: Cayo. Outcome: refund eventually approved and processed. Describes specific refund.hotmart.com workflow failure.

---

**F-P10**
**What:** Buyer purchased "Super Links 2024" product previous year; was unaware of automatic annual subscription renewal. Requested cancellation from producer before renewal but was charged R$208,56 anyway.
**Verbatim snippet:** "Olá, comprei esse produto no ano passado mas não sabia que tinha assinatura automática. Solicitei ao produtor para cancelar pois não estava conseguindo acessar o link, mandei e-mail e mesmo assim foi cobrado no meu cartão 208,56. Peço por gentileza de me reembolsar pois não vou utilizar o produto."
**Source:** https://www.reclameaqui.com.br/hotmart/cobranca-indevida-de-assinatura-automatica-apos-solicitacao-de-cancelamento-e-pedido-de-reembolso_WIJr8wuVjt6ah0hg/
**source_type:** buyer_review
**verification_status:** blocked_url_index_verified
**Date:** ~January 2026 (subscription cancelled 11/12/2025)
**Notes:** Specific complaint URL returned 403; verbatim from Google search snippet. Speaker: Welton. Product: Super Links 2024. Producer: VASCONCELOS. Price: R$208,56 in 2× installments. Payment: Saldo Hotmart (Hotmart balance). Periodicity: annual subscription. Outcome: refund approved after Reclameaqui complaint.

---

**F-P11**
**What:** Buyer purchased an AI tool from a producer on Hotmart; discovered the product was a sales funnel to upsell another tool at 1000% markup. Requested refund.
**Verbatim snippet:** "O @cleitonquerobin oferta uma ferramenta de ia e aí você compra e quando chega dentro da compra que seria a ferramenta ele te ensina como comprar outra ferramenta com a mensalidade 1000% do valor que ele te vendeu. É isso tudo dentro do Hotmart. Quero meu dinheiro de volta"
**Source:** https://www.reclameaqui.com.br/hotmart/propaganda-enganosa-e-oferta-de-ferramenta-de-ia-com-mensalidade-abusiva_26msD_1WlPuI9_3g/
**source_type:** buyer_review
**verification_status:** blocked_url_index_verified
**Date:** January 2026 (refund processed 07/01/2026)
**Notes:** Specific complaint URL returned 403; verbatim from Google search snippet. Speaker: Marcelo. Product type: AI tool (turned out to be upsell funnel). Payment: Pix. Outcome: refund processed within guarantee period. Transaction codes: HP3647388388C1 and HP3647388388C2.

---

**F-P12**
**What:** Buyer purchased a one-time course and downloaded it; months later received recurring charges from Hotmart for courses never purchased. Had to block credit card to stop charges.
**Verbatim snippet:** "Una vez compre un curso de pago unico y pude descargarlo pero a los meses noto que empiezan a llegarme unos cobros de hotmart de otros cursos que nunca compre, nunca me soluccionaron me toco bloquear la tarjeta para generar una nueva y asi no siguieran robando , OJO CON DEJAR DATOS DE TU TARJETA , MUCHO OJO.."
**Source:** https://es.trustpilot.com/review/hotmart.com?page=9
**source_type:** buyer_review
**verification_status:** blocked_url_index_verified
**Date:** Accessed April 2026; review undated in snippet (likely 2025–2026 based on page position)
**Notes:** Page 9 was directly fetched but this specific review's date was not captured in the subagent report; reviewer name not captured from search snippet processing. Product: one-time payment course (successfully downloaded). Outcome: unauthorized recurring charges for unordered courses; blocked credit card.

---

**F-P13**
**What:** Buyer purchased a product on Hotmart, was charged immediately, but never received confirmation email, product access, or any form of platform access. Multiple support contacts yielded only automated responses. System showed "error desconocido."
**Verbatim snippet:** "Compré un producto en Hotmart y me hicieron el cobro inmediatamente, pero nunca recibí ningún correo de confirmación, acceso al producto ni forma de entrar a la plataforma. Revisé spam, intenté recuperar el acceso, busqué por todos los medios posibles… nada. Contacté al soporte de Hotmart varias veces y solo me dieron respuestas automáticas inútiles, sin resolver absolutamente nada. Me están dando largas y siguen sin entregarme lo que compré. Incluso su sistema me marcó un 'error desconocido' cuando intenté recuperar el acceso."
**Source:** https://es.trustpilot.com/review/hotmart.com?page=11
**source_type:** buyer_review
**verification_status:** blocked_url_index_verified
**Date:** Accessed April 2026; review undated in snippet (likely 2025–2026)
**Notes:** Page 11 not directly fetched; verbatim from Google search snippet indexing Trustpilot page. Reviewer name not captured. Outcome: charged but no product, no access, automated support only.

---

**F-P14**
**What:** Buyer in New York owed installments to Black Sheet Pro; agreed with a Spanish lawyer to pay 7 installments. Paid all 7 but Hotmart continues charging through the platform. Daughter's credit card being debited even after removing it from the platform.
**Verbatim snippet:** "yo debía unas cuotas a black sheet, me contactó un abogado español el cual llegamos a un acuerdo de pagar 7 cuotas y resulta que pagué las 7 cuotas y aún me siguen cobrando a través de la plataforma hotmart, por favor paren de cobrar o me tocará ir a las vías legales, porque ya esto no es un cobro, es un robo cobrar cuotas de más, mi nombre es juan carlos martinez anillo"
**Source:** https://hotmart.pissedconsumer.com/review.html
**source_type:** buyer_review
**verification_status:** blocked_url_index_verified
**Date:** 2 Feb 2026
**Notes:** PissedConsumer page; cannot confirm if directly fetched or from search snippet — assigned provisional status conservatively. Speaker: JUAN M Fda (Juan Carlos Martinez Anillo). Product: Black Sheet Pro. Price: loss stated $231 USD. Location: New York. Outcome: ongoing overcharges, legal threats. Snippet truncated from longer review to preserve continuous passage without full personal identifiers.

---

## Part 3 — Pattern Candidates (sealed)

**Status: sealed; not validated.**

---

**PC-01:** Buyers report being charged for products or subscriptions beyond their initial purchase, including charges for courses not ordered, recurring fees on one-time purchases, and installments exceeding agreed amounts. (References: F-06, F-09, F-10, F-11, F-P10, F-P12, F-P14)

**PC-02:** Buyers report confusion or friction around the refund guarantee period — encountering expired guarantees, technical failures on refund.hotmart.com, and discrepancies between seller-advertised guarantee durations and actual platform-enforced deadlines. (References: F-P01, F-P02, F-P04, F-P09)

**PC-03:** Buyers report receiving products whose content does not match the advertising or purchase expectation — including empty courses, incomplete content, products partially in a different language, and products that are upsell funnels rather than the tool advertised. (References: F-07, F-09, F-P05, F-P06, F-P11, F-P13)

**PC-04:** International buyers (English-speaking, primarily) report discovering Hotmart products via Facebook ads and TikTok-related marketing that promise income-generating activities; the actual product delivered is a digital course or eCourse unrelated to the ad promise. (References: F-06, F-10, F-12)

**PC-05:** Buyers direct complaints to Hotmart for content-quality and delivery issues that Hotmart defines as the producer's responsibility — indicating buyer confusion about the platform's role as payment processor vs. content provider. (References: F-P06, F-P08, F-02, F-05)

---

## Part 4 — Could Not Verify / Out-of-Scope

---

**F-X01:** Reddit buyer experience reports
**Subject:** Buyer-voice posts about Hotmart purchase experiences on Reddit.
**Snippet:** n/a — absence finding
**Notes:** 14+ distinct search queries executed across r/hotmart, r/desabafos, r/brasil, r/farialimabets in Spanish, Portuguese, and English. Zero buyer-voice posts identified. Reddit's Hotmart ecosystem is seller/affiliate-dominated. Direct fetch of reddit.com/r/hotmart/search blocked. SocialGrep data shows Hotmart mentions concentrated in investment/business subreddits, not consumer-complaint contexts. Buyer voice for Hotmart is concentrated on dedicated complaint platforms (Reclameaqui, Trustpilot, PissedConsumer), not Reddit.

---

**F-X02:** YouTube buyer-voice videos
**Subject:** YouTube videos by Hotmart product buyers sharing purchase experiences.
**Snippet:** n/a — absence finding
**Notes:** 12+ search queries executed in Spanish and Portuguese. Zero confirmed buyer-voice videos found. YouTube Hotmart content is ~90% affiliate marketing tutorials, ~5% Hotmart official, ~3% affiliate-promoted reviews with affiliate links, ~2% seller/producer platform opinions. Genuine buyer complaint and review behavior migrates to text-based complaint platforms, not YouTube. Coverage gap: no video_transcript findings could be captured.

---

**F-X03:** Hotmart platform-wide cart abandonment rate
**Subject:** Aggregate cart abandonment data specific to Hotmart.
**Snippet:** n/a — absence finding
**Notes:** Searched for "hotmart cart abandonment rate," "hotmart abandono de carrito," "hotmart taxa de abandono." No Hotmart-specific aggregate figure found published by the platform or by third-party analysts. Hotmart provides cart abandonment reporting tools to individual sellers but does not publish a platform-wide rate. Generic industry benchmark is ~70% (Baymard Institute).

---

**F-X04:** Hotmart average order value (AOV)
**Subject:** Published average order value across Hotmart transactions.
**Snippet:** n/a — absence finding
**Notes:** No Hotmart-specific published AOV found. DPL News article (F-13/F-14 source) notes Finance & Investments and Marketing & Sales categories have the "highest average ticket prices" but provides no numeric AOV. Hotmart's commission structure references a $15 threshold (9.9% + $0.50 for products >$15).

---

**F-X05:** Buyer-voice comparison Hotmart vs. other platforms
**Subject:** Buyer explicitly comparing their purchase experience on Hotmart to Udemy, Domestika, or other course platforms.
**Snippet:** n/a — absence finding
**Notes:** Searched for "comprar en Hotmart vs Udemy experiencia," "Hotmart o Domestika comprador." All Hotmart-vs-competitor content found was from the seller/creator perspective (comparing commission rates, platform features), not buyer experience. No buyer-voice comparison captured.

---

**F-X06:** TikTok buyer discovery chain (from buyer voice)
**Subject:** Buyer describing their full discovery chain from TikTok to Hotmart purchase.
**Snippet:** n/a — absence finding
**Notes:** F-12 captures a buyer who expected "making money on TikTok" (discovery via TikTok-related marketing), but the full discovery-to-purchase chain is not articulated. No buyer-voice finding captured describing "I found this on TikTok and bought it on Hotmart" with complete chain. TikTok content itself was not searchable via available tools.

---

**F-X07:** Quora buyer complaint — drawing course via Facebook
**Subject:** Spanish-speaking buyer purchased a drawing course through Facebook via Hotmart; payment approved but no email received and Hotmart showed an error.
**Verbatim snippet (from search index):** "Compré hace un rato por facebook un curso de dibujo por hotmart. Se aprobó la compra y no me llegó nada al mail y salta hotmart error tengo el número de operación. Y mandé al mail del curso. Ni noticias."
**Source:** https://es.quora.com/Alguien-sabe-si-Hotmart-es-seguro-o-es-una-estafa-o-hay-p%C3%A1ginas-falsas-de-Hotmart-que-son-falsos
**source_type:** buyer_review
**verification_status:** could_not_verify
**Date:** Accessed April 2026; page undated
**Notes:** Quora page blocked on direct fetch; verbatim from search snippet. Question-level URL only — individual answer not addressable by URL. Multiple speakers on same page; cannot isolate this answer's URL. Undated. Discovery channel: Facebook. Product: drawing course. Outcome: payment approved, no access.

---

**F-X08:** Quora buyer complaint — 16% IVA, no comprobante
**Subject:** Buyer purchased a course, was charged 16% IVA tax but never received the tax receipt; refund denied because deadline had passed.
**Verbatim snippet (from search index):** "No yo acabo de comprar un curso me cobraron el 16% de comisión, pague el curso mas el IVA(impuestos para facturar) nunca enviaron el comprobante, de haberlo tenido pido reembolso, cuando lo pedí para cancelar la compra me dijeron que se había pasado la fecha"
**Source:** https://es.quora.com/Alguien-sabe-si-Hotmart-es-seguro-o-es-una-estafa-o-hay-p%C3%A1ginas-falsas-de-Hotmart-que-son-falsos
**source_type:** buyer_review
**verification_status:** could_not_verify
**Date:** Accessed April 2026; page undated
**Notes:** Same URL as F-X07; different speaker. Quora page blocked; verbatim from search snippet. Individual answer not addressable by URL. Undated. Likely Mexican buyer (16% IVA). Outcome: no tax receipt, refund denied.

---

**F-X09:** Quora buyer complaint — double billing
**Subject:** Buyer claims Hotmart charged for two courses when only one was purchased; promised refund never materialized.
**Verbatim snippet (from search index):** "Son un fraude total, compré un curso y me facturaron dos, dijeron me devolverían el descuento y nada de eso ocurrió. Chantas total"
**Source:** https://es.quora.com/Alguien-sabe-si-Hotmart-es-seguro-o-es-una-estafa-o-hay-p%C3%A1ginas-falsas-de-Hotmart-que-son-falsos
**source_type:** buyer_review
**verification_status:** could_not_verify
**Date:** Accessed April 2026; page undated
**Notes:** Same URL as F-X07, F-X08; different speaker. Quora page blocked; verbatim from search snippet. Individual answer not addressable by URL. Undated. Outcome: double billing, unfulfilled refund promise.

---

**F-X10:** OCU Spain — virtual assistant training scam
**Subject:** Spanish buyer enrolled in a training program sold via Hotmart with a job placement guarantee; after months with no placements, concluded it was a scam.
**Verbatim snippet (from search index):** "Tras claros incumplimientos de los servicios que ofrecen, y falta de compromiso con las condiciones del contrato; ya que en el contrato pone literalmente que la finalidad de este es que el alumno trabaje y que si no es aceptado en las vacantes puede recibir el rembolso del dinero, a mi no me han enviado ninguna vacante estando varios meses en la bolsa de empleo"
**Source:** https://www.ocu.org/reclamar/lista-reclamaciones-publicas/estafa-formaci-C3-B3n/77ea9d53c64744630c
**source_type:** buyer_review
**verification_status:** could_not_verify
**Date:** 08/11/2024
**Notes:** OCU URL blocked on direct fetch; verbatim from search snippet. Date 08/11/2024 falls outside April 2025–April 2026 time window. Location: Spain. Product: virtual assistant training program with employment guarantee. Outcome: no job placements after months, buyer requests refund. Secondary issue: phishing attempt via unofficial payment page.

---

**F-X11:** SimilarWeb / Semrush — Hotmart traffic and audience data
**Subject:** Third-party traffic analytics for hotmart.com and pay.hotmart.com.
**Verbatim snippet:** n/a — could not verify (direct fetch of similarweb.com/website/hotmart.com/ and semrush.com/website/hotmart.com/overview/ both returned PERMISSIONS_ERROR)
**Notes:** Analytics subagent reported the following data points, but direct page fetch could not be confirmed:
- 36.88M visits to hotmart.com in Feb 2026, avg session 12:32 (Semrush)
- 65–66% direct traffic, 16% organic search (Semrush/SimilarWeb)
- 38.23% bounce rate, 6.6 pages/visit (Semrush, Nov 2025)
- Audience 54.9% female, 45.1% male; largest age group 25–34 (SimilarWeb, Oct 2025)
- pay.hotmart.com checkout: 14.1M visits, 39.88% bounce rate, avg 2:05 duration (SimilarWeb, Aug 2025)
- Social traffic: YouTube #1, Instagram #2, WhatsApp #3 (SimilarWeb, Oct 2025)
- 136,484 websites using Hotmart payment technology (SimilarWeb, Aug 2025)
All data obtained via subagent search; source URLs blocked on independent verification fetch. Data scope, measurement source, and period were reported by subagent for each point. Degraded to Part 4 per conservative verification rule.

---

**F-X12:** BigBangConversion blog comment — buyer purchased one course, got 20% of content
**Subject:** Spanish-speaking buyer reports purchasing a single course on Hotmart and receiving only 20% of promised content, with no support response.
**Verbatim snippet:** "Hola. Les cuento mi experiencia. Compré un solo curso, y me estafaron!!! me dieron solo el 20% del curso, no tiene servicio de ayuda, sin soporte ni de reclamos, les envié emails y nunca respondieron. Agoté todos los medios para que me solucionen y nunca tuve una respuesta"
**Source:** https://bigbangconversion.com/blog/opinion-hotmart/
**source_type:** blog
**verification_status:** could_not_verify
**Date:** Blog post dated October 2020; comment by "Iván" dated variously as Sept 2024 or undated — inconsistent date attribution across searches
**Notes:** Page directly fetched and comment visible, but degraded to Part 4 because: (1) date falls outside April 2025–April 2026 time window (comment likely 2024 or earlier); (2) inconsistent date attribution between subagent reports (one reports "October 2020," another "September 2024"). Product: single course. Outcome: 20% content delivered, no support. Blog is a producer-focused site (author Javi Pastor is a Hotmart seller).

---

## Part 3 supplement — Aggregate behavior data (sealed observations from F-X11)

The following aggregate observations were reported by the analytics subagent but could not be independently verified via direct page fetch. They are recorded here as context rather than validated findings:

- Hotmart's buyer demographics (SimilarWeb site visitors aged 25–34 peak) diverge from Hotmart's own buyer profile data (purchasers aged 40–59 peak per Hotmart Insights 2023 in F-14), suggesting younger users browse the platform but older users complete purchases.
- 89.9% of Hotmart sales are one-time (single) purchases; 69% of sales are cross-border (international), 31% local (from DPL News article, same source as F-13/F-14/F-15 — directly verified data points not given their own finding IDs to avoid exceeding reasonable density from a single source).
- Social traffic to hotmart.com is led by YouTube, followed by Instagram and WhatsApp, per SimilarWeb (Oct 2025, unverified).
- Hotmart operates in 188 countries with 30+ payment methods and 22 currencies (DPL News, directly verified source).

---

## Research QA Notes

### Forced-to-provisional list
- F-P01 through F-P11 (all Reclameaqui findings): Individual complaint URLs returned HTTP 403 on direct fetch. Verbatim text extracted from Google search result snippets reproducing complaint content. Specific URLs confirmed in search index. Assigned blocked_url_index_verified.
- F-P12, F-P13 (Trustpilot ES pages 9, 11): Reviewer names not captured in search snippet processing. Page 9 was fetched for other reviews (F-01–F-03) but these specific reviews' attribution was incomplete in the snippet-based pass. Assigned blocked_url_index_verified conservatively.
- F-P14 (PissedConsumer): Could not confirm whether page was directly fetched by subagent. Assigned blocked_url_index_verified conservatively.

### Degraded list
- F-X10 (OCU Spain): Degraded from provisional to Part 4 — date (08/11/2024) falls outside time window.
- F-X12 (BigBangConversion blog — Iván): Degraded from clean to Part 4 — inconsistent date attribution and likely outside time window.
- F-X11 (SimilarWeb/Semrush analytics): Degraded from provisional to Part 4 — direct page fetch returned PERMISSIONS_ERROR; cannot confirm subagent access method.
- F-13, F-14, F-15 (DPL News): Retained in Part 1 (directly verified) but article date (March 2024) and data period (2018–2022) predate the time window. No newer aggregate buyer data found to replace these findings. Noted in each finding's Notes field.

### URL-not-fixable list
- Reclameaqui individual complaint pages: All 11 specific URLs returned 403 consistently. Domain-wide pattern; not fixable via URL correction.
- SimilarWeb and Semrush: Direct fetch returned PERMISSIONS_ERROR. These sites restrict automated access.
- es.quora.com: Direct fetch blocked. Quora restricts automated/unauthenticated access.
- ocu.org complaint page: Direct fetch blocked.
- portaldaqueixa.com complaint page: Direct fetch blocked.

### Multi-speaker splits
- https://www.trustpilot.com/review/hotmart.com — 7 findings (F-06 through F-12), each a different reviewer on the same listing page.
- https://es.trustpilot.com/review/hotmart.com?page=9 — 3 findings (F-01, F-02, F-03) + 1 provisional (F-P12), each a different reviewer.
- https://es.trustpilot.com/review/hotmart.com?page=2 — 2 findings (F-04, F-05), each a different reviewer.
- https://es.quora.com/Alguien-sabe-si-Hotmart-es-seguro... — 3 entries (F-X07, F-X08, F-X09), each a different answerer. All degraded to Part 4 due to question-level URL (individual answers not addressable).

### Truncated sources
- Trustpilot English listing page (trustpilot.com/review/hotmart.com): Reviews display truncated with "..." on listing page. Affects F-06, F-07, F-09, F-10, F-11, F-12. Verbatim preserved up to truncation point; truncation is Trustpilot's display behavior, not editorial.
- Reclameaqui listing page snippet: F-P listing-page entries may have been truncated by Google search snippet length limits. Noted per finding.

### source_type ambiguities
- PissedConsumer (F-P14): Classified as buyer_review (consumer complaint platform). Could also be argued as "article" if PissedConsumer is treated as a review aggregator. Kept as buyer_review because the speaker is a verified individual buyer posting their own complaint.
- DPL News (F-13, F-14, F-15): Classified as article. Contains data originally from Hotmart's own Hotmart Insights 2023 report (which would be "report" or "platform_doc"). Classified as article because the cited source is the DPL News article, not the underlying report. The underlying Hotmart Insights 2023 report was not directly accessed.
- PR Newswire (F-16): Classified as report (press release). Could also be "platform_doc" since it conveys Hotmart's own data. Kept as report because it's a PR Newswire publication, not a Hotmart help center page.

### Coverage gaps
1. **Reddit (SD-04):** Zero buyer-voice findings despite 14+ search queries. Reddit's Hotmart discussion ecosystem is seller/affiliate-dominated. Buyer complaint behavior migrates to Reclameaqui, Trustpilot, PissedConsumer.
2. **YouTube (SD-05):** Zero confirmed buyer-voice video findings. YouTube Hotmart content is overwhelmingly affiliate marketing tutorials and seller platform reviews. No video_transcript source_type captured.
3. **Cart abandonment (SD-07):** No platform-wide aggregate figure found.
4. **Average order value (SD-07):** No published figure found.
5. **Buyer comparison with other platforms (SD-10):** No buyer-voice comparison captured; all comparison content found was from seller/creator perspective.
6. **TikTok discovery chain (SD-09):** No complete buyer-narrated discovery chain from TikTok to Hotmart purchase captured. F-12 contains a partial reference.
7. **Time window compliance:** Aggregate data findings (F-13, F-14, F-15) rely on March 2024 article reporting 2022 data. No newer Hotmart buyer volume/demographics report was found for the April 2025–April 2026 window. The Pix Automático finding (F-16) is the only aggregate data point fully within the time window.
8. **Language balance:** Part 1 skews toward English (7 English Trustpilot, 5 Spanish Trustpilot, 3 Spanish articles, 1 English report, 1 English platform_doc). Part 2 is predominantly Portuguese (11 Reclameaqui) with 3 Spanish entries. No Portuguese findings in Part 1 due to Reclameaqui's 403 blocks preventing direct verification.
9. **Positive buyer experiences:** Only 3 of 31 Part 1+2 findings capture positive buyer outcomes (F-03 successful refund, F-04 repeat buyer confidence, F-08 positive experiences). This reflects source bias: complaint platforms (Reclameaqui, Trustpilot at 2.2/5, PissedConsumer at 1.2/5) over-represent negative experiences. Reclameaqui score for Hotmart is 8.5/10 (resolution rate), suggesting a higher base of resolved cases than raw complaint text conveys.

### Decomposition issues
- SD-06 (analytics) and SD-07 (aggregate buyer data) overlap for traffic/engagement metrics. In practice, analytics tools (SimilarWeb, Semrush) serve both sub-searches.
- SD-09 (discovery channels) yielded findings that also serve SD-04/SD-08 (buyer voices describing how they found products). Discovery channel data is embedded in individual buyer findings rather than appearing as standalone findings.