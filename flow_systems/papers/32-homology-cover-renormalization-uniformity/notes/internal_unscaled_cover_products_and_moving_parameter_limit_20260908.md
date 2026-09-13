# P32 内部研究：未缩时覆盖乘积、精确阈值与移动参数主项

记录日期：2026-09-08 UTC。接续[几何覆盖塔与长度截断][geometry-note]。本轮有两类互补结论：借用已发表研究中的素测地线计数定理，确定完整普通 Euler 乘积的正实收敛阈值；另从既有几何初等证明 content–长度统一界，得到移动参数下的指数误差及有限字符分解。

原对象仍使用规定的 `1/N` 周期缩放和 `1/N^3` 对数归一化。本轮不更换它们，不启动规范枚举或实验，不构造谱算子，不修改论文或正式审查状态。下文新引入的覆盖度数归一化量明确标为辅助对象。

## 1. 输入与两种参数

沿用同一个真实、带标记的闭双曲亏格二曲面、全体本原有向基流 owner 集 `O`、物理长度 `ell_g>0` 及整数同调

\[
\alpha_g=\alpha(g)\in\mathbb Z^4.
\]

`O_0` 指 `alpha_g=0`，`O_+` 指 `alpha_g!=0`。正 owner 的 `d_g` 是四个坐标绝对值的最大公约数，严格为正。逆向 owner 不合并，不以轨道起点重复计数。固定层定义为

\[
m_{N,g}=
\begin{cases}
\gcd(N,d_g),&g\in\mathcal O_+,\\
N,&g\in\mathcal O_0,
\end{cases}
\qquad h_{N,g}=N/m_{N,g}.
\]

上轮已证明覆盖轨道被完整的基底提升块分拆：每块有 `N^3 m_(N,g)` 条本原覆盖轨道，每条未缩时周期为 `h_(N,g) ell_g`。沿用

\[
L_t(z)=\sum_{r\ge1}\frac{e^{-rzt}}r,\qquad
\mathscr L_N(s)=\sum_gm_{N,g}L_{\ell_g/m_{N,g}}(s),
\qquad Q_N(s)=e^{\mathscr L_N(s)}.
\]

`s` 是原缩时乘积的参数；`w` 是未缩时参数。记未缩时覆盖乘积的归零对数为

\[
\mathscr U_N(w):=\mathscr L_{V,N}(Nw)
=N^3\mathscr L_N(Nw)
=N^3\sum_gm_{N,g}L_{h_{N,g}\ell_g}(w),
\qquad U_N(w)=e^{\mathscr U_N(w)}.
\]

这些无限等式已在 `Re(w)>1`、即 `Re(s)>N` 上成立。全基准记为

\[
\mathscr B(w)=\sum_gL_{\ell_g}(w),\qquad B(w)=e^{\mathscr B(w)}.
\]

上轮另已给出 `ell_*>0`、`C_cnt>0`，使所有 `ell_g>=ell_*`、`n(L)<=C_cnt e^L`，并证明对每个 `a>1` 有

\[
S_0(a)=\sum_ge^{-a\ell_g}<\infty,\qquad
\sum_{\ell_g>T}e^{-a\ell_g}
\le\frac{aC_{\rm cnt}}{a-1}e^{-(a-1)T}.
\]

这些是实际固定几何下的理论结果，不再作为尚待证明的抽象求和假设；常数仍未数值认证。

## 2. 全体同调向量受物理长度线性控制

### 2.1 从有限位移集到同调上界

使用上轮固定的 `x in H^2` 与 `D=diam(Sigma)+1`：轨道 `Gamma x` 是 `D`-稠密的，而且每个有界位移集合有限。定义

\[
S=\{\gamma\in\Gamma:\operatorname{dist}(x,\gamma x)\le2D+1\}.
\]

`S` 有限。对非恒等 `gamma`，令 `R=dist(x,gamma x)>0`，把从 `x` 到 `gamma x` 的测地段分成 `q=ceil(R)` 段，每段长度至多为一。各中间分点选择一个距离至多 `D` 的轨道点 `gamma_j x`，首尾明确取 `gamma_0=1`、`gamma_q=gamma`。于是

\[
\operatorname{dist}(x,\gamma_{j-1}^{-1}\gamma_jx)
=\operatorname{dist}(\gamma_{j-1}x,\gamma_jx)\le2D+1.
\]

