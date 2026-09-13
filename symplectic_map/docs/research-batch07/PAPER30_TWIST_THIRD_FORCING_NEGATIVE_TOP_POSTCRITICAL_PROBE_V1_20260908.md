# Proof Package：负端最高参数系数的后一临界层仍消失

日期：2026-09-08。作者：`/root/negative_top_alternative`。
本件只计算已接受临界层之后紧邻的一层；仅写本文件，不修改旧稿、入口或接受记录。
使用 proof-writer；有界子检查只核新参照引理、下一移位及自由符号代数，不计作本稿终审。

## Claim

对任意素数 $p\ge5$、$a\ge2$，保持同一实际双谐波分支，令

$$
m=(p-1)/2,\qquad M=p^{a-1}m,\qquad D=p+m=3m+1,
\qquad \chi=(-1)^{m+1},\qquad C_D=[L^D]\mathcal B_3.
$$

本件计算已接受的 $pC_D\in h^{m+1}\mathcal O^+$ 之后的下一可能系数：

$$
\boxed{\overline{h^{-(m+1)}pC_D}=0.}
\tag{1}
$$

因此

$$
\boxed{pC_D\in h^{m+2}\mathcal O^+,\qquad
v_h([L^p]U_{\rm cl})\ge M-2m+1.}
\tag{2}
$$

仍不声称准确赋值；旧的下一可能高度 $M-2m$ 并非非零锚点。
不计算其他商系数，不据此宣称完整负 Newton 图或准确根斜率。

## Status

**PROVABLE AS STATED。** 本稿给出一个新的有限参照引理与完整的一阶后临界计算。
全局有理核 $R_{m+1,0}$ 的 $p$ 极部并未被宣称求出；
下文证明该全局极部不是本次有限端点计算的必要义务。

## Assumptions and accepted inputs

- $h=2-\zeta-\zeta^{-1}$，$\zeta$ 为任意本原 $p^a$ 次根，
  $K^+=\mathbb Q_p(h)$、$\mathcal O^+=\mathbb Z_p[h]$，
  $v_h(h)=1$、$v_h(p)=M\ge5m$。因此 $m\ge2$。
- 实际传播子为 $d_n=-(2-\zeta^n-\zeta^{-n})/h$。
  对 $1\le n<3p<p^a$ 它非零；$p\nmid n$ 时是单位，
  $v_h(d_p)=v_h(d_{2p})=2m$。
- 带权重幅度的实际递推为

  $$
  d_nV_n(b)=-\frac b2[x^{n-1}]e^{V(b)}-L[x^{n-2}]e^{2V(b)},
  \qquad V(0)=0\text{ 指 }x\text{ 的常数项为零}.
  \tag{3}
  $$

  实际原分支取 $b=1$，且
  $\mathcal B_3=-[x^{3p-1}]e^V-2L[x^{3p-2}]e^{2V}$。
- [预临界证明](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_PRECRITICAL_PROOF_V1_20260908.md)
  和其 [23 项独审](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_PRECRITICAL_INDEPENDENT_CHECK_V1_20260908.md)
  提供实际最高权重身份、有限整性、共振污染支撑与基带导数身份。
- [临界证明](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_CRITICAL_PROBE_V1_20260908.md)
  和其 [22 项独审](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_CRITICAL_INDEPENDENT_CHECK_V1_20260908.md)
  提供 $pC_D\in h^{m+1}\mathcal O^+$、临界响应及当时的误差边界。
  本件不重开这些已接受结论；只证明本次所需新精度。
- [高阶低块结构 Claim 1—2、Step 4](PAPER30_TWIST_THIRD_FORCING_HIGHER_RESPONSE_STRUCTURE_PROBE_V1_20260907.md)
  提供全阶有理性、极点阶数界、有限低块的 $p$ 整性。
  其全局有理核整性只覆盖 $k+j\le m$，不覆盖 $R_{m+1,0}$。
- 仅在推出商高度时使用已接受分解
  $S=h^{-D}p^2\mathcal B_3=P_{\rm cl}U_{\rm cl}$，其中
  $P_{\rm cl}$ 首一、次数 $m$，$U_{\rm cl}$ 次数 $p$。

