# Paper30：奇素数例外 word 的双权重不消去证明

日期：2026-09-07。范围：有界纯数学作者探查；不是独立审稿、正式候选、Route 评价、实验或稿件。只新增本文件，不改动旧作者记录、旧审查或旧处置。

## Claim

固定代数闭域 $K$，$\operatorname{char}K=p\ge5$ 为素数，令

$$
A=K[x,y],\qquad F(x,y)=(x^2+c-y,x),\qquad \sigma=F^*,\qquad c\in K,
$$

$$
\lambda\in\mathbb F_p^*,\qquad
\overline C_\lambda=A/((\sigma-\lambda)A+K),\qquad
\phi\langle h\rangle=\langle h^p\rangle.
$$

本文件证明全部有限多项式支撑上的结论

$$
\ker(\phi-1:\overline C_\lambda\longrightarrow\overline C_\lambda)=0.
\tag{1}
$$

结合既有 Artin–Schreier 桥接，这等价于

$$
\bigl(A/\{u^p-u:u\in A\}\bigr)^{\sigma=\lambda}=0.
\tag{2}
$$

这不是只对单项式、稀疏模板或预先有界次数作出的结论。

另证一个适用于全部 $p>2$ 的中间结论：任何 $\phi$ 固定元均属于单字轨道直线 $K\langle x\rangle$。本文件不另行处理 $p=3$ 在该直线上的分类。

## Status

**PROVABLE AS STATED / AUTHOR PROOF COMPLETE。**

本结论在本文件中是作者侧新证明，尚未因写入文件而获得独立审查、正式立项或论文验收状态。原主张的量词未缩小；没有附加 $c$ 或 $\lambda$ 的限制。

## Assumptions

- 上述 $K,p,c,\lambda$ 固定；$\lambda\ne0$ 且 $\lambda^p=\lambda$。
- 使用 [既有 Frobenius 记录](PAPER30_AS_FROBENIUS_COINVARIANT_PROBE_20260907.md) 中已建立的轨道基、twisted obstruction 和桥接。
- 最高支撑的 strong-balanced 结论使用其修复后的证明：只用普通次数沿平移轨道的严格离散凸性，故同轨道的最小次数代表至多相邻两个；相邻的两个 $p$ 整除指数对经除以 $p$ 后仍是相邻来源。旧稿中未经位反转修正的任意 $r$ 步移位公式不作为本文件前提。该局部表达缺陷及修复由主控保留为[定向勘误](PAPER30_AS_SHIFT_FORMULA_ERRATUM_20260907.md)；本文件也在下文说明实际需要的版本。
- 不使用数值、有限次数枚举、有限素数检查或新文献检索。下述二项式系数与整数不等式对所有指定参数同时成立。

## Notation

沿用轨道坐标

$$
X_0=x,\quad X_{-1}=y,\quad X_i^2=X_{i-1}+X_{i+1}-c,
\qquad \sigma X_i=X_{i+1}.
$$

对有限二进制 word $e=(e_i)$，设

$$
M_e=\prod_iX_i^{e_i},\quad
a(e)=\sum_{i\ge0}e_i2^i,\quad
b(e)=\sum_{i\le-1}e_i2^{-i-1}.
$$

记对应唯一 word 为 $M(a,b)$，并记 $\mu(a,b)=a+b$。它的最高普通齐次项为 $x^ay^b$，系数为 $1$；其余单项式的普通次数严格小于 $a+b$。$\operatorname{NF}$ 表示唯一二进制 word 展开。称指数对 strong-balanced，是指同时满足 $2a\ge b$、$2b\ge a$。

对非空轨道 $O$，以 $v_O$ 表示选定轨道基下的系数，记

$$
d(O)=\min_r\{a(\sigma^re)+b(\sigma^re)\},\qquad
\delta(v)=\max_{v_O\ne0}d(O).
$$

对多项式定义两种加权次数

