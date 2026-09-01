# P30 Checkpoint-1 Resolution — Revision 1

Date: **2026-09-01 UTC**  
Scope: **Phase-1 RQ Brief and Methodology Blueprint only**  
Status: **ARCHITECT RESPONSE COMPLETE; INDEPENDENT DA REPLAY REQUIRED**

The original Devil's Advocate report is unchanged. This resolution answers
every Critical, Major, and Minor item without performing Phase 2 or scientific
computation.

## Item-by-item resolution

| DA item | Severity | Resolution | Revised location |
|---|---|---|---|
| DA30-1 roof-agnostic primary test | **Critical** | **Resolved by reformulation.** Euler/trace/determinant agreement is now explicitly a roof-agnostic calibration identity; unit and admissible shuffled roofs are expected to pass internally. Physical distinction requires an independently constructed pointwise roof plus physical fidelity and cross-roof scale/coboundary nontransfer against unit, shuffled, and neighboring typed determinants. | RQ Brief, “Three non-interchangeable endpoints”; Methodology, “Algebraic calibration identity” and “Physical fidelity and cross-roof nontransfer” |
| DA30-2 unmatched cutoff semantics | Major | **Resolved fail-closed.** The primary common object is coefficientwise comparison through order `n<=N`. A finite-rank full determinant is separately typed; function/zero comparisons require explicit orbit-tail, rank, quadrature, and roundoff bounds. | Methodology, “Common coefficient comparison and cutoff mapping” |
| DA30-3 totals do not define pointwise roof | Major | **Resolved by an evaluability interface.** Added return section, coding, inverse branches, pointwise geometric roof, regularity, function-space, and independent input-path requirements. Ledger totals are validation only; absence emits `OPERATOR_NOT_EVALUABLE`. | Methodology, “Pointwise roof/operator evaluability gate” |
| DA30-4 deferred compatibility/error contract | Major | **Resolved procedurally and fail-closed.** Added a mandatory Phase-2-theory-derived, author-confirmed pre-validation freeze with exact fields for domain, projection, ranks, quadrature, precision, norms, four error bounds, roots, resources, and control directions. No empirical construction behavior may choose them; incomplete contract emits `ERROR_CONTRACT_NOT_EVALUABLE`. | Methodology, “Phase-2-derived pre-validation freeze rule” |
| DA30-5 unsupported sealed-test status | Major | **Resolved by downgrade.** `n=11,12` is now a prospective complexity holdout only. The files acknowledge that the ledger is readable and may have been inspected historically; no sealed/unread-byte claim remains. | RQ Brief scope; Methodology, “Orbit cutoff” |
| DA30-6 A0/A2 route semantics | Major | **Resolved by non-credit labeling.** The only positive result is `TYPED_PHYSICAL_DETERMINANT_INFRASTRUCTURE_PASS`, which contains no A2 credit. The full candidate is fixed at `A2_NOT_ELIGIBLE`, and overall Route A is fixed at `A0_FAIL / A2_NOT_ELIGIBLE / NO_ROUTE_PROMOTION`. | RQ Brief, “Typed dispositions” and route boundary; Methodology, required outputs and final boundary |
| DA30-7 unqualified independence | Minor | **Resolved in reporting.** The channels are “code-path-separated,” with shared inputs, conventions, assumptions, and correlated failures disclosed; separate code is not called independent evidence. | Methodology, analysis sequence and validity criteria |

## Control-direction resolution

| Typed control | Internal identity expectation | Physical/control comparison |
|---|---|---|
| Unit roof | PASS if implemented consistently | Physical nontransfer tested by exact period-two/period-three ratios |
| Pointwise shuffled roof | PASS if it defines an admissible operator roof | Nontransfer tested on predeclared changed owner associations; otherwise determinant `NOT_EVALUABLE` |
| Neighboring physical roofs | PASS if independently constructed consistently | Nontransfer from `d=6a` tested on the same two owner types under one scale |

No control is expected to fail merely because it is nonphysical for the primary
geometry.

## Preserved boundaries

- Frozen `d=6a` geometry, physical clock, oriented owner/repetition convention,
  and no-target firewall remain unchanged.
- No pointwise roof is invented from totals, no error tolerance is selected,
  and no determinant is computed in this revision.
- A0 remains absent/failed; A3/A4 and Route B remain closed.
- No source search, bibliography, synthesis, drafting, computation, claim
  registration, or Route evaluation was performed.

## Replay request

The revised artifacts do not self-award `PASS`. The independent Devil's
Advocate must replay Checkpoint 1, with DA30-1 treated as resolved only if the
new calibration/nontransfer separation is accepted.

## Revised artifact hashes

- `stage1_phase1_rq_brief.md`:
  `87bf07d94ba92fc69f7c1f8bd73cdf6d8dcc2f5331d6478b3d11ba6c1aa68cf0`
- `stage1_phase1_methodology_blueprint.md`:
  `167c890be3e7dd771542e4c48d8b15015368ba86f8595b838dd04f7a3b6a953a`
