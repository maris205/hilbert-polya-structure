# Paper30：第二阶乘响应桥与一般第三 forcing 联合非作者独审

日期：2026-09-07。核查者：`p30_third_forcing_general_independent`。
本核查者没有参与两份受审稿的作者推导、主控共推或作者身份核对；
完整读取工作区入口与 `proof-writer` 后，独立审查实际冻结文本。
本件只写核查报告，未修改作者稿、旧接受记录、入口或任何锁。

## Claim

本件审查两份新冻结稿的完整连接，而不是只检查最终候选系数：

1. 第二阶乘带的两条形式阶乘桥、实际块与零初值模型的误差、
   精确组合响应方程及其首个二阶响应；
2. 对任意素数 $p\ge5$、$a\ge2$ 及任意本原 $p^a$ 次根，第三 forcing 的
   准确首层、实际第三内部模态、参数点值边界及已述互素推论。

规范始终为

$$
h=2-\zeta-\zeta^{-1},\quad \rho=-h,\quad L=\rho\lambda,
\quad m=(p-1)/2,\quad M=p^{a-1}m,\quad \chi=(-1)^{m+1},
$$
$$
d_n=-D_n/h,\qquad
d_nV_n=-\frac12[x^{n-1}]e^V-L[x^{n-2}]e^{2V}.
$$

这里 $D_n=2-\zeta^n-\zeta^{-n}$、$K^+=\mathbb Q_p(h)$、
$\mathcal O^+=\mathbb Z_p[h]$，$v_h(h)=1$、$v_h(p)=M$；
$\mathcal B_3=-[x^{3p-1}]e^V-2L[x^{3p-2}]e^{2V}$ 仅需 $n<3p$ 的实际分支。
$\mathcal B_1$ 是同一分支在第 $p$ 个模态处的第一内部 forcing。

被核查的新端点结论是

$$
h^{-(3m+1)}p^2\mathcal B_3\in\mathcal O^+[L],\qquad
\overline{h^{-(3m+1)}p^2\mathcal B_3}=-\frac{3\chi}{64}L^m,
$$
$$
h^{-(m+1)}p^2V_{3p}\in\mathcal O^+[L],\qquad
\overline{h^{-(m+1)}p^2V_{3p}}=\frac{\chi}{384}L^m,
\qquad \gcd_{K^+[L]}(\mathcal B_1,\mathcal B_3)=1.
$$

系数最小赋值与参数点值赋值分别审查，不将这两个命题混同。

## Status

**PROVABLE AS STATED：18 项限定检查全部 PASS。**

两份冻结稿的原有主张均保持，未发现阻断性证明缺口，没有要求作者修改。
结论严格限于两份输入已述范围；这不是完整素数幂首项或 Paper30 产物验收。

## Assumptions and Frozen Inputs

核查者已全文读取下列两份实际冻结稿，并实际核对其 SHA256：

| 输入 | 行数 | SHA256 |
| --- | ---: | --- |
| [第二阶乘响应桥 V1](PAPER30_TWIST_PRIME_POWER_SECOND_FACTORIAL_RESPONSE_BRIDGE_PROBE_V1_20260907.md) | 640 | `6320b1250373ba0172ea683ecc9314fb542c8434b32c84cf35a85a0c888e325d` |
| [一般第三 forcing V1](PAPER30_TWIST_THIRD_FORCING_GENERAL_PRIME_PROBE_V1_20260907.md) | 843 | `1c91dd36cd2932f11635e0aa2b1b817579af65f0f5fef34daac9eda2a32fd88a` |

已接受输入只按既有范围调用，不重新授予独审：

- [第二阶乘带处置](PAPER30_TWIST_PRIME_POWER_SECOND_FACTORIAL_BLOCK_DISPOSITION_20260907.md)：
  低块整性、两块正规化整性、实际内部初值高度以及严格低于 $3p$ 的指数整性。
- [第二内部层处置](PAPER30_TWIST_PRIME_POWER_SECOND_INTERNAL_DISPOSITION_20260907.md)：
  第一 forcing 的全部根局部整、其剩余根满足 $\bar L^m=2$，以及已述正规化。
- 首层内部结构 V1 中已接受的有限矩
  $\sum_{i=1}^{p-1}i^2U_iU_{p-i}=(2-L^m)/2$，按问题定向定位原式后调用。

