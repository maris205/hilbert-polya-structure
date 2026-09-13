# P32 内部研究：全局同调 Gaussian 界与指数临界过渡

记录日期：2026-09-08 UTC。接续[收缩临界层笔记][shrinking-note]。本轮在同一固定几何和原归一化下，将平方根正偏移的充分结论推进为移动半平面零同调主项的充要判准，并确定实轴上的非平凡指数过渡。

新增论证分为四环：小同调锥相对渐近与加权轨道增长给出全局 Gaussian 上界；格点求和给出对数 majorant；稠密格点上的一致计数确定首系数；Laplace 积分将它转为原乘积的临界过渡。外部定理与下文项目推论分开记录，不从固定覆盖层的渐近常数偷换出随层一致性。

这仍是内部理论推导及普通公开来源核对；未改变原 `1/N` 时间缩放、`1/N^3` 日志归一化、冻结输入、论文或正式状态，未启动实验、owner 枚举、Route 评估或 Stage 5／6。

## 1. 沿用对象与本轮主张

固定同一个真实、带标记、曲率负一的闭双曲亏格二曲面 `Sigma`。全部本原有向 owner 的整数同调为 `alpha_g in Z^4`，物理周期为 `ell_g`，且

\[
\ell_g\ge\ell_*>0,\qquad
\|\alpha_g\|_\infty\le M\ell_g,\qquad
\|\alpha_g\|_2\le2M\ell_g.
\]

改变起点只作时间平移，反向 owner 不合并。沿用上轮已经建立的等式

\[
\mathscr L_N(Nw)=NH(w)+E_N^+(w),\qquad
B_0(w)=e^{H(w)},\quad
Q_N(s)=e^{\mathscr L_N(s)},\quad R_N(s)=Q_N(s)/B(s).
\]

这里 `H=mathscr B_0` 是零同调 Euler 日志，不是下文外部计数定理中的熵函数。设

\[
\mathcal A_N
=\{g:\alpha_g\in N\mathbb Z^4\setminus\{0\}\},\qquad
a_N(t)=\#\{g\in\mathcal A_N:\ell_g\le t\}.
\]

上轮的最大重数分拆为

\[
\boxed{
E_N^+(w)
=N\sum_{g\in\mathcal A_N}e^{-w\ell_g}
+\mathcal E_N(w),\qquad
\sup_{\operatorname{Re}w\ge1}|\mathcal E_N(w)|
\le C_{\rm rem}e^{-N/(4M)}.}
\tag{1}
\]

主和仍只在 `Re(w)>1` 使用；余项则可到闭临界半平面。所有 `g in mathcal A_N` 满足 `ell_g>=N/M`，故 `a_N(t)=0` 于 `t<N/M`。余项来自真因子重数和最大重数的重复次数至少二；本轮不重复改变该分拆。

令 `log_+(x)=max(0,log x)`。本轮要证明：存在仅依赖固定基底及本轮外部输入的 `tau_N->0`、`C,c_*>0`，使全部 `0<epsilon<=1` 上有

\[
\boxed{
\left|E_N^+(1+\varepsilon)-\Lambda_N(\varepsilon)\right|
\le\tau_N\Lambda_N(\varepsilon)
+C\frac{1+\log N}{N^3}+Ce^{-c_*N},\qquad
\Lambda_N(\varepsilon)=
\frac{\log_+(1/(\varepsilon N^2))}{N^3}.}
\tag{2}
\]

式 (2) 是本轮推论，不是引用文献中的公式；其左侧是实轴值。复域的一致趋一判准将在第 6 节由非负系数 majorant 推出。

## 2. 两种外部输入如何闭合全局同调上界

### 2.1 小线性锥内的一致相对渐近

本轮重新核对 Richard Sharp，*A local limit theorem for closed geodesics and homology* 的[作者公开版 pp.2–3，Eq. (0.2)][sharp-source]。不同于上轮 Theorem 1 的一致加法误差，Eq. (0.2) 在一个足够小的固定线性锥中给出一致相对渐近。

用 `mathfrak h` 重命名来源中的熵函数。对某个固定 `delta>0`，

\[
n_\alpha(t)
=\frac{C(\alpha/t)e^{t\mathfrak h(\alpha/t)}}{t^3}
\bigl(1+r(t,\alpha)\bigr),\qquad
\sup_{\|\alpha\|_2\le\delta t}|r(t,\alpha)|\longrightarrow0.
\tag{3}
\]

