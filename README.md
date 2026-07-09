# Database Conference Skills (SIGMOD/VLDB)

Project-agnostic skill pack for turning a database research project from
code/experiments into a submission-ready SIGMOD/VLDB paper.

This repository packages:
- a reusable skill system (`.agents/skills`)
- distilled knowledge from target-paper corpora (`.references`)
- rebuild scripts for continuous knowledge refresh (`scripts/`)

## Why This Repo

The goal is not one-off polishing for a single paper. It is to build a
repeatable writing-and-review pipeline you can reuse across projects.

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

Detailed catalog: [docs/skill-catalog.md](./docs/skill-catalog.md)

## Quick Start

### 1) Use the pack directly from this repo

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

Playbook: [docs/workflow-playbook.md](./docs/workflow-playbook.md)

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

## Refresh Knowledge

```bash
./rebuild_knowledge.sh
```

Equivalent staged run:
```bash
./scripts/refresh_paper_index.sh
./scripts/distill_topconf_patterns.py
./scripts/distill_fulltext_semantics.py
```

## Core Artifacts

- Fulltext profile:
  `.references/paper-corpus/fulltext_semantic_profile.csv`
- Fulltext distillation report:
  `.references/paper-corpus/fulltext_distillation_report.md`
- Distilled novelty patterns:
  `.references/distilled/novelty_patterns_fulltext.md`
- Distilled proof patterns:
  `.references/distilled/proof_patterns_fulltext.md`
- Distilled experiment patterns:
  `.references/distilled/experiment_patterns_fulltext.md`

## Version Notes

- current package: v0.3
- previous `.agents/skills/README.md` wording has been aligned to v0.3
- remaining future gaps are tracked in [skill_gap_report.md](./skill_gap_report.md)

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for:
- how to add a new skill
- how to add regression tests
- pre-merge validation checklist
