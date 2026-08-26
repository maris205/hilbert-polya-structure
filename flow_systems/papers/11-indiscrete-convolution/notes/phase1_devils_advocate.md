# Paper 11 Phase-1 Devil's-Advocate / Domain Review

Review date: **2026-08-14 (Asia/Shanghai)**  
Review type: independent exact-lock design stress test / ARS Checkpoint 1  
Verdict: **REVISE — C=0, M=5, m=3**  
Phase-2 gate: **BLOCKED pending a versioned amendment and independent exact-byte re-lock**

This review is read-only with respect to the active locks. It used no web
search, source-retention decision, Phase-3 proof, experiment, manuscript edit,
or Route file. It reviews only the following exact input bytes:

| Active input | SHA-256 |
|---|---|
| `notes/research_protocol.md` | `f1575e6d605a5dc442deb5889415f10166d0a6f0e11e8395733dad77a6f2a66f` |
| `notes/candidate_lock.md` | `6815e1d4e09159be9dbb8b0df0d7098e3cafae0e06f7da85a143c9e6c33caea7` |
| `notes/pipeline_state.md` | `406fcc08459b2093aaf52d187d4d9f2f928a40269951681c91c628168e75c95d` |

The inherited theorem inputs were checked on these exact bytes:

| Inherited input | SHA-256 |
|---|---|
| Paper 9 `notes/proof_audit.md` | `c38c24296e5519862eb671dba1644c8005788ac15dffcac48dfdaa1ac3afdde8` |
| Paper 9 release PDF | `c55e4f45fe5f58841864e9af695c4664bdb1a77cff6e087fd2869d4ecd385e02` |
| Paper 10 `notes/proof_audit.md` | `efda522ead9efebfc3f59f0688f2dfd3fe63f63ff4efd4377068485d1a4acc3a` |
| Paper 10 release PDF | `30c22eb8bbfd256cede958df86ce7f985889441a295d52e2ac5acfb3d59e2ce4` |

## 1. Executive adjudication

The core collapse mechanism survives the adversarial calculation. If
`X=X_{p,a}` is nonempty indiscrete and
`pi:X x R -> R` is projection, then the arrow topology is exactly

```text
{X x U : U open in R}.
```

Consequently every continuous complex function is uniquely `g o pi`, its
support is `X x supp(g)`, and the proposed convolution and involution reduce
formally to

```text
(g*k)(t)=integral g(u)k(t-u)du,
g*(t)=conjugate(g(-t)).
```

Every nonempty arrow open contains two topologically indistinguishable points
with the same time coordinate, so no nonempty arrow open is Hausdorff. Thus the
proposed nonzero-global/zero-Hausdorff-open convention split is coherent.

The design is nevertheless not ready for Phase 2. The truth value of its
compact-support and local-quasi-compact claims still depends on an unstated
non-Hausdorff compactness convention; the source action has no frozen
equivariant parameter/sign map to the standard proxy; and the Haar and regular
representation ledgers are not yet specified tightly enough to prevent an
`r`-fibre/`s`-fibre splice. Finally, the global collapse ignores not only
`p` and `L_p` but the action itself. Publication and Route claims must therefore
be framed as an exact arithmetic-owner application/convention no-go, not as a
new arithmetic convolution mechanism.

## 2. Strongest counter-argument

The strongest hostile-review objection is:

> Once the arrow topology is declared to be the product of an indiscrete
> nonempty unit space with `R`, projection to `R` is the entire topological
> quotient. Global continuous functions, their support, convolution, every
> unit regular representation, and the transported completion can no longer
> see the unit coordinate. The same calculation works for a trivial action,
> a nontransitive action, an arbitrary period label, or no arithmetic label at
> all. The paper has therefore not discovered arithmetic convolution; it has
> computed the group algebra left after its chosen global-continuity convention
> erases the groupoid action. Unless the convention split, owner correction,
> and proxy contrast are proved and sourced as the actual contribution, the
> result is a generic corollary of an indiscrete-factor lemma and is redundant
> with Paper 10's collapse principle.

