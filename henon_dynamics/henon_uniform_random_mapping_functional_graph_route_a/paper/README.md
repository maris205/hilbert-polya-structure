# Paper build

`main.tex` is compiled with LuaLaTeX at
`SOURCE_DATE_EPOCH=1788220800`.  Defining `\CRevisionRound` as `0`, `1`, or
`2` selects three substantive theorem stages.  The source defaults to round 2,
and `main.pdf` must be byte-identical to `main_round2.pdf`.

Each round is built twice in fresh sidecar-only temporary directories, using
two LuaLaTeX passes per build.  `COMPILE_REPORT.md` records revision hashes,
page count, font embedding/subsetting, warning scans, and fresh-build byte
identity.
