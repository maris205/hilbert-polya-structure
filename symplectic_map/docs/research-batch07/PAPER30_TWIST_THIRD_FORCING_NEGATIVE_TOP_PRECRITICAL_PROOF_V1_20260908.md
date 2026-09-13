# Paper30：负端最高参数系数的整个预临界层消失

日期：2026-09-08。作者：`/root`。使用 formula-derivation 固定目标，
使用 proof-writer 给出有限系数证明。作者稿，独立核查另记；不改写旧稿。

## Claim

保持同一实际双谐波递推、固定参数和规范。对所有素数 $p\ge5$、$a\ge2$，令
$$
m=(p-1)/2,\quad M=p^{a-1}m,\quad D=3m+1=p+m,\quad e_*=M-D.
$$
则最高参数系数满足整个预临界消失
$$
\boxed{p[L^D]\mathcal B_3\in h^m\mathcal O^+.}                 \tag{1}
$$
因而在已接受的分解 $S=h^{-D}p^2\mathcal B_3=P_{\rm cl}U_{\rm cl}$ 中，
$$
\boxed{v_h([L^p]U_{\rm cl})\ge e_*+m.}                       \tag{2}
$$
这不是准确赋值声明：临界 $h^m$ 系数可能消失，本文不计算该系数。

记
$$
\delta=\min\left\{\frac{e_*}{p-1},\frac{e_*+m}{p}\right\}
>\frac{e_*}{p}.
$$
则所有负根仍按重数计，并满足
$$
v_h(\beta)\le-\delta.                                      \tag{3}
$$
对任何有限扩域中的非零参数 $\ell$，若 $-\delta<v_h(\ell)\le0$，则
$$
v_h(S(\ell))=m v_h(\ell).                                  \tag{4}
$$
特别是此前排除的端点 $v_h(\ell)=-e_*/p$ 现在包含在式 (4) 中；
新的端点 $-\delta$ 不包含。无准确负斜率、因子型、简单性或野分裂域结论。

## Status

`PROVABLE AS STATED`：以下作者证明完整；是否接受由新独立核查决定。
目标未缩为仅模 $h$。原模 $h$ 稿中的奇共振后约化不在本文使用。

## Assumptions and accepted inputs

$h=2-\zeta-\zeta^{-1}$，$\zeta$ 本原 $p^a$ 次，
$K^+=\mathbb Q_p(h)$，$\mathcal O^+=\mathbb Z_p[h]$，
$v_h(h)=1$、$v_h(p)=M\ge5m$。
实际分支为
$$
d_nV_n=-\frac b2[x^{n-1}]e^V-L[x^{n-2}]e^{2V},\qquad
d_n=-\frac{2-\zeta^n-\zeta^{-n}}h,
$$
其中 $b$ 仅是权重为一的辅助幅度，实际取 $b=1$。
$$
\mathcal B_3=-[x^{3p-1}]e^V-2L[x^{3p-2}]e^{2V}.
$$
只使用 $n<3p<p^a$ 的非零实际传播子。$p\nmid n$ 时 $d_n$ 为单位，
$v_h(d_p)=v_h(d_{2p})=2m$。

既有输入按问题调用，不重审未变证明：

- [统一正簇处置](PAPER30_TWIST_THIRD_FORCING_UNIFORM_POSITIVE_CLUSTER_DISPOSITION_20260907.md)：
  $P_{\rm cl}$ 首一次数 $m$，$\deg U_{\rm cl}=p$，全部正根赋值为 $(m-1)/m$。
- [根簇分离证明](PAPER30_TWIST_THIRD_FORCING_ROOT_CLUSTER_SEPARATION_PROBE_V1_20260907.md)：
  $U_{\rm cl}=u_0+\sum_{j=1}^p u_jL^j$，$u_0$ 为单位，$u_j\in h^{e_*}\mathcal O^+$；
  不将 $u_0\equiv a_m\pmod{h^{e_*}}$ 误写为准确相等。
- [高阶低块结构证明](PAPER30_TWIST_THIRD_FORCING_HIGHER_RESPONSE_STRUCTURE_PROBE_V1_20260907.md)
  Claim 1–2 及其已接受的
  [独立核查](PAPER30_TWIST_THIRD_FORCING_UNIFORM_POSITIVE_CLUSTER_INDEPENDENT_CHECK_20260907.md)：
  特征零解 $P(H,0,4z)=-2\log(1-z)+\sum_{k\ge1}H^kR_{k,0}(z)$，
  $1\le k\le m$ 时 $R_{k,0}\in\mathbb Z_{(p)}[z,(1-z)^{-1}]$。
  本文只调用 $k<m$，不移用二次谐波参数的结论。

## Notation and invariant object

