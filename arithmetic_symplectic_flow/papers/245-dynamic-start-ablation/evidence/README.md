## Material Passport

- Origin Skill: ars-codex:academic-research-suite / experiment-agent
- Origin Mode: run
- Origin Date: 2026-09-18
- Verification Status: UNVERIFIED — run and saved-array checks, no inferential validation
- Version Label: DS02-experiment-result-v1

## DS02 evidence and execution lock

**Scope ID:** `ASFS-DISCOVERY-20260918-DS02`。  
**Execution state at freeze:** `AUTHORIZED; NOT YET RUN`。
**Current status:** `CONTROLLED COMPARISON COMPLETE; DYNAMIC PATH ADVANTAGE SCOPED`。

用户已批准逐点谱/残差与同参数静态对照。独立采集程序只调用上游
原始 `solve()` 两次，以 return-event profiler 只读复制局部变量，
不改写原函数的运算。不自动执行其他扫描或复验。

## 输入锁

| 输入 | SHA-256 |
| --- | --- |
| [执行前 card 原始字节](../candidate-card-frozen-v1.md) | `fc066c799c812b444ecf8089c70a96bc68e19f16711d79eb3695072076a58ae3` |
| [run_comparison.py](../run_comparison.py) | `734dfd7883cf9abc7e13b9b31205aa80077b0e77a9b2b057cb63b23d4cdb22eb` |
| 上游 9-robustness_sensitivity.py | `dd154507ab7138b2377b9dd7b5fc38809a62b4b1e9ecbf7d7c9ba702e6f737cb` |
| 244 H1 stdout | `e9762469697898ed0381719e5826e402ba048e6794745fad3dc8bfdf6c6b48c7` |

执行前 `python -m py_compile` 已通过，只作语法检查，不运行数值核心。

## 冻结命令与输出范围

工作目录：`/root/autodl-tmp/hilbert-polya-structure/arithmetic_symplectic_flow`。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 timeout -k 10s 600s python -u papers/245-dynamic-start-ablation/run_comparison.py
```

仅写新的 `evidence/run-1/`：开始/每组结束/整体结束的 JSONL 进度，
输入 manifest，各组完整矩阵/谱 NPZ、100 行逐点 CSV、300 步参数
CSV、摘要 JSON，以及静态沿用动态尺度的单独 CSV 和比较 JSON。
目录若已存在会拒绝覆盖。`numpy`/`matplotlib` 均沿用现有依赖；无安装。

600 秒后可终止，额外 10 秒仅作 SIGTERM 后退出宽限；进程、RSS 和
日志以约 30 秒间隔观察。没有输出的时间段不虚构进度。不自动重跑
崩溃或超时；若动态组无法复现 H1，静态组不启动。

## 实际执行结果

上述命令已执行一次，退出码 0，无 stderr，无超时/重试。Python PID
39747，timeout PID 39746；早期进程快照 RSS 60796 KiB、NLWP=1。
程序开始 2026-09-18T15:48:24.354942+00:00，结束事件
15:48:27.077922+00:00。程序计时合计 2.7229874283 秒（截至最终
序列化前），动态/静态 forward 含采集各 0.9982435443 / 0.8717619479
秒。峰值 RSS 91028 KiB；短于 30 秒监控周期，没有停滞告警。

两组各 100 行目标结果、250 个有限谱态、300 步路径。动态 MSE
12.228914226096645、MAPE 2.29045795741477%；静态 MSE
5107.894105246986、MAPE 75.48528887770436%。详细解释与限制
见 [paper.md](../paper.md)，而不是将成功退出当作科学门通过。

## 输出索引

| 输出 | 内容 |
| --- | --- |
| [manifest.json](run-1/manifest.json) | 原源码/脚本/冻结卡/H1 输出 hash、环境、PID |
| [progress.jsonl](run-1/progress.jsonl) | 两次 forward 的开始结束与总体状态 |
| [comparison.json](run-1/comparison.json) | 两组指标、尺度、矩阵诊断及独立共同尺度结果 |
| [D points.csv](run-1/DS02-D/points.csv) / [S points.csv](run-1/DS02-S/points.csv) | 各 100 行预测、残差、百分比、谱序对应 |
| [D spectrum.npz](run-1/DS02-D/spectrum.npz) / [S spectrum.npz](run-1/DS02-S/spectrum.npz) | 各约 2.4 MiB；原矩阵、本征对、分支、250 态与排序 |
| [D schedule.csv](run-1/DS02-D/schedule.csv) / [S schedule.csv](run-1/DS02-S/schedule.csv) | 各 300 步实际参数 |
| [共同动态尺度 CSV](run-1/static_with_dynamic_scale.csv) | 诊断专用；不取代各自首点锚定主比较 |
| [低阶读出链](readout-diagnostic.md) | 只读已存 NPZ 的后处理，无额外 forward |

CSV 的 `target_index` 是 1 基，`original_eigen_index` 是 0 基。
`sort_order` 是原本征序到升序能量的置换；若以后出现精确简并，
简并内编号不具有唯一物理意义。本轮两组最小相邻能量差均为正。

comparison.json SHA-256：
`378d861f7d86fb1afdb400f512b21f86d34b5753d956bd0ada76395f56acf982`。
实际运行 manifest 的 card hash 对应未改动的 frozen-v1；当前
candidate-card 仅追加完成状态，没有变更已执行输入。

## 校验与限制

源码 SHA-256 未变，锁定上游快照工作树干净；无依赖安装、GPU、
图/PDF、原日志覆盖或额外前向。独立代理只读检查了采集代码与现有
NPZ/CSV，确认主指标、100 行覆盖、排序、分支和首点规则一致。
这不是另一次前向，也不是跨模型或外部同行评审。

没有测试重新优化的静态模型、保留集、网格收敛、任意目标拟合能力
或算术消融。完整数组使后续诊断可复查，不自动提升这些证据等级。

交接校验：本包及两个入口共 9 个 Markdown 文件、514 个本地链接
无断链；7 处当前身份/状态一致；9 项输入/输出/受保护记录 hash
未变；两组 CSV 分别有 100 个目标行与 300 个路径行。H1 两个总
指标逐位相同，上游两个快照工作树干净，入口 diff 无空白错误。
语法检查生成的单个 pyc 缓存已移至临时目录保留，不计作实验输出。
