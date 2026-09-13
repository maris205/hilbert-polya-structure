---
title: "Symbolic Dynamics：P211–P215 结论与边界"
direction: symbolic_dynamics
status: "EXACT_FIVE_INTERNAL_COMPLETE / HOLD_EXTERNAL"
authoritative_checkpoint: "2026-09-11 UTC"
---

# Symbolic Dynamics：结论与边界

[P1 Wiki 首页](../../README.md) · [方向索引](index.md) · [路线图](roadmap.md) · [来源与证据](sources.md)

## 批次层结论

[终验报告](../../../symbolic_dynamics/docs/papers211_215_sequence/FINAL_QA_REPORT.md)记录：P211–P215 **恰好五篇**内部完成。每篇均有 author、Review A、Review B 的接受/replay 证据，物理 Round0/1/2，两次 terminal source-only build，实际最终页查看以及零 current Critical/Major/Minor findings 的单篇 final QA。

整批 exact-five gate 接受了 15 组 replay pair、15 份 Round manifest、10 次 terminal build；保留的失败、HOLD 和淘汰证据没有被删除。这个结果说明该有限系统批次的内部证据与制品门已闭合，**不**说明原始 HP A0–A4 已通过，亦不说明一个全局新颖性、算子、迹公式、零点对应或 RH 命题。

## 五篇论文的保留结论

下表是导航摘要，不是证明替代物；准确假设、证明和证据边界应回到对应 manuscript/package 与 final-QA 原件。

| 论文 | 保留的定理性内容 | 明确不主张／限制 |
|---|---|---|
| [P211](../../../symbolic_dynamics/papers/211-kernel-image-projection-feedback/FINAL_QA_REPORT.md) | 对有限链非降自映射的重算 kernel–image feedback，给出 exact terminal projection、每个状态的 entrance time（全 carrier 的最大值为 `ceil(n/2)`，`n≥2`），以及标记 target 的完整一步前驱和 Laurent 系数 fibre 公式。 | 限于此重算动力学和 target-specific factorization；不主张 global fibre maximum、maximizer、basin 或 all-time inverse atlas。 |
| [P212](../../../symbolic_dynamics/docs/papers211_215_sequence/P212_FINAL_QA.md) | 对 closed pointer reversal 的完整有限 carrier，给出精确 return-period 分类、可达 period 集和含根树/primitive necklace 的有理标号 census。 | 有限 verifier 为 deductive theorem 提供压力而非证明；不主张全局新颖性、无 factor 定理或超出闭合 carrier 的结果。 |
| [P213](../../../symbolic_dynamics/docs/papers211_215_sequence/P213_FINAL_QA.md) | 对 cyclic nonnegative transfer rule，给出 terminal state、sharp worst fixation clock、all-target comparison-word inverse、fibre counts、fixed-target product 及 fixed-`n` largest-fibre growth exponent `floor(n/3)`。 | 不主张 exact finite-`N` maximum/全部 maximizer、general pointwise clock、full basin census 或 arbitrary-encoding nonconjugacy。 |
| [P214](../../../symbolic_dynamics/docs/papers211_215_sequence/P214_FINAL_QA.md) | 对 `F(x,y)=(y,x(t+y))`（幂零理想上），给出 cancellation-safe pointwise clock、唯一 recurrent zero、sharp maximum depth、深度 census 和 complete one-step target-fibre formula/distribution。 | 已扣除乘法与线性 control 机制；`m=2` 是边界；不主张 arbitrary chain-ring extension、all-time inverse、功能图分类或 global priority。 |
| [P215](../../../symbolic_dynamics/docs/papers211_215_sequence/P215_FINAL_QA.md) | 对 iterated prefix drawdown，给出 sign-run exact clock、唯一 recurrent zero、sharp height、每个 inverse fibre 的 record-height 重建、递推、image size 和 unique maximum fibre。 | 经典 one-step drawdown/barrier enumeration 仅作背景；不主张 arbitrary-poset extension、all-time inverse atlas、随机版本或 universal no-factor theorem。 |

## 正确的状态读法

| 层次 | 可以说什么 | 不可以据此说什么 |
|---|---|---|
| 单篇定理 | 在各 manuscript 假设下，保留表中明确列出的窄定理。 | 有限枚举本身证明了所有参数范围。 |
| 单篇 QA | 对记录的 author/A/B、round、build、view、artifact 门已完成内部验收。 | 不存在任何数学错误、环境风险或未知反例。 |
| 五篇批次 | `EXACT_FIVE_INTERNAL_COMPLETE`，且失败/HOLD 记录被保留。 | 自动晋级原始 HP A0–A4、Route B 或外部发表。 |
| Session 4 | 形成有限自治系统的可复用局部结果与 evidence pattern。 | 已完成“symbolic skeleton → geometric carrier → operator realization”的整条计划。 |

## 可交接给下一阶段的东西

- 五个有明确 carrier、literal update、时钟／recurrent 描述和 inverse/fibre/计数轴的有限系统案例。
- “先扣除已知机制，再评估新贡献”的批次合同，以及 author/A/B、physical rounds、terminal build、page-view、artifact gate 的可追溯审计结构。
- 原始 Session 的问题框架：若符号对象要通向更强的动力学/算子计划，需明确它究竟仍缺 primitive-orbit、自然 zeta/determinant、全局解析结构或几何/算子 lift 的哪一部分。

没有被交接的是 Route A 的新 gate credit、Route B 资格、Hilbert–Pólya 证明成分或外部发布许可。若未来获授权重开，应先依[路线图](roadmap.md)判断新系统与缺失条件，而非把 P211–P215 的内部完成当作自动晋级。
