# P26 Stage 3 — Editorial Synthesis and Decision

Date: **2026-08-29**  
Mode: **ARS `reviewer_full` under `reviewer/reviewer_full/v2`**  
Decision authority: **mechanical Schema 13.2 sprint-contract synthesis**  
Calibration status: **`NOT_CALIBRATED`**

## Scope, panel, criteria binding, and immutable route boundary

Five usable Phase-2 cards are present for the fixed roles `eic`,
`methodology`, `domain`, `perspective`, and `da`; panel cardinality is 5/5.
Each card explicitly carries the unbound state, and Phase 0 supplies no
author-confirmed venue, track, article type, ReviewTargetContext, or target
criteria authority:

criteria_binding_unavailable

This is a field-general scientific assessment. It makes **no venue-fit,
venue-alignment, or submission-readiness claim**. D6 is used only as the
Journal-Fit card's field-general contribution-positioning assessment; it does
not refer to any named or inferred venue.

The review, decision letter, ledger, and roadmap preserve the frozen object
and route boundary exactly:

- the formal Route-A tuple remains
  `(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)` with
  `ROUTE_A_EXPLORATORY`;
- the proved finite object remains the **138-instance/55-group
  correspondence-component multiset**, with the instance and group
  denominators kept distinct;
- that multiset is not promoted into a global primitive-conjugacy census,
  globally canonical primitive-owner ledger, or global primitive-orbit
  multiplicity rule;
- no A2 credit, global determinant, analytic continuation, prime-to-orbit
  correspondence, target-zero comparison, or natural operator lift is
  supplied or implied; and
- Route B remains unrun and unauthorized.

The manuscript and five reviewer cards are immutable, read-only inputs. This
document does not amend them and does not authorize revision execution.

## Machine audit receipt

```text
dimension_verdicts: [D1=warn, D2=warn, D3=block, D4=warn, D5=warn, D6=warn]
fired_conditions: [F2, F3, F5]
da_critical_adjudications: []
editorial_decision=major_revision
```

The DA CRITICAL table is empty. There are no `C<n>` IDs to adjudicate, no
rejection-rationale line to supply, and no DA-critical-versus-accept marker.
The DA's three MAJOR rows are not converted into a phantom CRITICAL; they are
carried in full as SC-08, SC-09, and SC-10 below.

## Role-scoped scoring matrix

Only assessed scores from contract-eligible roles enter the matrix.
Ineligible `not_assessed` rows are structural exclusions, not votes or
abstentions. The audit verdict is the worst assessed eligible score and is
distinct from each failure condition's cross-reviewer quantifier.

| Dimension | Priority | Eligible role(s) | Assessed eligible scores parsed from cards | Assessed n | Audit verdict |
|---|---|---|---|---:|---|
| D1 `methodology_rigor` | mandatory | methodology | methodology=`warn` | 1 | `warn` |
| D2 `domain_accuracy` | mandatory | domain | domain=`warn` | 1 | `warn` |
| D3 `argumentative_coherence` | mandatory | da, methodology | da=`block` (repairable); methodology=`pass` | 2 | `block` |
| D4 `cross_disciplinary_relevance` | high | perspective | perspective=`warn` | 1 | `warn` |
| D5 `writing_and_structure` | normal | eic | eic=`warn` | 1 | `warn` |
| D6 `venue_fit_and_contribution` | mandatory | eic | eic=`warn` | 1 | `warn` |

No dimension is unassessed. D3 contains one repairable block and no fatal
block. The methodology pass is preserved, but it neither averages away nor
softens the DA block.

### Five-card scoring profiles

These categorical profiles are parsed from the cards. Sprint cards do not
contain per-seat editorial recommendations, so none is inferred.

| Source card | Verbatim assessed profile | Strengths recorded | Weaknesses carried forward |
|---|---|---:|---:|
| Journal-Fit Reviewer (`EIC`) | D5=`warn`; D6=`warn` | 4 | 3 |
| Methodology / exact computation (`R1`) | D1=`warn`; D3=`pass` | 6 | 1 |
| Domain / theorem (`R2`) | D2=`warn` | 6 | 1 |
| Topology / transfer-operator perspective (`R3`) | D4=`warn` | 3 | 2 |
| Devil's Advocate (`DA`) | D3=`block`, `block_class=repairable` | narrative scope assessment | 0 CRITICAL; 3 MAJOR |

