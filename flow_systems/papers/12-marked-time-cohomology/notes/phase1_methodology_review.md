# Paper 12 Phase-1 methodology and nonredundancy review

Review date: **2026-08-15 (Asia/Shanghai)**  
Reviewer role: **independent methodology/domain/devil reviewer (ARS Phase-1 gate)**  
Scope: **exact initial design bytes only; no browsing, Phase-2 source/novelty
search, Phase-3 proof, or control execution**  
Verdict: **REVISE — C0 / M6 / m2**

## 1. Exact-byte review basis

| Locked artifact | SHA-256 | Match |
|---|---|---|
| `notes/research_protocol.md` | `1ea7e67825d5f543f472e1f4e0b3ea57a986269b24ec8dad1bf533475cc860eb` | yes |
| `notes/candidate_lock.md` | `6a03983a76d34937f01ff03da4d074d1111b0722afff417a4532c5d7744f2975` | yes |
| `notes/pipeline_state.md` | `4fe89540fb743e757e45ce71569261659a0d780db0c79ee5867792fe8ac936c0` | yes |

The inherited evidence tuple named by the candidate also matches:

| Inherited artifact | SHA-256 | Match |
|---|---|---|
| Paper 9 `notes/proof_audit.md` | `c38c24296e5519862eb671dba1644c8005788ac15dffcac48dfdaa1ac3afdde8` | yes |
| Paper 9 `notes/source_audit.md` | `20fecdf360d18f9accf3e3ec8467f3beb369a8737761eb6219fef71e9773ac20` | yes |
| Paper 10 `notes/proof_audit.md` | `efda522ead9efebfc3f59f0688f2dfd3fe63f63ff4efd4377068485d1a4acc3a` | yes |
| Paper 11 `notes/proof_audit.md` | `03f17606b0c9d69b496d2766c0a404b0d090698101150a800de4c2108ddc6b28` | yes |
| Paper 11 `notes/composition_blueprint.md` | `4b6bfa27c83f72858ac5f0d03c0b9964f93e914fc1d4fdfced619327bcdfc30b` | yes |

The prior-work audit was limited to the proof/composition facts needed to
test ownership and nonredundancy. Paper 9 owns the actual packet and inherited
orbit indiscreteness, the exact right action, the common fixed-prime
stabilizer `p^Z`, and the logarithmic clock. Paper 10 owns collapse of
separated unit observables. Paper 11 already owns the generic arrow topology,
the composable-pair chart, continuous `T0`-target factorization through time,
and the action-blind fixed-orbit application. None of those inputs is treated
as a Paper-12 result.

## 2. Overall assessment

The design has a defensible mathematical spine. The range-first action
groupoid convention, all-globally-continuous cochain domain, explicit
inhomogeneous differential, source-normalized real clock, isotropy image,
packet source gate, actual/standard topology separation, arbitrary-clock
controls, and negative Route ceiling are all well chosen. The all-degree
nerve statement is also correctly prevented from being inferred merely from
the arrow case, and the proposed degree-one calculation does not smuggle the
unbounded time cocycle into Paper 11's global-QC algebra.

The exact bytes nevertheless cannot pass the Phase-1 zero-finding gate. The
primary rigidity wording asserts more than the three morphism classes can
show; the constant coefficient system and the status of the cohomology
quotient are not fully typed; and the period-quotient construction is not
valid for an arbitrary rescaling of the marked class unless the mark is
restricted to the coordinate-normalized clock. Its promised functoriality is
also only an object assignment, with no source category or morphism map. The
deterministic controls contain unfrozen examples and an unspecified random
choice. Finally, the standalone gate does not yet operationalize the stated
rule that a formal extension of Paper 11 plus a stabilizer restatement must be
merged rather than released separately. These are repairable Phase-1 design
defects; no Critical defect was found.

## 3. Major findings

### M1 — “Preserved precisely by strict morphisms” is not the theorem the registered categories can support

**Location:** `research_protocol.md` Sections 1 and 6; `candidate_lock.md`
Sections 1, 4, and 5.  
**Why Major:** strict marked isomorphisms certainly provide a sufficient
invariance class, while one scaled counterisomorphism is enough to show that
period scale does not descend to the positive-scaled or unmarked equivalence
category. That is not an if-and-only-if characterization of individual
morphisms. The unmarked class contains the strict class, so many unmarked
morphisms preserve periods. Moreover, an orientation-reversing unmarked
automorphism of a translation control can preserve the subgroup `LZ` while
sending the clock to `-c`; it is not strict and is outside the declared
positive-scaled class. Thus exact subgroup preservation does not characterize
strictness. The words “precisely” and “only” make the primary RQ false under a
natural morphism-level reading and blur “not invariant in a category” with
“changed by every morphism in that category.”  
**Minimum repair:** freeze marked objects and three actual sub/forgetful
categories, including their object sets, unit and arrow maps, continuity,
composition, inverse, and the time-orientation rule. Replace the iff-like
claim by:

