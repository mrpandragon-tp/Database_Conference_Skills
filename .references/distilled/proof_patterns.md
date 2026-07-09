# Proof Patterns for Database Papers

## Proof obligations that frequently matter
- Explicit assumptions for data model, query model, update model.
- Correctness/exactness conditions and fallback behavior.
- Closed lemma-theorem dependency chain.
- Complexity claims tied to clear computational model.

## Common proof failure modes
- Theorem wording without assumptions.
- Guarantee claim without proving corner-case handling.
- Complexity discussion that mixes offline and online costs.

## Checklist
- For each theorem-like claim: assumption list, dependency list, proof pointer, empirical cross-check pointer.
