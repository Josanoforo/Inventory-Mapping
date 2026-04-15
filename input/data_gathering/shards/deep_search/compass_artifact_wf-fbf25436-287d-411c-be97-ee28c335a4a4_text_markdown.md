# DG Run — Gumroad × D4: Buyer Behavior

---

## 1. Search Decomposition

**SD-01 — Reddit buyer-voice content**
- Queries: `site:reddit.com/r/gumroad "bought" 2025`; `site:reddit.com "bought on gumroad" 2025 2026`; `reddit gumroad purchase experience`; `site:reddit.com "gumroad refund" 2025`; `reddit gumroad "payment failed" 2025`; direct fetch attempts on r/gumroad/new/ and r/gumroad/search/?q=bought&sort=new&t=year
- Subreddits covered: r/gumroad, r/NotionSo, r/DigitalArt, r/passive_income
- Yield: 0 buyer-voice thread-level findings. Reddit content not indexable for this topic/period via web search engines.

**SD-02 — Trustpilot buyer reviews**
- Direct fetches: trustpilot.com/review/gumroad.com pages 1, 2, 3 (page 3 via ie.trustpilot.com regional mirror showing identical content)
- Individual review URLs attempted (6 URLs — permissions blocked; content verified via listing pages)
- Yield: 19 buyer-voice reviews identified within window; 12 selected for Part 1, 6 for Part 2, 1 excluded (seller voice on verification)

**SD-03 — BBB buyer complaints**
- Direct fetch: bbb.org/us/ca/san-francisco/profile/ecommerce/gumroad-1116-448858/complaints
- Yield: 6 buyer complaints in window; 1 for Part 1, 2 for Part 2, 3 excluded (seller voice or redundant with Trustpilot)

**SD-04 — PissedConsumer buyer reviews**
- Direct fetch: gumroad.pissedconsumer.com/review.html
- Web search: `site:pissedconsumer.com gumroad`
- Yield: 6 reviews found; 3 to Part 4 (date uncertain or outside window), 3 excluded (overlap with BBB filings or insufficient date precision)

**SD-05 — Sitejabber buyer reviews**
- Web search and direct fetch: sitejabber.com/reviews/gumroad.com
- Yield: 0 reviews within April 2025–April 2026 window. Most recent Sitejabber review predates window (Oct 2024).

**SD-06 — Twitter/X buyer posts**
- Queries: `site:twitter.com "bought on gumroad" 2025`; `site:x.com "bought on gumroad" 2025 2026`; fetch attempted on twitter.com/search?q=%22bought+on+gumroad%22
- Yield: 0. Platform blocked and not indexable via web search.

**SD-07 — YouTube buyer review videos**
- Queries: `site:youtube.com "bought on gumroad" 2025`; `youtube gumroad buyer review 2025`
- Yield: 0 buyer-perspective videos in window.

**SD-08 — Substack buyer posts**
- Queries: `substack "bought on gumroad" 2025`; `substack gumroad purchase review 2025`
- Yield: 0 buyer-voice posts. Found seller-perspective comparison articles only (Payhip vs Gumroad, Stan Store vs Gumroad).

**SD-09 — Gumroad blog / help center / platform docs**
- Fetches attempted: gumroad.com/discover (SPA partial render — meta description captured); customers.gumroad.com/article/191 (redirected; content from search engine cache)
- Web search: `site:gumroad.com/blog buyer data`; `site:help.gumroad.com buyer refund`
- Yield: Discover page meta description (1.6M products). Help center buyer guide content from cached snippets. No buyer behavior statistics published by Gumroad.

**SD-10 — SimilarWeb / Semrush traffic data**
- Fetch attempted: similarweb.com/website/gumroad.com/ (blocked — permissions error)
- Web search: `similarweb gumroad 2025 traffic`; `semrush gumroad 2025`
- Yield: Partial traffic/demographic data from search snippets only. Cannot confirm direct page access for either source.

**SD-11 — Articles / blogs about Gumroad buyer experience**
- Web search: `"gumroad" "buyer experience" 2025`; `"buying on gumroad" experience 2025`
- Direct fetch: foliovision.com/2025/06/negative-reviews-gumroad (success)
- Yield: 1 article with verifiable buyer-relevant data (Foliovision — review system investigation).

**SD-12 — General buyer-voice web search**
- Queries: `"gumroad" "I bought" review 2025`; `"gumroad checkout" experience 2025`; `gumroad "as a buyer" 2025 2026`
- Yield: Results overlapped with SD-02 through SD-04 findings. No unique buyer-voice sources beyond those already captured.

---

## Part 1 — Clean Findings (direct_verified)

---

**F-01**
- **What:** Buyer purchased a Chrome extension for $17 on Gumroad; product did not work; no receipt was provided; developer contact info was missing; buyer received only AI-generated email responses from Gumroad support and was forced to open a chargeback.
- **Verbatim snippet:** "BUYERS BEWARE: I purchased a chrome extension for $17 that didn't work. I never received a receipt and the extension didn't work with no contact info for the developer. I contacted support after multiple AI email responses, was forced to open a chargeback. TERRIBLE customer service. I wish I'd checked into this website before purchasing this extension."
- **Source:** https://www.trustpilot.com/review/gumroad.com?page=3
- **source_type:** unknown
- **verification_status:** direct_verified
- **Date:** August 13, 2025
- **Notes:** Trustpilot buyer review (reviewer: V.C. AF). source_type "unknown" per protocol rule for Trustpilot. Product type: Chrome browser extension. Price: $17 USD. Purchase outcome: product non-functional, chargeback filed. Reviewer location: TH (Thailand). Rating: 1/5. Full review text verified on Trustpilot listing page 3. Review title: "BUYERS BEWARE".

---

