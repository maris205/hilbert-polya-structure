# P32 内部研究：收缩临界层、最大重数分支与分数阶奇性

记录日期：2026-09-08 UTC。接续[零同调临界边界][critical-note]和[未缩时覆盖乘积][moving-note]。本轮把原乘积的零同调主项从对数级正偏移推进到 `s-N=u/sqrt(N)`，其中 `u>0` 固定；另对每个固定层确定临界发散阶，并据此排除 `N>=2` 的完整归一化乘积在临界点的局部亚纯延拓。

前一结论使用对全部整数同调类一致的外部局部极限定理；后一结论使用每个固定覆盖曲面的素测地线计数余项。两种一致性不能混用。原 `1/N` 时间缩放和 `1/N^3` 对数归一化均不变，未启动实验、规范枚举、论文修订或正式审查。

## 1. 沿用对象及本轮问题

固定同一个真实、带标记、曲率负一的闭双曲亏格二曲面，全部本原有向 owner 集 `O=O_0 union O_+`。有

\[
\ell_g\ge\ell_*>0,\qquad
\|\alpha_g\|_\infty\le M\ell_g,\qquad
d_g\le M\ell_g\quad(g\in\mathcal O_+),
\]

其中 `alpha_g in Z^4`、`d_g` 为非零同调坐标的正 gcd，`M>0` 是上轮固定的理论常数。逆向 owner 不合并，起点改变不重复计数。沿用

\[
m_{N,g}=\gcd(N,d_g)\quad(g\in\mathcal O_+),\qquad
m_{N,g}=N\quad(g\in\mathcal O_0),\qquad
h_{N,g}=N/m_{N,g}.
\]

令

\[
L_t(w)=\sum_{r\ge1}\frac{e^{-rwt}}r,\qquad
H(w)=\mathscr B_0(w),\qquad B_0(w)=e^{H(w)}.
\]

在 `Re(w)>1` 上已证明

\[
\mathscr L_N(Nw)=NH(w)+E_N^+(w),\qquad
E_N^+(w)=\sum_{g\in\mathcal O_+}
m_{N,g}L_{h_{N,g}\ell_g}(w),
\]

\[
Q_N(s)=e^{\mathscr L_N(s)},\qquad
R_N(s)=Q_N(s)/B(s),\qquad
\mathscr U_{\Sigma_N}(w)=N^3\mathscr L_N(Nw).
\]

最后一式来自所有覆盖本原轨道的完整提升块分拆；`mathscr U_(Sigma_N)` 是未缩时覆盖 Euler 对数，`Sigma_N` 是固定层的连通闭双曲覆盖曲面。

上轮还证明

\[
H_*:=H(1)>0,\qquad D_*:=H'(1)<0,\qquad B_*:=e^{H_*}>1,
\]

\[
H(1+\varepsilon)
=H_*+D_*\varepsilon+
\frac{c_{\rm hom}}2\varepsilon^2\log(1/\varepsilon)
+O(\varepsilon^2)
\quad(\varepsilon\downarrow0).
\]

本轮的未知量是 `w` 随 `N` 逼近一时正分支的大小。固定同调类的 Liu 渐近不允许直接替代移动同调类的统一控制。

## 2. 临界困难集中到最大重数的单重复项

### 2.1 真因子重数在闭临界半平面指数小

设 `g in O_+` 且 `m_(N,g)<N`。由于 `m_(N,g)|N`，有

\[
m_{N,g}\le N/2,\qquad h_{N,g}\ge2,\qquad
\ell_g\ge m_{N,g}/M.
\]

因此

\[
(h_{N,g}-3/2)\ell_g
\ge\frac{N-\tfrac32m_{N,g}}M
\ge\frac{N}{4M}.
\]

记 `c_1=1-e^(-ell_*)>0`。对全部 `Re(w)>=1`，

