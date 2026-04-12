# Payhip Catalog, Discovery Mechanisms, and Market Signals — Evidence Catalog

---

## GROUP A — DIRECTLY VERIFIED
*(Source accessed directly via web_fetch; snippet is from that source)*

---

### A1. Marketplace location and category structure (18 categories)

**What:** Payhip's public discovery/browse feature is the "Marketplace" at payhip.com/marketplace (not /explore). It presents 18 top-level categories with descriptions, listed in this order: 3D, Roblox, Crafts, Music & Sound Design, Design, Drawing & Painting, Fiction Books, Fitness & Health, Photography, Writing & Publishing, Business & Money, Films, Comics & Graphic Novels, Audio, Recorded Music, Education, Gaming, Software Development.

**Verbatim snippet:** Section header reads "Explore categories" followed by:
- 3D — "Discover exceptional 3D avatars, assets and more for VRChat and other platforms"
- Roblox — "Build the perfect Roblox game with high quality assets, vehicles, scripts, VFX etc"
- Crafts — "Crochet, sewing, knitting, quilting, stitching patterns and much more for crafters"
- Music & Sound Design — "Sample packs, loops, beats, sound kits etc from the most creative producers and engineers"
- Design — "Level up your designs with these creative design assets that you'll fall in love with"
- Drawing & Painting — "Procreate brushes, illustrations and art from the most talented creators in the world"
- Fiction Books — "Explore a universe of spellbinding, special and unique books"
- Fitness & Health — "From the gym, to the kitchen - fun and inspiring ways to change your lifestle"
- Photography — "All things presets, lightroom and photoshop to help your photography projects"
- Writing & Publishing — "Literary resources to help craft your stories - from guides, inspiration and more"
- Business & Money — "From making a dollar to making a lot more - learn the ins and outs here"
- Films — "LUTs packs and resources for Adobe Premier Pro and Final Cut Pro"
- Comics & Graphic Novels — "Acclaimed creators bringing you stories and art that will keep you hooked"
- Audio — "Meditation music, healing and subliminal audio that nourish the soul"
- Recorded Music — "Find albums and tracks from incredible musicians and artists"
- Education — "The perfect place to learn new skills and level up your existing ones"
- Gaming — "The place to discover upcoming indie developers and their amazing work"
- Software Development — "Learning to code and improving your skills has never been easier"

**Source URL:** https://payhip.com/marketplace
**source_type:** search_results_page
**Date:** Accessed April 2026; page undated
**Verification:** direct_verified
**Notes:** "lifestle" is a typo present on the actual page (Fitness & Health description). The top nav bar shows a subset: "All | 3D | Roblox | Crafts | Design | Drawing & Painting | Music & Sound Design | Films | More"

---

### A2. Marketplace discovery mechanisms — sort, price filter, rating filter

**What:** Each marketplace category page provides sorting (7 options), price filtering (6 tiers), and rating filtering (5 levels) as discovery mechanisms.

**Verbatim snippet (from /marketplace/design, identical structure on /marketplace/3d, /marketplace/crafts, /marketplace/roblox):**

Sort options: "Sort by / Default / Recently added / Hot and new / Highest rated / Most reviewed / Price: Low to high / Price: High to low"

Price filter: "Price / All prices / Free / Under $5 / $5 - $25 / $25 - $40 / $40 - $60 / $60 and above"

Rating filter: "Rating / All ratings / 4 stars and up / 3 stars and up / 2 stars and up / 1 star and up"

Additional controls: "Related tags" and "[More filters]" and "Filter" button.

**Source URL:** https://payhip.com/marketplace/design
**source_type:** search_results_page
**Date:** Accessed April 2026; page undated
**Verification:** direct_verified
**Notes:** Identical filter UI confirmed on /marketplace/3d, /marketplace/crafts, /marketplace/roblox. Products themselves are JavaScript-rendered and not visible in static HTML fetch.

---

### A3. Design category — 13 subcategories

**What:** The Design marketplace category contains 13 subcategories, with further sub-subcategories under some (e.g., Graphics breaks down into Assets & Templates, Marketing & Social, Mockups, Textures & Patterns (2D), Vector Graphics).

**Verbatim snippet (subcategory list from sidebar):** "Architecture, Branding, Entertainment Design, Fashion Design, Fonts, Graphics, Icons, Interior Design, Premade Book Cover, Print & Packaging, Printable, UI & Web, Wallpapers"

**Source URL:** https://payhip.com/marketplace/design
**source_type:** search_results_page
**Date:** Accessed April 2026; page undated
**Verification:** direct_verified

---

### A4. 3D category — 6 subcategories

**What:** The 3D marketplace category contains 6 subcategories.

**Verbatim snippet:** "3D Assets, 3D Modeling, Animating, Avatars, Textures, VRChat"

**Source URL:** https://payhip.com/marketplace/3d
**source_type:** search_results_page
**Date:** Accessed April 2026; page undated
**Verification:** direct_verified

---

### A5. Crafts category — 10 subcategories

**What:** The Crafts marketplace category contains 10 subcategories.

**Verbatim snippet:** "3D Printing, Coloring Books, Crochet, Cross Stitch, Embroidery, Knitting, Lego, Papercrafts, Quilting, Sewing"

**Source URL:** https://payhip.com/marketplace/crafts
**source_type:** search_results_page
**Date:** Accessed April 2026; page undated
**Verification:** direct_verified

---

### A6. Roblox category — 9 subcategories

**What:** The Roblox marketplace category contains 9 subcategories.

**Verbatim snippet:** "Aircraft, Assets, Boats, Games, Kit, Scripts, UI, Vehicles, Weapons"

**Source URL:** https://payhip.com/marketplace/roblox
**source_type:** search_results_page
**Date:** Accessed April 2026; page undated
**Verification:** direct_verified

---

### A7. Marketplace featured products section exists but is JS-rendered

**What:** The marketplace homepage has a "Featured products" section, but product cards are dynamically loaded via JavaScript and are not visible in static HTML. The fallback text shown is "Loading results..." followed by "No products found / Could not find products with your current filters, please try expanding your filters."

**Verbatim snippet:** "### Featured products" followed by "Loading results..." and "No products found"

**Source URL:** https://payhip.com/marketplace
**source_type:** search_results_page
**Date:** Accessed April 2026; page undated
**Verification:** direct_verified
**Notes:** This is an architectural finding — marketplace product grids use client-side JS rendering, while individual store pages render product listings server-side.