**F-02**
- **What:** Buyer attempted to purchase on Gumroad using 4 different bank cards from major European banks; all were declined — either by the bank (flagging Gumroad as suspicious) or by Gumroad's website (claiming the card "isn't supported") — despite all being regular international VISA cards.
- **Verbatim snippet:** "The worst shopping experience I've ever had. I tried 4 different cards from different banks – either the bank declines the transaction because it considers Gumroad suspicious, or the website itself says the card isn't supported. What exactly isn't supported? It's a regular international VISA card from a major European bank. How do you even operate like this?"
- **Source:** https://www.trustpilot.com/review/gumroad.com?page=2
- **source_type:** unknown
- **verification_status:** direct_verified
- **Date:** November 28, 2025
- **Notes:** Trustpilot buyer review (reviewer: Alexey Kolin). Payment method attempted: international VISA. Reviewer location: RS (Serbia). Purchase outcome: abandoned — could not complete checkout with any of 4 cards. Rating: 1/5. Full review text verified on Trustpilot listing page 2 (sorted most recent).

---

**F-03**
- **What:** Buyer purchased a product from a Gumroad seller; experienced a problem (buyer acknowledges partial fault); seller did not respond to multiple help requests; Gumroad initially reassured the buyer and promised a refund, then appeared to reverse that position.
- **Verbatim snippet:** "Bought a product from a seller who uses the site. Had a small problem which to be fair was down to me. Seller never responded to multiple requests for help. Gumroad gave me reassurance that they would help and give a refund. The best they did until lately was answer my emails reasonably quick, despite my earlier thoughts that they would help. Now they seem to be trying to get out of their earlier positive position. All I can say is, don't have any issues as you won't get any responseable conclusions"
- **Source:** https://www.trustpilot.com/review/gumroad.com?page=3
- **source_type:** unknown
- **verification_status:** direct_verified
- **Date:** August 26, 2025
- **Notes:** Trustpilot buyer review (reviewer: Stephen Betts). Product type: unspecified. Purchase outcome: refund initially promised then reneged. Reviewer location: GB (United Kingdom). Rating: 1/5. Review title: "Bought a product from a seller via Gumroad". Full text verified on page 3.

---

**F-04**
- **What:** Buyer paid for a product on Gumroad but never received it; received zero customer support responses, including no automated acknowledgment; reported the transaction to Mastercard for a refund and recommended Gumroad be blacklisted.
- **Verbatim snippet:** "DONT GO NEAR THIS COMPANY. SMOKESCREENS AND MIRRORS EXPERIENCE . ZERO CUSTOMER SUPPORT , NOT EVEN A BOT GENERATED COURTESY MAILMTOMSAY WE HAVE RECEIVED YOUR QUERY/COMPLAINT AND RE LOOKING INTO IT. I HAVE REPORTED THEM TO MASTERCARD WITH A REFUND REQUEST AND A RECOMMENDATION TO BLACK LIST THEM . WETHER IT IS INCOMPETENCE OR DELIBERATE FRAUDULENCE IS DIFFICULT TO TELL, BUT THE RESULT IS THE SAME. YOU WASTE TIME AND MONEY ON A PRODUCT THAT YOU PAY FOR BUT NEVER RECEIVE."
- **Source:** https://www.trustpilot.com/review/gumroad.com?page=2
- **source_type:** unknown
- **verification_status:** direct_verified
- **Date:** November 19, 2025
- **Notes:** Trustpilot buyer review (reviewer: Chris). Payment method: Mastercard. Purchase outcome: product never received, Mastercard chargeback filed with blacklist recommendation. Reviewer location: NO (Norway). Rating: 1/5. All-caps is reviewer's original formatting. Full text verified on page 2.

---

**F-05**
- **What:** Buyer attempted to download purchased files from Gumroad but experienced download speeds below 10 kB/s; a 100 MB file required hours to download and the download canceled repeatedly; buyer verified their own connection speed at 100 MB/s on another platform (Steam).
- **Verbatim snippet:** "Trying to download bought fiels ... Download speed of gumroad <10kB/s ... you have to sit for hours trying to download 100MB that take verywhere els just a second ... and it cancels the download every few minutes... unable to get my purchase ... and i checked ... if i go somewhere else like steam i download at 100MB/s"
- **Source:** https://www.trustpilot.com/review/gumroad.com?page=2
- **source_type:** unknown
- **verification_status:** direct_verified
- **Date:** November 2, 2025
- **Notes:** Trustpilot buyer review (reviewer: Dominik Konter). Purchase outcome: unable to access purchased files due to download speed and stability. Reviewer location: DE (Germany). Rating: 1/5. Ellipses ("...") are reviewer's original punctuation, not editorial truncation. Full text verified on page 2.

---

**F-06**
- **What:** Buyer purchased a book on Gumroad but the seller had not uploaded the file for download; Gumroad did not provide a refund.
- **Verbatim snippet:** "I purchased a book, but seller did not even upload it so I could download. Gumroad never gave me a refund. THis is how Scam works."
- **Source:** https://www.trustpilot.com/review/gumroad.com?page=2
- **source_type:** unknown
- **verification_status:** direct_verified
- **Date:** October 28, 2025
- **Notes:** Trustpilot buyer review (reviewer: Alexander Kalashnikov). Product type: book (digital). Purchase outcome: product not uploaded by seller, no refund from Gumroad. Reviewer location: FI (Finland). Rating: 1/5. Capitalization error ("THis") is original. Full text verified on page 2.

---

**F-07**
- **What:** Buyer was blocked by a Gumroad seller while still within the refund period; provided full proof of being blocked to Gumroad support; received only automated AI replies instructing buyer to "contact the seller"; subsequently, emails were ignored entirely; buyer reported the matter to the FTC and their local bank.
- **Verbatim snippet:** "I provided full proof that I was blocked by the seller within the refund period, yet Gumroad kept sending automated AI replies saying \"contact the seller.\" Now, they simply ignore my emails — not even a single human response. This platform protects scammers, not creators or customers. I've already reported this to FTC and my local bank."
- **Source:** https://www.trustpilot.com/review/gumroad.com?page=2
- **source_type:** unknown
- **verification_status:** direct_verified
- **Date:** October 23, 2025
- **Notes:** Trustpilot buyer review (reviewer: lucas harper sohn). Reviewer location: KR (South Korea). Purchase outcome: blocked by seller, AI-only support responses, escalated to FTC and bank. Rating: 1/5. Full text verified on page 2.

