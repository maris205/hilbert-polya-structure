# Paper30：qPI 圆分坏素数退化的有界先例核查 V1

日期：2026-09-09。执行者：`/root/p30_qpi_cyclotomic_prior_art_v1`。
性质：来源与适用条件筛查；不是正式查新票、Route 评价、证明接受或新候选立项。

## 1. 对主控判断的实际影响

**不能把“Frobenius／圆分 confluence／首非零 ramified jet”本身视为一个尚无人处理的机制。**
此次找到比一般 q-curvature 更近的先例：Koroteev–Smirnov 的根单位 quantum q-difference 研究，
2024 年首发预印本，2026 年已刊 IMRN；作者最新 v4 的 §5.5 直接抽取分歧参数的首非零项，
得到微分连接的 $p$-curvature。Bai–Lee 2025 又在圆分整数完成及关联分级语言中说明该极限。
因此，若拟议差额只是“将 $M_r$ 展开一次并认出 Frobenius 型项”，深入价值应下调，不能据新术语立项。
具体证据与版本见 §3 的 S4–S5。

与此同时，**本轮没有找到可以不经额外工作就覆盖原 qPI 完整能级 pencil 的混合特征野退化定理**。
这不是未有先例的保证：现有直接证据分别针对线性 q-difference 模、特定强 Frobenius 结构，
或 Nakajima variety 的 quantum connection；原 qPI 还缺相应结构、整数模型与参数归一化接口。
能否形成真正剩余，取决于一个内禀几何／动力结论是否超出这些标准机制；本报告不选择或证明它。

## 2. 范围、对象和实际检索

本地科学输入仅消费
[候选简报 V2 §§2–3](PAPER30_QPI_CANDIDATE_BRIEF_V2_20260909.md)
及[来源缺口处置 V1](PAPER30_QPI_SOURCE_GAP_DISPOSITION_V1_20260909.md)。
另读 `AGENTS.md`、`docs/WORKFLOW.md` 和 research-lit 技能全文。
初次显示简报的命令意外带出标题与 §1，已向主控披露；它们未作为本轮科学论据。
没有读取旧票、扫描论文库、调用书目 API、下载本地 PDF、对外发信、投稿或付费访问。
research-lit 采用用户限定的公开网页来源与阅读层级记录；不执行其默认本地库/API 流程。

沿用原对象

\[
F_t(x,y)=\left(\frac{st}{sx-y},\frac{sx}{y}\right),\quad t\mapsto st,\qquad
M_r(z)=A(s^{r-1}z)\cdots A(z),\quad I_r=\operatorname{tr}M_r(1)-(t^r+1).
\]

待筛问题是：特征零中 $s$ 精确 $r=mp^a$ 阶、$p\nmid m$，在 $p$ 上的素位降成精确 $m$ 阶时，
对原整数对象的混合特征退化进行研究。旧 T1–T7 的正特征输入是剩余域中实际精确阶，故不直接等同于该退化问题。
任务给出的零阶预计式为 $\overline I_r=(\overline I_m)^{p^a}$；本件不提供其证明，
也不将矩阵重复乘积／特征 $p$ 迹恒等式登记为新结果。
这里文献的 $q$ 一般对应本地 $s$，而不是有限域大小。

2026-09-09 实际执行八个主题 query，随后仅增加一次精确书名定位以核最新原始来源：

| 编号 | 完整 query | 本轮用途／所得边界 |
|---|---|---|
| Q1 | `"q-Painlevé" "root of unity" characteristic cyclotomic` | JR 原对象与圆分积分；未给目标野退化专论 |
| Q2 | `"q-difference" "curvatures" cyclotomic Di Vizio` | Di Vizio–Hardouin 的圆分曲率理论 |
| Q3 | `"q-Painlevé" "positive characteristic" isomonodromy` | 未定位可核的原 qPI 混合特征 isomonodromy 定理 |
| Q4 | `"q-difference" "cyclotomic" "higher" curvature` | 高阶相关入口有限，不据无结果排除先例 |
| Q5 | `"q-isomonodromy" "characteristic"` | 多数非本问题，未追宽泛经典 isomonodromy |
| Q6 | `"q-difference" "curvatures" 2024 2025 2026` | 近期 Frobenius／quantum K-theory 线索 |
| Q7 | `"Strong Frobenius structures associated with q-difference operators"` | Vargas-Montoya 出版全文与作者版身份 |
| Q8 | `"q-difference" "cyclotomic" Frobenius divided power jets` | 模圆分同余、近期 quantum Adams、分次结构风险 |
| B1 | `"On the quantum K-theory of quiver varieties at roots of unity"` | 从 Bai–Lee 的 KS24 引用追到原文 v4 与 2026 出版记录；非新增宽搜 |

