# Paper31：首非零 Fitting 与双对偶缺陷的一手来源补查 V1

日期：2026-09-10 UTC；沿用指定的 `20260909` 输出文件名。
执行席：`/root/p31_qpi_novelty_cd_i08_v1`。本席曾检查 D05、$M_4$、C／D 工具与 A 合并稿，未参与这些作者推导；本轮不是盲审。
仅新增本件来源补充，不改作者、旧报告、索引或任何数学接受记录。
`SOURCE_SUPPLEMENT_COMPLETE / FULL_TEXT_NOT_OBTAINED / IMPORTANT_PRECEDENT_NOT_CLEARED / NO_NOVELTY_VOTE`。

## 1. 结论与实际覆盖

完成两篇指定论文的有界公开来源查找，新增查询恰为6个。未取得匹配的作者／机构公开全文或可核对证明的 PDF。
两篇的官方元数据可核对；Hadjirezaei 2026 的官方索引预览还包含摘要、引言及部分定理／节选，Ohm 2008 只取得官方摘要层内容。
**不能据此排除任何一篇对本项目通用 Fitting／双对偶机制的重要包含；缺少全文不是新颖性证据。**
本项目 [D 主引理][D] 已按标准机制扣除，这一处置保持，不因未找到同形公式而恢复新意。
[A 合并稿][A] 的原 $q=1$ 实际格绑定及具体整数理想公式与通用机制分开记录；本件不对其差额评分或给完整门票。

## 2. 两篇来源身份与可读范围

| 来源 | 官方书目信息 | 本席实际可读范围 | 尚未读取 |
|---|---|---|---|
| S. Hadjirezaei, *First nonzero Fitting ideals, reflexive defect, and local cohomology* | Journal of Pure and Applied Algebra **230**(8), 2026, 108300；DOI `10.1016/j.jpaa.2026.108300` | 官方搜索索引的摘要、引言、Theorem 1.3 声明及部分节选 | 正文完整定理链、证明、全部假设与例子；没有 PDF |
| Jack Ohm, *On the first nonzero Fitting ideal of a module* | Journal of Algebra **320**(1), 2008, 417–425；DOI `10.1016/j.jalgebra.2008.03.012` | 官方搜索索引的元数据与摘要，部分数学公式提取缺失 | 两条全球推广的完整声明、编号、证明及使用范围；没有 PDF |

