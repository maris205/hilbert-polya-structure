# Proof Package：最高参数端点的 Ward 整段消失及统一二次边界

日期：2026-09-08。作者：`/root/negative_top_alternative`。
本件从已接受后临界稿接续；仅写本文件，不修改旧稿、入口或接受记录。
使用 proof-writer。作者侧固定 $p=5$ 检查不计非作者独审，也不用于外推一般素数。

## Claim

保持同一实际双谐波分支。固定任意素数 $p\ge5$、$a\ge2$，令

$$
m=(p-1)/2,\qquad M=p^{a-1}m,\qquad D=3m+1=p+m,
\qquad \chi=(-1)^{m+1},\qquad C_D=[L^D]\mathcal B_3.
$$

原指定下一层的答案仍为零：

$$
\boxed{\overline{h^{-(m+2)}pC_D}=0.}
\tag{1}
$$

新 Ward 身份与完整二次边界实际上统一证明更强的整段结论

$$
\boxed{pC_D\in h^{2m+1}\mathcal O^+=h^p\mathcal O^+,\qquad
v_h([L^p]U_{\rm cl})\ge M-m.}
\tag{2}
$$

因为 $p=2m+1\ge m+3$ 对 $m\ge2$ 成立，(2) 蕴含 (1)，包括 $p=5$。
这仍是下界：本件没有计算 $h^p$ 层是否非零，也没有给最高商系数的准确赋值。

## Status

**PROVABLE AS STATED。** 先证明一般 Ward 部分达到 $h^{2m}$，
再完整保留 $h^{2m}$ 的二次传播子项和二次响应，证明该边界也为零。
没有把线性 Ward 截断未经检查延用于 $p=5$。
新结论及其非作者独立审查状态分别记录；本件仍是作者证明稿。

## Assumptions and accepted inputs

- $h=2-\zeta-\zeta^{-1}$，$\zeta$ 为任意本原 $p^a$ 次根；
  $K^+=\mathbb Q_p(h)$、$\mathcal O^+=\mathbb Z_p[h]$，
  $v_h(h)=1$、$v_h(p)=M\ge5m$，$\mathcal O^+/(h)=\mathbb F_p$。
- 实际传播子 $d_n=-(2-\zeta^n-\zeta^{-n})/h$ 与实际递推为

  $$
  d_nV_n(b)=-\frac b2[x^{n-1}]e^{V(b)}-L[x^{n-2}]e^{2V(b)},
  \qquad 1\le n<3p<p^a.
  \tag{3}
  $$

  $x$ 的常数项为零，实际取 $b=1$；没有置零内部模态。
  $p\nmid n$ 时 $d_n$ 为单位，$v_h(d_p)=v_h(d_{2p})=2m$。
- [已接受后临界稿](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_POSTCRITICAL_PROBE_V1_20260908.md)
  及其 [独审](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_TOP_POSTCRITICAL_INDEPENDENT_CHECK_V1_20260908.md)
  提供实际最高权重身份、低带及正规化高带整性、污染支撑、有限多项式参照引理。
  这些输入本轮不重开。
- [共同高项与后临界接受处置](PAPER30_TWIST_THIRD_FORCING_NEGATIVE_HIGH_AND_POSTCRITICAL_DISPOSITION_20260908.md)
  记录此前 $pC_D\in h^{m+2}\mathcal O^+$ 与共同高项界；
  本件只推进最高项，不审查其他商系数。
- 仅新增定向调用早已接受的第一内部 forcing 整性：
  [首内部局部结构作者稿式 (2)](PAPER30_TWIST_PRIME_POWER_LOCAL_STRUCTURE_PROBE_V1_20260907.md)
  与其 [独审第 11—12 项](PAPER30_TWIST_PRIME_POWER_LOCAL_STRUCTURE_INDEPENDENT_CHECK_20260907.md)
  给形式有限整块

  $$
  \mathcal B_1(H,L)=\chi H^m(2-L^m)+H^{m+1}R(H,L)+pT(H,L),
  \quad R,T\in\mathbb Z_{(p)}[[H]][L].
  \tag{4}
  $$

  此处只用该形式整除身份，不用其根结构，也不重审其证明。
