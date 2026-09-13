# Flow Systems：路线图与判定边界

[P1 Wiki](../../README.md) · [本方向目录](index.md) · [结论边界](conclusions.md) · [路线图](roadmap.md) · [五种连续时间子型](p24-p28-five-planned-forms.md) · [来源与原件](sources.md)

## 总设计

Flow Systems 的原始设计把连续时间视为可能比离散映射更自然的载体，但这一点只是研究假设。目标链条是：

```text
算术结构
  → 符号/离散骨架
  → 连续时间流
  → 本原闭轨（周期、action、稳定性、相位）
  → 动力 Zeta / trace formula
  → 自然量子或半经典对象
  → 固定算子的谱问题
```

要点不是“找一个看起来混沌的系统”，而是让同一对象上的周期、重复、权重、trace 和量子化具有可检验的内生联系。完整提案见 [研究提案](../../../flow_systems/propose-flow-systems.md)。

## 共同的研究纪律

所有 Flow 候选在比较前应固定相空间、生成元、时钟、本原对象、重复律、算术来源、解析对象和数据拆分；然后才讨论目标相符性。

- 主对象必须是真正的**连续时间流**，不是给离散映射换名。
- 不把 `T_p=log p`、von Mangoldt 权重或零点数据手工塞进定义、筛选、参数或 cutoff。
- 大胆假设可以提出，但在有来源或证明前只能标为 `HEURISTIC`。
- generic chaos、打乱标签、相邻参数、较简单母体和 `PROVES_TOO_MUCH` 对照是证伪合同的一部分。
- 局部半经典轨道贡献不等于固定算子的全局算术 trace；数值吻合和 GUE 统计也不等于算术证据。

这些规则使“有趣的机制”与“可获得 Route credit 的机制”保持分离。

## Route A 与 Route B 的角色

正式细则不在本页重述；判断时直接使用 [Route A evaluator](../../../flow_systems/skills/route-a-evaluator.md) 与 [Route B evaluator](../../../flow_systems/skills/route-b-evaluator.md)。提案中的 Route A 语言如下：

| Route A 坐标 | 要检查的对象 |
| --- | --- |
| A0 | 算术相关性 |
| A1 | 本原周期/闭轨结构 |
| A2 | 动力 Zeta / Fredholm determinant |
| A3 | 解析结构 / Weil-compression 兼容性 |
| A4 | 自然量子化或算子 lift |

Route B 只面向已经有连贯经典—量子延续的强候选；量子算子“存在”本身不能用来挽救 A 端薄弱的对象。所有 formal verdict 必须回到具体 evaluator 输入与项目级记录，不能由本 wiki 推演。

## 原始六阶段研究路线

| 阶段 | 目标 | 主要 Route 关注 |
| --- | --- | --- |
| 1. Classical Flow Baseline | 比较流族、本原闭轨、周期/action/monodromy、自然符号编码及显然障碍。负分类是有效结果。 | A0–A1 |
| 2. Flow Zeta and Resonance Structure | 为最强经典候选构造本原/重复 ledger、自然 Zeta 或 determinant，检查收敛、延拓、权重和 cutoff。 | A1–A3 |
| 3. Classical vs Quantum Trace | 验证闭轨数据是否出现在同一自然量子对象的 trace/wave trace 中，并分清局部与全局、半经典与固定算子。 | A3–A4 |
| 4. Arithmetic Flow Search | 寻找不直接编码素数表的连续时间算术机制；允许大胆假设，也要求内生周期、相位、权重和重复。 | A0–A3 |
| 5. Fixed Quantum Operator Candidate | 只为强候选处理 Hilbert 空间、域、自伴性、谱型、计数律、行列式与高能行为。 | A4；必要时 B1–B3 |
| 6. Prime Trace / Weil Interface | 仅在前段出现严肃候选后，比较素数幂侧与同一对象的闭轨 trace，并测试最强算术/算子桥。 | A3–A4；必要时 B4 |

这是一张研究设计图，不是逐阶段完成即自动获得数学结论的清单。尤其 Stage 3 必须把“一条已认证轨道贡献”和“完整全局 trace formula”分开。

## P24–P28 在路线图中的位置

五个连续时间子型最初以 Stage 1 / Route A `A0–A1` 的冻结对象和证伪合同启动；完整设计见 [五种连续时间子型](p24-p28-five-planned-forms.md)。后续经历的论文、完整性与格式化流水线不会重写这条初始科学路线。

Round 9 的终态应如此读取：

```text
论文/完整性/格式化链：完成（Stage 5；Stage 6 明确跳过）
科学路线：仍为早期 A0–A1 / A1–A2 evidence & control layer
正向算术 A2：0/5
Route B 调用：0/5
```

因此，P25 的 unit-roof symbolic determinant 只能作为非算术 calibrator 的解析结果，P28 的正控制也不能转写为 magnetic/arithmetic A2。逐篇限制见 [结论边界](conclusions.md#p24p28五个子型的最终受限结果)。

## 给下一位 agent 的定位方法

1. 先确定所问的是哪一个 flow 对象，而非只按关键词（“zeta”“trace”“quantum”）合并不同对象。
2. 读取对象对应的项目 README、最终论文和项目级 route/evidence artifact；不要把总 README 的摘要当作证明。
3. 分开记录：定理、有限/数值观察、`HEURISTIC`、proxy/calibrator 结果、pipeline/format 状态和 formal Route verdict。
4. 每一次跨对象映射都核对 operator owner、time/roof、primitive/repetition law、trace regime、normalization 和 cutoff 是否真的相同。
5. 若想开始新的科学执行，终态收据不自动提供授权；它只记录上一批已经结束的 pipeline。

## 关键边界

本方向的最终目标仍是一个研究假设：连续时间的周期、action、phase、trace 和自然量子化**可能**提供算术 Hilbert–Pólya 候选的合适语言。已经完成的障碍、正控和局部结果会收缩或引导该搜索，但它们不会自动拼成全局固定算子、全局 determinant equality 或 RH 结论。

路线细节、禁止的捷径和原始阶段说明以 [提案的核心问题与阶段](../../../flow_systems/propose-flow-systems.md) 为准；批次 P24–P28 的状态边界以 [Stage-5 完成报告](../../../flow_systems/BATCH_ROUND9_STAGE5_COMPLETION_REPORT.md) 为准。