## Failure-condition receipt

The contract's cross-reviewer quantifier is applied within each selected
dimension first; the expression's dimension quantifier is applied second.
For a one-seat dimension, `majority` means that owner seat. For D3's two
assessed eligible seats, `majority` requires both seats.

| Condition | Severity | Mechanical evaluation | Fired |
|---|---:|---|---|
| F1 — any mandatory dimension has a fatal block (`any`) | 95 | D1, D2, D3, and D6 have no fatal block; DA's D3 block is explicitly repairable. | false |
| F2 — any mandatory dimension scores `block` (`any`) | 90 | D3 is mandatory, and DA is eligible for D3 and scores `block`. Methodology's D3 `pass` does not cancel an `any` result. | **true** |
| F3 — two or more mandatory dimensions score `warn` or worse (`majority`) | 70 | D1: true (1/1); D2: true (1/1); D3: false (DA is `block`, methodology is `pass`, so only 1/2 meets the threshold and both are required); D6: true (1/1). Three mandatory dimensions pass the per-dimension test, so the two-or-more test is met. | **true** |
| F4 — any high-priority dimension scores `block` (`any`) | 60 | D4 is the only high-priority dimension and scores `warn`, not `block`. | false |
| F5 — any dimension scores `warn` or worse (`any`) | 40 | Every dimension contains at least one assessed eligible `warn` or worse. | **true** |
| F0 — every dimension scores `pass` (`all`) | 10 | No dimension is uniformly `pass`; the universal condition fails. | false |

F2, F3, and F5 fire. F2 has the highest severity and supplies the binding
action, **Major Revision**. The action is not a vote average: DA's repairable
D3 block fires F2 even though methodology passes D3. Conversely, D3 does not
count toward F3 because that condition uses `majority` and both D3 seats would
have to score `warn` or worse. No qualitative recommendation matrix,
confidence label, venue inference, or post-hoc appraisal may alter this
mechanical result.

## Part 1 — Editorial decision letter

Dear Author,

Thank you for submitting *Exact Newform-Period Taxonomy for a Level-11 Time
Change of the Modular Geodesic Flow* for field-general scholarly review. The
manuscript was evaluated through five role-separated review seats under the
fixed Schema 13.2 sprint contract. I write to convey the resulting editorial
action: **Major Revision**.

The panel found a rigorous and unusually well-bounded finite mathematical
core. The manuscript correctly assigns the Hecke relation to cycle
pushforwards, distinguishes branch-cycle degree from primitive-root exponent
and zeta repetition, derives the all-parameter quadratic degree-moment
criterion, and gives an exact rational-homology taxonomy of the frozen
138-instance/55-group correspondence-component multiset. It keeps the two
full complex-period kernels distinct from the two real-projection-only
kernels, uses exact arithmetic rather than floating-point zero decisions, and
does not promote the finite certificate into a global primitive census,
determinant, operator, or Route-B claim.

Major Revision is nevertheless mechanically required. DA's repairable D3
block fires F2: the paper must align every primitive-Euler conclusion with
the actual correspondence-component owner domain and declared multiplicity,
show what part of the 51-of-55 pattern is scientifically discriminative after
the generic genus-one and inverse-pairing controls, and make the finite
primitive-root completeness argument auditable within the manuscript. F3
also fires because methodology rigor, domain accuracy, and field-general
contribution positioning each warn in their one-seat mandatory dimensions.
Accordingly, the revision must close the final source-dependency manifest,
strengthen the verified adjacent-literature comparison, and explain why the
finite negative result is informative at precisely its claimed scale.

The requested changes must preserve, rather than expand, the evidentiary
boundary. The finite object remains the 138-instance/55-group
correspondence-component multiset. A global primitive-owner interpretation
would require separately authorized canonicalization and a justified
multiplicity rule; absent that new evidence, the minimum remedy is explicit
multiset-scoped wording. Likewise, a matched control decomposition may refine
the contribution claim, but it cannot supply A2 credit, a global determinant,
or Route B. Expository revisions should add the requested index/count
crosswalk, first-use formal-product dictionary, and Schreier-to-taxonomy
schematic without changing the theorem's scope.

This is a revision action, not a rejection: the only block is repairable, no
fatal block exists, and the DA records no CRITICAL item. It is also not a
venue-fit or submission-readiness determination because no venue or criteria
binding exists. Please respond point by point to every SC ledger row after
the mandatory scholar checkpoint authorizes the exact response and revision
scope. A revised package will require a separate evidence-based re-review.

