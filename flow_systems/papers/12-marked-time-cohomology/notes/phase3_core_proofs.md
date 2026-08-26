# Paper 12 Phase-3 core proofs: P12-1--P12-5

Proof date: **2026-08-15 (Asia/Shanghai)**  
Scope: **direct proofs of P12-1 through P12-5 only**  
Proof-lane verdict: **PASS -- C0/M0/m0**  
Independent-review status: **pending**

This report proves the generic all-degree nerve and cochain results, the real
degree-one calculation, and the generic isotropy-image theorem. It does not
prove P12-6, invoke the packet corollary as a conclusion, construct the
P12-7/P12-8 categories or functor, execute P12-9 controls, evaluate Route A,
draft a manuscript, or authorize standalone release.

## 1. Exact authority and input receipt

The work is authorized by the exact current Phase-2 gate tuple:

| Artifact | SHA-256 | Role here |
|---|---|---|
| `notes/phase2_final_gate.md` | `1b05110e23f23848442742b415811205ef24616413b59989996993d4297be9ab` | authorizes direct Phase-3 proofs and deterministic controls only |
| `notes/phase2_status_relock.md` | `c6fb9d3a04171bc68ed6239e1a91cee8f9987cd75d8516967d3ded5de6b89eea` | certifies the status-only transition |
| `notes/pipeline_state.md` | `24c226e35d69c6aab68df19d495957469ec761551680696b20cff865604fe62d` | records Phase 3 as authorized and later gates as blocked |
| `notes/research_protocol.md` | `9213d6e27505c09dbfc24899a15dcca9670e897e754fe40efbc9c1ae7248f434` | fixes signs, domains, targets, falsifiers, and owner ceilings |
| `notes/candidate_lock.md` | `f0878aaf97e44041460b05c59acd5b5a45fd6d1bef2d7042e3ad273de5320d1c` | fixes the candidate and terminology |
| `notes/phase1_design_amendment.md` | `76684044f434c8084712e558c32ee47e996a84763a3eca405f7014ab3d77f949` | v1 correction ledger |
| `notes/phase1_design_amendment_v2.md` | `26222c9e6888f0aa45d019a9f1fd74038285ac460ae6aa0342b8b4e01b4c3285` | v2 packet/Route exactness ledger |
| `notes/phase2_category_owner_audit.md` | `8fad79f121439145e0ac3cac7ca67e82f3e2ad6af86da5b0f001e92da30e1d62` | category, coefficient, and owner ceiling |
| `notes/phase2_framework_source_audit.md` | `32560640ce95894f3b60191593ce55cbcc50a3dd4ce713b148d96cd96bcdfdcb` | exact framework/source strengths |
| `notes/phase2_novelty_search.md` | `c4584862824dbaadec9945fb85defd6d11ee7822849471b075ff4d90d57ca1bd` | bounded `SUPPORTED_WITHIN_SEARCH` result only |
| `notes/phase2_final_review.md` | `032d558fecdccc492ce59733e20dd9322f573d033355aee3c74563680cea2ea7` | independent Phase-2 C0/M0/m0 review |
| `notes/sources/coh-source-manifest.md` | `77adde8e38853b4623212eaf60aee68f5c0d76112d859c643c061fb5b2fddb22` | primary-source manifestations and locators |
| `notes/sources/coh-sources.sha256` | `4a64a9de52d6f2b0b192778afc19b183929818aea3698f3afb9043fab12c20a4` | ten-object source checksum ledger |

The inherited Paper-9 and Paper-11 proof audits were read before this proof
was written; their adjacent frozen source/blueprint hashes were also rebound:

| Dependency | SHA-256 | Licensed inherited strength |
|---|---|---|
| Paper 9 `notes/proof_audit.md` | `c38c24296e5519862eb671dba1644c8005788ac15dffcac48dfdaa1ac3afdde8` | actual fixed-prime packet and every inherited orbit are nontrivial indiscrete spaces |
| Paper 9 `notes/source_audit.md` | `20fecdf360d18f9accf3e3ec8467f3beb369a8737761eb6219fef71e9773ac20` | exact Deninger source/action/stabilizer ceiling |
| Paper 11 `notes/proof_audit.md` | `03f17606b0c9d69b496d2766c0a404b0d090698101150a800de4c2108ddc6b28` | range-first arrow topology and degree-one `T0` time factorization |
| Paper 11 `notes/composition_blueprint.md` | `4b6bfa27c83f72858ac5f0d03c0b9964f93e914fc1d4fdfced619327bcdfc30b` | inherited-credit and terminology ceiling |

