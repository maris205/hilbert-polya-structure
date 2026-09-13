# Paper 30：第二阶乘带的形式／实际桥与两块耦合响应

日期：2026-09-07。作者：`p30_twist_leading_structure_probe`。
本轮全文读取并使用 `proof-writer`。本件是作者证明，不是非作者独审票。

## Claim

固定素数 $p\ge5$、整数 $a\ge2$ 及任意本原 $p^a$ 次根 $\zeta$，沿用

$$
h=2-\zeta-\zeta^{-1},\qquad \rho=-h,\qquad L=\rho\lambda,
\qquad m=(p-1)/2,\qquad M=p^{a-1}m,\qquad \chi=(-1)^{m+1}.
\tag{1}
$$

实际局部环为 $\mathcal O^+=\mathbb Z_p[h]$，$v_h(h)=1$、$v_h(p)=M\ge5m$。
使用已接受的同一实际分支

$$
d_n(h)V_n=-\frac12[x^{n-1}]e^V-L[x^{n-2}]e^{2V},\qquad
d_n(h)=-D_n/h,\qquad D_n=2-\zeta^n-\zeta^{-n}.
\tag{2}
$$

本件为已接受的两块

$$
Y^{\rm act}(x)=\sum_{j=0}^{p-1}pV_{p+j}x^j,\qquad
Z^{\rm act}(x)=\sum_{j=0}^{p-1}p^2V_{2p+j}x^j
\tag{3}
$$

证明以下精细桥，不重新证明这些块的普通剩余定理。

1. 令 $P(H,x)$ 为低块的形式整分支。对 $\alpha=1,2$、$0\le j<p$，
存在 $R^{(2)}_{\alpha,j}\in\mathbb Z_{(p)}[L][[H]]$，使

$$
\boxed{p^2[x^{2p+j}]e^{\alpha P(H,x)}
=\frac{\alpha^2}{8}[x^j]e^{\alpha P(H,x)}+pR^{(2)}_{\alpha,j}(H,L).}
\tag{4}
$$

误差是 $p$ 倍形式整数级数，不是只在 $H=0$ 正确或未经控制的 $H$ 误差。

2. 在下文定义的单位三角模型中，取零常数项的 $\mathscr Y,\mathscr Z$，满足

$$
(\mathcal D_1+J)\mathscr Y=J/2,\qquad
(\mathcal D_2+J)\mathscr Z=-K(\mathscr Y-1/2)^2\pmod{x^p}.
\tag{5}
$$

它们属于 $\mathbb Z_{(p)}[L][[H]][x]/(x^p)$，且全部所需实际系数满足

$$
\boxed{Y^{\rm act}-\mathscr Y(h,x),\quad
Z^{\rm act}-\mathscr Z(h,x)
\in h^{M-m}\mathcal O^+[L][x]/(x^p).}
\tag{6}
$$

模型的零初值只是证明工具，实际的 $pV_p$ 和 $p^2V_{2p}$ 均保留。

3. 设 $\mathcal N=x\partial_x$，$\Delta_k=\mathcal D_k-\mathcal D_0$，并记

$$
Y^{(0)}=-\frac12\mathcal NP,\qquad Z^{(0)}=\frac18\mathcal N^2P,\qquad
y=\mathscr Y-Y^{(0)},\qquad z=\mathscr Z-Z^{(0)},\qquad
Q=z+\frac12\mathcal Ny.
\tag{7}
$$

则有准确的形式耦合恒等式

$$
\boxed{(\mathcal D_2+J)Q
=(2\Delta_1-\Delta_2)Z^{(0)}
+\frac12(\Delta_2-\Delta_1)\mathcal Ny-Ky^2\pmod{x^p}.}
\tag{8}
$$

这保留所有 $H$ 阶，并非只保留最低修正。

4. 在形式环先模 $p$。令 $q=(1-4L)/16$、$A=1-x/2+qx^2$、$U=-\log A$，
$U$ 只在次数低于 $p$ 的系数上约化。设 $S=\mathcal N-L\partial_L$，则

