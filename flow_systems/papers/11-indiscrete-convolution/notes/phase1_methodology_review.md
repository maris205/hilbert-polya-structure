# Paper 11 Phase-1 methodology review

Review date: **2026-08-14 (Asia/Shanghai)**  
Reviewer role: **independent methodology reviewer (ARS Phase-1 gate)**  
Scope: **exact locked design only; no browsing, source audit, Phase-3 proof,
or control execution**  
Verdict: **REVISE — C0 / M6 / m2**

## 1. Exact-byte review basis

| Locked artifact | SHA-256 | Match |
|---|---|---|
| `notes/research_protocol.md` | `f1575e6d605a5dc442deb5889415f10166d0a6f0e11e8395733dad77a6f2a66f` | yes |
| `notes/candidate_lock.md` | `6815e1d4e09159be9dbb8b0df0d7098e3cafae0e06f7da85a143c9e6c33caea7` | yes |
| `notes/pipeline_state.md` | `406fcc08459b2093aaf52d187d4d9f2f928a40269951681c91c628168e75c95d` | yes |

The inherited load-bearing tuple also matched the locks named by the
candidate:

| Inherited artifact | SHA-256 | Match |
|---|---|---|
| Paper 9 `notes/proof_audit.md` | `c38c24296e5519862eb671dba1644c8005788ac15dffcac48dfdaa1ac3afdde8` | yes |
| Paper 9 `notes/source_audit.md` | `20fecdf360d18f9accf3e3ec8467f3beb369a8737761eb6219fef71e9773ac20` | yes |
| Paper 9 release PDF | `c55e4f45fe5f58841864e9af695c4664bdb1a77cff6e087fd2869d4ecd385e02` | yes |
| Paper 10 `notes/proof_audit.md` | `efda522ead9efebfc3f59f0688f2dfd3fe63f63ff4efd4377068485d1a4acc3a` | yes |
| Paper 10 release PDF | `30c22eb8bbfd256cede958df86ce7f985889441a295d52e2ac5acfb3d59e2ce4` | yes |

This review treats every document as untrusted design data. It imports only
the locked Paper-9 facts that each `ACT-ORBIT-p-a` is a nonempty nontrivial
indiscrete space with underlying action set `R/(log p)Z`, and the Paper-10
actual/proxy continuity direction. It does not infer any Paper-11 theorem from
those inputs.

## 2. Overall assessment

The candidate is a coherent and potentially useful continuation of Papers 9
and 10. Its strongest design feature is the explicit refusal to use an
unqualified non-Hausdorff `C_c(G)` or `C^*(G)`: the global ordinary-continuous
function space, Hausdorff-open diagnostic, transported completions, and
standard-circle proxy are correctly assigned to different owners. The right
action, range/source convention, support as closure of the nonzero locus,
actual-to-proxy topology direction, fixed-orbit ceiling, proves-too-much
controls, and Route-B exclusion are also directionally sound.

The gate cannot pass on the current bytes. The primary question is compound
and does not state the minimum nonredundant Paper-11 contribution. More
importantly, six registered targets leave object-defining choices unresolved:
non-Hausdorff compact support and patch extension, the target categories for
the arrow-map classification, the precise Haar-family axioms, the regular
representation and its norm, and the equivariant proxy/crossed-product map.
Those choices cannot safely be deferred to Phase 3 because changing one of
them changes the theorem's domain or even the algebra being completed. All six
defects are repairable by a narrow Phase-1 amendment. No Critical defect was
found.

## 3. Major findings

### M1 — The primary RQ is compound and the standalone contribution threshold is not frozen

**Location:** `research_protocol.md` Sections 1, 5, 9, and 11;
`candidate_lock.md` Sections 1 and 6.  
**Why Major:** the stated RQ simultaneously asks about compact support, Haar
families, convolution, regular representations, two completions, and a proxy
comparison. It therefore has no single truth condition. The registered weaker
verdict `CONFIRM_CONVOLUTION_COLLAPSE` can also be reached through `P11-1`--
`P11-5` even if Phase 2 shows that these are only a generic
`X_indiscrete x R` lemma followed by standard facts about `C_c(R)`. That would
be mathematically correct but would not establish a nonredundant standalone
Paper-11 contribution rather than an extension or appendix to Paper 10.
Absence of an exact rational-Witt precedent is not, by itself, evidence that
an immediate generic corollary is a publishable novelty.  
**Minimum repair:** replace the primary RQ by one falsifiable question, for
example:

> For every rational prime `p` and normalized orbit label `a`, does the frozen
> map `Phi:g |-> ((x,t) |-> g(t))` give a `*`-isomorphism from the ordinary
> convolution algebra `C_c(R)` onto
> `C_c^glob(G_{p,a}^{act})`?

Move topology/Haar admissibility, regular/full/reduced consequences, the
Hausdorff-open convention split, proxy strictness, and arithmetic blindness
into separately bound subquestions. Label the general indiscrete-product
lemma as standard and identify the exact source-owned arithmetic application
as the application, not as generic-topology novelty. Add a Phase-2
publication gate: a standalone release requires both an exact convention
split/strict proxy boundary (`P11-6`--`P11-7`) and a bounded search that finds
no exact package precedent. If that gate fails, preserve the mathematics but
merge it into the prior paper or release it explicitly as a technical note.
Any novelty wording remains `SUPPORTED_WITHIN_SEARCH`, with databases, date
range, nearest prior work, and `last_searched_at` recorded.

