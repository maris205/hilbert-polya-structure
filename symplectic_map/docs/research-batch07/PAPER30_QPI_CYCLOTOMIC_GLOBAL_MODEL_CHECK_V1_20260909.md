# Paper30 qPI：圆分完整模型 G1–G3 独立数学核查 V1

日期：2026-09-09。独立核查者：`/root/p30_qpi_cyclotomic_global_check_v1`。
类型：限定输入、限定主张的非作者数学核查；不是正式四门、查新、Route 评价、立项接受或稳定约化分类。

## Claim

核查[作者 G 诊断 V1](PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_DIAGNOSTIC_V1_20260909.md)的 G1–G3 全部合取，保留其原矩阵、原积分、原能级及相对微分规范。

1. G1：同一个八截面吹起模型在圆分 DVR 上光滑射影；八环边界相对反典范；原截面生成的态射射影平坦，剩余态射准确为小阶 pencil 后接幂态射，包含全部几何剩余能级的概形重数。
2. G2：原完整线性系的实际基变换像和余核、第一上同调的自由部分与扭子过滤、扭子长度及零阶 Fitting 理想、最少生成元数全部成立，且不假设扭子过滤分裂。
3. G3：原状态微分除以 $p^a$ 后在整个开放初值空间正则，约化恒等式与系数理想等式包括四条完整末端仿射直线；公共整除阶与扭子长度一致，但不等同于逐闭点赋值或临界理想饱和。

## Status

**PROVABLE AS STATED。G1：数学 PASS；G2：数学 PASS；G3：数学 PASS。**

原主张的量词与规范不需削弱，没有发现要求修改作者稿的数学错误。这里的 PASS 明确消费已接受的域上 T1 和本轮另行 fresh 数学 PASS 的 D1–D3；不是重新核发那些依赖的接受，也不对来源新意作判断。

| 核查对象 | 结论 | 关键理由 |
|---|---|---|
| 八截面吹起、特化碰撞、相对八环 | PASS | 末次中心在四个不同分量，坐标 $1,t,t,s$ 始终为单位 |
| $I_r$ 作为 $\mathcal L_r$ 截面的高度一延拓 | PASS | 水平素点由域上 T1，唯一竖直素点由 Laurent 整性，局部自由模用正常性延拓 |
| 完整原 pencil 的生成性、平坦及 $\operatorname{Pow}_N$ 复合 | PASS | 基底的泛、闭两个纤维上截面生成性加 Nakayama；逐纤维平坦判据条件齐备 |
| 相对边界复形、$j<r$ 过滤及 $j=r$ 限制满射 | PASS | 有向乘子为 $s^{-1}$；原 $I_r$ 的边界限制在所有点生成 $\mathcal N^r$ |
| 长度、Fitting 理想与最少生成元 | PASS | 长度由乘积恒等式得出；生成元数由实际基变换正合列独立计算 |
| 全 $\mathcal U$ 上的整除微分与非饱和边界 | PASS | 微分层局部自由，剩余环面稠密，整除首项非零；系数理想取约化后的像 |

## Assumptions

设 $p$ 为任意素数，$a,m\ge1$，$p\nmid m$，并设

$$
N=p^a,\qquad r=mN,\qquad s=\zeta_r,\qquad
\mathcal O=\mathbb Z[\zeta_r]_{\mathfrak p},\quad\mathfrak p\mid p.
$$

$\mathcal O$ 是特征零 DVR，$\pi$ 是其任意参数，$K$ 与 $\kappa$ 分别为分式域与剩余域，$e=v_\pi(p)$。固定任意 $t\in\mathcal O^\times$。剩余根单位 $\eta=\bar s$ 的精确阶为 $m$。不添加 $p>3$、一般 $t$、$m>1$ 或 $a=1$ 的限制。

模型严格采用作者 G §1 的 $1+2+3+2$ 次截面吹起；$\mathcal D$ 是四条坐标边界及四条中间节点例外曲线的最终严格变换之和。末次四条例外不计入 $\mathcal D$。

