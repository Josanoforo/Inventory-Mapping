# DG Run — Lemon Squeezy × D2: Seller Experience and Workarounds

**Shard scope:** Lemon Squeezy only. Seller experience and workarounds only.
**Time window:** April 2025 – April 2026
**Run date:** April 14, 2026

---

## 1. Search Decomposition

### SD-01
**Query:** `site:reddit.com "lemon squeezy" seller experience 2025` and variants targeting r/SaaS, r/indiehackers, r/Entrepreneur, r/SideProject, r/microsaas
**Target:** Reddit seller discussions within time window
**Result:** Zero Reddit URLs returned across 15+ query variations. Direct Reddit URLs blocked by fetch tool. old.reddit.com, libreddit, pullpush.io, arctic-shift mirrors all blocked.

### SD-02
**Query:** `site:news.ycombinator.com "lemon squeezy" 2025` and `site:news.ycombinator.com lemonsqueezy seller`
**Target:** Hacker News threads with seller voice
**Result:** Multiple threads found and fetched. Two substantive seller comments verified (ninefoxgambit, ben_makes_stuff). One comment (omnimus) could not be located.

### SD-03
**Query:** `site:indiehackers.com "lemon squeezy" 2025` and `site:indiehackers.com "lemonsqueezy" revenue`
**Target:** Indie Hackers posts with seller experience within window
**Result:** Major IH posts about LS predate April 2025 (e.g., "200+ paying customers" post ~Oct/Nov 2024). No in-window IH posts confirmed.

### SD-04
**Query:** `site:medium.com "lemon squeezy" seller experience 2025` and `site:medium.com "lemon squeezy" revenue income 2025`
**Target:** Medium articles by sellers describing LS experience
**Result:** Two articles found within window: Hazel Paradise (Mar 2026, accessible), Muhammad Wani (Dec 2025, paywalled).

### SD-05
**Query:** `site:substack.com "lemon squeezy" seller 2025`
**Target:** Substack posts by founders describing LS experience
**Result:** No in-window Substack posts found with direct seller experience.

### SD-06
**Query:** `site:youtube.com "lemon squeezy" seller experience review 2025`
**Target:** YouTube transcripts of indie hacker interviews mentioning LS
**Result:** No direct seller experience video transcripts found within window.

### SD-07
**Query:** `twitter.com OR x.com "lemon squeezy" seller revenue 2025`
**Target:** X/Twitter posts by sellers about LS experience
**Result:** One post identified (Surjith S M, payout stopped due to tax form) but full content not directly verifiable (X requires JavaScript rendering).

### SD-08
**Query:** `"lemon squeezy" seller experience revenue blog 2025 2026` and `"lemon squeezy" review seller frustration workaround 2025`
**Target:** Blog posts by founders describing LS experience
**Result:** One substantive blog found: Velox Themes (March 2026), first-person seller comparing Polar, LS, Gumroad. Fully accessible.

### SD-09
**Query:** `site:trustpilot.com lemonsqueezy.com reviews`
**Target:** Trustpilot reviews from LS sellers
**Result:** Multiple pages fetched (pages 1–4). ~40+ reviews within window identified; filtered to seller-perspective reviews only. Many reviews truncated on page behind "See more" button.

### SD-10
**Query:** `"lemon squeezy" fees "merchant of record" seller experience 2025` and `"lemon squeezy" workaround limitation seller 2025`
**Target:** Broader web for seller experience content
**Result:** Product Hunt reviews page found with in-window seller reviews. Competitor comparison articles found but excluded as secondary retellings.

---

## Part 1 — Clean Findings (direct_verified)

### F-01

**What:** Seller used Lemon Squeezy from January 2024 to August 2025 to sell Framer templates. Reports the experience was mostly positive, with a good-looking dashboard and helpful built-in tools like email marketing and affiliate tracking.

**Verbatim snippet:** "From January 2024 to August 2025, I used Lemon Squeezy to sell my Framer templates. The experience was mostly positive. The dashboard looked great, and the built-in tools like email marketing and affiliate tracking were definitely helpful."

**Source:** https://veloxthemes.com/blog/polar-vs-lemonsqueezy-vs-gumroad
**source_type:** blog
**verification_status:** direct_verified
**Date:** March 24, 2026
**Notes:** Author identified as Widya Bayu W, Co-founder of Velox Themes. Product type: Framer templates. Platform tenure: January 2024 to August 2025.

---

### F-02

**What:** Seller had to wait about a week for Lemon Squeezy to approve a new account in January 2025. To avoid holding off a release, seller switched to Gumroad to start selling right away. Once the Lemon Squeezy store was approved, seller moved everything back over because Gumroad fees felt high.

