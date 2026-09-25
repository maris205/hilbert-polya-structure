# CS06 evidence and validation

Scope ID: `ASFS-DISCOVERY-20260919-CS06`。  
Current status: `LOW-100 JOINT TARGET MET; STATIC CONTROL NEAR-IDENTICAL; HIGH-MODE STABILITY OPEN`。

## Material Passport — run

- Origin Skill: academic-research-suite / experiment-agent。
- Origin Mode: run。
- Origin Date: 2026-09-19研究标签；真实执行UTC为2026-09-18。
- Verification Status: UNVERIFIED（单次原实验，没有独立重跑）。
- Version Label: cs06_exp_result_v1。

## Experiment result

精确命令与工作目录见[执行卡](../execution-card.md)，主控确实安装
`timeout -k 10s 600s`后只启动一次。PID55919，开始UTC
2026-09-18T21:10:31.168841，结束事件21:11:34.394522，真实退出码0。
程序报告主段63.177秒；单BLAS线程另加一个监控线程。
112训练传播、1自由热控制、4固定主成员后检，共117传播；
60次成对调用含4次缓存，56个唯一成员，无INVALID。
8个附加赢家完整SVD与8个静态eigvalsh不是额外传播，已计入同一耗时预算。
四个Nelder–Mead均到8调用上限，非优化收敛。

约30/60秒各有一次资源样本；峰值183552KiB=179.25MiB，
两次均未越512MiB提示线。run-1共312个文件、325093495字节。
没有超时、自动重试、GPU、安装、PDF、外部上传、提交或推送。

