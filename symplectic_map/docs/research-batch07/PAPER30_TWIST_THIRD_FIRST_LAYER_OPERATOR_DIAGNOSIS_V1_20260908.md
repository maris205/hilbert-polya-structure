# Paper30：第三 forcing 首层的全参数有限算子替代

日期：2026-09-08。作者有界数学探测，使用 formula-derivation 与 proof-writer。
本件唯一新增，不修改 O1／O2、冻结作者源、接受记录或原失败。
不估页、不评分、不试写测页，不改变完整第三 forcing 的原科学中心。

## Claim / Target

固定素数 $p\ge5$，令 $m=(p-1)/2$、$\chi=(-1)^{m+1}$。
使用同一个真实 Chebyshev 有限低块、完整三次移位系数 $\mathcal F_3$ 和
实际规范 $h=D_1$、SUM action、$L=\rho\lambda$、$\rho=-h$。
本件证明在完整参数多项式环中

$$
\boxed{\mathcal F_3(H,L)=-\frac{3}{512}HL^m\pmod{H^2}.}
\tag{T1}
$$

因此按 A07 的原定义 $\mathcal F_3=E_0+HE_1+O(H^2)$，

$$
\boxed{E_0=0,\qquad E_1=-\frac3{512}L^m.}
\tag{T2}
$$

新证明只需既有有限矩 F2 的严格预临界输入，以及两个由同对象
纯偶／一次奇有限块直接求得的最高参数边界：

$$
\boxed{[L^m]W(0,L)=-\frac12,\qquad
[HL^m]W(H,L)=-\frac3{32}.}
\tag{T3}
$$

本件不以原首层单位 $a_m=-3\chi/64$ 或旧 $E_1$ 倒推 (T1)–(T3)。
目标全量词 $p\ge5,a\ge2$ 保持；$a$ 只进入最后调用的既有实际桥。

## Status

目标 (T1)–(T3)：PROVABLE AS STATED。
推导主线：COHERENT AS STATED。
这是作者完成的新替代证明，尚待针对新变化的真正非作者检查。
没有依赖未证明的最高参数矩、临界有理核或第 $p$ 个低模态。

## Inputs, Reading Scope, and Noncircular Dependency Map

本件全文读取两项技能及
[有限替代接受处置](PAPER30_TWIST_POSITIVE_FINITE_REPLACEMENT_DISPOSITION_V1_20260908.md)、
[桥义务清点 B1–B9](PAPER30_TWIST_POSTFINITE_BRIDGE_OBLIGATIONS_V1_20260908.md)、
[有限矩 F2](PAPER30_TWIST_POSITIVE_FINITE_MOMENT_DIAGNOSIS_V2_20260908.md)。
另读取 A07 Steps 5–8 及相邻定义，A09 Step 1 与 Step 2 的完整三次系数接口，
并核对 O2 Steps 3–5 中截断前的平均恒等式。

| 来源 | 本件准确调用 |
| --- | --- |
| [F2 有限矩](PAPER30_TWIST_POSITIVE_FINITE_MOMENT_DIAGNOSIS_V2_20260908.md) | $[H^kL^j]W=\delta_{j0}\beta_k$，$k+j<m$；其证明只依赖原有限低块和 Chebyshev 数据 |
| [O2 统一算子](PAPER30_TWIST_POSITIVE_UNIFIED_CRITICAL_OPERATOR_PROBE_V2_20260908.md) Steps 3–4 | 截断前的精确平均端点恒等式 $\mathcal F_3^{\rm ev}=3\mathscr DW/8$，不是仅模总阶理想的 U1 |
| [A09 全阶响应](PAPER30_TWIST_THIRD_FORCING_GENERAL_NEXT_LAYER_PROBE_V1_20260907.md) Step 1、式 (15) | 单位三角方程证明的精确 $t,q$ 和完整四项三次系数；不使用该稿后面的二阶矩 |
| [A07 第三首层](PAPER30_TWIST_THIRD_FORCING_GENERAL_PRIME_PROBE_V1_20260907.md) Steps 5、8 | $E_0,E_1$ 的原对象及实际端点／精度接口；Steps 6–7 只作为待替换的旧证明读取，不作新证明输入 |

