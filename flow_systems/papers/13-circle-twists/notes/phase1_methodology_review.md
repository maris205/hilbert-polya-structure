# Paper 13 Phase-1 methodology and nonredundancy review

Review date: **2026-08-15 (Asia/Shanghai)**  
Review role: **independent ARS methodology/domain reviewer**  
Review mode: **read-only theoretical protocol review**  
Verdict: **MAJOR REVISION / Phase 2 remains blocked — C0/M5/m3**  
Confidence: **5/5 for internal methodology, convention, owner, and gate
consistency; no source-currentness or completed-proof verdict is issued**

## 1. Exact scope and lock

This report reviews only these three active Phase-1 artifacts:

| Artifact | Independently recomputed SHA-256 |
|---|---|
| `notes/research_protocol.md` | `99a6552621ebc38f0288255d34fc3bdca6dd4e8fe2fd8c5db4ec4d7594d7769e` |
| `notes/candidate_lock.md` | `3dd4f8ece7469edc0f5e55447b94e632281b66cb95792a7a10cbe370bc74c6f0` |
| `notes/pipeline_state.md` | `f4ed05d837414549d8cfecb4d2d05668fcea4cc2b148dbff5d5fe1dce73c2ad8` |

The review did not read any sibling Paper-13 Phase-1 review, manuscript,
proof artifact, implementation, control output, Stage-13 Route file, or Route
audit. It used no web browsing and ran no proof, code, control, Route, Git, or
public-sync action. The inherited Paper-9/11/12 hashes were assessed only as
statements inside the active locks; this lane did not open or revalidate
those upstream artifacts. The only write is this report.

The applicable ARS academic-paper-reviewer, methodology-reviewer,
domain-reviewer, and peer-review report instructions were read in full before
the lock was assessed. Because the proposed work is theoretical, empirical
sampling and statistical-reporting criteria are inapplicable; the operative
criteria are question-method alignment, definition precision, logical
closure, counterexample/falsifier design, owner attribution,
nonredundancy, and reproducible gate specification.

## 2. Summary assessment

The protocol asks a clear and answerable conditional question: after
globally continuous normalized circle two-cochains on an actual globally
indiscrete action groupoid collapse to time, do their gauge classes, twisted
global-QC algebras, or transported completions retain the action or marked
period? The coefficient topology, normalized cocycle equation, coboundary
sign, quadratic control, product, involution, and gauge-map direction are
mutually compatible. The proposed lift–integer-defect–real-cocycle route to
the candidate `H^2` collapse is methodologically plausible and is correctly
kept unproved. The protocol also has good hard stops against proxy-topology
transfer, standard actual-groupoid `C*` promotion, finite-controls-as-proof,
and premature Route B.

The current bytes nevertheless cannot clear Phase 1. Most importantly,
P13-1 is already within the Paper-12 all-degree `T0` factorization owner and
must not be presented as a fresh Paper-13 result. Once that correction is
made, the standalone contribution becomes materially less certain, yet the
current standalone test does not operationally distinguish a genuinely new
owner-specific theorem from a formal composition of Paper 12, standard
one-object multiplier theory, and Paper 11. The retention predicate is not
yet a defined invariant, the regular-representation and norm-transport
directions are not frozen, and P13-10 lacks an exhaustive Route owner
registry. These are repairable Phase-1 design defects, not evidence that the
candidate theorem is false. An amended tuple should receive a new independent
Phase-1 review before Phase 2.

## 3. Strengths

### S1. The normalized cochain signs are coherent

The range-first right-action cocycle identity and the declared multiplicative
coboundary use the same composable-pair convention. Normalization on both
axes is explicit, and the one-object formulas are the exact time-only
specialization.

**Evidence Anchor:** `equation: research_protocol.md §3, lines 87–116 — normalized one-/two-cochains, multiplier identity, and delta convention`

### S2. The quadratic control checks the nontrivial gauge direction

With the frozen sign,
`delta alpha_kappa(t,u)=exp(i kappa t u)=sigma_kappa(t,u)`. Thus the
quadratic family is a valid sign control, and the protocol correctly refuses
to generalize from that family to all multipliers.

**Evidence Anchor:** `equation: research_protocol.md §6, lines 198–207 — sigma_kappa and alpha_kappa`

### S3. The candidate `H^2` collapse is held at the correct epistemic status

The locks call vanishing conjectured/unproved and require a direct lift,
normalization, integer-defect, real-cocycle, exponentiation, and uniqueness
argument. A nearby source theorem is not permitted to replace the exact
same-convention proof.

**Evidence Anchor:** `text: research_protocol.md §8, lines 250–267 "If a direct contracting argument cannot be completed, the candidate conclusion remains open"`

### S4. Actual/proxy and completion firewalls are explicit

The protocol forbids importing a standard actual-groupoid `C*` norm, permits
transport only after a continuous gauge-star isomorphism, and disallows a
completion map inferred from an actual-to-standard proxy.

**Evidence Anchor:** `text: candidate_lock.md Hard domain locks 6–7 "Full/reduced norms may be author-transported only after a continuous gauge-star isomorphism is proved"`

