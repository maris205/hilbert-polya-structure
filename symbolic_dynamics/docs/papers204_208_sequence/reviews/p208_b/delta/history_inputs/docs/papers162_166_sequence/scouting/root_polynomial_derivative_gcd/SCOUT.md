# Root focused scout — derivative--GCD dynamics (`DGD`)

**Date:** 2026-09-03 UTC  
**Route:** A, finite rank-changing algebraic dynamics  
**Carrier:** monic polynomials of degree at most `N` over `F_p`  
**Author-side decision:** `KILL_DIRECT_OWNER_AND_INTERNAL_PDG`  
**External state:** `HOLD_EXTERNAL`

## Outcome first

Let `p` be prime and let `M_(p,N)` consist of every monic polynomial in
`F_p[x]` of degree at most `N`, including `1`.  Define

```text
D(f)=monic gcd(f,f').                                  (1)
```

The operation is the classical first step of square-free factorization and
receives no credit by itself.  Iterating it on the entire capped phase space,
however, exposes a characteristic-`p` residue dynamics on every irreducible
multiplicity.  That gives a pointwise/sharp clock, exact depth and image
censuses, and a target-resolved Euler-product fibre polynomial at every time.

The characteristic-residue formulas are a correct strengthening of the old
`char>N` calculation, but the literal system was already audited internally
as `PDG` and again as `SFE`.  Both audits correctly rejected it because
Yun/Musser own the derivative--GCD multiplicity engine.  The extra residue
branches and capped Euler products do not create a new independent mechanism.
This lane is therefore frozen as negative evidence, not sent to a paper gate.

## 1. Complete iterate and point clock

Write the unique factorization

```text
f=product_P P^m_P.
```

Every irreducible over a finite field is separable.  The product rule gives

```text
v_P(D(f))=m_P-1[p does not divide m_P].                (2)
```

If `p|m_P`, all derivative summands are divisible by `P^m_P`; if not, the
summand differentiating `P^m_P` has exact valuation `m_P-1` and cannot cancel
modulo `P`.  Therefore, for every `t>=0`,

```text
D^t(f)=product_P P^(m_P-min(t,m_P mod p)).             (3)
```

The point depth is

```text
h(f)=max_P (m_P mod p),                                (4)
```

with empty maximum zero.  Every recurrent state is fixed, and the fixed
states are exactly the `p`th powers.  On the capped carrier,

```text
max_f h(f)=min(p-1,N),                                 (5)
```

attained by a power of any linear irreducible.  The number of fixed states is

```text
1+p+...+p^floor(N/p).                                  (6)
```

The `n=0`, `N<p`, `p=2`, derivative-zero, and constant-polynomial boundaries
are all included in (3)--(6).

## 2. Depth and image atlases

Let `I_p` be the monic irreducibles and put `d_P=deg P`.  If
`s=min(t,p-1)`, the degree generating polynomial for states of depth at most
`t`, truncated after degree `N`, is

```text
[x^<=N] product_(P in I_p)
   (1+x^d_P+...+x^(s d_P))/(1-x^(p d_P)).              (7)
```

Differences in `t` give every exact depth layer.

For a target `g=product P^e_P`, define its minimum time-`t` source degree by

```text
m_t(g)=sum_(e_P=0 mod p) e_P d_P
       +sum_(e_P not=0 mod p) (e_P+t)d_P.              (8)
```

Then `g` belongs to the time-`t` image exactly when

```text
e_P mod p is in {0,1,...,p-t-1} for every P, and
m_t(g)<=N,                                             (9)
```

for `t<p`; at `t>=p-1`, only residue zero remains and (8) reduces to
`deg g`.  The cap term in (9) is essential: a formally admissible target can
require a source above degree `N`.

## 3. Every-time, every-target Euler fibres

Fix `g in M_(p,N)` and `t>=0`, and again put `s=min(t,p-1)`.  Mark source
degree excess over `g` by `z`.  For each irreducible `P`, define a local
factor

```text
L_(P,g,t)(z)=
  1+sum_(r=1)^s z^(r d_P),              P does not divide g;
  sum_(r=0)^s z^(r d_P),                e_P=0 mod p;
  z^(t d_P),                            1<=e_P mod p<=p-t-1;
  0,                                    otherwise.     (10)
```

