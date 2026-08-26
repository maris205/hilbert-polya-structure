# Paper 12 Phase-3 v4 proofs: orbitwise standardization and the `H^1` diagonal

Proof date: **2026-08-15 (Asia/Shanghai)**  
Authorized lane: **the exact v4 proof package only**  
Proof-lane verdict: **PASS -- C0/M0/m0**  
Standalone disposition: **proof-side repair complete; independent disposition pending**

This report proves the v4 common-stabilizer, orbitwise-standardization,
automorphism, and degree-one cohomology package. It writes no lock, control,
Route, composition, manuscript, or release artifact. In particular, it does
not execute the frozen `STD-COPROD-H1` controls and does not grant
`STANDALONE_PASS`.

## 1. Exact authority and input receipt

### 1.1 Current active tuple and gates

The proof is authorized by the current active tuple and the narrow final
design/source gate below. Every digest was recomputed before proof work.

| Artifact | SHA-256 | Authority in this lane |
|---|---|---|
| `notes/research_protocol.md` | `a32ed2137bed3d6784fdba170a1b1041157907c772c2de12e07e65a087ea919f` | active theorem, owner, falsifier, and Route ceilings |
| `notes/candidate_lock.md` | `654f026cb59ed4df8c81a8f994e8857ce11428f1e7bc7fdb3e06ad254d4acb41` | active candidate and terminology lock |
| `notes/pipeline_state.md` | `f5ee48cc308df835cbdc840169c51e63da1a80b10e45db87881913fa46bbacbf` | records targeted proof/controls as authorized and later stages as blocked |
| `notes/phase3_v4_design_gate.md` | `ab3862cd0455d0c3f7e7773fe48aa2ee65c5d2934f557b722d454f0117df3e1a` | v4 repair boundary |
| `notes/phase3_standalone_amendment_v4.md` | `5d9ca4357639bc1e290ca5b85b540a28bfb2a4452ab81826ee9106ae147f0809` | exact proof obligations |
| `notes/phase3_v4_final_gate.md` | `974a3f1be30aeaced279b31b3d403450e292144802370c7515e3e3ac644f41e0` | authorizes only this proof and the frozen deterministic controls |
| `notes/phase3_v4_status_relock.md` | `64a63d8b7565add4047875c9610a408d1e4264b8e205e600814de778b93ab90d` | certifies the active status-only transition, including the candidate-Section-9 closure, at C0/M0/m0 |

The final gate binds the independently reviewed predecessor content tuple.
The status re-lock proves by exact inverse reconstruction that the current
protocol, candidate, and pipeline differ from that reviewed tuple only in
gate/status provenance. Thus this proof uses the current active bytes without
silently treating a status edit as a mathematical re-lock.

### 1.2 Stable mathematical and independent-review inputs

| Artifact | SHA-256 | Permitted use |
|---|---|---|
| `notes/phase3_disposition_gate.md` | `cc0a9578d187f5dad443b7dc37870e7c24278fca5f02ad532523aeee76ceefa8` | conservative v2 standalone hold and exact repair target |
| `notes/phase3_core_proofs.md` | `9ab5c860f2ceceba27aa820ddd66564f9a7be2f2ee21bc06ea7110d1c38c16cd` | frozen differential, actual all-degree complex, and actual `H^1=R[c]` |
| `notes/phase3_marked_packet_proofs.md` | `3cf4a29d97499e1875d8f5bbfb1124d88e45e972ad3dbadbe6b8fffb5a3e6d49` | strict-arrow normal form precursor, packet source chain, and mark conventions |
| `notes/phase3_standalone_review.md` | `a05139142f24b75b682561c732045787923d5c9d6a6d619657880919ba9a39ec` | the prior routine-reduction Major that this lane addresses only on the proof side |
| `notes/phase3_v4_methodology_relock.md` | `c31e1c6d6b21eb4d9de0c698fcbd10bbd2516a7e8a3e477eba591e88de7bfb81` | final corrected tuple, methodology PASS C0/M0/m0 |
| `notes/phase3_v4_devils_advocate.md` | `9a9a87fa621b0d0434fb2f0ece635e45a4b721a2f65c238ef4ca441f69aea190` | final corrected tuple, domain/devil PASS C0/M0/m0 |
| `notes/phase3_v4_source_novelty_audit.md` | `cf985db1270bb6b1480f0b29a7770e0865a627ea2412adfc6c4476eeba439c22` | source feasibility, exact precedent ceilings, and `SUPPORTED_WITHIN_SEARCH` only |
| `notes/phase2_final_review.md` | `032d558fecdccc492ce59733e20dd9322f573d033355aee3c74563680cea2ea7` | accepted same-object packet source/action/clock/stabilizer chain |

The inherited owner bytes also match: Paper 9 proof
`c38c24296e5519862eb671dba1644c8005788ac15dffcac48dfdaa1ac3afdde8`,
Paper 9 source
`20fecdf360d18f9accf3e3ec8467f3beb369a8737761eb6219fef71e9773ac20`,
Paper 10 proof
`efda522ead9efebfc3f59f0688f2dfd3fe63f63ff4efd4377068485d1a4acc3a`,
Paper 11 proof
`03f17606b0c9d69b496d2766c0a404b0d090698101150a800de4c2108ddc6b28`,
and Paper 11 composition blueprint
`4b6bfa27c83f72858ac5f0d03c0b9964f93e914fc1d4fdfced619327bcdfc30b`.

