# Paper build

`main.tex` is a conditional three-round manuscript.  Compile with
`\CRevisionRound=0,1,2`; the final `main.pdf` is byte-identical to round 2.
The release script performs two fresh LuaLaTeX builds per round at fixed epoch,
rejects warnings and layout defects, verifies fonts/text/raster output, and
records the receipts in `COMPILE_REPORT.md` and the release manifest.
