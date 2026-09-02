# Paper 30 — Stage 1 Phase 3 Devil's Advocate Checkpoint 2

Date: **2026-09-02 UTC**  
Seat: **DA-SEAT-C**  
Reviewed synthesis seat: **SYNTH-SEAT-A**  
Final verdict: **`PASS`**  
Severity census: **0 CRITICAL / 0 MAJOR / 2 MINOR / 4 OBSERVATIONS**

## Independent-seat statement

`DA-SEAT-C` did not author the Paper-30 claim-intent manifest, literature
matrix, or synthesis and did not edit any of them. This review used their
frozen bytes and the controlling Phase-1/Phase-2 materials. This Devil's
Advocate report is the only file created by this seat. No external or
cross-model review was requested or run.

## Hash-bound review inputs

| Input | SHA-256 |
|---|---|
| `BATCH_ROUND10_STAGE1_PHASE3_SYNTHESIS_CONTRACT.md` | `2607c63b04c48584827825312f14f36fe852c358191d4abcb4cd882c54a75e1f` |
| `skills/route-a-evaluator.md` | `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c` |
| `skills/route-b-evaluator.md` | `170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595` |
| `stage1_phase1_rq_brief.md` | `87bf07d94ba92fc69f7c1f8bd73cdf6d8dcc2f5331d6478b3d11ba6c1aa68cf0` |
| `stage1_phase1_methodology_blueprint.md` | `167c890be3e7dd771542e4c48d8b15015368ba86f8595b838dd04f7a3b6a953a` |
| `stage1_phase2_annotated_bibliography.md` | `efa7a8b33fa37995f3345f46b232efd4515033d73e2a03f9e5919f59d2977e31` |
| `stage1_phase2_source_inventory.tsv` | `72c5383b65a23b32983f124c667bac1efdcbe71695e22d8d3d81fb7d5aa4140f` |
| `stage1_phase2_source_verification.md` | `e91bb28ee2f12748764b6b182e3d30837f892b4b8f7f58b309230413a16b07fe` |
| `stage1_phase2_source_verification.tsv` | `5442161a39d94fe62d57acb664c2536594500b79d9e6c29cae775d01567c7472` |
| `stage1_phase2_checkpoint.md` | `4a8bfd6ee234f752b607c62fa9582139e17f8a0be9dc9dd478c7e381aaaed3d0` |
| `pipeline_state.md` | `ffab3995f092c3e5f368011622949109a0f701a5eaaf9cff3048e816932eada8` |
| `stage1_phase3_claim_intent_manifest.json` | `cb88f85503a1beedc8cea54deffb0d16d94506346fe0f1ce9dad6ab874bcd71d` |
| `stage1_phase3_literature_matrix.tsv` | `74600edf4847299a838029127b637468e5bcc230af9b36e96957cd7e70b86c6b` |
| `stage1_phase3_synthesis.md` | `f4551764c8c3903e8437e0fcf1d5c16e24e1f327a729e019745c51c51ffa6f73` |

## Mechanical and provenance audit

| Check | Exact result | DA disposition |
|---|---|---|
| Inventory rows / unique IDs | `26 / 26` | PASS |
| Matrix rows / unique IDs | `26 / 26` | PASS |
| Matrix-to-inventory ID set | exact equality, `P30-S01`–`P30-S26` | PASS |
| Matrix evidence fields | all 26 `existence_outcome`, `claim_fitness_grade`, and `support_class` values equal the verification TSV | PASS |
| Matrix grade census | A=`8`, B=`16`, C=`2` | PASS |
| Matrix support census | direct=`9`, adjacent=`10`, background=`7` | PASS |
| Matrix years | 26/26 equal the inventory year | PASS |
| Claim-intent schema | valid `claim_intent_manifest/1.0`; 6 unique claims | PASS |
| Planned references | 21 unique IDs; all resolve to the frozen inventory | PASS |
| Experiment joins | no `planned_experiment_ids` field | PASS |
| Narrative ref/anchor pairs | 69/69 valid and paired; all 26 source IDs cited; no dangling ID | PASS |
| Themes | 6, within the required 3–7 | PASS |
| Required synthesis fields | consensus, debates, contradictions, gaps, methodology, implications, and concrete advance all present | PASS |
| Candidate tension inventory | 6 edges; all `scholar_confirmation: pending` | PASS |

## Critical issues — blocks progression

No critical issues identified.

The synthesis does not substitute a quantum or unit-roof determinant for the
physical-flow object, infer physical specificity from internal calibration,
or claim that a pointwise roof/operator/error contract has been built.

