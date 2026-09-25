# 257 — 高模截止与次序作用审计

Scope ID: `ASFS-DISCOVERY-20260919-CS07`。  
Status: `320-MODE FINITE STABILITY MET; TINY ORDER EFFECT; FIT BENEFIT NOT ESTABLISHED`。

固定256的S0047参数，审核原beta=.02下的N/时间求积/箱宽变化，
另以64个相同样本的奇偶排列及beta=.20局部细分检查次序作用。
不训练、不换主成员、不生成新目标。单次运行完成11传播和5个静态分解，
约163.70秒，退出码0，未重试；全部角色通过有限矩阵有效性线。

结果：N1023/1279/1535的全320相邻G约5.70e−12%/1.08e−10%；
时间求积与箱宽G约.001951%/8.84e−11%，均低于冻结2%工程线。
主诊断A3的前100/101–300/301–320 MAPE为2.050747%/4.366299%/
5.901961%，全320为3.738668%。旧N767的尾段1.444500%没有保留，
其至N1023的全320 G为6.719311%；不把旧有利分辨率当作稳定结果。

beta=.20原序/奇偶序的全320差约5.510180e−6%，超过冻结工程检测线，
但301–320窗口为8.740832e−7%，仍UNRESOLVED。原beta=.02的次序差
仅5.515712e−8%，未做该beta的细分比判别。静态对照仍近似相同，
小次序效应不构成有实质量级的拟合收益。

Portfolio：**advance有限320项基准；stop旧尾段好成绩和次序收益的
推广。** 下一步若继续，应另冻结有效势/色散构造，并以此稳定残差作
对照；本包不追加N、beta、优化或目标窗口。无限谱收敛与算术身份OPEN。

所有1–320目标已经观察；本包不是新盲测。A/B控制和静态对象分别归属，
不把较大beta的效应转移到原低谱拟合。A0/A1/A2/T0–T3 NOT EVALUATED，
formal UNASSIGNED，B NOT INVOKED；241/242继续暂停。

[完整记录](paper.md) · [冻结候选卡](candidate-card.md) ·
[执行卡](execution-card.md) · [声明账本](claim-ledger.md) ·
[输入锁](input-locks.json) · [证据记录](evidence/README.md) ·
[实际结果](evidence/run-1/result.json) · [保存结果审查](evidence/saved-result-review.md)。
