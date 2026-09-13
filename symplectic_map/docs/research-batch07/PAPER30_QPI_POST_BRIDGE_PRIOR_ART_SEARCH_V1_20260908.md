# Paper30 qPI 新结果：Phase A/B 定向查新证据包 V1

日期／检索截止：2026-09-08（UTC）。
范围：novelty-check 的 claim 抽取与多来源检索，配合 research-lit；不是正式四门评分、立项票、Route 评价或数学独审。
唯一新增文件为本件；未修改作者证明、原报告、锁或论文项目，未生成稿件／PDF，未进行外部写入。

## 1. 有界结论

在下列实际读取的一手来源中，未找到直接覆盖 A–C 全部量词及实际对象识别的既成定理。
这只是本次公开定向检索的结果，全球新意仍为 `UNCERTAIN`；不据此给出 HIGH、分数或 PROCEED 票。
最重要的扣除不是“未搜到同名文章”，而是以下三点：

1. A 的光滑椭圆层周期窗口及同一实数重叠阈值，在 JRV 2006 已有；剩余增量必须落在原 qPI 的全参数、完整状态和奇异层覆盖。
2. B 的法丛阶与最小 Halphen pencil 的一般联系已有全特征定理；复数域单位根 q-Painlevé 的 Halphen 机制亦已有。2024 年 Mizuno 还列有与作者实际计算同型的平方为 −8 的秩二边界正交格。因此，不能把一般机制、抽象格或复数域一般亏格一单独包装为新理论。
3. C 除 Beauville 谱对应外，还必须扣除 Inoue–Vanhaecke–Yamazaki 2015 的循环谱约化、商曲线 Jacobian 及拉回单射性。可定位的增量是原 JR 矩阵到实际二维动力纤维的有理逆、固定谱线丛差和任意有限阶／全部特征的精确对接。

出处及其读取边界见第 4–6 节。本件不以本地独审票判断新意，也不把作者待完成的准确坏值桥作为已接受结果。

## 2. Phase A：三个精确 claim

统一对象：JR 原映射

\[
F_t(x,y)=\left(\frac{st}{sx-y},\frac{sx}{y}\right),\qquad t\mapsto st,
\]

及其原完整初值空间／状态，原积分为 \(I_r\)，\(s\) 的精确有限阶为 \(r\)。
正特征时自动 \(p\nmid r\)。不能改换参数、只取环面点或仅取光滑能级。

### A. 原全部状态的 Hasse 上界与原 ceil 分箱

对任意有限域 \(\mathbb F_q\)、\(s,t\ne0\) 及任意完整一步周期轨道，设最小周期为 \(m\)，
则 reduced length 精确为 \(\ell=m/r\)。目标是 JR Conjecture 1.2.A/B 的原结论：

\[
N_\pm=q+1\pm2\sqrt q,\qquad
M_q=\left\lceil(\sqrt q+q^{-1/2}-2)/4\right\rceil,
\]

\[
\ell\le N_+,
\qquad
\ell\in\bigcup_{1\le j\le M_q}B_j^{(q)},\quad
B_j^{(q)}=\begin{cases}[N_-/j,N_+/j],&j<M_q,\\[1,N_+/M_q],&j=M_q.\end{cases}
\]

机制：实际光滑纤维的回返平移；实际奇异整纤维的唯一奇点固定，其他周期经有理正规化归入
\(\operatorname{PGL}_2(\mathbb F_q)\) 的分支，周期整除 \(q-1\) 或 \(q+1\)，或等于 \(p\)。
真正待比较的不是 Hasse／有限群分类本身，而是该机制对上述原对象及全部合法状态的覆盖。

### B. 原八次吹起上的全特征几何与实际临界概形

对每个非零固定 \(t\)、全部特征（含 2、3），在实际紧化 \(S\) 及 \(D=-K_S\) 上：

