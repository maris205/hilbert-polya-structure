# Paper30：非加性 Hénon 的 Artin–Schreier 覆盖预筛

日期：2026-09-07。范围：有界作者证明预筛；不是论文立项、容量判断、Route 评价或 PDF 验收。

## Claim

设 $K$ 为代数闭域，$\operatorname{char}K=p>0$，
$A=K[x,y]$，$\wp(u)=u^p-u$，

$$
F(x,y)=(P(x)-y,x),\qquad \deg P=d\ge 2.
$$

原问题是：在非加性合同下，若

$$
F^*g-g=\wp(h),\qquad g,h\in A,
$$

是否必有 $g\in\wp(A)+K$？由于 $K$ 代数闭，$\wp(K)=K$，结论也就是 $[g]=0$ 于加法群商

$$
Q=A/\wp(A).
$$

分别检查两种次数合同：

1. $d$ 不是 $p$ 的幂；
2. 更强的 $p\nmid d$。

组合预筛 W 节另外指定的首试是 $p>2$、$P=x^2+c$，其中 $c\in K$ 任意。它不得与上述更宽合同混为一谈。

## Status

**原固定类命题：NOT CURRENTLY JUSTIFIED；在上述两个宽合同下均为 REFUTED。**

- 仅要求 $d$ 不是 $p$ 幂时，任意特征均有显式非加性固定类反例。
- 即使要求 $p\nmid d$，特征 $2$ 仍有显式非加性固定类反例；最小例子是 $P=x^3+x$、$g=xy$。
- W 的精确首试 $p>2$、$P=x^2+c$ 中，**任意** $g\in A$ 的固定类是否全零，本预筛仍为 **OPEN**。

**修正后的可闭合结论：PROVABLE AFTER WEAKENING / EXTRA ASSUMPTION。** 本记录完整分类了 $p\nmid d$ 时所有可由

$$
a xy+A_0(x)+B_0(y)
$$

表示的 $\lambda$-特征类，其中 $\lambda\in\mathbb F_p^*$；精确内容见定理 4。它包含任意次数的分离变量多项式，不等于任意多项式的分类。

**概念纠正：** $F^*[g]=[g]$ 等价于保持已指定 deck 生成元的 $\mathbb Z/p$-torsor 提升；若只要求底层连通覆盖被保持，允许
$F^*[g]=\lambda[g]$，$\lambda\in\mathbb F_p^*$。奇特征的 $\lambda=-1$ 不能忽略。

## Assumptions

- 除单独指出的反例 2 外，定理 4 使用 $p\nmid d$。
- 全文固定 $F(x,y)=(P(x)-y,x)$，不更换耗散参数、不拼接别的动力系统。
- “非加性”指 $P$ 不是只由 $p$ 幂指数项组成的加性多项式；所有反例的最高次数已经排除了加性。
- 所有覆盖、同构和多项式均定义于 $K$；不声称有算术下降。
- $Q$ 自然是 $\mathbb F_p$-向量空间，但一般不是由多项式标量乘法诱导的 $K$-向量空间。后文使用系数参数，不把它们误称为 $K$-线性商结构。

## Notation

- $[g]$：$g\in A$ 的 Artin–Schreier 类。
- $F^*g=g\circ F$。
- $p$-primitive 指数对：$(i,j)\in\mathbb Z_{\ge0}^2\setminus\{(0,0)\}$，且 $p$ 不同时整除 $i,j$。
- $\mathcal R(g)$：去掉常数并按共同 $p$ 因子约化指数对后得到的唯一代表，见引理 1。
- $\lambda$-特征类：$F^*[g]=\lambda[g]$，其中 $\lambda\in\mathbb F_p^*$。
- 本文的稀疏代表集合为

$$
\mathcal W=\{[a xy+A_0(x)+B_0(y)]:a\in K,\ A_0,B_0\in K[t]\}\subset Q.
$$

