# Paper30：三个有序互异点的特殊仿射商空间能量下界

日期：2026-09-06。性质：独立有界数学核查与完整作者证明。
只新增本文件；不修改两份 T 分支报告，不涉及整个有限生成随机游走的谱隙。

## Claim

对素数 $p\geq29$，令
$$
\Omega=\{(x_0,x_1,x_2)\in(\mathbb F_p^2)^3:x_0,x_1,x_2\text{ 两两不同}\},
\qquad \mathscr A=\operatorname{ASL}_2(\mathbb F_p).
$$
$\mathscr A$ 通过对三个点施加同一个特殊仿射变换而作用。
令 $H(x,y)=(x^2-y,x)$，并令 $H$ 在 $\Omega$ 上逐点作用。
对任意 $\mathscr A$-不变函数 $f:\Omega\to\mathbb C$，证明
$$
\mathcal D_H(f):=\frac12\mathbb E_\Omega|f(H\mathbf x)-f(\mathbf x)|^2
\ \geq\ \frac1{24}\operatorname{Var}_\Omega(f),
\tag{T}
$$
其中期望取 $\Omega$ 上的均匀概率测度，
$\operatorname{Var}_\Omega(f)=\mathbb E_\Omega|f-\mathbb E_\Omega f|^2$。

## Status

`PROVABLE AS STATED`。下文实际上证明
$$
\operatorname{Var}_\Omega(f)\leq23\mathcal D_H(f),
\tag{1}
$$
从而原定安全常数 $1/24$ 成立。原命题及其函数空间没有缩小。
不声称常数最优，不证明整个随机游走的谱隙，不进行新意或容量评价。

## Assumptions

- $p\geq29$ 是素数；特别地排除特征 $2$、$3$。
- 点是有序的；不对三个点的置换取商。
- 群的线性部分是 $\operatorname{SL}_2$，不是 $\operatorname{GL}_2$，所以有向面积本身保留。
- $f$ 允许复值；函数差的平方范数均为复绝对值平方。$H$ 的坐标公式仍在 $\mathbb F_p$ 中计算。
- 能量使用前向 $H$ 和因子 $1/2$；不额外假设商空间转移可逆或满足细致平衡。

## Notation

对 $\mathbf x=(x_0,x_1,x_2)$ 写差向量
$$
w_1=x_1-x_0=(u,r),\qquad w_2=x_2-x_0=(v,s),
\qquad\Delta=\det(w_1,w_2)=us-vr.
$$
非共线轨道记为 $\mathcal N_\Delta$，其中 $\Delta\in\mathbb F_p^*$。
共线轨道记为 $\mathcal C_a$，其中 $a\in\mathbb F_p\setminus\{0,1\}$，且 $w_2=aw_1$。
分别记两类轨道指标集合为 $\mathcal N$、$\mathcal C$。
总指标集取带类型标记的不交并 $I=\mathcal N\sqcup\mathcal C$，$\mathcal O_i$ 表示对应轨道。
轨道上的函数值记为 $f_\Delta$、$f_a$，轨道概率质量记为 $\pi_\Delta$、$\pi_a$。

## Proof Strategy

先精确分类特殊仿射轨道并计算质量。随后计算 $H$ 后有向面积的变化，
通过三次纤维计数证明非共线面积轨道之间的转移概率有统一下界。
纤维下界使用完整的高斯和与 Jacobi 和证明，不调用一般 Weil 界。
最后分别控制非共线部分的离差和共线部分到非共线均值的离差，组合得到 (1)。

## Dependency Map

1. 轨道分类依赖特殊线性变换对给定行列式标架和非零向量的传递性。
2. 商空间平稳性只依赖 $H$ 是 $\Omega$ 的置换。
3. 非共线转移下界依赖 $uv(u-v)$ 的纤维计数和三次 Jacobi 和绝对值。
4. 共线逃逸概率依赖非零差向量的均匀分布。
5. 最终能量不等式依赖复平方范数恒等式、平稳入流界及明确常数计算。

## Proof

### Step 1. 轨道分类、大小与均匀测度

若 $\Delta\neq0$，两个标架矩阵 $B=(w_1,w_2)$、$B'=(w'_1,w'_2)$
具有同一行列式，当且仅当 $B'B^{-1}\in\operatorname{SL}_2(\mathbb F_p)$。
配上平移项 $x'_0-(B'B^{-1})x_0$，即得到把基点也送到指定目标的特殊仿射变换。
反向由行列式不变性给出。因此每个非零有向面积恰是一条轨道。
计数时，基点有 $p^2$ 种，非零 $w_1$ 有 $p^2-1$ 种，而
$\det(w_1,w_2)=\Delta$ 对 $w_2$ 有 $p$ 个解；于是
$$
|\mathcal N_\Delta|=p^3(p^2-1).
\tag{2}
$$

