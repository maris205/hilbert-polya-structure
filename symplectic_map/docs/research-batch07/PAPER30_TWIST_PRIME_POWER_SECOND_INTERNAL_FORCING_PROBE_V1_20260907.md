# Paper 30：奇素数幂第二内部 forcing 的首个非零层

日期：2026-09-07。作者：`p30_twist_root_counterexample_probe`。
按本轮完整读取的 `proof-writer` 撰写。主控参与端点恒等式的协作推导，
不重复记为另一个贡献，也不充当本稿的非作者审查。

## Claim

令 $p$ 为任意奇素数，$a\ge2$，$s=p^a$，$\zeta$ 为任意本原 $s$ 次根。
保持同一个物理正 kick、固定参数和 SUM action，设

$$
h=2-\zeta-\zeta^{-1},\qquad \rho=-h,\qquad
L=\rho\lambda,\qquad m=(p-1)/2,\qquad M=p^{a-1}m.
\tag{1}
$$

在 $K^+=\mathbb Q_p(h)$ 中，记 $\mathcal O^+=\mathbb Z_p[h]$，
规范 $v_h(h)=1$。真实传播子和缩放分支是

$$
d_n=\frac{\zeta^n+\zeta^{-n}-2}{h}
=-\frac{D_n}{h}=\frac{D_n}{\rho},\qquad
V_n(L)=\rho^n v_n(L/\rho).
\tag{2}
$$

取实际分支到 $2p-1$，令

$$
V(x)=\sum_{n=1}^{2p-1}V_nx^n,\qquad
\mathcal B_2(L)=-[x^{2p-1}]e^V-2L[x^{2p-2}]e^{2V}.
\tag{3}
$$

这是同一个周期 $p^a$ 系统的第二内部 forcing，亦可记作
$\mathcal B_{2p\mid p^a}$ 的缩放式；它不是周期 $2p$ 系统的首项。
由于 $2p<p^a$，实际 $V_{2p}$ 不被设为零，而是
$V_{2p}=\mathcal B_2/(2d_{2p})$。

本件证明完整参数多项式身份

$$
\boxed{
h^{-2m}p\mathcal B_2\in\mathcal O^+[L],\qquad
\overline{h^{-2m}p\mathcal B_2}=2\in\mathbb F_p[L].}
\tag{4}
$$

因而 $p\mathcal B_2$ 的系数最小 $h$ 赋值，即其准确首个非零层，
恰为 $q_2=2m$，不是 $0$ 或 $m$。并有

$$
\boxed{pV_{2p}\in\mathcal O^+[L],\qquad
\overline{pV_{2p}}=-1/4.}
\tag{5}
$$

对每个局部代数整数参数 $L$，包括 $\bar L^m=2$ 的代数剩余根类，

$$
v_h(\mathcal B_2(L))=2m-M,\qquad v_h(V_{2p}(L))=-M.
\tag{6}
$$

令 $\mathcal B_1$ 为此前已接受的第一内部 forcing 的同一 $L$ 缩放式。
则式 (4) 还直接给出

$$
\boxed{\gcd_{K^+[L]}(\mathcal B_1,\mathcal B_2)=1.}
\tag{7}
$$

式 (7) 仅比较两个实际内部 forcing，不是完整 $C_{r,p^a}$、$Q_{r,p^a}$
的共同根定理，也不把任何内部根类称为完整首项的根。

## Status

式 (4)—(7) 及所述准确首层：`PROVABLE AS STATED`。

本件保留所有低于 $2m$ 的取消、非整 $V_p$ 和低块阶乘贡献。
对于完整 $C_{r,p^a}$ 的 Newton 多边形、简单性或 $C,Q$ 互素，
本件没有证明，也不作这些结论的推断。

## Assumptions and Exact Inputs

1. 已接受的
   [素数幂首层内部结构](PAPER30_TWIST_PRIME_POWER_LOCAL_STRUCTURE_PROBE_V1_20260907.md)，
   SHA256 `f9dd643975ecbdb08a1512aacbebb692b96e84fceb8ab66fd69baecbbba6b616`。
   本轮已全文读取。使用其真实递推、低块形式整性、
   $v_h(p)=M>2m$、$d_p/h^{2m}\equiv-1\pmod h$，以及

