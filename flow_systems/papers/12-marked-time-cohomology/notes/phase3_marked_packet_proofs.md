# Paper 12 Phase-3 marked-packet, category, and quotient proofs

Proof date: **2026-08-15 (Asia/Shanghai)**  
Authorized lane: **`P12-6`--`P12-8` only**  
Lane verdict: **PASS — C0/M0/m0**  
Standalone disposition: **ELIGIBLE/PENDING integrated independent review; not released**

## 1. Scope, authority, and exact-byte receipt

This report proves only the fixed-orbit and fixed-prime packet
specialization, the strict/positive-scaled/unmarked category boundary, and
the normalized pointed standard-quotient functor. It does not adjudicate
`P12-1`--`P12-5`, execute `P12-9`, serialize a Route record, draft a
manuscript, or authorize release.

The ARS academic-pipeline, argument-building, reviewer, integrity, and source
verification instructions were applied as proof-discipline constraints:
every imported statement is kept at its exact owner and source strength,
negative controls are not promoted to universal proofs, and a lane proof is
not presented as a final standalone decision.

The following inputs were independently rehashed before proof construction.

| Frozen input | SHA-256 |
|---|---|
| `notes/phase2_final_gate.md` | `1b05110e23f23848442742b415811205ef24616413b59989996993d4297be9ab` |
| `notes/phase2_status_relock.md` | `c6fb9d3a04171bc68ed6239e1a91cee8f9987cd75d8516967d3ded5de6b89eea` |
| current `notes/pipeline_state.md` | `24c226e35d69c6aab68df19d495957469ec761551680696b20cff865604fe62d` |
| `notes/research_protocol.md` | `9213d6e27505c09dbfc24899a15dcca9670e897e754fe40efbc9c1ae7248f434` |
| `notes/candidate_lock.md` | `f0878aaf97e44041460b05c59acd5b5a45fd6d1bef2d7042e3ad273de5320d1c` |
| `notes/phase1_design_amendment.md` | `76684044f434c8084712e558c32ee47e996a84763a3eca405f7014ab3d77f949` |
| `notes/phase1_design_amendment_v2.md` | `26222c9e6888f0aa45d019a9f1fd74038285ac460ae6aa0342b8b4e01b4c3285` |
| `notes/phase1_final_gate.md` | `fc327245bf5653b18f21f782f4783a2ad0b606340c5f5e7da6516d0514cac72c` |
| `notes/phase1_status_relock.md` | `a7a9875c810ea98f5a5563c8f243612b006c20f397aaa8ebae533d8b8c6c61d6` |
| `notes/phase2_framework_source_audit.md` | `32560640ce95894f3b60191593ce55cbcc50a3dd4ce713b148d96cd96bcdfdcb` |
| `notes/phase2_category_owner_audit.md` | `8fad79f121439145e0ac3cac7ca67e82f3e2ad6af86da5b0f001e92da30e1d62` |
| `notes/phase2_novelty_search.md` | `c4584862824dbaadec9945fb85defd6d11ee7822849471b075ff4d90d57ca1bd` |
| `notes/phase2_final_review.md` | `032d558fecdccc492ce59733e20dd9322f573d033355aee3c74563680cea2ea7` |
| `notes/sources/coh-source-manifest.md` | `77adde8e38853b4623212eaf60aee68f5c0d76112d859c643c061fb5b2fddb22` |
| Paper 9 `notes/source_audit.md` | `20fecdf360d18f9accf3e3ec8467f3beb369a8737761eb6219fef71e9773ac20` |
| Paper 9 `notes/proof_audit.md` | `c38c24296e5519862eb671dba1644c8005788ac15dffcac48dfdaa1ac3afdde8` |
| Paper 10 `notes/proof_audit.md` | `efda522ead9efebfc3f59f0688f2dfd3fe63f63ff4efd4377068485d1a4acc3a` |
| Paper 11 `notes/proof_audit.md` | `03f17606b0c9d69b496d2766c0a404b0d090698101150a800de4c2108ddc6b28` |
| Paper 11 `notes/composition_blueprint.md` | `4b6bfa27c83f72858ac5f0d03c0b9964f93e914fc1d4fdfced619327bcdfc30b` |