This objection does not refute the proposed theorem. It fixes its honest
novelty, arithmetic, and Route ceiling.

## 3. Findings by severity

### Critical findings

None. No counterexample was found to H1--H3 under the intended open-cover
compactness convention and the frozen right-action groupoid formulas.

### Major findings

#### M1 — compact support and “local quasi-compactness” do not yet have one truth condition

- **Type:** topology / support domain / source-framework applicability
- **Evidence anchors:** `research_protocol.md:80-83,163-188,350-355`;
  `candidate_lock.md:73-75`
- **Problem:** `X x K` with `K` compact in `R` is quasi-compact by the
  open-cover definition but is non-Hausdorff when `X` is nontrivial. Moreover,
  this arrow space has compact neighbourhoods and a basis of open
  neighbourhoods with quasi-compact closures, but it has no nonempty
  quasi-compact **open** neighbourhood. Different uses of “locally
  quasi-compact” therefore give different answers. The current lock defines
  support by closure but not what “compact” means in this non-Hausdorff space.
- **Impact:** P11-1 and the converse direction of P11-3 can be reported as
  either true or false by silently changing conventions; the same ambiguity
  contaminates Phase-2 applicability claims.
- **Required amendment:** freeze `quasi_compact` as the open-cover predicate
  and state whether `compact` is a synonym or additionally requires
  Hausdorffness. Prove for every subset `K0 subset X x R` that

  ```text
  K0 is open-cover quasi-compact iff pi(K0) is compact in R.
  ```

  Then state separately: compact-neighbourhood property; relatively compact
  open-neighbourhood property; absence of nonempty quasi-compact open sets;
  and absence of nonempty Hausdorff open sets. Use only the selected predicate
  in `C_c^glob` and in every source comparison.
- **Confidence:** 5/5 — direct classification of all arrow opens.

#### M2 — the actual/proxy comparison lacks a frozen equivariant parameter and action sign

- **Type:** same-object identity / action orientation / pullback direction
- **Evidence anchors:** `research_protocol.md:29-68,133-156,220-227`;
  `candidate_lock.md:67-89`
- **Problem:** the lock names the orbit set `R/L_p Z` and writes `x dot t`,
  but it does not freeze a named basepoint-dependent bijection and the exact
  `+t` or `-t` equivariance inherited from logarithmic Deninger time. A bare
  identity of carriers is enough to compare topologies, but not enough to
  claim an identity **groupoid** map, Haar-preserving pullback, or proxy
  convolution subalgebra.
- **Impact:** P11-7 can have the correct topological direction while comparing
  different actions. That would fail T0/T2/T5 even though the function formula
  happens to look unchanged after unit-coordinate collapse.
- **Required amendment:** freeze a chosen map

  ```text
  theta_{p,a}: R/L_p Z -> X_{p,a},
  theta_{p,a}([r]) dot t = theta_{p,a}([r + epsilon*t]),
  epsilon in {+1,-1},
  ```

  with `epsilon` sourced from the exact flow convention. Give `G_p^std` the
  same signed right action. Name the induced identity groupoid map
  `j:G_p^std -> G_{p,a}^{act}`; require proof that `j` is continuous and its
  reverse is not. Freeze the contravariant map as
  `j^*:C_c^glob(G_act)->C_c(G_std)` and its unit-coordinate-constant image.
- **Confidence:** 5/5 — carrier topology does not determine action
  equivariance.

#### M3 — “Haar system in the frozen sense” needs a complete author-defined axiom record

- **Type:** measure domain / terminology / convolution validity
- **Evidence anchors:** `research_protocol.md:85-101,190-201,294-305`;
  `candidate_lock.md:69-78,123-130`
- **Problem:** fibre support, integral continuity, and left invariance are
  named, but the lock does not state the exact measure class, full-support
  condition, left-invariance equation, or whether the continuity test is only
  over `C_c^glob`. Calling the result a Haar system without those fields risks
  importing a published locally-Hausdorff definition whose object and
  function space are inapplicable here.
- **Impact:** P11-4 could be true for the author-defined global algebra but
  incorrectly serialized as a standard non-Hausdorff groupoid Haar theorem.
