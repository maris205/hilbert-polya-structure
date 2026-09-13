# Paper30 T 分支：固定目标支撑的全形式问题与单向支撑等价归约

日期：2026-09-06。性质：新的一次有界作者理论探索，不是旧结果复审、正式候选或论文扩写。
本报告只新增本文件；两份既有 T 分支报告冻结。

## Claim

固定
$$
A=\begin{pmatrix}2&1\\1&1\end{pmatrix},\qquad
S_\kappa(q,p)=(q,p+\kappa\sin(2\pi q)),\qquad F_\kappa=A\circ S_\kappa.
$$
令 $\mathcal T$ 为复系数有限三角多项式空间，并令
$$
\mathcal B=\{f(q)-f(q-p):f\text{ 为一元有限三角多项式}\}.
$$
原形式问题保持为：对任意预先固定的有限 Fourier 支撑空间 $V\subset\mathcal T$，
若
$$
g_t\in V[[t]],\qquad h_t\in\mathcal T[[t]],\qquad
g_t=(F_{t/\pi}^*-1)h_t,
\tag{F}
$$
是否必有 $g_t\in\mathcal B[[t]]$？
$h_t$ 的每阶系数有限，但原假设没有限制各阶支撑的并集。

本次证明一个对任意固定 $V$ 都成立的条件引理及等价归约：
在满足 (F) 的同一个解上，原函数的任一新坐标频率投影有限、
原函数总支撑有限、目标属于 $\mathcal B[[t]]$，三类性质彼此等价。
这不证明原假设自动给出其中任何一项。

## Status

- 形式主命题 (F)：`NOT CURRENTLY JUSTIFIED`；科学状态仍为 `OPEN`。
- 下文命题 3 的条件引理与等价归约：`PROVABLE AS STATED`。
- 下文的全形式拉回例子：严格说明去掉固定目标支撑后会发生尾部消去，
  但不满足 (F) 的固定目标支撑假设，因而不是原主命题的反例。
- 没有得到任意固定 $V$ 的全阶刚性证明，也没有得到严格全形式反例。

等价归约没有增加原问题的假设。只有在使用其充分方向时，
才需要另行证明单向支撑有限；这一缺失义务在本报告末尾明列，不能当作已知。

## Assumptions

- $t$ 是形式不定元；$t=\pi\kappa$ 的非零常数重标不改变固定支撑问题。
- $V$ 由一个固定有限整数频率集张成；其大小任意，但所有阶次使用同一个集。
- $h_t$ 的每阶系数属于 $\mathcal T$，不假设级数收敛，不作非零参数代入。
- 所有级数、分组、导数和拉回均按 $t$ 阶次解释。
- 原问题没有原函数的统一支撑界、单向支撑界或 Fourier 衰减假设。

## Notation

采用整数可逆坐标变换
$$
u=e^{2\pi i(q-p)},\qquad v=e^{2\pi iq},\qquad
\phi(z)=z-z^{-1}.
$$
单项式 $u^a v^b$ 对应原频率 $(a+b,-a)$；该对应在 $\mathbb Z^2$ 上双射。
因而 $\mathcal T$ 可以与 $\mathbb C[u^{\pm1},v^{\pm1}]$ 等同。
写
$$
\mathscr R=\mathbb C[u^{\pm1},v^{\pm1}][[t]],\qquad
\mathscr R_{\mathrm{bd}}=\mathbb C[[t]][u^{\pm1},v^{\pm1}].
\tag{1}
$$
$\mathscr R$ 只要求每阶支撑有限；其子环 $\mathscr R_{\mathrm{bd}}$ 要求总支撑有限。
下标仅标记统一有限支撑，不表示系数大小的估计。

对 $h\in\mathscr R$，定义总支撑与两个频率投影
$$
\begin{aligned}
\operatorname{Supp}(h)&=\{(a,b)\in\mathbb Z^2:[u^a v^b]h\neq0
\text{ 作为 }\mathbb C[[t]]\text{ 中的级数}\},\\
P_u(h)&=\{a:\exists b,\ (a,b)\in\operatorname{Supp}(h)\},\\
P_v(h)&=\{b:\exists a,\ (a,b)\in\operatorname{Supp}(h)\}.
\end{aligned}
\tag{2}
$$
零级数的这些集合均为空集。每阶有限并不保证 (2) 中任何一个集合有限。
记 $\sigma_t=F_{t/\pi}^*$、$\delta_t=\sigma_t-1$；后文略去 $g,h$ 的下标 $t$。
在新坐标下
$$
\mathcal B=\{f(v)-f(u):f\in\mathbb C[z^{\pm1}]\}.
\tag{3}
$$

