# CS10 — 输入、审查和执行证据

Scope ID: `ASFS-DISCOVERY-20260919-CS10`。  
Status: `COMPLETE; LOW-WINDOW ORDER EFFECT; NO ROBUST FIT GAIN`。

## Material Passport

- Origin Skill: academic-research-suite / experiment-agent
- Origin Mode: one bounded run → saved-output analysis
- Origin Date: 2026-09-19
- Verification Status: ANALYZED — NOT INDEPENDENTLY RERUN
- Version Label: exp_result_v1

[候选卡](../candidate-card.md)、[执行卡](../execution-card.md)在证明审查与
数值前冻结。[24项输入锁](../input-locks.json)保留259原17项依赖并核验
不变，加入本包两卡、259纯数学helper、B0055身份/两训练网格/细网格数组。
不运行旧main，不修改旧globals、卡或输出。

[形式审查](form-review.md)、[独立代码审查](code-review.md)和
[最终实现冻结](implementation-freeze.md)均在科学运行前完成，并由主控
全文读回。作者和审查者只做AST、纯导入、日志/元数据接口检查，没有
科学预演；六个数值控制均计入正式预算。最终runner797行SHA为
`7e71e4df43739edc854ada54c196ac1cc6d0123dfbe2efdec39000cc0ff0e395`。

## 唯一执行与保存证据

主控实际执行[执行卡](../execution-card.md)一次，父进程观察exit0。
[执行回执](execution-receipt.json)：PID75584，01:55:24至02:01:01 UTC，
最终序列化前337.158777秒，RSS峰值452900KiB=442.29MiB；342文件共
589825230字节。没有异常、补跑、安装/GPU、目标生成或外部发布。

54成对调用=52唯一成员+2缓存调用；104训练+6小控制+6赢家后检+4探针
=120传播/full SVD；11静态分解。所有52成员有效、全部冻结角色完整。
两个优化器均maxfev20预算用尽，不能称收敛。未用缓存节约增算。
24输入哈希、源码及赢家身份结束时匹配；600秒、124传播/11静态及
1GiB输出上限未超出。原始机器输出的UNVERIFIED字样保持不改，它并未
宣称独立复现；保存数据分析不能把它改成VERIFIED。

| 证据 | 内容和限制 |
| --- | --- |
| [manifest](run-1/manifest.json)、[result](run-1/result.json) | 命令、实际环境、哈希、角色/计数/完整指标 |
| [events](run-1/events.jsonl)、[calls](run-1/calls.json) | 实际日志和54调用；尝试/完成/保存分列 |
| [控制1](run-1/control-1-free.json)、[控制4](run-1/control-4-constant.json)、[控制5](run-1/control-5-transport.json)、[控制6](run-1/control-6-reverse.json) | 六控制全通过；有限代数null，不算机制收益 |
| [默认回归](run-1/default-regression.json) | 旧B0055双训练N预测差最大6.253e-12，M/W差最大2.567e-13 |
| [身份冻结](run-1/winners-frozen.json)、[训练数组冻结](run-1/training-arrays-frozen.json) | 两角色、16文件哈希；先冻再解析已知开发目标 |
| [拟合](run-1/development-fit-metrics.json)、[比较](run-1/comparisons.json)、[逐点CSV](run-1/points.csv) | 26对象四窗和8320数据行，含所有不利粗高段 |
| [raw机制比较](run-1/mechanism-comparisons.json)、[机制门](run-1/mechanism-verdict.json) | 左侧原能量分母，不含目标/尺度；两高窗口未通过 |
| [最低值账本](run-1/minimum-ledger.json) | 2368标量最低值求解、5092 Brent返回；浮点非区间认证 |
| [文件清单](run-1/file-inventory.json) | 341文件大小/SHA，不含清单自身 |

完整保存14热角色的C、全sigma/E/mask与前320复数左右态，11静态角色
的Havg/全lambda/前320态；六小控制另保存全63态。104紧凑训练网格
不保存C/态/完整G表，重建需要另运行冻结代码，本轮没有做这种重跑。

## 结果与保留的负面证据

全局S0038只新增lambda=.036，其余四参数同B默认，训练M/W=
1.695149773%/5.226750927%，J=.999926845262。B保持旧默认，无重拟合提升。
S/N1279全320 M3.531779%比B3.525125%差；自身静态几乎相同，G8.2531e-8%。
128中点引起前100 M变化0.000205146个百分点，超过训练M改善0.000124017
个百分点。没有匹配B128，不能宣称严格反转，但稳健拟合增益未建立。

S细空间/时间/扩箱工程线通过，粗639→1023全320 G53.446904%仍失败。
固定S06顺序Delta低窗/全窗为1.09765e-5%，高窗分别9.58985e-7%和
4.06925e-7%，均未过1e-6%线。全窗通过由低窗最大值主导，不转授高窗。
固定S06全320拟合约5.34725%，不能救S0038的拟合门。

