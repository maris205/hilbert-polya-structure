# P32 内部研究：字符计数可积尾项与全右半圆径向轮廓

记录日期：2026-09-08 UTC。接续[复临界笔记][complex-note]第 7.2 节：本轮对实际非零同调格点计数证明加权尾项可积，因而去掉该笔记中正分支过渡的法向指数限制。

证明链为：固定基底上的统一字符计数 → sharp 本原无权计数 → 有限字符平均及零类扣除 → 随长度衰减的实际余项 → 全右半圆的一致相对轮廓。来源提供第一环；后面各环是这里的推导，不是来源中直接陈述的项目结论。

全部对象仍是同一个固定、带标记、曲率负一的闭双曲亏格二曲面，全部本原有向 owner，原 `1/N` 时间缩放与 `1/N^3` 对数归一化。没有更换几何、抽取 owner 子族、执行实验或推进正式状态。

## 1. 沿用输入与待闭合的积分

按[指数临界笔记][real-note]及[复临界笔记][complex-note]记

\[
\mathcal A_N=\{g:\alpha_g\in N\mathbb Z^4\setminus\{0\}\},
\qquad
a_N(t)=\#\{g\in\mathcal A_N:\ell_g\le t\},
\]

\[
E_N^+(w)=N\sum_{g\in\mathcal A_N}e^{-w\ell_g}
+\mathcal E_N(w),\qquad
\sup_{\operatorname{Re}w\ge1}|\mathcal E_N(w)|
\le Ce^{-c_*N}.
\tag{1}
\]

同一基底上已有全局界和零类界

\[
a_N(t)\le C\frac{e^t}{N^4t}e^{-c_\theta N^2/t}
\quad(t>0,\ N\text{ 充分大}),\qquad
n_0(t)\le C\frac{e^t}{t^3}\quad(t\text{ 充分大}).
\tag{2}
\]

定义实际误差，不能用抽象小函数替换：

\[
r_N(t)=N^4t e^{-t}a_N(t)-1,\qquad
I_N=\frac1{N^3}\int_{N^3}^{\infty}|r_N(t)|\,\frac{dt}{t}.
\tag{3}
\]

上轮只用 `eta_N=sup_{t>=N^3}|r_N(t)|->0`，未建立 `I_N->0`。本轮证明

\[
\boxed{
|r_N(t)|\le C\left(\frac1t+
e^{-ct/N^2}+\frac{N^4}{t^2}\right)
\quad(t\ge N^2),\qquad I_N=O(N^{-5}).}
\tag{T}
\]

所有常数依赖同一固定基底与下文一次选定的字符邻域，独立于 `N,t`；没有数值认证。

## 2. 新核对的来源：固定基底上的统一字符计数

### 2.1 精确入口与口径

本轮普通浏览核对 Richard Sharp，*A local limit theorem for closed geodesics and homology*，[作者公开版][sharp-source] pp.4–7：Propositions 1–2、Lemma 1、§2 的定义及 Lemma 3。需要的是 p.7 的 **Lemma 3**，不是 p.8 的 Proposition 5；后者是同调辅助函数的局部极限定理，不能替代这里的定量余项。

该文覆盖紧致负曲率曲面，故本项目的固定亏格二曲面满足几何条件；熵在原物理时钟下为 `h=1`。有向口径沿用[指数临界笔记][real-note]第 2.2 节的单位切丛周期轨道识别，反向 owner 不合并。

将来源的字符变量改写为 `theta`、长度变量改写为 `t`、可任意选取的误差幂阶改写为 `K`，避免与覆盖模数 `N` 混用。设 `T^4=R^4/(2pi Z)^4`，来源使用

\[
S_\theta^*(t)=
\sum_{\substack{g\ {\rm prime},\,m\ge1\\m\ell_g\le t}}^{*}
\ell_g e^{i\langle\theta,m\alpha_g\rangle},
\tag{4}
\]

