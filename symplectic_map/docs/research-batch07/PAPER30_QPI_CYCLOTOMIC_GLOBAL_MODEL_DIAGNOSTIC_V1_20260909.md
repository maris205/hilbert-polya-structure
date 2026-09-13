# Paper30 qPI：圆分降阶的完整模型与上同调缺陷诊断 V1

日期：2026-09-09。作者：主控 /root，可用 Codex AI。
类型：有界作者证明，不是正式候选、独立接受、稳定约化定理或论文稿。
proof_status：PROVABLE AS STATED（作者判断，等待非作者检查）。

## 1. 目标与准确假设

本件检验[整除微分诊断 D1–D3](PAPER30_QPI_CYCLOTOMIC_DIFFERENTIAL_DIAGNOSTIC_V1_20260909.md)
在原完整八吹起模型上是否有真正的几何接口，并计算原 pencil 的上同调基变换缺陷。
不是只在环面上重命名 Hasse 系数，也不由本件推断已足以独立立项。

取任意素数 $p$、整数 $a\ge1,m\ge1$，$p\nmid m$，
$$N=p^a,\qquad r=mN,\qquad s=\zeta_r,\qquad
\mathcal O=\mathbb Z[\zeta_r]_{\mathfrak p},\quad \mathfrak p\mid p.$$
记 $K=\operatorname{Frac}(\mathcal O)$、$\kappa=\mathcal O/\pi$、$e=v_\pi(p)$，
其中 $\pi$ 为任一 DVR 参数。固定任意 $t\in\mathcal O^*$。
横线表示剩余约化，$\eta=\bar s$ 的精确阶为 $m$。
这里先固定单位 $t$，不把以下断言默认为任意非单位时间参数或任意奇异基环的定理。

在 $\mathbb P^1_{\mathcal O}\times_{\mathcal O}\mathbb P^1_{\mathcal O}$ 上，
按下表的**截面**而不是只按泛纤维闭点逐次吹起，定义 $\mathcal S$。

| 簇 | 中心的次序／局部说明 | 末端图 |
|---|---|---|
| 1 | $(x^{-1},y-1)=(0,0)$ | $x=u^{-1},\ y=1+uv$ |
| 2 | $(x,y^{-1})=(0,0)$，随后 $(u,xy)=(0,t)$ | $x=u(t+uv),\ y=u^{-1}$ |
| 3 | $(x,y)=(0,0)$；再吹第一次例外与 $y=0$ 的交截面；随后 $(u,x^2/y)=(0,t)$ | $x=u(t+uv),\ y=u^2(t+uv)$ |
| 4 | $(x^{-1},y^{-1})=(0,0)$，随后 $(u,y/x)=(0,s)$ | $x=[u(s+uv)]^{-1},\ y=u^{-1}$ |

第 2、4 簇相应的 $u=1/y$，第 3 簇最后的 $u=y/x$。
等价地先做四次边界节点吹起，再在四个不同边界分量的坐标 $1,t,t,s$ 处吹起。
这些坐标全是单位，所以在任一纤维上都不撞边界节点；不因 $s$ 的剩余阶下降增加或合并中心。
令 $\mathcal D$ 为四条坐标边界与四条中间节点例外的最终严格变换之和，
令 $\mathcal U=\mathcal S\setminus\mathcal D$，$\mathcal L_n=\mathcal O_{\mathcal S}(n\mathcal D)$。

$I_r$ 保持上述 D 诊断及[brief V2 §2](PAPER30_QPI_CANDIDATE_BRIEF_V2_20260909.md)
的原矩阵、原迹与原能级规范；不将 $I_r$ 替换成任意有理函数。
记 $J=I_{m,\eta}(x,y;\bar t)$、$T=\bar t^m$、$\varepsilon=(-1)^{m+1}$，
$H=H_p(T,J;\varepsilon)$，$\sigma=(N-1)/(p-1)$。
所有相对微分均固定 $\mathcal O$，特别固定 $t$。

采用已接受 T1 的域上结果，分别应用于 $K$ 上阶 $r$ 以及 $\kappa$ 上阶 $m$；
若需验证几何性质，先到代数闭域再下降。**并不把旧 T1 直接当作混合特征结论。**

## 2. 准确结论

### G1. 同一个完整模型上的平坦退化

