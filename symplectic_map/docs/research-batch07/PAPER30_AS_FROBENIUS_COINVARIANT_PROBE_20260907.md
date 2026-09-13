# Paper30：Artin–Schreier 特征类与 Frobenius coinvariant 有界预筛

日期：2026-09-07。范围：纯数学作者侧有界 probe；不是独立审查、正式候选、Route 评价、稿件或数值实验。仅新增本记录，不修改旧稿。

## Claim

固定代数闭域 $K$，$\operatorname{char}K=p>2$，并令

$$
A=K[x,y],\qquad F(x,y)=(x^2+c-y,x),\qquad \sigma=F^*,\qquad c\in K,
$$

$$
\lambda\in\mathbb F_p^*,\qquad L=\sigma-\lambda,\qquad
\wp(u)=u^p-u,\qquad Q=A/\wp(A).
$$

本轮目标是全部多项式、全部 mixed 支撑的 $Q^{\sigma=\lambda}$，不是旧记录中的稀疏模板 $\mathcal W$。检验以下桥接并尝试分类右侧：

$$
Q^{\sigma=\lambda}\ \simeq\
\ker(\phi-1:\overline C_\lambda\longrightarrow\overline C_\lambda),
\qquad
\overline C_\lambda=A/(LA+K),\qquad \phi\langle h\rangle=\langle h^p\rangle.
\tag{1}
$$

这里 $\langle\cdot\rangle$ 指 coinvariant 类，$[\cdot]$ 指 Artin–Schreier 类，不混用。

## Status

- 桥接同构 (1)：**PROVABLE AS STATED / PROVED**。
- 特征 $p$ 的二进制 orbit basis 与 twisted orbit obstruction：本记录重新证明其适用性，不直接援引 Paper29 的特征零定理。
- 全 mixed Frobenius 固定元的“最高轨道次数只能为奇反射 word”必要条件：**PROVED**，见命题 3。
- 特例 $p=3,c=0,\lambda=-1$ 的完整 Frobenius **核**：**PROVED**，恰为 $K\langle x\rangle$，见命题 4。这里是一个 $K$-线性直线，不是 $K[x]$，也不是 Frobenius 固定空间。
- $p\ge5$ 的全部 mixed 特征类，以及 $p=3,c=0$ 的全部 mixed 特征类：**NOT CURRENTLY JUSTIFIED / OPEN**。上述核分类不解决固定空间。
- 已有 $p=3,c\ne0,\lambda=-1$ 非零类保留；本轮没有证明它们穷尽全部 mixed 类。

## Assumptions

- $K$ 代数闭，特别是完美，且 $\wp(K)=K$。
- $\lambda\in\mathbb F_p^*$；这是 $L\wp=\wp L$ 和 Frobenius 在 twisted coinvariant 上下降的必要条件。
- 不更换二次 Hénon 族，不改变 $c$ 的量词，不由单项式计算外推全 mixed 不消去。
- 只做证明推导；未运行数值、有限次数枚举或实验，未新增网页检索。

## Notation

定义轨道坐标

$$
X_0=x,\quad X_{-1}=y,\quad
X_i^2=X_{i-1}+X_{i+1}-c\quad(i\in\mathbb Z).
$$

有限二进制 word $e=(e_i)$ 满足 $e_i\in\{0,1\}$；对应 $M_e=\prod_iX_i^{e_i}$。非空 word 的平移轨道记为 $O$。

对于 word，令

$$
a(e)=\sum_{i\ge0}e_i2^i,\qquad
b(e)=\sum_{i\le-1}e_i2^{-i-1},\qquad
\mu(e)=a(e)+b(e).
$$

每个有序非负整数对 $(a,b)$ 唯一指定一个 word。设

$$
d(O)=\min_{r\in\mathbb Z}\mu(\sigma^re),\qquad
\delta(v)=\max_{v_O\ne0}d(O)\quad(0\ne v\in\overline C_\lambda).
$$

轨道系数的非零性不依赖选哪个平移代表；因此 $\delta$ 定义良好。

## Proof Strategy