**Verbatim snippet:** "In January 2025, I started building a dedicated store for a new set of Framer templates. That's when I hit my first roadblock. I had to wait about a week for Lemon Squeezy to approve my account. During that time, I couldn't launch or sell anything. To avoid holding off my release, I switched to Gumroad so I could start selling right away. Gumroad worked well. It was easy to set up, and I liked the clean interface. But the fees felt a bit high. So once my Lemon Squeezy store was approved, I moved everything back over."

**Source:** https://veloxthemes.com/blog/polar-vs-lemonsqueezy-vs-gumroad
**source_type:** blog
**verification_status:** direct_verified
**Date:** March 24, 2026
**Notes:** Separate continuous passage from the same URL as F-01. Workaround: temporary Gumroad use during LS approval wait. Tools used outside platform: Gumroad.

---

### F-03

**What:** Seller wanted to know exactly where each sale came from, down to the campaign or ad that drove it. Neither Lemon Squeezy nor Gumroad could fully deliver this feature. Seller discovered Polar and switched.

**Verbatim snippet:** "As my store grew and I started running more campaigns, I realized I needed something more from a Merchant of Record. I was looking for one specific feature that neither Lemon Squeezy nor Gumroad could fully deliver. I wanted to know exactly where each sale came from, down to the campaign or ad that drove it. That's when I discovered Polar."

**Source:** https://veloxthemes.com/blog/polar-vs-lemonsqueezy-vs-gumroad
**source_type:** blog
**verification_status:** direct_verified
**Date:** March 24, 2026
**Notes:** Separate continuous passage from the same URL. Describes the specific analytics limitation that drove the platform switch. Tools used outside platform: Polar.

---

### F-04

**What:** Seller reports Lemon Squeezy requires account approval that can take several days to over a week, support is very slow, and there have been a lot of recent bugs including people being unable to check out and customers getting double-charged.

**Verbatim snippet:** "The downside: you can't start selling immediately. Lemon Squeezy requires account approval, which can take several days to over a week, and their support is very slow. There have also been a lot of recent bugs, like people being unable to check out and customers getting double-charged."

**Source:** https://veloxthemes.com/blog/polar-vs-lemonsqueezy-vs-gumroad
**source_type:** blog
**verification_status:** direct_verified
**Date:** March 24, 2026
**Notes:** Separate continuous passage from the same URL. "Recent bugs" is the author's characterization; article does not specify dates for the bugs described.

---

### F-05

**What:** Seller uses Lemon Squeezy for selling digital products on a faceless YouTube account and reports conversion rates are really good.

**Verbatim snippet:** "This is what I am using lately. I mainly use this for selling digital products on my faceless YouTube account. I really love this because conversion rates are really good."

**Source:** https://medium.com/@hazelparadise/gumroad-vs-payhip-vs-lemon-squeezy-71cec796cba3
**source_type:** blog
**verification_status:** direct_verified
**Date:** Accessed April 2026; page header displays "Mar, 2026"
**Notes:** Author identified as Hazel Paradise, "Writer of 90+ books under multiple pen names," 36K followers on Medium. No specific revenue figures attributed to Lemon Squeezy in this passage. Product type: digital products (ebooks). Channel: faceless YouTube.

---

### F-06

**What:** Seller reports Lemon Squeezy does not tell where traffic is coming from, analytics is very basic, there are no categories (seller sells in two niches and categorizing them becomes difficult), no cross-selling or upselling, and email marketing is a little costly.

**Verbatim snippet:** "Some features I want so that this platform can become better — Source — Doesn't tell where the traffic is coming from. Analytics is very basic. No categories. I sell in two niches, and categorizing them becomes difficult. No cross-selling or upselling. Email marketing is a little costly."

**Source:** https://medium.com/@hazelparadise/gumroad-vs-payhip-vs-lemon-squeezy-71cec796cba3
**source_type:** blog
**verification_status:** direct_verified
**Date:** Accessed April 2026; page header displays "Mar, 2026"
**Notes:** Separate continuous passage from the same URL as F-05. Original formatted as a bulleted list in source; presented here as sequential text. Seller operates in two niches.

---

### F-07

**What:** Seller sells templates for a living and has used several payment providers. Reports Lemon Squeezy was very popular until being acquired by Stripe, is full of serious bugs with bad support, has lovely design and slightly better fees than Gumroad but many hidden fees. Would still use over Gumroad because Gumroad checkout design loses sales. Reports most creators abandoning Lemon Squeezy are moving to Polar.sh.

