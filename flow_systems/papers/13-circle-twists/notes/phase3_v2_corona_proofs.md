# Paper 13 Phase-3 v2 cardinality, diagonal, and corona proofs

Status: **PROOF CANDIDATE COMPLETE / INDEPENDENT EXACT-BYTE REVIEW REQUIRED**  
Date: **2026-08-15 (Asia/Shanghai)**  
Proof scope: the bounded P13-8A--C delta authorized below  
Standalone disposition: **not granted; `NOTE_OR_MERGE` remains binding**  
`route_b_invocation_allowed: false`

## 1. Authority, exact inputs, and proof boundary

The sole authorizing gate is
`notes/phase3_v2_design_gate.md`, SHA-256
`0094462b1e06cde0cf1fcc3536c608dcd96ef1e9eb0d85a0714df1666b799706`.
It was rehashed and read in full before this file was created.  This proof
uses the following exact v2 tuple.

| artifact | SHA-256 | proof use |
|---|---|---|
| `notes/phase3_standalone_amendment_v2.md` | `99c796bffe24f262d8ac8458b21fd253451bca51bac4b283660dab319992ed82` | base P13-8A--C statements and firewalls |
| `notes/phase3_standalone_amendment_v2_ownership_addendum.md` | `d9523d1692d60fbdff7bbf5ab6c00d44bdcd26f02dc5cdeeba8c7ba43d78a39f` | Paper-2 subtraction, bare-set typing, and contribution ceiling |
| `notes/phase3_v2_methodology_review.md` | `96a5067015847ff88155b91658ae94e9ef5a6355ae176c1945644b3e729f4f74` | final methodology closure, C0/M0/m0 |
| `notes/phase3_v2_devils_advocate.md` | `1c6bbb0bc7d3fc366de4d8a4eb869d4d4708f19647f10d780be095ac9e81f110` | final devil/domain closure, C0/M0/m0 |
| `notes/phase3_v2_source_feasibility.md` | `3ce4e8db7914c0053a31b7e0e08e8f0fe02e0b2db15620f194c1ccae5ffeb320` | final source/ownership closure, C0/M0/m0 |
| `notes/phase3_core_twist_proofs.md` | `62dac0782ba74fea9e8318e0835f7f20eede4cc9963c67471797a006b00decbd` | frozen P13-1--P13-5 signs, gauges, regular representation, and time norms |
| `notes/phase3_support_retention_proofs.md` | `f8a0672026b2efaaf07af20d90a17e870e8d0e2f849af0eb78d6dcb1573fb811` | frozen P13-8 test-support theorem |
| Paper 2 `papers/2-flow-zeta/paper/manuscript.tex` | `72c34a0a30279ed7c070917a2c9242b8e9cb0a37a56779c246fa2cae04097fdc` | inherited Proposition `prop:uncountable` lower bound |
| Paper 2 `papers/2-flow-zeta/notes/proof_audit.md` | `aaab83c32eb9d6c172be192dbb14acc6ed927a972d61c24a90dbfe94ecd0dbae` | accepted lower-bound proof and topology ceiling |

The ownership addendum has precedence on the surfaces it declares.  In
particular, Paper 2 owns the sign-subgroup/procyclic-intersection proof of

```text
|U_p/H_p| >= 2^aleph_0.
```

That proof is not repeated here.  Section 2 proves only the authorized
Paper-13 delta: the elementary upper bound and equality closure, exact
retyping, and direct consequences on the standard/discrete topology owners.
Sections 3--10 prove the component, multiplier, diagonal, corona, gauge, and
fixed-prime statements.  No control, Route, composition, manuscript,
citation, release, Git, or public-synchronization action is performed or
authorized by this record.

## 2. P13-8A: inherited lower bound, exact equality, and topology

Fix a rational prime `p`.  Retain the exact Paper-9 bare-set identification

```text
Q_p^bare ~=_set U_p/H_p,
U_p = product_(ell != p) Z_ell^x,
H_p = p^Zhat subset U_p.
```

Paper 2 Proposition `prop:uncountable` supplies the mandatory inherited
premise

```text
|U_p/H_p| >= 2^aleph_0.                              (2.1)
```

Its proof uses the fully typed sign subgroup, with every unused coordinate
fixed to `1`.  Equation (2.1), including that sign argument and its bare-set
packet transfer, receives no Paper-13 novelty, priority, author-delta,
standalone, or Route credit.

### Proposition 2.1 (elementary continuum upper bound and equality)

For every rational prime `p`,

```text
|U_p| <= 2^aleph_0,
|Q_p^bare| = |U_p/H_p| = 2^aleph_0.                 (2.2)
```

#### Proof

Each `ell`-adic integer is specified by a countable digit string, so

```text
|Z_ell^x| <= |Z_ell| <= aleph_0^aleph_0 = 2^aleph_0.
```

There are countably many rational primes different from `p`.  Cardinal
exponentiation therefore gives

