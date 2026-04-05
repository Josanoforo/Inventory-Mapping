# URL Normalization — Execution Summary

**Executed:** 2026-04-05  
**Script:** `legacy-migration/working/preprocessing/run_url_normalization.py`  
**Input:** `working/index/card_index.jsonl` (read-only)  
**Output:** `legacy-migration/working/preprocessing/normalized_source_refs.jsonl`

---

## Counts by pattern

| Pattern | Actual | Design expectation | Match |
|---|---|---|---|
| `https_already_present` | 1101 | 1101 | ✓ |
| `https_prepend` | 232 | 232 | ✓ |
| `domain_name_only` | 27 | 27 | ✓ |
| `url_not_identified` | 201 | 201 | ✓ |
| **Total** | **1561** | **1561** | ✓ |

All four counts match the design specification exactly.

---

## card_index.jsonl modification status

`card_index.jsonl` was **not modified**. The script opens it read-only and writes exclusively to `normalized_source_refs.jsonl`. The `original_source` field in every output record is the verbatim value from the input — no transformation is applied to it.

---

## Sampled examples (20 across categories)

### https_already_present (1101 records) — 5 samples

| signal_id | original_source (truncated) | normalized_url (extracted) |
|---|---|---|
| SC-R8-099 | `Notion Marketplace Guidelines & Terms — https://www.notion.com/help/template-gal…` | `https://www.notion.com/help/template-gallery-guidelines-and-terms` |
| SC-R3-072 | `Fitnancials.com — https://www.fitnancials.com/sell-planners-on-etsy/` | `https://www.fitnancials.com/sell-planners-on-etsy/` |
| SC-R3-068 | `Etsy listing — https://www.etsy.com/listing/773727113/` | `https://www.etsy.com/listing/773727113/` |
| SC-R4-070 | `Creativebutfine.substack.com (Etsy digital seller) — https://creativebutfine.sub…` | `https://creativebutfine.substack.com/p/youre-probably-underpricing-your` |
| SC-R6-024 | `Gumroad. URL: https://gumroad.com/design/print-and-packaging/canva?sort=hot_and_…` | `https://gumroad.com/design/print-and-packaging/canva?sort=hot_and_new` |

`normalization_applied = false` for all — URL already present, extracted as-is.

---

### https_prepend (232 records) — 5 samples

| signal_id | original_source (truncated) | normalized_url |
|---|---|---|
| SC-R10-106 | `Authors Guild — authorsguild.org/news/amazons-new-disclosure-policy-for-ai-…` | `https://authorsguild.org/news/amazons-new-disclosure-policy-for-ai-generated-book-content-is-a-welcome-first-step/` |
| SC-R10-180 | `CBC News — cbc.ca/news/canada/saskatchewan/mushroom-picking-ai-generated-1.750…` | `https://cbc.ca/news/canada/saskatchewan/mushroom-picking-ai-generated-1.7502667` |
| SC-R10-025 | `writerontheside.com/gumroad-vs-amazon-kdp/` | `https://writerontheside.com/gumroad-vs-amazon-kdp/` |
| SC-R2-024 | `Etsy shop, etsy.com/shop/Sheetastic` | `https://etsy.com/shop/Sheetastic` |
| SC-R10-037 | `selfmademillennials.com/gumroad-review/` | `https://selfmademillennials.com/gumroad-review/` |

`normalization_applied = true`, `normalization_confidence = strict` for all.

---

### domain_name_only (27 records) — 5 samples

| signal_id | original_source | normalized_url |
|---|---|---|
| SC-R2-047 | `Gumroad, spreadsheetpoint.gumroad.com` | `null` |
| SC-R1-039 | `Comnectado.com` | `null` |
| SC-R10-170 | `kentonlibrary.org` | `null` |
| SC-R1-038 | `Comnectado.com` | `null` |
| SC-R10-154 | `doingcontentright.com` | `null` |

`normalization_applied = false`, `normalization_confidence = domain_only`. No URL constructed per Rule 3 — bare domain names are not stable URLs.

---

### url_not_identified (201 records) — 5 samples

| signal_id | original_source |
|---|---|
| SC-R10-083 | `Publishers Weekly` |
| SC-R1-032 | `Blog personal de Gerardo Marote (con capturas del dashboard de KDP)` |
| SC-R1-007 | `Hotmart (platform-reported)` |
| SC-R10-142 | `LinkedIn by India Lindsey` |
| SC-R2-036 | `Etsy market pages (etsy.com/market/)` |

`normalized_url = null`, `normalization_applied = false`. Includes free-text descriptions, methodology notes, and cases where a domain appears only inside parentheses (not at segment start — strict-pattern only, no guessing).

---

## Implementation notes

- **Segment splitting:** sources are split on `,\s+|\s+[—–|]\s+|;\s+` before applying anchored Rules 2 and 3. This correctly handles the `"Label — domain.com/path"` and `"Platform, domain.com/path"` patterns common in the corpus.
- **Rule 1** (protocol already present) scans the whole string — no splitting needed.
- **Rules 2 and 3** use `^`-anchored patterns per segment, preventing false matches where a domain appears embedded in narrative text (e.g., `Etsy market pages (etsy.com/market/)` → `url_not_identified`, not `https_prepend`).
- The script is idempotent: re-running against the same `card_index.jsonl` produces bit-identical output.
