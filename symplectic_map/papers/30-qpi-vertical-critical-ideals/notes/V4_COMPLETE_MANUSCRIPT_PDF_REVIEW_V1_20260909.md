# Paper30 V4：fresh 非作者完整实际稿件 / PDF 审查

日期：2026-09-09。审查结论：PASS_CURRENT_CONTRACT_MANUSCRIPT_PDF。
对象：冻结的 paper/v4/ 全部源文件及 r4 的完整实际 PDF；r5 用于独立根产物身份核对。
本结论表示在当前有效合同下，未发现需要修订的新转写、必要证明遗漏、范围越界或 PDF 可读性问题；不是无条件正确性证书、新的候选四门票或整批完成声明。

## 1. 审查身份、授权与有效合同

本席为 p29_p30_existing_interface_limits_v1，未参与 Paper30 证明作者、正式候选投票、此前全稿静审或排版。
本轮此前做过有界 P29/P30 既有接口盘点，接触过 P30 的部分既有材料；该接触已披露，不称完全盲审，也不称跨模型审查。
此前接口盘点已经独立交付并冻结；本文件不改变它，不新造候选、不打开 Paper31，也不把不同系统族的结果拼接为本稿证明。
本次亲自全文阅读全部十一件 V4 源，亲自打开全部四十一张实际页面；没有分片委派后冒称本人全文阅读，也没有用根代理逐页结论替代自身观看。
根代理的结果记录是在本人完成全部页面观看以后读取；仅作为构建过程及渲染来源记录使用，页面判断来自下述实际图像。

已全文读取的当前控制文件：

- [PUBLICATION_LOCK_20260909.md](PUBLICATION_LOCK_20260909.md)。
- [PUBLICATION_PAGE_ADDENDUM_V2_20260909.md](PUBLICATION_PAGE_ADDENDUM_V2_20260909.md)：仅 Paper30 正文上限由 30 改为 40，当前窗口为 22–40。
- [SOURCE_SCOPE_LOCK_V2_20260909.md](SOURCE_SCOPE_LOCK_V2_20260909.md)、[PAPER_PLAN.md](../PAPER_PLAN.md)、[CITATION_RECORDS_20260909.md](CITATION_RECORDS_20260909.md)。
- [V4_COMPLETE_PRODUCTION_PROTOCOL_V1_20260909.md](V4_COMPLETE_PRODUCTION_PROTOCOL_V1_20260909.md)。
- [当前证明图](../../../docs/research-batch07/PAPER30_QPI_VERTICAL_ALPHA_CURRENT_PROOF_MAP_V1_20260909.md)。

页数增补没有解除匿名、正常字号/行距/边距、全部必要证明在正文、冻结源、双新根确定性、引用与科学范围的其他约束。
没有重开已通过且输入未变的 69 件来源正式投票，没有重新评新意，没有另做外部文献检索。
本席只新写本报告，未改源、未编译、未编辑旧构建、未安装依赖、未上传或对外发送。

## 2. 本人全文源阅读与冻结身份

下表每项均从首行读至末行；总计 3486 行，而非仅查看差异或依赖旧版本阅读。

| V4 文件 | 行数 | 本次全文覆盖 |
|---|---:|---|
| main.tex | 62 | 版式、匿名、摘要、八节输入、正文末页标记及参考文献分界 |
| macros.tex | 9 | 记号与运算符定义 |
| references.bib | 183 | 全部 17 条书目信息、版本及 correction/title notes |
| sections/01-introduction.tex | 300 | 原矩阵、系数环、全部主定理、状态表、相关工作与边界 |
| sections/02-surface-pencil.tex | 446 | 八中心、完整四末端、极除子、常数与节点复形、完整 pencil |
| sections/03-spectral-jacobian.tex | 438 | 临界代数、完整谱图、实际模块、有理逆、无核与原域下降 |
| sections/04-closed-hasse.tex | 271 | 完整光滑闭纤维、同能量模型延拓、全曲线 Cartier/Hasse |
| sections/05-integral-trace.tex | 246 | 整数插入、秩二递推、唯一系数提取、全开曲面正则性 |
| sections/06-first-layer.tex | 397 | 实际 Bockstein、原 trace 同余、Taylor 商、像层类、完整首层理想 |
| sections/07-odd-jets.tex | 468 | odd 全时间 jet、内外块修正、weighted identity、全形式与截断理想 |
| sections/08-two-jets.tex | 666 | 二特征四块基式、特征四比较、两次局部整除、混合理想与状态 |