### M2 — Compactness, global support, and the Hausdorff-open patch convention are not yet one exact object

**Location:** `research_protocol.md` Sections 3.1, 3.2, 5 (`P11-1`, `P11-3`,
`P11-6`), 6 (H1/H3), and 10; `candidate_lock.md` Sections 3--4.  
**Why Major:** in a non-Hausdorff space, “compact,” “compact support,” and
“zero-extension from a Hausdorff open subset” have convention-sensitive
meanings. The global owner defines ambient topological support, but it does
not say whether compactness means the open-cover property without a
Hausdorff/closedness requirement. The patch owner does not specify whether
support is closed in the patch or the arrow space, whether the zero extension
must be globally continuous, or even the ambient vector space in which the
span is taken. The expected zero patch algebra may be robust, but an
undefined diagnostic cannot be compared faithfully with a published
non-Hausdorff convention. “Locally quasi-compact” is likewise not testable
until its exact local definition is stated.  
**Minimum repair:** freeze, before source audit:

```text
quasi-compact = every open cover has a finite subcover, with no separation
                or closedness clause;
supp_Z(h)      = closure_Z({z:h(z) != 0});
C_c^glob(G)    = {h in C(G,C):supp_G(h) is quasi-compact};
C_c(U)         = {h in C(U,C):supp_U(h) is quasi-compact};
ext_U(h)(g)    = h(g) for g in U and 0 otherwise;
C_c^HOp(G)     = span_C{ext_U(h)} inside the raw function space C^G,
                with no global-continuity claim unless separately proved.
```

If a different patch convention is intended, give it a different owner name
and compute it separately. Define “locally quasi-compact” explicitly (for
example, a neighbourhood basis of quasi-compact neighbourhoods) and do not
equate it with local Hausdorffness or any convention that builds Hausdorffness
into “locally compact.” Register the exact identities to be proved,
`supp_G(Phi g)=X_{p,a} x supp_R(g)` and
`supp_G(Phi g)` quasi-compact iff `supp_R(g)` is compact, with the reverse
implication proved by projection as already requested.

### M3 — `P11-2` has no frozen target category or factorization contract

**Location:** `research_protocol.md` Section 5 (`P11-2`) and Section 7
(`T1`--`T3`); no corresponding exact target signature appears in
`candidate_lock.md`.  
**Why Major:** “named Hausdorff/countably-separated targets” names neither a
list of targets nor a universal class. Continuous maps and Borel-measurable
maps also belong to different categories. Without exact source and target
sigma-algebras and quantifiers, the classification cannot be falsified, and
it can accidentally inherit the unit-space result of Paper 10 without adding
an arrow-coordinate statement.  
**Minimum repair:** name the time projection
`pi_R:G_{p,a}^{act}->R`, define
`B(G)=sigma(tau_G)`, and register two separate factorization theorems:

1. for every `T0` topological space `Y`, a continuous
   `F:G_{p,a}^{act}->Y` factors uniquely as `F=g o pi_R` with `g:R->Y`
   continuous, and conversely;
2. for every countably separated measurable space `(Y,Sigma_Y)`, a
   `B(G)`/`Sigma_Y`-measurable `F` factors uniquely as `F=g o pi_R` with
   `g:(R,B(R))->(Y,Sigma_Y)` measurable, and conversely.

If only particular targets are intended, enumerate them instead. State
separately the expected arrow Borel identity
`B(G)={X_{p,a} x B:B in B(R)}`. Paper 10 remains the unit-space input; the
time-projection factorization is the new arrow-level target.

### M4 — The “explicitly frozen” Haar family still lacks its exact axioms and test domain

**Location:** `research_protocol.md` Sections 3.1, 5 (`P11-4`), 7 (`T4`), and
10; `candidate_lock.md` Sections 3--4.  
**Why Major:** the protocol mentions fibre support, continuity, and left
invariance but does not state their formulas, the measure class, or the test
function domain. In a non-locally-Hausdorff groupoid these details determine
whether “Haar system” is a standard sourced term or only an author-defined
family. They also determine the convolution sign and which integrals are
licensed.  
**Minimum repair:** define a typed `GLOBAL-HAAR-FAMILY` contract, without yet
calling it a published-framework Haar system:

- `lambda^x` is a positive Radon measure on the locally compact Hausdorff
  range fibre `G^x`, with `supp(lambda^x)=G^x` in the fibre topology;
- for every `f in C_c^glob(G)`, the integral is absolutely finite and
  `x |-> integral_{G^x} f d lambda^x` is continuous on the actual unit space;
- for every arrow `gamma` and every licensed test function `f`, left
  invariance is the exact equality
  `integral_{G^{s(gamma)}} f(gamma eta)d lambda^{s(gamma)}(eta)
   = integral_{G^{r(gamma)}} f(eta)d lambda^{r(gamma)}(eta)`;
- range-fibre and source-fibre measures are never interchanged without an
  explicit inversion pushforward.