唯一目标是实际 $[L^D]\mathcal B_3$，不是商同余的任意模型。
在 $b=0$ 取 $u=Lx^2/4$，写
$$
V|_{b=0}=W(u),\qquad (\partial_bV)|_{b=0}=xA(u),\qquad
\Theta=u\partial_u.
$$
所有级数只提取所需有限的 $u$ 系数，不主张 $p$-进指数函数的解析收敛。
约化环取 $R=\mathcal O^+/h^m\mathcal O^+$；因 $M\ge5m$，它具有特征 $p$。
在 $R$ 中使用指数符号时，低次数 $<p$ 按单位阶乘定义；高次数只在先乘 $p$
并证明整性后约化。

## Strategy and dependency map

1. 权重将实际最高系数准确化为纯偶解 $W$ 和一次奇响应 $A$。
2. 纯偶解经 $H_2=H(4-H)$ 准确变换到既有单谐波形式解；它提供一个
   带单个对数项的特征零参照级数。正阶有理核确保所需有限整性。
3. 在 $R$ 中，传播子平移 $2p$ 不变；共振污染的最短乘积次数超过目标。
4. 两个归一化高带分别为 $-2\Theta W$ 和 $-(1+2\Theta)A$。
   端点提取的系数是 $2m+1=p$，消去全部 $h^0,\ldots,h^{m-1}$ 层。
5. 返回实际首一商，用唯一最低赋值项证明根界和点值式。

## Proof

### Step 1. 实际最高权重的有限恒等式

给 $x^n$ 对应的系数赋总参数权重 $n$，$b$ 权重一、$L$ 权重二。
递推的三角归纳给出 $V_n$ 的该齐次性。最高 $L^D$ 项在第一指数项只能取
$b^0$，在第二指数项只能取 $b^1$，因此
$$
[L^D]\mathcal B_3=-4^{-D}\left(
[u^{p+m}]e^W+16[u^{p+m-1}]e^{2W}A\right).                    \tag{5}
$$
因第二指数为 $e^{2V}$，它的一次响应是 $2xe^{2W}A$；连同原 $-2L$
和变量缩放给出式 (5) 的 $16$。
直接对实际递推取纯偶及一次奇项，得到
$$
d_{2r}W_r=-4[u^{r-1}]e^{2W},                                \tag{6}
$$
$$
d_{2r+1}A_r=-\frac12[u^r]e^W-8[u^{r-1}]e^{2W}A.             \tag{7}
$$
在所需范围，$W$ 取至 $p+m$，$A$ 取至 $p+m-1$；没有使用 $V_{3p}$。

### Step 2. 低带整性与共振污染的明确界

对 $r<p$，式 (6) 中的指数次数 $r-1<p$，且 $d_{2r}$ 为单位，故归纳得到
$W_r\in\mathcal O^+$。于是 $[u^k]e^{cW}$ 对 $k<p$、$c=1,2$ 均整。
式 (7) 依次给出
$$
A_r\in\mathcal O^+\quad(0\le r<m),\qquad
v_h(A_r)\ge-2m\quad(m\le r<p).                              \tag{8}
$$
证明后一式：$r=m$ 唯一使用高度 $2m$ 的除数 $d_p$，其右端整；
$m<r<p$ 的除数均为单位，右端只乘整指数系数，故保持此界。
同理式 (6) 的 $r=p$ 给出
$$
v_h(W_p)\ge-2m.                                            \tag{9}
$$
因此 $pW_p$ 及 $pA_r$（$m\le r<p$）属于 $h^{M-2m}\mathcal O^+$，
在 $R$ 中均为零，因为 $M-2m\ge3m$。
本文从未声称这些未正规化的奇共振后系数可在 $R$ 中约化。

### Step 3. 传播子移位的全部预临界精度

真实 Chebyshev 展开为
$$
d_n(H)=\sum_{k\ge0}H^kD_k(n),\qquad
D_k(X)=\frac{(-1)^{k+1}X^2\prod_{s=1}^k(X^2-s^2)}{(k+1)(2k+1)!}.
                                                                    \tag{10}
$$
当 $k<m$，分母与 $p$ 互素，故 $D_k(n+2p)\equiv D_k(n)\pmod p$。
对固定整数 $n$，真实 $d_n(H)$ 是整系数多项式；$H^m$ 以上项代入 $h$
后可模 $h^m$ 舍去，低项的 $p$ 倍误差也可舍去。因此
$$
d_{2p+2j}(h)=d_{2j}(h),\quad
d_{2p+2j+1}(h)=d_{2j+1}(h)\quad\text{在 }R\text{ 中}.         \tag{11}
$$
只在相应非共振正下标使用逆；$d_0=0$ 不取逆。

### Step 4. 纯偶特征零参照级数及单个阶乘带