后续只按已有链接和正文节号读取。搜索索引的抓取时间不当作发表时间；第三方聚合结果只作入口，
下述结论依据一手作者版、作者机构托管或出版社网页。

## 3. 六项最直接来源及阅读层级

| ID | 文献、时间／发表状态、一手入口 | 本轮实际读取 | 与目标的关系 |
|---|---|---|---|
| S1 | Nalini Joshi, Pieter Roffelsen, *Arithmetic dynamics of a discrete Painlevé equation*，作者 v2（2026-01-16）；[arXiv HTML](https://arxiv.org/html/2508.18578v2) | §3.1 定理 3.1、Remarks 3.2–3.5 与证明；标题与对象段。未重读出版全文 | 原整数 $I_r$ 和谱乘积的直接先例 |
| S2 | Lucia Di Vizio, Charlotte Hardouin, *On the Grothendieck conjecture on p-curvatures for q-difference equations*，2012 预印本；[arXiv 元数据](https://arxiv.org/abs/1205.1692)、[作者机构 PDF](https://www.math.univ-toulouse.fr/~hardouin/qGKgeneric-2.pdf) | 机构稿页首日期 2011-12-28；在线 PDF 文本引言、§§1.3/1.5、Prop.1.8/Rem.1.9、Thm.4.12/Cor.4.15、§5 三分情形和 Thm.5.4。非全文、未核出版版 | 曲率、非约化商、高阶除幂与正特征迭代均有成熟先例 |
| S3 | Daniel Vargas-Montoya, *Strong Frobenius structures associated with q-difference operators*，The Ramanujan Journal 67, article 56（2025-05-23）；[出版 HTML](https://link.springer.com/article/10.1007/s11139-025-01098-3) | Definition 1.1、Theorems 1.2–1.3、§2 环与 Frobenius 定义、§3.1 开头、§4 末同余及 §4.1/§5 指定段。非全文 | 明确处理 confluence 与模 $\Phi_p(q)$ 同余，不是只有标题相似 |
| S4 | Peter Koroteev, Andrey Smirnov, *Quantum K-theory of quiver varieties at roots of unity*，IMRN 2026(14), rnag153，2026-07-10；[出版摘要](https://academic.oup.com/imrn/article-abstract/2026/14/rnag153/8729579)、[作者 v4 HTML](https://arxiv.org/html/2412.19383v4) | 出版元数据／摘要；2026-06-02 作者 v4 §§5.1–5.5 指定段，Lemma 5.1、式 (5.25)–(5.27) 与 Thm.5.4。未读出版正文、未全文读作者版 | 本轮对“首非零分歧项”最接近、最能改变判断的先例 |
| S5 | Shaoyun Bai, Jae Hee Lee, *Quantum Adams operations in quasimap K-theory*，2025-10-10 预印本；[作者 v1 HTML](https://arxiv.org/html/2510.09335v1) | 引言主张、§3.3 定义、§5.2 Thm.5.5、§5.4 Lemmas 5.10–5.11/Prop.5.12、§6.2 开头指定段。非全文 | 将 S4 的极限解释为圆分完成上特定关联分级项；不是 qPI pencil 定理 |
| S6 | Andrey Smirnov, *Frobenius intertwiners for q-difference equations*，2024-05-31 首发、2025-02-24 v2；[arXiv 摘要与版本页](https://arxiv.org/abs/2406.00206) | **只读摘要与版本元数据**；未读正文、未核正式发表状态 | 特定 q-hypergeometric／$T^*\mathbb P^{n-1}$ 上的显式 Frobenius 结构；用于保留近期构造风险，不据摘要排除完整先例 |

### S1：原圆分整数结构已经提供约化入口

JR Theorem 3.1 的系数环就是圆分整数，Remark 3.2 特别强调模素数可约化性；
Remark 3.4 和证明给出整个矩阵迹多项式。不能把“从圆分整数约化原积分”称为新方法。
本轮已读段未陈述 $r=mp^a$ 坏素位的完整相对 pencil 或首非零 jet；这只是指定段的边界。
[S1 §3.1](https://arxiv.org/html/2508.18578v2#S3.SS1)

### S2：不能用“高阶／非约化”绕开已有 q-curvature

S2 §1.5 已在可能非约化的 $\mathcal A/(\phi_v)$ 上定义曲率；Prop.1.8/Rem.1.9
在整性及零曲率条件下把高阶除幂算子与 iterative q-difference 结构连接起来。
§4 的正特征分解处理 $p^\ell$ 次迭代与非约化 generic Galois group。
但 §5 将固定根单位、超越参数、非根单位代数数分开；固定根单位分支在统一曲率表述中用平凡赋值，
不是一个自动覆盖每个坏素位 jet 的结论。后两类的“几乎所有位”不能替代本题指定坏位。
[S2 作者稿 §§1.5、4、5](https://www.math.univ-toulouse.fr/~hardouin/qGKgeneric-2.pdf)

### S3：strong Frobenius 是额外结构，不由 Lax 相容自动产生

该文在 $\mathfrak m=(p,1-q)$ 的完成型系数环中工作，Frobenius 同时作用 $q\mapsto q^p,z\mapsto z^p$。
Definition 1.1 要求可逆 intertwiner；Theorem 1.2 是评价 $q=1$ 后保留强 Frobenius，
Theorem 1.3 在已存在该结构及整幂级数解的条件下给模 $\Phi_p(q)$ 的线性 Frobenius 同余。
§4 的特定一阶 q-hypergeometric 例子还有高次 $\mathfrak m$ 同余，不能宣称该领域只做零阶。
§4.1 仍将更一般 q-hypergeometric 强结构存在性列为问题。
这些不是任意 $A(z)$ 的通用定理；本轮未验证原 qPI 满足其前提。
[S3 Definitions/Theorems 1.1–1.3、§§2、4](https://link.springer.com/article/10.1007/s11139-025-01098-3)

### S4–S5：首非零圆分项已有非常接近的实现

S4 的对象是 Nakajima variety 的 quantum q-difference equation；其 §5 同时缩放 equivariant 参数。
在 $\pi^{p-1}=-p$、$q=1+\pi+O(\pi^2)$ 的设置中，式 (5.26) 给出

\[
\frac{\mathbf M_{\mathcal L_i^p}^{-1}-1}{\pi^p}\bmod\pi
=C_p(\nabla_i).
\]

这里是**指定归一化的逆乘积**和微分连接曲率，不是原 qPI 的迹或返回点。
其参数整性、近单位归一化与已构造 quantum connection 是实质前提。
[S4 作者 v4 §5.5](https://arxiv.org/html/2412.19383v4#S5.SS5)

S5 §5.4 则显式使用 $\mathbb Z_p[\zeta_p]$、$\zeta_p-1=\beta t$，
把特定 $\beta^p$ 项解释为关联分级中的曲率；相关公式和理论出处归给 S4。
§5.2 将 quantum Adams operator 与 $k$-curvature 相识别；一般 $k$ 不必是素数，
但 §5.4 的同调极限固定素数 $p>2$。不能将两处不同量词拼成任意 $mp^a$ 的野退化定理。
[S5 §§5.2、5.4](https://arxiv.org/html/2510.09335v1#S5.SS4)

S6 摘要另给特定 q-hypergeometric 方程上 $\mathbb Q_p$ 的 Frobenius action、
intertwiner 常数项公式及 $q\to1$ 极限。它的正文仍未核，故不作更强覆盖断言。
[S6 摘要](https://arxiv.org/abs/2406.00206)

## 4. 对拟议差额的适用性筛查（本轮判断，不是新证明）

| 拟议内容 | 已有证据造成的扣除／风险 | 真正未关闭的接口 |
|---|---|---|
| $\overline I_r=(\overline I_m)^{p^a}$ | 原整数乘积已是 S1；任务给出的重复块与迹 Frobenius 是初等机制，不足立项 | 本轮不证明；不能据此推出完整平坦模型、原能级重数或稳定化 |
| 任意“第一非零 uniformizer 系数” | S4–S5 已将特定首非零分歧项识别为 $p$-curvature；S2–S3 也包含高阶／非约化结构 | 原 qPI 的量、坐标／规范独立性、正确阶数和非零性尚未定义／验证 |
| 将 $M_m$ 调整成 $1+\pi\nabla+\cdots$ | S4 的近单位归一化不能直接搬用：本地原矩阵与能级通常非单位矩阵；改规范须保持原对象 | 可否在允许整数模型中做到；是否仅得到一般线性理论的标准例子 |
| 完整 $I_r=c$ pencil 的 wild 退化／适当稳定模型 | 本轮直接来源不等同于相对曲面／曲线稳定约化；“来源未覆盖”不等于该结果新 | 需先固定 DVR、能级及时间参数的提升、完整模型、基变换与目标几何结论；本轮均 OPEN |
| 返回动力与 Frobenius／乘 $p^a$ | 不能混同线性曲率、谱特征值的 Frobenius、曲线 Frobenius 态射及椭圆群乘法 | 须有同一原模型、同一指定返回点与态射的准确比较；旧 T1–T7 不能自动充当混合特征相容性 |
| 正特征 q-isomonodromy 一般定理 | Q3/Q5 没有定位可核的目标定理；线性 q-curvature 成熟不等于该桥梁已给出 | 保留正式概念与特定系统识别缺口，不把 formal Lax 相容写成未经构造的解析 monodromy |

### 主控补充的具体诊断量：仅记录待核适用性

落盘期间主控给出一个更具体、**尚未独审或接受**的诊断量：相对 $x,y$ 微分，
考察 $p^{-a}dI_r$ 的整数性，以及预计约化

\[
\overline{p^{-a}dI_r}
=\operatorname{Ha}_p(t^m,I_m)^{(p^a-1)/(p-1)}dI_m,
\]

其中主控拟将系数识别为原 Jacobian 的 Hasse 不变量；所述循环 trace 插入和
Cayley–Hamilton 推导均是主控未接受的工作线索，本件没有验证它们。

这比“首非零 jet”口号具体得多。**S4–S5 的上述已读结论没有直接给出这个量**：
其分母为近单位连接乘积的特定分歧参数幂，作用对象和参数缩放也不同；
它们没有在已读定理中将原 qPI 的相对积分微分、$p^a$ 整除性及 Jacobian Hasse 零点相识别。
这使该具体问题不能仅凭 S4 的标题判作已包含，也不能反过来宣称新颖。
本轮只补做 S4/S5 网页内 `Hasse`/`trace` 定点查找；无命中不是内容排除证明，
尤其网页字符串查找本身不可靠（S5 实际存在复数 `traces` 的段落）。
没有为此扩大主题检索；Cartier/Hasse–Witt、椭圆形式群及 trace 多项式微分先例的适用性仍未核。
主控若深入，应以这个准确量及非形式几何后果作为待查剩余，而不是以一般 confluence 机制作为差额。

本轮给主控的最小有用结论是：**如果没有完整几何／动力的不变量与非形式后果，这一方向不宜仅凭 jet 计算继续升级。**
若后续出现准确原对象上的剩余结论，仍需首先逐条对照 S2 的除幂/零曲率前提、S3 的强结构前提、
S4 的归一化和参数缩放，再评估其是否只是已有一般论的实例。
这条判断不改变 T1–T7，不生成 V3，不承诺证明可成或四门可过。

## 5. 未关闭来源与访问边界

- André–Di Vizio, *q-difference equations and p-adic local monodromy*，Astérisque 296（2004）, 55–111：
  [Numdam 书目页](https://www.numdam.org/item/AST_2004__296__55_0/)已核。
  在线 PDF 初次返回页数／文本索引，后续指定段读取反复 internal error／timeout，未得到所需原文段，停止该入口。
  关于其 $q$ 非根单位、
  $|1-q|<1$、Robba 环与 Frobenius／confluence 的条件，本轮仅直接读到 S3 §5 的回顾；
  不冒称已读 André–Di Vizio 原论证，不以该转述关闭原文缺口。
- Hardouin, *Iterative q-difference Galois theory*，J. reine angew. Math. 644（2010）, 101–144：
  书目及关联只来自 S2 的 Rem.1.9 与引用，未读原文。作者主页入口 internal error 后未继续展开查阅。
  不把“首阶已知”误写成“所有高阶 jets 均已分类”。
- Q8 还出现 prismatic/cyclotomic calculus 索引线索；未取得一手正文，不据标题声称能覆盖本问题，
  也未把它计入六项直接来源。一般 genus-one 稳定约化文献本轮未系统检索。
- qPII／qPVI 等对象未作身份确认的搜索结果仅为 `ROUND2_CLUE`；没有把其特殊解或不同 Lax 系统当原 qPI 先例。
- S5 初次手工尝试不存在的 v2 HTML 返回 internal error；随后沿 arXiv 正式 HTML 链接读取 v1。
  这不是访问限制绕行。S4 出版页实际仅给摘要，正文改读作者公开 v4，未尝试突破出版访问条件。

本轮没有任何全文全域排除结论，没有新意数字，没有基于搜索无命中的新意加分。
本件是唯一新建本地文件；未创建 Paper30 项目、实验、稿件、锁或 PDF。
交付后由执行者全文回读本件并向主控另报 SHA256 与行数；文件自身不放自引用哈希。