所以每个 `delta_j=gamma_(j-1)^(-1) gamma_j` 属于 `S`，且 `gamma=delta_1...delta_q`。这同时证明 `S` 生成 `Gamma`，无需先认证一份数值基本多边形或生成词表。

令

\[
M=\max_{\delta\in S}\|\alpha(\delta)\|_\infty.
\]

`M` 有限；由于 `S` 生成 `Gamma` 且 `alpha` 满射，`M>0`。同调的可加性给出

\[
\|\alpha(\gamma)\|_\infty
\le M\bigl(\operatorname{dist}(x,\gamma x)+1\bigr).
\]

恒等元的情形也满足此不等式。

### 2.2 用同一个元素的幂去掉加性常数

固定任意 owner 的群代表 `g`，令 `rho_g=dist(x,axis(g))`。它的测地轴及平移长度已由[既有 owner 绑定][owner-note]确定。对每个正整数 `n`，

\[
\operatorname{dist}(x,g^nx)\le n\ell_g+2\rho_g,
\qquad \alpha(g^n)=n\alpha(g).
\]

对 `g^n` 应用上界，除以 `n` 后令 `n` 趋于无穷，得到

\[
\boxed{\|\alpha_g\|_\infty\le M\ell_g\quad(g\in\mathcal O),\qquad
d_g\le M\ell_g\quad(g\in\mathcal O_+).}
\]

这里没有要求各 `rho_g` 有共同上界：先固定一个 owner，再对它的幂取极限即可。最后得到的 `M` 与 owner 无关，依赖的是固定几何、标记和已固定的长度单位。零 owner 不具有正 `d_g`，后文不会对它使用 `m_(N,g)<=d_g`。

### 2.3 一个加权指数和

为使后续误差没有多余的 `N` 前因子，对 `b>1` 记

\[
S_1(b)=\sum_g\ell_ge^{-b\ell_g}.
\]

因为

\[
\ell e^{-b\ell}\le\int_\ell^\infty bu\,e^{-bu}\,du,
\]

对非负项先作有限求和，再通过单调极限，得到

\[
S_1(b)\le\int_0^\infty bu\,e^{-bu}n(u)\,du
\le\frac{bC_{\rm cnt}}{(b-1)^2}<\infty.
\]

这一步只使用上轮计数界，不依赖第 3 节的外部素测地线定理。

## 3. 完整普通 Euler 乘积的精确正实阈值

### 3.1 使用的外部计数结论及其范围

Wu–Xue 的作者版论文 *Prime geodesic theorem and closed geodesics for large genus*，arXiv v3，第 1 页明确采用本原有向闭测地线；Theorem 2（第 2–3 页）适用于任意固定闭双曲曲面，Theorem 21（第 13 页）给出相同口径及证明入口。这不同于该文的随机曲面结论。固定曲面后，其误差是 `o(t/log t)`，额外的 `Li` 项最终非负，因而对每个这样的曲面 `X` 存在 `c_X>0,L_X>0`，使

\[
n_X(L)\ge c_X\frac{e^L}{L}\qquad(L\ge L_X).
\]

此处只借用这个最终下界，不需要跨覆盖层的一致误差常数，也不另乘或除以二。[作者版指定定理][pgt-source]；书目身份及 DOI 由[EMS 官方条目][pgt-metadata]核对。下述阈值推导是该外部定理在本项目规定产品上的应用，并非本轮重新证明素测地线定理。

### 3.2 临界点需要积分论证

固定任意层 `N`，取 `X=Sigma_N`，以 `tau` 表示其全部本原有向轨道的未缩时周期。对实数 `u>0`，非负积分恒等式给出

\[
\sum_{\widetilde\gamma}e^{-u\tau_{\widetilde\gamma}}
=\int_0^\infty u e^{-uL}n_X(L)\,dL.
\]

若 `0<u<=1`，右侧至少包含

\[
c_Xu\int_{L_X}^\infty\frac{e^{(1-u)L}}L\,dL=+\infty.
\]

因此包括临界点 `u=1` 在内，单重复项 `r=1` 已不可求和。不能仅用 `e^{-T}n_X(T)` 的下界处理临界点，因为那个量的所给下界趋于零。

