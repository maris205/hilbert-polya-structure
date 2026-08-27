# Paper 26 — level-11 newform time change

Working title: *Level-11 Newform Periods as an Intrinsic Time Change of a Geodesic Flow*

## Current status

- ARS: **Stage 1 RESEARCH in progress; Rounds 2--4 executed reproducibly**.
- Proposal: **Stage 1 Classical Flow Baseline / Route A A0--A1**.
- The arithmetic one-form, positive time-density/slowness factor, reciprocal
  speed multiplier, generator, and exact period-variation formula are frozen.
- Round 2 exactly enumerated 125 primitive positive `LR` necklaces through the
  frozen word cutoff 9; 11 representatives have lower-left matrix entry
  divisible by 11.  Their matrices, primitive roots/exponents, and geodesic
  lengths are recorded alongside numerical one-form axis-period proxies, the
  corresponding explicit first-variation coefficients and signs, and controls.
- Two isolated runs were byte-identical with artifact-tree SHA-256
  `e635ee051ea25d543eb4f3fd72bce5ae4da95d64ee2ca9f90b2f5f81ba8a2da5`;
  all 7 unit tests passed.
- Round 3 proves that the newform one-form period is owned by an oriented
  `Gamma_0(11)` conjugacy class, reverses sign under inverse orientation, and
  is linear under repetition.  The finite regression layer checked 99 exact
  bounded-conjugacy rows and 44 direct translation-covariance rows; 5/5 tests
  and two byte-identical replays passed.  The maximum observed translation
  residual is `1.5543122344752192e-15`, and the Round-3 tree SHA-256 is
  `a3e71f86124ec8ae58f3971002fd3e0f11a0f06ccf3851e1f4ed4fad25d03841`.
- Round 4 proves the correctly normalized prime-to-11 Hecke relation on the
  **cycle pushforward**:
  `integral_(T_(p,*)C) alpha_f = a_p integral_C alpha_f`.  The double-coset
  right action decomposes the left side into an explicit finite sum of closed
  `Gamma_0(11)` geodesic owners; it does not select one primitive orbit.
- The frozen finite ledger for `p={2,3,5,7,13}` has 385/385 exact branch
  gluings, 320/320 exact eta-product coefficient identities, 138/138 finite
  cycle owners with exact primitive-root certificates, and 55/55 direct
  complex period-sum checks.  The largest primary numerical residual is
  `2.229752420147902e-14`.
- A genus-one cohomology theorem shows that every legitimate compactly
  extending closed-form control satisfies the same scalar Hecke relation.
  Hence the relation is structural but not discriminative evidence for a
  primitive Euler mechanism: `DISCRIMINATIVE_HECKE_EULER_EVIDENCE=STOP_SCOPED`.
- Round 4 passed 8/8 tests and two byte-identical full replays; artifact-tree
  SHA-256 is
  `4cd45da8e7fa82e4688bc6975dae44c4206837b40652979167432ffe7b07f20e`.
- Formal Route-A tuple: **unassigned**.
- Route B: `EVALUATION=NOT_RUN`; `INVOCATION_ALLOWED=false`.

## Frozen dynamical system

Let `Y_0(11)=Gamma_0(11)\H`, let `X_geo` be its unit-speed geodesic vector
field, and take the normalized weight-2 newform

```text
f(z) = eta(z)^2 eta(11z)^2 = q - 2q^2 - q^3 + ... .
```

Define `omega_f=2 pi i f(z) dz`, `alpha_f=Re(omega_f)`, and on `T^1Y_0(11)`
put `a(v)=alpha_f(v)`.  For

```text
rho_epsilon(v) = 1 + epsilon a(v),
X_epsilon = X_geo / rho_epsilon,
```

Here `rho_epsilon` is the time-density/slowness factor, not the speed.  The
speed multiplier relative to `X_geo` is `1/rho_epsilon`.  The cusp-form decay
makes `a` bounded.  The frozen positivity interval is
`|epsilon| < ||a||_infinity^(-1)`.  For an original closed geodesic `gamma`,

```text
T_epsilon(gamma) = ell(gamma) + epsilon integral_gamma alpha_f,
T_epsilon(gamma^r) = r T_epsilon(gamma).
```

Writing `rho X` instead would change the period law and is not this candidate.

## Research question and bold hypothesis

Can the first derivative of the time-changed dynamical zeta be decomposed into
Hecke/Euler factors using only the same primitive-geodesic ledger?

`PROVED`: the period of the Hecke **cycle pushforward** is `a_p` times the
original period.  This is a sum-valued correspondence identity.  It does not
say that an individual primitive closed geodesic has period `a_p`, and no
primitive orbit-to-prime correspondence is assumed.

## Round-4 Hecke gate and kill result

Round 2 registered a norm-matched generic smooth observable and a period
permutation. Round 4 separates these numerical controls from the stricter
same-owner Hecke control: only closed 1-forms on the same quotient participate
in the homological correspondence theorem.

The source-derived recurrence now exists on the correct owner. For
`beta_b=[[1,b],[0,p]]` and `beta_infinity=[[p,0],[0,1]]`, right multiplication
by a frozen hyperbolic owner permutes the branches; each permutation cycle
produces a closed `Gamma_0(11)` owner. Their signed periods sum to `a_p` times
the original signed period.

The strongest admissible generic control does not reject this relation. Since
`X_0(11)` has genus one, `T_p` acts by `a_p` on all of real compact cohomology;
therefore every smooth closed real 1-form extending over `X_0(11)` passes.
A deterministic nonmodular q-series control fails 302/320 exact coefficient
rows and every direct period comparison, but it has no quotient owner and is
not a valid same-class counterexample.

Thus `hecke_correspondence_cycle_relation=PROVED`, while
`primitive_euler_factorization=NOT_ESTABLISHED` and the discriminative Euler
interpretation is `STOP_SCOPED`.  A2 remains unrun.

## Files

- [Stage-1 research brief](notes/stage1_research_brief.md)
- [pipeline state](notes/pipeline_state.md)
- [Round-2 conclusion](notes/round2_conclusion.md)
- [Round-2 completion receipt](notes/round2_completion_receipt.md)
- [Round-3 conjugacy-owner theorem](notes/round3_conjugacy_owner_theorem.md)
- [Round-4 Hecke-correspondence theorem](notes/round4_hecke_correspondence_theorem.md)
- [Round-4 conclusion](notes/round4_conclusion.md)
- [Round-4 paper-facing research spine](paper/round4_research_spine.md)
- [results and artifact contract](results/README.md)
- [reproduction instructions](experiments/README.md)

The finite positive-word ledger is not a complete certificate of
`Gamma_0(11)` conjugacy classes.  No single-orbit Hecke rule, primitive Euler
factorization, dynamical-zeta A2 result, automorphic-`L` determinant identity,
prime/zero target match, formal Route-A tuple, or Route-B entry is claimed.