$$
y=H^mY^{(1)}+O(H^{m+1}),\qquad
z=H^mZ^{(1)}+O(H^{m+1}),
\tag{9}
$$
$$
\boxed{Y^{(1)}=-\chi SU,\qquad Z^{(1)}=-\tfrac12\mathcal NY^{(1)},}
\tag{10}
$$
$$
\boxed{Q=H^{2m}Q^{(2)}+O(H^{2m+1}),\qquad
Q^{(2)}=\left(\tfrac12S^2+\tfrac14S\right)U.}
\tag{11}
$$

式 (11) 是组合响应 $Q$ 的准确首个可能层；不是宣称 $z$ 没有
$H^{m+1},\ldots,H^{2m-1}$ 修正，也不是宣称第三 forcing 在 $3m$ 层非零。
这些形式同余可按下文误差界转回实际 $h$。

## Status

式 (4)—(11) 与下文的实际误差推论：`PROVABLE AS STATED`。

本件确定可用于第三端点的模型精度和响应身份，不确定第三 forcing 的准确首个非零层。
对于 $p=3$ 不作本件高精度结论；其内部传播子及最小真共振边界另行处理。

## Assumptions and Inputs

本轮全文读取以下接受输入；只调用列明的已证事实，不重开旧证明：

- [第二阶乘带处置](PAPER30_TWIST_PRIME_POWER_SECOND_FACTORIAL_BLOCK_DISPOSITION_20260907.md)；
- [第二阶乘带作者稿](PAPER30_TWIST_PRIME_POWER_SECOND_FACTORIAL_BLOCK_PROBE_V1_20260907.md)，475 行；
- [第二内部 forcing 作者稿](PAPER30_TWIST_PRIME_POWER_SECOND_INTERNAL_FORCING_PROBE_V1_20260907.md)，640 行。

| 输入 | SHA256 |
| --- | --- |
| SECOND_FACTORIAL_BLOCK_DISPOSITION | `e3f46a7725f7f6354695c30613219a9df67f526ab559a832f0f2e9bbfe21c213` |
| SECOND_FACTORIAL_BLOCK V1 | `3ff45f425669adbd012245f5cf605083a72e3cccb131cc6469f787cc58920e04` |
| SECOND_INTERNAL_FORCING V1 | `278ce73d9844c8a30b93b8952b8a3a178aa577f1c808fce48c333be721c97f15` |

具体调用：低块 $V_i$ 在 $1\le i<p$ 时逐系数整；$V_1=1/2$ 精确；
两块式 (3) 的全部系数整；以及真实初值高度

$$
Y^{\rm act}_0=pV_p\in h^{M-m}\mathcal O^+[L],\qquad
Z^{\rm act}_0=p^2V_{2p}\in h^M\mathcal O^+[L].
\tag{12}
$$

第二个高度只使用 $pV_{2p}$ 整，不需要它的准确剩余 $-1/4$。
还调用低块的形式整性、已接受的第一阶乘带形式桥，以及低块在 $H=0$
的有限平方传播子 $U=-\log A$。不调用任何第三 forcing 非零层候选。

## Notation

使用真实 Chebyshev 传播子多项式

$$
C_0(H)=2,\quad C_1(H)=2-H,\quad
C_{n+1}(H)=(2-H)C_n(H)-C_{n-1}(H),\quad
d_n(H)=\frac{C_n(H)-2}{H}.
\tag{13}
$$

这里 $C_n(H)$ 只是 Chebyshev 辅助记号，不是系统首项 $C_{r,s}$。
令 $\mathscr R=\mathbb Z_{(p)}[L][[H]]$，
$P(H,x)=\sum_{i=1}^{p-1}P_i(H,L)x^i$ 为已接受的形式低块，
$P_i(h,L)=V_i(L)$、$P_1=1/2$。定义有限整系数

$$
J=\frac x2e^P+2Lx^2e^{2P},\qquad
K=\frac x4e^P+2Lx^2e^{2P}\pmod{x^p}.
\tag{14}
$$

所有指数在这里仅取严格低于 $p$ 的所需系数，故 $J,K\in\mathscr R[x]/(x^p)$，
且均无常数项。对 $1\le j<p$ 定义