After these gates, require closure of `C_c^glob(G)` under the displayed
convolution and involution, associativity, the `*` identities, and support
control. These may be proved efficiently through `Phi`, but they may not be
assumed merely because the formulas resemble the group case. Phase 2 must
then classify the contract as author-defined or as an exact instance of a
retained source framework.

### M5 — The regular representation and the full/reduced norm domains are underspecified

**Location:** `research_protocol.md` Sections 3.3 and 5 (`P11-5`), Section 7
(`T5`), and Section 10; `candidate_lock.md` Sections 3--4.  
**Why Major:** “the exact regular representation” is postponed to the proof,
but a range-Haar convention admits several equivalent-looking source/range
fibre formulas with opposite translation signs. Until the fibre, pushed
measure, integrated formula, and representation class are fixed, “left
regular representation,” “regular norm,” and “universal norm” do not name
testable objects. In particular, the supremum over all algebraic
`*`-representations of a raw convolution algebra must not silently replace
the universal group norm.  
**Minimum repair:** freeze one convention such as

```text
G_x       = s^{-1}(x);
lambda_x  = inversion-pushforward of lambda^x;
theta_x(t)= (x dot (-t),t):R -> G_x;
H_x       = L^2(G_x,lambda_x);
(pi_x(f)xi)(gamma)
          = integral_{G_x} f(gamma eta^{-1})xi(eta)d lambda_x(eta);
||f||_red = sup_x ||pi_x(f)||.
```

Require a direct proof that `theta_x` is measure preserving, `pi_x` is a
bounded `*`-representation, and under `Phi` the formula is the chosen left
regular representation of `R` rather than its unannounced right/reflected
variant. Define the transported full norm explicitly by

```text
||Phi(g)||_full := ||g||_{C*(R)},
```

where `||g||_{C*(R)}` is the supremum over integrated strongly continuous
unitary representations of `R`. Keep this author-defined transported norm
distinct from a universal norm over a standard groupoid algebra. Freeze the
Fourier character convention (for example
`hat g(xi)=integral g(t)e^{-it xi}dt`) before identifying either completion
with `C_0(Rhat)`, and source separately the amenability/full=reduced step.

### M6 — The proxy comparison is not yet an equivariant arrow map, and its crossed product is untyped

**Location:** `research_protocol.md` Sections 4, 5 (`P11-7`), 7 (`T2`, `T5`),
9, and 10; `candidate_lock.md` Sections 5 and 8.  
**Why Major:** an “identity after choosing a parameter bijection” is
insufficient for an algebra comparison. The chosen unit bijection must be
action equivariant for the induced arrow bijection to preserve multiplication,
inverse, Haar measure, and convolution. Topological continuity alone would
only produce a function pullback, not a convolution `*`-homomorphism. The
displayed `C(S_p^std) rtimes R ~= C^*(L_p Z) tensor K` also leaves full versus
reduced crossed product, action sign, Haar normalization, Morita equivalence
versus actual/stable isomorphism, and completion-map extension unresolved.
Those are different theorem strengths.  
**Minimum repair:** freeze the Paper-10 basepoint map as an action-equivariant
set bijection

```text
beta_{p,a}(x dot t)=beta_{p,a}(x)+t mod L_p,
J_{p,a}(x,t)=(beta_{p,a}(x),t).
```

Register `J` as a set-groupoid isomorphism, test that
`J:G_act->G_std` is not continuous and `J^{-1}:G_std->G_act` is continuous,
and define the actual-to-proxy function map exactly by
`I(f)=f o J^{-1}`. Require compact-support preservation, Haar compatibility,
and convolution/involution intertwining before calling `I` a `*`-monomorphism;
then prove that its image is precisely the unit-coordinate-constant
subalgebra and exhibit one compactly supported proxy function outside it.

For the completion ledger, split the proxy dense algebra, full crossed
product, and reduced crossed product. Freeze the induced action convention.
Phase 2 should first source the exact Green/imprimitivity or transitive-
groupoid statement and record whether it yields Morita equivalence, stable
isomorphism, or an actual isomorphism; do not place the strongest `~=` in the
lock before that audit. Any extension of `I` to a completion requires its own
boundedness/isometry proof and receives no actual-topology credit.

## 4. Minor findings

### m1 — The composable-pair and unit-map topologies should be frozen explicitly

`P11-1` asks for continuity of multiplication and units, but the lock does not
name the unit embedding or the topology on the multiplication domain. Add

```text
u(x)=(x,0),
G^(2)={((x,t),(x dot t,u)):x in X, t,u in R}
```

with `G^(2)` carrying the subspace topology inherited from `G x G`, and state
that the right action is jointly continuous. The proof may then use the
coordinate bijection `X x R x R -> G^(2)`, but it must verify that this is a
homeomorphism under the frozen topologies rather than using it implicitly.

### m2 — The label-neutrality controls currently confound the label and period axes

`P11-8` requests arbitrary positive periods, composite labels, and randomized
labels, but no control object says whether a composite label `n` forces
`L=log n` or is merely a tag. Freeze the analytic controls as
`X_L=R/LZ` with the indiscrete topology for independently chosen `L>0`.
Then vary labels while holding `L` fixed and vary `L` while holding the label
fixed. Declare any `label -> period` rule as external data. The finite cyclic
controls in `P11-9` may test sign, involution, matrices, and label neutrality,
but must retain the existing disclaimer that they do not certify Lebesgue
integration, continuum support, or the infinite-dimensional norm.