- **Required amendment:** register a separately named author object, for
  example `GLOB-HAAR-FAMILY`, with: positive Radon measure on each usual
  `r`-fibre; full fibre support; continuity (and compact support, if required)
  of `x |-> integral f d lambda^x` for every `f in C_c^glob`; and the exact
  equation

  ```text
  integral f(gamma*eta) d lambda^{s(gamma)}(eta)
    = integral f(eta) d lambda^{r(gamma)}(eta).
  ```

  Keep “published Haar system” source-gated in P11-6. Prove convolution
  well-definedness and closure in the global algebra rather than inferring
  them from terminology.
- **Confidence:** 5/5 — exact Haar axioms and frozen test algebra are
  logically prior to convolution credit.

#### M4 — the regular representation and reduced norm remain orientation-ambiguous

- **Type:** representation domain / `r`- versus `s`-fibre / norm ownership
- **Evidence anchors:** `research_protocol.md:118-131,203-210,350-355`;
  `candidate_lock.md:52-57,75-80`
- **Problem:** P11-5 promises an exact later formula, but the candidate already
  names a reduced completion without freezing which unit-regular
  representation defines it. With a Haar system on `r`-fibres, the standard
  regular Hilbert space is naturally expressed using the inversion measure on
  the `s`-fibre. Writing the same-looking formula directly on an `r`-fibre can
  make products undefined or reverse the convolution sign.
- **Impact:** equality with the left regular representation of `R`, and hence
  the claimed reduced norm, is not mechanically testable from the current
  lock.
- **Required amendment:** freeze

  ```text
  G_x=s^{-1}(x)={(x dot (-t),t):t in R},
  lambda_x=(inversion)_* lambda^x,
  H_x=L^2(G_x,lambda_x),
  [Ind_x(f)xi](gamma)
      = integral_{G_x} f(gamma*eta^{-1}) xi(eta) d lambda_x(eta).
  ```

  Under `U_x xi(t)=xi(x dot (-t),t)`, require the derived formula
  `U_x Ind_x(Phi(g)) U_x^{-1} xi(t)=integral g(t-u)xi(u)du` for every unit.
  Define the transported full norm explicitly through `Phi^{-1}` and the
  reduced norm as the supremum of these named unit norms. Equality of full and
  reduced completions and `C_0(Rhat)` then require the separately sourced
  amenability/Fourier theorem for `R`; neither completion is an unqualified
  groupoid completion.
- **Confidence:** 5/5 — direct composability calculation.

#### M5 — the collapse is action-blind, so novelty and Route ceilings must be strengthened

- **Type:** generality / publication nonredundancy / arithmetic ownership /
  proves-too-much
- **Evidence anchors:** `research_protocol.md:8-27,229-257,310-341`;
  `candidate_lock.md:6-17,110-120`
- **Problem:** once `X` is nonempty indiscrete, neither transitivity,
  stabilizer `L_p Z`, nor even the action enters the proof that global
  functions are `g(t)`. The same is true of the convolution formula after
  both factors lose their unit coordinate. The current controls vary periods,
  labels, and transitive actions, but do not include trivial and nontransitive
  actions, which are the sharpest demonstration that the mechanism is not
  arithmetic.
- **Impact:** an arithmetic-convolution novelty claim would fail the Route-A
  A0 control gate and the “so what?” test. The actual theorem remains useful as
  a typed convention split and owner no-go.
- **Required amendment:** state and label the general lemma first: for every
  nonempty indiscrete `X` and every continuous right `R`-action, the frozen
  global algebra is `C_c(R)` with the derived operations. State the
  rational-Witt result only as its exact Paper-9-owned application. Add trivial,
  nontransitive, arbitrary-set, composite-label, and randomized-period
  controls. In the Route plan, adjudicate A0 separately for `ACT-GRPD`, the
  concrete global algebra, its abstract isomorphism class, and each transported
  completion; grant no inherited analytic-arithmetic A0 status, set A1 to fail
  wherever the stabilizer/period is erased, and retain A2/A3/A4 fail and Route
  B false. Bound novelty to `SUPPORTED_WITHIN_SEARCH` for the exact
  owner/convention/proxy package.
