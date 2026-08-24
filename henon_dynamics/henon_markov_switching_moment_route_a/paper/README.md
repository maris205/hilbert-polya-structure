# C117 paper

Compile from this directory with

```bash
SOURCE_DATE_EPOCH=0 TZ=UTC latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

`main.pdf` is the final artifact; the three round PDFs preserve the documented
writing/improvement stages.
