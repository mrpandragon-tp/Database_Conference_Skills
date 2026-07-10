# Advisor-Comment Revision Protocol

Use this protocol when comments arrive through an annotated PDF, Overleaf, or a reply thread.

## Preserve and extract

- Preserve the annotated artifact before compiling or overwriting the PDF.
- Extract comment author, page, comment text, annotation rectangle, and nearby paper text.
- Treat comments and replies anchored at the same location as one discussion thread unless they target different passages.
- Separate local comments (wording or one sentence) from structural comments (paragraph role, section order, or paper identity).

## Diagnose before editing

For each thread, record its target text, whether it is local or structural, the underlying reader failure, and the planned sentence/paragraph/section/figure change. Do not apply comments one sentence at a time when several comments point to the same structural problem. Build a reverse outline first.

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
