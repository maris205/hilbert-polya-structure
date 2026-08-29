# Paper 25 Stage-2.5 Integrity Report

Audit timestamp: **2026-08-29T02:40:46Z**  
Mode: **pre-review / ARS Stage 2.5 Mode 1**  
Decision: **FAIL-CLOSED — DO NOT ENTER STAGE 3**

## Outcome

The complete registered integrity surfaces were audited against the frozen manuscript, bibliography, PDF, sources, proof chain, and local result artifacts. Scientific/data surfaces are clean within the stated denominators; the checkpoint nevertheless fails because 2 named blocking issue(s) remain open. A FAIL is not a rejection of the paper's mathematics: it is the mandatory correction/intake boundary.

| Artifact | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `283695c485a2a48abfab1ef0fe3d479f597f68f3082e20f4a5a1894ca37baefb` |
| `paper/references.bib` | `acec840393408f146f5e6eed9723cd4e12275108a6059fe0fdb0c2bc508e7248` |
| `paper/paper.pdf` | `608b669835f55c02bf5e43c570878728865e8659a58dbd23dae02dbf16dd101f` |
| claim registry | `57063b60063a873d909506e6fcf8c3bd938c4fed57de06cb58beee0daca76956` |
| coverage report | `0b68204e8a47ae36c68467dddd6fbde480f7de7063e5eabc213ff1dddc481a8d` |
| evidence rows | `26e7fd2a6f628e463c5fb8f224f17851d55bd65fb67d726aa4dcd0b72e27eb89` |
| semantic verdict receipt | `86fa4dd705f7661ad9e47cb02c1384dd2f8dc402c1bd3df1abd5ac9d49026abd` |

## Phase results

| Phase | Coverage | Result |
|---|---:|---|
| A — reference identity/metadata | 8/8 | 7 VERIFIED; 1 MISMATCH |
| B — citation contexts | 10/10 | all content contexts supported |
| C — registered numerical/data families | 7/7 | all internally consistent and replayed |
| C4/D7 — experiment intake | 0/1 declaration | **FAIL-CLOSED**; scholar declaration absent |
| D — originality heuristic | 22/70 (31.4%) | no actionable body overlap; one shared standardized-declaration MINOR recorded |
| E — registered claim verification | 48/72 selected | 48 semantically VERIFIED in the hash-bound receipt; 49/49 tuple carriers valid |
| E6 — claim-strength drift | first pass | correctly skipped: no revision evidence |

Phase D is heuristic public-Web screening, not Turnitin or iThenticate. It can miss paywalled, cross-language, or unindexed overlap. Professional screening remains recommended before submission.

The batch self-overlap audit checked all 10/10 local paper pairs, 22/22 ORCID-bound Zenodo PDFs, and two older official arXiv PDFs. It found zero substantive exact eight-word body reuse. P24--P25 contain a 98-word exact standardized declarations block; it is administrative boilerplate, not scientific-body reuse. This note is non-blocking and does not change the scientific originality result.

## Phase E receipt and limitation

The stable risk selection contains `45` HIGH-IMPACT claims checked at 100% and `3` RANDOM sentinels, for `48` distinct claims and `49` source tuples. Coverage replay reports zero bounded lexical gaps, while semantic extraction coverage remains `not_machine_detectable`.

All `49` evidence rows are explicitly `anchorless`. Their schema and tuple coverage are valid, but those rows alone do not prove semantic correctness or reproduce an external excerpt. The substantive verdict rests on the independent Phase A--C audit plus `notes/stage2_5_phase_e_semantic_audit.md`, now bound claim-by-claim by `notes/stage2_5_phase_e_semantic_verdicts.json`; this limitation is preserved rather than hidden.

## Active issues

| ID | Phase | Finding | Exact closure route |
|---|---|---|---|
| `P25-IL-SERIOUS-REF-1` | A | The official AMS record names O. E. Lanford III; the current author field omits the suffix III. | Authorize replacement of `author = {Bowen, Rufus and Lanford, Oscar E.}` with `author = {Bowen, Rufus and Lanford, III, Oscar E.}`; rebuild and re-audit Phase A/B. |
| `P25-IL-SERIOUS-EXP-DECL-1` | C4/D7 | The manuscript reports project-owned computational results, but the post-#260 passport has no scholar-owned experiment_intake_declaration or experiment_provenance ledger. | Scholar confirms the exact batch experiment declaration; then transcribe and align the already frozen Round-2--8 provenance artifacts. |

## Seven failure modes

- Mode 1 implementation bugs: CLEAR within the `65` historical-test + `12` Round-8 replay scope.
- Mode 2 hallucinated citation: SUSPECTED / BLOCKING because named author metadata mismatches remain.
- Mode 3 hallucinated result: CLEAR within the frozen source/result/hash and replay scope.
- Mode 4 shortcut reliance: CLEAR; frozen populations and negative controls are retained.
- Mode 5 bug reframed as insight: CLEAR; the manuscript preserves negative and bounded conclusions.
- Mode 6 methodology fabrication: **INSUFFICIENT EVIDENCE / BLOCKING** until the scholar-owned intake/provenance ledger exists.
- Mode 7 early frame-lock: CLEAR; limitations and the next falsifiable Route-A obligation remain explicit.

## Roadmap crosswalk

- Route A: unit-roof symbolic control (A0_FAIL, A1_PASS_ANALYTIC, A2_ANALYTIC_DETERMINANT, A3_FAIL, A4_FAIL), rejected; no physical-flow tuple because nontransfer is proved.
- Route A file SHA-256: `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.
- Route B: **NOT INVOKED**; file SHA-256 `170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595`.
- Positive arithmetic candidate reaching A2: **no**.
- Gate credit from this integrity audit: **none**.

## Mandatory checkpoint

Stage 2.5 stops here with `verification_status=UNVERIFIED`. Manuscript, bibliography, and PDF remain frozen. The named bibliographic corrections require exact user authorization, and experiment intake requires the scholar's explicit declaration. Stage 3 must not start automatically.
