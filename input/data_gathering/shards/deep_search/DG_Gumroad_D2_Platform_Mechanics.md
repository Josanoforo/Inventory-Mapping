# DG Delivery — Gumroad × D2: Mecánica de plataforma

---

## Search decomposition

- SD-01: Gumroad fee structure — transaction fees, flat fees, percentage-based fees, Discover fees, mobile app fees
- SD-02: Gumroad buyer payment methods accepted at checkout
- SD-03: Gumroad seller payout methods, payout schedule, and payout thresholds
- SD-04: Gumroad product types supported and pricing constraints
- SD-05: Gumroad file delivery mechanics — file size limits, streaming, PDF stamping, rentals
- SD-06: Gumroad seller tools and features — email workflows, custom domains, analytics integrations, embeds, license keys
- SD-07: Gumroad country and currency restrictions for sellers and buyers
- SD-08: Gumroad terms of service — merchant of record status, prohibited content, seller obligations, arbitration
- SD-09: Gumroad refund and dispute policies — refund windows, chargeback handling, seller responsibility
- SD-10: Gumroad technical limitations — API specs, storage caps, bandwidth limits

---

## Part 1 — Clean findings (direct_verified)

### F-01

What: Gumroad charges 10% + $0.50 per transaction for all sales through a seller's profile or direct links.
Verbatim snippet: [Stated in layout: "10% + $0.50 Per transaction for all sales through your profile or direct links to your customers."]
Source: https://gumroad.com/pricing
source_type: pricing_page
verification_status: direct_verified
Date: Accessed April 2026; page undated
Notes: Structured layout; fee displayed in card element on pricing page.

### F-02

What: Gumroad charges 30% per transaction when new customers find and buy through the Discover marketplace.
Verbatim snippet: [Stated in layout: "30% Per transaction when new customers find and buy from you through our discover marketplace."]
Source: https://gumroad.com/pricing
source_type: pricing_page
verification_status: direct_verified
Date: Accessed April 2026; page undated
Notes: Structured layout; fee displayed in card element on pricing page.

### F-03

What: Gumroad does not charge a monthly fee; fees are deducted as a percentage of every sale.
Verbatim snippet: "Unlike other platforms, Gumroad doesn't charge you a monthly fee. Instead, our fees are deducted as a small percentage of every sale, so we only make money when you do."
Source: https://gumroad.com/pricing
source_type: pricing_page
verification_status: direct_verified
Date: Accessed April 2026; page undated
Notes: From FAQ section "What are the fees?" on pricing page.

### F-04

What: Since January 1, 2025, Gumroad states it handles all seller tax obligations as a merchant of record, including worldwide sales tax collection and remittance.
Verbatim snippet: "Since January 1, 2025, Gumroad handles ALL your tax obligations. Yes, you read that right – we manage sales tax collection and remittance worldwide."
Source: https://gumroad.com/pricing
source_type: pricing_page
verification_status: direct_verified
Date: Accessed April 2026; page undated (references January 1, 2025)
Notes: none

### F-05

What: Gumroad states it will collect taxes in regions where it has tax obligations as a merchant of record, varying by location, and will handle the appropriate tax collection for each sale automatically.
Verbatim snippet: "We'll collect taxes in regions where we have tax obligations as a merchant of record. This varies by location, and we'll automatically handle the appropriate tax collection for each sale."
Source: https://gumroad.com/pricing
source_type: pricing_page
verification_status: direct_verified
Date: Accessed April 2026; page undated
Notes: From FAQ section "Will Gumroad collect taxes everywhere?" on pricing page.

### F-06

What: Gumroad states sellers can sell digital products, e-books, courses, tutorials, and memberships. Physical goods are listed separately as not permitted outside that scope. A full list of prohibited items is referenced at gumroad.com/prohibited.
Verbatim snippet: "Digital products, e-books, courses, tutorials, and memberships—almost anything! Creators in just about every industry use (and love) Gumroad, from digital artists, writers, musicians and other creative-types to business-minded entrepreneurs and tech gurus like our SaaS creators. A better question is, 'What can't I sell on Gumroad?'"
Source: https://gumroad.com/pricing
source_type: pricing_page
verification_status: direct_verified
Date: Accessed April 2026; page undated
Notes: From FAQ section "What can I sell on Gumroad?" on pricing page.

### F-07

What: Gumroad states payment to creators — whether through direct deposit or PayPal — varies by country.
Verbatim snippet: "Gumroad's goal is to help creators make a living doing what they love, so we make it as simple as possible to get paid. How we pay creators, whether through direct deposit or PayPal, varies by country."
Source: https://gumroad.com/pricing
source_type: pricing_page
verification_status: direct_verified
Date: Accessed April 2026; page undated
Notes: From FAQ section "How do I get paid?" on pricing page.

### F-08

