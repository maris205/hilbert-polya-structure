# Paper build

`main.tex` is compiled with LuaLaTeX under
`SOURCE_DATE_EPOCH=1787875200`.  `main_round0_original.pdf` is the initial
statement, `main_round1.pdf` adds the explicit endpoint-cancellation and
LaSalle proof details, and `main_round2.pdf` adds the degenerate-face and audit
supplement.  The release `main.pdf` is byte-identical to round 2.

The paper is intentionally source-local.  Its Route-A conclusion is
`ROUTE_A_REJECTED`, with no arithmetic, target determinant, or Hilbert–Pólya
claim.  This file is not external peer review.