若 $\Delta=0$，因三个点两两不同，$w_1\neq0$ 且存在唯一
$a\in\mathbb F_p\setminus\{0,1\}$ 使 $w_2=aw_1$。
任何可逆仿射变换都保持这个有序比值。另一方面，特殊线性群对非零向量传递：
把给定非零向量分别扩成行列式为 $1$ 的两个标架，其标架变换即在特殊线性群内。
故每个 $a$ 恰是一条轨道，并且
$$
|\mathcal C_a|=p^2(p^2-1).
\tag{3}
$$
由有序互异点的直接计数，或由 (2)、(3) 相加，
$$
|\Omega|=p^2(p^2-1)(p^2-2),\qquad
\pi_\Delta=\frac{p}{p^2-2},\qquad
\pi_a=\frac1{p^2-2}.
\tag{4}
$$
其中非共线指标有 $p-1$ 个，共线指标有 $p-2$ 个。
这些是整个 $\Omega$ 上的轨道质量，不是各块内重新归一化后的质量。

### Step 2. 商空间转移与有向面积公式

$H$ 的逆映射是 $H^{-1}(X,Y)=(Y,Y^2-X)$，所以 $H$ 是 $\mathbb F_p^2$ 的置换，
逐点作用也置换 $\Omega$，并保持其均匀概率测度。
对任意两个轨道指标 $i,j$，定义
$$
K_{ij}=\frac{|\{\mathbf x\in\mathcal O_i:H\mathbf x\in\mathcal O_j\}|}
{|\mathcal O_i|}.
$$
则 $K$ 行随机，并且
$$
\sum_i\pi_iK_{ij}=\pi_j.
\tag{5}
$$
式 (5) 来自目标轨道 $\mathcal O_j$ 在置换 $H$ 下的原像计数。
并不需要 $H$ 把一整条特殊仿射轨道送到另一整条轨道，也不要求 $K$ 可逆。
对轨道不变函数，定义直接给出
$$
\mathcal D_H(f)=\frac12\sum_{i,j}\pi_iK_{ij}|f_j-f_i|^2.
\tag{6}
$$

写 $x_0=(x,y)$。两个变换后差向量是
$$
(2xu+u^2-r,u),\qquad(2xv+v^2-s,v).
$$
按上述固定的列向量取向计算行列式，得到
$$
\Delta'=\Delta+u^2v-uv^2=\Delta+uv(u-v).
\tag{7}
$$
基点中的 $x$ 项完全相消，因此面积转移不依赖基点。

在固定 $\mathcal N_\Delta$ 上，$(u,v)$ 均匀分布于
$\mathbb F_p^2\setminus\{(0,0)\}$：给定非零行 $(u,v)$，方程
$us-vr=\Delta$ 对 $(r,s)$ 有恰好 $p$ 个解，另有 $p^2$ 个基点选择。
因此每个这样的 $(u,v)$ 都对应 $p^3$ 个三点组。

### Step 3. 三次纤维的统一下界

对 $t\in\mathbb F_p$ 定义
$$
n_t=\#\{(u,v)\in\mathbb F_p^2\setminus\{(0,0)\}:uv(u-v)=t\}.
$$
我们证明
$$
n_t\geq\frac p2\qquad\text{对所有 }t\in\mathbb F_p.
\tag{8}
$$

**零纤维。** 三条直线 $u=0$、$v=0$、$u=v$ 只在原点相交。
去掉原点后，每条贡献 $p-1$ 个点，所以 $n_0=3p-3\geq p/2$。

**非零纤维与三次特征。** 若 $t\neq0$，则 $u\neq0$，写 $a=v/u$。
方程变为 $a(1-a)u^3=t$，其中 $a\neq0,1$。
如果 $p\equiv2\pmod3$，三次幂在 $\mathbb F_p^*$ 上是双射，故
$$
n_t=p-2.
\tag{9}
$$

如果 $p\equiv1\pmod3$，取 $\mathbb F_p^*$ 上一个阶为 $3$ 的乘性特征 $\chi$，
并延拓为 $\chi(0)=0$；其存在性来自 $\mathbb F_p^*$ 的循环性。
对 $r\neq0$，方程 $u^3=r$ 的解数是 $1+\chi(r)+\chi(r)^2$。
记
$$
J(\eta,\theta)=\sum_{a\in\mathbb F_p}\eta(a)\theta(1-a).
$$
于是
$$
n_t=p-2+\chi(t)J(\chi^2,\chi^2)+\chi(t)^2J(\chi,\chi).
\tag{10}
$$
这里使用 $\chi(a(1-a))^{-1}=\chi(a)^2\chi(1-a)^2$；
$a=0,1$ 的 Jacobi 和项为零，因此没有漏掉或多加这两个参数。

