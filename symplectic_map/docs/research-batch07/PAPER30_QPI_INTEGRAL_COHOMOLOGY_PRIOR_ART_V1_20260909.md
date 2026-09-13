# Paper30 qPI：整系数反典范上同调的有界先例核查 V1

日期：2026-09-09。执行者：独立来源核查代理。
类型：定向 primary-source 核查；不是证明接受、正式四门、完整 novelty Phase C/D 或全球先例排除。
科学状态：下列新目标现已在作者 U 成稿，但其新非作者检查尚未在本件验收；本件不授予 PROVED。
route_applicability: NOT_APPLICABLE。

## 1. 结论先行

本轮实际读到的最接近一般结果，已覆盖复数 Looijenga 对的周期、沿参数截面吹起的通用族，以及 proper flat 族上线丛上同调的 perfectness 和任意**派生**基变换。不能把这些内容作为本题的新一般机制。

在下面明确列出的原文范围内，未取得一个定理，直接给出原 qPI 的整个整系数八截面族的反典范上同调对角分解、所有边界扩张同时消失，以及指定圆分特化的完整 Smith 指数。这是“尚未取得精确包含来源”，不是“证明全球没有先例”。特别是，本轮并未全面检索一般相对 Halphen 对的整系数形式邻域和扩张分类。

准确待查差额应落在：原循环迹系数在整个共振闭子概形上的延拓与边界单位性，以及由此消去**曲面级**扩张类。若这一差额最终只是某个一般相对反典范分裂定理的直接实例，候选的独立贡献必须相应缩减；不能靠“任意基变换”“derived”或 Smith 术语恢复已扣除的新意。

## 2. 固定靶标：不是旧 G 的长度结论

本件全文读取 [G 完整模型诊断](PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_DIAGNOSTIC_V1_20260909.md)、[旧上同调来源预筛](PAPER30_QPI_COHOMOLOGY_SOURCE_SCREEN_V1_20260909.md)，并沿 G 的引用全文定位 [N 法丛入口](PAPER30_QPI_BOUNDARY_NORMAL_BUNDLE_ENTRY_V1_20260908.md)。没有重开旧 47 件输入。

检索结束后，主控提交冻结的 [U 通用整系数上同调作者诊断](PAPER30_QPI_UNIVERSAL_COHOMOLOGY_DIAGNOSTIC_V1_20260909.md)；本件有限补读其全部 255 行，核对 SHA-256 后据之锁定准确比对对象，没有追加查询。U 使用时间参数 $\tau$，下文 $t$ 对应其 $\tau$。U 的根单位截面引理依赖 S；本件只读 U 对该依赖的完整说明，没有冒充全文读取或独立核准 S。

取
$$R=\mathbb Z[q^{\pm1},t^{\pm1}],\qquad p:S_R\longrightarrow\operatorname{Spec}R,$$
其中 $S_R$ 是 G/N 的同一八截面构造：四次边界节点吹起后，在四个不同分量的单位坐标 $1,t,t,q$ 处吹起。$D$ 是四条原坐标边界与四条中间例外的最终严格变换组成的相对八环，$L_n=\mathcal O_{S_R}(nD)$。仅比较这一系统与紧化，不扩到其他 Painlevé 族。

与 U 一致的作者目标为
$$R\Gamma(S_R,L_n)\simeq R[0]\oplus\bigoplus_{j=1}^n
 [R\xrightarrow{\,1-q^j\,}R],\tag{T}$$
每个两项复形放在次数 $0,1$。这是非典范同构；固定一个同构以后要求其经任意 $R\to A$ 的派生拉回给出相应比较，不声称分裂具有未证明的唯一性或自然选择。

相应目标包括
$$H^1(S_R,L_n)\simeq\bigoplus_{j=1}^nR/(1-q^j),\qquad
H^1(S_A,L_{n,A})\simeq\bigoplus_{j=1}^nA/(1-q_A^j),$$
也包括非约化 $A$。这里任意基变换后的 $H^0$ 要保留各乘法映射的 kernel，不能从 $H^0(S_R,L_n)=R$ 猜成恒等于 $A$。

