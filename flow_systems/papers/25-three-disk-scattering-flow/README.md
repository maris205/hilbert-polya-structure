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
- Round-3 stability status: **2,241/2,241 direct physical return-map checks
  `NUMERICALLY_CERTIFIED`** at the frozen cutoff; 2,232 rows are newly closed
  relative to Round 2.  Aggregate half-density evidence remains
  `NUMERICAL_OBSERVATION`.
- Round-4 methods status: the 39/2,241 condition-aware fallback rows have a
  complete deterministic audit.  All were old-open length-11/12 rows, all pass
  the same final acceptance contract, and a static dependency check verifies
  that fallback selection precedes and does not consume the paraxial comparison
  target.  This is a post-hoc descriptive audit, not a claim of statistical
  unbiasedness.
- Round-5 theorem status: **`[PROVED]`** for every real two-dimensional
  symplectic hyperbolic return map,
  `|det(I-M^r)|^(-1/2)=Lambda^(-r/2)/|1-sigma^r Lambda^(-r)|`.  The tested
  half-density is therefore a universal leading factor rather than an
  arithmetic discriminator.  A 6,723-row primitive/repetition replay passes
  on all 2,241 frozen owners.  The project is retained as a
  methods/negative-control paper; Stage 2 remains unauthorized.
- Round-6 symbolic-Zeta status: **`[PROVED]`** for the separately typed
  unit-roof no-repeat symbolic suspension.  Its 747 frozen owners reproduce
  the primitive Euler product, trace exponential and `3 x 3` determinant
  exactly modulo `z^13`; collision parity gives precisely `z -> -z`.
  This typed control has formal tuple
  `(A0_FAIL,A1_PASS_ANALYTIC,A2_ANALYTIC_DETERMINANT,A3_FAIL,A4_FAIL)` and
  overall `ROUTE_A_REJECTED`.  The physical flight-length flow tuple remains
  unassigned.
- Round-7 family-theorem status: **`[PROVED]`** for every integer `q>=2`.
  The q-symbol no-repeat suspension has
  `det(I-u z A_q)=(1-(q-1)u z)(1+u z)^(q-1)`, and its primitive Euler,
  trace-exponential, and determinant constructions coincide exactly.  The
  replay covers `q=2,...,8`, 84 trace/count rows and 182 coefficient rows with
  zero mismatches.  This strengthens P25 into a universal negative-control
  theorem: exact A1--A2 wiring persists across an infinite non-arithmetic
  family, while the physical flow remains `UNASSIGNED`.

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
`NUMERICALLY_CERTIFIED` for only 9 rows in the historical Round-2 binary64
artifact.  Round 3 replaces that check with a 100-digit, three-scale direct
physical return-map calculation and certifies all 2,241 rows.  The batch-wide
half-density conclusion nevertheless remains `[NUMERICAL_OBSERVATION]` because
this is finite-cutoff numerical calibration, not an exact identity.

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

## Round-6 exact symbolic-Zeta calibrator

For the separately typed unit-roof suspension of the no-repeat collision shift,
let `A=J_3-I_3` and `z=exp(-s)`.  Oriented primitive cyclic words are owners;
reversal remains distinct, and repetitions are traversal powers.  Then

```text
zeta_0(z)  = det(I-zA)^(-1) = 1/((1-2z)(1+z)^2),
zeta_pi(z) = det(I+zA)^(-1) = zeta_0(-z)
           = 1/((1+2z)(1-z)^2).
```

All 747 frozen owners through length 12 match the exact Möbius counts.  Three
independent exact implementations agree coefficient by coefficient modulo
`z^13`, with zero mismatches.  The collision phase is therefore source-owned
but non-discriminative: it only changes `z` to `-z`.

This is an A1-to-A2 **symbolic calibrator**, not the physical Euclidean-flight-
length Gutzwiller--Voros zeta, the exact multiple-scattering determinant, or a
quantum-resonance calculation.  Its Route tuple is typed and may not be
transferred to the physical three-disk flow.

## Round-7 universal q-symbol theorem

Let `A_q=J_q-I_q` for any integer `q>=2`.  The eigenspaces of the all-ones
vector and its coordinate-sum-zero complement give

```text
tr(A_q^n)=(q-1)^n+(q-1)(-1)^n,
det(I-u z A_q)=(1-(q-1)u z)(1+u z)^(q-1).
```

Möbius inversion gives the exact oriented primitive-owner count for every
length, and the associated Euler product equals the reciprocal determinant.
For `u=-1`, collision parity remains exactly the substitution `z -> -z`.
The theorem holds for the whole family; the finite exact replay over seven q
values is a regression certificate, not the basis of the proof.

This result makes the negative-control conclusion stronger and cleaner:
determinant exactness alone cannot supply A0.  The family is formally typed
`(A0_FAIL,A1_PASS_ANALYTIC,A2_ANALYTIC_DETERMINANT,A3_FAIL,A4_FAIL)` and
rejected as a primary HP-Dynamics candidate.

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
- [executed result ledgers](results/README.md)
- [Round-2 conclusion](notes/round2_conclusion.md)
- [Round-2 validation](experiments/round2_validation.md)
- [Round-3 conclusion](notes/round3_conclusion.md)
- [Round-3 direct validation](experiments/round3_validation.md)
- [Round-4 conditioning audit](notes/round4_conditioning_audit.md)
- [Round-4 reproducibility receipt](experiments/round4_reproducibility_receipt.json)
- [Round-5 theorem and negative-control closure](notes/round5_universal_half_density_theorem.md)
- [Round-5 paper research spine](paper/round5_research_spine.md)
- [Round-5 reproducibility receipt](experiments/round5_reproducibility_receipt.json)
- [Round-6 symbolic-Zeta theorem](notes/round6_symbolic_zeta_theorem.md)
- [Round-6 typed Route-A audit](notes/round6_route_audit.md)
- [Round-6 freeze contract](experiments/round6_symbolic_zeta_freeze.json)
- [Round-6 validation](experiments/round6_validation.md)
- [Round-6 formal Route-A record](../../evaluations/route_a/THREE-DISK-NO-REPEAT-MASLOV-SYMBOLIC/2026-08-28-stage1.yaml)
- [Round-7 q-symbol family theorem](notes/round7_q_symbolic_family_theorem.md)
- [Round-7 paper research spine](paper/round7_research_spine.md)
- [Round-7 freeze contract](experiments/round7_q_symbolic_family_freeze.json)
- [Round-7 validation](experiments/round7_validation.md)
- [Round-7 formal Route-A record](../../evaluations/route_a/P25-Q-SYMBOL-NO-REPEAT-PHASE-CALIBRATOR/2026-08-28-round7.yaml)

No exact physical scattering determinant, physical-flow A2 test, or manuscript
is claimed.  The formal A1/A2 tuple belongs only to the explicitly typed
unit-roof symbolic suspension.
