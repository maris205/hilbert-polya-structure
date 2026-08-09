# Manuscript build

Build the standalone generic article with two direct `pdflatex` passes:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The manuscript uses no external citations.  Its numerical table is a display
of the frozen scalar certificate; the machine-readable outward intervals are
kept in `../artifacts/log_0001_lower_growth/lower_growth_certificate.json`.