\[
\begin{aligned}
\sum_{\substack{g\in\mathcal O_+\\m_{N,g}<N}}
m_{N,g}|L_{h_{N,g}\ell_g}(w)|
&\le\frac{e^{-N/(4M)}}{c_1}
\sum_{\substack{g\in\mathcal O_+\\m_{N,g}<N}}
m_{N,g}e^{-3\ell_g/2}\\
&\le\boxed{
\frac{M S_1(3/2)}{c_1}e^{-N/(4M)}},
\end{aligned}
\]

其中 `S_1(3/2)=sum_g ell_g e^(-3ell_g/2)<infinity` 已由上轮证明。这是全部真因子 owner 的一次求和，不另乘除数个数。

### 2.2 最大重数等价于非零整数同调落在 N 格点中

对正 owner，

\[
m_{N,g}=N
\iff N\mid d_g
\iff\alpha_g\in N\mathbb Z^4\setminus\{0\}.
\]

定义该集合及其累计计数

\[
\mathcal A_N=\{g\in\mathcal O_+:
\alpha_g\in N\mathbb Z^4\setminus\{0\}\},\qquad
a_N(T)=\#\{g\in\mathcal A_N:\ell_g\le T\}.
\]

此处 `mathcal A_N` 是 owner 集合，不是前轮覆盖度数归一化函数 `A_N(w)`。所有 `g in mathcal A_N` 满足 `ell_g>=N/M`，故 `a_N(T)=0` 于 `T<N/M`。

还可以排除重复次数 `r>=2` 的边界困难。由已有固定基底素测地线定理，存在 `C_pg,T_0>0`，使 `n(t)<=C_pg e^t/t` 于 `t>=T_0`。令 `A=N/M>=T_0`。允许保留 `ell_g=A` 的端点原子，非负积分给出

\[
\sum_{\ell_g\ge A}e^{-2\ell_g}
\le2\int_A^\infty e^{-2t}n(t)\,dt
\le2C_{\rm pg}\frac{e^{-A}}A.
\]

因 `r>=2` 的单 owner 日志受 `e^(-2ell_g)/c_1` 控制，

\[
N\sum_{g\in\mathcal A_N}\sum_{r\ge2}
\frac{e^{-r\ell_g}}r=O(e^{-N/M}).
\]

所以，在 `Re(w)>1`，

\[
\boxed{
E_N^+(w)
=N\sum_{g\in\mathcal A_N}e^{-w\ell_g}
+\mathcal E_N(w),\qquad
\sup_{\operatorname{Re}w\ge1}|\mathcal E_N(w)|
\le C_{\rm rem}e^{-N/(4M)}.}
\]

余项的级数在闭临界半平面绝对一致收敛；对每个固定 `N`，它还在 `Re(w)>1/2` 全纯，因为真因子部分有 `h>=2`、另一部分有 `r>=2`，均由 `S_0(2a)<infinity` 控制。上式不把主和赋值到 `w=1`：它在那里发散。

### 2.3 仅用总计数时已经能够改进旧界

这一小节不使用第 3 节的新同调输入。设 `x=s-N>0`、`a=1+x/N`。利用 `a_N(t)<=n(t)` 和其起始长度限制，

\[
\sum_{g\in\mathcal A_N}e^{-a\ell_g}
=a\int_{N/M}^\infty e^{-at}a_N(t)\,dt
\le C_{\rm pg}a\,\mathrm E_1(x/M),
\]

其中

\[
\mathrm E_1(y)=\int_y^\infty e^{-v}\frac{dv}{v}
\le e^{-y}/y\quad(y>0).
\]

故对 `Re(w)>=1+x/N`，

\[
\sum_{g\in\mathcal O_+}
m_{N,g}|L_{h_{N,g}\ell_g}(w)|
\le C_{\rm proper}e^{-N/(4M)}
+\frac{C_{\rm pg}Na}{c_1}\mathrm E_1(x/M).
\]

当 `x_N->infinity`、`x_N=o(N)` 时，右侧为