### S5. Controls and Route are correctly held downstream

The current state makes proof, controls, Route, manuscript, and release
false; requires a future exact control-design amendment; and imposes the
acyclic Route order `upstream stable tuple -> YAMLs -> route_audit ->
composition` with no self-hash.

**Evidence Anchor:** `text: research_protocol.md §§11 and 13 "No Stage-13 Route YAML or Route audit may exist before final proof"`

## 4. Weaknesses and exact fixes

### W1. P13-1 is assigned to the wrong novelty owner

**Problem:** The protocol says Paper 12 owns marked degree-one cohomology and
the actual-versus-standard comparison, while P13-1 is marked
`SPECIFIED / UNPROVED`. But the same lock also binds Paper 12 and describes
its all-degree `T0` time-factorization result. Since the usual circle is
Hausdorff and hence `T0`, factorization of continuous circle-valued
two-cochains on `X_indisc x R^2` is already the degree-two specialization of
that Paper-12 theorem. Normalization does not create a new factorization
argument.

**Why it matters:** This overstates freshness at the first step of the
candidate center and distorts both owner credit and the later standalone
test. It could allow an inherited theorem to be counted as a Paper-13
contribution.

**Exact fix:** Amend all three locks as follows:

1. In the inherited-owner ledger, state explicitly that Paper 12 owns the
   all-finite-degree `T0` coefficient factorization, including the
   circle-valued degree-two case.
2. Change P13-1 from `SPECIFIED / UNPROVED` to
   `INHERITED COROLLARY / EXACT-LOCK REVERIFICATION REQUIRED`.
3. Give Paper 13 ownership only of the normalized multiplier/gauge
   specialization, the exact `H^2` classification under its frozen sign,
   and the twisted global-QC/retention consequences.
4. Replace the unqualified sentence “This is a fresh question” with a
   claim-level statement: the twist/gauge/completion/nonretention conjunction
   is the fresh candidate; the time-factorization premise is inherited.
5. Ensure the eventual abstract, title rationale, novelty matrix, and Route
   owners never count P13-1 as a new theorem.

**Severity:** Major  
**Evidence Anchor:** `text: research_protocol.md §§2.2, 7, and 12 "Paper 12 owns the marked-period and actual-versus-standard comparison" and "P13-1. Every globally continuous normalized"`  
**Confidence:** 5/5 — direct owner/claim comparison within the active lock

### W2. The standalone gate does not operationalize its own nonredundancy rule

**Problem:** Section 12 requires seven deliverables, then says a formal
composition of Paper-12 factorization with standard `H^2(R;T)=0` is
`NOTE_OR_MERGE`. Completion of the seven-item list does not itself distinguish
that prohibited formal composition: P13-1 is inherited; P13-2 is its
normalized specialization; P13-3 is a one-object classification; and
P13-4–P13-7 may all become formal gauge-transport consequences.

**Why it matters:** The current rule can return either `STANDALONE_PASS` or
`NOTE_OR_MERGE` on the same proof package without violating its text. This is
an underdetermined acceptance criterion for the paper's central
nonredundancy decision.

**Exact fix:** Before Phase 2, freeze a P11/P12/source/P13 claim-delta matrix
with one row for P13-1–P13-7 and these mandatory fields:

`claim_id`, `premise_owner`, `closest_P11_result`, `closest_P12_result`,
`standard_group_R_input`, `new_P13_lemma_or_construction`,
`derivable_by_direct_substitution`, `standalone_weight`, and
`failure_disposition`.

Set `NOTE_OR_MERGE` as the default unless an independent post-proof reviewer
identifies at least one central theorem whose proof requires a genuinely new
lemma/construction or owner-specific obstruction not obtainable by direct
substitution from Paper 11, Paper 12, and applicable group-`R` theory. If the
project instead intends exact typed synthesis itself to justify a standalone
paper, revise Section 12 to say that openly and define the threshold; do not
simultaneously say formal composition is insufficient. The standalone
review must occur before manuscript authorization and remain independent of
the proof author.

**Severity:** Major  
**Evidence Anchor:** `text: research_protocol.md §12, lines 330–348 "If the result is only the formal composition"`  
**Confidence:** 5/5 — research-design and nonredundancy gate logic

### W3. “Retention” is not yet a mathematically registered invariant

**Problem:** Action retention is phrased as distinguishing two
“registered nonisomorphic” actions, but the isomorphism category and the
allowed algebra/completion equivalence are not defined. Period retention is
phrased as a “gauge-invariant restriction to isotropy,” but neither its
quotient codomain nor the comparison across different stabilizer subgroups
is specified. Failure to find a distinguishing pair is not, by itself, a
proof of universal action blindness.

**Why it matters:** P13-6 and P13-7 are central negative conclusions. Without
a fixed invariant and equivalence relation, a representative-dependent
isotropy value, an abstract algebra isomorphism, and a gauge-induced
isomorphism could be interchanged after results are known.

**Exact fix:** Replace Section 6 with formal registrations containing all of
the following:

