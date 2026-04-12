# Gumroad catalog, discovery, and market signals

Gumroad's marketplace operates as a **JavaScript-rendered single-page application** with **18 official product categories**, **300+ subcategories**, and a meta-described catalog of "over 1.6 million free and premium digital products." Third-party datasets tracking active/engaged listings count between **146,271 and 250,000+ products**, suggesting most of the 1.6 million are inactive or dormant. The platform charges a **10% flat fee** on direct sales and a minimum **30% fee** on Discover marketplace sales, with a paid boost system that directly determines product visibility.

---

## Part 1 — Clean findings (direct_verified)

None.

---

## Part 2 — Provisional findings (blocked_url_index_verified)

None.

---

## Part 3 — Pattern candidates (sealed)

### PC-01: Gumroad marketplace structure and category taxonomy

Cross-source synthesis from GumTrends (250K+ product dataset), InsightRaider (146,271 products, March 2026), InfoProdSpy (207,000+ products, April 2026), Amy Peniston's blog, and StoreLeads platform data.

**The 18 categories:** 3D, Audio, Business and Money, Comics and Graphic Novels, Design, Drawing and Painting, Education, Fiction Books, Films, Fitness and Health, Gaming, Music and Sound Design, Other, Photography, Recorded Music, Self Improvement, Software Development, Writing and Publishing. Confirmed independently by GumTrends, Amy Peniston, and InsightRaider.

**Price ranges across categories (InsightRaider, 146,271 products, March 2026):**

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

**Revenue concentration:** Products priced $200+ hold 65.7% of all revenue (InsightRaider).

**Seller catalog size vs. total sales (InsightRaider):** 1 product → 269 avg sales; 2–3 → 706; 4–5 → 1,681; 11+ → 5,201.

**Traffic sources (InsightRaider):** Organic search 41% at 3.1% conversion; social media 33% at 2.4%; direct 18% at 5.8%; paid ads 8% at 1.9%.

**Platform-level store data (StoreLeads):** 19,321 active stores Q4 2025 (12% YoY growth); 10,909 stores Q1 2026 (partial).

**Product counts by category (InfoProdSpy, 207,000+ products, April 2026):**

| Category | Product Count | Total Revenue | Avg Rev/Engaged Product |
|---|---|---|---|
| Graphic Design | 35,000 | $65.4M | $8,300 |
| 3D Design | 16,500 | $106.6M | $13,100 |
| Education & Career | 16,400 | $48.9M | $11,700 |
| Business | 13,700 | $55.7M | $24,700 |
| Software & Tech | 10,600 | $48.3M | $15,300 |

**Discount patterns observed on actual product pages (multi-source observation):** Strikethrough pricing, bundle discounts, limited-time offers, deep discounts, dynamic/graduated pricing, installment payments, creator-set promo codes.

**Discovery and search mechanisms:** All Gumroad discover and category pages are JavaScript-rendered SPAs. Direct web fetching returned only HTML shells. URL pattern for categories: gumroad.com/{category-slug}. Default sort: sort=curated. Paid boost requires minimum 30% commission. Mobile Discover restricts products to max $100 price; mobile sales incur 40% fee.

