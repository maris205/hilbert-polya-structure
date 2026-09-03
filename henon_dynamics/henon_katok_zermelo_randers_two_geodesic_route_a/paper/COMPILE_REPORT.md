# HCS-C339 compile report

All three revisions were built with LuaLaTeX twice from fresh directories at
`SOURCE_DATE_EPOCH=1788393600`; each pair was byte-identical.

| revision | pages | font rows | SHA-256 |
|---|---:|---:|---|
| round 0 | 2 | 12 | `df9ac03abf38b99b294ddf4ab29e8847a176a219028343534aae3a934354e6cb` |
| round 1 | 2 | 12 | `1d5bc3208c06c194385f9bf18cc283dfa7385d7759f034d15af40f633f7dbdc1` |
| round 2/final | 3 | 12 | `7cd9174cfd2ec0294e043e28e244b86edbddfd96cc92984922d11593cb184979` |

Settled logs contain no LaTeX/package warning, overfull/underfull box,
undefined reference/citation, rerun request, or missing-character report.
All fonts are embedded and subset.  `pdftotext -layout` contains the
round-specific sentinels and no forbidden control byte or drafting literal;
every page passes `pdftoppm` rasterization.  `main.pdf` is byte-identical to
round 2.
