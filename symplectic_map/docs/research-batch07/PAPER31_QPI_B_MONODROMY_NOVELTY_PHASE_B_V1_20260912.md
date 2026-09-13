# Paper31：指定 b 覆盖全阶单值群查新 Phase B V1

日期：2026-09-12 UTC；本人实际检索／核读自 17:21 起，17:26:08 再核 clock。
作者：/root/p31_b_novelty_phase_b；性质：有界来源核查，不是 Phase C/D 或四门评价。
状态：PHASE_B_SOURCE_PACKET / NO_NOVELTY_SCORE / ALL_N_CONJECTURE_UNCHANGED。

## 1. 固定输入、权限与结论边界

本人全文读取 novelty-check SKILL、WORKFLOW 39 行、[Phase A][A]66 行及[既有诊断][M]173 行。
Phase A SHA256：6740c84a45ef60b5f86118837307380a7895c4f47be8ec860dfac9ab57f54f3d。
既有诊断 SHA256：a6f5ceee1ddb47da09d80d010e3ae4749f0c133326baf850c01e9c462f36c6a9。
本件只使用 novelty-check 的 Phase B；未调用 ARS bibliography/source-verification 角色或其认证程序。
未读取本轮并行数学机制作者的新文件，故以下比较始终针对 Phase A 固定的未证问题。
只拥有本新文件；未更改旧 FAIL、旧数学、Papers27–30、当前接续、锁或稿件。

对象为代数闭特征零域上通常的 $X_1(N)$、Tate 形
$y^2+(1-c)xy-by=x^3-bx^2$ 及指定 $\beta_N=b:X_1(N)\to\mathbf P^1_b$。
B1 是全 $N\ge4$ 满 $S_{d_N}$ 或真实例外；B2 是不预设中间曲线类型的全部中间域；B3 是实际足够惯性。
在本件已核来源范围中，未定位到直接完成 B1、B2 或全阶 B3 的定理。
这句话只描述检索所得，不能推出无先例、猜想正确、finding 新颖或长文价值通过。
已发现的最强吸收材料覆盖正常形／精确阶模型、模单位群、尖点阶、低次数函数和标准稳定子方法。
因此“换一种 primitive 表述”“重算 b 的除子”“优化另一个投影”均不能算解决 B2/B3。

## 2. 搜索实施与覆盖缺口

本人实际执行 36 条 web 查询，核心 B1/B2/B3 各至少四种原样表达，见第6节。
来源入口包含公开 web、arXiv 题录／PDF、Scholar 及 Semantic Scholar 的公开搜索页和站点限定检索。
工具发现没有专用 arXiv／Scholar／Semantic Scholar 学术 MCP；公开浏览为现有替代，不声称原生数据库检索成功。
基础文献不限年；明确执行 2024–2026 及 2026-03-12 至 2026-09-12 最近六个月查询。
搜索引擎的 after/before 是所提交查询条件，不保证返回集合已严格按论文发布日期筛好；逐项日期另核。
ICLR、NeurIPS、ICML 数据库对此纯数学问题为 NOT_APPLICABLE；没有虚构会议检索或 ML 实验。
检索工具未提供可复核的总 hit 数；本件不报告总命中量、PRISMA 流程数或完备召回率。
搜索结果含大量建筑、软件 modular unit、泛 Tate conjecture、一般单值矩阵等词义噪声，未纳入科学证据。
不因同现 “Galois”“Tate”“primitive” 就纳入直接重叠；须核对象、基域、指定函数及结论量词。

| 实际入口／失败对象 | 本人取得的返回 | 如何处理 |
|---|---|---|
| Scholar：Tate normal form + monodromy；modular units + indecomposable；modular units + ramification | 三个搜索页均 Internal Error，正文说明 not safe to open (non-retryable error) | 不猜是 robots/403；站点限定查询也不等同搜索页覆盖 |
| Semantic Scholar：上述 monodromy、intermediate covers、ramification 三页 | 三页同样 not safe to open (non-retryable error) | 留数据库覆盖缺口；未调用其 API 或凭据 |
| arXiv 搜索页：Tate normal form，按最新排序 | Failed to fetch，TimeoutError | 改用可达公开题录/PDF及站点限定检索；不重启任何任务 |
| Koo–Shin KAIST 旧稿 PDF | Internal Error，单行且无明确原因 | 后来取得主控定位的 IMPAN 出版社 PDF；两入口不冒称同版 |
| García–Selfa 等 idUS PDF | Internal Error，单行无原因 | 已有独立 arXiv v3 可读，不解释为权限拒绝 |
| García–Selfa 等 ScienceDirect 题录页 | 后续 open 明确 (403) Forbidden | 停止该入口；其先前搜索呈现的 DOI/刊期与 arXiv 原文分开 |
| Fricke families II ScienceDirect 页 | Internal Error，单行无原因；搜索呈现公式多处缺失 | 列为未充分读取线索，不消费缺式 Theorem 3.2 |

