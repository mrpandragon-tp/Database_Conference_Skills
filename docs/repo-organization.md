# Repository Organization

## Design Principles

1. Runtime-safe layout:
   skill runtime files are colocated in `.agents/skills`.
2. Knowledge separation:
   distilled corpus artifacts are isolated in `.references`.
3. Rebuild reproducibility:
   distillation scripts are centralized under `scripts/`.
4. Reader-first discoverability:
   root `README.md` and `docs/` provide onboarding before deep files.

## Why Hidden Prefixes (`.agents`, `.references`)

The hidden-prefix layout is intentional:
- keeps runtime and large reference materials separated from user docs
- reduces accidental edits in core skill internals
- aligns with agent-oriented workspace conventions

## Suggested Future Refactors

1. Add a stable manifest file (`pack_manifest.yaml`) with:
   - skill names
   - version
   - dependency pointers
   - test cases
2. Add CI checks:
   - frontmatter validation for all `SKILL.md`
   - broken-link checks across references/docs
   - minimal script dry-run checks
3. Add release discipline:
   - semantic tags (`v0.3.x`)
   - changelog sections for skill/rule/data updates

## Current Entry Points

- human entry: `README.md`
- human entry (Chinese): `README.zh-CN.md`
- skill inventory: `docs/skill-catalog.md`
- skill inventory (Chinese): `docs/skill-catalog.zh-CN.md`
- execution flow: `docs/workflow-playbook.md`
- execution flow (Chinese): `docs/workflow-playbook.zh-CN.md`
- usage examples and fusion: `docs/usage-examples.md`
- usage examples and fusion (Chinese): `docs/usage-examples.zh-CN.md`
- bilingual coverage list: `docs/bilingual-index.md`
- runtime skills: `.agents/skills/`
- knowledge base: `.references/`
