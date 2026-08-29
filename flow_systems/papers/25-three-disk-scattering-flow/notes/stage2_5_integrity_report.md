# Paper 25 Stage-2.5 Integrity Report

Audit timestamp: **2026-08-29T06:48:53Z**
Mode: **pre-review / ARS Stage 2.5 Mode 1**
Decision: **PASS AT STAGE 2.5 CHECKPOINT — AWAIT EXPLICIT STAGE 3 AUTHORIZATION**

## Outcome

The complete registered integrity surfaces pass their stated denominators. The workflow nevertheless stops at the mandatory checkpoint; Stage 3 is not authorized automatically.

| Artifact | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `283695c485a2a48abfab1ef0fe3d479f597f68f3082e20f4a5a1894ca37baefb` |
| `paper/references.bib` | `de776cc0bf16e6c837917f4a289f8c07b8b4f7e9146183b9a9e0e6294db99e6b` |
| `paper/paper.pdf` | `2bff30f417741922bb2b28e3208dd08993f0a83a9511421283143ace22177c9e` |
| claim registry | `57063b60063a873d909506e6fcf8c3bd938c4fed57de06cb58beee0daca76956` |
| coverage report | `0b68204e8a47ae36c68467dddd6fbde480f7de7063e5eabc213ff1dddc481a8d` |
| evidence rows | `26e7fd2a6f628e463c5fb8f224f17851d55bd65fb67d726aa4dcd0b72e27eb89` |
| semantic verdict receipt | `77e67e293b1208fb90aa066be336b623aa24fa53a27aa832f19f33437944e4fa` |

## Phase results

| Phase | Coverage | Result |
|---|---:|---|
| A — reference identity/metadata | 8/8 | 8 VERIFIED; 0 MISMATCH |
| B — citation contexts | 10/10 | all content contexts supported |
| C — registered numerical/data families | 7/7 | all internally consistent and replayed |
| C4/D7 — experiment intake | 1/1 declaration | scholar-owned intake plus non-empty provenance/alignment VERIFIED |
| D — originality heuristic | 22/70 (31.4%) | no actionable body overlap; one shared standardized-declaration MINOR recorded |
| E — registered claim verification | 48/72 selected | 48 VERIFIED; 0 MINOR_DISTORTION; 49/49 tuple carriers valid |
| E6 — claim-strength drift | first pass | correctly skipped: no revision evidence |

Phase D is heuristic public-Web screening, not Turnitin or iThenticate. It can miss paywalled, cross-language, or unindexed overlap. Professional screening remains recommended before submission.

The batch self-overlap audit checked all 10/10 local paper pairs, 22/22 ORCID-bound Zenodo PDFs, and two older official arXiv PDFs. It found zero substantive exact eight-word body reuse. P24--P25 contain a 98-word exact standardized declarations block; it is administrative boilerplate, not scientific-body reuse. This note is non-blocking and does not change the scientific originality result.

## Phase E receipt and limitation

The stable risk selection contains `45` HIGH-IMPACT claims checked at 100% and `3` RANDOM sentinels, for `48` distinct claims and `49` source tuples. Coverage replay reports zero bounded lexical gaps, while semantic extraction coverage remains `not_machine_detectable`.

All `49` evidence rows are explicitly `anchorless`. Their schema and tuple coverage are valid, but those rows alone do not prove semantic correctness or reproduce an external excerpt. The substantive verdict rests on the independent Phase A--C audit plus `notes/stage2_5_phase_e_semantic_audit.md`, now bound claim-by-claim by `notes/stage2_5_phase_e_semantic_verdicts.json`; this limitation is preserved rather than hidden.

## Active issues

| ID | Phase | Finding | Exact closure route |
|---|---|---|---|
| — | — | No active blocking integrity issue. | — |

## Seven failure modes

- Mode 1 implementation bugs: CLEAR within the `65` historical-test + `12` Round-8 replay scope.
- Mode 2 hallucinated citation: CLEAR.
- Mode 3 hallucinated result: CLEAR within the frozen source/result/hash and replay scope.
- Mode 4 shortcut reliance: CLEAR; frozen populations and negative controls are retained.
- Mode 5 bug reframed as insight: CLEAR; the manuscript preserves negative and bounded conclusions.
- Mode 6 methodology fabrication: CLEAR within disclosure and claim-to-provenance fidelity scope; design/run adequacy remains outside this check.
- Mode 7 early frame-lock: CLEAR; limitations and the next falsifiable Route-A obligation remain explicit.

## Roadmap crosswalk

- Route A: unit-roof symbolic control (A0_FAIL, A1_PASS_ANALYTIC, A2_ANALYTIC_DETERMINANT, A3_FAIL, A4_FAIL), rejected; no physical-flow tuple because nontransfer is proved.
- Route A file SHA-256: `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.
- Route B: **NOT INVOKED**; file SHA-256 `170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595`.
- Positive arithmetic candidate reaching A2: **no**.
- Gate credit from this integrity audit: **none**.

## Mandatory checkpoint

Stage 2.5 passes and stops at its mandatory checkpoint with `verification_status=VERIFIED`. Manuscript, bibliography, and PDF remain frozen. Stage 3 still requires an explicit authorization and must not start automatically.
