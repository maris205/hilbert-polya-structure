# P30 pipeline state

Synchronized: **2026-09-04 UTC**

Current controlling state: **`stage4_5_round1_fail_awaiting_exact_correction_authorization`**.

<!-- ROUND10_STAGE4_PRIME_EXECUTION_STAGE4_5_ROUND5_STATUS_SYNC_20260904 -->

| Current gate field | Value |
|---|---|
| Pipeline global state | `stage4_5_round1_fail_awaiting_exact_correction_authorization` |
| Current completed gate | fresh Stage 4.5 Round 1 `FAIL`; full audit completed, no silent repair |
| Audit denominators | references 28/28; contexts 30/30 = 4 verified + 26 anchorless; claims 102/102; evidence 104/104 |
| Blockers | 1 Serious + 3 Medium: passage locators, 26-vs-28 wording, stale Stage-2.5 status, AI disclosure interval |
| Build | `PASS`, 16 pages; unresolved citations/references and overfull boxes `0` |
| Route | A0_FAIL / A2_NOT_ELIGIBLE; formal tuple `UNASSIGNED`; A3/A4 `0`; Route B uninvoked |
| Frozen boundaries | canonical manuscript/bib/PDF, science/results, initial system and Route crosswalk unchanged |
| Next legal transition | bounded source-finalization and exact correction-request preparation; patch application requires later confirmation |

## Historical previous-checkpoint state

<!-- ROUND10_STAGE4_PRIME_ROUND4_STATUS_SYNC_20260904 -->

| State field | Value |
|---|---|
| Pipeline global state | `stage4_prime_author_side_complete_awaiting_stage4_5_authorization` |
| ARS Stage 1 | `COMPLETE` |
| ARS Stage 2 WRITE | `COMPLETE` |
| ARS Stage 2.5 INTEGRITY | `COMPLETE`; verdict `PASS` |
| Stage-2.5 mandatory checkpoint | `SATISFIED_BY_STAGE3_ENTRY_AUTHORIZATION` |
| Stage 3 entry | `authorized=true`; receipt `../../../BATCH_ROUND10_STAGE3_AUTHORIZATION_RECEIPT.json` |
| Stage 3 Phase 0 | `COMPLETE`; scholar-confirmed; 4 dynamic cards + 1 fixed DA; validation `PASS` |
| Stage 3 substantive review | `COMPLETE`; Phase 1/2 reports `5/5`; editorial decision `Major Revision`; source weaknesses `13`; roadmap items `9 = 8 must + 1 should` |
| Stage 3 final validation | `PASS`; `../../../BATCH_ROUND10_STAGE3_VALIDATION_RECEIPT.json`; SHA-256 `808d0a89b27bf538b9a8134225e824d1d17952e4ed5df86d4ed7fe1b5f694c7b` |
| Stage 4 | `COMPLETE WITHIN EXACT AUTHORIZATION`; 9/9 items; 21 operations; 7 RESOLVED + 2 DELIBERATE_LIMITATION; 21/95 affected E1; +635 words; 15-page clean preview |
| Stage-4 write boundary | only versioned `notes/` revision artifacts changed; canonical manuscript/bibliography/PDF and science trees unchanged; Route advancement `NONE` |
| Stage 3′ Round 1 | `ABORTED / phase1_lint_failed` fail-closed; official checker/apply chain `PASS`; recorded and audit-supported aggregates both 4/5/0; Phase-1 criterion-inheritance drift in 2 rows; mechanical B4 (Major Revision candidate) suppressed; no decision issued |
| Stage 3′ Round 2 | `COMPLETE`; Phase 1/2A/2B PASS; final 4/5/0; adjustments/new issues/dissents/escalations all `0`; official checker `PASS`, apply chain `pass`; decision `Major Revision / ARS B4` |
| Stage 4′ author-side revision | `COMPLETE`; 5/5 residuals; 14 operations; 113/127 preserved blocks; 54/54 queries; 28-row matrix; 16-page clean preview; final audit 86/86; Stage 4.5 `NOT_INVOKED` |
| Semantic-audit provenance | fresh-context; role-separated; same-family; not independent error processes |
| Next legal action | fresh Stage 4.5 audit of the current versioned Stage-4′ chain; no silent repair or promotion |
| Current gated scope | All 5/5 residual items are addressed by 14 authorized operations. The final chain preserves 113/127 base blocks, records 54/54 successful dated metadata queries and a 28-row passage matrix, and appends two verified correction records only to the notes-side bibliography. The clean preview is 16 pages with zero blocking TeX findings or overfull boxes. |

