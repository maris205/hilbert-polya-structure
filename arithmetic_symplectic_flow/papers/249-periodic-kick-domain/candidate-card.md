# DS06 冻结卡：原 FFT 量子踢的周期边界与能量域

**Scope ID:** `ASFS-DISCOVERY-20260919-DS06`。  
**Version/date:** v1 / 2026-09-19。  
**Freeze status:** `FROZEN BEFORE MATHEMATICAL AUDIT`。

用户已授权自动继续本地有界发现工作。本卡先于新的数学审计与计算。
本包审查原有限 FFT 算法的一个明确连续比较对象，不声称已证明
有限矩阵或其读出收敛到它；不替换 245/247 的对象。

## 冻结定义

源码：[上游 sensitivity solver](../../docs/upstream_snapshots/20260918/riemann_henon/9-robustness_sensitivity.py)，
SHA256 `dd154507ab7138b2377b9dd7b5fc38809a62b4b1e9ecbf7d7c9ba702e6f737cb`。
原动态路径保持 a_start=1.551941486210356 → a_end=1.02，300步，c=10；
hbar=.06138739295586476，L=3.5，quartic=.05。

比较 Hilbert 空间为 L²(R/(2L Z),dq)，周期动能
T=−hbar² ∂q²/2，其二次型域 H¹_per，算子域 H²_per。
V_a(q)=−q+q²+a q³/3+.05q⁴ 定义在 [-L,L) 并可测周期延拓；
K_a 为 exp(−i V_a/hbar) 乘法，D=exp(−i T/hbar)，单步 U_a=D K_a。
多步按原顺序 U_aS ... U_a1。H_base=T+V_aend 为独立参考能量算子。
不得以周期边界不光滑直接否认 L² 酉性或 H_base 自伴性。

审计问题：端点相位是否接合；若不接合，K_a 是否保持 H¹_per；
对常数态的 Fourier 尾部与截断动能能否给出解析结论。
必须区分单步域不保持、300步特定本征态、有限矩阵拟合失败三件事。

## 允许的有界证据与控制

可进行独立数学推导、主要来源核对；可对首步 a_start 与末步 a_end
进行一次向量 FFT 截断诊断，预选 N=250,500,1000,2000,4000,8000，
输入归一化常数态，无矩阵本征求解、无300步前向、无目标零点拟合。
控制为同一 a 的光滑周期踢 V_control(q)=a*cos(pi*q/L)，仅作边界控制，
不作为修复后的候选或原 Hénon 势的等价物。保存全部模式权重/动能汇总。
有限 N 不能替代 Fourier 解析证明，采样 FFT 尾部不等于精确投影尾部。
脚本/输入在执行前锁定；硬限120秒，输出只到本包 evidence/run-1。

谱系：素数符号 → 非自治 Logistic → Hénon 有限提升；本包是其量子
读出几何边界诊断，不建立算术源。经典相空间/roof/闭轨门不适用。
A0/A1/A2/T0–T3 `NOT EVALUATED`，formal `UNASSIGNED`，B `NOT INVOKED`。
若域保持失败，停止以光滑周期有限能量对象解释原踢的自动晋级；
不否认可测 L² 模型，不推断所有谱态发散。任何修复须新对象、独立卡。
