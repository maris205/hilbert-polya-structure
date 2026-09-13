# Paper30：第三 forcing 零剩余根簇的唯一多项式分离

日期：2026-09-07。作者：`p30_third_forcing_general_independent`；
主控共同推导本轮实际次数、常数非零及高系数高度加强。
该代理在上一轮承担第三 forcing 独审；本轮改为本新引理的作者，
因此本件不是这个新引理的非作者独审票，仍待另一核查者审查。
本轮完整读取 `proof-writer`，调用已接受首层及端点误差身份，
不重审原来的 843／640 行证明。

## Claim

令 $p\ge5$、$a\ge2$，沿用任意本原 $p^a$ 次根的实际规范

$$
h=2-\zeta-\zeta^{-1},\quad \rho=-h,\quad L=\rho\lambda,\quad K^+=\mathbb Q_p(h),\quad
\mathcal O^+=\mathbb Z_p[h],\quad v_h(h)=1,
$$
$$
m=(p-1)/2,\quad M=p^{a-1}m=v_h(p),\quad \chi=(-1)^{m+1},
\quad q_3=3m+1.
$$

记已接受的第三 forcing 正规化为

$$
S(L)=h^{-q_3}p^2\mathcal B_3(L)\in\mathcal O^+[L],
\qquad \bar S(L)=cL^m,\qquad c=-3\chi/64\in\mathbb F_p^\times.
\tag{1}
$$

令 $D=\deg S=\deg\mathcal B_3$，并记
$e_*=M-(3m+1)>0$、$a_m=[L^m]S\in(\mathcal O^+)^\times$。
则实际有 $D=3m+1$、$S(0)\ne0$，并有唯一分解

$$
\boxed{S=P_{\rm cl}U_{\rm cl},\qquad
P_{\rm cl}\in\mathcal O^+[L]\text{ 首一},\quad
\deg P_{\rm cl}=m,\quad \bar P_{\rm cl}=L^m,}
\tag{2}
$$
$$
\boxed{U_{\rm cl}\in\mathcal O^+[L],\qquad
\bar U_{\rm cl}=c,\qquad \deg U_{\rm cl}=D-m=2m+1=p.}
\tag{3}
$$

高系数还满足完整一致高度

$$
\boxed{[L^j]S\in h^{e_*}\mathcal O^+\quad(j>m),\qquad
U_{\rm cl}\equiv a_m\pmod{h^{e_*}\mathcal O^+[L]}.}
\tag{3a}
$$

这里的 $P_{\rm cl}$ 与旧形式低块 $P(H,x)$ 不同。
式 (2) 的 distinguished 意为首一且所有非最高系数均在 $h\mathcal O^+$ 中。
$U_{\rm cl}$ 在所有局部整参数处取单位值，不声称它一定是多项式环中的单位。

在代数闭包中固定 $v_h$ 的延拓，并约定 $v_h(0)=+\infty$。
计代数重数，$\mathcal B_3$ 恰有 $m$ 个非零正赋值根，全部来自 $P_{\rm cl}$；
其余恰好 $p$ 个根全部为负赋值，来自 $U_{\rm cl}$。根界为

$$
\boxed{v_h(\alpha)\ge1/m\quad(P_{\rm cl}(\alpha)=0),\qquad
v_h(\beta)\le-e_*/p\quad(U_{\rm cl}(\beta)=0).}
\tag{3b}
$$

因此开区间 $(-e_*/p,1/m)$ 内没有根的赋值，也没有零根。
一般引理本身仍完整处理零常数项与零根，不把实际的非零性预加为其假设。

设 $\alpha_1,\ldots,\alpha_m$ 为 $P_{\rm cl}$ 的根，按重数重复列出。
对任意有限局部扩域 $E/K^+$ 及任意 $\ell\in\mathcal O_E$，有准确公式

$$
\boxed{v_h(S(\ell))=v_h(P_{\rm cl}(\ell))
=\sum_{j=1}^m v_h(\ell-\alpha_j),}
\tag{4}
$$
$$
\boxed{v_h(\mathcal B_3(\ell))
=3m+1-2M+\sum_{j=1}^m v_h(\ell-\alpha_j).}
\tag{5}
$$

