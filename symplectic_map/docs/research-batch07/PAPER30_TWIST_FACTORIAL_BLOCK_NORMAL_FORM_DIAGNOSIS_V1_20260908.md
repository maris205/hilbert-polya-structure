# Paper30：两条有限阶乘块的统一正常形诊断 V1

日期：2026-09-08。作者推导；使用 `formula-derivation` 固定对象与误差，再按 `proof-writer` 完成证明。
唯一新增文件为本件；上一份 POSTFINITE_BRIDGE_OBLIGATIONS V1、原作者源与接受记录全部不改。

## Target and Claim

目标是为原 B1–B4 的阶乘／整性部分给出一个统一有限代数证明，而不是重证全部 C1–C3。
固定全部素数 $p\ge5$、$a\ge2$ 及任意本原 $p^a$ 次根 $\zeta$，同一实际分支、SUM action 及

$$
h=D_1=2-\zeta-\zeta^{-1},\quad \rho=-h,\quad L=\rho\lambda,
\quad m=(p-1)/2,\quad M=p^{a-1}m=v_h(p),\quad \chi=(-1)^{m+1}.
$$

局部域及其整数环为 $K^+=\mathbb Q_p(h)$、$\mathcal O^+=\mathbb Z_p[h]$，赋值规范为 $v_h(h)=1$。

下面证明三个相连但不混同的主张。

**N1：统一阶乘正常形。** 设 $R$ 是交换的、无 $p$ 挠元的 $\mathbb Z_{(p)}$-代数，
$P\in xR[x]$、$\deg_xP<p$、$[x]P=1/2$，且始终只取 $\alpha=1,2$。
对 $0\le r\le2$、$0\le j<p$，有

$$
p^r[x^{rp+j}]e^{\alpha P}\in R,\qquad
p^r[x^{rp+j}]e^{\alpha P}
\equiv\frac{(-\alpha/2)^r}{r!}[x^j]e^{\alpha P}\pmod{pR}.
\tag{N1}
$$

指数首先在 $R[1/p][x]/(x^{3p})$ 中按有限和定义；没有特征 $p$ 的无限指数。
因此 $r=1,2$ 同时给出原两条形式阶乘桥及各自的 $pR$ 误差。

**N2：整块的统一指数正常形。** 定义

$$
\mathfrak F_R=R[x,\eta]/(x^p-p\eta,\eta^3),\qquad
\mathbf E_\alpha(x)=e^{\alpha P}\bmod x^p\in R[x]_{<p}.
\tag{N2a}
$$

对任意 $Y,Z\in R[x]_{<p}$，在 $R[1/p][x]/(x^{3p})$ 中令

$$
V=P+\frac{x^p}{p}Y+\frac{x^{2p}}{p^2}Z.
$$

则 $e^{\alpha V}$ 属于 $\mathfrak F_R$ 的自然像，其模 $p$ 正常形为

$$
\overline{e^{\alpha V}}
=\overline{\mathbf E_\alpha}(x)
\exp_\eta\!\left(\alpha\eta(\bar Y-1/2)+\alpha\eta^2\bar Z\right)
\quad\text{于 }(R/pR)[x,\eta]/(x^p,\eta^3).
\tag{N2}
$$

这里 $\exp_\eta B=1+B+B^2/2$，因为括号中的 $B$ 属于 $(\eta)$。
横线左侧通过所证明的整系数归属定义，不先约化非整指数系数。

**N3：同一实际前缀的非循环应用。** 由已接受的低块与第一内部入口开始，
用同一有限代数闭包归纳证明第一高块整；在第一块及其比较模型完成之后导入原第二 forcing
常数 $2$，跨过 $2p$ 入口，再继续同一单位步归纳，得到第二高块整。这里

$$
V=\sum_{n=1}^{3p-1}V_nx^n,\qquad
Y^{\rm act}=\sum_{j=0}^{p-1}pV_{p+j}x^j,\qquad
Z^{\rm act}=\sum_{j=0}^{p-1}p^2V_{2p+j}x^j.
$$

其指数桥、两条单位模型与原始误差准确为

