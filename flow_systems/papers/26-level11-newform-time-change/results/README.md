# P26 generated results

## Round 4 — Hecke correspondence-cycle owner

- `round4_hecke_branch_owner_ledger.csv`: 385 exact rows for the right action
  of the 11 frozen owners on the standard double-coset branches at
  `p={2,3,5,7,13}`. Every row binds
  `beta_j M = gamma_j beta_(pi(j))` with an exact
  `gamma_j in Gamma_0(11)`.
- `round4_hecke_coefficient_ledger.csv`: 320 exact eta-product coefficient
  checks of `a_(pn)+p a_(n/p)=a_p a_n`. All 320 pass. The bounded deterministic
  nonmodular control fails 302 rows and is explicitly marked as lacking a
  quotient owner.
- `round4_hecke_cycle_ledger.csv`: 138 permutation-cycle owners
  `delta_O=beta_j M^|O| beta_j^(-1)`. All 138 are exact integral
  `Gamma_0(11)` matrices and all 138 pass the finite complete root search for
  primitivity.
- `round4_hecke_period_summary.csv`: 55 word/prime period-sum rows at q
  cutoffs 1536/1024 and Simpson panels 256/128. Maximum primary complex
  residual is `2.229752420147902e-14`; maximum comparison residual is
  `1.9479273482635503e-14`.
- `round4_summary.json` and `round4_artifact_manifest.json`: registered counts,
  evidence tokens, control interpretation, claim boundary, and artifact
  bindings.

The cycle-pushforward relation is `[PROVED]`; exact finite ledgers are
`NUMERICALLY_CERTIFIED`; quadrature residuals are `NUMERICAL_OBSERVATION`.
The genus-one same-owner closed control also passes by theorem, so
discriminative primitive-Euler evidence is `STOP_SCOPED`. A single-orbit
recurrence, global primitive Euler factorization, A2 dynamical-zeta evaluation,
formal Route-A tuple, and Route-B entry are not claimed.

## Round 3 — conjugacy owner

- `round3_conjugacy_owner_ledger.csv`: 99 exact rows from 11 selected
  Round-2 elements and nine bounded `Gamma_0(11)` conjugators.  Each row checks
  determinants, subgroup membership, trace, powers two and three, and inverse
  orientation over the integers.
- `round3_translation_covariance_ledger.csv`: 44 direct q-series quadrature
  checks under `z -> z+k`, `k=-2,-1,1,2`; maximum observed residual
  `1.5543122344752192e-15`.
- `round3_summary.json` and `round3_artifact_manifest.json`: the frozen counts,
  scope boundary, verdict, and SHA-256 bindings.

The analytic conjugacy/orientation/repetition result is `[PROVED]` in
`../notes/round3_conjugacy_owner_theorem.md`.  The finite integer regression is
`NUMERICALLY_CERTIFIED`; the binary64 period comparison is a
`NUMERICAL_OBSERVATION`.  Neither is a complete conjugacy-class enumeration or
a Hecke recurrence.

## Round 2 — finite positive-word experiment

Canonical generated artifacts are:

- `newform_timechange_variation_ledger.csv`: 11 selected positive-necklace
  representatives, exact matrix/primitive metadata, lengths, numerical
  one-form proxies, explicit signed first-variation coefficients
  `dT_epsilon/d epsilon|_0`, and every residual/control value;
- `simpler_parent_length_control.csv`: all 125 primitive positive hyperbolic
  necklaces through cutoff 9, including the 11 selected rows;
- `round2_summary.json`: configuration, counts, finite-ledger metrics, maximum
  residuals, and claim boundary; and
- `artifact_manifest.json`: SHA-256 bindings for the generator, tests,
  reproduction script, and the three primary data artifacts.

The 11 selected rows split by length as 1 at length 7, 4 at length 8, and 6 at
length 9.  Their newform-proxy RMS is `0.8557007383823421`.  The matched generic
control has the same finite-ledger RMS by construction.  Correlation with
length is `0.38226372301679423` for the newform proxy,
`0.8180749583713894` for the matched generic control, and
`-0.11520138109343742` after the deterministic period permutation.

Maximum observed binary64 cross-check differences are:

```text
q cutoff (48 versus 192)               1.5021317523178368e-13
quadrature (512 versus 1024 panels)     6.661338147750939e-16
basepoint shift                         2.6645352591003757e-15
orientation reversal                    1.7763568394002505e-15
direct M^2 repetition                   3.9968028886505635e-15
repeat q cutoff (2048 versus 4096)      1.5418777365994174e-12
repeat quadrature (256 versus 512)      2.220446049250313e-15
```

These are observed double-truncation/double-quadrature differences, not exact
zeros or rigorous error bounds.  The ledger status is
`NUMERICALLY_CERTIFIED` for the finite exact owner enumeration and
`NUMERICAL_OBSERVATION` for periods and controls.

No prime labels or zero data occur.  The finite positive-word ledger is not a
complete `Gamma_0(11)` conjugacy-class certificate.  Hecke/Euler evidence is
`HEURISTIC`, testability is `NOT_TESTABLE`, the formal Route-A tuple remains
`UNASSIGNED`, and Route B was not run.
