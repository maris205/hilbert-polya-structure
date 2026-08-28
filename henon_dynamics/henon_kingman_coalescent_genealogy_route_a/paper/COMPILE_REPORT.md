# C215 compilation report

* Engine: LuaHBTeX/LuaLaTeX with fixed `SOURCE_DATE_EPOCH=1787961600`.
* Build: the release source suppresses optional PDF metadata (including the
  trailer identifier); two
  passes in each of two independent directories produced the same final bytes.
  `main.pdf` equals `main_round2.pdf`.
* Final pages: 2 (within the 2--6 package contract); final SHA-256 is
  `a2ce47e6c601a153720c29b907e27d0aae56ffc6e383e04ce54f3853fa718a5c`.
* Undefined references/citations: 0 after the second pass.
* Overfull/underfull boxes: none in the final log.
* Fonts: all final PDF fonts embedded and subsetted (`pdffonts`).
* Text audit: Kingman, hypoexponential, MRCA, branch, coalescent,
  `ROUTE_A_REJECTED`, scope literal, and Artin--Mazur boundary present.
* Sidecars: removed before manifest closure.

The first pass of a fresh revision may emit the normal rerun warning; the
fixed-epoch second pass is the release check.

The retained revision hashes are `b02c7c9fd76a69fae9133d2f30961c2b8dda16017bacbb9175e51962a0e69dad`
(round 0), `ba55650d01d8d7bdbfd98575080fb40865319e0dbee6f9874f28e90720f3b7e8`
(round 1), and the final hash above (round 2); all three are distinct.
