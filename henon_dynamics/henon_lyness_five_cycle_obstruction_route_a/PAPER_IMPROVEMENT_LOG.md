# Two-round paper improvement log

The three PDF snapshots are intentionally distinct and the final
`main.pdf` is byte-identical to `main_round2.pdf`.

## Round 0: theorem skeleton

- Froze the positive domain, clock, and map.
- Gave the explicit five iterates and unique fixed point.
- Stated the first Artin--Mazur failure at (n=5).
- Boundary weakness found: the first draft did not prove the invariant
  measure, projection sign, or operator-class consequences.

Snapshot: `paper/main_round0_original.pdf`.

## Round 1: geometry and operator audit

- Added the Jacobian density calculation and (RFR=F^{-1}).
- Added (U^5=I), the signed cyclic projections, and the ordinary Fredholm
  boundary.
- Hostile review found that merely saying the Hilbert space is infinite did
  not prove that every root-of-unity eigenspace has infinite multiplicity.

Snapshot: `paper/main_round1.pdf`.

## Round 2: complete obstruction proof

- Added the disjoint-orbit-tube construction proving all five eigenspaces
  infinite-dimensional.
- Separated noncompactness, finite Schatten exclusion, trace-class
  determinant failure, and non-self-adjointness.
- Added the antiunitary reversal, A0--A4 tuple, explicit limitations, and
  all six declaration categories.
- Re-ran both mandatory seven-mode ARS integrity gates, with explicit
  implementation-bug, hallucinated-citation, hallucinated-result,
  shortcut-reliance, bug-as-insight, methodology-fabrication, and
  early-frame-lock findings, plus the deterministic build checks.

Snapshot: `paper/main_round2.pdf`; release target: `paper/main.pdf`.

Final SHA-256 values are recorded in `paper/COMPILE_REPORT.md` and the
release manifest after deterministic compilation.