不假设 $\mathcal W$ 对 $F^*$ 封闭，也不据此推断任意有限维不变子空间的结构。

## Proof Strategy

先用唯一的 Frobenius-reduced 代表证明候选类确实非平凡；再直接验证覆盖的提升恒等式。对 $\mathcal W$ 的分类，找出 $A_0(P(x)-y)$ 最高混合 $y$ 次数的项。它不能从 Frobenius carry 中消失，迫使 $A_0$ 至多线性。剩余问题变成三个单项式系数比较和一个一变量 Artin–Schreier 条件。

这一论证显式处理了所用模板中的 carry；它不提供任意 $g$ 所需的多项式轨道基与 Frobenius 的共同规范形。

## Dependency Map

1. 引理 1 独立给出 $Q$ 的约化代表和非平凡性检验。
2. 命题 2 只依赖代数恒等式及引理 1，反驳“非 $p$ 幂次数足够”。
3. 命题 3 只依赖代数恒等式及引理 1，反驳特征 $2$ 的 $p\nmid d$ 固定类消失。
4. 定理 4 依赖引理 1 和最高混合 $y$ 次数比较；不依赖特征零余上同调、数值观测或未证明的轨道基。
5. 推论 5 从定理 4 及多项式整除得到特征类的显式参数化。
6. 命题 6 直接核对 $\lambda=-1$ 的覆盖提升，并将原问题的 marked/unmarked 两种含义分开。
7. 二次族推论只用定理 4 与三次 Artin–Schreier 多项式的系数比较。

## Proof

### Step 1. 唯一约化代表及其非平凡性

**引理 1（PROVED）。** 每个 $[g]\in Q$ 有唯一的代表

$$
\mathcal R(g)=\sum_{(i,j)\ p\text{-primitive}}b_{ij}x^iy^j,
$$

其中只有有限多个系数非零。具体地，若 $c_{ij}$ 是 $g$ 的系数，则

$$
b_{ij}=\sum_{r\ge0}c_{p^ri,p^rj}^{p^{-r}}.
$$

这里 $K$ 完美保证 $p^r$ 次根唯一；求和只有有限项。

**证明。** 对任一单项式和 $r\ge1$，恒等式

$$
c x^{pi}y^{pj}-c^{1/p}x^iy^j
=\wp(c^{1/p}x^iy^j)
$$

将共同含有 $p$ 因子的指数对降一级。反复处理每个单项式，并用 $\wp(K)=K$ 去掉常数，得到所述代表。

为证明唯一性，设一个不含常数、仅含 $p$-primitive 指数对的非零多项式 $r$ 等于 $u^p-u$。此时 $u$ 非常数。记 $M=\deg u>0$，则 $u^p-u$ 的最高总次数为 $pM$；其该次齐次部分是 $u$ 的最高次齐次部分的 $p$ 次幂，所有指数对均被 $p$ 同时整除，且该齐次部分非零。这与 $r$ 的支撑条件矛盾。因此两个约化代表之差若属于 $\wp(A)$，它们必相等。证毕。

特别地，对任意 $a\ne0$，有

$$
[x-y]\ne0,\qquad [a xy]\ne0.
$$

这些是商中的非平凡类，不是只写出一个看似非恒定但实际属于 $\wp(A)$ 的方程。

### Step 2. 非 $p$ 幂次数仍有固定类：显式 AS 降阶机制

**命题 2（PROVED；宽合同反例）。** 取整数 $m\ge2$ 且 $p\nmid m$，并令

$$
P(t)=t^{pm}-t^m+2t.
$$

则 $d=pm$ 不是 $p$ 幂，$P$ 非加性，而且

$$
g=x-y,\qquad h=x^m
$$

满足 $F^*g-g=\wp(h)$、$[g]\ne0$。

**证明。** 直接展开得到

$$
F^*(x-y)-(x-y)=P(x)-2x=x^{pm}-x^m=\wp(x^m).
$$

