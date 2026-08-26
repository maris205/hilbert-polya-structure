# Paper 11 Phase-3 convention, proxy, and ownership proofs

Proof date: **2026-08-15 (Asia/Shanghai)**  
Scope: **P11-6--P11-8 only**  
Result: **P11-6 PROVED; P11-7 PROVED AT THE FROZEN TEST-FUNCTION LEVEL;
P11-8 PROVED**  
Completion extension of `I`: **NOT CLAIMED**  
Route verdict: **NOT PERFORMED**

This report proves only the convention split, the actual/standard-proxy map
and strict image, and the general action-blindness/ownership statements. It
does not edit a lock, run deterministic controls, prove the other Phase-3
targets by reference, create a Route record, or write manuscript text.

## 1. Exact-byte binding and owner boundary

The proofs use the current active bytes and the Phase-2 gate at the following
SHA-256 values:

| Artifact | SHA-256 | Role |
|---|---|---|
| `notes/research_protocol.md` | `27c0ffd9c233301528e36f401e9cdf3f4030d65cea8002aafcf6fb97e557f860` | exact definitions and P11 targets |
| `notes/candidate_lock.md` | `a97e9c30bca6bf9cee3e5543b5d83b72ab7291e5485fa9604811dfa3ce4c8012` | typed owners, signs, exclusions, ceilings |
| `notes/phase1_design_amendment.md` | `e3124bddd6fb9bd9661c6104137086f87ca1a6e2b4fbae212a65b40304aa9572` | repaired signatures |
| `notes/phase1_final_gate.md` | `ac26f72f9ff1c5eb935903c20518a43aa043feb8d1572a920bfad471ca47d85f` | Phase-1 exact-byte gate |
| `notes/phase2_framework_source_audit.md` | `a2345046972cc00d3031abdc214442359d0f78c7c0daf7d513ea26f924fb7439` | framework applicability and source strengths |
| `notes/phase2_owner_proxy_audit.md` | `18116cf52c2359a840c9996fb6424fae56260f590990fac79704c040245fa761` | actual/proxy direction, sign, measure, theorem-strength ledger |
| `notes/phase2_novelty_search.md` | `024398a3575cf41a7f33c6950dc1c8de8a8d5f4ec81675f8760ce7c7a87ac24e` | bounded novelty ceiling |
| `notes/sources/framework_source_manifest.md` | `b3b61a5bdfd206cb8cc4a8bf574373bc6485d96b22547698ac69fb3a9e36812f` | exact retained manifestations and locators |
| `notes/sources/framework_sources.sha256` | `057e9c32b2f654c765f40f0ddd40014c12876d22c0567470fdf04a2eb0fd2e7f` | ten-file source/preflight checksum ledger |
| `notes/phase2_final_review.md` | `9607ec7eab0a947bf7de14d2c8a4233185c4e94994e19821d16b3f41b7c2638d` | integrated C0/M0/m0 source review |
| `notes/phase2_final_gate.md` | `96d5bb1e82bb5db416d9b52993b13fdc6c5eb25e26e0e1896b265138b800f0fb` | Phase-3 authorization |
| `notes/pipeline_state.md` | `317ab9e8b3082b2d8bc75590618a6e86ca742bb8c23a899c3b612ea6304125e6` | current status: proofs/controls authorized; Route/manuscript blocked |

The Phase-2 audits used the preceding status-only pipeline byte
`d4801ffb...`; the current `317ab9e8...` byte changes only the post-gate
status. No object, sign, function convention, measure, or theorem target is
changed here.

Fix a rational prime `p` and a normalized Paper-9 label `a`, and abbreviate

```text
L=L_p=log p,
X=X_{p,a},
G_act=X rtimes R,
S=R/LZ with its ordinary circle topology,
G_std=S rtimes R.
```

The actual `X` is nonempty, nontrivial, and indiscrete by the locked Paper-9
theorem. Deninger owns the underlying right flow and stabilizer `LZ`; Paper 9
owns the inherited topology; Paper 11 owns the groupoid assembly, function
owners, proofs below, and no more.

## 2. Two elementary topology lemmas

