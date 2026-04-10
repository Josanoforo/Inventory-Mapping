# Research Directions Protocol

Methodology for segmenting deep research into directions and shards. Independent of any specific research goal or downstream pipeline. Produces source-anchored, structurally comparable findings suitable for any structured processing stage.

This protocol exists because:
- Broad research prompts produce broad, incomparable outputs.
- Large prompts fail delivery in deep research tools (empty returns, timeouts, truncation).
- Cross-comparing unstructured outputs across subjects is impossible after the fact.

Directions force pre-defined scope. Shards force delivery to stay within render limits.

---

## 1. Direction

A direction is one bounded research question within a topic, with its own:
- scope statement
- allowed source types (closed list)
- unit of observation
- time window (or explicit "no window")
- exclusions

Directions are **angles of attack** on a topic, not topics themselves. Two directions can cover the same topic from different source-type perspectives (e.g., "fees as stated by the platform" vs "fees as described by third parties").

### Good directions
- Mutually distinguishable by source type or unit of observation
- Non-overlapping: a finding belongs to exactly one direction
- Individually executable without depending on other directions
- Boundable: you can write the allowed source types and unit of observation before running

### Bad directions
- "Everything about X" — no boundary
- "Opportunities in Y" — interpretive, not observational
- "Pros and cons of Z" — demands synthesis
- "What should we do about W" — advisory, not research

If you cannot write the direction's allowed source types and unit of observation in one sitting, the direction is not ready.

---

## 2. Shard

A shard is one execution unit: **one subject × one direction**.

Example: 7 subjects × 5 directions = 35 shards.

### When to shard
- Single-execution prompts fail delivery (empty returns, timeouts, truncation)
- Agent output mixes subjects when you wanted them separated
- Cross-contamination between subjects leaks into the output
- Output too large for single-pass human review

### Shard-local rule (critical)
Each shard runs in isolation. The agent executing a shard must not:
- Reference prior shards or assume their context
- Compare the subject to other subjects
- Synthesize across shards
- Produce cross-subject observations

Cross-shard comparison happens downstream, never inside a shard execution.

---

## 3. Shard prompt structure

Every shard prompt must declare all of the following:

1. **Subject** — the one thing being researched (one platform, one entity, one product)
2. **Direction** — the one direction, with its scope statement
3. **Language** — search language
4. **Time window** — explicit or "no window"
5. **Allowed source_type** — closed list
6. **Unit of observation** — what counts as one finding
7. **Qualifiers to preserve** — timeframes, units, scope restrictions, thresholds
8. **What to skip** — explicit exclusions
9. **Delivery format** — 4-part structure (Section 4)
10. **Scope reminder** — explicit statement that this shard does not cover other subjects or directions

Template in Section 9.

---

## 4. Delivery contract

Every shard returns exactly four parts:

- **Part 1 — Clean findings** — `direct_verified` only
- **Part 2 — Provisional findings** — `blocked_url_index_verified` only
- **Part 3 — Pattern candidates (sealed)** — any cross-source synthesis that leaked despite the rules; `None.` if clean
- **Part 4 — Could not verify** — verification failed, include what was tried; `None.` if clean

No shard returns fewer than four parts. Empty parts are declared as `None.`, not omitted.

---

## 5. Verification states

Every finding declares exactly one:

- **`direct_verified`** — URL directly accessible, claim directly visible on the page, snippet directly confirmed
- **`blocked_url_index_verified`** — URL blocked; exact text recovered from a search engine cache, indexed snippet, archive snapshot, or mirror of the same URL
- **`could_not_verify`** — verification failed materially

### Default stance: conservative
When in doubt, downgrade. Never upgrade.
- Unsure clean/provisional → provisional
- Unsure provisional/failed → failed
- Unsure URL is specific → failed
- Unsure source_type fits → `unknown`

---

## 6. Finding integrity