每个实数 Euler 对数 `L_tau(u)>=e^{-u tau}`，故未缩时完整普通乘积在 `0<u<=1` 发散到正无穷；`u>1` 的有限值收敛已由上轮证明。完整提升块共尾性使这一结论传回基底 owner 有限子集网。

用[扩展实轴接口][interface-note]的记号，遂有

\[
\boxed{
\mathcal Q_N(s)<\infty\iff s>N,\qquad
\mathcal B(s)<\infty\iff s>1
\quad(s>0).}
\]

这里 `mathcal Q_N` 和 `mathcal B` 在其余正实参数处均为 `+infinity`。在有限值区域，它们与既有全纯产品的实轴取值一致。

对于复参数，规定的覆盖轨道／重复次数双级数的绝对值和恰为相应正实级数。因此其精确绝对收敛半平面为 `Re(w)>1`，缩时后为 `Re(s)>N`；在实部非正时，单个轨道的重复次数级数已不绝对收敛。这是绝对 Euler 级数的边界，不排除条件收敛、另一种求和方式或另行证明的解析延拓；本轮没有构造它们。

### 3.3 相对产品与 N=1 例外

单 owner 相对因子为

\[
r_{N,g}(s)=
\frac{(1-e^{-s\ell_g/m_{N,g}})^{-m_{N,g}}}
{(1-e^{-s\ell_g})^{-1}}\ge1.
\]

固定 `N,g`，其对数导数为

\[
\frac{d}{ds}\log r_{N,g}(s)
=-\frac{\ell_g}{e^{s\ell_g/m_{N,g}}-1}
+\frac{\ell_g}{e^{s\ell_g}-1}\le0.
\]

于是每个有限相对乘积及其扩展上确界 `mathcal R_N` 均随 `s` 非增。若 `N>=2`，在 `s=N` 有 `B(N)<infinity`、`mathcal Q_N(N)=infinity`，故

\[
\mathcal R_N(N)=\mathcal Q_N(N)/B(N)=+\infty.
\]

单调性向左传递，再结合 `s>N` 时两乘积均有限，得到

\[
\boxed{
\begin{array}{ll}
N\ge2:&\mathcal R_N(s)<\infty\iff s>N,\\
N=1:&\mathcal R_1(s)=1\quad\text{对全部 }s>0.
\end{array}}
\]

`N=1` 时每个局部比值恒为一，即使 `s<=1` 时两个原乘积均为无穷，也不能写成 `infinity/infinity` 来定义它。

因此，对任意固定实数 `s>0`，所有满足 `N>=2` 且 `N>=s` 的整数层已经有 `mathcal Q_N(s)=mathcal R_N(s)=infinity`。这加强了上轮仅凭见证得到的层数发散：现在对完整 owner 集，足够大的每一固定层本身就无穷。该结论不自动给出随 `N` 一致的有限截断发散速度，也没有确定单独正 owner 子乘积的精确临界点。

## 4. 移动参数 s=Nw 下的指数主项

### 4.1 正分支的全局指数衰减

固定任意 `1<b<a`，令

\[
c_a=1-e^{-a\ell_*}>0,\qquad
\kappa_{a,b}=\frac{a-b}{M}>0,\qquad
\eta_{a,b}(N)=
\frac{MbC_{\rm cnt}}{c_a(b-1)^2}e^{-\kappa_{a,b}N}.
\]

对正 owner，`m_(N,g)<=d_g<=M ell_g` 且 `m_(N,g)<=N`，故未缩时块周期

\[
T_{N,g}=h_{N,g}\ell_g=\frac{N\ell_g}{m_{N,g}}
\]

同时满足 `T_(N,g)>=ell_g` 与 `T_(N,g)>=N/M`。因此

\[
aT_{N,g}\ge b\ell_g+(a-b)N/M.
\]

由单周期级数的绝对值界，对全部 `Re(w)>=a`，

\[
\begin{aligned}
\sum_{g\in\mathcal O_+}
\left|m_{N,g}L_{T_{N,g}}(w)\right|
&\le\frac1{c_a}\sum_{g\in\mathcal O_+}
m_{N,g}e^{-aT_{N,g}}\\
&\le\frac{M S_1(b)}{c_a}e^{-\kappa_{a,b}N}\\
&\le\eta_{a,b}(N).
\end{aligned}
\]