The Deninger source was also read directly at the preflight-cleared local
manifestation `1807.06400v4`, PDF SHA-256
`edd0bc8c2efb601ed7574e8eceae40e8cde21d0e4b2bc8c4ce7e60d8e1f82a09`.
Its sidecar has SHA-256
`84e43728af040d539a46fbbb95ff8cd34f46c75c0245130ef79c2978ccc3806d`
and reports `PASS`, `119=119=119` pages, and no warnings. The load-bearing
locators are physical/printed p. 38, Section 6, and p. 39, Theorem 6.1.

No source PDF, lock, code file, result, Route record, or sibling proof report
is modified by this lane.

## 2. Frozen notation and a local descent lemma

Let `X` be a nonempty indiscrete right `R`-space and let

```text
G=X rtimes R,
r(x,t)=x,
s(x,t)=x dot t,
(x,t)(x dot t,u)=(x,t+u).
```

Write

```text
H_x=Stab_R(x)={t in R:x dot t=x},
G_x^x={(x,t):t in H_x},
c(x,t)=t.
```

The next elementary calculation is included only to make the uses of
`Per_x([c])` in `P12-6`--`P12-8` self-contained. It is not a separate verdict
on the full generic `P12-5` package.

### Lemma 2.1 — the normalized coordinate class has isotropy image `H_x`

The coordinate cochain `c` is a continuous real 1-cocycle. Its restriction
to `G_x^x` is the continuous homomorphism

```text
(x,t) |-> t,
```

and therefore

```text
image(res_x(c))=H_x.
```

Moreover, for any continuous degree-zero cochain `h`, the frozen differential
is

```text
(d^0 h)(x,t)=h(x dot t)-h(x).
```

If `(x,t)` is isotropy, the two arguments agree, so
`(d^0h)(x,t)=0`. Consequently `c` and `c+d^0h` have the same isotropy image,
and the notation

```text
Per_x([c])=H_x
```

is representative-independent.

**Proof.** For composable arrows `(x,t)` and `(x dot t,u)`,

```text
(d^1c)((x,t),(x dot t,u))
  =c(x dot t,u)-c(x,t+u)+c(x,t)
  =u-(t+u)+t=0.
```

Continuity follows from time projection. On isotropy, restriction is the
identity inclusion of the subgroup `H_x` into `R`, and the coboundary
calculation above proves descent. QED.

Two limits are already visible. First, the generic coordinate cocycle does
not by itself carry an arithmetic normalization. Second, the unmarked
groupoid does not select `c`: Sections 4.4 and 4.5 exhibit unmarked
isomorphisms that rescale or reverse it.

## 3. `P12-6`: fixed-orbit and fixed-prime packet recovery

### 3.1 Exact same-object source chain

Fix a rational prime `p`. Deninger physical/printed p. 38 defines the
suspension and right multiplicative flow by

```text
[P,u] dot v=[P,uv],
phi^t([P,u])=[P,u e^t].
```

The same page defines the fixed-point packet `Gamma_(x_0)`, and the paragraph
there states `Gamma^E_(x_0)=Gamma_(x_0)` when `E_f` is contained in `E`.
For the exact Paper-9 owner one takes `E=E_f`. Deninger physical/printed
p. 39, Theorem 6.1, states that every point of that packet has multiplicative
isotropy `N(x_0)^Z`. For `X_0=Spec Z` and `x_0=(p)`, this is `p^Z` at every
packet point.

The additive time action used here is the same flow under `t |-> e^t`.
Hence, at every `x in Gamma_p`,

```text
H_x={t in R:e^t in p^Z}
   ={k log p:k in Z}
   =(log p)Z.
```

This is not a topology transport through Deninger's circle bijection.
Paper 9 separately owns the actual inherited indiscrete topology of
`Gamma_p` and of every inherited orbit. Papers 11--12 separately own the
range-first transformation-groupoid construction.

### Theorem 3.1 — actual fixed-orbit marked-period recovery

For every rational prime `p`, every normalized Paper-9 orbit label `a`, and
every unit `x` of the actual fixed orbit

