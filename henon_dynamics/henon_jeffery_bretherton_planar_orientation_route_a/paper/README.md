# Paper build

`main.tex` contains all three retained revisions.  Build round `k=0,1,2` with

```bash
SOURCE_DATE_EPOCH=1788220800 FORCE_SOURCE_DATE=1 TZ=UTC \
  lualatex -interaction=nonstopmode -halt-on-error -jobname=main \
  '\def\CRevisionRound{k}\input{ABSOLUTE_PATH_TO/main.tex}'
```

Run two passes in each of two fresh directories.  The two builds for a given
round must be byte-identical.  `main.pdf` is an exact copy of
`main_round2.pdf`; all fonts must be embedded/subset and `pdftotext` must
recover the theorem, evidence, citations, tuple, and scope literal.
