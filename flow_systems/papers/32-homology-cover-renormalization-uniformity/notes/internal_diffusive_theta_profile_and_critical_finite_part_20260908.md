# P32 内部研究：扩散尺度 theta 轮廓与临界有限部分

记录日期：2026-09-08 UTC。接续[可积字符尾项笔记][tail-note]。本轮确定该笔记留下的有限部分极限，并在同一输入内将全右半圆轮廓细化到 `N^{-3}` 阶。

固定对象仍是同一个带标记、曲率负一的闭双曲亏格二曲面，全部本原有向 owner，原 `1/N` 时间缩放和 `1/N^3` 对数归一化。以下对充分大的整数 `N` 成立，因而也适用于原固定阶乘子序列。分析中换元 `t=N^2u` 不改变几何、时钟、产品或冻结长度截断。

证明链为：统一字符 PGT 的更高精度 → 扩散尺度真实计数 → 全正轴加权 L1 收敛 → 临界有限部分与复参数轮廓。Poisson 和 Mellin 公式用于表达已经出现的极限函数与常数，不用于替换原 Euler 产品的定义。

## 1. 沿用输入和精确首系数

记

\[
a_N(t)=\#\{g:\ell_g\le t,\ \alpha_g\in N\mathbb Z^4\setminus\{0\}\},
\qquad
r_N(t)=N^4te^{-t}a_N(t)-1.
\]

[可积字符尾项笔记][tail-note]在同一个固定基底上已经证明

\[
E_N^+(w)
=N\sum_{\alpha_g\in N\mathbb Z^4\setminus\{0\}}e^{-w\ell_g}
+\mathcal E_N(w),\qquad
\sup_{\operatorname{Re}w\ge1}|\mathcal E_N(w)|\le Ce^{-cN},
\tag{1}
\]

\[
0\le N^4te^{-t}a_N(t)\le C e^{-cN^2/t}\quad(t>0),
\tag{2}
\]

\[
|r_N(t)|\le C\left(t^{-1}+e^{-ct/N^2}+N^4t^{-2}\right)
\quad(t\ge N^2).
\tag{3}
\]

为取固定层临界值，还沿用[收缩临界笔记][shrinking-note]第 2.2 节的更精确信息：`mathcal E_N` 的级数在闭 `Re w>=1` 上绝对一致收敛，对每个固定 `N` 在 `Re w>1/2` 全纯。因此 `mathcal E_N(1)` 是合法的边界值，不是仅由 (1) 的大小界猜测出来的极限。

该笔记第 5 节还给出了每个固定层的 `kappa_N>0`：

\[
E_N^+(1+\varepsilon)
=N^{-3}\log(1/\varepsilon)
+\log\kappa_N-NH_*+O_N(\varepsilon),
\quad \varepsilon\downarrow0,
\tag{4}
\]

其中 `H_*=H(1)`、`B_*=e^{H_*}`，而

\[
Q_N(Nw)=B_0(w)^N e^{E_N^+(w)},\qquad R_N(s)=Q_N(s)/B(s).
\tag{5}
\]

### 1.1 本轮需要 p=4，不能只使用上一轮选定的 p=3

[可积字符尾项笔记][tail-note]第 2–3 节核对并转换了 Sharp Lemma 3。其无权本原字符计数结论对每个固定整数 `p>=1` 成立：

\[
\pi_\theta(t)
=\mathbf1_{\theta\in U}\operatorname{Li}(e^{s(\theta)t})
+O_p(e^t/t^p),\qquad \theta\in\mathbb T^4,
\tag{6}
\]

误差对全部字符一致，且同一个固定邻域上

\[
s(\theta)=1-\tfrac12\theta^{\mathsf T}D\theta+O(|\theta|^3),
\quad D=D^{\mathsf T}>0,\quad
s_0\le s(\theta)\le1-c_0|\theta|^2.
\tag{7}
\]

旧笔记选 `p=3` 以证明 (3)，但没有限制 (6) 可使用的精度。本轮一次固定 `p=4`；它不是令精度阶随 `N` 增长。若只取 `p=3`，在 `t=N^2u` 下归一化余项是 `O(u^{-2})`，不趋零，不能据此得出后面的 theta 极限。

### 1.2 零类首系数由同一计数的唯一极限确定