## 2. Frozen categories and main theorem

Fix `H=LZ` with `L>0`. An object of `C_common(H)` is

```text
(G_actual=X_indisc rtimes R,c),
c(x,t)=t,
Stab_R(x)=H for every x in X,
```

where `X` is nonempty, carries one global indiscrete topology, and has a
jointly continuous right `R`-action (continuity is automatic for a map into
the globally indiscrete unit space). The range-first operations are

```text
r(x,t)=x,
s(x,t)=x dot t,
(x,t)(x dot t,u)=(x,t+u).
```

Morphisms are strict marked topological-groupoid isomorphisms. Put

```text
C_common=disjoint-union_(L>0) C_common(LZ).
```

Let `Q=X/R`, used initially only as the nonempty bare set of action orbits.
Let `Tor_R^coprod(H)` be the category of nonempty topological coproducts of
standard right `R/H` homogeneous torsors, with strictly `R`-equivariant
homeomorphisms. Its disjoint union over positive lattice generators is
`Tor_R^coprod`.

### Theorem 2.1 (the v4 package)

For every object of `C_common(H)`:

1. there is a section-free topology `Std_coprod(X)` on the same set, obtained
   by putting the quotient `R/H` topology on each orbit and taking their
   topological coproduct;
2. this topology is Hausdorff, makes the action jointly continuous, has open
   orbits, and is the unique topology with those three properties;
3. `Std_coprod:C_common->Tor_R^coprod` is full and faithful and has the
   concrete strict inverse `Indisc`;
4. canonically as abstract groups, in ZFC,

   ```text
   1 -> (R/H)^Q -> Aut_R(Std_coprod(X)) -> Sym(Q) -> 1;
   ```

   an orbit-origin choice splits it noncanonically;
5. for the frozen author complex with trivial real coefficients,

   ```text
   rho:H_cnv^1(G_std;R) -> R^Q,
   rho([b])(q)=b(x,L)/L, x in q,
   ```

   is a canonical algebraic isomorphism; and
6. for the continuous identity marked functor

   ```text
   J:G_std -> G_actual,
   ```

   one has

   ```text
   rho(J^*(lambda[c]))=(q |-> lambda),
   image(J^*)=(R^Q)^(Aut_R(G_std))
              ={constant functions Q->R}.
   ```

No topology is placed on `R^Q`, either cohomology group, or either
automorphism group.

## 3. Strict marked arrows and fixed-stabilizer components

### Proposition 3.1 (strict-arrow normal form)

Let `F:(G,c)->(G',c')` be a strict marked groupoid isomorphism. Then uniquely

```text
F(x,t)=(F_0(x),t),
F_0(x dot t)=F_0(x) dot t.
```

It follows that `F_0` maps orbits bijectively to orbits and preserves the
stabilizer as a literal subgroup of the same time line.

#### Proof

The range of `F(x,t)` is `F_0(x)`. The strict equation gives
`c'(F(x,t))=t`. In a range-first transformation groupoid, range and time
determine the arrow uniquely, so `F(x,t)=(F_0(x),t)`. Comparing sources gives

```text
F_0(x dot t)=F_0(x) dot t.
```

The inverse has the same form, so `F_0` is an equivariant bijection and hence
maps orbits bijectively. Finally,

```text
t in Stab_R(x)
iff F_0(x dot t)=F_0(x)
iff F_0(x) dot t=F_0(x)
iff t in Stab_R(F_0(x)).
```

Thus a strict arrow cannot connect `C_common(LZ)` to
`C_common(MZ)` unless `LZ=MZ`, which for `L,M>0` forces `L=M`. This proves
the asserted disjoint-union category decomposition. QED.

Conversely, an equivariant bijection `phi:X->X'` between globally indiscrete
unit spaces has the unique strict lift

```text
F_phi(x,t)=(phi(x),t).
```

Both unit maps are homeomorphisms because the spaces are indiscrete. The
arrow map and inverse are continuous: every arrow open is `X' x U`, whose
preimage is `X x U`. Equivariance verifies source preservation, and the
range, multiplication, inverse, and mark formulas are immediate. This
converse will supply fullness below.

## 4. Section-free orbitwise standardization

Fix an orbit `O` and a unit `x in O`. Define

```text
q_x:R->O, q_x(t)=x dot t.
```

### Lemma 4.1 (quotient chart and basepoint independence)

Give `O` the quotient topology for `q_x`. This topology is independent of
`x`, and the induced map

```text
bar(q)_x:R/H -> O,
[t] |-> x dot t,
```

is an equivariant homeomorphism.

#### Proof

The map `q_x` is surjective and

```text
q_x(t)=q_x(u) iff t-u in H.
```

It therefore induces the displayed bijection. By the definition of the
quotient topologies on both sides, the bijection and its inverse are
continuous.

If `x'=x dot u`, then, for `T_u(t)=u+t`,

```text
q_(x')(t)=x dot(u+t)=(q_x o T_u)(t).
```

Because `T_u` is a homeomorphism of `R`, a subset of `O` has open inverse
image under `q_(x')` exactly when it has open inverse image under `q_x`.
Thus the topology does not use a chosen orbit origin. QED.

