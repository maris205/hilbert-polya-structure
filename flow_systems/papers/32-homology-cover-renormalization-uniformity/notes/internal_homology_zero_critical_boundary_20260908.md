# P32 内部研究：零同调临界边界、正分支发散与对数偏移渐近

记录日期：2026-09-08 UTC。接续[未缩时覆盖乘积与移动参数主项][moving-note]。本轮引入适用于固定曲面的已发表同调计数定理，补齐上轮未确定的两分支临界行为，并推导零分支的边界奇性、靠近临界点的移动参数渐近及精确截断尺度。

原来的 `1/N` 时间缩放和 `1/N^3` 对数归一化均保持不变。此处是内部数学推导，不是新实验、规范 owner 枚举、论文修订、Route 评估或正式审查放行。

## 1. 对象及新增外部计数输入

沿用同一个固定、真实、带标记、曲率为负一的闭双曲亏格二曲面，全部本原有向基流 owner 集 `O`、整数同调 `alpha_g in Z^4` 与物理长度 `ell_g>=ell_*>0`。不合并逆向 owner，不因改变起点重复计数。令

\[
\mathcal O_0=\{g:\alpha_g=0\},\qquad
\mathcal O_+=\{g:\alpha_g\ne0\},\qquad
n_0(L)=\#\{g\in\mathcal O_0:\ell_g\le L\}.
\]

上轮已证明全体计数 `n(L)<=C_cnt e^L` 以及对正 owner 的统一界 `d_g<=M ell_g`，其中 `M>0` 依赖固定几何、标记和长度单位。本轮不改变这些常数的定义，也不声称已给出数值认证。

### 1.1 来源入口与口径对应

新增外部输入取自 Dongsheng Liu，*Asymptotic expansion for closed geodesics in homology classes*，Glasgow Mathematical Journal 46 (2004), 283–299，DOI 10.1017/S0017089504001764。[出版社开放全文][liu-source]的 Theorem 2、Eq. (10)（印刷 p.297）给出固定整数同调类的累计闭测地线计数展开，首系数严格为正。其二维条件直接覆盖这里的闭双曲曲面；此处不需要额外调用高维的曲率夹逼分支。

口径对应为：p.284 的单位速度测地流把长度取为最小周期，p.285 使用无挠整数同调，p.298 讨论反向闭测地线。故本项目的本原、有向、整数同调零类与该定理对应。代入第一 Betti 数 `b=4` 和曲率负一时的熵 `h=1`，得到本轮所需输入

\[
\boxed{
n_0(L)=\frac{e^L}{L^3}
\left(c_{\rm hom}+O(L^{-1})\right),
\qquad c_{\rm hom}>0.}
\tag{HC}
\]

Petridis–Risager 的作者版 *Equidistribution of geodesics on homology classes and analogues for free groups*，arXiv v3，p.1 的 prime／有向定义及 p.2 Remark 1.4、Eq. (1.4) 的固定同调类公式，为曲率负一的指数、幂次及计数口径提供交叉核对。[指定作者版][pr-source] 这里不以其零密度结论或更弱的归一化误差替代固定类渐近。

只保留 `c_hom>0`，不需要求出其精确数值。所有渐近常数均对当前固定曲面而言；没有导入跨度量、跨覆盖层的一致余项。下面分析结论是从 (HC) 和上轮已证界自行推得，不是文献直接给出的 P32 产品结论，也不声称文献计数定理由本轮重新证明。

### 1.2 零分支函数与实轴扩展对象

沿用

\[
L_t(w)=\sum_{r\ge1}\frac{e^{-rwt}}r,\qquad
H(w):=\mathscr B_0(w)
=\sum_{g\in\mathcal O_0}L_{\ell_g}(w),\qquad
B_0(w)=e^{H(w)}.
\]

在 `Re(w)>1` 上，这些已是非零全纯产品及其指定归零对数。有限长度截断记为

\[
H_T(w)=\sum_{\substack{g\in\mathcal O_0\\\ell_g\le T}}
L_{\ell_g}(w),\qquad B_{0,T}(w)=e^{H_T(w)}.
\]

