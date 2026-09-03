# P31 manuscript package

Package note: this directory is the immutable canonical Stage-2.5 manuscript
package; its Phase-0 wording below is historical. The authoritative current
state is [the paper README](../README.md) and [pipeline state](../notes/pipeline_state.md).
Control state: `stage3_prime_round1_aborted_awaiting_round2_authorization`.
**Stage 3′ Round 1 aborted fail-closed at `phase1_lint_failed`; no decision was
issued.** Recorded 4/6/1 became audit-supported 3/7/1 because `REV-P31-009` is
false FULL; Phase-1 criterion inheritance drifted at `REV-P31-005` and
`REV-P31-009`; the mechanical B3 direction was suppressed. The semantic passes
were fresh-context, role-separated, and same-family; they were not independent
error processes. Only a new user `确认` may authorize fresh Round 2. Canonical
manuscript/PDF/bibliography bytes remain unchanged.

## Deliverables

- [`manuscript.tex`](manuscript.tex) -- complete English article with an independent Traditional-Chinese abstract.
- [`references.bib`](references.bib) -- 22 frozen, fully cited records in plainnat numeric style.
- [`paper.pdf`](paper.pdf) -- 12-page isolated LuaLaTeX/BibTeX build.
- [`stage2_manuscript_audit.md`](stage2_manuscript_audit.md) -- hash, structure, citation, boundary, and build audit.
- [`stage3_phase0_field_analysis.md`](../notes/stage3_phase0_field_analysis.md) -- current Stage-3 field analysis and reviewer cards.
- [`stage3_review_baseline.json`](../notes/stage3_review_baseline.json) -- immutable Stage-3 review target.

## 结论概要

完整论文把确定性 canonicalization 双条件提升为首要证书目标，将 9,453 个 pair rows 降为派生的对抗审计，并保持全局 owners G、incidences I 与 cell-local quotient C 三种估计量互不替代。

## Claim and route boundary

The article makes a deterministic canonicalization biconditional the primary certificate target. The 9,453 pair rows become a derived adversarial audit, while global owners G, incidences I, and cell-local quotient C remain distinct prospective estimands.

Route A / A1 preparation; formal tuple UNASSIGNED; positive arithmetic A2 absent; Route B closed. Stage-2.5 integrity passed; no later review stage changed a scientific result or Route coordinate. The only legal next action is a new user `确认` authorizing a new-id/new-manifest/fresh-context Stage 3′ Round 2.
