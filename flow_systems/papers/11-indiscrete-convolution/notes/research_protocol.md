# Paper 11 research protocol

Protocol date: **2026-08-14 (Asia/Shanghai)**  
Status: **PHASE 1 PASS — PHASE 2 AUTHORIZED**  
Working title: **Continuous Convolution Collapse on Indiscrete Arithmetic
Orbit Groupoids**

## 1. Trigger and research question

Paper 9 proves that, for every rational prime `p` and every normalized orbit
label `a`, the actual inherited finite-kernel Deninger time orbit
`ACT-ORBIT-p-a` is a nontrivial indiscrete space. Paper 10 proves that all
continuous maps from this unit space into named separated targets are
constant. Neither paper computes the arrow-level convolution object obtained
from the genuine flow action.

The single primary falsifiable question is:

> For every rational prime `p` and normalized orbit label `a`, is the frozen
> map `Phi:g |-> ((x,t) |-> g(t))` a `*`-isomorphism from ordinary group
> convolution `C_c(R)` onto the author-defined global quasi-compact-support
> algebra `C_qc^glob(G_{p,a}^{act})`?

Arrow topology, fibre-measure admissibility, regular/full/reduced
consequences, the Hausdorff-open convention split, proxy strictness, and
arithmetic blindness are separately registered subquestions. The generic
indiscrete-product reduction is not claimed as novelty. A standalone Paper-11
release requires both the exact convention split and strict proxy boundary in
`P11-6`--`P11-7`, plus a documented bounded search with no exact package
precedent. If that gate fails, preserve the mathematics as a technical note or
merge it into the preceding project. Novelty wording is capped at
`SUPPORTED_WITHIN_SEARCH`.

The protocol must not assume that a standard groupoid `C*`-algebra exists.
Non-Hausdorff groupoid conventions differ, and many published constructions
require locally Hausdorff or Hausdorff unit spaces. Paper 11 therefore freezes
each function-space convention and completion as a separately typed object.

## 2. Frozen actual orbit and action

Fix an arbitrary rational prime `p`, put `L_p=log p`, and fix an arbitrary
normalized orbit label `a` in the Paper-9 orbit ledger. Write

```text
X_{p,a} = ACT-ORBIT-p-a
```

with its **actual inherited indiscrete topology**. Its underlying flow set is
`R/L_p Z`. Use additive logarithmic time and write the right action as

```text
x dot t,  x in X_{p,a}, t in R,
```

with stabilizer `L_p Z` at every point. The action and stabilizer are inherited
set/action data. Indiscreteness is the exact Paper-9 topology theorem. No
ordinary-circle topology is imported.

Choose a base point `x_{p,a}^0` and freeze the equivariant orbit chart

```text
theta_{p,a}:R/L_p Z -> X_{p,a},
theta_{p,a}([r])=x_{p,a}^0 dot r,
theta_{p,a}([r]) dot t=theta_{p,a}([r+t]).
```

Thus the additive sign is fixed by the actual right-flow convention. Put
`beta_{p,a}=theta_{p,a}^{-1}` as a set map to the standard circle.

Define, as a `DERIVABLE_NEW_DEFINITION`, the transformation groupoid

```text
G_{p,a}^{act} = X_{p,a} rtimes R
```

with arrow set `X_{p,a} x R` and the product of the actual indiscrete topology
with the usual topology on `R`. Freeze the convention

```text
r(x,t)=x,
s(x,t)=x dot t,
(x,t)(x dot t,u)=(x,t+u),
(x,t)^{-1}=(x dot t,-t).
```

The source owns `X_{p,a}`, its flow action, and the stabilizer. Paper 11 owns
the transformation-groupoid assembly and product arrow topology. This grants
no claim that Deninger or Morishita defined this groupoid or any convolution
completion.

The unit embedding and composable-pair domain are frozen as

```text
unit(x)=(x,0),
G^(2)={((x,t),(x dot t,u)):x in X_{p,a}, t,u in R},
```

where `G^(2)` has the subspace topology from `G x G`. The action is jointly
continuous. The coordinate bijection from `X x R x R` to `G^(2)` is a
homeomorphism only if proved from these exact topologies.

## 3. Separately typed convolution conventions

### 3.1 Global ordinary-continuous quasi-compact-support convention

Freeze the non-Hausdorff conventions

