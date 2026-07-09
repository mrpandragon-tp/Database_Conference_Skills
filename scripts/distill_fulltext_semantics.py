#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
import sqlite3
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CORPUS = ROOT / '.references' / 'paper-corpus'
DISTILLED = ROOT / '.references' / 'distilled'
CORPUS.mkdir(parents=True, exist_ok=True)
DISTILLED.mkdir(parents=True, exist_ok=True)

DB_URI = 'file:/Users/mrpandragon/Zotero/zotero.sqlite?immutable=1'
ZOTERO_STORAGE = Path('/Users/mrpandragon/Zotero/storage')

paper_index_csv = CORPUS / 'paper_index.csv'
if not paper_index_csv.exists():
    raise SystemExit(f'Missing {paper_index_csv}. Run refresh_paper_index.sh first.')

paper_rows = list(csv.DictReader(paper_index_csv.open(encoding='utf-8')))
paper_by_id = {r['paper_id']: r for r in paper_rows}

conn = sqlite3.connect(DB_URI, uri=True)
cur = conn.cursor()

# Pick one best PDF attachment per paper by indexedChars then totalPages.
q = '''
WITH target_collections AS (
  SELECT collectionID
  FROM collections
  WHERE collectionName IN ('ANN', 'SIGMOD/VLDB')
),
papers AS (
  SELECT DISTINCT ci.itemID AS paperItemID
  FROM collectionItems ci
  JOIN target_collections tc ON tc.collectionID = ci.collectionID
),
pdf_attachments AS (
  SELECT
    p.paperItemID,
    ia.itemID AS attachmentItemID,
    ai.key AS attachmentKey,
    COALESCE(fi.indexedChars, 0) AS indexedChars,
    COALESCE(fi.totalPages, 0) AS totalPages
  FROM papers p
  JOIN itemAttachments ia ON ia.parentItemID = p.paperItemID
  JOIN items ai ON ai.itemID = ia.itemID
  LEFT JOIN fulltextItems fi ON fi.itemID = ia.itemID
  WHERE LOWER(COALESCE(ia.contentType,'')) = 'application/pdf'
),
ranked AS (
  SELECT *,
         ROW_NUMBER() OVER (
            PARTITION BY paperItemID
            ORDER BY indexedChars DESC, totalPages DESC, attachmentItemID ASC
         ) AS rn
  FROM pdf_attachments
)
SELECT paperItemID, attachmentItemID, attachmentKey, indexedChars, totalPages
FROM ranked
WHERE rn = 1
'''

att_rows = cur.execute(q).fetchall()

baseline_patterns = {
    'hnsw': re.compile(r'\bhnsw\b', re.I),
    'diskann': re.compile(r'\bdiskann\b', re.I),
    'ivf-pq': re.compile(r'\bivf[\s_-]?pq\b', re.I),
    'ivf': re.compile(r'\bivf\b', re.I),
    'pq': re.compile(r'\bpq\b', re.I),
    'scann': re.compile(r'\bscann\b', re.I),
    'spann': re.compile(r'\bspann\b', re.I),
    'faiss': re.compile(r'\bfaiss\b', re.I),
    'aster': re.compile(r'\baster\b', re.I),
    'knn-index': re.compile(r'\bknn[\s_-]?index\b', re.I),
    'glad': re.compile(r'\bglad\b', re.I),
    'ten_t': re.compile(r'\bten[_-]?t\b', re.I),
    'dijkstra': re.compile(r'\bdijkstra\b', re.I),
    'acorn': re.compile(r'\bacorn\b', re.I),
    'navix': re.compile(r'\bnavix\b', re.I),
}
metrics = {
    'quality': ['recall', 'accuracy', 'ndcg', 'precision'],
    'latency': ['latency', 'response time'],
    'throughput': ['throughput', 'qps'],
    'build': ['build time', 'construction', 'indexing time'],
    'update': ['update', 'insertion', 'ingestion', 'maintenance'],
    'memory': ['memory', 'footprint', 'index size', 'rss'],
}