### Lemma 2.1 — opens of an indiscrete product

Let `X` be a nonempty indiscrete space. The open subsets of `X x R` are
exactly

```text
emptyset and X x U, with U open in R.
```

**Proof.** A product-basis element is `V x U`, where
`V in {emptyset,X}` and `U` is open in `R`. Every nonempty basis element is
therefore `X x U`, and arbitrary unions retain this form. The converse is
immediate. QED.

### Lemma 2.2 — quasi-compact subsets and support

For every subset `K` of `X x R`, with its subspace topology,

```text
K is open-cover quasi-compact  iff  pi_R(K) is compact in R.
```

If `N` is a subset of `R`, then

```text
closure_(X x R)(X x N)=X x closure_R(N).
```

**Proof.** If `K` is quasi-compact, its continuous time projection is
quasi-compact; in Hausdorff `R` this means compact. Conversely, every relative
open subset of `K` is `K intersect (X x U)` for some open `U` in `R`. An open
cover of `K` therefore induces an open cover of `pi_R(K)`; compactness of the
projection gives a finite subcover and hence a finite cover of `K`.

For the closure statement, `(x,t)` is in the closure of `X x N` exactly when
every neighborhood `X x U` of it meets `X x N`, which is equivalent to every
neighborhood `U` of `t` meeting `N`. QED.

## 3. P11-6 — the HOpen diagnostic and framework no-go

### Theorem 3.1 — no nonempty Hausdorff open arrow patch

If `X` is nontrivial indiscrete, then `X x R` has no nonempty Hausdorff open
subset.

**Proof.** Let `O=X x U` be a nonempty open subset. Choose `t in U` and
distinct `x_0,x_1 in X`. Every relative open neighborhood in `O` of
`(x_0,t)` has the form `X x (U intersect V)` for an open neighborhood `V` of
`t`, and therefore also contains `(x_1,t)`. The two points are topologically
indistinguishable in `O`; in particular `O` is not `T0` and cannot be
Hausdorff. QED.

### Corollary 3.2 — exact raw HOpen value

Under the frozen raw-function definition,

```text
C_c^HOp(G_act)={0}.
```

**Proof.** The only open Hausdorff subset of `G_act` is `emptyset`. Its
`C_c` space contains only the zero function, whose raw zero-extension is
zero. The linear span of all legal generators is therefore `{0}`. No ambient
continuity of a zero-extension is used. QED.

This zero is a **diagnostic raw-span value**. It is not a standard groupoid
algebra or completion. The convention split is genuine and not merely a zero
algebra in disguise: choose a nonzero `g in C_c(R)` and put
`Phi(g)(x,t)=g(t)`. It is globally continuous, and Lemma 2.2 gives

```text
supp_G(Phi(g))=X x supp_R(g),
```

which is quasi-compact. Hence `C_qc^glob(G_act)` is nonzero while the HOpen
diagnostic is zero.

### Proposition 3.3 — retained-framework applicability

The exact Phase-2 framework classifications are consequences of failed
hypotheses, not of the diagnostic value:

| Framework / record | Required hypothesis that fails on `G_act` | Classification | Licensed conclusion |
|---|---|---|---|
| Tu 2004 | Tu-local compactness requires a compact Hausdorff neighborhood and therefore local Hausdorffness | `NOT_APPLICABLE` | terminology and HOpen comparison only |
| Muhly--Williams 2008 | unit space must be Hausdorff; every arrow must have a compact Hausdorff neighborhood | `NOT_APPLICABLE` | accepted raw Hausdorff-open-span practice only |
| Exel 2009 étale framework | unit must be locally compact Hausdorff; range/source must be local homeomorphisms | `NOT_APPLICABLE` | an independent boundary only |
| Buss--Holkar--Meyer 2018 | the universal property is formulated for locally compact Hausdorff groupoids with Haar systems | `NOT_APPLICABLE` | no actual universal/full theorem |
| Green/Williams homogeneous-space theorems | require the ordinary locally compact Hausdorff quotient `R/LZ`, not its actual indiscrete retopology | `NOT_APPLICABLE_ACTUAL` | `APPLICABLE_PROXY_ONLY` |
| MRW equivalence/transitive theorems | retained standing locally compact/Haar-system domain is not met by the actual topology | `NOT_APPLICABLE_ACTUAL` | alternative full-level proxy route only |
| Frozen raw `C_c^HOp(G_act)` | an author diagnostic, not an invocation of any preceding framework | `DIAGNOSTIC_ONLY` | the direct value in Corollary 3.2 |
| `GLOB-FIBRE-FAMILY`, `Ind_x`, transported completions | author definitions outside every retained actual framework | `AUTHOR_DEFINED_DIRECT` | only direct proofs and subsequent group-`R` transport |

