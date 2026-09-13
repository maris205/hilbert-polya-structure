# Paper30：全部次数及全部首一系数的三点商空间能量界

日期：2026-09-06。性质：独立有界数学核查与完整作者证明。
只新增本文件；340 行二次商空间报告及两份 T 分支报告保持冻结。

## Claim

设 $d\geq3$ 为整数，$p\geq16d^2$ 为素数，且
$$
P(X)=X^d+c_{d-1}X^{d-1}+\cdots+c_0\in\mathbb F_p[X]
$$
为任意次数恰好为 $d$ 的首一多项式。令
$$
H_P(x,y)=(P(x)-y,x),\qquad
\Omega=\{(x_0,x_1,x_2)\in(\mathbb F_p^2)^3:x_0,x_1,x_2\text{ 两两不同}\}.
$$
特殊仿射群 $\mathscr A=\operatorname{ASL}_2(\mathbb F_p)$ 对三个有序点同时作用。
对每个 $\mathscr A$-不变复函数 $f:\Omega\to\mathbb C$，证明
$$
\operatorname{Var}_\Omega(f)\leq24\mathcal D_{H_P}(f),\qquad
\mathcal D_{H_P}(f)=\frac12\mathbb E_\Omega|f(H_P\mathbf x)-f(\mathbf x)|^2.
\tag{T}
$$
概率测度为 $\Omega$ 上的均匀测度。常数对所有满足条件的 $d,p$ 及所有 $P$ 的系数统一。

## Status

`PROVABLE AS STATED`。下文实际证明
$$
\operatorname{Var}_\Omega(f)\leq18\mathcal D_{H_P}(f),
\tag{1}
$$
因此目标的安全常数 $24$ 成立。没有加入消除次高项、限制低阶系数或选取特殊多项式的条件。
唯一外部深定理是精确适用的多项式加性特征和 Weil 界，来源和条件在 Step 3 明确核验。

## Assumptions

- $d\geq3$，$p\geq16d^2$ 为素数，因而 $p>d$ 且 $p\neq2$。
- 三个点有序、互异，线性群是行列式为 $1$ 的特殊线性群。
- 函数允许复值，函数差的平方范数均为复绝对值平方。
- $P$ 的所有低阶系数都任意；首一且次数恰为 $d$ 是唯一系数约束。
- 不要求增量分布对称，也不要求特殊仿射商上的转移可逆。
- 目标只限于 $\mathscr A$-不变函数，不包括整个生成元随机游走的轨道内谱隙或词长比较。

## Notation

写 $x_0=(x,y)$，$x_1-x_0=(u,r)$，$x_2-x_0=(v,s)$，固定有向面积
$$
\Delta=us-vr=\det(x_1-x_0,x_2-x_0).
$$
非共线轨道为 $\mathcal N_\Delta$，$\Delta\in\mathbb F_p^*$；
共线轨道为 $\mathcal C_a$，$a\in\mathbb F_p\setminus\{0,1\}$，满足 $x_2-x_0=a(x_1-x_0)$。
两个轨道指标集合取带类型标记的不交并 $I=\mathcal N\sqcup\mathcal C$。
记对应函数值为 $f_\Delta,f_a$，轨道质量为 $\pi_\Delta,\pi_a$。
下文 $k=d-2$，$\beta=3/(p+1)$，并定义
$$
R=\frac{d-3}{\sqrt p}+\frac3{p+1},\qquad
M=\frac{d-2}{p}+\frac3{p+1}.
\tag{2}
$$
用 $R$ 表示 Fourier 上界，以免与差向量第二坐标 $r$ 混淆。

## Proof Strategy

首先将非共线面积变化写成独立基点变量与差向量变量的多项式。
其关于基点第一坐标的首项在全部低阶系数下保持不变，给出统一的指数和界与最大原子界。
随后在整个加法群上作 Fourier 能量估计，再精确扣除人为加入的零状态所关联的边。
最后用共线轨道的统一逃逸下界与原始均匀测度的平稳性控制共线函数值。