```text
|U_p|
  <= (2^aleph_0)^aleph_0
   = 2^(aleph_0 * aleph_0)
   = 2^aleph_0.                                    (2.3)
```

The quotient map is surjective, hence
`|U_p/H_p| <= |U_p|`.  Combining (2.3) with the inherited Paper-2 lower
bound (2.1) proves the quotient equality.  The Paper-9 bare-set bijection
then gives the equality for `Q_p^bare`.  No continuum hypothesis, Haar
measure, quotient topology, or orbit enumeration occurs. `square`

### Owner retyping

The Paper-9 bare owner `Q_p^bare` is exactly the underlying set of
`Q_p^actual`.  Equation (2.2) is a cardinality statement about that carrier;
it does not alter any topology.  The four records remain distinct:

- `Q_p^actual` is the intrinsic Paper-9 quotient with its indiscrete
  topology.  In particular, its two-element open family is still a
  countable base.
- `Q_p^bare` carries no topology in (2.2).
- `Std(Gamma_p)` is the Paper-12 topological coproduct of compact Hausdorff
  orbit torsors.
- `Q_p^disc` is the discrete component quotient of that standardization.

Thus continuum cardinality is compatible with second countability of the
actual indiscrete quotient.  No standard or discrete topology is transported
to either actual or bare owner.

### Lemma 2.2 (two coproduct facts)

Let `Y=coproduct_(q in Q) Y_q`, where every `Y_q` is nonempty.

1. If `Q` is uncountable, then `Y` is not second countable.
2. Every compact subset of `Y` meets only finitely many components.
   Consequently, if `Q` is uncountable, then `Y` is not `sigma`-compact.

#### Proof

The component sets `Y_q` are pairwise disjoint nonempty opens.  If
`{V_n:n in N}` were a countable base, choose for each `q` the least `n(q)`
such that a nonempty basic open `V_(n(q))` lies in `Y_q`.  Disjointness makes
`q |-> n(q)` injective, contradicting uncountability.

For a compact `K subset Y`, the component opens that meet `K` form an open
cover of `K`.  A finite subcover exists, so `K` meets only finitely many
components.  A countable union of compact subsets consequently meets only
countably many components and cannot cover an uncountable coproduct.
`square`

### Theorem 2.3 (authorized standard-topology consequences)

For every rational prime `p`, each of

```text
Q_p^disc,
Std(Gamma_p),
G_std(Gamma_p)=Std(Gamma_p) semidirect R
```

is neither second countable nor `sigma`-compact.

#### Proof

The discrete space `Q_p^disc` has the continuum-sized family of singleton
opens.  Its compact subsets are finite, so the two conclusions follow
directly.

The standard unit space is

```text
Std(Gamma_p)=coproduct_(q in Q_p^bare) O_q,
O_q ~= R/(log p)Z,
```

and every `O_q` is nonempty and open.  Proposition 2.1 makes the index set
uncountable, so Lemma 2.2 applies.  The standard arrow space is likewise the
coproduct of the nonempty open component arrow spaces `O_q x R`; the same
lemma applies again. `square`

These failures are topology facts on the stated standard/discrete owners.
They imply no nonexistence or nonconstructibility statement about any
analytic framework.

## 3. Generic component records and the time test map

Let `X` be a nonempty globally indiscrete right-`R` set whose stabilizer at
every point is the same cocompact lattice `H=LZ`, `L>0`.  Write

```text
Q^bare := the underlying set of X/R, with no topology,
Std(X) := coproduct_(q in Q^bare) O_q,
O_q    := the intrinsic standard orbit torsor.
```

Each `O_q` is a nonempty compact Hausdorff right-`R` torsor with stabilizer
`H`.  No point of `O_q` is selected.  Fix a continuous normalized multiplier
`sigma:R^2->T` and retain the P13-4 time test algebra
`A_sigma=C_c(R)`.

For one component define

```text
C_c(O_q semidirect R,sigma)
```

to be `C_c(O_q x R)` with Lebesgue range-fibre measure and the frozen
range-first formulas

```text
(F *_sigma G)(x,t)
  = integral_R F(x,u)G(x.u,t-u)sigma(u,t-u)du,      (3.1)

F^{*sigma}(x,t)
  = overline{sigma(t,-t)} overline{F(x.t,-t)}.      (3.2)
```

For these range-first coordinates, use the exact `I`-norm

```text
||F||_I=max{
  sup_(x in O_q) integral_R |F(x,t)|dt,
  sup_(x in O_q) integral_R |F(x.t,-t)|dt
}.                                                   (3.3)
```

The maximal component record `B_(q,sigma)^max` is the universal completion
over the `I`-norm-decreasing test representations.  The reduced component
record `B_(q,sigma)^r` is the completion for the supremum of the unit-regular
representations below.  These two records remain separately typed.

### Lemma 3.1 (component gauge map and existence of the records)

If `sigma overline(tau)=delta alpha` for a continuous normalized
`alpha:R->T`, define

```text
(U_(alpha,q)F)(x,t)=alpha(t)F(x,t).                 (3.4)
```

