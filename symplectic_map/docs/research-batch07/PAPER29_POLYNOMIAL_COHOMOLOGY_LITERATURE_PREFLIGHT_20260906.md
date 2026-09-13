# Paper29 新方向：多项式余同调与有限周期概形的独立文献预筛

日期：2026-09-06。范围：一手文献的精确覆盖、Bousch 后续线索、加性扩张固定域及术语边界。本报告不改既有 STOP，不建立正式 Paper29，也不提前评价尚在完成的主证明稿的最终容量。

## 1. 当前结论

本轮没有找到与下述主张完全相同的一手定理：**对一般多 phase 辛 Hénon 多项式映射，利用一个充分长周期的完整固定点概形，精确判定给定多项式是否为多项式余边界，并给出由次数控制的有效周期。** 这只是有界检索结论，不是排他性新颖性证明。

已经确认的贡献扣除项很明确：

- Bousch 1992 的二次 Hénon 代数已同时拥有有限周期代数、重数信息、无限 bounded-exponent 基、wrapping 和指标平移。二次情形的 word-orbit 余同调描述因而是既有基结构的直接线性代数推论。
- 加性扩张的固定域是否增长，等价于其平移项是否为底差分域中的余边界，是 Karr 的经典常数域判据，不是新扩张理论。
- “有限 Livšic”不是新名称。已有 Hölder/Anosov 理论给出有限周期信息控制的近似余边界；但这不等于当前无双曲性假设、保留非既约结构、得到严格多项式解的判据。

因此适合继续核证的新增核是：**有效的单周期概形余边界检测、一般 Hénon 的单变量右端刚性，以及它导出的特定四维辛 lift 的完整有理固定域。** 不应把一般次数的基重建、word shift 或加性扩张常数域引理重新包装成并列的大创新。随后收到的精确次数滤过 Hilbert 级数、对数周期上界与尖锐性输入，已作为不同于 word 基直接推论的定量主张另作专项检索，见 §8；本报告不代替其独立证明检查。

## 2. 被查对象与不能混淆的量词

令 $K$ 为特征零域，$H_i(x,y)=(p_i(x)-y,x)$，$\deg p_i\ge2$，$F$ 为固定 $k$ 个 phase 的复合。当前研究的线性余同调是

$$
H^1_F(K[x,y])=K[x,y]/(F^*-1)K[x,y].
$$

这里是 $K$-向量空间或群作用模的商，不自动是交换代数的商；$(F^*-1)K[x,y]$ 一般不是理想，也不是代数几何中的 de Rham 或层上同调。

设 $A_n$ 为 $\operatorname{Fix}(F^n)$ 的坐标代数，保留其全部概形结构，$\pi_n$ 为限制。需查新的有限检测陈述为

$$
\pi_n\!\left(\sum_{j=0}^{n-1}g\circ F^j\right)=0\quad\text{in }A_n
\quad\Longleftrightarrow\quad
g=f\circ F-f,\quad f\in K[x,y],
$$

其中 $n$ 足够大且由规范 word 的跨度或多项式次数有效控制。任务输入给出待完成的阈值 $nk>2L$；本报告不把该阈值或尚未定稿的 logarithmic degree bound 认证为已证。

左边不是对所有周期点取平均后得到一个标量零，也不是只在几何点上逐点取值零，更不是已停止方向的周期 multiplier trace。它是一个有限维坐标代数中的元素恒等式。“单周期”应解释为一个 $\operatorname{Fix}(F^n)$ 概形，包含所有周期整除 $n$ 的轨道，不是任选一个周期轨道。

另一个被查陈述是：对 $H_p(x,y)=(p(x)-y,x)$、$\deg p\ge2$、$R\in K[x]$，若

$$
f\circ H_p-f=R(x),\qquad f\in K(x,y),
$$

则恰有 $f=c(x-y)+c_0$、$R=c(p(x)-2x)$。其充分性直接可验；必要性属于当前主证明代理负责的新推导，不能由一般 Livšic 正则性定理直接替代。

## 3. Bousch 1992：完整阅读后的覆盖与扣除

