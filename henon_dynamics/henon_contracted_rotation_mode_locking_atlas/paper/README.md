# Paper build

`main.tex` is compiled with LuaLaTeX twice per revision in fresh temporary
trees under `SOURCE_DATE_EPOCH=1788048000`.  The release keeps three
content-distinct PDFs: `main_round0_original.pdf`, `main_round1.pdf`, and
`main_round2.pdf`; `main.pdf` equals round 2 byte-for-byte.

The paper presents the exact Fraction itinerary/interval certificate for the
contracted rotation, endpoint equality audit, direct-iteration control, and
the conservative Route-A boundary.  It distinguishes source-local derivative
bookkeeping from any target determinant and makes no arithmetic claim.  No
global one-periodic-orbit theorem is claimed: the cited general two-branch
piecewise-contraction theorem gives only an at-most-two bound under its
hypotheses.  This is not external peer review.