```text
G_(p,a)^orb=X_(p,a) rtimes R,
```

the Deninger-source-normalized coordinate class satisfies

```text
Per_x([c])=(log p)Z.
```

**Proof.** Every unit of the orbit lies in the exact fixed-prime packet.
The source chain in Section 3.1 gives
`H_x=(log p)Z`. Lemma 2.1 gives
`Per_x([c])=H_x`. QED.

This recovers the source stabilizer as the image of a marked cohomology
class. It is not a new derivation of Deninger's stabilizer and not a
normalization selected by the abstract one-dimensional cohomology space.

### Corollary 3.2 — `PACKET_COROLLARY`

For every rational prime `p`, on the exact actual fixed-prime packet

```text
G_p^pkt=Gamma_p rtimes R,
```

with the restricted Deninger right flow and the same source-normalized
coordinate `c(x,t)=t`, one has

```text
Per_x([c])=(log p)Z     for every x in Gamma_p.
```

**Proof.** Theorem 6.1 supplies the common multiplicative stabilizer `p^Z`
at every packet point, not merely at one orbit representative. The logarithmic
coordinate converts it to `(log p)Z` at every unit. Lemma 2.1 identifies
that subgroup with the isotropy image of `[c]`. QED.

Thus this lane returns

```text
packet_result: PACKET_COROLLARY
orbit_only: false
owner: exact fixed-prime G_p^pkt only
```

There is no conclusion on `G^global`, a cross-prime union, or the full
Deninger suspension.

## 4. `P12-7`: categories, covariance, and exact non-descent

### 4.1 Objects and category laws

The three categories have the common object class of pairs `(G,c)` where

```text
G=X rtimes R,
X is nonempty and indiscrete,
the right R-action is transitive,
c(x,t)=t,
H=Stab_R(x)=LZ for one L>0.
```

Because the acting group is abelian and the action is transitive, `H` does
not depend on `x`: if `y=x dot u`, then

```text
y dot t=y
iff x dot (u+t)=x dot u
iff x dot t=x.
```

The morphisms are exactly those frozen in the protocol:

| Category | Morphism | Identity | Composition | Inverse law |
|---|---|---|---|---|
| `C_str` | a topological-groupoid isomorphism `F` with `c' o F=c` | `id` | ordinary composition | `c o F^(-1)=c'` |
| `C_scale` | `(F,alpha)`, `alpha>0`, with `c' o F=alpha c` | `(id,1)` | `(F',alpha') o (F,alpha)=(F'oF,alpha'alpha)` | `(F^(-1),alpha^(-1))` |
| `C_un` | an underlying topological-groupoid isomorphism, with no equation involving `c` | `id` | ordinary composition | ordinary inverse |

These rules define categories. The only nonformal marking check is

```text
c'' o F' o F=alpha'(c' o F)=alpha'alpha c,
```

and solving `c' o F=alpha c` for the inverse gives

```text
c o F^(-1)=alpha^(-1)c'.
```

Thus `C_str` is precisely the `alpha=1` subcategory of `C_scale`, and both
forget to `C_un`.

### Theorem 4.1 — exact positive covariance

Let `(F,alpha):(G,c)->(G',c')` be a morphism in `C_scale`. For every unit
`x`,

```text
Per_(F_0(x))([c'])=alpha Per_x([c]).
```

In particular a strict morphism preserves the subgroup exactly.

**Proof.** A groupoid isomorphism maps `G_x^x` bijectively onto
`G'_(F_0(x))^(F_0(x))`. Therefore

```text
c'(G'_(F_0(x))^(F_0(x)))
 =c'(F(G_x^x))
 =alpha c(G_x^x).
```

By Lemma 2.1, the left and right images are respectively
`Per_(F_0(x))([c'])` and `Per_x([c])`. The inverse morphism gives the reverse
inclusion with scale `alpha^(-1)`, so the displayed relation is equality,
not merely inclusion. QED.

Equivalently, writing `H_x` and `H'_(F_0(x))` for the stabilizers,

```text
H'_(F_0(x))=alpha H_x.
```

