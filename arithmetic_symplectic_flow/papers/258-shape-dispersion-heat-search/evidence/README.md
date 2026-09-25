# CS08 — 执行与保存证据

Scope ID: `ASFS-DISCOVERY-20260919-CS08`。  
Status: `FIXED REPAIR COMPLETE; FINE-320 STABILITY MET; STATIC NEAR-IDENTICAL`。

下方v1保留原run-1失败时点记录；用户批准的单次修复及最终结果见末尾v2。

## Material Passport

- Origin Skill: academic-research-suite / experiment-agent
- Origin Mode: run
- Origin Date: 2026-09-19研究标签，实际UTC另记
- Verification Status: UNVERIFIED
- Version Label: exp_result_v1

## Experiment Result

- ID: `ASFS-DISCOVERY-20260919-CS08`
- Type: analysis / deterministic supervised structural search
- Status: CRASHED AFTER TRAINING / BEFORE COMPLETE-ARRAY FREEZE
- Working Directory: `/root/autodl-tmp/hilbert-polya-structure/arithmetic_symplectic_flow`
- Command: [冻结执行卡](../execution-card.md)，600秒硬限+10秒宽限。
- 授权：沿用用户继续的本地实现/运行授权，不另扩大研究或外部权限。
- Input: [16项锁](../input-locks.json)，旧源代码、对象和目标只读。
- Output: 仅本包run-1，存在即拒绝；非赢家不保存完整传播矩阵。
- Budget: 最多345传播、10额外保存态SVD、22静态分解；不自动重试。
- Actual: 165成对调用、160唯一成员、5缓存调用；320训练+3控制=323传播。
- Duration: 启动到失败事件174.153598秒，UTC22:40:33.785918→22:43:27.939516。
- Actual Exit Code: 1；600秒硬限未触发；PID61165。
- Observed peak RSS: 最后150秒采样160912KiB，非最终峰值保证。
- Saved output: 原run-1共815文件、111211968字节，无覆盖或追加重跑。
- Environment: Python3.12.3、NumPy2.4.4、SciPy1.16.1；单BLAS线程。

### 中断、剩余工作与计数纠正

异常为`event()`的形参与关键字均命名`name`，在runner第684行冲突。
赢家身份已冻结为Q；完整训练矩阵/状态尚未保存，训练完整数组冻结
记录不存在。因此高N/时间/箱宽、全部静态分解、态诊断和开发评分均未
执行。计数器先加1再触发失败，实际额外态SVD为0，不照抄原计数为1。

这是作者、主控和静态审查漏检的实现错误，不是数学否定或数值控制失败。
保留原脚本、原审查和失败事件；按冻结卡及ARS“不自动重试”规则停止。
只读证据审查与文档整理未执行研究代码。补齐固定赢家矩阵需要新的
传播，不能从sigma假装恢复C；须用户批准新的修复执行卡后才做。

### 输出导航

| 记录 | 实际内容 |
| --- | --- |
| [launch-receipt.json](launch-receipt.json) | 主控工具退出码、事件时间、计数偏差及缺失阶段 |
| [failed-run-inventory.json](failed-run-inventory.json) | 主控在原run-1外收集的815文件大小/SHA，非runner正常完成清单 |
| [manifest](run-1/manifest.json) | 冻结输入/脚本身份、环境和预定预算，不代表预算全部执行 |
| [events](run-1/events.jsonl) | 三控制、320训练、资源采样、身份冻结和失败记录 |
| [全部唯一成员](run-1/unique-members.json) / [调用账本](run-1/calls.json) | 160成员、165调用、5缓存和全部训练指标 |
| [赢家身份](run-1/winners-frozen.json) | 五个训练角色及全局Q0107，开发尚未评分 |
| [B](run-1/control-B.json) / [U](run-1/control-U.json) / [D](run-1/control-D.json) | 三种解析控制均通过；各有同名NPZ |
| [双回归](run-1/default-regression.json) | 两N完整320预测及前100M/W差均0 |
| [根账本](run-1/minimum-ledger.jsonl) | 6464个势最低值记录；浮点非认证，JSONL保留而汇总JSON未产生 |
| evaluations目录 | 每唯一成员两个NPZ、两个网格JSON及一个成员JSON，共800文件 |

所有唯一训练成员的全sigma/E/mask/320预测/路径/势数据均保存；训练
C原来只驻内存，故包括赢家在内都没有完整C/左右态落盘。
没有result.json、training-arrays-frozen.json、开发评分或后检NPZ；
不以主控收集文件伪造这些未达阶段。