Then (3.4) is a support- and `I`-norm-preserving star isomorphism from the
`sigma` component test algebra to the `tau` component test algebra.  It
extends isometrically to both maximal and reduced component records.

#### Proof

At `(u,t-u)` the gauge identity reads

```text
alpha(t)sigma(u,t-u)
  =alpha(u)alpha(t-u)tau(u,t-u).                   (3.5)
```

Substitution in (3.1) proves product preservation.  The inverse-face
calculation from the frozen P13-4 proof gives

```text
alpha(t)overline{sigma(t,-t)}
  =overline{tau(t,-t)}overline{alpha(-t)},          (3.6)
```

which proves star preservation.  Circle multiplication leaves supports and
absolute values unchanged, so it preserves the component `I`-norm.  Its
inverse is `U_(overline(alpha),q)`.  Taking `tau=1`, with the continuous
trivializer supplied by frozen P13-3, transports (3.1)--(3.2) bijectively to
the audited ordinary compact-orbit test algebra.  This proves closure,
associativity, both star laws, finiteness of the universal norm, and existence
of the two completions without choosing an orbit origin.

For the reduced statement, fix `x in O_q`.  The source fibre at `x` is
parameterized without a torsor origin by

```text
t |-> (x.(-t),t).
```

On `L^2(R)` the corresponding unit-regular representation is

```text
[Reg_(q,x,sigma)(F)xi](t)
  = integral_R F(x.(-t),u)sigma(u,t-u)xi(t-u)du.    (3.7)
```

In kernel coordinates `s=t-u`, its absolute kernel is
`|F(x.(-t),t-s)|`.  The row integrals are bounded by the first term of
(3.3).  With `y=x.(-s)` and the change of variable `v=s-t`, the column
integrals are bounded by the second term of (3.3).  Schur's estimate therefore
gives

```text
||Reg_(q,x,sigma)(F)|| <= ||F||_I.
```

Thus every unit-regular representation is among the representations counted
by the maximal norm; in particular, the maximal component norm dominates the
reduced component norm.

Equations (3.5) and (3.7) give

```text
Reg_(q,x,tau)(U_(alpha,q)F)
  =M_alpha Reg_(q,x,sigma)(F) M_overline(alpha).   (3.8)
```

Thus every unit-regular norm is preserved.  The universal representations
are bijected by precomposition with (3.4), so the maximal norm is preserved
as well. `square`

No equality of the entire maximal and reduced component records is used or
claimed.

### Definition 3.2 (origin-free time map)

For `f in C_c(R)`, set

```text
d_(q,sigma)(f)(x,t)=f(t).                           (3.9)
```

The support is `O_q x supp(f)`, which is compact because `O_q` is compact.
Hence (3.9) belongs to the component test algebra.

### Proposition 3.3 (test-level injective star homomorphism)

The map `d_(q,sigma):A_sigma->C_c(O_q semidirect R,sigma)` is an injective
star homomorphism.

#### Proof

Substituting (3.9) into (3.1) gives

```text
[d(f) *_sigma d(g)](x,t)
  =integral_R f(u)g(t-u)sigma(u,t-u)du
  =d(f *_sigma g)(x,t).
```

Substitution into (3.2) gives `d(f)^{*sigma}=d(f^{*sigma})`.  Since `O_q`
is nonempty, `d(f)=0` implies `f(t)=0` for every `t`, so `f=0`. `square`

## 4. Exact maximal/reduced norm chain

### Lemma 4.1 (unit-regular restriction)

For every `x in O_q` and `f in C_c(R)`,

```text
Reg_(q,x,sigma)(d_(q,sigma)(f))=Lambda_sigma(f).   (4.1)
```

Consequently

```text
||d_(q,sigma)(f)||_(B_q^r)
  =||Lambda_sigma(f)||
  =||f||_(C*_r(R,sigma)).                          (4.2)
```

#### Proof

The coefficient in (3.7) becomes
`d(f)(x.(-t),u)=f(u)`.  Formula (3.7) is then exactly the intrinsic frozen
P13-5 formula

```text
[Lambda_sigma(f)xi](t)
  =integral_R f(u)sigma(u,t-u)xi(t-u)du.
```

This holds at every unit, so taking the supremum of the unit-regular norms
proves (4.2). `square`

### Lemma 4.2 (maximal upper bound)

For every `f in C_c(R)`,

```text
||d_(q,sigma)(f)||_(B_q^max)
  <= ||f||_(C*_(max)(R,sigma)).                    (4.3)
```

#### Proof

For the component `I`-norm, both terms in (3.3) reduce on (3.9) to
`||f||_1`; hence

```text
||d_(q,sigma)(f)||_I=||f||_1.                      (4.4)
```

Let `Pi` be any representation counted by the component universal norm.
Then `Pi o d_(q,sigma)` is, by Proposition 3.3 and (4.4), an
`L^1(R,sigma)`-continuous star representation of the time test algebra.
The defining universal property of `C*_(max)(R,sigma)` therefore gives