```text
Per is an exact invariant on the strict marked category.
Under a morphism with c' o F=alpha c, Per_(F_0 x)(c')=alpha Per_x(c).
The exact scale does not descend to positive-scaled or unmarked equivalence,
because explicit unequal-period objects are isomorphic after forgetting or
allowing scale.
```

State explicitly that non-descent is existential. Include the
orientation-reversing control to show that exact period equality outside the
strict class is possible and therefore cannot be used as a converse test for
strictness.

### M2 — The “trivial coefficient” and cohomology objects are not yet fully typed

**Location:** `research_protocol.md` Sections 3--5; `candidate_lock.md`
Sections 3--4.  
**Why Major:** a groupoid coefficient is not merely a single topological
group with the phrase “trivial `G`-action.” It must be clear whether the
intended standard object is the constant bundle `X x A -> X` with every arrow
acting by the identity, or whether the displayed formulas define an
author-specific cochain complex without a coefficient-bundle claim. The
current lock also does not state whether `H_cont^n` is the algebraic quotient
`ker d^n / im d^(n-1)` or a topological quotient of topologized cochain
spaces. That distinction affects the meaning of “isomorphism,” and in degree
one it affects whether `R[c]` is an algebraic real line or a topological
identification. “Entire complex” also needs an explicit declaration that the
displayed complex is the unnormalized nerve complex; no degeneracy/normalized
subcomplex result is being claimed. Deferring only the label “standard” to
Phase 2 is sound, but deferring the mathematical coefficient object and
quotient type is not.  
**Minimum repair:** define the constant coefficient bundle and identity arrow
action, or call the displayed object an author-defined unnormalized
continuous nerve complex. Define cochain addition pointwise and freeze

```text
Z_cont^n=ker d^n,
B_cont^n=im d^(n-1),
H_cont^n=Z_cont^n/B_cont^n
```

as abstract abelian groups; for `A=R`, state that these are real vector spaces.
If a compact-open or other cochain topology and topological quotient is also
intended, make it a separate target with separately proved continuity and
closed-image obligations. Require Phase 2 to classify the exact frozen
complex, not to choose among these alternatives.

### M3 — `R/Per(c)` parametrizes the action orbit only for a normalized clock, not for an arbitrary marked class

**Location:** `research_protocol.md` Sections 4--7 (`P12-5`, `P12-8`);
`candidate_lock.md` Sections 3--4.  
**Why Major:** the based orbit map `t |-> x dot t` has kernel
`H_x=Stab_R(x)`, so its homogeneous-space source is `R/H_x`. For a general
real class `[b]=lambda[c]`, however,
`Per_x([b])=lambda H_x`. The displayed map

```text
theta_x:R/Per_x(b) -> X,  [t] |-> x dot t
```

need not be well defined or bijective when `lambda != 1`. For example, one
choice of scale makes `Per_x(b)` larger than `H_x`, so equivalent source
classes can act to distinct units; the opposite scale can make the map
many-to-one. The candidate lock intends the Deninger-normalized coordinate
cocycle, but Section 7 states the construction for a generic “marked
transitive object” using only the period subgroup. The generic statement is
therefore too broad and conflicts with the preceding scale-blindness result.
  
**Minimum repair:** choose and freeze one of two nonconflated constructions:

1. restrict `P12-8` to source-normalized coordinate-clock action groupoids
   with `c(x,t)=t`, prove `Per_x(c)=H_x`, and only then put
   `S(G,c)=R/H_x=R/Per_x(c)`; or
2. for arbitrary marked classes, keep the actual orbit model `R/H_x`
   separate from the value-space quotient `R/Per_x(b)` and do not define
   `theta_x` between them without an additional scale map and its exact
   hypotheses.

The manuscript must not present the second quotient as a reconstruction of
the unit orbit from the abstract cohomology class.

### M4 — The period-quotient “functor” has no frozen morphism assignment or naturality contract

