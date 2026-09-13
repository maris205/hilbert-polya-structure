# Paper31：完整非单位候选关闭后的形变／野分裂文献地形 V1

日期：2026-09-10（项目日期）；执行席：主控 `/root`。
状态：`BOUNDED_PRIMARY_LANDSCAPE / IDEA_INPUT_ONLY / NO_NOVELTY_SCORE / NO_CANDIDATE_ADMISSION`。
`route_applicability: NOT_APPLICABLE`。这是新一轮发现的来源输入，不是新证明、先例穷尽或正式 Route／四门评价。

## 1. 本地起点与本轮问题

[完整候选双票处置][CLOSED]保持：同一非单位时间 C1–C3 数学接受，但新意与独立价值未准入；不得换名复投。
本轮先读本地接受 P30 PDF 的前3页，以及旧地形208行、旧十项生成164行、旧排名112行、Kummer接受50行；随后主控全文读取[新基线盘点][BASE]210行。
它们给出当前准确输入：原完整曲面／pencil／Jacobian、首层几何障碍及真实末端多截面已存在；完整非单位格链也已闭合。
原能量提升到整体曲线分裂的判别、一般 q 的跨次数乘法比较，并未由这些输入给出。
本件集中在前一处及其与联合形变的潜在接点；乘法来源由另一席单独交付，二者不互相代签。
未重扫旧 build 树、重开接受稿审查、执行 I09 固定对诊断，或把旧 HOLD 自动变成新的研究准入。

## 2. 实际检索与访问边界

先本地、后公开一手来源；未配置的 Zotero／Obsidian 工具未使用。未归档新 PDF，GPU 0；官方 PDF 的在线文本读取不等于下载加入文献库。
新检索重点是最近两年及最近六个月，必要基础文献明确保留旧年代，不按网页抓取日期误报新作。

| 序号 | 实际查询字符串 | 主要用途／结果 |
|---|---|---|
| Q01 | `genus one curves wild ramification torsors good reduction local field 2024 2025 2026 arxiv` | 野约化入口；弱相关结果未当作先例排除 |
| Q02 | `"q-Painlevé" "degeneration" "2026"` | 原族及近期退化检索 |
| Q03 | `"principal parts" "q" "integral" deformation arxiv 2025` | 联合形变入口；一般名称命中不证明对象相同 |
| Q04 | `"genus one" "torsors" "2025" reduction` | 曲线整体与 torsor 区分 |
| Q05 | `"genus one" "logarithmic" "good reduction"` | D2、D3 基础邻域 |
| Q06 | `"q-Painlevé I" "arithmetic" Joshi Roffelsen` | D1 原族核对 |
| Q07 | `"q-deformed" "principal parts"` | 仅作乘法／形变接口搜索，不据空命中给新意 |
| Q08 | `"torsion in the cohomology of wild elliptic fibers"` | D3 一手版本 |
| Q09 | `"Moduli of finite flat torsors over nodal curves"` | D4 最新版本与发表信息 |
| Q10 | `"log smooth curves" "Lodh"` | D2 的独立旧先例线索；未获取 Lodh 全文 |
| Q11 | `"genus one" "torsors" after:2026-03-10 before:2026-09-11` | 最近六个月补查；多项实际返回旧文，未误记为近期 |
| Q12 | `"q-Painlevé" after:2026-03-10 before:2026-09-11` | 取得 E1–E3 近期相邻工作，仅摘要层 |

官方 arXiv API 实际执行 `(all:"genus one" AND (all:torsor OR all:reduction)) AND submittedDate:[202403100000 TO 202609102359]`，最大10条、按提交日期倒序，HTTP 200，实际4条。
返回 2606.13161、2601.09666、2601.07070、2410.20831，分别偏结、Chern–Simons、wedge、Hurwitz／热带问题，均未纳入直接比较。
Google Scholar 的 `genus one wild torsor logarithmic good reduction` 入口返回 HTTP 403；Semantic Scholar 同词 API 返回 HTTP 429，均停止该入口，不规避限制、不声称其数据库完整搜索通过。
公开 arXiv 正文可用，故这两项访问缺口没有阻断本地研究；仍不宣称全网无先例。
D7 HTML 两次 Internal Error 后改读官方 PDF 文本成功；PDF 第4页截图仍 Internal Error，本件不依赖其图示，也不声称完成视觉阅读。

## 3. 七项核心一手来源及准确阅读层级

以下为逐件有界阅读；“摘要＋引言”不等于全文证明审计。D2 两个版本是同一论文，只计一项。

