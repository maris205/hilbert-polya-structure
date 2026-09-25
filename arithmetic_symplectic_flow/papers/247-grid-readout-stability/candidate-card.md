# DS04 — 固定非自治路径的网格读出稳定性冻结卡

**Scope ID:** `ASFS-DISCOVERY-20260919-DS04`。  
**Paper ID:** `247-grid-readout-stability`。  
**Version / date:** 1 / 2026-09-19；先于脚本与计算冻结。  
**Status:** `GRID TEST COMPLETE; FIT GRID-SENSITIVE; STABILITY PROMOTION STOP`。  
**Formal coordinates:** `UNASSIGNED`；**Route B:** `NOT INVOKED`。

三次前向均已完成，未重跑 N250。原执行前授权卡字节保存在
[authorized-v1](candidate-card-authorized-v1.md)，与实际 manifest
的 candidate-card hash 一致。下列冻结实验方法未变；实际结果见
[paper.md](paper.md) 和 [evidence](evidence/README.md)。

## 当前授权

用户在 246 交接后要求“继续”，在看到本卡具体命令和新增采集脚本
范围后明确答复“按此执行”。授权已满足，只覆盖本卡三次前向，
不扩为参数搜索。执行前原协议字节见
[frozen-v1](candidate-card-frozen-v1.md)；原方法内容不变。

## 原对象族与唯一主动变动

| 控制 ID | 网格 N | 来源 / 执行 |
| --- | ---: | --- |
| DS04-N250-reference | 250 | 原 DS02-D 保存数据；不重跑、不冒充新数据 |
| DS04-N260 | 260 | 拟一次 solve(N=260) |
| DS04-N280 | 280 | 拟一次 solve(N=280) |
| DS04-N300 | 300 | 拟一次 solve(N=300) |

全部固定：hbar=.06138739295586476，L=3.5，quartic=.05，
a_start=1.551941486210356，a_end=1.02，S=300，c=10。
非自治参数路径仍为 a_n=a_end+(a_start−a_end)[f(n)−f(S)]/
[f(1)−f(S)]，f(n)=1/log²(n+c)，n=1,...,300。
动态起点是这条完整参数路径的端点，不是轨道初值 x0。

源码固定为 Hénon commit `6f78e365c7c5d7afb413c8828c79f0e82f0bb4f4`
的 [9-robustness_sensitivity.py](../../docs/upstream_snapshots/20260918/riemann_henon/9-robustness_sensitivity.py)，
SHA-256 `dd154507ab7138b2377b9dd7b5fc38809a62b4b1e9ecbf7d7c9ba702e6f737cb`。
保持原时间乘积、相位、H_base 期望选支、排序、移零和各组首点尺度。
不改为 H_base 直接谱，不改单位 kick 步长，不重优化任何参数。

不同 N 对应不同有限维矩阵，分别拥有 H_N、U_N、态、分支及尺度；
不能共享矩阵或按排序号认定同一态。固定 L 时 dq=2L/N，FFT
动量间隔理论上为 pi*hbar/L，动量截止随 N 增长。本检验因此是
固定箱长离散族的空间细化/动量截止敏感性，不是只改变显示精度。
不能由四个有限点证明连续极限、箱长稳定性或无限谱归属。

## 采集与固定比较

复用 [245 采集方法](../245-dynamic-start-ablation/run_comparison.py)
中的 return-event capture 和 save_case；锁定 hash
`734dfd7883cf9abc7e13b9b31205aa80077b0e77a9b2b057cb63b23d4cdb22eb`。
不调用它的 main；仅将新包装器进程内的 OUTPUT 指向本包新目录。
原 245 文件和保存数据不编辑，不替换数值核心或运算顺序。

每个新 N 保存全部矩阵/本征对/期望/分支/排序 NPZ、100 行预测残差、
300 行参数路径和原 scalar 指标。另记录 dq、动量截止、最大动能、
最低三态原 ee/重构能量、首间隙、尺度、纯期望诊断及其自身尺度。
比较各 N 对 N250、相邻 N 的百点输出差异与尺度比；这是排序后的
输出曲线比较，不是跨网格本征态跟踪。

不设置可宣称收敛的 PASS 阈值；报告实际变化幅度、方向与有限证据
限制。原首点准确由定标强制，不能充当稳定性证据。百点均参与过
历史训练，不能将网格更改当作样本外测试。三点按预定顺序全部保存，
不按哪一点拟合更好挑选新 N 或更换历史基线。

## 命令与停止边界

确认后的唯一拟执行命令，cwd 为本项目根目录：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 timeout -k 10s 600s python -u papers/247-grid-readout-stability/run_grid.py
```

仅三次新前向、单进程、BLAS/OMP=1、无 GPU、无安装。总 600 秒
硬限及 10 秒终止宽限；不保证 OS CPU affinity。输出仅新建
本包 evidence/run-1；若存在则拒绝覆盖。记录开始/结束 UTC、PID、
初始和峰值 RSS、每组耗时、退出码；约30秒监控，短任务直接收集。
原源码/采集 helper/基线 hash 不符、缺失或非有限输出、目标不全、
截获与原 scalar 不一致时停止，保留失败记录，不自动重试或补点。

## 同对象与门状态

谱系：素数符号观测 → 非自治 Logistic 动机 → Hénon 有限数值
提升；本包检验该有限读出对离散化的敏感性，不声称严格素数编码。
相空间/roof/悬流/完整闭轨 `NOT APPLICABLE`；A0/A1/A2/T0–T3
`NOT EVALUATED`；不继承任何 Route 信用。241/242 仍暂停。
