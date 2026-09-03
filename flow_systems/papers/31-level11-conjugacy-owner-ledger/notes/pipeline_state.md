# P31 pipeline state

Synchronized: **2026-09-03 (UTC+08:00)**

Current controlling state: **ARS STAGE 3′ ROUND 1 ABORTED — `phase1_lint_failed` / AWAITING ROUND-2 AUTHORIZATION**.

| State field | Value |
|---|---|
| Pipeline global state | `stage3_prime_round1_aborted_awaiting_round2_authorization` |
| ARS Stage 1 | `COMPLETE` |
| ARS Stage 2 WRITE | `COMPLETE` |
| ARS Stage 2.5 INTEGRITY | `COMPLETE`; verdict `PASS`; authorized two-surface repair replay complete |
| Stage-2.5 mandatory checkpoint | `SATISFIED_BY_STAGE3_ENTRY_AUTHORIZATION` |
| Stage 3 entry | `authorized=true`; receipt `../../../BATCH_ROUND10_STAGE3_AUTHORIZATION_RECEIPT.json` |
| Stage 3 Phase 0 | `COMPLETE`; scholar-confirmed; 4 dynamic cards + 1 fixed DA; validation `PASS` |
| Stage 3 substantive review | `COMPLETE`; Phase 1/2 reports `5/5`; editorial decision `Major Revision`; source weaknesses `13`; roadmap items `11 must-fix` |
| Stage 3 final validation | `PASS`; `../../../BATCH_ROUND10_STAGE3_VALIDATION_RECEIPT.json`; SHA-256 `808d0a89b27bf538b9a8134225e824d1d17952e4ed5df86d4ed7fe1b5f694c7b` |
| Stage 4 | `COMPLETE WITHIN EXACT AUTHORIZATION`; 11/11 items; 11 operations; 6 RESOLVED + 5 DELIBERATE_LIMITATION; 8/78 affected E1; +440 words; 13-page clean preview |
| Stage-4 write boundary | only versioned `notes/` revision artifacts changed; canonical manuscript/bibliography/PDF and science trees unchanged; Route advancement `NONE` |
| Stage 3′ Round 1 | `ABORTED / phase1_lint_failed` fail-closed; official checker/apply chain `PASS`; recorded 4/6/1; audit-supported 3/7/1; mechanical B3 (Major Revision candidate) suppressed; no decision issued |
| Semantic-audit provenance | fresh-context; role-separated; same-family; not independent error processes |
| Next legal action | only a new user `确认` authorizing fresh Stage 3′ Round 2 with a new round id, new manifest, fresh Phase-1/2A contexts, and all Round-1 artifacts preserved |
| Active Stage-3′ findings | `REV-P31-009`: recorded FULL, audit-supported PARTIAL/must-fix (false FULL); Phase-1 criterion-inheritance drift at `REV-P31-005` and `REV-P31-009` |

## Canonical package

| Artifact | State |
|---|---|
| [Manuscript](../paper/manuscript.tex) | SHA-256 `f92fb801b08855f8068e742e3d0ce6cce0100ed7111e04cb03a75b235302a14a` |
| [Bibliography](../paper/references.bib) | 22 cited entries; unchanged by repair; SHA-256 `b9078a8468e821feb31c6dc01b41c787991e36d376f81298850271573eaf9958` |
| [PDF](../paper/paper.pdf) | 12 pages; 222,542 bytes; SHA-256 `f40a230291ea432d44b197e005d333147a21fc3f9c3a24f2444e4d2ec90d7722` |

## Explicit paper progress

The paper makes a deterministic canonicalization biconditional the primary
certificate target and demotes the 9,453 unordered pair dispositions to a
derived adversarial audit.  It distinguishes global owners `G`, the
occurrence-level incidence ledger `I`, and the cell-local quotient `C`.

The reconstructability contract is explicitly asymmetric: if occurrence-level
`I` is complete under the declared schema, complete `I` can project `G` and
induce `C`; neither `G` alone nor `C` alone can reconstruct occurrence-level
`I`.  This is a prospective interface result.  No `G`, `I`, or `C` table,
owner partition, canonicalization theorem, or all-pairs audit has been
materialized.  Contribution novelty remains unassessed.

## Exact Stage 2.5 ledger

| Audit surface | Exact state |
|---|---|
| References | `22/22 VERIFIED`; `0` failed |
| Citation contexts | `7/22` sampled; `7/7` supported within boundaries |
| Phase C quantitative/data surfaces | `45/45`; findings `[]`; figures `0`; tables `0` |
| Phase D originality | `21/67`; sections `10/10`; `21 ORIGINAL`; authorized repair paragraphs `2/2` separately reviewed; `0` close/verbatim |
| Claim Registry | `78` registered = `68 HIGH-IMPACT + 3 RANDOM + 7 NOT-SELECTED` |
| Phase E selected claims | `71/71 VERIFIED`; `89` evidence tuples; `89` anchorless |
| Semantic receipt | [stage2_5_phase_e_semantic_verdicts.json](stage2_5_phase_e_semantic_verdicts.json); SHA-256 `1f531a2bfcd0e0171fc5bc95ee4622e644234ac7a75b7328f3763c955fb803d5` |
| Failure-mode checklist | `7/7 CLEAR` |
| Experiment intake | `status=no_experiments_declared`; `declared_by=scholar`; `experiment_provenance=[]`; alignment rows required `0` |
| Own science executions/results | executions `0`; newly reported own results `0`; canonical-result refreshes `0` |
| Official E6 | Stage-4 Revision-Evidence Bundle present at SHA-256 `463c00cf2975c945ef5f9c180bb4ba0040ebddf13731da5f0e16bc12ac43f612`; Stage-4.5 E6 `NOT_INVOKED`; bounded semantic audit `PASS` is not official E6 |

