# Uniform trace charts：已核验引用记录

核验日期：2026-09-06。适用输入：
PAPER29_UNIFORM_TRACE_CHARTS_BRIEF_20260906.md。
本文件只做候选阶段 citation 准备：6 条记录，其中 5 条为指定最小参考集，
1 条为可选的平面多项式自同构背景。不是查新重评、数学复审或任何 PASS。
没有读取候选 R1/R2 报告，没有修改既有 proof、brief、literature 或创建论文项目、
LaTeX 源文件、独立 bib 文件。

## 1. 核验方法与使用原则

沿用已完整读取的 research-lit 工作方法：先定位本地已读文献和当前 brief，
再核对 arXiv 官方记录、出版社记录及其向 Crossref 登记的 DOI 元数据。
没有通过二手引文补齐未核实字段。正式发表者优先引用 version of record；
预印本保留明确的已核版本。以下 BibTeX 是可复用片段，不是已完成的 bibliography build。

每条记录分别说明“书目信息已核”和“内容定位已读”的边界。
先前已读的 arXiv 节号不会无声地变成期刊正式版节号。
本轮不重做先前数学审查，也不将有限纤维结论改写成逐点微分满秩。

| Key | 核验状态 | 当前适当用途 |
| --- | --- | --- |
| Gorbovickis2016 | 正式发表，ETDS 36(4), 1156–1166 | 一变量指定周期乘子独立性的直接比较 |
| CantatDujardin2026 | arXiv:2603.09445v1；未核到正式期刊版本 | 固定多重 Jacobian 的完整谱刚性比较 |
| SterlingMeiss1998 | 正式发表，Physics Letters A 241(1–2), 46–52 | 经典 anti-integrable 轨道构造背景 |
| CvitanovicLiang2026 | 正式发表，Chaos 36(2), article 023130 | Hill／状态 Jacobian 与参数迹 Jacobian 的概念区分 |
| BianchiHe2026 | arXiv:2606.29363v1；未核到正式期刊版本 | 仅热力学谱几何背景，不作为当前正式推论 |
| FriedlandMilnor1989 | 正式发表，ETDS 9(1), 67–99 | 可选：平面多项式自同构及 Hénon 复合背景 |

## 2. Gorbovickis：正式发表记录