For Tu, a compact Hausdorff neighborhood would contain a nonempty ambient
open subset; that subset would be Hausdorff as a subspace, contradicting
Theorem 3.1. Muhly--Williams fails both its Hausdorff-unit and neighborhood
conditions. Exel already fails at the non-Hausdorff unit; moreover, on any
nonempty arrow open `X x U`, range cannot be injective because `U` contains
two distinct time points, so it cannot be a local homeomorphism. The actual
arrow space itself is not even `T0`, so the Buss--Holkar--Meyer Hausdorff
standing hypothesis fails immediately.

Nothing in this argument proves that every conceivable non-Hausdorff
convolution theory is impossible. Logical non-applicability has the form

```text
source theorem hypotheses fail  =>  that source theorem cannot be invoked,
```

not

```text
source theorem hypotheses fail  =>  no construction can exist.
```

Indeed the nonzero author-defined global algebra above is an explicit reason
not to make the latter inference. This closes P11-6 without universalizing a
bounded framework audit.

## 4. P11-7 — exact actual/proxy map, topology direction, and strict image

The frozen orbit chart and its inverse are

```text
theta:S_set -> X,       theta([r])=x^0 dot r,
beta:X_set -> S_set,    beta=theta^{-1}.
```

They satisfy

```text
theta([r]) dot t=theta([r+t]),
beta(x dot t)=beta(x)+t.
```

Define

```text
J:G_act -> G_std,       J(x,t)=(beta(x),t),
J^{-1}([r],t)=(theta([r]),t).
```

### Theorem 4.1 — set-groupoid isomorphism and equivariance

`J` is a bijective set-groupoid homomorphism with the displayed inverse. It
intertwines range, source, units, product, inverse, and the right action.

**Proof.** Bijectivity is immediate from `beta=theta^{-1}`. For endpoints,

```text
r_std(J(x,t))=beta(x)=beta(r_act(x,t)),
s_std(J(x,t))=beta(x)+t=beta(x dot t)=beta(s_act(x,t)).
```

For a composable pair,

```text
J((x,t)(x dot t,u))
  =(beta(x),t+u)
  =(beta(x),t)(beta(x)+t,u)
  =J(x,t)J(x dot t,u).
```

Also

```text
J((x,t)^{-1})
  =(beta(x dot t),-t)
  =(beta(x)+t,-t)
  =J(x,t)^{-1}.
```

Units follow by setting `t=0`, and equivariance is exactly the relation for
`beta` above. QED.

### Theorem 4.2 — the topology direction is strict

```text
J is not continuous,        J^{-1} is continuous.
```

**Proof.** Every actual arrow open is `X x U`. Its inverse image under the
map `J^{-1}:G_std->G_act` is `S x U`, which is open, so `J^{-1}` is
continuous.

Choose a nonempty proper open arc `V` in the ordinary circle `S`. Then
`V x R` is open in `G_std`, while

```text
J^{-1}(V x R)=beta^{-1}(V) x R
```

is a nonempty proper unit-coordinate subset and hence is not open in
`G_act`. Thus `J` is not continuous. QED.

This is a finer proxy retopology on the same arrow set, not a homeomorphism,
quotient, or separated reflection of the actual topology.

### Lemma 4.3 — exact factorization and support on the actual owner

Every `f in C_qc^glob(G_act)` has a unique `g in C_c(R)` such that

```text
f(x,t)=g(t).
```

