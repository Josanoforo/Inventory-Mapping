# SHARD: Domestika × D4 — Buyer Behavior
# DG_OUTPUT_CONTRACT

---

## Search Decomposition

**SD-01:** Trustpilot domestika.org — buyer reviews within April 2025 – April 2026 window. Executed via web_search and web_fetch of https://www.trustpilot.com/review/domestika.org (page 1), page 2, and es.trustpilot.com page 3. Pages fetched directly. 8,757–8,878 reviews found (count varies by access time). Predominantly 1-star reviews within window. Multiple buyer voices extracted.

**SD-02:** Sitejabber domestika.org — buyer reviews within window. Executed via web_search and web_fetch of https://www.sitejabber.com/reviews/domestika.org. Page fetched directly. 6 total reviews found, 4 within window (May–Dec 2025). All negative. Full review text visible.

**SD-03:** r/Domestika — buyer-voice threads. Executed via web_search ("site:reddit.com/r/Domestika"). Reddit blocked all fetch attempts (direct, old.reddit.com, libredd.it). No thread-level URLs recovered. Subreddit existence confirmed via external references.

**SD-04:** r/learnart — Domestika buyer-voice threads. Executed via web_search ("site:reddit.com/r/learnart domestika"). Zero results returned. Reddit blocked.

**SD-05:** Other subreddits (r/Spanish, r/artistlounge, r/illustration, r/learntodraw, r/graphic_design). Executed via web_search for each. Zero Reddit results returned across all subreddits. One thread URL found via external reference: r/craftsnark/comments/1bmk1j7/domestika_scam/ (March 2024 origin, outside window). Reddit blocked all fetch attempts.

**SD-06:** Spanish-language blog reviews from buyer perspective. Executed via web_search in Spanish ("domestika opiniones 2025 curso compré," "domestika vale la pena," "domestika reseña experiencia compra"). Found: Consumidor Global (2 articles), Genbeta (1 article), Fujistas forum, tuQuejaSuma, OCU complaints, iGraal reviews. Multiple sources fetched.