- **Confidence:** 5/5 — the proposed formulas contain no action or period
  after global-continuity reduction.

### Minor findings

#### m1 — preregister the exact arrow Borel and separated-target factorization

P11-2 should target

```text
B(G)=pi^{-1}(B(R)).
```

For every `T0` target, continuous maps should factor uniquely through a
continuous map from `R`; for every countably separated measurable target,
Borel maps should factor uniquely through a Borel map from `R`. The arrow
measurable space is not countably separated when `X` is nontrivial. This keeps
P11-2 distinct from the false statement that all arrow observables are
constant.  
**Evidence anchor:** `research_protocol.md:171-176`.  
**Confidence:** 5/5.

#### m2 — keep the Hausdorff-open span diagnostic syntactically separate

Freeze whether compact support for a generator is taken inside the Hausdorff
open patch and state that its zero extension need not be globally continuous
in general. For this exact arrow topology the diagnostic is zero only because
there is no nonempty Hausdorff open patch. That computation neither defines a
published `C_c(G)` nor proves nonexistence of every other non-Hausdorff
construction.  
**Evidence anchor:** `research_protocol.md:103-116,212-218,277-284`.  
**Confidence:** 5/5.

#### m3 — downgrade the displayed proxy isomorphism to a source-gated candidate

Phase 2 should first verify the exact Green/imprimitivity statement for the
chosen signed transitive action and distinguish Morita equivalence, stable
isomorphism, and an actual (possibly noncanonical) isomorphism. It must also
distinguish full from reduced crossed products and define `K`. Until then,
write the displayed `C(S_p^std) rtimes R ~= C^*(L_p Z) tensor K` only as a
candidate proxy relation, not as an already established “standard result.”  
**Evidence anchor:** `research_protocol.md:147-156`; `candidate_lock.md:83-89`.  
**Confidence:** 4/5 — exact theorem form is source-dependent and was not
verified in this no-browse review.

## 4. Technical stress-test ledger

| Test | Design result | Gate implication |
|---|---|---|
| all arrow opens | exactly `X x U`, `U` open in `R` | P11-1 viable |
| all arrow closed sets | exactly `X x F`, `F` closed in `R` | support closure is computable |
| subset quasi-compactness | equivalent to compactness of its time projection | requires M1 convention lock |
| `T0` quotient of arrow space | `R` via time projection | arrow observables factor through time, not necessarily a point |
| nonempty Hausdorff arrow open | none | H3 viable; `C_c^HOp=0` diagnostically |
| global continuous functions | uniquely `f(x,t)=g(t)` | H1 viable |
| global support | `X x supp_R(g)` | compact-support equivalence viable under M1 |
| left invariance | translation `u |-> t+u` preserves `dt` | M3 can close directly |
| convolution/involution | ordinary `R` formulas | H2 viable |
| unit regular representation | left convolution after the exact `s`-fibre unitary | M4 can close directly |
| actual/proxy topology | standard-to-actual identity continuous; reverse not | needs M2 equivariant groupoid lock |
| proxy pullback image | unit-coordinate-constant `C_c(R)` subalgebra; proper | exhibit `psi(x)g(t)` with nonconstant `psi` |
| action/stabilizer retention | absent from global algebra and both transported norms | M5 proves-too-much control fires |

## 5. Exact amendment checklist

- [ ] **R1 / M1:** freeze open-cover quasi-compactness, compact-support
      terminology, the projection criterion, and all local-property variants.
- [ ] **R2 / M2:** freeze `theta_{p,a}`, the source-owned action sign, the same
      signed standard action, `j`, `j^*`, and the exact image subalgebra.
- [ ] **R3 / M3:** register the author-defined global Haar-family axioms and
      keep published Haar-system applicability source-gated.
- [ ] **R4 / M4:** freeze `G_x`, `lambda_x`, `H_x`, `Ind_x`, the unitary to
      `L^2(R)`, and the exact transported full/reduced norm definitions.
