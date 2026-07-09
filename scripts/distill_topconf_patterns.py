#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CORPUS = ROOT / '.references' / 'paper-corpus'
DISTILLED = ROOT / '.references' / 'distilled'
CORPUS.mkdir(parents=True, exist_ok=True)
DISTILLED.mkdir(parents=True, exist_ok=True)

paper_csv = CORPUS / 'paper_index.csv'
if not paper_csv.exists():
    raise SystemExit(f'Missing {paper_csv}. Run refresh_paper_index.sh first.')

rows = list(csv.DictReader(paper_csv.open(encoding='utf-8')))


def n(text: str) -> str:
    return (text or '').lower()


def has_any(text: str, kws: list[str]) -> bool:
    t = n(text)
    return any(k in t for k in kws)


def pick_tags(text: str, mapping: dict[str, list[str]]) -> list[str]:
    out = []
    for tag, kws in mapping.items():
        if has_any(text, kws):
            out.append(tag)
    return out


def table(headers: list[str], rows_: list[list[str]]) -> str:
    out = ['| ' + ' | '.join(headers) + ' |', '| ' + ' | '.join(['---'] * len(headers)) + ' |']
    for r in rows_:
        out.append('| ' + ' | '.join(str(x).replace('|', '\\|').replace('\n', ' ') for x in r) + ' |')
    return '\n'.join(out)


problem_kws = ['challenge', 'difficult', 'limitation', 'bottleneck', 'struggle', 'fails to', 'underexplored']
gap_kws = ['however', 'yet', 'while', 'but', 'do not', 'does not', 'lack', 'insufficient']
proposal_kws = ['we propose', 'we present', 'this paper presents', 'we introduce', 'we develop']
exp_kws = ['experiment', 'evaluate', 'benchmark', 'datasets', 'extensive', 'empirical']
quant_kws = ['up to', 'x speedup', '×', '%', 'recall@', 'latency', 'throughput']

novelty_map = {
    'new-index-structure': ['index', 'graph', 'layout', 'tree', 'structure', 'framework'],
    'algorithmic-optimization': ['optimiz', 'accelerat', 'pruning', 'routing', 'scheduling'],
    'system-co-design': ['system', 'architecture', 'pipeline', 'co-design', 'database'],
    'benchmark-analysis': ['benchmark', 'survey', 'in-depth study', 'analysis'],
    'theoretical-characterization': ['theorem', 'bound', 'guarantee', 'convergence', 'complexity'],
}

proof_map = {
    'exactness-correctness': ['exact', 'correctness', 'fallback', 'certify', 'certification'],
    'approximation-guarantee': ['guarantee', 'target recall', 'approximate objective', 'admissible'],
    'complexity-bound': ['complexity', 'bound', 'time complexity', 'space complexity'],
    'convergence': ['convergence'],
}

exp_map = {
    'quality-metric': ['recall', 'accuracy', 'nDCG', 'precision'],
    'latency-throughput': ['latency', 'throughput', 'qps'],
    'build-cost': ['build time', 'indexing time', 'construction'],
    'update-cost': ['update', 'insertion', 'ingestion'],
    'memory-footprint': ['memory', 'index size', 'footprint', 'rss'],
    'ablation': ['ablation'],
    'sensitivity': ['sensitivity', 'selectivity', 'ratio'],
    'scalability': ['scale', 'distributed', 'multi-machine', 'billion-scale'],
}

baseline_names = [
    'hnsw', 'diskann', 'ivf', 'ivf-pq', 'pq', 'scann', 'spann', 'faiss',
    'aster', 'knn-index', 'glad', 'ten', 'dijkstra', 'acorn', 'navix',
]

@dataclass
class PaperSig:
    paper_id: str
    title: str
    year: str
    source: str
    novelty_tags: list[str]
    proof_tags: list[str]
    exp_tags: list[str]
    has_problem: bool
    has_gap: bool
    has_proposal: bool
    has_exp: bool
    has_quant: bool
    baseline_mentions: list[str]
    abstract_chars: int


