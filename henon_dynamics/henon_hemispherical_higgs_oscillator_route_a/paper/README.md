# Paper build

`main.tex` is a three-round conditional manuscript. Define
`\CRevisionRound` as 0, 1, or 2; the release PDF is round 2. The release gate
performs two fresh LuaLaTeX builds per round at `SOURCE_DATE_EPOCH=1788480000`,
requires byte identity, scans settled logs, checks embedded subset fonts and
extracted-text hygiene, and rasterizes every page.
It also rejects unescaped `quad` or `qquad` source tokens and a leaked literal
`qquad` token in extracted PDF text.

The bibliography records S. Bellucci, A. Nersessian, A. Saghatelian, and
V. Yeghikyan for arXiv:1008.3865, and Ye. M. Hakobyan and G. S. Pogosyan for
arXiv:quant-ph/9803085. The latter source supports separation and Jacobi-mode
background; the paper proves the hemisphere multiplicity by direct label
count rather than importing its conflicting prose degeneracy sentence.
