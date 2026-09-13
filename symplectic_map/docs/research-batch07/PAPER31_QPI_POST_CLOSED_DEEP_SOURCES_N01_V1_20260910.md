# Paper31：N01 逐主张深查新来源席（Phase B，V1）

日期：2026-09-10（项目日期）；实际公开检索执行于2026-09-09 UTC。执行席：`/root/p31_post_closed_multiplicative_landscape_v1`。
状态：`NOVELTY_PHASE_B_SOURCE_ONLY / NO_SCORE / NO_MATHEMATICAL_DIAGNOSTIC / NO_CANDIDATE_ADMISSION`。
`route_applicability: NOT_APPLICABLE`。本件不是正式独立票、跨模型验证、N02形式性证明或P31准入。

## 1. 绑定输入与范围

本人FULL读取 `novelty-check/SKILL.md`（86行）及[Phase A逐主张包][CLAIMS]92行；只执行§2的N01-C1/C2/C3来源工作，不启动技能Phase C/D。模型沿用默认，不覆盖为技能提及但当前未配置的GPT-5.4 MCP。
本席先前写后FULL读回的[乘法地形][LAND]155行、[N01–N03首筛][QF]110行保持冻结；本轮按有关问题回看，不重扫旧构建、旧证明或其他席报告。外文身份不因读本地报告而升级为FULL。

| 直接输入 | 绑定SHA-256 |
|---|---|
| CLAIMS | `8a8b9ba44f5e98e9ea6c31820c299dc69b81fe76b4f0ff8f67850f09a048a0a3` |
| LAND | `6a01ce0ffde645d16a5c201e7603e5a0b5bf0c163fd98f9f5b124bffacdb6deb` |
| QF | `9b2b0a56465c5f0f89da3c668979f5034608fe4a74794e01476116b0684e9c54` |

固定单位时间原对象为 $R_u=\mathbb Z[q^{\pm1},\tau^{\pm1}]$ 上 $\mathcal A=\bigoplus_{n\ge0}R\Gamma(S,\mathcal O_S(nD))$，保留单位、原极阶包含、原乘法和合法底环上的Lax标记。N01仍是旧I04延续；P27–30接受与非单位自治C1–C3完整关闭后的FAIL全部扣除。
本件只问已知文献覆盖到哪一层，不做实际混合乘法、平方商提升、同伦轨道或相对形式性计算；“所读来源未给原接口”不等于全球开放或足够支撑长文。

## 2. 本轮25条新主张查询及渠道限制

下表均为实际提交的不同查询：C1八条、C2九条、C3八条，不把前轮九条首筛查询重新计数。`A184`表示本次调用另设 `domains=[arxiv.org], recency=184`；它是检索约束，不保证返回论文版本真的新于六个月，后续逐项核元数据。项目最近六个月窗口为2026-03-10至2026-09-10；实际只能报告执行时已公开内容。

