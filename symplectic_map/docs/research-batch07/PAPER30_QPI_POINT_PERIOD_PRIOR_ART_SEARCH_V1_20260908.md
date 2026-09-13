# Paper30 qPI：准确回返点、闭纤维周期与自治置换对应的 Phase A/B 来源包 V1

日期／公开检索截止：2026-09-08（UTC）。作者侧有界查新；不是 Phase C、正式评分、四门票、数学独审或候选修订。
本件只保存本次实检证据，不把新结果写入任何旧冻结 candidate。未新建论文、锁、稿件或 PDF，未作外部写入。

## 1. 结论先行与状态边界

在本次实际读取的一手文献范围内，未定位到直接覆盖下述 C1–C4 全部量词和真实原动力识别的既成定理；全球先例状态仍为 `UNCERTAIN`。
这不是“全球不存在”的结论，也不是新意高低、可发表性或可过门判断。

需要明确扣除的最强重合是：

1. **同一曲线族已经存在。** 本题 $W$ 经 $Y=\varepsilon v$、$a=1-\varepsilon c$ 变为经典 Tate 标准形
   $Y^2+(1-a)uY-TY=u^3-Tu^2$。Sutherland 2012 直接研究此两参数族及 $(0,0)$ 在有限域的点阶；
   本题回返点变成它的负点 $(0,T)$。不能把 $W$ 或这个标记点坐标当新曲线／新标记族。
2. **光滑层的完整等长分解已经存在。** JRV06 实际 §4.2、式(37)前，明确给出所有轨道的共同周期
   $\operatorname{ord}\omega$，且轨道数乘周期等于 $\#W$；不只是 Hasse 上界或窗口的弱背景。
3. **准确平移点这一表示方式已经存在。** Tsuda 2004 的 QRT 模型明确写成在 Weierstrass 曲线上加 $(0,0)$；
   Beauville／IVY 的谱线丛及循环谱商 Jacobian 机制也必须扣除。
4. **节点／尖点的乘法／加法群机制不是新理论。** 由有限群上的平移得到等长循环、由唯一奇点得到固定点，
   也不能单独计为本题新贡献。

因此可比较的精确差额只能是：原 JR 时间矩阵产生哪个有向除子；它对原参数、原域 torsor、所有允许阶和特征的准确作用；
该同一作用如何覆盖每条原闭纤维；以及 C4 拟议的原回返置换与自治参数 $T=t^r$ 的全状态共轭。
这些差额的数学完成状态和查新状态分开记录。

## 2. Phase A：本次比较的精确 claims

统一原映射及参数约定：

$$
F_t(x,y)=\left(\frac{st}{sx-y},\frac{sx}{y}\right),\qquad t\mapsto st,
\quad \operatorname{ord}(s)=r,\quad T=t^r,\quad\varepsilon=(-1)^{r+1},\quad t\ne0.
$$

“全部状态”指原已解消初值空间的状态，不能仅取有理公式无分母的环面开集。
“有限纤维”指原积分 $c$ 的有限值纤维，不包含无穷远多重边界。

### C1. 原时间矩阵的准确谱模除子与泛回返点

原谱曲线及其循环商为

$$
C:\lambda^2-(T+cz^r+z^{2r})\lambda+\varepsilon z^{3r}=0,
\qquad E:\lambda^2-(T+cZ+Z^2)\lambda+\varepsilon Z^3=0,\quad Z=z^r.
$$

在输入固定的原域谱模／torsor约定下，一步 $B$ 的谱线丛同态具有准确除子 $P_T-P_0$，
完整 $r$ 步回返是加 $p_T$，在

$$W:v^2+cuv-\varepsilon Tv=u^3-Tu^2$$

上准确为加 $P=(0,\varepsilon T)=-(0,0)$，且此点在 $k_0(c)$ 上非挠。
量词是全部允许 $r$、全部特征（包括 2、3）、每个固定 $t\ne0$，不预设泛 torsor 有原域点。
这里必须同时指定作用约定，不能从其他自治坐标任取同号平移点。

**输入状态：** 已收到完整作者证明；本件只比对其主张，不授予新的数学接受。

