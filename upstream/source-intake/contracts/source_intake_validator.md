# Source Intake Validator

## Purpose

Validate each Source Packet before it can pass to Data Extraction.

The validator does **not** decide whether the source is important.
The validator does **not** decide whether the source contains a real signal.
The validator does **not** compare sources against each other.
The validator does **not** produce market conclusions.

Its job is narrower:

- verify that one packet corresponds to one source
- verify that local snippets are present
- verify that traceability is usable
- verify that the packet is not already a cross-source synthesis
- verify that tentative fields remain tentative, not interpretive
- verify that uncertainties are preserved instead of flattened
- decide whether the packet should pass, pass with flags, go to rework, move to parking lot, or be rejected

---

## Inputs

Read:
- one `Source Packet`

Optional references:
- `source_packet.schema.json`
- `Source Intake Contract v0.1`

---

## Output

Produce one validation result per Source Packet.

Allowed validation statuses:
- `pass`
- `pass_with_flags`
- `rework`
- `parking_lot`
- `reject`

Allowed check statuses:
- `pass`
- `flag`
- `fail`
- `not_applicable`

---

## Validator stance

Be conservative.

A Source Packet is useful only if Data Extraction can work on it **without reconstructing the source from a cooked summary**.

Prefer:
- explicit uncertainty
- one-source purity
- local snippets
- narrow operational notes
- parking lot when one recoverable piece is missing

Over:
- summary elegance
- repaired interpretation
- “close enough”
- importing cross-source patterns into intake

---

## Core validation principle

A good Source Packet should let Data Extraction answer:

1. what source this is
2. where it came from
3. what local snippets are available
4. where those snippets live inside the source
5. what is tentatively visible
6. what remains uncertain

If Data Extraction would need to infer too much, the packet is not ready.

---

## Validation checks

### 1. Single-source boundary

#### Question
Does this packet represent exactly one source?

#### Pass if
- one source only is represented
- all snippets clearly belong to that source
- there is no blended material from another source

#### Flag if
- source identity is stable, but one snippet needs confirmation that it belongs to the same source page/section

#### Fail if
- multiple sources are fused
- the packet carries a “summary of several sources”
- snippets come from different URLs/files/documents

#### Typical failure codes
- `multiple_sources_fused`

#### Edge case: voice_container_mismatch

A page that is directly fetchable may carry claims attributed to a speaker who is not the container's own voice — for example, a blog post paraphrasing a Reddit user's experience without linking to that user's original post.

This is an edge case of the single-source boundary check. The container is one source, but the attributed claim belongs to a different speaker whose words are not actually in the snippet.

**Routing — two paths:**

**Path 1: `pass_with_flags`**

Use when the packet can be reclassified so that the claim is attributed to the container author reporting about the external speaker, rather than attributed to the external speaker directly. The packet continues downstream. Data Extraction must then assign `evidence_role: reported_event` rather than `direct_claim`. This preserves the signal as weaker-than-direct evidence without discarding it.

Example: a blog post says "Reddit user u/foo reported that X" with a link to u/foo's post. The packet is reclassifiable — the container is reporting on the external speaker.

**Path 2: `reject`**

Use when the paraphrase is so weak that it cannot support even a `reported_event` classification. The criterion: the packet cannot anchor any verifiable claim about any specific speaker, even as a reported event.

Example: a blog post says "some sellers on Reddit complain that X" with no link and no named speaker. No verifiable claim can be anchored.

#### Typical failure codes
- `voice_container_mismatch`

---

### 2. Source metadata

#### Question
Is the source itself identifiable enough to be worked on later?

#### Pass if
- `source_title` exists
- `source_type` is plausible
- `source_ref` is usable
- date/author are preserved if available

#### Flag if
- some metadata is missing but the packet is still workable
- source type is tentative but not destructive

#### Fail if
- source reference is missing
- source type is too unclear to safely interpret later
- the source cannot be reliably identified