**Verbatim snippet:** "I sell templates for a living and have used several of these providers. The main options are Gumroad - high fees and ugly design, solid system never had issues does most what I need. Lemon Squeezy - it was very popular until being acquired by stripe. Full of serious bugs, bad support. Lovely design, slightly better fees than Gumroad, but many hidden. Would still use over Gumroad just cause the Gumroad checkout design is so bad it loses sales imo. Paddle - haven't used it but I think it's probably as good as Gumroad or Lemon. Polar.sh - the trendy new option, most creators abandoning Lemon Squeezy are moving there. Has lots of innovation in features beyond payments such as selling private GitHub access. All of these platforms are MOR as far as I know, all provide the checkout UI etc. all handle digital asset file delivery. They are perfect for creators selling digital products that want a turn key solution and don't want to do any development work."

**Source:** https://news.ycombinator.com/item?id=43606206
**source_type:** seller_forum
**verification_status:** direct_verified
**Date:** Accessed April 2026; displayed as "11 months ago," approximately May 2025
**Notes:** Comment in thread "Gumroad's Interestingly Timed 'Open-Source' Play." Date approximated from relative timestamp ("11 months ago" from April 14, 2026). Product type: templates. HN classified as seller_forum (forum where founders and indie sellers discuss tools).

---

### F-08

**What:** Seller used to sell a digital product through Lemon Squeezy. Reports it was full of bugs, the fees were high, and payouts were slow. When seller switched to Stripe, started saving money and got paid faster. Built DownloadPage to simplify selling digital downloads via Stripe.

**Verbatim snippet:** "Hey HN, I'm Ben, the founder of DownloadPage Let me share a quick story... I used to sell a digital product through Lemon Squeezy. It was full of bugs, the fees were high, and payouts were slow. When I switched to Stripe, I started saving money and got paid faster. The only problem? Selling directly meant stitching together a bunch of tools just to deliver a file. So I built DownloadPage to make it simple. You connect Stripe, upload your product, and share a link. That's it. If you're tired of giving up a cut to your payment processor, this is for you! Let me know what you think. P.S. I'll personally do the work of migrating you from your old payment processor to DownloadPage via Stripe! Free white-glove service is included with all plans."

**Source:** https://news.ycombinator.com/item?id=44296422
**source_type:** seller_forum
**verification_status:** direct_verified
**Date:** Accessed April 2026; displayed as "10 months ago," approximately June 2025
**Notes:** Show HN post. Seller is also promoting their own alternative product (DownloadPage). The LS critique serves as motivation for building a competing tool. Date approximated from relative timestamp. Tools used outside platform: Stripe, DownloadPage. Workaround: migrated to Stripe and built custom delivery layer.

---

### F-09

**What:** Seller wanted to publish an e-book with more than 10 customers waiting. Reports identity verification has not been completed for over 3 weeks. Contacted support twice with no response.

**Verbatim snippet:** "Wanted to publish an e-book, with more than 10 customers waiting, but they are not verifying my identity for over 3 weeks now. Contacted support twice, never got a response. Horrible."

**Source:** https://www.trustpilot.com/review/lemonsqueezy.com
**source_type:** buyer_review
**verification_status:** direct_verified
**Date:** January 9, 2026
**Notes:** Trustpilot review by Amer Brcaninovic, rated 1 star. Full review text visible on page (not truncated). source_type classified as buyer_review (closest taxonomy match for review-platform content); reviewer is a seller, not a product buyer. Product type: e-book. Audience: 10+ waiting customers.

---

### F-10

**What:** Seller has been trying to transfer money from the store for 3 months. Reports customer support is slow and deflects questions.

**Verbatim snippet:** "I've been trying to transfer my money from the store for 3 months now. Customer support is slow and just deflects the questions. Stay away."

**Source:** https://www.trustpilot.com/review/lemonsqueezy.com
**source_type:** buyer_review
**verification_status:** direct_verified
**Date:** August 27, 2025
**Notes:** Trustpilot review by Marko Žužić, rated 1 star. Full review text visible on page (not truncated). source_type classified as buyer_review; reviewer is a seller (references "the store" and transferring money). Time period for payout issue: 3 months.

---

### F-11

**What:** Seller reports payout has been failing for 3 months. Lemon Squeezy did not reply, did not show any initiative, and is completely silent.

**Verbatim snippet:** "payout has been failing for 3 months, and Lemon Squeezy did nothing, did not reply, didn't show any initiative, they are completely silent as if they closed the shop!"

**Source:** https://www.trustpilot.com/review/lemonsqueezy.com?page=3
**source_type:** buyer_review
**verification_status:** direct_verified
**Date:** March 14, 2026
**Notes:** Trustpilot review by MUSTAKIM MASUM, rated 1 star. Full review text visible on page (not truncated). source_type classified as buyer_review; reviewer is a seller (receiving payouts). Time period for payout failure: 3 months.

---

### F-12

**What:** Solo developer selling globally chose Lemon Squeezy because the Merchant of Record model handles VAT, GST, and sales tax compliance across 50+ countries. Reports getting a clean payout. Notes Lemon Squeezy's setup was simpler than Paddle and dashboard is cleaner for a one-product business. The license key generation API integrates cleanly with a custom activation system on Cloudflare Workers.