原文在 Eq. (0.2) 后给出 `C` 连续、`C(0)=C_0>0`，以及

\[
\mathfrak h(x)
=1-\tfrac12\langle x,D^{-1}x\rangle+O(\|x\|_2^3),
\qquad D>0.
\tag{4}
\]

采用同一个整数同调基；若原文范数与此处欧氏范数不同，只需缩小固定的 `delta`。本轮只使用原文写明的 Taylor 信息，不额外声称已核验熵函数的完整解析理论。

缩小 `delta` 后，二次项支配三阶余项，故存在 `c_near>0`，使
`mathfrak h(x)<=1-c_near||x||_2^2`；`C(x)` 在该闭球上有正下界与有限上界。再使 (3) 的一致相对误差至多一，就得到

\[
n_\alpha(t)\le
C_{\rm near}\frac{e^t}{t^3}
e^{-c_{\rm near}\|\alpha\|_2^2/t}
\quad(\|\alpha\|_2\le\delta t,\ t\ge T_{\rm near}).
\tag{5}
\]

原文指出三阶项妨碍从 (0.2) 直接得到其精确 Gaussian 局部极限；这不妨碍 (5) 这种减弱二次指数常数后的上界。也不能据此把上轮 ULL 的加法误差直接改成乘法误差。

### 2.2 有向口径与中心首系数

Sharp 作者版 p.1 定义累计 prime 闭测地线及整数同调，但没有在该定义处直接使用“oriented”一词。方向识别来自其 p.5 的单位切丛测地流及有符号积分

\[
\int_0^{\ell(\gamma)}
F(\gamma(t),\dot\gamma(t))\,dt=[\gamma].
\]

其 p.11 对一般流也使用 prime periodic orbit 和 least period 的约定。应用到同一个单位切丛时，owner 是按流方向的本原周期轨道；反向是另一条流轨道并将基底同调变号，零同调时也不合并。这个几何识别是采用精确系数的前提，不再仅以可能的固定方向倍数吸收上界。

来源 p.2 的 Theorem 1 后给出

\[
C_0=\frac1{(2\pi)^2\sigma^4},\qquad
\sigma^8=\det D,
\]

其中本项目熵为一、第一 Betti 数为四。故在固定整数坐标的 Lebesgue 测度下，

\[
f(x):=C_0e^{-\langle x,D^{-1}x\rangle/2},
\qquad
\boxed{\int_{\mathbb R^4}f(x)\,dx=1.}
\tag{6}
\]

这是 Gaussian 积分的直接计算，没有额外方向因子二。已有实际 owner 总素测地线定理 `n(t)~e^t/t` 与此规范一致；本轮没有通过任意调整 `C_0` 来“修正”口径。

### 2.3 远离小锥的指数尾界

新增来源是 Solly Coles–Richard Sharp，*Helicity, linking and the distribution of null-homologous periodic orbits for Anosov flows* 的[公开作者修订版][weighted-source]：

- 作者版 p.2：计数集合为 prime periodic orbits，长度是 least period。
- pp.7、10：压力变分定义、唯一平衡态，以及 Lemma 3.5 的 Hölder 势参数实解析性。
- pp.10–11：第 4 节明确没有同调类限制；在 weak-mixing Anosov 流背景下，Lemma 4.2 给固定长度窗口的加权计数指数增长率。

本项目的固定紧负曲率曲面测地流是传递 Anosov 流，并满足所需 weak mixing。也可将非格点周期条件与既有总 PGT 对照：若所有周期位于某个 `aZ`，两个固定正距离且同处连续格点间的时间具有相同计数，与 `e^t/t` 渐近矛盾；来源 §2 给出传递 Anosov 流中相应的非格点／weak-mixing 等价。本轮不调用其后零同调 linking 定理或三维 helicity 主结论。

只提取 Lemma 4.2 明确陈述的窗口指数率。若 `phi` 是固定 Hölder 势、`kappa>0` 且 `P(phi)+kappa>0`，令

\[
A_\phi(j)=
\sum_{\substack{g\in\mathcal O\\j\le\ell_g\le j+1}}
e^{\int_g\phi}.
\]

该引理给 `j^(-1)log A_phi(j)->P(phi)`。吸收有限短轨道后，对整数窗口求和即得

\[
\boxed{
W_\phi(t):=\sum_{\ell_g\le t}e^{\int_g\phi}
\le C_{\phi,\kappa}e^{(P(\phi)+\kappa)t}.}
\tag{7}
\]

