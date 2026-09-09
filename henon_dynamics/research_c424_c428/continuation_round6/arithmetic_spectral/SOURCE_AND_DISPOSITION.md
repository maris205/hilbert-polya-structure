# R6 算术谱：来源核查、WM6 处置与执行记录

2026-09-09 UTC。当前团队 AI 辅助研究；不是人类同行评审或全球查新。
本支线仅一项冻结题 WM6，作者已交完整手证；数学程序零次。

## 1. 本轮结果与实质边界

[WM6 冻结合同](FROZEN_CONTRACT.md) 与 [完整证明](PROOF_PACKAGE.md)
回答全 $p,E,m>r\ge1,a\ne0,c$ 稀疏族
$F=(y,y^{p^m}+cy^{p^r}-ax)$ 的两项性质：

- 全部原生周期的返回乘子都是局部单位，当且仅当 $|a|=1$ 且
  $|c|\le |p|^{-r(p^m-p^r)/(p^m-1)}$。
- 潜在全仿射好约化，当且仅当 $|a|=1$ 且 $|c|\le1$。
- 整个单位 Jacobian 分支的每步周期谱范数包络精确为
  $\log\max\{1,|p|^r\max(1,|c|)^{(p^m-1)/(p^m-p^r)}\}$，
  由实际固定点达到；全部周期的上界先行证明，没有周期截断。

**作者数学状态：PROVABLE AS STATED；实质状态：待非作者／协调者，
不自准入。** 本结果确有完整相界及全时间量词，但方法由最大项、
导数范数、韦达根界及已有 GR5 局部刚性组成，证明较短。
一维“无排斥周期点却无潜在好约化”的野现象已有明确主源；
不能将其移到二维后就宣称一个新的普遍机制。

建议至少保留为完整的谱范数适用性边界：它严格否定在本族上以
“全部周期乘子局部单位”反推潜在全仿射好约化。是否足够一项
独立论文，应评价精确全族包络和相界的残余内容；若仅够经典现象
的短扩展，则保留辅助定理，不补第四项。不会把谱平台、固定点例子、
扩域障碍分别拆项，也没有再凑第二题。

## 2. 两项被来源覆盖的预筛入口

### 2.1 精确 Hénon 周期谱逆问题

