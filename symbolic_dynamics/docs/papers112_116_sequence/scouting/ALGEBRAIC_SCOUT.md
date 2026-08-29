# Algebraic scout for the next Route-A five-paper round

**Historical provenance:** this is a Stage-1 scouting record.  Paper-local
consolidated hostile review and final QA are authoritative after repair.

Status: **SCOUTING FREEZE / EXTERNAL HOLD**  
Scope: finite rings, groups, modules, lattices, polynomial spaces, and
linear-operator-induced finite dynamics.  This file assigns **no final paper
number**.  `NO DIRECT HIT LOCATED` means only that a bounded stop-search did
not locate the same update and theorem package; it is not a novelty or
priority claim.

## 1. Read-only historical audit and hard firewall

Before generating candidates I inspected the root paper table, every present
`docs/papers*_sequence/README.md`, all four present Phase-1 system-collision
firewalls, the paper-directory titles, and the paper-local opening action
descriptions where present.  The canonical batch summaries were used when an
old directory has no `README`.  The on-disk history includes gaps in the
numbered directory run and a legacy duplicate `96-*` directory; neither was
changed and neither was treated as a free system slot.

The action-level exclusions relevant to this scout are:

| historical range | occupied action or proof-engine boundary |
|---|---|
| P1--P91 | arithmetic incidence/Fredholm compilers, ordinary finite-memory shifts, substitutions, graph/relation systems, cellular automata, random reset/stack products, affine and modular functional graphs, and the later algebraic shift families |
| P92--P101 | recurrence avoidance, push--pop and S-adic actions, no-repeat/torsion shifts, finite-subset circle expansion, sumset squaring, unipotent sublattice shear, least-valuation digit erasure, and random cap--floor synchronization |
| P102--P106 | involutive group-algebra norm with scalar squaring blocks, double adjugation on all matrices, random monomial products, permutation cycle pruning, and an antitone MIS polarity |
| P107--P111 | annihilator--power ideal reflection, capped Fibonacci absorption, nilpotent image on the full subspace lattice, cyclic shift--join closure on partitions, and a positive Heisenberg word-area cocycle |
| prior algebra scout reserves/kills | matrix Möbius, Drazin inverse, Newton--Schulz, nilpotent squaring, translation on irreducibles, Euclidean remainder, Hurwitz pairs, subspace-product squaring, centralizer polarity, and meet/join lattice sorting |

Consequently this scout kills or reserves a candidate as soon as its engine is
merely a power map, adjugate/cofactor map, annihilator or colon operation,
nilpotent-image action, sum/product squaring closure, generic affine/linear
functional graph, polarity triple-collapse, ordinary cyclic-sieving action,
or a standard random-rank process.  A finite cycle census by itself cannot
clear the firewall.

## 2. Ranked candidate pool

