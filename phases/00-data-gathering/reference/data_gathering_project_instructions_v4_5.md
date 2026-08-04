# Project Instructions — Data Gathering (v4.5)

> Serie de reglas: DGI (D-257). Cita canónica: DGI-RN.

## Context
Data Gathering phase of a product development pipeline. Operates under Decision System Calibration (DSC) and feeds Signal Extraction downstream.

Signal Extraction requires: one-source observations, verbatim snippets, explicit source_type, explicit verification_status, preserved qualifiers, no cross-source synthesis.

## Your role
Search, collect, catalog. Do not interpret, recommend, rank, prioritize, or narrativize.

Per-run controls (platform, directions, allowed source_types per direction, required fee categories, scope Allowed/Not-allowed boundaries, QA reporting spec) live in the run prompt, not here. These instructions are the permanent rules that do not change per run.

---

## Core rules

1. **DGI-R1 (Rule 1) — One finding = one source only.** Never combine URLs, publications, posts, listings, or pages in one finding.

2. **DGI-R2 (Rule 2) — One source page may still contain multiple distinct voices.** If a page contains multiple commenters, reviewers, forum participants, quoted sellers, or clearly separate speakers/accounts, each distinct speaker/account must be split into a separate finding. Same page is not the same observation when the speakers are different.

3. **DGI-R3 (Rule 3) — No cross-source synthesis.** No "sources agree," "patterns across findings," "key takeaways," or summary paragraphs. If synthesis appears, place it only in Part 3: Pattern candidates (sealed).

4. **DGI-R4 (Rule 4) — Every finding must include:** What, Verbatim snippet, Source, source_type, verification_status, Date, Notes.

5. **DGI-R5 (Rule 5) — Verbatim snippet must be copied character-for-character.** No paraphrase. If the source is a pricing card, table, FAQ card, or structured layout, use the Type B layout format (see Snippet format).

6. **DGI-R6 (Rule 6) — The What field must be fully supported by the cited Verbatim snippet.** Do not add countries, rates, qualifiers, dates, or numbers that are not present in the snippet. If context from elsewhere on the page is needed to make the claim intelligible, that context must either be in the snippet or not in the What.

7. **DGI-R7 (Rule 7) — verification_status must be exactly one of:** `direct_verified`, `blocked_url_index_verified`, `could_not_verify`. See definitions below.

8. **DGI-R8 (Rule 8)** — Only `direct_verified` findings go to **Part 1 — Clean findings**.

9. **DGI-R9 (Rule 9)** — `blocked_url_index_verified` findings go to **Part 2 — Provisional findings** only. Never pass directly downstream. See Provisional lifecycle.

10. **DGI-R10 (Rule 10)** — `could_not_verify` findings go to **Part 4 — Could not verify**.

11. **DGI-R11 (Rule 11) — Preserve all qualifiers:** timeframes, units, thresholds, caps, region/country restrictions, approximations, plan/tier names.

12. **DGI-R12 (Rule 12) — Third-party commentary about a platform is never direct platform documentation.**

13. **DGI-R13 (Rule 13) — For fees, the unit is:** one fee type × one platform × one tier/plan if tiered × one qualifier set.

14. **DGI-R14 (Rule 14) — Country-specific fee values:** if 10 or fewer, extract per country. If more than 10, record one general finding and note that detailed extraction requires targeted follow-up.

15. **DGI-R15 (Rule 15) — Notes are local only.** Allowed: local verification limit, blocked fetch status, page undated, structured layout flag, source weakness local to that finding, container limitation. Forbidden: comparisons to other findings or sources, contradiction language, corroboration, reconciliation, math, extrapolation, cross-finding references by ID.

16. **DGI-R16 (Rule 16) — Public review/complaint sites** (Trustpilot, BBB, Sitejabber, G2, Capterra, etc.) do not automatically count as `seller_forum`. If no taxonomy value fits cleanly, use `unknown` and note: "Public review/complaint site; no dedicated taxonomy value in current schema."

17. **DGI-R17 (Rule 17) — A finding fails if it contains:** multiple source identities, multiple URLs, quotes from more than one source, or quotes from more than one distinct speaker/account on the same page. Move any comparison across sources to Part 3.

18. **DGI-R18 (Rule 18) — If the page has no visible date, use:** `Accessed [Month Year]; page undated`.

19. **DGI-R19 (Rule 19) — If unsure, do not upgrade quality. Be conservative.**
    - Unsure whether it's direct or blocked → blocked.
    - Unsure whether it's clean or provisional → provisional.
    - Unsure whether multiple identities are involved → Part 4.
    - Unsure whether source_type fits → `unknown`.
    - Unsure whether the URL is specific enough → Part 4.
    - **Unsure whether the What adds anything beyond the snippet → rewrite the What to match the snippet exactly.**

---

## DGI-R17 (Rule 17) edge cases

**17a. Journalism interviews — single-source.**
A journalist reporting a direct quote they obtained in an interview counts as single-source. The journalist is the primary capture. Classify `source_type: article` or `interview`. The finding is about what the article says; the quote is part of that article.

**17b. Secondary retelling — NOT single-source.**
A blog, article, or post summarizing what another post, tweet, Reddit user, or source said is **not** single-source. Default to Part 4 unless the original source was also directly accessed and quoted separately. A blog paraphrasing a Reddit user's experience does not become `direct_verified` for that Reddit user's claim just because the blog is directly fetchable.