虽然 A09 的历史输入表还列有旧 $E_1$，其 Step 1 的实际证明只用低块方程、
Chebyshev 微分身份和此前的有限响应方程，不用旧能量式、旧两矩或 $E_1$。
本件只调用这段独立向前的证明。
没有调用负端也记为 $w_1,a_1,W$ 的对象，亦未从负端归一化移植系数。

新依赖链是：
真实有限低块与 B6 精确响应 $\rightarrow$ 全平均算子的模 $H^2$ 截面；
F2 与幅度次数 $\rightarrow$ 只剩两项最高参数边界；
同对象纯偶／一次奇有限解 $\rightarrow$ 两个边界；
同一算子 $\rightarrow$ (T2)；最后接回未改变的 B5 实际桥。

## Notation and Working Rings

令 $\mathcal N=x\partial_x$。辅助幅度 $b$ 只用于有限低块，最终仍取 $b=1$：

$$
\mathcal D_HP=-\frac{bx}{2}e^P-Lx^2e^{2P},\qquad
\mathcal D_Hx^i=d_i(H)x^i,\qquad P=\sum_{i=1}^{p-1}P_ix^i.
\tag{1}
$$

$d_i=(C_i-2)/H$ 为原 Chebyshev 多项式，
$d_i(0)=-i^2$，$\Omega_i=-d_i-Hd_i'$。
所有 $x$ 指数只取 $i<p$；单位三角递推给
$P_i\in\mathbb Z_{(p)}[b,L][[H]]$。
指数的所需阶乘严格小于 $p$，因此以下模 $p$ 取值合法。
令

$$
W(H,b,L)=\sum_{i=1}^{p-1}\Omega_iP_iP_{p-i},\qquad
W(H,L)=W(H,1,L),\qquad
\ell=L\partial_L,\quad \mathscr E=H\partial_H+\ell.
$$

主截面为 $\mathbb F_p[L][[H]]/(H^2)$，不把 $L$ 设为幂零。
后文的 $u=Lx^2/4$ 是为提取最高参数项使用的有限代入，不是把实际参数
$L$ 改成另一规范，也不同于 F2 全参数构造中的 $u=x/4$。

## Proof

### Step 1. 从完整平均身份重新取得全 $L$、模 $H^2$ 截面

O2 截断前的精确身份为

$$
\mathcal F_3^{\rm ev}=\frac38\mathscr DW,\qquad
\mathscr D=\mathscr E^2+
\frac{2(H-1)}{H-4}\mathscr E+\frac H{H-4}.
\tag{2}
$$

这里平均 $i,p-i$ 的 $d,\Omega,\Psi$ 满足同一 Chebyshev 微分方程，
所有权重导数项已在完整形式环中取消，系数只在左侧相乘。
真实反射差满足

$$
\Omega_i-\Omega_{p-i}\in H^m\mathbb F_p[H],\qquad
\Psi_i-\Psi_{p-i}\in H^{m+1}\mathbb F_p[[H]].
\tag{3}
$$

完整原四项端点中的 $P,t,q$ 都是非负 $H$ 阶的有限系数。
所以先不作任何总阶截断，就有
$\mathcal F_3-\mathcal F_3^{\rm ev}\in H^m\mathbb F_p[L][[H]]$。
$m\ge2$ 因而给

$$
\mathcal F_3=\frac38\mathscr DW\pmod{H^2}
\quad\text{在整个 }\mathbb F_p[L]\text{ 上}.
\tag{4}
$$

$p=5$ 的缺陷恰从 $H^2$ 开始，仍不进入本截面。
本步不是把仅模 $(H,L)^{m+1}$ 的旧 U1 外推到总阶 $m+1$ 的 $HL^m$。

写 $W=W_0(L)+HW_1(L)+O(H^2)$。由于

$$
\frac{2(H-1)}{H-4}=\frac12-\frac38H+O(H^2),\qquad
\frac H{H-4}=-\frac14H+O(H^2),
$$

