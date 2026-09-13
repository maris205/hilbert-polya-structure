# Paper29 余同调候选：实际引用记录

日期：2026-09-06。用途：为后续可能采用的正文提供少量已核一手书目与 claim 对照；不是查新报告、证明审查、立项或容量评分。

## 0. 输入、取舍与编号规则

本次只读当前两份证明报告与已完成文献报告，没有改动它们：

- **S**：[scalar 证明报告](PAPER29_HENON_COHOMOLOGY_PROBE_20260906.md)，当前 447 行。
- **M**：[multi-phase 证明报告](PAPER29_CYCLIC_COHOMOLOGY_FINITE_PERIOD_PROBE_20260906.md)，当前 408 行。
- **L**：[已完成文献预筛](PAPER29_POLYNOMIAL_COHOMOLOGY_LITERATURE_PREFLIGHT_20260906.md)，当前 242 行。

下文分别记录“正式出版元数据”与“实际读取版本中的定位”。书目采用正式卷年；只有明确核过同一正式版时，才把某个定理编号称为正式版编号。作者稿／arXiv 的编号不能未经对照移植。BibTeX 是根据所列一手元数据整理的最小可用条目，不是声称从出版社原样导出。

| 条目 | 实际用途 | 正文对应位置 |
|---|---|---|
| Bousch 1992 | 必须归属的有限／无限二次 Hénon 代数基、wrapping 与 shift 先例 | S §3、§6；M §1、§3 及其开头归属段 |
| Schneider 2016 | Karr 型加性超越扩张常数域判据的直接可读引文 | S 引理 8.1 |
| Cerveau–Déserti 2018 | 接触 lift 中次高系数降为余同调方程的邻近先例 | S 引理 8.1 后的归属说明、§11 |
| Pollicott–Sharp 2004 | 有限周期 Livšic 的 Anosov／Hölder 近似背景 | 引言；与 S 定理 6.3、M 主命题的条件比较 |
| Gouëzel–Lefeuvre 2021 | quantitative finite approximate Livšic 的流版本 | 引言；与精确单周期概形判据的条件比较 |
| Bruin–Holland–Nicol 2005 | 可选：仅在正文专门提到 Hénon-like 正则性文献时使用 | S §11 第 4 项／引言 |

不按数量补文献。Frigo–Johnson 的 FFT 数字反转不是本候选的理论依赖，本册不为它增加 BibTeX 条目；若只把 mixed-radix reversal 定义为一个显式置换，无需强加 FFT 参考文献。Endler–Gallas 的轨道坐标和、其他 Hénon skew products、2026 年有限 Livšic 报告摘要，也不因曾在 L 中排查过就自动进入理论依赖列表。

## 1. Bousch 1992：未发表作者稿