```text
quasi-compact = every open cover has a finite subcover, with no separation or
                closedness clause;
supp_Z(h)      = closure_Z({z:h(z) != 0});
C_qc^glob(G)   = {h in C(G,C):supp_G(h) is quasi-compact}.
```

The word `compact` without qualification remains reserved for the usual
Hausdorff meaning when discussing subsets of `R`. Define

```text
C_qc^glob(G_{p,a}^{act})
```

to be all globally continuous complex functions on the exact arrow topology
whose support is open-cover quasi-compact. This is an author-defined function
space and is not Tu/Muhly--Williams `C_c(G)`.

`P11-1` must separately classify the quasi-compact-neighbourhood property, a
basis of open neighbourhoods with quasi-compact closures, nonexistence of
nonempty quasi-compact open subsets, and nonexistence of nonempty Hausdorff
open subsets. None is abbreviated as unqualified `locally compact`.

For each unit `x`, the range fibre is

```text
(G_{p,a}^{act})^x = {(x,t):t in R}.
```

Define `lambda^x` as the pullback of Lebesgue measure `dt` under
`t -> (x,t)`. Register the author-owned object `GLOB-FIBRE-FAMILY`, never an
unqualified published-framework Haar system. Its contract is:

1. `lambda^x` is a positive Radon measure on the locally compact Hausdorff
   range fibre `G^x`, with `supp(lambda^x)=G^x` in the fibre topology;
2. for every `f in C_qc^glob(G)`, the fibre integral is absolutely finite and
   `x |-> integral_{G^x} f d lambda^x` is continuous on the actual unit;
3. for every arrow `gamma` and licensed `f`, left invariance is

```text
integral_{G^{s(gamma)}} f(gamma eta) d lambda^{s(gamma)}(eta)
  = integral_{G^{r(gamma)}} f(eta) d lambda^{r(gamma)}(eta).
```

Range- and source-fibre measures may be exchanged only through the explicit
inversion pushforward below. Phase 2 decides whether retained standard
frameworks are `APPLICABLE` or `NOT_APPLICABLE`; satisfaction of this author
contract alone does not decide that gate.

Only after those gates pass may convolution and involution on
`C_qc^glob(G)` be defined by

```text
(f*h)(x,t) = integral_R f(x,u) h(x dot u,t-u) du,
f^*(x,t)   = conjugate(f(x dot t,-t)).
```

### 3.2 Hausdorff-open patch convention

For an open Hausdorff subset `U` freeze

```text
C_c(U)={h in C(U,C):supp_U(h) is quasi-compact},
ext_U(h)(gamma)=h(gamma) for gamma in U and 0 otherwise.
```

The zero extension is a raw complex-valued function and need not be globally
continuous. Define the diagnostic object

```text
C_c^HOp(G_{p,a}^{act})
```

as the linear span of these zero-extensions inside the raw function space
`C^G`. Phase 2 must determine
which published non-Hausdorff groupoid frameworks actually use this or a
related convention and which hypotheses they impose. Paper 11 may compute the
frozen diagnostic even if the published framework is inapplicable, but it
must not call that computation a standard groupoid `C*`-algebra theorem.

### 3.3 Transported completions

If `C_qc^glob(G_{p,a}^{act})` is proved `*`-isomorphic to a familiar group
convolution algebra, define separately:

```text
C^full_glob(G_{p,a}^{act}) = completion in the transported universal norm,
C^red_glob(G_{p,a}^{act})  = completion in the explicitly proved regular norm.
```

Freeze the source-fibre regular record:

```text
G_x=s^{-1}(x)={(x dot (-t),t):t in R},
lambda_x=(inversion)_* lambda^x,
vartheta_x(t)=(x dot (-t),t),
H_x=L^2(G_x,lambda_x),
U_x:H_x->L^2(R,dt),  (U_x xi)(t)=xi(vartheta_x(t)),
[Ind_x(f)xi](gamma)
  = integral_{G_x} f(gamma eta^{-1}) xi(eta) d lambda_x(eta),
||f||_{red,glob}=sup_x ||Ind_x(f)||.
```

`P11-5` must prove `vartheta_x` measure preserving, boundedness and the
`*`-representation identities, and

```text
[U_x Ind_x(Phi(g)) U_x^{-1} xi](t)
  = integral_R g(t-u)xi(u)du.
```

