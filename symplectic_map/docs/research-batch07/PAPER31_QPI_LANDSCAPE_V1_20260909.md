# Paper31 原 qPI 算术临界结构：有界文献景观 V1

日期：2026-09-09（UTC）。状态：`LANDSCAPE_ONLY / NO_CANDIDATE_ADMISSION`。
本报告仅执行 `idea-creator` 的景观部分与 `research-lit` 的定向检索；不排序想法，不出正式查新票，不证明候选定理。
范围是原 qPI 八中心模型、原圆分整除微分与两方向临界理想；高厚度、自然圆分塔、奇异完整能级只是待比较接口。
Paper30 已实际本地接受；本文件既不重开其接受，也不把其未覆盖边界自动指定为 Paper31。

## 1. 输入、实际本地阅读与绑定

本轮实际新读：接受 PDF 前 3 页（`pdftotext -f 1 -l 3 -layout`）；V4 引言全文 300 行；§8 末尾 567–666 行；两个接口盘点全文；本地接受记录全文。
引用记录只定向读与 JR、Vlasenko、Dwork、Lubin–Tate、Shimada 等有关的条目，未把旧阅读账转称本轮全文阅读。
本轮不读取整个旧构建树，不重新编译、不改已接受原稿、不建立 `papers/31-*`。

| 输入（以下路径均相对于工作区） | SHA-256 |
|---|---|
| `papers/30-qpi-vertical-critical-ideals/notes/LOCAL_ACCEPTANCE_20260909.md` | `cfb2f9e034716545fd22d9e7024d7b9b62d89350c3eecc97852870b17f094a52` |
| `papers/30-qpi-vertical-critical-ideals/build/natural-20260909-r4/work/main.pdf` | `40f05a156cbedc16a881b090a19af299c12c41a1fd9fb62a0290406a83737007` |
| `papers/30-qpi-vertical-critical-ideals/paper/v4/sections/01-introduction.tex` | `9b2876f36052d545ccf03a8309c4119f66ea06c3a9bbffa002e6228aa7610c0e` |
| `papers/30-qpi-vertical-critical-ideals/paper/v4/sections/08-two-jets.tex` | `5cfee2a607e6ff1ab52192bb5c9b1a73cef6635c3e5dcfe26aa73fe1192b42a9` |
| `papers/30-qpi-vertical-critical-ideals/notes/CITATION_RECORDS_20260909.md` | `8c531f799e71f82f01039332b1d80eaa78ea15b20d6716ddb21924faf98cbf6e` |
| `docs/research-batch07/PAPER30_EXISTING_QPI_INTERFACE_INVENTORY_V1_20260909.md` | `e5033d678872970d5018f007fa18c15e4cf0085980f26eb0ba0a616fdab4036d` |
| `docs/research-batch07/PAPER29_30_EXISTING_INTERFACE_LIMITS_V1_20260909.md` | `bbcc282cad6a78da92500b21ee91ed892f1152bbfc339f2ad860468c27af593c` |

局部基线：首圆分层已有全部素数与 tame block 下、完整光滑有限纤维附近的完整原两方向系数理想。
更高层已有带精确残余域/全时间 jet 条件的模圆分参数平方结果；特征二长度五属于该截断商及原基参数作用。
不能把“高层完整理想”“所有奇异纤维”“统一形式群比较”写成 Paper30 已证，也不能把首层既得部分重新当作创新。
P29/P30 的跨系统族接口只保留 `ROUND2_CLUE`，本报告没有据此另开系统族。

## 2. 检索账与工具限制

全部检索发生于 2026-09-09；近六个月窗口取 2026-03-09 至 2026-09-09，另覆盖 2024–2026 与基础原文。
以下为实际执行的不同查询，按主题合并展示；返回的非论文营销页、目录页和同名无关结果没有进入证据表。