消费的已知数学输入仅为：

- 域上 T1，分别用于 $K$ 中阶 $r$ 及 $\kappa$ 中阶 $m$：实际无基点最小完整 pencil、极除子、$f_*\mathcal O=\mathcal O$，及全部有限几何纤维整且约化。需要时先作代数闭域扩张再下降。
- D1–D3 中本核查所需的 D1、D2：原 Laurent 环内 $\bar I_r=J^N$，$p^{-a}dI_r$ 整，约化为 $H^\sigma dJ\ne0$；任意单位 $t$ 特化仍成立。本核查全文读取 D，但不重做其循环插入与 Cartier 证明。
- P 的实际坐标、反典范边界构造，以及 N 的明确节点帧与传播比。混合特征结论在下文重新建立，不把域上接受当作相对结论。

## Notation

$$
\mathcal U=\mathcal S\setminus\mathcal D,\qquad
\mathcal L_n=\mathcal O_{\mathcal S}(n\mathcal D),\qquad
\mathcal N=\mathcal O_{\mathcal D}(\mathcal D),\qquad
J=I_{m,\eta}(x,y;\bar t).
$$

记 $T=\bar t^m$、$\varepsilon=(-1)^{m+1}$、$\sigma=(N-1)/(p-1)$、$H=H_p(T,J;\varepsilon)$，使用 D 原定义的 $H_p$，包括 $H_2(T,h;\varepsilon)=h$。所有微分固定 $\mathcal O$，特别固定 $t$。

下文把支持在 $\mathcal D$ 或剩余纤维的层隐含地推前到 $\mathcal S$。$\mathcal T[\pi]$ 表示被 $\pi$ 杀死的子模；$\mu(\mathcal T)$ 表示最少生成元数。

## Proof Strategy

先直接核相对中心和边界，随后以两次独立的高度一延拓处理原积分与整除微分。上同调不使用未经证明的非平坦基变换交换，而从相对节点环的两项复形、边界短正合列和乘 $\pi$ 序列逐项计算。

## Dependency Map

1. 相对八吹起与单位条件 $\Rightarrow$ 光滑正常的 $\mathcal S$、几何整剩余纤维、相对边界与法丛帧。
2. 域上 T1、原 Laurent 整性及 D1 $\Rightarrow$ 原截面全模型延拓、无基点生成性、剩余复合；逐纤维平坦性 $\Rightarrow$ G1。
3. 相对法丛帧 $\Rightarrow$ 边界两项复形；曲面消失结果与原边界单位截面 $\Rightarrow$ 扭子过滤及 $j=r$ 正合列；投影公式与乘 $\pi$ 序列 $\Rightarrow$ G2。
4. D2 与局部自由微分层的高度一交性质 $\Rightarrow$ G3a；逐项系数及 D2 非零性 $\Rightarrow$ G3b–c。G2、G3 的数值由各自论证得到，不假设典范模同构。

## Proof

### Step 1. 八个中心是相对截面，不发生特化碰撞

四个原始位置为 $(\infty,1),(0,\infty),(0,0),(\infty,\infty)$。它们在任何剩余特征下仍互异。先实施四次节点吹起，其中 $(0,0)$ 处的第二次位于第一次例外与 $y=0$ 的交截面。随后四个非节点中心分别位于

$$
C_{x\infty}:y=1,\quad E_{2,1}:xy=t,\quad
E_{3,2}:x^2/y=t,\quad E_{4,1}:y/x=s.
$$

这四个分量互异，坐标的节点值是 $0,\infty$。$1,t,t,s$ 是 $\mathcal O$ 中的单位，故任何特化都不使末次中心变成节点。即使 $\bar s=1$、$\bar t=1$ 或 $\bar t=\bar s$，相等的是不同分量上的坐标值，不是同一个中心。特征 $2$ 时 $-1=1$ 也不使两个原始位置或边界节点合并。