实轴上的 `mathcal Q_N^bullet`、`mathcal R_N^bullet` 仍由各自有限乘积的上确界定义，允许取正无穷；分支 `bullet` 为全部、正或零。尤其相对产品必须使用自己的局部比值，不能在两个无限产品都发散时写成 `infinity/infinity`。[既有扩展接口][interface-note]

## 2. 临界值有限，且零分支尾部为代数阶

### 2.1 函数及一阶导数的边界收敛

令

\[
q(t)=e^{-t}n_0(t)
=\frac{c_{\rm hom}}{t^3}+O(t^{-4})\qquad(t\to\infty).
\]

取 `A in (0,ell_*)`，故 `n_0(A)=0`。Stieltjes 分部积分或非负积分恒等式给出

\[
\sum_{g\in\mathcal O_0}e^{-\ell_g}
=\int_A^\infty q(t)\,dt<\infty,
\]

\[
\sum_{g\in\mathcal O_0}\ell_ge^{-\ell_g}
=\int_A^\infty(t-1)q(t)\,dt<\infty.
\]

第二个积分的被积式在小长度处可以变号，不影响分部积分恒等式；可积性由无原子的起始区间和无穷远尾部保证。又有

\[
|L_{\ell_g}(w)|\le
\frac{e^{-\ell_g}}{1-e^{-\ell_*}},\qquad
\left|\frac{d}{dw}L_{\ell_g}(w)\right|
=\left|\frac{-\ell_g}{e^{w\ell_g}-1}\right|
\le\frac{\ell_ge^{-\ell_g}}{1-e^{-\ell_*}}
\quad(\operatorname{Re}w\ge1).
\]

因此 `H` 和其内部导数的级数都在整个闭半平面 `Re(w)>=1` 绝对一致收敛，并连续到达边界。这里的“闭半平面连续”不是“在边界附近全纯”。特别地，

\[
H_*:=H(1)>0,\qquad
D_*:=H'(1)=-\sum_{g\in\mathcal O_0}
\frac{\ell_g}{e^{\ell_g}-1}<0,\qquad
B_*:=B_0(1)=e^{H_*}>1
\]

均为有限实数；`H'(1)` 表示从内部连续到达的导数值。正性也由 (HC) 蕴含的零 owner 非空保证。

若 `0<u<1`，则

\[
\sum_{g\in\mathcal O_0}e^{-u\ell_g}
=u\int_A^\infty e^{(1-u)t}q(t)\,dt=+\infty.
\]

由单重复项下界以及正长度下界，

\[
\boxed{\mathcal B_0(u)<\infty\iff u\ge1\qquad(u>0).}
\]

因而零分支的普通 Euler 级数可绝对收敛到临界竖线；这与完整 owner 级数的边界发散并不矛盾。

### 2.2 严格长度尾及端点原子的处理

长度截断包含 `ell_g=T`，故尾为 `ell_g>T`。对光滑 `f`，使用精确公式

\[
\int_{(T,R]}f(t)\,dn_0(t)
=f(R)n_0(R)-f(T)n_0(T)
-\int_T^R n_0(t)f'(t)\,dt.
\]

这里保留 `-f(T)n_0(T)` 项，不能把阶梯计数函数的渐近当作可以逐点求导的公式。取 `f(t)=e^{-t}`、再取 `f(t)=te^{-t}` 并令 `R` 趋于无穷，分别得到

\[
\sum_{\ell_g>T,\ g\in\mathcal O_0}e^{-\ell_g}
=-q(T)+\int_T^\infty q(t)\,dt
=\frac{c_{\rm hom}}{2T^2}+O(T^{-3}),
\]

\[
\sum_{\ell_g>T,\ g\in\mathcal O_0}\ell_ge^{-\ell_g}
=-Tq(T)+\int_T^\infty(t-1)q(t)\,dt
=\frac{c_{\rm hom}}T+O(T^{-2}).
\]

