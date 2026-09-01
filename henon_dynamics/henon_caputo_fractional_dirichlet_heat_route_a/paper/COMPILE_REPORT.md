# HCS-C277 compile report

All three manuscript stages were built with LuaLaTeX under
`SOURCE_DATE_EPOCH=1788220800`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.  Each
stage received two LuaLaTeX passes in each of two fresh temporary build
directories.  The two fresh outputs were byte-identical at every stage.

| Stage | Pages | Bytes | SHA-256 |
|---|---:|---:|---|
| `main_round0_original.pdf` | 2 | 130501 | `cf3a8fb6ba9fd650836e85f2085f54670fe82c9178cd9a084d7cfe4b8be50b0a` |
| `main_round1.pdf` | 2 | 150207 | `b06650e2bff0c629c93c5e020120148279b3ab7038e7852e0a4b5ab20e116180` |
| `main_round2.pdf` | 3 | 169355 | `c3efe7030d157fbbe1a7b0a45b2bda73973a8bc5070af9968facef32297fc169` |
| `main.pdf` | 3 | 169355 | `c3efe7030d157fbbe1a7b0a45b2bda73973a8bc5070af9968facef32297fc169` |

The settled logs are warning-free: no LaTeX warning, overfull or underfull
box, undefined reference, multiply-defined label, or rerun request remains.
`pdffonts` reports 22 fonts; every font is embedded and subset.  A rendered
three-page visual audit found no clipped equations, collisions, missing
glyphs, or unreadable material.  The three revision PDFs have distinct
hashes, and `main.pdf` is byte-for-byte identical to the Round-2 PDF.

Round 0 establishes the frozen owner, spectral solution, and subordination.
Round 1 adds the non-semigroup category theorem and sharp smoothing and
Schatten endpoints, with the smoothing iff explicitly quantified on
`theta>=0` and the bounded negative powers separated as out of domain.  Round
2 adds the operator-norm resolvent limit, the
classical heat boundary, executable certificate, and Route-A decision.