$$
\mathcal D_kx^j=d_{kp+j}(H)x^j\quad(k=0,1,2),\qquad
\Delta_k=\mathcal D_k-\mathcal D_0.
\tag{15}
$$

这些算子只在正次数子空间使用，模型常数项另指定为零。
没有对实际内部常数项施加模型方程。所有 $\mathcal D_k$ 与 $\mathcal N$ 交换。
因 $d_{kp+j}(0)=-(kp+j)^2$ 是 $p$-单位，每个正次数对角元在 $\mathscr R$ 中可逆。

每个固定 $x$ 次数涉及的参数多项式次数有统一有限界，
由低块递推、有限指数及逐阶单位除法得到。
因此 $H=h$ 在完备局部环中的代入收敛且保持逐系数整性。
所有负下标的 $x$ 系数定义为零。形式 $O(H^r)$ 均在先模 $p$ 后解释；
实际 $O(h^r)$ 则指 $h^r\mathcal O^+[L]$ 的逐系数误差。

## Proof Strategy and Dependency Map

1. 在未代入 $H$ 的环中清理完整第二阶乘带，证明式 (4) 的 $pR$ 误差。
2. 保留旧高模线性、新高模线性及旧高模二次项，得到实际有限系数桥和两个准确递推。
3. 以真实初值和 $p$ 倍误差作单位三角比较，得到式 (6)，并说明端点乘缺陷后的精度。
4. 用低块的缩放导数求未移位基解；借助交换子准确消去线性交叉项，证明式 (8)。
5. 用真实 Chebyshev 移位的一阶与二阶差分控制 $y,Q$ 的最低 $H$ 层。
6. 以幅度参数的加权导数解出 $Y^{(1)},Q^{(2)}$，再合法转回实际 $h$。

主控也分别导出了同一组合响应公式，属于共同推导。
另有作者协作的有界身份核对；这些不替代绑定冻结稿的非作者审查。

## Proof

### Step 1. 第二阶乘带在形式环中的完整系数桥

写 $E_{\alpha,N}(H,L)=[x^N]e^{\alpha P(H,x)}$。
当 $N<3p$ 时，只用到 $k!$、$k\le N<3p<p^2$；
阶乘至多含两个 $p$ 因子，故 $p^2E_{\alpha,N}\in\mathscr R$。
$N<2p$ 时 $pE_{\alpha,N}$ 整，$N<p$ 时 $E_{\alpha,N}$ 整。

对 $k=2p+r$、$0\le r<p$，在 $\mathbb Z_{(p)}$ 中清掉两个 $p$ 因子，再模 $p$，得到

$$
\frac{p^2}{(2p+r)!}\equiv
\frac{1}{2((p-1)!)^2r!}=\frac1{2r!}\pmod p.
\tag{16}
$$

最后一步是非零剩余类的逆元配对给出的 $(p-1)!=-1$。
$k<2p$ 的指数项乘 $p^2$ 后全在 $p\mathscr R$ 中。
在 $\mathscr R/p\mathscr R=\mathbb F_p[L][[H]]$ 中应用 Frobenius，
因为 $P_1(H,L)=1/2$ 精确，有

$$
P(H,x)^p=\frac{x^p}{2}+O(x^{2p}),\qquad
P(H,x)^{2p}=\frac{x^{2p}}4+O(x^{3p})\pmod p.
$$

这保留形式变量 $H$，不将 $H$ 置零，也不把 $L^p$ 替换成 $L$。
又因整数 $\alpha=1,2$ 满足 $\alpha^{2p}=\alpha^2$，故

$$
p^2e^{\alpha P(H,x)}
\equiv\frac{\alpha^2}{8}x^{2p}
\sum_{r=0}^{p-1}\frac{(\alpha P(H,x))^r}{r!}
\pmod{p,x^{3p}}.
\tag{17}
$$

乘去 $x^{2p}$ 后只取低于 $p$ 的系数；该有限和可合法写成相应的 $e^{\alpha P}$ 系数。
式 (17) 的差已经在整环 $\mathscr R$ 中，其模 $p$ 为零，因而属于 $p\mathscr R$。
这就证明式 (4)，而不是只证明一个模 $h$ 的剩余身份。