sigs: list[PaperSig] = []
for r in rows:
    text = f"{r.get('title','')} {r.get('abstract','')} {r.get('venue','')}"
    t = n(text)

    novelty_tags = pick_tags(text, novelty_map)
    proof_tags = pick_tags(text, proof_map)
    exp_tags = pick_tags(text, exp_map)

    baselines = sorted({b for b in baseline_names if b in t})

    sigs.append(
        PaperSig(
            paper_id=r.get('paper_id', ''),
            title=r.get('title', ''),
            year=r.get('year', ''),
            source=r.get('source_collection', ''),
            novelty_tags=novelty_tags,
            proof_tags=proof_tags,
            exp_tags=exp_tags,
            has_problem=has_any(text, problem_kws),
            has_gap=has_any(text, gap_kws),
            has_proposal=has_any(text, proposal_kws),
            has_exp=has_any(text, exp_kws),
            has_quant=has_any(text, quant_kws),
            baseline_mentions=baselines,
            abstract_chars=int(r.get('abstract_chars') or 0),
        )
    )

# Aggregate counters
c_novel = Counter(tag for s in sigs for tag in s.novelty_tags)
c_proof = Counter(tag for s in sigs for tag in s.proof_tags)
c_exp = Counter(tag for s in sigs for tag in s.exp_tags)
c_baseline = Counter(tag for s in sigs for tag in s.baseline_mentions)

# Matrix files
method_rows = []
writing_rows = []
proof_rows = []
exp_rows = []
perf_rows = []
risk_rows = []

for s in sigs:
    text_struct = []
    if s.has_problem:
        text_struct.append('problem')
    if s.has_gap:
        text_struct.append('gap')
    if s.has_proposal:
        text_struct.append('proposal')
    if s.has_exp:
        text_struct.append('evaluation')
    if s.has_quant:
        text_struct.append('quant-result')

    method_rows.append([
        s.paper_id,
        s.year,
        s.source,
        s.title,
        ', '.join(s.novelty_tags) or 'none-detected',
    ])

    writing_rows.append([
        s.paper_id,
        s.title,
        ', '.join(text_struct) or 'none-detected',
        s.abstract_chars,
    ])

    proof_rows.append([
        s.paper_id,
        s.title,
        ', '.join(s.proof_tags) or 'none-detected',
    ])

    exp_rows.append([
        s.paper_id,
        s.title,
        ', '.join(s.exp_tags) or 'none-detected',
        ', '.join(s.baseline_mentions) or 'none-detected',
    ])

    perf_focus = 'balanced'
    if 'quality-metric' in s.exp_tags and 'latency-throughput' not in s.exp_tags:
        perf_focus = 'quality-only-risk'
    elif 'latency-throughput' in s.exp_tags and 'quality-metric' not in s.exp_tags:
        perf_focus = 'speed-only-risk'

    perf_rows.append([
        s.paper_id,
        s.title,
        perf_focus,
        'yes' if s.has_quant else 'no',
    ])

    novelty_risk = 'moderate'
    if 'benchmark-analysis' in s.novelty_tags and len(s.novelty_tags) == 1:
        novelty_risk = 'major'
    elif not s.novelty_tags:
        novelty_risk = 'major'

    proof_risk = 'moderate'
    title_l = n(s.title)
    theorem_words = any(k in title_l for k in ['exact', 'guarantee', 'bound', 'convergence'])
    if theorem_words and not s.proof_tags:
        proof_risk = 'major'
    elif s.proof_tags:
        proof_risk = 'minor-to-moderate (depends on formal assumptions in full text)'

    evidence_risk = 'moderate'
    if not s.has_exp:
        evidence_risk = 'major'
    elif not s.has_quant:
        evidence_risk = 'moderate-high'

    fairness_risk = 'moderate'
    if not s.baseline_mentions:
        fairness_risk = 'major'

    risk_rows.append([
        s.paper_id,
        s.title,
        novelty_risk,
        evidence_risk,
        fairness_risk,
        proof_risk,
    ])

(CORPUS / 'method_matrix.md').write_text(
    '# Method Matrix\n\n' +
    table(['paper_id', 'year', 'collection', 'title', 'novelty_tags'], method_rows) + '\n',
    encoding='utf-8'
)

(CORPUS / 'writing_signal_matrix.md').write_text(
    '# Writing Signal Matrix\n\n' +
    table(['paper_id', 'title', 'abstract_structure_signals', 'abstract_chars'], writing_rows) + '\n',
    encoding='utf-8'
)

(CORPUS / 'proof_signal_matrix.md').write_text(
    '# Proof Signal Matrix\n\n' +
    table(['paper_id', 'title', 'proof_signals_from_metadata'], proof_rows) + '\n',
    encoding='utf-8'
)

