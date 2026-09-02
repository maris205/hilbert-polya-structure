# Paper 29 — Stage 1 Phase 3 Devil's Advocate Checkpoint 2

Date: **2026-09-02 UTC**  
Seat: **DA-SEAT-C**  
Reviewed synthesis seat: **SYNTH-SEAT-A**  
Final verdict: **`PASS`**  
Severity census: **0 CRITICAL / 0 MAJOR / 2 MINOR / 4 OBSERVATIONS**

## Independent-seat statement

`DA-SEAT-C` did not produce the Paper-29 claim-intent manifest, literature
matrix, or synthesis and did not edit those artifacts during this review. The
review was performed from their frozen bytes and the Phase-1/Phase-2 inputs.
This file is the only artifact created by this seat. No cross-model review was
requested or run.

## Hash-bound review inputs

| Input | SHA-256 |
|---|---|
| `BATCH_ROUND10_STAGE1_PHASE3_SYNTHESIS_CONTRACT.md` | `2607c63b04c48584827825312f14f36fe852c358191d4abcb4cd882c54a75e1f` |
| `skills/route-a-evaluator.md` | `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c` |
| `skills/route-b-evaluator.md` | `170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595` |
| `stage1_phase1_rq_brief.md` | `47899a9f82875df3be569da62c4699b3a11d4f7a4f2423d9830f66ad9aa4218f` |
| `stage1_phase1_methodology_blueprint.md` | `99e88f3569a51cc40bb649919265fc46e15ec3080f67eaf76d1f3fdabf4e69d6` |
| `stage1_phase2_annotated_bibliography.md` | `c4d71637e5676337326d2eb78dcdd64d78b4b116a397c50c54a081d7c5e2650b` |
| `stage1_phase2_source_inventory.tsv` | `67ed7713bd6881d11466dc16755c7660a458c52e07ee072d086d6467f8ad7bd8` |
| `stage1_phase2_source_verification.md` | `81b50e0b6b834da414d8dc4bb60a47380255a26954d613393a7d817301a506e8` |
| `stage1_phase2_source_verification.tsv` | `bcf5fa7af07f353fbcaaa6fca319e79f173d7a6af070b58276a91fe9a44d8901` |
| `stage1_phase2_checkpoint.md` | `a9847cd300102f05927923dc3f7ac67d95987656413afc27ffc9bf172bb0e2dc` |
| `pipeline_state.md` | `869b1b0b7e6a47d567b2d0f51624685838b7bf678c438770ce19c1b55d40013d` |
| `stage1_phase3_claim_intent_manifest.json` | `dca6ddb1bd39bbc14c585cfe76b2c68643101436ebae088501691207011e09a7` |
| `stage1_phase3_literature_matrix.tsv` | `219309f0c8cea9106ba162c95f2de266b78b1c5d8e0d541e5b4a0e8122247d2c` |
| `stage1_phase3_synthesis.md` | `862dd41f318dd107e9d69a163c49266c34d48418a9632bfa13ceff81b952b5b0` |

## Mechanical and provenance audit

| Check | Exact result | DA disposition |
|---|---|---|
| Inventory rows / unique IDs | `22 / 22` | PASS |
| Matrix rows / unique IDs | `22 / 22` | PASS |
| Matrix-to-inventory ID set | exact equality, `P29-S01`–`P29-S22` | PASS |
| Matrix evidence fields | all 22 `existence_outcome`, `claim_fitness_grade`, and `support_class` values equal the verification TSV | PASS |
| Matrix grade census | A=`7`, B=`10`, C=`5` | PASS |
| Matrix support census | direct=`7`, adjacent=`7`, background=`8` | PASS |
| Matrix years | 22/22 agree with inventory years | PASS |
| Claim-intent schema | valid `claim_intent_manifest/1.0`; 5 unique claims | PASS |
| Planned references | 15 unique IDs; all resolve to the frozen inventory | PASS |
| Experiment joins | no `planned_experiment_ids` field | PASS |
| Narrative ref markers | 52/52 valid `P29-Sxx` markers paired with `anchor:none`; no dangling ID | PASS WITH WARNING |
| Narrative unique source IDs | 21; `P29-S17` is matrix-only | PASS WITH MINOR LABEL CLARIFICATION |
| Themes | 4, within the required 3–7 | PASS |
| Required synthesis fields | consensus, debates, contradictions, gaps, methodology, implications, and concrete advance all present | PASS |
| Candidate tension inventory | 5 edges; all `scholar_confirmation: pending` | PASS |

