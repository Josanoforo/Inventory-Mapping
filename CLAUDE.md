DSC Pipeline — Project
What this is
Decision System Calibration pipeline for digital product design.
One repo, multiple phases (0–8). Currently active: Phase 0 through Phase 3.
Phases 4–8 have blueprints but no repo implementation yet.
The system assigns who does what — human or AI — at every phase and transition.
AI executes where it has advantage. Human directs, interprets, and decides.
The structure scales: early phases default to speed; late phases default to caution.
Active phase scoping
Not all phases are built yet. When working in the repo, identify which phase
is active before reading files. Only load the relevant phase's contracts,
modules, schemas, and skills.
Phase	Status	Location
00 Data Gathering	Implemented	phases/00-data-gathering/
01 Source Intake + Data Extraction	Implemented	phases/01-source-intake/
02 Signal Extraction	Implemented	phases/02-signal-extraction/
03 Inventory Mapping	Implemented	phases/03-inventory-mapping/
04 Design Thinking	Placeholder	phases/04-design-thinking/
05 Concept Design	Placeholder	phases/05-concept-design/
06 Selector	Placeholder	phases/06-selector/
07 Expression	Placeholder	phases/07-expression/
08 Expression Research	Placeholder	phases/08-expression-research/
Pipeline flow
```
Phase 0: Data Gathering (shards → findings)
    ↓
Phase 1: Source Intake + Data Extraction (findings → source packets → extraction records)
    ↓
Phase 2: Signal Extraction (extraction records → signal cards)
    ↓
Phase 3: Inventory Mapping (signal cards → tension candidates)
    ↓
Phase 4–8: Not yet in repo (blueprints in project knowledge)
```
Quick navigation — Phase 3 (Inventory Mapping)
This is the most developed phase. Here's the full map:
Step	Module	Skill	Reads from	Writes to
1. Entry Gate	phases/03-inventory-mapping/modules/01_entry_gate.md	entry-gate	input/signal_cards_round_*.md	working/entry_gate/
2. Splitter	phases/03-inventory-mapping/modules/02_splitter.md	split-cards	(entry gate output)	working/split/
3. Indexer	phases/03-inventory-mapping/modules/03_indexer.md	index-cards	(split output)	working/index/card_index.jsonl
4. Scanner	phases/03-inventory-mapping/modules/04_scanner.md	scan-asymmetries, scan-co-occurrences, scan-contradictions, scan-frictions, scan-gaps, scan-lexical-overlap, scan-opposite-directions	working/index/	working/scans/*.json
5. Builder	phases/03-inventory-mapping/modules/05_candidate_builder.md	build-candidate	working/scans/	output/tension_candidates/
6. Validator	phases/03-inventory-mapping/modules/06_validator.md	validate-candidate	output/tension_candidates/	output/tension_candidates/ (validated)
Quick navigation — upstream phases
Phase	Converter skill	Reads from	Writes to
01 Source Intake	p1-convert-findings	working/source_intake/skeleton_batches/	working/source_intake/packets/
01 Data Extraction	p1-extract-records	working/data_extraction/skeleton_batches/	working/data_extraction/records/
02 Signal Extraction	p2-extract-signals	working/signal_extraction/skeleton_batches/	working/signal_extraction/cards/

## Branch state verification

Branch state is read from verified `origin`, never from a local view or from
the GitHub UI. Any claim about what a branch contains — including "this branch
exists" — must be backed by a command run against `origin` after a fresh fetch.

Known instances of this failure, not an exhaustive list:

- A local view of `origin/*` goes stale silently. Run `git fetch origin --prune`
  before reading any branch state, including your own.
- A branch name can exist without existing in `origin`. The harness assigns
  branch names to sessions that never push, and the relay does not remove them.
  Confirm with `git log -1 origin/<branch>`; a name in a list, a UI row, or a
  prior handoff is not evidence the branch is real.
- The Ahead/Behind columns describe a comparison whose base may not be the one
  you assume. Verify divergence with `git log` against an explicit `origin/main`
  SHA rather than the displayed counts.
- A precondition is fixed on the property that matters, not on an identifier.
  A reference SHA is verified by checking it is an ancestor of `origin/main`
  (`git merge-base --is-ancestor`) plus a diff scoped to the relevant paths —
  not by equality against HEAD, which advances on its own with automatic
  snapshots. A branch name is never a precondition; when the task assigns
  "whatever branch the harness gives you, branched from `origin/main`", that
  is the condition to satisfy, not a name to match. Three tasks stalled on
  preconditions fixed on identifiers instead of on the actual condition.

When a check contradicts a record, the check wins and the record gets corrected.

Authority hierarchy
`phases/03-inventory-mapping/reference/protocol_canonical.md` — the canon for IM. Overrides everything within Phase 3.
`pipeline_vocabulary.yaml` — canonical enum registry for all phases. Overrides schema and contract enum definitions.
`phases/*/modules/*.md` and `phases/*/contracts/*.md` — normative specs per phase. Override skills.
`.claude/skills/*/SKILL.md` — executable routines. Follow their module or contract.
If a skill contradicts its module, the module wins.
If a module contradicts the canon, the canon wins.

> `Blueprint_DSC.md` define la asignación humano/IA y la estructura de fases del pipeline.
> Vive en project files, no en el repo. No se edita desde el repo ni desde sesiones de
> ejecución de fase. Divergencias entre lo que el repo hace y lo que el Blueprint dice se
> reportan al operador, no se resuelven aquí.

Scope boundaries — read ONLY when asked
`phases/` subfolders outside the active phase → irrelevant unless asked.
`working/` → mutable state. Read for diagnostics, not for understanding the process.
`agents/codex/` → recovery contracts for interrupted runs. Ignore unless resuming a failed phase.
`input/data_gathering/shards/` → raw deep_search sources. Parsed into
findings (Phase 0). Not yet processed into Signal Cards.
`output/repo_study/` → historical self-analysis. Reference only.
Global rules (apply to all phases)
Every Signal ID must be verified against `input/signal_cards_round_*.md` before inclusion.
Format: `SC-R[round]-[number]` with brief description in parentheses.
No figures without a Signal ID backing them.
No valorative adjectives in mechanical descriptions.
Allowed verbs: aparece, co-ocurre, contradice, se distribuye, no se encontró, se concentra, se separa en polos, no converge.
Forbidden language: importante, fuerte, central, revela que, demuestra que, necesidad, solución, recomendación, sugiere que.
Polo definitions in corpus terms, not absolute ranges.
Mixed units must be declared, not hidden.
Human fields are never filled by the agent.
Schemas
All intermediate and final outputs must validate against their schema:
Phase 3 schemas: `phases/03-inventory-mapping/schemas/`
Phase 1 schemas: `phases/01-source-intake/schemas/` and `phases/01-source-intake/data-extraction/schemas/`
Phase 2 schemas: `phases/02-signal-extraction/schemas/`
If output does not validate, the step has failed.
Resumability
Every step that processes batches maintains a manifest in `working/`.
If interrupted, resume from the last recorded position in the manifest.
Failure routing
Failed items route to recovery, never to discard:
Phase 1: `working/source_intake/source_intake_gpt_recovery/`
Phase 1 (extraction): `working/data_extraction/rejected_archive/`
Phase 2: `working/signal_extraction/signal_gpt_recovery/`
Reject is archived with reason, not discarded.