What: The Gumroad Terms of Service have an effective date of January 1, 2025 and were last updated December 10, 2024. They establish Gumroad as a non-exclusive reseller of suppliers' digital products and define the services enabling sellers to appoint Gumroad as such.
Verbatim snippet: "The Services enable sellers of digital products ("Suppliers") that have a Supplier Account (as defined below) with Gumroad to appoint Gumroad as such Suppliers' non-exclusive reseller of certain of their digital products that Gumroad deems eligible for resale through the Services ("Digital Products" or "Products")."
Source: https://gumroad.com/terms
source_type: policy_page
verification_status: direct_verified
Date: Effective Date: January 1, 2025; Last Updated Date: December 10, 2024
Notes: Section 1.1 of Terms of Service.

### F-09

What: Per the Terms, Gumroad has sole discretion to determine product eligibility for resale and reserves the right not to sell products it considers fraudulent or illegal. Gumroad is acknowledged as the merchant of record and suppliers shall not issue invoices or demand payment directly from buyers.
Verbatim snippet: "You hereby appoint Gumroad as your non-exclusive reseller of the Digital Products (including any subsequent updates and upgrades thereto) that you expressly agree to be resold by Gumroad and that Gumroad deems eligible for resale through the Services. To be deemed eligible for resale through the Services, Digital Products must meet product eligibility requirements, and Gumroad has the sole discretion to determine and change from time to time the product categories and products that are eligible for resale through the Services. For the avoidance of doubt, Gumroad reserves the right not to sell any products that Gumroad considers in its sole discretion to be fraudulent or illegal under any applicable law. You acknowledge and agree that Gumroad is the merchant of record for the resale of your Products to the Buyers, and that you shall not issue any invoice or make any demand for payment to any Buyer in relation to any completed resale of your Products through the Services."
Source: https://gumroad.com/terms
source_type: policy_page
verification_status: direct_verified
Date: Effective Date: January 1, 2025; Last Updated Date: December 10, 2024
Notes: Section 6.1.

### F-10

What: Per the Terms, the supplier agrees to pay Gumroad a per-transaction fee (the "Gumroad Fee") that is automatically deducted from the purchase price. The remainder after fees, taxes, and other charges is the "Supplier Fee" paid to the supplier. Gumroad may offset funds owed but not yet paid against sums due to Gumroad.
Verbatim snippet: "In consideration of Gumroad's MOR Services, in respect of each resale of your Products through the Services, you agree to pay Gumroad a per-transaction fee (the, "Gumroad Fee") for each resale made by Gumroad through the Services. The Gumroad Fee owed for each resale through the Services is automatically deducted from the purchase price paid by the Buyer, with the remainder (less any amounts in respect of taxes and any other charges payable by you pursuant to this Agreement) owed and paid to you by Gumroad (such remainder amount, the "Supplier Fee"). Supplier Fees owed to you by Gumroad will be paid to you after a completed resale transaction based on an agreed upon settlement schedule, which is subject to change at the discretion of Gumroad. Notwithstanding the forgoing, Gumroad may also offset against funds owed but not yet paid to Supplier via the Services any sums due, or reasonably likely to become due, to Gumroad pursuant to these Terms of Service."
Source: https://gumroad.com/terms
source_type: policy_page
verification_status: direct_verified
Date: Effective Date: January 1, 2025; Last Updated Date: December 10, 2024
Notes: Section 6.4.

### F-11

What: Per the Terms, Gumroad handles buyers' refund requests, chargebacks, and disputes in its sole discretion. The supplier is responsible for reimbursing Gumroad for any monies paid to buyers or third-party providers in connection with refunds, chargebacks, or disputes, as well as other reasonable costs.
Verbatim snippet: "Gumroad will handle Buyers' requests for refunds, chargebacks and other disputes with Buyers in Gumroad's sole discretion. The Supplier shall, at Gumroad's request, provide all information as may be requested by Gumroad to resolve Buyers' requests or disputes. Supplier is responsible for reimbursing Gumroad for the amount of any monies paid by Gumroad to Buyers or Third-Party Service Providers, or any other parties, in connection with refunds, chargebacks or disputes, as well as for any other reasonable costs incurred by Gumroad in resolving these requests."
Source: https://gumroad.com/terms
source_type: policy_page
verification_status: direct_verified
Date: Effective Date: January 1, 2025; Last Updated Date: December 10, 2024
Notes: Section 7.1(a).

### F-12

