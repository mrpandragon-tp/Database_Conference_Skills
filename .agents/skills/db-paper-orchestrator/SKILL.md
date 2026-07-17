---
name: db-paper-orchestrator
description: Orchestrate end-to-end SIGMOD/VLDB paper production from project code and experiment outputs to near-submission draft. Use when starting a new paper project, planning milestones, or coordinating writing/proof/experiment/figure/format passes.
---

# DB Paper Orchestrator

Use this skill as the top-level controller for database-paper workflow.

## Workflow

1. Load `references/phase_checklist.md` and `references/handoff_artifacts.md`.
2. Load corpus-wide status when available:
- `.references/paper-corpus/topconf_signal_report.md`
- `.references/paper-corpus/fulltext_distillation_report.md`
- `.references/distilled/good_db_paper_principles.md` as the cross-phase acceptance contract.
- `.references/distilled/iterative_revision_lessons.md` for multi-round projects.
3. Inspect project assets: code modules, configs, run scripts, logs, result tables, figures, draft text.
4. Build a phase plan and route work to specialized skills:
- novelty: `db-novelty-positioning`
- writing: `db-writing-copilot`
- method/proof: `db-method-proof-check`
- experiments: `db-experiment-evidence-auditor`
- figures: `db-figure-design`
- formatting: `db-format-finish`
- preflight: `db-reader-reviewer-preflight`
5. Require artifact completion before phase transitions.
6. Establish the source of truth and synchronization policy for local files, Git remotes, Overleaf, and generated PDFs.
7. Keep an explicit unresolved-risk list and context-resilient project state.
8. Gate each phase on the same chain: important problem, complete artifact, mechanism, guarantee, evidence, and boundary.

## Output Contract

1. `Current Phase`
2. `Completed Artifacts`
3. `Missing Artifacts`
4. `Next Actions`
5. `Risk Register`

## Rules

- Do not polish language before novelty/evidence/proof gaps are visible.
- Do not mark pipeline complete while major reviewer risks remain unresolved.
- Do not hard-code one machine's skill paths in portable project instructions.
- Do not treat page count, prose polish, or figure count as evidence that a phase is complete.