## Notation

令 $u=Lx^2/4$，$V|_{b=0}=W(u)$、
$\partial_bV|_{b=0}=xA(u)$，并写

$$
W=\sum_{r\ge1}W_ru^r,\quad A=\sum_{r\ge0}A_ru^r,
\quad F_c=e^{cW}\ (c=1,2),\quad
\Theta=u\partial_u,\quad \mathcal Q=2\Theta+1.
$$

本次工作环为 $\mathscr R=\mathcal O^+/h^{m+2}\mathcal O^+$，其特征为 $p$。
低级数 $w=W_{<p}\bmod h^{m+2}$、$a=A_{<m}\bmod h^{m+2}$ 只用于允许截断。
令 $f_1=e^w$、$f_2=e^{2w}$，所需低系数次数小于 $p$，因而阶乘都是单位。

零阶低函数记为

$$
w_0=-\log(1-u),\quad a_0=\frac1{2(1-u)},\quad
f=\frac1{1-u},\quad g=f^2.
\tag{4}
$$

新增的奇响应级数是

$$
\mathscr H(u)=\sum_{r\ge0}\frac{u^r}{2r+1},\qquad
\mathcal Q\mathscr H=f.
\tag{5}
$$

它先在特征零中定义。约化时只使用 $r<m$ 的系数，
分母 $2r+1\le p-2$ 全为单位；不使用其含 $1/p$ 的 $u^m$ 项。

## Proof Strategy

先审定全局新核的真正已知边界，然后用与实际低带准确匹配的有限多项式参照替代它。
新参照的正规化指数误差至少为 $h^p$，足够覆盖本次 $h^{m+2}$ 精度。
随后保留下一 Chebyshev 移位和低解的一阶 $h$ 修正，求出两条高带的新响应。
最后精确计算端点里的有限奇数倒数和，证明该系数仍为零。

## Dependency Map

1. 实际权重递推与既有有限整性给出唯一计算对象和截断范围。
2. 新有限参照引理直接替代未知的全局 $R_{m+1,0}$ 极部。
3. 下一 Chebyshev 移位确定一阶后临界驱动。
4. 低解 $w_1,a_1$ 及两响应 $t_1,s_1$ 由单位三角方程唯一确定。
5. 端点有限系数的自由符号求和给 (1)；真实误差界再给 (2)。

## Proof

### Step 1. 全局新核的边界与本次采用的替代

先准确说明旧理论对 $R_{m+1,0}$ 能推出什么。
全阶有理性给

$$
R_{m+1,0}(u)=\frac{A(u)}{(1-u)^{p+1}},\qquad \deg A\le p+1.
\tag{6}
$$

有限低块给 $R_{m+1,0}$ 的 $u^0,\ldots,u^{p-1}$ 系数 $p$ 整；
乘以整数多项式 $(1-u)^{p+1}$ 后，得到 $A$ 的前 $p$ 个系数 $p$ 整。
因此未受此信息确定的非整分子系数只可能位于 $u^p,u^{p+1}$。
但这不控制这两个系数各自的 $p$ 极点阶数，不能推出 $pR$ 或 $p^2R$ 必整。
若另取足够大的最小 $e>0$ 使 $p^eA$ 整，则其剩余确实形如
$u^p(\alpha+\beta u)$；这一描述本身不确定 $e,\alpha,\beta$。

本次不继续假定或求解这些全局未知量，而采用下列独立有限引理。

**有限多项式参照引理。** 假设 $W_r\in\mathcal O^+$ 且
$W_r\equiv1/r\pmod h$ 对 $1\le r<p$ 成立，$M\ge p$。
定义

$$
T(u)=\sum_{r=1}^{p-1}W_ru^r,\qquad
Q_{\rm ref}(u)=T(u)-\sum_{r=1}^{p-1}\frac{u^r}{r}
\in h\mathcal O^+[u],\qquad
G(u)=-\log(1-u)+Q_{\rm ref}(u).
\tag{7}
$$

则 $G_{<p}=W_{<p}$ 准确。对 $c=1,2$、$N<2p$，有

