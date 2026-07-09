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
3. Verify metric pairing: quality + efficiency + cost dimensions.
4. Verify baseline coverage and tuning fairness.
5. Verify stress tests (scale/update/selectivity/distributed where relevant).
6. Produce prioritized missing-experiment list.

## Output Contract

1. `Coverage Summary`
2. `Fairness Findings`
3. `Missing Experiments`
4. `Table/Figure Contract`
5. `Priority Fixes`

## Rules

- No speed-only claim without quality target.
- No major claim with appendix-only evidence.
