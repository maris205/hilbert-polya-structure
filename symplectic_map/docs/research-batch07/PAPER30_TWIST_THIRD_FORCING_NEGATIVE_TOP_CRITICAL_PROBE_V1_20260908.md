# Proof Package：负端最高参数系数的临界层仍消失

日期：2026-09-08。作者：`/root/negative_top_alternative`。
本件是新的有界作者推导，不计作非作者审查；只计算紧邻预临界结果的一个临界层。
不扫素数、不拟合、不计算其他商系数，不重审任何已接受正簇结论。

## Claim

保持同一实际双谐波分支。对任意素数 $p\ge5$、$a\ge2$，令

$$
m=(p-1)/2,\qquad M=p^{a-1}m,\qquad D=p+m=3m+1,
\qquad \chi=(-1)^{m+1}.
$$

记 $C_D=[L^D]\mathcal B_3$。本件计算的临界剩余为

$$
\boxed{\overline{h^{-m}pC_D}=0.}
\tag{1}
$$

等价地，本件证明

$$
\boxed{pC_D\in h^{m+1}\mathcal O^+.}
\tag{2}
$$

因此，仅对最高商系数可继续推出

$$
v_h([L^p]U_{\rm cl})\ge M-D+m+1=M-2m.
\tag{3}
$$

这不是准确赋值；没有声称下一层非零，也没有从形式系数中的 $p^2$ 因子
推出两个额外的实际 $p$-进赋值。

## Status

**PROVABLE AS STATED。** 临界 $h^m$ 层为零，不能作为新的非零负端锚点。
下文直接在 $\mathcal O^+/h^{m+1}\mathcal O^+$ 中验证实际最高系数为零，
故其论证也给出 (1) 所需的预临界整除性。
[预临界证明](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_PRECRITICAL_PROOF_V1_20260908.md)
现已通过
[23 项独立核查](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_PRECRITICAL_INDEPENDENT_CHECK_V1_20260908.md)，
在本件作为已接受接续输入；本件自己的新临界层仍是待独立核查的作者结果。

## Assumptions and accepted inputs

- $h=2-\zeta-\zeta^{-1}$，$\zeta$ 为任意本原 $p^a$ 次根；
  $K^+=\mathbb Q_p(h)$，$\mathcal O^+=\mathbb Z_p[h]$，
  $v_h(h)=1$、$v_h(p)=M$。因此 $M\ge5m$、$m\ge2$。
- 实际传播子和带幅度的实际有限递推为

  $$
  d_n=-\frac{2-\zeta^n-\zeta^{-n}}h,\qquad
  d_nV_n(b)=-\frac b2[x^{n-1}]e^{V(b)}-L[x^{n-2}]e^{2V(b)}
  \quad(1\le n<3p).
  \tag{4}
  $$

  实际原分支取 $b=1$，$x$ 的常数项为零。
  $p\nmid n$ 时 $d_n$ 为单位；$v_h(d_p)=v_h(d_{2p})=2m$。
- 第三 forcing 为

  $$
  \mathcal B_3=-[x^{3p-1}]e^V-2L[x^{3p-2}]e^{2V}.
  \tag{5}
  $$

- 已接受的 Chebyshev 临界移位，在 $\mathbb F_p[[H]]$ 中满足

  $$
  d_{2p+n}(H)-d_n(H)=4\chi nH^m+O(H^{m+1})
  \qquad(1\le n<p).
  \tag{6}
  $$

  所需依据是
  [第二阶乘响应桥 Step 5、式 (34)—(35)](PAPER30_TWIST_PRIME_POWER_SECOND_FACTORIAL_RESPONSE_BRIDGE_PROBE_V1_20260907.md)
  及其
  [联合独审的移位核查](PAPER30_TWIST_THIRD_FORCING_GENERAL_AND_BRIDGE_INDEPENDENT_CHECK_20260907.md)。
  这是 $\Delta_k(n)=2k\chi nH^m+O(H^{m+1})$ 的 $k=2$ 特例。