---

**F-08**
- **What:** Buyer subscribed to two Gumroad subscriptions for lessons; both subscriptions stopped delivering lessons despite the buyer continuing to be charged; Gumroad support provided only bot-like responses and refused to help.
- **Verbatim snippet:** "Some of ther worst support I've ever received in my entire life. I keep having bot like responses even though ironically chat GPT would respond better. I randomly had lessons from 2 subscriptions stop sending me lessons despite being charged, the support refuses to help I've never had such poor quality support."
- **Source:** https://www.trustpilot.com/review/gumroad.com?page=2
- **source_type:** unknown
- **verification_status:** direct_verified
- **Date:** October 16, 2025
- **Notes:** Trustpilot buyer review (reviewer: adam). Product type: subscription-based lessons (2 subscriptions). Purchase outcome: continued charges without delivery of content. Reviewer location: GB (United Kingdom). Rating: 1/5. Typo ("ther") is reviewer's original. Full text verified on page 2.

---

**F-09**
- **What:** First-time Gumroad visitor attempted to acquire a free ($0) product but was blocked at checkout by a message claiming an active chargeback on past Gumroad purchases; the buyer was not logged in, had not entered card information, and had never used Gumroad before.
- **Verbatim snippet:** "I was trying to purchase something on Gumroad for $0, but as I got to the checkout, it said that I have an active chargeback on one of my past Gumroad purchases. However, I wasn't logged in, I didn't give them my card information AND I HAVEN'T USED GUMROAD BEFORE. So, even if I did have an active chargeback, how would they know?"
- **Source:** https://www.trustpilot.com/review/gumroad.com?page=3
- **source_type:** unknown
- **verification_status:** direct_verified
- **Date:** August 12, 2025
- **Notes:** Trustpilot buyer review (reviewer: James Mirth). Price: $0 (free product). Purchase outcome: abandoned — blocked by false chargeback flag. Reviewer location: NO (Norway). Rating: 1/5. Review title: "False claims about chargebacks". Implies Gumroad's risk detection may use IP-based or browser-fingerprint blocking. Full text verified on page 3.

---

**F-10**
- **What:** Buyer placed two orders totaling $900 through Gumroad from seller "digitalebooks1"; seller had promoted physical clothing merchandise via Instagram and directed the buyer to complete orders through Gumroad; invoices falsely labeled the purchases as "digital books"; buyer received neither digital content nor physical clothing; one human Gumroad agent acknowledged the complaint and promised a refund, but no refund was issued thereafter.
- **Verbatim snippet:** "On May 31, 2025, I placed two separate orders totaling $900 through the Gumroad platform from the seller digitalebooks1. The seller promoted physical clothing merchandise via Instagram and instructed buyers to complete their orders through Gumroad. However, the invoices falsely labeled the purchases as digital books, even though I never received any digital content or the actual clothing products I paid for."
- **Source:** https://www.bbb.org/us/ca/san-francisco/profile/ecommerce/gumroad-1116-448858/complaints
- **source_type:** unknown
- **verification_status:** direct_verified
- **Date:** July 22, 2025 (complaint filed); purchase date: May 31, 2025
- **Notes:** BBB buyer complaint. source_type "unknown" per protocol rule for BBB. Product type: physical clothing (falsely invoiced as digital books). Price: $900 USD (two orders). Discovery channel: Instagram. Purchase outcome: nothing received; one human agent promised refund, no follow-through. Verbatim is the first paragraph of a multi-paragraph complaint; remaining paragraphs detail seller evidence and refund request. BBB complaint status: Unanswered.

---

**F-11**
- **What:** Investigation of Gumroad's review display system found that product reviews are sorted positive-first (not chronologically), with no user-accessible filter for negative reviews; on MacWhisper (223,515 sales, 1,715 ratings), only 349 ratings include text reviews; Gumroad rounds a real average of 4.37 stars to a displayed 5-star score; sellers can remove negative reviews by refunding the purchase or revoking product access.
- **Verbatim snippet:** "Gumroad reviews are not sorted by most recent. It is positive reviews first with no way to see negative reviews for a popular product except clicking and clicking and clicking. This is what I meant about a fairly dodge platform. Sahil Lavingia has set up Gumroad to make it very difficult for potential buyers to even see negative reviews."
- **Source:** https://foliovision.com/2025/06/negative-reviews-gumroad
- **source_type:** blog
- **verification_status:** direct_verified
- **Date:** June 10, 2025
- **Notes:** Author (Alec Kinnear, Foliovision founder) is a prospective buyer investigating MacWhisper software before purchase. Article includes verifiable observations about platform behavior affecting buyer information access. Additional data in article: MacWhisper review breakdown — 5★: 259, 4★: 31, 3★: 22, 2★: 4, 1★: 33. Author notes ~22 anonymous reviews appear astroturfed, and that creator (Jordi Bruin) reportedly refunded/closed accounts of negative reviewers. Article provides a bookmarklet tool for buyers to load all reviews at once. The finding qualifies as a data point about buyer behavior (review patterns and information access) published by a third-party source.

---

**F-12**
- **What:** Buyer reports being scammed for $20 by a specific named Gumroad seller ("bailey Richardson"); warns others not to buy from this seller.
- **Verbatim snippet:** "I got scammed for 20$ don't buy from bailey Richardson they are the biggest thing"
- **Source:** https://www.trustpilot.com/review/gumroad.com?page=3
- **source_type:** unknown
- **verification_status:** direct_verified
- **Date:** August 16, 2025
- **Notes:** Trustpilot buyer review (reviewer: Sam Alsaidy). Price: $20 USD. Product type: unspecified. Purchase outcome: scammed — product presumably not delivered or not as described. Reviewer location: GB (United Kingdom). Rating: 1/5. Full text verified on page 3; no truncation indicator present — this appears to be the complete review as posted.

