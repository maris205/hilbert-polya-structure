# Compilation report

`latexmk` is unavailable in the execution environment, so the documented
fallback was used:

    pdflatex -interaction=nonstopmode -halt-on-error paper.tex
    bibtex paper
    pdflatex -interaction=nonstopmode -halt-on-error paper.tex
    pdflatex -interaction=nonstopmode -halt-on-error paper.tex

Result: `paper.pdf`, 5 A4 pages and 261877 bytes. The final log has no
unresolved citation/reference, overfull, underfull, package-warning, or fatal
error. All 22 reported fonts are embedded. Extracted text has no `TODO`,
`FIXME`, `XXX`, `[VERIFY]`, `??`, or `[?]` marker. The source tree has no
carriage-return bytes. All five pages were rendered and visually inspected;
the title, equations, proof endings, claim table, references, and page
boundaries are legible with no clipping or overlap.

PDF SHA-256:
`56c92875973cbad5a76bcc2e3aa07c367b0eaa61b88c5f2571edb002e463061c`.
