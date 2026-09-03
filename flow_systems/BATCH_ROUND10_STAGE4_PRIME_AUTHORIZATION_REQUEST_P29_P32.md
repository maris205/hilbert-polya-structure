# Round 10 Papers 29 and 32 -- Stage 4′ Exact Authorization Request

Date: **2026-09-03 UTC**

Status: `AWAITING_EXPLICIT_AUTHOR_CONFIRMATION`

This artifact is preparation-only. It changed no manuscript, bibliography, PDF, experiment, result, registered claim, initial dynamical system, or Route state. A later exact confirmation is required before any listed revision, source, proof-audit, or bibliography operation is executed.

Machine-readable request: `BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P29_P32.json` (SHA-256 `3a17181450f040e274f1fa6c31386ff2593c04f409013908bfad759d408d65fa`).

The request contains **11 residual roadmap items**, **1 Round-3 regression issue**, **26 exact target entries**, and **36 block/operation pairs**.

## Frozen authority bindings

| Artifact | SHA-256 |
|---|---|
| `BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_AUTHOR_EVENT_20260903.txt` | `111505020ac13b92ac253361e21777de8343455edd9ed3a4436fe924600cb812` |
| `BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_AUTHORIZATION_RECORD.md` | `67ad4ce8bfb34676b46ffb96e8c9833c1204ada3ffde1e0dc542ea43c46acca5` |
| `BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_AUTHORIZATION_RECEIPT.json` | `c94137879092d7d475b22c8985a8f09073c29027f77a89b8ccb8749acfdac48b` |
| `BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_INPUT_FREEZE.json` | `82dbf52120f120ffea6ba82b4614c69d4022a32bc01305a892eadde92b8248b7` |
| `BATCH_ROUND10_STAGE3_PRIME_ROUND3_MANDATORY_CHECKPOINT.md` | `dff758cae93c8fba9c17d9b26cbe6c07ae3584d7645aa0db357ab75a73fee94e` |
| `BATCH_ROUND10_STAGE3_PRIME_ROUND3_FINAL_INTEGRITY_AUDIT.json` | `b61f44535bd83b84da163391f30225de1b6afba5aa1434babb0bcca808c5b692` |
| `BATCH_ROUND10_STAGE3_PRIME_ROUND3_FINAL_INTEGRITY_RECEIPT.json` | `f6eb05b19724b868b5aacb3dfbfb28ec56995675effd5984176bd9aea202f53e` |
| `skills/route-a-evaluator.md` | `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c` |
| `skills/route-b-evaluator.md` | `170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595` |

## Frozen paper inputs

| Paper | Round-3 verdict | Traceability | Checker | Stage-4′ base | Block manifest | Bibliography | Claim surfaces |
|---|---|---|---|---|---|---|---|
| P29 | `98e59c1eaea31c5984ebe79ab85d5beabd08a0bc4b768710586d814da2ee4507` | `7c09a9ce0e5e69cde594a3c825102fae79c54e352b7c553456f2cb385b859fea` | `004745261d59e14f8ad5da3bc154eccab1fdd6ee1742719eeb5817e536586e07` | `eb6694ccbe8881a22a04bbe224883406ffbb7b0ad9269268b581f16b83f40bda` | `eaa1450e6ddb5198837fe7ef557513d36bc904eae83220b826379dd06a028294` | `c78ea003596e5c27fb1332643db2654dd6a67f96b9ba25b923cd2af655540555` | 0 |
| P32 | `28c0ce281eba26240e584bc7dd1aa787e32c03b742b09a53cab97c4d0f3e8f48` | `6b4efd892d4f551481363c99e7b01f7e2f8a21550807c86eb994ae589d95b0d6` | `7151f6f309ecc98d1056416272f95d2c69ea1f35f8d99dd51a079c1bdd305d89` | `d1a65f96d09477f19250acecb77c578c83218ca0deb1ca75ad0bbe4398f24d05` | `1619df00762015f4e4c9130c6b37373148a162da69810c4dc10af5b0a0bba056` | `e699c96196377892d3aa1f280e6a5117001c3cec37a511a3d1c08fdc52127de9` | 0 |

## P29 -- 4 residual items, 1 new-issue action