Moreover

```text
supp_act(f)=X x supp_R(g).
```

**Proof.** For fixed `t`, the restriction `x |-> f(x,t)` is a continuous map
from the indiscrete `X` to the Hausdorff space `C`, so it is constant. Define
`g(t)` to be this common value. For any fixed `x`, the map
`t |-> (x,t)` is continuous; hence `g` is continuous. Uniqueness follows
from nonemptiness of `X`. Lemma 2.2 gives the displayed support and shows
that quasi-compactness of the actual support is equivalent to compactness of
`supp_R(g)`. Thus `g in C_c(R)`. QED.

### Theorem 4.4 — `I` is a fibre-compatible `*`-monomorphism

Define at the frozen test-function level

```text
I:C_qc^glob(G_act) -> C_c(G_std),
I(f)=f o J^{-1}.
```

Then `I` is well-defined and injective, preserves the exact support under
`J`, preserves the range-fibre Lebesgue measures and integrals, and
intertwines convolution and involution.

**Proof.** If `f=Phi(g)` as in Lemma 4.3, then

```text
I(f)([r],t)=f(theta([r]),t)=g(t).
```

It is continuous on the ordinary product topology, and

```text
supp_std(I(f))=S x supp_R(g)=J(supp_act(f)).
```

The right side is compact because both factors are compact. Thus `I(f)` lies
in the standard Hausdorff `C_c(G_std)`. Injectivity follows because `J^{-1}`
is surjective.

For each `x`, `J` restricts to

```text
J^x:G_act^x -> G_std^{beta(x)},
(x,t) |-> (beta(x),t).
```

Both range-fibre measures are the pullback of the same Lebesgue `dt`; hence
`J^x_* lambda_act^x=lambda_std^{beta(x)}`. Since `J` commutes with inversion,
the corresponding inversion-pushed source-fibre measures are preserved as
well. In particular, for every licensed `f`,

```text
integral_(G_act^x) f d lambda_act^x
  =integral_(G_std^{beta(x)}) I(f) d lambda_std^{beta(x)}.
```

Under the frozen right-action, range-first convention, proxy convolution and
involution are

```text
(F *_std H)([r],t)
  =integral_R F([r],u) H([r+u],t-u) du,
F^*([r],t)=conjugate(F([r+t],-t)).
```

Write `f=Phi(g)` and `h=Phi(k)` by Lemma 4.3. The same coordinate formula
first gives

```text
f*h=Phi(g*k),       f^*=Phi(g^*),
```

so convolution and involution are closed on the actual named domain. Now,
using `theta([r]) dot u=theta([r+u])`,

```text
I(f*h)([r],t)
 =integral_R f(theta([r]),u)
              h(theta([r]) dot u,t-u) du
 =integral_R I(f)([r],u)I(h)([r+u],t-u) du
 =(I(f) *_std I(h))([r],t),
```

and

```text
I(f^*)([r],t)
 =conjugate(f(theta([r]) dot t,-t))
 =conjugate(I(f)([r+t],-t))
 =I(f)^*([r],t).
```

Thus `I` is a `*`-monomorphism on exactly the named test-function domains.
QED.

### Theorem 4.5 — exact image and a strict proxy witness

Put

```text
A_const={F in C_c(G_std):
         F([r],t)=F([s],t) for all [r],[s] in S and t in R}.
```

Then

```text
I(C_qc^glob(G_act))=A_const,
```

and this is a proper `*`-subalgebra of `C_c(G_std)`.

**Proof.** Theorem 4.4 shows that every image function is unit-coordinate
constant. Conversely, if `F in A_const`, choose any `[r_0]` and put
`g(t)=F([r_0],t)`. Then `g` is continuous and

```text
supp_std(F)=S x supp_R(g).
```

Compactness of the left side implies compactness of `supp_R(g)` by time
projection. Hence `g in C_c(R)`, `Phi(g) in C_qc^glob(G_act)`, and
`I(Phi(g))=F`. This proves the image identity. Closure under convolution and
involution also follows directly from Theorem 4.4, or from ordinary group
convolution on the time functions.

