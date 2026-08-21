# C97 paper

`main.tex` is the complete finite theorem note.  Build twice with a fixed
environment and compare hashes:

```text
SOURCE_DATE_EPOCH=1787300000 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C pdflatex -interaction=nonstopmode -halt-on-error main.tex
SOURCE_DATE_EPOCH=1787300000 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The release checks byte identity across two isolated build directories,
embedded fonts, page count, extracted text, references, and box warnings.