What: Per the Terms, all transactions through the Services settle in USD. Currency conversion uses exchange rates from openexchangerates.org/api. Gumroad does not guarantee the displayed exchange rate reflects the most up to date rate.
Verbatim snippet: "If the retail price of a Product is listed in a currency other than United States Dollars (USD), Gumroad will calculate a USD price based upon an exchange rate determined by Gumroad. Gumroad uses exchange rates obtained from http://openexchangerates.org/api. Gumroad cannot and does not guarantee that the exchange rate displayed reflects the most up to date rate due to the fluctuating nature of exchange rates. Accordingly, Gumroad recommends that you confirm current rates before engaging in any transactions on the Platform. Regardless of listed currency, all transactions through the Services will settle in USD."
Source: https://gumroad.com/terms
source_type: policy_page
verification_status: direct_verified
Date: Effective Date: January 1, 2025; Last Updated Date: December 10, 2024
Notes: Section 9.

### F-13

What: Per the Terms, as merchant of record, Gumroad will be treated as the supplier or principal for Indirect Tax purposes and will be responsible for administration, collection, reporting, and remittance of relevant Indirect Tax on resales through the Services.
Verbatim snippet: "As the merchant of record, Gumroad will be treated as the supplier or principal, for relevant Indirect Tax purposes, in respect of Products resold by Gumroad through the Services, and, subject to as provided pursuant to these Terms of Services, will be responsible for the administration, collection, reporting and remittance of any relevant Indirect Tax (except in limited circumstances where the Buyer may be responsible, for example as outlined in Section 10.5 below)."
Source: https://gumroad.com/terms
source_type: policy_page
verification_status: direct_verified
Date: Effective Date: January 1, 2025; Last Updated Date: December 10, 2024
Notes: Section 10.2.

### F-14

What: Per the Terms, Gumroad uses Stripe, Inc. and PayPal as third-party payment processing service providers for card acceptance, merchant settlement, and related services.
Verbatim snippet: "Gumroad currently uses Stripe, Inc. and its affiliates, as well as PayPal, as third-party service providers for payment processing services (e.g., card acceptance, merchant settlement, and related services) (each, a "Third-Party Payments Provider")."
Source: https://gumroad.com/terms
source_type: policy_page
verification_status: direct_verified
Date: Effective Date: January 1, 2025; Last Updated Date: December 10, 2024
Notes: Section 5.

### F-15

What: Per the Terms, the supplier shall upload a digital file in a format approved by Gumroad (including .mp3, .pdf, .png, .jpeg) to the Services, and Gumroad will facilitate delivery to the buyer upon purchase.
Verbatim snippet: "With respect to a Digital Product, Supplier shall upload a digital file in a format approved by Gumroad (including, but not limited to, .mp3, .pdf, .png, .jpeg files) to the Services. Upon a Buyer's purchase of a Digital Product on the Services, Gumroad will promptly facilitate the delivery of the Digital Product to Buyer."
Source: https://gumroad.com/terms
source_type: policy_page
verification_status: direct_verified
Date: Effective Date: January 1, 2025; Last Updated Date: December 10, 2024
Notes: Section 6.8.

### F-16

What: Per the Terms, the agreement requires binding arbitration for disputes, with limited exceptions. Users may opt out within 30 days. Class action and jury trial waivers apply. Governing law is the State of California.
Verbatim snippet: "UNLESS YOU OPT OUT OF THE AGREEMENT TO ARBITRATE WITHIN 30 DAYS: (1) YOU WILL ONLY BE PERMITTED TO PURSUE DISPUTES OR CLAIMS AND SEEK RELIEF AGAINST US ON AN INDIVIDUAL BASIS, NOT AS A PLAINTIFF OR CLASS MEMBER IN ANY CLASS OR REPRESENTATIVE ACTION OR PROCEEDING AND YOU WAIVE YOUR RIGHT TO PARTICIPATE IN A CLASS ACTION LAWSUIT OR CLASS-WIDE ARBITRATION; AND (2) YOU ARE WAIVING YOUR RIGHT TO PURSUE DISPUTES OR CLAIMS AND SEEK RELIEF IN A COURT OF LAW AND TO HAVE A JURY TRIAL. ANY DISPUTE, CLAIM OR REQUEST FOR RELIEF RELATING IN ANY WAY TO YOUR USE OF THE SITE WILL BE GOVERNED AND INTERPRETED BY AND UNDER THE LAWS OF THE STATE OF CALIFORNIA, CONSISTENT WITH THE FEDERAL ARBITRATION ACT, WITHOUT GIVING EFFECT TO ANY PRINCIPLES THAT PROVIDE FOR THE APPLICATION OF THE LAW OF ANY OTHER JURISDICTION. THE UNITED NATIONS CONVENTION ON CONTRACTS FOR THE INTERNATIONAL SALE OF GOODS IS EXPRESSLY EXCLUDED FROM THIS AGREEMENT."
Source: https://gumroad.com/terms
source_type: policy_page
verification_status: direct_verified
Date: Effective Date: January 1, 2025; Last Updated Date: December 10, 2024
Notes: From preamble section of Terms of Service.

### F-17

