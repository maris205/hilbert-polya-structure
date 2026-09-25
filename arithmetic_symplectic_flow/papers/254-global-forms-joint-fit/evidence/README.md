## Material Passport

- Origin Skill: experiment-agent (ARS-Codex)
- Origin Mode: run
- Origin Date: 2026-09-19 (supplied research date)
- Verification Status: UNVERIFIED (formal ARS rerun not invoked)
- Version Label: cs04_result_v1

## Scope and outcome

Scope ID: `ASFS-DISCOVERY-20260919-CS04`。  
Current status: `JOINT TRADEOFF IMPROVED; DUAL THRESHOLD UNMET`。

一次有界执行完成；OS exit0，无崩溃、超时或重试。主A0226训练MAPE
2.311218679860112%、最差百分比误差11.86675601723329%、J=1.0173546276444025。
相对共同起点改善，但未同时超过两个固定基准，维度敏感性仍明显。
本页记录运行与核验事实，不把Passport的正式rerun认证标成通过。

## Exact execution and runtime

从arithmetic_symplectic_flow根目录执行一次：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 timeout -k 10s 600s python -u papers/254-global-forms-joint-fit/run_search.py
```

- 实际PID49957，timeout父进程49954；退出码0由执行工具返回。
- UTC启动2026-09-18T19:22:55.531884；完成2026-09-18T19:25:48.892808。
- 内部耗时173.3821591846645秒，计至最终序列化前；峰值maxRSS131236KiB。
- Python3.12.3、NumPy2.4.4、SciPy1.16.1；三个BLAS环境值均为1。
- 进程另有一个资源监控线程，观察NLWP=2，不能误说整个进程只有1线程。
- shell观察：elapsed11s RSS105196KiB；50s107640；97s117940；135s122008。
- 内部资源采样在约30.024/60.030/90.035/120.040/150.068秒各记录一次。
  对应输出106/216/336/454/530文件与3091103/4559602/6170005/7746629/8727147字节。
  maxRSS依次105232/113492/117940/122008/122412KiB；未观察停滞。
- 最终run-1含567文件、40182418字节（含inventory自身）；无GPU、安装、上传、PDF。

研究日期与实际UTC日期分开记录，不以给定日期替换机器事件时间。
[Manifest](run-1/manifest.json)保存环境、输入及可执行脚本锁。
脚本SHA256：`24eab23bade643dfc5888f458243066beeecc625e48627ae7461e23e89a9d6b5`。
输入锁文件SHA256：`ac1c5c022f42f706a95a1d64ecde5baacbc49469082e3bd255316dd9de4589e5`。

## Before execution

[独立公式审查](form-review.md)核对F/L色散、W非共轭/接缝、A交替路径、
H升降算子与DVR边界，以及联合目标/窗口/七角色。[静态代码审查](code-review.md)
核对实现、预算、缓存与冻结门控。主代理修正过公共缓存的参数元数据：
L/W/A共享F默认矩阵，但其第三参数必须存0而非F的2；仅修正后版本被执行。
AST解析与无副作用import通过，11项输入锁一致，未在preflight做完整前向。

[实际回归控制](run-1/regression-control.json)：首个F默认前向与旧Q0103的
百点预测、MAPE和最差百分比误差差值全部0，容差1e−6。
[Hermite预计算检查](run-1/hermite-basis-250-checks.json)最大残差约3.87e−15；
[完整基底](run-1/hermite-basis-250.npz)保存Q、T_G、O、DVR动能及漂移。

## Output, budgets and freeze ordering

[种子设计](run-1/seed-design.json)保存共同RNG20260921与所有85个物理种子。
[调用记录](run-1/calls.json)：285调用，272实际训练前向，13缓存；F55、
L54、W54、A54、H55实际前向。十个优化阶段均nfev20、success=False。
缓存行继承来源seconds，不能累加这些行计算总耗时。
[全部唯一评价](run-1/evaluations/)含272对NPZ/JSON，保存有限谱与240预测。

[冻结身份](run-1/winners-frozen.json)SHA256：
`3289e10ea0fafa50bcb96ce07468cec83876dd6f37f28170fd40d5f7702e5a26`。
其七角色完整NPZ先写完，再有[事件](run-1/events.jsonl)training_frozen
19:25:34.593170，postfreeze_reference_start19:25:34.593220。
主A0226与secondary-mean是同一成员；七角色对应六个实际成员。
[201–240参考](run-1/reference-201-240.json)用mpmath1.3.0、40位工作精度生成，
非区间认证、非历史盲测。旧101–200在冻结后读取作开发评价。

[角色点表](run-1/winner-points.csv)1680行；[旧对照点表](run-1/control-points.csv)
480行。旧控制用保存能谱与既有尺度，无新旧控制前向。
[训练Pareto清单](run-1/training-pareto.json)10项，仅已试浮点成员的描述。
[结果](run-1/result.json)保存七角色、两个旧控制与主A的两维度诊断。
[N260](run-1/resolution-260.npz)、[N280](run-1/resolution-280.npz)固定参数，未重训。
[文件尺寸清单](run-1/file-inventory.json)列566项，不递归记录自身。

## Review and handoff checks

[保存结果独立审查](saved-result-review.md)完整核对272对评价、285调用、
7角色、两个维度、10个Pareto成员及全部2160行CSV。参数/分支/能量/
尺度/240预测/指标/J、角色与网格矩阵诊断等派生字段重算最大差0。
五族和全局三种角色排序均正确；全部已评价成员J<1数量为0。
Hermite保存基底公式与缩放吻合，没有重做指数、本征求解或传播。
全部584事件在本次日志中UTC单调；七角色最晚保存于19:25:34.576949，
确在新参考生成之前。11输入、脚本、锁文件、冻结哈希和566尺寸记录
全部一致。审查状态ANALYZED，不改变运行Passport的UNVERIFIED标签。

主集成核对本包9份Markdown与两份根索引、全部本地链接、8个核心文件
的Scope ID、6个当前ID/status对、13个输入/manifest哈希及2160行CSV，
没有错误。搜索前卡保持原冻结标签，不覆盖为事后状态；当前状态在
README/全文/账本/本页和两根索引一致。独立审查不是外部同行评审。

主执行已确认11输入在结束时未改，旧上游Hénon/Logistic源码快照Git-clean。
原plan、两份Route镜像及243方法论文未改。所有权有限记录完整，但算术、
closed-orbit/roof/trace缺项仍在；formal UNASSIGNED，B NOT INVOKED。