(CORPUS / 'experiment_signal_matrix.md').write_text(
    '# Experiment Signal Matrix\n\n' +
    table(['paper_id', 'title', 'experiment_signals', 'baseline_mentions'], exp_rows) + '\n',
    encoding='utf-8'
)

(CORPUS / 'performance_claim_matrix.md').write_text(
    '# Performance Claim Matrix\n\n' +
    table(['paper_id', 'title', 'performance_focus_risk', 'quantified_result_signal'], perf_rows) + '\n',
    encoding='utf-8'
)

(CORPUS / 'reviewer_risk_matrix.md').write_text(
    '# Reviewer Risk Matrix\n\n' +
    table(['paper_id', 'title', 'novelty_risk', 'evidence_risk', 'fairness_risk', 'proof_risk'], risk_rows) + '\n',
    encoding='utf-8'
)

# topconf signal report
n_total = len(sigs)
has_problem = sum(1 for s in sigs if s.has_problem)
has_proposal = sum(1 for s in sigs if s.has_proposal)
has_exp = sum(1 for s in sigs if s.has_exp)
has_quant = sum(1 for s in sigs if s.has_quant)

report = [
    '# Topconf Signal Report',
    '',
    f'- Total papers analyzed: {n_total}',
    f'- Problem framing signal in abstract/title: {has_problem}/{n_total}',
    f'- Explicit proposal signal: {has_proposal}/{n_total}',
    f'- Evaluation signal: {has_exp}/{n_total}',
    f'- Quantified-result signal: {has_quant}/{n_total}',
    '',
    '## Novelty pattern frequency',
]
for k, v in c_novel.most_common():
    report.append(f'- {k}: {v}')
report += ['', '## Proof pattern frequency']
for k, v in c_proof.most_common():
    report.append(f'- {k}: {v}')
report += ['', '## Experiment pattern frequency']
for k, v in c_exp.most_common():
    report.append(f'- {k}: {v}')
report += ['', '## Baseline mention frequency (metadata-level)']
for k, v in c_baseline.most_common():
    report.append(f'- {k}: {v}')

(CORPUS / 'topconf_signal_report.md').write_text('\n'.join(report) + '\n', encoding='utf-8')

# Distilled docs
(DISTILLED / 'novelty_patterns.md').write_text(
    '\n'.join([
        '# Novelty Patterns for SIGMOD/VLDB',
        '',
        '## What repeatedly appears in stronger papers',
        '- A clear system-level mechanism, not only model insertion.',
        '- Explicit statement of what cost is reduced and where in the execution path.',
        '- Positioning against strongest nearest prior work, not only weak baselines.',
        '- Quantified improvement under fair comparison setup.',
        '',
        '## Common novelty failure modes',
        '- "We add a learned model" without architectural or maintenance innovation.',
        '- Novelty claim relies on wording rather than measurable or provable deltas.',
        '- Nearest prior work is ignored or reframed unfairly.',
        '',
        '## Checklist',
        '- Define the delta vs nearest prior in one sentence.',
        '- Show why delta is system-relevant (build/update/query/memory/reproducibility).',
        '- Provide evidence plan before polishing language.',
    ]) + '\n',
    encoding='utf-8'
)

(DISTILLED / 'writing_patterns.md').write_text(
    '\n'.join([
        '# Writing Patterns for SIGMOD/VLDB',
        '',
        '## Typical abstract/introduction skeleton',
        '1. Problem and practical tension.',
        '2. Why existing methods are insufficient.',
        '3. Proposed mechanism and scope.',
        '4. Key evidence and quantified takeaway.',
        '',
        '## Common writing risks',
        '- Contribution sentence is too generic to be testable.',
        '- Claims outrun evidence in Abstract/Introduction.',
        '- Method and experiment sections optimize different goals.',
        '',
        '## Reader-first checks',
        '- Can a skeptical reader state your exact contribution in one sentence?',
        '- Is every major claim linked to a figure/table/theorem location?',
        '- Are limitation and applicability boundaries explicit?',
    ]) + '\n',
    encoding='utf-8'
)