引理 1 给出 $[x-y]\ne0$。因为 $m\ge2$ 且 $p\nmid m$，$pm$ 不可能是 $p$ 幂；最高项指数因此也排除了加性。证毕。

更一般地，任何 $P=R^p-R+2t$ 都产生同一个固定类，取 $h=R(x)$ 即可。这里机制是 $P$ 在 Artin–Schreier 意义下降到 $2t$，不要求 $P$ 本身是向量群加性映射。

本反例的次数被 $p$ 整除，故它本身不回答 $p\nmid d$ 合同。

### Step 3. 特征 2 的素于特征次数反例及精确分类

**命题 3（PROVED）。** 设 $p=2$、$\deg P\ge2$。则

$$
F^*[xy]=[xy]
\quad\Longleftrightarrow\quad
P(t)=tR(t)^2-R(t)
\text{ for some }R\in K[t].
$$

此时 $R$ 必非常数，故

$$
d=2\deg R+1\ge3
$$

为奇数。每个这样的 $P$ 都非加性。

**证明。** 在特征 $2$ 中

$$
F^*(xy)-xy=x(P(x)-y)-xy=xP(x).
$$

若 $P=xR^2-R$，取 $h=xR(x)$ 就有

$$
xP=x^2R^2-xR=h^2-h.
$$

反过来，若 $xP(x)=h(x,y)^2-h(x,y)$，则 $h$ 与 $y$ 无关：若 $e=\deg_yh>0$，右端的 $y$ 次数就是 $2e$，不可能等于零。因此可写 $h=H(x)$。代入 $x=0$ 得 $H(0)^2-H(0)=0$，所以 $H(0)\in\mathbb F_2$。将 $H$ 减去这个常数不改变 $\wp(H)$，且得到 $H=xR$。再除以 $x$ 即得公式。

若 $R$ 为常数，则 $\deg P\le1$，与假设矛盾。若 $\deg R=r\ge1$，最高项来自 $xR^2$，故 $d=2r+1\ge3$，为大于 $1$ 的奇数，不能是 $2$ 幂。证毕。

最小具体反例为

$$
p=2,\quad P=x^3+x,\quad g=xy,\quad h=x^2.
$$

对应的连通有限 étale 覆盖及其提升为

$$
z^2-z=xy,\qquad
\widetilde F(x,y,z)=(x^3+x-y,x,z+x^2).
$$

$[xy]\ne0$ 由引理 1 保证；对 $z$ 的方程导数为 $-1\ne0$，所以覆盖确为 étale。提升是多项式同构，因为底图逆映射为
$F^{-1}(x,y)=(y,P(y)-x)$，第三坐标可用减去 $h\circ F^{-1}$ 恢复。

### Step 4. 分离变量加 $xy$ 模板中的完整特征类分类

**定理 4（PROVED；精确弱化结论）。** 设 $p\nmid d$、$d\ge2$，取 $\lambda\in\mathbb F_p^*$。若 $[g]\in\mathcal W$ 且

$$
F^*[g]=\lambda[g],
$$

则其唯一约化代表有形式

$$
g=a xy+b x+c y.
$$

非零特征类存在当且仅当

$$
\lambda=-1,\qquad a\ne0,\qquad c=b,
$$

以及

$$
(a x+b)P(x)+2b x\in\wp(K[x]).                 \tag{1}
$$

换言之，全部非零特征类恰为满足 (1) 的

$$
[a xy+b(x+y)],\qquad a\in K^*,\ b\in K,
$$

且特征值只能是 $-1$。在 $p=2$ 中 $-1=1$，因此这些都是固定类；在奇特征中，这个模板没有非零固定类。

**证明。**

**4.1 先约化代表。** 由引理 1 可将代表写成

$$
g=a xy+A_0(x)+B_0(y),
$$

其中 $A_0,B_0$ 无常数，且每个非零指数均不被 $p$ 整除。对 $\wp$ 的替换不影响特征类等式，因为 $F^*$ 与 $\wp$ 交换，且 $\lambda\in\mathbb F_p$。