The final source checksum command passed `10/10` entries before proof work.
All inputs listed above are rehashed again after writing in Section 10's
mechanical closeout. No source PDF is edited or used as a public artifact.

## 2. Frozen setting and notation

Let `X` be a nonempty indiscrete space with an arbitrary right action of the
additive group `R`, written `x dot t`. Set

```text
G=G(X,alpha)=X rtimes R,
r(x,t)=x,
s(x,t)=x dot t,
(x,t)(x dot t,u)=(x,t+u),
(x,t)^(-1)=(x dot t,-t).
```

The arrow topology is the product of the indiscrete topology on `X` and the
usual topology on `R`. Fix the named coefficient object `A`: a `T0`
topological abelian group whose addition and inversion are continuous. The
generic claims below use no transitivity, freeness, stabilizer, lattice,
arithmetic label, or Deninger normalization.

For `n>=1`, write `G^(n)` for composable `n`-tuples with the subspace topology
from `G^n`, and put `G^(0)=X`. Let

```text
Psi_n(x;t_1,...,t_n)
 =((x,t_1),
   (x dot t_1,t_2),
   ...,
   (x dot (t_1+...+t_(n-1)),t_n)).
```

All cochains below are global continuous maps. There is no support,
boundedness, integrability, smoothness, Borel-only, decay, or compactness
condition, and no normalized-subcomplex condition.

## 3. P12-1: all finite nerve charts, faces, and degeneracies

### Theorem 3.1 (all-degree nerve topology)

For every `n>=1`, `Psi_n:X x R^n -> G^(n)` is a homeomorphism. In these
coordinates, the open subsets of `G^(n)` are exactly

```text
emptyset  and  X x U,  with U open in R^n.
```

#### Proof

A composable tuple has a unique first range `x` and unique time coordinates
`t_1,...,t_n`. Composability recursively forces the range of its `j`th arrow
to be `x dot (t_1+...+t_(j-1))`. Hence `Psi_n` is bijective, with inverse

```text
Theta_n((x_1,t_1),...,(x_n,t_n))=(x_1;t_1,...,t_n).
```

Reorder the coordinates of `G^n=(X x R)^n` as `X^n x R^n`. Because every
finite power `X^n` is indiscrete, every open subset of `G^n` is exactly
`X^n x U` for an open `U subset R^n`. Its intersection with `G^(n)` pulls
back under `Psi_n` to `X x U`. Conversely every `X x U` is the pullback of
that open. Thus `Psi_n` and `Theta_n` are continuous and open, proving the
homeomorphism and the asserted complete list of opens. This argument works
for every finite `n`; it is not an extrapolation from the arrow case. QED.

### Exact face coordinates

Let `partial_i^n:G^(n)->G^(n-1)`, `0<=i<=n`, be the nerve faces. For `n>=2`,
their exact coordinate formulas are

```text
partial_0^n Psi_n(x;t_1,...,t_n)
  =Psi_(n-1)(x dot t_1;t_2,...,t_n),

partial_i^n Psi_n(x;t_1,...,t_n)
  =Psi_(n-1)(x;t_1,...,t_i+t_(i+1),...,t_n),  1<=i<=n-1,

partial_n^n Psi_n(x;t_1,...,t_n)
  =Psi_(n-1)(x;t_1,...,t_(n-1)).
```

In degree one,

```text
partial_0^1(x,t)=s(x,t)=x dot t,
partial_1^1(x,t)=r(x,t)=x.
```

These are precisely the protocol's order: the first face drops the first
arrow, an interior face multiplies adjacent arrows, and the last face drops
the last arrow. Each is continuous. For `partial_0`, the time part is a
coordinate projection and the `X`-valued part is continuous because `X` is
indiscrete (also because the action is continuous). Interior faces use
continuous addition in `R`; the last face is a projection.

### Exact degeneracy coordinates

Let `sigma_i^n:G^(n)->G^(n+1)`, `0<=i<=n`, insert the identity at the `i`th
vertex. Then

```text
sigma_i^n Psi_n(x;t_1,...,t_n)
 =Psi_(n+1)(x;t_1,...,t_i,0,t_(i+1),...,t_n).
```