## Major issues — revision required

No major issues identified.

The core conclusion is appropriately fail-closed: the corpus supplies typed
components and transfer boundaries, but no compatible object-specific chain.
Every missing bridge retains a `NOT_EVALUABLE` or nontransfer-not-proved path.

## Minor issues — nonblocking

### P30-DA2-MINOR-1 — bridge count is internally ambiguous

- **Type:** Internal consistency / reporting precision.
- **Location:** Theme 6 closing paragraph and Concrete Phase-3 advance.
- **Problem:** Both locations say that **five** object-specific bridges must
  close. The gate graph separately lists P30-G1 through P30-G6, and the
  executable table separately lists substantive obligations P30-E01 through
  P30-E06 before the E07 authorization gate. The intended grouping may combine
  pointwise-roof construction with physical-fidelity validation, but that
  grouping is not stated.
- **Impact:** No gate is omitted from the actual graph or executable table, so
  the scientific boundary is intact. A reader could nevertheless miscount the
  prerequisites.
- **Recommendation:** In a bounded cleanup, say “six object-specific
  obligations” or define which two rows form one bridge.

### P30-DA2-MINOR-2 — roundoff lacks an explicitly identified source component

- **Type:** Evidence traceability / error-contract precision.
- **Location:** Theme 4, P30-G4, Research gap 4, and P30-E04.
- **Problem:** The matrix explicitly maps S19–S20 to eligible spectral/tail
  bounds, S21 to Galerkin/projection error, and S22 to numerical/quadrature
  evaluation. No matrix contribution explicitly claims a roundoff theorem or
  bound, yet Research gap 4 says orbit-tail, rank, quadrature, **and roundoff**
  all “have component literature.” S22's bounded verification surface is
  numerical and quadrature error for eligible trace-class operators; it does
  not expressly instantiate the frozen roundoff term.
- **Impact:** The synthesis still marks the four-part contract incomplete and
  authorizes no calculation, so no numerical conclusion is overstated. The
  issue is limited to the phrasing of available component support.
- **Recommendation:** State that roundoff is an additional unsourced or
  locator-unresolved obligation unless a frozen source row is explicitly
  licensed for it; retain `ERROR_CONTRACT_NOT_EVALUABLE` either way.

## Observations — warnings retained without a defect finding

1. **Author typography:** Phase-3 displays use `Cvitanovic` and `Livsic`
   instead of verified `Cvitanović` and `Livšic`. IDs and years remain exact,
   so this is manuscript-cleanup typography rather than metadata ambiguity.
2. **Owner details remain inherited:** the synthesis abbreviates the owner as
   an oriented cyclic no-repeat itinerary. The controlling blueprint still
   fixes cyclic-rotation identification, distinct time reversal, and no silent
   disk-label quotient; no Phase-3 operation changes those rules.
3. **Locator and integrity warnings remain genuine:** every citation uses
   `anchor:none`; COI is `UNKNOWN_NOT_AUDITED`; structured retraction status is
   `NOT_CHECKED`. None is laundered into theorem or integrity clearance.
4. **Chronology is preserved:** S22 remains a 2010 issue citation with 2009
   electronic publication, and S26 remains a 2026 issue citation with 2025
   online-first provenance.

## Correction-companion audit

| Binding | Required boundary | Synthesis result |
|---|---|---|
| P30-S01 | formula-level use requires DOI `10.1063/1.457669` | PASS: matrix and warning bind the exact DOI; no companion source row is invented |
| P30-S02 | affected use requires DOI `10.1063/1.457669` | PASS: distinct semiclassical type and exact correction are retained |
| P30-S03 | affected use requires DOI `10.1063/1.457670` | PASS: exact-quantum type and exact correction are retained |
| P30-S17/S18 | affected Section-7 maximal-entropy spectral-gap use requires both; first meromorphicity part reported unaffected | PASS: affected/unaffected split and S18's non-peer-reviewed erratum status remain explicit |

The correction notices are companions, not independent additional evidence
items. The 26-source census is therefore not inflated.

## Claim-intent and claim-drift review