两项元数据分别来自[Hadjirezaei 官方页](https://www.sciencedirect.com/science/article/pii/S0022404926001313)与[Ohm 官方页](https://www.sciencedirect.com/science/article/pii/S0021869308001452)。
主控先前报告普通直开403；本席三次普通打开对应两页及2026公开摘要页，工具均返回 `Internal Error`，没有返回可读正文。
本席不能把该工具错误改记成自己观测到的 HTTP 403，也不能把搜索可见预览记成全文成功打开。
Ohm 页的公开索引带有开放归档标签，但这不等于本席已取得全文；2026页显示机构访问／购买入口，本席未付费或尝试进入。

## 3. 可以准确记录的最强已见内容

### 3.1 Hadjirezaei 2026：预览中的实际定理，不外补缺失公式

官方预览用自然双对偶映射的余核描述无正则扭子商的缺陷，并研究其与首非零 Fitting 理想的支撑关系。
在正规整环情形，这一缺陷概念与本项目 $E=L^{**}/L$ 对应；它不是本项目新增的概念。[官方预览](https://www.sciencedirect.com/science/article/abs/pii/S0022404926001313)

该公开索引中 Theorem 1.3 的可读声明是：$R$ 为 Noetherian UFD，$M$ 有限生成，$Q$ 为其首非零 Fitting 理想；**另假设 $Q$ 为准素且高度为1**。
于是 $Q=(\pi^e)$，其中 $\pi$ 不可约、$e\ge1$；$N=M/T(M)$ 在高度一处局部自由，且相应双对偶缺陷的支撑只落在包含 $(\pi)$ 的高度至少二的素点。
这是预览声明的中文转述，未读取其证明。[Theorem 1.3 所在官方预览](https://www.sciencedirect.com/science/article/abs/pii/S0022404926001313)

其他预览公式存在空缺，不能据上下文自行补出 Theorem 1.1／1.2 的完整表达式、精确局部上同调同构或全部适用条件。
尤其不能把引言中略写的“高度一分支”转述为任意高度一首 Fitting 理想必主；上面确见的准素条件不可删除。

### 3.2 Ohm 2008：摘要层的经典机制压力

官方摘要明确讨论 Lipman 的局部正则主理想判据，并说明本文给出两种全局推广，分别以首 Fitting 理想正则主生成或可逆为出发条件。
这足以将首 Fitting、关系模与去扭商结构的通用联系列为直接先例压力；尚不足以重建两条全球定理或断言其是否包含 D 的完整因子式。
本席不以二手摘录补齐官方提取中丢失的数学符号，也不捏造定理编号。[Ohm 官方摘要](https://www.sciencedirect.com/science/article/pii/S0021869308001452)

## 4. 与 D 主式、原完整 Fitting 和原格缺陷的包含表

下表“未建立包含”只指当前可读证据不足，绝不等于“已排除先例”。

| 本项目待比较内容 | 已见直接重合／压力 | 当前可作的判断 |
|---|---|---|
| D：$\operatorname{Fitt}_n(M)=\tau^B\operatorname{detideal}(M/T)$，含自然双对偶归一化 | 2026来源直接讨论首 Fitting 与双对偶缺陷；2008来源直接讨论首 Fitting 与去扭商结构 | 通用机制继续扣除；两篇是否已有等价完整因子定理，全文缺失，未排除 |
| A1：原留数给 $L_n\simeq\bigoplus_a I_{n,a}$，$E_n\simeq\bigoplus_a R/I_{n,a}$ | 缺陷定义及一般支撑理论已有直接先例 | 具体原 $J_n$／标架／留数像和整数理想的绑定是另一个比较对象；当前未建立其被包含，也未凭预览排除 |
| A2：整个 $\mathbb Z[\tau]$ 上 $\tau^{B_n}\prod_a I_{n,a}$ 的准确原 Fitting | 已见2026 Theorem 1.3控制一个准素高度一分支 | 下段说明其不能直接代入本项目首次非主理想；不因此排除该文其他定理或2008全文的包含 |
| A3–A4：具体 $D_n(p)$、首现及数字递推 | 可读范围没有提供与该原对象逐项匹配的公式证据 | 仍是待全文匹配的具体差额，不给“未见所以新”的结论 |

### 4.1 已见 Theorem 1.3 的一个确切适用性边界

以下是本席基于本项目已证明公式作的代数推论，不声称出自外文全文。
在原首次次数处，写 $A_p=\mathbb Z[\tau]_{(p,\tau)}$、$s=p-1\ge1$、$B=B_{p+1}>0$，则
$$Q=\tau^B(p,\tau)^s,\qquad \sqrt Q=(\tau).$$
有 $p^s\tau^B\in Q$，但 $\tau^B\notin Q$，因为 $(p,\tau)^s$ 是真理想；另一方面 $p\notin\sqrt Q$。
所以 $Q$ 不是 $(\tau)$-准素理想。这给已见 Theorem 1.3 的明确前提不匹配，不能直接用其 $Q=(\pi^e)$ 结论取代本项目的非主理想计算。
这一观察只限制**该条已见定理**的直接应用。它不排除整篇论文中更一般的支撑、行列式或缺陷结论，也不为 D 或 A 自动生成新意。

## 5. 有界查询与公开访问记录

已 FULL 读取 research-lit 技能，并按其来源分层执行；本任务采用用户的两篇目标、最多6查询和不外发边界。
本地只按文件名筛选 `papers/`、`literature/` 中含 Fitting／Hadjirezaei／Ohm 的 PDF／文本，未命中；没有全文扫描全部本地库。
指定可用目录未找到 arXiv 抓取脚本，因此按技能回退到 arXiv 站点搜索，不下载 PDF。

| 新查询序号 | 实际查询 | 结果界限 |
|---:|---|---|
| 1 | `"First nonzero Fitting ideals, reflexive defect, and local cohomology"` | 命中官方预览及聚合记录，未取得作者／机构全文 |
| 2 | `"On the first nonzero Fitting ideal of a module" Ohm` | 命中官方摘要及相关索引，未取得匹配全文 |
| 3 | `"Hadjirezaei" "reflexive defect" pdf` | 官方索引扩展到引言、节选；未取得匹配 PDF |
| 4 | `"Jack Ohm" "Fitting" pdf` | 官方摘要、聚合记录及噪声结果；没有匹配公开稿 |
| 5 | `site:arxiv.org ("Hadjirezaei" OR "Jack Ohm") "Fitting"` | 未返回匹配的 arXiv 稿件，不据此断言不存在 |
| 6 | `"Fitting" ("Hadjirezaei" OR "Ohm")`，域限定 `vru.ac.ir`、`lsu.edu`、`hal.science` | 未命中匹配论文；这些是检索入口，不作为作者任职的独立证据 |

另有三次普通官方页面打开，均未返回正文；没有尝试绕过访问限制，没有付费、联系作者、使用凭据或进入机构认证。
ResearchGate、其他聚合条目及检索中顺带出现的论文只作发现线索；本报告的书目／定理转述只依据指定两篇的官方索引内容。
没有补做第7个查询，没有扩大成全部 Fitting 文献综述。到达约定上限后结束本次补查，保留全文访问缺口。

## 6. 冻结对象与后续可用结论

本席已在紧邻数学任务全文读取并检查下列对象；本次不修改或重新评分它们：

| 本地比较对象 | SHA-256 |
|---|---|
| [D 主引理][D]，297行 | `913e701986e540a59476a9f64bf890bf3bbdc300596ef9db9514ebe784dcb250` |
| [A 合并定理][A]，180行 | `f214e2e14d065e778d752f15855995d0a66df4c115d7aa72e14af5695e153260` |

外部两篇没有取得全文文件，所以没有可提供的 PDF 哈希、全文页码覆盖或“全文已读”标签。
本次来源补充已终态，但重要先例的全文包含排除仍未完成；两种状态必须分开。
任何后续独立评价都应同时保留已见强机制压力和未读全文限制，不能把本报告转写为新意通过或已排除既有文献包含原对象。
本报告终态本人全文自读，并核对两条直接本地引用及其输入身份；最终行数、SHA 随交付给出。

[D]: PAPER31_QPI_NONUNIT_DETERMINANT_IDEAL_LEMMA_V1_20260909.md
[A]: PAPER31_QPI_NONUNIT_ALL_DEGREE_ARITHMETIC_THEOREM_V1_20260909.md
