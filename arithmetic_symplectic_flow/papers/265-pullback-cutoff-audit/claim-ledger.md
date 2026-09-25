# CS15 claim ledger

Scope ID: `ASFS-DISCOVERY-20260919-CS15`。

Current status: `COMPLETE; FINITE-320 STABILITY MET; LOW-INDEX SHAPE ERROR PERSISTS`。

| Claim | Status | Evidence / limit |
| --- | --- | --- |
| 连续对象及h、κ、固定3/2读出不变 | FROZEN | [卡](candidate-card.md)，2640028；不是新优化 |
| 两个y奇偶块带重数合并等于完整S_n谱 | EXACT LOCAL DERIVATION | [正文§2](paper.md)；q不分块 |
| padding每轴+4捕获S V_n的完整作用 | EXACT LOCAL DERIVATION | [正文§3](paper.md)；先链后截取 |
| r²=r_in²+r_out²；精确dist(λ,spec S)≤r | EXACT LOCAL DERIVATION | 正交分解及谱展开；不定位第j |
| 全部冻结四比较/四窗G<2% | FINITE OBSERVATION — MET | [结果](evidence/run-1/result.json)；64→80、80→96及两宽度，无重选 |
| 主n96/ρ1 MAPE320=1.111008714% | FINITE OBSERVATION | 优于旧B3.525124952%；不是首百/逐态全面胜出 |
| 低指标形状误差仍在 | PRESERVED NEGATIVE | W100=9.568465737%，M100=1.861861241%也不及旧B |
| 最大观测r从n52 .368640降到n96 .000642061 | FLOATING DIAGNOSTIC | 非外向舍入、非第j误差证书、非K向量残差 |
| 24次分解、零优化/额外科学、103科学文件完整 | EXECUTED; SAVED EVIDENCE ANALYZED | [实际回执](evidence/execution-receipt.json)及[检查stdout](evidence/saved-analysis-stdout.txt)；非独立重跑 |
| 内外监控严格≤30秒 | NOT MET AS STRICT CADENCE | 内部实际间隔约30–49秒、外部约27–34秒；正常关闭，无超时 |
| CS14联合门失败 | PRESERVED NEGATIVE | 旧结果卡只读，不能追认 |
| 连续第j谱值/320归一化误差认证 | OPEN | 双精度残差、G门均不提供此证书 |
| 自然算术、prime符号、roof、primitive/重复/算术迹 | NOT SUPPLIED | 没有从监督目标反推机制 |
| A0/A1/A2/T0–T3 | NOT EVALUATED | formal UNASSIGNED，B NOT INVOKED |

模型审查是内部辅助；科学运行与保存数组ANALYZED分开记录，不假称独立重跑。
Portfolio: **advance有限稳定基线；stop更强联合/连续认证/算术晋升**；
不改旧卡、不追加科学预算，不据有限结果排除或认证整个家族。