令 $H_2=H(4-H)$。Chebyshev 倍角给出准确身份
$d_{2r}(H)=(4-H)d_r(H_2)$。因而式 (6) 的特征零形式解准确为
$$
G(H,u)=\frac12P\left(H_2,0,\frac{16u}{4-H}\right).           \tag{12}
$$
确实，$2G$ 的右端是 $-8u e^{2G}/(4-H)$，与单谐波方程 $-xe^P/2$
在 $x=16u/(4-H)$ 下相同；零常数三角唯一性证明式 (12)。
记 $c(H)=4/(4-H)$。所调用有理性与整性给出，在 $H$ 次数低于 $m$ 的范围，
$$
G(H,u)=-\log(1-c(H)u)+Q(H,u),                               \tag{13}
$$
其中 $Q\in H\mathbb Z_{(p)}[u,(1-u)^{-1}][H]/(H^m)$，且 $Q(H,0)=0$。
这是对有理核作 $H_2$ 和 $c(H)u$ 的有限 Taylor 替换；分母 $4$ 为单位。
选这些低 $H$ 系数的多项式提升，并在 $H=h$ 后仍记为 $Q$，取
$c=(1-h/4)^{-1}$。得到有限计算用的参照级数
$G=-\log(1-cu)+Q$。
对 $r<p$，实际 $W_r$ 的 $H$-Taylor 系数都 $p$-整，所以
$$
W_r-[u^r]G\in h^m\mathcal O^+\quad(r<p).                    \tag{14}
$$

下面只对 $N<2p$ 提取系数。由式 (13)，
$$
p[u^{p+j}]G\equiv c^p\,\mathbf1_{j=0}\equiv\mathbf1_{j=0}
\pmod{h^m},\quad 0\le j\le m.                              \tag{15}
$$
最后的同余使用 $c^p=(1-h/4)^{-p}\equiv1\pmod{h^m}$：
二项式的中间项含 $p$，端点 $h^p$ 的高度也大于 $m$。

还需检查指数，而不能把形式 $H$ 截断擅自当作 $p$-进指数收敛。
对 $c_0=1,2$，精确形式恒等式
$$
e^{c_0G}=(1-cu)^{-c_0}e^{c_0Q}
$$
用于每个 $N<2p$。$Q$ 零常数且每个系数属于 $h\mathcal O^+$，故其指数
只需 $q\le N<2p$ 个因子的项。$q<p$ 时 $q!$ 是单位，乘 $p$ 后高度至少 $M$；
$p\le q<2p$ 时 $v_p(q!)=1$，乘 $p$ 后高度至少 $q\ge p>m$。
因此
$$
p[u^N]e^{c_0G}\in h^m\mathcal O^+\quad(N<2p).              \tag{16}
$$

令 $T_j=pW_{p+j}$。从 $j=0$ 的式 (9) 起，式 (6) 可归纳证明 $T_j$ 整，
$0\le j\le m$：在指数次数 $p+j-1<2p$ 中，低带阶乘至多含一个 $p$，
且至多出现一个指标 $\ge p$ 的高带因子；先乘 $p$ 就全部整。
与式 (14)–(16) 比较并利用高带乘积的最低次数 $2p$，得到
$$
p[u^{p+j}]e^{c_0W}
=[u^j]c_0e^{c_0w}(\tau-1)\quad\text{在 }R\text{ 中},        \tag{17}
$$
其中 $\tau=\sum_{j=0}^m\overline{T_j}u^j$，$w$ 是实际整低带 $W_{<p}$ 的约化。
右端指数仅用次数 $j\le m<p$，因而有定义。
详细误差控制是：低带差的每个系数含 $h^m$；低带指数次数 $<2p$ 的阶乘
至多一个 $p$，先乘 $p$ 后该差仍含 $h^m$。若差与高带相乘，后者只有一个
且其 $p$ 倍整，同样保持 $h^m$。这也证明式 (17) 的约化没有隐藏负赋值误差。

### Step 5. 偶带是缩放导数

在低次数 $\le m$，记 $\mathcal D_eu^j=d_{2j}u^j$。
式 (6)、(11)、(17) 和 $\tau_0=0$ 给出
$$
(\mathcal D_e+8u e^{2w})\tau=8u e^{2w}.                     \tag{18}
$$
低带方程为 $\mathcal D_ew=-4u e^{2w}$。算子与 $\Theta$ 对易，故
$$
(\mathcal D_e+8u e^{2w})(-2\Theta w)=8u e^{2w}.
$$
两者零常数相同，$1\le j\le m$ 的对角元 $d_{2j}$ 是单位，三角唯一性给出
$$
\tau=-2\Theta w\pmod{u^{m+1}}.                             \tag{19}
$$
令 $E_1=e^w(\tau-1)$，$E_2=2e^{2w}(\tau-1)$，则
$$
E_1=-(1+2\Theta)e^w,\qquad
E_2=-2e^{2w}(1+2\Theta w).                                  \tag{20}
$$

