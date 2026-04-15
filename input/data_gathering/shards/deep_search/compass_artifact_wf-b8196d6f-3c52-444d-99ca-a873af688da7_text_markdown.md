# Data Gathering Run — Shard: Lemon Squeezy × D3: Catalog, Discovery, and Market Signals

---

## Search Decomposition

**SD-01** — Fetch and document https://www.lemonsqueezy.com/wedge. Determine whether the page relates to catalog, discovery, or market signals.

**SD-02** — Fetch and document https://www.lemonsqueezy.com/showcase. Determine whether the page exists and what it shows (stores, products, categories, counts).

**SD-03** — Fetch and document https://docs.lemonsqueezy.com/guides. Identify any catalog or discovery mechanism content.

**SD-04** — Fetch and document https://www.lemonsqueezy.com/blog. Identify any posts containing observable catalog or market-signal data.

**SD-05** — Execute Google search `site:lemonsqueezy.com store`. Document resulting URLs, snippet text, and any observable product/store data.

**SD-06** — Identify discovery mechanisms on lemonsqueezy.com: search bars, filters, browse pages, category pages, public marketplace presence or absence. Test URLs: /store, /marketplace, /discover, /explore.

**SD-07** — Find and document public product listings on Lemon Squeezy hosted storefronts ({merchant}.lemonsqueezy.com). Capture product names, prices with currency, categories, review counts.

**SD-08** — Identify auxiliary services, tools, and third-party products built around Lemon Squeezy (SEO tools, template generators, listing optimizers, migration tools, mobile apps, integration connectors, boilerplates).

**SD-09** — Retrieve database profile entries for Lemon Squeezy from Crunchbase, G2, Capterra, BuiltWith, Wappalyzer, Ful.io, SimilarTech, Product Hunt. Extract observable catalog and market-signal metrics only.

**SD-10** — Search for reports and articles citing observable counts, price ranges, GMV, store/seller counts, or category breakdowns specific to Lemon Squeezy catalog.

**SD-11** — Determine presence or absence of a public marketplace-style discovery layer (public browse URL, indexed category pages, searchable product directory).

---

## Part 1 — Clean Findings (direct_verified)

---

**F-01**

- **Finding ID:** F-01
- **What:** Wappalyzer identifies 1,900 websites using Lemon Squeezy, categorized under payment processors.
- **Verbatim snippet:** "Get company and contact details for 1,900 Lemon Squeezy websites"
- **Source:** https://www.wappalyzer.com/technologies/payment-processors/lemon-squeezy/
- **source_type:** database_profile
- **verification_status:** direct_verified
- **Date:** April 2026
- **Notes:** Page was directly fetched and content confirmed. The 1,900 figure represents websites detected by Wappalyzer's technology crawler. Wappalyzer classifies Lemon Squeezy under "Payment processors." The same page displays geographic distribution data and a sample of top websites by traffic, but those elements are rendered in a format that may not constitute a single continuous text passage, so they are not included in this finding's verbatim.

---

**F-02**

