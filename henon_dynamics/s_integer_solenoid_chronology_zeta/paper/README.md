# Manuscript

**Title:** *Chronology Changes Analytic Type in a Dyadic-Solenoid Skew
Product*

- `main.tex`: master source;
- `sections/`: modular manuscript sections and appendices;
- `references.bib`: verified, cited-only bibliography;
- `main.pdf`: compiled 13-page preprint;
- `COMPILE_REPORT.md`: build and quality checks.

The local TeX installation does not provide `latexmk`, so the reproducible
fallback build is:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```