$$
\deg_V(x)=1,\quad\deg_V(y)=2,\qquad
\deg_U(x)=2,\quad\deg_U(y)=1,
$$

并把常数权重取为 $0$。对于 word 指数对写

$$
V(a,b)=a+2b,\qquad U(a,b)=2a+b.
$$

## Proof Strategy

先证明普通次数三角的 word 展开同时保持两种权重上界。对无限例外族 $(n,2n+1)$、$n\ge1$，其 Frobenius 最高目标轨道只有两个可能出现在普通次数上界内的代表；低次代表违反 $U$ 权重上界，因此目标轨道系数不消去。这样所有固定元被压到单字直线。

最后对 $x^p$ 使用 $V$ 的最高权重部分，显式选出一个二项式系数非零、且在其平移轨道上唯一达到最小 $V$ 权重的 word。任何 $p\ge5$ 都有这样的 word，故单字也不能产生固定元。

## Dependency Map

1. 双权重保持引理只依赖轨道坐标递推与普通次数三角展开。
2. $n\ge1$ 的不消去依赖第 1 项、一次平移公式与普通次数严格离散凸性。
3. 全部固定元压到 $K\langle x\rangle$ 依赖第 2 项及修复后的既有 strong-balanced 最高支撑引理。
4. 任意 $p\ge5$ 的单字排除依赖第 1 项、$V$-最高权重展开、严格凸性与 $\binom m j\not\equiv0\pmod p$。
5. Artin–Schreier 结论只另用既有全 mixed 桥接，不重新构造或假定稀疏代表。

## Proof

### Step 1. 三角展开同时保持双权重

**引理 1。** 若 $\alpha,\beta$ 是非负整数，且 $M(a,b)$ 在 $\operatorname{NF}(x^\alpha y^\beta)$ 中的系数非零，则

$$
a+b\le\alpha+\beta,\qquad V(a,b)\le V(\alpha,\beta),\qquad U(a,b)\le U(\alpha,\beta).
\tag{3}
$$

**证明。** 对递推向正、负两个方向归纳，得到

$$
\begin{array}{lll}
i\ge0:&\deg_VX_i\le2^i,&\deg_UX_i\le2^{i+1},\\
i\le-1:&\deg_VX_i\le2^{-i},&\deg_UX_i\le2^{-i-1}.
\end{array}
$$

初值 $X_0=x,X_{-1}=y$ 满足这些界；相邻的 $X_1=x^2-y+c$ 与 $X_{-2}=y^2-x+c$ 也满足。随后每一步 $X_{i+1}=X_i^2-X_{i-1}+c$ 或其向左版本，把当前上界加倍，而被减项与常数不超过该界。因此 $M(a,b)$ 的每个普通单项式同时满足普通次数至多 $a+b$、$V$ 权重至多 $a+2b$、$U$ 权重至多 $2a+b$。

现在对普通次数归纳，展开一个普通单项式 $x^\alpha y^\beta$。减去 $M(\alpha,\beta)$ 后，余项的普通次数严格下降，且两个权重上界均保持。对每个余项 $x^ay^b$ 再减去其 monic word $M(a,b)$ 时，产生的所有项仍不超过该余项本身的两种权重，因而不超过原上界。普通次数严格下降使过程有限，并给出唯一的 $\operatorname{NF}$，证明 (3)。此证明不要求给加权次数指定全序，也没有假定加权最高单项式唯一。证毕。

### Step 2. 所有 $n\ge1$ 的例外顶层均严格增长

**引理 2。** 允许任意奇素数 $p>2$。设 $0\ne v\in\overline C_\lambda$ 的唯一最高支撑轨道为例外轨道

$$
(a,b)=(n,2n+1),\qquad n\ge1,\qquad D=3n+1.
$$

则

$$
\delta(\phi v)\ \ge\ pD-\frac{p-1}{2}\ >D.
\tag{4}
$$