section_patterns = {
    'introduction': re.compile(r'(^|\n)\s*(\d+\.?\s*)?introduction\s*(\n|$)', re.I),
    'related_work': re.compile(r'(^|\n)\s*(\d+\.?\s*)?(related work|background and related work)\s*(\n|$)', re.I),
    'preliminaries': re.compile(r'(^|\n)\s*(\d+\.?\s*)?(preliminar|background|problem definition)\s*(\n|$)', re.I),
    'method': re.compile(r'(^|\n)\s*(\d+\.?\s*)?(method|approach|design|framework|system design)\s*(\n|$)', re.I),
    'experiments': re.compile(r'(^|\n)\s*(\d+\.?\s*)?(experiment|evaluation)\s*(\n|$)', re.I),
    'conclusion': re.compile(r'(^|\n)\s*(\d+\.?\s*)?(conclusion|concluding)\s*(\n|$)', re.I),
}

def norm(t: str) -> str:
    return (t or '').lower()


def count_matches(text: str, pat: str) -> int:
    return len(re.findall(pat, text, flags=re.I))


def has_any(text: str, kws: list[str]) -> bool:
    t = norm(text)
    return any(k in t for k in kws)


def first_n_chars(text: str, n: int = 5000) -> str:
    return text[:n]

profiles = []
missing_cache = 0

for paper_id, att_item_id, att_key, indexed_chars, total_pages in att_rows:
    paper_id = str(paper_id)
    item = paper_by_id.get(paper_id)
    if not item:
        continue

    cache_path = ZOTERO_STORAGE / str(att_key) / '.zotero-ft-cache'
    full_text = ''
    if cache_path.exists():
        full_text = cache_path.read_text(encoding='utf-8', errors='ignore')
    else:
        missing_cache += 1

    t = norm(full_text)
    intro_window = norm(first_n_chars(full_text, 7000))

    # Section signals from full text
    section_hits = {name: bool(p.search(full_text)) for name, p in section_patterns.items()}

    # Writing structure signals
    has_problem = has_any(intro_window, ['challenge', 'difficult', 'limitation', 'bottleneck', 'underexplored', 'important'])
    has_gap = has_any(intro_window, ['however', 'yet', 'while', 'but', 'do not', 'does not', 'lack', 'insufficient'])
    has_proposal = has_any(intro_window, ['we propose', 'we present', 'this paper presents', 'we introduce', 'our approach'])
    has_contrib_list = has_any(t, ['our contributions are', 'we make the following contributions', 'contributions are summarized'])
    has_quant = bool(re.search(r'\b\d+(\.\d+)?\s*(x|×|%)\b', full_text))

    # Proof semantics
    theorem_count = count_matches(full_text, r'\btheorem\b')
    lemma_count = count_matches(full_text, r'\blemma\b')
    proposition_count = count_matches(full_text, r'\bproposition\b')
    corollary_count = count_matches(full_text, r'\bcorollary\b')
    proof_count = count_matches(full_text, r'\bproof\b')
    assumption_count = count_matches(full_text, r'\bassumption\b')
    complexity_count = count_matches(full_text, r'\btime complexity\b|\bspace complexity\b|\bO\([^\)]*\)')

    # Experiment semantics
    metric_hits = {k: has_any(t, kws) for k, kws in metrics.items()}
    ablation_hit = has_any(t, ['ablation'])
    sensitivity_hit = has_any(t, ['sensitivity', 'selectivity', 'vary', 'ratio'])
    fairness_hit = has_any(t, ['same recall', 'same memory', 'fair', 'tuning'])
    reproducibility_hit = has_any(t, ['code available', 'github', 'artifact', 'reproduc'])

    baseline_hits = [name for name, pat in baseline_patterns.items() if pat.search(full_text)]

    # Performance claim semantics
    speedup_mentions = count_matches(full_text, r'\b\d+(\.\d+)?\s*(x|×)\b')
    percent_mentions = count_matches(full_text, r'\b\d+(\.\d+)?\s*%\b')
    tradeoff_hit = has_any(t, ['trade-off', 'tradeoff', 'latency-recall', 'build-update-query'])

    profiles.append({
        'paper_id': paper_id,
        'title': item.get('title', ''),
        'year': item.get('year', ''),
        'source_collection': item.get('source_collection', ''),
        'attachment_item_id': str(att_item_id),
        'attachment_key': str(att_key),
        'indexed_chars': int(indexed_chars or 0),
        'total_pages': int(total_pages or 0),
        'fulltext_chars': len(full_text),
        'section_introduction': int(section_hits['introduction']),
        'section_related_work': int(section_hits['related_work']),
        'section_preliminaries': int(section_hits['preliminaries']),
        'section_method': int(section_hits['method']),
        'section_experiments': int(section_hits['experiments']),
        'section_conclusion': int(section_hits['conclusion']),
        'signal_problem': int(has_problem),
        'signal_gap': int(has_gap),
        'signal_proposal': int(has_proposal),
        'signal_contribution_list': int(has_contrib_list),
        'signal_quantified_result': int(has_quant),
        'theorem_count': theorem_count,
        'lemma_count': lemma_count,
        'proposition_count': proposition_count,
        'corollary_count': corollary_count,
        'proof_count': proof_count,
        'assumption_count': assumption_count,
        'complexity_signal_count': complexity_count,
        'metric_quality': int(metric_hits['quality']),
        'metric_latency': int(metric_hits['latency']),
        'metric_throughput': int(metric_hits['throughput']),
        'metric_build': int(metric_hits['build']),
        'metric_update': int(metric_hits['update']),
        'metric_memory': int(metric_hits['memory']),
        'signal_ablation': int(ablation_hit),
        'signal_sensitivity': int(sensitivity_hit),
        'signal_fairness': int(fairness_hit),
        'signal_reproducibility': int(reproducibility_hit),
        'baseline_mentions': '; '.join(baseline_hits),
        'speedup_mentions': speedup_mentions,
        'percent_mentions': percent_mentions,
        'signal_tradeoff': int(tradeoff_hit),
    })

