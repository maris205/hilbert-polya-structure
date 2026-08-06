# R102 — Fourth-Grid Check for the \(a=1.02\) Core

## Motivation

R101 passed the preregistered median level-change gate for all cells.  A
post-hoc spacing-stability diagnostic then passed for both \(a=1.02\) cells
and failed for both \(a=6\) cells.  R102 freezes one final grid before the
\(a=1.02\) quantum conclusion is written.

## Design

- Cells: \((a,n,B)=(1.02,1,0)\) and \((1.02,1,1)\).
- Grid: nominal \(h=0.0175\), same contour wall and 180 eigenvalues.
- Compare modes 25--164 against R101 \(h=0.0225\).
- Level gate: median relative change below 0.5%.
- Compute a new two-grid \(h^2\) extrapolation.
- Spacing gate: fine/extrapolated mean adjacent-ratio difference below 0.015.

No additional magnetic field is tuned and no zero or prime data are loaded.
