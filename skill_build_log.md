# Skill Build Log (v0.5)

## Strong-paper acceptance update

- Added a bilingual definition of a strong database paper, synthesizing 80 fulltext profiles and 92 advisor annotations from four revision PDFs.
- Defined one cross-phase contract: important problem, complete artifact, mechanism, guarantee, evidence, and boundary.
- Added paragraph-function, notation-budget, learned-component, executable-method, result-analysis, plain-language, local-citation, and non-defensive-writing checks.
- Routed the shared contract through all eight skills and updated their regression prompts.

## v0.4 revision-field update

- Added bilingual lessons distilled from iterative SIGMOD-style revision.
- Added an advisor-comment revision protocol with topic-sentence, paragraph-role, and comment-thread closure checks.
- Strengthened paper-identity, ablation attribution, baseline-role, formal-consistency, figure-layout, and collaborative LaTeX rules across all eight skills.
- Updated all eight regression prompts to cover the new failure modes.

## Why this version

User requested:
- project-agnostic SIGMOD/VLDB pipeline skills
- fulltext per-paper semantic parsing
- skill-pack placement in a `.codex/skills`-style directory

## Skills included

- db-paper-orchestrator
- db-novelty-positioning
- db-writing-copilot
- db-method-proof-check
- db-experiment-evidence-auditor
- db-figure-design
- db-format-finish
- db-reader-reviewer-preflight

## Knowledge build pipeline

1. `scripts/refresh_paper_index.sh` -> paper metadata index
2. `scripts/distill_topconf_patterns.py` -> metadata-level pattern matrices
3. `scripts/distill_fulltext_semantics.py` -> fulltext per-paper semantic profiles and fulltext distilled patterns

## Fulltext coverage in this run

- Target papers: 81
- Fulltext profiles: 80
- Missing: 1 paper without usable selected fulltext cache

## New fulltext outputs

- `.references/paper-corpus/fulltext_semantic_profile.csv`
- `.references/paper-corpus/fulltext_section_signal_matrix.md`
- `.references/paper-corpus/fulltext_writing_signal_matrix.md`
- `.references/paper-corpus/fulltext_proof_signal_matrix.md`
- `.references/paper-corpus/fulltext_experiment_signal_matrix.md`
- `.references/paper-corpus/fulltext_reviewer_risk_matrix.md`
- `.references/paper-corpus/fulltext_distillation_report.md`
- `.references/distilled/novelty_patterns_fulltext.md`
- `.references/distilled/proof_patterns_fulltext.md`
- `.references/distilled/experiment_patterns_fulltext.md`
- `.references/distilled/reader_reviewer_patterns_fulltext.md`

## Validation notes

- Rebuild pipeline executed successfully.
- Skill frontmatter validated (`name` + `description`).
- Optional `quick_validate.py` still depends on local Python `yaml` module.