Sincerely,  
Editorial Synthesizer

## Decision basis: cross-card convergence and divergence

Silence is neither agreement nor opposition. Confidence values are
self-reported competence and scope disclosures only; they do not weight
findings, alter transported severity, change consensus counts, or resolve
disagreement.

### Convergence

1. **Exact finite theorem and route boundary.** All five cards accept the
   exactness of the finite counts and preserve the same bounded object: a
   138-instance/55-group correspondence-component multiset, not a global
   primitive census. Every card preserves
   `(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`,
   `ROUTE_A_EXPLORATORY`, no global determinant, and no Route B.
2. **Owner, degree, root, and repetition are distinct.** The non-DA cards
   praise the cycle-owned Hecke law and the three-index separation; DA also
   states that these concepts are formally separated. The dispute concerns
   how far the primitive-Euler interpretation may extend without cross-instance
   owner canonicalization, not the correctness of the formal distinction.
3. **Current-literature and significance positioning need repair.** EIC-W2
   and R2-W1 converge on a missing nearest-neighbor comparison. EIC transports
   Major severity for the broad contribution-positioning gap; R2 transports
   Minor severity for the specific modern geodesic-period omission. The shared
   operation is verified comparison, while each source severity remains
   unchanged.
4. **The finite interfaces can be easier to audit.** EIC-W3 and R3-W1/R3-W2
   ask for complementary reader maps: an index/denominator crosswalk, a
   first-use formal-product scope dictionary, and a Schreier-classification
   chain. None requests a determinant, operator, or global census.
5. **Certificate closure is localized.** R1-W1 and DA-M3 both concern audit
   closure, but at different layers: R1 identifies omitted transitive source
   dependencies in the final manifest; DA identifies an omitted
   manuscript-level completeness argument for the root search. Neither card
   alleges that the recorded 2/2/134 taxonomy or 51/55 counts are numerically
   wrong.

### Divergence and editorial adjudication

| Issue | Card positions | Editorial resolution |
|---|---|---|
| D3 eligible-seat score difference | Methodology passes D3 because the theorem-to-finite-certificate chain is coherent on the declared multiset. DA blocks D3 as repairable because primitive-Euler wording, discriminative significance, and the primitive-root premise are not yet fully supported at the manuscript surface. | Preserve both scores exactly. D3's audit verdict is `block`; F2 fires under `any`. D3's F3 majority predicate is false because only 1/2 eligible seats scores `warn` or worse. No averaging, softening, or substitute score is permitted. |
| Correspondence components versus primitive owners | EIC-S3, R1-S6, R2-S6, and R3-S3 credit the finite/global qualification; DA-M1 argues that some primitive-Euler conclusions still exceed the non-deduplicated owner domain and unproven canonical multiplicity rule. | Retain DA-M1 as a Major response obligation. The minimum remedy is to scope every tested primitive-Euler conclusion expressly to the correspondence-component multiset and declared finite multiplicity. Cross-instance conjugacy canonicalization is an optional stronger evidence path requiring explicit author authorization and later re-review; it is not silently required or treated as already done. |
| Scientific discrimination of 51/55 failures | The non-DA cards regard the exact finite obstruction as valuable and correctly bounded. DA-M2 argues that genus-one scalar action, inverse pairing, square positivity, and widespread nonunit-degree mass can force much of the failure pattern without identifying a newform-specific arithmetic residue. | Require a source-visible decomposition under matched exact controls, or narrow significance to the generic finite obstruction actually demonstrated. The revision may not infer arithmetic causation, A2 credit, a determinant, or a prime-owner mechanism from exactness alone. |
| Primitive-root support | R1-S2 and R2-S3 accept the exact finite certificates and the branch-degree/root distinction. DA-M3 agrees with the distinction but finds the exponent bound and exhaustive root-reconstruction lemma absent from the paper. | Distinguish certificate truth from manuscript self-containment. Retain the finite primitivity claim, but require a self-contained bounded-search lemma and auditable certificate fields. This resolves the support gap without changing the frozen output population or asserting a global primitive census. |
| Related-work severity | EIC-W2 transports Major; R2-W1 transports Minor. Both identify an incomplete adjacent-work comparison, but from different editorial and domain scopes. | Treat this as corroboration of the evidence gap, not a license to re-rate either source. Use one verified literature operation and respond to both SC rows separately. |
| Expository remedies | EIC-W3, R3-W1, and R3-W2 request different but compatible maps; no card argues against any of them. | Retain them as distinct source-specific obligations. They may be implemented coherently, but non-mention by the other seats is not consensus and the scholar must authorize exact blocks before any edit. |