同一低块的已接受第一条形式桥为

$$
pE_{\alpha,p+r}=-\frac\alpha2E_{\alpha,r}+pR^{(1)}_{\alpha,r},
\qquad 0\le r<p,\qquad R^{(1)}_{\alpha,r}\in\mathscr R.
\tag{18}
$$

对 $-p\le r<0$，仍可用式 (18)，只须将 $E_{\alpha,r}$ 定义为零，
并取 $R^{(1)}_{\alpha,r}=E_{\alpha,p+r}\in\mathscr R$。
当 $r<-p$ 时，所涉两个系数均为零，取 $R^{(1)}_{\alpha,r}=0$ 即可。
式 (4) 在 $j=-1,-2$ 也可按相同形式使用：右侧主项为零，
而 $p^2E_{\alpha,2p+j}\in p\mathscr R$。
这些负下标约定不会删掉真实系数；该真实值被准确保留在 $p$ 倍误差中。

### Step 2. 实际四项有限桥及两块耦合递推

把实际分支写成 $V=P(h,x)+R_1+R_2$，其中

$$
R_1=\sum_{n=p}^{2p-1}V_nx^n=\frac{x^p}{p}Y^{\rm act},\qquad
R_2=\sum_{n=2p}^{3p-1}V_nx^n=\frac{x^{2p}}{p^2}Z^{\rm act}.
$$

严格小于 $3p$ 的次数中，特征零准确身份是

$$
e^{\alpha V}=e^{\alpha P(h,x)}
\left(1+\alpha R_1+\alpha R_2+\frac{\alpha^2}{2}R_1^2\right)
\pmod{x^{3p}}.
\tag{19}
$$

高模立方及 $R_1R_2$ 从 $x^{3p}$ 起，先按次数舍去。
旧高模的二次项完整保留；其中包含真实内部模式 $V_p$。

将式 (19) 乘 $p^2$，取 $x^{2p+j}$ 系数，$-2\le j<p$。
低块用式 (4)，贡献主项 $\alpha^2E_{\alpha,j}/8$，误差属于 $p\mathcal O^+[L]$。
旧高模线性项逐项写成

$$
\alpha\sum_{k=0}^{p-1}Y^{\rm act}_k\,
pE_{\alpha,p+j-k}(h,L).
$$

用式 (18) 及负下标约定，主项为
$-\alpha^2[x^j]e^{\alpha P(h,x)}Y^{\rm act}/2$。
其误差是 $p$ 乘整的 $Y^{\rm act}_k$ 与整系数的有限和，故仍在 $p\mathcal O^+[L]$ 中。
新高模线性项准确为 $\alpha[x^j]e^{\alpha P(h,x)}Z^{\rm act}$；
旧高模二次项准确为 $\alpha^2[x^j]e^{\alpha P(h,x)}(Y^{\rm act})^2/2$。
后两者只取低于 $p$ 的指数系数，无新增阶乘分母。
合并得

$$
\boxed{
p^2[x^{2p+j}]e^{\alpha V}
=[x^j]e^{\alpha P(h,x)}
\left(\alpha Z^{\rm act}+\frac{\alpha^2}{2}(Y^{\rm act}-1/2)^2\right)
+p\epsilon^{(2)}_{\alpha,j},\qquad
\epsilon^{(2)}_{\alpha,j}\in\mathcal O^+[L].}
\tag{20}
$$

误差可明确写成式 (4)、式 (18) 的形式余项在 $H=h$ 处的值，
及它们与实际 $Y^{\rm act}_k$ 的有限线性组合；没有未知非整因子。
第一块在所需的 $-1\le j<p$ 范围也有已接受的对应桥

$$
p[x^{p+j}]e^{\alpha V}
=\alpha[x^j]e^{\alpha P(h,x)}(Y^{\rm act}-1/2)
+p\epsilon^{(1)}_{\alpha,j},\qquad
\epsilon^{(1)}_{\alpha,j}\in\mathcal O^+[L].
\tag{21}
$$

