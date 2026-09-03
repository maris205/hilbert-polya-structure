# P32 manuscript package

Package note: this directory remains the immutable canonical Stage-2.5 package;
current revision/review outputs are versioned under `../notes/`. The authoritative
state is [the paper README](../README.md) and [pipeline state](../notes/pipeline_state.md).
<!-- ROUND10_STAGE4_PRIME_ROUND4_STATUS_SYNC_20260904 -->
Control state: `stage4_prime_request_prepared_awaiting_exact_authorization`. The Stage-4′ request now maps seven residual roadmap items to 18 exact targets and 26 block-operation pairs. It specifies closest-work comparison, a commit-pinned artifact inventory, scholarly/development provenance separation, formal definitions, AN-1--AN-5 closure, a 51-manifestation replay and passage matrix, and a bounded conditional inequality lemma. No patch, revised draft, bibliography, or scientific result was created.
Canonical manuscript/PDF/bibliography bytes and `plainnat` numeric citation style
remain unchanged.

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

## Historical Stage 3′ Round-2 controlling outcome

The committed 7 FULL / 5 PARTIAL / 0 other record is controlled as 6 FULL / 6
PARTIAL / 0 other because `REV-P32-DA-M1` is a false FULL. The no-retry semantic
gate therefore aborted before the response letter, Phase 2B, traceability,
official checker, or decision.

| Artifact | SHA-256 |
|---|---|
| [`stage3_prime_round2_verification_report.md`](../notes/stage3_prime_round2_verification_report.md) | `7039eaba478ee048ff7c1000ff343f0b39c61ca8c05937ef14f57bd00584ae6a` |
| [`stage3_prime_round2_checker_receipt.json`](../notes/stage3_prime_round2_checker_receipt.json) | `d145a433e299b2b63cf4308a2af2f6b66a432732e381dd2a41e5de7a5c17a892` |
| [`stage3_prime_round2_abort_record.json`](../notes/stage3_prime_round2_abort_record.json) | `0768572cc545275f9fd8580552e0653bae82a8022077c52fbece8b99b3c90aeb` |

## Historical Stage 3′ Round-3 checker-backed outcome

P32 completed Round 3 at Major Revision / B4 with checker PASS, 5/7/0, and zero adjustments.

| Current artifact | SHA-256 |
|---|---|
| [P32 Round-3 verification report](../../../papers/32-homology-cover-renormalization-uniformity/notes/stage3_prime_round3_verification_report.md) | `640da9d1f3237575a1e5139da6ce7e75960746673146c44d63b04fa8760f56f1` |
| [P32 Round-3 checker receipt](../../../papers/32-homology-cover-renormalization-uniformity/notes/stage3_prime_round3_checker_receipt.json) | `7151f6f309ecc98d1056416272f95d2c69ea1f35f8d99dd51a079c1bdd305d89` |
| [P32 Round-3 traceability](../../../papers/32-homology-cover-renormalization-uniformity/notes/stage3_prime_round3_traceability.json) | `6b4efd892d4f551481363c99e7b01f7e2f8a21550807c86eb994ae589d95b0d6` |
| [Round-3 batch report](../../../BATCH_ROUND10_STAGE3_PRIME_ROUND3_REPORT.md) | `c122ca7f070a20568e47fab8999d6a3bf106b29da21f1dc8bca056b2c1ce5432` |
| [Round-3 batch receipt](../../../BATCH_ROUND10_STAGE3_PRIME_ROUND3_RECEIPT.json) | `ad20c4331936d2d8e1fb55613f72c3cf6bb5d07852775a47071ac427a9107172` |
| [Round-3 mandatory checkpoint](../../../BATCH_ROUND10_STAGE3_PRIME_ROUND3_MANDATORY_CHECKPOINT.md) | `dff758cae93c8fba9c17d9b26cbe6c07ae3584d7645aa0db357ab75a73fee94e` |

## Stage 2.5 integrity result

- Phase A: 26/26 references checked and 26/26 bibliographically `VERIFIED`; no unresolved finding.
- Phase B: 8/26 citation contexts sampled and 8/8 supported within their stated boundaries.
- Phase C: 58/58 registered quantitative/data surfaces verified; 0 figure/table surfaces; scholar declaration `no_experiments_declared`; `experiment_provenance=[]`.
- Phase D: 24/77 body paragraphs checked across 10/10 major sections, all 24 classified `ORIGINAL`; all five authorized changed paragraphs also received 5/5 inspection.
- Phase E: 98 registered claims, 88 selected claims, and 108/108 evidence tuples; 88/88 selected claims are `VERIFIED`, with zero minor/major/unverifiable verdicts. All 108 tuples remain anchorless.
- Seven-mode audit: 7/7 `CLEAR`, 0 `SUSPECTED`, 0 `INSUFFICIENT EVIDENCE`.
- Official E6: `skipped_no_revision_evidence`, `revision_evidence_bundle_sha256=null`, and no drift finding. The project-local repair evidence is not an official ARS Revision-Evidence Bundle.

## Current Stage 4′ request-preparation outcome