No non-DA weakness sub-claim has an explicit disputing position from another
non-DA reviewer, so no formal `[SPLIT]` label is created among the four
non-DA seats. The material D3 disagreement includes the fixed DA seat and is
adjudicated separately above; its mechanical score consequences remain exact.

## Source-ordered, non-ranking revision-response ledger

The immutable source order is EIC → R1 → R2 → R3 → DA. `SC-01` through
`SC-10` are stable trace keys, **not priorities or a work order**. Every actual
weakness from every card appears once, including all three DA MAJOR rows. The
author must answer every row separately even where one roadmap operation
addresses corroborating concerns.

| Trace key | Source finding | Transported severity | Confidence | Actual weakness and typed evidence anchor | Required point-by-point response | Roadmap |
|---|---|---|---|---|---|---|
| SC-01 | EIC-W1 | Minor | 5/5 | The title does not expose the exact finite-output scope. `text: Title, manuscript.tex line 36, "Exact Newform-Period Taxonomy for a Level-11 Time Change of the Modular Geodesic Flow"` | Revise or justify the title so the finite Hecke-output/correspondence-component multiset is visible at first impression; do not call the multiset a primitive-orbit census or imply cross-instance deduplication. | REV-01 |
| SC-02 | EIC-W2 | Major | 4/5 | The closest-work comparison is insufficient for judging field-general significance. `absence: Related work and claim position, manuscript.tex lines 139–153 — expected comparison with close work on modular geodesic-flow time changes, Hecke or transfer-operator mechanisms, and computer-assisted orbit taxonomies; checked references.bib and all five cited contexts` | Add a verified compare-and-contrast map and explain the precise increment and value of the exact 2/2/134 taxonomy and 51/55 failures at the finite-multiset scale; narrow any significance or novelty statement not supported by the comparison. | REV-02 |
| SC-03 | EIC-W3 | Minor | 5/5 | The paper lacks a synoptic map of easily conflated indices and denominators. `absence: Three indices subsection and Complete finite taxonomy, manuscript.tex lines 204–210 and 405–407 — expected one synoptic crosswalk linking branch-cycle degree, primitive-root exponent, zeta repetition, instance count, and group count; checked all manuscript tables and displayed summaries` | Add one compact crosswalk for `d_O`, primitive-root exponent `q`, repetition `r`, 138 correspondence-component instances, and 55 source-word/prime groups, with permitted and prohibited inferences and an explicit no-global-census statement. | REV-03 |
| SC-04 | R1-W1 | Minor | 5/5 | The final certificate manifest is not closed over transitive source dependencies. `dataset: results/round8_artifact_manifest.json#/sources (dependency imports at code/round8_exact_taxonomy.py:152-154 and code/round7_exact_survivors.py:123-124)` | Regenerate the manifest and receipt with a dependency-closed project-source list, bind every transitive hash, and add a fail-closed dependency verification that leaves the checked-in output tree unchanged. | REV-04 |
| SC-05 | R2-W1 | Minor | 4/5 | The five-source frame omits a directly adjacent current geodesic-period literature strand. `absence: manuscript.tex Related work and references.bib — expected a verified nearest-neighbor comparison for modern closed-geodesic-period results and the claimed finite owner-obstruction contribution; checked the five cited entries, Related work, and supplied Stage-2/2.5 citation audits` | Verify and compare the identified 2025 geodesic-period work and relevant primary antecedents, distinguish nonvanishing/distribution results from the present cycle-pushforward and finite moment obstruction, and state the bounded search limits. | REV-02 |
| SC-06 | R3-W1 | Minor | 5/5 | “Finite formal log product” lacks a first-use operator-scope dictionary. `absence: manuscript.tex, opening of Section “Zeta variations and exact moment obligations” through Equations (ruelle) and (selberg) — expected a first-use statement naming the finite owner index set and explicitly separating the formal repetition series from a constructed transfer operator, trace formula, Fredholm determinant, convergent zeta function, or global divisor; checked the section preamble, both displayed log products, the paragraph immediately following them, and Section “Limitations and open obligations”` | Define the frozen finite owner multiset before the formulas and state locally that the repetition series is formal coefficient bookkeeping with no function space, operator, nuclearity, determinant identity, convergence, continuation, or global divisor result. | REV-05 |
| SC-07 | R3-W2 | Minor | 4/5 | The Schreier coordinates lack a compact bridge to the three-way taxonomy. `absence: manuscript.tex, Section “Exact Schreier homology classifier,” from the introduction of the frozen coordinate basis through subsection “Kernel semantics and exact-decision hierarchy” — expected a short schematic linking a closed owner to its Schreier class, compact quotient, real-involution projection, and final kernel label; checked the full classifier section, the kernel-semantics subsection, and the taxonomy theorem` | Add the reader-facing chain from owner to rational Schreier class, compact class, real coordinate `k`, and the three exact labels; state that it classifies the frozen correspondence-component multiset only. | REV-06 |
| SC-08 | DA-M1 | Major | 5/5 | The paper moves from non-deduplicated correspondence components to a primitive-Euler interpretation without a canonical primitive-owner set or justified multiplicity rule. `text: § Limitations and open obligations, paragraph 1, "It does not deduplicate $\G$-conjugate owners across different output instances"` | At minimum, restrict every primitive-Euler conclusion to the registered correspondence-component multiset and its declared multiplicity. If the author instead elects the stronger evidence path, separately authorize cross-instance oriented conjugacy canonicalization, publish unique-owner multiplicities, justify the product multiplicity rule, and recompute before re-review. | REV-07 |
| SC-09 | DA-M2 | Major | 5/5 | The 51-of-55 failure count is not yet decomposed into generic degree-support effects, matched control failures, and any newform-specific residue. `text: § Adversarial controls and Route-A interpretation, paragraph 2, "The mechanism is therefore generic within a large control class."` | Supply a matched exact control decomposition or narrow the contribution to the generic finite obstruction that the current controls establish; do not treat the failure count or exactness as causal evidence for newform-specific arithmetic, A2, or a prime-owner mechanism. | REV-08 |
| SC-10 | DA-M3 | Major | 4/5 | The manuscript omits the completeness proof for the finite primitive-root search. `absence: § Hecke cycle ownership and § Certificate and reproducibility method — expected a proof that the finite root search exhausts every possible subgroup exponent and integral root; checked primitive-root discussion, taxonomy proof, certificate description, and bibliography` | Add a self-contained lemma with the trace-growth exponent bound, central-sign treatment in `PSL_2`, exact integral-root reconstruction and uniqueness, subgroup-membership check, and the certificate fields that audit all 138 registered instances. | REV-09 |

