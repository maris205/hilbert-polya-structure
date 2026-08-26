# C187 paper artifacts

`main.tex` is the final source.  `CRevisionRound=0,1,2` selects a distinct
revision-focus paragraph.  The release contains:

- `main_round0_original.pdf`
- `main_round1.pdf`
- `main_round2.pdf`
- `main.pdf`, byte-identical to round 2

LuaLaTeX is used for the bilingual abstract.  Builds use the frozen epoch
`SOURCE_DATE_EPOCH=1787702400`, `FORCE_SOURCE_DATE=1`, and UTC.  Exact commands,
hashes, logs, font checks and visual findings are in `COMPILE_REPORT.md`.
