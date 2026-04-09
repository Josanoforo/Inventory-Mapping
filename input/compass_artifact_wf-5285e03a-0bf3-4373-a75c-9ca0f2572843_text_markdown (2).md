# Etsy Platform Fees — Data Gathering Research Pack

**Platform:** Etsy only | **Scope:** Directions 1 and 2 | **Language:** English | **Output:** Run-local only

---

## Part 1 — Clean findings (direct_verified only)

All findings below are from Direction 2 (third-party commentary) pages that were directly fetched and verified.

---

### Finding 1

- **What:** General Etsy seller fee burden estimated at 20–30%+ of sale price before materials, labor, or shipping
- **Verbatim snippet:** "Add it all up and the typical Etsy seller loses roughly 20–30%+ of their sale price to fees before accounting for materials, labor, or shipping costs."
- **Source:** https://blog.marmalead.com/etsy-fees-explained/
- **source_type:** blog
- **verification_status:** direct_verified
- **Date:** February 13, 2026
- **Signal type:** fee_burden_claim
- **Notes:** None.

---

### Finding 2

- **What:** Etsy transaction fee is 6.5% of total sale price including shipping; increased from 5% in April 2022
- **Verbatim snippet:** "The transaction fee is the big one. Etsy takes 6.5% of the total sale price, and that includes the shipping price the buyer pays. This is the detail that catches many sellers off guard."
- **Source:** https://blog.marmalead.com/etsy-fees-explained/
- **source_type:** blog
- **verification_status:** direct_verified
- **Date:** February 13, 2026
- **Signal type:** fee_claim
- **Notes:** None.

---

### Finding 3

- **What:** Etsy US payment processing fee is 3% + $0.25 per transaction; fixed component disproportionately impacts low-priced items
- **Verbatim snippet:** "Nearly all Etsy sellers are required to use Etsy Payments, the platform's built-in payment processing system. In the US, the payment processing fee is 3% + $0.25 per transaction. That fixed $0.25 component is important to understand. On a $50 sale, $0.25 represents 0.5% of the sale price. On a $10 sale, it represents 2.5%. This means lower-priced items carry a disproportionately higher effective fee rate."
- **Source:** https://blog.marmalead.com/etsy-fees-explained/
- **source_type:** blog
- **verification_status:** direct_verified
- **Date:** February 13, 2026
- **Signal type:** fee_claim
- **Notes:** US-specific rate cited; blog notes rates vary by country.

---

### Finding 4

- **What:** Etsy offsite ads fee is 15% (under $10K, optional) or 12% (at or above $10K, mandatory); 30-day attribution window
- **Verbatim snippet:** "If your shop earned $10,000 or more in the trailing 12-month period, two things change: your Offsite Ads rate drops to 12%, but you can no longer opt out of the program. It becomes mandatory."
- **Source:** https://blog.marmalead.com/etsy-fees-explained/
- **source_type:** blog
- **verification_status:** direct_verified
- **Date:** February 13, 2026
- **Signal type:** fee_claim
- **Notes:** None.

---

### Finding 5

- **What:** Etsy offsite ads 30-day attribution window applies even when ad played minimal role in sale
- **Verbatim snippet:** "The 30-day attribution window is particularly painful. A customer who found your shop through organic search, bookmarked it, then clicked an Etsy retargeting ad a week later will trigger the offsite ads fee — even though the ad played a minimal role in the sale."
- **Source:** https://blog.marmalead.com/etsy-fees-explained/
- **source_type:** blog
- **verification_status:** direct_verified
- **Date:** February 13, 2026
- **Signal type:** fee_claim
- **Notes:** None.

---

### Finding 6

- **What:** Etsy currency conversion fee is 2.5% when listing currency differs from payment account currency
- **Verbatim snippet:** "If you sell in a currency different from your payment currency, Etsy charges a 2.5% currency conversion fee."
- **Source:** https://blog.marmalead.com/etsy-fees-explained/
- **source_type:** blog
- **verification_status:** direct_verified
- **Date:** February 13, 2026
- **Signal type:** fee_claim
- **Notes:** None.

---

### Finding 7

- **What:** Worked example: $30 sale with 15% offsite ads yields $7.80 total fees (26% of sale price)
- **Verbatim snippet:** "Listing fee: $0.20 / Transaction fee (6.5%): $1.95 / Payment processing (3% + $0.25): $1.15 / Offsite Ads fee (15%): $4.50 / Total fees: $7.80—that's 26% of the sale price"
- **Source:** https://blog.marmalead.com/etsy-fees-explained/
- **source_type:** blog
- **verification_status:** direct_verified
- **Date:** February 13, 2026
- **Signal type:** worked_example
- **Notes:** Structured layout snippet; layout is slash-separated fee line items as published.

---

### Finding 8

- **What:** Etsy transaction fee increase from 5% to 6.5% in April 2022 described as 30% jump; prompted seller strike and petition
- **Verbatim snippet:** "The biggest single reason sellers feel Etsy fees are high is the April 2022 transaction fee increase — from 5% to 6.5%. That's a 30% jump in Etsy's primary fee, enacted despite significant seller pushback including a week-long seller strike and a petition signed by tens of thousands of Etsy sellers."
- **Source:** https://craftybase.com/blog/why-etsy-fees-are-so-high
- **source_type:** blog
- **verification_status:** direct_verified
- **Date:** Accessed April 2026; page undated (content updated for 2026)
- **Signal type:** fee_claim
- **Notes:** Page undated; content references "2026" in title.

---

### Finding 9

- **What:** Worked example: $45 item + $8 shipping (US), without offsite ads, total Etsy fees = $5.49 (10.4%)
- **Verbatim snippet:** "Listing fee: $0.20 / Transaction fee (6.5%): 6.5% × ($45 + $8) = $3.45 / Payment processing (3% + $0.25): 3% × $53 + $0.25 = $1.84 / Total fees: $5.49"
- **Source:** https://craftybase.com/blog/why-etsy-fees-are-so-high
- **source_type:** blog
- **verification_status:** direct_verified
- **Date:** Accessed April 2026; page undated
- **Signal type:** worked_example
- **Notes:** Structured layout snippet; slash-separated fee line items as published.

---

### Finding 10

- **What:** Worked example: same $45 + $8 sale with 15% offsite ads adds $6.75, total fees = $12.24 (23.1%)
- **Verbatim snippet:** "Offsite ads fee (15%): 15% × $45 = $6.75 / Total fees with offsite ads: $12.24"
- **Source:** https://craftybase.com/blog/why-etsy-fees-are-so-high
- **source_type:** blog
- **verification_status:** direct_verified
- **Date:** Accessed April 2026; page undated
- **Signal type:** worked_example
- **Notes:** Structured layout snippet; continues from worked example on same page (Finding 9).

---

