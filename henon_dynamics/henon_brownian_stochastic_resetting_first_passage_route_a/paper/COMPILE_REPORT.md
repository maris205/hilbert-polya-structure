# C214 compilation report

* Engine: LuaHBTeX/LuaLaTeX with fixed `SOURCE_DATE_EPOCH=1787961600`.
* Build: the release source suppresses optional PDF metadata (including the
  trailer identifier); two
  passes in each of two independent directories produced the same final bytes.
  `main.pdf` equals `main_round2.pdf`.
* Final pages: 3 (within the 2--6 package contract); final SHA-256 is
  `135989257553d59dadf4fbe2b31a2843c06a892a56b612fc1b9494289b8cde06`.
* Undefined references/citations: 0 after the second pass.
* Overfull/underfull boxes: none in the final log.
* Fonts: all final PDF fonts embedded and subsetted (`pdffonts`).
* Text audit: Brownian, renewal, stationary, first-passage, `z*`,
  `ROUTE_A_REJECTED`, scope literal, and Evans citations present.
* Sidecars: removed before manifest closure.

The first pass of a fresh revision may emit the normal rerun warning; the
fixed-epoch second pass is the release check.

The retained revision hashes are `a2cad9da48500b59ff1b87f59298bff7b74a8e1ccd5d25e9791da24c0dddf103`
(round 0), `3f878d5d026819c9ff8bbc502372be7e2458d2f0613abe49490bd2c7810ca31d`
(round 1), and the final hash above (round 2); all three are distinct.
