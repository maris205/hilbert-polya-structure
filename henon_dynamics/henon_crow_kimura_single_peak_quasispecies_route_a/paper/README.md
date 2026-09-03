# Paper build

`main.tex` is one conditional source.  Define `\CRevisionRound` as `0`, `1`
or `2` before input to reproduce the retained original, strengthened and final
manuscripts.  Build twice with LuaLaTeX under
`SOURCE_DATE_EPOCH=1788393600`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.

The release script performs fresh builds, warning checks, extracted-text
sentinels, font embedding/subsetting, page rasterization and equality of
`main.pdf` with the Round-2 PDF.
