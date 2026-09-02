# P32 manuscript package

Current state: **ARS STAGE 2.5 INTEGRITY PASS / MANDATORY STOP BEFORE STAGE 3**.
The checkpoint records `mandatory_stop=true`, `scholar_confirmation_required=true`,
and `stage3_authorized=false`; no Stage-3 review has been dispatched.

## Deliverables

- [`manuscript.tex`](manuscript.tex) -- canonical article; SHA-256 `4a3e1f084dc1e27005479971299fd9da67bb6c817278d5de0de6cf03cbc8000a`.
- [`references.bib`](references.bib) -- 26 frozen, fully cited plainnat records; SHA-256 `e699c96196377892d3aa1f280e6a5117001c3cec37a511a3d1c08fdc52127de9`.
- [`paper.pdf`](paper.pdf) -- 13-page, 254332-byte isolated LuaLaTeX/BibTeX build; SHA-256 `66948e247c72a3388a7f3da1f80be1d74860afa1261c99fb18c85e2b8bb84f93`.
- [`stage2_manuscript_audit.md`](stage2_manuscript_audit.md) -- hash, structure, citation, boundary, and build audit.
- [`stage2_5_integrity_report.md`](../notes/stage2_5_integrity_report.md) and [`stage2_5_material_passport.json`](../notes/stage2_5_material_passport.json) -- final per-paper Stage-2.5 report and Schema-9 passport.

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

Route A remains at the A0/A1 foundation/interface position only: P32 A0 is unavailable, the formal tuple is `UNASSIGNED`, positive arithmetic A2 is absent, A3/A4 were not run, and Route B is closed with zero invocation. Stage 2.5 authorizes no scientific execution, canonical-result refresh, Route promotion, or Stage 3. The next legal transition is an explicit scholar confirmation for Stage-3 independent review.

## Batch traceability

| Artifact | SHA-256 |
|---|---|
| [`BATCH_ROUND10_STAGE2_5_INTEGRITY_REPORT.md`](../../../BATCH_ROUND10_STAGE2_5_INTEGRITY_REPORT.md) | `ce99860d6fe60de840c9802757686d4818a1d735dd2b03cf5f11976b1b9d2106` |
| [`BATCH_ROUND10_STAGE2_5_MANDATORY_CHECKPOINT.json`](../../../BATCH_ROUND10_STAGE2_5_MANDATORY_CHECKPOINT.json) | `8d9ecc4d4ccba99762db1656e9055b2e236f0b352c19a144eed32e6df0aa38b8` |
| [`BATCH_ROUND10_STAGE2_5_POST_REPAIR_INPUT_FREEZE.json`](../../../BATCH_ROUND10_STAGE2_5_POST_REPAIR_INPUT_FREEZE.json) | `54bd577683595dd9259ba2a97405b7257a269bf740ffcaa1c0135718869e5041` |
| [`BATCH_ROUND10_STAGE2_5_CORRECTION_AUTHORIZATION_RECEIPT.json`](../../../BATCH_ROUND10_STAGE2_5_CORRECTION_AUTHORIZATION_RECEIPT.json) | `14c846c4b32dc77e7735fc645c7afe359c91109cc4c5c6c60554882317c1cf3b` |
| [`BATCH_ROUND10_STAGE2_5_VALIDATION_RECEIPT.json`](../../../BATCH_ROUND10_STAGE2_5_VALIDATION_RECEIPT.json) | `946973cc01c273cb38d88efdfbb4693e709b9aa08e6fb769e649c2c408393c7b` |
