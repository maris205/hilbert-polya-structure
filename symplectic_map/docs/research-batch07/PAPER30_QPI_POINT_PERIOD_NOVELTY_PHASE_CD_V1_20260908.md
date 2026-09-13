# Paper30 qPI：准确回返点、全闭纤维周期与同族自治普适性的独立 Phase C/D 新意报告 V1

公开来源快照／截止：2026-09-08（UTC）；交付环境日期：2026-09-09。
版本名及检索窗口保持本轮冻结的20260908，不声称覆盖9日新增文献。
角色：新上下文的非作者新意复核者；只做 `novelty-check` 的 Phase C/D。
本件不是数学独审、正式四门票、Route A/B 评价、论文资格或发表保证。

## 1. 结论先行

**整体新意分数：6.5/10。建议：`PROCEED_WITH_CAUTION`。全球先例状态：`UNCERTAIN`。**

方法本身主要不新：谱模线性化、指定点平移、Tate 标准形、最小正则模型唯一性、
节点／尖点的乘法／加法群、有限群陪集循环，以及周期时间的循环悬挂，均有强先例或属于标准工具。
特别是“周期为点阶、循环数为 $N/d$”及“这条带标记点的 Tate 曲线族”已有明确先例，不能重包装。

但合取后的 finding 不应被这些扣除抹掉：在作者新主张的精确范围内，
原 JR 根单位 qPI 的完整回返，在所有有限域、所有有限闭纤维和全部合法状态上，
都对应同一个已知标记族上的同一点；因此整个回返置换只依赖 $q$ 和 $T=t^r$，
与**同一原族**的自治映射 $F_{1,T}$ 置换共轭。
本轮已读一手段落中没有找到直接给出这一整套量词和原动力身份的定理。

这是一个有实质内容的、系统特定的精确约化 finding，不是一般新方法。
它超过“给周期系数系统取一次回返”的普通事实，但其最后的共轭拼合和悬挂是标准后果；
剩余新意集中于准确标记动力的识别和无遗漏的闭纤维实现，不能按证明模块数重复计分。

分数只评价这组新主张相对实际可核先例的差额，不是证明正确概率。
新闭纤维稿和纯 $W$ 奇异稿均已写完、尚待另一数学独审；本件没有预授数学 PASS。
若后续数学核查改变了主张的量词或对象，须对改变后的实际 finding 重估，不沿用本分数。

## 2. 独立性、模型与隔离输入

先全文读取 `/root/autodl-tmp/.codex/skills/skills-codex/novelty-check/SKILL.md`。
技能指定的 `gpt-5.4` 本轮不可用；实际执行者为委派配置的 **Codex，xhigh**。
这是同模型家族的新上下文非作者复核替代，**不是实际的跨模型核验**，没有人类认证或校准含义。
本代理没有再委派、没有读取其他评审者意见，也没有尝试迎合其他关卡的分数。

除技能文件外，本轮只全文读取以下四份本地研究输入；没有沿它们的本地链接扩读。
SHA256 和行数均由本轮直接核对，与委派输入一致。

| 本地输入，均在 `docs/research-batch07/` | 行数 | SHA256 |
|---|---:|---|
| `PAPER30_QPI_POINT_PERIOD_PRIOR_ART_SEARCH_V1_20260908.md`，下称 AB | 321 | `75a1324e1fbefba2251f412435b4a76c180d9525dddb4b4f341c9c8344e1ccba` |
| `PAPER30_QPI_EXPLICIT_RETURN_POINT_ENTRY_V1_20260908.md`，下称 V | 277 | `2ca0b56081c76be343c0b8d86c6a5463533802d4aee8baed7068d992d830a0e7` |
| `PAPER30_QPI_CLOSED_FIBRE_RETURN_CONJUGACY_ENTRY_V1_20260908.md`，下称 L | 372 | `734b3f218bc3f16c8565ebb688d82c66252367d28e3e6a0e38f3aa571094c72a` |
| `PAPER30_QPI_SINGULAR_CUBIC_GROUP_ENTRY_V1_20260908.md`，下称 S | 683 | `64cb688c586c8a82123c998dd23275539935fd3baed9c9e0f38d98c814f2dce7` |