特别使用

$$
Y^{\rm act}_0=pV_p\in h^{M-m}\mathcal O^+[L],\qquad
Z^{\rm act}_0=p^2V_{2p}\in h^M\mathcal O^+[L],\qquad
d_p/h^{2m}\equiv-1\pmod h.
$$

$p\ge5$ 给出 $m\ge2$、$M\ge5m$，并保证所用 $2,3$ 分母为单位。
不假设 $L\ne0$，不把 $L^p$ 改成 $L$，也不在递推中除以参数多项式。

## Notation

$\mathscr R=\mathbb Z_{(p)}[L][[H]]$，$P$ 是次数严格低于 $p$ 的形式低块，
$P_1=1/2$；$\mathcal N=x\partial_x$。
$\mathcal D_kx^j=d_{kp+j}(H)x^j$ 只用于 $1\le j<p$，
$\mathcal D=\mathcal D_0$、$\Delta_k=\mathcal D_k-\mathcal D$。
这些正次数上的对角常数项为 $-(kp+j)^2$，故属于 $p$-单位。

使用两稿共同的 $J,K,Y,Z,y,Q$ 定义：

$$
J=xe^P/2+2Lx^2e^{2P},\qquad K=xe^P/4+2Lx^2e^{2P},
$$
$$
Y^{(0)}=-\mathcal NP/2,\quad Z^{(0)}=\mathcal N^2P/8,
\quad y=Y-Y^{(0)},\quad Q=Z-Z^{(0)}+\mathcal Ny/2.
$$

$Y,Z$ 是桥稿的零常数模型，实际块为
$Y^{\rm act}=\sum_{j=0}^{p-1}pV_{p+j}x^j$、
$Z^{\rm act}=\sum_{j=0}^{p-1}p^2V_{2p+j}x^j$。
下文的 $\mathsf S,\mathsf T,\mathsf A,f,g,w$ 分别采用一般稿式 (23)、(25)、(30)
的冻结定义；$\langle f,g\rangle_k=\sum_{i=1}^{p-1}i^k f_i g_{p-i}$，$k=2,4$。

形式 $H$ 阶均先在模 $p$ 环中解释；实际 $h$ 阶是
$\mathcal O^+[L]$ 中的逐系数整除。它们之间必须使用明确误差桥。

## Proof Strategy and Dependency Map

1. 先核阶乘分母和实际三角递推，保证后续形式模型有正确实际输入。
2. 独立导出 $Q$ 的准确消元式，不用最低阶候选代替精确方程。
3. 从有限 SUM action 重建端点，逐项保留低／第二块与第一块平方。
4. 审查有限移位参数的固定环、响应的下一 $H$ 阶与完整四项收集。
5. 用低块响应首积分核实第 $p$ 阶边界，求两个矩，再合并端点两层。
6. 最后检查实际误差余量、点值量词及互素推论，避免越出已证明范围。

## Proof

### 1. 形式阶乘桥与实际模型精度

对 $N<3p<p^2$，指数展开中的阶乘至多含两个 $p$ 因子。
本节 $\alpha=1,2$，两条阶乘桥首先取 $0\le j<p$，再按所需负下标延伸。
在最高阶乘带，独立清分母得到

$$
\frac{p^2}{(2p+r)!}\equiv\frac1{2r!}\pmod p,
\qquad 0\le r<p.
$$

在保留 $H,L$ 的形式系数环中，Frobenius 及 $P_1=1/2$ 给出
$P^{2p}=x^{2p}/4+O(x^{3p})$。所有更低阶乘带乘 $p^2$ 后含 $p$，所以

$$
p^2[x^{2p+j}]e^{\alpha P}
=\frac{\alpha^2}{8}[x^j]e^{\alpha P}+pR^{(2)}_{\alpha,j},
\qquad R^{(2)}_{\alpha,j}\in\mathscr R.
$$

第一阶乘桥同样保留完整形式依赖：

$$
p[x^{p+j}]e^{\alpha P}
=-\frac\alpha2[x^j]e^{\alpha P}+pR^{(1)}_{\alpha,j}.
$$