在 G 的圆分 DVR 上令 $r=mp^a$、$p\nmid m$、$s=\zeta_r$、$n=r$，预期特化为
$$H^1(\mathcal S,\mathcal L_r)\simeq
\mathcal O\oplus\bigoplus_{1\le j<r}\mathcal O/(1-s^j),$$
其非零扭子 Smith 因子是
$$\bigoplus_{b=0}^{a-1}
 (\mathcal O/(\pi^{p^b}))^{\oplus (p-1)p^{a-b-1}}.\tag{S}$$
本件仅把 (T)、(S) 固定为检索靶标，不另写证明，也不以来源核查取代主控及非作者的数学验算。

新机制靶标更具体：
$$C_j=[z^j]\operatorname{tr}\bigl(A(q^{j-1}z)\cdots A(qz)A(z)\bigr)$$
必须是原矩阵的原循环迹系数，并在 $R_j=R/(1-q^j)$ 上延拓为 $L_j$ 的截面，限制到 $D_{R_j}$ 为单位；据此通过 Bockstein/连接同态消去边界递增中的扩张类。不能只在复数单位根点、分数域、正规化后或约化纤维上核对。

U 还记录由对角呈示直接取得的
$$\operatorname{Fitt}_0H^1(S_R,L_n)
=\left(\prod_{j=1}^n(1-q^j)\right)
=\left(\prod_{d=1}^n\Phi_d(q)^{\lfloor n/d\rfloor}\right).$$
这是同一模结构的推论，不是本件新增检索的独立机制。U 的边界同样保留：各固定 $n$ 的选择不声称自动给出关于 $n$ 的派生过滤相容性，也不是截面环、cup product、动力作用或对偶的同构。

措辞上应区分：$R_j$ 是整个共振闭子概形，不能预先拆成彼此独立的圆分分支；它可非正规。特征整除 $j$ 的纤维及进一步基变换可以非约化。“在每个域上 $h^0$ 数对了”不等于上述概形级单位截面或模扩张已识别。

## 3. 实际检索日志与来源范围

使用 research-lit 的对象与实读范围分级。可用工具中未检出 Zotero/Obsidian；按题名相关性定向扫描本地 `papers/`、`literature/` 未发现匹配的现成 PDF，未重扫旧构建树。未找到本次可用的 `arxiv_fetch.py`，采用网页搜索与 arXiv 原站回退。未单独运行 Google Scholar 或 Semantic Scholar 的数据库查询，故不能把本件说成三数据库全覆盖。

本轮准确提交十二条主题查询；后续精确 URL 打开及原文内定位不另计主题查询：

1. `Looijenga pair relative anticanonical cohomology integral period torsion line bundle`
2. `"anti-canonical cycle" "universal" "period" Gross Hacking Keel`
3. `"anticanonical" "derived" "pushforward" cohomology rational surfaces`
4. `"Looijenga pairs" "cohomology" "2024"`
5. `"Looijenga" "period" "2025" "2026" integral`
6. `"anticanonical" "cohomology" "torsion" family 2024 2025 2026`
7. `"Looijenga" "cohomology" "family" "torsion"`
8. `"anticanonical" "relative" "cohomology" "period"`
9. `"q-Painlevé" "cohomology" "integral"`
10. `"Halphen" "cohomology" "Smith"`
11. `"Looijenga pairs" "characteristic" "integral"`
12. `"nodal" "Poincaré" "Fourier-Mukai" "family"`

这些查询明确含 2024–2026。搜索引擎显示的“数月前”并非出版年：GHK 的作者 PDF 标明 arXiv v5 日期为 2014-06-30，其出版信息是 2015；FHHO 最新文本则由 arXiv 元数据和正文共同确认是 2026-04-28 的 v2。查询噪声、未命中和仅含近似词汇均不计新意证据。

## 4. Primary 来源表：实读定理与包含映射

“未覆盖”仅指所列实际陈述与阅读范围，不替未读全文或整个学科作否定判断。