同一实际模态还满足
$v_h(V_{3p}(\ell))=m+1-2M+\sum_{j=1}^m v_h(\ell-\alpha_j)$。
求和在任意包含 $E$ 与这些根的有限扩域中解释，并包含值 $+\infty$。
这些式子与根界不预定簇内根的具体赋值、分裂域或简单性。

此外，对任意有限局部扩域中的非零参数 $\ell$，不要求它整，若
$-e_*/p<t=v_h(\ell)<1/m$，则有准确点值

$$
\boxed{v_h(S(\ell))=mt,\quad
v_h(\mathcal B_3(\ell))=3m+1-2M+mt,\quad
v_h(V_{3p}(\ell))=m+1-2M+mt.}
\tag{5a}
$$

区间两端均开；不宣称边界点仍满足这些点值等式。

## Status

`PROVABLE AS STATED`，作者证明完成；原主张无需削弱或增添参数排除。
本件给出唯一根簇分离、准确两侧根数及一致空隙，
不冒充下一 Newton 层、准确斜率或完整分裂结构。

## Assumptions and Accepted Inputs

动力学输入是已接受的
[一般第三 forcing V1](PAPER30_TWIST_THIRD_FORCING_GENERAL_PRIME_PROBE_V1_20260907.md)，
SHA256 为 `1c91dd36cd2932f11635e0aa2b1b817579af65f0f5fef34daac9eda2a32fd88a`。
本件调用其整性与完整参数剩余，以及其式 (17) 和已接受模型替换共同给出的
模 $h^M$ 端点配对身份，不重开这些证明。
模态点值只另调用同稿已接受的
$V_{3p}=\mathcal B_3/(2d_{3p})$、$v_h(d_{3p})=2m$。

有限递推与 forcing 的定义保持为

$$
d_nV_n=-\frac12[x^{n-1}]e^V-L[x^{n-2}]e^{2V},\qquad
d_n=-\frac{2-\zeta^n-\zeta^{-n}}h,
$$
$$
\mathcal B_3=-[x^{3p-1}]e^V-2L[x^{3p-2}]e^{2V},\qquad V_1=1/2.
$$

实际次数界使用有限递推的加权次数；准确次数及常数非零另由数域实嵌入证明。
高系数高度使用接受的端点同余与单位模型的参数次数。
没有假设 $S$ 首一、最高系数为单位、$S(0)\ne0$ 或剩余次数等于实际次数；
这里实际的 $S(0)\ne0$ 是新推论，不是输入。

## Notation

一般引理使用完备离散赋值环 $R$、分式域 $K$、均匀化元 $\pi$、
剩余域 $k=R/\pi R$，以及归一化赋值 $v(\pi)=1$。
上划线表示约化至 $k$。代数根均按重数计；$\operatorname{ord}_{X=0}$
表示多项式在零点的消失重数，不是系数赋值。
对代数扩域采用固定的延拓赋值，有限扩域的值群不要求等于 $\mathbb Z$。

## Proof Strategy

使用固定次数的逐阶 Hensel 提升，并完整给出提升和唯一性证明。
每一步只解 $cA+X^mB$ 的低／高次数分解，因而不需要简单根假设，
也不需要将整个多项式改为首一。
根的位置及整参数点值随后由唯一最低赋值项直接判断。

## Dependency Map

1. 因子存在性使用 $R$ 完备、$c\ne0$ 和有限实际次数。
2. 因子唯一性使用首一归一化、固定次数及 $R$ 的赋值分离性。
3. 根簇大小使用因子次数与两种系数剩余，不使用平方自由性。
4. 整参数距离公式使用 $U$ 在所有有限扩域整点取单位值。
5. 准确次数与常数非零使用全局代数系数的一个实嵌入，不对局部域排序。
6. 高系数高度使用模 $h^M$ 的端点配对及模型次数；商的高度由首一因子给出。
7. 实际点值使用 $\mathcal B_3=h^{q_3}p^{-2}S$；根空隙使用两因子的系数高度。

## Proof

### Step 1. 一般 DVR 分离引理：固定次数提升

设 $S_*(X)\in R[X]$ 满足

$$
\overline{S_*}=cX^m,\qquad c\in k^\times,\qquad m\ge1.
\tag{6}
$$