将式 (20)—(21) 代入真实递推 (2)，对 $1\le j<p$ 得

$$
d_{p+j}(h)Y^{\rm act}_j+[x^j]J(h)Y^{\rm act}
=\tfrac12[x^j]J(h)+p\varepsilon^{(1)}_j,
\tag{22}
$$
$$
d_{2p+j}(h)Z^{\rm act}_j+[x^j]J(h)Z^{\rm act}
=-[x^j]K(h)(Y^{\rm act}-1/2)^2+p\varepsilon^{(2)}_j,
\tag{23}
$$

其中所有 $\varepsilon^{(k)}_j\in\mathcal O^+[L]$。
式 (23) 保留了旧高块平方与旧高块乘第一阶乘带生成的交叉项，
并未将两个块视为互不影响的独立线性响应。

### Step 3. 单位形式模型、真实初值与实际误差

因 $J,K$ 无常数项及每个正次数 $d_{kp+j}(H)$ 为单位，
式 (5) 先逐阶唯一确定 $\mathscr Y\in\mathscr R[x]/(x^p)$，
然后其平方驱动再逐阶唯一确定 $\mathscr Z$。
两个模型常数项均定义为零，属于证明内部的辅助规范。

记 $E=M-m$。式 (12) 给 $Y^{\rm act}_0\in h^E\mathcal O^+[L]$、
$Z^{\rm act}_0\in h^M\mathcal O^+[L]\subset h^E\mathcal O^+[L]$。
先从式 (22) 减去第一模型在 $H=h$ 的方程。
每个正次数只使用已知低阶差、整系数和赋值至少 $M$ 的额外误差，
再除以单位。由初值归纳，$Y^{\rm act}-\mathscr Y(h)\in h^E$。

对于第二块，平方之差准确分解为

$$
(Y^{\rm act}-1/2)^2-(\mathscr Y(h)-1/2)^2
=(Y^{\rm act}-\mathscr Y(h))(Y^{\rm act}+\mathscr Y(h)-1).
\tag{24}
$$

第二因子整，故该差在 $h^E$ 中；没有需要额外除以 $p$ 的因子。
从式 (23) 减去第二模型方程，用同样的逐阶单位除法及真实 $Z_0$ 高度，
得到第二个差也在 $h^E$ 中，证明式 (6)。

这一界还适用于两块的任意有限整系数多项式组合，
因为多项式相减可逐因子抽出至少一个块的差。
特别地，若端点中的某项再乘至少 $h^m$ 的实际传播子缺陷，
模型替换误差至少为

$$
E+m=M.
\tag{25}
$$

因此在 $p\ge5$ 范围，模型误差不影响任何严格低于 $M$ 的端点层，
包括 $3m$ 和 $4m$ 层。这个陈述以相应端点系数确实含 $h^m$ 缺陷为前提；
本件不据此省略端点 action 或其他尚未核定赋值的项。
未乘缺陷时只能使用原始的 $M-m$ 误差，不能擅自提升到 $M$。

### Step 4. 未移位基解与准确耦合消元

记 $\mathcal D=\mathcal D_0$、$F=xe^P/2+Lx^2e^{2P}$。
低块精确满足 $\mathcal DP+F=0\pmod{x^p}$。
对它作用 $\mathcal N$，得到

$$
(\mathcal D+J)\mathcal NP=-J.
\tag{26}
$$

因为 $\mathcal D$ 与 $\mathcal N$ 交换，且
$\mathcal NF=J(1+\mathcal NP)$。
另有准确身份

$$
\mathcal NJ=2K(1+\mathcal NP).
\tag{27}
$$

再对式 (26) 作用 $\mathcal N$，用式 (27)，得到

$$
(\mathcal D+J)\mathcal N^2P=-2K(1+\mathcal NP)^2.
$$

因此式 (7) 的基解满足

$$
(\mathcal D+J)Y^{(0)}=J/2,\qquad
(\mathcal D+J)Z^{(0)}=-K(Y^{(0)}-1/2)^2.
\tag{28}
$$

