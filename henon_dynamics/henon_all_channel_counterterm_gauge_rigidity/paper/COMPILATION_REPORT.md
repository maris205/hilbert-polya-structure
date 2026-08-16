# Compilation report

`latexmk` was not installed in the environment, so the equivalent explicit
pipeline was used:

    pdflatex -interaction=nonstopmode -halt-on-error paper.tex
    bibtex paper
    pdflatex -interaction=nonstopmode -halt-on-error paper.tex
    pdflatex -interaction=nonstopmode -halt-on-error paper.tex

The final `pdflatex` pass confirmed stable labels after the source-residual
wording repair.

Result: `paper.pdf`, 10 A4 pages, 256425 bytes.  The final log has no
unresolved citations or references and no overfull/underfull box warnings.
All 17 listed fonts are embedded.

PDF SHA-256:
`44e7b5ccad854933df0f130abe77ec63b07b6ca9ded375118b622fcda73f4a98`.
