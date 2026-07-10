# Baseline Fairness

- compare at matched quality targets
- disclose memory budget differences
- include strongest relevant baselines
- label each baseline role: materialized latency reference, non-materialized search method, update-oriented index, same-stack substrate, or full database system
- report parameter tuning method for each baseline
- show non-win regimes when they exist
- compare build, update, query, and space only where methods expose comparable semantics

Interpretation rules:
- a materialized answer index may set the raw latency reference while paying different construction, update, and memory costs
- a same-stack baseline isolates the new access mechanism from shared storage
- full systems establish practical graph-operation behavior but may include general runtime overhead
- do not use "similar to baseline X" as the paper identity; explain the proposed system's own path first