Empty strings at either endpoint are omitted. In particular,
`sigma_0^0(x)=(x,0)`. These maps are continuous because they leave the first
unit coordinate unchanged and insert the constant real coordinate zero.

The formulas directly satisfy the simplicial identities. For faces, with
all degree superscripts restored, the identity used below is

```text
partial_i^(m-1) partial_j^m
 =partial_(j-1)^(m-1) partial_i^m,  0<=i<j<=m.
```

This is checked in coordinates: disjoint additions commute; adjacent
additions agree by `(t_i+t_(i+1))+t_(i+2)=t_i+(t_(i+1)+t_(i+2))`; the
`i=0,j=1` case is exactly `(x dot t_1) dot t_2=x dot (t_1+t_2)`; and endpoint
deletions commute with the remaining operation. Face-degeneracy identities
reduce to inserting and then deleting zero, using `t+0=0+t=t` and
`x dot 0=x`; two degeneracies reduce to the equality of the two orders of
inserting zeros. Thus the face and degeneracy maps are established with the
frozen right-action/range-first signs. No normalized-cochain conclusion is
drawn from the degeneracies.

**P12-1 verdict: PROVED.**

## 4. P12-2: the author-defined complex and a direct proof that d squared is zero

### 4.1 Constant coefficient bundle and action

Use the frozen bundle

```text
underline(A)_X=X x A -> X,
gamma . (s(gamma),a)=(r(gamma),a).
```

The action domain is

```text
G _s times_prX (X x A)
 ={((x,t),(x dot t,a))}.
```

On it the action map is `((x,t),(x dot t,a)) |-> (x,a)`. It is the
restriction of the continuous product map

```text
(gamma,(y,a)) |-> (r(gamma),a)
```

on `G x (X x A)`. Identity and composition act as the identity on `a`, so
the bundle action is continuous and satisfies the coefficient-system axioms.
This is an elementary author-defined trivial coefficient system; no source
framework is imported to enlarge its domain.

### 4.2 Cochains and differential

After the displayed trivialization, set

```text
C_cnv^0(G;underline(A))=C(X,A),
C_cnv^n(G;underline(A))=C(G^(n),A),  n>=1,
```

with pointwise addition. For `h in C_cnv^0`, define

```text
(d^0 h)(gamma)=h(s gamma)-h(r gamma).
```

For `n>=1`, define, with the faces of Section 3,

```text
d^n f=sum_(i=0)^(n+1) (-1)^i (partial_i^(n+1))^* f.
```

Equivalently, on a composable `(n+1)`-tuple,

```text
(d^n f)(gamma_1,...,gamma_(n+1))
 = f(gamma_2,...,gamma_(n+1))
   +sum_(i=1)^n (-1)^i
      f(gamma_1,...,gamma_i gamma_(i+1),...,gamma_(n+1))
   +(-1)^(n+1)f(gamma_1,...,gamma_n).
```

Every pullback is continuous by Section 3, and every finite alternating sum
is continuous because addition and inversion in `A` are continuous. Thus
each `d^n` has exactly the displayed domain and codomain.

### 4.3 Direct cancellation proof

Let `f in C_cnv^n`. Expanding twice and retaining the order of pullbacks
gives

```text
d^(n+1)d^n f
 =sum_(j=0)^(n+2) sum_(i=0)^(n+1)
    (-1)^(i+j)
    f o partial_i^(n+1) o partial_j^(n+2).
```

For every pair `i<j`, the face identity proved directly in Section 3 gives

```text
partial_i^(n+1) partial_j^(n+2)
 =partial_(j-1)^(n+1) partial_i^(n+2).
```

The term indexed `(i,j)` therefore has the same composite map as the term
whose inner-face index is `j-1` and outer-face index is `i`. Their signs are

```text
(-1)^(i+j)  and  (-1)^((j-1)+i)=-(-1)^(i+j).
```

Pairs with `i<j` and their partners partition the full double sum, so every
term cancels exactly in the abelian group `A`. This also covers `n=0`; in
that degree the three face identities are the action law and the source/range
identities displayed in Section 3. Hence

```text
d^(n+1)d^n=0  for every n>=0.
```

It follows, purely algebraically, that

```text
Z_cnv^n=ker d^n,
B_cnv^0={0},
B_cnv^n=im d^(n-1)  (n>=1),
H_cnv^n=Z_cnv^n/B_cnv^n
```