## Proof Strategy

新坐标使一个输入频率投影变成拉回的另一个输出投影，且不同分组不会互相抵消。
先利用这一精确性质把任一投影界升级为总支撑界；
再用形式 Laurent 多项式的导数次数矛盾排除全部非零横向分组。
最后用形式原函数模常数唯一性证明反向，从而得到真正的等价关系。

## Dependency Map

1. 精确投影恒等式只依赖拉回公式、每阶有限支撑和形式指数为单位元。
2. 单向支撑等价依赖固定目标支撑及上述投影恒等式。
3. 总支撑下的分类依赖一个在 $\mathbb C((t))$ 上的 Laurent 次数引理；
   不依赖非零实参数处的解析增长。
4. 从 $g\in\mathcal B[[t]]$ 反推原函数总支撑有限，依赖固定目标支撑和形式核为常数。
5. 原主命题仍缺少从固定目标支撑推出任一原函数投影有限的论证。

## Proof

### Step 1. 全形式拉回与精确投影恒等式

由 $(q-p)\circ F_\kappa=q$ 及 $t=\pi\kappa$，直接得到
$$
\sigma_tu=v,\qquad
\sigma_tv=u^{-1}v^3\exp\!\bigl(t\phi(v)\bigr).
\tag{4}
$$
因此
$$
\sigma_t(u^a v^b)=u^{-b}v^{a+3b}\exp\!\bigl(tb\phi(v)\bigr).
\tag{5}
$$
每个 $t^N$ 系数仅涉及输入的前 $N+1$ 阶有限多项式和有限项指数展开，
所以 (5) 在整个 $\mathscr R$ 上定义良好。

按 $v$ 次数分组，写
$$
h=\sum_{b\in\mathbb Z}v^b H_b(u,t),\qquad
\sigma_th=\sum_{b\in\mathbb Z}u^{-b}v^{3b}
\exp\!\bigl(tb\phi(v)\bigr)H_b(v,t).
\tag{6}
$$
这里 $H_b\in\mathbb C[u^{\pm1}][[t]]$；对每个固定阶次，只有有限个 $b$ 有贡献。
因此 (6) 是逐阶局部有限的恒等式，而不是无条件交换无穷求和。

**引理 1。** 对所有 $h\in\mathscr R$，有精确集合等式
$$
P_u(\sigma_th)=-P_v(h),\qquad -D:=\{-d:d\in D\}.
\tag{7}
$$

固定 $b$ 后，(6) 中的整个系数乘上了单位元
$v^{3b}\exp(tb\phi(v))$，故该组非零当且仅当 $H_b\neq0$。
不同 $b$ 对应不同的 $u$ 指数 $-b$，不会跨组抵消。
这恰好证明 (7)。$\square$

若 $\sigma_th=h+g$ 且 $g$ 总支撑有限，由 (7) 得到
$$
-P_v(h)=P_u(\sigma_th)\subseteq P_u(h)\cup P_u(g).
\tag{8}
$$
所以 $P_u(h)$ 有限会迫使 $P_v(h)$ 有限。
反之，若 $P_v(h)$ 有限，则由 (7) 可知 $P_u(\sigma_th)$ 有限；
等式 $h=\sigma_th-g$ 给出
$$
P_u(h)\subseteq -P_v(h)\cup P_u(g),
\tag{9}
$$
故 $P_u(h)$ 也有限。两个投影都有限时，总支撑包含于它们的有限 Cartesian 积。
于是，在固定目标支撑假设下，任一投影有限等价于 $h\in\mathscr R_{\mathrm{bd}}$。

### Step 2. 统一支撑时的形式指数排除

**引理 2。** 若 $b\in\mathbb Z\setminus\{0\}$ 且
$P,Q\in\mathbb C[[t]][z^{\pm1}]$ 满足
$$
Q=P\exp\!\bigl(tb(z-z^{-1})\bigr)
\quad\text{在 }\mathbb C[z^{\pm1}][[t]]\text{ 中成立},
\tag{10}
$$
则 $P=Q=0$。

