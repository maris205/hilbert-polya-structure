# 首层整除微分与能级提升障碍的 Čech—Cartier 比较

日期：2026-09-09。作者：主控 `/root`。类型：有界几何作者引理，待非作者检查。
`route_applicability: NOT_APPLICABLE`。不预授 qPI 的实际同余式、全剩余阶结论或新一般理论地位。

## Claim

取混合特征 DVR $\mathcal O$，剩余域 $k$ 完美、特征为素数 $p$，参数为 $\pi$，且
$$v_\pi(p)=p-1.$$
取常数单位 $\lambda\in\mathcal O^\times$，满足 $\bar\lambda=1$ 及
$$\overline{\lambda\pi^{p-1}/p}=-1\quad\text{in }k. \tag{A1}$$
不要求 $\mathcal O/(\pi^2)$ 具有特征 $p$；特别允许 $p=2$ 的混合特征二阶商。

设 $\mathcal U/\mathcal O$ 光滑，相对维数二，$U_0=\mathcal U\otimes k$，
且 $J\in\Gamma(U_0,\mathcal O_{U_0})$。给定 $h\in k$，假设
$$X=(J=h)\subset U_0$$
是完整、光滑、射影、几何整的亏格一曲线；在需要时可先作完美剩余域扩张。
特别是 $dJ$ 在 $X$ 上是环境余切模的非零法向截面。

固定一个全局函数 $I\in\Gamma(\mathcal U,\mathcal O_{\mathcal U})$，
以及只含底环常数系数的多项式
$$F(H)=\lambda H^p+pQ(H),\qquad Q\in\mathcal O[H]. \tag{A2}$$
这里大写 $H$ 暂为多项式自变量。记
$$\widehat{mathcal H}(H)=F'(H)/p\in\mathcal O[H],\qquad
\mathcal H=\overline{\widehat{mathcal H}}\in k[H],$$
并假设 $\mathcal H(h)=0$。

在覆盖 $X$ 的原光滑模型开集 $U_i$ 上选正则 $j_i$ 提升 $J$，假设
$$I-F(j_i)\in p\pi\,\mathcal O_{U_i}. \tag{A3}$$
令
$$f_{ij}=\overline{(j_j-j_i)/\pi}\big|_X,$$
并设这给出的能级提升障碍满足
$$\kappa_J=[(f_{ij})]\ne0\quad\text{in }H^1(X,\mathcal O_X). \tag{A4}$$
取 Čech 符号为零上链 $(c_i)$ 的余边界 $c_j-c_i$。
可以把覆盖细化到使 Čech 上同调计算该拟凝聚层的上同调；改变局部提升只改变余边界。

**OC.1：准确的上同调类比较。** 定义
$$G_i=\frac{I-F(j_i)}{p\pi},\qquad
\alpha=p^{-1}d_{\rm state}I.$$
则 $\alpha$ 在 $X$ 的邻域整且正则，局部满足
$$\alpha=\widehat{mathcal H}(j_i)dj_i+\pi dG_i.$$
形式
$$\nu=d(\bar G_i|_X)$$
在整个 $X$ 上粘合成一个正则一形式，并属于局部恰当微分层 $B^1_X=\operatorname{im}(d:\mathcal O_X\to\Omega^1_X)$。
对正合列
$$0\longrightarrow\mathcal O_X^p\longrightarrow\mathcal O_X
\xrightarrow{d} B^1_X\longrightarrow0,$$
其连接同态 $\partial$ 满足
$$\boxed{\quad\partial(\nu)=\operatorname{Fr}_*(\kappa_J)
\quad\text{in }H^1(X,\mathcal O_X^p).\quad} \tag{OC1}$$
其中 $\mathcal O_X^p$ 是局部 $p$ 次幂函数子层，
$\operatorname{Fr}_*$ 由加法层同构 $f\mapsto f^p$ 诱导，按 $k$ 常数理解为 Frobenius 半线性，
**不是**随后嵌入 $H^1(X,\mathcal O_X)$ 的 Hasse/Frobenius 线性算子。

**OC.2：首切向单位及完整理想。** $\nu$ 非零，且在整个 $X$ 上处处非零。
在每一实际局部环 $\mathscr A=\mathcal O_{\mathcal U,P}$、$P\in X$ 中，
$$\boxed{\quad\mathfrak c(\alpha)_P=(\pi,\widetilde{mathcal H(J)}).\quad} \tag{OC2}$$
波浪号表示剩余函数的任意局部提升，$\mathfrak c$ 保留原相对自由秩二微分模的两个系数。