## Non-ranking revision roadmap

The roadmap follows the first occurrence of each source finding. It groups only
SC-02 and SC-05 because both require one verified adjacent-work comparison;
their point-by-point responses and transported severities remain separate.
Every other source finding retains a distinct revision operation. Grouping does
not average, re-rate, rank, or authorize implementation.

| Roadmap ref | Source trace(s) and transported severity | Obligation class | Revision operation | Cost scope | Bounded consequence if unresolved |
|---|---|---|---|---|---|
| REV-01 | SC-01 Minor | `should_fix` | Qualify or justify the title so the finite correspondence-component multiset is unmistakable and matches the abstracts and theorem boundary. | `sentence`: title and matching abstract/keyword consistency check | `claim_scope_unsupported` / title: first-impression scope remains broader than the proved finite object. |
| REV-02 | SC-02 Major; SC-05 Minor | `must_fix` | Build a source-verified nearest-neighbor comparison covering modern geodesic periods and the genuinely closest time-change, Hecke/transfer, and exact-taxonomy work; allocate novelty and significance at the finite-multiset scale and state search limits. | `section`: Related work, Introduction, Conclusion, and references | `evidence_gap_remains` / contribution claim: field-general significance and bounded novelty remain unauditable. |
| REV-03 | SC-03 Minor | `should_fix` | Add one index-and-denominator crosswalk that identifies mathematical owner, role, permitted inference, and prohibited inference for `d_O`, `q`, `r`, 138 instances, and 55 groups. | `section`: Three indices and Complete finite taxonomy | `reader_traceability_reduced` / manuscript: readers can still conflate branch closure, traversal repetition, product repetition, and the two finite denominators. |
| REV-04 | SC-04 Minor | `should_fix` | Produce a dependency-closed Round-8 source manifest/receipt and a fail-closed check over every transitively imported project source. | `other` `source_dependency_manifest`: Round-8 certificate and reproduction package | `method_reproducibility_unresolved` / dataset: the final certificate alone remains incomplete over the bytes used to rebuild it. |
| REV-05 | SC-06 Minor | `should_fix` | Add a first-use finite-owner/formal-series dictionary immediately before the two displayed products, keeping all operator, determinant, convergence, continuation, and divisor objects explicitly unconstructed. | `section`: opening of Zeta variations and exact moment obligations | `interpretive_ambiguity_remains` / section: “finite” can still be misread as modifying the repetition series or supplying an analytic operator object. |
| REV-06 | SC-07 Minor | `should_fix` | Add the compact owner-to-Schreier-class-to-compact-class-to-`k`-to-taxonomy schematic and three-label legend, expressly bounded to the frozen multiset. | `section`: Exact Schreier homology classifier and taxonomy pointer | `reader_traceability_reduced` / manuscript: adjacent-field readers still lack a reusable path from an owner matrix to its exact label. |
| REV-07 | SC-08 Major | `must_fix` | Use multiset-scoped primitive-Euler wording throughout as the minimum remedy. Treat global owner canonicalization, unique multiplicities, and recomputation only as a separately authorized stronger evidence path; until completed and re-reviewed, they supply no global claim. | `section`: research question, Introduction, Three indices, taxonomy interpretation, Limitations, and Conclusion | `claim_scope_unsupported` / primitive-Euler claim: correspondence-component moments remain liable to be read as a canonical primitive-owner product. |
| REV-08 | SC-09 Major | `must_fix` | Decompose verdicts under matched exact controls into generic degree-support/control effects and any supported residue, or narrow significance to the generic finite obstruction; preserve the fixed Route-A boundary in either path. | `re_analysis`: control ledger plus Adversarial controls, Introduction, and Conclusion | `evidence_gap_remains` / significance claim: exact failure prevalence remains non-discriminative with respect to newform-specific arithmetic. |
| REV-09 | SC-10 Major | `must_fix` | Add a self-contained finite-root completeness lemma and expose the auditable exponent-bound, reconstruction, sign, subgroup, and certificate fields without asserting global enumeration. | `section`: Hecke cycle ownership and Certificate and reproducibility method | `acceptance_criterion_unmet` / primitive-root premise: branch degree remains insufficiently separated from hidden traversal repetition at the manuscript surface. |

