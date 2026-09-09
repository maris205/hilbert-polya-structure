# R6 算术线：原始来源、实际访问与所有权审计

访问日期均为 **2026-09-09 UTC**。这里区分实际读到的正文、
元数据、失败访问和未读部分；检索没有发现某项定理不等于
全球不存在。最终 R6-IH 证明不依赖未读外文定理。

## 1. 工作流与本地碰撞

本轮按仓库 `henon-route-a-batch` 与 workflow 执行完整合同门，
结合 `research-lit → idea-creator → proof-writer`。ARS 只采用
有界事实核验的来源质量、论证、交叉验证与失败回退指导，
不启动额外研究到论文流水线。当前团队覆盖旧技能中的外部
GPT/MCP/GPU 模板；没有付费 API、稿件外传或 GPU 工作。

实际工具目录未提供 Zotero、Obsidian、arXiv 或 Semantic
Scholar 连接；本地知识库入口未给出可用专门库，使用仓库
材料与普通 web 原始来源回退。不据此声称这些服务本身无内容。

本地 `rg` 检查了三项登记入口：

- `henon_dynamics/docs/candidate_registry.md`；
- `henon_dynamics/docs/obstruction_registry.md`；
- `henon_dynamics/next_paper_henon_candidate_search/CANDIDATE_REGISTRY.md`；

并窄查本批目录内 `Pezda`、整数系数、任意次数、全次数、
universal period、reversor、twist、Galois、primitive divisor 等
相应词。早期一次宽搜索输出截断；不把列出的所有文件视为
已读。本轮实际核对的最近数学所有者包括：

| 本地来源与实际读取 | 扣除内容与本题区别 |
|---|---|
| C412 `continuation_c409_c413_round2/papers/C412_integer_henon/main.tex` 的入口，以及 `sections/1_introduction.tex` 前 130 行 | 首一整系数二次、Jacobian +1 的全部有理周期点，精确参数表，周期 1,2,3,4，最多八点。它不包含所有首项系数、所有次数或 Jacobian −1。 |
| C417 `continuation_c414_c418_round2/cubic_arithmetic/PROOF_PACKAGE.md` 前 190 行及后续关键词定位；其中前 110 行又复核 | 首一整系数三次、Jacobian +1 的完整有理周期点表，周期 1,2,3,4,6，最多十一点。其割线余项是单个首一线性因子；端点图方法和小周期见证明确扣除。未声称本轮重读后半部分的全部旧证明。 |
| 本批 `arithmetic_maps/SCOUT_REPORT.md` 120–175 行及已有登记状态 | AM1 处理整值但非整系数的二次正规形，存在原生五周期；不能把整数格保持性误当成整系数性。旧 scout 中的当时未闭合标签不覆盖根节点后来已准入的 AM1 状态。 |
| 本批第五轮决定、第四轮 LG4 登记和来源索引的关键词命中 | 一般整系数自同构的同余闭包、经典统一周期上界及 GR5 好模型均已扣除；本题不重开这些合同。 |

R6-IH 的候选增量是任意整系数单因子 Hénon、全部次数和两个
符号的精确周期谱，以及不依赖三次余项只有一个根的全族
整数余项同余约化。不是新的 Pezda 上界、低次例子、插值
引理或有限图分解。是否达到独立合同实质门须由非作者审查。

## 2. 最近公开原始来源