---

## Part 2 — Provisional Findings (blocked_url_index_verified)

---

**F-P01**
- **What:** Buyer purchased piano sheet music and a MIDI file on Gumroad with no problems; defended the platform against scam accusations, attributing issues to individual dishonest sellers rather than the site itself.
- **Verbatim snippet:** "everybody says its a scam blah blah blah, i bought my piano sheet + MIDI with no problems or anything, its about the buyer who ripps you off not the site, dont start bombing it with 1 star reviews jus..."
- **Source:** https://www.trustpilot.com/review/gumroad.com
- **source_type:** unknown
- **verification_status:** blocked_url_index_verified
- **Date:** April 29, 2025
- **Notes:** Trustpilot buyer review (reviewer: Juan). Product type: piano sheet music + MIDI file. Purchase outcome: satisfied — no problems reported. Rating: 5/5. This is the only clearly positive buyer-voice finding within the time window. Review text truncated on Trustpilot listing page (individual review URL not accessible); verbatim is continuous text up to Trustpilot's truncation point. The truncated portion (after "jus...") may contain additional context.

---

**F-P02**
- **What:** Buyer purchased an ebook about veganism on Gumroad and found it entirely generated by ChatGPT, evidenced by bullet-point-only formatting and emojis before every heading; Gumroad declined to take action.
- **Verbatim snippet:** "Bought a book about veganism and it's entirely written by chatgpt. How do i know? It consists only of bullet-point lists and it has emojis before every heading. Gumroad won't do anything about it and..."
- **Source:** https://www.trustpilot.com/review/gumroad.com
- **source_type:** unknown
- **verification_status:** blocked_url_index_verified
- **Date:** July 30, 2025
- **Notes:** Trustpilot buyer review (reviewer: Mitar Milić). Product type: ebook (veganism). Purchase outcome: dissatisfied — AI-generated content with no platform recourse. Rating: 1/5. Review truncated on listing page; individual review URL not accessible.

---

**F-P03**
- **What:** Buyer purchased a book on Gumroad; post-payment Kindle delivery option did not work; buyer set up an account but encountered further difficulties accessing the product.
- **Verbatim snippet:** "This is the worst online purchasing experience I have ever had. I paid for my purchase, post payment I was given the option to send the book to kindle - this didn't work. I set up an account and to..."
- **Source:** https://www.trustpilot.com/review/gumroad.com
- **source_type:** unknown
- **verification_status:** blocked_url_index_verified
- **Date:** July 23, 2025
- **Notes:** Trustpilot buyer review (reviewer: Annie R). Product type: book (ebook). Purchase outcome: could not access/download product via Kindle integration. Rating: 1/5. Review truncated on listing page. Cross-referenced search data (unverified) suggests the full review also describes being double-charged and 2FA authentication issues.

---

**F-P04**
- **What:** Buyer purchased 2 music albums on Gumroad; one album was being censored by the platform despite being allowed to remain listed; PayPal checkout displayed an issue on the final screen.
- **Verbatim snippet:** "I purchased 2 albums. One is apparently being censored by them even though they allow it to be listed. When I checked out with Paypal it told me on the final checkout screen that there was an issue..."
- **Source:** https://www.trustpilot.com/review/gumroad.com
- **source_type:** unknown
- **verification_status:** blocked_url_index_verified
- **Date:** May 6, 2025
- **Notes:** Trustpilot buyer review (reviewer: Steam Cheap). Product type: music albums (2). Payment method: PayPal. Purchase outcome: checkout issues and content censorship encountered. Rating: 1/5. Review truncated on listing page.

---

**F-P05**
- **What:** Buyer purchased a book from the seller subdomain "Depths manifestation.gumroad.com"; buyer had no prior awareness of Gumroad as a company; the book did not arrive; 3 emails sent with no response; purchase was made mid-April 2025.
- **Verbatim snippet:** "Purchased a book from Depths manifestation.gumroad.com. Had no idea about the company needless to say my book has not arrived. I have emailed 3 times with no response. Mid April was my purchase....I'..."
- **Source:** https://www.trustpilot.com/review/gumroad.com
- **source_type:** unknown
- **verification_status:** blocked_url_index_verified
- **Date:** June 17, 2025 (review date); purchase date: mid-April 2025
- **Notes:** Trustpilot buyer review (reviewer: Kara Wanser). Product type: book. Discovery: via seller subdomain — buyer was unaware they were purchasing through Gumroad. Purchase outcome: product not received, seller unresponsive to 3 emails. Rating: 1/5. Review truncated.

---

**F-P06**
- **What:** Buyer attempted to purchase a $15 course on Gumroad; during checkout, an additional unauthorized transaction worth over $100 was processed simultaneously without the buyer's initiation or confirmation.
- **Verbatim snippet:** "I went on this platform to purchase a course that costs 15$ but upon checking out I was shocked to notice that another transaction worth over 100$ that I neither initiated nor confirmed passed simult..."
- **Source:** https://www.trustpilot.com/review/gumroad.com
- **source_type:** unknown
- **verification_status:** blocked_url_index_verified
- **Date:** April 1, 2026
- **Notes:** Trustpilot buyer review (reviewer: Yawovi Holonou). Product type: course. Price: $15 USD (intended purchase); $100+ USD (unauthorized additional charge). Purchase outcome: unauthorized simultaneous transaction during checkout. Rating: 1/5. Review truncated after "simult..." (likely "simultaneously"). Individual review URL not accessible.

---

