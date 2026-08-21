# C84 paper build

From this directory:

```bash
SOURCE_DATE_EPOCH=0 FORCE_SOURCE_DATE=1 TZ=UTC \
  latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The frozen package retains `main.tex`, `main.pdf`, `compile.log`, and
`COMPILE_REPORT.md`.  Auxiliary LaTeX files are excluded from the manifest.