$$
p[u^N]e^{cG}\in h^{\min(M,p)}\mathcal O^+=h^p\mathcal O^+,
\qquad
pG_{p+j}\equiv\mathbf1_{j=0}\pmod{h^p}\quad(0\le j<p).
\tag{8}
$$

第二式只在 $p+j<2p$ 使用。如果实际 $pW_{p+j}$ 已整，令
$\tau_j=pW_{p+j}\bmod h^p$，则

$$
p[u^{p+j}]F_c=[u^j]\,c e^{cT}(\tau-1)\pmod{h^p}.
\tag{9}
$$

**证明。** $Q_{\rm ref}$ 无常数项，每个系数含 $h$，且其次数小于 $p$。
因此 $G_{<p}=T$，而 $G_r=1/r$ 对 $r\ge p$ 成立；(8) 的第二式由
$G_p=1/p$ 及其余所需 $r$ 是 $p$ 单位得到。
对第一式，准确形式身份为

$$
e^{cG}=(1-u)^{-c}e^{cQ_{\rm ref}}.
$$

$c=1,2$ 保证左边分解中的 $(1-u)^{-c}$ 系数全部为整数。
在 $u^N$ 内，指数至多使用 $q\le N<2p$ 个 $Q_{\rm ref}$ 因子。
若 $q<p$，乘 $p$ 后高度至少 $M$；若 $p\le q<2p$，则
$v_p(q!)=1$，乘 $p$ 后高度至少 $q\ge p$。这证明 (8)。

因 $W-G$ 始于 $u^p$，模 $u^{2p}$ 准确有
$e^{cW}=e^{cG}(1+c(W-G))$。
与高带相乘的低指数下标小于 $p$，其系数整且与实际低指数准确相同；
高带的 $p$ 倍也已整。乘 $p$、使用 (8)，得到 (9)。证毕。

这个 $G$ 不被要求求解完整递推，也没有替换实际 $W_p$。
其用途只是有限指数比较；因此 $R_{m+1,0}$ 的全局极部即使存在，也不构成本次端点义务。
由于 $p=2m+1\ge m+2$，(9) 可在 $\mathscr R$ 中使用。

### Step 2. 实际高带、支撑与计算窗口

已接受的权重身份为

$$
d_{2r}W_r=-4[u^{r-1}]F_2,\qquad
d_{2r+1}A_r=-\frac12[u^r]F_1-8[u^{r-1}]F_2A,
\tag{10}
$$

$$
4^DC_D=-[u^{p+m}]F_1-16[u^{p+m-1}]F_2A.
\tag{11}
$$

所需 $W$ 至 $p+m$，$A$ 至 $p+m-1$；没有内部 $V_{3p}$。
已有单位三角整性给 $W_r$ 整且剩余 $1/r$ 对 $r<p$ 成立，
$A_r$ 整对 $r<m$ 成立，正规化高带 $pW_{p+j}$、$pA_{p+j}$ 在所需范围内整。
这些正是 Step 1 的实际前提。

本次提高精度仍可排除同一共振污染：
$v_h(W_p),v_h(A_r)\ge-2m$ 对 $m\le r<p$，因此它们乘 $p$ 后高度至少
$M-2m\ge3m\ge m+2$。
当总次数 $N\le p+m-1$ 时，中间响应下标 $r\ge m$ 只可能乘指数下标
$N-r\le p-1$ 的整系数；非整指数带和该响应的最短乘积次数为 $p+m$，不出现。
两个高带的乘积也因最低次数为 $2p$ 不出现。

在 $\mathscr R$ 中写

$$
\tau=\sum_{j=0}^{m}(pW_{p+j})u^j,\quad
\sigma=\sum_{j=0}^{m-1}(pA_{p+j})u^j,\quad
E_1=f_1(\tau-1),\quad E_2=2f_2(\tau-1).
\tag{12}
$$

所有这些量已整后才进入 $\mathscr R$；$\tau_0=0$。
Step 1 和上述支撑给

$$
4^DpC_D=-[u^m]E_1-16[u^{m-1}](f_2\sigma+E_2a)
\quad\text{在 }\mathscr R\text{ 中}.
\tag{13}
$$

### Step 3. 下一 Chebyshev 移位，包含最小素数边界

