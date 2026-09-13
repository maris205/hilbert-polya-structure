# Paper31 闭合非单位时间算术：C2 来源深核 V1

日期范围口径：按用户更新后的环境日期 **2026-09-10** 截止；保留主控指定的 `20260909` 文件名。
席位：`/root/p31_qpi_novelty_cd_i01_i03_v1`，也是原格引理 [G] 的作者。
身份是 `NOVELTY_PHASE_B / C2_SOURCE_COLLECTION / NO_INDEPENDENT_VOTE / NO_ADMISSION`。
本件使用 research-lit 与 novelty-check 的 A/B 部分；不执行本席自己的 C/D 新意评分，也不预设合并分数。

## 1. 范围、输入与结果摘要

本人完整读取 [Phase A][PA]，本轮重新完整读取冻结的 [G]。唯一新增文件为本文；不改 G、其他证明包、旧新意票或索引。

| 输入 | 阅读范围 | SHA-256 |
|---|---|---|
| Phase A V1 | FULL | `07b658e0e6a07fece0db86d85face58a852646760a6e8d185f7715800dd2ae5f` |
| G：原全次数自由格引理 V1 | FULL；保留其作者身份，不视为独查 | `d872b731423107412631a9834b639229b2578e0084afef752c6a94d6e90f7c6a` |

检索的对象是固定 $R=\mathbb Z[\tau]$ 的原四簇实际余核 $M_n$，以及

$$
L_n=M_n/T_n,\qquad
\rho_n(M_n)=\tau^{-n}\bigoplus_{a=0}^{n-1}I_{n,a},\qquad
I_{n,a}=\left(\binom{n-1-b}{a}\tau^b:0\le b\le n-1-a\right),
$$

连同原 $s_0$ 的 $\tau$ 倍右移和 $E_n=L_n^{**}/L_n$。不是只检索 qPI 题名，也不是考查特征零秩或某个有限 $n$ 的 Smith 表。

本轮来源支持以下**有限结论**，不是完整新颖性判决：

1. 整数主部丛的二项式 Laurent 过渡矩阵、负二项式局部基、全局留数及其局部求和都有明确先例，须从方法新意中扣除。
2. 忘掉原几何后，$\bigoplus I_{n,a}$ 及其 $\tau$ 倍右移是一个行独立的加权 Taylor/Pascal 像的短计算；§2 给出完整恒等式，不把“格”和“shift”重复记作独立机制。
3. 已实际读取的定理尚未给出原 $M_n$ 与这个行独立整数像的识别。这个“尚未得到包含”的结论，不等于该识别有足够新意，也不排除它是标准几何工具的短应用。
4. 特征 $p$ 的主部丛分裂已有全次数递推，不能把“所有 $p$ 的二项式异常”本身当作新的现象。其对 C3 的具体包含判断交主控/非作者合并，本件不提前投票。

## 2. 忘掉 qPI 的最强包含压力：抽象格与连接的短推论

本节是**本报告的比较推导**，不是声称下面的记号或同一公式已原样出现于某篇来源。
它把必须扣除的标准机制和仍需识别的原对象分开。

令 $N=n-1$、$A_N=R[U,V]/(U,V)^{N+1}$，并定义 $R$-线性映射

$$
\mathcal T_N:A_N\longrightarrow R^{N+1},\qquad
\mathcal T_N(U^aV^b)=
(-1)^{N-a-b}\binom{N-b}{a}\tau^b e_a
\quad(a+b\le N).
\tag{T}
$$

这里每个 $a$ 的源单项式是独立的。因此从生成元即有

$$
\operatorname{im}\mathcal T_N=\bigoplus_{a=0}^{N}I_{N+1,a}e_a.
\tag{T-image}
$$

每个行系数也可由 Hasse–Taylor 算子写成

$$
\binom{N-b}{a}=D_X^{[a]}(X^{N-b})\big|_{X=1},
\qquad D_X^{[a]}X^m=\binom maX^{m-a}.
$$

所以 (T-image) 是加权 Taylor **行内容理想**的直和；它不是一种新的二项式系数生成机制。
与整数主部丛的二项式坐标计算相对应的经典框架见 [Maakestad 的 §3][M08]；本节的具体像身份由上述生成元直接证明。