| 主张／号 | 实际query及额外过滤 |
|---|---|
| C1-Q1 | `site:arxiv.org "q-de Rham" "multiplicative" "comparison" after:2023-12-31 before:2027-01-01` |
| C1-Q2 | `"q-Painlevé" "derived" "anticanonical" "algebra"` |
| C1-Q3 | `site:scholar.google.com "q-de Rham" "Pridham" "multiplication"` |
| C1-Q4 | `site:semanticscholar.org "q-de Rham" "Wagner" "comparison"` |
| C1-Q5 | `"q-de Rham" "comparison" 2026`；A184 |
| C1-Q6 | `"q-de Rham" "Pridham" "multiplicative"` |
| C1-Q7 | `"q-de Rham" "Wagner" 2026`；A184 |
| C1-Q8 | `"q-de Rham" "multiplication" Pridham`；`domains=[scholar.google.com]` |
| C2-Q1 | `site:arxiv.org "q-de Rham" "cyclotomic" "Bockstein" after:2023-12-31 before:2027-01-01` |
| C2-Q2 | `"q-Painlevé" "Lax" "Bockstein" "section"` |
| C2-Q3 | `site:scholar.google.com "q-de Rham" "roots of unity" "multiplication"` |
| C2-Q4 | `site:semanticscholar.org "q-de Rham-Witt" Wagner` |
| C2-Q5 | `"q-de Rham" "Bockstein" 2026`；A184 |
| C2-Q6 | `"q-de Rham" "cyclotomic" "square" 2024 2025 2026` |
| C2-Q7 | `"q-de Rham" "root of unity" "product" Wagner` |
| C2-Q8 | `"q-Painlevé" "Lax" "derived sections"` |
| C2-Q9 | `"q-de Rham-Witt" "Bockstein"`；`domains=[semanticscholar.org]` |
| C3-Q1 | `site:arxiv.org "elliptic" "formality" "derived" after:2026-03-09 before:2026-09-11` |
| C3-Q2 | `"elliptic fibration" "derived pushforward" "algebra" "formal"` |
| C3-Q3 | `site:scholar.google.com "genus one" "A-infinity" "marked" "Polishchuk"` |
| C3-Q4 | `site:semanticscholar.org "Elliptic Cohomology" "Mapping Stacks"` |
| C3-Q5 | `"elliptic" "derived global functions" "formal"`；A184 |
| C3-Q6 | `"genus one" "A-infinity" "moduli" 2024 2025 2026` |
| C3-Q7 | `"elliptic fibration" "relative" "formality" "structure sheaf"` |
| C3-Q8 | `"Equivariant Elliptic Cohomology and Mapping Stacks"`；`domains=[scholar.google.com,semanticscholar.org]` |

另实际做题名解析 `"Meyer" "Wagner" "q-Hodge complexes and refined"`，以及原文 `open/find`，不计入25条。初轮合并回执有输出截断，未把未显示部分冒作已读；使用的候选均另开一手正文。
arXiv、出版社正文及作者官网能提供有效原文；Scholar／Semantic Scholar这里只经公开网页索引尝试，不宣称原生数据库完整覆盖。此前原生入口403／429保持失败，本轮不重试绕过；最后C1-Q8/C2-Q9/C3-Q8组合回执未返回结果。网站限定搜索少量无关／聚合命中只用于定位，不作数学证据；与此任务无关的ML会议目录不冒充数学数据库覆盖。

## 3. 七份核心来源：版本、本人阅读与可扣除内容

以下全部为**整篇PARTIAL**，没有一篇被声称完成全文证明审计。各自摘要／引言及所列定理段已本人读取；主结论只按该版本原文，不拼接不同版本的最强说法。

### S01. Pridham：最贴近原加法型，但比较等级须分清

[J. P. Pridham, *On q-de Rham cohomology via Λ-rings*, Math. Ann. 375 (2019), 425–452][PRI]，官方刊本文本，在线发表于2019-02-05。
实读摘要、引言，Definition1.8、Remark1.10、Proposition1.15及证明、Theorem1.17及证明、Remark1.18；Theorem1.23的条件与所显示模$(q-1)$／首平方陈述。其余证明未全读。
Remark1.10／Proposition1.15给余单纯Λ-ring结构；Theorem1.17明确给的是 $R[q]$-线性准同构zigzag：未décalage qDR的微分为$(q-1)\nabla_q$，作$L\eta_{q-1}$后才是Jackson q-de Rham复形。这既扣除普通加法系数发现，也禁止把定理原句升级为原过滤$E_1$识别。[官方§1.15–1.18][PRI]
对象对齐仍须使用冻结LAND的**相对一变量**模型 $\mathrm{qDR}(B[u]/B)$、$B=\mathbb Z[\tau^{\pm1},v]$ 与指定rank-one Λ结构；$u,du,v$权一，$q,\tau$权零。不能擅换为把$v$也作为相对变量的二变量qDR而多出$dv$；这个模型字典已知，不是原乘法的证明。

### S02. Wagner q-Witt：圆分商乘法及Bockstein已有强定理

