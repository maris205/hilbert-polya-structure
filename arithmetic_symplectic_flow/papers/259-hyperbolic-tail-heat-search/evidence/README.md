# CS09 — 输入、执行和复核记录

Scope ID: `ASFS-DISCOVERY-20260919-CS09`。  
Status: `COMPLETE; MODEST BASELINE REFIT; NO HYPERBOLIC GAIN`。

## Material Passport

- Origin Skill: academic-research-suite / experiment-agent
- Origin Mode: run → saved-output validation
- Origin Date: 2026-09-19
- Verification Status: ANALYZED — NOT INDEPENDENTLY RERUN
- Version Label: exp_result_v1

## Experiment Result

主控已且仅已执行[执行卡](../execution-card.md)中的一次命令。程序作者、
形式/实现审查者没有执行科学预演。执行前[形式审查](form-review.md)、
[实现审查](code-review.md)和[实现冻结](implementation-freeze.md)均完成；
运行内控制及预定全部角色完成，无异常或补跑。

[实际执行回执](execution-receipt.json)：PID67466，exit0；UTC00:38:13.604
至00:42:24.504，最终序列化前250.979183秒。RSS峰值341.39MiB；run-1共
677文件/417433771字节。123成对调用、120唯一成员/3缓存，240训练+1控制+
8后检=249传播及同数full SVD，14静态分解。三优化器各32评价用尽，均未收敛。
正式运行只用单线程CPU，未安装或使用GPU，未生成新目标。

[17项输入锁](../input-locks.json)包含新两卡、258的原/修复纯helper、256数学源、
旧Q训练/细网格数组及全部历史目标来源。旧对象保持只读，不能改写其卡或输出。
run-1排他创建；255传播/full SVD与14静态、600秒及1GiB硬上限均未超出。
原始输出中的`run_passport=UNVERIFIED`保留不改；它没有宣称独立重现。
本保存分析用ANALYZED，不能据此将原输出升级为VERIFIED。

## 保存结果与关键负结果

全局赢家`CS09-B-QUINTIC-REFIT-0055`，J=.997116989436；双训练N的
max M/W=1.695273790%/5.234299092%。N1279四窗MAPE为
1.695274%/4.222825%/5.697383%/3.525125%，旧Q全320为3.567910%。
这只提供原多项式基线小幅重拟合收益。E0002/X0003都κ=0，J−1约−3.6e−13
只是舍入，不能称双曲结构有益。

细空间对、时间和箱宽四窗均G<2%；B粗639→1023全320 G53.452999%失败。
B/N1279热静态G6.221975e−8%，不支持时间排序收益。全部既有开发目标均
观察过，没有盲测、假目标等预算控制或普适否定新族的结论。

| 证据 | 内容与限制 |
| --- | --- |
| [manifest](run-1/manifest.json)、[result](run-1/result.json) | 原命令、环境、输入锁、全角色计数/指标；不改写机器输出 |
| [events](run-1/events.jsonl)、[calls](run-1/calls.json) | 原调用与资源事件；120唯一成员均有效，缓存调用仍计预算 |
| [evaluation controls](run-1/evaluation-controls.json) | κ0精确嵌套、210项Decimal60比较，有限控制不是全箱证明 |
| [free control](run-1/free-kinetic-control.json)、[regression](run-1/default-regression.json) | 自由热核及旧Q双网格回归；全部在正式单次预算内 |
| [winners](run-1/winners-frozen.json)、[training freeze](run-1/training-arrays-frozen.json) | 身份先冻、24训练文件先冻，随后读开发数据，无重选 |
| [fits](run-1/development-fit-metrics.json)、[comparisons](run-1/comparisons.json) | 29对象四窗拟合、G、原E/E0/scale及热/静态比较 |
| [points](run-1/points.csv) | 29×320=9280逐点数据行，含不利粗高段 |
| [minimum ledger](run-1/minimum-ledger.json) | 6784连续最低值算法记录、分区/根/残差；浮点非区间认证 |
| [inventory](run-1/file-inventory.json) | 676文件SHA/字节数，不含清单自身 |

非赢家保存完整sigma/E/mask、路径/势/最低值索引，而不保存其完整C/态。
14热角色保存C、全sigma、前320左右态；14静态角色保存H、全lambda和
前320态。部分态不是完整重构，全尾mask不是相对精度认证。

