# C217 paper build

Set SOURCE_DATE_EPOCH=1787788800 and compile main.tex with LuaLaTeX.
The revision switch CRevisionRound is 0, 1, or 2; the release keeps all three
distinct PDFs and makes main.pdf byte-identical to round 2.  Build sidecars are
removed before the manifest is generated.  The final audit checks page count,
embedded/subset fonts, extracted text, fixed-epoch reproducibility, and
warning/bad-box logs.
