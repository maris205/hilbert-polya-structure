# Paper30 几何周期检测：G1–G5 有界一手查新

日期：2026-09-06（UTC）。

状态：BOUNDED_PRIMARY_NOVELTY_CHECK；不是数学证明验收、容量评分、候选 PASS 或 Route A/B 评价。

## 1. 结论与适用边界

在本轮检索及下列六项核心一手来源的实际阅读范围内，**未定位到直接给出 G2 或 G5 完整量词交集的先行定理**。这个结论是 `NO_DIRECT_PRIOR_LOCATED_IN_BOUNDED_SEARCH`，不是“首次”“世界新颖”或文献穷尽证明；总体置信度为中等。

最值得保留的精确差异是：在本文固定的辛 Hénon 复合族中，不要求整体双曲、固定概形约化或耗散性；以几何周期点的标量轨道和，判定整个仿射平面上的**多项式**余边界。V1 给固定映射的所有充分大整数周期，并对次数有界的观测量统一；增补进一步声称固定有序次数族的全部复参数共用一个可终止符号搜索得到的周期，及其所有倍数。

必须大幅扣除的组成部分包括：Bousch/Paper29 的周期代数、轨道词与无混叠结构，一般 footprint/首项秩估计，BLS 鞍周期点计数，特征零迹形式检测约化商，以及 Nullstellensatz、有限开覆盖、Gröbner 理想成员判定和最小公倍数归并。**这些一般工具不构成新的理论原理。** G4 的次数常数也不应凭“未搜到同一个公式”被单列为强新意。

特别接近的 2024 年正比例 Livšic 定理，已经在双曲/Hölder 范畴内从正上密度零周期和推出 Hölder 余边界；因而“周期点正比例检测”这一宽泛表述已有强先例。它与本题的全参数、多项式转移函数、次数统一单周期结论仍有明确区别，不能单凭名称相近判为完整覆盖，亦不能在引言里忽略它。见下表 P4 的一手正文定位。

本报告对输入中“PROVABLE AS STATED”的措辞不作背书。后续若独立数学检查修正假设、对象或量词，必须按实际剩余命题重新解释本查新结论，不得保留较强旧表述来主张新意。

## 2. 冻结输入、声明分解与非目标

完整读取的本次作者输入：

- [rank-detection proof V1](PAPER30_GEOMETRIC_RANK_DETECTION_PROOF_V1_20260906.md)，320 行；SHA256 `9544b15fcef634697e21a33e85d55f0a656728ba01f225b47e57148d6009e79d`。
- [uniform-period addendum](PAPER30_GEOMETRIC_UNIFORM_PERIOD_ADDENDUM_20260906.md)，251 行；SHA256 `3a61b858489516689e33f709aaf1572e37754f2cc5840f412df1b403d9772839`。
- [saddle-count prior](PAPER30_GEOMETRIC_SADDLE_COUNT_PRIOR_20260906.md)，沿用其 BLS 适用性核查，不重新开展鞍点计数文献全景。
- [既有 landscape](PAPER30_LITERATURE_LANDSCAPE_20260906.md) 的几何问题及既有先例边界；[Paper29 preflight](PAPER29_POLYNOMIAL_COHOMOLOGY_LITERATURE_PREFLIGHT_20260906.md) 的 Bousch/有限 Livšic 相关段。

对象限定为输入中的递推
\[
X_{i+1}+X_{i-1}=p_i(X_i),\qquad \sigma=F^*,\qquad
\delta=\prod_{i=0}^{k-1}d_i>1,
\]
其中有序次数 \(d_i\ge2\)，最高次系数非零。不得擅自扩展为任意 Jacobian 的整个多项式自同构族。记 \(S_ng=\sum_{j=0}^{n-1}\sigma^jg\)，\(\deg g\le D\)。

