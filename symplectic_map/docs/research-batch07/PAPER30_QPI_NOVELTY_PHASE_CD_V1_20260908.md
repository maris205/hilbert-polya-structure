# Paper30 qPI：独立 Phase C/D 有界新意核查 V1

日期／公开检索截止：2026-09-08（UTC）。
审查对象：同一 JR qPI 问题的四个精确数学候选，不拆成四篇，不按模块数加分。
结论：各完整 claim 的结果新意均为 `MEDIUM`；一般方法新意为 `LOW`；
总体有界新意 `6.0/10`，建议 `PROCEED_WITH_CAUTION`，全球首创仍为 `UNCERTAIN`。
这是查新建议，不是数学通过、科学价值、自然页数、完整四门或立项 PASS。

## 1. 独立性、技能实施与权限边界

本审查为未参与所列作者推导的全新本地 Codex 独立实例，按委派采用 xhigh 深度。
已全文读取 novelty-check 与 research-review 两个 SKILL.md，并执行有界 Phase C/D：
以既有 Phase A/B 来源包为输入，自行复读最强争议先例，独立比较方法与结果差额。
已检索当前可用工具元数据，未发现技能指定的 GPT-5.4 Codex MCP 调用接口；
没有配置服务、安装工具或调用虚构的 GPT-5.4。故本件是本地独立实例替代，
不是跨模型验证，不是人类同行评审，也没有可报告的外部 reviewer threadId。
没有虚构多轮外部对话或“双方共识”；本件记录一次独立判断与其证据。

没有打开 README、BATCH、旧内部候选正式评价、任何 NON_AUTHOR／REVIEW／DISPOSITION 文件、
新组合核查或另一代理报告。作者输入中自然出现的旧状态和审查链接不作为新意证据。
本轮四个 claim 均按明确数学候选比较；准确坏值作者稿仍须由主控另行处理数学接受，
本件既不预判其独审 PASS，也不以其他模块已获接受推导新意。
只新增本文件；所有公开访问只读，不修改冻结稿、锁、项目、其他报告或外部对象。

## 2. 被比较的准确对象

统一使用原映射、原完整初值空间与原积分，不改状态定义或基底坐标：

$$
F_t(x,y)=\left(\frac{st}{sx-y},\frac{sx}{y}\right),\qquad t\mapsto st,
\qquad c=I_r,
$$

$s$ 的精确有限阶为 $r$，$s,t\ne0$；正特征 $p$ 自动满足 $p\nmid r$。
几何候选覆盖每个固定非零 $t$、全部特征，含 $2,3$；算术候选覆盖全部有限域与原合法 states。
本件的 claim B 是几何模块（F 并入 N/G）；claim D 才是文件代号 B 的准确坏值桥，避免混淆。

| Claim | 原始候选的比较范围 | 明确不替换为 |
|---|---|---|
| A 全轨道 | 最小完整一步周期 $m$ 的 $\ell=m/r\le q+1+2\sqrt q$；进入 JR 原 ceil bins；含唯一奇点固定、正规化后 $q-1,q+1,p$ 分支 | 只取光滑层、只取环面点、自治 $s=1$ 或事后新阈值 |
| B 实际几何 | 原八中心的 $\operatorname{ord}\mathcal O_D(D)=r$；$1,I_r$ 生成最小完整 $\lvert rD\rvert$；泛光滑几何整亏格一；全部有限纤维几何整约化、坏纤维唯一奇点且正规化有理；实际 $Z(dI_r)$ 长度四 | 抽象存在某个 Halphen pencil、只证一般 $t$、谱判别式次数四 |
| C 泛 Jacobian | 实际 $X/k(c)$ 的 Jacobian 是原循环谱商 $E$；实际 $M$ 到 $x,y$ 有理逆、固定谱线丛差、循环拉回无核，保留 $K$-torsor 可能不平凡 | 同亏格、未排不可分次数的点集单射、未知次数同源、全局有理截面 |
| D 准确坏值／重数 | 在原 $c$ 上 $R_{r,t,s}(C)=\delta(C,t^r)$，保留实际非约化临界概形；有限局部模型比较与四维临界代数，含碰撞与小特征 | 仅四次公式、仅根集猜想、一般参数比较、无穷远重纤维结论 |

