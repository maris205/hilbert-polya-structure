# HCS-C20 compilation report

**Date:** 2026-08-08

The manuscript was built from `paper/main.tex` with

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Final artifact: `paper/main.pdf`

- pages: 10;
- PDF version: 1.5;
- all fonts embedded;
- no undefined citations or references;
- no overfull or underfull box warnings; and
- no LaTeX warnings in the final log.

The mathematical body ends before the bibliography; the reproducibility
appendix occupies the final two pages.
