# Paper build

`main.tex` uses `\CRevisionRound=0,1,2` to expose three substantive revisions.  Compile in a fresh directory with two LuaLaTeX passes, `SOURCE_DATE_EPOCH=1788393600`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.  The release script repeats each build twice, checks exact bytes against the checked-in PDF, rejects warnings and layout defects, verifies embedded/subset fonts, extracts text, and rasterizes every page.  `main.pdf` must equal `main_round2.pdf` byte for byte.
