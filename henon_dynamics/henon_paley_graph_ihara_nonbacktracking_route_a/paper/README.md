# Paper build

`main.tex` is a single deterministic LuaLaTeX source.  Define
`CRevisionRound` as 0, 1, or 2 before input to obtain the three substantively
different review rounds.  The release script performs two fresh builds of
each round with `SOURCE_DATE_EPOCH=1788393600`, compares bytes, audits logs,
fonts, extracted text, and rasterized pages, and requires `main.pdf` to equal
round 2 byte for byte.