## 保存输出验证

主控已只读提取角色、四窗指标、比较、计数、控制、资源及事件次序。
独立[保存输出审查](saved-output-review.md)已完成并由主控全文读回，
未发现阻断项；报告SHA-256为
`bd07cf9c8fc231c4595d7676b9fe7077fac16c8d3e76bfc323a422880a6434c2`。
676项清单文件的路径/大小/SHA逐项匹配，17输入锁及24训练冻结文件匹配。
原前100目标及五份开发参考纯解析后与保存目标逐项完全相同。全部训练
指标/排名、29对象四窗、28组比较及9280行CSV均由保存数组独立重算一致。
训练J的不同求和次序差最大3.55e−15，没有改变赢家或结论。

另复算保存态的方程、正交性、Frobenius矩和边缘/高动量占据；没有新
传播、求根、优化、SVD、eigh或目标生成。报告中的162034项断言只是
不同粒度且有交叉的记账，不是162034次独立实验或概率证据。

适用方法是比较保存的预测/能量/目标数组，用原冻结公式重新计算M/W/G，
核对全谱mask、形状、恒定参数、SVD状态诊断及身份/24文件冻结先于开发。
这属于保存证据内部一致性检查，不是重跑原实验或独立实现复现。

## 方法谬误覆盖：11/11

数据是确定性有限矩阵与已知目标的比较，不是概率样本；无p值、置信区间、
显著性或总体效果量结论。数值β是冻结热参数，不是统计回归系数。

| 类型 | 本结果的处理 |
| --- | --- |
| 1 Simpson | 所有四窗分报，粗/细N分报，不用总体均值盖住高段失败 |
| 2 Ecological | 有限网格整体误差不推出逐点恒等或无限谱性质 |
| 3 Berkson | 只描述访问的有限成员；不从赢家样本推断整个参数族 |
| 4 Collider | 无因果调整模型；冻结有效性筛选不当作因果证据 |
| 5 Base rate | 不涉及患病率/诊断概率；不能将一次胜出率当总体概率 |
| 6 Regression to mean | 无随机前后测效应估计；旧最优再拟合仅作有限重调 |
| 7 Survivorship | 120唯一成员、零INVALID及全部粗失败/κ0赢家均保留 |
| 8 Look-elsewhere | 三族/123调用及历史探索明示；没有选择性显著性声明 |
| 9 Forking paths | 单轮定义/预算/角色预冻；跨轮用已知目标设计仍属探索 |
| 10 Correlation/causation | 拟合小幅改善不归因为内生算术或非自治演化 |
| 11 Reverse causality | 目标影响结构设计，不反推结构自行产生目标 |

解释等级：CAUTION，有限探索性结果；不会为确定性误差计算虚构多重检验
p值修正。实质风险是跨轮设计自由度和PROVES_TOO_MUCH控制缺失。

## 外部来源核对

本轮只为平均密度动机核对Brent、Platt、Trudgian，
“Accurate estimation of sums over zeros of the Riemann zeta-function”，
Mathematics of Computation 90 (2021), 2923–2935，
[DOI 10.1090/mcom/3652](https://doi.org/10.1090/mcom/3652)，
[作者托管正式offprint](https://maths-people.anu.edu.au/~brent/pd/rpb276-MC-preprint.pdf)。
实际阅读范围为标题/作者/出版信息及§2（印刷2926页，式5–7与其说明），
支持N(T)主项和O(log T)余项；不声称读完全文或用户已读。
没有下载/复制论文，没有新生成零点数据，也不借该文证明本包的谱性质。
NIST DLMF25.10浏览仅作导航，未将其未列出的计数公式冒充该页直接证据。

## 验证边界

执行后只读重算指标、比较、计数、冻结次序及状态诊断；不得自动重跑。
结果分析标记ANALYZED，独立完整复现未授权/未运行，不能标VERIFIED。
11类方法谬误已逐项覆盖；机械文档QA见[最终检查回执](final-qa.md)。
内部同家族模型审查不是外部同行评审；既有监督和开发接触不能洗成盲测。

组合决定：保留B的有限advance；stop本轮双曲增益推广，后续fork而非追加
当前优化。各族/静态owner不混合，无Route坐标评估，formal UNASSIGNED，
B NOT INVOKED；241/242暂停。详见[论文](../paper.md)及[结果附卡](../result-card.md)。
