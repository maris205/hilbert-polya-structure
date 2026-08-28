# C218 paper build

Set SOURCE_DATE_EPOCH=1787788800 and compile main.tex with LuaLaTeX.  The
revision switch CRevisionRound is 0, 1, or 2; all three PDFs remain distinct
and main.pdf is byte-identical to round 2.  Sidecars are removed before
manifest closure.  The final audit checks fixed-epoch reproducibility, page
count, embedded/subset fonts, extracted theorem phrases, and settled
warning/bad-box logs.
