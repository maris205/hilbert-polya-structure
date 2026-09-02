# Manuscript builds

`main.tex` uses `\CRevisionRound`:

- round 0: exact finite recurrence and complete hitting law;
- round 1: Poisson isolated vertices, all-other-component bound, and Gumbel;
- round 2: small/terminal/rounding faces, evidence, nonclaims, repository
  collision boundary, Route A, and source/AI-use statements;
- `main.pdf`: byte-identical to round 2.

The release script performs fresh double LuaLaTeX builds at frozen epoch
`1788393600`, checks warning-free logs, embedded/subset fonts, text sentinels,
all rendered pages, and three distinct round hashes.