1. Define the action category and “nonisomorphic”: for example, nonempty
   globally indiscrete right-`R` sets with strict equivariant bijections, and
   state separately whether marked/scaled maps are admitted.
2. Define the three compared outputs separately: the normalized gauge class,
   the twisted test-algebra isomorphism class, and each transported completion
   class. For each, state whether equivalence means gauge-induced star
   isomorphism, isometric star isomorphism, or arbitrary abstract
   star isomorphism.
3. Define action-blindness universally: every registered owner must map,
   naturally or by the explicitly allowed equivalence, to one
   action-independent record. Retention is the existence of a pair whose
   registered outputs are inequivalent; nonretention requires the universal
   proof, not an unsuccessful search.
4. Define an isotropy restriction map. One safe choice is
   `Res_x([sigma])=[sigma|_(H_x x H_x)]`, with the target quotient and the
   allowed restricted gauges stated explicitly. If only restrictions of
   globally continuous gauges are allowed, say so; if all continuous
   `H_x`-gauges are allowed, say so and use the subspace topology on `H_x`.
5. State how outputs attached to different literal subgroups are compared.
   The negative theorem should say that a global trivializer restricts to
   every `H_x`, so every registered restriction class is zero; it must not
   infer blindness merely because a chosen representative was gauged away.
6. Keep dense stabilizers outside the common-lattice marked-period category
   unless a separate marked object is defined for them.

**Severity:** Major  
**Evidence Anchor:** `text: research_protocol.md §6, lines 176–184 "It retains a marked period only if a gauge-invariant restriction to isotropy changes"`  
**Confidence:** 5/5 — core expertise in invariant/equivalence specification

### W4. P13-4/P13-5 leave the regular representation and norm direction unfrozen

**Problem:** The time-only twisted product, involution, and `U_alpha` are
written, but the actual-fibre formula, Haar/modular convention, intrinsic
twisted left-regular representation, unitary intertwiner, and exact
transported norm definitions are absent. Section 5 merely lists “the exact
unit-regular representation and sign convention” as a future obligation.

**Why it matters:** These missing formulas are where a gauge inverse,
`sigma(u,t-u)` versus its conjugate, `x` versus `x.u`, or the wrong unitary
conjugation can change associativity, the star law, and the reduced norm.
P13-4 and P13-5 are not reproducibly specified until the direction is frozen.

**Exact fix:** Add the following convention block before proof or control
design, with `dt` as Haar measure and modular function one:

```text
(F *_sigma G)(x,t)
  = integral_R F(x,u) G(x.u,t-u) sigma(x;u,t-u) du,

F^{*sigma}(x,t)
  = overline{sigma(x;t,-t)} overline{F(x.t,-t)}.
```

Require the proof to show
`sigma(x;t,-t)=sigma(x.t;-t,t)` from normalization and the cocycle identity.
After time factorization, freeze

```text
(Lambda_sigma(f)xi)(t)
  = integral_R f(u) sigma(u,t-u) xi(t-u) du.
```

For `sigma=delta alpha`, define `M_alpha xi(t)=alpha(t)xi(t)` and record the
direction

```text
Lambda_sigma(f) = M_overline(alpha) lambda(U_alpha f) M_alpha,
||f||_(r,sigma,alpha) = ||lambda(U_alpha f)||,
||f||_(full,sigma,alpha) = ||U_alpha f||_(C*(R)).
```

If `beta` is another trivializer, fix one ratio convention, for example
`chi=beta/alpha`, prove `chi` is a continuous character, define
`C_chi h(t)=chi(t)h(t)`, state `U_beta=C_chi U_alpha`, and prove `C_chi`
is isometric for both transported norms. Distinguish the
intrinsic `Lambda_sigma` formula from the transported representation
`lambda o U_alpha`; do not call both “the regular representation” without
the intertwining statement.

**Severity:** Major  
**Evidence Anchor:** `absence: research_protocol.md §§4–5 — expected the actual-fibre product/star, twisted regular representation, intertwiner, and exact transported norms; checked lines 119–171 and candidate_lock.md Hard domain locks 5–7`  
**Confidence:** 5/5 — direct convention and operator-direction audit

### W5. P13-10 has no exhaustive pre-registered Route owner inventory

**Problem:** Section 2 registers three owner IDs, Sections 4–5 introduce
additional generic test-algebra and full/reduced transported records, and
Section 13 refers to generic factorization, gauge-collapse, fixed-prime, and
quadratic-control owners. P13-10 nevertheless says “every typed owner” will
be evaluated without fixing which records count as Route owners or how many
Stage-13 YAMLs must eventually exist.

**Why it matters:** The acyclic provenance order is good, but an unfrozen
owner set permits post-result inclusion, omission, or aggregation. That can
alter A0 credit and enable exactly the cross-owner donation the protocol
otherwise prohibits.

**Exact fix:** Add a Phase-1 Route owner registry that enumerates every
candidate owner class before results: generic cochain/gauge quotient,
generic twisted test algebra, generic full transport, generic reduced
transport, fixed-prime cochain/gauge application, fixed-prime twisted
global-QC record, and every control owner that will receive a Route verdict.
For each entry freeze `owner_id`, carrier/topology, mark/coefficient,
construction, eligible P13 claims, source-origin ceiling, and whether it is
`RESULT_OWNER` or `CONTROL_ONLY`. Freeze the expected YAML count to that
registry count; any later addition/removal must be a versioned pre-Route
amendment with independent review.