are abelian groups, and are real vector spaces when `A=R`. No topology on a
cochain group and no quotient topology on `H_cnv^n` is defined or claimed.

**P12-2 verdict: PROVED.**

## 5. P12-3: all-degree time-projection chain isomorphism

### Lemma 5.1 (all-degree T0 factorization)

For every `n>=0`, every continuous map `F:X x R^n -> A` is independent of
the `X` coordinate. For `n=0`, this means every continuous `X->A` map is
constant.

#### Proof

Fix `t in R^n`. For all `x,y in X`, the points `(x,t)` and `(y,t)` have the
same open neighborhoods, because every open of `X x R^n` is `X x U`. If
`F(x,t)` and `F(y,t)` were distinct, the `T0` axiom for `A` would supply an
open set containing one image and not the other. Its inverse image would
distinguish `(x,t)` from `(y,t)`, a contradiction. Thus the values agree.
The same argument with no time coordinate proves the degree-zero assertion.
QED.

Choose `x_0 in X`, which is possible because `X` is nonempty. Let `pi_n` be
time projection in the `Psi_n` chart, and let `pi_0:X->{*}`. Define

```text
T_0:A -> C(X,A),              T_0(a)(x)=a,
T_n:C_cnv^n(R;A)->C_cnv^n(G;underline(A)),
T_n(f)(Psi_n(x;t_1,...,t_n))=f(t_1,...,t_n),  n>=1.
```

Here `C_cnv^bullet(R;A)` is the same author-defined unnormalized
inhomogeneous continuous complex on the one-object additive topological
group `R`, with trivial coefficients and the same signs.

Define evaluation candidates

```text
E_(x_0),0(h)=h(x_0),
E_(x_0),n(F)(t_1,...,t_n)
 =F(Psi_n(x_0;t_1,...,t_n)).
```

The insertion `t |-> (x_0,t)` is continuous by the open-set description, so
`E_(x_0),n(F)` is continuous. Lemma 5.1, applied only now, gives

```text
E_(x_0) T=id,
T E_(x_0)=id.
```

It also proves that `E_(x_0)=E_(x_1)` for every other chosen unit `x_1`.
Thus unit-independence is a consequence of the `T0` factorization theorem,
not an assumption used to define the inverse.

### Chain-map calculation

Let `bar_partial_i` denote the one-object group faces. Their time formulas
are

```text
bar_partial_0(t_1,...,t_(n+1))=(t_2,...,t_(n+1)),
bar_partial_i(...)=
  (t_1,...,t_i+t_(i+1),...,t_(n+1)),  1<=i<=n,
bar_partial_(n+1)(t_1,...,t_(n+1))=(t_1,...,t_n).
```

The coordinate formulas of Section 3 give, for every face,

```text
pi_n partial_i^(n+1)=bar_partial_i pi_(n+1).
```

The first groupoid face changes the unit from `x` to `x dot t_1`, but it
drops exactly `t_1`; hence it has the same projected time face. Therefore,
with the frozen signs,

```text
d_G^n T_n f
 =sum_i (-1)^i f pi_n partial_i
 =sum_i (-1)^i f bar_partial_i pi_(n+1)
 =T_(n+1)d_R^n f.
```

In degree zero, both group faces land at the one object, so `d_R^0(a)=0`,
while the coboundary of the constant `T_0(a)` is also zero. Thus the equality
holds in every degree. Since every `T_n` is bijective with the already-proved
choice-independent inverse `E_n`, `T_bullet` is an isomorphism of cochain
complexes.

### Sharp coefficient boundary

The `T0` condition cannot be dropped. Let `X={x_0,x_1}` be indiscrete with
the trivial action, and let `A=Z/2Z` carry the indiscrete, hence non-`T0`,
topology. The nonconstant degree-zero function

```text
h(x_0)=0,  h(x_1)=1
```

is continuous but is not in the image of `T_0`. The same unit dependence can
be extended constantly in the time variables in higher degrees. Thus the
failure is at the exact coefficient hypothesis, not at the action or nerve
calculation.

**P12-3 verdict: PROVED for every named `T0` topological abelian coefficient
group `A`; refuted without that hypothesis.**

## 6. P12-4: real degree-one classification and the marked coordinate class

Now specialize to `A=R` with its usual topology and trivial coefficients.
Define

```text
c(x,t)=t.
```

