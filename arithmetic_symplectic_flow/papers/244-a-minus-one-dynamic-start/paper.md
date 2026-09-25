# A−1 发现轨的动态起点：Logistic/Hénon 更新同步与首个基线复现

**Paper ID:** `244-a-minus-one-dynamic-start`  
**Scope ID:** `ASFS-DISCOVERY-20260918-DS01`  
**Date:** 2026-09-18。  
**Status:** `SOURCE SYNC COMPLETE; H1 BASELINE REPRODUCED`。  
**Route:** A0/A1/A2 不评价；formal coordinates `UNASSIGNED`；B `NOT INVOKED`。

## 摘要

本工作包执行用户提出的 A−1 构造发现方向的来源准备：同步两个更新的
公开代码库，核对非自治动态起点，并设计有界基线。第一阶段完成固定
提交的代码同步和只读审计；用户随后确认 H1 单次运行，实际得到前
100 点 MSE=12.228914226096645、MAPE=2.29045795741477%。
MSE 与历史同参数日志的完整保存数值一致，没有重新搜索参数。
Hénon 的首步参数和终点补偿必须留在同一有序演化中；Logistic 的历史
版本则包含左右逼近、预热重置和有限端点补偿等不同约定，不能按名字
合并。新增样本外材料必须逐段核对：task12 的测试标签重新定标和谱
编号问题，使其不能直接充当冻结外推证据。后续先建立受限、可复查的
非自治基线；其复现不代表完美拟合、保留集预测或 A0 评分。

## 1. 来源、授权与同对象账本

本包承接 [243 方法说明](../243-construction-first-search-note/paper.md)，
但用户此次明确要求试做发现轨并同步更新，因此 243 的“尚未授权试做”
是其历史状态，不覆盖本次来源准备。原 241/242 推进仍暂停。

| 对象 | 固定来源 | 本包处理 |
| --- | --- | --- |
| Logistic 非自治转移矩阵族 | `e3419dda3d5515afd91a5dd6e8d8b8398f359dde` | 逐个实现核对，不合并不同冷却/读出约定 |
| Hénon 有序有限酉矩阵 | `6f78e365c7c5d7afb413c8828c79f0e82f0bb4f4` | 冻结动态起点、时间乘积和原重构读出 |
| Hénon 宏观累积转移矩阵 | 同一仓库提交 | 独立比较对象，不等同于量子矩阵 |
| ASFS 相空间、roof、悬流、完整闭轨账本 | 未在本包构造 | `NOT APPLICABLE`，不默认为通过 |
| 新 A−1 实验 | DS01-H1 独立冻结卡 | H1 单次前向已完成；L1/L0 和其他控制 `NOT RUN` |

来源谱系为素数符号观测 → 非自治 Logistic → Hénon 比较。它是这里
选择方程族的具体历史动机，不是已建立的内生素数生成、算术同构或
完整几何提升定理。零点作为标签的用途必须保留在发现记录内。

## 2. 同步结果与证据等级

快照位于 [20260918 来源目录](../../docs/upstream_snapshots/20260918/README.md)。
它们有独立 Git 数据、固定 HEAD 和来源 URL；原 `legacy`、243 以及
Route 镜像均未改动。工作树只展开代码、机器可读数据、笔记本、日志
和 Markdown，不生成论文出版物。