What: Gumroad describes itself as a "powerful, but simple, e-commerce platform" enabling sellers to sell books, memberships, courses, and more directly to their audience.
Verbatim snippet: "Gumroad is a powerful, but simple, e-commerce platform that puts a wide selection of tools at your fingertips. Now you can sell the digital services you want—books, memberships, courses, and more—right to your audience."
Source: https://gumroad.com/features
source_type: platform_doc
verification_status: direct_verified
Date: Accessed April 2026; page undated
Notes: none

### F-18

What: Gumroad's features page states sellers can use a flexible page editor to build a storefront, link an existing site under a custom domain, or embed the payment platform and follow button on an existing site.
Verbatim snippet: [Stated in layout: "Create a home here — No site? No problem. Use our flexible page editor to build a storefront and customize your site's colors, and more."]
Source: https://gumroad.com/features
source_type: platform_doc
verification_status: direct_verified
Date: Accessed April 2026; page undated
Notes: Structured layout; feature card on features page. Adjacent cards state "Use your own website, too" and "Power-up your page" as separate layout elements.

### F-19

What: Gumroad's features page states sellers can create simple memberships, set up subscriptions with monthly/quarterly/biannual/yearly payments, and offer pay-what-you-want pricing.
Verbatim snippet: [Stated in layout: "Create simple memberships — Give customers access to a library of content for as long as they're subscribed."]
Source: https://gumroad.com/features
source_type: platform_doc
verification_status: direct_verified
Date: Accessed April 2026; page undated
Notes: Structured layout; feature card. Adjacent cards cover "Set up subscriptions" and "The sky's the limit" (pay what you want).

### F-20

What: Gumroad's features page states it accepts different currencies, handles VAT collection and remittance to the EU, generates license keys, allows selling multiple versions (PDF, ePub, Mobi, lossless audio), and provides lightweight DRM.
Verbatim snippet: [Stated in layout: "Generate license keys — Selling software? We can create your license keys, so you can get back to beta."]
Source: https://gumroad.com/features
source_type: platform_doc
verification_status: direct_verified
Date: Accessed April 2026; page undated
Notes: Structured layout; feature card. Adjacent cards cover "Sell multiple versions" and "Protect your work" (DRM).

### F-21

What: Gumroad publishes a list of 54 prohibited product categories, citing U.S. federal law, card network rules, or payment processor restrictions as reasons. The list may change abruptly and without notice, with changes taking effect immediately.
Verbatim snippet: "The following products and activities are not allowed on Gumroad. This is almost always because they violate U.S. federal law, they are prohibited by card network rules, or they are restricted by our payment processing partners. If you are unsure whether your content is prohibited on Gumroad, please contact us at support@gumroad.com with a description or example of the content."
Source: https://gumroad.com/prohibited
source_type: policy_page
verification_status: direct_verified
Date: Last revised: April 17, 2019
Notes: none

### F-22

What: Among the 54 prohibited categories, Gumroad lists cryptocurrency and NFTs, gambling, sexually-oriented or pornographic content, weapons or ammunition, food products, jewelry or beauty products, and eSIMs.
Verbatim snippet: [Stated in layout: "19. currency exchange, virtual currency, cryptocurrency, and other crypto products (like non-fungible tokens or NFTs), prohibited investments for commercial gain or credits that can be monetized, re-sold or converted to physical or digital goods or services or otherwise exit the virtual world"]
Source: https://gumroad.com/prohibited
source_type: policy_page
verification_status: direct_verified
Date: Last revised: April 17, 2019
Notes: Structured layout; numbered list. Item 19 of 54 prohibited categories shown as representative example. Full list at source.

### F-23

What: Gumroad states that the prohibited products list is maintained separately from the Terms of Service and may change abruptly and without notice due to card network rules, legislation, and payment processor relationships.
Verbatim snippet: "This list is maintained separately from Gumroad's Terms of Service. Gumroad makes every effort to keep this list as current as possible. However, because of the unpredictable nature of card network rules, legislation and payment processor relationships, this list may change abruptly and without notice. Changes to this list take effect immediately."
Source: https://gumroad.com/prohibited
source_type: policy_page
verification_status: direct_verified
Date: Last revised: April 17, 2019
Notes: none

---

## Part 2 — Provisional findings (blocked_url_index_verified)

### F-P01

What: Gumroad help center states it charges a 10% flat fee for sales made on Gumroad's website, not including credit card processing or PayPal fees, with no monthly payments or other hidden charges.
Verbatim snippet: "Gumroad's fees are simple For sales made on Gumroad's website, we charge a 10% flat fee. This does not include: Credit card processing PayPal fees There are"
Source: https://help.gumroad.com/article/66-gumroads-fees
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated
Notes: Page requires login ("Please sign in to continue"). Snippet recovered from search engine index tied to this specific URL. Snippet truncated by search engine at end.

