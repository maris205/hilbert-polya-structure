# Proof / Derivation Package：第一 forcing 下一层的同对象最高矩复用

日期：2026-09-08。作者有界替代证明，使用 proof-writer 与 formula-derivation。
本件只新增本文件，不改旧 A20、T、接受记录或完整第三 forcing 的科学中心。
没有独立数学审查资格；以下作者证明不充当独审票、容量票或任何对外效力。

## Claim / Target

固定任意素数 $p\ge5$、任意整数 $a\ge2$ 及任意本原 $p^a$ 次单位根 $\zeta$。
保持原双谐波模型、正 kick、SUM action、实际分支与规范

$$
m=\frac{p-1}{2},\qquad \chi=(-1)^{m+1},\qquad
h=D_1=2-\zeta-\zeta^{-1},\qquad \rho=-h,\qquad L=\rho\lambda,
\qquad M=p^{a-1}m=v_h(p).
$$

独立形式变量记为 $H$。原有限低块的第一内部 forcing 记为
$\mathcal B_1(H,L)$；其准确递推与实际对应在下文给出。本件证明

$$
\boxed{[L^m]\mathcal B_1(H,L)
=-\chi H^m-\frac\chi{16}H^{m+1}+O(H^{m+2})
\quad\text{在 }\mathbb F_p[[H]]\text{ 中}.}
\tag{R1}
$$

对同一原对象在实际圆分整环 $\mathcal O^+=\mathbb Z_p[h]$ 中有

$$
\boxed{[L^m]\mathcal B_1(h,L)
=-\chi h^m-\frac\chi{16}h^{m+1}+O(h^{m+2}).}
\tag{R2}
$$

目标是用已经接受的正端最高矩替换旧 A20 的一次奇响应展开和有限双和求值；
不是把第一 forcing 当作完整第三 forcing 的替代目标。

## Status

证明：`PROVABLE AS STATED`。推导：`COHERENT AS STATED`。
原全部量词和实际参数规范不变，不新增科学假设。
这两个状态仅表明本件给出完整作者论证，不表示新复用接口已经独立接受。

## Sources, Accepted Inputs, and Reading Scope

全文读取两项技能、下列 T 与 A20；另核对原局部结构的定义及 Steps 1–3、
T 的接受处置和实际桥义务清点。只调用以下有界数学输入。

| 来源 | 本件使用及边界 |
| --- | --- |
| [T：第三首层有限算子证明](PAPER30_TWIST_THIRD_FIRST_LAYER_OPERATOR_DIAGNOSIS_V1_20260908.md) | 式 (1) 的真实有限递推、式 (12) 的零阶纯偶／一次奇有限解，以及 Steps 3–6 直接证明的 (T3)。不由 T 的最终第三 forcing 单位倒推矩。 |
| [T 的接受处置 §3.2](PAPER30_TWIST_BLOCK_ENDPOINT_REPLACEMENT_DISPOSITION_V1_20260908.md) | 只确认 (T3) 是已独立接受的可引用输入；处置文字不代替 T 的证明。 |
| [原第一内部局部结构](PAPER30_TWIST_PRIME_POWER_LOCAL_STRUCTURE_PROBE_V1_20260907.md) | 式 (4)–(11) 的规范、有限整性、实际代入和非驻值 Euler 身份；不重新评价其后 Newton／分解结论。 |
| [A20：原下一层证明](PAPER30_TWIST_FIRST_FORCING_TOP_NEXT_LAYER_PROOF_V1_20260908.md) | 作为待替换目标及对象接口核对。下文重新推导其反射展开与式 (9) 的配对权重；不调用其式 (10)–(15) 的一次响应或双和结论，不以其 (1)–(4) 的目标数值为输入。 |

T 中的全矩 $W(H,b,L)$ 与 A20 中的纯偶函数 $W(H,u)$ 不是同一个符号对象。
下文分别重命名为 $\mathscr W(H,b,L)$ 与 $E(H,u)$，并从递推唯一性证明对应，
不因两稿使用过同名字母便移植结论。

