# Experiment plan

## Experiment E1: symbolic cycle enumeration

Enumerate all primitive directed cycles through period five in the frozen H6
adjacency matrix.  Acceptance counts: `1,0,1,2,2`.

## Experiment E2: block-incidence rank

Compute cyclic block-count matrices for widths one through four.  Verify the
width-three relation and the determinant `-1` of the selected width-four
minor.

## Experiment E3: exact period-five elimination

Derive the coordinate, trace and multiplier polynomials symbolically.  Use
exact Sturm counts in six rational trace intervals.  Decimal roots are only
diagnostics.

## Experiment E4: independent reconstruction

Use DFS instead of Cartesian-product enumeration and independently recompute
the resultants, root counts and excess inequality.

## Experiment E5: adversarial controls

Mutate graph incidence, polynomial coefficients, root counts, inequality
direction, memory claim and Route-B flag.  Every mutation must be rejected.

## Stop conditions

- Any dependency hash drift: fail closed.
- Any missing primitive cycle or root interval: fail closed.
- A finite four-block interpolant must not be promoted to an all-orbit model.
- Numerical excess values alone cannot certify a strict algebraic inequality.
