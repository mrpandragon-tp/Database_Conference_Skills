---
name: db-reader-reviewer-preflight
description: Run reader and reviewer perspective checks for SIGMOD/VLDB papers and produce a prioritized fix plan. Use before submission, after major revisions, or when preparing rebuttal strategy.
---

# DB Reader Reviewer Preflight

Use this skill to identify likely rejection points and reader confusion.

## Workflow

1. Load `references/review_rubric.md`, `references/reader_questions.md`, and `references/action_plan_template.md`.
2. Load fulltext-derived risk signals when available:
- `.references/paper-corpus/fulltext_reviewer_risk_matrix.md`
- `.references/distilled/reader_reviewer_patterns_fulltext.md`
- `.references/distilled/good_db_paper_principles.md` as the manuscript acceptance test.
- `.references/distilled/iterative_revision_lessons.md` for multi-round consistency checks.
3. Evaluate in fixed order:
- novelty clarity
- technical/proof soundness
- experiment fairness and coverage
- reproducibility signals
- narrative readability
4. Assign severity (`fatal/major/moderate/minor`).
5. Run a separate terminology/formula/pseudocode contradiction audit.
6. Produce concrete fix actions tied to artifacts.
7. Run a paragraph-function audit and the ten-question acceptance test from `good_db_paper_principles.md`.

## Output Contract

1. `Preflight Summary`
2. `Major Findings`
3. `Reader Confusion Points`
4. `Reviewer Risk Scores`
5. `Prioritized Action Plan`

## Rules

- Prioritize substantive risks over stylistic comments.
- Every major finding must map to a concrete fix artifact.
- Do not fill the report with optional word substitutions.
- Treat undefined or renamed concepts, unnecessary notation, unexplained pseudocode, and scattered learned-component descriptions as substantive reader failures.
