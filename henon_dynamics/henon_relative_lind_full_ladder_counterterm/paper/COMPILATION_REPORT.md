# Compilation report

The manuscript was compiled with:

    pdflatex -interaction=nonstopmode -halt-on-error paper.tex
    bibtex paper
    pdflatex -interaction=nonstopmode -halt-on-error paper.tex
    pdflatex -interaction=nonstopmode -halt-on-error paper.tex

Result: `paper.pdf`, 6 A4 pages and 228818 bytes.  The final log has no
unresolved citations or references and no overfull/underfull box warnings.
All PDF fonts are embedded.

PDF SHA-256:
`b54804f45bd10f47429eb2cd43f76ff02bf6b6628aaabfdccf7f8643a9200a26`.
