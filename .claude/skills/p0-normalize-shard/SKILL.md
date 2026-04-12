# p0-normalize-shard — Skill

Read before executing:
- `phases/00-data-gathering/reference/data_gathering_project_instructions_v4_5.md`
- `phases/00-data-gathering/reference/research_directions_protocol.md`
- One working shard as a canonical format reference (e.g. `input/data_gathering/shards/deep_search/compass_artifact_wf-d5fe5a2c-6077-4bcd-ad62-c4fe3960e23a_text_markdown.md`)

## Purpose

Normalize a Phase 0 shard that does not conform to the canonical 4-part delivery format so that `parse_dg_shard.py` can process it without modification.

## When to use

Run this skill on a shard **before** calling `parse_dg_shard.py` when the shard:
- Uses non-standard section headers (Category N, GROUP A/B, Parte N, topical headings)
- Uses non-standard finding headers (`### Finding N —`, `### A1.`, `**Finding ID:** F-NN`, field-only blocks)
- Uses non-standard verification labels ("Verified", "Partially verified", no verification_status at all)

**Do not run** on a shard that already has `## Part 1` / `## Part 2` / `## Part 4` headers **and** finding blocks that start with `### F-NN` or `## F-NN` or `**F-NN**` headings — it will already parse correctly.

## Steps

### Step 1 — Canonical format check

Read the shard. Test all three conditions:
1. Does the file contain a `## Part 1` (or `# N. Part 1`) section header?
2. Does the file contain a `## Part 2` section header?
3. Do finding blocks open with `### F-NN`, `## F-NN`, or `**F-NN**` on their own line?

If all three are true → **stop**. Output: "Shard already in canonical format — no normalization needed." Do not write any file.

---

### Step 2 — Read and inventory the shard

Read the entire shard. Identify and count:
- All discrete finding blocks (blocks containing at least Verbatim/snippet AND Source/URL)
- All Part 4 / could-not-verify / absence blocks
- Any pattern candidate blocks (cross-source synthesis, PC-NN IDs)
- Any non-finding content (narrative prose, tables without individual source anchors, search decomposition)

A block qualifies as a finding if and only if it contains:
- A verbatim snippet (a quoted passage or structured layout excerpt from a single source), AND
- A source URL, AND
- At least one of: What/claim description, Date, source_type

Blocks that contain only narrative summary, cross-source comparison, or data with no single-source anchor are **not findings** — they are either pattern candidates (Part 3) or discarded context.

**Aggregated section lists — special handling:**

Some shards organize content as an aggregated category section: a bolded or heading-level topic label (e.g., "Analytics and market intelligence tools:", "Listing optimization and AI writing tools:") followed by a flat bulleted list where every item is homogeneous — each bullet names a distinct entity, provides verbatim text cited from that entity's own source, and includes a URL either explicitly in parentheses immediately after the name (e.g., `(gumtrends.com)`, `(putler.com/integrations/gumroad)`) or as an inline domain string matching the entity name.

Treat each bullet in such a list as an **individual finding**, not as part of a single aggregate block. Apply the standard finding qualification test (verbatim snippet + source URL + at least one of What/Date/source_type) to each bullet individually.

The section-level topic label (e.g., "Third-party tools and services built around Gumroad") is **not a finding** and its URL, if any, is not inherited by the bullets. Record it in the Notes of each child finding as: `"section: [label]"`.

A section qualifies as an aggregated section list only when **all** of the following hold:
1. The section header or sub-header describes a topic category — not a specific named source.
2. Each bullet names a distinct entity different from the others.
3. Each bullet contains its own verbatim excerpt in quotation marks cited from that entity's material.
4. Each bullet includes a URL or a named source reference resolvable to a URL (see Step 3 for derivation rules).

Contrast with aggregate tables (pricing tables, cross-source statistics, multi-source comparison blocks): those remain pattern candidates routed to Part 3, PC-NN. Sub-headers within a section (e.g., "Analytics tools:" then "SEO tools:") are organizational scaffolding only; the bullets beneath them are still individual findings if the four conditions above hold.

Inline named-source citations in prose (e.g., "Gumroad's help documentation states: '...'", "A GitHub issue (#682) reveals: '...'") also qualify as individual findings when they name a specific source, carry a verbatim quote, and the URL is derivable (see Step 3). They are not aggregated section list items structurally, but follow the same per-item extraction and URL derivation rules.

---

### Step 3 — Determine verification_status for each finding

For each finding block:

| Source signal in the block | Assigned verification_status |
|---|---|
| Explicit `verification_status: direct_verified` | `direct_verified` |
| Explicit `verification_status: blocked_url_index_verified` | `blocked_url_index_verified` |
| Explicit `verification_status: could_not_verify` | `could_not_verify` |
| `Verified` or `directly verified` | `direct_verified` |
| `Partially verified` or `snippet only` or `search snippet` + URL present | `blocked_url_index_verified` |
| GROUP A heading | `direct_verified` |
| GROUP B heading | `blocked_url_index_verified` |
| GROUP C or GROUP D heading | `could_not_verify` |
| `Accessibility: direct fetch` or `Access: direct web_fetch` | `direct_verified` |
| `Accessibility: blocked` or `access: 403` or `search snippet only` | `blocked_url_index_verified` |
| Item from an aggregated section list AND has a per-item URL (explicit in parentheses or as inline domain) AND has verbatim content cited from that specific source | `direct_verified` |
| Item from an aggregated section list AND named source reference present but URL must be derived (e.g., "Gumroad's help documentation", "GitHub issue #NNN") AND has verbatim content from that source | `direct_verified` |
| No verification signal AND URL present | `could_not_verify` (conservative default) |
| No URL | `could_not_verify` |