---

### A8. Marketplace help center — eligibility, scope, and tagging

**What:** The Payhip marketplace requires sellers to have made at least $10 in total sales and pass an account review. Only digital products are supported. Tags are used for search discovery. No additional fees apply for marketplace sales.

**Verbatim snippet:** "The Payhip marketplace is the perfect place for you to share your work with the world. It recommends your products to prospective customers outside of your existing following. Helping more people discover your work." … "For your store to be eligible to be listed on the marketplace you would need to meet the following criteria: - Have made at least $10 in total sales - Our accounts team has reviewed your store" … "Please note that self-purchases do not count toward this total." … "We aim to complete the approval process within 10 days of submission, but may take longer in some cases." … "At the moment, we can only support digital products on the marketplace. We plan to work on support for the other product types in the future, but will take some time." … "There is no additional fee for sales from the marketplace. You'll continue to be charged the usual Payhip fee for transactions." … "Tagging helps customers easily find your products through search and other discovery areas. So it's a good idea to include tags along with your products."

**Source URL:** https://help.payhip.com/article/307-marketplace
**source_type:** article
**Date:** Last updated January 26, 2026
**Verification:** direct_verified

---

### A9. Homepage — product types supported and featured showcase prices

**What:** Payhip's homepage lists five product types (Digital Downloads, Online Courses, Coaching, Memberships, Physical Products) and showcases 9 featured digital download products with prices ranging from £4.50 to $30.00.

**Verbatim snippet (product types):** "Sell digital downloads, courses, coaching and more from one simple platform. We make it easy for you to sell anything online anywhere." … "Sell any type of digital download such as ebooks, software, design assets, templates, video, music and more. If you can save it, you can sell it." … "Create online courses with rich features such as videos, digital files, quizzes and assignments. Publish drip courses and provide completion certificates." … "Sell your expertise through 1:1 coaching sessions. Easily set up online meetings with clients using Zoom, Calendly and more." … "Allow your customers to pay you on a recurring basis to access your digital downloads or membership group. Manage your members easily." … "Sell and manage inventory for any physical products. Manage your store, fulfill orders, run promotions and more."

**Verbatim snippet (featured prices):** Transitioning Vegan Cookbook $15.00 | Tales Of The Greatcoats $11.99 | Dujitsu Font $19.00 | Keto Cookbook Volume 2.0 $14.99 | Love to Cook Again Weekly Meal Planners $5.95 | Master Handstand $30.00 | Simple Science Fitness $5.99 | Breakfast Eats and Protein £4.50 | Planting Our Roots $10.00

**Source URL:** https://payhip.com/
**source_type:** product_listing
**Date:** Accessed April 2026; page undated (footer reads "© 2026 Payhip")
**Verification:** direct_verified
**Notes:** Multi-currency: 8 products in USD, 1 in GBP (£4.50). Price range: £4.50–$30.00.

---

### A10. Virtual Ink store — ebook prices, sale patterns, popularity claim

**What:** The Virtual Ink store (payhip.com/virtualink/ebooks) lists 6 ebook products. Prices range from $4.99 to $5.99. Two items show "On Sale" with struck-through original prices. One product (Ultimate AI Bundle) displays seller-written text "OVER 10,000 COPIES SOLD!!!" and a "Get 40% Off Now" promotional banner.

**Verbatim snippet (products and prices):**
- SaaS: Everything You Need to Know About Building Successful SaaS Company in One Place — $4.99
- Ultimate AI Bundle — $4.99 (On Sale; was $9.99, struck through)
- Top 50 Questions About AI — $4.99
- Top 50 Questions People Ask AI — $4.99
- Book About AI — $4.99
- Reinforcement Learning Explained - A Step-by-Step Guide to Reward-Driven AI — $5.99 (On Sale; was $11.99, struck through)

Popularity text: "OVER 10,000 COPIES SOLD!!!"
Promo banner: "⇊ Get 40% Off Now ⇊"
Stock display: "Only -1 left" (likely a bug or unlimited stock indicator)

**Source URL:** https://payhip.com/virtualink/ebooks
**source_type:** product_listing
**Date:** Accessed April 2026; page undated
**Verification:** direct_verified
**Notes:** "OVER 10,000 COPIES SOLD" is seller-written text in the product description, not a platform-generated metric. No star ratings or review counts visible. 6 products observed with "View All" link suggesting more may exist.

---

### A11. NTT Solmare / Sol Store — ASMR and visual novel digital products, multi-language

**What:** Sol Store (NTT Solmare) lists 16 products on page 1 of 2. Products are ASMR audio for the mobile game "Obey Me!" and side stories for "Ex and Bee." Prices: $14.99 (ASMR items), $9.99 (side stories), $29.97 (bundle of 3 side stories), and Free (4 "Quick Cast Talk" items). Both English and Japanese versions are sold.

**Verbatim snippet (selected products and prices):**
- Obey Me! ASMR - Leviathan: The Bathtub and You — $14.99
- Obey Me! ASMR - Belphegor To Wish Upon a Star With You — $14.99
- Side Story: Meeting in the Rain with Bee — $9.99
- Must-Have! Side Story Bundle — $29.97
- Free: Quick Cast Talk #1 — Free
- 【Obey Me!ASMR】case.レヴィアタン ～君とバスタブのすべて～ — $14.99

**Source URL:** https://payhip.com/NTTsolmare
**source_type:** product_listing
**Date:** Accessed April 2026; page undated
**Verification:** direct_verified
**Notes:** 16 products visible on page 1; pagination indicates page 2 exists. Bundle price ($29.97) equals 3× individual price ($9.99). No reviews/ratings visible. No PayPal listed as payment method for this store (only Maestro, Mastercard, Visa, Discover).

---

### A12. Purge it with Patti store — E-books & Digital Journals collection

**What:** The Purge it with Patti store lists 4 products in its "E-books & Digital Journals" collection. Three products priced at $14.95, one at $7.99. Store has 5 collections visible.

**Verbatim snippet (collections):** "All Products | Purge it with Patti | Paperback Books & Journals | E-books & Digital Journals | My Next Chapter Habit Trackers"

**Verbatim snippet (products and prices):**
- Purge it Plan E-Book | Detoxify Your Body Digital Download E-Book | Recipes for Detoxing Your Body | Weight Loss | Reset Your Body and Mind — $14.95
- Detox Diary Prep for the Purge, Digital Journal with Unlimited Pages, Printable, Goodnotes, Journal Mind, Body, Soul, Faith Based, Declutter Pantry, Reflection Journal — $7.99
- Pray it Like You Mean It - Digital Prayer Journal — $14.95
- Read it Like You Mean It - Digital Bible Study Journal — $14.95