这些身份使用完整形式低块 $P(H,x)$，不把它替换成只在 $H=0$ 正确的 $U$。
设 $B_0=Y^{(0)}-1/2$，从模型式 (5) 减去式 (28)，得到

$$
(\mathcal D_1+J)y=-\Delta_1Y^{(0)},
\tag{29}
$$
$$
(\mathcal D_2+J)z=-\Delta_2Z^{(0)}-2KB_0y-Ky^2.
\tag{30}
$$

现在对式 (29) 作用 $\mathcal N$，并把传播子改写成 $\mathcal D_2$：

$$
(\mathcal D_2+J)\mathcal Ny
=-\Delta_1\mathcal NY^{(0)}-(\mathcal NJ)y
+(\Delta_2-\Delta_1)\mathcal Ny.
\tag{31}
$$

这里 $\mathcal N(Jy)=J\mathcal Ny+(\mathcal NJ)y$，符号与系数均由该乘积法则确定。
把式 (31) 的一半加到式 (30)。由
$\mathcal NY^{(0)}=-4Z^{(0)}$ 和 $\mathcal NJ=-4KB_0$，
两个线性 $B_0y$ 交叉项准确相消，余式正是式 (8)。
其中 $-Ky^2$ 与传播子二阶差分仍保留，不能在二阶响应中舍去。

### Step 5. 真实传播子的两种移位差分

以下先在模 $p$ 的形式环工作。取 $t=1+\eta$，
$H=2-t-t^{-1}=-\eta^2/t$、$T=t^p=1+\eta^p$。
将 $\mathbb F_p[[H]]$ 代入 $\mathbb F_p[[\eta]]$ 是单射。
由真实 Chebyshev 身份，对 $1\le j<p$ 有

$$
\Delta_1(j)=\frac{(T-1)(t^j-T^{-1}t^{-j})}{H},
\tag{32}
$$
$$
(2\Delta_1-\Delta_2)(j)
=-\frac{(T-1)^2}{H}(t^j+T^{-2}t^{-j}).
\tag{33}
$$

式 (32) 的分子首项为 $2j\eta^{p+1}$，除以 $H$ 后为
$-2j\eta^{p-1}$，而 $H^m$ 首项为 $(-1)^m\eta^{p-1}$。
式 (33) 的首项为 $2\eta^{2p-2}$，与 $2H^{2m}$ 相同。
这些差分本来就是 $H$ 多项式，所以下一个可能次数分别至少为 $m+1$ 和 $2m+1$。
于是作为正次数对角算子，有

$$
\Delta_1=2\chi H^m\mathcal N+O(H^{m+1}),\qquad
2\Delta_1-\Delta_2=2H^{2m}I+O(H^{2m+1}),
\tag{34}
$$
$$
\Delta_2-\Delta_1=2\chi H^m\mathcal N+O(H^{m+1}).
\tag{35}
$$

最后一式由前两式相减得到，$I$ 是恒等算子。
式 (29) 的单位三角性给出 $y\in H^m$。
式 (8) 的三个驱动分别在 $H^{2m}$、$H^{2m}$、$H^{2m}$ 中，
故同样的单位三角性给出 $Q\in H^{2m}$。
这一次排除 $Q$ 所有低于 $2m$ 的层，不是逐个猜测中间系数取消。

令 $J_0=x/(2A)+2Lx^2/A^2$、$K_0=x/(4A)+2Lx^2/A^2$，
$\mathcal L_0=-\mathcal N^2+J_0$。式 (29) 的 $H^m$ 系数满足

$$
\mathcal L_0Y^{(1)}=\chi\mathcal N^2U.
\tag{36}
$$

因 $Q=z+\mathcal Ny/2\in H^{2m}$，式 (10) 的第二关系已经成立。
取式 (8) 的 $H^{2m}$ 系数，得

$$
\mathcal L_0Q^{(2)}
=\frac14\mathcal N^2U+\chi\mathcal N^2Y^{(1)}-K_0(Y^{(1)})^2.
\tag{37}
$$

这两个方程均在正次数小于 $p$ 时有唯一零常数项解，因为对角元 $-j^2$ 为单位。
没有将该唯一性延伸到 $j=p$。