To prove strictness, take nonzero `k in C_c(R)` and define

```text
F_out([r],t)=exp(2 pi i r/L) k(t).
```

The circle character is well-defined, continuous, nonconstant, and never
zero. Thus

```text
supp_std(F_out)=S x supp_R(k)
```

is compact, so `F_out in C_c(G_std)`. At any `t` with `k(t)!=0`, it varies
with `[r]`; hence `F_out notin A_const`. QED.

### 4.6 Completion stop

No map on any completion is defined or inferred here. In particular,

```text
I on test functions
  does not imply
an extension C^full_glob or C^red_glob -> a proxy completion.
```

Such an extension would require a separately named target norm and a proof of
boundedness or isometry. The Phase-2 BHM/Green/MRW/BGR/Williams theorems
describe the **proxy** algebra at their exact strengths; none supplies that
actual-to-proxy norm estimate. No density, completion surjectivity, actual/
proxy Morita equivalence, stable isomorphism, or unstabilized completion
isomorphism is claimed.

## 5. Standard-proxy source theorem ledger

The direct P11-7 proof above and the retained source theorems occupy separate
rows:

| Record | Exact strength licensed by the frozen source audit | Explicit non-credit |
|---|---|---|
| BHM Theorem 7.1, after `K([r],t)=(t,[r+t])` | natural **full** proxy transformation-groupoid / full crossed-product isomorphism | no reduced bridge, tensor model, or actual theorem |
| Green Proposition 3; Williams 4.22; MRW 2.8 | full-level strong Morita equivalence | no algebra isomorphism or tensor model |
| Brown--Green--Rieffel 1.2 | stable isomorphism under its hypotheses | no cancellation of `K` and no unstabilized conclusion |
| Williams 4.30, after coordinate inversion and `rho=1/L` | unstabilized full proxy isomorphism `C(S) rtimes_alpha,full R ~= C^*(LZ) tensor K(L^2(S,mu_p))` | proxy only; not an actual-completion map |
| MRW 3.1 | independent unstabilized full groupoid tensor route for some positive unit-space measure | does not select the frozen `mu_p` |
| Williams 7.13 | full equals reduced **proxy crossed products** because `R` is amenable | no reduced proxy groupoid bridge from the retained sources |
| Williams Example 1.80, Proposition 3.1, Examples 7.9/7.11 | `C^*(R)=C_r^*(R) ~= C_0(R)` with Fourier kernel `exp(-it xi)` | group `R` owner; actual use only by registered transport |
| Theorems 4.4--4.5 of this report | strict test-function `*`-monomorphism with image `A_const` | no completion extension or standard actual-groupoid theorem |

The proxy coefficient sign remains

```text
alpha_t(h)([r])=h([r+t]).
```

The Phase-2 dictionary converts the right action to BHM's left action and
then uses circle-coordinate inversion for Williams; no sign is silently
changed. The `mu_p` in Williams 4.30 is the frozen normalized Haar probability
obtained from equation (4.63) with `rho=1/L`.

## 6. P11-8 — general action-blind theorem

### Theorem 6.1 — action-blind global convolution and regular norm

Let `X` be **any nonempty indiscrete space**, and let
`alpha:X x R->X`, written `x dot t`, be any right `R`-action. Every such
action is jointly continuous because its codomain is indiscrete. Form the
right-action transformation groupoid

```text
G(X,alpha)=X rtimes R
```

with the frozen product topology and range-first convention. Then:

1. `Phi_X:g |-> ((x,t) |-> g(t))` is a canonical `*`-isomorphism
   `C_c(R)->C_qc^glob(G(X,alpha))`;
2. the author range-fibre integrals, convolution, and involution are
   independent of `X` and `alpha` under `Phi_X`;
3. every frozen unit regular representation is unitarily the same left
   regular representation of `R`;
4. the author-defined reduced norm and the transported full norm are the
   ordinary group reduced and full norms; hence their completions are
   `C_r^*(R)` and `C^*(R)`, equal because `R` is amenable.

