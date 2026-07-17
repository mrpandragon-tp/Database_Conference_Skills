# What Makes a Strong Database Paper

This guide synthesizes two evidence sources in this repository: semantic profiles of 80 SIGMOD/VLDB papers and 92 advisor annotations recovered from four annotated revision PDFs. The corpus shows recurring successful structures; the annotations expose the points where a technically informed reader loses trust or understanding. Treat the rules below as decision criteria, not a surface template.

## The paper contract

A strong database paper closes one coherent contract:

`important problem -> complete artifact -> mechanism -> guarantee -> evidence -> boundary`

The title, Abstract, Introduction, Method, experiments, and Conclusion must describe the same artifact at the same level. If any arrow is missing, polished prose will not repair the paper.

## 1. Give the paper one identity

- Choose one paper-level subject: a system, index, algorithm, language, optimizer, or other complete artifact.
- State a one-sentence thesis that names the problem, artifact, core mechanism, and resulting capability.
- Use one demanding main workload to expose the central challenge. Use companion workloads to establish completeness or generality.
- Make every paragraph advance a claim, explain a required mechanism, provide evidence, or state a boundary. Remove paragraphs that mainly manufacture anxiety, defend against imagined objections, or repeat the roadmap.
- Keep the core idea visible through substance. Do not add slogans to paragraphs that do not need them.

## 2. Make novelty a mechanism-level delta

- Position against the nearest strong prior work, not only weak baselines.
- State what changes in the data path, execution path, maintenance path, or correctness argument.
- Name the cost that the mechanism removes, defers, bounds, or moves offline.
- Present the artifact on its own terms. Design lineage may be cited, but the paper must not read as a patch to one prior system.
- Do not define novelty as a model insertion, a new label, or a win on one specialized metric.

For a learned database paper, answer all of these explicitly:

1. What signal is learned, and what target or ordering does it approximate?
2. Where does inference change access, routing, pruning, scheduling, or layout?
3. Which exact procedure verifies results or preserves semantics?
4. How is learned and physical state built, updated, buffered, rebuilt, or bypassed?
5. Which ablation and end-to-end result isolate the learned contribution?

If these answers are scattered or hidden behind changing names such as "accelerator," the learning contribution is not yet central.

## 3. Make the Method executable by the reader

- Show the full build, query, update, verification, stopping, fallback, and output path that the claimed artifact supports.
- Explain enough of the storage and execution substrate to establish a complete database contribution.
- Introduce each nontrivial mechanism in this order when applicable: purpose, typed objects, invariant, algorithm, running example, complexity, and correctness obligation.
- Explain pseudocode in execution order. State what each important line reads, writes, and guarantees.
- Use an example before or beside a dense definition. Connect every example value back to the symbols in the formula.
- Number displayed definitions, invariants, and bounds that carry later responsibility.
- Keep implementation constants and policy thresholds out of the main argument unless the result depends on them; report them as experimental configuration when needed.

## 4. Spend notation only when it buys precision

- Give one concept one preferred term and one symbol. Do not vary technical names for style.
- State type, scope, lifecycle, and first-use semantics for every formal object.
- Reserve time subscripts for state that actually changes with time. Do not mix enumeration, time, owner, and dimension subscripts without a clear distinction.
- Remove one-use aliases, redundant tuple components, and symbols that merely rename ordinary operations.
- Distinguish physical state from logical state, persistent state from query-local state, approximate access from exact evaluation, and exact evaluation from safe stopping.
- Keep terminology and notation identical across prose, equations, pseudocode, figures, experiments, and appendices.
- Prefer a simple familiar term over two close technical words that non-native readers may confuse.

Notation is good when it compresses a repeated dependency or makes a guarantee checkable. It is bad when the reader must decode it before learning why the object exists.

## 5. Build a claim-evidence closure

- Map every Abstract and Introduction claim to a main-paper figure, table, theorem, or measured fact.
- Organize experiments by research question and claim, not by script or metric order.
- Give each baseline an explicit role: nearest prior, latency reference, general system, specialized upper bound, or component alternative.
- Evaluate the joint operating point claimed by the paper: semantics or quality, query performance, construction, updates, memory, and ordinary operations where relevant.
- Use ablations to separate the claimed mechanism from candidate expansion, verification, buffering, and shared systems engineering.
- Analyze results with the chain `observation -> mechanism -> condition -> claim`. Do not merely repeat bar heights or speedup numbers.
- State limitations directly and locally. Do not surround claims with defensive disclaimers.

## 6. Engineer the reading experience

- Put the paragraph message in the topic sentence. Keep one principal message per paragraph.
- Introduce the proposed artifact directly: "To address this problem, we propose X, ..." Then explain the core idea before listing capabilities.
- Use short, direct English. Prefer simple sentences and stable words over dense clauses and fashionable synonyms.
- Attach each citation to the exact method, dataset, benchmark, or factual claim it supports. Avoid citation clusters at the end of a broad paragraph.
- Organize Related Work by the paper's problem and claim-prior delta. Give important methods individual treatment.
- Give each figure or table one primary reader question. Choose single-column width unless information density requires two columns.
- Place the teaser near the first complete method explanation and place result figures near their interpretation.

## 7. Revise globally, not comment by comment

- Classify each advisor or reviewer comment as local, structural, formal, experimental, or global.
- Diagnose the underlying reader failure before editing the highlighted sentence.
- After changing a term, symbol, state lifecycle, policy, output type, or claim, search the full paper, figures, algorithms, and appendix for dependent occurrences.
- Rebuild a reverse outline after structural edits and test whether every paragraph still has a necessary role.
- Keep a bilingual response ledger for substantial review rounds and preserve annotated source artifacts before recompilation.
- Treat page pressure as an allocation problem. Remove repetition, defensive prose, low-value detail, and oversized floats before removing claim support, method completeness, or essential evidence.

## Acceptance test

A manuscript is not ready until a skeptical reader can answer these questions without author assistance:

1. What important database problem is solved?
2. What complete artifact is proposed?
3. What is the one mechanism-level delta from the nearest prior work?
4. How does a request flow through build/query/update state and return a correct result?
5. Which parts are learned or approximate, and which parts establish exact semantics?
6. Which theorem or experiment supports each major claim?
7. Why are the baselines and metrics fair for that claim?
8. Where does the method work, and what are its limitations?
9. Are all terms, symbols, figures, algorithms, and appendices consistent?
10. Can a non-native English reader follow the paper without decoding avoidable vocabulary or notation?
