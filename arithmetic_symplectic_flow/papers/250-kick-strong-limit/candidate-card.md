# DS07 冻结卡：固定步数 FFT 踢的强 L² 极限

**Scope ID:** `ASFS-DISCOVERY-20260919-DS07`。  
**Version/date:** v1 / 2026-09-19。  
**Freeze status:** `FROZEN BEFORE PROOF AUDIT`。

承接用户自动执行授权；只作本地数学审计，无新数值运行、调参或
原代码修改。本包先冻结问题再推导，不给 249 的域结论补写旧信用。

## 同对象与理想离散族

原始来源、300步动态起点、hbar、L、V_a、顺序均与
[249 比较对象](../249-periodic-kick-domain/candidate-card.md) 相同。
连续空间 H=L²(R/(2L Z),dq)，U=D K_aS ... D K_a1，S=300固定。
K_a 为多项式势的可测周期踢，D 为周期自由 Schrödinger 动能步。
这不是 smooth-Hamiltonian 修复，也不把历史拟合换成另一势。

令偶数 N，H_N 张成 exp(i*pi*k*q/L)/sqrt(2L)，
k=−N/2,...,N/2−1，P_N 为正交投影，q_j=−L+2Lj/N。
I_N 是这些 N 点和模式的三角插值；K_a,N f=I_N(m_a f) 对 f∈H_N；
D_N=D|H_N；U_N 为原次序300步乘积，J_N:H_N→H 为包含映射。
使用精确数学的等距DFT，不将浮点残差等于零作为假设结论。

## 待证明或否证的合同

审核 J_N U_N P_N → U 是否对每个固定 f∈H 强收敛。
如果成立，要求给出不假设相位连续的完整稠密性/有界性证明，
明确使用有界分段连续乘子、固定步数、Riemann求和与离散Parseval。
如果不成立，保存反例或缺口，不把未知标为失败定理。

不得由强L²收敛推出谱点/本征向量排序收敛、能量型域保持、
H_base期望收敛、期望选支定标后百点拟合稳定、算术机制或RH结论。
强收敛与249的单步H¹域不保持可以同时成立，必须解释而非删掉其一。
控制：光滑有限Fourier输入、无踢自由步，以及一般酉算子有限压缩
不保证谱读出控制的 PROVES_TOO_MUCH 风险。

谱系仍是非自治 Logistic 动机 → Hénon 有限几何/量子读出，不是新
算术候选；相空间/roof/闭轨账本在此 `NOT APPLICABLE`。
A0/A1/A2/T0–T3 `NOT EVALUATED`，formal `UNASSIGNED`，B `NOT INVOKED`。
结果若成立仅 `advance` 连续L²所有权；能量/谱拟合晋级保持停止。