\[
O\!\left(\frac{N}{x_N}e^{-x_N/M}\right)
+O(e^{-N/(4M)}).
\]

所以 `x_N/M+log x_N-log N->infinity` 已是充分条件；尤其 `x_N=M log N` 给出 `O(1/log N)`。这只是总计数提供的中间加强，不把它称为真实阈值。以下新增输入将偏移进一步缩小到趋于零。

## 3. 全同调类一致局部极限与收缩半平面

### 3.1 新增外部输入的精确强度

Richard Sharp，*A local limit theorem for closed geodesics and homology*，Trans. AMS 356(12) (2004), 4897–4908；书目 DOI 标识为 `10.1090/S0002-9947-04-03534-2`。出版身份由[Manchester 公开书目记录][sharp-meta]核对，定理支持来自[作者公开版 Theorem 1，作者版 p.2][sharp-source]，不是受限刊本的未读内容。

该定理对紧致负曲率流形，在二维或指定 pinching 条件下，给出累计 prime 闭测地线计数的 Gaussian 主项加一致绝对误差，明确一致于全部整数同调类。作者版 p.1 定义 prime 和整数同调；p.5 的单位切丛轨道积分使用有符号同调。本项目只提取上界，不识别精确 Gaussian 首常数，也不额外用它认证有向计数的首项倍数。

对固定 P32 基底，取第一 Betti 数四、熵一，正定二次型给出常数 `C_LL,c_LL>0`、`T_LL>0` 和非负尾包络 `rho(T) downarrow 0`，使

\[
\boxed{
n_\alpha(T)\le
C_{\rm LL}\frac{e^T}{T^3}
\left[
e^{-c_{\rm LL}\|\alpha\|_2^2/T}+\rho(T)
\right]
\quad(\alpha\in\mathbb Z^4,\ T\ge T_{\rm LL}).}
\tag{ULL}
\]

例如对定理中的全同调类归一化误差先取绝对值上确界，再取 `t>=T` 的尾上确界，即可选出这样的 `rho`。固定正系数吸收进 `C_LL`；若仅以正反向计数之和取上界，同样至多改变固定常数，因为 Gaussian 对 `alpha` 与 `-alpha` 相同。

(ULL) 保留了 Gaussian 项之外的加法误差。它不是全局 Gaussian 相对上界，不意味着 `n_alpha(T)<=C e^T T^(-3)e^(-c||alpha||^2/T)`。本轮也不从一致 `o(1)` 猜测 `rho(T)` 的幂次或数值速率。

### 3.2 非零 N 格点的累计计数

取 `N` 足够大，使 `N/M>=T_LL`，并设

\[
\rho_N=\rho(N/M)\longrightarrow0.
\]

若某 `alpha in NZ^4` 在长度 `t` 内出现，已有几何界要求 `||alpha||_infinity<=Mt`。对于 `t>=N/M`，可能的非零格点个数至多

\[
(2\lfloor Mt/N\rfloor+1)^4-1
\le81(Mt/N)^4.
\]

每个非零格点又满足 `||alpha||_2>=N`。将 (ULL) 在这些有限同调类上求和，得到

\[
\boxed{
a_N(t)\le C_{\rm lat}\frac{e^t t}{N^4}
\left[e^{-c_{\rm LL}N^2/t}+\rho_N\right]
\quad(t\ge N/M),}
\]

其中可取 `C_lat=81M^4 C_LL`；`t<N/M` 时仍为零。这里既使用了全同调类一致性，又保留了可能随长度增长的类数，未用逐类极限替代求和。

### 3.3 由正实积分控制复域的绝对总和

令 `0<epsilon<=1`、`a=1+epsilon`。对 `Re(w)>=a`，最大重数部分满足