Revision completion criteria, stated in source-derived rather than work-order
terms:

- **REV-01 acceptance criterion:** the title explicitly names or otherwise
  unmistakably delimits the finite Hecke-output/correspondence-component
  multiset and matches the abstract's no-global-census boundary.
- **REV-02 acceptance criterion:** every added source is metadata- and
  relevance-verified; the comparison identifies object, owner/operator level,
  result type, and precise difference, and it states the search boundary
  without an exhaustive novelty claim.
- **REV-03 acceptance criterion:** one compact surface distinguishes `d_O`,
  primitive-root `q`, product repetition `r`, the 138-instance taxonomy, and
  the 55-group verdict denominator, with explicit prohibited inferences.
- **REV-04 acceptance criterion:** one immutable final receipt hashes every
  transitively imported project source and fails closed on dependency drift
  while reproducing the current checked-in tree.
- **REV-05 acceptance criterion:** before the formal products, the finite
  owner index set and infinite formal repetition bookkeeping are distinct, and
  no operator, determinant, convergence, continuation, or divisor result is
  implied.
- **REV-06 acceptance criterion:** a reader can follow an owner matrix through
  rational Schreier class, compact quotient, real coordinate `k`, and exactly
  one of the three finite labels without mistaking the schematic for global
  conjugacy canonicalization.
- **REV-07 acceptance criterion:** every primitive-Euler statement is bounded
  to the registered correspondence-component multiset and declared
  multiplicity unless a separately authorized canonicalization/recomputation
  package has actually been completed and passed re-review.
- **REV-08 acceptance criterion:** the manuscript identifies which failures
  are forced by degree support, which occur for matched closed-form controls,
  and what residue, if any, is supported as newform-specific; otherwise all
  significance language is narrowed to the generic finite obstruction.