两式的结论确实是 $p\mathscr R$ 误差，而不只是模 $H$ 的身份。
负下标主项为零时，实际低次数系数被留在 $p$ 倍误差中；没有删除真实值。

把 $V=P+x^pY^{\rm act}/p+x^{2p}Z^{\rm act}/p^2$ 代入指数，
严格低于 $3p$ 时保留常数、两条线性项及第一块平方。
四个来源合成

$$
p^2[x^{2p+j}]e^{\alpha V}
=[x^j]e^{\alpha P}
\left(\alpha Z^{\rm act}+\frac{\alpha^2}{2}(Y^{\rm act}-1/2)^2\right)
+p\epsilon_{\alpha,j},
$$

其中余项整。由此得到作者桥稿的两条实际耦合递推。
模型只将自身常数项定为零；实际内部常数项使用上述已知高度。
逐阶单位除法先给 $Y^{\rm act}-Y(h)\in h^{M-m}$。
平方之差抽出该差为因子，继而给出

$$
Y^{\rm act}-Y(h),\quad Z^{\rm act}-Z(h)\in h^{M-m}.
$$

有限整系数多项式组合保持此高度；只有再乘至少 $h^m$ 的端点缺陷，
误差才达到 $h^M$。本次端点确实具备这一额外因子。

### 2. 组合响应的准确耦合

低块方程及其 $x$ 导数给出

$$
(\mathcal D+J)\mathcal NP=-J,\qquad
\mathcal NJ=2K(1+\mathcal NP),
$$

从而 $Y^{(0)},Z^{(0)}$ 满足各自未移位模型。
对 $y$ 的方程作 $\mathcal N$ 导数，再与 $Z-Z^{(0)}$ 的方程相加，
使用 $\mathcal NY^{(0)}=-4Z^{(0)}$ 及
$\mathcal NJ=-4K(Y^{(0)}-1/2)$，两个线性交叉项准确相消。
独立得到

$$
(\mathcal D_2+J)Q
=(2\Delta_1-\Delta_2)Z^{(0)}
+\frac12(\Delta_2-\Delta_1)\mathcal Ny-Ky^2.
$$

这里 $-Ky^2$ 必须保留。
真实 Chebyshev 差分给 $\Delta_1=2\chi H^m\mathcal N+O(H^{m+1})$、
$2\Delta_1-\Delta_2=2H^{2m}I+O(H^{2m+1})$。
单位三角性因此排除 $y$ 的所有低于 $m$ 层及 $Q$ 的所有低于 $2m$ 层。

对幅度族 $U_b=-\log(1-bx/2+(b^2-4L)x^2/16)$ 用
$\mathcal T=b\partial_b+L\partial_L$，独立核得桥稿的

$$
y_1=-\chi(\mathcal N-L\partial_L)U,\qquad
Q_2=\left(\frac12(\mathcal N-L\partial_L)^2
+\frac14(\mathcal N-L\partial_L)\right)U.
$$

相关导数可写成整有理式；无限对数只在次数低于 $p$ 时约化。
这些桥结论本身并不确定第三 forcing 的下一层，后文另核其所需新响应。

### 3. 正 action、实际余界与四项重组

独立从

$$
\Phi=[x^{3p}]\left(V\mathcal D_hV/2+xe^V/2+Lx^2e^{2V}/2\right)
$$

重算偏导与加权 Euler 身份，得到

$$
\mathcal B_3=-6p\Phi+
\sum_{i=1}^{3p-1}i(d_i-d_{3p-i})V_iV_{3p-i}.
$$

正动能、正势能及右侧非驻值项的符号吻合实际递推。
低／第二块与第一块平方的正规化积均整，内部积的高度也足够，
故 $p^2\Phi$ 整，舍弃的 $p^3\Phi$ 高度至少 $M$。
内部权重含 $p$，其正规化贡献至少 $2M-m>M$。
将剩余权重模 $p$ 化简，所丢项也至少为 $M$。

令 $\delta_i^\ell=d_i-d_{3p-i}$、
$\delta_i^c=d_{p+i}-d_{2p-i}$、$C_i=\delta_i^\ell-\delta_i^c$。
两缺陷均至少 $h^m$，故实际块替换误差达到 $M$。
将 $Y_i=-iP_i/2+y_i$、$Z_i=i^2P_i/8-iy_i/2+Q_i$ 逐项代入，
利用 $p-i=-i$ 及 $\delta_{p-i}^c=-\delta_i^c$，独立得到完整式