\[
\begin{aligned}
\sum_{g\in\mathcal A_N}|N L_{\ell_g}(w)|
&\le\frac N{c_1}\sum_{g\in\mathcal A_N}e^{-a\ell_g}\\
&=\frac{Na}{c_1}\int_0^\infty e^{-at}a_N(t)\,dt\\
&\le\frac{C_{\rm lat}a}{c_1N^3}
\int_0^\infty t e^{-\varepsilon t}
\left[e^{-c_{\rm LL}N^2/t}+\rho_N\right]dt.
\end{aligned}
\]

第二行是对正实非负 majorant 使用 Tonelli，不是给复项强加大小序。第三行把下限扩至零只增大积分。`a<=2` 将并入后续常数。

AM–GM 给出

\[
\frac{\varepsilon t}{2}+\frac{c_{\rm LL}N^2}{t}
\ge\sqrt{2c_{\rm LL}}N\sqrt\varepsilon.
\]

所以

\[
\int_0^\infty t e^{-\varepsilon t-c_{\rm LL}N^2/t}\,dt
\le\frac4{\varepsilon^2}
e^{-\sqrt{2c_{\rm LL}}N\sqrt\varepsilon},
\qquad
\int_0^\infty t e^{-\varepsilon t}\,dt=\varepsilon^{-2}.
\]

记 `gamma_LL=sqrt(2c_LL)>0`，合并真因子部分得到

\[
\boxed{
\sup_{\operatorname{Re}w\ge1+\varepsilon}
\sum_{g\in\mathcal O_+}
m_{N,g}|L_{h_{N,g}\ell_g}(w)|
\le C_{\rm proper}e^{-N/(4M)}
+\frac{C_{\rm maj}}{N^3\varepsilon^2}
\left[4e^{-\gamma_{\rm LL}N\sqrt\varepsilon}+\rho_N\right].}
\tag{M}
\]

常数依赖固定基底、标记及已选定的计数输入，不依赖当层 `N`、`epsilon in (0,1]` 或虚部。以偏移 `delta=N epsilon` 表示，第二项为

\[
\frac{C_{\rm maj}}{N\delta^2}
\left[4e^{-\gamma_{\rm LL}\sqrt{N\delta}}+\rho_N\right],
\qquad0<\delta\le N.
\]

只使用 (ULL) 的粗 `O(e^T/T^3)` 上界会丢掉 `rho_N->0`，因而无法由同一方法包含下面的固定平方根端点。

### 3.4 固定平方根端点及原乘积的一致相对主项

固定 `u>0`，定义移动半平面

\[
\Omega_{N,u}
=\{w:\operatorname{Re}w\ge1+uN^{-3/2}\}.
\]

代入 `epsilon=uN^(-3/2)`，对充分大 `N`，(M) 的右侧变为

\[
d_N(u):=
C_{\rm proper}e^{-N/(4M)}
+\frac{C_{\rm maj}}{u^2}
\left[4e^{-\gamma_{\rm LL}\sqrt u\,N^{1/4}}+\rho_N\right]
\longrightarrow0.
\]

因此

\[
\boxed{
\sup_{w\in\Omega_{N,u}}|E_N^+(w)|\le d_N(u)\to0,\qquad
\sup_{w\in\Omega_{N,u}}
\left|\frac{Q_N(Nw)}{B_0(w)^N}-1\right|
\le e^{d_N(u)}-1\to0.}
\]

基准日志也可一致控制：对充分大 `N` 及 `w in Omega_(N,u)`，

\[
|\mathscr B(Nw)|
\le\frac{S_0(2)}{c_1}e^{-(N-2)\ell_*}
=O(e^{-c_0N})
\]

可取某个固定 `c_0>0`。故将指数上界再加入该基准误差，就得到

\[
\boxed{
\sup_{w\in\Omega_{N,u}}
\left|\frac{R_N(Nw)}{B_0(w)^N}-1\right|\longrightarrow0.}
\]

这是对整个移动复半平面的相对渐近，使用原来的归零对数和归一化。`u>0` 必须固定；允许 `u` 位于固定正紧区间内，但不能令其任意趋于零而忽略 `rho_N/u^2`。