其中星号仅将 `m ell_g=t` 的项计为半权；迭代项的长度权重是 `ell_g`，不是 `m ell_g`。

Lemma 3 的内容是：对每个固定整数 `K>=1`，在充分大的全部实 `t` 上，

\[
S_\theta^*(t)=
\mathbf1_{\theta\in U}\frac{e^{s(\theta)t}}{s(\theta)}
+O_K(e^t/t^K),
\quad\text{误差常数对全部 }\theta\in\mathbb T^4\text{ 一致}.
\tag{5}
\]

这里 `U` 是固定的充分小零点邻域。Proposition 1 与 Lemma 1 给出的 `s(theta)` 是实值解析函数，

\[
s(0)=1,\quad \nabla s(0)=0,\quad
\nabla^2s(0)=-D,\quad D>0.
\tag{6}
\]

因此可以一次选定 `U`，使其上

\[
s_0\le s(\theta)\le1-c_0|\theta|^2,\qquad s_0>0.
\tag{7}
\]

若需缩小来源的邻域，旧新邻域间固定环带的主项具有固定指数缺口，可吸收到任意逆幂余项；没有要求常数在邻域半径趋零时一致。注意这里 Hessian 为 `-D`，不是实同调熵函数的 `-D^{-1}`。

(5) 是固定基底的全字符估计；不是先对每个覆盖 `Sigma_N` 分别应用 PGT，再假定其余项常数随 `N` 一致。来源 Proposition 2 的显示域写作 `Re(s)>1-epsilon`，本次只取 `h=1`，不据此解释一般熵的版本。

### 2.2 从半端点到 sharp 累计：保留同一常数

全重复长度谱在任意有界区间局部有限：本原长度下界正、有限长度以内本原轨道有限、每条本原轨道只有有限次迭代。

固定充分大的 `t`，令 `u downarrow t` 且 `u>t`。可在 `t` 右侧无新长度的间隙内取 `u`；此时 `S_theta^*(u)` 就是 `t` 处全部端点计全权的和。对 (5) 取此右极限，连续主项及 `e^u/u^K` 给出

\[
S_\theta^\le(t)=
\mathbf1_{\theta\in U}\frac{e^{s(\theta)t}}{s(\theta)}
+O_K(e^t/t^K)
\tag{8}
\]

且仍对全部 `theta` 一致。这里使用 (5) 对所有充分大实长度成立，不是沿删去某些端点邻域的子序列成立。间隙长度无需有统一正下界，也没有另添短窗渐近假设。

## 3. 去迭代与去长度权重

令 `P(t)` 为全体本原有向轨道数，沿用固定基底的粗界 `P(t)<=Ce^t` 及最短长度 `ell_*>0`。在 `m>=2` 的和中，每条本原轨道贡献的绝对长度权重至多 `t`，且其长度不超过 `t/2`，故

\[
\sup_\theta
\left|\sum_{\substack{g\ {\rm prime},\,m\ge2\\m\ell_g\le t}}
\ell_g e^{i\langle\theta,m\alpha_g\rangle}\right|
\le tP(t/2)\le Ct e^{t/2}.
\tag{9}
\]

这被任意 `O_K(e^t/t^K)` 吸收。因此 sharp 本原加权和

\[
W_\theta(t)=\sum_{\ell_g\le t}\ell_g
e^{i\langle\theta,\alpha_g\rangle}
\]

也满足 (8)。定义本原无权和

\[
\pi_\theta(t)=\sum_{\ell_g\le t}
e^{i\langle\theta,\alpha_g\rangle}.
\]

取固定 `t_0` 足够大，且 `s_0 t_0>log 2`。Stieltjes 分部求和给

\[
\pi_\theta(t)=\frac{W_\theta(t)}t+
\int_{t_0}^{t}\frac{W_\theta(u)}{u^2}\,du
+C_\theta,\qquad \sup_\theta|C_\theta|<\infty.
\tag{10}
\]