### Step 6. 奇带及中间奇共振项的严格排除

令 $B_j=pA_{p+j}$，$0\le j<m$。用式 (7) 作三角归纳可证明这些量整。
对于指数与响应的乘积，设总次数 $N\le p+m-1$。若响应下标
$s\in[m,p-1]$，则指数下标 $N-s\le p-1$，该指数系数整。
其 $p$ 倍贡献高度至少 $M-2m\ge3m$，在 $R$ 中为零。
若指数下标 $\ge p$，则响应下标至多 $m-1$，正是整的低奇带。
若响应下标 $\ge p$，则指数下标小于 $m$。两个高带不能同时出现。
这证明整性归纳，并逐项穷尽了所需的乘积类型。

记 $a=\sum_{j=0}^{m-1}\bar A_ju^j$、$\sigma=\sum_{j=0}^{m-1}\bar B_ju^j$，
$\mathcal D_ou^j=d_{2j+1}u^j$。式 (7)、(11)、(17) 给出
$$
(\mathcal D_o+8u e^{2w})\sigma=-\tfrac12E_1-8uE_2a.          \tag{21}
$$
低带满足 $(\mathcal D_o+8u e^{2w})a=-e^w/2$。
对该式应用 $1+2\Theta$，逐项对乘法系数求导，得
$$
(\mathcal D_o+8u e^{2w})\bigl(-(1+2\Theta)a\bigr)
=\tfrac12e^w(1+2\Theta w)+16u e^{2w}a(1+2\Theta w),
$$
右端等于式 (21)。$0\le j<m$ 的 $d_{2j+1}$ 为单位，故
$$
\sigma=-(1+2\Theta)a\pmod{u^m}.                            \tag{22}
$$
特别地
$$
e^{2w}\sigma+E_2a=-(3+2\Theta)(e^{2w}a)\pmod{u^m}.          \tag{23}
$$
式 (23) 的系数 $3$ 来自一次响应和二次指数的全部三项，未省略中间共振贡献。

### Step 7. 端点系数消去整个预临界层

式 (5)、(17)、(20)、(23) 给出
$$
\begin{aligned}
4^D p[L^D]\mathcal B_3
&=-[u^m]E_1-16[u^{m-1}](e^{2w}\sigma+E_2a)\\
&=(2m+1)[u^m]e^w
  +16(3+2(m-1))[u^{m-1}]e^{2w}a=0
\end{aligned}                                             \tag{24}
$$
在 $R$ 中成立，因为两个系数都是 $2m+1=p=0$。
此前的整性归纳已证明式 (24) 左侧在 $\mathcal O^+$ 中有定义，
$4$ 是单位，故式 (1) 成立。
首一性给出 $[L^p]U_{\rm cl}=[L^D]S=h^{-D}p^2[L^D]\mathcal B_3$，
得到式 (2)。

### Step 8. 新根界与旧负端点的处置

对 $U_{\rm cl}$，$u_0$ 为单位，$v_h(u_j)\ge e_*$（$1\le j<p$），
$v_h(u_p)\ge e_*+m$。若 $t=v_h(\ell)>-\delta$ 且 $t\le0$，则
$$
v_h(u_j\ell^j)\ge e_*+jt>0\quad(1\le j<p),\qquad
v_h(u_p\ell^p)\ge e_*+m+pt>0.
$$
故 $U_{\rm cl}(\ell)$ 为单位，证明式 (3) 的无根部分。
正赋值及零赋值处 $U_{\rm cl}$ 已知为单位，故所有根均满足式 (3)。
正簇每根 $\alpha$ 有严格正赋值，所以 $t\le0$ 时
$v_h(\ell-\alpha)=t$。$P_{\rm cl}$ 首一次数 $m$ 给出式 (4)。
$\delta>e_*/p$，因此旧端点 $-e_*/p$ 严格落在本次已证区间内。
新端点 $-\delta$ 可能出现最低项并列，本文不包含它。证毕。$\square$

## Corrections, boundaries, and open risks

- 原模 $h$ 稿 Step 2 的 $A$ 有理约化只能用于 $r<m$；本文使用式 (8)
  与明确乘积支撑处理其余中间层，没有把负赋值量直接约化。
- 单谐波有理核只通过准确倍角变换作用于 $W$；没有声称整个 $A$ 有全局整有理核。
- 证明使用 $H<m$ 时的 $p$-单位符号系数。临界 $H^m$ 的 Chebyshev 反射缺陷
  尚未处理，不能把式 (1) 擅自加强为严格大于 $m$，也不能宣称恰等于 $m$。
- 其余商系数的准确高度、完整负 Newton 图、负因子因子型与简单性仍开放。
- 本件只推进同一个实际 forcing。不是 Paper30 正式候选、篇幅认证、稿件或 PDF；
  不涉及 Route A/B 或任何投稿上传。