**4.2 排除 $\deg A_0\ge2$。** 假设 $n=\deg A_0\ge2$，最高项为 $\alpha t^n$。约化条件给出 $p\nmid n$。在

$$
F^*g-\lambda g
=a xP(x)-(1+\lambda)a xy
 +A_0(P(x)-y)+B_0(x)
 -\lambda A_0(x)-\lambda B_0(y)
$$

中，$A_0(P(x)-y)$ 的最高混合 $y$ 次数为 $n-1$。该次中 $x$ 次数为正的部分是

$$
\alpha n(-1)^{n-1}(P(x)-P(0))y^{n-1}.
$$

记 $\rho\ne0$ 为 $P$ 的最高项系数，则单项式

$$
\alpha n(-1)^{n-1}\rho\,x^d y^{n-1}          \tag{2}
$$

系数非零。这个指数对为 $p$-primitive，因为 $p\nmid d$。它不与外面的 $xy$ 项相同，因为 $d\ge2$。

约化时，能向 (2) 的指数对贡献的其他单项式必须具有指数对
$(p^r d,p^r(n-1))$，$r\ge1$。它们是混合项，其 $y$ 次数严格大于 $n-1$；整个上述差式没有这样的混合项。纯 $x$ 或纯 $y$ 项约化后也不会成为混合项。因此 (2) 在 $\mathcal R(F^*g-\lambda g)$ 中保留，违背该约化式等于零。故 $\deg A_0\le1$，可写 $A_0=bx$。

**4.3 排除 $\deg B_0\ge2$。** 现在 $F^*g$ 的 $y$ 依赖仅有 $-a xy-b y$。若约化后的 $B_0$ 有次数至少 $2$ 的单项式，它在 $-\lambda B_0(y)$ 中保留；其他项都是纯 $x$、$xy$ 或线性 $y$，不可能在约化中消去它。因此 $B_0=cy$。

**4.4 比较余下的三个方向。** 对 $g=a xy+bx+cy$，有

$$
F^*g-\lambda g
=a xP(x)+bP(x)+(c-\lambda b)x
 -(1+\lambda)a xy-(b+\lambda c)y.            \tag{3}
$$

式 (3) 属于 $\wp(A)$ 当且仅当

$$
(1+\lambda)a=0,\qquad b+\lambda c=0,
$$

且其纯 $x$ 部分属于 $\wp(K[x])$。最后一个等价不隐藏多变量原函数：若一个仅依赖 $x$ 的多项式等于 $h^p-h$，则比较 $y$ 次数可知 $h$ 也仅依赖 $x$。

若 $a=0$ 且 $b\ne0$，该纯 $x$ 多项式为

$$
bP(x)-b(\lambda+\lambda^{-1})x.
$$

它的次数为 $d$，最高项指数不被 $p$ 整除，因此不可能属于 $\wp(K[x])$。故 $a=0$ 时必有 $b=c=0$。

于是任何非零特征类均有 $a\ne0$，从而 $\lambda=-1$、$c=b$，并且纯 $x$ 条件正好是 (1)。反过来，这些条件代入 (3) 得到 $F^*g-\lambda g\in\wp(A)$；引理 1 保证 $a\ne0$ 时类非零。证毕。

**直接推论。** 在 $p\nmid d$ 下，任何可由 $A_0(x)+B_0(y)$ 表示的固定类均为零，甚至不存在非零的 $\mathbb F_p^*$ 特征类。这个结论没有对 $A_0,B_0$ 施加次数上界。

### Step 5. 特征类的显式参数化和次数约束

**推论 5（PROVED）。** 定理 4 中的非零特征类可精确参数化如下。选择

$$
a\in K^*,\quad b\in K,\quad H\in K[t],\quad m=\deg H,
$$

要求

$$
H(-b/a)^p-H(-b/a)=-2b^2/a                  \tag{4}
$$

