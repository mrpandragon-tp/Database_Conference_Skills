# Skill Catalog (v0.3)

## End-to-End Skill Map

| Skill | Primary Responsibility | Typical Inputs | Typical Outputs |
| --- | --- | --- | --- |
| `db-paper-orchestrator` | project-to-paper stage planning | project code, results, target venue | stage plan, handoff artifacts |
| `db-novelty-positioning` | claim-prior delta and incremental-risk audit | contribution claims, related work | differentiator table, risk flags |
| `db-writing-copilot` | section drafting with claim-evidence discipline | outlines, figures, result tables | structured section drafts |
| `db-method-proof-check` | theorem/proof/assumption consistency checks | method section, proof appendix | proof issue list, closure checklist |
| `db-experiment-evidence-auditor` | fairness, baseline, stress-test coverage | experiment scripts/results | evidence-gap report, repair plan |
| `db-figure-design` | figure narrative and visual quality | data tables, scripts, plot specs | figure story plan, figure QA |
| `db-format-finish` | final formatting and venue-facing polish | LaTeX/PDF draft | pre-submission formatting checklist |
| `db-reader-reviewer-preflight` | reviewer simulation and fatal-risk triage | near-final manuscript | major/fatal concern list |

## Suggested Trigger Conditions

- `db-paper-orchestrator`: start of a new paper cycle or major scope reset
- `db-novelty-positioning`: after problem framing and before deep drafting
- `db-writing-copilot`: whenever section writing starts or stalls
- `db-method-proof-check`: once theorem statements and assumptions exist
- `db-experiment-evidence-auditor`: once first full results are available
- `db-figure-design`: before camera-ready visual production
- `db-reader-reviewer-preflight`: before submission freeze
- `db-format-finish`: final pass before submission upload

## Ordering Rule

Recommended full order:
1. orchestrator
2. novelty positioning
3. writing copilot
4. method/proof check
5. experiment auditor
6. figure design
7. reviewer preflight
8. format finish

## Where Each Skill Lives

All skill definitions are under:
- `.agents/skills/<skill-name>/SKILL.md`

Supporting references for each skill are colocated in:
- `.agents/skills/<skill-name>/references/`

