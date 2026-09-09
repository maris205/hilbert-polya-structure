# NG2-V 第六轮：实际来源与所有权扣除

2026-09-09 UTC，协调者作者。来源核验采用 ARS 的有界 fact-check
规则与 `research-lit` 本地优先／web 回退；不是系统综述、全球
新颖性认证或人类阅读声明。下列判断区分公开原文、既有本地
证明和本轮手推。没有向外部模型上传稿件。

## 1. 本地输入与本轮增量边界

| 输入 | 实际阅读与适用性 | 扣除 |
|---|---|---|
| R5 `nonlinear_geometry/FROZEN_QUESTIONS.md`、`PROOF_AND_GAPS.md` | 本轮全文；原对象全 $n,a,D$，原剩余域为混合零通道 | 无零高度 $A+4$、经典 $L_n$ 已完成，不算新增 |
| R4 `nonlinear_geometry/PROOF_PACKAGE.md` | 本轮全文 | V4-H 逐层判定和 V4-Z 全零更新乘积子域已完成 |
| R2 `nonlinear_geometry/PROOF_AND_GAPS.md` | 本轮全文 | 原高维差分方程与 cancelling-sum 障碍，不冒称本轮发现 |
| C421 `IR1_PROOF.md`，已发布 supplement 路径 | 本轮分两段全文到 EOF | 三维 scalar 全分类、有限认证与所有仿射字均已有；不重跑 |
| 本批与前批相关 Markdown 的 `semi.?linear/半线性/nonzero block/非零块` 定向检索 | 命中旧 char-$p$ 的系数半线性与本轮文件；不是全仓库历史审计 | 正特征系数半线性与此处 Presburger 半线性不是同一对象 |

本轮研究增量被明确限于：把内部窗口估计局部化到每个非零块，
证明全部大非零块恰长 $n$ 且内部全为单位；据此将原全域周期
方程确切化为有限多个整数线性系统。后续锥生成、最小周期分层
和源 zeta 是所需完整合同的经典有效收尾，不拆篇。

## 2. 核心公开原始来源

### W：Junho Peter Whang，2023 预印本

[On periodic orbits of polynomial maps，arXiv v3](https://arxiv.org/abs/2305.13529)
及其 [原文 HTML](https://arxiv.org/html/2305.13529v3)。
元数据明确 v1 为 2023-05-22、v3 为 2023-09-08；HTML 的
`Date: August 24, 2026` 是渲染页面日期，不作为新版本或发表年。
本轮读完 §1–2（含 Theorems 1.1–1.4、Proposition 2.2、
Theorem 2.3 及全部证明），还核读其参考文献表。

它证明整点有限轨道的有效统一界及给定点的周期可判定性，覆盖
任意整多项式映射集，比本题所用经典周期上界更一般。该源没有
给本题整周期集合的完整半线性参数化；这一区分来自所读定理
的实际结论，不来自搜索不到某个词。本文不将统一界或逐输入
判定作为新贡献。未核定后续期刊版本或独立期刊审稿状态。

### H：Hengnan Hu、Ser Peow Tan、Ying Zhang，2015 预印本

[Polynomial automorphisms of C^n preserving the Markoff-Hurwitz polynomial](https://arxiv.org/abs/1501.06955)，
[v2 原文 HTML](https://arxiv.org/html/1501.06955v2)。
元数据 v2 为 2015-05-06；最初尝试不存在的 v3 HTML 返回错误，
随后从元数据纠正到 v2，没有把失败访问计作正文阅读。
本轮读元数据／摘要、Theorem 1.1 所示完整群对象、§2.6 dihedral
定义，以及 Lemma 2.2 的 fork 主张与相关推导片段；此前 R4
所需 fork 证明已在当时实际核读，本轮不声称重读全 1205 行。

原对象为无 forcing 的 Markoff–Hurwitz 多项式和整个生成群；
两零 dihedral 支撑及小乘积 fork 均是应扣除的背景。本文不把
完整群轨道替代固定原生循环词，也不把没有 `periodic` 文本命中
当作全球未研究的证据。未核定期刊版本或全篇来源优先权。

### G：Seymour Ginsburg、Edwin H. Spanier，1966

[Semigroups, Presburger formulas, and languages，出版社原 PDF](https://msp.org/pjm/1966/16-2/pjm-v16-n2-p09-p.pdf)，
Pacific Journal of Mathematics 16(2), 285–296，
[DOI](https://doi.org/10.2140/pjm.1966.16.285)。
实际打开出版社 PDF，读取题名、作者、卷期与 §1 pp.285–289，
包括 Theorems 1.1–1.3 的表述、半线性／Presburger 有效转换及
Theorem 1.3 的证明；未声称读取 §2 的语言论全部证明。
单独 HTML 猜测路径访问失败，PDF 正文访问成功；这是 web
PDF，不是本地 PDF 页锚，因此没有虚报本地结构 preflight。

该原始论文明确拥有半线性集合的布尔／投影闭包、Presburger
可判定性与有效转换。本文 §4 的非负线性系统有限生成是这一
经典范围，以有理锥取整给自足实现；不是本轮新算术结构。
出版社正文证实书目存在；未额外核查 COPE、利益冲突或撤稿库，
不把这些未做的项目标 PASS。

## 3. 实际新查询账

以下 15 个查询本轮均实际发送，非计划清单。大多只返回无关
结果；仅上节列出的原始正文作为研究支撑。搜索引擎的抓取时间
不充当论文日期。

1. `"Markoff Hurwitz" "periodic" "zero"`
2. `"Vieta" "periodic points" "integer" higher dimensional`
3. `"Markoff" "additive" "periodic" automorphism`
4. `site:arxiv.org Markoff Hurwitz polynomial dynamics periodic orbits zero`
5. `site:arxiv.org "Markoff-Hurwitz" "fork"`
6. `"Hurwitz" "periodic" "Vieta involutions"`
7. `"Gordan lemma" "polyhedral cone" "lattice points" pdf`
8. `"integer points" "polyhedron" "finite union" "linear sets" Ginsburg Spanier`
9. `"Markoff-Hurwitz" "semilinear" periodic`
10. `"Semigroups, Presburger formulas, and languages" Ginsburg Spanier`
11. `"Toric Varieties" Cox Little Schenck "Gordan" pdf`
12. `"periodic points" "Markoff-Hurwitz" semilinear integral`
13. `"integer periodic points" "semilinear" polynomial`
14. `"Markoff" "nonzero blocks" recurrence`
15. `"Hurwitz" "x_n" "periodic" integer recurrence`

本轮工具调用中另有 `open/find`，它们不是新的搜索式，不混入查询数。
浏览命中的 Bristol 教学笔记、Stanford thesis、Hemmecke thesis
与诸多聚合页面未用作新增定理的原始来源；Gordan 经典机制的
证明已自足给出，最近所有权以 G 的原文扣除。

## 4. 科学裁决边界

源 W、G 的一般理论和源 H 的既有群作用背景是必要扣除；它们
没有被包装成三个新增结果。作者目前提出的是一个整合的原
NG2-V 完整解，须由非作者审查主证明、真实原合同和来源边界。
这份有界来源检查不保证全球首创、可发表性或正式 Route-A 通过。
纯数学适用性以定理假设与证明为依据，不套医学试验等级，未做
的期刊资质／利益冲突检查保留未检查状态。

全部证明与文件为当前 AI 团队辅助研究。无外部模型复核、无
人类同行评审、无目标 Euler／根数或 Hilbert–Pólya 声明。
