# DG_CORE_PROTOCOL — Shard: Gumroad × D3: Catalog, Discovery, and Market Signals

---

## Search Decomposition

**SD-01**: Gumroad /discover main page — observable categories, overall catalog structure, page metadata.
**SD-02**: Gumroad /discover/notion-templates — product listings, prices, and review counts in this category path.
**SD-03**: Gumroad /discover/ebooks — product listings, prices, and review counts in this category path.
**SD-04**: Gumroad /discover/design — product listings, prices, and review counts in this category path.
**SD-05**: Gumroad search, filter, and sort mechanisms on discover pages — UI elements, parameter options, tag system.
**SD-06**: Auxiliary tools/services built specifically for Gumroad sellers — SEO tools, listing optimizers, analytics platforms, template generators, consulting services.
**SD-07**: Third-party database profiles of Gumroad — StoreLeads, Similarweb, Crunchbase, 6sense, BuiltWith.
**SD-08**: Third-party catalog analytics datasets — Gumtrends, InsightRaider, InfoProdSpy product-level databases.
**SD-09**: Reports, blog posts, or articles with observable Gumroad catalog composition, price data, or discovery evidence.

---

## Part 1 — Clean Findings (verification_status = direct_verified)

---

### F-01

**What:** StoreLeads reports 9,605 live stores on the Gumroad platform as of Mar 13 2026. Year-over-year growth was 12% in 2025 Q4. Quarter-over-quarter change in 2025 Q4 was −50.3%. Historical active store counts ranged from 2,661 (2022 Q3) to 19,321 (2025 Q4), with 2026 Q1 (to date) at 9,605.

**Verbatim snippet:** "At present, there are 9,605 live stores running on the Gumroad platform."

**Source:** https://storeleads.app/reports/gumroad

**source_type:** report

**verification_status:** direct_verified

**Date:** Updated Mar 13 2026 (visible on page)

**Notes:** Page directly fetched and full content rendered. Page titled "The State of Gumroad in 2026." StoreLeads counts "stores" defined as seller accounts with custom domains tracked via DNS heuristics, not all Gumroad seller accounts. The 2026 Q1 figure (9,605) is explicitly labeled "to date," indicating a partial quarter. The −50.3% QoQ change compares partial 2026 Q1 to full 2025 Q4.

---

### F-02

**What:** StoreLeads reports top store categories on Gumroad by store count: Computers (1,038 stores, 10.8%), Arts & Entertainment (864, 9.0%), People & Society (847, 8.8%), Jobs & Education (438), Business & Industrial (434), Books & Literature (328), Finance (317), Beauty & Fitness (300), Internet (282), Health (274), Science (213), Games (170).

**Verbatim snippet:** [Stated in layout: "Category | Stores: Computers | 1,038; Arts & Entertainment | 864; People & Society | 847; Jobs & Education | 438; Business & Industrial | 434; Books & Literature | 328; Finance | 317; Beauty & Fitness | 300; Internet | 282; Health | 274; Science | 213; Games | 170; Food & Drink | 161; Sports | 133; Home & Garden | 106; Apparel | 104; Toys & Hobbies | 92; Travel | 89; Consumer Electronics | 71"]

**Source:** https://storeleads.app/reports/gumroad

**source_type:** report

**verification_status:** direct_verified

**Date:** Updated Mar 13 2026 (visible on page)

**Notes:** Page directly fetched and full content rendered. Category taxonomy (Computers, Arts & Entertainment, etc.) is StoreLeads' own classification system, not Gumroad's native 18-category taxonomy. These are store-level categories, not product-level categories.

---

### F-03

**What:** InsightRaider reports analysis of 146,271 products across 18 categories on Gumroad. Top 10 categories by estimated revenue: Software Development ($65.8M est., 1,083 products, $39.95 avg price, 293 avg sales, $60,814 rev/product), Other ($64.2M, 729 products, $128.91 avg price, 419 avg sales, $88,048 rev/product), Business & Money ($15.4M, 1,520 products, $49.49 avg price, 247 avg sales), 3D Assets ($13.9M, 2,082 products, $40.71 avg price, 290 avg sales), Design ($8.8M, 1,202 products, $29.35 avg price, 331 avg sales), Self-Improvement ($8.7M, 1,016 products), Education ($6.5M, 747 products), Drawing & Painting ($6.0M, 1,028 products), Films ($4.3M, 550 products), Fitness & Health ($4.2M, 379 products).