最初考虑以全部原生周期的精确返回迹／乘子重建正规化 Hénon 系数。
主源实际给出了固定次数下的有限选择刚性、统一有限周期决定性，
并扩展到任意代数闭特征零域；非特殊 Jacobian 下，周期一和二
已有有限选择且一般点唯一的结果。这直接覆盖了该预筛入口。
出处为 [Cantat–Dujardin, 2026，Theorem A、Theorem 3.7、Theorem 4.2](https://arxiv.org/html/2603.09445v1)。

**处置：SOURCE_OWNED_PRESCREEN_REJECTED，未冻结逆谱新合同。**
其不例外地唯一重建每个特殊映射并非已读定理所声称；不能把
有限选择说成全点唯一，也没有转而冒称解决这个更强问题。
本轮 Hill/Jacobi 前端查询另命中 C05/C32 的既有 Hessian／Hill
边界，未形成额外完整题或新理论。

WM6 使用的是局部乘子绝对值及其每步上包络，不是精确迹或乘子
全部相同，所以它不反驳上述特征零刚性。原文 Example 3.8 的
正特征加性 Hénon 常导数反例也先扣除：本题域特征仍为零，
导数没有消失，结论只是范数平台而非精确全谱恒定。

### 2.2 用完整有限周期模修复绝对周期计数

不同于上轮 Hillar 的绝对计数，这次预筛考虑保留
$\mathbb Z^n/\mathbb Z^n(A^j-I)$ 的自然模结构，以及全部兼容
有限商上的线性作用，问能否重建 profinite 共轭类。
对相似的双曲整数可逆矩阵，主源已经证明 principal Bowen–Franks
模给出该等价关系的完整不变量，并说明和更一般 $g(A)$ 模的关系。
出处为 [Bakker–Rodrigues, 2022，Theorem 4.13、Corollaries 4.14–4.15](https://arxiv.org/html/2207.00922v1)。

**处置：SOURCE_OWNED_PRESCREEN_REJECTED，未冻结新合同。**
这不是说绝对周期计数足够；也不是说 profinite 共轭已经等价于
整数共轭。原文 §5.1 明确保留嵌入的整数格，并修正旧论文中一个
交集判据的缺项。这里不把该已知额外标记再次包装为新全局修复。

## 3. 实际主源访问范围与判定

按 ARS 的有界 fact-check 使用正文核验，而非整套研究到论文管线。
来源的“数学适用性”和“出版／利益冲突核验”分别记录；未执行
医学式 I–VII 实验分级、期刊排名、Scopus/Cabell/COPE 或 COI 调查，
这些项目是未核验／不适用，不伪装为通过。无需它们证明某主源
已经明确陈述一个数学结果。

| 来源 | 实际读取范围 | 适用性、状态与限制 |
| --- | --- | --- |
| [Cantat–Dujardin, *Multiplier rigidity for complex Hénon maps*, arXiv:2603.09445v1](https://arxiv.org/html/2603.09445v1) | 引言的 Theorem A 与附近说明；§3.4 Theorem 3.7 全陈述与完整证明、Example 3.8；§4 Theorem 4.2 与 Example 4.3 的陈述及后者推导；另读 Proposition 3.3 陈述和 §1.5 的适用性讨论 | 原始作者预印本。用于精确谱逆问题的覆盖及与局部范数谱的区分；没有读完整篇 Lyapunov 证明，未独立认证其全部主定理。 |
| [Bakker–Rodrigues, *Generalized Bowen-Franks Groups and Profinite Conjugacy …*, arXiv:2207.00922v1](https://arxiv.org/html/2207.00922v1) | §1 引入及 BF 定义；§4.1 的 $\mathcal Q^{a},\mathcal Q^{p}$ 构造附近，Definition 4.6、Remark 2；Lemma 4.12、Theorem 4.13、Corollaries 4.14–4.15 的完整陈述与证明；§5.1 旧判据修正的陈述 | 原始作者预印本。覆盖相似双曲矩阵、带自然模结构的周期资料之 profinite 分类。并未声称标量计数足够或所有整数共轭问题已解决。 |
| [Robert L. Benedetto, *Determining Potential Good Reduction in Arithmetic Dynamics*, Silvermania 2015 原始 slides](https://math.colorado.edu/arithmetic2015/slides/Benedetto.pdf) | 标题／日期；PDF 页 2–9 的域、好约化、乘子与反向失败条款，特别 PDF 第 8 页（零起编号 7） | 2015-08-11 的原始讲演材料，不冒称期刊全文。明确拥有一维无排斥周期点但无潜在好约化现象；幻灯片未提供本题二维全族的完整证明。文字已读，单页截图失败，未据不可见图像补充公式细节。 |

[Cantat–Dujardin 版本页](https://arxiv.org/abs/2603.09445) 确认
v1 上传于 2026-03-10；[Bakker–Rodrigues 版本页](https://arxiv.org/abs/2207.00922)
确认 v1 上传于 2022-07-03。只使用实际 v1 正文，不将搜索抓取日期
当成出版日期。第二篇版本页标题用 “for”，所读 HTML 标题用 “of”；
按同一 arXiv ID 识别，不将这一标题措辞差异造作两篇来源。

讲演原始 PDF 的文字抽取直接支持其“逆命题失败”表述。
一次 `screenshot` 对零起编号 7 返回 Internal Error；没有伪称目视
成功，也没有为此下载或转换本地 PDF。检索结果中的第三方幻灯片
镜像、ResearchGate、自动摘要站仅用于发现，不作为上述数学断言的证据。

## 4. 本地碰撞与既有依赖

本轮读过当前 AGENTS、状态入口、第六轮计划、第五轮谱预筛报告。
对两个本地 registry 及本批文件进行了定向检索，关键词覆盖
multiplier spectrum、spectral rigidity、Hill determinant、Bowen–Franks、
profinite conjugacy、indifferent、unit multipliers 与野谱等。
这不是把全库所有论文重新全文审查。

相关命中包括 C05/C32 的 Hill／Morse 不变量边界、C401、GM3、
既有全局代数单位标签障碍及 GR5；没有将它们宣布为尚未完成。
本轮不再研究 Hillar 绝对 cyclic-resultant、C401 非共振 Frobenius、
GM3 全周期联合 Galois 群、Salem 或 Heisenberg 已闭合辅助模型。

WM6 明确依赖 [GR5 已准入的局部全仿射引理](../../continuation_round5/arithmetic/PROOF_PACKAGE.md)，
不是仅引用其摘要。该证明在上一轮已由本作者以非作者身份完整
审查；本轮作为已证明输入使用，并只读取主定理／局部假设定位，
没有为新任务重开已关闭的全篇审查。
此次核对的文件 SHA-256 仍为
`165f262916ae4cebaee51202fabbb9292c942942573c969de40b3bbbe58b46cb`。
新的谱上界与达到性不是由 GR5 自动给出的；但无好模型这一侧
确实借用了其强局部刚性，应从本题独立贡献中扣除。

所探测的 `henon_dynamics/papers/`、`henon_dynamics/literature/` 和
根 `literature/` 不存在；根 `papers/` 的相关枚举为另一 symbolic
研究流的文件，因此没有越流读其论文来制造本支线文献量。
工具目录无 Zotero、Obsidian、arXiv 或 Semantic Scholar 专用接口；
按技能回退到本地资料与主站网页。ARS 默认路由不启动程序化书目
resolver；没有声称运行 Semantic Scholar API 验证或付费索引。

## 5. 全部实际查询字串

本轮共五次 search-bearing 调用，每次三个字串，共十五条；
后续 open/find 和一次失败 screenshot 不计作新查询。

1. `"Hénon" "multiplier" "spectrum" rigidity`
2. `"Hénon" "Hill" "determinant"`
3. `"toral automorphisms" "profinite conjugacy" "Bowen"`
4. `"Hénon" "good reduction" "multipliers"`
5. `"Hénon" "non-archimedean" "repelling" periodic good reduction`
6. `"profinite conjugacy" "weak equivalence" ideals`
7. `"Hénon" "indifferent" "non-archimedean"`
8. `"Hénon" "multipliers" "bad reduction"`
9. `"periodic multipliers" "potentially good reduction" polynomial wild`
10. `"Henon" "nonrepelling" "p-adic"`
11. `"Hénon" "indifferent periodic" reduction`
12. `"non-archimedean" polynomial "no repelling periodic points" "bad reduction"`
13. `"Determining Potential Good Reduction" Robert`
14. `"polynomial" "no repelling periodic points" Benedetto`
15. `"Hénon" "y" "p^2" "multipliers"`

查询中的无关天体 Hill 问题、Hénon–Heiles、随机动力、隐写／加密、
一般群作用 weak equivalence 和自动摘要结果都没有作为证据使用。
未查尽所有语言、数据库或非公开资料；未命中同一二维公式不等于
全球优先权成立。新结果是作者手推，来源判定仅限上述正文范围。

## 6. 技能作用与执行收据

本轮主作者全文读取仓库 `henon-route-a-batch` 及其 workflow，
`idea-creator`、`research-lit`、`proof-writer`，以及 ARS router、
deep-research workflow、source-verification 角色和相关质量／失败边界。
批次技能促成两个已有机制的预筛淘汰与一题完整冻结；proof-writer
要求保留全部量词、边界和明确依赖；ARS 只用于来源适用核验。
当前用户／团队约定覆盖旧 GPT-5.4、外部 MCP 和 GPU 模板。
没有启动 Socratic 访谈、全 ARS 管线、强行评分或固定复审轮数。

只在本轮自有目录新增冻结合同、证明包和本文件。未修改共享状态、
计数、GR5 或其他旧输入、另一研究流、正式评价、稿件或 Git 暂存／提交。
入口静态状态为 tracked CURRENT 状态文档修改、本批及原有八目录
未跟踪，均保留。数学程序、GPU、付费 API、外部模型上传、
TeX/PDF、提交／推送／fetch 均为零。

`NO_BAD_EULER_OR_ROOT_NUMBER` 无条件保留。
三项原准入不被重开；WM6 是否另准入留给非作者与协调者，
本文件不更改当前总数，也不宣布五篇交付完成。
