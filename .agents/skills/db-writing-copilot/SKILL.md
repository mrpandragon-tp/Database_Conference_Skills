---
name: db-writing-copilot
description: Draft and revise SIGMOD/VLDB paper sections with claim-evidence discipline and reader-oriented clarity. Use for Abstract, Introduction, Method, Experiments, Related Work, and Conclusion writing.
---

# DB Writing Copilot

Use this skill for section-level writing with strict claim-evidence alignment.

## Workflow

1. Load `references/section_blueprint.md` and `references/claim_evidence_map.md`.
2. For advisor/reviewer comments or annotated PDFs, load `references/advisor_comment_revision.md`.
3. Load fulltext-derived writing patterns when available:
- `.references/paper-corpus/fulltext_writing_signal_matrix.md`
- `.references/distilled/writing_patterns_fulltext.md`
- `.references/distilled/iterative_revision_lessons.md` for multi-round revision.
4. Draft by section goal, not sentence-level polishing first.
5. Build a reverse outline and assign one principal message to each paragraph.
6. Put the paragraph message in its topic sentence, especially in the Introduction and experiment analysis.
7. Keep terminology and the paper-level subject stable across sections.
8. Attach each major claim to an evidence pointer (figure/table/theorem).
9. Run reader-flow and comment-closure checks before finalizing each section.

## Output Contract

1. `Section Outline`
2. `Draft Text`
3. `Claim-Evidence Map`
4. `Clarity Risks`

## Rules

- Remove or weaken unsupported claims.
- Prefer concise, testable statements over broad rhetoric.
- Introduce the proposed artifact explicitly before expanding its components or capabilities.
- Preserve logical transitions when removing AI-like prose.