### Finding 11

- **What:** Worked example: $100 item via Etsy Payments yields $9.95 total fees (~10% effective rate)
- **Verbatim snippet:** "For example, let's say you sell an item for $100, and the buyer pays using Etsy Payments. The transaction fee for this sale would be $6.50 (6.5% of the sale price), and the payment processing fee would be $3.25 (3% + $0.25). Taking also into account the listing fee of $0.20, this means that a total of $9.95 would be deducted from the sale price, leaving you with a deposit of $90.05 in your account. That's roughly a 10% effective fee rate — and it goes much higher if offsite ads are involved."
- **Source:** https://craftybase.com/blog/the-complete-guide-to-etsy-fees
- **source_type:** blog
- **verification_status:** direct_verified
- **Date:** Accessed April 2026; page undated (content updated for 2026)
- **Signal type:** worked_example
- **Notes:** Page undated.

---

### Finding 12

- **What:** Etsy Plus subscription is $10 USD; 15 listing credits appear as $3 credit; credits expire at end of billing cycle
- **Verbatim snippet:** "Currently, Etsy Plus is $10 USD. Depending on your location, you may also need to pay tax on this fee." and "15 listing credits (which will appear as $3 credit)... These credits expire at the end of the billing cycle and disappear from your payment account if not used."
- **Source:** https://craftybase.com/blog/the-complete-guide-to-etsy-fees
- **source_type:** blog
- **verification_status:** direct_verified
- **Date:** Accessed April 2026; page undated
- **Signal type:** fee_claim
- **Notes:** Page undated.

---

### Finding 13

- **What:** Etsy shop setup fee is $15 USD one-time fee for new shops, introduced to reduce bot shops and drop-shipping fraud
- **Verbatim snippet:** "To maintain the security of the marketplace, Etsy charges a one-time set-up fee of $15 USD (or your currency equivalent) before you can open your shop for business. Etsy introduced this to reduce bot shops and drop-shipping fraud."
- **Source:** https://www.growingyourcraft.com/blog/how-much-does-it-really-cost-to-sell-on-etsy
- **source_type:** blog
- **verification_status:** direct_verified
- **Date:** Last Updated: January 26, 2026
- **Signal type:** fee_claim
- **Notes:** None.

---

### Finding 14

- **What:** Etsy offsite ads fee is 12% for sellers over $10K (mandatory, cannot opt out) and 15% for the rest
- **Verbatim snippet:** "The offsite ads fee is 12% for sellers who made over $10,000 for the last 12 months, and 15% for the rest of the sellers. For sellers who made over $10,000 over the last 12 months, offsite ads is compulsory and cannot be opted out."
- **Source:** https://www.growingyourcraft.com/blog/how-much-does-it-really-cost-to-sell-on-etsy
- **source_type:** blog
- **verification_status:** direct_verified
- **Date:** Last Updated: January 26, 2026
- **Signal type:** fee_claim
- **Notes:** None.

---

### Finding 15

- **What:** Etsy Share and Save program reduces transaction fee by 4% (from 6.5% to 2.5%) on sales via seller's own shared link
- **Verbatim snippet:** "Etsy now rewards you for bringing your own traffic. If you share a unique trackable link (generated in your dashboard) on your social media, email list, or business cards, and a buyer purchases through that link, Etsy takes 4% off your transaction fee." and "This means instead of paying the standard 6.5% transaction fee, you only pay 2.5% on that sale."
- **Source:** https://www.growingyourcraft.com/blog/how-much-does-it-really-cost-to-sell-on-etsy
- **source_type:** blog
- **verification_status:** direct_verified
- **Date:** Last Updated: January 26, 2026
- **Signal type:** fee_claim
- **Notes:** None.

---

### Finding 16

- **What:** Etsy general fee burden estimated at 10% to 15% of final sale price for most transactions
- **Verbatim snippet:** "In general, you can expect Etsy to take roughly 10% to 15% of your final sale price for most transactions."
- **Source:** https://www.growingyourcraft.com/blog/how-much-does-it-really-cost-to-sell-on-etsy
- **source_type:** blog
- **verification_status:** direct_verified
- **Date:** Last Updated: January 26, 2026
- **Signal type:** fee_burden_claim
- **Notes:** None.

---

### Finding 17

- **What:** Etsy transaction fee described as 6.5%, increased from 5% in April 2022, characterized as "shockingly high"
- **Verbatim snippet:** "You will likely see the bulk of your Etsy seller fees comprised of the transaction fee. Etsy's transaction fee costs your business 6.5 percent of the final sale price of an item. It's also worth noting that Etsy increased its transaction fee from 5 percent to 6.5 percent on April 11th, 2022. This transaction fee is shockingly high compared to average credit card processing fees seen across other payment processors."
- **Source:** https://paymentcloudinc.com/blog/etsy-seller-fees/
- **source_type:** blog
- **verification_status:** direct_verified
- **Date:** Updated: Mar. 24, 2026
- **Signal type:** fee_claim
- **Notes:** None.

---

### Finding 18

- **What:** Etsy transaction fee increase from 5% to 6.5% announced February 2022, effective April 2022
- **Verbatim snippet:** "Etsy's latest fee increase was announced in February, raising the amount sellers pay for each transaction from 5 percent of their sales to 6.5 percent, effective Monday."
- **Source:** https://www.pbs.org/newshour/economy/why-etsys-latest-fee-increase-has-inspired-thousands-of-sellers-including-its-most-marginalized-to-strike
- **source_type:** article
- **verification_status:** direct_verified
- **Date:** Apr 19, 2022
- **Signal type:** fee_increase_report
- **Notes:** None.

---

### Finding 19

- **What:** Sellers report Etsy fees can add up to as much as 20 percent of revenue
- **Verbatim snippet:** "In addition to transaction fees, sellers could be responsible for a host of other charges, such as listing fees, processing fees and advertising fees, which can all add up to as much as 20 percent of their revenue, sellers said."
- **Source:** https://www.pbs.org/newshour/economy/why-etsys-latest-fee-increase-has-inspired-thousands-of-sellers-including-its-most-marginalized-to-strike
- **source_type:** article
- **verification_status:** direct_verified
- **Date:** Apr 19, 2022
- **Signal type:** fee_burden_claim
- **Notes:** None.

---

### Finding 20 (Speaker: Sydney Sky Griffin, seller)

- **What:** Seller complaint about fee confusion — difficulty understanding and untangling multiple Etsy fees
- **Verbatim snippet:** "\"It's very confusing, because there's so many fees,\" said Sydney Sky Griffin, 25, a strike participant who has run an Etsy shop selling skincare products for the past year. \"It would take me so long to try to understand and untangle where the money was going and how much they were charging and why they were charging it.\""
- **Source:** https://www.pbs.org/newshour/economy/why-etsys-latest-fee-increase-has-inspired-thousands-of-sellers-including-its-most-marginalized-to-strike
- **source_type:** article
- **verification_status:** direct_verified
- **Date:** Apr 19, 2022
- **Signal type:** seller_complaint
- **Notes:** Individual seller quoted within news article; split per Rule 2.

