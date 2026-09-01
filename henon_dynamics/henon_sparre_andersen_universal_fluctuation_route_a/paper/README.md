# Paper build

`main.tex` is compiled with LuaLaTeX at
`SOURCE_DATE_EPOCH=1788134400`.  Defining `\CRevisionRound` as `0`, `1`, or
`2` selects the three substantive paper stages.  The final source defaults to
round 2, and `main.pdf` must be byte-identical to `main_round2.pdf`.

Each round is built twice from fresh sidecar-free directories with two
LuaLaTeX passes per build.  `COMPILE_REPORT.md` records hashes, page count,
font embedding, warning scans, and deterministic equality.
