# R4 arithmetic：来源先行记录

2026-09-08 UTC。本文件首版与 LG4 合同同时落盘；首版所列访问均在冻结前
实际完成，冻结后新增核查已单列。ARS-Codex 仅用作已确定主张的
source fact-check，不开启另一条完整研究/写作流程。

## 主来源与适用边界

| 来源 | 实际读取范围 | 拥有或排除的主张 |
| --- | --- | --- |
| Dan Segal, [Some aspects of profinite group theory](https://www.math.auckland.ac.nz/~obrien/segal-survey.pdf), Chapter 7, Theorem 7.2.3 | PDF 开篇及 §7.2.2–7.2.6 定理/说明，非整本 66 页通读；更早原始书籍证明未重读 | virtually polycyclic 自同构群作用在 virtually polycyclic 群上的轨道闭性。应用于 \(\mathbb Z^r\) 与单个整可逆矩阵是原定理直接范围；不拥有一般非线性平面轨道 |
| E. Amerik, P. Kurlberg, K. D. Nguyen, A. Towsley, B. Viray, J. F. Voloch, [Evidence for the dynamical Brauer–Manin criterion, v2](https://arxiv.org/pdf/1305.4398v2) | arXiv metadata、摘要/引言、Theorems 4.2–4.4 的完整陈述，§4.4–4.6，包括 Proposition 4.16 和 4.17 的论证；也读到 §4.3 的 uniformization 替代证明；不是全部 §2–§4.3 通读 | étale invariant/preperiodic 目标的局部避免；前驱点导致正向假局部全局。不能取消目标条件用于游荡单点；本文编号固定用 v2，避免与出版版混用 |
| Bjorn Poonen, [p-adic interpolation of iterates](https://math.mit.edu/~poonen/papers/p-iteration.pdf) | 3 页 PDF 全文，包括唯一主定理证明、Remarks 2–4、参考文献 | 系数意义 \(f\equiv\mathrm{id}\pmod{p^c}\)、\(c>1/(p-1)\) 时的 Mahler 插值。不是任意逐点 mod \(p\) 恒等即可直接插值；\(p=2\) 阈值不可省略 |

## 本地检索与初筛范围

已读根与 henon 子目录指令、第四轮 PLAN、批次 skill/workflow，以及
当前状态最新段；不是整库逐文审查。`rg` 在 henon 的 Markdown/TeX
中检索 bad reduction、p-adic、primitive/Zsigmondy、ramification、
orbit separability、profinite orbit、dynamical Hasse/Brauer–Manin 等相关词。
碰撞包括 C394 局部 \(p\)-进流、C393 arboreal、C179 单位乘法
Zsigmondy、C389 Carlitz；本轮不重开这些辅助材料。更早算术 scout
已有 torus/power-map translate 的 Hsia–Silverman 所有权记录。

冻结前完成五组共 19 个网页检索查询，覆盖 Hénon 坏约化/2-adic/
ramification/Zsigmondy、polynomial automorphism profinite orbit、
congruence orbit、two-sided dynamical Brauer–Manin、dynamical Hasse
point étale、Segal profinite orbit 和 Poonen 插值。其中仅第 8 条查询
限制近 180 天，另含 2025/2026 字样查询；
不把少量检索称为文献全覆盖。
初次大批工具返回有截断，未显示的内容不计已读。固定有限域上的
“profinite polynomial automorphism group”搜索命中属于另一种完成化，
仅作检索线索，未引用其证明。冻结后又做两组共 8 条窄范围查询，
共计 27 条，不因数量目标增加查询。精确字串如下。

## 可复现的实际网页查询记录

均为 2026-09-08 UTC 的实际调用；只列本轮算术，不混入此前 NG2-F
评审查询。除第 8 条外没有 recency 参数，也没有 domains 限制。
各组返回长度为 long。网页结果会随时间变化，本表只保证查询字串
和当次选用过滤器可复现，不保证重搜得到同一排名。

| 序号 | 阶段/组 | 原样查询字串 | 额外过滤 |
| --- | --- | --- | --- |
| 1 | 冻结前 A | "Hénon" "bad reduction" arithmetic periodic points 2025 2026 | 无 |
| 2 | 冻结前 A | "Hénon" "2-adic" dynamics | 无 |
| 3 | 冻结前 A | "Henon" "ramification" periodic points | 无 |
| 4 | 冻结前 A | "Hénon" "Zsigmondy" | 无 |
| 5 | 冻结前 B | "polynomial automorphism" "orbit" "profinite" | 无 |
| 6 | 冻结前 B | "dynamical" "Brauer-Manin" "Hénon" | 无 |
| 7 | 冻结前 B | "orbit" "congruence" "polynomial automorphism" | 无 |
| 8 | 冻结前 B | "Hénon" "local-global" orbit | recency = 180 天 |
| 9 | 冻结前 C | "Evidence for the dynamical Brauer-Manin criterion" | 无 |
| 10 | 冻结前 C | "polynomial automorphisms" "local-global" "orbits" | 无 |
| 11 | 冻结前 C | "orbit closure" "profinite" "polynomial" | 无 |
| 12 | 冻结前 C | "dynamical Hasse principle" "point" "étale" | 无 |
| 13 | 冻结前 D | "two-sided" "orbit" "Brauer-Manin" | 无 |
| 14 | 冻结前 D | "Henon" "orbit" "separation" arithmetic | 无 |
| 15 | 冻结前 D | "polynomial" "orbit problem" "modulo" | 无 |
| 16 | 冻结前 D | "orbit" "closed in the profinite topology" automorphism | 无 |
| 17 | 冻结前 E | "Poonen" "p-adic interpolation of iterates" pdf | 无 |
| 18 | 冻结前 E | "polynomial automorphism" "congruence" orbit separability 2025 2026 | 无 |
| 19 | 冻结前 E | "Hénon" "Brauer–Manin" | 无 |
| 20 | 冻结后 F | "polynomial automorphisms" "profinite" "orbits" | 无 |
| 21 | 冻结后 F | "Hénon" "congruence" "orbit" | 无 |
| 22 | 冻结后 F | "two-sided" "dynamical" "Hasse" | 无 |
| 23 | 冻结后 F | "integral" "orbit separability" polynomial | 无 |
| 24 | 冻结后 G | "polynomial automorphism" "local-global principle" orbit | 无 |
| 25 | 冻结后 G | "Hénon maps" "Brauer" "Manin" | 无 |
| 26 | 冻结后 G | "orbits" "closed" "congruence topology" polynomial | 无 |
| 27 | 冻结后 G | "dynamical Hasse" "automorphisms" "affine" | 无 |

F–G 没有找到可直接适用的全非线性 LG4 主定理或反例。若干结果是
书目、无关算术群同余拓扑或固定有限域自同构，不凭关键词相似
转移结论。没有从“未检索到”推断一般 LG4 是开放问题或作者首创。

## 本地相邻所有权及证明使用清单

实际读取 C394 的 THEOREM_PACKAGE、SOURCE_AUDIT 及 ANALYTIC_PROOF：
证明曾因合并输出截断，冻结后另分 1–115 与 116–EOF 补齐；
不把未显示的初次输出计作完整读取。
对应路径是
[C394 原证明](../../../henon_padic_symplectic_analytic_interpolation_route_a/proof/ANALYTIC_PROOF.md)；
该相对链接只用于本地定位，文献所有权仍以其指向的主来源为界。

LG4 证明包的引理 1–2 不调用来源中的未重证分析定理，而是给出
自足的有限迭代赋值计算；辅助定理 A 则直接给完整逆极限/零核证明。
这不免除实质性扣除：局部 near-identity、周期增长与 adding-machine
均属已知机制。辅助定理 B 唯一非初等外部依赖是 Segal Theorem
7.2.3(i)，其适用对象与 congruence/profinite 拓扑等价逐项核实。
AKNTVV 与 Poonen 用来核对所有权和禁止误套，未被冒称为 LG4 的
完整证明。没有重审这些论文每个不相关分支或所有参考文献。

当前没有 Zotero/Obsidian/arXiv/Semantic Scholar 专用工具；使用网页
访问主来源，没有声称运行专用数据库。没有向外部模型上传本地资料，
没有付费 API、GPU、TeX、正式评价或 Git 写入。

## 准入边界

本轮来源状态只是有界的适用范围核查，不是“全球首创”认证。
LG4 全量词是否成立仍待数学裁决；已知局部桥和经典线性化不能
折算新独立完整合同。`NO_BAD_EULER_OR_ROOT_NUMBER`。
