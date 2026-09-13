# Paper31：I01 / I03 深查来源与包含映射 V1

日期：2026-09-09 UTC；执行席：`/root/p31_qpi_quick_filter_algebra_v1`。
阶段：`novelty-check / PHASE_B_ONLY`；状态：`SOURCES_AND_CONTAINMENT_MAP / NO_ADMISSION`。
范围：I01、I03 各三个 Phase A 核心；不改已冻结首筛，不进行 Phase C/D、跨模型评审、正式分数或候选投票。
主要结论：完整形式群/Witt 过滤、积分闭包特殊化和尖点稳定解消已有很强先例；余量必须落实为原 trace 两系数的保基比较及真实消费者。
没有读到直接识别本项目原临界理想的定理，不等于已经证明该比较新颖、困难或足够成篇。

## 1. 实际输入、技能与权限边界

本次完整读取 `novelty-check` 与其调用的 `research-lit` 技能，按每核心至少三条不同检索、近期覆盖及一手定理假设核查执行。
技能的后续评分/外审阶段不在本席授权内；只交付本文件，主控另行合取独立数学核验。
继承本人此前已经读过、且输入未变的局部基线；不重扫整个历史论文库，也不把旧阅读伪装为本轮新增阅读。

| 本次核定对象 | 阅读身份 | SHA-256 |
|---|---|---|
| [Phase A 三核心拆解](PAPER31_QPI_SURVIVOR_CLAIMS_PHASE_A_V1_20260909.md) | FULL，81行；本轮重新核定 | `be4a8b04354b762dc43cb9b7947248005c7f2c8612970387a2ef588b477d0b33` |
| [已冻结代数首筛](PAPER31_QPI_QUICK_FILTER_ALGEBRA_V1_20260909.md) | FULL，170行；仅读取继承账，不修改 | `28746a09feaa908b5e0a532cff311332936c4710580b5e2724d307f621cc5702` |
| `/root/autodl-tmp/.codex/skills/novelty-check/SKILL.md` | FULL，86行 | `bf82687716497fd301e828fd8eb835815eb16d3d9267c1f9dd0849b3a05948df` |
| `/root/autodl-tmp/.codex/skills/research-lit/SKILL.md` | FULL，193行 | `63a2d6459b14e5f25496bf28fc45020c5ff537261aa7b2ffa66ced72b1f895d7` |

原始[十项生成](PAPER31_QPI_IDEA_GENERATION_V1_20260909.md)、[组合基线](PAPER31_QPI_PORTFOLIO_BASELINE_V1_20260909.md)、[新接口处置](PAPER31_QPI_DISCOVERY_INTERFACES_DISPOSITION_V1_20260909.md)的读取与哈希沿用首筛 §1。
所有比较保留原八中心、两状态方向、完整有限纤维及指定提升；不以正规化、去挠率、饱和或积分闭包替换原理想。
`route_applicability: NOT_APPLICABLE`；纯数学，必要及实际 GPU 均为0。
未运行候选 CAS、未建 `papers/31*`、未改索引/锁/接受原稿，未联络作者或申请资源。
为了核对排版歧义，只在独立临时目录保存两份公开原文 PDF 及相应单页图像；不是论文构建或候选实验。

## 2. 按核心固定的搜索方法与 setting

| 核心 | 方法关键词 | 不能在比较中丢失的 setting | 基础检索数 |
|---|---|---|---|
| I01-C1 | 形式群普遍形变、Hasse–Witt、微分系数整性、Fitting | 奇 p、p不整除m、光滑 Hasse 根、原 C₂ 与积分闭包分别检查 | B01–03、B11–12，共5 |
| I01-C2 | integral dependence、Rees valuations、polar multiplicities、specialization | 同一完整纤维；固定 π、能级标记；不是任意换参数后的抽象同构 | B04–07，共4 |
| I01-C3 | canonical subgroup、ramification、higher Hasse–Witt | 实际状态阶/厚度及末端四图；不能只给一个系数或群扭点阶 | B08–10、B13–14，共5 |
| I03-C1 | A₂/plane cusp deformation、Kähler、Jacobian | 保留 π、T−T₀、J−h₀ 的原两系数；T₀=−27/256，h₀=9ε/8 | B15–18，共4 |
| I03-C2 | critical scheme、complete intersection、associated primes、flatness | 总空间和固定时间/能级切片分开；嵌入分量存在仅是问题 | B19–22，共4 |
| I03-C3 | arbitrary characteristic、cusp/node smoothing、stable resolution | p≥5；原理想的层间特殊化，不重复旧 p=5、7、≥11 切向结果 | B23–26，共4 |