- 已接受的单谐波正阶有理核整性：若

  $$
  P(H,0,4z)=-2\log(1-z)+\sum_{k\ge1}H^kR_{k,0}(z),
  $$

  则对 $1\le k\le m$ 有
  $R_{k,0}\in\mathbb Z_{(p)}[z,(1-z)^{-1}]$，且 $R_{k,0}(0)=0$。
  本件明确使用临界 $k=m$，依据
  [高阶低块结构 Claim 1—2、Step 4](PAPER30_TWIST_THIRD_FORCING_HIGHER_RESPONSE_STRUCTURE_PROBE_V1_20260907.md)
  及已接受的
  [统一正簇独立核查](PAPER30_TWIST_THIRD_FORCING_UNIFORM_POSITIVE_CLUSTER_INDEPENDENT_CHECK_20260907.md)。
  只调用该有理核结论，不调用正簇根结构。
- 仅在推出 (3) 时使用 $S=h^{-D}p^2\mathcal B_3=P_{\rm cl}U_{\rm cl}$，
  $P_{\rm cl}$ 首一、次数 $m$，$U_{\rm cl}$ 次数 $p$。

## Notation

令 $u=Lx^2/4$，定义纯偶部分和一次奇响应

$$
V|_{b=0}=W(u),\qquad \left.\partial_bV\right|_{b=0}=xA(u),
\qquad \Theta=u\partial_u,
$$

$$
W=\sum_{r\ge1}W_ru^r,\qquad A=\sum_{r\ge0}A_ru^r,
\qquad F_c=e^{cW}\quad(c=1,2).
$$

工作环为 $R_*=\mathcal O^+/h^{m+1}\mathcal O^+$，它具有特征 $p$。
$\bar f$ 单独表示模 $h$ 的剩余；未加横线但指明“在 $R_*$ 中”的等式表示模
$h^{m+1}$。所有指数只作为有限形式系数使用，不主张解析收敛。

在 $R_*$ 中令 $w$ 为 $W_{<p}$ 的约化，$a$ 为 $A_{<m}$ 的约化，
并写 $f_1=e^w$、$f_2=e^{2w}$；这里它们只用次数小于 $p$ 的整系数。
模 $h$ 的低解记为

$$
w_0=-\log(1-u),\quad a_0=\frac1{2(1-u)},\quad
f_{10}=\frac1{1-u},\quad f_{20}=\frac1{(1-u)^2}.
\tag{7}
$$

对数只在次数小于 $p$ 使用，或在取正阶导数后使用其有理表达式。

## Proof Strategy

将预临界的实际单阶乘比较提高一阶；所需新输入恰为 $R_{m,0}$ 的整性。
保留两个传播子的临界移位，不继续把它们视为不变。
用零阶单位线性算子求出偶、奇两个临界响应，再在真实最高系数的端点提取中相加。
全部误差先在特征零证明整性和高度，再进入 $R_*$。

## Dependency Map

1. 权重给实际递推和最高系数恒等式 (8)—(9)。
2. 低带整性、共振界与单阶乘支撑保证所有正规化高带整。
3. $R_{m,0}$ 整性、倍角身份和指数误差界给模 $h^{m+1}$ 的单阶乘比较 (15)。
4. 临界移位 (6) 给出 (16)；两个单位三角响应确定 (22)、(27)。
5. 完整端点提取 (29)—(31) 证明 (1)—(2)；首一性只用于 (3)。

## Proof

### Step 1. 不变的实际最高系数身份

在 (4) 中赋 $b$ 权重一、$L$ 权重二。按 $x$ 次数三角归纳得
$[L^j]V_n(b)$ 与 $b^{n-2j}$ 成比例。
取纯偶项和 $b$ 的一次响应，得到

$$
d_{2r}W_r=-4[u^{r-1}]F_2,
\qquad
d_{2r+1}A_r=-\frac12[u^r]F_1-8[u^{r-1}]F_2A.
\tag{8}
$$

第一式只需 $1\le r\le D$，第二式只需 $0\le r\le D-1$。
第一 forcing 的最高 $L^D$ 项取 $b^0$；第二 forcing 的最高项取 $b^1$，
其中 $\partial_be^{2V}|_{b=0}=2xAe^{2W}$。
连同外部的 $-2L$ 及 $Lx^2=4u$，给准确恒等式

$$
4^DC_D=-[u^{p+m}]F_1-16[u^{p+m-1}]F_2A.
\tag{9}
$$

不存在对 $V_{3p}$ 的除法；$W_p$、$A_m$ 仍是实际值，未被投影置零。

### Step 2. 共振污染在本次精度仍可排除

