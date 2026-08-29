# C230 paper artifacts

main.tex                  -- source, revision selector CRevisionRound
main_round0_original.pdf  -- baseline
main_round1.pdf           -- first substantive revision
main_round2.pdf           -- final revision
main.pdf                  -- byte-identical to round 2
COMPILE_REPORT.md         -- fixed-epoch build and audit record

Each revision is compiled twice in a fresh directory with
SOURCE_DATE_EPOCH=1787875200 and LuaLaTeX.  The paper states the global
Hamiltonian/Lax theorem, sorted scattering, exact N=2 solution, norming
coordinates, and the repeated-root boundary.  Numerical endpoint rows are
identified as diagnostics rather than exact asymptotic formulas.

