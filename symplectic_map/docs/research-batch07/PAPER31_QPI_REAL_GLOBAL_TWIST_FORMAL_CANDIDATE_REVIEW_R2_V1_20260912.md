# Paper31 原全实正则旋转／twist 完整新候选：独立正式 R2

批次标签：20260912；本席审查与冻结于 2026-09-12 UTC。本文仅是一席完整候选正式审查，不是作者修订、论文正文、Route A/B 评价或产物验收。

## 1. 身份、权限与结论

本席为 fresh R2：未参加该候选作者稿、查新或此前有界数学审查；由当前可用 secondary Codex 承担，按任务指定 xhigh 审查配置工作。具体底层模型标识不在本席可独立核验的信息内；不自称 GPT-5.4，不声称跨模型审查。GPT-5.4 Codex MCP 不可用，mcp_threadId = null。本席没有再委派，没有阅读或接收另一正式席评分，也没有与另一席分工拼票。

按指定顺序，本人完整阅读 research-review、proof-writer、novelty-check 三个 SKILL.md，并采用最小完整研究审查路由：独立批判评价、依赖与证明逐项核验、定向一手对照。不启动 ARS 总管线，不添加纯数学任务无关的 ML 实验，不调用外部模型/API。技能默认迭代、通用输出路径等建议服从本任务精确权限；本席只写本报告。

本席结论如下。分数是有证据约束的审稿判断，不是概率或统计置信区间；各门独立，不平均补偿。

| 门 | 本席分数／结果 | 阈值 | 结论 |
|---|---:|---:|---|
| 新意 | 7.2 / 10 | ≥ 7.5 | FAIL |
| 独立价值 | 7.8 / 10 | ≥ 7.5 | PASS |
| 完整证明信心 | 9.3 / 10 | ≥ 9 | PASS |
| 可信完整正文容量 | 自然低／中／高 21.75 / 26.50 / 31.25 页；存在可信 22–30 页正文方案 | 22–30 页 | PASS |
| 本席全部合取 | 新意门未过；其余三门通过 | 四门全过 | FAIL |

这不是重投旧 exact-thickness 候选的双 FAIL；此次科学对象、主 finding 和证明负载均按当前完整候选判断。CD 中的 6.5 谨慎判断作为既有反方材料保留，不是本轮正式票，本席不继承也不要求同分。结论不是“已有完整包含定理”或“没有新结果”，而是当前可证增量与未关闭的强包含风险，尚不足以使本席给予 ≥7.5 的高新意评价。

## 2. 共同输入、读取身份与完整性

唯一共同入口是 [共同清单](PAPER31_QPI_REAL_GLOBAL_TWIST_FORMAL_COMMON_INPUT_MANIFEST_V1_20260912.md)，本人 FULL 读 1–117 行；117 行、13490 bytes、SHA256 605b34e1149e8294526c628f4355e5032738f9280ec2f3ab2753f73b47e1e1bd，与指定身份一致。本席逐一只核验清单中的 33 件本地文件，行数、bytes、SHA256 全部 MATCH；没有递归重扫构建树。

以下 FULL 指本人阅读全文，不是摘要、搜索命中或他席代读；PARTIAL 精确限定为清单指定范围。表中 SHA 为完整 SHA256，尺寸为原文件总行数／bytes，不把 PARTIAL 冒称全文。

### 2.1 本人 23 件 FULL

