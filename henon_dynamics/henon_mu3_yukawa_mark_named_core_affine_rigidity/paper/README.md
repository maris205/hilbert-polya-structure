# C74 paper

Build with:

```bash
SOURCE_DATE_EPOCH=0 FORCE_SOURCE_DATE=1 latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The prefreeze gate requires two isolated byte-identical clean builds and
embedded fonts.  The occurrence-overlap convention is defined in the paper
and in the evidence certificate.
