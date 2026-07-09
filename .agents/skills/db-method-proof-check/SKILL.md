---
name: db-method-proof-check
description: Write and audit method formalization and mathematical proofs for database papers. Use when defining models, presenting algorithms, stating theorem-like claims, or checking correctness/complexity arguments.
---

# DB Method Proof Check

Use this skill to keep theorem-like claims formally defensible.

## Workflow

1. Load `references/proof_checklist.md`, `references/theorem_template.md`, and `references/notation_consistency.md`.
2. Load fulltext-derived proof signals when available:
- `.references/paper-corpus/fulltext_proof_signal_matrix.md`
- `.references/distilled/proof_patterns_fulltext.md`
3. Extract theorem-like claims from target section.
4. Check assumption completeness and symbol consistency.
5. Validate lemma-theorem dependency closure.
6. Link theorem claims to empirical cross-checks where needed.

## Output Contract

1. `Claim Inventory`
2. `Assumption Gaps`
3. `Dependency Findings`
4. `Required Rewrites`
5. `Proof Risk Summary`

## Rules

- Do not accept guarantee wording without explicit assumptions.
- Keep offline/online complexity statements separated.
