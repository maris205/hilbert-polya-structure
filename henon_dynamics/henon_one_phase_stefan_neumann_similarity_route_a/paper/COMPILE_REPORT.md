# Compile report

Build epoch: `SOURCE_DATE_EPOCH=1787875200`; engine: LuaHBTeX 1.14.0. Each
revision was compiled in two independent fresh temporary build directories,
with two settled LuaLaTeX passes per directory. All six settled logs have no
overfull/underfull boxes, undefined references, missing citations, duplicate
destinations, or missing characters; disposable build files were removed before
the manifest audit. Fonts in the final PDF are embedded and subset.

| artifact | pages | SHA-256 |
|---|---:|---|
| `main_round0_original.pdf` | 3 | `a1e6a913892eb99058ffa6dd1ec7a61da66b1392ae7dd81ac0d6735bebdd4775` |
| `main_round1.pdf` | 3 | `592fce5cbc89a038e24d896227c75d5dbeb8e2a8a346d9b75e16c353911252f3` |
| `main_round2.pdf` | 3 | `0c75cf8d6c47e528a3967317d2437d114e54b1f3039f75690d97b7ef8f9fd327` |
| `main.pdf` | 3 | `0c75cf8d6c47e528a3967317d2437d114e54b1f3039f75690d97b7ef8f9fd327` |

The round PDFs are distinct and `main.pdf` is byte-identical to round 2.
`pdfinfo` reports three pages for the final manuscript and `pdffonts` reports
all 22 listed fonts with `emb=yes` and `sub=yes`. Extracted text contains the
Stefan, Neumann, Lambert, energy, `A3_FAIL`, `ROUTE_A_REJECTED`,
`NO_BAD_EULER_OR_ROOT_NUMBER`, zero-latent, and source heat clock is not target
continuation/divisor/counting law locks.

The declaration block is deliberately placed after `\clearpage`; a 120-dpi
visual inspection of all three final pages found no clipping, overlap, broken
glyph, or truncated declaration.

The independent checker reports 308 assertions, SymPy reports 12 symbolic
identities (including the lambda-factor reversion check), replay is byte-stable, and the hostile suite rejects 22/22
repaired/stale mutations.