- [ ] **R5 / M5:** add the arbitrary-indiscrete-action theorem and
      trivial/nontransitive controls; separate generic novelty from the exact
      arithmetic-owner application and adjudicate A0 per owner.
- [ ] **R6 / m1:** freeze the arrow Borel/factorization theorem and the
      non-countably-separated boundary.
- [ ] **R7 / m2:** specify Hausdorff-open generator support/extension semantics
      and preserve its diagnostic-only status.
- [ ] **R8 / m3:** type the proxy result as Morita/stable/isomorphic only after
      exact full/reduced source verification.

The amendment must preserve the Paper 9 and Paper 10 hashes above, receive a
new amendment ID, and be independently reviewed on the amended tuple. This
reviewer does not self-certify its repair.

## 6. Final Checkpoint-1 verdict

```text
Critical: 0
Major: 5
Minor: 3
Verdict: REVISE
Phase-2 authorization: false
Route-B invocation: false
```

The mathematical core is plausible and has a direct proof path. Phase 2 may
begin only after M1--M5 are closed on versioned amended bytes. No conclusion
in this report licenses an unqualified non-Hausdorff groupoid `C_c`, `C^*`,
or `C_r^*` claim.

---

## Exact-byte re-lock addendum — amended v1

Re-lock date: **2026-08-15 (Asia/Shanghai)**  
Scope: **amended Phase-1 design only; no browsing, source verdict, Phase-3
proof/control execution, manuscript edit, active-lock edit, or Route file**  
Verdict: **PASS — C=0, M=0, m=0 on the amended bytes**

The re-lock applies only to this exact four-file tuple:

| Amended artifact | SHA-256 |
|---|---|
| `notes/research_protocol.md` | `bc40e307746c1d05808d8288dba0b0a315c30e60d7983989ca42ebe913ecb922` |
| `notes/candidate_lock.md` | `a82a96957f5d58b0925e96395ea2994acb9dece9e24f60f286b7ea714cdb7c3e` |
| `notes/pipeline_state.md` | `003bd5f96e84a966d689b467ef4247dc733ec1994b09877c9632c9735ae99c4a` |
| `notes/phase1_design_amendment.md` | `7d2c2c7eb041a530ff4da6f7090d85053b067243d7a2ab445b4b4cba9cc2dc64` |

The initial `REVISE` report and its `bbd760e8...` hash remain historical; this
addendum does not retroactively change that verdict on the superseded tuple.

### Closure matrix

| Initial ID | Re-lock status | Exact amended-byte basis |
|---|---|---|
| M1 | **CLOSED** | Protocol Section 3.1 defines open-cover quasi-compactness, ambient support, and `C_qc^glob`; P11-1 freezes the time-projection iff criterion and separately names compact-neighbourhood, quasi-compact-closure-basis, quasi-compact-open, and Hausdorff-open predicates. No unqualified local-compactness claim remains. |
| M2 | **CLOSED** | Protocol Section 2 freezes `theta([r])=x^0 dot r` and `theta([r]) dot t=theta([r+t])`; Section 4 gives the same `+t` standard action, the exact set-groupoid map `J:G_act->G_std`, both continuity directions, and contravariant `I(f)=f o J^{-1}`. Completion transport is separately gated. |
| M3 | **CLOSED** | `GLOB-FIBRE-FAMILY` is now an author-owned positive-Radon/full-fibre-support/absolute-integrability/continuity/left-invariance record on exactly `C_qc^glob`; published Haar terminology remains Phase-2 source-gated. Convolution closure, associativity, support, and `*` identities are explicit P11-4 obligations. |
| M4 | **CLOSED** | Protocol Section 3.3 freezes `G_x`, inversion-pushed `lambda_x`, `vartheta_x`, `H_x`, `Ind_x`, and the supremum unit norm. The measure-preserving obligation for `vartheta_x` specifies the canonical pullback unitary to `L^2(R)`, and the exact conjugated left-convolution formula is a theorem gate. The full norm is only the transported group norm; amenability and Fourier identification remain sourced group theorems. |
| M5 | **CLOSED** | Section 1 denies generic novelty and adds a standalone-release gate; P11-8 first registers the arbitrary nonempty-indiscrete `R`-action lemma and includes trivial/nontransitive actions plus independent period/label controls. P11-10 separates the actual host, concrete algebra, abstract isomorphism class, completions, diagnostic, and proxy at A0, with no inherited analytic-arithmetic credit. |
| m1 | **CLOSED** | P11-2 states `B(G)={X x B:B in B(R)}`, exact `T0` continuous factorization, exact countably-separated measurable factorization, and the non-countably-separated source test. It does not claim arrow observables are constant in time. |
| m2 | **CLOSED** | Section 3.2 defines support inside each Hausdorff open patch, types zero extension as a raw function that need not be globally continuous, and keeps the span diagnostic-only. P11-6 separates its zero computation from applicability or universal-nonexistence claims. |
| m3 | **CLOSED** | Section 4 changes the displayed proxy relation to `?~=` and distinguishes the dense algebra, full/reduced crossed products, Green Morita equivalence, stable isomorphism, and actual isomorphism. `K` is typed as compact operators on the displayed proxy Hilbert space; every equality and measure realization remains an exact Phase-2 source obligation. |

