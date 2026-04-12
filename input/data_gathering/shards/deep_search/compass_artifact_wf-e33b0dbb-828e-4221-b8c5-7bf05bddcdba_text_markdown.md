# Payhip platform fees, payments, and payouts — first-party documentation

**Payhip operates a three-tier pricing model where all plans share identical features, differentiated solely by the transaction fee Payhip charges on each sale: 5% (Free), 2% (Plus, $29/mo), or 0% (Pro, $99/mo).** Payment processor fees from Stripe, PayPal, or any of the other 11 supported gateways are always additional and collected by those processors, not by Payhip. Payouts flow directly to sellers' connected processor accounts — Payhip itself never holds funds, cannot issue refunds, and does not impose minimum payout thresholds for standard sellers. All findings below come exclusively from payhip.com and help.payhip.com.

---

## Plan tiers and Payhip's own transaction fees

### Finding 1 — Pricing cards (three tiers)
- **URL:** https://payhip.com/pricing
- **Accessibility:** Directly accessible
- **Page date:** Undated (footer © 2026)
- **Layout:** Structured pricing cards

**Verbatim text:**

> **Free Forever** — $0 /mo — +5% transaction fee — All features — Unlimited products — Unlimited revenue

> **Plus** — $29 /mo — +2% transaction fee — All features — Unlimited products — Unlimited revenue

> **Pro** — $99 /mo — No transaction fee — All features — Unlimited products — Unlimited revenue

### Finding 2 — Billing and upgrading help article (expanded fee explanation)
- **URL:** https://help.payhip.com/article/102-billing-and-upgrading
- **Accessibility:** Directly accessible
- **Page date:** Last updated June 20, 2021
- **Layout:** Prose

**Verbatim text:**

> "By default, you'll be on Payhip's Free Forever plan. At $0 per month, this comes with all features, unlimited products, and unlimited revenue, but you will be charged a 5% fee by us on any transactions processed through your Payhip site. This is great for if you're just getting started, but once the sales start rolling in you'll want to upgrade to reduce your transaction fee."

> "For $29 a month you can upgrade to the Plus plan and we'll reduce the transaction fee to 2%. Or, for just $99 per month, you can be on our Pro plan and there will be no transaction fee from us at all."

> "Please note, PayPal and Stripe will still charge their transaction fees."

> "To upgrade your Payhip account, go to "Account" > "Settings" and then click on the "Billing & Invoices" tab. Then all you need to do is choose the plan that you'd like to upgrade to, enter your credit card details, and that's it."

### Finding 3 — No feature gating across tiers
- **URL:** https://payhip.com/pricing (FAQ section)
- **Accessibility:** Directly accessible
- **Page date:** Undated
- **Layout:** Structured FAQ accordion block

**Verbatim text:**

> "At Payhip, our goal is to make pricing as simple and transparent as possible. So, no feature-gating here! You'll get access to all of our amazing features to help you grow your business, even on our free plan."

### Finding 4 — No gateway connection fee
- **URL:** https://payhip.com/features/payments (FAQ section)
- **Accessibility:** Directly accessible
- **Page date:** Undated (footer © 2026)
- **Layout:** Structured FAQ accordion block

**Verbatim text:**

> "Payhip does not charge any fees to connect a payment gateway, so you'll only pay the transaction fees set by your chosen provider."

> "Yes. Payhip allows you to connect multiple digital goods payment processors at the same time (no extra fees), so you can offer customers more ways to pay at checkout and increase your chances of completing a sale."

### Finding 5 — Charity discounts available
- **URL:** https://payhip.com/pricing (FAQ section)
- **Accessibility:** Directly accessible
- **Page date:** Undated
- **Layout:** Structured FAQ accordion block

**Verbatim text:**

> "For sure, we love to support great causes of all kinds so please get in touch with us and we'll help setup a discount for your account."

---

## How sellers get paid — payout flow and timing

### Finding 6 — Instant payouts (general statement)
- **URL:** https://payhip.com/pricing (FAQ section)
- **Accessibility:** Directly accessible
- **Page date:** Undated
- **Layout:** Structured FAQ accordion block

**Verbatim text:**

> "We will deposit your sales to you immediately after a transaction has been completed. Not quite the speed of light, but close."

### Finding 7 — Detailed payment flow (PayPal and Stripe)
- **URL:** https://help.payhip.com/article/173-how-do-i-get-paid
- **Accessibility:** Directly accessible
- **Page date:** Last updated April 19, 2024
- **Layout:** Prose with subheadings

**Verbatim text (receiving payments):**

> "When a customer buys from your Payhip store, the payment is instantly transferred to your PayPal or Stripe account (minus PayPal/Stripe's fees as well as Payhip's fees, which we'll go into below)."

> "The transfer to PayPal/Stripe is instant - you'll get paid after every transaction as it happens."

> "If you have both PayPal and Stripe linked, then PayPal payments will be processed through PayPal and credit/debit card payments will be processed through Stripe."