以及 $pm-1\ge2$。定义

$$
P(t)=\frac{H(t)^p-H(t)-2bt}{at+b}.         \tag{5}
$$

则 (5) 是多项式，次数为 $pm-1$，且

$$
F^*[a xy+b(x+y)]=-[a xy+b(x+y)].
$$

反过来，定理 4 中每个非零特征类都来自这样的参数。因此其存在必要求

$$
d\equiv-1\pmod p.
$$

**证明。** 分子在 $t=-b/a$ 处为零恰好等价于 (4)，故可被线性多项式 $at+b$ 整除。如果 $H$ 非常数且 $pm-1\ge2$，分子的最高次数为 $pm$，没有来自 $H$ 或 $2bt$ 的同次消去，除法后次数为 $pm-1$。式 (1) 由定义成立。

反过来，(1) 给出某个 $H$ 使 $(at+b)P+2bt=H^p-H$。由于 $a\ne0$、$\deg P=d\ge2$，左端次数为 $d+1\ge3$，因此 $H$ 非常数，比较次数得到 $d+1=p\deg H$。代入根 $-b/a$ 得 (4)，并恢复 (5)。证毕。

在特征 $2$，取 $a=1,b=0$ 后，$H(0)^2-H(0)=0$；减去 $\mathbb F_2$ 常数并写 $H=tR$，就恢复命题 3。这里不是从奇特征结论强行外推，而是同一个完整系数计算中的 $-1=1$ 分支。

### Step 6. 指定 deck 生成元与底层覆盖不是同一个问题

对非零 $[g]$，考虑连通 $\mathbb Z/p$ 覆盖

$$
X_g=\operatorname{Spec}A[z]/(z^p-z-g).
$$

选定 deck 生成元 $z\mapsto z+1$。若 $F^*g=\lambda g+\wp(h)$，其中 $\lambda\in\mathbb F_p^*$，则

$$
\widetilde F(x,y,z)=(F(x,y),\lambda z+h(x,y))                 \tag{6}
$$

定义覆盖的同构，其逆第三坐标为
$\lambda^{-1}(z-h\circ F^{-1})$。它将 deck 平移参数乘以 $\lambda$；因此保持指定生成元当且仅当 $\lambda=1$。

反过来，任意底层覆盖提升通过共轭给出其 deck 群 $\mathbb F_p$ 的一个自同构，即乘以某个 $\lambda\in\mathbb F_p^*$。于是第三坐标减去 $\lambda z$ 是 deck 不变量，属于 $A$，可写成 $h$。代回覆盖方程便得到 $F^*g=\lambda g+\wp(h)$。

所以两个精确问题是

$$
\begin{array}{ll}
\text{指定 deck 生成元的 torsor 不变：}&F^*[g]=[g],\\[2pt]
\text{底层连通 }\mathbb Z/p\text{ 覆盖不变：}&F^*[g]=\lambda[g]\text{ for some }\lambda\in\mathbb F_p^*.
\end{array}
$$

其中连通性可由 $[g]\ne0$ 判定：若 Artin–Schreier 多项式在 $K(x,y)$ 有根，该根在 $A$ 上整；$A$ 为整闭域环，故根在 $A$。而次数为素数 $p$ 的 Artin–Schreier 多项式若可约即有根。这与引理 1 的非平凡性矛盾。

