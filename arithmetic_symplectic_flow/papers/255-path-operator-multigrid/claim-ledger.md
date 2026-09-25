# CS05 — 声明账本

Scope ID: `ASFS-DISCOVERY-20260919-CS05`。  
Current status: `PATH-OPERATOR SEARCH COMPLETE; JOINT TARGET UNMET`。

| 声明 | 状态 | 证据与边界 |
| --- | --- | --- |
| 五个有限载体及各自的T、V、路径、H_ref、K_path明确 | ESTABLISHED AS DEFINITIONS | [冻结卡](candidate-card.md)，不声称五个算术候选 |
| 精确酉前缀下K自伴、保迹、谱受H_ref上下界约束 | ESTABLISHED — FINITE ALGEBRA | [全文§4](paper.md#4-路径算子的有限数学性质与实现)；不代表目标谱吻合 |
| 单项酉共轭同谱；平均具有Hilbert–Schmidt方差恒等式 | ESTABLISHED — FINITE ALGEBRA | 不保证每个间隔缩小或首间隔稳定 |
| P/J/D/H/B、双维度目标和冻结顺序已实际执行 | COMPLETED — BOUNDED COMPUTATION | [runner](run_search.py)、[result](evidence/run-1/result.json)；240训练+1回归+2维度前向，退出码0 |
| 旧N250回归 | PASS — SCOPED REGRESSION | 预测、M、W与旧Q0103差值0；不要求新旧读出同谱 |
| 本轮联合拟合目标 | UNMET — FINITE NEGATIVE | 主B0112的M320/M352=6.170107%/6.262007%，G4.342523%，J2.756417；120个不同成员J<1数为0 |
| 五族、静态数组先冻结，241–300后评价 | RECORDED | 十份完整赢家NPZ先保存，training_frozen在新参考生成之前；不声称历史盲测 |
| N384/N416预定2%稳定性线 | UNMET — SCOPED DIAGNOSTIC | 固定参数G5.673720%/5.501768%；不是无限不收敛定理 |
| 同参数静态谱与新路径谱的MAPE比较 | OBSERVED — FINITE ABLATION | 五族路径结果均较其静态参考小；静态族未另行优化，两个读出各自定标 |
| 五族实现中的有限矩阵关系 | FLOATING-POINT CONSISTENCY | 保存全部前缀、K_raw/K及本征态；小残差不替代精确假设或无限维证明 |
| 无限维路径能量/谱收敛、全局最优和可信A−1 | OPEN / NOT ESTABLISHED | 两训练维度不是独立验证；有限误差不能替代证明 |
| 内生素数机制、roof/悬流、primitive/repetition、轨道迹/zeta | OPEN / NOT SUPPLIED | 不借用其他论文或形式的结果 |
| A0/A1/A2/T0–T3 | NOT EVALUATED | 没有正式Route坐标；formal UNASSIGNED；B NOT INVOKED |

Portfolio：stop本轮拟合/稳健性提升声明，保留有限对照并fork后续构造。
研究标签2026-09-19与实际UTC运行时间分开记录。
卡中的冻结状态不覆盖为事后标签；有限数学命题的假设不被浮点残差替代。