### Lemma 4.2 (compact Hausdorff orbit)

The standard quotient `R/H` is compact Hausdorff.

#### Proof

The formula

```text
d_H([s],[t])=inf_(k in Z) |s-t-kL|
```

defines a metric on `R/LZ` and induces its quotient topology, so the quotient
is Hausdorff. The quotient map sends the compact interval `[0,L]`
surjectively onto `R/H`; hence `R/H` is compact. QED.

Define a topology on the same underlying set `X` by

```text
U open in Std_coprod(X)
iff U intersect O is open in O for every orbit O.
```

This is precisely the topological coproduct of the standard orbit spaces.
It makes no choice of an origin in any orbit and gives no pre-existing
topology to `Q`.

### Proposition 4.3 (Hausdorffness, open orbits, and joint action)

`Std_coprod(X)` is Hausdorff; every orbit is open (indeed also closed); and
the right action

```text
Std_coprod(X) x R -> Std_coprod(X)
```

is jointly continuous.

#### Proof

Each orbit is an open summand by the coproduct definition. Its complement is
the union of all other open summands, so it is closed. Two points in one
orbit are separated by Lemma 4.2; points in different orbits are separated
by their disjoint open orbit summands. Hence the coproduct is Hausdorff.

The action preserves each orbit. Under `bar(q)_x`, its restriction is

```text
(R/H) x R -> R/H, ([u],t) |-> [u+t],
```

which is continuous. The sets `O x R` form an open cover of
`Std_coprod(X) x R`, and the action is continuous on each of them. It is
therefore jointly continuous globally. QED.

### Proposition 4.4 (uniqueness at the locked lattice domain)

The coproduct topology is the unique Hausdorff topology `tau` on the same
`R`-set for which the action is jointly continuous and every orbit is open.

#### Proof

Fix such a topology and an orbit `O`. Evaluation at `x` makes

```text
q_x:R->(O,tau|_O)
```

continuous. Since it is constant exactly on `H`-cosets, the quotient
property gives a continuous bijection

```text
bar(q)_x:R/H -> (O,tau|_O).
```

Its domain is compact by Lemma 4.2 and its codomain is Hausdorff as a
subspace of `(X,tau)`, so it is a homeomorphism. Thus `tau` restricts to the
standard quotient topology on every orbit.

Because every orbit is `tau`-open, a set `U` is `tau`-open exactly when each
`U intersect O` is open in `O`: the reverse implication follows by taking
the union of those subsets, each open in an open orbit. This is exactly the
coproduct topology. QED.

The proof uses compactness of `R/LZ`. It does not prove the same uniqueness
statement for `H={0}` or any other noncocompact quotient.

### Proposition 4.5 (the one-sided identity topology)

The identity map

```text
id_X:Std_coprod(X)->X_indisc
```

is continuous, while the reverse identity is not.

#### Proof

The only opens of the target `X_indisc` are `emptyset` and `X`, so the first
identity is continuous. Every object is nonempty and each orbit is a copy of
the nontrivial circle `R/LZ`, hence `X` has more than one point. A continuous
map from an indiscrete space to a `T0` space is constant, whereas the reverse
identity into the Hausdorff `Std_coprod(X)` is not. Thus it is not
continuous. QED.

This is a same-set retopologization supplied by the marked action. It is not
the Hausdorff, completely regular, or Kolmogorov reflection of the actual
indiscrete topology; those separated reflections collapse the nonempty
actual space to one point.

## 5. Full faithfulness and the `Indisc` inverse

Define `Std_coprod` on objects by Section 4 and on strict arrows by

```text
Std_coprod(F)=F_0.
```

### Theorem 5.1 (full and faithful equivalence)

The functor

```text
Std_coprod:C_common(H)->Tor_R^coprod(H)
```

is full and faithful. Global indiscretization defines a strict inverse
`Indisc`; hence the disjoint-union functor over all `L>0` is an equivalence,
and under the frozen same-set convention the two composites are identities.

#### Proof

By Proposition 3.1, `F_0` is an equivariant orbit bijection. On an orbit
through `x`,

```text
F_0 o q_x=q_(F_0(x)).
```

The quotient charts therefore make its restriction a homeomorphism to the
target orbit. Since it permutes open coproduct summands, `F_0` and its inverse
are globally continuous. Identities and compositions are inherited from the
unit maps, so `Std_coprod` is a functor.

It is faithful because Proposition 3.1 says a strict arrow is uniquely
determined by `F_0`. It is full because any target equivariant homeomorphism
`phi` is an equivariant bijection of the underlying sets and therefore has
the unique strict lift `F_phi(x,t)=(phi(x),t)` proved after Proposition 3.1.

For a nonempty target object `Y`, define `Indisc(Y)` by retaining the same
set and action, replacing the entire unit topology by one global indiscrete
topology, and forming the marked range-first action groupoid. The action into
the indiscrete target is continuous, all stabilizers remain `H`, and a target
arrow `phi` lifts to `(y,t)|->(phi(y),t)`. Thus `Indisc` is a functor into
`C_common(H)`.

