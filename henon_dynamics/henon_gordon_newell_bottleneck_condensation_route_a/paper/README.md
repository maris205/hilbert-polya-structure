# Deterministic paper build

`main.tex` is a single source for three substantive revisions selected by
`\CRevisionRound`:

- round 0: finite product form, complete occupancy calculus, physical flows,
  and exact time reversal;
- round 1: adds the unique/tied bottleneck normalizer and joint
  geometric–Dirichlet limit with proof;
- round 2: adds the full boundary table, executable/proof separation,
  collision audit, limitations, and strict Route-A nonclaims.

Each archived PDF is produced by two LuaLaTeX passes in a fresh directory
with `SOURCE_DATE_EPOCH=1788307200`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.
The fixed PDF trailer ID and suppressed optional metadata make unrelated
fresh builds byte-identical. The release script performs two complete fresh
builds per round and compares both with the archived bytes.

Manual reproduction for round `R`:

```bash
SOURCE_DATE_EPOCH=1788307200 FORCE_SOURCE_DATE=1 TZ=UTC \
  lualatex -interaction=nonstopmode -halt-on-error -jobname=main \
  '\def\CRevisionRound{R}\input{/absolute/path/to/paper/main.tex}'
```

Run the command twice in the same fresh directory. The release audit also
requires warning-free logs, embedded/subset fonts, expected extracted text,
and visual inspection of rendered pages.