## 4. 实轴后果：固定偏移、趋零偏移和任意正对数系数

### 4.1 有界偏移区间上的统一渐近

固定 `u,D_max>0`。对充分大 `N`，令

\[
u/\sqrt N\le\delta\le D_{\max}.
\]

上轮零同调边界展开给出

\[
NH(1+\delta/N)
=NH_*+D_*\delta+O_{u,D_{\max}}(\log N/N)
\]

一致成立。第 3 节同时控制正分支，因此对 `Q_N` 和 `R_N` 分别有

\[
\boxed{
\sup_{\delta\in[u/\sqrt N,D_{\max}]}
\left|
\frac{Q_N(N+\delta)}{B_*^N e^{D_*\delta}}-1
\right|
=O_{u,D_{\max}}\!\left(
\rho_N+e^{-\gamma_{\rm LL}\sqrt u\,N^{1/4}}
+\frac{\log N}{N}
\right)\to0.}
\]

`R_N` 替换 `Q_N` 后同式。指数小的真因子和基准误差已吸收；不能把总误差只写成零分支展开的 `O(log N/N)`，因为当前没有认证 `rho_N` 的速度。

所以，对每个固定 `delta>0`，

\[
\frac{Q_N(N+\delta)}{B_*^N},
\ \frac{R_N(N+\delta)}{B_*^N}
\longrightarrow e^{D_*\delta};
\]

而在 `delta=u/sqrt N` 时，

\[
\boxed{
Q_N(N+u/\sqrt N)\sim R_N(N+u/\sqrt N)\sim B_*^N.}
\]

仅有 `rho_N=o(1)` 不足以进一步声称该端点具有 `1+D_*u/sqrt N+o(N^(-1/2))` 的相对展开。

### 4.2 上轮对数偏移可扩展至全部固定 K>0

对任何固定 `K>0`，取 `delta=K log N`。它最终满足 `0<delta<=N`，故 (M) 给出

\[
E_N^+(1+K\log N/N)
=O_K\!\left(
\frac{\rho_N+e^{-\gamma_{\rm LL}\sqrt{KN\log N}}}
{N\log^2N}
+e^{-N/(4M)}
\right).
\]

结合 `H` 的边界展开，得到

\[
\boxed{
Q_N(N+K\log N)
=B_*^N N^{KD_*}
\left[1+O_K\!\left(\frac{(\log N)^3}{N}\right)\right],}
\]

且 `R_N` 同式。这里使用了新的同调一致输入，所以不与上轮仅凭旧界得到的 `K>2M` 充分条件冲突；旧文保留。新结论对每个固定 `K>0` 成立，不包含 `K=0`，也不声称误差常数对 `K downarrow 0` 一致。

## 5. 每个固定层的临界发散阶与局部延拓

本节先固定曲面或层数，再令参数趋近临界点。其常数、误差域及指数谱隙不用于第 3 节的随层一致估计。

### 5.1 固定曲面的计数余项

Wu–Xue，*Prime geodesic theorem and closed geodesics for large genus*，[作者 arXiv v3][pgt-source] p.1 明定本原有向累计计数，Theorem 2（pp.2–3）及 Theorem 21（p.13）适用于任意固定闭双曲曲面 `X`，不是只适用于随机曲面。

固定 `sys(X)>0` 后，定理中的短测地项最终消失；有限个非零小特征值给出 `s_j<1`。将其有限项吸收，得到某个 `theta_X<1`，使

\[
\boxed{
n_X(T)=\operatorname{Li}(e^T)+O_X(e^{\theta_XT}).}
\tag{PG}
\]

例如可取 `theta_X=max({5/6} union {s_j:0<lambda_j<=1/4})`。这加强了仅有 `n_X(T)~e^T/T` 的主项信息，足以保证下面的有限解析余项。每个固定连通覆盖 `X=Sigma_N` 都可使用 (PG)，但 `theta_(Sigma_N)` 及相关常数不声称对 `N` 一致。