| ID | 文件 | 行／bytes | SHA256 |
|---|---|---:|---|
| PF0 | PAPER31_QPI_REAL_GLOBAL_TWIST_PREFLIGHT_DISPOSITION_V1_20260912.md | 130 / 11107 | 0923e18bd1286daa421a5656cffe8f4bb31aaa3e1a7ffd2ba8030f0fbcd25ce1 |
| MD | PAPER31_QPI_REAL_GLOBAL_TWIST_MATHEMATICS_DISPOSITION_V1_20260912.md | 135 / 10371 | c3325516b39ad2595863de544f7db577c6a65f72511f379c1f566a8aae8c568b |
| A | PAPER31_QPI_REAL_GLOBAL_TWIST_NOVELTY_PHASE_A_V1_20260912.md | 77 / 5629 | 18076931181e67484cf6d676cf94438d719c1575014ed4e4b5819f388964ff6a |
| G | PAPER31_QPI_REAL_COMPONENT_RETURN_GEOMETRY_V1_20260912.md | 208 / 11847 | f0c92b3d03bc1686deb63877777d36c6297efde779d2fc02f81cde4d86e8a196 |
| B | PAPER31_QPI_REAL_ACNODE_TWIST_BOUND_V1_20260912.md | 144 / 7701 | 9c948e5a649754192e781aac8fdec3c2d313645290dd36686f4b8a8e004eb96d |
| M | PAPER31_QPI_REAL_MIDDLE_ENDPOINT_TWIST_V1_20260912.md | 115 / 6053 | 4b07925048eb416d431d1e924c7d54a46c90c1a9b08708b6647c4430a79860a3 |
| U | PAPER31_QPI_REAL_UPPER_RETURN_FINITE_TWIST_V1_20260912.md | 112 / 5614 | beaff1ed89c8f99b71f241340c5833d74ab1debfebf0c408335d2e4ed3dd5bff |
| I | PAPER31_QPI_REAL_INFINITY_C1_ASYMPTOTICS_V1_20260912.md | 215 / 11115 | a6949cdae36598dd7b6d607e32f172321edeb046ebb08d1fab63dd9fa23191f6 |
| S | PAPER31_QPI_REAL_GLOBAL_TWIST_SYNTHESIS_V1_20260912.md | 133 / 6753 | 63f5fb82d37ecb629482d97ccd629ccc0964bcece65edbfb630caf9cd39a0c24 |
| FRC | PAPER31_QPI_PICARD_FUCHS_FORCING_PROBE_V1_20260912.md | 267 / 10608 | c169efcceb6045c0c69ff1a8d5c53551ba984ce7965491ce5937960c182f4c5b |
| Q | PAPER31_QPI_REAL_GLOBAL_TWIST_SOMOS_QRT_SOURCE_PROBE_V1_20260912.md | 140 / 8737 | 089df2e31231d3bf2288525dd2fd99f7c3a7fda0f01fb98d2fb7543715cb0c44 |
| Z | PAPER31_QPI_REAL_ZERO_LYNESS_SOURCE_BRIDGE_V1_20260912.md | 123 / 7175 | 3c5809411c9979b6d6702dbb867af85fce78dff15fb568fddabc204dbc2d5ceb |
| MA | PAPER31_QPI_REAL_GEOMETRY_TWIST_MATH_REVIEW_V1_20260912.md | 212 / 14963 | e00f5e920b9a66213e22709e3a7379161d311ee2f735473ba597171ab8d305e8 |
| MB | PAPER31_QPI_REAL_OUTER_GLOBAL_MATH_REVIEW_V1_20260912.md | 201 / 14712 | 5e99316e1e20caca644ffe76724d86a62e791e7276e2168bb8527e230f2c5320 |
| QR | PAPER31_QPI_REAL_POSITIVE_QRT_INTERFACE_MATH_REVIEW_V1_20260912.md | 97 / 6141 | 279651002d1ec3dfa6ba7eaae3feaf65a16f7eddf071ad92b93b66cb8ab274aa |
| ZR | PAPER31_QPI_REAL_ZERO_LYNESS_BRIDGE_MATH_REVIEW_V1_20260912.md | 107 / 7140 | e70025868b6dd4321435dc6667456de0c2c70918ffad11fd7c488c7d3a89809d |
| BRIEF | PAPER31_QPI_REAL_GLOBAL_TWIST_CANDIDATE_BRIEF_V1_20260912.md | 283 / 19233 | 642a1d76f81a3619ea04e621507fe07856e560b150fd6ea34d6359509f0243c3 |
| MAP | PAPER31_QPI_REAL_GLOBAL_TWIST_CURRENT_PROOF_MAP_V1_20260912.md | 265 / 22687 | 666bc9b73e7b98a270ed17138cbfa07392ec3e4efa451f088e11d80ab6dbe77e |
| NB | PAPER31_QPI_REAL_GLOBAL_TWIST_NOVELTY_PHASE_B_V1_20260912.md | 213 / 19024 | 059dc1df27a69f5227f449394137ca7ebb4d47e56eb8a41610194a2594b8a521 |
| CD | PAPER31_QPI_REAL_GLOBAL_TWIST_NOVELTY_CD_V1_20260912.md | 208 / 21268 | f87c7c1d4f2e8a9627dfdf33ea4f530f55ee9ed7b1921715cfef1c5584beb1e9 |
| SRC | PAPER31_QPI_REAL_TWIST_STRONG_SOURCE_AUDIT_V1_20260912.md | 159 / 13101 | cf80d3e4e9567eaf15ac302bdafda1e25c3f0dd81501d0edd52ef2706ff51d92 |
| SUP | PAPER31_QPI_REAL_STRONG_CONTAINMENT_SUPPLEMENT_V1_20260912.md | 166 / 13926 | fc5973efb0fe84261aea622d68f425fed1e23d86ab039e6c4b26ac057c7df972 |
| PORT | PAPER31_QPI_REAL_GLOBAL_TWIST_PORTFOLIO_DELTA_V1_20260912.md | 137 / 13708 | 68523a126d01913e2ab82e4280a730db2d3164fdb176f2bf06420428a4e58834 |

以上文件均在 docs/research-batch07/。一次合并读取 BRIEF／MAP 的工具外层输出截断了 MAP 前部；本人随后补读 MAP 1–75 行，全文覆盖已恢复，未以截断结果宣称 FULL。

### 2.2 本人 10 件规定 PARTIAL

| ID | 文件 | 本人实际行范围 | 原文件行／bytes | SHA256 |
|---|---|---|---:|---|
| S02 | papers/30-qpi-vertical-critical-ideals/paper/v4/sections/02-surface-pencil.tex | 1–226；388–437 | 446 / 20456 | 573a521e07117dc43b9291417469fa429701c67d711ec150a578b22c54205f8f |
| S03 | papers/30-qpi-vertical-critical-ideals/paper/v4/sections/03-spectral-jacobian.tex | 1–111 | 438 / 19219 | 38e52e45513c51e9365d9bd0453776d09351fb1ca48b5d86233581112f95434f |
| F30 | PAPER30_QPI_ACTUAL_SINGULAR_FIBRE_ENTRY_V1_20260908.md | 7–26；66–92；128–245；362–416 | 466 / 22170 | 3b7a495b723d9ba45003fe767431c4420053c0b3de6656a2335c3aad01307003 |
| R30 | PAPER30_QPI_RETURN_TRANSLATION_ENTRY_V1_20260908.md | 1–18；54–70；107–160 | 368 / 16747 | 9ee29e426c14334c41c26b1265bd71fe53b232c37949d5ad21aef14550a6851c |
| FIX | PAPER31_QPI_MANIN_FIXED_SCHEME_INTERFACE_PROBE_V1_20260912.md | 30–71；86–139 | 348 / 20304 | 401db0359ad2e05456ff3ec2aa7f93e2ad7fb7136e2f815f131b02a66e762ba7 |
| FXD | PAPER31_QPI_MANIN_PRIMEFIELD_AND_FIXED_SCHEME_DISPOSITION_V1_20260912.md | 1–19；61–75；140–161 | 176 / 11013 | 8527248c907f2b8abc1c84c0b89a5623ffae5d09e5c55877d59f98ca2054522a |
| FMD | PAPER31_QPI_EXACT_LOCAL_THICKNESS_DISPOSITION_V1_20260912.md | 1–34；111–133 | 234 / 13710 | 5340f77faa1354b1239240e3d7ba7068ae32e752e6d4550e32b2f243ea08bc99 |
| RG | PAPER31_QPI_GOOD_CONTACT_INDEPENDENT_V1_20260912.md | 1–59；72–139 | 331 / 17843 | 7f7d6f659b69af334a32dca24ae4335ff98965a4de01f4643a56032aeea6b0e1 |
| OB | PAPER31_QPI_EXACT_THICKNESS_CANDIDATE_BRIEF_V1_20260912.md | 130–139；210–248 | 360 / 24719 | 1d00acccbd1056f361ac2736cbe9c035c965a566167bf6f8b9efdc4da1ba01dd |
| OS | PAPER31_QPI_POST_EXACT_SOURCE_AND_SCOPE_V1_20260912.md | 49–82 | 179 / 16523 | 737b52c9217187897eaef5e12bbd63d6907282464ba458b94d4d0be79cf41426 |