因为次数小于 $p$ 的指数阶乘分母均为 $p$ 单位，(8) 的单位三角递推给

$$
W_r\in\mathcal O^+\ (r<p),\qquad
[u^r]F_c\in\mathcal O^+\ (r<p),\qquad
A_r\in\mathcal O^+\ (r<m).
$$

在 $r=p$ 的纯偶式与 $r=m$ 的奇式，右端仅使用以上整系数，故
$v_h(W_p),v_h(A_m)\ge-2m$。
在 $m<r<p$ 的奇式，除数再次为单位且指数次数小于 $p$；归纳给

$$
v_h(A_r)\ge-2m\quad(m\le r<p).
\tag{10}
$$

因此上述非整量乘 $p$ 后均属于 $h^{M-2m}\mathcal O^+$。
本次精度下

$$
M-2m\ge3m\ge m+1,
\tag{11}
$$

所以其单项贡献为零。对积仍须检查支撑：若 $N\le D-1=p+m-1$ 且
$A$ 的下标 $s\in[m,p-1]$，则对应指数下标 $N-s\le p-1$，指数系数整。
其乘 $p$ 后的高度仍至少 $M-2m$，不能被非整指数降低。
若指数下标至少为 $p$，响应下标就不超过 $m-1$，只能来自整低奇带。
若响应下标至少为 $p$，则指数下标小于 $m$。
两个高带的乘积最低次数为 $2p>D-1$。

这同时说明：共振响应与非整指数的最短相遇次数为 $p+m=D$，不在 (9) 的范围内。
该支撑结论不是把 $pA_m\equiv0$ 无条件乘以任意非整系数。

最后，按高带下标归纳，利用每个指数总次数小于 $2p$ 时至多一个阶乘 $p$ 分母、
至多一个高带因子，得

$$
pW_{p+j}\in\mathcal O^+\quad(0\le j\le m),\qquad
pA_{p+j}\in\mathcal O^+\quad(0\le j<m).
\tag{12}
$$

偶带由 $W_p$ 的界开始；后续除数 $d_{2p+2j}$ 为单位。
奇带用上面的积支撑归纳，除数 $d_{2p+2j+1}$ 对 $0\le j<m$ 均为单位。
同一论证保证 (9) 乘 $p$ 后整，后面所有约化均有定义。

### Step 3. 单阶乘参照可以合法保留到临界阶

特征零倍角身份为

$$
d_{2r}(H)=(4-H)d_r(H(4-H)).
$$

设 $H_2=H(4-H)$。纯偶形式解的准确参照是

$$
G(H,u)=\frac12P\left(H_2,0,\frac{16u}{4-H}\right).
\tag{13}
$$

把 (13) 代入单谐波方程，右端为
$-4u e^{2G}/(4-H)$；乘 $4-H$ 得 (8) 的纯偶方程。
特征零零常数三角唯一性保证 (13) 是同一形式解。
注意这里的单谐波未知量是 $2G$；相应方程的右端是
$-8u e^{2G}/(4-H)$，除以二才得到以上 $G$ 的方程。

使用 $1\le k\le m$ 的全部已接受有理核整性，对 $H_2$ 和
$c(H)u=4u/(4-H)$ 作有限 Taylor 替换，得到

$$
G(H,u)=-\log(1-c(H)u)+Q(H,u)\pmod{H^{m+1}},
\qquad Q\in H\mathbb Z_{(p)}[u,(1-u)^{-1}][H]/(H^{m+1}),
\quad Q(H,0)=0.
\tag{14}
$$

选 (14) 的有限多项式提升，代入 $H=h$，仍记为 $Q$，并取准确单位
$c=(1-h/4)^{-1}$。以下 $G=-\log(1-cu)+Q$ 只作有限系数参照。
对 $r<p$，实际 $W_r(H)$ 的三角除数常数 $-4r^2$ 是 $p$ 单位，
故其整个 $H$-Taylor 展开 $p$ 整；与 (13)—(14) 比较给
$W_r-[u^r]G\in h^{m+1}\mathcal O^+$。

对 $N<2p$，$[u^N]Q$ 整且含 $h$。
所以 $p[u^{p+j}]G$ 在 $R_*$ 中仅可能由对数的下标 $p$ 项贡献，
该贡献为 $c^p$。在特征 $p$ 的 $R_*$ 中，$h^p=0$，因为
$p=2m+1\ge m+1$；于是 $c^p=(1-h^p/4^p)^{-1}=1$。