未读取 README、BATCH、其他本地作者输入、旧／新正式票、数学审查／处置、其他 Phase C/D 报告。
V 的已独立接受状态仅按本轮明确交接消费，没有读取其审查报告。
L、S 是完整新作者证明，状态为待数学独审；AB 中“正在证明”的文字是更早冻结快照，保持不改。
本件没有修改上述输入、锁或其他文件；唯一新增文件为本报告。

## 3. Proposed Method 与精确 claim 映射

原映射是

$$
F_t(x,y)=\left(\frac{st}{sx-y},\frac{sx}{y}\right),\qquad
t\mapsto st,\quad \operatorname{ord}(s)=r,\quad T=t^r\ne0,\quad
\varepsilon=(-1)^{r+1}.
$$

主张以原时间矩阵的有向谱格除子固定回返作用，再通过保持原剩余域的局部最小模型，
把指定作用延到整个有限闭纤维；奇异处写出准确群元素，有限域上再逐纤维与原自治系统拼合。
状态集是完整 $U_{t,s}(\mathbb F_q)$，包括合法例外线点，不是仅环面上的有理式定义域。
有限闭纤维不包含无穷远多重边界。

**本报告 C1–C4 一律沿用 AB 编号，不能与 L 的 C1–C4 混用。**

| 本报告／AB 编号 | 本次比较的主张 | 新作者件对应位置 |
|---|---|---|
| C1 | 原 $B$ 的准确有向除子 $P_T-P_0$，指定原域 torsor 上完整回返准确加 $P=(0,\varepsilon T)=-(0,0)$，泛非挠 | V 的 Claim 1–3、Steps 1–5；不是 L-C1 |
| C2 | 每条有限域光滑闭纤维上同一准确作用；周期 $d=\operatorname{ord}P$、循环数 $N/d$、原一步时间周期 $rd$ | L-C1、L-C2 及式(20)，时间因子来自 L-C4 |
| C3 | 全部奇异 $W$ 的准确参数、标记群元素、整条曲线平移及周期，并与真实原闭纤维动力识别 | S-Claim 1–5 为纯 $W$；真实动力桥来自 L-C1、L-C2、Steps 2–3；两件合用才是本 C3 |
| C4 | $R_{s,t}\sim F_{1,t^r}$ 的全状态置换共轭，原一步为 $r$ 层悬挂，全部非零时间按 $T\in(\mathbb F_q^*)^r$ 求和 | L-C3、L-C4、Steps 5–6；不是 L-C4 单独一项 |

L-C1 在任意原域要求实际纤维有光滑有理点；L-C2 仅在有限域证明此条件自动满足。
C4 不主张随 $c$ 有理变化的统一坐标、不主张全曲面双有理共轭，也不主张泛 torsor 平凡。
这一限制降低普适性的层级，但不是查新时可以忽略的措辞差别。

## 4. Core Claims：逐项新意判断

标签定义：LOW 表示主表达式／机制已有直接先例或属例行专门化；MEDIUM 表示仍有可辨认的、
系统特定的精确 finding，但依赖强标准方法且不宜声称广泛机制创新；HIGH 应保留给更强且证据更足的差额。
标签不是对“全球未出现”的置信区间。

| 核心 claim | Novelty | Closest | 准确剩余差额与扣除 |
|---|---|---|---|
| C1：准确泛回返点 | **MEDIUM** | JR；Beauville–IVY；Tsuda；Sutherland／Jin | 剩余是原 $B$ 在固定谱模方向上的除子，以及全允许 $r$、全特征、每个 $t\ne0$ 的指定 torsor 作用。谱模法、指定点表示、同 Tate 族和负点坐标都须扣除。 |
| C2：全光滑闭纤维周期 | **LOW** | JRV06 §4.2；Sutherland §2 | $d,N/d$ 是已明说的结果；本题新增的是把该已知定理所需的准确作用，在全部真实闭纤维和状态上实现，而不是新周期理论。这个实现是 C4 的关键支撑，但不能再把循环商公式算一次创新。 |
| C3：全奇异参数及真实动力 | **MEDIUM** | 同 Tate 族；Jin；节点／尖点群律文献；JR／Ohyama 特殊解 | 纯 $W$ 正规化、群识别、$N/d+1$ 大部分是标准计算；有限的剩余是准确标记元素、全部特征／参数的无遗漏表及原闭纤维共轭的合取。单独截取 S 作为“新群理论”应判 LOW。 |
| C4：同族自治普适性 | **MEDIUM（本组最强）** | CT 的根单位自治；JR 的原系统；JRV 的标记平移比较 | 未检出直接覆盖 $R_{s,t}\sim F_{1,t^r}$ 全有限域合法状态的先例。新 finding 是参数依赖准确降为 $q,T$；不是自治本身，亦不是循环悬挂本身。它仍是特定系统内由准确标记模型导出的约化，而非新的一般共轭方法。 |