The direction is forced by the equation `c' o F=alpha c`; it is not
`alpha^(-1)H_x`.

### 4.2 Explicit unequal-period scaled isomorphisms

For `L,M>0`, put

```text
X_L=R/LZ       as a set with the indiscrete topology,
[r]_L dot t=[r+t]_L,
G_L=X_L rtimes R,
alpha=M/L.
```

Define

```text
F_alpha([r]_L,t)=([alpha r]_M,alpha t),
(F_alpha)_0([r]_L)=[alpha r]_M.
```

### Theorem 4.2 — the dilation isomorphism

`F_alpha:G_L->G_M` is a topological-groupoid isomorphism and

```text
c_M o F_alpha=alpha c_L.
```

Its inverse is

```text
F_alpha^(-1)([s]_M,u)=([alpha^(-1)s]_L,alpha^(-1)u).
```

**Proof.** If `r'=r+kL`, then

```text
alpha r'=alpha r+k alpha L=alpha r+kM,
```

so the unit formula is well-defined. The inverse formula is well-defined by
the same calculation and proves bijectivity.

Every arrow open in `G_L` has the form `X_L x U`; its inverse image under
`F_alpha` is `X_L x alpha^(-1)U`. Thus `F_alpha` is continuous, and the same
argument with `alpha^(-1)` proves inverse continuity. The unit maps are
homeomorphisms as well (indeed every set map between indiscrete spaces is
continuous).

Range and source are preserved because

```text
r_M(F_alpha([r],t))=[alpha r]
                   =(F_alpha)_0(r_L([r],t)),

s_M(F_alpha([r],t))=[alpha r+alpha t]
                   =[alpha(r+t)]
                   =(F_alpha)_0(s_L([r],t)).
```

For a composable pair `([r],t),([r+t],u)`, the images are composable and

```text
F_alpha(([r],t)([r+t],u))
  =F_alpha([r],t+u)
  =([alpha r],alpha(t+u))
  =F_alpha([r],t)F_alpha([r+t],u).
```

Also

```text
F_alpha(([r],t)^(-1))
 =F_alpha([r+t],-t)
 =([alpha r+alpha t],-alpha t)
 =F_alpha([r],t)^(-1).
```

Finally `c_M(F_alpha([r],t))=alpha t`. QED.

The stabilizers are `LZ` and `MZ=alpha LZ`, exactly as Theorem 4.1 requires.
If `L!=M`, this is an isomorphism in `C_scale` and, after forgetting the
mark, in `C_un`, between objects with unequal positive period generators.
Hence the unscaled subgroup and its generator do not descend as invariants
of either weaker category.

There is no strict marked isomorphism between `G_L` and `G_M` when `L!=M`.
Indeed Theorem 4.1 with `alpha=1` would give `LZ=MZ`; equality of these
rank-one lattices forces equality of their least positive elements, hence
`L=M`.

### 4.3 Orientation reversal and failure of the converse

For `L>0`, define

```text
F_-([r]_L,t)=([-r]_L,-t).
```

The same range, source, product, inverse, and product-topology calculations
as above, now with scalar `-1`, show that `F_-` is an involutive underlying
topological-groupoid automorphism. It satisfies

```text
c_L o F_-=-c_L,
```

so it is not strict and, because `C_scale` permits only positive scales, it
is not a `C_scale` morphism. It is a `C_un` morphism. Nevertheless

```text
(-1)LZ=LZ.
```

Therefore exact equality of period subgroups does not imply strictness. This
is a counterexample to the converse only; it does not weaken the strict
implication in Theorem 4.1.

### 4.4 Arbitrary-period family and boundary controls

The category theorem deliberately assumes a positive rank-one lattice. The
generic marked construction accepts much more.

For any additive subgroup `H<=R`, let

```text
X_H=R/H as a set with the indiscrete topology,
[r]_H dot t=[r+t]_H,
G_H=X_H rtimes R.
```

This action is continuous and transitive, its stabilizer at every unit is
exactly `H`, and Lemma 2.1 gives

```text
Per_x([c])=H.
```

Thus the construction realizes arbitrary subgroups before any arithmetic
specialization. If `alpha>0` and `K=alpha H`, the formula