再令 $F=U(\tau+V)$。乘 $F$ 后截断给出良定义映射
$m_F:A_N\to A_{N+1}$，因为 $F\in(U,V)$。设 $\operatorname{sh}(e_a)=e_{a+1}$。
对 $a+b\le N$，有

$$
\begin{aligned}
\mathcal T_{N+1}\bigl(FU^aV^b\bigr)
&=(-1)^{N-a-b}\tau^{b+1}
\left[\binom{N+1-b}{a+1}-\binom{N-b}{a+1}\right]e_{a+1}\\
&=\tau\,\operatorname{sh}\bigl(\mathcal T_N(U^aV^b)\bigr).
\end{aligned}
\tag{T-shift}
$$

边界 $a+b=N$ 时第二项的单项式被截断，其二项系数亦为零，故式子仍成立。
(T-shift) 仅为 Pascal 恒等式。原 [G] 一旦证明坏图整数正规形 $F=U(\tau+V),G=V$，并保留整个 fat-jet 的 Jacobian 单位，格像和连接就由这同一计算给出；不能各自再计一份方法新意。

同理，$I_{n,a}$ 同时含非零整数 $\binom{n-1}{a}$ 与 $\tau^{n-1-a}$，在非端点时二者互素；端点理想为 $R$。指定嵌入中的 $I_{n,a}^{**}=R$ 是 UFD 分式乘法的短推论。因此在原格身份成立之后，$E_n=\bigoplus R/I_{n,a}$ 也不是另一种独立方法。

### 2.1 不能省掉的比较桥梁

“某篇论文有 Pascal 矩阵”不足以推出原格已被包含；“逐行内容相同”也不等于整个矩阵像相同。
例如 $\left(\begin{smallmatrix}1&1\\1&-1\end{smallmatrix}\right)$ 的两行内容均为 $\mathbb Z$，但其像不是 $\mathbb Z^2$。
在 (T) 中能取直和，是因为不同 $a$ 的源系数确实独立；这正是 [G] 需要从原完整目标 jet 和 Jacobian 单位证明的事实。

要由一篇既有主部丛/留数定理直接包含 C2，至少必须实际给出并核对：

- 原受限 $J_n$ 被完整四中心、正确反典范符号的留数映射湮灭；遗漏边界共同零点不能用抽象留数定理补救。
- 该留数映射识别原 $M_n[1/\tau]$，而不只是给一些线性泛函；需要原秩与满射或等价的真正余核识别。
- 在 $\mathbb Z[\tau]$ 上原坏图的坐标/Jacobian 保留完整 fat jets，不反演 $\tau$ 或整数素数。
- 两好图的像不会扩大所算整数格，且原 $s_0$ 与 (T-shift) 的乘法严格对应。

截至本轮实际读取范围，没有从来源定理单独构造出这一整套映射。
但这只定位了**尚需原对象识别**的差额；其工作量和研究价值仍须独立判断，不能把每个核对步骤包装为新的一般理论。

## 3. 来源证据表：经典与近期分别核查

阅读级别：`M`=元数据/摘要；`R`=相关正文段；`T`=实际定理陈述；`P`=其证明；`FULL`=全篇。
下表无一项冒称 FULL。编号是本文来源号，不是新意排序或分数。

