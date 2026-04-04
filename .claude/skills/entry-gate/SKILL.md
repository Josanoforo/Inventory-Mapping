# Entry Gate — Skill

Read `modules/01_entry_gate.md` before executing.

## Steps

1. List all files in `input/` matching `signal_cards_round_*.md`. Confirm 10 files.
2. For each file, parse cards by `---` delimiter containing `**SC-R`.
3. Count cards per round. Record totals.
4. Run the 5 checks from the module on every card.
5. For Check 2 (no strategic interpretation): scan the Observation field for card-level interpretation. Words like "should", "must" inside quoted source material are NOT violations.
6. Write `working/entry_gate/entry_gate_report.json` with:
   ```json
   {
     "status": "pass" | "fail",
     "total_cards": N,
     "rounds": [{"round": N, "cards": N}],
     "checks": [
       {"check": "discrete_cards", "passed": bool, "violations": []},
       {"check": "no_interpretation", "passed": bool, "violations": []},
       {"check": "no_meta_observations", "passed": bool, "violations": []},
       {"check": "evidence_preserved", "passed": bool, "violations": []},
       {"check": "ids_traceable", "passed": bool, "violations": []}
     ]
   }
   ```
7. If status is `fail`, stop and report. Do not continue pipeline.
