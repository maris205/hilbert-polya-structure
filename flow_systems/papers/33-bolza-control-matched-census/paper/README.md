# P33 manuscript package

Package note: this directory is the immutable canonical Stage-2.5 manuscript
package; its Phase-0 wording below is historical. The authoritative current
state is [the paper README](../README.md) and [pipeline state](../notes/pipeline_state.md):
**`stage3_prime_round2_aborted_awaiting_round3_authorization`.** Stage 3′ Round
2 failed closed at `phase2a_lint_failed`; no decision was signed or emitted,
and a fresh Round 3 requires explicit authorization. Canonical
manuscript/PDF/bibliography bytes remain unchanged.

## Deliverables

- [`manuscript.tex`](manuscript.tex) -- canonical article; SHA-256 `b407441c07091ad38fb7e918721d31d2c4e3d897db9a705d92d9ff1f231f96d3`.
- [`references.bib`](references.bib) -- 20 frozen, fully cited plainnat records; SHA-256 `12143967175abb0d325e16d156b1bc227e51f886009e7acd64691e84b92cb5e0`.
- [`paper.pdf`](paper.pdf) -- 14-page, 255325-byte isolated LuaLaTeX/BibTeX build; SHA-256 `487a8838d9d422e00dcf3e896c9231b96c58fedfc2cdeb2265045f8d11d70031`.
- [`stage2_manuscript_audit.md`](stage2_manuscript_audit.md) -- hash, structure, citation, boundary, and build audit.
- [`stage2_5_integrity_report.md`](../notes/stage2_5_integrity_report.md) and [`stage2_5_material_passport.json`](../notes/stage2_5_material_passport.json) -- final per-paper Stage-2.5 report and Schema-9 passport.
- [`stage3_phase0_field_analysis.md`](../notes/stage3_phase0_field_analysis.md) and [`stage3_review_baseline.json`](../notes/stage3_review_baseline.json) -- current Stage-3 Phase-0 configuration and immutable target.

## Historical Stage 3′ Round-1 outcome

Recorded and audited aggregates agree at 6 FULL / 7 PARTIAL / 0 NOT, with all
13 recorded verdicts supported. A dedicated manuscript/verdict/outcome-blind
criterion audit nevertheless confirms Phase-1 drift in `REV-P33-001`,
`REV-P33-003`, `REV-P33-004`, `REV-P33-006`, `REV-P33-007`, `REV-P33-009`, and
`REV-P33-012`. The mandatory gate therefore aborted with
`phase1_lint_failed`; B4 is only a suppressed mechanical candidate and no
decision exists. The fresh-context semantic checks were role-separated but
same-family and are not independent error processes.

| Artifact | SHA-256 |
|---|---|
| [`stage3_prime_round1_verification_report.md`](../notes/stage3_prime_round1_verification_report.md) | `b751ae39f142310e37c76bd80db1f11db6e5963c15f8e5a5cfdda47aa9659128` |
| [`stage3_prime_round1_checker_receipt.json`](../notes/stage3_prime_round1_checker_receipt.json) | `2cf5c82cdeebc5c0c2f93f5a138b39414a40161a968b9b7db666a5e8461458b4` |
| [`stage3_prime_round1_abort_record.json`](../notes/stage3_prime_round1_abort_record.json) | `765174c153843e14af50af25da8b10a1bdd3839618aa1f30a14a3894fa00725b` |

## Current Stage 3′ Round-2 controlling outcome

The committed 6 FULL / 7 PARTIAL / 0 other record is controlled as 5 FULL / 8
PARTIAL / 0 other because `REV-P33-011` is a false FULL. The no-retry semantic
gate therefore aborted before the response letter, Phase 2B, traceability,
official checker, or decision.

| Artifact | SHA-256 |
|---|---|
| [`stage3_prime_round2_verification_report.md`](../notes/stage3_prime_round2_verification_report.md) | `a0086ede828d0d16ec345ffe0d87869076f724752071d3493c4a435a5d0bf3c6` |
| [`stage3_prime_round2_checker_receipt.json`](../notes/stage3_prime_round2_checker_receipt.json) | `dbf9cdb7e1a8ba42ab671ec9e03d600e90b78abefc7c395504381d6909ecd480` |
| [`stage3_prime_round2_abort_record.json`](../notes/stage3_prime_round2_abort_record.json) | `b6b449b3899b7b3a35957474d5951af12cefdb3723acc2e9c435c1ea61b020df` |