- 最后仅用已接受首一分解
  $S=h^{-D}p^2\mathcal B_3=P_{\rm cl}U_{\rm cl}$，
  $P_{\rm cl}$ 首一、次数 $m$，$U_{\rm cl}$ 次数 $p$。

## Notation

令 $u=Lx^2/4$，$V|_{b=0}=W(u)$、$\partial_bV|_{b=0}=xA(u)$。
使用 $\Theta=u\partial_u$、$\mathcal Q=2\Theta+1$。
形式变量 $H$ 与真实 $h$ 分开；另记 $\mathcal E=H\partial_H$。
低级数 $w=W_{<p}(H,u)$、$a=A_{<m}(H,u)$ 在各自有限 $u$ 范围内使用，
并令 $f_1=e^w$、$f_2=e^{2w}$。

工作环为

$$
\mathscr R_H=\mathbb F_p[H]/(H^p)
\cong\mathcal O^+/(h^p),\qquad H\longmapsto h.
\tag{5}
$$

因 $M\ge p$，这个有限比较与实际圆分整环的规范一致。
$\mathcal E$ 是形式 Euler 导数；本件不对单个已经取值的 $p$-进数作未经定义的求导。
所有出现的指数仅提取低于 $p$ 的低系数；高指数先乘 $p$ 并证明整性后比较。

零阶函数及两个有限求和级数记为

$$
w_0=-\log(1-u),\quad a_0=\frac1{2(1-u)},\quad
f=\frac1{1-u},\quad g=f^2,\quad G=\frac{1+u}{1-u},
\tag{6}
$$

$$
\ell(u)=\log(1-u)=-\sum_{k\ge1}\frac{u^k}{k},\quad
\mathscr D(u)=\sum_{k\ge1}\frac{u^k}{k^2},\quad
\mathscr H(u)=\sum_{r\ge0}\frac{u^r}{2r+1}.
\tag{7}
$$

它们先在特征零定义，约化只用 $\ell,\mathscr D$ 的次数 $\le m<p$，
以及 $\mathscr H$ 的次数 $<m$；所有实际使用的分母为 $p$ 单位。
逐项有

$$
\Theta\ell=-\frac{u}{1-u},\qquad
\Theta\mathscr D=-\ell,\qquad \mathcal Q\mathscr H=f.
\tag{8}
$$

## Proof Strategy

把真实传播子平移精确写成一个 Chebyshev 一阶响应和一个二次常数项。
前者产生由 $\mathcal E$ 与 $\Theta$ 组成的精确 Ward 响应，
其完整端点归结为已接受的第一内部 forcing，因此一次消去整个预二次段。
二次边界只依赖零阶低解；用 (7) 的有限系数级数显式求解两条三角方程，
再计算完整端点。最后以实际高度统一核对 $p=5$ 与其他素数。

## Dependency Map

1. 实际最高权重与有限参照确定两条正规化高带及唯一端点。
2. 准确 Chebyshev 加法、导数身份给完整移位至 $H^{2m}$。
3. Ward 响应与第一内部 forcing 的形式整性消去线性段。
4. 二次响应的显式级数及有限调和和消去 $H^{2m}$ 边界。
5. 实际误差界把有限身份提升到 (2)，首一性换算最高商系数。

## Proof

### Step 1. 实际有限方程与本次合法精度

已接受的权重提取得到

$$
d_{2r}W_r=-4[u^{r-1}]e^{2W},\qquad
d_{2r+1}A_r=-\frac12[u^r]e^W-8[u^{r-1}]e^{2W}A,
\tag{9}
$$

$$
4^DC_D=-[u^{p+m}]e^W-16[u^{p+m-1}]e^{2W}A.
\tag{10}
$$

所需 $W$ 至 $p+m$，$A$ 至 $p+m-1$，没有使用 $V_{3p}$。
定义正规化高带 $\tau_j=pW_{p+j}$、$\sigma_j=pA_{p+j}$，
分别在 $0\le j\le m$、$0\le j<m$ 使用；它们已由实际递推证明整。
此外 $\tau_0=0$ 在 (5) 的环中成立，因为
$v_h(pW_p)\ge M-2m\ge3m\ge p$。

有限参照引理的准确低带匹配及 $h^p$ 误差允许在 $\mathscr R_H$ 中写

$$
E_1=f_1(\tau-1),\qquad E_2=2f_2(\tau-1),
\tag{11}
$$

