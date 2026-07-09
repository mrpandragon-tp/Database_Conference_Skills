# Usage Examples and Skill Fusion

This page focuses on practical, copyable usage patterns for the
`db_topconf_skill_pack_v03` skill set.

## 1) Quick Capability Map

| Skill | When to run | Example request to the agent | Expected output |
| --- | --- | --- | --- |
| `db-paper-orchestrator` | project start or scope reset | "Based on my code, logs, and plots, plan the full SIGMOD/VLDB writing pipeline." | phase plan + artifact checklist + risk register |
| `db-novelty-positioning` | before deep drafting | "Map my claims to nearest prior work and flag incremental-risk." | claim-prior-delta table + evidence needed |
| `db-writing-copilot` | section drafting | "Draft Introduction + Method with claim-evidence pointers." | section draft + claim-evidence map |
| `db-method-proof-check` | theorem/proof stabilization | "Audit theorem assumptions and dependency closure." | assumption gaps + required proof rewrites |
| `db-experiment-evidence-auditor` | experiment planning and result audit | "Check baseline fairness and missing stress tests." | fairness findings + priority experiment fixes |
| `db-figure-design` | figure planning and QA | "Design figures tied to top claims and reviewer questions." | figure plan + caption drafts + visual QA |
| `db-reader-reviewer-preflight` | near-submission | "Review from strict SIGMOD/VLDB reviewer perspective." | fatal/major findings + action plan |
| `db-format-finish` | final stage | "Run final LaTeX/PDF formatting preflight." | blocking formatting issues + final checklist |

## 2) End-to-End Recipe

### Scenario A: from code and raw results to full paper workflow

1. Run `db-paper-orchestrator` to define phases and required artifacts.
2. Run `db-novelty-positioning` on top claims.
3. Run `db-writing-copilot` for Abstract/Intro/Method/Experiments.
4. Run `db-method-proof-check` for theorem-quality closure.
5. Run `db-experiment-evidence-auditor` for fairness and coverage.
6. Run `db-figure-design` to align visual evidence with claims.
7. Run `db-reader-reviewer-preflight` for rejection-risk triage.
8. Run `db-format-finish` for final submission hygiene.

### Scenario B: reviewer says "novelty is weak"

1. Re-run `db-novelty-positioning` and regenerate the claim-prior map.
2. Re-run `db-experiment-evidence-auditor` to collect missing decisive evidence.
3. Re-run `db-writing-copilot` to tighten wording to measurable deltas.
4. Re-run `db-reader-reviewer-preflight` and verify risk-level drop.

### Scenario C: proof concerns appear late

1. Run `db-method-proof-check` first and close assumption gaps.
2. Add empirical cross-checks with `db-experiment-evidence-auditor`.
3. Rewrite affected sections with `db-writing-copilot`.

## 3) Fusion with External Skills

The pack is designed to work with other general-purpose writing and figure
skills. Recommended pairings:

| External skill | How to combine with this pack | Why this pairing helps |
| --- | --- | --- |
| `research-paper-writing` | use after `db-novelty-positioning`, before final section drafting | stronger paragraph-level scientific argument flow |
| `ml-paper-writing` | use only for learning-specific technical wording inside DB paper sections | improves ML-heavy wording while keeping DB framing |
| `humanizer` | use after major technical risks are closed | smoother language without changing technical meaning |
| `scientific-figure-making` | pair with `db-figure-design` | converts figure plan into publication-ready plots |
| `canvas-design` | pair with system-overview figure passes | improves architecture diagram readability |
| `pdf` | pair with `db-format-finish` | checks final layout and rendering quality |

Guardrail:
- keep DB venue expectations as the primary objective
- do not let style-oriented skills override evidence/proof correctness

## 4) Add New Papers and Distill New Knowledge

This pack supports continuous corpus expansion from local Zotero.

### 4.1 Add papers (no code change path)

1. Add papers into Zotero collections currently used by scripts:
   - `ANN`
   - `SIGMOD/VLDB`
2. Ensure PDF fulltext cache is available in Zotero.
3. Rebuild knowledge:

```bash
./rebuild_knowledge.sh
```

### 4.2 Change source collections or Zotero path

Edit:
- `scripts/refresh_paper_index.sh`
  - update collection names in SQL: `('ANN', 'SIGMOD/VLDB')`
  - update `DB_URI` if your Zotero DB path differs
- `scripts/distill_fulltext_semantics.py`
  - update `DB_URI`
  - update `ZOTERO_STORAGE`

Then rerun:

```bash
./rebuild_knowledge.sh
```

### 4.3 Validate distillation quality

Check:
- `.references/paper-corpus/fulltext_distillation_report.md`
- `.references/paper-corpus/fulltext_semantic_profile.csv`
- `.references/distilled/*_fulltext.md`

Sanity expectations:
- profile row count should roughly match selected paper count
- novelty/proof/experiment matrices should refresh with new papers

## 5) Regression Checks After Skill/Corpus Updates

Run:

```bash
find .agents/skills -mindepth 1 -maxdepth 1 -type d | while read -r d; do
  test -f "$d/SKILL.md" || echo "Missing SKILL.md: $d"
  test -f "$d/agents/openai.yaml" || echo "Missing openai.yaml: $d"
done

for s in .agents/skills/*; do
  n="$(basename "$s")"
  test -f ".agents/skill_tests/${n}-test.md" || echo "Missing test: $n"
done
```

For full checks after script updates:

```bash
./rebuild_knowledge.sh
```