**Verbatim text (withdrawing from Stripe):**

> "Stripe payments will stay as 'pending' for a few days. The length of this pending period depends on your location (see here)."

> "Once that period has passed, payouts will be sent to your connected bank account on a daily basis by default. In your Stripe dashboard, you're able to change this to weekly, monthly, or manual."

**Verbatim text (withdrawing from PayPal):**

> "Please note that, by default, PayPal withdrawals need to be manually initiated. To enable automatic payouts, you'll want to switch on auto transfers (available for Premier/Business accounts only)."

**Verbatim text (holding funds):**

> "Can you hold onto the money for me? You may be wondering whether Payhip can hold off on sending you the money for each transaction in order to minimize Stripe/PayPal fees. Sadly that isn't possible at this point in time."

### Finding 8 — Alternative billing model for non-Stripe/PayPal gateways
- **URLs:** Identical language across all of these help articles: https://help.payhip.com/article/342-connecting-your-square-account, https://help.payhip.com/article/341-connecting-your-mollie-account, https://help.payhip.com/article/344-connecting-your-paystack-account, https://help.payhip.com/article/367-connect-your-flutterwave-account, https://help.payhip.com/article/343-connecting-your-mercado-pago-account, https://help.payhip.com/article/366-connect-your-xendit-account, https://help.payhip.com/article/365-connect-your-midtrans-account, https://help.payhip.com/article/370-connect-your-payu-account, https://help.payhip.com/article/368-connect-your-razorpay-account, https://help.payhip.com/article/371-connect-your-iyzico-account, https://help.payhip.com/article/372-connect-your-paytabs-account
- **Accessibility:** All directly accessible
- **Page dates:** Range from December 17, 2025 to February 22, 2026
- **Layout:** Structured prose + FAQ

**Verbatim text (identical across all 11 gateway articles):**

> "[Gateway name] payments are processed instantly, so you receive funds immediately after each transaction. [Gateway name] payments work a little differently compared to Stripe or PayPal on Payhip. You will get your full payment (without Payhip fees deducted) instantly after each transaction has been processed. At the end of each month, you'll be billed for your Payhip fees using your preferred credit card."