## Status、边界与依赖

**PROVABLE AS STATED**，下面给出完整证明；作为新的作者件仍待非作者核查。
本引理的科学前提包括实际同余式 (A3) 与实际障碍非零 (A4)；不能仅因存在一个抽象补基而省略它们。
它没有断言任意根单位迹、任意 q-difference 模型或任意退化都满足这两项前提。

没有使用本方向先前的纯四次 $R$ 配对或首矩阵 jet 公式。
采用的工具是 Čech 连接同态、光滑曲线上的 $\ker d=\mathcal O_X^p$ 及亏格一典范除子次数。
这些标准工具和比较形式的先例地位需在来源阶段扣除，不把下面自足证明视为全球创新证据。

责任图为：整数 Taylor 商 $\to$ $G_i$ 的实际粘合余差 $\to$
局部恰当微分连接类 $\to$ 非零首切向类 $\to$ 原两状态理想。
本件没有识别 qPI 的 $\kappa_J$，也没有证明其 $I$ 满足 (A3)。

## Proof

### Step 1. 首层整数 Taylor 商

对任意 $a,f$ 属于一个 $\mathcal O$-平坦的交换代数，(A2) 给
$$F(a+\pi f)-F(a)
=\lambda\sum_{r=1}^{p}\binom pr a^{p-r}\pi^r f^r
+p\bigl(Q(a+\pi f)-Q(a)\bigr).$$
当 $1\le r<p$ 时 $p\mid\binom pr$，而 $r=p$ 的一项由
$v_\pi(p)=p-1$ 保证 $\pi^p/(p\pi)$ 为单位。
因此整个差可被 $p\pi$ 整除。除完后模 $\pi$，$2\le r<p$ 的项都消失；
对 $Q$ 只留下其一次 Taylor 项。得到
$$\overline{\frac{F(a+\pi f)-F(a)}{p\pi}}
=\mathcal H(\bar a)\bar f+
\overline{\lambda\pi^{p-1}/p}\,\bar f^p
=\mathcal H(\bar a)\bar f-\bar f^p. \tag{1}$$
这在 $p=2$ 同样成立：中间求和为空；没有把 $p$ 在底环中置零后再除以它。

### Step 2. 局部原函数与精确粘合余差

(A3) 使每个 $G_i$ 为实际正则函数；平坦性使除法所给函数唯一。
对 $I=F(j_i)+p\pi G_i$ 作相对微分，因所有系数、$p,\pi$ 对状态为常数，得到
$$p^{-1}dI=\widehat{mathcal H}(j_i)dj_i+\pi dG_i. \tag{2}$$
右侧整且正则，故也给 $\alpha$ 的实际局部整延拓；在重叠上因同为特征零的 $p^{-1}dI$ 而一致。

在重叠处取 $j_j=j_i+\pi\widetilde f_{ij}$。由 (1)，
$$\bar G_j-\bar G_i
=-\mathcal H(J)\bar{\widetilde f}_{ij}
+\bar{\widetilde f}_{ij}^{,p}\quad\text{on }U_0. \tag{3}$$
再限制到 $X$；因 $\mathcal H(h)=0$，得到准确函数等式
$$\bar G_j|_X-\bar G_i|_X=f_{ij}^p. \tag{4}$$
这里没有只在函数域中比较，也没有省略时间或原能级常数的变化。
在特征 $p$ 的 $X$ 上求微分，(4) 的右边为零；
所以 $d(\bar G_i|_X)$ 粘为 $\nu\in H^0(X,B_X^1)\subset H^0(X,\Omega_X^1)$。

由 (2)，它也正是环境一形式 $(\alpha-\widehat{mathcal H}(j_i)dj_i)/\pi$
约化后在 $\Omega^1_{U_0}|_X/\mathcal O_XdJ=\Omega^1_X$ 中的类。
因此它是原整除微分的两方向分解所给首切向类，而非另选的一条有利微分。
若 $j_i$ 改为 $j_i+\pi a_i$，(3) 的局部改变量限制到 $X$ 为一个 $p$ 次幂，
其微分为零；这也直接说明首切向类对局部提升不变。

### Step 3. $\ker d=\mathcal O_X^p$ 的适用条件

在完美域上的光滑几何整曲线，其函数域 $K$ 可取分离超越基 $z$，
$K/k(z)$ 为有限可分扩张。若其次数为 $n$，Frobenius 及 $k$ 完美给
$$[K^p:k(z^p)]=n,\qquad [K:k(z^p)]=pn,$$
所以 $[K:K^p]=p$。可分性使 $dz\ne0$，且 $z\notin K^p$，
故 $1,z,\ldots,z^{p-1}$ 是 $K/K^p$ 的基。
逐项微分这一展开，证明 $\ker(d:K\to\Omega^1_{K/k})=K^p$。

