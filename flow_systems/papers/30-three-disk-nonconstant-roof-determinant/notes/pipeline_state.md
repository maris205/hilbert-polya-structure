# P30 pipeline state

Synchronized: **2026-09-03 (UTC+08:00)**

Current controlling state: **ARS STAGE 4 AUTHOR-SIDE REVISION COMPLETE / AWAITING SCHOLAR CONFIRMATION BEFORE STAGE 3 PRIME**.

| State field | Value |
|---|---|
| Pipeline global state | `stage4_complete_awaiting_scholar_confirmation_before_stage3_prime` |
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
| Next legal transition | `AWAITING_SCHOLAR_CONFIRMATION_BEFORE_STAGE3_PRIME`; Stage 3 prime, Stage 4.5, and Stage 5 not started |
| Active integrity findings | `[]` (`0`) |

## Canonical package

| Artifact | State |
|---|---|
| [Manuscript](../paper/manuscript.tex) | SHA-256 `af270bc06a3f1e00d657fdc875585e3da9ab9b2b7198ad8d096d188a93af9506` |
| [Bibliography](../paper/references.bib) | 26 cited entries; SHA-256 `1b2538b3cfa9e0326112dd3ae086a420032e4edecd06f9e27939d2691d10de6f` |
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

## Current Stage-4 completion bindings

| Artifact | SHA-256 |
|---|---|
| [Per-paper completion report](stage4_completion_report.md) | `2b10af7850c298bc55020279c68c9b3802802777b56fda809172a8222c95566d` |
| [Bounded semantic audit](stage4_unregistered_claim_drift_audit.md) | `4370074983c10644e5cc256076e4dba42532573eee0b8f63c08f6ef89194e42c` |
| [Route crosswalk](stage4_route_crosswalk.md) | `d1af9901e66450ca88d01419a9fe02d6606bac2f7e7e0999a14a9213bb9ce166` |
| [Revision-Evidence Bundle](stage4_revision_evidence_bundle.json) | `e6ff8927bd88d3d6c08c74f366c84f7704f84bbb67b5a9f178a12ee7a62f31e2` |
| [Batch completion report](../../../BATCH_ROUND10_STAGE4_COMPLETION_REPORT.md) | `b285a5478b08f9740926d534ad5256237ac5bd43da5059586fd3d87daced830a` |
| [Batch completion receipt](../../../BATCH_ROUND10_STAGE4_COMPLETION_RECEIPT.json) | `9628917f81d07288dbb6a255f922c397ca87cf4114df61a07fe600c02cfb97bd` |

The ClaimIntent replay is `0/0` vacuous and not a clean certificate. Completion
rests on the bounded changed-operation/E1 semantic audit. `A0_FAIL / A2_NOT_ELIGIBLE / NO_ROUTE_PROMOTION`; formal tuple `UNASSIGNED`; Route B uninvoked.
Canonical bytes and scientific trees are unchanged. Stage 3 prime has not
started.