| 组 | 实际查询字符串（分号分隔不同查询） |
|---|---|
| 原对象 | `"q-Painlevé I" "cyclotomic" differential`；`"q-Painlevé I" "critical ideal"` |
| 奇异 Cartier | `"Cartier operator" "singular curves" normalization nodal cuspidal`；`"Cartier operator" "singular curves" normalization` |
| 对偶化/Frobenius | `"Cartier" "singular" "dualizing" curves paper`；`"Frobenius" "kernel" "cuspidal" differential` |
| 原 Kähler 对象 | `"Kähler differentials" "cusp" "characteristic p"`；`"kernel" "differential" "singular curves" "p-th"` |
| 挠率/半正规化 | `"Cartier isomorphism" "seminormal"`；`"torsion differentials" curves positive characteristic cusp` |
| 分歧临界 | `"critical" "ramified" "arithmetic" schemes differential cyclotomic`；`"ramified" "critical scheme" arithmetic differential`；`"ramification" "critical" "Fitting" "differentials" arithmetic geometry` |
| higher Hasse | `"higher Hasse" "formal groups" 2024 2025 2026`；`Vlasenko 2024 higher Hasse Witt crystalline cohomology`；`"Higher Hasse-Witt matrices" corrigendum 2019 Vlasenko` |
| 圆分塔 | `"q-Hodge" "Wagner" cyclotomic`；`"Dwork crystals III"`；`"Dwork crystals III" journal 2023` |
| 近六个月 | `site:arxiv.org "Cartier" "singular" after:2026-03-09 before:2026-09-10`；同一日期约束的 `"Dwork"`、`"Frobenius-Witt"` 查询 |
| 2026 原对象/障碍 | `site:arxiv.org "Painlevé" "arithmetic" 2026`；`Shimada "Frobenius-Witt" "2026"` |
| 题名追索 | `"Formal Abel relations for curves in characteristic" arxiv`；`"On the p-rank of singular curves and their smooth models" arxiv`；`"Differential forms on the curves associated" "arxiv"` |

arXiv 官方 API 实际查询：`all:"Cartier" AND all:"singular" AND submittedDate:[202603090000 TO 202609092359]`，`max_results=10`，HTTP 200。
该次返回四条近期同名/弱相关记录（2605.22782、2605.22987、2607.20272、2608.10219），只检查返回元数据后排除；没有用它们凑阅读数量。
Semantic Scholar Graph API 查询 `cyclotomic q-Painleve critical differential`，请求 title/year/url/abstract，HTTP 429；停止该访问，不改账号或申请付费额度。
Google Scholar 查询 `"q-Painlevé" "critical" "cyclotomic"`，HTTP 403；停止该访问，不绕过反爬或把失败当零命中。
可用工具中未发现 Zotero/Obsidian 接口；技能指向的 arXiv 下载脚本未在所检查技能目录找到，故使用公开官方 API 与作者 arXiv 正文。
Ohashi–Harashita 官方刊本 PDF 入口未成功取得可读正文；使用其作者 arXiv v3，未宣称核准刊本逐式一致。
以上是有界多路检索，不是数据库全量检索；未访问内容既不支持包含结论，也不支持全球新意结论。

## 3. 实读文献：原对象与奇异纤维

共实际重新打开并读摘要/引言或等价开头段的 15 份相关学术文献：研究论文/预印本及两份讲义/综述材料分项说明。
下列“已知机制”指来源直接叙述的内容；“接口判断”是本次比较推论，不声称来源已研究原 qPI 临界理想。
来源为作者 arXiv、作者站点或官方原文；正文范围均为实际阅读，不等于全文证明复核。

### L01. Joshi–Roffelsen：原 qPI 算术退化