式 (4) 给出本次准确的两个全参数算子：

$$
E_0=\frac38\ell(\ell+1/2)W_0,
$$
$$
E_1=\frac38\left\{
(\ell+1)(\ell+3/2)W_1-(3\ell/8+1/4)W_0
\right\}.
\tag{5}
$$

### Step 2. 核准真正剩下的最高参数义务

式 (1) 的幅度齐次性给

$$
P_i(H,b,L)=\sum_{0\le2j\le i}c_{ij}(H)b^{i-2j}L^j.
\tag{6}
$$

有限配对总 $x$ 次数是 $p=2m+1$，所以

$$
W(H,b,L)=\sum_{j=0}^{m}w_j(H)b^{p-2j}L^j,\qquad
\deg_LW(H,L)\le m.
\tag{7}
$$

F2 的严格预临界矩和 $\beta_0=1,\beta_1=1/6$ 给

$$
W_0=1+cL^m,\qquad
W_1=\frac16+dL^{m-1}+eL^m.
\tag{8}
$$

其中 $c,d,e\in\mathbb F_p$ 尚未赋值；$m=2$ 时式 (8) 仍适用。
在式 (5) 中，$E_0=0$ 已经不依赖 $c$，因为 $m(m+1/2)=0$。
$E_1$ 的常数项是 $(3/8)(1/4-1/4)=0$，
$dL^{m-1}$ 的乘子是 $m(m+1/2)=0$。
唯一剩余是

$$
E_1=\frac38\left(\frac e2-\frac c{16}\right)L^m.
\tag{9}
$$

所以不必证明 $W_{1,m-1}$ 的值。实际新义务是 $c,e$，或它们在式 (9)
中的一个组合；下文直接计算两者，没有使用旧目标数值来选择它们。

### Step 3. 最高 $L$ 项只需同对象的纯偶与一次奇块

在辅助幅度上展开至一次项，令

$$
u=\frac{Lx^2}{4},\qquad
P(H,b,L,x)=A(H,u)+bx\,B(H,u)+O(b^2).
\tag{10}
$$

这里 $A$ 的所需 $u$ 模态是 $1\le k\le m$，
$B$ 的所需模态是 $0\le n<m$。
令

$$
A=E(u)+HV(u)+O(H^2),\qquad
B=f(u)+Hg(u)+O(H^2),
$$
$$
M_u=2u\partial_u,\qquad D_u=1+2u\partial_u,\qquad
Q(u)=\frac{8u}{(1-u)^2}.
\tag{11}
$$

$\mathcal N$ 作用于 $A(u)$ 为 $M_u$，
作用于 $xB(u)$ 为 $xD_uB$；这里 $D_u$ 不是实际 $D_1=h$。
下面纯偶身份在模 $u^{m+1}$ 使用，一次奇身份在模 $u^m$ 使用。

把 $b=0,H=0$ 代入式 (1)，再取一次 $b$ 系数，得到

$$
E=\sum_{k=1}^{m}\frac{u^k}{k},\qquad
f=\frac1{2(1-u)}\pmod{u^m}.
\tag{12}
$$

第一式给 $M_u^2E=4u/(1-u)^2=4u e^{2E}$，其有限指数身份只用 $k\le m<p$。
第二式满足

$$
(D_u^2-Q)f=\frac1{2(1-u)}.
\tag{13}
$$

两者均由原单位三角递推唯一确定，因而不是另设的参照解。
纯偶低块可记为 $E=-\log_{\le m}(1-u)$；所需有限指数满足

$$
\exp E=\frac1{1-u},\qquad
\exp(2E)=\frac1{(1-u)^2}\pmod{u^{m+1}}.
\tag{14}
$$

这些恒等式只涉及次数不超过 $m<p$ 的系数，分母均为 $p$ 单位。

### Step 4. 一次 $H$ 的有限奇偶解：不引入第 $p$ 个积分系数

真实 Chebyshev 首阶为

$$
d_i=-i^2+\frac H{12}(i^4-i^2)+O(H^2).
\tag{15}
$$

