## Material Passport

- Origin Skill: ars-codex:academic-research-suite / experiment-agent
- Origin Mode: run
- Origin Date: 2026-09-18
- Verification Status: UNVERIFIED — run-mode report, not a formal statistical validation
- Version Label: DS01-H1-result-v1
- Scope ID: `ASFS-DISCOVERY-20260918-DS01`

## Experiment Result

- **ID:** `DS01-H1`。
- **Type:** finite deterministic simulation / one forward spectral extraction。
- **Status:** `COMPLETED; HISTORICAL MSE REPRODUCED AT PRINTED PRECISION`。
- **Input contract:** [执行前冻结卡](h1-card.md)。
- **Card SHA-256:** `31fff820a883e0754785028b9c797aaf6d19bc9727bacd3e1f6b9db7f1fa75ba`。
- **Source SHA-256 before and after:**
  `dd154507ab7138b2377b9dd7b5fc38809a62b4b1e9ecbf7d7c9ba702e6f737cb`。
- **Working directory:** `/root/autodl-tmp/hilbert-polya-structure/arithmetic_symplectic_flow`。
- **Start observation:** `2026-09-18 15:34:12 UTC`。
- **Completion collected:** `2026-09-18 15:34:25 UTC`。
- **Duration:** completed within the approximately 13-second observation window;
  exact kernel/runtime duration was not separately instrumented. Do not treat
  the sum of polling wait times as process runtime.
- **Exit code:** `0`；no stderr was returned；no timeout or retry。
- **Invocation count:** one `solve()` call；no optimizer, scan or second solve。

### Command

与用户已确认、冻结卡列出的命令完全相同：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 timeout 600s python -c 'import importlib.util,json; p="docs/upstream_snapshots/20260918/riemann_henon/9-robustness_sensitivity.py"; s=importlib.util.spec_from_file_location("henon_baseline",p); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); mse,mape=m.solve(); print(json.dumps({"experiment":"DS01-H1","mse":float(mse),"mape_percent":float(mape)}))'
```

### Output Files

原命令仅打印 JSON。主代理用受控文件编辑原样保存 stdout：

| File | Size / content |
| --- | --- |
| [h1-stdout.json](h1-stdout.json) | 87 bytes；唯一一行 stdout，实验 ID、MSE、MAPE 百分比 |
| 本文件 | Markdown 运行记录；命令、时序、进程观察、比较与边界 |

stdout SHA-256：`e9762469697898ed0381719e5826e402ba048e6794745fad3dc8bfdf6c6b48c7`。

```json
{"experiment": "DS01-H1", "mse": 12.228914226096645, "mape_percent": 2.29045795741477}
```

### Output Summary

| Metric | This run | Historical comparator | Scoped conclusion |
| --- | --- | --- | --- |
| First-100 MSE, source four-decimal reference table | 12.228914226096645 | 12.228914226096645 | 全部保存十进制位一致；差为 0 |
| First-100 MAPE, percent | 2.29045795741477 | notebook prints 2.29%, with a different reference table | 当前数值实测；旧 notebook 只能作近似对照，非精确同输入复现 |

完整 MSE 比较来自
[历史微观日志](../../../docs/upstream_snapshots/20260918/riemann_henon/6-henon_micro_param_scan_100_zeros.log)
第 30018–30020 行，同一 hbar 和 a_start；第 30023 行另有搜索后固定
参数前向复验，保存四位 MSE `12.2289`。扫描器与 H1 的目标 100 个
四位小数、网格、时间、四次正则、分裂乘法与重构公式对应。

该历史优化日志第 30015 行同时保存了 `Maximum number of iterations
has been exceeded.`，故不能把上述参数称为已证明或成功收敛的全局
最优。这里复现的是**该历史参数的目标值**。

[旧 notebook](../../../docs/upstream_snapshots/20260918/riemann_henon/6-heon_100_zeros_match.ipynb)
第 18 行给出 `2.29%`，但第 70–71 行使用 mpmath 25 位生成后转 float
的参考零点，而非 H1 四位表；其矩阵乘法表达也有浮点路径差异。因此
不宣称完整 MAPE 位串的跨实现复现，也不以近似比较替代本次实际输出。

### Monitoring and anomalies

- 硬限由 `timeout 600s` 提供；在上限前正常退出。
- 启动后观察 timeout PID `38971`，Python PID `38972`；Python RSS
  `48792 KiB`。这只是早期瞬时 RSS，不是峰值。
- BLAS/OMP 环境值均为 `1`，单一 Python 进程；`ps` 早期快照的 NLWP
  为 `2`，未设置 CPU affinity，不能把环境设置写成已验证严格只占一个
  OS 线程或绑定一个 CPU。没有多进程优化或 GPU。
- 完成时两个 PID 均已退出。运行小于 30 秒监控周期，没有需要发出的
  停滞/内存增长告警，也不虚构中间迭代计数。
- Python 导入自动产生一个源模块 `.pyc` 缓存；已移到独立临时缓存
  位置保留，不删除源数据。源文件 hash 未变，锁定快照工作树恢复干净。

### Scientific limits and next boundary

1. 这是 100 个已参与历史选参的训练目标，不是保留集外推。
2. 非自治 `a_start` 和完整序列保留，但没有静态/动态消融，所以不能
   从这一运行推出“动态起点是拟合改善的原因”。
3. MAPE 是平均误差，不是最大误差或逐点保证；首点已强制定标。
4. 原始谱、取整分支、逐点误差、数值条件和网格收敛未由本命令输出。
   单次标量吻合不验证这些更强结论。
5. 没有新的训练、任意目标对照、算术消融、PINN 或无限维证明。
6. 冻结的有限量子读出未与 Logistic、宏观 Markov 矩阵或旧 ASFS
   候选拼接。A0/A1/A2/T0–T3 未评估，formal `UNASSIGNED`，B `NOT INVOKED`。

**Decision:** `advance` 基线层：已获得可复查的同参数运行结果。
按本次单次前向授权在此停止计算；若后续研究动态起点的作用，另行
冻结保存逐点输出的动态/静态对照，不自动扩大预算或继续优化。