本件需要在既有临界移位后多保留一阶。结果为

$$
\boxed{d_{2p+n}(H)-d_n(H)
=4\chi nH^m-\frac{\chi n(4n^2-1)}6H^{m+1}
+O(H^{m+2})\quad\text{于 }\mathbb F_p[[H]].}
\tag{14}
$$

这里只用 $1\le n<p$。
为证明，置 $z=1+\eta$、$H=-\eta^2/(1+\eta)$。
在特征 $p$ 中 $z^p=1+\eta^p$，从真实 Chebyshev 差式展开得到

$$
d_{2p+n}-d_n
=\frac{2\eta^p(z^n-z^{-n})}{H}+O(\eta^{4m}).
$$

二次及更高的 $\eta^p$ 项在除以 $H$ 后至少为 $\eta^{2p-2}=\eta^{4m}$。
又有

$$
\frac{z^n-z^{-n}}{z-z^{-1}}
=n-\frac{n(n^2-1)}6H+O(H^2),
$$

这可由初值 $S_0=0,S_1=1$ 与递推 $S_{n+1}=(2-H)S_n-S_{n-1}$
分别比较常数项和一次项证明。
剩余因子为

$$
\frac{2\eta^p(z-z^{-1})}{H}
=2\chi H^m(2+\eta)(1+\eta)^m.
$$

因 $m\equiv-1/2\pmod p$，展开至 $\eta^3$ 给
$(2+\eta)(1+\eta)^m=2-H/4+O(\eta^4)$。
相乘即得 (14) 中两项；误差的 $\eta$ 阶数至少为 $2(m+2)$，
因为 $4m\ge2(m+2)$。完整差式是 $H$ 多项式，且 $v_\eta(H)=2$，
所以该误差确实属于 $H^{m+2}$。
当 $p=5,m=2$ 时，二次移位恰从 $H^4=H^{m+2}$ 开始，仍可舍去；
分母 $6,8$ 都是单位，没有边界素数例外。

代入真实 $H=h$ 后，模 $p$ 系数误差高度至少 $M\ge m+2$。
因此 (14) 在 $\mathscr R$ 中给出实际算子差

$$
\Delta_e=h^m(\delta_{e0}+h\delta_{e1}),\quad
\delta_{e0}=8\chi\Theta,\quad
\delta_{e1}=-\frac\chi3(16\Theta^3-\Theta),
\tag{15}
$$

$$
\Delta_o=h^m(\delta_{o0}+h\delta_{o1}),\quad
\delta_{o0}=4\chi\mathcal Q,\quad
\delta_{o1}=-\frac\chi6(4\mathcal Q^3-\mathcal Q).
\tag{16}
$$

偶式对 $1\le j\le m$ 使用，奇式对 $0\le j<m$ 使用；其实际对角元均为单位。

### Step 4. 一阶低解，保留非有理的有限奇响应

写 $w=w_0+hw_1+O(h^2)$、$a=a_0+ha_1+O(h^2)$，只在各自允许低次数提取。
真实 Chebyshev 一次系数为
$[H]d_n=n^2(n^2-1)/12$，因此定义

$$
\mathcal L_{e0}=-4\Theta^2+8ug,\quad
\mathcal L_{o0}=-\mathcal Q^2+8ug,
\quad
\mathcal D_{e1}=\frac{4\Theta^4-\Theta^2}{3},\quad
\mathcal D_{o1}=\frac{\mathcal Q^4-\mathcal Q^2}{12}.
\tag{17}
$$

从 (10) 的低带一次 $h$ 系数得到

$$
\mathcal L_{e0}w_1=-\mathcal D_{e1}w_0,
\qquad
\mathcal L_{o0}a_1=-\frac12fw_1-\mathcal D_{o1}a_0-16ugw_1a_0.
\tag{18}
$$

其解为

$$
\boxed{w_1=\frac{u(1+u)}{4(1-u)^2},\qquad
a_1=\frac{1+16u+7u^2}{48(1-u)^3}
-\frac{1+u}{48(1-u)}\mathscr H(u).}
\tag{19}
$$