- \(\mathcal O_D(D)\) 的精确阶为 \(r\)，原 \(1,I_r\) 生成最小完整 \(|rD|\)；
- 原泛纤维光滑、几何整、亏格一；
- 每个有限概形纤维均几何整且约化；坏纤维只有一个节点／尖点，正规化为 \(\mathbb P^1\)；
- 实际 \(Z(dI_r)\subset S\setminus D\) 长度恰为 4，保留小特征下的真实局部重数。

本件不把“有四次谱判别式”替代为“实际临界概形长度四”，也不把泛光滑与全部有限纤维整性混同。

### C. 实际泛动力纤维的 Jacobian 与循环谱商

令 \(K=k(c)\)、\(T=t^r\)、\(\varepsilon=(-1)^{r+1}\)，实际泛纤维为 \(X/K\)。
目标是原参数上的 \(\operatorname{Jac}(X)\simeq E\)，其中

\[
E:\quad\lambda^2-(T+cZ+Z^2)\lambda+\varepsilon Z^3=0.
\]

实际桥包括：原 \(M(z)\) 的谱线丛；端点系数恢复原 \(x,y\) 的有理逆；
\(\sigma^*L\otimes L^{-1}\) 为固定除子类；循环商 \(\pi:C\to E\) 的 \(\pi^*\) 无核。
这里不是只知两条曲线同亏格，也不是未排纯不可分次数的几何点单射，亦不擅自平凡化 \(K\)-torsor。

### 输入身份与本轮读取范围

以下均为本地作者输入，不是外部先例；本件只消费其精确主张并定向读相应机制，未重新作数学验收。

| 作者文件 | 本轮读取范围 | SHA256 |
|---|---|---|
| [A 全轨道](PAPER30_QPI_ALL_ORBIT_HASSE_BINS_ENTRY_V1_20260908.md) | Claim、依赖、原定义／来源、策略，行 1–110；标题定位 | `78191a3faa7d2a867e45eccd708b106b722d43e6f5ea73d583e0385637be2469` |
| [F 实际有限纤维](PAPER30_QPI_ACTUAL_SINGULAR_FIBRE_ENTRY_V1_20260908.md) | 行 1–110、Steps 2–5（206–344），另定向读取格的显示等式 | `3b7a495b723d9ba45003fe767431c4420053c0b3de6656a2335c3aad01307003` |
| [J 泛 Jacobian 桥](PAPER30_QPI_LAX_JACOBIAN_BRIDGE_ENTRY_V1_20260908.md) | 行 1–116、Steps 4–6（290–425） | `a6aa5e30ea0795b05790b058dfd4debc6431de1918090b9a6add88351a1eb63f` |
| [N 法丛](PAPER30_QPI_BOUNDARY_NORMAL_BUNDLE_ENTRY_V1_20260908.md) | Claim 标题定位、Steps 6–7（205–270） | `8234b5584adba10ec02adb0269300b0c5191b5445fca345e28e1eb5171c12469` |
| [G 原始一般亏格一](PAPER30_QPI_PRIMITIVE_GENUS_ONE_BRIDGE_V1_20260908.md) | Claim／来源标题定位、Steps 4–5（167–239） | `0d7a3e2d37eb7218feddfe5c85bf244a0be358bfcc880279d5f14afd5cb77ace` |

查新过程中主控另通知：准确坏值桥已形成 \(R_{\rm actual}=\delta\) 的更强候选思路，涉及
\(y^2+cxy-\varepsilon Ty=x^3-Tx^2\)、实际局部截面、最小正则模型及相对微分 Fitting 理想。
截至本证据包成稿，本任务未接收并核对其最终作者全文／新独审；记为 `PENDING`。
它不改变 A–C 本件的输入身份，也不进入“已接受新定理”或新意评分。

## 3. Phase B：来源选择、检索记录与空白

完整读取 novelty-check、research-lit 技能后执行其来源部分。Phase C 不在本委派范围；
技能指定的 GPT-5.4 Codex MCP 未配置可调用接口，未假称调用、未以同模型子任务冒充跨模型验证。
ICLR 2025/2026、NeurIPS 2025、ICML 2025/2026 与本纯代数／算术动力问题无直接领域对应，明确跳过，未编造相关 ML 文献。