## Assumptions, Notation, and Invariant Object

工作整环为 $\mathscr R=\mathbb Z_{(p)}[b,L][[H]]$；$b$ 是辅助幅度，实际仍取 $b=1$。
取整数 Chebyshev 多项式

$$
C_0=2,\quad C_1=2-H,\quad C_{n+1}=(2-H)C_n-C_{n-1},\qquad
d_n=\frac{C_n-2}{H},\qquad \Omega_n=-d_n-Hd_n'.
\tag{1}
$$

令 $\mathcal D_Hx^n=d_nx^n$。唯一有限低块
$P=\sum_{n=1}^{p-1}P_nx^n$ 满足

$$
\mathcal D_HP=-\frac{bx}{2}e^P-Lx^2e^{2P}\pmod{x^p}.
\tag{2}
$$

因 $d_n(0)=-n^2$，$1\le n<p$ 时 $d_n$ 是单位；每一右侧的第 $n$ 项
只依赖此前系数。所需指数阶乘至多为 $(p-1)!$，故三角递推在 $\mathscr R$ 中合法。
第一 forcing 在 $b=1$ 处取值；共享矩暂时保留辅助幅度：

$$
\mathcal B_1(H,L)=\left(-[x^{p-1}]e^P-2L[x^{p-2}]e^{2P}\right)\big|_{b=1},\qquad
\mathscr W(H,b,L)=\sum_{i=1}^{p-1}\Omega_iP_iP_{p-i}.
\tag{3}
$$

本次始终计算 (3) 的第一 forcing 最高参数系数。
共享矩只是同一低块的辅助不变量，定义

$$
\mathscr W_{\rm top}(H)=[L^m]\mathscr W(H,1,L).
$$

T 的已证输入 (T3) 正是

$$
\mathscr W_{\rm top}(H)=-\frac12-\frac3{32}H\pmod{H^2}
\quad\text{在 }\mathbb F_p[[H]]\text{ 中}.
\tag{4}
$$

所有形式截断均是有限商环中的同余，不是数值近似；不限制 $L$ 为零、幂零或某个根。

## Proof Strategy / Dependency Map

1. 同一单位三角递推给 T 与 A20 的低块及幅度分解逐系数相同。
2. 有限非驻值 Euler 身份与准确 Chebyshev 反射给 forcing 的两层权重。
3. 同一配对的 $\Omega_i$ 权重给共享矩；两组权重相减只剩零阶平方矩。
4. 已接受的式 (4) 与一个初等有限和给 (R1)，不重新求一次奇响应。
5. 原形式整性和 $M\ge m+2$ 将形式模 $p$ 结论送回准确实际对象，得到 (R2)。

## Proof

### Step 1. 同对象与最高参数缩放

T 式 (1) 与本件式 (2) 相同。A20 在 $b=1$ 的 $V_n$ 方程也正是式 (2)
逐系数的方程；引入 $b$ 后，它的右侧第一项同样乘 $b$。
三稿使用的 $d_n$ 均由式 (1) 给出。因此单位三角唯一性给出
$P_n=V_n$；没有传播子符号、整体幅度或实际 $L$ 的改变。

式 (2) 的齐次性进一步给

$$
P_n=\sum_{0\le2j\le n}c_{nj}(H)b^{n-2j}L^j.
\tag{5}
$$

证明采用递推归纳：乘积中每个 $x^n$ 系数的幅度权重都是 $n$，
其中 $b,L$ 的权重分别为 $1,2$；$d_n$ 不含 $b,L$，取逆保持权重。
因此总下标为 $p=2m+1$ 的配对中，$L^m$ 恰对应一次 $b$，
并且 $\deg_L\mathscr W(H,1,L)\le m$。

令