没有下载私稿、上传、对外发信、购买全文、运行 Python resolver、提取凭据或调用外部模型 API。
原文消费以下列本人范围为准；获得 PDF 句柄不等于阅读完整 PDF，更不等于独立证明验收。

## 3. 去重后的主要来源与本人核读矩阵

同题名／作者／DOI 的 arXiv、期刊、机构副本合并为一个条目；不同版本日期分列。
表内S1–S9及下述S10均取得一手正文；第5节另列未读／不纳入线索，不补造等级。

| ID | 一手来源及版本身份 | 本人实际读取范围 | 与 B1–B3 的直接边界 |
|---|---|---|---|
| S1 | van Hoeij–Smith, *A Divisor Formula and a Bound on the Q-gonality of the Modular Curve X1(N)*；[arXiv 2004.13644v2][S1]，2020-05-03；刊本 RNT 7(2021)22，DOI 10.1007/s40993-021-00243-3 | 摘要／§1 全文；§2.2 尖点行计数；Theorem4.2及证明、Remark4.3；§6.3至式(39)；Appendix A 的命题陈述及证明开头 | 同一 b=-F3；全阶尖点除子和次数是必扣输入，不是 b 覆盖满群定理 |
| S2 | Streng, *Generators of the group of modular units for Γ¹(N) over the rationals*；[AHL 6(2023)95–116][S2]，DOI 10.5802/ahl.160 | 摘要；§1（含1.1）全文，Theorems1.1–1.2；§2.1的Lemma2.1陈述；Propositions2.4–2.5、Theorem2.8陈述 | 精确正常形模模型和单位自由基包含 B；单位生成不等于 C(B) 在函数域中极大 |
| S3 | Derickx–van Hoeij, *Gonality of the modular curve X1(N)*；[arXiv 1307.5719v3][S3]，2014-04-01；J.Algebra417(2014)52–71，DOI 10.1016/j.jalgebra.2014.06.026 | 摘要／§1 全文含Remark1；§2开头定义；Theorem4陈述与证明说明 | 最小次数、LLL模单位搜索及 j-上子域；不分类指定 b 的所有中间域 |
| S4 | Koo–Shin, *Function fields of certain arithmetic curves and application*；[IMPAN刊本][S4]，ActaArith141.4(2010)321–334，DOI 10.4064/aa141-4-2 | 刊本无单列摘要，§1 全文；Lemma3.1、Theorem3.2及证明；Theorem3.5及证明 | 通过 ord_q 比较和稳定子给 C(j,g) 及 Fricke 商生成；基域和指定函数与 C(b) 不同 |
| S5 | Jung–Koo–Shin, *Primitive and totally primitive Fricke families with applications*；[arXiv1506.06317v3][S5]，2016-11-11（首稿2015-06-21） | 摘要／§1全文，primitive定义；Prop4.1及证明；Th4.3(i)陈述和部分证明；Th4.4(i)(ii)陈述及几何证明开头 | primitive 意为标记只在±同余时相等；应用是 C(X(N))/C(j)生成，不是 b 投影的无块系 |
| S6 | Orlić, *Tetragonal intermediate modular curves*；[arXiv2407.14512v1][S6]，PDF标2024-06-26；[刊本题录][S6P]ActaArith220(2025)263–288，DOI10.4064/aa240831-22-3，online2025-09-15 | 摘要／§1 全文，Theorems1.1–1.5及研究方法说明；未运行其代码或核全证明 | 分类 X1→XΔ→X0 范围的 gonality；不能限制 B2 的任意中间曲线 Y 为这些 XΔ |
| S7 | García–Selfa–González–Jiménez–Tornero, *Galois theory, discriminants and torsion subgroup of elliptic curves*；[arXiv0811.1463v3][S7]，页边2009-06-30；JPAA214(2010)1340–1346，DOI10.1016/j.jpaa.2009.11.001 | 摘要／§1全文；§3 Tate 参数和低阶族；§9 Theorems1–2全文；未核所有中段证明 | N5/7/9参数已出现，但其 S3 是 Q(E[2])/Q 的算术群，不能冒认指定 b 覆盖几何群 |
| S8 | Brunault, *On the ramification of modular parametrizations at the cusps*；[arXiv1206.2621v3][S8]，2018-12-14；[JTNB28(2016)773–790题录][S8P]，DOI10.5802/jtnb.963，online2017-01-03 | 摘要／§1全文，Theorem1.2和Remark1.3；§2开头的分歧定义/引理 | 研究 X0(N)→E 的新形式模参数化；不是 X1(N)→P1_b，不能直接解决有限非零值尖点 |
| S9 | Sutherland, *Constructing elliptic curves over finite fields with prescribed torsion*；[arXiv0811.0296v4][S9]，2012-03-27；Math.Comp81(2012)1131–1147，DOI10.1090/S0025-5718-2011-02538-X | 摘要／§1全文；§2 raw form、Algorithm1、Proposition1及证明；§3优化问题陈述和Algorithm2 | 原 b,c 与 r,s 字典、精确阶因子去除和优化平面模型均已知；优化坐标投影不等于指定 b |

