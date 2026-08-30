# C241 paper artifacts

`main.tex` is the complete paper for the classical Lüroth countable-branch
map.  It is compiled at revision rounds 0, 1, and 2 with LuaLaTeX, two settled
passes in two independent fresh directories, and
`SOURCE_DATE_EPOCH=1788048000`.  The checked-in `main.pdf` is byte-identical
to `main_round2.pdf`; round 0/1/2 hashes and font/text checks are recorded in
`COMPILE_REPORT.md` and the release manifest.

The paper explicitly distinguishes the branch image `(0,1]` from the excluded
endpoint, marks full-weight divergence at `Re(s)=1/2`, and separates the
absolute primitive-product domain `|z| A(Re(s))<1` from meromorphic
continuation away from denominator zeros.  Route-A is
`A0_FAIL/A1_PASS_ANALYTIC/A2_FAIL/A3_FAIL/A4_FORMAL_HINT`.