## Stage 2.5 integrity result

- Phase A: 20/20 references checked; 19 `VERIFIED` and one bounded `PLAUSIBLE`; no unresolved finding.
- Phase B: 18/48 citation contexts sampled and 18/18 supported within their stated boundaries.
- Phase C: 43/43 registered quantitative/data surfaces verified; 2/2 figure/table traces closed; scholar declaration `no_experiments_declared`; `experiment_provenance=[]`.
- Phase D: 21/68 body paragraphs checked across 10/10 major sections; verdicts are 19 `ORIGINAL` and 2 bounded `PARAPHRASE`.
- Phase E: 126 registered claims, 74 selected claims, and 108/108 evidence tuples; 74/74 selected claims are `VERIFIED`, with zero minor/major/unverifiable verdicts. All 108 tuples remain anchorless.
- Seven-mode audit: 7/7 `CLEAR`, 0 `SUSPECTED`, 0 `INSUFFICIENT EVIDENCE`.
- Official E6: `skipped_no_revision_evidence`, `revision_evidence_bundle_sha256=null`, and no drift finding.

## 结论概要

本轮形成的明确论文进展是：把两个曲面的异构精确证明产生器约束到同一语义 owner-certificate schema，并要求独立验证器复验；同时把固定、target-blind 截断造成的 target-empty/control-nontrivial 不对称及 systole 混杂显式化。P33-RC-1 仍为 0/7，没有执行 owner census；进展属于可验证的方法与证书设计，而不是已经得到的计数或算术对比结果。

## Citation and claim boundary

P33-S06 remains bounded `PLAUSIBLE`, page-unpinned, and background-/context-only. Its carriers remain `anchor:none`, and claim-to-passage faithfulness remains `INCONCLUSIVE`; it is not used to assert an exact Bolza systole theorem, formula, or replay inequality.

## Route position and next gate

Route A remains at A1 preparation only: P33 formal A0 is prohibited/confounded, the formal tuple is `UNASSIGNED`, positive arithmetic A2 is absent, A3/A4 were not run, and Route B is closed with zero invocation. Stage 3′ cannot create Route credit, and no later review stage changed the frozen system or scientific result. The only next legal action is explicit authorization for a new-id/new-manifest/fresh-context Stage 3′ Round 3.

## Batch traceability

| Artifact | SHA-256 |
|---|---|
| [`BATCH_ROUND10_STAGE2_5_INTEGRITY_REPORT.md`](../../../BATCH_ROUND10_STAGE2_5_INTEGRITY_REPORT.md) | `ce99860d6fe60de840c9802757686d4818a1d735dd2b03cf5f11976b1b9d2106` |
| [`BATCH_ROUND10_STAGE2_5_MANDATORY_CHECKPOINT.json`](../../../BATCH_ROUND10_STAGE2_5_MANDATORY_CHECKPOINT.json) | `8d9ecc4d4ccba99762db1656e9055b2e236f0b352c19a144eed32e6df0aa38b8` |
| [`BATCH_ROUND10_STAGE2_5_POST_REPAIR_INPUT_FREEZE.json`](../../../BATCH_ROUND10_STAGE2_5_POST_REPAIR_INPUT_FREEZE.json) | `54bd577683595dd9259ba2a97405b7257a269bf740ffcaa1c0135718869e5041` |
| [`BATCH_ROUND10_STAGE2_5_CORRECTION_AUTHORIZATION_RECEIPT.json`](../../../BATCH_ROUND10_STAGE2_5_CORRECTION_AUTHORIZATION_RECEIPT.json) | `14c846c4b32dc77e7735fc645c7afe359c91109cc4c5c6c60554882317c1cf3b` |
| [`BATCH_ROUND10_STAGE2_5_VALIDATION_RECEIPT.json`](../../../BATCH_ROUND10_STAGE2_5_VALIDATION_RECEIPT.json) | `946973cc01c273cb38d88efdfbb4693e709b9aa08e6fb769e649c2c408393c7b` |
