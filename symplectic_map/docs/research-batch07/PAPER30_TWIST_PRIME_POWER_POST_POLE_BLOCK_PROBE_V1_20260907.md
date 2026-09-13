# Paper 30：奇素数幂第一个极点之后的非内部模态块

日期：2026-09-07。作者：`p30_twist_leading_structure_probe`。
本轮完整读取并使用 `proof-writer` 技能。本件是作者证明，不是非作者独审票。

## Claim

令 $p$ 为任意奇素数、$a\ge2$、$s=p^a$，$\zeta$ 为任意本原 $s$ 次根。
使用同一物理正 kick、固定参数与 SUM action，取

$$
h=2-\zeta-\zeta^{-1},\qquad \rho=-h,\qquad
L=\rho\lambda,\qquad m=(p-1)/2,\qquad M=p^{a-1}m.
$$

在 $K^+=\mathbb Q_p(h)$ 中令 $\mathcal O^+=\mathbb Z_p[h]$，
$v_h(h)=1$，所以 $v_h(p)=M>2m$。
对实际非共振分支

$$
V_n(L)=\rho^n v_n(L/\rho),\qquad
d_n=\frac{D_n}{\rho}=-\frac{D_n}{h},\qquad
D_n=2-\zeta^n-\zeta^{-n},
$$

本件只研究 $p+1\le n\le2p-1$，证明以下完整多项式结论。

1. 对每个 $1\le j\le p-1$，

$$
\boxed{W_j(L):=pV_{p+j}(L)\in\mathcal O^+[L].}
\tag{1}
$$

2. 令 $q=(1-4L)/16$、$A(x)=1-x/2+qx^2$。
全部首层剩余由同一个有限生成函数给出：