**Location:** `research_protocol.md` Sections 6--7 and 9 (`P12-7`, `P12-8`);
`candidate_lock.md` Sections 3--4.  
**Why Major:** `S(G,c)=R/P` is presently only an object assignment. The lock
does not specify the category of transitive normalized marked action
groupoids on which `S` is defined, the target category of homogeneous
`R`-spaces, or `S(F)` for a strict marked isomorphism. Nor does it state the
naturality equation for the based maps. Consequently “the unbased standard
homogeneous-space isomorphism class may be canonical after functoriality” has
no falsifiable theorem signature. Basepoint changes being rotations is not a
substitute for functoriality.  
**Minimum repair:** define a category whose objects satisfy the exact
normalization and closed-discrete stabilizer assumptions from M3. For a
strict marked isomorphism `F`, define the induced map, expected here to be
`S(F)([t])=[t]` after proving equality of the relevant subgroups, and require

```text
F_0 o theta_x = theta_(F_0 x) o S(F).
```

Prove identity and composition laws as explicit `P12-8` obligations. State
how `theta_(x dot u)` differs from `theta_x` by translation and distinguish
the canonical unbased object from every chosen based chart. If scaled maps
are discussed, type their separate induced dilation rather than letting it
enter the strict functor silently.

### M5 — The standalone nonredundancy gate is principled but not operational

**Location:** `research_protocol.md` Sections 1, 9, and 11;
`candidate_lock.md` Sections 1--3 and 8.  
**Why Major:** the lock correctly says that Paper 12 must fail as a standalone
paper if it reduces to Paper 11's time-factorization lemma plus Deninger's
stabilizer. Yet every current positive target is, at design level, compatible
with exactly that reduction: the all-degree theorem adds the iterated nerve
chart and face identities; `H^1` adds the continuous Cauchy classification;
period recovery evaluates the coordinate cocycle on the source-owned
stabilizer; and the category/quotient statements are elementary consequences
of retaining or forgetting clock scale. The adjective “substantive” and the
six-item eligibility list do not say what evidence would distinguish a
standalone categorical theorem from a technically correct appendix to Paper
11. A bounded search finding no exact conjunction is necessary but is not by
itself a nonredundancy theorem; conjunction novelty can be manufactured by
packaging standard consequences.
  
**Minimum repair:** add a pre-registered Paper-9--11 delta matrix giving, for
each Paper-12 theorem, its exact new premise, conclusion, and proof obligation
beyond the inherited statements. Freeze a standalone decision rule such as:

```text
STANDALONE_PASS requires all-degree natural chain-level reduction plus the
fully typed marked-category/non-descent theorem and the normalized quotient
functor, each absent from P9--P11, together with a bounded exact-package
precedent audit and a nearest-precedent comparison.

If the chain theorem is only a routine degreewise restatement and the
category/quotient package has a direct standard precedent, classify the work
as TECHNICAL_NOTE_OR_MERGE even when every formula is correct.
```

The Phase-2 novelty report must separate generic background, direct
continuous-groupoid-cohomology precedent, P9--P11 internal prior use, and the
rational-Witt application. Retain `SUPPORTED_WITHIN_SEARCH`; never infer
priority from a zero exact-string hit.

### M6 — `P12-9` is called deterministic, but several controls are not frozen enough to reproduce

**Location:** `research_protocol.md` Section 8 and target `P12-9`;
`candidate_lock.md` Sections 3 and 7.  
**Why Major:** the control classes are mathematically appropriate, but a
“random integer” and “random label” have no fixed value, seed, generator, or
manifest contract. The nontransitive action and non-`T0` coefficient controls
do not name their carrier, action, coefficient group, degree, or witness
cochain. `X_L` also lacks the explicit translation formula even though the
scaled-isomorphism audit depends on it. A later implementer could select
examples after seeing the result, and independent reproduction would not
have exact expected outputs. This leaves the registered deterministic target
not testable on the locked bytes.
  
**Minimum repair:** freeze a finite control table before proof work. At
minimum it should specify:

- `X_L=R/LZ` as a set with the indiscrete topology and action
  `[r]_L dot t=[r+t]_L`;
- fixed `L` values representing prime, composite, and nonarithmetic clocks,
  plus any pseudorandom value generated from a recorded algorithm and seed;
- a global-indiscrete nontransitive disjoint carrier such as two translation
  orbits with explicitly different stabilizers;
- a named non-`T0` topological abelian coefficient group, a nontrivial
  indiscrete `X`, the cochain degree, the exact cochain formula, and the two
  same-time points witnessing failure of factorization;
- the positive scaled map, its inverse, an unequal-period no-strict witness,
  and the orientation-reversing subgroup-preserving witness required by M1;
- exact expected pass/fail fields, tolerance policy (if any), source hash,
  script path, manifest path, and independent reproduction command.