Replace the placeholder “upstream stable tuple” with an explicit required
provenance tuple: final proof, controls manifest, source/domain audit,
nonredundancy/standalone audit, and integrated gate hashes. Preserve the
already correct order `stable tuple -> YAMLs -> route_audit -> composition`,
the no-self-hash rule, owner-local A0–A4 evidence, and Route-B false ceiling.

**Severity:** Major  
**Evidence Anchor:** `absence: research_protocol.md §§2, 4–5, 7 P13-10, and 13 — expected an exhaustive Route owner registry and fixed eventual YAML count; checked all three active locks`  
**Confidence:** 5/5 — provenance and preregistration logic within active bytes

### W6. The gauge quotient is described verbally rather than registered algebraically

**Problem:** “Their quotient is delta a” is orientation-insensitive as an
equivalence relation, but the protocol does not define the normalized
cochain, cocycle, and coboundary groups or state that no topology is imposed
on the quotient. Later gauge maps do depend on the chosen orientation
`sigma=delta alpha`.

**Why it matters:** The omission is local, but explicit group notation will
prevent inverse conventions from drifting between classification,
retention, sources, and controls.

**Exact fix:** Define pointwise-multiplicative groups
`C^1_n,cont`, `Z^2_n,cont`, and
`B^2_n,cont=delta(C^1_n,cont)`, verify in the protocol that `delta a` is a
normalized multiplier, and set
`H^2_tw=Z^2_n,cont/B^2_n,cont` as an abstract group with no topology. Freeze
gauge orientation as `sigma'=(delta a)sigma`; for untwisting, separately say
`sigma=delta alpha` and `U_alpha:A_sigma->A_1`.

**Severity:** Minor  
**Evidence Anchor:** `text: research_protocol.md §3, lines 100–108 "Two multipliers are gauge equivalent when their quotient is delta a"`  
**Confidence:** 5/5 — local definition/convention audit

### W7. The conjecture-failure branch is not propagated through the pipeline

**Problem:** P13-5 is correctly conditional on P13-3, and Section 9 lists
sharp falsifiers, but the candidate and pipeline locks do not state what
happens to P13-4–P13-7 and the standalone decision if a nontrivial continuous
multiplier is found or the direct contracting argument fails.

**Why it matters:** The omission does not make the present conjecture
unsound, but it leaves room to continue a negative-retention narrative after
its universal premise has failed.

**Exact fix:** Add a fail-closed branch table:

- if P13-3 closes, continue to P13-4–P13-7 as registered;
- if a nontrivial class is found, freeze the counterexample, mark the
  universal P13-3/P13-6/P13-7 conclusions false, restrict P13-5 to the
  trivializable subclass, and return to Phase 1 with a new research question;
- if the direct proof remains open, do not substitute a nearby theorem with
  mismatched continuity/cochain conventions;
- if an exact same-package precedent is found, route disposition to
  `NOTE_OR_MERGE` before proof/manuscript authorization.

Mirror the chosen branch in `candidate_lock.md` and `pipeline_state.md`.

**Severity:** Minor  
**Evidence Anchor:** `absence: candidate_lock.md Candidate center/status table and pipeline_state.md — expected a fail-closed branch if P13-3 is false or remains open; checked P13-3–P13-7 statuses and every pipeline row`  
**Confidence:** 4/5 — theoretical project-contingency design

### W8. The control-design amendment needs its own pipeline gate and a dense-stabilizer boundary

**Problem:** Section 11 correctly requires a later schema/count freeze, but
`pipeline_state.md` has only a single blocked P13-8 implementation row. It
does not expose the prerequisite design-lock stage. The protocol also shifts
from “dense-stabilizer” to “dense-period,” although a dense stabilizer is not
the common discrete lattice used for the marked-period category; finite CSVs
cannot establish topological density in `R`.

**Why it matters:** This is a bounded planning defect. Without an explicit
gate, implementation could begin against filenames alone, and a finite
diagnostic could be overread as proof of density or marked-period behavior.

**Exact fix:** Add a pipeline row
`P13-8 deterministic-control design lock | BLOCKED | after amended Phase-1
exact-byte gate`, followed by the separate implementation row. Require the
future design amendment to freeze, for every CSV, schema version, exact row
formula, canonical ordering and serialization, oracle, exact expected row
count, negative-reason labels, tolerance (if any), and manifest bindings,
plus aggregate test/artifact/row/negative counts.

Use “dense-stabilizer” consistently. Register the actual dense-subgroup
example as proof-owned. Any executable bounded rational-window or finite
quotient surrogate must be labeled `FINITE_DIAGNOSTIC_ONLY` and must not
claim to verify density or the common-lattice marked-period theorem.

