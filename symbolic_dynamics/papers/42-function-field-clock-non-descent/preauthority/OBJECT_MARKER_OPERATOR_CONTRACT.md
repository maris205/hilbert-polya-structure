# Object, marker, clock, and operator contract

## Type table

| Type | Elements | Primitive relation | Clock | Marker | Owner |
|---|---|---|---|---|---|
| `ShiftPrimitiveNecklace_q` | aperiodic cyclic words over `F_q` | ordinary word power | `n log q` | `z^n` | full `q`-shift |
| `FiniteFieldPrimePolynomial_q` | monic irreducibles in `F_q[x]` | polynomial powers in the Euler ledger | `deg(P) log q` | degree marker | affine-line function-field zeta |
| `RationalPrimeAtom` | rational primes `p` | `p -> p^r` | `log p` | `z` per prime-loop traversal | separate rational-prime diagonal inventory |

Equal cardinalities between the first two types at each degree do not create a
canonical objectwise bijection. Neither type is identified with the third.

## Source ledger

For `gamma` of primitive length `n`, the source factor is

\[
 F_\gamma(s,z)=\left(1-z^n q^{-ns}\right)^{-1}.
\]

The source determinant and trace-log are

\[
 D_q(s,z)=1-zq^{1-s},
\]

\[
 -\log D_q(s,z)=\sum_{r\ge1}\frac{z^r}{r}q^{r(1-s)}
\]

for `|z q^(1-s)|<1`. The primitive product identity is formal in `z` and
analytic wherever absolute convergence is invoked.

## Rational-prime comparator

The target factor and marked trace-log are

\[
 F_p(s,z)=(1-zp^{-s})^{-1},
\]

\[
 -\log D_{\mathbb P}(s,z)
 =\sum_{r\ge1}\frac{z^r}{r}P(rs),
 \qquad P(s)=\sum_p p^{-s},
\]

on `Re(s)>1` and sufficiently small `|z|`. The target marker counts a
primitive rational-prime loop, not a source symbol.

## Necessary equality matrix

| Requirement | Source length `n` | Rational-prime target | Consequence |
|---|---:|---:|---|
| Weight/clock | `q^(-ns)` | `p^(-s)` | `p=q^n` |
| Primitive marker | `z^n` | `z` | `n=1` |
| Multiplicity at `n=1` | `N_q(1)=q` | one factor at `p=q` | collision of `q` source factors |
| Repetition | `z^(nr)q^(-nrs)` | `z^r p^(-rs)` | follows only if primitive marker and weight already agree |
| First trace-log coefficient | `q^(1-s)` | `P(s)` | unequal Dirichlet coefficients |

No theorem row claims that one condition alone exhausts every changed model.
The conjunction defines the frozen same-object descent obligation.

## Declared repair matrix

| Repair | Prime support | Clock | Marker | Multiplicity | Ownership | Classification |
|---|---|---|---|---|---|---|
| finite-field norm `q^n` | fails for `n>=2` | passes | fails for `n!=1` | fails at `n=1` | source-derived | exact negative projection |
| keep degree-one necklaces | only prime `q` | passes | passes | fails `q:1` | projected source | incomplete ledger |
| choose one degree-one necklace | only prime `q` | passes | passes | passes locally | projected source | single-factor positive control, not all primes |
| enumerate necklaces by rational primes | can pass by choice | fails exact source clock | fails source marker | can be arranged | external relabeling | forbidden post-hoc map |
| induce every primitive orbit to one return | label-dependent | clock can be stored | marker changed from `z^n` to `z` | requires new components | changed operator/object | no same-marker credit |
| finite-field prime-polynomial dictionary | function-field primes, not rational primes | passes | passes by degree | passes countwise | function-field owner | exact positive control |

## Ownership firewall

The scalar source determinant is not deficient as a function-field object.
The failure occurs when rational-prime factor semantics are demanded while all
source fields remain fixed. A rational-prime diagonal operator can realize the
target product, but it is a distinct countable inventory. Equality or
resemblance of displayed zeta notation cannot transfer primitive type,
marker, clock, or determinant ownership.