题名：Algebraic independence of multipliers of periodic orbits in the space of
polynomial maps of one variable。作者：Igors Gorbovickis。
正式卷期为 2016 年，Ergodic Theory and Dynamical Systems 36(4), 1156–1166；
DOI 为 10.1017/etds.2014.103。2014-12-15 是 online-first 日期，
2013 是 arXiv 初稿年份，均不替代本条正式卷期的 year=2016。
[出版社记录](https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/abs/algebraic-independence-of-multipliers-of-periodic-orbits-in-the-space-of-polynomial-maps-of-one-variable/F56F073EEB6B7125E0B51F57FC822E35)
与 [Crossref 登记](https://api.crossref.org/works/10.1017/etds.2014.103) 相符。

~~~bibtex
@article{Gorbovickis2016,
  author  = {Gorbovickis, Igors},
  title   = {Algebraic independence of multipliers of periodic orbits in the space of polynomial maps of one variable},
  journal = {Ergodic Theory and Dynamical Systems},
  year    = {2016},
  volume  = {36},
  number  = {4},
  pages   = {1156--1166},
  doi     = {10.1017/etds.2014.103},
  url     = {https://doi.org/10.1017/etds.2014.103}
}
~~~

Claim-use：一变量多项式的指定周期 marked multipliers 可作泛型局部坐标；
先前内容核验使用 [arXiv:1305.0867v1](https://arxiv.org/abs/1305.0867v1)
Theorem 1.6、Lemma 2.1，后者还提供共同基点的选轨道结果。
本条不能替代当前非零 Jacobian Hénon 复合族的证明，
也不能证明固定非缩小参数邻域上的全周期一致 conditioning。
若正文保留上述精确节号，应注明 arXiv 版本，或在以后实际准备正文时核对正式版编号。

## 3. Cantat–Dujardin：已核预印本版本

题名：Multiplier rigidity for complex Hénon maps。
作者：Serge Cantat、Romain Dujardin。
[arXiv 官方记录](https://arxiv.org/abs/2603.09445) 在本轮显示 v1，
提交日期为 2026-03-10，未载 journal reference 或正式期刊 DOI。
标题定向 Crossref 查询未检得精确匹配的 version of record；
这只是本次检索结果，不是断言世界范围内不存在发表或接收信息。
10.48550/arXiv.2603.09445 是预印本 DOI，不是期刊 DOI。

~~~bibtex
@misc{CantatDujardin2026,
  author        = {Cantat, Serge and Dujardin, Romain},
  title         = {Multiplier rigidity for complex {H{\'e}non} maps},
  year          = {2026},
  eprint        = {2603.09445},
  archivePrefix = {arXiv},
  doi           = {10.48550/arXiv.2603.09445},
  url           = {https://arxiv.org/abs/2603.09445v1},
  note          = {Preprint, version 1}
}
~~~

Claim-use：[已读 v1](https://arxiv.org/html/2603.09445v1) 的 Theorem B、
Theorems 3.5、3.7 支撑完整周期谱的有限纤维及有限周期截断背景；
Remark 3.4(2) 讨论沿无穷周期子序列保留完整轨道数据。
这些结论不直接给出每个预先指定周期向量的恰好 k 条观测、
逐点无分歧、固定邻域全周期一致下界或本候选的最优喷射阶。
页面正文出现的其他日期不能当成未登记的 v2 发布日期。

## 4. Sterling–Meiss：anti-integrable 经典记录

题名：Computing periodic orbits using the anti-integrable limit。
正式 DOI 登记作者为 D. Sterling、J. D. Meiss；
arXiv 作者栏写 D. G. Sterling、J. D. Meiss。本片段采用正式登记的缩写，
不据此扩写未经本轮核验的全名。
Physics Letters A 241(1–2), 46–52 (1998)，
DOI 10.1016/S0375-9601(98)00094-2。
[出版社提交的 Crossref 元数据](https://api.crossref.org/works/10.1016/S0375-9601(98)00094-2)
与 [arXiv 官方 journal reference](https://arxiv.org/abs/chao-dyn/9802014) 相互核对。

~~~bibtex
@article{SterlingMeiss1998,
  author  = {Sterling, D. and Meiss, J. D.},
  title   = {Computing periodic orbits using the anti-integrable limit},
  journal = {Physics Letters A},
  year    = {1998},
  volume  = {241},
  number  = {1-2},
  pages   = {46--52},
  doi     = {10.1016/S0375-9601(98)00094-2},
  url     = {https://doi.org/10.1016/S0375-9601(98)00094-2}
}
~~~

Claim-use：先前已读 [arXiv 全文](https://arxiv.org/html/chao-dyn/9802014)
§2、Theorem 1 支撑 Hénon 的全符号序列 anti-integrable 延拓和统一小参数构造背景。
本候选可引用其经典方法渊源，但其轨道存在估计不等于本候选的参数迹 Jacobian、
周期归一化导数、模六障碍或选轨道消元证书。
当前证明不调用某个特定最锐 horseshoe 阈值，故不为补数量另加 Devaney–Nitecki。

## 5. Cvitanović–Liang：应从旧预印本更新为正式版

题名：A chaotic lattice field theory in two dimensions。
作者：Predrag Cvitanović、Han Liang。
正式发表为 Chaos: An Interdisciplinary Journal of Nonlinear Science 36(2),
article 023130 (2026)，DOI 10.1063/5.0273642。
023130 是文章号，不是已核验的页码范围；
[Crossref 正式登记](https://api.crossref.org/works/10.1063/5.0273642)
给出 2026 年 2 月卷期及 2026-02-18 在线日期。
[arXiv 官方记录](https://arxiv.org/abs/2503.22972) 也载该期刊 DOI，
当前显示 v3，2026-02-13；旧文献审查使用过的 v2 为 2025-12-30。

~~~bibtex
@article{CvitanovicLiang2026,
  author  = {Cvitanovi{\'c}, Predrag and Liang, Han},
  title   = {A chaotic lattice field theory in two dimensions},
  journal = {Chaos: An Interdisciplinary Journal of Nonlinear Science},
  year    = {2026},
  volume  = {36},
  number  = {2},
  eid     = {023130},
  doi     = {10.1063/5.0273642},
  url     = {https://doi.org/10.1063/5.0273642}
}
~~~

Claim-use：Hill／状态 Jacobian、离散 Fourier 与 anti-integrable 的背景比较，
不能将状态变量的线性化算子当作当前周期迹关于系数的 Jacobian。
本轮对 [v3 定向核对](https://arxiv.org/html/2503.22972v3)：
状态 Jacobian 的节标题现在是 §V，式 (55)–(59)，有限胞例子仍见式 (64)–(65)；
Fourier 部分现在是 §IX。旧 v2 的 §IV、§VIII 不能直接照搬。
正式版书目信息已核，但没有声称已逐节核对出版社 PDF 的编号。
以后若所选 BibTeX 样式不显示 eid，可按样式规则把文章号放入 pages；
无论采用哪个字段，均不得把 023130 捏造成物理页码范围。

## 6. Bianchi–He：仅作背景，不提升为当前定理

题名：A thermodynamic path metric for complex Hénon maps。
作者：Fabrizio Bianchi、Yan Mary He。
[arXiv 官方记录](https://arxiv.org/abs/2606.29363) 本轮显示 v1，
提交日期 2026-06-28，未载 journal reference 或正式期刊 DOI。
定向 Crossref 标题查询未得到精确匹配的 version of record。
10.48550/arXiv.2606.29363 是预印本 DOI。

~~~bibtex
@misc{BianchiHe2026,
  author        = {Bianchi, Fabrizio and He, Yan Mary},
  title         = {A thermodynamic path metric for complex {H{\'e}non} maps},
  year          = {2026},
  eprint        = {2606.29363},
  archivePrefix = {arXiv},
  doi           = {10.48550/arXiv.2606.29363},
  url           = {https://arxiv.org/abs/2606.29363v1},
  note          = {Preprint, version 1}
}
~~~

Claim-use：[已读 v1](https://arxiv.org/html/2606.29363v1)
Theorem 1.1、Proposition 3.4、Corollary 3.5 仅供热力学谱几何背景。
当前统一 brief 已不把热力学推论列作正式定理。
不得借其路径距离非退化偷换成逐点协方差正定，
也不得由当前有限迹坐标矩阵的最小奇异值直接宣称协方差的定量下界。

## 7. Friedland–Milnor：可选的族背景记录

题名：Dynamical properties of plane polynomial automorphisms。
作者：Shmuel Friedland、John Milnor。
Ergodic Theory and Dynamical Systems 9(1), 67–99 (March 1989)，
DOI 10.1017/S014338570000482X。
[Crossref 正式登记](https://api.crossref.org/works/10.1017/S014338570000482X)
与 [出版社第 9 卷第 1 期记录](https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/issue/AFB64CE12885AB78D98E07273163305E)
支持上述字段。页面显示的 2008 在线日期属于后来的数字上线记录，
不是本论文的发表年份。

~~~bibtex
@article{FriedlandMilnor1989,
  author  = {Friedland, Shmuel and Milnor, John},
  title   = {Dynamical properties of plane polynomial automorphisms},
  journal = {Ergodic Theory and Dynamical Systems},
  year    = {1989},
  volume  = {9},
  number  = {1},
  pages   = {67--99},
  doi     = {10.1017/S014338570000482X},
  url     = {https://doi.org/10.1017/S014338570000482X}
}
~~~

Claim-use：仅在介绍平面多项式自同构、广义 Hénon 映射及其复合的历史背景时可选。
当前显式给定的二次复合族和参数坐标公式不依赖重新调用完整分类定理。
本轮未阅读正式全文，不为它添加未经核对的 §7 分类细节，
也不以它证明本候选固定多重 Jacobian 族上的精确有限规范群。
如正文无需上述历史背景，此条可以省略。

## 8. 未决事项及交付边界

- 6 条均有实际核验的主记录；4 条正式发表、2 条以已核 arXiv v1 记录。
  CD 与 BH 的正式期刊信息本轮未找到，因此没有补造 venue、卷期或页码。
- Cvitanović–Liang 的正式版已发表，引用年份与旧预印本编号需要区分；
  特定节号若归属于正式版，仍需以后按实际引文位置核对正式全文。
- Gorbovickis 与 Sterling–Meiss 的内容定位来自已读 arXiv 版本；
  不将正式版 metadata 验证包装成正式全文复审。
- 不添加未被当前实际证明调用的奇异值比较教材条目，
  不引用本地未公开论文作为外部核心证据，不按文献数量 quota 扩展搜索。
- 本记录不改写既有查新／价值结论，不解除体量或其他验收约束，
  不代表引用构建已编译通过，也不产生投稿、上传或外部写入权限。