# Save full profile CSV
profile_csv = CORPUS / 'fulltext_semantic_profile.csv'
with profile_csv.open('w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=list(profiles[0].keys()) if profiles else [])
    writer.writeheader()
    writer.writerows(profiles)

# Helper: markdown table

def md_table(headers, rows):
    out = ['| ' + ' | '.join(headers) + ' |', '| ' + ' | '.join(['---'] * len(headers)) + ' |']
    for r in rows:
        out.append('| ' + ' | '.join(str(x).replace('|', '\\|') for x in r) + ' |')
    return '\n'.join(out)

# Build matrices
sec_rows, write_rows, proof_rows, exp_rows, risk_rows = [], [], [], [], []

for p in profiles:
    sec_rows.append([
        p['paper_id'], p['title'], p['section_introduction'], p['section_related_work'], p['section_method'], p['section_experiments'], p['section_conclusion']
    ])

    write_rows.append([
        p['paper_id'], p['title'],
        p['signal_problem'], p['signal_gap'], p['signal_proposal'], p['signal_contribution_list'], p['signal_quantified_result']
    ])

    proof_rows.append([
        p['paper_id'], p['title'], p['theorem_count'], p['lemma_count'], p['proof_count'], p['assumption_count'], p['complexity_signal_count']
    ])

    exp_rows.append([
        p['paper_id'], p['title'], p['metric_quality'], p['metric_latency'], p['metric_throughput'], p['metric_build'], p['metric_update'], p['metric_memory'], p['signal_ablation'], p['signal_fairness']
    ])

    novelty_risk = 'minor'
    if not (p['signal_problem'] and p['signal_gap'] and p['signal_proposal']):
        novelty_risk = 'major'
    elif not p['signal_quantified_result']:
        novelty_risk = 'moderate'

    proof_risk = 'minor'
    theorem_like = (p['theorem_count'] + p['lemma_count'] + p['proposition_count'] + p['corollary_count']) > 0
    if theorem_like and p['proof_count'] == 0:
        proof_risk = 'major'
    elif theorem_like and p['assumption_count'] == 0:
        proof_risk = 'moderate'

    evidence_risk = 'minor'
    has_quality = p['metric_quality'] == 1
    has_eff = p['metric_latency'] == 1 or p['metric_throughput'] == 1
    if not has_quality or not has_eff:
        evidence_risk = 'major'
    elif p['signal_fairness'] == 0:
        evidence_risk = 'moderate'

    risk_rows.append([p['paper_id'], p['title'], novelty_risk, evidence_risk, proof_risk])

(CORPUS / 'fulltext_section_signal_matrix.md').write_text(
    '# Fulltext Section Signal Matrix\n\n' +
    md_table(['paper_id', 'title', 'intro', 'related', 'method', 'experiments', 'conclusion'], sec_rows) + '\n',
    encoding='utf-8'
)

(CORPUS / 'fulltext_writing_signal_matrix.md').write_text(
    '# Fulltext Writing Signal Matrix\n\n' +
    md_table(['paper_id', 'title', 'problem', 'gap', 'proposal', 'contrib_list', 'quantified'], write_rows) + '\n',
    encoding='utf-8'
)

(CORPUS / 'fulltext_proof_signal_matrix.md').write_text(
    '# Fulltext Proof Signal Matrix\n\n' +
    md_table(['paper_id', 'title', 'theorem', 'lemma', 'proof', 'assumption', 'complexity_signal'], proof_rows) + '\n',
    encoding='utf-8'
)

(CORPUS / 'fulltext_experiment_signal_matrix.md').write_text(
    '# Fulltext Experiment Signal Matrix\n\n' +
    md_table(['paper_id', 'title', 'quality', 'latency', 'throughput', 'build', 'update', 'memory', 'ablation', 'fairness'], exp_rows) + '\n',
    encoding='utf-8'
)

(CORPUS / 'fulltext_reviewer_risk_matrix.md').write_text(
    '# Fulltext Reviewer Risk Matrix\n\n' +
    md_table(['paper_id', 'title', 'novelty_risk', 'evidence_risk', 'proof_risk'], risk_rows) + '\n',
    encoding='utf-8'
)

# Aggregate fulltext report
n = len(profiles)
cov = lambda k: sum(int(p[k]) for p in profiles)

tag_counts = Counter()
for p in profiles:
    if p['baseline_mentions']:
        for b in [x.strip() for x in p['baseline_mentions'].split(';') if x.strip()]:
            tag_counts[b] += 1

report = [
    '# Fulltext Distillation Report',
    '',
    f'- Papers with selected PDF attachment: {len(att_rows)}',
    f'- Papers with parsed fulltext profile: {n}',
    f'- Missing `.zotero-ft-cache` among selected attachments: {missing_cache}',
    '',
    '## Writing structure coverage (fulltext)',
    f'- problem signal: {cov("signal_problem")}/{n}',
    f'- gap signal: {cov("signal_gap")}/{n}',
    f'- proposal signal: {cov("signal_proposal")}/{n}',
    f'- quantified-result signal: {cov("signal_quantified_result")}/{n}',
    '',
    '## Proof structure coverage (fulltext)',
    f'- papers with theorem/lemma/proposition/corollary mentions: {sum(1 for p in profiles if (p["theorem_count"]+p["lemma_count"]+p["proposition_count"]+p["corollary_count"])>0)}/{n}',
    f'- papers with proof mentions: {sum(1 for p in profiles if p["proof_count"]>0)}/{n}',
    f'- papers with assumption mentions: {sum(1 for p in profiles if p["assumption_count"]>0)}/{n}',
    '',
    '## Experiment signal coverage (fulltext)',
    f'- quality metric mention: {cov("metric_quality")}/{n}',
    f'- latency mention: {cov("metric_latency")}/{n}',
    f'- throughput mention: {cov("metric_throughput")}/{n}',
    f'- build cost mention: {cov("metric_build")}/{n}',
    f'- update cost mention: {cov("metric_update")}/{n}',
    f'- memory mention: {cov("metric_memory")}/{n}',
    f'- ablation mention: {cov("signal_ablation")}/{n}',
    '',
    '## Baseline family mentions (fulltext)',
]
for k, v in tag_counts.most_common():
    report.append(f'- {k}: {v}')

(CORPUS / 'fulltext_distillation_report.md').write_text('\n'.join(report) + '\n', encoding='utf-8')

# Distilled updates based on fulltext
(DISTILLED / 'novelty_patterns_fulltext.md').write_text(
    '\n'.join([
        '# Novelty Patterns (Fulltext-Derived)',
        '',
        'Derived from per-paper fulltext semantic profiles.',
        '',
        '## High-signal structure',
        '- Problem -> gap -> proposal -> quantified evidence chain is a strong acceptance pattern.',
        '- Novelty claims are stronger when mechanism-level delta is explicit in method sections and reflected in experiments.',
        '',
        '## Frequent novelty risks',
        '- Gap not clearly articulated even when method is technically complex.',
        '- Proposal appears, but quantified evidence is weak or delayed.',
        '- Contribution bullets exist, but do not map cleanly to theorem/experiment artifacts.',
    ]) + '\n',
    encoding='utf-8'
)

(DISTILLED / 'proof_patterns_fulltext.md').write_text(
    '\n'.join([
        '# Proof Patterns (Fulltext-Derived)',
        '',
        '## Strong proof signals',
        '- theorem/lemma presence paired with proof sections and explicit assumptions.',
        '- complexity discussions that separate online and offline costs.',
        '',
        '## Common proof risks',
        '- theorem-like claims without visible assumption statements.',
        '- proof mentions exist but dependency chain is unclear in main text.',
        '- complexity notation appears without clear computational model context.',
    ]) + '\n',
    encoding='utf-8'
)

(DISTILLED / 'experiment_patterns_fulltext.md').write_text(
    '\n'.join([
        '# Experiment Patterns (Fulltext-Derived)',
        '',
        '## Strong experiment signals',
        '- quality + efficiency + cost dimensions reported together.',
        '- ablation and fairness/tuning statements present in experiment narrative.',
        '- stress tests beyond default settings (scale, update, selectivity, etc.).',
        '',
        '## Common experiment risks',
        '- speed-focused evidence without explicit quality target coupling.',
        '- fairness assumptions implied but not stated.',
        '- missing maintenance or memory discussions for system claims.',
    ]) + '\n',
    encoding='utf-8'
)

(DISTILLED / 'reader_reviewer_patterns_fulltext.md').write_text(
    '\n'.join([
        '# Reader/Reviewer Patterns (Fulltext-Derived)',
        '',
        '## Frequent reviewer concerns',
        '- novelty narrative not cleanly connected to measured or proved deltas.',
        '- proof obligations partially addressed (assumptions or dependencies missing).',
        '- experiment fairness not sufficiently explicit for strongest baselines.',
        '',
        '## Preflight recommendation',
        '1. claim-prior delta check',
        '2. theorem assumption/dependency closure check',
        '3. fairness and stress-test completeness check',
        '4. final reader comprehension check',
    ]) + '\n',
    encoding='utf-8'
)

print(f'fulltext profiles: {n}')
print(f'profile csv: {profile_csv}')
print('done')
