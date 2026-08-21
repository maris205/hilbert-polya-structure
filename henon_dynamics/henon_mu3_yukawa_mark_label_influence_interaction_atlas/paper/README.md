# C87 paper build

Build from this directory with:

```bash
SOURCE_DATE_EPOCH=0 TZ=UTC LC_ALL=C latexmk -pdf \
  -interaction=nonstopmode -halt-on-error main.tex
```

The final deterministic-build hash, page count, and inspection results are
recorded in `COMPILE_REPORT.md` after the two isolated builds.
