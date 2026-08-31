# Paper build

`main.tex` is authoritative and revision-gates substantive content.  Each of
rounds 0, 1, and 2 is compiled twice in independent fresh directories with
`SOURCE_DATE_EPOCH=1788048000`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.  Each
pair must be byte-identical; round hashes must differ; `main.pdf` equals
round 2.  Acceptance requires 2--6 pages, embedded/subsetted fonts, clean
text/log checks, and visual inspection.
