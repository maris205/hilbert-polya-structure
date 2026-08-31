# Paper build

`main.tex` is authoritative and uses revision-gated substantive content.
Rounds 0, 1, and 2 are each compiled twice in independent fresh directories
with `SOURCE_DATE_EPOCH=1788048000`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.
Each pair must be byte-identical, the three retained round hashes distinct,
and `main.pdf` equal to round 2.  Acceptance also requires 2--6 pages,
embedded/subsetted fonts, text extraction, visual inspection, and a clean
second-pass log.