$$
h^mV_p\in\mathcal O^+[L],\qquad
\overline{h^mV_p}=\frac{(-1)^m}{2}(2-L^m).
\tag{8}
$$

   还使用其已证明的有限平方传播子和式 (32) 的配对系数和。
   不重新审查已经接受的首层。
2. 本轮新作者输入
   [首个极点后的非内部模态块](PAPER30_TWIST_PRIME_POWER_POST_POLE_BLOCK_PROBE_V1_20260907.md)，
   SHA256 `0a70394315cfe78b860c6ac46eec53bb58ccb8b3e432c1108438f7e721ee4c34`。
   已全文读取其 391 行准确版本。使用 $pV_{p+j}$ 的整性、
   完整有限指数线性展开，以及形式 $H$ 环中的精确阶乘桥 (10a)。
   这些是作者证明输入，接受由主控安排的非作者核查决定；
   本稿不把协作同推当作独立认证。

## Notation

令 $\mathcal N=x\partial_x$，$M$ 始终只表示分歧高度。
$\chi=(-1)^{m+1}$ 是一个符号常数，不表示参数中心。
多项式的赋值指系数赋值的最小值；对零取 $+\infty$。
对局部代数参数使用完备赋值的唯一延拓。

用独立形式变量 $H$ 定义实际 Chebyshev 传播子多项式

$$
C_0(H)=2,\quad C_1(H)=2-H,\quad
C_{n+1}(H)=(2-H)C_n(H)-C_{n-1}(H),\quad
d_n(H)=\frac{C_n(H)-2}{H}.
\tag{9}
$$

这里 $C_n(H)$ 仅是这一行定义的 Chebyshev 辅助记号，
与系统首项 $C_{r,s}$ 无关。
记 $\mathscr R=\mathbb Z_{(p)}[L][[H]]$。
低块形式分支

$$
P(H,x)=\sum_{n=1}^{p-1}P_n(H,L)x^n
\tag{10}
$$

由真实 $d_n(H)$ 递推定义。因为 $d_n(0)=-n^2$ 在 $n<p$ 时为单位，
$P_n\in\mathscr R$，且 $P_n(h,L)=V_n(L)$、$P_1=1/2$。
所用有限 $x$ 系数都有统一有限的 $L$ 次数界。
所以 $H=h$ 的代入在完备局部环中收敛，并保持逐系数整性。

下文所有形式指数只用于明确限定的有限次数。
没有在特征 $p$ 中定义越过 $p!$ 的无限指数。

## Proof Strategy

第二端点需要非内部块的 $h^m$ 修正，而不只是它的普通剩余。
先将真实块与一个形式 $H$ 的单位三角模型比较，准确控制被模型省略的
$pV_p$ 初值和 $p$ 倍阶乘余项。随后计算实际传播子的移位缺陷与配对缺陷。
用有限 action 的非驻值 Euler 身份把端点改写为低／高模态的配对和，
其中一阶缺陷整个配对消失，第二阶的两项分别为 $2-L^m$ 和 $L^m$。
这才给出首个非零常数 $2$。

## Dependency Map

1. 已接受低块和新块的形式阶乘桥给出真实／形式比较，误差至少 $M-m$。
2. 真实 Chebyshev 传播子的两种缺陷给出 $H^m$ 修正和 $H^{2m}$ 配对层。
3. 参数导数的 Jacobi 方程给出非内部块的准确 $h^m$ 修正。
4. 非驻值有限 action 身份把 $p\mathcal B_2$ 化成有精确误差界的配对和。
5. 已接受的低块系数和及其多项式导数计算首个非零层。
6. 真实 $d_{2p}$ 和常数单位剩余给出式 (5)—(7)。

## Proof

### Step 1. 实际块、阶乘桥及保留的内部初值

输入 2 已证明对 $0\le j<p$、$\alpha=1,2$，有

$$
p[x^{p+j}]e^{\alpha P(H,x)}
=-\frac\alpha2[x^j]e^{\alpha P(H,x)}
+pR_{\alpha,j}(H,L),\qquad R_{\alpha,j}\in\mathscr R.
\tag{11}
$$