$$
4^DpC_D=-[u^m]E_1-16[u^{m-1}](f_2\sigma+E_2a).
\tag{12}
$$

在 (12) 中，响应下标 $\ge m$ 而 $<p$ 时，只能乘指数下标 $<p$ 的整项；
乘 $p$ 后高度至少 $M-2m\ge3m\ge p$。
非整指数与该中间响应的最短乘积次数为 $p+m$，严格超出目标 $p+m-1$。
两个高带相乘的最低次数为 $2p$，也不出现。
因此 (11)—(12) 没有隐藏非整乘积。

在各自低范围定义

$$
\mathcal D_eu^j=d_{2j}(H)u^j,\quad
\mathcal D_ou^j=d_{2j+1}(H)u^j,\quad
\mathcal L_e=\mathcal D_e+8uf_2,\quad
\mathcal L_o=\mathcal D_o+8uf_2.
\tag{13}
$$

令 $\Delta_eu^j=(d_{2p+2j}-d_{2j})u^j$、
$\Delta_ou^j=(d_{2p+2j+1}-d_{2j+1})u^j$。
从 (9)、(11) 得实际正规化高带方程

$$
(\mathcal L_e+\Delta_e)\tau=8uf_2\pmod{u^{m+1}},\qquad
(\mathcal L_o+\Delta_o)\sigma
=-\left(\frac{f_1}{2}+16uf_2a\right)(\tau-1)\pmod{u^m}.
$$

低方程为 $\mathcal D_ew=-4uf_2$、$\mathcal L_oa=-f_1/2$。
所有低系数的 $H$-Taylor 展开均 $p$ 整：对 $W_r$、$r<p$，
除数常数为 $-4r^2$；对 $A_r$、$r<m$，除数常数为 $-(2r+1)^2$；
指数的低次数阶乘也是单位。
所以低带 $[H^2]w,[H^2]a$ 及其后续所需系数均可合法使用。
后面的精确 Ward 身份包含这些系数的全部贡献，不以省略二阶低带代替计算。

### Step 2. 准确移位，不能省掉二次常数项

令 $C_n(H)=z^n+z^{-n}$、$H=2-z-z^{-1}$，并定义整数 Chebyshev 多项式

$$
S_n(H)=\frac{z^n-z^{-n}}{z-z^{-1}},\qquad C_n=2+Hd_n.
$$

在特征 $p$ 中，准确有

$$
C_{2p}=2-4H^p+H^{2p},\qquad
z^{2p}-z^{-2p}=(z-z^{-1})^p(2-H^p).
$$

把这些式子代入加法身份

$$
C_{2p+n}-C_n
=\frac{(C_{2p}-2)C_n+(z^{2p}-z^{-2p})(z^n-z^{-n})}{2},
$$

并使用 $(z-z^{-1})^2=-H(4-H)$，得到准确形式身份

$$
\begin{aligned}
\Delta(n):=d_{2p+n}-d_n
={}&\chi H^m(4-H)^{m+1}\left(1-\frac{H^p}{2}\right)S_n\\
&+\left(-2H^{p-1}+\frac{H^{2p-1}}2\right)(2+Hd_n).
\end{aligned}
\tag{14}
$$

令 $\lambda(H)=\chi H^m(4-H)^{m+1}$。因 $p=2m+1$，在 (5) 的环中

$$
\boxed{\Delta(n)=\lambda S_n-4H^{2m}.}
\tag{15}
$$

在低带上相应定义 $S_eu^j=S_{2j}u^j$、$S_ou^j=S_{2j+1}u^j$。
此处的 $-4H^{2m}$ 是完整二次常数项，包含 $p=5$ 的 $H^4$ 项。
对本件所需 $1\le n<p$，还可对整数多项式求导得到

$$
C_n'(H)=-nS_n(H),\qquad
d_n+Hd_n'=-nS_n.
\tag{16}
$$

第一式可由 $dH/dz=-(z-z^{-1})/z$ 与 $dC_n/dz=n(z^n-z^{-n})/z$ 相除证明；
两边原本为多项式，故为整数多项式身份。
在所用下标上 $n$ 是 $p$ 单位，因而 (16) 可用于反演频率算子。
以上模 $p$ 身份代入真实 $h$ 后，整数系数误差高度至少 $M\ge p$，
所以 (15) 确实控制实际所需精度。