先从降因子次数的重写系统重建任意特征的轨道基；再在每个无限移位轨道上计算 twisted obstruction。利用常数 Artin–Schreier 满射构造并证明 (1)。最后以最小普通次数代表分析 Frobenius 的最高项，严格排除 strong-balanced 顶层支撑，并另外用多项式微分形式分类一个完整 Frobenius 核。

## Dependency Map

1. 任意特征 orbit basis：只用重写降次数、不同纯平方因子的互素性及递推给出的代数同构。
2. Twisted obstruction、$Ls\in K\Rightarrow s\in K$：只用上述基及非空 word 的无限移位轨道。
3. 桥接 (1)：依赖第 2 项、$L\wp=\wp L$、$\ker\wp=\mathbb F_p$ 和 $\wp(K)=K$。
4. 最高 obstruction 必要条件：依赖普通最高项的二进制编码、轨道次数凸性和 $p$ 倍指数对的轨道分离。
5. $p=3,c=0,\lambda=-1$ 的核分类：依赖多项式不变量只有常数、显式 Wronskian 及 $\ker d=A^3$；不依赖第 4 项。

## Proof

### Step 1. 特征 $p$ 的轨道基与 twisted obstruction

**引理 1（PROVED）。** $\{M_e\}$ 是 $A$ 的 $K$-基，且 $\sigma M_e$ 是 word 平移一格。每条非空轨道都是无限轨道。特别地，若 $Ls\in K$，则 $s\in K$。

**证明。** 在无限变量多项式环中使用规则

$$
Z_i^2\ \longrightarrow\ Z_{i-1}+Z_{i+1}-c.
$$

一次替换将被替换单项式的总因子次数至少降一，故从任一有限多项式开始，所有分支均有限。不同位置的首项 $Z_i^2,Z_j^2$ 互素；同时可约的单项式 $M$，先后在两处替换都到达

$$
\frac{M}{Z_i^2Z_j^2}
(Z_{i-1}+Z_{i+1}-c)(Z_{j-1}+Z_{j+1}-c).
$$

即使 $i,j$ 相邻，原来的另一个平方因子仍可被选中替换。对因子次数归纳得到完全约化唯一。线性延拓的 normal form 消去关系理想，并固定每个二进制单项式，故它们在商中既张成又线性无关。

递推分别向左右表达全部 $Z_i$，使该商与 $K[Z_0,Z_{-1}]$ 互为显式逆同构。代入 $Z_i\mapsto X_i$ 给出所称基。$\sigma X_i=X_{i+1}$ 由两个相邻初值和递推确定。非空有限支撑不可能在非零平移下保持不变，因此轨道无限。

展开 $s$ 的某个非空轨道部分为 $\sum_ru_r\sigma^rM_O$。$Ls\in K$ 强制

$$
u_{r-1}-\lambda u_r=0\quad(r\in\mathbb Z).
$$

有限支撑和 $\lambda\ne0$ 迫使所有 $u_r=0$，故 $s$ 只有常数项。全过程没有除以正整数或使用特征零。证毕。

更具体地，若 $h$ 在该轨道上的系数为 $c_r$，其 twisted obstruction 是

$$
\ell_{O,\lambda}(h)=\sum_r\lambda^r c_r.
\tag{2}
$$

它在 $LA$ 上为零。反过来，若 (2) 为零，则

$$
u_r=-\lambda^{-r-1}\sum_{s\le r}\lambda^s c_s
$$

有有限支撑，满足 $u_{r-1}-\lambda u_r=c_r$。故 $\overline C_\lambda$ 恰有每个非空轨道的一条 $K$-基方向，且

$$
\langle\sigma^rM_O\rangle=\lambda^r\langle M_O\rangle.
\tag{3}
$$

当 $\lambda=1$ 时额外商去 $K$ 是重要的；当 $\lambda\ne1$ 时 $K\subset LA$，同一记号仍适用。

### Step 2. 全 mixed Artin–Schreier–Frobenius 桥

**定理 2（PROVED）。** (1) 是自然的 $\mathbb F_p$-线性同构。$\phi$ 是 $p$-半线性的加法映射，不是一般的 $K$-线性映射。

