# Deterministic compile report

Engine: LuaLaTeX.  Every round used `SOURCE_DATE_EPOCH=1788393600`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`, a fixed PDF trailer ID, two passes, and two isolated fresh directories.  The two fresh PDFs for each round were byte-identical.  The settled-log scan found no `LaTeX`/package warning, overfull/underfull box, undefined citation/reference, rerun request, or missing character.

| artifact | SHA-256 | pages | bytes | embedded/subset font rows |
|---|---|---:|---:|---:|
| `main_round0_original.pdf` | `c6b969ca113ae80684098f450f846ddfa556c06cbee32e05d3389e5ee9d215dc` | 1 | 237107 | 15 |
| `main_round1.pdf` | `386d2743aad8a079071662d39bebb17f92045e31e1d7dd3e3cc9bd5c615e6b93` | 2 | 253495 | 16 |
| `main_round2.pdf` | `0ddd3fad510c184a999ad785ab7ac1af170b66169f15b54bda92b9fcb5e1e8bd` | 3 | 293631 | 17 |
| `main.pdf` | `0ddd3fad510c184a999ad785ab7ac1af170b66169f15b54bda92b9fcb5e1e8bd` | 3 | 293631 | 17 |

All font rows reported `emb=yes` and `sub=yes`.  Text extraction found the round-specific sentinels `Chebyshev spectrum`, `biorthogonal density`, `one nilpotent N-Jordan block`, `ROUTE_A_REJECTED`, `NO_BAD_EULER_OR_ROOT_NUMBER`, and `AI-use disclosure` in the appropriate rounds.

Visual inspection of all three final pages passed: equations remain within margins, headings and theorem/proof flow are legible, no glyph is clipped, and the deliberately short reference page is clean.  Raster smoke tests produced nonempty images for every archived page.