## Canonical package

| Artifact | State |
|---|---|
| [Manuscript](../paper/manuscript.tex) | SHA-256 `af270bc06a3f1e00d657fdc875585e3da9ab9b2b7198ad8d096d188a93af9506` |
| [Bibliography](../paper/references.bib) | 26 cited entries; SHA-256 `1b2538b3cfa9e0326112dd3ae086a420032e4edecd06f9e27939d2691d10de6f` |
| Citation style | `plainnat` numeric; unchanged |
| [PDF](../paper/paper.pdf) | 14 pages; 255,074 bytes; SHA-256 `c8f54cf535ca1fa12a14662a248889b332c8a3b0c5b4db6d7abae707827f313e` |

## Explicit paper progress

The paper turns the nonconstant physical-roof determinant proposal into six
typed, fail-closed gates and a common-norm uncertainty contract with four
numerical channels plus separately propagated geometry/roof-input uncertainty.
That is a concrete design and method-interface advance.  No roof, operator,
determinant, enclosure, fidelity result, or nontransfer theorem has been
constructed or reported.

## Exact Stage 2.5 ledger

| Audit surface | Exact state |
|---|---|
| References | `26/26 VERIFIED`; `0` failed |
| Citation contexts | `8/26` sampled; `8/8` supported within boundaries |
| Phase C quantitative/data surfaces | `53/53`; findings `[]`; figures `0`; tables `0` |
| Phase D originality | `27/87`; sections `10/10`; `27 ORIGINAL`; `0` close/verbatim |
| Claim Registry | `95` registered = `75 HIGH-IMPACT + 3 RANDOM + 17 NOT-SELECTED` |
| Phase E selected claims | `78/78 VERIFIED`; `78` evidence tuples; `78` anchorless |
| Semantic receipt | [stage2_5_phase_e_semantic_verdicts.json](stage2_5_phase_e_semantic_verdicts.json); SHA-256 `6a03a331adef1c4914a19e3b61579ae3e3791e7f3e6fe8a9f1e3b285998b9509` |
| Failure-mode checklist | `7/7 CLEAR` |
| Experiment intake | `status=no_experiments_declared`; `declared_by=scholar`; `experiment_provenance=[]`; alignment rows required `0` |
| Own science executions/results | executions `0`; newly reported own results `0`; canonical-result refreshes `0` |
| Official E6 | Stage-4 Revision-Evidence Bundle present at SHA-256 `e6ff8927bd88d3d6c08c74f366c84f7704f84bbb67b5a9f178a12ee7a62f31e2`; Stage-4.5 E6 `NOT_INVOKED`; bounded semantic audit `PASS` is not official E6 |

A schema-compatible Revision-Evidence Bundle now exists for this Stage-4 revision.
Official Stage-4.5 E6 has not been invoked; the bounded Stage-4 semantic audit
must not be represented as the official E6 verdict.

Exact C4 boundary: “This check verifies disclosure and claim-to-provenance
fidelity. It does not judge whether the experiment was correctly designed,
run, statistically adequate, or reproducible by ARS.”

## Roadmap position

| Item | State |
|---|---|
| Frozen system | no-eclipse equilateral three-disk flow at `d=6a`; Euclidean free-flight clock; primitive cyclic collision-word owner; physical roof distinct from unit-roof control |
| Route A | `A0_FAIL / A2_NOT_ELIGIBLE / NO_ROUTE_PROMOTION`; formal tuple `UNASSIGNED`; assigned tuples `0` |
| A2 | positive arithmetic results `0`; not eligible |
| A3 / A4 | `false / false`; not attempted |
| Route B | `NOT_INVOKED`; closed |
| Route advancement from Stage 4 | `NONE` |