It is continuous because it is time projection. Let `b` be a continuous
one-cochain. Lemma 5.1 gives a unique continuous `f:R->R` such that
`b(x,t)=f(t)`. In `Psi_2(x;t,u)` coordinates, the frozen differential is

```text
(d^1 b)(x;t,u)=f(u)-f(t+u)+f(t).
```

Hence `b` is a cocycle exactly when

```text
f(t+u)=f(t)+f(u)  for all t,u in R.
```

The continuity step is direct. Additivity gives `f(0)=0`,
`f(m)=m f(1)` for integers `m`, and `f(m/n)=(m/n)f(1)` for rationals with
`n!=0`. For any real `t`, choose rationals `q_k->t`; continuity gives

```text
f(t)=lim_k f(q_k)=lim_k q_k f(1)=t f(1).
```

Writing `lambda=f(1)`, every cocycle is therefore `lambda c`, and every such
multiple is visibly a cocycle. Thus

```text
Z_cnv^1(G;R)=R c.
```

Every continuous `h:X->R` is constant by Lemma 5.1 in degree zero. Hence

```text
(d^0 h)(x,t)=h(x dot t)-h(x)=0,
B_cnv^1(G;R)={0},
H_cnv^1(G;R)=R[c].
```

The last equality is an equality of algebraic real vector spaces; no
cohomology topology is present. The argument is specific to real
coefficients at the continuous Cauchy step and does not classify degree-one
cohomology for arbitrary `A`.

The coordinate cocycle is not a Paper-11 global-QC test function. It is
unbounded, its nonzero set is `X x (R minus {0})`, and its support is all of
`X x R`; the time support is therefore not compact. The generic formula
selects a coordinate cocycle only. The arithmetic source normalization that
marks `[c]` is a later same-owner input; the abstract one-dimensional vector
space alone does not recover a preferred arithmetic scale.

**P12-4 verdict: PROVED.**

## 7. P12-5: isotropy restriction, descent, period formula, and unit transport

For a unit `x`, let

```text
H_x=Stab_R(x)={t in R:x dot t=x},
G_x^x={(x,t):t in H_x}.
```

The action law shows directly that `H_x` is a subgroup of `R`: zero fixes
`x`, sums of stabilizing times stabilize `x`, and applying `-t` to
`x dot t=x` shows that `-t` also stabilizes `x`.

The map `t |-> (x,t)` is a topological-group isomorphism from `H_x` with its
subspace topology in `R` onto `G_x^x` with its arrow-subspace topology. No
closedness or discreteness of `H_x` is assumed.

### Proposition 7.1 (restriction on cocycles)

For `b in Z_cnv^1(G;R)`, its restriction to `G_x^x` is a continuous group
homomorphism. Moreover

```text
res_x:Z_cnv^1(G;R)->Hom_cont(G_x^x,R),
res_x(b)=b|_(G_x^x)
```

is itself a homomorphism of abelian groups.

#### Proof

If `t,u in H_x`, then `(x,t)` and `(x,u)` are composable isotropy arrows and
their product is `(x,t+u)`. The cocycle equation gives

```text
b(x,t+u)=b(x,t)+b(x,u).
```

Continuity is inherited by restriction. Pointwise restriction also satisfies
`res_x(b+b')=res_x(b)+res_x(b')`. QED.

### Proposition 7.2 (coboundary vanishing and class descent)

Every one-coboundary vanishes on every isotropy group. Consequently

```text
Per_x([b])=image(res_x(b)) subset R
```

is well-defined on `H_cnv^1(G;R)` and is an additive subgroup of `R`.

#### Proof

For `b=d^0h` and `(x,t) in G_x^x`, range and source both equal `x`, so

```text
b(x,t)=h(s(x,t))-h(r(x,t))=h(x)-h(x)=0.
```

Thus if `b'` and `b` represent the same class, their restrictions agree
pointwise, not merely in image. Proposition 7.1 then makes their common image
an additive subgroup. This proof logically precedes the definition of
`Per_x` on cohomology classes; it does not rely on the later observation that
real continuous coboundaries vanish globally. QED.

### Proposition 7.3 (generic period formula)

For every `lambda in R`,

```text
Per_x([lambda c])=lambda H_x.
```

#### Proof

On isotropy, `(lambda c)(x,t)=lambda t`. Its image as `t` runs over `H_x`
is exactly `{lambda t:t in H_x}=lambda H_x`. QED.

