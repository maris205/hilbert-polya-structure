# Deterministic compile report

All manuscripts were built with LuaLaTeX in fresh temporary directories under
`SOURCE_DATE_EPOCH=1788393600`, two passes per build and two independent builds
per round.  The paired bytes were identical.  Settled logs contain no LaTeX or
package warnings, overfull or underfull boxes, undefined references or
citations, rerun requests, or missing-glyph messages.  `pdffonts` reports every
font embedded and subset; every page rasterizes, and extracted text passes the
control-byte and drafting-token gate.

| round | pages | font rows | SHA-256 |
|---:|---:|---:|---|
| 0 | 2 | 11 | `8eb527baea8e37e40a70df7f3c58f0a162b2e44e4c7914fd382357516868a18a` |
| 1 | 2 | 11 | `344a9764b65290cc34ce805999b486c44d08330f5e0982cd91fe3eb391929ca9` |
| 2 | 3 | 12 | `f7d5568fb30b19a5b072f128b2998d884085b677e3529ffdca3b47f94e2f384b` |

`main.pdf` is byte-identical to round 2.  The three round hashes are distinct,
and their required extracted-text sentinels certify substantive revision
growth.