## Audit and correction traceability

| Artifact | SHA-256 |
|---|---|
| [Per-paper integrity report](stage2_5_integrity_report.md) | `2be788bd84a7a85e83f4f9bca46937fad1a68ffc32bfa392e85d600b7171c999` |
| [Per-paper machine report](stage2_5_integrity_report.json) | `d5b8e0024b4a5a12ecfd12d70d4c7bf79e8a6060ac8bb4eee457c9973acfc251` |
| [Batch integrity report](../../../BATCH_ROUND10_STAGE2_5_INTEGRITY_REPORT.md) | `ce99860d6fe60de840c9802757686d4818a1d735dd2b03cf5f11976b1b9d2106` |
| [Batch integrity summary](../../../BATCH_ROUND10_STAGE2_5_INTEGRITY_SUMMARY.json) | `ea4773bd5d612a8095f2f9950854e7274c6ed9d33b1568cc7fb543cd928b0bc9` |
| [Mandatory checkpoint](../../../BATCH_ROUND10_STAGE2_5_MANDATORY_CHECKPOINT.md) | `c4bfa81f36793778589421ee209f64360934572472bbe3f13fb75908c040443c` |
| [Mandatory checkpoint JSON](../../../BATCH_ROUND10_STAGE2_5_MANDATORY_CHECKPOINT.json) | `8d9ecc4d4ccba99762db1656e9055b2e236f0b352c19a144eed32e6df0aa38b8` |
| [Post-repair input freeze](../../../BATCH_ROUND10_STAGE2_5_POST_REPAIR_INPUT_FREEZE.json) | `54bd577683595dd9259ba2a97405b7257a269bf740ffcaa1c0135718869e5041` |
| [Correction authorization receipt](../../../BATCH_ROUND10_STAGE2_5_CORRECTION_AUTHORIZATION_RECEIPT.json) | `14c846c4b32dc77e7735fc645c7afe359c91109cc4c5c6c60554882317c1cf3b` |
| [Correction execution report](../../../BATCH_ROUND10_STAGE2_5_CORRECTION_EXECUTION_REPORT.md) | `e0afdbaa02ef933402f98a8fe03fecf60d3b3ca25d8c6c4694cdd00893fa356a` |
| [Repair lineage](../../../BATCH_ROUND10_STAGE2_5_REPAIR_LINEAGE.json) | `4d4b72779ee7e59b71c66d22abf74774c01a03270a51663d07aefc957ea8e65d` |
| [Experiment declaration receipt](../../../BATCH_ROUND10_STAGE2_5_EXPERIMENT_DECLARATION_RECEIPT.json) | `4d38cbe820e8832604b1cbb9a8443f8da1b6d27f57c4c6143da54fabbc0fdae2` |
| [Validation receipt](../../../BATCH_ROUND10_STAGE2_5_VALIDATION_RECEIPT.json) | `946973cc01c273cb38d88efdfbb4693e709b9aa08e6fb769e649c2c408393c7b` |

Stage 2.5 PASS is coverage-bounded.  It does not certify determinant
correctness, scientific execution, semantic-extraction completeness, global
novelty, or route promotion, and it does not remove the mandatory scholar
checkpoint.

## Frozen Stage-4 completion bindings

| Artifact | SHA-256 |
|---|---|
| [Per-paper completion report](stage4_completion_report.md) | `2b10af7850c298bc55020279c68c9b3802802777b56fda809172a8222c95566d` |
| [Bounded semantic audit](stage4_unregistered_claim_drift_audit.md) | `4370074983c10644e5cc256076e4dba42532573eee0b8f63c08f6ef89194e42c` |
| [Route crosswalk](stage4_route_crosswalk.md) | `d1af9901e66450ca88d01419a9fe02d6606bac2f7e7e0999a14a9213bb9ce166` |
| [Revision-Evidence Bundle](stage4_revision_evidence_bundle.json) | `e6ff8927bd88d3d6c08c74f366c84f7704f84bbb67b5a9f178a12ee7a62f31e2` |
| [Batch completion report](../../../BATCH_ROUND10_STAGE4_COMPLETION_REPORT.md) | `b285a5478b08f9740926d534ad5256237ac5bd43da5059586fd3d87daced830a` |
| [Batch completion receipt](../../../BATCH_ROUND10_STAGE4_COMPLETION_RECEIPT.json) | `9628917f81d07288dbb6a255f922c397ca87cf4114df61a07fe600c02cfb97bd` |