This formula includes `lambda=0`, whose image is `{0}`. It neither assumes
nor concludes that `H_x` is a lattice.

### Proposition 7.4 (transitive-unit transport)

If the right `R`-action is transitive, then `H_x=H_y` for all units `x,y`.
For every real one-cocycle `b`, conjugation between the corresponding
isotropy groups preserves its values, so `Per_x([b])=Per_y([b])`.

#### Proof

Write `y=x dot u`. If `t in H_y`, then

```text
x dot (u+t)=y dot t=y=x dot u.
```

Acting on both sides by `-u` and using commutativity of additive `R` gives
`x dot t=x`; hence `H_y subset H_x`. Replacing `u` by `-u` gives the reverse
inclusion.

For the value statement, put `eta=(x,u)` and `gamma=(y,t)`. Then

```text
eta gamma eta^(-1)=(x,t).
```

A one-cocycle is additive on products. It vanishes on units and takes
`eta^(-1)` to `-b(eta)`, so

```text
b(x,t)=b(eta)+b(y,t)+b(eta^(-1))=b(y,t).
```

Thus conjugate restrictions have the same image. In this additive abelian
action, conjugation also leaves the time label `t` itself unchanged. QED.

### Corollary 7.5 (the precise lattice-scale blindness)

Under the additional hypothesis `H_x=L Z` with `L>0`, the marked coordinate
class recovers that chosen lattice:

```text
Per_x([c])=L Z.
```

But if the mark is forgotten and the class ranges over all nonzero elements
of the algebraic line `H_cnv^1(G;R)`, then

```text
{Per_x([lambda c]):lambda in R^x}
 ={lambda L Z:lambda in R^x}
 ={r Z:r>0},
```

which is independent of the original positive generator `L`. This is the
only scale-blindness claimed here. Trivial stabilizer `R`, free stabilizer
`{0}`, dense stabilizer `Q`, and nontransitive actions are not forced into
the lattice conclusion.

**P12-5 verdict: PROVED.**

## 8. Integrated theorem/proof matrix

| Target | Exact proved conclusion | Load-bearing direct step | Hypothesis that may not be dropped | Status |
|---|---|---|---|---|
| `P12-1` | `Psi_n` is a homeomorphism for every finite `n`; opens are exactly `X x U`; all faces and degeneracies have the displayed coordinates and are continuous | finite-product indiscreteness plus the explicit inverse; direct right-action/addition checks | `X` indiscrete; finite nerve degree | `PROVED` |
| `P12-2` | the constant identity-action bundle is continuous; the global unnormalized differential is well typed and satisfies `d^(n+1)d^n=0` | exact face identity and sign-reversing pair cancellation | abelian coefficient group with continuous `+` and `-` for continuity of cochains | `PROVED` |
| `P12-3` | `T_bullet=pi_bullet^*` is an all-degree cochain-complex isomorphism; evaluation is its unit-independent inverse | topological indistinguishability plus `T0`; exact projected-face identities | nonempty `X`; coefficient `A` is `T0` | `PROVED`; non-`T0` removal `REFUTED` |
| `P12-4` | `Z_cnv^1=R c`, `B_cnv^1=0`, `H_cnv^1=R[c]` algebraically | time factorization, exact `d^1` sign, continuous Cauchy theorem, degree-zero constancy | usual real coefficient topology; no cochain topology inferred | `PROVED` |
| `P12-5` | restriction lands in continuous isotropy homomorphisms, kills coboundaries, descends to `Per_x`; `Per_x([lambda c])=lambda H_x`; transitive units transport exactly | direct product/coboundary/conjugation calculations | lattice-scale statement additionally requires `H_x=LZ`, `L>0` | `PROVED` |

Proof dependencies are one-way:

```text
all-degree nerve topology and exact faces
  -> well-typed direct d^2 proof
  -> all-degree T0 factorization and projected-face chain map
  -> real degree-one Cauchy classification
  -> representative-independent isotropy image and transitive transport.
```

No finite control is used as proof of a universal statement.

## 9. Claim-owner/source-domain matrix