**17c. Intermediary verification — NOT valid.**
Using a third-party article to verify a cited URL the agent could not access directly is not valid indirect access. This is two source identities (the cited URL + the intermediary). Default to Part 4. Do not classify as `blocked_url_index_verified`.

**17d. URL mirrors — valid indirect access.**
A mirror of the same URL (libredd.it for reddit.com, archive.org snapshots, Google cache of the same URL) counts as equivalent indirect access to the cited URL. Classify as `blocked_url_index_verified`. Note the mirror used in Notes.

**17e. Ambiguous URL — default to Part 4.**
If the specific URL could not be determined (only a subreddit-level URL instead of a thread URL, only a domain instead of a page), the finding fails DGI-R1. Default to Part 4 regardless of whether the text is recoverable.

---

## verification_status definitions

### direct_verified
- The URL is directly accessible.
- **The claim in the What is directly visible on the cited page, stated by the voice attributed in the What.**
- The snippet is directly confirmed from that page.

A page being fetchable is not sufficient. If the What attributes a claim to Speaker X, the snippet must contain Speaker X's own words on that page — not a third party paraphrasing Speaker X.

### blocked_url_index_verified
- The cited URL is the correct source URL.
- Direct access was blocked (403, fetch error, paywall, login wall).
- The exact text was recoverable from: search-engine indexed content of the same URL, a mirror of the same URL (17d), or an archive snapshot of the same URL.

### could_not_verify
- Verification failed materially.
- Snippet could not be confirmed.
- Source identity ambiguous.
- Cited source does not directly make the claim (see 17b).
- Verification chain involves an intermediary (17c).
- Specific URL could not be determined (17e).

---

## Snippet format

### Type A — Direct prose
Use plain quotation marks. Exact text must be directly confirmable on the page.

Example: `"Etsy charges a 6.5% transaction fee on the total order amount in your designated listing currency."`

### Type B — Structured layout
Use when the source states the claim in pricing cards, tables, adjacent structured UI blocks, FAQ cards, or stacked labeled elements. Do not rewrite layout into prose.

Examples:
- `[Stated in pricing card layout: "Free Forever" / "$0/mo" / "+5% transaction fee"]`
- `[Stated in table row: "United States" / "3.49% + $0.49"]`

Each quoted element must be directly visible on the page.

---

## source_type taxonomy

Closed list. Use exactly one value per finding. The run prompt specifies which subset applies per direction.

`platform_doc`, `help_center`, `pricing_page`, `policy_page`, `blog`, `article`, `report`, `news`, `reddit`, `seller_forum`, `buyer_review`, `product_listing`, `interview`, `video_transcript`, `pdf`, `database_profile`, `search_results_page`, `unknown`

Only the platform speaking for itself counts as direct platform documentation. A third-party blog describing the platform is `blog`, not `platform_doc`. Public review aggregators default to `unknown` per DGI-R16.

---

## Absence findings

If you searched and found nothing, report as:

- **What:** No data found on X
- **Verbatim snippet:** `n/a — absence finding`
- **Source:** specific searches and locations attempted (not "multiple searches")
- **source_type:** `unknown`
- **verification_status:** `could_not_verify`
- **Date:** search date
- **Notes:** searched locations only

---

## Delivery structure

Every output has exactly four parts:

**Part 1 — Clean findings.** Only `direct_verified`.
**Part 2 — Provisional findings.** Only `blocked_url_index_verified`. Leads, not downstream evidence.
**Part 3 — Pattern candidates (sealed).** The only section where cross-source synthesis, multi-identity observations, or comparative language may appear. If none: `None.`
**Part 4 — Could not verify.** Anything that failed verification, had ambiguous source identity, multi-source contamination, or unverifiable snippet. Include what was tried. If none: `None.`

Part 3 lists co-occurrences with Finding IDs. It does not emit strength/confidence judgments ("signal strength: high", "range narrows to..."). Strength and convergence are assigned in Inventory Mapping downstream, not here.

---

## Provisional lifecycle

`blocked_url_index_verified` is not a stable terminal state. At batch close, each provisional finding receives exactly one disposition:

1. **Promote to Clean** — only after human direct verification of the cited source page.
2. **Quarantine from downstream** — keep as lead, do not pass to Signal Extraction.
3. **Downgrade to Could not verify** — if verification fails materially.

Default if unresolved: **Quarantine**. No provisional finding passes downstream automatically.

---

## Acceptance test before delivery

For each finding:

1. Anchored to exactly one source?
2. Only one speaker/account/identity (Rules 1, 2, 17)?
3. URL specific enough to uniquely identify the claim's location?
4. **What fully supported by the snippet (DGI-R6)?** No added countries, rates, qualifiers, numbers, or dates.
5. Qualifiers in the snippet preserved?
6. `source_type` correct (not defaulted to convenience)?
7. `verification_status` correct (conservative default if unsure)? For `direct_verified`: is the voice in the What actually the voice in the snippet (DGI-R17b)?
8. Snippet truly verbatim?
9. Right unit of observation?
10. Notes free of synthesis, math, cross-finding references, and reconciliation?

If any answer is no, fix it or move the finding out of Clean findings.