```text
||Pi(d_(q,sigma)(f))||
  <=||f||_(C*_(max)(R,sigma)).
```

Taking the supremum over `Pi` proves (4.3).  Degenerate restrictions cause
no problem: adjoining a zero summand or passing to the nondegenerate part
does not enlarge their norm. `square`

### Theorem 4.3 (two-sided norm equality and completed embeddings)

For every `q`, `f in C_c(R)`, and `epsilon in {max,r}`,

```text
||d_(q,sigma)(f)||_(B_q^max)
 =||d_(q,sigma)(f)||_(B_q^r)
 =||f||_(C*_(max)(R,sigma))
 =||f||_(C*_r(R,sigma)).                           (4.5)
```

Thus `d_(q,sigma)` extends uniquely to an isometric faithful star
homomorphism

```text
d_(q,sigma)^epsilon:
  C*_(epsilon)(R,sigma) -> B_(q,sigma)^epsilon.    (4.6)
```

Its completed image lies in the component algebra itself.

#### Proof

The component maximal norm dominates the reduced norm.  Lemmas 4.1--4.2
and the frozen P13-5 amenable-time theorem give the closed chain

```text
||f||_(time,max)
 >= ||d_q(f)||_(component,max)
 >= ||d_q(f)||_(component,r)
  = ||Lambda_sigma(f)||
  = ||f||_(time,r)
  = ||f||_(time,max).                              (4.7)
```

Every inequality in (4.7) is therefore equality.  Isometry on the dense
test algebra gives the unique completion map (4.6), and isometry gives
faithfulness.  If `a` is a completion element, choose `f_n in C_c(R)` with
`f_n->a`.  Then `d_q(f_n)` is Cauchy in `B_q^epsilon` and converges there,
so the image is in `B_q^epsilon`, not only in its multiplier algebra.
`square`

The proof used amenability only for the one-object time group after both
component inequalities had been established.

## 5. Arbitrary-index `c0` assembly and its multiplier algebra

For either `epsilon in {max,r}`, abbreviate

```text
C_sigma^epsilon := C*_(epsilon)(R,sigma),
B_q              := B_(q,sigma)^epsilon,
A                 := A_(std,sigma)^epsilon
                   = direct_sum_(q in Q^bare)^c0 B_q.       (5.1)
```

Thus `A` consists of all families `b=(b_q)` such that

```text
sup_q ||b_q|| < infinity,
for every eta>0, {q:||b_q||>=eta} is finite.       (5.2)
```

There is no enumeration of `Q^bare`.

### Theorem 5.1 (direct arbitrary-index multiplier-product identity)

There is a canonical isometric star isomorphism

```text
M(A) ~= product_(q in Q^bare)^bounded M(B_q).       (5.3)
```

Under (5.3), an element of `A` is the same `c0` family, with each `b_q`
viewed as its inner multiplier of `B_q`.

#### Proof

Use the double-centralizer realization of a multiplier.  Write a multiplier
of `A` as a bounded pair `(L,R)` satisfying

```text
L(ab)=L(a)b,
R(ab)=aR(b),
aL(b)=R(a)b.                                      (5.4)
```

Let `I_q` be the closed coordinate ideal consisting of families supported
at `q`.  If `a in I_q`, `r!=q`, and `c in I_r`, then `ac=ca=0`.  Hence

```text
L(a)c=L(ac)=0,
cR(a)=R(ca)=0.                                    (5.5)
```

Apply (5.5) to an approximate identity of `B_r`.  It follows that the
`r`-coordinates of both `L(a)` and `R(a)` vanish.  Thus each coordinate
ideal is preserved, and the restrictions `(L_q,R_q)` define a multiplier
`m_q in M(B_q)` with

```text
||m_q|| <= ||(L,R)||.
```

The resulting family is uniformly bounded.  On a finite-support element,
`L` and `R` act coordinatewise by these restrictions.  Finite-support
families are dense in `A`, so the same coordinate formula holds on all of
`A`.  The map from `M(A)` into the right side of (5.3) is therefore
injective.

Conversely, let `(m_q)` be a uniformly bounded multiplier family, with
`C=sup_q||m_q||`.  Define

```text
[L_m(b)]_q=m_q b_q,
[R_m(b)]_q=b_q m_q.                                (5.6)
```

The estimates

```text
||m_q b_q|| <= C||b_q||,
||b_q m_q|| <= C||b_q||
```

show that both families in (5.6) satisfy the `c0` condition (5.2).
Coordinatewise multiplication verifies (5.4), so (5.6) defines a multiplier
of `A`.  The two constructions are inverse star homomorphisms.

Their norm is `sup_q||m_q||`: the upper bound follows from (5.6), while for
each `q` an element supported in `I_q`, chosen against an approximate unit
of `B_q`, recovers the multiplier norm of `m_q` arbitrarily closely.  Taking
the supremum proves isometry. `square`