除 S02、S03 已给仓库相对路径外，本表文件仍在 docs/research-batch07/。规定范围之外未被假定已读；其不相关旧结论也未计入新证明。

### 2.3 流程与共同版式附单

本人 FULL 读 docs/WORKFLOW.md（39 行／4901 bytes）及上述三个技能原文。research-review 为 106 行／4501 bytes，proof-writer 为 223 行／7594 bytes，novelty-check 为 86 行／3015 bytes。

另本人 FULL 读 [共同版式澄清](PAPER31_QPI_REAL_FORMAL_LAYOUT_CLARIFICATION_V1_20260912.md)，17 行／1621 bytes，SHA256 4676978aebcc96406cc0d2cf0d21a0d4aef1e5a7a39a2b911a1b3b0640ad7b28。仅为核对既有版式，定位阅读旧 PAPER31_QPI_EXACT_THICKNESS_REVIEW_INPUT_MANIFEST_V1_20260912.md 第 164–181 行及 PAPER31_QPI_EXACT_THICKNESS_FORMAL_CANDIDATE_DISPOSITION_V1_20260912.md 第 68 行；未读取旧完整审查包、未把其旧页数票移植到当前候选。

版式为匿名英文、单栏、11pt article、letter、四边 1 inch、普通行距和段落。正文包含摘要、引言、结论与全部对象特有的必要证明；参考文献另起页、另计。中值落窗不是额外独立门槛，低／中／高也不是实际排版测量或严格界。

## 3. 定向一手读取及访问失败

本人执行的是共同清单 §4 的同样十项范围，不是重新查新。没有新建 search query、下载 PDF、使用 CAS 或数值实验，也没有绕过付费或被拒入口。网页/PDF 经公开浏览工具直接阅读，与下载到本地不同。下表“本人已读”只表示本次实际返回内容；既有 SRC/SUP 的来源读取不冒充本席读取。