**证明。** 首先

$$
(Lu+k)^p=L(u^p)+k^p
$$

因为 $\lambda^p=\lambda$，故 $\phi$ 在商上定义良好，并满足 $\phi(av)=a^p\phi(v)$。

对 $[g]\in Q^{\sigma=\lambda}$，选 $h\in A$ 使

$$
Lg=\wp(h),
$$

定义 $\Psi[g]=\langle h\rangle$。该像满足 $\phi\langle h\rangle=\langle h\rangle$。若换一个 $h$，差属于 $\ker\wp=\mathbb F_p\subset K$，故像不变。若换代表 $g'=g+\wp(u)$，则可以取 $h'=h+Lu$，因为 $L\wp(u)=\wp(Lu)$；故像仍不变。加法及 $\mathbb F_p$ 数乘相容。

若 $\Psi[g]=0$，写 $h=Lu+a$，其中 $a\in K$。于是

$$
L\bigl(g-\wp(u)\bigr)=\wp(a)\in K.
$$

引理 1 给出 $g-\wp(u)\in K$，而 $K=\wp(K)$，所以 $[g]=0$。这同时处理 $\lambda=1$，没有遗漏“差为非零常数”的情况。

反过来，设 $\langle h\rangle$ 为 $\phi$ 固定元，写

$$
\wp(h)=Lg+a\qquad(a\in K).
$$

选 $b\in K$ 满足 $\wp(b)=-a$，则 $\wp(h+b)=Lg$。因此 $[g]\in Q^{\sigma=\lambda}$，且 $\Psi[g]=\langle h+b\rangle=\langle h\rangle$。单射和满射均证毕。

### Step 3. 对全 mixed 顶层支撑有效的不消去引理

轨道 word 的最高普通齐次项为 $x^{a(e)}y^{b(e)}$。这是由 $X_i$ 在正射线的最高项 $x^{2^i}$、负射线的最高项 $y^{2^{-i-1}}$ 逐项相乘得到的。二进制编码唯一，所以不同 word 不会消去最高普通齐次项。

若 $\epsilon=a\bmod2$、$\eta=b\bmod2$，平移一格的指数对为

$$
T_+(a,b)=(2a+\eta,(b-\eta)/2),\quad
T_-(a,b)=((a-\epsilon)/2,2b+\epsilon).
\tag{4}
$$

一个 word 的移位次数序列是若干 $\ldots,4,2,1,1,2,4,\ldots$ 序列的平移之和，故离散凸。由 (4)，该位置为全局最小值当且仅当

$$
2a\ge b-\eta,\qquad 2b\ge a-\epsilon.
\tag{5}
$$

称一对最小代表指数 **strong-balanced**，如果进一步满足

$$
2a\ge b,\qquad 2b\ge a.
\tag{6}
$$

**命题 3（PROVED）。** 在 $\overline C_\lambda$ 的每个非零轨道方向选一个最小普通次数代表。若 $0\ne v$ 的最高轨道次数为 $D=\delta(v)$，且至少一个次数 $D$ 的支撑轨道满足 (6)，则

$$
\delta(\phi v)=pD>D.
\tag{7}
$$

因此非零 $\phi$ 固定元的最高支撑，只能是

$$
(a,b)=(n,2n+1)\ \text{或}\ (2n+1,n),\qquad D=3n+1.
\tag{8}
$$

两个 (8) 代表属于同一轨道；每个给定的 $D$ 至多有这一条例外轨道。其 word 是一个中心 $1$ 加左右反射成对的相同二进制位。

**证明。** 令 $h$ 为上述最小代表的有限线性组合，则 $\deg h=D$。在特征 $p$ 下 $h^p$ 的次数为 $pD$。一个顶层 source $(a,b)$ 的唯一最高 normal-form word 对应 $(pa,pb)$，系数是 source 系数的 $p$ 次幂；它的其他 normal-form 项次数严格小于 $pD$。

若 (6) 成立，$(pa,pb)$ 仍满足 (6)，所以其轨道最小次数恰为 $pD$。因此所有次数严格小于 $pD$ 的项都不能属于该轨道。