## 审查与复现边界

[形式审查](form-review.md)核对新势全线最低点隔离与有限owner。
[执行前代码审查](code-review.md)及作者AST/纯导入未做数值预演，
且都漏检了日志参数冲突；原报告保留其当时判断，并由本记录纠正边界。
[保存结果审查](saved-result-review.md)只读取已有训练数组，重算前100
指标/排名并核对计数/冻结，不从头重跑。审查为同家族模型内部
检查，可能共享历史上下文，不是盲审、跨模型认证或外部同行评审。
脚本和输入足以定义非赢家的重建方法，但不声称其完整C已保存或复算。

## Material Passport

- Origin Skill: academic-research-suite / experiment-agent
- Origin Mode: validate
- Origin Date: 2026-09-19研究标签
- Verification Status: ANALYZED（保存训练数组复算；非独立传播重跑）
- Version Label: validation_v1

## Validation Report

CAUTION：确定性有限谱，不使用抽样p值、显著性、置信区间或统计总体
误差条。J<1与G<2%是预设工程标准，不是误差认证或目标谱身份。

主赢家Q0107训练maxM/W=1.709232%/5.249433%，J=.833468；本轮
B为1.957695%/5.474616%。Q两指标均改善，O仅M/J改善但W更差，
U/D相同z=0母体不算新色散收益。五个优化器均未收敛；训练两N的
G很小不等于后检通过。全101–320此前已知，但本次未评分。

### 11/11谬误类型覆盖

| 类型 | 本包处理与限制 |
| --- | --- |
| Simpson聚合反转 | 五族、两训练N及各开发窗口分别报告，不以全局平均隐藏失败 |
| Ecological生态推断 | 不从有限前缀或聚合MAPE推断每个无限编号 |
| Berkson选择偏差 | 参数源与范围含先前监督；高N后检不消除历史选择 |
| Collider碰撞变量 | 无因果调整模型；不据此推导因果收益 |
| Base-rate基率忽略 | 无分类/患病率推断，本项不适用 |
| Regression-to-mean均值回归 | 非随机重复测量；改进与同调用B并列，不称统计回归效应 |
| Survivorship幸存者偏差 | 160成员均有效且全保留；五个预算终止及本次崩溃显式报告，未发生后检不伪称通过 |
| Look-elsewhere多处寻找 | 五个赢家均报告，不在开发阶段另换主赢家 |
| Forking-paths分析自由度 | 卡前定五族、种子、目标、阈值、预算；无事后细调或新N |
| Correlation/causation相关因果 | 非零z且较好也非独立结构因果证明；静态未单独训练 |
| Reverse-causality反向因果 | 目标用于原参数及本次监督，不能反推由动力学自然生成 |

Independent reproduction: NOT RUN；Verdict: CANNOT_VERIFY。
这些边界不替代结果和源码审查，也不把内部模型检查称为数学认证。

## 原run-1集成检查

本轮研究执行因实现错误停止；未安装、GPU、上传、发布、PDF或Git提交。
输入锁16/16与runner SHA未变，输出收集未修改run-1。主控集成检查覆盖
11份Markdown（本包9份及两个根索引）、574个本地链接/锚点，0错误；
四份当前结果文档的Scope ID/状态一致，根索引`git diff --check`通过。
原候选卡保持执行前的冻结状态，不以
事后状态改写其字节；当前结果状态以paper/README/claim ledger为准。

## 用户批准的固定赢家修复 — Material Passport v2

- Origin Skill: academic-research-suite / experiment-agent
- Origin Mode: run
- Origin Date: 2026-09-19研究标签；实际UTC2026-09-18
- Verification Status: UNVERIFIED（有限执行，不等同完整独立复现）
- Version Label: exp_result_v2_fixed_repair

用户明确批准修复后冻结[修复执行卡](../repair-execution-card.md)及
[34项输入锁](../repair-input-locks.json)。原脚本、原815文件和旧审查保留，
只新增resume_fixed.py及run-2-fixed。新日志接口通过四种历史调用的实际
非数值测试和独立[代码审查](repair-code-review.md)，未关闭日志避错。

### Experiment Result v2

