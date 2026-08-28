# C210 compile report

The manuscript is compiled with LuaLaTeX (`-interaction=nonstopmode
-halt-on-error`) with `SOURCE_DATE_EPOCH=1787875200`.  Two fresh two-pass
builds of the final source were byte-identical.  The source sets
`\pdfvariable suppressoptionalinfo 611`, so this holds in independent build
directories:
`13c4900f1df2e4b2d7e00075adcc5913d41826e389fa789a12acd64c5c1ebd0e`.
The final PDF has three pages (242976 bytes); `pdffonts` reports 16 embedded,
subsetted fonts.  The stabilized logs contain no undefined-reference,
overfull, or underfull messages, and extracted text contains the scope literal
and Route-A tuple.  The three revision PDFs have distinct hashes and
`main.pdf == main_round2.pdf`; the exact hashes are recorded in the release
manifest.  This report records a reproducibility check, not external peer
review.