`r>=2` 的重复项尾指数更小。例如对充分大 `T`，其函数尾至多是常数倍的 `sum_(ell_g>T)e^(-2ell_g)`，再用 `e^(-ell_g)<=e^(-T)` 控制；导数尾同理带上 `ell_g`。因此

\[
\boxed{
\Delta(T):=H(1)-H_T(1)
=\frac{c_{\rm hom}}{2T^2}+O(T^{-3}),}
\]

\[
\boxed{
H_T'(1)-H'(1)
=\frac{c_{\rm hom}}T+O(T^{-2}).}
\]

两式左端均非负。三角不等式与正实点 `w=1` 的同号取值，还给出

\[
\sup_{\operatorname{Re}w\ge1}|H(w)-H_T(w)|=\Delta(T),
\]

\[
\sup_{\operatorname{Re}w\ge1}|H'(w)-H_T'(w)|
=H_T'(1)-H'(1).
\]

这是固定零同调对象的边界尾界，不是完整乘积或正分支在临界点的可求和 majorant。

## 3. 二阶对数奇性及局部延拓障碍

### 3.1 单重复项给出精确首个奇性

分拆

\[
H(w)=F(w)+G(w),\qquad
F(w)=\sum_{g\in\mathcal O_0}e^{-w\ell_g},\qquad
G(w)=\sum_{g\in\mathcal O_0}\sum_{r\ge2}
\frac{e^{-rw\ell_g}}r.
\]

对任意 `a>1/2`，`G` 的绝对总和受常数倍的 `sum_g e^(-2a ell_g)` 控制，后者由上轮全体计数界有限。因此 `G` 在 `Re(w)>1/2` 全纯，其二阶导数在 `w=1` 附近有界。局部求导可以在稍大的紧集上使用绝对一致收敛。

令 `epsilon>0`。对 `F''(1+epsilon)` 作 Stieltjes 分部积分，

\[
F''(1+\varepsilon)
=\int_A^\infty
\bigl[(1+\varepsilon)t^2-2t\bigr]
e^{-\varepsilon t}q(t)\,dt.
\]

因 `t^2q(t)=c_hom/t+O(t^(-2))`，其中的余项可积；同时 `tq(t)` 在无穷远可积。利用

\[
\int_A^\infty\frac{e^{-\varepsilon t}}t\,dt
=\log(1/\varepsilon)+O(1),
\]

得到

\[
\boxed{
H''(1+\varepsilon)
=c_{\rm hom}\log(1/\varepsilon)+O(1)
\qquad(\varepsilon\downarrow0).}
\]

有界余项确实使用了 (HC) 的 `O(L^(-1))` 相对误差；仅有主项等价不能在不补论证时自动写成这里的 `O(1)`。

### 3.2 两次积分与函数展开

二阶对数奇性可积。利用第 2 节已证明的一阶连续边界值，积分得到

\[
H'(1+\varepsilon)
=D_*+c_{\rm hom}\varepsilon\log(1/\varepsilon)
+O(\varepsilon),
\]

\[
\boxed{
H(1+\varepsilon)
=H_*+D_*\varepsilon+
\frac{c_{\rm hom}}2\varepsilon^2\log(1/\varepsilon)
+O(\varepsilon^2).}
\]

例如二次积分中的对数项精确满足

\[
\int_0^\varepsilon(\varepsilon-t)\log(1/t)\,dt
=\frac{\varepsilon^2}2\log(1/\varepsilon)
+\frac{3\varepsilon^2}4.
\]

这里明确是沿 `epsilon>0` 的实轴渐近；没有据此选择全复邻域的对数分支或声称扇形上的统一余项。

### 3.3 有限边界值不等于可延拓

由