这是在形式 $H$ 环中成立的系数式，不只是令 $H=0$ 后的结果。
其分母控制是：小于 $2p$ 阶的指数只遇到至多一个 $p$ 因子的阶乘；
清去该因子后，$p/(p+j)!\equiv-1/j!\pmod p$，而
$P(H,x)^p\equiv x^p/2\pmod{p,x^{2p}}$。
这里仅用 $P_1=1/2$，没有把 $L^p$ 替換成 $L$。

设实际高块和它的乘 $p$ 形式为

$$
R(x)=\sum_{n=p}^{2p-1}V_nx^n,\qquad
Y(x)=\sum_{j=0}^{p-1}Y_jx^j,\qquad Y_j=pV_{p+j}.
\tag{12}
$$

对指数小于 $2p$，特征零中精确有
$e^{\alpha(P+R)}=e^{\alpha P}(1+\alpha R)$。
因此清分母以后，高块只线性进入这些有限系数。
输入 2 给出 $Y_j\in\mathcal O^+[L]$，并且输入 1 给出更强初值界

$$
Y_0=pV_p\in h^{M-m}\mathcal O^+[L].
\tag{13}
$$

此处从未把实际 $V_p$ 置零。

令

$$
J(H,x)=\frac x2e^{P(H,x)}+2Lx^2e^{2P(H,x)}\pmod{x^p},
\tag{14}
$$

它只有正 $x$ 次数，所需系数均在 $\mathscr R$。
将实际 $p+j$ 模态递推乘 $p$，代入式 (11) 及精确高块线性式，
得到对 $1\le j<p$ 的准确关系

$$
d_{p+j}(h)Y_j+[x^j]J(h,x)Y(x)
=\frac12[x^j]J(h,x)+p\varepsilon_j(h,L),
\quad\varepsilon_j\in\mathscr R.
\tag{15}
$$

在出现负下标的最低几阶，该系数按零处理；式 (15) 仍成立。

### Step 2. 真实块与形式单位三角模型的准确比较

定义形式模型 $\mathscr Y(H,x)=\sum_{j=1}^{p-1}\mathscr Y_jx^j$，
其常数项为零，并要求

$$
d_{p+j}(H)\mathscr Y_j+[x^j]J(H,x)\mathscr Y(H,x)
=\frac12[x^j]J(H,x),\qquad 1\le j<p.
\tag{16}
$$

由于 $d_{p+j}(0)=-(p+j)^2$ 在该区间为 $p$-单位，
且 $J$ 没有常数项，式 (16) 唯一逐阶确定 $\mathscr Y_j\in\mathscr R$。
这只是一个内部证明模型，不是修改实际模态的定义。

对式 (15) 与式 (16) 相减，从常数项误差式 (13) 开始逐阶归纳。
每一步只乘整的低阶系数、除以单位 $d_{p+j}(h)$；额外来源
$p\varepsilon_j(h,L)$ 的赋值至少为 $M$。
于是全部所需系数满足

$$
\boxed{Y_j-\mathscr Y_j(h,L)
\in h^{M-m}\mathcal O^+[L],\qquad 0\le j<p,}
\tag{17}
$$

其中定义 $\mathscr Y_0=0$。
式 (17) 是省略模型初值的准确误差界，不能把它替换成实际 $V_p=0$。

### Step 3. 真实移位传播子及配对缺陷

在形式 $H$ 环中定义

$$
\Delta_j=d_{p+j}-d_j,\qquad
\delta_i=d_i-d_{2p-i}\quad(1\le i,j<p).
\tag{18}
$$

下列三个同余式在 $\mathbb F_p[[H]]$ 中成立：

$$
\Delta_j=2\chi jH^m+O(H^{m+1}),\qquad
\delta_i=4\chi iH^m+O(H^{m+1}),
\tag{19}
$$
$$
\boxed{\delta_i+\delta_{p-i}=4H^{2m}+O(H^{2m+1}).}
\tag{20}
$$

特别是式 (20) 消去整个低于 $2m$ 的配对缺陷，
不只是偶然消去单个 $H^m$ 系数。

