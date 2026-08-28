# C213 compile report

The manuscript is compiled with LuaLaTeX (`-interaction=nonstopmode
-halt-on-error`) with `SOURCE_DATE_EPOCH=1787875200`.  Two fresh two-pass
builds of the final source were byte-identical.  The source sets
`\pdfvariable suppressoptionalinfo 611`, so this holds in independent build
directories:
`dc8d5e0e5474290f12bdd50f8a409f7b350db88ede7a3e14923df6532b50b124`.
The final PDF has two pages (145265 bytes); `pdffonts` reports 20 embedded,
subsetted fonts.  The stabilized logs contain no undefined-reference,
overfull, underfull, or missing-character messages, and extracted text
contains the scope literal and Route-A tuple.  The three revision PDFs have
distinct hashes and `main.pdf == main_round2.pdf`; exact hashes are recorded
in the release manifest.  This is an internal reproducibility report, not
external peer review.
