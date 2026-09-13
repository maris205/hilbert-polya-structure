# 实循环芽 probe：反射曲线条件的自动性

日期：2026-09-07。本轮仅选择两个局部反射对应的实解析曲线机制。
已完整读取本轮 `proof-writer` 技能；下面直接用明确共轭公式证明，
不借用未核查的 Schwarz／Grunsky 不等式。
旧反函数和循环芽等价证明不重开，本稿只检验新增实结构是否真的筛选参数根。

## Claim and status

对实际传播子及实参数 $a=-4\lambda$，检查
$\mathcal F^\#=\mathcal F^{-1}$ 能否提供超出既有正频递推的根约束。
其中 $\mathcal F^\#(y)=\overline{\mathcal F(\bar y)}$ 是系数共轭。

本稿的自动实结构、反射曲线及局部模长导数结论：`PROVABLE AS STATED`。
它们对**每个实参数**均成立，不依赖 $R_s(a)=0$。
因此这套实结构本身不能证明原全分母实根或简单性；原命题仍
`NOT CURRENTLY JUSTIFIED`。

## Assumptions and notation

固定互素 $0<r<s$、$s\ge3$，令
$\zeta=e^{2\pi ir/s}$、$D_n=4\sin^2(\pi rn/s)$。
用已规范化的正支截断

$$
v(t,a)=\sum_{n=1}^{s-1}v_n(a)t^n,
\qquad v_n=\frac{[t^{n-1}]e^v+a[t^{n-2}]e^{2v}}{D_n},
$$

定义 $Y_a(t)=t e^{v(t,a)}$、$T_a=Y_a^{-1}$、
$\mathcal F_a=Y_a\circ(\zeta\,\cdot)\circ T_a$。
本稿 $t=-\epsilon e^{i\theta}/2$，$a=-4\lambda$，不混用物理未缩放变量。

采用上轮已经证明的首项缺陷式

$$
\log\frac{\mathcal F_a(y)\mathcal F_a^{-1}(y)}{y^2}
=-y-ay^2+R_s(a)y^s+O(y^{s+1}).\tag{1}
$$

$\mathcal F^{-1}$ 是复合逆，分子是两个值的普通乘积。
局部对数针对常数项为 $1$ 的解析单位，因此无分支选择问题。

## Proof strategy and dependency map

1. 实参数使递推的全部系数实，直接得到实解析共轭。
2. 把系数共轭写为反全纯映射 $\kappa(y)=\bar y$，明确算出第二条反射曲线。
3. 在实轴上把式 (1)转成真实正模长的对数，再核查参数导数的符号究竟
   来自哪一阶，而不是把它当成共振系数的横截性。

## Proof

### Step 1. 实结构对每个实参数自动成立

递推的分母为实非零数，故各 $v_n(a)$ 是实系数参数多项式。
当 $a\in\mathbb R$ 时，$Y_a^\#=Y_a$，其局部反函数亦满足
$T_a^\#=T_a$。由 $\bar\zeta=\zeta^{-1}$，直接得到

$$
\mathcal F_a^\#
=Y_a\circ(\zeta^{-1}\,\cdot)\circ T_a
=\mathcal F_a^{-1}.\tag{2}
$$

同时 $\mathcal F_a^{\circ s}=\operatorname{id}$。这些都是完整局部芽身份，
不是只有在某个根上成立的有限阶条件。

例如 $a=0$ 时正递推逐阶给出 $v_n(0)>0$，所以
$R_s(0)=[t^{s-1}]e^{v(t,0)}>0$，首项并未消失；式 (2)仍然成立。
因此它不是 $R_s=0$ 的充分条件，也没有在实参数线上删去任何候选参数。

