# Proof Package：JR 显式积分的原始 pencil 与所有特征的一般亏格一

Date: 2026-09-08.
Author status: PROVABLE AS STATED；新消费者证明，尚未独立审查。
两项基础作者输入正分别进行非作者检查；本文件不把待回报告当成已通过。
不立项、不评分、不写稿测页，也不把本入口单独算成一篇论文。

## Claim

设 $k$ 为任意特征的代数闭域，$s,t\in k^*$，$s$ 的精确阶为 $r\ge1$。
若 $\operatorname{char}k=p>0$，则 $p\nmid r$。
取 JR 的原始 $I_r(x,y;t,s)$，以及两份基础输入共同定义的实际八次吹起曲面
$S=S_{t,s}$、反典范节点环 $D$ 和开初值曲面 $U=S\setminus D$。

则：

1. 对 $0\le m<r$，$h^0(S,\mathcal O(mD))=1$；
   $h^0(S,\mathcal O(rD))=2$，且 $1,I_r$ 恰是一组基。
2. $f=I_r:S\to\mathbb P^1$ 是无基点完整 pencil 给出的态射，
   $f^*\mathcal O(1)\simeq\mathcal O(rD)$，$f^{-1}(\infty)=rD$ 为概形纤维。
   $f_*\mathcal O_S=\mathcal O_{\mathbb P^1}$，所有几何纤维连通。
3. 存在非空 Zariski 开集 $V\subset\mathbb A^1_k$，使每个 $c\in V$
   的纤维都是光滑、几何整、射影的亏格一曲线。
   此结论包括特征 $2,3$，不只覆盖 $p>3$。
4. $k(I_r)$ 在 $k(S)$ 中相对代数闭，且该函数域扩张可分生成；
   因而 $I_r$ 是原始积分，不是另一个有理函数的次数大于一的复合。
5. 所有有限纤维位于 $U$；一般纤维与原 Laurent 方程 $I_r=c$ 的
   环面部分的光滑射影完成相同。因此第 3 项识别的是 JR 的实际动力纤维，
   不是仅仅“存在另一个亏格一 pencil”。

所有陈述均对每个非零固定 $t$ 成立，不仅对超越或一般 $t$ 成立。
这里没有确定有限坏参数集合，没有证明 JR 的四次条件穷尽该集合，
没有识别 Jacobian 或回返平移点，也没有证明全部有限域轨道的 Hasse 分箱。

## Status

PROVABLE AS STATED，限于本 Claim；独立审查待完成。
这是一般亏格与显式 pencil 身份的证明，不是整个 JR 退化／轨道猜想的完成。

## Assumptions and frozen mathematical inputs

基础输入均已由主控全文读取；本文件使用其数学陈述而非预期的审查结果。

| ID | 作者输入 | SHA256 | 本文件使用的结论 |
|---|---|---|---|
| P | [辛与极除子入口 V1](PAPER30_QPI_SYMPLECTIC_POLAR_ENTRY_V1_20260908.md) | `61d2b0ace7003e19ff1e81242e4080402049d98c024657b94d9b812086f358b3` | $S$ 为八次实际吹起；$D=-K_S$ 是八条 $(-2)$ 曲线的 SNC 环；$D$ nef、$D^2=0$；$(I_r)_\infty=rD$；$1,I_r$ 生成无基点 pencil；四末端例外曲线各与 $D$ 交一次 |
| N | [边界法丛入口 V1](PAPER30_QPI_BOUNDARY_NORMAL_BUNDLE_ENTRY_V1_20260908.md) | `8234b5584adba10ec02adb0269300b0c5191b5445fca345e28e1eb5171c12469` | $N=\mathcal O_D(D)$ 有精确阶 $r$；对每个 $m\ge1$，$h^0(D,N^m)=1$ 当且仅当 $r\mid m$，否则为零；所有特征适用 |

不使用谱商入口来证明本 Claim；该入口即便通过，也不能代替动力纤维身份。
不假设 $I_r$ 已有连通纤维、光滑性、非复合性或 genus-one 性质。

## Notation

$L_m=\mathcal O_S(mD)$，$h^i(L_m)=\dim_k H^i(S,L_m)$。
$\eta$ 为 $\mathbb P^1$ 的泛点，其函数域记为 $K=k(c)$，并以 $c\mapsto I_r$
嵌入 $k(S)$。$f^{-1}(c)$ 均表示概形论纤维。
SNC 指约化除子在每点局部由一个光滑参数或两个横截光滑参数的乘积定义。