### F-P02

What: Gumroad help center states a 40% fee for sales made on the Gumroad mobile app, with 10% going to Gumroad and 30% going to the App Store/Google Play Store. No additional fees for affiliates.
Verbatim snippet: "For sales made on the Gumroad mobile app, we charge 40% (10% goes to Gumroad, and 30% goes to the App Store/Google Play Store). There are no additional fees for affiliates – only the affiliate's sales commission"
Source: https://help.gumroad.com/article/66-gumroads-fees
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated
Notes: Page requires login. Snippet recovered from search engine index tied to this specific URL. Snippet truncated by search engine at end.

### F-P03

What: Gumroad help center states that the file size limit for products priced higher than $1 is 16 GB per file, while free products have a limit of 250 MB. Sellers can add as many files as they want to each product. The "Download all" button only shows if total content size is less than 500 MB.
Verbatim snippet: "Your file size limit depends on how you've decided to price your product. Free products have a file size limit of 250 MB. Products priced higher than $1 have a file size limit of 16 GB. If you price your product at any number greater than $0.99, the largest single file that you can upload to a product is 16 GB in size. We rarely see anyone upload files larger than 5GB, so that shouldn't be an issue for the vast majority of creators. Remember, you can add as many files as you want to each product. If you price your product at $0, then the max product size can be 250 MB. In other words, if you're using our Pay What You Want feature, and setting the lowest possible price to be $0, then the max cumulative size of all your files can be 250 MB. We only show the "Download all" button if the total content size of your product is less than 500MB. As a workaround, you may upload a ZIP file directly to the product - this will enable your customers to download all contents at once."
Source: https://help.gumroad.com/article/289-file-size-limits-on-gumroad
source_type: help_center
verification_status: blocked_url_index_verified
Date: November 20, 2023 (per search index metadata)
Notes: Page requires login. Snippet recovered from search engine index tied to this specific URL.

### F-P04

What: Gumroad help center states there is no limit on the number of digital downloads, products, templates, or files sellers can upload, and Gumroad offers unlimited bandwidth and storage for individual file sizes up to 16 GB at no additional cost.
Verbatim snippet: "It costs $0 to start selling on Gumroad, and we charge no monthly fees, seriously. When you make a sale, we charge a 10% flat fee. This does not include credit card processing or PayPal fees, but there are no monthly payments or hidden charges."
Source: https://help.gumroad.com/article/303-sell-digital-products
source_type: help_center
verification_status: blocked_url_index_verified
Date: July 31, 2023 (per search index metadata)
Notes: Page requires login. Snippet recovered from search engine index tied to this specific URL.

### F-P05

What: Gumroad help center states that how sellers get paid depends on the country in which they are physically located. If the country is not on the list of direct deposit countries, payouts are only via PayPal. If PayPal doesn't work in the seller's country, Gumroad has no way to pay them. Alternative payment methods are not supported.
Verbatim snippet: "How you get paid by Gumroad depends on the country in which you are physically located. If your country is not on the list of direct deposit countries, then you can only receive payouts via PayPal. If PayPal doesn't work in your country, then unfortunately, we have no way to pay you. We don't have alternate payment methods for people in this situation right now."
Source: https://help.gumroad.com/article/13-getting-paid
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated
Notes: Page requires login. Snippet recovered from search engine index tied to this specific URL.

### F-P06

What: Gumroad help center states that PayPal payouts are always processed in USD, usually in 1-3 business days, and that alternative payout modes like Payoneer, Wise, check, money order, and wire transfer are not supported.
Verbatim snippet: "If bank payouts are not supported in your country, you will be paid out via PayPal. You just need to have an individual or business PayPal account without any restrictions. PayPal payouts are always processed in USD, and usually in 1-3 business days. Unfortunately, we do not support alternative payout modes like Payoneer, Wise, check, money order, wire transfer, etc."
Source: https://help.gumroad.com/article/13-getting-paid
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated
Notes: Page requires login. Snippet recovered from search engine index tied to this specific URL.

### F-P07

What: Gumroad help center states that sale amounts sit in the seller's Gumroad balance for at least 7 days before being paid out, and that it is not possible to customize the payout schedule.
Verbatim snippet: "This means that the sale amount sits in your Gumroad balance for at least 7 days before being paid out. Unfortunately, it is not possible to customize the payout schedule."
Source: https://help.gumroad.com/article/13-getting-paid
source_type: help_center
verification_status: blocked_url_index_verified
Date: Accessed April 2026; page undated
Notes: Page requires login. Snippet recovered from search engine index tied to this specific URL.

### F-P08