$$
\mathcal E=\frac14\sum_i i^3C_iP_iP_{p-i}
+\sum_i i^2C_iP_i y_{p-i}
+2\sum_i i\delta_i^\ell P_iQ_{p-i}
+\sum_i i\delta_i^c y_i y_{p-i}.
$$

尤其第一块的两个交叉项在反射后相加，而不是被误删。

### 4. 有限移位与下一 $H$ 阶响应

以 $z=1+\eta$、$T=z^p$、$u=z^i$ 直接相减传播子，核实

$$
C_i=-\frac{(T-1)^2(T^2+T+1)}{T^3H}(u+T^2/u),
$$
$$
C_i-C_{p-i}=\frac{(T-1)^3(T^2+T+1)}{T^3H}(u-T/u).
$$

第二式的 $\eta$ 阶为至少 $3p-1=2(3m+1)$，
因此基线项低于 $3m+1$ 的全部层均被排除。

作者的有限反演对称对数 $\ell(T)$ 不需要特征 $p$ 的无限对数。
$r=\ell(T)(z-z^{-1})/H$ 反演不变；用
$w_0=(z-1)/(z+1)$ 后固定环为 $\mathbb F_p[[w_0^2]]=\mathbb F_p[[H]]$。
其首项为 $2\chi H^m$。有限三次指数余项除以 $H$ 后至少为
$\eta^{4p-2}=\eta^{2(4m+1)}$，且仍反演不变，所以作者写出的
$O(H^{4m+1})$ 高度有效。

以独立 $\nu$ 替换 $r$ 后，单位模型的 $\nu$ 系数满足

$$
\mathscr Lt=\mathsf S\mathcal NP/2,\qquad
\mathscr Lq=-\mathsf T\mathcal N^2P/4+\mathsf S\mathcal Nt/2-Kt^2.
$$

这里 $y=\nu t+O(\nu^2)$、$Q=\nu^2q+O(\nu^3)$。
独立使用 $\mathscr Lf=\mathcal DP$、
$\mathscr Lg=(\mathcal D-J)f-2Kf^2$ 及
$\mathscr L_0w=-\mathsf AU$ 重算一次 $H$ 项，得到

$$
t_0=-f_0/2,\quad t_1=(w-\mathcal Tw)/2,
$$
$$
q_0=g_0/8+f_0/16,\quad
q_1=\mathcal T^2w/8-3\mathcal Tw/16+w/16+f_0/64.
$$

核查 $q$ 时，减去 $\mathscr L(g/8+f/16)$ 后的驱动准确为

$$
H\left(-\frac{\mathcal N^4+2\mathcal N^2}{192}U
-\frac14\mathscr L_0(\mathcal Tw)\right)+O(H^2).
$$

它等于 $H\mathscr L_0(w/16+f_0/64-\mathcal Tw/4)$，
所以该下一阶响应不是未经控制地外推桥稿的 $Q_2$。

### 5. 低块响应首积分与不可删除的第 $p$ 阶项

使用一般稿的 $A,v,G,F_0,J_0,w$ 定义，独立求导验证

$$
G\mathcal Nw-F_0w=R/12,\qquad
R=(3/8+3L/2)v^2+2Lv^3+\frac32L^2v^4.
$$

再次求导给
$(\mathcal N^2-J_0)w=(\mathcal N^4-\mathcal N^2)U/12$，
并且 $w_0=w_1=0$。次数低于 $p$ 时积分分母均为单位，
故它与形式低块的一次 $H$ 导数由单位递推唯一性相同。

在第 $p$ 阶，只有 $I_A=\int_0^x A(t)^{-1}dt$ 的第 $p$ 个系数可能含 $p$ 分母。
其前乘因子 $G$ 的常数项是 $1$；更低积分系数以及有理部分均整。
因此

$$
\overline{p[x^p]w}=-\frac1{48}[x^{p-1}]A^{-1}=-\frac1{48}L^m.
$$

这是非零边界贡献，不能因 $\mathcal N$ 在次数 $p$ 上为零便删除。
在首积分取第 $p$ 项时，两个正次数乘积分别给
$-\langle U,w\rangle_2$ 和 $+\langle U,w\rangle_2$，从而