| 号 | 一手来源与出版信息 | 本人准确阅读层级 | 对 C2 的包含压力及边界 |
|---|---|---|---|
| S1 | Helge Øystein Maakestad, *Principal parts on the projective line over arbitrary rings*, Manuscripta Math. **126** (2008), 443–464；arXiv 初版2004、所读 v4=2020-11-12。[官方预印本][M08] | R/T/P：§2 定义2.1、命题2.2；§3 定理3.1–3.2和展开证明；§4 定理4.1及证明、定理4.2陈述与所需方程，预印本 pp.2–10。§5只读主结果对应范围，非全篇。 | **已含**整数二项式 Laurent 过渡矩阵；任意环分裂是带线性方程可解及单位条件的判据，不是所有整数格的无条件分裂。没有在所读定理中出现原四簇 $M_n$；直接包含需补 §2.1 的识别。 |
| S2 | A. Kyomuhangi, E. Marangone, C. Raicu, E. Reed, *Cohomology on the incidence correspondence and related questions*, arXiv:2411.13450v1，2024-11-20；本轮页面未列期刊信息。[正文][K24] | R/T/P：§2与主部丛相连的局部上同调段；§3 定义(3.1)–(3.5)、Remark3.1、Theorem3.2完整陈述、Corollary3.3及证明、Lemma3.4及负二项式证明。未读取 Theorem3.2 余下全部证明。 | **已含**正特征主部丛分裂的递推定理及负二项式局部基。输入是域上射影线向量丛；不能仅凭其分裂型得到 $\mathbb Z[\tau]$ 的原余核格。C3 需认真比较该强先例，不能只称二项式异常新。 |
| S3 | 同四作者，*Computing the cohomology of line bundles on the incidence correspondence and related invariants*, arXiv:2503.17522v1，2025-03-21；本轮页面未列期刊信息。[正文][K25] | M/R/T/P：摘要/导言；完整 §3、§3.1，含主部丛与 $\mathcal F_r^d$ 的三种次数范围识别及推导、软件接口与例3.1–3.3；非全篇，也未运行其软件。 | **已含**上述正特征分裂理论的实际计算接口；主部丛与 $\mathcal F_r^d$ 的识别须区分次数范围，等变式还含行列式扭转。未给原整数格/原截面连接，不能把分裂算法直接当原 $M_n$ 算法。 |
| S4 | David Perkinson, *Principal parts of line bundles on toric varieties*, Compositio Math. **104** (1996), 27–39。[期刊存档][P96] | R/部分T：§0 的复数/光滑 toric 假设、Taylor 解释；§1 到Theorem1.2的文字与§2射影空间应用。PDF解析丢失关键交换图；截图一次超时、一次未识别PDF，故**未完整核清定理1.2交换图及证明**。 | 重要经典线索：Euler 序列描述 toric 主部丛。已读前提为复数几何；不能把其题名视为整数格包含定理。本项保留读取限制，**未排除**更精确的形式比较；不以残缺交换图证明包含或排除。 |
| S5 | E. Cattani, D. Cox, A. Dickenstein, *Residues in Toric Varieties*, Compositio Math. **108** (1997), 35–76；所读arXiv:alg-geom/9506024v1，1995-06-27。[正文][CCD97] | R/T/P：导言Theorems0.1–0.4；§4局部定义(4.8)–(4.9)、Remark4.10、Theorem4.12及证明，预印本 pp.22–25；证明调用的所有前置 currents 命题未逐一重证。 | **已含**紧空间留数和消失及 toric/global/local 留数接口。0.3的余环同构须 ample、无共同零点等假设；4.12是有限交与空全交的局部求和。它们不自动计算原族的整数格或其 $\tau=0$ 缺陷。 |
| S6 | Francesco Galuppi, *Collisions of fat points and applications to interpolation theory*, J. Algebra **534** (2019), 100–128；arXiv:1803.02746，2018-03-07。[正文][GAL19] | R/T/P：预印本§1复数假设、Construction10、Remark11、Propositions12–13和Lemma14及其证明，pp.1–4。 | **已含**碰撞/平坦极限与插值维数的标准联系。Proposition13在一般碰撞下由最小非零线性系次数确定极限重数；不是任意受限截面在整数基上的余核格与连接分类。一般性和底环均须另匹配。 |
| S7 | E. Guardo, L. Marino, A. Van Tuyl, *Separators of fat points in $\mathbb P^n$*, J. Algebra **324** (2010), 1492–1512。[作者机构期刊PDF][GMT10] | R/T/P：期刊pp.1492–1497，导言、定义、Theorem3.3及完整证明；Theorem6.4仅获得同一机构PDF搜索索引中的陈述和证明开头，正文后续请求403，**不是§6完整阅读**。 | **已含**降低一个点重数的 separator 理想/生成元与 Hilbert 函数机制。§6线索是特征零、齐次 fat points 且支撑为完全交的 CB 型同度结论；不能据此直接宣称原整数格已包含，完整强比较仍**未排除**。 |
| S8 | Carlos D’Andrea, Alicia Dickenstein, *Toric Euler-Jacobi vanishing theorem and zeros at infinity*, arXiv:2601.13977v1，2026-01-20，预印本。[正文][DD26] | M/R/T/P：§1.1–1.2的定义/假设、Theorem1.4陈述及§6.1其证明；未完整读取其关键前置Theorem6.4证明。 | **已含/邻近扩展**复数 Laurent 系统在 indecomposable Newton 多面体条件下的留数消失、无穷远零点与 Jacobian 代表判别。需零维闭包交；不是所有整数素数的 $I_{n,a}$ 分类。不能用它把原边界检查自动略去。 |
| S9 | Raquel Mallavibarrena, Ragni Piene, *On fundamental forms and osculating bundles*, arXiv:2411.07882v1，2024-11-12，预印本。[正文][MP24] | M/R：摘要、导言、§2至基本形式定义及经典比较段；非主定理完整阅读。 | **已含**主部丛/Taylor映射的坐标无关框架；某些对偶识别明确要求阶乘可逆。此处只作邻近术语/框架来源，不拿未读定理排除 C2。 |
| S10 | Heng Li, Xizhi Liu, *Sharp bounds for minimal dependencies of linear-form powers*, arXiv:2606.24349v1，2026-06-23，预印本。[正文][LL26] | M/R/T：导言、§2.1–2.2，含Theorem2.6完整陈述；未读其证明。 | 近期邻近压力：最小线性形式幂依赖的域上维数界，正特征版本使用指数的base-$p$数字和。不是所查整数族格；但不能把“二项式/Frobenius产生数字规律”当原研究专有现象。本项不作强包含证据。 |