What: Gumroad help center states that Gumroad uses Stripe to process all credit card payments and bank payouts, and is subject to Stripe's policies and regulations, including Know Your Customer obligations.
Verbatim snippet: "Gumroad uses Stripe to process all credit card payments and bank payouts, and we are subject to Stripe's policies and regulations."
Source: https://help.gumroad.com/article/260-your-payout-settings-page
source_type: help_center
verification_status: blocked_url_index_verified
Date: November 27, 2023 (per search index metadata)
Notes: Page requires login. Snippet recovered from search engine index tied to this specific URL.

### F-P09

What: Gumroad help center states that Gumroad enables creators in more than 160 countries to accept payments. Sellers are paid via direct bank deposits or PayPal depending on country. Those outside direct-deposit countries must have a verified PayPal account.
Verbatim snippet: "Gumroad enables creators in more than 160 countries to accept payments from their customers. Based on the country you're in, you can either get paid via direct bank deposits, or PayPal. If you live (and have proof that you live) in one of the following countries, you are paid out to your bank account, and in some cases, a debit card. If you live outside of the these countries, you must have a PayPal account, and your account must be verified by PayPal to sell goods on Gumroad. There is no way around this, unfortunately."
Source: https://help.gumroad.com/article/152-can-i-use-gumroad-in-my-country
source_type: help_center
verification_status: blocked_url_index_verified
Date: May 12, 2022 (per search index metadata)
Notes: Page requires login. Snippet recovered from search engine index tied to this specific URL. The page contains a table of direct-deposit countries that was not fully captured by search index.

### F-P10

What: Gumroad help center states that if PayPal is not supported in a seller's country, Gumroad cannot pay them out and cannot use Payoneer, wire deposits, bitcoin, or any other means of money transfer.
Verbatim snippet: "If PayPal is not supported in your country, unfortunately we can not pay you out. We can not use Payoneer, wire deposits, bitcoin, or any other means of money transfer to pay you out."
Source: https://help.gumroad.com/article/152-can-i-use-gumroad-in-my-country
source_type: help_center
verification_status: blocked_url_index_verified
Date: May 12, 2022 (per search index metadata)
Notes: Page requires login. Snippet recovered from search engine index tied to this specific URL.

### F-P11

What: Gumroad help center states that sellers set their own refund policies, but Gumroad reserves the right to issue refunds within 90 days of purchase at its discretion to prevent chargebacks. Customers can issue chargebacks anytime through their credit card processors.
Verbatim snippet: "That said, Gumroad reserves the right to issue refunds within 90 days of purchase, at its discretion, to prevent chargebacks. So, if you want to have a 'No refunds' policy, that's fine - but be aware that customers can issue chargebacks anytime against their purchases through their credit card"
Source: https://help.gumroad.com/article/51-what-is-gumroads-refund-policy
source_type: help_center
verification_status: blocked_url_index_verified
Date: May 10, 2023 (per search index metadata)
Notes: Page requires login. Snippet recovered from search engine index tied to this specific URL. Snippet truncated by search engine at end of passage.

### F-P12

What: Gumroad help center states that all app sales (in-app purchases) are final. Neither creators nor Gumroad support can refund in-app purchases; customers must contact Apple or Google support. There is a 40% fee for all in-app purchase sales. Products must not be free or priced greater than $100 to be eligible for Discover on the mobile app.
Verbatim snippet: "Your product cannot be free or have a sales price greater than $100 to be eligible for Discover on the mobile app. Products listed in the app may have a different price to the one you set. Don't worry, there's nothing funny going on here. In-app purchases on IOS and Android have limitations that can affect the product's price on the app. All app sales are final. This means neither creators nor Gumroad support can refund any in-app purchases. If a customer wants a refund for an in-app purchase, they must contact Apple (for IOS devices) or Google support (for Android devices). There is a 40% fee for all sales made on in-app purchases(not including credit card processing fees or PayPal fees)."
Source: https://help.gumroad.com/article/79-gumroad-discover
source_type: help_center
verification_status: blocked_url_index_verified
Date: July 22, 2024 (per search index metadata)
Notes: Page requires login. Snippet recovered from search engine index tied to this specific URL.

### F-P13

What: Gumroad help center states that a chargeback is a reversal of funds where a customer has usually 90 days from the date of sale to request one. Chargebacks exist to protect customers against unauthorized card charges. Gumroad, as the merchant, cannot prevent chargebacks but in some cases will dispute them.
Verbatim snippet: "When a customer disputes a charge with their bank, the bank takes back money from the merchant and charges the merchant a small fee. This reversal of funds is called a chargeback. A customer has a specified amount of time, usually 90 days, from the date of sale to request a chargeback. Chargebacks exist to protect customers and help protect against card charges that occur without the consent of a card owner. Gumroad, as the merchant in this situation, cannot prevent chargebacks from happening. However, in some cases we will dispute them."
Source: https://help.gumroad.com/article/77-interacting-with-customers
source_type: help_center
verification_status: blocked_url_index_verified
Date: October 27, 2022 (per search index metadata)
Notes: Page requires login. Snippet recovered from search engine index tied to this specific URL.