$$
A_1=2\langle U,w\rangle_2
=\overline{p[x^p]w}-[x^p]R/12.
$$

对一般线性系数 $a_0$，
$[x^{p-1}](1-a_0x+\theta x^2)^{-1}=(a_0^2-4\theta)^m$
先在根差非零的局部化中成立，再由多项式单射覆盖重根。
作至多三次 $a_0$ 导数便得到全部 $[x^p]v^k$，$1\le k\le4$。
独立合并这些导数后核得

$$
B_0=\langle U,U\rangle_4=\frac14L^m-\frac1{16}L^{m-1},
\qquad [x^p]R=-\frac58L^m+\frac3{32}L^{m-1},
$$
$$
A_1=\frac1{32}L^m-\frac1{128}L^{m-1}=B_0/8.
$$

合并在多项式环中完成，最低 $m=2$ 时也不产生负参数幂，
不存在将 $0\cdot L^{-1}$ 当作合法公式的边界漏洞。

### 6. 全部三次移位项及下一层合并

四项端点展开中，基线提供 $-3r^3HB_0/32$。
其余三项的传播子分别提供
$-6\mathsf T_i$、$6i\mathsf S_i$、$3i\mathsf S_i$，
各自一次 $H$ 修正与一般稿式 (39) 一致。
省略的四次及更高移位项至少为 $H^{4m}$。

在总次数 $p$ 的矩上，幅度权重使
$\mathcal T=p-L\partial_L\equiv\mathfrak d=-L\partial_L$。
逐一代入上节 $t_0,t_1,q_0,q_1$ 后，独立收集得到下表：

| 一次 $H$ 项来源 | $A_1$ 的算子 | $B_0$ 的算子 | $A_0$ 的算子 |
| --- | --- | --- | --- |
| 两响应与低块变化 | $3\mathfrak d^2/8-15\mathfrak d/16+9/16$ | $0$ | $3\mathfrak d/64$ |
| 三条传播子修正及配对基线 | $0$ | $-\mathfrak d^2/16+5\mathfrak d/32-3/32$ | $\mathfrak d^2/16-\mathfrak d/16$ |

此表直接核对一般稿式 (54) 的全部项，而不依赖最后单项式系数反推。
常数层为

$$
E_0=(3\mathfrak d^2/8-3\mathfrak d/16)A_0=0,
\qquad A_0=1-L^m/2.
$$

因为 $\mathfrak d$ 在 $L^m$ 上为 $1/2$，整个 $3m$ 层消失；
$r$ 的未写下一项因此不会乘出额外贡献。

一次 $H$ 层以 $A_1=B_0/8$ 合并后，$B_0$ 的算子为
$-(2\mathfrak d-3)(\mathfrak d-1)/128$，
$A_0$ 的算子为 $\mathfrak d(4\mathfrak d-1)/64$。
$L^{m-1}$ 的特征值是 $3/2$，故其系数为零；
$L^m$ 的两个来源分别为 $-1/512$ 与 $-1/256$。
由此得到 $E_1=-3L^m/512$，进而

$$
\mathcal E=-\frac{3\chi}{64}H^{3m+1}L^m
+O(H^{3m+2})+O(H^{4m}).
$$

### 7. 实际精度、模态及全部量词

已核误差总高度是

$$
\min(3m+2,4m,M)\ge3m+2,
$$

因为 $m\ge2$、$M\ge5m$。最小边界 $m=2$ 时，四次移位误差恰从
$3m+2=4m$ 起，仍严格高于目标层。
实际模型误差及形式模 $p$ 的提升误差均已界到 $M$。
因此得到作者所述逐系数实际首层，且其系数 $-3\chi/64$ 为单位。

三倍频恒等式 $d_{3p}=d_p(3+hd_p)^2$ 给
$d_{3p}/h^{2m}\equiv-9$。由于 $3p<p^a$，除以 $2d_{3p}$ 合法，
得到 $V_{3p}$ 的剩余 $\chi L^m/384$，没有误用真共振传播子。