\[
B_0''(1+\varepsilon)
=B_0(1+\varepsilon)
\left(H''(1+\varepsilon)+H'(1+\varepsilon)^2\right)
\longrightarrow+\infty
\]

可知，`B_0` 不存在包含 `w=1` 的开邻域上的全纯延拓并与右侧原函数相合。若这样的邻域上存在亚纯延拓，则由于 `B_0(1+epsilon)->B_*` 有限且非零，`w=1` 不可能是极点；它必须是普通全纯点，又与二阶导数发散矛盾。所以

\[
\boxed{B_0\text{ 在 }w=1\text{ 处既无全纯延拓，也无亚纯延拓。}}
\]

此处仅排除经过这个点的局部延拓，不证明整个 `Re(w)=1` 是自然边界，也不排除避开该点的延拓、其他求和对象或另行定义的行列式。

对每个固定 `N>=1`，零分支有 `Q_N^0(s)=B_0(s/N)^N`。其二阶导数在 `s=N` 从右侧同样发散，而函数值有限且非零，故具有同样的局部非亚纯延拓障碍。若 `N>=2`，零分支相对产品在右侧为 `R_N^0(s)=Q_N^0(s)/B_0(s)`；分母在 `s=N>1` 附近全纯且非零，因此障碍也传递给它。`N=1` 的相对产品恒为一，是必须保留的例外。

## 4. 两分支的精确正实有限值区域

表中参数均为实数 `s>0`，表外的相应扩展乘积值均为正无穷。

| 分支 | `mathcal Q_N^bullet(s)` 有限，`N>=1` | `mathcal R_N^bullet(s)` 有限，`N>=2` | `N=1` 的相对乘积 |
| --- | --- | --- | --- |
| 全部 owner | `s>N` | `s>N` | 对全部 `s>0` 恒为一 |
| 正同调 `O_+` | `s>N` | `s>N` | 对全部 `s>0` 恒为一 |
| 零同调 `O_0` | `s>=N` | `s>=N` | 对全部 `s>0` 恒为一 |

完整分支一行由上轮指定外部素测地线定理及项目推导完成。新增的两分支结论证明如下。

### 4.1 零分支的临界有限性与相对产品

零 owner 的 `m_(N,g)=N`，故正实扩展值满足

\[
\mathcal Q_N^0(s)=\mathcal B_0(s/N)^N,
\qquad
\mathcal Q_N^0(s)<\infty\iff s\ge N.
\]

对单个零 owner，设 `t=e^(-s ell_g/N) in (0,1)`。两个单 owner 日志都有限，允许先相减：

\[
\begin{aligned}
\log r_{N,g}^0(s)
&=N\sum_{j\ge1}\frac{t^j}j
-\sum_{j\ge1}\frac{t^{Nj}}j\\
&=N\sum_{\substack{j\ge1\\N\nmid j}}\frac{t^j}j.
\end{aligned}
\]

对 `N>=2`，首项未被消去，因此

\[
Ne^{-s\ell_g/N}
\le\log r_{N,g}^0(s)
\le NL_{\ell_g}(s/N).
\]

求和后，`s<N` 时下界发散，`s>=N` 时上界有限，完全绕开了无限值相除。特别地，

\[
1<\mathcal R_N^0(N)=\frac{B_*^N}{B_0(N)}<\infty
\qquad(N\ge2).
\]

`N=1` 时这个非负展开为空；局部相对因子全部为一。

### 4.2 临界发散必须在正分支中出现

各绝对局部因子均至少为一，故全乘积可以按正、零 owner 分拆为扩展乘积。由

\[
\mathcal Q_N(N)=+\infty,\qquad
\mathcal Q_N^0(N)=B_*^N<\infty
\]

推出 `mathcal Q_N^+(N)=+infinity`。各正分支局部因子随 `s` 非增，所以发散向 `0<s<=N` 传递；`s>N` 时全乘积有限，其正子乘积自然有限。这一论证包括 `N=1`。

若 `N>=2`，基准正子乘积 `B^+(N)` 有限，可以在临界点合法相除，得 `mathcal R_N^+(N)=+infinity`。局部相对因子的非增性由上轮导数式给出，也可在上述非负展开中将 `N` 换成固定整数 `m_(N,g)` 直接看出，故相对发散同样向左传递。`N=1` 时全部 `m_(1,g)=1`，仍须用恒等于一的例外。

取 `N=1`，基准正、零分支的有限值区域也随之确定：

\[
\mathcal B^+(s)<\infty\iff s>1,\qquad
\mathcal B_0(s)<\infty\iff s\ge1.
\]

这些正实陈述不把任何发散级数赋成有限值。第 3 节的局部非延拓证明只针对零分支，不据此判定完整或正分支是否具有其他意义下的亚纯延拓。

## 5. 正分支的层数极限与临界极限不交换

对实数 `w>1` 定义

\[
F_N(w):=Q_N^+(Nw)
=\frac{Q_N(Nw)}{B_0(w)^N}.
\]

上轮的正分支指数误差证明，对于每个固定 `w>1`，

\[
\lim_{N\to\infty}F_N(w)=1.
\]

另一方面，对每个固定 `N`，正 owner 对数项随 `w downarrow 1` 单调增加；由单调收敛及第 4 节的临界发散，

\[
\lim_{w\downarrow1}F_N(w)=+\infty.
\]

因此在扩展正实意义下，

\[
\boxed{
\lim_{w\downarrow1}\lim_{N\to\infty}F_N(w)=1,
\qquad
\lim_{N\to\infty}\lim_{w\downarrow1}F_N(w)=+\infty.}
\]

这说明对任意固定 `delta>0`，`F_N->1` 都不可能在整个 `(1,1+delta]` 上一致。这里有真实的边界发散依据，不只是原误差界在 `a downarrow 1` 时变差。

同样，不能把上轮有限字符／Haar 日志平均中的绝对换和论证直接搬到 `w=1`：完整 owner 的绝对支配级数在那里发散。本轮只建立零同调函数的边界收敛，没有另证临界字符积分的合法性。

## 6. 距临界点对数级距离的移动参数渐近

虽然第 5 节禁止无条件的一致到边界，但可以在明确的对角线上继续控制完整乘积。沿全部整数 `N>=2`，固定实数 `K>2M` 并设

\[
s_N=N+K\log N,\qquad
a_N=w_N=s_N/N=1+\frac{K\log N}N,\qquad
b_N=1+\frac{2M}N.
\]

充分大 `N` 时有 `1<b_N<a_N`。上轮对任意 `1<b<a` 的界为

\[
|E_N^+(w)|\le
\frac{MbC_{\rm cnt}}{c_a(b-1)^2}
\exp\!\left[-\frac{a-b}{M}N\right],
\quad\operatorname{Re}w\ge a,\qquad
c_a=1-e^{-a\ell_*}.
\]

逐层代入 `a_N,b_N`，无须假定它们固定，得到精确上界

\[
0\le E_N^+(w_N)\le
\frac{e^2b_NC_{\rm cnt}}{4Mc_{a_N}}
N^{\,2-K/M}
=O(N^{\,2-K/M})\longrightarrow0.
\]

此处 `c_(a_N)>=c_1>0` 且 `b_N` 有界。`K>2M` 是这项估计的充分条件，不声称必要或最优；不能把端点 `K=2M` 包含进趋零结论。

令 `epsilon_N=K log N/N`。第 3 节给出

\[
NH(1+\varepsilon_N)
=NH_*+KD_*\log N+
O\!\left(\frac{(\log N)^3}{N}\right).
\]

由上轮的精确分拆 `mathscr L_N(Nw)=NH(w)+E_N^+(w)`，

\[
\boxed{
\mathscr L_N(s_N)
=NH_*+KD_*\log N+
O\!\left(N^{\,2-K/M}+\frac{(\log N)^3}{N}\right).}
\]

同时，全基准日志满足 `mathscr B(s_N)=O(e^(-cN))`，某个固定 `c>0` 即可：对充分大 `N` 用 `S_0(2)<infinity` 与统一正长度下界，界住 `sum_g e^(-s_N ell_g)`。因此相对产品的指定日志 `mathscr L_N(s_N)-mathscr B(s_N)` 具有相同展开。指数化得到

\[
\boxed{
Q_N(s_N)
=B_*^N N^{KD_*}
\left[1+
O\!\left(N^{\,2-K/M}+\frac{(\log N)^3}{N}\right)\right],}
\]

\[
\boxed{
R_N(s_N)
=B_*^N N^{KD_*}
\left[1+
O\!\left(N^{\,2-K/M}+\frac{(\log N)^3}{N}\right)\right].}
\]

由于 `B_*>1`、`D_*<0`，它是指数增长主项乘以幂次衰减修正，整体仍趋于正无穷。这是原归一化产品的渐近，不是辅助覆盖度数归一化；移动的参数始终处于该层已证收敛域 `s_N>N`。它不恢复固定 `s` 的有限值极限，也不把这条对角线写入冻结实验输入。

## 7. 纯零分支临界截断的精确尺度

对任意实数长度序列 `T_N>=0`、`T_N->infinity`，在临界点 `s=N` 只比较零分支：

\[
Z_N(T_N)
:=\frac{Q_{N,E_0(T_N)}(N)}{\mathcal Q_N^0(N)}
=\left(\frac{B_{0,T_N}(1)}{B_*}\right)^N
=\exp[-N\Delta(T_N)].
\]

由第 2 节，

\[
N\Delta(T_N)
=\frac{c_{\rm hom}}2\frac{N}{T_N^2}
\left(1+O(T_N^{-1})\right).
\]

若 `N/T_N^2->lambda in [0,infinity]`，则

\[
\boxed{
Z_N(T_N)\longrightarrow
\exp(-c_{\rm hom}\lambda/2),}
\]

其中 `lambda=infinity` 时右侧解释为零。尤其不必假定比值已有极限，就能得到必要且充分的相对精度条件

\[
\boxed{
Z_N(T_N)\longrightarrow1
\iff\frac{T_N}{\sqrt N}\longrightarrow+\infty.}
\]

理由是 `Delta(T)~c_hom/(2T^2)>0`，而 `exp(-N Delta)->1` 当且仅当 `N Delta->0`。例如 `T_N/sqrt(N)->rho in (0,infinity)` 时，截断相对值趋于 `exp[-c_hom/(2rho^2)]`，严格介于零与一之间。

每层日志再除以 `N` 的误差则仅为 `Delta(T_N)`，任何 `T_N->infinity` 都使其趋零。故归一化日志精度仍不能替代乘积的相对精度。

本节不对临界点已为无穷的完整乘积 `mathcal Q_N(N)` 定义相对误差，也不声称 `sqrt(N)` 是其完整 owner 截断尺度。它仅针对已证明有限的纯零分支临界对象。与上轮固定 `a>1` 的指数尾界相比，此处处于 `a=1`，代数尾和不同尺度不构成冲突。所有长度集合仍是数学截断，未执行规范 producer、`m_k=2^k` 或冻结 panel。

## 8. 完成范围、来源使用与保全

本轮按 ARS 论证流程把外部同调计数输入、项目推论、边界反例及误差适用域分开。主线程推导并整合；同系助手分别检错来源口径、临界分析及分支／极限关系。这是同系逻辑复核，不是独立科学证据，也不是重新启动正式审查。

主线程通过普通浏览核对 Liu 出版社开放 PDF 的定理、定义及指定页面的解析文本，并核对 Petridis–Risager 作者 arXiv v3 的相关定义、固定类公式与曲率约定。没有声称逐页通读两篇证明、复证文献定理、获得人类已读确认、完成本地 PDF 结构认证，或认证作者版与最终刊本的逐字一致。未依赖其他扫描来源的低质量数学 OCR；未重试此前 Utah 403 路径，未上传私人材料。

本轮只新增此笔记，在前轮移动参数笔记、无限接口笔记及总内部记录各追加入口。保全核对针对三个旧文件的原文前缀和十二个指定保护文件的原始长度／SHA-256；文档检查另涵盖本地链接、数学环境配对、控制字符及范围标记。检查只验证所列文档条件，不把通过情况当作数学真实性或来源充分性的证书。工作目录不是 Git 仓库；本轮只读 `git status --short` 再次返回该既有环境事实，未据此尝试初始化或修改版本管理。

首次提交最后的只读文档检查编排时，检查代码中的反引号与外层 JavaScript 模板冲突，调用在执行前返回 SyntaxError；该次未运行检查，也未执行同批拟议的追加措辞调整。改用字符码表示后重新提交，保留这次失败记录，不将它误写为已通过的检查。

未运行科学实验、owner 枚举、矩阵／长度计算程序、旧 artifact writer、论文构建或正式审查脚本；未修改论文、代码、结果、输入锁、正式回执及历史失败记录。原 AN-1–AN-5 合同的指定域、索引与任务仍不能由这里的不同对象自动完成。正式 `FAIL / BLOCK`、Route 状态和 Stage 5／6 均不变。

仍开放的方向包括：靠近边界的更窄移动参数尺度、正分支临界附近的定量发散律、其他边界点的延拓问题，以及数学长度集合与实际规范枚举的认证接口。它们在此仅列作后续研究问题，不登记为已取得结论或已获执行授权。

[moving-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_unscaled_cover_products_and_moving_parameter_limit_20260908.md
[interface-note]: /root/autodl-tmp/flow_systems/papers/32-homology-cover-renormalization-uniformity/notes/internal_scalar_infinite_product_interfaces_20260908.md
[liu-source]: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/47B4C2A0B6E4A26C32224CD8ED01D363/S0017089504001764a.pdf/asymptotic-expansion-for-closed-geodesics-in-homology-classes.pdf#page=15
[pr-source]: https://arxiv.org/pdf/math/0509513v3#page=2

## 追加进展：收缩临界层与固定层分数阶（2026-09-08）

后续[收缩临界层、最大重数分支与分数阶奇性](internal_shrinking_critical_layer_and_fractional_singularity_20260908.md)通过重数整除分拆，把正分支边界困难定位到非零整数同调落在 `NZ^4` 的单重复项；再导入 Sharp 对全部同调类一致的局部极限定理，保留 Gaussian 加法余项，证明固定 `u>0` 时原 `Q_N(Nw)`、`R_N(Nw)` 在 `Re(w)>=1+uN^(-3/2)` 上均以 `B_0(w)^N` 为一致相对主项。因此 `s=N+u/sqrt N` 已有 `Q_N,R_N~B_0(1)^N`，旧对数偏移结论扩展到每个固定 `K>0`。另从固定覆盖曲面的 PGT 指数余项证明临界发散阶为 `epsilon^(-1/N^3)`，据此排除 `N>=2` 的完整及正分支原乘积／相对乘积在临界点的局部亚纯延拓；`N=1` 完整乘积为简单极点，但正分支由商论证仍不能亚纯延拓，相对分支仍恒为一。收缩充分尺度不声称最优，固定层常数不当作随层一致，未改归一化、冻结输入、论文或正式状态。

## 追加进展：闭右半圆的复对数展开与原参数相位（2026-09-08）

后续[复临界过渡、零分支相位与切向限制](internal_complex_critical_crossover_and_tangential_limits_20260908.md)用本笔记的 `HC` 和一阶连续性，将实展开扩展为 `H(1+z)=H_*+D_*z-(c_hom/2)z^2 Log z+O(|z|^2)`，在小闭右半圆上对角度一致。对 `Nz_N->xi`，由此得到 `B_0(1+z_N)^N/B_0(1)^N->exp(D_*xi)`。再结合另行证明的正分支复控制，对固定 `a>=0`、`theta≠0`，原 `s_N=N+N^(-1)exp(-aN^3)+i theta` 的 `Q_N`、`R_N` 除以 `B_0(1)^N` 均趋于 `exp(i D_*theta)`；对 `a>0`，虚偏移趋零与层数趋无穷不交换。闭半平面展开不等于跨点全纯延拓，也不清除既有二阶奇性、固定层例外或正式停止条件。
