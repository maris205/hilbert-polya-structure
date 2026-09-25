# CS10 — 声明账本

Scope ID: `ASFS-DISCOVERY-20260919-CS10`。  
Status: `COMPLETE; LOW-WINDOW ORDER EFFECT; NO ROBUST FIT GAIN`。

| 声明 | 类别 / 当前状态 | 证据与边界 |
| --- | --- | --- |
| 逐步G A G*保持正定和瞬时谱 | 有限矩阵代数 | 论文§2；不保证完整乘积同谱 |
| 恒定相位/纯传输/整对全逆序保持完整奇异谱 | 有限矩阵恒等式 / 控制通过 | 论文§2、run-1六控制；不是新机制收益 |
| 同参数静态平均须共轭K | 同对象定义 | 不等于旧K+mean W；不另训 |
| 整对排列与同段细分保留Havg | 有限代数 / 保存检查通过 | 固定探针样本与归一化重数一致，1静态owner |
| S前100监督拟合改善 | 有限极小改善 | lambda=.036，J=.999926845262；B仍旧默认 |
| 稳健/整体剪切拟合收益 | NOT ESTABLISHED / 不利证据 | 开发和全320变差，时间求积变化超过微小M优势 |
| S非自治拟合优势 | NOT ESTABLISHED | 自身热/静态G8.2531e-8%，静态未另训 |
| 固定S06顺序效应 | 有限低窗口RESOLVED | 1–100与其主导的1–320通过，两个高窗UNRESOLVED |
| 细空间/时间/箱宽G<2% | 有限工程线通过 | 粗高段失败仍保留；不证明无限收敛或极小增益稳健 |
| 内生算术、prime-symbolic自然性、RH谱认同 | NOT ESTABLISHED | 未供应所需对象 |
| PROVES_TOO_MUCH与盲测 | OPEN / NOT AVAILABLE | 全部1–320目标历史已知 |
| 独立完整复现 | NOT RUN | 内部保存审查不等于VERIFIED |

同对象账本分离B/S、静态和算法null。A0/A1/A2/T0–T3 NOT EVALUATED，
formal UNASSIGNED，B NOT INVOKED；241/242暂停。
当前原预算执行完毕，不追加搜索。组合决定：保留有限低窗口顺序控制，
stop稳健拟合/非自治优势推广，后续fork；微小机制效应不救拟合或算术门。

[论文](paper.md) · [冻结卡](candidate-card.md) · [证据](evidence/README.md)。