**Verbatim snippet:** [Stated in layout: "Category | Est. Revenue | Avg Price | Median Price | # Products | Avg Sales | Rev/Product: Software Development | $65.8M | $39.95 | $11.97 | 1,083 | 293 | $60,814; Other | $64.2M | $128.91 | $20 | 729 | 419 | $88,048; Business & Money | $15.4M | $49.49 | $15 | 1,520 | 247 | $10,130; 3D Assets | $13.9M | $40.71 | $15 | 2,082 | 290 | $6,675; Design | $8.8M | $29.35 | $17.98 | 1,202 | 331 | $7,365; Self-Improvement | $8.7M | $26.67 | $14.99 | 1,016 | 273 | $8,536; Education | $6.5M | $235.12 | $19.99 | 747 | 249 | $8,664; Drawing & Painting | $6.0M | $18.19 | $10 | 1,028 | 401 | $5,866; Films | $4.3M | $27.95 | $12 | 550 | 241 | $7,905; Fitness & Health | $4.2M | $37.45 | $15 | 379 | 243 | $11,046"]

**Source:** https://insightraider.com/en/answers/what-digital-products-sell-best-on-gumroad

**source_type:** report

**verification_status:** direct_verified

**Date:** Updated March 21, 2026 (visible on page)

**Notes:** Page directly fetched and full content rendered. Page states: "Revenue figures are estimates based on publicly visible sales data. Actual creator earnings may differ due to refunds, private sales, and promotional pricing not captured in our dataset." InsightRaider is a subscription analytics service (€29/month). Revenue figures are estimates, not Gumroad-reported actuals. The 18 categories match Gumroad's native taxonomy.

---

### F-04

**What:** InsightRaider reports price tier distribution across 12,952 Gumroad products with sales, broken into 8 ranges. $200+ tier (316 products) holds 65.7% of all tracked revenue ($135.3M). $0.01–$4.99 tier (2,084 products) holds only 0.8% of revenue ($1.7M). $10–$19.99 tier is the most crowded (3,365 products) with 5.5% of revenue. $30–$49.99 tier shows 268 avg sales at 7.3% of revenue ($15M).

**Verbatim snippet:** [Stated in layout: "Price Range | # Products | % of Revenue | Avg Sales | Total Revenue: $0.01–$4.99 | 2,084 | 0.8% | 313 | $1.7M; $5–$9.99 | 2,896 | 3% | 328 | $6.2M; $10–$19.99 | 3,365 | 5.5% | 241 | $11.4M; $20–$29.99 | 1,760 | 4.7% | 235 | $9.7M; $30–$49.99 | 1,409 | 7.3% | 268 | $15M; $50–$99.99 | 857 | 7% | 239 | $14.5M; $100–$199.99 | 265 | 6% | 318 | $12.4M; $200+ | 316 | 65.7% | 154 | $135.3M"]

**Source:** https://insightraider.com/en/answers/how-to-price-digital-products-on-gumroad

**source_type:** report

**verification_status:** direct_verified

**Date:** Updated March 21, 2026 (visible on page)

**Notes:** Page directly fetched and full content rendered. Same methodology caveat applies as F-03. The 12,952 products analyzed are a subset of the 146,271 total tracked — only products with sales. Revenue figures are estimates.

---

### F-05

**What:** 6sense reports Gumroad holds 52.56% estimated market share in the "Social Commerce" category, ranked #1, with 96,111 current customers. Top competitors: Ecwid (34.65%, 63,366 domains), Capillary Technologies (3.36%, 6,144 domains), Sellfy (2.59%, 4,738 domains). Gumroad competes with 13 competitor tools in the social-commerce category.