### C2. 全部有限光滑纤维的准确周期和循环数

拟在每个有限域上的每条光滑闭纤维，证明原回返是 C1 的同一准确点作用，而非仅有某个未知平移。
若 $N=\#W(\mathbb F_q)$、$d=\operatorname{ord}P$，则该纤维每个状态的回返最小周期为 $d$、循环数为 $N/d$，
固定 $t\langle s\rangle$ 时间轨道上完整一步周期为 $rd$。

**输入状态：** 主控正在证明；本件没有读取或预先接受其新证明。泛等式不能在本件中自动充作全部特化定理。

### C3. 全部坏纤维的显式参数、群元素和真实周期

拟对每条坏纤维写出纯 $W$ 的节点／尖点参数化，以及同一 $P$ 在乘法／加法坐标中的准确元素。
有限域上节点光滑点数为 $q-1$ 或 $q+1$，尖点光滑点数为 $q$；非奇异状态分解为同一点平移的等长循环，
唯一奇点固定。需要另证明这些描述与**真实原 qPI** 在整条闭纤维上的共轭，包含原例外线状态。

**输入状态：** 纯 $W$ 显式部分由另一作者在证明，真实原动力桥由主控继续处理；两层都不写成已接受。
本件未取得待写的具体节点斜率／乘子表达式，故能查的是结构目标及同族，而非对尚未收到的式子逐字符查重。

### C4. 后续追加的自治置换对应与循环悬挂

主控追加的拟推论：固定同一 $\mathbb F_q$、$s,t$ 后，原完整时间切片上的回返置换 $R_{s,t}$，
经纤维参数 $c\mapsto\varepsilon c$、坐标 $v\mapsto\varepsilon v$ 规范化，与自治原映射 $F_{1,T}$
在完整 $U_{T,1}(\mathbb F_q)$ 上置换共轭。
预期共轭是逐纤维 $\mathbb F_q$ 曲线同构拼成的集合共轭，**不是全曲面代数共轭，也不声称泛 torsor 平凡**。
于是固定时间轨道上的完整 $F$ 为该自治置换的 $r$ 层循环悬挂：一个自治 $d$ 循环对应一个 $rd$ 循环，循环数不变。

**输入状态：** 追加时仍在主控证明，仅作待核查的 finding；不借 C1 完成状态预支 C4。
“周期参数系统的回返是自治映射”这一普通事实，弱于“它共轭于同一原族 $F_{1,t^r}$ 的全部有限域状态置换”。

### 本地输入隔离

只全文读取下面三个获准文件，没有递归读取其中链接的其他本地材料：

| 文件 | 行数 | SHA256 |
|---|---:|---|
| `PAPER30_QPI_EXPLICIT_RETURN_POINT_ENTRY_V1_20260908.md` | 277 | `2ca0b56081c76be343c0b8d86c6a5463533802d4aee8baed7068d992d830a0e7` |
| `PAPER30_QPI_POST_BRIDGE_PRIOR_ART_SEARCH_V1_20260908.md` | 268 | `4470af64294525bc4ae33b9b00fc38c44c38215290a36fa6f3a5b6bdf861f90e` |
| `PAPER30_QPI_EXACT_BAD_VALUES_PRIOR_ART_SUPPLEMENT_V1_20260908.md` | 112 | `2aae448ca17022aa7b51990b84058e57ee455ab0e4c0a4127d8e0ec7fc39c898` |

后两件仅作一手来源索引；其历史评价用语不作为本次判断依据。C4 来自主控追加的明确任务。
未读取新旧正式票、Phase C/D 评分、NON_AUTHOR／REVIEW／DISPOSITION、README、BATCH 或其他代理意见。

## 3. Phase B：实际来源入口和访问边界

全文读取 `novelty-check/SKILL.md` 后只执行 A/B；未执行其 C/D，也未调用跨模型评分。
本纯数学任务不套用 ICLR／NeurIPS／ICML 数据库筛选。未配置、安装或升级任何服务。