$\mathcal S/\mathcal O$ 光滑射影，相对维数二；$\mathcal D$ 是相对八分量 SNC 环，
且 $\mathcal D\sim-K_{\mathcal S/\mathcal O}$。
原截面 $1,I_r$ 生成无基点 pencil，定义射影平坦态射
$$f_r:\mathcal S\longrightarrow\mathbb P^1_{\mathcal O},\qquad
f_r^{-1}(\infty)=r\mathcal D.$$
其泛纤维上的态射是原最小完整 $r$ 阶 pencil；剩余态射准确为
$$\bar f_r=\operatorname{Pow}_N\circ f_m,\qquad
f_m=J:S_{\bar t,\eta}\longrightarrow\mathbb P^1_\kappa,
\quad \operatorname{Pow}_N([b_0:b_1])=[b_0^N:b_1^N]. \tag{G1}$$
$\operatorname{Pow}_N$ 是保持 $\kappa$ 常数的幂态射，可作标准坐标下的相对 Frobenius 解释；
若 $\kappa\ne\mathbb F_p$，不将它混同于同时对常数取幂的绝对 Frobenius。
每个几何剩余能级 $c=h^N$ 的概形纤维为 $N\,f_m^{-1}(h)$，包括 $h=\infty$；
有限约化支撑为旧 T1 的几何整曲线，重数准确为 $N$。

### G2. 完整线性系跳跃的准确长度

有
$$H^0(\mathcal S,\mathcal L_r)=\mathcal O\langle1,I_r\rangle,\qquad
H^0(\bar{\mathcal S},\bar{\mathcal L}_r)=\kappa\langle1,J,\ldots,J^N\rangle. \tag{G2a}$$
实际基变换映射的像只有 $\kappa\langle1,J^N\rangle$，余核维数为 $N-1$。
设
$$\mathcal T=H^1(\mathcal S,\mathcal L_r)_{\mathrm{tors}}.$$
则
$$H^1(\mathcal S,\mathcal L_r)\simeq\mathcal O\oplus\mathcal T,
\qquad \operatorname{length}_{\mathcal O}\mathcal T=v_\pi(r)=ae,
\qquad \operatorname{Fitt}_0(\mathcal T)=(r), \tag{G2b}$$
第一项分裂是 $\mathcal O$-模的非典范分裂。
更准确地，$\mathcal T$ 有由边界递增得到的过滤
$$0=\mathcal T_0\subset\mathcal T_1\subset\cdots\subset\mathcal T_{r-1}=\mathcal T,
\qquad \mathcal T_j/\mathcal T_{j-1}\simeq\mathcal O/(1-s^j). \tag{G2c}$$
零商允许出现。$\mathcal T$ 的最少生成元数为 $N-1$。
**过滤不声称分裂**；本件没有计算所有 elementary divisors 或边界扩张类。

### G3. 完整开放初值空间上的微分与临界理想

$\alpha=p^{-a}dI_r$ 唯一延拓为 $\Gamma(\mathcal U,\Omega^1_{\mathcal U/\mathcal O})$ 中的正则一形式，
并在整个 $\bar{\mathcal U}$（含四条完整末端仿射直线）上满足
$$\bar\alpha=H^\sigma dJ. \tag{G3a}$$
若 $\mathfrak c(\nu)$ 表示一形式 $\nu$ 在局部自由基中的系数理想，则
$$\overline{\mathfrak c(\alpha)}=(H^\sigma)\,\mathfrak c(dJ). \tag{G3b}$$
左边指理想在剩余结构层中的像。
$dI_r$ 的最大统一 $\pi$-幂整除阶仍为 $ae$，于是有准确数值／理想对应
$$\operatorname{ord}_{\bar{\mathcal U}}(dI_r)
=\operatorname{length}_{\mathcal O}\mathcal T=ae,
\qquad \operatorname{Fitt}_0(\mathcal T)=(p^a). \tag{G3c}$$
该阶数指沿整个剩余曲面的泛点取局部自由系数的公共阶数，不是每个闭点的提升赋值。
除去公共 $p^a$ 因子**不是**对临界理想作 $\pi$-饱和；G3b 仍可能有竖直曲线。
本件不声称 G3c 来自已构造的两者之间的典范模同构。

## 3. 依赖与证明策略

