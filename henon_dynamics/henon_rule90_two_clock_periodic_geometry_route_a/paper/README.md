# C145 paper build

Compile deterministically with:

```bash
SOURCE_DATE_EPOCH=1787616000 TZ=UTC \
  latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The three round PDFs preserve the initial draft and two genuine internal
review repairs.  `main.pdf` is byte-identical to `main_round2.pdf`.
