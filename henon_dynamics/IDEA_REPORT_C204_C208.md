# Route-A idea report: C204--C208

Date: 2026-08-27

Source commit: `d108ef46fea7a8f62490a69071a83fcbda7c113b`.

Evaluator: `flow_systems/skills/route-a-evaluator.md`, v0.2.0, SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.

Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Design objective

This round applies the large-step rule to five independent dynamical owners:
finite-field linear maps, a non-sofic context-free shift, a linear shear PDE,
a nonlinear diffusion PDE, and a continuous-time branching process.  No paper
is a chapter, corollary, or parameter slice of another paper.

`NEW` below means only that C1--C203 contains no package with the same frozen
owner.  It is not a literature-priority claim.  Classical sources retain
ownership of the underlying results.  Each retained package contributes a
convention-locked all-parameter synthesis, a complete boundary and stopping
atlas, independently replayable exact evidence, a full paper, and a strict
Route-A decision.

## Collision scan, kills and pivots

- **All finite linear maps replace a narrow LFSR or cellular-automaton paper.**
  C204 uses rational canonical form to treat every matrix over every finite
  field, including singular and inseparable cases.  Rule 90 and finite-field
  multiplication appear only as controls; the owner is the full linear
  endomorphism family.
- **The Dyck shift is retained precisely because it is non-sofic.**  C205 is
  not another finite cover, S-gap shift, or rational renewal determinant.  Its
  source zeta is algebraic and nonrational, with a context-free circular-code
  owner, an all-period ledger, a dominant-pole regime, and a branch-point
  boundary.
- **Couette shear is retained as a PDE semigroup rather than a finite affine
  shear.**  C206 owns the exact Fourier characteristic flow and the cubic-time
  dissipation geometry on `T x R`.  It does not borrow the nonlinear Couette
  stability theorem or a finite modular shear clock.
- **Barenblatt is enlarged across the entire exponent range.**  C207 keeps
  compact support, the Gaussian interface, algebraic tails, exact mass and
  moment normalization, moment-divergence thresholds, pressure geometry and
  rescaled stationarity in one theorem.  It is not a claim about classifying
  arbitrary Cauchy solutions.
- **The branching paper keeps the full three-regime process.**  C208 includes
  the exact transition law for every initial population and all critical,
  pure-birth, pure-death and zero-rate boundaries, together with the
  subcritical, critical and supercritical limit laws.  It is not another
  finite orthogonal-polynomial Markov spectrum.
- **Rejected near-collisions.**  Open Toda repeated C196's Lax/scattering
  architecture; conjugate gradients remained too close to C201; directed
  Laplacian forests remained too close to C203; KdV and Duffing repeated recent
  elliptic traveling-wave/action-atlas forms; Gordon--Newell and Tsetlin were
  sound but would add another finite Markov-operator package to an already
  dense lane.  The all-data `p`-system was deferred because a single wave-family
  sign error would compromise its entire Riemann atlas in this release window.

No retained system intrinsically labels primitive trajectories by rational
primes, realizes prime powers as repetitions, or supplies a logarithmic prime
clock.  Exact source zeta functions, semigroups and probability generating
functions retain their native meanings; no arithmetic interpretation is
manufactured.

## Frozen independent theorem increments

### C204 -- rational-canonical dynamics of every finite linear map

For every finite field `F_q`, dimension and matrix `A`, derive every iterate
fixed count from the invariant factors by

```text
#Fix(A^n) = q^(sum_i deg gcd(f_i, X^n - 1)).
```

Split the primary zero factors from the invertible factors to identify the
complete periodic subspace and exact maximal preperiod.  Close exact periods,
cycle counts, the finite Artin--Mazur zeta and the full-function Koopman
characteristic polynomial, retaining nilpotent, nonsemisimple, inseparable and
invertible boundaries.

### C205 -- algebraic zeta and primitive growth of the Dyck shift

Freeze the edge-type one-vertex, `N`-loop Dyck shift.  Starting from its
context-free circular-code equation, close the exact algebraic zeta

```text
2(1 + sqrt(1 - 4 N z^2)) /
  (1 - 2 N z + sqrt(1 - 4 N z^2))^2,
```

all fixed and primitive counts, entropy, the `N>1` dominant double pole and
primitive-orbit asymptotic, both algebraic branch points, and the `N=1` full
two-shift degeneration.  Linear-word and bi-infinite periodic admissibility
are kept distinct.

### C206 -- exact Couette mixing and enhanced-dissipation semigroup

For `f_t + a y f_x = nu Delta f` on `T x R`, freeze one Fourier convention and
derive the exact Fourier-sector propagator.  Close its semigroup composition,
the exact nonzero-sector norm

```text
exp(-nu (k^2 t + a^2 k^2 t^3 / 12)),
```

the `nu^(-1/3)` enhanced-dissipation scale, inviscid mixing, every
`a=0`, `nu=0`, `k=0` and `t=0` boundary, the periodic-state classification,
and the non-trace-class stopping line on the noncompact channel.

### C207 -- full-exponent one-dimensional Barenblatt atlas

For `u_t=(u^m)_{xx}`, `m>0`, and fixed positive mass, classify every centered
nonnegative first-kind zero-flux integrable self-similar profile.  The theorem
unifies compact-support profiles for `m>1`, the Gaussian at `m=1`, and
full-support algebraic tails for `0<m<1`; it gives exact Beta-function mass
constants and absolute moments, the sharp threshold
`r < (1+m)/(1-m)`, the second-moment boundary `m=1/3`, pressure/free-boundary
geometry, rescaled stationarity and the precisely delimited entropy-dissipation
range.

### C208 -- complete linear birth--death branching process

For every pair of nonnegative per-particle birth/death rates and every initial
population, close the probability-generating-function semigroup, the
one-ancestor zero-modified geometric law, and the exact multi-ancestor
binomial-survivor/negative-binomial mixture.  Derive all moments and the
subcritical quasi-stationary geometric law, critical Yaglom exponential
scaling, and supercritical martingale-limit atom/gamma mixture.  Pure birth,
pure death, critical, zero-rate, zero-population and zero-time boundaries are
part of the theorem.

## Frozen strict expectations

| paper | A0 | A1 | A2 | A3 | A4 | overall |
|---|---|---|---|---|---|---|
| C204 | `A0_FAIL` | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |
| C205 | `A0_FAIL` | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_FAIL` | `ROUTE_A_REJECTED` |
| C206 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |
| C207 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FAIL` | `ROUTE_A_REJECTED` |
| C208 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FAIL` | `ROUTE_A_REJECTED` |

C204 and C205 have native primitive-orbit ledgers, but neither has the A0
arithmetic owner and neither source zeta is the target zeta.  C206's inviscid
unitary is a candidate-local source operator only.  These coordinates are not
combined, every Route-B flag remains false, and final tuples are governed by
the package evaluator records.
