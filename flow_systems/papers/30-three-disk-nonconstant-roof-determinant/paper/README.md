# P30 manuscript package

Package note: this directory remains the immutable canonical Stage-2.5 package;
current revision/review outputs are versioned under `../notes/`. The authoritative
state is [the paper README](../README.md) and [pipeline state](../notes/pipeline_state.md).
<!-- ROUND10_STAGE4_PRIME_ROUND4_STATUS_SYNC_20260904 -->
Control state: `stage4_prime_author_side_complete_awaiting_stage4_5_authorization`. All 5/5 residual items are addressed by 14 authorized operations. The final chain preserves 113/127 base blocks, records 54/54 successful dated metadata queries and a 28-row passage matrix, and appends two verified correction records only to the notes-side bibliography. The clean preview is 16 pages with zero blocking TeX findings or overfull boxes.
Canonical manuscript/PDF/bibliography bytes and `plainnat` numeric citation style
remain unchanged.

## Deliverables

- [`manuscript.tex`](manuscript.tex) -- complete English article with an independent Traditional-Chinese abstract.
- [`references.bib`](references.bib) -- 26 frozen, fully cited records in plainnat numeric style.
- [`paper.pdf`](paper.pdf) -- 14-page isolated LuaLaTeX/BibTeX build.
- [`stage2_manuscript_audit.md`](stage2_manuscript_audit.md) -- hash, structure, citation, boundary, and build audit.
- [`stage3_phase0_field_analysis.md`](../notes/stage3_phase0_field_analysis.md) -- current Stage-3 field analysis and reviewer cards.
- [`stage3_review_baseline.json`](../notes/stage3_review_baseline.json) -- immutable Stage-3 review target.
- [`stage3_prime_round2_verification_report.md`](../notes/stage3_prime_round2_verification_report.md) and [`stage3_prime_round2_checker_receipt.json`](../notes/stage3_prime_round2_checker_receipt.json) -- current Round-2 decision and official checker evidence; Round 1 remains historical and immutable.

## Historical prepared Stage-4′ request (not yet authorized)

P30 remains at its completed Round-2 Major Revision / B4 outcome (4/5/0); the joint exact request has 13 residuals, 37 targets, and 156 passing checks, with zero manuscript/bibliography writes.

| Current artifact | SHA-256 |
|---|---|
| [P30/P31 Stage-4′ exact request](../../../BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P30_P31.md) | `4b42e929286be28655f0afa74145370399eed4e7d00f9d205d480db70f8dc03a` |
| [Machine-readable request](../../../BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P30_P31.json) | `a35002ccadc74ef1f05d79b5cd7a81bff728664c27bab679504780fcb91dd688` |
| [Request validation](../../../BATCH_ROUND10_STAGE4_PRIME_AUTHORIZATION_REQUEST_P30_P31_VALIDATION.json) | `52739c5ef1cb2a8142feadb73945fbcbe06a551f43d37fc2e0022b497c6a645c` |
| [Round-3 batch report](../../../BATCH_ROUND10_STAGE3_PRIME_ROUND3_REPORT.md) | `c122ca7f070a20568e47fab8999d6a3bf106b29da21f1dc8bca056b2c1ce5432` |
| [Round-3 batch receipt](../../../BATCH_ROUND10_STAGE3_PRIME_ROUND3_RECEIPT.json) | `ad20c4331936d2d8e1fb55613f72c3cf6bb5d07852775a47071ac427a9107172` |
| [Round-3 mandatory checkpoint](../../../BATCH_ROUND10_STAGE3_PRIME_ROUND3_MANDATORY_CHECKPOINT.md) | `dff758cae93c8fba9c17d9b26cbe6c07ae3584d7645aa0db357ab75a73fee94e` |

## Current Stage 4′ author-side revision outcome

**本轮结论概要。** 本轮 P30 已形成实质性的论文修订稿：5/5 剩余项由 14 个授权操作闭合，补入 54 条可回放检索、28 行 passage matrix 与两条 notes-only correction records；16 页预览干净构建。物理 roof、算子、determinant、误差界和 Route 结论仍未被虚构，下一步是 fresh Stage 4.5 审计。

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

## 结论概要

完整论文把物理 roof 行列式方案整理为六道型别化关卡，并冻结共同范数下的误差契约：四个数值通道加独立传播的几何／roof 输入不确定性。没有宣称已构造 roof、算子、行列式、包络、忠实度或非转移定理。

## Claim and route boundary

Explicit paper progress: All 5/5 residual items are addressed by 14 authorized operations. The final chain preserves 113/127 base blocks, records 54/54 successful dated metadata queries and a 28-row passage matrix, and appends two verified correction records only to the notes-side bibliography. The clean preview is 16 pages with zero blocking TeX findings or overfull boxes.

Frozen initial system: no-eclipse equilateral three-disk flow at d=6a; Euclidean free-flight clock; primitive cyclic collision-word owner; physical roof distinct from the unit-roof control.

Route mapping: A0_FAIL / A2_NOT_ELIGIBLE / NO_ROUTE_PROMOTION; formal tuple UNASSIGNED; positive arithmetic A2=0; A3=0; A4=0; Route B uninvoked. Across Papers 29--33, formal Route-A
tuples, positive arithmetic A2, A3, A4, and Route B remain `0/5`.

The next legal action is fresh Stage 4.5 audit of the current versioned Stage-4′ chain; no silent repair or promotion. Canonical manuscript,
bibliography, PDF, science/results, and the frozen system remain unchanged.
Stage 5/6, canonical promotion, submission, Route advancement, result refresh,
and new scientific execution remain unauthorized.
