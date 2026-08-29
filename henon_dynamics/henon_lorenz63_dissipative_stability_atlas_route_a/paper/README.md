# Paper build

`main.tex` is the final revision-controlled source.  It defaults to revision
2.  The three released PDFs are built from the same source with
`\CRevisionRound` set to 0, 1 and 2; the conditional additions are substantive
theorem-boundary and reproducibility revisions, not metadata-only changes.

The release build uses LuaLaTeX twice per revision under
`SOURCE_DATE_EPOCH=1787875200`.  `main.pdf` is byte-for-byte equal to
`main_round2.pdf`.  Build sidecars are removed after log, font, text and visual
inspection.  See `COMPILE_REPORT.md` for the final hashes and checks.