| 一手来源及固定入口 | 本人实际读取 | 对本次判断的用途与保留 |
|---|---|---|
| [Bastien–Rogalski 2005](https://link.springer.com/article/10.1155/ADE.2005.227) | 公开落地页身份、摘要及参数族；未进入全文 | 摘要给出非负参数二阶 QRT 族和正象限不变圆上的旋转。Q 的精确代入已把本候选下外分支放入该族。§§6–9 未读，不能排除更强旋转结论或断言完整包含。 |
| [Cima–Gasull–Mañosa 2008](https://arxiv.org/pdf/math/0702121) | 摘要、完整引言、Theorems 1–2 完整陈述和对应圆分量说明；PDF 抽取行 0–256 | 兼容向量场、周期流的时间比及有限分量返回的基础机制是标准已有工具；未将仅有摘要当成定理范围。其一般框架本身没有给当前五行表。 |
| [Cima–Gasull–Mañosa 2012](https://arxiv.org/pdf/0912.5031) | §§1–2 映射、积分及 Theorem 3；§5 零参数及 5/8 段、逆时针约定、Theorem 3 完整证明；p.18 零参数分类条目 | 正参数邻域的旋转数非单调性有证明，不能算本候选首次发现。零参数 5/8 端值与分类线索也先在。Theorem 3 的三能量轨道界只推出局部非单调，不是唯一非退化极大或全参数分类；p.18 文字方向问题保留。 |
| [Bastien–Mañosa–Rogalski 2013](https://arxiv.org/pdf/1201.1027) | 摘要、完整 §1；Proposition 13；式 (34)–(37)；Lemma 14 完整陈述及相邻对数主项推导；Proposition 24 陈述 | 正参数区域、旋转方向互补及完全／不完全椭圆积分比已有。这里读到的主对数结论不能直接代替 I 的 C1 余项与两个精确 Wronskian 常数；未宣称全文无更强结果。 |
| [Bastien–Mañosa–Rogalski 2016 指定稿](https://ddd.uab.cat/pub/caplli/2016/221036/BasManRog2016.Preprint.pdf) | 一次返回 400，说明为 Timeout fetching；指定 pp.2–5 本人未读 | 不重试、不换入口。SUP 关于正参数假设、Theorems 1–2／Proposition 1／Corollary 1 及零参数退化式的记载只能标为继承材料，不能转成本人一手确认。 |
| [Gasull–Mañosa–Xarles](https://arxiv.org/pdf/1004.5511) | Theorem 3、§2.1 群律转换与 §2.2 全部；抽取行 177–187、244–418 | 标点椭圆曲线到 Lyness/Tate 正规形是旧工具；原 h=1 的四阶点例外以及 h=2 的局部缩放边界必须保留。这里不是原实轨道全域同一性的替代证明。 |
| [McMillan III v3](https://arxiv.org/html/2410.10380v3)；[版本记录](https://arxiv.org/abs/2410.10380) | 摘要、§II 两种正规化、§V 全部；核版本记录 | 精确椭圆积分旋转表达和局部 detuning 不是方法新意。v1 为 2024-10-14，v3 为 2026-03-23，正式文章为 Nonlinear Dynamics 114, 635 (2026)，DOI 10.1007/s11071-026-12509-5；HTML 显示日期不当作首次公开日。未证其家族完全包含本模型。 |
| [Bastien–Rogalski 2020](https://link.springer.com/article/10.1007/s12346-020-00393-2) | 摘要及页面公开的 Appendices 1–3 全文；主文未读 | 可核对其特殊 QRT 曲线、有限周期和圆几何，不能据附录排除主文或其他参数族对当前结论的覆盖；未尝试受限主文。 |
| [Beukers–Cushman 1998](https://research-portal.uu.nl/en/publications/zeemans-monotonicity-conjecture/) | 门户可见元数据全文；本次没有呈现科学摘要或定理正文 | 可确认作者、题名、Journal of Differential Equations 143、页 191–200 和年份；参数、实分支、方向和证明边界未核。没有重试既有 403／406／付费路径。 |
| [Duistermaat 指定目录](https://toc.library.ethz.ch/objects/pdf/e01_978-1-4419-7116-6_01.pdf) | 一次 Internal Error，无 HTTP 状态码；本人未读成功 | SRC 的三页目录读取仅为继承身份。§8.2 pp.384–390、§8.4 pp.395–399、§8.5 pp.400–404、§11.4 pp.518–545 正文仍未读；不得把目录当成正文排除证据。 |

本席把两个本次指定入口失败及时报告主控，没有自扩共同包。没有出现需补入新科学材料的新增来源或真正未供给的证明依赖。因此失败不阻断本地证明检查，却降低强包含排除的可完成程度。BR 2005 强段、BC、Duistermaat 的保留不是从风险清单删除、也不是声称已证包含。

## 4. 审查对象与唯一主 finding

固定 T>0，原映射为
\[
 F_T(x,y)=\left(\frac{T}{x-y},\frac{x}{y}\right),\qquad
 h=-x+y+\frac{x}{y}-\frac{T}{x}.
\]
对象不是正象限辅助图的单一椭圆圆周，而是八次吹起给出的原 U=S\setminus D 上全部有限正则实纤维；四条保留末端仿射线必须一起处理。其 proper 椭圆模型是
\[
 E_h:\ v^2+huv-Tv=u^3-Tu^2,\quad O,\quad P=(0,T),
\]
且原一步映射为 +P。设 Y=v+(hu-T)/2，则
\[
Y^2=f_h(u)=u^3-Tu^2+\frac{(hu-T)^2}{4},\qquad \omega=\frac{du}{2Y}.
\]
本文的旋转方向由 \(\omega\) 固定，并在各能量区间采用候选指定的连续 lift，不能任意取补数。

令 T=w^3(w-1)，其两个实解 w_-<0、w_+>1，对应 h_\pm=w_\pm(3-2w_\pm)。有 h_-<h_+<1。低区 L=(-∞,h_-) 有两个圆且 P 在单位分量，逐圆最小返回为 F；中区 C=(h_-,h_+) 只有一个圆，返回为 F；高区 R=(h_+,∞) 的 P 在另一分量，F 交换两个圆，最小逐圆返回为 F²。

C1 是唯一主 finding：对每个 T>0，给出原全部正则实纤维的旋转数对 h 的严格 twist 符号与内部驻点完整分类。

| 参数 | 低区 \(\rho_-\) | 中区 \(\rho_0\) | 高区最小返回 \(\rho_+\) |
|---|---|---|---|
| 0<T<3/16 | 严增 | 先增后减 | 严增 |
| T=3/16 | 严增 | 严减 | 严增 |
| 3/16<T<1 | 先增后减 | 严减 | 严增 |
| T=1 | 严减 | 严减 | 严增 |
| T>1 | 严减 | 严减 | 先增后减 |

每一“先增后减”恰有一个内部驻能量，且为简单、非退化极大值；没有其它驻点。按能量而非按两个圆重复计数。T=3/16 的 h_-=-2 上 persistent smooth circle 的极大是奇异纤维中的边界现象，不计入正则内部。

C2 是上述结果的端值、旋转像、最大值阈值及积分刻画；C3 是固定 T 的可微边界、精确 Wronskian 常数与全局符号闭合机制。它们分别是 C1 的消费者与证明支撑，不再包装为两个同等独立大发现。原模型返回、方向和 Q/Z 精确源桥另作为范围及优先权接口保留，不把源桥误称为 C3。全 N 周期／固定方案、节点全轨道分类、非自治扩展均不被消费；既有算术或谱项目也不借入本候选的价值或页数。

## 5. 本席完整证明检查

此节是本人对实际依赖链的检查记录。MA、MB、QR、ZR 的接受结论作为历史证据阅读，不机械重开旧验收；但本席对当前完整结论所需的几何、forcing、移动端点和 C1 渐近作了独立实际核查，不从“已有 PASS”推导 9.3。

### 5.1 原模型、整个实纤维与分量返回

证据定位：S02 1–226、388–437；S03 1–111；F30 7–26、66–92、128–245、362–416；R30 1–18、54–70、107–160；G 的几何及全纤维延拓步骤；FIX／FXD 的指定接口范围。

本人核对原八中心与 proper pencil、去除 D 后仍保留的四末端线。F30 的整数 Picard 正交格论证在此只需 r=1 情形：正整数的 \(\sum m_j\ell_j=1\) 排除多分量及非约化；无需把一般 r 的法丛故事拖入此正文。有限光滑纤维全部留在 U，不能把有理图的分母零点删成漏点轨道。

有理同构为
\[
u=T/y,\quad v=Tx(y-1)/y^2,\qquad
x=\frac{Tu}{T-hu-v},\quad y=T/u.
\]
本人检查其定义、模型方程及群律一步 +P 的一致性。G 使用每条正则实纤维上的光滑射影曲线延拓和分离性，将稠密开集等式延到整个纤维；所以无需把 FIX／FXD 的正特征接口不加说明地照搬为实数定理。四末端点为 -2P、-P、O、P，正则情形下彼此不同；低区都在单位分量，高区两点各在一个分量。

判别式 \(\delta=h^4-h^3-8Th^2+36Th+16T^2-27T\) 的两个实零点由 w 参数给出，\(\delta'(h(w))=w^2(4w-3)^3\neq0\)。完成平方后的根符号确定三个区间的圆数及 P 分量：低区三根负，中区一实根，高区 \(r_1<0<r_2<r_3\)。这也解释高区为什么必须用 F²，不能把辅助系统两个交替更新错当原 F²。

这里未发现全域漏点或返回次数缺口；“已知 QRT”不能替代这一原模型覆盖证明。

### 5.2 原 forcing 与所有移动端点项

证据定位：FRC 全文 1–267，当前证明消费其中特征零 Steps 1–2；B、U 的算子及 Wronskian 段。其余正特征材料虽已 FULL 读，不拿来增益新意或厚度。

令 \(s=h^2-4T,\ X=u+s/12\)，短式为 \(Y^2=f(X,h)=X^3+aX+b\)，本小节 \(f_h\) 专指固定 X 的偏导，不是 §4 以 h 作下标的原三次多项式；其中
\[
a=-\frac{s^2+24hT}{48},\qquad b=\frac{s^3+36hTs+216T^2}{864}.
\]
本人检查原多项式恒等式与两个有理原函数，而不只看最终 RHS：
\[
\alpha=-\frac{\delta'}{12\delta},\quad \beta=-\frac{q}{\delta},\quad
q=8h-9,\quad \gamma=\frac{a\beta}{3},\quad
\kappa=\frac{8}{q}-\frac{\delta'}{\delta},
\]
\[
r_0=2\alpha X-2\beta X^2-\frac{4a\beta}{3},\quad
r_1=2\alpha X^2+\frac{2a\beta X}{3}+2b\beta,\quad R_j=\frac{r_j}{2Y}.
\]
关键消去 \(r_1-Xr_0=2\beta(X^3+aX+b)\) 给 \(R_1-XR_0=\beta Y\)。取 \(V=\alpha'+\alpha^2+\beta\gamma-\alpha\kappa\)，得到
\[
\mathcal L=D_h^2-\kappa D_h-V,\qquad
-V=\frac{8h^3-18h^2+9h-12T}{q\delta}.
\]
在 O 的局部参数 t=X^{-1/2} 下，R0 与 R1 各自有极项；不能逐个扔掉。组合
\[
Q=(D_h+\alpha-\kappa)R_0+\beta R_1
 =\frac{2VX-\beta a'}{2Y}-\frac{r_0f_h}{4Y^3}
\]
的极项因 \(-\beta'+\kappa\beta=0\) 消去，且常数项为零，故 Q(O)=0。

移动端点 P 在短坐标中满足 \(X_P'=h/6,\ Y_P=T/2\)，而固定 X 的偏导为 \(f_X(P)=-Th/2,\ f_h(P)=Th^2/12\)。即使沿 P 的总导数 \(Y_P'=0\)，也不能误置该偏导为零。完整 Leibniz 边界项为
\[
\frac{X_P''-\kappa X_P'}{2Y_P}
-\frac{2X_P'f_h(P)+(X_P')^2f_X(P)}{4Y_P^3}
=-\frac{h^3}{36T^2}+\frac{1-\kappa h}{6T}.
\]
它与 Q(P) 的对应项抵消后，留下
\[
\mathcal L I_P=-\frac{H}{q\delta},\quad
\mathcal L\Omega=0,\qquad H=32T+3h .
\]
本人手工检查消去结构及端点代入；没有用 CAS 输出替代证明。FRC 所引一般方法仅为背景，当前特例的恒等式和端点论证已经在包内，不缺外部未供给引理。

### 5.3 acnode 锚点与中区端值

证据定位：B 的 persistent circle 参数化、锚点和符号积分；M 的两端讨论；G 的节点因式分解。

对于 w=w_-，奇异三次为 \((u-a)^2(u-b)\)，其中 \(a=w^2(w-1)<b=-w^2/4<0\)。persistent circle 可用 \(u=r(h)+s^2,\ Y=s\sqrt{g(h,s)}\) 参数化，\(s\in\mathbb{RP}^1\)，\(\omega=ds/\sqrt g\)。无穷端用 1/s 坐标可正常延拓；路径移动不是未经说明的奇异积分。故相关周期和短 Abel 积分跨该 h 解析，且 \(\Omega_*>0\)。

在低／中区置 \(J=\delta\Omega^2\rho'/q\)，上面的非齐次方程给
\[
J'=-\frac{H\Omega}{q^2},\qquad J(h_-)=0.
\]
\(H(h_-)=w_-(2w_-+1)(4w_--3)^2\) 导出 3/16。导数符号积分给驻点上界，而不是直接保证驻点存在；M 另外利用右端 nodal 周期发散、短积分有限及两端旋转值，补出中区小 T 的实际极大存在。这样“至多一个”到“恰一个”的逻辑已经闭合。

acnode 端值为
\[
\theta(T)=\frac12+\frac1\pi\arctan\frac1{\sqrt{3-4w_-}}\in(1/2,2/3).
\]
另一节点 w_+ 的周期发散可由非负积分及 Fatou 判断，原 O–P 短弧远离节点，故中区右端为 1/2。T=3/16 在奇异能量的边界极大与正则驻点计数已严格区分。

### 5.4 高区的实际 2P、h=1 和 q=0

证据定位：U 全文；G 的真实高区分量；M、I 的相应边界；S 的综合符号步骤。

2P 在原坐标为 (T,0)，完成平方后 \(Y=T(h-1)/2\)。高区弧端
\[
s_2=\frac{T(h-1)}{2\sqrt{(T-r_1)(T-r_2)}}
\]
在 h=1 解析穿过零，而原 \(I_{2P}\) 应沿指定实圆从 \(-\infty\) 积到 s2。上节点极限中 s2<0，离节点参数零有距离，故该积分有有限极限，周期发散，\(\rho_+(h_++ )=0\)。不能把中区的实 P 积分直接倍乘作为高区实路径；U 通过复 Abel lift 相差固定整数周期说明 forcing 倍为 \(-2H/(q\delta)\)，随后回到实际 2P 实路径，逻辑合格。

高区令 \(K=\delta\Omega^2\rho_+'\)。其解析关系
\[
qK'-8K=-2H\Omega
\]
在 q=0 给 \(K=H\Omega/4>0\)，因此
\(\rho_+'(9/8)=H/(4\delta\Omega)>0\)。表观算子奇点不是动力学异常点。h=1 为正则四阶点且 \(\rho_+(1)=1/2\)，也未被误删。

在 q 两侧，J'=−2HΩ/q²<0；左侧 J 在 q→0− 趋于 −∞，右侧趋于 +∞。结合左端旋转为零和正 lift，可排除左侧驻点；右侧至多一个严格极大。最终是否存在由正无穷 C1 常数决定，而不是由图形猜测。

### 5.5 无穷端：完整 C1 余项而非形式微分

证据定位：I 全文 1–215，尤其根的隐函数展开、完全积分的分割估计、不完全积分两参数误差、链式求导与最后 Wronskian 极限。本人没有以摘要或单行渐近式代替本段。

令 \(\varepsilon=1/|h|,\ \sigma=\operatorname{sgn}h,\ \ell=\log(1/\varepsilon),\ c=\log T\)，则 \(\partial_h=-\sigma\varepsilon^2\partial_\varepsilon\)。把 \(u=\sigma T\varepsilon+\varepsilon^2z\) 代入，得到
\[
\frac{f_h(u)}{\varepsilon^2}
=\frac{z^2}{4}-T^3+\sigma\varepsilon(T^3-2T^2z)
+\varepsilon^2(3T^2z-Tz^2)+3\sigma T\varepsilon^3z^2+\varepsilon^4z^3 .
\]
两根由简单零点 \(z=\pm2T^{3/2}\) 解析延伸。于是
\[
D=r_3-r_1=(4\varepsilon^2)^{-1}(1+O_{C^1}(\varepsilon^2)),\quad
d=r_3-r_2=4T^{3/2}\varepsilon^2(1+O_{C^1}(\varepsilon)),\quad
k=\sqrt{d/D}=4T^{3/4}\varepsilon^2(1+O_{C^1}(\varepsilon)).
\]
完全周期 \(\Omega=2K_c(k)/\sqrt D\)。证明通过减去 \(\operatorname{arsinh}(1/k)\) 并在 (0,k)、(k,1)、(1,∞) 分割积分，既得到 \(K_c(k)=\log(4/k)+O(k^2\log(1/k))\)，也控制其导数。此处确实有余项导数估计，不是擅自微分 o(1)。

不完全弧用统一公式
\[
A=\frac1{2\sqrt D}\int_0^B\frac{(1+t/D)^{-1/2}}{\sqrt{t(t+d)}}\,dt
\]
处理，其中 \(B_-=T\varepsilon(1+O_{C^1}(\varepsilon))\)，\(B_+=T(1+O_{C^1}(\varepsilon))\)。令 \(\eta=d/B,\ \zeta=B/D\)，误差 E 满足
\[
|E|+|\eta E_\eta|+|\zeta E_\zeta|\le C\zeta .
\]
配合两参数有界对数导数，这控制了原移动端点整条路径的 C1 误差，而不只是固定 B 的积分。

最终
\[
\Omega=\varepsilon(8\ell-3c+R_\Omega),\quad
A_-=\varepsilon(\ell-c/2+R_-),\quad
A_+=\varepsilon(2\ell-c/2+R_+),
\]
各余项满足 \(|R|+|\varepsilon R'|\le C_T\varepsilon\)，相应无穷端的真实 lift 均为 \(\rho=1/2+A/\Omega\)。若 a_- =1、a_+=2，主 Wronskian 为
\[
\varepsilon(3a_\pm-4)c+O_T(\varepsilon^2\ell).
\]
乘以正确的 \(\partial_h\) 符号及 \(\delta/q=\sigma/(8\varepsilon^3)(1+O_T(\varepsilon))\)，得到
\[
\lim_{h\to-\infty}J_-=\frac{\log T}{8},\qquad
\lim_{h\to+\infty}J_+=-\frac{\log T}{4}.
\]
本人核对了常数、方向与两个 a 值。T=1 在估计内，没有除以 log T；两端零常数再与 J 严格单调结合，足以给严格符号，不需要另猜下一阶系数。固定 T 的 C1 控制已经满足逐 T 定理，不要求候选未声明的 T 一致渐近。

### 5.6 全局综合与 C2

证据定位：S 全文，结合上述 B／M／U／I。H 的唯一零点、q 的表观奇点和两端 Wronskian 常数共同决定 C1 五行表；各驻点都落在 J' 非零处，故 \(\rho''<0\)，不是可能退化的平台。

端值依次为 L：(5/8, θ)，C：(θ, 1/2)，R：(0, 3/4)。有内部极大时旋转像的上端为包含的极大值，否则两端为开端；低区两端大小交换发生在 \(T=(1+\sqrt2)/4\)，此常数不是 twist 相变阈值。不得把端值大小交换错译成新驻点诞生。

对低／中内部极大，非锚点根满足
\[
\int_{h_-}^{h_m}\frac{H(s)\Omega(s)}{q(s)^2}\,ds=0.
\]
对 T>1 的高区极大，\(h_m>9/8\) 且
\[
\int_{h_m}^{\infty}\frac{2H(s)\Omega(s)}{q(s)^2}\,ds=\frac{\log T}{4}.
\]
这些是唯一性的有效刻画，不是未经证明的闭式阈值。旋转像、范围端点和阈值消费 C1 与端值证明，不另计主发现。

### 5.7 Q／Z 已证明的精确同一性

证据定位：Q、Z 全文，QR、ZR 全文；GMX 与 CGM 的指定一手范围。本人确认该身份桥不是剩余缺项。

在原 x>0、y<0 上置 \(D(x,y)=(p,q)=(-x/y,-y)\)，则
\[
H_T(p,q)=\left(\frac{T}{qp(p+1)},p\right),\quad
G=pq+p+q+\frac{T}{pq}=-h .
\]
正象限能量 proper，唯一极小点 p=q=c 由 T=c³(c+1) 决定，正则能量为一条紧圆。这给原低区无末端圆的整个覆盖，不是仅有局部有理公式。

设 \(\lambda=T^{1/3}\)，再置 \((a,b)=(\lambda/p,\lambda/q)\)，映射为
\[
\left(\frac{a+\lambda}{ba^2},a\right),\qquad
G=\lambda\left(ab+\frac1a+\frac1b+\frac{\lambda}{ab}\right).
\]
故 BR 2005 的两个规范参数代表 \((T,0,0,1)\) 与 \((\lambda,1,0,0)\) 都与该分支精确相连。这是对新意的实质扣除，不是弱类比。

\(\Psi(a,b)=(ab,a)\) 把它变成 \(L_0\circ L_\lambda\)，组合 \(\Phi(x,y)=(\lambda^2/x,-\lambda y/x)\)，能量 E=-h。原 F 一步等于两次交替 Lyness 更新组成的一次映射，不是原 F²。正象限兼容场 \(pq(-G_q,G_p)\) 逆时针，但 \(\omega(Z)=-1\)；双倒数 Jacobian 为正，Psi 的 Jacobian 为 -a，所以原 \(\omega\) 的方向经最终桥恰与 CGM 逆时针约定相同，得到
\[
\rho_{\rm CGM}(E)=\rho_-(-E),
\]
没有取补数，也没有倍数。参数交换的共轭还保持能量和方向。

因此 CGM 的零参数边界与当前低区结论确是同一对象的比较。p.18 “decreasing” 文字与本桥及旧边界线索的冲突需要保持可见；不能擅改原文，也不把纠正这一个文字方向当成高新意来源。上述身份已在包内完成，不能再以“先证明 Q/Z 共轭”作为阻断性建议。

### 5.8 完整证明信心判断

本席未发现必须补充新数学命题才能得到当前完整 C1–C3 的硬缺口。高区实路径、表观奇点、两个极限常数、T=1 严格性及真实原 U 的覆盖都经实际检查。9.3 / 10，PASS。

剩余工作主要是将分散但已闭合的证明组织为自足正文，保持分支与偏导记号不混用；它不等于新增证明任务。9.3 而非 10 反映人工书面检查仍可能遗漏代数或转写错误，并非把访问受限文献转嫁成证明不可信。未声称形式化验证、机器定理检查、试排或数值验证已经完成。

## 6. 新意与独立价值的分开判断

### 6.1 已有、确有增量与未排清包含

应扣除的已有部分是实质性的：正 QRT／Somos 型原分支、精确椭圆积分旋转表达、兼容流时间比、Lyness 归一化、非单调旋转现象、零参数 5/8 线索都已在已读的一手范围或本地已证明源桥中。内部组合账本还表明八吹起、群律翻译、原 forcing 和 3/16 锚点不是此次新候选首创。把它们全部重新命名后计为新 finding 不成立。

确有实质增量的是：把原全部正则实纤维而非仅正圆纳入统一定理；明确 F 与 F² 的最小返回；以正确方向给出所有 T>0 的严格五区参数表；得到唯一性和非退化性；关闭 T=1 与高区 q=0；用可微余项给两个精确无穷端 Wronskian 常数。这比一个孤立零参数例子或图形上的非单调观察明显更强。本席未在已读来源范围内找到直接给出整套 C1 的定理。

但“尚未找到整套定理”不等于优先权已成立。下外分支已精确落入最贴近的旧族，BR 2005 的强章节未读；BC 及 Duistermaat 强范围未核。高区和中区的新增覆盖也大量使用经典实椭圆曲线与同一旋转积分框架，不能仅因原坐标不同而推出高方法新意。McMillan 的现有精确旋转技术进一步压低方法层面的独特性，但本席没有反向宣称它已完整包含原模型。

### 6.2 新意 7.2：FAIL 的具体原因

本席把 C1 视为中上强度的特定经典系统全局分类增量，而非微小计算补丁；然而其最醒目的低区现象、源家族和大量关键工具均须扣除，其余主要是同一可积机制下的精确全域闭合。就当前可证明的新颖内容而言，达到明确专门定理的水平，但尚不足以让我确认达到 ≥7.5 的高新意门槛。

强源未读是额外不确定性，不是唯一扣分规则：即使暂假设未读段没有逐字完整 C1，也不能把标准方法和已知非单调现象恢复为原创分值。反过来，未读也不允许宣告候选已被前人完全包含。此区分是本席与 CD 6.5 的独立性所在：我认可目前完整候选相较保守下界有明确增量，给 7.2；仍不把增量自动抬到通过。

C2 的旋转像与极值条件主要是 C1 的解释性后果；C3 的 C1 可微控制和精确常数是 C1 的实质证明支撑，应计其增量但不能再拆作同等独立主 finding 叠加评分。Q/Z 精确桥另用于范围和优先权校正。后续若获统一授权并读到强段，可改变包含判断；本报告不要求作者以重包装、加案例或迎合性措辞换分。

### 6.3 价值 7.8：PASS 的具体原因

价值与优先权不相同。对实际研究原映射的人，当前定理一次性回答了全部正则实圆的返回次数、旋转方向、频率随能量变化、twist 退化个数及非退化性，并处理两个参数边界。这使原模型不再只能借正象限辅助系统推测其它实分量；可作为以后研究非退化旋转区、局部扰动条件或共振位置的准确输入。

其价值上限仍受系统专属性约束：没有在此证明新的 KAM 结论、全周期计数、节点所有轨道或非自治动力学，也不把这些潜在应用当成既得产出。尽管新意未过，本席认为完整分类本身足以达到独立价值 7.8，而不是必须附属于旧算术 thickness 论文才能成立。

## 7. 完整正文自然容量

评价对象是允许版式下的完整英文数学正文，不是当前 Markdown 行数、审查账本字数或 LaTeX 实测。以下区分新数学负载、必要旧证明与标准技术；交叉使用的证明只写一次。没有任何必要特例证明外移到附件，也没有通过放大字号、行距或冗长文献史凑页。

| 模块 | 新／必要旧／标准区分与必须留正文的内容 | 低 | 中 | 高 |
|---|---|---:|---:|---:|
| 1. 摘要、问题、完整主定理、文献定位 | 呈现负载；C1 唯一主 finding，C2/C3 附属，不算新证明 | 1.75 | 2.50 | 3.00 |
| 2. 原曲面、八中心、proper pencil、有限纤维完整性 | 必要旧证明；足够的中心与交数计算、r=1 不可约约化及 U 覆盖；不引入无关一般 r 分支 | 3.50 | 4.25 | 5.00 |
| 3. 原映射、+P、四末端及整纤维延拓 | 必要旧证明加特例接口；不是仅列双有理公式 | 1.75 | 2.00 | 2.25 |
| 4. 实坏值、根符号、方向与最小返回 | 新应用加标准实椭圆几何；完整三能量区间 | 2.00 | 2.50 | 3.00 |
| 5. Gauss–Manin、PF、O 与 P 的完整端点消去 | 必要旧特例证明加标准方法；保留两个原函数、局部展开及偏导/总导数区别 | 2.75 | 3.25 | 3.75 |
| 6. acnode 锚点及中区两端、存在性 | 新的完整组合证明；共享圆参数只证明一次 | 2.00 | 2.50 | 3.00 |
| 7. 高区 2P 实路径、h=1、q=0 | 新负载；倍 forcing 与实际实积分分开说明 | 1.50 | 1.75 | 2.25 |
| 8. 正负无穷的 C1 渐近 | 新特例证明加标准椭圆积分估计；根展开、分割估计、移动 B、导数误差与两个常数全部保留 | 3.50 | 4.00 | 4.75 |
| 9. 全局符号综合、唯一性、旋转像与极值条件 | 新主结论及附属 C2；不重复端点证明 | 1.50 | 1.75 | 2.00 |
| 10. Q/Z 精确源桥与边界定位 | 必要身份校正，不是新方法；全圆覆盖、方向与一步数均保留 | 1.25 | 1.50 | 1.75 |
| 11. 结论及明确范围边界 | 呈现负载；不追加未来工作的证明外负载 | 0.25 | 0.50 | 0.50 |
| 算术总计 | 逐列相加；不含另起页参考文献 | 21.75 | 26.50 | 31.25 |

低值是紧凑但完整表达的自然预测，不是保证能压到 21.75；高值包括更舒展的坐标解释及估计细节，也不是必需下界。中值 26.50 的可信性来自各模块实际证明负载：模块 2、3、5 的原模型和 forcing 必要旧证明中值合计 9.50 页，实分支、端点和 C1 控制等新负载也均在正文；不能靠“请参阅内部 probe”省掉。

存在可信的 22–30 页完整写法，故本席容量 PASS。中值恰在窗内只是这张表的结果，不是新附加门槛。高预测 31.25 表示真实的超窗风险：若把原旧证明全盘复制、正特征算术或强源审查账本写成长节，就会超过上限；这些本来不属于必要证明，不能计入正文容量证据。低预测稍低于 22 也不能靠无关内容填充；应按实际数学表述选择自然精度。

本席没有试排、编译、生成 PDF 或根据结果调页数。此 PASS 是可信完整正文容量判断，不是已存在合格 22–30 页产物的断言；也不继承 Paper30 的 22–40 页例外。

## 8. 硬问题、剩余风险与有限建议

硬问题 H1（新意门）：当前完整分类确有增量，但在源族与主要方法扣除后，本席不认为已经达到 ≥7.5；最接近的强源范围尚未关闭包含风险。本报告因此不能给四门合取通过。它不是已发现数学反例，也不是要求先完成全 N 或非自治问题。

风险 R1（来源）：BR 2005 强段、BC、Duistermaat 仍保留未读身份；本次 BMR2016、目录入口失败只能如实记录。若之后允许补强，应由主控向两席统一供给目标原文，逐一定理比较参数、实分量、方向、严格性与唯一非退化性，不能让一席独自扩包后改变评分。本文不执行该扩张。

风险 R2（正文转写）：最容易损坏已闭合证明的地方是把高区的复 Abel 倍数关系当成实 P 路径、把 \(Y_P'=0\) 当成 \(f_h(P)=0\)、遗漏 q=0 的解析关系，以及只保留无穷端主项不保留 C1 误差。建议将这些四处作为以后正文自检的明确检查点；不要求新增结论。

风险 R3（主张强度）：应写“当前原全实正则分类”及可核实的精确增量，不写“首次发现非单调旋转”“新的椭圆积分方法”或“所有前作不适用”。Q/Z 已证明，必须同时作为正确接口和新意扣除保留。

风险 R4（容量）：必须把对象特有的必要旧证明写入正文，但不把正特征、一般 r 或审查过程伪装成数学厚度。参考文献外计只适用于文献表，不适用于把关键证明挪到参考资料。

以上建议有限且不构成自动修订授权。本席没有改共同输入、批次、锁、稿件、PDF 或任何旧接受产物，也没有发布或启动后续流程。

## 9. 本席最终处置与冻结声明

最终独立正式票：新意 7.2 FAIL；价值 7.8 PASS；完整证明信心 9.3 PASS；可信 22–30 页完整正文容量 PASS；全部合取 FAIL。

新意失败不抹掉当前证明闭合、精确 Q/Z 身份或分类的实际价值；证明通过也不替代优先权和论文容量判断。C1 是唯一主 finding，C2/C3 依附；范围外全 N、节点全轨道、非自治均不消费。旧候选 FAIL、CD 6.5、既有数学接受与本席正式票各有独立身份，均未删除、伪装或机械重投。

冻结对象仅为本文件。完成写入后，本席将本人 FULL 读回全文并核对行数、bytes、SHA256；最终指纹在交付消息中报告，避免自包含哈希循环。未收到另行明确授权前，不修改冻结报告。
