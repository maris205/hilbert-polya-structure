# P26 Round-7 exact homology classification of the four `p=5` survivors

Date: 2026-08-28

Evidence status: **PROVED** for the exact homology and real-structure
statements; the inherited q-series quadratures remain
`NUMERICAL_OBSERVATION` cross-checks.

## 1. Question inherited from Round 6

For a source owner `M`, the Round-6 inverse-pair second variation uses the
square of the real newform period

```text
I_R(M) = Re integral_M 2 pi i f(z) dz,
f(z) = eta(z)^2 eta(11z)^2.
```

At `p=5`, where `a_5=1`, four finite Hecke output groups passed the numerical
`lambda_p=a_p^2` quadratic degree-moment audit:

```text
LRRLRRR, LLRLLRLR, LLLRLLRLR, LLLRLRLLR.
```

Each group has one degree-one cycle and one degree-five cycle.  Numerical
survival requires

```text
I_R(delta_1)^2 = I_R(M)^2,
I_R(delta_5)^2 = 0.
```

Round 7 asks whether these two relations are exact source identities or
binary64 quadrature accidents.  No target primes, Riemann zeros, or fitted
thresholds are admissible.

## 2. Exact homology model

Work in

```text
PSL(2,Z) = <s,r | s^2=r^3=1>.
```

The right cosets of `Gamma_0(11)` are identified with `P^1(F_11)` by the
projective bottom row.  A deterministic Schreier transversal gives:

```text
right cosets                                      12
Schreier arcs                                     24
tree arcs killed                                  11
relation-matrix rows                              35
relation-matrix rank over Q                       21
dim H_1(Y_0(11),Q)                                 3
dim H_1(X_0(11),Q)                                 2
```

The 35 rows consist of the rewritten `s^2` and `r^3` relations and the tree
relations.  Exact fraction row reduction produces three independent rational
homology coordinates.  In the frozen coordinate basis, the cusp loop
`T=[[1,1],[0,1]]` is

```text
p_infinity = (-1,0,0).
```

Compactification quotients its rational span.  The loop at the other cusp is
checked to lie in the same span.  Hence an owner has zero compact class
exactly when its three-coordinate vector is proportional to `p_infinity`.

Every owner matrix is converted to an `s,r` word by an exact Euclidean
decomposition and then Schreier-rewritten.  The reconstructed word product is
required to equal the matrix up to the central sign.  No floating-point
arithmetic enters this layer.

## 3. Real structure and the real-period kernel

Let

```text
kappa(z) = -conjugate(z),
kappa_*(a,b;c,d) = (a,-b;-c,d).
```

The newform has real Fourier coefficients, so for
`omega_f=2 pi i f(z)dz`,

```text
integral_(kappa C) omega_f = conjugate(integral_C omega_f).
```

It follows that if

```text
kappa_*[C] = -[C] in H_1(X_0(11),Q),
```

then the complex period is purely imaginary and `I_R(C)=0` exactly.  If the
compact class itself vanishes, the full complex period vanishes because the
cusp form extends holomorphically across the cusps.  Conversely, on the
genus-one compact curve `X_0(11)`, integration of its nonzero holomorphic
one-form embeds rational homology into its period lattice.  Thus a nonzero
compact class cannot have zero full complex period.

For the degree-one condition, write `v^+=v+kappa_*v`.  The real period factors
through this invariant projection.  Equality of the source and degree-one
`v^+` classes modulo the cusp direction proves equality of their real periods,
and therefore of their squares, without quadrature.

## 4. Theorem

**Theorem (exact classification of all four frozen survivors).**  For each of
the four frozen `p=5` Hecke groups:

1. the degree-one output and source have the same conjugation-invariant
   compact homology class, hence
   `I_R(delta_1)=I_R(M)` exactly;
2. the degree-five output has zero real period exactly; and therefore
3. because `a_5^2=1`, the complete finite quadratic moment conditions
   `Q_1=a_5^2 I_R(M)^2` and `Q_5=0` hold exactly.

The degree-five outputs split into two different mechanisms:

| source word | `H_1(Y_0(11),Q)` coordinates | compact class | exact period character |
|---|---:|---|---|
| `LRRLRRR` | `(-9,0,0)` | zero | full complex period zero |
| `LLRLLRLR` | `(-20,0,0)` | zero | full complex period zero |
| `LLLRLLRLR` | `(-23,1,-2)` | nonzero | purely imaginary, nonzero |
| `LLLRLRLLR` | `(-23,1,-2)` | nonzero | purely imaginary, nonzero |

For the last two rows, conjugation sends the coordinate vector to
`(23,-1,2)`, its exact negative.  Their Round-4 imaginary value near
`-2.917633233876991` is therefore consistent with, but is not used to prove,
the nonzero purely imaginary conclusion.

Consequently:

```text
frozen survivors exactly classified                 4/4
exact finite a_p^2 group-moment survivors            4/4
full complex source kernels                          2/4
real-projection-only kernels                         2/4
floating-quadrature artifacts                        0/4
unresolved rows                                      0/4
```

## 5. Interpretation

The result upgrades four numerical observations to exact source-side
identities, but it does not supply a primitive Euler mechanism.  Indeed, the
two mechanisms are ordinary genus-one topology and conjugation parity:

- a compact-homology zero; or
- a nonzero anti-invariant class annihilated by taking the real part.

They do not encode an intrinsic rational-prime-to-primitive-orbit map.  The
classification therefore strengthens the local paper result while also
making the Route-A boundary sharper: these finite positives are structural
kernels, not evidence for A2 root matching.

## 6. Scope boundary

This theorem classifies four pre-frozen cycle owners only.  It does not:

- enumerate all primitive `Gamma_0(11)` conjugacy classes;
- deduplicate the full Hecke output population globally;
- construct or continue a global dynamical determinant;
- prove a primitive Euler factorization;
- run a root count, zero match, or cutoff/precision drift campaign;
- use target-prime or Riemann-zero data; or
- authorize Route B.

The formal tuple remains

```text
(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL),
```

with overall status `ROUTE_A_EXPLORATORY`.

## 7. Reproducibility

The builder derives the degree-one and degree-five owners from the exact
Round-4 right action, checks the SHA-locked Round-4 and Round-6 inputs, and
performs all homology calculations over `fractions.Fraction`.  Thirteen tests
cover the group model, exact decomposition, cusp quotient, four owner
certificates, real-structure split, fail-closed validation, and Route boundary.
Two isolated artifact trees are byte-identical with SHA-256

```text
bdfa8f5baaeef47f1bfd8482e8b459d2bd0606cdbb9cdcf0c441a8f65829d678.
```

Run `experiments/reproduce_round7.sh` to verify the canonical artifacts or
`experiments/reproduce_round7.sh --refresh` to refresh them explicitly.