## Critical issues — blocks progression

No critical issues identified.

The synthesis does not invalidate its own method, fabricate an execution,
misidentify the frozen object, or convert a bounded search gap into a theorem
of nonexistence.

## Major issues — revision required

No major issues identified.

The two decisive interfaces remain explicitly open: a source-defined literal
Gaussian-prime-ideal owner law and a complete level-(3) primitive/unoriented
quotient. Neither is presented as completed, so the core conclusion remains
proportionate to the evidence.

## Minor issues — nonblocking

### P29-DA2-MINOR-1 — source-coverage ledger label is ambiguous

- **Type:** Traceability / reporting precision.
- **Location:** `stage1_phase3_synthesis.md`, Closed ledger,
  `SOURCE_IDS_COVERED=22/22`.
- **Problem:** The literature matrix covers all 22 sources, but the synthesis
  narrative contains citation markers for 21 unique IDs; `P29-S17` appears
  only in the matrix. The ledger is true if it means Phase-3 artifact or matrix
  coverage, but it can be read as 22/22 narrative citation coverage.
- **Impact:** No evidence is omitted from the required matrix and S17 is only
  background, so this does not change any theme, gap, or disposition. It is an
  audit-label ambiguity, not cherry-picking.
- **Recommendation:** In a bounded cleanup, distinguish
  `MATRIX_SOURCE_IDS_COVERED=22/22` from
  `NARRATIVE_SOURCE_IDS_CITED=21/22`, or add a bounded S17 background citation.

### P29-DA2-MINOR-2 — three author names lose verified diacritics

- **Type:** Metadata presentation.
- **Location:** Matrix and synthesis displays of `P29-S06`/`S07`, `P29-S08`,
  and `P29-S12`.
- **Problem:** The frozen inventory records `Avdispahić`, `Milićević`, and
  `Préaux`, while the Phase-3 display uses `Avdispahic`, `Milicevic`, and
  `Preaux`. Source IDs and years remain exact, and no authors are confused.
- **Impact:** No scientific or logical impact, but byte-level bibliographic
  fidelity is weaker than the verified inventory.
- **Recommendation:** Restore the verified diacritics before manuscript reuse;
  do not change source IDs or bibliographic dispositions.

## Observations — warnings retained without a defect finding

1. **Locator warning is real and visible.** All narrative source markers use
   `anchor:none`. The synthesis correctly treats this as a downstream theorem-
   locator warning and does not use metadata verification as theorem proof.
2. **Correction and discrepancy chain is preserved.** P29-S06 is bound to
   P29-S07; P29-S09 remains a repaired non-peer-reviewed preprint; the P29-S11
   `Some`/`Strong` title display conflict and P29-S13 287–305/287–306 page
   conflict remain visible without changing the stronger record values.
3. **Integrity unknowns are not laundered.** COI remains
   `UNKNOWN_NOT_AUDITED` and structured retraction status remains
   `NOT_CHECKED`; the S06/S07 correction is not misreported as retraction
   clearance.
4. **Non-peer-reviewed records stay bounded.** The preprint, research chapter,
   and monographs are used only for explicitly limited context or component
   interfaces; no peer-review weight is invented.

## Claim-intent and claim-drift review