Controls remain finite witnesses and falsifiers; they must not be presented
as proofs of the universal nerve or cochain theorems.

## 4. Minor findings

### m1 — The RQ reverses the direction of the induced cochain map

`research_protocol.md` Section 1 says that time projection induces an
isomorphism “from” the groupoid cochain complex “to” the group complex, but
the frozen map is the pullback

```text
T_n=pi_n^*:C_cont^n(R;A) -> C_cont^n(G;A).
```

Since cochains are contravariant, replace the RQ wording by “time projection
induces a pullback isomorphism from the `R` complex onto the groupoid complex”
and separately name its inverse, for example evaluation on a chosen section.
The inverse is independent of the chosen unit only after the factorization
theorem, so that independence should be an explicit obligation rather than a
silent reversal of arrows.

### m2 — The packet gate should bind the already available common-stabilizer source claim, not search for an unspecified new packet owner

Paper 9's locked source audit records Deninger's fixed-prime packet with
common stabilizer `p^Z`, and its proof audit establishes the exact actual
packet topology and unit-exponent exhaustion. The current `NOT_TESTABLE`
default is appropriately cautious, but Phase 2 should be told exactly what
would close it: bind Deninger physical pp. 38--39, Section 6/Theorem 6.1 for
the packet action and common stabilizer, and bind Paper 9's exact
`Gamma_p` owner/topology separately. State whether the Paper-12 packet
groupoid is the restriction of the same action to all of `Gamma_p`, and
verify `c(x,t)=t` on that owner. Do not require or invent a new packet action,
and do not borrow fixed-orbit topology as packet topology without the Paper-9
packet theorem.

## 5. Requested-domain audit

| Domain | Methodology verdict | Reason |
|---|---|---|
| RQ tightness | **MAJOR REVISION** | Pullback direction is reversed in prose, and “precisely” conflates sufficient strict invariance with a false converse and existential non-descent (M1, m1). |
| All-degree nerve/cochain target | **PASS WITH TYPING REVISION** | Every degree and both bijectivity/differential commutation are registered; coefficient and quotient type must be frozen (M2). |
| Coefficient/module/domain definitions | **MAJOR REVISION** | Constant coefficient bundle, unnormalized status, and algebraic versus topological cohomology are unresolved (M2). |
| Differential and signs | **PASS AT DESIGN LEVEL** | `d^0`, all higher signs, range-first multiplication, direct `d^2=0`, and chain-map checks are explicit; no Phase-3 truth verdict is issued here. |
| Generic versus arithmetic owners | **PASS** | The generic complex is action-blind and receives no arithmetic credit; the marked fixed-orbit owner inherits only source-gated arithmetic input. |
| Marked/scaled/unmarked categories | **MAJOR REVISION** | Categories are not fully typed, and exact period preservation cannot characterize strictness (M1). |
| Isotropy restriction | **PASS AT DESIGN LEVEL** | Homomorphism, coboundary invariance, basepoint behavior, scale dependence, and fixed-orbit source gate are all separately registered. |
| Standard period quotient | **MAJOR REVISION** | `R/Per(b)` is not the orbit homogeneous space for arbitrary scaled marks (M3). |
| Period-quotient functoriality | **MAJOR REVISION** | No category, morphism assignment, identity/composition law, or naturality square is frozen (M4). |
| Packet promotion | **MINOR REVISION / SOURCE-GATED** | The nonpromotion gate is sound; exact existing packet locators should be named (m2). |
| Controls and falsifiers | **MAJOR REVISION** | Control classes are good, but random and negative witnesses are not deterministic exact records (M6). |
| Standalone nonredundancy | **MAJOR REVISION** | The intended failure rule is not operational against the strong P11/P9 inheritance (M5). |
| Novelty ceiling | **PASS WITH M5 AMENDMENT** | `SUPPORTED_WITHIN_SEARCH` and no-priority language are correct; exact-package absence cannot alone establish standalone contribution. |
| Route A | **PASS AT DESIGN LEVEL** | Generic `A0/A1` failure, source-gated actual A0, `A1_WEAK` ceiling, and universal `A2/A3/A4` failure are nonconflated; final coordinates remain unproved. |
| Route B | **PASS** | Invocation is false, no Route-B YAML is allowed, and no operator/domain/determinant claim is imported. |
| Phase discipline | **PASS** | Phase 2 and Phase 3 remain blocked; the present review neither browses nor proves active targets. |

## 6. Mandatory amendment and re-lock checklist

