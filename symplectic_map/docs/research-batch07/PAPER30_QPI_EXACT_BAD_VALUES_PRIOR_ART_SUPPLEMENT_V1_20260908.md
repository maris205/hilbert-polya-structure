# Paper30 qPI：准确坏值与临界重数的来源补充 V1

日期：2026-09-08。主控执行的有界 Phase A/B 补充；不是数学独审、正式新意票或立项。
本件补充[前三项查新证据](PAPER30_QPI_POST_BRIDGE_PRIOR_ART_SEARCH_V1_20260908.md)，
不改其冻结时准确坏值尚未核对的 `PENDING` 快照。

## 1. 新增被比较的准确 claim

输入为[全阶实际坏值作者稿](PAPER30_QPI_EXACT_BAD_VALUES_BRIDGE_ENTRY_V1_20260908.md)，
488 行，SHA256 `1e7ade432e62b1e116270d2588d0d798accbf482fcc6edd46dca12b76be42bb1`。
主控已全文读原稿及最后术语／CM 补充；该输入的新非作者数学核查另行进行。
本件不预判其审查结论。

设任意特征代数闭域上，$s,t\ne0$，$s$ 精确阶为 $r$，
$T=t^r$、$\varepsilon=(-1)^{r+1}$，原基底是 $c=I_r$。作者主张

$$
R_{r,t,s}(C)=\det(C\operatorname{id}-m_{I_r}\mid\Gamma(Z(dI_r),\mathcal O))
=C^4-\varepsilon C^3-8TC^2+36\varepsilon TC+16T^2-27\varepsilon^2T.
$$

这保留实际临界概形的非约化重数，不只是坏值集合相等；涵盖每个固定 $t\ne0$、
全部允许的 $r$，包括特征 $2,3$ 和坏值碰撞。它同时给原有限纤维的准确光滑判据。
不包括无穷远重纤维，也不声称全局 torsor 有截面。

机制分两层：

1. 在原 $c$ 上识别谱商的长 Weierstrass 模型
   $W:v^2+cuv-\varepsilon Tv=u^3-Tu^2$，其总空间正则、有限纤维整约化。
   实际模型经 henselian 局部截面平凡化后，由最小正则模型唯一性与 $W$ 同构。
2. 该同基底同构保留相对微分的 Fitting 临界概形；$W$ 的临界代数准确为
   $k[z]/((T-z^2)^2-\varepsilon Tz)$，其中原 $c=\varepsilon-z-z^3/T$。
   四维乘法特征多项式直接给上式。

待判断的差额是这个原模型／原参数／重数的精确对接，
不是一般最小模型理论、四次式本身或把同一判别式重新命名。

## 2. 实际公开检索

下列查询均由主控实际提交；结果并非数据库穷尽或完整引文图。
年份词检索外另列最近半年日期窗。未配置新工具或下载文件。

| Query | 结果与处置 |
|---|---|
| `"q-Painlevé" "critical" "discriminant" "2026"` | 未返回可核验的本题准确临界概形定理。 |
| `"Painlevé I" "Jacobian" "minimal" "root of unity"` | 大量连续 Painlevé／谱渐近近名项；未取得本题直接模型识别。 |
| `"Painlevé" "critical scheme" "2024" "2025" "2026"` | 无可核验的本题直接先例；不将无关 PDE／物理命中算覆盖。 |
| `"2508.18578" "discriminant" after:2026-03-08 before:2026-09-09` | 未得到可核实的新增证明／勘误。 |
| `"Arithmetic dynamics of a discrete Painlevé equation" singular` | 返回原 JR 作者／出版材料；最近直接先例仍是同一四次候选条件。 |
| `"q-Painlevé I" "singular" "elliptic"` | 返回 JR、Joshi–Lobb 初值空间／渐近工作及其他近邻；不能从题名判断后者解决有限阶问题。 |
| `"Halphen" "Jacobian" "singular fibres"` | 返回一般 Halphen／Coble 背景与讲义；标准模型关系需扣除，不以二手讲义支撑本题定理。 |
| `"Painlevé" "minimal regular model"` | 未得本题直接证明；实际使用的模型定理转读 Stacks／Conrad。 |
| `"q-Painlevé" "discriminant" "2024" "2025" "2026"` | 未检出本题准确临界重数的既成定理。 |
| `"Arithmetic dynamics of a discrete Painlevé equation" "3.7" "singular"` | 公开出版索引给出谱奇点讨论与 $s=\pm1$ 例子；没有取得出版 §3.2 全文。 |

Google Scholar、Semantic Scholar 引文图、Consensus 的具体执行／缺口沿用前三项证据包，
不把它们冒称为本件另外成功完成的完整前向引文检索。

## 3. 实际读到的最强先例与扣除