为直接证明这些式子，在 $\mathbb F_p[[\eta]]$ 中取

$$
z=1+\eta,\qquad H=2-z-z^{-1}=-\eta^2/z,\qquad
T=z^p=1+\eta^p.
$$

该代入在 $\mathbb F_p[[H]]$ 上是单射。
真实 Chebyshev 身份给出

$$
\Delta_j=\frac{(T-1)(z^j-T^{-1}z^{-j})}{H},\qquad
\delta_i=\frac{(T^2-1)(T^{-2}z^i-z^{-i})}{H}.
\tag{21}
$$

分子首项分别为 $2j\eta^{p+1}$ 和 $4i\eta^{p+1}$，
故除以 $H$ 后的首项分别为 $-2j\eta^{p-1}$ 和 $-4i\eta^{p-1}$。
由于 $H^m$ 的首项为 $(-1)^m\eta^{p-1}$，得到式 (19)。
这些式子本来都是 $H$ 的多项式，故下一项至少为 $H^{m+1}$，
不会出现半整数 $H$ 次数。

对于配对和，先作准确因式分解：

$$
\begin{aligned}
H(\delta_i+\delta_{p-i})
&=(1+T^{-1}-T-T^{-2})z^i
 +(1+T-T^{-1}-T^2)z^{-i}\\
&=-\frac{(T-1)^2(T+1)}{T^2}(z^i+Tz^{-i}).
\end{aligned}
\tag{22}
$$

其除以 $H$ 后的首项为 $4\eta^{2p-2}$，
而 $H^{2m}$ 的首项就是 $\eta^{2p-2}$，证明式 (20)。

将上述形式模 $p$ 身份代入 $H=h$ 时，所有 $p$ 倍误差的赋值至少为
$M>2m$。因此式 (19)—(20) 同样给出实际 $h$ 进所需的逐系数同余，
其中 $O(h^r)$ 表示属于 $h^r\mathcal O^+$。

### Step 4. 非内部块的准确 $h^m$ 修正

令 $\mathcal D_Hx^j=d_j(H)x^j$，
$\mathcal D_H^{\rm sh}x^j=d_{p+j}(H)x^j$。
低块真实方程是

$$
\mathcal D_HP+\frac x2e^P+Lx^2e^{2P}=0\pmod{x^p}.
$$

对它作用 $\mathcal N$，利用 $\mathcal D_H$ 与 $\mathcal N$ 交换，得

$$
(\mathcal D_H+J)\mathcal NP=-J\pmod{x^p}.
$$

因此

$$
\mathscr Y^{(0)}=-\tfrac12\mathcal NP
\tag{23}
$$

是未移位方程 $(\mathcal D_H+J)\mathscr Y^{(0)}=J/2$ 的准确有限解。
式 (16) 与它相减，得到

$$
(\mathcal D_H^{\rm sh}+J)(\mathscr Y-\mathscr Y^{(0)})
=-(\mathcal D_H^{\rm sh}-\mathcal D_H)\mathscr Y^{(0)}
\pmod{x^p}.
\tag{24}
$$

在形式环中先模 $p$，由式 (19) 及单位三角性，差至少被 $H^m$ 整除。
其 $H^m$ 系数记为 $Y^{(1)}(x)\in\mathbb F_p[L][x]/(x^p)$，
常数项为零。令

$$
A(x)=1-x/2+(1-4L)x^2/16,\qquad U=-\log A,
\quad u_i=[x^i]U\ (i<p),
\quad J_0=\frac{x}{2A}+\frac{2Lx^2}{A^2}.
$$

这些有限系数的来源是输入 1 的平方传播子解。
取式 (24) 的 $H^m$ 系数，得到

$$
(-\mathcal N^2+J_0)Y^{(1)}=\chi\mathcal N^2U\pmod{x^p}.
\tag{25}
$$

它在正次数小于 $p$ 的范围有唯一零常数项解，因为每个 $-j^2$ 都非零。

为准确求这个修正，引入仅用于证明的幅度 $b$，取

$$
A_b(x)=1-bx/2+(b^2-4L)x^2/16,\qquad U(b,L,x)=-\log A_b(x).
$$