Thierry Bousch，*Algèbres de Hénon*，1992，未发表手稿，13 页。[作者目录](https://www.imo.universite-paris-saclay.fr/~thierry.bousch/preprints/)，[作者原文](https://www.imo.universite-paris-saclay.fr/~thierry.bousch/preprints/alghenon.pdf)。本代理独立全文读完；网页提取失败后，以只读方式读取同一作者 PDF，没有写入工作区。

| 原文位置 | 已有内容 | 当前应如何归属 |
|---|---|---|
| §2，Theorem 1 | 二次周期代数的 square-free monomial 基；明确说明多重点须保留导数信息 | 二次有限概形/有界指数基归 Bousch |
| §5.1，Theorem 1 bis | 无限指标代数的 stable 基及 wrapping | 二次无限 word 基和有限周期兼容性归 Bousch |
| §7 | 右复合 Hénon 等于指标平移 | 二次 permutation-module 结构归 Bousch |
| §3–5，Theorem 3 | multiplication operator trace 所定义的平均最终稳定 | 不等于当前 orbit-sum 元素为零的判据 |

**直接推论，而非原文同式定理：** 若已有基被 $F^*$ 置换，则每个基轨道在余边界商中留下一个坐标；有限支撑系数在该轨道上的总和就是障碍。这解释了为何 word-orbit 描述应写成基定理的应用，而不宜单靠它承担新论文的首创性。

未在原文发现当前单周期概形 iff、一般 $p$ 的单变量有理余边界分类、四维参数 lift 固定域分类。即便如此，新的有限检测证明仍须明确指出它在 wrapping 之外新增了哪条有限环上的无混叠引理及有效性界，不能只说“Bousch 没有写出本句”就视为较大增量。

### 3.1 后续引用检索中的一个容易误判处

Bonnot–Radu–Tanase，*Hénon mappings with biholomorphic escaping sets*，2017，[一手全文](https://doi.org/10.1186/s40627-017-0010-9)，明确采用 Bousch 的方法，但其参考文献第 3 项是 **1994 年的 *Automorphismes des applications de Hénon***，不是 1992 年的 *Algèbres de Hénon*。它研究 escaping set 的双全纯刚性，不能作为当前代数余同调已被处理的证据。

以原题、`alghenon.pdf`、英文题名变体和 Bousch 加 Hénon/cohomology/trace 等组合检索，没有定位到一条可逐项核实的“1992 手稿后续直接给出 scheme-sum 判据”的引用链。这里的结论是**直接后续覆盖未定位**，不是“没有任何引用”或“没有先例”。

## 4. 真正邻近的周期和与 Livšic 文献

### 4.1 Hénon 的轨道和已有精确代数研究，但目标不同

Endler–Gallas，*Reductions and simplifications of orbital sums in a Hamiltonian repeller*，Physics Letters A 352 (2006)，124–128，[作者全文](https://inaesp.org/PublicJG/endler_gallas_orbital_sums_PLA2006.pdf)，[DOI](https://doi.org/10.1016/j.physleta.2006.01.031)。已核全文：研究面积保持二次 Hénon 的周期坐标和及其最小多项式、因式分解和轨道分组；正文主要展示周期不超过 6 的结果。

这使“对 Hénon 周期轨道和做精确代数计算”不能被笼统宣布为新主题。但它没有给任意观测多项式 $g$ 的余边界空间、一个足够长固定点概形上的零检测，也没有给多项式解重建的 iff。只因二者都写 orbit sums，不能判作直接覆盖。

### 4.2 经典与有限 Livšic 的覆盖范围

Pollicott–Sharp，*Livsic theorems, maximizing measures and the stable norm*，Dynamical Systems 19 (2004)，75–88，[出版记录](https://doi.org/10.1080/14689360410001658990)，[作者稿](https://warwick.ac.uk/fac/sci/maths/people/staff/richard_sharp/p2/livsic.pdf)。其有限周期结果控制 Hölder 函数到余边界空间的距离；有限周期信息得到的是定量近似，不是当前环上的精确等式。近年的 finite-time Livšic 结果也沿着逼近精度问题推进，而不能被当成 polynomial/scheme 结论。

Bruin–Holland–Nicol，*Livšic regularity for Markov systems*，ETDS 25 (2005)，1739–1765，[全文](https://arxiv.org/pdf/math/0503690)，[DOI](https://doi.org/10.1017/S0143385705000179)。已核引言和 §6：确实包括某些 Hénon-like 映射，但通过 Young towers 处理可测解的 Hölder 正则性，并要求相应非一致双曲结构。不是任意系数辛 Hénon 上的有理解或多项式解分类。

二者提供应承认的思想背景，却不消除以下差异：无双曲参数限制、有限周期而非无限全周期、精确而非近似、概形而非几何点、输出多项式而非 Hölder 函数。新颖性必须落在这些精确交集上，而不是仅落在“Livšic”一词上。

## 5. 参数保持四维辛 lift：旧扩张工具与新分类位置

被查的映射为

$$
a'=a,\qquad s'=s+V_t(t,a),\qquad t'=t+s',\qquad r'=r+V_a(t,a),
\qquad V\in\mathbb C[t,a],\quad\deg_tV\ge3.
$$

在基域 $\mathbb C(a)$ 上作 $x=t$、$y=t-s$，底映射变成

$$
H_{p_a}(x,y)=(p_a(x)-y,x),\qquad p_a(x)=2x+V_t(x,a).
$$

因此 $r$ 的更新是一个 Hénon 差分域上的加性扩张。这不是一般 ΠΣ 塔中的平移变量模型；不能声称 Karr 算法因此已经直接解决了 Hénon 底上的余边界判定。

Carsten Schneider，*A difference ring theory for symbolic summation*，J. Symbolic Comput. 72 (2016)，82–127，在线发表于 2015，[作者预印本](https://arxiv.org/pdf/1408.2776)，[DOI](https://doi.org/10.1016/j.jsc.2015.02.002)。已核 §3.1，尤其 Lemma 3.10 和 Theorem 3.11：对特征零差分域及超越扩张 $E(r)$、$\sigma r=r+h$，常数域保持不变当且仅当底域 $E$ 中没有 $\sigma f-f=h$。原文明确将对应场论结果归于 Karr。

这条已知判据可作为当前完整固定域证明的正式依据。若底常数域为 $\mathbb C(a)$，则新工作的实质是决定 $V_a$ 何时为 Hénon 余边界。按照待核的单变量分类，这迫使

$$
V_a(t,a)=c(a)V_t(t,a).
$$

进一步把该等式精确分类为 $V(t,a)=W_0(t+A(a))$、核定 $A$ 的函数类别，并证明例外情形的实际辛解耦，才是对象专属的新内容；一般扩张引理本身不是新贡献。

当前输入的目标固定域为一般情形 $\mathbb C(a)$，例外情形 $\mathbb C(a,r-A'(a)s)$。本报告没有找到该精确四维 lift 及势函数例外的直接发表分类；其最终正确性仍取决于底固定域、单变量必要性、参数函数类别和辛坐标变换四处证明完整。

### 5.1 不应泛称“全部 isotrivial 分类”

通常 Hénon family 的 isotriviality 允许参数依赖的代数共轭，不只允许当前势函数中的平移。下面是本代理的直接代数检查，不是文献引用：

$$
V(t,a)=\frac a3t^3,\qquad p_a(x)=2x+ax^2,\qquad L_a(x,y)=(ax,ay).
$$

在 $\mathbb C(a)$ 上有 $L_a\circ H_{p_a}=H_{2x+x^2}\circ L_a$，所以该底 Hénon family 已是 isotrivial；但 $V_a=t^3/3$ 不可能等于 $c(a)V_t=c(a)at^2$。若单变量刚性定理成立，其四维 lift 仍只有 $\mathbb C(a)$ 作为有理固定域。

甚至给固定的势函数增加非恒定的纯参数项也不改变底 Hénon family，却改变 $r$ 的漂移。故推荐用 **translation-decoupling exception / 平移解耦例外**；如坚持使用 isotrivial，必须明确定义更窄的辛 lift 等价关系，并证明该定义与例外完全吻合。

### 5.2 邻近的参数 Hénon skew product 不是本固定域分类

Déserti–Leguil，*Dynamics of a Family of Polynomial Automorphisms of $\mathbb C^3$, a Phase Transition*，[作者全文](https://leguil.perso.math.cnrs.fr/Articles/Deserti_Leguil.pdf)，[DOI](https://doi.org/10.1007/s12220-017-9816-1)。已核引言及 §2：研究带乘法底参数的特定三维 Hénon skew product、保持纤维化和增长，并用参数缩放作半共轭。没有当前四维辛加性 lift 的 $V_a$ 分类；但“参数 Hénon 族可经缩放消除参数”的现象明确不是新概念。

## 6. 贡献登记建议与证据缺口

| 待写部分 | 建议登记 | 当前剩余核证 |
|---|---|---|
| 二次 bounded-word 基与 wrapping | Bousch 已有 | 正确引用，不重复首创 |
| 任意次数/multi-phase 基 | 所需推广或工具 | 勿仅凭次数推广宣称重大新机制 |
| 基轨道描述 $H^1$ | permutation-module 的直接推论 | 常数 word、phase 与线性商类别写清 |
| 单一长周期概形零检测 | 尚未发现直接 prior 的候选新陈述 | 严格无混叠证明及非既约情形 |
| 从 $D$ 得到有效 $n(D)$ | 候选有效性增量 | 锁定跨度定义、常数、适用次数 |
| 单变量有理余边界 iff | 尚未发现直接 prior 的对象专属分类 | 有理极点降为多项式的必要性 |
| 加性扩张常数域 criterion | Karr/Schneider 已有 | 引用并核定基础差分域 |
| 四维完整固定域与平移解耦例外 | 尚未发现直接 prior 的候选应用分类 | 参数 PDE、函数类别、真实辛解耦 |

不把这张表视为证明通过表，也不把“尚未发现 prior”直接改为新颖性 PASS。本次按委派要求优先完成证据/覆盖；没有给 22–30 页最终容量结论，没有把上一候选的页数估计套到这一新对象。

## 7. 检索范围与交付边界

检索使用了原题/文件名及多组组合：`Bousch Algèbres de Hénon`、`alghenon`、`Henon algebras`、`Hénon cohomologie polynômes`、`Henon polynomial cohomological equation`、`Henon rational coboundary`、`polynomial automorphism cohomological equation`、`polynomial Livsic periodic`、`finite Livsic symbolic`、`locally constant coboundary period length`、`Hénon orbit sums polynomial`、`Henon telescoping polynomial`、`Henon fixed field`、`Henon additive extension invariant field`、`Hénon isotrivial family`、`Karr additive extension constants`。

数学结论只依据上述一手论文/作者手稿及明确标注的直接代数检查。未将 Hénon–Heiles 连续 Hamiltonian、Hardy–Hénon PDE、非交换“Henon algebras”或一般动力系统层上同调混入直接相关工作。Bousch 的作者目录说明该稿未发表；未发表不意味着其已公开的内容可以不归属。

本次只新增此报告，没有修改原 preflight、正式论文、周期 trace/jet 候选或固定锁。没有下载 PDF 到工作区，没有外部写操作。本报告仅完成有界文献覆盖预筛；主证明和最终科学/容量门仍由实际完成的证据分别验收。

## 8. 后续定量核心专项查新

本节对应主代理后续明确委派：查新新增的精确 Hilbert 级数、primitive 次数上界和 sharp logarithmic certificate；不先做最终容量评价。下列公式是本轮收到的主证明输入，不能因登记于此就视为证明已经通过。

### 8.1 精确对象与检索结论

在 scalar 情形令 $A=K[x,y]$、$\sigma=H_p^*$、$d=\deg p\ge2$，并使用原始仿射坐标的总次数滤过

$$
\mathcal H_D=\operatorname{im}\bigl(A_{\le D}\longrightarrow A/(\sigma-1)A\bigr).
$$

新增输入是

$$
\operatorname{Hilb}_{\operatorname{gr}\mathcal H}(t)
=1+\frac{t(1+t+\cdots+t^{d-2})}{(1-t)(1-t^{d+1})},
\qquad
\dim_K\mathcal H_D\sim\frac{d-1}{2(d+1)}D^2,
$$

且结果只依赖 $d$，不依赖 $p$ 的低次系数。这里的级数记录 $\dim(\mathcal H_D/\mathcal H_{D-1})$，不是直接以 $\dim\mathcal H_D$ 为系数的累积级数；也不是有限群不变量理想的 coinvariant algebra Hilbert 级数。

本轮以 Hénon/Henon、cohomological equation、polynomial cohomology、coinvariants、degree filtration、Hilbert series、Hilbert–Poincaré 及法文变体组合检索，**没有定位到该精确函数或对所有系数成立的对应一手公式**。无关的有限反射群 coinvariant algebra、de Rham/拓扑上同调以及 Hénon–Heiles 系统均已排除。

这一输入比“余同调由 word 轨道张成”更强：它还需确定普通总次数滤过与轨道代表的最小次数如何相交，以及不同代表之间是否发生降次抵消。Bousch 的无限基为所需工具，但单独的 permutation-module 描述没有自动给出这个特定滤过的精确尺寸。主证明仍须完成滤过严格性与计数论证，不能用有界检索的未命中替代这两点。

同一输入还给出：若 $g\in(\sigma-1)A$ 且 $\deg g\le D$，则存在 $\deg f\le D$ 的 $f$ 满足 $\sigma f-f=g$。检索 polynomial automorphism/cohomological equation/degree bound、polynomial/rational summation/Henon 和 coboundary/degree 的组合，未定位到此对象上的同式一手次数界。一般差分域常数判据也不包含这条原函数次数控制。

### 8.2 对数周期与尖锐性的准确范围

新增 scalar 充分周期输入为

$$
n(D)=4\lfloor\log_dD\rfloor+3,\qquad D\ge1,
$$

在这一周期的完整固定点概形上，orbit-sum 为零精确判定 $\deg g\le D$ 的多项式余边界；主推导还意在给出所有足够长 $n$ 的一致判据。多 phase 情形输入为 $4\log_\delta D+O(1)$，其中 $\delta=\prod_i\deg p_i$，$O(1)$ 的依赖须在正式证明中锁定。

输入的反例族限于 $d\ge3$。以 $X_0=x$、$X_{-1}=y$ 为规范，用

$$
g_r=X_{-r-1}X_r^2-X_{-r-1}^2X_r,\qquad
D_r=3d^r,\qquad n_r=4r+2,
$$

说明无限 word 轨道不同，而模 $n_r$ wrapping 后位于同一循环轨道，故其有限 orbit-sum 相消但并非无限余边界。这条反例若核证成立，因 $n_r/\log_dD_r\to4$，可排除把**对所有足够长周期都成立的统一最终阈值**的首项常数降到 $4$ 以下。

必须保留量词边界：仅这条偶数周期子序列并不直接证明“任何特殊选择的较短单一周期都不可能”，也不排除多个短周期联合检测；不能称作一般算法的信息论下界。它也没有直接给出 $d=2$ 的尖锐性。本报告没有定位到此 Hénon 概形检测阈值、其 leading-$4$ 反例或对应代数型下界的一手先例。

### 8.3 近年的 quantitative finite Livšic 仍是不同问题

Sébastien Gouëzel–Thibault Lefeuvre，*Classical and microlocal analysis of the X-ray transform on Anosov manifolds*，Analysis & PDE 14 (2021)，301–322，[一手预印本](https://arxiv.org/pdf/1904.12290)，[DOI](https://doi.org/10.2140/apde.2021.14.301)。已核引言及 Theorem 1.2：归一化 Hölder 函数在长度至多 $\varepsilon^{-1/2}$ 的闭轨道上有小平均时，可写成流方向余边界加一个范数受 $C\varepsilon^\tau$ 控制的余项。它本身明确属于 finite approximate Livšic，并承认 Svetlana Katok 对三维 contact Anosov flow 的较早工作。

本轮亦检到 Thomas O'Hare 于 2026-04-16 的[Georgia Tech 官方研究报告摘要](https://math.gatech.edu/node/32841312)，宣布与 Jonathan DeWitt、Spencer Durham、James Marshall Reber 合作，把 transitive Anosov flow 的有限周期近似误差改善为指数小。本报告只核到该一手机构报告摘要，没有以其代替未定位全文的定理核证；摘要仍明确说 approximate solution，而不是多项式环中的精确余边界。

因此不宜说“有限 Livšic 的最好结果只有多项式误差”，更不能因 exponential 与 logarithmic 互为尺度就认为上面的精确证书已被覆盖。需要同时比较：函数类别、双曲性限制、所有短周期还是单个完整周期概形、误差是否严格为零、以及输出原函数是否保留多项式类别。本轮所核文献均未给出该交集中的当前结论。

### 8.4 证书长度与直接求解规模不可互换

若固定点代数长度为 $\dim_K A_n=d^n$ 且上述 scalar 周期界成立，则直接推出

$$
\dim_K A_{n(D)}\le d^3D^4.
$$

这记录的是固定 $d$ 下的**有限周期代数向量空间维数／概形长度**。不自动等于读取该代数所需的位数、计算 orbit-sum 的操作次数、Gröbner 求解复杂度或任何算法下界；系数高度、编码、稀疏性和运算模型均未在此受控。

另一方面，若 §8.1 的 primitive 次数界成立，可直接设 $f\in A_{\le D}$ 比较 $\sigma f-f=g$ 的系数。其未知数至多 $\binom{D+2}{2}$，方程涉及次数至多 $dD$，所以至多 $\binom{dD+2}{2}$ 个系数条件。这是由待核次数界作出的直接线性代数推论，不是已实测的运行时结论；它足以提醒写作时不能把 $D^4$ 周期代数说成“最小求解规模”。

本次定量补查的登记结论是：**精确滤过尺寸、原函数次数界和对数单周期概形检测／稳定阈值尖锐性，仍为未发现直接 prior 的候选新增核心，且不与二次 word 基的归属扣除混为一项。** 是否证明成立、是否形成足够完整的论文，以及最终科学/容量评价，均保持独立验收；本报告不将其提前改成 PASS 或 STOP。

### 8.5 多 phase mixed-radix reversal／Hilbert 后到命题的有界补记

本附记只针对随后送达的同一余同调核心命题，不重开 §1–8.4 已完成的覆盖。令 $\delta=\prod_{i=1}^k d_i$，$\rho$ 为所选 phase 规范中负向射线最低 $k$ 位数字移至正向射线时诱导的 mixed-radix reversal 置换。主代理与另一证明代理独立推导后送审的公式是

$$
C_\rho(t)=\sum_{0\le R<\delta}t^{\max(R,\rho(R))},\qquad
E_\rho(t)=\frac{C_\rho(t)+2t^\delta/(1-t)}{1-t^{\delta+1}},
\qquad
\operatorname{Hilb}_{\operatorname{gr}\mathcal H}(t)
=1+\frac1{(1-t)^2}-E_\rho(t).
$$

这里仍是原始 $(x,y)$ 普通总次数的诱导滤过。scalar 情形 $\rho=\mathrm{id}$ 回到 §8.1；按二进制两位反转直接计算，$(d_1,d_2)=(2,2)$ 给 $C_\rho=1+2t^2+t^3$，单一 $d=4$ 给 $C_{\mathrm{id}}=1+t+t^2+t^3$。因此该公式若核证成立，可区分相同 $\delta$ 的这两种构造；没有据此主张一般多项式共轭不变性，也没有声称它完整恢复任意有序 multidegree。

本次新检索限定于 “Henon mixed radix”、“Hénon digit reversal”、“Henon Hilbert composition”、“polynomial cohomology mixed radix”、“Hénon Hilbert series cohomology”（含 arXiv 域内）、“Henon radix polynomial”、“Hilbert series digit reversal”、“mixed-radix cohomology”、“mixed-radix digit-reversal permutation polynomial”、“Hénon cohomology multidegree”、“digit reversal generating function max” 和 “Hénon Hilbert filtration”。**没有定位到该多 phase 余同调 Hilbert 公式、$C_\rho$ 最大值统计在此滤过中的应用，或上述同 $\delta$ 区分结论的直接一手 prior。** 这是本轮有界未命中，不是穷尽性首创证明。

需要扣除的相邻已知工具仅是数字反转本身：Matteo Frigo–Steven G. Johnson，*The Design and Implementation of FFTW3*，Proceedings of the IEEE 93(2) (2005)，216–231，[作者／项目全文](https://www.fftw.org/fftw-paper-ieee.pdf)，§II 明确把 mixed-base digit-reversal permutation 用于 Cooley–Tukey FFT 的索引重排。已核该节；它不涉及 Hénon 余同调或普通次数 Hilbert 级数。故本命题的候选增量应写作**数字反转所控制的次数滤过精确计数**，不应写作发明了 mixed-radix reversal。

本附记只登记文献覆盖。主代理告知的普通坐标有限矩阵吻合检查属于核错证据，既不代替一般公式证明，也不承担文献新颖性或容量验收；本次没有重复这些检查、修改其他文件或给出容量终审。
