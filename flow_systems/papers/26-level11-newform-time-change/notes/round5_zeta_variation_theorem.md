# P26 Round-5 zeta first-variation and no-Euler theorem

Date: **2026-08-27**

Evidence boundary: this note derives first variations for an explicitly frozen
primitive-orbit product and proves what the Round-4 Hecke cycle identity does
and does not imply.  It does not construct a global meromorphic zeta for the
noncompact time-changed flow, run Route-A A2, or identify an automorphic
Euler factor.

## Source and convention lock

Let

```text
Gamma = Gamma_0(11),
T_epsilon(gamma) = ell(gamma) + epsilon I(gamma),
I(gamma) = integral_gamma alpha_f.
```

The owner `gamma#` is an **oriented primitive flow orbit**, equivalently the
oriented `Gamma` conjugacy owner frozen in Round 3.  Its `r`-fold traversal is
`gamma#^r`; `r` is the zeta repetition index.

Round 5 uses the reciprocal-product convention

```text
log Z_R(s,epsilon)
  = sum_(gamma#) sum_(r>=1)
      exp(-s r T_epsilon(gamma#)) / r.                 (R)
```

Thus `Z_R=product_(gamma#)(1-exp(-sT_epsilon(gamma#)))^(-1)` wherever the
product converges.  Ruelle's 1976 paper writes the nonreciprocal product;
changing between the two conventions only changes the sign of the
logarithmic derivative.  It changes neither the exact-zero theorem nor the
missing-obligation theorem below.

The second frozen convention retains the base transverse return map:

```text
log Z_S^fr(s,epsilon)
  = sum_(gamma#) sum_(r>=1)
      exp(-s r T_epsilon(gamma#))
      / (r (1-exp(-r ell(gamma#)))).                    (S)
```

Equivalently it is the reciprocal formal product

```text
product_(gamma#) product_(k>=0)
  (1-exp(-s T_epsilon(gamma#)-k ell(gamma#)))^(-1).
```

This is called **Selberg-type with frozen stability**, not the Selberg zeta of
a deformed metric.  A positive time reparametrization changes the traversal
time but not the first-return map on a transverse section.  Hence the base
stable multiplier `exp(-ell(gamma#))` is held fixed.

All analytic statements below are exact for a finite primitive-owner family.
They also hold term by term for an infinite inverse-closed family in any
domain of absolute/local-uniform convergence.  Establishing such a global
domain for the full time-changed, cusped quotient is outside Round 5.

## Theorem 1 — primitive/repetition first variation

Define, for `s>0`, `L>0`,

```text
K_R(s,L) = sum_(r>=1) exp(-s r L),

K_S(s,L) = sum_(r>=1)
  exp(-s r L) / (1-exp(-r L)).
```

For either a finite primitive family or a locally uniformly convergent
infinite family,

```text
d/depsilon log Z_R(s,epsilon)|_(epsilon=0)
  = -s sum_(gamma#) I(gamma#) K_R(s,ell(gamma#)),

d/depsilon log Z_S^fr(s,epsilon)|_(epsilon=0)
  = -s sum_(gamma#) I(gamma#) K_S(s,ell(gamma#)).
```

Evidence token: `[PROVED]`.

### Proof

For a fixed primitive owner and repetition,

```text
d/depsilon [ exp(-s r (L+epsilon I)) / r ]|_0
  = -s I exp(-s r L).
```

The period of the repeated path is `rI`; the `1/r` log-series coefficient
cancels that factor.  This is why the primitive owner must remain separate
from its repetitions.  Dividing by the epsilon-independent frozen stability
denominator proves the second formula.

## Theorem 2 — inverse orientation kills the canonical first variation

Suppose the primitive family is closed under inverse orientation.  Then

```text
ell(gamma#^(-1)) = ell(gamma#),
I(gamma#^(-1))   = -I(gamma#).
```

Consequently,

```text
d/depsilon log Z_R(s,epsilon)|_0    = 0,
d/depsilon log Z_S^fr(s,epsilon)|_0 = 0.
```

Evidence token: `[PROVED]`.

### Proof

For every primitive owner, inverse orientation is another primitive forward
flow orbit.  At each repetition `r`, the two log terms are proportional to

```text
exp(-s r (L+epsilon I)) + exp(-s r (L-epsilon I)),
```

with the same log coefficient and, for (S), the same frozen stability
denominator.  This expression is even in `epsilon`, so its first derivative
vanishes.  Equivalently, the two terms in Theorem 1 cancel.