另纳入最近六个月的一手来源 S10：
[Matthew Baker, *Elliptic matroids and modular curves*, arXiv2608.05299v1][S10]。
arXiv提交2026-08-05，PDF内部2026-08-07；[作者官网][S10A]列为 preprint，无期刊发表锁。
本人读摘要及§1.1–1.3全文，含Theorems1.1–1.2；没有核41页全部证明。
该文对 n≥10、char(k)∤n，建立 X1(n)^circ 与椭圆拟阵实现空间的域值／Z[1/n]概形对应。
这里 circ 保留不可约结点立方对应的尖点、移除可约Néron多边形尖点，并不是一律删去全部尖点。
该文 β 是模空间到 realization scheme 的同构，不是本件 β_N=b，不能因字母相同推定覆盖了 B1。
它是最近模型/边界重述的强对照；从所读摘要和主定理不能取得指定 b 的中间域或惯性结论。
此处只记录文中定理主张和适用性，不把预印本状态或作者检查声明当作本项目独立证明接受。

日期纪律：S1内部Date是2020-05-05而页边v2为05-03；S3内部04-03而v3为04-01；均非新版本误判。
S1另实际读取[刊本][S1P]首页及§1，核实期刊DOI；本件主体定理编号和核读范围按arXiv版本记录。
S7所取PDF页边v3为2009-06-30，但内部Date显示2018-11-01，差异保留，不据此声称2018新定理。
S6近期刊本题录与2024预印本合并；所读定理明确归于v1，不声称逐式比过刊本。
搜索“数月前发布／抓取”标签不能覆盖上述原文和正式题录日期。

## 4. WHY／HOW／WHAT：每一审查面的强先例与剩余义务

### B1：全 N 的指定 b 几何单值群

WHY：消费者是原精确周期能级随 T=b 的置换及闭合方程的几何分裂域，不是给模曲线再添一个模型。
HOW：拟议路线为 B2 的本原性加 B3 的实际惯性；传递性与本原加二换位均属标准工具。
WHAT：必须得到全N满群或准确反例／例外，N4–9短表不能成为全称替代。
最强直接对象对照是S1/S2/S9；它们已给同一模型和全阶代数描述，故“能写方程、算次数”全部扣除。
S7给出的S3只针对mod-2算术表示；S5自然j覆盖的SL2群也不回答b投影。
已核来源未找到B1定理不等于B1有高新意；仍须证明finding不被其它指定模单位研究吸收。

### B2：指定函数不可分解／任意中间曲线

