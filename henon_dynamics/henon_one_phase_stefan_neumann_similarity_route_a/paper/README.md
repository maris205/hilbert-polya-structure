# C226 paper build

Set SOURCE_DATE_EPOCH=1787875200 and compile main.tex with LuaLaTeX in two
settled passes. The revision switch CRevisionRound is 0, 1, or 2; each round
contains a substantive textual change and the three PDFs are distinct.
paper/main.pdf is byte-identical to round 2. Remove .aux, .log, .toc, .out,
.fls, .fdb_latexmk, .synctex.gz, and Python bytecode before manifest closure.
