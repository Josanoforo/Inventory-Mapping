# DG RUN — SHARD: Etsy × D3 — Catalog, Discovery, and Market Signals

**DG Agent Designation:** Conservative DG  
**Shard:** Etsy × D3 — Catalog, discovery, and market signals (Etsy only)  
**Direction:** Observable catalog composition, price ranges, category dominance, discovery/search mechanisms, auxiliary services, and market signals  
**Language:** English  
**Time Window:** Current state only  
**Run Date:** April 11, 2026  

---

## 1. SEARCH DECOMPOSITION

**SD-01:** What top-level product categories exist on etsy.com and how is the category taxonomy structured?

**SD-02:** What products, prices, and category labels appear on Etsy search results for "digital download"?

**SD-03:** What products, prices, and category labels appear on Etsy market page for "digital_planner"?

**SD-04:** What products, prices, and category labels appear on Etsy market page for "notion_template"?

**SD-05:** What discovery/search mechanisms (filters, sort options, badges, recommendation modules) are observable on etsy.com buyer-facing pages?

**SD-06:** What are the most-searched keywords on Etsy as reported by third-party analytics tools with observable data?

**SD-07:** What third-party auxiliary tools (SEO, analytics, listing optimization, competitor analysis) exist for Etsy sellers, and what services do they offer?

**SD-08:** What observable data on Etsy catalog size, category distribution, or market composition is available from database profiles (Statista, SimilarWeb, Koalanda)?

**SD-09:** What pricing patterns, discount structures, and sale formats are observable across Etsy category pages?

