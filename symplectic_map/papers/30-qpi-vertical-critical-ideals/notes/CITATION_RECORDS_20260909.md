# Paper30 Vertical Alpha V1：引用身份与正文责任台账

日期：2026-09-09。状态：`CITATION_PLAN_FINAL`，不是新查新、新审查或证明认证。
范围：已准入的完整 V1–V3，匿名英文纯数学正文；本文不改 scientific / acceptance locks。
唯一产出为本台账，不生成 bibliography、稿件或新锁。

## 1. 口径与输入

采用 paper-plan 的引用规划及 ARS academic-paper 的 citation-compliance 路由。
用户本地、匿名、英文、纯数学、22–30 页完整正文合同优先于技能的默认 ML 模板、
双语、实验、上传和整条流水线建议。本任务没有启动额外审查或下游代理。

完整读取以下当前输入；这些是本地责任来源，不应成为匿名论文的对外参考文献：

- `PAPER30_QPI_VERTICAL_ALPHA_FORMAL_CANDIDATE_DISPOSITION_V1_20260909.md`。
- `PAPER30_QPI_VERTICAL_ALPHA_CANDIDATE_BRIEF_V1_20260909.md`。
- `PAPER30_QPI_VERTICAL_ALPHA_CURRENT_PROOF_MAP_V1_20260909.md`。
- `PAPER30_QPI_JR_PUBLICATION_SOURCE_CHECK_V1_20260909.md`（下称 JR-source）。
- `PAPER30_QPI_VERTICAL_ALPHA_NOVELTY_PHASE_B_V1_20260909.md`（下称 VB）。
- `PAPER30_QPI_VERTICAL_ALPHA_NOVELTY_PHASE_CD_V1_20260909.md`（下称 VCD）。
- `PAPER30_QPI_VERTICAL_ALPHA_HEIGHT1_SOURCE_DELTA_V1_20260909.md`（下称 H1-source）。
- `PAPER30_QPI_VERTICAL_ALPHA_OBSTRUCTION_CARTIER_SOURCE_DELTA_V1_20260909.md`（下称 OC-source）。

另按引用身份定向读取旧来源报告中的匹配段，未全扫历史账本或构建树。
这些定位文件同在 `docs/research-batch07/`：
`PAPER30_QPI_INTEGRAL_NOVELTY_PHASE_B_V1_20260909.md`（整数 B）、
`PAPER30_QPI_NOVELTY_PHASE_CD_V1_20260908.md`（旧 CD）、
`PAPER30_QPI_DIVIDED_DIFFERENTIAL_SOURCE_DELTA_V1_20260909.md`（Ddiff-source）、
`PAPER30_QPI_COHOMOLOGY_SOURCE_SCREEN_V1_20260909.md`（cohomology-source）。
下文“继承阅读”仅指上述输入及被具名定位的既有记录所载实读，不冒称本轮亲读原文；
“本轮阅读”明确区分元数据、作者正文文字、PDF 抽取及未取得的图像。
公开检索只用于这批引用的身份与必要定位；未调用书目 API、付费/登录入口或上传私稿。

消费者代号沿用当前 proof map：P/Nbd/Gfield/Gint 为原模型与 pencil，Jspec/Wreuse/Hloc/SH 为
实际 Jacobian 与完整光滑闭能级，Ddiff 为先除后约化形式，DB/prime/TH/OC 为首层，TB/P2/PI 为高层。
`S` 表示标准工具或原对象来源；`B` 表示背景；`L` 表示相关工作及适用限制。
17 条是有实际消费者的上限计划，不是引用数量验收。未出现正文消费者时应删去对应可选条目。

## 2. 已核身份与推荐 citation keys

刊本身份与实际读取版本可以不同；正文的公式/定理号必须指向实际读取版。
DOI 为稳定定位，不代表本轮已取得其后全部出版正文。