All items below are mandatory because this pipeline requires zero unresolved
Critical, Major, or Minor findings for `PASS`.

1. Replace the morphism-level “precisely/only” claim by strict-category
   invariance plus existential non-descent in the scaled and unmarked
   categories; fully define those categories and add the
   orientation-reversing preservation counterexample.
2. Define the constant coefficient bundle/action, pointwise cochain group,
   unnormalized nerve convention, `Z/B/H`, and algebraic quotient status;
   separate any topologized-cochain target.
3. Restrict the standard orbit quotient to the source-normalized coordinate
   clock and prove `Per_x(c)=H_x`, or separate `R/H_x` from
   `R/Per_x(b)` for arbitrary marked classes.
4. Define the source and target categories of `S`, the map `S(F)`, identity
   and composition obligations, basepoint-change law, and the naturality
   equation with `theta_x`.
5. Add a Paper-9--11 delta matrix and an exact standalone/merge decision rule;
   require nearest-precedent comparison in addition to the bounded exact-
   package search and retain the `SUPPORTED_WITHIN_SEARCH` ceiling.
6. Freeze every deterministic control owner, action, coefficient, witness,
   parameter/seed, expected output, manifest, and reproduction contract.
7. Correct the pullback direction in the RQ and name its inverse only after
   the unit-independence obligation is stated.
8. Bind the packet corollary to the exact Deninger and Paper-9 packet
   locators while preserving the fixed-orbit/packet owner split.
9. Issue a versioned Phase-1 design amendment and new exact-byte re-lock;
   do not edit the initial locks in place.
10. Re-run independent methodology, domain/source, and devil's-advocate
    reviews on the amended bytes. Phase 2 remains blocked until every report
    says `C0 / M0 / m0`.

## 7. Gate decision

```text
phase1_methodology_gate: REVISE
critical: 0
major: 6
minor: 2
phase2_authorized: false
route_a_evaluation_authorized: false
route_b_yaml_authorized: false
```

The smallest safe next step is a narrow design amendment and exact-byte
re-lock. No source search, novelty conclusion, target proof, or Route
promotion is authorized by this review.

---

## 8. Amended-v1 exact-byte methodology re-lock addendum

Re-lock date: **2026-08-15 (Asia/Shanghai)**  
Scope: **amended four-artifact tuple only; no browsing, other-review-report
inspection, Phase-2 source/novelty adjudication, Phase-3 proof, or control
execution**  
Base review SHA-256 before this addendum:
`797e194f9b02f236c5c5b103cac09b63a55078f46b3a269ccea3ebfc61775008`  
Verdict: **REVISE — C0 / M0 / m2**

### 8.1 Exact amended tuple

| Active artifact | SHA-256 | Match |
|---|---|---|
| `notes/research_protocol.md` | `a923bfcf5fbae2d3136632794f0eb68ce4b7e48f217f0a071295e9fe4a85dda5` | yes |
| `notes/candidate_lock.md` | `0932d8a388ce732a3ad0702f3703cc91088d2fa73cc02f0a8063d240d70f5a42` | yes |
| `notes/pipeline_state.md` | `9cb7c51c534fd26f68fb66853312b022202c1d58b0ff2d74910c4deb3b32059b` | yes |
| `notes/phase1_design_amendment.md` | `76684044f434c8084712e558c32ee47e996a84763a3eca405f7014ab3d77f949` | yes |

All four artifacts were read in full. The other reviewers' reports were not
opened; the review-verdict rows embedded in the amendment were treated only
as part of the amendment's submitted bytes. The active locks were not edited.

### 8.2 Original-finding closure audit

