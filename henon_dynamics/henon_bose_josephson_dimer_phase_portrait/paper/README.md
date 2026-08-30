# C243 manuscript build

`main.tex` presents the coordinate-safe Bose--Josephson dimer phase portrait,
including the fixed-point pitchfork, quartic energy reduction, complete
elliptic-`K` periods, sech homoclinic, and component-level self-trapping
criterion.  Compile LuaLaTeX twice for each revision with
`SOURCE_DATE_EPOCH=1788048000`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`, and
`LC_ALL=C`.  The final `main.pdf` must equal `main_round2.pdf`; all three
round PDFs are retained.

The manuscript explicitly states that regular levels are continuous and that
the result is not an arithmetic determinant or Hilbert--Pólya construction.
