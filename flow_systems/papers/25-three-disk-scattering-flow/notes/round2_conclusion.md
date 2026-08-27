# P25 Round-2 conclusion — executed three-disk negative control

Date: **2026-08-27**

## Landed result

`[PROVED]`: there are 747 oriented primitive cyclic words over three disk labels
with no adjacent repetition through topological length 12.  Applying the same
schema at `d/a=5.8,6.0,6.2` creates 2,241 rows.

`[NUMERICALLY_CERTIFIED]`: all 2,241 rows have an actual specular billiard
solution under the frozen residual contract.  A variational BFGS solution and
an independent least-squares stationarity solution agree; the final maximum
stationarity, reflection, independent-length, and independent-angle residuals
are respectively `3.20e-14`, `3.80e-14`, `2.14e-14`, and `4.61e-8`.  Segment
visibility and outward/inward normal signs are checked.  Center-polygon lengths
remain separate `MODELING_CHOICE` proxies.

The paraxial monodromy formula defines
`UNSTABLE_MULTIPLIER_HALF_DENSITY_V1=|Lambda_u|^(-1/2)`.  Direct finite-
difference return-map validation is `NUMERICALLY_CERTIFIED` on 9 rows and
`[OPEN]` on 2,232 highly unstable rows.  Aggregate half-density claims are
therefore `[NUMERICAL_OBSERVATION]`.  An 80-digit rebuild supplies the recorded
unit-determinant check and is compared with the binary64 trace.  This closes a
floating-point cancellation risk in the ledger, but is not treated as an
independent stability derivation.

## Executed falsification result

All 747 words form complete neighboring-parameter triplets.  Correlations of
log half-density between `d/a=6.0` and `5.8,6.2` are `0.999998520` and
`0.999998755`, exceeding the frozen `0.98` persistence threshold.  A period
shuffle within topological length retains almost the same coarse correlation;
guaranteed-composite labels fit the fixed `-1/2` envelope at least as well as
the rank-integer proxy under the recorded RMSE.

Thus `[NUMERICAL_OBSERVATION]`: generic hyperbolic instability structure
survives non-arithmetic neighboring and label controls.  The statistic is
`[STOP_SCOPED] / PROVES_TOO_MUCH` as arithmetic evidence.  This is the intended
negative-control outcome, not a candidate success.

## Route boundary

```text
PROPOSAL_STAGE=1
ROUTE_A_SCOPE=A0-A1_NEGATIVE_CONTROL
A0_SOURCE_EVIDENCE=MODELING_CHOICE
A0_SOURCE_STATUS=ABSENT_BY_CONSTRUCTION
A1_SYMBOLIC_ENUMERATION=PROVED
A1_ACTUAL_ORBIT_ROWS=NUMERICALLY_CERTIFIED
HALF_DENSITY_EVIDENCE=NUMERICAL_OBSERVATION
HALF_DENSITY_CONTROL_VERDICT=STOP_SCOPED
FORMAL_A0_A4_TUPLE=UNASSIGNED
ROUTE_B_EVALUATION=NOT_RUN
ROUTE_B_INVOCATION_ALLOWED=false
GATES_A_E=NOT_REACHED
```

No prime/zero data defined or screened parameters.  No arithmetic owner,
prime-power repetition law, exact multiple-scattering determinant computation,
A2 zeta divisor, or Route-B claim follows.  The unresolved technical risk is
the finite-difference monodromy cross-check on 2,232 rows; the unresolved
scientific boundary is more fundamental—the geometry has no intrinsic
arithmetic source by design.
