# C247 manuscript build

`main.tex` is the single source for three substantive revision rounds.  Round
0 freezes the angle-chart translation, reduced rational range, and the initial
clean-return/endpoint statements.  Round 1 adds the all-parameter geometry and
the explicit clean-return proposition.  Round 2 adds
the endpoint-identification policy, the two one-sided grazing limits, the
noncanonical-incidence convention, the natural Dirichlet/Neumann note, and
the final scope boundary.  `main.pdf` is a byte-for-byte copy of
`main_round2.pdf`.

Each round is compiled twice in independent fresh trees with LuaLaTeX,
`SOURCE_DATE_EPOCH=1788048000`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`; only the
PDFs are retained in this package.  Auxiliary build files are deliberately
excluded from the release manifest.