**Verbatim snippet:** "Merchant of record was the dealbreaker. As a solo developer selling globally, I didn't want to handle VAT, GST, and sales tax compliance across 50+ countries myself. Lemon Squeezy handles all of that as the merchant of record — they collect the tax, file the returns, and I get a clean payout. Stripe is more flexible but puts the tax burden on me. Paddle was the other serious option but Lemon Squeezy's setup was simpler and their dashboard is cleaner for a one-product business. The license key generation API also integrates cleanly with my custom activation system on Cloudflare Workers."

**Source:** https://www.producthunt.com/products/lemon-squeezy/reviews
**source_type:** buyer_review
**verification_status:** direct_verified
**Date:** Accessed April 2026; page displays "7d ago," approximately April 7, 2026
**Notes:** Product Hunt review by DΛX | VibeSonic.ai. source_type classified as buyer_review (closest taxonomy match for review-platform content); reviewer is a seller/developer using LS. Date approximated from relative timestamp ("7d ago" from April 14, 2026). Product type: software (VibeSonic). Geographic scope: global. Alternatives considered: Stripe, Paddle, FastSpring.

---

## Part 2 — Provisional Findings (blocked_url_index_verified)

No provisional findings captured.

All six strategies for accessing Reddit content via mirrors failed (old.reddit.com, libreddit, pullpush.io, arctic-shift, Google cache, web search for cached pages). No mirror, archive, or cache of any Reddit URL was successfully accessed. Twitter/X content could not be recovered via mirrors. No other blocked URLs were recovered via alternate access methods.

---

## Part 3 — Pattern Candidates (sealed)

### PC-01
**Candidate statement:** Multiple sellers report account approval or identity verification delays ranging from days to multiple weeks, during which they cannot sell.
**Related Finding IDs:** F-02, F-04, F-09
**Status:** sealed; not validated

### PC-02
**Candidate statement:** Multiple sellers report frozen funds, failed payouts, or inability to withdraw earned money for periods of months.
**Related Finding IDs:** F-10, F-11
**Status:** sealed; not validated

### PC-03
**Candidate statement:** Multiple sellers describe migrating from Lemon Squeezy to alternative platforms including Polar, Stripe, and Gumroad, citing bugs, fees, analytics limitations, or support issues as reasons.
**Related Finding IDs:** F-02, F-03, F-07, F-08
**Status:** sealed; not validated

### PC-04
**Candidate statement:** Multiple sellers report that Lemon Squeezy lacks granular traffic source or campaign attribution analytics, and describe this as a limitation that affects marketing decisions.
**Related Finding IDs:** F-03, F-06
**Status:** sealed; not validated

---

## Part 4 — Could Not Verify / Out-of-Scope

### F-X01: Francesco P. — Account flagged for alleged fraud after low-risk onboarding

**What:** Seller reports signing up, being told the business was low risk, and being onboarded without issues. After receiving payments from customers for services fully delivered, Lemon Squeezy flagged the account for "alleged fraud," refunded customers without investigation, and closed the account.

**Verbatim snippet:** "I had a very bad experience with LemonSqueezy. When I signed up, they reviewed my business, told me it was low risk, and onboarded me without issues. After receiving payments from customers – for services I fully delivered – LemonSqueezy suddenly flagged my account for "alleged fraud." They refunded my customers without any proper investigation and then closed my account. This left me without the money I had legitimately earned, even though I had done everything as agreed. To me, this looks like a full scam: they take your payments, then shut you down and keep you stuck with nothing."

**Source:** https://www.trustpilot.com/review/lemonsqueezy.com?page=3
**source_type:** buyer_review
**verification_status:** could_not_verify
**Date:** September 6, 2025
**Notes:** Degraded to could_not_verify. The directly fetched Trustpilot page displayed the review truncated behind a "See more" button; the full text above was obtained from a search engine snippet attributed to the same URL. Because the full continuous passage was not visible on the directly rendered page, conservative assignment applies. Reviewer appears to be a seller (received payments for services delivered).

---

### F-X02: Terry Mark — Store shut down, payouts over $3,500 frozen

**What:** Seller reports Lemon Squeezy abruptly shut down the store, froze payouts over $3,500, and is refunding all customers even though all products were delivered with zero chargebacks.

**Verbatim snippet:** "Lemon Squeezy abruptly shut down my store, froze my payouts (over $3,500), and is now refunding all my customers even though all products were delivered, with zero chargebacks, zero compl"

**Source:** https://www.trustpilot.com/review/lemonsqueezy.com
**source_type:** buyer_review
**verification_status:** could_not_verify
**Date:** May 26, 2025
**Notes:** Degraded to could_not_verify. Review text truncated on Trustpilot page behind "See more" button; snippet ends mid-word. Visible portion only. Revenue figure: over $3,500 in frozen payouts. Reviewer is a seller (references "my store," "my payouts," "my customers").