对复参数，精确关系是
$\mathcal F_a^\#=\mathcal F_{\bar a}^{-1}$。
如果另外强加 $\mathcal F_a^\#=\mathcal F_a^{-1}$，式 (1)在实轴上的
左边成为实系数的 $\log|\mathcal F_a(x)/x|^2$；其二阶系数是 $-a$，
所以已经强迫 $a\in\mathbb R$。反向由上面证明成立。
这也说明：若想用实结构排除非实参数根，仍须另证
$R_s(a)=0\Rightarrow\mathcal F_a^\#=\mathcal F_a^{-1}$；不能先把该
实结构作为复参数根的现有性质，否则等于预设参数为实。

### Step 2. 明确的两条反射曲线

设 $\omega=2\pi r/s$，$\kappa(y)=\bar y$，并定义
$\rho_a=\mathcal F_a\circ\kappa$。
由式 (2)，$\rho_a^{\circ2}=\operatorname{id}$。因为 $Y_a,T_a$ 为实型，

$$
\rho_a=Y_a\circ(\zeta\kappa)\circ T_a.
$$

它的固定点恰是

$$
\Gamma_a=Y_a(e^{i\omega/2}\mathbb R)
$$

在原点附近的部分：方程 $t=\zeta\bar t$ 等价于
$t\in e^{i\omega/2}\mathbb R$。另一反射 $\kappa$ 的固定曲线是实轴。
$Y_a'(0)=1$，所以两曲线的夹角为 $\omega/2$（按直线角模 $\pi$），
而 $\mathcal F_a=\rho_a\circ\kappa$。

此构造对每个实 $a$ 都给出真正实解析局部曲线。局部反函数／单叶性由
$Y_a'(0)=1$ 得到，邻域可以依赖参数；没有给出固定大域的单叶性、面积
或边界几何假设，因此不能在这里无条件借用全局系数不等式。

### Step 3. 一个严格但不筛根的局部单调性

对实 $a,x$，把 $\mathcal F_a(x)/x$ 在 $x=0$ 处补定义为 $\zeta$，令

$$
\mu_a(x)=\log\left|\frac{\mathcal F_a(x)}{x}\right|^2.
$$

它在原点附近是实解析函数，式 (1)、(2)给出

$$
\mu_a(x)=-x-ax^2+R_s(a)x^s+O(x^{s+1}),
$$

以及

$$
\partial_a\mu_a(x)=-x^2+R_s'(a)x^s+O(x^{s+1}).\tag{3}
$$

对任意固定紧实参数集 $K$，解析反函数可在一个共同小邻域中选择；
系数及余项的一阶参数导数在更小邻域上一致有界。
因此存在 $\delta_K>0$，使

$$
\partial_a\mu_a(x)\le-\frac12x^2<0
\quad(a\in K,\ 0<|x|<\delta_K).\tag{4}
$$

具体地，将式 (3)除以 $x^2$，剩余两项一致为 $O(x^{s-2})$，
而 $s\ge3$；缩小邻域使其绝对值不超过 $1/2$ 即得。

式 (4)并不是 $R_s'(a)$ 的符号或非零性结论。它的严格负号来自所有参数
共有的低阶项 $-x^2$，即使共振系数导数为零，证明也没有任何变化。
真正筛选参数根的是扣去这些固定低阶项后的射流

$$
[x^s](\mu_a+x+ax^2)=R_s(a),
\qquad
[x^s](\partial_a\mu_a+x^2)=R_s'(a).
$$

反射曲线自动性和式 (4)均未给这两个高阶系数额外约束。∎

## Corrections or missing assumptions

未得到从反射曲线导出的新根实性／横截性判据。
必要的新内容只能是对扣去固定低阶项之后的共振射流的独立约束，不能用
自动实型、局部反函数存在或未扣除低阶项的模长单调性替代。

## Scope record and handoff

收到主控的新优先级前，曾执行并立即披露一次三分母纯正第二障碍的精确
代数计算；随后停止该分支，没有扩展分母或将结果列为本稿结论。
本稿不增加第二障碍作者任务，接续转向已有明确突破的素分母平方自由包
非作者核查。没有新根扫描、旧文件修改、论文／容量票或批次完成数变化。
