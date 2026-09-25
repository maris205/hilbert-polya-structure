# DS01-H1 — 固定动态起点单次前向冻结卡

**Scope ID:** `ASFS-DISCOVERY-20260918-DS01`  
**Experiment ID:** `DS01-H1`  
**Version:** 1；2026-09-18，执行前冻结。  
**Freeze status:** `AUTHORIZED; FROZEN BEFORE EXECUTION`。

## 授权与范围

用户在上一轮“先调用 Hénon 现成函数、单核、最多 10 分钟、不调参、
保留动态起点”的明确运行请求后答复“可以，继续”。本次只执行该 H1，
不扩大为 Logistic、静态对照、网格扫描、新优化或第二次重跑。

## 固定输入与同对象定义

- 来源提交：`6f78e365c7c5d7afb413c8828c79f0e82f0bb4f4`。
- 文件：[9-robustness_sensitivity.py](../../../docs/upstream_snapshots/20260918/riemann_henon/9-robustness_sensitivity.py)。
- 文件 SHA-256：`dd154507ab7138b2377b9dd7b5fc38809a62b4b1e9ecbf7d7c9ba702e6f737cb`。
- 函数：原始 `solve()`，无参数覆盖、不修改源码、不调用 `main()`。
- 参数：hbar = 0.06138739295586476；a_start = 1.551941486210356；
  a_end = 1.02；S = 300；c = 10；N = 250；L = 3.5；quartic = 0.05。
- 网格：`q = linspace(-L,L,N,endpoint=False)`；原 FFT 动能矩阵。
- 动态起点：f(n)=1/log²(n+c)，
  a_n=a_end+(a_start−a_end)[f(n)−f(S)]/[f(1)−f(S)]。
- 有序演化：U_tot = U_S ... U_1；每一步保留原分裂顺序。
- 读出：U_tot 特征相位 + 终端 H_base 期望值 + 原整数取整分支；
  重构能量排序、减最低值，再用第一激发值锚定首个目标零点。
- 目标：源码内四位小数的 `TRUE_ZEROS_100`；这 100 点参与历史选参，
  所以本次为训练基线，不是盲测或新的零点预测。
- 输出：一次 solve 返回 MSE、MAPE（百分比），stdout 一行 JSON。
  原命令不返回原始谱、分支数组或逐点误差；这些不在本次已获输出中。
- 相空间/roof/完整闭轨 ledger：此有限数值控制不定义古典 ASFS 对象。
  A0/A1/A2/T0–T3 `NOT EVALUATED`；formal `UNASSIGNED`；B `NOT INVOKED`。

## 已确认命令

工作目录：`/root/autodl-tmp/hilbert-polya-structure/arithmetic_symplectic_flow`。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 timeout 600s python -c 'import importlib.util,json; p="docs/upstream_snapshots/20260918/riemann_henon/9-robustness_sensitivity.py"; s=importlib.util.spec_from_file_location("henon_baseline",p); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); mse,mape=m.solve(); print(json.dumps({"experiment":"DS01-H1","mse":float(mse),"mape_percent":float(mape)}))'
```

## 监控、完成与停止条件

单进程/BLAS 单线程，600 秒硬超时；记录开始与结束 UTC、实际耗时、
退出码与 stdout/stderr。启动后检查进程/PID/RSS，运行超过 30 秒则
按约 30 秒间隔继续检查；该函数没有逐步日志，不假造迭代进度。
硬超时可终止，其他异常只报告；不自动重跑失败或超时的实验。

执行完成要求 exit code 0 且两个输出有限。仅 exit 0 或有一个 JSON
不等于复现历史最优，也不等于“完美百点”。结果只支持此固定参数、
有限网格、原始读出和目标精度下的一次前向。没有新拟合阈值或接受
无限/高精度主张的条件；必要时与相同上游日志做限定比较。

原命令只输出到终端，主代理将原样结果与运行元数据保存到本目录；
不改写上游日志和数据，不生成图/PDF，不安装依赖。