其中 A 的原分箱明确为

$$
N_\pm=q+1\pm2\sqrt q,\quad M_q=\left\lceil(\sqrt q+q^{-1/2}-2)/4\right\rceil,
\qquad B_j^{(q)}=\begin{cases}[N_-/j,N_+/j],&1\le j<M_q,\\ \left[1,N_+/M_q\right],&j=M_q.\end{cases}
$$

为固定 C、D 的身份，令 $T=t^r$、$\varepsilon=(-1)^{r+1}$。原谱商与 D 的模型为

$$
E:\lambda^2-(T+cZ+Z^2)\lambda+\varepsilon Z^3=0,
\qquad W:v^2+cuv-\varepsilon Tv=u^3-Tu^2.
$$

D 所比较的是原临界代数上乘 $I_r$ 的特征多项式，而非重命名谱式：

$$
R(C)=\det(C\operatorname{id}-m_{I_r})
=C^4-\varepsilon C^3-8TC^2+36\varepsilon TC+16T^2-27\varepsilon^2T.
$$

其原参数临界模型候选为

$$
k[z]/\big((T-z^2)^2-\varepsilon Tz\big),\qquad
c=\varepsilon-z-z^3/T.
$$

这些公式在本节用于确定本地候选，不作为本审查新推导或数学验收。

## 3. 实际读取的本地输入及身份

| 输入 | 本实例实际读取范围 | SHA256 |
|---|---|---|
| [前三项 Phase A/B 来源包](PAPER30_QPI_POST_BRIDGE_PRIOR_ART_SEARCH_V1_20260908.md) | 全文 268 行，含实际来源、查询与访问限制 | `4470af64294525bc4ae33b9b00fc38c44c38215290a36fa6f3a5b6bdf861f90e` |
| [准确坏值来源补充](PAPER30_QPI_EXACT_BAD_VALUES_PRIOR_ART_SUPPLEMENT_V1_20260908.md) | 全文 112 行 | `2aae448ca17022aa7b51990b84058e57ee455ab0e4c0a4127d8e0ec7fc39c898` |
| [A 全轨道作者稿](PAPER30_QPI_ALL_ORBIT_HASSE_BINS_ENTRY_V1_20260908.md) | 全文 298 行；只作新意／机制比较，不出证明票 | `78191a3faa7d2a867e45eccd708b106b722d43e6f5ea73d583e0385637be2469` |
| [F 实际有限纤维作者稿](PAPER30_QPI_ACTUAL_SINGULAR_FIBRE_ENTRY_V1_20260908.md) | 行 1–370：精确 Claim、整数格、有限纤维与临界计数机制 | `3b7a495b723d9ba45003fe767431c4420053c0b3de6656a2335c3aad01307003` |
| [J 泛 Jacobian 作者稿](PAPER30_QPI_LAX_JACOBIAN_BRIDGE_ENTRY_V1_20260908.md) | 行 1–135、230–446：Claim、策略、谱模／逆重建／固定差／无核／下降段 | `a6aa5e30ea0795b05790b058dfd4debc6431de1918090b9a6add88351a1eb63f` |
| [准确坏值作者稿](PAPER30_QPI_EXACT_BAD_VALUES_BRIDGE_ENTRY_V1_20260908.md) | 全文 488 行，含最后版本的模型术语、CM 与概形级消元 | `1e7ade432e62b1e116270d2588d0d798accbf482fcc6edd46dca12b76be42bb1` |
| [N 法丛作者稿](PAPER30_QPI_BOUNDARY_NORMAL_BUNDLE_ENTRY_V1_20260908.md) | 行 1–80、205–278：Claim、实际四图、四因子乘积及精确阶 | `8234b5584adba10ec02adb0269300b0c5191b5445fca345e28e1eb5171c12469` |
| [G 最小 pencil／一般亏格一作者稿](PAPER30_QPI_PRIMITIVE_GENUS_ONE_BRIDGE_V1_20260908.md) | 行 1–90、160–245：Claim、依赖、互素 SNC 排准椭圆及原始性机制 | `0d7a3e2d37eb7218feddfe5c85bf244a0be358bfcc880279d5f14afd5cb77ace` |

