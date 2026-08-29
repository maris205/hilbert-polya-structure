# Paper 27 Stage-2.5 Integrity Report

Audit timestamp: **2026-08-29T02:40:46Z**  
Mode: **pre-review / ARS Stage 2.5 Mode 1**  
Decision: **FAIL-CLOSED — DO NOT ENTER STAGE 3**

## Outcome

The complete registered integrity surfaces were audited against the frozen manuscript, bibliography, PDF, sources, proof chain, and local result artifacts. Scientific/data surfaces are clean within the stated denominators; the checkpoint nevertheless fails because 1 named blocking issue(s) remain open. A FAIL is not a rejection of the paper's mathematics: it is the mandatory correction/intake boundary.

| Artifact | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `c2809011a722b81732952d889f194549adea58875b605dbafe58ada93de9b4b9` |
| `paper/references.bib` | `32307e53e52ca8c11f039c0b0609bc7c24f3c2fa4ecedd7d9e3eb9be4a158981` |
| `paper/paper.pdf` | `540403e2cfb3c893822f3bcb80fb56e33bff00970f340df3dc9e6e8d2810d65a` |
| claim registry | `05455f35794381fc5f472baaa56cdd2fedaf3d3cbdb99f58f344364c26893452` |
| coverage report | `407174b357de7e718d6d379de4807fc20ea694610091789f176444debdbbb07d` |
| evidence rows | `2f47adea1276a72469fddd8c1ee666796e2b73dcd388acc986c9088756be0496` |
| semantic verdict receipt | `913e75651609345e59a06c8567df57fab7b7bfaf3379d0c4394cb2a6aef4b23a` |

## Phase results

| Phase | Coverage | Result |
|---|---:|---|
| A — reference identity/metadata | 5/5 | 5 VERIFIED; 0 MISMATCH |
| B — citation contexts | 5/5 | all content contexts supported |
| C — registered numerical/data families | 13/13 | all internally consistent and replayed |
| C4/D7 — experiment intake | 0/1 declaration | **FAIL-CLOSED**; scholar declaration absent |
| D — originality heuristic | 21/67 (31.3%) | no actionable body overlap; one shared standardized-declaration MINOR recorded |
| E — registered claim verification | 70/77 selected | 70 semantically VERIFIED in the hash-bound receipt; 71/71 tuple carriers valid |
| E6 — claim-strength drift | first pass | correctly skipped: no revision evidence |

Phase D is heuristic public-Web screening, not Turnitin or iThenticate. It can miss paywalled, cross-language, or unindexed overlap. Professional screening remains recommended before submission.

The batch self-overlap audit checked all 10/10 local paper pairs, 22/22 ORCID-bound Zenodo PDFs, and two older official arXiv PDFs. It found zero substantive exact eight-word body reuse. P26--P27 contain a 100-word exact standardized declarations block; it is administrative boilerplate, not scientific-body reuse. This note is non-blocking and does not change the scientific originality result.

## Phase E receipt and limitation

The stable risk selection contains `67` HIGH-IMPACT claims checked at 100% and `3` RANDOM sentinels, for `70` distinct claims and `71` source tuples. Coverage replay reports zero bounded lexical gaps, while semantic extraction coverage remains `not_machine_detectable`.

All `71` evidence rows are explicitly `anchorless`. Their schema and tuple coverage are valid, but those rows alone do not prove semantic correctness or reproduce an external excerpt. The substantive verdict rests on the independent Phase A--C audit plus `notes/stage2_5_phase_e_semantic_audit.md`, now bound claim-by-claim by `notes/stage2_5_phase_e_semantic_verdicts.json`; this limitation is preserved rather than hidden.

## Active issues

| ID | Phase | Finding | Exact closure route |
|---|---|---|---|
| `P27-IL-SERIOUS-EXP-DECL-1` | C4/D7 | The manuscript reports project-owned computational results, but the post-#260 passport has no scholar-owned experiment_intake_declaration or experiment_provenance ledger. | Scholar confirms the exact batch experiment declaration; then transcribe and align the already frozen Round-2--8 provenance artifacts. |

## Seven failure modes

- Mode 1 implementation bugs: CLEAR within the `58` historical-test + `12` Round-8 replay scope.
- Mode 2 hallucinated citation: CLEAR.
- Mode 3 hallucinated result: CLEAR within the frozen source/result/hash and replay scope.
- Mode 4 shortcut reliance: CLEAR; frozen populations and negative controls are retained.
- Mode 5 bug reframed as insight: CLEAR; the manuscript preserves negative and bounded conclusions.
- Mode 6 methodology fabrication: **INSUFFICIENT EVIDENCE / BLOCKING** until the scholar-owned intake/provenance ledger exists.
- Mode 7 early frame-lock: CLEAR; limitations and the next falsifiable Route-A obligation remain explicit.

## Roadmap crosswalk

- Route A: residual model (A0_WEAK_ARITHMETIC_RELATION, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL), rejected; homology calibrator (A0_FAIL, A1_PASS_ANALYTIC, A2_FAIL, A3_FAIL, A4_FAIL), rejected.
- Route A file SHA-256: `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.
- Route B: **NOT INVOKED**; file SHA-256 `170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595`.
- Positive arithmetic candidate reaching A2: **no**.
- Gate credit from this integrity audit: **none**.

## Mandatory checkpoint

Stage 2.5 stops here with `verification_status=UNVERIFIED`. Manuscript, bibliography, and PDF remain frozen. The named bibliographic corrections require exact user authorization, and experiment intake requires the scholar's explicit declaration. Stage 3 must not start automatically.