Two integrity rules apply to every finding: single-source integrity (the finding is anchored to exactly one speaker/account/source) and What-snippet fidelity (the finding's "What" field is fully supported by the cited snippet, nothing added).

### 6.1 Single-source integrity

A finding fails if it contains multiple source identities, multiple URLs, or quotes from more than one source.

**Multi-speaker splitting.**
One source page may still contain multiple distinct voices. If a page contains multiple commenters, reviewers, forum participants, quoted sellers, or clearly separate speakers/accounts, each distinct speaker/account must be split into a separate finding. Same page is not the same observation when the speakers are different.

### 6.2 Edge cases for single-source

**Journalism interviews — single-source.**
A journalist reporting a direct quote they obtained in interview counts as single-source. The journalist is the primary capture. The finding is about what the article says; the quote is part of that article. Classify `source_type: article` or `interview`.

**Secondary retelling — not single-source.**
A blog or article summarizing what another post, tweet, or source said is NOT single-source. Default to Part 4 unless the original source was also directly accessed and quoted.

**Intermediary verification — not valid.**
Using a third-party article to verify a cited URL the agent could not access directly is NOT valid indirect access. This is two identities (the cited URL + the intermediary). Default to Part 4. Do not classify as provisional.

**URL mirrors — valid indirect access.**
A mirror of the same URL (e.g., libredd.it for reddit.com, archive.org snapshots, Google cache of the same URL) counts as equivalent indirect access. Classify as `blocked_url_index_verified`. Note the mirror in the Notes field.

**Ambiguous URL — default to Part 4.**
If the specific URL could not be determined (e.g., only a subreddit-level URL instead of a thread URL, only a domain instead of a page), default to Part 4 regardless of whether the text is recoverable.

### 6.3 What-snippet fidelity

The "What" field of a finding must be fully supported by the cited Verbatim snippet.

Do not add:
- countries the snippet does not mention
- rates the snippet does not state
- qualifiers (timeframes, thresholds, units) absent from the snippet
- numbers the snippet does not contain
- inferences ("this probably means X") the snippet does not make

The snippet is the single source of truth for the What. If the What says more than the snippet, the What is contaminated by inference. Rewrite the What to match the snippet exactly, or move the finding to Part 4 if the claim cannot be supported by any verbatim text.

---

## 7. Failure modes and recovery

| Failure | Recovery |
|---|---|
| Delivery empty / timeout / truncated | Re-split the failing shard. If subject × direction fails, split direction into sub-directions and re-run. |
| Two consecutive delivery failures on the same shard | Execute manually instead of via deep research, or drop the shard and document the gap. |
| Agent synthesizes across shards | Shard-local rule not enforced. Re-prompt with explicit reminder at top of shard prompt. |
| Agent interprets, recommends, or ranks | Prompt did not forbid interpretation explicitly. Add "Do not interpret. Do not recommend. Do not rank." at top. |
| Agent treats third-party as primary source | Reinforce Section 6 edge cases in the prompt. |
| Agent adds inferences to What field not present in snippet | Remind Section 6.3: What must be fully supported by snippet. Rewrite What to match snippet. |
| Agent conflates multiple speakers on same page | Remind Section 6.1: multi-speaker splitting. Each distinct speaker = separate finding. |
| Most findings in Provisional, few in Clean | Expected when the source domain blocks direct fetch. Resolve at batch close via human verification. |
| Source_type defaulted to convenience | Tighten taxonomy guidance or add `unknown` fallback instruction. |

---

## 8. Batch close

After running N shards for one subject:

1. Count findings per part.
2. List all Part 2 (provisional) findings for human review. Each must be:
   - **Promoted to Clean** — after direct human verification
   - **Quarantined** — held out of downstream, not killed
   - **Downgraded to Could not verify** — if verification attempt failed
3. List all Part 4 (could not verify) findings as explicit coverage gaps.
4. Do not auto-merge shards into a combined document. Downstream processing handles merging, deduplication, and pattern detection.

**No provisional finding passes downstream without human resolution.** Default if unresolved at batch close: Quarantine.

---

## 9. Minimal shard prompt template

```
# Shard — [SUBJECT] × [DIRECTION NAME]

## Scope
[SUBJECT] only. [DIRECTION NAME] only. No other subjects, no other directions.
No references to prior shards. No cross-subject comparisons.

## Language
[LANGUAGE]

## Time window
[Explicit window with start–end dates, or "No window — current state only"]

## Direction statement
[One sentence: what you are looking for and why it matters as a distinct angle]

## Allowed source_type
[Closed list, e.g., platform_doc, pricing_page, help_center, policy_page]

## Unit of observation
[What counts as one finding — e.g., "one fee type × one tier × one qualifier set"]

## Where to look first
[Known URLs or domains, optional but reduces search variance]

## Qualifiers to preserve
[List — timeframes, units, thresholds, scope restrictions]

## Finding ID convention

Each finding declares an ID at the section header. Use one of three patterns based on which Part the finding belongs to:

- Part 1 (clean / direct_verified): `F-NN` where NN is sequential starting at 01 (e.g., F-01, F-02, F-03)
- Part 2 (provisional / blocked_url_index_verified): `F-PNN` where NN is sequential starting at 01 (e.g., F-P01, F-P02)
- Part 4 (could not verify / out-of-scope): `F-XNN` where NN is sequential starting at 01 (e.g., F-X01, F-X02)

Sequence is per-Part, not global across Parts. Each Part starts at 01.

Header format: `### F-NN` for Part 1 and Part 2 findings. `### F-XNN: <subject>` for Part 4 items (Part 4 items include the subject in the header line, separated by colon, because Part 4 items do not have a verbatim snippet to identify them by content).

Part 3 (pattern candidates) does not introduce new IDs. It references findings from Parts 1 and 2 by their existing IDs.

Global uniqueness across shards is achieved at processing time by combining `shard_id` (derived from the shard filename) with `finding_id` (from the header). The downstream parser stores `shard_id` and `finding_id` as separate fields, so within-Part sequencing inside a single shard is sufficient.

## Filesystem convention for shard inputs

Shards are organized by source tool in the input directory:

- `input/data_gathering/shards/deep_search/` — shards executed via deep research tools
- `input/data_gathering/shards/gpt_custom/` — shards executed via custom GPT

The parent directory is the structural declaration of source. The parser uses the parent directory name to populate the `source_tool` field in every output JSON. The same value flows downstream to `retrieval_method` in Source Packet.

Valid values match the `retrieval_method` enum in `upstream/source-intake/schemas/source_packet.schema.json`: `deep_search`, `gpt_custom`, plus the existing values for other retrieval methods.

A shard placed directly in `input/data_gathering/shards/` without a sub-directory is malformed. The parser will emit a warning and tag the source as `unknown`.

## What to skip
[Explicit exclusions — paid reviews, roundups, tutorials, synthesis blogs, etc.]

## Verification handling
- Direct access + direct confirmation = Clean (direct_verified)
- Blocked direct access + exact text from cache/mirror/archive of same URL = Provisional (blocked_url_index_verified)
- Anything else = Could not verify

Follow the single-source integrity rules (Rule 16) including edge cases for journalism, retelling, intermediary verification, mirrors, and ambiguous URLs.

## Delivery
Return findings in four parts:
- Part 1 — Clean findings (direct_verified)
- Part 2 — Provisional findings (blocked_url_index_verified)
- Part 3 — Pattern candidates (sealed) — `None.` if clean
- Part 4 — Could not verify — `None.` if clean

## Scope reminder
This shard is [SUBJECT] × [DIRECTION NAME] only. Do not include findings from other subjects or directions in this output.
```

---

## 10. What this protocol does not do

- Does not define how to process shard outputs downstream
- Does not define how to compare findings across shards
- Does not define how to handle contradictions between findings
- Does not define interpretation, ranking, or prioritization
- Does not define how to derive insights, opportunities, or recommendations

All of those happen in downstream stages. The purpose of this protocol is to produce clean, source-anchored, structurally comparable inputs for those stages — nothing more.
