# Collaborative LaTeX Workflow

## Source-of-truth check

Before editing, identify the newest source among local Git, the shared Git host, and Overleaf. Compare commit IDs and file diffs; do not infer content changes from commit messages alone.

Recommended order:

1. Fetch or pull Overleaf source.
2. Confirm the working tree and remote heads.
3. Preserve local user changes.
4. Edit source.
5. Compile locally and inspect the PDF.
6. Commit the exact source changes.
7. Push the shared Git remote and Overleaf.
8. Verify all heads match.

## Comments and annotated PDFs

- Overleaf comments and reply threads are web collaboration metadata. Git synchronization should not resolve or delete them.
- A comment action can create an empty Overleaf Git commit. Inspect `git show --stat` and file diffs before merging it as a source change.
- Save an annotated PDF before recompiling. A LaTeX build replaces the generated PDF and its annotations.
- Extract annotations with author, page, text, rectangle, and nearby words so comments map to exact source passages.

## Proxy isolation

If a global proxy points to an inactive local port, bypass it only for the Overleaf command:

- clear command-scoped Git `http.proxy` and `https.proxy`;
- temporarily clear process-scoped `HTTP_PROXY`, `HTTPS_PROXY`, and `ALL_PROXY` variants;
- restore the process environment after the command;
- do not disable or rewrite the system-wide proxy.

## PDF and build state

- Keep the local compiled PDF current even when Git ignores it.
- Measure the main-paper page count separately from references and appendix pages.
- Inspect affected pages visually after meaningful text, float, or sizing changes.
- Treat undefined references, missing citations, overfull boxes, clipped figures, and unreadable labels as blocking.

## Cross-platform rules

- Resolve skill and tool paths from the active environment; do not hard-code one Windows or macOS home directory.
- Keep OS-specific sync commands in scripts or project instructions.
- Record stable decisions in `AGENTS.md` or an equivalent project state file so context compression and machine switching do not reset the process.
