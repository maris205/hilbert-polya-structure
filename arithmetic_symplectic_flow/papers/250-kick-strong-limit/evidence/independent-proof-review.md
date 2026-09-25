# DS07 独立证明审查：FFT 插值踢的强 L² 极限

- 审查对象：`ASFS-DISCOVERY-20260919-DS07`，v1 / 2026-09-19。
- 依据：[完整冻结卡](../candidate-card.md)及其链接的
  [DS06 比较对象](../../249-periodic-kick-domain/candidate-card.md)。
- 本次工作：独立数学推导；无数值运行、谱求解、调参或外部来源补充。
- 结论：**合同中的固定 300 步强 L² 收敛成立**，不要求踢相位在圆周端点接合。
  结果只推进连续 L² 所有权；能量和谱拟合晋级不随之成立。

## 1. 对象及命题

令 \(H=L^2(\mathbb R/(2L\mathbb Z),dq)\)，采用内积
\(\langle f,g\rangle=\int_{-L}^L f\overline g\,dq\)。定义

\[
 e_k(q)=\frac{e^{i\pi kq/L}}{\sqrt{2L}},\qquad
 \Lambda_N=\{-N/2,\ldots,N/2-1\},\qquad
 H_N=\operatorname{span}\{e_k:k\in\Lambda_N\},
\]

其中 \(N\) 沿偶数趋于无穷。\(P_N:H\to H_N\) 为正交投影，
\(J_N:H_N\to H\) 为包含映射；写 \(P_N f\) 时也将它视为一个三角多项式。
网格为 \(q_j=-L+2Lj/N\)，\(j=0,\ldots,N-1\)，网格宽度
\(h_N=2L/N\)。

对 DS07 所有踢，采用冻结的实际代表元

\[
 V_a(q)=-q+q^2+\frac{a q^3}{3}+.05q^4,\qquad
 m_a(q)=\exp(-iV_a(q)/\hbar),\quad -L\le q<L,
\]

并作可测周期延拓。固定 \(L=3.5\)、
\(\hbar=.06138739295586476\)，以及冻结的 300 项实参数序列
\(a_1,\ldots,a_{300}\)。证明不改变该序列，也不利用零点数据。
每个 \(m_a\) 有模长一、在半开基本区间内部光滑、在边界有有限单侧极限；
允许 \(m_a(-L+)\ne m_a(L-)\)。

连续踢为 \(K_a f=m_a f\)。离散踢定义为

\[
 K_{a,N}p=I_N(m_a p),\qquad p\in H_N,
\]

其中 \(I_N\) 是以这些节点和这些模式进行的唯一三角插值。
周期自由步满足

\[
 D e_k=d_k e_k,\qquad
 d_k=\exp\!\left[-\frac{i\hbar}{2}\left(\frac{\pi k}{L}\right)^2\right],
 \qquad D_N=D|_{H_N}.
\]

连续及离散乘积保持原次序：

\[
 U=(DK_{a_{300}})\cdots(DK_{a_1}),\qquad
 U_N=(D_NK_{a_{300},N})\cdots(D_NK_{a_1,N}).
\]

要证明的是：对每个固定 \(f\in H\)，

\[
 \boxed{\ \|J_NU_NP_Nf-Uf\|_{L^2}\longrightarrow0\ }.
\]

这里不对任意 L² 函数作点采样：实际接受采样的是 \(P_N f\in H_N\)。
乘子的逐点代表元由冻结的半开区间公式指定，而不是任取同一 L² 等价类的代表元。

## 2. 精确采样等距与离散踢的统一界

对于 \(k,\ell\in\Lambda_N\)，直接计算有限几何级数得到

\[
 h_N\sum_{j=0}^{N-1}e_k(q_j)\overline{e_\ell(q_j)}
 =\frac1N\sum_{j=0}^{N-1}
 e^{i\pi(k-\ell)(-1+2j/N)}
 =\delta_{k\ell}.
\]

因为非零差 \(k-\ell\) 的绝对值小于 \(N\)，不可能是 \(N\) 的倍数。
故对每个 \(p\in H_N\)，有精确离散 Parseval 恒等式

\[
 \|p\|_2^2=h_N\sum_{j=0}^{N-1}|p(q_j)|^2.
\]