若一个正则函数 $g$ 在曲线开集上微分为零，在函数域中有 $g=a^p$。
该开集每一局部 DVR 的赋值满足 $pv(a)=v(g)\ge0$，因此 $a$ 在所有点正则；
光滑曲线正规，故 $a$ 是该开集上的正则函数。
这证明所用层核确为 $\mathcal O_X^p$，而非仅在泛点相等。
Frobenius 在约化层 $\mathcal O_X$ 上单射，并按 $\mathcal O_X^p$ 的定义局部满射，
故它是到该像层的加法层同构。完美 $k$ 也保证 $\mathcal O_X^p$ 对所有 $k$ 常数封闭。

### Step 4. 连接同态与不能混淆的两个 Frobenius 箭头

$B_X^1$ 按定义是上述 $d$ 的像层，所以 Step 3 给 Claim 中的短正合列。
用 $\bar G_i|_X$ 作为 $\nu$ 的局部原函数计算其连接类。
按已固定的 Čech 符号，其代表正是 (4) 的余差 $(f_{ij}^p)$，
于是
$$\partial(\nu)=[(f_{ij}^p)]
=\operatorname{Fr}_*[(f_{ij})]=\operatorname{Fr}_*(\kappa_J).$$
这证明 (OC1)。由于 $\operatorname{Fr}:\mathcal O_X\to\mathcal O_X^p$ 是层同构，
它在上同调上也是加法群同构；(A4) 因而给 $\partial(\nu)\ne0$，从而 $\nu\ne0$。

这里不能把目标换成 $H^1(X,\mathcal O_X)$ 后说像仍非零。
事实上，短正合列精确性迫使该连接像经
$H^1(X,\mathcal O_X^p)\to H^1(X,\mathcal O_X)$ 后为零；
这个后续嵌入所诱导的上同调映射正是超奇异情况下可以为零的另一箭头。
本证明保留像层及完整连接列，因此没有作“超奇异 Frobenius 可逆”的错误推论。

### Step 5. 从非零切向类到所有点的实际理想

$X$ 光滑射影亏格一，$\deg\Omega^1_X=2g-2=0$。
非零正则一形式的零除子有效且次数为零，故为空。
因此 $\nu$ 在完整 $X$ 的每个点非零，而不只是在一个环面稠密开集上非零。

在 $P\in X$ 的实际局部自由秩二模中，将 $dj_i$ 补为基 $(dj_i,\theta)$；
这可行，因为其剩余法向 $dJ$ 非零。由 (2) 写
$$\alpha=(\widehat{mathcal H}(j_i)+\pi A)dj_i+\pi B\theta.$$
$\nu(P)\ne0$ 说明 $B$ 在该局部环为单位，因此
$$\mathfrak c(\alpha)_P
=(\widehat{mathcal H}(j_i)+\pi A,\pi B)
=(\pi,\widehat{mathcal H}(j_i)).$$
任一其他剩余函数 $\mathcal H(J)$ 的提升只相差 $\pi$ 倍数，理想不变。
这证明 (OC2) 的全部局部点量词。证毕。

## Corrections or Missing Assumptions

- 非零障碍必须位于该完整 $X$ 的 $H^1(\mathcal O_X)$；只有其他空间上的一个非零类还不足够。
- (A3) 必须是先在整数环中成立的实际 $p\pi$ 同余；仅有 $\bar I=J^p$ 或整除 $dI$ 不够。
- 首层 $v_\pi(p)=p-1$ 用于 Taylor 商的 $p$ 次项；高层圆分参数不自动满足这个相同论证。
- 完美剩余域、光滑与正规性用于函数层 $p$ 次根；射影亏格一用于将非零变为处处非零。
- 标准 Čech／Cartier 工具不是本引理宣称的新理论；实际 qPI 前提的识别需另证并独审。

## Open Risks

本件未判断 qPI 全 $p,m$ 是否满足 (A3)–(A4)，未提供实际迹的 word-orbit 证书，
未代替旧原曲面的完整几何，也未声称一般 $m$ 的端点配对常数必为 $m^2$。
它是一条可独立检查的比较引理，不是论文、新意票、晶体比较或全厚度结论。
仅新增本文件；无 GPU、稿件、锁、PDF 或外部效力。