**SD-07:** YouTube video transcripts in Spanish — Domestika buyer reviews. Executed via web_search ("site:youtube.com domestika opinión 2025," "youtube domestika reseña curso 2025"). TikTok discovery page found (https://www.tiktok.com/discover/cursos-domestika-opiniones) and @nanaliteraria video identified. No transcripts recoverable; video content not directly fetchable.

**SD-08:** Medium / Substack buyer reviews. Executed via web_search ("site:medium.com domestika review 2025," "site:substack.com domestika 2025"). Found: Medium @ben.roberts_50857 (July 2024, outside window), Medium @norec (undated). No in-window Medium/Substack buyer reviews with verifiable dates found.

**SD-09:** SimilarWeb or other analytics reports — Domestika traffic/conversion/AOV data. Executed via web_search and subagent fetch of https://www.similarweb.com/website/domestika.org/ and https://www.semrush.com/website/domestika.org/overview/. SimilarWeb and Semrush data recovered by subagent. ByRATINGS case study URL returned 404; snippet data from search index only.

**SD-10:** Third-party market research — Domestika buyer behavior. Executed via web_search ("domestika market share online courses 2025," "domestika revenue users 2025"). Found: Eightception case study (Apr 2025), Tracxn profile, ZoomInfo, PitchBook, Whop blog review. No dedicated market research report on Domestika buyer behavior found.

**SD-11:** Domestika platform doc about buyer-facing features with behavior data. Executed via web_search ("site:domestika.org help buyer," "domestika refund policy buyer"). No platform documentation containing buyer behavior data (as opposed to marketing claims) found within window.

---

## Part 1 — Clean Findings (direct_verified)

**F-01**
- **What:** Domestika has 8,878 reviews on Trustpilot with a TrustScore of 1.7 out of 5
- **Verbatim snippet:** [Stated in layout: "Domestika Reviews 8,878 • 1.7"]
- **Source:** https://www.trustpilot.com/review/domestika.org?page=2
- **source_type:** unknown
- **verification_status:** direct_verified
- **Date:** Accessed April 2026; page undated
- **Notes:** Public review/complaint site (Trustpilot); no dedicated taxonomy value in current schema. Aggregate rating from page layout at time of fetch. Review count increases over time; earlier fetch of page 1 showed 8,757.

**F-02**
- **What:** Buyer reports being charged an unrequested 370 CAD subscription and receiving a refund after complaint
- **Verbatim snippet:** "Edit. They charged me an unrequested 370 CAD subscription, but they refunded me, so all good, just stop charging unrequested subscriptions to people please"
- **Source:** https://www.trustpilot.com/review/domestika.org?page=2
- **source_type:** unknown
- **verification_status:** direct_verified
- **Date:** Updated Feb 27, 2026
- **Notes:** Public review/complaint site (Trustpilot); no dedicated taxonomy value in current schema. Reviewer: Daniel Valderrama. Full review text visible on fetched page; not truncated.

**F-03**
- **What:** Buyer reports being charged over $500 and receiving only generic email responses when requesting cancellation
- **Verbatim snippet:** "I keep asking to cancel. I'm only getting generic email responses telling me why I can't cancel. Meanwhile, I've been charged over $500 and they are not responding to my requests for cancellation."
- **Source:** https://www.trustpilot.com/review/domestika.org
- **source_type:** unknown
- **verification_status:** direct_verified
- **Date:** Feb 19, 2026
- **Notes:** Public review/complaint site (Trustpilot); no dedicated taxonomy value in current schema. Reviewer: Denise. Full review text visible on fetched page.

**F-04**
- **What:** Buyer reports Domestika charged $349, up from $169 the previous year, and that the website states no refunds; buyer requested a refund via PayPal and canceled subscription
- **Verbatim snippet:** "Domestika charged me $349, up from $169 last year. Their website says no refunds. I requested a refund anyway and notified PayPal. I canceled my subscription today."
- **Source:** https://www.trustpilot.com/review/domestika.org?page=2
- **source_type:** unknown
- **verification_status:** direct_verified
- **Date:** Approximately April 9, 2026 (listed as "4 days ago" on page fetched April 13, 2026)
- **Notes:** Public review/complaint site (Trustpilot); no dedicated taxonomy value in current schema. Reviewer: Paul Blankenship. Full review text visible. Date approximated from relative timestamp.

**F-05**
- **What:** Buyer who had previously purchased three courses without issue reports being charged 228 euros for an unwanted Domestika Plus annual subscription, describing the experience as "patrones oscuros" (dark patterns)
- **Verbatim snippet:** "Como muchas personas, he sido víctima de los patrones oscuros de Domestika.org. Ya había comprado tres cursos en la plataforma anteriormente y nunca he tenido ningún problema. Pero la última compra venía con sorpresa: una suscripción anual a Domestika Plus por tan solo 228 euros"
- **Source:** https://www.consumidorglobal.com/tecnologia/todas-opiniones-estafa-domestika-suscripcion_15595_102.html
- **source_type:** article
- **verification_status:** direct_verified
- **Date:** 8 julio 2025
- **Notes:** Named buyer (O. Chamorro) quoted in investigative consumer journalism article by Juan Manuel Del Olmo in Consumidor Global.

**F-06**
- **What:** Buyer compares Domestika unfavorably to Canva Pro, Adobe, and GoDaddy, stating those platforms notify users before trial or billing period ends as required by law
- **Verbatim snippet:** "Las plataformas más decentes (estoy suscrita a Canva pro, Adobe, GoDaddy, etc.) suelen avisarte antes de que termine el periodo de prueba gratuita o tu periodo de facturación anual. Y no creo que lo hagan porque son buenos, sino porque lo exige la ley"
- **Source:** https://www.consumidorglobal.com/tecnologia/todas-opiniones-estafa-domestika-suscripcion_15595_102.html
- **source_type:** article
- **verification_status:** direct_verified
- **Date:** 8 julio 2025
- **Notes:** Same buyer (O. Chamorro) as F-05; distinct observation about comparison to other subscription platforms. Same article source.

**F-07**
- **What:** Argentine buyer purchased a course for 0.99 dollars and reports a debit of 167.01 dollars appearing on their card a month later for an unrequested item
- **Verbatim snippet:** "Compré un curso de Canva 0,99 dólares y me apareció un mes después un débito en mi tarjeta de 167,01 dólares por otro curso que no he pedido. Exijo un reembolso y que me den de baja mi cuenta"
- **Source:** https://www.consumidorglobal.com/tecnologia/todas-opiniones-estafa-domestika-suscripcion_15595_102.html
- **source_type:** article
- **verification_status:** direct_verified
- **Date:** 8 julio 2025
- **Notes:** Anonymous buyer quoted in article; described as "internauta argentino" in surrounding article text. Prices in USD.

**F-08**
- **What:** Buyer purchased a travel writing course on Domestika for less than two euros in November, having previously bought courses on the platform years earlier without issues
- **Verbatim snippet:** "En noviembre compré un curso de crónicas de viajes en Domestika que costaba menos de dos euros. Yo estaba viajando por Marruecos, muy inspirada, y me pareció una buena idea retomar una escritura más personal que tengo bastante abandonada por mi trabajo del día a día. No le di muchas vueltas: ya había comprado otros cursos en la plataforma años atrás sin ningún problema."
- **Source:** https://www.genbeta.com/paso-a-paso/compre-curso-domestika-noviembre-mes-despues-me-llego-cobro-casi-300-euros-consegui-recuperar-mi-dinero
- **source_type:** article
- **verification_status:** direct_verified
- **Date:** 17 diciembre 2025
- **Notes:** First-person account published as article in Genbeta (Spanish tech outlet). Author: Bárbara Bécares. Course: crónicas de viajes. Location at time of purchase: Morocco.

**F-09**
- **What:** Buyer reports that contacting Domestika involved only an AI chatbot that directed to a page stating the subscription cannot be canceled once activated
- **Verbatim snippet:** "Intentar contactar con Domestika no fue sencillo. Hay un chat en la esquina inferior, pero es para hablar con una IA... y esta te remite a una página donde se indica que no es posible cancelar la suscripción una vez activada."
- **Source:** https://www.genbeta.com/paso-a-paso/compre-curso-domestika-noviembre-mes-despues-me-llego-cobro-casi-300-euros-consegui-recuperar-mi-dinero
- **source_type:** article
- **verification_status:** direct_verified
- **Date:** 17 diciembre 2025
- **Notes:** Same buyer (Bárbara Bécares) as F-08; distinct observation about support interaction and cancellation path.

**F-10**
- **What:** Buyer obtained refund through PayPal dispute after PayPal accepted the claim that the payment was not authorized
- **Verbatim snippet:** "Días después, PayPal aceptó mi reclamación y me devolvió el dinero al considerar que yo, efectivamente, no había autorizado ese pago."
- **Source:** https://www.genbeta.com/paso-a-paso/compre-curso-domestika-noviembre-mes-despues-me-llego-cobro-casi-300-euros-consegui-recuperar-mi-dinero
- **source_type:** article
- **verification_status:** direct_verified
- **Date:** 17 diciembre 2025
- **Notes:** Same buyer (Bárbara Bécares) as F-08 and F-09; distinct observation about refund resolution via PayPal.

**F-11**
- **What:** Sitejabber buyer in Germany reports being charged hundreds of dollars after a $1 course, states cancellation menus referenced by support do not exist, and describes support as automated bots repeating "no refund"
- **Verbatim snippet:** "LISTEN TO THE NEGATIVE REVIEWS. I am out hundreds of dollars because of this company's predatory \"Plus\" trap. They lure you in with a $1 course and then the nightmare begins. They secretly enroll you in a trial that auto-renews for a massive annual fee without sending a single reminder email or warning. By the time you see the charge on your bank statement, they've already locked your account settings so you can't even remove your credit card. I spent hours following their \"cancellation steps\" only to find out they point to menus that don't even exist. It's a gaslighting loop designed to keep your money. Their \"support\" is just a wall of automated bots that repeat the same \"no refund\" script over and over. They are literally stealing from people and hiding behind fine print. If you give them your card info, you are giving them permission to empty your account. GET OUT NOW."
- **Source:** https://www.sitejabber.com/reviews/domestika.org
- **source_type:** unknown
- **verification_status:** direct_verified
- **Date:** December 23, 2025 (Date of experience: October 1, 2025)
- **Notes:** Public review/complaint site (Sitejabber); no dedicated taxonomy value in current schema. Reviewer: Avi T., Germany. Full review text visible on fetched page.

**F-12**
- **What:** Sitejabber buyer in Lithuania reports purchasing a course thinking it was a one-time payment, being charged without clear consent, and finding that after canceling the subscription her credit card remained locked in their system with no option to remove it
- **Verbatim snippet:** "I bought a course, thinking it was a one-time payment. What they didn't make clear was that they were also signing me up for an expensive subscription. Suddenly, I realized they had charged me without my clear consent. That was my first shock. The second shock was worse: even after I canceled the subscription, my credit card stayed locked inside their system. There was no button to remove it, no option to take back control over my own financial data. The only thing they offered was to replace the card with another – as if they own my details forever."
- **Source:** https://www.sitejabber.com/reviews/domestika.org
- **source_type:** unknown
- **verification_status:** direct_verified
- **Date:** September 30, 2025 (Date of experience: September 6, 2025)
- **Notes:** Public review/complaint site (Sitejabber); no dedicated taxonomy value in current schema. Reviewer: Justina G., Lithuania. Full review text visible; excerpt is continuous passage from middle of longer review.

**F-13**
- **What:** Sitejabber buyer in Portugal reports being charged $259.64 without subscribing, having only bought two individual courses, and receiving only automated replies with no human customer service
- **Verbatim snippet:** "I was charged $259.64 by Domestika without ever subscribing to anything. I only bought two individual courses, and suddenly I'm being billed for a subscription I never signed up for. I have reached out multiple times, and all I get are automated replies—there's no customer service, no phone number, no human reply."
- **Source:** https://www.sitejabber.com/reviews/domestika.org
- **source_type:** unknown
- **verification_status:** direct_verified
- **Date:** May 30, 2025 (Date of experience: May 23, 2025)
- **Notes:** Public review/complaint site (Sitejabber); no dedicated taxonomy value in current schema. Reviewer: Arianne A., Portugal. Full review text visible; excerpt is continuous passage from beginning of review.

**F-14**
- **What:** Spanish-language Trustpilot buyer reports positive experience with a Poetryarn crochet/color-mixing course, stating it was everything needed to understand the technique
- **Verbatim snippet:** "Aunque ya sé tejer a gancho, nunca había intentado mezclar colores, este curso de Poetryarn fue todo lo que necesitaba para entender la técnica. Lo recomiendo al 100 %."
- **Source:** https://es.trustpilot.com/review/domestika.org?page=3
- **source_type:** unknown
- **verification_status:** direct_verified
- **Date:** 27 nov 2025
- **Notes:** Public review/complaint site (Trustpilot); no dedicated taxonomy value in current schema. Reviewer: María A. Positive buyer experience. Full review text visible.

---

## Part 2 — Provisional Findings (blocked_url_index_verified)

**F-P01**
- **What:** UK buyer reports being charged $175 in March 2025 without prior notification, then $361.70 subsequently, and escalated to PayPal's legal team, the Competition and Markets Authority (CMA), and Action Fraud
- **Verbatim snippet:** "I am writing this to warn others about Domestika's deceptive billing practices. What started as a small, one-off purchase has turned into a nightmare of unauthorized, high-value charges. In March 2025, I was charged $175 without any prior notification, renewal reminder, or receipt. Most recently, they hit my account for a staggering $361.70—a massive \"price hike\" that was also taken without consent or notice."
- **Source:** https://www.trustpilot.com/review/domestika.org?page=2
- **source_type:** unknown
- **verification_status:** blocked_url_index_verified
- **Date:** Accessed April 2026; reviewer date not visible in snippet
- **Notes:** Public review/complaint site (Trustpilot); no dedicated taxonomy value in current schema. Text recovered from search index snippet tied to specific URL. Reviewer name not visible in snippet. UK location inferred from CMA/Action Fraud references in extended text visible in search result.

**F-P02**
- **What:** Buyer in Japan purchased a course for 155 JPY in December 2025 and was charged 49,522 JPY on January 1, 2026, described as "300 times the original price"; filed case with Cross-border Consumer Center Japan (CCJ)
- **Verbatim snippet:** "I bought a single course for 155 JPY in Dec 2025. On Jan 1, 2026, I was charged 49,522 JPY (300 times the original price!) for a subscription I tried to cancel."
- **Source:** https://ie.trustpilot.com/review/domestika.org?page=7
- **source_type:** unknown
- **verification_status:** blocked_url_index_verified
- **Date:** Approximately January 2026
- **Notes:** Public review/complaint site (Trustpilot); no dedicated taxonomy value in current schema. Text recovered from search index snippet tied to specific URL. Reviewer name: Richie (from Domestika reply context in search snippet).

**F-P03**
- **What:** Buyer in Germany reports being charged €125.46 in January 2025, receiving no response to 7+ emails over 13 months, then being charged $347.52 in January 2026 without renewal notification; filed complaints with California Attorney General, FTC, BaFin (Germany), and European Consumer Centre
- **Verbatim snippet:** "In January 2025 I contacted Domestika to cancel my subscription and request a refund for an unexpected charge of €125.46. They never responded. Not once. Based on their silence, I assumed the subscription was cancelled. In January 2026 they charged me again — this time $347.52 — with no prior renewal notification whatsoever. I have now sent 7+ emails over 13 months. Zero responses."
- **Source:** https://www.trustpilot.com/review/domestika.org?page=3
- **source_type:** unknown
- **verification_status:** blocked_url_index_verified
- **Date:** Accessed April 2026; review appears to be from early 2026
- **Notes:** Public review/complaint site (Trustpilot); no dedicated taxonomy value in current schema. Text recovered from search index snippet tied to specific URL. Extended text in snippet references GDPR Article 17 data deletion request.

**F-P04**
- **What:** Buyer purchased a course for €0.99, which through an unclear process automatically signed them up for a Plus annual subscription; charged €119 in 2025, then €298.93 on January 9, 2026 — triple the previous price — without prior notice or receipt; received a full refund after Trustpilot review
- **Verbatim snippet:** "I purchased a course for €0.99 which, through an unclear process, automatically signed me up for a \"Plus\" annual subscription. I never received any notification regarding the initial activation (€119 in 2025). Furthermore, on January 9th, 2026, I was charged €298.93 for a renewal."
- **Source:** https://ca.trustpilot.com/review/domestika.org?page=8
- **source_type:** unknown
- **verification_status:** blocked_url_index_verified
- **Date:** Accessed April 2026; charge date January 9, 2026
- **Notes:** Public review/complaint site (Trustpilot); no dedicated taxonomy value in current schema. Text from search index of specific URL. Extended snippet indicates refund was eventually received after review and follow-up actions.

**F-P05**
- **What:** Buyer in Turkey purchased a course for 49 TL on December 10, 2025, then found an unauthorized charge of 6,400 TL on January 10, 2026, describing it as a practice that "misleads and victimizes users" under the guise of low-cost course sales
- **Verbatim snippet:** "On December 10, 2025, I purchased one course from Domestika and paid a total of 49 TL for this transaction. The description of the transaction reflected on my credit card statement was \"Order C5110**19T33503436\". During the purchase, I only made payment for this single course and did not consent to any subscription or recurring payment. However, on January 10, 2026, I noticed an unauthorized deduction of 6,400 TL from my credit card by Domestika under the code \"Order C5158**62T33959279\"."
- **Source:** https://www.trustpilot.com/review/domestika.it
- **source_type:** unknown
- **verification_status:** blocked_url_index_verified
- **Date:** Accessed April 2026; charge date January 10, 2026
- **Notes:** Public review/complaint site (Trustpilot); no dedicated taxonomy value in current schema. Text from search index of specific URL (domestika.it Trustpilot page). Prices in Turkish Lira (TL).

**F-P06**
- **What:** Change.org petition titled "DOMESTIKA PLUS ESTAFA" states buyers are charged 99 dollars after 30 days following purchase of a course advertised at 5.99 euros, with confirmation email only showing the course price and "0€" for the free trial in small text
- **Verbatim snippet:** "Compras un curso por un valor mínimo de 5,99€ como ellos anuncian, a la que una vez lo compras sin avisarte ni anunciarte nada te han suscrito a su plan anual, en la confirmación de la compra del curso te pone solo el valor del curso y en muy pequeñito (después de tu prueba gratuita) 0€ es lo que marca en ese email. Pues pasado 30 días te llega el pago de 99$."
- **Source:** https://www.change.org/p/domestika-plus-estafa
- **source_type:** unknown
- **verification_status:** blocked_url_index_verified
- **Date:** Accessed April 2026; page undated (petition ongoing)
- **Notes:** Change.org petition; no dedicated taxonomy value in current schema. Text from search index of specific URL. Search snippet also mentions "Paula Labarca and 19 others have signed recently." Article reference (Consumidor Global) states 12,000+ signatures.

**F-P07**
- **What:** Buyer in Mexico purchased a bracelet-making course for 19 MXN for their daughter, then found a charge of $193.02 USD for Domestika Plus subscription; reports family financial hardship
- **Verbatim snippet:** "Me pongo en contacto con ustedes desde una situación muy sensible para mi familia. El 6 de agosto de 2025 se me realizó un cargo de $193.02 USD por una suscripción Domestika Plus (ID de transacción: 30N29347HU427601C). Este cargo me tomó totalmente por sorpresa, pues nunca lo autoricé de manera consciente. Lo que realmente sucedió es que, con mucha ilusión, compré un curso de pulseras por 19 MXN porque mi hija quiere aprender a hacerlas."
- **Source:** https://domestika.pissedconsumer.com/reviews/RT-P.html
- **source_type:** unknown
- **verification_status:** blocked_url_index_verified
- **Date:** Charge date August 6, 2025
- **Notes:** Public review/complaint site (PissedConsumer); no dedicated taxonomy value in current schema. Text reported by research subagent from page fetch; not independently verified by lead researcher. Location: Mexico. Course: bracelet-making (pulseras). Price: 19 MXN course, $193.02 USD subscription.

**F-P08**
- **What:** Chilean buyer purchased a course for $845 Chilean pesos in March 2025 and received a charge of $164,780 pesos on May 2 for an unauthorized Domestika Plus subscription
- **Verbatim snippet:** "Durante el mes de marzo compré un curso en Domestika por $845 pesos chilenos. El 2 de mayo recibí un cobro de $164780 pesos, por cobro de una suscripción a Domestika plus, que no solicité y que por supuesto que no aparecía en la descripción del anuncio."
- **Source:** https://www.reclamos.cl/domestika/reclamo/2025/may/domestika-estafa-suscripci-n-no-autorizada
- **source_type:** unknown
- **verification_status:** blocked_url_index_verified
- **Date:** Published May 5, 2025
- **Notes:** Chilean consumer complaints site (Reclamos.cl); no dedicated taxonomy value in current schema. Text reported by research subagent from page fetch. Location: Chile. Prices in CLP.

**F-P09**
- **What:** Buyer on Spanish Trustpilot reports purchasing a course for 0.99 euros on July 2, 2025 and being charged 313.41 euros in August 2025
- **Verbatim snippet:** "El día 2 de julio de 2025 compré un curso individual en la plataforma Domestika por 0,99 €. En el mes de agosto de 2025 se cargó en mi cuenta bancaria un importe de 313,41 €, correspondiente"
- **Source:** https://es.trustpilot.com/review/domestika.org?page=3
- **source_type:** unknown
- **verification_status:** blocked_url_index_verified
- **Date:** July 2, 2025 (purchase date); review visible on page fetched but text truncated ("Ver más")
- **Notes:** Public review/complaint site (Trustpilot); no dedicated taxonomy value in current schema. Review text partially visible on directly fetched page but truncated; full text not recovered. Snippet tied to specific URL via direct page access showing truncated version.

**F-P10**
- **What:** BBB profile for Domestika Inc. shows 298 total complaints in last 3 years, 181 complaints closed in last 12 months, and 291 unanswered; business is NOT BBB Accredited with a Pattern of Complaints alert active
- **Verbatim snippet:** [Stated in layout: "298 total complaints (last 3 years); 181 complaints closed in last 12 months; 291 unanswered"]
- **Source:** https://www.bbb.org/us/ca/berkeley/profile/art-and-culture/domestika-inc-1116-953820/complaints
- **source_type:** unknown
- **verification_status:** blocked_url_index_verified
- **Date:** Accessed April 2026; page undated
- **Notes:** Public review/complaint site (BBB); no dedicated taxonomy value in current schema. Data reported by research subagent from page fetch; not independently verified. HQ listed as 2001 Addison St. Suite 300, Berkeley, CA 94704.

**F-P11**
- **What:** Semrush reports Domestika received 6.44M visits in March 2026 with average session duration 11:01, bounce rate 58.86%, and 4.2 pages per visit; top traffic countries are Spain (12.3%), United States (11.45%), Mexico (8.33%), Brazil (7.93%), Colombia (6.86%)
- **Verbatim snippet:** "In March domestika.org received 6.44M visits with the average session duration 11:01. Compared to February traffic to domestika.org has increased by 14.48%."
- **Source:** https://www.semrush.com/website/domestika.org/overview/
- **source_type:** report
- **verification_status:** blocked_url_index_verified
- **Date:** March 2026 data (page fetched by subagent April 11, 2026)
- **Notes:** Semrush uses anonymized clickstream data and ML algorithms; estimated data, not GA4-validated. Data reported by research subagent from direct page fetch; not independently verified by lead researcher.

**F-P12**
- **What:** Spanish-language Trustpilot buyer who has been a Domestika user for years and invested in courses across diverse topics rates them all as enriching
- **Verbatim snippet:** "Soy usuario en DOMESTIKA desde hace años. He invertido en varios cursos de temas diversos. Todos (TODOS) han resultado muy enriquecedores."
- **Source:** https://es.trustpilot.com/review/domestika.org?page=3
- **source_type:** unknown
- **verification_status:** blocked_url_index_verified
- **Date:** 30 nov 2025
- **Notes:** Public review/complaint site (Trustpilot); no dedicated taxonomy value in current schema. Reviewer: Poncho Alarcon. Review text visible on directly fetched page but truncated after initial sentences ("Ver más"). Only the visible portion is captured. Positive buyer experience.

---

## Part 3 — Pattern Candidates (sealed)

**PC-01**
- **Candidate statement:** Buyers across multiple countries and currencies report purchasing individual courses priced under $2/€2 and subsequently being charged amounts ranging from $100–$600+ for Domestika Plus annual subscriptions they report not knowingly authorizing.
- **Related Finding IDs:** F-05, F-07, F-08, F-11, F-13, F-P02, F-P04, F-P05, F-P07, F-P08, F-P09
- **Status:** sealed; not validated

**PC-02**
- **Candidate statement:** Buyers who report attempting to resolve billing disputes with Domestika describe encountering AI chatbots and automated email responses rather than human customer service representatives.
- **Related Finding IDs:** F-03, F-09, F-11, F-13
- **Status:** sealed; not validated

**PC-03**
- **Candidate statement:** Buyers who report obtaining refunds describe doing so through PayPal disputes, bank chargebacks, or complaints to external consumer protection organizations rather than through Domestika's internal support processes.
- **Related Finding IDs:** F-02, F-04, F-10, F-P03
- **Status:** sealed; not validated

**PC-04**
- **Candidate statement:** Buyers who report positive course content experiences describe specific courses by name and reference the quality of instruction, while buyers reporting negative experiences focus on billing and subscription practices rather than course content quality.
- **Related Finding IDs:** F-14, F-P12 (positive content); F-03, F-05, F-11, F-13 (billing focus)
- **Status:** sealed; not validated

**PC-05**
- **Candidate statement:** Buyers in multiple findings report that the Domestika Plus subscription annual price increased from approximately €80–€120 to approximately €270–€350 between 2024/2025 and 2025/2026 renewal cycles.
- **Related Finding IDs:** F-04, F-P03, F-P04
- **Status:** sealed; not validated

---

## Part 4 — Could Not Verify / Out-of-Scope

**F-X01: Reddit r/Domestika buyer-voice threads**
- **What:** No data found on buyer-voice threads in r/Domestika within April 2025–April 2026 window
- **Verbatim snippet:** n/a — absence finding
- **Source:** Searched: web_search "site:reddit.com/r/Domestika buyer review 2025"; web_search "site:reddit.com domestika course review 2025"; web_search "reddit domestika review bought course 2025"; attempted web_fetch of https://www.reddit.com/r/Domestika/ (blocked)
- **source_type:** unknown
- **verification_status:** could_not_verify
- **Date:** Accessed April 2026
- **Notes:** Searched locations only. Reddit blocks all fetch attempts. Zero Reddit results returned from site:reddit.com searches. Subreddit existence confirmed via external references but no thread-level URLs within window were recoverable.

**F-X02: Reddit r/craftsnark "Domestika Scam" thread**
- **What:** Thread URL https://www.reddit.com/r/craftsnark/comments/1bmk1j7/domestika_scam/ identified via external references but inaccessible
- **Verbatim snippet:** n/a — could not verify
- **Source:** URL identified via references in sewingreport.com, artdesignbytc.com, and medium.com/@ben.roberts_50857; direct fetch blocked; libredd.it fetch blocked; old.reddit.com fetch blocked
- **source_type:** reddit
- **verification_status:** could_not_verify
- **Date:** Original post approximately March 2024 (outside window); may contain newer comments
- **Notes:** Thread URL is fixed and specific, but all access methods failed. Original post predates the April 2025 window. Cannot confirm whether in-window comments exist without access.

**F-X03: Reddit r/learnart and other subreddits Domestika discussions**
- **What:** No data found on Domestika buyer discussions in r/learnart, r/Spanish, r/artistlounge, r/illustration, r/learntodraw, or r/graphic_design
- **Verbatim snippet:** n/a — absence finding
- **Source:** Searched: web_search "site:reddit.com/r/learnart domestika 2025"; web_search "site:reddit.com/r/Spanish domestika 2025"; web_search "site:reddit.com/r/illustration domestika 2025"; web_search "site:reddit.com/r/graphic_design domestika 2025"; web_search "site:reddit.com/r/learntodraw domestika"; web_search "site:reddit.com/r/artistlounge domestika"
- **source_type:** unknown
- **verification_status:** could_not_verify
- **Date:** Accessed April 2026
- **Notes:** Searched locations only. Zero results returned for all subreddit-specific searches. Reddit anti-indexing measures may prevent discovery.

**F-X04: YouTube Spanish-language video transcripts on Domestika buyer experience**
- **What:** TikTok discovery page and individual TikTok videos identified (e.g., @nanaliteraria "Cuidado con esta plataforma #domestika #estafa," 1,985 likes, 646 comments) but video transcripts not recoverable
- **Verbatim snippet:** n/a — could not verify
- **Source:** Searched: web_search "site:youtube.com domestika opinión 2025"; web_search "youtube domestika reseña curso compré 2025"; found https://www.tiktok.com/@nanaliteraria/video/7441600101849648417 in search results but transcript not accessible
- **source_type:** unknown
- **verification_status:** could_not_verify
- **Date:** Accessed April 2026
- **Notes:** Searched locations only. YouTube and TikTok video content is not fetchable as text. Video existence confirmed but buyer-voice content within cannot be extracted or verified.

**F-X05: ByRATINGS Domestika buyer behavior case study**
- **What:** ByRATINGS case study "How Domestika identifies customers who will buy more" referenced in search results with metrics including "30% increase in conversion in segmented campaigns" and "70% of revenue was achieved with just 35% of the user base" but page returned 404
- **Verbatim snippet:** n/a — could not verify
- **Source:** URL https://byratings.com/success-case/how-domestika-identifies-customers-who-will-buy-more/ returned 404 on direct fetch. Metrics appeared in search index snippets and on https://byratings.com/customer-stories/ but without date, scope, or sample information.
- **source_type:** report
- **verification_status:** could_not_verify
- **Date:** Accessed April 2026; page date unknown
- **Notes:** Page returned 404 error. Search snippets reference "community of over 1M users" which predates current 8M+ figure, suggesting case study may be from an earlier period. Metrics lack the required source + scope + period attribution per direction rules (Rule 4).

**F-X06: Domestika conversion rate (visitor-to-buyer)**
- **What:** No data found on Domestika's website conversion rate
- **Verbatim snippet:** n/a — absence finding
- **Source:** Searched: web_search "domestika conversion rate buyer data 2025"; web_search "domestika conversion rate 2025 2026"; reviewed SimilarWeb and Semrush outputs. Neither publishes Domestika-specific conversion rates.
- **source_type:** unknown
- **verification_status:** could_not_verify
- **Date:** Accessed April 2026
- **Notes:** Searched locations only. No third-party analytics source publishes Domestika-specific visitor-to-buyer conversion rate data.

**F-X07: Domestika cart abandonment rate**
- **What:** No data found on Domestika-specific cart abandonment rate
- **Verbatim snippet:** n/a — absence finding
- **Source:** Searched: web_search "domestika average order value cart abandonment"; web_search "domestika cart abandonment rate 2025". No Domestika-specific data found.
- **source_type:** unknown
- **verification_status:** could_not_verify
- **Date:** Accessed April 2026
- **Notes:** Searched locations only. Baymard Institute publishes industry average (~70%) but no Domestika-specific rate found.

**F-X08: Domestika average order value**
- **What:** No data found on Domestika average order value (AOV)
- **Verbatim snippet:** n/a — absence finding
- **Source:** Searched: web_search "domestika average order value 2025"; web_search "domestika AOV buyer data". No Domestika-specific AOV data found in any source.
- **source_type:** unknown
- **verification_status:** could_not_verify
- **Date:** Accessed April 2026
- **Notes:** Searched locations only. Course price ranges ($10–$40) are published by multiple review sites but no aggregated AOV metric found.

**F-X09: Medium/Substack Domestika buyer reviews within window**
- **What:** No Medium or Substack articles with buyer-voice content about Domestika found within April 2025–April 2026 window
- **Verbatim snippet:** n/a — absence finding
- **Source:** Searched: web_search "site:medium.com domestika review 2025"; web_search "site:medium.com domestika course buyer 2025"; web_search "site:substack.com domestika 2025"; web_search "medium domestika opinión experiencia 2025". Found Medium @ben.roberts_50857 (July 2024, outside window) and Medium @norec (undated, cannot confirm window).
- **source_type:** unknown
- **verification_status:** could_not_verify
- **Date:** Accessed April 2026
- **Notes:** Searched locations only. Two Medium posts found but neither published within the April 2025–April 2026 window with verifiable dates.

**F-X10: Domestika platform documentation with buyer behavior data**
- **What:** No data found on Domestika platform documentation containing buyer behavior data (distinct from marketing claims)
- **Verbatim snippet:** n/a — absence finding
- **Source:** Searched: web_search "site:domestika.org help buyer"; web_search "domestika.org refund policy buyer"; web_search "domestika help center buyer purchase refund policy". Found help center/refund policy pages but none containing buyer behavior analytics.
- **source_type:** unknown
- **verification_status:** could_not_verify
- **Date:** Accessed April 2026
- **Notes:** Searched locations only. Domestika help center pages discuss policies but do not publish buyer behavior data.

**F-X11: SimilarWeb Domestika detailed buyer/conversion data**
- **What:** SimilarWeb page for domestika.org accessed by subagent showing traffic estimates (6.9M–8.2M visits) and demographics but source page was not independently verified and specific visit figures vary between snapshots
- **Verbatim snippet:** n/a — could not verify
- **Source:** https://www.similarweb.com/website/domestika.org/ — attempted fetch by subagent; data reported but two different visit counts (8.2M and 6.9M) from same source raise consistency concerns
- **source_type:** report
- **verification_status:** could_not_verify
- **Date:** Reported as January 2026 data by subagent
- **Notes:** SimilarWeb data is estimated, not GA4-validated. Conflicting visit figures from same source (8.2M vs 6.9M) may reflect different months or measurement updates. Could not independently verify which snapshot applies. Degraded to Part 4 due to inconsistency.

**F-X12: Fujistas.com forum — Domestika buyer thread**
- **What:** Spanish photography forum thread titled "DOMESTIKA = Estafa" contains buyer voices describing unauthorized Plus charges after purchasing 0.99€ courses, including one buyer who reports filing a police report and eventually receiving a refund described by Domestika as "an error"
- **Verbatim snippet:** "Pues estos estafadores me acaban de pasar un cargo de 156€ por una servicio que no solicite, ni disfruté."
- **Source:** https://fujistas.com/foro/threads/domestika-estafa.84418/
- **source_type:** unknown
- **verification_status:** could_not_verify
- **Date:** Accessed April 2026; thread appears active in 2025–2026 based on search snippet content but exact post dates not visible in snippet
- **Notes:** Text from search index snippet only; page not directly fetched. Forum post dates not independently confirmed. Degraded to Part 4 because exact dates of individual posts are not visible in search snippet, preventing confirmation of window compliance.

---

## Research QA Notes

**Container ambiguity:** Trustpilot review pages contain multiple buyers per page. Each buyer review was split into a separate finding per the multi-speaker page rule. The same URL appears across multiple findings within Part 1 (e.g., F-02 and F-03 share https://www.trustpilot.com/review/domestika.org; F-05, F-06, F-07 share the Consumidor Global URL).

**Findings forced to Provisional (Part 2):** F-P01 through F-P12. Reasons: F-P01, F-P02, F-P03, F-P04, F-P05 — text recovered from search index snippets of specific Trustpilot URLs; pages were not independently fetched by lead researcher. F-P06 — Change.org text from search index. F-P07 — PissedConsumer text reported by subagent; not independently verified. F-P08 — Reclamos.cl text reported by subagent; not independently verified. F-P09 — text visible on directly fetched page but truncated ("Ver más"); full review text not recovered. F-P10 — BBB data reported by subagent; not independently verified. F-P11 — Semrush data reported by subagent from direct fetch; not independently verified by lead researcher. F-P12 — review text visible but truncated on directly fetched page.

**Findings degraded to could_not_verify:** F-X02 — Reddit thread URL is fixed but all access methods failed. F-X05 — ByRATINGS page returned 404; metrics lack required scope/period attribution. F-X11 — SimilarWeb data inconsistency between two reported snapshots (8.2M vs 6.9M). F-X12 — Fujistas forum text from search snippet only; individual post dates not confirmable.

**Findings degraded due to URL not fixable:** None. All findings have specific URLs.

**Multi-speaker pages split into separate findings:** Trustpilot page 1 (https://www.trustpilot.com/review/domestika.org) → F-02, F-03. Trustpilot page 2 → F-01, F-04, F-P01. Sitejabber page → F-11, F-12, F-13. Consumidor Global article → F-05, F-06, F-07. Genbeta article → F-08, F-09, F-10. es.Trustpilot page 3 → F-14, F-P09, F-P12.

**Truncated/partial sources:** Multiple Trustpilot reviews are truncated with "See more" / "Ver más" on fetched pages. Only visible text was used for verbatim snippets. Full review text was not accessible for truncated reviews. Findings with truncated text that could still support a meaningful What were included with notes; those where truncation prevented meaningful extraction were excluded. Consumidor Global article fetch was truncated at approximately 4,500 tokens; later sections of the article (including full Change.org petition text and additional buyer voices) were only available via search index snippets.

**source_type ambiguities:** All Trustpilot, Sitejabber, BBB, PissedConsumer, Reclamos.cl, Change.org, and Fujistas findings classified as `unknown` per contract rule that Trustpilot/Sitejabber/BBB use `unknown`; extended by analogy to other public review/complaint sites not in the 18-value taxonomy. Semrush classified as `report`. Consumidor Global and Genbeta classified as `article` (investigative consumer journalism). No `buyer_review` classification was used because on-platform Domestika reviews were not captured as verified findings (subagent reported them but they were not independently verified by lead researcher; excluded from Parts 1-2 to avoid inflating clean count).

**Coverage gaps by category (expected but not found):**
- Reddit buyer voice: Complete gap. All Reddit access blocked.
- YouTube/TikTok video transcripts: Complete gap. Video content not fetchable as text.
- Medium/Substack in-window buyer reviews: Complete gap. No verifiable in-window content found.
- Domestika on-platform buyer reviews: Subagent reported positive buyer reviews from domestika.org course pages (e.g., self-promotion course, May 2025) but these were not independently verified and are excluded from Parts 1-2.
- Buyer discovery channel data: Limited. Only F-P01 (sponsored ad) and F-08 (returning buyer) and F-06 (comparison platforms) contain discovery chain information. No systematic buyer discovery data found.
- Conversion/AOV/cart abandonment metrics: Complete gap. No Domestika-specific ecommerce funnel metrics found from any source.
- Positive buyer experiences: Underrepresented relative to negative. F-14, F-P12 are the only positive-sentiment findings captured in Parts 1-2. The Trustpilot aggregate data (F-01: 1.7/5) suggests positive reviews exist but are a small minority within the review population.

**Cases where input couldn't be decomposed without interpretation:** The "Canva" reference in F-07 likely refers to a Canva-related course on Domestika (not a purchase on Canva.com), based on article context. This interpretation was noted but no qualifier was added to the What field per the "no inferred categories" rule.