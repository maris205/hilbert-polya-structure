# C98 paper

Build `main.tex` twice in isolated directories under a fixed environment:

```text
SOURCE_DATE_EPOCH=1787300000 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C pdflatex -interaction=nonstopmode -halt-on-error main.tex
SOURCE_DATE_EPOCH=1787300000 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The final audit checks byte identity, embedded fonts, page count, extracted
text, unresolved references, and serious box warnings.
