# P32 manuscript package

Package note: this directory is the immutable canonical Stage-2.5 manuscript
package; its Phase-0 wording below is historical. The authoritative current
state is [the paper README](../README.md) and [pipeline state](../notes/pipeline_state.md):
**`stage3_prime_round2_aborted_awaiting_round3_authorization`.** Stage 3′ Round
2 failed closed at `phase2a_lint_failed`; no decision was signed or emitted,
and a fresh Round 3 requires explicit authorization. Canonical
manuscript/PDF/bibliography bytes remain unchanged.

## Deliverables

- [`manuscript.tex`](manuscript.tex) -- canonical article; SHA-256 `4a3e1f084dc1e27005479971299fd9da67bb6c817278d5de0de6cf03cbc8000a`.
- [`references.bib`](references.bib) -- 26 frozen, fully cited plainnat records; SHA-256 `e699c96196377892d3aa1f280e6a5117001c3cec37a511a3d1c08fdc52127de9`.
- [`paper.pdf`](paper.pdf) -- 13-page, 254332-byte isolated LuaLaTeX/BibTeX build; SHA-256 `66948e247c72a3388a7f3da1f80be1d74860afa1261c99fb18c85e2b8bb84f93`.
- [`stage2_manuscript_audit.md`](stage2_manuscript_audit.md) -- hash, structure, citation, boundary, and build audit.
- [`stage2_5_integrity_report.md`](../notes/stage2_5_integrity_report.md) and [`stage2_5_material_passport.json`](../notes/stage2_5_material_passport.json) -- final per-paper Stage-2.5 report and Schema-9 passport.
- [`stage3_phase0_field_analysis.md`](../notes/stage3_phase0_field_analysis.md) and [`stage3_review_baseline.json`](../notes/stage3_review_baseline.json) -- current Stage-3 Phase-0 configuration and immutable target.

## Historical Stage 3′ Round-1 outcome

Recorded and audited aggregates both remain 6 FULL / 5 PARTIAL / 1 NOT, but
`REV-P32-R1-W2` is a false FULL and `REV-P32-R3-W1` is a false PARTIAL. Phase-1
criterion drift affects `REV-P32-R3-W1` and `REV-P32-DA-M1`; therefore the
mandatory gate aborted with `phase1_lint_failed`, the mechanical B3 candidate is
suppressed, and no decision exists. The fresh-context semantic checks were
role-separated but same-family and are not independent error processes.

| Artifact | SHA-256 |
|---|---|
| [`stage3_prime_round1_verification_report.md`](../notes/stage3_prime_round1_verification_report.md) | `deab1d001c3b6a183a94c371ecb8ddf9494147e23d86ba9dcc0ff1ff22aebb85` |
| [`stage3_prime_round1_checker_receipt.json`](../notes/stage3_prime_round1_checker_receipt.json) | `4033a2346ba98d56f37176523e07f682115838e07e6b73c0395e2020ed4c82f6` |
| [`stage3_prime_round1_abort_record.json`](../notes/stage3_prime_round1_abort_record.json) | `b11516b0046dfb0a8c33d18090df33e0191cf1e9a2f8efe68df189116e27a941` |

## Current Stage 3′ Round-2 controlling outcome

The committed 7 FULL / 5 PARTIAL / 0 other record is controlled as 6 FULL / 6
PARTIAL / 0 other because `REV-P32-DA-M1` is a false FULL. The no-retry semantic
gate therefore aborted before the response letter, Phase 2B, traceability,
official checker, or decision.

| Artifact | SHA-256 |
|---|---|
| [`stage3_prime_round2_verification_report.md`](../notes/stage3_prime_round2_verification_report.md) | `7039eaba478ee048ff7c1000ff343f0b39c61ca8c05937ef14f57bd00584ae6a` |
| [`stage3_prime_round2_checker_receipt.json`](../notes/stage3_prime_round2_checker_receipt.json) | `d145a433e299b2b63cf4308a2af2f6b66a432732e381dd2a41e5de7a5c17a892` |
| [`stage3_prime_round2_abort_record.json`](../notes/stage3_prime_round2_abort_record.json) | `0768572cc545275f9fd8580552e0653bae82a8022077c52fbece8b99b3c90aeb` |

