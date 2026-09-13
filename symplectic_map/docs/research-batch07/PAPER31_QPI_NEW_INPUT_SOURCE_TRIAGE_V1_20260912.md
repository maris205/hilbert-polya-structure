# Paper31：原族新输入的来源筛选 V1

日期：2026-09-12 UTC。执行者：主控 `/root`，Codex AI。
性质：`BOUNDED_SOURCE_TRIAGE`；不是查新分数、数学接受、候选准入或论文交付。
问题：上一轮关闭后，原 qPI 的一手文献是否给出本地尚未使用的具体问题或可核接口？
研究对象仍为原 $F_t(x,y)=(st/(sx-y),sx/y)$、$t\mapsto st$ 及其已接受完整模型。

## 1. 事前范围和证据纪律

先核原作者与当前一手来源，再按对象身份筛选。日期范围优先2024–2026；与具体接口直接有关的基础文献不限年份。
纳入原文、作者页和官方元数据；近名连续方程、其他差分族、四维扩展只作排除说明或 `ROUND2_CLUE`。
搜索索引可定位来源，不代替完整正文；没有找到后续证明不等于全球开放。
本件使用 `research-lit` 的来源／阅读分层，以及 `academic-research-suite` 的 Investigation 来源核查规则。
按 Codex 适配使用公开浏览和官方元数据；没有运行程序化书目解析器、付费服务或外部模型。
这不是PRISMA全量综述，搜索结果由工具合并返回，未虚构逐库总命中数、召回率或系统性覆盖证明。

本地先查指定论文目录及来源索引；工作区没有名为 `literature/` 的目录，名称筛选未定位可复用的JR/JL原PDF。
没有因此重扫旧构建树。既有来源报告只继承其明确读范围，不把别人读过的正文当作主控本次全文已读。

## 2. 已核一手来源卡

### S1. 原JR与作者当前目录