```text
([r]_H,t) |-> ([alpha r]_K,alpha t)
```

is proved exactly as in Theorem 4.2 and has covariance `K=alpha H`.

The preregistered boundary controls are theorem-level instances of this
observation or direct variants:

| Control | Exact calculation | Boundary established |
|---|---|---|
| `TRIV-2` | on the two-point indiscrete space with trivial action, `H_x=R` and `Per_x([c])=R` at both units | there is no least positive period; the action is not transitive |
| `FREE-R` | on indiscrete `R` with translation, `H_x={0}` and `Per_x([c])={0}` | transitivity does not imply a nonzero period |
| `PER-L` | for each `L in {log 2,log 4,sqrt(2),37/29}`, `H_x=LZ` | the same theorem accepts prime, composite, nonarithmetic, and neutral constants |
| `DENSE-Q` | on indiscrete `R/Q`, `H_x=Q` and `Per_x([c])=Q` | the marked image need not be closed, discrete, or a lattice |
| `NONTRANS-1-2` | on `(R/Z) disjoint-union (R/2Z)` with one indiscrete topology, the two invariant orbits have stabilizers `Z` and `2Z` | without transitivity the subgroup can depend on the unit/orbit |
| `LABEL-SWAP` | permuting the four external labels attached to the fixed `PER-L` carriers changes no action, stabilizer, period calculation, or category proof | labels do not create arithmetic selectivity |

For the dense control, every positive rational `q` satisfies `qQ=Q`. The
map

```text
([r]_Q,t) |-> ([qr]_Q,qt)
```

is therefore a non-strict positive-scaled automorphism for `q!=1`, yet the
period subgroup remains exactly `Q`. This supplies a direct counterexample
to any universal statement that every nontrivial positive rescaling changes
the subgroup once the lattice-object restriction is removed.

The control table proves scope sharpness. It does not prove arithmetic
specificity and does not create a Route coordinate.

## 5. `P12-8`: normalized pointed standard quotient

### 5.1 The target category

Let `Hom_(R,0)^std` have objects

```text
(R/H,[0]),     H=LZ, L>0,
```

with the usual Hausdorff quotient topology and right translation, and let
its morphisms be basepoint-preserving, continuous, strictly
`R`-equivariant homeomorphisms.

### Lemma 5.1 — target morphisms are rigid

A morphism

```text
phi:(R/H,[0])->(R/H',[0])
```

exists if and only if `H=H'`. When it exists it is uniquely

```text
phi([t]_H)=[t]_(H').
```

**Proof.** Strict equivariance and basepoint preservation force

```text
phi([t]_H)=phi([0]_H dot t)=phi([0]_H) dot t=[t]_(H').
```

The stabilizer of `[0]_H` is `H`. An equivariant homeomorphism maps this
stabilizer to the stabilizer `H'` of the target basepoint, so `H=H'`.
Conversely, when the subgroups agree, the forced formula is well-defined and
is a basepoint-preserving equivariant homeomorphism. QED.

### Theorem 5.2 — the normalized strict functor

For an object `(G,c)` of `C_str`, choose any unit `x` and put

```text
S(G,c)=(R/H,[0]),
H=H_x=Per_x([c]).
```

For a strict morphism `F:(G,c)->(G',c')`, put

```text
S(F)([t]_H)=[t]_(H').
```

Then `S:C_str->Hom_(R,0)^std` is a well-defined functor.

**Proof.** Transitivity and commutativity make `H_x` independent of `x`, as
proved in Section 4.1. Lemma 2.1 identifies it with the normalized period
image. Theorem 4.1 with `alpha=1` gives `H'=H`, so Lemma 5.1 proves that
`S(F)` is well-defined, continuous, basepoint-preserving, strictly
equivariant, and unique.

For the identity morphism,

```text
S(id)([t])=[t].
```

For composable strict morphisms `F,F'`, all three subgroups agree and

```text
S(F' o F)([t])=[t]
                 =S(F')(S(F)([t])).
```

Thus identities and composition are preserved. QED.

Different strict morphisms can have the same image under `S`; faithfulness
is not claimed. The functor records the normalized marked period quotient,
not the full groupoid.

