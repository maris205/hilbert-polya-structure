# C185 compile report

Status: release checks complete.

## Build protocol

All manuscripts were compiled with LuaLaTeX, twice per build, under
`SOURCE_DATE_EPOCH=1787702400` and `FORCE_SOURCE_DATE=1`.  Round selection used
the package-local `\CRevisionRound` switch.  Final-pass log scans matched zero
LaTeX/package warnings, overfull or underfull boxes, badness reports, missing
characters, undefined references, fatal diagnostics, or errors.

## Released artifacts

| artifact | pages | bytes | SHA-256 |
|---|---:|---:|---|
| `main_round0_original.pdf` | 1 | 122112 | `2077903e4bf4ad9a04fc307ec6dd870362c702e1ffba04f62de6507e20632e1b` |
| `main_round1.pdf` | 2 | 138983 | `5f15f53c6f6acf893fd7754a48776fe25a970441e6c40ec6353a899795bc650b` |
| `main_round2.pdf` | 2 | 147222 | `94fd82d3077217c35edd8d92f035e91425206af838c8881dca76596bd6f38497` |
| `main.pdf` | 2 | 147222 | `94fd82d3077217c35edd8d92f035e91425206af838c8881dca76596bd6f38497` |

The final manuscript is therefore byte-identical to Round 2.  PDF text checks
also recover each round's distinct focus marker: Round 0 freezes the global
theorem, Round 1 adds local-to-global dynamics, and Round 2 locks the boundary
and Route-A evaluation.

## Independent fresh-build gate

Two newly created isolated directories each received only `paper/main.tex`.
Two fixed-epoch LuaLaTeX passes in each directory produced SHA-256
`94fd82d3077217c35edd8d92f035e91425206af838c8881dca76596bd6f38497`,
equal to one another and to the released `paper/main.pdf`.

`pdffonts` reports every final-PDF font embedded.  Both pages were rendered at
140 dpi and visually inspected: equations, bilingual abstract, table,
declarations, and reference are readable, with no clipping, overlap,
truncation, accidental blank page, or missing glyph.