验证方法是对 (19) 逐项使用 $\Theta\mathscr H=(f-\mathscr H)/2$，
代入 (18)；两边相等。$w_1(0)=a_1(0)=0$。
第一式的单位对角元为 $-4j^2$，$1\le j\le m$；
第二式为 $-(2j+1)^2$，$0\le j<m$。这证明所需有限解的唯一性。
式 (19) 中所有被使用的 $\mathscr H$ 系数都 $p$ 整，分母 $48$ 也是单位。
这里没有将 $a_1$ 冒称为全局有理核，或在低奇带使用 $1/p$。

令

$$
\mathcal L_{e1}=\mathcal D_{e1}+16ugw_1,
\qquad \mathcal L_{o1}=\mathcal D_{o1}+16ugw_1.
\tag{20}
$$

这是 $\mathcal D_e+8uf_2$ 与 $\mathcal D_o+8uf_2$ 的一次 $h$ 系数。

### Step 5. 两条高带的新响应方程与显式解

保持已接受的精确基带导数解

$$
\tau^{\rm b}=-2\Theta w,\qquad \sigma^{\rm b}=-\mathcal Q a.
$$

在 $\mathscr R$ 中写

$$
\tau=\tau^{\rm b}+h^m(t_0+ht_1),\qquad
\sigma=\sigma^{\rm b}+h^m(s_0+hs_1).
\tag{21}
$$

临界项已接受且为

$$
t_0=-\frac{4\chi u}{1-u},\qquad
s_0=-\frac{2\chi}{(1-u)^2}.
\tag{22}
$$

为本次新项设置
$\tau^{\rm b}_0=-2\Theta w_0$、$\tau^{\rm b}_1=-2\Theta w_1$、
$\sigma^{\rm b}_0=-\mathcal Q a_0$、$\sigma^{\rm b}_1=-\mathcal Q a_1$。
将 (15)—(16)、(20)—(21) 代入实际高带方程，并扣除基带和已接受临界项，得到

$$
\mathcal L_{e0}t_1
=-\mathcal L_{e1}t_0-\delta_{e0}\tau^{\rm b}_1
-\delta_{e1}\tau^{\rm b}_0,
\tag{23}
$$

$$
\begin{aligned}
\mathcal L_{o0}s_1={}&-\mathcal L_{o1}s_0
-\frac f2(t_1+w_1t_0)\\
&-16ug\{a_0t_1+(2w_1a_0+a_1)t_0\}
-\delta_{o0}\sigma^{\rm b}_1-\delta_{o1}\sigma^{\rm b}_0.
\end{aligned}
\tag{24}
$$

没有保留两个临界修正的乘积，因为其高度至少 $2m\ge m+2$。
新响应的显式解是

$$
\boxed{t_1=\frac{\chi u(1-8u-u^2)}{2(1-u)^3},}
\tag{25}
$$

$$
\boxed{s_1=\chi\left\{
\frac{7-51u-87u^2-13u^3}{24(1-u)^4}
+\frac{-1+4u+u^2}{24(1-u)^2}\mathscr H(u)
\right\}.}
\tag{26}
$$

完整代数验证可按下列展开源项逐项执行。
(23) 的右端为

$$
\frac{2\chi u(9u^3+45u^2+27u-1)}{(1-u)^5},
$$

它等于 $\mathcal L_{e0}$ 作用于 (25)。
(24) 的右端为

$$
\chi\left\{
\frac{6u^5+521u^4+2632u^3+1882u^2+146u-3}{12(1-u)^6}
-\frac{2u(1+u)^2}{3(1-u)^4}\mathscr H(u)
\right\},
$$

使用 (5) 求导，$\mathcal L_{o0}$ 作用于 (26) 也给该式。
由与 Step 4 相同的单位三角性，(25)—(26) 是所需范围内的唯一解。
尤其 $s_1(0)=\chi/4$，不能置零。
作为常数项复核，真实奇入口为

$$
d_{2p+1}=-1+4\chi h^m-\frac\chi2h^{m+1}
\quad\text{在 }\mathscr R\text{ 中},
$$

故 $\sigma_0=1/(2d_{2p+1})=-1/2-2\chi h^m+(\chi/4)h^{m+1}$，与 (21)—(26) 一致。