本人在 paper/v4/、r4/work/、r5/work/ 分别执行同一冻结列表的 sha256sum -c：十一项各自全部 OK，共 33 项通过。
校验列表 [SOURCE_V4_20260909.sha256](SOURCE_V4_20260909.sha256) 的 SHA-256 为 f57b18fdd0549183ec4250350158ffa721a82a351c15f3b4b792de51043655a9。
当前出版锁、V2 页数增补、V2 科学范围锁的本人实测哈希均与冻结 protocol 一致，未把旧 22–30 页窗口默默改写为通过。
该检查仅涉及当前指定源、副本及控制对象，没有扫描历史构建树。

## 3. 数学转写与结论范围审查

以下是对实际稿件所含论证及其锁定输入的审查，不把 PDF 生成成功当作数学证明，也不把本轮阅读说成重新审完外部原论文。

| 审核点 | 当前正文证据与判断 |
|---|---|
| 八中心和完整四末端 | §2 保留八次原替换及四条完整终端仿射线；极除子是 rD。有限纤维完整性、一般纤维光滑与“选定完整 scheme fiber 光滑”没有混为一谈。 |
| 任意特征有限临界代数 | Lemma 3.1 使用实际四次关系及逆代入；端点和总空间正则检查没有除以 2 或 3，没有通过判别式分母排除小特征。 |
| 原谱模块，而非相似方程 | Theorem 3.2 的实际矩阵给出族上线丛与有限推下；无标量点论证、循环向量和 Picard 族恢复均在正文。C 的亏格 2r−1 与原状态曲线的亏格没有混写。 |
| 原状态逆与不可分风险 | (3.9)–(3.11) 使用原矩阵最高项、次高 (1,2) 项及常数项恢复 x,y，并说明族上 gauge 不变比值；不只靠几何点单射排除隐藏纯不可分次数。 |
| 拉回无核与原域下降 | 完全固定点 P0、范数与 r 可逆给出实际 scheme-theoretic kernel 排除；不变切空间维数、整陪集、次数一和 K 上 torsor 下降连续衔接，未假设原曲线有 K 点。 |
| 闭纤维同能量认同 | Theorem 4.1 保留 complete scheme fiber 光滑前提；普通 henselization、局部 section、双方正则 proper flat minimal 模型、正反两延拓及稠密性均明确，保留 c=h 和所有末端点。 |
| 全曲线 Hasse | Proposition 4.2 检查有限分歧点及无穷端点的正则微分；奇素数系数公式和 p=2 的 H2=h 分开计算；Cartier 的 p 的逆半线性、系数 p 次根和几何零条件下降均保留。 |
| 整数先除后约化 | Lemma 5.1 与 §7 block insertion 在约化前完成整数除法；循环只旋转、不交换矩阵。全块公式不遗失内部 m 次插入，也不额外乘 m。 |
| 模幂剩余乘子与全图延拓 | §5 递推和支持区间证明 H 的 sigma 次幂；正则性由实际水平/垂直余维一与局部自由性延拓；非约化末端用 u 局部化单射，不借点集稠密性。 |
| 指定 J 的首层障碍 | Proposition 6.1 在原 L_m、原常数 section、固定节点复形和实际限制同构中计算，核是常数线；kappa_J 对每个完整光滑有限纤维非零，并非只对超奇异纤维。 |
| 像层目标与符号 | Proposition 6.4 的 nu 只在 Hasse-zero 光滑纤维构造；连接类在 H1(O_X^p)，Frobenius 是到像层的加性层同构。没有误称超奇异 H1(O_X) 上 Frobenius 可逆。 |
| 完整首层理想 | Theorem 6.5 使用法向 dJ 与处处非零 tangent coefficient 得到实际全理想 (pi,Htilde)，包括重根、四末端和普通纤维；不是只模 pi² 的结论。 |
| 奇素数全时间 jet | §7 的两个指定商 pi1, pia 均映到 epsilon，时间在整个商中匹配；明确区别自然分圆嵌入。内部 tame deformation、时间项和 dj_* 均保留。 |
| odd 全形式与 smooth-only 理想 | Theorem 7.1 在有限 residue k 下覆盖整个原开曲面且不要求能量光滑；Corollary 7.7 只在完整光滑有限纤维给精确截断理想，未升级为高阶全理想。 |
| 支持和独立系数提取 | §7 保留一般 m 的第五个 resonant degree；odd 的区间 [1,2p−1] 与二特征 [1,7] 分别给唯一首位。仅标量取 Frobenius 次幂，不对一形式取幂。 |
| 特征二与特征四 | §8.1 的 a≥2 商是特征二 dual numbers；§8.2 的 a=1 比较独立在特征四完成，先保留 2j dj=−pi1 j dj 再取剩余，未将两商等同。 |
| 原四块 mixed term | Theorem 8.1 从实际 determinant/state differential 及支持推出 beta4=T dJ+J² chi_m；不能由 odd 公式替换 p=2 得到，且保留完整时间 jet。 |
| chi_m 的限界及所有点两次整除 | chi_m 只先定义为 ambient torus form；Lemma 8.3 在每个原光滑纤维点的局部整环及其素 Cartier 理想 (J) 中两次应用素性与消去，证明 rho_i 正则并识别 tangent 为实际 nu，未假设 chi_m 全局 ambient 正则。 |
| mixed 理想两系数 | Theorem 8.4 保留法向 j^(N−1)+pi Ttilde j^(N−4) 与切向 pi j^(N−2)，任意 lift 变化被另一生成元吸收；普通纤维的单位理想另行核对。 |
| 长度五和原 base action | Corollary 8.5 是加上 pi2² 后的截断商，保留沿纤维变量 w，横截长度五而非闭点全 Artin 长度或全临界商长度；pi2 映到 z³/T，后续可容许非分歧扩域归一化 T。 |
| 状态准确值与下界 | Table 1 与 Corollary 8.6 一致：普通态原阶 a phi(p^a)；首层超奇异原阶 p；(p,a)=(2,2) 原阶 5；其余所述高层只给 ≥a phi(p^a)+2。只容许指定有限非分歧扩张，不扩大到额外分歧态。 |
| 非零剩余与厚度限界 | 末段明确高层逐态下界不等于全曲面形式被 pi² 整除；不声称完整高阶理想、未得的精确高阶超奇异阶或奇异能量理想。 |

