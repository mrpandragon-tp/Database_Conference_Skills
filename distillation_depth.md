# Distillation Depth (v0.3)

## Current depth

This version includes per-paper fulltext semantic parsing based on Zotero fulltext cache files (`.zotero-ft-cache`) for papers in the target collections.

Coverage in this run:
- Total target papers: 81
- Fulltext semantic profiles built: 80
- Uncovered papers: 1 (no usable selected fulltext cache)

## What is distilled from fulltext

For each parsed paper, the pipeline extracts:
- section-structure signals (introduction/method/experiments/conclusion)
- writing-chain signals (problem -> gap -> proposal -> quantified evidence)
- proof signals (theorem/lemma/proof/assumption/complexity mentions)
- experiment signals (quality/latency/throughput/build/update/memory/ablation/fairness)
- performance-claim signals (speedup/percent/tradeoff mentions)
- reviewer-risk estimates (novelty/evidence/proof)

Outputs are in:
- `.references/paper-corpus/fulltext_semantic_profile.csv`
- `.references/paper-corpus/fulltext_*_matrix.md`
- `.references/paper-corpus/fulltext_distillation_report.md`
- `.references/distilled/*_fulltext.md`

## Remaining limitations

- This is semantic signal extraction, not a complete logical reconstruction of every theorem proof.
- Formula-level equivalence checks and full dependency proof graphs still require a deeper theorem parser.
- PDF OCR quality depends on Zotero fulltext cache quality.

## Next deepening options

1. Add theorem dependency graph extraction from section-level fulltext chunks.
2. Add per-paper claim-to-figure/theorem pointer extraction.
3. Add section-level rhetorical template mining for accepted-paper writing style.