| Key | 已核作者、准确题名及出版身份 | 官方/作者定位及版本说明 |
|---|---|---|
| `JoshiRoffelsen2026` | Nalini Joshi and Pieter Roffelsen, *Arithmetic dynamics of a discrete Painlevé equation*. Journal of Physics A: Mathematical and Theoretical **59** (2026), 195201. | [DOI 10.1088/1751-8121/ae67bf](https://doi.org/10.1088/1751-8121/ae67bf)；[作者 arXiv v2](https://arxiv.org/abs/2508.18578v2)，2026-01-16。出版身份依 JR-source 所核出版社提供同文全文；本轮重核作者页与 arXiv 元数据。 |
| `JoshiLobb2016` | Nalini Joshi and S. B. Lobb, *Singular dynamics of a q-difference Painlevé equation in its initial-value space*. Journal of Physics A: Mathematical and Theoretical **49** (2016), 014002. | [DOI 10.1088/1751-8113/49/1/014002](https://doi.org/10.1088/1751-8113/49/1/014002)；[arXiv v3](https://arxiv.org/abs/1407.1961v3)，2015-08-01。作者元数据名为 Sarah Lobb；刊本引文用 S. B. Lobb，不从记忆展开中间名。 |
| `GrossHackingKeel2015` | Mark Gross, Paul Hacking and Sean Keel, *Moduli of surfaces with an anti-canonical cycle*. Compositio Mathematica **151**(2) (2015), 265–291. | [出版社元数据](https://www.cambridge.org/core/journals/compositio-mathematica/article/abs/moduli-of-surfaces-with-an-anticanonical-cycle/DEE22E3839DD39806C2E3D1E5A63EB4E)，DOI **10.1112/S0010437X14007611**；[作者 v5 PDF](https://paulhacking.github.io/mlp.pdf)，2014-06-30。在线发表 2014-10-09，不替代刊本年 2015。 |
| `CantatDolgachev2012` | Serge Cantat and Igor Dolgachev, *Rational surfaces with a large group of automorphisms*. Journal of the American Mathematical Society **25**(3) (2012), 863–905. | [作者提供刊本 PDF](https://sites.lsa.umich.edu/idolga/wp-content/uploads/sites/1334/2024/08/jams12.pdf)，DOI **10.1090/S0894-0347-2012-00732-2**；[arXiv v2](https://arxiv.org/abs/1106.0930v2)，2012-01-25。纠正旧 CD 表中错误期刊名，不修改旧原件。 |
| `Beauville1990` | Arnaud Beauville, *Jacobiennes des courbes spectrales et systèmes hamiltoniens complètement intégrables*. Acta Mathematica **164** (1990), 211–235. | [作者出版目录第 41 项](https://math.univ-cotedazur.fr/u/beauvill/bibli.html)、[作者原 PDF](https://math.univ-cotedazur.fr/u/beauvill/pubs/jacspec.pdf)；[DOI 10.1007/BF02392754](https://doi.org/10.1007/BF02392754) 重定向至期刊档案。当前作者目录核准题名/年/卷/页；不把空白档案页当全文。 |
| `InoueVanhaeckeYamazaki2015` | Rei Inoue, Pol Vanhaecke and Takao Yamazaki, *Algebraic integrable systems related to spectral curves with automorphisms*. Journal of Geometry and Physics **87** (2015), 198–216. | [DOI 10.1016/j.geomphys.2014.07.008](https://doi.org/10.1016/j.geomphys.2014.07.008) 的出版社检索元数据；[作者 arXiv v1](https://arxiv.org/abs/1312.4208v1)，2013-12-15。以作者正文编号定位；直接出版页 403 后停止。 |
| `StacksProject2026` | The Stacks Project Authors, *The Stacks Project*，持续维护在线参考，访问日期 2026-09-09。 | [minimal model 定义 0C2V](https://stacks.math.columbia.edu/tag/0C2V)、[唯一性 0C6B](https://stacks.math.columbia.edu/tag/0C6B)、[mapping property 0C9Z](https://stacks.math.columbia.edu/tag/0C9Z)。一条总书目，正文每次给准确 tag；2026 是访问版本标记而非初版年。 |
| `AchterHowe2019` | Jeffrey D. Achter and Everett W. Howe, *Hasse-Witt and Cartier-Manin matrices: A warning and a request*. In *Arithmetic Geometry: Computation and Applications*, Y. Aubry, E. W. Howe and C. Ritzenthaler (eds.), Contemporary Mathematics **722**, American Mathematical Society, 2019, 1–18. | [DOI 10.1090/conm/722/14534](https://doi.org/10.1090/conm/722/14534)；[订正版 arXiv v5](https://arxiv.org/abs/1710.10726v5)，2020-02-07。作者明确说明 v5 修正 §2.5 错误；建议刊本条目加 corrected-version note 与 v5 URL。 |
| `Vlasenko2018` | Masha Vlasenko, *Higher Hasse–Witt matrices*. Indagationes Mathematicae **29** (2018), 1411–1424. | [作者出版页](https://www.imath.kiev.ua/~mariyka/)、[DOI 10.1016/j.indag.2018.07.004](https://doi.org/10.1016/j.indag.2018.07.004)、[arXiv v3](https://arxiv.org/abs/1605.06440v3)，2018-04-17。原文身份已核；另有未取得的一手勘误线索，见 §5，不将原版称为已核无勘误终版。 |
| `BeukersVlasenko2021` | Frits Beukers and Masha Vlasenko, *Dwork crystals I*. International Mathematics Research Notices **2021**(12), 8807–8844. | [DOI 10.1093/imrn/rnaa119](https://doi.org/10.1093/imrn/rnaa119)、[arXiv v4](https://arxiv.org/abs/1903.11155v4)，2021-05-31，作者元数据说明编号匹配刊本。不要写成 Dwork II 的 rnaa120 或仅用 online-first 年。 |
| `Vlasenko2024` | Masha Vlasenko, *Cohomology and congruences*. arXiv:2412.13313v1 (2024-12-17)，作者讲义/预印本，未核刊本。 | [官方元数据](https://arxiv.org/abs/2412.13313v1)、[作者 HTML](https://arxiv.org/html/2412.13313v1)。正文标题为 *Congruences and cohomology*；建议书目从官方 metadata，附 note 说明正文题名次序相反。 |
| `DeligneIllusie1987` | Pierre Deligne and Luc Illusie, *Relèvements modulo p² et décomposition du complexe de de Rham*. Inventiones Mathematicae **89** (1987), 247–270. | [出版社 DOI 10.1007/BF01389078](https://doi.org/10.1007/BF01389078)、[作者 IAS 原 PDF](https://publications.ias.edu/sites/default/files/Number57.pdf)。本轮核出版元数据；原文范围继承 OC-source，不冒称本轮通读。 |
| `DupuyZureickBrown2019` | Taylor Dupuy and David Zureick-Brown, *Deligne–Illusie Classes as Arithmetic Kodaira–Spencer Classes*. Journal de Théorie des Nombres de Bordeaux **31**(2) (2019), 371–383. | [官方刊本元数据](https://www.numdam.org/articles/10.5802/jtnb.1086/)、[正式 PDF](https://www.numdam.org/item/10.5802/jtnb.1086.pdf)，DOI **10.5802/jtnb.1086**。这篇只有两位作者。 |
| `DupuyKatzRabinoffZureickBrown2019` | Taylor Dupuy, Eric Katz, Joseph Rabinoff and David Zureick-Brown, *Total p-differentials on schemes over Z/p²*. Journal of Algebra **524** (2019), 110–123. | [DOI 10.1016/j.jalgebra.2019.01.003](https://doi.org/10.1016/j.jalgebra.2019.01.003)、[作者 arXiv v1](https://arxiv.org/abs/1712.09487v1)，2017-12-27。不能与两作者 JTNB 文混写。 |
| `LubinTate1966` | J. Lubin and J. Tate, *Formal moduli for one-parameter formal Lie groups*. Bulletin de la Société Mathématique de France **94** (1966), 49–59. | [官方原文元数据](https://numdam.org/item/BSMF_1966__94__49_0/)、[官方 PDF](https://www.numdam.org/article/BSMF_1966__94__49_0.pdf)，DOI **10.24033/bsmf.1633**。依官方书目保留作者首字母，不从记忆增补全名。 |
| `Shimada2026` | Kanau Shimada, *Arithmetic Kodaira–Spencer Class and Frobenius Liftings via Frobenius–Witt Cotangent Complex*. arXiv:2608.21772v1 (2026-08-22)，预印本，未核刊本。 | [官方元数据](https://arxiv.org/abs/2608.21772v1)、[作者正文](https://arxiv.org/html/2608.21772)。不写成已同行评审出版定理；不将抓取日期当发布日期。 |
| `KoroteevSmirnov2026` | Peter Koroteev and Andrey Smirnov, *On the Quantum K-theory of Quiver Varieties at Roots of Unity*. International Mathematics Research Notices **2026**(14), rnag153. | [DOI 10.1093/imrn/rnag153](https://doi.org/10.1093/imrn/rnag153)、[arXiv v4](https://arxiv.org/abs/2412.19383v4)，2026-06-02。正文定位依 v4，刊本身份由官方 arXiv metadata 与既有刊本核准继承。 |

## 3. 阅读账与实际正文消费者

以下“正文责任”是编写时的消费边界，不是把引用存在本身当成已完成证明。

| Key | 继承的原文实读范围 | 本轮原文/元数据实际读取 | 正文消费者、性质及限制 |
|---|---|---|---|
| `JoshiRoffelsen2026` | JR-source：出版社提供同文全文已读；旧积分来源另实读作者 v2 §3.1。 | 作者出版页、arXiv 身份；作者 v2 §2.1 原图和 §3.1 的原矩阵/迹式等返回正文，非出版 PDF 图像审计。 | P/Gint/Ddiff/prime 的原对象来源 `S`，引言归属 `B`。保留 w=1 的原积分、降序乘积及单位时间，不能以等谱矩阵替换。出版 Conj.3.7 与 v2 Conj.3.6 不同号。 |
| `JoshiLobb2016` | JR-source：作者 v3 印页 1–8 的 §§1–4，含初值空间、八点、反典范与 Picard 作用；附录仅 A 开头。 | arXiv 作者/题名/版本；未新通读 23 页，未取得刊本—作者版逐式差分。 | 原八点几何 P/Nbd 的 `S/B`。复数设置、t→0 自治极限和固定非零时间有限阶回返不可混同；原整数八截面图仍完整给出。 |
| `GrossHackingKeel2015` | 整数 B 报告：§1、Example5.6、Construction5.7、Remarks5.8–5.9、Lemma5.10、Cor.5.11、Thm6.1及证明。 | 出版社元数据；作者 v5 开头三页与 Example5.6/Construction5.7 文字。未通读全文。 | Nbd/DB 引入八环法丛与周期框架 `B/L`。八个 (-2) 环已有；基域为复数，不能将普遍周期族当作原整数节点单位复形或实际 Bockstein 的证明。 |
| `CantatDolgachev2012` | 旧 CD：作者 v2 Prop.2.2 及证明、Remark2.3。 | 作者提供刊本首页元数据及相关 Prop.2.2 定位文字，重核 v2 日期；非全篇证明审计。 | Gfield 的法丛精确阶/最小 pencil 标准机制 `S/B`。特征 2、3 的准椭圆可能仍须以原对象证明排除，不自动由 Halphen 一词得泛光滑。 |
| `Beauville1990` | Jspec 作者材料曾使用原文；旧独立 CD 明确只通过 IVY §4.3 核准重述，没有继承作者的原文阅读身份。 | 作者目录准确条目及其 25 页原 PDF 入口；该 PDF 未返回可核正文文字，图像请求也未产生可依赖的完整视觉阅读。 | Jspec 的历史谱线丛对应归属 `B`；实际可读定理陈述由 IVY §4.3 配引。不能把本轮取得 PDF 入口写成已新审计 Beauville 原证明。原矩阵的端点/有限推下/下降必须自证。 |
| `InoueVanhaeckeYamazaki2015` | 旧 CD：§§4.2–4.4，Thm4.4、Prop.4.5、Thm4.6及证明；Appendix Thm7.1及证明。 | arXiv 作者身份及版本、出版社搜索元数据；本轮未重读这些完整证明。 | Jspec 的 Beauville 对应、循环不变 Picard/拉回机制 `S/B/L`。其复数域、矩阵秩等于循环素数阶等条件不可删除；本题秩二任意 m 及任意原域不是直接实例。 |
| `StacksProject2026` | 旧 CD：Def.55.8.4、Lemmas55.10.1–2及证明；Fitting 07ZA、光滑提升 07LW 等标准段。 | 0C2V、0C6B、0C9Z 的完整条目及相关条件。 | Hloc/SH 的正亏格光滑射影泛曲线最小正则模型唯一性 `S`；双方在同一 DVR 上且已证明最小，方能延拓。0C2R/0C9Y 是节 tag，不冒充准确 lemma tag。 |
| `AchterHowe2019` | Ddiff-source：订正版 v5 §§1.2、2.2、2.4–2.5、3.1、3.3；cohomology-source 再核 §§3.1、3.3。 | v5 官方元数据、书目、§2.5 correction note；未重审全部正文。 | Ddiff/SH 的 Cartier/Frobenius 半线性与奇特征四次系数公式 `S`。正文必须区别正/逆 Frobenius及矩阵作用方向；特征二使用本文独立 W0/Cartier 计算。 |
| `Vlasenko2018` | VB：§1定义(1)–(4)、Thm1(i)–(iii)、Thm2前后条件、Lemma7和Thm1(i)证明；旧形式群 §4 证明记录不转为本轮实读。 | 作者身份/出版页、arXiv v3 metadata；本轮没有取得勘误一手正文。 | 相关工作 `L`：原 v3 Thm1(i) 已包含模 p Hasse 迭代；Thm2 的形式群整性原陈述不要求 ordinary。均不作本稿必要证明黑箱，见 §5。 |
| `BeukersVlasenko2021` | VB/VCD：§§1–3必要前提、Prop.3.3，Thm4.3/Remark4.4及应用证明，§5 Lemma5.1/Prop.5.2/Thm5.3及证明。 | v4 作者/题名/刊本 metadata 与编号匹配说明；未独立复证 contraction 引理。 | Ddiff/TB 前后的相关工作 `L`；unit-root 商及导数同余使用 Hasse–Witt 可逆与指定 Frobenius lift；Prop.3.3取 p>2，不能移给当前 p=2 全称原理想。 |
| `Vlasenko2024` | VB：§4.3 Thm34及证明、§§5.1–5.4，尤其 Thm37、Defs38/41、Lemma40；VCD独立复核范围较窄。 | arXiv 日期/题名及作者页标题次序差异；不把先前阅读重报成本轮完整阅读。 | 高层 TB/P2 的 related-work 限制 `L`，不是证明前提。所读 higher-Hasse 框架要求 k<p 及全部较低 Hasse 条件，第一级可逆不能抹去；未另读 Dwork III 全文。 |
| `DeligneIllusie1987` | OC-source：Thm1.2；Thm2.1(a)–(d)/Remark2.2(i)–(iii)，pp.249–254；§3.4、Thm3.5/Cor.3.6及构造证明，pp.262–264。 | 出版社准确作者/卷页/DOI；原 IAS PDF 的上述正文阅读为继承。 | OC 的 Cartier 同构标准背景 `S/B`；局部除 p Frobenius 微分/同伦、提升 gerbe 已有 `L`。DB的指定 J 连接类和原迹 pπ 同余均由本稿计算，不由 DI 自动代签。 |
| `DupuyZureickBrown2019` | OC-source：Remark1.1/Thm1.2，§§2.1–2.7，§3局部兼容及Lemmas3.2–3.3/Thm3.4证明。 | 官方 numdam 完整 metadata；本轮未重复原 PDF 证明。 | DB/OC 引言定位 `L`，非必要黑箱。文中已允许分歧 π-形式模型，不能以“分歧底”排除；whole Frobenius lifting torsor 不等于指定函数 J 的连接。 |
| `DupuyKatzRabinoffZureickBrown2019` | OC-source：v1 §§2.1、2.7–2.15、Thms3.2/4.1及证明，另补PDF的基本正合列与 p>2 条件。 | 作者 v1 身份；刊本元数据继承已核来源。 | OC 的扩张类/cup-product机制归属 `L`；所读框架 W2(k)、p>2，目标 total-p 微分模与原相对余切模不同，不代替本稿实际比较。 |
| `LubinTate1966` | VCD：p.49问题/带标记等价、Prop.1.1、Thm3.1及证明文字、§§3.2–3.5；§3.5另有文字复读。 | numdam 官方 metadata；官方 PDF 的 §3.5 文字定向复读，公式 OCR 不清部分不逐式抄写，不称图像审计。 | P2/PI 后的特征二有限高度先例 `L`。§3.5确有二次无分歧二进底 R、R[[t]] 上椭圆提升族、F4 上高度二形式群；不只是抽象存在参数。其族到原状态两系数理想的运输不在该文。 |
| `Shimada2026` | OC-source：§2、Defs3.1/3.7、Thms3.3/3.9及证明、§4Thm4.2、§5Thm5.3/Cor.5.6–5.7；部分图像缺口仍在。 | arXiv v1 作者/日期/题名；未重核完整图式。 | 首层障碍相关工作 `L`，不是必要证明黑箱。一般 Frobenius–Witt/算术 KS 障碍不自动识别本文指定 J 的原线丛连接类；不能把 flat 版本说成完全不容分歧。 |
| `KoroteevSmirnov2026` | H1-source/VCD：v4 §5.2规范、§§5.3–5.6，Lemma5.1、(5.22)–(5.27)、Thms5.4–5.5及证明。 | arXiv v4 与刊本身份；未重跑本轮相关工作搜索。 | 引言和 prime/TB 前的根单位首非零分歧层先例 `L`；逆乘积、参数同缩放与等谱结论是指定量子 K 理论系统，不是原 qPI 两系数理想。 |

## 4. 正文调用建议与不得外包的证明

正文可以将条目合并消费，而不需要为每篇写单独的文献综述段落：

| 实际位置/责任 | 建议引用 | 引用后仍须保留的本文证明 |
|---|---|---|
| 引言，原研究问题和矩阵规范 | JR；必要时 JL | 不把原积分、原矩阵、原八点登记为本文新结果；原 w=1 与排序须明写。 |
| 原几何与边界法丛 | JL、GHK、Cantat–Dolgachev | 原八截面、单位帧、法丛阶、完整 pencil、非复合性及小特征泛光滑。 |
| 原谱 Jacobian 到闭光滑层 | Beauville、IVY、Stacks | 两图/端点、有限推下、状态有理逆、不变 Picard、无核及原域下降；双方最小正则模型前提。 |
| Hasse/Cartier 与先除后约化 | Achter–Howe订正版；DI；相关段 Vlas2018 | 原积分与谱系数的实际认同，完整光滑闭纤维运输，p=2 独立计算，原整数整除和全图延拓。 |
| 指定 J 的实际 Bockstein 与首层理想 | DI、两篇 Dupuy；需要最新邻域时 Shimada | DB的真实常数/节点复形/连接箭头，prime的 pπ 同余，OC的像层 Frobenius与Čech符号。 |
| 高层 first jet及特征二高度二 | BV2021、Vlas2024、LT1966；根单位规范比较用 KS | TB/P2全 tame 内外部项、时间双数像、非约化限制单射、PI两次整除及混合理想。 |

标准唯一性已经有 Stacks 精确条目，当前不另加入 Liu 书籍条目；避免同一工具重复铺书目。
如正文确实使用 Fitting 表示独立/基变换，可在同一 Stacks 条目下用
[Lemma 15.8.4 / 07ZA](https://stacks.math.columbia.edu/tag/07ZA)；它的阅读为旧来源继承，
本轮没有用它创造新的 Fitting 理论。系数理想定义及本稿需要的基变换可直接说明。

GHK 已承接八环与周期背景，Cantat–Dolgachev 承接法丛阶与 pencil；Friedman 不为补数加入。
同理 Mellit–Vlasenko 的常数项同余、Dwork II/III、Fonseca/Movasati 的补基叙述、Bai–Lee、
Urbanik–Yang、Rezchikov、Wu 等不自动全入正文：当前直接计算和以上代表已覆盖实际消费者。
这不是排除这些工作的优先权；若稿件新增对应具体论断，必须先给准确来源与范围，不能借本表替代。

## 5. 新发现但未核清的勘误线索：保留未知，不作为书目成品

在核 Vlasenko2018 出版身份时，一个自动生成的公开聚合页面显示
*Erratum to: “Higher Hasse–Witt matrices” [Indag. Math. 29 (2018) 1411–1424]*，
并给出 2019、30(4)、DOI 线索 `10.1016/j.indag.2019.03.008`。
该聚合页没有原文，不能用作一手确认；本台账不给它正式 citation key 或可用 BibTeX。
定向打开 DOI 未取得可读正文；出版社卷目录返回 403；作者公开主页与 arXiv v3 未给出可读勘误。
这些失败入口已停止，不尝试登录、代理下载、程序化 API 或其他绕过方式。

目前不能核准勘误究竟改动哪个 theorem、公式、假设或证明，尤其不能宣称“与本文无关”。
也不能因未读勘误，反向宣称原版所有结论失效。当前正确状态是 `CORRECTION_IMPACT_UNKNOWN`。
原 v3 的已读陈述可以准确加版本限定地作为先例定位；没有把它升级成已核勘误后的结论。

| Vlas2018 原文范围 | 本稿计划用途 | 是否为必要证明前提 |
|---|---|---|
| Thm1(i)，及定义(1)–(4)/Lemma7中的模 p 迭代机制 | 说明 Hasse 乘积指数/半线性已有，原版范围不含 ordinary 假设 | **否**：Ddiff/prime/TB/P2所需原系数与循环词计算在完整正文自足给出。 |
| Thm1(ii)/(iii)，可逆时的矩阵极限/导数同余 | ordinary 条件的 related-work 边界，配 BV2021 | **否**：不能用来证明本文超奇异理想，也不将其可逆假设移给(i)。 |
| Thm2，形式群整性原陈述 | 非ordinary形式群先例，不把“非ordinary”自身算新机制 | **否**：本文没有把该形式群认同为原两状态系数理想；首 jet 来自原矩阵自足代数。 |

上述引用路由由当前完整 proof map 和主控明确的自足计算要求决定；不是通过未读勘误推定安全。
不得在写作时把这里的 related-work 条目悄然改成 necessary lemma citation。
若最终文字要强断言勘误后的精确原定理，或必须依靠该文某个不可替代结论，则该处仍是需要补源的缺口。

## 6. 其他残余边界与交接结论

Ohyama/GRT11 既有原文封锁不重试；Garcia–Tafazolian 原文未读缺口继续保留。
本文不依赖它们作为不可替代证明来源，也不根据未读正文作强排除性或全球首创判断。
Beauville 原 PDF 本轮虽找到公开作者入口，仍不称本轮新完成原证明阅读；正文可配 IVY 的已读重述，
并由 Jspec 的原对象自足证明承担实际识别。PDF 抽取和目录入口均不等于图像/图式审读。

按本台账路由，没有“身份未验证且又不可替代地充当必要证明前提”的计划条目。
这不等于所有相关来源缺口关闭：Vlasenko 勘误内容、Beauville 本轮未读原正文及上列旧缺口仍显式开放。
外部标准工具的适用条件、本稿每个原对象识别和完整必要证明必须在稿中实际落实；
本台账不替代 mathematical review、reference compilation、PDF 页数或产物验收。

交接时对本文件全文读回，并在交接消息报告终态行数及 SHA-256；不将文件自身 SHA 写回文件造成递归失配。