| rank | concrete phase and update | first exact signal | owner/internal risk and immediate decision |
|---:|---|---|---|
| 1 | bounded monic polynomials over `F_q`, `D(f)=gcd(f,f')` | an irreducible multiplicity `e=pa+r` evolves as `e -> e-1` until it reaches `pa`; universal depth `p-1` and a rational full-depth generating function | **GO-1 / HOLD**; square-free decomposition owns the ingredients, but no direct source for the same iterated self-map and temporal/fibre package was located |
| 2 | functions `2^[n] -> F_q`, Boolean zeta transform `(Zf)(S)=sum_{T subset S}f(T)` | `(Z^m)_{S,T}=m^{|S\T|}` and `Z^p=I`; fixed dimension has a sharp first modular excess at `n=2p-1` | **CONDITIONAL GO-2 / HOLD**; modular tensor-product owners are close and the ordinary-linear-map firewall is live; retain only for the modular-anomaly theorem, never for a generic cycle census |
| 3 | bounded monic polynomials, `E(f)=gcd(f(x),f(x+1))` | `E^t(f)=gcd(f(x),...,f(x+t))`; stabilization after `p-1` steps to `F_q[x^p-x]` is sharp | **RESERVE / HOLD**; mathematically strong but collides within this pool with rank 1's polynomial/GCD phase and with the owned translation action on irreducibles |
| 4 | subspaces of a symplectic `F_q^(2m)`, `R(U)=U intersect U^perp` | `R^2=R`; every `(dim U,dim R(U))` cell has an orbit--stabilizer product formula | **KILL DIRECT OWNER**; prescribed code-hull dimensions and polar-space subspace orbits are already counted directly |
| 5 | monic degree-`n` polynomials with nonzero constant, normalized reciprocal `f -> f(0)^(-1)x^n f(1/x)` | an involution; fixed points have `f(0)^2=1` and paired coefficients, giving a closed 1/2-cycle census | **KILL DIRECT OWNER / SHALLOW**; self-reciprocal-polynomial enumeration is a mature direct literature and the residual dynamics is only an involution wrapper |
| 6 | `GL_d(F_q)`, `A -> A^(-T)` | an involution with fixed set the appropriate finite orthogonal group | **KILL DIRECT/INTERNAL**; the inverse-transpose extension of `GL` is directly studied and this repeats the involution/fixed-subgroup skeleton near P102/P106 |
| 7 | subgroup lattice of a finite `p`-group, `H -> N_G(H)` | every proper `H` strictly grows; `G` is the unique periodic point and depth is at most `log_p [G:H]` | **KILL DIRECT OWNER**; this is literally the normalizer-tower problem (including maximal towers/soft subgroups) |
| 8 | random subspace growth, `U_{t+1}=U_t+<v_t>` for uniform `v_t` | at rank `r`, hold with probability `q^(r-d)` and otherwise rise by one; absorption is a sum of independent geometric waits | **KILL DIRECT/INTERNAL**; equivalent to the sequential rank process of a uniform random matrix and too near random absorption plus P109's phase |
| 9 | `Gr_r(F_(q^m)^d)`, coefficientwise `q`-Frobenius | `F^m=id` and `Fix(F^k)=[d choose r]_(q^gcd(m,k))` by Galois descent | **KILL INTERNAL/DIRECT INGREDIENTS**; this is a coordinate power map and an owned finite-Grassmannian/Galois-descent action |
| 10 | bounded monic polynomials, `S(f)=f/gcd(f,f')` | `S^2=S`; fixed states are square-free polynomials | **KILL SIBLING/DIRECT**; it is the standard square-free quotient and a one-step shadow of rank 1 |
| 11 | all `d x d` matrices, `A -> A+A^T` | `T^2=2T`; characteristic two gives depth two, while odd characteristic gives scalar cycles on symmetric matrices | **KILL INTERNAL**; an ordinary linear functional graph with no residual engine beyond the historical hard exclusion |
| 12 | noncrossing partitions, Kreweras complement | `K^2` is rotation and all orbit lengths divide `2n` | **KILL DIRECT OWNER**; exact Kreweras orbit enumeration and cyclic sieving are already explicit |
| 13 | subgroup lattice of a finite group, `H -> Core_G(H)=intersection_g gHg^(-1)` | an idempotent retraction whose fixed states are the normal subgroups | **KILL SHALLOW/OWNER**; normal core is standard and the dynamical layer adds only one transient step |

Only ranks 1 and 2 are recommended below.  Rank 2 is conditional: discovery
of a direct specialization of the modular tensor-product literature, or a
decision that the system remains an ordinary linear functional graph after
owner subtraction, changes it immediately to `STOP_DUPLICATE/RESERVE`.

## 3. Strong candidate A: differential-core dynamics

### 3.1 System and exact temporal conjugacy

Let `q=p^a`, let `X_n(q)` be all monic polynomials in `F_q[x]` of degree at
most `n` (including `1`), and define

```text
D(f)=gcd(f,f'), normalized to be monic.
```

For `f=product_P P^(e_P)` over monic irreducibles and
`e_P=p a_P+r_P`, `0<=r_P<p`, unique factorization and separability of
irreducibles over the perfect field give

```text
e_P(D(f)) = e_P-1,  if r_P != 0,
             e_P,   if r_P = 0,

e_P(D^t(f)) = e_P-min(t,r_P),
tau(f) = max_P r_P,
D^(p-1)(f) = product_P P^(p floor(e_P/p)).
```

Thus every orbit reaches a fixed point in at most `p-1` steps; the bound on
the exact-degree-`n` layer is sharply `min(n,p-1)`.  The fixed polynomials are
exactly the `p`th powers.  This is multiplicity erosion by a derivation, not a
polynomial power map and not an image action on subspaces.

### 3.2 Full depth law, fibres, and asymptotic anomaly

Let `C_t(n)` be the number of monic exact-degree-`n` inputs with
`tau(f)<=t`, where `0<=t<=p-1`.  The irreducible-factor Euler product collapses
to the rational function