令这个正分支日志为

\[
E_N^+(w)=\mathscr L_N^+(Nw).
\]

所得界控制的是绝对总和，而不只是依赖抵消的总值；同样控制任意有限正 owner 子集的日志。沿全部整数 `N->infinity`，

\[
\boxed{
\sup_{\operatorname{Re}w\ge a}|E_N^+(w)|
\le\eta_{a,b}(N)\longrightarrow0,\qquad
\sup_{\operatorname{Re}w\ge a}|Q_N^+(Nw)-1|
\le e^{\eta_{a,b}(N)}-1.}
\]

每个 `a>1` 都允许选 `1<b<a`，所以这覆盖整个 `Re(w)>1` 的局部一致结论，不要求 `N` 是阶乘或 `gcd(N,d_g)` 随全整数单调。

### 4.2 零分支给出完整乘积的主项

定义新的明确标量函数

\[
\mathscr B_0(w)=\sum_{g\in\mathcal O_0}L_{\ell_g}(w),
\qquad B_0(w)=e^{\mathscr B_0(w)},\qquad\operatorname{Re}w>1.
\]

它是基准乘积的零同调子乘积，全纯且非零；不是跨零 owner 的 Hahn 乘法或整个形式载体的求值。因为零 owner 有 `m_(N,g)=N`，其移动参数日志恰为 `N L_(ell_g)(w)`。因此

\[
\boxed{
\mathscr L_N(Nw)=N\mathscr B_0(w)+E_N^+(w),\qquad
\sup_{\operatorname{Re}w\ge a}
\left|\frac{Q_N(Nw)}{B_0(w)^N}-1\right|
\le e^{\eta_{a,b}(N)}-1.}
\]

这是未改变原 `N^{-3}` 归一化的相对渐近；移动的是参数，且明确在原产品每一层均有定义的区域内。

相对产品的基准也可控制。记

\[
\beta_{a,b}(N)=
\frac{S_0(b)}{c_a}e^{-(Na-b)\ell_*}.
\]

由 `N>=1`、`Na-b>0` 和 `ell_g>=ell_*`，

\[
\sup_{\operatorname{Re}w\ge a}|\mathscr B(Nw)|
\le\frac1{c_a}\sum_ge^{-Na\ell_g}
\le\beta_{a,b}(N)\longrightarrow0.
\]

所以

\[
\boxed{
\sup_{\operatorname{Re}w\ge a}
\left|\frac{R_N(Nw)}{B_0(w)^N}-1\right|
\le e^{\eta_{a,b}(N)+\beta_{a,b}(N)}-1.}
\]

正分支的 `R_N^+(Nw)` 也趋于一，使用相同上界即可。注意这里比较的是 `B(Nw)`，不是固定参数的 `B(w)`。

### 4.3 实增长与复相位

[已有零 owner][owner-note]保证 `O_0` 非空，因此对每个实数 `w>1` 有 `mathscr B_0(w)>0`。在任意非空实紧区间 `I subset (1,infinity)` 上，它具有正的最小值，故 `Q_N(Nw)`、`R_N(Nw)` 均一致趋于正无穷，而正分支单独趋于一。

对复数不能把这一结论机械传递。以下 `K` 均为 `{Re(w)>1}` 内的非空紧集。相对渐近保留了 `B_0(w)^N` 的完整相位：若 `inf_K Re(mathscr B_0)>0`，则模长一致发散；若 `sup_K Re(mathscr B_0)<0`，则模长一致趋零。这里不声称后一类紧集一定存在，也不对 `Re(mathscr B_0)=0` 的集合给出普遍极限。

## 5. 有限字符分解与 Haar 对数平均

本节给出纯 Euler 级数层面的另一种表示，不借助谱算子、迹公式或 Artin 型谱行列式恒等式。

### 5.1 全部有限 deck 字符

对 `theta in T^4=R^4/Z^4`，定义

\[
\mathscr T(w,\theta)=
\sum_g\sum_{r\ge1}
\frac{e^{2\pi i r\langle\theta,\alpha_g\rangle}
e^{-rw\ell_g}}r,\qquad
B_\theta(w)=e^{\mathscr T(w,\theta)}.
\]

