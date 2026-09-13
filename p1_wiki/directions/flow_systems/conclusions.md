# Flow Systems：结论、障碍与未完成的桥

[P1 Wiki](../../README.md) · [本方向目录](index.md) · [结论边界](conclusions.md) · [路线图](roadmap.md) · [五种连续时间子型](p24-p28-five-planned-forms.md) · [来源与原件](sources.md)

## 总结

这条方向已经产出的是：连续时间流的闭轨、Zeta、trace、拓扑与量子所有权上若干**精确且有范围的结果**，以及一组有意设计的负对照。它没有产出一个经 Route A/Route B 认可的正向算术候选，也没有给出 Hilbert–Pólya 或黎曼假设的证明。

以下按“已得到什么 / 它不代表什么”写，避免把论文交付、局部定理和整体路线混为一层。

## 早期 Flow 路线留下的可复用结论

| 主题 | 已有的受限结论 | 不能升级为 |
| --- | --- | --- |
| P1：经典流基线 | Deninger 算术流能内生产生周期为 `log p` 的紧致轨道包，但没有规范化的单轨 trace；模曲面测地流有完整闭轨与 Selberg/Ruelle 架构，但标准长度支撑与所有 `k log p` 严格不相交。 | 自然的素数—单轨 trace 对应。 |
| P2：flow Zeta | 每个素数 packet 含不可数条同长本原轨道；普通逐轨 Ruelle 乘积已在单个 packet 内发散。测度、群胚或上同调替代仍为 `NOT_TESTABLE`，不是已被否证。 | 普通逐轨乘积可作为该对象的自然全局 Zeta。 |
| P3：trace bridge | 同一对象的 trace certificate `T0–T7` 被建立；局部 trace germ 有 smooth ambiguity，不同对象的 coordinate splice 失效；模曲面重复长度与 `k log p` 严格不交。 | 局部半经典贡献就是全局固定算子算术 trace。 |
| P4：算术正控 | 有限域 Frobenius suspension 精确给出原生 Hasse–Weil Zeta；一时钟定理排除 characteristic-zero 的全素数目标，逐素数圆周拼接被标记为 `PROVES_TOO_MUCH`。 | 特征零全素数动力系统已经构造。 |
| P5–P6：量子与所有权 | 一个典范 Koopman 生成元可完整定义且自伴，但其谱结构在 B3 严格失败；精确 Hasse–Weil 行列式与自伴悬挂时间属于不同算子，不能跨算子拼接 credit。 | 任意“同一算术母体”都给出同一有效 Hilbert–Pólya 算子。 |
| P7–P9：packet 拓扑 | proxy 上的局部对象与零模 trace-log determinant 可以分离；真实继承轨道是非平凡不可分空间，真实标准 LCH 分支在拓扑前提处失败，旧圆周计算仅保留为 proxy。 | proxy 迹公式描述了真实 packet 拓扑。 |
| P22：代数支撑 | 对所有 `N>1`，fppf 与 finite-flat site 上 Verschiebung 加性 sheaf lift 不存在；`N=1` 是严格对照。 | 这项局部代数 no-go 本身完成了整体流/算子构造。 |