- Execution ID: `CS08-REPAIR-FIXED-01`；主赢家仍Q0107，五个theta均冻结。
- Command/working directory: [修复启动回执](repair-launch-receipt.json)，唯一一次启动。
- Exit/PID: 0 / 64098；600秒硬限未触发；Python/NumPy/SciPy与v1相同。
- UTC events: 23:42:25.303309→23:43:57.469873；事件间隔92.166564秒。
- Internal timer: 93.142345秒，从初始核验前开始；结束前峰值RSS297068KiB。
- Actual: 10固定重建+12固定后检=22传播，22 full SVD、22静态分解；尝试=完成。
- Zero: 新优化、主赢家重选、新目标、旧控制重跑、额外科学执行。
- Combined run-1/run-2: 345已完成传播；原run-1额外态SVD实际仍为0。
- Output: 101文件、478484239字节；硬输出上限1GiB未触发。
- Inputs: 34修复锁、16原锁、815原文件成员/大小/SHA首尾均通过。
- Reconstruction: 原物理/选择数组精确保持，新full sigma最大差3.774759e−15≤1e−12。
- Freeze: 原赢家逐字节副本；十训练热+十静态对象的40文件先哈希冻结，后读开发参考。

| 新记录 | 内容和界限 |
| --- | --- |
| [manifest](run-2-fixed/manifest.json) / [events](run-2-fixed/events.jsonl) | 环境、参数/SHA、实际阶段与分别计数 |
| [logger regression](run-2-fixed/logger-regression.json) | 四实际内存流测试；非科学运行 |
| [training freeze](run-2-fixed/training-arrays-frozen.json) | 40训练NPZ/JSON、原身份SHA；开发评分此前false |
| [result](run-2-fixed/result.json) | 全重建一致性、22+22对象、角色/指标/诊断和首尾核验 |
| [fits](run-2-fixed/development-fit-metrics.json) / [comparisons](run-2-fixed/comparisons.json) | 四窗口全五族及静态、时间、箱宽，无后验重选 |
| [points](run-2-fixed/points.csv) | 45对象×320=14400数据行；含旧S固定对照 |
| [root ledger](run-2-fixed/minimum-ledger.json) | 384独立最低值记录；旧/new ID分账，浮点非认证 |
| [file inventory](run-2-fixed/file-inventory.json) | 100输出的大小/SHA，自身为第101文件且明确不自哈希 |

### Validation Report v2

- Origin Skill: academic-research-suite / experiment-agent
- Origin Mode: validate
- Verification Status: ANALYZED（保存数组复核；不是完整搜索独立重跑）
- Version Label: validation_v2_fixed_repair

Q/N1279的四窗口MAPE为1.709232%/4.277943%/5.760972%/3.567910%，
全320最坏5.898319%；相同四窗口均优于旧S及B。B/O/U/D全320 MAPE
均不如旧S，训练收益不普遍外推。原共同优化及活动维数差仍限制归因。

负结果保留：五族N639→1023全320 G均>45%，Q为52.903616%；全部低100
稳定不认证粗高320。正结果严格限于所测更细N：五族N1023→1279全320
G<1e−11%；Q时间G=.001662738%、箱宽G=4.142e−11%，满足2%工程线。
N1023的高动量最大占据仍为.355256，N1279约3.031e−27；占据不是误差界。
Q热/静态全320 G=5.949e−8%，22对最大也仅1.294e−7%，没有实质次序收益。
全C/全sigma和全静态H/lambda保存，只有前320态保留，不称完整态重构。

独立[保存结果复核](repair-saved-result-review.md)只读数组/日志，核验
指标、计数、40文件开发前冻结、原身份与所有哈希，不执行新传播、分解、
求根或优化。完整搜索独立复现NOT RUN；同家族内部审查不冒称外部同行评审。
上列11/11类型在修复中继续覆盖：各族/窗口分开、粗网格失败及原崩溃不删除、
静态不利对照保留、无开发重选、无p值/因果/无限推论，历史监督来源明确。

组合advance Q为细网格有限320改进基线；stop粗尾谱、热优越性与无限推广。
本修复范围全部完成，未安装/GPU/上传/发布/PDF/提交或开启新研究。
same-object按各族独立保持，A0/A1/A2/T0–T3未评，formal UNASSIGNED，
B NOT INVOKED；241/242暂停。[只读集成检查程序](../check_repair_evidence.py)
核验本包与两个索引链接/状态、输入锁、两次输出清单和runner SHA。
结果另存[repair-document-check.json](repair-document-check.json)，
不改写原document-check.json或任何旧回执/审查。
