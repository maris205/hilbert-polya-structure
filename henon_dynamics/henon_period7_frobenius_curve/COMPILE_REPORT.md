# Paper compile report

**Date:** 2026-08-08

**Output:** `paper/main.pdf`

**Pages:** 8

**Final size:** 231,216 bytes

The manuscript was compiled with:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Checks:

- no undefined citation, reference, or multiply defined label;
- no overfull or underfull box warning in the final log;
- all PDF fonts are embedded, including one harmless custom Type-3 glyph set;
- title page, generic-neighbor theorem, oriented-cover corollary, and genus
  theorem pages were visually inspected;
- paper title, abstract, theorem conventions, artifact names, and Route-A
  boundary agree with the release documents.