Every `B_q` here is nonzero because Theorem 4.3 embeds the nonzero time
completion into it.  The proof of (5.3) did not assume countability,
separability, unitality, or mutual identifications of the components.

## 6. P13-8B: the origin-free diagonal and exact algebra membership

### Definition 6.1 (time diagonal)

For `a in C_sigma^epsilon`, define

```text
D_sigma^epsilon(a)
  =(d_(q,sigma)^epsilon(a))_(q in Q^bare).          (6.1)
```

Each coordinate in (6.1) lies in `B_q subset M(B_q)`, and Theorem 4.3 gives

```text
||d_(q,sigma)^epsilon(a)||=||a||                  (6.2)
```

for every `q`.  Thus (6.1) is a bounded multiplier family and defines an
element of `M(A)` through Theorem 5.1.

### Theorem 6.2 (isometric faithful diagonal)

The map

```text
D_sigma^epsilon:C_sigma^epsilon->M(A)              (6.3)
```

is an isometric faithful star homomorphism.

#### Proof

Every coordinate map in (6.1) is a star homomorphism, so their product is a
star homomorphism.  The multiplier-product norm and (6.2) give

```text
||D_sigma^epsilon(a)||
  =sup_(q in Q^bare)||d_(q,sigma)^epsilon(a)||
  =||a||.
```

Hence (6.3) is isometric and therefore injective. `square`

The construction is origin-free.  It uses the intrinsic torsors, the bare
index set, and functions constant in the unit variable.  If an origin is
chosen temporarily to present one torsor as `R/H`, changing that origin
acts by an equivariant translation, whose pullback fixes every function
`d_q(f)`.  No such choice enters (6.1), and no simultaneous component
identification is asserted.

### Theorem 6.3 (finite/infinite membership dichotomy)

For every `a in C_sigma^epsilon`,

```text
D_sigma^epsilon(a) in A_(std,sigma)^epsilon
  iff a=0 or Q^bare is finite.                     (6.4)
```

Equivalently,

```text
D_sigma^epsilon(C_sigma^epsilon) intersect A
  =D_sigma^epsilon(C_sigma^epsilon),  if Q^bare is finite,
  ={0},                               if Q^bare is infinite. (6.5)
```

#### Proof

The zero diagonal belongs to `A`.  If `Q^bare` is finite, every finite
family belongs to the `c0` sum.  Conversely, suppose `a!=0` and `Q^bare` is
infinite.  Every coordinate of the diagonal has the positive norm `||a||`.
For `eta=||a||/2`, the set of coordinates whose norm is at least `eta` is
all of `Q^bare`, so condition (5.2) fails.  This proves (6.4), and
faithfulness of `D_sigma^epsilon` gives (6.5). `square`

This is the exact completed analogue of the earlier test-support split.  It
does not replace the `c0` algebra by a bounded product: the bounded product
appears only as its multiplier algebra.

## 7. Infinite branch: exact corona kernel and quotient norm

Assume throughout this section that `Q^bare` is infinite.  Let

```text
pi_cor:M(A)->M(A)/A
```

be the quotient map.

### Theorem 7.1 (faithful isometric corona survival)

The composite

```text
pi_cor o D_sigma^epsilon:
  C_sigma^epsilon -> M(A)/A                       (7.1)
```

is a faithful isometric star homomorphism.  More precisely, for every
`a in C_sigma^epsilon`,

```text
ker(pi_cor o D_sigma^epsilon)
  ={a:D_sigma^epsilon(a) in A}
  ={0},                                            (7.2)

||pi_cor(D_sigma^epsilon(a))||=||a||.              (7.3)
```

#### Proof

The first equality in (7.2) is the definition of the quotient kernel.  The
second is Theorem 6.3.

The quotient norm can also be computed directly.  Fix `b=(b_q) in A` and
`eta>0`.  By the `c0` condition, only finitely many `q` satisfy
`||b_q||>=eta`.  Since `Q^bare` is infinite, choose a coordinate outside
that finite set.  At that coordinate,

```text
||d_(q,sigma)^epsilon(a)-b_q||
  >= ||a||-eta.                                    (7.4)
```

Using the supremum norm in the multiplier product, (7.4) gives

```text
||D_sigma^epsilon(a)-b||>=||a||-eta.
```

Letting `eta` tend to zero and then taking the infimum over `b in A` yields

```text
dist(D_sigma^epsilon(a),A)>=||a||.
```

The reverse inequality follows by taking `b=0` and using Theorem 6.2.
Thus the distance, which is the quotient norm, equals `||a||`.  This proves
(7.3) directly and hence proves both faithfulness and isometry in (7.1).
`square`

For finite `Q^bare`, Theorem 6.3 instead puts the whole diagonal in `A`, so
its corona image is zero.  The two branches are exact.

## 8. Actual-author completion map

Let `Sigma=pi_2^*sigma` be the actual multiplier.  Use the existing author
record names

