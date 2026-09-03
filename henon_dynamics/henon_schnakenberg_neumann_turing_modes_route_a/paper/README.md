# C350 paper build

`main.tex` is the single source for three substantive revisions.  Define
`\CRevisionRound` as `0`, `1`, or `2` before inputting the source.  The
checked artifacts are `main_round0_original.pdf`, `main_round1.pdf`, and
`main_round2.pdf`; `main.pdf` is byte-identical to round 2.

The release gate builds every round twice in fresh directories with
`SOURCE_DATE_EPOCH=1788393600`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.  It
rejects warnings, layout defects, missing glyphs, unembedded fonts, control
bytes, stale revision PDFs, and a final PDF different from round 2.