V1 的 perfect-k 首层范围、V2 的 finite-k odd 几何比较、V3 的 perfect-k 代数与 finite-k 几何范围在引言和各节保持区分。
所有上述必要证明在 §§2–8 的正文；本稿没有把 actual Jacobian、闭 Hasse、四末端延拓或两次局部整除藏入附录，也没有将这些原对象的实质论证替换为条件未核的外部“标准”黑箱。
本轮未发现需要定向回到原材料才能解决的新转写疑点，故未重开不变的来源审查。

## 4. 本人逐页实际 PDF 阅读记录

本人实际打开 r4/inspection/page-01.png 至 page-41.png 每一张 110 dpi 单页图像，包括全部参考文献；没有以缩略拼图或抽样替代。
图像来自记录所述对冻结 r4 PDF 的 pdftoppm 渲染；本次 r4 文件身份实测见 §5。
每页均核读实际内容、页码、数学上下标/分式、边距、断页、字符及相邻内容连续性。下表记录逐页覆盖，不是由源长度反推页数。

| 实际页 | 本人覆盖与页面判断 |
|---:|---|
| 1 | Anonymous 标题、完整摘要、引言和原映射；标题与正文层次正常，无署名泄露。 |
| 2 | 原矩阵 (1.1)、trace/determinant、分圆系数环与 Hasse 设置；矩阵和长式可读。 |
| 3 | Theorems 1.1–1.3 的全理想/截断理想、像层与 mixed 商；公式均在边距内。 |
| 4 | Table 1 的准确值/下界以及相关工作；表格、列映射和文献比较清楚。 |
| 5 | 引言限界结束；§2 原八中心终端图 (2.1) 与 Proposition 2.1，无内容被挤出。 |
| 6 | 辛形式末端表达、极性输入及 Lemma 2.2；分式和证明连续。 |
| 7 | 八次 boundary valuation/transport 表及四实际 terminal maps；整表完整、不裁切。 |
| 8 | 极性证明末段、Lemma 2.3 常数与节点 frames；行列和符号可辨。 |
| 9 | 节点 unit ratios、含特征四的 boundary complex、Theorem 2.4 与 Stein 分解。 |
| 10 | 小特征 generic smoothness、完整 pencil 与 §3 入口，段落和证明终止清楚。 |
| 11 | §3.1 四次临界代数及 scheme-level 逆代入；所有 2、3 系数和单位条件可辨。 |
| 12 | §3.2 两个完整谱图、四端点、有限推下、C/E 亏格与商。 |
| 13 | Theorem 3.2、族上实际谱模块、line-bundle pushdown 与 constant conjugacy 恢复。 |
| 14 | 原状态逆、族上比值、Picard difference；M(sz)A(z)=A(z)M(z) 独立显示正常。 |
| 15 | 实际无核、不变群分量、整陪集及 K 上 torsor/Jacobian 下降，完整证明结束。 |
| 16 | §4 完整光滑 scheme fiber 和 henselian base/models，页末句子正常续页。 |
| 17 | 局部 section、minimal-model 正反延拓、同能量全模型同构及完整 Hasse 命题。 |
| 18 | 全曲线 differential 正则、Cartier 约定、odd/p=2 独立计算及几何零条件下降。 |
| 19 | 两个 state differential 方向；§5 integral insertion 和剩余 block 入口。 |
| 20 | 剩余 insertion、秩二递推、coefficient formula 与 residue multiplier 证明；长式正常。 |
| 21 | 唯一 digit coefficient、全开曲面正则延拓、非约化 restriction lemma。 |
| 22 | 剩余理想/全曲面 generic order；§6 原 boundary Bockstein、特征四区别及 proposition。 |
| 23 | 原节点复形、Bockstein 计算、实际 restriction、prime-trace 设置；跨页常数陈述未失条件。 |
| 24 | 原 prime trace congruence、cyclic word phase、非 resonant 返回与 Taylor quotient。 |
| 25 | ramified Taylor 整数商、全图 G_i、实际像层 tangent class 及局部形式。 |
| 26 | Frobenius 到像层、全曲线 nonvanishing、完整首层理想与状态阶；§7 入口。 |
| 27 | finite-k odd common quotient、完整时间匹配、非自然嵌入及全开曲面 factorization。 |
| 28 | integral block insertion、系数 projection、完整 internal deformation 及 deformed trace。 |
| 29 | nonresonant square-zero 消去、内部 coefficient factorization、weighted operator 入口。 |
| 30 | weighted commutator 证明、external corrections 与实际 support cases；区间排版清楚。 |
| 31 | 第五 resonant degree、唯一 digit extraction、全图 gluing 与 odd 截断理想陈述。 |
| 32 | odd 截断理想证明及“只下界”限界；§8 二特征实际 torus forms。 |
| 33 | Theorem 8.1、正确二特征 common quotient、内部 deformation 与四块基式。 |
| 34 | 二特征内部项、weighted commutator、[1,7] binary selection 与所有高块数。 |
| 35 | 实际 four-block coefficient、state-constant determinant 前提及四末端乘子 gluing。 |
| 36 | 特征四首层比较、两条 alpha 表达和保留整数 2 的实际符号计算。 |
| 37 | 实际 nu 认同、local difference quotients、Lemma 8.3 所有点的两次素性整除。 |
| 38 | mixed ideal 任意 lift、法向/切向系数消去、截断 quotient 与横截长度五证明。 |
| 39 | w 和 base action 限界、T 可归一化、Corollary 8.6 全证明及最终范围限界；正文实际结束。 |
| 40 | References 标题和条目 [1]–[13]；数学题名、重音、DOI/URL 换行正常，无正文证明。 |
| 41 | 条目 [14]–[17]、版本及题名差异 notes、最后页码；短参考文献尾页为自然结束。 |