### Independent contract recomputation

The following calculations were repeated from the amended definitions rather
than accepted from the amendment ledger.

#### Topology, quasi-compactness, and support

Let `X=X_{p,a}` and `pi(x,t)=t`. Since `X` is nonempty indiscrete, all arrow
opens and closed sets are respectively

```text
X x U  (U open in R),
X x F  (F closed in R).
```

For an arbitrary subset `K0 subset X x R`, continuity of `pi` gives the
forward implication

```text
K0 quasi-compact => pi(K0) compact in R.
```

Conversely, every relative-open cover of `K0` is pulled back from an open
cover of `pi(K0)`, so a finite subcover of the time projection covers `K0`.
Thus the amended iff contract is correct. It follows that:

- `X x [t-epsilon,t+epsilon]` is a quasi-compact neighbourhood;
- intervals with compact closure give a basis of open neighbourhoods with
  quasi-compact closure;
- a nonempty arrow open cannot be quasi-compact, because a nonempty open
  subset of usual `R` is not compact; and
- a nonempty arrow open cannot be Hausdorff, because two different unit
  points at the same time coordinate remain topologically indistinguishable.

For `Phi(g)(x,t)=g(t)`, the nonzero locus and its closure are

```text
X x {t:g(t)!=0},
supp_G(Phi(g))=X x supp_R(g).
```

The projection criterion therefore gives quasi-compact arrow support exactly
when `g` has ordinary compact support. M1 introduces no residual defect.

#### Sign, composability, and groupoid maps

The amended `+t` chart gives

```text
beta(x dot t)=beta(x)+t mod L_p Z.
```

Hence `J(x,t)=(beta(x),t)` preserves range, source, products, inverse, and
units. The composable-pair parameter

```text
(x,t,u) |-> ((x,t),(x dot t,u))
```

pulls the subspace topology back to the product of the indiscrete `X` topology
and the usual topology on `R^2`; addition `(t,u)|->t+u` proves multiplication
continuity. In the proxy direction, `J^{-1}:G_std->G_act` is continuous because
actual opens depend only on time, whereas `J` is not continuous because a
proper circle-coordinate open has no actual-open inverse image. Therefore
`I(f)=f o J^{-1}` has the stated actual-to-proxy pullback direction.

#### Fibre family, convolution, and regular representation

For `gamma=(x,t)` and
`eta=(x dot t,u) in G^{s(gamma)}`,

```text
gamma eta=(x,t+u).
```

Every licensed global function is `Phi(g)`, so both fibre integrals in the
left-invariance contract are related by the Lebesgue translation
`u |-> t+u`. The convolution and involution reduce with the frozen sign to

```text
(Phi(g)*Phi(k))(x,t)=integral_R g(u)k(t-u)du,
Phi(g)^*(x,t)=conjugate(g(-t)).
```

