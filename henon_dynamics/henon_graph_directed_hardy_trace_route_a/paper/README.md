# Paper build

Build from the package root with a fixed source date:

```bash
SOURCE_DATE_EPOCH=1787529600 TZ=UTC latexmk -pdf -interaction=nonstopmode -halt-on-error paper/main.tex
```

`main_round0_original.pdf`, `main_round1.pdf`, and `main_round2.pdf` preserve
the two internal improvement passes.  `main.pdf` is the final release copy.