令 $D_* =\deg S_*$，则 $D_*\ge m$。取 $c$ 的任意单位提升 $c_0\in R^\times$，
从 $P_1=X^m$、$U_1=c_0$ 开始。它们的乘积与 $S_*$ 模 $\pi$ 相同。

假设已构造 $P_n,U_n$，其中 $P_n$ 首一且次数为 $m$，
$\deg U_n\le D_*-m$，剩余分别为 $X^m,c$，并且
$S_*-P_nU_n\in\pi^nR[X]$。设

$$
E_n=\frac{S_*-P_nU_n}{\pi^n},\qquad \deg E_n\le D_*.
$$

在 $k[X]$ 中存在唯一分解

$$
\bar E_n=c\bar A_n+X^m\bar B_n,
\quad \deg\bar A_n<m,\quad \deg\bar B_n\le D_*-m.
\tag{7}
$$

具体地，$\bar A_n$ 等于 $\bar E_n$ 除以 $X^m$ 的余式乘 $c^{-1}$；
$\bar B_n$ 是剩余差除以 $X^m$ 的商。这也证明唯一性。
选择相同次数范围的系数提升 $A_n,B_n$，定义

$$
P_{n+1}=P_n+\pi^nA_n,\qquad U_{n+1}=U_n+\pi^nB_n.
$$

乘积增加 $\pi^n(U_nA_n+P_nB_n)+\pi^{2n}A_nB_n$。
式 (7) 消去第 $n$ 层误差，而 $2n\ge n+1$，故新的误差在 $\pi^{n+1}R[X]$。
首一性、所有次数界及两项剩余都保持。

每个系数序列均为 Cauchy 序列。$R$ 完备且次数界固定，故极限仍是多项式：

$$
P_*\in R[X],\quad \deg P_*=m,\quad P_*\text{ 首一},\quad\bar P_*=X^m,
$$
$$
U_*\in R[X],\quad \deg U_*\le D_*-m,\quad\bar U_*=c.
$$

逐系数取极限给出 $S_*=P_*U_*$。多项式域上的次数可加，
所以 $\deg U_*=D_*-m$，而不只是一个上界。
这个构造没有使用 $S_*$ 的最高系数可逆，也没有得到无限次的商。

### Step 2. 唯一性及多项式商的边界

设另有 $S_*=P' U'$，满足 $P'$ 首一、次数为 $m$、$\bar P'=X^m$，
且 $U'\in R[X]$。约化后有 $X^m\bar U'=cX^m$，
因此 $\bar U'=c$，并且 $\deg U'=D_*-m$。

若 $P'-P_*,U'-U_*$ 均属于 $\pi^nR[X]$，记除以 $\pi^n$ 的差为 $A,B$。
其中 $\deg A<m$、$\deg B\le D_*-m$。由两个乘积相同，约化得到

$$
c\bar A+X^m\bar B=0.
$$

比较低于 $m$ 的部分给 $\bar A=0$，继而 $\bar B=0$。
所以差从 $\pi^n$ 提升至 $\pi^{n+1}$。初始的模 $\pi$ 相等已成立；
归纳并用 $\bigcap_n\pi^nR=0$，得到 $P'=P_*$、$U'=U_*$。

即使先只假设 $P'$ 在 $K[X]$ 中整除 $S_*$，商也自动在 $R[X]$：
对首一 $P'$ 在 $R[X]$ 中作带余除法，再与 $K[X]$ 中的零余式比较即可。
故唯一性并未遗漏一个仅在分式域中出现的同类因子。

当 $D_*>m$ 时，$U_*$ 非常数，其最高系数非单位，因为 $\bar U_*=c$。
所以 $U_*$ 不必是 $R[X]$ 的单位；它只是具有单位常数项及非单位高次系数。
当 $D_*=m$ 时，$U_*$ 则是常数单位。两种情况均已包含。

### Step 3. 所有根的赋值分离，包含零根与重根

写 $P_*(X)=X^m+\sum_{i<m}b_iX^i$，其中 $b_i\in\pi R$。
若非零代数元 $\alpha$ 满足 $v(\alpha)\le0$，则

$$
v(b_i\alpha^i)\ge1+i\,v(\alpha)>m\,v(\alpha)
\qquad (i<m).
$$

