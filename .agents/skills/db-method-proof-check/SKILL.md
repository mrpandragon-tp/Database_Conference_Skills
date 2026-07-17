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
- `.references/distilled/good_db_paper_principles.md` for the executable-method and notation-budget tests.
- `.references/distilled/iterative_revision_lessons.md` for self-contained-method checks.
3. Extract theorem-like claims from target section.
4. Check assumption completeness and symbol consistency.
5. Trace each guarantee through access, verification, updates, fallback, and tie/corner cases.
6. Validate lemma-theorem dependency closure.
7. Link theorem claims to empirical cross-checks where needed.
8. Audit every formal object for type, lifecycle, scope, necessity, and implementation correspondence.
9. Explain pseudocode in execution order and verify that every state read or written is introduced before use.
10. Audit figure notation as part of the proof surface when a figure encodes an invariant, stopping rule, or data structure.
11. Build a representation map from ideal mathematics to stored values and runtime scans; prove every containment or rounding step.
12. Build a policy-role map that records which access structure, verifier, bound, and fallback each adaptive branch actually uses.
13. Compare the formal contract against source code, including equality boundaries, update cancellation, fallback triggers, and degenerate cases.
14. Match the theorem output to the implemented API and evaluated metric; a count-only operator must not inherit an unimplemented set-returning claim.
15. Require a reader-executable sequence for every core mechanism: purpose, typed state, invariant, algorithm, example, complexity, and correctness obligation.

## Output Contract

1. `Claim Inventory`
2. `Assumption Gaps`
3. `Dependency Findings`
4. `Required Rewrites`
5. `Proof Risk Summary`

## Rules

- Do not accept guarantee wording without explicit assumptions.
- Keep offline/online complexity statements separated.
- Put compact complexity results next to the corresponding algorithms and keep detailed derivations supplementary.
- Treat notation equality across prose, formulas, pseudocode, and proofs as blocking.
- Number every displayed definition, invariant, or bound that carries proof responsibility.
- Remove one-use aliases and avoid subscripts without a semantic owner, dimension, or time role.
- Separate exact verification from stopping certification and define insufficient-result and empty-set cases explicitly.
- Separate physical base structures, current logical query groups, delta state, and query-local collections.
- Do not use a verifier-internal heuristic as a group-level certification bound unless its group admissibility is stated and proved.
- A deterministic tie rule is part of the theorem: every pruning comparison and fallback must preserve it at equality.
- Reserve notation for repeated dependencies or proof obligations. Remove symbols that only rename an ordinary operation or appear once.