---

### F-X03: Bernhard — Processed thousands of dollars, migrating away due to support

**What:** Seller used Lemon Squeezy to process thousands of dollars in payments. Reports almost no customer support; when problems arise, waits days between emails and most replies show the person has not understood the problem. Reports the tech is great but support makes it no longer an option; migrating products to other payment processors.

**Verbatim snippet:** "There is almost no customer support. I used them to process thousands of dollars in payments and everything ran kinda smooth, but when there is any problem, I wait days between emails, and most of them are just evident that the person has not really understood your problem or situation... Their tech is great, but with nearly non-existent customer support, they are not an option anymore for a payment processor, and we're migrating our products to other payment processors."

**Source:** https://www.trustpilot.com/review/lemonsqueezy.com?page=2
**source_type:** buyer_review
**verification_status:** could_not_verify
**Date:** December 8, 2025
**Notes:** Degraded to could_not_verify. The directly fetched Trustpilot page showed the review truncated behind "See more"; full text above obtained from search engine snippet attributed to the same URL. Reviewer is a seller (processed payments, migrating products). Revenue: "thousands of dollars."

---

### F-X04: Jay Shenawy — Moved to LS expecting reliability, reports nightmare with 4 active paying clients

**What:** Seller moved to Lemon Squeezy because of the Stripe acquisition, expecting a reliable platform. Reports it has been a nightmare. Has 4 active paying clients.

**Verbatim snippet:** "I moved to Lemon Squeezy because they were acquired by Stripe, expecting a reliable platform. It has been a nightmare. I have 4 active paying clients and my Lemon Squeezy dashboard"

**Source:** https://www.trustpilot.com/review/lemonsqueezy.com
**source_type:** buyer_review
**verification_status:** could_not_verify
**Date:** February 4, 2026
**Notes:** Degraded to could_not_verify. Review truncated on Trustpilot page behind "See more"; snippet ends mid-sentence. Reviewer is a seller (has paying clients, references dashboard). Client count: 4 active paying clients.

---

### F-X05: Jak Warner — Denied for "prohibited items" when selling code component; building competitor

**What:** Seller switching from WordPress to Framer, writing a code component to sell on the Framer marketplace. Framer suggested Lemon Squeezy. After sign-up, seller was denied for selling "prohibited items" because seller also runs an IT services company. Seller reports working on writing a competitor for Lemon Squeezy based on Stripe.

**Verbatim snippet:** "I am switching from WordPress to Framer and was writing a code component to give out for a few bucks on the framer marketplace. Framer suggested Lemon Squeezy, did my sign up and then a couple days la"

**Source:** https://www.trustpilot.com/review/lemonsqueezy.com
**source_type:** buyer_review
**verification_status:** could_not_verify
**Date:** November 4, 2025
**Notes:** Degraded to could_not_verify. Review truncated on Trustpilot page behind "See more"; snippet ends mid-word. What field includes details from search engine snippet of the same URL that displayed more text, but the directly rendered page truncated the review. Reviewer is a seller (attempted). Product type: code component for Framer.

---

### F-X06: Rita Michiels — Reports 90% of store applications declined post-acquisition

**What:** Seller reports that since Lemon Squeezy was bought by Stripe, micro management has gotten awful. States "you will most likely not be able to create a store here" and that they decline 90% of the store applications.

**Verbatim snippet:** "It seems since they were bought by Stripe that their micro management has gotten awful. Take my words for this, you will most likely not be able to create a store here. They decline 90% of the store"

**Source:** https://www.trustpilot.com/review/lemonsqueezy.com
**source_type:** buyer_review
**verification_status:** could_not_verify
**Date:** August 2, 2025
**Notes:** Degraded to could_not_verify. Review truncated on Trustpilot page behind "See more"; snippet ends mid-sentence. The "90%" figure is the reviewer's claim; no source for that statistic is visible. Reviewer is a seller (attempted store creation).

---

### F-X07: Reiff Lorenz — Week of setup, rejected after video demo, built Shopify store in 4 hours

**What:** Seller spent a week setting up a LemonSqueezy account and loading digital files. Jumped through verification hoops. After 3 days waiting for account activation, was told a video demonstration was required. Provided it. Then 4 more days to decide the seller was not approved. No explanation, no appeal process. Seller abandoned LS and built a working Shopify account with fully functional payments in 4 hours.

**Verbatim snippet:** "I spent a week setting up a LemonSqueezy account and loading the digital files I was selling. Jumped through all the verification hoops. After 3 days of waiting for account activation, they said a v"