[零同调临界笔记][zero-note]的固定零类输入为

\[
n_0(t)=\frac{e^t}{t^3}
\left(c_{\rm hom}+O(t^{-1})\right).
\]

[指数临界笔记][real-note]第 2.2 节记录了同一有向口径的 Sharp 首系数：

\[
C_0=(2\pi)^{-2}\sigma^{-4},\qquad \sigma^8=\det D.
\]

将其固定类首项取在 `alpha=0`，与上述 `t^3e^{-t}n_0(t)` 的极限比较，唯一性给出

\[
\boxed{
c_{\rm hom}=c_D:=(2\pi)^{-2}(\det D)^{-1/2}.}
\tag{8}
\]

这不是为使 Poisson 公式成立而选取的新扣除常数。两个输入使用同一个整数同调基及本原测地流轨道口径；正反向分别计数，零同调时也不合并，没有额外方向因子二。

## 2. 真实计数的扩散尺度极限

定义

\[
F_N(u):=N^4(N^2u)e^{-N^2u}a_N(N^2u),\qquad u>0,
\tag{9}
\]

以及只由 `D` 决定的格点函数

\[
\Theta_D(u):=\sum_{k\in\mathbb Z^4}
e^{-2\pi^2u\,k^{\mathsf T}Dk},
\qquad
F_D(u):=\Theta_D(u)-\frac{c_D}{u^2}.
\tag{10}
\]

本节证明 `F_N->F_D` 在 `(0,infinity)` 的每个紧子区间上一致收敛。

### 2.1 精确字符平均与零类扣除

令 `mathscr T_N` 是环面上的全部 `N` 阶字符。有限字符正交性仍给

\[
a_N(t)=N^{-4}\sum_{\theta\in\mathscr T_N}\pi_\theta(t)-n_0(t).
\]

设 `t=N^2u`，在 (6) 中取 `p=4`，得到

\[
F_N(u)=
\sum_{\theta\in\mathscr T_N\cap U}
te^{-t}\operatorname{Li}(e^{s(\theta)t})
-N^4te^{-t}n_0(t)
+O(N^{-2}u^{-3}).
\tag{11}
\]

这里 `N^4` 项的平均与 `N^{-4}` 抵消，乘回归一化后才产生 `N^4/t^{p-1}`；没有再损失一个网格点数因子。零类项则为

\[
N^4te^{-t}n_0(t)=\frac{c_D}{u^2}+O(N^{-2}u^{-3}).
\tag{12}
\]

### 2.2 在固定整数格上使用可求和的支配函数

将网格点写为 `theta=2pi k/N`，选中心整数代表，并把未落在该代表域或 `U` 内的项延为零。对每个固定 `k`，它最终被包括，且

\[
(1-s(2\pi k/N))N^2u
=2\pi^2u\,k^{\mathsf T}Dk+O_k(u/N).
\tag{13}
\]

对 `s in[s_0,1]` 一致有

\[
te^{-t}\operatorname{Li}(e^{st})
=s^{-1}e^{-(1-s)t}\bigl(1+O(t^{-1})\bigr).
\]

固定 `0<u_-<=u<=u_+<infinity`，每个被包括的格点项因此受

\[
C_{u_-,u_+}e^{-c u_-|k|^2}
\]

控制。这是固定整数格上的可求和函数。有限格点逐项极限与统一 Gaussian 尾界给出

\[
\sum_{\theta\in\mathscr T_N\cap U}
te^{-t}\operatorname{Li}(e^{s(\theta)t})
\longrightarrow\Theta_D(u)
\]

在该区间上一致。结合 (11)–(12)，

\[
\boxed{
F_N(u)\longrightarrow F_D(u)
\quad\text{局部一致于 }u\in(0,\infty).}
\tag{14}
\]

这里没有对随 `N` 增长的整个字符网格直接使用固定字符点态渐近；统一 Gaussian 支配承担了扩展到全格点和的步骤。

## 3. Poisson 表示、端点和换基不变性

### 3.1 零类扣除后的正表示

本轮普通浏览核对 NIST DLMF 的 [Poisson 公式 1.8.14 及 Gaussian 特例 1.8.16][poisson-source]。采用 Fourier 核 `exp(-2pi i x·xi)`。

对 `f_u(x)=exp(-2pi²u x^TDx)`，正定 Gaussian 积分给

