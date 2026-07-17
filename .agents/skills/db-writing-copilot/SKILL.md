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
- `.references/distilled/writing_patterns.md`
- `.references/distilled/good_db_paper_principles.md` as the paper-wide writing and acceptance contract.
- `.references/distilled/iterative_revision_lessons.md` for multi-round revision.
4. Draft by section goal, not sentence-level polishing first.
5. Build a reverse outline and assign one principal message to each paragraph.
6. Put the paragraph message in its topic sentence, especially in the Introduction and experiment analysis.
7. Keep terminology and the paper-level subject stable across sections.
8. Attach each major claim to an evidence pointer (figure/table/theorem).
9. Run reader-flow and comment-closure checks before finalizing each section.
10. For formal-method comments, audit every object's type, lifecycle, scope, necessity, and first-use explanation before rewriting sentences.
11. For annotated review rounds, produce a bilingual comment-response ledger and preserve the original annotated artifact.
12. When the implementation has multiple adaptive paths, state the role of each path instead of blending them into one cleaner but inaccurate story.
13. After local revisions, search the entire paper and every figure label for the same terminology, lifecycle, and proof obligations.
14. Audit every paragraph by function: advance a claim, explain a required mechanism, provide evidence, or state a boundary. Merge, move, or remove paragraphs with no necessary role.
15. Prefer simple sentences and stable vocabulary, especially for non-native English readers. Do not trade logical connectors for choppy prose.

## Output Contract

1. `Section Outline`
2. `Draft Text`
3. `Claim-Evidence Map`
4. `Clarity Risks`
5. `Paragraph Function and Global Follow-through`

## Rules

- Remove or weaken unsupported claims.
- Prefer concise, testable statements over broad rhetoric.
- Introduce the proposed artifact explicitly before expanding its components or capabilities.
- Preserve logical transitions when removing AI-like prose.
- Treat comments about notation, algorithms, or figures as possible section-wide failures, not isolated wording requests.
- Do not retain an equation, symbol, algorithm line, or figure element whose role cannot be tied to a later operation, claim, or proof.
- Do not make a learned component appear universal when some policies bypass it; accurate role separation is stronger than inflated mechanism coverage.
- Do not answer imagined objections in the paper with phrases such as "we do not claim." State the supported claim and limitation directly.
- Attach citations to the exact method, dataset, benchmark, or factual statement they support.