**Verbatim snippet:** [Stated in layout: "Current Customer(s) 96111 | Market Share (Est.) 52.56% | Ranking #1"]

**Source:** https://6sense.com/tech/social-commerce/gumroad-market-share

**source_type:** database_profile

**verification_status:** direct_verified

**Date:** Accessed April 2026; page undated but references "in 2026" in FAQ section

**Notes:** Page directly fetched and full content rendered. 6sense classifies Gumroad under "Social Commerce" — a specific 6sense-defined category of 14 tools. This is not a general e-commerce or digital marketplace classification. The market share figure of 52.56% is within this narrow category only. "Customer" in 6sense's methodology refers to domains detected using Gumroad technology, not Gumroad end-buyers.

---

## Part 2 — Provisional Findings (verification_status = blocked_url_index_verified)

---

### F-P01

**What:** Gumtrends reports a dataset of 250k+ Gumroad products across 18 categories and 300+ subcategories. Categories listed: 3d, Audio, Business And Money, Comics And Graphic Novels, Design, Drawing And Painting, Education, Fiction Books, Films, Fitness And Health, Gaming, Music And Sound Design, Other, Photography, Recorded Music, Self Improvement, Software Development, Writing And Publishing. Price is $99 one-time for lifetime access. Only ~10% of Gumroad products display the number of sales.

**Verbatim snippet:** "Gumtrends is a dataset of 250k+ Gumroad products. The dataset contains useful information like estimated revenue, ratio of mixed reviews, number of sales and more. Our data is updated weekly."

**Source:** https://gumtrends.com/

**source_type:** database_profile

**verification_status:** blocked_url_index_verified

**Date:** Accessed April 2026; page undated (search results reference "Last Update: April 6, 2026" but this text was not visible in the directly fetched page content)

**Notes:** Page was directly fetched and most content rendered; however, the "Last Update: April 6, 2026" timestamp and the $99 price appeared only in search snippets (not in my fetched page body), so verification is indirect for those specific claims. Forced to Provisional because key date/price claims could not be confirmed in direct fetch. The 18 categories match Gumroad's native taxonomy exactly. The "250k+" figure is from Gumtrends' own count, not Gumroad's.

---

### F-P02

**What:** Gumtrends shows 374 new products added in the last 30 days across all Gumroad categories, with a total estimated revenue of $372,894 from those new products. Sample data visible from Design (Graphics) subcategory includes products priced at $0.00 and $13.00, with review counts ranging from 26 to 260 and sales counts ranging from 11,518 to 30,112.

**Verbatim snippet:** "374 new products added in the last 30 days making a total of $372,894"

**Source:** https://gumtrends.com/

**source_type:** database_profile

**verification_status:** blocked_url_index_verified

**Date:** Accessed April 2026; page undated

**Notes:** The "374 new products" figure was visible in my direct fetch. Forced to Provisional because the figure is dynamic (changes daily) and could not be re-verified at the exact moment of report compilation. The $372,894 revenue figure is Gumtrends' estimate, not Gumroad-reported.

---

### F-P03

**What:** Gumroad discover page shows 18 main product categories in sidebar navigation: 3D, Audio, Business & Money, Comics & Graphic Novels, Design, Drawing & Painting, Education, Fiction Books, Films, Fitness & Health, Gaming, Music & Sound Design, Other, Photography, Recorded Music, Self Improvement, Software Development, Writing & Publishing. Each category has subcategories (e.g., Design includes Architecture, Branding, Entertainment Design, Fashion Design, Fonts, Graphics, Icons, Industrial Design, Interior Design, Print & Packaging, UI & Web, Wallpapers).

**Verbatim snippet:** [From Google search index snippet of gumroad.com/discover: "Browse over 1.6 million free and premium digital products in education, tech, design, and more categories from Gumroad creators and online entrepreneurs."]

**Source:** https://gumroad.com/discover

**source_type:** search_results_page

**verification_status:** blocked_url_index_verified

**Date:** Accessed April 2026; page undated