**Jacobi 和绝对值的自包含证明。** 令
$\psi(x)=\exp(2\pi i x/p)$，其中 $x$ 取任意整数代表元；
对非平凡乘性特征 $\eta$，延拓 $\eta(0)=0$ 并记
$G(\eta)=\sum_x\eta(x)\psi(x)$。
非平凡性给出 $\sum_{t\neq0}\eta(t)=0$。令 $x=ty$，有限求和直接得到
$$
\begin{aligned}
|G(\eta)|^2
&=\sum_{t\neq0}\eta(t)\sum_{y\neq0}\psi((t-1)y)\\
&=(p-1)-\sum_{t\neq1}\eta(t)=p.
\end{aligned}
\tag{11}
$$
第二行使用非平凡加性特征的和为零：内和在 $t=1$ 时为 $p-1$，其余时候为 $-1$。

在乘积 $G(\chi)^2$ 中按 $s=x+y$ 分组。
$s=0$ 部分是 $\chi(-1)\sum_x\chi(x)^2=0$，因为 $\chi^2$ 非平凡。
对 $s\neq0$，置 $x=sa$、$y=s(1-a)$，得到
$$
G(\chi)^2=J(\chi,\chi)G(\chi^2).
\tag{12}
$$
(11) 分别适用于 $\chi$ 和 $\chi^2$，因此 (12) 给出
$$
|J(\chi,\chi)|=\sqrt p.
$$
又因 $\chi^2=\overline\chi$，
$J(\chi^2,\chi^2)=\overline{J(\chi,\chi)}$，其绝对值也为 $\sqrt p$。
这一步没有调用一般 Weil 界，也没有把乘积特征非平凡的条件略去。

由 (10)，非零纤维满足 $n_t\geq p-2-2\sqrt p$；(9) 也满足这个较弱下界。
最后 $p\geq29$ 保证 $\sqrt p\geq5$，故
$$
p-2-2\sqrt p-\frac p2
=\frac{(\sqrt p-2)^2-8}{2}\geq\frac12>0.
$$
与零纤维计算合并，证明 (8)。$\square$

### Step 4. 非共线块的完整混合下界

由 (7)、均匀的 $(u,v)$ 分布和 (8)，对所有非零 $\Delta,\varepsilon$，
$$
K_{\Delta\varepsilon}=\frac{n_{\varepsilon-\Delta}}{p^2-1}
\geq\frac{p}{2(p^2-1)}\geq\frac1{2p}.
\tag{13}
$$
当 $\varepsilon=\Delta$ 时使用的是零纤维 $n_0=3p-3$，不是非零纤维公式。

定义非共线块的条件均值和两个未重新归一化的离差量：
$$
\mu_{\mathcal N}=\frac1{p-1}\sum_{\Delta\neq0}f_\Delta,\qquad
V_{\mathcal N}=\sum_{\Delta\neq0}\pi_\Delta|f_\Delta-\mu_{\mathcal N}|^2,
\qquad
V_{\mathcal C}=\sum_a\pi_a|f_a-\mu_{\mathcal N}|^2.
\tag{14}
$$
方差的最小化性质对复数同样成立，故
$$
\operatorname{Var}_\Omega(f)\leq V_{\mathcal N}+V_{\mathcal C}.
\tag{15}
$$
例如对任意 $c\in\mathbb C$，
$\mathbb E|f-c|^2=\operatorname{Var}(f)+|\mathbb Ef-c|^2$；取 $c=\mu_{\mathcal N}$ 即得 (15)。

令 $r=p-1$、$\alpha=p/(p^2-2)=\pi_\Delta$。
复平方范数恒等式为
$$
\sum_{\Delta,\varepsilon\neq0}|f_\varepsilon-f_\Delta|^2
=2r\sum_{\Delta\neq0}|f_\Delta-\mu_{\mathcal N}|^2.
$$
对 (6) 只保留非共线到非共线的有向项，并使用 (13)，得到
$$
\begin{aligned}
\mathcal D_H(f)
&\geq\frac12\sum_{\Delta,\varepsilon\neq0}\pi_\Delta K_{\Delta\varepsilon}
|f_\varepsilon-f_\Delta|^2\\
&\geq\frac{\alpha}{4p}\sum_{\Delta,\varepsilon\neq0}|f_\varepsilon-f_\Delta|^2
=\frac{p-1}{2p}V_{\mathcal N}
\geq\frac13V_{\mathcal N}.
\end{aligned}
\tag{16}
$$
所以 $V_{\mathcal N}\leq3\mathcal D_H(f)$。