## 5. Requested-domain audit

| Domain | Methodology verdict | Reason |
|---|---|---|
| Research question | **MAJOR REVISION** | One compound RQ has several truth conditions; M1 supplies a single primary theorem and bound subquestions. |
| Nonredundancy versus Papers 9/10 | **MAJOR REVISION** | Arrow convolution is a real scope delta, but the generic lemma is immediate enough that a standalone convention-split/strict-proxy threshold must be predeclared. |
| Prime/orbit quantifiers | **PASS** | The lock correctly fixes arbitrary `p` and arbitrary normalized `a` and forbids packet/global promotion. |
| Transformation-groupoid convention | **PASS WITH MINOR REVISION** | Range/source/product/inverse and right-action sign are exact; `G^(2)` and the unit embedding need m1. |
| Arrow topology/separation | **PASS WITH REVISION** | The target is answerable; the non-Hausdorff meaning of local quasi-compactness must be fixed in M2. |
| Arrow Borel/map classification | **MAJOR REVISION** | The target classes and factorization arrows are missing (M3). |
| Global `C_c` convention | **MAJOR REVISION** | Ambient support is named, but compactness and exact equivalence need M2. |
| Hausdorff-open patch convention | **MAJOR REVISION** | Patch support, zero extension, ambient span, and continuity status are not fixed (M2). |
| Haar family/convolution | **MAJOR REVISION** | Measure class, full-support formula, test domain, and left-invariance equation need M4. |
| Regular representation/reduced norm | **MAJOR REVISION** | Fibre, inversion-pushed measure, formula, and norm supremum need M5. |
| Full transported completion/Fourier | **MAJOR REVISION** | The representation class and Fourier normalization need M5; author-defined ownership is otherwise correct. |
| Actual/proxy map direction | **MAJOR REVISION** | The topological direction is correct, but algebra transport requires an equivariant arrow map (M6). |
| Proxy crossed product | **MAJOR REVISION** | Full/reduced and Morita/stable/actual-isomorphism strengths must be separated (M6). |
| Arithmetic blindness controls | **PASS WITH MINOR REVISION** | Proves-too-much logic is strong; label and period axes need m2. |
| Deterministic controls | **PASS AT DESIGN LEVEL** | Positive/negative sign, topology, support, regular-matrix, proxy, hash, and two-generation controls are adequate witnesses and are not called proofs. |
| Stop rules | **PASS WITH REVISION** | Topology/function/fibre/completion splice rules are strong; add the M1 nonredundancy stop. |
| `T0`--`T7` owner certificate | **PASS WITH REVISIONS** | The certificate has the right dimensions; M2--M6 make its function, measure, norm, and map entries executable. |
| Route-A ceiling | **PASS** | Owners are separated, no A1 credit is inherited, A2--A4 remain failed absent same-object evidence, and proves-too-much is treated negatively. |
| Route B | **PASS / FALSE** | No A4-ready operator exists; no Route-B YAML is licensed. |
| Integrity and phase discipline | **PASS** | No source theorem, novelty result, proof, determinant, fitted target, zero data, or standard groupoid completion is pre-certified. |

## 6. Minimal amendment and exact-byte re-lock checklist

1. Replace the compound primary RQ with the exact `Phi` `*`-isomorphism
   question; bind the remaining topics as subquestions and add the standalone
   nonredundancy stop.
2. Freeze open-cover compactness, ambient and patch support, zero extension,
   the ambient patch span, and local quasi-compactness.
3. Freeze `pi_R`, the arrow Borel sigma-algebra, and the universal `T0` and
   countably-separated factorization contracts.
4. Add the exact global Haar-family axioms, function domain, left-invariance
   formula, closure, associativity, and involution gates.
5. Add the source-fibre regular representation, inversion-pushed measure,
   reduced norm, transported universal group norm, and Fourier convention.
6. Freeze the action-equivariant `beta`, arrow map `J`, function pullback
   `I`, and proxy full/reduced/Morita-isomorphism distinctions.
7. Add the explicit unit/composable-pair topology and decouple labels from
   positive-period controls.
8. Record the amendment as a new artifact, recompute all three lock hashes,
   and obtain independent exact-byte methodology/devil/source-feasibility
   PASS reports before authorizing Phase 2.

No browsing, source download, proof construction, implementation, Route YAML,
or manuscript work is needed to close this methodology review.

## 7. Gate decision

```text
phase1_methodology_gate: REVISE
critical: 0
major: 6
minor: 2
phase2_authorized: false
route_b_yaml_authorized: false
```

The central direction remains viable. The required amendment narrows and
types the design; it does not change the actual orbit, action, topology, or
the intended negative arithmetic conclusion.

---

## 8. Exact-byte methodology re-lock — amended v1

Re-lock date: **2026-08-15 (Asia/Shanghai)**  
Scope: **amended four-artifact tuple only; no browsing, source audit,
Phase-3 proof, control execution, Route evaluation, or active-lock edit**  
Verdict: **REVISE — C0 / M0 / m2**

### 8.1 Amended tuple