先在特征零作有限系数运算。平方传播子与加权参数身份分别为

$$
\mathcal N^2U=\frac{bx}{2}e^U+Lx^2e^{2U},\qquad
\mathcal NU=bU_b+2LU_L.
\tag{26}
$$

在 $b=1$ 处对第一式分别作参数导数，得到

$$
(-\mathcal N^2+J_0)U_b=-\frac{x}{2A},\qquad
(-\mathcal N^2+J_0)U_L=-\frac{x^2}{A^2}.
$$

所以式 (25) 的唯一有限解为

$$
\boxed{Y^{(1)}=-\chi(U_b+LU_L)|_{b=1}
=-\chi(\mathcal NU-LU_L).}
\tag{27}
$$

以上只约化小于 $p$ 阶的系数，所用阶乘均为单位；
参数导数没有改变实际固定参数的科学规范。

把式 (24) 的形式同余代回 $H=h$，再使用式 (17)。
因为 $M-m>m$，两种误差都在 $h^{m+1}$ 中，故对 $1\le j<p$ 有

$$
\boxed{
Y_j=-\frac j2V_j+h^mY^{(1)}_j+O(h^{m+1}).}
\tag{28}
$$

此处 $Y^{(1)}_j$ 可取任意整提升；换提升只改变所写误差。
这一步不是把只在 $H=0$ 正确的平方传播子当作全部实际分支。

### Step 5. 第二端点的非驻值有限 action 身份

用实际 $d_n(h)$ 定义一个取第 $2p$ 阶系数的有限泛函

$$
\Phi=[x^{2p}]\left(
\frac12V\mathcal D_hV+\frac b2xe^V+\frac L2x^2e^{2V}
\right)\bigg|_{b=1},
\tag{29}
$$

其中 $V$ 截断至 $2p-1$，在作参数偏导时先把各 $V_i$ 视为独立变量。
这里传播子仍来自本原 $p^a$ 次根，没有换成周期 $2p$ 的传播子。
对 $1\le i<2p$，在真实分支上

$$
\frac{\partial\Phi}{\partial V_i}
=\frac{d_i+d_{2p-i}}2V_{2p-i}
 +\frac12[x^{2p-i-1}]e^V+L[x^{2p-i-2}]e^{2V}
=\frac{d_i-d_{2p-i}}2V_{2p-i}.
$$

因此真实分支不是该截断泛函的临界点；这些缺陷项必须保留。
给 $V_i,b,L$ 权重 $i,1,2$，有限泛函权重为 $2p$。
精确加权 Euler 身份遂给出

$$
\mathcal B_2=-4p\Phi+
\sum_{i=1}^{2p-1}i(d_i-d_{2p-i})V_iV_{2p-i}.
\tag{30}
$$

先明确舍弃 action 项的合法赋值界。
低模 $V_i$ 整，非内部高模 $V_{p+j}$ 的赋值至少为 $-M$。
动能配对的非中央项至多是一个低模乘一个高模；传播子 $d_i$ 均整。
中央项含 $V_p^2$，保守下界为 $-2m>-M$。
势能只取到 $e^V$ 的第 $2p-1$ 阶和 $e^{2V}$ 的第 $2p-2$ 阶；
由输入 2 的有限指数桥，它们乘 $p$ 后整。
故整个 $\Phi$ 的逐系数赋值至少为 $-M$，从而
$v_h(p^2\Phi)\ge M>2m$。

式 (30) 乘 $p$，将 $i$ 与 $2p-i$ 配对。中央项的缺陷为零。
成对系数为 $2i-2p$；其中 $-2p$ 的部分赋值至少为 $M+m>2m$。
得到准确端点同余

$$
\boxed{
p\mathcal B_2
\equiv\sum_{i=1}^{p-1}2i\delta_iV_iY_{p-i}
\pmod{h^{2m+1}\mathcal O^+[L]}.}
\tag{31}
$$

所有式 (17) 的真实／形式误差也可以在此省略：
它们至少为 $M-m$，再乘缺陷 $\delta_i$ 的 $m$ 阶，达到 $M>2m$。
这说明即使在最小边界 $p=3,a=2$，$pV_p$ 的初值也没有遗漏同阶贡献。

