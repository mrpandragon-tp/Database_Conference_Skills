---
name: db-experiment-evidence-auditor
description: Design and audit SIGMOD/VLDB experiment evidence with fairness and coverage checks. Use when planning experiments, writing experiment sections, or validating whether claims are sufficiently supported.
---

# DB Experiment Evidence Auditor

Use this skill to enforce strong evidence quality.

## Workflow

1. Load `references/experiment_checklist.md`, `references/baseline_fairness.md`, and `references/result_table_contract.md`.
2. Load fulltext-derived experiment signals when available:
- `.references/paper-corpus/fulltext_experiment_signal_matrix.md`
- `.references/distilled/experiment_patterns_fulltext.md`
- `.references/distilled/good_db_paper_principles.md` for claim-evidence closure and result-analysis rules.
- `.references/distilled/iterative_revision_lessons.md` for evidence-attribution checks.
3. Verify metric pairing: quality + efficiency + cost dimensions.
4. Verify baseline coverage and tuning fairness.
5. Verify one consistent aggregation policy per metric family.
6. Verify that ablations isolate the claimed algorithmic or learned contribution from systems engineering.
7. Verify stress tests (scale/update/selectivity/distributed where relevant).
8. Produce prioritized missing-experiment list.
9. Require each result paragraph to follow `observation -> mechanism -> condition -> claim`; flag number-only narration and unsupported causal explanations.

## Output Contract

1. `Coverage Summary`
2. `Fairness Findings`
3. `Missing Experiments`
4. `Table/Figure Contract`
5. `Priority Fixes`

## Rules

- No speed-only claim without quality target.
- No major claim with appendix-only evidence.
- Do not treat every baseline as serving the same role.
- Do not accept mixed mean/geomean/median reporting without a stated rationale.
- Do not let repeated plots substitute for one integrated answer to the research question.
- State each baseline's role before interpreting wins or losses.
