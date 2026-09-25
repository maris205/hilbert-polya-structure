# CS07 — 声明账本

Scope ID: `ASFS-DISCOVERY-20260919-CS07`。  
Status: `320-MODE FINITE STABILITY MET; TINY ORDER EFFECT; FIT BENEFIT NOT ESTABLISHED`。

| ID | 声明 | 证据类型 / 当前边界 |
| --- | --- | --- |
| C01 | S0047固定theta、能量原点、首点规则不变 | 两卡及15项哈希锁；非重新拟合 |
| C02 | 每样本连续r次保持该样本总时间beta/64 | 有限乘积定义；不是重采样或全序列循环 |
| C03 | A1与B1–B5共享相同H_avg | 相同N/L/样本/权重的精确恒等；不同beta热算子仍不同 |
| C04 | 全反序奇异谱相同；奇偶排列无此保证 | 段矩阵对称、乘积转置；不预判数值效应 |
| C05 | 空间/时间/箱宽四窗口诊断均过全320的2%工程线 | FINITE NUMERICAL；最大为时间.001950947%；不证明连续极限 |
| C06 | beta.20次序差在1–100、101–300、1–320过检测线，301–320未过 | FINITE NUMERICAL；全320 Delta20=5.510180e−6%，epsilon=4.360177e−9%；非严格误差认证 |
| C07 | 解析控制通过，11传播/11SVD/5静态按预算完成 | ACTUAL RUN，163.698625秒，exit0，全部VALID，未重试 |
| C08 | 稳定尾段MAPE约5.901961%，旧N767的1.444500%不稳定 | ADVERSE FINITE RESULT；N767→A1的全320 G=6.719311%，全部旧行保留 |
| C09 | 主A3前100/全320 MAPE约2.050747%/3.738668% | DESCRIPTIVE，参数未重拟合；1–320全为已知目标 |
| C10 | 原beta热谱与同参数静态谱近似相同 | A3全320 G=7.402718e−8%；未建立排序拟合收益，不等于精确同谱 |
| C11 | 运行输出可作保存证据分析，尚无独立从头复现 | UNVERIFIED run / ANALYZED review；模型检查非外部同行评审 |

OPEN：连续全线谱与误差界、无限编号拟合、自然算术源、符号可容许性
保留、primitive/重复/roof、同对象迹公式。所有1–320目标已知，不能
重新称盲测；无同预算静态优化，不声称次序对拟合有因果贡献。

Same-object账本按卡分别冻结A原族、B次序/热时长控制及静态对照。
Portfolio：advance有限320项基准，stop旧尾段有利成绩/次序收益推广；
决定性理由是有限离散标准通过，而稳定目标残差和近似静态性仍保留。
A0/A1/A2/T0–T3 NOT EVALUATED，formal
UNASSIGNED，B NOT INVOKED；241/242保持暂停。

证据：[论文](paper.md)、[候选卡](candidate-card.md)、
[形式审查](evidence/form-review.md)、[执行与验证](evidence/README.md)、
[完整结果](evidence/run-1/result.json)、[四窗口比较](evidence/run-1/comparisons.json)。
