# 264 — 单步 Hénon 拉回振子

Scope ID: `ASFS-DISCOVERY-20260919-CS14`。

Current status: `COMPLETE; FINITE-320 FIT SIGNAL; JOINT AND ROBUSTNESS GATES FAIL`。

直接从F_a(q,p)=(1−aq²−p,q)及其逆拉回酉算子构造正振子混合形式。
精确约化只留下h、κ=η(1−η)a²两个谱参数；预先固定3/2幂读出，
不加地板、不减基态、不挑奇偶扇区。这个幂是密度导向工程选择，
不是自然量子化或算术来源。

形式定义、相体积推导和Hermite完整压缩见[全文](paper.md)，当前状态以
[执行后结果卡](result-card.md)为准；计算前卡保持冻结字节。

一次66次全分解运行exit0，30对调用/29独立点。赢家0028在n52的全320
MAPE为1.149170%（旧B3.525125%），但J=1.856056>1，前100最坏误差9.568466%。
两细截断全320 G为12.534604%/2.314617%，基宽差3.025945%，均失败。
三小控制/SOURCEOFF通过；保存数组分析ANALYZED，无独立科学重跑。
同对象ledger保持独立；A0/A1/A2/T0–T3 NOT EVALUATED，formal UNASSIGNED，
B NOT INVOKED；241/242继续暂停。

- [计算前冻结卡](candidate-card.md)
- [预审澄清v1a](pre-execution-clarifications.md)
- [执行合同](execution-card.md)与[16项输入锁](input-locks.json)
- [主张台账](claim-ledger.md)
- [证据索引](evidence/README.md)

当前决定：**保留解析构造及有限拟合信号；停止稳健增益晋升；fork**。
没有追加调参/改幂/删态/新目标；不把冻结门失败变成全族无效结论。
