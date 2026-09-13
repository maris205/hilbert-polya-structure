# Paper30：高参数分界系数的双阶乘方向证明

日期：2026-09-08。作者：主控。新作者稿，尚待非作者独立核查。
本件按 `formula-derivation` 固定两个真实端点，再按 `proof-writer` 证明它们的高度。

## Claim

对任意素数 $p\ge5$、整数 $a\ge2$，保持同一实际双谐波分支与规范，令

$$m=(p-1)/2,\quad M=p^{a-1}m,\quad D=p+m=3m+1,\quad e_*=M-D.$$

证明此前上半参数区间下边界的系数满足

$$\boxed{p[L^p]\mathcal B_3\in h^{2m}\mathcal O^+.}\tag{1}$$

这里 $[L^p]\mathcal B_3$ 不是最高 forcing 系数，也不是 $[L^p]U_{\rm cl}$。
它对应首一因子分解中的商指标 $p-m=m+1$。
本件不假定这一新下界层非零，也不把 $j=p$ 自动纳入只允许辅助幅度次数小于 $p$ 的证明。

条件应用另列：若同轮上半段证明经独审接受
$p[L^j]\mathcal B_3\in h^{2m}\mathcal O^+$ 对 $p<j\le D$，
则合并后 $u_r=[L^r]U_{\rm cl}$ 在 $m+1\le r\le p$ 满足
$v_h(u_r)\ge e_*+2m=M-m-1$。
该条件应用不是接受同轮其他作者稿的替代。

## Status

`PROVABLE AS STATED`；推导对象 `COHERENT AS STATED`。
以下证明式 (1) 不依赖同轮上半段稿的结论，必要的辅助支撑与有限恒等式均重新明示。
没有从少数素数的计算外推，也没有降低实际构造的科学要求。

## Assumptions and exact inputs

取本原 $p^a$ 次根 $\zeta$，令

$$h=2-\zeta-\zeta^{-1},\quad K^+=\mathbb Q_p(h),\quad
\mathcal O^+=\mathbb Z_p[h],\quad v_h(h)=1,\quad v_h(p)=M,$$
$$L=-h\lambda,\quad d_n(h)=(\zeta^n+\zeta^{-n}-2)/h,\quad
\chi=(-1)^{m+1}.$$

使用辅助幅度 $b$ 的齐次实际递推

$$d_nV_n(b)=-\frac b2[x^{n-1}]e^{V(b)}-L[x^{n-2}]e^{2V(b)},
\qquad1\le n<3p,$$
$$\mathcal B_3=-[x^{3p-1}]e^{V(1)}-2L[x^{3p-2}]e^{2V(1)}.\tag{2}$$

实际仍取 $b=1$。所有估值均指逐参数系数，未对局部域赋予实序。
只使用以下已接受证据的有关部分：

1. [第一内部结构](PAPER30_TWIST_PRIME_POWER_LOCAL_STRUCTURE_PROBE_V1_20260907.md)，
   式 (3)、(15)：实际 $h^mV_p(L)$ 整，及低形式 forcing 的完整身份
   $$\mathcal B_1(H,L)=\chi H^m(2-L^m)+H^{m+1}R(H,L)+pT(H,L),
   \quad R,T\in\mathbb Z_p[L][[H]].\tag{3}$$
   参数次数有统一有限界。这允许先在形式变量 $H$ 中微分，再作实际代入。
2. [最高项预临界证明](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_PRECRITICAL_PROOF_V1_20260908.md)，
   式 (13) 附近的准确 Chebyshev 倍角与同一纯偶规范。下文也核回缩放常数。
3. [当前接受处置](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_HIGH_AND_POSTCRITICAL_DISPOSITION_20260908.md)：
   仅在末尾条件应用中使用实际首一分解和既有高系数共同界，不用于证明式 (1)。

整数 Chebyshev 多项式记为
$C_n(H)=z^n+z^{-n}$、$H=2-z-z^{-1}$，$d_n(H)=(C_n(H)-2)/H$。
在实际 $n<3p$ 范围，唯一非单位传播子指标为 $p,2p$，二者高度为 $2m$。