- **REV-09 acceptance criterion:** the manuscript gives an auditable complete
  finite-root search argument for all 138 registered instances, including the
  exponent bound, sign convention, exact root reconstruction, subgroup test,
  and certificate linkage.

No author triage, preferred display order, work order, permission to group
responses, claim-strength authorization, collateral authorization, or
manuscript/provenance write authority is inferred. The response letter must
cite every `SC-nn` row, record the author's explicit disposition, describe the
change or reason for declining, and point to exact revised locations and
completion evidence.

## Response-letter requirements

The author response must preserve the source order above and answer every SC
row separately, even where one revision operation is shared. For each row it
must provide: the explicit author disposition; the evidence or reasoning for
that disposition; the exact changed location if authorized; the resulting
claim boundary; and the completion evidence to be checked in re-review. No
journal deadline is supplied or inferred.

## Review panel provenance (#540/#740)

The supplied provenance artifact replay-validates. Its six observations are
rendered separately and are not reduced to a binary or numeric independence
claim.

Artifact: `review-panel-provenance/1.0`  
Artifact raw SHA-256:
`f8b571665ded06e443557e11851987bcc70fca9b0bee6760a86517ff6444bf7f`  
Panel ID: `p26-stage3-round1-2026-08-29`  
Contract ID: `reviewer/reviewer_full/v2`  
Contract SHA-256:
`e9712090d2469fea15a37b8e22d4e137afbcb2bf38d5789939c5df56738ef7af`  
Normalized manifest SHA-256:
`571445b4cf36edfd7a5ee0d2bf7a70c9094a98518786d6ed2398608e75cb670f`  
Execution topology SHA-256:
`a1f8e1998cabc29c3dff3c103f2a38a00a0fb2a020fba5816012bf1ab240cb4d`  
Fresh-context scope: `within_panel_attempt_only`

| Provenance axis | Recorded value | Meaning retained in this synthesis |
|---|---|---|
| `blind_to_peer_outputs` | `true` | No seat saw peer outputs before committing. |
| `fresh_context` | `true` | Contexts were distinct within this panel attempt only; this says nothing about retries, earlier rounds, or later-round history. |
| `human_distinct` | `false` | The five seats were model-executed, with no distinct accountable human reviewer identities. |
| `model_family_distinct` | `false` | Every seat used the `gpt-5` model family. |
| `provider_distinct` | `false` | Every seat used the `openai` provider. |
| `role_separated` | `true` | The five seats had distinct review roles. |

**Correlated-error disclosure:** All model-executed review seats used one
model family; role separation does not remove correlated-error risk.

Persona and role separation do not establish independent error processes. No
cross-family aggregate, same-model majority, binary independence claim, or
independence score is computed.

## Mandatory scholar checkpoint

**Revision execution is not authorized until the scholar completes this
checkpoint.** The scholar must explicitly:

1. confirm or amend the Phase-0 field-general panel framing, retaining
   `criteria_binding_unavailable` unless an author-confirmed
   ReviewTargetContext and resolved binding are separately supplied;
2. adjudicate **each of SC-01 through SC-10 separately** as `will_address`,
   `wont_address`, or `not_on_point`, with a reason and the selected minimum
   remedy or stronger evidence path;
3. confirm whether SC-02 and SC-05 may share one literature-comparison
   operation while retaining separate point-by-point responses and unchanged
   transported severities;
4. choose explicitly between the bounded minimum remedy and any stronger new
   evidence path for SC-08, and likewise choose whether SC-09 will be met by
   matched exact reanalysis or by narrower contribution language; no choice is
   inferred from this roadmap;
5. confirm that every authorized response will preserve
   `(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`,
   `ROUTE_A_EXPLORATORY`, the finite 138-instance/55-group
   correspondence-component multiset, no global primitive census, no A2 or
   global determinant claim, and no Route B; and
6. authorize the exact manuscript, code, manifest, receipt, or other blocks
   that may change and the completion evidence for every accepted `REV-nn`
   item.

Until that explicit record exists, the roadmap is a reviewer-owned,
non-ranking proposal rather than an author decision. After any authorized
revision, the next substantive gate is a separate evidence-based re-review of
every ledger row. This synthesis does not revise the manuscript, authorize
route advancement, or pre-judge a later re-review outcome.