WHY：无diamond稳定子只排除一类对称商，不能排除非Galois中间覆盖。
HOW：S4/S5展示用q阶比较排除标记稳定子、在j扩张里给primitive generator的成熟方法。
WHAT：本题仍要处理 C(b)⊊K⊊C(X1(N)) 的全部 K；不能把 K 限成 C(Y)且Y有理或模商。
S3的子域以j为底，S6的中间曲线是XΔ；这些是强工具／强警告，尚不是指定b的分类。
S2单位自由基里的b、S1整系数primitive、S5标记primitive、置换primitive四个概念不可互换。
即使证明C(X1(N))=C(j,b)，也仅说明在已固定j时b分离相应标记，不自动说明C(b)没有中间域。
必须让所有“排除稳定子”的新短引理与S4/S5方法逐项扣除；仅更换具体Siegel积不能自动成为独立贡献。

### B3：实际惯性与有限非零值边界

WHY：单支值上多个e=2点给二换位乘积，不能任选其中一枚来套满S判据。
HOW：S1的MinFormula和Siegel积q展开给b在0/∞上的尖点阶及几何重数；这部分已知。
WHAT：仍需证明某条实际群生成路线全阶可用，并处理同支值多点、有限非零值尖点、可能e=3点。
S8只在其模参数化／twist-minimal假设下给尖点不分歧，不能移植为本件边界不分歧。
S10加强模空间边界模型的既有描述，不提供b−b_*在该尖点的首非零项。
因此局部厚度≤3、div(b)完整、Riemann–Hurwitz总量三者均不能单独或无桥接合并成B3。
本件没有证明新的临界值分离、单二换位存在或全阶例外；这些仍须实际数学而非查新记录闭合。

## 5. 排除、未读线索与并行边界

独立只读定位子代理 b2_primary_locator 执行6条查询并核读4篇；其结论不是正式独立查新评分。
其S1/S2/S3/S9提醒均已由本人上述原文范围复核，不把其HTML全文声明移植为本人的阅读声明。
它另读 Pribanić, *Radical isogenies and modular curves*, arXiv2210.12840 的Theorem4.2：
该代理指出对象为X1(N²)至X0(N)的同源塔；本人未读原文，故仅保留排除方向的转述，不用其定理支持本件断言。
Fricke families II（JMAA2019，DOI10.1016/j.jmaa.2018.11.033）只有搜索呈现与失败open。
其多处关键公式空缺，不能称已核主定理或断言它没有更强的B2内容；保留可由C/D继续核查的来源缺口。
搜索还出现 *Mean field equations, hyperelliptic curves and modular forms: I* 的单值问题片段。
本人未读其摘要／引言／实际覆盖定义，未把Lamé／平均场相关结果当作指定b先例或可直接移植方法。
固定T的Kummer满像、泛j覆盖、一般算术特化、其它dynatomic系统均未拼入本题。
跨系统族仅可记ROUND2_CLUE；本件不启动新族、不扩N≥10扫表，也不改原全N目标。

## 6. 本人实际 query 账本

下列均于2026-09-12 UTC实际提交web搜索；Q1–12是固定三面的事前核心，Q13以后为定位／核对。
同一调用内的查询返回有聚合，故只记录实际取得的可用线索，不给每条伪造hit数量。