## Historical Stage-3′ Round-1 bindings

| Artifact | SHA-256 |
|---|---|
| [Verification report](stage3_prime_round1_verification_report.md) | `f7f7956dc8c484ae707ce0c48dee2b4bf6a158d5e286c9873fae6fce208db5e8` |
| [Checker/semantic receipt](stage3_prime_round1_checker_receipt.json) | `960bc02225aa6d0e3215ef99e1e9a27179b453783d20f8472d053468fbfcfe9e` |
| [Abort record](stage3_prime_round1_abort_record.json) | `b5692f11d24224b0c17ddad6a467a3ddcd7689cdf6a88a25184f1a3c0b061a0d` |
| [Batch outcome report](../../../BATCH_ROUND10_STAGE3_PRIME_ROUND1_REPORT.md) | `0343b34e2fcb80477046ac5cd0ea069fe51f6efe162edf18dc32b51ad25d0672` |
| [Batch outcome receipt](../../../BATCH_ROUND10_STAGE3_PRIME_ROUND1_RECEIPT.json) | `cfa61eb8504c45250b1658d63193475567a2e8fd0afc1037ef6eda580c196852` |

## Historical Stage-3′ Round-2 bindings

| Artifact | SHA-256 |
|---|---|
| [Verification report](stage3_prime_round2_verification_report.md) | `0eec7f0f0179914b04c2d84883501540b5c2c4d35a024abf5700717256d4f2ab` |
| [Official checker receipt](stage3_prime_round2_checker_receipt.json) | `254caf1613906cd493040d87c03ee054c339cc1be43d4ecf22192fffb3fe5dd3` |
| [Phase-2B integration](stage3_prime_round2_phase2b_integration.json) | `5b01ffc57053be2f07b02193503099ad85905b629ba4bd0eeea0df7faa822d24` |
| [Traceability matrix](stage3_prime_round2_traceability.json) | `79d665653d3aa43f469355d48b1b315de4601e8062af33595acb7c0e29c8e548` |
| [Batch outcome report](../../../BATCH_ROUND10_STAGE3_PRIME_ROUND2_REPORT.md) | `817306f3a26bdcef88af02ef7308b3de9436c372ba74f2693538ccfb40db31e3` |
| [Batch outcome receipt](../../../BATCH_ROUND10_STAGE3_PRIME_ROUND2_RECEIPT.json) | `5ce56d67a784df9ff3a6b4ebf8bf3c0102e0f34009b6612ea8e0cd6225d2d53e` |

The ClaimIntent replay is `0/0` vacuous and not a clean certificate. Completion
rests on the bounded changed-operation/E1 semantic audit. `A0_FAIL / A2_NOT_ELIGIBLE / NO_ROUTE_PROMOTION`; formal tuple `UNASSIGNED`; Route B uninvoked.
Canonical bytes and scientific trees are unchanged; Round 1 remains immutable.
Stage 3′ cannot create Route credit: P30 remains `A0_FAIL / A2_NOT_ELIGIBLE /
NO_ROUTE_PROMOTION`, formal tuple `UNASSIGNED`, A3/A4 absent, and Route B
uninvoked. Stage 4′, Stage 4.5, Stage 5, canonical promotion, submission, Route
advancement, result refresh, and new scientific execution remain unauthorized.

## Historical prepared Stage-4′ request bindings

P30 remains complete under Round 2 at Major Revision / B4 (4/5/0). The exact P30/P31 Stage-4′ request is prepared but not authorized or executed.

