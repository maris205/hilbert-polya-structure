# Manuscript build

`main.tex` is a self-contained short paper.  The three PDF revisions are
`main_round0_original.pdf`, `main_round1.pdf`, and `main_round2.pdf`; the
release copy is `main.pdf`.  Build with LuaLaTeX in two passes under
`SOURCE_DATE_EPOCH=1788048000`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.

The paper states the wall-erosion lemma, complete periodic classification,
sharp transient bound, Lucas/cosine fixed count, and parity-twisted transfer
formula.  It explicitly keeps the even all-one wall boundary separate and
does not make target arithmetic or operator claims.