## Dependency Map

1. 商轨道及质量只依赖特殊仿射几何，不依赖 $P$。
2. 面积增量的精确次数依赖首一性及 $p>d$，不依赖低阶系数。
3. Fourier 界使用已核验的 Weil 加性特征和界；最大原子及共线逃逸只用多项式根数。
4. 非共线能量使用 Fourier–Parseval 恒等式及删去零状态的精确边损失。
5. 最终不等式使用置换保测性、复范数三角估计和统一常数计算。

## Proof

### Step 1. 商轨道、平稳性及所需变量的独立性

特殊线性变换保持有向面积，并对行列式相同的两个可逆标架传递；
也对非零向量传递。因此上述 $\mathcal N_\Delta$ 和 $\mathcal C_a$ 恰是全部轨道。
通过选择基点和差向量计数，得到
$$
|\mathcal N_\Delta|=p^3(p^2-1),\qquad
|\mathcal C_a|=p^2(p^2-1),\qquad
|\Omega|=p^2(p^2-1)(p^2-2),
$$
从而
$$
\pi_\Delta=\alpha:=\frac p{p^2-2},\qquad
\pi_a=\frac1{p^2-2}.
\tag{3}
$$
这些质量相对于整个 $\Omega$，未在各块内重新归一化。

在固定 $\mathcal N_\Delta$ 内，给定任意 $x\in\mathbb F_p$ 及 $(u,v)\neq(0,0)$，
$us-vr=\Delta$ 对 $(r,s)$ 有 $p$ 个解，基点的第二坐标 $y$ 有 $p$ 种选择。
所以每个 $(x,u,v)$ 都有恰好 $p^2$ 个补全，证明
$$
x\text{ 在 }\mathbb F_p\text{ 上均匀，}\quad
(u,v)\text{ 在 }\mathbb F_p^2\setminus\{(0,0)\}\text{ 上均匀，且二者独立。}
\tag{4}
$$
分布也不依赖所固定的非零 $\Delta$。

$H_P^{-1}(X,Y)=(Y,P(Y)-X)$，所以 $H_P$ 置换 $\Omega$ 并保持均匀测度。
令 $K_{ij}$ 为轨道 $i$ 内均匀选点后，其像落入轨道 $j$ 的概率，则
$$
\sum_i\pi_iK_{ij}=\pi_j,\qquad
\mathcal D_{H_P}(f)=\frac12\sum_{i,j\in I}\pi_iK_{ij}|f_j-f_i|^2.
\tag{5}
$$
此商链由条件平均定义，不要求 $H_P$ 把一整条轨道映到一整条轨道。

### Step 2. 全系数保持的面积增量最高项

变换后的两个差向量为
$$
(P(x+u)-P(x)-r,u),\qquad(P(x+v)-P(x)-s,v).
$$
因此
$$
\Delta'=\Delta+F_P(x,u,v),\qquad
F_P(x,u,v)=v(P(x+u)-P(x))-u(P(x+v)-P(x)).
\tag{6}
$$
若 $uv(u-v)=0$，则 $F_P$ 作为 $x$ 的多项式恒为零。
这些坏的非零 $(u,v)$ 在三条过原点直线上，共有 $3p-3$ 个，所占概率为 $\beta=3/(p+1)$。

若 $uv(u-v)\neq0$，则 $F_P$ 关于 $x$ 的次数恰好为 $k=d-2$，最高项系数为
$$
\binom d2uv(u-v)\neq0.
\tag{7}
$$
验证如下：首一项 $X^d$ 在一次差分中的 $x^{d-1}$ 系数是 $du$，
在 $v$ 倍第一差分减 $u$ 倍第二差分时相消；下一阶的贡献是
$\binom d2(vu^2-uv^2)$。次高项 $c_{d-1}X^{d-1}$ 的可能 $x^{d-2}$ 项也因
$(d-1)c_{d-1}(vu-uv)=0$ 相消，更低项至多贡献 $x^{d-3}$。
因为 $p>d$，$\binom d2=d(d-1)/2$ 在 $\mathbb F_p$ 中非零，证明 (7)。