若 $P\neq0$，形式指数为单位元保证 $Q\neq0$。
按 $z$ 逐阶求导并消去指数，得到
$$
PQ'-QP'=tb(1+z^{-2})PQ.
\tag{11}
$$
(11) 的两边均为统一有限支撑的 Laurent 多项式，
故可在域 $K=\mathbb C((t))$ 上比较 Laurent 最高次数。
令 $d_P,d_Q\in\mathbb Z$ 分别为非零多项式 $P,Q$ 的最高次数。
左侧若非零，其最高次数不超过 $d_P+d_Q-1$；左侧也可能为零。
右侧非零且最高次数恰为 $d_P+d_Q$，因为 $tb\neq0$ 在 $K$ 中成立，
并且 $1+z^{-2}$ 的最高次数为零。这两种左侧情形均与 (11) 矛盾。
因此 $P=0$，再由 (10) 得 $Q=0$。$\square$

现在设 $h\in\mathscr R_{\mathrm{bd}}$ 且 $g=\delta_th$ 总支撑有限。
则 $\sigma_th=h+g\in\mathscr R_{\mathrm{bd}}$。
在 (6) 中，每个 $H_b(v,t)$ 均属于 $\mathbb C[[t]][v^{\pm1}]$，
而 $[u^{-b}]\sigma_th$ 也属于同一有限 Laurent 环。
取
$$
P=H_b(v,t),\qquad Q=v^{-3b}[u^{-b}]\sigma_th.
$$
它们满足 (10)。引理 2 因此迫使所有 $b\neq0$ 的 $H_b$ 为零。
所以存在 $f\in\mathbb C[[t]][z^{\pm1}]$，使
$$
h=f(u,t),\qquad g=f(v,t)-f(u,t)\in\mathcal B[[t]].
\tag{12}
$$
该证明没有把形式 $t$ 代入非零值；使用 $\mathbb C((t))$ 只为比较已具有有限支撑的系数。

### Step 3. 反向与完整等价关系

先记录形式核。在线性参数 $t=0$，$\ker(\delta_0|_{\mathcal T})=\mathbb C$：
$A$ 的特征值为 $(3\pm\sqrt5)/2$，故非零整数频率的 $A$ 轨道全部无限；
有限支撑的不变系数沿每条轨道恒定，只能为零。
这也是冻结形式尾部报告中已证明的核结论。

若 $\delta_tw=0$，其零阶系数必须为常数。
依次减去已经确定的低阶常数项；在第 $n$ 阶，因拉回严格固定常数，
方程只剩 $\delta_0w_n=0$，所以 $w_n$ 仍为常数。
逐阶归纳得到
$$
\ker(\delta_t|_{\mathscr R})=\mathbb C[[t]].
\tag{13}
$$

现设 $g\in V[[t]]\cap\mathcal B[[t]]$。
每个 $g_n$ 可唯一写为 $f_n(v)-f_n(u)$，其中 $f_n\in\mathbb C[z^{\pm1}]$
且常数项取零。令 $S\subset\mathbb Z^2$ 为 $V$ 在新坐标中的固定有限支撑集。
若 $f_n$ 的非零 $k$ 次系数不为零，则 $g_n$ 的频率 $(0,k)$ 与 $(k,0)$
分别出现该系数及其负数。这两个格点在 $k\neq0$ 时不同，也不与其他指数项重合。
于是所有 $f_n$ 的非零次数均属于固定有限集
$$
D_S=\{k\in\mathbb Z\setminus\{0\}:(0,k)\in S\text{ 且 }(k,0)\in S\}.
\tag{14}
$$
因此 $f=\sum_{n\geq0}t^nf_n\in\mathbb C[[t]][z^{\pm1}]$。
由 (4)，$\delta_tf(u,t)=g$；任何给定原函数 $h$ 都满足
$\delta_t(h-f(u,t))=0$。式 (13) 给出
$$
h=f(u,t)+c(t),\qquad c(t)\in\mathbb C[[t]],
\tag{15}
$$
从而 $h$ 具有统一有限支撑。

**命题 3（任意固定支撑的条件引理与等价归约）。**
对任意固定有限 Fourier 空间 $V$，以及满足 (F) 的任意一对 $(g,h)$，下列四项等价：

1. $P_u(h)$ 有限。
2. $P_v(h)$ 有限。
3. $h\in\mathscr R_{\mathrm{bd}}$。
4. $g\in\mathcal B[[t]]$。

这些条件成立时，$h$ 事实上只依赖 $u$ 和 $t$，并具有统一有限的一元支撑。
Step 1 证明前三项等价，Step 2 证明第三项蕴含第四项，
(13)—(15) 证明第四项蕴含第三项，故全部结论成立。$\square$