| Initial finding | Amended-v1 disposition | Re-lock result |
|---|---|---|
| M1 — strict iff / universal-loss overclaim | The RQ and Section 6 now state scaled covariance, strict sufficiency, existential non-descent, and the `F_-` nonconverse. The three categories have objects, morphisms, identities, composition, and inverses. | **CLOSED** |
| M2 — coefficient and cohomology typing | The constant bundle and identity action, author-defined unnormalized complex, pointwise group law, face differential, algebraic `Z/B/H`, real-vector-space specialization, and no-topology ceiling are frozen. | **CLOSED** |
| M3 — `R/Per(b)` versus the action orbit | The orbit quotient is restricted to the normalized coordinate class with `Per_x([c])=H_x`; arbitrary scaled classes receive a separate value-space quotient. | **CLOSED** |
| M4 — absent quotient-functor contract | `C_str`, `Hom_(R,0)^std`, `S(F)`, well-definedness, identity, composition, naturality, basepoint rotation, and the scaled semilinear stop are explicit. | **CLOSED** |
| M5 — nonoperational standalone rule | A Paper-9--11 delta matrix, nearest-precedent comparison, `STANDALONE_PASS`, and `NOTE_OR_MERGE` branches are now preregistered. The remaining packet-branch wording conflict is separately recorded as new `m3` below. | **CLOSED AS ORIGINALLY FRAMED** |
| M6 — nondeterministic controls | Carriers, actions, constants, coefficient witness, scaled/reversed maps, label controls, paths, tolerance, seed status, minimum test count, two-generation identity, verify-only, tamper rejection, and cache hygiene are frozen. | **CLOSED** |
| m1 — pullback direction | `T_n=pi_n^*` is correctly contravariant, and evaluation is an inverse only after unit-independence is proved. | **CLOSED** |
| m2 — packet owner and source binding | Orbit, packet, and excluded global owners are separate; the exact Deninger and Paper-9 source roles and the every-unit packet checks are frozen. | **CLOSED** |

### 8.3 Cross-surface audit

| Surface | Re-lock result | Basis |
|---|---|---|
| Algebraic author-defined complex | **PASS AT DESIGN LEVEL** | No unqualified standard-cohomology claim, normalized-subcomplex claim, or quotient topology remains. |
| All-degree target and signs | **PASS AT DESIGN LEVEL** | Every degree, face maps, range-first product, direct `d^2=0`, chain commutation, and inverse obligations are explicit; no truth verdict is issued here. |
| Pullback direction | **PASS** | Cochain contravariance and the conditional evaluation inverse are exact. |
| Categories, covariance, and non-descent | **PASS AT DESIGN LEVEL** | Strict preservation is not used as a converse; weaker-category failure is existential and has unequal-period and orientation-reversal controls. |
| Normalized quotient functor | **PASS AT DESIGN LEVEL** | Orbit and value-space quotients are separated, and functorial/naturality ceilings are explicit. |
| Packet owner | **PASS WITH NEW m3** | Same-owner action/clock/stabilizer gates are exact; only the standalone fallback consequence is inconsistent. |
| Deterministic controls | **PASS AT DESIGN LEVEL** | The package is reproducibly specified and remains a witness layer rather than a proof substitute. |
| Standalone/nonredundancy | **PASS WITH NEW m3** | The delta and merge rule are substantive; the packet-unavailable branch must have one outcome. |
| Novelty ceiling | **PASS** | Comparator/search requirements are preregistered, and `SUPPORTED_WITHIN_SEARCH` is the only negative-search language. |
| Route A/B boundary | **PASS WITH NEW m4** | The negative ceiling and no-Route-B rule are sound; the Route-A serialization record is not yet schema-complete. |
| Release/source-byte boundary | **PASS** | Generated outputs, local evidence PDFs, canonical bibliography endpoints, companion dependency handling, and public-sync payload checks are separated. |
| Pipeline discipline | **PASS** | Phase 2, Phase 3, Route evaluation, and release remain blocked on their proper gates. |

### 8.4 New minor findings

#### m3 — The standalone packet-unavailable branch has two incompatible outcomes

`research_protocol.md` Section 1 first makes standalone eligibility depend on
a source-verified packet corollary **or a documented reason it is
unavailable**. Its immediately following executable `STANDALONE_PASS` rule,
however, requires a source-verified packet corollary without the alternative.
Sections 5 and 11 and `candidate_lock.md` Section 5 then use the weaker phrase
“packet decision,” under which `ORBIT_ONLY` could appear sufficient. These
wordings yield different release decisions if the every-unit packet gate
fails honestly. Replace all occurrences with one rule: either
`PACKET_COROLLARY` is mandatory for `STANDALONE_PASS` and `ORBIT_ONLY` forces
`NOTE_OR_MERGE`, or a documented `ORBIT_ONLY` outcome is explicitly accepted
and the executable rule lists its additional standalone conditions. The
mathematical packet owner itself is correctly typed.

#### m4 — The frozen Route-A record does not list every mandatory evaluator key

`research_protocol.md` Section 10 and `candidate_lock.md` Section 6 say the
later Route-A record has every mandatory input, but their displayed record
starts at `candidate_definition`. The Route-A evaluator's required schema
also has distinct fields

```text
candidate_id
family
phase_space
dynamics
parameters
parameter_provenance
```