关于最直接的原工具：同席在 G 作者阶段已定向读过 Griffiths, *Variations on a theorem of Abel*, Invent. Math. **35** (1976), 321–390，§III(a) pp.368–373 的定义、(3.7)及 Stokes 证明；本轮不重读整篇。
原 G 已明示该全局留数定理须扣除，也没有消费要求正性的逆定理。[官方作者机构原文][GR]

### 3.1 合并后的四种证据标签

| 标签 | 本轮可落下的内容 | 不能由此推出的内容 |
|---|---|---|
| **明确已含** | 整数二项式主部丛矩阵；负二项式局部展开；留数与局部和；正特征主部丛全次数分裂递推；碰撞/插值及separator的一般机制 | 原受限四簇整数上同调整包已原样出现 |
| **短推论** | 达到坏图整数正规形且允许完整独立 jet 系数后，(T-image)、(T-shift)、$I^{**}=R$与缺陷商 | 正规形、原余核识别本身自动拥有较高新意 |
| **尚需原对象识别** | 完整四中心与符号、$\rho J=0$、秩/满射、Jacobian单位作用、好图像包含与原$s_0$绑定 | 该识别是新的一般定理或足够支撑独立长篇论文 |
| **未排除** | 是否有更一般的整数 principal-parts/碰撞截面/残差对偶定理，直接统一原识别；S4交换图与S7后段的精确匹配 | “没检索到同式”就是不存在先例；或用本文替代非作者C/D |

## 4. 查询与覆盖记录

### 4.1 本地与公开入口

- 检查了可用工具名/描述；未配置 Zotero、Obsidian 专用入口。按技能降级，不申请新插件。
- 对 `papers/`、`literature/` 的文件名相关性检查没有识别出可用于本题的外部论文收藏；项目自身接受稿不重复计为外部来源。未扫描不相关旧PDF内容。
- 按技能查找 `arxiv_fetch.py` 未找到；使用 arXiv 官方论文页/正文与站点限定网页检索。没有下载PDF到本地，没有运行任何数学CPU/GPU实验。
- Google Scholar公开搜索入口 `https://scholar.google.com/scholar?q=%22principal+parts%22+%22arbitrary+rings%22` 返回 Internal Error。
- Semantic Scholar公开搜索入口 `https://www.semanticscholar.org/search?q=principal%20parts%20projective%20line%20arbitrary%20rings&sort=relevance` 返回 Internal Error。
- 追加 `site:scholar.google.com` 与 `site:semanticscholar.org` 的同题站点索引检索，没有得到可独立使用的新记录；**不声称成功检索了两站数据库**。

### 4.2 技术表达式：经典包含检索

以下为实际发出的主要查询；并非只换 qPI 的名称。多个查询中的非数学同词结果已排除，不计相关证据。

