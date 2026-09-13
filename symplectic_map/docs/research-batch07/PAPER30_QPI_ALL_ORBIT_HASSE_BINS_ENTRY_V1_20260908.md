# Proof Package：qPI 全部有限域轨道的 Hasse 上界与原始分箱

Date: 2026-09-08.
Author status: PROVABLE AS STATED，依赖下列两份已写出但仍在非作者核查中的新证明。
本消费者自身也尚未独立审查；此时不把整条链登记为已接受定理。
仅新增本地证明文件；不立项、不建锁、不写论文稿／PDF、不评分或估页。

## Claim

设 $q=p^e$ 为任意素数幂，$e\ge1$，$s,t\in\mathbb F_q^*$，
$s$ 的精确乘法阶为 $r$。在 JR 的完整初值空间
$U_{t,s}=(\mathbb G_m)^2\sqcup L_1\sqcup L_2\sqcup L_3\sqcup L_4$ 上使用实际一步映射

$$
F_t(x,y)=\left(\frac{st}{sx-y},\frac{sx}{y}\right),\qquad t\longmapsto st,
$$

并在末端状态上使用原有的正则延拓。
令 $\gamma$ 为任意完整一步周期轨道，$m_\gamma=\#\gamma$ 为其最小周期，
$\ell_\gamma=m_\gamma/r$ 为 JR 定义的 reduced orbit length。
置

$$
N_-=q+1-2\sqrt q,\qquad N_+=q+1+2\sqrt q,\qquad
M_q=\left\lceil\frac{\sqrt q+q^{-1/2}-2}{4}\right\rceil.
$$

则：

1. $\ell_\gamma$ 为正整数，且

   $$\boxed{\ell_\gamma\le N_+.}$$

2. 定义原分箱

   $$
   B_j^{(q)}=
   \begin{cases}
   [N_-/j,N_+/j],&1\le j<M_q,\\
   [1,N_+/M_q],&j=M_q.
   \end{cases}
   $$

   则 $\ell_\gamma$ 落在其中恰好一个分箱。
   这些闭区间两两不交，包括 $M_q=1$ 的小域情形。
3. 更准确地，对该轨道的实际有限能级：
   - 若纤维光滑，$\ell_\gamma$ 整除某个椭圆曲线点数 $N\in[N_-,N_+]$；
   - 若纤维奇异，$\ell_\gamma$ 整除 $q-1$ 或 $q+1$，或者 $\ell_\gamma=p$。
     其中唯一奇点的回返周期为 $1$，没有将该状态删掉。

因此，若下列输入及本消费者经独立核查接受，得到 JR 作者 v2 的
Conjecture 1.2.A、1.2.B 的完整结论，适用于全部允许的 $q,s,t$ 和全部合法状态。
这里不缩为光滑能级，不假定 $s=1$，也不排除特征 $2,3$。
本件不同时宣布其准确坏值 Conjecture 3.6 已关闭。

## Status and dependencies

PROVABLE AS STATED 是作者证明状态，不是独立验收票。
仅消费以下两份新作者包的指定结论；它们的独立核查当前并行进行。

| ID | 输入 | SHA256 | 本件消费范围 |
|---|---|---|---|
| F | [实际有限纤维](PAPER30_QPI_ACTUAL_SINGULAR_FIBRE_ENTRY_V1_20260908.md) | 3b7a495b723d9ba45003fe767431c4420053c0b3de6656a2335c3aad01307003 | 所有有限纤维射影、几何整约化、算术亏格一；每个坏纤维只有一个几何奇点、正规化亏格零 |
| R | [实际回返平移](PAPER30_QPI_RETURN_TRANSLATION_ENTRY_V1_20260908.md) | 9ee29e426c14334c41c26b1265bd71fe53b232c37949d5ad21aef14550a6851c | 全初值空间及紧曲面的真实同构；积分保持；所有有限光滑纤维回返是平移；完整周期除以 $r$ 的准确关系 |

F、R 消费的未变 P、G 等基础已经接受，本件不重新证明基础。
本件不消费 F 的长度四计算，不消费谱 Jacobian 桥，
也不要求先证明 $R_{r,t,s}(c)=\delta(c,t^r)$ 或其零集身份。
不把两份输入作者稿中的自评当作非作者 PASS。

## Notation

固定初始时间 $t$，置