### 3.1 来源可用性

| 来源 | 实际执行及限制 |
|---|---|
| 本地 PDF 优先 | 先列 `papers/`、`literature/` 中 PDF 文件名，并以 qPI／Painlevé／Halphen／Jogia／Beauville／IntegrabilityRS 定向过滤；无相关题名 PDF。没有打开无关旧论文 PDF，也未重扫旧构建内容。 |
| Zotero／Obsidian | 可用工具元数据中无对应连接；未捏造库检索结果。 |
| arXiv | 未定位到任务相关可用 `arxiv_fetch.py`，按 research-lit 允许的公开 WebSearch 回退；实际打开 arXiv abstract、HTML／PDF及 submission history。未声称 arXiv API 成功。 |
| Google Scholar | 从原 arXiv 页面点击 Scholar：重定向到 Google sorry/security 页面并失败；停止该路径。另作公开 `site:scholar.google.com` 定向搜索，无可用新增记录。 |
| Semantic Scholar | 原 arXiv 的引用入口重定向到 paper 页面时工具报 non-retryable safe-open 错误；另作公开 `site:semanticscholar.org` 题名查询，无可用新增记录。没有声称已查完整引文图。 |
| Consensus | 实际执行下列两条定向查询；第一条零结果，第二条返回 IVY 及两个不同 Mumford 系统条目。对 IVY 执行 required `fetch`，仅得作者／年份／arXiv 类别等书目元数据，明确返回摘要不可用；没有把索引命中当全文阅读或独立新证明。该库将 IVY 记为2013年预印本，本包定理阅读仍以实际取得的一手1312.4208全文为据。 |
| 作者／期刊公开源 | 正常访问作者网页、作者托管 PDF、期刊 DOI；IOP 为公开搜索索引片段可读而 direct open 失败；Beauville 官方入口要求安全检查。未换身份、解挑战或绕过访问限制。 |
| 文件保存 | 未下载 PDF 到工作区。JRV06 作者公开 PDF 因浏览器抓取超时，使用普通公开 GET 经 `pdftotext` 输出到标准输出完成定向阅读；无持久化 PDF。 |

### 3.2 每个 claim 的至少三种检索式

以下字符串均实际提交过。年份词查询不是数据库穷尽过滤；故另做明确日期窗及作者近期论文核对。
命中二手聚合、搜索生成的 open-problem 页面和无关同名结果只作线索，不作为定理证据。

| Claim | Query | 主要结果／处置 |
|---|---|---|
| A1 | `"q-Painlevé I" "finite fields" proof 2024 2025 2026` | JR 及非同方程的有限域初值空间文献；转读 JR 原文。 |
| A2 | `"Arithmetic dynamics of a discrete Painlevé equation" conjecture proof correction 2026` | JR 作者／出版版本；未返回可核实新证明或勘误。 |
| A3 | `"Painlevé" "Hasse" "bins" 2024 2025 2026` | JR 与既有 Hasse-window 背景；追读 JRV06。 |
| A4 | `site:arxiv.org "q-Painlevé" "finite fields" after:2026-03-08 before:2026-09-09` | 此精确式无结果；不能推成半年无论文。 |
| A5 | `"2508.18578" proof correction erratum after:2026-03-08 before:2026-09-09` | 未得新证明／勘误一手来源。 |
| B1 | `"q Painlevé" "Halphen" "root of unity" 2024 2025 2026` | JR Remark 3.5、CT／Halphen 理论；另追读 CD。 |
| B2 | `"Painlevé" "normal bundle" "finite fields" 2024 2025 2026` | 无直接覆盖实际法丛／全量词的新来源。 |
| B3 | `"Painlevé" "singular fibres" "characteristic" "2026"` | 定位 JR 2026 后继工作，另族，见第 5 节。 |
| B4 | `site:arxiv.org "Halphen" "characteristic" after:2026-03-08 before:2026-09-09` | 此精确式无结果。 |
| B5 | `"q-Painlevé I" "genus" "2024"` 与 `"q-Painlevé" "Halphen" "2026"` | 扩展检索定位 Mizuno 2024、Stokes 等 2025，打开一手正文。 |
| C1 | `"q-Painlevé I" "Jacobian" "spectral curve" 2024 2025 2026` | 未得实际 JR 泛纤维桥的直接新定理。 |
| C2 | `"Joshi" "Roffelsen" "spectral" "proof" "2026"` | 定位 2026 年 2 月／7 月新文及作者写作列表。 |
| C3 | `"Painlevé" "cyclic" "spectral sheaf" "root of unity"` | 追索谱自同构路线，定位 IVY 2015 的强方法先例。 |
| C4 | `site:arxiv.org "Painlevé" "spectral" "Jacobian" after:2026-03-08 before:2026-09-09` | 此精确式无结果；后继文由作者／题名路线另行找到。 |
| C5 | `"Algebraic integrable systems related to spectral curves with automorphisms" arxiv` | 获取 1312.4208 并读相关定理与证明。 |

