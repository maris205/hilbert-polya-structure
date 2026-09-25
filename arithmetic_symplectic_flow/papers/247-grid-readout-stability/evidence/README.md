## Material Passport

- Origin Skill: ars-codex:academic-research-suite / experiment-agent
- Origin Mode: run
- Origin Date: 2026-09-19（用户研究日期；实际进程 UTC 另列）
- Verification Status: UNVERIFIED — execution and saved-array checks; no independent forward re-run or inferential validation
- Version Label: DS04-experiment-result-v1

## DS04 — 执行证据入口

**Scope ID:** `ASFS-DISCOVERY-20260919-DS04`。  
**Status:** `GRID TEST COMPLETE; FIT GRID-SENSITIVE; STABILITY PROMOTION STOP`。

## 具体命令确认

ARS `experiment-agent/agents/code_runner_agent.md` 的 EXECUTE 第1项
要求先确认具体命令；其 Safety 第5项再次规定确认后执行。
`experiment-agent/WORKFLOW.md` Safety 第1项不允许自动生成/修改
实验脚本。此前已向用户请求新增独立采集脚本并执行以下命令，
用户现明确答复“按此执行”。确认已满足，脚本已按原协议创建，
没有更改三个 N、任何固定参数或命令。授权记录见
[execution-card](../execution-card.md)，原协议和授权前快照均保留。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 timeout -k 10s 600s python -u papers/247-grid-readout-stability/run_grid.py
```

cwd：`/root/autodl-tmp/hilbert-polya-structure/arithmetic_symplectic_flow`。
输出限定为本包新的 `evidence/run-1/`；执行前该目录不存在。
只新增 N260、280、300 三次动态前向，无 GPU、调参、安装或自动重试。

## 固定输入

| 输入 | SHA-256 |
| --- | --- |
| [上游 solve](../../../docs/upstream_snapshots/20260918/riemann_henon/9-robustness_sensitivity.py) | `dd154507ab7138b2377b9dd7b5fc38809a62b4b1e9ecbf7d7c9ba702e6f737cb` |
| [245 采集 helper](../../245-dynamic-start-ablation/run_comparison.py) | `734dfd7883cf9abc7e13b9b31205aa80077b0e77a9b2b057cb63b23d4cdb22eb` |
| [N250 基线 NPZ](../../245-dynamic-start-ablation/evidence/run-1/DS02-D/spectrum.npz) | `e5817dc78833b35f1f4f4b234c2ed41d6f0b2c213f56bebe128b7f0136ef0833` |
| [245 汇总](../../245-dynamic-start-ablation/evidence/run-1/comparison.json) | `378d861f7d86fb1afdb400f512b21f86d34b5753d956bd0ada76395f56acf982` |

执行前新增锁：

- [原协议快照](../candidate-card-frozen-v1.md)：`90d4c96ac7b2eccbf6dfb6f3d95d4ad33298a7e5f88614a118202404fe4fce64`。
- [执行卡](../execution-card.md)：`1b3eca157f679022a19cead0194c1c03b7041c6866f6f0dd487fcebf122248c7`。
- [run_grid.py](../run_grid.py)：`9d803431b8ae0f0c5934b8406b0106dbdbe1e5f898a5ce801e6b969a54e52447`。

当前卡执行前字节保存在 [authorized-v1](../candidate-card-authorized-v1.md)。
用 compile(source, path, 'exec') 检查语法已通过，不执行脚本顶层，
不产生 pyc 或新增前向。原输入/输出只读，不覆盖历史 N250 数据。

## 预期记录与解释审查

确认后保存 PID、UTC、线程环境、RSS、进度 JSONL、每组原数组与
完整 CSV、汇总和比较；600秒硬限及10秒退出宽限。仅监控新目录
与本任务进程，不因拟合较差而提前删去结果或调整参数。

独立代理已只读核对原源码与 245 采集方法，强调固定箱长下动量
截止变化、不能跨维度匹配原列号、首点定标可能遮蔽原始尺度变化、
四点不能证明连续极限。协议已明确这些限制；代理没有运行计算、
写代码或发出跨模型/同行评审认证。

首次协议准备阶段（批准前）检查：本包及两个入口共7个 Markdown 文件、495个本地
链接、8项输入/保护文件 hash，错误数0；身份状态一致，入口 diff
无空白错误。当时执行脚本与新输出目录均不存在，保持 NOT RUN；
这是历史准备记录，不是现在的执行状态。

## 实际运行

上述命令原样执行一次，退出码0，无 stderr、超时或重试。
恰好三个 `forward_start` / `forward_complete`，N250只复用原数组。
进程 PID43098、timeout PID43097；进程快照 NLWP=1、RSS90848 KiB。
manifest 初始峰值 RSS35532 KiB，最终峰值90848 KiB。

原日志开始事件 UTC 为 `2026-09-18T17:12:32.481096+00:00`，
完成事件为 `2026-09-18T17:12:37.464146+00:00`；程序计时
4.9959202968秒，截至最后汇总序列化前。研究卡按用户当前环境日期
2026-09-19编号，与实际进程时钟日期不同；两者明确区分，未改写日志。
三次 forward 含返回采集分别0.9464175291、1.2195253111、
1.3870099448秒。任务短于30秒监控间隔，无停滞告警。

使用 Python3.12.3、NumPy2.4.4、单进程与既定线程环境，无 GPU
或依赖安装。源代码、旧 helper、旧 NPZ/JSON 与冻结原协议在执行
前后 hash 均相同。执行卡和授权卡的 hash 见 manifest，当前卡
只追加完成状态，执行前字节快照仍可复核。

## 输出索引与数值摘要

| 文件 | 内容 |
| --- | --- |
| [manifest.json](run-1/manifest.json) | 输入/脚本/卡 hash、PID、环境与初始RSS |
| [progress.jsonl](run-1/progress.jsonl) | 恰好三次前向及整体完成事件 |
| [comparison.json](run-1/comparison.json) | 四网格主指标、诊断与有标识的排序输出差 |
| [reference-250.json](run-1/reference-250.json) | 旧 N250 的复用说明；其 forward 耗时是历史值，不计本轮 |
| [prediction-comparison.csv](run-1/prediction-comparison.csv) | 100行四网格预测与相对 N250 的逐点差 |
| [N260 points](run-1/DS04-N260/points.csv) / [NPZ](run-1/DS04-N260/spectrum.npz) | 100点与260态，NPZ2689809字节 |
| [N280 points](run-1/DS04-N280/points.csv) / [NPZ](run-1/DS04-N280/spectrum.npz) | 100点与280态，NPZ3111696字节 |
| [N300 points](run-1/DS04-N300/points.csv) / [NPZ](run-1/DS04-N300/spectrum.npz) | 100点与300态，NPZ3602582字节 |

每个 case 目录另有 `schedule.csv`（300行）、`summary.json`、
`grid-diagnostics.json` 与 `pure-expectation.csv`（100行）。
各网格目标和完整路径均与 N250 逐元素相同；所有新指标由保存
预测重算与原 scalar 相同。没有删去不利网格或改变目标数量。

comparison.json SHA-256：
`9140d157139aee259651d634227b19469715bd172ddd1e78e0839fc5a344ff64`。
全部主结果与界限见 [paper.md](../paper.md)。

## 独立核对与限制

独立子代理只读复核了维度、全部 CSV/NPZ、动态路径、目标、排序
映射、首间隙、尺度和指标；没有导入 solver、运行前向或调用 eigh。
未发现缺失、索引或数值一致性问题。它支持“已测离散族中明显敏感”
的有限描述，反对将之扩大为无限不收敛或所有模型失败。核对为同一
模型家族的代理工作，不是跨模型或外部同行评审。

UNVERIFIED 是 ARS run 的验证等级，不否认进程已实际完成；本轮
没有额外重复三次前向，也没有推断统计检验。小矩阵残差不代替
谱极限或网格稳健性证据；本轮本身给出了负向稳定性控制。

最终交接检查：本包及两入口共10个 Markdown 文件、528个本地
链接、13项输入/输出/保护文件 hash，错误数0；日志恰好覆盖
N260/280/300，逐组 CSV 行数为100/300/100。当前身份状态一致，
两个上游快照工作树干净，入口 diff 无空白错误。独立结论边界
复核无必须修正项；未为重复检查追加前向计算。