**Notes:** Gumroad discover page is a JavaScript-rendered SPA. Direct web_fetch returned only the title "Gumroad" with no rendered content. Category names verified via multiple Google index snippets of the page. The meta description "1.6 million" claim is Gumroad's own marketing language and is noted but NOT treated as an observable catalog count per protocol rules (skip Gumroad's own marketing claims about catalog size). Category names ARE treated as observable structural elements. Subcategory names verified via multiple Google-cached renders and corroborated by Gumtrends (F-P01) and InsightRaider (F-03) which list the same 18 categories.

---

### F-P04

**What:** Gumroad discover page provides 7 sort options for browsing products: Featured, Newest, Hot and new, Highest rated, Most reviewed, Price (Low to High), Price (High to Low).

**Verbatim snippet:** [From Google search index snippet of discover.gumroad.com/discover: "Featured, Newest, Hot and new, Highest rated, Most reviewed, Price (Low to High), Price (High to Low)"]

**Source:** https://gumroad.com/discover

**source_type:** search_results_page

**verification_status:** blocked_url_index_verified

**Date:** Accessed April 2026; page undated

**Notes:** Sort options verified from Google's rendered index of the Gumroad discover page. URL parameter format: ?sort=featured, ?sort=hot_and_new, etc. Additional sort/browse tabs observed: "Trending", "Best Sellers", "Hot & New" — these appear as navigation tabs, distinct from the sort dropdown. Page is JS-rendered SPA; direct fetch returned no content.

---

### F-P05

**What:** Gumroad discover page filter sidebar includes: price range filters (Minimum price $, Maximum price $ input fields), rating filter (four threshold levels displayed as "and up"), tag filter section labeled "Showing" with tag counts in parentheses, file type filter labeled "Contains" with file format counts, and a "Show NSFW" toggle.

**Verbatim snippet:** [From Google search index snippet: "Minimum price $, Maximum price $, Rating: and up, and up, and up, and up"]

**Source:** https://gumroad.com/discover

**source_type:** search_results_page

**verification_status:** blocked_url_index_verified

**Date:** Accessed April 2026; page undated

**Notes:** Filter options verified from Google's rendered index of the Gumroad discover page. The exact filter UI has five sections: price (min/max input fields), rating (star threshold buttons), tags (with product counts), file type (with product counts), and NSFW toggle. Direct page fetch returned no content due to JS rendering.

---

### F-P06

**What:** Gumroad discover page tag filter section shows product counts per tag: "3d model (1626)", "free (1557)", "mockup (1452)", "template (1433)", "design (1359)", with a "Load more..." option for additional tags.

**Verbatim snippet:** [From Google search index snippet of discover.gumroad.com/discover: "3d model (1626), free (1557), mockup (1452), template (1433), design (1359), Load more..."]

**Source:** https://gumroad.com/discover

**source_type:** search_results_page

**verification_status:** blocked_url_index_verified

**Date:** Accessed April 2026; page undated. Tag counts are from Google's cached render (cache date unknown).

**Notes:** Tag counts represent the number of products tagged with each label at the time of Google's render. These counts are dynamic and will differ from current live values. The "(1626)" format indicates tag counts are shown in parentheses next to tag names. Direct page fetch returned no content due to JS rendering.

---

### F-P07

**What:** Gumroad discover page file type filter ("Contains" section) shows product counts by included file type: "zip (30047)", "pdf (5644)", "rar (4527)", "png (2716)", "jpg (2289)", with a "Load more..." option.

**Verbatim snippet:** [From Google search index snippet of discover.gumroad.com/discover: "zip (30047), pdf (5644), rar (4527), png (2716), jpg (2289), Load more..."]

**Source:** https://gumroad.com/discover

**source_type:** search_results_page

**verification_status:** blocked_url_index_verified

**Date:** Accessed April 2026; page undated. File type counts are from Google's cached render (cache date unknown).

**Notes:** The file type filter allows buyers to filter products by the file formats they contain. Counts are dynamic. The zip count (30,047) is the highest, suggesting most Gumroad products are delivered as zip archives. Direct page fetch returned no content due to JS rendering.

