# C242 manuscript build

`main.tex` is a two-round revised manuscript on the irrational ellipsoid
Reeb-orbit theorem and rational Morse--Bott boundary.  Build with LuaLaTeX,
twice per round, using `SOURCE_DATE_EPOCH=1788048000`, `TZ=UTC`, and
`LC_ALL=C`.  The final `main.pdf` must equal `main_round2.pdf`; all three
round PDFs remain in the package for auditability.

The manuscript states the coordinate complex-line trivialization used by
Hutchings, keeps the rational CZ value undefined before perturbation, and
contains the `NO_BAD_EULER_OR_ROOT_NUMBER` scope declaration.
