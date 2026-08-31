# Paper build

`main.tex` is the authoritative source.  It defines a fixed LuaTeX trailer ID
and revision-gates substantive content with `\CRevisionRound`.

Each of rounds 0, 1, and 2 is compiled twice in separate fresh directories
with:

```text
SOURCE_DATE_EPOCH=1788048000
FORCE_SOURCE_DATE=1
TZ=UTC
```

The two builds of each round must be byte-identical.  The three retained
round PDFs must have distinct hashes, and `main.pdf` must equal
`main_round2.pdf`.  Final acceptance also requires 2--6 pages, embedded and
subsetted fonts, text extraction, visual inspection, and no second-pass
layout/reference warning.
