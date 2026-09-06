# C402 书目与引用适配核对

日期：2026-09-05。范围：本论文实际使用的全部四条 BibTeX。
这是当前代理对原文和元数据的核对记录，不是外部专家或人工通读认证。
正文无全局“首次／无人研究”断言；有边界的所有权检索保留在冻结合同 §4。

## 全部书目条目、版本与实际访问

| Bib key | 经核实的版本与元数据 | 实際访问与数学依赖 |
|---|---|---|
| `cattani1996residues` | Eduardo Cattani、Alicia Dickenstein、Bernd Sturmfels；1996；*Algorithms in Algebraic Geometry and Applications*，Progress in Mathematics 143，135–164；编辑 L. González-Vega、T. Recio；Birkhäuser Basel；DOI `10.1007/978-3-0348-9104-2_8` | [出版方章节页](https://link.springer.com/chapter/10.1007/978-3-0348-9104-2_8)、[作者发表目录](https://math.berkeley.edu/~bernd/articles.html) 与 DOI BibTeX 导出核对元数据。具体数学定位来自 [1994 作者原稿](https://arxiv.org/pdf/alg-geom/9404011)：Theorem 2.3、Lemma 4.2（含证明）、Corollary 1.18 和所需纯幂首项条件已访问。正文明确定位为 author preprint，不假装读取了出版方付费正文。 |
| `molinari2008determinants` | Luca Guido Molinari；*Linear Algebra and its Applications* 429(8–9)，2221–2226，2008；DOI `10.1016/j.laa.2008.06.015` | [作者机构记录](https://air.unimi.it/handle/2434/43334)、[作者发表目录](https://wwwteor.mi.infn.it/~molinari/PUBBLICAZIONI/molinari_pubblicazioni.html) 与 DOI BibTeX 导出核对。具体 [作者原稿 v3](https://arxiv.org/pdf/0712.0681v3) equation (1)、其 block identity 假设和标量化推导已访问。对本族代入右邻 −1、左邻 −a；短周期直接证明。 |
| `bornemann2010fredholm` | Folkmar Bornemann；*Mathematics of Computation* 79(270)，871–915，2010；DOI `10.1090/S0025-5718-09-02280-7` | [作者机构记录（含 BibTeX）](https://portal.fis.tum.de/en/publications/on-the-numerical-evaluation-of-fredholm-determinants/) 与 AMS 卷期元数据核对出版年份。[作者原稿](https://arxiv.org/pdf/0804.2543) §3 的 trace-class 定义条件、整 determinant 及式 (3.3) 已实际访问。该段总结经典 Gohberg–Krein、Dunford–Schwartz、Grothendieck／Simon 理论；只用于明确所调用的既有输入，不记为本论文创新。 |
| `timeordered2026notes` | *HCS-C22 T1--T3 derivation package*；本地头部日期 2026-08-09；未发表随附研究记录，无伪造作者、期刊、DOI | 定向读取 [DERIVATION_PACKAGE.md](../../../henon_time_ordered_ruelle_cocycle/DERIVATION_PACKAGE.md) 头部及第 515–675 行。Lemma 4／Theorem 5 拥有该两字母参数族的 Hill、单位权重全周期消去、返回导数迹分子以及退化 signed scheme-residue 约定。正文只扣除此基础层，不借旧包补主定理证明。 |

三项 DOI 元数据实际使用如下命令形态读取到 stdout，均退出 0：

```text
curl -fLSs --max-time 25 -H 'Accept: application/x-bibtex' 'https://doi.org/<DOI>'
```

`references.bib` 仅据这些实际数据作 LaTeX 转义、键名统一和必要元数据补全。
CDS 的 DOI 导出为 `@inbook` 且省略已核实的编辑、丛书和卷号，书目据出版方
页面规范成 `@incollection`。Bornemann 的 DOI 导出年份为 **2009**（在线出版），
卷期出版年份为 **2010**；使用后者作为 `year` 并在 `note` 明记在线年份。
没有把两个版本伪造为两篇论文。四条中仅本地未发表记录没有 DOI。

## 全部实际引用语境与 locator

| 编号 | TeX 位置／语境 | 所引用源的精确支持及限制 |
|---|---|---|
| R1 | `sections/1_introduction.tex`，Classical inputs 第一段 | CDS 作者原稿 Theorem 2.3／Lemma 4.2：固定多项式系统的 Laurent／正规形留数算法，满足纯幂初始项；不拥有此处的周期无关矩阵结论。 |
| R2 | 同段后半，循环 Jacobian 到返回矩阵的转换 | Molinari 作者原稿 v3 equation (1)：循环三对角 determinant 与 transfer product；不是任意多项式权重的残差迹压缩。 |
| R3 | `sections/1_introduction.tex`，preceding time-ordered calculation 段 | 本地 note Lemma 4／Theorem 5，范围严格为其指定族及单位权重／导数迹分子；主定理不依赖未复核的其他包结论。 |
| R4 | 同段末，经典 Fredholm determinant argument | Bornemann 作者原稿 §3：trace-class 算子的整 determinant 和局部迹展开；不据此声称本 W 是自然转移算子。 |
| R5 | `sections/3_residues.tex`，Lemma `lem:normal-form` 证明 | CDS 作者原稿 Lemma 4.2：最高标准单项式系数等于全局留数；本正文先验证首项及有限完全交。 |
| R6 | `sections/3_residues.tex`，Lemma `lem:hill` 长周期证明 | Molinari equation (1)，具体代入两种邻项与两条环角积；$n=1,2$ 不从不同顶点情形套用，而在正文展开。 |
| R7 | `sections/3_residues.tex`，Lemma `lem:local-expansion` 证明开头 | CDS 作者原稿 Theorem 2.3 的全局 Laurent 系数抽取，结合本文充分大圆条件重组为局部 $p(x_i)$ 分母级数。 |
| R8 | `sections/4_flow.tex`，Remark `rem:threshold` 最后一段 | CDS 作者原稿 Corollary 1.18 的 Euler–Jacobi 低次数消去；正文也从流量总和独立推出本族结论。 |
| R9 | `sections/5_consequences.tex`，Proposition `prop:trace-class` 证明 | Bornemann 作者原稿 §3、equation (3.3)：trace-class determinant 整性及迹展开。本文随后给出整个极点／幂零 iff 推理。 |

不存在未被引用的 Bib 条目；实际初编译的 `.aux` 含 9 个 `citation` 记录、
4 个 `bibcite`，最终 LaTeX/BibTeX 日志无未解析引文或警告，详见
[`INITIAL_BUILD_RECEIPT.md`](../INITIAL_BUILD_RECEIPT.md)。原文通过网页
PDF 文本访问，使用 theorem／section／equation
定位，不依赖未经 structural preflight 核实的本地 PDF 页码锚点。

## 完整性边界

不存在期刊／赛道校准、作者人工已读标记、Cabell/Scopus 订阅审计、外部
引用服务批量验证或外部模型评审声明。未将未公开正文发送给第三方模型。
Simon 的书目页曾用于寻找经典 determinant 原始定位，但没有读取对应整章，
因此不把它加进书目或冒称为已读依赖；最终采用已访问的 Bornemann §3。

AI 辅助写作与待作者确认的作者贡献／资助／利益冲突事项在正文声明中保留。
这些元数据待确认不妨碍匿名研究稿初编译，也不授权外部投稿。