(DISTILLED / 'proof_patterns.md').write_text(
    '\n'.join([
        '# Proof Patterns for Database Papers',
        '',
        '## Proof obligations that frequently matter',
        '- Explicit assumptions for data model, query model, update model.',
        '- Correctness/exactness conditions and fallback behavior.',
        '- Closed lemma-theorem dependency chain.',
        '- Complexity claims tied to clear computational model.',
        '',
        '## Common proof failure modes',
        '- Theorem wording without assumptions.',
        '- Guarantee claim without proving corner-case handling.',
        '- Complexity discussion that mixes offline and online costs.',
        '',
        '## Checklist',
        '- For each theorem-like claim: assumption list, dependency list, proof pointer, empirical cross-check pointer.',
    ]) + '\n',
    encoding='utf-8'
)

(DISTILLED / 'experiment_design_patterns.md').write_text(
    '\n'.join([
        '# Experiment Design Patterns for Top DB Venues',
        '',
        '## Core evidence dimensions',
        '- Quality metric (recall/accuracy) + efficiency metric (latency/throughput).',
        '- Build/indexing cost, update cost, and memory footprint.',
        '- Fair tuning disclosure and repeated-run policy.',
        '',
        '## Typical stress axes',
        '- Data scale and dimensionality.',
        '- Update ratio and stream dynamics.',
        '- Filter selectivity/correlation where filtering is claimed.',
        '- Distributed scale-out where distributed claims are made.',
        '',
        '## Checklist',
        '- No speedup claim without paired quality target.',
        '- No quality claim without corresponding efficiency cost.',
        '- No main claim supported only by appendix-only experiments.',
    ]) + '\n',
    encoding='utf-8'
)

(DISTILLED / 'performance_claim_patterns.md').write_text(
    '\n'.join([
        '# Performance Claim Patterns',
        '',
        '## Strong claim style',
        '- State metric, setting, and comparison target in one sentence.',
        '- Report tradeoff, not only one-axis wins.',
        '- Include non-win regimes and explain why.',
        '',
        '## Weak claim style',
        '- Absolute "faster" claims without recall/memory/tuning context.',
        '- Aggregated claims that hide scenario-specific regressions.',
    ]) + '\n',
    encoding='utf-8'
)

(DISTILLED / 'reader_reviewer_risk_patterns.md').write_text(
    '\n'.join([
        '# Reader and Reviewer Risk Patterns',
        '',
        '## High-frequency rejection risks',
        '- Incremental novelty framing.',
        '- Incomplete baseline fairness disclosure.',
        '- Missing proof assumptions for guarantee-like claims.',
        '- Evidence mismatch between Abstract claims and main-paper figures/tables.',
        '',
        '## Pre-submission preflight order',
        '1. Novelty and positioning',
        '2. Technical soundness and proof obligations',
        '3. Experiment fairness and coverage',
        '4. Reproducibility and reporting clarity',
        '5. Final readability and layout quality',
    ]) + '\n',
    encoding='utf-8'
)

(DISTILLED / 'existing_skill_integration.md').write_text(
    '\n'.join([
        '# Existing Skill Integration',
        '',
        '| Existing skill | Recommended role in pipeline | Risk to control |',
        '| --- | --- | --- |',
        '| research-paper-writing | Main drafting and claim-evidence structuring | Keep venue-specific DB constraints explicit |',
        '| ml-paper-writing | Tighten learning-related technical prose | Avoid importing ML-venue rhetorical habits as default |',
        '| humanizer | Final pass for natural writing | Do not weaken formal caveats or proof precision |',
        '| scientific-figure-making | Produce publication-quality experiment figures | Tie each figure to a claim and reviewer question |',
        '| canvas-design | System/architecture diagram refinement | Keep technical clarity over artistic complexity |',
        '| pdf | Final layout and visual integrity checks | Ensure content quality checks are done before formatting-only pass |',
    ]) + '\n',
    encoding='utf-8'
)

(DISTILLED / 'end_to_end_pipeline.md').write_text(
    '\n'.join([
        '# End-to-End Paper Pipeline (Code/Results -> Submission Draft)',
        '',
        '1. Inventory project assets: code modules, experiment scripts, outputs, plots, logs.',
        '2. Draft contribution candidates and nearest-prior map.',
        '3. Design evidence plan: experiments + proof obligations + figure plan.',
        '4. Write sections with claim-evidence mapping.',
        '5. Run proof soundness pass.',
        '6. Run experiment fairness pass.',
        '7. Run reader/reviewer preflight pass.',
        '8. Polish language and finalize layout.',
    ]) + '\n',
    encoding='utf-8'
)

print(f'Analyzed {len(sigs)} papers')
print(f'Wrote corpus files to {CORPUS}')
print(f'Wrote distilled files to {DISTILLED}')