在任意有限局部扩域中，若 $\bar L\ne0$，上述两正规化值为单位；
若 $\bar L=0$，它们只保证处于该扩域极大理想。
作者使用严格大于基线的赋值表述，未将分歧扩域值群强制变成整数格。

互素推论只调用已接受的第一 forcing 根整性及 $\bar L^m=2$。
这些根的剩余不为零，第三 forcing 的正规化在每个这些根处都是单位，
故无共同根，得到所述 $K^+[L]$ 上互素性。
这里没有证明或暗含 $\gcd(\mathcal B_2,\mathcal B_3)=1$。

## Exact Verification Actually Run

证明审查之外，本核查者实际运行了两组独立自由符号运算：

1. 自由 $b,L,x,c$，仅使用 $c^2=1$，核对平方传播子、加权导数、
   第一响应方程及 $Q_2$ 方程。五个有理残差均为零：
   `INDEPENDENT_EXACT_PASS rational low-block, weighted response, Q2 residuals: [0, 0, 0, 0, 0]`。
2. 自由 $T,u,H$ 的两个差分因式；自由 $k,v$ 的有限三次移位展开；
   自由 $x,L,I$ 并用 $I'=1/A$ 的首积分、二阶方程及能量多项式。
   七个残差均为零：
   `INDEPENDENT_EXACT_PASS endpoint defect factors, free-k finite shifts, low-H first integral/ODE/energy: [0, 0, 0, 0, 0, 0, 0]`。
   最终算子合并另输出 $-(d-1)(2d-3)/128$，两个单项式系数为 $-3/512,0$。

全部运算只处理新自由符号身份，没有素数、根、分母、分子或参数扫描。
运行不代替一般阶乘证明、实际整性、误差高度或有限扩域量词的核查。

## Check Ledger

| 项 | 限定检查 | 结果 |
| ---: | --- | --- |
| 1 | 两稿规范、范围及旧输入调用边界 | PASS |
| 2 | 两条完整形式阶乘桥及 $pR$ 余项 | PASS |
| 3 | 实际指数四来源及两块耦合递推 | PASS |
| 4 | 真实初值、$M-m$ 误差及乘缺陷提升 | PASS |
| 5 | 准确 $Q$ 消元及二次项符号 | PASS |
| 6 | 桥稿第一响应及组合二阶响应 | PASS |
| 7 | 正 SUM action、非驻值 Euler 身份及实际 $M$ 界 | PASS |
| 8 | 端点四项重组和两种精确配对差分 | PASS |
| 9 | 反演固定环、有限对数及 $4m+1$ 移位余界 | PASS |
| 10 | 两单位响应的下一 $H$ 阶 | PASS |
| 11 | 完整三次移位项及 $4m$ 高次项界 | PASS |
| 12 | 低块 $w$ 首积分、二阶方程及有限整性 | PASS |
| 13 | 非零 $p[x^p]w$ 边界及其符号 | PASS |
| 14 | 通用矩、$A_1=B_0/8$ 及最小 $m=2$ 边界 | PASS |
| 15 | 整个 $3m$ 层取消 | PASS |
| 16 | 式 (39)/(54) 全部同阶项及 $E_1$ | PASS |
| 17 | 实际首层、$V_{3p}$ 正规化及扩域点值边界 | PASS |
| 18 | $\mathcal B_1,\mathcal B_3$ 互素的实际根论证与限制 | PASS |

## Corrections or Missing Assumptions

本次两份冻结 V1 没有需要新增的假设或修订要求。
一般稿已披露的传递草式笔误，在实际受审冻结稿中已使用正确正 action
和 $3L^2v^4/2$；本报告只核准此冻结文本，不追认未受审草式。
没有覆盖或改称旧失败、旧作者稿或旧接受结果。

## Open Risks and Delivery Boundary

- 本报告不处理 $p=3$；其高内部传播子和最小真共振由另一限定核查负责。
- $\bar L=0$ 类的准确更高层、第三 forcing 的完整 Newton 多边形及全部根仍未解决。
- 未证明第二／第三 forcing 互素、完整 $C_{r,p^a}$、$C,Q$ 互素或参数根全实性。
- 本报告不给新意、正文容量、立项、PDF 或 Route 接受票；Batch07 篇数不由本件改变。
- 当前交付仅为本地联合数学独审；由主控全文读取本报告后作范围处置。