### 5.2 从计数余项构造局部简单极点

对固定 `X`，定义未缩时对数及其乘积

\[
\mathscr U_X(w)=\sum_\gamma\sum_{r\ge1}
\frac{e^{-rw\ell_\gamma}}r,\qquad
U_X(w)=e^{\mathscr U_X(w)}
\quad(\operatorname{Re}w>1).
\]

取足够大 `A>log 2`，令 `R_X(t)=n_X(t)-Li(e^t)`。将 `ell_gamma<=A` 的有限项先分离，再对严格尾分部积分，单重复和满足

\[
P_X(w):=\sum_\gamma e^{-w\ell_\gamma}
=\int_A^\infty\frac{e^{-(w-1)t}}t\,dt+F_X(w),
\]

\[
F_X(w)=
\sum_{\ell_\gamma\le A}e^{-w\ell_\gamma}
-e^{-wA}R_X(A)
+w\int_A^\infty e^{-wt}R_X(t)\,dt.
\]

端点原子由有限和及 `R_X(A)` 精确保留。由 (PG)，`F_X` 在 `Re(w)>theta_X` 全纯。`r>=2` 的重复和 `V_X(w)` 在 `Re(w)>1/2` 全纯，证明与前轮重复项相同。

记 `z=w-1`。在 `Re(z)>0` 上，

\[
I_A(z)=\int_A^\infty e^{-zt}\frac{dt}{t}
=-\operatorname{Log}z+j_A(z).
\]

`Log` 是在右半平面取正实值为实对数的分支。因为

\[
j_A'(z)=\frac{1-e^{-Az}}z
\]

在零点可去奇，`j_A` 延为零点附近的全纯函数。于是存在在零点附近全纯的 `mathcal F_X(z)`，使

\[
\mathscr U_X(1+z)
=-\operatorname{Log}z+\mathcal F_X(z)
\quad(\operatorname{Re}z>0,\ |z|\text{ 充分小}),
\]

\[
\boxed{
U_X(1+z)=\frac{\Psi_X(z)}z,\qquad
\Psi_X(z):=e^{\mathcal F_X(z)}
\text{ 全纯且非零。}}
\]

故普通未缩时乘积在 `w=1` 具有简单亚纯极点。这里仅构造该点附近的延拓，没有建立全局谱行列式或迹公式。正实侧还给出

\[
\mathscr U_X(1+\varepsilon)
=\log(1/\varepsilon)+\mathcal F_X(0)+O_X(\varepsilon).
\]

### 5.3 原 N^{-3} 归一化给出非整数发散阶

固定 `N>=1`，令

\[
q_N=N^{-3},\qquad
\Xi_N(z)=\exp\!\left(\mathcal F_{\Sigma_N}(z)/N^3\right),
\qquad \kappa_N:=\Xi_N(0)>0.
\]

由已经证明的几何对数恒等式，

\[
\boxed{
Q_N(N(1+z))
=e^{-q_N\operatorname{Log}z}\,\Xi_N(z)
\quad(\operatorname{Re}z>0,\ |z|\text{ 充分小}).}
\]

这由原 Euler 对数推出，不是用实轴渐近另选一个复根定义 `Q_N`。特别地，

\[
\boxed{
Q_N(N(1+\varepsilon))
=\kappa_N\varepsilon^{-1/N^3}
\bigl[1+O_N(\varepsilon)\bigr]
\quad(\varepsilon\downarrow0).}
\]

若 `N>=2`，则 `0<q_N<1`。一个在 `s=N` 的邻域内亚纯、且从右侧发散的函数，Laurent 主项必须具有正整数极点阶；上述非整数阶与此矛盾。因此 `Q_N` 在 `s=N` 无局部亚纯延拓。`B(s)` 在 `s=N>1` 附近全纯且非零，故同一障碍传递给 `R_N`，并且

