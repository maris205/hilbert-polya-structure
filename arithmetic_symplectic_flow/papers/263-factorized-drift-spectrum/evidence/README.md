# CS13 冻结、执行与保存证据

Scope ID: `ASFS-DISCOVERY-20260919-CS13`。

Status: `COMPLETE; NO FACTORIZED-SPECTRUM FIT GAIN; FINE-GRID CHAIN FAILS`。

## Material Passport

- Origin Skill: academic-research-suite / experiment-agent
- Origin Mode: bounded construction, single execution and saved-output analysis
- Origin Date: 2026-09-19
- Verification Status: UNVERIFIED
- Separate Saved-output Analysis Status: ANALYZED; no independent scientific rerun
- Version Label: exp_result_v1

## 冻结与预审

[候选卡](../candidate-card.md)、[执行卡](../execution-card.md)、
[14项输入锁](../input-locks.json)先于正式计算；原卡保持不变。
[形式审查](preflight-form-review.md)与[代码预审](preflight-code-review.md)
无未解决阻断；主控全文读回全部源代码及报告，然后冻结
[869行实现与SHA](implementation-freeze.json)。源程序只使用本包定义，
不导入旧科学模块。未做求谱/求积/优化预演。

预审修复一个纯证据保全问题：已完成分解但读出硬失败时，保存raw谱/
同次态/矩阵后再抛错；不改公式或正常路径。实际运行没有触发此分支。
代码审查者与作者分工，但共享任务背景；不是外部同行评议或跨模型认证。

## 唯一实际运行

[父进程收据](execution-receipt.json)记录PID114750、实际退出0、约40.1秒；
600秒硬限+10秒终止宽限未触发。父进程在约18/38秒检查进程及输出，
内部30秒另记一次资源采样。最高RSS344112KiB，低于1GiB提示线。
科学输出总382文件/59802413字节，未触及1GiB硬限；原文件保持不动。

66调用/64唯一成员/2缓存，128训练+6控制+8后检+3消融=145物理全分解；
另一次Gauss7节点构造、64帧直接Gram组装独立计数，无SVD/额外求态/
新目标。两优化器预算耗尽不是优化收敛。六控制均通过，正式读出均有效。

- [manifest与环境](run-1/manifest.json)、[事件与资源](run-1/events.jsonl)
- [机器结果](run-1/result.json)、[381项哈希库存](run-1/file-inventory.json)
- [先冻结的身份](run-1/winners-frozen.json)、[8训练文件SHA冻结](run-1/training-arrays-frozen.json)
- [64成员记录](run-1/unique-members.json)、[66调用记录](run-1/calls.json)
- [四窗拟合](run-1/development-fit-metrics.json)、[网格与消融](run-1/comparisons.json)
- [必要发现门](run-1/finite-discovery-assessments.json)、[方差边界](run-1/variance-effect-assessment.json)
- [逐点表](run-1/points.csv)、[旧B外部标尺](run-1/external-history-comparator.json)
- [Gauss节点与矩](run-1/quadrature.npz)、[求积控制](run-1/quadrature.json)

库存不把自身列入哈希，故381项对应382文件。所有原始lambda/E/mask保留。
四份训练赢家NPZ是原同次分解态的另存，不是额外四次物理求解。

## 保存输出分析

只读[检查器](../check_saved_outputs.py)由分离任务编写，主控全文读回428行。
[实际分析摘要](saved-analysis-result.json)及[审查报告](saved-output-review.md)
记录首次执行exit0、ANALYZED，无审计重试。核对149份谱NPZ（128训练、
4赢家另存、6控制、11固定后检/消融），其中21份含状态；另核对Gauss
数组。覆盖4800 CSV行、60拟合窗、56比较窗、14输入锁、8训练冻结文件
及全部381库存成员。所有382科学文件保持原样。

独立代数恢复FE条带相对差最多8.12e−16，状态最大残差4.40e−12，
相对行和最大1.72e−15，正交F误差最大1.19e−12。无无效或负lambda
对象；重新计算的排名及必要门与原结果一致。检查止于保存数组及FE
条带代数，不重新求谱/优化；不能把ANALYZED改称独立复现VERIFIED。
两族赢家恰好同theta，VAROFF与M在对应网格相同，不虚构额外独立证据。
所有工程门仅属有限对象；无Route坐标升级。

[论文](../paper.md) · [结果卡](../result-card.md) · [声明账本](../claim-ledger.md)。