$$
u=\frac{Lx^2}{4},\qquad
P(H,b,L,x)=E(H,u)+bx\,O(H,u)+O(b^2).
\tag{6}
$$

$E$ 只需 $u^1,\ldots,u^m$，$O$ 只需 $u^0,\ldots,u^{m-1}$。
记 $E_r=[u^r]E$、$O_s=[u^s]O$。准确符号对应是

$$
(E,O)=(A,B)_{\rm T}=(W,A)_{\rm A20}.
\tag{7}
$$

式 (7) 由相同递推及相同 $u=Lx^2/4$ 得到，区别于 T 所警示的其他负端响应符号。
最高项每对给出

$$
[L^m]\left(P_{2r}P_{p-2r}\big|_{b=1}\right)
=4^{-m}E_rO_{m-r},\qquad 1\le r\le m.
\tag{8}
$$

这里一次奇下标 $p-2r=2(m-r)+1$ 严格小于 $p$。
费马小定理给 $4^m=2^{p-1}=1$ 于 $\mathbb F_p$，故之后在模 $p$ 公式中
可以令 $4^{-m}=1$。该等式没有被提升为特征零的精确缩放等式。

### Step 2. 反射的下一项及两个端点权重

用形式 Laurent 变量 $z$ 表示 $H=2-z-z^{-1}$，记

$$
S_i(H)=\frac{z^i-z^{-i}}{z-z^{-1}},\qquad
\lambda_H=\chi H^m(4-H)^{m+1}.
$$

$S_i$ 是 $H$ 的整数多项式；$\lambda_H$ 是反射因子，不是物理参数 $\lambda$。
特征 $p$ 的 Frobenius 给 $C_p=2-H^p$ 和
$z^p-z^{-p}=(z-z^{-1})^p$。
Chebyshev 加法公式

$$
2C_{p-i}=C_pC_i-(z^p-z^{-p})(z^i-z^{-i})
$$

与 $(z-z^{-1})^2=-H(4-H)$ 给出精确多项式身份

$$
d_i-d_{p-i}=\frac{\lambda_H}{2}S_i+H^{2m}+\frac{H^p}{2}d_i.
\tag{9}
$$

比较式 (1) 的 $H,H^2$ 系数可得

$$
d_i=-i^2+\frac{i^2(i^2-1)}{12}H+O(H^2),\qquad
S_i=i-\frac{i(i^2-1)}6H+O(H^2).
\tag{10}
$$

第一式的系数满足 Chebyshev 递推及 $C_0,C_1$ 初值；第二式也可由
$C_i'=-iS_i$ 得到，其中 $1\le i<p$ 使 $i$ 可逆。
再用 $m+1=1/2$ 于 $\mathbb F_p$，有

$$
\lambda_H=4\chi H^m(1-H/8)+O(H^{m+2}).
$$

由于 $2m\ge m+2$、$p=2m+1\ge m+2$，式 (9) 得

$$
d_i-d_{p-i}
=2\chi iH^m-\frac{\chi i(4i^2-1)}{12}H^{m+1}
+O(H^{m+2}).
\tag{11}
$$

原有限 action

$$
\Phi=[x^p]\left(\frac12P\mathcal D_HP+
\frac b2xe^P+\frac L2x^2e^{2P}\right)
$$

只用低于 $p$ 的模态，且属于 $\mathscr R$。
在 $b=1$ 的实际分支上，它的导数为
$\partial\Phi/\partial P_i=(d_i-d_{p-i})P_{p-i}/2$，不是零。
按权重 $i,1,2$ 对 $P_i,b,L$ 应用 Euler 身份，得原准确式

$$
\mathcal B_1=-2p\Phi+
\sum_{i=1}^{p-1}i(d_i-d_{p-i})P_iP_{p-i}.
\tag{12}
$$