**URL derivation for aggregated section list items:** When a bullet item or inline named-source citation provides a named reference rather than an explicit URL, derive the URL using these patterns and document in Notes:

- Domain in parentheses: prepend `https://`. Example: `(gumtrends.com)` → `https://gumtrends.com`.
- Path in parentheses: prepend `https://`. Example: `(putler.com/integrations/gumroad)` → `https://putler.com/integrations/gumroad`.
- "Gumroad's help documentation" or "the help center" with no further qualifier → `https://help.gumroad.com`. Note: `"URL derived from named source reference in shard: 'Gumroad's help documentation' → help.gumroad.com"`.
- "GitHub issue #NNN" or "A GitHub issue (#NNN)" → `https://github.com/[org]/[repo]/issues/NNN` where org/repo are determinable from the shard's research context. Note: `"URL derived from named source reference in shard: 'GitHub issue #682' → github.com/gumroad/gumroad/issues/682"`.
- Tool name that is itself a domain (e.g., "fullStats.io" as the item name) → `https://fullstats.io`.

Write `"URL derived from named source reference in shard: [rationale]"` in Notes. Do **not** use the word "inferred" for derivations — reserve "inferred" solely for the conservative-default `could_not_verify` case below.

When assigning conservatively, add to the finding's Notes field: `"verification_status inferred during normalization: [reason]"`

---

### Step 4 — Route findings to Parts

| verification_status | Target Part |
|---|---|
| `direct_verified` | Part 1 |
| `blocked_url_index_verified` | Part 2 |
| `could_not_verify` | Part 4 |

Absence findings (source was searched, nothing found) → Part 4 regardless of how they are labelled.

Pattern candidates (cross-source synthesis, references to multiple findings) → Part 3.

---

### Step 5 — Assign canonical IDs

Within each Part, assign IDs sequentially:
- Part 1: `F-01`, `F-02`, `F-03`, …
- Part 2: `F-P01`, `F-P02`, `F-P03`, …
- Part 4: `F-X01`, `F-X02`, `F-X03`, …
- Part 3: no new IDs (reference existing Part 1/2 IDs)

If the original finding had an ID (any format: `T-1`, `A3`, `Finding 5`, `F-01`), preserve it in the finding's Notes field: `"Original ID: [original_id]"`. Do not use original IDs as the canonical ID.

---

### Step 6 — Map fields to canonical labels

Translate any non-canonical field labels to the canonical set. **Never modify the content of these fields — only the label.**

| Original label(s) | Canonical label |
|---|---|
| Verbatim quote, Verbatim text, Verbatim | `Verbatim snippet` |
| URL, Source URL | `Source` |
| Access, Accessibility, Access method | (fold into Notes) |
| Speaker, Platform | (fold into Notes) |
| Page date | `Date` |
| Verification, Verification status | `verification_status` |
| Key data | (fold into Notes) |
| Category | (fold into Notes) |
| Layout | (fold into Notes) |
| What, Workflow claim | `What` |
| source_type | `source_type` |
| Notes | `Notes` |

Fields that have no canonical equivalent are folded into Notes as `"[OriginalLabel]: [value]"` — never discarded.

---

### Step 7 — Assemble the normalized shard

Write the normalized file with this exact structure:

```
# [original shard title, unchanged]

[original direction/scope statement, unchanged if present]

---

## Part 1 — Clean findings (direct_verified)

[If no Part 1 findings:]
None.

[For each Part 1 finding:]
### F-NN: [subject or first few words of What]

**What:** [content unchanged]
**Verbatim snippet:** [content unchanged, verbatim]
**Source:** [URL unchanged]
**source_type:** [value]
**verification_status:** direct_verified
**Date:** [value]
**Notes:** [original notes] Original ID: [original_id]. [any folded fields].

---

## Part 2 — Provisional findings (blocked_url_index_verified)

[Same structure as Part 1, IDs as F-P01, F-P02, …]

---

## Part 3 — Pattern candidates (sealed)

[Preserve any cross-source synthesis blocks found in the original, unchanged.]
[If none:] None.

---

## Part 4 — Could not verify

[Same structure, IDs as F-X01, F-X02, …]
[Absence findings go here.]

---

## Research QA Notes

[Preserve original QA notes section if present.]
[If absent:] QA notes not present in source shard.
```

**Invariants:**
- Every finding must open with `### F-NN:`, `### F-PNN:`, or `### F-XNN:` on its own line.
- Verbatim snippet content is never modified — not a single character.
- What content is never rewritten, summarized, or expanded.
- Source URL is never modified.
- The original shard file is never touched.

---

### Step 8 — Write output

Write the normalized content to:
```
[same directory as original]/[original_stem]_normalized.md
```

Example: `compass_artifact_wf-22c5fbd5-..._text_markdown_normalized.md`

---

### Step 9 — Report

For each shard processed, output a report with:

```
Shard: [filename]
Findings identified in original: N
  → Part 1 (direct_verified): N
  → Part 2 (blocked_url_index_verified): N
  → Part 4 (could_not_verify): N
Part 3 pattern candidates: N
Blocks discarded (not findings): N (reason: [brief reason])
verification_status inferred: N (list of finding IDs)
Original IDs preserved in Notes: [list]
Output: [path to _normalized.md]
```
