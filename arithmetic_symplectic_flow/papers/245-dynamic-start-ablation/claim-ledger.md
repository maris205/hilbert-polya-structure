# Claim ledger — ASFS-DISCOVERY-20260918-DS02

**Status:** `CONTROLLED COMPARISON COMPLETE; DYNAMIC PATH ADVANTAGE SCOPED`。  
**Formal Route coordinates:** `UNASSIGNED`；**Route B:** `NOT INVOKED`。

| ID | 声明 | 证据与状态 | 限制 |
| --- | --- | --- | --- |
| DS02-C1 | 原 solve 两次前向，D 默认路径，S 仅将 a_start 设为 a_end | Source lock + execution log；ESTABLISHED | 不将 S 偷换成 H_base 直接谱 |
| DS02-C2 | D 的 MSE/MAPE 与 H1 保存位一致 | Numerical control；OBSERVED | 不等于全部本征向量/分支跨环境稳定 |
| DS02-C3 | 各自首点定标下 D MAPE 2.29046%，S 75.48529%；MSE 12.22891 vs 5107.89411 | Finite numerical comparison；OBSERVED | 历史参数固定的消融，非各自重新优化的最优模型排名 |
| DS02-C4 | D 最大相对误差 20.17088% 在第 2 点；最大绝对误差 9.84489 在第 80 点 | Full 100-row residual ledger；OBSERVED | 平均误差不能替代逐点保证 |
| DS02-C5 | 每组保存 250 态、矩阵/分支、100 点残差及 300 步路径 | Machine-readable artifacts；COMPLETE | 浮点有限网格，非无限谱身份 |
| DS02-C6 | 静态沿用动态尺度结果另存 | Diagnostic only；OBSERVED | 与各自定标主比较分开，不混选有利结果 |
| DS02-C7 | 小矩阵残差、酉性偏差及取整边界距离已记录 | Numerical diagnostics；OBSERVED | 非后向误差认证、网格收敛或分支稳定性证明 |
| DS02-C8 | 静态低阶大跳已存在于 H_base 期望间隙，不是取整独自造成 | Saved-array readout audit + algebra；SCOPED | 不把 ee 称为 H_base 本征谱，不推断更深根因 |
| DS02-N1 | 已完美拟合百点、盲测成功、动态普遍优越、自然算术机制 | NOT ESTABLISHED | 这些结论不由本次比较推出 |
| DS02-R1 | A0/A1/A2/T0–T3 与 Route B | NOT EVALUATED | A−1 发现控制，不发 Route 坐标 |

`advance` 仅指低自由度候选有了实际消融与逐点诊断依据。两组分别拥有
自己的时间乘积、谱与尺度；没有把一个对象的输出转移给另一个对象。
