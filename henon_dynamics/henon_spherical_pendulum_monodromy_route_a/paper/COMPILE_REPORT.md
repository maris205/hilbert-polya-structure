# C244 compile report

The three revision sources were compiled with LuaLaTeX on 2026-08-30 UTC.
Each round was built twice in two independent fresh trees with
SOURCE_DATE_EPOCH=1788048000, FORCE_SOURCE_DATE=1, and TZ=UTC; each pair was
byte-identical.  All documents are two pages.  The resulting SHA-256 values
are:

| artifact | SHA-256 | pages |
|---|---|---:|
| main_round0_original.pdf | 99308c9fb6a0d9447027ee667156c58bb46d9091bd4cd8fa660c0349636bc438 | 2 |
| main_round1.pdf | d47fb3370e3fb0ff9c7583eaf1b1a0597899f3a93c5f372c601673723d6dddbe | 2 |
| main_round2.pdf | ead1cc2f0c378db3630bfe24f4032270f00ddaa25b43671e91c910e157b3c9d8 | 2 |
| main.pdf (copy of round 2) | ead1cc2f0c378db3630bfe24f4032270f00ddaa25b43671e91c910e157b3c9d8 | 2 |

The final PDF has 22 embedded and subsetted Latin Modern font entries; the
round-0 and round-1 artifacts have 20 and 21 entries respectively.
pdftotext and visual inspection contain the cubic, discriminant, root labels,
three quadratures (including the square-root numerator in the action),
Liouville fibers, isolated focus-focus value, matrix-column convention,
closure/repetition rule, route tuple, and scope boundary.  The first pass of
each fresh tree emits only the standard rerun/undefined-reference notice;
the second pass is warning-free (no overfull/underfull boxes, unresolved
references, or multiply-defined labels).  Build sidecars were removed before
manifest generation.