| Artifact | SHA-256 | Exact match |
|---|---|---|
| `notes/research_protocol.md` | `bc40e307746c1d05808d8288dba0b0a315c30e60d7983989ca42ebe913ecb922` | yes |
| `notes/candidate_lock.md` | `a82a96957f5d58b0925e96395ea2994acb9dece9e24f60f286b7ea714cdb7c3e` | yes |
| `notes/pipeline_state.md` | `003bd5f96e84a966d689b467ef4247dc733ec1994b09877c9632c9735ae99c4a` | yes |
| `notes/phase1_design_amendment.md` | `7d2c2c7eb041a530ff4da6f7090d85053b067243d7a2ab445b4b4cba9cc2dc64` | yes |

The first three hashes equal the content tuple recorded in amendment v1. The
amendment hash is separately bound by this re-lock. No active artifact changed
during the review.

### 8.2 Original-finding closure audit

| Original finding | Re-lock result |
|---|---|
| M1 — compound RQ / nonredundancy | **CLOSED:** Section 1 now asks only the exact `Phi:C_c(R)->C_qc^glob(G)` `*`-isomorphism question. The remaining topics are subquestions; generic indiscrete topology receives no novelty claim; standalone status requires `P11-6`--`P11-7` plus the dated bounded-search gate, otherwise technical-note/merge status. |
| M2 — quasi-compact support / HOpen convention | **CLOSED:** open-cover quasi-compactness, ambient support, `C_qc^glob`, patch support, raw zero-extension, ambient raw-function span, the two local predicates, and projection-based support/compactness tests are separately frozen. No local-Hausdorff inference is introduced. |
| M3 — arrow Borel / target categories | **CLOSED:** `pi_R`, `B(G)`, universal `T0` continuous factorization, countably-separated measurable factorization, converses, uniqueness, and the exact arrow-Borel identity are registered. |
| M4 — fibre-family/Haar contract | **CLOSED:** `GLOB-FIBRE-FAMILY` now fixes positive fibre Radon measures, full fibre support, absolute integrability, unit-variable continuity, the exact range-fibre left-invariance formula, and inversion-only source-fibre transport. Published “Haar system” terminology remains Phase-2 source-gated. |
| M5 — regular/full/reduced domains | **CLOSED AT OBJECT LEVEL:** source fibre, inversion-pushed measure, `vartheta_x`, `H_x`, `Ind_x`, the reduced supremum, transported group-full norm, strongly-continuous-unitary representation class, Fourier sign, and amenability ceiling are frozen. A new dangling-symbol defect remains below; it does not reopen the original Major object/domain defect. |
| M6 — equivariant proxy / crossed-product split | **CLOSED AT OBJECT LEVEL:** the basepoint chart is `+t` equivariant; `J`, its two topology directions, `I`, support/measure/`*` gates, dense/full/reduced ledgers, Morita/stable/actual-isomorphism strengths, and completion-extension gate are separated. Two proxy notations remain undefined below; they do not reopen the original Major actual/proxy splice defect. |
| m1 — units and composable pairs | **CLOSED:** `unit(x)`, `G^(2)`, its subspace topology, joint action continuity, and the coordinate-homeomorphism proof obligation are explicit. |
| m2 — label/period control confounding | **CLOSED:** labels and positive periods are independent axes; trivial, transitive, and nontransitive actions are included; finite controls remain witnesses only. |

The amendment also sharpens the Route split: actual host, concrete global
algebra, abstract isomorphism class, transported completions, HOpen diagnostic,
and proxy require separate records. No analytic-arithmetic A0 coordinate, A1
orbit credit, A2--A4 result, or Route-B permission is inherited.

### 8.3 New minor drift findings

#### mR1 — The regular-equivalence formula uses an undefined `U_x`

**Location:** amended `research_protocol.md` Section 3.3, displayed
regular-equivalence target; `candidate_lock.md` Section 4.  
`vartheta_x` and `H_x` are defined, but `U_x` occurs only in
`U_x Ind_x(Phi(g)) U_x^{-1}` and has no domain, codomain, or action. The
intended unitary is recoverable, so this is not a Major representation-domain
failure, but an exact-byte theorem target cannot contain a dangling map.

**Exact repair:** freeze

```text
U_x:H_x -> L^2(R,dt),
(U_x xi)(t)=xi(vartheta_x(t)),
```

and require measure preservation of `vartheta_x` before calling `U_x`
unitary. Use this same direction in the displayed intertwining identity.

#### mR2 — The proxy crossed product still has an unbound action and measure symbol

**Location:** amended `research_protocol.md` Section 4, displayed proxy
candidate.  
The point action `[r] dot t=[r+t]` is frozen, but the corresponding
`C^*`-dynamical action used by `C(S_p^std) rtimes_full R` is not named. Both
pullback signs are otherwise plausible conventions. The same display uses
`mu` in `K(L^2(S_p^std,mu))`, but `mu` is nowhere defined. The whole statement
is correctly source-gated, so these are Minor exactness defects rather than a
premature proxy theorem.

**Exact repair:** freeze, consistently with the displayed groupoid
convolution,

```text
alpha_t(F)([r])=F([r+t]),
mu_p = normalized Haar probability measure on R/L_p Z,
```