| 入口 | 实际执行与边界 |
|---|---|
| Web／arXiv | 实际提交下表检索式，打开 arXiv 摘要、HTML、PDF 和 submission history；没有声称 arXiv API 查询成功。年份词不是严格日期过滤，另提交明确 2024–2026 和最近半年日期窗。 |
| Google Scholar | 从 JR arXiv 页面点击官方 Scholar 引用入口，重定向至 Google sorry/security 页面，工具返回 non-retryable safe-open 错误；停止直接访问。另提交公开 `site:scholar.google.com` 查询，未取得任务相关可读引文记录。 |
| Semantic Scholar | 从 JR arXiv 的 Semantic 引用入口跳转 paper 页失败，non-retryable safe-open；停止此路径。公开 `site:semanticscholar.org` 查询返回无关 PDE／物理片段等，没有成功读取完整引用图或调用 S2 API。 |
| Consensus | 先发现已配置 search／fetch 工具，再实际查询。对报告涉及的 JR、JRV06、Stokes 等三个结果都执行 required fetch；其他返回只当检索线索，不引用其未 fetch 内容为证据。 |
| 官方／作者源 | JRV 作者托管 PDF、Tsuda 作者页及 RIMS 原文、Sutherland arXiv 原文、EMS 原文正常可读；用期刊／作者页核对年份及 DOI。 |
| 访问失败 | JR 出版 DOI direct open 为 Internal Error，只有公开搜索索引片段；Beauville DOI 只返回 ProjectEuclid iframe，没有获得原文定理。Ohyama 作者预印本 PDF 的后续正文读取超时，DOI safe-open 失败。未解挑战、换身份或绕过 rate／permissions。 |
| 本地边界 | 没有下载／缓存 PDF 到工作区，没有扫旧构建树、论文库或新增其他文件；唯一写入为本件。 |

最近半年窗口明确为 **2026-03-08 至 2026-09-08**，查询结束界取 `before:2026-09-09`。
搜索返回的“几个月前”“last week”等爬取标记不当出版时间；这点对 Tsuda 2004、老节点论文等尤其重要。

## 4. 实际 query ledger

下列字符串均实际提交；同批多 query 返回的结果不强行分配为每一式的独立零结果。
“未定位直接先例”只表示未从该检索取得可核实的直接覆盖，不表示数据库穷尽。

| Claim | 实际检索式 | 可核查处置 |
|---|---|---|
| C1 | `"q-Painlevé I" "translation point" "2024" "2025" "2026"` | 近名／一般平移结果；未取得全阶原 B 除子的直接定理。 |
| C1 | `"q-Painlevé" "time evolution" "divisor" spectral curve root unity` | 转核 JR §3.1 与谱方法先例。 |
| C1 | `"2508.18578" translation divisor after:2026-03-08 before:2026-09-09` | 未定位可核实的新增准确点／除子证明。 |
| C1 | `site:arxiv.org "q-Painlevé" "translation" after:2026-03-08 before:2026-09-09` | 定位 2609.02927；实际读摘要／§1，排除其不同 Weyl 表示对象。 |
| C1 | `"q-Painlevé I" "spectral curve" "translation point" 2024..2026` | 补近期窗口，不把引擎范围语法视为完整索引审计。 |
| C2 | `"q-Painlevé I" "finite fields" "period" "point order" 2024 2025 2026` | 转读 JR 与 JRV06；无新增全光滑闭纤维准确点先例。 |
| C2 | `"Arithmetic dynamics of a discrete Painlevé equation" cycles elliptic order` | JR 对象／原频率算法；并非点阶计算已经证明。 |
| C2 | `"q-Painlevé" "cycle" "elliptic" after:2026-03-08 before:2026-09-09` | 未取得直接覆盖 C2 的一手新文。 |
| C2 | `"q-Painlevé I" "point order" "finite field" after:2024-01-01 before:2026-09-09` | 补明确日期窗；近名项不计直接结果。 |
| C3 | `"q-Painlevé I" singular nodal cuspidal multiplicative additive 2024 2025 2026` | 未取得同 W／原动力的全部节点尖点参数公式。 |
| C3 | `"Painlevé" "root of unity" "singular fibres" periodic` | 查到 Halphen 机制与不同系统闭纤维；转读 CT。 |
| C3 | `"q-Painlevé" "singular" "period" after:2026-03-08 before:2026-09-09` | 未定位 C3 直接完整先例。 |
| C3 | `"q-Painlevé" "singular fibers" "root of unity" after:2024-01-01 before:2026-09-09` | 部分命中是旧 CT 内容被近期爬取，不能报成 2026 新定理。 |
| C4 | `"q-Painlevé I" "root of unity" "autonomous" conjugate finite fields 2024 2025 2026` | JR 与一般根单位回返；未取得同族自治 T 的全状态共轭。 |
| C4 | `"Arithmetic dynamics of a discrete Painlevé equation" "t^r" "distribution"` | JR 原公式／频率背景；未取得所提重整化定理。 |
| C4 | `"q-Painlevé" "return map" "autonomous" permutation after:2026-03-08 before:2026-09-09` | 未取得直接覆盖 C4 的一手结果。 |
| C4 | `"q-Painlevé I" "period distribution" rescaling root unity` | 未定位可核实的同族频率相等定理。 |
| C4 | `"q-Painlevé" "cyclic suspension" "finite"` | 无任务相关可核实的一手覆盖。 |
| C4 | `"q-Painlevé" "finite fields" "root of unity" "autonomous" after:2024-01-01 before:2026-09-09` | 补明确近期窗口；取得 JR 等原问题来源。 |

