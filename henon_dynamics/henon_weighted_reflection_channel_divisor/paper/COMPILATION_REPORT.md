# Compilation report

`latexmk` is unavailable in the execution environment, so the documented
fallback was used:

    pdflatex -interaction=nonstopmode -halt-on-error paper.tex
    bibtex paper
    pdflatex -interaction=nonstopmode -halt-on-error paper.tex
    pdflatex -interaction=nonstopmode -halt-on-error paper.tex

Result: `paper.pdf`, 5 A4 pages and 230761 bytes.  The final log has no
unresolved citations or references, no overfull/underfull box warnings, and
no fatal errors.  All 18 reported fonts are embedded.  Extracted text has no
`TODO`, `FIXME`, `XXX`, `[VERIFY]`, `??`, or `[?]` marker.  All five rendered
pages were visually inspected; equations, theorem blocks, references, and
page boundaries are legible with no clipping or overlap.

PDF SHA-256:
`da68d4cfea785e121ffff960bebf10a5c0ee5b2ace20f0b81bc81c0c9aa3aa8f`.