这里 `C_theta` 仅含固定长度以前的有限项。对 `theta in U`，

\[
\frac{e^{s t}}{st}
+\int_{t_0}^{t}\frac{e^{su}}{s u^2}\,du
=\operatorname{Li}(e^{st})+C_s,\qquad
\sup_{s\in[s_0,1]}|C_s|<\infty,
\tag{11}
\]

其中 `Li(v)=int_2^v du/log u`。等式可对 `t` 求导验证，两边导数均为 `e^{st}/t`。

若加权余项为 `O_K(e^u/u^K)`，其 (10) 中贡献为

\[
O_K(e^t/t^{K+1})+
O_K\!\left(\int_{t_0}^{t}\frac{e^u}{u^{K+2}}\,du\right)+O_K(1)
=O_K(e^t/t^{K+1}).
\]

积分界可在 `t/2` 分段得到，常数独立于字符。特别地，每个固定整数 `p>=1` 都有

\[
\boxed{
\pi_\theta(t)=
\mathbf1_{\theta\in U}\operatorname{Li}(e^{s(\theta)t})
+O_p(e^t/t^p),\quad \theta\in\mathbb T^4.}
\tag{12}
\]

远离 `U` 时只有余项。去权过程中没有将可能有符号的字符和当作正测度；只在估计迭代和及余项时取绝对值。

## 4. 有限字符平均给出真实格点余项

### 4.1 先取平均，再扣除零同调

令 `Theta_N` 为 `T^4` 上的全部 `N` 阶字符网格，具有 `N^4` 个点。字符正交关系给出精确等式

\[
b_N(t):=\#\{g:\ell_g\le t,\ \alpha_g\in N\mathbb Z^4\}
=\frac1{N^4}\sum_{\theta\in\Theta_N}\pi_\theta(t),
\qquad a_N(t)=b_N(t)-n_0(t).
\tag{13}
\]

零同调属于所有模 `N` 的零类，必须扣除；不能将 `b_N` 直接认作 `a_N`。

将 (12) 代入，由于误差对全部字符一致，`N^4` 项的平均仍是 `O_p(e^t/t^p)`，不是该平均误差再乘 `N^4`。于是

\[
b_N(t)=\frac{\operatorname{Li}(e^t)}{N^4}
+\frac1{N^4}
\sum_{\substack{\theta\in\Theta_N\cap U\\\theta\ne0}}
\operatorname{Li}(e^{s(\theta)t})
+O_p(e^t/t^p).
\tag{14}
\]

之后乘回 `N^4te^{-t}` 时，余项才成为 `O_p(N^4/t^{p-1})`。

### 4.2 非平凡字符网格的 Gaussian 和

对 `s in[s_0,1]` 及充分大的 `t`，

\[
0\le \operatorname{Li}(e^{st})\le C e^{st}/t,
\qquad
te^{-t}\operatorname{Li}(e^t)=1+O(t^{-1}).
\tag{15}
\]

第一式可将定义积分在其对数变量的中点分段；第二式是一次分部积分后的标准初等余项估计。

将近零网格点写为 `theta=2pi k/N`，选定不重复的环面代表。由 (7)，当 `v=t/N^2>=1` 时，

\[
\begin{aligned}
te^{-t}\!
\sum_{\substack{\theta\in\Theta_N\cap U\\\theta\ne0}}
\operatorname{Li}(e^{s(\theta)t})
&\le C\sum_{k\in\mathbb Z^4\setminus\{0\}}e^{-cv|k|^2}\\
&\le Ce^{-cv/2}
\sum_{k\in\mathbb Z^4\setminus\{0\}}e^{-c|k|^2/2}
\le C'e^{-c'v}.
\end{aligned}
\tag{16}
\]

最后两步使用 `v>=1` 和 `|k|²>=1`。这一步保留了网格尺度；不采用会损失一个 `N^4` 因子的粗最大值估计。

