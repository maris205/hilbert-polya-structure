# Paper 26 Stage-2.5 Integrity Report

Audit timestamp: **2026-08-29T06:48:53Z**
Mode: **pre-review / ARS Stage 2.5 Mode 1**
Decision: **PASS AT STAGE 2.5 CHECKPOINT — AWAIT EXPLICIT STAGE 3 AUTHORIZATION**

## Outcome

The complete registered integrity surfaces pass their stated denominators. The workflow nevertheless stops at the mandatory checkpoint; Stage 3 is not authorized automatically.

| Artifact | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `00a21246f496b12f98389522d762ad6c4e10683e0eb21163b881d7b035f9c2fe` |
| `paper/references.bib` | `9b061c02006f07f1c93df68d8577d44906122f55db71e6f529f43cf3f6483ed8` |
| `paper/paper.pdf` | `b2911495fff88a1e351c4b7cc65989f998df47822b3a2bae0db60b543c34d5aa` |
| claim registry | `1d27b238ae1fd5485192c7044f135e530d68aba6c997041fd441d7db4ded9cf2` |
| coverage report | `0d9b8e7d83e6c443e3eab02939511ce454d070377ccd8cdad5d3093a9aa47d20` |
| evidence rows | `7cdc6095fae6ef317059ce46104bfaeee4a7707f51fb4dcd78005e1bf8f0a842` |
| semantic verdict receipt | `df0dfe86e2387693e4e94acc830f7036d3d56814b1417bf18a04c1a890222884` |

## Phase results

| Phase | Coverage | Result |
|---|---:|---|
| A — reference identity/metadata | 5/5 | 5 VERIFIED; 0 MISMATCH |
| B — citation contexts | 5/5 | all content contexts supported |
| C — registered numerical/data families | 14/14 | all internally consistent and replayed |
| C4/D7 — experiment intake | 1/1 declaration | scholar-owned intake plus non-empty provenance/alignment VERIFIED |
| D — originality heuristic | 21/65 (32.3%) | no actionable body overlap; one shared standardized-declaration MINOR recorded |
| E — registered claim verification | 68/72 selected | 68 VERIFIED; 0 MINOR_DISTORTION; 70/70 tuple carriers valid |
| E6 — claim-strength drift | first pass | correctly skipped: no revision evidence |

Phase D is heuristic public-Web screening, not Turnitin or iThenticate. It can miss paywalled, cross-language, or unindexed overlap. Professional screening remains recommended before submission.

The batch self-overlap audit checked all 10/10 local paper pairs, 22/22 ORCID-bound Zenodo PDFs, and two older official arXiv PDFs. It found zero substantive exact eight-word body reuse. P26--P27 contain a 100-word exact standardized declarations block; it is administrative boilerplate, not scientific-body reuse. This note is non-blocking and does not change the scientific originality result.

## Phase E receipt and limitation

The stable risk selection contains `65` HIGH-IMPACT claims checked at 100% and `3` RANDOM sentinels, for `68` distinct claims and `70` source tuples. Coverage replay reports zero bounded lexical gaps, while semantic extraction coverage remains `not_machine_detectable`.

All `70` evidence rows are explicitly `anchorless`. Their schema and tuple coverage are valid, but those rows alone do not prove semantic correctness or reproduce an external excerpt. The substantive verdict rests on the independent Phase A--C audit plus `notes/stage2_5_phase_e_semantic_audit.md`, now bound claim-by-claim by `notes/stage2_5_phase_e_semantic_verdicts.json`; this limitation is preserved rather than hidden.

## Active issues

| ID | Phase | Finding | Exact closure route |
|---|---|---|---|
| — | — | No active blocking integrity issue. | — |

## Seven failure modes

- Mode 1 implementation bugs: CLEAR within the `74` historical-test + `18` Round-8 replay scope.
- Mode 2 hallucinated citation: CLEAR.
- Mode 3 hallucinated result: CLEAR within the frozen source/result/hash and replay scope.
- Mode 4 shortcut reliance: CLEAR; frozen populations and negative controls are retained.
- Mode 5 bug reframed as insight: CLEAR; the manuscript preserves negative and bounded conclusions.
- Mode 6 methodology fabrication: CLEAR within disclosure and claim-to-provenance fidelity scope; design/run adequacy remains outside this check.
- Mode 7 early frame-lock: CLEAR; limitations and the next falsifiable Route-A obligation remain explicit.

## Roadmap crosswalk

- Route A: (A0_WEAK_ARITHMETIC_RELATION, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL); exhaustive finite Hecke-owner obstruction.
- Route A file SHA-256: `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.
- Route B: **NOT INVOKED**; file SHA-256 `170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595`.
- Positive arithmetic candidate reaching A2: **no**.
- Gate credit from this integrity audit: **none**.

## Mandatory checkpoint

Stage 2.5 passes and stops at its mandatory checkpoint with `verification_status=VERIFIED`. Manuscript, bibliography, and PDF remain frozen. Stage 3 still requires an explicit authorization and must not start automatically.