| Item | Kind | Residual/severity | Exact proposed target/operation set |
|---|---|---|---|
| `REV-R1-1` | `residual_roadmap_item` | `must_fix` | `B0048/replace_block`, `B0048/insert_after`, `B0080/replace_block`, `B0089/replace_block`, `B0107/replace_block` |
| `REV-R3-1` | `residual_roadmap_item` | `should_fix` | `B0112/replace_block` |
| `REV-R3-2` | `residual_roadmap_item` | `should_fix` | `B0113/replace_block` |
| `REV-DA-2` | `residual_roadmap_item` | `should_fix` | `B0084/replace_block`, `B0084/insert_after` |
| `NEW-1` | `round3_regression_new_issue` | `minor` | `B0049/replace_block` |

Implementation branches:

- `REV-R1-1`: Run a dated, bounded replay of the frozen interfaces and exact query strings; publish a row-level retrieval/deduplication/screening ledger for the replay and a deterministic P29-S01--P29-S22 inventory-to-matrix row crosswalk. Keep the missing original-session rejected rows explicitly unavailable, label replay rows as new observations, and bind every new ledger/crosswalk artifact by path, schema, and SHA-256.
- `REV-R3-1`: Replace the reader map with one complete dependency/stop map: ObjectLedger input validation; Gate Q to oriented classes and owners or a named quotient-not-certified stop; Gate M to MECHANISM_ADMISSIBLE, SPLIT_IDEAL_CODOMAIN_OBSTRUCTION, or FORMAL_MAP_REFUTED; PerformanceLedger to a valid empty/result skeleton or its named hash/freeze/reconciliation stops; and replay to pass or first-mismatch stop. Every edge remains prospective.
- `REV-R3-2`: Assign a fail-closed output to each unexecuted control: owner-label permutation failure -> CONTROL_LABEL_DEPENDENCE_STOP; inversion-paired failure -> CONTROL_REPRESENTATIVE_INVARIANCE_STOP; broadened-codomain noncomparability -> CONTROL_CODOMAIN_COMPARABILITY_STOP. Retain the diagnostic/non-diagnostic interpretation and state that no control or stop has been observed.
- `REV-DA-2`: Replace the scientific-usefulness wording with prospective organizational stress-test value pending implementation. Define, but do not run, one labeled synthetic fixture SF-LITERAL-01 with a frozen owner input, unordered-conjugate-pair baseline, literal-branch candidate, expected codomain-specific typed stop, and a prohibition on treating the expected disposition as performance or an all-codomain obstruction.
- `NEW-1`: Replace 'independently assessed' with 'assessed from procedurally role-separated, same-model-family perspectives'; state that role separation does not remove correlated-error risk and make no independence claim. No review result or scientific disposition changes.

## P32 -- 7 residual items, 0 new-issue action

| Item | Kind | Residual/severity | Exact proposed target/operation set |
|---|---|---|---|
| `REV-P32-EIC-W1` | `residual_roadmap_item` | `must_fix` | `B0018/replace_block`, `B0018/insert_after` |
| `REV-P32-EIC-W2` | `residual_roadmap_item` | `must_fix` | `B0098/replace_block`, `B0098/insert_after`, `B0125/replace_block` |
| `REV-P32-EIC-W4` | `residual_roadmap_item` | `should_fix` | `B0049/replace_block`, `B0128/insert_after` |
| `REV-P32-R1-W1` | `residual_roadmap_item` | `must_fix` | `B0081/replace_block`, `B0081/insert_after`, `B0082/replace_block`, `B0083/replace_block`, `B0083/insert_after`, `B0084/replace_block`, `B0131/replace_block` |
| `REV-P32-R1-W2` | `residual_roadmap_item` | `must_fix` | `B0090/replace_block`, `B0090/insert_after`, `B0091/replace_block` |
| `REV-P32-R1-W4` | `residual_roadmap_item` | `must_fix` | `B0044/replace_block`, `B0044/insert_after`, `B0047/replace_block`, `B0047/insert_after`, `B0109/replace_block` |
| `REV-P32-DA-M1` | `residual_roadmap_item` | `must_fix` | `B0060/replace_block`, `B0060/insert_after`, `B0066/replace_block`, `B0072/replace_block` |

Implementation branches:

- `REV-P32-EIC-W1`: Run a bounded, dated closest-work search across owner algorithms, homology-cover factors, formal coefficient objects, and compact-uniform limit programs. Name the closest works individually and add a four-component overlap/difference matrix. Source-verify every retained record; add at most four verified bibliography records under deterministic keys P32-CW01--P32-CW04; retain the bounded-search and no-priority boundary.
- `REV-P32-EIC-W2`: Use a commit-pinned public repository base as the stable resolving locator. Enumerate every artifact claimed current in Section 6, not only four examples, and give each repository-relative path, full SHA-256, byte count, schema/version or explicit non-schema media type, access state, and bounded evidentiary role. Make no persistent-archive or DOI claim.
- `REV-P32-EIC-W4`: Keep the main executed-method block limited to corpus capture, deduplication, screening, effect coding, synthesis, and nonexecution boundaries. Move the four role labels, same-family limitation, MAJOR_REVISION code, and author-adjudication history into a separately labeled development-provenance paragraph in the declarations; do not represent the roles as independent validation.
- `REV-P32-R1-W1`: Use a self-contained formalization rather than an analogy: declare coefficient rings, exponent/owner monoids, support conditions, topology/filtration, equality, localization domains, transition maps, R_+, the separately typed R_0, scalar specialization, and singleton projections with complete domains and codomains. Add a labeled well-definedness/compatibility lemma and proof for the operations actually used. If any definition or proof does not close, retain UNDEFINED/NOT_EVALUABLE and stop; assert no global-product or recovery theorem.
- `REV-P32-R1-W2`: Replace the prose registry with one complete AN-1--AN-5 table. Each row must identify the exact logarithmic summand and branch convention, owner and modulus indices, schedule/coupling, K(delta,T,R), quantified limit order, the explicit majorant obligation, the precise sum/limit or limit/limit interchange claimed, prerequisites, and current status. Preserve finite prefixes as nonconvergent diagnostics and do not assert a tail theorem.
- `REV-P32-R1-W4`: Run a dated replay of the frozen search strings and publish a complete current 51-manifestation retrieval/deduplication/screening/retention ledger, explicitly distinct from unavailable historical row decisions. For every decision-bearing source use, publish a source-to-claim table with exact passage locator, hypotheses, correction state, applicability statement, and prohibited stronger transfer; unresolved or inaccessible passages remain INCONCLUSIVE.
- `REV-P32-DA-M1`: Add the exact conditional scalar lemma: for ell>0, real s>0, and integer m>=2, Phi_m(s)>B(s). Prove it by x=exp(-s ell/m) in (0,1), so (1-x)^m < 1-x < 1-x^m. Apply it only conditionally to m=d after a valid higher-content factor derivation and to m=N after a valid zero-content derivation. It supplies no factor derivation, ownerwise observation, global obstruction, recovery result, or Route credit.

## Supporting scopes requested for later execution

- P29: dated replay ledger plus an admitted-ID/evidence-row crosswalk; historical missing rows remain missing.
- P32: bounded closest-work search, with zero to four source-verified `P32-CWxx` bibliography additions only if required.
- P32: commit-pinned, schema-bearing inventory of every artifact claimed current in Section 6; no uncreated archive or DOI claim.
- P32: dated 51-manifestation replay ledger and exact claim-to-passage matrix; inaccessible rows remain `INCONCLUSIVE`.
- P32: self-contained formal-definition/compatibility audit and the exact conditional scalar lemma stated in the JSON request.

## Boundaries

- Every action is proposed as `will_address` and displayed in `source_traceability` order. A later patch may use a subset of an approved target/operation set but may not broaden it.
- The two claim-surface manifests contain zero registered surfaces. No registered-claim replacement and no collateral authorization is requested.
- There is no current revision patch, manuscript or bibliography write, PDF build, scientific execution, or result refresh.
- The scalar lemma is conditional and elementary; it does not derive either candidate factor or produce an ownerwise observation, global obstruction, recovery result, or Route credit.
- Route-A coordinates, the five initial systems, and canonical manuscript/bibliography/PDF triples remain frozen. Route B and Stages 4.5--6 remain unauthorized.
- Any target expansion, registered-claim change, verification failure, failed definition/proof, scientific-value change beyond the exact conditional lemma, build failure, Route change, or later-stage transition stops for a new checkpoint.

## Short confirmation

Reply `确认` to approve this exact JSON request and its SHA-256. Any byte change to the request requires a new confirmation.
