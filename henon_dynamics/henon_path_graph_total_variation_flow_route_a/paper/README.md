# C279 paper build

`main.tex` defaults to substantive revision round 2.  Define
`\CRevisionRound` as 0 or 1 before input to build the archived revisions.
Round 0 proves convex-flow well-posedness, dissipation, and finite consensus;
round 1 adds the exact no-splitting coalescence atlas; round 2 adds the
all-time ROF identity, executable integrity receipt, source boundary, and
strict Route-A nonclaim.

Every retained PDF is built twice in two unrelated fresh directories, with
two LuaLaTeX passes per build, fixed epoch `1788220800`, UTC, and the fixed
trailer ID embedded in the source.  `main.pdf` must be byte-identical to
`main_round2.pdf`.
