# Paper build

`main.tex` contains retained revision rounds 0, 1, and 2.  For round `k`, run
two LuaLaTeX passes in each of two fresh directories with

```bash
SOURCE_DATE_EPOCH=1788220800 FORCE_SOURCE_DATE=1 TZ=UTC \
  lualatex -interaction=nonstopmode -halt-on-error -jobname=main \
  '\def\CRevisionRound{k}\input{ABSOLUTE_PATH_TO/main.tex}'
```

Fresh builds must be byte-identical.  The settled logs must be warning-free,
all fonts embedded/subset, and every rendered page visually inspected.