| 查询组 | 实际表达式 | 有效落点 |
|---|---|---|
| 整数主部丛 | `"principal parts" "binomial" "integers"`；`"principal parts" "projective line" "positive characteristic" splitting`；`"Principal parts on the projective line over arbitrary rings" Maakestad` | S1、S2；另有Maakestad2004旧文与2000论文线索，不与S1重复记先例数 |
| Taylor/整数格 | `"Taylor" "Pascal" "lattice" binomial integer`；`"jet bundles" "arithmetic" "binomial coefficients"`；`"Taylor map" "integer" "principal parts" projective line`；`"principal parts" "Z[t]"` | 整数二项式坐标机制，S1；无同一原格的直接识别定理 |
| 留数/CB | `"toric residue" "Cayley-Bacharach" "fat points" interpolation`；`"Cayley-Bacharach" "fat points" toric residue`；`Cox Toric residues theorem global residues 1996 pdf` | S5、S7；进而找到S8 |
| 碰撞插值 | `"collision" "interpolation" "principal parts" arithmetic`；`"collision of points" interpolation arithmetic`；`"colliding sections" "interpolation" algebraic`；`"Collisions of fat points and applications to interpolation theory" arxiv` | S6；其他物理碰撞结果无关 |
| Pascal内容 | `"integer" "Pascal matrix" "ideals" binomial`；`"Pascal" "content ideals"`；`"Taylor" "lattices" "arithmetic" binomial coefficients` | 未找到直接原对象包含；多元Riordan/Pascal矩阵论文仅摘要线索，不用于主结论 |
| toric主部丛 | `"Principal parts of line bundles on toric varieties" Perkinson pdf`；`"principal parts" "projective line" "torsion" integers` | S4及S1；不把任意ring题名误读为任意整数格分类 |

### 4.3 2024–2026 与最近六个月

年份检索实际包含以下表达式：

- `site:arxiv.org "principal parts" "2024" OR "2025" OR "2026"`；`site:arxiv.org "Taylor" "lattice" "binomial" 2024..2026`；`site:arxiv.org "toric residue" 2024..2026`。
- 更精确地追加 `site:arxiv.org/abs/ "principal parts" after:2024-01-01 before:2026-09-11`、`"jet bundles" "arithmetic"`及`"fat points" "collision"`的同日期站点查询。
- `"toric residue" 2024 2025 2026 arithmetic`；`"collision" "fat points" 2024 2025 2026 arxiv`；`"principal parts" "binomial" after:2024-01-01 before:2026-09-11 site:arxiv.org`。

最近六个月采用 **2026-03-09 至 2026-09-10** 的覆盖区间，先对 arXiv 站点发出 `after:2026-03-09 before:2026-09-11`，终态又以 `after:2026-03-08 before:2026-09-11` 补足左端日期边界；分别组合：

1. `"principal parts"`；
2. `"jet bundles"`；
3. `"toric residue"`；
4. `"fat points" "interpolation"`，另以 `"fat points"` 放宽；
5. `"Pascal" "lattice"`；
6. `"Cayley-Bacharach"`。

日期过滤是公开搜索索引条件，不等于完整 arXiv 数据库枚举。另向 `export.arxiv.org/api/query` 发出三组结构化日期查询：

```text
(all:"principal parts" OR all:"jet bundle" OR all:"Taylor map")
  AND submittedDate:[202603090000 TO 202609102359]
(all:"toric residue" OR all:"Cayley Bacharach" OR all:"fat points")
  AND submittedDate:[202603090000 TO 202609102359]
(all:"binomial" AND (all:"lattice" OR all:"Pascal"))
  AND submittedDate:[202401010000 TO 202609102359]
```

三组 API 请求均返回 `not safe to open (non-retryable error)`，没有获得结构化结果；保留该失败，不当作零命中，也未用其他手段绕过。

2024–2026 的相关落点为 S2、S3、S8、S9，终态补查另得近六月的 S10；均按官方arXiv记录日期区分，不按抓取时间或HTML正文内部日期当发表日期。
最近六个月检索还返回下列较近术语，但**只到搜索结果摘要/元数据层，不作强包含证据**：