This establishes **two distinct billing models**: for Stripe and PayPal, Payhip deducts its fee from each transaction before depositing the remainder to the seller. For all other 11 gateways, the seller receives the full payment (minus only the gateway's own fees) instantly, and Payhip bills the seller's credit card for accumulated platform fees at month-end.

### Finding 9 — Missing payment or payout troubleshooting
- **URL:** https://help.payhip.com/article/374-missing-payment-or-payout
- **Accessibility:** Directly accessible
- **Page date:** Last updated March 17, 2026
- **Layout:** Structured numbered sections + prose

**Verbatim text:**

> "When a sale is made on Payhip, the payment is processed and sent directly to your connected payment processor at the time of purchase."

> "Payment processors will occasionally hold a transaction and mark it as pending, on hold, or processing, which means the funds won't be available until the payment works its way through. You can check the status in your payment processor account. If it's been pending for more than 48 hours, you'll need to reach out to them directly to get further clarification."

> "Sometimes you may expect the full sale amount to be credited to your account, but keep in mind that platform and payment processor fees may apply. Because of this, the net amount you receive may be lower than expected."

> "Payments are always routed to whichever account was connected at the exact moment a purchase was made."

---

## Payment processor fees (collected by each gateway, not Payhip)

### Finding 10 — PayPal and Stripe fees (general)
- **URL:** https://help.payhip.com/article/173-how-do-i-get-paid
- **Accessibility:** Directly accessible
- **Page date:** Last updated April 19, 2024
- **Layout:** Prose

**Verbatim text:**

> "PayPal's fees are roughly around 2.9% + $0.30 per transaction, but vary for international transactions."

> "Stripe's fees are also 2.9% + $0.30, but depend on which country you're from."

### Finding 11 — PayPal fees (detailed)
- **URL:** https://help.payhip.com/article/64-connecting-your-paypal-account
- **Accessibility:** Directly accessible
- **Page date:** Undated
- **Layout:** Structured prose + FAQ

**Verbatim text:**

> "The standard credit and debit card payment fee is 2.99% + a fixed fee per transaction, which varies according to the transaction currency. An additional 1.5% applies to international commercial transactions. Note that these fees are collected by PayPal and do not go to Payhip."

### Finding 12 — Stripe fees (detailed)
- **URL:** https://help.payhip.com/article/65-connecting-your-stripe-account
- **Accessibility:** Directly accessible
- **Page date:** Last updated February 25, 2026
- **Layout:** Structured prose + FAQ

**Verbatim text:**

> "The standard Stripe fee is 2.9% + $0.30 per transaction. Fees may vary by country. For full details, please visit Stripe's pricing page. Note that these fees are collected by Stripe and do not go to Payhip."

### Finding 13 — Square fees
- **URL:** https://help.payhip.com/article/342-connecting-your-square-account
- **Accessibility:** Directly accessible
- **Page date:** Undated (from search results)
- **Layout:** Structured prose

**Verbatim text:**

> "The standard Square fee for online credit card transactions is 2.8% + $0.30 per transaction. Please check Square's pricing page for the latest updates. There are no chargeback fees. Note that these fees are collected by Square and do not go to Payhip."

### Finding 14 — Mollie fees
- **URL:** https://help.payhip.com/article/341-connecting-your-mollie-account
- **Accessibility:** Directly accessible
- **Page date:** Last updated February 22, 2026
- **Layout:** Structured prose + bulleted lists

**Verbatim text:**

> "The standard Mollie fee for online credit card transactions ranges from 1.80% + €0.25 to 2.90% + €0.25 per transaction for European Economic Area consumer credit cards from Mastercard and Visa. Rates vary by payment methods, please check Mollie's pricing page for the latest updates. Note that these fees are collected by Mollie and do not go to Payhip."

### Finding 15 — Paystack fees
- **URL:** https://help.payhip.com/article/344-connecting-your-paystack-account
- **Accessibility:** Directly accessible
- **Page date:** Undated (from search results)
- **Layout:** Structured prose

**Verbatim text:**

> "The standard Paystack fee for local transactions is 1.5% + NGN 100 per transaction and 3.9% + NGN 100 for international transactions. Please check Paystack's pricing page for the latest updates. Note that these fees are collected by Paystack and do not go to Payhip."

### Finding 16 — Mercado Pago fees
- **URL:** https://help.payhip.com/article/343-connecting-your-mercado-pago-account
- **Accessibility:** Directly accessible
- **Page date:** Last updated December 31, 2025
- **Layout:** Structured prose

**Verbatim text:**

> "The standard Mercado Pago fee starts from 3.99% per transaction. Note that these fees are collected by Mercado Pago and do not go to Payhip."

### Finding 17 — Flutterwave fees
- **URL:** https://help.payhip.com/article/367-connect-your-flutterwave-account
- **Accessibility:** Directly accessible
- **Page date:** Undated (from search results)
- **Layout:** Structured prose

**Verbatim text:**

> "Flutterwave's standard fee for online credit card transactions ranges from 2.6% - 4.8% per transaction depending on your country/region and where your customer is paying from. Fees vary by payment methods, please check Flutterwave's pricing page for the latest updates. Note that these fees are collected by Flutterwave and do not go to Payhip."

### Finding 18 — Xendit fees
- **URL:** https://help.payhip.com/article/366-connect-your-xendit-account
- **Accessibility:** Directly accessible
- **Page date:** Last updated December 17, 2025
- **Layout:** Structured prose

**Verbatim text:**

> "Xendit's standard fee for online credit card transactions is 3% + $0.30 per transaction. Note that these fees are collected by Xendit and do not go to Payhip."

### Finding 19 — Midtrans fees
- **URL:** https://help.payhip.com/article/365-connect-your-midtrans-account
- **Accessibility:** Directly accessible
- **Page date:** Last updated December 31, 2025
- **Layout:** Structured prose

**Verbatim text:**

> "Midtrans' standard fee for online credit card transactions is 2,9% + IDR 2,000 per transaction, and the standard fee for bank transfer is IDR 4,000 per transaction. Note that these fees are collected by Midtrans and do not go to Payhip."

### Finding 20 — PayU fees
- **URL:** https://help.payhip.com/article/370-connect-your-payu-account
- **Accessibility:** Directly accessible
- **Page date:** Last updated December 17, 2025
- **Layout:** Structured prose

**Verbatim text:**

> "The standard PayU fee for online transactions ranges from 2% per transaction depending on your country/region and where your customer is paying from. Note that these fees are collected by PayU and do not go to Payhip."

### Finding 21 — Razorpay fees
- **URL:** https://help.payhip.com/article/368-connect-your-razorpay-account
- **Accessibility:** Directly accessible
- **Page date:** Last updated December 31, 2025
- **Layout:** Structured prose

**Verbatim text:**

> "Razorpay's standard fee for online transactions ranges from 2% per transaction depending on your country/region and where your customer is paying from. Note that these fees are collected by Razorpay and do not go to Payhip."

### Finding 22 — Iyzico fees
- **URL:** https://help.payhip.com/article/371-connect-your-iyzico-account
- **Accessibility:** Directly accessible
- **Page date:** Last updated December 31, 2025
- **Layout:** Structured prose

**Verbatim text:**

> "The standard Iyzico fee for online transactions ranges from 4.29% + 0.25 TRY per transaction depending on your country/region and where your customer is paying from. Note that these fees are collected by Iyzico and do not go to Payhip."

### Finding 23 — PayTabs fees
- **URL:** https://help.payhip.com/article/372-connect-your-paytabs-account
- **Accessibility:** Directly accessible
- **Page date:** Last updated February 21, 2026
- **Layout:** Structured prose

**Verbatim text:**

> "The standard PayTabs fee for online transactions starts from 2.25% per transaction. Fees vary by payment methods, and there might be a monthly or setup fee depending on your region. Note that these fees are collected by PayTabs and do not go to Payhip."

---

## Payment gateway availability by country and region

### Finding 24 — Stripe countries
- **URL:** https://help.payhip.com/article/65-connecting-your-stripe-account
- **Accessibility:** Directly accessible
- **Page date:** Last updated February 25, 2026
- **Layout:** Structured prose

**Verbatim text:**

> "Stripe is currently supported in over 40 countries including Austria, Australia, Belgium, Brazil, Bulgaria, Canada, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Germany, Gibraltar, Greece, Hong Kong, Hungary, Ireland, Italy, Japan, Latvia, Liechtenstein, Lithuania, Luxembourg, Malaysia, Malta, Mexico, Netherlands, New Zealand, Norway, Poland, Portugal, Romania, Singapore, Slovenia, Slovakia, Spain, Sweden, Switzerland, Thailand, United Arab Emirates, United Kingdom and United States."

### Finding 25 — PayPal countries
- **URL:** https://help.payhip.com/article/64-connecting-your-paypal-account
- **Accessibility:** Directly accessible
- **Page date:** Undated
- **Layout:** Structured prose

**Verbatim text:**

> "PayPal is currently supported in over 200 countries including Australia, Austria, Belgium, Brazil, Canada, Cyprus, Czech Republic, Estonia, Finland, France, Germany, Greece, Hungary, Ireland, Italy, Latvia, Luxemburg, Malta, Mexico, Netherlands, New Zealand, Poland, Portugal, Romania, San Marino, Slovakia, Slovenia, South Africa, Spain, United Kingdom, and United States."

> "If you're based in the countries listed above, you can connect either a personal or business PayPal account to your Payhip store. For all other countries on PayPal's supported list, you must have a business PayPal account."

### Finding 26 — Square countries
- **URL:** https://help.payhip.com/article/342-connecting-your-square-account
- **Accessibility:** Directly accessible
- **Page date:** Undated
- **Layout:** Structured prose

**Verbatim text:**

> "Square is available in Australia, Canada, France, Ireland, Japan, Spain, United Kingdom, and the United States."

### Finding 27 — Mollie countries
- **URL:** https://help.payhip.com/article/341-connecting-your-mollie-account
- **Accessibility:** Directly accessible
- **Page date:** Last updated February 22, 2026
- **Layout:** Structured prose

**Verbatim text:**

> "Mollie is currently supported in over 20 countries including Austria, Belgium, Czech Republic, Denmark, Finland, France, Germany, Greece, Hungary, Ireland, Italy, Luxembourg, The Netherlands, Norway, Poland, Portugal, Romania, Slovenia, Spain, Sweden, Switzerland, and United Kingdom."

### Finding 28 — Paystack countries
- **URL:** https://help.payhip.com/article/344-connecting-your-paystack-account
- **Accessibility:** Directly accessible
- **Page date:** Undated
- **Layout:** Structured prose

**Verbatim text:**

> "Paystack is supported in Côte d'Ivoire (Ivory Coast), Ghana, Kenya, Nigeria, and South Africa."

### Finding 29 — Flutterwave countries
- **URL:** https://help.payhip.com/article/367-connect-your-flutterwave-account
- **Accessibility:** Directly accessible
- **Page date:** Undated
- **Layout:** Structured prose

**Verbatim text:**

> "Flutterwave is available in Nigeria, Ghana, Kenya, South Africa, Uganda, Rwanda, Zambia, Tanzania, and Cameroon."

### Finding 30 — Mercado Pago countries and currencies
- **URL:** https://help.payhip.com/article/343-connecting-your-mercado-pago-account
- **Accessibility:** Directly accessible
- **Page date:** Last updated December 31, 2025
- **Layout:** Structured prose

**Verbatim text:**

> "Mercado Pago is available in Argentina, Brazil, Chile, Colombia, Mexico, Peru and Uruguay."

> "Supported currencies include ARS, BRL, CLP, COP, MXN, PEN, and UYU."

### Finding 31 — Xendit countries
- **URL:** https://help.payhip.com/article/366-connect-your-xendit-account
- **Accessibility:** Directly accessible
- **Page date:** Last updated December 17, 2025
- **Layout:** Structured prose

**Verbatim text:**

> "Xendit supports payment processing in Indonesia, Malaysia, Philippines, Thailand, and Vietnam."

### Finding 32 — Midtrans (Indonesia only)
- **URL:** https://help.payhip.com/article/365-connect-your-midtrans-account
- **Accessibility:** Directly accessible
- **Page date:** Last updated December 31, 2025
- **Layout:** Structured prose

**Verbatim text:**

> "Midtrans is available in Indonesia and is currently only able to process transactions in Indonesian Rupiah (IDR)."

> "the default currency that you set on your Payhip account must match the currency on your Midtrans account. In this case, it would need to be IDR (Indonesian Rupiah)."

### Finding 33 — PayU (India only)
- **URL:** https://help.payhip.com/article/370-connect-your-payu-account
- **Accessibility:** Directly accessible
- **Page date:** Last updated December 17, 2025
- **Layout:** Structured prose

**Verbatim text:**

> "PayU supports payment processing for sellers in India."

### Finding 34 — Razorpay (India, accepting from 180+ countries)
- **URL:** https://help.payhip.com/article/368-connect-your-razorpay-account
- **Accessibility:** Directly accessible
- **Page date:** Last updated December 31, 2025
- **Layout:** Structured prose

**Verbatim text:**

> "Razorpay supports payment processing for sellers in India. Sellers in India can accept payments from over 180 countries around the world through Razorpay."

### Finding 35 — Iyzico (Turkey only)
- **URL:** https://help.payhip.com/article/371-connect-your-iyzico-account
- **Accessibility:** Directly accessible
- **Page date:** Last updated December 31, 2025
- **Layout:** Structured prose

**Verbatim text:**

> "Iyzico supports payment processing for sellers in Turkey."

### Finding 36 — PayTabs (MENA region)
- **URL:** https://help.payhip.com/article/372-connect-your-paytabs-account
- **Accessibility:** Directly accessible
- **Page date:** Last updated February 21, 2026
- **Layout:** Structured prose

**Verbatim text:**

> "PayTabs supports countries in the Middle East and North Africa (MENA) region, including Egypt, Iraq, Jordan, Kuwait, Oman, Saudi Arabia, and United Arab Emirates."

---

## Currency handling

### Finding 37 — Currency matching requirement (universal across non-Stripe/PayPal gateways)
- **URLs:** Found identically in all of: https://help.payhip.com/article/342-connecting-your-square-account, https://help.payhip.com/article/341-connecting-your-mollie-account, https://help.payhip.com/article/344-connecting-your-paystack-account, https://help.payhip.com/article/367-connect-your-flutterwave-account, https://help.payhip.com/article/343-connecting-your-mercado-pago-account, https://help.payhip.com/article/366-connect-your-xendit-account, https://help.payhip.com/article/365-connect-your-midtrans-account, https://help.payhip.com/article/370-connect-your-payu-account, https://help.payhip.com/article/368-connect-your-razorpay-account, https://help.payhip.com/article/371-connect-your-iyzico-account, https://help.payhip.com/article/372-connect-your-paytabs-account
- **Accessibility:** All directly accessible
- **Layout:** Structured prose

**Verbatim text (identical across all gateway articles):**

> "Note that the currency used in your Payhip account must match the currency in your [gateway name] account."

---

## Payment methods accepted

### Finding 38 — Overall payment methods overview
- **URL:** https://payhip.com/features/payments (FAQ section)
- **Accessibility:** Directly accessible
- **Page date:** Undated (footer © 2026)
- **Layout:** Structured FAQ accordion block

**Verbatim text:**

> "You can accept all major debit and credit cards, PayPal, mobile wallets like Apple Pay and Google Pay, and local payment methods (e.g. iDEAL, Pix, UPI, etc) through Payhip's supported digital goods payment gateways. You can connect with multiple gateways to give customers more ways to pay at checkout. Keep in mind that payment methods vary by location and provider."

### Finding 39 — Card brands listed on pricing page
- **URL:** https://payhip.com/pricing (FAQ section)
- **Accessibility:** Directly accessible
- **Page date:** Undated
- **Layout:** Structured FAQ accordion block

**Verbatim text:**

> "Customers can pay with their PayPal account or their card. Visa, MasterCard, American Express, JCB, Discover, and Diners Club and more."

### Finding 40 — Multiple gateway connection rules
- **URL:** https://payhip.com/features/payments (FAQ section)
- **Accessibility:** Directly accessible
- **Page date:** Undated
- **Layout:** Structured FAQ accordion block

**Verbatim text:**

> "In most cases, you are able to connect PayPal plus one other payment processor for card and other applicable payment types."

### Finding 41 — Stripe-specific payment methods
- **URL:** https://help.payhip.com/article/65-connecting-your-stripe-account
- **Accessibility:** Directly accessible
- **Page date:** Last updated February 25, 2026
- **Layout:** Structured bulleted lists

**Verbatim text:**

> "Stripe supports all major debit and credit cards, including Visa, Mastercard, American Express, and more. This also includes a wide range of local and alternative payment methods, such as:
> * Digital wallets: Apple Pay, Google Pay, Link, Samsung Pay, Cash App Pay, Alipay, WeChat Pay
> * Bank redirects / transfers: iDEAL, Bancontact, EPS, Przelewy24, BLIK, FPX, Pay by Bank, Multibanco, MB WAY, OXXO, Konbini
> * Real-time payments: Pix, Swish, PayNow, PromptPay, PayTo
> * Mobile payments: TWINT, Kakao Pay, Naver Pay, PAYCO, MobilePay, Satispay, Revolut Pay
> * Buy Now, Pay Later: Afterpay / Clearpay, Klarna, Affirm, Alma, Zip, Billie"

---

## Refund policies

### Finding 42 — Fees not refunded upon refund
- **URL:** https://help.payhip.com/article/173-how-do-i-get-paid (FAQ section)
- **Accessibility:** Directly accessible
- **Page date:** Last updated April 19, 2024
- **Layout:** Structured FAQ block

**Verbatim text:**

> "If I refund a payment, do the fees get refunded? Both Payhip fees and PayPal/Stripe fees will not be returned when you refund a transaction."

### Finding 43 — Seller-managed refunds, Payhip does not hold funds
- **URL:** https://help.payhip.com/article/281-refund-request
- **Accessibility:** Directly accessible
- **Page date:** Last updated March 17, 2026
- **Layout:** Structured FAQ blocks + prose

**Verbatim text:**

> "Payhip does not hold funds and cannot issue refunds directly."

> "Each seller sets and manages their own refund policy. Some sellers may offer refunds, while others may not, especially if the product has already been downloaded or accessed."

> "If you would like to request a refund for a product you purchased from a Payhip seller, you'll need to contact the seller directly."

> "Many sellers on Payhip are individual creators or small businesses, so response times may vary. Most sellers typically reply within 24 to 72 hours."

### Finding 44 — Refund process for sellers
- **URL:** https://help.payhip.com/article/147-how-do-i-refund-a-transaction
- **Accessibility:** Directly accessible
- **Page date:** Last updated April 10, 2024
- **Layout:** Prose with instructional steps

**Verbatim text:**

> "In order to refund a customer, you'll want to log into your PayPal/Stripe account and find the user's details/transaction."

> "Please be aware that your refunds in PayPal/Stripe will also be reflected in Payhip. Since the refunded amount is taken into consideration in all places, the numbers shown on your monthly sales report and analytics will reflect that."

### Finding 45 — Chargebacks
- **URL:** https://help.payhip.com/article/287-protect-yourself-against-chargebacks
- **Accessibility:** Directly accessible
- **Page date:** Last updated April 10, 2024
- **Layout:** Structured prose

**Verbatim text:**

> "On occasion, a customer may file a chargeback for their purchase. This means that they are claiming that you did not provide them with the promised product or service and want their money back."

> "If customers have agreed to your refund policy and terms of service before they make their purchase and they then put through a chargeback, you should be protected. You can let the company who is handling the chargeback know that the customer was made aware of your terms."

### Finding 46 — PayPal disputes (30-day window)
- **URL:** https://help.payhip.com/article/159-paypal-disputes
- **Accessibility:** Directly accessible
- **Page date:** Last updated July 30, 2021
- **Layout:** Prose + instructional steps

**Verbatim text:**

> "As a seller using PayPal, there is a possibility that a client might not be happy with your product/service and that they could dispute the payment. Whilst this is not common, PayPal does provide you and the customer with a system called the Resolution Center to assist both parties."

> "Please be aware that you will only have 30 days to dispute the claim before PayPal will automatically refund the buyer."

---

## VAT and tax handling

### Finding 47 — EU/UK digital VAT (reseller model)
- **URL:** https://help.payhip.com/article/127-digital-eu-vat
- **Accessibility:** Directly accessible
- **Page date:** Last updated February 21, 2026
- **Layout:** Structured prose with worked numerical examples

**Verbatim text:**

> "On the 1st Jan 2015, the European Union introduced the digital EU VAT law. This law requires all sales of digital items (such as ebooks) in the EU to pay VAT based on the location of the customer."

> "In order to remove all of the administrative burden from our sellers we will take care of all EU VAT issues for your customers based in the European Union."

> "The UK has left the EU but they have a similar law that also requires VAT be charged on digital products if your customer is based in the UK - regardless of where the seller is from."

> "By default, we automatically handle digital UK & EU VAT for you. If you'd rather handle the process yourself you can uncheck the first two checkboxes."

> "Choosing to include taxes within the product price means your customers won't see a difference in the price they need to pay. However it means your profits will be impacted to account for sales tax - instead of being passed on to customers."

> "If your customer is not based in the EU or UK, then this digital tax will not be applied to their transaction. They will be charged at the regular price you set for the product."

### Finding 48 — VAT calculation examples
- **URL:** https://help.payhip.com/article/127-digital-eu-vat
- **Accessibility:** Directly accessible
- **Page date:** Last updated February 21, 2026
- **Layout:** Structured numerical examples

**Verbatim text (VAT on top of price, $10 product, France 20% VAT, Free plan 5% Payhip fee):**

> "Your customer will be charged: $10 + (0.20 × $10) = $12"

> "We will charge 5% and will collect the EU VAT amount: (0.05 × $10) + (0.20 × $10) = $2.50"

> "You will receive the remaining amount: $12 – $2.50 = $9.50 (Note: PayPal will deduct it's fees as well)"

**Verbatim text (VAT included in price, same scenario):**

> "Your customer will be charged: $10"

> "Price before VAT applied: $10 ÷ 1.20 = $8.33"

> "We will charge 5% and will collect the EU VAT amount: (0.05 × $8.33) + ($10 – $8.33) = $2.09"

> "You will receive the remaining amount: $10 – $2.09 = $7.91 (Note: PayPal will deduct its fees as well)"

### Finding 49 — Reseller model for EU/UK VAT
- **URL:** https://payhip.com/features/vat-taxes
- **Accessibility:** Directly accessible
- **Page date:** Undated (footer © 2026)
- **Layout:** Marketing page with headings and bullet points

**Verbatim text:**

> "Dealing with the digital EU & UK VAT laws are an administrative and legal nightmare. However, Payhip can take this burden off your shoulders and take on full responsibility for complying with these laws. If your customer is buying a digital product in the EU/UK we act as your reseller which means we're 100% responsible for digital EU/UK VAT."

> "We detect if a customer is based in the EU or UK"

> "Apply the correct VAT amount to their transaction based on the tax rate of their country"

> "Each quarter we report and submit any VAT amounts collected to the relevant tax authorities"

### Finding 50 — Non-EU/UK taxes (seller-configured)
- **URL:** https://help.payhip.com/article/174-taxes-for-digital-products
- **Accessibility:** Directly accessible (via search results)
- **Page date:** Undated (from search results)
- **Layout:** Prose with instructions

**Verbatim text:**

> "Payhip handles digital EU VAT for you, but what about taxes for countries outside of the EU? Whilst we don't remit this tax on your behalf, we do make it easy to collect that tax on top of, or within, your product pricing. We also give you a monthly sales report that summarizes how much tax you've collected, making reporting a breeze!"

> "Payhip will automatically detect the customer's location at checkout and add any applicable taxes that you've set up."

> "By default, we'll charge tax on top of your pricing. If you'd like it to be included within your pricing, scroll down to Tax Settings and select the checkbox for 'Include taxes within product price'."

> "Here at Payhip we're not tax experts. Please always check with your accountant to understand exactly who/what you need to charge. If you don't want to deal with taxes for certain countries, you are also able to block customers in that location from purchasing from you."

### Finding 51 — Pricing page VAT statement
- **URL:** https://payhip.com/pricing (FAQ section)
- **Accessibility:** Directly accessible
- **Page date:** Undated
- **Layout:** Structured FAQ accordion block

**Verbatim text:**

> "Payhip is fully compliant to collect and remit EU VAT and UK on your behalf automatically. You can also set up any other taxes with Payhip and we report these to you."

---

## Partner program fees and payouts

### Finding 52 — Partner commission and payout details
- **URL:** https://help.payhip.com/article/227-becoming-a-partner
- **Accessibility:** Directly accessible (via search results)
- **Page date:** Undated
- **Layout:** Prose

**Verbatim text:**

> "you can earn a 50% recurring commission on Payhip's transaction fees and any monthly paid plans from the sellers you refer. That means if someone signs up through your link and has upgraded to a paid plan, you get a cut every month as long as the seller is active. You will also earn 50% of the amount we collect from their sales for transaction fees."

> "You get paid out on a monthly basis on the 13th of every month via Paypal. There is a minimum commission amount of $50 for payouts, and if you do not meet this threshold, your commission will be combined with the following months until you reach the minimum balance of $50."

---

## Affiliate payouts (seller-managed)

### Finding 53 — Affiliate payout handling
- **URL:** https://help.payhip.com/article/214-becoming-an-affiliate
- **Accessibility:** Directly accessible (via search results)
- **Page date:** Undated
- **Layout:** Prose

**Verbatim text:**

> "At this point in time, Payhip does not automatically process payouts for affiliates. The sellers handle the payments to affiliates themselves. We make this process easier for them though. We provide monthly affiliate sales reports that include the PayPal email of the affiliate and the commission they earned for each month."

---

## Sales reporting

### Finding 54 — Monthly sales report contents
- **URL:** https://help.payhip.com/article/219-sales-report
- **Accessibility:** Directly accessible
- **Page date:** Last updated September 27, 2022
- **Layout:** Bulleted list

**Verbatim text:**

> "EU and UK VAT - These are digital UK & EU VAT collected for that period"

> "Stripe/PayPal Fees - These are payment processor fees charged by PayPal and Stripe"

> "Payhip Fees - These are platform fees charged by Payhip depending on your plan"

> "Custom Taxes - These are taxes that were manually set up, collected, and sent to you"

> "Products Sold - This lists the products and the number of items sold for that period"

> "Affiliates Commission - This shows the amount earned by your affiliates"

> "Affiliate Sales - This shows the number of sales generated by your affiliates"

---

## Terms of service and legal

### Finding 55 — Terms of Use (payments section)
- **URL:** https://payhip.com/terms
- **Accessibility:** Directly accessible
- **Page date:** "Last updated: 19 February 2018"
- **Layout:** Prose, numbered sections

**Verbatim text (Section 3 — Payments):**

> "All payments will be made directly to you by the End User via Paypal or Stripe or any other payment gateway we choose to support."

> "You must have an active Paypal or Stripe account to use our service and you must abide by and adhere to their respective terms, conditions and policies (Paypal terms, Stripe terms) in order to use our site."

**Verbatim text (Section 2 — Licence, VAT):**

> "Once you have uploaded your file, you will set the sale price and decide whether the price includes or excludes VAT for EU customers."

**Verbatim text (Section 5 — VAT Obligations):**

> "We will comply with all applicable laws in performing our rights and obligations under these terms and conditions and we shall obtain, at our own cost, all clearances consents and provisions required in connection with distributing copies of Your Digital Content. This includes dealing with HMRC in respect of the place of supply rules for VAT supplies made within in the European Union."

### Finding 56 — Privacy policy (payment data and retention)
- **URL:** https://payhip.com/privacy
- **Accessibility:** Directly accessible
- **Page date:** Undated
- **Layout:** Prose with headings

**Verbatim text:**

> "Payment is handled separately, and securely, through the payment processor you have selected during checkout ('Payment Processor'). Your payment card details are never collected by Us."

> "We will hold details relating to any transaction you make, such as your name, e-mail address, IP address, billing address, location data for 10 years from the date of the transaction for EU VAT purposes in respect of digital products."

> "All information We hold about you is stored on secure servers in the EU."

### Finding 57 — Security statement
- **URL:** https://payhip.com/faq
- **Accessibility:** Directly accessible
- **Page date:** Undated (footer © 2026)
- **Layout:** Structured FAQ accordion block

**Verbatim text:**

> "Payhip is secure. We don't store card details - all payments are handled by Paypal and Stripe."

### Finding 58 — Company registration
- **URL:** https://payhip.com/terms
- **Accessibility:** Directly accessible
- **Page date:** Last updated 19 February 2018
- **Layout:** Prose

**Verbatim text:**

> "Payhip Limited is a company incorporated in England and Wales with registration no 08386910. We own and operate www.payhip.com. Our registered office is Payhip, 167-169 Great Portland Street, 5th Floor, W1W 5PF, London, United Kingdom."

**Verbatim text (governing law):**

> "These terms of use are governed by English law and we both agree to submit to the exclusive jurisdiction of the English courts in the event of any dispute."

---

## Consolidated reference tables

### Payhip plan tiers

| Plan | Monthly cost | Payhip transaction fee | Features | Products | Revenue cap |
|------|-------------|----------------------|----------|----------|-------------|
| Free Forever | $0 | 5% | All features | Unlimited | Unlimited |
| Plus | $29 | 2% | All features | Unlimited | Unlimited |
| Pro | $99 | 0% | All features | Unlimited | Unlimited |

### Payment processor fees (as stated by Payhip)

| Gateway | Standard fee | Currency/notes |
|---------|-------------|---------------|
| Stripe | 2.9% + $0.30 | Varies by country |
| PayPal | 2.99% + fixed fee | +1.5% for international; fixed fee varies by transaction currency |
| Square | 2.8% + $0.30 | No chargeback fees |
| Mollie | 1.80%–2.90% + €0.25 | EEA consumer Visa/Mastercard |
| Paystack | 1.5% + NGN 100 (local); 3.9% + NGN 100 (intl) | — |
| Mercado Pago | From 3.99% | — |
| Flutterwave | 2.6%–4.8% | Varies by country/region |
| Xendit | 3% + $0.30 | — |
| Midtrans | 2.9% + IDR 2,000 (cards); IDR 4,000 (bank transfer) | IDR only |
| PayU | From 2% | India |
| Razorpay | From 2% | India; accepts from 180+ countries |
| Iyzico | 4.29% + 0.25 TRY | Turkey |
| PayTabs | From 2.25% | Possible monthly/setup fee by region (MENA) |

### Billing model by gateway

| Billing model | Gateways | How it works |
|--------------|----------|-------------|
| Per-transaction deduction | Stripe, PayPal | Payhip deducts its fee from each transaction before depositing to seller |
| Monthly billing | Square, Mollie, Paystack, Flutterwave, Mercado Pago, Xendit, Midtrans, PayU, Razorpay, Iyzico, PayTabs | Seller receives full payment (minus gateway fee only); Payhip bills its fees to seller's credit card at month-end |

### Items explicitly not found

- **No minimum payout amount** is stated for standard seller payouts (only the $50 minimum for the Partner Program)
- **No annual billing discount** for Payhip's own paid plans is mentioned anywhere
- **No maximum or cap** on Payhip transaction fees is documented
- **No country-specific variations in Payhip's own fee percentages** — the 5%/2%/0% tiers apply universally regardless of seller or buyer location
- **No effective dates** are given for the current fee structure; the pricing page is undated
- **No webhook-specific fees** or API usage fees are mentioned