| Manifest claim | Synthesis realization | Result |
|---|---|---|
| C-001: physical geometry and coding do not validate a project roof/operator | Theme 1, P30-G0–G1, gap 1 | ALIGNED |
| C-002: general operator results require an exact hypothesis map | Theme 2, P30-G2, gap 2, P30-E02 | ALIGNED |
| C-003: internal determinant calibration is roof-agnostic | Theme 3, consensus item 3, P30-T03 | ALIGNED |
| C-004: numerical components do not jointly provide the common map/four errors | Theme 4, P30-G3–G4, gaps 3–4, P30-E03–E04 | ALIGNED WITH MINOR ROUND-OFF WORDING NOTE |
| C-005: Livšic obstruction is directional and finite agreement is insufficient | Theme 5, P30-G6, P30-T05, P30-E06 | ALIGNED |
| C-006: Phase 3 emits an evaluability chain without execution or Route change | Theme 6, obligations, immutable ledger | ALIGNED |

No substantive emitted claim exceeds the manifest. The dependency graph and
obligation table are refinements of C-006, not a formal project Claim Registry.

## Object, clock, owner, and determinant-type firewalls

| Test | Adversarial question | Result |
|---|---|---|
| Geometry | Is another separation substituted for the primary object? | PASS: the primary remains no-eclipse equilateral `d=6a`; neighboring geometries remain typed controls only. |
| Speed and clock | Is symbolic length, unit roof, fitted scale, stability, or quantum action called physical time? | PASS: unit speed and physical Euclidean flight length remain immutable. |
| Primitive owner | Are time reversal, repetitions, or label permutations silently merged? | PASS: the inherited oriented cyclic owner and traversal convention remain controlling; no new quotient is performed. |
| Unit roof | Is unit-roof internal agreement used as physical evidence or imported credit? | PASS: it is an expected algebraic control result and carries no physical/A2 credit. |
| Shuffled roof | Are shuffled finite totals promoted to a pointwise operator roof? | PASS: label-only shuffling remains a ledger unit test and the typed pair becomes `NOT_EVALUABLE`. |
| Semiclassical object | Is P30-S02's spectral construction identified with the classical transfer determinant? | PASS: explicitly typed as a comparator only. |
| Exact-quantum object | Is P30-S03 or P30-S06 trace-class status transferred to the classical roof? | PASS: the substitution is explicitly prohibited. |
| General-flow theorem | Does shared Axiom-A/Anosov language establish exact open-billiard applicability? | PASS: geometry, coding, regularity, normalization, and function space must each match. |
| Coefficient cutoff | Does a shared label `N` identify orbit and rank objects? | PASS: a lawful extractor/projection map remains a separate prerequisite. |

## Four-error and common-map stress test

The synthesis correctly keeps two logically prior objects separate:

1. a coefficient/projection map that says which orbit/repetition coefficient
   is legally compared with which operator or projected-trace coefficient; and
2. the full-function approximation identity whose separate obligations are
   orbit tail, rank/projection, quadrature/evaluation, and roundoff.

A common cutoff symbol, a finite-rank determinant value, or a numerical
quadrature routine cannot supply the missing comparison map. Likewise, three
bounded error terms cannot absorb a missing fourth term. S19–S22 are kept
conditional on operator/function-space applicability. The only DA reservation
is MINOR-2: roundoff-specific literature support should not be implied unless
its bounded source surface is identified.

## Livšic asymmetry stress test

The direction of inference is correct. For roofs on one legally matched coding
and one prospectively fixed scale, a certified periodic-sum mismatch can refute
that proposed scale/coboundary relation after the applicable hypotheses are
bound. Finite equality cannot prove equality for every periodic orbit and
therefore cannot prove global cohomology. Matrix-cocycle and abelian extensions
do not become direct open-repeller theorems merely because they are stronger in
another setting.

The synthesis also avoids a second overclaim: one failed equivalence does not
prove all possible relations between roofs or establish physical specificity
without independent geometry-derived fidelity.

## Bias and logical-fallacy audit

| Risk | Stress result |
|---|---|
| Cherry-picking | Not detected. All 26 sources appear in the matrix and in valid narrative citations; correction companions and applicability failures are visible. |
| Confirmation bias | Not detected. Expected control calibration passes, failures, and not-evaluable paths are all reported without favoring physical success. |
| Appeal to authority | Not detected. General Anosov/open-billiard theorems and prestigious venues are not treated as object-specific applicability. |
| Hasty generalization | Not detected. Finite orbit data, finite-rank approximations, and one nontransfer witness remain bounded. |
| False equivalence | Specifically resisted across physical/unit, classical/quantum, orbit/rank, scalar/matrix-cocycle, and error-component types. |
| False dichotomy | Not detected. Pass, fail, not-proved, and not-evaluable outcomes remain distinct. |
| Moving goalposts | Not detected. Geometry, roof registry, coefficient map, errors, controls, and failure states must freeze before output inspection. |
| Equivocation | Not detected. “Calibration,” “physical fidelity,” “nontransfer,” and “Route credit” remain non-interchangeable endpoints. |
| Post hoc fitting / Texas sharpshooter | Not detected. No operator output, determinant value, cutoff tuning, or tolerance selection occurs. |
| Proves-too-much risk | Contained. Roof-agnostic calibration is explicitly denied physical specificity and arithmetic A2 meaning. |

