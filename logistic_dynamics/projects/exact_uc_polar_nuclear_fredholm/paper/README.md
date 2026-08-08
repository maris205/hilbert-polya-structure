# Manuscript

This generic-article manuscript documents the analytic determinant stage of
`LOG-0001`. It intentionally makes no Riemann-zero calculation or Riemann
Hypothesis claim. The compiled four-page manuscript is `main.pdf`.

## Build

```bash
cd paper
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

No external citations are used; `references.bib` is retained as an explicit
empty bibliography ledger.