对指数需另作估值。准确的有限形式身份是
$e^{c_0G}=(1-cu)^{-c_0}e^{c_0Q}$，$c_0=1,2$。
在 $u^N$ 中，$e^{c_0Q}$ 至多用 $q\le N<2p$ 个 $Q$ 因子。
$q<p$ 时乘 $p$ 后各项高度至少 $M$；$p\le q<2p$ 时
$v_p(q!)=1$，乘 $p$ 后高度至少 $q\ge p>m$。
两类都属于 $h^{m+1}\mathcal O^+$，故
$p[u^N]e^{c_0G}=0$ 在 $R_*$ 中成立。

定义正规化实际高带

$$
\tau(u)=\sum_{j=0}^{m}(pW_{p+j}\bmod h^{m+1})u^j,
\qquad
\sigma(u)=\sum_{j=0}^{m-1}(pA_{p+j}\bmod h^{m+1})u^j.
$$

比较实际 $W$ 与参照 $G$，由于高带平方始于 $u^{2p}$，得到

$$
p[u^{p+j}]F_1=[u^j]E_1,\qquad
p[u^{p+j}]F_2=[u^j]E_2,\qquad
E_1=f_1(\tau-1),\quad E_2=2f_2(\tau-1)
\quad\text{在 }R_*\text{ 中}.
\tag{15}
$$

所需范围为 $0\le j\le m$。
误差的逐项理由是：低带差含 $h^{m+1}$；低带指数在次数小于 $2p$ 时最多
有一个阶乘 $p$ 分母，先乘 $p$ 仍保留该高度。
若低带差与高带相乘，高带只有一个且其 $p$ 倍整；余下低指数次数小于 $p$，
仍保留 $h^{m+1}$。因此 (15) 不是对非整指数直接作形式约化。
由 (11) 又有 $\tau_0=0$ 在 $R_*$ 中成立。

### Step 4. 临界移位的算子与实际误差

在低带定义对角算子
$\mathcal D_eu^j=d_{2j}u^j$、$\mathcal D_ou^j=d_{2j+1}u^j$。
式 (6) 先在 $\mathbb F_p[[H]]$ 中成立；实际 $d_n(H)$ 均为整系数多项式，
故其低于 $H^{m+1}$ 的系数差，除去式 (6) 指定项后都是 $p$ 倍。
代入 $h$ 后这些 $p$ 倍项高度至少 $M\ge m+1$，高阶项也在 $h^{m+1}$ 中。
因此实际移位在 $R_*$ 中准确为

$$
\begin{aligned}
d_{2p+2j}-d_{2j}&=8\chi jh^m\quad(1\le j\le m),\\
d_{2p+2j+1}-d_{2j+1}&=4\chi(2j+1)h^m\quad(0\le j<m).
\end{aligned}
\tag{16}
$$

记 $\mathcal L_e=\mathcal D_e+8uf_2$、
$\mathcal L_o=\mathcal D_o+8uf_2$。
由 (8)、(15)—(16)，实际高带满足

$$
(\mathcal L_e+8\chi h^m\Theta)\tau=8uf_2
\pmod{u^{m+1}},
\tag{17}
$$

$$
(\mathcal L_o+4\chi h^m(2\Theta+1))\sigma
=-\frac12E_1-8uE_2a\pmod{u^m}.
\tag{18}
$$

奇式所有中间共振项已由 Step 2 在模 $h^{m+1}$ 排除。
对偶式的正下标、奇式的全部下标，真实移位传播子对角元都是单位。
偶式常数项单独指定 $\tau_0=0$，不使用 $d_0^{-1}$ 或 $d_{2p}^{-1}$。

### Step 5. 偶带临界响应

低带纯偶方程为 $\mathcal D_ew=-4uf_2$。
因为对角算子与 $\Theta$ 对易，令 $\tau^{\rm b}=-2\Theta w$，直接求导得到

$$
\mathcal L_e\tau^{\rm b}=8uf_2.
\tag{19}
$$

构造 $\tau=\tau^{\rm b}+h^mt$。由于 $2m\ge m+1$，
两个临界修正的乘积为零；$h^m$ 乘任何系数时只需保留其模 $h$ 的剩余。
所以 (17) 所需的新响应方程是