窗口端点可能重复计数，只扩大上界。本轮不使用该引理证明中更强的累计渐近，也不导入其中把 prime 指数和与 Euler zeta 作相同简单极点描述的解析措辞；prime 指数和的临界奇性不能据此当作 zeta 的简单极点。本轮所需只有陈述中的指数率及上述有限窗口求和。

取与固定同调基对偶的光滑闭形式 `omega_j`，在单位切丛上令 `F_j(v)=omega_j(v)`。于是 `int_g F_j=alpha_(g,j)`。时间反演将 `F_j` 变号、将不变测度双射到不变测度，并保持其时间一熵，故压力变分式给

\[
P(qF_j)=P(-qF_j),\qquad
P(0)=1,\qquad P(\pm qF_j)=1+O(q^2).
\]

给定 (5) 的固定 `delta`，选固定 `q>0` 足够小，使全部八个势同时满足

\[
P(\sigma qF_j)\le1+q\delta/8,\qquad
\kappa=q\delta/8,\qquad P(\sigma qF_j)+\kappa>0.
\]

若 `||alpha||_2>delta t`，则有某个 `j` 和 `sigma in {+1,-1}` 满足 `sigma alpha_j>delta t/2`。有限次指数 Markov 不等式及 (7) 给

\[
\begin{aligned}
\sum_{\|\alpha\|_2>\delta t}n_\alpha(t)
&\le\sum_{j=1}^4\sum_{\sigma=\pm1}
e^{-q\delta t/2}W_{\sigma qF_j}(t)\\
&\le\boxed{C_\delta e^{(1-\eta)t}},
\qquad \eta=q\delta/4>0.
\end{aligned}
\tag{8}
\]

这些势、常数和起始时间全部在固定基底上选定，不随 `N`、`alpha` 或积分中的 `t` 重新优化。

### 2.4 合并为全局 Gaussian

有轨道出现的同调类满足 `||alpha||_2<=2Mt`。选

\[
0<c_{\rm G}\le
\min\{c_{\rm near},\eta/(8M^2)\}.
\]

远端每一类的计数受 (8) 的总计数控制，而

\[
t^3e^{-\eta t+c_{\rm G}\|\alpha\|_2^2/t}
\le t^3e^{-\eta t/2}
\]

有界。支持外计数为零；与近端 (5) 合并，便有固定常数 `C_G,T_G>0`，使

\[
\boxed{
n_\alpha(t)\le
C_{\rm G}\frac{e^t}{t^3}
e^{-c_{\rm G}\|\alpha\|_2^2/t}
\quad(\alpha\in\mathbb Z^4,\ t\ge T_{\rm G}).}
\tag{G}
\]

(G) 是 (3)、(7) 及几何支持界共同推出的项目估计，不是把任何一篇来源的单一定理改写成更强结论。

## 3. 格点和与对数 majorant

设 `u=t/N^2`。初等 Gaussian 格点估计给出某些 `C_theta,c_theta>0`：

\[
\Theta(u):=\sum_{k\in\mathbb Z^4\setminus\{0\}}
e^{-c_{\rm G}\|k\|_2^2/u}
\le C_\theta u^2e^{-c_\theta/u}
\quad(u>0).
\tag{9}
\]

证明：`u>=1` 时将四个一维和与 Gaussian 积分比较，得到 `C u^2`，再吸收 `e^(-c_theta/u)`。`0<u<=1` 时利用非零格点 `||k||_2>=1`，先提出 `e^(-c_G/(2u))`，余和一致有界；取 `c_theta=c_G/4`，用 `u^(-2)e^(-c_G/(4u))` 有界吸收所需 `u^2`。

对足够大 `N`，有 `N/M>=T_G`。在 `a_N` 非零的时间域内，对 (G) 求和并用 (9) 得

\[
\boxed{
a_N(t)\le
C\frac{e^t}{N^4t}e^{-c_\theta N^2/t}.}
\tag{10}
\]

`t<N/M` 时左侧为零，故可以把这个 majorant 延到全部 `t>0`。对于 `0<epsilon<=1`，Tonelli 给出

