# P32 内部研究：复临界过渡、零分支相位与切向限制

记录日期：2026-09-08 UTC。接续[指数临界过渡][real-note]与[零同调临界边界][zero-note]。本轮把实轴过渡扩展到一类明确的复参数域，区分径向主项与法向误差控制；同时补出零同调函数的复对数展开，确定原参数固定虚偏移时的相位极限。

证明链为：已有格点计数 → 复 Laplace 加性误差 → 径向过渡；已有零同调计数 → 复边界展开 → 完整乘积相位。另用一个明确标记的抽象余项例子说明为什么现有误差大小界不能直接覆盖任意切向路径。

全部结论保持同一固定几何、全部本原有向 owner、原 `1/N` 时间缩放和 `1/N^3` 日志归一化。这里没有给精确临界点赋有限值、改变冻结方案、运行实验或进入正式审查／Stage 5／6。

## 1. 固定输入与两个不同的距离

沿用同一带标记、曲率负一的闭双曲亏格二曲面及

\[
\mathscr L_N(Nw)=NH(w)+E_N^+(w),\qquad
B_0(w)=e^{H(w)},\qquad
Q_N(s)=e^{\mathscr L_N(s)},\qquad R_N(s)=Q_N(s)/B(s).
\]

记

\[
H_*=H(1)>0,\qquad D_*=H'(1)<0,\qquad B_*=e^{H_*}>1.
\]

对非零 `NZ^4` 同调的最大重数 owner 集 `mathcal A_N`，令
`a_N(t)=#{g in mathcal A_N:ell_g<=t}`。上轮已证明

\[
E_N^+(w)=N\sum_{g\in\mathcal A_N}e^{-w\ell_g}
+\mathcal E_N(w),\qquad
\sup_{\operatorname{Re}w\ge1}|\mathcal E_N(w)|
\le Ce^{-c_*N},
\tag{1}
\]

\[
a_N(t)\le C\frac{e^t}{N^4t}e^{-c_\theta N^2/t}
\quad(t>0,\ N\ {\rm sufficiently\ large}),
\tag{2}
\]

以及

\[
a_N(t)=\frac{e^t}{N^4t}(1+r_N(t))
\quad(t\ge N^3),\qquad
\eta_N:=\sup_{t\ge N^3}|r_N(t)|\longrightarrow0.
\tag{3}
\]

式 (2) 在小时间成立是因为 `a_N(t)=0` 于 `t<N/M`，不是额外短轨道渐近。式 (3) 的误差速度没有数值认证。本轮复用这些未变输入，不重复外部同调定理的证明，也不把 (3) 当作可逐点微分的公式。

写

\[
w=1+z,\qquad z=x+iy,\qquad x>0,\qquad |z|\le1.
\]

`x` 是到临界竖线的法向距离，`|z|` 是到临界点的径向距离。定义

\[
\Lambda_N^\perp(z)
=\frac1{N^3}\log_+\frac1{N^2x},\qquad
\Lambda_N^{\rm rad}(z)
=\frac1{N^3}\log_+\frac1{N^2|z|},
\qquad 0\le\Lambda_N^{\rm rad}\le\Lambda_N^\perp.
\tag{4}
\]

正实轴上两者相同；复域中可能相差很大。本轮将证明

\[
\boxed{
\left|E_N^+(1+z)-\Lambda_N^{\rm rad}(z)\right|
\le2\eta_N\Lambda_N^\perp(z)
+C\frac{1+\log N}{N^3}+Ce^{-c_*N}.}
\tag{C}
\]

(C) 是复数与实数径向主项之差的模，不只是模长差。

## 2. 复指数积分的分支与一致估计

本轮普通浏览核对了 NIST DLMF 的[定义及表示 6.2.1–6.2.4][dlmf-definition]和[幂级数 6.6.2][dlmf-series]。使用其中的主值分支；在右半平面 `-pi/2<arg z<pi/2`，没有绕零点换支。

在 `Re(zeta)>0` 上可写

\[
\mathrm E_1(\zeta)
=\int_1^\infty e^{-\zeta u}\frac{du}{u}
=e^{-\zeta}\int_0^\infty\frac{e^{-v}}{\zeta+v}\,dv.
\tag{5}
\]

