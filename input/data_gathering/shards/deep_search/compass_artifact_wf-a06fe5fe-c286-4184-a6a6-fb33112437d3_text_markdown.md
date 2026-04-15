# SHARD: Payhip × D4 — Buyer behavior
## DG Agent Output

---

# 1. Search Decomposition

**SD-01** | Trustpilot buyer reviews for payhip.com
Query: Fetch https://www.trustpilot.com/review/payhip.com and paginated subpages (?page=3, ?page=4, ?page=8); also au.trustpilot.com and ca.trustpilot.com locale variants. Classify each review as buyer or seller voice.
Result: 406 total reviews; ~99% seller voice. 2 confirmed buyer reviews within window, 1 just outside window.

**SD-02** | Sitejabber buyer reviews for payhip.com
Query: Fetch https://www.sitejabber.com/reviews/payhip.com (redirects to smartcustomer.com/reviews/payhip.com). Classify each review.
Result: 43 total reviews, 2.3/5 stars. 1 confirmed buyer review found (Jan 2024, outside window). All others are seller voice.

**SD-03** | BBB listing for Payhip
Query: web_search "payhip" site:bbb.org
Result: No BBB listing exists. Payhip is UK-based (First Floor, 85 Great Portland Street, London W1W 7LT); BBB covers US/Canada.

**SD-04** | Reddit buyer experiences with Payhip
Queries: "bought on payhip" site:reddit.com | "purchased on payhip" site:reddit.com | "payhip checkout" site:reddit.com | "payhip download" site:reddit.com | "payhip refund" site:reddit.com | "payhip" "as a buyer" site:reddit.com | payhip buyer experience reddit | payhip vs gumroad buyer site:reddit.com | "payhip" "I bought" OR "I purchased" site:reddit.com | site:reddit.com payhip customer 2025 2026 | "payhip" cart checkout payment reddit
Result: Zero buyer-voice Reddit posts or comments found across 16 distinct queries. All Payhip Reddit content is seller-focused.

**SD-05** | SimilarWeb traffic analytics for payhip.com
Query: Fetch https://www.similarweb.com/website/payhip.com/; also web_search for cached/historical snapshots.
Result: March 2026 data directly verified. December 2025 data found in Google search cache. November 2024 data found in cached competitor page.

**SD-06** | General web search for buyer reviews and experiences
Queries: "payhip checkout experience" | "payhip refund" buyer experience | "payhip download" experience review | "bought from payhip" review | "purchased on payhip" experience | payhip buyer review 2025 | payhip customer satisfaction | "payhip" "buying experience" OR "purchase experience"
Result: No additional direct buyer-voice content found beyond Trustpilot. Several blog/article sources with secondary assessments.

**SD-07** | YouTube buyer review content for Payhip
Queries: site:youtube.com "payhip" buyer review | site:youtube.com "bought on payhip" OR "purchased on payhip" | site:youtube.com payhip checkout review 2025 | "payhip" buying experience youtube
Result: Zero buyer-voice YouTube content. All Payhip YouTube videos are seller/creator platform reviews.

**SD-08** | Twitter/X buyer mentions of Payhip
Queries: site:twitter.com OR site:x.com "payhip" "bought" OR "purchased" | "payhip" tweet buyer experience | Attempted fetch of https://twitter.com/search?q=%22payhip%22+review
Result: Zero authentic buyer-voice tweets found within window. Twitter/X content about Payhip is dominated by sellers and Payhip marketing.

**SD-09** | Payhip platform documentation (buyer-relevant)
Queries: Fetch help.payhip.com/article/108-conversion-rate | /article/281-refund-request | /article/158-buying-from-payhip | /article/228-unable-to-open-file | /article/128-custom-checkout-questions
Result: All five articles successfully fetched with full text captured.

**SD-10** | Payhip blog for aggregate buyer data
Query: Fetch https://payhip.com/blog/whats-new-at-payhip-2025/
Result: No aggregate buyer metrics found. Blog is feature announcements. One seller-reported claim about conversion rate improvements from cross-selling.

**SD-11** | Third-party analytics (SEMrush) for traffic/behavior data
Query: web_search "payhip.com" semrush traffic 2026; search snippets from semrush.com/website/payhip.com/overview/
Result: February 2026 data captured from search snippets. 10.55M visits, avg session 08:04. Not directly fetched from page.

**SD-12** | Forum/community buyer discussions about Payhip
Query: web_search payhip buyer experience forum | site:quora.com payhip buyer | Fetch https://www.side7.com/forums/thread/1156/1
Result: One relevant Side7 forum post (Jun 2025) about buyer interaction scarcity. Page blocked by robots.txt; text captured via Google index.

**SD-13** | Conversion rate and cart abandonment data for Payhip
Queries: "payhip" "cart abandonment" OR "abandoned cart" | "payhip" conversion rate report | payhip conversion rate benchmark
Result: No Payhip-specific conversion rate or cart abandonment data exists publicly. Only industry-wide benchmarks found (Baymard: 70.22% average cart abandonment across e-commerce).

**SD-14** | Average order value and session duration data for Payhip
Queries: "payhip" "average order value" OR "AOV" | "payhip" "session duration" OR "time on site" buyer
Result: No Payhip-specific AOV data found. Session duration available only via third-party estimates (SEMrush: 08:04 for full domain, not buyer-specific).

---

# 2. Part 1 — Clean findings (direct_verified)

---

### F-01