\[
\begin{aligned}
N\sum_{g\in\mathcal A_N}e^{-(1+\varepsilon)\ell_g}
&=N(1+\varepsilon)
\int_0^\infty e^{-(1+\varepsilon)t}a_N(t)\,dt\\
&\le\frac C{N^3}
\int_0^\infty e^{-\varepsilon t-c_\theta N^2/t}\frac{dt}{t}\\
&=\frac C{N^3}J(\varepsilon N^2),
\end{aligned}
\tag{11}
\]

其中

\[
J(z)=\int_0^\infty e^{-zu-c_\theta/u}\frac{du}{u}.
\]

分割积分为 `(0,1)`、`(1,1/z)`、`(1/z,infinity)`，中段用
`1-e^(-zu-c_theta/u)<=zu+c_theta/u`，得到

\[
J(z)=\log(1/z)+O(1)\quad(0<z\le1),\qquad
J(z)\le J(1)\quad(z\ge1).
\tag{12}
\]

因此绝对值和的非负 majorant 满足

\[
\boxed{
\sup_{\operatorname{Re}w\ge1+\varepsilon}|E_N^+(w)|
\le Ce^{-c_*N}
+\frac C{N^3}
\left[1+\log_+\frac1{\varepsilon N^2}\right].}
\tag{13}
\]

同样的上界也控制其逐项绝对总和；`c_*>0` 可以取不大于 `1/(4M)` 的固定值。式 (13) 没有上轮未知的 `rho_N/epsilon^2` 放大项。

特别地，`log_+(1/(epsilon_N N^2))=o(N^3)` 已足以给出 `E_N^+->0` 的移动半平面一致性。此处尚只是单侧界；必要性和首系数需要下一节，不从 (13) 单独推出。

## 4. 稠密格点区的首系数与统一量词

现在证明

\[
\boxed{
\eta_N:=
\sup_{t\ge N^3}
\left|N^4t e^{-t}a_N(t)-1\right|
\longrightarrow0.}
\tag{14}
\]

这是在固定基底上移动同调格点的计数，不是固定覆盖 PGT 的随层版本。`N^3` 只是本证明选用的积分分割点，不是新冻结 cutoff 或枚举合同。

对每个固定 `R>0`，(3)–(4) 蕴含

\[
\sup_{\|\alpha\|_2\le R\sqrt t}
\left|t^3e^{-t}n_\alpha(t)
-f(\alpha/\sqrt t)\right|
\longrightarrow0
\quad(t\to\infty).
\tag{15}
\]

原因是该范围最终包含于小线性锥，`C(alpha/t)->C_0` 一致，且熵展开的指数余项为 `O_R(t^(-1/2))`；相对余项使用其真正的尾上确界趋零，而非猜测具体速率。

令 `h=N/sqrt t`。对 `t>=N^3` 有 `0<h<=N^(-1/2)`。中心格点和写成

\[
N^4t e^{-t}
\sum_{\substack{k\ne0\\\|hk\|_2\le R}}n_{Nk}(t)
=h^4\sum_{\substack{k\ne0\\\|hk\|_2\le R}}
\left[f(hk)+o_R(1)\right].
\tag{16}
\]

这里 `h^4` 乘中心格点数一致有界，故可累加误差；当 `N->infinity` 时，Riemann 和对全部 `0<h<=N^(-1/2)` 一致趋向 `int_(||x||<=R)f(x)dx`。删除零格点仅损失 `h^4f(0)->0`。

对于外尾，(G) 给

\[
N^4t e^{-t}
\sum_{\substack{k\ne0\\\|hk\|_2>R}}n_{Nk}(t)
\le C_{\rm G}h^4
\sum_{\|hk\|_2>R}e^{-c_{\rm G}\|hk\|_2^2}.
\tag{17}
\]

右侧在 `0<h<=1` 上随 `R->infinity` 一致趋零：用边长 `h` 的格点小立方体与稍减弱指数的 Gaussian 积分比较即可。先固定 `R` 令 `N->infinity`，再令 `R->infinity`，结合 (6)，得到 (14)。

这一证明保留了“有界中心区的一致相对渐近”和“无限格点尾的可积控制”两步，未对无界格点直接求和一致加法 `o(1)`。

## 5. 实轴临界日志的统一渐近

取 `T_N=N^3`。对 (11) 的精确积分在 `T_N` 分割。低段由 (10) 控制：

