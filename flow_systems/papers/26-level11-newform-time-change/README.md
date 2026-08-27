# Paper 26 — level-11 newform time change

Working title: *Level-11 Newform Periods as an Intrinsic Time Change of a Geodesic Flow*

## Current status

- ARS: **Stage 1 RESEARCH in progress; Rounds 2--3 executed reproducibly**.
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

`HEURISTIC`: newform periods along primitive closed geodesics may satisfy a
useful Hecke recurrence.  They are not known to equal Hecke eigenvalues `a_p`,
and no primitive orbit-to-prime correspondence is assumed.

## Round-2 kill-gate result

Replace `alpha_f` by a norm-matched generic smooth bounded observable and, in a
separate control, permute the newform periods among primitive orbits.  If an
Euler-factor score survives or no exact Hecke recurrence can be derived without
prime labels, stop the arithmetic interpretation.

The deterministic finite-ledger controls are now present: a bounded
PSL2Z-invariant `j`-based observable was RMS-matched on the selected ledger,
the newform periods were cyclically permuted, and all 125 parent necklaces form
a simpler length control.  These are numerical controls, not a Hecke test.  No
source-derived recurrence or prime owner exists, so
`hecke_euler_evidence_status=HEURISTIC` and
`hecke_euler_testability=NOT_TESTABLE` remain unchanged.

## Files

- [Stage-1 research brief](notes/stage1_research_brief.md)
- [pipeline state](notes/pipeline_state.md)
- [Round-2 conclusion](notes/round2_conclusion.md)
- [Round-2 completion receipt](notes/round2_completion_receipt.md)
- [Round-3 conjugacy-owner theorem](notes/round3_conjugacy_owner_theorem.md)
- [results and artifact contract](results/README.md)
- [reproduction instructions](experiments/README.md)

The finite positive-word ledger is not a complete certificate of
`Gamma_0(11)` conjugacy classes.  No automorphic-`L` identity, prime/zero data,
Riemann target match, formal Route-A tuple, or Route-B entry is claimed.