| 来源与版本 | 实读范围／访问状态 | 准确旧结果与靶标映射 |
|---|---|---|
| Gross–Hacking–Keel, *Moduli of surfaces with an anti-canonical cycle*, Compositio Math. 151 (2015), 265–291，DOI 10.1112/S0010437X14007611；[arXiv 元数据](https://arxiv.org/abs/1211.6367)、[作者 v5](https://paulhacking.github.io/mlp.pdf) | 读 §1 开头与基础条件；Example 5.6 全段；Construction 5.7、Remarks 5.8–5.9、Lemma 5.10、Corollary 5.11；§6 定理前定义及 Theorem 6.1 陈述和证明。未读全文。 | 全篇 $k=\mathbb C$。Construction 5.7 是扭环上沿截面吹起，Lemma 5.10 识别标记周期，Theorem 6.1 描述模空间／栈。故“通用周期族”已有；未给 (T)。Corollary 5.11 的 $\phi(\alpha)=1$ 是根超环，不能直接替换成 $jD$ 的共振模。 |
| Robert Friedman, *On the geometry of anticanonical pairs*, [arXiv:1502.02560v2](https://arxiv.org/pdf/1502.02560)，2016-07-22 修订的作者预印本 | 读引言、§1 条件及 Lemmas 1.6–1.7；§3 Definitions 3.7、3.9 与 Theorem 3.11 的陈述／证明；定点读 Theorems 3.16–3.17 及随后构造说明。未读全文；此处不补造已出版 venue。 | 全篇在 $\mathbb C$；1.6 给有向 $\operatorname{Pic}^0(D)\simeq\mathbb G_m$ 粘合，1.7 给零多重次数截面判据。3.11 的基明确为 reduced connected analytic space。周期的局部／整体性质不是整系数 $R^1p_*L_n$ 的扩张分裂定理。 |
| The Stacks Project, [07VJ：Lemma 30.22.1、Remark 30.22.2](https://stacks.math.columbia.edu/tag/07VJ) | 实读完整命题、证明及 remark；不依赖页面评论。 | $R$ Noetherian、$p$ proper、$L_n$ coherent 且对基 flat，即直接满足其条件：$R\Gamma$ perfect，且与任意派生基变换相容。只断言存在有限 projective 复形，不规定其矩阵为 $\operatorname{diag}(1-q^j)$。 |
| The Stacks Project, [0A1G：Lemma 36.30.1、Remark 36.30.2、Lemma 36.30.4](https://stacks.math.columbia.edu/tag/0A1G) | 读上述陈述及返回的证明；没有递归核读全部引用引理。 | 对 proper、flat、finite presentation 的 $p$ 和 perfect 的 $L_n$，36.30.4 再次直接覆盖 perfectness／任意派生基变换。该一般性本身须扣除；不包含 (T) 的显式分裂。 |
| Bousseau–Brini–van Garrel, *Stable maps to Looijenga pairs*, Geom. Topol. 28 (2024), 393–496，DOI 10.2140/gt.2024.28.393；[arXiv 元数据／摘要](https://arxiv.org/abs/2011.08830) | 实读摘要、作者、版本与出版元数据；未把搜索返回的零散正文当作全文核读。 | 摘要对象是复数对在正性条件下的若干曲线计数理论。仅作 2024 邻域筛查，不据摘要排除正文全部潜在工具；未取得 (T)/(S) 的包含定理。 |
| Yannik Schuler, *The log-open correspondence for two-component Looijenga pairs*, Forum Math. Sigma 13 (2025), e102，DOI 10.1017/fms.2025.10042；[出版原文](https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/logopen-correspondence-for-twocomponent-looijenga-pairs/E895DF32C1450AFD55D0388F471B4B14) | 实读元数据、摘要、§1.1 的 Assumption ★、Theorem 1.2、Corollary 1.3；亦读 Theorem 1.5 的陈述。未读证明。 | 两分量、$D_2^2\ge0$ 等条件下的 log/open GW 对应与 BPS 整性。八个 $(-2)$ 分量与本题相干上同调不满足这一直接映射；这里的 integrality 不是 (S)。 |
| Franco–Hanson–Horn–Oliveira, *Fourier–Mukai transforms and normalisation of nodal curves*, [arXiv:2405.11860v2](https://arxiv.org/abs/2405.11860)，2026-04-28；[作者 HTML](https://arxiv.org/html/2405.11860v2) | 实读摘要、§1 开头、§1.1 Theorem A 完整陈述和相邻说明、§2.1 开头；未核 §5 证明。机构 PDF 的网页分段读取超时；同一公开 PDF 流式文本读取成功，随后在 arXiv HTML 确认版本及定理。未保存 PDF。 | 对 $\mathbb C$ 上 integral nodal projective curve 及部分正规化，Theorem A 比较紧化 Jacobian 的 Poincaré 层和 Fourier–Mukai 变换。不是八分量 $D$，更不是 $S_R$ 上 $L_n$ 的推送；术语 integral 在此指整曲线，不指 $\mathbb Z$ 上的系数。 |
| Eduard Looijenga, *Rational surfaces with an anti-canonical cycle*, Ann. of Math. 114 (1981), 267–322；[期刊原站](https://annals.math.princeton.edu/1981/114-2/p03) | 本轮仅期刊元数据；未读取原论文定理，不从 GHK/Friedman 的引用冒充亲读。 | 保留基础文献入口及原文核查缺口；本件不对该文全部结论作精确包含／排除结论。 |
| Jennifer Li–Sebastián Torres, *Rational surfaces with a non-arithmetic automorphism group*, Bull. London Math. Soc. 56 (2024), 3895–3904；[出版原站](https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/blms.13175) | 实际可稳定回读的是作者、日期、DOI 等元数据。搜索曾返回 §2 片段，但后续打开未返回完整正文，故降为访问不完整。 | 不以题名或片段作“不包含”的定理级结论。没有将该项算作完整排除的先例。 |

## 5. 一般工具与真正待查差额

最接近的几何实例不止一般题名相似：[GHK v5 Example 5.6](https://paulhacking.github.io/mlp.pdf) 从 $\mathbb F_1$ 的四次节点吹起、四个内点吹起得到八个 $(-2)$ 圈，并说明 $D^\perp$ 无平方 $-2$ 根；恒等周期时有无穷纤维为 $D$ 的椭圆纤维化、无其他可约纤维，Mordell–Weil 秩为一。本轮已实读这整段，必须作为更近的已发表几何先例扣除。尚未构造它到本 qPI 模型的精确整坐标同构；其复几何或 Mordell–Weil 识别也不等于 (T)/(S) 的整系数上同调包含。

### 5.1 不能重复计为新贡献的部分

- N 的节点环有向粘合、$\operatorname{Pic}^0\simeq\mathbb G_m$ 与 $q^{-1}$ 的具体坐标计算属于标准方法及本题实例识别；Friedman 的已读基础引理说明其一般背景。反向环使乘子取逆，不改变 $1-q^j$ 的主理想。
- GHK 已将“沿周期参数截面吹起的族”作为一般构造；本题四个单位坐标嵌入这一构造模式，不因把参数记为 $q,t$ 就成为新通用族理论。把其复数模空间定理延伸到整个 $\mathbb Z$ 基仍需自己的合法论证，不能自动引用。
- 边界正规化给两项复形、除子短正合列给过滤，及 DVR 上长度可加／有限模结构／圆分赋值的使用均是通用工具。即使最终得到全部 Smith 指数，单独的赋值整理也不能与真正的扩张消失重复计为两个新机制。
- perfectness 和**任意派生基变换**由表中 Stacks 命题直接覆盖。新的若有，只是找到了该 perfect object 的具体对角模型，而不是发现基变换原则。
- U 从商模的长度一自由分解得到 $\operatorname{Ext}^2$ 消失，再由截断三角取得派生分裂，以及对角呈示的 Fitting 公式，均按标准同调代数／交换代数处理。作者 U 自己也明确不把这些推论分别计为新方法；本件保留这一扣除。

### 5.2 为何已有周期或边界结果还不等于 (T)

以下是本件对已读定理与目标的逻辑范围比较，不是对 (T) 的证明。

第一，周期确定 $L_n|_D$ 的粘合乘子，只确定边界层的 kernel/cokernel。它没有指定嵌入曲面后
$$0\longrightarrow L_{j-1}\longrightarrow L_j\longrightarrow\mathcal O_D(jD)\longrightarrow0$$
的推送连接态射。故边界的 $1-q^j$ 复形与曲面的逐项直和不可混同。

第二，根超环、$q$ 在域中的有限阶、或每个闭点的上同调维数，均不能在本轮来源映射中替代 $R/(1-q^j)$ 的概形级结构。特别是在剩余特征整除 $j$ 时，改到约化支撑会遗失本题正要识别的信息。

第三，(S) 必须以前述模或复形分裂为输入。G 中已有的长度 $ae$、最少生成元数 $p^a-1$ 和 associated graded 并不是本轮被比较的完整 Smith 分类；不能用旧 G 与标准模结构定理的名称代替扩张类处理。

第四，本题给定的 $C_j$ 机制要求核准原迹、全共振基上的延拓、边界单位性及 Bockstein 接口。所读 GHK/Friedman/Stacks 陈述没有自动提供这四项。此处不推断其一定困难或一定新，只定位尚未由实际来源扣尽的部分。

### 5.3 什么样的通用先例会把候选进一步降为普通实例

若已有一般相对反典范定理，针对含本八环的整系数／任意特征族，在周期 $u$ 的整个挠点闭子概形上给出边界单位截面，且推出
$$Rp_*\mathcal O(nD)\simeq\mathcal O\oplus\bigoplus_{j=1}^n[\mathcal O\xrightarrow{1-u^j}\mathcal O],$$
那么将 $u=q$ 或 $q^{-1}$ 代入就会包含 (T) 的主体；(S) 再只是圆分特化。本轮没有取得这样的原文，但也没有排除它存在。仅有一般 Poincaré 层／节点曲线 Fourier–Mukai 理论，尚不足以在不补曲面连接态射的情况下完成这一包含映射。

## 6. 保留旧 G 来源差额，不挪用其他部分的新意

[旧预筛 §3–4](PAPER30_QPI_COHOMOLOGY_SOURCE_SCREEN_V1_20260909.md) 的扣除继续有效：STT 的复数 Okamoto–Painlevé 对变形量与本题 $H^1(\mathcal O(nD))$ 不同；其已读范围也不是整系数模定理。本轮没有重搜该日志或重做普通 Halphen 判据，不把“不重复检索”写成新的排除证据。

同一旧件关于 Vlasenko Theorem 1(i) 覆盖 Hasse 几何级数次幂迭代的具体扣除也保留；本轮未亲读 Vlasenko/Achter–Howe，故这里只引用已记录的来源差分，不冒充新核查。新增的上同调分裂即便成立，也不会使原 Hasse 迭代工具重新变新。

G 的正常延拓、逐纤维平坦、边界长正合列与 DVR 长度均继续按标准工具扣除。旧 G 的同一完整模型、原 pencil 退化与整除微分的规范识别是它自己的待评价组合；本件并未通过新增 (T)/(S) 给该组合补一张新意票。

## 7. 交付与未覆盖范围

本件完成了有界定向核查：十二条查询、若干准确 primary 定理／条件映射，并覆盖 2024 出版、2025 出版、2026 修订近邻。实读范围不足以授予全球新颖性结论，尤其未穷尽一般相对 Halphen/反典范对的整系数扩张分类、历史原文及未公开工作。

本次只新增本报告。未写新证明、未改作者 G/N 或旧来源预筛，未创建论文项目、publication/source lock、稿件或 PDF；未计算票数、分数或篇幅。research-lit 只影响来源分级与访问缺口披露，没有触发外部写入。

绑定输入 SHA-256：

| 输入 | SHA-256 |
|---|---|
| G 完整模型诊断 | `59b308f605832d82e00720c5a3a7871c862698e194503ff3b289da592ced28e0` |
| 旧上同调来源预筛 | `12628cbef7904732212424ee545451e709438d4d2a23909d6f2d3e69117ae6ad` |
| N 法丛入口 | `8234b5584adba10ec02adb0269300b0c5191b5445fca345e28e1eb5171c12469` |
| U 通用整系数上同调作者诊断 | `a1e50c82c32f5411dce28a2bf2ff2b10bf4fdefdb8ac9b127de852de5e36c42b` |

本报告写入后全文回读；交付消息另报本报告 SHA-256，避免自引用哈希。