\[
\begin{aligned}
0\le
N(1+\varepsilon)\int_0^{N^3}
e^{-(1+\varepsilon)t}a_N(t)\,dt
&\le\frac C{N^3}
\int_0^{N^3}e^{-c_\theta N^2/t}\frac{dt}{t}\\
&=\frac C{N^3}\mathrm E_1(c_\theta/N)
=O\!\left(\frac{1+\log N}{N^3}\right),
\end{aligned}
\tag{18}
\]

一致于 `0<epsilon<=1`。其中 `E_1(x)=int_x^infinity e^(-v)dv/v`。这是对 Tonelli 积分变量分割，轨道长度恰在分割点不产生遗漏或额外负端点项。

高段由 (14) 得

\[
N(1+\varepsilon)\int_{N^3}^\infty
e^{-(1+\varepsilon)t}a_N(t)\,dt
=\frac{1+\varepsilon}{N^3}
\mathrm E_1(\varepsilon N^3)
\left(1+\theta_{N,\varepsilon}\right),
\qquad |\theta_{N,\varepsilon}|\le\eta_N.
\tag{19}
\]

使用对全部 `x>0` 成立的初等界

\[
\left|\mathrm E_1(x)-\log_+(1/x)\right|\le C,\qquad
x\mathrm E_1(x)\le e^{-x}\le1,
\]

以及

\[
\left|
\log_+\frac1{\varepsilon N^3}
-\log_+\frac1{\varepsilon N^2}
\right|\le\log N,
\]

就有

\[
\left|
\frac{1+\varepsilon}{N^3}\mathrm E_1(\varepsilon N^3)
-\Lambda_N(\varepsilon)
\right|
\le C\frac{1+\log N}{N^3}.
\tag{20}
\]

其中 `epsilon E_1(epsilon N^3)/N^3<=N^(-6)`，所以 `1+epsilon` 不引入额外主项。合并 (1)、(18)–(20)，并将最终有界的 `eta_N` 所乘低阶项吸收入余项，即得 (2)，可取某个 `tau_N->0`。

(2) 的量词是对每个充分大 `N`、同时对全部 `0<epsilon<=1` 成立。因此可合法代入任意指定的 `epsilon_N`；没有用到上轮固定覆盖的 `kappa_N`、谱隙、局部全纯半径或 `O_N(epsilon)` 常数。

## 6. 充要判准、实轴过渡与不能混同的极限

### 6.1 移动半平面相对趋一的充要条件

对任意序列 `0<epsilon_N<=1`，令

\[
\Omega_N=\{w:\operatorname{Re}w\ge1+\varepsilon_N\},
\qquad \Lambda_N=\Lambda_N(\varepsilon_N).
\]

正分支 Euler 日志的全部系数非负。因此不仅有上界，而且

\[
\boxed{
\sup_{w\in\Omega_N}
\left|\frac{Q_N(Nw)}{B_0(w)^N}-1\right|
=e^{E_N^+(1+\varepsilon_N)}-1.}
\tag{21}
\]

上界由 `|e^z-1|<=e^{|z|}-1` 及非负 majorant 给出；等号在正实边界点取得。由 (2) 得

\[
\boxed{
\sup_{w\in\Omega_N}
\left|\frac{Q_N(Nw)}{B_0(w)^N}-1\right|\longrightarrow0
\quad\Longleftrightarrow\quad
\Lambda_N\longrightarrow0.}
\tag{22}
\]

必要性也包含任意振荡序列：对充分大 `N`，(2) 给
`E_N^+(1+epsilon_N)>=(1-tau_N)Lambda_N-o(1)`。

已有基准日志界在整个 `Re(w)>=1` 上为
`|mathscr B(Nw)|=O(e^(-c_0N))`。故 (22) 中 `Q_N` 换成 `R_N`，同一充要条件仍成立。必要性只需在正实边界观察 `E_N^+(1+epsilon_N)-mathscr B(N(1+epsilon_N))`；基准项趋零，不能抵消非零临界量。

由于两种对数的差至多 `2log N`，还可以将条件写为

\[
\boxed{
\log_+(1/\varepsilon_N)=o(N^3).}
\tag{23}
\]

写成原偏移 `delta_N=s_N-N=N epsilon_N` 时，条件等价于
`log_+(1/delta_N)=o(N^3)`，只要仍保留 `0<epsilon_N<=1` 的所述域。条件不含 `epsilon_N=0`；完整乘积在精确临界点仍发散。

### 6.2 实轴上的三种行为

令 `w_N=1+epsilon_N`，仍取 `0<epsilon_N<=1`。由 (2) 和固定基准日志的指数小界：