**Source:** https://www.trustpilot.com/review/lemonsqueezy.com
**source_type:** buyer_review
**verification_status:** could_not_verify
**Date:** November 11, 2025
**Notes:** Degraded to could_not_verify. Review truncated on Trustpilot page behind "See more"; snippet ends mid-word. What field includes details from search engine snippet of the same URL. Reviewer is a seller (loaded digital files for sale). Tools used outside platform: Shopify.

---

### F-X08: Ruben Milland — Shop terminated for selling digital e-books

**What:** Seller reports that Lemon Squeezy will terminate shops for selling digital e-books, saying it is a risk to their card processor.

**Verbatim snippet:** "Stay away, stay away, just stay away... they will terminate your shop for selling digital e-books and say its a risk to their card processor..."

**Source:** https://www.trustpilot.com/review/lemonsqueezy.com
**source_type:** buyer_review
**verification_status:** could_not_verify
**Date:** October 4, 2025
**Notes:** Degraded to could_not_verify. The trailing ellipsis may be author punctuation or platform truncation; cannot confirm whether additional text exists behind a "See more" element. Conservative assignment applied. Reviewer is a seller (references "your shop," selling digital e-books). Product type: digital e-books.

---

### F-X09: Soukaina Ait oumghar — Frozen money, rejected information

**What:** Seller reports frozen money. Lemon Squeezy refuses to release it, claiming information is rejected. Platform also refuses to let the seller rewrite the information.

**Verbatim snippet:** "This was truly a bad experience with this website. They've frozen my money and refuse to release it, claiming my information is rejected. They also refuse to let me rewrite it."

**Source:** https://www.trustpilot.com/review/lemonsqueezy.com
**source_type:** buyer_review
**verification_status:** could_not_verify
**Date:** January 26, 2026
**Notes:** Degraded to could_not_verify. Full review text visible on page. However, it is unclear from the review text alone whether this reviewer is a seller or a buyer of products sold through LS. "Frozen my money" could refer to seller payouts or buyer refund disputes. Conservative assignment applied due to ambiguous seller identity.

---

### F-X10: Surjith S M — Payout stopped due to Stripe tax form; PAN not accepted

**What:** Seller reports Lemon Squeezy stopped payout because of a Stripe tax form. LS is not accepting the seller's PAN. Seller emailed support 1 month ago with no reply. Seller checked with Polar and reports they did not have this requirement.

**Verbatim snippet:** "Lemon Squeezy stopped my payout because of stripe tax form. They are not accepting my PAN. I already emailed support 1 month ago and no reply yet. I checked with @polar_sh and they didn't have this requirement."