and write the candidate as
`C(S_p^std) rtimes_{alpha,full} R`. Alternatively replace the Hilbert-space
factor by an abstract `K` and defer its concrete realization, but do not leave
`mu` unbound. Phase 2 must still adjudicate only Morita equivalence, stable
isomorphism, or actual isomorphism at the strength its exact source proves.

### 8.4 Regression audit

- The two new findings are notation/signature defects only. They do not alter
  the actual orbit, right action, arrow topology, quasi-compact-support owner,
  fibre family, convolution formula, or intended collapse theorem.
- No repaired claim was strengthened into a proof. `P11-1`--`P11-10`, the
  proxy relation, full/reduced equality, bounded novelty, and all Route
  coordinates remain hypotheses or future gates.
- Fixed-orbit quantifiers remain uniform over every rational prime and every
  normalized label. No packet, copied-prime coproduct, or global suspension
  claim entered the amended bytes.
- The deterministic plan retains negative sign/source-range controls,
  action/label/period controls, implementation hashes, verify-only mode, and
  two byte-identical generations; it still grants no continuum theorem.
- No additional Critical, Major, or Minor drift was found after checking the
  research question, all ten targets, hypotheses/falsifiers, `T0`--`T7`, stop
  rules, source/novelty boundaries, and Route ceiling.

### 8.5 Re-lock gate

```text
phase1_methodology_relock_amended_v1: REVISE
critical: 0
major: 0
minor: 2
reviewed_tuple_exact: true
methodology_phase2_block: remains
phase2_authorized_by_methodology: false
route_b_yaml_authorized: false
```

Because this project requires `C0/M0/m0` for PASS, the two one-line signature
repairs need an amended-v2 hash tuple and a short exact-byte re-lock. No new
research, source search, proof work, or implementation is required.

---

## 9. Final exact-byte methodology re-lock — mechanical v1.1 closure

Re-lock date: **2026-08-15 (Asia/Shanghai)**  
Scope: **final four-artifact tuple only; no browsing, source adjudication,
Phase-3 proof, control execution, Route evaluation, or active-lock edit**  
Verdict: **PASS — C0 / M0 / m0**

### 9.1 Final tuple and append-only basis

| Artifact | SHA-256 | Exact match |
|---|---|---|
| `notes/research_protocol.md` | `0f500ca7e10596024a883a027e63203f7f21ffade3d5de59eb367eb2090fb7d5` | yes |
| `notes/candidate_lock.md` | `6ddbea5f4e104ac3bd3ab99fa561b9f6c632e8cd4e86d34371628ecb591526ed` | yes |
| `notes/pipeline_state.md` | `003bd5f96e84a966d689b467ef4247dc733ec1994b09877c9632c9735ae99c4a` | yes |
| `notes/phase1_design_amendment.md` | `e3124bddd6fb9bd9661c6104137086f87ca1a6e2b4fbae212a65b40304aa9572` | yes |

Before this section was appended, the 476-line methodology report matched
SHA-256
`8d28d3b037c685bd8d0e6033a8ff38b45bf78d1e8c9c7bc90541f2db504b993d`.
Thus Sections 1--8 remain the immutable audit history for the initial and
amended-v1 tuples. The Paper-9/Paper-10 load-bearing proof, source, and release
artifacts also retain all five hashes recorded in Section 1.

### 9.2 Closure of the two amended-v1 minor findings

#### mR1 — `U_x` direction and domain: CLOSED

The final protocol now freezes

```text
U_x:H_x -> L^2(R,dt),
(U_x xi)(t)=xi(vartheta_x(t)),
```

where `H_x=L^2(G_x,lambda_x)`,
`vartheta_x(t)=(x dot (-t),t)`, and
`lambda_x=(inversion)_*lambda^x`. The candidate lock repeats both the direction
from `H_x` to `L^2(R,dt)` and the action formula. This is the correct direction:
for `gamma=vartheta_x(t)` and `eta=vartheta_x(u)`, one has
`gamma eta^{-1}=(x dot (-t),t-u)`. Consequently the frozen representation
formula yields

```text
[U_x Ind_x(Phi(g)) U_x^{-1} xi](t)
  = integral_R g(t-u)xi(u)du,
```

exactly the displayed left-convolution target. `P11-5` still requires proof
that `vartheta_x` is measure preserving before `U_x` is called unitary, so the
repair does not pre-certify a Phase-3 result.

#### mR2 — `mu_p` and `alpha_t`: CLOSED

The final protocol binds `mu_p` to the normalized Haar probability measure on
the standard circle `S_p^std=R/L_p Z`, and the proxy display consistently uses
`L^2(S_p^std,mu_p)`. It also freezes the unique crossed-product automorphism in
scope as

```text
alpha_t(h)([r])=h([r+t]).
```

The plus sign agrees with the frozen point right action
`[r] dot t=[r+t]`. With the corresponding dense crossed-product convention,
`alpha_u(H_{t-u})([r])=H([r+u],t-u)`, matching the actual groupoid integrand
`H(x dot u,t-u)`. The nearby notation `C(S_p^std) rtimes_full R` suppresses the
now uniquely frozen action but does not leave it unbound. The candidate remains
explicitly source-gated as `?~=`, with full/reduced, Morita, stable-isomorphism,
and actual-isomorphism strengths kept distinct.

