# C187 paper improvement log

This is an internal deterministic drafting record, not external peer review.

## Round 0 — theorem normalization

- Froze Rhoades's remove-maximum promotion convention.
- Locked the standard-tableau q-hook polynomial with no q-shift.
- Replaced the false phrase “promotion has order `N`” by the correct theorem
  `j^N=id`, with actual order dividing `N`.
- Added one-row, one-column and `2x2` boundary controls.

## Round 1 — dynamical closure

- Added exact-period and cycle formulas by divisor Möbius inversion.
- Added the finite Artin--Mazur zeta and reciprocal Koopman determinant.
- Added the complete root-of-unity spectral multiplicity formula and trace law.

## Round 2 — operator and release closure

- Added evacuation as a unitary reversor and evacuation plus conjugation as an
  antiunitary reversor.
- Made source attribution and finite-regression limitations explicit.
- Added 230,034 independent assertions, 3,065 SymPy checks, byte replay, and
  107 repaired-hash plus one stale-hash rejection.
- Locked the rejected Route-A tuple and Route-B false status.

All three round PDFs contain different revision-focus text.  Final compile,
font, log, determinism and visual findings are recorded separately in
`paper/COMPILE_REPORT.md`.