**Source URL:** https://payhip.com/purgeitwithpatti
**source_type:** product_listing
**Date:** Accessed April 2026; page undated
**Verification:** direct_verified
**Notes:** No reviews/ratings visible. No sale indicators. Store tagline: "A faith- and plant-based approach for high-performing women ready for a physical, mental, and spiritual transformation"

---

### A13. Product page — Serviceform store, uniform £1.99 pricing with "On Sale" tag

**What:** The Serviceform Design & Print store (product page for "Pricing List, Price List Flyer") shows £1.99 pricing. The "You Might Also Like" section shows 10 additional products, ALL priced at £1.99, all Canva template products.

**Verbatim snippet (You Might Also Like products, all £1.99):**
- Canva Newsletter Template Fashion — £1.99
- Unicorn Sparkle with Heart Monogram — £1.99
- CANVA Workout Planner - Fitness Logbook — £1.99
- Editable Project Cover Design Avocado — £1.99
- KDP Canva Editable Workout and Meal Plan — £1.99
- CANVA Accounting Ledger 8,5x11 — £1.99
- 2024 Calendar - Canva Editable Template — £1.99
- Editable Cover Design Nanny Notes — £1.99
- 2024 Small Business Planner for Canva — £1.99
- CANVA Order Form KDP Template — £1.99

**Source URL:** https://payhip.com/b/gniq2
**source_type:** product_listing
**Date:** Accessed April 2026; page undated
**Verification:** direct_verified
**Notes:** Product marked "On Sale" but price and original price both show £1.99. 11 products observed total on this page. All are Canva template products.

---

### A14. Homepage footer — resource hub reveals promoted product types

**What:** Payhip's footer "Resources" section reveals the product types the platform actively promotes: presets, printables, ebooks, Canva templates, and online courses.

**Verbatim snippet:** "Resources: Marketing ideas tool, How to write an ebook, How to sell presets, How to sell printables, How to sell ebooks, How to sell canva templates, Online Course Ideas, Content Creator, Digital Products, Resource Hub"

**Source URL:** https://payhip.com/
**source_type:** product_listing
**Date:** Accessed April 2026; page undated
**Verification:** direct_verified

---

### A15. Homepage — navigation features dropdown shows product types and tools

**What:** The top navigation "Features" dropdown explicitly lists sellable product types (Digital Downloads, Online Courses, Coaching, Memberships, Physical Products) and growth tools (Store Builder, Payment Gateways, VAT & Taxes, Marketing Tools, Email Marketing).

**Verbatim snippet:** "Features > Sell: Digital Downloads, Online Courses, Coaching, Memberships, Physical Products / Features > Grow: Store Builder, Payment Gateways, VAT & Taxes, Marketing Tools, Email Marketing"

**Source URL:** https://payhip.com/
**source_type:** product_listing
**Date:** Accessed April 2026; page undated
**Verification:** direct_verified

---

### A16. Blog — recent content is competitor-comparison focused (April 2026)

**What:** The Payhip blog's most recent posts (April 2026) are predominantly competitor-comparison articles, not marketplace/catalog feature announcements. Blog has 20 pages of posts.

**Verbatim snippet (recent titles and dates):**
- "5 Amazon KDP Alternatives for Self-Published Authors" — Nicole Martins Ferreira, April 9, 2026
- "5 Sellfy Alternatives That Are Clearly Better Replacements" — Nicole Martins Ferreira, April 8, 2026
- "6 Selly Alternatives for Selling Online in 2026" — Nicole Martins Ferreira, April 7, 2026
- "Payhip Vs Etsy: Which is Better in 2026?" — Nicole Martins Ferreira, April 7, 2026
- "6 Lemon Squeezy Alternatives for Selling Digital Products" — Nicole Martins Ferreira, April 6, 2026
- "Top Ebook Topic Ideas in 2026: What do readers want?" — Abs @ Payhip, April 2, 2026

**Source URL:** https://payhip.com/blog
**source_type:** blog
**Date:** April 2026
**Verification:** direct_verified

---

### A17. Blog — 2024 features included wishlists and running sales

**What:** Payhip launched customer wishlists and a "running sales" feature in 2024.

**Verbatim snippet:** "Your customers can now create wishlists for your products!" and "Running a sale has never been easier! The running sales feature allows you to set up temporary price reductions for specific products or your entire store."

**Source URL:** https://payhip.com/blog/exciting-new-features-launched-in-2024/
**source_type:** blog
**Date:** 2024 (exact month not captured)
**Verification:** direct_verified

---

### A18. Blog — 2025 feature roundup (no marketplace discovery features)

**What:** Payhip's 2025 feature roundup covers Content Editor, Collaborations, 11 new payment gateways, improved coupon tools, cross-selling improvements, order notes, dark mode, archive products, product variants, API for coupons/license keys. No marketplace-specific discovery or catalog features were announced.

**Verbatim snippet:** Title: "What's New at Payhip: 2025 Feature Round‑Up" — Abs @ Payhip, October 1, 2025 (last updated December 30, 2025), 27 Comments

**Source URL:** https://payhip.com/blog/whats-new-at-payhip-2025/
**source_type:** blog
**Date:** October 1, 2025 (last updated December 30, 2025)
**Verification:** direct_verified

---

### A19. Payhip SEO features — built-in, limited scope

**What:** Payhip offers built-in SEO features: meta titles, SEO descriptions per collection, image alt texts, custom product URLs (with custom domain), and auto-generated sitemap.xml (regenerated every 24 hours).

**Verbatim snippet:** "By default, Payhip will use your about me description as your store description, but this can be changed by editing the SEO description of your All Products collection... Custom Domains now have a sitemap.xml and it gets autogenerated every 24 hours."

**Source URL:** https://help.payhip.com/article/218-optimize-seo
**source_type:** article
**Date:** Accessed April 2026; page undated
**Verification:** direct_verified

---

### A20. Payhip Collections system — seller-defined category groupings

**What:** Payhip offers a "Collections" feature allowing sellers to group products into categories within their own store.

**Verbatim snippet:** "Collections allow your customers to buy your products based on categories easily. You might have a particular group of products that naturally fit together, and it could make a lot of sense to display them as a collection on your store page, making shopping easier for your customers."