## Notation and proof map

取 $t=bx$、$u=Lx^2/4$。单项式 $t^ku^r$ 的权重为 $k+2r$。
本件在下降封闭区域

$$0\le k\le p,\qquad k+2r<3p$$

工作；即对 $t^{p+1}$ 及超出权重窗口的项作截断。
这比 $t^p=0$ 的上半段证明多保留一条真实幅度带。
令 $\Theta=u\partial_u$、$\mathcal N=t\partial_t+2\Theta$、
$\mathcal S=t\partial_t+\Theta$。

由齐次性，准确目标是

$$[L^p]\mathcal B_3=-4^{-p}
\left([t^{p-1}u^p]e^V+8[t^pu^{p-1}]e^{2V}\right).\tag{4}$$

证明分别处理式 (4) 中沿 $u^p$ 和沿 $t^p$ 的两个正规化阶乘带。
策略如下：保留全部内部值的实际估值 → 用有严格误差的零初值辅助分支
→ 两个方向各自先清 $p$ 后约化 → 用 Chebyshev 移位与导数恒等式
→ 以第一 forcing 的 $H^m$ 整性消去两个边界端点。

## Proof

### Step 1. 零内部初值辅助分支与实际误差

在每个权重为 $p$ 或 $2p$ 的位置，将实际系数视为一个独立初值 $q_{n,k}$。
权重 $p$ 的允许 $k$ 是奇数 $1\le k\le p$；权重 $2p$ 的允许 $k$
是偶数 $0\le k\le p-1$。其他位置都用单位传播子作三角递推。
将全部这些初值指定为零，定义辅助分支 $\widetilde V$。
它不是实际分支；下面将定量比较两者。

由式 (3) 的实际初值整性及 $b,L$ 齐次性，全部第一次初值满足
$v_h(q_{p,k})\ge-m$。
纯偶第二次初值是 $W_p=[u^p]V$。其递推右端只用 $u$ 次数小于 $p$ 的整指数，
故 $v_h(q_{2p,0})\ge-2m$。

其余第二次初值的幅度次数为偶数 $2\le k\le p-1$。
求这些位置的 forcing 时，所需指数权重小于 $2p$，故不能含两个第一次内部值。
其 $t$ 次数小于 $p$、纯偶指数的 $u$ 次数小于 $p$；展开时两方向的阶乘均为单位。
在非内部位置按权重归纳，相关 forcing 系数的高度至少为 $-m$。
除以高度 $2m$ 的 $d_{2p}$ 后，得到

$$v_h(q_{p,k})\ge-m,\qquad v_h(q_{2p,k})\ge-3m.\tag{5}$$

纯偶 $k=0$ 保留前述更强界，但共同误差只需式 (5)。

在辅助分支中，所有同时满足 $k<p$、$r<p$ 的系数整。
为证明，先展开 $e^{\widetilde V}=e^W e^{\widetilde V-W}$，其中后因子每项至少含一个 $t$。
提取 $t^k$ 只需要阶乘至 $k!$；提取纯偶 $u^r$ 只需要至 $r!$。
它们都不含 $p$，非内部传播子为单位，内部初值为零，故权重归纳封闭。
在同一区域，所需指数系数也整。

新增的 $t^p$ 带本身不要求整；其阶乘分母正是下文要清除的对象。
但是它不会破坏实际／辅助差的共振多项式估值：
第一次内部值至少含一个 $t$，不能与幅度次数已为 $p$ 的辅助非整带相乘后仍落在 $k\le p$。
第二次内部值的权重为 $2p$，与 $t^p$ 带相乘的权重至少为 $3p$，也被排除。
纯偶 $u^p$ 辅助带同样从权重 $2p$ 开始，不能与任何第一次内部值相乘于当前窗口。

具体地，令 $V(q)$ 表示独立初值递推，$\Delta=V(q)-\widetilde V$。
$\Delta$ 从权重 $p$ 开始，所以在权重小于 $3p$ 时