**Third-party ecosystem:** Analytics tools (fullStats.io, GumTrends at $99 one-time, Marketsy.ai, Putler, SegMetrics, InfoProdSpy); listing optimization (GumForge, GumBoost Pro, MindPal, Instapage); SEO tools (Auto Page Rank, Charles Floate's guide); Fiverr lists 562+ Gumroad-related services.

Sources span multiple independent providers without single-source URL anchors; not eligible for individual finding extraction.

---

## Part 4 — Could not verify

### F-X01: fullStats.io — analytics tool for Gumroad sellers
**What:** fullStats.io offers detailed analytics for Gumroad sellers including net revenue after fees, top products, top countries, affiliate sales, refunds, new vs. returning customers, and day-of-week/hour-of-day grouping.
**Verbatim snippet:** "Better analytics for Gumroad. Detailed stats to help you increase revenue and sales."
**Source:** https://fullstats.io
**source_type:** marketplace_tool
**verification_status:** could_not_verify
**Date:** April 2026 (observed in shard)
**Notes:** Pricing: free under $300/month MRR; $2.50–$82.50/month tiered by revenue. verification_status inferred during normalization: no per-finding access method specified in source shard; conservative default applied.

---

### F-X02: GumTrends — dataset of 250K+ Gumroad products
**What:** GumTrends provides a growing dataset of 250,000+ Gumroad products with estimated revenue, sales counts, and mixed review ratios across 300+ subcategories. One-time $99 for lifetime access.
**Verbatim snippet:** "Build your next digital product using data no one else has. Get access to a growing dataset of 250k+ Gumroad products."
**Source:** https://gumtrends.com
**source_type:** marketplace_tool
**verification_status:** could_not_verify
**Date:** April 2026 (observed in shard; updated weekly per source)
**Notes:** 150+ business owner users per shard. verification_status inferred during normalization: no per-finding access method in source shard.

---

### F-X03: Marketsy.ai — free tool for identifying high-performing Gumroad products
**What:** Marketsy.ai Gumroad Trends is a free tool for digital product sellers to identify high-performing products and track trends. Updated daily with search and sorting capabilities.
**Verbatim snippet:** "A must-have inspiration tool for digital products sellers: identify high-performing products, be aware of trends, earn more."
**Source:** https://marketsy.ai/tools/gumroad-trends
**source_type:** marketplace_tool
**verification_status:** could_not_verify
**Date:** April 2026 (observed in shard)
**Notes:** verification_status inferred during normalization: no per-finding access method in source shard.

---

### F-X04: Putler — multi-store analytics with native Gumroad integration
**What:** Putler provides SaaS metrics (MRR, churn, LTV, ARPU), RFM customer segmentation, and forecasting with native Gumroad OAuth integration and multi-store analytics.
**Verbatim snippet:** "Dominate Gumroad with Putler's actionable insights."
**Source:** https://putler.com/integrations/gumroad
**source_type:** marketplace_tool
**verification_status:** could_not_verify
**Date:** April 2026 (observed in shard)
**Notes:** verification_status inferred during normalization: no per-finding access method in source shard.

---

### F-X05: SegMetrics — revenue attribution and reporting dashboards for Gumroad
**What:** SegMetrics provides revenue attribution and customer journey analytics connecting Gumroad with 130+ integrations. Tracks which ads bring contacts with highest LTV after 3, 6, and 12 months.
**Verbatim snippet:** "The Best Gumroad Reporting Dashboards."
**Source:** https://segmetrics.io/integration/gumroad
**source_type:** marketplace_tool
**verification_status:** could_not_verify
**Date:** April 2026 (observed in shard)
**Notes:** verification_status inferred during normalization: no per-finding access method in source shard.

---

### F-X06: GumForge — AI-powered Gumroad page generator
**What:** GumForge generates high-converting Gumroad product pages using AI. Claims conversion rate increases up to 25%. Offers auto-generated optimized copy, layout/pricing recommendations, one-click export, multilingual support, and SEO optimization.
**Verbatim snippet:** "AI-Powered Page Generator! Transform your Gumroad listings into high-converting product pages with AI."
**Source:** https://gumforge.reavid.cc
**source_type:** marketplace_tool
**verification_status:** could_not_verify
**Date:** April 2026 (observed in shard)
**Notes:** verification_status inferred during normalization: no per-finding access method in source shard.

---

### F-X07: GumBoost Pro — AI tool for Gumroad product descriptions
**What:** GumBoost Pro uses GPT-3/GPT-4, Claude2, and Google Bard for generating compelling Gumroad product descriptions. 100+ out-of-the-box commands. One-time payment (sold on Gumroad itself).
**Verbatim snippet:** "Boost Your Gumroad Sales with the Ultimate AI Tool for Compelling Product Descriptions."
**Source:** https://waveupuk.gumroad.com/l/GumBoostPro
**source_type:** marketplace_tool
**verification_status:** could_not_verify
**Date:** April 2026 (observed in shard)
**Notes:** verification_status inferred during normalization: no per-finding access method in source shard.

---

### F-X08: MindPal — free AI workflow for Gumroad product listing writing
**What:** MindPal's Gumroad Product Listing Writer generates SEO-optimized product names, descriptions, slugs, and launch/thank-you emails. Described as a free AI tool.
**Verbatim snippet:** "Generates SEO-optimized product names, compelling product descriptions, user-friendly product slugs, and even crafts launch and thank-you emails."
**Source:** https://agentcrew.co/workflow/gumroad-product-listing-writer
**source_type:** marketplace_tool
**verification_status:** could_not_verify
**Date:** April 2026 (observed in shard)
**Notes:** verification_status inferred during normalization: no per-finding access method in source shard.

---

### F-X09: Gumroad help documentation — tag system for sellers
**What:** Gumroad's help documentation states that detailed tags boost Discover sales and enable customer filtering. Tags appear on creator profiles when they have 9+ products.
**Verbatim snippet:** "Detailed tags on your products can both boost sales on Discover and help your customers filter your profile."
**Source:** https://help.gumroad.com
**source_type:** platform_help
**verification_status:** could_not_verify
**Date:** April 2026 (observed in shard)
**Notes:** Source URL inferred during normalization — shard cites "Gumroad's help documentation" without explicit URL. verification_status inferred: no access method specified.

---

### F-X10: Gumroad help center — paid boost and commission structure
**What:** Gumroad's help center describes the paid boost system: agreeing to a higher commission percentage (minimum 30%) gives products a higher boost on Discover. Fees only charged when a sale results from Discover discovery.
**Verbatim snippet:** "The higher the percentage chosen, the higher the boost the product receives. These fees are only charged when a sale occurs after it was found on Discover."
**Source:** https://help.gumroad.com
**source_type:** platform_help
**verification_status:** could_not_verify
**Date:** April 2026 (observed in shard)
**Notes:** Source URL inferred during normalization. verification_status inferred: no access method specified.

---

### F-X11: GitHub issue #682 — spam listings problem on Gumroad Discover
**What:** A GitHub issue (#682, labeled "$1K priority") describes a spam problem where fake products containing only affiliate links to popular Discover products are being published on Discover despite having no sales, no ratings, and unverified creators.
**Verbatim snippet:** "Spammers are creating fake products that only contain affiliate links to popular Discover products. These low-effort listings are getting published on Discover, even though they have no sales, no ratings, and their creators haven't been marked as compliant."
**Source:** https://github.com/gumroad/gumroad/issues/682
**source_type:** developer_community
**verification_status:** could_not_verify
**Date:** April 2026 (observed in shard; issue date not specified)
**Notes:** Source URL inferred from issue number cited in shard text. verification_status inferred: no access method specified. Issue labeled "$1K priority" per shard.

---

## Research QA Notes

QA notes not present in source shard.