| 原始来源 | 实际访问强度 | 已核实的所有权／限制 |
|---|---|---|
| T. Pezda, *On cycles and orbits of polynomial mappings Z²→Z²*, Acta Math. Inform. Univ. Ostraviensis 10(1) (2002), 95–102；[期刊数字库记录](https://dml.cz/handle/10338.dmlcz/120574) | 记录全文已读。浏览器 PDF 及代理失败；一次只读 `curl` 管道到 `pdftotext - -` 成功，读封面、定义、Theorems 2.1–2.2、Propositions 3.1/3.3/3.4 与 3.5 起始，流式文本前 190 行。未保存 PDF，未声称全文证明或页图检查。 | Theorem 2.1 的一般整系数二维周期全集为 `{1,2,3,4,6,8,9,12,16,18,24}`。系数属于 Z，不只是函数在 Z 上取整数值。统一有界性完全是已有内容。本题证明直接排除而不借用其上界。 |
| Kim–Krieger–Postolache–Szeto, *Hénon maps with many rational periodic points*；[arXiv v2](https://arxiv.org/html/2412.01668v2)，[版本记录](https://arxiv.org/abs/2412.01668) | 摘要与版本记录；HTML 引言全文、Theorems A–B、§2.2 定义及 Lemma 2.1 全证明；§5 的 Theorem 5.1 与证明正文已读。也实际读到部分其他定位段落，不声称 689 行全部核验。 | v1 为 2024-12-02，v2 为 2025-07-08；HTML 的 2026-08-24 Date 不当成新版本。构造使用有理系数整值 `s_d`，非 Z[t] 全族。其任意长整数循环不反驳本题；其广义有理系数问题也不被本题解决。未核实期刊发表版本。 |
| *Hénon maps: a list of open problems*, §11（P. Ingram 的算术问题）；[期刊正文](https://armj.math.stonybrook.edu/html-articles/Files-2015-2024/23-70/index.html) | 实际读取 §11 全部正文（浏览器约 714–802 行），含 Questions 46–47、Conjectures 2–5 及 Hénon divisibility sequence 定义；参考文献只用于定位，不视为相应论文已读。 | Conjecture 3 是 Q 上 `F=(y,y²+c+x)` 的有理点问题，Jacobian −1；虽然预测周期名单相同，本题仅整系数/整点而不限次数，不解决其有理系数断言。原生 Hénon gcd 返回理想已明确有定义与研究问题所有权。 |
| Cantat–Dujardin, *Holomorphically conjugate polynomial automorphisms of C² are polynomially conjugate*；[作者预印本 v1](https://arxiv.org/html/2403.19621v1)，[出版 DOI](https://doi.org/10.1112/blms.13164) | 预印本主文约 27–174 行已读；出版页只核元数据。预印本 v1 上传 2024-03-28，HTML 重绘日期不当成新版本。 | 代数闭包上的共轭可降到有限扩张及显式次数界；主文已举 `f=(y,x+y^(m+1))` 与 `g=(y,x+D y^(m+1))` 的非平凡幂扭曲。因此不将该例或直接 Kummer 延伸冻结为第二题。 |
| Gómez–Meiss, *Reversors and symmetries for polynomial automorphisms of the plane*, Nonlinearity 17 (2004), 975–1000；[作者 PDF](https://amath.colorado.edu/faculty/jdm/papers/Reversors.pdf)，[arXiv](https://arxiv.org/abs/nlin/0304035) | 作者 PDF §2.4，Theorem 7 与完整证明、Proposition 8 与证明、Corollary 9、Lemma 10 与证明，约 PDF 文本 306–550 行。未读完全部 26 页。 | 普通多项式对称/反演分类有直接所有权；单因子公共缩放根群也不是新机制。 |
| Baake–Roberts, *Symmetries and reversing symmetries of polynomial automorphisms of the plane*, Nonlinearity 18 (2005), 791–816；[arXiv v1 PDF](https://arxiv.org/pdf/math/0501151)，[DOI](https://doi.org/10.1088/0951-7715/18/2/017) | UNSW 作者副本访问失败，转 arXiv PDF；读引言与定义、Lemma 5、§5 Lemma 6、Theorems 4–5 及对应证明、Corollary 3 起始，约文本 1039–1202 行。未读完全部 27 页。 | 任意域的反演阶数/根单位限制是经典内容。普通 reversor 候选不冻结。 |

表中定理适用性依据数学假设判断，不套用医学试验的证据等级。
作者稿与期刊记录分开标记。除实际读到的 Kim 等致谢外，
未独立调查各论文利益冲突、撤稿或期刊信誉；不暗示这些项目
已经专门审查。搜索结果中的二手转载、维基、论坛和不相关
数值 Hénon 文本没有用作数学证明来源。

## 3. 冻结前预筛及停止记录

| 预筛方向 | 结论 | 是否冻结／运行数学程序 |
|---|---|---|
| 单因子 Hénon 的域下降／幂扭曲 | 已有具体幂扭曲所有者；单因子公共缩放群的 Kummer 分类很可能只是短推论，未建立独立新整类机制 | 否／否 |
| 任意域普通 polynomial reversor | Baake–Roberts 与 Gómez–Meiss 有直接全族入口 | 否／否 |
| 整数轨道 gcd 返回序列的原始素因子 | 返回理想及 divisibility 已有定义；坐标高度增长不提供 gcd 的下界，无法直接套单变量 Zsigmondy 论证 | 否／否 |
| 全次数整系数、双符号 Hénon 整点周期谱 R6-IH | 扣除 Pezda 和本地低次后，冻结完整精确谱；作者证明包覆盖全部次数/坐标直径，等待非作者审查 | 是／冻结后两次 |

没有用前三个预筛方向填第二项名额，也未把未闭合 gcd 思路
写成不可能性定理。搜索缺失不支撑全球新颖性断言。

## 4. 实际检索账本

以下 1–27 在冻结前执行，28–30 是证明完成后的最近来源
反查。全部为普通 web 查询，无域过滤、无 recency 过滤；
相关原始页随后直接打开。引号和排除词按实际查询保留。

1. `Hénon polynomial automorphism integer periodic points arbitrary degree periods`
2. `Hénon maps twists Galois descent polynomial conjugacy number fields`
3. `Hénon primitive prime divisors orbit divisibility arithmetic`
4. `Hénon reversors symmetry arbitrary field arithmetic classification`
5. `"Hénon" "integer" "periods" polynomial`
6. `"Hénon" "Galois" "conjugate" Cantat`
7. `"polynomial automorphisms" "reversors" field`
8. `"Holomorphically conjugate polynomial automorphisms" arxiv`
9. `"Symmetries and reversing symmetries" "Baake" "Roberts" arxiv`
10. `"Hénon" "twists"`
11. `"Hénon" "field of moduli"`
12. `"polynomial automorphisms" "Galois cohomology"`
13. `"Hénon" "primitive prime"`
14. `Pezda polynomial automorphisms Z2 periods cycles integer plane`
15. `"polynomial mappings" "Z2" "cycles"`
16. `"Hénon" "Pezda"`
17. `"Hénon" "integer coefficients" "period"`
18. `"Henon" "integral coefficients" cycles`
19. `"polynomial automorphism" "integer" "period 8"`
20. `"Hénon" "integer" "periods" "polynomial" -potential -quantum`
21. `"polynomial automorphisms" "Z" "periods" Pezda`
22. `"Hénon" "integral periodic" arbitrary degree`
23. `"Henon" "period 24"`
24. `"Hénon maps" "integral" "Pezda"`
25. `"cycles" "polynomial automorphisms" "integers"`
26. `"Henon" "integral points" "periods"`
27. `"polynomial automorphism" "integer lattice" periodic`
28. `"Hénon" "integer coefficients" "8"`
29. `"Henon" "integral" "6" "Pezda"`
30. `"generalized Hénon" "periods" "integers"`

直接 open/find/click、只读 PDF 文本流与本地 `rg` 是访问和
碰撞检查，不列为新的数学运行。两次实际数学程序见
`RUN_LOG.md`；全批计数仅由协调者更新。