### Step 6. 计算首个非零层，保留两项同阶抵消

记已接受的低块配对和为

$$
\mathcal A(L)=\sum_{i=1}^{p-1}i^2u_i u_{p-i}
=\frac{2-L^m}{2}\quad\text{于 }\mathbb F_p[L].
\tag{32}
$$

这是输入 1 式 (14) 的同一身份；$u_i$ 是它的 $V_i(0,L)$。
以下始终在完整多项式环 $\mathbb F_p[L]$ 中计算，
不限制 $L$ 为 $\mathbb F_p$ 的点，也不除以 $2-L^m$。

将式 (28) 代入式 (31)。零阶块 $-\mathcal NP/2$ 的贡献是

$$
-\sum_{i=1}^{p-1}i(p-i)\delta_iV_iV_{p-i}
\equiv\sum_{i=1}^{p-1}i^2\delta_iV_iV_{p-i}
\pmod{h^{2m+1}}.
$$

这里替换所丢项含 $p\delta_i$，赋值至少为 $M+m$。
再把 $i$ 与 $p-i$ 配对；$(p-i)^2-i^2$ 也是 $p$ 的倍数。
由式 (20)，这部分恰为

$$
\frac12\sum_{i=1}^{p-1}i^2(\delta_i+\delta_{p-i})V_iV_{p-i}
\equiv2h^{2m}\mathcal A(L)
=h^{2m}(2-L^m)\pmod{h^{2m+1}}.
\tag{33}
$$

式 (33) 一次排除了所有低于 $2m$ 的层，
不需要猜测逐个中间 $h$ 系数消失。

式 (28) 中 $h^mY^{(1)}$ 的贡献，使用式 (19)、式 (27)，为

$$
\begin{aligned}
h^{-2m}\sum_{i=1}^{p-1}2i\delta_iV_i h^mY^{(1)}_{p-i}
&\equiv8\chi\sum_{i=1}^{p-1}i^2u_iY^{(1)}_{p-i}\\
&=-8\sum_{i=1}^{p-1}i^2u_i
\bigl((p-i)u_{p-i}-L\partial_Lu_{p-i}\bigr).
\end{aligned}
\tag{34}
$$

三次权重和 $\sum_i i^3u_i u_{p-i}$ 在 $i\leftrightarrow p-i$ 下变号，
因 $p$ 为奇数而等于零。
又由同样的配对，
$\mathcal A'(L)=2\sum_i i^2u_i\partial_Lu_{p-i}$。
所以式 (34) 的剩余值是

$$
4L\mathcal A'(L)=-2mL^m=L^m
\quad\text{于 }\mathbb F_p[L].
\tag{35}
$$

最后等号只用 $2m=p-1$，不是用任何参数点方程。
式 (28) 的其余误差乘 $\delta_i$ 后至少为 $2m+1$。
将式 (33) 与式 (35) 合并，得到

$$
p\mathcal B_2\equiv h^{2m}\bigl((2-L^m)+L^m\bigr)
=2h^{2m}\pmod{h^{2m+1}\mathcal O^+[L]}.
\tag{36}
$$

由于 $2$ 在每个奇剩余特征中非零，式 (36) 同时证明了整性、
首个非零层恰为 $2m$，以及式 (4) 的常数剩余。

### Step 7. 实际第二内部模态及内部 forcing 互素

真实倍频身份给出

$$
d_{2p}=d_p(4+hd_p).
$$

输入 1 已接受 $d_p/h^{2m}\equiv-1\pmod h$，故

$$
\frac{d_{2p}}{h^{2m}}\equiv-4\pmod h.
\tag{37}
$$

从实际递推 $V_{2p}=\mathcal B_2/(2d_{2p})$ 与式 (4)、式 (37)，
得到式 (5)。全部系数先整，再作参数代入；
对任何局部代数整数 $L$，式 (4)、式 (5) 的剩余值仍是同样的非零常数。
这证明式 (6)，覆盖原来 $\bar L^m=2$ 的全部代数剩余根类，
也覆盖 $p=3$ 的对应边界类。

第一内部 forcing 的已接受规范为