Standardizing `Indisc(Y)` restores on every orbit exactly the topology that
`Y` already has, and the coproduct step restores its global topology. Hence
`Std_coprod Indisc=id`. Starting from a source object, standardizing and then
globally indiscretizing restores the same unit topology, action, groupoid,
mark, and arrow maps, so `Indisc Std_coprod=id`. With abstractly isomorphic
presentations these same identity-set maps give the corresponding natural
isomorphisms. QED.

The inverse indiscretizes the whole carrier. A coproduct of componentwise
indiscrete topologies would be a different, generally non-indiscrete source
and is not used.

## 6. The canonical automorphism extension

Let

```text
A=Aut_R(Std_coprod(X)).
```

By Theorem 5.1, this is also the strict marked automorphism group of
`G_actual` and of `G_std` under the corresponding unit-map identification.
Every `phi in A` permutes the open action orbits. Write

```text
p:A->Sym(Q), p(phi)(q)=phi(O_q).
```

### Theorem 6.1 (canonical exact sequence)

In the ambient ZFC convention there is a canonical exact sequence of
abstract groups

```text
1 -> (R/H)^Q --i--> A --p--> Sym(Q) -> 1,
```

where

```text
i(a)(x)=x dot a(q), x in O_q.
```

The maps and kernel identification are section-free. Surjectivity uses
choice. A choice of one origin in every orbit supplies a noncanonical split.

#### Proof

For `a:Q->R/H`, the displayed formula is independent of the representative
of `a(q)`, is strictly equivariant, and is a homeomorphism on every open
orbit. It is therefore a global equivariant homeomorphism. The assignment is
an injective homomorphism because a rotation is the identity on `O_q`
exactly when its displacement is zero in `R/H`.

If `phi in ker p`, then it preserves every orbit. For any `x in O_q`, there
is a unique `a(q) in R/H` such that `phi(x)=x dot a(q)`. This displacement is
independent of `x`: if `y=x dot u`, equivariance and commutativity give

```text
phi(y)=phi(x) dot u=(x dot a(q)) dot u=y dot a(q).
```

Thus `ker p=image i`, canonically and without an orbit origin.

To prove surjectivity for a given `sigma in Sym(Q)`, use ZFC choice to select
one `x_q in O_q` for every `q`. Define

```text
s_sigma(x_q dot t)=x_(sigma q) dot t.
```

The common stabilizer `H` makes this well-defined; it is an equivariant
homeomorphism between coproduct summands and satisfies `p(s_sigma)=sigma`.
Hence `p` is onto.

If one section `q|->x_q` is fixed once and for all, the same formula for all
`sigma` satisfies

```text
s_sigma s_tau=s_(sigma tau), p s=id.
```

It therefore gives a split and a noncanonical isomorphism

```text
A ~= (R/H)^Q semidirect Sym(Q).
```

Conjugation in these chosen coordinates is

```text
(sigma dot a)(q)=a(sigma^(-1)q).
```

The split depends on the selected origins; neither the section nor the
semidirect coordinates are canonical. The exact maps `i,p` and the abstract
kernel identification are canonical. QED.

No topology or continuous-splitting assertion is made for this sequence.

## 7. The standardized degree-one cohomology

Put

```text
G_std=Std_coprod(X) rtimes R.
```

Use exactly the frozen author-defined globally continuous unnormalized nerve
complex with the trivial real coefficient bundle. Thus a continuous
one-cochain is a continuous map `b:X x R->R`, and the frozen signs give

```text
(d^1 b)(x;t,u)=b(x dot t,u)-b(x,t+u)+b(x,t),
(d^0 h)(x,t)=h(x dot t)-h(x).
```

Consequently the one-cocycle equation is

```text
b(x,t+u)=b(x,t)+b(x dot t,u).                 (7.1)
```

For a cocycle, (7.1) gives `b(x,0)=0`; on the isotropy at a unit it makes
`t|->b(x,t)` a group homomorphism.

### Proposition 7.1 (canonical orbit slope)

For `q in Q` and any `x in O_q`, define

```text
rho([b])(q)=b(x,L)/L.
```

This is independent of the chosen unit and of the cocycle representative,
and it defines a linear map

```text
rho:H_cnv^1(G_std;R)->R^Q.
```

#### Proof

Let `x'=x dot u`. Since `x dot L=x` and addition in `R` is commutative,
applying (7.1) in the two orders gives

```text
b(x,u+L)=b(x,u)+b(x dot u,L),
b(x,L+u)=b(x,L)+b(x dot L,u)=b(x,L)+b(x,u).
```

The left sides agree, so cancellation yields

```text
b(x dot u,L)=b(x,L).
```

Every unit of the orbit has the form `x dot u`, proving basepoint
independence.

If `b'=b+d^0h`, then

```text
(d^0h)(x,L)=h(x dot L)-h(x)=0.
```

Hence the slope is representative-independent. Pointwise addition and real
scalar multiplication make `rho` linear. The positive generator `L` is
unique for the lattice `H=LZ`, so no hidden generator choice remains. QED.

### Proposition 7.2 (surjectivity onto the full product)

For every function `lambda:Q->R`, define

```text
b_lambda(x,t)=lambda([x]) t,
```

where `[x]` denotes the bare orbit containing `x`. Then `b_lambda` is a
globally continuous one-cocycle and

```text
rho([b_lambda])=lambda.
```

#### Proof

On each open set `O_q x R`, the formula is the continuous function
`(x,t)|->lambda(q)t`. These open sets cover `X x R`, so the function is
globally continuous. The action preserves `[x]`; hence

