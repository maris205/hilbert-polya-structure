# Paper build

`main.tex` is a single deterministic LuaLaTeX source parameterized by
`\CRevisionRound`.

- round 0: frozen finite owner and strict chamber;
- round 1: parabolic walls, exact length and all degenerate faces;
- round 2: independent executable reconstruction, source/collision audit and
  Route-A disposition.

Each archived PDF is built twice from separate fresh directories with
`SOURCE_DATE_EPOCH=1788307200`, two LuaLaTeX passes per build, and must be
byte-identical to both fresh reconstructions.  `main.pdf` equals round 2.
The release gate also checks every round's settled log, embedded/subset fonts,
page count, extracted semantic text, and exact revision hash.
