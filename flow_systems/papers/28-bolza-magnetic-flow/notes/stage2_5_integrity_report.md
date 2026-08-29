# Paper 28 Stage-2.5 Integrity Report

Audit timestamp: **2026-08-29T02:40:46Z**  
Mode: **pre-review / ARS Stage 2.5 Mode 1**  
Decision: **FAIL-CLOSED — DO NOT ENTER STAGE 3**

## Outcome

The complete registered integrity surfaces were audited against the frozen manuscript, bibliography, PDF, sources, proof chain, and local result artifacts. Scientific/data surfaces are clean within the stated denominators; the checkpoint nevertheless fails because 3 named blocking issue(s) remain open. A FAIL is not a rejection of the paper's mathematics: it is the mandatory correction/intake boundary.

| Artifact | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `864d2f6ce0f76245d4d4237ba2981b3e82fc8e31f7991f1f331817f7c028aec7` |
| `paper/references.bib` | `42474f492f261e97883f7b8e0577fc7a42ce58db7e084f456d92045b5788d284` |
| `paper/paper.pdf` | `6bbda36564994ac8dcc16c962655867f6c427b6aeb19d7071922c6e07678e688` |
| claim registry | `031e04aae854667ba03e4b39d8df28fa61391264ab7f8c1fee55d6d6a3514f07` |
| coverage report | `312bd9883bd4a15993ce40702e696e125e1ba550b762204a9c9956b76fd2b35a` |
| evidence rows | `31c68cf97a63af5709c7c48883b3df1765449bb47b3efe0cc8fff89872c4cc3f` |
| semantic verdict receipt | `62f0d7f1293dc888ebcbae8b538436dec1a5458dfaa62e6c7d4ef284b26e88d3` |

## Phase results

| Phase | Coverage | Result |
|---|---:|---|
| A — reference identity/metadata | 6/6 | 4 VERIFIED; 2 MISMATCH |
| B — citation contexts | 9/9 | all content contexts supported |
| C — registered numerical/data families | 10/10 | all internally consistent and replayed |
| C4/D7 — experiment intake | 0/1 declaration | **FAIL-CLOSED**; scholar declaration absent |
| D — originality heuristic | 28/72 (38.9%) | no actionable body overlap; no paper-specific overlap issue |
| E — registered claim verification | 81/85 selected | 81 semantically VERIFIED in the hash-bound receipt; 84/84 tuple carriers valid |
| E6 — claim-strength drift | first pass | correctly skipped: no revision evidence |

Phase D is heuristic public-Web screening, not Turnitin or iThenticate. It can miss paywalled, cross-language, or unindexed overlap. Professional screening remains recommended before submission.

The batch self-overlap audit checked all 10/10 local paper pairs, 22/22 ORCID-bound Zenodo PDFs, and two older official arXiv PDFs. It found zero substantive exact eight-word body reuse. No paper-specific declaration-template overlap was assigned to this manuscript. This note is non-blocking and does not change the scientific originality result.

## Phase E receipt and limitation

The stable risk selection contains `78` HIGH-IMPACT claims checked at 100% and `3` RANDOM sentinels, for `81` distinct claims and `84` source tuples. Coverage replay reports zero bounded lexical gaps, while semantic extraction coverage remains `not_machine_detectable`.

All `84` evidence rows are explicitly `anchorless`. Their schema and tuple coverage are valid, but those rows alone do not prove semantic correctness or reproduce an external excerpt. The substantive verdict rests on the independent Phase A--C audit plus `notes/stage2_5_phase_e_semantic_audit.md`, now bound claim-by-claim by `notes/stage2_5_phase_e_semantic_verdicts.json`; this limitation is preserved rather than hidden.

## Active issues

| ID | Phase | Finding | Exact closure route |
|---|---|---|---|
| `P28-IL-SERIOUS-REF-1` | A | The official record gives A. V. Nazarenko (submission name Andrey Nazarenko) and primary subject math-ph; the entry expands Aleksandr V. and records hep-th. | Authorize `author = {Nazarenko, A. V.}` and `primaryclass = {math-ph}`; rebuild and re-audit Phase A/B. |
| `P28-IL-SERIOUS-REF-2` | A | Official metadata gives Aline Aigon-Dupuy, Peter Buser, Michel Cibils, Alfred F. Künzle, and Frank Steiner; three given names in the entry are wrong. | Authorize `author = {Aigon-Dupuy, Aline and Buser, Peter and Cibils, Michel and K{\"u}nzle, Alfred F. and Steiner, Frank}`; rebuild and re-audit Phase A/B. |
| `P28-IL-SERIOUS-EXP-DECL-1` | C4/D7 | The manuscript reports project-owned computational results, but the post-#260 passport has no scholar-owned experiment_intake_declaration or experiment_provenance ledger. | Scholar confirms the exact batch experiment declaration; then transcribe and align the already frozen Round-2--8 provenance artifacts. |

## Seven failure modes

- Mode 1 implementation bugs: CLEAR within the `104` historical-test + `24` Round-8 replay scope.
- Mode 2 hallucinated citation: SUSPECTED / BLOCKING because named author metadata mismatches remain.
- Mode 3 hallucinated result: CLEAR within the frozen source/result/hash and replay scope.
- Mode 4 shortcut reliance: CLEAR; frozen populations and negative controls are retained.
- Mode 5 bug reframed as insight: CLEAR; the manuscript preserves negative and bounded conclusions.
- Mode 6 methodology fabrication: **INSUFFICIENT EVIDENCE / BLOCKING** until the scholar-owned intake/provenance ledger exists.
- Mode 7 early frame-lock: CLEAR; limitations and the next falsifiable Route-A obligation remain explicit.

## Roadmap crosswalk

- Route A: control theorem only; full Route-A tuple unassigned because the Bolza target census and magnetic comparison have not been executed.
- Route A file SHA-256: `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.
- Route B: **NOT INVOKED**; file SHA-256 `170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595`.
- Positive arithmetic candidate reaching A2: **no**.
- Gate credit from this integrity audit: **none**.

## Mandatory checkpoint

Stage 2.5 stops here with `verification_status=UNVERIFIED`. Manuscript, bibliography, and PDF remain frozen. The named bibliographic corrections require exact user authorization, and experiment intake requires the scholar's explicit declaration. Stage 3 must not start automatically.
