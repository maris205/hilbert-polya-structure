# Paper artifacts

`main.tex` is the final two-revision manuscript.  `main_round0_original.pdf`,
`main_round1.pdf`, and `main_round2.pdf` are intentionally content-distinct;
`main.pdf` is byte-identical to round 2.  The manuscript keeps the exact
asymptotic Weber result separate from the finite-window RK4 control and states
the strict Route-A rejection.

Build with LuaLaTeX in a clean temporary directory, twice at fixed epoch
`1787875200`, then remove `.aux`, `.log`, `.out`, `.toc`, `.fls`, `.fdb_latexmk`,
`.synctex.gz`, and `__pycache__` sidecars before running the release manifest.