**Severity:** Minor  
**Evidence Anchor:** `text: research_protocol.md §§6, 7, and 11 "Before implementation, a versioned amendment must freeze exact schemas, row formulas, and expected counts"`  
**Confidence:** 5/5 — deterministic-design and claim-boundary audit

## 5. Convention and feasibility adjudication

| Item | Phase-1 methodology verdict | Required boundary |
|---|---|---|
| Coefficient group | PASS | Usual Hausdorff circle with trivial action is exact and `T0`. |
| Actual composable-pair chart | PASS | `X_indisc x R^2` is explicitly registered. |
| Two-cocycle identity | PASS | Correct for `(x,t)(x.t,u)(x.t+u,v)` in the frozen range-first convention. |
| Normalized coboundary | PASS | `delta a=a(x,t)a(x.t,u)overline{a(x,t+u)}` matches the multiplier convention. |
| Time-only reduction | MATHEMATICALLY ALIGNED / OWNER AMENDMENT REQUIRED | The `T0` factorization is exact but belongs to Paper 12 at P13-1. |
| Quadratic family | PASS AS CONTROL | `alpha_kappa=exp(-i kappa t^2/2)` has the stated `delta` sign; it is not a classifier. |
| Twisted product | ALIGNED / METHOD INCOMPLETE | The time formula has the correct `sigma(u,t-u)` direction; actual-fibre and regular formulas must be frozen. |
| Twisted involution | ALIGNED / METHOD INCOMPLETE | `overline{sigma(t,-t)}overline{f(-t)}` is compatible with normalization; actual-fibre form and equality with the inverse-first coefficient remain proof obligations. |
| Gauge map | PASS IN STATED DIRECTION | If `sigma=delta alpha`, `U_alpha f=alpha f` maps twisted product/star to untwisted; do not silently replace it by the inverse. |
| `H^2_tw(R;T)=0` | PLAUSIBLE, UNPROVED | The lift/defect/contraction route is coherent; the continuous real-cocycle coboundary step must close directly in the frozen convention. |
| Choice-independent norms | SPECIFIABLE, NOT YET FROZEN | Requires the formulas in W4 and a fixed `beta/alpha` character convention. |
| Generic nonretention | NOT YET ADJUDICABLE | Requires W3's universal invariant/equivalence definitions. |
| Fixed-prime application | OWNER FIREWALL PASS / RESULT OPEN | No standard topology is transferred; result awaits P13-3, W3, and proof. |
| Phase-2 source discovery | FEASIBLE AS A PLAN | The source classes are separated and bounded; this lane did not browse or verify them. |

## 6. P13-1–P13-10 method audit

| Target | Review status | Exact next gate |
|---|---|---|
| P13-1 | AMEND | Reclassify as Paper-12 inherited corollary and reverify the bound theorem/domain. |
| P13-2 | PROCEED AFTER AMENDMENT | Prove normalization, multiplier equation, and gauge quotient are preserved by the inherited factorization. |
| P13-3 | PROCEED CONDITIONALLY | Complete direct exact-sign proof and independent same-domain source audit; retain conjectured status until then. |
| P13-4 | AMEND | Freeze actual-fibre product/star, Haar convention, intrinsic regular representation, and gauge intertwiner before proof/controls. |
| P13-5 | AMEND | Freeze full/reduced transported norm formulas, choice ratio, isometries, and amenability-only equality route. |
| P13-6 | AMEND | Replace witness-style retention language with W3's universal registered invariant. |
| P13-7 | PROCEED ONLY AFTER P13-3/P13-6 | Keep source/companion facts at their current ceilings and transfer only the typed negative result. |
| P13-8 | AMEND GATE | Add a control-design-lock stage; no implementation until exact schema/count/oracle freeze. |
| P13-9 | PROCEED IN PHASE 2 | Bounded primary-source and exact-conjunction searches are well scoped; retain `SUPPORTED_WITHIN_SEARCH`. |
| P13-10 | AMEND | Freeze exhaustive Route owner registry and eventual YAML count before any result-driven selection is possible. |

## 7. Exact amendment checklist

The next candidate tuple should not request re-review until every item below
is closed on exact bytes.

| ID | Required lock change | Closure evidence expected in amended bytes |
|---|---|---|
| A1 | Correct Paper-12 ownership of all-degree `T0` factorization and P13-1 status | owner ledger, claim table, research question, and standalone section agree |
| A2 | Add claim-delta/nonredundancy matrix and deterministic `STANDALONE_PASS` versus `NOTE_OR_MERGE` rule | one row per P13-1–P13-7; no inherited theorem counted as new |
| A3 | Register action isomorphism, output equivalences, universal blindness, and isotropy restriction quotient | definitions are usable verbatim by P13-6/P13-7 proofs and controls |
| A4 | Freeze actual-fibre product/star and intrinsic/transported regular/norm formulas | all signs, `x.u` ownership, Haar measure, `M_alpha`, `U_alpha`, and ratio character explicit |
| A5 | Freeze exhaustive Route owner registry and fixed eventual YAML count | every result/control record mapped to one owner ID; provenance tuple explicit |
| A6 | Define `C^1`, `Z^2`, `B^2`, quotient topology status, and gauge orientation | candidate lock and protocol use identical notation |
| A7 | Add conjecture-failure decision tree | candidate and pipeline statuses fail closed for every sharp falsifier |
| A8 | Add control-design pipeline stage and dense-stabilizer finite/proof boundary | future schema freeze cannot be bypassed; no finite density claim |