A schema-compatible Revision-Evidence Bundle now exists for this Stage-4 revision.
Official Stage-4.5 E6 has not been invoked; the bounded Stage-4 semantic audit
must not be represented as the official E6 verdict.

Exact C4 boundary: “This check verifies disclosure and claim-to-provenance
fidelity. It does not judge whether the experiment was correctly designed,
run, statistically adequate, or reproducible by ARS.”

## Roadmap position

| Item | State |
|---|---|
| Frozen system | fixed positive time change of the `Gamma_0(11)` geodesic flow; oriented primitive owner; inverse separate; powers repetitions; Hecke degree distinct |
| Route A | `A1_ONLY_PREPARATION`; formal tuple `UNASSIGNED`; assigned tuples `0` |
| A2 | positive arithmetic results `0`; absent |
| A3 / A4 | `false / false`; not attempted |
| Route B | `NOT_INVOKED`; closed |
| Route advancement from Stage 4 | `NONE` |

## Audit and correction traceability

| Artifact | SHA-256 |
|---|---|
| [Per-paper integrity report](stage2_5_integrity_report.md) | `bad8a2260b89d2b8724e42e763be59a9687002cf37a79ad37fadca8cb143d265` |
| [Per-paper machine report](stage2_5_integrity_report.json) | `52fe4a73db645a4d83c0665fc7961da18baf77c7a80d9b3c54e1d339fd5a8754` |
| [Authorized repair lineage](stage2_5_authorized_repair_lineage.json) | `5a9f608f9a25074cdbcc553c6b101a95a5ac57318d1f6eae04722bcef72e19c7` |
| [Post-repair build receipt](stage2_5_postrepair_build_receipt.json) | `948df804c6e5886d5b6e04a18e3a14f2d84290618cd9a84a5af6ea5e247aec2b` |
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

Stage 2.5 PASS is coverage-bounded.  It does not certify canonicalization
correctness, scientific execution, semantic-extraction completeness, global
novelty, or route promotion, and it does not remove the mandatory scholar
checkpoint.

## Frozen Stage-4 completion bindings

| Artifact | SHA-256 |
|---|---|
| [Per-paper completion report](stage4_completion_report.md) | `4c24f36dfddefd6ac9647b7fe30e410424c5d251efdf1b68808de21b949a5d1d` |
| [Bounded semantic audit](stage4_unregistered_claim_drift_audit.md) | `3730bd7380221f0f648b96c5051529682ba43fd64f2571860bd2c8b576eab80d` |
| [Route crosswalk](stage4_route_crosswalk.md) | `e851c2ee493414fe26321740aac277e95cd196372a11bc2618eb089b8ad1eff2` |
| [Revision-Evidence Bundle](stage4_revision_evidence_bundle.json) | `463c00cf2975c945ef5f9c180bb4ba0040ebddf13731da5f0e16bc12ac43f612` |
| [Batch completion report](../../../BATCH_ROUND10_STAGE4_COMPLETION_REPORT.md) | `b285a5478b08f9740926d534ad5256237ac5bd43da5059586fd3d87daced830a` |
| [Batch completion receipt](../../../BATCH_ROUND10_STAGE4_COMPLETION_RECEIPT.json) | `9628917f81d07288dbb6a255f922c397ca87cf4114df61a07fe600c02cfb97bd` |

## Current Stage-3′ Round-1 bindings

| Artifact | SHA-256 |
|---|---|
| [Verification report](stage3_prime_round1_verification_report.md) | `da4852ef02ead1ec6635b80940731e5e92cc7c78f7e8a3bb5389d0f92f9eb659` |
| [Checker/semantic receipt](stage3_prime_round1_checker_receipt.json) | `15b12b4e6969d1d050f8257d1fb5a1cd3853f88bf930e1a770bc81433b7b2670` |
| [Abort record](stage3_prime_round1_abort_record.json) | `fd86640c991a79034866d875862524d007b247ec1d7b7ff7183ebf36cd7b951c` |
| [Batch outcome report](../../../BATCH_ROUND10_STAGE3_PRIME_ROUND1_REPORT.md) | `16799921ba4222fca534adf9c56b242879b012576bb72bac9ba95c025cdd8fbf` |
| [Batch outcome receipt](../../../BATCH_ROUND10_STAGE3_PRIME_ROUND1_RECEIPT.json) | `2d315dae3f051956698958fab9ea95b0024ec7e78d78c8abd9e4a3ead4377ba2` |

The ClaimIntent replay is `0/0` vacuous and not a clean certificate. Completion
rests on the bounded changed-operation/E1 semantic audit. Route A A1 owner/canonicalization preparation; formal tuple `UNASSIGNED`; positive arithmetic A2 `0`; Route B uninvoked.
Canonical bytes and scientific trees are unchanged. Round 1 is immutable and
failed closed. Stage 4.5, Stage 5, canonical promotion, submission, Route
advancement, result refresh, and new scientific execution remain unauthorized.