采样映射 \(p\mapsto(\sqrt{h_N}p(q_j))_j\) 因此是两个 N 维 Hilbert
空间之间的酉映射，其逆就是三角插值。由于每个样本 \(|m_a(q_j)|=1\)，

\[
 \|K_{a,N}p\|_2^2
 =h_N\sum_j|m_a(q_j)p(q_j)|^2
 =\|p\|_2^2.
\]

所以 \(K_{a,N}\) 是 \(H_N\) 上的酉算子。将其扩展成

\[
 A_{a,N}=J_NK_{a,N}P_N:H\to H,
\]

便有 \(\|A_{a,N}\|\le1\)，且
\(\|A_{a,N}f\|_2=\|P_Nf\|_2\)。这个扩展在 \(H_N^\perp\) 上为零，
不是整个 H 上的酉算子；证明只需要上述统一有界性。

## 3. 固定三角多项式上的单踢收敛

固定一个三角多项式 \(p\)。充分大时 \(p\in H_N\)。令
\(r_N=J_NK_{a,N}p\)。对每个固定整数 \(k\)，充分大时也有
\(k\in\Lambda_N\)。由离散正交性及插值节点恒等式，

\[
 \begin{aligned}
 \langle r_N,e_k\rangle
 &=h_N\sum_{j=0}^{N-1}r_N(q_j)\overline{e_k(q_j)}\\
 &=h_N\sum_{j=0}^{N-1}m_a(q_j)p(q_j)\overline{e_k(q_j)}.
 \end{aligned}
\]

函数 \(m_a p\overline{e_k}\) 有界且分段连续，因而 Riemann 可积。
等距左端点 Riemann 和收敛到其积分，得到

\[
 \langle r_N,e_k\rangle\longrightarrow
 \langle m_a p,e_k\rangle.
\]

这里包括跨圆周端点的跳跃：Riemann 和不要求所有点连续。将 q=L 的值
补为任意有限单侧值不改变积分；网格上 q=−L 的取值已经明确固定。

由线性性，以上收敛对任意固定三角多项式测试函数成立。
又由 \(\|r_N\|_2=\|p\|_2\) 和 \(\|m_ap\|_2=\|p\|_2\)，
对任意 \(g\in H\) 及三角多项式 \(g_0\)，有

\[
 |\langle r_N-m_ap,g-g_0\rangle|
 \le2\|p\|_2\|g-g_0\|_2.
\]

先用稠密性选择 \(g_0\)，再令 N 趋于无穷，即得
\(r_N\rightharpoonup m_ap\)。此时范数精确相等，故

\[
 \|r_N-m_ap\|_2^2
 =2\|p\|_2^2-2\operatorname{Re}\langle r_N,m_ap\rangle
 \longrightarrow0.
\]

这证明了固定三角多项式输入上的强收敛。没有假设傅里叶系数绝对可和，
也没有把采样 aliasing 忽略成正交投影；aliasing 已包含在插值系数的
Riemann 和中。

## 4. 用稠密性扩展到每个固定 L² 输入

对任意固定 \(f\in H\)，选三角多项式 p。充分大时 \(P_Np=p\)，且

\[
 \begin{aligned}
 \|A_{a,N}f-K_af\|_2
 &\le \|A_{a,N}(f-p)\|_2
       +\|A_{a,N}p-K_ap\|_2+\|K_a(p-f)\|_2\\
 &\le2\|f-p\|_2+\|A_{a,N}p-K_ap\|_2.
 \end{aligned}
\]

中间项由第3节趋零，再让 p 逼近 f，得到

\[
 A_{a,N}\xrightarrow{\mathrm{s}}K_a.
\]

证明实际适用于任意固定、有模长一且在基本区间 Riemann 可积的乘子；
冻结的每个多项式相位乘子都满足这一充分条件。
这一推广是证明的适用范围，不产生新的研究候选。

## 5. 自由步和固定 300 步乘积

由于 D 在同一 Fourier 基上对角且 \(|d_k|=1\)，它与 \(P_N\) 可交换，
并精确保持 \(H_N\)。定义

\[
 B_{s,N}=J_ND_NK_{a_s,N}P_N=DA_{a_s,N},\qquad B_s=DK_{a_s}.
\]

由 D 的酉性与第4节，\(B_{s,N}\to B_s\) 强收敛，且
\(\|B_{s,N}\|\le1\)。对固定有限的 \(S=300\)，有恒等式