各来源补充查询实际包括：

- Scholar：`site:scholar.google.com "q-Painlevé" "translation" "period"`；
  `site:scholar.google.com "q-Painlevé I" "finite fields" period point order`；
  `site:scholar.google.com "q-Painlevé" nodal cuspidal fibres`；
  `site:scholar.google.com "q-Painlevé" autonomous return root unity`。
- Semantic：`site:semanticscholar.org "q-Painlevé" "singular" "finite fields"`；
  `site:semanticscholar.org "q-Painlevé" spectral divisor translation`；
  `site:semanticscholar.org "q-Painlevé" "finite fields" cycles`；
  `site:semanticscholar.org "q-Painlevé" autonomous conjugacy root unity`。
- 同族／标准工具：`"Tate normal form" "y" "b" "1-c" elliptic`、`"q-Painlevé" "Tate normal form"`、
  `"Painlevé I" "Tate" elliptic`、`"q-Painlevé" "Tate normal form" return`、
  `"Tsuda" "QRT" "translation" "point"`、`Tsuda Integrable mappings via rational elliptic surfaces translation point QRT 2004 pdf`、
  `"An algebraic geometric approach to integrable maps of the plane" "37"`、
  `"Constructing elliptic curves over finite fields with prescribed torsion" Sutherland pdf`。
- 奇异／根单位专门近邻：`"q-Painlevé" "root of unity" closed fibres singular elliptic`、
  `"Expansions on special solutions of the first q-Painlevé equation" pdf`、
  `"Mappings of Hirota-Kimura-Yahagi type can have periodic coefficients too" pdf`、
  `"Small complete caps from nodal cubics" arxiv`、`"D-bundles and integrable hierarchies" arxiv Ben Zvi Nevins`。
- 出版后更新核查：`"Arithmetic dynamics" "ae67bf" "translation"`、
  `"Arithmetic dynamics" "ae67bf" "conjugate"`、`"Arithmetic dynamics" "ae67bf" "order" "point"`。

### Consensus 实际执行

| Query | 实际返回与处理 |
|---|---|
| `"q-Painlevé I" spectral curve divisor translation point root of unity year:2024-2026` | 初次宽检索；未取得可以充作本题准确除子定理的结果。 |
| `"q-Painlevé" finite fields period elliptic point order singular nodal cuspidal year:2024-2026` | 近名 qPVI／四维扩展等；对四维条目 fetch，再读 arXiv 一手正文排除。 |
| `"An algebraic geometric approach to integrable maps of the plane"` | 返回 JRV06 与 JR；两者均 fetch，再以实际一手正文为依据。 |
| `"q-Painlevé I" "spectral" "divisor" "translation point" year:2024-2026` | 返回 `results: []`；仅为此精确式零结果。 |
| `"q-Painlevé I" nodal cuspidal fibres multiplicative additive group periodic orbits` | 返回四维扩展及其他近名项；无完整本题来源。 |
| `"q-Painlevé I" root of unity autonomous conjugacy return map finite fields period distribution year:2024-2026` | 只返回已 fetch 的四维扩展条目，不能视为 C4 覆盖。 |