### Step 3. Ward 响应与整个线性段的消失

已接受的基导数解为

$$
\tau^{\rm b}=-2\Theta w,\qquad \sigma^{\rm b}=-\mathcal Q a.
$$

引入新的精确低带组合

$$
Z=(\mathcal E-\Theta)w,\qquad
T=(\mathcal E-\Theta-1)a.
\tag{17}
$$

由低方程分别取 $\mathcal E$ 和 $\Theta$，并展开乘积法则，得到

$$
\mathcal L_eZ=-(\mathcal D_e+\mathcal E\mathcal D_e)w,
\tag{18}
$$

$$
\mathcal L_oT
=-\left(\frac{f_1}{2}+16uf_2a\right)Z
-(\mathcal D_o+\mathcal E\mathcal D_o)a.
\tag{19}
$$

$\mathcal E\mathcal D_e$ 在这里仅指对角符号 $Hd_{2j}'$，奇式同理。
例如 (18) 来自
$\mathcal L_e(\mathcal Ew)=-(\mathcal E\mathcal D_e)w$ 与
$\mathcal L_e(\Theta w)=-4uf_2$。
为核对 (19)，低奇式分别给

$$
\begin{aligned}
\mathcal L_o(\mathcal Ea)
&=-\left(\frac{f_1}{2}+16uf_2a\right)\mathcal Ew
  -(\mathcal E\mathcal D_o)a,\\
\mathcal L_o(\Theta a)
&=-\frac{f_1}{2}\Theta w-8uf_2a(1+2\Theta w),\\
\mathcal L_oa&=-f_1/2.
\end{aligned}
$$

将后两式从第一式减去，即得 (19)。
由 (16)，线性移位作用于基导数解分别为

$$
(\lambda S_e)\tau^{\rm b}
=\lambda(\mathcal D_e+\mathcal E\mathcal D_e)w,
\qquad
(\lambda S_o)\sigma^{\rm b}
=\lambda(\mathcal D_o+\mathcal E\mathcal D_o)a.
$$

因此模 $H^{2m}$，高带的实际解为

$$
\tau=\tau^{\rm b}+\lambda Z,
\qquad \sigma=\sigma^{\rm b}+\lambda T.
\tag{20}
$$

证明 (20) 时，移位再作用于其修正的项至少为 $H^{2m}$；
各正偶下标和全部所需奇下标的三角对角元均为单位，故构造解即唯一实际解。
偶常数项由 $\tau_0=0$ 单独固定，不取 $d_0^{-1}$。

两条端点乘积的 Ward 身份为

$$
f_1Z=(\mathcal E-\Theta)f_1,\qquad
f_2(T+2aZ)=(\mathcal E-\Theta-1)(f_2a).
\tag{21}
$$

记

$$
B_{\rm low}(H)=[u^m]f_1+16[u^{m-1}]f_2a.
\tag{22}
$$

基带端点的两个系数都是 $2m+1=p$，故为零。
式 (21) 表明全部线性移位端点准确压缩为

$$
-\lambda(\mathcal E-m)B_{\rm low}.
\tag{23}
$$

同一权重提取在第一内部 forcing 处给
$B_{\rm low}=-4^m[L^m]\mathcal B_1(H,L)$。
这些系数只用原下标 $<p$ 的实际低块，与 (4) 是同一个对象。
由已接受形式身份 (4)，模 $p$ 有 $B_{\rm low}\in H^m\mathbb F_p[[H]]$，
从而

$$
(\mathcal E-m)B_{\rm low}\in H^{m+1}\mathbb F_p[[H]].
\tag{24}
$$

这是对形式整系数的 Euler 求导；不能仅从一个取值的赋值界直接推导 (24)。
于是 (23) 在 $H^{2m+1}=H^p$ 处才可能非零。
在考虑二次移位之前，已经得到一般的 $pC_D\in h^{2m}\mathcal O^+$。
但这一步本身尚不决定 $H^{2m}$，下面单独保留该边界。

### Step 4. 二次边界的两条统一方程

在 $\mathscr R_H$ 中补写

$$
\tau=\tau^{\rm b}+\lambda Z+H^{2m}X,
\qquad
\sigma=\sigma^{\rm b}+\lambda T+H^{2m}Y.
\tag{25}
$$