**F-P07**
- **What:** Buyer purchased a $200 digital product on Gumroad; seller failed to deliver and product links/pages were unavailable from day of purchase; Gumroad instructed buyer to "contact seller directly" despite Gumroad's own stated policy of intervening after 30 days of seller non-response; buyer's card issuer and country's financial regulator both declined recourse due to time-limit expiration.
- **Verbatim snippet:** "I purchased a digital product on Gumroad for approximately $200. The seller failed to deliver the product properly, and I could not access the content from the day of purchase. The link/pages were unavailable and did not function. I contacted the seller many times, but they stopped responding and provided no solution at all. I then contacted Gumroad support and provided full evidence, including screenshots, purchase receipts, and the entire message history. Gumroad repeatedly told me to contact the seller directly and refused to intervene, even though their own policy states that Gumroad may step in when a seller does not respond for 30 days."
- **Source:** https://www.bbb.org/us/ca/san-francisco/profile/ecommerce/gumroad-1116-448858/complaints
- **source_type:** unknown
- **verification_status:** blocked_url_index_verified
- **Date:** November 25, 2025 (complaint filed)
- **Notes:** BBB buyer complaint. source_type "unknown" per protocol rule for BBB. Product type: digital product. Price: ~$200 USD. Purchase outcome: product inaccessible from purchase date; Gumroad did not enforce its own 30-day intervention policy; card issuer and financial regulator both refused recourse (time-expired). Individual complaint URL not available; text visible on BBB complaints listing page. BBB complaint status: Unanswered. Verbatim is first two paragraphs of multi-paragraph complaint.

---

**F-P08**
- **What:** Buyer was charged twice for the same digital product on Gumroad — $37 on May 8, 2025, and $37 on June 5, 2025 ($74 total); Gumroad support confirmed the duplicate purchase on June 5 and said the case would be escalated for review; on June 13 support said it was still under review; no further communication or refund was issued despite multiple follow-ups.
- **Verbatim snippet:** "I was charged twice for the same digital product once on May 8, 2025, and again on June 5, 2025. I contacted Gumroad Support immediately. On June 5, Gumroad Support confirmed the duplicate purchase and said the case would be escalated for review. On June 13, they replied again saying it was still under review. However, since then, I have received no further communication, and no refund has been issued."
- **Source:** https://www.bbb.org/us/ca/san-francisco/profile/ecommerce/gumroad-1116-448858/complaints
- **source_type:** unknown
- **verification_status:** blocked_url_index_verified
- **Date:** July 10, 2025 (complaint filed); charges on May 8 and June 5, 2025
- **Notes:** BBB buyer complaint. Product type: digital product ("Full Bundle"). Price: $37 USD per transaction, $74 USD total (duplicate charge). Purchase outcome: Gumroad acknowledged the duplicate but never processed the refund. Individual complaint URL not available; text from BBB listing page. Verbatim is excerpt from multi-paragraph complaint. BBB complaint status: Unanswered.

---

**F-P09**
- **What:** Gumroad's buyer-facing marketplace page ("Discover") advertises over 1.6 million free and premium digital products available for browsing across categories including education, tech, and design; top product tags by volume include VRChat (23,361 listings), 3D model (13,192), and Notion template (12,329).
- **Verbatim snippet:** "Browse over 1.6 million free and premium digital products in education, tech, design, and more categories from Gumroad creators and online entrepreneurs."
- **Source:** https://gumroad.com/discover
- **source_type:** platform_doc
- **verification_status:** blocked_url_index_verified
- **Date:** Accessed April 2026; page undated
- **Notes:** Gumroad Discover page is a single-page application (SPA); full dynamic content did not render on static fetch, but meta description tag was captured from the page source HTML. Top tag counts (VRChat 23,361; 3D model 13,192; Notion template 12,329; VRChat asset 10,256; Blender 9,271) were visible on discover.gumroad.com free products page. Product count claim (1.6M+) is Gumroad's own marketing; no independent verification of this number was found. Categories confirmed: 3D, Audio, Comics/Graphic Novels, Business/Money, Design, Drawing/Painting, Films, Education, Fitness/Health, Fiction Books, Gaming, Music/Sound Design, Photography, Self-Improvement, Recorded Music, Software Development, Writing/Publishing.

---

## Part 3 — Pattern Candidates (sealed)

---

**PC-01 — Automated support barrier between buyers and dispute resolution**

Across multiple findings, buyers describe Gumroad customer support responding exclusively or primarily through automated/AI systems during purchase disputes. Reported behaviors include receiving "AI email responses" (F-01), "bot like responses" (F-08), "automated AI replies saying 'contact the seller'" (F-07), and "ZERO CUSTOMER SUPPORT, NOT EVEN A BOT GENERATED COURTESY MAIL" (F-04). In several instances, buyers escalated to external authorities — Mastercard (F-04), FTC and local bank (F-07), BBB (F-P07, F-P08) — after failing to reach human support or obtain resolution. One buyer noted "ironically chat GPT would respond better" (F-08). The pattern spans April 2025 through November 2025 and is observed across both Trustpilot and BBB sources.

Descriptive only. No causal claim about whether automation reflects policy, resource constraints, or other factors.

Referenced findings: F-01, F-03, F-04, F-07, F-08, F-P07, F-P08

---

**PC-02 — Product non-delivery across varied failure modes with no effective platform recourse**

Across multiple findings, buyers paid for products on Gumroad and did not receive or could not access them. Observable failure modes include: seller never uploaded the product file (F-06), seller disappeared after payment (F-10, F-P05), seller blocked the buyer (F-07), download infrastructure failed with speeds below 10 kB/s (F-05), unauthorized duplicate charges (F-P08), and AI-generated content delivered instead of a genuine product (F-P02). Purchase prices range from $0 (F-09, blocked at checkout) to $900 (F-10). Discovery channels include Instagram (F-10) and seller subdomains (F-P05). Buyers who escalated to Gumroad support were typically directed back to the unresponsive seller.

Descriptive only. No claim about rate, prevalence, or systemic cause.

Referenced findings: F-04, F-05, F-06, F-07, F-10, F-12, F-P02, F-P05, F-P07

---

## Part 4 — Could Not Verify / Out-of-Scope

---

