# Paper30 F：已定位先例的引文元数据台账

核验日期：2026-09-06。状态：`BOUNDED_CITATION_METADATA`。
仅为可能的后续写作保存六项书目，不是新查新、候选评审、立项或正文稿。
不改变任何数学 claim、最强先例扣除、评分或验收状态。

## 输入与核验口径

完整读取 [既有先例预筛](PAPER30_GAUGE_ACTION_PRIOR_PREFLIGHT_20260906.md)，
只处理其中 F 来源；读取 [冻结 brief](PAPER30_FORMAL_GAUGE_CANDIDATE_BRIEF_20260906.md)
§5 的引文与扣除。brief SHA256 核对为
`a663ee771399cc3a2b9c8b3964710dbe3b87e4c9f369e48d0f6c27777cba9622`。
采用 `research-lit` 的一手来源、版本区分和访问深度规则；按有界任务收窄为
已知题名/DOI 的元数据核对，没有扩展到文献全景、候选优先权或新科学判断。

“正式出版元数据已核”不等于“正式版全文及定理编号已核”。
已有定理定位继续绑定实际读过的版本，不能把预印本编号直接移给正式版。

## 1. Bousch 1992：未发表作者稿

- 作者：Thierry Bousch。
- 准确题名：*Algèbres de Hénon*。
- 年份/性质：1992，未发表手稿，13 页；无期刊、卷期或已核 DOI。
- 一手来源：[作者目录](https://www.imo.universite-paris-saclay.fr/~thierry.bousch/preprints/)
  明载年份与未发表性质；[作者原稿链接](https://www.imo.universite-paris-saclay.fr/~thierry.bousch/preprints/alghenon.pdf)。
- 复用来源：[Paper29 已接受书目](../../papers/29-filtered-henon-cohomology/paper-successor-20260906-transcription-v1/references.bib)
  的 `Bousch1992HenonAlgebras`，及 [Paper29 引文记录 §1](PAPER29_COHOMOLOGY_CITATION_RECORDS_20260906.md)。
- 实际支撑版本：前轮已全文读取的同一份 13 页作者稿；本次只核作者目录，未重新读取 PDF。
  §2 Théorème 1、§5.1 wrapping / Théorème 1 bis、§7 的指标平移均属于该未发表稿。
- 写作边界：保留其有限/无限二次 Hénon 基、wrapping 与 shift 的归属；
  不把直接线性代数推论包装为 Bousch 原文同式定理，不补造期刊或 DOI。

## 2. de la Llave–Saprykina：正式版已定位，旧编号仍属预印本

- 作者：Rafael de la Llave；Maria Saprykina。
- 正式准确题名：*Noncommutative coboundary equations over integrable systems*。
- 正式出版：*Journal of Modern Dynamics* **19** (2023), 773–794。
  出版社记录未另列期号；不补造期号或文章号。
- DOI：[10.3934/jmd.2023020](https://doi.org/10.3934/jmd.2023020)。
  [出版社元数据与摘要](https://www.aimsciences.org/article/doi/10.3934/jmd.2023020)
  核实作者、卷页及在线发表日期 **2023-10-07**。
- 预印本：[arXiv:2205.12356v1](https://arxiv.org/abs/2205.12356v1)，
  提交日期 **2022-05-24**；arXiv 本次只列 v1，未列 journal reference。
  预印本题名实际拼作 *Nonconmutative coboundary equations over integrable systems*，
  不应把该拼写误差复制为正式刊名记录的题名。
- 实际支撑版本：[arXiv v1 正文](https://arxiv.org/html/2205.12356v1) 的
  **Theorem 3、Remark 4**；本次重新定位这两处。出版社页面提供正式元数据与摘要，
  抽取的 HTML 全文区未给定理正文，本次未读取正式 PDF、未核正式版编号对应关系。
- 可复用写法：按 2023 正式版列书目，但具体编号写明
  “Theorem 3 and Remark 4 of the 2022 preprint, arXiv:2205.12356v1”。
  若不附版本限定，应先核正式版编号再引用。
- 既有扣除不变：解析 cocycle 的周期条件、参数形式解与解析解存在的关系是相关先例；
  不能把解析解存在写成给定形式解必收敛，也不能转为全局多项式 Hénon 坐标共轭分类。

## 3. Fiorenza–Manetti 2007：mapping-cone 框架

- 作者：Domenico Fiorenza；Marco Manetti。
- 准确题名：*$L_\infty$ structures on mapping cones*。
- 正式出版：*Algebra & Number Theory* **1**, no. **3** (2007), 301–330。
- DOI：[10.2140/ant.2007.1.301](https://doi.org/10.2140/ant.2007.1.301)。
  本次 DOI/出版社落地页抽取返回 internal error，没有据此宣称已读正式全文。
  [作者机构记录](https://iris.uniroma1.it/handle/11573/236044)核实作者、卷页与 DOI；
  [arXiv 元数据](https://arxiv.org/abs/math/0601312)明确补全 no. 3。
- 实际支撑版本：[arXiv:math/0601312v3 正文](https://arxiv.org/html/math/0601312v3)，
  v1 为 **2006-01-13**，v3 为 **2007-04-03**。
  前轮所读 Introduction / Theorem 1、Theorem 5.5、§6、Theorem 7.4 均指 v3；
  本次重新定位 Theorems 5.5 与 7.4，不宣称完成另一轮全文审证。
- 写作边界：正式书目可用 2007 刊本，精确编号仍注明 arXiv v3，
  除非以后另核刊本编号。一般高阶括号与 MC/gauge 框架的既有归属不变；
  本台账不构造 mapping-cone 模型，也不把 $1-\sigma$ 当作已成立的 Lie morphism。

## 4. Mardešić–Novikov–Ortiz-Bobadilla–Pontigo-Herrera 2026

- 作者：Pavao Mardešić；Dmitry Novikov；Laura Ortiz-Bobadilla；Jessie Pontigo-Herrera。
- 准确题名：*Noetherianity and Length of Melnikov Functions*。
- 正式出版：*Bulletin of the Brazilian Mathematical Society, New Series*
  **57** (2026), **article 34**；34 是文章号，不是起始页。
- DOI：[10.1007/s00574-026-00521-7](https://doi.org/10.1007/s00574-026-00521-7)。
- [出版社正式全文与书目](https://link.springer.com/article/10.1007/s00574-026-00521-7)
  核实：received **2025-12-26**，accepted **2026-06-27**，
  published / version of record 均为 **2026-07-20**。这些日期不混作卷年。
- 实际支撑版本：上述 2026 正式版，**§2.1 “Relation with o-Minimality”**；
  不是 Remark 2.1。本次核读了该节有限维解析扰动族的 Noetherian 说明段。
- 既有扣除不变：这里只用有限参数族的非有效有限首障碍阶数原则；
  不转用其主 Theorem A/B 的轨道长度结论，不据此声称 Hénon 分类已被覆盖或证明。

## 5. Arcet–Giné–Romanovski 2022：仅元数据及公开索引层

- 作者：Barbara Arcet；Jaume Giné；Valery G. Romanovski。
- 准确题名：*Linearizability of planar polynomial Hamiltonian systems*。
- 正式出版：*Nonlinear Analysis: Real World Applications* **63** (2022), **103422**。
  103422 是文章号；本次不补期号或页码。
- DOI：[10.1016/j.nonrwa.2021.103422](https://doi.org/10.1016/j.nonrwa.2021.103422)。
  DOI 内的 2021 不替代正式卷年 2022。
- [出版社记录](https://www.sciencedirect.com/science/article/pii/S1468121821001346)
  沿用既有先例预筛的来源；**本次没有重新打开该受限全文入口**。
  [作者机构研究记录](https://portalrecerca.udl.cat/documentos/64ad08dae28d57322266916c?lang=en)
  核实题名、卷年、作者缩写及 DOI；
  [机构库元数据索引](https://repositori.udl.cat/items/76a25878-2627-478a-8acc-a5ab90ee9579)
  的公开搜索结果给出作者全名和文章号，直接打开返回反机器人页面后停止。
- 实际证据深度不变：前轮为出版社公开索引中 Noetherian 理想稳定段落，
  **没有完成全文阅读**；本次元数据补全不升级这一深度。
  搜索结果另显示机构 PDF 链接，但未打开或下载，也未追索其他全文入口。
- 写作边界：可作为已识别的相邻文献列目；若引述精确定理、编号、充分性或证明细节，
  必须另有授权范围内的正文核验，不能由本台账补成“已读”。

## 6. Paper29：本地接受的匿名手稿

- 作者字段：**Anonymous**，来自已接受源码；不推断实名。
- 实际完整题名：*Filtered polynomial cohomology and finite periodic tests for symplectic Hénon maps*。
- 版本/性质：2026 年本地手稿；2026-09-06 本地接受。
  没有期刊、卷期、DOI、arXiv 编号或可对外使用的公开 URL。
- 一手来源：[项目接受索引](../../papers/29-filtered-henon-cohomology/README.md)
  明确指向 [已接受 main.tex](../../papers/29-filtered-henon-cohomology/paper-successor-20260906-transcription-v1/main.tex)。
  本次核对其 `\title` 与 `\author`；没有读取旧 PDF 或 build 内容。
- 可复用书目文字：Anonymous, *Filtered polynomial cohomology and finite periodic tests
  for symplectic Hénon maps*, local manuscript, 2026。
  “Accepted locally”只是工作区产物状态，不代表期刊接受或同行评议发表。
- 既有 F 依赖限于冻结 brief §5 已扣除的轨道基、系数障碍与次数适配正常形；
  本次不新核 theorem label，不给出论文间新贡献切分。

## 收尾

本次唯一新增文件为本台账；冻结 brief、既有 prior report 与 Paper29 接受源码均未修改。
没有创建项目、LaTeX/BibTeX 文件、下载文献、编译、外部写入或候选评分。
未打开当前 Paper30 R1/R2、未读取评审代理历史、未联系两位评审。
一次 Paper29 来源定位的广匹配输出意外包含旧 Paper29 候选记录的少量行；
已停止该检索方式，未将其用于本任务，也未扩展为评审审计。
最主要的元数据补充是 de la Llave–Saprykina 的 **2023 正式出版信息**，
以及 2026 Melnikov 论文的 **57 卷、文章 34**；原科学扣除保持不变。