If `X` is nontrivial, the HOpen diagnostic is also zero, independently of the
action. For singleton `X`, the action-blind convolution conclusion remains
true but the HOpen-zero statement does not; the singleton is Hausdorff.

**Proof.** Lemmas 2.1--2.2 and the argument of Lemma 4.3 depend only on the
topology, not on the action. They give the bijection

```text
C_qc^glob(G(X,alpha))={Phi_X(g):g in C_c(R)}.
```

For `f=Phi_X(g)` and `h=Phi_X(k)`, the exact formulas are

```text
(f*h)(x,t)
 =integral_R f(x,u)h(x dot u,t-u)du
 =integral_R g(u)k(t-u)du
 =(g*k)(t),

f^*(x,t)
 =conjugate(f(x dot t,-t))
 =conjugate(g(-t)).
```

Thus the action coordinate disappears from both operations. Associativity
and the `*` identities transport from ordinary group convolution. The range
fibre at `x` is parameterized by `t |-> (x,t)` and carries `dt`, so

```text
integral_(G^x) Phi_X(g) d lambda^x=integral_R g(t)dt,
```

independent of `x` and the action. Left invariance is equally direct: for
`gamma=(x,v)`, the integrand on `G^{x dot v}` is `g(v+u)`, whose integral is
`integral g` after translation.

For the source fibre, define exactly as locked

```text
vartheta_x(t)=(x dot (-t),t).
```

It is a homeomorphism `R->G_x`. Inversion sends `(x,t)` to
`vartheta_x(-t)`; reflection preserves Lebesgue measure, so
`lambda_x=(vartheta_x)_*dt` and the locked `U_x` is unitary. If
`gamma=vartheta_x(t)` and `eta=vartheta_x(u)`, then

```text
eta^{-1}=(x,-u),
gamma eta^{-1}=(x dot (-t),t-u).
```

Consequently

```text
[U_x Ind_x(Phi_X(g)) U_x^{-1}xi](t)
  =integral_R g(t-u)xi(u)du
  =[lambda_R(g)xi](t).
```

This simultaneously proves boundedness on the named domain and shows that
every unit gives the same regular norm. Hence

```text
||Phi_X(g)||_(red,glob)=||lambda_R(g)||.
```

The full norm is defined by transport from `C^*(R)`. The source-verified
amenability result for the group `R` gives

```text
C^full_glob(G(X,alpha))
  ~= C^*(R)=C_r^*(R)
  ~= C^red_glob(G(X,alpha))
  ~= C_0(R)
```

with the frozen Fourier sign `exp(-it xi)`. These are author-defined
transported completions, not standard groupoid completions. Finally, if
`X` is nontrivial, Theorem 3.1 and Corollary 3.2 apply without reference to
`alpha`. QED.

### Corollary 6.2 — exact adversarial mathematical controls

The theorem survives the following independent changes:

| Control | Exact action data changed | Result |
|---|---|---|
| nontrivial indiscrete `X`, trivial action `x dot t=x` | every orbit is a singleton; every stabilizer is all of `R` | same `C_c(R)`, fibre formula, regular norm, and transported completions |
| `X=({0,1} x R/Z)_indisc`, `(i,[r]) dot t=(i,[r+t])` | nontrivial action with two distinct orbits; stabilizer `Z` | same analytic result |
| `X_{ell,L}=({ell} x R/LZ)_indisc`, `[r] dot t=[r+t]`, arbitrary `L>0` | transitive action; stabilizer varies as `LZ` | same analytic result for every `ell,L` |
| arbitrary labels `ell` | prime, composite, randomized-string, or non-arithmetic tags alter no formula | same analytic result; no label parser is used |
| arbitrary positive periods | `L=log p`, `log m` for composite `m`, `1`, `pi`, or any fixed positive value | same analytic result although the stabilizer changes |

The nontransitive example is deliberately infinite: an algebraic action of
the divisible group `R` on a finite set has trivial finite image, so a claimed
finite nontrivial `R`-action would be a false control. The theorem is
pointwise in every label and every positive period; randomized labels require
no probabilistic inference.