```text
b_lambda(x,t)+b_lambda(x dot t,u)
 =lambda([x])t+lambda([x])u
 =b_lambda(x,t+u),
```

which is (7.1). Finally

```text
b_lambda(x,L)/L=lambda(q).
```

No boundedness, support, finite-orbit, or continuity condition on `lambda`
is needed: the component-index topology created by the coproduct is
discrete. Therefore the target is the full algebraic Cartesian product
`R^Q`, not a direct sum. QED.

### Proposition 7.3 (zero slope is exactly a coboundary)

If a continuous cocycle `b_0` has zero slope on every orbit, then there is a
continuous `h:X->R` satisfying

```text
d^0h=b_0.
```

#### Proof

Use ZFC choice to select one unit `x_q in O_q` for each `q in Q`. Define

```text
h(x_q dot t)=b_0(x_q,t).                     (7.2)
```

First check well-definedness. Zero slope and Proposition 7.1 imply
`b_0(y,L)=0` for every unit `y`. Restriction to the isotropy group then gives

```text
b_0(y,kL)=0 for every k in Z.
```

If `x_q dot t=x_q dot(t+kL)`, equation (7.1) gives

```text
b_0(x_q,t+kL)
 =b_0(x_q,t)+b_0(x_q dot t,kL)
 =b_0(x_q,t).
```

Thus (7.2) is independent of the representing time.

The pullback of `h|_(O_q)` along the quotient map `q_(x_q)` is the
continuous function `t|->b_0(x_q,t)`. Since it is constant on `H`-cosets,
the quotient property makes `h|_(O_q)` continuous. The orbit components are
open and carry the coproduct topology, so the componentwise functions glue
to a globally continuous `h`.

For `y=x_q dot t`, equation (7.1) now gives

```text
(d^0h)(y,u)
 =h(x_q dot(t+u))-h(x_q dot t)
 =b_0(x_q,t+u)-b_0(x_q,t)
 =b_0(x_q dot t,u)
 =b_0(y,u).
```

The sign is exactly the frozen `h(s)-h(r)` sign. QED.

The orbit section in this proof is an existence device for a potential; it
is not part of `rho`, the standardization topology, or the canonical inverse

```text
R^Q -> H_cnv^1(G_std;R), lambda |-> [b_lambda].
```

### Theorem 7.4 (standardized `H^1`)

The slope map is a canonical algebraic isomorphism

```text
rho:H_cnv^1(G_std;R) ~= R^Q.
```

#### Proof

Surjectivity is Proposition 7.2. For injectivity, if `rho([b])=0`,
Proposition 7.3 gives `b=d^0h`, so `[b]=0`. More explicitly, for an arbitrary
`b`, set `lambda=rho([b])`. Then `b-b_lambda` has zero slope and is a
coboundary, so `[b]=[b_lambda]`. QED.

### Proposition 7.5 (standardized coboundaries are genuinely nonzero)

In general

```text
B_cnv^1(G_std;R) != {0},
Z_cnv^1(G_std;R) != {b_lambda:lambda in R^Q}.
```

#### Proof

Choose one orbit `O_(q_0)` and one origin `x_0` in it. Define a continuous
unit cochain by

```text
h(x_0 dot t)=sin(2 pi t/L) on O_(q_0),
h=0 on every other orbit.
```

It is well-defined modulo `LZ` and continuous by the coproduct topology. At
the arrow `(x_0,L/4)`,

```text
(d^0h)(x_0,L/4)=1,
```

so the coboundary is nonzero. The already proved identity `d^1d^0=0` makes
it a one-cocycle. Its slope is zero on every orbit, whereas a pure
`b_lambda` with zero slopes is the zero cochain. Therefore this nonzero
coboundary is also a cocycle that is not literally one of the orbitwise
time-only representatives. QED.

This is why Theorem 7.4 identifies cohomology classes, not the full
standardized cocycle space.

## 8. The actual-to-standard comparison and strict invariants

Let

```text
G_actual=X_indisc rtimes R.
```

The identity on units and arrows defines

```text
J:G_std->G_actual.
```

### Proposition 8.1 (continuity and variance)

`J` is a continuous strict marked functor, but its reverse is not continuous.
It induces the contravariant map

```text
J^*:H_cnv^1(G_actual;R)->H_cnv^1(G_std;R).
```

#### Proof

The unit map is the continuous finer-to-indiscrete identity from Proposition
4.5. An arrow open in `G_actual` is `X x U` with `U` open in `R`; its inverse
image is the same open set in `G_std`. Hence the arrow map is continuous.
All algebraic groupoid operations and `c(x,t)=t` are unchanged, so it is a
strict marked functor. The reverse unit identity is not continuous by
Proposition 4.5. Pullback of continuous nerve cochains commutes with the
faces and therefore has the displayed contravariant direction. QED.

The v2 actual theorem applies to every nonempty globally indiscrete action,
without transitivity. It gives

```text
H_cnv^1(G_actual;R)=R[c],
B_cnv^1(G_actual;R)={0}.
```

### Proposition 8.2 (constant diagonal)

Under `rho`, the comparison map is

```text
rho(J^*(lambda[c]))=(q |-> lambda).
```

