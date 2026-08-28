# Paper build

From this directory, with `SOURCE_DATE_EPOCH=1787875200`, run LuaLaTeX twice.
The source suppresses optional PDF metadata.  Revision PDFs are compiled from
content-distinct `CRevisionRound=0,1,2` states; the final `main.pdf` equals
`main_round2.pdf`.  The release audit requires a second pair of fresh builds
to reproduce the final PDF byte for byte, embedded/subset fonts, a clean log,
extractable text and visual inspection of every page.
