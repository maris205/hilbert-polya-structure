# Paper build

`main.tex` is a deterministic three-round LuaLaTeX source.  The default is
round 2.  To build one round in an isolated directory, run twice with

```bash
lualatex -interaction=nonstopmode -halt-on-error -jobname=main \
  '\def\CRevisionRound{R}\input{/absolute/path/to/paper/main.tex}'
```

using `SOURCE_DATE_EPOCH=1788307200`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.
The release script performs two fresh two-pass builds for every round, checks
settled logs, embedded/subset fonts, extracted-text contracts, page counts,
and byte identity against the retained PDFs.