P、R 的契约在上述作者输入内用于理解依赖，本实例未另行打开其作者全文。
这不是完整数学重审，故不能把上述读取表解释为所有引用证明已经再次验证。

## 4. 最强先例：本实例复读后的实质扣除

| 最接近一手来源 | 年份／出处 | 本实例实际读取范围 | 必须扣除的 overlap；剩余对象边界 |
|---|---|---|---|
| [Joshi–Roffelsen 作者 v2](https://arxiv.org/html/2508.18578v2) | 2025 初稿，2026-01-16 v2；出版 J. Phys. A 59,195201 | 摘要／§1.1；§2.1–2.2 states；§3.1 单周期矩阵／积分相关段；§3.2 全节、§4 | 原系统、积分、分箱、谱式、四次条件与待解问题均已有；不是本件首次提出。原文未呈现当前准确桥的完整证明。 |
| [Jogia–Roberts–Vivaldi](https://web.maths.unsw.edu.au/~jagr/JRV06.pdf) | 2006，J. Phys. A 39,1133–1149 | PDF pp.1–4：引言及§2开头；pp.13–16：§5窗口、Corollary1及证明、后续讨论 | 已有相同光滑平移层窗口及重叠实数阈值；全篇排特征2、3，且讨论一般约化条件。原qPI完整states／奇异层的全量词覆盖不在所读结论中。 |
| [Cantat–Dolgachev](https://arxiv.org/pdf/1106.0930v2) | 2011 预印本；J. Reine Angew. Math. 2012 | PDF pp.6–9，Prop2.2全部陈述与证明、Remark2.3 | 任意特征法丛精确阶与Halphen index／最小pencil、唯一多重纤维已有；特征2、3明确保留准椭圆可能。 |
| [Carstea–Takenawa](https://arxiv.org/pdf/1005.3586v2) | 2012，J. Phys. A 45,155206 | 复曲面设定；Thm2.2全部陈述／证明、Remark2.3、§3开头根单位推论 | q-Painlevé参数为根单位、回返保持对应Halphen fibration已有；本题不是新发现“根单位导致椭圆化”。 |
| [Mizuno](https://arxiv.org/pdf/2008.11219v4) | 2024，Selecta Math.30,19；初稿2020 | Appendix A，Type $E_1^{(1)}$ Root data（PDF pp.25–26）；邻近另一 $E_1^{(1)\prime}$ 条目仅用于辨别 | 已明确给平方−8、交数8、和为八边界的同型秩二格。不是新的抽象格；此处未证明其toric标记与JR八中心逐项同一。 |
| [Inoue–Vanhaecke–Yamazaki（IVY）](https://arxiv.org/pdf/1312.4208) | 2013 预印本；2015，J. Geom. Phys.87,198–216 | §4.2–4.4全文，含Thm4.4构造、Prop4.5及推导、Thm4.6及证明；另读Appendix Thm7.1全部陈述／证明 | 循环谱约化、商曲线Jacobian开集、拉回单射已有；专门模型为复数域、矩阵秩等于循环素数阶。不是本题秩二任意r的直接实例定理。 |
| [Stacks 模型与唯一性](https://stacks.math.columbia.edu/tag/0C2R)、[§55.10](https://stacks.math.columbia.edu/tag/0C9Y) | 持续维护标准资料 | 任意DVR设定、Def55.8.4；Lemmas55.10.1–2全文及证明 | 局部双方最小正则模型、同泛曲线推出同基底同构是标准定理；不算D的新一般机制。 |
| [Stacks 光滑提升](https://stacks.math.columbia.edu/tag/07LW)、[Fitting ideals](https://stacks.math.columbia.edu/tag/07ZA) | 标准资料 | Lemma15.9.14全文／证明；Lemma15.8.4全部陈述／证明，特别(3) | étale局部截面提升和Fitting理想基变换均是旧工具。概形级保留并不是新提出一种临界理论。 |
| [Conrad, Minimal Models for Elliptic Curves](https://math.stanford.edu/~conrad/papers/minimalmodel.pdf) | 2015-11-21作者讲义 | §2任意DVR长方程定义；Cor2.9全部证明、随后判别式／微分变换及Cor2.10；未通读24页 | 长Weierstrass理论及十二次幂变换已有；D中的低赋值最小性判断是它的短应用。 |

### 4.1 A：同一阈值必须按“已有”处理

JRV 的 $N_-/n\le\mathrm{period}\le N_+/n$ 及
$n\ge\sqrt q/4+1/(4\sqrt q)-1/2$，经相同归一化就是本题原窗口结构。
因此“非自治情形重新出现Hasse窗口”不能作为新的普遍现象或方法；
返回固定时间切片本身也只是周期系统的标准处理。扣除依据为上表 JRV §5。

本地 A 真正保留的是原 JR 猜想在所有允许参数、所有合法状态上的证明候选，
尤其坏纤维唯一奇点不删除、非奇异点经正规化保持周期、$p$ 分支仍进入原bins。
这些分类与整数不等式自身初等；若实际几何与回返平移作为现成输入，
A 的消费者确实是短而标准的推论。故结果新意可为中等，方法不能为高。

### 4.2 B：已知格并非弱背景，全特征也不自动得分

CD／CT已经控制Halphen机制；Mizuno又提供本地F所算的抽象交格。
在该整数格已与实际模型对上后，伴随公式排有限可约分量、最小性排重数，
属于相当直接的几何推论。$12-8=4$ 的Chern计数也不构成新的计数理论。

仍需区别“抽象格已知”与“原 $I_r$ 在每个 $t$、每种特征满足所需几何契约”。
本地 N 的准确粘合乘子、G 的完整原pencil身份／互素SNC排准椭圆、F的实际有限概形
是所保留的对接增量；它们不是仅写一句“相同证明适用于小特征”。
但不能因为具体图多、检查细、包含2／3便认定高新意。
本件将 B 放在 `MEDIUM` 下沿；其中单独的法丛阶—index原则、抽象格及长度四是 `LOW`。

### 4.3 C：扣除 Beauville 与 IVY 后，剩下实际矩阵识别

IVY的§4.3确切重述并构造Beauville对应，§4.4再得到商曲线Jacobian及拉回单射。
本件不把“取循环不变Picard单位分支”或“分歧排核”重新记作原创。
其Appendix Thm7.1还单列复数域素数次Galois覆盖的拉回核／étale关系。

本地 C 的可辨别增量在实际 $M_{2r},M_{2r-1},M_0$ 的系数恢复原 $x,y$，
把几何点单射升级为有理逆；以及实际intertwiner给出的固定谱差、原 $k(c)$ 上的torsor下降。
秩二与任意r不是IVY的“矩阵秩=循环素数阶”参数替换；不过从素数阶推广到任意tame阶，
在本题有全群固定点时并不是一种新的拉回核理论。
因此 C 有中等的准确模型识别增量，不能定位为新的一般谱约化方法。

### 4.4 D：准确重数是更强 finding，但不是另一个方法突破

四次式与退化猜想已有JR来源。D候选改变的是证据级别与对象身份：
将原 $I_r$ 的实际临界代数、原基底函数和谱Weierstrass模型在所有有限点准确连接。
这比只给坏值根集、只算谱判别式更强；非约化重数与特殊 $t$ 不能用一般参数结论代替。

但一旦 B 的有限整约化模型与 C 的准确泛Jacobian都给定，
henselian截面—泛torsor平凡化—最小模型唯一性—Fitting理想保真是一条标准短链。
四维商代数与乘法特征多项式是明确的消元计算，不是新的最小模型或判别式理论。
这里的 $r$ 只经 $T=t^r,\varepsilon$ 进入最终模型也是结果的具体内容，
不是产生了无穷多项独立新发现。D结果新意为中等，作为B/C后的边际方法新意为低。
本段完全不预判准确坏值稿的数学独审结论。

## 5. 最近文献、访问缺口与检索范围

本实例再次读取 [JR arXiv submission history](https://arxiv.org/abs/2508.18578)：
入口仍列2025-08-26 v1、2026-01-16 v2；不能把该页措辞较强的摘要当成正文猜想已证。
[出版DOI的公开搜索索引](https://doi.org/10.1088/1751-8121/ae67bf)
仍给Conjecture1.2及3.7线索。此前direct访问被拒的记录沿用两份来源包，
本实例没有重试被拒路径、没有绕过，未取得完整出版§3.2。
出版编号／新增形式Lax警告仅按来源包的索引证据理解，不宣称与v2所有量词逐字相同。

本实例读了 [Roffelsen写作列表](https://proffelsen.github.io/writing) 的2026相关条目，
并复读 [2026-07-08的2607.06980v1](https://arxiv.org/html/2607.06980v1)
摘要及§1到旧qPI相关工作段：该段仍把旧曲线一般椭圆性列作猜想。
这支持问题仍被明确提出，不证明世界上不存在别处后继证明。
[2026-02-10的2602.09298v1](https://arxiv.org/html/2602.09298v1)
摘要与§1则明确为PIV／dPII及其投影约化；不是当前qPI四项结论的直接替代。
本实例未复读上述两篇的完整技术证明，不赋予它们超出所读段落的排他性结论。

本实例补充实际提交的公开检索式如下；Phase B每claim三种表达、多来源访问及半年窗记录
已全文消费输入包，本实例不冒称重新完成整个数据库／引文图检索：

- `"q-Painlevé I" "Jacobian" "proof" after:2026-03-08 before:2026-09-09`
- `"Arithmetic dynamics of a discrete Painlevé equation" "proof" "2026"`
- `"q-Painlevé" "critical scheme" discriminant`
- `"Halphen" "root of unity" "q-Painlevé I" elliptic`
- `"Arithmetic dynamics" "ae67bf" "Remark 3.6"`
- `"q-Painlevé I" elliptic proof 2024 2025 2026 Jacobian`

这些检索没有返回可核验的四claim全量词已证先例。部分命中四维扩展、别种Painlevé、
二手聚合和无关分析论文；本件没有拿题名／摘要索引代替相关定理阅读。
最近半年明确指2026-03-08至2026-09-08，不采信搜索引擎相对“几个月前”作为事件日期。

两份来源包中还有RJV03、Stokes–Takenawa–Carstea四维扩展、
Willox–Grammaticos–Ramani高阶去自治化等已读取范围及对象排除记录；
本实例没有独立复读这些全文，不把包的“实际读过”改写成本实例读过。
其余Stacks完成环／好约化条目与Liu–Lu交叉检查同理，未作为新增独立扣分证据。

Beauville原文在J作者任务曾读过；来源包的独立重取失败。
本实例未重新取其原文，也不继承作者的全文阅读身份。
标准谱对应的本轮直接阅读证据是IVY§4.3，属明确标注的Beauville定理重述。
Google Scholar安全页、Semantic Scholar不可用引文入口、Consensus仅有限元数据、
无相关本地PDF／Zotero／Obsidian等覆盖缺口均保留来源包记录；
这些来源本实例未重新连接，不能宣称完整前向引文覆盖。
领域不匹配的ML会议目录没有被伪装成数学查新数据库。
公开PDF使用正常GET和文本抽取输出至标准输出，未持久化下载；无额外外部授权扩展。

## 6. Phase D：各 claim 与总体判断

以下 HIGH／MEDIUM／LOW 表示扣除先例后的候选结果新意，不表示证明置信度。
`MEDIUM`指存在可定位的具体知识差额，但主问题／机制强依赖已知工作；
`LOW`指作为一般工具或局部步骤主要是既有理论的直接应用。这里没有一项评为 HIGH。

| Claim | 结果新意 | 最接近先例 | 保留delta | 方法／显然短应用判断 |
|---|---|---|---|---|
| A | MEDIUM | JR Conj1.2；JRV06§5 | 原全部状态、全有限域／参数、奇异层的准确原bins结论 | 已有几何和回返契约后是标准短推论；Hasse／分箱机制LOW |
| B | MEDIUM（下沿） | CD Prop2.2、CT Thm2.2、Mizuno E1格、JR一般亏格猜想 | 同一原八中心和原积分的全特征／每个t身份；所有有限纤维及实际临界概形 | Halphen、格、伴随、Chern主体LOW；增量集中在实际对象核对 |
| C | MEDIUM | JR原M与谱式；Beauville经IVY；IVY§4.4 | 实际二维动力坐标逆、固定谱差、任意r／全特征原K-torsor与无核Jacobian识别 | 方法主体LOW；不是直接代入IVY现成命题，但也不是新谱理论 |
| D | MEDIUM | JR四次猜想；标准最小模型／长Weierstrass／Fitting理论 | 原c的实际临界特征多项式，含碰撞／非约化重数，所有固定t与r | 相对B/C的边际方法LOW；准确finding强于根集，不独立加总 |

总体有界新意：`6.0/10`。这是解释性判断，不是统计估计、概率、全球证书或验收门槛。
量尺上，0–3接近已有结果重复／换写；4–6是已知方法下的具体结果推进；
7–10要求更明显的新方法、非预期结构或更广的独立理论增量。
本候选位于第二档上端：精确完成一个公开具体问题的多处对象桥具有可辨别增量，
但“椭圆化—谱Jacobian—判别式—Hasse窗口”的方向与大部分机制早已在先例中。

建议：`PROCEED_WITH_CAUTION`。

- 不选 `ABANDON`：本次已读一手资料没有直接覆盖原对象四claim全部量词的既成定理；
  留下的不是仅把变量改名，而是实际积分／纤维／谱模和局部临界重数的准确识别候选。
- 不选无保留 `PROCEED`：JR已经明确提出目标并指示谱矩阵与初值空间几何两条路线；
  JRV、CD／CT、Mizuno、IVY和标准模型理论实质压低方法新意。
  出版全文、完整前向引文图及Mizuno标记对应仍有限制，全球首创不能确定。
- 四块在同一问题上相互支持，A消费者与D局部桥大幅依赖B/C；
  不能把“每块都完整”换算成四倍新意，也不能因D包含重数就自动提升整篇至HIGH。
- 以上建议不依赖作者投入、批次需要、既有接受状态、文件长度或预期发表收益。

## 7. 建议定位与后续判断的触发条件

适当定位是“原JR有限阶qPI积分的全特征几何与谱模型识别，以及其算术和退化推论”。
在数学独审另行接受后，可以准确叙述为证明作者v2中的指定猜想、并给出概形级强化；
现阶段不能由本件直接登记猜想已关闭。
不宜使用“首次发现根单位q-Painlevé椭圆化”“新Hasse分箱原理”“新循环Jacobian理论”
或“首次提出四次坏值公式”等标题／摘要表述。

面向真正的新意争议，应把三类身份写明：已有定理直接给什么；原模型还缺哪项对应；
当前准确计算补上什么。N/G/F给出的结构与C的实际坐标逆是桥，
A和D是同一桥的算术／退化消费者，不制造四项平行理论突破的印象。

能实质改变本票的后续证据，是一篇可读先例已在原JR模型、原c和相同量词上完成这些识别，
或精确说明所有剩余桥均由一个现成命题立即推出；这会下调，必要时转为ABANDON。
相反，单纯多做小域计算、增加引理数、增写篇幅或数学独审通过，不会自动上调新意。
访问缺口不要求此刻停工或扩建文献基础设施；它限制的是全球首创措辞。

本文件全文自查后作为单次查新快照冻结；最终行数与SHA256随交接报告提供。
本件不是后续两份完整四门评审之一，不授予立项、稿件／PDF完成或任何外部效力。
