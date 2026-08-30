# Compilation report

Status: **PASS**

Engine: LuaLaTeX, two passes per revision, with
`SOURCE_DATE_EPOCH=1788048000`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.  Each
revision was compiled in an independent temporary tree; settled second-pass
logs contained no fatal errors, undefined references, overfull boxes, or
underfull boxes.  The source has no figures or auxiliary bibliography files.
The LuaTeX trailer ID is fixed in `main.tex`, so repeated independent trees
are byte-identical.

| revision | SHA-256 | pages |
|---|---|---:|
| `main_round0_original.pdf` | `de86e7bb812e15ed52ac57bf80036b2423c016e8cc4c2c807ac9fc9e0be6fdfe` | 2 |
| `main_round1.pdf` | `7b6bb28ea490b1f866aeb5fe4e3f8605abb66b494bf43bb619652f23919730af` | 2 |
| `main_round2.pdf` | `a44589bc7f25d8576c337f916db772cedef8bf0e8c4e89b10356a2a540bea555` | 2 |

`main.pdf` is byte-identical to `main_round2.pdf`.  `pdfinfo` reports two
pages; `pdffonts` reports only embedded/subset fonts; `pdftotext` contains the
title, wall-erosion theorem, Lucas count, transient transfer, Route-A tuple,
and scope boundary.  Page-level visual inspection found no clipping or
unreadable mathematics.