After amendment, recompute all three active hashes, update the active tuple
without embedding `pipeline_state.md`'s own hash, and commission fresh
independent Phase-1 reviews. Do not carry a zero-open-finding statement from
this superseded tuple.

## 8. Final disposition

| Severity | Count |
|---|---:|
| Critical | **0** |
| Major | **5** |
| Minor | **3** |

**Final Phase-1 verdict: MAJOR REVISION — C0/M5/m3.**

The candidate question remains viable, and no sign-level contradiction was
found in the normalized multiplier, coboundary, quadratic gauge, twisted
product, involution, or `U_alpha` direction. Phase 2 nevertheless remains
blocked because owner credit, standalone nonredundancy, retention invariants,
regular/norm methods, and Route owner enumeration are central design gates,
not post-proof copy edits. Amend the three locks, issue a new exact tuple, and
repeat the independent Phase-1 gate before source discovery or proof work.

## 9. Amended-v1 exact-byte re-lock addendum

Addendum date: **2026-08-15 (Asia/Shanghai)**  
Pre-addendum review SHA-256:
`7a434952771115085b9d8c32c47849d969da23be19ac791a13d64af175977a54`  
Re-review mode: **fixed-yardstick verification of W1–W8 plus amended-v1
regression review**  
Amended-v1 verdict: **PASS — C0/M0/m0**  
Confidence: **5/5 for internal methodology, type, owner, nonredundancy-gate,
control-gate, and Route-provenance consistency**

This addendum supersedes the initial C0/M5/m3 disposition only for the exact
amended tuple below. The original report remains the frozen yardstick and
historical receipt for the superseded initial bytes.

### 9.1 Exact amended tuple and scope

| Artifact | Independently recomputed SHA-256 |
|---|---|
| `notes/research_protocol.md` | `519563a28c3f11e3b3853f6875a84191444a68cd2c032c4cfcf69ca4152d5064` |
| `notes/candidate_lock.md` | `8cc0d08971762aa784afe1c844215353f170a75a3c0ab892415458ab010d0266` |
| `notes/pipeline_state.md` | `d98bf49d2eb5c1905ea3625251d787b247f3cf19577ff40f8bc0136186280fd5` |
| `notes/phase1_amendment_v1.md` | `ea5242ba6a8a1f2f867e8b258abc802fdeaace54db76629f0a9f0629e3e90d27` |

The active protocol and candidate lock explicitly give the amendment
precedence over conflicting initial claim/status rows while retaining every
unmodified owner firewall, inherited byte lock, prohibition, and release
condition. `pipeline_state.md` binds the amendment digest externally and
correctly omits its own digest.

The re-lock read only this review and the four amended artifacts above. It
did not read sibling Paper-13 reviews, upstream Paper-9/11/12 artifacts,
proofs, code, controls, Route files, a manuscript, or release material. It
used no browsing and ran no proof, program, control, Route, Git, or public-
sync action. The only write is this appended addendum.

### 9.2 Fixed-yardstick closure matrix

| Original finding | Required evidence pattern | Amended-v1 evidence | Verification verdict |
|---|---|---|---|
| W1 — P13-1 owner | Paper 12 owns all-degree `T0` factorization; P13-1 is inherited; freshness is claim-level | Amendment §§2, 3.2, 8, 10, and 11 identify `thm:factorization`, mark P13-1 `INHERITED PAPER-12 COROLLARY`, give it zero novelty weight, and reserve Paper-13 ownership for the typed twist/support package | **FULLY ADDRESSED** |
| W2 — standalone discriminator | Claim-delta matrix; deterministic `STANDALONE_PASS`/`NOTE_OR_MERGE` rule; independent post-proof judgment | Amendment §11 contains one row for P13-1–P13-11, defaults `STANDALONE_PASS` to false, assigns no novelty to inherited/source/control/Route rows, and makes P13-8 the sole candidate subject to an independent dependency-break paragraph | **FULLY ADDRESSED** |
| W3 — retention invariant | Action category, named outputs, exact equivalences, universal blindness, typed isotropy restriction | Amendment §§3.1 and 6 define `Act_indisc(R)`, four named records, gauge-induced/isometric equivalences, universal action blindness, and `Res_x` in `H^2_tw(H_x;T)` with subspace topology and all continuous normalized restricted gauges | **FULLY ADDRESSED** |
| W4 — product/representation/norm direction | Actual fibre formulas, Haar/modular convention, intrinsic regular representation, gauge intertwiner, exact norms, choice ratio | Amendment §5 freezes `x.u`, `sigma(x;u,t-u)`, both star forms, Lebesgue Haar measure, `Delta_R=1`, `lambda_sigma`, `Lambda_sigma`, `M_alpha`, `U_alpha`, both transported norms, `chi=beta/alpha`, and `C_chi` in the correct directions | **FULLY ADDRESSED** |
| W5 — Route registry | Exhaustive owner inventory, fixed YAML count, owner-local eligibility/A0 ceiling/role, explicit upstream tuple | Amendment §13 registers exactly ten owner IDs with construction, eligible claims, A0 ceiling, and `RESULT_OWNER`/`CONTROL_ONLY`; freezes ten YAMLs, versioned pre-Route amendment for count drift, explicit upstream gates, acyclic order, no self-hash, and Route B false | **FULLY ADDRESSED** |
| W6 — quotient registration | `C^1`, `Z^2`, `B^2`, abstract quotient, no topology, oriented gauge map | Amendment §4 defines all four groups, requires direct verification that `delta a` is normalized/cocyclic, freezes `sigma overline(tau)=delta a`, and types `U_a:A_sigma->A_tau` and `U_alpha:A_sigma->A_1` | **FULLY ADDRESSED** |
| W7 — failure branch | Fail closed for nontrivial class, open proof, exact precedent, and downstream claims | Amendment §8 gives a trigger/disposition table: counterexample freeze and Phase-1 return, trivializable-only P13-5, no mismatched-theorem substitution, exact-precedent merge, and P13-8 merge fallback; candidate and pipeline bind that active amendment | **FULLY ADDRESSED** |
| W8 — control-design gate | Separate design and implementation stages; exact per-CSV freeze; dense-stabilizer proof/finite boundary | Amendment §12 freezes the required future design fields, expands the inventory to eleven CSVs for P13-8, labels dense stabilizer proof-owned and surrogates `FINITE_DIAGNOSTIC_ONLY`; pipeline rows separately block design and implementation | **FULLY ADDRESSED** |