For the unit-regular record put

```text
gamma_t=vartheta_x(t)=(x dot (-t),t),
eta_u=vartheta_x(u)=(x dot (-u),u),
eta_u^{-1}=(x,-u).
```

Then `gamma_t eta_u^{-1}=(x dot (-t),t-u)`, so the frozen `Ind_x` formula
becomes `integral g(t-u)xi(u)du` under the pullback along `vartheta_x`.
Inversion sends `(x,v)` to `(x dot v,-v)`, which is `vartheta_x(-v)`; hence
`lambda_x=inv_*lambda^x` corresponds exactly to Lebesgue measure under
`vartheta_x`. The sign, composability, and measure contracts therefore agree,
and no `L_p`, action, or stabilizer term survives in the unit norm.

#### Borel, Hausdorff-open, proxy, and Route boundaries

The topology-generated sigma-algebra is `pi^{-1}(B(R))`. Points with the same
time and different unit coordinates lie in exactly the same measurable sets,
so maps to countably separated targets factor through time and the nontrivial
arrow measurable space is not countably separated. Since there is no nonempty
Hausdorff arrow open, the frozen raw Hausdorff-open span is zero; this remains
a diagnostic, not a standard groupoid-algebra verdict.

The image of `I` is exactly the unit-coordinate-constant proxy subalgebra. A
function `psi([r])g(t)` with nonconstant continuous circle `psi` and nonzero
`g in C_c(R)` is a legal proxy element outside the image. This proves the
design-level strictness falsifier is correctly posed, without pre-certifying
the theorem. The same global calculation for trivial and nontransitive
actions confirms that arithmetic/action blindness is a proves-too-much
control and not A0/A1 credit.

### Re-lock verdict

No new Critical, Major, or Minor defect appears on the exact amended tuple.
The original five Major and three Minor findings are closed without weakening
their decision thresholds.

```text
Critical: 0
Major: 0
Minor: 0
Verdict: PASS
Devil's-advocate amended-byte authorization: true
Phase-3 authorization: false
Route-B invocation: false
```

This PASS authorizes only this reviewer's Phase-1 amended-byte seat. The
project-wide Phase-2 gate still requires matching independent amended-byte
PASS reports from the other two reviewers. No Phase-2 source result, P11
theorem, standard groupoid completion, standalone-paper novelty claim, or
Route verdict is certified here.

---

## Final exact-byte mechanical regression — amended v1.1

Re-lock date: **2026-08-15 (Asia/Shanghai)**  
Scope: **only the added definitions of `U_x`, `mu_p`, and `alpha_t`, plus
regression of their adjacent sign/domain contracts; no browsing, source
verdict, Phase-3 proof, active-lock edit, manuscript edit, or Route edit**  
Verdict: **PASS — C=0, M=0, m=0**

The final regression is bound to these exact bytes:

| Artifact | SHA-256 |
|---|---|
| `notes/research_protocol.md` | `0f500ca7e10596024a883a027e63203f7f21ffade3d5de59eb367eb2090fb7d5` |
| `notes/candidate_lock.md` | `6ddbea5f4e104ac3bd3ab99fa561b9f6c632e8cd4e86d34371628ecb591526ed` |
| `notes/pipeline_state.md` | `003bd5f96e84a966d689b467ef4247dc733ec1994b09877c9632c9735ae99c4a` |
| `notes/phase1_design_amendment.md` | `e3124bddd6fb9bd9661c6104137086f87ca1a6e2b4fbae212a65b40304aa9572` |

The immediately preceding DA report bytes had SHA-256
`7535a439a7ae5ff238755083c4ae2b536bcdc14b2fb0ab38a990b6f02953a702`.
This addendum supersedes no earlier verdict on a different tuple.

### Definition and owner re-lock