```text
TW-max-TRANSPORT_X(Sigma) := TW-FULL-TRANSPORT_X(Sigma),
TW-r-TRANSPORT_X(Sigma)   := TW-RED-TRANSPORT_X(Sigma).
```

The frozen P13-4/P13-5 map

```text
Phi_(X,Sigma)(f)(x,t)=f(t)
```

is a star isomorphism on the dense author test records and is isometric for
each separately typed norm.  It therefore extends to an isometric star
isomorphism

```text
widehat(Phi)_(X,Sigma)^epsilon:
  C_sigma^epsilon -> TW-epsilon-TRANSPORT_X(Sigma). (8.1)
```

### Definition 8.1 (actual-to-standard named-record map)

Define

```text
Delta_(X,Sigma)^epsilon
  :=D_sigma^epsilon o
    (widehat(Phi)_(X,Sigma)^epsilon)^(-1),          (8.2)

Delta_(X,Sigma)^epsilon:
  TW-epsilon-TRANSPORT_X(Sigma)
    -> M(A_(std,sigma)^epsilon).
```

### Theorem 8.2 (actual-author location and corona norm)

The map (8.2) is isometric and faithful.  For an author completion element
`z`,

```text
Delta_(X,Sigma)^epsilon(z) in A_(std,sigma)^epsilon
  iff z=0 or Q^bare is finite.                     (8.3)
```

If `Q^bare` is infinite, then

```text
||pi_cor(Delta_(X,Sigma)^epsilon(z))||=||z||,       (8.4)
```

and the corona composite is faithful.

#### Proof

Equation (8.1) and Theorem 6.2 make (8.2) isometric and faithful.  Apply
Theorem 6.3 to
`a=(widehat(Phi)_(X,Sigma)^epsilon)^(-1)(z)` to obtain (8.3).  In the
infinite branch, Theorem 7.1 and the isometry (8.1) give (8.4). `square`

Equation (8.2) is only a map between the named author records displayed
above.  It gives the actual non-Hausdorff owner no additional standard
completion name, and it introduces no additional global completion record.

## 9. Gauge covariance, trivializer independence, and choice firewalls

Let `sigma` and `tau` be normalized continuous time multipliers with the
frozen orientation

```text
sigma overline(tau)=delta alpha.
```

Here `alpha:R->T` is continuous and normalized.

Write `U_alpha^epsilon:C_sigma^epsilon->C_tau^epsilon` for the completed
time gauge map.  Lemma 3.1 supplies the component maps
`U_(alpha,q)^epsilon`.  Their coordinatewise `c0` sum is an isometric star
isomorphism

```text
mathcal(U)_alpha^epsilon:
  A_(std,sigma)^epsilon -> A_(std,tau)^epsilon.     (9.1)
```

Explicitly,

```text
mathcal(U)_alpha^epsilon((b_q)_q)
  =(U_(alpha,q)^epsilon(b_q))_q.
```

Because every coordinate map is isometric, this formula preserves the
supremum norm and the finite-above-each-threshold condition (5.2), in both
directions.  Thus it maps the arbitrary-index `c0` sum onto the corresponding
`c0` sum.  If `i_(q,sigma)` and `i_(q,tau)` denote the two coordinate-ideal
inclusions, its `c0`-level square is

```text
mathcal(U)_alpha^epsilon i_(q,sigma)
  =i_(q,tau) U_(alpha,q)^epsilon.
```

It extends coordinatewise to the multiplier products and descends to their
corona quotients.  Denote those maps by
`M(mathcal(U)_alpha^epsilon)` and
`Cor(mathcal(U)_alpha^epsilon)`.  Write `pi_cor,sigma` and `pi_cor,tau` for
the two corresponding quotient maps.

### Theorem 9.1 (all gauge squares commute)

At component, multiplier-diagonal, and corona levels,

```text
U_(alpha,q)^epsilon d_(q,sigma)^epsilon
  =d_(q,tau)^epsilon U_alpha^epsilon,               (9.2)

M(mathcal(U)_alpha^epsilon) D_sigma^epsilon
  =D_tau^epsilon U_alpha^epsilon,                   (9.3)

Cor(mathcal(U)_alpha^epsilon) pi_cor,sigma D_sigma^epsilon
  =pi_cor,tau D_tau^epsilon U_alpha^epsilon.        (9.4)
```

Let `widehat(U)_(alpha,X)^epsilon` be the completed actual-author gauge map.
Then

```text
M(mathcal(U)_alpha^epsilon) Delta_(X,pi_2^*sigma)^epsilon
  =Delta_(X,pi_2^*tau)^epsilon
     widehat(U)_(alpha,X)^epsilon,                  (9.5)
```

and its corona square is

```text
Cor(mathcal(U)_alpha^epsilon) pi_cor,sigma
    Delta_(X,pi_2^*sigma)^epsilon
  =pi_cor,tau Delta_(X,pi_2^*tau)^epsilon
     widehat(U)_(alpha,X)^epsilon.                  (9.6)
```

#### Proof