在截面中心的两参数图内，理想为 $(u,w)$；吹起图为 $w=uv$ 和 $u=wv'$，均为相对光滑二维图，且这种显式描述与基变换相容。因此每步是光滑相对曲面上正则截面的吹起。射影性逐次保持，泛、剩余纤维恢复指定的域上八吹起模型。总空间及剩余纤维分别整，后者几何整且有理。

节点吹起用例外分量替换一个边界节点；光滑边界点吹起不把末次例外列入边界。由相对典范除子公式，两类操作均保持选定的约化边界反典范。所有节点是互异横截截面，各分量为 $\mathbb P^1_{\mathcal O}$。故 $\mathcal D$ 是相对八分量 SNC 环且

$$\mathcal D\sim-K_{\mathcal S/\mathcal O}.$$

### Step 2. 高度一延拓针对的是原截面，且涵盖全部高度一素点

$\mathcal S$ 光滑于正则 DVR，故正则、正常。把原 $I_r$ 当作 $\mathcal L_r$ 的有理截面，而非当作全 $\mathcal S$ 上的正则函数。

水平高度一素点位于泛纤维，域上 T1 的极除子恰为 $rD_K$，因而该线丛截面在这些点正则。唯一竖直高度一素点是整剩余曲面的泛点；它位于原 Laurent 环面，那里 $\mathcal L_r$ 由 $1$ 平凡化，$I_r$ 的系数属于 $\mathcal O$，故也正则。

