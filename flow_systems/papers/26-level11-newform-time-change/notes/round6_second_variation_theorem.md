# P26 Round-6 inverse-paired second variation and quadratic Hecke moments

Date: **2026-08-28**

## Material Passport

- Origin Skill: `ars-codex:academic-research-suite`
- Origin Workflow: ARS Stage-1 theorem development plus deterministic
  experiment validation
- Mathematical owner: the frozen level-11 newform time change and the
  oriented primitive `Gamma_0(11)` flow-orbit convention of Rounds 3--5
- Verification status: formulas and finite-multiset moment criterion
  `[PROVED]`; generated period-weighted rows `[NUMERICAL_OBSERVATION]`;
  deterministic serialization `[NUMERICALLY_CERTIFIED / REPRODUCIBLE]`

This note answers the next-smallest question frozen at the end of Round 5.  It
does **not** construct the full dynamical zeta of the cusped time-changed flow,
enumerate all primitive conjugacy classes, prove global convergence or
continuation, count determinant roots, compare zeros, or run Route-A A2.

## Frozen source and product conventions

For an oriented primitive owner `gamma#`, write

```text
L = ell(gamma#),
I = integral_(gamma#) alpha_f,
T_epsilon(gamma#) = L + epsilon I.
```

The inverse owner has the same base length and the opposite signed one-form
period, hence the opposite first-order variation.  Its full deformed period is
`L-epsilon I`, not the negative of `L+epsilon I`.  Round 6 keeps
the reciprocal Ruelle and frozen-stability Selberg-type log products from
Round 5:

```text
log Z_R(s,epsilon)
  = sum_(gamma#) sum_(r>=1) exp(-sr T_epsilon(gamma#))/r,

log Z_S^fr(s,epsilon)
  = sum_(gamma#) sum_(r>=1)
      exp(-sr T_epsilon(gamma#))
      / (r(1-exp(-r ell(gamma#)))).
```

The second convention freezes the transverse stability multiplier of the
base return map.  It is not called the Selberg zeta of a deformed metric.

## Theorem 1 — canonical inverse-pair second variation

For one inverse pair `{gamma#,gamma#^(-1)}`, define

```text
K_R^(2)(s,L) = sum_(r>=1) r exp(-srL),

K_S^(2)(s,L) = sum_(r>=1)
  r exp(-srL)/(1-exp(-rL)).
```

Then

```text
d^2/d epsilon^2 log Z_R,pair(s,epsilon)|_0
  = 2s^2 I^2 K_R^(2)(s,L),

d^2/d epsilon^2 log Z_S,pair^fr(s,epsilon)|_0
  = 2s^2 I^2 K_S^(2)(s,L).
```

These formulas are exact for a finite owner family.  They also hold term by
term for an infinite owner family in a domain of absolute, locally uniform
convergence.  Evidence token: `[PROVED]`.

### Proof

At repetition `r`, the inverse-paired log term is

```text
exp(-sr(L+epsilon I))/r + exp(-sr(L-epsilon I))/r
  = 2 exp(-srL) cosh(sr epsilon I)/r.
```

Its first derivative at zero vanishes and its second derivative is

```text
2 s^2 r I^2 exp(-srL).
```

Thus inverse orientation cancels odd variations but adds even variations.
The two powers of the repeated period contribute `r^2`; the logarithmic
coefficient removes one factor, leaving `r`, not `1`.  Dividing by the frozen
stability denominator proves the second formula.

The result is orientation-even and nonnegative for real `s>0`.  It avoids the
noncanonical positive-word half-ledger required to make the first variation
nonzero.

## Theorem 2 — exact quadratic degree-moment criterion

Fix a Round-4 source pair `(M,p)`, put `L=ell(M)`, and let `delta_O` be its
primitive-certified Hecke cycle-owner instances.  If `d_O` is the branch-cycle
degree, define the quadratic moments

```text
Q_d(M,p) = sum_(O:d_O=d) I(delta_O)^2.
```

Let `lambda_p` be any scalar frozen before looking at the weighted zeta
residuals and depending only on `p`, not on `M` or `s`.  On the finite Hecke
output multiset, either canonical inverse-paired identity

```text
sum_O V^(2)(delta_O;s) = lambda_p V^(2)(M;s)
```

holds for every sufficiently large real `s` if and only if

```text
Q_1(M,p) = lambda_p I(M)^2,
Q_d(M,p) = 0 for every d>1.                         (QM)
```

