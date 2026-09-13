---
title: "Symbolic Dynamics：路线图与批次流程"
direction: symbolic_dynamics
session_theme: "Arithmetic skeleton vs geometric realization"
---

# Symbolic Dynamics：路线图与批次流程

[P1 Wiki 首页](../../README.md) · [方向索引](index.md) · [结论](conclusions.md) · [来源与证据](sources.md)

## 两层路线，不能混写

本方向有两个不同层次的“路线图”。

1. **Session 4 的研究设计：** 在 symbolic dynamics 内测试算术骨架能够走多远，并明确记录必须由几何实现承担的缺口。
2. **P211–P215 的内部批次流程：** 对五个有限自治确定性映射完成论文、审稿、重放、冻结、构建与制品验收。

第二层已经完成，但它不是第一层中 Hilbert–Pólya Route A A0–A4 的替代，也没有启动 Route B。

## A. Session 4 的概念路线

原始设计的中心问题是“符号结构能否自然给出算术骨架，以及何时必须转向几何载体”。建议的探索梯子如下：

| 阶段 | 做什么 | 合格输出／停止纪律 |
|---|---|---|
| S1：有限符号系统 | SFT、sofic shift、有限邻接 grammar 的精确 zeta/determinant 与解析限制。 | 不可能性定理也是成功产物。 |
| S2：可数符号系统 | countable Markov shift、renewal、coded system 等；检查 logarithmic roof、divisor counting、非有理 determinant 与内生算术结构。 | 复杂度增加不自动等于自然性或算术性。 |
| S3：带符号／复结构 | 仅研究系统内生的 orientation、有限群 cocycle、unitary representation、phase 或 holonomy。 | 不得按 Riemann-zero target 人为挑选相位。 |
| S4：几何兼容性审计 | 对最强的 surviving symbolic object，说明需要什么 Markov coding、return grammar、closed orbit、roof/action 或 phase 几何来源。 | 本 Session 只写缺失义务／`ROUND2_CLUE`，不离开符号族去建几何系统。 |

这些阶段来自[原始方案的 S1–S4](../../../symbolic_dynamics/propose-symbolic-dynamics.md)。原方案同时规定：需要 Hénon、辛、Hamiltonian、quantum graph 或无关算子构造的分支，应记录为 `ROUND2_CLUE` 后停止；不能借本方向偷偷扩张为另一个系统族。

## B. Route A / Route B 的正确位置

原始方案把 Route A 用于判断候选是否具备：

```text
可信的算术起源
  → primitive-orbit / repetition 结构
  → 自然的 dynamical zeta 或 Fredholm determinant
  → 全局解析结构
  → 可能的 geometric / operator lift
```

Route B 只留给已经足够强、明确准备进入 operator-level analysis 的候选；它不能用来“救活”一个弱的 Symbolic fit。更具体的门定义应以相应 evaluator 与原始研究记录为准，不能由本 Wiki 重新发明。

因此，P211–P215 的 `Stage`、`Round`、build 或 QA 标记不能被读成 A0–A4 通过。流级状态也明确：当前是 `Route A / Symbolic Dynamics` 下的有限自治确定性系统子轨，**没有进入 Route B**。

## C. P211–P215 批次合同与已完成流程

本轮的问题不是“找五篇论文”，而是寻找五个超出已知 rejected/reserved surface 的有限 autonomous deterministic maps。每一保留项需要：

```text
明确 carrier + literal autonomous update
  → all-parameter temporal / recurrent theorem
  → 独立的 inverse / fibre / enumeration / extremal theorem
  → 扣除旧 map、共轭、factor、参数限制与旧证明机制
  → author + 两个不同非作者 Review A/B 的证据链
  → physical Round0 / Round1 / Round2
  → 两次 source-only terminal build + 实际全页查看 + artifact check
  → exact-five batch terminal gate
```

有限 CPU 只帮助发现边界、检验实现和给出 proof pressure；不能代替全参数定理。弱、重复或有未解决 finding 的候选必须替换，不可以为了五席配额而保留。完整合同见[问题锚点](../../../symbolic_dynamics/docs/papers211_215_sequence/PROBLEM_ANCHOR.md)。

2026-09-11 的[终验报告](../../../symbolic_dynamics/docs/papers211_215_sequence/FINAL_QA_REPORT.md)确认该流程已对 P211–P215 闭合，并把 scoped private Git synchronization 列为最后的操作性 closeout；随后[当前研究状态](../../../symbolic_dynamics/SYMBOLIC_DYNAMICS_STATE.md)记录该限定同步已接受、批次已暂停。外部行动始终仍为 `HOLD_EXTERNAL`。

## 下一阶段如何使用这张图

在有新的明确授权前，本页是知识导航，不是启动新实验或新批次的许可。若重开研究，建议先按顺序固定：

1. 系统对象、carrier 和 literal update；
2. grammar、roof/potential、cocycle（如有）、function space 与 determinant convention；
3. 旧机制／共轭／factor／参数约束的扣除；
4. 它相对 Route A 缺的是哪一项，而非仅有何种数值相似；
5. 若必须依赖几何，写清楚 `ROUND2_CLUE` 与需补的几何义务。

本方向最有价值的输出也可以是严格反证或精确接口描述，而非一条被过度解释的“正向路线”。与当前已闭合批次的结论对应，见[结论](conclusions.md)。
