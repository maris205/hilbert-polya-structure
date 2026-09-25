# 265 — 固定 Hénon 拉回振子截断审计

Scope ID: `ASFS-DISCOVERY-20260919-CS15`。

Current status: `COMPLETE; FINITE-320 STABILITY MET; LOW-INDEX SHAPE ERROR PERSISTS`。

固定2640028的h、κ及3/2幂，完整双奇偶谱在n64/80/96及两个额外
基宽下通过全部冻结有限稳定门。预定n96/ρ1全320 MAPE1.111009%，
低于旧B3.525125%；首百最坏误差9.568466%仍在，旧264联合失败保留。
真实连续残差最大从n52的0.368640降至n96的0.000642061，但没有连续
第j谱值或归一化320态误差证书。零新优化、零新目标。
单次193.213秒、24分解、exit0；保存48NPZ/103科学文件并ANALYZED，
264旧185文件原SHA保全。241/242暂停。同对象不变；无Route信用。

- [完整记录](paper.md)
- [当前结果卡](result-card.md)
- [计算前冻结卡](candidate-card.md)
- [执行合同](execution-card.md)
- [声明台账](claim-ledger.md)
- [输入字节锁](input-locks.json)
- [证据索引](evidence/README.md)
- [独立保存审查](evidence/saved-output-review.md)

Portfolio: **advance有限固定参数320态稳定基线；停止旧联合成功、连续
索引认证与算术机制晋升**。本轮结束；继续时需另冻针对低指标误差的
合同，不在本轮加算。A0/A1/A2/T0–T3 NOT EVALUATED，formal UNASSIGNED，B NOT INVOKED。