26条基础查询已超过六核心各三条的最低18条；另13条追索准确题名/包含定理，共39条网页查询。
搜索窗口明确覆盖2024–2026，最近六个月按2026-03-09至2026-09-09；发表日期、arXiv提交日期与网页抓取日期分别识别。
实际可用：公开网页搜索、公开 arXiv Atom API、arXiv/作者/出版社/机构原文、Stacks 官方条目。
未发现已配置的 Zotero/Obsidian/S2/Scholar 专用检索工具或可用本地 arxiv_fetch.py；不冒称已调用。
Scholar/S2 历史直接访问为403/429，本次不重试受限端点、不绕过；仅执行域名限制的公开索引查询，不能算完整数据库覆盖。
检索返回的论坛、聚合摘要、AI内容或无关 GitHub 文档一律只作噪声/定位，不承担包含性证明。

## 3. 完整实际网页查询账

以下字符串为本轮实际调用；打开/定位原文不另计query。某些域名查询返回泛化噪声，不伪装为有效查全。

| ID | 核心/用途 | 原样查询 |
|---|---|---|
| B01 | I01-C1 | `"q-Painlevé" "critical" "formal group"` |
| B02 | I01-C1 | `"supersingular" "deformation" "Fitting ideal" "Hasse"` |
| B03 | I01-C1 / 近期 | `site:arxiv.org "higher Hasse-Witt" (2024 OR 2025 OR 2026)` |
| B04 | I01-C2 | `specialization integral dependence modules Rees Gaffney Kleiman` |
| B05 | I01-C2 / Scholar索引 | `site:scholar.google.com Rees valuations ideals equisingularity` |
| B06 | I01-C2 / S2索引 | `site:semanticscholar.org integral closure ideals specialization` |
| B07 | I01-C2 / 近期 | `site:arxiv.org "Rees valuations" after:2024-01-01 before:2026-09-10` |
| B08 | I01-C3 | `supersingular elliptic formal group canonical subgroup Hodge height ramification valuations theorem` |
| B09 | I01-C3 / 近期 | `Dwork crystals higher Hasse Witt conditions 2024 2025 2026` |
| B10 | I01-C3 / 六个月 | `site:arxiv.org supersingular critical ramification differential after:2026-03-09 before:2026-09-10` |
| B11 | I01-C1 / Scholar索引 | `site:scholar.google.com supersingular formal group deformation Hasse Witt critical ideal` |
| B12 | I01-C1 / S2索引 | `site:semanticscholar.org supersingular formal groups higher Hasse Witt` |
| B13 | I01-C3 / Scholar索引 | `site:scholar.google.com canonical subgroup Hodge height ramification valuations` |
| B14 | I01-C3 / S2索引 | `site:semanticscholar.org Dwork crystals higher Hasse Witt` |
| B15 | I03-C1 | `"plane curve" "cusp" "Kähler" "deformation" positive characteristic` |
| B16 | I03-C1 / Scholar索引 | `site:scholar.google.com equisingular deformations plane curves arbitrary characteristic` |
| B17 | I03-C1 / S2索引 | `site:semanticscholar.org cusp Kahler differentials Jacobian deformation` |
| B18 | I03-C1 / 近期 | `site:arxiv.org cusp differential deformation after:2024-01-01 before:2026-09-10` |
| B19 | I03-C2 | `critical ideal flat family complete intersection embedded associated primes` |
| B20 | I03-C2 / Scholar索引 | `site:scholar.google.com Jacobian scheme family complete intersection flatness` |
| B21 | I03-C2 / S2索引 | `site:semanticscholar.org cusp deformation Fitting ideals flatness` |
| B22 | I03-C2 / 近期 | `site:arxiv.org "critical" "complete intersection" after:2024-01-01 before:2026-09-10` |
| B23 | I03-C3 | `cusp node smoothing deformation positive characteristic Jacobian scheme exceptional primes` |
| B24 | I03-C3 / Scholar索引 | `site:scholar.google.com cusp deformations plane curves positive characteristic good characteristic` |
| B25 | I03-C3 / S2索引 | `site:semanticscholar.org equisingular deformations plane curves arbitrary characteristic Campillo Greuel Lossen` |
| B26 | I03-C3 / 六个月 | `site:arxiv.org cusp smoothing positive characteristic after:2026-03-09 before:2026-09-10` |
| B27 | CGL准确题名 | `"Equisingular deformations of plane curves in arbitrary characteristic" arxiv` |
| B28 | 完全交包含 | `site:stacks.math.columbia.edu regular local ring height generated regular sequence Cohen Macaulay no embedded primes` |
| B29 | Rabinoff原文 | `"Higher-level canonical subgroups" Rabinoff arxiv` |
| B30 | 形式群原文 | `"Lubin" "Tate" "Formal moduli" deformation 1966 universal` |
| B31 | 2024准确题名 | `"Polar Multiplicities and Integral Dependence" 2024 arxiv` |
| B32 | Dwork原文 | `"Dwork crystals II" arxiv` |
| B33 | 2025题名定位 | `"110512" "Hasse" 2025` |
| B34 | 官方旧原文 | `"Formal moduli for one-parameter formal Lie groups" numdam` |
| B35 | 2025作者定位 | `"Beukers" "Vlasenko" "110512"` |
| B36 | 形式群整性 | `site:arxiv.org "formal groups" "integrality" Vlasenko` |
| B37 | 相邻比较定位 | `"On Vlasenko" "formal group laws" arxiv` |
| B38 | 高阶条件原文 | `"Higher Hasse-Witt conditions" Vlasenko` |
| B39 | 2024–26核对 | `site:arxiv.org "Hasse-Witt" 2024 2025 2026 supersingular` |

