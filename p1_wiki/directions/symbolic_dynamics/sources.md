---
title: "Symbolic Dynamics：来源、权威顺序与复现入口"
direction: symbolic_dynamics
wiki_role: "navigation-only"
---

# Symbolic Dynamics：来源、权威顺序与复现入口

[P1 Wiki 首页](../../README.md) · [方向索引](index.md) · [结论](conclusions.md) · [路线图](roadmap.md)

## 这页的用途

本页只建立来源地图。Wiki 的摘要、链接与状态文字不替代原始证明、review、运行输出、冻结清单、Git 对象或 PDF/TeX 制品。发生冲突时，应按下列优先级回到原件。

## 权威顺序

1. **当前批次终态：** [P211–P215 final QA](../../../symbolic_dynamics/docs/papers211_215_sequence/FINAL_QA_REPORT.md)与[流级当前研究状态](../../../symbolic_dynamics/SYMBOLIC_DYNAMICS_STATE.md)的最新段。
2. **批次合同与过程状态：** [PROBLEM_ANCHOR.md](../../../symbolic_dynamics/docs/papers211_215_sequence/PROBLEM_ANCHOR.md)和[PIPELINE_STATE.md](../../../symbolic_dynamics/docs/papers211_215_sequence/PIPELINE_STATE.md)。
3. **单篇结果与验证边界：** 各 P211–P215 paper package、其 `main.tex`、`PROOF_PACKAGE.md`、`CLAIMS_EVIDENCE.md`、单篇 final QA 和被链接的 receipt。
4. **Session 设计与历史导航：** [propose-symbolic-dynamics.md](../../../symbolic_dynamics/propose-symbolic-dynamics.md)和[方向 README](../../../symbolic_dynamics/README.md)。其中阶段性文本应按其日期阅读，不能反向覆盖上层终态。

`SYMBOLIC_DYNAMICS_STATE.md` 也明确保留历史 pending 语境。使用它时，应优先读文件开头的最新状态及其指定的当前入口，而不要把旧条目的当时语气当作现时阻碍。

## 核心源文件

| 用途 | 权威来源 | 本 Wiki 的对应页 |
|---|---|---|
| Session 身份、Symbolic vs Geometry、S1–S4、Route A/B 位置 | [propose-symbolic-dynamics.md](../../../symbolic_dynamics/propose-symbolic-dynamics.md) | [路线图](roadmap.md) |
| 当前流状态、P211–P215 已完成和 Route 边界 | [SYMBOLIC_DYNAMICS_STATE.md](../../../symbolic_dynamics/SYMBOLIC_DYNAMICS_STATE.md) | [方向索引](index.md)、[结论](conclusions.md) |
| 流级项目入口与历史论文导航 | [README.md](../../../symbolic_dynamics/README.md) | [方向索引](index.md) |
| 五席的科学／证据合同和外部 hold | [PROBLEM_ANCHOR.md](../../../symbolic_dynamics/docs/papers211_215_sequence/PROBLEM_ANCHOR.md) | [路线图](roadmap.md) |
| `EXACT_FIVE_INTERNAL_COMPLETE` 终态 | [FINAL_QA_REPORT.md](../../../symbolic_dynamics/docs/papers211_215_sequence/FINAL_QA_REPORT.md) | [结论](conclusions.md) |

## P211–P215 原件入口

| 论文 | Canonical manuscript | 包级说明／证据入口 | 单篇终验入口 |
|---|---|---|---|
| P211 | [main.tex](../../../symbolic_dynamics/papers/211-kernel-image-projection-feedback/main.tex) | [README.md](../../../symbolic_dynamics/papers/211-kernel-image-projection-feedback/README.md) | [FINAL_QA_REPORT.md](../../../symbolic_dynamics/papers/211-kernel-image-projection-feedback/FINAL_QA_REPORT.md) |
| P212 | [main.tex](../../../symbolic_dynamics/papers/212-closed-pointer-orbits/main.tex) | [README.md](../../../symbolic_dynamics/papers/212-closed-pointer-orbits/README.md) | [P212_FINAL_QA.md](../../../symbolic_dynamics/docs/papers211_215_sequence/P212_FINAL_QA.md) |
| P213 | [main.tex](../../../symbolic_dynamics/papers/213-receiver-limited-cyclic-transfer/main.tex) | [README.md](../../../symbolic_dynamics/papers/213-receiver-limited-cyclic-transfer/README.md) | [P213_FINAL_QA.md](../../../symbolic_dynamics/docs/papers211_215_sequence/P213_FINAL_QA.md) |
| P214 | [main.tex](../../../symbolic_dynamics/papers/214-nilpotent-bilinear-clock/main.tex) | [README.md](../../../symbolic_dynamics/papers/214-nilpotent-bilinear-clock/README.md) | [P214_FINAL_QA.md](../../../symbolic_dynamics/docs/papers211_215_sequence/P214_FINAL_QA.md) |
| P215 | [main.tex](../../../symbolic_dynamics/papers/215-prefix-drawdown-clock/main.tex) | [README.md](../../../symbolic_dynamics/papers/215-prefix-drawdown-clock/README.md) | [P215_FINAL_QA.md](../../../symbolic_dynamics/docs/papers211_215_sequence/P215_FINAL_QA.md) |

对数学内容，优先阅读 `main.tex`、各 paper package 中声明的 proof/claim documents 和相应终验；对“是否完成”“有哪些 preserved failure”“是否可对外行动”，优先阅读 final QA、pipeline state 和当前流状态。不要把 README 中的 source-preparation 或旧 lifecycle 文字误认为当前全局状态。

## 复现和证据解释边界

- 每个 paper package 是可分享／复现的完整单位；其 TeX、验证器、参数、输出、评审与 QA 文件分工不同，不能只凭一个 README 或 PDF 推断全部证据。
- 终验报告保留 246 份 failed/HOLD/rejected 文件。保留失败是证据完整性要求，不是后来成功把历史失败“抹掉”。
- `HOLD_EXTERNAL` 是行动边界：它不等于“数学必错”，也不把内部验收升级为公开发表、专家认可或 Route gate credit。
- 有限计算与成功构建分别检验有限语义／制品流程；它们不能单独证明无限、全参数或 Hilbert–Pólya 结论。

若要给后续 agent 增加 paper-level Markdown 全文或知识卡，应把它们标为从此表所列 canonical source 派生的导航副本，并保留相对源路径、来源状态和非主张；不得以转换件取代原始包。