### Step 6. 完整参数的第一响应与组合二阶响应

引入仅用于证明的幅度参数 $b$，取

$$
A_b=1-bx/2+(b^2-4L)x^2/16,\qquad U_b^{\rm fam}=-\log A_b,
\qquad \mathcal T=b\partial_b+L\partial_L.
$$

为避免混淆，这里的 $U_b^{\rm fam}$ 表示整个参数族，不表示一次偏导。
以下本节暂写 $\widetilde U=U_b^{\rm fam}$、$\widetilde E=A_b^{-1}$，并令

$$
\widetilde F=bx\widetilde E/2+Lx^2\widetilde E^2,
\quad\widetilde J=bx\widetilde E/2+2Lx^2\widetilde E^2,
\quad\widetilde K=bx\widetilde E/4+2Lx^2\widetilde E^2,
\quad\widetilde{\mathcal L}=-\mathcal N^2+\widetilde J.
$$

平方传播子及加权参数身份为

$$
\mathcal N^2\widetilde U=\widetilde F,\qquad
\mathcal N\widetilde U=b\partial_b\widetilde U+2L\partial_L\widetilde U.
\tag{38}
$$

它们可直接代入 $A_b$ 验证。设 $f=\mathcal T\widetilde U$。
对第一式用 $\mathcal T$ 求导：显含的两个幅度项各增加一次自身，
通过 $\widetilde U$ 的部分给 $\widetilde J f$，故

$$
\widetilde{\mathcal L}f=-\widetilde F,
\qquad \mathcal N^2f=\widetilde Jf+\widetilde F.
\tag{39}
$$

式 (38) 还给 $f=(\mathcal N-L\partial_L)\widetilde U$。
因此式 (36) 的唯一解是
$Y^{(1)}=-\chi f|_{b=1}=-\chi SU$，证明式 (10) 的第一关系。

继续对式 (39) 的第一式作用 $\mathcal T$。
有 $\mathcal T\widetilde J=\widetilde J+2\widetilde Kf$，
$\mathcal T\widetilde F=\widetilde F+\widetilde Jf$，从而

$$
\widetilde{\mathcal L}(\mathcal T f)
=-\widetilde F-2\widetilde Jf-2\widetilde Kf^2.
\tag{40}
$$

把式 (40) 的一半加到式 (39) 的四分之一，得到

$$
\widetilde{\mathcal L}\left(\frac12\mathcal T f+\frac14f\right)
=-\frac34\widetilde F-\widetilde Jf-\widetilde Kf^2
=\frac14\mathcal N^2\widetilde U-\mathcal N^2f-\widetilde Kf^2.
\tag{41}
$$

取 $b=1$、$Y^{(1)}=-\chi f$、$\chi^2=1$，右边正是式 (37) 的驱动。
所以 $Q^{(2)}=(\mathcal T^2\widetilde U/2+\mathcal T\widetilde U/4)|_{b=1}$。
加权身份 (38) 在再用 $\mathcal T$ 求导后仍成立，因为相关微分算子交换，
故也可写成式 (11) 的 $S$ 表达式。

本节先在特征零作代数导数。$f,\mathcal T f$ 以及 $\mathcal N^2\widetilde U$
都是分母仅含 $2$ 的幂与 $A_b$ 的幂的有理式，$A_b(0)=1$。
因此它们在所有奇素数下逐系数整，可以先约化再取所需有限次数。
没有在特征 $p$ 中对非整的无限对数系数直接取模，也没有除以参数多项式。
所以 $L=0$、$q=0$ 及旧内部 forcing 的全部代数剩余根类无需排除。

### Step 7. 从形式响应转回实际块，保留精度边界

式 (34)—(37) 在形式环中先模 $p$ 成立。
取任意整提升，代入 $H=h$ 时 $p$ 倍余项的赋值至少为 $M$。
再加上式 (6) 的实际模型比较误差，得到

$$
Y^{\rm act}=-\tfrac12\mathcal NP(h,x)+h^mY^{(1)}+O(h^{m+1}),
\tag{42}
$$
$$
Z^{\rm act}=\tfrac18\mathcal N^2P(h,x)+h^mZ^{(1)}+O(h^{m+1}).
\tag{43}
$$

