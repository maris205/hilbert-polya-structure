# C144 paper build

Compile with a fixed source epoch:

```bash
SOURCE_DATE_EPOCH=1787616000 TZ=UTC \
  latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

`main_round0_original.pdf`, `main_round1.pdf`, and `main_round2.pdf` preserve
the genuine internal review stages.  `main.pdf` is byte-identical to round 2.
