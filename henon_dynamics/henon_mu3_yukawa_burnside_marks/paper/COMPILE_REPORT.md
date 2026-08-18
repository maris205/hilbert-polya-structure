# C64 compile report

Command:

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The final build completed with no undefined citations or references and no
LaTeX errors.  With `SOURCE_DATE_EPOCH=0`, two clean builds were byte
identical.  The PDF has 3 pages, letter size, and SHA-256
`2228e29506b39f2fb0aaa45ddb38b5739caef786ba5695ca1091cffdc52c523d`.
