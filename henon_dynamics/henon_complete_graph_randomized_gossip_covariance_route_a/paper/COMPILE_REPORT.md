# Deterministic paper compile report

The three revisions were compiled with LuaLaTeX, two passes per build,
`SOURCE_DATE_EPOCH=1788393600`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.

| Artifact | Pages | Font rows | SHA-256 |
|---|---:|---:|---|
| `main_round0_original.pdf` | 1 | 19 | `b482073ac460c56c434987949079d93707720b39fa7e7d0840141943d1864503` |
| `main_round1.pdf` | 3 | 24 | `fbdfdf7cf12c9f586dfa35657ef4247e42a98b5d15ce536da9b6acc810ac5b54` |
| `main_round2.pdf` | 4 | 26 | `db444df6d1f778a1c1b821b68c79abe1321ec9a643a43b37024d4b095c04422c` |
| `main.pdf` | 4 | 26 | `db444df6d1f778a1c1b821b68c79abe1321ec9a643a43b37024d4b095c04422c` |

The release gate rebuilds every round twice in separate fresh directories and
requires byte equality with these checked-in files.  It rejects LaTeX/package
warnings, overfull or underfull boxes, undefined references/citations, rerun
requests, and missing glyphs.  Every listed font is embedded and subset.
`pdftotext -layout` contains no forbidden control byte or literal TeX/reference
garbage, and every page rasterizes to a nontrivial PNG.  Visual inspection of
all four final pages found no clipping, overlap, missing equation, or malformed
heading.