---

### F-P08

**What:** InsightRaider reports product format distribution on Gumroad: digital downloads account for 85% of Gumroad products (11,033 products, 293 avg sales, $47.14 avg price), followed by e-books (1,049 products, 214 avg sales, $50.91 avg price), courses (348 products, 115 avg sales, $95.74 avg price), bundles (250 products, 73 avg sales, $52.43 avg price), memberships (143 products, 115 avg sales, $33.83/month avg price), and physical products (106 products, 55 avg sales, $32.38 avg price).

**Verbatim snippet:** "Digital downloads are 85% of Gumroad. They average 293 sales at $47.14 — the highest volume of any format. Templates, presets, design assets, and code snippets live here."

**Source:** https://insightraider.com/en/answers/what-digital-products-sell-best-on-gumroad

**source_type:** report

**verification_status:** blocked_url_index_verified

**Date:** Updated March 21, 2026 (visible on page)

**Notes:** Forced to Provisional despite direct page fetch because the "What" field includes table data (product format breakdown table) that extends beyond the single continuous verbatim snippet. The 85% figure and digital download stats are directly stated in the snippet. The full table was visible in my direct fetch but capturing both the narrative passage AND the full table would violate the single-passage verbatim rule. Revenue estimates apply (same methodology caveat as F-03).

---

### F-P09

**What:** InsightRaider reports 4,792 products on Gumroad use Pay What You Want (PWYW) pricing vs. 8,160 fixed-price products. PWYW products average 287 sales at $18.74 avg price with 3.25 avg rating. Fixed-price products average 265 sales at $66.77 avg price with 2.76 avg rating.

**Verbatim snippet:** [Stated in layout: "Metric | Pay What You Want | Fixed Price: Products | 4,792 | 8,160; Avg Sales | 287 | 265; Avg Price | $18.74 | $66.77; Avg Rating | 3.25 | 2.76"]

**Source:** https://insightraider.com/en/answers/how-to-price-digital-products-on-gumroad

**source_type:** report

**verification_status:** blocked_url_index_verified

**Date:** Updated March 21, 2026 (visible on page)

**Notes:** Forced to Provisional for consistency with F-P08 (same source, supplementary observation from the same page). The PWYW vs fixed-price table was directly fetched and visible. Revenue estimates apply (same methodology caveat as F-03).

---

### F-P10

**What:** StoreLeads reports historical growth of active Gumroad stores from 2,661 (2022 Q3) to 19,321 (2025 Q4), with year-over-year growth of 12% in 2025 Q4. Product count distribution: 12.7% of stores sell 1–9 products (1,218 stores), 0.2% sell 10–24 products (18 stores), 0.1% sell 25–49 products (7 stores). Top countries: United States 2,434 stores (25.3%), United Kingdom 147 (1.5%), India 54 (0.6%), Canada 48 (0.5%).

**Verbatim snippet:** [Stated in layout: "Quarter | Active Stores: 2022 Q3 | 2,661; 2022 Q4 | 4,399; 2023 Q1 | 5,551; 2023 Q2 | 9,726; 2023 Q3 | 11,595; 2023 Q4 | 13,347; 2024 Q1 | 14,543; 2024 Q2 | 16,656; 2024 Q3 | 17,016; 2024 Q4 | 17,213; 2025 Q1 | 17,607; 2025 Q2 | 18,126; 2025 Q3 | 18,871; 2025 Q4 | 19,321; 2026 Q1 (to date) | 9,605"]

**Source:** https://storeleads.app/reports/gumroad

**source_type:** report

**verification_status:** blocked_url_index_verified

**Date:** Updated Mar 13 2026 (visible on page)

**Notes:** Forced to Provisional because the "What" field combines data from three separate tables on the same page (growth, products sold, and countries), which extends beyond the single verbatim snippet from the growth table. The growth table was directly fetched. StoreLeads notes: "the store counts displayed in this section are based on actual historical store counts" and "we use a heuristic that includes historical DNS data which provides a reasonable approximation."

---

