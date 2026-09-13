---
title: "Session 4：Symbolic Dynamics"
direction: symbolic_dynamics
session_theme: "符号骨架 vs 几何实现"
status: "P211–P215 EXACT_FIVE_INTERNAL_COMPLETE / HOLD_EXTERNAL"
authoritative_checkpoint: "2026-09-11 UTC"
---

# Session 4：Symbolic Dynamics

[P1 Wiki 首页](../../README.md) · [结论](conclusions.md) · [路线图](roadmap.md) · [来源与证据](sources.md)

> **当前结论。** P211–P215 是一个已完成的五篇“有限自治确定性系统”内部批次，状态为 `EXACT_FIVE_INTERNAL_COMPLETE / HOLD_EXTERNAL`。这不等于原始 Hilbert–Pólya 算术路线的 A0–A4 有自动进展，也不构成 Route B、Riemann 零点、RH 或全局新颖性结论。

## 这个方向研究什么

Session 4 的原始问题是：符号动力学能提供 Riemann/Hilbert–Pólya 动力学模型的哪些**算术骨架**，又有哪些结构必须由几何动力系统承担？因此其主题不是泛化的 RH 搜索，而是“**符号结构 vs 几何实现**”。

原始方案限定主对象为 symbolic dynamical systems；若想法需要转到 Hénon、辛映射、Hamiltonian flow、量子图或无关算子模型，只能作为 `ROUND2_CLUE` 记录，不能在本 Session 内另开主线。详见[原始方案](../../../symbolic_dynamics/propose-symbolic-dynamics.md)与[路线图](roadmap.md)。

## 当前恢复入口

建议下一位 agent 按下列顺序阅读：

1. [本页](index.md)：识别 Session 范围及当前批次边界。
2. [结论](conclusions.md)：读取 P211–P215 的紧凑结果与非主张。
3. [路线图](roadmap.md)：区分原始 Symbolic / Route A–B 设计与后来的内部批次流程。
4. [来源与证据](sources.md)：回到权威原件；Wiki 是导航层，不替代证明、审稿、运行记录或 Git 对象。

流级的最新恢复记录是[当前研究状态](../../../symbolic_dynamics/SYMBOLIC_DYNAMICS_STATE.md)，批次级终态以[P211–P215 final QA](../../../symbolic_dynamics/docs/papers211_215_sequence/FINAL_QA_REPORT.md)为准。部分单篇 README 保存了当时的阶段性 pending 文案；不得用它们覆盖后来已验收的终态记录。

## P211–P215：本轮五个有限系统

| 论文 | 研究对象／保留的窄结论 | 入口 |
|---|---|---|
| P211 | 非降自映射上的 kernel–image projection feedback：终态投影、逐点 sharp clock 与每个标记目标的一步前驱分解。 | [包说明](../../../symbolic_dynamics/papers/211-kernel-image-projection-feedback/README.md) |
| P212 | 封闭 pointer reversal：完整 carrier 的精确周期分类，以及带标号 orbit census。 | [包说明](../../../symbolic_dynamics/papers/212-closed-pointer-orbits/README.md) |
| P213 | receiver-limited cyclic transfer：终态与 sharp fixation clock、所有 target 的 comparison-word inverse 与 fibre 计数。 | [包说明](../../../symbolic_dynamics/papers/213-receiver-limited-cyclic-transfer/README.md) |
| P214 | 幂零理想上的双线性映射：cancellation-safe clock、深度分布与一步 target fibre。 | [包说明](../../../symbolic_dynamics/papers/214-nilpotent-bilinear-clock/README.md) |
| P215 | iterated prefix drawdown：sign-run clock、唯一 recurrent zero 与 inverse-fibre 重建。 | [包说明](../../../symbolic_dynamics/papers/215-prefix-drawdown-clock/README.md) |

它们的共同合同不是“凑足五个编号”，而是：对每个被保留系统，先给出明确的 literal autonomous update，再给出 all-parameter temporal/recurrent 定理，另给 inverse、fibre、enumeration 或 extremal 定理；已知机制、共轭、factor、参数限制和弱候选必须扣除。有限 CPU 运行只为证明施压，不能代替全参数证明。见[问题锚点](../../../symbolic_dynamics/docs/papers211_215_sequence/PROBLEM_ANCHOR.md)。

## 状态与边界

- **内部批次完成：** P211–P215 恰好五篇均完成 author、Review A、Review B 的证据链、Round0/1/2、两次 terminal source-only build、实际末页查看和单篇 final QA；batch exact-five gate 与随后限定私有 Git 同步均已记录为完成，批次现已暂停。
- **外部仍暂停：** `OWNER_AMBER / HOLD_EXTERNAL`；不授权公开发布、上传、投稿或专家联系。
- **Route 层不自动推进：** 当前短论文子轨虽然仍位于 `Route A / Symbolic Dynamics` 的大框架内，但 paper Stage/Round 不是 A0–A4；没有进入 Route B。
- **不从 QA 推出数学全称结论：** “零 current finding”是已记录评审 finding 的状态，不是对所有数学、环境或未来反例的保证；有限验证也不证明 all-parameter theorem。

详细的可用结论和限制见[结论](conclusions.md)；原始路线、门槛和未来可复用的停止规则见[路线图](roadmap.md)。