Define the full norm only by transport,

```text
||Phi(g)||_{full,glob}=||g||_{C*(R)},
```

where the group norm is the supremum over integrated strongly continuous
unitary representations of `R`. Freeze
`Fourier(g)(xi)=integral_R g(t)exp(-it xi)dt`. Equality of full and reduced
norms may be attributed only to amenability of the group `R` after source
verification.

These are author-defined completions of the frozen global algebra. The names
`C^*(G_{p,a}^{act})` and `C_r^*(G_{p,a}^{act})` are forbidden unless a Phase-2
source theorem applies to this exact non-locally-Hausdorff object and exact
function convention.

## 4. Standard-circle proxy

Freeze separately

```text
S_p^std = R/L_p Z with its ordinary Hausdorff circle topology,
G_p^std = S_p^std rtimes R with its usual transformation-groupoid topology.
```

Give `S_p^std` the signed right action `[r] dot t=[r+t]`, let `mu_p` be its
normalized Haar probability measure, and freeze the crossed-product
automorphism convention

```text
alpha_t(h)([r])=h([r+t]).
```

Any retained source using the inverse pullback convention must be translated
explicitly rather than silently changing this sign. The chart above
defines the set-groupoid isomorphism

```text
J_{p,a}:G_{p,a}^{act}->G_p^std,
J_{p,a}(x,t)=(beta_{p,a}(x),t).
```

Test that `J` is not continuous and `J^{-1}` is continuous. Define the
contravariant actual-to-proxy function map `I(f)=f o J^{-1}`. Compact-support
preservation, fibre-measure compatibility, convolution, and involution must
all pass before `I` is called a `*`-monomorphism.

The following is only a Phase-2 source-gated proxy candidate:

```text
C(S_p^std) rtimes_full R
  ?~= C*(L_p Z) tensor K(L^2(S_p^std,mu_p)).
```

The full dense algebra, full crossed product, reduced crossed product, Green
Morita equivalence, stable isomorphism, and any actual isomorphism are distinct
claims. Full/reduced equality is source-gated through amenability of `R`.
This is a **proxy candidate** subject to exact Phase-2 checks. It
may not be promoted to the actual groupoid. Conversely, any actual global
function pulled back to the standard proxy must be identified only with its
exact image subalgebra, not with the full proxy convolution algebra.

## 5. Registered theorem targets

New theorem targets use IDs `P11-1`--`P11-10`. The same-object transport
certificate keeps the separate reserved names `T0`--`T7`.

### P11-1 — arrow topology and separation

Compute all open and closed subsets of `G_{p,a}^{act}`. Prove for every subset
`K0` that `K0` is open-cover quasi-compact iff its time projection is compact
in `R`. Determine both local quasi-compact variants frozen above, second
countability, `T0`, Hausdorffness, and whether any nonempty quasi-compact or
Hausdorff open subset exists. Prove continuity of range, source,
multiplication, inverse, and units under the frozen convention. Every claim is
quantified over all rational primes and all orbit labels.

### P11-2 — arrow Borel and standard-target maps

Name `pi_R:G->R`, `pi_R(x,t)=t`, and `B(G)=sigma(tau_G)`. Prove separately:

1. for every `T0` topological space `Y`, continuous `F:G->Y` factors uniquely
   as `F=g o pi_R` with continuous `g:R->Y`, and conversely;
2. for every countably separated measurable `(Y,Sigma_Y)`, measurable `F`
   factors uniquely through a measurable
   `g:(R,B(R))->(Y,Sigma_Y)`, and conversely.

Test `B(G)={X x B:B in B(R)}` and whether the nontrivial arrow measurable
space itself is countably separated. This is an arrow-space theorem, not a
reissue of Paper 10's unit-space record.

### P11-3 — global continuous quasi-compact-support collapse

Test whether every `f in C_qc^glob(G_{p,a}^{act})` has a unique form

```text
f(x,t)=g(t),  g in C_c(R),
```

and prove both directions of continuity and
`supp_G(Phi g)=X x supp_R(g)`. The support proof must use the frozen
open-cover quasi-compact convention and prove the converse by projection.

### P11-4 — fibre measure and convolution