对每个 `a>1`，这族级数在 `Re(w)>=a`、全部 `theta` 上的绝对总和至多为 `S_0(a)/c_a`。因此它关于 `theta` 连续、关于 `w` 全纯，并允许下面的换和与积分。各级数对数沿正实 `w->infinity` 归零；没有使用未指定分支的 `log B_theta`。

全部字符可写为 `theta=b/N`，其中 `b` 遍历 `(Z/NZ)^4`。每个坐标的有限几何级数相乘给出

\[
\sum_{b\in(\mathbb Z/N\mathbb Z)^4}
e^{2\pi i r\langle b/N,\alpha_g\rangle}
=N^4\mathbf1_{\{r\alpha_g\in N\mathbb Z^4\}}
=N^4\mathbf1_{\{h_{N,g}\mid r\}}.
\]

于是，对每个 owner，

\[
\sum_b\sum_{r\ge1}
\frac{e^{2\pi i r\langle b/N,\alpha_g\rangle}e^{-rw\ell_g}}r
=\frac{N^4}{h_{N,g}}L_{h_{N,g}\ell_g}(w)
=N^3m_{N,g}L_{h_{N,g}\ell_g}(w).
\]

对 owner 求和并利用完整提升块分拆，得到

\[
\boxed{
\mathscr U_N(w)=\sum_b\mathscr T(w,b/N),\qquad
U_N(w)=\prod_bB_{b/N}(w),\quad\operatorname{Re}w>1.}
\]

若 deck 作用采用逆字符约定，只会重新排列全部字符，不改变恒等式；有向 owner 口径已一致，不额外加二倍因子。

### 5.2 度数归一化辅助量与零同调投影

明确另定义

\[
A_N(w)=N^{-4}\mathscr U_N(w)
=N^{-1}\mathscr L_N(Nw)
=\frac1{N^4}\sum_b\mathscr T(w,b/N).
\]

这是覆盖度数归一化的辅助日志，不是把原合同中的 `N^{-3}` 改成 `N^{-4}`。第 4 节直接给出

\[
\boxed{
\sup_{\operatorname{Re}w\ge a}|A_N(w)-\mathscr B_0(w)|
\le\frac{\eta_{a,b}(N)}N,\qquad
e^{A_N(w)}\longrightarrow B_0(w).}
\]

另一方面，对 `T^4` 上质量为一的 Haar 测度，

\[
\int_{\mathbb T^4}
e^{2\pi i r\langle\theta,\alpha_g\rangle}\,d\theta
=\mathbf1_{\{\alpha_g=0\}}\qquad(r\ge1),
\]

因为整数同调群无挠。统一绝对收敛允许逐项积分，从而

\[
\boxed{\int_{\mathbb T^4}\mathscr T(w,\theta)\,d\theta
=\mathscr B_0(w).}
\]

所以辅助极限是有限字符日志平均趋向 Haar 日志平均；最终投影保留整数同调为零的 owner，而非把当层“模 `N` 为零”的非零同调误认成零同调。这也不是无限阿贝尔覆盖上未归一化的全部轨道乘积。

### 5.3 不能把平均与指数化交换

一个仅说明代数接口的两因子例子如下。取 `0<z<1`、归一化圆周测度，两因子的同调频率分别为 `1,-1`。它们的级数对数平均为零，但

\[
\int_0^{2\pi}
\frac{d\theta/(2\pi)}
{(1-ze^{i\theta})(1-ze^{-i\theta})}
=\sum_{j\ge0}z^{2j}=\frac1{1-z^2}\ne1.
\]

最后等式来自两个绝对收敛几何级数中只有相等次数被积分保留。因此本节并未声称 `integral B_theta=exp(integral mathscr T)`。这是解析反例，不是 P32 的数值实验。

## 6. 移动参数下的有限长度截断

令 `E(T)={g:ell_g<=T}`，`E_0(T)=E(T) intersect O_0`；对有限 `F subset O_0`，记 `mathscr B_(0,F)(w)=sum_(g in F)L_(ell_g)(w)`，空和为零。对任意有限 owner 集合 `E`，第 4 节的绝对总和界仍给出

\[
\mathscr L_{N,E}(Nw)
=N\mathscr B_{0,E\cap\mathcal O_0}(w)+E_{N,E}^+(w),
\qquad
\sup_{\operatorname{Re}w\ge a}|E_{N,E}^+(w)|\le\eta_{a,b}(N).
\]