解析控制通过：sigma最大差1.29896e−14、绝对能量差6.48592e−13。
S0047满足冻结的J<1，四项后验百点G也在线内；静态近同谱与高模截止
问题如实保留，详见[完整结果和限制](../paper.md#5-搜索结果与执行状态)。

## 原始证据索引

| 记录 | 用途 |
| --- | --- |
| [manifest](run-1/manifest.json) / [输入锁](../input-locks.json) | Python/库版本、线程、脚本/卡/澄清字节身份 |
| [events](run-1/events.jsonl) | 进程事件、传播次数、资源与冻结先后顺序 |
| [seed-design](run-1/seed-design.json) | 四族共同宽域种子和默认值 |
| [calls](run-1/calls.json) / [cache calls](run-1/cache-calls.json) | 60调用和4缓存完整账本 |
| [unique members](run-1/unique-members.json) / [evaluations](run-1/evaluations/) | 56对的Ctilde、全部奇异值/能量/mask、预测、根账本及指标 |
| [minimum cache](run-1/minimum-cache.json) | 冻结前标量全局min记录；新S128根记录另在后检JSON |
| [analytic control](run-1/analytic-control.json) / [arrays](run-1/analytic-control.npz) | W=0解析比较 |
| [winners frozen](run-1/winners-frozen.json) | 四角色身份、静态读出、选择与冻结时间 |
| [S383完整数组](run-1/winner-S-N383.npz) / [S511完整数组](run-1/winner-S-N511.npz) | 原sigma、右/左奇异态、占据诊断及H_avg；Q/R/E同命名 |
| [winner points](run-1/winner-points.csv) / [static points](run-1/static-control-points.csv) | 8×320动态和8×320静态逐点输出 |
| [reference301–320](run-1/reference-301-320.json) | 冻结后生成的非认证参考，非历史盲测 |
| [post points](run-1/post-points.csv) | 四后检各320点，固定参数，不重新定标未来窗口 |
| [N639](run-1/post-space-N639.json) / [N767](run-1/post-space-N767.json) | 固定L与S的空间维度诊断，对应NPZ保留完整矩阵与谱 |
| [S128](run-1/post-time-S128.json) / [L10](run-1/post-box-L10-N639.json) | 时间和箱宽诊断，对应NPZ保留完整矩阵与谱 |
| [result](run-1/result.json) / [inventory](run-1/file-inventory.json) | 汇总与尺寸清单；清单本身不列入自身 |
| [形式审查](form-review.md) / [代码审查](code-review.md) | 精确数学与静态契约分开核对 |
| [保存结果审查](saved-result-review.md) | 原始保存数组和指标的一致性检查，不重跑前向或求谱 |

## Material Passport — validation

- Origin Skill: academic-research-suite / experiment-agent。
- Origin Mode: validate。
- Origin Date: 2026-09-19。
- Verification Status: ANALYZED（保存证据分析，不是VERIFIED重跑）。
- Version Label: cs06_validation_v1。
- 评估范围：确定性监督拟合、数字与保存矩阵一致性；无p值、CI、总体抽样或因果检验。
- 解释警示：CAUTION，尤其静态近同谱与高模未稳定；不是外部同行评审。

### 描述性发现与限制

主成员两训练N的MAPE约2.05%、最坏点约6.35%，联合J=.903204。
后验百点G最大为时间细化的.001951%，均通过2%工程线。
这不能推广到全部320点：主成员后冻20点MAPE随N变化很大，且N511
前320右态的最高20%动量占据最大约.505。
同参数静态MAPE与动态之差极小，不能从正面拟合反推时间排序机制。
首点被强制定标，不能作为独立命中；所有形式共享目标，不是独立样本。

### Fallacy scan — 11/11 checked

| 类型 | 结果及处理 |
| --- | --- |
| 1 Simpson | 未进行人群合并；不同形式、N和窗口逐项报告，不用总均值掩盖高模差异 |
| 2 Ecological | 不从有限网格平均误差推断无限谱或单点误差界；另报最坏点 |
| 3 Berkson | 条件选优样本，不是总体随机样本；无相关性总体推断 |
| 4 Collider | 无因果回归或控制变量因果分析；工程目标的多项max不解释为因果 |
| 5 Base rate | 不报告诊断概率/预测概率；无适用的基率结论 |
| 6 Regression to mean | 不把选出的最低训练误差当必然泛化；后验未重新选参，高段坏结果保留 |
| 7 Survivorship | 56唯一成员及全部四角色保留；0无效成员；优化器预算停止没有删去 |
| 8 Look elsewhere | 多形式、多参数和长期历史均有选择效应；没有显著性或唯一机制声明 |
| 9 Forking paths | 卡、实施澄清、预算与选优规则在执行前锁定；新参考后不改赢家；历史探索仍非盲测 |
| 10 Correlation/causation | 有限拟合不证明算术原因；近同静态控制尤其禁止宣称动态排序导致改善 |
| 11 Reverse causality | 目标用于参数选择和首点尺度，不能倒称动力学独立预测了训练目标 |

### Reproducibility boundary

独立保存证据检查已完成：112份训练谱、四角色八份完整态、四份后检、
全部6400条CSV与2181条独立最低值记录一致；实际指标重建差为0。
只有S0047/S0048两成员J<1，主角色与原冻结一致。八角色原sigma重构
最大相对残差3.32283e−15；无W截零。详细检查及目录绑定见上方审查报告。

没有独立重跑，故再现性认证为`CANNOT_VERIFY FROM A RERUN — NOT RUN`。
原脚本、输入哈希、完整数组、指标和软件版本支持复核与未来复现；
保存结果内部一致性不能升级为浮点根认证、无限维误差界或学术同行评审。
ARS用于冻结执行/报告次序、异常不重试、11项误用检查及ANALYZED/VERIFIED区分。

### 最终文档检查收据

2026-09-18 21:23UTC完成：本包10个Markdown文件、77个本地链接/锚点
（含根索引指向256的链接）零错误；四份当前状态文档一致；10个原输入锁
与脚本/实施澄清/input-locks三个运行身份保持匹配；脚本AST通过。
根索引的`git diff --check`通过。冻结卡保留执行前状态，未以结果覆盖。

Portfolio：advance低100点有限S基准，停止时间排序优势与320点收敛推广。
Same-object完整；A0/A1/A2/T0–T3 NOT EVALUATED；formal UNASSIGNED；B NOT INVOKED。