- **Finding ID:** F-02
- **What:** A free Chrome extension called "Lemon Squeezy Fee Calculator" exists that helps users estimate fees for selling digital products on Lemon Squeezy.
- **Verbatim snippet:** "This fee calculator helps you estimate fees and know the money you receive for selling your digital products with Lemon Squeezy. 🤔 Who needs this extension? 👉 All users who sell their digital products on Lemon Squeezy."
- **Source:** https://chromewebstore.google.com/detail/lemon-squeezy-fee-calcula/bbadfcacpbejgcnagiibnammbhgfakdi
- **source_type:** product_listing
- **verification_status:** direct_verified
- **Date:** April 2026
- **Notes:** Chrome Web Store listing page. Extension is free. Creator listed as jlozano. Also listed on Product Hunt (176 upvotes, ranked #7 on launch day). This is a third-party auxiliary service not made by Lemon Squeezy.

---

**F-03**

- **Finding ID:** F-03
- **What:** A third-party iOS app provides dashboard, analytics, and sales tracking for Lemon Squeezy store owners, described as "your all-in-one dashboard, analytics, and sales tracking app."
- **Verbatim snippet:** "Manage your Lemon Squeezy store like never before, your all-in-one dashboard, analytics, and sales tracking app. Whether you run one product or an entire storefront, The App helps you stay connected to every sale, subscription, and trend right from your phone."
- **Source:** https://apps.apple.com/us/app/lemon-squeezy-ls-dashboard/id6753926253
- **source_type:** product_listing
- **verification_status:** direct_verified
- **Date:** April 2026
- **Notes:** Apple App Store listing for "Lemon Squeezy LS Dashboard." Developer: Maher Mouris. Rating: 5.0 (1 rating). Free with in-app purchases. Page includes disclaimer: "LS Dashboard is an independent app designed for Lemon Squeezy store owners. It is not affiliated with or endorsed by Lemon Squeezy." The listing also describes a "Directory Screen" feature: "List your Digital Products on the Directory Screen and get free trafic for your products" — a third-party discovery mechanism for Lemon Squeezy products, cited here in notes as it is from a separate passage on the same page.

---

## Part 2 — Provisional Findings (blocked_url_index_verified)

---

**F-P01**

- **Finding ID:** F-P01
- **What:** Ful.io lists 2,509 websites using Lemon Squeezy.
- **Verbatim snippet:** "Need a complete list of websites (2,509 - infact) using Lemon Squeezy?"
- **Source:** https://ful.io/technology/Widgets/lemon-squeezy
- **source_type:** database_profile
- **verification_status:** blocked_url_index_verified
- **Date:** April 2026
- **Notes:** Data retrieved from search engine cached snippet. Direct page fetch was not confirmed. Ful.io categorizes Lemon Squeezy under "Widgets," differing from Wappalyzer's "Payment processors" classification.

---

**F-P02**

- **Finding ID:** F-P02
- **What:** The storefront at uipress.lemonsqueezy.com lists three products: UiPress 3 Lite at $0.00, UiPress 3 Pro at $47.00–$999.00, and uiXpress at $57.00–$297.00.
- **Verbatim snippet:** "uipress · UiPress 3 Lite · $0.00 · UiPress 3 Pro · $47.00 - $999.00 · uiXpress · $57.00 - $297.00 · Powered by Lemon Squeezy"
- **Source:** https://uipress.lemonsqueezy.com/
- **source_type:** product_listing
- **verification_status:** blocked_url_index_verified
- **Date:** April 2026
- **Notes:** Page returned 403 on direct fetch. Data from search engine cached snippet. Three products observed. Prices in USD. Range pricing ($47.00–$999.00) indicates multiple variants. "Powered by Lemon Squeezy" footer visible. No category labels observed. No review counts observed.

---

**F-P03**

- **Finding ID:** F-P03
- **What:** The storefront at laragon.lemonsqueezy.com lists products including Laragon 1-year (Annual license) at $49.00–$69.00, Laragon Education license at $96.00–$192.00, Laragon Lifetime (Perpetual license) at $149.00–$199.00, and Laragon Lifetime for Team at $995.00.
- **Verbatim snippet:** "Laragon · Laragon 1-year (Annual license) · $49.00 - $69.00 · Laragon Education license (Non-Commercial) · $96.00 - $192.00 · Laragon Lifetime (Perpetual license) · $149.00 - $199.00 · Laragon Lifetime for Team (Perpetual license) · $995.00 · Laragon Non-Commercial license - Extended"
- **Source:** https://laragon.lemonsqueezy.com/
- **source_type:** product_listing
- **verification_status:** blocked_url_index_verified
- **Date:** April 2026
- **Notes:** Page returned 403 on direct fetch. Data from search engine cached snippet. Five or more products observed; snippet is truncated. Product is developer tools software (local development environment). Prices in USD. License types include annual, perpetual, education, and team — indicating tiered software licensing. No category labels observed. No review counts observed.

---

**F-P04**

- **Finding ID:** F-P04
- **What:** The storefront at notioneverything.lemonsqueezy.com lists products including Notion Complete Bundle at $199.00–$279.00, Notion Finance Tracker Pro at $34.00–$69.00, Notion Freelance OS at $79.00–$149.00, and Notion Second Brain 3.5 at $64.00–$124.00.
- **Verbatim snippet:** "Notion Everything · Notion Complete Bundle · $199.00 - $279.00 · Notion Finance Tracker Pro · $34.00 - $69.00 · Notion Freelance OS · $79.00 - $149.00 · Notion Second Brain 3.5 · $64.00 - $124.00 · Small Business OS"
- **Source:** https://notioneverything.lemonsqueezy.com/
- **source_type:** product_listing
- **verification_status:** blocked_url_index_verified
- **Date:** April 2026
- **Notes:** Page returned 403 on direct fetch. Data from search engine cached snippet. Five or more products observed; snippet is truncated. All observed products are Notion templates. Prices in USD. Range pricing indicates variant tiers. No category labels observed. No review counts observed.

---

**F-P05**

- **Finding ID:** F-P05
- **What:** The storefront at idearupt.lemonsqueezy.com lists three subscription products: Bhavesh AI Pro at $9.00/month, Idearupt Pro at $19.00/month, and Idearupt Pro+ with 7 Day Free Trial at $49.00/month.
- **Verbatim snippet:** "Idearupt · Bhavesh AI Pro · $9.00/month · Idearupt Pro · $19.00/month · Idearupt Pro+ - 7 Day Free Trial · $49.00/month · Powered by Lemon Squeezy"
- **Source:** https://idearupt.lemonsqueezy.com/
- **source_type:** product_listing
- **verification_status:** blocked_url_index_verified
- **Date:** April 2026
- **Notes:** Page returned 403 on direct fetch. Data from search engine cached snippet. Three products observed, all monthly subscriptions. Prices in USD. One product explicitly offers a "7 Day Free Trial." "Powered by Lemon Squeezy" footer visible. No category labels observed. No review counts observed.

---

**F-P06**

- **Finding ID:** F-P06
- **What:** The storefront at amdesigns.lemonsqueezy.com lists products priced in Tanzanian Shillings (TZS), including Anime Tracker | Notion Template at TZS15,000, Apple Slides | Figma Slides Template at TZS0+, and Bookworm Library | Notion Template at TZS25,000.
- **Verbatim snippet:** "Anime Tracker | Notion Template · TZS15,000 · Apple Slides | Figma Slides Template · TZS0+ · Bookworm Library | Notion Template · TZS25,000 · Min-folio | Notion Template · My Skin | Notion Template"
- **Source:** https://amdesigns.lemonsqueezy.com/
- **source_type:** product_listing
- **verification_status:** blocked_url_index_verified
- **Date:** April 2026
- **Notes:** Page returned 403 on direct fetch. Data from search engine cached snippet (site:lemonsqueezy.com store query). Products include Notion templates and Figma templates. Prices in TZS (Tanzanian Shillings), demonstrating non-USD currency display on Lemon Squeezy storefronts. TZS0+ indicates pay-what-you-want or free pricing. Five products listed; prices not visible for last two in snippet. No category labels observed. No review counts observed.

---

**F-P07**

- **Finding ID:** F-P07
- **What:** TechCrunch reported that Lemon Squeezy co-founder and CEO JR Farr described the company as a 13-person entity that publicly launched in 2021.
- **Verbatim snippet:** "Lemon Squeezy co-founder and CEO JR Farr noted that since his 13-person company's public launch in 2021"
- **Source:** https://techcrunch.com/2024/07/26/stripe-acquires-payment-processing-startup-lemon-squeezy/
- **source_type:** article
- **verification_status:** blocked_url_index_verified
- **Date:** July 26, 2024
- **Notes:** TechCrunch article covering Stripe's acquisition of Lemon Squeezy. Unable to confirm whether the page was directly fetched or data came from search snippet; degraded to provisional. The 13-person figure reflects team size at time of reporting (July 2024), not necessarily current state. The same article separately states Lemon Squeezy surpassed $1 million in annual recurring revenue nine months after its public launch, but that appears in a different passage and is therefore not included in this finding's verbatim. Journalism single-source rule applies (TechCrunch is primary reporting with direct CEO quotation).

---

## Part 3 — Pattern Candidates (sealed)

---

**PC-01** — Across observed Lemon Squeezy storefronts (F-P02 through F-P06), design templates (Notion templates, Framer templates, Figma templates) and software/SaaS products appear as listed product types. Both categories are present in the observed sample of storefronts.

**PC-02** — Observed storefronts display both one-time purchase pricing (F-P02, F-P03, F-P04, F-P06) and recurring subscription pricing (F-P05) on the platform. Some storefronts show pay-what-you-want pricing ($0+/TZS0+).

**PC-03** — Observed third-party auxiliary tools built around Lemon Squeezy cluster in developer integration categories (SaaS boilerplates, SDKs, MCP servers, WordPress libraries, integration platform connectors). Seller-facing auxiliary tools (fee calculator, mobile dashboard) are fewer in number within the observed sample.

---

## Part 4 — Could Not Verify / Out-of-Scope

---

**F-X01:** lemonsqueezy.com/showcase — URL from shard "Where to look first" does not appear to exist. No search results found for this specific URL. Fetches returned errors. The nearest equivalent found was lemonsqueezy.com/case-studies, but that page contains seller success stories (D2 territory).

**F-X02:** Public marketplace browse URL — Searched for marketplace.lemonsqueezy.com, lemonsqueezy.com/marketplace, lemonsqueezy.com/discover, app.lemonsqueezy.com/marketplace. None are indexed by search engines as publicly accessible pages. Lemon Squeezy marketplace documentation exists at docs.lemonsqueezy.com/help/marketplace describing a marketplace with categories, tags, eligibility rules, and a 30% fee, but no public browse URL was found. Third-party comparison sites (toolfolio.io) still listed the marketplace as "coming soon" at time of their last update. The marketplace appears to exist within the authenticated dashboard only.

**F-X03:** Marketplace categories list — A partial list of marketplace categories was observed in a search engine snippet from docs.lemonsqueezy.com/help/marketplace/categories, including: "Fonts · Serif · Sans Serif · Script + Handwritten · Decorative · Graphics · Backgrounds · Textures · Social · Patterns · Objects · Illustrations · Icons · Solid · Outline · Duotone · Emojis · Mockups · Templates · Print · Logos + Branding · Websites · UX + UI Kits · Infographics · Presentations · Email · Development · Business · Finance · IT · Productivity · Design · Marketing · Lifestyle · Photo + Video · Health + Fitness · Music · Education · News · Games" (truncated). Could not verify because: (a) page returned 403, (b) snippet is truncated, and (c) source_type is platform_doc/help_center, which is not in the allowed source_type list for this shard and maps to D1 territory.

**F-X04:** Customer review system — The Lemon Squeezy roadmap page (lemonsqueezy.com/roadmap) lists "Add support for customer reviews on product pages, marketplace listing pages, etc." as a future item. No review counts were observed on any storefront. Could not verify as formal finding because: (a) roadmap page returned 403, data from search snippet only, and (b) source_type is platform_doc (D1 territory). Observable absence: zero review counts across all examined storefronts.

**F-X05:** GMV or total transaction volume — No publicly reported gross merchandise volume or total transaction volume data was found for Lemon Squeezy in any source searched. The only revenue figure found is $1M ARR within nine months of 2021 launch (per TechCrunch, covered in F-P07). No updated figures post-Stripe acquisition.

**F-X06:** Total store or seller count — No specific total store or seller count is published in any verifiable source. Lemon Squeezy's own website uses "Join thousands of successful startups, software companies, and digital creators" and "Join 10,000+ founders" (newsletter signup). These are marketing claims (D1 territory, excluded per shard rules). The Horizon Partners acquisition announcement uses "attracted thousands of businesses" — also excluded as secondary retelling of company claims.

**F-X07:** lemonsqueezy.com/wedge — URL from shard "Where to look first" resolves to /wedges (plural). Content is "Wedges," an open-source React UI component library built with Radix UI and Tailwind CSS. Not related to catalog, discovery, or market signals. Out of scope for D3.

**F-X08:** Storefront search, filter, and browse mechanisms — All {merchant}.lemonsqueezy.com pages returned HTTP 403 on direct fetch, preventing observation of any search bars, filter controls, or browse mechanisms on individual storefronts. Documentation states storefronts use "a simple and easy to use template" but this is from platform_doc (D1 territory). No evidence of search or filter functionality on individual storefronts was observed in any search snippet.

**F-X09:** Capterra and SimilarTech profiles — No dedicated Capterra product page for Lemon Squeezy was found in search results. No SimilarTech profile page was found. A SaaSworthy page listing Lemon Squeezy pricing was found but contained data inconsistent with official pricing and source_type is ambiguous.

---

## Research QA Notes

### Findings forced to Provisional and why

All Lemon Squeezy first-party URLs (lemonsqueezy.com/*, docs.lemonsqueezy.com/*, {merchant}.lemonsqueezy.com) returned HTTP 403 due to Cloudflare bot protection. This affected every finding sourced from these domains. Findings F-P02 through F-P06 (storefront product listings) rely entirely on search engine cached snippets, which reproduce page content as last indexed by Google — indexing date unknown, so prices and products may not reflect current state. All were classified as blocked_url_index_verified and placed in Part 2.

F-P07 (TechCrunch): Could not confirm with certainty whether the TechCrunch article was directly fetched by the research agent or whether data came from a search engine snippet. Degraded from potential Clean to Provisional as a precaution.

### Findings degraded to could_not_verify and why

F-X03 (marketplace categories): Observable category names were partially retrieved from a search engine snippet, but the source page (docs.lemonsqueezy.com/help/marketplace/categories) is platform documentation, placing it outside the shard's allowed source_type list. Additionally, the snippet is truncated and the full category taxonomy is unknown.

F-X04 (customer reviews): The absence of reviews is directly observable (no review counts on any storefront snippet), but the confirmatory evidence (roadmap page stating reviews are planned) comes from platform documentation (D1 source_type territory).

F-X08 (storefront UI mechanisms): The 403 block on all storefronts makes it impossible to observe or report on the presence/absence of search bars, filters, or browse controls. Documentation-sourced descriptions of storefront features were excluded as D1 source_type.

### URL-not-fixable degradations

- lemonsqueezy.com/showcase: URL provided in shard "Where to look first" does not appear to exist as a live page. No redirect detected. No alternative URL identified as equivalent.
- lemonsqueezy.com/wedge: Actual URL is /wedges (with 's'). Content is a UI component library, not relevant to D3. Cannot be repurposed for this shard.

### Source_type ambiguities

1. **docs.lemonsqueezy.com/help/marketplace** and subpages: These pages describe the marketplace discovery mechanism (categories, tags, eligibility requirements, 30% fee), which is D3-relevant content. However, the source_type is platform_doc/help_center, which the shard execution instructions assign to D1 territory. The discovery mechanism data from these pages was moved to Part 4 (F-X02, F-X03) with the source_type conflict noted. This represents the largest single coverage gap in this run: the most detailed evidence of Lemon Squeezy's discovery infrastructure is locked behind a source_type exclusion.

2. **lemonsqueezy.com/roadmap**: Contains observable evidence of planned catalog/discovery features (reviews, cart, marketplace enhancements, course builder). Source_type is platform_doc. Moved to F-X04.

3. **GitHub repositories** (MCP LemonSqueezy Server by atharvagupta2003, ArrayPress Lemon Squeezy Updater, nextjs-lemonsqueezy-boilerplate): These are auxiliary services relevant to D3, but GitHub code repositories do not fit any of the allowed source_types (product_listing, search_results_page, database_profile, blog, article, report). Not included as formal findings. Their existence is noted in QA only: at least three open-source repositories exist that provide Lemon Squeezy-specific developer tooling.

4. **Integration platform pages** (Integrately, Pipedream, Make.com connectors for Lemon Squeezy): These pages list Lemon Squeezy integrations. Integrately claims "3,667 one-click integrations" for Lemon Squeezy. Source_type is ambiguous — could be product_listing or database_profile. Not included as formal findings due to this ambiguity.

5. **SaaS boilerplate product pages** (supastarter, Shipped, SaaS Starter Kit, NextJet, etc.): Multiple commercial SaaS boilerplates offer Lemon Squeezy as a payment integration option. These are auxiliary services but their source pages are product_listing or blog source_types and the products are multi-platform (supporting both Stripe and Lemon Squeezy). At least seven commercial boilerplate products were identified. Not included as individual findings to avoid inflating count with repetitive observations.

### Truncated/partial sources

- F-X03: Marketplace categories snippet is truncated; full taxonomy unknown.
- F-P02 through F-P06: Some storefront snippets are truncated; additional products may exist beyond those visible in cached snippets.
- F-P03: Snippet ends mid-listing with "Laragon Non-Commercial license - Extended" — additional products or pricing may follow.
- F-P04: Snippet lists "Small Business OS" without a price — product exists but price is not in the snippet.

### Coverage gaps

1. **Discovery mechanisms (SD-06, SD-11):** The most substantive evidence of Lemon Squeezy's discovery infrastructure (marketplace categories, tag system, eligibility rules) is sourced from platform documentation (D1 territory source_type). No public-facing marketplace browse URL was found indexed by search engines. This leaves a significant gap: the shard asks about discovery mechanisms, but the primary evidence falls outside allowed source_types.

2. **Total catalog size:** No observable count of total products or stores on Lemon Squeezy was found in any allowed source. Wappalyzer (1,900 websites) and Ful.io (2,509 websites) count websites using Lemon Squeezy's payment technology, not products listed on the platform. These are proxies, not direct catalog counts.

3. **Category dominance:** Observed storefronts show templates (Notion, Framer, Figma) and software/SaaS as recurring product types, but the sample is too small (six storefronts) to make population-level claims about which categories dominate. The marketplace categories list (F-X03) suggests a taxonomy weighted toward design assets and templates, but the list is truncated and from a D1 source.

4. **Geographic availability:** Wappalyzer shows geographic distribution of websites using LS (63% US, 21% Anguilla, 7% Canada), but this was reported from a page rendering format that may not constitute a verbatim-extractable continuous passage. Not included as a formal finding; noted here only.

5. **Discount patterns:** No original-vs-sale-price patterns were observed in any storefront snippet. Pay-what-you-want pricing ($0+) was observed in two storefronts (F-P06 amdesigns, and saasdesign.lemonsqueezy.com which was not included as a formal finding to avoid exceeding provisional count).

6. **Blog (SD-04):** The Lemon Squeezy blog (lemonsqueezy.com/blog) returned 403. Search snippets showed blog categories ("Lemon Drops" for feature releases, "Growth" for selling advice) and post dates (Oct 2022–Jan 2026). No blog posts contained observable catalog/market-signal data distinct from D1 marketing claims. The Stripe acquisition blog post (April 2025) mentions "Stripe Managed Payments" integration but contains no catalog data.

7. **Documentation guides (SD-03):** docs.lemonsqueezy.com/guides returned 403. Search snippets showed developer tutorials (SaaS billing, customer portals, subscriptions). No catalog or discovery-relevant data was found in guide content.

### Cases where input could not be decomposed without interpretation

- The shard's "Where to look first" lists lemonsqueezy.com/wedge, which does not exist (actual URL is /wedges). Interpreted as a minor URL error and searched for /wedges instead.
- The shard's "Where to look first" lists lemonsqueezy.com/showcase, which does not appear to exist. No interpretation was applied; the absence was documented as F-X01.
- The shard asks for "discovery mechanisms" and "auxiliary services," both of which could theoretically include Lemon Squeezy's own API (which enables programmatic product and store queries). The API documentation was excluded as platform_doc (D1 territory) and because API endpoints are infrastructure, not a catalog discovery mechanism in the D3 sense. This boundary required interpretive judgment.

### Additional observable data not formalized as findings

The following data was gathered but not included as formal findings due to source_type conflicts, verification issues, or shard boundary concerns:

- **G2 profile** (g2.com/products/lemon-squeezy/reviews): 0 reviews, profile inactive for over a year, categories listed as "E-Commerce Platforms, Merchant of Record, Usage-based billing software." Not formalized because verification of direct page fetch could not be confirmed.
- **Trustpilot profile** (trustpilot.com/review/lemonsqueezy.com): 121 reviews, 1.3/5 TrustScore, categorized as "e-Commerce Solution Provider." Review count is an observable market signal, but individual review content is D4 territory, and the aggregate rating is an aggregation of buyer opinion. Source_type ambiguity between database_profile and buyer review platform.
- **Product Hunt profile** (producthunt.com/products/lemon-squeezy): "This is the 30th launch from Lemon Squeezy." Tags include saas(46), developer tools(37), productivity(18), payments(61), fintech(41), e-commerce(41). Observable metadata but verification of direct page fetch not confirmed.
- **LinkedIn profile** (linkedin.com/company/lemon-squeezy-llc): Company size 11-50 employees, HQ Salt Lake City, Utah. Observable but sourced from search snippet (not confirmed fetch).
- **CheckThat.ai profile** (checkthat.ai/brands/lemon-squeezy): Reports "$1.4 million in total funding" citing PitchBook, and "the company hit $1 million ARR within nine months of launch." Contains outdated Trustpilot score (3.5/5 vs actual 1.3/5 in April 2026). Not formalized due to data quality concern and unclear source_type classification.
- **saasdesign.lemonsqueezy.com**: Shows "Framer Landing Page Templates · $97.00 · Thrive - Framer Portfolio Template · $12.00 · Ultimate Notion Planner - Updated for 2024 · $0.00+ · Powered by Lemon Squeezy." Not formalized to avoid inflating provisional count with additional storefront observations structurally identical to F-P02 through F-P06.
- **Easytools/Easycart migration tool** (easy.tools/docs/migrating-from-lemon-squeezy): Offers migration FROM Lemon Squeezy. Describes LS as "a closed system that doesn't offer conveniences for those looking to migrate to another platform." This is an auxiliary service, but source_type is platform_doc of a third-party tool, ambiguous as to whether it qualifies as article, blog, or product_listing.
- **Statamic CMS addon for Lemon Squeezy** (statamic.com/addons/rias/lemon-squeezy): "This addon has been abandoned by its developer." Auxiliary service, now defunct. source_type ambiguous.
- **Deprecated community SDK** (npmjs.com/package/lemonsqueezy.ts): "This packages has been deprecated in favor of the official Lemon Squeezy SDK." Still receives 1,013 weekly downloads. Observable auxiliary service artifact.

---

*End of Data Gathering run for shard Lemon Squeezy × D3.*