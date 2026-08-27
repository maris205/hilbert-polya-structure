# P25 Round-3 conclusion — direct return-map stability closure

Date: **2026-08-27**

## Clear progress

Round 2 left the independent return-map stability check certified on only 9 of
2,241 orbit rows.  Round 3 replaces the binary64 difference calculation with a
100-decimal-digit calculation of the physical ray-intersection/reflection map
in Birkhoff coordinates.  Each periodic point is refined without using the
paraxial stability product, and the direct Jacobian is recomputed at frozen
central-difference steps `1e-28`, `1e-32`, and `1e-36`.

`[NUMERICALLY_CERTIFIED]`: all **2,241/2,241** rows pass the Round-3 contract,
including all **2,232** rows that were open in Round 2.  Direct fixed-point
Newton succeeds on 2,202 rows.  For the 39 most conditioned length-11/12 rows,
the 15-digit serialized collision points lie outside that Newton cylinder; a
100-digit specular-stationarity solve first restores the collision geometry,
after which stability is still calculated exclusively from the direct return
map.  No rows remain open at the frozen geometry and word cutoffs.

The certified residual envelope is:

- maximum post-refinement return residual: `9.836e-71`;
- maximum three-step trace relative span: `5.791e-32`;
- maximum finest-step determinant residual: `3.686e-23`;
- maximum parity-corrected trace relative residual: `5.425e-15`;
- maximum half-density relative residual: `3.955e-15`.

The physical Birkhoff return map has one orientation reversal per collision
relative to the positive-reflection paraxial convention:

```text
trace(direct physical map) = (-1)^word_length * trace(paraxial product).
```

This identifies two distinct Round-2 failure classes: 804 odd-length rows had
the signed-convention mismatch, and 1,428 open even-length rows lay beyond the
binary64 difference-conditioning window.  Round 3 closes both classes with a
method that does not reuse the paraxial matrix formula.

## Evidence boundary

This is a finite-cutoff numerical calibration, not a theorem.  It supports the
internal consistency of the recorded instability multiplier and half-density,
but the aggregate half-density remains `[NUMERICAL_OBSERVATION]`.  The already
executed neighboring-geometry and label controls still imply
`[STOP_SCOPED] / PROVES_TOO_MUCH` for treating generic half-density persistence
as arithmetic evidence.

```text
PROPOSAL_STAGE=1
ROUTE_A_SCOPE=A0-A1_NEGATIVE_CONTROL
ROUND3_DIRECT_RETURN_MAP_ROWS=NUMERICALLY_CERTIFIED_2241_OF_2241
ROUND3_REMAINING_OPEN_ROWS=0
HALF_DENSITY_EVIDENCE=NUMERICAL_OBSERVATION
HALF_DENSITY_CONTROL_VERDICT=STOP_SCOPED
FORMAL_A0_A4_TUPLE=UNASSIGNED
A2_EVALUATION=NOT_RUN
ROUTE_B_EVALUATION=NOT_RUN
ROUTE_B_INVOCATION_ALLOWED=false
GATES_A_E=NOT_REACHED
```

No prime or zero table was used.  No arithmetic owner, exact
multiple-scattering determinant identity, dynamical-zeta divisor, formal
A0--A4 tuple, A2 promotion, or Route-B claim follows.
