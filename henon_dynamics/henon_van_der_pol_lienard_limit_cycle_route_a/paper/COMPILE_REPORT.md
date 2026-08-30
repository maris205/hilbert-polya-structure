# C249 compile report

The three revision sources were compiled with LuaLaTeX on 2026-08-30 UTC.
Each round was built twice in two independent fresh trees with
`SOURCE_DATE_EPOCH=1788048000`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`; each pair
was byte-identical.  All documents are two pages.  The resulting SHA-256
values are:

| artifact | SHA-256 | pages |
|---|---|---:|
| main_round0_original.pdf | 4ddebefec84857aa1aeb6fa01667561637b33629af92473e8971bb56bf9fee29 | 2 |
| main_round1.pdf | bd486ac66a7f5444eeae9a7b7a4da7f8834c73bb5231ce4167a7c89dfbf68d57 | 2 |
| main_round2.pdf | c83472c2c75850e23c9035661afe7bd58bad60b2936dbc44f783dc9f69131dab | 2 |
| main.pdf (copy of round 2) | c83472c2c75850e23c9035661afe7bd58bad60b2936dbc44f783dc9f69131dab | 2 |

The final PDF has 22 embedded and subsetted Latin Modern/AMS font entries;
none is unembedded.  The first pass of each fresh tree emits only the normal
cross-reference/rerun notices; the second pass has no overfull or underfull
boxes, unresolved references, or multiply-defined labels.  `pdftotext` and
visual inspection contain the Lienard theorem, Poincare section, Floquet
receipt, route tuple, and explicit scope boundary.  Build sidecars were
removed before manifest generation.  A fixed LuaTeX trailer ID is declared in
the source so byte identity is independent of the temporary directory.