$$
\mathcal L_{e0}t=-8\chi\Theta\tau^{\rm b}_0,
\qquad
\mathcal L_{e0}=-4\Theta^2+\frac{8u}{(1-u)^2},
\quad \tau^{\rm b}_0=-\frac{2u}{1-u}.
\tag{20}
$$

其右端是 $16\chi u/(1-u)^2$。用

$$
\mathcal L_{e0}\left(\frac{u}{1-u}\right)
=-\frac{4u}{(1-u)^2}
\tag{21}
$$

可逐项验证唯一零常数解为

$$
\boxed{t=-\frac{4\chi u}{1-u},\qquad
\tau=-2\Theta w+h^mt\pmod{u^{m+1}}.}
\tag{22}
$$

唯一性使用 $1\le j\le m<p$ 时对角元 $-4j^2$ 可逆，
而不是从特殊素数响应外推。

因此令 $E_1^{\rm b}=-(1+2\Theta)f_1$、
$E_2^{\rm b}=-2f_2(1+2\Theta w)$，有

$$
E_1=E_1^{\rm b}+h^mf_{10}t,\qquad
E_2=E_2^{\rm b}+2h^mf_{20}t.
\tag{23}
$$

### Step 6. 奇带临界响应：保留移位的常数项

低奇带方程是 $\mathcal L_oa=-f_1/2$。
对其使用 $1+2\Theta$ 并展开乘积求导，得到

$$
\mathcal L_o\sigma^{\rm b}
=-\frac12E_1^{\rm b}-8uE_2^{\rm b}a,
\qquad \sigma^{\rm b}=-(1+2\Theta)a.
\tag{24}
$$

构造 $\sigma=\sigma^{\rm b}+h^ms$，代入 (18)、(23)—(24) 得

$$
\begin{aligned}
\mathcal L_{o0}s
&=-\frac12f_{10}t-16uf_{20}a_0t
  -4\chi(2\Theta+1)\sigma^{\rm b}_0,\\
\mathcal L_{o0}&=-(2\Theta+1)^2+\frac{8u}{(1-u)^2},
\qquad \sigma^{\rm b}_0=-\frac{1+u}{2(1-u)^2}.
\end{aligned}
\tag{25}
$$

将 (7)、(22) 的 $t$ 代入右端，逐项求导化简得到

$$
-\frac12f_{10}t-16uf_{20}a_0t
-4\chi(2\Theta+1)\sigma^{\rm b}_0
=\frac{2\chi(1+3u)^2}{(1-u)^4}.
\tag{26}
$$

对 $s=-2\chi/(1-u)^2$ 直接应用 $\mathcal L_{o0}$，左端也为 (26)。
因为 $0\le j<m$ 时 $2j+1\le p-2$，全部对角元 $-(2j+1)^2$ 可逆，故

$$
\boxed{s=-\frac{2\chi}{(1-u)^2},\qquad
\sigma=-(1+2\Theta)a+h^ms\pmod{u^m}.}
\tag{27}
$$

这里 $s_0=-2\chi$ 不是可置零的规范：它来自奇移位
$4\chi h^m(2\Theta+1)$ 的常数部分。
例如 (18) 的常数方程给
$\sigma_0=1/[2(-1+4\chi h^m)]=-1/2-2\chi h^m$ 在 $R_*$ 中成立，
与 (27) 一致。

### Step 7. 完整临界端点仍含零剩余

由基带导数身份 (23)—(24) 得

$$
f_2\sigma^{\rm b}+E_2^{\rm b}a
=-(3+2\Theta)(f_2a).
$$

加入 (22)、(27) 的两个临界响应，完整指数积成为

$$
f_2\sigma+E_2a
=-(3+2\Theta)(f_2a)+h^mK(u),
\qquad
K=f_{20}(s+2a_0t)
=-\frac{2\chi(1+2u)}{(1-u)^4}.
\tag{28}
$$

Step 2 的支撑排除和 Step 3 的实际比较允许在 (9) 中准确使用 (23)、(28)，
从而在 $R_*$ 中

$$
\begin{aligned}
4^DpC_D
={}&p[u^m]f_1+16p[u^{m-1}]f_2a\\
&-h^m\left([u^m]f_{10}t+16[u^{m-1}]K\right).
\end{aligned}
\tag{29}
$$

第一行的两项为零，因为低带系数整且 $R_*$ 具有特征 $p$。
第二行的临界标量记为