**本轮结论概要。** 本轮明确进展是把 P32 的七个剩余评审项收敛为可逐块执行、可回放的 Stage 4′ 合同：18 个精确目标、26 个 block-operation pairs，并把形式定义、AN-1--AN-5、51 条 replay/matrix 与条件不等式的边界写入请求。正文尚未修改；没有 factor、limit、obstruction 或 Route credit。

| Current artifact | SHA-256 |
|---|---|
| [P29/P32 exact Stage-4′ request](../../../BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P29_P32.md) | `44cf590c2ce5ad86d7a698c436b13e21618e7965a8792dce262845ed2eb4fcf3` |
| [Machine-readable request](../../../BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P29_P32.json) | `3a17181450f040e274f1fa6c31386ff2593c04f409013908bfad759d408d65fa` |
| [377-check validation](../../../BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P29_P32_VALIDATION.json) | `fe80eb7dd58a1fe70766c602794839e4edd71fd8aeb70809663dbe0f21248420` |
| [Batch completion report](../../../BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_COMPLETION_REPORT.md) | `1f8d5247beebf04090e5b5eff0eb5bdc1fab61899f788e99abda9d80aba01a8f` |
| [Batch completion receipt](../../../BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_COMPLETION_RECEIPT.json) | `adad8657340c41ae4b054b5a291c9bc58a3e21acad5e07eacf285c63a414aa4f` |
| [Mandatory checkpoint](../../../BATCH_ROUND10_STAGE4_PRIME_AND_ROUND4_MANDATORY_CHECKPOINT.md) | `5561443b7a061673032eb8fbd635a0b47995e04eb80c977ef6ff5409d5699cad` |

## 结论概要

本轮形成的明确论文进展是：在固定 `1/N` 时间与 `1/N^3` 对数重整化下，把高内容与零内容局部因子锁定为最先、最短的否证性定理目标，并把 content-one 降为只有在两类不利测试存活后才进入的次级分支。该进展是可审计的理论与证书架构，不是已经完成的因子推导或阻碍定理；形式对象、面板、尾界和极限均未构造或执行。

## Citation and claim boundary

P32-S13 is now bibliographically `VERIFIED`, but remains background-only. Its citation carrier remains `anchor:none`, and claim-to-passage faithfulness remains `INCONCLUSIVE`; no theorem passage or locator was invented. The unchanged historical Phase-2 sentence still reports the earlier 25 `VERIFIED` plus P32-S13 `PLAUSIBLE` state as history.

## Route position and next gate

Explicit paper progress: The Stage-4′ request now maps seven residual roadmap items to 18 exact targets and 26 block-operation pairs. It specifies closest-work comparison, a commit-pinned artifact inventory, scholarly/development provenance separation, formal definitions, AN-1--AN-5 closure, a 51-manifestation replay and passage matrix, and a bounded conditional inequality lemma. No patch, revised draft, bibliography, or scientific result was created.

Frozen initial system: unit-speed genus-two geodesic flow; pure homology tower; oriented primitive owner with inverse separate; full-content scope; clock 1/N; logarithmic normalization 1/N^3.

Route mapping: generic Route A A1-A2 preparation with arithmetic A0 unavailable; formal tuple UNASSIGNED; positive arithmetic A2=0; A3=0; A4=0; Route B uninvoked. Across Papers 29--33, formal Route-A
tuples, positive arithmetic A2, A3, A4, and Route B remain `0/5`.

The next legal action is exact author confirmation of the frozen joint P29/P32 Stage-4′ request before any listed operation executes. Canonical manuscript,
bibliography, PDF, science/results, and the frozen system remain unchanged.
Stage 5/6, canonical promotion, submission, Route advancement, result refresh,
and new scientific execution remain unauthorized.

## Batch traceability

| Artifact | SHA-256 |
|---|---|
| [`BATCH_ROUND10_STAGE2_5_INTEGRITY_REPORT.md`](../../../BATCH_ROUND10_STAGE2_5_INTEGRITY_REPORT.md) | `ce99860d6fe60de840c9802757686d4818a1d735dd2b03cf5f11976b1b9d2106` |
| [`BATCH_ROUND10_STAGE2_5_MANDATORY_CHECKPOINT.json`](../../../BATCH_ROUND10_STAGE2_5_MANDATORY_CHECKPOINT.json) | `8d9ecc4d4ccba99762db1656e9055b2e236f0b352c19a144eed32e6df0aa38b8` |
| [`BATCH_ROUND10_STAGE2_5_POST_REPAIR_INPUT_FREEZE.json`](../../../BATCH_ROUND10_STAGE2_5_POST_REPAIR_INPUT_FREEZE.json) | `54bd577683595dd9259ba2a97405b7257a269bf740ffcaa1c0135718869e5041` |
| [`BATCH_ROUND10_STAGE2_5_CORRECTION_AUTHORIZATION_RECEIPT.json`](../../../BATCH_ROUND10_STAGE2_5_CORRECTION_AUTHORIZATION_RECEIPT.json) | `14c846c4b32dc77e7735fc645c7afe359c91109cc4c5c6c60554882317c1cf3b` |
| [`BATCH_ROUND10_STAGE2_5_VALIDATION_RECEIPT.json`](../../../BATCH_ROUND10_STAGE2_5_VALIDATION_RECEIPT.json) | `946973cc01c273cb38d88efdfbb4693e709b9aa08e6fb769e649c2c408393c7b` |