- 来源：[Arithmetic dynamics of a discrete Painlevé equation，arXiv:2508.18578v2](https://arxiv.org/html/2508.18578v2)，2026-01-16 修订；刊本身份继承已核 P30 引用账，非本轮刊本图像验收。
- 实读：作者 v2 摘要与 §1 引言/研究背景；原矩阵定义本轮主要以已接受 P30 为输入，未重新通读全部 JR 证明。
- 已知机制：有限域/单位根 qPI 的算术动力学、第一积分退化与次数结构是直接前置工作；原系统及纯幂现象不是新的研究对象。
- 接口判断：高层整除微分的混合理想须在同一原积分和时间作用下比较；不能因本文未在摘要提到临界理想就认定不包含。
- 证据等级：原对象最邻近来源；本轮引言级比较，后续若固定命题仍须回到相关精确定理逐项扣除。

### L02. Terzi：奇异曲线与光滑模型的 p-rank

- 来源：[On the p-rank of singular curves and their smooth models，arXiv:2309.06901v2](https://arxiv.org/pdf/2309.06901v2)，2024-01-19 修订。
- 实读：摘要、引言与 §2 关于奇异曲线、广义 Jacobian 和正规化的必要段；未通读 28 页。
- 已知机制：用奇异曲线与光滑模型 Jacobian 间的群概形正合列比较 p-rank/a-number，节点、尖点的线性部分不能混为一谈。
- 接口判断：这是研究奇异完整纤维的直接背景；p-rank/a-number 不等于原两状态微分系数理想，也不保留其圆分厚度。
- 必须扣除：仅把“普通/非普通”替换成广义 Jacobian 术语、或复算正规化 p-rank，不足以产生独立原 qPI 结果。

### L03. Ohashi–Harashita：奇异曲线对偶化微分的 Cartier

- 来源：[Differential forms on the curves associated to Appell-Lauricella hypergeometric series and the Cartier operator on them，arXiv:2105.11436v3](https://arxiv.org/pdf/2105.11436v3)，2022-01-31。
- 实读：摘要、引言（PDF 前 3 页）及 §6 Definition 6.1、Theorem 6.2 与所显示证明段。
- 已知机制：在指定曲线及部分解奇异模型上显式给出对偶化层全局截面，并证明所定义 Cartier 作用保存相应正则微分空间。
- 接口判断：提供奇异 Cartier 的真实可用模型，但消费者是对偶化/Rosenlicht 微分；不能径直替换原 Kähler 微分模。
- 未解决：没有建立其特定曲线方程与原八中心能级的识别，也没有从其 Cartier 矩阵推出 qPI 圆分临界理想。

### L04. Little：正特征形式 Abel 关系（近期工作稿）

- 来源：[Formal Abel relations for curves in characteristic p，arXiv:2607.09471v1](https://arxiv.org/html/2607.09471v1)。
- 实读：摘要、§§1–2 的问题与形式关系设置；§6 的奇异四次曲线示例段（HTML 704–737 行附近）。
- 已知机制：以（广义）Jacobian 的形式群处理正特征约化平面曲线的 Abel 关系，包含奇异情形与非唯一性问题。
- 接口判断：说明“仅一阶微分无法恢复全部形式映射”这类风险已有独立背景；其几何截线关系不是 qPI 迹矩阵的高层提升定理。
- 版本限制：arXiv 元数据显示 2026-07-10，所返回 v1 正文标 Date: August 24, 2026；保留该差异，未擅自称 v2 或已同行评审。

### L05. Huber–Kebekus–Kelly：正特征奇异微分与挠率

- 来源：[Differential forms in positive characteristic avoiding resolution of singularities，arXiv:1407.5786v4](https://arxiv.org/pdf/1407.5786v4)，2015-03-05。
- 实读：摘要、§1 全部（PDF 页 1–3），以及 §2.2 Definition 2.3、Warning 2.4 的挠率说明；未读全篇证明。
- 已知机制：构造 cdh 与 dvr 扩张微分，明确它们在光滑对象上与 Kähler 微分一致，而正特征奇异对象存在挠率及拉回失真。
- 接口判断：直接支持“先写明微分层再比较”的方法约束；将原微分先模挠率、正规化或换拓扑会改变研究对象。
- 必须扣除：一般性挠率警告和解奇异比较不是新发现；真正候选仍须给出原 qPI 上可验证的具体核、像或理想差异。

### L06. Illusie：饱和 de Rham–Witt 的节点与尖点（作者综述）

- 来源：[A new approach to de Rham-Witt complexes, after Bhatt-Lurie-Mathew，作者 PDF](https://www.imo.universite-paris-saclay.fr/~luc.illusie/Illusie-BLM6.pdf)，所读稿含 2020 增补；未重新核定刊本。
- 实读：摘要、§0 引言；§§4.1–4.2（PDF 页 19–20）节点、尖点与半正规化例子；非全篇阅读，亦非 BLM 原文阅读身份。
- 已知机制：节点的原 de Rham 到饱和 W₁ 比较在一次不是同构；尖点 k[t²,t³] 的饱和复形与 k[t] 相同，零次已经改变原环。
- 接口判断：饱和 Cartier/正规化工具可能恰好抹去待研究的奇点信息；它们不能被当成原临界概形的无损重写。
- 范围限制：此处只消费作者明确写出的局部例子；没有从综述间接宣称审计了 BLM 全部比较定理。

## 4. 实读文献：高厚度、形式群与提升障碍

### L07. Vlasenko：Higher Hasse–Witt matrices

- 来源：[arXiv:1605.06440v3](https://arxiv.org/pdf/1605.06440v3)，2018-04-17；与 P30 引用重叠，本轮确实重读以下范围。
- 实读：摘要、§1 引言和 Theorem 1 的定义/陈述；Theorem 2 形式群结论及紧邻条件，未重新读完整证明。
- 已知机制：多项式幂系数的模 p 迭代、较高 p 进同余及形式群整性已有；unit-root 极限部分依赖首层 Hasse–Witt 可逆。
- 接口判断：不能把普通区高阶矩阵一般公式当作超奇异点完整混合理想；也不能反过来声称该文全部形式群结果都要求 ordinary。
- 勘误缺口：原账所记 `CORRECTION_IMPACT_UNKNOWN` 未消除；本轮查询未获得一手勘误内容，不以原版充当未核终版黑箱。

### L08. Beukers–Vlasenko：Dwork crystals I

- 来源：[arXiv:1903.11155v4](https://arxiv.org/pdf/1903.11155v4)，2021-05-31；[官方摘要页](https://arxiv.org/abs/1903.11155v4)。
- 实读：摘要页、PDF §1 引言与最初 Dwork 周期例子；不重复声称 P30 旧账中的全部定理已在本轮复审。
- 已知机制：通过 Cartier/Dwork 收缩与系数极限构造 unit-root 数据；摘要明确其框架不要求通常的 smoothness 假设。
- 接口判断：不能凭“奇异纤维”三个字排除 Dwork 包含；真正差异须检查 Hasse 可逆、商模、lift 及原迹/原参数识别。
- 未解决：本文引言不直接给出本题超奇异处、原两个状态系数同时保留的圆分厚度理想。

### L09. Beukers–Vlasenko：Dwork crystals III

- 来源：[arXiv:2105.14841v3](https://arxiv.org/pdf/2105.14841v3)，2023-02-19；[官方刊本 DOI](https://doi.org/10.1093/imrn/rnad101)，IMRN 2023(23), 20433–20483。
- 实读：摘要、§1 引言及其中 excellent Frobenius lift 驱动超同余的设置；没有通读刊本全文或重证高阶 Cartier 定理。
- 已知机制：通过 Cartier、高阶形式导数与 excellent Frobenius lifts 获得超同余；高阶消失本身并非 qPI 专属机制。
- 接口判断：若候选只把矩阵幂展开改名为“高阶新结构”，须先扣除这套方法；指定 lift 与自然 qPI 圆分塔仍需实际比较映射。
- 证据限制：这里有正式刊本元数据与作者正文，但不把二者当作逐式版本一致性证明。

### L10. Vlasenko：Cohomology and congruences（讲义/综述）

- 来源：[arXiv:2412.13313v1](https://arxiv.org/html/2412.13313v1)，2024-12-17；元数据题名与 HTML 的 Congruences and cohomology 词序不同。
- 实读：开头摘要/介绍；§§5.1–5.3 中 higher Hasse–Witt 条件、Theorem 37 和紧邻定义的相关段；未重读全篇。
- 已知机制：从高阶 Cartier、形式导数到 higher Hasse–Witt 条件的分层框架；所述层级要求不能只留下最高阶非零条件。
- 接口判断：需明确 k<p 以及较低层 Hasse 条件（特别是首层可逆），否则不适用于待考虑的超奇异残余点。
- 必须扣除：Hasse 同余、higher-Hasse 命名与迭代机制均已有；剩余只能是原对象特定比较或不同局部假设下的新结论。

### L11. Lubin–Tate：一参数形式 Lie 群的模

- 来源：[Formal moduli for one-parameter formal Lie groups，官方原文](https://www.numdam.org/article/BSMF_1966__94__49_0.pdf)，BSMF 94 (1966), 49–59。
- 实读：引言；§§3.2–3.5，特别是特征二高度二椭圆提升族的例子；未声称本轮全文重证普遍形变定理。
- 已知机制：有限高度形式群的普遍提升和参数结构是经典机制；高度二、可正规化单位参数不单独构成新贡献。
- 接口判断：要识别本题必须保留原 qPI 时间/能级坐标与基参数作用，而非只证明抽象形式群同构或相同商长度。
- 科学边界：本轮没有推导原圆分塔等于该普遍提升，也没有把数字五当成独立机制。

### L12. Shimada：Frobenius–Witt cotangent complexes

- 来源：[arXiv:2605.14803v1](https://arxiv.org/html/2605.14803v1)，2026-05-14，未核刊本。
- 实读：摘要和 §1 引言的定义动机、性质及 Theorems 1.1–1.3 陈述；未读全部 perfectoid 计算证明。
- 已知机制：Frobenius–Witt 微分的导出版本、传递纤维序列及正则性关系，将非光滑算术微分纳入既有理论框架。
- 接口判断：可用于检查非光滑情况下短正合列为何需要修正；但导出对象的存在不等于原 qPI 系数理想已经计算。
- 未解决：没有从原八中心转移函数、圆分参量与该复形建立具体可计算比较。

### L13. Shimada：Arithmetic Kodaira–Spencer Class and Frobenius Liftings

- 来源：[via Frobenius–Witt Cotangent Complex，arXiv:2608.21772v1](https://arxiv.org/html/2608.21772v1)，2026-08-22，近期预印本。
- 实读：摘要和 §1 引言全段，包括 Definitions 1.3–1.4、Theorem 1.5 与 related-work；未审计全部比较证明。
- 已知机制：对平坦 Z_(p)-概形定义含非光滑情形的模 p² Frobenius 提升障碍，且讨论与给定基 Frobenius lift 兼容的相对版本。
- 接口判断：只声称“有一个算术 Kodaira–Spencer 障碍”明显落在已知机制内；待证的是其与原 qPI 截面/系数项的具体识别。
- 新近缺口：引言提及 Mao 的 derived-ring 扩展，本轮未独立追读；不宣称该理论周边文献已穷尽。

## 5. 实读文献：自然圆分塔与 Habiro 兼容

### L14. Wagner：q-Witt vectors and q-Hodge complexes

- 来源：[arXiv:2410.23078v5](https://arxiv.org/html/2410.23078v5)，2025-10-06 修订。
- 实读：摘要、引言 1.1–1.6；§5 Theorem 5.1 的 no-go 陈述与其前提，未通读整个构造证明。
- 已知机制：q-Witt/Frobenius/Verschiebung 的圆分兼容结构已有；引言 1.3 明确其普通 restriction maps 并不延拓，不能无条件取相应限制逆极限。
- 接口判断：这不是 qPI 自然塔“不可能”的定理；§5 的特定范畴/函子性 no-go 不可越界升级成任意 qPI 比较不可能。
- 必须扣除：仅提出“单位根各层应有兼容性”不足；需给出原对象映射、选择条件及实际失配项。

### L15. Wagner：q-Hodge complexes over the Habiro ring

- 来源：[arXiv:2510.04782v1](https://arxiv.org/html/2510.04782v1)，2025-10-06，未核刊本。
- 实读：摘要、§1.1 及引言 1.15–1.18 附近的过滤/下降与存在条件；非全篇证明阅读。
- 已知机制：具合适 q-Hodge filtration 时有 Habiro 下降；一般不存在无条件典范过滤，特定光滑情形需反转相应小素数。
- 接口判断：不能把一般 Habiro 下降说成“不存在”，也不能把它直接认作原 qPI 两方向整除微分的自然塔定理。
- 未解决：本轮尚未建立原矩阵、固定时序、原基参数与该上同调结构间逐层保真的构造，不假设其存在或不存在。

## 6. 机制扣除与仍须实证的接口

| 待探索接口 | 已知机制先扣除 | 本轮未获得的原对象结论 |
|---|---|---|
| 高厚度临界结构 | L07–L11 的 Hasse 迭代、Cartier/Dwork、高度二普遍提升 | 原两方向系数理想在模圆分参数平方之外的精确式与原基作用 |
| 自然圆分塔 | L14–L15 的 q-Witt/Habiro 兼容及其条件 | 同一原 qPI 积分、时序和参数下的比较映射、相容式或具体障碍 |
| 奇异完整能级 | L02–L06 的正规化、广义 Jacobian、对偶化 Cartier、饱和复形 | 原 Kähler 临界对象保留奇点挠率/下降信息的具体计算 |
| 提升障碍解释 | L12–L13 的非光滑 Frobenius–Witt/算术 Kodaira–Spencer | 障碍类与原 qPI 截面、实际系数及转移函数的一一对应 |

以上最后一列的“未获得”仅指本轮阅读没有建立，不是全世界无人研究的判定。
尤其奇异能级须先区分 Ω¹_X、其模挠率像、ω_X、正规化上的 Ω¹ 与饱和 W₁Ω；光滑时的相同记号不应掩盖奇异时不同的对象。
若候选采用光滑纤维 Cartier 的 ker(d)=p 次幂步骤，必须在选定奇异环和选定微分模上重新验证，不能从正规化函数域直接下降。
一般“节点属乘法型、尖点属加法型”、首阶 Hasse 消失及形式群高度只提供分类信息，不能替代原临界概形的计算。
本报告没有证明新的核公式、尖点局部理想或高厚度递推；主控/其他代理的局部探索仍须独立审查后才能升格为数学输入。

## 7. 交付边界与后续门槛

已交付：有界检索账、15 份实读文献的准确阅读层次、原输入 SHA、一般机制扣除和访问缺口；未给候选排序或新意分数。
真正固定候选后，应以其精确假设与结论回查最邻近来源的定理和证明，而不是再次笼统扫描全部文献。
需保留的未闭合项：Vlasenko 勘误内容；Scholar/S2 访问限制；作者版/刊本差分；Little 日期差异；未追读 Mao 等引文。
普通区、光滑性、k<p、指定 Frobenius lift、自然时序、微分模选择及原参数作用都应显式列入后续比较，不事后删条件。
本报告不建立 Paper31 项目，不修改 Paper30、索引或验收账；不运行 GPU、外传、投稿或付费服务。
终态检查：生成后全文自读、核行数与 SHA-256，随后停止写入；终态 SHA 通过交接消息提供，避免文件自指哈希。