No W1–W8 criterion was weakened, silently replaced, or satisfied by an
authorial assertion alone. Each closure is present in the amended active
bytes. No regression against a previously passing sign, domain, owner, proxy,
completion, source-credit, control-as-proof, Route-B, or release firewall was
found.

### 9.3 New P13-8 support-transfer audit

The new center is methodologically and mathematically well typed at the
protocol stage.

1. **Owner and direction.** The common-lattice hypothesis is explicit:
   every stabilizer is `H=L Z`, `L>0`; `Q=X/R` is a nonempty bare set; and
   `Std(X)` is the coproduct of standard compact Hausdorff `R/H` torsors.
   The identity functor points continuously
   `J:G_std(X)->G_actual(X)`, so function pullback correctly goes from the
   actual record to the standard record. No reverse continuity is used.
2. **Actual support.** For `f in C_c(R)`, the inherited author record is
   `Phi_actual(f)(x,t)=f(t)` with support
   `X x supp_R(f)`. The protocol credits only Paper 11 for the actual
   global-QC time isomorphism and quasi-compact projection criterion.
3. **Standard support.** The pullback is the same pointwise function and has
   support `Std(X) x supp_R(f)`. It is continuous on the Hausdorff standard
   arrow space. `C_c(G_std(X))` is expressly only the ordinary compact-
   support function space; no groupoid completion is inferred.
4. **Exact iff.** If `f=0`, the support is empty. If `f` is nonzero,
   `supp_R(f)` is nonempty compact. A finite `Q` makes `Std(X)` a finite
   coproduct of compact orbits and hence compact. For infinite `Q`, the
   orbit summands form an open cover with no finite subcover; equivalently,
   compactness of the product support would force compactness of its
   projection onto `Std(X)`. Thus the stated criterion
   `J^*Phi_actual(f) in C_c(G_std(X)) iff f=0 or Q is finite` has the right
   hypotheses and conclusion.
5. **Gauge invariance.** Every allowed gauge is circle-valued and nowhere
   zero, so multiplication preserves the nonzero set and its closure exactly.
   The support criterion therefore survives every proved trivialization
   without becoming a cohomology or completion claim.
6. **Fixed-prime type ceiling.** Substitution uses only
   `H=(log p)Z` and the bare set `Q_p`. The conclusion is conditional:
   nonzero support transfer holds iff `Q_p` is finite. No finiteness,
   cardinality, enumeration, measure, or actual quotient topology is
   asserted.

The premise ledger in amendment §10 credits Paper 11 separately for the
actual support half and Paper 12 separately for standardization and `J`.
Paper 13 claims only the cross-owner support obstruction and its typed
application. This avoids converting inherited ingredients into novelty.

### 9.4 P13-8 nonredundancy and standalone boundary

PASS as a **Phase-1 discriminator**, not as a pre-awarded standalone result.
The claim-delta matrix accurately gives P13-1 no weight, P13-3 low/prior-
covered weight, P13-4/P13-5 only medium weight, and P13-6/P13-7 low negative
weight. It identifies P13-8 as the only central candidate because it compares
quasi-compact actual support with compact support after the one permitted
same-carrier topology change.