合并 (2)、(13)–(16)，对充分大的 `N` 及全部 `t>=N^2`，

\[
|r_N(t)|\le C_p\left(
\frac1t+e^{-ct/N^2}
+\frac{N^4}{t^2}+\frac{N^4}{t^{p-1}}
\right).
\tag{17}
\]

固定 `p=3`，最后两项合并，即得 (T) 的逐长度界。该选择仅是源定理中一次固定的精度阶，不随覆盖模数增长。

### 4.3 加权可积性及其速率

对 (T) 逐项积分，

\[
\begin{aligned}
I_N
&\le \frac C{N^3}\left[
\int_{N^3}^\infty\frac{dt}{t^2}
+\int_{N^3}^\infty e^{-ct/N^2}\frac{dt}{t}
+N^4\int_{N^3}^\infty\frac{dt}{t^3}\right]\\
&\le C\left(N^{-6}+N^{-4}e^{-cN}+N^{-5}\right)
=O(N^{-5}).
\end{aligned}
\tag{18}
\]

中间指数积分为 `E_1(cN)<=e^{-cN}/(cN)`。同时

\[
\eta_N:=\sup_{t\ge N^3}|r_N(t)|=O(N^{-2}).
\tag{19}
\]

(19) 的速率本身不足以解决任意切向路径；真正消除法向限制的是 (18) 中对长度变量的可积控制。上轮的抽象共振诊断因此仍正确，但它不再是实际计数的证据缺口。

为取得下文更精确的误差，再定义一个不同的分析尾积分

\[
\widehat I_N:=\frac1{N^3}
\int_{N^2}^{\infty}|r_N(t)|\,\frac{dt}{t}.
\]

由于 (T) 已在 `t>=N^2` 成立，同样逐项积分给

\[
\widehat I_N\le C\left[
N^{-5}+N^{-3}\mathrm E_1(c)
+N^{-3}N^4\frac1{2N^4}\right]
=O(N^{-3}).
\tag{19a}
\]

这不是把 (18) 的 `O(N^{-5})` 延用到更早的起点；`I_N` 与 `widehat I_N` 是不同积分。在 `t=N^2` 附近，(T) 的相对误差无需趋零，其归一化后的总积分可控就足够。改变分析分割点不改变产品、时钟、归一化或任何冻结长度截断。

## 5. 全右半圆的一致径向轮廓

写

\[
w=1+z,\qquad \operatorname{Re}z>0,\quad |z|\le1,\qquad
\Lambda_N(z)=\frac1{N^3}\log_+\frac1{N^2|z|}.
\tag{20}
\]

沿用[复临界笔记][complex-note]的绝对可积 Fubini 与主值指数积分表示，本轮将普通积分在 `t=N^2` 处分割，(1) 给

\[
E_N^+(1+z)
=\frac{1+z}{N^3}\mathrm E_1(N^2z)+\mathcal R_N(z).
\]

低段由 (2) 控制为

\[
\left|N(1+z)\int_0^{N^2}e^{-(1+z)t}a_N(t)\,dt\right|
\le\frac C{N^3}\int_0^{N^2}e^{-c_\theta N^2/t}\,\frac{dt}{t}
=\frac C{N^3}\mathrm E_1(c_\theta).
\]

高段的实际误差由 (19a) 满足

\[
\left|
\frac{1+z}{N^3}\int_{N^2}^\infty
e^{-zt}r_N(t)\,\frac{dt}{t}
\right|\le 2\widehat I_N=O(N^{-3}),
\tag{21}
\]

完全不含 `Re(z)` 的倒数或对数。于是

\[
\sup_{\substack{\operatorname{Re}z>0\\|z|\le1}}
|\mathcal R_N(z)|
\le CN^{-3}+Ce^{-c_*N}.
\tag{22}
\]