**Finding ID:** F-01
**What:** Buyer purchased a WordPress plugin (WP Optimal State Pro WordPress Plugin) from Payhip. Buyer was skeptical because they did not know anything about Payhip or the plugin developer. Payment was quick and easy. Plugin works great. Buyer is 100% satisfied.
**Verbatim snippet:** "I bought a WordPress plugin from Payhip (WP Optimal State Pro WordPress Plugin)\n\nI was skeptical because I didn't really know anything about Payhip or the plugin developer.\n\nEverything worked out just fine. Payment was quick and easy, and the plugin works great.\n\n100% satisfied."
**Source:** https://www.trustpilot.com/review/payhip.com
**source_type:** unknown
**verification_status:** direct_verified
**Date:** Dec 13, 2025
**Notes:** Public review/complaint site; no dedicated taxonomy value in current schema. Reviewer: Paul. Location tag on page: IT (Italy). Star rating: 5 out of 5. Date of experience displayed on page: December 10, 2025. Review label on page: "Unprompted review." Full review text visible without expansion. Qualifiers — Product type: WordPress plugin (WP Optimal State Pro). Purchase outcome: satisfied. Discovery channel: not stated. Price: not stated. Buyer tenure: not stated. QA: buyer-speaker test passed ("I bought").

---

### F-02

**Finding ID:** F-02
**What:** Reviewer states Payhip supports sellers who are scammers. A seller agreed for refunds according to his refund policy but did not issue refunds. Text truncated by page display.
**Verbatim snippet:** "They support sellers who are scammers. I have evidences if you want to check. A seller agreed for refunds according to his refund policy but didn't issue refu..."
**Source:** https://www.trustpilot.com/review/payhip.com?page=3
**source_type:** unknown
**verification_status:** direct_verified
**Date:** Updated Dec 4, 2025
**Notes:** Public review/complaint site; no dedicated taxonomy value in current schema. Reviewer: OA wholesale FBA. No location tag displayed. Star rating: 1 out of 5. Review text truncated on page behind JavaScript "See more" button; the visible portion above is the full directly-verifiable text. Expanded text captured separately via Google search index — see F-P01. The expanded version (F-P01) identifies the product as BOTT Price Action Indicator at USD 499, but those facts are NOT in this truncated snippet and are therefore excluded from this finding's What field. QA: buyer-speaker test passed on expanded text; truncated text alone does not contain explicit "I bought/purchased" but expanded version confirms buyer status.

---

### F-03

**Finding ID:** F-03
**What:** payhip.com received 6.8M total visits. Bounce rate: 41.48%. Pages per visit: 4.38. Average visit duration: 00:02:55. Web traffic increased by 10.97% compared to last month. Direct traffic drives 55.87% of desktop visits; Organic Search is 2nd; Referrals is 3rd. Audience is 58.77% male and 41.23% female. Largest age group: 18–24 year olds. Top country: United States at 38.5%. Organic keyword traffic: 98.86% organic, 1.14% paid. Social media traffic led by YouTube, followed by Pinterest and Instagram (Desktop). Referral category: Video Games Consoles and Accessories 57.04%.
**Verbatim snippet:** "payhip.com's web traffic has increased by 10.97% compared to last month. [...] Total Visits 6.8M [...] Bounce Rate 41.48% [...] Pages per Visit 4.38 [...] Avg Visit Duration 00:02:55 [...] The top traffic source to payhip.com is Direct traffic, driving 55.87% of desktop visits last month Organic Search is the 2nd and Referrals is the 3rd. The most underutilized channel is Mail. [...] payhip.com's audience is 58.77% male and 41.23% female. The largest age group of visitors are 18 - 24 year olds. [...] United States 38.5% [...] Organic 98.86% Paid 1.14% [...] payhip.com gets most of its social media traffic from Youtube, followed by Pinterest and Instagram (Desktop). [...] Video Games Consoles and Accessories 57.04%"
**Source:** https://www.similarweb.com/website/payhip.com/
**source_type:** report
**verification_status:** direct_verified
**Date:** March 2026
**Notes:** Page title: "payhip.com Traffic Analytics, Ranking & Audience [March 2026] | Similarweb." SimilarWeb is estimated/modeled data, not verified by Payhip's own analytics. Page states: "Showing Similarweb estimated data." Metrics cover "desktop visits" primarily. Verbatim snippet assembled from multiple labeled data fields on the same page; [...] marks indicate non-contiguous sections within the same page view. Global Rank: #7,464. Country Rank: #3,723 (United States). Category Rank: #20 in Computers Electronics and Technology > Graphics Multimedia and Web Design (In United States). Top countries also include: United Kingdom 6.52%, France 3.77%, Germany 3.24%, India 2.71%. Top referral categories also include: Adult 4.1%, Music 2.74%. Also visited websites listed: gumroad.com, jinxxy.com, vrmodels.store, forum.ripper.store, vrchat.com. Competitors by affinity: gumroad.com (100%), sellfy.com (90%), vrmodels.store (85%), whop.com (83%). Audience interest categories: Video Games Consoles and Accessories, Computers Electronics and Technology - Other, Programming and Developer Software, Adult, Music. Because individual metrics are displayed as labeled data fields on a dashboard (not narrative prose), the verbatim snippet uses [...] to indicate the non-contiguous nature of each metric block within the same single page. All values captured character-for-character as displayed.

---

### F-04

