# C185 paper build

`main.tex` is a LuaLaTeX source with three content-distinct conditional
drafting rounds.  Build a round by defining `CRevisionRound` to `0`, `1`, or
`2`; the default is round 2.  The release requires:

- `main_round0_original.pdf`;
- `main_round1.pdf`;
- `main_round2.pdf`;
- `main.pdf`, byte-identical to round 2.

Builds use `SOURCE_DATE_EPOCH=1787702400` and `FORCE_SOURCE_DATE=1`.  The final
release is compiled twice in separate fresh directories and must be
byte-identical.  All fonts must be embedded, and logs must be free of warnings,
bad boxes, undefined references, and missing glyphs.

The three rounds are internal writing artifacts, not external peer review.