模 $p$ 时首项消失是因为 $\Phi$ 整，而不是把分支错误地设为 action 驻值点。
在式 (11) 乘上 $i$ 后，两层权重分别是 $i^2$、$i^2(4i^2-1)$，
于模 $p$ 反射 $i\mapsto p-i=-i$ 下均为偶函数。
故式 (8) 的每个偶／奇配对贡献两次，给出

$$
[L^m]\mathcal B_1=\chi4^{-m}H^m Q(H)+O(H^{m+2}),
\tag{13}
$$
$$
Q(H)=16\sum_{r=1}^m r^2E_rO_{m-r}
-\frac{2H}{3}\sum_{r=1}^m r^2(16r^2-1)E_rO_{m-r}
\pmod{H^2}.
\tag{14}
$$

这里第一和保留一次 $H$，第二和只需零阶；奇端权重没有省去。
式 (14) 正是 A20 式 (9) 的花括号，但本件未引用 A20 的求和结果。

### Step 3. 用共享最高矩消去一次低响应

由 $\Omega_i=-d_i-Hd_i'$ 和式 (11)，

$$
\Omega_i-\Omega_{p-i}
=-(1+H\partial_H)(d_i-d_{p-i})\in H^m\mathbb F_p[H].
\tag{15}
$$

由于 $m\ge2$，式 (15) 允许在模 $H^2$ 的最高矩中合并两个权重。
式 (10) 给

$$
\Omega_{2r}=4r^2-\frac{2H}{3}r^2(4r^2-1)+O(H^2).
$$

因此式 (8) 及 $4^{-m}=1$ 给出

$$
\mathscr W_{\rm top}
=8\sum_{r=1}^m r^2E_rO_{m-r}
-\frac{4H}{3}\sum_{r=1}^m r^2(4r^2-1)E_rO_{m-r}
\pmod{H^2}.
\tag{16}
$$

置 $\Sigma_2(H)=\sum_{r=1}^m r^2E_rO_{m-r}$。
从式 (14) 减去两倍式 (16)，每对权重的差是

$$
-\frac{2H}{3}r^2(16r^2-1)
+\frac{8H}{3}r^2(4r^2-1)=-2Hr^2.
$$

从而得到本件核心复用身份

$$
\boxed{Q(H)=2\mathscr W_{\rm top}(H)-2H\Sigma_2(0)\pmod{H^2}.}
\tag{17}
$$

这里只因前面已有 $H$ 才将 $\Sigma_2(H)$ 换为其零阶；
一次纯偶与一次奇响应已完整包含在 $\mathscr W_{\rm top}$ 中，没有分别丢项。

### Step 4. 一个零阶有限和与目标系数

T 式 (12) 在准确有限区间上给

$$
E(0,u)=\sum_{r=1}^m\frac{u^r}{r}\pmod{u^{m+1}},\qquad
O(0,u)=\frac12\sum_{s=0}^{m-1}u^s\pmod{u^m}.
\tag{18}
$$

它们是式 (2) 在 $H=0$ 的纯偶与一次奇唯一解，故通过 Step 1 可直接调用。
没有使用特征 $p$ 的无限对数，全部分母 $r\le m<p$。
因此

$$
\Sigma_2(0)=\sum_{r=1}^m r^2\frac1r\frac12
=\frac{m(m+1)}4=-\frac1{16}\quad\text{在 }\mathbb F_p\text{ 中}.
\tag{19}
$$

将已接受的式 (4) 和式 (19) 代入新身份 (17)，得到

$$
Q(H)=2\left(-\frac12-\frac3{32}H\right)
-2H\left(-\frac1{16}\right)
=-1-\frac1{16}H\pmod{H^2}.
\tag{20}
$$

再代回式 (13)，并使用模 $p$ 的 $4^{-m}=1$，即得 (R1)。
本步没有再展开 $[H]O_s$，也没有重算 A20 的奇分母双和。

### Step 5. 同一实际对象及最小精度边界

原真实传播子 $D_n=2-\zeta^n-\zeta^{-n}$ 满足
$d_n(h)=-D_n/h=D_n/\rho$。原局部结构式 (4)–(5) 的换元给