因而相对于当层零 owner 子乘积的 `N` 次幂，误差对所有有限 `E` 统一，不要求穷尽。

若要与完整固定主项 `B_0(w)^N` 比较，定义

\[
\tau_a(T)=\frac{aC_{\rm cnt}}{c_a(a-1)}e^{-(a-1)T}.
\]

上轮指数尾界给出

\[
\sup_{\operatorname{Re}w\ge a}
|\mathscr B_0(w)-\mathscr B_{0,E_0(T)}(w)|
\le\tau_a(T).
\]

于是两种精度须分开：

\[
\boxed{
\sup_{\operatorname{Re}w\ge a}
\left|\frac{\mathscr L_{N,E(T)}(Nw)}N-\mathscr B_0(w)\right|
\le\frac{\eta_{a,b}(N)}N+\tau_a(T),}
\]

\[
\boxed{
\sup_{\operatorname{Re}w\ge a}
\left|\frac{Q_{N,E(T)}(Nw)}{B_0(w)^N}-1\right|
\le e^{\eta_{a,b}(N)+N\tau_a(T)}-1.}
\]

所以对任意实数序列 `T_N>=0`、`T_N->infinity`，第一种归一化日志误差趋零。第二种相对产品误差由本界保证趋零的充分条件是

\[
(a-1)T_N-\log N\longrightarrow+\infty.
\]

这是特定误差界的充分截断速度，不声称必要性，也不能从第一种日志收敛直接推出第二种相对乘积收敛。对有限相对产品 `R_(N,E(T))(Nw)`，在第二个指数上界中再加入 `beta_(a,b)(N)` 即可，因为基准子日志由同一个全基准绝对和控制。

这些集合仍是数学长度截断，不是冻结 `SG2OwnerCanonical-v1` 字长／字典序前缀；没有执行 `m_k=2^k` 或任何 panel。沿 `N=k!` 使用这些定理当然合法，但不能把这里选择的移动 `s=Nw` 或充分长度阈值写回冻结输入。

## 7. 本轮完成与未完成

| 问题 | 本轮结论 | 保留边界 |
| --- | --- | --- |
| 全体 content 与物理长度 | 初等证明 `d_g<=M ell_g`，并有全同调向量界 | 不给出数值 `M` 或规范词证书 |
| 完整普通 Euler 产品 | 正实阈值恰为 `s=N`；`N>=2` 的相对产品相同；`R_1` 恒为一 | 依赖指定外部 PGT；不排除条件收敛或解析延拓 |
| 移动参数全产品 | `Q_N(Nw)` 与 `R_N(Nw)` 以 `B_0(w)^N` 为统一相对主项，误差指数衰减 | 仅 `Re(w)>1`；不变成固定 `s` 极限 |
| 有限 deck 字符 | 完成 Euler 日志分解及 Haar 零同调投影 | 不是谱行列式因子分解或迹公式证明 |
| 长度截断与两种精度 | 给出归一化日志与相对产品的不同误差条件 | 不认证实际枚举或原指定双序列合同 |

本轮没有把较弱的充分域当作精确边界，而是在外部计数定理支持下补证了完整产品的精确阈值；也没有把移动参数或辅助 `N^{-4}` 极限作为恢复原冻结目标的替代品。H1、数学长度截断共尾性与 `S_0(a)` 保持上轮已证明状态。原稿 AN-1–AN-5 的指定域与索引条件仍不能由这些不同对象自动完成，正式 `FAIL / BLOCK`、Route 判定和 Stage 5／6 均不变。

## 8. 来源、复核与文档保全

本轮采用 ARS 的论证流程，分开外部定理、项目推论、参数范围和反例；同系助手分别检错计数阈值、同调长度估计、字符接口，再由主线程整合。这是同系逻辑复核，不作为独立科学证据或正式审查。

新增外部证据只用于第 3 节：主线程通过普通浏览核对作者 arXiv v3 的指定定义与 Theorem 2、21 的解析文本，以及 EMS 的书目条目。没有逐页通读整篇、复证 PGT、声称人类已读或认证出版社最终全文与作者版逐字一致。EMS 页面注明全文需要订阅；本轮未请求其受限全文，也未尝试绕过访问限制。没有重试此前的 Utah 403 路径，没有上传私人材料。