The theorem applies to `alpha_f` and to every real 1-form control, including
`3 Re(omega_f)+4 Im(omega_f)`.  It is not a fitted cancellation.

An unoriented geometric geodesic does not avoid the issue: the periods
`L+epsilon I` and `L-epsilon I` differ, so one cannot attach a single
time-changed period to the unoriented curve without choosing an orientation.
Keeping only the positive-word orientation therefore defines an audit
half-ledger, not the canonical primitive-orbit zeta of the flow.

## Theorem 3 — Hecke degree is not zeta repetition

Let `M` be a Round-4 primitive source owner, of length `L`, and let `O` be a
cycle of the right-action permutation with degree `d_O`.  The Round-4 output

```text
delta_O = beta_j M^(d_O) beta_j^(-1)
```

has base length

```text
ell(delta_O) = d_O L.
```

Nevertheless, each of the 138 frozen `delta_O` instances has an exact finite
`Gamma_0(11)` primitive-root certificate.  Therefore `d_O` is a degree of the
Hecke branch cycle, not the zeta repetition of that primitive-certified
instance.  The zeta repetitions are the separate powers `delta_O^r`, with
length `r d_O L` and period `r I(delta_O)`.  Full cross-instance
`Gamma_0(11)` conjugacy canonicalization is not run, so 138 is an
output-multiset count, not a claim of 138 globally distinct conjugacy owners.

Evidence tokens: the length statement and owner separation are `[PROVED]`;
the 138 finite subgroup-primitivity certificates are
`[NUMERICALLY_CERTIFIED]` exact-integer checks.

## Theorem 4 — exact missing degree-moment obligation

For one source pair `(M,p)`, group the Hecke output periods by branch-cycle
degree:

```text
P_d = sum_(O: d_O=d) I(delta_O).
```

Round 4 proves only

```text
sum_d P_d = a_p I(M).                                  (H)
```

Consider the one-sided oriented audit family and the naive desired identity

```text
sum_O V(delta_O;s) = a_p V(M;s)                        (Z)
```

for either the Ruelle or frozen-stability Selberg-type first-variation
kernel.  On this finite output multiset, (Z) holds for every sufficiently
large real `s` if and only if

```text
P_1 = a_p I(M),
P_d = 0 for every d>1.                                  (M)
```

Evidence token: `[PROVED]`.

### Proof for the Ruelle kernel

Put `q=exp(-sL)`.  The output kernel sum is

```text
sum_d P_d sum_(r>=1) q^(dr).
```

The coefficient of `q^n` is `sum_(d|n) P_d`.  The source side has coefficient
`a_p I(M)` for every `n>=1`.  Equality on an interval of `q` therefore gives

```text
sum_(d|n) P_d = a_p I(M)  for every n>=1.
```

Möbius inversion yields exactly (M), and (M) plainly implies the identity.

### Proof for the frozen-stability Selberg-type kernel

Now the term of degree `d` and repetition `r` is

```text
q^(dr) / (1-exp(-drL)).
```

At power `q^n`, the extra denominator is the same nonzero number
`1-exp(-nL)` for every divisor `d` of `n`.  Hence the coefficient equality
reduces to the identical divisor-sum condition and the same Möbius-inversion
proof applies.

### No-implication consequence

The homological Hecke relation (H) is one unweighted constraint.  It neither
states nor implies the degree-wise conditions (M):

- for mixed degrees, (H) underdetermines the length-kernel weighted sum;
- for a uniform degree `d>1`, (H) puts the entire period sum at the shifted
  kernel `K(s,dL)`, not at `K(s,L)`.

Thus

```text
HECKE_CYCLE_PERIOD_RELATION_IMPLIES_ZETA_RECURRENCE=false,
PRIMITIVE_EULER_FACTORIZATION=NOT_ESTABLISHED.
```

This is a logical non-implication theorem, not a statement that some other,
independently supplied degree-moment theorem could never exist.

## Frozen finite ledger

Round 5 consumes the source-bound Round-4 files without recomputing or
relabeling owners:

```text
round4_hecke_cycle_ledger.csv
  SHA-256 f906df349b8f1fa2864fed592792e0fff63ba246a069179b7bd8cfdf46520662

round4_hecke_period_summary.csv
  SHA-256 c5de5c16c86d8db6ce7438c122deddb927d934bf0198fe3f72af4cbaf1233679
```

The frozen parameters and counts are