| 声明 | 本轮查新的精确对象 | 不能偷换的边界 |
|---|---|---|
| G1 | 无混叠后，非余边界轨道和在完整周期代数中的乘法秩有正比例下界；据此界定其几何零点数。 | 不是一般新 footprint 定理；几何零点上界以 \(\delta^n\) 为基准，不等于直接宣称所有周期代数约化。 |
| G2 | 每个固定 \(F,D\)，存在 \(n_0(F,D)\)，对每个整数 \(n\ge n_0\) 及所有次数 \(\le D\) 的 \(g\)，在最小周期恰为 \(n\) 的全部鞍点上零和，当且仅当 \(g\) 是多项式余边界；全部 \(\operatorname{Fix}(F^n)\) 几何点亦可；非余边界有统一正比例非零值。 | 最小周期鞍点是点数，不是轨道数；\(n_0\) 可依赖映射；不是先假设双曲后求 Hölder 解。 |
| G3 | 单个数域系数映射上，迹 Gram 矩阵精确计数几何点，递增搜索某个足够周期并终止，得到点值意义的有限检测证书。 | 不是预先给出的周期上界、复杂度界或新迹形式定理。 |
| G4 | 用 mixed-radix 数位不等式将 G1 的密度常数加强为 \(\eta_D=1/C_D\)，\(C_D=\lfloor(D+2)^2/4\rfloor\)，不依赖系数和周期变量数。 | 中间数位乘积不等式的等号，不等于实际轨道和的秩界或最优检测阈值达到等号。 |
| G5 | 给定 \(\mathbf d,D\)，符号算法终止并输出 \(M(\mathbf d,D)\)，对全部允许复系数及所有 \(\deg g\le D\)，在完整 \(\operatorname{Fix}(F^M)\) 几何点上零和恰好刻画多项式余边界；所有正整数倍 \(M\) 同样有效。 | 不声称参数统一的“所有充分大整数周期”，不输出本文已算出的数值 \(M\)，不声称有效 BLS 收敛速率或实用运行时间；这里测试完整固定点集，不是只测最小周期 \(M\) 的点。 |

本轮不涉及量子周期商、wild cover、Weyl/Hochschild 方向；不评价是否足够独立长文，不把别的构造拼入本问题。

## 3. 检索方法、时间覆盖与阅读等级

采用 research-lit 的本地背景先行和一手原文定位流程，以及 novelty-check 的逐声明多角度、2024–2026/最近六个月筛查。按任务限定未建立 PDF 语料库、未另存论文 PDF、未上传或对外发信。未使用付费数据库；可用来源为公开网页索引、arXiv、作者机构页及出版社页面。Google Scholar/Semantic Scholar 的定向网页查询不能视为完整数据库检索。

没有找到技能约定的本地 arXiv 抓取脚本，按其回退规则使用 arXiv 网页检索及版本页。novelty-check 的独立 Codex MCP 跨模型复核在本环境不可调用，本轮未完成该阶段；没有以自身重复判断冒充独立复核。依限定不另派代理。技能建议的数值新意评分和继续/放弃裁决不适用于本有界任务，故不输出。

下表记录实际执行查询的代表式；同义拼写含 Hénon/Henon、Livšic/Livsic/Livshits、cohomological/coboundary。先筛命中，再读相关定理，不能以零命中本身证明不存在先例。

| 声明/角度 | 实际查询代表式 | 命中与用途 |
|---|---|---|
| G1：首项与几何零集 | `Henon footprint periodic`；`Henon hypersurface periodic points coboundary`；`periodic multiplication rank polynomial Livsic` | 定位一般 footprint/零维代数方法；未见直接的本题轨道和几何检测定理。 |
| G2：多项式 Livšic | `Henon polynomial coboundary periodic orbit sums Livsic`；`Henon Bousch cohomological equation polynomial periodic points`；`algebraic Livsic polynomial automorphism`；`"polynomial coboundary" "periodic"`；`"Hénon" "finite" "cohomological equation"` | Bousch 原文、经典/现代双曲 Livšic 为主要邻近来源；专门核查多项式解与 Hölder 解区别。 |
| G3：几何值与迹 | `Henon trace form periodic`；`Henon Hermite periodic polynomial`；`polynomial automorphism trace pairing periodic`；`finite algebra trace matrix distinct roots` | 命中成熟迹矩阵/根基算法；未定位本题的逐周期终止检测算法。 |
| G4：mixed-radix 次数密度 | `"mixed radix" "footprint" polynomial degree`；`"mixed radix" "zeros" "polynomial" "bound"`；`"Henon" "multiplication" "rank" polynomial periodic` | 大量不相关 FFT/计算代数命中予以排除；公式新颖性未获独立文献证明，一般数位算术不计作新原理。 |
| G5：统一代数 Livšic | `Henon Livsic uniform coefficients`；`polynomial coboundary periodic uniform`；`algebraic Livsic finite parameter`；`"algebraic Livsic" "uniform"` | 未定位允许全部复系数的统一点值单周期定理。 |
| G5：Noetherian 有限测试/符号终止 | `Hénon polynomial Livsic Noetherian finite period test uniform coefficients`；`"Henon" "coboundary" "Groebner"`；`"periodic orbit" "Livsic" "Nullstellensatz"`；`"Livšic" "algebraic" "Noetherian"` | 未命中所需完整交集；一般有限生成、秩开条件和理想成员算法作为标准工具扣除。 |
| 2024–2026 | `Henon coboundary after:2024-01-01 before:2026-09-07`；`"Livsic" "finite" "polynomial" after:2024-01-01 before:2026-09-07` | 2024 正比例 Livšic 和 2026 有限 Livšic 报告是重要近邻；后者只读到机构报告简介。 |
| 最近六个月 | `arxiv Henon polynomial cohomological periodic after:2026-03-06 before:2026-09-07`；`Livsic finite polynomial geometric after:2026-03-06 before:2026-09-07`；`Henon trace coboundary after:2026-03-06 before:2026-09-07`；`"Henon" "Noetherian" "periodic" after:2026-03-06 before:2026-09-07` | 时间窗口 2026-03-06 至 2026-09-06；核对 P5 的 arXiv 首次提交日期为 2026-06-28，不用页面抓取/HTML 内部日期冒充版本日期。 |