#### Typical failure codes
- `source_metadata_missing`
- `source_ref_missing`
- `source_type_unclear`

---

### 3. Traceability

#### Question
Can I get back to the source and to the relevant local location?

#### Pass if
- `source_ref` is usable
- every snippet has a `location_pointer`
- pointers are specific enough for later reopening

#### Flag if
- traceability exists but is coarse
- location pointer reaches the page/doc but not the exact local section

#### Fail if
- traceability is weak to the point of blocking reopening
- snippets cannot be traced back to a concrete location

#### Typical failure codes
- `traceability_weak`
- `location_pointer_missing`

---

### 4. Local snippets present

#### Question
Does the packet contain real source-local snippets, not just a paraphrase?

#### Pass if
- there is at least one useful local snippet
- the snippet preserves actual wording from the source

#### Flag if
- the snippet is useful but slightly too compressed
- there is only one snippet and it is minimally sufficient

#### Fail if
- there are no snippets
- the packet is mostly a summary with no source-local wording
- the packet only contains a high-level claim about the source

#### Typical failure codes
- `no_local_snippets`
- `packet_too_cooked_for_extraction`

---

### 5. Snippet context sufficiency

#### Question
Does each snippet include enough local context to avoid distortion?

#### Pass if
- `context_before` / `context_after` is sufficient where needed
- the snippet can be interpreted locally without heavy reconstruction

#### Flag if
- the snippet is probably usable but should be reopened if selected for sensitive downstream use

#### Fail if
- missing context would materially change reading
- qualifiers or scope are likely lost because the snippet was clipped too tightly

#### Typical failure codes
- `snippet_context_missing`

---

### 6. No cross-source summary carried over

#### Question
Did the packet avoid importing a deep-search synthesis into source intake?

#### Pass if
- the packet remains source-local
- it does not say “multiple sources indicate” or equivalent
- it does not present a pattern across sources as packet content

#### Fail if
- the packet carries cross-source summary language
- the packet uses another source to explain the current one
- the packet is already framed as contradiction, asymmetry, friction, or market pattern

#### Typical failure codes
- `cross_source_summary_carried_over`
- `packet_too_cooked_for_extraction`

---

### 7. Possible fields remain non-interpretive

#### Question
Are `possible_subjects`, `possible_metric_types`, and other tentative helpers still tentative rather than downstream interpretation?

#### Pass if
- they are narrow, local, and plausibly useful for Data Extraction
- they do not lock in a pattern or meaning prematurely

#### Flag if
- one tentative field is a bit broad but recoverable

#### Fail if
- a tentative field is really an interpretation
- it already encodes contradiction, friction, asymmetry, importance, or opportunity

#### Good examples
- `Gumroad Discover activation requirement`
- `Creative Market seller commission base rate`
- `PayPal as checkout payment method in Gumroad`

#### Bad examples
- `Gumroad chicken-and-egg problem`
- `evidence of marketplace asymmetry`
- `business opportunity in seller acquisition`

#### Typical failure codes
- `possible_subject_overinterpreted`
- `possible_metric_overinterpreted`
- `packet_too_cooked_for_extraction`

---

### 8. Uncertainties preserved

#### Question
Did the packet preserve visible ambiguity instead of flattening it?

#### Pass if
- real uncertainty is made explicit
- the packet does not pretend certainty it does not have

#### Flag if
- the right uncertainty exists but is too coarsely described

#### Fail if
- visible ambiguity from the source is absent
- the packet chooses one reading without basis
- deep search compression erased uncertainty

#### Typical failure codes
- `uncertainty_hidden`

---

### 9. Priority assignment reasonable

#### Question
Is `priority_for_source_first` assigned on sensible grounds?

#### Pass if
- `high` is used for sensitive, contradictory-looking, policy, pricing, payout, requirement, or quantitative claims
- `medium` is used for promising but not critical material
- `low` is used for contextual or peripheral material

