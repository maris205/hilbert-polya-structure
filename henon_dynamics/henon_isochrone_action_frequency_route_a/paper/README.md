# Paper build

`main.tex` contains all three substantive versions, selected by defining `\CRevisionRound` to 0, 1, or 2 before input.  With no override it builds the final round 2.

The release contract uses LuaLaTeX, two passes per build, `SOURCE_DATE_EPOCH=1788307200`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`, and two isolated builds for each round.  Temporary files remain outside this directory.  The archived outputs are:

- `main_round0_original.pdf`
- `main_round1.pdf`
- `main_round2.pdf`
- `main.pdf`, byte-identical to round 2

`COMPILE_REPORT.md` records final hashes, pages, fonts, warning checks, text checks, and visual rendering checks.
