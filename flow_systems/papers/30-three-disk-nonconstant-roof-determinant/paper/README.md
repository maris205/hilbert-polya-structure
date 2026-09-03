# P30 manuscript package

Package note: this directory is the immutable canonical Stage-2.5 manuscript
package; its Phase-0 wording below is historical. The authoritative current
state is [the paper README](../README.md) and [pipeline state](../notes/pipeline_state.md).
Control state: `stage3_prime_round1_aborted_awaiting_round2_authorization`.
**Stage 3′ Round 1 aborted fail-closed at `phase1_lint_failed`; no decision was
issued.** Recorded and audit-supported aggregates are both 4/5/0, while
`REV-EIC-W4` is false PARTIAL, `REV-R3-W1-DA-N1` is false FULL, and Phase 1 has
2 criterion-inheritance drift rows; the mechanical B4 direction was
suppressed. The semantic passes were fresh-context, role-separated, and
same-family; they were not independent error processes. Only a new user `确认`
may authorize fresh Round 2. Canonical manuscript/PDF/bibliography bytes remain
unchanged.

## Deliverables

- [`manuscript.tex`](manuscript.tex) -- complete English article with an independent Traditional-Chinese abstract.
- [`references.bib`](references.bib) -- 26 frozen, fully cited records in plainnat numeric style.
- [`paper.pdf`](paper.pdf) -- 14-page isolated LuaLaTeX/BibTeX build.
- [`stage2_manuscript_audit.md`](stage2_manuscript_audit.md) -- hash, structure, citation, boundary, and build audit.
- [`stage3_phase0_field_analysis.md`](../notes/stage3_phase0_field_analysis.md) -- current Stage-3 field analysis and reviewer cards.
- [`stage3_review_baseline.json`](../notes/stage3_review_baseline.json) -- immutable Stage-3 review target.

## 结论概要

完整论文把物理 roof 行列式方案整理为六道型别化关卡，并冻结共同范数下的误差契约：四个数值通道加独立传播的几何／roof 输入不确定性。没有宣称已构造 roof、算子、行列式、包络、忠实度或非转移定理。

## Claim and route boundary

The article turns the physical-roof determinant proposal into six typed gates and a common-norm uncertainty contract: four numerical channels plus separately propagated geometry/roof-input uncertainty. No roof, operator, determinant, enclosure, fidelity result, or nontransfer theorem is reported.

A0_FAIL / A2_NOT_ELIGIBLE / NO_ROUTE_PROMOTION; formal tuple UNASSIGNED; Route B closed. Stage-2.5 integrity passed; no later review stage changed a scientific result or Route coordinate. The only legal next action is a new user `确认` authorizing a new-id/new-manifest/fresh-context Stage 3′ Round 2.