于是 $\alpha^m$ 是 $P_*(\alpha)$ 中唯一的最低赋值项，不能被其余项抵消。
所以 $P_*$ 的每个非零根均有正赋值；零根按 $v(0)=+\infty$ 计入此簇。
在代数闭包中，首一 $m$ 次多项式共有 $m$ 个根，按重数计。

对 $U_*=u_0+\sum_{j\ge1}u_jX^j$，有 $u_0\in R^\times$、$u_j\in\pi R$。
若 $v(\beta)\ge0$，则常数项赋值为零，其余项至少为一，
故 $U_*(\beta)$ 是单位，不能为零。这同时适用于 $\beta=0$。
因此 $U_*$ 的全部 $D_*-m$ 个根均为负赋值。

$P_*,U_*$ 的根没有交叠，且 $S_*$ 的全部根由两者组成，重数相加。
令 $r_0=\operatorname{ord}_{X=0}S_*$。因 $U_*(0)\ne0$，
$r_0=\operatorname{ord}_{X=0}P_*\le m$；非零正赋值根恰有 $m-r_0$ 个。
这不要求 $S_*(0)\ne0$，也不要求簇内根简单。

### Step 4. 所有有限扩域整参数的准确距离公式

令 $E/K$ 是任意有限扩域，$\ell\in\mathcal O_E$。
常数项 $u_0$ 在 $\mathcal O_E$ 中仍为单位；所有 $u_j\ell^j$、$j\ge1$，
均在其极大理想中。因此 $v(U_*(\ell))=0$，从乘积身份得到

$$
v(S_*(\ell))=v(P_*(\ell)).
$$

取包含 $E$ 及 $P_*$ 全部根 $\alpha_1,\ldots,\alpha_m$ 的有限扩域。
首一因子的分解 $P_*(X)=\prod_{j=1}^m(X-\alpha_j)$ 给出

$$
v(S_*(\ell))=\sum_{j=1}^m v(\ell-\alpha_j).
\tag{8}
$$

若 $\ell$ 恰是某个根，等式两边均为 $+\infty$，公式仍成立。
若 $v(\ell)=0$，每个差都为单位；若 $v(\ell)>0$ 或 $\ell=0$，
每个差具有正扩展赋值，故总值严格大于零。
本论证不把分歧扩域中的严格不等式提升为整数“加一”下界。

### Step 5. 第三 forcing 的准确次数与常数非零

实际递推的 $d_n$ 不含 $L$ 且在 $n<3p$ 的本范围非零。
归纳若 $\deg_LV_i\le\lfloor i/2\rfloor$，则指数的第 $r$ 个系数
由总指标和为 $r$ 的乘积组成，其参数次数至多 $\lfloor r/2\rfloor$。
递推中的两项因此分别有次数至多
$\lfloor(n-1)/2\rfloor$、$1+\lfloor(n-2)/2\rfloor$，
证明所需 $\deg_LV_n\le\lfloor n/2\rfloor$；起点是 $V_1=1/2$。
对 $\mathcal B_3$ 的两项应用同一界，得到

$$
\deg_L\mathcal B_3\le\left\lfloor\frac{3p-1}{2}\right\rfloor
=3m+1.
$$

还需证明最高系数和常数项非零，不能从上界或剩余多项式自行推断。
所有有限递推系数都在数域 $\mathbb Q(h)$ 中：传播子是 $h$ 的有理多项式，
其余操作只有有限次数的加、乘和非零标量除法。
先取 $\mathbb Q(\zeta)$ 到 $\mathbb C$ 的嵌入，再限制到 $\mathbb Q(h)$；
记 $\zeta$ 的像为复本原 $p^a$ 次根 $\zeta_{\mathbb C}$。
在该嵌入下

$$
h=|1-\zeta_{\mathbb C}|^2>0,\qquad
d_n=-\frac{|1-\zeta_{\mathbb C}^n|^2}{h}<0
\quad(1\le n<3p<p^a).
\tag{9}
$$

故原递推使各 $V_n$ 的全部 $L$ 系数非负：指数展开系数非负，
而递推整体乘数 $-1/d_n$ 为正。起点 $V_1=1/2>0$，
且 $V_2=-(1/4+L)/d_2$ 的常数系数和一次系数均严格为正。