| 临界量的行为 | 正分支实日志 | 原乘积的相对行为 |
| --- | --- | --- |
| `Lambda_N->0` | `E_N^+(w_N)->0` | `Q_N(Nw_N)/B_0(w_N)^N->1`，`R_N` 同 |
| `Lambda_N->lambda in (0,infinity)` | `E_N^+(w_N)->lambda` | 两个比值均趋于 `exp(lambda)` |
| `Lambda_N->infinity` | `E_N^+(w_N)~Lambda_N` | 两个比值趋于正无穷，其实对数均等价于 `Lambda_N` |

最后一行不能加强为 `Q_N/B_0^N~exp(Lambda_N)`：目前的 `tau_N Lambda_N` 可能不趋零，指数化会放大该误差。中间一行是实轴结论，不声称整个复移动半平面上都趋于同一个非一常数。

### 6.3 原参数中的显式指数过渡

沿用已证 `H_*=H(1)>0`、`D_*=H'(1)<0`、`B_*=exp(H_*)>1`。对每个固定 `lambda>=0`，取

\[
\varepsilon_N=N^{-2}e^{-\lambda N^3},\qquad
s_N=N+N^{-1}e^{-\lambda N^3}.
\]

此时 `Lambda_N=lambda`，且 `delta_N=s_N-N->0`。零同调边界展开给

\[
NH(1+\varepsilon_N)-NH_*
=D_*\delta_N+
O\!\left(N\varepsilon_N^2
\log(1/\varepsilon_N)\right)\longrightarrow0.
\]

所以

\[
\boxed{
\frac{Q_N(N+N^{-1}e^{-\lambda N^3})}{B_*^N}
\longrightarrow e^\lambda,\qquad
\frac{R_N(N+N^{-1}e^{-\lambda N^3})}{B_*^N}
\longrightarrow e^\lambda
\quad(\lambda\ge0\ {\rm fixed}).}
\tag{24}
\]

固定 `lambda=0` 对应 `s_N-N=1/N`，不是精确临界点。所有固定幂次正偏移 `s_N-N=N^(-p)`（`p>0`）都落在趋一侧；例如 `epsilon_N=e^(-N^2)` 也落在趋一侧。非平凡的过渡由 `N^(-3)log(1/epsilon_N)` 的有限非零极限识别，而不是上轮的平方根端点。

这确定的是所述移动半平面相对主项和实轴极限的渐近阈值，不提供有限层可认证的临界长度、数值误差常数或全部复方向的过渡图像。

### 6.4 与固定层分数阶奇性相容

上轮对每个固定 `N` 得到临界实轴阶 `epsilon^(-1/N^3)`，并在 `N>=2` 排除完整归一化乘积的局部亚纯延拓；`N=1` 的完整简单极点与相对恒一例外均保留。

本轮的 `N^(-3)log(1/epsilon_N)` 过渡与该阶数相容，但论证来源不同：本轮通过固定基底的全同调类相对渐近、远尾和格点积分获得随层控制，没有将固定层局部展开未经验证地代入快速对角线。也没有构造正则化临界值、证明整条自然边界，或把该乘积等同于谱行列式。

## 7. 论证边界、实际操作与文档保全

本轮采用 ARS 的论证构建流程，以“外部输入—项目推理—量词—反对意见及限制”组织记录。四个关键风险分别被显式处理：近锥相对式不能自动管远尾；一致加法误差不能在无限格点上直接求和；方向常数不能在精确系数中被忽略；日志相对误差不能无条件指数化为乘积相对误差。

主线程推导、写入并整合；同系助手分别只读核查近锥与方向、格点积分与交叉量词、加权来源与远尾。本轮复核不是独立科学证据、跨模型认证或正式审查，也不对结果作新颖性或发表优先权声明。

主线程普通浏览实际核读 Sharp 作者版 Eq. (0.2) 及相邻定义／展开、Coles–Sharp 作者修订版的 prime 定义、压力及 Lemma 4.2 陈述和相关上下文。上轮已核对的固定基底 PGT 和几何分拆作为未变输入复用；未声称复证外部定理、逐页通读两篇全部证明、取得人类已读确认或校验作者版与刊本逐字一致。