**F-X01: Reddit buyer-voice posts about Gumroad (April 2025–April 2026)**
- **What:** No buyer-voice Reddit thread-level content was recoverable for this topic and period.
- **Verbatim snippet:** n/a — absence finding
- **Source:** Searches attempted: `site:reddit.com/r/gumroad "bought" 2025`; `site:reddit.com "bought on gumroad" 2025 2026`; `site:reddit.com "gumroad purchase" 2025`; `site:reddit.com "gumroad refund" 2025`; `reddit gumroad buyer experience 2025`; `reddit gumroad "payment failed" 2025`; direct fetch of reddit.com/r/gumroad/new/ and /search/?q=bought&sort=new&t=year
- **source_type:** reddit
- **verification_status:** could_not_verify
- **Date:** April 2026 (searches conducted)
- **Notes:** Multiple search strategies across r/gumroad, r/NotionSo, r/DigitalArt, r/passive_income all returned zero thread-level results with buyer-voice content from this period. Reddit content appears poorly indexed by web search engines for Gumroad buyer discussions. This is an indexing/accessibility limitation, not confirmation that such content does not exist.

---

**F-X02: Twitter/X buyer posts about Gumroad purchases**
- **What:** No buyer-voice tweets about Gumroad purchases were verifiable for this period.
- **Verbatim snippet:** n/a — absence finding
- **Source:** Searches attempted: `site:twitter.com "bought on gumroad" 2025`; `site:x.com "bought on gumroad" 2025 2026`; `twitter "gumroad purchase" buyer 2025`; direct fetch attempted on twitter.com/search?q=%22bought+on+gumroad%22
- **source_type:** unknown
- **verification_status:** could_not_verify
- **Date:** April 2026 (searches conducted)
- **Notes:** Twitter/X content is not indexable via web search. Direct access to Twitter search was blocked. Buyer-voice tweets about Gumroad likely exist but cannot be verified through available tools.

---

**F-X03: YouTube buyer review videos for Gumroad**
- **What:** No YouTube videos featuring buyer-perspective reviews of Gumroad purchases were found in the April 2025–April 2026 window.
- **Verbatim snippet:** n/a — absence finding
- **Source:** Searches attempted: `site:youtube.com "bought on gumroad" 2025`; `youtube gumroad buyer review 2025`; `youtube "gumroad purchase" experience 2025`
- **source_type:** video_transcript
- **verification_status:** could_not_verify
- **Date:** April 2026 (searches conducted)
- **Notes:** YouTube results returned seller-focused content (tutorials, platform comparisons) but no buyer-voice purchase reviews within the window.

---

**F-X04: Substack buyer reviews of Gumroad purchases**
- **What:** No Substack posts by buyers reviewing Gumroad purchases were found in the window. Results were exclusively seller/creator comparison articles.
- **Verbatim snippet:** n/a — absence finding
- **Source:** Searches attempted: `substack "bought on gumroad" 2025`; `substack gumroad purchase review 2025`
- **source_type:** blog
- **verification_status:** could_not_verify
- **Date:** April 2026 (searches conducted)
- **Notes:** Found seller-perspective comparison posts (Payhip vs Gumroad by Rhonda Explains, Nov 5 2025; Stan Store vs Gumroad by J.R. Heimbigner, Jul 10 2025) but these are creator voice comparing platforms for selling, not buyer voice. Excluded per D2/D4 boundary.

---

**F-X05: SimilarWeb traffic and behavior data for gumroad.com**
- **What:** Partial SimilarWeb data recovered from search snippets: 64.55% male / 35.45% female visitors; largest age group 18–24; direct traffic 58.05% of desktop visits; YouTube is top social traffic source; chatgpt.com accounts for 3.48% of referral traffic.
- **Verbatim snippet:** "gumroad.com's audience is 64.55% male and 35.45% female. The largest age group of visitors are 18 - 24 year olds." (from search snippet of SimilarWeb page)
- **Source:** https://www.similarweb.com/website/gumroad.com/
- **source_type:** database_profile
- **verification_status:** could_not_verify
- **Date:** February 2026 (data period per snippet); source URL not directly accessed
- **Notes:** Direct fetch of SimilarWeb URL failed (permissions error). All data obtained from search engine result snippets only. Per Edge 3 (intermediary verification not valid indirect access), degraded to could_not_verify. SimilarWeb data is estimated, not GA4-verified. Desktop-only for traffic source breakdown. The chatgpt.com referral at 3.48% is a notable data point about buyer discovery channels if verified.

---

**F-X06: Gumroad-published buyer behavior statistics**
- **What:** No buyer behavior statistics (conversion rates, AOV, cart abandonment, buyer demographics) published by Gumroad were found.
- **Verbatim snippet:** n/a — absence finding
- **Source:** Searches attempted: `site:gumroad.com/blog buyer data statistics`; `site:help.gumroad.com buyer`; `gumroad conversion rate published`; `gumroad buyer demographics official 2025`; fetch attempted on gumroad.com/blog (SPA redirect)
- **source_type:** platform_doc
- **verification_status:** could_not_verify
- **Date:** April 2026 (searches conducted)
- **Notes:** Gumroad does not appear to publish marketplace analytics reports, buyer demographic breakdowns, conversion rate data, or any aggregate buyer behavior statistics on its blog, help center, or public-facing pages. The homepage displays weekly creator earnings ($2,121,615) but no buyer-side metrics. This represents an absence of platform-published buyer data.

---