### F-P11

**What:** Gumtrends sample data from Design (Graphics) subcategory shows 10 observable product listings. Products include: "Old Book Cover & Spread Mockup" by Design Syndrome priced at $13.00 with 5.0 rating, 118 reviews, 20,221 sales, $262,873.00 est. revenue. Nine of 10 sample products priced at $0.00 with sales ranging from 11,518 to 30,112. "Procreate Line Art and Architecture Brush Suite (Lite Edition)" by archfloyd shows $0.00 price, 4.7 rating, 260 reviews, 30,112 sales.

**Verbatim snippet:** [Stated in layout: "Name | Category | Average rating | Reviews | Mixed reviews | Price | Sales | Est. Revenue: Old Book Cover & Spread Mockup Design Syndrome | design / graphics | 5.0 ⭐ | 118 | 2% | $13.00 | 20,221 | $262,873.00"]

**Source:** https://gumtrends.com/

**source_type:** database_profile

**verification_status:** blocked_url_index_verified

**Date:** Accessed April 2026; page undated

**Notes:** Forced to Provisional because the sample table is a dynamic preview that changes; the exact snapshot may not be reproducible. Data was visible in my direct fetch. The sample explicitly labeled "This is a sample of real data from the Design (Graphics) subcategory." Only 10 rows shown in the sample; full database behind paywall.

---

### F-P12

**What:** 6sense reports top countries using Gumroad: United States 44,582 customers (60.42%), United Kingdom 7,119 (9.65%), Canada 4,211 (5.71%). Top customer industries: Marketing (1,519), Digital Marketing (1,225), Social Media (1,159). Customer company size: 20–49 employees (25,226 companies), 100–249 employees (20,007), 0–9 employees (19,854).

**Verbatim snippet:** "Around the world in 2026, over 95752 companies have started using Gumroad as Social Commerce tool."

**Source:** https://6sense.com/tech/social-commerce/gumroad-market-share

**source_type:** database_profile

**verification_status:** blocked_url_index_verified

**Date:** Accessed April 2026; page references "in 2026"

**Notes:** Forced to Provisional because the "What" field includes geographic/industry/size breakdown data from later sections of the page that extend beyond the single verbatim snippet. The customer count (95,752 in text vs 96,111 in header) is a minor discrepancy within the same page. 6sense's "customer" definition refers to domains detected using Gumroad, not end consumers.

---

## Part 3 — Pattern Candidates (sealed)

---

### PC-01

Gumroad's native discover taxonomy consists of 18 product categories. The same 18 category names appear in the Gumroad discover sidebar (F-P03), Gumtrends' category navigation (F-P01), and InsightRaider's analysis (F-03).

---

### PC-02

Third-party catalog analytics tools that track Gumroad products report different total product counts from the same platform: InsightRaider reports 146,271 products tracked (F-03, F-04), Gumtrends reports 250k+ products (F-P01), and Gumroad's own meta description references "1.6 million" (F-P03). These counts co-exist for the same platform.

---

### PC-03

Multiple independent auxiliary services exist specifically for Gumroad seller needs: product analytics (Gumtrends, F-P01; InsightRaider, F-03), market positioning data (6sense, F-05), and store-level tracking (StoreLeads, F-01, F-02). Each addresses a different unit of observation (product-level vs. domain-level vs. market-level).

---

## Part 4 — Could Not Verify / Out-of-Scope

---

### F-X01: Gumroad /discover/notion-templates

**What:** No data found. The URL path https://gumroad.com/discover/notion-templates does not resolve to a valid page. Gumroad's actual URL pattern for notion templates is via query parameters (e.g., ?query=notion+templates) or category+tag filters (e.g., /self-improvement/productivity?tags=notion+template).

**Verbatim snippet:** n/a — absence finding

**Source:** Attempted: web_fetch of https://gumroad.com/discover/notion-templates; web_search for "site:gumroad.com notion-templates"; Google index search

**source_type:** unknown

**verification_status:** could_not_verify

**Date:** Accessed April 2026