### 5.2 Actual charts, naturality, and basepoint change

For a chosen unit `x`, define

```text
theta_x:R/H->X,
theta_x([t])=x dot t.
```

### Theorem 5.3 — the chart laws and one-sided topology

`theta_x` is a well-defined right-`R`-equivariant set bijection. For every
strict morphism `F`,

```text
F_0 o theta_x=theta_(F_0(x)) o S(F).
```

If `x'=x dot u` and

```text
tau_u([t])=[u+t],
```

then the exact basepoint-change law is

```text
theta_(x')=theta_x o tau_u.
```

With the usual quotient topology on `R/H` and the actual indiscrete topology
on `X`, `theta_x` is continuous. Its inverse is not continuous.

**Proof.** If `[t]=[s]`, then `t-s in H_x`, so `x dot t=x dot s`; hence the
map is well-defined. Transitivity gives surjectivity. If
`x dot t=x dot s`, applying the action by `-s` gives
`x dot(t-s)=x`, so `t-s in H_x`; hence it is injective. Equivariance is

```text
theta_x([t] dot u)=x dot(t+u)=theta_x([t]) dot u.
```

For a strict `F`, the arrow `(x,t)` has image with range `F_0(x)` and marked
time `t`. In a range-first transformation groupoid that arrow is uniquely
`(F_0(x),t)`. Comparing sources gives

```text
F_0(x dot t)=F_0(x) dot t.
```

Therefore

```text
F_0(theta_x([t]))
 =F_0(x dot t)
 =F_0(x) dot t
 =theta_(F_0(x))(S(F)([t])).
```

For `x'=x dot u`,

```text
theta_(x')([t])=(x dot u) dot t
                      =x dot(u+t)
                      =theta_x(tau_u([t])).
```

Every map into an indiscrete space is continuous, so `theta_x` is
continuous. Since `H=LZ` is a proper closed subgroup, the standard quotient
`R/H` is a nontrivial Hausdorff space. The transitive `X` is therefore also
nontrivial as a set. If `theta_x^(-1)` were continuous, it would be a
nonconstant continuous map from a nontrivial indiscrete space into a `T0`
space, contradicting the elementary separated-target lemma used in Papers
9--10. Thus the inverse is not continuous. QED.

The translation `tau_u` is generally not basepoint-preserving: it sends
`[0]` to `[u]`. Therefore a chosen unit supplies a based chart, while only
the unbased homogeneous space is independent of that choice. In particular,
the standard quotient is not the actual inherited topology.

### 5.3 The scaled semilinear map and the stop

For `alpha>0`, define

```text
D_alpha:R/H->R/(alpha H),
D_alpha([t]_H)=[alpha t]_(alpha H).
```

This is well-defined and is a homeomorphism with inverse `D_(alpha^(-1))`:
it is induced on quotient spaces by the homeomorphism `t |-> alpha t` of
`R`. It preserves `[0]` and obeys the semilinear law

```text
D_alpha(z dot u)=D_alpha(z) dot (alpha u).
```

For a scaled morphism `(F,alpha)`, Theorem 4.1 gives `H'=alpha H`, and the
scaled chart square is

```text
F_0 o theta_x=theta_(F_0(x)) o D_alpha.
```

Indeed the source comparison now reads

```text
F_0(x dot t)=F_0(x) dot(alpha t).
```

However, for the unchanged right `R`-actions,

```text
D_alpha(z dot u)=D_alpha(z) dot(alpha u)
```

is not the strict equivariance equation

```text
D_alpha(z dot u)=D_alpha(z) dot u
```

unless `alpha=1`. If `alpha!=1`, strict equivariance would require
`(alpha-1)R` to be contained in the discrete lattice `alpha H`, which is
impossible. Consequently `D_alpha` is not a morphism of
`Hom_(R,0)^std` unless `alpha=1`, and it is not silently inserted into the
strict functor.

For an arbitrary class `[b]`, the quotient `R/Per_x([b])` is only a
value-space quotient. No result here identifies it with an action orbit or
with the actual inherited topology.

## 6. Required matrices