Joshi, N., & Roffelsen, P. (2026). *Arithmetic dynamics of a discrete Painlevé equation*. Journal of Physics A, 59, 195201.
[出版身份](https://doi.org/10.1088/1751-8121/ae67bf)、[作者目录](https://proffelsen.github.io/writing)、[arXiv](https://arxiv.org/abs/2508.18578)。
本次主控核作者目录全部条目、官方检索返回的出版元数据与指定正文；出版日期为2026-05-13。
此前DOI直达正文的robots拒绝保持；本次未重试该受限路径，搜索结果自然返回出版索引不等于访问恢复。
明确问题的正文逐项核对见已完成的[JR来源审查](PAPER31_QPI_NEW_INPUT_JR_SOURCE_AUDIT_V1_20260912.md)，114行报告已主控全文读取；该席的原文阅读不归成本次主控阅读。
旧原猜想、积分与循环消费者仍按[已有来源核查](PAPER30_QPI_JR_PUBLICATION_SOURCE_CHECK_V1_20260909.md)和实际本地接受范围扣除。

### S2. 七月新预印本：对象并非原qPI

Joshi, N., Lasic Latimer, T., & Roffelsen, P. (2026). *On difference-differential Lax pairs and integrals of Painlevé equations in finite characteristic*.
[官方元数据](https://arxiv.org/abs/2607.06980)、[v1正文](https://arxiv.org/html/2607.06980v1)。提交日期2026-07-08，仅核到v1。
实读：摘要、目录、§1、§10全部，另浏览返回的§9末段与附录A开头；不是全文证明审查。
该文收集连续 $P_{\rm VI},P_{\rm V},P_{\rm IV},P_{\rm III}$ 的差分—微分Lax对，并在正特征提取积分。
§10提出的 $P_{\rm I}$ Lax对、纯微分Lax积分及最小性问题不能改写成原qPI的新未解命题。
处置：`ROUND2_CLUE / DIFFERENT_SYSTEM`；不建立跨族研究任务。

### S3. 二月新预印本：同名“非自治”不构成同一对象

Joshi, N., & Roffelsen, P. (2026). *On integrals of non-autonomous dynamical systems in finite characteristic*.
[官方元数据](https://arxiv.org/abs/2602.09298)、[v1正文](https://arxiv.org/html/2602.09298v1)。提交日期2026-02-10，仅核到v1。
实读：官方摘要、定向返回的§2定理／Remark2.4、§4.2 Conjecture4.4及必要上下文、§4.3–4.4相邻段落；不是全文。
实际对象为连续 $P_{\rm IV}$ 与加法差分 $dP_{\rm II}$，并讨论到 $dP_{\rm I}$ 的射影约化。
可约纤维分类猜想、特征三Weyl归一化问题和Okamoto约化周期观察皆不能移作原乘法qPI的已授权候选。
处置：`ROUND2_CLUE / DIFFERENT_SYSTEM`。该文§4.4提到原qPI既有代数解，也不产生原族新增定理。

### S4. 原倍点接触可用的具体公式；不是新发现的论文

Ulmer, D., & Voloch, J. F. (2025). *New unlikely intersections on elliptic surfaces*.
[官方元数据](https://arxiv.org/abs/2508.06680)、[指定官方HTML](https://arxiv.org/html/2508.06680v1)。
实读：§1–3全部，以及§4.1–4.11（不含§4.12各例与全部参考文献）；最初读至Example2.7开头后，又补完§2剩余、§3与上述§4范围。
本次补读到的原工具把指定截面的 $p$-下降值写成其短Weierstrass坐标、导数和Hasse系数的明确式；好约化点上的切触给该值的消失必要条件。
原文要求 $p>3$、$j\notin K^p$，全局半稳定推论另有假设。无限阶不自动意味着不被 $p$ 整除；必要条件也不是准确切触清单。
这篇来源已在[旧POSTV2粗筛](PAPER30_QPI_POSTV2_IDEATION_V1_20260909.md)§3 N4列入并扣除，不能重记为新来源空白。
新工作只可能来自公式对**原回返点**的实际计算、例外位置处理和非零证明，是否有独立价值尚未判断。
元数据版本史为2025-08-08 v1，HTML顶部相同，但正文Date显示2026-08-24；保留这一区别，不据渲染日期声称存在v2或完成版本差分。
§3.1明确将该节固定在Igusa普遍族；Definition3.4后的“未知严格不等式例子”受此书面范围约束，不能直接改写成原qPI未解问题。
共同覆盖不自动使原指定截面下降为Igusa普遍族上的全局截面，局部允许截面集合也未获任意底变换不变性；主控和来源审查席的有界复读一致支持这项适用性限制，不声称作者主观仅关心该范围。
§4讨论复参数Betti叶的至少三阶接触，不是普通挠叶的二阶切触；本轮不把该节公式移作正特征或原倍点接触的充要判据。

### S5. 截面横截性已有强一般先例

Ulmer, D., & Urzúa, G. (2020). *Bounding tangencies of sections on elliptic surfaces*；以及两位作者的(2019)预印本 *Transversality of sections on elliptic surfaces with applications to elliptic divisibility sequences and geography of surfaces*。
[前者官方元数据](https://arxiv.org/abs/2002.01906)、[后者官方元数据](https://arxiv.org/abs/1908.02208)。
本次核官方摘要与版本史：前者最新列2020-05-26 v2，后者2020-10-20 v4；未另读完整证明。这里用预印本年份，不冒称本轮取得刊本；既有精确阅读范围见旧POSTV2 §3 N3。
特征零的有限切触与很一般曲面的横截性已经有先例；不能把原固定低维切片无证明地等同于很一般族。
本件不以摘要援引具体上界或删除原定理假设。

### S6. qdPI／椭圆整除序列线索须先做坐标身份核准

Hone, A. N. W. (2008). *Algebraic curves, integer sequences and a discrete Painlevé transcendent*.
[官方元数据](https://arxiv.org/abs/0807.2538)、[v1全文HTML](https://arxiv.org/html/0807.2538v1)。
实读：正文§1–3全部，参考文献仅开头；不称全文参考核验。
§3的标量qdPI为 $f_{n+1}f_{n-1}=(\alpha q^n f_n+\beta)/f_n^2$，并讨论双线性递推的算术性质。
本轮没有证明其与原 $F_t$ 的准确共轭，故不能借同名转移对象、根单位量词或原态标记。
官方评论明确提示正文一处猜想错误；不将旧“未来工作”或该猜想当成未解定理依据。
处置：`SOURCE_LEAD / OBJECT_IDENTIFICATION_NOT_SUPPLIED`，不运行其递推或把其数值观察变成原qPI候选。

## 3. 核验等级和限制

S1出版身份和S2–S4/S6作者预印本身份已由官方条目核实；“来源存在”不等于本件审查其证明正确性。
本研究是纯数学：实验设计I–VII分级不适配定理证明，标为 `DESIGN_LEVEL_NOT_APPLICABLE`；依据原命题、证明读范围与对象适配性评价，不能以生医证据金字塔授予数学PASS。
预印本明确保留未经本件确认同行审查的状态；S5仅摘要层，引用限于其明确宣称的研究范围。
没有核查付费Scopus/Cabell数据库，没有生成“所有来源无撤稿／无利益冲突”的认证；作者未声明或未实读的项均为未知。
没有下载本地PDF，因此没有本地PDF页锚或结构预检PASS。这里全部定位使用官方HTML章节或元数据。
文献集合以理论预印本为主，构成方法与载体集中提示；此为窄数学问题的范围特征，不作为质量或新意加分。

## 4. 实际公开查询记录

以下是主控本次按批实际提交的18条字符串；同批返回合并，未把零结果虚构为单条独立排除。

1. `"q-Painlevé I" arithmetic dynamics 2026`
2. `"Arithmetic dynamics of a discrete Painlevé equation" -site:researchgate.net -site:academia.edu`
3. `"q-Painlevé I" 2025 2026 conjecture`
4. `"q-Painlevé I" "height"`
5. `"q-Painlevé I" "arithmetic degree"`
6. `"q-Painlevé I" "2026" -"neural" -"Morlet"`
7. `"q-Painlevé I" "canonical"`
8. `q discrete Painleve first equation height growth Halburd`
9. `q Painleve I algebraic solutions irreducibility rational invariant non root unity`
10. `q Painleve I arithmetic 2024 2025 2026 Joshi Roffelsen new`
11. `q Painleve elliptic divisibility sequences torsion periodic parameters`
12. `"Painlevé" "division polynomials"`
13. `"QRT" "periodic" "division polynomials"`
14. `"elliptic surface" "torsion" "I8"`
15. `elliptic surfaces torsion sections tangency 2024 2025 2026 Ulmer Urzua`
16. `"Tate normal form" "ramification" "b"`
17. `"elliptic divisibility" "transversality"`
18. `"torsion" "Painlevé" "2026"`

其余操作是直接打开官方页面、点击作者目录与定向定位，不计为新查询。
近名检索返回的dPII高度定理、四维qPI扩展及连续方程不纳入原对象直接证据，未由其摘要推定原族结论。
后续只消费实际来源边界与[本地问题碰撞图](PAPER31_QPI_NEW_INPUT_LOCAL_COLLISION_MAP_V1_20260912.md)，
不重评旧完整候选、不自动接续POST_CLOSED N03/N10，不建立Paper31项目、source/publication locks、稿件或PDF。