本轮请求 Warwick WRAP 所列出版版 PDF 时返回 Internal Error／Timeout，未登记为成功访问、未重试；实际定理支持仍为此前已成功打开的公开作者版。既有 Restricted Manchester PDF、Utah 403 和失败 AMS 路径未重试，未绕过访问限制。一次本地角色说明定位读取因路径不正确失败，随后用 `rg --files` 定位并完成正确文件的只读读取；没有隐去该失败，也没有因此改变科学输入。

本轮仅新增此笔记，并在收缩临界层笔记、未缩时移动参数笔记和总内部记录各追加入口。编辑前以只读 Node 文件读取及 SHA-256 取得快照；写后核对三个旧文件的全部原文前缀和十四个指定保护文件的原始长度／哈希。文档检查限于本轮新增文本的本地链接、数学环境、控制字符、占位符、反引号配对、末尾换行和范围标记。这些机械检查不认证数学正确性或外部来源充分性；实际结果在本轮交接答复中报告。

未运行科学实验、owner／矩阵／长度程序、既有 artifact writer、论文构建或正式审查脚本；未改论文、代码、实验、结果、输入锁、正式回执或历史失败记录。既有正式 `FAIL / BLOCK`、Route 状态及 Stage 5／6 停止边界保持不变。

[shrinking-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_shrinking_critical_layer_and_fractional_singularity_20260908.md
[sharp-source]: https://warwick.ac.uk/fac/sci/maths/people/staff/richard_sharp/p2/gauss.pdf#page=2
[weighted-source]: https://warwick.ac.uk/fac/sci/maths/people/staff/richard_sharp/p2/linking_final_nonlinearity_revision_20october2023.pdf#page=10

## 追加进展：复径向轮廓与切向限制（2026-09-08）

后续[复临界过渡、零分支相位与切向限制](internal_complex_critical_crossover_and_tangential_limits_20260908.md)将本笔记格点一致计数转为复 Laplace 加性误差：主项由 `N^(-3)log_+(1/(N^2|z|))` 决定，误差仍受 `eta_N N^(-3)log_+(1/(N^2 Re z))` 控制。由此取得有界法向指数域中的一致径向相对轮廓，以及更一般误差乘积趋零路径上的复极限；双指数偏移 `s_N=N+N^(-1)(exp(-aN^3)+i sigma exp(-bN^3))` 除以 `B_0(1)^N` 后趋于 `exp(min(a,b))`。另补零分支复对数展开，证明固定非零原虚偏移 `theta` 下的极限相位为 `exp(i D_* theta)`，并说明这不推翻本笔记的整个半平面充要判准。任意极端切向尚未闭合；抽象截断余项只反驳从大小界自动推出消去的推理，不否证实际流。未改冻结方案、论文或正式状态。

## 追加进展：任意切向、超临界相对等价与振幅首项（2026-09-08）

后续[字符计数可积尾项与全右半圆径向轮廓](internal_integrable_character_tail_and_global_radial_profile_20260908.md)从新核对的 Sharp Lemma 3 导出实际模 `N` 本原计数的可积余项，取得全部 `Re z>0, |z|<=1` 上 `Q_N(N(1+z))/(B_0(1+z)^N exp(Lambda_N^rad(z)))=1+O(N^{-3})`，`R_N` 同式。实轴径向量趋于无穷时，原先只证的日志等价由新的绝对小误差升级为乘积相对等价；这是增加余项证据后的加强，不是对旧误差直接指数化。全域估计再按固定层顺序令正实偏移趋零，给 `log(kappa_N/B_*^N)=-2log N/N³+O(N^{-3})`，识别振幅的首个对数修正但未求出更细的有限部分常数。整个移动半平面充要判准及精确临界点发散不变；未改原时钟、归一化、冻结对象、论文或正式状态。

## 追加进展：确定临界有限部分常数（2026-09-08）

后续[扩散尺度 theta 轮廓与临界有限部分](internal_diffusive_theta_profile_and_critical_finite_part_20260908.md)通过扩散尺度真实计数及全正轴加权 L1 收敛，证明 `log(kappa_N/B_*^N)=(-2log N+C_D+o(1))/N³`。常数由同一个同调协方差矩阵 `D` 的 theta 格点和决定，有绝对收敛积分及明确标量格点 zeta 导数两种表达，并在整数换基下不变；不是新引入的原乘积正则化或谱行列式。新 Laplace 函数还将全右半圆径向轮廓细化至 `o(N^{-3})` 的相对误差，保留首阶复相位。未认证数值常数或更高阶速率，不包括精确临界点；冻结方案、论文和正式状态不变。