It is injective and its image is the constant diagonal in `R^Q`.

#### Proof

The pulled-back representative is still `(x,t)|->lambda t`. For every
orbit,

```text
rho(J^*(lambda[c]))(q)=lambda L/L=lambda.
```

Because `Q` is nonempty, a constant function is zero exactly when its value
is zero, so the diagonal map is injective. QED.

### Proposition 8.3 (raw pullback and the induced left action)

For `phi in Aut_R(G_std)`, let `sigma_phi in Sym(Q)` be its orbit
permutation. Raw cohomological pullback satisfies

```text
rho(phi^*[b])(q)=rho([b])(sigma_phi(q)).       (8.1)
```

If the automorphism group is made to act on the left by

```text
phi dot [b]=(phi^(-1))^*[b],
```

then the corresponding action on `R^Q` is

```text
(phi dot lambda)(q)=lambda(sigma_phi^(-1)(q)). (8.2)
```

#### Proof

The strict groupoid automorphism has formula `(x,t)|->(phi(x),t)`. Thus

```text
rho(phi^*[b])(q)
 =b(phi(x),L)/L
 =rho([b])(sigma_phi(q)),
```

which proves (8.1). Substituting `phi^(-1)` proves (8.2). QED.

Equation (8.2) has the same inverse-index convention as the semidirect
coordinate action in Theorem 6.1, but they are distinct constructions: one
is the induced left action on cohomology, the other is conjugation on the
rotation kernel. Raw pullback itself is (8.1), not (8.2).

### Theorem 8.4 (strict-automorphism invariant diagonal)

For the left action above,

```text
(R^Q)^(Aut_R(G_std))={constant functions Q->R}.
```

Consequently

```text
image(J^*)=(R^Q)^(Aut_R(G_std)).
```

#### Proof

Kernel rotations have `sigma_phi=id`, so they act trivially on slopes.
Theorem 6.1 says every permutation of `Q` occurs. A function invariant under
all of `Sym(Q)` has equal values at every pair `q,r`: when `q!=r`, apply the
transposition exchanging them; the singleton case is immediate. Conversely,
constant functions are fixed by all permutations. Proposition 8.2 identifies
this subspace with `image(J^*)`. QED.

Here `Aut_R(G_std)` means strict time-preserving equivariant automorphisms,
equivalently strict marked groupoid automorphisms via Theorem 5.1. Scaled,
unmarked, orientation-reversing, and arbitrary abstract groupoid
automorphisms are not part of the invariant theorem.

## 9. Same-object fixed-prime packet application

Fix a rational prime `p`. The accepted source/owner chain states, on the
same packet owner:

1. Deninger supplies the fixed-prime right flow, the normalized logarithmic
   clock, and multiplicative stabilizer `p^Z` at every packet point;
2. logarithmic time converts this to the common additive stabilizer
   `H=(log p)Z` at every unit;
3. Paper 9 supplies the same packet set `Gamma_p` with one global actual
   indiscrete topology and its orbit quotient; and
4. Papers 11--12 supply the range-first transformation groupoid and the
   author complex.

Therefore

```text
G_p^actual=Gamma_p^actual rtimes R
```

is an object of `C_common((log p)Z)`. It need not, and in the Paper-9 owner
does not, become transitive.

### Corollary 9.1 (packet standardization and cohomology comparison)

Let `Q_p^set=Gamma_p/R` be only the underlying orbit set. Give every orbit
its standard `R/(log p)Z` topology and take their coproduct on the same
packet set. Then

```text
G_p^std=Gamma_p^std rtimes R,
J_p:G_p^std->G_p^actual,
H_cnv^1(G_p^actual;R)=R[c],
H_cnv^1(G_p^std;R)=R^(Q_p^set),
rho_p(image(J_p^*))={constant functions on Q_p^set}
                    =(R^(Q_p^set))^(Aut_R(G_p^std)).
```

The canonical automorphism extension is

```text
1 -> (R/(log p)Z)^(Q_p^set)
  -> Aut_R(G_p^std)
  -> Sym(Q_p^set)
  -> 1.
```

#### Proof

The every-unit common-stabilizer statement places the packet in the exact
domain of Theorems 5.1, 6.1, 7.4, and 8.4. Substituting
`H=(log p)Z` gives every formula. QED.

The application keeps four records distinct:

| Record | Exact type/topology | What is not inferred |
|---|---|---|
| `Gamma_p_actual` | the packet unit set with one global indiscrete topology | no standard circle topology on the actual packet |
| `Gamma_p_std` | the same set, topological coproduct of open standard circles | not inherited, not a separated reflection |
| `Q_p_actual` | Paper-9 orbit quotient with its actual indiscrete quotient topology | no discreteness, enumeration, measure, or local triviality |
| `Q_p_disc` | the same bare orbit set as the discrete component index of `Gamma_p_std` | not the topology of `Q_p_actual` |

The last topology is discrete because the inverse image of every subset of
the component set is a union of open standardized orbits. No cardinality or
arithmetic selection statement follows.

## 10. Theorem, owner, source, and Route ceilings

### 10.1 Exact theorem ceiling