**Source URL:** https://help.payhip.com/article/74-collections
**source_type:** article
**Date:** Accessed April 2026; page undated
**Verification:** direct_verified

---

### A21. Payhip webhooks — 4 event types

**What:** Payhip supports 4 webhook events for developer integrations.

**Verbatim snippet:** "Webhooks allow you to set up integrations which subscribe to certain events from your Payhip store. There are 4 webhook events available for you to listen from." Events: paid, refunded, subscription.created, subscription.deleted. "If your endpoint does not return a 200 HTTP status code, the POST is retried once an hour for up to 3 hours."

**Source URL:** https://help.payhip.com/article/115-webhooks
**source_type:** article
**Date:** Accessed April 2026; page undated
**Verification:** direct_verified

---

### A22. Payhip Public API (v2) — limited to license keys and coupons

**What:** Payhip's public API currently supports license key management and coupon CRUD operations only.

**Verbatim snippet:** "We have an API available for managing coupons and license keys, you can find the instructions here: https://payhip.com/api-reference · In the future, we plan to expand the API to support many more resource types."

**Source URL:** https://help.payhip.com/article/347-public-api
**source_type:** article
**Date:** Accessed April 2026; page undated
**Verification:** direct_verified

---

### A23. Payhip mobile app — sales monitoring only, no product upload

**What:** Payhip has a mobile app for monitoring sales and analytics, but product uploads and store design changes must be done via web dashboard.

**Verbatim snippet:** "The app makes it easy to monitor your sales in real time, view analytics and sales metrics, and receive instant notifications for new orders." … "At the moment, all product uploads (digital downloads, courses, coaching, memberships, and physical products) as well as store design changes must be managed via the web dashboard."

**Source URL:** https://help.payhip.com/article/348-payhip-mobile-app
**source_type:** article
**Date:** Accessed April 2026; page undated
**Verification:** direct_verified

---

### A24. Google Analytics 4 integration — built-in

**What:** Payhip natively integrates with Google Analytics 4, sending a "Purchase" key event on checkout completion.

**Verbatim snippet:** "By default, we send a 'Purchase' key event to Google Analytics whenever someone completes the checkout process on your Payhip store... Whilst Payhip has some built-in Analytics features, we recommend connecting your store to Google Analytics for more advanced insights."

**Source URL:** https://help.payhip.com/article/93-google-analytics
**source_type:** article
**Date:** Accessed April 2026; page undated
**Verification:** direct_verified

---

### A25. Payhip free store themes

**What:** Payhip offers free, customizable store themes with no coding required.

**Verbatim snippet:** "Free beautifully designed store themes that are fully customizable. Every theme is just a starting point. No coding or HTML required."

**Source URL:** https://payhip.com/themes
**source_type:** product_listing
**Date:** Accessed April 2026; page undated
**Verification:** direct_verified

---

### A26. Payhip Partner (Affiliate) Program — 50% recurring commission

**What:** Payhip offers a partner program with 50% lifetime recurring commissions and no earning cap.

**Verbatim snippet:** "You are a partner in more than name and share 50% of our revenue from anyone you refer. Lifelong recurring commissions. Our commissions are for life. You continue to earn from stores which you referred years earlier. Unlimited earning potential. There is no cap on the amount you can earn as a partner."

**Source URL:** https://payhip.com/partner-program
**source_type:** product_listing
**Date:** Accessed April 2026; page undated
**Verification:** direct_verified

---

### A27. Payhip built-in analytics — Sales/Views, Visitor Sources, Conversion Rate

**What:** Payhip has built-in analytics covering sales/views, visitor sources, and conversion rate, described as basic.

**Verbatim snippet:** "Analytics helps you understand exactly where you should dedicate your focus on with powerful, in-depth analytics." … Visitor Sources help article states: "These analytics are enough to get you started with tracking visitor sources. If you need more in-depth information then we recommend connecting your Google Analytics account to Payhip."

**Source URL:** https://payhip.com/features/analytics
**source_type:** article
**Date:** Accessed April 2026; page undated
**Verification:** direct_verified

---

### A28. Payhip pricing plans — Free ($0 + 5%), Plus ($29/mo + 2%), Pro ($99/mo + 0%)

**What:** Payhip offers three pricing tiers. All features are available on all plans (no feature-gating). All plans support unlimited products and unlimited revenue.

**Verbatim snippet:** "Free Forever: $0/mo + 5% transaction fee — All features / Unlimited products / Unlimited revenue" … "Plus: $29/mo + 2% transaction fee" … "Pro: $99/mo + No transaction fee" … "At Payhip, our goal is to make pricing as simple and transparent as possible. So, no feature-gating here! You'll get access to all of our amazing features to help you grow your business, even on our free plan."

**Source URL:** https://payhip.com/pricing
**source_type:** product_listing
**Date:** Accessed April 2026; page undated
**Verification:** direct_verified

---

### A29. File type support — most types accepted, security exclusions listed

**What:** Payhip supports most file types for digital products including PDFs, audio, video, and ZIP files, with each file up to 5GB. EXE, ISO, DMG, VBS, SCR, and JAR are excluded.

**Verbatim snippet:** "You can upload multiple files, including ebooks, PDFs, audio, video, or other file types. Each file can be up to 5GB in size." … "We support most file types, including PDFs, audio, video, ZIP files, and more. However, certain file types such as EXE, ISO, DMG, VBS, SCR, and JAR are not supported."

**Source URL:** https://help.payhip.com/article/59-adding-a-digital-product
**source_type:** article
**Date:** Accessed April 2026; page undated
**Verification:** direct_verified

---

## GROUP B — PROVISIONALLY VERIFIED
*(Source blocked but content recovered via cache/mirror/search index tied to exact URL)*

---

### B1. Zapier integration — connects Payhip with 8,000+ apps

**What:** Payhip integrates with Zapier, offering triggers for New Sale, Sale Refund, New Membership Subscription, Cancel Membership Subscription, and New Product Added. Connects to 8,000+ apps.

**Verbatim snippet:** "Instantly connect Payhip with the apps you use everyday. Payhip integrates with 8,000 other apps on Zapier - it's the easiest way to automate your work."

**Source URL:** https://zapier.com/apps/payhip/integrations
**source_type:** database_profile
**Date:** Accessed April 2026; page undated
**Verification:** blocked_url_index_verified (content from search snippet tied to exact URL)

---

### B2. Pabbly Connect — alternative automation platform for Payhip