1. 相对模型由实读 [P 的 Step 2–3](PAPER30_QPI_SYMPLECTIC_POLAR_ENTRY_V1_20260908.md)
   和 [N 的 Step 1–7](PAPER30_QPI_BOUNDARY_NORMAL_BUNDLE_ENTRY_V1_20260908.md) 的单位坐标构造。
   本轮主控全文读这两份作者文件，不重新撤销或重审它们的旧域上接受。
2. G1：构造相对光滑模型；用整性与余维一延拓取得原截面，再逐纤维验证无基点及平坦。
3. G2：计算相对节点环上线丛上同调，用边界短正合列得到过滤；
   最后用完整 $I_r$ 在边界的单位限制及 $\prod_{j=1}^{r-1}(1-s^j)=r$ 封闭长度。
4. G3：D2 的环面整性结合正常模型上的向量丛延拓；不是重做 Cartier 公式。
5. 已有 T1 的完整 pencil 与 $f_{m*}\mathcal O=\mathcal O$ 用于 G2a 的特殊纤维；
   没有把实际混合特征上同调直接套成可交换基变换。

## 4. 证明

### Step 1. 相对模型没有中心碰撞

在任一中心附近取相对正则参数 $a,b$，中心是截面 $a=b=0$。
其吹起的两张图为 $(a,b/a)$ 与 $(a/b,b)$；它们是相对仿射平面型光滑图。
各步中心在相应光滑图上仍为截面，最后中心坐标为单位，故全部八步在 $\mathcal O$ 上实施。
吹起射影性和上述图分别给相对射影性与光滑性，基变换后恢复相同的八个域上中心。
节点与光滑边界点的吹起计算同 P Step 2：节点吹起保留新单极边界，
光滑点吹起不把末次例外列入边界。因此相对八环与相对反典范等式成立。
特殊纤维是一张光滑几何整有理曲面，不是 $N$ 张曲面的并。

### Step 2. 原截面的整性与全模型无基点