```text
sum_(n>=0) C_t(n) u^n
  = product_P (1-u^((t+1)deg P))
              / ((1-u^(deg P))(1-u^(p deg P)))
  = (1-q u^(t+1))/((1-q u)(1-q u^p)).
```

Equivalently, with `A(s)=0` for `s<0` and

```text
A(s)=sum_(b=0)^floor(s/p) q^(s-(p-1)b),
C_t(n)=A(n)-q A(n-t-1).
```

On the bounded phase,

```text
|X_n(q)| = sum_(d=0)^n q^d,
F_n(q,p) = #Fix(D) = sum_(j=0)^floor(n/p) q^j,
zeta_D(z) = (1-z)^(-F_n(q,p)).
```

If the terminal point is `g^p`, then its exact-degree-`d` fibre under
`D^(p-1)` has size `Q_(d-p deg g)`, where invalid indices give zero and

```text
sum_(k>=0) Q_k u^k = (1-q u^p)/(1-q u),
Q_k = q^k                         (0<=k<p),
      q^k-q^(k-p+1)               (k>=p).
```

For uniform monic exact-degree `n` inputs and fixed `p,q`, the rational CDF
also gives the nondegenerate limiting law

```text
lim P(tau<=t) = (1-q^(-t))/(1-q^(1-p)),
lim P(tau=t)  = (q-1)q^(-t)/(1-q^(1-p)),  1<=t<=p-1.
```

The support recovers `p`; for `p>=3`, adjacent positive limiting masses have
ratio `1/q`.  The degenerate `p=2` boundary is isolated and recovers `q` from
the exact degree-one/fibre census instead.  This supplies a temporal
parameter-recovery clause rather than only a fixed-point count.

### 3.3 Owner subtraction and kill condition

