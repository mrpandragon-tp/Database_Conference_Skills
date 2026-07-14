# Advisor-Comment Revision Protocol

Use this protocol when comments arrive through an annotated PDF, Overleaf, or a reply thread.

## Preserve and extract

- Preserve the annotated artifact before compiling or overwriting the PDF.
- Extract comment author, page, comment text, annotation rectangle, and nearby paper text.
- Treat comments and replies anchored at the same location as one discussion thread unless they target different passages.
- Separate local comments (wording or one sentence) from structural comments (paragraph role, section order, or paper identity).

## Diagnose before editing

For each thread, record its target text, whether it is local or structural, the underlying reader failure, and the planned sentence/paragraph/section/figure change. Do not apply comments one sentence at a time when several comments point to the same structural problem. Build a reverse outline first.

Keep the response logic out of the revised paper. The response ledger may say that a symbol is persistent state rather than a query parameter, or that a subscript is omitted because an algorithm reads one snapshot. The paper should absorb that reasoning into the mechanism itself: describe when the state changes, what the algorithm reads and writes, and how logical and physical state are synchronized. Sentences that sound like direct answers to a highlighted comment usually need one more rewrite.

When a notation comment reveals that the symbol has competing conventions in the literature, prefer a standard explicit construction over a local defense. For example, optimize over a defined set of paths rather than using a reachability arrow as though it were a path object. Record the rejected convention and rationale in the response ledger, not in the paper.

## Introduction-specific rules

A strong advisor-facing Introduction should make these paragraph roles visible without labels:

1. General problem and requirement.
2. Concrete difficult instance.
3. Existing approaches and the unresolved problem; state the main failure in the first sentence.
4. Relevant technical opportunity and why it is insufficient by itself.
5. Directly introduce the proposed artifact in the first sentence: "To address this problem, we propose X, ..."
6. Explain the first core design idea.
7. Explain the second core design idea.
8. Summarize evidence and contributions.

Checks:

- Each topic sentence summarizes its paragraph.
- The first proposal sentence defines the method name, abbreviation, artifact type, and target problem.
- The method paragraph explains the core idea before listing capabilities.
- Long method and evidence paragraphs are split by message.
- Input relationships are explicit. If objects are attached to a graph, do not list graph and objects as unrelated peer inputs.
- The teaser figure appears near the proposal and is referenced in the text.

## Close the loop

1. Map every comment thread to a concrete change or a reasoned non-change.
2. Re-read without comments and write a one-line reverse outline for every paragraph.
3. Check title, Abstract, Introduction, contributions, and Method for the same paper-level subject.
4. Compile and visually inspect affected pages, including float placement and page transitions.
5. Keep online comments unresolved unless the author explicitly asks to resolve them.

A successful revision reads as a coherent new section, not a sequence of patches around highlighted phrases.

## Formal-method comments

When comments target definitions, equations, pseudocode, or figures, use an element-level audit rather than a wording pass.

For every introduced object, record:

- its mathematical type;
- whether it is input, persistent index state, query-local state, or output;
- when it is created, read, updated, and discarded;
- why the reader needs it;
- where its exact semantics are first stated.

Delete an object if it is only an alias, appears once, or does not simplify a later statement. If it remains, repeat the symbol when explaining a tuple and define every operator, subscript, arrow, ordering rule, fallback, and corner case at first use.

Explain algorithms in execution order. A reader should be able to reconstruct each line from the prose, including the state read, state written, exact operation, and stopping condition. Apply the same test to figures: every box, label, abbreviation, arrow, color, and omitted subscript needs a meaning in the caption or nearby text.

When one comment exposes a representation or lifecycle gap, audit the same distinction globally:

- physical base structure versus current logical query unit;
- latest-rebuild state versus post-rebuild deltas;
- complete remaining state versus the subset selected this round;
- ideal mathematical bound versus stored rounded bound versus runtime scan;
- group-level certification bound versus verifier-internal acceleration;
- one adaptive policy versus mechanisms shared by all policies.

For mutable learned structures, explain the lifecycle operationally: which logical change is visible immediately, which physical component is updated locally, which delta is buffered, and which global organization is rebuilt in batches. This is more informative than merely labeling an object as build-time, persistent, or query-time state.

Do not repair a paper--implementation mismatch by inventing a fallback in prose. Read the implementation branch, state its real behavior, and either align the paper, align the code, or record a concrete unresolved implementation issue. Equality boundaries deserve a separate audit whenever the paper declares deterministic tie handling.

Audit output granularity as well as internal mechanics. A semantic set may be introduced to define exact matches, but if the implementation and experiment return only its cardinality, remove claims, examples, and complexity statements for an unimplemented identifier-returning API.

## Bilingual response ledger

For each annotation, record:

1. stable comment ID and target passage;
2. comment intent in English and Chinese;
3. original text or behavior;
4. revised text or behavior;
5. rationale in English and Chinese;
6. global follow-through, such as terminology searches, proof updates, figure repairs, and compilation checks.

Add a clearly separated implementation-audit note when source inspection reveals a correctness or reproducibility risk that was not itself an annotation. State whether code was changed; do not bury the risk inside a polished response.

Record annotation-state events such as `Accepted` or `None` for completeness, but do not invent a textual revision for them. Keep the annotated source PDF unchanged and separate from the newly compiled PDF.