这里 $M-m\ge4m>m$，所以省略的真实初值确实在所写误差之外。
更强地，定义真实组合

$$
Q^{\rm act}=Z^{\rm act}-\tfrac18\mathcal N^2P(h,x)
+\tfrac12\mathcal N\bigl(Y^{\rm act}+\tfrac12\mathcal NP(h,x)\bigr).
\tag{44}
$$

则 $Q^{\rm act}-Q(h,x)\in h^{M-m}$，且

$$
\boxed{Q^{\rm act}=h^{2m}Q^{(2)}+O(h^{2m+1}).}
\tag{45}
$$

这一式没有把 $Y^{\rm act}$ 截断为只剩 $h^m$ 首项：
式 (44) 保留它的全部真实中间修正。
需要高于式 (45) 精度时，应继续使用准确形式方程 (8) 和误差 (6)，
不能把 $O(h^{2m+1})$ 无理由改为 $O(h^{3m})$ 或更高。
乘端点的 $h^m$ 缺陷后，式 (45) 只保证确定到 $3m$ 层；
要确定 $4m$ 层还需继续计算相应响应或证明额外的准确取消。
证明完成。$\square$

## Exact Verification Actually Run

使用自由符号 $b,L,x$ 及 Step 6 中的 $A_b$，实际精确核对以下五项：

$$
\mathcal N\widetilde J-2\widetilde K(1+\mathcal N\widetilde U),\qquad
\widetilde{\mathcal L}f+\widetilde F,
$$
$$
\widetilde{\mathcal L}(\mathcal T f)+\widetilde F
+2\widetilde Jf+2\widetilde Kf^2,
$$
$$
\widetilde{\mathcal L}\left(\tfrac12\mathcal T f+\tfrac14f\right)
-\left(\tfrac14\mathcal N^2\widetilde U-\mathcal N^2f-\widetilde Kf^2\right),
\qquad \mathcal T\widetilde U-(\mathcal N-L\partial_L)\widetilde U.
$$

通分后的五个残差均严格为零。实际输出：
`EXACT_PASS full-parameter second-response and weighted derivative identities; residuals = [0, 0, 0, 0, 0]`。
这些只核对新自由有理身份；一般阶乘桥、单位递推、真实初值及实际误差高度由证明承担。
没有素数样本、本原根、分母或参数根扫描。

## Corrections or Missing Assumptions

- 第二阶乘带桥中的低块保留完整 $H$ 依赖，误差准确在 $p\mathscr R$ 中。
- 模型误差原始高度是 $M-m$，不是未经证明的 $M$；后者需要再乘 $m$ 阶端点缺陷。
- 基解 $Z^{(0)}=\mathcal N^2P/8$ 与首层关系 $Z^{(1)}=-\mathcal NY^{(1)}/2$
  的系数不同；式 (7)—(8) 明确保留这个区别。
- $Q^{(2)}$ 是组合响应，不应误写成 $z$ 自身的完整二阶系数。
- 没有额外参数排除条件，没有把真实内部模式置零。

## Open Risks and Delivery Boundary

- 第三 forcing 的准确首个非零层仍需其自身的 action、配对缺陷和全部同阶项证明。
  本件不预设 $3m$ 或 $4m$ 层非零，普通取消也不等于准确层已知。
- 精确模型可以继续提供更高响应，但本件只显式求出式 (10)—(11)；
  后续使用必须遵守 Step 7 的精度边界。
- 本件高精度主范围仅 $p\ge5$，不借用此处的 $M\ge5m$ 去处理 $p=3$。
- 不构造 $V_{3p}$，不宣称完整 $C_{r,p^a}$、简单性、全实根或 $C,Q$ 互素。
- 作者与主控的同推、作者协作检查和符号残差不算正式非作者独审，仍待绑定冻结稿的核查。
- 只新增本作者稿；既有接受稿、处置、入口、锁、脚本与他人文件均未改。
  无正文估页、立项、PDF、Route、对外写入或付费资源操作。