The proved theorem requires a nonempty action with one common cocompact
lattice `H=LZ`, `L>0`. It does not cover mixed stabilizers, the free owner
`H={0}`, the trivial owner `H=R`, the dense owner `H=Q`, or a noncocompact
closed subgroup in the topology-uniqueness step. It computes standardized
degree one only. It proves no higher standardized cohomology, normalized
subcomplex comparison, Morita invariance, cohomology topology, Haar measure,
function algebra, trace, completion, determinant, or operator statement.

### 10.2 Owner and source-credit matrix

| Claim | Exact owner | Permitted source role | Forbidden promotion |
|---|---|---|---|
| quotient circle and topological coproduct | Paper-12 construction on a common-`H` action | standard `R/H` and Stacks coproduct background | no source theorem for the full same-set comparison |
| strict lift/descent | Paper-12 direct Proposition 3.1 and Theorem 5.1 | Gepner--Meier Proposition 2.15 is the closest over-`BG` mechanism | its compactly generated weak-Hausdorff theorem is not imported to the actual non-weak-Hausdorff owner |
| orbit rotations and permutations | Paper-12 direct Theorem 6.1 for arbitrary nonempty `Q` | Guillou--May and Alp--Wensley are finite nearest precedents | no finite-to-arbitrary transfer and no canonical wreath split |
| standardized `H_cnv^1=R^Q` | Paper-12 author complex and Theorem 7.4 | Mackenzie is a different-theory transitive comparator only | no identification with rigid cohomology or a named standard theory |
| diagonal/invariant theorem | Paper-12 same-set topology comparison | no direct exact-package precedent was found within the bounded audit | no firstness or global novelty claim |
| packet action, clock, and common stabilizer | Deninger at the frozen exact locators | exact same-object source input | no “Deninger groupoid/cohomology” wording |
| actual packet and `Q_p_actual` topology | Paper 9 | exact inherited owner | no transfer of the constructed discrete component topology |
| range-first groupoid and actual arrow factorization | Papers 11--12 | exact dependency only | no v4 standardization or `R^Q` credit to Paper 11 |

The novelty statement remains only

```text
SUPPORTED_WITHIN_SEARCH through 2026-08-15;
DIRECT_EXACT_PACKAGE_PRECEDENT_FOUND=false.
```

This proof does not strengthen it to “first,” “novel,” “unprecedented,” or a
global absence claim.

### 10.3 Route ceiling

This proof creates no Route YAML and makes no A-coordinate decision. The
generic construction remains action-blind and accepts arbitrary periods.
The owner

```text
DEN-EF-STANDARDIZED-PACKET-H1-DIAGONAL-P
```

records only the derived pair `(G_p^std,G_p^actual,J_p)`, the bare orbit set,
and the copied common source lattice. It receives no topology or count for
`Q_p`, no actual-topology transport, no arithmetic selectivity, no primitive
orbit amplitude, trace, completion, determinant, or analytic continuation.
The one-orbit `DEN-EF-STANDARD-PERIOD-QUOTIENT-P` remains a separate proxy.
All frozen A2/A3/A4 failures or `NOT_TESTABLE` ceilings remain, the evaluator
still owns A0/A1, and `Route_B_invocation=false` remains binding.

## 11. Falsifier audit

| Frozen attack | Direct proof response | Result |
|---|---|---|
| basepoint changes the orbit topology | `q_(x dot u)=q_x o T_u` | impossible under the theorem |
| the coproduct is non-Hausdorff or the action discontinuous | compact Hausdorff orbit charts plus the open-component cover | impossible under the theorem |
| a second Hausdorff action topology with open orbits exists | compact-to-Hausdorff rigidity on each orbit, then coproduct gluing | impossible at `H=LZ`; no noncocompact claim |
| a strict arrow distorts time or is lost by standardization | strict mark fixes `t`; equivariance gives quotient homeomorphisms and unique lifts | impossible |
| `Indisc` only indiscretizes components | the inverse uses one global indiscrete topology | excluded by definition and proof |
| the automorphism kernel is a direct sum | rotations may be chosen independently on every orbit | refuted; the kernel is the full product |
| the wreath split is canonical | its construction explicitly chooses every orbit origin | refuted; only the exact sequence is canonical |
| standardized `B^1` vanishes | the sine potential has a nonzero coboundary | refuted |
| every standardized cocycle is literally time-only | the same nonzero zero-slope coboundary is a counterexample | refuted; only class representatives reduce |
| `J` or `J^*` has the reverse direction | topology gives `G_std->G_actual`; cochains pull actual-to-standard | refuted |
| raw pullback uses the inverse permutation | equation (8.1) gives `lambda o sigma`; only the induced left action uses `sigma^(-1)` | refuted |
| strict invariants contain nonconstant slopes | all orbit permutations occur in ZFC | impossible for nonempty `Q` |
| mixed stabilizers enter `C_common` | Proposition 3.1 preserves stabilizers and the object lock requires one `H` | excluded; `NONTRANS-1-2` remains a generic-v2 control |
| the packet theorem transports the actual `Q_p` topology | the four-way typing table separates both packet and both quotient records | excluded |
| the theorem selects primes or arithmetic clocks | no proof step uses primality; only Corollary 9.1 imports the source lattice | `PROVES_TOO_MUCH` for arithmetic specificity |

Finite controls remain required as deterministic witnesses and tamper checks,
but none is used here as proof of a universal statement.

## 12. Prior standalone Major: proof contribution versus disposition

