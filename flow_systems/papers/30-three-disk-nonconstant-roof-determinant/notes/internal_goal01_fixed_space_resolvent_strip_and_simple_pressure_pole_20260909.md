# P30 Goal01：固定 Hölder 空间的 resolvent 条带与简单压力极点

日期：2026-09-09 UTC。持续授权内的新纸面推论；仅新增本文件。

**结论范围。** 在原等边三盘、原真实时钟的一侧正 roof g 及原固定
\(\mathcal B_\beta\) 上，存在 \(\eta>0\)，使
\[
 \mathscr R(s):=(I-\mathcal L_s)^{-1}
\]
在 \(|\operatorname{Re}s-h_T|<\eta\) 内除 \(s=h_T\) 外全纯，
且该点有一个明确的 rank-one 简单极点。证明使用新补齐的固定
全 Hölder 空间高频界，不把周期 zeta 的标量延拓直接当成算子结论。

以下是经典 transfer resolvent，不是物理散射 resolvent、量子
Hamiltonian resolvent、Fredholm determinant 或 Route 晋级。
ARS 的有界论证组织用于将谱半径、算子逆、参数全纯及定量界分开。

## 1. 固定对象与已核查输入

采用[一侧 roof 笔记][roof]的全部固定选择：
原等边三盘半径 a>0、中心距离 6a、单位速率，标准交替过去，
固定有限平均，\(\beta=\alpha/2\)，\(q=\theta^\beta\in(0,1)\)，
\[
 \mathcal B_\beta=C^\beta(\Sigma^+,d_\theta^+;\mathbb C),\qquad
 \mathcal L_su(x)=\sum_{j\ne x_0}e^{-sg(jx)}u(jx),\qquad
 2a\le g\le10a.
 \tag{1}
\]
本篇不换到新几何族的较小 beta，不把不同 Banach 模型的谱等同。
s→L_s 在这个固定 Banach 空间上算子范数整。

对实 t，令 \(\lambda_t=r(\mathcal L_t)>0\)。[实 RPF 与局部分支][low]
给简单正本征值、正函数 \(H_t\)、正本征测度 \(\nu_t\)，规范化
\(\nu_t(H_t)=1\)，以及 \(\mu_t=H_t\nu_t\)。
[压力与物理熵身份][entropy]给
\[
 h:=h_T>0,\qquad \lambda_h=1,\qquad
 \partial_t\log\lambda_t=-\mu_t(g)<0.
 \tag{2}
\]
原固定 g 与同一物理轨道的对应已由上述输入建立。

另外使用两个不同频段的输入：

- [固定频率笔记][finite]：对每个实 t、每个 b≠0，
  \(r(\mathcal L_{t+ib})<\lambda_t\)；在实紧区间和
  \(0<\delta\le|b|\le B<\infty\) 上，归一化谱半径有统一小于 1 的上界。
  该结论包括任意常相位 circle coboundary 的排除，不仅排除 eigenvalue 1。
- [固定全空间高频笔记][high]：存在以 h 为内点的实紧区间 \(I_0\)，
  常数 \(B_0\ge e^2\)、\(C\ge1,K>0,c>0\)，对 t∈I_0、
  \(B=|b|\ge B_0\)、所有整数 n≥0，有
  \[
   \|\lambda_t^{-n}\mathcal L_{t+ib}^{\,n}\|_{\beta,b\to\beta,b}
   \le C\min\{1,B^Ke^{-cn}\},\qquad
   \|u\|_{\beta,b}:=\|u\|_\infty+B^{-1}[u]_\beta.
   \tag{3}
  \]
  它由源定理的纯 roof 版本、本案 cylinder 几何分离、
  同一显式 coboundary 和两段 Lasota–Yorke 推出。
  本篇不再把该新接口列作悬空假设，也不将它称为原文直接陈述。

(3) 的范数随 b 加权，但空间的集合与固定 \(\|\cdot\|_\beta\) 不变。
对每个固定 b 两者等价；全纯性以下仍在固定算子范数中理解，
不能从“频率加权界”单独推导参数全纯。

## 2. 高频部分先给真正的统一谱半径下降

对每个固定 (t,b)，在 (3) 中取 n 次方根及上极限，得到
\[
 r(\mathcal L_{t+ib})\le \lambda_t e^{-c},
 \qquad t\in I_0,\quad |b|\ge B_0.
 \tag{4}
\]
范数等价不改变谱半径；常数 CB^K 在固定 b 的 n 次方根下趋于 1。
(4) 是先有全空间幂界才得到的结论，不是仅有逐点
\(r<\lambda_t\) 时擅取无限频段的 supremum。

因为 \(\lambda_h=1\) 且 t→λ_t 连续，可在 h 附近选较小区间，使
\[
 \sup_t\log\lambda_t<c/2.
 \tag{5}
\]
于是此区间的全部高频满足 \(r(\mathcal L_{t+ib})<e^{-c/2}<1\)，
故 \(I-\mathcal L_{t+ib}\) 可逆。

## 3. 原点附近的简单谱分支与精确 residue