$$
\begin{aligned}
p[x^{p+j}]e^{\alpha V}
&=\alpha[x^j]e^{\alpha P(h,x)}(Y^{\rm act}-1/2)+pR^{(1)}_{\alpha,j},
&&-1\le j<p,\\
p^2[x^{2p+j}]e^{\alpha V}
&=[x^j]e^{\alpha P(h,x)}
\left\{\alpha Z^{\rm act}+\frac{\alpha^2}{2}(Y^{\rm act}-1/2)^2\right\}
+pR^{(2)}_{\alpha,j},
&&-2\le j<p,
\end{aligned}
\tag{N3a}
$$

其中 $R^{(k)}_{\alpha,j}\in\mathcal O^+[L]$，负下标系数为零，并且

$$
\begin{gathered}
(\mathcal D_1+J)\mathscr Y=J/2,\qquad
(\mathcal D_2+J)\mathscr Z=-K(\mathscr Y-1/2)^2\pmod{x^p},\\
\mathscr Y_0=\mathscr Z_0=0,\qquad
Y^{\rm act}-\mathscr Y(h),\ Z^{\rm act}-\mathscr Z(h)
\in h^{M-m}\mathcal O^+[L][x]/(x^p).
\end{gathered}
\tag{N3b}
$$

模型零常数不改变实际内部模态。N3 不把原始误差提高为 $h^M$，也不从 N1／N2 推出第二 forcing
常数 $2$。相应定义、阶段依赖与证明见下文。

## Status

数学状态：`PROVABLE AS STATED`，指本件精确定义的 N1–N3，作者证明如下，尚未取得本件的非作者检查。
推导状态：`COHERENT AS STATED`。正常形是同一有限指数对象的整系数重表述，不改实际规范或参数量词。

本件确实用一条带指标 $r=0,1,2$ 的阶乘论证及一个有限代数乘法导出两带和四项桥；
这不只是把两份旧 lemma 并排放进同一标题。但这也不证明完整 B1–B4 已有一条“新短证明”：
真实入口、第二 forcing、实际比较及 A06 后半的响应消元仍有原义务，未取得容量或评分结论。

## Invariant Object

组织对象是 $e^{\alpha V}\bmod x^{3p}$ 的全部有限系数，按第 $r$ 个 $p$-块作准确缩放
$p^r[x^{rp+j}]$。$\eta=x^p/p$ 是证明中的除幂坐标，不是实际参数、Chebyshev 的局部变量，
也不是可以独立改变真实传播子的移位。整系数层必须保留 $x^p=p\eta$ 的进位；
只有模 $p$ 后才有 $x^p=0$。

## Assumptions and Notation

1. N1／N2 中 $R$ 的无 $p$ 挠元条件保证 $R\hookrightarrow R[1/p]$。
   实际应用取 $R=\mathcal O^+[L]$，形式应用取 $R=\mathbb Z_{(p)}[[H]][L]$；两者均满足该条件。
   后者是原 $\mathbb Z_{(p)}[L][[H]]$ 中参数次数有统一有限界的子环。
2. 实际低块为 $P(h,x)=\sum_{i=1}^{p-1}V_ix^i$，其形式来源 $P(H,x)$ 由真实 Chebyshev 递推给出。
   使用已接受的 $P_i\in\mathbb Z_{(p)}[[H]][L]$、$P_1=1/2$、$V_i=P_i(h,L)$，以及

   $$
   h^mV_p\in\mathcal O^+[L],\qquad
   \overline{h^mV_p}=\frac{(-1)^m}{2}(2-L^m),\qquad
   Y^{\rm act}_0=pV_p\in h^{M-m}\mathcal O^+[L].
   \tag{A1}
   $$

   此行横线是模 $h$，仅本行及下述入口剩余采用该意义；N1／N2 的横线一直是模 $p$。
3. 原实际递推是

   $$
   d_n(h)V_n=-\frac12[x^{n-1}]e^V-L[x^{n-2}]e^{2V},\qquad d_n=-D_n/h.
   \tag{A2}
   $$

   在 $1\le n<3p<p^a$ 且 $p\nmid n$ 时，$d_n(h)$ 为单位，剩余为 $-n^2$。
   不以单位递推跨过 $p,2p$；它们是真实非共振模态，但不是单位传播子入口。
   第二 forcing 的定义是 $\mathcal B_2=-[x^{2p-1}]e^V-2L[x^{2p-2}]e^{2V}=2d_{2p}V_{2p}$；
   此定义的系数只使用 $V_1,\ldots,V_{2p-1}$。
