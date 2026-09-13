# Paper30 AS：先例扣除与自然正文范围预筛

日期：2026-09-07。性质：**作者侧有界文献／范围预筛，不是独立候选评价**。
本报告不作正式四门评分、不代替独立数学核查、不写稿或试编译，
不改变科学输入、冻结记录、Paper30 项目状态或正文 **22–30 页**要求。

## 1. 作者侧结论

当前包真正值得保留的是：固定二次 Hénon 族在所有奇特征、全部
多项式支撑上的 AS 特征类分类，以及进一步包括特征整除周期情形的
完整有限轨道分类。所查先例不能被解释成已经证明了这一分类。

但是例外曲面及其显式 lift 可直接由标准 Danielewski 自同构公式
得到，AS torsor 字典、有限维有限域线性代数和旧轨道基机制也须扣除。
把 scalar 和 matrix 公共证明只写一次、完整保留 vector 不消去与非半单
义务后，正常英文实质正文的作者估算为 **低 12、中心 16、高 20 页**。
这是未排版的范围判断，不是页数实测或严格上界。

因此作者侧建议：**当前四模块包自然范围不足，不为它立项；不进入正式
四门评审，不试写凑页**。这不是正式四门 FAIL，也不是数学失败。
本文件只提交建议；不登记项目处置、不假造正式评审结果。
即使矩阵证明独立核查通过，本范围估算仍适用。

## 2. 输入、读取层级及边界

本轮完整读取两份核心输入：

| 输入 | 行数 | 本轮读取时 SHA-256 |
| --- | ---: | --- |
| [完整奇特征分类](PAPER30_AS_FULL_ODD_CLASSIFICATION_20260907.md) | 205 | `bc98b7e02553909ccdecc0f77be4325e3e2a357f260d6535f6311d5d65cfde89` |
| [矩阵有限轨道证明](PAPER30_AS_FINITE_ORBIT_MATRIX_PROOF_20260907.md) | 244 | `04bb1abdf720a2a1862acd9be6aff7d01641eae957886d089a0269c01926373d` |

另读[双权重证明](PAPER30_AS_ODD_PRIME_EXCEPTION_PROBE_20260907.md)的数学论证、
[移位勘误](PAPER30_AS_SHIFT_FORMULA_ERRATUM_20260907.md)、
[旧桥接输入](PAPER30_AS_FROBENIUS_COINVARIANT_PROBE_20260907.md)的基、
twisted obstruction 与桥接部分，并定向读取 Paper29 引用记录和
[已接受 PDF](../../papers/29-filtered-henon-cohomology/build/natural-20260906-r1/work/main.pdf)
前三页。本报告不逐项验算新证明。

主控告知前三份 scalar 数学输入已独立通过，新的 matrix 输入正在另行核查；
这是分工状态说明，不是本报告授予的 PASS。旧输入中的历史 pending 字样
也不由本报告追溯修改。本次范围核算以当前作者矩阵主张成立为条件，
不预先消除其独立核查义务。

使用 research-lit 技能：检索和读取区分元数据、摘要、指定正文段落；
arXiv 仅摘要／元数据，不下载 PDF。无可用 Zotero／Obsidian 工具；
本地相关 PDF 文件名检索未找到 Danielewski／AS 外部论文。
Paper29 是项目自身的已接受成果，不当作外部一手文献。

## 3. 有界检索及真实读取记录

本代理新增查询恰为四条，之后未扩大搜索：

1. `Danielewski surface automorphism positive characteristic Lind 2009 xy P(z) generators`
2. `"Hénon" "Artin-Schreier" finite orbit`
3. `site:arxiv.org "Danielewski" automorphisms characteristic`
4. `"Dubouloz" "Poloni" "On a class of Danielewski surfaces" automorphism`

未找到 `arxiv_fetch.py`，依技能采用 arXiv 站点检索及官方摘要 fallback。
主控此前十条查询是独立的上游检索，本报告不把它们冒充本代理执行的查询。
下表只把本轮亲自打开的来源记为本轮读取；搜索摘要不是全文证据。