上轮已由主值表示与级数证明

\[
|\zeta\mathrm E_1(\zeta)|\le1,\qquad
\left|\mathrm E_1(\zeta)-\log_+\frac1{|\zeta|}\right|\le C
\quad(\operatorname{Re}\zeta>0).
\]

现在 `E_1` 的参数直接匹配 `Lambda_N` 的 `N^2` 尺度；另有 `N^{-3}|z E_1(N^2z)|<=N^{-5}`。因此不损失比较两个分割点所产生的 `log N`，得到本轮主结论

\[
\boxed{
\sup_{\substack{\operatorname{Re}z>0\\|z|\le1}}
\left|E_N^+(1+z)-\Lambda_N(z)\right|
\le CN^{-3}.}
\tag{G}
\]

指数小项已吸收。这里比较的是复数日志与实数径向主项，故同时控制相位误差；不是只比较模长。尽管该域容许 `z` 任意接近零，(G) 比较的两项之间有一致小差，不断言各项单独有界。

由 `Q_N(Nw)=B_0(w)^N exp(E_N^+(w))`，令
`d_N=CN^{-3}`，有

\[
\boxed{
\sup_{\substack{\operatorname{Re}z>0\\|z|\le1}}
\left|
\frac{Q_N(N(1+z))}
{B_0(1+z)^N e^{\Lambda_N(z)}}-1
\right|
\le e^{d_N}-1
=O(N^{-3}).}
\tag{23}
\]

完整相对产品 `R_N=Q_N/B` 满足同式：固定基底基准的 Euler 日志在 `Re(N(1+z))>=N` 上指数小。所有公式仅取 `N` 充分大；不将其改写成 `N=1` 的统一相对断言。

### 5.1 任意切向路径与任意径向量

对任意 `Re(z_N)>0, 0<|z_N|<=1`：

- 若 `Lambda_N(z_N)->lambda<infinity`，则 `Q_N(N(1+z_N))/B_0(1+z_N)^N->exp(lambda)`，`R_N` 同样成立。
- 若 `Lambda_N(z_N)->infinity`，仍有 (23) 的乘积相对等价，且相应比值的模趋于无穷、相位趋于零；不再只有日志等价。
- 若 `Lambda_N(z_N)` 仅有界而不收敛，(23) 给一致轮廓与相应子序列极限，不保证单一极限。

上述均无需法向指数 `N^{-3}log_+(1/(N² Re z_N))` 有界，也无需其与 `eta_N` 的乘积趋零。尤其可让实部比虚部小任意多个指数尺度。

还得到路径上的充要判准

\[
\frac{Q_N(N(1+z_N))}{B_0(1+z_N)^N}\longrightarrow1
\quad\Longleftrightarrow\quad
\Lambda_N(z_N)\longrightarrow0,
\tag{24}
\]

`R_N` 同理。必要性来自 (23) 及 `Lambda_N>=0`；这与旧的“整个移动半平面”判准不同，后者还包含最不利的实轴点。

### 5.2 实轴超临界发散也有相对主项

正实 `z=epsilon` 是 (23) 的特例。因此任意 `0<epsilon_N<=1` 上，

\[
\frac{Q_N(N(1+\varepsilon_N))}
{B_0(1+\varepsilon_N)^N}
=\exp\!\left(\frac1{N^3}
\log_+\frac1{N^2\varepsilon_N}\right)
\left[1+O(N^{-3})\right],
\tag{25}
\]

误差对全部这些实参数一致，`R_N` 同理。这明确加强[指数临界笔记][real-note]在径向量趋于无穷时只保留的日志结论；不是把原来大小为 `o(Lambda_N)` 的误差直接指数化。

## 6. 零分支相位与固定层临界振幅

### 6.1 有界原参数偏移，不再限制法向指数

沿用上轮已证的闭右侧展开