$$\mathcal R=F_{s^{r-1}t}\circ\cdots\circ F_t.$$

$f=I_r$ 是实际原积分；$C=f^{-1}(c)\subset U_{t,s}$ 是有限能级的整条射影纤维。
它不是仅取原环面方程的点集，也不是删除奇点后的曲线。
$\nu:\widetilde C\to C$ 为其正规化。
本文用 $\mathcal R$ 表示回返，避免与 F 输入的临界值多项式 $R_{r,t,s}$ 混用。

## Source boundary

- 实际逐项核对 [JR 作者 v2，Definition 1.1、Conjecture 1.2、Definition 2.2、
  Algorithm 1](https://arxiv.org/html/2508.18578v2)。
  上面的分箱、上界和 reduced length 定义就是其原声明，不是事后另选阈值。
  原文的自治说明及先前可积映射／Hasse 联系均为先例；
  本件的新消费者任务是全非自治参数和所有奇异层的覆盖。
- 使用 Hasse 定理：对任意 $\mathbb F_q$ 上椭圆曲线 $E$，
  $|\#E(\mathbb F_q)-(q+1)|\le2\sqrt q$。
  实际读取 [Milne, Elliptic Curves, 2nd ed., Chapter IV,
  Theorem 9.4 及其完整证明和随后的 $p\mapsto q$ 说明](https://jmilne.org/math/Books/EC2.pdf)，
  书内第 150 页。它包括全部有限域特征，无 $p>3$ 前提。
  本件不声称 Hasse 定理是新结果。
- 亏格零且有有理点的光滑射影曲线为 $\mathbb P^1$，使用
  [Stacks 53.10.2、53.10.4](https://stacks.math.columbia.edu/tag/0C6L)，
  已读取这两项的假设和完整证明。本文实际轨道本身给出正规化上的有理点，
  因而不需另外假定所有 genus-zero torsor 都平凡。
- 下面直接证明所用 $\operatorname{PGL}_2(\mathbb F_q)$ 元素阶分类，
  不把一般椭圆平移定理或有限群分类重复包装成新贡献。

本轮沿用已做的相关本地来源检查；没有新下载、外部写或全局查新评分。

## Proof Strategy and Dependency Map

1. 在实际时间切片上，完整一步周期除以 $r$ 恰为 $\mathcal R$ 周期。
2. 光滑能级由 R 转化成有限椭圆群中的点阶；应用 Hasse。
3. 奇异能级由 F 转化成一条有理正规化；唯一奇点固定，
   其余实际点经正规化不改变周期，适用二维矩阵的 Jordan／特征值分类。
4. 用一个整数除数引理及 $p$ 的专门分支，把两类长度放入原阈值分箱。
5. 单独检验原分箱的两两不交和 $M_q=1$ 边界。

## Proof

### Step 1. 全部实际轨道都进入某个有限完整纤维

R 给出 $F_t:U_{t,s}\simeq U_{st,s}$，并保持原积分。
有限域上的合法状态集有限，正反方向均定义，因此每条轨道均为周期轨道，
没有额外的前周期尾巴。积分在 $U$ 正则且按 $\mathbb F_q$ 定义，
所以任一状态的积分值 $c$ 属于 $\mathbb F_q$，而非无穷远值。
纤维在一步映射下送到同一积分值、下一时间的纤维。

时间坐标沿 $t,st,\ldots$ 变化，且 $t\ne0$，因此 $r\mid m_\gamma$。
固定时间切片上的 $\mathcal R$ 最小周期恰为 $\ell_\gamma=m_\gamma/r$：
若更短的 $\mathcal R$ 迭代回到原点，便给出更短的完整一步周期；
若完整一步回到原状态，其步数必须为 $r$ 的倍数。
这也说明 $\ell_\gamma$ 为正整数。

F 的量词在基变换到 $\overline{\mathbb F}_q$ 后适用。
故每个有限 $C/\mathbb F_q$ 射影、几何整约化且算术亏格一。
以下光滑／奇异两种情况穷尽所有有限能级，无须事先定位坏值。

### Step 2. 光滑纤维的长度整除 Hasse 区间内的整数

若 $C$ 光滑，任一所选实际轨道状态 $Q\in C(\mathbb F_q)$
可作为原点，将 $C$ 识别为 $\mathbb F_q$ 上椭圆曲线。
R 已证明 $\mathcal R$ 在这个实际光滑纤维上为平移，
其位移 $P=\mathcal R(Q)-Q$ 在 $\mathbb F_q$ 上。
对于任一 $Q'$，

$$\mathcal R^a(Q')=Q'+aP.$$

所以 $\ell_\gamma=\operatorname{ord}(P)$，由有限群 Lagrange 定理，

$$\ell_\gamma\mid N:=\#C(\mathbb F_q).$$

Hasse 定理给 $N_-\le N\le N_+$。
因此光滑情况不仅有上界，还具有所需整数整除结构。

### Step 3. 奇异状态固定，非奇异状态在正规化上保持原周期

若 $C$ 奇异，F 给出唯一几何奇点 $a$，且正规化的几何亏格为零。
唯一性使该点在 Frobenius 下不变；有限域完美，故 $a$ 是 $\mathbb F_q$-有理点。
曲线自同构保持奇异点集，因此 $\mathcal R(a)=a$。
若所选轨道在固定时间切片经过 $a$，其 reduced length 就是 $1$。
这条轨道仍属原合法状态，不删除或收缩它。

其余状态 $Q$ 在 $C$ 的光滑部分。
正规化在该部分是同构，所以 $Q$ 有唯一原域有理提升
$\widetilde Q\in\widetilde C(\mathbb F_q)$。
正规化在完美域上是光滑射影几何整曲线；在代数闭包上它是 F 的亏格零正规化，
故其原域亏格也是零。
$\mathcal O_{\widetilde C}(\widetilde Q)$ 的次数为一，Stacks 53.10.2
使其完整线性系给出到 $\mathbb P^1_{\mathbb F_q}$ 的闭浸入。
像是一维闭子曲线，故即整个 $\mathbb P^1$。
从而 $\widetilde C\simeq\mathbb P^1_{\mathbb F_q}$。

$\mathcal R$ 通过正规化的通用性质唯一提升为
$g:\widetilde C\simeq\widetilde C$，且 $\nu g=\mathcal R\nu$。
该提升按 $\mathbb F_q$ 定义，逆映射由 $\mathcal R^{-1}$ 提升。
原轨道始终避开 $a$，正规化在其上逐点单射，所以

$$
g^d(\widetilde Q)=\widetilde Q
\quad\Longleftrightarrow\quad
\mathcal R^d(Q)=Q.
$$

因此正规化没有改变该实际周期。
节点两分支是否按 $\mathbb F_q$ 分裂，以及尖点是否在小特征，
均不影响此结论；没有为下降偷偷选择某个奇点分支。

### Step 4. 射影直线自同构的全部可能周期

$\mathbb P^1_{\mathbb F_q}$ 的自同构保持次数一线丛，
作用于其二维全局截面，因而由某个
$A\in\operatorname{GL}_2(\mathbb F_q)$ 表示，
只相差标量矩阵：$g\in\operatorname{PGL}_2(\mathbb F_q)$。
有限域完美，所以 $A$ 的特征多项式只有以下情况。

**标量。** $g=1$，所有周期为 $1$。

**重根非标量。** 重根 $\lambda$ 属于 $\mathbb F_q^*$。
缩放并换基后 $A=1+N$，$N\ne0,N^2=0$。
在特征 $p$ 中，

$$(1+N)^j=1+jN.$$

当 $1\le j<p$ 时它非标量，而 $j=p$ 时恒等。
故 $g$ 的阶为 $p$，每个点周期为 $1$ 或 $p$。
此处没有把特征二的阶误设为 $2$ 之外的偶数。

**两个不同的原域特征值。** 对角化后，
$g$ 的阶等于特征值比 $\rho\in\mathbb F_q^*$ 的阶，
所以整除 $q-1$；每个点周期也整除 $q-1$。

**不可约二次特征多项式。** 两根为
$\lambda,\lambda^q\in\mathbb F_{q^2}^*$。
它们的比 $\rho=\lambda/\lambda^q$ 满足

$$\rho^{q+1}=1.$$

在 $\mathbb F_{q^2}$ 上对角化表明 $g$ 的阶为 $\operatorname{ord}(\rho)$，
所以整除 $q+1$，每个点周期也整除 $q+1$。
共轭扩域不改变矩阵某幂是否为标量的事实。

综上，奇异纤维的任意实际 reduced length 满足

$$\ell_\gamma\mid(q-1)\quad\text{或}\quad
\ell_\gamma\mid(q+1)\quad\text{或}\quad\ell_\gamma=p.$$

周期 $1$ 包含于前两种，因 $q\ge2$。
因此奇异情况下 $\ell_\gamma\le q+1\le N_+$。
结合 Step 2，得到 Claim 1 和 Claim 3。

### Step 5. 原分箱的界与两两不交

置 $x=\sqrt q>1$ 以及

$$
b=\frac{N_-}{4x}=\frac{x+x^{-1}-2}{4}>0,\qquad M=\lceil b\rceil=M_q.
$$

故 $M\ge1$。由 $M<b+1=N_+/(4x)$，得到

$$\frac{N_+}{M}>4x>1.\tag{1}$$

所以最后一个分箱是非空区间，且包含 $1$。
若 $1\le j<M$，则 $j\le M-1<b$，从而

$$
j(N_+-N_-)=4xj<N_-
\quad\Longrightarrow\quad
\frac{N_+}{j+1}<\frac{N_-}{j}.
\tag{2}
$$

式 (2) 说明每一对相邻分箱之间有严格间隔，包括最后一个扩展到底的分箱；
于是全部分箱两两不交。$M=1$ 时只有 $[1,N_+]$，无需相邻比较。

### Step 6. 整数除数与单独的特征 $p$ 分支恰落原分箱

先证明除数引理：若正整数 $\ell$ 整除某个整数
$N\in[N_-,N_+]$，置 $j=N/\ell\in\mathbb Z_{\ge1}$。
若 $j<M$，则

$$N_-/j\le\ell=N/j\le N_+/j,$$

所以 $\ell\in B_j^{(q)}$。
若 $j\ge M$，则 $1\le\ell\le N_+/M$，所以 $\ell\in B_M^{(q)}$。
这不是只由 $\ell\le N_+$ 推出的分箱结论；整数除数是必需的。

光滑情况已由 Step 2 满足此引理。
奇异情况下，$q-1$ 和 $q+1$ 都在 $[N_-,N_+]$：
$q-1-N_-=2\sqrt q-2>0$，其它端点不等式直接成立。
因此整除 $q\pm1$ 的两类也满足引理。

剩下 $\ell=p$。若 $M=1$，由 $p\le q<N_+$ 落入唯一分箱。
若 $M\ge2$，分两种：

- 当 $e=1$，$p=q\in[N_-,N_+]$，故 $p\in B_1^{(q)}$。
- 当 $e\ge2$，$p\le\sqrt q=x$；由 (1)，
  $1\le p<N_+/M$，故 $p\in B_M^{(q)}$。

于是全部实际轨道长度都至少落入一个原分箱；
Step 5 的严格不交使这个分箱唯一。这完成 Claim 2，及完整 Claim。$\square$

## Corrections or Missing Assumptions

- 没有新增一般 $t$、大特征、光滑能级或自治参数条件。
- 奇异层必须单独论证；不能直接套光滑椭圆平移或仅凭 Hasse 上界推出分箱。
- 正规化所需原域点来自所选非奇异实际状态，不预设节点分支原域分裂。
- 用的是原完整周期除以 $r$，不是第三种删缩状态算法。
- 不把 $p$ 一概说成 $q$；在非素有限域中，$p$ 是单独放入末箱的分支。
- 原谱商、准确坏参数、临界长度四和位移坐标均不是此证明的必要输入。

## Verification and open risks

1. 原定义、两个原猜想及完整状态算法已从 JR 作者 v2 实际读取。
2. 两份新输入已由主控全文读取，但当前其独审未完成；
   本稿没有用作者状态代替依赖验收。依赖若出现真实修正，应按修正范围复核本消费者。
3. 本消费者须由未参与作者推导者独立核查；
   重点是有限域下降、唯一奇点、正规化周期保真、$\operatorname{PGL}_2$ 的四种情况，
   以及 $M_q$ 的 ceiling 严格不等式和 $p$ 分支。
4. 本稿是全参数符号证明，不采用固定小域枚举、实验拟合或事后调箱。
5. 准确坏值与谱四次的身份仍另行开放；本文不偷换为已证明 JR 的全部猜想。
6. Hasse、genus-zero 有理点判据、矩阵阶分类和整数除数引理都是已知／初等工具；
   科学验收、新意／价值／容量审查与论文交付是分开的阶段。