这一 torsor 背景与 [Stacks Project, Section 59.63, Artin–Schreier sequence](https://stacks.math.columbia.edu/tag/0A3J) 一致；上述提升公式与 deck 共轭计算已在此直接给出。

**命题 6（PROVED；奇特征底层覆盖反例）。** 对任意奇素数 $p$ 和整数 $m\ge2$，令

$$
P(t)=t^{pm-1}-t^{m-1},\qquad g=xy,\qquad h=x^m.
$$

则 $d=pm-1$ 与 $p$ 互素，$P$ 非加性，且

$$
F^*g+g=xP(x)=x^{pm}-x^m=\wp(h).
$$

所以 $[g]\ne0$ 是特征值 $-1$ 的类，不是 $F^*$ 固定类，却给出真正被 $F$ 保持的底层覆盖；提升为

$$
(x,y,z)\longmapsto(P(x)-y,x,-z+x^m).
$$

此外 $F^{2*}[g]=[g]$，其显式原函数为

$$
F^{2*}g-g
=\wp\big((P(x)-y)^m-x^m\big).
$$

证明就是上述恒等式与引理 1。最高次数 $pm-1\ge2$ 不被 $p$ 整除，故不能是 $p$ 幂，排除了加性。

这说明即使今后证明奇特征 $F^*$ 的固定类消失，也不能把结论换写成“所有底层 $\mathbb Z/p$ 覆盖都不变不了”，更不能自动换写成“所有迭代都没有固定类”。

### Step 7. W 的精确二次首试：模板内结论与实际反例边界

现在固定 $p>2$、$P=x^2+c$。

1. 由定理 4，$\mathcal W$ 内的 $F^*$ 固定类全部为零，对所有 $c$ 成立。
2. 若 $p\ge5$，$2\not\equiv-1\pmod p$，故 $\mathcal W$ 内没有任何非零 $\mathbb F_p^*$ 特征类。
3. 若 $p=3$ 且 $c\ne0$，则这个精确二次族已经有底层不变覆盖。

第三点可显式写成：选 $q\in K^*$ 满足

$$
q^2=-1/c,\qquad a=q^3.
$$

令 $g=a xy$、$h=qx$。则

$$
F^*g+g=a x(x^2+c)=q^3x^3-qx=h^3-h.
$$

因此 $z^3-z=a xy$ 是非平凡覆盖，具有提升

$$
(x,y,z)\longmapsto(x^2+c-y,x,-z+qx).
$$

还可完整确定这个二次族在 $\mathcal W$ 内的所有非零特征类。推论 5 强制 $\deg H=1$，写 $H=qx+r$。方程 (1) 成为

$$
(a x+b)(x^2+c)+2b x
=q^3x^3-qx+(r^3-r).
$$

比较 $x^2$ 系数得到 $b=0$，继而 $a=q^3$、$ac=-q$。由于 $a\ne0$，有 $q\ne0$，条件等价于上面的 $q^2=-1/c$。常数项只要求 $r\in\mathbb F_3$。故 $c=0$ 时 $\mathcal W$ 内没有非零特征类；$c\ne0$ 时恰有由这两个非零 $q$ 给出的两条相反非零类，它们生成同一个 $\mathbb F_3$ 直线。

**这些均不解决任意 $g\in K[x,y]$ 的 marked 固定问题。** 二次族在模板之外仍须另行证明或寻找反例。

## Corrections or Missing Assumptions

### 1. 必须拆开的三个命题

| 命题 | 本预筛结论 | 原因 |
|---|---|---|
| 非加性且 $d$ 非 $p$ 幂蕴含 $Q^{F^*}=0$ | REFUTED | 命题 2 的 $[x-y]$ |
| 非加性且 $p\nmid d$ 蕴含 $Q^{F^*}=0$ | REFUTED | 命题 3 的特征 $2$、$[xy]$ |
| $p>2$、$P=x^2+c$ 蕴含 $Q^{F^*}=0$ | OPEN | 本文只完成 $\mathcal W$ 内分类 |
| $p\nmid d$ 蕴含无底层不变 $\mathbb Z/p$ 覆盖 | REFUTED | 命题 6；甚至二次 $p=3,c\ne0$ 已失败 |

### 2. 不能使用的替代论证

- $A^{F^*}=K$ 即使另有证明，也没有计算 $Q^{F^*}$。
- 普通多项式余边界 $F^*u-u$ 的分类不等于 $\wp$ 商中的固定类分类。
- 仅观察 $\deg(F^*g)$ 增长不够；$\wp$ 约化会把共同 $p$ 因子的指数同时除以 $p$。
- 本文的最高混合项证明依赖代表形状 $a xy+A_0(x)+B_0(y)$。任意混合多项式可以有更高 $y$ 次数的 Frobenius 祖先；不能套用 Step 4.2 的“没有祖先”结论。
- $F^*$ 没有特征值 $1$，不排除特征值 $-1$，也不排除某个迭代的特征值 $1$。

### 3. 可精确接续的 OPEN

对固定 $p>2$、$P=x^2+c$，建立或否定以下声明：

$$
\mathcal R(F^*g)=g,\qquad g=\mathcal R(g)
\quad\Longrightarrow\quad g=0
\qquad (g\in K[x,y]).
$$

缺失的是**任意混合支撑**的最高项/轨道规范形：必须证明候选最高混合项没有其他 Frobenius 祖先消去，或者完整计入那些祖先后仍存在严格单调量。本文没有此引理，不声称存在全局 Frobenius-height 增长定理。

## 有界一手查新

按 research-lit 技能仅做公开 web 来源核对，未下载论文、未扫描历史构建树。此次共使用六个搜索查询，依次为：

1. `"Hénon" "Artin-Schreier"`
2. `"Henon" "étale" "positive characteristic"`
3. `site:arxiv.org polynomial automorphism finite etale cover positive characteristic Henon`
4. `"Hénon" "Artin" cover characteristic`
5. `"Artin-Schreier" "polynomial automorphisms"`
6. `"Hénon" "positive characteristic" covers`

搜索查询外只打开或定位所得一手页面及 Stacks 的精确基础条目；没有追加关键词查询。

| 来源 | 实际核对内容 | 对本题覆盖范围 |
|---|---|---|
| [Stacks Project, Section 59.63](https://stacks.math.columbia.edu/tag/0A3J) | Artin–Schreier 正合列与仿射背景 | 支持 $\wp$ 商解释；不分类 Hénon 固定类 |
| [Kiran S. Kedlaya, *On the geometry of p-typical covers in characteristic p*，2005 arXiv 原稿](https://arxiv.org/html/math/0501541) | $p$-typical 覆盖、AS 塔以及仿射环面型空间上的分解与高度框架 | 相关上位理论；此次核对未找到本文精确 Hénon 不变式或覆盖分类的直接定理 |

有限检索没有找到直接覆盖本记录精确分类的一手定理，**不等于证明新颖性**。当前只确认计算和证明内容；命题 2、3、6 与定理 4 是否已有明确先例，仍需独立查新。没有给出论文容量判断，也没有因搜索未命中而立项。

## Open Risks

- 二次奇特征首试的任意多项式固定类问题仍 OPEN。
- 未分类模板 $\mathcal W$ 外的特征类、广义特征向量或有限轨道类。
- 未分类一般有限 étale 覆盖、非循环 $p$ 群覆盖或 Artin–Schreier–Witt 覆盖。
- 非平凡性、étale 性、显式提升和模板内分类均有正文证明；它们不授予 Route PASS 或论文验收状态。
- 本文件是作者侧证明预筛。奇特征反特征类与 marked/unmarked 区分由主控并行指出并在此核对；全文尚未经过独立终审。

## 最终核验记录

- 对象和量词：保留原 $F$、$\wp$、$p\nmid d$ 及 W 的 $d=2,p>2$ 首试分支。
- 反例：均通过写出的精确恒等式验证；非平凡性由唯一约化代表证明。
- 模板分类：对 Frobenius 祖先的排除只用于 Step 4.2 明确允许的支撑，不外推。
- 边界：$p=2$ 的 $-1=1$、奇特征的 deck 反转、$F^2$ 固定、二次 $p=3$ 全部单独处理。
- 未运行数值或随机程序；未创建论文项目，未修改旧稿、索引、锁、账本或失败产物。
- 本地新增文件仅为本记录。其 SHA-256 由交付消息给出，避免自哈希字段。