\[
R_N(N(1+\varepsilon))
=\frac{\kappa_N}{B(N)}
\varepsilon^{-1/N^3}
\bigl[1+O_N(\varepsilon)\bigr]
\qquad(N\ge2).
\]

未改变归一化来消除分数阶；未缩时乘积的简单极点和原归一化乘积的分数阶是不同对象的准确结论。

### 5.4 正分支及 N=1 例外

右侧精确分拆为

\[
Q_N^+(Nw)=Q_N(Nw)/B_0(w)^N.
\]

用 `B_0(1+epsilon)->B_*>0` 及其一阶展开，对每个固定 `N`，

\[
\boxed{
Q_N^+(N(1+\varepsilon))
=\frac{\kappa_N}{B_*^N}
\varepsilon^{-1/N^3}
\bigl[1+O_N(\varepsilon)\bigr].}
\]

这还给出正分支日志的定量发散律

\[
E_N^+(1+\varepsilon)
=\frac1{N^3}\log(1/\varepsilon)
+\log\kappa_N-NH_*+O_N(\varepsilon).
\]

`B_0(w)^(-N)` 仅在原右侧全纯并有上述边界值；不能把它称为跨越临界点的全纯前因子。对 `N>=2`，仅凭实轴的非整数发散阶已足以排除正分支的局部亚纯延拓；相对正分支的基准 `B^+(s)` 在 `s=N>1` 附近全纯且非零，结论同样成立。

当 `N=1` 时，完整 `Q_1=B` 在 `s=1` 有简单亚纯极点，非整数阶反证不适用。然而 `Q_1^+=B^+=B/B_0` 仍不能在那里亚纯延拓：若它能够延拓，则非零亚纯函数之商 `B/B^+` 会给出 `B_0` 的亚纯延拓，与上轮的零分支障碍矛盾。

结合上轮零分支结论，局部情况可汇总为：

| 对象 | `N=1`，经过临界点 `s=1` | `N>=2`，经过临界点 `s=N` |
| --- | --- | --- |
| 完整 `Q_N` | 简单亚纯极点 | 非整数发散阶，无亚纯延拓 |
| 正分支 `Q_N^+` | 发散，但无亚纯延拓 | 非整数发散阶，无亚纯延拓 |
| 零分支 `Q_N^0` | 有限，但无亚纯延拓 | 有限，但无亚纯延拓 |
| 全部／正／零相对分支 `R_N^bullet` | 全部恒为一 | 均无亚纯延拓 |

“无亚纯延拓”也排除了在该点的全纯延拓；所有判断只针对经过所列临界点的局部延拓，不证明整条竖线是自然边界。

## 6. 两种极限及尚未取得的尺度

第 3 节和第 5 节不冲突。前者沿 `N->infinity` 保持 `s-N>=u/sqrt N>0`，得到正分支趋一；后者先固定 `N`，再令 `s downarrow N`，正分支以 `epsilon^(-1/N^3)` 发散。上轮两次迭代极限不交换的结论保留。

特别地，不得把固定层公式中的 `O_N(epsilon)`、`kappa_N` 或全纯邻域当作对 `N` 一致，直接代入任意快速趋零的 `epsilon_N`。本轮没有据此定位真正最窄的临界过渡层。

收缩半平面结果的主要限制为：

- `s-N=u/sqrt N` 是已证充分尺度，不是必要或最优尺度。更小的指定尺度需要进一步控制 (M) 中的 `rho_N` 和 Gaussian 项。
- 未把 Gaussian 加法误差改成乘法误差，未从中心极限定理或固定类渐近直接推出移动类估计。
- 所有 `M,C_LL,c_LL,rho_N` 都属于固定基底的理论控制，没有数值认证、显式 producer 或误差常数证书。
- 渐近比较移动了参数，没有恢复固定 `s` 的有限值产品；也没有把任何临界发散值通过正则化改成有限值。
- 未修改原 AN-1–AN-5 的指定域、索引条件或其正式处置，未以局部延拓结果替代全局行列式等式。