On test functions, both sides of (9.2) have value `alpha(t)f(t)` at
`(x,t)`.  The isometric extensions give (9.2).  Taking the bounded product
of the coordinate identities proves (9.3), and applying the quotient maps
proves (9.4).

After completion, and already on the dense actual author test record,

```text
widehat(U)_(alpha,X)^epsilon
  widehat(Phi)_(X,pi_2^*sigma)^epsilon
  =widehat(Phi)_(X,pi_2^*tau)^epsilon
     U_alpha^epsilon.                               (9.7)
```

Substitute (8.2) into (9.3) and use (9.7) to obtain (9.5).  Quotienting
gives (9.6). `square`

The coordinate extensions used above are canonical double-centralizer
extensions: an isomorphism `theta:B->C` sends a multiplier `m` to the
multiplier acting on `c in C` as
`theta(m theta^(-1)(c))`, with the analogous right action.  Hence (9.3) does
not require origins or identifications among distinct components.

### Corollary 9.2 (gauge and trivializer choice independence)

Faithfulness, the finite/infinite membership predicate, and the exact corona
norm are invariant under every allowed gauge.  If
`sigma=delta alpha=delta beta`, then `chi=beta/alpha` is a continuous
character and

```text
U_beta=U_chi U_alpha,
U_(beta,q)=U_(chi,q)U_(alpha,q).
```

Thus the two untwisted presentations differ by the character automorphisms
in the commuting squares above.  They present the same intrinsic twisted
diagonal and the same actual-author map.  No preferred trivializer, Fourier
coordinate, torsor origin, or orbit enumeration is selected.

#### Proof

All maps in (9.1)--(9.5) are isometric isomorphisms and carry the relevant
`c0` ideal onto the corresponding `c0` ideal.  They therefore preserve
membership, intersections, kernels, and quotient norms.  The character
statements are the frozen P13-3 choice theorem followed by Theorem 9.1.
`square`

## 10. P13-8C: unconditional fixed-prime theorem

Fix a rational prime `p`, put `H=(log p)Z`, and let

```text
Q^bare=Q_p^bare,
A_(std,p,sigma)^epsilon
  =direct_sum_(q in Q_p^bare)^c0 B_(q,sigma)^epsilon.
```

Proposition 2.1 gives `|Q_p^bare|=2^aleph_0`, so the infinite branch of
Sections 6--9 applies for every prime.  Write `D_(p,sigma)^epsilon` and
`Delta_(Gamma_p,Sigma)^epsilon` for the maps of Sections 6 and 8 on this
specialized owner, and let `pi_cor` denote its corona quotient.

### Theorem 10.1 (fixed-prime completed diagonal and corona survival)

For every rational prime `p`, every continuous normalized multiplier
`sigma` on `R`, every `epsilon in {max,r}`, and every
`a in C*_(epsilon)(R,sigma)`,

```text
D_(p,sigma)^epsilon(a) in A_(std,p,sigma)^epsilon
  iff a=0.                                          (10.1)
```

Moreover,

```text
||pi_cor(D_(p,sigma)^epsilon(a))||=||a||,           (10.2)

pi_cor o D_(p,sigma)^epsilon
  :C*_(epsilon)(R,sigma)
    ->M(A_(std,p,sigma)^epsilon)/A_(std,p,sigma)^epsilon
```

is an isometric faithful star homomorphism.  For the actual packet multiplier
`Sigma=pi_2^*sigma`, the named author map satisfies

```text
Delta_(Gamma_p,Sigma)^epsilon(z) in
  A_(std,p,sigma)^epsilon
    iff z=0,                                        (10.3)

||pi_cor(Delta_(Gamma_p,Sigma)^epsilon(z))||=||z||. (10.4)
```

All four statements are gauge covariant through the squares in Section 9.

#### Proof

The fixed-prime owner has the common cocompact lattice required in Section
3.  Its bare component set is infinite by Proposition 2.1.  Equations
(10.1)--(10.2) are therefore Theorems 6.3 and 7.1.  Equations
(10.3)--(10.4) are Theorem 8.2.  Gauge covariance is Theorem 9.1. `square`

### Corollary 10.2 (test-level fixed-prime branch)

For every nonzero `f in C_c(R)`, the already proved support theorem at SHA
`f8a0672026b2efaaf07af20d90a17e870e8d0e2f849af0eb78d6dcb1573fb811`
now specializes unconditionally to

```text
J_p^* Phi_actual(f) notin C_c(G_std(Gamma_p)),
T_p intersect C_c(G_std(Gamma_p))={0}.              (10.5)
```

#### Proof

The frozen support theorem says that a nonzero time function has standard
compact support exactly when the bare orbit set is finite.  Proposition 2.1
makes `Q_p^bare` infinite. `square`

Corollary 10.2 is a specialization of the frozen generic test-support proof,
not a new proof or a new contribution claim.  The prime label supplies only
the registered packet owner, local-unit product, and common period.  No
trace, determinant, orbit enumeration, amplitude, analytic continuation,
Weil structure, or quantization conclusion follows.