### 6.1 Theorem matrix

| Target | Subclaim | Lane result | Exact ceiling |
|---|---|---|---|
| `P12-6` | every actual fixed-orbit unit has `Per_x([c])=(log p)Z` | **PROVED** | Deninger owns stabilizer/clock; Paper 12 owns marked image |
| `P12-6` | every exact fixed-prime packet unit has the same image | **PROVED — PACKET_COROLLARY** | no `G^global` or cross-prime promotion |
| `P12-7` | `C_str`, `C_scale`, and `C_un` are categories | **PROVED** | author-defined categories only |
| `P12-7` | `Per_(F_0x)([c'])=alpha Per_x([c])` | **PROVED** | covariance, not an iff characterization |
| `P12-7` | unequal `L,M` are scaled/unmarked isomorphic but not strictly isomorphic | **PROVED** | existential non-descent only |
| `P12-7` | orientation reversal preserves `LZ` without preserving `c` | **PROVED** | nonconverse in `C_un`; negative scale is not in `C_scale` |
| `P12-8` | rigid pointed target and strict functor `S` | **PROVED** | normalized strict category only |
| `P12-8` | chart, naturality, and basepoint-rotation laws | **PROVED** | set-level actual chart with one-sided continuity |
| `P12-8` | scaled dilation is semilinear, not a strict target morphism | **PROVED** | no scaled extension of `S` in the frozen target |

### 6.2 Owner matrix

| Owner | Unit topology/action | Mark/source | Result licensed here | Forbidden claim |
|---|---|---|---|---|
| generic `G(X,alpha)` | author arbitrary nonempty indiscrete right `R`-space | coordinate `c=t`, no arithmetic normalization | category lemmas and arbitrary-period controls | arithmetic or Deninger credit |
| `G_(p,a)^orb` | Paper-9 actual inherited orbit; Deninger restricted right flow | Deninger-normalized additive clock | fixed-orbit marked image `(log p)Z` | “Deninger's groupoid/cohomology” |
| `G_p^pkt` | Paper-9 actual inherited packet; Deninger fixed-prime packet flow | same clock at every unit | `PACKET_COROLLARY` | orbitwise promotion, cross-prime union, or global suspension |
| `G^global` | excluded | excluded | none | every Paper-12 theorem on this owner |
| `(R/H,[0])^std` | usual Hausdorff quotient with standard translation | derived from normalized marked `H` | strict pointed proxy functor | identification with actual indiscrete topology |
| `G_H` controls | author-declared indiscrete quotient carriers | arbitrary coordinate clocks/subgroups | falsifiers and scope boundaries | arithmetic selectivity or source provenance |

### 6.3 Category matrix

| Property | `C_str` | `C_scale` | `C_un` |
|---|---:|---:|---:|
| preserves `c` exactly | yes | only when `alpha=1` | not required |
| transports subgroup | equality | `H'=alpha H` | no marked transport law |
| connects unequal lattice generators | no | yes, by `F_(M/L)` | yes, after forgetting the mark |
| orientation reversal `F_-` | no | no (`alpha>0`) | yes |
| ordinary subgroup is an invariant | yes | no | no |
| exact subgroup equality implies strictness | not a converse claim | not a converse claim | false by `F_-` |

### 6.4 Functor and topology matrix

| Construction | Formula | Exact status | Stop |
|---|---|---|---|
| object `S(G,c)` | `(R/H,[0])`, `H=Per_x([c])` | unit-independent on normalized transitive objects | no arbitrary-class orbit chart |
| strict arrow `S(F)` | `[t]_H |-> [t]_(H')` | unique target morphism because `H'=H` | no claim of faithfulness/fullness |
| actual chart `theta_x` | `[t] |-> x dot t` | equivariant set bijection; standard-to-actual continuous | inverse not continuous |
| basepoint change | `theta_(x dot u)=theta_x o tau_u` | exact | `tau_u` need not preserve `[0]` |
| strict naturality | `F_0 theta_x=theta_(F_0x) S(F)` | exact | strict category only |
| scaled dilation | `D_alpha([t])=[alpha t]` | quotient homeomorphism; semilinear | not in `Hom_(R,0)^std` unless `alpha=1` |