还须排除另一个顶层 source 的最高 word 撞入同一轨道。设两个 $p$ 倍指数对相差向右平移 $r\ge0$ 格。平移公式为

$$
(pa,pb)\longmapsto
(2^rpa+t,(pb-t)/2^r),\qquad t=pb\bmod2^r.
$$

若所得两个分量也都被 $p$ 整除，则 $t=pu$，其中 $0\le u<2^r$，且 $b-u$ 被 $2^r$ 整除。因此 $u=b\bmod2^r$，除以 $p$ 后的原始指数对本身也相差这 $r$ 格平移。这说明两个 source 本来属于同一轨道，违背每轨道只选一个代表。若平移方向为左，交换两个指数对后使用同一论证。

所以目标轨道的 obstruction 只有一个非零顶层贡献，不会消去。另一方面 $h^p$ 的每个 word 都有普通次数至多 $pD$，故其轨道最小次数也至多 $pD$，证明 (7)。

若最小代表满足 (5) 却不满足 (6)，整数性迫使 $b=2a+1$ 或 $a=2b+1$。在第一种情形，$b$ 的最低位为 $1$，其余位恰为 $a$ 的各位；这给出以 $-1$ 为中心的反射 word。平移一次得到第二种情形。因为 $D=a+b$，得 $D=3n+1$；二进制编码唯一给出每个 $D$ 的唯一例外轨道。证毕。

**边界。** 命题 3 不是所有非零元上的严格增长定理。它没有计算 (8) 的 Frobenius normal form 在同一轨道内的全部加权和。即使从一个 source 看见更高 word，仍可能有其较低普通次数平移伙伴带来消去。

### Step 4. Single-letter 计算与不能跳过的消去

记 $u=\langle X_0\rangle$、$E=\langle X_0X_1\rangle$。在 $p=3$ 中直接重写得

$$
\phi(u)=(1+\lambda^{-1})E-cu.
\tag{9}
$$

当 $\lambda=-1$ 时 $Ku$ 对 $\phi$ 稳定，$\phi(au)=-ca^3u$。该直线的固定元满足 $-ca^3=a$；$c=0$ 时只有零，$c\ne0$ 时恰为零和两个相反非零元。

式 (1) 将非零 $au$ 对应到 $[a^3xy]$：条件 $ca^3=-a$ 给出

$$
(\sigma+1)(a^3xy)=a^3x^3+ca^3x=(ax)^3-ax.
$$

这是旧记录的已知反例，在这里由桥接恢复，不是新的全 mixed 分类。

在 $p=5$ 中，另记 $D_2=\langle X_0X_2\rangle$、$T=\langle X_0X_1X_2\rangle$。由 $X_0^5=X_0(X_{-1}+X_1-c)^2$ 得

$$
\begin{aligned}
\phi(u)={}&(1+\lambda^{-2})D_2+2\lambda^{-1}T
-2c(1+\lambda^{-1})E\\
&+(c^2-2c+2\lambda+2\lambda^{-1})u.
\end{aligned}
\tag{10}
$$

三个非空 word 轨道 $D_2,T,E$ 两两不同。$2\lambda^{-1}\ne0$，所以 single-letter 直线上没有非零固定元；这不排除更高 mixed source 共同抵消 (10) 的高层方向。

### Step 5. 一个完整 Frobenius 核，而不是固定空间

**命题 4（PROVED）。** 若 $p=3,c=0,\lambda=-1$，则

$$
\ker(\phi:\overline C_{-1}\to\overline C_{-1})=K\langle x\rangle.
\tag{11}
$$

**证明。** 先分类满足 $\sigma^*\alpha=-\alpha$ 的多项式 $1$-形式。写 $\alpha=a\,dx+b\,dy$。由于在特征 $3$ 中 $d(x^2-y)=-x\,dx-dy$，系数比较给出

$$
b=\sigma a,\qquad \sigma^2a=x\sigma a-a.
\tag{12}
$$

设 $W=ax-y\sigma a$。使用 $\sigma x=x^2-y$、$\sigma y=x$ 和 (12)，直接计算