阅读标签：`PRIMARY_READ` 表示实际读到列明的原文位置；`SCREEN_ONLY` 表示摘要/报告介绍或既有记录，不能升级为全文核验；`INFERENCE` 表示本报告根据假设比较作出的判断，而不是来源原文声称本项目新颖。

## 4. 六项最接近的一手来源

| 文献、年份/状态及一手链接 | PRIMARY_READ：实际阅读范围 | 已有内容与本题的精确差异 |
|---|---|---|
| **P1** Thierry Bousch, *Algèbres de Hénon*，1992，作者列为未发表文稿。[作者原文](https://www.imo.universite-paris-saclay.fr/~thierry.bousch/preprints/alghenon.pdf)，[作者目录](https://www.imo.universite-paris-saclay.fr/~thierry.bousch/preprints/)。 | 全部 13 页；重点 §2、§3、§5.1–5.2 Theorem 3、§7。 | 已有二次 Hénon 周期代数的稳定基、包含重数的乘法谱/迹、无限词基与周期折返及均值稳定化。本轮未在其正文定位任意参数的几何点值多项式 Livšic 充要定理。P29 已吸收的基与无混叠不得重复申报；该“未定位”不抹除 Bousch 的基础贡献。 |
| **P2** Eric Bedford, Mikhail Lyubich, John Smillie, *Distribution of periodic points of polynomial diffeomorphisms of C²*, Invent. Math. **114** (1993), 277–288，正式发表；[作者预印本](https://arxiv.org/pdf/math/9301220v1)。 | 开头两页 §1 定义、Theorem 1、Corollary 1；计数适用性沿用本次专门 prior 的核查。 | 最小周期恰为 \(n\) 的鞍点数量满足 \(s_n/\delta^n\to1\)。对固定复多项式自同构适用，不加本题不具备的耗散或整体双曲前提。没有次数有界的多项式余边界检测或统一参数检测周期。计数本身全部扣除。 |
| **P3** Olav Geil, Tom Høholdt, *Footprints or generalized Bezout's theorem*, IEEE Trans. Inform. Theory **46**(2) (2000), 635–641，正式发表，DOI [10.1109/18.825832](https://doi.org/10.1109/18.825832)；[作者原文合集](https://people.math.aau.dk/~olav/footorgenBez.pdf)。 | 作者合集 PDF 第 5–6 页，内部页码 167–168，Theorem II.16.4 及证明；扫描页实际图像阅读。 | 几何零点数受 footprint 基数控制，加入方程的首项缩小 staircase；这是 G1 的成熟一般方法。该处不含 Hénon 轨道词、周期折返或多项式余边界的动力学结论。 |
| **P4** Caleb Dilsavor, James Marshall Reber, *A positive proportion Livshits theorem*, Proc. Amer. Math. Soc. **152**(11) (2024), 4729–4744，正式发表，DOI [10.1090/proc/16880](https://doi.org/10.1090/proc/16880)；[作者版 v2](https://arxiv.org/html/2304.01372v2)，2023-05-19。 | §1 Theorems 1.1–1.2、Axiom A 备注；§3.1 证明与 Theorem 3.3。 | 在传递 Anosov、实值 Hölder 设定下，正渐近上密度的零周期和已足以推出 Hölder 余边界；原文亦说明 Axiom A 微分同胚版本。其概率/中心极限定理机制不提供全体非双曲复参数、多项式转移函数，或对所有 \(\deg g\le D\) 统一的单周期阈值。不能声称本题发明了正比例周期检测。 |
| **P5** Fabrizio Bianchi, Yan Mary He, *A thermodynamic path metric for complex Hénon maps*, arXiv:2606.29363v1，2026-06-28，预印本；[一手正文](https://arxiv.org/html/2606.29363v1)，[版本记录](https://arxiv.org/abs/2606.29363)。 | §§1、2.1–2.4，重点 §2.6 Lemma 2.7。 | 在复 Hénon 双曲分量上，以复不稳定导数 cocycle 的协方差和 Hölder 余边界描述退化性。它是最近六个月内最直接的 Hénon/Livšic 近邻，但对象为导数 cocycle 和双曲分量，不是任意多项式 \(g\) 的全参数点值有限检测。 |
| **P6** Itnuit Janovitz-Freireich, Ágnes Szántó, Bernard Mourrain, Lajos Rónyai, *Moment matrices, trace matrices and the radical of ideals*，2008，arXiv 记录列 ISSAC 2008, 125–132；本轮使用 [2008-11-29 作者版](https://arxiv.org/html/0812.0088v1)。 | 引言 related work；§3 Definition 14、Proposition 20、Algorithm 21、Remark 22。 | 迹矩阵用于恢复零维理想的约化代数，已有精确符号/线性代数方法。特征零迹形式的根基/几何点计数用途全部扣除；该文专用算法另有 Gorenstein 等前提，不应抹去。它没有 Hénon 逐周期搜索由 BLS 保证终止的定理。 |

对 P1 最直接的防碰撞核对是：**13 页全文中未定位到“全部几何周期和为零，则为多项式余边界”的命题**。实际对应位置为 §5.1（pp. 7–8）的基与 wrapping、§5.2 Theorem 3（p. 8）的全周期均值稳定、§7（p. 10）的 holomorphic mixing；§8.1（p. 11）的极限双线性形式非退化引理明确未附证明；§9（pp. 12–13）讨论递归行列式问题。这些内容不能直接登记为已经给出该几何 Livšic 充要判据。[Bousch 原文](https://www.imo.universite-paris-saclay.fr/~thierry.bousch/preprints/alghenon.pdf)

P4 的结论转向复值 Hölder 函数可通过实虚部分比较，但这个简单操作仍不能把转移函数提升为 \(\mathbb C[x,y]\) 中的多项式。以上是对象/假设比较，不是本项目证明审查。

### 只作筛查或沿用既有记录的近邻

- Bruin–Holland–Nicol, *Livšic regularity for Markov systems*（2005）：本轮公开检索再次命中其 Hénon-like/Markov tower 可测正则性结果；[作者原文](https://empslocal.ex.ac.uk/people/staff/mph204/bhn_livsic.pdf)。本次仅摘要及搜索可见正文，相关更深阅读沿用 P29 记录，不计为本次第七篇全文核验。不能把 Hénon-like 的可测/Hölder 正则性当作全部复参数的多项式解结论。
- Thomas O'Hare 2026-04-16 的 [Georgia Tech 官方报告](https://math.gatech.edu/seminars-colloquia/series/cdsns-colloquium/thomas-ohare-20260416)，*A Finite Livsic Theorem for Anosov Flows with Exponentially Small Errors*：报告简介称与 Jonathan DeWitt、Spencer Durham、James Marshall Reber 合作，从长度至多 \(T\) 的周期约束获得指数小误差的近似解。`SCREEN_ONLY`，未取得对应完整定理；它提醒“有限 Livšic”不能不加修饰地宣称首次，但简介中的近似/Hölder/Anosov 对象没有直接覆盖本题精确多项式判据。
- Cantat–Dujardin 的 [2026 年 Hénon multiplier rigidity](https://arxiv.org/html/2603.09445v1)，按既有 landscape B1 的一手读证沿用完整迹谱及有限周期截断扣除。本轮未重新审阅全文；完整乘子谱确定映射的问题，与任意多项式观测量的余边界问题不同。不能将 G5 包装成“首个 Hénon 有限周期代数测试”。

## 5. 逐声明 prior/delta 矩阵

此处“剩余差异”只指已读先行来源未直接覆盖；不等于已证明新定理。置信度针对文献比较，不给数学正确性打分。

| 声明 | 强先例/应扣除部分 | 本轮剩余精确差异（INFERENCE） | 判断及主要风险 |
|---|---|---|---|
| G1 | P1/P29 的轨道词基与周期结构；P3 的首项/footprint 一般原理。 | 非余边界短词和在可能非约化周期代数中占据确定比例的乘法像，并用这个比例约束几何零值。 | 一般引理已有性：高置信；未见本题完整组合：中等置信。可能只是已有动力学词基上的短而自然的应用，不能把“秩”改名当作新一般方法。 |
| G2 | P2 的全整数鞍点渐近；P4 的双曲正比例 Livšic；P1/P29 的多项式代数结构。 | 不要求整体双曲/约化，对固定任意允许 \(F\)，每个充分大单周期即以几何值判定多项式余边界，且统一于 \(\deg g\le D\)。 | `NO_DIRECT_PRIOR_LOCATED`，中等置信。这是 V1 中最清楚的对象与量词差异；G1 一旦建立，调用 P2 的后半部分本身是短推论，不另算一套新计数理论。 |
| G3 | P6 的迹形式/约化计算，常规数域精确线性代数。 | 与 G1、P2 结合的单映射适应性周期搜索保证终止。 | 新应用式算法包装，不是新的求根或迹矩阵算法；未命中同一终止定理，中等置信，不支持复杂度新意。 |
| G4 | 数位归纳、二维次数乘积最大化、P29 次数三角化及 P3 型计数。 | 以 \(C_D=\lfloor(D+2)^2/4\rfloor\) 控制相关 Hénon 轨道词乘积，使密度只依赖普通次数。 | 精确公式先例未定位，但一般机制显然是初等估计；只宜作为本题定量加强。中间等号不赋予最终界最优性。 |
| G5 | P6 型迹矩阵及其秩子式；标准代数开条件、Nullstellensatz/有限生成、符号理想成员、最小公倍数。 | 在固定有序次数族上，覆盖包括退化及超越复系数的全部参数，以有限代数恒等式产生共同点值检测周期及其所有倍数。 | 完整交集未命中，中等置信；这是增补中最明确的声明差异。但从通用秩开证书到有限子覆盖和 lcm 的步骤是标准短链，不是新 Noetherian 原理，也不是统一 BLS 速率。 |

G2 与 P4 不是简单强弱关系：在 P4 的双曲/Hölder 类别中，非余边界的零周期和比例趋零，比 G2 给出的固定正比例非零更强；但其转移函数类别和对观测量的量词不能提供 G2 的统一次数多项式结论。本题若只保留“存在很多非零周期和”而删去全参数、多项式和单周期量词，则新意将被明显削弱。

G5 的核心区别应放在**这个特定检测性质确实由全参数的代数秩开条件覆盖**，以及其与本题几何值的连接。一般无限开覆盖有限化并不稀有；本报告不据“采用 Noetherian”提高新意等级。也不把“逐参数的所有充分大 \(n\)”交换为“某个统一阈值以后的所有 \(n\)”；增补实际只从有限周期证书归并出一个 \(M\) 及其倍数。

## 6. 可用定位、剩余不确定性与收口

可用的保守定位是：

> 在既有 Hénon 周期轨道代数及鞍点计数的基础上，以一个次数受控的乘法秩/零点界，将概形检测降到几何点值检测；进一步用参数族的代数证书获得统一的精确单周期判据。

这段定位仍须以独立证明审查通过的实际命题为准。不得写成“新 footprint 理论”“新鞍点渐近”“新 Hermite 形式算法”“新 Nullstellensatz”“所有复 Hénon 映射首个有限 Livšic”，或声称已给出可用数值周期/运行时间。

剩余文献风险主要是未公开或索引较差的 Hénon 多项式上同调文稿，以及可能采用不同术语陈述的代数有限检测推论。本轮六项核心来源均区分了实际阅读位置；2026 有限 Livšic 报告只作筛查，不因未获全文而宣布排除。一般多变量动力系统、任意代数群 cocycle、所有代数动力学有限性定理的引用网络没有穷尽，也没有必要据此扩展到另一个系统族。

综上，本轮找到了必须严肃扣除的强先例，但未找到直接消灭 G2/G5 精确对象与量词差异的一手定理。是否构成足够实质的新贡献，需要在数学审查和另外的候选评价中决定；**本文件不作该决定**。唯一新增本地文件是本报告，两个作者证明输入的 SHA256 与任务给定值一致；未修改冻结原稿、旧失败记录或其他项目。
