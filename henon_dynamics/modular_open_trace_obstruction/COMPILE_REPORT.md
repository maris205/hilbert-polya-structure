# Paper compile report

**Date:** 2026-08-07

**Output:** `paper/main.pdf`

**Pages:** 11

**Final size:** 290,267 bytes

`latexmk` is not installed in the workspace, so the documented fallback was
used:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Checks:

- no undefined citation or reference;
- no multiply defined labels;
- no overfull boxes;
- one harmless underfull bibliography line in the long local Hénon title;
- all PDF fonts are embedded, including the one custom Type-3 glyph set;
- first page and object-wise Route-A table page visually inspected;
- paper title, abstract scope, artifact names, and final object-wise verdict
  agree with the release documents.
