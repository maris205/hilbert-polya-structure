# CS11 输入、执行与审查证据

Scope ID: `ASFS-DISCOVERY-20260919-CS11`。  
Status: `COMPLETE; NO POSITION-MOBILITY GAIN; ZERO-PARAMETER BASELINE RETAINED`。

## Material Passport

- Origin Skill: academic-research-suite / experiment-agent
- Origin Mode: bounded constructive run → saved-output analysis
- Origin Date: 2026-09-19
- Verification Status: ANALYZED — NOT INDEPENDENTLY RERUN
- Version Label: exp_result_v1

[冻结卡](../candidate-card.md)、[执行卡](../execution-card.md)和
[19项输入锁](../input-locks.json)先于科学运行。
锁定本轮定义、旧纯函数代码、旧B0055双训练/细网格数组、历史目标及
Hénon定义来源；不改旧模块globals、不调用旧main或优化器。

[形式审查](form-review.md)已完成，315行报告由主控全文读回，未发现
形式阻断；SHA为`d65d2fd83bb71ec487fa8626d4441b9fdcde953916f774d9dc7e48bbc3b63e58`。
[独立代码审查](code-review.md)已完成，主控全文读回167行；
[最终实现冻结](implementation-freeze.md)绑定输入、代码及审查SHA。
唯一正式进程于02:56:19 UTC启动，PID82157，02:58:39完成，主控观察exit0。
实际96传播/full SVD、50动能eigh、10静态eigh，均在冻结上限内。
不采用未登记的科学预演。模型内部审查不等于外部同行评审。

## 实际执行与证据索引

[执行回执](execution-receipt.json)记录实际命令、进程、退出码、约140.515秒
耗时、345252KiB峰值RSS及284文件/469558733字节。没有异常、超限、补跑、
GPU/安装、外传、目标生成或发布。44对调用=42独特成员+2缓存，两个优化器
各用尽16调用而未收敛；84训练+6控制+6后检=96传播。全部成员有效。

| 保存记录 | 覆盖 |
| --- | --- |
| [manifest](run-1/manifest.json)、[result](run-1/result.json) | 输入/环境/SHA、角色、计数与完整指标 |
| [events](run-1/events.jsonl)、[calls](run-1/calls.json) | 实际事件与44调用，attempted/completed/saved分开 |
| [身份冻结](run-1/winners-frozen.json)、[训练数组冻结](run-1/training-arrays-frozen.json) | B/M角色和16文件SHA；先冻结再解析已知开发数据 |
| [六控制之一：κ0](run-1/control-3-M-zero.json)、[默认回归](run-1/default-regression.json) | 六控制全过，默认B双N与旧预测/指标实际差0 |
| [四窗M/W](run-1/development-fit-metrics.json)、[比较](run-1/comparisons.json)、[逐点CSV](run-1/points.csv) | 全25报告对象、100拟合窗口及8000逐点行，包含别名和负面粗尾 |
| [结构判定](run-1/structure-assessment.json)、[消融别名](run-1/ablation-aliases.json) | κ0不能构成增益；Z/F引用同一来源不补算 |
| [最低值账本](run-1/minimum-ledger.json)、[文件清单](run-1/file-inventory.json) | 1792最低值求解、3796 Brent返回；非区间认证；清单排除自身 |

100个热NPZ包括96实际传播和4份训练赢家完整复制；16套完整C/K/P/Q
包含六控制和十正式热角色，另10套静态。非赢家没有完整C/K/P/Q/态；
25个报告对象包含4个热/静态消融别名，不能计为25次新实验。
原run文件的UNVERIFIED标记保持不改，分析层级由本索引与独立报告区分。

## 结果边界

M0002κ=0与B0001同四参数，是同一精确对象的两种浮点实现。
约10^(-11)个百分点的训练差及J−1≈−6.25e−12不是进步。
16个非零κ访问成员的最佳联合J仍1.065845，未过旧参考；不宣称全族无解。
N1279四窗MAPE仍1.695274/4.222825/5.697383/3.525125%，不是新的拟合基线。
细空间/时间/箱宽四窗G<2%通过；粗639→1023 full320 G53.452999%失败。
热/自身静态G6.25757e−8%近同，Z/F退化引用G0不证明轮廓特异收益。

独立[保存数据审查](saved-output-review.md)已完成，最终
[检查器](../check_saved_outputs.py)实际exit0且failures为空。它只读
NPZ/JSON/CSV，核对矩阵恒等式、保存态残差、指标和哈希，没有新科学求解。
覆盖42对训练、100热NPZ、16套完整矩阵/保存态、10静态对象、100拟合窗口、
100比较窗口、8000行CSV、19输入锁、16训练冻结文件及283清单文件。
原目标拼接、16个非零κ成员统计、冻结顺序及别名均相符。
主控全文读回109行报告及484行检查器；形式审查者另读结果正文/结果卡，
无实质修正。模型内部审查不替代独立重跑或严格数值认证。

| 最终审查文件 | SHA-256 |
| --- | --- |
| `saved-output-review.md` | `2a1c722d50de3e646798f99bd54594964531e2f593b9c5e191a08c998966bf4a` |
| `check_saved_outputs.py` | `4a69cf0d222392634e07d83cce289efb848c0acc6f583efcc44c5467e8f15299` |

[最终机械核对](final-qa.md)另记链接、状态一致性、冻结SHA及格式检查，
与科学运行和保存数组分析分开。

## 方法解释检查：11/11

等级CAUTION。本轮是确定性、历史已知目标上的有限探索，无p值、置信
区间、随机样本显著性或总体因果解释；以下核对适用性而非制造统计结论。

| 类型 | 处理与限制 |
| --- | --- |
| Simpson | 四窗及粗细网格分报，不能由低100或总指标覆盖高窗失败 |
| Ecological | 平均误差不能推出每点、全谱或算术恒等 |
| Berkson | 只描述访问集与赢家；不从16非零成员推出全族无解 |
| Collider | 无因果调整模型；有效门是数值筛选，不是因果证据 |
| Base rate | 无概率诊断；未从一次搜索给总体成功率 |
| Regression to mean | 旧最佳继续搜索不作随机前后测；κ0微差属实现差 |
| Survivorship | 全42成员、预算终止及粗网格负结果保留；无效数为0亦明确 |
| Look-elsewhere | 两形式44对以及历史多轮选择明示，不声称选择后显著性 |
| Forking paths | 当前定义/预算/读出预冻；跨轮数据暴露仍属探索性 |
| Correlation/causation | 胜B、胜F与非自治收益分离；别名不充作独立消融 |
| Reverse causality | 目标影响历史参数和设计；导数profile动机不恢复目标独立性 |

Portfolio：保留有限实现控制；stop空间动能收益推广；fork新机制。
冻结范围已完成，无继续优化；同对象记录完整，所有Route坐标未评价。

[论文](../paper.md) · [声明账本](../claim-ledger.md)。