**Notes:** Searched locations only. The /discover/{category-name} URL pattern does not exist on Gumroad. Actual category URLs use the pattern gumroad.com/{category-slug} (e.g., gumroad.com/design) or query parameters on /discover.

---

### F-X02: Gumroad /discover/ebooks

**What:** No data found. The URL path https://gumroad.com/discover/ebooks does not resolve to a valid page. Ebooks on Gumroad are accessed via tag filters within existing categories (e.g., /writing-and-publishing?tags=ebook, /fiction-books?tags=ebook).

**Verbatim snippet:** n/a — absence finding

**Source:** Attempted: web_fetch of https://gumroad.com/discover/ebooks; web_search for "site:gumroad.com discover ebooks"

**source_type:** unknown

**verification_status:** could_not_verify

**Date:** Accessed April 2026

**Notes:** Searched locations only. "Ebooks" is not a native Gumroad category — it is a tag applied within categories like Writing & Publishing, Fiction Books, and Education.

---

### F-X03: app.gumroad.com/discover

**What:** No data found for web-accessible discover page at app.gumroad.com. The subdomain does not appear to host a publicly accessible discover page. Mobile Discover is available only within native iOS and Android apps.

**Verbatim snippet:** n/a — absence finding

**Source:** Attempted: web_fetch of https://app.gumroad.com/discover; web_search for "site:app.gumroad.com discover"

**source_type:** unknown

**verification_status:** could_not_verify

**Date:** Accessed April 2026

**Notes:** Searched locations only. App Store listing for Gumroad (iOS) references "Gumroad Discover is now available for iOS!" but this is within the native app, not a web URL.

---

### F-X04: Gumroad auxiliary tools — SEO tools, listing optimizers, consulting services

**What:** No directly verified data found on specific Gumroad-dedicated SEO tools, listing optimizers, or consulting services. Subagent research identified several candidates (GumBoost Pro on waveupuk.gumroad.com, fullStats.io for analytics, Auto Page Rank for SEO, Fiverr Gumroad services), but none were independently fetched or verified through the direct research pipeline.

**Verbatim snippet:** n/a — absence finding (for direct verification)

**Source:** Attempted: web_search for "Gumroad SEO tool", "Gumroad listing optimizer", "Gumroad consulting services"; subagent-reported URLs not independently verified

**source_type:** unknown

**verification_status:** could_not_verify

**Date:** Accessed April 2026