实 RPF 在 h 给 rank-one 投影
\[
 \Pi_hu=H_h\,\nu_h(u),\qquad \nu_h(H_h)=1,
 \tag{6}
\]
其余谱严格位于单位圆内。由固定算子族的整性与 Riesz 投影，
存在复圆盘 \(\mathbb D(h,r_0)\) 及解析分支 \(\Lambda(s),\Pi(s)\)，使
\[
 \Lambda(h)=1,\quad \Pi(h)=\Pi_h,\quad
 \operatorname{rank}\Pi(s)=1,\qquad
 \mathcal L_s=\Lambda(s)\Pi(s)+N(s),
 \quad N(s)\Pi(s)=\Pi(s)N(s)=0,
 \tag{7}
\]
且 \(I-N(s)\) 在该盘全纯可逆。可通过先隔开 h 的余谱，再缩小盘，
保证余谱没有到达 1；无需假设 \(\|N(h)\|<1\)。

由 (1) 的直接微分与 \(\nu_h\mathcal L_h=\nu_h\)，
\[
 \Lambda'(h)
 =\nu_h(\mathcal L'_h H_h)
 =-\nu_h(\mathcal L_h(gH_h))
 =-\mu_h(g)=:-m_h,\qquad m_h\in[2a,10a].
 \tag{8}
\]
因此缩小 r_0 后，
\[
 1-\Lambda(s)=(s-h)d(s),\qquad
 d(h)=m_h>0,\quad d(s)\ne0
 \quad(s\in\mathbb D(h,r_0)).
 \tag{9}
\]
对于 s≠h，
\[
 \mathscr R(s)
 =\frac{\Pi(s)}{1-\Lambda(s)}
  +(I-N(s))^{-1}(I-\Pi(s)).
 \tag{10}
\]
由 (9)–(10)，
\[
 \boxed{\displaystyle
 \mathscr R(s)=\frac{\Pi_h}{m_h(s-h)}+\mathscr H(s),
 \qquad \mathscr H\text{ 在 }\mathbb D(h,r_0)\text{ 全纯}.}
 \tag{11}
\]
余项全纯的理由是
\(\Pi(s)/d(s)-\Pi_h/m_h\) 在 h 为零，可除以 s−h；
另一项已在 (10) 全纯。由于 \(\Pi_h\ne0\)，此极点确实存在，
不是仅有一个“允许的候选极点”。

\(\Pi_h\) 是这个 Banach 空间中的谱投影，不宣称是某个未定义
Hilbert 内积下的正交投影。residue 的正号来自 (8) 的负导数。
本篇也不把 \(m_h\) 改成几何常数或另一测度下的平均。

## 4. 有限中频补合成一条开竖条带

取 \(0<\delta<\min\{r_0/3,B_0\}\)。选择一个较小闭实区间
\(I_1\subset I_0\)，h 在其内部。对紧集
\[
 \mathcal K=I_1\times\{b:\delta\le|b|\le B_0\},
\]
[finite] 的统一结论给
\[
 \sup_{\mathcal K}
 r(\lambda_t^{-1}\mathcal L_{t+ib})\le\kappa_{\rm mid}<1.
 \tag{12}
\]
此处只能在有限紧频段这样使用既有结论；无限高频由 (4) 另外处理。

再取 \(\eta>0\)，使
\[
 [h-\eta,h+\eta]\subset I_1,\qquad \eta<r_0/3,
\]
\[
 \sup_{|t-h|\le\eta}\lambda_t\kappa_{\rm mid}<1,\qquad
 \sup_{|t-h|\le\eta}\log\lambda_t<c/2.
 \tag{13}
\]
λ_h=1、κ_mid<1 保证这样的 η 存在。于是：

- 若 |b|≥B_0，由 (4)、(13) 得 \(r(\mathcal L_s)<1\)。
- 若 δ≤|b|≤B_0，由 (12)、(13) 同样得到 \(r(\mathcal L_s)<1\)。
- 若 |b|<δ 且 |Re s−h|<η，则
  \(|s-h|<\sqrt2\,r_0/3<r_0\)，由 (9)–(10) 可逆，唯独 s=h 除外。

所以在整个
\[
 \mathcal S_\eta=\{s\in\mathbb C:|\operatorname{Re}s-h|<\eta\}
 \tag{14}
\]
上，\(I-\mathcal L_s\) 只在 h 不可逆。算子逆在可逆群上局部全纯，
而 s→L_s 是固定范数整函数；各局部逆由唯一性相容，得到 (14) 上
除 h 外的全纯 \(\mathscr R\)，并由 (11) 给唯一简单极点。

注意 t<h、b 很小时 \(\lambda_t>1\) 可以成立。
这不与本结论矛盾：需要的是 1 不在谱中，不是整条条带内
每一点的整个谱半径都小于 1。该低频区域用 (10)，不用错误的
单位圆内 Neumann 断言。

## 5. 非归一化 resolvent 的定量高频界

(3) 中的 \(\lambda_t^{-n}\) 不能在求和时遗漏。本节显式处理它。
令 \(I'\subset[h-\eta,h+\eta]\) 为含 h 的闭实区间，并记
\[
 a_{I'}:=\max\{0,\sup_{t\in I'}\log\lambda_t\}<c/2.
 \tag{15}
\]
a_{I'} 只是实压力增长上界，不是圆盘半径 a。
由 (3)，对 t∈I'、B≥B_0，
\[
 \|\mathcal L_s^n\|_{\beta,b}
 \le C e^{a_{I'}n}\min\{1,B^Ke^{-cn}\}.
 \tag{16}
\]
这里 \(\|\cdot\|_{\beta,b}\) 简写相应算子范数。
按
\[
 n_*=\left\lceil(K/c)\log B\right\rceil
 \tag{17}
\]
拆分 Neumann 级数。前 n_* 项由 (16) 的第一分支给
\[
 \sum_{0\le n<n_*}\|\mathcal L_s^n\|_{\beta,b}
 \le C n_* e^{a_{I'}n_*}
 \le C_1(1+\log B)B^{Ka_{I'}/c}.
 \tag{18}
\]
尾部由第二分支、\(c-a_{I'}>c/2\) 给
\[
 \sum_{n\ge n_*}\|\mathcal L_s^n\|_{\beta,b}
 \le \frac{CB^K e^{-(c-a_{I'})n_*}}
           {1-e^{-(c-a_{I'})}}
 \le C_2 B^{Ka_{I'}/c}.
 \tag{19}
\]
因此该级数实际算子范数绝对收敛，且
\[
 \boxed{\displaystyle
 \|\mathscr R(t+ib)\|_{\beta,b}
 \le C_3(1+\log B)B^{Ka_{I'}/c},
 \qquad t\in I',\quad B=|b|\ge B_0.}
 \tag{20}
\]
这是真正的非归一化 \(I-\mathcal L_s\) 逆，不再是
\(I-\lambda_t^{-1}\mathcal L_s\) 的逆。

在 t=h，\(a_{\{h\}}=0\)，故
\[
 \|\mathscr R(h+ib)\|_{\beta,b}\le C_3(1+\log|b|).
 \tag{21}
\]
若预先给任意 \(\epsilon>0\)，连续性允许再缩小实宽度，使
\(Ka_{I'}/c<\epsilon/2\)。结合
\(1+\log B\le C_\epsilon B^{\epsilon/2}\)，得到该较窄闭条带上的
\[
 \|\mathscr R(t+ib)\|_{\beta,b}\le C_\epsilon |b|^\epsilon.
 \tag{22}
\]
条带宽度与常数可以依赖 ε；不声称在原来固定宽度中同时享有所有 ε。
(20)–(22) 仍是频率加权范数，不能不加等价因子就叫作原强范数界。
例如 B≥1 时
\[
 \|u\|_{\beta,b}\le\|u\|_\beta\le B\|u\|_{\beta,b},
\]
所以从 (22) 直接得到的固定强范数上界至多
\(C_\epsilon B^{1+\epsilon}\)，不是同一个 \(B^\epsilon\)。

## 6. 这条闭合链没有附送什么

本篇建立的对象是原固定一侧 transfer operator 的谱逆与条带。
这里既没有定义 \(\det(I-\mathcal L_s)\)，也没有证明其普通核性、
trace-class 性或一个 Fredholm determinant 的存在。
\(\mathscr R\) 的极点因此不能直接当成某个未构造 determinant 的零点。

先前[经典 zeta 同轨道延拓][zeta]已经给相同物理 h_T 的简单极点。
两项结论可以分别成立，但“极点位置相同”本身不是全局函数身份、
完整谱／零点重数等式或 quantum determinant。
本篇不把分布平坦迹的时间积分等同于 \(\mathscr R\) 的普通迹。

此外，没有在几何参数邻域取得 source 高频常数的一致性；
没有全平面固定空间 resolvent、实际波／散射算子的共振身份、
自伴 Hilbert–Pólya 算子或 Route／Stage 判定。
P30 现有失败记录和所有正式执行停止条件不变。

本篇是 AI 辅助内部纸面推导。主代理使用上述已经逐式读审的本地
输入，并实际核读 Petkov–Stoyanov 的编码／纯 roof 高频来源段落；
新增贡献在本页是三频段拼合、rank-one residue 和未归一化级数估计。
通过 apply_patch 只新增本文件，没有运行科学、符号、谱数值、
枚举、producer 或稿件 build。后继差异读审与文本检查由工作索引记录。

[roof]: internal_goal01_one_sided_roof_and_transfer_bounds_20260909.md
[low]: internal_goal01_positive_variance_and_low_frequency_branch_20260909.md
[entropy]: internal_goal01_pressure_equals_physical_entropy_20260909.md
[finite]: internal_goal01_fixed_frequency_spectral_gap_20260909.md
[high]: internal_goal01_full_holder_high_frequency_from_cylinder_approximation_20260909.md
[zeta]: internal_goal01_classical_zeta_continuation_same_orbits_20260909.md