\[
H(1+z)=H_*+D_*z-\frac{c_{\rm hom}}2z^2\Log z+O(|z|^2),
\qquad B_*=e^{H_*},\quad D_*<0.
\tag{26}
\]

对每个固定 `K>0`，在 `Re z>0, N|z|<=K` 上，

\[
N\bigl(H(1+z)-H_*-D_*z\bigr)
=O_K((1+\log N)/N).
\]

与 (23) 合并为

\[
\boxed{
\frac{Q_N(N(1+z))}
{B_*^N\exp(D_*Nz+\Lambda_N(z))}
=1+O_K\!\left(\frac{1+\log N}{N}\right)
\quad(\operatorname{Re}z>0,\ N|z|\le K),}
\tag{27}
\]

`R_N` 同样成立。(27) 去掉了上轮还需固定法向指数上界的条件，同时给出理论误差阶。

例如 `z_N=x_N+i theta/N`，其中 `theta!=0` 固定、`x_N>0` 且 `Nx_N->0`，无论 `x_N` 缩得多快，

\[
\frac{Q_N(N+Nx_N+i\theta)}{B_*^N},
\quad
\frac{R_N(N+Nx_N+i\theta)}{B_*^N}
\longrightarrow e^{iD_*\theta}.
\tag{28}
\]

此时 `Lambda_N=0` 最终成立。另一方面，若 `Lambda_N(z_N)->infinity`，则 `Nz_N->0`，故从 (23) 还可将分母 `B_0(1+z_N)^N` 换为 `B_*^N` 而保持乘积相对趋一。

### 6.2 现在可以控制 κ_N，但必须按正确顺序取极限

[收缩临界笔记][shrinking-note]第 5 节对每个固定 `N` 定义了 `kappa_N>0`，并证明

\[
E_N^+(1+\varepsilon)
=\frac1{N^3}\log(1/\varepsilon)
+\log\kappa_N-NH_*+O_N(\varepsilon)
\quad(\varepsilon\downarrow0).
\tag{29}
\]

旧结论本身没有随 `N` 的误差控制。本轮先独立证明 (G) 对全部 `0<epsilon<=1` 一致，再对每个充分大的固定 `N` 令 `epsilon downarrow0`。因这时
`Lambda_N=N^{-3}(log(1/epsilon)-2log N)`，得到

\[
\left|
\log\kappa_N-NH_*+\frac{2\log N}{N^3}
\right|\le CN^{-3}.
\tag{30}
\]

因此首个对数修正可以分离：

\[
\boxed{
\log\frac{\kappa_N}{B_*^N}
=-\frac{2\log N}{N^3}+O(N^{-3}),\qquad
N^{2/N^3}\frac{\kappa_N}{B_*^N}=1+O(N^{-3}).}
\tag{31}
\]

特别地，`kappa_N/B_*^N=1+O((1+log N)/N^3)->1`。这里先有新的统一估计，再取固定层极限；没有将 `O_N(epsilon)` 插入未受控的对角路径。已经识别 `log N/N^3` 项的系数 `-2`，但尚未证明 `N^3 log(kappa_N/B_*^N)+2log N` 收敛，也未求出可能的有限部分常数。

## 7. 范围、来源与实际检查

本轮按照 ARS 的论证流程将来源、转换、实际余项及新推论分开，并检错了最易混淆的四点：半端点与 sharp 累计、迭代的长度权重、字符平均的 `N^4` 因子、零同调扣除。检错中进一步注意到实际余项界已经覆盖 `t>=N^2`，据此在同一输入内将初稿的最终 `O((1+log N)/N^3)` 加强到 `O(N^{-3})`；原 `I_N` 的证明仍原样保留。主线程是唯一文件写入者；同系助手分别只读复核来源入口、去权步骤与网格／复域推论。这些检错不是独立科学证据、跨模型认证或正式同行审查。

