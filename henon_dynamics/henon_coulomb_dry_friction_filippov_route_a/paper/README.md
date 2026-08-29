# Paper build

`main.tex` is compiled with LuaLaTeX twice per revision in fresh temporary
trees under `SOURCE_DATE_EPOCH=1787875200`.  The release keeps three
content-distinct PDFs: `main_round0_original.pdf`, `main_round1.pdf`, and
`main_round2.pdf`; `main.pdf` equals round 2 byte-for-byte.

The paper freezes the maximal-monotone/viability selection at zero velocity.
It distinguishes a nonzero-velocity partial slip arc from subsequent complete
half-cycles and makes no arithmetic or Hilbert–Pólya claim.  This is not
external peer review.
