# 首轮 A−1 动态起点试验方案

## Material Passport

- Origin Skill: ars-codex:academic-research-suite / experiment-agent
- Origin Mode: plan
- Origin Date: 2026-09-18
- Verification Status: UNVERIFIED — plan; H1 execution is separately recorded
- Version Label: DS01-code-plan-v1
- Scope ID: `ASFS-DISCOVERY-20260918-DS01`

这是原始执行设计。后续用户确认了 H1 现成函数、单次前向、最多
600 秒；现已完成，见 [冻结合同](evidence/h1-card.md) 与
[运行结果](evidence/h1-result.md)。L1/L0 和其他扩展仍未运行，不能
把局部 H1 确认理解为整张计划表均已获执行授权。

## 研究问题

在保留真实非自治动态起点、完整时间历程和固定谱读出的情况下，现有
低参数数值候选能否形成可复查的基线，并与明确标识的静态对照区分？
首轮只解决实现与可测性，不直接回答“能否完美拟合前 100 点”。

## 建议的两个独立入口

| 入口 | 固定输入与改动边界 | 输出与非声明 |
| --- | --- | --- |
| L1：Logistic 降规模前向 | task27 单次内核；T=20000000、bins=800、W=200000、c=100000、Uc=1.543689、x0=.5、历史 k=6.481896；不优化 | 动态起点和尾步、计数、全谱、有效相位数量、归一化检查；新尺度，不复现原 1e10 步 |
| L0：固定参数对照 | 与 L1 相同离散参数，k=0、mu=Uc；独立控制 ID | 比较动态路径是否造成可辨变化，不把无差异称为数学否定 |
| H1：Hénon 原参数单次前向（可优先） | 9-robustness_sensitivity.py 的 solve()；hbar=.06138739295586476、a_start=1.551941486210356、a_end=1.02、S=300、N=250、L=3.5、quartic=.05 | 返回历史百点训练 MSE/MAPE；非盲测，不等同于 Hilbert–Pólya 结果 |

L1/L0 是已发确认请求中的 Logistic 首轮选项；H1 是源码核对后发现的
更小既有函数入口。不能在只批准其中一项时自动扩成三项或参数搜索。
当前缺 numba，L 路若采用该上游内核还需确认隔离依赖准备；不要为了
省依赖静默改变内核精度、fastmath 或边界处理。

## 运行限制（H1 已确认；其余项待确认）

- 单进程、BLAS 单线程，合计硬上限 600 秒；无 GPU，无优化器。
- 每个配置只做一次前向；失败或超时不自动重试。
- 仅在本工作包的新证据目录写 JSON/日志，不覆盖上游已有结果。
- 记录 wall time、版本、输入 hash、有效谱点数；输出不齐即标记失败
  或不足，不能用少于 100 点的误差冒充完整百点拟合。
- 原样重现与修正实现分开；特别不悄悄改变预热末尾索引、首个跨预热
  计数、CSR 约定、谱分支、量子整数解缠或首点归一化。

## 具体命令状态

L 路需要获准后建立独立 wrapper：当前未创建脚本，因此不列一条
看似已可执行却指向不存在文件的命令。得到脚本授权后先固定文件、
输入和输出，再展示确切运行命令。

H1 不改上游代码调用现成函数。以下最小入口现已确认并执行一次，
在工作区根目录运行；它只打印 JSON，不自行覆盖原仓库输出：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 timeout 600s python -c 'import importlib.util,json; p="docs/upstream_snapshots/20260918/riemann_henon/9-robustness_sensitivity.py"; s=importlib.util.spec_from_file_location("henon_baseline",p); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); mse,mape=m.solve(); print(json.dumps({"experiment":"DS01-H1","mse":float(mse),"mape_percent":float(mape)}))'
```

该命令的原样 stdout、时序、退出码与来源已保存于上述运行记录；
若要保存原始谱和分支，则需另定 wrapper 编辑范围，并独立校验包装
没有改变原函数的数值运算。不能因为输出两项指标就声称这些数组已保存。

## 后续拟合和外推设计（不在首轮自动执行）

先锁住完整谱编号和训练期尺度，再查看保留窗口；测试标签不得再进入
定标、排序选择或参数优化。历史 k 与 Hénon 最优参数已见过前 100
零点，不能因后来划分 70/30 就把同一百点改称严格盲测。可用更高
索引作后续固定参数检验，但已公开/已检视信息的限制必须如实记录。

新训练需要另定低维参数边界、损失、预算和停机阈值；任意目标/算术
消融也需同预算比较。当前不预先声称这些控制会通过。

## 下一决策

H1 单次授权已完成。下一步可选择逐点输出与动态/静态对照，或另行
推进 Logistic；均不能静默扩大本次参数、计算预算或目标读取权限。
