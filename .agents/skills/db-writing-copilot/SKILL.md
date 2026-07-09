---
name: db-writing-copilot
description: Draft and revise SIGMOD/VLDB paper sections with claim-evidence discipline and reader-oriented clarity. Use for Abstract, Introduction, Method, Experiments, Related Work, and Conclusion writing.
---

# DB Writing Copilot

Use this skill for section-level writing with strict claim-evidence alignment.

## Workflow

1. Load `references/section_blueprint.md` and `references/claim_evidence_map.md`.
2. Load fulltext-derived writing patterns when available:
- `.references/paper-corpus/fulltext_writing_signal_matrix.md`
- `.references/distilled/writing_patterns_fulltext.md`
3. Draft by section goal, not sentence-level polishing first.
4. Keep terminology stable across sections.
5. Attach each major claim to evidence pointer (figure/table/theorem).
6. Run a short reader-flow check before finalizing each section.

## Output Contract

1. `Section Outline`
2. `Draft Text`
3. `Claim-Evidence Map`
4. `Clarity Risks`

## Rules

- Remove or weaken unsupported claims.
- Prefer concise, testable statements over broad rhetoric.