**F-X07: Semrush traffic aggregates for gumroad.com**
- **What:** Semrush data via search snippets and limited-access preview: January 2026: 27.09M visits, 07:07 avg session duration, 54.91% bounce rate, 3.84 pages/visit; February 2026: 24.14M visits (-10.9% MoM), 06:34 avg session; geographic distribution: US 32.22%, India 7.0%, UK 5.13%, Germany 3.73%, Brazil 2.8%.
- **Verbatim snippet:** "In January gumroad.com received 27.09M visits with the average session duration 07:07." (from Semrush overview page/snippet)
- **Source:** https://www.semrush.com/website/gumroad.com/overview/
- **source_type:** database_profile
- **verification_status:** could_not_verify
- **Date:** January–February 2026 (data periods)
- **Notes:** Cannot confirm whether Semrush page was directly fetched (full data typically requires paid login) or whether data was extracted from free preview / search snippets. Degraded to could_not_verify for source access uncertainty. Semrush estimates are modeled data, not first-party analytics. Data has source (Semrush) and period (Jan/Feb 2026) but scope qualifier (all devices, global) was inferred not explicitly stated in snippet.

---

**F-X08: PissedConsumer — BOI filing scam ($140)**
- **What:** Buyer purchased Beneficial Ownership Information filing papers on Gumroad for $140; identified the product as a scam; requested refund.
- **Verbatim snippet:** "I bought beneficial ownership information online. I did receive a paper to file. I just registered my business. I was thinking the paper came from a secure source. When I scanned the paper, I saw it was on Gumroad, so I bought it. When I was done, I bought it. I don't have any proof, not even a tracking number. I understand it was a scam. I need my $140 to be refunded to me."
- **Source:** https://gumroad.pissedconsumer.com/review.html
- **source_type:** unknown
- **verification_status:** could_not_verify
- **Date:** Listed as January 23, 2025
- **Notes:** Review date (January 2025) falls OUTSIDE the April 2025–April 2026 time window. Moved to Part 4 for date non-compliance. source_type "unknown" per protocol (PissedConsumer). Price: $140 USD. Product type: BOI filing document. Discovery: found via web search while registering business.

---

**F-X09: PissedConsumer — Unauthorized $53 charge**
- **What:** Consumer reported an unauthorized credit card charge of $53.00 described as "GUMROAD* J1 FOR TEACHE" on December 22, 2025; did not authorize the purchase and received no product or service.
- **Verbatim snippet:** "I noticed a charge on my credit card that I do not recognize and would like your help identifying it. Charge description: GUMROAD* J1 FOR TEACHE. Amount: $53.00. Date: December 22, 2025." (partial, from listing page)
- **Source:** https://gumroad.pissedconsumer.com/review.html
- **source_type:** unknown
- **verification_status:** could_not_verify
- **Date:** December 22, 2025 (charge date)
- **Notes:** Within time window. However: (1) ambiguous buyer-voice status — the reporter is an unauthorized charge victim, not a volitional buyer; (2) only visible in listing page snippet, individual review not separately verifiable; (3) source_type "unknown" per protocol (PissedConsumer). Price: $53.00 USD. Moved to Part 4 for ambiguous buyer-voice status and source granularity.

---

**F-X10: PissedConsumer — Nail art machine + unwanted subscription**
- **What:** Consumer ordered a nail art digital machine on Gumroad; received an email saying they had agreed to a monthly subscription; found cancellation impossible — phone numbers were not in service and cancellation instructions were confusing; canceled the order and reported the transaction as fraud.
- **Verbatim snippet:** "I ordered a nail art digital machine...then got an email saying I had agreed to a monthly subscription for some reason. Went to cancel, and they make it impossible!!! The numbers ive called were not in service! The instructions to cancel were so confusing! I canceled my order right away and reported them as fraud"
- **Source:** https://gumroad.pissedconsumer.com/review.html
- **source_type:** unknown
- **verification_status:** could_not_verify
- **Date:** Undated in available snippet; review position on listing page suggests mid-2025
- **Notes:** source_type "unknown" per protocol (PissedConsumer). Date cannot be confirmed within the April 2025–April 2026 window from available data. Product type: nail art digital machine. Purchase outcome: order canceled, reported as fraud. Moved to Part 4 for unverifiable date.

---

**F-X11: Trustpilot "$10 Uxpeak ebook" review — attribution conflict**
- **What:** A buyer review reportedly described purchasing a $10 ebook titled "ChatGPT for UX/UI Design: Top Prompts and Expert Tips for Maximum Impact" and leaving a negative review that was suppressed.
- **Verbatim snippet:** "Don't trust their 5-star reviews. I bought a cheap $10 Uxpeak e-book 'ChatGPT for UX/UI Design: Top Prompts and Expert Tips for Maximum Impact'. I left a negative review, as the book really j..." (from search snippet)
- **Source:** https://www.trustpilot.com/review/gumroad.com
- **source_type:** unknown
- **verification_status:** could_not_verify
- **Date:** Attributed to November 27, 2025
- **Notes:** Initially attributed to reviewer "Julien Carcaly" (Nov 27, 2025) by search snippets. However, direct verification of the Julien Carcaly review at that date found a DIFFERENT review text (seller-voice content about balance withholding and platform policies). The "$10 Uxpeak ebook" quote may belong to a different reviewer or a different date; attribution could not be confirmed. Moved to Part 4 for reviewer identity conflict. Edge case: search snippet text does not match fetched page text for the same attributed reviewer.

---

**F-X12: Sitejabber buyer reviews within time window**
- **What:** No Sitejabber/SmartCustomer reviews for Gumroad fell within the April 2025–April 2026 window.
- **Verbatim snippet:** n/a — absence finding
- **Source:** Searches attempted: web_fetch of sitejabber.com/reviews/gumroad.com; web_search `site:sitejabber.com gumroad`
- **source_type:** unknown
- **verification_status:** could_not_verify
- **Date:** April 2026 (searches conducted)
- **Notes:** All 20 existing Sitejabber reviews for Gumroad predate the time window; most recent review was October 23, 2024. Platform appears inactive for Gumroad reviews during the study period.

---