\[
\widehat f_u(\xi)=\frac{c_D}{u^2}
\exp\!\left(-\frac{\xi^{\mathsf T}D^{-1}\xi}{2u}\right).
\]

Gaussian 及其各阶导数快速衰减；可对各坐标应用 Poisson 公式，并用绝对收敛交换积分与格点和。由此得到四维形式

\[
\Theta_D(u)=\frac{c_D}{u^2}
\sum_{m\in\mathbb Z^4}
\exp\!\left(-\frac{m^{\mathsf T}D^{-1}m}{2u}\right),
\]

\[
\boxed{
F_D(u)=\frac{c_D}{u^2}
\sum_{m\in\mathbb Z^4\setminus\{0\}}
\exp\!\left(-\frac{m^{\mathsf T}D^{-1}m}{2u}\right)>0.}
\tag{15}
\]

这同时核对了 Fourier 中的 `2pi²` 和实际零类项 `c_D/u²`，并不是从 `F_N>=0` 反推常数。

### 3.2 两端渐近与有限部分

由正定性及两种格点表示，存在 `b,c,C>0` 使

\[
F_D(u)=O(u^{-2}e^{-c/u})\quad(u\downarrow0),
\qquad
F_D(u)=1-\frac{c_D}{u^2}+O(e^{-bu})\quad(u\to\infty).
\tag{16}
\]

因此定义

\[
A_D:=
\int_0^1F_D(u)\,\frac{du}{u}
+\int_1^\infty(F_D(u)-1)\,\frac{du}{u},
\]

\[
\boxed{C_D:=A_D-\gamma}
\tag{17}
\]

时，两段都是绝对收敛的普通积分。`gamma` 是 Euler 常数。没有把两个各自发散的积分相减，也未声明 `F_D` 单调、始终小于一或 `C_D` 具有固定符号。

若换用其他分割点 `L>0`，相同常数写为

\[
C_D=-\gamma-\log L+
\int_0^L F_D(u)\,\frac{du}{u}
+\int_L^\infty(F_D(u)-1)\,\frac{du}{u}.
\tag{18}
\]

对 `L` 求导或直接相减即可验证；显示的 `-log L` 不能省略。

对 `A in GL_4(Z)`，整数格双射 `k mapsto A^T k` 给

\[
\Theta_{ADA^{\mathsf T}}=\Theta_D,\qquad
F_{ADA^{\mathsf T}}=F_D,\qquad C_{ADA^{\mathsf T}}=C_D.
\tag{19}
\]

故常数不依赖所选整数基的坐标表示。作为纯矩阵尺度校验，`F_{aD}(u)=F_D(au)` 给 `C_{aD}=C_D+log a`，`a>0`。这个校验不授权实际改变曲面或原时钟。

## 4. 全正轴的加权 L1 收敛

局部一致极限本身不足以交换无穷积分。将 (2)–(3) 改写为

\[
0\le F_N(u)\le Ce^{-c/u}\quad(u>0),
\tag{20}
\]

\[
|F_N(u)-1|
\le C\left(\frac1{N^2u}+e^{-cu}+\frac1{u^2}\right)
\quad(u\ge1).
\tag{21}
\]

对 `0<u<=1`，(20) 及 (16) 给 `|F_N-F_D|/u` 一个形如 `C u^{-3}e^{-c'/u}` 的可积支配；对 `u>=1`，先分别减去一，得到可积支配