写 $U=P|_{H=0}$、$w=\partial_HP|_{H=0}$，
直接对式 (1) 求导得

$$
(\mathcal N^2-J)w=\frac{\mathcal N^4-\mathcal N^2}{12}U,\qquad
J=\frac{bx}{2}e^U+2Lx^2e^{2U}.
\tag{16}
$$

这只是原低块的一次导数方程，不是旧能量首积分。
取式 (16) 的纯偶系数，得到

$$
(M_u^2-Q)V=\frac{u(u^2+6u+1)}{(1-u)^4}.
$$

其零常数唯一解是

$$
\boxed{V=\frac{u(1+u)}{4(1-u)^2}\pmod{u^{m+1}}.}
\tag{17}
$$

将式 (17) 代入上一行，通分的分子差为零；
对角元是 $(2k)^2$，$1\le k\le m$，均为 $p$ 单位。

在式 (16) 再取一次 $b$ 系数。由式 (12) 的 $f$ 和式 (14)，

$$
\frac{[b]J}{x}=\frac1{2(1-u)}+\frac{8u}{(1-u)^3}.
$$

所以 $g$ 满足准确有限方程

$$
(D_u^2-Q)g
=\frac{D_u^4-D_u^2}{12}f+
\left(\frac1{2(1-u)}+\frac{8u}{(1-u)^3}\right)V
=\frac{u(u^3+39u^2+95u+25)}{8(1-u)^5}.
\tag{18}
$$

定义只在有限奇指标上取逆的多项式

$$
J_{\rm odd}(u)=\sum_{n=0}^{m-1}\frac{u^n}{2n+1},
\qquad D_uJ_{\rm odd}=\frac1{1-u}\pmod{u^m}.
\tag{19}
$$

所有分母属于 $1,3,\ldots,p-2$。没有定义 $n=m$ 项，
也没有引入 $1/p$ 或任何 $[x^p]w$。
令 $G=(1+u)/(1-u)$。直接求导有

$$
(M_u^2-Q)G=0,\qquad M_uG=\frac{4u}{(1-u)^2}.
$$

乘积法则和式 (19) 给

$$
(D_u^2-Q)(GJ_{\rm odd})
=GD_u^2J_{\rm odd}+2(M_uG)D_uJ_{\rm odd}
=\frac{1+10u+u^2}{(1-u)^3}\pmod{u^m}.
\tag{20}
$$

因此式 (18) 的解是

$$
\boxed{g=
\frac{1+16u+7u^2}{48(1-u)^3}
-\frac{1+u}{48(1-u)}J_{\rm odd}(u)
\pmod{u^m}.}
\tag{21}
$$

为完整核对这个有限证书，记第一项为 $R(u)$，则

$$
48(1-u)^5(D_u^2-Q)R
=1+158u+552u^2+242u^3+7u^4.
$$

从右边减去 $(1+10u+u^2)(1-u)^2$，结果恰为
$6u(u^3+39u^2+95u+25)$，正是式 (18) 乘以 $48(1-u)^5$。
$g(0)=1/48-1/48=0$，且一次奇对角元
$(2n+1)^2$ 在 $0\le n<m$ 均为单位。
故式 (21) 是原真实有限块的唯一解，不是从旧答案反推的形式证书。

式 (19) 在商环中合法：$D_u$ 保持 $(u^m)$，从
$D_uJ_{\rm odd}\equiv(1-u)^{-1}$ 再求导不会产生未知边界。
此处从未越过第 $m-1$ 个奇模态。

### Step 5. 直接求最高参数矩

由式 (7)，$[b]W(H,b,L)=L^m[L^m]W(H,L)$。
它只配对一个纯偶模态 $2k$ 和一个一次奇模态
$p-2k=2(m-k)+1$，$1\le k\le m$。
到模 $H^2$，式 (3) 使两端权重相同，且

$$
\Omega_{2k}=4k^2-\frac H6\,4k^2(4k^2-1)+O(H^2).
\tag{22}
$$

由式 (14)、(17)、(12)，