## 11. Proof-author falsifier and owner audit

| audited surface | exact receipt | prohibited promotion retained |
|---|---|---|
| P13-8A lower bound | imported only from Paper 2 `prop:uncountable`; sign proof not repeated | no Paper-13 novelty, standalone, or Route credit |
| P13-8A upper/equality | countable product upper bound plus inherited lower bound | no CH, Haar measure, or topology in the cardinal proof |
| four quotient owners | actual indiscrete, bare set, standard coproduct, and discrete quotient remain distinct | actual quotient is not called non-second-countable |
| topology consequences | disjoint open components and finite-component compact intersection proved directly | no analytic-framework impossibility inference |
| component test record | intrinsic torsor, frozen signs, Lebesgue range fibres, all-unit regular norm | no common origin or component enumeration |
| time embedding | direct test star map and exact every-unit restriction | no faithfulness inferred from notation |
| max/reduced norms | both inequalities and amenable-time endpoint equality appear in (4.7) | no equality of whole component records claimed |
| arbitrary `c0` sum | bare arbitrary index set and vanishing-at-infinity definition | no replacement of the algebra by a product |
| multiplier identity | direct double-centralizer proof in Theorem 5.1 | no countability, separability, or unitality assumption |
| diagonal | every coordinate lies in `B_q` and has norm `||a||` | no origin-dependent common-model identification |
| membership | zero/finite iff proved from the exact `c0` definition | no finite diagnostic used for the infinite theorem |
| corona | kernel/intersection and quotient norm proved directly | no mere nonzero-in-quotient assertion without isometry |
| actual author map | composition through the proved named time record | no promotion of the actual owner |
| gauge/choices | component, sum, multiplier, corona, and actual squares commute | no preferred trivializer, character coordinate, or origin |
| fixed prime | continuum implies the infinite branch for both `max` and `r` | no arithmetic credit beyond the registered source-origin relation |

The standard `c0`, multiplier, crossed-product, constant-coordinate, and
quotient ingredients are not isolated novelty claims.  The cardinality and
topology packet has zero standalone weight.  Whether the fully typed
maximal/reduced/gauge/corona conjunction is sufficiently central remains for
the required independent post-proof review; this proof record does not close
the binding `NOTE_OR_MERGE` disposition.

## 12. Claim matrix and proof-author disposition

| claim | result in this record | exact owner/credit ceiling | author proof status |
|---|---|---|---|
| P13-8A | elementary upper bound, equality closure from inherited Paper-2 lower bound, exact retyping, and standard/discrete topology consequences | Paper 2 owns the lower bound; Papers 9/12 own quotient/standardization; no standalone weight | **PROVED WITH INHERITED LOWER BOUND** |
| P13-8B | origin-free component embeddings at test/max/reduced levels; exact norm chain; arbitrary-index multiplier identity; diagonal, membership, and corona norm; actual-author map; gauge/choice covariance | componentwise author records only; ordinary ingredients receive no isolated novelty | **PROVED** |
| P13-8C | unconditional fixed-prime max/reduced diagonal, actual-author location, isometric faithful corona maps, gauge covariance, and inherited test-support branch | source-origin specialization only; no A2--A4 promotion | **PROVED** |

Proof-author self-audit:

```text
AUTHORIZED_DESIGN_GATE_SHA256=0094462b1e06cde0cf1fcc3536c608dcd96ef1e9eb0d85a0714df1666b799706
PAPER2_CONTINUUM_LOWER_BOUND_INHERITED=true
P13_8A_LOWER_BOUND_REDERIVED=false
P13_8A_DIRECT_DELTA_PROVED=true
P13_8B_PROVED=true
P13_8B_MAX_PROVED=true
P13_8B_REDUCED_PROVED=true
P13_8C_PROVED=true
P13_8C_MAX_PROVED=true
P13_8C_REDUCED_PROVED=true
MAX_REDUCED_SEPARATELY_PROVED=true
ARBITRARY_INDEX_MULTIPLIER_IDENTITY_DIRECTLY_PROVED=true
CORONA_QUOTIENT_NORM_DIRECTLY_PROVED=true
GLOBAL_COMPLETION_RECORD_ADDED=false
STANDALONE_PASS=false
NOTE_OR_MERGE_BINDING=true
ROUTE_A_AUTHORIZED=false
ROUTE_B_INVOCATION_ALLOWED=false
MANUSCRIPT_AUTHORIZED=false
RELEASE_AUTHORIZED=false
CRITICAL_OPEN=0
MAJOR_OPEN=0
MINOR_OPEN=0
PROOF_AUTHOR_VERDICT=PASS_C0_M0_m0_PENDING_INDEPENDENT_REVIEW
```

**Final proof-author verdict: PASS — C0/M0/m0 on the bounded P13-8A--C
proof lane.**  The artifact remains a proof candidate until an independent
exact-byte proof review acts.  Its SHA-256 is intentionally recorded outside
the file after the bytes are frozen, avoiding a self-digest cycle.