---

### Finding 21 (Speaker: Brontë Grimm, seller)

- **What:** Worked example: $50 necklace sale after fees and costs yielded $15.45 profit, equivalent to $3.86/hour
- **Verbatim snippet:** "This month, Grimm sold a necklace for $50 just as the new transaction fee was being implemented. After taking out fees plus the cost of materials and production, they made $15.45 in profits, working out to an hourly pay of $3.86 for their labor."
- **Source:** https://www.pbs.org/newshour/economy/why-etsys-latest-fee-increase-has-inspired-thousands-of-sellers-including-its-most-marginalized-to-strike
- **source_type:** article
- **verification_status:** direct_verified
- **Date:** Apr 19, 2022
- **Signal type:** worked_example
- **Notes:** Individual seller quoted within news article; split per Rule 2. Profit figure includes both fees and material/production costs, not fees alone.

---

### Finding 22

- **What:** Etsy CEO announced transaction fee increase from 5% to 6.5% effective April 11, 2022
- **Verbatim snippet:** "Earlier this year, Etsy's CEO Josh Silverman announced that starting April 11 the company would increase the 5% transaction fee for sellers to 6.5%."
- **Source:** https://www.npr.org/2022/04/11/1091123928/etsy-strike-2022
- **source_type:** article
- **verification_status:** direct_verified
- **Date:** April 11, 2022
- **Signal type:** fee_increase_report
- **Notes:** None.

---

### Finding 23 (Speaker: Etsy strikers' collective letter)

