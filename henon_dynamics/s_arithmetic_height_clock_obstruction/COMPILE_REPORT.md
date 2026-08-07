# Compilation report

The manuscript was compiled from `paper/main.tex` with the system TeX Live
pdfTeX toolchain:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The release build produces `paper/main.pdf` with ten pages. The final log has
no undefined citations, undefined references, LaTeX errors, or overfull
boxes. Two harmless underfull-box warnings occur in the narrow Route-A table.

The PDF is included in `results/release_manifest.json` together with its TeX
source, bibliography, section files, documentation, code, evaluation record,
and generated numerical artifacts.