**What:** Pabbly Connect offers Payhip integration as an alternative to Zapier, triggering on successful transactions.

**Verbatim snippet:** "With Pabbly Connect, you can easily connect and integrate Payhip with different applications associated with CRM, Sales, Marketing, Productivity, or any apps." … "Unlike others, Pabbly Connect does not charge for trigger and internal steps."

**Source URL:** https://www.pabbly.com/connect/integrations/payhip/
**source_type:** database_profile
**Date:** Accessed April 2026; page undated
**Verification:** blocked_url_index_verified

---

### B3. Pipedream — developer-focused Payhip integration

**What:** Pipedream offers Payhip API integration for developers, with webhook events (paid, subscription.created, refunded, subscription.deleted) and actions (Disable/Enable/Verify license key).

**Verbatim snippet:** "Pipedream enables developers to easily integrate the Payhip API with more than 3,000 other applications remarkably fast. Join the 1,000,000+ developers using the Pipedream platform today. Free to get started."

**Source URL:** https://pipedream.com/apps/payhip
**source_type:** database_profile
**Date:** Accessed April 2026; page undated
**Verification:** blocked_url_index_verified

---

### B4. Make.com — community-developed Payhip module

**What:** Make.com (formerly Integromat) has a community-developed Payhip integration module, not officially supported by Make.

**Verbatim snippet:** "payhip is an e commerce platform that enables users to sell digital products, memberships, and courses directly online integrating with make com allows automation of sales, customer management, and product delivery workflows" … "payhip is a community developed application and is subjected to the developer's terms and conditions... make does not maintain or support this integration"

**Source URL:** https://apps.make.com/payhip-p5v3ea
**source_type:** database_profile
**Date:** Accessed April 2026; page undated
**Verification:** blocked_url_index_verified

---

### B5. BookFunnel — ebook/audiobook delivery integration

**What:** BookFunnel integrates with Payhip via webhooks to automatically deliver ebook/audiobook download links and handle reader tech support.

**Verbatim snippet:** "With BookFunnel Delivery Actions, you can sell your book on Payhip and BookFunnel will send a unique, private download link to your buyer automatically! We'll also handle any tech support if the reader has trouble transferring the book to their reading device."

**Source URL:** https://authors.bookfunnel.com/help/setup-payhip/
**source_type:** article
**Date:** Accessed April 2026; page undated
**Verification:** blocked_url_index_verified

---

### B6. Payhip WordPress plugin (official) — shortcode embedding

**What:** Payhip has an official free WordPress plugin for embedding products via shortcodes, with ESP integrations.

**Verbatim snippet:** "The Payhip WordPress plugin allows you to embed all your products anywhere on your WordPress site simply using a short code. Customers can click on each product and buy from you directly. We provide you with your customers emails so you can build up your mailing list."

**Source URL:** https://wordpress.com/plugins/payhip-sell-ebooks
**source_type:** database_profile
**Date:** Accessed April 2026; page undated
**Verification:** blocked_url_index_verified

---

### B7. WP Payhip Integration (third-party by Robin Phillips)

**What:** A free third-party WordPress plugin that automatically converts Payhip product page links into "Buy" overlay boxes.

**Verbatim snippet:** "Integrates Payhip into WordPress. When a Payhip product page link is clicked, it will open a Payhip 'Buy' box. To use, just install and activate the plugin. There are no settings, it will automatically work on all links to Payhip product pages, both existing and new ones."

**Source URL:** https://wordpress.org/plugins/wp-payhip-integration/
**source_type:** database_profile
**Date:** Accessed April 2026; page undated
**Verification:** blocked_url_index_verified

---

### B8. Common Ninja — search widget for Payhip stores

**What:** Common Ninja offers a Google-powered search bar widget that can be embedded in Payhip stores.

**Verbatim snippet:** "Enhance your Payhip store's user experience with the Search Bar Widget. Provide fast, accurate, and customizable search functionality powered by Google... The Payhip Website Search widget leverages Google's powerful search engine, ensuring fast and accurate results."

**Source URL:** https://www.commoninja.com/widgets/google-search/payhip
**source_type:** database_profile
**Date:** Accessed April 2026; page undated
**Verification:** blocked_url_index_verified

---

### B9. Fiverr — 549 Payhip freelance services available

**What:** Fiverr lists 549 freelance services specifically tagged as "payhip" services, covering store setup, product listing optimization, design, and consulting.

**Verbatim snippet:** "Best payhip freelance services online. Outsource your payhip project and get it quickly done and delivered remotely online"

**Source URL:** https://www.fiverr.com/gigs/payhip
**source_type:** search_results_page
**Date:** Accessed April 2026; page undated
**Verification:** blocked_url_index_verified
**Notes:** "549 services available" observed in search results. Price range noted as from $5 to $150+.

---

### B10. Etsy — Payhip template market exists

**What:** Payhip-specific store templates and graphics are sold on Etsy.

**Verbatim snippet:** "Check out our payhip template selection for the very best in unique or custom, handmade pieces from our templates shops."

**Source URL:** https://www.etsy.com/market/payhip_template
**source_type:** search_results_page
**Date:** Accessed April 2026; page undated
**Verification:** blocked_url_index_verified

---

### B11. Payhip blog — ebook pricing guidance ($2.99–$9.99 range, PWYW data)

**What:** Payhip's own blog suggests $2.99–$9.99 as a common ebook price range and reports that 43% of pay-what-you-want buyers pay above the minimum.

**Verbatim snippet:** "While pricing your ebook between 2.99 and 9.99 might feel a bit low, consider having an upsell in your ebook... On Payhip, you can sell any digital products, not just ebooks." … "a Payhip survey found that more than 43% of buyers pay above the minimum price set by the seller."

**Source URL:** https://payhip.com/blog/ebook-pricing/
**source_type:** blog
**Date:** Accessed April 2026; page undated
**Verification:** blocked_url_index_verified (content from search snippet tied to exact URL)

---

### B12. Payhip blog — launch pricing pattern ($19.99 regular / $9.99 launch)

**What:** Payhip's blog on selling ebooks describes a common launch pricing pattern.

**Verbatim snippet:** "Many ebook authors launch their ebook at a special, temporary low price. For instance, they might have a regular price of $19.99 but launch at $9.99."

**Source URL:** https://payhip.com/blog/how-to-sell-ebooks/
**source_type:** blog
**Date:** Accessed April 2026; page undated
**Verification:** blocked_url_index_verified