| Current artifact | SHA-256 |
|---|---|
| [P30/P31 Stage-4′ exact request](../../../BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P30_P31.md) | `4b42e929286be28655f0afa74145370399eed4e7d00f9d205d480db70f8dc03a` |
| [Machine-readable request](../../../BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P30_P31.json) | `a35002ccadc74ef1f05d79b5cd7a81bff728664c27bab679504780fcb91dd688` |
| [Request validation](../../../BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P30_P31_VALIDATION.json) | `52739c5ef1cb2a8142feadb73945fbcbe06a551f43d37fc2e0022b497c6a645c` |
| [Round-3 batch report](../../../BATCH_ROUND10_STAGE3_PRIME_ROUND3_REPORT.md) | `c122ca7f070a20568e47fab8999d6a3bf106b29da21f1dc8bca056b2c1ce5432` |
| [Round-3 batch receipt](../../../BATCH_ROUND10_STAGE3_PRIME_ROUND3_RECEIPT.json) | `ad20c4331936d2d8e1fb55613f72c3cf6bb5d07852775a47071ac427a9107172` |
| [Round-3 mandatory checkpoint](../../../BATCH_ROUND10_STAGE3_PRIME_ROUND3_MANDATORY_CHECKPOINT.md) | `dff758cae93c8fba9c17d9b26cbe6c07ae3584d7645aa0db357ab75a73fee94e` |

Citation style remains plainnat numeric. The canonical manuscript,
bibliography, PDF, science/results, frozen initial system, and Route
coordinates are unchanged. New science executions: `0`. Stage 4.5, Stage 5,
canonical promotion, submission, Route advancement, and result refresh remain
unauthorized.

## Current Stage-4′ completion bindings

Control state: `stage4_prime_author_side_complete_awaiting_stage4_5_authorization`.

All 5/5 residual items are addressed by 14 authorized operations. The final chain preserves 113/127 base blocks, records 54/54 successful dated metadata queries and a 28-row passage matrix, and appends two verified correction records only to the notes-side bibliography. The clean preview is 16 pages with zero blocking TeX findings or overfull boxes.

| Current artifact | SHA-256 |
|---|---|
| [P30 revised anchored draft](../../../papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_prime_revision_round2.tex) | `6c09fa99b17a1f0d47a1c186f0fe48072a3f7d7e45b036a0b237460cd51ae39a` |
| [P30 exact patch](../../../papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_prime_revision_patch_round2.json) | `5876b07df9741ca1d384a78441030d96734a1e87547e94cb7c097efa8d099846` |
| [P30 evidence bundle](../../../papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_prime_revision_evidence_bundle_round2.json) | `abce06717e7f7d0938caf13c3dca01f310b7164a299663b55d178fb270a72d3a` |
| [P30 build receipt](../../../papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_prime_preview_build_receipt_round2.json) | `f95563f1ea0488368f49817b359b8518d9cbab463ba2828fc2361909f291909e` |
| [P30 final audit](../../../papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_prime_final_audit_round2.json) | `dbcf15ba835bdbe3c7a05b7ef8891f92672655e953ae8896907b484628f5a5ba` |
| [Batch completion report](../../../BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_COMPLETION_REPORT.md) | `1f8d5247beebf04090e5b5eff0eb5bdc1fab61899f788e99abda9d80aba01a8f` |
| [Batch completion receipt](../../../BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_COMPLETION_RECEIPT.json) | `adad8657340c41ae4b054b5a291c9bc58a3e21acad5e07eacf285c63a414aa4f` |
| [Mandatory checkpoint](../../../BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_MANDATORY_CHECKPOINT.md) | `5561443b7a061673032eb8fbd635a0b47995e04eb80c977ef6ff5409d5699cad` |

Next legal action: fresh Stage 4.5 audit of the current versioned Stage-4′ chain; no silent repair or promotion. Citation style remains
`plainnat` numeric. Canonical manuscript/bibliography/PDF, science/results,
frozen initial system, and Route coordinates are unchanged. Formal Route-A
tuples, positive arithmetic A2, A3, A4, and Route B remain `0/5`. Stage 5/6,
canonical promotion, submission, result refresh, and new scientific execution
remain unauthorized.