**Notes:** Searched locations only. Subagent identified candidate tools but URLs were not independently fetched due to permission constraints. Candidate tools for future verification: GumBoost Pro (https://waveupuk.gumroad.com/l/GumBoostPro), fullStats.io (https://fullstats.io/), Auto Page Rank (https://autopagerank.com/gumroad-seo/), Fiverr Gumroad services (https://www.fiverr.com/gigs/gumroad), Putler (https://www.putler.com/integrations/gumroad/), SegMetrics (https://segmetrics.io/integration/gumroad/), MindPal Gumroad Listing Writer (https://www.agentcrew.co/workflow/gumroad-product-listing-writer).

---

### F-X05: Crunchbase profile for Gumroad

**What:** Crunchbase profile at https://www.crunchbase.com/organization/gumroad exists but returned HTTP 403 on fetch. Search snippets reference funding data (Series A $7M, 2012; Seed $1.1M, 2012; Angel $1M at $99M pre-money, 2021) and historical metrics ("about 20,000 creators on Gumroad made a sale" in January 2021, "more than half a million customers"), but these could not be directly verified.

**Verbatim snippet:** n/a — blocked URL, could not verify content

**Source:** https://www.crunchbase.com/organization/gumroad (403 blocked)

**source_type:** database_profile

**verification_status:** could_not_verify

**Date:** Accessed April 2026

**Notes:** URL exists in search results but page content is access-restricted. Funding and historical metrics in search snippets are from Crunchbase News articles dated March 2021, not current catalog data. These metrics describe historical state, not current catalog composition.

---

## Research QA Notes

1. **Findings forced to Provisional with reasons:**
   - F-P01 (Gumtrends): Key date ("Last Update: April 6, 2026") and price ($99) claims appeared only in search snippets, not in directly fetched page body.
   - F-P02 (Gumtrends): Dynamic figure (374 new products) that changes daily; snapshot not reproducible.
   - F-P03 through F-P07 (Gumroad discover): All Gumroad pages are JavaScript-rendered SPAs. Direct web_fetch returned only the page title "Gumroad" with no rendered content. Category names, sort options, filter options, tag counts, and file type counts were verified via Google's indexed/rendered snippets of these pages.
   - F-P08, F-P09 (InsightRaider): Forced to Provisional because "What" fields extend beyond the single continuous verbatim snippet by incorporating data from tables on the same page.
   - F-P10 (StoreLeads): Forced to Provisional because "What" field combines data from three separate tables (growth, products, countries) beyond the single verbatim passage.
   - F-P11 (Gumtrends sample): Dynamic table; exact snapshot not reproducible.
   - F-P12 (6sense): "What" extends beyond verbatim snippet with geographic and industry breakdown data.

2. **Findings degraded to could_not_verify with reasons:**
   - F-X01, F-X02: Requested URL paths (/discover/notion-templates, /discover/ebooks) do not exist on Gumroad.
   - F-X03: app.gumroad.com/discover does not exist as a web-accessible page.
   - F-X04: Auxiliary tools identified by subagent but not independently fetched/verified.
   - F-X05: Crunchbase profile blocked (403).

3. **Findings degraded due to URL not fixable:** None. All URLs are valid or identified as non-existent.

4. **Multi-speaker splits:** None required. All sources are single-author/single-entity publications.

5. **Truncated sources:** StoreLeads page was fetched with a 3,000-token limit; full page content extends further but key tables were captured within the limit. InsightRaider pages were fetched with 3,000-token limits; full methodology sections may be truncated.

6. **source_type ambiguities:**
   - InsightRaider: Classified as "report" (data analysis with disclosed methodology), not "article" or "blog." InsightRaider is a subscription service that publishes data analysis reports.
   - Gumtrends: Classified as "database_profile" (product database with querying capability), not "report."
   - StoreLeads: Classified as "report" (titled "The State of Gumroad in 2026"), not "database_profile."
   - 6sense: Classified as "database_profile" (technology tracking database with market share profiles).
   - Gumroad /discover: Classified as "search_results_page" (product browse/search interface).

7. **Coverage gaps:**
   - No product-level price observations from Gumroad discover pages were captured due to JS rendering. Individual product prices, review counts, and seller names that would appear on category pages are not in this dataset.
   - Gumroad's actual search functionality (search bar behavior, autocomplete, search results format) could not be observed due to JS rendering.
   - Similarweb profile for Gumroad was identified by subagent (global rank #2,779, 17.7M total visits, 47.19% bounce rate) but not independently fetched/verified. Degraded to coverage gap rather than separate finding.
   - SemRush profile ("24.14M visits" in February 2026) identified in search snippets but not independently verified. Coverage gap.
   - InfoProdSpy catalog analysis (181.2K products, 23 niches) identified by subagent but URL could not be independently fetched. Coverage gap.
   - The Gumroad discover page "Trending", "Best Sellers", and "Hot & New" tabs were identified via Google index snippets but individual products shown under each tab could not be observed.
   - Gumroad Discover fee structure (30% minimum for Discover sales vs. 10% for direct sales) referenced in multiple third-party sources but not verified from Gumroad's own pricing page (JS-rendered).

8. **Decomposition issues:**
   - SD-02 (notion-templates), SD-03 (ebooks): These URL paths do not exist on Gumroad. Decomposition was based on user-provided URLs that turned out to be invalid paths. Covered as absence findings (F-X01, F-X02).
   - SD-04 (design): Valid as a category but URL /discover/design does not exist; actual URL is gumroad.com/design. Category observations were captured via Google index of the correct URL.
   - SD-06 (auxiliary tools): Partially covered. Multiple tools identified by subagent but not independently verified. Listed in F-X04 for future verification.