### 6.5 Same-object/source-credit matrix

| Claim component | Exact object | Owner of input | Owner of conclusion in this lane | No-splice rule |
|---|---|---|---|---|
| fixed-prime packet and every-unit `p^Z` | Deninger `Gamma_p`, `E=E_f` | Deninger p. 38 and Theorem 6.1 | none; imported source fact | no topology, groupoid, or cohomology credit to Deninger |
| additive `+t` and `(log p)Z` | same restricted source flow | Deninger exponential clock | none; exact conversion only | no fitted/rescaled clock |
| actual packet/orbit topology | same `Gamma_p` and its orbits | Paper 9 | none | no ordinary-circle or proxy topology import |
| range-first transformation groupoid | actual orbit/packet crossed with `R` | Paper 11/Paper 12 allocation | none | do not call it source-defined |
| class image `Per_x([c])` | exact author groupoid with source mark | Lemma 2.1 plus source stabilizer | Paper 12 / this lane | no claim that unmarked `G` selects `c` |
| standard quotient/chart | derived `R/H` proxy | standard quotient construction; Paper-10 direction | Paper 12 / this lane | never identify proxy and actual topology |

### 6.6 Standalone matrix

| Standalone condition relevant to this lane | Evidence here | Status |
|---|---|---|
| source-verified every-unit packet statement | Corollary 3.2 | **CLOSED** |
| exact strict/scaled/unmarked covariance and non-descent | Theorems 4.1--4.2 plus `F_-` | **CLOSED** |
| normalized pointed quotient functor and topology direction | Theorems 5.2--5.3 | **CLOSED** |
| arbitrary-period and label falsifiers | Section 4.4 | **CLOSED analytically; executable controls remain `P12-9`** |
| all-degree complex and `H^1` package | outside this lane | **PENDING integration** |
| deterministic control execution | outside this lane | **PENDING** |
| independent Phase-3 review and stable integrated proof tuple | later gate | **PENDING** |
| Route, manuscript, citation, peer, release, and public-sync gates | expressly unauthorized here | **BLOCKED by workflow, not a mathematical finding** |

The correct lane-level disposition is therefore

```text
standalone_lane_status: ELIGIBLE_PENDING_INTEGRATION_AND_INDEPENDENT_REVIEW
STANDALONE_PASS: not granted
NOTE_OR_MERGE: not triggered by packet failure in this lane
release: not authorized
```

The bounded Phase-2 novelty result remains exactly
`SUPPORTED_WITHIN_SEARCH`; this report makes no absolute priority claim.

## 7. Open findings and final lane verdict

### 7.1 Finding register

| Severity | Count | Open item |
|---|---:|---|
| Critical (`C`) | 0 | none |
| Major (`M`) | 0 | none |
| Minor (`m`) | 0 | none |

There is no packet, covariance-direction, inverse, category-composition,
basepoint, naturality, quotient-topology, or scaled-semilinearity blocker in
`P12-6`--`P12-8`.

### 7.2 Pending downstream work is not silently closed

The following are required later but are not open defects in this bounded
lane: integration with the independent `P12-1`--`P12-5` proof, execution and
review of `P12-9`, independent review of the stable Phase-3 tuple, the
standalone-versus-merge decision on the full package, and every Route,
manuscript, citation, declaration, release, and synchronization gate.

### 7.3 Final verdict

```text
P12-6: PROVED — PACKET_COROLLARY; ORBIT_ONLY=false
P12-7: PROVED — strict preservation, positive covariance,
                   explicit unequal-period non-descent,
                   orientation-reversal nonconverse
P12-8: PROVED — normalized strict pointed quotient functor,
                   chart/naturality/basepoint laws,
                   one-sided topology, scaled semilinear stop
critical_open: 0
major_open: 0
minor_open: 0
standalone_release: PENDING
route_or_manuscript_authorized: false
```

The detached SHA-256 of this report is computed after the final byte is
written; it cannot be embedded in the hashed file without changing that
hash. The post-write checksum is the authoritative output receipt supplied
to the integrating proof lane.