[F. Wagner, *q-Witt vectors and q-Hodge complexes*, arXiv:2410.23078v5][WW]，当前元数据核准为2025-10-06，78页。
实读摘要、引言1.1–1.9；§4.8扭曲乘法完整段，§4.16短正合列、§4.17陈述及部分显示证明，§5.1 no-go完整陈述及部分证明。未全读§4比较证明或§5全证明。
§4.8的 $du\,f=\gamma(f)du$ 同时服务q-de Rham／q-Hodge显式模型；Theorem1.7把完成的q-de Rham–Witt复形与 $H^*(q\text{-Hdg}/(q^m-1))$ 识别为交换DGA，微分来自Bockstein。§4.16的提升底环涉及 **$(q^m-1)^2$**，不是自动等于原题任一单独$\Phi_m(q)^2$商。[§4与Theorem1.7][WW]
§5.1排除的是全体光滑代数上兼容指定q-Witt识别／商映射的函子；不排除一个固定qPI族比较。应用到原题之前，整底环、完成、framing及实际商／平方商必须对齐；没有任何源定理把只在商上存在的原Lax截面变成$R_u$全局截面。

### S03. Wagner Habiro：对称幺半下降以过滤pair为输入

[F. Wagner, *q-Hodge complexes over the Habiro ring*, arXiv:2510.04782v2][WH]，2025-10-08，82页。
实读摘要、引言1.1–1.17，包括Definition1.6全部兼容条件、Theorem1.11、1.15及Remark1.17(a–c)；后文构造／Corollary4.16证明未全审。
Theorem1.11的对称幺半因子化从**已携带选定q-Hodge filtration的pair范畴**出发。Theorem1.15在光滑且反演$p\leq\dim$的范围给典范过滤；这不自动保证该选择对所有乘法／高阶相干相容。Remark1.17(c)解释构造乘法、同伦结合及更多相干会要求继续反演小素数，并非证明所有$E_1$模型皆不可能。[Definition1.6、Theorems1.11/1.15、Remark1.17][WH]
因此通用下降机制全部扣除，但不能把q-Hodge过滤改名成原极阶过滤，也不能从对称幺半pair函子跳到原$\mathcal A$已有所需乘法。这里尚未检查原输入能否满足条件，正反结论都未给。

### S04. Wagner ku：条件乘法比较，不是原极阶过滤的代签

[F. Wagner, *q-de Rham cohomology and topological Hochschild homology over ku*, arXiv:2510.06057v1][WKU]，2025-10-07，95页；当前元数据未显示v2。
实读摘要、引言1.1–1.9可见正文；本轮补读§4.18的(A)/(R)、§4.18a的$R_2$，并重核§4.25–4.28定义／陈述。§3.1／3.2所引用球面提升和下降条件、全篇比较证明仍未完整核准。
Theorem1.2的简化范围是quasi-syntomic、2可逆、有球面$E_2$提升；给的是完成的q-Hodge过滤比较。一般§4.27还须指定逐素条件，§4.28在相应选择或$E_n$提升下给$E_{n-1}$-monoidal性。不能只摘“multiplicative”一词而丢掉这些前提。[Theorem1.2与§4.18–4.28][WKU]
这加强C1的标准压力，不解决原所有次数、原极阶、原单位与Lax标记的同步比较；未据本源重定义研究对象为THH。

### S05. Sibilla–Tomasini：单椭圆导出函数确实丢失模参数

[N. Sibilla–P. Tomasini, *Equivariant Elliptic Cohomology and Mapping Stacks*, arXiv:2303.10146v3][ST]，2026-06-01发表版本，56页，关联DOI `10.1016/j.aim.2026.111041`；是本次核到的最近六个月更新，不是2026首次提出单椭圆形式性。
实读摘要、引言可见正文与相关工作，完整§2.3；另定向查§5.10陈述和§6.4相对语境，未审其全证明。
§2.3直接记载特征零域上 $R\Gamma(E,\mathcal O_E)$ 作为cdga形式，与次数0、1各一份基域的上同调等价，故其affinization与圆相同。这已否决仅靠单条无额外数据椭圆导出函数恢复$j$的说法。[§2.3][ST]
但§6.4出现“relative”时仍围绕固定$E$的相对mapping stack，不能据此宣称已证明原变化铅笔的 $Rf_*\mathcal O$ 连同原$s_0,s_1$分次标记形式。N02的这一实际桥接仍只是待核标准短子问题，本席未做证明。