These controls establish a `PROVES_TOO_MUCH` diagnostic for arithmetic
specificity. They do not refute the theorem; they show that its analytic
output cannot receive credit for distinguishing the arithmetic action,
period, orbit structure, or stabilizer.

### Corollary 6.3 — rational-Witt application, fixed orbit only

For every rational prime `p` and every normalized Paper-9 orbit label `a`,
the locked input `X_{p,a}` is nonempty, nontrivial, and indiscrete, and its
Deninger right action is an instance of Theorem 6.1. Therefore:

```text
C_qc^glob(G_{p,a}^act) ~= C_c(R),
C_c^HOp(G_{p,a}^act)={0},
all range-fibre and convolution formulas reduce to those of R,
all unit regular norms reduce to lambda_R,
C^full_glob ~= C^red_glob ~= C^*(R) ~= C_0(R).
```

The first line is a theorem on the exact actual fixed-orbit owner; the final
identifications are transported author completions. In the abstract algebra,
fibre formula, regular norm, and transported completion, none of

```text
p, a, L_p, the action, the orbit decomposition, or the stabilizer L_p Z
```

survives. The concrete groupoid still retains `X_{p,a}`, its source/range
maps, action, and stabilizer as host data. This is an application of a general
topological theorem to the rational-Witt input, not a packet theorem, prime
coproduct theorem, full-suspension theorem, or new Deninger source claim.

## 7. Theorem/proof matrix

| Target | Atomic statement | Result | Proof owner / locator | Explicit ceiling |
|---|---|---|---|---|
| P11-6 | no nonempty Hausdorff open arrow subset | `PROVED` | Theorem 3.1 | actual nontrivial indiscrete owner only |
| P11-6 | raw HOpen span equals zero | `PROVED` | Corollary 3.2 | diagnostic, not standard algebra |
| P11-6 | retained actual frameworks fail exact hypotheses | `PROVED_FROM_TOPOLOGY_AND_SOURCE_GATES` | Proposition 3.3 | no universal nonexistence theorem |
| P11-7 | `theta/beta/J` equivariance and set-groupoid isomorphism | `PROVED` | Theorem 4.1 | set/groupoid level; no topology imported |
| P11-7 | `J` not continuous; `J^{-1}` continuous | `PROVED` | Theorem 4.2 | proxy topology strictly finer |
| P11-7 | `I` preserves support, fibres, convolution, and `*` | `PROVED` | Theorem 4.4 | test-function level only |
| P11-7 | image is exactly `A_const` and is proper | `PROVED` | Theorem 4.5 | no density or completion claim |
| P11-8 | general nonempty-indiscrete action-blind theorem | `PROVED` | Theorem 6.1 | generic theorem; no arithmetic novelty |
| P11-8 | trivial/nontransitive/arbitrary-label/period controls | `PROVED_BY_UNIVERSAL_QUANTIFIER` | Corollary 6.2 | `PROVES_TOO_MUCH` for arithmetic specificity |
| P11-8 | every rational-Witt fixed orbit is an exact application | `PROVED_FROM_LOCKED_PAPER9_INPUT` | Corollary 6.3 | fixed orbit only |

## 8. Owner and same-object matrices

### 8.1 Owner matrix

| Record | Exact owner | What this report proves/uses | What it may not inherit |
|---|---|---|---|
| actual right flow and `L_p Z` stabilizer | Deninger source | exact `+t` action input | actual topology, groupoid, convolution |
| actual inherited orbit topology | Paper 9 | nonempty/nontrivial/indiscrete input | standard-circle topology |
| `beta` continuity direction on units | Paper 10 | inherited direction; arrow direction reproved directly | homeomorphism/reflection language |
| `ACT-GRPD-p-a` | Paper 11 construction over the preceding inputs | set-groupoid and one-sided proxy map | standard actual-groupoid framework credit |
| `C_c^HOp` | Paper 11 raw diagnostic | exact value `{0}` | standard convolution/completion meaning |
| `C_qc^glob`, fibre family, `Ind_x` | Paper 11 author-defined direct objects | collapse, operations, fibre and regular formulas | Tu/MW Haar or standard regular terminology |
| `C^full_glob`, `C^red_glob` | Paper 11 transported completion names | identification through group `R` | notation `C^*(G_act)` or `C_r^*(G_act)` |
| `C^*(R)=C_r^*(R) ~= C_0(R)` | Williams group-`R` source | used only after direct transport proof | arithmetic or actual-groupoid credit |
| `G_std` and its `C_c` algebra | standard Hausdorff proxy | strict test-function inclusion | actual-source topology or completion map |
| proxy full crossed product/tensor model | BHM/Williams source ladder | exact source-strength ledger only | actual theorem; reduced groupoid bridge |