---

### B13. Payhip — resume template price range ($3–$60)

**What:** Payhip's own landing page for selling resume templates states a price range.

**Verbatim snippet:** "Resume templates usually sell for about $3-60 depending on the design and complexity of the resume."

**Source URL:** https://payhip.com/sell-resume-templates-online
**source_type:** article
**Date:** Accessed April 2026; page undated
**Verification:** blocked_url_index_verified

---

### B14. Payhip — course video hosting costs $5/month

**What:** Payhip charges $5/month for video hosting for online courses (up to 16 hours of video).

**Verbatim snippet:** "Video lessons have one simple fixed price of $5 per month" … "From one-off pricing, subscriptions, payment plans and entirely free. You're 100% in control of pricing."

**Source URL:** https://payhip.com/features/sell-courses
**source_type:** product_listing
**Date:** Accessed April 2026; page undated
**Verification:** blocked_url_index_verified

---

### B15. TechHubInsider — recommended tools article for Payhip sellers

**What:** A third-party article lists recommended tools for Payhip store optimization, including Canva Pro, TidyCal, MailerLite, Carrd ($19/year), TinyPNG, Fathom Analytics, and SurferSEO.

**Verbatim snippet (TidyCal):** "Payhip supports coaching and online sessions, but if you're offering calls or coaching packages, TidyCal is a great external tool that plays nicely with Payhip. Embed booking links directly on your product or confirmation pages."

**Verbatim snippet (MailerLite):** "while Payhip has a basic email marketing tool, it's not built for automation-heavy campaigns or serious segmentation. That's where MailerLite comes in."

**Verbatim snippet (Carrd):** "Payhip gives you a solid storefront, but sometimes you need something a bit more flexible—especially if you're doing affiliate marketing, blogging, or just want a branded homepage that links to your Payhip store... Create one-page websites in minutes (no coding). Embed your Payhip products or link directly to them." Pricing: "$19/year"

**Source URL:** https://techhubinsider.com/best-tools-to-customize-and-optimize-your-payhip-store-in-2025/
**source_type:** article
**Date:** 2025 (per title; exact date not captured)
**Verification:** blocked_url_index_verified

---

### B16. Product page — VRChat avatar with limited-time pricing (€35 → €65)

**What:** A VRChat avatar product on Payhip uses time-limited promotional pricing in EUR.

**Verbatim snippet (from search index):** "Available for 35€ until March 1th, After that — the price rises to 65€"

**Source URL:** https://payhip.com/b/75OWj
**source_type:** product_listing
**Date:** Accessed April 2026; page undated
**Verification:** blocked_url_index_verified (from Google search snippet tied to exact URL)

---

### B17. Product page — software synth editor priced at €6.90

**What:** A Roland Boutique JU-06A Editor software product is listed at €6.90.

**Verbatim snippet (from search index):** "Price 6,90 € (About 7 US Dollars)"

**Source URL:** https://payhip.com/b/jLFv4
**source_type:** product_listing
**Date:** Accessed April 2026; page undated
**Verification:** blocked_url_index_verified

---

### B18. Product page — craft pattern with pay-what-you-want pricing

**What:** An "Electric Skylines shawl pattern" uses pay-what-you-want pricing where the listed price is the minimum.

**Verbatim snippet (from search index):** "pay what you feel program... price listed is the minimum"

**Source URL:** https://payhip.com/b/AKMI
**source_type:** product_listing
**Date:** Accessed April 2026; page undated
**Verification:** blocked_url_index_verified

---

### B19. Semrush — 10.55M monthly visits to payhip.com (Feb 2026)

**What:** Semrush estimates payhip.com received 10.55 million visits in February 2026 with average session duration of 8 minutes and 4 seconds.

**Verbatim snippet:** "In February payhip.com received 10.55M visits with the average session duration 08:04"

**Source URL:** https://www.semrush.com/website/payhip.com/overview/
**source_type:** report
**Date:** Last updated March 12, 2026
**Verification:** blocked_url_index_verified (from search snippet tied to exact URL)
**Notes:** Third-party estimate, not Payhip's own data.

---