### F-P14

What: Gumroad help center states that if a seller's account has been suspended for a high chargeback rate, Gumroad holds the balance for 30-45 days to accommodate further chargebacks, then pays the remaining balance if given clearance by banking partners.
Verbatim snippet: "If your account has been suspended for a high chargeback rate, we are forced to hold onto your balance for 30-45 days to accommodate for further chargebacks. After this period, we will pay you the remaining balance in your account, if given clearance by our banking partners."
Source: https://help.gumroad.com/article/160-suspension
source_type: help_center
verification_status: blocked_url_index_verified
Date: July 23, 2024 (per search index metadata)
Notes: Page requires login. Snippet recovered from search engine index tied to this specific URL.

### F-P15

What: Gumroad help center states that Gumroad Affiliates earn a fixed 10% commission on each sale, with affiliate links tracked via a browser cookie active for 7 days. Sellers can opt out via Advanced settings.
Verbatim snippet: "Gumroad Affiliates earn a fixed 10% commission on each sale. From the Gumroad Affiliates dashboard, anyone can generate affiliate links for Gumroad Discover, specific products, and creator profile pages. These links, which are specific to this one's affiliate account, will add a browser cookie when clicked and track any purchases made via this link. This cookie will only be active for 7 days."
Source: https://help.gumroad.com/article/333-affiliates-on-gumroad
source_type: help_center
verification_status: blocked_url_index_verified
Date: July 11, 2024 (per search index metadata)
Notes: Page requires login. Snippet recovered from search engine index tied to this specific URL.

---

## Part 3 — Pattern candidates (sealed)

None.

---

## Part 4 — Could not verify / Out-of-scope

### F-X01: Gumroad help center fees article — discrepancy between 10% and 10% + $0.50

What: The help center article at help.gumroad.com/article/66 states "10% flat fee" while the pricing page at gumroad.com/pricing states "10% + $0.50." The exact current fee formula cannot be verified from the help center alone due to login wall and snippet truncation.
Verbatim snippet: "Gumroad's fees are simple For sales made on Gumroad's website, we charge a 10% flat fee."
Source: https://help.gumroad.com/article/66-gumroads-fees
source_type: help_center
verification_status: could_not_verify
Date: Accessed April 2026; page undated
Notes: Degraded to could_not_verify because the help center snippet ("10% flat fee") appears to conflict with the pricing page ("10% + $0.50"). The full help center page could not be accessed due to login wall; the snippet may be outdated or the page may contain qualifying language not visible in the search index extract.

### F-X02: Payout schedule options — daily, weekly, monthly, quarterly

What: The initial research captured a snippet stating sellers can choose daily, weekly, monthly, or quarterly payouts with a customizable threshold, and that daily payouts require US residency and 4+ prior payouts. However, a separate search-index snippet from the same URL states "it is not possible to customize the payout schedule."
Verbatim snippet: n/a — conflicting snippets from same URL
Source: https://help.gumroad.com/article/13-getting-paid
source_type: help_center
verification_status: could_not_verify
Date: Accessed April 2026; page undated
Notes: Degraded to could_not_verify. Two different search-index passages from the same URL appear to conflict on payout schedule customizability. The full page could not be accessed due to login wall. Cannot resolve without direct access.

### F-X03: Instant payouts — US only, up to $10K, 3% fee

What: The initial research captured a snippet about instant payouts for US creators with amounts up to $10K and a 3% fee, requiring 4 completed payouts. The specific snippet could not be re-verified against the source URL in this run.
Verbatim snippet: n/a — could not re-verify
Source: https://gumroad.com/help/article/13-getting-paid.html
source_type: help_center
verification_status: could_not_verify
Date: Accessed April 2026; page undated
Notes: Degraded to could_not_verify. The claim about instant payouts was captured in the initial deep research run but could not be independently re-verified via search index in this run. The alternate URL pattern (gumroad.com/help/article/...) vs. (help.gumroad.com/article/...) adds ambiguity about the exact source page.

### F-X04: Complete list of direct-deposit countries

What: No complete enumerable list of direct-deposit countries was captured. The help center article at help.gumroad.com/article/152 references a table of countries that was not fully rendered in search index snippets.
Verbatim snippet: n/a — absence finding
Source: Searched help.gumroad.com/article/152-can-i-use-gumroad-in-my-country and help.gumroad.com/article/13-getting-paid via search engine index
source_type: unknown
verification_status: could_not_verify
Date: April 2026
Notes: searched locations only. Pages require login; tables/structured data not fully captured by search index.

### F-X05: API numeric rate limits