**Finding ID:** F-04
**What:** Payhip does not hold funds and cannot issue refunds directly. Each seller sets and manages their own refund policy. Buyer should contact seller directly via email from receipt or through seller's store. Sellers typically reply within 24 to 72 hours. If buyer believes a seller is acting in bad faith, buyer can contact Payhip support at contact@payhip.com. If buyer was charged twice, buyer can raise it with bank or payment provider if seller does not resolve.
**Verbatim snippet:** "If you would like to request a refund for a product you purchased from a Payhip seller, you'll need to contact the seller directly. In this article, we'll show you how to get in touch with the seller and what to expect during the process.\n\nPayhip does not hold funds and cannot issue refunds directly. [...] Each seller sets and manages their own refund policy. Some sellers may offer refunds, while others may not, especially if the product has already been downloaded or accessed. [...] Many sellers on Payhip are individual creators or small businesses, so response times may vary. Most sellers typically reply within 24 to 72 hours. [...] If you believe a seller is acting in bad faith, misrepresenting their products, or violating Payhip's policies, please get in touch with our support team at contact@payhip.com."
**Source:** https://help.payhip.com/article/281-refund-request
**source_type:** platform_doc
**verification_status:** direct_verified
**Date:** Updated March 17, 2026
**Notes:** Buyer-facing help center article. Page title: "Refund Request." Article describes the buyer's refund journey. Troubleshooting suggestions before requesting refund: try downloading again, use different browser/device, double-check seller instructions. Buyer recourse chain: contact seller → bank/payment provider → report to Payhip support. [...] marks indicate non-contiguous excerpts from the same article; full article is longer with FAQ sections.

---

### F-05

**Finding ID:** F-05
**What:** Buyers visit seller's store or may be taken directly to a product page via a direct purchase link. Buyers can add to cart and continue browsing or click Buy Now to proceed directly to checkout. At checkout, buyer enters email address and selects payment method. Buyer can pay using PayPal or debit or credit card, depending on seller's setup. Digital products delivered instantly after purchase via download page. Receipt sent to email. Payments processed through Stripe and PayPal. Payhip does not store full payment details. Sellers receive buyer's email and, for physical products, shipping details.
**Verbatim snippet:** "To get started, visit the seller's store. In some cases, you may be taken directly to a product page or checkout if the seller has shared a direct purchase link.\n\nOnce you're on the seller's store, click on the product you're interested in to view more details. You can either add it to your cart and continue browsing or click Buy Now to proceed directly to checkout.\n\nAt checkout, you'll be asked to enter your email address and select a payment method. You can typically pay using PayPal or a debit or credit card, depending on the seller's setup.\n\nOnce your payment is successful, your purchase is complete. [...] Digital products are delivered instantly after purchase via a download page. [...] Yes. After your purchase, you will receive an email receipt that includes your order details, a download or login link, and the seller's contact email. [...] Sellers will receive basic information needed to fulfill your order, such as your email address and, for physical products, your shipping details. They do not have access to your full payment details."
**Source:** https://help.payhip.com/article/158-buying-from-payhip
**source_type:** platform_doc
**verification_status:** direct_verified
**Date:** Updated March 17, 2026
**Notes:** Buyer-facing help center article. Page title: "Buying from Payhip." Article also states: "Yes, payments are processed securely through trusted providers like Stripe and PayPal. Payhip does not store your full payment details." Mentions Payhip marketplace for discovery: "you can browse the Payhip marketplace to discover similar digital products from other creators." Two checkout paths described: Add to Cart (continue browsing) and Buy Now (direct checkout). For memberships/subscriptions, buyer is "prompted to log in and access your content right away." [...] marks indicate non-contiguous excerpts from the same article.

---

### F-06

**Finding ID:** F-06
**What:** Issues buyers encounter when downloading files include running out of download credits. Other documented buyer download problems: not having the proper app or tool to open the file, having exceeded download attempts, not having enough space to save the file, having browser extensions enabled (e.g. ad blockers or VPN), and not having a good internet connection. Download credits can be reset by buyer via a "Reset download credits" button using their purchase email.
**Verbatim snippet:** "One of the issues that buyers encounter when downloading files is running out of download credits. A message similar to the one below will appear notifying you that you have already exceeded your download attempts.\n\nThis can easily be resolved by simply resetting your credits for this transaction. All you need to do is click the \"Reset download credits\" button and enter the email you used to make this purchase. [...] If you have any extensions or add-ons running in the background (e.g. ad blockers or VPN), you might run into some issues whilst downloading large files. [...] Another reason that may be preventing you from successfully downloading the files is your internet speed."
**Source:** https://help.payhip.com/article/228-unable-to-open-file
**source_type:** platform_doc
**verification_status:** direct_verified
**Date:** Updated October 21, 2025
**Notes:** Buyer-facing help center article. Page title: "Unable to Download or Open File." Article lists five common buyer download issues with solutions. Includes file-type compatibility table (RAR/ZIP, PDF, MP3/MP4, DOCX) with recommended apps per OS. File size displayed next to download button on buyer's download page. Fallback support: contact@payhip.com. [...] marks indicate non-contiguous excerpts within the same article.

---

# 3. Part 2 — Provisional findings (blocked_url_index_verified)

---

### F-P01