| # / 面 | 原样 query |
|---|---|
| Q01 B1 | "Tate normal form" "b" "monodromy" |
| Q02 B1 | "modular unit" "symmetric group" "X1" |
| Q03 B1 | "Tate normal form" "Galois group" 2024 2025 2026 |
| Q04 B1 | site:arxiv.org "modular" "b" "monodromy" after:2026-03-12 before:2026-09-13 |
| Q05 B2 | "Tate normal form" "indecomposable" |
| Q06 B2 | "X_1(N)" "intermediate" "modular units" |
| Q07 B2 | "modular unit" "decomposition" "cover" 2024 2025 2026 |
| Q08 B2 | site:arxiv.org "modular units" "cover" after:2026-03-12 before:2026-09-13 |
| Q09 B3 | "Tate normal form" "ramification" "b" |
| Q10 B3 | "modular units" "critical values" ramification |
| Q11 B3 | "modular curve" "inertia" "symmetric group" 2024 2025 2026 |
| Q12 B3 | site:arxiv.org "modular" "ramification" "units" after:2026-03-12 before:2026-09-13 |
| Q13 B2 | "Tetragonal intermediate modular curves" arxiv |
| Q14 B2 | "Gonality of the modular curve X1(N)" Derickx van Hoeij |
| Q15 B1 | "modular units" "monodromy" mathematics |
| Q16 B2 | "modular functions" "indecomposable" covers |
| Q17 B1 | site:scholar.google.com "Tate normal form" monodromy |
| Q18 B1 | site:semanticscholar.org "Tate normal form" monodromy |
| Q19 B2 | site:scholar.google.com "modular unit" "indecomposable" |
| Q20 B3 | site:semanticscholar.org "modular units" ramification |
| Q21 B1 | "Galois theory, discriminants and torsion subgroup of elliptic curves" arxiv |
| Q22 B3 | "On the ramification of modular parametrizations at the cusps" arxiv |
| Q23 B1 | "modular units" "monodromy" after:2024-01-01 before:2027-01-01 |
| Q24 B1 | "X1(N)" "monodromy" after:2026-03-12 before:2026-09-13 |
| Q25 全面 | site:arxiv.org "modular units" after:2026-03-12 before:2026-09-13 |
| Q26 B2 | site:arxiv.org "X_1(N)" "intermediate" after:2026-03-12 before:2026-09-13 |
| Q27 B3 | site:scholar.google.com "Tate" "ramification" "modular" |
| Q28 B2 | site:semanticscholar.org "modular" "indecomposable" "curve" |
| Q29 元数据 | "Tetragonal intermediate modular curves" "10.4064" |
| Q30 元数据 | "Primitive and totally primitive Fricke families with applications" DOI |
| Q31 B3 | "modular units" "ramification" "2026" mathematics |
| Q32 B1 | "Tate normal form" "2025" "2026" "cover" |
| Q33 全面 | "Elliptic matroids and modular curves" Baker |
| Q34 B1 | "modular unit" "geometric monodromy" mathematics |
| Q35 B3 | "Tate normal form" "branch points" |
| Q36 B2 | "Tate normal form" "decompositions" |

Q01–12聚合结果包含S7和S8线索、Orlić题名及无关词义结果；Q13–16定位S1/S3/S6。
Q17–20／Q27–28站点限定结果未给可核直接b结论，且不能弥补对应搜索页访问失败。
Q21–22取得S7正确arXiv标识与S8；Q29–30核S6刊期并暴露Fricke II的未读缺口。
Q25–26返回的2026材料含机械modular units与Waring问题，均排除；未记为本领域正证据。
Q31–32出现Baker题名的二手线索；Q33再定位本人可读的S10原文与作者官网。
最近六个月因此有实际原文筛查S10，但不是对该窗口内全部arXiv的系统性穷尽。

## 7. 交给 C/D 的准确包与冻结边界

交接对象是[A]固定B1–B3、[M]已有诊断、S1–S10强对照及第2/5节保留的来源缺口。
C/D须把方法新意与未证finding的潜在新意分开；不能以本件“没找到直接定理”自动给高分。
GPT-5.4 MCP不可用的fallback披露由主控处理；本件未伪称cross-model或人类审读。
本件不授HIGH/MEDIUM/LOW、分数或PROCEED/ABANDON建议；也不是正式双席四门。
未解除旧准确厚度双FAIL；Paper31仍非已准入项目，正文22–30页和Batch07完整五篇目标保持。
冻结：提交本件SHA256、行数、字节数后停止编辑；无任何外部效力。

[A]: PAPER31_QPI_B_MONODROMY_NOVELTY_PHASE_A_V1_20260912.md
[M]: PAPER31_QPI_MODULAR_B_MONODROMY_FEASIBILITY_V1_20260912.md
[S1]: https://arxiv.org/pdf/2004.13644
[S1P]: https://par.nsf.gov/servlets/purl/10310037
[S2]: https://ahl.centre-mersenne.org/item/10.5802/ahl.160.pdf
[S3]: https://arxiv.org/pdf/1307.5719
[S4]: https://www.impan.pl/shop/en/publication/transaction/download/product/83037
[S5]: https://arxiv.org/pdf/1506.06317
[S6]: https://arxiv.org/pdf/2407.14512
[S6P]: https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/online/116129/tetragonal-intermediate-modular-curves
[S7]: https://arxiv.org/pdf/0811.1463
[S8]: https://arxiv.org/pdf/1206.2621
[S8P]: https://www.numdam.org/item/JTNB_2016__28_3_773_0/
[S9]: https://arxiv.org/pdf/0811.0296
[S10]: https://arxiv.org/pdf/2608.05299
[S10A]: https://sites.google.com/view/mattbakermath/publications