当前主控已只读提取完整角色、计数、四窗结果、控制和诊断。S/N1279
左右态相对方程残差约1.77e-15/1.94e-15，正交Frobenius误差约5e-14；
S06相位网格上界约.456944，S主细网格约.0219333。这些仅为有限诊断，
不证明全尾相对精度、连续相位无混叠或空间收敛。
[独立保存输出审查](saved-output-review.md)已完成，无内部不一致；主控
全文读回132行报告和[最终只读检查器](../check_saved_outputs.py)。报告SHA
为`7bfdf8467a210f79d06675c6a61eb9897535ed1fa97ea1f502c1fecbe3fc758c`，
检查器SHA为`91048ea42e764f5ea60e9c4e3a5d4cd6d9cc77d9567fe5a582b1d04209ffd7da`。
最终检查器实际exit0、failures为空；在首版通过后只补入theta和旧B回归
再执行最终版，均为保存证据复核，非科学补跑。

全部124热NPZ（含4重复训练赢家）、11静态和8320逐点行检查完成；
104拟合窗口、96一般比较窗口和16机制比较窗口的数值均重算一致，
拟合/J/Delta/epsilon差为0。24输入、16训练冻结文件及341清单项匹配。
复数方程最大正向/伴随残差6.340e-15/5.236e-15，静态方程4.698e-12，
静态定义矩阵代数重构差0；不由此认证未保存的非赢家C/态或全尾精度。
主控还将原100目标NPZ及五份开发JSON逐项解析，与保存的320目标完全
相同；没有重新生成零点。全部检查是交叉覆盖的内部一致性验证，不是
相应数量的独立实验，也不是独立完整复现。最终机械QA见[回执](final-qa.md)。

主稿及result-card/README/claim-ledger已另经有界文字回读：与结果JSON
一致，未发现结论尺度阻断。该回读不代替保存数组复核。

组合决定：保留有限低窗口顺序控制；stop稳健拟合/非自治优势推广；fork。
原预算已完，不重选赢家、不追加调参；241/242暂停，所有Route坐标未评价。

## 外部方法来源

只核对[SciPy DST-I官方文档](https://docs.scipy.org/doc/scipy/reference/generated/scipy.fft.dst.html)
的定义/归一化，以及[NumPy SVD官方文档](https://numpy.org/doc/stable/reference/generated/numpy.linalg.svd.html)
的复数分解和Vh convention，不作新文献新颖性/算术结论。
主控另只读检查已安装SciPy的`scipy.fft._pocketfft.realtransforms._r2r`
源函数：复数输入的实虚部分别接受相同实变换。没有执行数值基准。
网上页面版本可能不同于本地；实际环境版本以正式manifest为准。

## 方法解释边界

确定性有限矩阵与已知目标不构成随机样本；无p值、显著性或概率推广。
需要分别保留四窗口、粗细网格、各族全部访问成员和三种问题的不同结果。
跨轮目标暴露、选择自由度、未另训静态、没有假目标等预算控制与无限
精度证据，均已在最终记录中明确。模型辅助内部审查不是外部同行评审。

## 方法谬误覆盖：11/11

解释等级CAUTION。以下是确定性探索的适用性核对，不制造p值、多重检验
修正、置信区间或总体因果效应。热参数β不是统计回归系数。

| 类型 | 本包处理 |
| --- | --- |
| Simpson | 四窗、粗细网格和原能量/归一化预测分报，不以总均值掩盖局部失败 |
| Ecological | 有限谱整体指标不推出每点恒等、无限谱或算术来源 |
| Berkson | 只描述有限访问成员；不从赢家样本推断全参数族 |
| Collider | 没有因果调整模型；有效性筛选不构成因果证据 |
| Base rate | 没有概率诊断；单次胜出不转为总体成功率 |
| Regression to mean | 历史最优参数继续搜索只是有限探索，不当作随机前后测效应 |
| Survivorship | 全调用、无效与预算终止、粗网格失败和负结果均保留 |
| Look-elsewhere | 两族/54对上限及跨轮历史探索明示，不声称选择后的显著性 |
| Forking paths | 定义、预算、角色和门预冻；历史已知目标仍使跨轮设计具有探索性 |
| Correlation/causation | 拟合、相对母体收益和顺序效应三栏分开；静态未另训 |
| Reverse causality | 目标影响设计和历史参数；raw D不含目标也不使探针参数变成目标独立 |

实质限制仍是监督与选择自由度、PROVES_TOO_MUCH控制缺失及仅有限分辨率。

[论文](../paper.md) · [声明账本](../claim-ledger.md)。