### 4.1 C1：什么确实值得比较

识别 $r(P_T-P_0)=\pi^*(p_T-p_0)$ 后，原 $r$ 步回返对应的是一个固定标记点，
不是再加 $rP$ 或未知同源像；这比“是某个平移”精确得多。
全特征及不预设泛 torsor 有点，也有实质对象边界。
但局部谱修改及把线丛张量变成 Jacobian 平移的方式不新；符号正确本身不能充作强独立 finding。
尤其 $P$ 与 $-P$ 同阶，并由取负同构联系；不能用一个坐标符号差异制造周期新意。

### 4.2 C2：明确扣掉强先例，而不抹掉实际实现

本轮直接读到 JRV06 §4.2 p.1145 式(37)前的共同周期和轨道数段，
它已经给出轨道由固定点平移产生、所有轨道周期等于点阶，以及 $n\,d=\#W$。
这不是只给 Hasse 上界的弱先例；该文全局排除特征 2、3。
其 Props.2–3 也已经通过平移点比较映射的幂关系与共轭。[JRV06 原文](https://web.maths.unsw.edu.au/~jagr/JRV06.pdf)

因此本题不能宣称首次发现有限域椭圆周期等长或 $N/d$ 公式。
另一方面，把“原 qPI 的每一个合法闭纤维状态”确实送到同一已知模型，并跨过奇异特化与原域障碍，
不是引用这一群论公式就自动完成的工作；它应写为主 finding 的实现定理，避免另起“新周期原理”。

### 4.3 C3：新写出的公式也须逐层扣除

本次新增的实际比较对象包括

$$
z=b/a,\quad a=T-z^2,\quad a^2=\varepsilon Tz,\quad c=T/z-3z,
\quad h(m)=m^2+cm+3z^2-2T,\quad r_P=2z-T/z;
$$

$$
\chi(P)=\frac{z-\beta}{z-\alpha},\qquad
\eta(P)=\frac1{\alpha-z},\qquad
\phi_P(m)=\frac{r_Pm-(3z^2-2T)}{m-z}.
$$

在 $p\ne2,3$，S 还主张唯一尖点参数
$T=-27/256,c=9\varepsilon/8$，其加法元素是 $-8\varepsilon/3$；在 $p=2,3$ 无尖点。
这些确切表达式此前未进入 AB 的逐式比较，本轮已用原符号、标准族符号和几何同义词补检，见 §7。
未检到直接逐式覆盖，不等于公式首创；改变量名、交换切根或换原点都会改变文字指纹。

S 的 $d\ge4$ 尤其不可独立加分。Sutherland §2 已在同 Tate 标记族的光滑层写出前三倍点，
并明确标记点阶大于 3。本题把这个后果核到奇异光滑群是必要验证，
但仍是同一低阶倍点计算，不是新挠点界。
S 的局部环延拓防止把正规化置换误当原曲线态射；证明必要性不能直接转换成方法新意。

节点 $q\mp1$、尖点 $q$ 和非零加法周期 $p$ 都是相应有限群的标准后果。
全曲线多出的一个奇点固定循环，也不新；本题的剩余在于它确为**实际原回返**的那一个状态，
并与整条光滑层的准确群元素相配，而非人为补规则。

### 4.4 C4：为什么合取仍揭示一个 finding

以下推论是本轮对作者主张及先例的比较，不是声称先例原文已经给出本题结论：

1. 谱方程系数只出现 $T$ 与奇偶符号，尚不足以决定原动力的平移点；同一曲线上不同点可有不同阶。
2. 周期系数回返是自治，只说明时间参数复原；它可能是另一个高次映射，不必是同一原族的 $s=1$ 成员。
3. 准确点独立于剩余 $r$，加上每条闭纤维的原域等变实现，才使符号规范化后两边成为同一标记动力。

所以 $R_{s,t}$ 的完整循环类型仅由 $q,T$ 决定是可辨认的结果；
它把表面不同的根单位阶情形统一成同一原自治族，且奇异点和例外线状态不再是额外补丁。
这里不能因为末步是拼合曲线同构，就把整个 finding 判成“只取回返”的同义改写。

同时要明确：一旦两边都被识别为同一带标记模型，C4 的构造已相当直接；
有限置换中相同循环类型与集合共轭的关系、$d\mapsto rd$、循环数不变及按时间轨道求和皆为标准。
没有新的 $a_{T,q}(n)$ 闭公式、点阶算法复杂度结果或跨素数极限分布。
因此整体不应因加入“普适性”一词自动升成高新意的一般理论。

## 5. Closest Prior Work 与全部 AB 来源层级

层级：D＝本轮直接读取一手相关正文；A＝本轮只读一手摘要／元数据；
I＝本轮仅消费 AB 的实际阅读记录；F＝本轮正文访问失败。
“D”不意味着通读该文全文，也不自动表示所引结果已数学审查。
下表纳入 AB 中全部实质来源；本轮扩读范围准确列出，未取得正文者不作排除性保证。

| Paper／来源 | 年份／Venue | 本轮读取层级及准确定位 | Overlap／Key difference |
|---|---|---|---|
| [Joshi–Roffelsen，Arithmetic dynamics of a discrete Painlevé equation](https://arxiv.org/html/2508.18578v2) | arXiv 2025，v2 2026；J. Phys. A 59 (2026),195201 的书目沿 AB | D：HTML 摘要、§1相关段、§3.1 原 B/式3.4–3.7、§3.2、§4；另核 PDF v2 的 Conj.1.2、Remark1.3、§3.2及结论相关段 | 同一问题、原映射、Lax/谱方程、原数值周期和坏值均属 JR；已读正文未给 C1 准确除子及 C4 全状态同族自治定理。 |
| [JR arXiv metadata](https://arxiv.org/abs/2508.18578)；[出版 DOI](https://doi.org/10.1088/1751-8121/ae67bf) | v1 2025-08-26，v2 2026-01-16；出版时间细节沿 AB | A/F：本轮 metadata 未显示 v3，出版 DOI direct open 仍 Internal Error；搜索可见摘要片段 | 不能保证出版未取得部分与 v2 一样。metadata 摘要使用“已给亏格界”的语气，但 HTML/PDF v2 正文仍列 Conj.3.6；本轮保留这项层级差异，不据摘要升级或据旧正文排除出版增补。 |
| [Jogia–Roberts–Vivaldi，An algebraic geometric approach to integrable maps of the plane](https://web.maths.unsw.edu.au/~jagr/JRV06.pdf) | 2006，J. Phys. A 39,1133–1149 | D：摘要／引言、§2 特征限制、Thm3、Props.2–3、§4.2 p.1145式37前及邻段 | C2 周期与循环数是最强直接先例；映射比较也已有。没有本题全阶实际 B、全特征闭纤维身份。 |
| [Tsuda，Integrable Mappings via Rational Elliptic Surfaces，日文 RIMS 原文](https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/1400-3.pdf) | 2004，RIMS Kôkyûroku 1400,31–38；英文 J. Phys. A 37 的书目沿 AB | D：摘要、§1、§2 Thm1及证明概略的指定点构造段；没有取得英文出版全文 | QRT 指定为加 $(0,0)$ 已有；本题原时间 B／原域 torsor 和任意 $r$ 仍不同。 |
| [Sutherland，Constructing elliptic curves over finite fields with prescribed torsion](https://arxiv.org/pdf/0811.0296) | 2012，Math. Comp.81,1131–1147；v4 2012-03-27 | D：摘要、§1式1、§2式3–6及前三倍点 | 同 Tate 标记族、有限域点阶和阶大于3均已有；没有识别本题原迭代。 |
| [Jin，Homogeneous division polynomials for Weierstrass elliptic curves](https://arxiv.org/pdf/1303.4327) | 初稿2013，v3 2015；PDF内部日期2021保留 | D：摘要／引言、Cor12及证明、§3.3 Thm44陈述及证明前部；后部未通读 | 任意 Weierstrass 光滑点的群概形、任意 scheme 的 Tate 标记规范化是强方法扣除。不能把 Thm44 对椭圆曲线的假设删掉，冒称其已经证明本题整条奇异曲线共轭。 |
| [Beauville，Jacobiennes des courbes spectrales…](https://doi.org/10.1007/BF02392754) | 1990，Acta Math.164,211–235 | F/I：本轮 DOI 只到 ProjectEuclid 空正文入口；未读其 Thm1.4原证明 | 谱对应归属须保留；实质扣除由本轮读到的 IVY §4.3明确重述支撑，不假称通读 Beauville。 |
| [Inoue–Vanhaecke–Yamazaki，Algebraic integrable systems related to spectral curves with automorphisms](https://arxiv.org/pdf/1312.4208) | arXiv2013，J. Geom. Phys.87 (2015),198–216 | D：引言可读片段、§4.3 Thm4.4及构造、§4.4素数阶设定、Thm4.6及证明；AB更广阅读不转为本轮通读 | 循环谱固定分支／商曲线 Jacobian 已有；复数域素数阶背景不等于本题所有允许 $r$ 与原 B 的准确作用。 |
| [Carstea–Takenawa，A classification of two-dimensional integrable mappings and rational elliptic surfaces](https://arxiv.org/pdf/1005.3586v2) | arXiv2010；J. Phys. A45 (2012),155206 | D：Remark2.3、§3开头、§3.1对象说明；未通读案例证明 | 根单位 $m$ 次回返自治并保 Halphen fibration 已有；§3.1对象是另一 qPVI 型映射，不直接覆盖 C4。 |
| [Ohyama，Expansions on special solutions of the first q-Painlevé equation around the infinity](https://doi.org/10.3792/pjaa.86.91) | 2010，Proc. Japan Acad. Ser.A 86，按 DOI/JR及AB | F/I：本轮 DOI、Newton作者预印本入口均 Internal Error；AB摘要／引言索引与本轮JR小阶例子 | $s=1,-1$ 特殊代数解及坏纤维奇点轨道有专门先例；未取全文，不能排除更广的准确公式。 |
| [Grammaticos–Ramani–Tamizhmani，Mappings of Hirota-Kimura-Yahagi type can have periodic coefficients too](https://doi.org/10.1088/1751-8113/44/1/015206) | 2011，J. Phys. A44,015206 | F/I：本轮公开题名／书目和摘要检索片段；DOI direct open失败，未取得一手全文 | 周期系数 HKY 是相关背景，不能把未读全文自动排除为无关；也不能仅据题名判它已有 C4。 |
| [Ben-Zvi–Nevins，D-bundles and integrable hierarchies](https://ems.press/content/serial-article-files/31805) | 2011，JEMS13,1505–1567 | F/I：AB实际读§2.1.1–2.1.2；本轮 content入口失败，另一个EMS入口也未取得正文 | 复数域节点／尖点群及作用延伸是标准扣除；不把AB读取或复数域结论冒称本轮全特征核验。 |
| [Anbar–Bartoli–Platoni–Giulietti，Small complete caps from nodal cubics](https://arxiv.org/pdf/1305.3019) | 2013预印本 | D：摘要、§2奇数域设定、§4开头节点规范式及乘法参数；未通读caps证明 | 显式有限域乘法正规化是直接先例；所读模型不负责本题非分裂／小特征和原回返识别。 |
| [Joshi–Lasic Latimer–Roffelsen，On difference-differential Lax pairs and integrals of Painlevé equations in finite characteristic](https://arxiv.org/html/2607.06980v1) | 2026-07-08预印本 | D：摘要、§1至列出统一Lax设定的相关段，非全文 | 是有限特征连续 Painlevé 的积分构造；已读主张不覆盖本题 C1–C4。 |
| [Sato–Takemura–Yamashita，Reducibility of symmetry on q-Painlevé equations](https://arxiv.org/html/2609.02927v1) | 页面日期2026-08-26，保留2609编号 | D：摘要、完整§1、目录；后续未通读 | Weyl表示等价／时间匹配，列明 $D_5,E_6,E_7,E_8$ 对象；不是本题全状态置换定理。 |
| [Stokes–Takenawa–Carstea，On the geometry of a 4-dimensional extension of a q-Painlevé I equation…](https://arxiv.org/html/2506.21092v1) | 2025-06-26预印本 | D：摘要、§1开头至4D映射及问题背景；未读完整后文 | 4D扩展、28吹起中心，非本题二维原状态；只能作相邻几何方法扣除。 |

AB 中 Tsuda 作者论文／摘要页、Sutherland 作者页、IVY 期刊页、Roffelsen 写作列表等，
本轮仅作为 AB 已记录的书目来源 I 纳入，没有重新打开，也没有假称本轮亲核其所有条目。
Google Scholar、Semantic Scholar 和 Consensus 入口的实际成败与覆盖边界沿 AB；
本轮没有重做其检索、fetch或引文图，不能把 AB 的全部检索算作本轮新独立命中。

### 5.1 同 Tate family 的显式扣除

设 $a_{\rm Tate}=1-\varepsilon c$、$b_{\rm Tate}=T$、$Y=\varepsilon v$。
本轮直接代入比较得

$$
(W,P)\simeq
\bigl(Y^2+(1-a_{\rm Tate})uY-b_{\rm Tate}Y=u^3-b_{\rm Tate}u^2,
(0,T)\bigr).
$$

这正是 Sutherland 式(1)的同一两参数族，标记点为其 $(0,0)$ 的负点；
同族不是“看起来类似”。代换不除以2或3；固定 $T$ 也只是既有族的一参数切片。
新尖点参数换为标准族参数就是 $(b_{\rm Tate},a_{\rm Tate})=(-27/256,-1/8)$。
以上为本报告对两套方程的直接比对，不归称 Sutherland 研究了原 qPI。[Sutherland §1–2](https://arxiv.org/pdf/0811.0296)

### 5.2 本轮新增近邻，及其实际排除层级

| 来源 | 本轮实际读取 | 对 delta 的影响 |
|---|---|---|
| [Roberts–Jogia，Birational maps that send biquadratic curves to biquadratic curves](https://web.maths.unsw.edu.au/~jagr/RJ15.pdf)，J. Phys. A48 (2015),08FT02 | D：摘要、§1、§2开头的原域设定；未读全文定理证明 | 进一步扣除“用相同曲线不变量比较周期／非QRT映射”的一般想法；正文所读设定为实／复双二次族，不是全特征原 qPI 的 C4。 |
| [Bershtein–Gavrylenko–Marshakov，Cluster integrable systems, q-Painleve equations and their quantization](https://arxiv.org/abs/1711.02063)，JHEP02 (2018),077 | A：arXiv摘要、版本与出版元数据 | cluster去自治化是相关方法；摘要不足以全面排除其正文可能有的特殊参数关系，本轮未把它当直接覆盖或完成全文排除。 |
| [Shin，Coset-refined trace statistics, nodal characters, and affine branches in cubic norm tori](https://arxiv.org/html/2605.21939v1)，2026-05-21 | D：摘要、§1开头至主定理包起始 | 有限域节点／范数环面／轨道统计词语很近，但列明目标是三次范数环面上的迹条件与特征标和，且排除特征2、3；未见原qPI或准确标记平移主张。未通读后部，不能作逐式全局排除。 |
| [Desiraju–Roffelsen，A Tau function for q-Painlevé VI as a Fredholm determinant](https://arxiv.org/abs/2608.03345)，2026-08-04 | A：完整摘要及日期 | 解析qPVI/Riemann–Hilbert tau对象，不是二维qPI有限域闭纤维周期；仅按摘要对象分流，没有声称全文无任何关联。 |

未采用搜索返回的 ResearchGate、Moonlight、论坛、转载书站或聚合页作技术定理证据。
它们只作定位线索；例如新节点近邻最终用 arXiv 一手摘要／引言核对。
没有把爬取日期当发表日期，也没有把含“cusp”的模曲线条目自动等同于三次曲线的尖点。

## 6. Overall Novelty Assessment 与定位

- **Method novelty：LOW。** 本轮未识别出新的通用谱方法、群律、模型延拓原理或置换理论。
- **Finding novelty：MEDIUM，C4最强。** 清楚的剩余是原系统所有有限阶时间回返对同一原自治族的精确全状态约化，以及支撑它的准确点／完整闭纤维识别。
- **Score：6.5/10；Recommendation：`PROCEED_WITH_CAUTION`。** 不是各模块分数相加，也不设置为满足其他阈值。
- **为何不是 ABANDON：** 已读最强先例没有直接陈述上述同原族、同 $T$、全状态的合取 finding；把它降为普通“周期系数回返自治”会丢掉真正内容。
- **为何不判高分 PROCEED：** 裸模型、标记点族、周期统计公式和主要方法高度既有；剩余是具体系统的准确实现与自然统一，没有更一般机制、算法提升或新的点阶分布结论；强近邻及出版全文还有有界访问缺口。

推荐定位是“根单位 qPI 的准确回返与有限域自治约化”，把 C4 放在结果摘要中心，
C1 作为产生约化的准确标记动力身份，C2／C3 作为全状态无遗漏分类的支撑。
应在介绍周期公式之前主动引用 JRV，在写曲线方程之后立即说明 Tate 先例。
宜称“explicit realization / exact reduction”，不宜称“新椭圆族”“新的 $N/d$ 周期原理”或“新广义Jacobian机制”。

建议可用的窄贡献句（是对作者新主张的定位，不是数学验收）：

> 识别原根单位 qPI 的准确回返点，并在全部有限域有限闭纤维上实现其指定作用，
> 从而将完整回返置换约化到参数 $T=t^r$ 的同一原自治族；闭纤维共轭包含全部合法状态，奇异纤维的显式群元素进一步给出其准确周期。

### 主要审稿风险

1. 若主摘要只写 $d,N/d$ 或列出一个长 Weierstrass 方程，JRV06 和 Sutherland 足以造成强重合质疑。
2. 若 C4 未明确“原族 $F_{1,T}$”“全部合法状态”“有限域逐闭纤维”三个限定，CT/JR自治事实会使其看似旧结果改述。
3. 若把 S 中长计算当新方法，标准奇异三次理论和 Jin 的全特征光滑群结构会削弱论点；长度不等于创新。
4. 不能用新奇异公式的搜索零匹配证明全球首创，也不能忽略标记点变号、Tate参数更名及非分裂下降的等价写法。
5. 未取得的 JR 出版后文、Ohyama／GRT11全文以及更完整的前向引文图，是查新不确定性；不能用“旧”或“不同题名”代替核查。
6. 把有限点集共轭写成全曲面／泛域代数共轭，会把科学主张扩大到本轮输入未证明也未查新的层级。

## 7. 本轮额外 query 与访问记录

AB 的 Phase A/B 查询表保持原样，本轮没有声称重复执行其中全部查询。
本轮主要任务是独立核最强重合与比较新完成公式；最近半年窗口另实检为
2026-03-08 至 2026-09-08，搜索上界使用 `before:2026-09-09`。
年份／日期搜索语法不是数据库穷尽保证；同批多查询的返回不硬拆成各自的零结果。

| 目的 | 本轮实际提交字符串 | 处理与结论边界 |
|---|---|---|
| C3精确常数，原参数 | `"q-Painlevé" singular cubic "27/256"` | 返回含同数字的其他谱曲线／无关结果，未取得同W及原qPI的直接覆盖。 |
| C3尖点，标准族但原c | `"Tate normal form" cusp "9/8"` | 多为模曲线／挠点线索；未取得本题尖点公式定理。 |
| C3斜率表达式 | `"Painlevé" "2z" "T/z" singular` | 近名ODE／Lax片段，未核到本题公式。 |
| C3交比表达式 | `"nodal cubic" "m-alpha" "m-beta" translation` | 未定位可核直接对应；不据变量名检索推首创。 |
| C3几何同义检索 | `"Tate normal form" singular cusp parameter normalization` | 找到Tate／Jin类来源，按同族强扣除，不当作新发现。 |
| C3常数宽检索 | `"Tate" "27" "256" singular cubic` | 多为Tate算法／不相关常数；未形成直接公式先例。 |
| C3规范化后的尖点b | `"Tate normal form" "-27/256"` | 未定位可核同参数尖点主张。 |
| C3规范化后的尖点a | `"Tate normal form" "-1/8" singular` | 未取得本题准确标记元素；不能排除其他参数化。 |
| C3另一公式片段 | `"q-Painlevé" "3z" "singular"` | 未核到本题对应式。 |
| C3结构与有限域 | `"nodal cubic" translation cross ratio normalization finite field` | 标准正规化材料；出现2026范数环面近邻，转读一手源。 |
| C4精确对象 | `"q-Painlevé I" "conjugate" "autonomous" finite fields` | 未取得同原族全状态共轭直接先例。 |
| C4原参数依赖 | `"q-Painlevé" "t^r" "period" autonomous` | 原系统／一般自治背景；未取得精确置换类型约化。 |
| C4同义表述 | `"q-Painlevé I" "autonomous" "conjugacy"` | 未核到C4全量词先例。 |
| C4置换表述 | `"q-Painlevé" "autonomous" "permutation"` | 命中cluster等近邻，打开BGM一手摘要，未冒称全文排除。 |
| 最近半年有限域 | `"q-Painlevé" "finite fields" after:2026-03-08 before:2026-09-09` | JR出版索引等；没有取得新完整C1–C4定理。 |
| 最近半年arXiv | `site:arxiv.org "q-Painlevé" translation period after:2026-03-08 before:2026-09-09` | Sato及qPVI tau近邻，已按一手实际对象分流。 |
| JR精确点更新 | `"Arithmetic dynamics of a discrete Painlevé equation" "translation"` | 未获得出版全文的新准确点定理；另直接核PDFv2。 |
| GRT全文定位 | `"Mappings of Hirota-Kimura-Yahagi type can have periodic coefficients too" pdf` | 只得相关文献、引文／索引及RJ15线索；GRT全文未取得。 |
| GRT出版入口 | `"Mappings of Hirota-Kimura-Yahagi type can have periodic coefficients too" doi` | 核到出版DOI并实开失败；不绕访问限制。 |
| 新节点近邻 | `"Coset-refined trace statistics, nodal characters, and affine branches in cubic norm tori"` | 定位2605.21939，一手摘要／引言对象不同；后文未通读。 |

其中部分精确式为压缩显示结果而重复提交；一次组合返回过长时，未显示部分不作为已读证据。
公式补查覆盖十种表述，超过至少三种的要求，但仍不是符号等价式的穷尽搜索。

实际访问限制汇总：

- JR 出版 DOI、GRT DOI、Ohyama DOI和Newton预印本入口本轮均未取得正文，返回 Internal Error。
- Beauville DOI只给 ProjectEuclid入口，未取得定理正文；不以IVY重述冒充直接阅读全文。
- Ben-Zvi–Nevins 的EMS content入口及另一次EMS页面尝试未取得正文；本轮保留 AB 的既有阅读层级。
- JRV第13个PDF页面截图返回 Internal Error，但关键段已从同PDF文本完整取得；未因此伪称截图核验成功。
  Sutherland截图请求得到页面结果，本判断实际依赖可读原文式1及§2文本，不依赖未展示图像细节。
- Scholar／Semantic在AB的访问缺口没有在本轮被关闭；本轮没有调用Consensus或声称获得完整前向引文图。
- 没有下载PDF到本地、没有破解访问挑战、切身份、配置新服务、外部写信或发起付费资源。

## 8. 交付自查与边界

本件保存后全文回读，核对以下事项：

1. AB-C编号与L-C编号清楚映射；L与S均作为新完整作者稿待独审，不改AB历史快照。
2. 明确否认方法主链的新理论主张，同时实际评价C1–C4合取的特定finding。
3. 最强先例的 $N/d$、同Tate标记族和低阶点阶界已扣除，不以公式重写制造新意。
4. CT的自治事实与同原族 $T=t^r$ 全状态共轭没有偷换；不新增全局双有理／泛torsor主张。
5. 纯W算式与真实原动力桥分开，尖点周期为 $p$，群点数为 $q$，两者不混同。
6. 所有AB实质来源纳入比较，直接／继承／摘要／失败层级分开；新近邻及真实访问缺口均保留。
7. 分数与建议仅由本轮新意判断给出，没有正式价值、容量、证明信心或Route票。

交付行数与SHA256在交接消息给出，不在本文写自指哈希。
本次结论为有限公开来源下的谨慎新意判断；未检出完整先例仍为 `UNCERTAIN`，不是全球首创证书。