在正常 Noetherian 整环上，有限 reflexive 模等于其全部高度一局部化之交。局部可逆层满足此条件，因而取得唯一全局截面。所引性质及证明已实读：[Stacks Lemma 15.24.18, tag 0AVB](https://stacks.math.columbia.edu/tag/0AVB)。这里不需从末端图中的有限极限猜测正则性，也没有遗漏可能位于特殊纤维更高余维的点。

小阶积分 $J$ 是 $\mathcal O_{\bar{\mathcal S}}(m\bar{\mathcal D})$ 的全局截面，故 $J^N$ 属于 $\bar{\mathcal L}_r$。D1 在稠密环面给出的 $\bar I_r=J^N$ 是同一线丛截面的等式；整曲面上的局部自由层没有支持在真闭集上的非零截面，所以等式延至整个剩余曲面。

### Step 3. 全模型生成性、射影平坦态射与精确剩余重数

考虑评价映射

$$\mathcal O_{\mathcal S}^{\oplus2}\xrightarrow{(1,I_r)}\mathcal L_r.$$

泛纤维上由 T1 满射；剩余纤维上它是小阶 pencil 两截面的 $N$ 次幂，故在每个点至少有一个截面生成。其相干余核在泛纤维消失，且在每个剩余点模 $\pi$ 为零，局部 Nakayama 引理给余核为零。由此得到态射 $f_r$。$\mathcal S$ 对 $\mathcal O$ 射影且 $\mathbb P^1_{\mathcal O}$ 分离；图像闭浸入与基变换的射影投影说明 $f_r$ 本身射影。

截面 $1$ 的零除子是 $r\mathcal D$，所以 $f_r^{-1}(\infty)=r\mathcal D$。剩余态射的标准齐次坐标为小阶截面的 $N$ 次幂，给出严格的 $\kappa$-态射等式

$$\bar f_r=\operatorname{Pow}_N\circ f_m.$$

$\operatorname{Pow}_N$ 在仿射坐标中对应 $\kappa[c]\to\kappa[h]$、$c\mapsto h^N$，且保持常数；后者是以前 $N$ 个幂为基的自由模，无穷图亦然。因此它有限平坦，次数为 $N$。作者保留了它与非平凡剩余域上的绝对 Frobenius 的区别。

域上的原 pencil 与小阶 pencil 都是整曲面到正则曲线的主导态射。目标非泛点的局部环是 DVR，其非零元素在源局部整环中仍非零；源作为该 DVR 模无扭，故平坦。目标泛点处则是域，不需另加条件。因而基底的泛、闭两个纤维上的 $f_r$ 都平坦。总空间对 $\mathcal O$ 平坦且有限呈示，目标对 $\mathcal O$ 有限型；以结构层应用逐纤维平坦判据得到 $f_r$ 平坦。判据的命题及证明已实读：[Stacks Theorem 37.16.2, tag 039C](https://stacks.math.columbia.edu/tag/039C)。

作几何剩余域扩张并固定有限 $c=h^N$。方程准确为

$$J^N-c=(J-h)^N.$$

域上 T1 保证 $f_m^{-1}(h)$ 是几何整约化 Cartier 纤维，故原剩余纤维是它的 $N$ 倍，没有额外支撑。光滑曲面上该局部方程的幂仍是非零因子，所得 Cartier 曲线为 Cohen–Macaulay，因而没有嵌入分量。无穷处也拉回局部参数的 $N$ 次幂，但应保留

$$Nf_m^{-1}(\infty)=Nm\bar{\mathcal D}=r\bar{\mathcal D}.$$

因此有限几何支撑上的重数为 $N$；无穷边界每个分量的重数为 $r$，并不是一律把约化边界乘 $N$。作者 G1 正是前一种准确表述。G1 得证。

### Step 4. 相对边界法丛与两项复形

按 N 指定的有向环和 Laurent 帧，四个非平凡传播比依次为

$$-1/t,\quad-1,\quad-1/s,\quad-t,$$

其余四个为 $1$。每个因子在 $\mathcal O$ 中可逆，乘积严格为 $s^{-1}$。这些是实际整环上的帧计算，不是仅根据两个域上限制猜出一个相对线丛。四个受末次吹起影响的分量用相应一次消失因子、其余四个用单项式帧平凡化，张量幂沿用各帧的幂。即使剩余特征为 $2$，四个负号消去后的同一恒等式仍成立。

节点处的局部模型为 $\mathcal O[u,v]/(uv)$，有从本环到两分支之和、再取节点差值的正合列。张量可逆层并对八个节点求和，得到全局节点正规化短正合列。各分量上为平凡线丛，且 $H^0(\mathbb P^1_{\mathcal O},\mathcal O)=\mathcal O$、正次数上同调为零。故

$$R\Gamma(\mathcal D,\mathcal N^j)\simeq[\mathcal O^8\to\mathcal O^8].$$

前七个粘合比用单位基变换消去；剩余一个是 $s^{-j}$，复形化为

$$[\mathcal O\xrightarrow{1-s^{-j}}\mathcal O].$$

当 $1\le j<r$ 时，$s^j\ne1$ 是特征零整环中的陈述，故该乘法单射，即使它模 $\pi$ 变成零也仍单射。因此

$$H^0(\mathcal D,\mathcal N^j)=0,\qquad
H^1(\mathcal D,\mathcal N^j)=\mathcal O/(1-s^j).$$

当 $j=r$ 时微分为零，两个上同调均为 $\mathcal O$。这里最容易错误地把模 $\pi$ 的 kernel 当成整环上的 kernel；作者没有作此混淆。

### Step 5. 曲面上同调消失、扭子过滤及末端限制满射

射影性给所有 $H^i(\mathcal S,\mathcal L_n)$ 有限生成。特殊纤维是光滑有理曲面，故 $H^1(\bar{\mathcal S},\mathcal O)=0$。任意 $n\ge0$ 时，Serre 对偶把 $H^2(\bar{\mathcal S},\bar{\mathcal L}_n)$ 对偶于

$$H^0(\bar{\mathcal S},\mathcal O(-(n+1)\bar{\mathcal D})).$$

非零有效 $\bar{\mathcal D}$ 与 ample 除子交数正，所显示负除子类与其交数负，不可能有非零有效代表，故该空间为零。这是在任意特征的光滑射影曲面上应用 Serre 对偶及整数交数，没有除以剩余特征。

从乘 $\pi$ 的短正合列得到 $H^2(\mathcal S,\mathcal L_n)/\pi=0$，有限性与 Nakayama 给 $H^2(\mathcal S,\mathcal L_n)=0$；同理 $H^1(\mathcal S,\mathcal O)=0$。$H^0(\mathcal S,\mathcal O)$ 有限、无扭、泛秩一，常数 $1$ 模 $\pi$ 非零，故是以 $1$ 为基的自由秩一模。

对边界短正合列

$$0\to\mathcal L_{j-1}\to\mathcal L_j\to\mathcal N^j\to0$$

取上同调，Step 4 给 $1\le j<r$ 时

$$H^0(\mathcal S,\mathcal L_j)=\mathcal O\langle1\rangle,$$

$$0\to H^1(\mathcal S,\mathcal L_{j-1})
\to H^1(\mathcal S,\mathcal L_j)
\to\mathcal O/(1-s^j)\to0. \tag{C1}$$

从 $H^1(\mathcal S,\mathcal O)=0$ 开始归纳，中间各模都是有限长扭子模。

在 $j=r$ 时必须检查连接同态，不能仅凭 $\mathcal N^r$ 平凡就断言它为零。Step 3 的全模型生成性正好提供这一步：截面 $1$ 在 $\mathcal D$ 上限制为零，所以 $I_r|_{\mathcal D}$ 在每一点生成 $\mathcal N^r$。这包括特殊纤维的全部点，不只是泛纤维的非零限制。以该单位截面平凡化 $\mathcal N^r$，限制映射向 $H^0(\mathcal D,\mathcal N^r)=\mathcal O$ 满射。因此

$$H^0(\mathcal S,\mathcal L_r)=\mathcal O\langle1,I_r\rangle,$$

$$0\to H^1(\mathcal S,\mathcal L_{r-1})
\to H^1(\mathcal S,\mathcal L_r)\to\mathcal O\to0. \tag{C2}$$

商模自由，故 (C2) 作为 $\mathcal O$-模正合列非典范分裂；核是全部扭子模 $\mathcal T$。通过 (C1) 的单射识别子模，得到作者的 $\mathcal T_j$ 过滤及全部所列商。这里没有把 (C1) 中的扩张作任何分裂。

### Step 6. 长度与 Fitting 理想

由于 $s$ 是特征零中的本原 $r$ 次根，在 $\mathcal O$ 中有

$$\prod_{j=1}^{r-1}(1-s^j)=r.$$

(C1) 中的长度可加，故

$$\operatorname{length}_{\mathcal O}\mathcal T
=\sum_{j=1}^{r-1}v_\pi(1-s^j)=v_\pi(r)=ae.$$

其中 $m$ 为 $\mathcal O$ 单位。若用 DVR 有限长模结构定理写作某个非典范直和 $\bigoplus_i\mathcal O/(\pi^{b_i})$，其零阶 Fitting 理想由对角呈示矩阵的行列式生成，等于 $(\pi^{\sum_i b_i})$。这只是计算 Fitting 理想，不是断言 (C1) 按其指定商分裂。因此

$$\operatorname{Fitt}_0(\mathcal T)=(\pi^{ae})=(r)=(p^a).$$

不需要指定 $\pi$ 的某种圆分规范，也不需要由 $ae$ 猜测初等因子。

### Step 7. 实际基变换缺陷与最少生成元数

小阶原 pencil 给 $\mathcal O(m\bar{\mathcal D})=f_m^*\mathcal O_{\mathbb P^1}(1)$。所以

$$\bar{\mathcal L}_r=f_m^*\mathcal O_{\mathbb P^1}(N).$$

消费 T1 的 $f_{m*}\mathcal O=\mathcal O$ 后，投影公式给

$$H^0(\bar{\mathcal S},\bar{\mathcal L}_r)
=\kappa\langle1,J,\ldots,J^N\rangle,$$

维数为 $N+1$。在非代数闭的 $\kappa$ 上，上述等式由其本域构造及域扩张上的忠实平坦下降成立；不需增加 $\kappa=\mathbb F_p$ 的假设。

乘 $\pi$ 序列的次数零到一段准确为

$$0\to H^0(\mathcal S,\mathcal L_r)/\pi
\to H^0(\bar{\mathcal S},\bar{\mathcal L}_r)
\to H^1(\mathcal S,\mathcal L_r)[\pi]\to0.$$

(C2) 的自由商没有 $\pi$-扭子，最右项为 $\mathcal T[\pi]$。最左项的像恰为 $\kappa\langle1,J^N\rangle$，维数二。因此

$$\dim_\kappa\mathcal T[\pi]=N-1.$$

每个非零 DVR 初等因子对 $\mathcal T[\pi]$ 与 $\mathcal T/\pi\mathcal T$ 各贡献一维，Nakayama 引理据此给

$$\mu(\mathcal T)=\dim_\kappa\mathcal T/\pi\mathcal T=N-1.$$

这是由实际基变换计算的维数，不是把长度 $ae$ 误报为 $N-1$。二者仅在所有初等因子长度为一时相等。过滤中 $1-s^j$ 非单位恰当且仅当 $m\mid j$，所以恰有 $N-1$ 个非零商；这与上述计算一致，但不能单凭这些商的个数决定扩张或全部初等因子。G2 得证。

### Step 8. 整除微分延至全开放模型及其准确非饱和理想

在 $\mathcal U$ 上 $I_r$ 是正则函数，故 $dI_r$ 正则。设 $\alpha=p^{-a}dI_r$，先视为有理相对一形式。在全部水平高度一处，$p$ 可逆且 $dI_r$ 正则；在唯一竖直高度一处，D2 的 Laurent 环整性保证 $\alpha$ 正则。$\Omega^1_{\mathcal U/\mathcal O}$ 因相对光滑而局部自由，Step 2 所用高度一交性质适用，给唯一全局正则延拓。这特别覆盖四条末端相对仿射直线及其特殊点。

约化后，局部自由微分层基变换为 $\Omega^1_{\bar{\mathcal U}/\kappa}$。$J$ 在全 $\bar{\mathcal U}$ 正则，所以 $H^\sigma dJ$ 也正则。D2 在稠密环面给出的等式，在整剩余曲面上的局部自由层中唯一延拓，故

$$\bar\alpha=H^\sigma dJ$$

在整个 $\bar{\mathcal U}$ 成立，不删除末端线上的任何有限点。

在任意局部自由基中逐项取系数，并把左侧理想取到剩余结构层中的像，立即得到

$$\overline{\mathfrak c(\alpha)}=(H^\sigma)\mathfrak c(dJ).$$

可逆换基不改变系数生成理想。这里不把理想的抽象张量积误认为其在剩余环中的嵌入，也不把乘积理想替换成两个根集。

D2 给 $H^\sigma dJ$ 在剩余环面不为零；它因而在剩余曲面的泛点不为零。因此 $\alpha$ 在该 DVR 泛点的至少一个系数是单位，而

$$dI_r=p^a\alpha$$

的公共 $\pi$-阶准确为 $ae$。结合 Step 6 的独立计算得到 G3c。这个证明没有从逐闭点提升赋值推出统一阶，也没有构造或需要构造 $\mathcal T$ 与微分对象的典范同构。

除以公共 $p^a$ 因子不等于 $\pi$-饱和。一般局部理想 $(\pi,z)$ 本来就没有公共因子 $\pi$，但它的 $\pi$-饱和是单位理想，约化像却是 $(z)$；这说明两种操作逻辑上不同，并非提供本模型的额外初等因子计算。作者 G3b 保留了特殊纤维上的含重数零理想，允许其中出现曲线。G3 得证。$\square$

## Corrections or Missing Assumptions

没有必需的数学修正或额外假设。下列边界必须在后续引用中保持，均已在作者 G 中明确或由其式子准确表达：

1. 中心必须按相对截面吹起且 $t$ 为单位；不推广到非单位参数。剩余根单位阶下降不改变中心数或曲面分量数。
2. $I_r$ 在完整模型上是 $\mathcal L_r$ 截面；只有在 $\mathcal U$ 上才作为正则函数求微分。
3. $j=r$ 时限制满射来自原 pencil 的全相对无基点性，不能用“法丛平凡”替换；这是过滤闭合的实质接口。
4. 仅 (C2) 因自由商而可非典范分裂；不宣称扭子过滤按 $\mathcal O/(1-s^j)$ 分裂。
5. 有限剩余几何纤维重数为 $N$，无穷纤维为 $r\bar{\mathcal D}$；保持 $\operatorname{Pow}_N$ 与绝对 Frobenius 的区别。
6. 最少生成元数是 $N-1$，长度是 $ae$；整除阶是剩余曲面泛点处的公共阶，既非每个闭点提升赋值，也非 $\pi$-饱和结果。

## Open Risks

在本次限定 G1–G3 的数学命题内未留下未闭合步骤。T1 和 D1–D3 是已接受的显式依赖，本报告没有另行审查它们的来源新意或改写其旧接受。

本文不计算扭子模全部初等因子或边界扩张类，不构造稳定／半稳定约化、野导子、vanishing cycles、能级提升的下一阶整除或超奇异处更高阶 jet，不证明整个混合特征回返在全部闭纤维上的延拓。它们不是 G1–G3 的已证推论，也不作为本次 PASS 的隐含附加主张。

## 实际阅读与输入绑定

唯一待核作者输入的 SHA-256 必须精确为：

`59b308f605832d82e00720c5a3a7871c862698e194503ff3b289da592ced28e0`

| 文件 | 本轮实际阅读范围 | SHA-256 |
|---|---|---|
| [G 诊断 V1](PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_DIAGNOSTIC_V1_20260909.md) | 全文 1–254 行；核查 G1–G3 与全部六个证明步骤 | `59b308f605832d82e00720c5a3a7871c862698e194503ff3b289da592ced28e0` |
| [D 诊断 V1](PAPER30_QPI_CYCLOTOMIC_DIFFERENTIAL_DIAGNOSTIC_V1_20260909.md) | 全文 1–268 行；消费已接受 D1、D2，不重审 D1–D3 | `e2f032ff1197d415be611670e3d233efd7f6ead0d7dbe16b05f796ed42f43652` |
| [P 作者入口](PAPER30_QPI_SYMPLECTIC_POLAR_ENTRY_V1_20260908.md) | 全文 1–275 行；实际使用中心与 Step 2–3 的相对化 | `61d2b0ace7003e19ff1e81242e4080402049d98c024657b94d9b812086f358b3` |
| [N 作者入口](PAPER30_QPI_BOUNDARY_NORMAL_BUNDLE_ENTRY_V1_20260908.md) | 全文 1–284 行；实际使用 Step 1–7 的帧、传播比和节点环 | `8234b5584adba10ec02adb0269300b0c5191b5445fca345e28e1eb5171c12469` |
| [brief V2](PAPER30_QPI_CANDIDATE_BRIEF_V2_20260909.md) | 定向定位后实读 35–140 行，即 §2 对象及 T1；没有通读整份候选或 T2–T7 | `b8f1ca66927b977b05a2996e42d299390d6a895d1a3378119d1be5415d70a00f` |

外部仅为本次标准工具核对而实读 Stacks 0AVB、039C 的命题及证明；未以外部检索开展一般查新。本轮没有读取旧 47 件正式输入、重新扫描历史构建树、数值抽样代替全参数证明、打分、预测页数或创建论文项目。

核查者亲读 proof-writer 技能全文，并按其要求保留准确主张、假设、依赖、证明和边界。唯一写入对象是本新核查文件；作者 G、P、N、D、brief、旧票、锁和产物均未修改。