## 7. 来源复核、实际操作与文档保全

本轮按 ARS 论证流程区分总计数推论、全同调类一致输入、项目估计和固定层局部分析。主线程推导并整合；同系助手分别检错计数余项／局部极点、整除分拆／渐近后果、Sharp 来源／移动半平面估计。这是同系检错，不是独立科学证据、跨模型认证或正式审查。

主线程通过普通浏览核对 Sharp 作者版的 Theorem 1、prime／整数同调定义及单位切丛表示，核对 Manchester 的公开卷页信息；并核对 Wu–Xue 作者 v3 的有向计数定义、Theorem 2 和 21。Petridis–Risager 的旧 Theorem 2.8 也被用于比较证据强度，但其较弱归一化误差不承担 (ULL) 的证明。没有声称逐页通读全部证明、复证外部定理、认证作者版与刊本逐字一致、获得人类已读确认或完成本地 PDF 结构检查。

同系来源检索中，AMS 落地页／DOI 请求返回 Internal Error，未登记为成功解析；后续来源支持采用已公开的作者全文与机构书目。Manchester 明确标为 Restricted 的 PDF 未被请求，也未重试此前 Utah 403 路径或绕过访问限制。没有上传私人材料或调用程序化文献／外部模型服务。

本轮仅新增此笔记，在零同调临界笔记、未缩时移动参数笔记和总内部记录各追加入口。保全比较使用编辑前快照，核对三个旧文件的原文前缀及十三个指定保护文件的长度和 SHA-256；文档检查限定为链接、数学环境、控制字符、占位符、末尾换行与范围标记。这些机械检查不认证数学真实性或外部来源充分性。

未运行科学实验、owner 枚举、矩阵／长度程序、既有 artifact writer、论文构建或正式审查脚本；未修改论文、代码、结果、锁、正式回执和历史失败记录。工作目录既有非 Git 环境事实不影响本轮按字节快照保全，未重新初始化版本管理。正式 `FAIL / BLOCK`、Route 状态及 Stage 5／6 均不变。

[critical-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_homology_zero_critical_boundary_20260908.md
[moving-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_unscaled_cover_products_and_moving_parameter_limit_20260908.md
[sharp-source]: https://warwick.ac.uk/fac/sci/maths/people/staff/richard_sharp/p2/gauss.pdf#page=2
[sharp-meta]: https://eprints.maths.manchester.ac.uk/505/
[pgt-source]: https://arxiv.org/pdf/2209.10415v3#page=13

## 追加进展：指数临界过渡的充要判准（2026-09-08）

后续[全局同调 Gaussian 界与指数临界过渡](internal_exponential_critical_crossover_20260908.md)另行使用 Sharp 的小线性锥一致相对渐近和 Coles–Sharp 的加权固定窗指数率，合并得到全同调 Gaussian 上界，不把本笔记 ULL 的加法误差改写为乘法误差。通过格点和、中心归一化及 `t>=N^3` 上的稠密格点一致计数，证明 `Re(w)>=1+epsilon_N` 移动半平面中 `Q_N(Nw)/B_0(w)^N`、`R_N(Nw)/B_0(w)^N` 一致趋一，当且仅当 `log_+(1/epsilon_N)=o(N^3)`（`0<epsilon_N<=1`）。若实轴临界量 `N^(-3)log_+(1/(epsilon_N N^2))` 趋于有限 `lambda>=0`，两个比值趋于 `exp(lambda)`；量趋于无穷时只证明日志等价及比值发散，不无条件指数化为乘积相对等价。该推导不用本笔记固定覆盖渐近中的随层未控常数，也不包括精确临界点。原归一化、局部非亚纯结论及 `N=1` 例外、冻结输入和正式状态均不变。