| 文献／来源 | 发表性质与实际读取层级 | 可支持的比较；不能支持的结论 |
| --- | --- | --- |
| L. Makar-Limanov, *On groups of automorphisms of a class of surfaces*, Israel J. Math. 69 (1990), 250–256，[官方页](https://link.springer.com/article/10.1007/BF02937308) | 同行评议论文；本轮打开官方摘要和元数据，全文订阅受限，未获取 | 摘要确认对象为 `xy=P(z)` 的自同构群。仅凭摘要不能确认完整定理假设、具体生成元，也不能推出或排除 AS 有限轨道分类。 |
| Andreas Lind, *Holomorphic automorphisms of Danielewski surfaces*, Mid Sweden University Doctoral Thesis 76 (2009)，[公开 PDF](https://miun.diva-portal.org/smash/get/diva2:277555/FULLTEXT01.pdf) | 一手学位论文；取得有效完整 PDF，直接读封面／摘要与 §2 相关正文，特别是内页 6–7 的 Theorem 2.1；未通读 87 页。该定理在论文内是对 Makar-Limanov 的二手转述 | 明列 n=1 的 swap、triangular、symmetry 与正特征 translation 公式，足够供本报告直接代入比较。没有把转述升级成“已读 Makar 原始证明”，也没有把整本复几何论文移植为本项目分类定理。 |
| Anthony J. Crachiola, *On automorphisms of Danielewski surfaces*, [arXiv:math/0406415](https://arxiv.org/abs/math/0406415), 2004 预印本 | 本轮打开官方摘要／元数据；未读正文 | 明确研究 `X^nY-Z^2-h(X)Z`、n≥2、h(0)≠0 的任意特征族。它是邻近自同构先例，不是当前 n=1、三次 AS 曲面的完整分类证据。 |
| Adrien Dubouloz–Pierre-Marie Poloni, *On a class of Danielewski surfaces in affine 3-space*, J. Algebra 321 (2009), 1797–1812，[官方 arXiv 摘要](https://arxiv.org/abs/math/0602549)，[作者出版列表](https://dubouloz.pages.math.cnrs.fr/perso/publis.html) | 同行评议出版元数据来自搜索所见出版社／作者页；本轮直接打开 arXiv v2 摘要，未读论文正文 | 摘要对自己的广义族明确 n≥2，任意基域。不能因 Lind 后续转述中出现 n=1 involution，就未经原文假设核对把其定理直接覆盖本问题。 |
| Stacks Project，[§59.63](https://stacks.math.columbia.edu/tag/0A3J) | 本轮直接打开参考正文，读取 AS 正合列、仿射上结构层上同调消失的使用、Lemma 59.63.2 的有限维 Frobenius 结论 | AS 正合列及仿射 torsor 字典是标准输入。有限维 Frobenius 的一般事实不能直接解出无限维 Hénon 商空间。 |
| Thierry Bousch, *Algèbres de Hénon* (1992)，未发表作者稿，[作者 PDF](https://www.imo.universite-paris-saclay.fr/~thierry.bousch/preprints/alghenon.pdf) | 本轮尝试打开未成功；只读取了[项目已存的一手文献定位记录](PAPER29_COHOMOLOGY_CITATION_RECORDS_20260906.md)及 Paper29 正文归属，不声称本轮重读原文 | square-free／bounded-exponent 基、wrapping、shift 先例必须归属。具体引用位置沿用已有记录而非本轮新核定；系数和判据另为直接线性代数后果。 |

Lind 下载采用新临时路径的一次常规公开请求，90 秒超时限，实际约 8 秒成功，
退出码 0；`pdfinfo` 成功解析为 87 页、581582 bytes、无加密。
所保留文件为 `/tmp/p30-as-scope-lind-g7aaFd/lind2009-complete-attempt.pdf`，
SHA-256 `7d63d37ff274a3654174b0837d9ffbb0288b5b6bd841966119e88c38742837a6`。
主控旧 294881-byte 部分下载未触碰、未用于读正文；本轮另一次网页 PDF
打开超时亦未当作全文。Lind 记录页出现 Anubis 挑战，未处理挑战、未绕过限制，
没有随后追加网络重试。Makar-Limanov 订阅限制同样保留。

## 4. 显式例外 lift 的标准生成元扣除

以下是**作者从已读标准公式作的直接代入比较**，不是声称 Makar-Limanov
原文明确写出了本例，更不是对完整 AS 分类的新独立证明。

在 p=3、c≠0、q²=−1/c 时，令

\[
P(z)=q^{-3}(z^3-z),\qquad Y_q=\{xy=P(z)\}.
\]

Lind Theorem 2.1(c) 所列三角公式，取常数 f=q，成为

\[
S_q(x,y,z)=\left(x,
y+\frac{P(z+qx)-P(z)}x,z+qx\right)
=(x,y+x^2+c,z+qx).
\]

最后一个等式只用特征三及 q⁻²=−c。由于 P 为奇多项式，
`R(x,y,z)=(x,−y,−z)` 是其符号对称；`I(x,y,z)=(y,x,z)` 是交换。
于是

\[
(I\circ S_q\circ R)(x,y,z)
=(x^2+c-y,x,-z+qx)=\widetilde F_c(x,y,z).
\]

所以曲面类型、这条显式 lift、显式逆以及把 lift 迭代 N 次，
都不能各自当成新的独立研究模块。正特征 deck translation 也已有标准形式。

但这项扣除没有证明：给定基底 F 后的所有可提升 cyclic degree-p covers
均为该曲面；也没有排除其他 p、c、任意多项式 AS 代表，或排除只在高次
迭代后才返回的 AS 类。这些是**变动 cover／AS 类上的穷尽问题**，
不等同于**一个已给定曲面的自同构群描述**。本轮有限检索未定位到相同
穷尽结论的先例；不能把“未定位”写成正式 novelty PASS。

## 5. 四模块净内容与相互重叠

| 当前模块 | 可以保留的对象专属净内容 | 必须扣除／合并的内容 |
| --- | --- | --- |
| scalar AS–Frobenius bridge | 在 Hénon coinvariant 上处理常数、半线性及全部 mixed 代表，明确桥接适用性 | AS 正合列本身、商空间的通用交换图逻辑、Bousch 基、Paper29 同族 orbit cohomology、加权系数和／有限支撑递推均不是新的框架；仍可短证自含性 |
| dual weights／全支撑不消去 | 修复后的相邻最小代表碰撞排除；双权重对 normal form 的兼容；无限 odd-reflection 层的唯一 surviving target；所有 p≥5 的统一 boundary word | 不重新写 Paper29 的离散凸性理论；旧错误与修复历史不进入正文主章；证明同一排除结论的多份笔记／重复检查不累计 |
| all-odd scalar classification | 全部参数、奇特征与 λ 的精确分类，以及 p=3 的唯一非零 AS 直线 | p=3,c=0 冗余核验不另算定理；末端 cubic 方程及 q 的选择为短计算；显式 Danielewski 存在公式不是独立主贡献 |
| matrix all-iterates and cover corollary | 常系数 T∈GL_r(F_p) 下的向量不消去，包含非半单 T；全有限轨道而非仅 scalar eigenclasses；由此得到所有正迭代的 cover 排他性 | r=1 桥接不能重写为第二个大章；循环矩阵编码、有限域乘法阶、M1⇒M2、deck 奇偶作用是短线性代数／字典推论，不拆成多个新模块 |

Paper29 的正式陈述是特征零，但其二次 orbit-basis／ordinary-degree 机制
已有具体本族先例。当前论文仍须交代为何所需 monic 重写在正特征成立，
不能直接套用特征零定理；这份必要适用性证明并不使旧机制变成新框架。

矩阵推广有实际价值：只分类 F_p 标量 eigenclasses 不控制所有有限轨道，
特别不能凭对角化处理 p 整除周期。因此正文必须保留 T 的 Frobenius
可交换性、T 加权有限支撑解、唯一目标向量 T^j t^[p] 非零、single-letter
block、循环编码等实际逻辑。另一方面，它们依赖同一套 scalar support
几何，最自然的完整写法是把公共引理向量化一次，再取 r=1，或先证 scalar
后逐项列出向量变更；不能将全部相同证明重复铺开来增加页数。

## 6. 正常英文正文的逐节自然估算

口径：正常数学论文版式、完整必要证明、适度背景和解释；不使用人为放大的
字号／间距，不计算参考文献页，不计 proof-log、审查报告、工作流状态、
冗余作者验算或可删重复证明。表中低／中心／高是同一净内容的紧凑／正常／
较充分讲解情形，不是已编译测量；高值已经允许清楚解释非半单情形。

| 正文章节与唯一计数内容 | 低 | 中心 | 高 |
| --- | ---: | ---: | ---: |
| 1. Introduction：问题、完整 finite-orbit 主定理、与曲面自同构先例的准确区别 | 1.5 | 2.0 | 2.5 |
| 2. Orbit preliminaries：归属、正特征适用性、必要记号，不复写 Paper29 | 1.0 | 1.5 | 2.0 |
| 3. AS–coinvariant bridge：常数与半线性，公共 scalar/vector 逻辑只计一次 | 1.0 | 1.5 | 2.0 |
| 4. Highest-orbit separation：相邻最小代表及修复后 collision 排除 | 1.0 | 1.5 | 2.0 |
| 5. Dual-weight obstruction：weight preservation、全部 odd-reflection 顶层、统一 p≥5 boundary | 2.5 | 3.0 | 3.5 |
| 6. All-odd scalar conclusion：single-letter cubic 计算与全参数分类 | 1.5 | 2.0 | 2.5 |
| 7. Matrix and all iterates：真正向量变更、非半单保护、finite-orbit 编码和 M1/M2 | 2.0 | 2.5 | 3.0 |
| 8. Covers：标准字典、connected／unmarked 区别、穷尽推论、生成元比较 | 1.0 | 1.5 | 2.0 |
| 9. Boundaries and conclusion：char 2、非闭域、高阶 cover 等未覆盖边界 | 0.5 | 0.5 | 0.5 |
| **合计** | **12.0** | **16.0** | **20.0** |

§4–5 是实质证明的主要空间；§7 不以“finite-dimensional linear algebra”
一句跳过非半单义务。§6／8 可以合并，表格分列只是便于核算，不主张必须
真的设置九节。末端三次计算和 cover 字典已给较充分篇幅；继续增加主要会
重讲同一结论，不自然产生达到 22 页所需的新增实质。

当前高值低于 22 页不能被写成排版不可能性的定理，但正常中心距离下限
明显，且没有已经证明而尚未计入的独立内容。作者不应为追到下限而展开
一般曲面自同构综述、重证 Bousch／Paper29、反复证明 scalar/vector 同式
结论，或补入特征二、非闭域、高阶 cover 等尚未建立的新范围。

## 7. 交付与接续建议

保留当前证明与独立核查成果；本轮文献层面承认可能有意义的完整有限轨道
分类，而范围层面不为当前四模块包建立 Paper30 项目。正文 22–30 页锁定
不变，不开展试写测页，不把作者范围不足伪装成两份正式四门 FAIL。

若未来出现真正不同且已证明的族内新增内容，可重新做净内容判断；只有
自然范围确实足够时，才建议进入**两份全新的正式四门评审**，不会由本报告
预授任何门的通过。本轮无稿件、构建、候选评分、Route 结论、状态登记或
外部写操作。唯一新增的工作区成果是本报告。
