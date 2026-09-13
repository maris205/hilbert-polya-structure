# Paper31：指定 Tate b 的全阶实分歧强来源筛查 V1

日期：2026-09-12 UTC；执行者：`/root/p31_real_b_ramification_prior_screen`。
状态：BOUNDED_PRIMARY_SOURCE_SCREEN / NO_FORMAL_VOTE。
仅核来源包含关系，不重审已接受数学，不授新意、价值、证明信心或容量分数。

## 1. 结论及其边界

本轮三篇 primary 的已读正文没有给出 [BM] 的指定 b 正实分歧准确清单、临界值互异或 [OD] 的全偶数阶奇惯性结论。
这不是“未找到所以新颖”：已确认多个关键入口完全是旧结构，且出现一个必须继续扣除的精确近邻表达。
Streng 的 Siegel 函数公式把 b 的分歧问题写成指定对数导数组合的零点问题；当前 12 条查询没有完成该微分的专门零点理论筛查。
因此本件不能关闭全部强先例义务，更不能把全实旋转旧 FAIL 加本件自动改成正式准入。

三项判断均为“已读先例未直接强包含；创新份额仍需扣除／独立评价”，不是数字评分。
模解释、Tate 正规形、单位群生成、尖点阶、实模曲线的圈及拼接图均不能再作为新一般理论。
奇惯性的共轭配对论证仍只是 [BM] 的标准短消费者，不提供新的单中心或22–30页容量。

## 2. 输入与实际阅读

采用 research-lit 与 novelty-check，两个 SKILL.md 均本人 FULL 读取。
本任务由主控明确分派为 Phase A/B 有界来源核对；不执行 Phase C/D 完整候选报告，不假称跨模型验证。
工具发现没有配置 Zotero／Obsidian 接口；相关本地 PDF 文件名及指定 arxiv_fetch.py 路径检索无匹配，使用公开 web／arXiv 替代。
未扫描无关项目 PDF；主控另负责 Betti 强文与已失败 Lyness 基线，本代理不重复该部分广泛检索。

|输入|实际范围|SHA256|
|---|---|---|
|[D] 当前数学处置|FULL，109行|`940a86738f6293687a0f9f13e13f9da2cf2e479721b0191d5960ed4654580acf`|
|[BM] 实Betti／全实分歧证明|FULL，202行|`90eb1eda994228c028bd81e850faecbb830857e11fb4d7035f3e8fd08da16727`|
|[OD] 奇惯性消费者|FULL，64行|`c557ea48a985c1b3d066f32351cd71498becf8fbb69fc0ee270729cbcc5e7143`|
|[MB] 旧模入口|PARTIAL，仅§2，先rg定位、再读20–42行；未显示§3–8|未重做旧文件完整性审查|
|[SC] 新问题初筛|PARTIAL，1–36、109–205行，含景观、来源账及旧查询|其链接文献不自动计本人亲读|

没有重读旧 N4–9 计算、尖点证明、原固定T证明或正式双 FAIL 票；它们的状态仅由 [D] 消费。

## 3. 三个准确 Claim

对象始终是通常 $X_1(N)$，$N\ge4$，及指定 Tate 函数 $\beta_N=b=T$。
原方程 $v^2+huv-Tv=u^3-Tu^2$ 的标点用 $R=-P=(0,0)$ 对应先例，$B=b=T,C=c=1-h$。
$(E,P)$ 与 $(E,-P)$ 已经通过带点同构识别；不得再施加一个符号二次商。

1. **C1：准确实点清单。** 所有满足 b>0 的实分歧点，各 e=2，与
   $A_N=\{m:\gcd(m,N)=1,\ 5N/8<m<2N/3\}$ 一一对应；N偶时另加
   $B_N=\{m:\gcd(m,N/2)=1,\ 3N/8<m<N/2\}$。
   这是整个紧化的实点结论；不声称所有映向正实值的复分歧点已分类。
2. **C2：同阶实临界值分离。** 固定N，C1所数实临界b两两不同；A组b<1，B组b>1。
3. **C3：实际奇惯性。** 每个所数实临界值的几何局部惯性为奇；全部偶数N≥10都有b*>1见证。
   奇置换不等于单枚二换位、不可分解覆盖或满对称群。

## 4. 三篇 primary 的实际强映射

### 4.1 van Hoeij–Smith：尖点除子，不是非零值分歧除子

