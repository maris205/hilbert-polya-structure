# Compilation report

The manuscript was compiled with:

    pdflatex -interaction=nonstopmode -halt-on-error paper.tex
    bibtex paper
    pdflatex -interaction=nonstopmode -halt-on-error paper.tex
    pdflatex -interaction=nonstopmode -halt-on-error paper.tex

Result: paper.pdf, 4 A4 pages. Final log has no unresolved citations or
references and no overfull/underfull box warnings.

PDF SHA-256:
4c89c65983c0d867bd8bb3130c5176705d8e1d05876d7cc67f8b26c77433a5b1.