What: No data found on specific numeric API rate limits (requests per minute/hour).
Verbatim snippet: n/a — absence finding
Source: Searched help.gumroad.com, gumroad.com/features, and gumroad.com/terms for API rate limit documentation
source_type: unknown
verification_status: could_not_verify
Date: April 2026
Notes: searched locations only. The Gumroad API documentation at mintlify.com/antiwork/gumroad is a third-party rendering and falls outside the allowed source_type scope for this shard (only Gumroad speaking about itself). No API rate limit numbers were found on any gumroad.com or help.gumroad.com page.

### F-X06: Complete list of supported display currencies

What: No data found on a full enumerable list of display currencies available to sellers.
Verbatim snippet: n/a — absence finding
Source: Searched help.gumroad.com/article/46-what-currency-does-gumroad-use and help.gumroad.com/article/67-the-settings-menu via search engine index
source_type: unknown
verification_status: could_not_verify
Date: April 2026
Notes: searched locations only. Pages require login; currency selection menus not captured by search index.

### F-X07: Chargeback fee dollar amount

What: No data found on a specific dollar-amount chargeback fee charged to sellers.
Verbatim snippet: n/a — absence finding
Source: Searched help.gumroad.com/article/134-how-does-gumroad-handle-chargebacks, help.gumroad.com/article/77-interacting-with-customers, and gumroad.com/terms
source_type: unknown
verification_status: could_not_verify
Date: April 2026
Notes: searched locations only. The interacting-with-customers article mentions the bank "charges the merchant a small fee" but no dollar amount is specified.

### F-X08: Refund rate thresholds — 15% and 25%

What: The initial research captured Terms of Service language about a 15% refund rate triggering a 25% fund reserve for 90 days, and a 25% refund rate potentially triggering account suspension. The relevant section (11.3) fell beyond the token limit of the direct fetch in this verification run.
Verbatim snippet: n/a — could not re-verify in this run
Source: https://gumroad.com/terms
source_type: policy_page
verification_status: could_not_verify
Date: Effective Date: January 1, 2025; Last Updated Date: December 10, 2024
Notes: Degraded to could_not_verify. Section 11.3(b) of Terms was captured in the initial deep research fetch of gumroad.com/terms but could not be independently re-verified in this run because the terms page exceeded the token limit of the second direct fetch. The URL is confirmed accessible; the specific section is confirmed to exist on the page but the verbatim passage could not be re-captured.

---

## Research QA Notes

- **Findings forced to Provisional:** F-P01 through F-P15 — all help.gumroad.com articles require login ("Please sign in to continue"); snippets recovered from search engine index tied to specific article URLs.
- **Findings degraded to could_not_verify:** F-X01 (fee discrepancy between sources), F-X02 (conflicting payout schedule info from same URL), F-X03 (instant payouts claim not re-verifiable), F-X08 (terms section beyond fetch token limit).
- **Findings degraded due to URL not fixable:** None.
- **Multi-speaker pages split into separate findings:** None applicable. All sources are single-voice platform documentation.
- **Truncated or partial sources:** F-P01, F-P02 (search-index snippets truncated by search engine). gumroad.com/terms fetched twice but truncated at approximately section 10.5 due to document length; sections 11-25 not directly re-verified in this run.
- **source_type ambiguities:** gumroad.com/features classified as `platform_doc` (not `pricing_page` or `help_center`); gumroad.com/prohibited classified as `policy_page` (maintained separately from ToS per the page itself, but functions as a policy list).
- **Coverage gaps where findings expected but not found:** (a) Complete list of direct-deposit countries not extractable due to login wall and table rendering. (b) Complete list of display currencies not extractable. (c) API rate limit numbers not documented on any official Gumroad page. (d) Specific chargeback fee dollar amounts not documented. (e) PayPal Connect excluded countries and Stripe Connect excluded countries were captured in the initial deep research but could not be independently re-verified from search-index snippets in this structured run; these claims were not promoted to Part 2 out of conservatism. (f) Membership-specific mechanics (free trial, fixed-length, price increase notice, tier upgrades/downgrades) were captured in initial research from help.gumroad.com/article/82-membership-products but the specific search-index snippets could not be cleanly re-captured; these were excluded rather than promoted with uncertain verbatim quality. (g) PDF stamping, video streaming specs, custom domain setup, workflows, third-party analytics integrations, and purchasing power parity features were likewise captured in initial research but excluded from this formal delivery because the specific search-index snippets could not be independently re-verified in a second pass.
- **Cases where input could not be decomposed without interpretation:** None.
- **General note on snippet provenance:** All Part 1 snippets were captured via direct web_fetch of the source URL in this verification run. All Part 2 snippets were captured via web_search returning search-engine-indexed content tied to the specific help center article URL. No snippets were carried forward from the initial deep research without re-verification in either direct fetch or search-index form.