对于 $g=0$，(13) 已经给出 $h=c(t)$，包含在上述结论中。
若 $g$ 只含空间常数，则逐阶方程中的零频率系数先迫使 $g_n=0$，
再由 $\ker\delta_0=\mathbb C$ 迫使 $h_n$ 为常数；从零阶归纳可得 $g=0$。
这里用到低阶原函数均为常数后，其高阶拉回修正为零。
本报告不通过预先删除常数来改变 $V$。

### Step 4. 形式尾部确能消去，但当前例子不满足固定目标支撑

固定任意 $b\in\mathbb Z\setminus\{0\}$，定义一个严格全形式原函数
$$
h_b=v^b\exp\!\bigl(-tb\phi(u)\bigr)\in\mathscr R.
\tag{16}
$$
由 (4) 逐阶复合，精确得到
$$
\sigma_th_b=u^{-b}v^{3b},\qquad
\delta_th_b=u^{-b}v^{3b}-v^b\exp\!\bigl(-tb\phi(u)\bigr).
\tag{17}
$$
$h_b$ 在每阶都是有限 Laurent 多项式，但没有统一支撑界，
而其拉回恰好是单项式。因此，“形式原函数的拉回有统一有限支撑”
本身不能推出“原函数有统一有限支撑”。

不过 (17) 的目标并不属于任何固定有限 Fourier 空间的形式级数环。
对每个 $n\geq1$，其 $t^n$ 系数中 $u^n v^b$ 的系数为
$-(-b)^n/n!\neq0$，故目标的总支撑无限。
此例只有 $P_v(h_b)=\{b\}$ 有限；它不与命题 3 冲突，
因为命题所需的固定目标支撑在这里失败。

该例仅定位直接套用有限 Laurent 拉回分类的边界，
不是 (F) 的反例，也没有借助目标支撑逐阶扩大来宣称解决 (F)。

## Corrections or Missing Assumptions

原主问题精确等价于补上以下缺失论证：
$$
\boxed{\quad
g\in V[[t]],\ h\in\mathscr R,\ \delta_th=g
\quad\Longrightarrow\quad P_u(h)\text{ 有限}.
\quad}
\tag{18}
$$
也可以把右侧换成 $P_v(h)$ 有限；命题 3 保证这两种表述等价。
这是一项仍待证明的结论，不是新加入的原假设。

式 (8)、(9) 只使两个投影的有限性相互传递，
没有给出任一投影必须有限的起点。若真的存在 (F) 的反例，
则它的原函数在这两个投影上都必须有无限总支撑；
“两个投影都无限”只是必要条件，不是反例构造，
也没有声称两个投影必须向正负两端都逃逸，或在相同阶次逃逸。

本次未排除这种双投影无限的形式解，也未构造其中任何一例。
不能将命题 3 的等价归约叙述为已经完成了全局刚性。

## Open Risks

- 无统一支撑界时，(6) 中的 $H_b$ 一般只是每阶有限的形式 Laurent 级数；
  Step 2 的最高次数论证不能直接应用于它。
- 仅有某一侧次数有界、某一阶次数有界、或有限多阶成立，都不等于命题 3 的投影有限。
- 本报告没有把形式原函数与固定非零实参数处的原函数、真实周期条件或级数收敛等同。
- 不使用旧报告的三阶常量族失败去排除允许任意高阶 $g_n\in V$ 的一般目标。
- 本报告没有新增文献查新，不声称全球新颖性；条件引理的证明与研究贡献评估分离。

## 冻结输入与有界处置

已完整读取 `proof-writer/SKILL.md` 与下列两份冻结输入；使用证明技能使原命题、
条件引理、例子边界和缺失义务分别标明，没有隐式加强原假设：

- `PAPER30_TORUS_FOURIER_FIRST_PROBE_20260906.md`，275 行，SHA-256：
  `cc81f9015c60ce4ab0810fcb911bae6899c99cbdc0764fe80d1e000df88e4230`。
- `PAPER30_TORUS_FORMAL_TAIL_OBSTRUCTION_PROBE_20260906.md`，281 行，SHA-256：
  `da8f89945a4e81dc8d44a9935123f8737e3f4ff623bd8e6ca830e8c2e81ef1c7`。

本轮实际新增的是任意固定目标支撑下的条件引理、等价归约及一个适用边界例子。
七维周期检验及三阶常量族失败未重做；未增加小支撑表、逐阶试验、数值实验或新框架。
全局主问题仍 `OPEN`，按有界作者结果停止。
不创建正式项目，不触发 Route 评价、候选容量估计或论文计数，所有旧文件保持不变。