对应的原论文入口在 [来源与原件](sources.md#早期-flow-论文与状态材料)。上表是导航摘要；它不替代论文中的假设、定理范围、证明或 evaluator 记录。

## P24–P28：五个子型的最终、受限结果

| Paper | 最终论文承载的结果 | 明确不声称 |
| --- | --- | --- |
| P24 | 一般系数环上的 principal-congruence trace identity 与 first-jet laws 是精确定理；冻结 loxodromic profile 的最大碰撞桶由 208 降至 84，但 singleton owner 为 0。 | 这只是量化的负特异性结果；不是 orbit-owner 解。proxy 保持 `(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`，完整 flow 未赋值。 |
| P25 | exact roof-nontransfer 定理与 2,241 行 validation-only estimand 给出清晰的负迁移结果：物理三圆盘流不继承 unit-roof symbolic determinant credit。 | 非算术 unit-roof calibrator 的解析行列式，不是物理三圆盘流的正向算术 A2；物理 flow 未赋值。 |
| P26 | 138-instance / 55-group 的精确 owner taxonomy、配对负控、both-controls-pass residue `0` 支持限定的 nonfactorization 结论。 | 有限 multiset 不能提升为全局本原 Euler owner；A2 仍失败。 |
| P27 | residual inverse-limit renormalization no-go / fixed-owner escape，以及独立的 homology-cover 四象限校准，都是明确的负候选结果。 | 不把 non-residual `Q11` control 与 residual 定理混同；residual tuple 的 A1 为失败，两个冻结候选均没有正向算术 A2。 |
| P28 | exact nonarithmeticity、有限 word-to-length completeness certificate、exact systole chain 构成实质正控制。 | 不将正控制转移为 magnetic/arithmetic credit；magnetic/arithmetic transfer 与匹配的 Bolza/control A2 比较均未声明，完整 tuple 未赋值。 |

五个对象的初始限定、假设和 kill gate 见 [五种连续时间子型](p24-p28-five-planned-forms.md)。最终 PDF 与项目级证据的链接见 [来源与原件](sources.md#p24p28最终论文与项目入口)。

## 流程终态不等于科学路线终态

P24–P28 的 Round 9 收尾同时有两组事实，必须并列保存：

| 记录层 | 已完成的事情 | 不表示 |
| --- | --- | --- |
| Stage 4.5 冻结完整性重放 | 397/397 通过；记录了引用、证据行和冻结输出的核验。 | 数学正确性、全局语义完备性或 Route credit。 |
| Stage 5 FULL | 五篇最终 PDF 共 71 页；20 个独立构建输出、444/444 批审通过；锁定 manuscript/bib/content proof 未变。 | 新科学执行、路线晋级、投稿就绪或外部认可。 |
| Stage 6 | 用户明确选择“跳过，继续下一批”；5/5 pipeline 的 Stage 6 为 `skipped`，全局状态为 `completed`，Process Record 为 0。 | 已经写出或暗含 Stage-6 流程记录；以后不需要新授权即可继续研究。 |

终态收据还明确：科学内容、最终 PDF、canonical/results 树和 route 均未因该 transition 改变；没有投稿或外联。后续研究、修订、格式化或发布应作为新 pipeline 或另行授权的定点任务开始。

## 当前 Route 边界

对 P24–P28，源记录的批次状态是 Route A 的早期 `A0–A1 / A1–A2` 证据与对照层：

- 正向算术 A2：`0/5`；
- Route B 调用：`0/5`；
- Gates A–E：没有新增 credit；
- 12 个冻结几何/物理实例与 7 个 `q`-symbol calibrator 只是 19 个 bookkeeping model instances，不是 19 个独立统计样本。

因此，最简洁而不越界的总述是：**五个连续时间子型提供了精确局部定理、负特异性/负迁移/非因子化障碍和一个正控制；它们的交付流水线已经完成，但尚未构成正向算术 A2、Route B、固定算子全局 trace identity 或 Hilbert–Pólya/RH 结论。**

## 下一步阅读而非自动推进

准备继续某一子型时，先以 [路线图](roadmap.md) 的共同约束定位 A0–A4，再读取对应的原项目 README、最终论文和 route record。不要从“pipeline completed”反推“科学已通过”；也不要从一个 proxy、calibrator 或局部定理搬运到另一个对象。

批次终态的权威说明为 [Stage-5 完成报告](../../../flow_systems/BATCH_ROUND9_STAGE5_COMPLETION_REPORT.md) 与 [Stage-6 跳过收据](../../../flow_systems/BATCH_ROUND9_STAGE6_SKIP_RECEIPT.json)。