| Manifest claim | Synthesis realization | Result |
|---|---|---|
| C-001: object and owner vocabulary do not define an ideal owner | Theme 1 and consensus item 1 | ALIGNED |
| C-002: algorithm components do not instantiate the level-(3) quotient | Theme 2, P29-G2, gap 3, P29-E03 | ALIGNED |
| C-003: ideal arithmetic and ideal powers do not select owners or prove group roots | Theme 3, consensus items 3–4, P29-T04 | ALIGNED |
| C-004: split-prime branch must respect the unoriented inversion quotient | Theme 3, P29-T01, gap 2, P29-E02 | ALIGNED |
| C-005: Phase 3 produces obligations, not execution or Route credit | Phase fence, advance, executable-obligation table, closed ledger | ALIGNED |

No intended claim is silently promoted. No material emitted claim falls
outside the five intended surfaces. The dependency graph is a refinement of
C-005, not a formal project Claim Registry.

## Theorem, object, clock, owner, and codomain compatibility

| Compatibility test | Adversarial question | Result |
|---|---|---|
| Frozen dynamical object | Is the full Picard group substituted for the inherited torsion-free level-(3) flow? | PASS: full-group literature is treated as context/components; exact level-(3) reduction stays open. |
| Clock | Does word length or an arithmetic label replace hyperbolic arclength? | PASS: arclength is preserved; no alternative clock is introduced. |
| Primitive owner | Are matrix rows, equal traces, or ideal powers called primitive loxodromic owners? | PASS: the matrix population remains pre-quotient and ideal-power detection is separated from group roots. |
| Repetition | Can a power mint a new owner? | PASS: powers remain repetitions of one primitive root. |
| Unoriented quotient | Is `[gamma]` silently separated from `[gamma^-1]` for performance convenience? | PASS: external inversion linking remains mandatory. |
| Literal codomain | Is a split pair weakened to a norm, rational prime, residue, composite ideal, or unordered pair? | PASS: every weakening is rejected as a change of question. |
| Group-algorithm transfer | Are compact-lattice, word-hyperbolic, `GL(n,Z)`, or adjacent-manifold results applied directly? | PASS: every transfer requires an explicit reduction and hypothesis map. |
| Finite codomain performance | Is a hypothetical positive `S_H` generalized to a global correspondence? | PASS: the synthesis explicitly forbids that inference. |

## Split-ideal/inversion obstruction stress test

The strongest formal vulnerability is correctly retained. Conjugate Gaussian
split prime ideals are distinct literal codomain values, while the primary
owner is an unoriented class modulo inversion. An admissible map must therefore
produce the same literal ideal from inverse representatives and cannot defer
branch selection to observed collision performance. The synthesis neither
asserts that inversion necessarily swaps the two ideals nor claims a universal
impossibility theorem; it asks for a source-defined, representative-independent
selection law and otherwise stops as `SPLIT_IDEAL_CODOMAIN_OBSTRUCTION` or
`FORMAL_MAP_REFUTED`. That is the correct fail-closed posture.

Alternative explanations remain alive: a lawful invariant branch rule may
exist in literature outside the bounded corpus, or a future exact locator pass
may expose one inside it. Those possibilities do not license invention or
post-hoc composition in the present run.

## Bias and logical-fallacy audit

| Risk | Stress result |
|---|---|
| Cherry-picking | Not detected. All 22 records remain in the matrix; the matrix-only S17 background row cannot reverse the owner-law or quotient gaps. |
| Confirmation bias | Bounded. The synthesis is falsification-first and preserves positive, obstruction, and not-evaluable branches rather than steering toward refinement. |
| Appeal to authority | Not detected. `VERIFIED` and high claim-fitness grades are not treated as theorem applicability or mechanism completion. |
| Hasty generalization | Not detected. No finite word-ball, future holdout pair, or ideal factorization is generalized to the full flow. |
| False dichotomy | Not detected. Multiple typed stop states and a possible lawful mechanism remain available. |
| Moving goalposts | Not detected. Literal codomain, gate order, primary estimand, and performance-independent registry remain frozen. |
| Equivocation | Specifically resisted. Ideal maximal power, group-element root, matrix row, conjugacy class, and inverse-paired owner remain separate types. |
| Texas-sharpshooter / outcome selection | Not detected. No row-level performance is opened and no candidate formula is selected. |
| Survivorship bias | Not applicable to an unexecuted mechanism comparison; failures and unresolved states are first-class outcomes. |
| Proves-too-much risk | Contained. No A2, determinant, zero, Hilbert–Pólya, or RH consequence is drawn from the component literature. |

