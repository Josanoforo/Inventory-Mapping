# URL Normalization Design

**Status:** Design only. Not yet executed.

---

## Motivation

299 of 1,561 legacy Signal Cards carry source references that contain a recognizable domain or domain/path string without a protocol prefix (e.g., `etsy.com/listing/1603401096`, `wordsrated.com/amazon-publishing-statistics/`). These are mechanically recoverable by prepending `https://`.

**Constraint from user:** The raw `source` field in `card_index.jsonl` must not be overwritten. The normalization must be non-destructive, auditable, idempotent, and strict-pattern only.

---

## Output artifact

**File:** `legacy-migration/working/preprocessing/normalized_source_refs.jsonl`

One record per card in the full corpus. Fields:

| Field | Type | Description |
|---|---|---|
| `signal_id` | string | Matches `id` in `card_index.jsonl` |
| `original_source` | string | Verbatim value of `source` from `card_index.jsonl` — never modified |
| `normalized_url` | string \| null | Extracted and normalized URL if pattern matched; null otherwise |
| `normalization_applied` | boolean | True only if a transformation was performed |
| `pattern_matched` | string | One of `https_prepend`, `https_already_present`, `url_not_identified`, `domain_name_only` |
| `normalization_confidence` | string | `strict` (domain + path identified) or `domain_only` (name only, no path) |

---

## Transformation rules (strict)

**Rule 1 — Already has protocol:** If any segment of `source` already starts with `https://` or `http://`, extract as-is. `normalization_applied = false`, `pattern_matched = https_already_present`.

**Rule 2 — Domain + path without protocol:** If a segment matches `^([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}(/[^\s,;—()\"\']+)` (domain followed by at least one path segment), prepend `https://`. `normalization_applied = true`, `pattern_matched = https_prepend`, `normalization_confidence = strict`.

**Rule 3 — Domain name only (no path):** If a segment matches `^([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$` (bare domain, e.g., `Marketsy.ai`, `LaRepublica.es`), record as `domain_name_only`. `normalization_applied = false`. No URL constructed — a bare domain name is not a stable URL.

**Rule 4 — No match:** Source contains no identifiable URL or domain pattern. `normalized_url = null`, `normalization_applied = false`, `pattern_matched = url_not_identified`.

---

## What is NOT done

- No guessing from free text (e.g., "Etsy marketplace (observed)" → no URL generated)
- No constructing URLs from platform name + search term
- No modifying `card_index.jsonl` in any way
- No normalization for bare domain names (Rule 3) — these remain partial references
- No HTTP → HTTPS upgrade on already-present `http://` URLs (leave as-is, flag for review)

---

## Idempotency

Running the transform twice over the same `card_index.jsonl` produces identical output. The transform reads only `source` (never the output artifact) and applies the same deterministic regex rules.

---

## Exact corpus coverage

Computed 2026-04-05 against full `card_index.jsonl` (1,561 cards) using the exact rules above.

| Pattern | Count | Notes |
|---|---|---|
| `https_already_present` | 1,101 | Source contains `https?://`; no normalization applied |
| `https_prepend` | 232 | Domain + at least one path segment, no protocol — `https://` prepended |
| `domain_name_only` | 27 | Bare domain (e.g., `Marketsy.ai`, `LaRepublica.es`); no URL constructed per Rule 3 |
| `url_not_identified` | 201 | Free text, methodology notes, or absence findings; no URL pattern found |
| **Total** | **1,561** | |

**Note on the 299 figure:** an earlier exploratory count using a looser regex (path optional) reported 299 candidates. That run collapsed `https_prepend` and `domain_name_only` into a single bucket. The figures here use the rules as defined above, which treat bare domain names separately and produce no URL for them. 232 is the authoritative count for cards where `https://` will actually be prepended.

---

## Integration with migration rail

During a full-corpus migration run, the migration skill reads `normalized_source_refs.jsonl` (if present) as a supplementary lookup. For each card:
- If `normalization_applied = true`, use `normalized_url` as the `reference_stable` candidate
- If `normalization_applied = false`, use original `source` field (existing behavior unchanged)

The migration record always records `legacy_source_ref_raw` from the original `source` field, regardless of normalization state.