$$
\begin{aligned}
\mathfrak c_m
&=-[u^m]f_{10}t-16[u^{m-1}]K\\
&=4\chi m+32\chi\left\{\binom{m+2}{3}+2\binom{m+1}{3}\right\}\\
&=4\chi m+16\chi m^2(m+1)
=4\chi m(2m+1)^2.
\end{aligned}
\tag{30}
$$

这些是自由整数 $m$ 的有理系数身份；所用分母只有 $2,3$，对 $p\ge5$ 均为单位。
由于 $2m+1=p$，其特征 $p$ 剩余为

$$
\overline{\mathfrak c_m}=\overline{4\chi mp^2}=0.
\tag{31}
$$

因此 (29) 的全部右端在 $R_*$ 中为零。
Step 2 已证明左端实际整，$4$ 是单位，得到 $pC_D\in h^{m+1}\mathcal O^+$，
从而完成 (1)—(2)。
最后由首一性 $[L^p]U_{\rm cl}=h^{-D}p^2C_D$，得
$v_h([L^p]U_{\rm cl})\ge M-D+m+1=M-2m$，即 (3)。证毕。$\square$

### 实际误差的闭合表

| 来源 | 在乘 $p$ 后、代入真实 $h$ 的最低高度 | 相对本次目标 |
| --- | --- | --- |
| 参照低带 $W_r-G_r$，$r<p$ | $m+1$；至多一个阶乘 $p$ 分母已被正规化消去 | 可舍 |
| 实际 $W_p$ 或中间奇响应与整低指数的乘积 | $M-2m\ge3m$ | 可舍 |
| 参照正阶有理核指数的 $q<p$ 项 | $M$ | 可舍 |
| 同一指数的 $p\le q<2p$ 项 | $q\ge p=2m+1$ | 可舍 |
| 真实 Chebyshev 移位的模 $p$ 系数误差 | $M$ | 可舍 |
| 移位的下一 $H$ 阶、保留核的下一 $H$ 阶 | $m+1$ | 可舍 |
| 两个临界响应的乘积 | $2m\ge m+1$ | 可舍 |
| 非整指数带与奇共振响应的乘积 | 最低 $u$ 次数为 $D$，目标仅为 $D-1$ | 不出现 |

其中参照核之外的实际低带 $H$ 余项 $p$ 整，是由单位三角递推单独保证；
没有假设 $R_{m+1,0}$ 或更高全局有理核具有 $p$ 整性。

### 自由符号核验记录

对自由符号 $u,\chi,m$ 做精确有理化简，核验以下身份；不取素数样本：

1. 偶响应 (20)—(22) 的残差为零。
2. 奇响应 (25)—(27) 的残差为零。
3. 完整端点修正核 (28) 的残差为零。
4. 端点有限系数身份 (30) 的残差为零。

上述核验仅防止符号和因子笔误；实际误差、整性和全部量词由证明及已接受输入承担。

## Corrections or Missing Assumptions

- 预临界的传播子不变式在临界层必须替换为 (16)；
  直接把预临界缩放导数解延用至 $h^m$ 会漏掉 (22)、(27)。
- 不能只算偶响应 $t$。奇响应 $s$ 的常数项与完整 $2a_0t$ 项均参与 (30)。
- 正阶有理核整性此次确实用到 $k=m$；只知道 $k<m$ 不足以推出 (14) 的新精度。
- 式 (31) 中形式标量含 $p^2$，只在本次临界商层说明剩余为零。
  实际未控制的下一阶误差是 $h^{m+1}$，所以不能由该 $p^2$ 写出更强的实际赋值。

## Open Risks

- 下一层 $h^{m+1}$ 的系数尚未计算；最高系数的准确赋值仍未确定。
- 后续若提高精度，必须重新控制有理核 $R_{m+1,0}$、下一 Chebyshev 移位以及
  可能进入目标精度的共振残量；本件不授予这些控制。
  特别地，旧 Claim 2 的量词是 $k+j\le m$，不覆盖 $R_{m+1,0}$ 的 $p$ 整性。
- 不据本件单一最高系数推断其他商系数、完整负 Newton 图、负根简单性、
  不可约性、野分歧结构或分裂域。
- 本件是作者推导；独立审查另行完成。没有改变批次接受状态、出版锁或任何外部资源。