## Source and prior-art boundary

- JR 的积分构造及其一般亏格猜想见
  [arXiv:2508.18578v2](https://arxiv.org/html/2508.18578v2)，
  主控已读全文；v2 猜想编号为 3.6，出版版相应编号为 3.7。
- 一般法丛挠阶与 Halphen pencil 的联系已有强覆盖：
  [Cantat–Dolgachev, Proposition 2.2](https://arxiv.org/pdf/1106.0930)
  包括任意代数闭特征的椭圆／准椭圆分支；
  [Carstea–Takenawa, Theorem 2.2](https://arxiv.org/pdf/1005.3586v2)
  已有复数域根单位机制。
  下面将本模型的基础输入接到明确的线性系与光滑性证明；这些标准方法不算新理论。
- 使用 [Stacks, Stein factorization, tag 03H0](https://stacks.math.columbia.edu/tag/03H0)
  的有限中间曲线与几何连通纤维结论；主控已读该定理及其证明。
- 光滑性的局部判据与
  [Stacks tag 01V9](https://stacks.math.columbia.edu/tag/01V9) 相容。
  本文 Step 4 另明确检查平坦、纤维维数与 Jacobian，不能只由一般点的 $df\ne0$
  断言整条几何泛纤维光滑。

## Proof Strategy

用节点法丛的张量幂截面维数及曲面 Riemann–Roch 算出最小完整 pencil。
经 Stein 分解把任何可能的复合次数转为 $h^0(L_r)$，从而排除该次数大于一。
最后单独证明“有一个重数与特征互素的 SNC 纤维，则临界集没有横向分量”，
用这一步排除特征 $2,3$ 的准椭圆可能，而不是调用特征零的一般光滑定理。

## Dependency Map

1. 精确 $h^0$：输入 N、$D^2=0,K_S=-D$、有理曲面的 $H^1(\mathcal O)=0$。
2. 完整 pencil：第 1 项与输入 P 的实际两截面及无基点性。
3. 原始性／几何连通：第 2 项、Stein 分解、投影公式、$H^1(S,\mathcal O)=0$。
4. 所有特征的一般光滑：输入 P 的确切无穷远纤维与 SNC 性，$p\nmid r$，
   Step 4 的独立局部微分论证。
5. 一般几何亏格一：第 3、4 项及曲面伴随公式；不依赖谱曲线或未证明的平移解释。

## Proof

### Step 1. 有理曲面上各 $L_m$ 的 Euler 特征

$S$ 是 $\mathbb P^1\times\mathbb P^1$ 的八次光滑点吹起，
故 $H^1(S,\mathcal O_S)=H^2(S,\mathcal O_S)=0$，$\chi(\mathcal O_S)=1$。
这里的吹起不改变结构层上同调可如下核定：一次点吹起的例外曲线是 $\mathbb P^1$，
其逐层无穷小邻域的理想层商为 $\mathcal O_{\mathbb P^1}(j)$，$j\ge0$，
这些商的 $H^1$ 全为零。由逐层正合列与形式函数定理得 $R^1\pi_*\mathcal O=0$；
$\pi_*\mathcal O=\mathcal O$ 来自目标正规性和双有理性，
更高直像由纤维维数至多一消失。Leray 序列给出上同调不变，
而原 $\mathbb P^1\times\mathbb P^1$ 的高次结构层上同调由 Künneth 公式为零。

对每个 $m\ge0$，曲面 Riemann–Roch 给出

$$
\chi(L_m)=1+\frac{mD\cdot(mD-K_S)}2=1.
\tag{1}
$$

Serre 对偶给 $h^2(L_m)=h^0(\mathcal O(-(m+1)D))=0$。
确实，取任意 ample 除子 $A$，非零有效除子 $D$ 满足 $A\cdot D>0$；
若 $-(m+1)D$ 有有效代表，其与 $A$ 的交数将为负，矛盾。
于是

$$ h^1(L_m)=h^0(L_m)-1. \tag{2} $$

### Step 2. 最小线性系及显式基

因 $D$ 是有效 Cartier 除子，对每个 $m\ge1$ 有准确的正合列

$$
0\longrightarrow L_{m-1}\longrightarrow L_m
\longrightarrow N^{\otimes m}\longrightarrow0.
\tag{3}
$$

当 $1\le m<r$，输入 N 给出 $H^0(D,N^m)=0$。
由 (3) 归纳得到 $h^0(L_m)=h^0(L_0)=1$。
特别地，(2) 给 $H^1(L_{r-1})=0$；$r=1$ 时此句就是 $H^1(L_0)=0$。
在 $m=r$ 使用 $h^0(D,N^r)=1$，长正合列给出

$$ h^0(L_r)=h^0(L_{r-1})+1=2. \tag{4} $$

输入 P 的两个截面 $1,I_r$ 线性独立，因此恰好构成完整空间的基。
它们没有共同零点，所以 $f^*\mathcal O(1)=L_r$；
在把 $1$ 作为齐次分母的坐标规范下，函数值就是原 $I_r$，
分母截面的零除子为 $rD$。故 $f^{-1}(\infty)=rD$，没有换基引入另一参数。

### Step 3. 用截面数排除全部复合次数

对非恒定射影态射 $f:S\to\mathbb P^1$ 作 Stein 分解

$$ S\xrightarrow{h} B\xrightarrow{g}\mathbb P^1. \tag{5} $$

因 $S$ 正规，$B$ 是正规射影整曲线；$k$ 代数闭，故它光滑。
$h_*\mathcal O_S=\mathcal O_B$，$h$ 的几何纤维连通，$g$ 有限。
Leray 的低次正合列给出注入
$H^1(B,\mathcal O_B)\hookrightarrow H^1(S,\mathcal O_S)=0$。
因此 $B$ 亏格为零，有 $k$-有理点，故 $B\simeq\mathbb P^1$。

记 $e=\deg g$，包括可能的不可分次数。投影公式与 (4) 给出

$$
2=h^0(S,f^*\mathcal O(1))
 =h^0(B,g^*\mathcal O(1))
 =h^0(\mathbb P^1,\mathcal O(e))=e+1.
\tag{6}
$$

所以 $e=1$。正规射影曲线间的有限次数一映射为同构，
因而 $f_*\mathcal O_S=\mathcal O_{\mathbb P^1}$，全部几何纤维连通。
这没有只排除可分复合而漏掉纯不可分复合。

### Step 4. 互素重数的 SNC 纤维排除横向临界集

下面明确证明本模型所需的一般引理。
设 $f:S\to\mathbb P^1$ 是光滑射影整曲面到光滑曲线的非恒定态射，
某纤维为 $rD$，其中 $D$ 是约化 SNC 除子，且 $r\in k^*$。
则 $f$ 在基底某个非空开集上光滑。

首先 $f$ 平坦：在任一基底闭点的 DVR 上，$\mathcal O_{S,x}$ 作为模没有挠元，
因为非零基底函数在整曲面函数域中非零。DVR 上无挠模平坦。
纤维是光滑曲面上的非零主 Cartier 除子，纯维数为一。
因此局部的非光滑集等于微分
$f^*\Omega^1_{\mathbb P^1/k}\to\Omega^1_{S/k}$ 的零点集；
可在闭点用相对 Jacobian 判据，或用平坦性与 tag 01V9 的维数判据核定。
这给出闭集 $\mathrm{Crit}(f)$。

在给定纤维的基底点选参数 $z$。在 $D$ 的光滑点可选正则坐标 $u,v$，
使局部 $D=(u)$，并有

$$ z\circ f=u^r a,\qquad a\text{ 为局部单位}. $$

写 $da=a_u\,du+a_v\,dv$，则

$$ d(z\circ f)=u^{r-1}\{(ra+u a_u)\,du+u a_v\,dv\}. \tag{7} $$

$ra+u a_u$ 在该点是单位，因 $r$ 与特征互素。
缩小邻域后，该邻域中所有不属于 $D$ 的点都不是临界点。

在 $D$ 的节点选正则坐标使 $D=(uv)$。此时

$$ z\circ f=u^r v^r a,\qquad
d(z\circ f)=u^{r-1}v^{r-1}
\{v(ra+u a_u)\,du+u(ra+v a_v)\,dv\}.
\tag{8}
$$

括号中的两个单位因子在节点均取值 $ra\ne0$。
缩小邻域后，在 $uv\ne0$ 处该微分不为零。
覆盖整个 $D$，得到开邻域 $W\supset D$，使

$$ \mathrm{Crit}(f)\cap W\subset D. \tag{9} $$

若 $\mathrm{Crit}(f)$ 有支配基底的不可约分量 $Z$，
其在射影曲面中闭，故 $f(Z)$ 闭且等于整个 $\mathbb P^1$，于是 $Z$ 必与 $D$ 相交。
但 (9) 说明 $Z\cap W$ 是 $Z$ 中的非空开集且包含于 $D$，
因此 $Z\subset D$，与支配基底矛盾。
所以全部临界分量都是竖直的。Noether 性给出有限多个分量，
proper 性使它们的像为有限闭点集；移去这些点后，$f$ 光滑。
引理得证。

本模型的 $f^{-1}(\infty)=rD$ 恰满足该引理。
$s$ 的精确阶保证 $r$ 与正特征互素，输入 P 保证 $D$ 的 SNC 性。
因此特征 $2,3$ 也不存在支配整个基底的尖点临界曲线；
本证明没有把“几何泛点处可分”误当作“整个几何泛纤维光滑”。

### Step 5. 实际一般纤维的几何亏格与原始性

移去 Step 4 的有限临界值及 $\infty$，得到非空开集 $V\subset\mathbb A^1$。
Step 3 保证几何纤维连通，Step 4 保证其光滑。
光滑曲线的不同不可约分量不相交，因此几何连通的光滑曲线几何整。
对任一纤维除子 $G\sim rD$，伴随公式给

$$ p_a(G)=1+\frac{G\cdot(G+K_S)}2=1. \tag{10} $$

在光滑几何整纤维上，这就是几何亏格。所有纤维射影，故得到第 3 项。

又 $f_*\mathcal O_S=\mathcal O_{\mathbb P^1}$ 的泛点给
$H^0(S_\eta,\mathcal O)=K$。对光滑射影几何整曲线，其函数域中的常数域正是 $K$；
等价地，几何整性使 $K$ 在 $k(S)$ 中相对代数闭。
Step 4 的泛光滑性给出可分生成性。
若 $I_r=R(J)$，其中 $J\in k(S)$ 非恒定且 $\deg R>1$，
则 $k(J)$ 是 $k(I_r)$ 在 $k(S)$ 中的非平凡有限代数扩张，矛盾。

### Step 6. 与开放初值曲面及原方程的身份

$D$ 是 $\infty$ 纤维的完整支集，所以任一有限纤维都与 $D$ 不交，位于 $U$。
这也说明有限纤维虽然写在开曲面内，实际上仍然射影完整。

唯一可能不与环面相交的非边界曲线是四个末端例外曲线 $E_j$。
输入 P 给出 $D\cdot E_j=1$，所以

$$ (rD)\cdot E_j=r>0. $$

若 $E_j$ 是某个纤维分量，它与另一个纤维的交数应为零，
与上述正交数矛盾。因此没有有限纤维分量完全藏在这些例外曲线中。
原环面方程的闭包在 $S$ 中正是该纤维的支集，一般光滑几何整纤维尤为如此。
由双有理曲线光滑射影模型的唯一性，第 3 项得到的是原 $I_r=c$ 的几何亏格。
这完成 Claim。$\square$

## Corrections or Missing Assumptions

- 没有为通过证明把 $t$ 改成一般参数，或把特征限制成 $p>3$。
- 明确区分算术亏格、几何连通性、几何整性与一般光滑性，每项有独立消费者步骤。
- Step 4 必须保留 $r\in k^*$ 及全部纤维支集为 SNC；
  “任意一个分量上极阶不被特征整除”并不是本文证明的充分条件。
- 本文没有对有限坏参数集合的大小、位置、重数或各坏纤维作声明。

## Open Risks

- 基础输入 P、N 的非作者报告及本新消费者链均需完成实际独立检查，不能以作者状态替代。
- 需要特别独立检查 Step 4 的局部微分到全球无横向临界分量的推理。
- 本文只关闭一般亏格与原始 pencil 身份；JR 四次退化条件的双向完备性仍为 OPEN。
- 实际动力纤维与谱商椭圆曲线的 Jacobian／torsor 桥仍为 OPEN；不由两者均亏格一推出。
- 有限域全部轨道、奇异纤维的分量置换及 Hasse 分箱仍为 OPEN。
- 科学意义、全球新意与自然正文容量仍须在真实新增结果形成后评价；本入口不预支候选资格。