\[
\frac{|F_N(u)-F_D(u)|}{u}
\le C\left(u^{-2}+e^{-c'u}/u+u^{-3}\right).
\]

这里 `1/N²<=1`，支配函数独立于充分大的 `N`。由 (14) 与支配收敛，

\[
\boxed{
\rho_N:=\int_0^\infty|F_N(u)-F_D(u)|\,\frac{du}{u}
\longrightarrow0.}
\tag{22}
\]

两个函数本身都在无穷远趋近一，`int_1^infinity F_N du/u` 不收敛；(22) 是差值的可积收敛，不能写成各函数在该权空间中单独可积。

同理，每个充分大的 `N` 有有限的

\[
A_N:=\int_0^1F_N(u)\,\frac{du}{u}
+\int_1^\infty(F_N(u)-1)\,\frac{du}{u},
\qquad |A_N-A_D|\le\rho_N\to0.
\tag{23}
\]

本轮未给 `rho_N` 的数值或具体幂次速率；其极限由已经证明的支配条件取得。

## 5. 临界振幅有限部分的真正极限

### 5.1 先处理每个固定 N 的边界值

令 `varepsilon>0`，`a=N²varepsilon`。由绝对收敛的计数积分及换元，

\[
N^3E_N^+(1+\varepsilon)
=(1+\varepsilon)\int_0^\infty e^{-au}F_N(u)\,\frac{du}{u}
+N^3\mathcal E_N(1+\varepsilon).
\tag{24}
\]

将积分精确分拆为

\[
\int_0^\infty e^{-au}F_N(u)\,\frac{du}{u}
=\mathrm E_1(a)+
\int_0^\infty e^{-au}
\bigl(F_N(u)-\mathbf1_{[1,\infty)}(u)\bigr)\,\frac{du}{u}.
\tag{25}
\]

第二项在 `a downarrow0` 时由绝对可积性趋于 `A_N`。沿用[复临界笔记][complex-note]已经核对的指数积分展开，
`E_1(a)=-log a-gamma+o(1)`。对每个固定 `N`，

\[
(1+\varepsilon)\mathrm E_1(N^2\varepsilon)
-\log(1/\varepsilon)
\longrightarrow -2\log N-\gamma.
\]

这里 `varepsilon log(1/varepsilon)->0`，所以 `1+varepsilon` 前因子不留下额外常数。再由 `mathcal E_N` 的已知连续性及 (4)，得到精确恒等式

\[
\boxed{
N^3\log\frac{\kappa_N}{B_*^N}+2\log N
=A_N-\gamma+N^3\mathcal E_N(1).}
\tag{26}
\]

### 5.2 再令 N 趋于无穷

由 (1)、(22)–(23)，

\[
\boxed{
N^3\log\frac{\kappa_N}{B_*^N}+2\log N
\longrightarrow C_D,}
\tag{27}
\]

且与极限之差至多 `rho_N+C N³e^{-cN}`。等价地，

\[
\boxed{
\log\frac{\kappa_N}{B_*^N}
=\frac{-2\log N+C_D+o(1)}{N^3},\qquad
N^{2/N^3}\frac{\kappa_N}{B_*^N}
=1+\frac{C_D}{N^3}+o(N^{-3}).}
\tag{28}
\]

(27) 严格加强上轮的有界结论。取极限顺序是：先独立建立真实计数的统一支配，再对每个固定 `N` 使用 (4)，最后由 (23) 取 `N` 极限。没有将固定层未知的 `O_N(varepsilon)` 插入对角线。

因 `B_*^N` 已分离零同调主增长，剩下这一级极限常数只通过同调协方差矩阵 `D` 出现；这不表示曲面的全部几何由 `D` 唯一决定。

## 6. N^{-3} 阶的完整复参数轮廓

### 6.1 极限 Laplace 函数和临界展开

对 `Re a>0` 定义

\[
\mathcal J_D(a):=
\int_0^\infty e^{-au}F_D(u)\,\frac{du}{u},
\qquad
\mathcal J_N(a):=
\int_0^\infty e^{-au}F_N(u)\,\frac{du}{u}.
\tag{29}
\]

这些积分在该开半平面绝对收敛、全纯，且由 (22)

\[
\boxed{
\sup_{\operatorname{Re}a>0}
|\mathcal J_N(a)-\mathcal J_D(a)|\le\rho_N.}
\tag{30}
\]

设 `b_D(u)=F_D(u)-1_[1,infinity)(u)`。不仅 `int|b_D|du/u<infinity`，由 (16) 还有 `int|b_D|du<infinity`。对 `Re a>=0`，
`|e^{-au}-1|<=|a|u`，所以

\[
\mathcal J_D(a)
=\mathrm E_1(a)+A_D+O(|a|).
\]

采用右半平面的主值对数，

\[
\boxed{
\mathcal J_D(a)=-\Log a+C_D+O(|a|)
\quad(a\to0,\ \operatorname{Re}a>0),}
\tag{31}
\]

余项无需非切向条件。这里只在 `a!=0` 定义函数，减去显式对数后才取得有限部分。

### 6.2 不能从大小界猜导数：用 theta 公式单独证明

为控制全部 `|z|<=1`，需要额外处理 `z mathcal J_D(N²z)`。定义
`g_D(u)=F_D(u)/u`。两种 theta 级数在任何紧正区间上均可逐项微分；对端点则分别使用 (15) 与 (10)。具体给出

\[
g_D'(u)=O(u^{-5}e^{-c/u})\quad(u\downarrow0),
\]

\[
g_D'(u)=-u^{-2}+3c_Du^{-4}+O(e^{-bu})
\quad(u\to\infty).
\]

因此

\[
g_D(0+)=g_D(\infty)=0,\qquad
\int_0^\infty|g_D'(u)|\,du<\infty.
\tag{32}
\]

对 (29) 分部积分，两端项消失，得到

\[
a\mathcal J_D(a)=\int_0^\infty e^{-au}g_D'(u)\,du,
\qquad
\boxed{\sup_{\operatorname{Re}a>0}|a\mathcal J_D(a)|\le C_D^{(1)}<\infty.}
\tag{33}
\]

`C_D^{(1)}` 是导数绝对积分界，不是 (17) 的有限部分常数。这里不对阶梯状的实际 `F_N` 求导；(32) 来自明确的极限 theta 函数，而不是从 (20)–(21) 的大小控制推出。

### 6.3 原全右半圆上的一致细化

设 `Re z>0, |z|<=1`，`a=N²z`。精确换元给

\[
N^3E_N^+(1+z)
=(1+z)\mathcal J_N(N^2z)+N^3\mathcal E_N(1+z).
\]

用 (30) 及 (33)，

\[
\boxed{
\sup_{\substack{\operatorname{Re}z>0\\|z|\le1}}
\left|N^3E_N^+(1+z)-\mathcal J_D(N^2z)\right|
\le2\rho_N+\frac{C_D^{(1)}}{N^2}+CN^3e^{-cN}
\longrightarrow0.}
\tag{34}
\]

所以完整产品有统一的更精细相对轮廓

\[
\boxed{
\sup_{\substack{\operatorname{Re}z>0\\|z|\le1}}
\left|
\frac{Q_N(N(1+z))}
{B_0(1+z)^N\exp\!\bigl(N^{-3}\mathcal J_D(N^2z)\bigr)}
-1\right|
=o(N^{-3}).}
\tag{35}
\]

`R_N` 同式，因为 `log B(N(1+z))` 在该域指数小。(35) 的误差含 `rho_N`，不能把它改写为未经证明的固定幂次 `O(N^{-3-delta})`。

特别地，对任意 `z_N` 满足 `Re z_N>0` 且 `N²z_N->0`，有

\[
N^3E_N^+(1+z_N)+\Log(N^2z_N)\longrightarrow C_D.
\tag{36}
\]

(36) 保留了 `-i arg(N²z_N)` 的首阶相位修正，不能把 `Log` 换成 `log|·|` 后仍声称同一个复数常数极限。

若 `a>0` 固定，取 `z=a/N²`，则原参数偏移为 `s-N=a/N`，并有 `N³E_N^+(1+a/N²)->mathcal J_D(a)`。这描述的是原产品已经定义的移动参数，不是在精确临界点赋有限值。

## 7. 同一常数的标量格点 zeta 表达

这节只为 (17) 的普通收敛积分提供另一表达，不构造任何项目谱算子或量子行列式。本节的 `s` 是新的 Mellin 变量，不是原乘积中的物理参数。

先在 `Re s>2` 定义正定二次型的格点级数

\[
Z_D(s):=\sum_{k\in\mathbb Z^4\setminus\{0\}}
(2\pi^2 k^{\mathsf T}Dk)^{-s}.
\tag{37}
\]

绝对收敛来自正定性及四维格点计数。Gamma 积分的换元与绝对 Fubini 给

\[
\Gamma(s)Z_D(s)=
\int_0^\infty u^{s-1}(\Theta_D(u)-1)\,du.
\]

定义两个整函数

\[
H_0(s):=\int_0^1u^{s-1}F_D(u)\,du,\qquad
H_\infty(s):=\int_1^\infty u^{s-1}(\Theta_D(u)-1)\,du.
\]

其整性分别由 (16) 的小端／大端指数衰减和局部一致支配保证。在初始收敛域分拆积分后，

\[
\boxed{
\Gamma(s)Z_D(s)
=H_0(s)+H_\infty(s)+\frac{c_D}{s-2}-\frac1s.}
\tag{38}
\]

右侧提供到零点附近的明确亚纯延拓。由于
`int_1^infinity c_Du^{-3}du=c_D/2`，其零点展开为

\[
\Gamma(s)Z_D(s)=-\frac1s+A_D+O(s).
\]

本轮核对了 DLMF [5.7.1 及其后首两个系数][gamma-source]：
`1/Gamma(s)=s+gamma s²+O(s³)`。相乘便得

\[
\boxed{
Z_D(0)=-1,\qquad Z_D'(0)=A_D-\gamma=C_D.}
\tag{39}
\]

没有引用未检查的谱行列式定理来识别常数；(38) 已给出本节所需的延拓构造。若改用不含 `2pi²` 的格点和
`mathcal Z_D(s)=sum_{k!=0}(k^TDk)^{-s}`，则

\[
C_D=\mathcal Z_D'(0)+\log(2\pi^2).
\tag{40}
\]

该尺度项不能漏掉。`Z_D` 是这里明确定义的标量二次型级数，不等同于原测地流的 Euler 函数，也不是 Riemann zeta、全局行列式等式或 Hilbert–Pólya 对象。

## 8. 来源、范围与实际检查

本轮按 ARS 论证流程分开处理来源、参数尺度、积分交换和有限部分。三个关键检错点是：扩散尺度极限需要 `p>3` 的字符余项；在无穷远必须先减去一才有可积控制；极限函数的导数界必须由 theta 表示另证，不能从实际计数大小界推导。主线程为唯一写入者，同系助手只读复核格点极限／首系数、有限部分／复域量词及 Poisson／Mellin 归一化；这些检错不构成独立科学证据或正式同行审查。

Sharp 字符估计、固定零类展开、全局 Gaussian 界及有限层临界公式均复用已经记录且未变的输入。本轮新增普通浏览只用于 NIST DLMF 的 Poisson 公式与 Gamma 首项；没有重新请求旧文献 PDF、进行程序化文献核验或上传私人材料。来源中的一维公式、首项展开与本项目四维极限推导已明确分开；不提出文献穷尽或发表新颖性判断。

本轮仅新增此笔记，并在可积字符尾项笔记、指数临界笔记和总内部记录追加入口。编辑前使用只读 Node 文件字节／SHA-256 快照；最后核对三个追加文件的旧前缀、十七个指定保护文件，以及新增文本的链接、数学环境、控制字符、占位符、反引号配对和末尾换行。沿用上轮已修正的占位符检测方法，不重新触发已知误报。实际检查结果在交接答复中报告，机械保全不认证数学或来源充分性。

未运行科学实验、owner 枚举、数值积分、矩阵或长度程序、既有 artifact writer、论文构建或正式审查脚本。未改论文、代码、实验结果、输入锁、正式回执、历史失败记录、原 `FAIL / BLOCK` 或 Route 状态；Stage 5／6 停止条件保持有效。

本轮结论的边界是：

- 已证明有限部分收敛并给出两个等价表达，但没有认证当前固定曲面的具体 `D` 数值，也没有输出数值 `C_D`。
- 所有统一性针对同一个固定基底；换基不变性不是不同曲面族上的统一误差定理，更不识别曲面的全部几何。
- `rho_N->0` 没有已证的具体速率；更高阶修正仍需控制高阶压力项、零类展开与小尺度区域，不由 (28) 自动产生。
- 未定义精确临界点的有限 Euler 值，也未改变局部分数阶／零分支非亚纯结论或各 `N=1` 例外。
- 格点 zeta 导数只表达本轮标量常数，不构成算子域、自伴性、迹公式、谱行列式、固定参数恢复或正式 AN／Route 义务的完成。

[tail-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_integrable_character_tail_and_global_radial_profile_20260908.md
[shrinking-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_shrinking_critical_layer_and_fractional_singularity_20260908.md
[zero-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_homology_zero_critical_boundary_20260908.md
[real-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_exponential_critical_crossover_20260908.md
[complex-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_complex_critical_crossover_and_tangential_limits_20260908.md
[poisson-source]: https://dlmf.nist.gov/1.8#E14
[gamma-source]: https://dlmf.nist.gov/5.7#E1