The operation `gcd(f,f')`, multiplicity peeling, and square-free
decomposition are zero-credit background.  See D. Y. Y. Yun,
[On square-free decomposition algorithms](https://doi.org/10.1145/800205.806320),
and the finite-characteristic discussion in the official MIT
[Finite Field Arithmetic notes](https://ocw.mit.edu/courses/18-783-elliptic-curves-spring-2021/b6d0aef71278ad8c1d8b5144c4138cb7_MIT18_783S21_notes3.pdf).
Exact-phrase and conjugate-rule searches did not locate the same iterated
self-map together with its depth CDF, uniform terminal fibres, limiting law,
and zeta.  That bounded result is `NO DIRECT HIT LOCATED`, not clearance.

**Kill immediately** if a square-free-factorization source already states
this repeated self-map and the same temporal/fibre package, or if drafting
shows that after the classical multiplicity lemma is subtracted there is no
independent theorem beyond a one-page reformulation.

## 4. Conditional candidate B: Boolean zeta-transform dynamics

### 4.1 Exact iterate and orbit types

Let `q=p^a`, `V_n(q)=F_q^(2^n)` be functions on the Boolean lattice, and

```text
(Z_n f)(S)=sum_(T subseteq S) f(T).
```

Counting intermediate subsets gives, over the integers and hence over
`F_q`,

```text
(Z_n^m)_(S,T) = m^(|S\T|) if T subseteq S, and 0 otherwise.
```

For `n>=1`, `Z_n` therefore has exact order `p`.  Every orbit has length one
or `p`.  If `kappa_(n,p)=dim ker(Z_n-I)`, then

```text
Fix(Z_n^m) = q^(2^n)       if p divides m,
             q^kappa       otherwise,

#Per_1 = q^kappa,
#Per_p = (q^(2^n)-q^kappa)/p,
zeta_Z(z)=(1-z)^(-q^kappa)
          (1-z^p)^(-(q^(2^n)-q^kappa)/p).
```

### 4.2 Modular fixed dimension and first anomaly

The matrix is the tensor power `J_2(1)^(tensor n)`, so the Boolean action is
the `C_p`-module `V_2^(tensor n)`.  For odd `p`, let `a_(n,r)` be the
multiplicity of the nonprojective indecomposable `V_r`, `1<=r<p`, and let
`c_n` be the multiplicity of the projective block `V_p`.  Then

```text
a_(1,r)=1_(r=2),  c_1=0,
a_(n+1,r)=a_(n,r-1)+a_(n,r+1),
             with a_(n,0)=a_(n,p)=0,
c_(n+1)=2c_n+a_(n,p-1),
kappa_(n,p)=sum_(r=1)^(p-1) a_(n,r)+c_n.
```

For `p=2`, `kappa_(n,2)=2^(n-1)`.  The first modular departure from the
characteristic-zero block count is sharply

```text
kappa_(n,p) = binom(n,floor(n/2))       for n<=2p-2,
kappa_(2p-1,p) = binom(2p-1,p-1)+1.
```

The path-graph recurrence also yields

```text
kappa_(n,p) = 2^n/p + O((2 cos(pi/p))^n)
```

for fixed odd `p`, and hence `log_q #Fix(Z_n)/2^n -> 1/p`.  This modular
threshold and asymptotic fixed-density law are the only defensible residual
headline; the order-`p` cycle census alone is insufficient.

### 4.3 Owner subtraction and kill condition

General tensor products of unipotent Jordan blocks and their modular Jordan
partitions are directly owned; see Glasby--Praeger--Xia,
[Decomposing modular tensor products](https://arxiv.org/abs/1403.4685), and
their later [Norman involutions paper](https://arxiv.org/abs/1711.06860).
Callan's [Jordan and Smith forms of Pascal-related matrices](https://arxiv.org/abs/math/0209356)
is an additional transform-matrix neighbor.  The bounded search did not find
a paper specializing these ingredients to the Boolean zeta action and
stating the fixed-dimension threshold plus complete dynamical package.

**Kill immediately** if backward/forward citation chaining finds a direct
`V_2^(tensor n)` specialization with the displayed `kappa` recurrence and
threshold, or if the sequence chair enforces the generic-linear-functional-
graph exclusion after owner subtraction.  This candidate is therefore a
conditional second recommendation, not a locked selection.

## 5. Strong reserves and successful dead road

### 5.1 Translation--GCD erosion -- RESERVE

For `E(f)=gcd(f(x),f(x+1))` in characteristic `p`, induction gives

```text
E^t(f)=gcd(f(x),f(x+1),...,f(x+t)).
```

Since translation by one has order `p`, `E^(p-1)` is a retraction to the
invariant ring `F_q[x^p-x]`; the sharp exact-degree depth is
`min(n,p-1)`, and the bounded fixed count is again
`sum_(j<=n/p)q^j`.  The exact profiles differ from differential-core
dynamics (for example over `F_3` in degree five they are `180/63` versus
`177/66` at depths one/two), so the maps are not conjugate.  Nevertheless,
co-selecting two bounded-polynomial GCD erosions would violate breadth.
Translation actions on irreducibles sit inside the direct `PGL_2` literature;
see Gow--McGuire,
[Invariant Rational Functions, Linear Fractional Transformations and Irreducible Polynomials](https://arxiv.org/abs/2105.11247).
Keep only as a replacement if candidate A is killed and only after deriving a
closed full-depth census.

### 5.2 Symplectic radical retraction -- KILL DIRECT OWNER

For a symplectic `2m`-space, `R(U)=U intersect U^perp` is idempotent.  Write

```text
I_(m,h) = [m choose h]_q product_(i=0)^(h-1)(q^(m-i)+1),
S_m=|Sp(2m,q)|.
```

If `r-h=2j`, the exact joint census is

```text
#{U: dim U=r, dim R(U)=h}
 = I_(m,h) S_(m-h)/(S_j S_(m-h-j)),
```

and it is zero otherwise.  The spike verifies every cell, idempotence, and
uniform fibres over each isotropic dimension.  This is mathematically clean
but owner-dominated: Sendrier's
[On the Dimension of the Hull](https://doi.org/10.1137/S0895480195294027)
already counts codes with prescribed hull dimension, while Wan's
[Anzahl theorems in finite singular symplectic, unitary and orthogonal geometries](https://doi.org/10.1016/0012-365X(93)90013-J)
counts the relevant polar-space subspace orbits.  The remaining dynamics is
only an idempotent wrapper, so this candidate is killed despite a complete
formula.

## 6. Exact proof spikes

All four scripts use only the Python standard library and exact integer/prime-
field arithmetic.  Formula routines are compared against literal map
iteration; no paper implementation, CAS, factorization package, or numerical
tolerance is imported.

| script | lanes and adversarial checks | result |
|---|---|---:|
| `code/algebraic_differential_core.py` | prime fields `p=2,3,5,7`, degrees through `8,7,6,5`; literal derivative/GCD iteration, every depth CDF cell, sharp depth, all fixed states, and every degree-resolved terminal fibre | **224,090 PASS** |
| `code/algebraic_boolean_zeta.py` | direct ranks through `n=7`; literal iterate-entry identities, exhaustive small functional graphs, module recurrence through `n=12`, and sharp first-anomaly probes for primes through `19` | **76,811 PASS** |
| `code/algebraic_symplectic_radical.py` | every subspace for `(q,2m)=(2,2/4/6),(3,2/4),(5,2/4)`; all joint rank/radical cells, idempotence, isotropy, and fibres | **23,321 PASS** |
| `code/algebraic_translation_gcd.py` | prime fields `2,3,5,7`, degrees through `8,7,6,5`; every sliding-window iterate, sharp depth, invariant-ring fixed set, and complete depth profiles | **382,545 PASS** |
| **total** | four independent exact spikes | **706,767 PASS** |

The successful symplectic computation is deliberately retained as a dead-road
certificate: exactness does not override a direct owner.  Likewise the
translation spike records a real reserve, not permission to co-select two
nearby polynomial systems.

## 7. Recommended theorem contracts

### Contract A -- differential core (recommended first)

Freeze exactly five clauses:

1. irreducible-multiplicity conjugacy, exact iterates, fixed projection, and
   sharp depth `min(n,p-1)` with all boundary cases;
2. the complete exact-degree depth CDF via
   `(1-q u^(t+1))/((1-q u)(1-q u^p))` and explicit coefficient form;
3. degree-resolved fibres of `D^(p-1)` over every fixed `g^p`, including the
   `p`-power-free residual count;
4. complete periodic sequence and rational zeta on the bounded phase;
5. the truncated-geometric limiting depth law and recovery of `(p,q)` from
   its support and adjacent-mass ratio, with the `p=2` boundary isolated.

Two materially different routes:

1. a proof route through UFD valuations, perfect-field separability, Euler
   products, and singularity extraction of the rational generating function;
2. a factorization-free control route using literal formal derivatives and
   Euclidean polynomial GCDs, exhaustive bounded phases, direct terminal
   fibre hashing, and independent coefficient recurrences.

Subtract all credit for square-free factorization itself.  External status
remains **HOLD**.

### Contract B -- Boolean zeta (conditional second)

Freeze exactly five clauses only if the owner gate survives:

1. the entrywise iterate identity and exact order `p`;
2. the complete indecomposable-block/fixed-dimension recurrence, including
   characteristic two;
3. the sharp characteristic-zero window through `2p-2` and the first `+1`
   modular anomaly at `2p-1`;
4. all fixed counts, 1/`p`-cycle counts, fixed sequence, and dynamical zeta;
5. `kappa_(n,p)=2^n/p+O((2cos(pi/p))^n)` and the limiting logarithmic fixed
   density `1/p`.

Two materially different routes:

1. count intermediate Boolean subsets to prove the iterate formula, then use
   modular `C_p` representation theory/Green-ring tensor rules for
   `V_2^(tensor n)` and a path-graph spectral estimate;
2. construct the literal zeta matrix, compute exact modular ranks independently,
   exhaust all vectors in small phases, and compare the complete functional
   graph against the recurrence without using Jordan-form software.

Subtract all general modular Jordan-product theory.  If that subtraction
leaves only the standard finite-linear-map census, downgrade to `RESERVE`.
External status remains **HOLD**.

## 8. Bounded owner-search boundary

The stop-search used exact update strings, factor/multiplicity conjugates,
transform-matrix/Jordan formulations, DOI metadata, arXiv primary records,
and the repository kill ledgers.  It found immediate reasons to kill the
symplectic hull, inverse-transpose, normalizer-tower, random-rank, reciprocal,
and Kreweras candidates.  In particular, exact Kreweras orbits are already a
direct topic; see Heitsch,
[Counting orbits under Kreweras complementation](https://arxiv.org/abs/2303.12240),
and the inverse-transpose extension of `GL` is directly studied in
[Conjugacy Class Properties of the Extension of GL(n,q) Generated by the Inverse Transpose Involution](https://arxiv.org/abs/math/0304047).
The random-spanning proposal is subsumed by finite-field random-rank work,
including Fulman--Goldstein,
[Stein's method and the rank distribution of random matrices over finite fields](https://arxiv.org/abs/1211.0504).

No bounded search proves absence.  Before any manuscript drafting, candidate
A still needs backward/forward chaining from finite-field square-free
factorization sources, and candidate B needs an exact specialization search
inside the cyclic-`p` Green-ring literature.  Public release, submission,
specialist contact, venue choice, authorship, and all novelty/priority
language remain **HOLD**.