\[
 \begin{aligned}
 &(B_{S,N}\cdots B_{1,N}-B_S\cdots B_1)f\\
 &=\sum_{r=1}^{S}
 B_{S,N}\cdots B_{r+1,N}
 (B_{r,N}-B_r)B_{r-1}\cdots B_1f,
 \end{aligned}
\]

空乘积按恒等算子解释。每个右侧输入
\(B_{r-1}\cdots B_1f\) 都是不依赖 N 的固定 L² 向量，因此

\[
 \|(B_{S,N}\cdots B_{1,N}-B_S\cdots B_1)f\|_2
 \le\sum_{r=1}^{S}
 \|(B_{r,N}-B_r)B_{r-1}\cdots B_1f\|_2\longrightarrow0.
\]

有限和即可完成证明；不需要任何中间态保持光滑或保持 H¹。
各离散因子的输出都在 \(H_N\) 内，故相邻的 \(P_NJ_N\) 消去，

\[
 B_{S,N}\cdots B_{1,N}=J_NU_NP_N.
\]

这正是冻结合同所要求的结论，而不是相似对象之间的比较。

## 6. 控制、边界和禁止外推

**无踢控制。** 若 \(m_a\equiv1\)，则 \(K_{a,N}=I_{H_N}\)，
\(J_NU_NP_Nf=D^{300}P_Nf\to D^{300}f\)。这是 Fourier 投影收敛的直接情形。
固定光滑有限 Fourier 输入则由第3节直接处理。

**与 DS06 域障碍的关系。** 强 L² 收敛只控制无权平方和。
若一次踢产生端点跳跃，L² 极限仍然完全合法；它不必属于周期 H¹。
因此它与单步 H¹ 域不保持同时成立，不相互否定。
例如，一般序列 \(e_0+n^{-1}e_{n^2}\) 强 L² 收敛到 \(e_0\)，但其周期动能
二次型值为 \(\hbar^2\pi^2n^2/(2L^2)\)，发散。这个例子只说明
L² 控制不足以控制能量，不声称冻结的300步谱态具有同样行为。

**不是算子范数收敛。** 对每个有限 N，扩展的 \(J_NU_NP_N\) 在
\(H_N^\perp\) 上为零，而 U 是酉算子。因此
\(\|J_NU_NP_N-U\|\ge1\)。强极限成立不等于所有单位输入的统一误差趋零。

**PROVES_TOO_MUCH 谱控制。** 一般强收敛的有限维酉近似，不保证极限有
对应本征向量。例如在同一圆周空间取乘子 \(m(q)=e^{i\pi q/L}\)，
其离散插值踢是 Fourier 模式的循环移位，有限维上有完整本征基；
其连续乘法算子却没有非零 L² 本征向量，因为任何一个水平集
\(\{q:m(q)=\lambda\}\) 都是零测集。第2–4节仍证明它的强收敛。
此为一般方法的负控制，不替换 DS07 的多项式势或自由步。

本审查因而不推出：谱点排序、本征向量排序、随 N 改变的选态、
参考能量 \(H_{\mathrm{base}}\) 的期望、能量型域、百点拟合或其重定标收敛。
尤其不能将这里的“每个固定 f”替换成未经控制的 N 依赖本征态序列。

**固定合同不可省略。** 证明要求 S=300固定，参数序列、L、hbar、步时
及乘法代表元都固定。若步数或参数随 N 变化，有限和论证不自动适用。
这里也没有误差率、有限 N 精度保证或浮点稳定性结论。
对任意可测但不 Riemann 可积的乘子，点采样可依赖零测集上的改值；
本证明没有覆盖那种扩大后的假设。

## 7. 审查交接

DS07 的单对象账本保持完整：同一圆周、同一300步参数路径、同一可测多项式
踢、同一自由步及同一插值约定。数学结果为 `advance` 连续 L² 所有权。
能量/谱拟合晋级仍保持停止，下一步不能跳过独立的谱与读出控制。
A0/A1/A2/T0–T3 均 `NOT EVALUATED`；formal `UNASSIGNED`；B `NOT INVOKED`。
本文给出自足证明，没有将未核对的外部引文当作依据，也没有把模型审查当作同行评审。