The third line occurs only for `t<p`.  Then the full target fibre is

```text
sum_(D^t(f)=g, deg f<=N) z^(deg f-deg g)
 = [z^<=N-deg g] product_(P in I_p) L_(P,g,t)(z).      (11)
```

Only irreducibles of degree at most `N` affect the truncation.  Formula (11)
is target-dependent through both the support and residue vector of `g`; it
also gives (9) by coefficient positivity.  At `g=1`, it counts all
polynomials whose positive exponents are at most `s` and hence disappear by
time `t`.  At `t=0`, (11) is the singleton fibre.

The proof is local and bijective: for a target exponent divisible by `p`, a
source may add any residue `0,...,s`; for an allowed nonzero residue, the only
source exponent is `e_P+t`; and a new factor can disappear only with exponent
`1,...,s`.  Multiplying independent irreducible choices and enforcing the
global cap proves (11).

## 4. Functional graph, zeta, and recovery

Every nonfixed update strictly lowers degree, so the graph is a disjoint
union of rooted DAGs directed into the fixed `p`th powers.  Equations
(7) and (11) give, respectively, all depth layers and every target's incoming
time layers.  With

```text
F_(p,N)=1+p+...+p^floor(N/p),
```

the Artin--Mazur zeta function is

```text
zeta_D(u)=(1-u)^(-F_(p,N)).                            (12)
```

When `N>=p-1`, the sharp clock recovers the characteristic as
`p=1+max h`.  The degree-one phase stratum has cardinality `p`, providing an
independent recovery coordinate and covering `N<p-1`.  No ungraded phase-size
recovery is claimed: repunit cardinalities can collide.

## 5. Owner and internal subtraction

Zero-credit inputs include:

- formal derivatives, polynomial gcds, separability over finite fields, and
  unique factorization;
- detecting repeated factors with `gcd(f,f')`;
- Musser/Yun square-free decomposition, all multiplicity-peeling algorithms,
  and the derivative-zero `p`th-root branch;
- Euler products over irreducible polynomials and the standard count of
  irreducibles by degree;
- generic finite-DAG, zeta, and Möbius bookkeeping.

The candidate may claim only the literal capped self-map and the conjunction
of (3)--(12).  It does not claim a new factorization algorithm.

Closest internal papers do not transfer the theorem package, but an earlier
scout does transfer the literal map:

- P100 is a nilradical polynomial map over `Z/p^a Z`; P115 is a Cartier
  coefficient operator; P157 iterates a scalar idempotent-lifting cubic over
  `Z/2^n Z`.
- P107 iterates annihilator powers of ideals, while DGD acts on actual monic
  polynomials and has characteristic-residue multiplicity fibres.
- Earlier finite-difference/Hasse-derivative scouts are linear coefficient
  operators and were killed as such; (1) is a nonlinear gcd divisor map.
- More decisively, P152--P156 scouting already used the same literal map under
  handle `PDG` for `char>N`, with its multiplicity clock and target Euler
  product, and `algebraic_replacement2` killed it again as `SFE`.  The present
  `char<=N` residue extension cannot be presented as a new dynamical system.

## 6. Exact evidence

Run

```text
python3 docs/papers162_166_sequence/scouting/root_polynomial_derivative_gcd/verify_scout.py
```

The verifier implements polynomial arithmetic, formal derivative, Euclidean
gcd, irreducibility testing, and factorization independently over the prime
fields.  It exhausts `(p,N)=(2,7),(3,6),(5,5),(7,4)`, checks literal iterates
against (3), every point clock, strict degree loss, fixed and sharp counts,
the Euler depth census, the capped image criterion, and every coefficient of
(11) for every target and all relevant times.  The frozen run makes `148,477`
exact assertions and ends in `STATUS PASS`.

This is bounded falsification pressure, not a proof or priority certificate.

## Author-side gate

```text
DGD  KILL_DIRECT_OWNER_AND_INTERNAL_PDG
HOLD_EXTERNAL
```