**F-X13: businessmodelcanvastemplate.com buyer behavior statistics**
- **What:** Article claims various buyer behavior statistics including "65% of Gumroad purchases occur on mobile," "42% of revenue from educational digital products (early 2026)," "AI Utility transactions up ~150% YoY," and "referral traffic from existing creator storefronts accounted for 45% of all new sign-ups."
- **Verbatim snippet:** "65% of Gumroad purchases occur on mobile" (from article)
- **Source:** https://businessmodelcanvastemplate.com/blogs/target-market/gumroad-target-market
- **source_type:** blog
- **verification_status:** could_not_verify
- **Date:** Article appears 2025–2026 (exact date unclear)
- **Notes:** Source does not cite primary data sources per statistic; methodology absent; appears to be a business analysis blog with unverifiable claims. Multiple statistics presented without attribution, sample size, or period specification. Does not meet the aggregate data standard requiring source + scope + period with credible methodology. Moved to Part 4 per Direction-specific rule 4.

---

**F-X14: Michael McGhie Trustpilot review — page unconfirmable**
- **What:** Buyer purchased a religious/faith product on Gumroad and never received it; did not receive any confirmation email; product was not accessible when logged into the site.
- **Verbatim snippet:** "This company is a joke. I purchased a religious/faith product and never received it. I didn't get any confirmation email or indication in my gmail account. I logged onto the site but the product th..."
- **Source:** https://www.trustpilot.com/review/gumroad.com
- **source_type:** unknown
- **verification_status:** could_not_verify
- **Date:** May 13, 2025
- **Notes:** Trustpilot buyer review (reviewer: Michael McGhie). Review was visible in earlier search results and on a Trustpilot listing page at time of initial fetch, but the specific page number could not be confirmed on subsequent verification fetches (Trustpilot pagination shifts as new reviews are added). Review text is truncated. Individual review URL not available. Moved to Part 4 because the specific listing page where this text appeared cannot be independently confirmed. Product type: religious/faith product. Purchase outcome: not received, no confirmation email.

---

## Part 5 — Research QA Notes

### Coverage assessment
- **Strongest source:** Trustpilot (pages 2–3 directly fetched, 383 total reviews, 83% one-star, TrustScore 1.3/5). The platform's inherent selection bias (dissatisfied users disproportionately review) is noted but does not affect the validity of individual buyer-voice findings.
- **Weakest sources:** Reddit, Twitter/X, YouTube — all returned zero verifiable buyer-voice findings. This is an accessibility/indexing limitation, not evidence of absence.
- **Aggregate data gap:** No platform-published buyer behavior metrics (conversion rates, AOV, cart abandonment) were found from Gumroad. Third-party analytics (SimilarWeb, Semrush) could not be directly verified. The businessmodelcanvastemplate.com statistics were too poorly sourced to use.
- **BBB context:** Gumroad holds an F rating from BBB with 39 total complaints in the last 3 years, 37 of which were unanswered. 11 complaints were closed in the last 12 months (within window). This aggregate was confirmed on the directly fetched BBB page but is noted here rather than as a standalone finding because the BBB rating reflects both buyer and seller complaints.
- **Positive buyer voice scarcity:** Only 1 clearly positive buyer finding (F-P01, Juan) was captured within the window. Lemar Rakk (page 3, 5-star, "BEST MUSIC KITS SELLERS") was considered but excluded from Parts 1–2 as the review could be interpreted as either buyer voice or seller self-promotion; it was not included to avoid ambiguity. The heavy negative skew reflects Trustpilot's selection bias, not necessarily the overall buyer experience distribution.

### Verification decisions
1. **Trustpilot page 3 mirror:** ie.trustpilot.com (Ireland regional domain) was used for page 3 fetch. This is the same platform/database as trustpilot.com, not a third-party mirror. Treated as direct_verified with notation.
2. **Truncated reviews → Part 2:** Reviews where only truncated text was available on listing pages (individual review URLs blocked) were classified as blocked_url_index_verified. The blocked URL is the individual review page; the "index" is the listing page. Truncation is Trustpilot's UI display, not editorial.
3. **BBB complaints → Part 2:** Individual BBB complaint pages are not publicly accessible; complaint text appears on the complaints listing page. Same blocked_url_index_verified logic as truncated Trustpilot reviews.
4. **Foliovision article:** Classified as a data point about buyer behavior (review patterns, information access) rather than pure buyer voice. Author is a prospective buyer investigating product reviews. The MacWhisper review breakdown data (259/31/22/4/33 by star rating) is an empirically observed count, not an opinion.
5. **Seller voice exclusions:** Multiple reviews initially captured were excluded on verification as seller voice: Julien Carcaly (Nov 27, 2025 — seller discussing balance withholding), theWellness Project/Sam Alsaidy confusion resolved (theWellness Project at Aug 20 is seller voice from South Africa; Sam Alsaidy at Aug 16 is buyer voice confirmed).
6. **PissedConsumer date uncertainty:** Several PissedConsumer reviews were moved to Part 4 because exact dates within the window could not be confirmed from the listing page.

### Protocol compliance notes
- No cross-source synthesis was performed outside Part 3.
- All verbatim snippets are character-for-character continuous passages from source pages.
- No model memory was used as evidence.
- No absence of policy/feature was inferred from inaccessible pages.
- All source_type values are from the 18-value closed list. Trustpilot, BBB, and PissedConsumer use "unknown" per protocol.
- Edge 5 (ambiguous URL) was applied to all subreddit-level Reddit results (none had thread-level URLs).
- Edge 3 (intermediary verification) was applied to SimilarWeb and Semrush data obtained only via search snippets.

### Scope boundary notes
- **D2 boundary:** Seller-voice reviews (account suspensions, payout withholding, verification difficulties) were prevalent on Trustpilot pages 1–3 but excluded per D4 scope. The Evie Shaffer review (Oct 27, 2025, seller describing a buyer's chargeback dispute) was excluded as D2.
- **D3 boundary:** Product listing data visible on Gumroad Discover (category counts, tag volumes) was included in F-P09 as buyer-facing discovery data, not as catalog description.
- **Time window:** All Part 1 and Part 2 findings fall within April 2025–April 2026. F-X08 (Jan 2025) was excluded for being outside the window.