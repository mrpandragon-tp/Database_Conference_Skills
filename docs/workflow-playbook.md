# Workflow Playbook

## Objective

Convert a project with code + experimental outputs into a
submission-ready SIGMOD/VLDB manuscript with a repeatable pipeline.

## Cross-phase acceptance gate

At every phase, use `.references/distilled/good_db_paper_principles.md` and preserve the same chain:

`important problem -> complete artifact -> mechanism -> guarantee -> evidence -> boundary`

Do not advance because the draft is polished or reaches the page limit. Advance when the artifacts needed by the next arrow exist.

## Phase 1: Intake and Scope

- run `db-paper-orchestrator`
- define paper objective, target claim scope, deliverables
- freeze milestone checkpoints for method, experiments, writing, submission

Gate to pass:
- clear phase plan exists
- required artifacts per phase are explicit

## Phase 2: Novelty and Positioning

- run `db-novelty-positioning`
- produce claim-prior-delta mapping
- classify claim types (system/algorithm/proof/evaluation)

Gate to pass:
- each top claim has a nearest prior and measurable differentiator
- no vague novelty wording without evidence plan

## Phase 3: Method + Proof Backbone

- run `db-writing-copilot` for method section skeleton
- run `db-method-proof-check` for theorem/assumption/dependency closure

Gate to pass:
- theorem assumptions are explicit and consistent
- proof obligations are complete for central claims

## Phase 4: Evidence Build and Audit

- run `db-experiment-evidence-auditor`
- verify baseline fairness, protocol consistency, stress-test coverage
- close claim-evidence gaps before narrative polishing

Gate to pass:
- strongest baselines are fairly configured
- central claims have matched quantitative support

## Phase 5: Figures and Reader Narrative

- run `db-figure-design`
- align figures with claim order and reviewer reading order

Gate to pass:
- each key claim maps to a figure/table anchor
- figure captions and axis choices support decision-relevant reading

## Phase 6: Reviewer Simulation and Final Format

- run `db-reader-reviewer-preflight`
- fix major/fatal reviewer concerns first
- run `db-format-finish` for final style and layout checks

Gate to pass:
- no unresolved fatal concerns
- the ten-question strong-paper acceptance test can be answered from the manuscript
- manuscript passes final pre-submission checklist