首次新增笔记的编排调用因 JavaScript 模板与 Markdown 反引号冲突，在执行前返回 SyntaxError，未写入文件；改为显式占位符替换后重新提交，保留该次失败记录。

本轮仅新增此笔记，并在几何笔记、无限接口笔记和总内部记录追加入口。文档保全检查针对三个旧文件的原文前缀、十一个指定保护文件的原始长度与 SHA-256，以及链接、数学环境配对、控制字符和范围标记；它不认证科学正确性。工作目录此前已确认不属于 Git 仓库，保全比较使用本轮编辑前快照，不声称工作树干净。未运行科学实验、owner 枚举、矩阵或长度程序、旧审查脚本、论文构建，也未修改论文、代码、结果、锁或正式回执。

[geometry-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_geometric_tower_and_length_cutoff_20260908.md
[owner-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_explicit_nonpower_owner_family_20260908.md
[interface-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_scalar_infinite_product_interfaces_20260908.md
[pgt-source]: https://arxiv.org/pdf/2209.10415v3#page=13
[pgt-metadata]: https://ems.press/journals/jems/articles/14298823

## 追加进展：零同调临界边界与对数偏移（2026-09-08）

后续[零同调临界边界、正分支发散与对数偏移渐近](internal_homology_zero_critical_boundary_20260908.md)引入并核对固定零同调类的外部计数展开，证明 `B_0(1)` 与一阶边界导数有限、二阶导数具有对数奇性，排除 `B_0` 在 `w=1` 处的局部全纯／亚纯延拓。它补齐本笔记当时未确定的单独正分支阈值：正分支与完整产品在 `s=N` 都发散，零分支在该点有限；相对产品保留 `N=1` 恒为一的例外。新笔记还证明正分支的层数极限与临界极限不交换；对 `K>2M`、`s_N=N+K log N`，原 `Q_N`、`R_N` 具有 `B_0(1)^N N^(K D_*)` 主项及明确趋零相对误差，并给出纯零分支临界相对截断的 `T_N/sqrt(N)->infinity` 必要充分条件。此处 `D_*=mathscr B_0'(1)` 是本笔记零同调日志的边界导数。不把 `K>2M` 声称为最优阈值，也不把纯零临界截断尺度用于该点已无穷的完整产品；未改原归一化、冻结输入、论文或正式状态。

## 追加进展：移动半平面可逼近临界线（2026-09-08）

后续[收缩临界层、最大重数分支与分数阶奇性](internal_shrinking_critical_layer_and_fractional_singularity_20260908.md)使用新增的全同调类一致局部极限输入，将本笔记固定 `Re(w)>=a>1` 的零同调相对主项加强到 `Re(w)>=1+uN^(-3/2)`（固定 `u>0`）；对有界正实偏移还得到 `B_0(1)^N exp(D_* delta)` 主项，并把对数偏移系数推广到所有固定 `K>0`。这不包含精确临界点，不把未知的统一余项速度当作数值证书。该笔记另证明每个固定未缩时覆盖乘积在 `w=1` 有简单亚纯极点，而规定 `N^(-3)` 日志归一化后的 `Q_N` 在 `N>=2` 具有非整数临界阶，因此不能局部亚纯延拓；保留所有 `N=1` 例外。未构造谱行列式、未换冻结归一化或改变正式状态。

## 追加进展：非平凡的指数边界层（2026-09-08）

后续[全局同调 Gaussian 界与指数临界过渡](internal_exponential_critical_crossover_20260908.md)在固定基底上补出远尾控制和非零 `NZ^4` 格点的统一计数，将零同调移动半平面主项的充分条件推进为充要判准 `log_+(1/epsilon_N)=o(N^3)`，其中 `0<epsilon_N=w_N-1<=1`。特别地，对每个固定 `lambda>=0`，原参数 `s_N=N+N^(-1)exp(-lambda N^3)` 满足 `Q_N(s_N)/B_0(1)^N->exp(lambda)`，`R_N` 同。该非一常数结论限于实轴，并以新的随层一致推导为依据，不从固定层 PGT 常数直接代入对角线；仍不恢复固定 `s` 域、不赋予精确临界点有限值，也不改变原归一化、冻结输入或正式状态。