新增普通浏览仅访问 Sharp 作者公开版及其已成功返回的文本页段。两页截图请求均返回 `TimeoutError`，没有作为已看见的页面证据，没有重试或转用其他下载通道；这里的页码与公式来自成功返回的 PDF 文本。没有请求既有失败／受限的 WRAP、Manchester、AMS、Utah 路径，没有上传私人材料、使用程序化文献接口或调用外部模型。该基础来源年代较早，沿用的是指定定理及当前作者公开文本，不提出文献穷尽或新颖性主张。

本轮仅新增此笔记，并在复临界笔记、指数临界笔记及总内部记录追加后续入口，保留各旧前缀。编辑前只读 Node 快照与最后的只读检查比较三个追加文件的全部旧字节／SHA-256，另比较十六个指定保护文件；新文本检查本地链接、公式环境、控制字符、占位符、反引号及末尾换行。机械结果在交接答复报告，不把文件检查当作数学证明。

首次只读文档检查的占位符检测器被其自身的字符替换步骤错误地改成检测合法反引号，因而把四份含行内代码的新增文本全部误报；同次旧前缀、保护文件、链接和公式环境检查已通过。保留这次失败记录，仅修正检测器并重新检查，没有为清除误报改动数学正文、旧文件内容或正式回执。

本轮未运行科学实验、owner 枚举、矩阵或长度程序、既有 artifact writer、论文构建或正式审查脚本；未改论文、代码、实验结果、锁、正式回执或历史失败记录。原 `FAIL / BLOCK`、Route 状态和 Stage 5／6 停止条件不变。

仍须保留以下限制：

- (G) 与 (23) 覆盖原解析域内 `Re z>0, |z|<=1` 的全部切向路径，不包含 `z=0`，不赋予精确临界点有限值，也不自动定义整条边界线上的普通 Euler 乘积。
- 不将相对轮廓中连续的实函数 `Lambda_N` 当作复全纯延拓因子。原分数阶、零分支非亚纯障碍及各 `N=1` 例外没有改变。
- 所有几何、压力及余项常数都依赖固定基底；没有认证具体输入矩阵、数值长度、有限生产器或不同几何族的一致性。
- 已控制 `kappa_N/B_*^N` 趋一并识别其日志的 `-2log N/N^3` 首项修正，尚未识别更细的临界有限部分常数；仍没有全局谱行列式等式、迹公式、固定参数恢复或正式 AN／Route 晋级结论。

[complex-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_complex_critical_crossover_and_tangential_limits_20260908.md
[real-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_exponential_critical_crossover_20260908.md
[shrinking-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_shrinking_critical_layer_and_fractional_singularity_20260908.md
[sharp-source]: https://warwick.ac.uk/fac/sci/maths/people/staff/richard_sharp/p2/gauss.pdf

## 后续追加：有限部分收敛与 theta 精细轮廓（2026-09-08）

后续[扩散尺度 theta 轮廓与临界有限部分](internal_diffusive_theta_profile_and_critical_finite_part_20260908.md)在本笔记已给出的任意精度字符估计中固定取 `p=4`，证明实际 `F_N(u)=N⁴(N²u)e^{-N²u}a_N(N²u)` 趋于 `F_D(u)=Theta_D(u)-c_D/u²`，并用本笔记全局界闭合 `int_0^infinity |F_N-F_D|du/u->0`。由此将本笔记仅有界的有限部分推进为 `N³log(kappa_N/B_*^N)+2log N->C_D`，其中 `C_D=-gamma+int_0¹F_Ddu/u+int_1^infinity(F_D-1)du/u` 是绝对收敛表达，亦等于明确标量二次型级数 `Z_D'(0)`。另外给出整个原右半单位圆盘上的 `N³E_N^+(1+z)-mathcal J_D(N²z)->0` 一致精细轮廓。没有提供 `rho_N` 的具体速率、数值 `D/C_D` 或谱算子结论；原时钟、归一化、冻结对象、论文及正式状态不变。
