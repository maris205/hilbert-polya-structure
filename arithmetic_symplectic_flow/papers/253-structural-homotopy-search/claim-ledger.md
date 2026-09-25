# CS03 声明账本

**Scope ID:** `ASFS-DISCOVERY-20260919-CS03`。  
**Current status:** `STRUCTURAL SEARCH COMPLETE; BASELINE SUBFAMILY RETAINED`。

| 声明 | 状态 | 范围/限制 |
| --- | --- | --- |
| 五个结构变形明确构造并实际搜索 | ESTABLISHED / FINITE EXECUTION | 三个活动参数；固定继承的alpha；无逐点校正 |
| J四阶局部结构及R端点/单调保持 | 解析核对成立 | 不推导算术源或拟合优势；J中间值仍有接缝 |
| 285调用、276训练前向和2网格前向完成 | EXECUTED / exit0 | 9缓存；一次运行；无重试 |
| 新实现默认点重现252 | 数值回归控制通过 | 首100预测/MAPE差均0；不是无限维谱证明 |
| 最低训练MAPE降至2.2717925658% | 有限监督观察 | 比2.2752254884%低0.0034329226百分点 |
| 六次项或其他新增项带来本轮最低MAPE | NOT SUPPORTED | 所有胜者lambda=0；S胜者只微调原hbar/a_start |
| 所有非零新增项在每个指标都更差 | FALSE / NOT CLAIMED | Q/S非零成员最大百分比误差较低；不改预定MAPE选优规则 |
| 整体预测/间距/MSE同步改善 | 本次结果不成立 | 两后续窗口、MSE与间距均未改善 |
| 网格稳健或可信A−1候选已建立 | NOT ESTABLISHED | N260/280百点MAPE54.89668%/41.03726% |
| 五个优化器收敛或全局最优 | NOT CLAIMED | 全部maxfev40耗尽；有限预算不能否定全族 |
| 151–200为历史盲检验 | NOT CLAIMED | 本轮选择前未生成；旧Logistic已有更长目标使用 |
| A0/A1/A2/T0–T3；formal；B | NOT EVALUATED；UNASSIGNED；NOT INVOKED | 仅构造发现层，不积累算术门信用 |

Portfolio fork后续不同结构；保留原模型子族最佳训练成员及旧比较基线，
不依据冻结后评价回写训练胜者，不将小幅MAPE变化包装成结构突破。