- **What:** Seller complaint: Etsy described as "hostile place for authentic small businesses" bringing sellers "to the brink of financial ruin"
- **Verbatim snippet:** "In a letter sent to Silverman on Monday, Etsy strikers said: \"Etsy has become a downright hostile place for authentic small businesses to operate. For both full-time and part-time sellers alike, the changes on Etsy have brought many of us to the brink of financial ruin.\""
- **Source:** https://www.npr.org/2022/04/11/1091123928/etsy-strike-2022
- **source_type:** article
- **verification_status:** direct_verified
- **Date:** April 11, 2022
- **Signal type:** seller_complaint
- **Notes:** Collective voice (strikers' letter) quoted in article; split per Rule 2.

---

### Finding 24

- **What:** Etsy survey suggests possible monthly subscription tiers from free (5 items, $0.40/listing) to $50/month (unlimited, $0.20 only if sold)
- **Verbatim snippet:** "The survey suggests Etsy is considering charging a monthly fee (likely optional) in addition to listing fees, and give sellers access to various features depending on which 'tier' they subscribe to." and "The survey offered various scenarios for sellers to consider, from a free monthly plan limiting sellers to listing 5 items/month at 40 cents/listing all the way to a $50 plan offering unlimited listings that comes with a 20-cent listing fee that is paid only if an item sells."
- **Source:** https://www.ecommercebytes.com/2024/02/25/monthly-fees-may-be-coming-to-etsy/
- **source_type:** article
- **verification_status:** direct_verified
- **Date:** February 25, 2024
- **Signal type:** fee_speculation
- **Notes:** Reports on seller survey, not confirmed policy.

---

### Finding 25 (Speaker: unnamed seller on EcommerceBytes)

- **What:** Seller complaint linking potential new fees to activist investor pressure to raise site income
- **Verbatim snippet:** "A seller discussing Etsy's survey about possible new subscription fees wrote, \"The Elliott Management person came on board to raise site income by a lot, and to raise it fast. How do you think that'll happen if not through fees? It sure as hell won't happen through sales!\""
- **Source:** https://www.ecommercebytes.com/2024/02/25/monthly-fees-may-be-coming-to-etsy/
- **source_type:** article
- **verification_status:** direct_verified
- **Date:** February 25, 2024
- **Signal type:** seller_complaint
- **Notes:** Seller quoted within article; split per Rule 2.

---

### Finding 26 (Speaker: joebcrafts, Sellers Ask Sellers forum)

- **What:** Seller complaint about recurring fee additions including $15 new seller setup fee; characterizes fee increases as growth facade
- **Verbatim snippet:** "I find it frustrating that Etsy, in order to keep showing increases (growth), they come up with a new seller fee for the quarter they need to have the boost. I did not know that they recently started charging $15 to new sellers. It will never end because they constantly need something new to keep up the growth facade. P.S. Silverman is a schmuck."
- **Source:** https://sellersasksellers.com/t/has-etsy-lost-its-way/4104
- **source_type:** seller_forum
- **verification_status:** direct_verified
- **Date:** May 24, 2024
- **Signal type:** seller_complaint
- **Notes:** None.

---

### Finding 27 (Speaker: ModernSwitch, Sellers Ask Sellers forum)

- **What:** Seller commentary on $15 setup fee being negligible relative to listing fee costs for large-catalog shops
- **Verbatim snippet:** "I think the $15 is just such a weird flex point. With there being a .20 cent listing fee to list an item, any store that already plans on listing 500 items (for example AI POD, or whatever), is already planning on spending $100, what is another $15?"
- **Source:** https://sellersasksellers.com/t/has-etsy-lost-its-way/4104
- **source_type:** seller_forum
- **verification_status:** direct_verified
- **Date:** May 24, 2024
- **Signal type:** fee_claim
- **Notes:** None.

---

### Finding 28 (Speaker: Jan Manley, Craft Industry Alliance comments)

- **What:** Seller complaint that offsite ads 30-day attribution unfairly charges 12–15% on repeat customer purchases
- **Verbatim snippet:** "But now I feel it is just unfair. Because of the type of product that I have designed, I have a lot repeat customers. They are REPEAT customers on a monthly, sometimes twice monthly basis! If one of those customers just happens to click on one of the Etsy ads, then all of the purchases for the next 30 days will have the ad fee. That is unfair – I have worked really hard to build my customer base over the last 6 years and for Etsy to gain 12 or 15% from my hard work is just wrong. I am really disappointed in this move by Etsy."
- **Source:** https://craftindustryalliance.org/why-im-mostly-on-board-for-etsys-new-offsite-ads-program/
- **source_type:** blog
- **verification_status:** direct_verified
- **Date:** March 2, 2020
- **Signal type:** seller_complaint
- **Notes:** Individual commenter on blog post; source_type classified as blog per page structure (see QA Notes for ambiguity note).

---

### Finding 29 (Speaker: Deb Grogan, Craft Industry Alliance comments)

- **What:** Seller complaint about offsite ads fee stacking on top of transaction and processing fees, including on shipping costs
- **Verbatim snippet:** "My issue is that they are also charging that fee on TOP of transaction fees for shipping, so we are in fact going to be paying 17% on the shipping costs as well. I understand and really do not have an issue with the 12% on the product but adding it to the shipping is greedy and BS in my opinion…….They already get a piece of the shipping cost (we know they have negotiated a better rate and we get a lesser one), they get a piece of the credit card fees, hell I don't even pay 3% for those on my website, and they charge their transaction fee on it ALL, even the taxes paid (thats BS too)…….These are (for the most part) tangibles we need to pay. But this ad fee on top of the shipping? Thats just crap……."
- **Source:** https://craftindustryalliance.org/why-im-mostly-on-board-for-etsys-new-offsite-ads-program/
- **source_type:** blog
- **verification_status:** direct_verified
- **Date:** March 3, 2020
- **Signal type:** seller_complaint
- **Notes:** Individual commenter on blog post; references pre-April 2022 transaction fee rate (5% at time of writing). The "17%" figure is the commenter's own calculation combining offsite ads + transaction fee on shipping.

---

### Finding 30 (Speaker: Lori, Craft Industry Alliance comments)

- **What:** Seller complaint that $10,000 mandatory offsite ads threshold is arbitrary and doesn't account for item price
- **Verbatim snippet:** "$10,000 is a really arbitrary number- it's not taking into account average cost of items. 10k for a sticker seller is a really successful shop. 10k in a year for someone who's average item price is over a hundred isn't necessarily the same. I make over 20k a year on Etsy, and I'm not a hobbyist. This has been my full time job for 16 years, and Etsy isn't my only platform (I also do in-person shows). I absolutely do not want to grow any more on Etsy, especially with the new ODR system. It should be opt-in for everyone. Period."
- **Source:** https://craftindustryalliance.org/why-im-mostly-on-board-for-etsys-new-offsite-ads-program/
- **source_type:** blog
- **verification_status:** direct_verified
- **Date:** March 4, 2020
- **Signal type:** seller_complaint
- **Notes:** Individual commenter on blog post.

---

### Finding 31 (Speaker: Carrol Thornby, Craft Industry Alliance comments)

- **What:** Seller complaint about mandatory 12% offsite ads after exceeding $10,000; describes it as permanently forced
- **Verbatim snippet:** "When I first realized that my sales had gone over the $10,000 mark in a 12 month period, I was thrilled. I am a small-time seller who got carried away with listing and selling items that put me over the limit of $10,000. which then put me into the never-ending and FORCED requirement by Etsy that I will now be required to pay 12% more in fees on items that sell on an advertised site. What I don't like is the FORCED aspect of this and that it is forever, I have no choice. Most of my items are priced as low as possible, with me making a small amount, and this added 12% will put me in a losing position."
- **Source:** https://craftindustryalliance.org/why-im-mostly-on-board-for-etsys-new-offsite-ads-program/
- **source_type:** blog
- **verification_status:** direct_verified
- **Date:** July 13, 2021
- **Signal type:** seller_complaint
- **Notes:** Individual commenter on blog post.

---

### Finding 32 (Speaker: Ruth Mierzwa, Craft Industry Alliance comments)

- **What:** Seller near $10K threshold considering leaving Etsy; prefers giving 15% to customers as discount rather than as offsite ads fee
- **Verbatim snippet:** "I have opted out. Aside from a few exceptions, my products are all under $10 with most in the $4-8 range. I have never advertised either on Etsy or eBay. After opting out I had my best week ever with nothing coming from left over clicks from ads. While the fees were being waived, the majority of the sales were coming from my most popular items. Our customers are the ones that lose out with this program. I would have to raise my prices to cover the cost. I also could no longer afford to run a sale. I would rather five my customers 15% off rather than give it to Etsy. I feel that I pay them a fair amount of fees as it is and I expect them to advertise the site. If sellers want to opt in then it should be optional not mandatory. Since I am about $700 away from the $10K mark I am already looking at going elsewhere."
- **Source:** https://craftindustryalliance.org/why-im-mostly-on-board-for-etsys-new-offsite-ads-program/
- **source_type:** blog
- **verification_status:** direct_verified
- **Date:** May 11, 2020
- **Signal type:** seller_complaint
- **Notes:** Individual commenter on blog post.

---

### Finding 33 (Speaker: Alecse, Craft Industry Alliance comments)

- **What:** Seller who opted out of offsite ads; calculates 15% offsite ads + 5% commission as ~20% combined fee
- **Verbatim snippet:** "I just opted out Etsy Off site ads as I consider that a 15% + 5% commission is quite prohibitive but it is not the sole reason. Unlike many companies who started their business on Etsy and eventually created their own brand website, we started on Shopify and just lately started listing our products on Etsy. Hence we have been long time advertising on Google, Facebook, Instagram, Pinterest, etc. and I think that Etsy off site adds would directly compete with our other advertising programs, bringing the CPC higher to end up paying more commissions on sales which could have been made on our Website without having to give away nearly 20% of the income. And I think that if I had more than 10 000 USD of sales per year making the program mandatory, I would definitely leave Etsy."
- **Source:** https://craftindustryalliance.org/why-im-mostly-on-board-for-etsys-new-offsite-ads-program/
- **source_type:** blog
- **verification_status:** direct_verified
- **Date:** June 13, 2020
- **Signal type:** seller_complaint
- **Notes:** Individual commenter on blog post. References pre-April 2022 transaction fee rate (5% at time of writing).

---

### Finding 34 (Speaker: Lacey, Craft Industry Alliance comments)

- **What:** Seller complaint predicting Etsy fees will reach consignment-shop levels (40%+) based on annual fee increases since 2009
- **Verbatim snippet:** "Etsy has increased one fee or another every year that I've been on Etsy since 2009. At this rate by 2024 we will be paying consignment shop prices (40%) or more to sell on their site."
- **Source:** https://craftindustryalliance.org/why-im-mostly-on-board-for-etsys-new-offsite-ads-program/
- **source_type:** blog
- **verification_status:** direct_verified
- **Date:** May 2, 2020
- **Signal type:** seller_complaint
- **Notes:** Individual commenter on blog post.

---

### Finding 35 (Speaker: Lisa Smallridge, Craft Industry Alliance comments)

- **What:** Australian seller closed Etsy account citing compulsory changes, fee increases, and fees charged on shipping
- **Verbatim snippet:** "Unfortunately, after many years of \"compulsory\" changes and fee increases (including having to pay fees on a shipping charge of $25 AUD from Australia to the US\"), this was the last straw. I've closed my Etsy account today."
- **Source:** https://craftindustryalliance.org/why-im-mostly-on-board-for-etsys-new-offsite-ads-program/
- **source_type:** blog
- **verification_status:** direct_verified
- **Date:** March 4, 2020
- **Signal type:** seller_complaint
- **Notes:** Individual commenter on blog post.

---

## Part 2 — Provisional findings (blocked_url_index_verified only)

All Direction 1 findings below were extracted from Google search index content. Every official Etsy URL returned HTTP 403 on direct fetch. Blocked Direction 2 findings are also included here.

---

### Finding 36

- **What:** Etsy listing fee is $0.20 USD per listing; charged on creation or renewal; listings expire after four months; auto-renews at $0.20 per quantity sold
- **Verbatim snippet:** "You will be charged a listing fee of $0.20 USD for each item that you list for sale on Etsy.com or Etsy's mobile apps. ... You will be charged a listing fee whether or not the listed item sells, unless you create a private listing, in which case you will only be charged the listing fee when the private listing is sold. Etsy.com listings expire after four months. ... If you list multiple quantities of the same item, the initial listing fee will be $0.20, and the listing will be automatically renewed at $0.20 after each of the items sells."
- **Source:** https://www.etsy.com/legal/fees/
- **source_type:** policy_page
- **verification_status:** blocked_url_index_verified
- **Date:** Accessed April 2026; page undated
- **Signal type:** platform_fee_policy
- **Notes:** Direct fetch returned HTTP 403; verbatim extracted from Google search index content. Ellipses mark omissions within same paragraph for brevity.

---

### Finding 37

- **What:** Etsy transaction fee is 6.5% of displayed listing price plus shipping and gift wrapping charges
- **Verbatim snippet:** "When you make a sale through Etsy.com, you will be charged a transaction fee of 6.5% of the price you display for each listing plus the amount you charge for shipping and gift wrapping."
- **Source:** https://www.etsy.com/legal/fees/
- **source_type:** policy_page
- **verification_status:** blocked_url_index_verified
- **Date:** Accessed April 2026; page undated
- **Signal type:** platform_fee_policy
- **Notes:** Direct fetch returned HTTP 403; verbatim from Google search index.

---

### Finding 38

- **What:** Etsy transaction fee excludes sales tax for US sellers unless tax is included in listing price; applies to listing price inclusive of taxes for non-US sellers
- **Verbatim snippet:** "If you sell from the US, the transaction fee will not apply to sales tax. If you sell from anywhere other than the US, the transaction fee will apply to the listing price (which should include any applicable taxes that you as a seller are responsible for), shipping price, and gift wrapping fee."
- **Source:** https://www.etsy.com/legal/fees/
- **source_type:** policy_page
- **verification_status:** blocked_url_index_verified
- **Date:** Accessed April 2026; page undated
- **Signal type:** platform_fee_policy
- **Notes:** Direct fetch returned HTTP 403; verbatim from Google search index. Snippet from current indexed version references US only (earlier cached version also referenced Canada).

---

### Finding 39

- **What:** Etsy payment processing fees vary by bank account location; assessed on total sale including tax and shipping
- **Verbatim snippet:** "Payment processing fees are charged for each transaction made through Etsy Payments. Payment processing fees vary based on the location of your bank account. In certain markets, a fixed deposit fee may be charged for the disbursement of seller funds that are under certain designated thresholds."
- **Source:** https://www.etsy.com/legal/fees/
- **source_type:** policy_page
- **verification_status:** blocked_url_index_verified
- **Date:** Accessed April 2026; page undated
- **Signal type:** platform_fee_policy
- **Notes:** Direct fetch returned HTTP 403; verbatim from Google search index. No specific country rates given on this page; page directs to Etsy Payments Policy for rate table.

---

### Finding 40

- **What:** Etsy Plus subscription fee is $10 USD per month; includes 15 listing credits ($3 value) and $5 in Etsy Ads credits per cycle
- **Verbatim snippet:** "Etsy sellers in good standing may opt-in to Etsy Plus, a subscription package offering an expanded set of tools for growing brands. The fee for an Etsy Plus subscription is $10 USD per month. Etsy Plus subscription fees are deducted from your current balance each month and reflected in your payment account."
- **Source:** https://www.etsy.com/legal/fees/
- **source_type:** policy_page
- **verification_status:** blocked_url_index_verified
- **Date:** Accessed April 2026; page undated
- **Signal type:** platform_fee_policy
- **Notes:** Direct fetch returned HTTP 403; verbatim from Google search index.

---

### Finding 41

- **What:** Etsy offsite ads standard fee is 15% on Attributed Orders for shops under $10,000 USD trailing 365-day sales; opt-out available
- **Verbatim snippet:** "If your shop has made less than $10,000 USD in sales over the prior 365 days (going back to February 20, 2019 and later), as calculated on the first day of the month, you will pay a fee of 15% (as described in the section below) on Attributed Orders, unless you opt out of participation in Offsite Ads for the duration your shop is under the $10,000 USD threshold."
- **Source:** https://www.etsy.com/legal/fees/
- **source_type:** policy_page
- **verification_status:** blocked_url_index_verified
- **Date:** Accessed April 2026; page undated
- **Signal type:** platform_fee_policy
- **Notes:** Direct fetch returned HTTP 403; verbatim from Google search index.

---

### Finding 42

- **What:** Etsy offsite ads discounted fee is 12% on Attributed Orders for shops at or above $10,000 USD trailing 365-day sales; mandatory, cannot opt out
- **Verbatim snippet:** "If at any time your shop has made sales of $10,000 USD or more over the prior 365 days (going back to February 20, 2019 and later), as calculated on the first day of the month, you will subsequently pay a fee of 12% (as described in the section below) on Attributed Orders"
- **Source:** https://www.etsy.com/legal/fees/
- **source_type:** policy_page
- **verification_status:** blocked_url_index_verified
- **Date:** Accessed April 2026; page undated
- **Signal type:** platform_fee_policy
- **Notes:** Direct fetch returned HTTP 403; verbatim from Google search index.

---

### Finding 43

- **What:** Etsy offsite ads fee per single Attributed Order capped at $100 USD
- **Verbatim snippet:** "There is no limit to the number of Offsite Ads fees you may be charged on Attributed Orders, but the total Offsite Ads fee you'll pay on a single Attributed Order will not exceed $100 USD."
- **Source:** https://www.etsy.com/legal/fees/
- **source_type:** policy_page
- **verification_status:** blocked_url_index_verified
- **Date:** Accessed April 2026; page undated
- **Signal type:** platform_fee_policy
- **Notes:** Direct fetch returned HTTP 403; verbatim from Google search index.

---

### Finding 44

- **What:** Etsy currency conversion fee is 2.5% on sale amount when listing currency differs from payment account currency
- **Verbatim snippet:** "As an Etsy Payments user, if you decide to list in a currency other than that of your payment account, you will be charged a 2.5% currency conversion fee on the sale amount to send funds to your payment account."
- **Source:** https://www.etsy.com/legal/fees/
- **source_type:** policy_page
- **verification_status:** blocked_url_index_verified
- **Date:** Accessed April 2026; page undated
- **Signal type:** platform_fee_policy
- **Notes:** Direct fetch returned HTTP 403; verbatim from Google search index.

---

### Finding 45

- **What:** Etsy payment processing fees are a set rate plus a percentage of total sale price; rate and percentage vary by country
- **Verbatim snippet:** "Payment processing fees are a set rate plus a percent of the total sale price of the item. This rate and percent vary by country. The fees are taken from the item's total sale price, including its shipping fees, and any applicable sales tax."
- **Source:** https://help.etsy.com/hc/en-us/articles/115015628847-What-are-Payment-Processing-Fees-for-Selling-on-Etsy
- **source_type:** help_center
- **verification_status:** blocked_url_index_verified
- **Date:** Accessed April 2026; page undated
- **Signal type:** platform_fee_policy
- **Notes:** Direct fetch returned HTTP 403; verbatim from Google search index. Page references a country-specific rate table ("Please consult the table below for fees in your location") containing more than 10 countries; detailed per-country extraction requires targeted follow-up per >10 cap rule.

---

### Finding 46

- **What:** Etsy payment processing fees are subject to VAT in required locations; fees are in addition to 6.5% transaction fee
- **Verbatim snippet:** "Payment processing fees are in addition to the 6.5% transaction fee that applies to the cost of the entire order." and "Note: Etsy Payments processing fees are subject to VAT. VAT will be collected and appear on the VAT invoice for sellers in required locations."
- **Source:** https://help.etsy.com/hc/en-us/articles/115015628847-What-are-Payment-Processing-Fees-for-Selling-on-Etsy
- **source_type:** help_center
- **verification_status:** blocked_url_index_verified
- **Date:** Accessed April 2026; page undated
- **Signal type:** platform_fee_policy
- **Notes:** Direct fetch returned HTTP 403; verbatim from Google search index.

---

### Finding 47

- **What:** Etsy offsite ads: buyer must click ad and purchase within 30 days for order to be attributed; no fee if no purchase
- **Verbatim snippet:** "If a buyer clicks through an offsite ad promoting one of your listings and then purchases from your shop within 30 days, that order will be attributed to the ad. You're only charged when a shopper clicks on an ad for one of your listings and purchases from your shop. If a shopper clicks on an ad for your item but doesn't make a purchase, you don't pay a fee."
- **Source:** https://help.etsy.com/hc/en-us/articles/360000338367-How-Etsy-s-Offsite-Ads-Work
- **source_type:** help_center
- **verification_status:** blocked_url_index_verified
- **Date:** Accessed April 2026; page undated
- **Signal type:** platform_fee_policy
- **Notes:** Direct fetch returned HTTP 403; verbatim from Google search index.

---

### Finding 48

- **What:** Etsy offsite ads: shops over $10,000 required to participate for lifetime of shop; cannot opt out even if sales later fall below threshold
- **Verbatim snippet:** "Once you hit the $10,000 USD threshold, you are no longer permitted to opt out of Offsite Ads, prior opt outs while under the $10,000 USD threshold no longer apply, and Etsy may promote your listings or shops under the Offsite Ads program on third-party platforms in our sole discretion, even if you fall below the $10,000 USD threshold at a later date."
- **Source:** https://www.etsy.com/legal/advertising/
- **source_type:** policy_page
- **verification_status:** blocked_url_index_verified
- **Date:** Accessed April 2026; page undated
- **Signal type:** platform_fee_policy
- **Notes:** Direct fetch returned HTTP 403; verbatim from Google search index. Lifetime mandatory participation is confirmed by this policy language.

---

### Finding 49

- **What:** Etsy Plus subscription is $10 USD/month; includes 15 listing credits and $5 Etsy Ads credits; credits don't roll over
- **Verbatim snippet:** "The fee for an Etsy Plus subscription is $10 USD per month, which you'll see deducted from your Payment account balance." and "Credits don't roll over month-to-month and will expire if they're not used. Credits are reset and replenished at the beginning of each monthly subscription cycle."
- **Source:** https://help.etsy.com/hc/en-us/articles/360001589928-What-is-Etsy-Plus
- **source_type:** help_center
- **verification_status:** blocked_url_index_verified
- **Date:** Accessed April 2026; page undated
- **Signal type:** platform_fee_policy
- **Notes:** Direct fetch returned HTTP 403; verbatim from Google search index.

---

### Finding 50

- **What:** Etsy currency conversion fee is 2.5% on sale amount; subtracted before funds reflected in payment account
- **Verbatim snippet:** "Etsy will convert your Etsy Payments sales amounts from your shop currency into the currency of your Payment account. You will be charged a 2.5% currency conversion fee on the sale amount. This fee will be subtracted from your sale amount before the funds are reflected on your Payment account."
- **Source:** https://help.etsy.com/hc/en-us/articles/360000344668-Currency-Conversion-Fees
- **source_type:** help_center
- **verification_status:** blocked_url_index_verified
- **Date:** Accessed April 2026; page undated
- **Signal type:** platform_fee_policy
- **Notes:** Direct fetch returned HTTP 403; verbatim from Google search index.

---

### Finding 51

- **What:** Over 18,000 Etsy sellers pledged strike; petition of nearly 50,000 demanded cancellation of fee increase to 6.5% from 5%
- **Verbatim snippet:** "More than 18,000 Etsy sellers have pledged to join a strike protesting a 30% increase in fees that takes effect today. In a petition signed by nearly 50,000, the organizers are demanding that Etsy CEO Josh Silverman cancel the fee increase to 6.5% from 5%."
- **Source:** https://time.com/6165964/etsy-sellers-strike-over-increase/
- **source_type:** article
- **verification_status:** blocked_url_index_verified
- **Date:** April 2022
- **Signal type:** fee_increase_report
- **Notes:** Direct fetch returned HTTP 403; verbatim from Google search snippet.

---

### Finding 52

- **What:** Etsy previously raised transaction fees in 2018 from 3.5% to 5%
- **Verbatim snippet:** "The company last raised transaction fees in 2018 to 5% from 3.5%."
- **Source:** https://time.com/6165964/etsy-sellers-strike-over-increase/
- **source_type:** article
- **verification_status:** blocked_url_index_verified
- **Date:** April 2022
- **Signal type:** fee_increase_report
- **Notes:** Direct fetch returned HTTP 403; verbatim from Google search snippet. Split from Finding 51 as distinct factual claim (fee history vs. current event).

---

### Finding 53 (Speaker: petition organizers, quoted in BuzzFeed News)

- **What:** Seller petition characterizes fee increase as "pandemic profiteering"; claims fees have more than doubled in less than 4 years
- **Verbatim snippet:** "\"Increasing seller fees by 30% after two years of record sales is nothing short of pandemic profiteering. After the planned increase, our fees as sellers will have more than doubled in less than 4 years\""
- **Source:** https://www.buzzfeednews.com/article/carolineodonovan/etsy-boycott-strike-fees
- **source_type:** article
- **verification_status:** blocked_url_index_verified
- **Date:** April 2022 (approximate)
- **Signal type:** seller_complaint
- **Notes:** Page blocked by robots.txt; verbatim from Google search snippet. Collective voice (petition) quoted in article.

---

### Finding 54

- **What:** Standard Etsy fees (listing, transaction, processing) total roughly 10–11% of a typical US order; rises to 25%+ with offsite ads on lower-priced items
- **Verbatim snippet:** "Standard fees (listing, transaction, and payment processing) total roughly 10% to 11% of a typical US order. That figure rises to 25% or more if Offsite Ads are involved on lower-priced items."
- **Source:** https://www.edesk.com/blog/etsy-seller-fees/
- **source_type:** blog
- **verification_status:** blocked_url_index_verified
- **Date:** Accessed April 2026; page undated
- **Signal type:** fee_burden_claim
- **Notes:** Page blocked by robots.txt; verbatim from Google search snippet.

---

## Part 3 — Pattern candidates (sealed)

This section is the ONLY place where cross-source synthesis, cross-finding observations, or excluded take-rate content may appear.

---

**Pattern 3.1 — Consistent fee burden range across sources**

Multiple independent sources (Findings 1, 7, 11, 16, 19, 54) converge on a baseline Etsy fee burden of approximately **10–15% without offsite ads** and **20–30% with offsite ads**. Marmalead estimates 20–30%+; PBS/The 19th reports sellers citing "as much as 20 percent"; Growing Your Craft estimates 10–15%; Craftybase worked examples show 10.4% (no ads) vs. 23.1% (with ads); eDesk states 10–11% typical rising to 25%+ with offsite ads. The range narrows to roughly 10–12% for baseline US transactions, with offsite ads as the primary escalator.

---

**Pattern 3.2 — Transaction fee escalation history: 3.5% → 5% → 6.5%**

Findings 8, 17, 18, 22, 51, and 52 collectively establish a documented fee escalation timeline: Etsy raised transaction fees from **3.5% to 5% in 2018**, then from **5% to 6.5% in April 2022**. This represents an 86% cumulative increase over roughly 4 years. The April 2022 increase triggered a seller strike (18,000+ participants) and petition (nearly 50,000 signatures). No further transaction fee increase has been announced through 2026 as of research date.

---

**Pattern 3.3 — Offsite ads mandatory enrollment is the dominant seller complaint**

The most emotionally intense and frequently surfaced seller complaints across all third-party sources (Findings 28, 29, 30, 31, 32, 33, 34, 35) concern the mandatory nature of offsite ads for shops exceeding $10,000 in trailing 12-month sales. Sellers specifically object to: (a) the lifetime lock-in even if revenue subsequently drops (Findings 31, 48); (b) the 30-day attribution window capturing repeat customers and organic traffic (Findings 5, 28); (c) fees applied to shipping in addition to item price (Findings 29, 35); and (d) the $10,000 threshold being too low and not accounting for item value (Finding 30). This was the single most common complaint category in the research.

---

**Pattern 3.4 — Setup fee is a recent addition (post-2024)**

Findings 13, 26, and 27 indicate Etsy introduced a one-time shop setup fee of **$15 USD** (one source cites a range of $15–$29). Third-party sources date the introduction to approximately September 2024. This fee does not appear in the indexed version of etsy.com/legal/fees consulted for this research, though one Direction 1 subagent noted the Fees & Payments Policy references a potential one-time setup fee. This item may warrant targeted verification against the live policy page.

---

**Pattern 3.5 — Excluded take-rate content**

Several third-party sources (Marmalead, EcommerceBytes, Craftybase fee calculator page) reference Etsy's "take rate" — the percentage of gross merchandise sales captured as platform revenue. This content was excluded from Findings per the Direction 2 exclusion rule prohibiting "take-rate analysis unless framed as seller fee burden." The EcommerceBytes article (Finding 25) quotes a seller linking activist investor (Elliott Management) pressure to fee increases; this was included because it was framed as seller fee burden, not as investor/margin analysis. General marketplace monetization analysis from Gelato and GlobalFeeCalculator blogs was excluded for the same reason.

---

**Pattern 3.6 — Share & Save program as countervailing factor**

Finding 15 identifies the Share & Save program, which reduces the transaction fee from 6.5% to 2.5% on sales driven by a seller's own shared links. This program was not referenced in any of the Direction 1 official pages consulted, nor in seller complaint sources. It represents a potential offset to fee burden that is not yet widely discussed in third-party commentary.

---

## Part 4 — Could not verify (could_not_verify only)

Findings below are from sources where content could not be directly accessed and search index snippets were insufficient or unreliable for full verification.

---

### Finding 55 (Speaker: TreeSeedMan, Etsy Community forum)

- **What:** Seller reports approximately 26.7% of sale goes to fees and taxes
- **Verbatim snippet:** "is anyone else still there way overcharged and seller fees? I added up my numbers and about 26.7% of my sale goes towards fees and taxes. That is ridiculous"
- **Source:** https://community.etsy.com/t5/Technical-Issues/Seller-fees/td-p/140902282
- **source_type:** seller_forum
- **verification_status:** could_not_verify
- **Date:** January 10, 2023 (from search snippet)
- **Signal type:** seller_complaint
- **Notes:** Etsy Community forum now requires active seller account login (as of ~2024); content captured from Google search snippet only. Could not verify full comment text or context.

---

### Finding 56 (Speaker: WanderingSilverbacks, Etsy Community forum)

- **What:** Worked example: $10 item with $22.23 total transaction cost; $3.13 offsite ads fee (15%); seller calculates effective margin reduction at 31.3%
- **Verbatim snippet:** "First; frustrated that Etsy opt'ed me into Offsite Ads without my permission. I have an item for sale that sells for $10. Total transaction cost was $22.23. Etsy is taking $3.13 in Offsite Ads (15% of the $22.23). An Advertising Fee should be assessed only on the value of the item sold not on the shipping fee, transaction fee, or taxes. This math reduces a seller's margin not by 15% but by 31.3% in my example. How does this get disputed?"
- **Source:** https://community.etsy.com/t5/Technical-Issues/Offsite-Ad-Fee/td-p/147505829
- **source_type:** seller_forum
- **verification_status:** could_not_verify
- **Date:** Accessed April 2026; date not visible in snippet
- **Signal type:** worked_example
- **Notes:** Etsy Community forum requires login; content from Google search snippet only. Username inferred from reply context. Could not verify full thread or confirm username attribution.

---

### Finding 57 (Speaker: dayspringcollectible, Etsy Community forum)

- **What:** Seller raised prices by $1 across 400+ listings to offset mandatory offsite ads lock-in
- **Verbatim snippet:** "I added one dollar to over 400 listings because I'm locked into offsite ads."
- **Source:** https://community.etsy.com/t5/Technical-Issues/Offsite-Ad-Fee/m-p/147506019
- **source_type:** seller_forum
- **verification_status:** could_not_verify
- **Date:** Accessed April 2026; date not visible in snippet
- **Signal type:** seller_complaint
- **Notes:** Etsy Community forum requires login; content from Google search snippet only. Could not verify full comment text or context.

---

### Finding 58 (Speaker: anonymous commenter, Marmalead blog)

- **What:** Supply seller complaint: cannot raise prices above MSRP to absorb offsite ads; locked into mandatory program permanently after exceeding $10K
- **Verbatim snippet:** "Hah, what a boondoggle, Etsy punishes successful sellers. Yes, I know all the lather about raising my prices – what Etsy doesn't consider are supply sellers – I *can't* raise my prices above MSRP. And what happens when a shop has a good year, going over that $10K mark and then I can't get the product anymore? Revenue drops from $10K down to a grand. But I'm still forcibly committed to offsite ads. So now I contemplate not selling on Etsy at all. Lose/lose."
- **Source:** https://blog.marmalead.com/the-truth-about-etsy-offsite-ads-are-they-worth-it/
- **source_type:** blog
- **verification_status:** could_not_verify
- **Date:** Accessed April 2026; comment undated
- **Signal type:** seller_complaint
- **Notes:** Anonymous commenter with no date; could not verify identity, date, or whether comment is still present on page. Comment section may have been accessed via search snippet rather than direct page fetch.

---

### Finding 59 (Speaker: anonymous Canadian seller, Made Urban blog)

- **What:** Canadian seller reports fees increased from about 11% to about 20% of total sales after fee increases and mandatory marketing charge
- **Verbatim snippet:** "Etsy used to be a great place to sell but, as a seller in Canada, it is no longer worth. Their increase in fees and addition of that much-despised 'marketing' charge have moved my fees from about 11% of my sales up to about 20% of my total sales. (including shipping and taxes!) As well, they no longer send US buyers to shops outside the USA."
- **Source:** https://www.madeurban.com/blog/is-selling-on-etsy-worth-it-in-2019/
- **source_type:** blog
- **verification_status:** could_not_verify
- **Date:** Accessed April 2026; comment undated (article updated for 2024)
- **Signal type:** seller_complaint
- **Notes:** Anonymous commenter in blog comment section; could not verify comment is still present on live page or confirm identity/date.

---

## Research QA Notes

**1. Findings forced into Provisional due to blocked direct access:**
Yes. All Direction 1 findings (Findings 36–50) are blocked_url_index_verified because every official Etsy page (etsy.com/legal/*, help.etsy.com/*) returned HTTP 403 on direct fetch. Content was extracted from Google search index snippets, which are substantial but not guaranteed to reflect the current live page. Additionally, three Direction 2 sources were blocked: TIME (403), BuzzFeed News (robots.txt), and eDesk (robots.txt) — these are Findings 51–54.

**2. Structured-layout snippets required:**
Yes. Findings 7, 9, and 10 contain worked examples presented in slash-separated layout format as originally published on the source pages. These are labeled as structured layout snippets in Notes.

**3. Country-specific fee table hit the >10 cap rule:**
Yes. The Etsy payment processing fee page (Finding 45) references a country-specific rate table containing more than 10 countries. Per the >10 cap rule, one general finding was recorded and a note was added that detailed per-country extraction requires targeted follow-up.

**4. Candidates rejected for violating one-finding-one-source:**
No candidates were rejected for this reason. All findings cite a single URL.

**5. Candidates split because one page had multiple distinct speakers:**
Yes. The following pages contained multiple distinct speakers and were split accordingly:
- PBS/The 19th article (Findings 18–21): article reporting, Sydney Sky Griffin, Brontë Grimm
- NPR article (Findings 22–23): article reporting, strikers' letter
- EcommerceBytes article (Findings 24–25): article reporting, unnamed seller
- Craft Industry Alliance blog comments (Findings 28–35): Jan Manley, Deb Grogan, Lori, Carrol Thornby, Ruth Mierzwa, Alecse, Lacey, Lisa Smallridge
- Sellers Ask Sellers forum (Findings 26–27): joebcrafts, ModernSwitch
- Etsy Community forum threads (Findings 55–57): TreeSeedMan, WanderingSilverbacks, dayspringcollectible

**6. Source_type classification felt ambiguous:**
Yes. The Craft Industry Alliance page (craftindustryalliance.org) hosts an article with an active comment section where individual sellers post substantive commentary. The page URL sits under /blog/ and the content functions as a blog post, but the comments function as a seller discussion forum. Classified as source_type: blog based on page structure. The distinction between "blog comments from sellers" and "seller_forum" is not cleanly resolved by the current schema. Similarly, the Made Urban blog comment section (Finding 59) has seller commentary that could be classified as seller_forum but was classified as blog.

**7. Take-rate/monetization content excluded or moved to Part 3:**
Yes. Several sources contained take-rate analysis, marketplace monetization discussion, and investor-oriented commentary. This content was excluded from Findings and documented in Part 3, Pattern 3.5 (Excluded take-rate content). The Gelato blog and GlobalFeeCalculator blog were excluded entirely as their primary framing was marketplace business-model commentary rather than seller fee burden. The EcommerceBytes article's reference to Elliott Management was included (Finding 25) because the quoted seller framed it specifically as a fee burden concern.

**8. Additional observations:**
- Reddit content was effectively inaccessible. Multiple search queries targeting site:reddit.com returned no directly fetchable Reddit thread URLs for Etsy fee discussions. Reddit seller commentary was recovered only indirectly through news articles quoting Reddit users.
- The Etsy Community forum (community.etsy.com) transitioned to requiring active seller login for most sections (approximately 2024–2025). Only search engine cached snippets were available. Three findings were placed in Part 4 accordingly.
- The Etsy seller landing page (etsy.com/sell) could not be accessed or indexed; it typically shows a simplified fee overview for prospective sellers but was unavailable for this research.
- An Etsy "Regulatory Operating fee" was mentioned across multiple sources (applicable in select countries at 0.25%–1.1%) but was not in the six required Direction 1 fee categories. It appears in some Direction 2 findings as contextual detail.
- The Etsy "Pattern" subscription ($15/month) was mentioned in sources but was not in the six required fee categories and was not extracted as a standalone finding.