**SD-10:** What Etsy-native discovery features (Editors' Picks, Trends, curated collections, Marketplace Insights) exist on the platform?

---

## 2. PART 1 — Clean Findings (direct_verified)

---

### F-01

**Finding ID:** F-01  
**What:** eRank reports the top 20 most-searched keywords on Etsy US for March 2026 as: 1. tshirt, 2. shirt, 3. stickers, 4. pokemon, 5. wall art, 6. gift, 7. jewelry, 8. phone case, 9. resident evil, 10. keychain, 11. home decor, 12. womens clothing, 13. necklace, 14. ayn thor, 15. png, 16. easter, 17. personalized gift, 18. ita bag, 19. press on nails, 20. t shirt.  
**Verbatim snippet:** "1. tshirt 2. shirt 3. stickers 4. pokemon 5. wall art 6. gift 7. jewelry 8. phone case 9. resident evil 10. keychain 11. home decor 12. womens clothing 13. necklace 14. ayn thor 15. png 16. easter 17. personalized gift 18. ita bag 19. press on nails 20. t shirt"  
**Source:** https://help.erank.com/blog/top-keywords-on-etsy/  
**source_type:** blog  
**verification_status:** direct_verified  
**Date:** 6 April 2026  
**Notes:** Page directly fetched via web_fetch. eRank's keyword data derives from eRank's own proprietary database analysis of Etsy US shopper search behavior. Exact methodology for measuring search volume not fully disclosed by eRank. The numbered list appears as a markdown ordered list on the page; character-for-character verbatim reproduced from web_fetch markdown extraction. Data describes March 2026 search activity. SD-06.

---

### F-02

**Finding ID:** F-02  
**What:** The keyword "png" rose from rank #121 to #15 on Etsy US top searches in one month, with search volume increasing 257%. The page states it carried a "High Conversion" badge indicating shoppers using this keyword in the past 30 days added to carts and purchased.  
**Verbatim snippet:** "As you can above right on the search history chart, "png" search volume is way up! In just the past month, it has shot up 257%!"  
**Source:** https://help.erank.com/blog/top-keywords-on-etsy/  
**source_type:** blog  
**verification_status:** direct_verified  
**Date:** 6 April 2026  
**Notes:** Page directly fetched via web_fetch. The 257% figure refers to month-over-month change (February to March 2026). Separately on the same page, eRank states the February CTR was 125% and the 12-month average CTR is 124%; those figures are in a different passage and not included in this verbatim. eRank's CTR and search volume metrics are eRank's own calculations, not Etsy official numbers. SD-06.

---

### F-03

**Finding ID:** F-03  
**What:** The keyword "personalized gift" rose from rank #162 to #17 on Etsy US top searches in one month, with search volume increasing 299%. It carried both "High Conversion" and "Trending in Search" gold badges.  
**Verbatim snippet:** "As you can see above right, "personalized gift" dropped to a 15-mo low this February. Then in just a month, it shot up 299%! And this one has both gold badges. For high conversion for the past 30 days, and another for continuing to trend in search this week."  
**Source:** https://help.erank.com/blog/top-keywords-on-etsy/  
**source_type:** blog  
**verification_status:** direct_verified  
**Date:** 6 April 2026  
**Notes:** Page directly fetched via web_fetch. A separate passage on the same page states the keyword reached its 15-month high in June at "Close to 170,000 searches" — not included here to maintain single-passage rule; that data would require a separate finding. eRank proprietary data. SD-06.

---

### F-04

**Finding ID:** F-04  
**What:** The keyword "sticker" had a March 2026 CTR of 150%, a 12-month average CTR of 127%, and searches that have not dropped below 20,000 per month in the past 15 months. eRank states stickers are "among Etsy's top sellers."  
**Verbatim snippet:** "Its 12-mo average CTR is also stellar: 127%. So, don't let that Competition stat deter you! Instead, use the data here to assess shopper demand and purchase intent. In the past 15 months, searches haven't dropped below 20,000/mo, which means plenty of demand. And both Average and Monthly CTR stats are superb, which tells us that stickers are among Etsy's top sellers."  
**Source:** https://help.erank.com/blog/top-keywords-on-etsy/  
**source_type:** blog  
**verification_status:** direct_verified  
**Date:** 6 April 2026  
**Notes:** Page directly fetched via web_fetch. The "150% March CTR" appears in the subheading above this passage ("March CTR: 150%") — not in this verbatim excerpt. The 20,000/mo floor and 127% average CTR are in the cited passage. eRank proprietary data. SD-06.

---

### F-05

**Finding ID:** F-05  
**What:** The keyword "crochet pattern" dropped to rank #58 on Etsy US searches but its monthly click-through rate increased by 892%.  
**Verbatim snippet:** "Since then, "crochet pattern" has dropped to #58 but boy has purchase intent soared! Its monthly CTR is up by 892%!"  
**Source:** https://help.erank.com/blog/top-keywords-on-etsy/  
**source_type:** blog  
**verification_status:** direct_verified  
**Date:** 6 April 2026  
**Notes:** Page directly fetched via web_fetch. "Since then" refers to the prior month's report where "crochet pattern" ranked 4th in the Top 20. The 892% CTR increase is month-over-month. eRank proprietary metric. SD-06.

---

### F-06

**Finding ID:** F-06  
**What:** Koalanda states it tracks all Etsy listings: currently more than 125 million. Of those, approximately 8 million had sales in the last 30 days. Listing sales history is 89% accurate on average.  
**Verbatim snippet:** "Koalanda tracks all Etsy listings: currently more than 125 million. Out of all listings, there are about 8 million that have sales in the last 30 days."  
**Source:** https://koalanda.pro/etsy-product-research  
**source_type:** database_profile  
**verification_status:** direct_verified  
**Date:** Accessed April 2026; page undated  
**Notes:** Page directly fetched via web_fetch. The "125 million" figure is Koalanda's own tracking count, presented on Koalanda's product page FAQ. The "89% accurate" claim appears in a separate FAQ answer on the same page ("The listing sales history is 89% accurate on average") and is not included in this verbatim. Koalanda states its primary data source is the Etsy API. SD-08.

---

### F-07

**Finding ID:** F-07  
**What:** Koalanda states its primary data source is the Etsy API, and that it uses machine learning and statistical algorithms to calculate each displayed metric. Shop sales history is claimed 100% accurate for the past year. Keyword search scores are 90% accurate measured by relative keyword popularity.  
**Verbatim snippet:** "Our primary source of data is the Etsy API, which enables us to retrieve real Etsy data and statistics. We use advanced machine learning and statistical algorithms to carefully design and calculate each metric that we show, based on the data coming from Etsy."  
**Source:** https://koalanda.pro/  
**source_type:** database_profile  
**verification_status:** direct_verified  
**Date:** Accessed April 2026; page undated  
**Notes:** Page directly fetched via web_fetch. The 100% shop accuracy and 90% keyword accuracy claims appear in separate sentences in the same FAQ answer block but were in paragraph-separated lines in the rendered page; only the above continuous paragraph is cited as verbatim. Self-reported accuracy figures cannot be independently verified from this source alone. SD-07, SD-08.

---

## 3. PART 2 — Provisional Findings (blocked_url_index_verified)

---

### F-P01

**Finding ID:** F-P01  
**What:** Etsy's category directory page lists 16 top-level product categories: Accessories, Art & Collectibles, Bags & Purses, Bath & Beauty, Books Movies & Music, Clothing, Craft Supplies & Tools, Electronics & Accessories, Home & Living, Jewelry, Paper & Party Supplies, Pet Supplies, Shoes, Toys & Games, Weddings, Kids & Baby. An additional "Gifts" section appears as a browsing/merchandising category with sub-sections.  
**Verbatim snippet:** n/a — content recovered via research subagent direct fetch of URL; verbatim character-for-character accuracy cannot be independently confirmed.  
**Source:** https://www.etsy.com/categories  
**source_type:** search_results_page  
**verification_status:** blocked_url_index_verified  
**Date:** Accessed April 2026; page undated  
**Notes:** URL is fixed. Page was fetched by research subagent using web_fetch tool on exact URL; page loaded successfully per subagent report. The 16-category list is structural/navigational content unlikely to differ from rendering. Subcategory counts were also reported (e.g., Jewelry: 12 subcategories; Home & Living: 16 subcategories; Clothing: 6 subcategories) but verbatim for those could not be independently confirmed. Recovery method: subagent direct fetch. SD-01.

---

### F-P02

**Finding ID:** F-P02  
**What:** The Etsy Jewelry category page (etsy.com/c/jewelry) displays "1,000+ items with ads" as the result count. Sort options available: Relevancy (default), Lowest Price, Highest Price, Top Customer Reviews, Most Recent. An "All Filters" button with "Refine your search" panel is present. Subcategory tiles shown include: Rings, Necklaces, Earrings, Bracelets, Jewelry Sets, Watches, Body Jewelry, Cremation & Memorial Jewelry, Jewelry Storage, Smart Jewelry, Cuff Links & Tie Clips, Brooches Pins & Clips, with "Show more (6)" indicating 6 additional hidden subcategories.  
**Verbatim snippet:** n/a — content recovered via research subagent direct fetch of URL; verbatim character-for-character accuracy cannot be independently confirmed.  
**Source:** https://www.etsy.com/c/jewelry  
**source_type:** search_results_page  
**verification_status:** blocked_url_index_verified  
**Date:** Accessed April 2026; page undated  
**Notes:** URL is fixed. Page was fetched by research subagent using web_fetch tool on exact URL; page loaded successfully per subagent report. The sort options and subcategory structure are structural UI elements. The "1,000+ items with ads" count is the platform's stated display count, not a total catalog count. Recovery method: subagent direct fetch. SD-05, SD-01.

---

### F-P03

**Finding ID:** F-P03  
**What:** On the Etsy Jewelry category page, a listing for "Custom Name Necklace, 18K Gold Plated Name Necklace, Personalized Name Necklace, Birthday Gift for Her, Mother's Day Gift, Gift for Mom" appears with Sale Price $14.05, Original Price $28.11 (50% off), from shop AnyaShopStudio, with 55,428 reviews, Star Seller badge, marked as Ad, with FREE shipping.  
**Verbatim snippet:** "Custom Name Necklace, 18K Gold Plated Name Necklace, Personalized Name Necklace, Birthday Gift for Her, Mother's Day Gift, Gift for Mom — (55,428 reviews), Star Seller — Sale Price $14.05, Original Price $28.11 (50% off), Shop: AnyaShopStudio, Ad, FREE shipping"  
**Source:** https://www.etsy.com/c/jewelry  
**source_type:** product_listing  
**verification_status:** blocked_url_index_verified  
**Date:** Accessed April 2026; listing undated  
**Notes:** URL is fixed. Content recovered via subagent direct fetch. Verbatim is from subagent's formatted report of listings visible on the page; the exact rendering format on etsy.com differs from this text representation. Price observation: $14.05 (was $28.11, 50% off). This is an ad-promoted listing. Review count of 55,428 is the highest observed in this category page. Recovery method: subagent direct fetch. SD-09.

---

### F-P04

**Finding ID:** F-P04  
**What:** On the Etsy Jewelry category page, a listing for "0.94 CTW Pear Lab Grown Diamond Halo Engagement Ring in 10K Gold" appears with Sale Price $1,959.30, Original Price $2,799.00 (30% off), from shop VOWANDCARAT, marked as Ad, with FREE shipping.  
**Verbatim snippet:** "0.94 CTW Pear Lab Grown Diamond Halo Engagement Ring in 10K Gold | Teardrop Diamond Ring | Classic Halo Bridal Ring | Gift For Women — Sale Price $1,959.30, Original Price $2,799.00 (30% off), Shop: VOWANDCARAT, Ad, FREE shipping"  
**Source:** https://www.etsy.com/c/jewelry  
**source_type:** product_listing  
**verification_status:** blocked_url_index_verified  
**Date:** Accessed April 2026; listing undated  
**Notes:** URL is fixed. Content recovered via subagent direct fetch. This represents the high end of the price range observed on this category page. The lowest observed price on the same page was $12.50 (was $25.00, 50% off) for a charm necklace. Recovery method: subagent direct fetch. SD-09.

---

### F-P05

**Finding ID:** F-P05  
**What:** The Etsy market page for "digital_planner" is titled "Digital Planner - Etsy" and described as offering products from "planner templates shops." Available filters include: Exclude digital items, Under $10, Star Seller, Personalizable, Free shipping, Ships from United States. Seller ads appear from shops including Plannerscollective, LetsPlanPlanners, KatacosmicDesign.  
**Verbatim snippet:** "Check out our digital planner selection for the very best in unique or custom, handmade pieces from our planner templates shops."  
**Source:** https://www.etsy.com/market/digital_planner  
**source_type:** search_results_page  
**verification_status:** blocked_url_index_verified  
**Date:** Accessed April 2026; page undated  
**Notes:** URL is fixed (user-specified). Page returned 403 error on direct fetch; content recovered via search engine index snippet of the same URL. The meta description is the verbatim. Filter list and shop names come from the subagent's search-index recovery and may reflect cached content. SD-03, SD-05.

---

### F-P06

**Finding ID:** F-P06  
**What:** The Etsy market page for "notion_template" is titled "Notion Template - Etsy" and described as offering products from "templates shops." Related market pages discovered include: Notion Templates, 500 Notion Templates, Notion Template Business, Notion Template Marketing, Notion Template Trading.  
**Verbatim snippet:** "Check out our notion template selection for the very best in unique or custom, handmade pieces from our templates shops."  
**Source:** https://www.etsy.com/market/notion_template  
**source_type:** search_results_page  
**verification_status:** blocked_url_index_verified  
**Date:** Accessed April 2026; page undated  
**Notes:** URL is fixed (user-specified). Page returned 403 error on direct fetch; content recovered via search engine index snippet. The presence of related market pages for business, marketing, and trading sub-niches of Notion templates is observable from the search index but exact URLs not independently verified. SD-04.

---

### F-P07

**Finding ID:** F-P07  
**What:** SimilarWeb reports etsy.com's global rank as #74 (as of February 2026), with total visits of 386M in February 2026 (decreased 16% from prior month), bounce rate of 40.02%, pages per visit of 6.03, average visit duration of 4 minutes 39 seconds, and audience split of 41.97% male / 58.03% female. Largest age group: 25-34. Top traffic country: United States at 56.29%.  
**Verbatim snippet:** n/a — content recovered via research subagent's search-index query of the SimilarWeb profile URL; verbatim character-for-character accuracy cannot be independently confirmed.  
**Source:** https://www.similarweb.com/website/etsy.com/  
**source_type:** database_profile  
**verification_status:** blocked_url_index_verified  
**Date:** February 2026 data (per SimilarWeb report cycle)  
**Notes:** URL is fixed. SimilarWeb data accessed via subagent search-index recovery. SimilarWeb uses its own estimation methodology; figures are SimilarWeb's estimates, not Etsy's reported metrics. The 386M visits figure is for February 2026; monthly traffic varies seasonally. The subagent also reported top competitors by affinity: redbubble.com, printerval.com, 1stdibs.com, zazzle.com, fineartamerica.com. Recovery method: subagent search-index retrieval. SD-08.

---

### F-P08

**Finding ID:** F-P08  
**What:** eRank is a third-party Etsy analytics tool offering keyword research, competitor analysis, trend tracking across Etsy and 40+ other marketplaces (Amazon, eBay, Google Shopping, Pinterest), shop health audits, listing audits, rank checker, Chrome extension, and AI listing helper. Pricing: Free plan, Basic $5.99/mo, Pro $9.99/mo, Expert $29.99/mo. Claims over 1 million Etsy sellers trust eRank.  
**Verbatim snippet:** "Discover high-performing global keywords tailored to your niche, helping you stand out in the crowded Etsy marketplace with options for countries around the world. Gain insights into your competitors' strategies and find opportunities to outshine them. Stay ahead of the curve with up-to-date data on trending products and seasonal searches across multiple marketplaces and countries."  
**Source:** https://erank.com  
**source_type:** database_profile  
**verification_status:** blocked_url_index_verified  
**Date:** Accessed April 2026; page undated  
**Notes:** URL is fixed. Verbatim from search engine index snippet of erank.com homepage. Pricing tiers confirmed across multiple search results. The "over 1 million" sellers claim appears on the same page. eRank's Trend Buzz tool specifically covers daily top 100 most-searched terms on Etsy plus 40+ other marketplaces, updated daily. Recovery method: search-index snippet. SD-07.

---

### F-P09

**Finding ID:** F-P09  
**What:** Marmalead is a third-party Etsy SEO tool priced at $19/month ($15.83/month billed annually at $190/year) with a 14-day free trial. Features include keyword research with search volume and competition data, Storm brainstorming tool, keyword comparison (up to 4 keywords), listing grades, 12+ month trend forecasting with 3-month forecast, Boost SEO (AI-powered), Marma AI chat assistant, Customer Voice (AI review analysis), Top 100 Etsy Keywords, Etsy fee calculator, and hashtag generator.  
**Verbatim snippet:** n/a — content recovered via research subagent's direct fetch of marmalead.com homepage; verbatim character-for-character accuracy cannot be independently confirmed.  
**Source:** https://marmalead.com/  
**source_type:** database_profile  
**verification_status:** blocked_url_index_verified  
**Date:** Accessed April 2026; page undated  
**Notes:** URL is fixed. Pricing and feature list reported by subagent from direct page fetch. Marmalead's keyword engagement data is derived from Marmalead's own algorithms, not from Etsy directly. The tool explicitly states it "measures engagement with search terms" using proprietary methodology. Recovery method: subagent direct fetch. SD-07.

---

### F-P10

**Finding ID:** F-P10  
**What:** EverBee is a third-party Etsy analytics tool claiming to track 170M+ listings and 50M+ keywords. It offers product analytics (monthly sales, revenue, views, conversion rate, favorites, reviews, tag analyzer), keyword research (monthly search volume, competition, keyword score), email marketing with 1-click Etsy integration, Chrome extension, and trademark checker. Pricing: Free (Hobby, 10 analytic searches/month), Growth $19.99/month annual. Claims to be used by 900,000+ creators (elsewhere stated as 600,000+).  
**Verbatim snippet:** "Access 170M+ listings and 50M+ keywords to find high-demand, profitable products fast"  
**Source:** https://everbee.io/  
**source_type:** database_profile  
**verification_status:** blocked_url_index_verified  
**Date:** Accessed April 2026; page undated  
**Notes:** URL is fixed. Verbatim and feature list recovered via subagent search-index retrieval. The discrepancy in user count claims (900,000+ vs. 600,000+) appeared across different pages of the same site per subagent report. EverBee states its sales estimate algorithm maintains "an average accuracy rate of approximately 80%." Recovery method: subagent search-index retrieval. SD-07.

---

### F-P11

**Finding ID:** F-P11  
**What:** Alura is a third-party Etsy analytics tool claiming 121,119+ Etsy sellers using the platform. It offers keyword and tag analysis, sales and revenue estimates, AI writing assistant, AI review analysis, shop analyzer, listing helper, financial analytics dashboard, follow-up reminder, post automator, Pinterest marketing integration, and Chrome extension. Pricing: Free plan available; Growth plan $19.99/month (or $9.99/month billed yearly at $120/year); Professional plan $49.99/month (or $29.99/month billed yearly).  
**Verbatim snippet:** "Join 121,119+ Etsy sellers using Alura"  
**Source:** https://www.alura.io  
**source_type:** database_profile  
**verification_status:** blocked_url_index_verified  
**Date:** Accessed April 2026; page undated  
**Notes:** URL is fixed. Content recovered via subagent search-index retrieval; alura.io homepage returned permissions error on direct fetch. User count figure and feature list from Chrome Web Store listing and search-index snippets. Alura states it estimates sales using "a combination of different data like views, favourites and more." Recovery method: subagent search-index retrieval. SD-07.

---

### F-P12

**Finding ID:** F-P12  
**What:** Sale Samurai is a third-party Etsy analytics tool at salesamurai.io offering keyword research with "real search volume data from Etsy," competitor analytics, Chrome extension, Etsy fees calculator, competition tracker, and an uploader tool integrating with print-on-demand providers (Printful, Printify, Gooten). Pricing: Free plan $0/month, Basic $5.99/month, Pro $9.99/month.  
**Verbatim snippet:** "Sale Samurai gives you the insights and analytics needed to skyrocket your Etsy SEO. Keyword research with real search volume data from Etsy."  
**Source:** https://salesamurai.io/  
**source_type:** database_profile  
**verification_status:** blocked_url_index_verified  
**Date:** Accessed April 2026; page undated  
**Notes:** URL is fixed. Content recovered via subagent search-index retrieval. Note: the actual domain is salesamurai.io (not salesamurai.com). The print-on-demand uploader integration is a distinctive feature not present in other Etsy SEO tools surveyed. Recovery method: subagent search-index retrieval. SD-07.

---

### F-P13

**Finding ID:** F-P13  
**What:** A third-party analysis reports that six primary categories collectively account for approximately 87% of Etsy's Gross Merchandise Sales (GMS). Home & Living leads with approximately 34% of GMS. Jewelry & Accessories showed 16% growth in November-December 2024. Apparel is a top-3 category. Craft Supplies and Paper & Party Supplies show stable demand.  
**Verbatim snippet:** "Six primary categories collectively account for approximately 87% of Etsy's Gross Merchandise Sales (GMS). This concentration underscores the significance of these segments in driving Etsy's overall sales."  
**Source:** https://linkmybooks.com/blog/etsy-sales-statistics-by-category  
**source_type:** report  
**verification_status:** blocked_url_index_verified  
**Date:** Accessed April 2026; article references 2024 performance and 2025 projections  
**Notes:** URL is fixed. Verbatim from search engine index snippet. The 87% and 34% figures are LinkMyBooks' analysis citing Etsy's financial data; the What field does not include the "Digital Products: Growing segment" row from the same table, which appeared in a separate rendering section. This is a secondary analysis of Etsy's reported data, not primary Etsy disclosure. Recovery method: own web_search snippet. SD-08.

---

### F-P14

**Finding ID:** F-P14  
**What:** Etsy's Trends page (etsy.com/trends) displays editorially curated trend sections including "Etsy Trend Edit: S/S 2026," "Get Ready With Us: Festival Edition" (featuring crochet/embroidery products), "Your Analog Era Starts Now" (featuring junk journals), and "Everyday Exhibits" (curated prints/ceramics). Editors' Picks section featured 5 products including: One Line A Day Journal at $17.00, Ivory Lace Mantilla Wedding Veil at $599.99, Tulips Needlepoint Kit at $60.00. The page header states: "Trending Now — Discover the latest and trendiest finds brought to you by our Trend Expert, Dayna Isom Johnson."  
**Verbatim snippet:** n/a — content recovered via research subagent direct fetch of URL; verbatim character-for-character accuracy cannot be independently confirmed.  
**Source:** https://www.etsy.com/trends  
**source_type:** search_results_page  
**verification_status:** blocked_url_index_verified  
**Date:** Accessed April 2026; page undated  
**Notes:** URL is fixed. Subagent fetched etsy.com/trends successfully. Prices are listed as flat amounts without sale indicators for the Editors' Picks items. The trend section product listings included promoted items (marked "Ad") with prices ranging from $5.00 to $599.99. A navigational banner offered first-time buyer discounts. Etsy's 2026 Color of the Year is identified as "Patina Blue" and first-ever Texture of the Year as "Washed Linen" on this page. Recovery method: subagent direct fetch. SD-10, SD-09.

---

### F-P15

**Finding ID:** F-P15  
**What:** Etsy launched its own keyword research tool, Marketplace Insights, in September 2025. It provides a 30-day window of search data with 15 free keyword searches per week for standard sellers. Etsy Plus subscribers get unlimited searches and can view average monthly searches, competition level, and 30-day search trend graphs.  
**Verbatim snippet:** "Etsy launched its own keyword research tool, Marketplace Insights, built into Shop Manager under the Stats tab."  
**Source:** https://blog.marmalead.com/etsy-policy-updates/  
**source_type:** blog  
**verification_status:** blocked_url_index_verified  
**Date:** 18 February 2026 (last updated per subagent report)  
**Notes:** URL is fixed. Content recovered via subagent direct fetch of blog.marmalead.com page. The 15 searches/week figure and Etsy Plus unlimited access detail are reported by Marmalead citing Etsy's own announcements. A separate eRank blog post (help.erank.com/blog/etsy-marketplace-insights-tool/) corroborates the 15 searches/week figure — but that constitutes cross-source observation noted here only, not synthesized into the What field. Recovery method: subagent direct fetch. SD-05, SD-10.

---

## 4. PART 3 — Pattern Candidates (Sealed)

---

### PC-01

**Pattern:** Digital product keywords ("png," "stickers," "digital") and personalization keywords ("personalized gift") appear alongside traditional physical-goods keywords ("jewelry," "necklace," "keychain," "womens clothing") within the same Etsy top-20 search list for March 2026.  
**Referenced findings:** F-01, F-02, F-03, F-P05, F-P06  
**Scope note:** Descriptive co-occurrence only. No claim about relative category size, growth rate, or causal relationship.

---

### PC-02

**Pattern:** At least six independently operated third-party analytics tools (eRank, Marmalead, Koalanda, EverBee, Alura, Sale Samurai) exist for Etsy sellers, each offering keyword research, competitor analysis, and/or sales estimation features not available through Etsy's native seller tools prior to September 2025. Pricing ranges from free tiers to $49.99/month.  
**Referenced findings:** F-06, F-07, F-P08, F-P09, F-P10, F-P11, F-P12, F-P15  
**Scope note:** Descriptive enumeration of observable tools. No claim about market need, seller satisfaction, or tool effectiveness.

---

### PC-03

**Pattern:** Etsy's catalog structure exhibits simultaneous breadth (16 top-level categories, 125M+ tracked listings per Koalanda) and reported concentration (six categories accounting for approximately 87% of GMS per third-party analysis). Home & Living is reported as the leading GMS category.  
**Referenced findings:** F-06, F-P01, F-P13  
**Scope note:** Descriptive juxtaposition of breadth and concentration data from different sources. The 125M figure is from Koalanda (third-party tracker), the 87%/six-categories figure is from LinkMyBooks (third-party analysis of Etsy financial reports). No synthesis of these into a unified claim about catalog health or efficiency.

---

### PC-04

**Pattern:** Observable price ranges on the Etsy Jewelry category page span from $12.50 (sale price for a charm necklace) to $1,959.30 (sale price for a lab-grown diamond ring), with the majority of visible listings in the $14–$170 range. Sale/discount formats appear on the majority of visible listings, with discount percentages ranging from 15% to 71% off stated original prices.  
**Referenced findings:** F-P03, F-P04, F-P14  
**Scope note:** Descriptive price range observation from one category page at one point in time. Not generalizable to other categories or to the full Jewelry catalog.

---

## 5. PART 4 — Could Not Verify / Out-of-Scope

---

### F-X01: Etsy digital download search results

**What:** No data found on exact product listings, result counts, or prices visible on https://www.etsy.com/search?q=digital+download  
**Verbatim snippet:** n/a — absence finding  
**Source:** Attempted: direct fetch of https://www.etsy.com/search?q=digital+download (returned 403/blocked); subagent search-index recovery of the same URL yielded partial filter labels but no product listings with prices or result counts.  
**source_type:** unknown  
**verification_status:** could_not_verify  
**Date:** Accessed April 2026  
**Notes:** Etsy actively blocks automated fetching of /search? query pages with 403 errors. The subagent recovered some filter labels from search-index cached snippets (e.g., "Exclude digital items," "Under $25," "Star Seller") but these could not be attached to specific product listings or verified for currency. SD-02.

---

### F-X02: Etsy Seller Handbook search algorithm documentation

**What:** No data found on the current text of Etsy's official "How Etsy Search Works" documentation page  
**Verbatim snippet:** n/a — absence finding  
**Source:** Searched for Etsy Seller Handbook search documentation; found secondary citations of Etsy's search ranking factors in eRank and Marmalead blog posts, but the primary Etsy source page was not directly accessed.  
**source_type:** unknown  
**verification_status:** could_not_verify  
**Date:** Accessed April 2026  
**Notes:** Multiple third-party sources cite Etsy's official documentation about two-phase search (query matching then ranking), 13 tags per listing, and Context Specific Ranking. These citations appear in eRank (help.erank.com/blog/etsy-seo-basics/) and Marmalead blogs but constitute secondary retelling, not single-source access. Per protocol, secondary retelling = NOT single-source, so these are excluded from Parts 1-2. SD-05.

---

### F-X03: Statista Etsy detailed category breakdown

**What:** No data found on detailed category-level statistics for Etsy from Statista beyond basic summary figures  
**Verbatim snippet:** n/a — absence finding  
**Source:** Searched statista.com/topics/2501/etsy/ and related Statista pages. Accessible data limited to summary snippets: "In 2023, there were approximately 96.48 million active buyers" and "about 9 million sellers." Detailed category breakdown, GMS by category, and product mix data require Statista Premium subscription ($2,388/year) or individual dossier purchase ($495).  
**source_type:** unknown  
**verification_status:** could_not_verify  
**Date:** Accessed April 2026  
**Notes:** Statista's paywall prevents access to granular category data. The accessible snippets reference 2023 data (two years old). SD-08.

---

### F-X04: Handmade Seller Magazine Etsy market data

**What:** No data found on Etsy market or catalog data from Handmade Seller Magazine beyond subscription gate  
**Verbatim snippet:** n/a — absence finding  
**Source:** Searched handmadeseller.com. Confirmed it is "an exciting publication dedicated to helping you build a sustainable business selling on Etsy, Amazon or any other platform." Content about Etsy's financial results and Marketplace Insights exists but requires paid subscription.  
**source_type:** unknown  
**verification_status:** could_not_verify  
**Date:** Accessed April 2026  
**Notes:** Subscription-gated content. No publicly accessible quantitative data about Etsy's catalog or market from this source. SD-08.

---

### F-X05: CrestaProject as Etsy auxiliary tool

**What:** CrestaProject (crestaproject.com) is NOT an Etsy-specific tool. It is a WordPress themes and plugins company offering themes (Fortunato, Semplicemente, Ansia) and plugins (Cresta Social Share Counter, Cresta Addons for Elementor). No Etsy connection found.  
**Verbatim snippet:** n/a — absence finding (out-of-scope correction)  
**Source:** Searched crestaproject.com and found "CrestaProject - Modern and Responsive Premium and Free WordPress Themes & Plugins with fast support."  
**source_type:** unknown  
**verification_status:** could_not_verify  
**Date:** Accessed April 2026  
**Notes:** The task's WHERE TO LOOK FIRST section listed CrestaProject as a potential Etsy auxiliary tool. Research confirms it has no relationship to Etsy. This is recorded to document the search and prevent future re-investigation. SD-07.

---

## 6. RESEARCH QA NOTES

### Forced Provisionals
- F-P01 through F-P15: All Part 2 findings were degraded from potential direct_verified because the DG agent could not independently re-fetch the same URLs (Etsy pages returned 403 errors; other pages were accessed only by research subagents whose formatted reports may not preserve character-for-character verbatim). Conservative degradation applied per protocol.

### Multi-Speaker Splits
- The Marmalead blog post at blog.marmalead.com/etsy-policy-updates/ contains Marmalead's own analysis alongside direct quotations of Etsy's official announcements (seller classifications, Marketplace Insights, ChatGPT integration). Only Marmalead's own reportorial statements were used in F-P15. Etsy's official statements within that post were not extracted as separate findings because they constitute secondary retelling.

### Truncations
- The eRank top keywords page (F-01 through F-05) contained extensive additional data beyond the Top 20 (Top 250 keywords with CTR analysis). Only selected findings with clear verbatim passages were extracted. The full page extends to ~13 min read with data on ~30+ additional keywords.

### Source_type Ambiguities
- Koalanda (F-06, F-07): Classified as database_profile because Koalanda functions as a database of Etsy listings/keywords, not as a blog or article. The pages accessed are product/feature pages describing the database.
- Etsy /trends page (F-P14): Classified as search_results_page because it is a platform-generated discovery page displaying product listings, not an article or report.
- Etsy /categories page (F-P01): Classified as search_results_page as it is a navigational taxonomy page on the marketplace platform.
- LinkMyBooks (F-P13): Classified as report because it presents analysis of Etsy financial data with tables and projections.

### Coverage Gaps
- **SD-02 (digital download search results):** No usable findings. Etsy's search results pages block automated access. The user-specified URL https://www.etsy.com/search?q=digital+download returned 403 errors on all fetch attempts. Search-index snippets yielded only filter labels, not product listings or prices.
- **SD-03/SD-04 (digital planner / notion template market pages):** Only meta-descriptions recovered. No product-level data (listings, prices, review counts) could be captured from these pages.
- **SD-09 (pricing patterns):** Price observations limited to Jewelry category and Trends page. No price data captured for digital downloads, craft supplies, home & living, or other major categories due to Etsy page access restrictions.
- **Etsy's own marketing claims exclusion:** Per D1 exclusion rule, Etsy's public statements about catalog size (e.g., "50M+ items" or "100M+ items") were not included as D3 findings. The 125M figure from Koalanda (F-06) is a third-party database count, not an Etsy marketing claim.

### Decomposition Limits
- The search decomposition covers 10 sub-searches. SD-02 through SD-04 produced limited or no valid findings due to Etsy's bot protection. SD-05 produced only indirect/subagent data. The strongest coverage is on SD-06 (keyword/market signals from eRank), SD-07 (auxiliary tools), and SD-08 (database profiles).
- The shard direction's focus on "what products exist" and "what price ranges appear" was significantly constrained by Etsy's anti-bot measures. Observable catalog data was primarily obtained through third-party tools and Etsy category/trends pages rather than through direct search results.

### Verification Integrity
- No findings were fabricated. All Part 1 findings derive from pages directly fetched by the DG agent using web_fetch tool with content visible in the response. All Part 2 findings derive from either subagent direct fetches of fixed URLs or search engine index snippets of fixed URLs, with recovery method noted. All Part 4 entries document specific search attempts and locations.
- The expected output shape guidance of "2-5 clean direct_verified" is exceeded at 7 findings because 3 source URLs were directly fetched (eRank blog, Koalanda homepage, Koalanda product research page), each yielding multiple distinct observable units. The verification bar was not lowered; each finding meets the "directly accessed the exact URL and snippet came from there" standard.