## 4. arXiv API 与近期结果闭环

API使用 `https://export.arxiv.org/api/query`，curl保持证书校验；按提交日期降序，不作外部写入。
下面 D 表示共同条件 `submittedDate:[202603090000 TO 202609092359]`；OR组合中有分词噪声，结果数不等于相关论文数。

| 请求 | 实际 search_query | 分页与返回 | 阅读/处置 |
|---|---|---|---|
| A1 | `(all:"supersingular" OR all:"integral dependence" OR all:"cusp") AND D` | total353，start0/max20；输出截断 | 仅证明端点可用；未通读20条，不作排除性覆盖 |
| A2 | `(all:"formal group" OR all:"Hasse-Witt") AND D` | total13，start0/max12；随后A2b start12/max1 | 13条标题/摘要均实读；重点打开 Rezk 与 Debaisieux |
| A3 | `(all:"plane cusp" OR all:"integral dependence" OR all:"Rees valuations") AND D` | total10，start0/max12 | 10条标题/摘要均实读；重点打开 Wewers 与 Das–Roy–Trivedi |

A2新增直接相关：[Rezk 2603.12490](https://arxiv.org/abs/2603.12490)、[Debaisieux 2606.25726](https://arxiv.org/abs/2606.25726)。
[2607.03257](https://arxiv.org/abs/2607.03257)是高度一交换形式动力系统；[2604.27111](https://arxiv.org/abs/2604.27111)是 Lubin–Tate 对数像，均仅摘要级相邻记录，不代替本题高度二比较。
A2其余9条涉及二次型Hasse–Witt、Igusa/自同构表示、泛化形式群属或非数学分词噪声，未发现摘要中直接识别原 qPI 理想；未作全文否定判断。
A3新增直接相关：[Wewers 2606.13875](https://arxiv.org/abs/2606.13875)、[Das–Roy–Trivedi 2605.14203](https://arxiv.org/abs/2605.14203)。
A3其余8条为单边非交换理想、量子线路应用、积分分析或分词噪声，不据其摘要声称涵盖/排除原算术临界概形。
2024主线新增 Cid-Ruiz 两篇、Vlasenko讲义；2025检出的 Beukers–Vlasenko 110512 实为 Calabi–Yau Frobenius/zeta 论文，不能误记为原高度二临界理想定理。
搜索也返回[Hasse-Witt invariants of Calabi-Yau varieties](https://arxiv.org/abs/2603.03055)，提交2026-03-03，属2024–26窗口但不属本次六个月窗口。

## 5. 本轮新增的一手定理级读取

等级 T：摘要/引言或related-work与实际定理假设已读；不是全文证明重审。等级 A：只读一手摘要/题名，不承担包含定理。
下表正文页均从1计；同源 HTML/PDF 的读取不重复计为不同论文。

| ID / 一手原文 | 实际读取范围 | 假设、已知机制及不能越过的边界 |
|---|---|---|
| S01 [Vlasenko, Formal groups and congruences, v5](https://arxiv.org/pdf/1509.06002v5) | T；pp1–4，Thms1–2、related-work；Thm1证明开头 | Thm1要求特征零整性底环及Frobenius endomorphism；给微分系数p-sequence整性充要条件，不要求ordinary。Thm2另要求绝对非分歧完备DVR，给所有有限高度的系数阶与局部特征多项式重建。 |
| S02 [Gaffney–Kleiman, Specialization of integral dependence for modules, v3](https://arxiv.org/html/alg-geom/9610003v3) | T；摘要、引言、§1设置、Thm1.8及证明、Prop1.5附近 | 复解析族、等维同维纤维、自由模中有限余长度族、商支持对基有限；总空间等维且BR重数常数时，稠密开上的积分依赖推广。不是直接的混合特征定理。 |
| S03 [Cid-Ruiz, Polar multiplicities and integral dependence, v2](https://arxiv.org/html/2401.10198v2) | T；摘要/引言、ThmA、Thm4.4与证明段、Thm5.1 | Thm5.1：等维且普遍链状Noetherian局部环、同秩有限模U⊂E；混合BR不变量刻画reduction。无复解析/特征零限定，但不会替人计算原两系数。 |
| S04 [Cid-Ruiz–Polini–Ulrich, Multidegrees, families, and integral dependence, v1](https://arxiv.org/pdf/2405.07000v1) | T；摘要/引言pp1–5、Setup5.1 p15、Thms6.6–6.7 pp25–26；p25图像核对 | PSID处理原积分闭包在切除参数后的检测；需要等维、普遍链状、维数降一、ht(I,t)≥2及指定Segre数相等。极重数本身并非无条件检测器；Thm6.7另有等阶/G-parameter条件。 |
| S05 [Beukers–Vlasenko, Dwork crystals II, v3](https://arxiv.org/html/1907.10390v3) | T；§1设置/引言、Thm2.3及证明、Cor3.1/Thm3.2 | p-adically complete特征零domain、Frobenius lift；Thm2.3明确要求首Hasse–Witt矩阵可逆。所得为Cartier/period及截断同余，不是Hasse根处原C₂。 |
| S06 [Vlasenko, Congruences and cohomology, v1](https://arxiv.org/html/2412.13313v1) | T；作者讲义引言、§5.1–5.3中Thm37/Def41及证明开头、相关来源表 | Thm37在1≤k<p及k阶Hasse–Witt条件下分裂高阶形式导数；Def41同时要求1≤ℓ≤k的规范化行列式为单位。不能只凭“beyond unit root”标题忽略这些假设；讲义所述机制归于作者Dwork系列。 |
| S07 [Rabinoff, Higher-level canonical subgroups for p-divisible groups](https://arxiv.org/pdf/0910.3323) | T；摘要、§1.9–1.11及前后定义/已有结果比较 | 完备混合特征rank-one valuation ring，level N BT群，Hasse invariant H<(p−1)/p^N；给规范子群及半径。群扭点半径不是原状态微分理想厚度。 |
| S08 [Hattori, On lower ramification subgroups and canonical subgroups](https://arxiv.org/pdf/1208.5326) | T；摘要/引言、Thms1.1–1.3、Thm1.2证明起始 | Thm1.2为完备DVR上level n BT群、0<d<h、Hodge height w<(p−1)/p^n；规范子群等于指定下分歧子群。只把其作为群论消费者的竞争机制，未构造qPI比较。 |
| S09 [Campillo–Greuel–Lossen, Equisingular deformations of plane curves in arbitrary characteristic](https://arxiv.org/pdf/math/0701002) | T；摘要/引言pp1–3、Def4.1、Thm4.2及证明pp21–22 | 代数闭域上约化平面形式曲线，equisingular deformation；好特征指p不除任一分支重数。给无阻碍性和参数化/方程比较；普通尖点重数2，因此p≥5不是此理论的坏特征。不是保原参数的算术trace两系数正规形。 |
| S10 [Wewers, Explicit local stable resolution of cusps, v1](https://arxiv.org/html/2606.13875v1) | T；摘要、§§1.1–1.3、Thm1.1、§2.1设置 | 完备离散赋值域、代数闭剩余域、primitive integral平面模型，在尖点邻域normal且离该点smooth。有限可分扩张及允许坐标选择后，一次(1,2,3)加权吹起给稳定解消、Weierstrass尾与节点厚度。它允许改坐标/扩域且处理曲线模型，不自动保原(π,T,J)理想。 |
| S11 [Rezk, The Witt filtration of Lubin–Tate deformation rings, v1](https://arxiv.org/pdf/2603.12490v1) | T；摘要/引言pp1–3、§§8.11–8.14含Prop8.13证明p12；p12图像核对 | perfect剩余域、有限高度形式群的普遍形变环；Witt过滤与自同构相容，p乘法/模p几何过滤相接；高度二有完整理想递推。原印本下标冲突另列§6，不把有歧义的闭式当可直接调用的公式。 |
| S12 [Debaisieux, Integrality of height-one formal groups](https://arxiv.org/pdf/2606.25726) | T；摘要、§1.1–1.2、Main theorem(4.2)陈述 | 有限扩张K/Qp、所有[n]积分且wideg([p])=p推出F积分；高度一限制明确，不包含I01高度二。 |
| S13 [Das–Roy–Trivedi, Numerical characterizations for integral dependence of graded modules, v1](https://arxiv.org/html/2605.14203v1) | T；摘要/引言、ThmD、§2设置、Thms6.5–6.6陈述 | 域上标准分次domain维数≥2、有限无挠分次同秩模；密度/epsilon及Rees对角重数刻画reduction。是近期强工具，不是原非分次混合特征局部理想的现成计算。 |
| S14 [Stacks 00NQ](https://stacks.math.columbia.edu/tag/00NQ)、[02JN](https://stacks.math.columbia.edu/tag/02JN)、[031O](https://stacks.math.columbia.edu/tag/031O) | T；各实际命题与所示证明，尤其10.157.2 | 正则局部环CM；CM局部环中正确余维的生成元组成正则列；S₁等价无嵌入关联素理想。用于I03-C2的条件性标准扣除。 |

继承但不计本轮新增T：首筛S1的Vlasenko高Hasse–Witt整性、S2的Lubin–Tate有限高度普遍形变、S5的原Kähler/去挠率警告、S6的Shimada模p²算术Kodaira–Spencer定理。
这些已知机制仍须扣除；普通条件不能泛化到全部形式群理论，模p²也不能偷换成原圆分任意深度。

## 6. 两处必须明示的公式读取风险

S04网页/PDF抽取把闭包横线和≥符号吞掉；官方PDF第25页肉眼确认：ht(I,t)≥2，且结论是h属于积分闭包Ī，当且仅当所有t不在其中的素理想局部化处h属于I Rₚ的积分闭包。
因此S04不是“原理想成员关系可由开集检测”的无条件定理，不能用它直接升级到C₂理想相等。
本次PDF SHA：`73ee73e4d2fee1425939610820033659c87b5f40a6d50150c16529fd934c9efc`。

S11不是仅有HTML转换问题：官方PDF第12页与HTML一致地印出下述彼此不协调的下标。
§8.12同时写n_d=N²_{p^d}=1+p+⋯+p^{d−1}；但按其§1.5的子群数定义，N²_{p^d}的计数末项应到p^d。
Prop8.13写f₁=a及O/I_d≈O/(p^d,p^{d−1}f₁,…,f_{d−1})；相邻Ex8.14却写I₁=(2,a)、I₂=(4,2a,a³−2)。
这是本次阅读识别出的源内下标冲突，不是作者确认的勘误；本报告不静默修正文献，也不宣告整项结果错误。
证明中明确写出I_{d+1}=pI_d+(f_d)，且模p商来自有限子群的普遍几何；作为完整过滤机制的相邻先例是实质性的。
精确闭式若要用于候选证明，必须先统一索引、核实初项并重新验证所用版本；此义务独立于把Witt理想比较到qPI的义务。
本次PDF SHA：`01665af8269b3a71b4bf26fcb2ea98db7f15655ecf3681af078b723a991af91a`。
S03/S04/S11实验HTML中的2026排版日期不当成arXiv提交日期；本件版本身份以正式提交记录/PDF页首为准。

## 7. I01：三核心逐项包含映射

| Phase A核心 | 最近/最强已知机制 | 真正可能的delta | 缺失证明与拒绝条件 |
|---|---|---|---|
| C1 原C₂与保标记基底比较 | Lubin–Tate普遍形变；S01任意高度形式群整性；S11完整Witt过滤 | 构造原trace微分的两系数与某一明确普遍理想的保(π,j)比较；原理想/积分闭包两层分别定理化 | 还没有实际比较态射、生成元对应、圆分深度与末端相容证明。只有“高度二故有一参数”或改名Witt理想应淘汰该表述。 |
| C2 同纤维Rees/归一化吹起不变量 | S02复解析PSID；S03一般局部环模reduction；S04 Segre特殊化；S13分次数值判据 | 实际计算原C₂，证明某同纤维差异经允许框架/保基变换后仍存在，或证明统一拉回确实成立 | 定义Rees代数、引用赋值判据、两个坐标系系数不同都不够。若通用判据加短消元即得答案，不能用术语包装成新机制。 |
| C3 实际状态阶与完整临界厚度 | S01 Thm2高度依赖的微分系数阶；S07/S08规范子群半径/分歧；S05/S06带可逆假设的高Cartier结构 | 将完整原理想的不变量转成超首jet的逐状态预测，并覆盖末端四图 | 未证形式群微分系数等于原trace系数；未证群扭点半径控制原状态厚度；未证有限jet决定完整理想。只给一个高阶系数应淘汰该缩减形式。 |

S01的特别强扣除：在其Thm2的绝对非分歧DVR假设下，高度h有限时ord_p(b_{p^n−1})≥n−⌊n/h⌋，h整除n时等号；正文明确写高度二偶奇模式及特征多项式恢复。
所以“高度二带来额外p阶”不是可独立计功的新发现；原圆分完备环与该DVR的比较仍是另一个必须证明的步骤。
S11表明竞争者已经在完整理想层，不止在首Hasse或单位根层；但其坐标a不能不经证明等同原能级提升j。
沿同一完整纤维的不可消差异也不能预设存在；若保基统一式成立，应如实给统一式，不制造失败以保留选题。
本次来源侧判断：`SUBSTANTIAL_CONTAINMENT_PRESSURE / ACTUAL_BRIDGE_UNPROVED`，不是正式HOLD/KEEP投票。
原22–30页全部必要证明容量仍UNKNOWN；不能将上述一般形式群/交换代数背景的篇幅当作新证明容量。

## 8. I03：三核心逐项包含映射

| Phase A核心 | 最近/最强已知机制 | 真正可能的delta | 缺失证明与拒绝条件 |
|---|---|---|---|
| C1 保π、T−T₀、J−h₀的实际两系数正规形 | S09好特征平面曲线变形；标准A₂；继承的Kähler/算术KS机制 | 在原算术局部环中给trace两系数的联合正规形，追踪指定时间与能级提升 | 只求曲线方程的Jacobian、正规化或模p² lift障碍不够；尚未证明坐标变换可保原三参数及原Kähler消费者。 |
| C2 关联素理想/局部长度/平坦性 | S14高度二两生成元的完全交/CM/无嵌入；一般Fitting与flatness机制 | 具体分量、重数、长度和沿指定基映射的平坦/非平坦分层；总空间与切片分开 | “有挠微分所以有嵌入分量”无效；“无嵌入分量”若是标准完全交推论就不得另算核心新定理。实际height和分量/平坦性尚未全证。 |
| C3 p≥5的尖点/节点/光滑原理想特殊化 | S09的好特征判别；S10最新完整局部稳定解消、尾曲线与节点厚度 | 原trace系数随时间/能级/圆分变化的统一特征分层；解释真实理想而非仅曲线类型 | 旧p=5、7挠微分及p≥11消失已接受；单独尖点稳定解消或A₂判别式属于已知机制。尚需实际系数和特殊化相容证明。 |

条件性标准扣除应准确写为：若总局部环R正则、C₁=(A,B)并且dim(R/C₁)=dim(R)−2，则A,B为正则列，R/C₁为CM，因而无嵌入关联素理想。
本件不扩展为新的qPI数学证明，也不将该“若”删除；原泛纤维/模π非零信息能否给所需height，交由独立数学核验。
即使总空间无嵌入素理想，固定T或固定J后所取商仍可能失去所需正则序列性质；切片关联素理想必须另算。
CM与无嵌入本身不等于对任意时间/能级基底平坦；还需核查所用基映射、维数条件或参数非零因子条件。
S09中尖点分支重数为2，p=5、7和p≥11均是好特征；故旧5/7分裂不能解释为A₂自身的坏特征，而要来自具体原微分/提升。
S10虽在2026年6月给出强局部稳定解消，它允许扩域/调坐标，且没有原trace系数这一附加对象；这不是已包含I03的证明，也绝非新颖性PASS。
本次来源侧判断：`NARROW_TO_ACTUAL_COEFFICIENT_FAMILY / GENERIC_SINGULARITY_NARRATIVE_DEDUCTED`，不改冻结首筛标签。
若原系数最终只给标准A₂消元和既有孤立切向结论，应淘汰该精确形式，不扩大成其他系统族以保活。

## 9. 引用限制、交付与下一阶段入口

未完成的数据库覆盖：Scholar/S2仅公开索引；Zotero/Obsidian未配置；arXiv查询只覆盖给定字符串和截止时点，不证明全世界无先例。
本轮未使用跨模型接口、未编造GPT-5.4 threadId；Phase C应由主控明确标识实际可用独立Codex评审身份。
OUP极重数页重定向读取失败；Utrecht Dwork PDF超时、2025 PDF为403；未绕过，改读作者公开arXiv版本或仅使用可读机构摘要。
Lubin–Tate本轮两个其他PDF地址超时，沿用本人首筛已读的准确官方原文身份，不声称本轮又成功读完。
S04 HTML正文定位失败后读官方PDF；网页截图未向本席提供可见图像时，使用公开PDF本地单页渲染核实，而非宣称已看截图。
搜索邻接错误打开的[2005.00676](https://arxiv.org/abs/2005.00676)实为Lee–Lian–Zhang的tautological-system论文；已读题名/摘要后排除，未误认作On Vlasenko's formal group laws。
Vlasenko高Hasse–Witt勘误/全部相邻形式群比较仍未穷尽；本报告的“不直接给出”只针对已读定理及其明确假设。
只请求后续核验两个有界事实入口：I01实际trace到形式群/完整理想的比较是否非短推论；I03实际两系数、height与特殊化是否仍有独立实质。
两者都不得因文献未提qPI名称而获得新意；也不得因旧定理未写所需比较态射就先估出22–30页长证明。
本件保存后全文自读，核六核心查询下限、39条查询账、3种API查询/4次请求、实际读段及本地直链；终态SHA在交付消息单列。