The v2 standalone Major identified a precise deficiency: the proved centre
was Paper-11 factorization plus routine bar/Cauchy formalism and a
nonfaithful pointed quotient shadow. The disposition gate required a
basepoint-independent standardization retaining strict translations, and the
later v4 gate strengthened the flip point to the same-carrier comparison

```text
R ~= H_cnv^1(G_actual;R)
  --J^*--> H_cnv^1(G_std;R) ~= R^Q
```

with image characterized intrinsically by all strict symmetries.

Sections 4--8 prove exactly that requested repair: the standardization is
section-free; `Std_coprod` is full and faithful with inverse `Indisc`; strict
translations survive in the canonical automorphism extension; and the new
cohomology directions not descending from the actual topology are separated
from the descending classes by the intrinsic invariant diagonal.

The proof-side contribution needed to close the old `M1` is therefore
complete. This sentence is not an adjudicative closure. The v4 final gate
expressly reserves the semantic question -- whether the proved conjunction
has sufficient nonroutine standalone weight -- for a fresh independent
post-proof reviewer. Until that reviewer closes it,

```text
PRIOR_STANDALONE_M1_PROOF_REPAIR=PROVED
PRIOR_STANDALONE_M1_DISPOSITION=PENDING_INDEPENDENT_REVIEW
STANDALONE_PASS=false
NOTE_OR_MERGE remains the fail-closed fallback.
```

## 13. Integrated theorem matrix and lane verdict

| Required v4 component | Direct result | Choice/canonicity boundary | Status |
|---|---|---|---|
| `C_common(H)` and disjoint union | strict maps preserve literal time and stabilizer | no choice | `PROVED` |
| section-free orbit topology | basepoint-independent quotient charts | no orbit section | `PROVED` |
| Hausdorff/action/open-orbit uniqueness | compact `R/LZ` plus open coproduct | cocompact lattice only | `PROVED` |
| `Std_coprod`/`Indisc` | full, faithful, concrete strict inverse | nonempty target only | `PROVED` |
| automorphism extension | canonical kernel and quotient maps | surjectivity uses ZFC; split needs chosen origins and is noncanonical | `PROVED` |
| standardized `H^1` | canonical slope isomorphism to full `R^Q` | zero-slope potential proof uses an orbit section | `PROVED` |
| standardized `B^1` boundary | explicit nonzero coboundary | existence witness only | `PROVED` |
| `J` and diagonal | continuous finer-to-actual identity; injective constant diagonal | `Q` nonempty | `PROVED` |
| strict invariants | raw pullback and induced left action separated exactly | all `Sym(Q)` lifts use ZFC | `PROVED` |
| fixed-prime packet | same-object common-`(log p)Z` application and four-way topology typing | source-owned stabilizer; no `Q_p` count/topology transfer | `PROVED` |
| source/novelty wording | nearest precedents retained at exact ceilings | `SUPPORTED_WITHIN_SEARCH` only | `PRESERVED` |
| deterministic controls | outside this proof lane | 3252-row/11-CSV/3486-row freeze unchanged | `PENDING SEPARATE LANE` |
| standalone/Route/manuscript/release | outside this proof lane | independent gates mandatory | `NOT AUTHORIZED` |

Finding register:

| Severity | Count | Open proof item |
|---|---:|---|
| Critical (`C`) | 0 | none |
| Major (`M`) | 0 | none |
| Minor (`m`) | 0 | none |

```text
V4_ORBITWISE_STANDARDIZATION=PROVED
STD_COPROD_INDISC_EQUIVALENCE=PROVED_FULL_FAITHFUL
AUT_CANONICAL_EXACT_SEQUENCE=PROVED
AUT_SPLIT_CANONICAL=false
H1_STD=R^Q_PROVED
STANDARDIZED_B1_ZERO=false
J_DIRECTION=G_STD_TO_G_ACTUAL
RAW_PULLBACK_SLOPE=lambda_o_sigma
LEFT_ACTION_SLOPE=lambda_o_sigma_inverse
J_PULLBACK_IMAGE=CONSTANT_DIAGONAL
STRICT_AUT_INVARIANTS=CONSTANT_DIAGONAL
PACKET_SAME_OBJECT_APPLICATION=PROVED
Q_P_FOUR_WAY_TYPING=EXACT
CRITICAL_OPEN=0
MAJOR_OPEN=0
MINOR_OPEN=0
PROOF_LANE_VERDICT=PASS
STANDALONE_DISPOSITION=PENDING_INDEPENDENT_REVIEW
ROUTE_MANUSCRIPT_RELEASE_AUTHORIZED=false
```

## 14. Mechanical integrity closeout

After the final proof bytes were written, every active, gate, stable-proof,
review, and inherited-owner input listed in Section 1 was rehashed. All
digests matched the pre-proof receipt. No input drift was observed, and no
file other than
`notes/phase3_orbitwise_standardization_h1_proofs.md` was written by this
lane.

The detached SHA-256 of this report is computed after its final byte is
written and is supplied to the integrating lane; it is not embedded here,
because embedding it would change the hashed bytes.

**Final proof-lane verdict: PASS (`C0/M0/m0`).** The exact v4 mathematical
package is proved. Controls, independent proof/source-boundary/standalone
review, Route, composition, manuscript, and release retain their separate
gates.