逐页未发现裁切、重叠、缺字、挤压边距、空白正文填充或需要缩字号才能读的内容；公式、表格及正常跨页续句均可读。
本文使用正常 11pt article、letter、一英寸边距和正常行距；没有为新窗口进行全局版式收缩，也没有附录。
实际计数为 39 页实质正文 + 2 页参考文献，满足仅对 P30 生效的 22–40 页正文窗口；不是旧 22–30 页合同下的 PASS。

## 5. 本人实际检查与构建证据归属

| 检查 | 本次实际结果 |
|---|---|
| r4 / r5 PDF 文件大小 | 两者均为 546617 bytes |
| r4 / r5 PDF SHA-256 | 两者均为 40f05a156cbedc16a881b090a19af299c12c41a1fd9fb62a0290406a83737007 |
| r4 与 r5 直接 cmp | exit 0，逐字节相同，不只是渲染近似 |
| pdfinfo | 41 页；612×792 pt letter；PDF 1.5；Author 空；无加密、表单或 JavaScript |
| 两个 main.aux | LastBodyPage=39；绝对末页=41 |
| 本人 pdftotext 39–41 + 实际图像 | 最后证明/限界止于 39；References 始于 40、止于 41 |
| 两根最终 main.log / main.blg | 定向检查未匹配 LaTeX/BibTeX warnings、over/underfull、缺字、未定义或实际 rerun 要求；rg exit 1 表示无匹配 |
| r4 main.blg 全文读取 | 使用 17 entries；warning 调用数 0 |
| PDF 全文未解标记检查 | pdftotext 后无 ?? 或 [?] 匹配；rg exit 1 表示无匹配 |
| pdffonts | 23 个 Type 1 字体资源均 embedded/subset/Unicode=yes |
| 原源与两副本校验 | 同一冻结列表的 33 项均 OK，见 §2 |