## GROUP C — COULD NOT VERIFY
*(Source couldn't be fully accessed, text from generic search snippet, or secondary retelling)*

---

### C1. Blogging Wizard — six product types on Payhip

**What:** A third-party review identifies six product types sellable on Payhip.

**Verbatim snippet:** "There are six types of products you can sell with Payhip: Digital products (i.e. ebooks, software, photos, etc.), Courses, Memberships, Physical Products, Coaching Services, and Bundles."

**Source URL:** https://bloggingwizard.com/payhip-review/
**source_type:** article
**Date:** Accessed April 2026; page undated
**Verification:** could_not_verify (search snippet only; page not fully accessed)
**Notes:** Consistent with directly verified homepage data (A9). Adds "Bundles" as a sixth type not explicitly shown as separate category on homepage.

---

### C2. Medium — Hazel Paradise compares Gumroad's "Discover" vs Payhip

**What:** A creator notes that Gumroad's "Discover" feature generates organic sales, and compares fee structures: Payhip 5% vs Gumroad 10%.

**Verbatim snippet:** "Pricing — Payhip takes 5% per transaction and Gumroad takes 10% per transaction" … "Discover Option — I didn't know this before until I got a sale from Gumroad itself. Yes, people go directly to Gumroad to buy products."

**Source URL:** https://medium.com/@hazelparadise/why-i-chose-gumroad-over-payhip-8821ae348d45
**source_type:** article
**Date:** Accessed April 2026; page undated
**Verification:** could_not_verify (search snippet only)
**Notes:** Provides comparative marketplace discovery context. Author uses both platforms.

---

### C3. Medium — Creator reports $33,000 in 3 months on Payhip

**What:** A Medium author claims $33,000 in Payhip sales over 3 months using email marketing and articles.

**Verbatim snippet:** "I've made $33,000 on Payhip in 3 months without being a slave to social media. I've used email marketing mostly and articles."

**Source URL:** https://edinajackson.medium.com/ive-made-33-000-on-payhip-in-3-months-without-posting-on-social-media-apps-73e3a29ab932
**source_type:** article
**Date:** Accessed April 2026; page undated
**Verification:** could_not_verify (search snippet only; self-reported, unverifiable income claim)
**Notes:** Author (Edina Jackson) has multiple Medium posts about Payhip income and appears to be a content marketer/affiliate. Claims should be treated with skepticism.

---

### C4. Medium — Creator reports $5,543 in one week on Payhip

**What:** Same Medium author claims $5,543 in one week from e-books, courses, and done-for-you offers.

**Verbatim snippet:** "Last week, I made $5,543 on the platform... I use Payhip to sell digital products such as e-books and courses. I also use it for my done-for-you offers."

**Source URL:** https://edinajackson.medium.com/i-made-5-543-in-a-week-on-payhip-d1f33aff6d29
**source_type:** article
**Date:** Accessed April 2026; page undated
**Verification:** could_not_verify (search snippet only; same author as C3, same caveats)

---

### C5. Medium — New seller reports $20 first-day revenue from 3 products at $1–$5

**What:** A Medium author reports creating 3 digital products and earning $20 on day one, testing prices of $1, $5, and pay-what-you-want.

**Verbatim snippet:** "Created a 'reading log template' in half an hour. Designed a small set of motivational quote posters (A4 JPGs). Wrote a short guide: '5 Tricks to Build a Micro-business in a Weekend.' Within 24 hours I had three live products. Tested $1 prices, $5, and the pay-what-you-want model... By day end, $20 in revenue"

**Source URL:** https://medium.com/@reennamatovu/how-i-started-a-digital-business-in-just-one-day-with-payhip-376035b928a9
**source_type:** article
**Date:** Accessed April 2026; page undated
**Verification:** could_not_verify (search snippet only)
**Notes:** Useful for price-testing pattern observation: $1, $5, and PWYW as entry-level price points.

---

### C6. Medium — "63% of new Payhip sellers make no sales in first 90 days"

**What:** A Medium article claims that over 63% of new Payhip sellers make no sales in their first 90 days, attributing the statistic to "Oberlo, 2025."

**Verbatim snippet:** "over 63% of new Payhip sellers make no sales in their first 90 days (Oberlo, 2025)"

**Source URL:** https://medium.com/@proacademia/5-reasons-your-payhip-digital-products-arent-selling-and-how-to-fix-it-in-2025-e09df9bbf805
**source_type:** article
**Date:** Accessed April 2026; page undated
**Verification:** could_not_verify (search snippet only; attribution to "Oberlo, 2025" is suspect — may be a general digital product statistic, not Payhip-specific)

---

### C7. CheckThat.ai — Free/Plus plan break-even at $967/month revenue

**What:** A third-party analysis calculates that the break-even point between Payhip's Free plan (5% fee) and Plus plan ($29/mo + 2% fee) is $967/month in revenue.

**Verbatim snippet:** "Upgrade when your monthly revenue consistently exceeds $967. At this point, the Plus plan's $29 subscription plus 2% fees costs the same as the Free plan's 5% fees."

**Source URL:** https://checkthat.ai/brands/payhip/pricing
**source_type:** article
**Date:** Accessed April 2026; page undated
**Verification:** could_not_verify (search snippet only)
**Notes:** Math checks out: $967 × 0.05 = $48.35; $29 + ($967 × 0.02) = $48.34. Verified by calculation.

---

### C8. Payhip blog — ebook statistics, positioning vs Amazon pricing

**What:** Payhip positions itself as enabling higher ebook pricing compared to Amazon's $2.99–$9.99 commission sweet spot.

**Verbatim snippet:** "Unlike Amazon, which encourages authors to price ebooks between $2.99 and $9.99 to earn the highest commission percentage... If you'd rather sell ebooks at a higher price point above $9.99, you can earn more revenue... by hosting your ebooks on your own Payhip store. Payhip only takes a 5% transaction fee for each eBook sale. That means you get to pocket 95% of your sales."

**Source URL:** https://payhip.com/blog/ebook-statistics/
**source_type:** blog
**Date:** Accessed April 2026; page undated
**Verification:** could_not_verify (search snippet; blog page not fully fetched)

---

### C9. Payhip blog — Canva templates selling at ~$10, Etsy benchmark 1,000–3,000 sales

**What:** Payhip's blog references Etsy data showing Canva template listings achieving 1,000–3,000 sales at approximately $10 each.

**Verbatim snippet:** "A quick look into Etsy reveals that a product listing for Canva templates can get up to 1000-3000 sales. Each of these templates sell for approximately $10, so the seller has earned approximately $10,000-$30,000 on that particular product listing alone!"

**Source URL:** https://payhip.com/blog/how-to-sell-canva-templates/
**source_type:** blog
**Date:** Accessed April 2026; page undated
**Verification:** could_not_verify (search snippet; this is Etsy data, not Payhip-observed data)

---

### C10. The Product Store — multi-category physical/digital store with prices $4.99–$80.00

**What:** Search results show a Payhip store called "The Product Store" with categories including New Arrivals, ON SALE!, Dj's Diggin in the Crates, Women's Products, Mens Products, Books, Furniture, Dog Products, Toys.

**Verbatim snippet (from search index):** Prices: $7.49, $8.50, $4.99, $55.00, $80.00, "On Sale", $17.48. Categories: "All Products, New Arrivals, ON SALE!, Dj's Diggin in the Crates, Women's Products, Mens Products, Books, Furniture, Dog Products, Toys"

**Source URL:** https://payhip.com/theproductstore
**source_type:** product_listing
**Date:** Accessed April 2026; date of listing unknown
**Verification:** could_not_verify (URL redirects to Payhip homepage when fetched; store may be removed or reconfigured. Data from search index only.)

---

### C11. Whop.com — notes "limited SEO capabilities" on Payhip

**What:** A competitor (Whop) claims Payhip has limited SEO capabilities.

**Verbatim snippet:** "Limited SEO capabilities: You can't customize URLs or set meta descriptions, which affects your store's search visibility."

**Source URL:** https://whop.com/blog/gumroad-vs-payhip/
**source_type:** article
**Date:** Accessed April 2026; page undated
**Verification:** could_not_verify (search snippet only; this claim appears contradicted by Payhip's own SEO help docs [A19] which show meta descriptions and custom URLs are available with custom domains)

---

## GROUP D — ABSENCE FINDINGS
*(Actively searched but found no data)*

---

### D1. No product counts found anywhere

**Searched for:** Total number of products on Payhip marketplace, per-category product counts, catalog size metrics.
**Where searched:** payhip.com/marketplace (direct fetch), all marketplace category pages (direct fetch), payhip.com homepage (direct fetch), Payhip help center (direct fetch), Payhip blog (direct fetch), Google searches for "payhip number of products," "payhip catalog size," "payhip marketplace products count."
**Result:** Payhip does not publicly display product counts anywhere. No page shows how many products exist in any category or on the platform overall. The marketplace category pages do not show "X products" counts.

---

### D2. No review counts or star ratings visible in static HTML

**Searched for:** Review counts, star ratings, review text on product listings and store pages.
**Where searched:** payhip.com/virtualink/ebooks (direct fetch), payhip.com/NTTsolmare (direct fetch), payhip.com/purgeitwithpatti (direct fetch), payhip.com/b/gniq2 (direct fetch), all marketplace category pages (direct fetch).
**Result:** No review counts or star ratings were visible on any page in static HTML, despite the marketplace having rating filter options (1–4+ stars). Reviews may be JavaScript-rendered or only visible on individual product detail pages.

---

### D3. No /explore URL exists on Payhip

**Searched for:** https://payhip.com/explore and all /explore/ sub-paths (ebooks, templates, courses, software, music, memberships).
**Where searched:** Direct fetch attempts, Google "site:payhip.com/explore" search.
**Result:** The /explore path does not exist on Payhip's website. The equivalent discovery feature is the Marketplace at https://payhip.com/marketplace. Individual stores may have /explore endpoints (e.g., payhip.com/somnetwork/explore) but there is no platform-level explore page.

---

### D4. No Payhip-specific Chrome extensions found

**Searched for:** Chrome extensions for Payhip sellers, Payhip browser tools.
**Where searched:** Google searches for "payhip chrome extension," "payhip browser extension."
**Result:** No dedicated Chrome extensions for Payhip sellers were found.

---

### D5. No dedicated Payhip analytics dashboard tools found

**Searched for:** Third-party analytics dashboards specifically for Payhip.
**Where searched:** Google searches for "payhip analytics dashboard tool," "payhip sales dashboard."
**Result:** No third-party dashboard specifically for Payhip analytics exists beyond GA4 integration and the built-in analytics. Fathom Analytics was recommended for Payhip stores but is a generic tool, not Payhip-specific.

---

### D6. No dedicated Payhip consulting firms found

**Searched for:** Consulting firms or agencies specializing in Payhip.
**Where searched:** Google searches for "payhip consulting services," "payhip agency."
**Result:** No dedicated consulting firm specializing in Payhip was found. The only consulting-adjacent services are individual Fiverr freelancers (B9: 549 services listed).

---

### D7. No public data on category dominance or catalog composition breakdown

**Searched for:** Data showing which categories have the most products, sales volume by category, or percentage breakdown of catalog composition.
**Where searched:** Payhip blog, Payhip help center, Google searches, Medium, third-party reviews and reports.
**Result:** No publicly available data exists about which marketplace categories are most populated or which generate the most sales. No category-level analytics or market share data is published by Payhip or any third party.

---

### D8. No blog posts about marketplace discovery improvements or new category additions

**Searched for:** Blog posts announcing new marketplace categories, discovery feature updates, or browse/search improvements.
**Where searched:** payhip.com/blog (direct fetch, 20 pages of blog content reviewed), 2024 and 2025 feature roundup posts (directly accessed).
**Result:** Neither the 2024 nor 2025 feature roundup posts mention marketplace discovery or category changes. No standalone blog post about marketplace improvements was found.

---

### D9. No pricing distribution data found

**Searched for:** Statistical distributions of product prices across Payhip's catalog (e.g., median price, price percentiles, average price by category).
**Where searched:** Payhip blog, help center, Google searches, third-party reports.
**Result:** No publicly available data exists about the distribution of product prices on Payhip.

---

## QUALIFIERS SUMMARY

**Price observations catalog (all directly or provisionally verified):**

| Source | Product Type | Prices Observed | Currency | Discount Pattern |
|---|---|---|---|---|
| payhip.com homepage | Digital downloads (cookbooks, fonts, fitness) | $5.95, $5.99, $10.00, $11.99, $14.99, $15.00, $19.00, $30.00, £4.50 | USD, GBP | None visible |
| virtualink/ebooks | AI ebooks | $4.99, $5.99 | USD | On Sale: $9.99→$4.99, $11.99→$5.99; "40% Off" promo |
| NTTsolmare | ASMR audio, visual novel side stories | $9.99, $14.99, $29.97 (bundle), Free | USD | Bundle = 3×$9.99; Free items exist |
| purgeitwithpatti | Health/faith e-books, journals | $7.99, $14.95 | USD | None visible |
| b/gniq2 store | Canva templates | £1.99 (uniform) | GBP | "On Sale" tag but no price difference |
| b/75OWj | VRChat avatar | €35 (limited-time), €65 (regular) | EUR | Time-limited: "until March 1th" |
| b/jLFv4 | Software (synth editor) | €6.90 | EUR | None |
| b/AKMI | Craft pattern (shawl) | PWYW (minimum listed) | — | Pay-what-you-want |
| Blog guidance | Ebooks (general) | $2.99–$9.99 (suggested range) | USD | Launch pattern: $19.99→$9.99 |
| Landing page | Resume templates | $3–$60 | USD | Range by complexity |

**Category names exactly as shown:** 3D, Roblox, Crafts, Music & Sound Design, Design, Drawing & Painting, Fiction Books, Fitness & Health, Photography, Writing & Publishing, Business & Money, Films, Comics & Graphic Novels, Audio, Recorded Music, Education, Gaming, Software Development

**Discovery mechanisms documented:** Marketplace category browse (18 categories + subcategories), Sort by (7 options), Price filter (6 tiers), Rating filter (5 levels), Related tags, "More filters" button, Featured products section, Collections (seller-defined), Tags (seller-applied), Per-store search (/search endpoint), Built-in SEO (meta titles, descriptions, sitemap.xml), Google Analytics 4 integration, Wishlist feature (launched 2024)

**Auxiliary services documented:** Zapier (8,000+ apps), Pabbly Connect, Pipedream, Make.com (community), BookFunnel (ebook delivery), Official WordPress plugin, WP Payhip Integration (third-party), WP Payhip Sell Digital (third-party), Common Ninja search widget, Fiverr freelance services (549 listed), Etsy template market, TidyCal, MailerLite, Carrd, TinyPNG, Fathom Analytics, SurferSEO (all recommended for Payhip in third-party article), Payhip Partner Program (50% recurring), Free store themes, Public API v2 (license keys + coupons), Webhooks (4 events), Mobile app (monitoring only)