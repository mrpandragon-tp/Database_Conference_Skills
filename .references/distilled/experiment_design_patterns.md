# Experiment Design Patterns for Top DB Venues

## Core evidence dimensions
- Quality metric (recall/accuracy) + efficiency metric (latency/throughput).
- Build/indexing cost, update cost, and memory footprint.
- Fair tuning disclosure and repeated-run policy.

## Typical stress axes
- Data scale and dimensionality.
- Update ratio and stream dynamics.
- Filter selectivity/correlation where filtering is claimed.
- Distributed scale-out where distributed claims are made.

## Checklist
- No speedup claim without paired quality target.
- No quality claim without corresponding efficiency cost.
- No main claim supported only by appendix-only experiments.