将 $I_r$ 看作 $\mathcal L_r$ 的有理截面。
在每个水平余维一处，它由已接受域上极除子公式正则；
唯一竖直余维一分量是 $\bar{\mathcal S}$，其泛点位于原环面，而 $I_r$ 的 Laurent 系数在 $\mathcal O$ 中。
故该有理截面在全部余维一处正则。
$\mathcal S$ 正常、$\mathcal L_r$ 可逆，余维一交性质将它唯一延拓为全局正则截面。
所用性质是正常 Noetherian 环上有限 reflexive 模等于其全部高度一局部化之交，
见实际核读的 [Stacks 0AVB](https://stacks.math.columbia.edu/tag/0AVB)；这里模局部为秩一自由模。

由 D1，余维零的环面上有 $\bar I_r=J^N$。
两边现均为 $\bar{\mathcal L}_r$ 的正则截面，故在整曲面上相等。
在泛纤维，$1,I_r$ 无共同零点由 T1 给出；
在剩余纤维，两个截面分别是小阶 pencil 的两个截面的 $N$ 次幂，因此也无共同零点。
若相对 cokernel 非零，其支撑中某点映到泛点或闭点，会违反对应纤维上的生成性与 Nakayama。
故两个截面生成整个 $\mathcal L_r$，定义 $f_r$。
截面 $1$ 的零除子就是 $r\mathcal D$，取得无穷纤维等式与 G1 的复合公式。

幂态射在几何点 $c=h^N$ 上拉回局部参数为 $(J-h)^N$；在无穷坐标也同样取 $N$ 次幂。
这证明所有概形纤维的重数，不只比较点集。
两个域上的 $f_r$ 与 $f_m$ 均为整曲面到正则曲线的主导态射：
曲线局部 DVR 的非零元素在曲面局部整环上无扭，所以这些态射平坦。
幂态射有限平坦，故 $\bar f_r$ 也平坦。
$\mathcal S/\mathcal O$ 平坦，所有资料有限呈示；逐纤维平坦判据
[Stacks 039C](https://stacks.math.columbia.edu/tag/039C) 将上述两个纤维的平坦性提升到 $f_r$。
这是在已构造的完整模型上使用该判据，不从环面平坦性猜出完整模型。

### Step 3. 相对节点环的两项复形

令 $\mathcal N=\mathcal O_{\mathcal D}(\mathcal D)$。
N 的指定有向帧与传播比只使用 $1,t,t,s$ 的求逆，因此同一计算在 $\mathcal O$ 中成立，
给 $\lambda(\mathcal N)=s^{-1}$，且各分量的限制是 $\mathbb P^1_{\mathcal O}$ 上的平凡线丛。
这里无需在剩余域倒推出整环上的线丛。

节点正规化短正合列把 $R\Gamma(\mathcal D,\mathcal N^j)$ 表示为
$$[\mathcal O^8\xrightarrow{d_j}\mathcal O^8]$$
（次数零到一）；各 $\mathbb P^1_{\mathcal O}$ 上平凡线丛的高次上同调为零。
逐节点用单位消元把前七个粘合归一为 $1$，消去七个可逆对，剩下
$$[\mathcal O\xrightarrow{1-s^{-j}}\mathcal O]. \tag{8}$$
因而对 $1\le j<r$，$H^0(\mathcal D,\mathcal N^j)=0$，
$$H^1(\mathcal D,\mathcal N^j)=\mathcal O/(1-s^j),$$
而 $j=r$ 时 $H^0=H^1=\mathcal O$。这些是整环上的 kernel/cokernel，
即使 $1-s^j$ 不是单位也不能把非零 torsion cokernel 丢掉。

### Step 4. 曲面上同调与递增过滤

$H^i(\mathcal S,\mathcal L_n)$ 是有限 $\mathcal O$-模，由射影相干上同调有限性给出。
在特殊有理曲面上，$H^1(\bar{\mathcal S},\mathcal O)=H^2(\bar{\mathcal S},\mathcal O)=0$；
可从 $\mathbb P^1\times\mathbb P^1$ 的上同调及逐次光滑点吹起的不变性得到。
对任意 $n\ge0$，Serre 对偶将
$H^2(\bar{\mathcal S},\bar{\mathcal L}_n)$ 对偶于 $H^0(\bar{\mathcal S},\mathcal O(-(n+1)\bar{\mathcal D}))$。
后者为零，因为它与任一 ample 除子的交数为负，不能有非零有效截面。

对 $0\to\mathcal L_n\xrightarrow{\pi}\mathcal L_n\to\bar{\mathcal L}_n\to0$
取长正合列，$H^2/\pi H^2$ 注入上述零群，有限性与 Nakayama 给
$H^2(\mathcal S,\mathcal L_n)=0$。同理 $H^1(\mathcal S,\mathcal O)=0$。
$H^0(\mathcal S,\mathcal O)=\mathcal O$：它有限且无扭，泛纤维秩为一，常数 $1$ 的约化非零，故为基。

现对
$$0\longrightarrow\mathcal L_{j-1}\longrightarrow\mathcal L_j
\longrightarrow\mathcal N^j\longrightarrow0 \tag{9}$$
取上同调。由 Step 3 及 $H^2=0$，对 $1\le j<r$ 有
$$H^0(\mathcal S,\mathcal L_j)=\mathcal O\langle1\rangle,$$
$$0\longrightarrow H^1(\mathcal S,\mathcal L_{j-1})
\longrightarrow H^1(\mathcal S,\mathcal L_j)
\longrightarrow\mathcal O/(1-s^j)\longrightarrow0. \tag{10}$$
故这些 $H^1$ 是有限长模，且构成所需过滤至 $j=r-1$。

在 $j=r$ 时，Step 2 的无基点性说明 $I_r|_{\mathcal D}$ 是 $\mathcal N^r$ 的处处非零截面。
以其平凡化作为 $H^0(\mathcal D,\mathcal N^r)=\mathcal O$ 的基，限制映射满射。
因此 (9) 的连接同态为零，给
$$H^0(\mathcal S,\mathcal L_r)=\mathcal O\langle1,I_r\rangle,$$
$$0\longrightarrow H^1(\mathcal S,\mathcal L_{r-1})
\longrightarrow H^1(\mathcal S,\mathcal L_r)\longrightarrow\mathcal O\longrightarrow0. \tag{11}$$
商自由，(11) 作为模序列分裂，前项恰是后项的全部扭子模 $\mathcal T$。
这证明 G2c，未假定 (10) 中的扩张分裂。

在 $K$ 中的多项式恒等式
$\prod_{j=1}^{r-1}(X-s^j)=(X^r-1)/(X-1)$ 代入 $X=1$ 得
$$\prod_{j=1}^{r-1}(1-s^j)=r.$$
式 (10) 的长度可加性给
$$\operatorname{length}\mathcal T=\sum_{j=1}^{r-1}v_\pi(1-s^j)=v_\pi(r)=ae.$$
DVR 上有限长模的零阶 Fitting 理想是长度对应的参数幂，故 G2b 成立。

### Step 5. 基变换缺陷的维数不是长度

在特殊曲面上，$\bar{\mathcal L}_r=f_m^*\mathcal O_{\mathbb P^1}(N)$。
T1 给 $f_{m*}\mathcal O=\mathcal O$，投影公式于是给 G2a 的第二个等式及维数 $N+1$。
这也是为何 $\bar f_r$ 不是特殊纤维的最小完整 pencil。

对 Step 4 的乘 $\pi$ 序列再取次数零到一，得准确序列
$$0\longrightarrow H^0(\mathcal S,\mathcal L_r)/\pi
\longrightarrow H^0(\bar{\mathcal S},\bar{\mathcal L}_r)
\longrightarrow\mathcal T[\pi]\longrightarrow0. \tag{12}$$
第一项的像由 $1,\bar I_r=J^N$ 生成，故 $\dim_\kappa\mathcal T[\pi]=N-1$。
对 DVR 上有限长模，$\dim\mathcal T[\pi]=\dim\mathcal T/\pi\mathcal T$
等于最少生成元数；这不等于长度 $ae$，除非 elementary divisors 全是一阶。
本件不由 (12) 猜出这些 elementary divisors 的完整分布。

### Step 6. 整除微分跨过四条末端线

在 $\mathcal U$ 上 $I_r$ 是正则函数，故 $dI_r$ 为正则相对一形式。
在泛纤维 $p$ 是单位，$p^{-a}dI_r$ 正则；
在唯一竖直余维一泛点，D2 的 Laurent 环整性保证它正则。
$\Omega^1_{\mathcal U/\mathcal O}$ 局部自由，套用同一个余维一交性质，
取得唯一全局延拓 $\alpha$，没有把有限极限当作局部正则性。

在剩余曲面，$\bar\alpha$ 与 $H^\sigma dJ$ 都正则，环面上由 D2 相等，
故在全部几何整 $\bar{\mathcal U}$ 相等。
局部任取自由基并逐项取系数，就得到 G3b；基变换矩阵可逆保证系数理想与基无关。
D2 的非零性给准确统一阶 $ae$；Step 4 独立计算 $\mathcal T$ 的长度及 Fitting 理想，得到 G3c。证毕。

## 5. 边界与来源扣除

本件确实构造同一个 $\mathcal O$-光滑完整曲面、原平坦 pencil、所有几何剩余能级的重数，
以及上同调扭子过滤与长度；它不是对任意能级提升的稳定／半稳定模型分类。
它未计算横截能级曲线的最小分裂扩张、野导子、vanishing cycles、全 ramified jet，
未证明整个混合特征回返的所有闭纤维延拓，也没有计算超奇异处下一阶微分。
保持原能级得到非约化特殊纤维，与换基后可能出现的约化稳定模型是不同问题。

G3 的 Hasse 次幂是标准 Cartier／高阶 Hasse–Witt 机制；
本轮来源追加核查还指出 Vlasenko 的一般同余覆盖该乘子的迭代部分。
G1 的延拓／平坦工具、G2 的边界长正合列／DVR 长度同样是标准工具，不能按步骤数计新发现。
这里尚待独立检查和查新的准确剩余，是原圆分 qPI 上的完整模型、
指定线性系基变换缺陷与原整除微分的同一规范识别；没有宣称该组合全球未见。

主控本轮完整读 P（275 行）、N（284 行）及 D 诊断（268 行），
实际使用 brief V2 §2 与 T1–T3，不重开旧 47 件正式输入。
外部标准性质实读 Stacks 0AVB、039C 的命题与证明；另查 07VJ、02KE，
本证明用乘 $\pi$ 短正合列直接展示缺陷，没有假定通常的非平坦基变换可交换。
采用 formula-derivation 固定原 pencil 与相对微分，proof-writer 分离模型、上同调和微分三个证明义务。
无数值拟合、无试排／页数预测、无正式四门分数；未改旧证明、票、锁、PDF 或项目。