4. 第二入口只在第一块完成后使用原 A04 Steps 3–7 的已接受端点推导：

   $$
   p\mathcal B_2=2h^{2m}+O(h^{2m+1}),\qquad
   \frac{d_{2p}}{h^{2m}}=-4+O(h),\qquad
   pV_{2p}=-\frac14+O(h).
   \tag{A3}
   $$

   该推导使用第一块桥、其第一模型比较、真实配对／移位和非驻值 action；不使用第二高块。
   下文先给出其所需第一块桥和第一模型比较，再导入 (A3)。不以待证明的 N3 作为 (A3) 的前提。
5. 设 $\mathcal N=x\partial_x$。低块的实际形式传播子为

   $$
   C_0=2,\quad C_1=2-H,\quad C_{n+1}=(2-H)C_n-C_{n-1},\quad
   d_n(H)=(C_n(H)-2)/H.
   $$

   只在 $1\le j<p$ 上定义 $\mathcal D_kx^j=d_{kp+j}(H)x^j$，并在模 $x^p$ 下取

   $$
   J=\frac x2e^P+2Lx^2e^{2P},\qquad K=\frac x4e^P+2Lx^2e^{2P}.
   \tag{A4}
   $$

   两者都无常数项；所需低于 $p$ 次的指数系数整。没有在本件引入辅助幅度 $b$。

## Proof Strategy and Dependency Map

有限代数的自由基与进位 → 一条统一阶乘剩余 → 高块有限指数乘法 → 已知前缀闭包。
实际顺序必须是：低块与 $p$ 入口 → 第一块单位步归纳 → 第一桥／第一模型及其 $h^{M-m}$ 比较
→ 原 A04 端点 (A3) → $2p$ 入口 → 第二块同一单位步归纳 → 完整桥／第二模型及其比较。
这是一个带两个单独入口的前缀归纳，不是把两个非单位入口也当作单位步。

## Proof

### Step 1. 有限阶乘代数、自由基与进位

先将 $\mathfrak F_R$ 写成 $(R[\eta]/(\eta^3))[x]/(x^p-p\eta)$。
关于 $x$ 的关系首一，因此逐次多项式除法给出唯一的 $x$ 次数小于 $p$ 的代表；
再取 $\eta$ 次数小于 $3$ 的代表，得到 $R$-自由基

$$
x^j\eta^r,\qquad 0\le j<p,\quad 0\le r\le2.
\tag{1}
$$

代入 $\eta=x^p/p$ 定义同态

$$
\iota:\mathfrak F_R\longrightarrow R[1/p][x]/(x^{3p}).
\tag{2}
$$