### 3.1 JR 原四次条件不是新公式

主控此前已全文读取 [JR 作者 v2](https://arxiv.org/html/2508.18578v2)，
本阶段再读 §3.2 的 Conjecture 3.6、谱奇点说明及 $s=1,-1$ 的代数例子。
四次式及它与退化的猜想关联都必须明确归于 JR。
本件作者证明若通过，提供的是原动力纤维的全量词证明和更强的临界重数身份。

[出版 DOI](https://doi.org/10.1088/1751-8121/ae67bf) 的公开搜索索引还显示
Conjecture 3.7、谱方程 (3.15)、相应奇点说明和两个例子。
本轮没有重新尝试被拒的全文访问，也没有取得完整出版 §3.2；
不据片段保证出版版每个量词与 v2 相同，正式对接采用实际可读作者版本。

### 3.2 局部模型与临界理想是既有理论

| 一手资料 | 主控实际读取及用途 |
|---|---|
| [Stacks §55.8](https://stacks.math.columbia.edu/tag/0C2R) | 模型定义、Definition 55.8.4，明确 regular 与 normal 不同；不含第一类例外曲线的最小正则 proper 模型定义。 |
| [Stacks §55.10](https://stacks.math.columbia.edu/tag/0C9Y) | Lemmas 55.10.1–2 的全部陈述和证明；任意 DVR、正亏格曲线的最小模型唯一性。 |
| [Stacks 55.14.7](https://stacks.math.columbia.edu/tag/0CDI) | 全部陈述与证明；好约化和最小模型光滑的关系。 |
| [Stacks 15.8.4](https://stacks.math.columbia.edu/tag/07ZA) | 全部陈述及证明，特别是 Fitting 理想任意基变换的矩阵论证。 |
| [Stacks §15.46](https://stacks.math.columbia.edu/tag/07QL) | 有限阶商／完成环相同、正则性和 DVR 保持的指定引理及证明；没有分歧更换原参数。 |
| [Stacks 15.9.14](https://stacks.math.columbia.edu/tag/07LW) | 完整陈述及证明：光滑点可在 étale 邻域提升，再消费 henselian 分裂。 |
| [Conrad, Minimal Models for Elliptic Curves](https://math.stanford.edu/~conrad/papers/minimalmodel.pdf) | §2 的任意 DVR 长方程定义；Corollary 2.9 的完整证明、判别式／微分变换与 Corollary 2.10；Theorem 3.10 及邻接模型说明。没有声称本轮通读其24页或Theorem2.8全部证明。 |

因此，已知泛 Jacobian、有限约化性和相对最小性之后，用局部截面比较模型不是新的一般原则。
Fitting 理想、特征多项式、长 Weierstrass 判别式的十二次幂变换也不计新理论。
潜在新 finding 是 JR 原动力模型满足这些条件，以及逐个有限 $c_0$ 的精确临界代数身份；
这是否足够非平凡须由后续独立候选判断，不在本件打分。

### 3.3 最近半年一手交叉检查

主控实际读 [Joshi–Lasic Latimer–Roffelsen, 2026-07-08](https://arxiv.org/html/2607.06980v1)
的摘要、§1 和 §2 Proposition 2.1 的证明。其 §1 仍将旧 qPI 曲线一般椭圆性称为猜想；
新文研究连续 Painlevé 的差分—微分 Lax 积分，不能当本题准确坏值桥。
这是一条支持问题仍被提出的近期证据，而非全局无后继证明的证书。

补充检索还定位到 [Willox–Grammaticos–Ramani,
The Trouble With Deautonomising Higher Order Maps](https://link.springer.com/article/10.1007/s11040-026-09563-1)，
正式日期为 2026-06-11。主控实际读摘要、完整 §1、§2 至式 (7) 及相邻说明。
其关注复数域高阶映射的去自治化／奇异型及次数增长；§2 从另一 QRT 递推开始构造高阶耦合。
这些读取段落没有本题有限阶原积分的临界多项式或有限域全轨道定理；
未通读其全部后续案例，不把标题里的 Painlevé 当成直接覆盖。

## 4. 合并时的准确边界

前三项证据包的 JRV 窗口、CD／CT Halphen、Mizuno 抽象格与 IVY 循环谱商扣除保持。
准确坏值是同一 qPI 问题的第四个比较维度，不拆成另一篇论文，也不靠模块计数增加价值。
本件有界检索仍为 `UNCERTAIN`：没有查明任何直接覆盖全量词的既成定理，
但“未查到”不保证全球首创，更不把方法先例的强重合淡化成无关背景。
后续 Phase C 应一并审查具体 finding、非平凡差额和已有工具扣除。

本件只补充来源证据；不授予数学接受、候选四门 PASS、正文容量、论文完成或任何外部效力。