**Finding ID:** F-P01
**What:** Buyer purchased a digital product (BOTT Price Action Indicator) for USD 499 through a Payhip link promoted by the seller "BO Turbo Trader." Seller's refund policy stated cancellations within 7 days eligible for 100% refund. Buyer requested refund within the period. Seller accepted refund request in writing. Payhip responded that it "does not have access to initiate refunds" because funds are transferred to seller immediately. Buyer states Payhip refused to intervene: did not take action against seller, did not freeze or suspend account, did not warn buyers, did not cooperate with payment processors. Seller accepted refund then delayed and disappeared. Payhip told buyer to "contact the seller" even after buyer confirmed seller stopped replying. Buyer also states seller revoked license access.
**Verbatim snippet:** "I purchased a digital product (BOTT Price Action Indicator) for USD 499 through a Payhip link promoted by the seller \"BO Turbo Trader.\" At the time of purchase, the seller's refund policy clearly stated that cancellations made within 7 days were eligible for a 100% refund. I requested a refund within this period, and the seller accepted my request in writing. [...] Payhip refused to intervene in any meaningful way. [...] Even if Payhip cannot physically reverse a transaction, they absolutely can: Take action against sellers who violate their own policies, Freeze or suspend accounts, Warn buyers, Cooperate with banks and payment processors, Demand accountability from sellers operating on their platform. In my case, Payhip did none of this. [...] The seller clearly acted in bad faith: accepted the refund request and then delayed and disappeared. At a minimum, Payhip should have contacted the seller formally, demanded compliance with their stated policy, and taken action when the seller refused. Instead, they told me to \"contact the seller\" – even after I confirmed the seller had stopped replying completely."
**Source:** https://www.trustpilot.com/review/payhip.com?page=3
**source_type:** unknown
**verification_status:** blocked_url_index_verified
**Date:** Updated Dec 4, 2025
**Notes:** Public review/complaint site; no dedicated taxonomy value in current schema. This is the expanded text of finding F-02. The expanded text was NOT directly fetchable from the Trustpilot page because it requires JavaScript "See more" click interaction. Text captured from Google's search index of the Trustpilot page and from au.trustpilot.com/review/payhip.com?page=4 (locale mirror). Reviewer: OA wholesale FBA. Star rating: 1 out of 5. Qualifiers — Product type: digital trading indicator (BOTT Price Action Indicator). Price: USD 499. Discovery channel: seller-promoted Payhip link. Purchase outcome: negative, refund denied. Seller: "BO Turbo Trader." Seller also revoked buyer's license access. Buyer contacted Payhip, Stripe, and seller — no help received. Buyer compares Payhip unfavorably to Amazon and Etsy for buyer protection. [...] marks indicate non-contiguous excerpts; text continues beyond what Google index captured (point "4." in buyer's list was cut off). QA: buyer-speaker test passed ("I purchased a digital product").

---

### F-P02

**Finding ID:** F-P02
**What:** Forum user states they use Payhip and noticed very few people actually interact with any Payhip stores. States people with Patreon and Ko-fi get all the visitors. States they see more seller than buyer review posts and very little buyer interaction.
**Verbatim snippet:** "I use Payhip mostly because I heard they handle additional EU VAT prices, despite them having 5% take off of prices [...] But I noticed that very few people actually interact with any Payhip stores, at all, meanwhile people with Patreon and Ko-fi get all the visitors. I know people avoid using Payhip to sell items due to poor customer service and all, but I haven't heard anything from the buyer's side? I see more seller than buyer review posts. And very little buyer interaction."
**Source:** https://www.side7.com/forums/thread/1156/1
**source_type:** blog
**verification_status:** blocked_url_index_verified
**Date:** Jun 13, 2025
**Notes:** Art community forum post (Side7). Closest allowed source_type is "blog"; this is a user-generated forum post, not a blog in the strict sense. Page blocked by robots.txt during direct fetch; text captured from Google search index. Author: @untilted (Neophyte, 26 posts, joined 17 Mar 2025). Post edited once (13 Jun 2025, 06:32 PM). Thread appears to have only 1 post (Page 1 of 1, Viewing 1-1 of 1) — no replies visible, no corroboration. Speaker is a SELLER asking about buyer perspectives, not a buyer. However, the observation about buyer interaction scarcity is a first-person behavioral observation about the Payhip ecosystem. Comparison statement: Payhip vs. Patreon and Ko-fi for buyer engagement. [...] marks indicate non-contiguous excerpts within the same post.

---

### F-P03

**Finding ID:** F-P03
**What:** payhip.com web traffic increased by 14.16% compared to last month. Global ranking changed from 8,988 to 8,064. Bounce rate: 42.15%. Pages per visit: 4.40. Average visit duration: 00:03:16. Direct traffic drives 54.46% of desktop visits. Audience is 58.73% male and 41.27% female. Top country: United States at 41.62%.
**Verbatim snippet:** "payhip.com's web traffic has increased by 14.16% compared to last month [...] Global ranking has changed from 8,988 to 8,064 [...] Bounce Rate: 42.15% [...] Pages per Visit: 4.40 [...] Avg Visit Duration: 00:03:16 [...] The top traffic source to payhip.com is Direct traffic, driving 54.46% of desktop visits last month [...] payhip.com's audience is 58.73% male and 41.27% female [...] United States: 41.62%"
**Source:** https://www.similarweb.com/website/payhip.com/
**source_type:** report
**verification_status:** blocked_url_index_verified
**Date:** December 2025
**Notes:** SimilarWeb data for December 2025, captured from Google search cache of the same URL (page title in cache: "payhip.com Traffic Analytics, Ranking & Audience [December 2025] | Similarweb"). Not directly fetched from the live page, which now displays March 2026 data (see F-03). SimilarWeb data is estimated/modeled. December 2025 social media order: YouTube, then Pinterest and Instagram; "Engaging audiences through X-twitter may reveal new opportunities." Most underutilized channel in December: Paid Search (vs. Mail in March 2026). [...] marks indicate non-contiguous data fields from the same cached page.

---

### F-P04

**Finding ID:** F-P04
**What:** payhip.com received 10.55M visits in February 2026 with average session duration 08:04. Compared to January, traffic decreased by -13.38%. Visitors mainly come from Direct (55.05% of traffic), followed by youtube.com (9.5%). Backlinks: 17.16M (dropped -0.5%). Referring domains: 105.54K (increased 0.79%). Core audience located in United States, United Kingdom, and India.
**Verbatim snippet:** "In February payhip.com received 10.55M visits with the average session duration 08:04. Compared to January traffic to payhip.com has decreased by -13.38%. [...] On payhip.com, visitors mainly come from Direct (55.05% of traffic), followed by youtube.com (9.5%). In most cases, after visiting payhip.com, users go to youtube.com and google.com. [...] Payhip.com's core audience is located in United States followed by United Kingdom, and India. [...] In February the number of backlinks to payhip.com has dropped by -0.5% and equals 17.16M. The amount of referring domains has increased by 0.79% and equals 105.54K."
**Source:** https://www.semrush.com/website/payhip.com/overview/
**source_type:** report
**verification_status:** blocked_url_index_verified
**Date:** February 2026
**Notes:** SEMrush data captured from web search result snippets, not directly fetched from the SEMrush page (which may require authentication for full access). SEMrush February 2026 visit count (10.55M) is significantly higher than SimilarWeb March 2026 (6.8M) — different estimation methodologies; neither represents verified first-party data. SEMrush session duration (08:04) covers full payhip.com domain including seller dashboards, help center, and marketing pages — not exclusively buyer sessions. Exit behavior noted: "after visiting payhip.com, users go to youtube.com and google.com." [...] marks indicate non-contiguous snippets from the same search result page.

---

# 4. Part 3 — Pattern candidates (sealed)

---

### PC-01

**Pattern:** Buyer protection gap in post-purchase dispute resolution
**Contributing findings:** F-02, F-P01, F-04
**Observation sealed without interpretation:** F-02 and F-P01 describe a buyer who purchased a USD 499 product, was denied a refund despite seller's own policy, and states Payhip refused to intervene. F-04 documents that Payhip does not hold funds and cannot issue refunds directly; refunds are entirely seller-managed. Both the buyer review and the platform documentation converge on the same structural point about the refund mechanism.

### PC-02

**Pattern:** Low buyer platform awareness and direct-link acquisition model
**Contributing findings:** F-03, F-P02, F-05, F-01
**Observation sealed without interpretation:** F-03 shows 55.87% of payhip.com desktop traffic is direct (not organic search discovery). F-05 describes buyers arriving via "a direct purchase link" shared by the seller. F-P02 reports "very few people actually interact with any Payhip stores" and "very little buyer interaction." F-01 buyer states being "skeptical because I didn't really know anything about Payhip or the plugin developer."

---

# 5. Part 4 — Could not verify / Out-of-scope

---

### F-X01: Daniella Perry Follos buyer review — out of time window

**Finding ID:** F-X01
**What:** Parent buyer purchased a Boeing 737 pack for Roblox game for £35. Received only a text document promising future file delivery. Product was never delivered. Seller took money and removed product from Payhip. Payhip refused to help.
**Verbatim snippet:** "Scammed by a seller, Payhip (the company who took the payment) refuse to do anything to help. My 7 year old son has saved up for a long time to purchase a Boeing 737 pack for his Roblox game. The £35 we spent, all we have received is a text document saying we would be sent the file in no more than 1 day. It has not been sent and they took the money and now removed the product from Payhip! DO NOT USE this platform unless you want to run the risk of being scammed."
**Source:** https://www.trustpilot.com/review/payhip.com (previously visible on page 8; page number has shifted due to new reviews; also appears on au.trustpilot.com and ca.trustpilot.com locale variants)
**source_type:** unknown
**verification_status:** direct_verified
**Date:** Mar 10, 2025
**Notes:** Public review/complaint site; no dedicated taxonomy value in current schema. OUT OF TIME WINDOW: March 2025 is one month before the April 2025 start date. Reviewer: Daniella Perry Follos. Location: MT (Malta). Star rating: 1 out of 5. Date of experience on page: March 9, 2025. Review label: "Unprompted review." Qualifiers — Product type: Roblox game asset (Boeing 737 pack). Price: £35 (GBP). Buyer: parent purchasing for 7-year-old son. Purchase outcome: scammed, product never delivered, product removed from platform. Platform response: refused to help. Buyer-speaker test passed ("My 7 year old son has saved up... to purchase"). QA: Confirmed buyer voice, verified text, but excluded from Parts 1–2 solely for temporal scope.

---

### F-X02: Sasa P. buyer review — out of time window

**Finding ID:** F-X02
**What:** Buyer purchased a set of ebooks ("Agatha Christie Crime Novels Ebook Coolection - pdf+epub+mobi") and received only one book. Seller ignored buyer. Payhip support responded: "I'm sorry I can't help you on this occasion!"
**Verbatim snippet:** "Worst web seller ever! I bought a set of books \"Agatha Christie Crime Novels Ebook Coolection - pdf+epub+mobi\" and I got only one book! The seller persistently ignores me, and when I turned to the website for help, I got the answer: \"I'm sorry I can't help you on this occasion!\" If they won't help people who buy on their website why spend your money there and be plus and cheated and ignored!"
**Source:** https://www.sitejabber.com/reviews/payhip.com
**source_type:** unknown
**verification_status:** direct_verified
**Date:** January 31, 2024
**Notes:** Public review/complaint site; no dedicated taxonomy value in current schema. OUT OF TIME WINDOW: January 2024 is 15 months before start date. Reviewer: Sasa P. Location: GB (Great Britain). Star rating: 1. Qualifiers — Product type: ebook collection (Agatha Christie, pdf+epub+mobi format). Purchase outcome: received 1 book instead of a set. Seller response: persistently ignored. Platform response: declined to help. This review also appears on saasadviser.co and smartcustomer.com (aggregation sites scraping Sitejabber). QA: confirmed buyer voice but temporally out of scope.

---

### F-X03: Reddit buyer voice — absence finding

**Finding ID:** F-X03
**What:** No buyer-voice posts or comments about Payhip exist on Reddit within April 2025 — April 2026.
**Verbatim snippet:** n/a — absence finding
**Source:** Searches attempted: "bought on payhip" site:reddit.com | "purchased on payhip" site:reddit.com | "payhip checkout" site:reddit.com | "payhip download" site:reddit.com | "payhip refund" site:reddit.com | "payhip" "as a buyer" site:reddit.com | payhip buyer experience reddit | site:reddit.com payhip customer 2025 2026 | "payhip" "I bought" OR "I purchased" site:reddit.com | site:reddit.com "payhip" bought purchased customer | "payhip" cart checkout payment reddit | reddit payhip vs gumroad buyer experience | reddit payhip scam OR legit buying 2025 2026 — 16 queries total, zero buyer-voice results
**source_type:** reddit
**verification_status:** could_not_verify
**Date:** April 2025 — April 2026
**Notes:** Comprehensive null finding. All Payhip Reddit content identified is seller-focused (r/Entrepreneur, r/selfpublish, r/ecommerce). Absence is consistent with Payhip's architecture: no centralized marketplace, buyers arrive via direct seller links and associate purchases with the seller rather than the platform.

---

### F-X04: YouTube buyer voice — absence finding

**Finding ID:** F-X04
**What:** No buyer-voice YouTube video content about Payhip exists within April 2025 — April 2026.
**Verbatim snippet:** n/a — absence finding
**Source:** Searches attempted: site:youtube.com "payhip" buyer review | site:youtube.com "bought on payhip" OR "purchased on payhip" | site:youtube.com payhip checkout review 2025 | site:youtube.com "payhip" buying experience OR "as a buyer" OR "I purchased" | "payhip" review buying youtube 2025 2026 — 5 queries, zero buyer-voice results
**source_type:** video_transcript
**verification_status:** could_not_verify
**Date:** April 2025 — April 2026
**Notes:** Comprehensive null finding. All Payhip YouTube content consists of seller/creator platform reviews (e.g., "How to sell on Payhip," "Payhip Review 2025"). No video found where someone reviews buying/purchasing through Payhip as a customer.

---

### F-X05: Twitter/X buyer voice — absence finding

**Finding ID:** F-X05
**What:** No authentic buyer-voice tweets about Payhip purchasing experience found within April 2025 — April 2026.
**Verbatim snippet:** n/a — absence finding
**Source:** Searches attempted: site:twitter.com OR site:x.com "payhip" "bought" OR "purchased" | "payhip" tweet buyer experience | site:x.com "payhip" review buyer — 3 queries, zero buyer-voice results within window
**source_type:** article
**verification_status:** could_not_verify
**Date:** April 2025 — April 2026
**Notes:** Twitter/X Payhip content is dominated by sellers announcing stores, Payhip's own marketing account, and seller-to-seller discussions. One attributed quote found ("Payhip's checkout experience is smooth. I moved from Gumroad and actually saw a slight uptick in conversion!" — attributed to "Shalini Writes" on Twitter in a Medium article by praveenax) could not be independently verified on X and appears to be seller voice, not buyer voice. source_type set to "article" as closest available enum value for social media absence.

---

### F-X06: BBB listing for Payhip — absence finding

**Finding ID:** F-X06
**What:** Payhip has no Better Business Bureau listing.
**Verbatim snippet:** n/a — absence finding
**Source:** Searches attempted: "payhip" site:bbb.org | payhip BBB complaint — zero results
**source_type:** article
**verification_status:** could_not_verify
**Date:** April 2025 — April 2026
**Notes:** Payhip is a UK-based company (London). BBB primarily covers US/Canadian businesses. No complaints, reviews, or profile page exists on BBB for Payhip. source_type set to "article" as proxy; no enum value for business registry/complaint body.

---

### F-X07: Aggregate platform-wide conversion rate — absence finding

**Finding ID:** F-X07
**What:** No Payhip-specific aggregate conversion rate data is publicly available.
**Verbatim snippet:** n/a — absence finding
**Source:** Searches attempted: "payhip" conversion rate benchmark | payhip conversion rate report | payhip average conversion rate | Also fetched https://help.payhip.com/article/108-conversion-rate (describes per-seller dashboard metric but publishes no aggregate benchmark) — zero aggregate results
**source_type:** report
**verification_status:** could_not_verify
**Date:** April 2025 — April 2026
**Notes:** Payhip tracks conversion rate (Views → Started Checkout → Completed Checkout) per seller in individual dashboards but does not publish platform-level aggregate data. No third-party source publishes Payhip-specific conversion benchmarks. The conversion rate help article (last updated June 14, 2021) confirms the feature exists but provides no numbers.

---

### F-X08: Aggregate average order value (AOV) — absence finding

**Finding ID:** F-X08
**What:** No Payhip-specific aggregate average order value data is publicly available.
**Verbatim snippet:** n/a — absence finding
**Source:** Searches attempted: "payhip" "average order value" OR "AOV" | payhip AOV data report — zero aggregate results. Payhip blog articles (payhip.com/blog/increase-average-order-value/ and /blog/offering-discounts-to-customers/) mention AOV as a concept using general industry statistics only.
**source_type:** report
**verification_status:** could_not_verify
**Date:** April 2025 — April 2026
**Notes:** Payhip references AOV only in educational blog content for sellers. Payhip 2025 feature roundup mentions cross-sell tools "designed to help you drive more conversions and increase your customers' average order value" but provides no actual AOV figures. No third-party source publishes Payhip-specific AOV data.

---

### F-X09: Aggregate cart abandonment rate — absence finding

**Finding ID:** F-X09
**What:** No Payhip-specific cart abandonment rate data is publicly available.
**Verbatim snippet:** n/a — absence finding
**Source:** Searches attempted: "payhip" "cart abandonment" OR "abandoned cart" — zero Payhip-specific results. Industry benchmark only: Baymard Institute reports "average cart abandonment rate of 70.22%" across e-commerce (50 studies). ScribeCount article confirms Payhip supports abandoned cart email flows. Medium article by ENG IGA GODFREY notes "Try abandoned cart flow (Payhip supports it!)."
**source_type:** report
**verification_status:** could_not_verify
**Date:** April 2025 — April 2026
**Notes:** Payhip offers abandoned cart flow functionality (feature exists for sellers), but no platform-specific abandonment rate data is published by Payhip or any third party. Industry average (70.22%) is not attributable to Payhip specifically.

---

### F-X10: Buyer satisfaction / NPS data — absence finding

**Finding ID:** F-X10
**What:** No buyer satisfaction survey, Net Promoter Score, or buyer sentiment aggregate data published by Payhip or any third party.
**Verbatim snippet:** n/a — absence finding
**Source:** Searches attempted: payhip buyer satisfaction | payhip NPS score | payhip customer satisfaction survey — zero results
**source_type:** report
**verification_status:** could_not_verify
**Date:** April 2025 — April 2026
**Notes:** Trustpilot aggregate rating (4.5/5, 406 reviews) and Sitejabber aggregate rating (2.3/5, 43 reviews) are NOT buyer satisfaction metrics — both platforms' reviews are overwhelmingly from sellers (~99% on Trustpilot). No buyer-specific satisfaction data exists publicly.

---

### F-X11: Kupkaike blog buyer hesitation claim — secondary retelling

**Finding ID:** F-X11
**What:** Blog article states "Less polished UX: The buyer checkout experience isn't quite as clean as Gumroad's. Some buyers report hesitation at checkout."
**Verbatim snippet:** "Less polished UX: The buyer checkout experience isn't quite as clean as Gumroad's. Some buyers report hesitation at checkout."
**Source:** https://kupkaike.com/blog/etsy-vs-gumroad-vs-payhip
**source_type:** blog
**verification_status:** could_not_verify
**Date:** 2026 (undated article, current content)
**Notes:** Secondary retelling. The claim "Some buyers report hesitation at checkout" cites no source, no sample size, no methodology, no time period. No original buyer statement supporting this claim was found in any primary source across all searches. Per edge case rules: secondary retelling without primary source = Part 4. Also: article is a comparison blog post with potential affiliate intent.

---

### F-X12: Medium attributed Twitter quotes — unverifiable secondary retelling

**Finding ID:** F-X12
**What:** Medium article attributes quote to "Shalini Writes (Twitter)": "Payhip's checkout experience is smooth. I moved from Gumroad and actually saw a slight uptick in conversion!"
**Verbatim snippet:** "'Payhip's checkout experience is smooth. I moved from Gumroad and actually saw a slight uptick in conversion!' — Shalini Writes (Twitter)"
**Source:** https://praveenax.medium.com/payhip-vs-gumroad-vs-instamojo-so-much-choice-332d20957d16
**source_type:** blog
**verification_status:** could_not_verify
**Date:** 2025 (Medium article, undated precisely)
**Notes:** Secondary retelling of attributed Twitter quote. Original tweet could not be found or verified on X/Twitter. The attributed speaker ("Shalini Writes") appears to be a SELLER voice ("I moved from Gumroad" and discusses "conversion" = seller metrics), not a buyer voice, even if the quote were verifiable. Per edge case rules: secondary retelling without primary source verification = Part 4. Also fails buyer-speaker test.

---

### F-X13: Seller BV reporting buyer download failures — D2 voice

**Finding ID:** F-X13
**What:** Seller reports that some customers purchased their e-book and couldn't download it due to broken download link. Seller had to send file manually.
**Verbatim snippet:** "Some customers purchased my e-book and couldn't download it. The download link was broken, even though the files I uploaded were perfectly fine. I contacted Payhip and had to send the file manually ju..."
**Source:** https://www.trustpilot.com/review/payhip.com
**source_type:** unknown
**verification_status:** direct_verified
**Date:** Sep 7, 2025
**Notes:** Public review/complaint site; no dedicated taxonomy value in current schema. OUT OF SCOPE: D2 (seller voice), not D4. Speaker is a seller describing what happened to their buyers. Per direction-specific rule 2 (buyer-speaker test): "Sellers on Payhip report buyers do X" is D2, not D4. Reviewer: BV. Star rating: 1 out of 5. Review text truncated on page. The observation about broken download links affecting buyers is relevant context but does not qualify as buyer voice.

---

### F-X14: Seller Nguyễn Minh Khang reporting buyer chargeback — D2 voice

**Finding ID:** F-X14
**What:** Seller reports a customer disputed a purchase after downloading a digital product. Despite seller providing evidence that download had occurred, funds were refunded and seller was charged fees.
**Verbatim snippet:** "One time, a customer disputed a purchase after downloading my digital product; despite providing evidence that the download had already occurred, the funds were refunded and I was still charged the associated fees."
**Source:** https://www.trustpilot.com/review/payhip.com
**source_type:** unknown
**verification_status:** direct_verified
**Date:** May 19, 2025
**Notes:** Public review/complaint site; no dedicated taxonomy value in current schema. OUT OF SCOPE: D2 (seller voice), not D4. Reviewer: Nguyễn Minh Khang. Location: VN (Vietnam). Star rating: 3 out of 5. Speaker is a seller describing buyer behavior from the seller's perspective. Per direction-specific rule 2: seller describing buyer action = D2. The observation that a buyer successfully disputed and received a refund after downloading is buyer behavior data but reported through seller lens.

---

### F-X15: Payhip custom checkout questions documentation — outside time window

**Finding ID:** F-X15
**What:** Payhip collects "the bare minimum information from your customers during the checkout process (for digital products, that's the email address only)." States this is "great for conversion - the less hurdles customers face during checkout, the better for your conversion rate." Warns "The more fields that customers are forced to fill out, the more likely it is that they'll drop out and not complete their purchase."
**Verbatim snippet:** "We collect the bare minimum information from your customers during the checkout process (for digital products, that's the email address only). This is great for conversion - the less hurdles customers face during checkout, the better for your conversion rate. [...] Most sellers do not need to ask their customers additional questions during checkout. The more fields that customers are forced to fill out, the more likely it is that they'll drop out and not complete their purchase."
**Source:** https://help.payhip.com/article/128-custom-checkout-questions
**source_type:** platform_doc
**verification_status:** direct_verified
**Date:** Updated January 15, 2022
**Notes:** Platform documentation; content is current and page is live, but last updated January 2022, outside the April 2025 — April 2026 time window. Contains Payhip's stated design philosophy about buyer checkout friction. Five custom question types available: Short Text, Multiple Choice, Yes/No, Dropdown, Legal. Name collection available via separate checkbox (not a custom question). [...] marks indicate non-contiguous excerpts within the same article.

---

# 6. Research QA Notes

**Coverage assessment:**
- Buyer-voice data for Payhip is structurally scarce. Only 2 confirmed buyer reviews exist within the April 2025 — April 2026 window (both on Trustpilot). Zero buyer-voice content was found on Reddit, YouTube, Twitter/X, Quora, or any other social media within the window. This scarcity is consistent with Payhip's architecture: no centralized marketplace, buyers arrive via seller-shared direct links, and buyers associate their purchase with the creator rather than the platform.
- One Side7 forum post (F-P02, Jun 2025) explicitly articulates this dynamic: "I see more seller than buyer review posts. And very little buyer interaction."
- The expected output shape (2–6 clean, 3–8 provisional, 10–15 could not verify) was met: 6 clean, 4 provisional, 15 could not verify / out-of-scope. Direction is heavy on Part 4 as predicted.

**Verification integrity:**
- All Clean findings (F-01 through F-06) were verified via direct page fetch with full or partial text visible.
- F-02 is truncated at the source (Trustpilot "See more" JavaScript barrier); the truncated text is directly verified. The expanded text (F-P01) is classified Provisional because it was captured from Google's search index, not from a direct page fetch.
- F-03 (SimilarWeb) contains data displayed as labeled dashboard fields, not narrative prose. The verbatim snippet uses [...] to indicate non-contiguous data fields from the same single-page view. All values captured character-for-character as displayed.

**Source_type notes:**
- Trustpilot and Sitejabber reviews classified as source_type "unknown" per shard rules: "Public review/complaint site; no dedicated taxonomy value in current schema."
- Side7 forum post (F-P02) classified as "blog" (closest available enum value); actual format is user-generated forum post.
- SimilarWeb and SEMrush classified as "report" (third-party analytics data).
- All Payhip help articles classified as "platform_doc."

**Cross-source discrepancies:**
- SimilarWeb (March 2026) reports 6.8M total visits for payhip.com. SEMrush (February 2026) reports 10.55M visits. Discrepancy (~55%) reflects different estimation methodologies. Neither is verified first-party data.
- SimilarWeb session duration (00:02:55, March 2026) differs significantly from SEMrush session duration (08:04, February 2026). SEMrush figure may include seller dashboard sessions; methodological differences are likely.
- Trustpilot review count varied between page fetches: 359 on one fetch, 406 on another, reflecting dynamic Trustpilot display behavior.
- Trustpilot aggregate rating: 4.4/5 on one fetch (359 reviews), 4.5/5 on another (406 reviews). These aggregate scores are NOT buyer satisfaction metrics — the overwhelming majority (~99%) of Trustpilot reviews are from sellers.

**Buyer-speaker test application:**
- F-01: Passed — "I bought a WordPress plugin from Payhip."
- F-02/F-P01: Passed — expanded text contains "I purchased a digital product (BOTT Price Action Indicator) for USD 499."
- F-X01: Passed — "My 7 year old son has saved up... to purchase a Boeing 737 pack." (Out of window.)
- F-X02: Passed — "I bought a set of books." (Out of window.)
- F-P02: Failed — speaker is a seller asking about buyers. Included because observation about buyer interaction scarcity is behavioral ecosystem data, not seller sales experience.
- F-X13, F-X14: Failed — sellers describing buyer actions. Classified as D2 voice, moved to Part 4.

**Key qualifiers preserved across findings:**
- Product types: WordPress plugin (F-01), digital trading indicator (F-P01), Roblox game asset (F-X01), ebook collection (F-X02)
- Prices with currency: USD 499 (F-P01), £35 GBP (F-X01)
- Buyer locations: Italy (F-01), Malta (F-X01), Great Britain (F-X02)
- Discovery channels: seller-promoted Payhip link (F-P01), direct purchase link (F-05 platform design)
- Purchase outcomes: satisfied (F-01), refund denied / scammed (F-P01), undelivered / scammed (F-X01), incomplete delivery (F-X02)
- Aggregate stats: 6.8M visits, 41.48% bounce rate, 4.38 pages/visit, 00:02:55 avg duration, 55.87% direct traffic, 58.77% male audience, 18–24 largest age group, US 38.5% top country (F-03, March 2026, SimilarWeb estimated)

**What was not found (structured absences):**
- No Reddit buyer voice (F-X03)
- No YouTube buyer voice (F-X04)
- No Twitter/X buyer voice (F-X05)
- No BBB listing (F-X06)
- No aggregate conversion rate (F-X07)
- No aggregate AOV (F-X08)
- No aggregate cart abandonment rate (F-X09)
- No buyer satisfaction/NPS data (F-X10)