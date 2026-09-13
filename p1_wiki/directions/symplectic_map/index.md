# Session 3：Symplectic Map（Hamiltonian chaos；耗散 vs 保守）

> [P1 Wiki 总入口](../../README.md) · [结论](conclusions.md) · [路线图](roadmap.md) · [来源与复现入口](sources.md) · 原始会话：[Symplectic Map README](../../../symplectic_map/README.md)

## 本页用途

这里是 Session 3 的导航页，而不是新的论文、Route 评分或研究授权。它把原始会话中的保守/耗散比较、周期结构、算术接口与量子化设想分开陈列，供后续获授权的 agent 定位既有证据、已知边界和不应重复启动的分支。

会话的原始问题是：离散辛映射能否成为比低维或耗散原型更自然的算术动力学几何载体。原提案将它放在“Logistic 算术种子 → Hénon 几何桥梁 → 辛映射/周期几何 → Zeta/迹 → 可能的量子提升”的**概念谱系**中；这不是已证明的定理链，也不是任意对象之间可自动迁移的结论。见[原始提案 §1](../../../symplectic_map/propose-symplectic-map.md#1-session-identity)与[跨论文科学边界审计 §4](../../../symplectic_map/docs/research-batch07/BATCH07_CROSS_PAPER_SCIENTIFIC_AUDIT_V1_20260913.md#4-可用共享输入--不得主张内容矩阵)。

## 终态快照

- 原始 Session 3 覆盖离散辛映射、其高维/耦合变体，以及作为**匹配对照**的耗散扰动；连续流、纯符号系统和独立量子模型不在本方向内。[范围](../../../symplectic_map/propose-symplectic-map.md#11-scope-discipline)
- `Papers 27–31`（Batch07）已完成 5/5 本地交付和统一跨论文审计；该批次的停止点是“汇报并暂停”，不是自动开启 Paper32 或下一轮研究。[最终处置](../../../symplectic_map/docs/research-batch07/BATCH07_FINAL_CROSS_PAPER_DISPOSITION_V1_20260913.md#6-最终停止点)
- 当前证据不支持任何候选完成同一对象上的 Route A `A0 + A1`；更没有由此得到 A2–A4、Route B 或 Hilbert–Pólya 结论。[会话总览](../../../symplectic_map/README.md#总体进展与-route-a-定位2026-09-13)
- Batch07 的五篇是纯数学成果，记录为 `route_applicability: NOT_APPLICABLE`。这既不是 Route A/B 失败，也绝不构成任一关卡 PASS。[审计结论](../../../symplectic_map/docs/research-batch07/BATCH07_FINAL_CROSS_PAPER_DISPOSITION_V1_20260913.md#3-科学合取五个中心和十对关系)

## 阅读路径

| 需要回答的问题 | 先读 | 再回到的原始材料 |
| --- | --- | --- |
| 这一方向到底研究什么、边界在哪里？ | [路线图](roadmap.md) | [提案](../../../symplectic_map/propose-symplectic-map.md) |
| 已经得到哪些数学结论、哪些没有得到？ | [结论](conclusions.md) | [会话 README](../../../symplectic_map/README.md) 与五篇接受稿 |
| P27–P31 是否互相依赖或可拼接？ | [结论中的依赖图](conclusions.md#概念谱系不等于定理依赖) | [跨论文科学审计](../../../symplectic_map/docs/research-batch07/BATCH07_CROSS_PAPER_SCIENTIFIC_AUDIT_V1_20260913.md) |
| 要定位可复核的原稿、PDF、接受记录和勘误？ | [来源与复现入口](sources.md) | 各项目的锁、接受记录和接受源 |
| 要开始新的 A0→A1 检查？ | [路线图的最低输入契约](roadmap.md#若日后另行授权-a0a1-桥接诊断的最低输入契约) | Route 规则及同一对象的新增证据 |

## 已探索的系统簇：不要把目录数等同于 Route 进度

原会话 README 将工作按合并同族参数变体的口径归为至少八类。下表只是检索索引；一个编号项目不等于一个独立系统，更不等于一项 RH 进展。

| 系统簇 | 代表项目/材料 | 已归档的作用 |
| --- | --- | --- |
| Logistic / PCF 二次母映射 | P1–P3、P7 | 算术种子、乘子/指数时钟与 2-adic 障碍的背景 |
| Hénon、广义 Hénon 与指定辛扩张 | P1、P4、P12–P16、P18、P29 | 保守/耗散对照、周期结构、上同调和有理固定域问题 |
| Markov–baker 分片辛映射 | P2 | 精确原始轨道账本与有限记忆时钟的反例式对照 |
| Cat 环面映射及扰动 | P8–P11 | 素数阶载体、重数、中心化子商和等变时钟尝试 |
| 高维 shift-like 递推 | P17、P19 | 有限秩乘法群与支撑维度方面的限制 |
| 多项式 Hamiltonian 梯度剪切 / coupled kick–drift | P20–P28 | 高维次数、选择机制、同步置换与 monodromy 的结构成果 |
| q-Painlevé I（qPI）及自治特化 | P30–P31 | 算术几何临界结构与实相混合；两者只共享明确几何接口 |
| 标准/正弦/双谐波 twist 映射 | 未成篇研究 | 共轭时间、共振与小除数的实质检查；不能因未成篇而被误写成零工作 |

完整的合并口径、已吸收项目和未成篇边界见[原始系统簇表](../../../symplectic_map/README.md#已探索的系统族)。

## 两张必须分开的图

### 概念谱系（研究动机）

```text
Logistic 算术种子
        ↓
Hénon 几何桥梁
        ↓
离散辛映射 / Hamiltonian chaos
        ↓
周期轨道几何、作用量与相位
        ↓
自然的动力学 Zeta / 迹结构
        ↓
若前序关卡成立，才讨论量子/算子提升
```

这是用来生成问题和安排对照的工作假说。它**不**允许把上游的时钟、下游的谱语言或不同系统中的“周期”互相替换。

### 定理依赖（Batch07 的实际关系）

```text
P27  正 Newton 支撑下的 degree-transport / reciprocity 证书
  └─ 与 P28 共享 shear、rank-one 与 strict-carry 的基础语言，非其前提

P28  带同步置换的 word-specific selector / monodromy 构造
  └─ 不从 P27 的有限切换结论推出

P29  特定特征零 Hénon 族的滤过上同调与完整周期概形测试
  └─ 不给 qPI 提供同类有效判据

P30  qPI 的 p-adic/cyclotomic 临界理想与 first jets
  └─ 原曲面、polar divisor、pencil、完整纤维等几何接口
       ↓（只有这条明确接口）
P31  同一原自治实 qPI 曲面的 circlewise-centered sharp correlations
```

P30 的算术 Bockstein/Hasse/临界理想**不是** P31 相关衰减的证明；P31 自行证明所需的实曲面 lift、组件、测度和频率结构。P27/P28 的加权次数、P29 的 scheme 周期和式、P30 的矩阵 trace、P31 的 ensemble correlation 也是不同对象，不能拼为共同的 Riemann 行列式。精确反主张矩阵见[科学审计 §4–6](../../../symplectic_map/docs/research-batch07/BATCH07_CROSS_PAPER_SCIENTIFIC_AUDIT_V1_20260913.md#4-可用共享输入--不得主张内容矩阵)。

## 当前知识库内的交叉导航

相邻方向的名称表达的是探索会话，而不是数学蕴含关系：

- [Session 1：Logistic Dynamics](../logistic_dynamics/index.md)
- [Session 2：Hénon Dynamics](../henon_dynamics/index.md)
- [Session 4：Symbolic Dynamics](../symbolic_dynamics/index.md)
- [Session 5：Flow Systems](../flow_systems/index.md)
- [早期自由探索：zeta_mvp0](../zeta_mvp0/index.md)

任何跨方向的新桥接都应先记录为待验证的研究假说（原提案中的 `ROUND2_CLUE`），而不是复制某方向的正面结果来填另一方向的 Route 门槛。

## 使用边界

本目录是面向后续 agent 的检索层：它保留原始材料的身份、结论和反主张，但不替代原稿、锁、接受记录或 Route 评价文件。若原始文件与本页概述有冲突，以[来源页](sources.md)所列的接受源和当前处置为准；不得据此自动启动实验、改写冻结稿、重新评分或宣称外部发表。
