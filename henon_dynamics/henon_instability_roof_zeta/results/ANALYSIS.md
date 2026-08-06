# Result Analysis

Evidence labels follow the Route-A hierarchy. The protocol hash is `0c284a1b3610a3d772aa00c6a8b33161a8bc6814957a9968d5c80fb618eec399`.

## Raw root table

| Orientation sector | Cutoff | Located roots | Numerical winding | Positive real root | Max precision drift |
|---:|---:|---:|---:|---:|---:|
| 0 | 7 | 43 | 43 | 0.277981048659 | 6.60e-14 |
| 0 | 8 | 43 | 43 | 0.277982796968 | 9.07e-14 |
| 0 | 10 | 43 | 43 | 0.277982988594 | 2.53e-13 |
| 0 | 12 | 43 | 43 | 0.277982981734 | 9.97e-13 |
| 0 | 14 | 43 | 43 | 0.277982981676 | 2.94e-12 |
| 0 | 16 | 43 | 43 | 0.277982981676 | 6.32e-12 |
| 0 | 18 | 43 | 43 | 0.277982981676 | 4.30e-11 |
| 0 | 20 | 43 | 43 | 0.277982981676 | 1.68e-10 |
| 1 | 7 | 45 | 45 | -- | 1.81e-14 |
| 1 | 8 | 45 | 45 | -- | 4.91e-14 |
| 1 | 10 | 43 | 43 | -- | 1.27e-13 |
| 1 | 12 | 43 | 43 | -- | 5.79e-13 |
| 1 | 14 | 43 | 43 | -- | 3.67e-12 |
| 1 | 16 | 43 | 43 | -- | 5.10e-12 |
| 1 | 18 | 43 | 43 | -- | 2.83e-11 |
| 1 | 20 | 43 | 43 | -- | 1.44e-10 |

All sampled numerical winding estimates above agree at 4096, 8192, and 16384 contour points. Every listed estimate equals the explicit census; no estimate is claimed as an interval-certified argument-principle count. The rectangle is the frozen `[-0.25,0.30] x [-20,20]` rectangle.

## Raw control table

| Control | Root-count status | Retention 8->16 (mean +/- SD) | Median drift | Degree 9--16 tail L1 | Tail / Hénon |
|---|---|---:|---:|---:|---:|
| Hénon instability roof | VALID_NUMERICAL_CANDIDATE | 1.000 | 1.891e-04 | 6.866e-07 | 1.00 |
| constant_roof_parent | EXACT_ANALYTIC_CONTROL | 1.000 +/- 0.000 | 0.000e+00 | 1.183e-16 | 1.72e-10 |
| positive_random_weights | VALID_NUMERICAL_CONTROL | 0.084 +/- 0.023 | 1.348e-02 | 7.827e-02 | 1.14e+05 |
| random_phases | VALID_NUMERICAL_CONTROL | 0.028 +/- 0.018 | 1.215e-02 | 2.197e-01 | 3.20e+05 |
| same_density_random_lengths | VALID_NUMERICAL_CONTROL | 0.042 +/- 0.012 | 1.073e-02 | 1.962e-02 | 2.86e+04 |
| shuffled_lengths | NOT_TESTABLE_ROOT_COUNT | N/T | N/T | 3.648e-01 | 5.31e+05 |
| shuffled_periods | NOT_TESTABLE_ROOT_COUNT | N/T | N/T | 2.997e-01 | 4.37e+05 |

`NOT_TESTABLE_ROOT_COUNT` means the frozen contour-sampling algorithm failed: its three resolutions disagree after a global shuffle creates high-frequency exponential terms. The entire control functions still have well-defined root counts, but the unresolved sampled counts and root-stability numbers are not used. The constant-roof row uses its exact four-eigenvalue formula; its reported coefficient tail is a floating-point floor, and the float root locator missed two roots at cutoff 16.

## Neighbor controls

| Parameter | Self retention 8->16 | Self median drift | Fraction matching H6 training roots | Roots at 16 |
|---:|---:|---:|---:|---:|
| 5.9 | 1.000 | 3.754e-04 | 0.128 | 43 |
| 6.1 | 1.000 | 4.080e-04 | 0.128 | 43 |

These are numerical continuations of the same words, not certified common-survivor theorems.

## Key findings

1. **PROVED — the unit-clock lattice-periodicity obstruction is removed.** The unit clock gives an exact vertically periodic determinant, and the stored action is not a positive roof because one exact period-four orbit has action zero. In contrast, the unstable roof obeys `J^u >= 773/224 > 1`. The fixed orbit multiplier has degree four, the explicit period-four multiplier has degree two, and no positive powers can coincide; hence their log ratio is irrational and the roof is non-lattice. This removes one obstruction, not the global analytic obligations.

2. **NUMERICAL_OBSERVATION — a preregistered family of finite-section zeros survives the sealed test.** Untwisted retention is 100%, with validation median drift `1.873e-04` and sealed median drift `1.759e-06`. Twisted retention is also 100%, with sealed median drift `8.097e-07`. The untwisted positive real finite-section zero reaches `0.27798298167618902348832311683180466042471613147972330864936381175446226192981557` at cutoff 20. In the twisted family, one of the 43 tracked zeros is the exact symbolic root `s=0`.

3. **NUMERICAL_OBSERVATION — the coefficient cancellation is strongly non-generic among the frozen orbit-level controls.** At the common Hénon probe, the Hénon degree-9--16 tail is `6.866e-07`. Valid random controls are tens of thousands to hundreds of thousands of times larger and retain only a small fraction of their cutoff-8 roots. This demonstrates structured cycle cancellation relative to those controls; it does not isolate shadowing as the cause. The exact constant-roof parent is even more stable, so stability is not an arithmetic signature.

4. **NUMERICAL_OBSERVATION — nearby parameters are also internally stable.** The `a=5.9` and `a=6.1` word continuations each retain all their cutoff-8 roots while most do not lie within the frozen H6 matching tolerance. Thus H6 is not numerically isolated by this test.

5. **OPEN / A3 blocker — no limiting global divisor has been proved.** Each fixed finite section is an exponential polynomial with linear zero-count growth in height. Inferring a `T log T` law by increasing cutoff with height would be moving-order fitting unless a uniform remainder theorem is supplied. No functional equation, Gamma factor, trivial-zero structure, or completed-xi identity appears.

## Suggested next experiments

1. Construct cylinder-memory approximations to the same Hölder roof and compare their analytic determinants with the orbit sections. This is the smallest test of a genuine transfer-operator limit.
2. Prove a uniform cycle-tail or Rouché bound on a small contour around the positive real finite-section zero; that would promote one observed zero toward a limiting statement.
3. Add within-period length shuffles and locally constant edge-roof controls, evaluated both at the common Hénon probe and at each control's own positive zero when it exists.
4. Certify a common parameter interval around `a=6` before interpreting neighbor continuation as structural stability of one family.

## Claim boundary

The exact result is a positive non-lattice instability roof on the local certified survivor. The cutoff-stable zero family and coefficient-decay results are finite-section numerical observations. No analytic continuation, limiting divisor, Riemann-zero match, functional equation, Riemann-von Mangoldt law, self-adjoint operator, or global Hénon statement is established.
