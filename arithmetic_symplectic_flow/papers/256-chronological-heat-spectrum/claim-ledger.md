# CS06 claim ledger

Scope ID: `ASFS-DISCOVERY-20260919-CS06`。  
Current status: `LOW-100 JOINT TARGET MET; STATIC CONTROL NEAR-IDENTICAL; HIGH-MODE STABILITY OPEN`。

| Claim | Evidence class / status | Owner and limit |
| --- | --- | --- |
| Q/R/S/E是四个分别冻结的有限热算子 | DEFINITION | [卡](candidate-card.md)，不是四个算术机制 |
| 热步正定收缩、乘积可逆，H_eff≥mI | EXACT FINITE PROPOSITION | [论文§4.1](paper.md#41-有序热算子的同对象能量)，非连续极限定理 |
| 三种势所有全局最低点在(−8,8)，可由V'单调段枚举 | EXACT SCALAR PROPOSITION | [论文§4.2](paper.md#42-全局势最低点确在固定根隔离区间)，float求根非认证 |
| 整体倒放步序不改变奇异谱 | EXACT NEGATIVE CONTROL | [论文§4.3](paper.md#43-时间排序不能从奇异谱全部恢复)，不声称全部时序可恢复 |
| 56唯一成员、112训练+1控制+4后检、退出码0 | COMPLETED COMPUTATION | [原结果](evidence/run-1/result.json)，未独立重跑 |
| S0047前100双网格M≈2.05%、W≈6.35%、G=.143515%、J=.903204<1 | POSITIVE FINITE FINDING | [论文§5](paper.md#5-搜索结果与执行状态)，两网格均参与监督选择 |
| 四个冻结后百点G均小于2% | POSITIVE ENGINEERING CHECK | N639/N767、时间S128和L10分别检查；非收敛定理 |
| 同参数静态谱与热谱几乎相同 | ADVERSE MECHANISM CONTROL | 不能主张改善依赖时间排序；未另行优化静态族 |
| 高编号仍随N明显变化；N767的301–320 MAPE1.444500% | POSITIVE FINITE VALUE / STABILITY OPEN | 同窗口N639仍33.130404%、N511168.369299%，不能只报告最有利N |
| 动态起点由同一连续a(u)提供 | DEFINITION | a(0)=a_start，中点离散本身不含端点 |
| 绝对原点固定，但m同时提供偏置与形状拟合容量 | DECLARED DESIGN LIMIT | 不减量子基态，不隐瞒监督目标 |
| 内生素数、可容许性、primitive/repetition、roof与轨道迹 | OPEN / NOT SUPPLIED | 不能由曲线相似或有限自伴性推出 |
| 无限全谱、收敛、RH或唯一自然机制 | NOT CLAIMED | 后验2%线仅工程诊断 |

四形式ID：`CS06-Q-NONREL-HEAT`、`CS06-R-REL-HEAT`、
`CS06-S-SEXTIC-HEAT`、`CS06-E-COSH-HEAT`。
Same-object边界保持，各矩阵、势、能量、尺度均归属同形式与参数。
Portfolio：advance低100点有限S基准；停止时间排序优势与高320点收敛推广。
冻结卡是执行前契约，不覆盖为执行后结果；没有继承其他对象的算术信用。
A0/A1/A2/T0–T3 NOT EVALUATED；formal UNASSIGNED；B NOT INVOKED。