### S06–S07. Lekili–Polishchuk：信息恢复的已知对象是另一self-Ext

[Y. Lekili–A. Polishchuk, *A modular compactification of M₁,n from A∞-structures*, arXiv:1408.0611v3][LP1]，2017-02-28，38页；刊于Crelle755 (2019),151–189。实读摘要、完整引言及Theorems A/B陈述，未读全部§2证明。
它用 $G=\mathcal O_C\oplus\bigoplus_i\mathcal O_{p_i}$ 的self-Ext及高阶运算恢复带标记曲线；光滑互异标记、强非特殊性／振幅条件与允许的gauge等价是对象的一部分。Theorem B对$n=2$排除特征2、$n=1$排除2、3。[引言与Theorem B][LP1]
[同作者, *Arithmetic mirror symmetry for genus 1 curves with n marked points*, arXiv:1601.06141v4][LP2]，2016-10-13，53页；刊于Selecta Math.23 (2017),1851–1907。实读摘要、引言、§1.1定义和Theorem1.1.1及显示证明；其余证明未全读。该定理把有关A∞模空间等价推广到$n\ge3$的整数底环，$n=2$需反演2。[§1.1][LP2]
所以“同样$m_2$而高阶运算不同”“积分属一标记恢复”不能作新发现；然而以上 $R\operatorname{End}(G)$ 不等于原 $\bigoplus_nR\Gamma(S,\mathcal O(nD))$。把两者混同既不能证明本题可恢复$j$，也不能用它反驳S05的单椭圆形式性。

## 4. 新命中／版本压力的有界处理

| 来源与核准版本 | 本人PARTIAL范围 | 本题处理，不作额外原定理 |
|---|---|---|
| Meyer–Wagner, *q-Hodge complexes and refined TC⁻*；[arXiv:2410.23115v4][MWA]为2025-10-08；[作者当前PDF][MWP]首页日期2026-02-05 | arXiv元数据；作者PDF摘要、引言§1.1–1.4正文，含Theorems1.9–1.11陈述 | 当前arXiv说明旧q-Hodge过滤材料已拆为独立论文；不能把2026作者文件称arXiv v5，也不算最近六个月更新。其refined TC／Habiro背景和引言展望不是原$\mathcal A$比较；本件不调用后文证明 |
| Garoufalidis–Wheeler, *Explicit classes in Habiro cohomology*；[arXiv:2505.19885v1][GW]，2025-05-26，PDF首页2025-05-21 | 摘要、引言§1.1、§1.2部分、§1.3及§1.4到Theorems1.5/1.6；未读全14页引言或后续证明 | 已有光滑族（含Legendre椭圆）上由超几何／Picard–Fuchs构造的显式类；此处定义的是$H^n_{\rm naiv}$，与Wagner理论的关系在§1.3仍用期待表述。不能将“椭圆＋q类”视为全新，也不能把这些类当原Lax消费者 |
| Bousseau, *Geometric helices on del Pezzo surfaces from tilting*；[arXiv:2603.22065v2][BOU]，2026-04-17（v1为03-23） | v2摘要、完整引言§1.1–1.3及相关工作；Theorem1.1／Corollary1.2陈述，未全读主证明 | 最近六个月命中有$q$-Painlevé-type seeds及反典范截面环，但陈述针对复del Pezzo上的geometric helices／锥完成的NCCR变异。没有从所读定理取得原$q$DR过滤比较；先读过v1，终态排除依据为复核后的v2，不混用变化措辞 |

上述近邻有实际内容，不能因没有题名级完全命中就忽略；同时不为完成“最近文献数量”将它们充作N01的直接包含定理。作者博士论文搜索命中已识别为学位论文，打开但未读正文，不列作新近核心先例；GHK/Lai–Zhou已在冻结LAND有明确对象边界，本轮不重复扩展镜像树。