| Claim surface | Exact owner | Source/comparator strength retained | Forbidden promotion |
|---|---|---|---|
| generic `G(X,alpha)`, its full nerve, and `C_cnv/H_cnv` | Paper 12 author construction and the direct proofs above | Paper 11 supplies only the inherited arrow (`n=1`) base case and degree-one factorization | no arithmetic, packet, standard groupoid-cohomology, or Deninger credit |
| real one-object comparison complex on `R` | additive topological group `R`; Paper-12 frozen inhomogeneous convention | Blanco--Uribe--Waldorf is an exact `(R,R)` continuous-cochain comparator; Fuchssteiner--Wockel is a one-object group comparator | no transfer of a group theorem to the actual groupoid without the direct proof above |
| actual all-degree groupoid complex at generic `T0 A` | Paper 12 author-defined `C_cnv/H_cnv` | Blanco--Uribe--Waldorf is conditional at the audited simplicial-paracompact/coefficient strength; Mackenzie is a stricter Hausdorff/local-trivial formula/module comparator only | do not call the full generic object unqualified continuous topological-groupoid cohomology |
| real degree-one cocycles and coboundaries | direct P12-4/P12-5 proof on the author groupoid | Farsi--Huang--Kumjian--Packer supports degree-one terminology for `R`; its opposite coboundary sign has the same image after negating the unit function | no all-degree or marked-period theorem imported from Definition 3.7 |
| actual fixed orbit/packet topology | Paper 9 | exact inherited indiscreteness only | no ordinary-circle topology and no Paper-12 cohomology credit to Paper 9 |
| Deninger fixed-prime packet/action/stabilizer/clock | Deninger at the frozen p. 38--39 locators | source input for the later P12-6 application only | no “Deninger groupoid,” “Deninger cohomology,” topology, or P12-1--P12-5 ownership |
| standard `R/H` quotient | not constructed in this report; reserved for P12-8 | Paper 10 supplies the one-sided actual-versus-standard topology boundary | no identification with the actual inherited indiscrete orbit |

The bounded literature statement remains exactly `SUPPORTED_WITHIN_SEARCH`.
Nothing in these direct proofs upgrades it to an absolute priority claim.

## 10. Falsifier and integrity closeout

| Preregistered falsifier or common failure | Direct check | Result |
|---|---|---|
| some finite `Psi_n` is not a homeomorphism | explicit inverse plus complete open-set calculation for arbitrary finite `n` | not observed; theorem proves the contrary |
| face/sign mismatch breaks `d^2=0` | exact range-first coordinates; adjacent case uses the right-action law; every double-sum term has an opposite-sign partner | not observed |
| a continuous `T0`-valued cochain retains unit dependence | indistinguishable-point argument in every degree | impossible under hypotheses |
| removing `T0` leaves the theorem true | indiscrete `Z/2Z` coefficient and nonconstant degree-zero map | explicit counterexample; removal refuted |
| `T_bullet` fails to commute with `d` | `pi partial_i=bar_partial_i pi` for every face, including the unit-changing first face | not observed |
| a nonlinear continuous real additive cocycle exists | rational-density Cauchy proof | impossible |
| a nonzero continuous real coboundary exists | every continuous `X->R` map is constant | impossible |
| `Per_x([b])` depends on representative | every coboundary is zero on isotropy before the image is defined | impossible |
| transitive units have different stabilizers or restriction images | direct additive conjugation by `(x,u)` | impossible for this `R` action |
| every stabilizer is a lattice | trivial/free/dense/nontransitive domains remain allowed | claim expressly not made |
| `c` belongs to Paper-11 `C_qc^glob` | `supp(c)=X x R`, and `c` is unbounded | refuted; domains remain distinct |
| generic collapse is arithmetically selective | the proof never uses `p`, `a`, a period, a stabilizer, or transitivity | `PROVES_TOO_MUCH` for arithmetic specificity |

Mechanical closeout requirements for the caller are now satisfied as
follows: the authorization, lock, Phase-2, source-manifest, and inherited
proof inputs listed in Section 1 are rehashed after this file write; the
source checksum ledger is rechecked; and no file other than
`notes/phase3_core_proofs.md` is written by this proof lane.

Finding register:

| Severity | Count | Open item |
|---|---:|---|
| Critical (`C`) | 0 | none |
| Major (`M`) | 0 | none |
| Minor (`m`) | 0 | none |

**Final proof-lane verdict: PASS (`C0/M0/m0`).** P12-1 through P12-5 are
proved at the frozen signs and domains. P12-6 through P12-10, independent
Phase-3 review, Route, composition, manuscript, standalone, and release
decisions remain outside this report and retain their own gates.