Hénon 根目录对应的 11 个 Python 文件和 8 个 notebook 与旧归档逐字
相同；因此“仓库更新”不能被写成“计算算法已更新”。当前 README
明确列出素数符号工作、非自治二次映射工作和 Hénon 后续的三步来源，
并将对应关系界定为数值研究。[上游固定版 README](https://github.com/maris205/riemann_henon/blob/6f78e365c7c5d7afb413c8828c79f0e82f0bb4f4/README.md)

Logistic 的当前入口已是根目录 task 系列及 `paper/mca/`；`backup/mvp2`
至 `mvp4` 是历史来源，不能因为版本号大就作为当前实现。新增 task12–15、
review_experiments/task24–27 及其已提交输出确实提供额外审计材料。
这不改变此前只读过旧 `python/` 两个优化器的局部结论；也不能把那个
旧代码范围的“没有保留集检验”扩展到更新后的整个仓库。
[上游固定版入口](https://github.com/maris205/riemann_logistic/blob/e3419dda3d5515afd91a5dd6e8d8b8398f359dde/readme.md)

## 3. 动态起点不是可以省略的初始条件细节

### 3.1 Hénon：同时锁住首步、终步与完整路径

令 \(f(n)=1/\log^2(n+c)\)，源码给出

\[
a_n=a_{\rm end}+(a_{\rm start}-a_{\rm end})
\frac{f(n)-f(S)}{f(1)-f(S)},\qquad 1\le n\le S.
\]

这是源码两个常数 `k_opt`、`a_dyna` 的代数整理，故
\(a_1=a_{\rm start}\)、\(a_S=a_{\rm end}\)。微观默认
\(S=300,c=10,a_{\rm end}=1.02\)；历史固定参数为
\(a_{\rm start}=1.551941486210356\)、
\(\hbar=0.06138739295586476\)。`a_start` 是首步映射/势参数，不是
轨道初态 \(x_0\)。宏观同型序列有不同 \(S\)，不是相同算子。
[源代码](../../docs/upstream_snapshots/20260918/riemann_henon/6-henon_micro_param_scan_100_zeros.py)
第 39–77 行；[固定参数函数](../../docs/upstream_snapshots/20260918/riemann_henon/9-robustness_sensitivity.py)
第 21–27、42–95 行。

保留的时间乘积是 \(U_{\rm tot}=U_S\cdots U_1\)，不是只求终端
\(a=1.02\) 的静态 Hamiltonian 谱。改变 \(S\) 同时改变整条序列，
不能未经定义就称为同一对象的网格精化。

### 3.2 Logistic：端点参数、实际计数起点和预热必须分别记账

当前 task12 及 task27 的单参数宏观律为

\[
\mu_i=U_c+k\left[\frac1{\log^2(i+c)}-
                       \frac1{\log^2(T+c)}\right],
\qquad x_{i+1}=1-\mu_i x_i^2.
\]

源码在普通 NumPy 标量上下文先算 `u_temp`，再传入 JIT 内核。旧稿
将其数值稳定性视作敏感点，因此基线不得静默把常数计算移入 fastmath
区域。task12 从 \(x_0=.5+10^{-8}\xi\) 出发，task27 从 \(.5\)
出发，二者初态约定也应区分。

预热 \(W\) 后计数循环使用 \(i=W,\ldots,T+W-1\)，而端点补偿
使用 \(T\)；所以严格地说 \(\mu_T=U_c\)，并非实际最后记录步
\(\mu_{T+W-1}=U_c\)。基线须同时保存 \(\mu_0,\mu_W,\mu_T,
\mu_{T+W-1}\)，保留原约定再报告偏差；修正时间索引必须另设版本。
当前实现还把 `last_bin` 初始化在预热前，未在预热后重置；首个累计
转移应作为实现细节记录，不在原样复核中悄悄修改。
[task12](../../docs/upstream_snapshots/20260918/riemann_logistic/task12_13_experiments_v2.py)
第 24–58、86–96 行；
[task27](../../docs/upstream_snapshots/20260918/riemann_logistic/review_experiments/task27_de_seed_robustness_reduced.py)
第 44–74、90–99 行。

历史 mvp2/mvp3 还存在 \(U_c-k/\log^2(i+c)\)、预热后重置时间
以及不带有限端点补偿的正号律。它们是对照来源，不是可以拼接的同一
非自治方程。微观 Gaussian 路径另以起终点差定 \(k\)，也不能把宏观
数值参数直接搬过去。

## 4. 新增检验不能只按文件名接受

### 4.1 task12：测试尺度与谱编号没有冻结

`run_single_experiment` 的测试段再次调用
`extract_eigenphases(counts_test, len(test_zeros))`，返回的是所请求
数量的最前面相位，而非例如第 71–100 个相位；随后又执行

```python
scale_test = np.dot(sim_phases_test, tz_test) / np.dot(sim_phases_test, sim_phases_test)
```

其中 `tz_test` 就是测试零点。故其已存 `test_mse` 不能解释为“训练
确定 \(k\)、尺度和谱编号后，对后续零点的冻结预测误差”。这既不能
证明外推成功，也不能据此直接断言正确外推必定失败。现有 JSON 原样
保留；正确实现需要新版本、新执行结果。

### 4.2 task26：有原编号分割，但只支持其自己的六点有限试验

其 `pred` 先固定首零点尺度，再按原始索引选训练和测试集合；未见
task12 那样的测试重定标。已提交 JSON 报告“前三点选择 epsilon、
后三点测试”时训练误差和约为 0.979，测试误差和约为 28.004；全部
六点共同选 epsilon 的对应后三点误差和约为 5.431。这些仅为**上游
已存数据读出**，不是本次重跑，不是概率显著性判断，更不是前 100
点外推结论。
[源程序](../../docs/upstream_snapshots/20260918/riemann_logistic/review_experiments/task26_epsilon_out_of_sample.py)；
[已存 JSON](../../docs/upstream_snapshots/20260918/riemann_logistic/review_experiments/task26_results/oos_results.json)。

### 4.3 CSR 行概率解释与谱影响要分开

Hénon 宏观及 Logistic task26 都有以 CSR 列索引访问行和的写法。
它构造的是 \(CD^{-1}\)，不是注释所称的行归一化 \(D^{-1}C\)。
但当零行和被置为 1 后 \(D\) 可逆，且
\(CD^{-1}=D(D^{-1}C)D^{-1}\)：两者精确特征值相同。
因此这里应纠正的是概率/特征向量解释和数值条件审计，不能仅凭此
直接宣称已有特征相位数值失效，也不能预报修正会改善多少拟合。
本次没有更改上游代码。

## 5. 首轮试验的选择与预算边界

[方案](experiment-plan.md) 将轻量 Logistic 前向与 Hénon 原参数单次
前向分开。关键是先保存真实动态起点、完整谱读出和控制结果，而不是
直接启动上游 HPC 搜索。Hénon 的现成 `solve()` 可以复核固定参数
100 点训练误差；它不是盲测。Logistic 降规模试验必须标为新尺度，
不能号称复现 \(10^{10}\) 步的旧结果。

上游默认预算有显著风险：Logistic task12 是 13 个 \(10^{10}\) 步
优化配置；Hénon 微观扫描器是 `maxiter=10000,popsize=80,workers=-1`；
其宏观扫描器使用 \(40000\times40000\) float32 累积矩阵和大量
并发。没有直接执行这些主程序。

运行前的本机依赖诊断：Python 3.12.3、NumPy 2.4.4、SciPy 1.16.1、
mpmath 1.3.0；默认解释器没有 numba。未安装新包，未更改环境。
Hénon 的 NumPy 单次前向不依赖 numba，用户确认后以现成命令执行；
未改变实现来绕过 Logistic 的依赖缺失。

## 6. 技能执行门与本次明确未做的事情

本次使用 ARS academic-research-suite 的 experiment-agent 工作流。
其 Safety Rule 1 为“Only execute user-specified commands — never
auto-generate or modify scripts”；code_runner 的 EXECUTE 第 1 步又
要求展示具体命令并确认。因此第一阶段在用户同意发现方向、但尚未
确认具体运行时只完成来源同步与设计。随后在明确提出“Hénon 现成
函数、原参数、一次前向、600 秒上限”之后，用户答复“可以，继续”，
满足本次 H1 的执行确认；不再重复要求同一许可。

先前提出的 Logistic 独立脚本/对照没有因此自动获准或执行。没有启动
优化、PINN、符号回归、GPU、自动重跑或外部上传。执行前已另冻结
[DS01-H1 卡](evidence/h1-card.md)，源文件未改动。

## 7. DS01-H1 单次固定参数运行

已确认命令直接导入 `9-robustness_sensitivity.py` 并调用一次
`solve()`，不运行扫描入口 `main()`。保留第 3.1 节全部输入、
动态起点、时间乘积及整数解缠，输出为：

| 量 | 本次实测 |
| --- | --- |
| 前 100 点 MSE | 12.228914226096645 |
| 前 100 点平均绝对百分比误差 MAPE | 2.29045795741477% |
| 退出码 | 0 |
| 时间观察 | 2026-09-18 15:34:12 UTC 启动，15:34:25 UTC 收到完成；约 13 秒观察窗口内结束 |

精确内核耗时没有额外计时，不把上述观察窗口当成内核计时结果。
单 Python 进程，BLAS/OMP 设为 1，600 秒硬限；没有 CPU affinity
约束，不能宣称已验证严格单一 OS 线程。原始 stdout、源 hash、进程
观察及命令均在 [H1 运行记录](evidence/h1-result.md)。

历史微观优化日志第 30018–30020 行给出相同完整参数及 MSE
12.228914226096645；第 30023 行另外保存搜索后一次固定参数前向
MSE=12.2289。因此本次复现了该有限模型的历史 MSE，所有保存位一致。
历史优化同时记录达到最大迭代次数，不能称全局最优已收敛。

本次 MAPE 可与历史 notebook 的 2.29% 作粗粒度对照，但 notebook
使用更高精度生成的参考零点，不是 H1 四位小数目标表；不声称同输入
MAPE 的完整位串复现。两个指标均来自实际运行，不从文稿数字转抄。

必须保留四项限制：这些 100 点已参与历史选参；首点强制定标；MAPE
是平均而非最大误差；原命令没有输出原始谱、逐点残差和取整分支。
没有进行静态/动态消融，所以“保留了动态起点”不等于“已经证实动态
起点导致拟合改善”。网格稳定性、外推和算术特异性仍未在本次检验。

## 8. 结论与交接

**Portfolio decision: advance（基线层）。** 决定性理由是保留动态
起点的固定参数有限计算已重现历史 MSE，后续比较有了实际基准。
约 2.29% 平均误差不是“完美百点”，也不支持无限调参的决定。

- 已建立：固定版本同步、动态起点公式与实现依赖、源码差异，以及
  DS01-H1 的一次实际 MSE/MAPE 运行与同参数 MSE 复现。
- 尚未建立：保留集预测力、动态起点消融效果、算术特异性、精度稳定性。
- 同对象账本：Logistic、Hénon 微观及宏观分别保留；没有拼接算子。
- Route：没有实际评估 A0/A1/A2/T0–T3，formal `UNASSIGNED`，B `NOT INVOKED`。
- 下一步：本次单次前向已完成，停止计算；可另行冻结保存逐点谱的
  动态/静态对照。不得自动续跑参数搜索；换冷却或读出另立版本。

## 复现与证据索引

[冻结卡](candidate-card.md) · [声明账本](claim-ledger.md) ·
[实验方案](experiment-plan.md) · [来源与校验](evidence/README.md)。
来源审计经两个独立代理分别读取核对，不是跨模型验证或外部同行评审；H1 的数值复现
证据则来自独立的实际命令运行，不能把二者混为一种验证。