### Step 6. 完整端点的一阶后临界核

基带仍满足准确身份

$$
E_1^{\rm b}=-(1+2\Theta)f_1,\qquad
f_2\sigma^{\rm b}+E_2^{\rm b}a=-(3+2\Theta)(f_2a).
$$

将 (21) 代入 (13)，基带端点的两个系数均为 $2m+1=p$，在 $\mathscr R$ 中为零。
临界端点系数已接受为 $4\chi m(2m+1)^2$，也为零。
剩下的 $h^{m+1}$ 系数准确为

$$
\mathfrak c_{m,1}=-[u^m]J(u)-16[u^{m-1}]K(u),
\tag{27}
$$

其中必须同时包含低带的一阶修正、两条高带的新项及指数的一阶修正：

$$
\begin{aligned}
J&=f(t_1+w_1t_0)
=\frac{\chi u(1-10u-3u^2)}{2(1-u)^4},\\
K&=g\{s_1+2a_0t_1+2a_1t_0+2w_1(s_0+2a_0t_0)\}\\
&=\chi\left\{
\frac{7-67u-319u^2-101u^3}{24(1-u)^6}
+\frac{-1+8u+5u^2}{24(1-u)^4}\mathscr H(u)
\right\}.
\end{aligned}
\tag{28}
$$

这两个身份直接从 (19)、(22)、(25)—(26) 代入化简得到。
相应实际比较为

$$
4^DpC_D=h^{m+1}\overline{\mathfrak c_{m,1}}
\quad\text{在 }\mathscr R\text{ 中}.
\tag{29}
$$

### Step 7. 端点有限求和；不把特征零分母擅自模五求逆

令

$$
H_{\rm odd}(m)=\sum_{r=0}^{m-1}\frac1{2r+1}\in\mathbb Z_{(p)}.
\tag{30}
$$

对 (28) 的两个有理部分，特征零二项式系数恒等式给

$$
\begin{aligned}
J_m^*&=[u^{m-1}]\frac{1-10u-3u^2}{(1-u)^4}
=-m(2m^2-2m-1),\\
R_m^*&=[u^{m-1}]\frac{7-67u-319u^2-101u^3}{(1-u)^6}
=-\frac{m(m+1)(2m+1)(12m^2-24m+5)}6.
\end{aligned}
\tag{31}
$$

式 (31) 先在特征零验证，再使用其右侧的 $p$-单位分母表达式。
特别是第二式若写成五次二项式，暂时可能出现 $120$；
本件不在 $p=5$ 时对 $120$ 取逆，完整化简后的分母只有 $6$。

对奇级数部分，定义

$$
P(n)=[u^n]\frac{-1+8u+5u^2}{(1-u)^4}
=(n+1)^2(2n-1).
$$

于是该卷积系数为
$\sum_{r=0}^{m-1}P(m-1-r)/(2r+1)$。
自由符号多项式除法给出准确身份

$$
\frac{P(m-1-r)}{2r+1}
=-r^2+(3m-1)r-3m^2+\frac{3m+1}{2}
+\frac{(m-1)(2m+1)^2}{2(2r+1)}.
\tag{32}
$$

将多项式部分从 $r=0$ 求和至 $m-1$，结果为
$-m(11m^2-5)/6$。因此

$$
\begin{aligned}
Q_m^*&=[u^{m-1}]\frac{-1+8u+5u^2}{(1-u)^4}\mathscr H(u)\\
&=-\frac{m(11m^2-5)}6
+\frac{(m-1)(2m+1)^2}{2}H_{\rm odd}(m).
\end{aligned}
\tag{33}
$$

代入 $\mathfrak c_{m,1}=\chi\{-J_m^*/2-(2/3)(R_m^*+Q_m^*)\}$，
完整化简得到

$$
\boxed{\mathfrak c_{m,1}=\chi\left\{
\frac{m(2m+1)(8m^3-8m^2-6m-3)}6
-\frac{(m-1)(2m+1)^2}{3}H_{\rm odd}(m)
\right\}.}
\tag{34}
$$