$$
h^{-m}\mathcal B_1\in\mathcal O^+[L],\qquad
\overline{h^{-m}\mathcal B_1}=(-1)^{m+1}(2-L^m),
\quad\deg_L\mathcal B_1=m.
$$

其最高次系数为单位，除以该系数后是单首整多项式，
所以全部代数根均为局部整数。式 (4) 使 $\mathcal B_2$ 在任何这些根上非零，
故二者没有共同代数根，得到式 (7)。

若用原始 $\lambda$ 变量，两个内部 forcing 分别满足
$\mathcal B_k(L)=\rho^{kp-1}\mathcal B_{kp\mid p^a}(L/\rho)$，$k=1,2$。
非零标量和可逆线性变量替换保持互素性，故原变量中结论相同。
这仍只是同一个周期 $p^a$ 系统的两个内部 forcing 的结论。
证明完成。$\square$

## Exact Verification Actually Run

只核对本证明新增的自由符号恒等式，没有输入素数、分母或参数点清单。
以下四项均已精确运行通过：

- 自由 $b,L,x$ 的平方传播子有理身份；
- 加权参数导数 $\mathcal NU=bU_b+2LU_L$；
- 式 (27) 所用的 Jacobi 修正身份；
- 式 (22) 的配对传播子缺陷因式分解。

运行代码为

```python
import sympy as s

x, b, L, T, z = s.symbols('x b L T z', nonzero=True)
A = 1-b*x/2+(b*b-4*L)*x*x/16
U = -s.log(A)
N = lambda f: x*s.diff(f, x)
E = 1/A
J = b*x*E/2+2*L*x*x*E*E
assert s.factor(N(N(U))-b*x*E/2-L*x*x*E*E) == 0
assert s.factor(N(U)-b*s.diff(U,b)-2*L*s.diff(U,L)) == 0
correction = s.diff(U,b)+L*s.diff(U,L)
assert s.factor((-N(N(correction))+J*correction
                 +N(N(U))).subs(b,1)) == 0
first = 1+1/T-T-1/T**2
second = 1+T-1/T-T*T
assert s.factor(first*z+second/z
                +(T-1)**2*(T+1)*(z+T/z)/T**2) == 0
print('PASS free-symbol square-propagator identity, weighted parameter '
      'derivative, Jacobi correction, paired propagator defect')
```

这里检验的是有理函数恒等式；清分母以后为多项式身份。
在形式 $x$ 环中 $A(0)=1$，因此不排除 $b=0$、$L=0$ 等参数。
一般阶乘界、任意素数的配对和以及实际误差控制由上述证明承担，
没有从有限实例外推。

## Corrections or Missing Assumptions

- $h$ 在本稿始终是 $D_1$，不是周期 $2p$ 分母稿中的 $D_2$。
- 传播子符号是 $d_n=-D_n/h$。特别是式 (37) 的剩余为 $-4$，
  与式 (5) 的 $-1/4$ 一致。
- 人工取第 $2p$ 阶的泛函没有周期 $2p$ 的反射对称性；
  式 (30) 精确保留非驻值缺陷，不能移植已闭合周期 $2p$ 的 action。
- 不假设 $\bar L^m\ne2$，也没有在任何步骤除以该多项式。
- $pV_p$ 可以在极小边界与某个中间阶相遇，但端点再乘缺陷后其误差
  达到 $M>2m$；因此没有额外排除 $p=3,a=2$。

## Open Risks and Delivery Boundary

- 本稿准确版本仍需非作者检查完整实际／形式桥和端点取消，
  作者与主控的协作复算不是独立审查。
- 本件到第二内部模态为止。后续指数达到 $2p$ 后会出现多个高模乘积，
  不能把本次低于 $2p$ 的线性展开永久延用。
- 内部 $\mathcal B_1,\mathcal B_2$ 互素不是完整 $C_{p^a},Q_{p^a}$ 互素；
  没有完整首项的根分类、全实性或完整塔定理。
- 只新增本作者稿，不修改旧接受稿、入口、脚本、冻结记录或批次状态。
  没有素数／根扫描、正文估页、立项、PDF 或对外操作。
