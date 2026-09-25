# CS11 最终结果卡

Scope ID: `ASFS-DISCOVERY-20260919-CS11`。  
Status: `COMPLETE; NO POSITION-MOBILITY GAIN; ZERO-PARAMETER BASELINE RETAINED`。

[候选卡](candidate-card.md)和[执行卡](execution-card.md)是保持字节不变的
计算前合同；本卡是计算后的状态，不反向修改冻结设计。

唯一运行exit0：44对调用、42独特成员（2缓存）、96传播/full SVD、
50动能eigh、10静态eigh，约140.515秒；284文件/469558733字节。

B0001保持旧四参数。全局M0002也保持旧四参数且κ精确为0，
paired max M/W=1.695273790050%/5.234299091561%，J−1=−6.2538863e−12。
这只是稠密/DST实现的舍入排序，不是训练或空间结构进步。
16个非零κ访问成员的最佳联合J=1.065845304，未过旧目标；不是全族无解。

M/N1279四窗MAPE=1.695274%/4.222825%/5.697383%/3.525125%，同旧基线。
细空间/时间/箱宽四窗G<2%通过，粗639→1023 full320 G=53.452999%失败。
热/自身静态G=6.25757e−8%；不声称非自治或顺序收益。
Z/F按κ0退化规则引用同一已存对象，G0不是两次独立消融实验。

同对象账本完整；形式、代码和保存输出的审查分层记录，不是同行评议或
独立完整重跑。可信A−1/内生算术/连续极限仍OPEN；A0/A1/A2/T0–T3
NOT EVALUATED，formal UNASSIGNED，B NOT INVOKED；241/242暂停。

Portfolio：**retain有限实现控制；stop空间动能增益推广；fork新机制**。
决定性理由是赢家κ0，不能将同一对象的浮点差当成新结构。范围完成，
不追加本包优化或重新选型。

[论文](paper.md) · [证据索引](evidence/README.md) · [声明账本](claim-ledger.md)。
