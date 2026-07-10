# Lessons from Iterative SIGMOD-Style Revision

These rules distill repeated paper revisions, reader tests, advisor feedback, formal audits, experiment redesign, figure iteration, and LaTeX collaboration. Apply the judgment rules rather than copying a project-specific story.

## Protect the paper identity

- Choose the paper-level subject before drafting: system, index, algorithm, language, or optimizer. Keep it stable in the title, Abstract, Introduction, contributions, Method, experiments, and Conclusion.
- Do not let one internal mechanism become the paper subject unless it is the actual contribution. Routing, filtering, caching, and verification should explain how the artifact works, not silently rename it.
- Describe the proposed artifact on its own terms. Avoid framing the paper as an upgrade to one prior system or an attempt to beat one specialized baseline on its strongest metric.
- State novelty as a mechanism-and-capability delta. A new label for a familiar filter-and-verify pipeline is insufficient.
- For multiple workloads, choose one demanding main workload and explain why it exposes the central challenge. Use companion workloads to show system completeness.

## Build the Introduction by paragraph role

A robust Introduction often follows this order:

1. General setting and system requirement.
2. A concrete demanding instance that makes the cost visible.
3. Existing approaches and the unresolved problem, with the main failure in the topic sentence.
4. A related technical opportunity and why it cannot be applied directly.
5. A direct proposal sentence: "To address this problem, we propose X, ..." Define the complete artifact and core idea here.
6. First method idea and why it solves part of the problem.
7. Second method idea, often correctness, updates, or system integration.
8. Evidence summary and contributions.

Additional rules:

- The first sentence of each paragraph must summarize that paragraph.
- Keep one principal message per paragraph. Split paragraphs that mix architecture, algorithms, updates, limitations, and results.
- At the first method mention, make the name and artifact type unmistakable. Optional emphasis is acceptable once.
- Express containment explicitly. Do not list a graph, attached objects, and a query as unrelated peer inputs.
- Explain the core mechanism before listing every capability.
- Place the teaser figure near the first complete method explanation, ideally by page two when the layout permits.

## Make Method self-contained

- Explain enough storage and execution substrate to establish a complete database artifact. Cite design lineage, but describe the operations implemented by the proposed system.
- Separate the learned or heuristic access mechanism from the exact semantics that define the answer.
- Show the full build, query, verification, update, and fallback path.
- Pair each nontrivial mechanism with the right object: definition, invariant, pseudocode, complexity, running example, or structure figure.
- State compact asymptotic results beside the corresponding algorithm. Keep detailed derivations supplementary while making the main paper logically self-contained.
- Audit formulas, pseudocode, proofs, captions, and prose for one-name-per-concept consistency.

## Make experiments prove the story

- Organize experiments by research questions, not script execution order.
- Give each baseline a role. A materialized-query method may be a latency reference rather than a method a dynamic system must beat on raw query time.
- Cover the joint operating point claimed by the paper: correctness/quality, query cost, construction, updates, memory, and ordinary operations when relevant.
- Use one aggregation policy per metric family. Do not mix mean, geometric mean, and median without a reason. Strengthen weak repetition or query counts rather than hiding them.
- Make ablations attribute gains to the claimed innovation. Separate learning from candidate expansion, verification, buffering, and shared systems engineering.
- Merge only metrics that answer the same reviewer question.
- Use grouped bars for cross-dataset summaries and line charts for parameter or scale sweeps. Use logarithmic axes when magnitude gaps hide values.
- Keep evidence for every major claim in the main paper when appendix-only experiments are not allowed.

## Design figures for two-column reading

- Prefer structure diagrams for index state and storage layout; use flowcharts only when sequence is the main point.
- Use single-column figures for compact summaries and double-column width only when information density requires it.
- Keep figure text close to body-text size after scaling.
- Keep the proposed method's color or marker stable across experiment families.
- Keep captions concise and add accurate accessibility descriptions.
- Place figures near the paragraph that interprets them.

## Keep citations and prose local

- Attach citations immediately to the method, dataset, benchmark, or claim they support.
- Preserve logical connectors when reducing AI-like prose. Remove inflated summaries without turning the argument into disconnected short sentences.
- Prefer direct technical statements over unsupported slogans such as "the broader lesson."
- During Overleaf collaboration, keep each prose paragraph as one logical source line when practical; do not flatten equations, pseudocode, tables, or structured environments.

## Treat collaboration state as reproducibility

- Identify the source of truth among local files, GitHub, and Overleaf before editing.
- Pull, inspect, edit, compile, commit, and push in a fixed order. Keep the local PDF current even when it is ignored by Git.
- Overleaf comments are collaboration metadata. A comment-only edit can produce an empty Git commit; inspect file diffs before treating it as a conflict.
- Preserve an annotated PDF before recompiling because the build replaces its annotations.
- Bypass an inactive proxy only for the affected remote command and restore the process environment. Do not change machine-wide proxy settings.
- Keep project instructions portable across Windows and macOS; resolve skill locations from the active environment.

## Run two final audits

1. Reader/reviewer audit: Is novelty obvious, self-proved, and supported? Can a reader explain the method after the Introduction and Figure 1?
2. Formal consistency audit: Are there contradictions, renamed concepts, symbol mismatches, unsupported guarantees, or serious grammatical errors across formulas, proofs, pseudocode, and prose?

Report fatal and major issues first. Do not fill reviews with optional synonym replacements.
