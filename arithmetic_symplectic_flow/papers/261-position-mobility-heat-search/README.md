# 261 — Hénon导数轮廓与空间动能热谱

Scope ID: `ASFS-DISCOVERY-20260919-CS11`。  
Status: `COMPLETE; NO POSITION-MOBILITY GAIN; ZERO-PARAMETER BASELINE RETAINED`。

本轮研究空间迁移率合同动能R K0 R，区别于260的酉相位剪切。
保留旧势、Logistic冷却与首点尺度，只新增一个全局κ；B母体单独重拟合。
唯一运行exit0：44对调用/42独特成员，96传播/full SVD、50动能和10静态
分解，约141秒。M0002选回κ=0及旧四参数，J−1≈−6.25e−12只是稠密/DST
舍入差，不算结构或拟合改善；16个非零κ成员的最佳联合J仍为1.065845。

M/N1279四窗MAPE为1.695274%/4.222825%/5.697383%/3.525125%，同旧基线。
细空间/时间/箱宽四窗工程线通过，粗639→1023 full320 G53.452999%失败；
热/自身静态G6.25757e−8%仍近同。Z/F仅引用κ0的同一已有对象，不是
两次独立消融。组合位置：**保留有限实现控制；stop空间动能收益推广；fork**。
本包范围完成，不追加调参。保存输出分析不叫独立完整复现。

[完整论文](paper.md) · [冻结候选卡](candidate-card.md) ·
[执行卡](execution-card.md) · [声明账本](claim-ledger.md) ·
[结果卡](result-card.md) · [证据](evidence/README.md) · [输入锁](input-locks.json)。

有限监督发现不构成内生算术、可信A−1或Route结果。
A0/A1/A2/T0–T3 NOT EVALUATED；formal UNASSIGNED，B NOT INVOKED；241/242暂停。
