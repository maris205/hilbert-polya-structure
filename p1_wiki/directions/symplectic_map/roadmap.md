# Symplectic Map：路线图、实际位置与后续准入边界

> [方向入口](index.md) · [结论](conclusions.md) · [来源与复现入口](sources.md) · [P1 Wiki 总入口](../../README.md)

## 先区分两种“路线图”

原[提案的 Stage 1–5](../../../symplectic_map/propose-symplectic-map.md#8-suggested-research-stages)是探索的组织方式；Route A 的 A0–A4 是要求**同一个候选**保持算术来源、原始轨道、时钟/归一化和后续对象一致的评价关卡。做到了“高维结构的 Stage 4”不等于通过 A4。

```text
提案阶段：  对照 → 轨道/Zeta → 算术搜索 → 高维/耦合 → 量子/迹
Route A：    A0          A1           A2              A3          A4
                同一候选、同一算术—轨道—权重链必须连续
Route B：    仅在前述链足够强、且存在自然算子级延续时才可能进入
```

## 原始五阶段与现有材料的对应

| 原始阶段 | 预期目标 | 当前可定位的成果/对照 | 仍未闭合的必要内容 |
| --- | --- | --- | --- |
| **Stage 1**：保守 vs 耗散结构基线 | 匹配比较，辨认究竟哪些周期/相位结构由辛性带来；重点 A0–A1。 | P1 的 Hénon 候选和 P2 的 baker 对照给出早期否定性检查；会话中也保留 Hénon 与耗散边界。 | 未筛出可贯穿后续关卡的强算术候选；P1/P2 的历史 Route 记录不可改写为正面进展。 |
| **Stage 2**：周期轨道 Zeta | 为最强对象建立自然的 primitive/repetition ledger 与动力学 Zeta/Fredholm；重点 A1–A2。 | P2 的精确账本、P29 的完整周期概形测试、Hénon 周期与上同调工具。 | 没有被认可的算术 Zeta/Fredholm 对象；普通结构性周期数据不等于目标行列式。 |
| **Stage 3**：算术辛搜索 | 无手工 prime table 地产生/保留算术结构；重点 A0–A2。 | P3–P11 的时钟/重数障碍，P30 的 qPI 算术几何 first-jet 结果。 | 没有同一对象内的自然 `p ↔ γ_p`、`log p` 尺度和素数幂重复机制。 |
| **Stage 4**：高维/耦合辛映射 | 测试高维是否提升算术容量、相消或行列式增长；重点 A1–A3。 | P20–P28 的高维梯度剪切；P25 的精确次数/支撑秩结果，P27/P28 的 certificate/selector/monodromy 结构。 | 高维没有自动产生算术容量、目标迹公式或零点计数；P28 仍为每个 word 的单独增维构造。 |
| **Stage 5**：量子化与迹接口 | 对前序存活候选考察 unitary/FIO/trace 与 prime-side compatibility；重点 A3–A4，必要时再有限进入 Route B。 | 辛结构、生成函数、局部相位等仅构成启发材料。 | 没有前置 A0–A3 链、自然 Hilbert 空间/量子化及可识别的量子 trace；不得因形式相似而开启 Route B。 |

此表对照的是会话 README 的实际盘点，而不是对每个历史编号项目重新评分。[原路线图](../../../symplectic_map/propose-symplectic-map.md#8-suggested-research-stages)与[实际进展表](../../../symplectic_map/README.md#五阶段研究计划不等于-a0a4-通关)应配套阅读。

## 历史 Route 状态：只保留，不重写

- P1 的冻结候选已在历史正式评价中因算术来源/冻结载体检验失败而拒绝。
- P2 的正式状态是 `A0_FAIL + A1_WEAK`：低周期原始轨道核对并不能弥补有限记忆标量时钟无法容纳全部素数对数的障碍。
- P27–P31 是纯数学成果，`route_applicability: NOT_APPLICABLE`；它们不继承 P1/P2 的 FAIL，也不倒推出新的 A0/A1 PASS。

这些状态的精确措辞以[会话 README](../../../symplectic_map/README.md#五阶段研究计划不等于-a0a4-通关)和[Batch07 最终处置](../../../symplectic_map/docs/research-batch07/BATCH07_FINAL_CROSS_PAPER_DISPOSITION_V1_20260913.md#3-科学合取五个中心和十对关系)为准。

## 已形成的路线图设计原则

### 保守/耗散必须是匹配对照

比较 `det DF = 1` 与耗散扰动时，应保持可比的 map family/参数约束，并明确比较原始周期、重复、monodromy、回返、作用量/返回时间、Zeta 稳定性、相位/符号与量子化自然性。对照的目的不是证明“保守更好”，而是隔离确实由辛几何带来的结构；否定结论同样是有效结果。[原始比较设计](../../../symplectic_map/propose-symplectic-map.md#6-conservative-vs-dissipative-comparison)

### 每一个动力学对象必须从内部产生自己的数据

原始路线禁止把轨道周期手工写成 `log p`、手工插入 von Mangoldt 权重、用 Riemann 零点表调参，或把不同对象的最佳子结果粘合成一条假链。任何 Zeta、Fredholm 或量子对象必须来自同一动力学对象及其明确的 primitive/repetition 规则。[算术自然性约束](../../../symplectic_map/propose-symplectic-map.md#71-arithmetic-naturality)与[Zeta 约束](../../../symplectic_map/propose-symplectic-map.md#73-dynamical-zeta--fredholm-determinant)

### 量子化是后置检查，不是补救手段

只有候选已经给出自然的古典算术—轨道链时，才讨论固定边界条件、自然 Hilbert 空间、unitary/Fourier-integral quantization 以及 trace 中的轨道相位。Route B 不用来弥补 A0/A1 的缺失。[Stage 5 条件](../../../symplectic_map/propose-symplectic-map.md#stage-5--symplectic-quantization-and-trace-interface)

## 若日后另行授权：A0→A1 桥接诊断的最低输入契约

这不是当前的待执行任务，也不评价 qPI 的成功概率。它是会话 README 已给出的最小、可审计问题框架：

1. 固定**同一个**原始动力对象、允许参数范围及算术来源，不能每个素数换对象或换调参规则。
2. 写出候选的素数对应、自然时间/权重、原始轨道与重复轨道规则，以及重数/连续族处理方式。
3. 对非素数、邻近参数和匹配对照做适用性检查；保留失败的机制与边界。
4. 明确区分“有限域点阶统计”等独立算术动力学结果，与真正满足 A0/A1 所需的素数—轨道桥接。
5. 禁止外贴标签、目标零点拟合、事后调整阈值，或拼接多个系统的最佳成分。

qPI 被提出为可优先**诊断**的已有系统，是因为其有限域回返与点阶接口比单纯复杂度/次数谱更直接接近算术；它仍不具备内生素数选择、自然 `log p` 时钟和孤立轨道式重数处理。[原始建议及限制](../../../symplectic_map/README.md#面向-a0a1qpi-是优先诊断对象不是已接近通关的候选)

## 必须保留的分叉边界

| 若出现的想法 | 在本方向的正确状态 |
| --- | --- |
| 连续 Hamiltonian flow、纯符号系统、量子图、无关算子构造 | 记录为 `ROUND2_CLUE`；不把它静默扩张成 Session 3 的新主线。 |
| qPI 上的实相关、p-adic 临界理想或高阶厚度猜想 | 保持其原对象与证明边界；P30/P31 不相互补全缺失部分。 |
| Hénon 的余边界/周期概形工具 | 只在其明确 Hénon 假设下使用；不能直接导入 qPI 或一般辛映射。 |
| P27/P28 的 degree-transport / monodromy 机制 | 带原始 support、维度、字典、strict carry 与 decoder 条件使用；不得转换成 entropy、谱或通用选择器。 |

Batch07 已经完成并暂停，因此这些分叉是知识库的防错标记，不是隐含的排期或继续授权。[当前停止点](../../../symplectic_map/BATCH_07_CONTEXT.md#当前终态batch07完成并暂停)