$$
\sigma W=(\sigma a)(x^2-y)-x(x\sigma a-a)=W.
$$

引理 1 使 $W$ 为常数。代入 $y=0$ 得 $a(x,0)x=W$；再代 $x=0$ 得 $W=0$，故 $y\mid a$。写 $a=yq$，则 $W=xy(q-\sigma q)=0$ 使 $\sigma q=q$，所以 $q\in K$。由 (12)，全部这些形式正好为

$$
\alpha=q\,d(xy),\qquad q\in K.
\tag{13}
$$

现设 $\phi\langle h\rangle=0$，即 $h^3=(\sigma+1)g+k$，其中 $k\in K$。取微分得到 $\sigma^*(dg)=-dg$，所以 (13) 给出 $d(g-qxy)=0$。在完美域的特征 $3$ 多项式环中，两偏导均为零等价于所有指数均被 $3$ 整除，故 $g=qxy+v^3$，某个 $v\in A$。

用 $(\sigma+1)(xy)=x^3$ 得

$$
h^3=q x^3+(\sigma v+v)^3+k.
$$

取唯一三次根得

$$
h=q^{1/3}x+(\sigma+1)v+k^{1/3}.
$$

因此 $\langle h\rangle\in K\langle x\rangle$。反向包含由 $x^3=(\sigma+1)(xy)$ 给出。$\langle x\rangle\ne0$ 由 twisted orbit basis 保证，故 (11) 是恰一条直线。证毕。

该直线上 $\phi=0$，所以它与 $\ker(\phi-1)$ 的交只有零。一个非零核的完整分类，不蕴含另一个不同方程 $\phi v=v$ 的完整分类。

## Corrections or Missing Assumptions

1. Paper29 原定理在特征零表述；本轮只取其显式重写思路，并在 Step 1、3 重新检查实际使用的任意特征步骤。没有将特征零结论整包移用。
2. $\overline C_\lambda$ 是 $K$-向量空间，$\phi$ 是 $p$-半线性；$Q$ 及 (1) 中的固定空间只声称 $\mathbb F_p$-线性。半线性核 (11) 是 $K$-线性子空间，但半线性固定空间一般不是。
3. 对全 mixed 分类仍缺：计算所有奇反射例外 word 的 Frobenius 顶层加权 orbit obstruction，并证明至少一个高于原轨道次数的方向不能被同一 source 的平移项和其他层抵消；或给出所有例外闭合块的完整替代分类。
4. 命题 3 只将可能的最高轨道缩小为每个次数的一条例外轨道；$D=3n+1$ 有无限多个，不能据此声称已有有限维例外子空间。
5. 没有证明 $p=3,c=0,\lambda=-1$ 的商去核后 Frobenius 严格增长，也没有由 (11) 推出固定空间为零。

## Open Risks

- $Q^{\sigma=\lambda}$ 的全 mixed 分类仍 OPEN；特别是 $p\ge5$ 和 $p=3,c=0$ 两个目标没有闭合。
- $p=3,c\ne0,\lambda=-1$ 的已知直线是否穷尽全部特征类仍 OPEN。
- 命题 3 是最高支撑必要条件，不是充分条件、统一次数上界或有限异常块分类。
- 本文件是作者侧有界证明记录；一个并行作者子 probe 独立核对了桥接并提出 Step 5 的 Wronskian 论证，主作者逐项重算后写入。这不授予独立终审或候选通过状态。

## 最终核验记录

- 完整读取指定旧 AS probe；读取 Paper29 轨道代数和普通 orbit obstruction 的证明上下文。
- 对桥接逐项核对代表选择、$\lambda=1$ 常数、单射、满射和半线性。
- 对顶层 lemma 显式处理不同 source 以及同一 target orbit 的平移碰撞；只在最小次数为 $pD$ 的 strong-balanced 情形排除所有低次项。
- 对核分类核对拉回微分符号、特征 $3$ 的 $2=-1$、Wronskian 恒等式、$y$ 整除以及多项式三次根。
- 没有数值、有限次数实验、额外文献检索、评分或稿件写作；没有修改旧记录。