before `arithmetic_origin`, in addition to the fields already displayed.
Values for most of these can be inferred from the owner dictionary, but an
exact-schema evaluation must not reconstruct required keys by guesswork.
Add all six keys per typed owner, give `artifact_paths` exact paths rather
than “Stage-12 YAML,” and require the pending `code_commit` placeholder to be
resolved to the final content/commit identifier before `P12-10` executes.
This does not change the negative A2/A3/A4 ceiling or authorize Route B.

### 8.5 Mandatory amended-v2 checklist

1. Harmonize the packet-unavailable branch across the eligibility list,
   executable standalone rule, target section, candidate decision
   vocabulary, and amendment ledger.
2. Add the six omitted mandatory Route-A keys for every evaluated owner,
   freeze exact artifact paths, and make final commit/content-hash resolution
   a `P12-10` precondition.
3. Issue amended v2 as a versioned tuple; do not mutate or relabel the
   amended-v1 history.
4. Re-run the three independent exact-byte re-locks. Phase 2 remains blocked
   until all three amended reports are `C0 / M0 / m0`.

### 8.6 Re-lock decision

```text
amended_v1_methodology_gate: REVISE
critical: 0
major: 0
minor: 2
phase2_authorized: false
phase3_authorized: false
route_a_evaluation_authorized: false
route_b_yaml_authorized: false
```

Amended v1 closes the full original `C0/M6/m2` methodology ledger. It does
not meet the mandatory zero-finding re-lock because the two new exactness
issues remain. The next safe step is a two-item amended-v2 correction and
fresh exact-byte re-lock, not source search or Phase-3 proof work.

---

## 9. Amended-v2 exact-byte methodology re-lock addendum

Re-lock date: **2026-08-15 (Asia/Shanghai)**  
Scope: **narrow amended-v2 methodology/nonredundancy re-lock of the exact
five-artifact tuple; no browsing, other-review-report inspection, Phase-2
source/novelty adjudication, Phase-3 proof, control execution, or Route
evaluation**  
Base review SHA-256 before this addendum:
`ba9e54f81847a4184463a206b0424177e4436702569b8dd39a995d7bf965382d`  
Verdict: **PASS — C0 / M0 / m0**

### 9.1 Exact amended-v2 tuple

| Bound artifact | SHA-256 | Match |
|---|---|---|
| `notes/research_protocol.md` | `9c4947880f894dabb0648e9434fdf6e3a28cf2d9bf6434f86579370d8da80087` | yes |
| `notes/candidate_lock.md` | `1893cb74a5fc1a004873d5d027faf58bb384c3419699675dd37f33ee7b13c14f` | yes |
| `notes/pipeline_state.md` | `971489c1208ef32082bf936bf6c8b45661740d9b867857250a02798e02fafb62` | yes |
| `notes/phase1_design_amendment.md` | `76684044f434c8084712e558c32ee47e996a84763a3eca405f7014ab3d77f949` | yes |
| `notes/phase1_design_amendment_v2.md` | `26222c9e6888f0aa45d019a9f1fd74038285ac460ae6aa0342b8b4e01b4c3285` | yes |

All five artifacts were read in full. The active protocol, candidate lock,
pipeline state, and both versioned amendments were not edited. No other
review report was opened; review-outcome rows embedded in the v2 amendment
were treated only as bytes of that submitted amendment.

### 9.2 Closure of amended-v1 minor findings

#### m3 — packet branch: CLOSED

The active protocol now gives one rule in its eligibility gate, executable
standalone predicate, packet target, and release decision:

```text
PACKET_COROLLARY is mandatory for STANDALONE_PASS.
ORBIT_ONLY forces NOTE_OR_MERGE.
```

The candidate lock repeats the same implication, and the v2 amendment
records it as the sole branch. There is no active “documented unavailable”
or generic “packet decision” alternative that could promote `ORBIT_ONLY` to
standalone release. Packet failure still omits the packet claim and changes
no orbit-level mathematical owner.

#### m4 — Route-A intake schema: CLOSED

The protocol freezes exactly seven nonconflated records. Each record supplies
all ten owner-specific fields:

```text
candidate_id, candidate_definition, family, phase_space, dynamics,
parameters, parameter_provenance, arithmetic_origin, clock, normalization
```

Each record also receives all seven common required fields:

```text
determinant_convention, orbit_cutoff, precision, training_data,
forbidden_data, code_commit, artifact_paths
```

The candidate lock expands the seven exact row-specific paths
`evaluations/route_a/<candidate_id>/2026-08-15-stage12.yaml`, consistently
with the protocol template, and the protocol freezes the exact Paper-12
proof-audit, manifest, peer-review, and Route-audit paths. `P12-10` is
explicitly blocked until every path exists and its final SHA-256 is
serialized in the YAML and Route audit. The value
`unavailable-no-git-content-sha256-lock-required` is explicitly a resolved
no-Git provenance state rather than a pending placeholder; final
implementation and artifact content hashes are mandatory substitutes.