fetch 记录 ID：JRV06 `df036e396ea85e9890179ef33b189e82`；JR `8f4a5a06b0515a3aa3fe51df766e7213`；
Stokes–Takenawa–Carstea `22f02da9f21d5753924fef572f7de586`。
Consensus 把 JR 年份记为 2025；其正式卷期年须用作者页／期刊 DOI 校正为 2026，不能照抄索引年充作出版年。
这里的 fetch 是书目／摘要读取，不是出版全文、引文图或跨模型独审。

## 5. 一手来源、实际读取和 nearest overlap

### S1. JR：同一原系统及时间 B，但不包含本次准确作用定理

[Nalini Joshi–Pieter Roffelsen, *Arithmetic dynamics of a discrete Painlevé equation*, arXiv:2508.18578v2](https://arxiv.org/html/2508.18578v2)。
实际读取摘要、§1、§2.3–2.4、§3.1 的时间矩阵／规范更新和式(3.4)–(3.7)、§3.2 与 §4。
原 B、$\bar M=BMB^{-1}$、积分／谱方程、坏值四次式和有限域频率样本都归 JR。
这些段落未给 $P_T-P_0$ 的谱格有向除子，也未给本题指定 torsor 作用上的准确回返点。
§3.2 仍以 Conjecture 3.6 陈述一般亏格与退化；§4 指出谱矩阵空间可能导向证明。
故 C1 的 delta 是具体作用的识别，不是再公布原 B 或谱曲线；C2–C4 不能由原频率样本自动获得。

[arXiv 元数据](https://arxiv.org/abs/2508.18578) 显示 v1 为 2025-08-26、v2 为 2026-01-16，本入口未显示 v3。
[正式出版 DOI](https://doi.org/10.1088/1751-8121/ae67bf) 的公开索引显示 *J. Phys. A* 59 (2026),195201，2026-05-13 出版；
本轮只读到索引中的摘要／部分正文／Remark 3.6，后者强调根单位时只能把 Lax 对作为形式方程处理。
Direct open 失败，**没有获得完整出版 §3.2／§4**，不能据片段保证其与 v2 完全相同，也不能排除未取得部分的增补。

### S2. JRV06：C2 的 d、N/d 是明确先例，不应再次包装

[D. Jogia–J. A. G. Roberts–F. Vivaldi, *An algebraic geometric approach to integrable maps of the plane*, J. Phys. A 39 (2006),1133–1149，作者托管原文](https://web.maths.unsw.edu.au/~jagr/JRV06.pdf)。
实际读取摘要／引言、§2 的特征限制、§4.2 式(36)–(37)及邻接推导、Corollary 1、频率讨论和 Table 3。
该文 §4.2 在式(37)前明确说明：每条光滑 $W(t)$ 上所有轨道共同周期为 $\operatorname{ord}\omega(t)$，
若 $n(t)$ 是轨道数，则 $n(t)\operatorname{ord}\omega(t)=\#W(t)$。
其一般共轭／点阶方法是最强直接扣除；本文全局假定特征不为 2、3，另讨论平面模型的约化和漏点风险。

准确定位：引言预告“§5 finite fields”，但出版 PDF 的实际标题为 **§4.2 The finite fields case**（p.1144 起），
关键共同周期／轨道数段在 p.1145，式号为 **(37)**。本件修正定位，不沿用旧索引“§5”说法。

### S3. Tsuda／QRT：指定点平移不是新方法

[Teruhisa Tsuda, *Integrable Mappings via Rational Elliptic Surfaces*, RIMS Kôkyûroku 1400 (2004),31–38（日文原文）](https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/1400-3.pdf)。
实际读摘要、§1、§2 的定理1及证明概略：QRT 明确转为 Weierstrass 曲线上加 $T=(0,0)$，给出系数表达。
设定是复数域 QRT／双二次 pencil，不是任意 r 的原 JR 时间 B 谱模，也不提供本题全部特征闭纤维桥。
[作者论文页](https://www.math.aoyama.ac.jp/users/tsuda/en/paper/) 和[作者摘要页](https://www.math.aoyama.ac.jp/users/tsuda/en/paper/abstruct.html)
核定英文论文 *J. Phys. A* 37 (2004),2721–2730；英文出版全文本轮未取得，不把日文证明概略冒称其完整证明。

### S4. 同 W 家族：Tate normal form 和有限域标记点阶已有

[Andrew V. Sutherland, *Constructing elliptic curves over finite fields with prescribed torsion*, arXiv:0811.0296v4](https://arxiv.org/pdf/0811.0296)。
实际读摘要、§1、§2 至式(6)及紧随的前三倍点；正式书目由[作者页](https://klein.mit.edu/~drew/)
核为 *Math. Comp.* 81 (2012),1131–1147，DOI [10.1090/S0025-5718-2011-02538-X](https://doi.org/10.1090/S0025-5718-2011-02538-X)。
其式(1)是 $E(b,a):Y^2+(1-a)uY-bY=u^3-bu^2$；§2 研究 $(0,0)$ 的倍点、负点及有限域点阶条件。

下面的同族比对是本件对公式的直接代换，不是声称 Sutherland 讨论 qPI：

$$
Y=\varepsilon v,\quad b=T,\quad a=1-\varepsilon c
\quad\Longrightarrow\quad
(W,P)\simeq(E(T,a),-(0,0))=(E(T,a),(0,T)).
$$

该代换不除以 2 或 3。$T$ 固定时仍是这个已知两参数族的一参数切片。
所以“同一 W family”确实有强先例；区别是**原 qPI 的哪个实际迭代对应这一标记点**，不是其点阶概念或裸曲线方程。

[Jinbi Jin, *Homogeneous division polynomials for Weierstrass elliptic curves*, arXiv:1303.4327v3](https://arxiv.org/pdf/1303.4327)，
实际读摘要／引言及 §3.3 Theorem 44 完整陈述与证明，另读 Corollaries 45–46。
Thm44 在任意 scheme、每个几何纤维满足 $2P,3P\ne0$ 的条件下给出 Tate normal form 的唯一性；
因此“全特征模型和标记点”也不能孤立地当新理论。
[元数据](https://arxiv.org/abs/1303.4327) 给初稿 2013、v3 修订 2015；当前 PDF 内部还印有 2021-10-31，
本件保留这个版本日期差别，不编造正式出版年份。

### S5. Beauville／IVY：循环谱模线性化的强方法先例

[Rei Inoue–Pol Vanhaecke–Takao Yamazaki, *Algebraic integrable systems related to spectral curves with automorphisms*, arXiv:1312.4208](https://arxiv.org/pdf/1312.4208)。
实际读摘要／引言、§2 Theorem 2.1 与 Remark 2.2、§4.2–4.4（Thm4.4 构造、Prop4.5、Thm4.6及证明）。
它把复数域素数阶循环谱矩阵固定分支放到商曲线 Jacobian，并证明拉回单射；
不是本题原秩二时间 B 的具体除子或每个有限域的完整周期分布。
正式卷期／DOI 由[期刊原页](https://www.sciencedirect.com/science/article/pii/S0393044014001429)
核为 *J. Geom. Phys.* 87 (2015),198–216，10.1016/j.geomphys.2014.07.008；arXiv 初稿 2013。

Beauville 的 [*Jacobiennes des courbes spectrales et systèmes hamiltoniens complètement intégrables*, Acta Math.164 (1990),211–235](https://doi.org/10.1007/BF02392754)
本次 DOI 仅返回 iframe，未获得原文 Thm1.4。
对标准谱对应的实质扣除依据是本轮实际读到的 IVY §4.3 对 Beauville 的明确重述及构造；
不能冒称本轮直接读完 Beauville 一手定理证明。

### S6. 根单位 Painlevé 与特定闭纤维：不能把“自治”偷换成 C4

[Adrian Stefan Carstea–Tomoyuki Takenawa, *A classification of two-dimensional integrable mappings and rational elliptic surfaces*, arXiv:1005.3586v2](https://arxiv.org/pdf/1005.3586v2)。
实际读摘要／引言、Remark2.3、§3 开头及 §3.1 对象说明，未通读全部案例证明。
§3 明确说原始 m 阶根单位时 $\phi^m(q)$ 自治并保持 index m 的 Halphen fibration；
§3.1 还研究另一映射的所有奇异纤维，其对象归入 qPVI 型。
这些是根单位回返／闭纤维机制的专门先例；上述已读段落未给本题 $R_{s,t}\sim F_{1,t^r}$ 的原状态置换等价。

[Yousuke Ohyama, *Expansions on special solutions of the first q-Painlevé equation around the infinity*，作者预印本入口](https://api.newton.ac.uk/website/v0/events/preprints/NI09061)
本轮实际可读摘要／引言索引，明确讨论复数域根单位下特殊形式解为代数函数；后续 PDF 正文读取超时。
其 [DOI](https://doi.org/10.3792/pjaa.86.91) 本轮 safe-open 失败，故不假称读到出版全文。
JR v2 §3.2 已实际给出并引用该文的 $s=1,-1$ 特殊代数解；那是坏纤维奇点轨道的专门先例，
不是该坏纤维全部光滑点参数／循环的分类。Ohyama 作者页面出现卷号 89，而 DOI 与 JR 引文为 86；本件采用后者，保留核验限制。
GRT11 的 HKY 周期系数论文只定位到题名／引文，未取得全文，因此不对其具体公式作排除性断言。

### S7. 节点／尖点群结构：明确当作标准扣除

[David Ben-Zvi–Thomas Nevins, *D-bundles and integrable hierarchies*, JEMS 13 (2011),1505–1567，期刊原文](https://ems.press/content/serial-article-files/31805)，
DOI 10.4171/JEMS/287；实际读摘要及 §2.1.1–2.1.2（p.1515）的三类三次曲线／光滑点 Jacobian 说明。
其中节点为 $\mathbb C^\times$、尖点为 $\mathbb C$，并描述正规化及群作用延到曲线。
这是一般机制扣除，**不能把其复数域设定冒充本题全特征定理**。

[Nurdagül Anbar–Daniele Bartoli–Massimo Giulietti–Irene Platoni, *Small complete caps from nodal cubics*, 2013 预印本](https://arxiv.org/abs/1305.3019)，
实际读摘要及[原文 §4 开头](https://arxiv.org/pdf/1305.3019)的节点参数和有限域乘法群同构。
该文服务于有限几何的 arcs／caps，不是 Painlevé 时间映射；只说明显式乘法参数本身早已是标准工具。

有限群后果也须扣除：一旦确认分裂节点／非分裂节点／尖点的光滑群分别是
$\mathbb F_q^\times$／范数一群／$(\mathbb F_q,+)$，其阶为 $q-1$／$q+1$／$q$；
加固定元素的每条循环都等长于该元素的阶。非零加法元素的阶是特征 $p$，**不是 $q$**，循环数为 $q/p$。
上述是群论后果，不是本件查到了一篇全特征 qPI 公式定理；非分裂与小特征的实际模型识别仍应由 C3 自己证明。

### S8. 2024–2026 最近邻与不同对象排除

| 一手来源 | 实际读取／时间核验 | 排除边界 |
|---|---|---|
| [Joshi–Lasic Latimer–Roffelsen, *On difference-differential Lax pairs and integrals of Painlevé equations in finite characteristic*, 2607.06980v1](https://arxiv.org/html/2607.06980v1) | 摘要、§1（含旧 qPI 仍为猜想的段落）、§2 Prop2.1及证明；arXiv 明列 2026-07-08 | 推广到连续 Painlevé 的差分—微分 Lax 积分，非 C1–C4 原 qPI 回返点／有限域置换。 |
| [Sato–Takemura–Yamashita, *Reducibility of symmetry on q-Painlevé equations*, 2609.02927v1](https://arxiv.org/html/2609.02927v1) | 摘要、完整 §1、目录；[arXiv history](https://arxiv.org/abs/2609.02927) 明列提交 2026-08-26（保留其 2609 编号） | 研究 $D_5,E_6,E_7,E_8$ 的 Weyl 表示等价及 Lax 时间匹配，非本题 A7 原矩阵／闭纤维 Jacobian 平移；未通读后续全证明。 |
| [Stokes–Takenawa–Carstea, *On the geometry of a 4-dimensional extension of a q-Painlevé I equation with symmetry type A1(1)*, 2506.21092v1](https://arxiv.org/html/2506.21092v1) | 摘要、§1 至 Remark1.1及对象解释；arXiv 2025-06-26 | 四维扩展、28中心、复数域伪自同构；不是本题二维原完整 states。不能仅因题名 qPI 就视为直接覆盖。 |

另实际读 [Roffelsen 作者写作列表](https://proffelsen.github.io/writing) 的 2026 预印本及原文 publication 条目。
未把其他 qPVI tau／monodromy 题名冒充 qPI 周期定理。不同系统或尚未读到的其他正文不作全球排除。

## 6. 逐 claim 的 exact delta 与未闭风险

| Claim | 最近重合／必须扣除 | 本次未定位直接先例的精确差额 | 不确定性／禁止越界 |
|---|---|---|---|
| C1 | JR 原 B／M；Beauville–IVY 谱模；Tsuda 指定点平移；Tate 标记族 | 原时间 B 在既定谱模方向上的 $P_T-P_0$、原域 torsor 回返准确加 $-(0,0)$，全 r／全特征／每 t，泛非挠 | 未定位不代表新；标准谱修改技术重合强。必须与输入作用约定一起比较，不能只比较最终坐标。 |
| C2 | JRV06 已有 d、N/d；Sutherland 已有同 Tate 族的有限域点阶 | 同一原 qPI 的准确 P 在每条光滑闭纤维延拓，包含全部原状态并带准确时间因子 r | 尚在证明；不是新的有限群周期理论，也不是已求出所有 q,c 的点阶闭公式。 |
| C3 | 一般节点／尖点群；已知显式参数；JR／Ohyama 坏纤维奇点特殊解 | 本 W 每条坏纤维的准确标记元素、全特征分裂类型与真实原 qPI 全状态共轭 | 纯 W 算式与原动力桥分开；尚未收到拟写显式式子，无法宣称逐式查重完成。 |
| C4 | CT 根单位迭代自治；Tate 族符号规范化；普通有限置换循环悬挂 | 精确 $R_{s,t}\sim F_{1,t^r}$ 的全部有限域状态置换、逐闭纤维含奇异点，从而固定时间轨道的循环频率对应 | 尚在证明；“自治回返”不等于“同族自治参数 T 共轭”；不得加强成曲面共轭／泛 torsor 平凡。 |

这四项是同一原 qPI 问题的相关比较维度，不拆成四篇成果，也不按模块数增加贡献。
C4 若得到证明，所报告的是一条具体系统内对应；其普通循环悬挂部分仍须扣除，不能靠术语包装成为一般新机制。

## 7. 交接与本次未完成的来源义务

- 本件完成规定的作者侧 A/B 实检范围；没有 Phase C／评分／正式建议／四门结论。
- JR 出版正文未完整取得，Google Scholar／Semantic 引文图未完整可达；不能宣布出版后所有前向引用已查尽。
- Beauville 原文证明未获取；目前方法扣除依 IVY 原文的明确转述，不隐去阅读层级。
- Ohyama 正文／GRT11 全文仍是有限缺口，不能写成“已读全文且排除”。已读原 JR 小阶例子保留为直接重合。
- 2026 年 8 月 Sato 等近邻已实际核对不同对象；不能把检到一篇新文或未检出另一篇当全球新意证书。
- 最终数学状态以各 claim 自己的新证明及后续独立核查为准。本件不改 C2–C4 的待证明状态，不消费其他代理意见。
- 保存后以全文回读、行数及 SHA256 核对本件交付；哈希在交接消息报告，不在文件内制造自指哈希。

本件为截至 2026-09-08 的有界公开来源快照，整体结论维持 `UNCERTAIN`。
