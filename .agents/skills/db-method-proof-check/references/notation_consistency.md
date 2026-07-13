# Notation Consistency

- Build a terminology ledger with columns for concept, preferred term, mathematical type, scope, lifecycle, and forbidden aliases.
- Give each symbol one meaning and each concept one preferred name across prose, equations, pseudocode, figures, and appendices.
- Repeat variables when explaining tuples: write "$G_t=(V_t,E_t)$, where $V_t$ is ... and $E_t$ is ...", not "where the first/second component is ...".
- State whether each object is an input, persistent index state, query-local state, or output. Explain when it is initialized and updated.
- Reserve time subscripts for quantities whose value changes with time. Reserve owner or dimension subscripts for distinctions the reader actually needs.
- Remove one-use aliases and intermediate symbols that do not shorten a later formula or proof.
- Use sets, functions, partial functions, sequences, and records according to their mathematical types. Define typed unions when one function accepts vertices and edges.
- Define every nonstandard operator, arrow, ordering relation, tie rule, and out-of-domain case at first use.
- Number every displayed equation that carries a definition, invariant, bound, or later dependency. Do not mix numbered equations with unexplained display-only formulas.
- Keep problem-definition answer objects aligned with pseudocode return values and theorem statements.
- Keep semantic helper sets separate from the public result type. If the system returns $|\sigma|$, use $\sigma$ to define membership but state, analyze, and prove the cardinality output.
- Distinguish candidate groups, materialized candidate sets, verified exact values, provisional answers, and final answers.
- Distinguish persisted physical partitions from current logical candidate groups. State how deletions, insertions, and stale bounding metadata transform one into the other.
- Distinguish verification (computing exact values) from certification (proving that unvisited state cannot change the answer).
- Distinguish the complete remaining-state collection from a selected competitive subset; write the cover or partition invariant explicitly.
- Distinguish graph updates, index-state updates, and workload-specific object updates; state which underlying data are fixed.
- Distinguish access, scan, verification, build, rebuild, compaction, flush, and fallback costs.
- Distinguish ideal real-valued bounds, their stored finite-precision representation, and the runtime scan they induce. Prove that the runtime representation is conservative.
- For every adaptive policy, record which model, partition, bound, verifier, and fallback it invokes. Do not describe one branch's mechanism as universal.
- In mutable learned indexes, distinguish latest rebuild time, base sequence, post-rebuild deltas, current logical state, and query-local state.
- Verify units, dimensions, quantifiers, empty-set behavior, insufficient-candidate behavior, and tie cases in every complexity or correctness statement.
- Use snapshot cardinalities for snapshot bounds and a sequence maximum for amortized analysis over changing state.
- Keep theorem notation aligned with algorithm notation and with the implementation path, including fallback behavior.

## Element-necessity test

For each definition, formula, pseudocode line, and figure element, ask:

1. What later claim, operation, or proof depends on it?
2. Is its type and scope explicit at first use?
3. Could the same statement be made directly with an existing symbol?
4. Does the implementation execute the operation as written?
5. Is every corner case defined?
6. Does equality at a pruning boundary preserve the declared tie rule?
7. Does the source code execute the same rounding, fallback, and policy branch described here?

If the first answer is "none", remove the element. If any other answer is "no", repair it before polishing prose.

Search the full source for deprecated names after terminology changes. Include section labels, algorithm names, figure descriptions, appendix headings, and complexity variables.