#### Flag if
- priority seems arguable but not harmful

#### Fail if
- priority is clearly mismatched and would distort downstream effort badly

#### Typical failure codes
None required by default. Use notes unless the mismatch is severe enough to justify rework.

---

## Decision rules

### Use `pass` when
- the packet is source-pure
- snippets are present
- traceability is good
- no cross-source synthesis is carried over
- tentative fields remain tentative
- uncertainties are preserved

### Use `pass_with_flags` when
- the packet is usable for Data Extraction
- but one or more non-fatal limitations remain visible

Typical examples:
- source date unclear
- snippet context slightly thin
- traceability only partial but still usable
- one ambiguity remains explicit

### Use `rework` when
- the packet contains real value
- but structure must be repaired before Data Extraction

Typical rework-worthy problems:
- snippets present but context too thin
- one source but metadata weak
- possible subjects too broad
- uncertainty not well surfaced but recoverable
- one location pointer missing but source is otherwise recoverable

### Use `parking_lot` when
- the packet seems useful
- but one recoverable missing piece blocks safe downstream use
- and that missing piece can be resolved by a bounded follow-up query or reopening

Good parking-lot cases:
- missing visible date on otherwise strong policy page
- ambiguous function that needs source reopen
- snippet useful but too clipped, with easy source recovery

Bad parking-lot cases:
- multi-source synthesis blob
- source not traceable
- packet already too cooked to salvage

### Use `reject` when
- multiple sources are fused
- no local snippets are present
- traceability is too weak
- packet is mostly a cooked summary
- tentative fields are really interpretations
- ambiguity was hidden in a way that changes downstream behavior

---

## Failure severity guide

### Usually `reject`
- `multiple_sources_fused`
- `cross_source_summary_carried_over`
- `packet_too_cooked_for_extraction`

### Usually `rework`
- `source_metadata_missing`
- `snippet_context_missing`
- `possible_subject_overinterpreted`
- `possible_metric_overinterpreted`
- `uncertainty_hidden`
- `location_pointer_missing`

### Often `parking_lot`
- `traceability_weak` when recoverable
- `source_date_unclear` style ambiguity when the rest is strong
- `snippet_needs_reopen` style uncertainty

---

## Notes discipline

Notes may explain:
- what failed
- why it failed
- what recovery path exists

Notes must not:
- interpret the market
- compare this source to others
- name a tension
- suggest an opportunity
- summarize “what this means overall”

---

## Rework instruction discipline

Good:
- `Add one more local snippet showing the condition wording`
- `Restore exact location pointer for snippet 2`
- `Narrow possible_subjects to local functional subject`
- `Remove cross-source summary sentence from raw_search_context`

Bad:
- `Make it better`
- `Needs more clarity`
- `Too broad`
- `Improve quality`

---

## Example evaluation patterns

### Example 1
Packet contains:
- one blog URL
- one snippet
- one location pointer
- possible subject: `PayPal as checkout payment method in Gumroad`
- uncertainty: `checkout_vs_payout_ambiguity`

Likely result:
- `pass_with_flags`

Reason:
Packet is source-local and usable, but ambiguity remains visible.

### Example 2
Packet contains:
- three snippets from two blogs and one forum
- one note saying “these sources suggest Gumroad lacks discoverability”

Likely result:
- `reject`

Reason:
This is not source intake anymore. It is already cross-source synthesis.

### Example 3
Packet contains:
- a pricing page
- one clean snippet
- no date
- source_ref usable
- strong local subject

Likely result:
- `parking_lot` or `pass_with_flags`

Reason:
Depends on whether the missing date materially blocks Data Extraction or can be safely carried as uncertainty.

---

## Global rule

If the packet already sounds like something that could appear in Inventory Mapping, it is too cooked for Source Intake.

Source Intake exists to hand Data Extraction **source-local material with preserved boundaries**.
It does not exist to hand it miniature findings.