**元数据。** Thierry Bousch，*Algèbres de Hénon*，1992，未发表手稿，13 页。年份与未发表性质来自[作者目录](https://www.imo.universite-paris-saclay.fr/~thierry.bousch/preprints/)；正文来自[作者 PDF](https://www.imo.universite-paris-saclay.fr/~thierry.bousch/preprints/alghenon.pdf)。没有为其虚构期刊、卷号、DOI 或 arXiv 编号。

**实际读取版本与位置。** 前轮已全文读取作者目录链接的 13 页 PDF；本轮核对作者目录和 S/M/L 中的对应使用。定位全部指这份未发表稿：§2 Théorème 1；§5.1 wrapping 与 Théorème 1 bis；§7 的指标平移；Théorème 3 及其 §3–5 的迹平均讨论。

**安全支持。** 二次 Hénon 有限周期代数的 square-free 标准基、无限轨道代数的 bounded-exponent 基、wrapping 与 Hénon pullback 的指标平移。§2 明确认识到多重点需要保留导数信息。其已公开内容应归属，即使它未发表于期刊。

**不能据此支持。** 任意次数／任意多 phase 的完整推广；本项目精确 Hilbert 公式、原函数次数界、单周期概形余边界 iff 或 leading-$4$ 尖锐性。Theorem 3 的乘法算子迹平均，不是 $S_ng$ 在固定点坐标代数中等于零的命题。基被置换后得到 word-orbit 余同调，是另行说明的直接线性代数推论，不应冒充该稿原文的同式定理。

~~~bibtex
@unpublished{Bousch1992HenonAlgebras,
  author = {Bousch, Thierry},
  title  = {Alg{\`e}bres de {H{\'e}non}},
  year   = {1992},
  note   = {Unpublished manuscript, 13 pp.},
  url    = {https://www.imo.universite-paris-saclay.fr/~thierry.bousch/preprints/alghenon.pdf}
}
~~~

**建议正文用法。** “Our normal-form construction extends the quadratic Hénon algebra basis and wrapping formalism of Bousch [Bou92, §§2, 5.1, 7].” 若正文独立给出推广证明，这句话表达归属，不把推广结论交给旧稿承担。

## 2. Schneider 2016：加性扩张判据的直接引文

**正式元数据。** Carsten Schneider，*A difference ring theory for symbolic summation*，Journal of Symbolic Computation **72** (2016)，82–127，DOI [10.1016/j.jsc.2015.02.002](https://doi.org/10.1016/j.jsc.2015.02.002)。已核[作者所属 JKU 的正式记录](https://research.jku.at/en/publications/a-difference-ring-theory-for-symbolic-summation-2/)。

**实际读取版本与位置。** [arXiv:1408.2776v2](https://arxiv.org/abs/1408.2776v2)，版本日期 2015-02-03；已读其 [PDF](https://arxiv.org/pdf/1408.2776v2) §3.1 的 Lemma 3.10、Theorem 3.11，作者稿内页 19。以下精确编号按该 v2，不把“19”当作正式卷页，也不声称本轮已逐页对照出版 PDF。arXiv 元数据还说明 v2 调整过环境编号，不能混用 v1。

**安全支持。** 在特征零差分域 $(E,\sigma)$ 上添加超越元 $r$，规定 $\sigma r=r+b$，常数域保持不变当且仅当底域中不存在 $\sigma h-h=b$ 的解。原文将相邻 Lemma 3.10 追溯到 Karr 1985 的 Theorems 2.1 与 2.3 的组合。因此 S 引理 8.1 的一般加性扩张步骤应承认为 Karr 型已知判据；项目自己的系数比较证明可为自含性保留。

**不能据此支持。** Hénon 底差分域中的具体余边界求解、单变量必要性、原函数次数不增、势函数平移例外或整个四维固定域的对象专属分类。其 $\Pi\Sigma$ 算法框架不自动包含当前 Hénon 底。可解时常数域恰为 $E^\sigma(r-h)$ 的简单补充可由 S 的系数比较证明给出，不应把未单独定位的强化句全部强归给 Theorem 3.11。

~~~bibtex
@article{Schneider2016DifferenceRings,
  author        = {Schneider, Carsten},
  title         = {A difference ring theory for symbolic summation},
  journal       = {Journal of Symbolic Computation},
  volume        = {72},
  year          = {2016},
  pages         = {82--127},
  doi           = {10.1016/j.jsc.2015.02.002},
  eprint        = {1408.2776},
  archivePrefix = {arXiv},
  primaryClass  = {cs.SC}
}
~~~

**年份与归属注意。** 2016 是正式卷年；2015 是 arXiv v2／在线出版时间所在年份，且出现在 DOI 中，不应改写正式书目为 “Schneider 2015, vol. 72”。本册选择这个已直接读到的判据作引用入口，未重新全文读取 Karr 原文，因此不新增一个只凭二次引文精确指定 Karr 定理的必需条目。可安全写：“the classical additive-extension criterion of Karr, in the form recalled by Schneider [Sch16, §3.1; Theorem 3.11 in arXiv v2]”。

## 3. Cerveau–Déserti 2018：接触 lift 的系数比较先例

**正式元数据。** Dominique Cerveau 与 Julie Déserti，*Birational maps preserving the contact structure on $\mathbb P^3_{\mathbb C}$*，Journal of the Mathematical Society of Japan **70**(2) (2018)，573–615，DOI [10.2969/jmsj/07027580](https://doi.org/10.2969/jmsj/07027580)。已核[J-STAGE 正式期目录](https://www.jstage.jst.go.jp/browse/jmath/70/2/_contents/-char/en)、[作者目录](https://dominique-cerveau.perso.math.cnrs.fr/)与 arXiv 的 journal reference。

**实际读取版本与位置。** [arXiv:1602.08866v2](https://arxiv.org/abs/1602.08866v2)，2017-04-10；本轮直接读取其 [HTML](https://arxiv.org/html/1602.08866v2) §4.1 的 Propositions 4.2、4.5 及证明。编号明确指 v2；未以搜索引擎的正式 PDF 摘录冒充正式全文编号核对。

**安全支持。** 对文中规定的保接触形式加性 lift，不变曲面方程首一化后，比较扩张变量的次高系数得到
$\ell b=a-a\circ\varphi$。因此从不变超曲面转为底上加性余同调方程的机制已有邻近几何先例。Proposition 4.5 还在其具体接触假设下得到 birational 解耦及相应不变有理函数。

**不能据此支持。** 去掉接触形式条件后直接套用其全部几何结论；把任意四维辛扩张等同于其三维接触 lift；替代 S 定理 2.1 的精确单变量 Hénon 刚性或 S 定理 9.1 的多项式势平移分类。正文如只使用通用常数域判据，应以 Schneider 为直接依赖，Cerveau–Déserti 用于说明邻近先例，而不是额外假设来源。

~~~bibtex
@article{CerveauDeserti2018Contact,
  author        = {Cerveau, Dominique and D{\'e}serti, Julie},
  title         = {Birational maps preserving the contact structure on {$\mathbb{P}^3_{\mathbb{C}}$}},
  journal       = {Journal of the Mathematical Society of Japan},
  volume        = {70},
  number        = {2},
  year          = {2018},
  pages         = {573--615},
  doi           = {10.2969/jmsj/07027580},
  eprint        = {1602.08866},
  archivePrefix = {arXiv},
  primaryClass  = {math.AG}
}
~~~

## 4. Pollicott–Sharp 2004：有限 Livšic 的离散背景

**正式元数据。** Mark Pollicott 与 Richard Sharp，*Livsic theorems, maximizing measures and the stable norm*，Dynamical Systems **19**(1) (2004)，75–88，DOI [10.1080/14689360410001658990](https://doi.org/10.1080/14689360410001658990)。[出版社页面](https://www.tandfonline.com/doi/full/10.1080/14689360410001658990)确认作者、卷期、卷年和页码；该页面显示的 2010 年上线日期不改变 2004 正式卷年。

**实际读取版本与位置。** 本轮重新直接读取 [Sharp 官方作者稿](https://warwick.ac.uk/fac/sci/maths/people/staff/richard_sharp/p2/livsic.pdf)，定位为 **§4 “Finite Livsic Theorems”，Theorem 2 与 Proposition 4.1**，作者稿内页 12–14。当前作者 PDF 未提供稳定的 arXiv 版本号；以上定位限定于 2026-09-06 所读 URL 内容，未声明与正式版编号相同。

**真实版本差异。** 此前检索可见另一份旧稿使用 §5、Theorem 3、Proposition 5.1。不能把旧稿编号与本轮作者稿编号交叉搭配，也不能只根据标题相同就写成正式版定位。最终正文可以仅引用“the finite Livšic result of Pollicott and Sharp”，或明确注明 “§4 of the author manuscript”。

**安全支持。** 在 transitive Anosov 微分同胚与 Hölder 函数假设下，有限短周期上的零和控制其余周期和；Proposition 4.1 还给出到余边界空间的统一范数距离估计，尺度为 $C\|f\|_\alpha L^{-\alpha\beta}$。这是有限周期的定量近似背景。

**不能据此支持。** 一般系数 Hénon 的无双曲性代数命题、严格多项式原函数、单个完整固定点概形的精确零检测、非既约结构或本项目的次数／Hilbert 公式。不能把小距离换成距离严格为零。

~~~bibtex
@article{PollicottSharp2004FiniteLivsic,
  author  = {Pollicott, Mark and Sharp, Richard},
  title   = {{Livsic} theorems, maximizing measures and the stable norm},
  journal = {Dynamical Systems},
  volume  = {19},
  number  = {1},
  year    = {2004},
  pages   = {75--88},
  doi     = {10.1080/14689360410001658990},
  url     = {https://warwick.ac.uk/fac/sci/maths/people/staff/richard_sharp/p2/livsic.pdf}
}
~~~

## 5. Gouëzel–Lefeuvre 2021：finite approximate Livšic 的流版本

**正式元数据。** Sébastien Gouëzel 与 Thibault Lefeuvre，*Classical and microlocal analysis of the x-ray transform on Anosov manifolds*，Analysis & PDE **14**(1) (2021)，301–322，DOI [10.2140/apde.2021.14.301](https://doi.org/10.2140/apde.2021.14.301)。已核[出版社文章页](https://msp.org/apde/2021/14-1/p08.xhtml)的作者、卷期、页码、DOI 与正式日期字段；正式出版日期为 2021-02-19。

**实际读取版本与位置。** [arXiv:1904.12290v2](https://arxiv.org/abs/1904.12290v2)，2019-08-09；已直接读 [PDF](https://arxiv.org/pdf/1904.12290v2) 引言，特别是 §1.1 Theorem 1.2，作者稿内页 2，以及 Remark 1.3。此处编号与页码按 arXiv v2；本轮出版社 PDF 链接未提供可解析的 PDF 内容，故不宣称已对照正式版的同号定理。

**安全支持。** 在 transitive Anosov flow 上，对归一化 Hölder 函数，如果长度至多 $\varepsilon^{-1/2}$ 的所有闭轨道的归一化积分足够小，则可分解为流方向余边界加一个范数为 $O(\varepsilon^\tau)$ 的余项。文中明确定位为 finite approximate Livšic，并承认 S. Katok 的较早 contact-flow 结果。

**不能据此支持。** 把有限误差估计改成多项式环中的精确等式；把所有短周期的观测改成单个完整周期概形；声称其适用于任意系数 Hénon；或把这里的 $\varepsilon$ 误差尺度等同于本项目普通次数 $D$。正文也不宜把这条 2021 结果称为“截至今日最佳误差率”。

~~~bibtex
@article{GouezelLefeuvre2021FiniteLivsic,
  author        = {Gou{\"e}zel, S{\'e}bastien and Lefeuvre, Thibault},
  title         = {Classical and microlocal analysis of the x-ray transform on {Anosov} manifolds},
  journal       = {Analysis \& PDE},
  volume        = {14},
  number        = {1},
  year          = {2021},
  pages         = {301--322},
  doi           = {10.2140/apde.2021.14.301},
  eprint        = {1904.12290},
  archivePrefix = {arXiv},
  primaryClass  = {math.DS}
}
~~~

## 6. 可选：Bruin–Holland–Nicol 2005

**采用条件。** 只有正文实际比较某些 Hénon-like 系统上的可测／Hölder Livšic 正则性时引用；它不是上面“两篇 finite Livšic”之一，也不是本代数证明的必要输入。

**正式元数据。** Henk Bruin、Mark Holland、Matthew Nicol，*Livšic regularity for Markov systems*，Ergodic Theory and Dynamical Systems **25**(6) (2005)，1739–1765，DOI [10.1017/S0143385705000179](https://doi.org/10.1017/S0143385705000179)。[Cambridge 官方记录](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/3F851FF311C4FDEA3677E2435F645C6A/S0143385705000179a.pdf/livsic-regularity-for-markov-systems.pdf)确认卷期及 2005 年，online date 为 2005-09-22；不采纳其他数据库出现的 2006 年日期作为卷年。

**实际读取版本与位置。** 前轮直接读取 [arXiv:math/0503690v2](https://arxiv.org/pdf/math/0503690v2)，2005-08-12，引言与 §6 “Livšic theorems for non-uniformly hyperbolic systems”。本轮核出版元数据，不把这一 arXiv 章节的分页／定理号当作正式版编号。

**安全支持。** Markov/Young tower 方法下某些 Hénon-like 映射上可测余同调解的正则性。**不能支持**任意系数保面积 Hénon 的有理或多项式解分类、有限单周期概形 iff、primitive 次数界或滤过 Hilbert 公式。

~~~bibtex
@article{BruinHollandNicol2005Livsic,
  author        = {Bruin, Henk and Holland, Mark and Nicol, Matthew},
  title         = {{Liv{\v{s}}ic} regularity for {Markov} systems},
  journal       = {Ergodic Theory and Dynamical Systems},
  volume        = {25},
  number        = {6},
  year          = {2005},
  pages         = {1739--1765},
  doi           = {10.1017/S0143385705000179},
  eprint        = {math/0503690},
  archivePrefix = {arXiv}
}
~~~

## 7. 交付边界

上述 5 条核心加 1 条可选记录足以覆盖这次限定的实际引用用途，不代表最终正文必须全部引用。未为未读原文编造定理编号；未把作者稿年月、网页上线日期与正式卷年混用。未重新运行全批文献检索，未修订 S/M/L，未创建正式论文或执行外部写操作。对候选的新意、价值、证明通过状态和容量不作评分。
