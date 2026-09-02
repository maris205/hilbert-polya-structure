# P31 pipeline state

Synchronized: **2026-09-03 (UTC+08:00)**

Current controlling state: **ARS STAGE 3 PHASE 0 COMPLETE / AWAITING REVIEWER-CONFIGURATION CONFIRMATION**.

| State field | Value |
|---|---|
| Pipeline global state | `stage3_phase0_complete_awaiting_scholar_reviewer_configuration_confirmation` |
| ARS Stage 1 | `COMPLETE` |
| ARS Stage 2 WRITE | `COMPLETE` |
| ARS Stage 2.5 INTEGRITY | `COMPLETE`; verdict `PASS`; authorized two-surface repair replay complete |
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
| Official E6 | `status=skipped_no_revision_evidence`; `revision_evidence_bundle_sha256=null`; findings `[]` |

Official E6 remains skipped because no official ARS Revision-Evidence Bundle
exists.  The authorized project-local repair lineage and manual semantic
comparison advisory must not be represented as that bundle.

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
| Route advancement from Stage 2.5 | `NONE` |

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