### 8.2 Same-object certificate

| Gate | Evidence in this report | Status for P11-6--P11-8 |
|---|---|---|
| `T0` identity | fixed `p,a`, exact `X_{p,a}`, right action, and range-first groupoid | `BOUND` |
| `T1` topology | actual `X_indisc x R` and proxy `S_std x R` kept distinct | `VERIFIED_DISTINCT` |
| `T2` map | `J`, `J^{-1}`, and contravariant `I` directions proved | `VERIFIED` |
| `T3` function convention | global QC, raw HOpen, and standard proxy `C_c` never conflated | `VERIFIED` |
| `T4` fibre measure | exact range fibres and Lebesgue pushforward preserved by `J` | `VERIFIED_TEST_LEVEL` |
| `T5` algebra/completion | convolution and `*` proved; completion extension of `I` withheld | `DENSE_LEVEL_ONLY` |
| `T6` aggregation | every arithmetic conclusion quantified over one fixed orbit; no packet/global promotion | `FIXED_ORBIT_ONLY` |
| `T7` arithmetic promotion | analytic objects erase `p,a,L_p`, action, and stabilizer | `NO_ANALYTIC_SURVIVAL_BASIS` |

## 9. Novelty, standalone, and Route ceilings

### 9.1 Novelty

The Phase-2 exact-package search remains
`SUPPORTED_WITHIN_SEARCH`, with no absolute priority claim. The generic
indiscrete-product/action-blind theorem in Theorem 6.1 receives **no novelty
claim**. The directly proved convention split and strict proxy image are only
components of the exact bounded package; no individual standard ingredient
is relabelled as new.

### 9.2 Standalone status

The Phase-3 mathematical legs required from this report are closed:

```text
P11-6 convention split: PROVED,
P11-7 strict proxy boundary: PROVED at the exact test-function level,
P11-8 action blindness/controls: PROVED.
```

Standalone release is nevertheless **not granted** by this report. It still
requires the integrated P11-1--P11-5 proof tuple, P11-9 deterministic
controls, P11-10 ownership/Route adjudication, independent proof/control
review, composition, manuscript, citation, peer, and release gates. A future
failure at those gates still routes the result to a technical note or merge.

### 9.3 Route evidence ceiling — no verdict

This report creates no Route-A result and no Route-B file. It supplies only
the following evidence for the later typed evaluator:

- the concrete actual groupoid retains the source action and stabilizer as
  host relations, but the global algebra, fibre formula, regular norm, and
  transported completions erase them;
- no analytic-arithmetic credit is inherited merely from the Deninger/Paper-9
  input;
- the HOpen value is diagnostic only;
- the standard proxy is a modeling choice and supplies no actual topology or
  completion credit;
- no determinant, quantization, zero matching, packet/global bridge, or
  Route-B predicate appears in these proofs.

The locked possible `A1` failure and `A2/A3/A4` ceilings must be decided, if
at all, by the later P11-10 Route-A evaluation on a stable integrated
proof/control tuple. They are not serialized here as verdicts.

## 10. Proof integrity statement

All statements were derived from the frozen topology, action, support,
fibre, and source/proxy conventions. Published sources are used only at the
strengths already verified in Phase 2. No standard actual-groupoid `C*`
notation, completion extension of `I`, global priority claim, packet/global
promotion, Route verdict, target-zero data, fit, determinant, or spectral
claim is introduced.

The exact SHA-256 of this report is intentionally computed after the final
byte freeze and reported out of band; embedding a self-hash would change the
bytes being hashed.