$$e^{\alpha V(q)}-e^{\alpha\widetilde V}
=e^{\alpha\widetilde V}\left(\alpha\Delta+\frac{\alpha^2}{2}\Delta^2\right),
\qquad\alpha=1,2.\tag{6}$$

上述支撑保证每个包含 $q$ 的项所乘背景系数均来自整的区域。
再按权重作单位除法归纳，$\Delta$ 和式 (6) 的系数都是 $q$ 的整系数多项式；
其单项式仅可能是一次 $q$，或两个第一次内部 $q$ 的乘积。
代入实际初值，所有高度至少为 $-3m$，故目标区域中

$$p(e^{\alpha V}-e^{\alpha\widetilde V})\in
h^{M-3m}\mathcal O^+\subset h^{2m}\mathcal O^+.\tag{7}$$

最后包含使用 $M\ge5m$。因此式 (4) 的两个正规化端点可用辅助分支计算至模 $h^{2m}$。

### Step 2. 形式工作环及准确移位

以下先在 $\mathbb Z_p[[H]]$ 中建立整的低带和乘 $p$ 后整的高带，
再在 $\mathbb F_p[H]/(H^{2m})$ 中计算。所得等式的整数提升误差在 $p$ 中，
实际代入 $H=h$ 后高度至少为 $M\ge2m$，所以合法。
不在实际商环中定义一个未经证明良定义的 $h$ 微分。

令

$$S_n(H)=\frac{z^n-z^{-n}}{z-z^{-1}},\qquad
\lambda(H)=\chi H^m(4-H)^{m+1}.$$

整数 Chebyshev 身份 $C_n'(H)=-nS_n(H)$ 给

$$d_n(H)+Hd_n'(H)=-nS_n(H).\tag{8}$$

在特征 $p$ 下，$C_p=2-H^p$、$C_{2p}=2-4H^p+H^{2p}$，
加法公式给

$$d_{p+n}-d_n=\frac\lambda2S_n-H^{p-1}-\frac{H^p}2d_n,
\tag{9}$$
$$d_{2p+n}-d_n=\lambda(1-H^p/2)S_n
+(-2H^{p-1}+H^{2p-1}/2)(2+Hd_n).\tag{10}$$

例如式 (9) 的奇部因子是
$(z^p-z^{-p})(z-z^{-1})/(2H)=\chi H^m(4-H)^{m+1}/2$。
所以在本件工作环内，两个移位分别为 $\lambda S_n/2$ 与 $\lambda S_n$。
被舍项均从 $H^{p-1}=H^{2m}$ 开始。
公式适用于下文全部整数 $n$；用于三角解的相应对角元仍为单位。

### Step 3. 第一端点：沿 $u^p$ 的带

暂限制到 $t^p=0$ 子域。令 $w(H,t,u)$ 为权重小于 $p$ 的辅助低解。
它与实际低块相同，并且整；定义

$$F=\frac t2e^w+4ue^{2w},\qquad
J=\frac t2e^w+8ue^{2w},\qquad\mathcal Dw=-F,$$

其中 $\mathcal D(t^ku^r)=d_{k+2r}(H)t^ku^r$，对常数的辅助作用取零。
所有方程只在权重小于 $p$ 内使用。

在辅助分支的 $u$ 次数小于 $p$ 部分，先乘 $p$ 再约化指数。
每个所需单项式的指数因子总数小于 $2p$，
$p/(p+s)!\equiv-1/s!\pmod p$。
Frobenius 给低部分的 $p$ 次幂为 $u^p$，模 $t^p,u^{2p},H^{2m}$；
纯偶线性系数为 $4/(4-H)$，其 $p$ 次幂与 $1$ 的差从 $H^p$ 开始。
由此及单高带线性分解，定义平移后的正规化带
$$\tau(t,u)=\sum_{k+2r<p}p[t^ku^{p+r}]\widetilde V\,t^ku^r,$$
得到

