# Paper build

`main.tex` is one conditional source.  Build revision `r` with

```bash
SOURCE_DATE_EPOCH=1788220800 FORCE_SOURCE_DATE=1 TZ=UTC \
  lualatex -interaction=nonstopmode -halt-on-error \
  "\\def\\CRevisionRound{r}\\input{main.tex}"
```

Run two passes in each of two fresh directories, compare the replicas byte for
byte, and archive revisions as `main_round0_original.pdf`, `main_round1.pdf`,
and `main_round2.pdf`.  `main.pdf` must be a byte copy of round 2.  Build
sidecars remain outside the 28-file package.