## Strongest counterargument

> The corpus does not merely lack a few constants; it lacks the object map
> that would turn the physical collision geometry into a pointwise roof on an
> eligible operator space. Every theorem citation has `anchor:none`, and most
> operator/cohomology sources concern broader or differently regular systems.
> Therefore the six-theme chain may organize future work, but it supplies no
> present evidence that the physical determinant infrastructure is evaluable.
> Internal calibration by unit or shuffled roofs would be algebraically
> unsurprising, and a finite mismatch would refute only one predeclared
> scale/coboundary relation.

This is the strongest fair criticism, and the synthesis already accepts it.
It labels every chain link uninstantiated, makes `OPERATOR_NOT_EVALUABLE` and
`ERROR_CONTRACT_NOT_EVALUABLE` legitimate outcomes, and calls the advance a
dependency graph rather than a determinant or nontransfer result. The
counterargument limits significance but does not defeat the actual Phase-3
claim.

## What's missing

- exact formula/theorem locators for the physical collision section, coding,
  pointwise Euclidean-flight roof, and function space;
- an object-specific applicability proof for one operator/determinant class;
- one legal orbit/repetition-to-projected-trace coefficient map;
- all four error bounds on one complex domain, with a specifically sourced or
  derived roundoff contract;
- pointwise shuffled and exact neighboring-geometry roofs on compatible
  codings;
- a theorem-hypothesis map and certified witnesses for each cross-roof test;
- exact source anchors, structured retraction screening, and source-level COI
  audit; and
- separate scholar authorization for design freeze or any construction and
  computation.

These absences are reported as gaps or executable obligations, not silently
filled by analogy.

## Stress-test checklist

| Test | Result | Reason |
|---|---|---|
| Remove P30-S11, the closest open-billiard operator source | CONCLUSION HOLDS, EVALUABILITY WEAKENS | General-flow sources cannot replace its object proximity; the chain remains uninstantiated. |
| Remove P30-S23, the foundational scalar Livšic source | NONTRANSFER SUPPORT WEAKENS | Stronger matrix/abelian sources do not directly replace the scalar open-repeller bridge. |
| Let UNIT pass its internal determinant identity | EXPECTED, NO PHYSICAL CREDIT | Calibration is roof-agnostic. |
| Let a shuffled roof fail internally | IMPLEMENTATION WARNING, NO SPECIFICITY | A failed control algebra does not prove the physical roof. |
| Import an exact-quantum determinant | INVALID TYPE TRANSFER | Shared geometry does not identify operator or determinant type. |
| Give orbit cutoff and rank the same integer `N` | INVALID COMPARISON | Equality of labels is not a coefficient map. |
| Bound only three of four numerical errors | `ERROR_CONTRACT_NOT_EVALUABLE` | No missing error may be absorbed into another term. |
| Observe finite agreement of periodic ratios | NO GLOBAL EQUIVALENCE | Positive Livšic conclusions require all prescribed periodic data and matched hypotheses. |
| Certify one mismatched periodic ratio | ONE RELATION MAY BE OBSTRUCTED | It does not prove every model relation or replace physical fidelity. |
| Change time reversal or disk-label quotienting | INVALID OWNER MIXING | The inherited oriented owner convention is immutable. |
| Pass all future E01–E06 obligations | STILL NO ROUTE PROMOTION | A0 remains failed and A2 remains ineligible by design. |

## Final checkpoint decision

**`PASS`**

Zero critical and zero major findings remain. The bridge-count ambiguity and
roundoff-source phrasing are bounded minor issues; neither changes the
scientific conclusion, error fail-closed state, immutable physical object, or
Route boundary. Paper 30 may proceed to Phase-3 checkpoint bookkeeping with
the existing `PHASE3_SYNTHESIS_READY_WITH_WARNINGS` recommendation, provided
the two minor issues and all correction/locator/applicability warnings remain
visible. This verdict authorizes no roof construction, computation, claim
registration, formal Route evaluation, manuscript drafting, or later stage.
