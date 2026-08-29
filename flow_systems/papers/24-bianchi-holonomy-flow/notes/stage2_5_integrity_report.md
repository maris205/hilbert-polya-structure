# Paper 24 Stage-2.5 Integrity Report

Audit timestamp: **2026-08-29T06:48:53Z**
Mode: **pre-review / ARS Stage 2.5 Mode 1**
Decision: **PASS AT STAGE 2.5 CHECKPOINT — AWAIT EXPLICIT STAGE 3 AUTHORIZATION**

## Outcome

The complete registered integrity surfaces pass their stated denominators. The workflow nevertheless stops at the mandatory checkpoint; Stage 3 is not authorized automatically.

| Artifact | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `e43ba0f77332b79df4d84346dcb6e3041c20f4bdded5a91f42caac348ea9fd11` |
| `paper/references.bib` | `11e7dd42f07ecf22744f5d9c829d13a22212e0d43cb2591c0e9dfd66bde86d87` |
| `paper/paper.pdf` | `e8dcfa74b967054a956521daa138a4cb397292c13674c19e1c03e218438759f1` |
| claim registry | `6a6fc0ebc3f76814638e49e378f2d64b086d06658cf54f1ccb877c0a8eedcdd4` |
| coverage report | `9e8c46db07e97ecadff4cda8e33f5c3ac754843ac2d7ab294594f59e58e20634` |
| evidence rows | `fe1a8634f6e0a09f0be623b23dd248257a1844a5ed54ce9ce86cfdd0ea7f9890` |
| semantic verdict receipt | `b51b55d807d357f66a6e61acc3f630e3349d1d04d9a12a3c8722e1a19f42f821` |

## Phase results

| Phase | Coverage | Result |
|---|---:|---|
| A — reference identity/metadata | 7/7 | 7 VERIFIED; 0 MISMATCH |
| B — citation contexts | 9/9 | all content contexts supported |
| C — registered numerical/data families | 6/6 | all internally consistent and replayed |
| C4/D7 — experiment intake | 1/1 declaration | scholar-owned intake plus non-empty provenance/alignment VERIFIED |
| D — originality heuristic | 21/69 (30.4%) | no actionable body overlap; one shared standardized-declaration MINOR recorded |
| E — registered claim verification | 64/76 selected | 64 VERIFIED; 0 MINOR_DISTORTION; 66/66 tuple carriers valid |
| E6 — claim-strength drift | first pass | correctly skipped: no revision evidence |

Phase D is heuristic public-Web screening, not Turnitin or iThenticate. It can miss paywalled, cross-language, or unindexed overlap. Professional screening remains recommended before submission.

The batch self-overlap audit checked all 10/10 local paper pairs, 22/22 ORCID-bound Zenodo PDFs, and two older official arXiv PDFs. It found zero substantive exact eight-word body reuse. P24--P25 contain a 98-word exact standardized declarations block; it is administrative boilerplate, not scientific-body reuse. This note is non-blocking and does not change the scientific originality result.

## Phase E receipt and limitation

The stable risk selection contains `61` HIGH-IMPACT claims checked at 100% and `3` RANDOM sentinels, for `64` distinct claims and `66` source tuples. Coverage replay reports zero bounded lexical gaps, while semantic extraction coverage remains `not_machine_detectable`.

All `66` evidence rows are explicitly `anchorless`. Their schema and tuple coverage are valid, but those rows alone do not prove semantic correctness or reproduce an external excerpt. The substantive verdict rests on the independent Phase A--C audit plus `notes/stage2_5_phase_e_semantic_audit.md`, now bound claim-by-claim by `notes/stage2_5_phase_e_semantic_verdicts.json`; this limitation is preserved rather than hidden.

## Active issues

| ID | Phase | Finding | Exact closure route |
|---|---|---|---|
| — | — | No active blocking integrity issue. | — |

## Seven failure modes

- Mode 1 implementation bugs: CLEAR within the `71` historical-test + `14` Round-8 replay scope.
- Mode 2 hallucinated citation: CLEAR.
- Mode 3 hallucinated result: CLEAR within the frozen source/result/hash and replay scope.
- Mode 4 shortcut reliance: CLEAR; frozen populations and negative controls are retained.
- Mode 5 bug reframed as insight: CLEAR; the manuscript preserves negative and bounded conclusions.
- Mode 6 methodology fabrication: CLEAR within disclosure and claim-to-provenance fidelity scope; design/run adequacy remains outside this check.
- Mode 7 early frame-lock: CLEAR; limitations and the next falsifiable Route-A obligation remain explicit.

## Roadmap crosswalk

- Route A: (A0_WEAK_ARITHMETIC_RELATION, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL); canonical A0 controls 2/3, exploratory/negative specificity result.
- Route A file SHA-256: `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.
- Route B: **NOT INVOKED**; file SHA-256 `170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595`.
- Positive arithmetic candidate reaching A2: **no**.
- Gate credit from this integrity audit: **none**.

## Mandatory checkpoint

Stage 2.5 passes and stops at its mandatory checkpoint with `verification_status=VERIFIED`. Manuscript, bibliography, and PDF remain frozen. Stage 3 still requires an explicit authorization and must not start automatically.
