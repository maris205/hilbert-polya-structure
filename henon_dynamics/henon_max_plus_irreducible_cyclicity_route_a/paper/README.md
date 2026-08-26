# C188 paper artifacts

`main.tex` is the release source.  It accepts a command-line
`\CRevisionRound` value:

- `0` builds `main_round0_original.pdf`;
- `1` builds `main_round1.pdf`;
- `2` builds `main_round2.pdf` and the byte-identical `main.pdf` release.

The three versions differ in their revision-focus paragraph; they are not
renamed copies.  `COMPILE_REPORT.md` records the frozen epoch, hashes,
deterministic rebuilds, log scan, font inspection and rendered-page inspection.
