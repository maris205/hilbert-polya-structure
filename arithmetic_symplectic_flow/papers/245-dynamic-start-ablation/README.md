# 245 — 非自治路径与静态终点：逐点谱对照

**Scope ID:** `ASFS-DISCOVERY-20260918-DS02`。  
**Status:** `CONTROLLED COMPARISON COMPLETE; DYNAMIC PATH ADVANTAGE SCOPED`。  
**Decision:** `advance` 受控数值诊断；两次前向已结束，不追加调参。  
**Formal Route coordinates:** `UNASSIGNED`；**Route B:** `NOT INVOKED`。

在 hbar、网格、300 步、目标表、谱重构和首点定标规则都固定时，
原非自治路径的 MAPE 为 **2.29046%**，静态 a=1.02 对照为
**75.48529%**；MSE 分别 **12.22891** 和 **5107.89411**。
因此本次静态消融使拟合明显变差，但不代表分别重新优化后的模型排名。
动态组第 2 点相对误差仍有 **20.17088%**，不是逐点高精度百点拟合。

每组保存全部 250 个重构能量、特征值/向量、矩阵、分支以及 100 个
目标的逐点残差。动态组两个总指标与 244-H1 完全一致。旧记录不改，
没有优化、GPU、保留集测试或 A0 评分。

- [完整结果与解释](paper.md)
- [候选/实验范围卡](candidate-card.md) · [执行前原始卡](candidate-card-frozen-v1.md)
- [声明账本](claim-ledger.md)
- [命令、运行与证据](evidence/README.md)
- [动态组逐点 CSV](evidence/run-1/DS02-D/points.csv)
- [静态组逐点 CSV](evidence/run-1/DS02-S/points.csv)
- [两组摘要 JSON](evidence/run-1/comparison.json)

下一步宜先分析已存低阶态的完整读出链，明确原相位、H_base 期望值、
整数分支与首点尺度各自的作用，再决定是否扩展实验；不要仅看平均误差
继续增加拟合自由度。
