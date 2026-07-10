# Experiment Checklist

Story and organization:
- each research question maps to a major claim
- each figure/table has one primary reviewer question
- the main workload exposes the central challenge
- companion workloads demonstrate system completeness or generality
- redundant metrics are merged only when they answer the same question

Core metrics:
- recall/accuracy
- latency/throughput
- build cost
- update cost
- memory footprint

Reporting:
- hardware/software config
- repeated runs and randomness handling
- one aggregation policy per metric family
- sufficient queries/runs for critical results
- baseline tuning policy
- raw data retained for reproducibility

Ablation:
- remove the claimed learning/algorithmic component directly
- separate learned organization from candidate expansion, verification, update buffering, and shared substrate
- explain a small delta precisely or strengthen the experiment
- do not call lower build/update cost a win if useful state was removed and query quality collapsed

Stress tests:
- data scale and dimensionality
- update ratio
- filter selectivity (if filtering)
- distributed scaling (if distributed claim)
- sparse/dense or weak-correlation boundaries when learned access depends on locality

Presentation:
- grouped bars for cross-dataset summaries
- lines for parameter and scale sweeps
- logarithmic axes when magnitude gaps hide values
- main-paper evidence for every major claim
