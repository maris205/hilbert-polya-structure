# 254 — 全局构造与双指标联合拟合

**Scope ID:** `ASFS-DISCOVERY-20260919-CS04`。  
**Current status:** `JOINT TRADEOFF IMPROVED; DUAL THRESHOLD UNMET`。

完成五个冻结形式：软幂动能、对数动能、位置势变形、交替驱动及
Hermite-DVR；285训练调用含272实际前向和13缓存，另完成两个主赢家
维度前向。主联合赢家A0226的训练MAPE为2.311219%、最差百分比误差
11.866756%，均好于共同起点的2.561938%/14.105397%。但历史最低MAPE
2.271793%未刷新，预定J=1.017355>1，双阈值未通过。

固定参数N260/280的MAPE仍为54.839782%/41.387553%。七个预定报告角色
对应六个不同成员；未来评价不重选主赢家，所有不利结果均保留。

[全文](paper.md) · [不可变搜索前卡](candidate-card.md) · [执行卡](execution-card.md) ·
[输入锁](input-locks.json) · [声明账本](claim-ledger.md) · [证据](evidence/README.md)。

Portfolio：**保留有限取舍对照，fork后续构造；stop稳健性升级**。
决定性原因是联合双阈值仍未达到且维度敏感性明显。不是可信A−1通过，
也不否定全部五个参数族。原241/242保持暂停。
A0/A1/A2/T0–T3 NOT EVALUATED；formal UNASSIGNED；B NOT INVOKED。
搜索前卡保留原freeze标签和哈希，当前执行结论以本页/全文/声明账本为准。
