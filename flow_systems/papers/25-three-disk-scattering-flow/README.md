# Paper 25 — three-disk scattering flow

Working title: *Generic Half-Density Is Not Arithmetic: A Three-Disk Scattering Control*

## Current status

- ARS: **Stage 1 RESEARCH in progress**.
- Proposal: **Stage 1 Classical Flow Baseline / Route A A0 kill control**.
- Concrete progress: the exact no-eclipse geometry is frozen; the exact quantum
  multiple-scattering determinant is separated from the semiclassical
  Gutzwiller--Voros orbit expansion; the project is internally prespecified as
  the batch's non-arithmetic control.  Round 2 has now executed the full
  symbolic cutoff and target-free negative-control experiment.
- A0-source status: **`[MODELING_CHOICE] ABSENT_BY_CONSTRUCTION`**.  This status
  follows from the frozen control design and does not depend on the numerical
  half-density experiment.
- Half-density control status: **`[STOP_SCOPED] / PROVES_TOO_MUCH`** for using
  generic instability-half-density persistence as arithmetic evidence.  This is
  a statistic-level negative result, not a formal A0--A4 tuple.  Route-B
  evaluation is not run and invocation is disallowed.

## Round-2 executed artifact

The deterministic symbolic enumerator found all 747 oriented primitive cyclic
three-label words with no adjacent repetition through topological length 12.
Across `d/a=5.8,6.0,6.2`, this gives 2,241 rows.  In every row the symbolic word,
center-polygon proxy, and actual specular billiard solution are separate.

`[NUMERICALLY_CERTIFIED]`: all 2,241 actual-orbit rows passed the frozen
two-solver agreement, visibility, independent length, stationarity, and
specular-reflection thresholds.  The maximum stationarity and reflection
residuals are `3.20e-14` and `3.80e-14`; the maximum independent length and
angle disagreements are `2.14e-14` and `4.61e-8`.

The analytic paraxial monodromy formula supplies a half-density
`|Lambda_u|^(-1/2)`.  A direct finite-difference return-map cross-check is
`NUMERICALLY_CERTIFIED` for only 9 rows and remains `[OPEN]` for 2,232 highly
unstable rows; therefore the batch-wide half-density conclusions are labeled
`[NUMERICAL_OBSERVATION]`, not numerical certification.

Long monodromy products are rebuilt with 80-digit decimal arithmetic; the
binary64 trace is retained as a recorded cross-check.  This removes catastrophic
`ad-bc` cancellation from the determinant field, but it is a precision check of
the same paraxial formula, not a substitute for the independent return map.

## Frozen dynamical system

Take three disks of radius `a`, with centers at the vertices of an equilateral
triangle of side `d=6a`.  The primary object is the unit-speed exterior billiard
flow with specular reflection.  Its primitive objects are primitive oriented
cyclic disk words; the clock is physical Euclidean flight length.

The third center lies at distance `(sqrt(3)/2)d` from the line joining the other
two.  Thus the no-eclipse condition follows from

```text
(sqrt(3)/2)d > 2a,
```

and `d=6a` is safely inside the open hyperbolic regime.

## Research question and bold hypothesis

Can any target-free statistic of the primitive-orbit half-density distinguish
rational primes from matched random/composite controls after stability and
escape rate are frozen?

The original bold statement was `[HEURISTIC]`: instability factors can mimic an envelope such
as `p^(-r/2)` without any arithmetic origin.  If so, amplitude resemblance is a
generic hyperbolic effect and the tested statistic must be classified
`[STOP_SCOPED] / PROVES_TOO_MUCH`.

The exact spectral surface is the multiple-scattering matrix determinant (or
exact `S`-matrix factorization).  A Gutzwiller--Voros zeta is used only as a
semiclassical curvature-expanded object, never as an exact determinant
identity.

## First kill gate

The internally prespecified test has been executed.  For all 747 words with
certified solutions at all three parameters, the correlations of log
half-density at `d/a=6.0` with the `5.8` and `6.2` controls are respectively
`0.999998520` and `0.999998755`, above the frozen `0.98` stop threshold.  A
within-word-length period shuffle preserves nearly the same coarse correlation
(`-0.965354` versus `-0.968442`), and the guaranteed-composite fixed-exponent
RMSE (`1.104095`) is lower than the rank-integer proxy RMSE (`1.556276`).
Random phase, random stability, and deterministic random-integer controls are
also recorded row by row without prime or zero tables.

Accordingly, `[NUMERICAL_OBSERVATION]` supports `[STOP_SCOPED] /
PROVES_TOO_MUCH` for this half-density statistic as arithmetic evidence.  The
outcome leaves the independently frozen A0-source absence unchanged and cannot
manufacture an arithmetic owner for this geometry.

Evidence labels in this project use the vocabulary of
`skills/route-a-evaluator.md`; assignment states such as `UNASSIGNED` and
`NOT_EVALUATED` are stage bookkeeping, not evidence tokens.

## Files

- [Stage-1 research brief](notes/stage1_research_brief.md)
- [pipeline state](notes/pipeline_state.md)
- [planned ledger](results/README.md)
- [Round-2 conclusion](notes/round2_conclusion.md)
- [Round-2 validation](experiments/round2_validation.md)

No exact scattering determinant, A2 zeta test, formal Route tuple, or manuscript
is claimed yet.
