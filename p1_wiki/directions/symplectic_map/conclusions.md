# Symplectic Map：结论、可用接口与未闭合关卡

> [方向入口](index.md) · [路线图](roadmap.md) · [来源与复现入口](sources.md) · [P1 Wiki 总入口](../../README.md)

## 结论如何读取

以下内容有三种不同的效力，不能混写：

1. **接受稿中的数学结论**：只在各自对象、假设和函数类下成立；应回到对应接受源核对量词。
2. **Batch07 的本地交付结论**：P27–P31 已按各自合同接受，并完成组内非碰撞审计；这不等于外部同行评审或全球优先权判断。
3. **Route 结论**：Batch07 五篇的 `route_applicability: NOT_APPLICABLE`，所以不产生 Route A/B 的 PASS、FAIL 或层级推进。[统一处置](../../../symplectic_map/docs/research-batch07/BATCH07_FINAL_CROSS_PAPER_DISPOSITION_V1_20260913.md#3-科学合取五个中心和十对关系)

会话层面的 RH/Hilbert–Pólya 盘点则另有一条明确负面边界：现有材料没有同一候选的 `A0 + A1` 连续通过，也没有自然的目标 Zeta/Fredholm 行列式、Weil 压缩桥接或 Route B 就绪的量子化路径。[会话 README 的定位](../../../symplectic_map/README.md#五阶段研究计划不等于-a0a4-通关)

## Batch07 五个中心结论

| 项目 | 接受稿的中心结论（极简） | 可复用的受限接口 | 不能据此声称 |
| --- | --- | --- | --- |
| **P27** | 在特征零、高维正 Newton 支撑、完整 strict source/reflected/target 证书下，分离 Hamiltonian 双 shear 的实际加权次数沿严格支发生对角平移、有限选择切换及逐字反射互易。 | 证书化的 leading-degree/carry 检查；`A_α`、`B_βA_α` 的 rank-one 形式；有限 word 的受限互易。 | 任意支撑分类、全局 reversor、entropy、普通/高阶 dynamical degree、全迭代扰动稳定性或 Riemann 谱。 |
| **P28** | 对每个给定本原 selector pair word，构造一个带同步置换的高维多项式辛映射；normal-fan、strict carry、标记 monodromy 与字典条件下可恢复有序信息。 | word-specific 的 incidence support、normal-fan cone、精确 monodromy/decoder 条件。 | 一个固定 map 生成所有任意长 word、固定维度构造、实际多项式状态周期、标量递推解码 word、inverse reciprocity 或 entropy。 |
| **P29** | 对指定的特征零 area-preserving Hénon 有限复合，给出保次数原函数、精确滤过 Hilbert 计数及由单个完整固定点概形检测多项式余边界；另有特定 lift 的有理固定域结论。 | orbit basis、ordinary-degree filtration、scheme no-alias 和 additive-extension 判据，均限该 Hénon 递推。 | 把 scheme 测试移植到 qPI/一般辛映射；把几何点零、标量迹和概形零混同；一般可积性判断。 |
| **P30** | 对原 qPI 给出完整首层两方向 coefficient ideal，并在明确有限域/完整 time-jet 条件下给出高层 cyclotomic first jet；特征二的比较从 height 2 开始。 | 原八中心曲面、polar divisor、primitive pencil、完整光滑有限纤维等准确几何接口。 | 所有高层的完整厚度、奇异纤维分类、实频率/相关衰减，或把截断长度五写成完整临界商长度。 |
| **P31** | 对同一原自治实 qPI 的完整曲面，在逐连通圆中心化后得到 sharp correlation 渐近：`T ≠ 1` 的驻相尺度、`T=1` 的中心 jet 尺度、`T=3/16` 的双贡献，以及原单步奇偶。 | 固定 `T`、紧能窗、原范数下的 circlewise projection/coarea、`F²` 频率与原 `F` parity 接口。 | 未投影/单圆 mixing、CLT、跨参数转变一致估计、正特征 Hasse/厚度、周期阶计数或 Riemann 谱。 |

P27–P31 的精确主文件、PDF、接受记录和已披露 P27 书目勘误均列在[来源页](sources.md#五篇接受产物)。五个 finding 的完整科学边界见[跨论文审计 §3](../../../symplectic_map/docs/research-batch07/BATCH07_CROSS_PAPER_SCIENTIFIC_AUDIT_V1_20260913.md#3-五个精确独立-finding)。

## 从整个会话可保留的判断

### 1. 保守几何提供了结构工具，但没有自动提供算术来源

辛性、生成函数、严格 carry、周期概形、相位或量子化语言，均可能让结构问题更精确；它们本身不生成 `p ↔ γ_p`、`log p` 时钟、素数幂重复规则或正确的稳定性权重。早期时钟、重数和有限记忆机制的负结果尤其说明：丰富周期不等于自然的素数机制。[算术自然性问题](../../../symplectic_map/propose-symplectic-map.md#71-arithmetic-naturality)

### 2. 高维提升是实质数学进展，但不是 Route A 的替代品

高维 Hamiltonian 梯度剪切线的 P25 被会话总览列为最强一般性结构成果；P27–P28 进一步给出受限的选择和 monodromy 机制。但 P28 对每个 word 增维并单独构造一个 map，不能变成“固定映射产生所有任意长词”。次数矩阵的 Perron 谱也不是 Hilbert–Pólya 能谱。[会话优先级判断](../../../symplectic_map/README.md#哪条最成熟哪条最值得继续考察)

### 3. P29 是强的周期—上同调工具，非 prime-weight 工具

P29 的贡献在于精确地辨别某个 Hénon 多项式余边界是否可由完整固定点概形检测，以及保持原函数的次数控制。它不提供自然素数权重、Fredholm 行列式或 qPI 的有效 cohomology 判据。P29/qPI 的系统、函数类与周期对象均不同。[P29/P30 的非迁移边界](../../../symplectic_map/docs/research-batch07/BATCH07_CROSS_PAPER_SCIENTIFIC_AUDIT_V1_20260913.md#52-2930为何-scheme-语言不是可迁移的-theorem)

### 4. qPI 是较直接的诊断接口，而不是已获 A1 的领先候选

qPI 让有限域中的点阶、算术几何与回返有可精确定义的连接；P30 与 P31 又在同一模型家族上给出不同的算术几何和实动力学成果。但它仍缺少内生素数选择、自然时钟/重复权重，以及处理连续周期纤维多重性的内生机制。P30 也没有证明 P31 的衰减，P31 不是 Riemann 谱。[A0→A1 的会话建议与缺口](../../../symplectic_map/README.md#面向-a0a1qpi-是优先诊断对象不是已接近通关的候选)

## 概念谱系不等于定理依赖

```text
概念上： Logistic → Hénon → Symplectic Map → 轨道/Zeta → 量子提升
                 （研究动机；不是推理箭头）

定理上：  P27      P28      P29      P30 ──[原曲面/pencil]──> P31
           │        │        │        │                         │
           └────────┴────────┴────────┴─────────────────────────┘
             方法、术语或对象相近，不自动交换结论
```

唯一明确的组内文献依赖是 P31 使用 P30 的未发表本地版本作为几何输入；P31 不消费 P30 的算术主定理，P30 不反向引用 P31，故没有循环依赖。P27/P28 共享的 shear/rank-one/strict-carry 基础也不能被重复计为两个独立机制。详见[组内依赖与术语边界](../../../symplectic_map/docs/research-batch07/BATCH07_CROSS_PAPER_SCIENTIFIC_AUDIT_V1_20260913.md#6-重复计功循环术语与未知边界)。

## 已明确不能跨越的 Route 边界

| 层级/主题 | 当前事实 | 不能用来替代它的材料 |
| --- | --- | --- |
| A0：算术来源 | 没有同一固定对象的内生素数选择与自然对应。 | 先选有限域特征、外贴标签、逐素数调参、GUE-like 统计。 |
| A1：原始轨道与重复 | 没有与 A0 同源的 `log p` 时钟、prime-power 重复与重数规则。 | 多个系统里挑各自最好的周期结果，或把 extension degree 当原轨道重复。 |
| A2：Zeta / Fredholm | 没有已认可的、由同一动力对象自然产生的目标行列式。 | 普通结构 Zeta、次数特征多项式或无共同轨道账本的谱构造。 |
| A3–A4 / Route B | 没有前序算术链支撑下的 Weil/迹压缩或自然量子/算子提升。 | 局部辛结构、形式生成函数、量子化启发或数值零点拟合。 |

原始路线图强调：Route B 只能对已经具有自然算子级延续的强 Route-A 候选使用，不能用来挽救较弱的 A0/A1 构造。[Route 使用原则](../../../symplectic_map/propose-symplectic-map.md#3-current-resources)

## 对下一位 agent 的安全交接

先把任何新设想分类为“本方向内的新候选”“对照”“已知系统的诊断”或 `ROUND2_CLUE`。只有在用户另行授权继续研究时，才可从[路线图](roadmap.md)的最低输入契约开始；不得把这里的概述、Batch07 完成状态或 P27–P31 的本地接受标签转写成新的数学证据、Route 晋级或外部发布资格。