The seven records are exactly:

1. `GEN-INDISC-R-ACTION-CNV`
2. `DEN-EF-ACTUAL-ORBIT-CNV-P-A`
3. `DEN-EF-ACTUAL-PACKET-CNV-P`
4. `DEN-EF-ACTUAL-ORBIT-MARKED-PERIOD-P-A`
5. `DEN-EF-ACTUAL-PACKET-MARKED-PERIOD-P`
6. `DEN-EF-STANDARD-PERIOD-QUOTIENT-P`
7. `UNMARKED-PERIOD-SCALING-CONTROL`

The negative determinant convention, owner separation, A1 ceiling,
`A2/A3/A4` ceiling, and false Route-B invocation remain unchanged.

### 9.3 Regression audit of every prior closure

| Finding or repair surface | Amended-v2 result | Regression check |
|---|---|---|
| M1 — categories, covariance, and non-descent | **CLOSED** | Strict preservation remains sufficient rather than iff; scaled and unmarked loss is existential, with the unequal-period and orientation-reversal controls retained. |
| M2 — author-defined cochain complex | **CLOSED** | Constant coefficients, identity module action, unnormalized all-degree cochains, algebraic `Z/B/H`, and the no-topology ceiling remain explicit. |
| M3 — normalized orbit quotient | **CLOSED** | The source-normalized coordinate class owns `Per_x([c])=H_x`; arbitrary scaled classes retain the separate value-space quotient. |
| M4 — quotient functor | **CLOSED** | Source/target categories, `S(F)`, well-definedness, identities, composition, naturality, and the scaled semilinear stop remain frozen. |
| M5 — standalone nonredundancy | **CLOSED** | The Paper-9--11 delta, nearest-precedent comparison, and executable merge rule remain intact and are now packet-branch consistent. |
| M6 — deterministic controls | **CLOSED** | Owners, actions, witnesses, frozen parameters, paths, tolerance, minimum counts, verify-only behavior, tamper rejection, and cache hygiene are unchanged. |
| m1 — pullback direction | **CLOSED** | `T_n=pi_n^*` remains contravariant; evaluation is named as inverse only after unit-independence. |
| m2 — packet owner/source split | **CLOSED** | Orbit, packet, and excluded global owners remain separate, with same-owner action, clock, stabilizer, and every-unit source gates. |
| v1 m3 — packet release branch | **CLOSED** | Mandatory `PACKET_COROLLARY` and `ORBIT_ONLY => NOTE_OR_MERGE` now agree everywhere active. |
| v1 m4 — Route schema | **CLOSED** | Seven complete 17-field records, exact paths, resolved no-Git provenance, and the final-SHA precondition are explicit. |
| Release/source-byte boundary | **PASS** | Local evidence, canonical bibliography endpoints, generated outputs, companion dependencies, and public-sync checks remain separated. |
| Route A/B boundary | **PASS AT DESIGN LEVEL** | Complete inputs remove the schema defect without pre-judging formal evaluator results or creating Route YAML. |
| Phase discipline | **PASS** | No source conclusion, target proof, control result, Route verdict, or manuscript-release authority is inferred from this re-lock. |

No amended-v2 edit reopens an original or v1 closure. In particular, the
all-degree differential/sign obligations, generic-versus-arithmetic owner
split, marked/scaled/unmarked category split, period-quotient naturality,
novelty ceiling, deterministic controls, and release boundary remain
internally consistent at the preregistered design level.

### 9.4 Findings and mandatory amendment checklist

```text
critical_findings: 0
major_findings: 0
minor_findings: 0
mandatory_methodology_amendments: NONE
```

The zero-finding requirement is met. There is no methodology amendment item
to carry forward from this review. This is a design-contract verdict only;
it does not prove any Phase-3 target or adjudicate the later source and
novelty searches.

### 9.5 Re-lock decision

```text
amended_v2_methodology_gate: PASS
critical: 0
major: 0
minor: 0
methodology_blockers_remaining: false
phase2_authorized_by_this_report_alone: false
phase3_authorized: false
route_a_evaluation_authorized: false
route_b_yaml_authorized: false
```

The methodology/nonredundancy component of the amended-v2 Phase-1 re-lock is
complete. Downstream authorization still requires the other independent
re-locks and the pipeline's aggregate zero-finding gate on this same exact
tuple.