## Stage 2.5 integrity result

- Phase A: 26/26 references checked and 26/26 bibliographically `VERIFIED`; no unresolved finding.
- Phase B: 8/26 citation contexts sampled and 8/8 supported within their stated boundaries.
- Phase C: 58/58 registered quantitative/data surfaces verified; 0 figure/table surfaces; scholar declaration `no_experiments_declared`; `experiment_provenance=[]`.
- Phase D: 24/77 body paragraphs checked across 10/10 major sections, all 24 classified `ORIGINAL`; all five authorized changed paragraphs also received 5/5 inspection.
- Phase E: 98 registered claims, 88 selected claims, and 108/108 evidence tuples; 88/88 selected claims are `VERIFIED`, with zero minor/major/unverifiable verdicts. All 108 tuples remain anchorless.
- Seven-mode audit: 7/7 `CLEAR`, 0 `SUSPECTED`, 0 `INSUFFICIENT EVIDENCE`.
- Official E6: `skipped_no_revision_evidence`, `revision_evidence_bundle_sha256=null`, and no drift finding. The project-local repair evidence is not an official ARS Revision-Evidence Bundle.

## 结论概要

本轮形成的明确论文进展是：在固定 `1/N` 时间与 `1/N^3` 对数重整化下，把高内容与零内容局部因子锁定为最先、最短的否证性定理目标，并把 content-one 降为只有在两类不利测试存活后才进入的次级分支。该进展是可审计的理论与证书架构，不是已经完成的因子推导或阻碍定理；形式对象、面板、尾界和极限均未构造或执行。

## Citation and claim boundary

P32-S13 is now bibliographically `VERIFIED`, but remains background-only. Its citation carrier remains `anchor:none`, and claim-to-passage faithfulness remains `INCONCLUSIVE`; no theorem passage or locator was invented. The unchanged historical Phase-2 sentence still reports the earlier 25 `VERIFIED` plus P32-S13 `PLAUSIBLE` state as history.

## Route position and next gate

Route A remains at generic A1--A2 preparation only: P32 arithmetic A0 is unavailable, the formal tuple is `UNASSIGNED`, positive arithmetic A2 is absent, A3/A4 were not run, and Route B is closed with zero invocation. Stage 3′ cannot create Route credit, and no later review stage changed the frozen system or scientific result. The only next legal action is explicit authorization for a new-id/new-manifest/fresh-context Stage 3′ Round 3.

## Batch traceability

| Artifact | SHA-256 |
|---|---|
| [`BATCH_ROUND10_STAGE2_5_INTEGRITY_REPORT.md`](../../../BATCH_ROUND10_STAGE2_5_INTEGRITY_REPORT.md) | `ce99860d6fe60de840c9802757686d4818a1d735dd2b03cf5f11976b1b9d2106` |
| [`BATCH_ROUND10_STAGE2_5_MANDATORY_CHECKPOINT.json`](../../../BATCH_ROUND10_STAGE2_5_MANDATORY_CHECKPOINT.json) | `8d9ecc4d4ccba99762db1656e9055b2e236f0b352c19a144eed32e6df0aa38b8` |
| [`BATCH_ROUND10_STAGE2_5_POST_REPAIR_INPUT_FREEZE.json`](../../../BATCH_ROUND10_STAGE2_5_POST_REPAIR_INPUT_FREEZE.json) | `54bd577683595dd9259ba2a97405b7257a269bf740ffcaa1c0135718869e5041` |
| [`BATCH_ROUND10_STAGE2_5_CORRECTION_AUTHORIZATION_RECEIPT.json`](../../../BATCH_ROUND10_STAGE2_5_CORRECTION_AUTHORIZATION_RECEIPT.json) | `14c846c4b32dc77e7735fc645c7afe359c91109cc4c5c6c60554882317c1cf3b` |
| [`BATCH_ROUND10_STAGE2_5_VALIDATION_RECEIPT.json`](../../../BATCH_ROUND10_STAGE2_5_VALIDATION_RECEIPT.json) | `946973cc01c273cb38d88efdfbb4693e709b9aa08e6fb769e649c2c408393c7b` |