**Source:** https://x.com/surjithctly/status/2000472787455275191
**source_type:** unknown
**verification_status:** could_not_verify
**Date:** Accessed April 2026; exact post date not confirmed
**Notes:** Degraded to could_not_verify. X/Twitter requires JavaScript rendering; snippet obtained from search result preview, not from direct page access. URL not directly fetched. source_type listed as unknown (Twitter is not in the shard's allowed source_type list). Seller likely located in India (PAN is an Indian tax identifier). Tools used outside platform: Polar.

---

### F-X11: omnimus — Lemon Squeezy more expensive than Paddle for EU-based sellers

**What:** No data found on this comment. A finding attributed to HN user "omnimus" at item?id=43340960 about Lemon Squeezy being more expensive than Paddle for EU-based sellers, with hidden fees and USD-only payouts causing exchange fees, could not be located.

**Verbatim snippet:** n/a — absence finding

**Source:** Searched: https://news.ycombinator.com/item?id=43340960 (not found), web search for "omnimus lemon squeezy expensive EU" (no results), Algolia HN search for "omnimus lemonsqueezy" (no results)
**source_type:** unknown
**verification_status:** could_not_verify
**Date:** n/a
**Notes:** HN item ID 43340960 could not be located through any search method. The comment may have been deleted, flagged, or the item ID may be incorrect. Cannot confirm existence, authorship, or content.

---

### F-X12: Muhammad Wani — Processed $10K through Stripe, Paddle, and Lemon Squeezy

**What:** Seller reports using all three payment processors (Stripe, Paddle, Lemon Squeezy) for a SaaS with $20–60/month subscription plans. Reports measuring setup difficulty, tax handling, payment success rates, fees, dashboard usability, and customer experience.

**Verbatim snippet:** "I've used all three payment processors for my SaaS. Started with Stripe. Switched to Paddle. Tested Lemon Squeezy. Each processed real customer payments. Here's what I learned when actual money was on the line. My SaaS: Subscription product. $20–60/month plans. What I measured: Setup difficulty · Tax handling · Payment success rates · Fees · Dashboard usability · Customer experience · Not theory. Real customers. Real money."

**Source:** https://medium.com/@muhammadwaniai/stripe-vs-paddle-vs-lemon-squeezy-i-processed-10k-through-each-heres-what-actually-matters-27ef04e4cb43
**source_type:** blog
**verification_status:** could_not_verify
**Date:** December 12, 2025
**Notes:** Degraded to could_not_verify. Article is behind Medium member-only paywall; only introductory text accessible. Full LS-specific findings, conclusions, and fee comparisons not visible. Snippet is from the accessible preview portion only. Revenue: $10K processed through each platform. Product: SaaS subscription, $20–60/month plans.

---

### F-X13: Reddit r/SaaS Lemon Squeezy threads — Inaccessible

**What:** No data found on Reddit seller discussions about Lemon Squeezy within the time window. Multiple known threads in r/SaaS, r/Entrepreneur, r/microsaas, and r/SideProject could not be accessed.

**Verbatim snippet:** n/a — absence finding

**Source:** Searched: 15+ query variations including site:reddit.com "lemon squeezy" 2025, site:reddit.com/r/SaaS "lemon squeezy," reddit "lemon squeezy" seller payout fees 2025. Also attempted: old.reddit.com, libreddit.kavin.rocks, search.pullpush.io, arctic-shift.photon-reddit.com, Google cache — all blocked.
**source_type:** unknown
**verification_status:** could_not_verify
**Date:** n/a
**Notes:** Zero Reddit URLs returned by any search engine query. Direct fetch of Reddit URLs blocked by tool permissions. All six mirror/archive strategies failed. Known threads referenced in third-party sources (r/SaaS/comments/1bywbqh, r/SaaS/comments/1b3sf2l) appear to predate April 2025 based on post IDs. Cannot confirm or deny existence of in-window Reddit seller discussions.

---

### F-X14: Indie Hackers — No in-window seller findings confirmed

**What:** No data found on Indie Hackers seller discussions about Lemon Squeezy within April 2025 – April 2026. Major known IH posts ("200+ paying customers and endless headaches") predate the time window (approximately October/November 2024).

**Verbatim snippet:** n/a — absence finding

**Source:** Searched: site:indiehackers.com "lemon squeezy" 2025, site:indiehackers.com "lemonsqueezy" revenue, indiehackers.com/search?q=lemon+squeezy
**source_type:** unknown
**verification_status:** could_not_verify
**Date:** n/a
**Notes:** IH does not display clear timestamps in search results. Some IH pages are behind login walls. It is possible in-window comments exist on older posts but could not be confirmed.

---

### F-X15: YouTube transcripts — No seller experience findings

**What:** No data found on YouTube video transcripts containing direct Lemon Squeezy seller experience content within the time window.

**Verbatim snippet:** n/a — absence finding

**Source:** Searched: site:youtube.com "lemon squeezy" seller experience review 2025, "lemon squeezy" youtube seller income 2025
**source_type:** unknown
**verification_status:** could_not_verify
**Date:** n/a
**Notes:** Search returned review/tutorial videos but none with verifiable seller-voice transcripts containing personal experience within the time window.

---

## Research QA Notes

### Findings forced to Provisional and reasons
- None. Zero findings met blocked_url_index_verified criteria because no mirror, cache, or archive access succeeded for any blocked URL.

### Findings degraded to could_not_verify and reasons
- **F-X01 (Francesco P.):** Full text obtained from search engine snippet of the Trustpilot URL, but directly fetched page showed truncated text. Degraded because the full continuous passage was not visible on the rendered page.
- **F-X02 (Terry Mark):** Review truncated mid-word on fetched Trustpilot page. Snippet cannot form a complete verbatim passage.
- **F-X03 (Bernhard):** Full text from search snippet; directly fetched page was truncated. Degraded for same reason as F-X01.
- **F-X04 (Jay Shenawy):** Review truncated mid-sentence on fetched page.
- **F-X05 (Jak Warner):** Review truncated mid-word on fetched page.
- **F-X06 (Rita Michiels):** Review truncated mid-sentence on fetched page.
- **F-X07 (Reiff Lorenz):** Review truncated mid-word on fetched page.
- **F-X08 (Ruben Milland):** Trailing ellipsis ambiguity (author punctuation vs. platform truncation).
- **F-X09 (Soukaina Ait oumghar):** Ambiguous seller identity; cannot confirm from review text alone whether reviewer is seller or buyer.
- **F-X10 (Surjith S M):** X/Twitter URL not directly fetched; snippet from search preview only.
- **F-X11 (omnimus):** HN item not locatable.
- **F-X12 (Muhammad Wani):** Medium paywall blocked full article.

### Findings degraded due to URL not fixable
- F-X11 (omnimus): Item ID 43340960 not found in HN. URL may be incorrect or content deleted.
- F-X13 (Reddit): No Reddit URLs obtained from any search query.

### Multi-speaker pages split into separate findings
- Trustpilot pages (https://www.trustpilot.com/review/lemonsqueezy.com and page=3): Multi-reviewer pages split by individual reviewer. Each finding captures one reviewer's text.
- VeloxThemes blog: Single author (Widya Bayu W) with multiple distinct passages → split into F-01, F-02, F-03, F-04 per the shard rule that separate topics from one seller = separate findings.
- Medium (Hazel Paradise): Single author with separate passages → split into F-05, F-06.
- HN thread (item?id=43604378): Multiple commenters; ninefoxgambit (F-07) isolated as the only comment with substantive seller experience within window.

### Truncated or partial sources
- 7 Trustpilot reviews (F-X01 through F-X07) were truncated on the rendered page behind a "See more" button that requires JavaScript interaction. Visible portions preserved; full text not accessible through the fetch tool.
- 1 Medium article (F-X12) behind member-only paywall; introductory text only.
- 1 X/Twitter post (F-X10) requires JavaScript rendering; snippet from search result preview only.

### source_type ambiguities
- **Trustpilot reviews (F-09, F-10, F-11, F-X01 through F-X09):** Classified as `buyer_review` (closest match from the 18-value taxonomy for review-platform content). The reviewers are sellers of digital products reviewing Lemon Squeezy as a service they used — not buyers of products sold through LS. The `buyer_review` type here describes the review format, not the reviewer's relationship to LS's end customers.
- **Product Hunt review (F-12):** Classified as `buyer_review` for the same reason. The reviewer (DΛX) is a developer/seller using LS.
- **Hacker News comments (F-07, F-08):** Classified as `seller_forum`. HN is a tech community forum, not a dedicated seller forum. The `seller_forum` type is the closest match from the taxonomy for a community forum where founders and indie sellers discuss tools and experiences.

### Coverage gaps where findings expected but not found
- **Reddit:** Expected to be a primary source per shard instructions. Zero accessible content. This is a significant coverage gap. Reddit discussions likely contain substantial seller voice content based on third-party references to Reddit sentiment.
- **Indie Hackers:** Expected per shard. No in-window findings confirmed. The platform appears to have less active LS discussion in the April 2025–April 2026 period compared to earlier.
- **YouTube:** Expected per shard. No seller-voice transcripts found within window.
- **Substack:** Expected per shard. No in-window seller experience posts found.
- **Positive seller experiences:** Clean findings skew negative (10 of 12 describe problems or limitations). Two findings (F-05, F-12) report positive experiences. This imbalance may reflect the source distribution (Trustpilot and forum complaints skew negative) rather than the full population of seller sentiment.
- **Revenue/income figures:** Only F-X02 (Terry Mark, $3,500 in frozen payouts) and F-X12 (Muhammad Wani, $10K processed) contain specific dollar amounts, and both are in Part 4. No clean finding contains a specific revenue figure. F-X03 (Bernhard, "thousands of dollars") is qualitative. This gap limits downstream revenue analysis.

### Cases where input could not be decomposed without interpretation
- The shard specifies "X/Twitter founder posts" as a search target, but Twitter/X is not in the allowed source_type list (blog, reddit, seller_forum, article, video_transcript, interview, buyer_review). F-X10 was assigned source_type `unknown` to avoid selecting an inapplicable type.
- HN comment dates are displayed as relative timestamps ("11 months ago"). Conversion to approximate calendar dates required interpretation (calculation from the access date of April 14, 2026). These dates are approximate, not exact.
- Trustpilot review pages use dynamic pagination; the same review may appear on different page numbers at different times. Source URLs reference the page as accessed at run time.

### Additional verified Trustpilot reviews not elevated to Part 1
The following Trustpilot reviews had complete text visible on the fetched page and are from confirmed or likely sellers within the time window. They were not included in Part 1 to remain near the expected output shape (5–12 clean). Their content is consistent with Part 1 findings:
- **Aziz (Jan 19, 2026):** "Yup they will take 2+ weeks to verify your identity, and if you got customers and they pay you, lemon squeezy will hold your money"
- **NM (Oct 11, 2025):** "Very bad customer service! Got transferred to multiple people they stopped replying after wasting round a month of my time. Cant Believe a reputed company behaves in this manner." (Ambiguous seller/buyer identity)

### HN findings within window but excluded from Part 1
- **kacesensitive (~May 2025):** "Lemon Squeezy is excellent" — Complete 4-word comment. Excluded from Part 1 due to insufficient substantive content for a finding (no experience detail, no revenue, no workaround, no frustration mechanism).
- **hristoff (~January 2026):** Built TrustSqueezy, a revenue verification tool for Lemon Squeezy creators. Excluded because the finding describes building a tool for the LS ecosystem, not the speaker's own selling experience on LS.

---

*End of DG run.*