这里只需要零阶低解。因为 $4^m=2^{p-1}=1$ 于 $\mathbb F_p$，
$\lambda/H^m$ 的常数为 $4\chi$，其平方为 $16$。
再用 $S_n(0)=n$、(15) 的二次项 $-4H^{2m}$，从实际两条高带方程得到

$$
\mathcal L_{e0}X=4\tau^{\rm b}_0-16(2\Theta)Z_0,
\tag{26}
$$

$$
\mathcal L_{o0}Y
=-\left(\frac f2+16uga_0\right)X
 +4\sigma^{\rm b}_0-16\mathcal Q T_0,
\tag{27}
$$

其中

$$
\begin{gathered}
\mathcal L_{e0}=-4\Theta^2+8ug,\quad
\mathcal L_{o0}=-\mathcal Q^2+8ug,\\
Z_0=-\Theta w_0=-\frac u{1-u},\quad
T_0=-(\Theta+1)a_0=-\frac1{2(1-u)^2},\\
\tau^{\rm b}_0=-\frac{2u}{1-u},\quad
\sigma^{\rm b}_0=-\frac{1+u}{2(1-u)^2}.
\end{gathered}
\tag{28}
$$

式 (26)—(27) 保留了两个不同来源：二次移位常数 $-4I$ 和线性移位再次作用于
线性响应的平方贡献 $16$。
任何再高的反馈至少为 $H^{3m}$，而 $3m\ge2m+1=p$，故在本次环中为零。
尤其 $p=5,m=2$ 时这里完整保留 $H^4$，没有沿用上一轮的线性截断。

两条方程的解为

$$
\boxed{X=4\ell-2G\mathscr D,}
\tag{29}
$$

$$
\boxed{Y=-\frac{1+u}{(1-u)^2}\mathscr D
-\frac{2\ell}{1-u}-\frac2{1-u}-4G\mathscr H.}
\tag{30}
$$

逐项使用 (8) 即可验证：式 (26) 的右端为
$8u(3+u)/(1-u)^2$，与 $\mathcal L_{e0}$ 作用于 (29) 相同。
式 (27) 的右端可写为

$$
-\left(\frac f2+8uf^3\right)X
+\frac{2(u^2+12u+3)}{(1-u)^3},
$$

使用 (8) 对 (30) 求导得到同一式子。
在 $1\le j\le m$，偶对角元 $-4j^2$ 为单位，且 $X(0)=0$；
在 $0\le j<m$，奇对角元 $-(2j+1)^2$ 为单位。
故这些有限解由三角唯一性成立。
尤其 $Y(0)=-6$ 必须保留；它包含二次移位与逆元平方项的共同贡献。

### Step 5. 二次完整端点的有限求和

由 (12)、(21)、(25)，线性端点已在 (24) 排除。
二次端点仅为

$$
\mathfrak c_2=-[u^m]J_2-16[u^{m-1}]K_2,
\quad J_2=fX,\quad K_2=g(Y+2a_0X).
\tag{31}
$$

代入 (29)—(30)，准确化简为

$$
\begin{aligned}
J_2&=4f\ell-\frac{2(1+u)}{(1-u)^2}\mathscr D,\\
K_2&=-\frac{3(1+u)}{(1-u)^4}\mathscr D
+\frac{2\ell}{(1-u)^3}-\frac2{(1-u)^3}
-\frac{4(1+u)}{(1-u)^3}\mathscr H.
\end{aligned}
\tag{32}
$$

定义三个 $p$-整有限和

$$
H_1=\sum_{k=1}^m\frac1k,\qquad
H_2=\sum_{k=1}^m\frac1{k^2},\qquad
H_o=\sum_{r=0}^{m-1}\frac1{2r+1}.
\tag{33}
$$

这里 $H_2$ 只表示有限倒数平方和，不是另一传播子变量。
由 $[u^n](1+u)/(1-u)^2=2n+1$，首先得到

$$
[u^m]J_2=-4H_1-2\{(2m+1)H_2-2H_1\}
=-2(2m+1)H_2.
\tag{34}
$$

对第二个核，置