Mark van Hoeij、Hanson Smith，*A Divisor Formula and a Bound on the Q-gonality of the Modular Curve X1(N)*。
正文使用 arXiv:2004.13644v2（2020-05-03；正文日期May5）；正式发表 Research in Number Theory 7:22（2021），DOI10.1007/s40993-021-00243-3（[NSF存档元数据](https://par.nsf.gov/servlets/purl/10310037)）。
Thm4.2给 $\operatorname{ord}_{C_c}(F_k)=e_c(N)v_k(c/N)$，其中v由min函数组成。
§6.3 Lemma6.2及式(36)给Tate形、$B=-F_3,C=-F_4$、精确阶模解释。
这些准确命中我们的旧入口及零极点来源，但 $\operatorname{div}(b)$ 不等于 $\operatorname{div}(db)$；有限非零值处的临界阶不能从函数阶零读出。
§2.2的实Abel–Jacobi矩形与primitive分数也使“精确阶转成有理角”属于明确旧结构。[VHS]

具体包含判定：C1需要非尖点处db=0的穷尽、二阶性及实性，C2需要这些零点的b值分离；上述公式没有给这些步骤。
因此“他们只算尖点，而我们算好点”只是对象差分，尚不自动证明创新价值。

### 4.2 Streng：同一个b已有显式Siegel表达

Marco Streng，*Generators of the group of modular units for Γ¹(N) over the rationals*。
正文使用 arXiv:1503.08127v3（2022-12-13）；正式发表 Annales Henri Lebesgue 6（2023）95–116，DOI10.5802/ahl.160（[官方元数据](https://www.numdam.org/articles/10.5802/ahl.160/)）。
Lemma2.1含Tate正规形完整证明；Prop2.4识别精确阶开曲线；Thm1.1／1.2给单位群的两套生成元。
Lemma3.3写 $t=H_1^2H_3/H_2^3$、$p_k=t^{k^2-1}H_k/H_1$；因$p_2=-b$，有

$$b=-\frac{H_1^5H_3^3}{H_2^8}.$$

这是同一Tate函数，不是相似函数。其Γ¹/Γ₁参数差由Remark2.14的$\tau\mapsto-1/\tau$明确处理，不能忽略后直接比较q符号。[STR]

由该旧公式作形式对数微分（本件的包含映射推论，不是新增已审定理），非尖点b≠0处

$$db=0\quad\Longleftrightarrow\quad 5\,d\log H_1+3\,d\log H_3-8\,d\log H_2=0.$$

所以存在被已有Siegel函数对数导数零点理论强包含的具体风险；这比泛查“modular units”更具体。
已读Streng段落没有给该组合沿全部实模弧的零点准确数、非退化性或零点值分离。
本轮没有检查这一个重二模微分的专门零点文献，亦没有证明它属于任何特定已知零点定理的假设类。
“Eisenstein型对数导数组合”仅是后续检索术语；不是把未经核实的一般Eisenstein零点结论引用为本b定理。

### 4.3 Snowden：全部实模曲线拓扑已知，但图没有给b的驻点

Andrew Snowden，*Real components of modular curves*，arXiv:1108.3131v1（2011-08-16；正文日期Aug15），本件只认证此预印本版本。
§1.1将实点集合写成由实尖点／适当椭圆点及实弧组成的图；§6.4给通常X1(N)的完整符号拼接。
写$N=2^rN'$、N'奇，实圈数为r≤1时$\psi(N')$，r≥2且N≠4时$\varphi(N)/4$，N=4时1；$\psi$是模去−1与2生成子群的指数。
这是同一实模曲线的强先例，不能宣称我们首次分类其全部实圈。[SNO]

但C1是额外函数b在这些圈上的临界点，C2是这些临界点的函数值；拓扑拼接与计圈没有直接算db或其零点的b像。
可能的强包含链应当是“Snowden实弧＋Streng显式b＋已有单调／零点定理”。本轮只核到前两环，末环未闭合。
没有用拓扑图猜测或新增证明极值数；更未执行Snowden的算法或附录阶数表。

## 5. 逐 Claim 的 prior 压力与剩余信息

|Claim|已确认应扣除的内容|本轮尚不能由先例推出的内容|处置|
|---|---|---|---|
|C1|通常X1(N)、唯一Tate形、分数阶条件、显式b、尖点函数阶、实圈拓扑均旧|指定db沿全部实弧的恰好零点数与非退化；其核心来源仍需与固定T严格表／新M排序区分|不是新模对象或新通用计数机制；准确结果仍待强包含闭合与价值判断|
|C2|源曲线实拓扑不能作为临界值分离的新技术|同阶不同实临界点b像互异；需要实际严格M排序，或旧微分零点／单调理论的包含映射|未在已读三篇中找到该断言；不据此授新意PASS|
|C3|共轭点成对使符号贡献为偶、唯一实e2给奇号均标准|覆盖级别的输入来自C1/C2；全偶数阶存在性由m=n−1立即消费|仅短推论；不能单列一般群论创新或追加一份容量|

C3的压力不因未查到同一句话而减轻：其新信息完全依附C1/C2，不能把应用换名当第二中心。
本件不给“单枚transposition”的先例比较结论，因为当前已接受数学本来就没有该命题。
收束前主控消息确认：已另做针对该对数导数组合的6条有界查询，未命中直接零点定理；本代理不重复扩搜。
该消息不是本人新增查询或亲读证据，具体日志及另外Betti来源由主控另件保存，本件仍只报告自己的12条边界。
接下来由fresh非作者做独立单中心价值审查；末环的NOT_FOUND不会替代该审查，也不应成为无限检索的理由。

## 6. 实际查询全日志（12条，未追加）

全部执行于2026-09-12 UTC。前三组变体分别是Tate normal form／modular units／real components；后加branch values／monodromy／inertia。
1–4、5–8、9–12分别为三次并列search调用。普通web无域限制；第12条限定arxiv.org、recency=183天。

1. `"Tate normal form" "ramification" "real" "b"`
2. `"modular units" "real" "critical values"`
3. `"X1(N)" "real" "ramification"`
4. `"Tate" "modular" "inertia" "b" 2024 2025 2026`
5. `"van Hoeij" "Smith" "modular units"`
6. `"Streng" "Generators of the group of modular units"`
7. `"real components" "modular curves" Snowden`
8. `"Tate normal form" "critical" "monodromy"`
9. `"modular unit" "real" "ramification" "critical points"`
10. `"Tate normal form" "branch values" "distinct"`
11. `"modular curves" "real" "odd" "monodromy"`
12. `modular units Tate real ramification critical values inertia 2024 2025 2026`（arxiv.org；最近183天）

Q5–7返回上述三篇最相关primary，Q1–4／8–11多为无关或更一般材料；并列返回没有逐条完整归因，不制造每条精确命中表。
Q12虽设置最近半年，返回可见arXiv结果包含2025-08旧日期及无关Mazur–Tate元素；故不声称最近半年已完整排除。
搜索器把旧文标为“若干月前”的抓取日期，均未当发表日期；Q4的2026二次数域扭增长官方结果仅作摘要级排除，未读作第四篇primary正文。
MathOverflow、ResearchGate、聚合综述和无关工程“modular units”结果均非本件科学依据。
第三次search与随后PDF初开并列输出发生截断，截断在无关搜索结果区；所消费三篇正文另有单独可见输出，不把截断区记FULL。

## 7. 外文阅读账与停止纪律

所有外文均PARTIAL；未称任何整篇PDF FULL，也未下载本地PDF。

|来源版本|真正消费的正文段落；web文字行以该版本返回为准|未认证内容|
|---|---|---|
|VHS 2004.13644v2，18页|§1（0–57）；§2.2（127–394）；Thm4.2及证明（721–775）；§6.2末的规范说明（1258–1279）；§6.3（1280–1519），包括Lemma6.2、式36–39|其余证明未FULL；工具附带显示的§5度数例及Appendix A开头未作为本件创新依据；没有读/跑计算网站|
|STR 1503.08127v3，17页|摘要、§1／§1.1及§2.1主要模解释（0–369）；Remark2.14／2.15（654–691）；Lemma3.3完整陈述和证明（851–912）|§4主生成定理证明、后部theta公式未读；初开附带例2.10／2.11未消费；没有运行Sage命令|
|SNO 1108.3131v1，33页|摘要、§1.1–1.2（0–108）；§6.4完整（1922–2078），包括三类r的符号推导和Prop6.4.1|§§2–5总图定理证明未FULL；工具前后附带§6.3／6.5片段不作b结论依据；附录表不消费|

Streng正式版官方PDF入口初开只取得页数／行数，随后两次find无匹配，一次正文open报400 Timeout，立即停止该入口；
随后使用任务既有、公开arXiv v3入口成功读到正文，不作镜像枚举或受限入口重试；2023正式版元数据只由官方Numdam结果核对。
SNO一次find(`1.2.`)自动回显远处附录N表匹配片段，已即时报告主控；未转录、消费、计算或进一步打开该表。
后续按已知正文行号开§6.4；没有执行N≥10枚举、数值、CAS、方程或群表扫描。
没有第四篇有足够相关性的primary正文，因此在三篇停止，保持“最多四篇”上限而非凑数。
只新增本文件，未修改冻结稿、锁、FAIL票或已接受产物，无投稿、上传、对外消息、付费资源或Git操作。

[D]: PAPER31_QPI_REAL_BETTI_AND_ODD_INERTIA_DISPOSITION_V1_20260912.md
[BM]: PAPER31_QPI_REAL_BETTI_MODULAR_FEASIBILITY_V1_20260912.md
[OD]: PAPER31_QPI_REAL_BRANCH_ODD_INERTIA_COROLLARY_V1_20260912.md
[MB]: PAPER31_QPI_MODULAR_B_MONODROMY_FEASIBILITY_V1_20260912.md
[SC]: PAPER31_QPI_POST_REAL_NEW_PROBLEM_SCREEN_V1_20260912.md
[VHS]: https://arxiv.org/pdf/2004.13644v2
[STR]: https://arxiv.org/pdf/1503.08127v3
[SNO]: https://arxiv.org/pdf/1108.3131v1