### 9.3 Full methodology regression

| Gate | Final result |
|---|---|
| Primary RQ and nonredundancy | **PASS:** one uniformly quantified `Phi` `*`-isomorphism question; topology, measure, completion, proxy, and arithmetic-blindness claims remain separate subquestions. Standalone status still requires the convention/strict-proxy package and bounded exact-precedent search, otherwise technical-note/merge status. |
| Quantifiers and aggregation | **PASS:** every fixed-orbit claim ranges over every rational prime `p` and every normalized label `a`; packet, prime-coproduct, and full-suspension promotion remain forbidden without a bridge. |
| Transformation groupoid | **PASS:** right action, range, source, product, inverse, unit, composable-pair domain/topology, and joint-continuity obligation retain one sign convention. |
| Arrow topology and Borel targets | **PASS:** quasi-compactness and the two local predicates stay separated; `pi_R`, `B(G)`, universal `T0` continuous factorization, countably-separated measurable factorization, converses, and uniqueness remain exact targets. |
| Global support/function owner | **PASS:** ambient closure support and open-cover quasi-compactness define the author-owned global algebra; the support identity and projection converse remain proof obligations. |
| Hausdorff-open diagnostic | **PASS:** patch support, raw zero extension, raw ambient span, and lack of presumed global continuity remain explicit and distinct from the global owner. |
| Fibre family/convolution | **PASS:** range-fibre Radon/full-support, absolute-integrability, unit-continuity, left-invariance, inversion-only source transport, closure, associativity, support, and `*` gates remain typed; published Haar-system applicability is not assumed. |
| Regular/full/reduced domains | **PASS:** `G_x`, `lambda_x`, `vartheta_x`, `H_x`, `U_x`, `Ind_x`, the reduced supremum, transported group-full norm, representation class, Fourier sign, and amenability ceiling form one executable ledger. |
| Actual/proxy maps | **PASS:** the `+t`-equivariant chart, set-groupoid map `J`, both continuity directions, contravariant `I(f)=f o J^{-1}`, support/measure/`*` gates, image strictness, and completion-extension gate remain directionally consistent. |
| Proxy crossed product | **PASS:** the standard topology, point action, `alpha`, `mu_p`, full candidate, reduced/full amenability gate, and Morita/stable/actual-isomorphism distinctions remain proxy-only and source-gated. |
| Controls and stop rules | **PASS:** action, label, and positive-period axes stay independent; trivial/transitive/nontransitive and sign/source-range negatives, proxy strictness, hashes, verify-only mode, and two fresh generations remain witnesses rather than proofs. All topology/function/measure/completion/aggregation and target-data stops remain active. |
| Route ceiling and integrity | **PASS:** actual host, concrete/abstract global algebra, completions, HOpen diagnostic, and proxy retain separate A0 decisions; lost action/period forces the stated A1 ceiling; A2--A4 receive no credit; Route B and Route-B YAML remain false. No proof, source applicability, novelty, determinant, zero fit, or operator claim is introduced. |

No Critical, Major, or Minor defect remains after the narrow symbol check and
the regression scan of the original M1--M6/m1--m2 findings, all `P11-1`--
`P11-10` targets, H1--H4 falsifiers, `T0`--`T7`, controls, stop rules, phase
gates, source/novelty boundaries, and Route ceilings.

### 9.4 No-weakness coverage receipt

| Dimension examined | What was checked | Basis for no remaining weakness |
|---|---|---|
| Internal mathematical consistency | Fibre coordinates, representation direction, convolution kernel, proxy action sign, and measure owner | All symbols are bound on compatible domains and the two direct substitutions reproduce the frozen formulas. |
| Design validity | RQ, theorem signatures, falsifiers, conventions, owners, and phase dependencies | Each proposed claim has a single frozen object and an explicit future proof or source gate. |
| Reproducibility and falsifiability | Quantifiers, negative controls, independent axes, deterministic artifacts, and stop rules | The plan exposes sign, topology, proxy, aggregation, and proves-too-much failures without treating finite controls as continuum proofs. |
| Claim and Route discipline | Actual/proxy split, author-defined/published split, A0--A4 ceilings, and Route-B entry | No conclusion crosses an owner, topology, completion, aggregation level, or Route gate. |

This PASS clears only the independent methodology seat for the exact tuple
above. Overall Phase 2 remains governed by the protocol requirement that all
three independent Phase-1 re-locks match and pass these bytes.

### 9.5 Final methodology gate

```text
phase1_methodology_final_relock: PASS
critical: 0
major: 0
minor: 0
reviewed_tuple_exact: true
methodology_phase2_block: cleared
phase2_authorized_by_methodology: true
overall_phase2_authorized: false_until_all_three_exact_relocks_pass
route_b_yaml_authorized: false
```

---

## 10. Status-only active-tuple mechanical final-gate audit

Audit date: **2026-08-15 (Asia/Shanghai)**  
Scope: **status transition only; exact inverse reconstruction against the
Section-9 reviewed content tuple; no browsing, mathematical re-review,
Phase-2 source finding, Phase-3 proof, Route evaluation, or active-lock edit**  
Verdict: **PASS — C0 / M0 / m0**