$$
\begin{aligned}
\mathfrak A_m&=\sum_{k=1}^{m}
\frac{(m-k)(m+1-k)(2m+1-2k)}{k^2},\\
\mathfrak B_m&=\sum_{k=1}^{m}\frac{(m-k)(m+1-k)}k,\\
\mathfrak C_m&=\sum_{r=0}^{m-1}\frac{(m-r)^2}{2r+1}.
\end{aligned}
$$

这些仅是本节的有限标量，不是实际模态 $A_r$。
式 (32) 的卷积给

$$
[u^{m-1}]K_2=-\frac12\mathfrak A_m-\mathfrak B_m-m(m+1)-4\mathfrak C_m.
\tag{35}
$$

分子展开及自由符号除法给出

$$
\begin{aligned}
\mathfrak A_m&=m(m+1)(2m+1)H_2-(6m^2+6m+1)H_1+m(5m+2),\\
\mathfrak B_m&=m(m+1)H_1-\frac{m(3m+1)}2,\\
\mathfrak C_m&=-\frac{m(3m+2)}4+\frac{(2m+1)^2}{4}H_o.
\end{aligned}
\tag{36}
$$

例如最后一式来自逐项身份
$(m-r)^2/(2r+1)=-m+r/2-1/4+(2m+1)^2/[4(2r+1)]$；
前两式展开 $k$ 的三次及二次分子后，分别使用
$\sum_{k=1}^m k=m(m+1)/2$ 得到。
代回 (35) 可得

$$
[u^{m-1}]K_2
=-\frac{2m+1}{2}
\{- (2m+1)H_1+m(m+1)H_2+2(2m+1)H_o-m\}.
\tag{37}
$$

因为 $2m+1=p$，(34) 与 (37) 各自的剩余都为零。
若将完整端点合并，其准确特征零有限和身份为

$$
\boxed{\mathfrak c_2
=2p\{p^2H_2-4pH_1+8pH_o-4m\},\qquad
\overline{\mathfrak c_2}=0.}
\tag{38}
$$

所有用到的 $k,2r+1$ 都小于 $p$，额外分母仅为 $2,4,6$ 的单位因子，
因此这一约化统一覆盖 $p=5$，没有含 $1/p$ 的边界系数。

### Step 6. 回到实际最高系数及精度边界

由 (12)、(23)—(25)、(31)，在 $\mathscr R_H$ 中完整有

$$
4^DpC_D=-\lambda(\mathcal E-m)B_{\rm low}
+H^{2m}\overline{\mathfrak c_2}=0.
\tag{39}
$$

第一项由 (24) 在 $H^p$ 中，第二项由 (38) 为零。
有限参照和实际比较已经证明左端整；$4$ 为单位，故
$pC_D\in h^p\mathcal O^+$。
由首一性 $[L^p]U_{\rm cl}=h^{-D}p^2C_D$，得到
$v_h([L^p]U_{\rm cl})\ge M-D+p=M-m$。
这证明 (2)，并由 $p\ge m+3$ 得 (1)。证毕。$\square$

### 本次实际误差审计

| 误差来源 | 高度或支撑界 | 是否覆盖模 $h^p$ |
| --- | --- | --- |
| 已接受有限参照正规化指数误差 | $h^p$ | 是；不外推到下一层 |
| 真实 $pW_p$、中间奇响应乘整低指数 | $M-2m\ge3m\ge p$ | 是 |
| 中间响应与非整指数相遇 | 最低 $u$ 次数 $D$，目标 $D-1$ | 不出现 |
| 两个高带相乘 | 最低 $u$ 次数 $2p>D$ | 不出现 |
| 模 $p$ Chebyshev 身份代入真实 $h$ 的误差 | $M\ge p$ | 是 |
| (14) 中舍去的二次非恒定项及更高项 | 至少 $H^{2m+1}=H^p$ | 是 |
| 线性移位与二次响应继续耦合 | 至少 $H^{3m}$ | 是，包括 $m=2$ |

低带的 $H^2$ 及更高系数没有单独设零；其合法整性在 Step 1 确认，
其所有贡献由 (18)—(24) 的完整形式恒等式统一包含。
实际有限域比较没有把 $\mathcal B_1$ 的单点赋值界不合法地直接求导。

### 固定 $p=5$ 的直接边界核验