## 5. 逐主张扣除、尚未核准的差与反对意见

| 主张 | 最近先例与必须扣除 | 来源核查后仍精确缺少什么 | 不能作出的结论 |
|---|---|---|---|
| N01-C1 | S01的未décalage qDR；S02显式扭曲乘法；S03/S04条件过滤、完成及幺半比较 | 对同一原$\mathcal A$的单位／极阶／全次数过滤$E_1$比较；或在允许整变基与链同伦后成立的真正障碍。还需明确比较到哪一个具体标准模型 | 加法zigzag不是过滤$E_1$定理；手写乘法的一次不相容不是不变量；通用no-go不是固定族否决；“未核准原比较”不等于高新颖性 |
| N01-C2 | S02圆分上同调DGA和Bockstein，S03圆分下降；旧幂基、$s_0$作用、标准Leibniz | 在原准确商及首平方加厚上，对实际存在的Lax截面、原混合运算／提升的同步作用与可见后果；这依赖C1对象级比较 | 不把$(q^m-1)^2$直接替为任意$\Phi_m^2$；不把商截面虚构成全局截面；只写Leibniz或“Habiro”不够计新功 |
| N01-C3 | S05单椭圆函数形式性；S06/S07另一self-Ext对象的标记恢复；冻结旧模参数／加法事实 | 原全分次带$s_0,s_1$对象与变化铅笔之间的信息边界；相对$Rf_*\mathcal O$短标准检查是否已足以关闭此项 | 不能由单纤维形式性推出整族带标记形式性，也不能由LP的对象换名推出原$\mathcal A_t$能辨别$j$；本件没有执行N02证明 |

**来源席结论：** 三项仍是待判问题，标准部分已很厚；本次所读原文没有提供足以直接代签这三个**原标记接口**的陈述。剩余价值只能来自准确原比较／不变量障碍及实际消费者，不能来自术语升级或把标准理论用在同名曲面上。C3应先接受标准短否决检查；若失明仅为短形式性后果，按Phase A只记限制，不另开长文。
这是来源边界，不投HIGH/MEDIUM/LOW、分数或KEEP正式票，也不改变首筛和已失败C1–C3的科学状态。未来至多权总和4／一个首圆分平方商等诊断继续由主控按既定流程决定，本件未执行。

## 6. 验证与交付边界

本席只新增本文件；写后本人全文读回，并只核三个直接本地引用的存在与SHA绑定。没有运行数学诊断、CAS、GPU、实验、论文编译或全树哈希；没有修改锁、接受／失败产物、索引、旧源或建立P31项目。
外部阅读均为上述PARTIAL；arXiv／出版社／作者原文可访问不等于整篇读完。此前Scholar403、Semantic429不绕过；本轮网站索引未命中、初回执截断及误先开Bousseau v1均已如实保留并限定后续用法。主控须亲读本终态后才能将其作为Phase C/D输入。

[CLAIMS]: PAPER31_QPI_POST_CLOSED_SURVIVOR_CLAIMS_PHASE_A_V1_20260910.md
[LAND]: PAPER31_QPI_POST_CLOSED_MULTIPLICATIVE_LANDSCAPE_V1_20260910.md
[QF]: PAPER31_QPI_POST_CLOSED_QUICK_FILTER_N01_N03_V1_20260910.md
[PRI]: https://link.springer.com/article/10.1007/s00208-019-01806-7
[WW]: https://arxiv.org/html/2410.23078v5
[WH]: https://arxiv.org/html/2510.04782v2
[WKU]: https://arxiv.org/html/2510.06057v1
[ST]: https://arxiv.org/html/2303.10146v3
[LP1]: https://arxiv.org/pdf/1408.0611v3
[LP2]: https://arxiv.org/pdf/1601.06141v4
[MWA]: https://arxiv.org/abs/2410.23115
[MWP]: https://ferdinand-wagner.github.io/papers/q-Hodge.pdf
[GW]: https://arxiv.org/pdf/2505.19885
[BOU]: https://arxiv.org/html/2603.22065v2