```text
source positive-word owners                         11
Hecke word/prime groups                             55
primitive-certified Hecke cycle-owner instances   138
inverse orientations per owner                       2
zeta repetition cutoff R                             4
orientation/repetition rows                       1104
degree-moment rows, including absent d=1 bins     110
s values                               0.125, 0.25, 0.5
one-sided Hecke-zeta rows                           165
```

Every one of the 55 groups still passes the unweighted Round-4 Hecke-period
relation.  Their degree profiles are

```text
mixed-degree groups                                 38
uniform groups, all at a nonunit degree             17
```

For the one-sided alpha-period audit:

```text
groups violating the all-s degree moments         51 / 55
groups passing only as numerical observations       4 / 55
finite Ruelle rows failing the naive recurrence   153 / 165
finite Selberg-type rows failing it                153 / 165
maximum Ruelle residual                    0.5496235070209148
maximum Selberg-type residual              0.5504742842041297
```

The four group-level numerical passes repeat at the three `s` values, giving
the 12 non-failing finite rows.  They do not establish a general recurrence.
Complex periods and the same-owner closed control each violate the all-s
degree moments in 53/55 groups.  These weighted residuals inherit the
Round-4 quadrature status `[NUMERICAL_OBSERVATION]`.

The inverse-paired 1,104-row ledger checks the distinct primitive `d` and
zeta-repetition `r` fields, the `rI`/`rL` laws, cancellation of the log
`1/r`, both frozen kernels, and exact sign pairing.  It is a finite
`[NUMERICALLY_CERTIFIED]` bookkeeping check; Theorems 1--4 do not depend on
the numerical residuals.

## Source audit

Primary sources checked for this convention on 2026-08-27:

1. David Ruelle, *Zeta-Functions for Expanding Maps and Anosov Flows*,
   Inventiones Mathematicae 34 (1976), 231--242,
   https://doi.org/10.1007/BF01403067.  The introduction explicitly defines
   the product over primitive periodic-flow orbits and displays the associated
   Selberg product for constant negative curvature.  The locally retained PDF
   is
   `../../2-flow-zeta/notes/sources/ruelle_1976_zeta_anosov_flows.pdf`,
   SHA-256
   `a48105428d3c9eff681e7b017614976a0aec02ff2911f89f5484243a3d26652e`.
2. David Fried, *The Zeta Functions of Ruelle and Selberg. I*, Annales
   scientifiques de l'Ecole Normale Superieure 19 (1986), 491--517,
   https://doi.org/10.24033/asens.1515.  Section 2 separates prime periodic
   orbits from their finite covers/multiplicity and gives the Ruelle and
   Selberg product representations.  The locally retained PDF is
   `../../2-flow-zeta/notes/sources/fried_1986_ruelle_selberg_i.pdf`, SHA-256
   `c603627f3754aa103714d0efcca1759a35c38d796619f0d761a6b1475b1e958c`.

The Round-4 Manin, Merel, and LMFDB source locks continue to own the Hecke
cycle-period theorem.  Neither Ruelle nor Fried supplies the new Hecke
degree-moment conditions; those conditions are derived above from the frozen
product.

## Route and manuscript boundary

```text
ARS_STAGE=STAGE_1_RESEARCH
PROPOSAL_STAGE=STAGE_1_ROUTE_A_A0_A1
LOG_ZETA_FIRST_VARIATION=PROVED_FOR_FINITE_OR_ABSOLUTELY_CONVERGENT_FAMILY
CANONICAL_INVERSE_PAIRED_FIRST_VARIATION=PROVED_EXACT_ZERO
HECKE_DEGREE_MOMENT_CRITERION=PROVED
HECKE_PERIOD_RELATION_IMPLIES_ZETA_RECURRENCE=false
ONE_SIDED_POSITIVE_WORD_ZETA=NONCANONICAL_AUDIT_HALF_LEDGER
DISCRIMINATIVE_HECKE_EULER_EVIDENCE=STOP_SCOPED
PRIMITIVE_EULER_FACTORIZATION=NOT_ESTABLISHED
GLOBAL_ZETA_CONTINUATION=NOT_RUN
A2_DYNAMICAL_ZETA_EVALUATION=NOT_RUN
FORMAL_A0_A4_TUPLE=UNASSIGNED
ROUTE_B_EVALUATION=NOT_RUN
ROUTE_B_INVOCATION_ALLOWED=false
```

The paper-level result is now a theorem/obstruction chain: the one-form time
change has an exact owner and Hecke cycle relation, but the canonical oriented
zeta first variation vanishes by inverse pairing; a one-sided orientation
choice is noncanonical and still lacks the degree moments required for a
primitive Euler recurrence.