Directly verify `GLOB-FIBRE-FAMILY`, all integral domains, continuity, and left
invariance. If valid, prove closure, associativity, the `*` identities, and
support control, and prove that the map

```text
Phi:g |-> ((x,t) |-> g(t))
```

intertwines convolution and involution with the usual `C_c(R)` operations.
No modular function or action sign may be inserted from memory; derive it from
the frozen groupoid convention.

### P11-5 — regular representations and transported completions

Prove the frozen source-fibre/inversion-measure representation at every unit.
Test whether all unit records reduce under `Phi` to the displayed left regular
representation of `R`. Only then identify the reduced norm. Separately source
the group universal norm, amenability step, and Fourier identification. State
exactly which completion is author-defined and which theorem belongs to `R`.

### P11-6 — Hausdorff-open patch and applicability no-go

Compute `C_c^HOp(G_{p,a}^{act})` in the frozen raw-function owner. Audit the
hypotheses of the retained
locally-Hausdorff/non-Hausdorff groupoid frameworks. Classify each as
`APPLICABLE`, `NOT_APPLICABLE`, or `DIAGNOSTIC_ONLY`; absence of a published
framework is not the same as nonexistence of every possible convolution
construction.

### P11-7 — actual/proxy direction and strictness

Prove all algebraic, topological, fibre-measure, and `*`-map properties of the
frozen equivariant `J` and `I`. Determine whether the image is precisely the
unit-coordinate-constant proxy subalgebra and exhibit a licensed proxy
function outside it. Keep proxy dense/full/reduced/Morita/isomorphism records
and the transported actual completion in separate ledgers. Any extension of
`I` to a completion needs an independent boundedness/isometry proof.

### P11-8 — arithmetic blindness and controls

First state and test the general lemma for every nonempty indiscrete space `X`
and every jointly continuous right `R`-action, including trivial and
nontransitive actions. Then apply it to the rational-Witt owner. Determine
whether the abstract global `*`-algebra, fibre formula, regular norm, or
transported completion retains `p`, `a`, `L_p`, the action, or the stabilizer.
Vary label and positive period as independent control axes; include composite,
randomized, and non-arithmetic labels. A construction that works unchanged is
a `PROVES_TOO_MUCH` control, not arithmetic credit.

### P11-9 — deterministic reproduction

Implement finite exact controls for topology, support, convolution,
involution, regular matrices, patch-convention collapse, proxy strictness,
sign errors, arbitrary periods/labels, implementation hashes, and two fresh
byte-identical generations. Controls are witnesses, not proofs of infinite or
continuous theorems.

### P11-10 — ownership and Route adjudication

Evaluate separately the actual transformation groupoid, global continuous
algebra, Hausdorff-open diagnostic, transported completion, and standard
proxy. The actual action's set-theoretic stabilizer must not be credited to an
algebra that erases it. Expected ceilings to test, not assume:

- actual groupoid: source host relation only; do not reissue the immutable
  Paper-9/Stage-9 orbit record;
- concrete global algebra, its abstract isomorphism class, and each completion
  receive separate A0 decisions; no inherited analytic-arithmetic A0 credit;
- global convolution/completion: `A1_FAIL` if action, `p`, and `L_p` vanish;
- standard proxy: modeling choice, no source-topology credit;
- all new records: `A2/A3/A4_FAIL` absent a same-object determinant or
  quantization;
- Route B false and no Route-B YAML.

## 6. Primary hypotheses and falsifiers

### H1 — global arrow collapse

The global ordinary-continuous quasi-compact-support algebra is exactly
`C_c(R)`.

**Falsifier:** a globally continuous quasi-compact-support arrow function that
varies with the unit coordinate, or a `g in C_c(R)` whose pullback fails the
frozen support condition.

### H2 — exact convolution collapse

The explicit fibre-family/convolution/involution ledger transports to ordinary group
convolution on `R` and is independent of `p`, `a`, and `L_p`.

**Falsifier:** a valid term depending on the orbit coordinate or stabilizer in
the exact convolution, involution, or regular norm.

### H3 — convention split

The arrow space has no nonempty Hausdorff open subset, so the frozen
Hausdorff-open patch diagnostic is zero even though the global ordinary
algebra is nonzero.

**Falsifier:** a nonempty Hausdorff open arrow subset or a nonzero legal patch
generator.

### H4 — proxy strictness

