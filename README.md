# Database Conference Skills (SIGMOD/VLDB)

Language:
- English (this file)
- 中文说明: [README.zh-CN.md](./README.zh-CN.md)

Project-agnostic skill pack for turning a database research project from
code/experiments into a submission-ready SIGMOD/VLDB paper.

This repository packages:
- a reusable skill system (`.agents/skills`)
- distilled knowledge from target-paper corpora (`.references`)
- rebuild scripts for continuous knowledge refresh (`scripts/`)

## Why This Repo

The goal is not one-off polishing for a single paper. It is to build a
repeatable writing-and-review pipeline reusable across projects.

Current distillation depth:
- target papers: 81
- fulltext semantic profiles built: 80
- per-paper outputs include novelty/evidence/proof risk signals

See [distillation_depth.md](./distillation_depth.md).

## Skill Pack (v0.3)

Eight end-to-end skills:
1. `db-paper-orchestrator`
2. `db-novelty-positioning`
3. `db-writing-copilot`
4. `db-method-proof-check`
5. `db-experiment-evidence-auditor`
6. `db-figure-design`
7. `db-format-finish`
8. `db-reader-reviewer-preflight`

Skill catalog: [docs/skill-catalog.md](./docs/skill-catalog.md)

## Practical Usage Examples

If you liked example-driven repositories, start here:
- usage recipes and copyable invocation patterns:
  [docs/usage-examples.md](./docs/usage-examples.md)
- full pipeline playbook:
  [docs/workflow-playbook.md](./docs/workflow-playbook.md)

Example task patterns covered:
- from code/results to full paper workflow planning
- novelty-risk triage and claim-prior-delta rewriting
- theorem/proof closure and experiment fairness auditing
- figure planning tied to claims and reviewer questions
- final reviewer preflight + format checks

## Skill Fusion (with Other Skills)

This pack also documents how to combine with external skills (when installed):
- `research-paper-writing`, `ml-paper-writing`, `humanizer`
- `scientific-figure-making`, `canvas-design`, `pdf`

Fusion guide and guardrails:
- [docs/usage-examples.md](./docs/usage-examples.md)
- source mapping:
  [./.references/distilled/existing_skill_integration.md](./.references/distilled/existing_skill_integration.md)

## Distill New Papers into New Knowledge

You can continuously expand this knowledge base with new Zotero papers.

Quick path:
1. add papers to Zotero collections used by scripts (`ANN`, `SIGMOD/VLDB`)
2. run:

```bash
./rebuild_knowledge.sh
```

For custom collections or paths, edit:
- `scripts/refresh_paper_index.sh` (`DB_URI` + collection names)
- `scripts/distill_fulltext_semantics.py` (`DB_URI` + `ZOTERO_STORAGE`)

Detailed operational steps:
- [docs/usage-examples.md](./docs/usage-examples.md)

## Quick Start

### 1) Use directly from this repository

If your agent runtime can read local paths, point it to:
- skills: `.agents/skills/`
- distilled references: `.references/distilled/`
- corpus matrices: `.references/paper-corpus/`

### 2) Install into local Codex skills directory (optional)

```bash
mkdir -p ~/.codex/skills/db-topconf-paper-pack-v03
rsync -av --delete \
  /path/to/db_topconf_skill_pack_v03/ \
  ~/.codex/skills/db-topconf-paper-pack-v03/
```

## Recommended Execution Flow

1. project intake and planning -> `db-paper-orchestrator`
2. claim-prior delta mapping -> `db-novelty-positioning`
3. section drafting and claim-evidence alignment -> `db-writing-copilot`
4. theorem/assumption/complexity closure -> `db-method-proof-check`
5. baseline fairness and stress-test coverage -> `db-experiment-evidence-auditor`
6. figure story and visual consistency -> `db-figure-design`
7. reviewer simulation and fatal-risk checks -> `db-reader-reviewer-preflight`
8. final formatting and submission polish -> `db-format-finish`

## Repository Layout

```text
.
├── .agents/
│   ├── skills/            # executable skills (SKILL.md + references)
│   └── skill_tests/       # test prompts/checkpoints for each skill
├── .references/
│   ├── paper-corpus/      # matrices/profiles/reports from distillation
│   └── distilled/         # compact reusable patterns
├── scripts/               # rebuild and distillation scripts
├── docs/                  # user-facing documentation
├── rebuild_knowledge.sh   # one-command refresh pipeline
└── skill_*.md             # scope/log/gap snapshots
```

More details: [docs/repo-organization.md](./docs/repo-organization.md)

## Core Artifacts

- fulltext profile:
  `.references/paper-corpus/fulltext_semantic_profile.csv`
- fulltext distillation report:
  `.references/paper-corpus/fulltext_distillation_report.md`
- distilled novelty patterns:
  `.references/distilled/novelty_patterns_fulltext.md`
- distilled proof patterns:
  `.references/distilled/proof_patterns_fulltext.md`
- distilled experiment patterns:
  `.references/distilled/experiment_patterns_fulltext.md`

## Docs Index

- capability map: [docs/skill-catalog.md](./docs/skill-catalog.md)
- capability map (Chinese): [docs/skill-catalog.zh-CN.md](./docs/skill-catalog.zh-CN.md)
- workflow playbook: [docs/workflow-playbook.md](./docs/workflow-playbook.md)
- workflow playbook (Chinese): [docs/workflow-playbook.zh-CN.md](./docs/workflow-playbook.zh-CN.md)
- usage examples + fusion + distillation operations:
  [docs/usage-examples.md](./docs/usage-examples.md)
- usage examples + fusion + distillation operations (Chinese):
  [docs/usage-examples.zh-CN.md](./docs/usage-examples.zh-CN.md)
- contribution guide: [CONTRIBUTING.md](./CONTRIBUTING.md)
- contribution guide (Chinese): [CONTRIBUTING.zh-CN.md](./CONTRIBUTING.zh-CN.md)
- bilingual coverage list: [docs/bilingual-index.md](./docs/bilingual-index.md)

## Version Notes

- current package: v0.3
- `.agents/skills/README.md` aligned to v0.3
- remaining future gaps tracked in [skill_gap_report.md](./skill_gap_report.md)