记 $E_N=[x^N]e^V$。对于每个 $0\le j\le\lfloor N/2\rfloor$，
在 $e^V=\prod_n e^{V_nx^n}$ 中选择 $j$ 个 $V_2$ 的一次项和
$N-2j$ 个 $V_1$，得到 $[L^j]E_N$ 的严格正贡献

$$
\frac{([L]V_2)^j V_1^{N-2j}}{j!(N-2j)!}>0.
$$

其余贡献非负，因此这些系数全部严格为正。
而 $e^{2V}$ 的所有系数也非负，所以
$\mathcal B_3=-E_{3p-1}-2L[x^{3p-2}]e^{2V}$ 的每个
$L^j$ 系数，$0\le j\le3m+1$，在该实嵌入下均严格为负。
由此 $D=3m+1$ 且 $\mathcal B_3(0)\ne0$，进而 $S(0)\ne0$。

这一实嵌入只证明原代数系数非零；嵌入的单射性将非零性带回原数域与局部实现。
没有给 $K^+$ 定序，也没有由系数同号声称参数根全实。

### Step 6. 高参数系数的一致实际高度

采用已接受的形式低块 $P(H,x)$ 与零常数单位模型 $Y(H,x),Z(H,x)$。
这里不把模型常数项与实际内部常数项混同；接受的模型替换误差已经包含后者。
记 $\mathcal D_kx^j=d_{kp+j}(H)x^j$，$1\le j<p$，并在模 $x^p$ 下记
$J=xe^P/2+2Lx^2e^{2P}$、$K=xe^P/4+2Lx^2e^{2P}$。
由低块的三角递推，$\deg_L P_i\le\lfloor i/2\rfloor$。
在 $J,K$ 的第 $j$ 个系数中，同一加权次数给出至多 $\lfloor j/2\rfloor$。
从模型方程

$$
(\mathcal D_1+J)Y=J/2,\qquad
(\mathcal D_2+J)Z=-K(Y-1/2)^2\pmod{x^p}
$$

作正次数单位三角归纳，得到
$\deg_L Y_i,\deg_L Z_i\le\lfloor i/2\rfloor$，$1\le i<p$。
乘积的指标相加时使用
$\sum\lfloor i_j/2\rfloor\le\lfloor(\sum i_j)/2\rfloor$，
而各传播子及其单位逆不含 $L$。

一般稿式 (17) 在接受的模型替换后给出实际同余

$$
p^2\mathcal B_3\equiv
\sum_{i=1}^{p-1}\left(
2i\delta_i^{\rm low}P_i(h)Z_{p-i}(h)
+i\delta_i^{\rm mid}Y_i(h)Y_{p-i}(h)\right)
\pmod{h^M\mathcal O^+[L]},
\tag{10}
$$

其中 $\delta_i^{\rm low}=d_i-d_{3p-i}$、
$\delta_i^{\rm mid}=d_{p+i}-d_{2p-i}$ 均与 $L$ 无关。
由于 $p$ 为奇数，
$\lfloor i/2\rfloor+\lfloor(p-i)/2\rfloor=m$。
故式 (10) 的右侧是次数至多 $m$ 的实际整多项式，
得到 $[L^j]p^2\mathcal B_3\in h^M\mathcal O^+$，$j>m$。
除以 $h^{q_3}$，便得式 (3a) 的第一项。
$e_*>0$ 因为 $M\ge5m$、$m\ge2$，所以 $e_*\ge2m-1\ge3$。

### Step 7. 唯一因子、商的高度与准确两侧根数

将一般引理应用于 $(R,K,\pi,S_*)=(\mathcal O^+,K^+,h,S)$，
得到式 (2)、(3)。实际 $S(0)\ne0$ 排除一般引理允许的零根，
所以恰有 $m$ 个有限正赋值根及 $D-m=p$ 个负赋值根，按重数计。

商的高系数还继承 $h^{e_*}$ 整除。为证明这一点，在
$(\mathcal O^+/h^{e_*}\mathcal O^+)[L]$ 中约化分解 $S=P_{\rm cl}U_{\rm cl}$。
由 Step 6，约化的 $S$ 次数恰为 $m$，因为 $a_m$ 是单位；
约化的 $P_{\rm cl}$ 仍首一次数 $m$。
若约化的 $U_{\rm cl}$ 有正次数 $t$，则乘积的最高系数就是其非零最高系数，
乘积次数为 $m+t>m$，矛盾。这一论证在有零因子的商环中仍有效，
原因是另一个因子首一。
因此 $U_{\rm cl}$ 约化后是常数，比较第 $m$ 项给出该常数为 $a_m$。
这证明式 (3a) 的第二项，不需要额外的 Hensel 重跑。

