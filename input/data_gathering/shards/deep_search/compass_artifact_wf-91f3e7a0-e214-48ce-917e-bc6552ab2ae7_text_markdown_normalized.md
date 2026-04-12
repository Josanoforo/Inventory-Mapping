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

None.

---

## Research QA Notes

QA notes not present in source shard.