### Step 5. 共线块逃逸与平稳入流控制

在 $\mathcal C_a$ 中，$w_1=(u,r)$ 均匀分布于非零向量，且 $w_2=aw_1$。
由 (7)，
$$
\Delta'=a(1-a)u^3.
$$
因为 $a\neq0,1$，像仍共线当且仅当 $u=0$。
满足 $u=0$ 的非零向量有 $p-1$ 个，因此
$$
\mathbb P(\Delta'=0\mid\mathcal C_a)=\frac1{p+1},\qquad
\sum_{\varepsilon\neq0}K_{a\varepsilon}=\rho:=\frac p{p+1}.
\tag{17}
$$
这个逃逸概率与 $a$ 无关。若 $u=0$，变换后的两个差向量是 $(-r,0)$、$(-ar,0)$，
有序比值仍为 $a$；此额外观察不参与能量下界。

对任意复数 $z,w$，$|z+w|^2\leq2|z|^2+2|w|^2$。
利用 (17) 后对 $f_a-\mu_{\mathcal N}=(f_a-f_\varepsilon)+(f_\varepsilon-\mu_{\mathcal N})$
应用这个不等式，得到
$$
\begin{aligned}
\rho V_{\mathcal C}
&\leq2\sum_{a,\varepsilon\neq0}\pi_aK_{a\varepsilon}|f_a-f_\varepsilon|^2\\
&\quad+2\sum_{\varepsilon\neq0}
\left(\sum_a\pi_aK_{a\varepsilon}\right)|f_\varepsilon-\mu_{\mathcal N}|^2\\
&\leq4\mathcal D_H(f)+2V_{\mathcal N}.
\end{aligned}
\tag{18}
$$
最后一行中，第一个未乘 $1/2$ 的子和至多为 $2\mathcal D_H(f)$，
再乘外面的 $2$ 即得 $4\mathcal D_H(f)$；第二项使用 (5) 的平稳入流界
$$
\sum_a\pi_aK_{a\varepsilon}
\leq\sum_i\pi_iK_{i\varepsilon}=\pi_\varepsilon.
$$
没有在这里假设反向转移概率等于前向概率。

### Step 6. 常数合并

为保留简单的绝对常数，只用 $\rho\geq1/2$。
由 (18)、(16)，
$$
V_{\mathcal C}\leq8\mathcal D_H(f)+4V_{\mathcal N}
\leq20\mathcal D_H(f).
$$
再用 (15)、(16)，
$$
\operatorname{Var}_\Omega(f)
\leq V_{\mathcal N}+V_{\mathcal C}
\leq23\mathcal D_H(f).
$$
这证明 (1)，因此也证明原定的 (T)。$\square$

## Corrections or Missing Assumptions

主控给出的推导无需定理级修正。完成证明时需明确的四点已经在正文补齐：

1. 面积固定为 $\det(x_1-x_0,x_2-x_0)$；(7) 的正号与这个有序取向一致。
2. 当面积转移差为零时，必须使用去掉原点后的 $3p-3$，而非套用非零纤维估计公式。
3. Jacobi 和的平方根绝对值要求 $\chi,\chi^2$ 都非平凡；$p\equiv1\pmod3$ 的阶三特征
   满足该条件，且 (11)、(12) 已给出完整证明。
4. 控制共线块入流时使用整个商链的平稳性，不是假定可逆性，也不把块内权重重新归一化。

## Open Risks

- 对本报告的目标 (T) 没有留下未证明的引理或参数例外；常数 $1/24$ 不宣称最优。
- 没有推广到 $p<29$、特征 $2$ 或 $3$，也没有推广到非素数有限域。
- 结论仅适用于 $\mathscr A$-不变函数；任意函数上的整体随机游走谱隙还需独立的轨道内控制
  及比较论证，本报告没有执行或默认这些步骤。
- 没有把这个三点结论推广到更多点，也没有将核查结果当作新意、容量或论文验收结论。

## 核验与交付边界

本轮完整读取 `proof-writer/SKILL.md`，其要求落实为精确定义、依赖分解、完整特征和证明、
复值范数处理及开放边界声明。所有计算均为以上符号推导；没有数值实验、外部写入或代理派生。
只新增本报告，原命题按原条件证明成立，至此完成本次有界任务。