$H_{\rm odd}(m)$ 中没有 $1/p$，因为最大的分母是 $2m-1=p-2$。
最终分母 $2,3$ 都为单位，故 $p\ge5$ 下均可约化。
使用 $2m+1=p$，式 (34) 的两个项均在 $p\mathbb Z_{(p)}$ 中，因此

$$
\overline{\mathfrak c_{m,1}}=0.
\tag{35}
$$

由 (29)、$4$ 为单位、实际 $pC_D$ 已整，得到 $pC_D\in h^{m+2}\mathcal O^+$，
即 (1) 及 (2) 的第一部分。
首一性给 $[L^p]U_{\rm cl}=h^{-D}p^2C_D$，于是

$$
v_h([L^p]U_{\rm cl})\ge M-D+(m+2)=M-2m+1.
$$

这完成 (2)，没有主张等号。证毕。$\square$

### Step 8. 本次新精度的实际误差核对

| 来源 | 可保证的高度或支撑 | 本次处理 |
| --- | --- | --- |
| 有限参照的正规化指数误差 | $\min(M,p)=p\ge m+2$ | 可舍 |
| $pW_p$、中间奇响应乘整低指数 | $M-2m\ge3m\ge m+2$ | 可舍 |
| 非整指数与中间奇响应相遇 | 最低 $u$ 次数 $p+m=D$ | 目标 $D-1$ 不出现 |
| 两个高带相乘 | 最低 $u$ 次数 $2p$ | 不出现 |
| 模 $p$ Chebyshev 系数提升误差 | $M\ge m+2$ | 可舍 |
| 下一移位的未保留项 | $m+2$ | 可舍 |
| 两个临界响应或移位修正相乘 | $2m\ge m+2$ | 可舍；$p=5$ 恰达边界 |
| 低带 $O(h^2)$ 乘临界响应 | $m+2$ | 可舍 |

最后一行的低带整性由实际单位三角递推保证；没有假设未受控制的全局核整性。
所有约化前的量均在其所需乘 $p$ 正规化后证明为整，
也没有用形式端点中的额外 $p$ 因子外推超出 $h^{m+2}$ 的误差精度。

### 定向核验记录

本件对自由符号执行了以下准确身份核验，无素数扫描或根拟合：

- 使用 $\Theta\mathscr H=(f-\mathscr H)/2$ 核验 $a_1,t_1,s_1$ 的三条响应方程。
- 核验完整后临界端点核 $J,K$。
- 对 (32) 作自由符号除法、对多项式部分作符号求和，并核验 (34)。

上述六项代数残差均为零；有界子检查独立得到同样结果。
子检查还独立核对有限多项式参照引理与 (14) 的下一移位和边界。
这些作者侧交叉核算不替代整稿的非作者独立审查。

## Corrections or Missing Assumptions

- 旧 $R_{k,0}$ 全局整性没有被外推到 $k=m+1$；其未知极部仍未求出。
  本次用与实际低带准确匹配的有限参照消除了对该非必要全局义务的依赖。
- 新引理不要求参照 $G$ 求解完整递推；实际 $W$ 的高带仍由真实递推求解。
- 新奇响应必须保留 $\mathscr H$，不能在这一步假设 $a_1$ 是全局有理函数。
- 不丢弃 $s_1(0)$、$2a_1t_0$ 或低指数一次修正；它们都在 (28) 的完整端点中。
- $p=5$ 不单独数值处理：全部可约化的最终系数分母为单位；
  中间除以 $120$ 的特征零写法只经整体恒等式化简后约化。

## Open Risks

- $h^{m+2}$ 的下一系数仍未计算，最高商系数的准确赋值尚未确定。
- 有限参照引理的误差下界为 $h^p$，不是无限精度；
  临界响应的二次项从 $h^{2m}$ 开始，$p=5$ 时它们恰进入下一层。
  不能用本件的一次响应形式自动继续。
- 全局 $R_{m+1,0}$ 的极部、归一化阶数及端点本身并未由本件计算；
  只证明其不是本次有限实际最高系数计算的必要输入。
- 其他商系数、完整负 Newton 多边形、因子型、简单性和野分裂域均不在本件结论内。
- 本件仍是新作者稿，需另作非作者独立核查；未改变任何项目接受或发布状态。