**证明。** 令 $m=(p-1)/2$、$\alpha=pn$、$\beta=2pn+p=2\alpha+2m+1$、$N=pD=3\alpha+2m+1$。选每条来源轨道的一个普通次数最小代表，并将最高代表选为上述方向。于是可写

$$
h=tM(n,2n+1)+h_{<D},\qquad t\in K^*,\qquad \deg h_{<D}\le D-1,
$$

且 $\langle h\rangle=v$。由 Frobenius 加法性及 word 的 monic 最高普通项，

$$
\deg\bigl(h^p-t^px^\alpha y^\beta\bigr)\le p(D-1).
\tag{5}
$$

考察 $M(\alpha,\beta)$ 的轨道。以下只用正确的一步平移式

$$
T_+(a,b)=(2a+\eta,(b-\eta)/2),\quad\eta=b\bmod2,
$$

$$
T_-(a,b)=((a-\epsilon)/2,2b+\epsilon),\quad\epsilon=a\bmod2.
$$

令 $W_0=(\alpha,\beta)$、$W_1=T_+W_0=(2\alpha+1,\alpha+m)$，则

$$
\mu(W_0)=N,\qquad\mu(W_1)=N-m.
\tag{6}
$$

若 $\epsilon=\alpha\bmod2$、$\xi=(\alpha+m)\bmod2$，直接再平移一步得到

$$
\mu(T_-W_0)-N=\frac{3\alpha+4m+2+\epsilon}{2}>0,
$$

$$
\mu(T_+W_1)-N=\frac{3\alpha-3m+2+\xi}{2}>0.
\tag{7}
$$

第二个严格不等式使用 $\alpha=pn\ge p=2m+1$。非空 word 的普通次数沿移位是若干 $\ldots,4,2,1,1,2,4,\ldots$ 序列的平移之和，每一项的一阶差分严格递增，故总和亦严格离散凸。由 (6)–(7)，$W_1$ 是唯一最小代表，轨道最小次数为

$$
q=N-m,
$$

而该轨道普通次数不超过 $N$ 的代表恰为 $W_0,W_1$。特别地

$$
q>p(D-1)
\tag{8}
$$

因为 $m<p$。因此 (5) 的低次余项在此目标轨道上没有贡献。

在 $\operatorname{NF}(x^\alpha y^\beta)$ 中，$W_0$ 系数为 $1$，由普通次数 monic 三角性得到。其唯一可能的伙伴 $W_1$ 则满足

$$
U(W_1)-U(\alpha,\beta)
=(5\alpha+m+2)-(4\alpha+2m+1)
=\alpha+1-m>0.
\tag{9}
$$

引理 1 禁止 $W_1$ 出现。其余平移代表的普通次数超过 $N$，同样不能出现。故此目标轨道的 twisted obstruction 只有 $t^p$ 这一项，非零；换代表仅乘非零 $\lambda$ 的整数次幂。得到 $\delta(\phi v)\ge q$。最后

$$
q-D=(p-1)D-m=m(2D-1)>0,
$$

证明 (4)。证毕。

**边界说明。** $n=0$ 时不能使用 (7) 的第二个正性条件：$M(0,p)$ 可能需要超过一步平移才能达到最小普通次数。本证明明确不把 $q=pD-m$ 的公式用于该边界；它由 Step 4 的另一个统一论证处理。

### Step 3. 固定空间统一压到单字轨道

**推论 3。** 对任意 $p>2$，

$$
\ker(\phi-1)\subseteq K\langle x\rangle.
\tag{10}
$$

**证明。** 假设 $v\ne0$ 固定，设 $D=\delta(v)$。既有 strong-balanced 最高支撑引理给出：其顶层只能是唯一的例外轨道 $(n,2n+1)$，并有 $D=3n+1$。若 $n\ge1$，引理 2 与 $\phi v=v$ 矛盾。故 $n=0,D=1$。

