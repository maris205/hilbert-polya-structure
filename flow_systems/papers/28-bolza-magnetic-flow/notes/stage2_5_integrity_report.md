# Paper 28 Stage-2.5 Integrity Report

Audit timestamp: **2026-08-29T06:48:53Z**
Mode: **pre-review / ARS Stage 2.5 Mode 1**
Decision: **PASS AT STAGE 2.5 CHECKPOINT — AWAIT EXPLICIT STAGE 3 AUTHORIZATION**

## Outcome

The complete registered integrity surfaces pass their stated denominators. The workflow nevertheless stops at the mandatory checkpoint; Stage 3 is not authorized automatically.

| Artifact | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `864d2f6ce0f76245d4d4237ba2981b3e82fc8e31f7991f1f331817f7c028aec7` |
| `paper/references.bib` | `95728b0a7120e5df341a364ff77f65f5c1d4628d55a6e584e2de7d747d8ca63e` |
| `paper/paper.pdf` | `f78ddd1f8676b24c4937ab94c4ad491b52892fd563c5a27facc77d523ff0c192` |
| claim registry | `031e04aae854667ba03e4b39d8df28fa61391264ab7f8c1fee55d6d6a3514f07` |
| coverage report | `312bd9883bd4a15993ce40702e696e125e1ba550b762204a9c9956b76fd2b35a` |
| evidence rows | `58ca03d5c726ec6a6fd018766c35e810e982067fe84fbe8d264dd0acc18879c4` |
| semantic verdict receipt | `68759361710eb221d325f8b1eee300054854e7c58ffd562edce94ae14529ab7e` |

## Phase results

| Phase | Coverage | Result |
|---|---:|---|
| A — reference identity/metadata | 6/6 | 6 VERIFIED; 0 MISMATCH |
| B — citation contexts | 9/9 | all content contexts supported |
| C — registered numerical/data families | 10/10 | all internally consistent and replayed |
| C4/D7 — experiment intake | 1/1 declaration | scholar-owned intake plus non-empty provenance/alignment VERIFIED |
| D — originality heuristic | 28/72 (38.9%) | no actionable body overlap; no paper-specific overlap issue |
| E — registered claim verification | 81/85 selected | 80 VERIFIED; 1 MINOR_DISTORTION; 84/84 tuple carriers valid |
| E6 — claim-strength drift | first pass | correctly skipped: no revision evidence |

Phase D is heuristic public-Web screening, not Turnitin or iThenticate. It can miss paywalled, cross-language, or unindexed overlap. Professional screening remains recommended before submission.

The batch self-overlap audit checked all 10/10 local paper pairs, 22/22 ORCID-bound Zenodo PDFs, and two older official arXiv PDFs. It found zero substantive exact eight-word body reuse. No paper-specific declaration-template overlap was assigned to this manuscript. This note is non-blocking and does not change the scientific originality result.

## Phase E receipt and limitation

The stable risk selection contains `78` HIGH-IMPACT claims checked at 100% and `3` RANDOM sentinels, for `81` distinct claims and `84` source tuples. Coverage replay reports zero bounded lexical gaps, while semantic extraction coverage remains `not_machine_detectable`.

All `84` evidence rows are explicitly `anchorless`. Their schema and tuple coverage are valid, but those rows alone do not prove semantic correctness or reproduce an external excerpt. The substantive verdict rests on the independent Phase A--C audit plus `notes/stage2_5_phase_e_semantic_audit.md`, now bound claim-by-claim by `notes/stage2_5_phase_e_semantic_verdicts.json`; this limitation is preserved rather than hidden.

## Active issues

| ID | Phase | Finding | Exact closure route |
|---|---|---|---|
| `P28-IL-MINOR-REPLAY-ORDER-1` | E | The manuscript says the verifier checks source/upstream digests before reconstruction, while the checked Round-8 builder runs finite_traversal() before build_validation() checks those locks. The verify-only wrapper remains temporary-directory safe and the result values are unaffected. | Correct the sequencing sentence during the next explicitly authorized manuscript-revision stage; retain this non-blocking audit finding until then. |

## Seven failure modes

- Mode 1 implementation bugs: CLEAR within the `104` historical-test + `24` Round-8 replay scope.
- Mode 2 hallucinated citation: CLEAR.
- Mode 3 hallucinated result: CLEAR within the frozen source/result/hash and replay scope.
- Mode 4 shortcut reliance: CLEAR; frozen populations and negative controls are retained.
- Mode 5 bug reframed as insight: CLEAR; the manuscript preserves negative and bounded conclusions.
- Mode 6 methodology fabrication: CLEAR within disclosure and claim-to-provenance fidelity scope; design/run adequacy remains outside this check.
- Mode 7 early frame-lock: CLEAR; limitations and the next falsifiable Route-A obligation remain explicit.

## Roadmap crosswalk

- Route A: control theorem only; full Route-A tuple unassigned because the Bolza target census and magnetic comparison have not been executed.
- Route A file SHA-256: `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.
- Route B: **NOT INVOKED**; file SHA-256 `170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595`.
- Positive arithmetic candidate reaching A2: **no**.
- Gate credit from this integrity audit: **none**.

## Mandatory checkpoint

Stage 2.5 passes and stops at its mandatory checkpoint with `verification_status=VERIFIED`. Manuscript, bibliography, and PDF remain frozen. Stage 3 still requires an explicit authorization and must not start automatically.
