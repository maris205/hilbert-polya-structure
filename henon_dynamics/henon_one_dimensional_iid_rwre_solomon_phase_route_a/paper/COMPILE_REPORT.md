# Compile report

All three revisions were built twice in fresh temporary directories with
LuaHBTeX/LuaLaTeX, `SOURCE_DATE_EPOCH=1788393600`, `FORCE_SOURCE_DATE=1`, and
`TZ=UTC`.  Each pair was byte-identical.  The settled second-pass logs contain
zero LaTeX/package warnings, overfull boxes, underfull boxes, undefined
references/citations, rerun requests, or missing-character reports.

| revision | pages | font rows | SHA-256 |
|---|---:|---:|---|
| round 0 | 2 | 19 | `4ec713f566d02d689d192dd785f3989bbecc6f54362b3636545678eff4531fe5` |
| round 1 | 3 | 20 | `79566d244d7ec0d732fc4c104c2d55f90e66783c922e0945bc8376ac969e2ae9` |
| round 2 | 3 | 20 | `4a3640e6f4ecaed268346c9844d00b2f2032dd0237591ab13fe3762b2095ac5a` |

Every reported font row is embedded and subset.  `pdftotext -layout` contains
the correct revision sentinel and no forbidden control bytes, `qquad`, `??`,
draft markers, or missing-glyph text.  Every page was rasterized successfully
with `pdftoppm` and visually inspected for clipping, collisions, malformed
mathematics, and sparse orphan pages.  `main.pdf` is byte-identical to
`main_round2.pdf`.
