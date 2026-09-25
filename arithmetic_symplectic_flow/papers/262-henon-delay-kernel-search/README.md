# 262 — 直接Hénon延迟转移核

Scope ID: `ASFS-DISCOVERY-20260919-CS12`。

Status: `COMPLETE; NO DELAY-KERNEL FIT GAIN; FINE-320 READOUT INVALID`。

本轮从二步递推本身定义有限周期随机核，比较自治A与四步冷却D。
每轴n格、总维n²，保留延迟状态和完整非平凡奇异谱；只剔除经检查的
唯一守恒常数模，不借旧热模型的质量或能量偏置。首末系数可能只在
连续对应的酉端点中出现，因此预定END采样归因控制与去二次源消融。
两卡和14项输入冻结后完成唯一运行：51对调用/45唯一成员，106次前向
及完整SVD，退出0；六项小控制通过，没有重跑或新目标。

主A0033的n23/n27训练MAPE=5.480690%/4.820761%，J=6.584580>1；
D0045更差。粗格G超2%，A/D n39/n47和两个END均未通过预定320态
分辨率门，正式四窗指标保留null。END全sigma近同不等于归因门通过。
保存证据已分析，原始284文件保留；不以执行成功代替发现成功。

Portfolio：**保留有限实现/解析控制；stop拟合改善与细格320态推广；fork**。
停止本卡追加调参，不排除整个架构。详见[结果卡](result-card.md)。
有限监督发现不构成内生算术或可信A−1；A0/A1/A2/T0–T3 NOT EVALUATED，
formal UNASSIGNED，B NOT INVOKED；241/242暂停。

[论文](paper.md) · [候选卡](candidate-card.md) · [执行卡](execution-card.md) ·
[声明账本](claim-ledger.md) · [输入锁](input-locks.json) · [证据](evidence/README.md)。