| 官方arXiv记录 | 日期 | 只据摘要能确认的区分 |
|---|---|---|
| Javier de Lucas, [*Jet Bundles as Higher-Order Polarised $k$-Contact Manifolds*](https://arxiv.org/abs/2606.09263) | 2026-06-08 | 光滑接触/PDE jet 几何；不是所查整数主部丛格 |
| Cristian Anghel, Filip Chindea, [*A no-go theorem for special Ulrich bundles, with a complement on primary Burniat surfaces*](https://arxiv.org/abs/2608.09901) | 2026-08-10 | 表面上CB构造与Ulrich扩张；未在摘要见原算术格，不据摘要排除全文潜在关联 |
| Leah Wrenn Berman, Jürgen Richter-Gebert, [*On Chasles’ Quadrilateral Theorem*](https://arxiv.org/abs/2603.27587) | 2026-03-29 | 经典射影关联的CB解释；不是整数族余核计算 |
| Seokho Jin, Sihun Jo, [*The k-Rank Taylor Family: Canonical Harmonic Lifts, Principal Parts, and Rademacher Series*](https://arxiv.org/abs/2608.26617) | 2026-08-27 | 模形式的Taylor系数/极部，principal parts为不同语境 |
| Nick Vorobtsov, [*On the Hidden Pascal Symmetry and Moment Constraints of Vector Representatives in Quebbemann’s 64-Dimensional Lattice*](https://arxiv.org/abs/2608.17367) | 2026-08-18 | 欧氏格向量/Pascal条件；不作为 $\mathbb Z[\tau]$ 主部格的同一对象来源 |
| Cicero Carvalho, Maria Vaz Pinto, Rafael H. Villarreal, [*On the regularity index of the minimum distance function in projective nested Cartesian codes*](https://arxiv.org/abs/2604.20729) | 2026-04-22 | 另打开官方摘要；嵌套有限域Cartesian点集的indicator最小次数/CB算术准则，未读正文，不据此排除原格 |

这些弱相关记录只证明进行了近期入口与术语筛选，不提高原结论新意或证明可信度；未找到直接同式记录也不构成不存在先例的证明。
本题是纯代数几何/数论，不机械加入 ICLR/NeurIPS/ICML 实验论文。

### 4.4 日期与阅读失败的纠偏

- *Toric residue codes: I* 在聚合搜索页显示“2025”，但[出版方记录](https://www.sciencedirect.com/science/article/pii/S1071579710000857)给出 Finite Fields Appl. **17** (2011), 15–50；未误记为2025新文，也未深读到足以排除 C2。
- S3 HTML正文内部显示 `Date: August 24, 2026`，但[官方提交历史](https://arxiv.org/abs/2503.17522)只列2025-03-21的v1；不把该内部日期算作近六月的新提交或修订。
- Maakestad2000的DiVA论文PDF后续访问返回Internal Error；本轮主要比较改用已实际读取的S1，未把2000论文未读定理当证据。
- S4的关键交换图解析/截图失败、S7后段403均已在表中保留；它们不妨碍读取S1/S5等强先例，也不授权把未读部分写成已核排除。

## 5. 交给非作者 C/D 的精确问题

来源侧不建议用“qPI专名缺席”或“全次数”三个字授予新意。
应在扣除 §2 的短推论和全部既有机制后，只问：**原受限四簇的完整整数留数识别，加上其原上同调消费者，是否产生足够独立的新发现；还是仍只是一次标准工具的具体算例？**

若能从 S1/S4/S5 或更强整数对偶定理写出 §2.1 的真正函子/模同构并保留原截面乘法，则应按实际短差额降级，不能拿本报告的检索未命中抵抗包含。
若目前不能写出，也只保留该准确差额；本席是 G 作者，不给独立新意、价值、信心或容量分数。
没有据此启动论文、追加计算扫描、修改锁定验收要求或扩展到其他系统族。

[PA]: PAPER31_QPI_NONUNIT_CLOSED_ARITHMETIC_PHASE_A_V1_20260909.md
[G]: PAPER31_QPI_NONUNIT_LATTICE_CONTROL_LEMMA_V1_20260909.md
[M08]: https://arxiv.org/pdf/math/0402279v4
[K24]: https://arxiv.org/html/2411.13450v1
[K25]: https://arxiv.org/html/2503.17522v1
[P96]: https://www.numdam.org/item/CM_1996__104_1_27_0.pdf
[CCD97]: https://arxiv.org/pdf/alg-geom/9506024v1
[GAL19]: https://arxiv.org/pdf/1803.02746
[GMT10]: https://www.iris.unict.it/retrieve/dfe4d226-fcd1-bb0a-e053-d805fe0a78d9/Separators-of-fat-points-in-P%7Bdouble-struck%7Dn_2010_Journal-of-Algebra.pdf
[DD26]: https://arxiv.org/html/2601.13977v1
[MP24]: https://arxiv.org/html/2411.07882v1
[LL26]: https://arxiv.org/html/2606.24349v1
[GR]: https://publications.ias.edu/sites/default/files/variationsonatheorem.pdf