第二式也可在此域中用 `1/u=int_0^infinity e^(-uv)dv` 及绝对可积的 Fubini 自行得到。由于 `|zeta+v|>=|zeta|`，

\[
\boxed{
|\zeta\mathrm E_1(\zeta)|
\le e^{-\operatorname{Re}\zeta}\le1.}
\tag{6}
\]

DLMF 的幂级数给

\[
\mathrm E_1(\zeta)
=-\gamma-\Log\zeta
-\sum_{k=1}^{\infty}\frac{(-1)^k\zeta^k}{k\,k!}.
\tag{7}
\]

因此在 `0<|zeta|<=1` 时，`E_1(zeta)+Log zeta` 一致有界；再用 `|arg zeta|<pi/2`，得到与实径向对数的有界差。`|zeta|>=1` 时使用 (6)。两段合并为

\[
\boxed{
\left|\mathrm E_1(\zeta)-\log_+\frac1{|\zeta|}\right|\le C
\quad(\operatorname{Re}\zeta>0).}
\tag{8}
\]

这里没有把 `Log zeta` 的虚部删去后宣称恒等；其虚部有界，经 `N^(-3)` 归一化才进入下文小余项。特别地，(6) 给

\[
\frac{|z\mathrm E_1(N^3z)|}{N^3}\le N^{-6}.
\tag{9}
\]

## 3. 正分支的复 Laplace 分拆

### 3.1 先证绝对可积，再交换复积分

由 (2) 及 `x>0`，相应正实 majorant 有限，所以可以对复被积式使用 Fubini：

\[
N\sum_{g\in\mathcal A_N}e^{-(1+z)\ell_g}
=N(1+z)\int_0^\infty e^{-(1+z)t}a_N(t)\,dt.
\tag{10}
\]

这不是对复被积式直接应用非负 Tonelli。按普通积分变量在 `t=N^3` 分割，没有重新截断 Stieltjes owner 和，因而不额外丢失端点原子。

低段由 `|1+z|<=2` 和 (2) 控制：

\[
\left|N(1+z)\int_0^{N^3}e^{-(1+z)t}a_N(t)\,dt\right|
\le\frac C{N^3}\mathrm E_1(c_\theta/N)
=O\!\left(\frac{1+\log N}{N^3}\right).
\tag{11}
\]

高段代入 (3) 后，主项为

\[
\frac{1+z}{N^3}\int_{N^3}^{\infty}e^{-zt}\frac{dt}{t}
=\frac{1+z}{N^3}\mathrm E_1(N^3z).
\]

误差只能按法向衰减作绝对估计：

\[
\left|
\frac{1+z}{N^3}\int_{N^3}^{\infty}
e^{-zt}r_N(t)\frac{dt}{t}
\right|
\le\frac{2\eta_N}{N^3}\mathrm E_1(N^3x).
\tag{12}
\]

不能把右侧换成 `2eta_N|E_1(N^3z)|/N^3`：实轴上的正权平均论证在这里不再成立。复相位会改变主积分的消去，却未必同样改变未知余项。

合并 (1)、(11)–(12)，

\[
\boxed{
E_N^+(1+z)=\frac{1+z}{N^3}\mathrm E_1(N^3z)
+\mathcal R_N(z),\quad
|\mathcal R_N(z)|
\le\frac{2\eta_N}{N^3}\mathrm E_1(N^3x)
+C\frac{1+\log N}{N^3}+Ce^{-c_*N}.}
\tag{13}
\]

### 3.2 主项径向化，误差仍保留法向量

由 (8)–(9) 和

\[
\left|
\log_+\frac1{N^3|z|}
-\log_+\frac1{N^2|z|}
\right|\le\log N,
\]

有

\[
\left|
\frac{1+z}{N^3}\mathrm E_1(N^3z)
-\Lambda_N^{\rm rad}(z)
\right|\le C\frac{1+\log N}{N^3}.
\tag{14}
\]

正实 `E_1(N^3x)<=log_+(1/(N^2x))+C`。由于 `eta_N` 最终有界，代入 (13) 即得 (C)。

本轮新增的一致范围是：对充分大 `N`，(C) 同时适用于所有 `x>0, |z|<=1`。但其右侧是否趋零，还取决于实际路径的 `eta_N Lambda_N^perp`，不能忽略这个乘积。

## 4. 已闭合的复域与非平凡过渡

### 4.1 有界法向指数域中的一致径向轮廓