$$p[t^ku^{p+r}]e^{\alpha\widetilde V}
=[t^ku^r]\alpha e^{\alpha w}(\tau-1),
\qquad k+2r<p,\quad\alpha=1,2.\tag{11}$$

这里 $\tau$ 是整系数带，按单位三角递推证明；其常数为零，因为纯偶第二内部初值指定为零。
含两个 $u^p$ 带的项从权重 $4p$ 开始，所涉背景低系数全部整。
因此式 (11) 没有对未整指数直接作特征 $p$ 约化。

高带方程为 $(\mathcal D_2+J)\tau=J$。
低块导数身份给 $(\mathcal D+J)\mathcal Nw=-J$。
再令 $Z=(H\partial_H-\mathcal S)w$，由式 (8) 和
$(\mathcal D+J)\mathcal Sw=-F$ 得

$$ (\mathcal D+J)Z=-(\mathcal D+H\mathcal D')w
=\mathcal N S_{\mathcal N}(H)w.\tag{12}$$

式 (10) 的移位与式 (12) 表明

$$\tau=-\mathcal Nw+\lambda Z\pmod{H^{2m}}.\tag{13}$$

余下的移位乘 $\lambda Z$ 含 $H^{2m}$；初值相同，各正权重对角元单位，故三角唯一性适用。
代回式 (11)：

$$p[t^ku^{p+r}]e^{\alpha\widetilde V}
=[t^ku^r]\left[-(\alpha+\mathcal N)e^{\alpha w}
+\lambda(H\partial_H-\mathcal S)e^{\alpha w}\right].\tag{14}$$

第一端点取 $\alpha=1,k=p-1,r=0$。基带乘子为 $p$，在工作环中为零。
置 $b(H)=[t^{p-1}]e^{w(H,t,0)}$。它准确等于 $-\mathcal B_1(H,0)$，
由式 (3) 得 $b(H)\in H^m\mathbb F_p[[H]]$。
所以剩余项
$\lambda(H\partial_H-(p-1))b(H)$ 属于 $H^{2m}$。
这证明

$$p[t^{p-1}u^p]e^{\widetilde V}\in h^{2m}\mathcal O^+.\tag{15}$$

### Step 4. 第二端点：新增 $t^p$ 阶乘带

现在保留 $t^p$，并限制 $u$ 次数小于 $p$。
把辅助分支分为 $T+t^pB$，其中 $T$ 的 $t$ 次数小于 $p$，全部所需系数整。
记 $W=T|_{t=0}$、$F_2=e^{2W}$、$\xi=pB$。

对 $0\le r<p$，$[t^pu^r]e^{\alpha T}$ 至多用 $p+r<2p$ 个指数因子。
先清一个阶乘 $p$ 后，Frobenius 的唯一相关项是
$T^p=t^p/2\pmod{u^p,t^{p+1}}$；$T$ 的线性 $t$ 系数常数恰为 $1/2$。
因此

$$p[t^pu^r]e^{\alpha\widetilde V}
=[u^r]\alpha e^{\alpha W}(\xi-1/2)\pmod p.\tag{16}$$

所有 $H$ 系数都保留。$t^{2p}$ 已超出本件幅度截断，所以仅有一个响应高因子。
由单位递推归纳，$\xi$ 的所需系数整，$\xi_0=0$ 来自第一次纯 $t^p$ 初值。
$p[t^{p-1}u^r]e^{\widetilde V}$ 是 $p$ 乘整系数，故在目标实际精度消失。
将式 (16) 代入真实辅助递推，正 $u$ 次数满足

$$ (\mathcal D_{p,e}+8uF_2)\xi=4uF_2,
\qquad\mathcal D_{p,e}u^r=d_{p+2r}(H)u^r.\tag{17}$$

对 $1\le r<p$，$p+2r$ 不被 $p$ 整除；不存在遗漏的第二内部除数。
常数另行指定，未倒置 $d_p$。

纯偶低方程为 $\mathcal D_eW=-4uF_2$，其中 $\mathcal D_eu^r=d_{2r}u^r$。
它给 $(\mathcal D_e+8uF_2)(-\Theta W)=4uF_2$。
令 $Z_e=(H\partial_H-\Theta)W$，式 (8) 给

$$ (\mathcal D_e+8uF_2)Z_e=2\Theta S_{2\Theta}(H)W.$$

由式 (9)，$\mathcal D_{p,e}-\mathcal D_e=\lambda S_{2\Theta}/2$ 模 $H^{2m}$。
因此单位三角比较给

$$\xi=-\Theta W+\frac\lambda4 Z_e\pmod{H^{2m}}.\tag{18}$$

移位乘修正的误差在 $H^{2m}$；两候选常数均为零。
对 $\alpha=2$，式 (16)、(18) 化为

$$p[t^pu^r]e^{2\widetilde V}
=[u^r]\left[-(1+\Theta)F_2
+\frac\lambda4(H\partial_H-\Theta)F_2\right].\tag{19}$$

注意这里基带算子是 $1+\Theta$，不是 $1+2\Theta$；这来自新 $t^p$ 带的常数缺陷 $1/2$。

### Step 5. 倍角把剩余纯偶端点送回第一 forcing

令 $H_2=H(4-H)$、$c(H)=16/(4-H)$。
若 $P_0(H,x)$ 是同一低块在参数 $L=0$ 的单谐波解，
准确倍角 $d_{2r}(H)=(4-H)d_r(H_2)$ 给

$$W(H,u)=\frac12 P_0(H_2,c(H)u)\pmod{u^p}.\tag{20}$$

核对常数：右侧代入纯偶方程时
$(4-H)c(H)/4=4$，恰产生 $-4e^{2W}$ 的源项。
所有 $r<p$ 的传播子均为单位，因此式 (20) 在形式整环成立。
于是

$$[u^{p-1}]F_2=-c(H)^{p-1}\mathcal B_1(H_2,0).
\tag{21}$$

由式 (3)，式 (21) 模 $p$ 属于 $H^m\mathbb F_p[[H]]$。
式 (19) 取 $r=p-1$，基带乘子为 $1+(p-1)=p$；
另一项是 $\lambda/4$ 乘
$(H\partial_H-(p-1))[u^{p-1}]F_2$，因而属于 $H^{2m}$。
这证明第二个正规化端点在 $h^{2m}$ 中。

合并式 (4)、(7)、(15) 及第二端点结论，得到式 (1)。证毕。

## Conditional coefficient transfer and boundary checks

若另审接受所有 $p<j\le D$ 的相同 $h^{2m}$ 界，则与式 (1) 合并得
$[L^j]S\in h^{e_*+2m}$ 对 $j\ge p$。
首一分解从最高项向下比较至 $L^p$，逐次得到

$$u_r\in h^{e_*+2m}\mathcal O^+=h^{M-m-1}\mathcal O^+
\qquad(m+1\le r\le p).$$

这只是显式条件应用；本文没有提前接受上半段或新的最高项证明。
对 $p=5$，$m=2$、$M\ge10$，式 (7) 的最弱误差为
$M-3m\ge4=2m$，恰满足目标，不能据此多提高一阶。
全部所用整数分母 $2,4$ 为单位，两个方向的非共振三角除数均为单位。

## Corrections or missing assumptions

- 原目标 $j=p$ 没有被替换成 $j>p$；其 $t^p$ 响应和新阶乘缺陷单独处理。
- $H\partial_H$ 只作用于有整形式提升的低块与第一 forcing，再合法约化和代入。
- 没有假设辅助 $t^p$ 带整；只证明其乘 $p$ 后整，并按支撑控制它对共振差的影响。

## Open risks

- 新下界层是否非零未定；不能据此授予负 Newton 图、不可约性或简单性。
- 从 $h^{2m}$ 继续提高精度，需要保留组合移位及在最小素数处恰达边界的实际误差。
- 本件仅为作者证明，须另作全文非作者核查；同轮数学输入和产物状态仍分开。