$$
\boxed{
\sum_{j=1}^{p-1}\overline{W_j}(L)x^j
=\frac{xA'(x)}{2A(x)}
=\frac{-x/4+qx^2}{1-x/2+qx^2}
\pmod{x^p}.}
\tag{2}
$$

横线在 $\mathcal O^+/(h)=\mathbb F_p$ 中解释。
等价地，在 $\mathbb F_p[L]$ 中定义

$$
T_0=2,\qquad T_1=1/2,\qquad
T_j=\frac12T_{j-1}-qT_{j-2}\quad(j\ge2).
$$

则 $\overline{W_j}=-T_j/2$，是完整参数多项式身份，不限于一般位置的参数。

3. $\deg_L\overline{W_j}=\lfloor j/2\rfloor$，其最高系数为

$$
\boxed{
[L^k]\overline{W_{2k}}=-4^{-k},\qquad
[L^k]\overline{W_{2k+1}}=-(2k+1)4^{-k-1}.}
\tag{3}
$$

只在 $1\le j<p$ 的范围使用式 (3)。这些数均非零，
故每个 $V_{p+j}$ 的系数最小 $h$ 赋值恰为 $-M$。
因此 $p$ 尺度在多项式系数意义上是准确的，不能继续使用 $h^m$ 尺度。
对整参数 $L$，若 $T_j(\bar L)\ne0$，有 $v_h(V_{p+j}(L))=-M$。
特别地，$\overline{W_1}=-1/4$，所以第一个后极点模态 $V_{p+1}$
对每个局部代数整数参数 $L$ 均有此准确极点阶。

## Status

式 (1)—(3)、完整有限指数桥及上述条件赋值结论：`PROVABLE AS STATED`。

本件不确定第二内部 forcing 的第一个非零层，不证明完整
$C_{p^a}$ 的 Newton 多边形、平方自由性或与 $Q_{p^a}$ 互素。
这些不能从本块的非内部模态整性推出。

## Assumptions and Inputs

已全文读取
[素数幂首层内部结构稿](PAPER30_TWIST_PRIME_POWER_LOCAL_STRUCTURE_PROBE_V1_20260907.md)，
SHA256：`f9dd643975ecbdb08a1512aacbebb692b96e84fceb8ab66fd69baecbbba6b616`。
只使用以下已接受事实：

$$
V_n\in\mathcal O^+[L]\quad(1\le n<p),\qquad
h^mV_p\in\mathcal O^+[L],\qquad
\overline{h^mV_p}=\frac{(-1)^m}{2}(2-L^m),
\tag{4}
$$

以及 $v_h(p)=M>2m$、$d_n\equiv-n^2\pmod h$ 对 $p\nmid n$ 成立。
实际递推的符号始终是

$$
d_nV_n=-\frac12[x^{n-1}]e^V-L[x^{n-2}]e^{2V}.
\tag{5}
$$

由于 $2p<s$，本件全部模态均不是全系统共振，没有进行任何模态置零。
特别是 $V_p$ 为实际非整模式，不是投影为零的素数周期模式。

## Notation

低块记作

$$
P(x)=\sum_{n=1}^{p-1}V_nx^n.
$$

在所需有限次数中，其剩余与平方传播子解

$$
U(x)=-\log A(x),\qquad A(x)=1-x/2+qx^2
\tag{6}
$$

相同。这里 $U$ 首先在特征零定义；只约化 $n<p$ 的系数。
指数在特征 $p$ 中仅表示明确限定次数的有限表达式，不定义越过 $p!$ 的无限指数。

记 $N_x=x\partial_x$；$M$ 专指分歧高度，不作微分算子使用。
所有多项式整性均为逐系数整性；参数代入的赋值结论另行注明。

## Proof Strategy and Dependency Map

1. 在特征零把 $n<2p$ 的指数分成低块指数与高模式的线性项。
2. 逐个检查低块指数的 $p!$ 带，证明乘 $p$ 后整，并算出其准确剩余。
3. 保留 $pV_p$ 后，对 $p+1,\ldots,2p-1$ 逐阶证明 $pV_n$ 整。
4. 只在整性完成后取模，得到一个有唯一有限解的 Jacobi 型方程。
5. 有理生成函数解该方程，再读取完整参数多项式及准确极点阶。

主控和第二 forcing 作者也分别导出了相同首层，属于协作交叉计算。
本件负责这段完整三角整性与首层证明的文件所有权；这些同推不计为非作者认证。

## Proof

### Step 1. 低块指数的一条完整阶乘带

必要时可把这里的低块先置于独立形式变量 $H$ 中：沿用输入稿的
$d_n(H)\in\mathbb Z[H]$，其 $n<p$ 的常数项为 $-n^2$，
故 $P(H,x)\in\mathbb Z_{(p)}[L][[H]][x]$，且 $V_1(H,L)=1/2$ 精确。
以下阶乘运算在该形式环中也成立；令 $H=h$ 才得到实际局部式。

对 $\alpha=1,2$ 和 $0\le N<2p$，系数 $[x^N]e^{\alpha P}$ 只使用
$k!$、$k\le N$。因 $2p-1<p^2$，这些阶乘至多含一个 $p$ 因子。
于是

$$
p[x^N]e^{\alpha P}\in\mathcal O^+[L],\qquad
[x^N]e^{\alpha P}\in\mathcal O^+[L]\quad(N<p).
\tag{7}
$$

对 $p\le k<2p$ 写 $k=p+r$、$0\le r<p$。在 $\mathbb F_p$ 中，

$$
\overline{\frac p{(p+r)!}}
=\frac1{(p-1)!\,r!}=-\frac1{r!}.
\tag{8}
$$

这里 $(p-1)!=-1$ 来自非零剩余类按逆元配对。
对 $k<p$ 的指数项，乘 $p$ 后的系数约化为零。
因此在所有小于 $2p$ 的系数上，

$$
\overline{p e^{\alpha P}}
=-\alpha\bar P^p\sum_{r=0}^{p-1}\frac{(\alpha\bar P)^r}{r!}
\pmod{x^{2p}}.
\tag{9}
$$

使用 $\alpha^p=\alpha$ 只针对整数 $\alpha=1,2$，没有将参数 $L^p$ 替换为 $L$。
第一阶原递推中 $d_1=-1$ 精确，所以 $V_1=1/2$。
Frobenius 在小于 $2p$ 的次数中只留下
$\bar P^p=x^p/2$；其余低模式的 $p$ 次幂从 $x^{2p}$ 起。
乘去 $x^p$ 后，所需指数系数只到 $p-1$ 阶，故式 (6) 可合法给出

$$
\boxed{
\overline{p e^{\alpha P}}
=-\frac\alpha2x^p A(x)^{-\alpha}
\pmod{x^{2p}}.}
\tag{10}
$$

更强的同范围形式系数版本是：对 $0\le j<p$ 和 $\alpha=1,2$，存在
$R_{\alpha,j}(H,L)\in\mathbb Z_{(p)}[L][[H]]$ 使

$$
p[x^{p+j}]e^{\alpha P(H,x)}
=-\frac\alpha2[x^j]e^{\alpha P(H,x)}
+pR_{\alpha,j}(H,L).
\tag{10a}
$$

证明仍是式 (8)—(9)，但先在形式系数环中模 $p$，不把 $H$ 置零；
$\bar P(H,x)^p=x^p/2\pmod{x^{2p}}$ 只用到精确第一系数，
所以不产生额外的 $H$ 误差。所有参数次数都有来自有限 $x$ 次数的统一界。

式 (10) 约化的是已整的 $p[x^N]e^{\alpha P}$。
不能先分别约化尚非整的 $[x^N]e^{\alpha P}$，也不能删掉第 $p$ 至第 $2p-1$
次指数项。

### Step 2. 保留内部模式的三角整性

对已求的高模式前缀写

$$
R(x)=\sum_{n=p}^{n_0}V_nx^n,
\qquad p\le n_0<2p.
$$

不论这些系数是否整，在特征零形式级数中都精确有

$$
e^{\alpha(P+R)}=e^{\alpha P}(1+\alpha R)
\pmod{x^{2p}},
\tag{11}
$$

因为 $R^2$ 的最小次数为 $2p$。
这是次数恒等式，不是将非整高模式的大小视为可忽略。
尤其式 (11) 的 $R$ 包含 $V_px^p$。

由式 (4)，

$$
pV_p=\frac p{h^m}(h^mV_p)
\in h^{M-m}\mathcal O^+[L],\qquad \overline{pV_p}=0.
\tag{12}
$$

假设已求高模式满足 $pV_n$ 整。
式 (11) 的低块部分乘 $p$ 后由式 (7) 整；
线性高模式部分在次数 $N<2p$ 中，每个 $pV_n$ 只乘以
$[x^{N-n}]e^{\alpha P}$，而 $N-n<p$，后者整。
因此当前前缀的所有所需指数系数乘 $p$ 后整。

对下一个 $n=p+j$，$1\le j<p$，其传播子满足
$\bar d_n=-j^2\ne0$。
把原递推 (5) 乘 $p$，右边已整，再除以这个单位，得到 $pV_n$ 整。
从式 (12) 开始逐阶归纳，直到 $2p-1$，证明式 (1)。

### Step 3. 完整有限指数桥

现在将已求块全部放入 $R=\sum_{n=p}^{2p-1}V_nx^n$，并定义

$$
\mathcal Z(x)=\sum_{j=0}^{p-1}pV_{p+j}x^j\in\mathcal O^+[L][x],
\qquad Z(x)=\overline{\mathcal Z}(x),\qquad Z(0)=0.
$$

式 (11) 的高模式部分乘 $p$ 后是
$\alpha x^p\mathcal Z e^{\alpha P}$。
其剩余只使用低于 $p$ 阶的指数，合法替换为 $A^{-\alpha}$。
与式 (10) 合并，得到对所有 $0\le N<2p$ 都成立的系数身份

$$
\boxed{
\overline{p[x^N]e^V}
=[x^{N-p}]A^{-1}(Z-1/2),\qquad
\overline{p[x^N]e^{2V}}
=2[x^{N-p}]A^{-2}(Z-1/2).}
\tag{13}
$$

负下标系数为零。这里 $V$ 可取至 $2p-1$ 的真实分支，
更高模式不影响该范围。
式 (13) 同时保留高模式反馈和低块阶乘带；$-1/2$ 只来自后者。
若把 $V_p$ 从特征零原式删去，便失去式 (12) 给出的真实余项，
即使本次普通约化无法看见该余项。

### Step 4. 非内部模态的首层方程及唯一解

对 $n=p+j$ 的式 (5) 乘 $p$ 后取模。
左边传播子为 $-j^2$，与右侧总负号相消。
使用式 (13)，得到

$$
j^2\overline{W_j}
=\frac12[x^{j-1}]A^{-1}(Z-1/2)
+2L[x^{j-2}]A^{-2}(Z-1/2).
$$

等价地，

$$
\boxed{
N_x^2 Z=\mathcal J(x)(Z-1/2)\pmod{x^p},\qquad
\mathcal J(x)=\frac{x}{2A(x)}+\frac{2Lx^2}{A(x)^2},\qquad Z(0)=0.}
\tag{14}
$$

每个 $j^2$ 在 $1\le j<p$ 可逆，而右侧因 $\mathcal J(0)=0$
只使用此前系数，所以式 (14) 有唯一所需有限解。

先在特征零令 $U=-\log A$。平方传播子方程给

$$
N_x^2U=\frac{x}{2A}+\frac{Lx^2}{A^2}.
$$

对它再施一次 $N_x$，利用
$N_x(x/A)=(x/A)(1+N_xU)$，得到准确身份

$$
N_x^3U=\mathcal J(1+N_xU).
$$

因此 $-N_xU/2=xA'/(2A)$ 满足式 (14) 的未截断有理身份及零常数项。
该有理式的分母常数为 $1$，全部系数只需除以 $2$，可在每个奇素数下约化。
由有限唯一性，它就是 $Z$，证明式 (2)。
这并不把 $j=p$ 的不可逆系数也纳入唯一性范围。

### Step 5. 完整参数多项式与准确尺度

在形式二次扩张中把
$A=(1-r_1x)(1-r_2x)$，其中 $r_1+r_2=1/2$、$r_1r_2=q$。
则

$$
\frac{xA'}{2A}
=-\frac12\sum_{j\ge1}(r_1^j+r_2^j)x^j.
$$

对称幂和 $T_j=r_1^j+r_2^j$ 满足 Claim 中的多项式递推，
所以结果实际上属于 $\mathbb F_p[L]$。
这里没有除以 $r_1-r_2$，故在 $L=0$ 的重根参数及 $q=0$ 的退化参数处同样成立。

也可直接以多项式身份计算

$$
T_j=\sum_{k=0}^{\lfloor j/2\rfloor}
(-1)^k\frac{j}{j-k}\binom{j-k}{k}
q^k\left(\frac12\right)^{j-2k}\qquad(j\ge1).
\tag{15}
$$

该式由 $-\log(1-x/2+qx^2)=\sum_{\ell\ge1}(x/2-qx^2)^\ell/\ell$
取第 $j$ 阶系数并乘 $j$ 得到：选 $k$ 个二次因子时 $\ell=j-k$，
因而产生所写的二项式和分母。

在本件 $j<p$ 范围，所有 $j-k$ 都可逆。
最大 $q$ 次幂的系数在偶数 $j=2k$ 时为 $2(-1)^k$，
在奇数 $j=2k+1$ 时为 $(2k+1)(-1)^k/2$。
代入 $q=(1-4L)/16$ 后得到式 (3)。
奇数情形有 $2k+1=j<p$，偶数情形的最高系数只含 $2$ 的单位因子，
所以均没有最高系数模 $p$ 意外消失。

于是 $pV_{p+j}$ 至少有一个单位系数，且所有系数整，
其实际 $V_{p+j}$ 的系数最小赋值恰为 $-M$。
这里只断言剩余多项式的次数为 $\lfloor j/2\rfloor$；
实际 $pV_{p+j}$ 可以有更高 $L$ 次数，其对应系数在 $h\mathcal O^+$ 中。
对任意整参数，非零剩余值时赋值恰为 $-M$，零剩余值时不作同样断言。
特别是 $j=1$ 的剩余为常数 $-1/4$，故该模态对所有整参数都不能消去。
证明完成。$\square$

## Exact Verification Actually Run

只执行一个全参数自由符号检查：对自由 $x,L$ 取 Claim 中的 $A,q$，令
$Y=xA'/(2A)$，计算

$$
N_x^2Y-\left(\frac{x}{2A}+\frac{2Lx^2}{A^2}\right)(Y-1/2).
$$

通分后残差严格为零，并同时核对 $Y=-N_x(-\log A)/2$。
实际输出：`EXACT_PASS full-parameter rational post-pole generating identity`。
整性和任意素数的阶乘带由上面的通用证明承担；未输入素数、分子或根的列表。

## Corrections or Missing Assumptions

- 传播子使用 $d_n=-D_n/h$，不是 $+D_n/h$。式 (14) 的符号已经保留这一区别。
- $pV_p$ 的本层消失来自 $M-m>0$，不是把内部模式置零。
- 任意奇素数均满足 $2p-1<p^2$、$2p<s$，所有边界次数对 $p=3$ 仍合法。
- 本件不把系数尺度的准确性误写成所有参数处所有模态都具有同一极点。

## Open Risks and Delivery Boundary

- 下一个内部模态 $2p$ 的传播子非单位；式 (14) 到 $j=p$ 失去单位三角性。
  即使端点 forcing 的普通剩余相消，也不能由本稿读出其第一个非零层。
- 对更高层必须保留 $d_{p+j}-d_j$ 的实际修正和式 (12) 的
  $h^{M-m}$ 级内部模式贡献，不能把本次 $h^0$ 首层永久代回全部递推。
- 更高指数一旦达到 $2p$，还会出现多个高模式的乘积和新的阶乘带；
  本件的精确线性展开只保证次数严格小于 $2p$。
- 不声明完整 $C_{p^a}$、全实根或 $C,Q$ 互素结论，不重复已有 $p$、$2p$ 结果。
- 只新写本作者稿；旧稿、入口、冻结锁与脚本均未改，待另行非作者核查。