$$
[u^k]E=\frac1k,\qquad
[u^k]V=\frac{2k-1}{4}\quad(k\ge1),\qquad
[u^n]f=\frac12.
\tag{23}
$$

每对的参数缩放是 $4^{-k}4^{-(m-k)}=4^{-m}=1$ 于 $\mathbb F_p$，
最后一个等式来自 $4^m=2^{p-1}=1$。
加上两种有序配对，式 (22)、(23) 直接给

$$
c=2\sum_{k=1}^m4k^2\frac1k\frac12
=4\sum_{k=1}^mk=2m(m+1)=-\frac12.
\tag{24}
$$

再记 $g_n=[u^n]g$。一次 $H$ 的三种贡献分别来自权重、纯偶块和一次奇块，
全部保留后得到

$$
\begin{aligned}
e={}&2\sum_{k=1}^m\left\{
-\frac{4k^2(4k^2-1)}6\frac1k\frac12
+4k^2\frac{2k-1}{4}\frac12
+4k^2\frac1k\,g_{m-k}
\right\}\\
={}&\sum_{k=1}^m\left(-\frac23k^3-k^2+\frac23k\right)+8S,
\qquad S=\sum_{n=0}^{m-1}(m-n)g_n.
\end{aligned}
\tag{25}
$$

本式的 $S$ 是一个只用实际低模态的有限和；下一步直接求值。

### Step 6. 有限奇响应卷积为零，且无隐藏 $p$ 分母

由式 (21)，

$$
48S=[u^{m-1}]
\left\{\frac{1+16u+7u^2}{(1-u)^5}
-\frac{1+u}{(1-u)^3}J_{\rm odd}(u)\right\}.
\tag{26}
$$

第一项的系数是

$$
R_m=\binom{m+3}{4}+16\binom{m+2}{4}+7\binom{m+1}{4}
=\frac{m(m+1)(2m^2-1)}2.
\tag{27}
$$

对 $m=2$，$\binom{m+1}{4}=\binom34=0$；没有使用负指数。
所有二项式都可以用分母 $4!=24$ 的多项式恒等式计算，$p\ge5$ 时合法。
在 $\mathbb F_p$ 中 $m=-1/2$，因此 $R_m=1/16$。

第二项的系数利用
$[u^r](1+u)/(1-u)^3=(r+1)^2$ 得

$$
J_m=\sum_{n=0}^{m-1}\frac{(m-n)^2}{2n+1}.
\tag{28}
$$

由于 $2n+1\ne0$ 且 $m-n=-(2n+1)/2$ 于 $\mathbb F_p$，
每个被求和项就等于 $(2n+1)/4$。故

$$
J_m=\frac14\sum_{n=0}^{m-1}(2n+1)=\frac{m^2}{4}=\frac1{16}.
$$

式 (26) 得 $S=0$。这不是将一个含 $1/p$ 的末项置零；
整个和的分母严格避开 $p$，终点就是 $n=m-1$。

最后，有限幂和公式给

$$
\sum_{k=1}^mk=-\frac18,\qquad
\sum_{k=1}^mk^2=0,\qquad
\sum_{k=1}^mk^3=\frac1{64}
\quad\text{于 }\mathbb F_p.
$$

这里分别代入
$m(m+1)/2$、$m(m+1)(2m+1)/6$ 及 $m^2(m+1)^2/4$，
所有分母均为单位。代回式 (25)，得到

$$
e=-\frac23\frac1{64}+\frac23\left(-\frac18\right)=-\frac3{32}.
\tag{29}
$$

式 (24)、(29) 证明 (T3)；整个计算对 $p=5,m=2$ 有效。

### Step 7. 回到同一全参数算子及实际首层

将新证 $c=-1/2$、$e=-3/32$ 代入式 (9)，有

$$
E_1=\frac38\left(-\frac3{64}+\frac1{32}\right)L^m
=-\frac3{512}L^m.
$$

结合 Step 2 的 $E_0=0$，(T1)、(T2) 得证。
被算子消去的 $d=[HL^{m-1}]W$ 从始至终没有赋值。$\square$

