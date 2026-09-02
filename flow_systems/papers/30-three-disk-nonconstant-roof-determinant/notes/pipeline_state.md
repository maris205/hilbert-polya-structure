# P30 pipeline state

Synchronized: **2026-09-03 (UTC+08:00)**

Current controlling state: **ARS STAGE 3 PHASE 0 COMPLETE / AWAITING REVIEWER-CONFIGURATION CONFIRMATION**.

| State field | Value |
|---|---|
| Pipeline global state | `stage3_phase0_complete_awaiting_scholar_reviewer_configuration_confirmation` |
| ARS Stage 1 | `COMPLETE` |
| ARS Stage 2 WRITE | `COMPLETE` |
| ARS Stage 2.5 INTEGRITY | `COMPLETE`; verdict `PASS` |
| Stage-2.5 mandatory checkpoint | `SATISFIED_BY_STAGE3_ENTRY_AUTHORIZATION` |
| Stage 3 entry | `authorized=true`; receipt `../../../BATCH_ROUND10_STAGE3_AUTHORIZATION_RECEIPT.json` |
| Stage 3 Phase 0 | `COMPLETE`; 4 dynamic cards + 1 fixed DA; validation `PASS` |
| Stage 3 substantive review | `reviewer_configuration_confirmed=false`; `started=false`; Phase 1/2 reports `0/0`; editorial decision `NONE` |
| Stage 4 | `authorized=false` |
| Phase-0 mutation/Route boundary | manuscript/bibliography/PDF edited `false`; scientific executions `0`; Route advancement `NONE` |
| Next legal transition | `AWAITING_EXPLICIT_SCHOLAR_CONFIRMATION_OF_REVIEWER_CONFIGURATION` |
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
| Official E6 | `status=skipped_no_revision_evidence`; `revision_evidence_bundle_sha256=null`; findings `[]` |

Official E6 remains skipped because no official ARS Revision-Evidence Bundle
exists.  The project-local repair lineage must not be represented as that
bundle.

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
| Route advancement from Stage 2.5 | `NONE` |

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