这部分是结构证明之外的有界作者检查，不是素数扫描，也不承担一般量词。
在 $\mathbb F_5[H]/(H^5)$ 中，由整数 Chebyshev 递推保留 $C_n$ 至 $H^5$、
再除以 $H$，有

| $n$ | $d_n$ | $d_{10+n}$ |
| --- | --- | --- |
| $1$ | $4$ | $4+H^2+3H^3+4H^4$ |
| $2$ | $1+H$ | $1+H+2H^2+4H^4$ |
| $3$ | $1+H+4H^2$ | $1+H+2H^2+4H^4$ |
| $4$ | $4+2H^2+H^3$ | $4+H^2+3H^3+4H^4$ |

完整单位三角计算给以下向量，按 $1,H,H^2,H^3,H^4$ 排列：

| 量 | 系数向量 |
| --- | --- |
| $W_1$ | $(1,4,1,4,1)$ |
| $W_2$ | $(3,2,4,4,3)$ |
| $A_0$ | $(3,0,0,0,0)$ |
| $A_1$ | $(3,0,0,3,4)$ |
| $\tau_1$ | $(3,2,2,4,0)$ |
| $\tau_2$ | $(3,2,3,4,0)$ |
| $\sigma_0$ | $(2,0,2,1,0)$ |
| $\sigma_1$ | $(1,0,4,3,3)$ |

这八行可由下列八条方程逐项手验：

$$
\begin{gathered}
d_2W_1=1,\quad d_4W_2=2W_1,\quad
d_1A_0=2,\quad d_3A_1=2W_1+1,\\
d_{12}\tau_1=3,\quad d_{14}\tau_2=2\tau_1+W_1,\quad
d_{11}\sigma_0=3,\quad
d_{13}\sigma_1=2\tau_1+3W_1+2\sigma_0+3.
\end{gathered}
$$

相应完整端点为

$$
[u^2]f_1(\tau-1)=3H^2+3H^3+H^4,
$$

$$
[u](f_2\sigma+2f_2(\tau-1)a)=2H^2+2H^3+4H^4.
$$

故负的第一项减去 $16$ 倍第二项为零，确认 $pC_7\in h^5\mathcal O^+$。
这里的逆元完整保留平方项；例如
$\sigma_0=3/(4+H^2+3H^3+4H^4)=2+2H^2+H^3$，
其 $H^4$ 的消失包含二次临界贡献。
因为任意 $a\ge2$ 都满足 $M\ge10$、污染高度 $M-4\ge6$，
此表证明的是全部五的幂边界，不是只取 $a=2$ 的数值样本。

### 定向验证记录

实际执行的自由符号核验包括：Chebyshev 加法式、两条 Ward 乘积身份、
二次偶响应、二次奇响应、二次端点核和有限和闭式，残差均为零。
固定 $p=5$ 的八条三角方程与完整端点残差均为零；
主作者另从整数 Chebyshev 递推重建了同一短表。
这些作者侧代数核验不替代整稿的非作者独立审查。

## Corrections or Missing Assumptions

- 仅保留 $\lambda S_n$ 的 Ward 响应最多控制模 $H^{2m}$；
  新的 (26)—(38) 才处理二次边界，不能把二者混写。
- 第一内部 forcing 的新调用是已接受的形式整系数身份 (4)，
  不是从实际取值的赋值界自行推出导数界。
- $[H^2]w,[H^2]a$ 不必逐项展开，但必须具有 Step 1 的有限整性；
  Ward 身份不能用于未经整性控制的全局奇响应。
- $\mathscr D$、$\mathscr H$ 仅在所列有限次数内约化，未使用含 $1/p$ 的后续系数。

## Open Risks

- 下一目标是 $\overline{h^{-p}pC_D}$；本件未证明它非零或为零。
- 有限参照误差恰从 $h^p$ 起，下一精度不能继续将该误差置零。
  还须控制 (14) 中新的非恒定二次项及相应响应；本件不预设这些项相消。
- 形式端点 (38) 中的额外 $p$ 因子不提供超出 $h^p$ 的实际精度，
  因为未计算的实际误差已在该层进入。
- 其他商系数、完整负 Newton 图、准确斜率、不可约性、简单性与野分裂域均未由本件确定。
- 本件仅为新的作者证明；没有改变任何既有接受记录、出版锁或外部资源。