对每个固定 `A>=0`，令

\[
\mathcal D_N(A)=
\{z:\operatorname{Re}z>0,\ |z|\le1,\
\Lambda_N^\perp(z)\le A\}.
\]

设

\[
d_N(A)=2A\eta_N+C(1+\log N)/N^3+Ce^{-c_*N}\longrightarrow0.
\]

由 (C)，

\[
\sup_{z\in\mathcal D_N(A)}
|E_N^+(1+z)-\Lambda_N^{\rm rad}(z)|
\le d_N(A),
\tag{15}
\]

故

\[
\boxed{
\sup_{z\in\mathcal D_N(A)}
\left|
\frac{Q_N(N(1+z))}
{B_0(1+z)^N\exp(\Lambda_N^{\rm rad}(z))}-1
\right|
\le e^{d_N(A)}-1\longrightarrow0.}
\tag{16}
\]

`R_N` 同样成立，因为已有 `mathscr B(Nw)=O(e^(-c_0N))` 一致于 `Re(w)>=1`。这是一致的相对轮廓，不是声称整个移动半平面收敛到同一个非一常数。式 (15) 还说明正分支日志的虚部在此域上一致趋零。

更一般，沿任意 `z_N`，如果

\[
\eta_N\Lambda_N^\perp(z_N)\longrightarrow0,
\qquad
\Lambda_N^{\rm rad}(z_N)\longrightarrow\lambda<\infty,
\tag{17}
\]

则

\[
\frac{Q_N(N(1+z_N))}{B_0(1+z_N)^N}
\longrightarrow e^\lambda,\qquad
\frac{R_N(N(1+z_N))}{B_0(1+z_N)^N}
\longrightarrow e^\lambda.
\tag{18}
\]

有界法向量是容易核对的充分条件，不是 (17) 的必要条件。

### 4.2 非切向路径与极端切向路径不能混同

固定 `c in (0,1]`，若 `x>=c|z|`，则

\[
0\le\Lambda_N^\perp(z)-\Lambda_N^{\rm rad}(z)
\le N^{-3}\log(1/c).
\tag{19}
\]

因此非切向路径上，若径向量趋于有限 `lambda`，就自动满足 (17)，从而得到 (18)；若径向量仅有界而不收敛，则只能得到 (16) 的一致相对轮廓及相应子序列结论，不能断言单一极限。若同一固定非切向条件下 `Lambda_N^rad->infinity`，则由 (C) 可得
`Re(E_N^+)/Lambda_N^rad->1`，从而两个相对比值的模长趋于无穷；没有因此取得乘积相对等价或稳定复相位。

在极端切向情形，不能仅凭 `Lambda_N^perp≫Lambda_N^rad` 就断言结论失败；只要 (17) 的误差乘积仍趋零，结论仍成立。尚未闭合的是该乘积不受控制的路径。第 7 节说明为什么只靠现有大小估计不能自动补上它。

### 4.3 双指数逼近的最小指数规则

固定 `a,b>=0` 和 `sigma in {+1,-1}`，取

\[
z_N=N^{-2}\left(e^{-aN^3}+i\sigma e^{-bN^3}\right).
\]

此时

\[
\Lambda_N^\perp(z_N)=a,\qquad
\Lambda_N^{\rm rad}(z_N)\longrightarrow\min\{a,b\}.
\tag{20}
\]

因为 `N^2|z_N|` 位于
`exp(-min(a,b)N^3)` 与其 `sqrt(2)` 倍之间，取 `log_+` 后的误差至多常数除以 `N^3`。所以 (18) 的极限为 `exp(min(a,b))`。这包括 `a=b` 和某个指数为零的端点，不把零指数误写成精确临界点。

要把分母换成 `B_*^N`，还需下面的零分支分析；这里没有省略它。

## 5. 零同调函数的复对数展开

### 5.1 一阶闭半平面连续性

已有零同调计数给 `sum_(alpha_g=0) ell_g e^(-ell_g)<infinity`。结合 `ell_g>=ell_*>0`，

\[
H'(w)
=-\sum_{\alpha_g=0}\ell_g
\sum_{r\ge1}e^{-rw\ell_g}
\]

在整个 `Re(w)>=1` 绝对一致收敛。故 `H` 和 `H'` 都连续到该闭半平面。沿线段积分给

