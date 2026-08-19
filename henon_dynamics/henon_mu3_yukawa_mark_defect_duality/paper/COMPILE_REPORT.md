# C68 compile report

The final build used

```text
SOURCE_DATE_EPOCH=0 latexmk -C
SOURCE_DATE_EPOCH=0 latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Two clean builds are byte-identical.  The PDF is two pages with no undefined
references, citations, overfull or underfull boxes, TODO/FIXME/VERIFY markers,
or non-embedded fonts.  PDF SHA-256:

```text
0d466021cb0fd3f764afb3f9322ed5079636a4d1410c41d739cb1246709ab072
```