The actual global algebra pulls into a proper unit-coordinate-constant
subalgebra of the standard-circle proxy algebra.

**Falsifier:** equality of the two function spaces under the exact set map, or
failure of the claimed continuity direction.

## 7. Same-object certificate

| Gate | Required evidence |
|---|---|
| `T0` identity | exact `ACT-ORBIT-p-a`, action, and groupoid convention |
| `T1` topology | actual product arrow topology versus standard proxy topology |
| `T2` map | exact direction for identities, pullbacks, and `Phi` |
| `T3` function convention | global ordinary, Hausdorff-open patch, or proxy `C_c` named |
| `T4` fibre measure | exact range/source fibre, measure, support, invariance |
| `T5` algebra/completion | convolution sign, involution, norm, and representation owner |
| `T6` aggregation | fixed orbit only; no packet/global upgrade without a bridge |
| `T7` arithmetic promotion | surviving `p`, repetition, period, amplitude, and phase independently proved |

Failure at a gate blocks downstream credit but does not mutate Paper 9 or
Paper 10.

## 8. Deterministic adversarial controls

The implementation must include at least:

1. finite nontrivial indiscrete unit sets with trivial, transitive, and
   nontransitive actions;
2. exact enumeration of product-topology opens and Hausdorff-open subsets;
3. continuous functions to finite complex meshes, detecting unit-coordinate
   dependence;
4. support closure and projection checks;
5. finite cyclic-time convolution and involution against group convolution;
6. an intentionally wrong source/range or sign convention that fails;
7. unit regular matrices for several base units and equality checks;
8. a discrete/standard proxy with strictly more continuous functions;
9. prime, composite, randomized, and arbitrary labels crossed independently
   with several positive periods;
10. implementation-file hash verification, forbidden-artifact scan, verify-only
    mode, and two fresh byte-identical generations.

## 9. Source and novelty protocol

Phase 2 must verify primary or authoritative sources for:

- transformation-groupoid conventions and Haar systems;
- `C_c` conventions for locally Hausdorff and non-Hausdorff groupoids;
- assumptions behind full/reduced groupoid `C*`-algebras;
- crossed products for the transitive standard-circle action;
- `C^*(R)=C_r^*(R)` and Fourier identification;
- Deninger/Paper-9 action, stabilizer, and actual topology ownership.

The novelty search must distinguish generic facts about indiscrete spaces,
generic crossed products, and Paper 10's unit-observable collapse from the
exact rational-Witt arrow-convolution/convention-split package. A bounded
negative search supports only `SUPPORTED_WITHIN_SEARCH`.

Retained full texts require exact manifestation, physical-page locator,
preflight, SHA-256, and public-redistribution classification. Retained source
PDFs remain local-only unless an exact-manifestation redistribution licence is
documented.

## 10. Stop rules

Stop or version-amend before Phase 2/3 if:

- an unqualified `C_c(G)` or `C^*(G)` conflates conventions;
- local Hausdorffness is assumed from local quasi-compactness;
- compact support is evaluated using a different closure convention;
- range- and source-fibre measure conventions are mixed;
- the standard-circle proxy supplies actual topology or operator credit;
- the fixed-orbit theorem is promoted to the packet/global source;
- the action stabilizer is claimed to survive without appearing in the exact
  algebra/norm;
- target zeros, fitting, determinant claims, or Route B enter the design.

## 11. Phase gates

1. Three independent Phase-1 methodology/domain/source reviews.
2. Versioned amendment and exact-byte re-lock for any Major/Critical finding.
3. Phase-2 source, convention, and bounded novelty audit, including databases,
   date range, nearest precedent, `last_searched_at`, and the standalone
   release gate in Section 1.
4. Phase-3 proofs plus deterministic controls.
5. Independent theorem/control review.
6. Typed Route-A evaluation; no Route-B file unless independently justified.
7. Composition blueprint, manuscript, citation, peer, and release audits.

No downstream object inherits a verdict from a different topology, function
convention, fibre measure, completion, or aggregation owner.

## 12. Integrity disclosure

This protocol was AI-assisted under the ARS research-integrity workflow. It
contains no Riemann-zero data, fitted parameter, hidden target, random search,
human/animal/personal data, external upload, or pre-certified theorem result.
Final mathematical and publication responsibility remains with the human
author.