### Step 3. 增量分布的 Fourier 上界与最大原子

按 (4) 的独立均匀分布定义概率测度
$$
\nu_P(t)=\mathbb P(F_P(x,u,v)=t),\qquad t\in\mathbb F_p.
$$
由 (6) 和 (4)，对所有非零 $\Delta,\varepsilon$，
$$
K_{\Delta\varepsilon}=\nu_P(\varepsilon-\Delta).
\tag{8}
$$
令 $\psi(z)=\exp(2\pi iz/p)$，并采用
$\widehat\nu_P(\xi)=\sum_t\nu_P(t)\psi(\xi t)$。
我们证明
$$
|\widehat\nu_P(\xi)|\leq R\quad(\xi\neq0),\qquad
\sup_t\nu_P(t)\leq M.
\tag{9}
$$

**使用的外部定理及条件。** 本文只需如下 Weil 加性特征和界：
若 $Q\in\mathbb F_p[X]$ 的正次数为 $n$，$p\nmid n$，且 $\eta$ 为非平凡加性特征，则
$$
\left|\sum_{x\in\mathbb F_p}\eta(Q(x))\right|\leq(n-1)\sqrt p.
\tag{W}
$$
已实际核对 Wan–Wang 的公开研究论文第一页式 (1) 及其紧邻的次数条件说明：
[Daqing Wan and Qiang Wang, *Index bounds for character sums with polynomials over finite fields*,
arXiv:1507.00988v1 (2015), p. 1](https://arxiv.org/pdf/1507.00988)。
该文给出上述经典 Weil 界的准确表述；本报告不把 (W) 视为自行证明的新引理。

对每个好的 $(u,v)$，(7) 给出 $1\leq n=k=d-2<p$，并且乘以任何 $\xi\neq0$ 不改变次数。
所以 $p\nmid n$，特征 $x\mapsto\psi(\xi x)$ 非平凡，(W) 的条件均满足。
亦可直接排除 Artin–Schreier 退化：非恒定 $Q_0^p-Q_0+c$ 的次数至少为 $p$，
不可能等于这里的 $1\leq k<p$。没有对未经核验的一般高次或小特征情形调用 (W)。

当 $d=3$ 时，好的 $(u,v)$ 给出非恒定线性多项式，因此相应的归一化加性特征和严格为零。
当 $d\geq4$ 时，(W) 给出其绝对值不超过 $(d-3)/\sqrt p$。
坏对的总权重为 $\beta$，它们的特征和绝对值不超过 $1$，故
$$
|\widehat\nu_P(\xi)|
\leq\beta+(1-\beta)\frac{d-3}{\sqrt p}
\leq R.
$$

对最大原子，固定好的 $(u,v)$ 后，$F_P(x,u,v)-t$ 为次数 $k$ 的非零多项式，
所以至多有 $k$ 个根。即便把全部坏对都计入一个原子，也只有
$$
\nu_P(t)\leq\beta+(1-\beta)\frac{k}{p}\leq M.
$$
这证明 (9)，而 $R,M$ 均不依赖 $P$ 的低阶系数。

### Step 4. 非对称卷积能量与删除零状态的精确损失

定义
$$
\mu_{\mathcal N}=\frac1{p-1}\sum_{\Delta\neq0}f_\Delta,\qquad
g(z)=\begin{cases}f_z-\mu_{\mathcal N},&z\neq0,\\0,&z=0.\end{cases}
$$
于是 $\sum_zg(z)=0$。这里的零状态只是 Fourier 证明装置，
不把具有不同函数值的共线轨道合并成一个真实马尔可夫状态。
采用计数测度范数 $\|g\|_2^2=\sum_z|g(z)|^2$，以及单位化 Fourier 变换
$$
\widehat g(\xi)=p^{-1/2}\sum_zg(z)\psi(-\xi z).
$$
完整加法群上的能量是
$$
\mathcal E_{\nu_P}(g)=\frac12\sum_{z,t}\nu_P(t)|g(z+t)-g(z)|^2.
$$
平移保持计数范数，展开平方并使用 Parseval 恒等式，给出
$$
\mathcal E_{\nu_P}(g)=\sum_\xi
\bigl(1-\operatorname{Re}\widehat\nu_P(\xi)\bigr)|\widehat g(\xi)|^2
\geq(1-R)\|g\|_2^2.
\tag{10}
$$
最后一步使用 $\widehat g(0)=0$ 和 (9)。这里使用实部而非假定 $\widehat\nu_P$ 为实数，
所以不需要 $\nu_P(t)=\nu_P(-t)$。

从完整能量中删去源或目标为零的边。$0\to0$ 的贡献为零，其他被删除边的总能量恰为
$$
\mathcal L_0(g)=\frac12\sum_{z\neq0}
\bigl(\nu_P(z)+\nu_P(-z)\bigr)|g(z)|^2
\leq M\|g\|_2^2.
\tag{11}
$$
两方向的原子界各为 $M$，但能量前面的 $1/2$ 保留，所以损失系数是 $M$，不是 $2M$。
剩余能量因此满足
$$
\mathcal E^\times_{\nu_P}(g)
:=\frac12\sum_{z,w\neq0}\nu_P(w-z)|g(w)-g(z)|^2
\geq(1-R-M)\|g\|_2^2.
\tag{12}
$$

令
$$
V_{\mathcal N}=\sum_{\Delta\neq0}\pi_\Delta|f_\Delta-\mu_{\mathcal N}|^2
=\alpha\|g\|_2^2.
$$
由 (5)、(8) 只保留非共线到非共线的能量，并使用 (12)，得到
$$
\mathcal D_{H_P}(f)\geq\alpha\mathcal E^\times_{\nu_P}(g)
\geq(1-R-M)V_{\mathcal N}.
\tag{13}
$$
没有遗漏 $p$ 或非共线块质量的归一化因子。

现在验证统一常数。由 $p\geq16d^2$、$d\geq3$ 和 $d+4\leq d^2$，
$$
R+M=\frac{d-3}{\sqrt p}+\frac{d-2}{p}+\frac6{p+1}
\leq\frac14+\frac{d+4}{16d^2}\leq\frac5{16}<\frac12.
$$
因此可安全使用
$$
\mathcal D_{H_P}(f)\geq\frac12V_{\mathcal N},\qquad
V_{\mathcal N}\leq2\mathcal D_{H_P}(f).
\tag{14}
$$

### Step 5. 共线轨道的统一逃逸下界

在 $\mathcal C_a$ 内，基点均匀，非零差向量 $(u,r)$ 均匀，且二者独立。
$u=0$ 的概率为 $1/(p+1)$；此时 $F_P(x,u,au)=0$。
当 $u\neq0$ 时，面积增量为
$$
F_P(x,u,au)
=u\bigl[aP(x+u)-P(x+au)+(1-a)P(x)\bigr].
\tag{15}
$$
由 (7)，它关于 $x$ 的次数为 $k$，首项系数是
$\binom d2a(1-a)u^3\neq0$。
因此条件于任意这样的 $u$，像仍共线的概率至多为 $k/p$。
若 $\rho_a=\sum_{\varepsilon\neq0}K_{a\varepsilon}$ 是实际逃逸概率，则
$$
\rho_a\geq\frac p{p+1}\left(1-\frac{k}{p}\right)
\geq\rho_*:=1-\frac1{p+1}-\frac{d-2}{p}.
\tag{16}
$$
不同 $a$ 的实际 $\rho_a$ 不必相等；后续只使用共同下界 $\rho_*$。
由参数界，
$$
\rho_*\geq1-\frac{d-1}{p}\geq1-\frac1{16d}\geq\frac{47}{48}>\frac12.
\tag{17}
$$

### Step 6. 平稳入流控制与最终常数

令 $V_{\mathcal C}=\sum_a\pi_a|f_a-\mu_{\mathcal N}|^2$。
由于条件均值是复数也不影响方差最小化，
$$
\operatorname{Var}_\Omega(f)\leq V_{\mathcal N}+V_{\mathcal C}.
\tag{18}
$$
由共同逃逸下界和 $|z+w|^2\leq2|z|^2+2|w|^2$，
$$
\begin{aligned}
\rho_*V_{\mathcal C}
&\leq\sum_a\pi_a\rho_a|f_a-\mu_{\mathcal N}|^2\\
&\leq2\sum_{a,\varepsilon\neq0}\pi_aK_{a\varepsilon}|f_a-f_\varepsilon|^2\\
&\quad+2\sum_{\varepsilon\neq0}
\left(\sum_a\pi_aK_{a\varepsilon}\right)|f_\varepsilon-\mu_{\mathcal N}|^2\\
&\leq4\mathcal D_{H_P}(f)+2V_{\mathcal N}.
\end{aligned}
\tag{19}
$$
最后一项用的是完整商链平稳性
$\sum_a\pi_aK_{a\varepsilon}\leq\sum_i\pi_iK_{i\varepsilon}=\pi_\varepsilon$，
不是反向边概率与前向边概率相等。
由 $\rho_*\geq1/2$ 及 (14)，
$$
V_{\mathcal C}\leq8\mathcal D_{H_P}(f)+4V_{\mathcal N}
\leq16\mathcal D_{H_P}(f).
$$
再结合 (18)、(14)，得到
$$
\operatorname{Var}_\Omega(f)\leq18\mathcal D_{H_P}(f),
$$
这证明 (1)，从而证明原命题 (T)。$\square$

## Corrections or Missing Assumptions

全次数推导没有定理级缺口；核查中需精确化但不改变结论的事项如下：

1. 非共线轨道中 $x$ 与 $(u,v)$ 的独立性按每个 $(x,u,v)$ 的 $p^2$ 个补全直接证明，
   不能只分别声称两个边际均匀。
2. 非对称增量分布的能量系数是 $1-\operatorname{Re}\widehat\nu_P$。
   删除零状态时须同时计入两个方向，并保留能量中的 $1/2$，得到 (11)。
3. 高次共线轨道的实际逃逸概率可随 $a$ 变化；(19) 第一行必须用共同下界对应的不等式。
4. 次高系数及更低系数不会改变 (7) 的首项，故整个论证确实对全部首一系数统一。
5. Weil 输入只在 $1\leq d-2<p$、非零加性频率下使用；三次多项式产生的线性和单独精确处理。

## Open Risks

- 对本报告的商空间命题 (T) 没有剩余开放证明义务；(W) 是明确引用且条件已核验的经典定理。
- 未处理 $d=2$，不复制旧报告的 Jacobi 和论证；未处理 $p<16d^2$ 或非首一约束以外的扩张。
- 未证明全部函数上的整体随机游走谱隙，未做有限差分提取、统一平移中心化或生成元词长比较。
- 未扩展到四点或更多点，不进行候选评分、容量估计或论文验收判断。

## 来源核验及交付边界

实际读取的外部数学输入是上述 Wan–Wang 原作者研究论文第 1 页式 (1) 及其次数充分条件。
Weil 1948 原文的 PMC 页面遇到验证码，出版社页面读取失败，已停止这些源；
它们没有被记作已核验正文，也未尝试绕过访问限制。
本报告依赖公开可读研究论文中的精确 Weil 界表述，不声称重新证明该深定理或完成专项查新。

本轮完整读取 `proof-writer/SKILL.md`，按其要求明确量词、外部定理、参数条件和边界。
全部新增论证均为符号证明，没有数值实验、外部写入、代理派生或旧报告修订。
仅交付本文件，原命题按全次数、全首一系数范围成立，至此完成有界任务。