基元映为 $p^{-r}x^{rp+j}$。这些指数各不相同，且 $R\hookrightarrow R[1/p]$，所以该同态单射。
它的像恰是满足 $p^r[x^{rp+j}]F\in R$ 的有限级数。其乘法已包含跨块进位：
若 $j+j'\ge p$，则 $x^{j+j'}\eta^{r+r'}=p x^{j+j'-p}\eta^{r+r'+1}$；
超过 $\eta^2$ 的项为零。因此像是一个环，不只是一个系数模。

对 $F$ 属于此像，模 $p\mathfrak F_R$ 的坐标就是
$\overline{p^r[x^{rp+j}]F}$，并且

$$
\mathfrak F_R/p\mathfrak F_R=(R/pR)[x,\eta]/(x^p,\eta^3).
\tag{3}
$$

即使 $R/pR$ 有幂零元，上述自由基和乘法仍成立。实际 $\mathcal O^+/p\mathcal O^+$ 正属于
不能擅自当作剩余域的情形；本件不把实际 $Y^{\rm act}_0$ 在该商中预先置零。

### Step 2. 单一阶乘计算同时给出两个形式带

对 $0\le r\le2$、$0\le s<p$，有 $rp+s<3p<p^2$，故
$v_p((rp+s)!)=r$。拆出倍数 $p,2p$ 中实际出现的那些因子，得到

$$
\frac{(rp+s)!}{p^r}
=r!\prod_{u=0}^{r-1}\prod_{i=1}^{p-1}(up+i)\prod_{i=1}^{s}(rp+i).
$$

空乘积取 $1$。在 $\mathbb F_p$ 中，非零元按逆元配对，只有 $1,-1$ 自配，
所以 $(p-1)!=-1$。因而统一得到

$$
\frac{p^r}{(rp+s)!}\equiv\frac{(-1)^r}{r!s!}\pmod p.
\tag{4}
$$

固定 $N=rp+j<3p$。$[x^N]e^{\alpha P}$ 只涉及 $k\le N$ 的阶乘，
每个 $v_p(k!)\le r$，所以其乘 $p^r$ 后整。
约化后 $k<rp$ 的项全为零；剩下 $k=rp+s$、$0\le s\le j$。
在 $(R/pR)[x]$ 中，Frobenius 给

$$
\bar P^{rp}\equiv 2^{-pr}x^{rp}\pmod{x^{(r+1)p}}.
\tag{5}
$$

对 $r=0$ 此式只是 $1=1$；对 $r=1,2$，任何选入 $\bar P^p$ 中 $x^{2p}$ 或更高项的乘积，
其次数至少为 $(r+1)p$，故不影响当前块。
由 (4)、(5)，当前缩放系数的剩余为

$$
\frac{(-1)^r}{r!}\left(\overline{\alpha/2}\right)^{pr}
\sum_{s=0}^{j}\frac{\alpha^s}{s!}[x^j]\bar P^s
=\frac{(-\alpha/2)^r}{r!}[x^j]\overline{\mathbf E_\alpha}.
\tag{6}
$$

最后等式只因为固定的 $\alpha/2$ 是 $\mathbb F_p$ 中的标量，
所以 $(\overline{\alpha/2})^{pr}=(\overline{\alpha/2})^r$。
没有用 $L^p=L$、$H^p=H$ 或任意幅度的 Frobenius 固定性。
(6) 证明 N1；Step 1 同时说明

$$
e^{\alpha P}\in\mathfrak F_R,\qquad
\overline{e^{\alpha P}}=\overline{\mathbf E_\alpha}\exp_\eta(-\alpha\eta/2).
\tag{7}
$$

特别对形式环 $R=\mathbb Z_{(p)}[[H]][L]$，N1 的差已经是整元素且属于 $pR$，
因此存在该形式环中的余项 $R_{\alpha,j}^{(r)}$；不是仅在 $H=0$ 的关系。

### Step 3. 一个有限指数乘法给出整个实际桥

在 Step 1 的单射下，高块恰为 $B=\eta Y+\eta^2Z$，且 $B^3=0$。
特征零的有限指数乘法给出

$$
e^{\alpha(P+B)}=e^{\alpha P}e^{\alpha B},\qquad
e^{\alpha B}=1+\alpha\eta Y+\eta^2\left(\alpha Z+\frac{\alpha^2Y^2}{2}\right).
\tag{8}
$$

第一等式可将有限二项式展开按两个幂次重新求和验证；所有总次数至少 $3p$ 的项已为零。
第二因子属于 $\mathfrak F_R$，因为 $2$ 为单位。由 (7)、环闭包及 (8)，整个指数整于
$\mathfrak F_R$。在商 (3) 中将两个 $(\eta)$ 中的指数相乘，得到

$$
\overline{e^{\alpha V}}
=\overline{\mathbf E_\alpha}
\left[1+\alpha\eta(\bar Y-1/2)
+\eta^2\left\{\alpha\bar Z+\frac{\alpha^2}{2}(\bar Y-1/2)^2\right\}\right].
\tag{9}
$$

这证明 N2。原四项中的低阶乘带、旧高块线性、新高块线性、旧高块平方，
现在由同一个整系数乘法产生；未单独预先假设四项各自可约化。
在整系数层，乘法中 $x$ 次数越过 $p$ 的贡献带额外因子 $p$；
它们消失于 (9)，但留在准确桥的 $pR$ 误差里，不是在原指数中删去。

比较 (9) 的 $\eta x^j$、$\eta^2x^j$ 坐标给 N3a 的 $j\ge0$ 部分。
右边的 $[x^j]e^{\alpha P}$ 可替换 $\mathbf E_\alpha$，因为此处 $j<p$。
第一带 $j=-1$ 时，$p[x^{p-1}]e^{\alpha V}\in pR$；第二带 $j=-2,-1$ 时，
Step 1 的第一块整性给 $p^2[x^{2p+j}]e^{\alpha V}\in pR$。
这些范围的右边负下标为零，故全部声明的下标与余项成立。

至此 N2 是对**给定整系数** $Y,Z$ 的通用代数引理；下一步以它作用于已知前缀，
而不把尚未证明整性的完整实际块当作输入。

### Step 4. 第一块：前缀归纳与第一比较模型先完成

令 $R=\mathcal O^+[L]$。第一入口 (A1) 给实际 $Y^{\rm act}_0$ 整。
假设在某个 $p<n<2p$ 之前，所有已求 $pV_i$（$p\le i<n$）整；
把它们置入 $Y$ 的对应系数，尚未求的系数置零，取 $Z=0$。
这是已知实际前缀在 Step 1 的表示，不是修改最终解。
Step 3 给该前缀的指数属于 $\mathfrak F_R$。

若 $r=\lfloor n/p\rfloor$、$N=n-1,n-2$，则 $\lfloor N/p\rfloor\le r$；
像的系数描述给 $p^r[x^N]e^{\alpha V}\in R$。
递推右边只用 $V_i$、$i<n$，故将 (A2) 乘 $p^r$ 后右边整。
当前 $d_n$ 为单位，于是 $p^rV_n$ 整。
这同一个单位步适用于下文第二块；此处先归纳完成全部 $p\le n<2p$。

于是可以对完整第一块使用 N3a 第一式。代入 (A2) 得

$$
d_{p+j}(h)Y^{\rm act}_j+[x^j]J(h)Y^{\rm act}
=\frac12[x^j]J(h)+p\varepsilon_j^{(1)},\quad 1\le j<p,
\tag{10}
$$

其中 $\varepsilon_j^{(1)}\in R$。第一带所需系数低于 $2p$，此式与任何尚未求的第二高块无关。
在形式环定义零常数的 $\mathscr Y$ 满足 N3b 第一模型。
因为 $J_0=0$ 且 $d_{p+j}(0)=-(p+j)^2$ 为 $p$-单位，每个 $j$ 只需求前面系数，
所以形式解存在且唯一。

形式系数具有有限参数次数，且 $H$ 系数的分母均为 $p$-单位；代入 $H=h$ 在完备局部环收敛。
从 (10) 减去模型方程，常数项差属于 $h^{M-m}$，新增 $p\varepsilon_j^{(1)}$ 属于 $h^M$。
逐个 $j$ 只乘整系数、除单位，得到

$$
Y^{\rm act}-\mathscr Y(h)\in h^{M-m}R[x]/(x^p).
\tag{11}
$$

这已经给出原 A04 Steps 1–2 所用的第一块桥和准确比较。
现在才导入 A04 Steps 3–7 的原证明 (A3)：真实移位／配对缺陷、第一响应、非驻值 action
及 $(2-L^m)+L^m=2$ 的合并均保留，不由 (9) 替代。
由 (A3) 得

$$
Z^{\rm act}_0=p^2V_{2p}=p(pV_{2p})\in pR=h^MR.
\tag{12}
$$

本入口的论证在任何第二高块非入口系数出现之前完成，故没有整性循环。

### Step 5. 第二块继续同一个单位步，完整桥随之成立

现在 $Y^{\rm act}$ 完整且整，第二入口 (12) 已知。
对 $2p<n<3p$，将已求的 $p^2V_i$（$2p\le i<n$）置入 $Z$，未知部分置零。
Step 3 对这个已知前缀成立。沿 Step 4 的同一单位步，取 $r=2$，得到 $p^2V_n\in R$。
归纳完成所有 $0\le j<p$ 的 $Z^{\rm act}_j=p^2V_{2p+j}$。
全实际 $V$ 截断至 $3p-1$ 因此属于 $\mathfrak F_R$；N3a 的完整两式现在都可以合法使用。

原入口核算也直接包含于同一正常形：在模 $h$ 下 $Y^{\rm act}_0=Z^{\rm act}_0=0$，
所以 $p^2[x^{2p}]e^V\equiv1/8\pmod h$；而
$p^2[x^{2p-1}]e^{2V}\in pR$。由 $d_{2p+1}\equiv-1\pmod h$，
得到 $p^2V_{2p+1}\equiv1/16\pmod h$。
这是已完成整性后的剩余推论，不是用该剩余倒证整性。

### Step 6. 完整耦合模型与原始比较误差

把 N3a 的第二式分别用于 $\alpha=1,2$ 后代入 (A2)。
线性 $Z^{\rm act}$ 的系数是 $J$，平方的系数是 $K$，因而

$$
d_{2p+j}(h)Z^{\rm act}_j+[x^j]J(h)Z^{\rm act}
=-[x^j]K(h)(Y^{\rm act}-1/2)^2+p\varepsilon_j^{(2)},
\quad 1\le j<p,
\tag{13}
$$

其中 $\varepsilon_j^{(2)}\in R$；$Y^{\rm act}$ 的常数和平方没有被删去。
已定义 $\mathscr Y$ 后，$K(\mathscr Y-1/2)^2$ 为已知整系数驱动；
$d_{2p+j}(0)=-(2p+j)^2$ 为单位，$J_0=0$，故 N3b 的第二模型逐阶存在且唯一。
低块及模型的固定 $x$ 次数只有有限个参数幂，单位对角逆不含 $L$，
因此 $\mathscr Z\in\mathbb Z_{(p)}[[H]][L][x]/(x^p)$，且 $H=h$ 可合法代入。

记 $E=M-m$。平方驱动之差准确为

$$
(Y^{\rm act}-1/2)^2-(\mathscr Y(h)-1/2)^2
=(Y^{\rm act}-\mathscr Y(h))(Y^{\rm act}+\mathscr Y(h)-1)\in h^ER[x]/(x^p).
\tag{14}
$$

第二因子整。由 (12)，第二常数差属于 $h^M\subset h^E$；
从 (13) 减去模型后，逐阶单位比较与 (14) 给

$$
Z^{\rm act}-\mathscr Z(h)\in h^ER[x]/(x^p).
\tag{15}
$$

(11)、(15) 正是 N3b。有限整系数多项式组合之差可逐因子抽出至少一个这样的块差，
所以仍只有 $h^E$ 的共同保证；若具体端点另有 $h^m$ 缺陷，才可获得 $h^{E+m}=h^M$。
N1–N3 的证明完成。$\square$

## Corrections, Boundary Checks and Non-Claims

- **固定首系数不可外推。** 若擅自令 $P=bx/2$，其中 $b$ 是独立参数，第一带在 $j=0$ 的剩余为
  $p[x^p]e^{\alpha bx/2}\equiv-(\alpha b/2)^p$，一般不等于 $-\alpha b/2$。
  因此本件并不把正常形扩到任意幅度 $b$；$P_1=1/2$、$\alpha=1,2$ 始终固定。
- **$p=5$ 边界包含在统一证明中。** 最高所用阶乘是 $(3p-1)!$，$3p<p^2$；
  $r!$ 的最大 $r$ 为 $2$，$s!$ 中 $s<p$，高块指数只除以 $2$。
  $M\ge5m$ 给 $M-m>0$，所以两个入口的正高度及模 $h$ 剩余计算合法。
  没有 $3!$ 或更高高块指数分母，因为三次高块项在特征零已经被 $x^{3p}$ 截断。
- **不能省去第二端点。** 有限代数只在非内部模态处提供单位步；$d_{2p}$ 非单位，
  (A3) 仍由原合法来源证明。本件没有证明第二 forcing 的完整 Newton 图或简单性。
- **原始 $h^{M-m}$ 界确实不能无条件提高。** 第一模型常数为零，而由 (A1)，
  $[L^0](h^mV_p)$ 的剩余为 $(-1)^m\ne0$，故
  $v_h([L^0]Y^{\rm act}_0)=M-m$。
  仅在已证明含额外缺陷的端点上提高误差，不改变块本身的比较精度。
- **本件的近似只有明确同余。** 特征零次数截断、有限代数同态与 (8)、(14) 是恒等式；
  (N1)、(9) 是模 $p$ 命题；(11)、(15) 是实际赋值误差。
  从未把模 $p$ 与模 $h$ 混用，也未约化不存在的特征 $p$ 无限指数。

## Replacement Scope and Retained Obligations

| 原步骤 | 本件实际可提供的替代 | 仍未消除的内容 |
| --- | --- | --- |
| A03 Step 1 与 A06 Step 1 分开的两条形式阶乘带证明 | N1 的单一公式 (4)–(7)，统一处理 $r=0,1,2$、完整形式 $H$ 和 $pR$ 误差 | 固定 $P_1$、有限次数和分母整性必须明确；不是直接定义特征 $p$ 指数 |
| A03 Steps 2–3、A05 Steps 1–2、A06 Step 2 的重复四类展开／逐项整性 | 有限代数闭包 (8)–(9) 与已知前缀的同一单位步；原四项桥由一次指数乘法得出 | 两个真实入口、原第二 forcing 常数 $2$、非单位模态的特殊处理仍保留 |
| A04 Steps 1–2、A06 Step 3 的第一／第二模型比较 | 同一正常形生成两条实际递推，Steps 4、6 给完整单位模型和误差 | 实际常数与模型零常数、平方差分解及 $h^{M-m}$ 比较仍需证明，不能只写正常形结论 |
| A04 Steps 3–7 的第二 forcing；A06 Steps 4–7 的基解、$Q$ 耦合消元和响应 | 不替代；仅准确提供它们的原输入接口 | 真实 Chebyshev 移位、非驻值 action、常数 $2$、二阶传播子差、$-Ky^2$ 与高精度边界全部保留 |

这是一项有完整作者证明的**统一代数接口**。它消除了独立重做两条阶乘带及四类乘法检查的需要，
但没有消除这些事实本身，也没有将 B1–B4 全部压成无需入口／误差证明的一条式子。
是否适合作为当前作者证明替代，仍需针对本件真实变化的非作者检查；
本件不自授接受状态，不称已获得容量所需的“新短证明”，不估页、不评分、不修改原容量 FAIL。

## Sources, Actual Verification and Open Risks

本件以同线程已实际读取的以下作者段落固定输入；它们没有因本轮推导被重审或改写：

- [A03 POST_POLE_BLOCK](PAPER30_TWIST_PRIME_POWER_POST_POLE_BLOCK_PROBE_V1_20260907.md)：81–276，特别 (10a) 与真实入口。
- [A04 SECOND_INTERNAL_FORCING](PAPER30_TWIST_PRIME_POWER_SECOND_INTERNAL_FORCING_PROBE_V1_20260907.md)：85–580，特别 Steps 3–7 的独立第二端点。
- [A05 SECOND_FACTORIAL_BLOCK](PAPER30_TWIST_PRIME_POWER_SECOND_FACTORIAL_BLOCK_PROBE_V1_20260907.md)：83–236，核对非循环入口与四项完整保留。
- [A06 SECOND_FACTORIAL_RESPONSE_BRIDGE](PAPER30_TWIST_PRIME_POWER_SECOND_FACTORIAL_RESPONSE_BRIDGE_PROBE_V1_20260907.md)：6–106、114–597，核对原模型与误差目标。

本轮实际证明检查覆盖有限代数的单射／自由基、跨块进位、统一阶乘公式、固定标量的 Frobenius、
前缀归纳不使用未求系数、$2p$ 入口的阶段位置、全部负下标、$p=5$、形式代入及实际误差。
这属于作者自查，不是非作者检查；没有用素数样本或脚本运行替代任一无限量词证明。
未读取其他代理本轮推导，没有引入第四移位或原第三首层的新结果，没有新科学范围或外部操作。
剩余交付风险是本件尚未经相应非作者核查，而不是原已接受阶段重新变成 OPEN。
