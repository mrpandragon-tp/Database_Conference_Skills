---
name: db-novelty-positioning
description: Position contributions against nearest prior SIGMOD/VLDB-related work and detect incremental-risk early. Use when defining contributions, writing related work, or validating novelty claims before drafting.
---

# DB Novelty Positioning

Use this skill to turn contribution claims into defensible deltas.

## Workflow

1. Load `references/novelty_rubric.md` and `references/claim_prior_template.md`.
2. Use local corpus matrices when available:
- `.references/paper-corpus/method_matrix.md`
- `.references/paper-corpus/reviewer_risk_matrix.md`
- `.references/paper-corpus/fulltext_writing_signal_matrix.md`
- `.references/paper-corpus/fulltext_reviewer_risk_matrix.md`
- `.references/distilled/novelty_patterns_fulltext.md`
3. Classify each claim type: algorithm/system/proof/evaluation.
4. Map nearest prior work and explicit differentiator.
5. Flag incremental-risk and missing support.

## Output Contract

1. `Claim Set`
2. `Nearest Prior Map`
3. `Differentiator Table`
4. `Incremental Risk`
5. `Evidence Needed`

## Rules

- Reject vague novelty wording without mechanism-level delta.
- Keep claim strength proportional to existing evidence.