根代理实际执行的“两个预先不存在的新根、各严格四过程、八个退出码 0、无额外 convergence pass”等过程证据，取自冻结 protocol 及 [双根结果](V4_TWO_ROOT_AND_ROOT_PDF_RESULT_V1_20260909.md)。
本席没有重跑编译来制造第二套过程证据；独立完成的是当前产物身份、指定日志诊断、源副本校验以及完整实际稿件/PDF读取。

本次按 academic-research-suite 的稿件审查路由采用证据定位、正文完整性与 PDF 结构预检；用户指定单席/不重新评分的范围优先于默认多席或评分模板。
该技能的 pdf_read_preflight.py 在 2026-09-09 12:59:24 UTC 对当前 r4 PDF 实际运行，但返回 UNAVAILABLE，原因 pypdf-not-installed；摘要中的 PDF hash 与上述身份一致。
其 exit 0 只表示产生了该 verdict，不表示结构预检 PASS；未安装依赖，未伪造脚本成功。当前实际页数/结构由已运行的 pdfinfo、aux、pdftotext 和本人全页观看交叉核对。
没有虚构期刊标准校准或数值置信度；技能附带的外部评分校准在本次为 NOT_CALIBRATED，不用于本稿验收加分。

## 6. 引用一致性与未关闭的旧来源缺口

本人全文读 references.bib，并将正文实际用途和第 40–41 页全部 17 条引用与现行 CITATION_RECORDS 对照；没有把该对照说成新读了十七篇外部原论文。
Achter–Howe 使用已记录的 v5 订正版及 §2.5 半线性警示；书目明确 corrected author version。
Vlasenko 2024 保留官方元数据题名，并说明正文题名次序不同；Shimada 2026 明列 arXiv 预印本，未升级为刊本。
Vlasenko 2018 明确使用原作者 v3 作 related-work 比较，其模 p 迭代与形式群陈述没有变成本稿必要证明黑箱。
该条可能勘误的一手内容缺口仍是 CORRECTION_IMPACT_UNKNOWN：本报告不声称勘误无影响，也不反向断言原版全部结论失效。
Beauville 原正文未新完成阅读的缺口、IVY 的适用条件及 citation record 其他旧阅读限制保持原状态；实际矩阵/端点/推下/有理逆/下降在本稿自证，不借这些缺口冒充已复核。
原 trace/Hasse 标准机制和已知谱 Picard 框架在引言有实质归属与范围说明；本轮不产生“没有人做过”的全局新意结论。
没有看到缺引、未解引文、虚构本文定理编号或把旧来源 gap 写成已通过的新转写问题。

## 7. 问题清单与处置

| 项目 | 状态 | 对当前结论的影响 |
|---|---|---|
| 新的科学范围/转写/必要证明遗漏 | 未发现 | 无需本轮修源 |
| 新的实际 PDF 可读性或页数违规 | 未发现 | 当前 39+2 在有效窗口内 |
| 技能结构脚本缺 pypdf | UNAVAILABLE，如实保留 | 不冒称该脚本通过；实际完整 PDF 检查已用现成只读工具与全页读取完成 |
| Vlasenko 勘误及其他既有来源限制 | 原状态未关闭 | 不能拿本报告扩大外部证明审计或改成新意无条件通过；当前正文不依赖其作未自证黑箱 |
| 后续最终完整性/本地验收与批次状态 | 不由本席授予 | 留给已授权后续流程；本报告不自行更新 README、验收、批次或启动 Paper31 |

最终结论仍为 PASS_CURRENT_CONTRACT_MANUSCRIPT_PDF，限定于上列冻结 V4 与精确 SHA 的 r4/r5 实际产物。
本席未提出为了凑审查问题而修改稿件的建议；若源或 PDF 改变，本报告不自动覆盖新产物。
本报告写成后由本人全文自读核对再交付终态 SHA，并停止写入；没有修改其他项目文件。
