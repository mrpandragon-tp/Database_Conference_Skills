---
name: db-format-finish
description: Finalize database-paper formatting and submission hygiene, including LaTeX consistency and PDF layout checks. Use at late-stage drafting when content is mostly fixed and submission quality polish is needed.
---

# DB Format Finish

Use this skill for final presentation quality and format compliance.

## Workflow

1. Load `references/format_preflight.md`, `references/latex_cleanup_checklist.md`, `references/pdf_layout_checks.md`, and `references/collaborative_latex_workflow.md` when Git/Overleaf collaboration is involved.
2. Load `.references/distilled/good_db_paper_principles.md` before making content cuts for a page limit.
3. Check structural consistency:
- section hierarchy
- references/citations consistency
- terminology consistency
4. Check visual layout:
- figure/table placement
- overflow/overlap issues
- readability in two-column format
5. Audit equations, pseudocode, and figure notation against the surrounding text.
6. Render and visually inspect every affected page.
7. Check that deferred floats do not cross the bibliography heading; use a float barrier before references when needed and verify the rendered result.
8. Produce final format fix list.

## Output Contract

1. `Format Status`
2. `Blocking Issues`
3. `Non-blocking Improvements`
4. `Final Pre-submission Checklist`

## Rules

- Do not use formatting polish to hide unresolved technical issues.
- Keep fixes minimal and deterministic at this stage.
- Preserve annotated review artifacts before recompiling.
- Verify local, shared Git, and Overleaf heads after synchronization.
- Prefer `[tb]` for ordinary single-column floats and `[t]` for double-column floats; do not force `h` as a default.
- Report main-text, reference, and appendix page boundaries separately.
- Confirm that the conclusion remains inside the main-text limit and that all main-paper floats appear before the reference list.
- Under page pressure, remove repetition, defensive prose, low-value implementation detail, and oversized floats before claim support, method completeness, or essential evidence.
