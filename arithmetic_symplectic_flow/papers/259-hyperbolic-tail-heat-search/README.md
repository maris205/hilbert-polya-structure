# 259 — 归一化双曲势尾热谱搜索

Scope ID: `ASFS-DISCOVERY-20260919-CS09`。  
Status: `COMPLETE; MODEST BASELINE REFIT; NO HYPERBOLIC GAIN`。

接续258的Q0107有限基线，冻结B原五次/六次势重拟合、E偶双曲尾、
X奇偶双曲尾。两新族保持六阶jet，κ=0精确回到母体；不是首次提出cosh。
保持完整冷却热乘积、自有连续最低值和绝对能量读出，不换静态代理。
三族各9种子+32优化调用已完成：123成对调用、120唯一成员，249传播/完整
SVD、14静态读出，退出码0，约251秒。没有追加运行或新目标，优化器均预算耗尽。

主赢家B0055仅为原多项式重拟合，训练max M/W=1.695274%/5.234299%，
J=.997117。E/X均退回κ=0，严格J<1的3.6e−13差只是舍入，不是双曲增益。
B/N1279四窗MAPE为1.695274%/4.222825%/5.697383%/3.525125%，旧Q全320
为3.567910%。细空间对、时间和箱宽G<2%，粗639→1023全320 G=53.452999%
仍失败；热/静态G=6.221975e−8%，没有非自治优势。

精确势/根结构已独立审查；经典体积动机不是量子Weyl定理。保存数值
按ANALYZED报告，不是独立完整复现。组合：有限advance保留B微调基线，
stop双曲增益推广，后续fork；不继续调当前分支。原冻结卡不改写，当前
状态见[结果附卡](result-card.md)。所有1–320目标均历史已知。
A0/A1/A2/T0–T3 NOT EVALUATED，formal UNASSIGNED，B NOT INVOKED；241/242暂停。

[论文](paper.md) · [候选卡](candidate-card.md) · [执行卡](execution-card.md) ·
[结果附卡](result-card.md) · [声明账本](claim-ledger.md) · [证据](evidence/README.md)。
