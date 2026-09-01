# Paper build

`main.tex` is a single conditional source.  Set `\CRevisionRound` to 0, 1,
or 2; round 2 is the final paper.

Each archived PDF is built in a fresh temporary directory with LuaLaTeX,
two passes, `SOURCE_DATE_EPOCH=1788220800`, `FORCE_SOURCE_DATE=1`, and
`TZ=UTC`.  The release script repeats every fresh build and requires byte
identity within a round, distinct hashes across rounds, embedded subset fonts,
warning-free logs, expected extracted text, and `main.pdf` equal to
`main_round2.pdf`.