还执行了作者题名／编号、`IntegrabilityRS.pdf`、`Jogia Roberts Vivaldi ... pdf`、Beauville 题名／DOI等定向查询。
出版版 3.6 的精确追索式为 `"Arithmetic dynamics" "ae67bf" "3.6" "Remark"`。
Consensus 两条实际提交式为 `"Arithmetic dynamics of a discrete Painlevé equation" "q-Painlevé" finite fields genus proof year:2024-2026`
和 `"Algebraic integrable systems related to spectral curves with automorphisms" Jacobian cyclic quotient`。
其中 IVY `fetch` 记录编号为 `8816e98c16bc5b62bf3106e63415e9e4`；未检得新对象证明，不将零结果外推为穷尽查新。
最近半年定义为 2026-03-08 至 2026-09-08；实际核对到的相关最新一手新文是 2026-07-08 的 2607.06980。
日期采用作者／出版元数据，不将搜索引擎的“几个月前”爬取标签当作发表日期。

## 4. 最近直接先例：JR 的版本与实际证明边界

### 4.1 作者 v2：主对象完全重合，结论仍为猜想

[Joshi–Roffelsen, *Arithmetic dynamics of a discrete Painlevé equation*, arXiv:2508.18578v2](https://arxiv.org/html/2508.18578v2)。
本轮实际读摘要、§1.1（Definitions 1.1／Conjecture 1.2／Remark 1.3）、§2.1–2.2 的状态定义和算法、
§3.1 Theorem 3.1 及完整证明、§3.2 全节与§4结论。
外部正文可读定位：HTML 行 390–546 是积分构造，547–600 是亏格／谱条件及结论。

原积分、完整 states、reduced length 定义、谱方程和四次候选坏值式均为先例，不计新发现。
作者对一般亏格及准确退化作 Conjecture 3.6；其谱奇点到动力奇点的说明没有写出本件 C 的逆重建和无核 Jacobian 桥。
不能把摘要中的强措辞当成上述猜想已经有完整证明。

[arXiv abstract 的 submission history](https://arxiv.org/abs/2508.18578) 本次显示：
v1 为 2025-08-26，v2 为 2026-01-16；没有显示 v3。
这是该入口在截止日的实际记录，不是对作者所有未公开工作的判断。

### 4.2 2026 年出版版：只得到公开索引片段，未取得全文

[JR, *J. Phys. A: Math. Theor.* 59 (2026), 195201, DOI 10.1088/1751-8121/ae67bf](https://doi.org/10.1088/1751-8121/ae67bf)。
公开搜索索引返回日期为 received 2026-01-15、revised 2026-04-07、accepted 2026-05-01、published 2026-05-13。
本轮 direct open DOI 及对应结果引用均 Internal Error；未重试绕过原站。

实际可读索引范围：摘要、§1及部分状态示例、Remark 1.3、Remark 3.2–3.6、部分积分证明公式。
它仍引用 Conjecture 1.2；一般亏格猜想编号变为 3.7。
新增的是 Remark 3.6：有限阶时不能预设差分系统存在通常意义的基本解，应把 Lax pair 当形式差分方程处理。
该片段不是新增泛亏格一、法丛或 Jacobian 定理。

未取得出版 §3.2 的完整陈述及证明文本，故不能保证其所有量词／措辞与作者 v2 逐字一致；
也不把“出版正文已完全恢复访问”写成事实。

### 4.3 作者近期更新／引文核查

实际打开 [Roffelsen 写作列表](https://proffelsen.github.io/writing)，定向读 2026 preprints／该篇 publication 条目。
列表中的 2026 年 2 月与 7 月有限特征工作已跟进正文；其余 qPVI tau／monodromy 题名不冒充 qPI 证明。
本次题名、编号、proof／correction／erratum 查询没有得到可核实的后继 A–C 完整证明或勘误。
Google Scholar／Semantic Scholar 引文图不可用，因此不能宣布完整 forward-citation 查新已经完成。

## 5. 最接近先例、精确读取范围与差异

### 5.1 A：JRV 2006 的窗口先例比泛 Hasse 背景更强

[Jogia–Roberts–Vivaldi, *An algebraic geometric approach to integrable maps of the plane*, J. Phys. A 39 (2006), 1133–1149，作者托管出版 PDF](https://web.maths.unsw.edu.au/~jagr/JRV06.pdf)。
实际读摘要／引言、§2（明确排除特征 2、3）、§3 Theorem 3 及完整证明、§4.1 Theorem 4及其导出与限制，
§5 中 pp.1145–1148 的窗口推导、Corollary 1及证明。
原指明的 [IntegrabilityRS 作者稿](https://web.maths.unsw.edu.au/~jagr/IntegrabilityRS.pdf) 本轮 direct open 失败；
其摘要及特征限制只读到公开索引片段，详细推论以上述可读出版 PDF 为准。

JRV 的光滑平移层已有
\[
N_-/n\le\operatorname{period}\le N_+/n,
\qquad n\ge\sqrt q/4+1/(4\sqrt q)-1/2
\]
的相邻窗口重叠门槛；这与 A 中 \(M_q\) 所取上整的实数相同。
因此“光滑层 Hasse 产生分箱／倒整数窗口”不是本件新发现。
A 的可能增量是原 qPI 全 \(r,t,q\)、全状态并含奇异层的完整证明；不能仅以 \(s\ne1\) 标签声称新机制。

另实际读 [Roberts–Jogia–Vivaldi, *The Hasse-Weil Bound and Integrability Detection in Rational Maps*, JNMP 10 suppl.2 (2003), 166–180](https://web.maths.unsw.edu.au/~jagr/RJV03.pdf)
摘要／§1，以及 §3 Theorems 1–2、推導与奇点／周期讨论（PDF pp.5–8，正文 pp.170–173）。
它已有可积映射、既有积分、不可约层上的 Hasse 上界检测框架；并非原 qPI 任意阶完整状态的定理。

### 5.2 B：Halphen 标准理论及 2024 年抽象格先例

| 来源 | 实际读取 | Overlap／边界 |
|---|---|---|
| [Cantat–Dolgachev, *Rational surfaces with a large group of automorphisms*, arXiv:1106.0930v2](https://arxiv.org/pdf/1106.0930) | 摘要、引言域假设、§2.1 Prop.2.2 的全部陈述及完整证明、Remark 2.3（PDF pp.6–9） | 全特征法丛精确阶 ↔ Halphen index／最小 pencil、唯一多重纤维是强先例；特征2/3明确允许准椭圆，不能直接借为本题泛光滑。 |
| [Carstea–Takenawa, *A classification of two-dimensional integrable mappings and rational elliptic surfaces*, J. Phys. A 45 (2012), 155206；1005.3586v2](https://arxiv.org/pdf/1005.3586v2) | 摘要／引言、复曲面设定；Thm2.2及完整证明、Remark2.3、§3开头单位根推论（PDF pp.1–6） | 复数域乘法型 period／单位根与精确 index、迭代保持 Halphen pencil 已有；不是原 JR Laurent 积分的全特征对象识别。 |
| [Mizuno, *q-Painlevé equations on cluster Poisson varieties via toric geometry*, Selecta Math. 30 (2024),19；2008.11219v4](https://arxiv.org/pdf/2008.11219) | 摘要／引言、Thm1.1/1.2；Thm3.35陈述及其证明开头的附录归约；Appendix A Type \(E_1^{(1)}\)（PDF pp.25–26）；未通读Thm3.35全部其余类型证明 | 明列两根平方−8、交数8与和对应八边界。与 F 的实际整数格抽象同型；尚未核验 toric 标记到 JR 八中心的逐项映射，故不直接授予 B 全量词先例。 |

对 B 应扣除：一般 Riemann–Roch／伴随、法丛 torsion→最小 pencil、正规化亏格公式、最高 Chern 类计数。
本包可定位的消费者增量是原参数下法丛粘合量、原 \(I_r\) 完整 pencil 身份、每个 \(t\) 的小特征泛光滑、
实际全部有限纤维整性及 \(dI_r\) 的长度四。
但长度四的 \(12-8\) 结构与八边界背景高度标准；不宜单独宣称一种新计数理论。
“抽象格已知”不等于“全参数实际纤维结论已直接发表”；反方向也不能把未检出的直接推论自动评为高新意。

### 5.3 C：循环谱商的专门旧文不能漏扣

[Inoue–Vanhaecke–Yamazaki, *Algebraic integrable systems related to spectral curves with automorphisms*, J. Geom. Phys. 87 (2015),198–216；arXiv:1312.4208](https://arxiv.org/pdf/1312.4208)。
实际读摘要／引言、§2 Theorem2.1的陈述与Remark2.2（未宣称通读其全部群上同调证明）；
§4.2–4.4，含 Theorem4.4的 Beauville 对应重述与构造、Prop4.5及前置推导、Thm4.6及完整证明。

其复数域素数阶循环谱模型已把固定矩阵商的连通分支识别为商曲线 Jacobian 开集，且明确证明拉回单射。
这一框架与 C 的后半段很接近。它采用秩等于循环素数阶的矩阵空间；本题则是实际秩二 \(M\)、任意 \(r\)、全特征，
还需真正的动力坐标逆及谱线丛差固定性。不能从该文直接断言本题同构，也不能把循环不变 Picard 思路算作新方法。

[Beauville, *Jacobiennes des courbes spectrales et systèmes hamiltoniens complètement intégrables*, Acta Math.164 (1990),211–235](https://doi.org/10.1007/BF02392754)：
本轮清华公开 PDF 的 WebFetch 失败，普通 GET 返回500；正式 DOI转到ProjectEuclid后要求安全检查，随即停止。
仅实际取得原文题名／书目及开头的公开索引，不声称本轮读到原文 Thm1.4 的完整证明。
标准谱矩阵／Picard对应的实质扣除依据是上列 IVY §4.3 明确重述并解释的 Beauville Thm1.4；
这是清楚标识的文献传递，不伪称 Beauville 本次一手全文复读成功。

该缺口并不使标准谱对应变为未知新成果，但限制本件对 Beauville 原文全部特征条件及更细模论细节的独立核验。

### 5.4 2024–2026 最近邻：已打开，不是本题直接新证明

| 来源 | 实际读取范围 | 对 A–C 的意义 |
|---|---|---|
| [Joshi–Roffelsen, *On integrals of non-autonomous dynamical systems in finite characteristic*, 2602.09298v1，2026-02-10](https://arxiv.org/html/2602.09298v1) | 摘要、§1引言／相关工作、§2 Definition2.1及Thm2.2陈述、§6结论及genus问题；未通读Thm2.2证明 | 对象为PIV／dPII（兼projective reduction到dPI），积分与可约层／Riccati关系；不当作原qPI准确纤维或全轨道证明。 |
| [Joshi–Lasic Latimer–Roffelsen, *On difference-differential Lax pairs and integrals of Painlevé equations in finite characteristic*, 2607.06980v1，2026-07-08](https://arxiv.org/html/2607.06980v1) | 摘要、§1全引言／相关工作、§2 Prop2.1及证明、Lemma2.2陈述、Thm2.3及证明；未通读技术附录 | 有限特征周期乘积产生积分的推广。§1仍称旧qPI曲线一般椭圆为猜想；本次最近半年关键一手对照，不含原qPI的A–C桥。 |
| [Stokes–Takenawa–Carstea, *On the geometry of a 4-dimensional extension of a q-Painlevé I equation with symmetry type A1(1)*, 2506.21092v1，2025-06-26](https://arxiv.org/html/2506.21092v1) | 摘要、§1前部相关工作、§4.3 Prop4.5／Cor4.6及邻接说明；未完整审查其28次吹起 | 四维扩展、28个中心及二维反典范线性系，非当前二维八中心问题；只作对象排除和一般几何背景。 |

Mizuno 的卷期年为2024而 arXiv 初稿为2020、v4为2024-02-08，已由 [arXiv metadata](https://arxiv.org/abs/2008.11219) 核定；
没有因为它被“近期”查询命中而误报成2026新文。
其他检索返回的连续 Painlevé 渐近、SCFT／Seiberg–Witten、Darboux–Halphen、数值神经网络等未见本题对象重合，未计作最接近文献。

## 6. 每项 delta 与查新风险结论

| Claim | 最近／最强先例 | 有限检索后保留的精确 delta | 查新风险 |
|---|---|---|---|
| A | JR原猜想与状态；JRV06窗口／阈值；RJV03 Hasse框架 | 原qPI任意有限阶、所有参数／有限域、完整原states、奇异层不删状态地进入原bins | 通用数学含量需认真扣除；光滑层或分箱单独包装不成立。尚无完整forward-citation覆盖，全球UNCERTAIN。 |
| B | CD全特征Halphen；CT复数域单位根；Mizuno已知格；JR一般亏格猜想 | 原积分与原紧化的逐项全特征／每个t对接、泛光滑排准椭圆、全部有限整纤维、实际临界概形 | 很多结论可能是标准几何的专门推论；必须评估实际对接是否足够非平凡，不能靠全特征标签直接加分。Mizuno标记身份尚未核完。 |
| C | JR原谱式；Beauville谱对应；IVY循环谱商／Jacobian／拉回单射 | 实际M恢复x,y的有理逆、固定谱差、任意r且全特征的无核桥及K上torsor身份 | IVY方法overlap较强；需把“通用循环谱约化”与“真实qPI识别”分开。Beauville全文本轮不可获取。 |

没有把三项拆作三篇立项建议。A、B、C 是同一问题的相互支撑模块，不把多个标准工具的拼合数当贡献数。
准确 \(R_{\rm actual}=\delta\) 若以后被接受，应另核对其与原猜想、Weierstrass模型和最小正则模型理论的差异；
本件不预支这一结论，也不以未来关闭去提高当前新意。

## 7. 交接与未完成来源义务

- 本件已完成规定的 Phase A/B 有界来源工作及现有来源扣除；没有执行 Phase C、正式评分或独立论文价值／容量判断。
- 出版版正文未完整取得；目前能确认的更号与新增形式 Lax 警告只来自公开索引片段。以后若需逐字引用出版 Conj3.7，须取得其实际全文。
- Beauville 原文 Thm1.4本次未完整取得；保留 IVY 的明确重述作为标准理论扣除，不能隐去这项读取差别。
- Scholar／Semantic 引文图未完整访问；公开检索未找到后继证明不构成全局不存在证明。
- IVY方法先例和JRV同阈值窗口应进入下一轮查新材料；Mizuno与实际标记的关系只列为可核对风险，未将其自动转化为数学反例或强制重审已接受基础。
- 科学状态、查新覆盖和产物状态彼此独立；作者证明或独审接受不等于“全球新”，本件检索成功也不等于数学证明通过。

本文件为2026-09-08单次来源证据快照；结论为有界 `UNCERTAIN`，无正式四门投票。