\[
H(1+z)-H_*-D_*z
=z\int_0^1[H'(1+uz)-D_*]\,du=o(|z|),
\tag{21}
\]

一致于 `Re(z)>=0, z->0`。这不是跨越边界的全纯延拓。

### 5.2 保留二次项中的精确复对数

沿用已核对的零类计数输入

\[
q(t):=e^{-t}n_0(t)
=\frac{c_{\rm hom}}{t^3}+O(t^{-4})
\quad(t\to\infty),\qquad c_{\rm hom}>0.
\tag{HC}
\]

令 `F(w)=sum_(alpha_g=0)e^(-w ell_g)`。取 `A_0` 足够大，在它之后使用 (HC)；之前的有限时间贡献单独保留。先从零计数起始区间作 Stieltjes 分部积分，再对所得普通积分分割，可写

\[
F''(1+z)
=\int_0^\infty
[(1+z)t^2-2t]e^{-zt}q(t)\,dt
\quad(\operatorname{Re}z>0).
\tag{22}
\]

小长度处 `q=0`，不存在零点积分问题。普通积分在 `A_0` 分割，不遗漏恰在该长度的 owner；若直接从大 `A_0` 重作 Stieltjes 分部积分，则必须另保留端点项，本轮不采用那个省略式。

代入 (HC) 后，除

\[
c_{\rm hom}(1+z)
\int_{A_0}^\infty e^{-zt}\frac{dt}{t}
=c_{\rm hom}(1+z)\mathrm E_1(A_0z)
\]

之外的项都由固定可积权重 `C t^(-2)` 等控制。重复次数 `r>=2` 的零分支在 `Re(w)>1/2` 全纯，二阶导数在一附近有界。因此，由 (7) 得

\[
H''(1+z)=-c_{\rm hom}\Log z+O(1)
\quad(0<|z|\le r_0,\ \operatorname{Re}z>0),
\tag{23}
\]

其中 `r_0>0` 固定足够小，误差对角度一致。额外的 `zLog z` 有界，不产生新的发散项。

利用一阶连续性沿径向两次积分，

\[
H(1+z)-H_*-D_*z
=z^2\int_0^1(1-u)H''(1+uz)\,du.
\]

这里 `Log(uz)=Log z+log u`，且
`int_0^1(1-u)log u du=-3/4`。于是

\[
\boxed{
H(1+z)=H_*+D_*z
-\frac{c_{\rm hom}}2z^2\Log z+O(|z|^2).}
\tag{24}
\]

式 (24) 对 `0<|z|<=r_0, Re(z)>=0` 一致：先在内部证明，再用 `H` 的连续边界值到达非零纯虚点。没有声称 `H''` 在零点连续，也没有得到过零点的全纯／亚纯延拓。较粗但便利的推论是

\[
H(1+z)=H_*+D_*z+
O\!\left(|z|^2\log\frac e{|z|}\right).
\tag{25}
\]

### 5.3 原参数有界复偏移时的相位

若 `Re(z_N)>=0`、`Nz_N->xi in C`，则

\[
\boxed{
\frac{B_0(1+z_N)^N}{B_*^N}\longrightarrow e^{D_*\xi}.}
\tag{26}
\]

在 `|Nz|<=K` 上，(25) 给其日志误差一致为 `O_K(log N/N)`。因为 `D_*` 是实负数，极限的模为 `exp(D_*Re xi)`，相位为 `D_*Im xi`（模 `2pi`）。

## 6. 完整乘积的幅度与相位

固定 `A>=0,K>0`。在 `z in mathcal D_N(A)` 且 `N|z|<=K` 的域上，结合 (15)、(25) 得

\[
\boxed{
\frac{Q_N(N(1+z))}
{B_*^N\exp(D_*Nz+\Lambda_N^{\rm rad}(z))}
=1+o_{A,K}(1),}
\tag{27}
\]

一致成立，`R_N` 同。日志误差受
`2A eta_N+O_K(log N/N)+O(e^(-cN))` 控制。

由 (20) 及 `Nz_N->0`，双指数例子于是得到原参数结论

\[
\boxed{
\frac{
Q_N\!\left(N+\frac{e^{-aN^3}+i\sigma e^{-bN^3}}N\right)}
{B_*^N}
\longrightarrow e^{\min(a,b)},\qquad
R_N\ {\rm same}.}
\tag{28}
\]

另一个不同的尺度是固定非零虚偏移。固定 `a>=0`、`theta in R\setminus{0}`，取

\[
s_N=N+N^{-1}e^{-aN^3}+i\theta,\qquad
z_N=N^{-2}e^{-aN^3}+i\theta/N.
\]

这里 `Lambda_N^perp=a`，但 `Lambda_N^rad=0` 于充分大 `N`，且 `Nz_N->i theta`。故

\[
\boxed{
\frac{Q_N(N+N^{-1}e^{-aN^3}+i\theta)}{B_*^N}
\longrightarrow e^{iD_*\theta},\qquad
\frac{R_N(N+N^{-1}e^{-aN^3}+i\theta)}{B_*^N}
\longrightarrow e^{iD_*\theta}.}
\tag{29}
\]

同一实部而取 `theta=0` 时，上一轮极限为 `e^a`。若 `a>0`，固定 `theta≠0` 后取层数极限，再令 `theta->0`，得到一；直接取 `theta=0` 则得到 `e^a`。这明确展示了原参数虚偏移与层数极限不交换。有限 `N` 的函数仍全纯于 `Re(s)>N`，不因这个非一致极限而矛盾。

更一般，将 (17) 与 `Nz_N->xi` 结合，可得极限
`exp(lambda+D_*xi)`。两参数不是任意独立：若 `lambda>0`，必有 `Nz_N->0`；若 `xi≠0`，径向临界量必趋零。

上轮整个移动半平面“相对趋一”的充要判准不被推翻：当法向指数 `a>0` 时，半平面仍包含实轴上比值趋 `e^a` 的点。若只选一条具有非零虚偏移的路径，比值可能趋一；单条路径与全域上确界是不同命题。

## 7. 为什么大小误差不足以覆盖任意切向路径

### 7.1 一个只针对估计方法的抽象诊断

以下不是实际测地流、同调格点计数或本项目对象的反例，也没有构造新的 owner 集；它只检验从 (3) 的大小信息能否推得任意切向的振荡消去。

设

\[
T_N=N^3,\quad \widetilde\eta_N=N^{-1},\quad
y_N=N^{-2},\quad x_N=N^{-2}e^{-N^4}.
\]

取固定光滑非增 `chi:[0,infinity)->[0,1]`，在 `[0,1]` 上为一、在 `[2,infinity)` 上为零，令

\[
\widetilde r_N(t)
=\widetilde\eta_N\chi(x_Nt)\cos(y_Nt)
\quad(t\ge T_N).
\]

有 `sup_t|rtilde_N(t)|<=1/N->0`，每个固定 `N` 的余项甚至最终为零。但在 `z_N=x_N+iy_N`，

\[
\begin{aligned}
\frac1{N^3}\int_{T_N}^\infty
e^{-z_Nt}\widetilde r_N(t)\frac{dt}{t}
&=\frac1{2N^4}(I_{0,N}+I_{2,N}),\\
I_{0,N}&=\int_{T_N}^\infty
e^{-x_Nt}\chi(x_Nt)\frac{dt}{t},\\
I_{2,N}&=\int_{T_N}^\infty
e^{-(x_N+2iy_N)t}\chi(x_Nt)\frac{dt}{t}.
\end{aligned}
\]

变元 `v=x_Nt` 给

\[
I_{0,N}=\log\frac1{x_NT_N}+O(1)
=N^4-\log N+O(1).
\]

函数 `e^(-x_Nt)chi(x_Nt)/t` 非增且最终为零。分部积分或 Dirichlet 估计给

\[
|I_{2,N}|\le\frac C{y_NT_N}=O(N^{-1}).
\]

因此

\[
\boxed{
\frac1{N^3}\int_{T_N}^\infty
e^{-z_Nt}\widetilde r_N(t)\frac{dt}{t}
\longrightarrow\frac12,}
\tag{30}
\]

而 `N^2|z_N|>1`，所以 `Lambda_N^rad(z_N)=0`。这证明“误差上确界趋零且每层最终消失”本身不足以推出任意切向路径的误差趋零。

该诊断不证明真实 `r_N(t)` 存在此共振，也不声称它满足全部逐类 Gaussian、同调兼容性或几何约束。它的作用是防止以未经证明的消去替代 (12)。

### 7.2 一个足够但尚未建立的补充义务

例如，若对实际计数余项另能证明

\[
\boxed{
\frac1{N^3}\int_{N^3}^\infty
|r_N(t)|\,\frac{dt}{t}\longrightarrow0,}
\tag{31}
\]

则 (12) 可在全部 `x>0, |z|<=1` 上用此积分控制，去掉法向指数限制。足够强的统一振荡积分估计也可能替代 (31)。

本轮没有证明 (31)，也没有提供其数值证书。仅改善 `eta_N` 的随 `N` 速率，仍不能自动覆盖任意更小的 `x_N`；固定覆盖层的局部解析邻域或 PGT 余项存在性也不等于这种统一控制。需要新证据的是余项随长度的衰减／积分性质或统一消去，不是改选原归一化。

## 8. 来源、范围和实际检查

本轮按照 ARS 论证流程保留四个关键区别：复 Fubini 与非负 Tonelli、复积分的加性误差与实轴正权平均、路径极限与半平面一致极限、抽象估计诊断与真实流的反例。新材料是内部论证笔记，不是完整论文写作、重新审查或 Route 评估。

Sharp 相对计数、Coles–Sharp 加权指数率以及固定零类计数输入沿用前两份笔记中已经核对的来源与限制；本轮没有重新请求其 PDF。新增外部核对仅为 DLMF 的指定定义、主值分支、积分表示及幂级数。上面的复过渡、零分支展开和抽象诊断是本轮推导，不是 DLMF 的原结论。

主线程为唯一文件写入者；同系助手分别只读检错复 Laplace 与量词、零分支展开、切向余项诊断。这不构成独立科学证据、跨模型认证或发表新颖性判断。

本轮草稿检错发现一处量词省略：非切向条件加径向量“有界”只能给相对轮廓，不能保证单一极限；正文已明确补上径向量趋于有限 `lambda` 的条件，并保留仅有界时的子序列说明。这个修正没有改变 (C) 或既有文件的原结论。

本轮仅新增此笔记，并在指数临界笔记、零同调临界笔记和总内部记录追加入口。保全检查使用编辑前只读 Node 字节／SHA-256 快照，核对三个追加文件的全部旧前缀及十五个指定保护文件；新增文本另查本地链接、公式环境、控制字符、占位符、反引号配对和末尾换行。机械检查的实际结果在交接答复报告，不把它当作数学证明。

本轮未请求既有失败／受限的 WRAP、Manchester、AMS、Utah 路径，没有上传私人材料或调用程序化文献／外部模型服务。未运行科学实验、owner 枚举、矩阵或长度程序、既有 artifact writer、论文构建或正式审查脚本；未改论文、代码、结果、锁、正式回执和历史失败记录。原 `FAIL / BLOCK`、Route 状态和 Stage 5／6 停止条件不变。

[real-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_exponential_critical_crossover_20260908.md
[zero-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_homology_zero_critical_boundary_20260908.md
[dlmf-definition]: https://dlmf.nist.gov/6.2
[dlmf-series]: https://dlmf.nist.gov/6.6#E2

## 后续追加：实际可积尾项闭合，法向限制解除（2026-09-08）

后续[字符计数可积尾项与全右半圆径向轮廓](internal_integrable_character_tail_and_global_radial_profile_20260908.md)核对 Sharp Lemma 3 的全字符统一逆幂余项，并完成 sharp 端点、去迭代、去权、有限字符平均及零类扣除。对本笔记实际 `r_N(t)` 证明 `|r_N(t)|<=C(1/t+exp(-ct/N²)+N⁴/t²)` 于 `t>=N²`；本笔记 (31) 的 `N^{-3}int_{N³}^infinity |r_N(t)|dt/t=O(N^{-5})` 因而闭合。另在 `N²` 处分割积分，将 (C) 推进为全部 `Re z>0, |z|<=1` 上 `E_N^+(1+z)=Lambda_N^rad(z)+O(N^{-3})`，乘积相对轮廓也有统一 `O(N^{-3})` 误差，不再限制法向指数，且径向量趋于无穷时仍成立。原抽象诊断保留：它说明旧大小界不足，不是实际计数反例。零分支相位结论因此扩展到任意更快的正实部逼近；不包括精确临界点，不改变原归一化、冻结输入、论文或正式状态。