The criterion is the same for the Ruelle and frozen-stability Selberg-type
kernels.  Evidence token: `[PROVED]`.

### Proof

Put `q=exp(-sL)`.  After removing the common factor `2s^2`, the Ruelle output
has coefficient at `q^n`

```text
n sum_(d|n) Q_d/d.
```

The source side has coefficient `n lambda_p I(M)^2`.  Therefore equality on
an interval is equivalent to

```text
sum_(d|n) Q_d/d = lambda_p I(M)^2  for every n>=1.
```

Möbius inversion gives `(QM)`.  For the frozen-stability Selberg-type kernel,
every divisor contribution at `q^n` has the same additional nonzero factor
`(1-exp(-nL))^(-1)`, so the identical argument applies.

The linear Hecke theorem

```text
sum_O I(delta_O) = a_p I(M)
```

does not state a sum-of-squares identity and cannot imply `(QM)`.  This is a
logical non-implication, not a theorem forbidding some independently proved
quadratic correspondence.

## Frozen scalar audits

Round 6 preregisters two primary finite audits:

1. `lambda_p=a_p`, which directly continues the Round-5 scalar proposal; and
2. `lambda_p=a_p^2`, the smallest orientation-even scalar made only from the
   already frozen Hecke eigenvalue.

The quantity `a_p^2-p=a_(p^2)` is retained only as an explicit **secondary
negative control**.  It is not promoted to the theoretical target, and no
choice among these scalars is fitted from the residuals.

## Finite source-locked result

The executable consumes the same two Round-4 inputs as Round 5:

```text
round4_hecke_cycle_ledger.csv
  f906df349b8f1fa2864fed592792e0fff63ba246a069179b7bd8cfdf46520662

round4_hecke_period_summary.csv
  c5de5c16c86d8db6ce7438c122deddb927d934bf0198fe3f72af4cbaf1233679
```

With repetition cutoff `R=4` and `s={0.125,0.25,0.5}`, it produces:

```text
inverse-pair/repetition rows                         552
quadratic degree-moment rows                         110
finite Hecke second-variation rows                   165
groups with nonunit quadratic mass                  51/55

lambda=a_p moment failures                          51/55
lambda=a_p^2 moment failures                        51/55
lambda=a_p Ruelle/Selberg row failures             153/165 each
lambda=a_p^2 Ruelle/Selberg row failures           153/165 each

secondary lambda=a_p^2-p moment failures            55/55
secondary Ruelle/Selberg row failures              165/165 each
```

Four `p=5`, `a_p=1` groups pass both primary finite audits numerically at all
three `s` values:

```text
LRRLRRR, LLRLLRLR, LLLRLLRLR, LLLRLRLLR.
```

For these rows the degree-5 real-period squares are at floating scale around
`10^-30`, while `Q_1/I(M)^2` is numerically one.  The individual periods come
from the Round-4 quadrature, so this is only `[NUMERICAL_OBSERVATION]`.  It is
not an exact homology-zero theorem, not a general `p=5` recurrence, and not an
Euler factor.

All twelve Round-6 tests pass.  Two isolated builds are byte-identical with
artifact-tree SHA-256:

```text
fc553aa18bc4fb54d70ea8f4c0bdbc41efc3c0905b3f2942c49e1f6f8c62f864
```

## Route and claim boundary

```text
ARS_STAGE=STAGE_1_RESEARCH
PROPOSAL_STAGE=STAGE_1_ROUTE_A_A0_A1
CANONICAL_INVERSE_PAIR_SECOND_VARIATION=PROVED
QUADRATIC_DEGREE_MOMENT_CRITERION=PROVED
FINITE_LOCAL_LOG_PRODUCT_AUDIT_ONLY=true
COMPLETE_PRIMITIVE_ENUMERATION=false
GLOBAL_ZETA_CONVERGENCE_OR_CONTINUATION=false
ROOT_COUNT_OR_ZERO_MATCHING_RUN=false
A2_DYNAMICAL_ZETA_EVALUATION=NOT_RUN
FORMAL_A0_A4_TUPLE=(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)
OVERALL_ROUTE_A_STATUS=ROUTE_A_EXPLORATORY
ROUTE_B_EVALUATION=NOT_RUN
ROUTE_B_INVOCATION_ALLOWED=false
```

The second variation is a useful canonical observable and a paper-level
advance, but the finite calculation does not satisfy Route-A A2's required
global determinant, frozen validation region, argument-principle root count,
missing/extra-zero report, cutoff/precision drift, or adversarial controls.
