# Flow Systems（Session 5）：经典 vs 量子

[P1 Wiki](../../README.md) · [本方向目录](index.md) · [结论边界](conclusions.md) · [路线图](roadmap.md) · [五种连续时间子型](p24-p28-five-planned-forms.md) · [来源与原件](sources.md)

## 这一方向在问什么

Flow Systems 研究连续时间动力系统能否提供 Hilbert–Pólya 候选所需的自然链条：

```text
连续时间流 → 本原闭轨 / 周期 / action / 相位
            → 动力 Zeta 或 trace
            → 自然量子（或半经典）对象
            → 固定算子的谱问题
```

本 Session 的比较轴是“**经典流 vs 量子谱实现**”。它不是已经完成的
Hilbert–Pólya 构造；它记录哪些机制、障碍、对照和所有权问题已经得到局部而可追溯的结果。

## 快速入口

| 想知道什么 | 先读 |
| --- | --- |
| 已有定理、负结果、对照结果，以及没有得到什么 | [结论边界](conclusions.md) |
| Route A / Route B 在这里如何使用；原始六阶段设计是什么 | [路线图](roadmap.md) |
| P24–P28 的五个冻结子型、初始假设、杀伤门和终态 | [五种连续时间子型](p24-p28-five-planned-forms.md) |
| 原论文、项目 README、批次报告、收据和判据文件 | [来源与原件](sources.md) |

## 当前状态：先分清三种“完成”

| 层次 | 当前可安全表述的状态 | 不能据此推出 |
| --- | --- | --- |
| 早期 Flow 论文（P1–P9、P22） | 留下多项局部定理、拓扑/谱障碍、正控和所有权分离结果 | 一个统一的 Hilbert–Pólya 候选已经成立 |
| P24–P28 的科学路线 | 五个连续时间子型保留在 Route A 的早期证据/对照层；正向算术 A2 为 `0/5`，Route B 调用为 `0/5` | Route A 的正向晋级、固定算子的全局算术 trace，或 RH 证明 |
| P24–P28 的交付流水线 | Stage 5 已完成；用户明确跳过可选 Stage 6，因此五条 pipeline 都记为 `completed` | 数学正确性、投稿就绪、外部认可或路线图晋级 |

“Stage 5 完成”在这里是冻结论文、可复现构建、内容身份和包审计的状态；不是新的科学计算，更不是 Route 坐标。Stage 6 被跳过，也不生成 Process Record。细节见 [结论边界](conclusions.md#流程终态不等于科学路线终态) 与 [终态收据](../../../flow_systems/BATCH_ROUND9_STAGE6_SKIP_RECEIPT.json)。

## 推荐的知识库阅读顺序

1. 从 [路线图](roadmap.md) 了解连续时间、内生算术性、闭轨、Zeta、trace 与量子化之间的约束链。
2. 从 [结论边界](conclusions.md) 区分“确切的局部结论”“负迁移/反例”“尚未建立的桥”。
3. 需要继续某一机制时，进入 [五种连续时间子型](p24-p28-five-planned-forms.md)，再打开对应的原项目与最终论文。
4. 做任何 Route 判断前，以 [来源与原件](sources.md) 指向的正式判据和项目级记录为准；本 wiki 只是导航与范围说明。

## 五种连续时间子型（P24–P28）

| Paper | 冻结对象 | 在五种形式中的作用 |
| --- | --- | --- |
| P24 | 有 cusp 的 Bianchi 双曲三维流与复 holonomy | 算术/几何所有权与描述符特异性压力测试 |
| P25 | 开放三圆盘散射/双曲台球流 | 非算术负校准：物理 roof 与 unit-roof 符号对象不可转移 |
| P26 | Level-11 新形式驱动的正时间变换测地流 | 时间重参数化是否保留 Hecke/Euler 所有权的对照 |
| P27 | 同余逆极限测地层状空间 | 极限流闭轨不存在时，有限层统计不得冒充极限流 Zeta |
| P28 | Bolza 曲面的磁 Hamiltonian/contact 流与 tensor-power 量子族 | flux、相位、半经典算子族与固定算子所有权分离 |

这些不是同一系统的五组参数扫描；它们刻意改变时间的拥有者、轨道相位、紧致性、解析对象和可证伪机制。详见 [五种连续时间子型](p24-p28-five-planned-forms.md)。

## 与其余五个方向的连接

自由探索的起点见 [zeta_mvp0](../zeta_mvp0/index.md)。后续五个路线图方向为：[Logistic Dynamics](../logistic_dynamics/index.md)、[Hénon Dynamics](../henon_dynamics/index.md)、[Symplectic Map](../symplectic_map/index.md)、[Symbolic Dynamics](../symbolic_dynamics/index.md) 与本页的 Flow Systems。跨方向的相似语言不自动传递 Route credit；每个方向都必须在自己的对象、时钟、所有权和证据边界内重新建立结论。

## 使用边界

- 不以黎曼零点表定义、筛选、调参或截断候选；不手工塞入 `log p` 周期或 von Mangoldt 权重。
- 数值吻合、GUE 统计、局部波迹或半经典贡献，不等于固定算子的全局算术 explicit formula。
- 一个量子对象存在，不足以启动或通过 Route B；Route B 只针对已有连贯经典—量子延续的强候选。
- 所有“已证”“失败”“未赋值”均应回到具体项目的论文、证明笔记、判定 YAML 或批次收据核对。

原始会话入口为 [Flow Systems README](../../../flow_systems/README.md)，总设计为 [研究提案](../../../flow_systems/propose-flow-systems.md)。