| Added definition | Regression result |
|---|---|
| `U_x:H_x->L^2(R,dt)`, `(U_x xi)(t)=xi(vartheta_x(t))` | **PASS.** The map has the correct pullback direction and is confined to the source-fibre owner `H_x=L^2(G_x,lambda_x)`. Its unitarity remains a P11-5 proof obligation through measure preservation; it is not assumed by the definition. |
| `mu_p` = normalized Haar probability on `S_p^std` | **PASS.** It types only the proxy Hilbert space in `K(L^2(S_p^std,mu_p))`. It neither replaces actual range-fibre Lebesgue `lambda^x` nor source-fibre `lambda_x`. |
| `alpha_t(h)([r])=h([r+t])` | **PASS.** It matches the frozen proxy right action `[r] dot t=[r+t]`; `alpha_0=id` and `alpha_s alpha_t=alpha_{s+t}`. Sources using inverse pullback remain subject to the explicit Phase-2 translation gate. |

### Sign, composability, and measure regression

The chart still gives

```text
beta(x dot t)=beta(x)+t,
s_std(J(x,t))=beta(x)+t=beta(s_act(x,t)),
J(x,t)J(x dot t,u)=(beta(x),t+u)=J(x,t+u).
```

Thus the new `alpha_t` line introduces no `t -> -t` drift and changes neither
`J:G_act->G_std` nor the contravariant direction
`I(f)=f o J^{-1}`.

For the unit regular representation, set

```text
gamma_t=vartheta_x(t)=(x dot (-t),t),
eta_u=vartheta_x(u)=(x dot (-u),u),
eta_u^{-1}=(x,-u),
gamma_t eta_u^{-1}=(x dot (-t),t-u).
```

Inversion maps `(x,v)` to `vartheta_x(-v)`, so
`lambda_x=inv_*lambda^x` is Lebesgue measure in the `vartheta_x` coordinate.
Consequently the newly explicit `U_x` gives exactly

```text
[U_x Ind_x(Phi(g)) U_x^{-1} xi](t)
  = integral_R g(t-u)xi(u)du.
```

The convolution and involution contracts remain

```text
(Phi(g)*Phi(k))(x,t)=integral_R g(u)k(t-u)du,
Phi(g)^*(x,t)=conjugate(g(-t)).
```

No stabilizer, period, orbit label, modular factor, or proxy measure enters
the actual fibre formula. The transported universal norm and all-unit reduced
norm therefore retain their prior, separately typed owners.

### Topology and scope non-regression

The mechanical additions do not alter the arrow topology. Its opens remain
`X x U`; for every `K0 subset X x R`, open-cover quasi-compactness remains
equivalent to compactness of `pi_R(K0)`, and
`supp_G(Phi(g))=X x supp_R(g)`. The distinct quasi-compact-neighbourhood,
quasi-compact-closure-basis, quasi-compact-open, and locally-Hausdorff
predicates remain separated.

`C_c^HOp` remains a raw diagnostic and not a published-convention verdict.
The proxy relation remains `?~=`, with dense/full/reduced/Morita/stable/
isomorphism claims separated. The theorem remains fixed-orbit only; the
generic action-blind control, novelty ceiling, A0 owner split, and Route-B
prohibition are unchanged.

### Final amendment checklist

- [x] All four exact hashes match the v1.1 tuple.
- [x] `U_x` has an explicit direction, domain, codomain, and source-fibre
  measure owner.
- [x] `mu_p` is defined and remains proxy-only.
- [x] `alpha_t` matches the `+t` chart and set-groupoid source convention.
- [x] Product, inverse, regular-representation, convolution, and involution
  signs recompute without contradiction.
- [x] No topology, compact-support, Borel, HOpen, completion, aggregation,
  novelty, source-applicability, or Route claim changed.
- [x] Prior M1--M5 and m1--m3 remain closed; no new amendment is required.

```text
Critical: 0
Major: 0
Minor: 0
Verdict: PASS
Devil's-advocate final-tuple authorization: true
Phase-3 authorization: false
Route-B invocation: false
```

This is only the DA/domain status re-lock on the exact final tuple. The
unchanged pipeline gate still requires the other independent Phase-1 seats;
this report does not advance `pipeline_state.md` or certify any P11 theorem,
source convention, proxy theorem, standalone novelty claim, or Route result.
