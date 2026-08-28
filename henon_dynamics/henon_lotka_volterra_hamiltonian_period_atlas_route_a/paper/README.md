# Paper build

Build each revision with LuaLaTeX and `SOURCE_DATE_EPOCH=1787788800` after
setting `\CRevisionRound` to 0, 1, or 2.  `main.pdf` is the round-2 artifact.
The release audit requires three distinct PDFs, two byte-identical final
rebuilds, embedded/subset fonts, extractable text, and no warning or bad-box
records.
