# Contributing Guide

Thanks for contributing to `Database Conference Skills (SIGMOD/VLDB)`.

This repository is designed for reusable, project-agnostic paper-production
skills. Please keep additions reproducible and reviewer-oriented.

## Contribution Scope

Good contributions:
- add a new reusable skill for the SIGMOD/VLDB writing pipeline
- improve an existing skill's workflow/output contract/rules
- add references that strengthen novelty/proof/experiment rigor
- improve distillation scripts and documentation clarity

Avoid:
- project-specific constraints hardcoded into generic skills
- venue-irrelevant hacks that reduce reproducibility

## Repository Map

- skills: `.agents/skills/`
- skill tests: `.agents/skill_tests/`
- distilled knowledge: `.references/`
- scripts: `scripts/`
- user docs: `README.md` + `docs/`

## Add a New Skill

### 1) Create skill folder

Create:
- `.agents/skills/<skill-name>/SKILL.md`
- `.agents/skills/<skill-name>/agents/openai.yaml`
- `.agents/skills/<skill-name>/references/*.md`

Naming convention:
- use kebab-case for `<skill-name>`
- keep `name` in `SKILL.md` equal to folder name

### 2) Write `SKILL.md`

Required frontmatter fields:
- `name`
- `description`

Required sections:
- workflow
- output contract
- rules

### 3) Add a regression test prompt

Create:
- `.agents/skill_tests/<skill-name>-test.md`

Suggested format:
- Input
- Expected
- Failure mode

### 4) Update skill catalog docs

Update:
- `docs/skill-catalog.md`
- `docs/workflow-playbook.md` (if execution order changes)
- `.agents/skills/README.md` (if inventory changes)

## Modify Existing Skills

When changing skill behavior:
- keep output contract backward-compatible if possible
- explain changed decision rules in skill references
- update matching test prompt in `.agents/skill_tests/`

## Regression Checks

Run from repository root.

### A) Structure checks

```bash
find .agents/skills -mindepth 1 -maxdepth 1 -type d | while read -r d; do
  test -f "$d/SKILL.md" || echo "Missing SKILL.md: $d"
  test -f "$d/agents/openai.yaml" || echo "Missing openai.yaml: $d"
done
```

### B) Frontmatter checks

```bash
rg -n "^name: " .agents/skills/*/SKILL.md
rg -n "^description: " .agents/skills/*/SKILL.md
```

### C) Skill-test coverage check

```bash
for s in .agents/skills/*; do
  n="$(basename "$s")"
  test -f ".agents/skill_tests/${n}-test.md" || echo "Missing test: $n"
done
```

### D) Distillation pipeline check (when script/data changes)

```bash
./rebuild_knowledge.sh
```

If full rebuild is not possible in your environment, run staged checks:

```bash
./scripts/refresh_paper_index.sh
./scripts/distill_topconf_patterns.py
./scripts/distill_fulltext_semantics.py
```

## Commit Convention

Use concise, intent-first messages, e.g.:
- `Add db-related-work-auditor skill and tests`
- `Refine novelty rubric and preflight checks`
- `Improve README onboarding and docs navigation`

## Pull Request Checklist

- new/changed skill has matching test prompt
- docs were updated for any behavior/inventory changes
- regression checks were run (or limitations noted)
- no project-specific hardcoding leaked into generic skills