每个非空 word 的普通次数至少是其字母数；含至少两个字母的任何平移代表普通次数都至少 $2$。所以 $d(O)=1$ 的唯一非空轨道是单字轨道，得到 (10)。证毕。

**实际使用的修复后顶层引理。** 其结论不依赖旧稿任意 $r$ 步公式。若一个来源 $(a,b)$ 是 strong-balanced，则 $(pa,pb)$ 为次数 $pD$ 的最小代表；较低普通次数项不能进入其轨道。另一顶层来源的最高项若撞入该轨道，也必须是最小次数 $pD$ 的代表。严格离散凸性使这两个位置至多相邻。相邻 $p$ 整除指数对满足 $p\mid(2pa+\eta)$，而 $\eta\in\{0,1\}$，故 $\eta=0$；由于 $p$ 为奇数，$pb$ 偶还给出 $b$ 偶。除以 $p$ 后正是一格来源平移，违背每条来源轨道只取一代表。反向邻居使用逆平移。因此该最高方向不消去；不满足 strong-balanced 的最小代表仍由正确的一步公式给出 $(n,2n+1)$ 或其交换。这是本文件所需的完整有限移位依赖，不复用旧错误的任意步公式。

### Step 4. 任意 $p\ge5$ 的单字不消去

**引理 4。** 对任意素数 $p\ge5$、任意 $c\in K$ 及 $\lambda\in\mathbb F_p^*$，

$$
\phi\langle x\rangle\notin K\langle x\rangle.
\tag{11}
$$

**证明。** 令 $p=2m+1$，所以 $m\ge2$。引理 1 给出：$\operatorname{NF}(x^p)$ 的全部 word 都满足

$$
V(a,b)=a+2b\le p.
\tag{12}
$$

先精确计算边界 $V=p$ 的系数。设 $\operatorname{in}_V$ 表示 $V$-最高权重部分。从递推及初值得

$$
\operatorname{in}_V X_0=x,\qquad
\operatorname{in}_V X_i=(x^2-y)^{2^{i-1}}\quad(i\ge1),
$$

$$
\operatorname{in}_V X_i=y^{2^{-i-1}}\quad(i\le-1).
\tag{13}
$$

在正方向，$X_1$ 的最高权重部分是 $x^2-y$，而后续递推的平方项权重严格超过被减相邻项及常数；负方向则从 $X_{-1}=y$ 开始，后续平方项也严格最高。这证明 (13)，且与 $c$ 无关。

当 $a=2j+1,b=m-j$、$0\le j\le m$ 时，二进制位相乘给出

$$
\operatorname{in}_V M(2j+1,m-j)
=x(x^2-y)^jy^{m-j}.
\tag{14}
$$

这些是全部 $V=p$ 的 word。它们在最高权重空间线性无关：令 $z=x^2$，则除去共同因子 $x$ 后，$(z-y)^jy^{m-j}$、$0\le j\le m$ 是 $z,y$ 的 $m$ 次齐次多项式空间的一组基，由可逆线性替换 $(z,y)\mapsto(z-y,y)$ 得到。恒等式

$$
x^p=x\bigl((x^2-y)+y\bigr)^m
=\sum_{j=0}^{m}\binom mj x(x^2-y)^jy^{m-j}
\tag{15}
$$

与 (12)–(14) 因而表明：$\operatorname{NF}(x^p)$ 中 $M(2j+1,m-j)$ 的系数恰为 $\binom mj$。

选取

$$
j=\lfloor m/2\rfloor,\qquad a=2j+1,\qquad b=m-j.
\tag{16}
$$

该系数不为零，因为 $0\le j\le m<p$，所以 $m!,j!,(m-j)!$ 在特征 $p$ 中均非零。

现在排除其全部平移伙伴，而非只比较最高普通次数。对于任意 word，

$$
V(a(e),b(e))=\sum_i e_i2^{|i|}.
$$