$$
P_n(h,1,L)=V_n(L)=\rho^n v_n(L/\rho),\qquad
\mathcal B_1(h,L)=\rho^{p-1}\mathcal B_{p\mid p^a}(L/\rho).
\tag{21}
$$

所以本件计算的是原第一内部 forcing 的准确有限低块，而不是为负端另造的参照块。
因 $a\ge2$，$p<p^a$；真实内部模态 $V_p$ 不是共振零模，本件未定义或置零它。

形式整性使 (R1) 精确表示为

$$
[L^m]\mathcal B_1(H,L)+\chi H^m+\frac\chi{16}H^{m+1}
\in(p,H^{m+2})\mathbb Z_{(p)}[[H]].
\tag{22}
$$

先在这个整环中取原对象，再代入 $H=h$；不是把 $\mathbb F_p$ 直接嵌入特征零。
$h$ 的正赋值保证单位形式级数可代入，且

$$
M=p^{a-1}m\ge pm\ge5m\ge m+2.
$$

故式 (22) 的 $p$ 倍误差和形式余项均落入 $h^{m+2}\mathcal O^+$，得到 (R2)。
这也吸收了模 $p$ 使用 $4^m=1$ 与其特征零数值之间的差。
在最小情形 $p=5,m=2,a=2$，反射式 (9) 的 $H^{2m}$ 恰为 $H^4$，
正是排除阶 $H^{m+2}$；式 (15) 的缺陷从 $H^2$ 起，不进入模 $H^2$ 共享矩。
此时 $M=10\ge4$，所有分母 $2,3,4,6,12,16,32$ 仍是单位。
因此没有以 $p\ge7$ 或更高 $a$ 缩窄原目标。证毕。$\square$

## Replacement Scope, Verification, and Boundaries

新增复用链是：同一低块的 T 最高矩 (4) → 权重差 (17) → 零阶和 (19)
→ A20 原下一层 (R1)–(R2)。T 的 Steps 3–6 从有限纯偶／一次奇方程直接求矩，
不引用 A20 的目标或双和，因此这条复用不引入证明循环。
T 的原矩证明必须仍完整保留并被准确引用；复用不是宣称矩无需证明。

可被本件替代的是 A20 针对此系数的 Steps 3–4：一次奇响应逐系数展开、
双和换序和最终 $R_m$ 的多项式余式求值。
A20 的真实非驻值 Euler 身份、反射下一项、偶／奇两端权重、幅度缩放和实际整性
仍是必需内容，本件已逐一保留并核对。旧 A20 及其接受记录原样保存。

作者以内存自由符号代数核对了每对权重差为 $-2Hr^2$、
反射下一项乘子为 $-(4i^2-1)/12$，以及式 (20) 的结果。
这些运算只是作者交叉检查，不构成一般素数量词的证据或非作者审查。
一般性由以上有限恒等式、单位分母及明确误差不等式保证。

本件不产生 A19–A22 完整新合并证明，不重新认证旧完整 Newton 图、互素或分裂域，
也不把下一层系数单独称作完整第三 forcing 非零证明。
若另沿 A20 的既有消费者关系使用本系数，仍须保留其各自准确权重和同阶其他来源。
没有外部检索、数值素数扫描、参数拟合、纸稿/PDF/页数操作或外部写入。

## Corrections or Missing Assumptions

无需修正目标或增加科学假设。仅做消歧记号变更：T 的全矩为 $\mathscr W$，
共享纯偶／一次奇块为 $E,O$；准确映射是式 (7)，实际规范不变。

## Open Risks

本件作者认为新证明闭合；仍需未参与本件推导者针对新复用身份、
同对象幅度映射及形式／实际转移做真正限定数学检查。
本件没有资格自行关闭这项独审程序，也不因此重开输入未变且已通过的 T 证明。