## Strongest counterargument

> The apparent absence of an admissible ideal-owner mechanism may be an
> artifact of a bounded, web-accessible corpus and an unusually strict literal
> codomain. General arithmetic invariants, oriented refinements, or a
> construction outside the searched vocabulary could provide a lawful map;
> moreover, `anchor:none` citations do not verify the theorem hypotheses
> needed to decide that question. Therefore the dependency graph is only a
> research-design checklist, not evidence that the desired mechanism is
> impossible or even unlikely.

This counterargument is compelling but already conceded by the synthesis. The
text calls the result a closed-corpus compatibility finding, permits an
outside-corpus or later-locator mechanism, and refuses novelty or nonexistence
claims. It therefore limits the significance of Phase 3 without defeating its
actual conclusion.

## What's missing

- one exact source/formula locator and normalized bytes for any candidate
  direct owner mechanism;
- a proved split-branch selection law compatible with conjugacy, inversion,
  and repetition;
- an exact level-(3) applicability and theorem-hypothesis map for every group
  algorithm component;
- complete positive and negative conjugacy/root certificates, deterministic
  serialization, and a read-only verifier;
- three sensitivity-qualified, evaluator-accepted specificity-control types;
- theorem-level source locators, a structured retraction check, and a complete
  source-level COI audit; and
- separate scholar authority for registry freeze or any scientific execution.

These absences are accurately reported as obligations or warnings. They are
not Phase-3 defects and cannot be filled by this DA seat.

## Stress-test checklist

| Test | Result | Reason |
|---|---|---|
| Remove P29-S08, the strongest inversion-semantics source | CONCLUSION HOLDS, SUPPORT WEAKENS | The frozen owner convention still requires inversion; no remaining source would suddenly instantiate the map. |
| Remove P29-S19, the strongest ideal-arithmetic source | CONCLUSION HOLDS, IMPLEMENTATION CONTEXT WEAKENS | S20–S22 retain bounded ideal/certificate context; owner selection remains absent. |
| Flip the research question: could a valid mechanism exist? | YES, CREDIBLE | The synthesis explicitly preserves that possibility and makes no nonexistence claim. |
| Weaken literal ideal to norm or unordered pair | EASIER BUT INVALID | It removes the split-branch difficulty by changing the frozen codomain, not by solving the registered question. |
| Treat the full Picard group as the level-(3) quotient procedure | FAIL | The subgroup reduction, conjugacy relation, roots, and serialization remain unproved. |
| Substitute ideal-power detection for group primitivity | FAIL | The algorithms act on different mathematical objects. |
| Infer an A0/A1 or Route verdict from the dependency graph | FAIL | Literature compatibility is not Route credit and no formal tuple exists. |
| Apply the result to A2, determinants, zeros, or Route B | FAIL / STOP_SCOPED | No entry condition or compatible determinant/operator object exists. |
| “So what?” significance | BOUNDED YES | Two independent pre-performance kill gates are made explicit without pretending to solve them. |

## Final checkpoint decision

**`PASS`**

Zero critical and zero major findings remain. The two minor issues concern
coverage-label precision and author-name typography; neither changes source
fitness, claim strength, frozen mathematical types, or the fail-closed
disposition. The synthesis may proceed to Phase-3 checkpoint bookkeeping with
its existing `PHASE3_SYNTHESIS_READY_WITH_WARNINGS` recommendation, provided
the minor items and all locator/integrity warnings remain visible. This verdict
does not authorize the candidate registry, scientific execution, formal Route
evaluation, manuscript drafting, or any later stage.