若 $P_{\rm cl}(\alpha)=0$、$v_h(\alpha)>0$，其首项的赋值为
$m v_h(\alpha)$，所有低次项的赋值至少为 $1$。
当 $v_h(\alpha)<1/m$ 时，首项是唯一最低项，不能相消。
所以正根都满足式 (3b) 的第一个界。

对 $U_{\rm cl}$，常数项为单位，其余系数至少有高度 $e_*$，次数恰为 $p$。
若负赋值元 $\beta$ 满足 $v_h(\beta)>-e_*/p$，则对每个 $1\le j\le p$，

$$
v_h([L^j]U_{\rm cl})+jv_h(\beta)
\ge e_*+jv_h(\beta)\ge e_*+pv_h(\beta)>0.
$$

常数项因此是唯一最低项，不能相消，证明负根界。
两界均直接在延拓值群中成立，不要求扩域未分歧。

最后由一般引理的式 (8) 与 $\mathcal B_3=h^{q_3}p^{-2}S$，
得到式 (4)、(5)，包括全部根参数处的无限值。
接受的 $V_{3p}=\mathcal B_3/(2d_{3p})$ 与 $v_h(d_{3p})=2m$
给出同一根距离和对应的模态基线；$p\ge5$ 使 $2$ 为单位。
高次数分支没有因剩余次数下降而被删除，而是被唯一的 $p$ 次商完整保留。

### Step 8. 无根开区间内，包括非整参数的准确点值

写 $S(L)=\sum_{j=0}^{3m+1}a_jL^j$。
已有 $v_h(a_m)=0$、$v_h(a_j)\ge1$ 对 $j<m$，
及 $v_h(a_j)\ge e_*$ 对 $j>m$。
若 $-e_*/p<t=v_h(\ell)<1/m$，则对于 $j<m$，

$$
v_h(a_j\ell^j)-mt\ge1+(j-m)t>0;
$$

对于 $j>m$，由于 $j-m\le p$，有

$$
v_h(a_j\ell^j)-mt\ge e_*+(j-m)t>0.
$$

后一个严格不等式在 $t\ge0$ 时由 $e_*>0$ 给出，
在 $t<0$ 时由 $e_*+(j-m)t\ge e_*+pt>0$ 给出。
故第 $m$ 项是唯一最低赋值项，直接得到 $v_h(S(\ell))=mt$。
乘回实际标量并使用已接受的模态除数，得到式 (5a)。
这不是把“$U_{\rm cl}$ 在整参数处为单位”擅自外推到非整参数，
也没有断言两端可能发生同阶相消时的准确值。
证明完成。$\square$

## Corrections or Missing Assumptions

- 无需假设原多项式首一或最高系数为单位；提升只使用剩余 $L^m$ 系数的单位性。
- 一般引理允许零根，非零正根数为 $m-r_0$；实际系统另以 Step 5 证明 $r_0=0$。
- 商在整参数处恒为单位，不等于它在多项式环中一定可逆。
- 唯一性要求 distinguished 因子首一；否则因子与商之间可转移常数单位。

## Open Risks and Delivery Boundary

- 本件已确定实际 $D=3m+1$、$r_0=0$ 及两侧准确根数；
  簇内根的下一 Newton 斜率、简单性、不可约性或分裂域仍未确定。
- 非整根分支由唯一 $p$ 次商保留并有一致赋值上界，但其准确赋值及因子型仍待证据。
- 本件不新增 $\mathcal B_2,\mathcal B_3$ 互素或完整素数幂 $C,Q$ 结论。
- 本件的准备分解机制是一般 Hensel 型代数，不单独作为系统新意或篇幅贡献。
- 没有运行任何素数或根扫描，也没有符号拟合；没有修改旧稿、失败或接受记录。
- 只新增此本地作者证明，待真正非作者核查；未作估页、立项、PDF、Route 或外部操作。
