# P26 generated results

## Round 7 — exact `p=5` survivor classification

- `round7_exact_survivor_classification_ledger.csv`: four frozen survivor
  rows with regenerated exact degree-one/degree-five owners, rational
  `Y_0(11)` homology coordinates, compact-zero certificates, real-structure
  parity, exact finite moment status, and inherited numerical cross-checks.
- `round7_exact_homology_model.json`: the 12-coset, 24-arc Schreier model,
  relation rank 21, cusp direction, and compact/real-period decision rules.
- `round7_summary.json` and `round7_artifact_manifest.json`: exact 4/4 split,
  source locks, claim boundary, and source/output SHA-256 bindings.

All four Round-6 `p=5`, `a_p^2` positives are exact finite group-moment
survivors.  Two degree-five owners are full complex-period kernels; two are
nonzero classes with purely imaginary periods and hence only real-projection
kernels.  No row is a floating-quadrature artifact and none is unresolved.
The result is local to four frozen groups and does not promote A2 or open
Route B.

## Round 6 — inverse-paired second variation and quadratic Hecke moments

- `round6_inverse_pair_second_variation_ledger.csv`: 552 rows for the 138
  primitive-certified Round-4 cycle-owner instances, both inverse
  orientations paired canonically, and repetitions `r=1,2,3,4`.  It checks
  that the second derivative has the exact surviving factor `r` and that
  inverse contributions add rather than cancel.
- `round6_quadratic_degree_moment_ledger.csv`: 110 degree rows over 55
  word/prime groups, including zero-population degree-one bins where needed.
  It audits the exact all-`s` obligations `Q_1=lambda_p I(M)^2` and `Q_d=0`
  for `d>1` for both primary scalar proposals.
- `round6_hecke_second_variation_ledger.csv`: 165 rows at
  `s={0.125,0.25,0.5}` and repetition cutoff `R=4`.  Both `lambda_p=a_p`
  and `lambda_p=a_p^2` fail 153/165 rows for each kernel.  The explicitly
  secondary `a_p^2-p` control fails 165/165 rows.
- `round6_summary.json` and `round6_artifact_manifest.json`: counts, frozen
  source hashes, analytic statements, Route boundary, and artifact bindings.

The inverse-pair formulas and finite-multiset moment criterion are `[PROVED]`;
as recorded at the end of Round 6, the period-weighted outcomes, including
four `p=5` survivors, were `[NUMERICAL_OBSERVATION]`.  Round 7 upgrades those
four rows exactly.  The formal tuple is
`(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)` with overall
`ROUTE_A_EXPLORATORY`.  A2 is `FAIL/NOT_TESTABLE`: no complete primitive
population, global product/continuation, root count, or zero comparison was
run.

## Round 5 — zeta first variation and degree-moment obstruction

- `round5_zeta_repetition_ledger.csv`: 1,104 rows from 138
  primitive-certified Round-4 Hecke cycle-owner instances in the finite output
  multiset, two inverse orientations, and zeta repetitions `r=1,2,3,4`.  It
  records Hecke cycle degree `d` separately, verifies the
  `rL`/`rI` laws and cancellation of the logarithmic `1/r`, and pairs both
  Ruelle and frozen-stability Selberg-type derivative contributions to exact
  zero by orientation sign.
- `round5_degree_moment_ledger.csv`: 110 degree-aggregated rows over the 55
  word/Hecke-prime groups.  It records the necessary-and-sufficient all-`s`
  obligations `P_1=a_p I(M)` and `P_d=0` for `d>1`, with an explicit
  zero-owner degree-one row when necessary, separately for the real
  newform period, the complex period, and the genus-one closed-form control.
- `round5_hecke_zeta_variation_ledger.csv`: 165 one-sided audit rows at
  `s={0.125,0.25,0.5}` and repetition cutoff `R=4`.  All 55 unweighted Hecke
  sums pass, while 153/165 rows fail the naive Ruelle recurrence and 153/165
  fail the naive frozen-Selberg recurrence.
- `round5_summary.json` and `round5_artifact_manifest.json`: registered
  counts, source-input hashes, evidence tokens, exact analytic boundaries,
  and artifact bindings.

The inverse-pair zero and the degree-moment criterion are `[PROVED]`.  The
owner/repetition bookkeeping is `[NUMERICALLY_CERTIFIED]`; the weighted period
residuals are `[NUMERICAL_OBSERVATION]` because they consume Round-4
quadratures.  The positive-word orientation surface is explicitly a
noncanonical half-ledger.  A global zeta construction/continuation, Route-A
A2, primitive Euler factorization, formal Route tuple, and Route B are not
claimed.

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
- `round4_hecke_cycle_ledger.csv`: 138 permutation-cycle owner instances
  `delta_O=beta_j M^|O| beta_j^(-1)`. All 138 are exact integral
  `Gamma_0(11)` matrices and all 138 pass the finite complete root search for
  primitivity.  They are output-multiset instances; full cross-instance
  `Gamma_0(11)` conjugacy canonicalization is not claimed.
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