接回原实际桥时仍保留 B5 的准确端点、
$r=2\chi H^m+O(H^{m+1})$ 及
$\mathcal E=r^3\mathcal F_3+O(H^{4m})$。
因为 $E_0=0$，$r$ 的更高修正不在 $H^{3m+1}$ 产生未控制项。
于是

$$
\mathcal E=-\frac{3\chi}{64}H^{3m+1}L^m
+O(H^{3m+2})+O(H^{4m}).
$$

既有实际误差为 $h^M$，$M=p^{a-1}m$，并且
$\min(3m+2,4m,M)\ge3m+2$ 对全部 $p\ge5,a\ge2$ 成立。
因此不改变原单位锚点：

$$
p^2\mathcal B_3=-\frac{3\chi}{64}h^{3m+1}L^m+O(h^{3m+2}),\qquad
a_m=-\frac{3\chi}{64}+O(h).
\tag{30}
$$

式 (30) 是新首层证明与原桥的合成后果，不是本件的计算输入。

## Actual Replacement and Retained Obligations

| 原义务 | 本件后的准确依赖 |
| --- | --- |
| A07 Step 6 的全参数一次低块显式首积分、能量多项式 (42) 与身份 (43) | 首层证明不再调用；只解最高参数所需的有限纯偶／一次奇响应，并直接验证二阶方程 |
| A07 式 (44) 中 $p[x^p]w$ 的积分边界 | 不再调用；有限 $J_{\rm odd}$ 的分母止于 $p-2$，没有第 $p$ 模态 |
| A07 Step 7 的全参数 $A_1=B_0/8$、$B_0$ 及 $R$ 矩求值链 | 不再调用；F2 加参数次数只留下 $c,e$，用式 (24)–(29) 的有限和求出 |
| A07 Step 8 的式 (39)、(54) 逐个响应合并 | 首层的合并由完整平均算子截面式 (5) 替代；完整四项端点本身仍保留 |
| B6／A09 的精确全 $H$ 响应与完整 $\mathcal F_3$ | 仍需保留；本件借用该接口，不以旧低阶展开代替它 |
| F2、O2 截断前平均身份、真实反射缺陷和有限整性 | 仍需保留其准确证明；本件只扩大被调用的截面，不重评已接受内容 |
| B1–B5 实际块、非驻值 action、合法移位及误差；B8 四次修正；B9 分离和商高度 | 全部不由本件替代 |

这不是把旧能量式换一个符号重新展示：新路径不构造全参数的 $w$ 首积分，
不在第 $p$ 项提取积分边界，不先求全参数 $A_1,B_0$。
它改为先用完整算子消去不需要的矩，再在原有限三角系统的两个幅度系数上
直接给出解和单位分母有限求和。
式 (21) 可以在其他证明中由更一般公式推出，但本件的证明与旧公式没有依赖关系。

不宣称 A07 的所有历史结果、或旧两矩在其他独立用途的证明均可删除。
也不将新方法另算贡献、将删除依赖数当作篇幅证据，或据此授予完整候选通过。

## Verification, Corrections, and Open Risks

作者在内存中对自由变量 $u$ 完整求导，核对以下准确残差均为 $0$：
纯偶 $V$ 方程、一次奇 $f$ 方程、$G$ 齐次方程、
式 (21) 代入式 (18) 后消去有限 $J_{\rm odd}$ 的有理残差。
另核对式 (27) 的二项式多项式化及式 (25) 的有限幂和，
得到 $S=0,e=-3/32$。无素数扫描、拟合或负端数据输入。

1. 需要真正非作者核对的新增接口是全平均身份在模 $H^2$ 全参数截面的使用、
   最高参数的幅度／缩放对应、有限奇响应及其卷积；作者符号核算不替代独审。
2. $p=3$ 不在范围；$12,24,48$ 等分母解释为 $\mathbb F_p$ 单位。
3. 不对总阶 U1 作越界使用，不定义特征 $p$ 的无限对数／积分，
   不把有限参数 $L$ 施加 $L^p=L$ 或任何根方程。
4. 本件未改变实际规范、全部量词、原数学中心或验收约束；只新增本文件。
