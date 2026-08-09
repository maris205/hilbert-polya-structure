# Manuscript build

The system does not provide `latexmk`, so the verified build uses two direct
`pdflatex` passes:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The manuscript is a standalone generic article.  It contains no external
citations and preserves the narrow theorem boundary of the stage.