The lock does not infer `STANDALONE_PASS` from that description. The default
remains false. If the proof fails, the theorem reduces to a direct P11/P12
restatement, or an exact same-domain package precedent is found, the mandatory
disposition is `NOTE_OR_MERGE`. Only an independent post-proof reviewer may
find a non-substitution dependency break and must state it explicitly. This
is the operational criterion W2 required; no Phase-1 novelty verdict is being
smuggled into the proof plan.

### 9.5 Fail-closed branch verification

PASS. The five branches are exhaustive for the registered center:

- proved P13-3 permits P13-4–P13-8 to proceed;
- a nontrivial continuous class freezes the counterexample, falsifies the
  universal negative claims, restricts completion transport to the
  trivializable subclass, and returns the question to Phase 1;
- an open direct proof remains open and cannot be replaced by Borel,
  measurable, smooth, or differently normalized theory;
- an exact same-package precedent forces `NOTE_OR_MERGE`; and
- failure/routineness of P13-8 forces `NOTE_OR_MERGE` even if the gauge
  package closes.

The revised direct-proof route additionally corrects the lifted defect to
`2 pi Z`, keeps the real continuous cocycle step open, and includes the
two-dimensional multiplier as a dimension-sensitive excluded-domain
falsifier. None of these planning details asserts a proof.

### 9.6 Control-design and Route-provenance verification

PASS. The control pipeline now has two separate blocked stages: the P13-9
design lock follows the Phase-2 source/domain gate, and implementation follows
independent review of that design lock. The future lock must specify schema,
columns, row formulas, serialization/order, oracle, exact row counts, negative
labels, tolerance, manifest bindings, and aggregate receipts for all eleven
CSVs. The dense-stabilizer and infinite-set facts remain proof-owned; finite
surrogates cannot prove them.

The Route registry contains exactly ten records:

1. one-object time gauge;
2. generic actual cochain/gauge;
3. generic actual twisted global-QC;
4. generic full transport;
5. generic reduced transport;
6. fixed-prime actual cochain/gauge;
7. fixed-prime actual twisted global-QC;
8. generic actual/standard support transfer;
9. fixed-prime actual/standard support transfer; and
10. one explicitly `CONTROL_ONLY` nonselectivity package.

The control package has no transferable A0 credit and cannot donate a
positive coordinate to a result owner. Every eventual YAML must evaluate all
five coordinates locally; any owner/count change requires a reviewed
pre-Route amendment. The final provenance tuple explicitly precedes the ten
YAMLs, Route audit, and composition, and no artifact may embed its own hash.

### 9.7 Coverage receipt for the zero-finding re-lock

**Covers:** amended-v1 Weaknesses

| Dimension examined | What was checked | Basis for no residual/new finding |
|---|---|---|
| Research-question alignment | inherited factorization versus twist/support center; conditional branches | The new question separates the inherited premise, gauge package, support obstruction, and failure dispositions. |
| Cochain/gauge definitions | normalization, cocycle, `delta`, quotient, orientation, quadratic control | All signs and types agree; the quotient is abstract and the oriented gauge map is fixed. |
| Product/star methods | actual fibre and time formulas, support, star coefficient, gauge-star direction | `x.u`, `sigma(u,t-u)`, inverse arrow, Haar measure, and proof obligations are explicit. |
| Representation/completions | projective regular action, integrated form, intertwiner, norms, choice independence, amenability | Intrinsic and transported records are distinct and connected by the correct unitary direction. |
| Retention theorem | action category, named outputs, equivalences, isotropy restriction, dense subgroup | The claims quantify only over registered records and use universal/gauge-invariant predicates. |
| P13-8 theorem | hypotheses, `J` direction, support identities, compactness iff, gauges, packet specialization | The theorem is exact, elementary proof obligations are complete, and no orbit-count fact is imported. |
| Nonredundancy | P11/P12/source ownership, claim weights, substitution test, post-proof authority | Standalone defaults false and has a deterministic independent escape condition; inherited results receive no novelty credit. |
| Controls | separate design/implementation gates, eleven-file inventory, exact freeze fields, finite/proof boundary | No implementation is authorized and no finite diagnostic may prove density or an infinite-set theorem. |
| Route | ten-owner count, construction/claims/A0/role, control ceiling, provenance order, Route B | Registry and future count are frozen; no owner-local evidence can be donated across rows. |
| Pipeline and release | active tuple, amendment precedence, downstream blocks, no Git/public sync | Only bounded Phase-2 source/framework work can follow three independent zero-finding receipts; every later stage remains blocked. |

### 9.8 Final amended-v1 disposition

| Severity | Open count |
|---|---:|
| Critical | **0** |
| Major | **0** |
| Minor | **0** |

**Final amended-v1 methodology/nonredundancy verdict: PASS — C0/M0/m0.**

This receipt closes this reviewer's W1–W8 on the exact tuple in §9.1 and
finds no regression or new Phase-1 methodology defect. It authorizes nothing
by itself: the pipeline may open bounded Phase-2 source/framework/precedent
work only after the other two independent reviewers also issue zero-finding
receipts and the exact-byte final gate binds the common tuple. Proof,
controls implementation, Route, manuscript, release, Git, and public sync
remain blocked.

Any byte change to the four amended artifacts requires another tuple-specific
re-lock.