### 10.1 Active tuple and final-gate ledger

| Artifact | Active SHA-256 | Exact match |
|---|---|---|
| `notes/research_protocol.md` | `27c0ffd9c233301528e36f401e9cdf3f4030d65cea8002aafcf6fb97e557f860` | yes |
| `notes/candidate_lock.md` | `a97e9c30bca6bf9cee3e5543b5d83b72ab7291e5485fa9604811dfa3ce4c8012` | yes |
| `notes/pipeline_state.md` | `d4801ffbe0785e3023c55245c21e7ab9c2ea08bf78d524ea86dfe7d54305bff1` | yes |
| `notes/phase1_design_amendment.md` | `e3124bddd6fb9bd9661c6104137086f87ca1a6e2b4fbae212a65b40304aa9572` | yes |
| `notes/phase1_final_gate.md` | `ac26f72f9ff1c5eb935903c20518a43aa043feb8d1572a920bfad471ca47d85f` | yes |

`phase1_final_gate.md` correctly binds the pre-status content tuple from
Section 9 and the three independent final reports:

| Review seat | Bound report SHA-256 | Exact match |
|---|---|---|
| methodology | `0945433bf604670e2ef50f2f2186663206ab93b139f259d8a27a72ebe54a5448` | yes |
| devil's advocate/domain | `610c9fa5c0c99419b58a70c8bf3d61b8777f2b862fb88a7247ef9e6216977c36` | yes |
| source/terminology feasibility | `8348d741aa4f477f8be84767a4a7de438393948e58cad813bf736a4dc3f84a35` | yes |

The methodology hash in that ledger is necessarily the 597-line report before
this status-only receipt is appended. The append changes the live report hash
but not the validity or referent of the recorded three-seat gate.

### 10.2 Exact inverse-reconstruction certificate

The status transition was reversed in a read-only stream, and each reconstructed
artifact reproduced its previously reviewed SHA-256 exactly:

| Active artifact | Reversed bytes only | Reconstructed reviewed SHA-256 | Match |
|---|---|---|---|
| `research_protocol.md` | line 4: `PHASE 1 PASS — PHASE 2 AUTHORIZED` back to `PHASE 1 AMENDED v1 — EXACT-BYTE RE-LOCK REQUIRED` | `0f500ca7e10596024a883a027e63203f7f21ffade3d5de59eb367eb2090fb7d5` | yes |
| `candidate_lock.md` | line 4: the same status reversal | `6ddbea5f4e104ac3bd3ab99fa561b9f6c632e8cd4e86d34371628ecb591526ed` | yes |
| `pipeline_state.md` | lines 7--9: restore amended-v1 freeze, pending exact-byte re-lock, and blocked Phase 2 | `003bd5f96e84a966d689b467ef4247dc733ec1994b09877c9632c9735ae99c4a` | yes |
| `phase1_design_amendment.md` | no reversal; active bytes are identical to the reviewed artifact | `e3124bddd6fb9bd9661c6104137086f87ca1a6e2b4fbae212a65b40304aa9572` | yes |

For `pipeline_state.md`, the only forward changes are exactly:

```text
Phase 1 protocol/candidate freeze:
  amended v1 / three initial REVISE reviews
  -> complete / amended v1.1 after three initial REVISE reviews
Phase 1 exact-byte re-lock:
  pending / all three amended-byte reviews required
  -> PASS / three independent C0/M0/m0 final re-locks
Phase 2 source/convention audit:
  blocked / Phase-1 PASS required
  -> authorized / primary/authoritative sources only
```

Because reversing only those five status/pipeline lines regenerates all three
reviewed file hashes, every other byte in the protocol, candidate, and pipeline
is unchanged. This rules out mathematical drift in the groupoid convention,
support/function owners, fibre measures, regular/full/reduced domains, proxy
maps and signs, theorem targets, hypotheses/falsifiers, controls, stop rules,
source ceilings, aggregation ceiling, and Route ceiling.

### 10.3 Authorization-boundary regression

- The status transition is licensed by three exact `PASS C0/M0/m0` reports on
  the same pre-status tuple; no cross-tuple verdict is inherited.
- Phase 2 is authorized only for primary/authoritative source verification,
  framework applicability, exact-manifestation retention, and bounded novelty
  search under the already frozen owners and conventions.
- Phase 3 proofs and controls remain blocked on the final Phase-2 source gate.
  Route evaluation remains blocked on a stable proof/control tuple, and
  manuscript/release remains blocked on its later blueprint and audits.
- No standard actual-groupoid `C*` theorem, proxy promotion, determinant,
  target-zero use, A2--A4 result, self-adjoint operator, or Route-B permission
  is added. `route_b_yaml_authorized` therefore remains false.
- The Paper-9/Paper-10 load-bearing proof/source/release files still match all
  five hashes recorded in Section 1.

### 10.4 Mechanical final gate

```text
phase1_methodology_status_only_gate_audit: PASS
critical: 0
major: 0
minor: 0
active_tuple_exact: true
final_gate_ledger_exact: true
inverse_reconstruction_exact: true
mathematical_content_drift: false
phase2_source_convention_audit_authorized: true
phase3_proofs_controls_authorized: false
route_evaluation_authorized: false
route_b_yaml_authorized: false
```
