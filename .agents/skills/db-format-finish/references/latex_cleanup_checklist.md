# LaTeX Cleanup Checklist

- no undefined references
- no duplicate labels
- no overfull/underfull critical warnings
- stable macros and notation
- bibliography style and ordering consistent
- every substantive displayed equation uses a numbered `equation`, `align`, or equivalent environment
- no forced `h` placement for ordinary two-column floats; prefer `[tb]` for single-column figures/tables and `[t]` for double-column figures unless a venue template requires otherwise
- each figure is cited near its first substantive use
- every figure symbol, abbreviation, color, arrow, and omitted subscript agrees with the body text and caption
- physical-structure labels and query-time logical terms are not used as visual synonyms (for example, partition versus candidate group)
- pseudocode symbols and return values agree with the surrounding prose and appendix
- mathematical residuals/bounds and stored rounded values are visually and textually distinguished
- annotated source PDFs are preserved before recompilation
- affected pages are rendered and visually checked after edits, not only compiled
- deferred figures do not appear after the References heading; insert and verify a float barrier when necessary
- final checks report main-text, reference, and appendix page starts separately
- source-wide searches confirm that deprecated terms, stale aliases, `\[...\]`, and restrictive float specifiers are gone
