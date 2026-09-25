# 258 — 势形状与对数色散热谱搜索

Scope ID: `ASFS-DISCOVERY-20260919-CS08`。  
Status: `FIXED REPAIR COMPLETE; FINE-320 STABILITY MET; STATIC NEAR-IDENTICAL`。

在257的稳定S0047基准之后，构造O八次势、Q五次不对称势、U对数增强
动能、D对数减速动能，并给原B形式同调用预算重拟合。每族实际计算
完整非自治热路径，不用静态代理；连续最低值归属于各自势。

完成165次成对调用、160个唯一成员、320次训练传播及3次解析控制。
N511/N639共同选择的主赢家`CS08-Q-QUINTIC-0107`保留非零五次项
z=−.003159505004882813；两个训练网格的最大MAPE1.709232%、
最大最坏误差5.249433%，J=.833468。相对旧基准2.050747%/6.351622%
及本轮B重拟合1.957695%/5.474616%，两项均降低。

原run-1在赢家身份冻结后、完整矩阵保存前因日志参数`name`冲突退出，
退出码1，未自动重试。用户随后批准修复：单次固定补跑退出码0，完成
十个训练矩阵重建和十二个原定后检，22传播/22 full SVD/22静态读出，
零优化、零新目标。原815文件逐字节保留，十个原选择谱/预测和Q主身份
不变；全sigma重建最大差3.775e−15。新结果共101文件、478484239字节。

| Q0107，N1279 | 1–100 | 101–300 | 301–320 | 1–320 |
| --- | ---: | ---: | ---: | ---: |
| MAPE% | 1.709232 | 4.277943 | 5.760972 | 3.567910 |
| 旧S0047 MAPE% | 2.050747 | 4.366299 | 5.901961 | 3.738668 |

Q四窗口MAPE和最坏误差亦优于本轮B。其N1023→1279、时间64→128中点、
扩箱L8→10的全320 G分别为7.977e−12%、.001662738%、4.142e−11%，
满足预设2%工程线。但N639→1023的全320 G=52.903616%，粗网格尾谱
仍失败；N1023高动量区占据也未全消失，不作无限收敛推论。
Q的热/同参数静态全320 G仅5.949e−8%，未显示实质非自治拟合收益。
三个原解析控制及母体双回归通过且未重跑；五个优化器均预算终止未收敛。
O是训练M/W取舍，U/D赢家均z=0；B/O/U/D的全320 MAPE均未优于旧S。

B三活动参数，新族四活动参数，等调用不等容量。小训练G不是独立
验证，也未继承旧S的稳定性；本次后检属于Q自己的固定对象。
原脚本、冻结卡及旧输入不修改。所有1–320目标此前已知，不是盲测。

用户已批准修复：[恢复执行卡v2](repair-execution-card.md)与
[恢复输入锁](repair-input-locks.json)保持五个赢家参数和原Q主身份，
已仅重建十个训练矩阵并补齐十二个后检，全部完成。
组合位置：advance Q作为细网格有限320改进基线；stop粗尾谱、热优越性
及无限收敛推广。本次修复范围已完成，不自动开启新结构/搜索。
Same-object账本独立。A0/A1/A2/T0–T3 NOT EVALUATED，formal UNASSIGNED，
B NOT INVOKED；241/242保持暂停。无新零点生成、发布、上传或PDF。

[完整记录](paper.md) · [冻结候选卡](candidate-card.md) ·
[执行卡](execution-card.md) · [输入锁](input-locks.json) ·
[声明账本](claim-ledger.md) · [证据记录](evidence/README.md) ·
[形式审查](evidence/form-review.md) · [执行前代码审查](evidence/code-review.md) ·
[失败回执](evidence/launch-receipt.json) · [冻结训练赢家](evidence/run-1/winners-frozen.json) ·
[原保存结果审查](evidence/saved-result-review.md) ·
[修复代码审查](evidence/repair-code-review.md) ·
[补跑回执](evidence/repair-launch-receipt.json) ·
[完整补跑结果](evidence/run-2-fixed/result.json) ·
[补跑保存复核](evidence/repair-saved-result-review.md)。