| ID／论文 | 日期与版本／发表状态 | 本人实际读取 | 与本轮的关系及不能外推之处 |
|---|---|---|---|
| D1，N. Joshi、P. Roffelsen，*Arithmetic dynamics of a discrete Painlevé equation* | [arXiv:2508.18578v2](https://arxiv.org/html/2508.18578v2)，2026-01-16版 | 摘要及引言主文，HTML 45–140；未读全篇／图表 | 核对原离散映射、根单位和 Hasse／genus 问题；这是既有原族，不是本轮新创新 |
| D2，K. Mitsui、A. Smeets，*Logarithmic good reduction and the index* | [最新修正版 v3](https://arxiv.org/html/1711.11547v3)，2023-06-15；先前 v2 为2017-12-01 | v2摘要／§1、§2陈述、§5；发现 corrected v3 后补读 v3摘要／§1完整、§2开头及命题、§4定义与判据、§5完整、§6文字；§6若干序列 HTML 空白，未声称完整证明核验 | 代数闭剩余域的 genus-one 对数好约化有既有完整判据；不能忽略剩余域和正则模型假设移植到原有限域设置 |
| D3，L. Zimmermann，*The torsion in the cohomology of wild elliptic fibers* | [v2](https://arxiv.org/html/1909.10891v2)，2020-08-22；[JPAA 225 (2021), 106522](https://doi.org/10.1016/j.jpaa.2020.106522) | 摘要＋引言完整（35–86），§1开头87–95；非全篇 | 在规定模型／规范化条件下，用群上同调表达椭圆族 $R^1f_*\mathcal O$ 的扭；不是原曲面每个 $H^1(S,L_n)$ 的现成识别 |
| D4，S. Mehidi、T. Poiret，*Moduli of finite flat torsors over nodal curves* | [v4](https://arxiv.org/html/2407.10924v4)，2025-06-26；JLMS 112 (2025), e70220，[DOI](https://doi.org/10.1112/jlms.70220) | 摘要及引言主陈述1.1–1.7，HTML 50–52、67–136；未读全部后文 | 有限平坦交换群作用在节点曲线上的 torsor 与 log Jacobian 对应；这与原 genus-one 曲线在域上作为其 Jacobian 的 torsor 是不同分类问题 |
| D5，S. Mehidi，*Extending torsors under quasi-finite flat group schemes* | [v3](https://arxiv.org/html/2211.16067v3)，2024-08-24；[Nagoya Math. J. 257 (2025), 45–54](https://doi.org/10.1017/nmj.2024.19)，2024在线 DOI不作2025新版本 | 摘要＋引言完整；Part II 228–256，包括Th4.1/4.2/4.4及所展示证明；上游Th2.5未全读 | 点化有限群 torsor 的延拓；不能先给原无点 genus-one 曲线添加 $K$ 点，再用此定理证明它有点 |
| D6，S. Mehidi，*Log purity, torsors on root stacks and log Nori fundamental group* | [v2](https://arxiv.org/html/2603.23697v2)，2026-06-05；首版2026-03-24，预印本 | 摘要＋引言51–125（Th1.1–1.4），另§2／§3部分展示，不作全文证明审查 | 线性约化（linearly reductive）有限平坦群的 log purity；一般有限平坦 torsor 的 root-stack 描述不是“所有野群都唯一延拓” |
| D7，L. Herr、S. Mehidi、M. Pieropan、T. Poiret，*Log geometry and lifting rational points* | [v2 PDF](https://arxiv.org/pdf/2509.12167v2)，arXiv修订2026-08-05、稿面2026-08-06；首版2025-09-15，预印本 | PDF文本摘要＋全部§1（第1–7页，0–298行），未依赖第4页图 | firm locus 给 log lifting 条件；Th1.3允许有限次域扩张，Th1.12只在指定模型上给 étale-local lifting，不能当作原域有点的充要式 |

D4 的正式发表身份另由[作者研究页](https://smehidi.perso.math.cnrs.fr/research.html)及所链接出版信息交叉核对；其他未给正式发表信息的项目保留为预印本。
D3/D4 页面出现的2026年 HTML render date 不是其版本日期。D2 最新 v3 明示 corrected；旧 v2 实读不抹去，但本轮比较以新 v3 的相应陈述为准。
本件未做 v2/v3 全文差异证明，不能声称全部修正影响已经穷尽；若未来证明实际消费 §2／§4／§6，必须取得并核对公式完整的对应版本。

## 4. 标准机制与原对象之间究竟差什么

### 4.1 对数好约化不是新的通用判据

D2 在代数闭剩余域、规定的最小正则模型上，把 genus-one 对数好约化归结为 tame $H^1$，并在 period 被 $p$ 整除时要求 Jacobian 好约化及上同调平坦；§4／§5用法丛阶 $\mu$ 与重数 $m$ 比较。超奇异层不能满足其非平凡 $p$-torsion 法丛条件。[D2修正版](https://arxiv.org/html/1711.11547v3)
因此“把通常 good reduction 改叫 log good reduction”、泛称法丛／log-unit 障碍，不是可直接重新计功的概念中心。
真正未由本地证据供应的是：原完整能量提升的正则模型、实际 period／法丛或等价零类判别，以及有限剩余域下降。这里未构造它们，也未断言必须沿某一种 bridge 才能解题。

### 4.2 同名上同调不能拼接

D3 的对象由椭圆族及其特定 Galois 规范化决定；原非单位时间链则按反典范次数给出曲面线丛上同调。[D3](https://arxiv.org/html/1909.10891v2)
若尝试把已得 C1–C3 转成野约化信息，必须先给同一底环、实际态射及自然性的比较；相同“torsion”“厚度”名称或相同长度不构成这样的比较。
同理，[基线盘点][BASE] §5 已区分原几何 $\kappa_J$、$\mathrm{Fr}_*\kappa_J$ 与域上 $H^1(K,E_c)$；后者在能量变化时目标 Jacobian 也可能变化。

### 4.3 新的 torsor 延拓论文不自动解决原曲线分裂

D4–D6 的自然对象是在给定曲线上、有限群方案之下的覆盖与延拓；群交换性、Cartier dual 的条件、点化、log regularity 和线性约化必须逐项保留。[D4](https://arxiv.org/html/2407.10924v4)、[D5](https://arxiv.org/html/2211.16067v3)、[D6](https://arxiv.org/html/2603.23697v2)
这些可能供应未来实际构造的工具，但既不识别本族 $[X_c]$，也不给其野过滤深度。尤其不能把已知 $\ell\ne p$ Kummer 满像换成混合特征 $p$-primary 类。
D7 强调的是允许扩张／étale-local 的 lift；这比固定原域有点弱，正好说明未来消费者必须锁定允许的扩张类型。[D7](https://arxiv.org/pdf/2509.12167v2)

### 4.4 可以带给新问题生成的三个接口，不是三个已准入题目

1. 原能量提升到 **整体** 有点／无点或 period 的实际可计算识别；已有末端根只给充分条件，不能冒充必要条件。
2. 尖点／普通／超奇异过渡中，原两参数退化与正则化之后的结构如何相接；不能预设有 embedded component 或有限 jet 必定丢信息。
3. 仅在实际态射可构造时，考察原截面／迹／相邻扩张是否控制某个新的几何消费者；若只重述非单位 C1–C3，则仍受原不准入处置约束。

以上是主控从来源与本地缺口作的研究推断，不是外文作者已提出同一 qPI 问题，也不是已有新意分或长文容量结论。
没有以跨族一般化充当当前 P31；真正跨系统族的方向只能列 `ROUND2_CLUE`。

## 5. 最近六个月的相邻前沿补查（只读摘要）

| ID | 一手入口／版本 | 摘要层结果与处理 |
|---|---|---|
| E1 | Sato–Takemura–Yamashita，[Reducibility of symmetry on q-Painlevé equations](https://arxiv.org/abs/2609.02927)，v1，页面提交2026-08-26 | Weyl表示等价／可约性与平移表达；元数据月份和编号月份不同，保留官方显示，不自行修正；未读正文，不作包含排除 |
| E2 | Desiraju–Roffelsen，[A Tau function for q-Painlevé VI as a Fredholm determinant](https://arxiv.org/abs/2608.03345)，v1，2026-08-04 | qPVI 的解析 tau／RH 可解性；不是本族积分反典范导出代数，跨系统应用仅线索 |
| E3 | Kim–Wang，[Bootstrapping bilinear relations of discrete Painlevé systems from 5d gauge theories](https://arxiv.org/abs/2608.15756)，v1，2026-08-16 | 5d 配分函数给双线性关系的方法；没有从摘要推断已覆盖或未覆盖本 qPI 算术对象 |

E1–E3 不计入“已读引言”的七项核心数量；不把搜索返回的旧文抓取日期作为2026新作。未读取它们全文，未来如果新想法实际消费其对象须继续定向核查。

## 6. 本件交付边界

本地直接引用及七项公开核心来源均有上面的准确入口与阅读范围；未复制外文长段原句，未把摘要阅读升级为证明审查。
无新数学状态、没有 I09 固定对运行、没有排他性全球开放断言、没有正式新意／独立价值／证明／容量四门票。
本件和独立乘法地形用于下一轮8–12项具体问题生成；不重写旧十项报告，不为固定失败包再抽票。
Papers27–30与所有旧锁／失败保留；Paper31仍无项目、稿件或PDF，Batch07仍4/5。

[CLOSED]: PAPER31_QPI_NONUNIT_CLOSED_FORMAL_CANDIDATE_DISPOSITION_V1_20260910.md
[BASE]: PAPER31_QPI_POST_CLOSED_BASELINE_GAPS_V1_20260910.md