函数 $r\mapsto\sum_i e_i2^{|i+r|}$ 严格离散凸：每个非零字母贡献的二阶差分在所有整数处均严格为正。对 (16)，$a$ 为奇数，一步平移直接给出

$$
V(T_+(a,b))-V(a,b)=a-b,
$$

$$
V(T_-(a,b))-V(a,b)=\frac{4b-a+3}{2}.
\tag{17}
$$

若 $m=2k$，则 $k\ge1$、$(a,b)=(2k+1,k)$，(17) 的两个值为 $k+1,k+1$。若 $m=2k+1$，则 $k\ge1$、$(a,b)=(2k+1,k+1)$，两个值为 $k,k+3$。所有情形均严格为正。因此 (16) 是该平移轨道唯一的最小 $V$ 权重代表，且其最小权重为 $a+2b=p$。

结合 (12)，该轨道的任何其他平移代表均不能在 $\operatorname{NF}(x^p)$ 中出现。其 twisted obstruction 因此只有非零系数 $\binom mj$，不可能被 $\lambda$ 的加权和消去。

最后，$a\ge3$ 且为奇数，故它至少有两个非零二进制位；$b\ge1$ 至少另有一个字母。这个 word 至少有三个字母，既不属于单字轨道，且轨道最小普通次数至少 $3$。因此 $\phi\langle x\rangle$ 有一个非单字的非零方向，证明 (11)。证毕。

### Step 5. 全 mixed 结论

若 $v$ 是 $\phi$ 固定元，推论 3 给出 $v=t\langle x\rangle$。若 $t\ne0$，则半线性给出

$$
\phi v=t^p\phi\langle x\rangle\notin K\langle x\rangle,
$$

与 $\phi v=v$ 矛盾。所以 $t=0$，证明 (1)。既有桥接对全部多项式支撑成立，故立即得到 (2)。$\square$

## Corrections or Missing Assumptions

1. 已通过旧稿中使用的任意 $r$ 步移位表达存在低位反转问题；其主结论使用 Step 3 明写的相邻最小代表证明修复。本文件不把旧 PASS 处置解释为错误表达仍可使用，旧文件保持不变。
2. 例外目标的最小普通次数 $pD-(p-1)/2$ 只在本文件证明的 $n\ge1$ 范围使用。单字情形完全由另一个权重论证处理。
3. 双权重界控制的是每个普通单项式及其三角反演后的 word 权重；它不把加权最高项误当成唯一普通单项式。Step 4 明确处理 $(x^2-y)^j$ 的非单项式最高权重部分。
4. 两次不消去均实际排除了同一来源的全部平移伙伴：Step 2 用普通次数上界加 $U$ 上界，Step 4 用唯一最小 $V$ 权重。没有仅凭一个高 word 系数作结。

## Open Risks

- 本文件是新作者证明，需要针对本文件及主控定向勘误的独立证明检查；不借用旧审查为新增引理授予通过状态。
- $p=3$ 的单字分类不属于本文件主张 (1) 的范围；这里只提供对其同样有效的约化 (10)。
- 不声称一般 Hénon 次数、非代数闭基域或 $\lambda\notin\mathbb F_p^*$ 的相应结论。
- 没有数值或有限枚举证据、查新结论、正式候选评分、页数判断或论文验收声明。

## 最终核验记录

- 全文读取指定的 $336$ 行作者记录与 $117$ 行处置，以及 proof-writer 技能；不改动这些输入。
- 逐项检查双权重递推、普通次数三角反演、两侧相邻平移的精确次数差和低来源截止 $q>p(D-1)$。
- 逐项检查任意奇素数的二项式系数非零性、$m$ 的两种奇偶分支、唯一最小权重和全部平移伙伴的排除。
- 使用 proof-writer 的精确主张、依赖图与边界核验组织此文件；未进行独立审稿、有限实验、数值计算或额外浏览。
