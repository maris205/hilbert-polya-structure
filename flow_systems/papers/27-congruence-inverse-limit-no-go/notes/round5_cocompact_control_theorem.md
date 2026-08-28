# P27 Round-5 theorem — factorial period escape in a closed-surface residual tower

Date: **2026-08-27**

## Material Passport

- Origin Skill: `ars-codex:academic-research-suite`
- Origin Workflow: Stage-1 theorem development plus experiment-agent validation
- Mathematical owner: a closed genus-2 hyperbolic surface, its canonical
  residual cores, and marked primitive homology owners
- Verification status: theorem `PROVED`; 24-row exact-integer audit
  `NUMERICALLY_CERTIFIED / REPRODUCIBLE`

## Frozen continuous-time subtype

Let `Sigma` be any marked closed oriented hyperbolic surface of genus 2 and

```text
Gamma = pi_1(Sigma)
      = <a1,b1,a2,b2 | [a1,b1][a2,b2]=1>.
```

The dynamical system is the unit-speed geodesic flow on each finite cover,
with the same hyperbolic-arclength clock.  This control is cocompact and has no
cusps.  No arithmetic lattice, rational-prime table, or zero table is used.

For `n>=1`, define

```text
R_n = intersection of all normal N triangleleft Gamma with [Gamma:N] <= n,
H_n = ker(Gamma -> H_1(Sigma; Z/n!Z)),
Gamma_n = R_n intersection H_n.
```

## Theorem 1 — the tower is normal, finite-index, nested, and residual

The group `Gamma` is finitely generated and residually finite.  One route to
the latter fact is that a cocompact Fuchsian group is finitely generated and
linear, so Mal'cev's theorem applies.  A finitely generated group has only
finitely many subgroups of each bounded index.  Therefore `R_n` is a
finite-index characteristic subgroup.  The cores descend with `n` and their
intersection is trivial: every nonidentity element is excluded by some
finite-index normal subgroup, which appears in the defining family for all
sufficiently large `n`.

Each `H_n` is normal and finite-index.  Because `n!` divides `(n+1)!`,
`H_(n+1)` is contained in `H_n`.  Consequently the `Gamma_n` form a descending
normal finite-index tower, and

```text
intersection_n Gamma_n is contained in intersection_n R_n = {e}.
```

Every finite cover `Sigma_n=Gamma_n backslash H` is again closed.  Thus this
is a genuine cocompact control for the noncompact principal-congruence tower
used in Rounds 1--4.

## Theorem 2 — an explicit factorial lower bound

Let `g in Gamma` have homology vector

```text
v(g) in H_1(Sigma;Z) = Z^4,
```

and let `d` be the gcd of its four coordinates.  The additive order of `v(g)`
modulo `m` is

```text
m / gcd(m,d).
```

Indeed, its coordinate orders are `m/gcd(m,v_i)`, and their least common
multiple is the displayed quantity.  Since `Gamma_n` is contained in `H_n`,
there is a quotient map

```text
Gamma/Gamma_n -> Gamma/H_n.
```

It follows that the order `o_n(g)` of `g Gamma_n` is a multiple of the order
of its homology image.  Hence

```text
o_n(g) >= n! / gcd(n!,d).
```

In particular, if `v(g)` is primitive (`d=1`), then

```text
n! divides o_n(g),  so o_n(g) >= n! -> infinity.
```

This is a quantitative strengthening of the general residual-tower escape
lemma from Round 4.  It gives a predeclared lower bound without enumerating
`R_n` or computing the full finite quotient `Gamma/Gamma_n`.

## Corollary — primitive geodesics have factorially escaping minimal periods

If the homology vector of `g` is primitive, `g` cannot be a proper group
power: an identity `g=h^k`, `k>=2`, would make every coordinate of `v(g)`
divisible by `k`.  Thus the conjugacy class of `g` is primitive.

For a torsion-free cocompact Fuchsian group, the stabilizer of a hyperbolic
axis is infinite cyclic.  Therefore the lift of the primitive closed geodesic
owned by `g` to the normal cover `Sigma_n` has exact minimal period

```text
T_n(g) = o_n(g) ell(g),
```

where `ell(g)` is its base geodesic length.  The homology quotient proves

```text
T_n(g) >= n! ell(g) -> infinity.
```

The word “minimal” is justified here by the primitive-homology certificate and
cyclic axis stabilizer.  This differs from Round 4, where the frozen modular
matrices lacked a full conjugacy-primitivity proof and only whole-`g`-loop
closing times were claimed.

## Frozen owner ledger

The executable freezes three words:

| Owner | Word | Homology vector | Content |
|---|---|---:|---:|
| `G2-H1-A` | `a1` | `(1,0,0,0)` | 1 |
| `G2-H1-AB` | `a1*b1` | `(1,1,0,0)` | 1 |
| `G2-H1-ACD` | `a1*a2*b2` | `(1,0,1,1)` | 1 |

At levels 1 through 8 the predeclared moduli and certified lower bounds are

```text
1, 2, 6, 24, 120, 720, 5040, 40320.
```

All 24 rows replay the exact homology order and preserve the distinction
between that bound and the unenumerated full quotient order.  Ten tests and
two byte-identical builds enforce this boundary.

## Scientific consequence

The same period-erasure mechanism survives after all three special features
of the original example are removed:

1. the surface is closed rather than cusped;
2. the tower is not a principal-congruence tower; and
3. no arithmetic lattice or prime target defines the owners.

Therefore `[PROVED]` residual-tower inverse-limit aperiodicity and fixed-owner
period escape are not intrinsically cusp, congruence, or arithmetic effects.
The construction works for every marked closed genus-2 hyperbolic metric, so
in particular it may be instantiated on a non-arithmetic uniformization; no
arithmetic classification of one specially selected metric is being assumed.
This is a useful target-free control, but it further narrows any proposed
arithmetic novelty claim for Paper 27.  The defensible paper contribution is a
compact-versus-noncompact comparative owner audit with explicit quantitative
controls, not a new general aperiodicity theorem.

## Source and proof boundary

- Nica, *Linear groups—Malcev's theorem and Selberg's lemma*,
  https://arxiv.org/abs/1306.2385, is used for the standard theorem that
  finitely generated linear groups are residually finite.
- The tower construction, homology-order bound, primitive-owner argument, and
  application to geodesic periods are proved above.
- The executable certifies only exact integer homology orders and serialization.
  It does not machine-prove Mal'cev's theorem, enumerate `R_n`, or compute
  `o_n(g)`.

## Route correspondence

```text
ARS_STAGE=1_RESEARCH
PROPOSAL_STAGE=1
ROUTE_A_SCOPE=A0-A1
COCOMPACT_CONTROL_THEOREM=PROVED
FINITE_INTEGER_LEDGER=NUMERICALLY_CERTIFIED
LOCAL_A1_PROGRESS_TAG=PROVED_A1_OBSTRUCTION
FORMAL_A0_A4_TUPLE=UNASSIGNED
A2_A4=NOT_EVALUATED
ROUTE_B_EVALUATION=NOT_RUN
ROUTE_B_INVOCATION_ALLOWED=false
GATES_A_E=NOT_REACHED
```

The control supplies no rational-prime owner, zeta determinant, or Route-B
input.  It cannot inherit Route credit from the modular specialization.
