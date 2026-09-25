# DS02 — 动态起点逐点读出与静态终点对照冻结卡

**Scope ID:** `ASFS-DISCOVERY-20260918-DS02`  
**Paper ID:** `245-dynamic-start-ablation`  
**Version:** 1，2026-09-18，在脚本与计算之前冻结。  
**Freeze status:** `AUTHORIZED CONTROLLED COMPARISON; NOT YET RUN`。  
**Current status:** `CONTROLLED COMPARISON COMPLETE; DYNAMIC PATH ADVANTAGE SCOPED`。  
**Formal Route coordinates:** `UNASSIGNED`；**Route B:** `NOT INVOKED`。

执行后仅追加本状态栏：两次前向正常完成，完整数据见
[证据记录](evidence/README.md)。运行前 v1 字节原样保存在
[frozen-v1](candidate-card-frozen-v1.md)，SHA-256 为
`fc066c799c812b444ecf8089c70a96bc68e19f16711d79eb3695072076a58ae3`；
该 hash 与实际运行 manifest 一致。下列协议内容未改。

## 授权

用户对“保存逐点谱与残差，并在其余参数不变时加入静态对照”的下一步
明确答复“可以的，继续，go!”。本轮执行该比较，包括必要的独立输出
采集脚本，不改写上游数值代码。仅两次前向、共用 600 秒上限，不调参、
不扩至 Logistic、外推、网格扫描或其他消融。244 的 H1 记录不改。

## 两个分别拥有谱与尺度的实验对象

| 项目 | DS02-D：动态组 | DS02-S：静态对照 |
| --- | --- | --- |
| 源码 | 同一固定上游 `solve()` | 同一固定上游 `solve(a_start=1.02)` |
| a_start | 1.551941486210356 | 1.02 |
| a_end | 1.02 | 1.02 |
| 序列 | a_n=a_end+(a_start−a_end)[f(n)−f(S)]/[f(1)−f(S)] | a_n 恒等于 1.02 |
| f(n)、总步数 | 1/log²(n+10)，S=300 | 相同 |
| 其他输入 | hbar=.06138739295586476；N=250；L=3.5；quartic=.05 | 完全相同 |
| 演化 | 原始有序乘积 U_S...U_1 | 相同乘积代码，常参数 300 步；不是替换成静态 H_base 的直接谱 |
| 主读出 | 原特征相位、H_base 期望、整数取整解缠、排序、减最低值 | 同一读出规则，不另选分支 |
| 主归一化 | gamma_1/E_1，各自首点锚定 | 同一规则，用自身 E_1 |
| 目标 | 上游四位小数 TRUE_ZEROS_100 | 相同目标，不接入新零点 |

上游提交 `6f78e365c7c5d7afb413c8828c79f0e82f0bb4f4`；文件
[9-robustness_sensitivity.py](../../docs/upstream_snapshots/20260918/riemann_henon/9-robustness_sensitivity.py)
SHA-256 `dd154507ab7138b2377b9dd7b5fc38809a62b4b1e9ecbf7d7c9ba702e6f737cb`。

DS02-D 延续 244-H1 数学输入但新增观测输出；DS02-S 是显式更换参数
路径的新控制 ID，不继承 H1 的拟合成绩。主结果不会把两组的尺度合并。
另报告“静态谱乘动态尺度”的标识明确的诊断，不用它替代主比较。

## 采集与预先指定的检验

通过 Python 的 return-event profile 回调读取原 `solve` 栈帧局部
变量，不重写、替换或复制数值核心。每组一次调用，保存：

- q/p 网格、U_tot、H_base、全部特征值与特征向量；
- 原始相位、H_base 期望能量、整数分支 m、排序对应关系、全体重构
  能量和移去最低值后的能量；
- 100 点目标、预测、带符号残差、绝对误差、百分比误差；
- 完整 300 步 a_n 参数路径；原首点比例；
- MSE、RMSE、MAE、MAPE、最大绝对/相对误差及所在序号、前后各 50
  点误差、误差最大的 10 点；不把分段统计称为留出验证；
- U_tot 的相对 Frobenius 酉性误差、特征对残差、H_base Hermitian
  误差和整数取整分支边界距离，均为有限数值诊断而非严格认证。

动态组返回的 MSE/MAPE 必须与 H1 已存值在绝对 1e-10 内一致；若不
一致，保存失败记录并停止，不自动续算静态组或修改实现追求吻合。
非有限输出、缺失局部量、少于 101 个能级同样停止。全部目标必须有
逐点记录，不能以截短目标改善误差。

## 停止、限度与解释

仅两次前向，单 Python 进程，BLAS/OMP=1；timeout 600 秒，超时后
10 秒可强制终止；无 CPU affinity 保证。每组完成写结果及耗时；
进程运行/输出按约 30 秒监控，失败不自动重试，既有输出不覆盖。

比较是条件化的：hbar 等参数由历史动态模型选取，静态组未重新优化。
无论结果好坏，最多支持这两个固定对象在已知百点目标上的描述性
差异；不证明非自治普遍优越、动态起点唯一作用、内生算术、RH、
完整无限谱或通过 A0。整数解缠和首点尺度也是输出机制的一部分。

谱系为素数符号观测 → 非自治 Logistic 动机 → Hénon 数值提升；本轮
检验最后一箭头内的非自治路径消融，不声称保持完整算术编码。
古典相空间、roof、悬流、闭轨账本 `NOT APPLICABLE`；A0/A1/A2 与
T0–T3 `NOT EVALUATED`。原 241/242 仍暂停。
