# Paper30 qPI：整系数问题的 novelty Phase B 来源比较 V1

日期：2026-09-09。执行者：`/root/p30_qpi_integral_cohomology_prior_art_v1`。
范围：冻结 Phase A 的 C1–C3；逐项多来源检索与 primary-source 对照。
状态：本件交付 Phase B 的实际检索、包含映射和明确访问缺口；不是 Phase C/D、新意票、证明接受或准入。
route_applicability: NOT_APPLICABLE。

## 1. 结论先行

三个主张都已有必须扣除的一般机制。本轮没有取得一个外部定理直接包含原 qPI 的 C1–C3 全部量词，
但这不构成全球新颖性保证，也不表示三个主张可以作为三个独立发现计数。

本轮对既有三份有界报告的实质增量，是确认了 C1 的一个更准确的**模型层先例**：
Wagner 的 q-Hodge 微分明确为 $T^j\mapsto(q^j-1)T^{j-1}dT$。
因此 C1 的对角块形状已有标准一元模型；真正待评价的是原八截面曲面上同调到该模型的整系数几何桥接，
特别是整个 $q^j=1$ 闭子概形上的边界单位截面与曲面级扩张消失。
这不是说 Wagner 已经证明了原 qPI 分裂，详见 §5.1。

C2 仍须扣除 JR 的原圆分整数积分、域上 Halphen 判据、矩阵迹 Frobenius 和一般平坦／延拓工具。
未被本轮精确来源直接点名包含的是：同一原完整模型上的降阶 pencil、全部纤维概形重数、
原 pencil 的非完整特化及相应扭子模。其完整初等因子从 C1 特化，不另计第二个一般上同调发现。

C3 的 Hasse 迭代乘子被 Vlasenko Theorem 1(i) **直接包含**，不是仅有相似性。
本轮又补读 Smirnov 正文引言，确认根单位 $p^s$ 阶的 Frobenius intertwiner 特化及 Dwork/Hasse–Witt 联系已有研究。
Koroteev–Smirnov 2026 的首非零 ramified 项先例也保留。
准确剩余只能是原能级、原排序下的先除后约化微分桥接、完整开放空间延拓与统一系数阶，
不是一般 Frobenius／Cartier／圆分 jet 方法的新发现。

数据库覆盖存在真实缺口：每项都实际尝试 arXiv、Google Scholar、Semantic Scholar 入口；
后两者均被当前访问层拒绝，未绕过、未假称完整数据库查询。
使用公开网页检索、可访问 arXiv 原文及已配置 Consensus 补充，不把这些替代入口改名为 Scholar/S2 API。

## 2. 绑定范围、执行方式和运行中断

全文读取 [Phase A](PAPER30_QPI_INTEGRAL_SCOPE_PHASE_A_V1_20260909.md) 的 107 行，
以及 [D](PAPER30_QPI_CYCLOTOMIC_DIFFERENTIAL_DIAGNOSTIC_V1_20260909.md) 268 行、
[G](PAPER30_QPI_CYCLOTOMIC_GLOBAL_MODEL_DIAGNOSTIC_V1_20260909.md) 254 行、
[U](PAPER30_QPI_UNIVERSAL_COHOMOLOGY_DIAGNOSTIC_V1_20260909.md) 255 行。
全文消费三份来源报告：
[圆分退化先例](PAPER30_QPI_CYCLOTOMIC_DEGENERATION_PRIOR_ART_V1_20260909.md)、
[整除微分来源差分](PAPER30_QPI_DIVIDED_DIFFERENTIAL_SOURCE_DELTA_V1_20260909.md)、
[整系数上同调先例](PAPER30_QPI_INTEGRAL_COHOMOLOGY_PRIOR_ART_V1_20260909.md)。
没有重读旧 47 件输入，也没有把作者 S 的证明检查冒充本件任务。

采用 novelty-check 的 Phase B；research-lit 的来源等级与访问披露沿用已读规则。
本代理不写 Phase C/D、不计算新意／价值／信心分数，不调用正式 Route A/B，
不以查询数或论文数替代新意判断。ICLR、NeurIPS、ICML 对本纯代数几何问题为 `NOT_APPLICABLE`，
没有执行无关会议扫描。没有发送通知、上传文本、发信、付费访问或创建论文项目。

较早一次 Phase B 运行因 usage limit 终止；主控转达用户“继续，额度重置了”后恢复同一任务。
恢复从实际保留结果接续，没有将终止期间记作持续运行或已完成检索，也没有改写此前完成的有界报告。
以下日志只记录实际执行的查询和原文访问；三次已保留 Consensus 查询未重复提交。

固定 $R=\mathbb Z[q^{\pm1},\tau^{\pm1}]$，曲面与八环边界沿用 Phase A，$L_n=\mathcal O(nD)$。
固定 $r=mp^a$、$p\nmid m$、$N=p^a$，圆分 DVR 为 $\mathcal O$，剩余小阶积分为 $J$。
微分仅作用于状态 $x,y$；全开放空间包括四条末端例外线。
非本原的 $q^j=1$ 整数基上使用 $C_j=[z^j]\operatorname{tr}M_j(z)$，不把它改名为唯一积分 $I_j$。

## 3. 可复核检索日志

### 3.1 每项准确关键词查询

实际提交十九条 web 检索式，以下保留原串。`site:arxiv.org` 是网页引擎域限定，不是 arXiv 数据库 API。
`after/before` 是网页检索的日期提示，不保证索引对出版日期精确过滤；实际版本日期在 §4 另核。

| ID | 主张 | 准确 query | 本轮结果／处置 |
|---|---|---|---|
| W01 | C1 | `site:arxiv.org Looijenga Halphen anticanonical cohomology integral base change 2024 2025 2026` | Friedman、Stable maps 等入口及噪声；不据综合命中数判新 |
| W02 | C1 | `"anticanonical" "cohomology" "torsion" "universal" family` | 不同维数／不同上同调的结果为主；没有取得精确分裂定理 |
| W03 | C1 | `"Looijenga" "integral" "cohomology" after:2026-03-09 before:2026-09-10` | 姓名匹配、拓扑整系数结果等噪声；不当作本反典范族先例 |
| W04 | C1 | `"Halphen" "cohomology" "base change" "splitting"` | 未定位可核的整系数逐级分裂陈述 |
| W05 | C2 | `site:arxiv.org q Painleve root unity cyclotomic reduction genus one pencil 2024 2025 2026` | 新近 quadrics-pencil 论文与不同算术对象入口 |
| W06 | C2 | `"q-Painlevé" "root of unity" "reduction"` | JR 原对象；另有 qPII/其他 folding 系统，未混同 |
| W07 | C2 | `"Halphen" "mixed characteristic" "pencil"` | 未取得准确原模型的混合特征定理 |
| W08 | C2 | `"Painleve" "root of unity" after:2026-03-09 before:2026-09-10` | JR 2026 出版入口；抓取日期不充当出版日期 |
| W09 | C3 | `site:arxiv.org cyclotomic divided differential Hasse Witt q difference 2024 2025 2026` | q-Witt、Vlasenko、q-difference 相关入口 |
| W10 | C3 | `"q-difference" "ramified" "2026"` | 与旧 KS 圆分先例合并比较，未制造新命中 |
| W11 | C3 | `"Hasse" "Vlasenko" "higher" matrices differential cyclotomic` | Higher Hasse–Witt、2018 Hasse–Witt/period 与 2024 讲义线索 |
| W12 | C3 | `"q-difference" "Frobenius" after:2026-03-09 before:2026-09-10` | Vargas-Montoya 及历史文献被索引返回；逐项核年 |
| W13 | C3 | `"The cyclosyntomic regulator of a number field"` | Bouis–Gazda 原站与 arXiv；首发实际为 2026-02-25 |
| W14 | C3 | `"Cohomology and congruences" Vlasenko` | arXiv:2412.13313；2024 讲义，不误算新原创定理 |
| W15 | C1/C3 | `"q-Witt vectors" "q-Hodge complexes"` | Wagner 2024 首发、2025 v5；发现 C1 模型层精确近邻 |
| W16 | C1 | `"Looijenga" "cohomology" 2026` | Looijenga 姓名匹配的 cyclic cover／Shimura 等不同对象；未据题名排尽 |
| W17 | C1 | `"q-Hodge" "anticanonical"` | 未定位 qPI 曲面桥接定理；无结果本身不证明无先例 |
| W18 | C1 | `"Halphen" "nonreduced" cohomology` | Hilbert scheme 等非目标结果；没有取得可用精确包含 |
| W19 | C1/C3 | `"q-Hodge complexes over the Habiro ring"` | Wagner 后续 2025 v2；核一般 Habiro descent 的前提 |

### 3.2 三个数据库入口的实际状态

三项初始查询分别为：

- E1：`Looijenga Halphen anticanonical cohomology integral`
- E2：`q Painleve root unity cyclotomic reduction pencil`
- E3：`q difference cyclotomic divided differential Hasse Witt`

| 主张 | arXiv 搜索网页 | Google Scholar，年份参数 2024–2026 | Semantic Scholar 搜索网页 |
|---|---|---|---|
| C1 | [E1](https://arxiv.org/search/?query=Looijenga%20Halphen%20anticanonical%20cohomology%20integral&searchtype=all&abstracts=show&order=-announced_date_first&size=50)：TimeoutError | [E1](https://scholar.google.com/scholar?q=Looijenga%20Halphen%20anticanonical%20cohomology%20integral&as_ylo=2024&as_yhi=2026)：non-retryable safe-open 拒绝 | [E1](https://www.semanticscholar.org/search?q=Looijenga%20Halphen%20anticanonical%20cohomology%20integral&sort=relevance)：同类拒绝 |
| C2 | [E2](https://arxiv.org/search/?query=q%20Painleve%20root%20unity%20cyclotomic%20reduction%20pencil&searchtype=all&abstracts=show&order=-announced_date_first&size=50)：页面明确返回 no results | [E2](https://scholar.google.com/scholar?q=q%20Painleve%20root%20unity%20cyclotomic%20reduction%20pencil&as_ylo=2024&as_yhi=2026)：同类拒绝 | [E2](https://www.semanticscholar.org/search?q=q%20Painleve%20root%20unity%20cyclotomic%20reduction%20pencil&sort=relevance)：同类拒绝 |
| C3 | [E3](https://arxiv.org/search/?query=q%20difference%20cyclotomic%20divided%20differential%20Hasse%20Witt&searchtype=all&abstracts=show&order=-announced_date_first&size=50)：页面明确返回 no results | [E3](https://scholar.google.com/scholar?q=q%20difference%20cyclotomic%20divided%20differential%20Hasse%20Witt&as_ylo=2024&as_yhi=2026)：同类拒绝 | [E3](https://www.semanticscholar.org/search?q=q%20difference%20cyclotomic%20divided%20differential%20Hasse%20Witt&sort=relevance)：同类拒绝 |

长合取查询的零项没有被视为无先例证据。随后 arXiv 搜索网页分别补试短式 `Looijenga`、
`Painleve AND unity`、`Hasse-Witt`（同样 all fields、最新 announced 排序、50 条），
三者均 internal error，故不声称看过其完整结果页。arXiv 的准确论文摘要和 HTML 仍可访问，已用于 §4。
没有改出口、获取额外凭据、绕过非重试拒绝或重试受限 Scholar/S2 服务。

### 3.3 配置数据库 Consensus 补充

每项一次 search，每次实际返回十项记录；只作为发现入口，结果有明显主题噪声。

| 主张 | 准确 query |
|---|---|
| C1 | `Looijenga Halphen anticanonical cohomology integral torsion base change year:2024-2026` |
| C2 | `q-Painleve root of unity cyclotomic reduction genus one pencil year:2024-2026` |
| C3 | `q-difference cyclotomic divided differential Hasse Witt Frobenius year:2024-2026` |

在引用选中记录前，实际执行 fetch：
[Schuler](https://consensus.app/papers/the-logopen-correspondence-for-twocomponent-looijenga-schuler/60b39657bff352ce8330d50e8a122554/?utm_source=chatgpt)、
[Koroteev–Smirnov](https://consensus.app/papers/quantum-ktheory-of-quiver-varieties-at-roots-of-unity-koroteev-smirnov/3239f3458ed550259925c9f07c97b6a0/?utm_source=chatgpt)、
[Smirnov](https://consensus.app/papers/frobenius-intertwiners-for-qdifference-equations-smirnov/60c4b09b23015591a7a7b16616e5b660/?utm_source=chatgpt)、
[Bouis–Gazda](https://consensus.app/papers/the-cyclosyntomic-regulator-of-a-number-field-bouis-gazda/bc1d4e9dd3155c1e877ee5c5ae929510/?utm_source=chatgpt)。
数学判断使用下面的一手原文，不依赖该服务的排序、引用数或年份字段。
例如 Consensus 把 Schuler 与 KS 标为 2024，并不推翻各自 2025／2026 的正式出版年。

### 3.4 时间覆盖的实际含义

检索明确覆盖 2024–2026，并以 2026-03-09 至 2026-09-09 为近六个月窗口。
窗口内确证的相关原文更新有 FHHO v2（2026-04-28）与 KS v4（2026-06-02）；
KS 的 2026-07-10 IMRN 出版记录沿用旧件已核元数据，本轮出版入口重开失败，不伪称重新读到出版正文。
JR 2026 已发表原输入亦保留，但本轮依据作者 v2 和公开出版索引，不把新抓取日期当正式发布日期。
Bouis–Gazda 首发 2026-02-25，**在近六个月窗外**，只计 2024–2026 扩展覆盖。
Wagner 两件最新版本都是 2025，不因作者 PDF 被近期抓取而误标为 2026。
这是一轮有界近期筛查，不声称完整覆盖该窗口内所有 arXiv 稿件或未公开工作。

## 4. Primary 来源、版本与真实 read range

“复用”与“本轮新读”严格区分。复用本代理此前亲读的 C1 来源时不重新跑搜索；
另两份来源报告由其他代理完成，其没有在本轮亲读的原文段只按**已有核查记录**使用，
不升级为本执行者的全文阅读。任何一行均不宣称通读整篇外部论文。

| ID | 来源与版本 | 实际读取／访问 | 对应边界 |
|---|---|---|---|
| P1 | Gross–Hacking–Keel, *Moduli of surfaces with an anti-canonical cycle*, Compositio Math. 151 (2015), 265–291，DOI 10.1112/S0010437X14007611；[作者 v5](https://paulhacking.github.io/mlp.pdf) | 复用本代理已亲读 §1 开头、Example 5.6 全段、Construction 5.7、Remarks 5.8–5.9、Lemma 5.10、Corollary 5.11、Theorem 6.1 与证明 | 全篇基域为复数；八个 $(-2)$ 圈的 Example 5.6 及通用周期族不可遗漏；未给 C1 的整数曲面分裂 |
| P2 | Friedman, *On the geometry of anticanonical pairs*, [arXiv:1502.02560v2](https://arxiv.org/pdf/1502.02560)，2016-07-22 | 复用已亲读引言、§1 Lemmas 1.6–1.7、§3 Definitions 3.7/3.9、Theorem 3.11 及证明，3.16–3.17 指定段 | 节点粘合与周期背景；3.11 的基是 reduced connected analytic space，不是任意整数基 |
| P3 | Stacks Project [07VJ](https://stacks.math.columbia.edu/tag/07VJ)、[0A1G](https://stacks.math.columbia.edu/tag/0A1G) | 复用已亲读 Lemma 30.22.1/Remark 30.22.2、Lemmas 36.30.1/36.30.4 与相邻证明 | proper flat/perfect 条件下任意派生基变换直接适用；不规定显式差分矩阵 |
| P4 | Wagner, *q-Witt vectors and q-Hodge complexes*, [arXiv:2410.23078v5](https://arxiv.org/html/2410.23078v5)，首发 2024-10-30，v5 2025-10-06 | 本轮新读元数据、摘要、引言 1.1–1.9 全段；包含准确微分、Theorems 1.5/1.7/1.9 陈述，未核正文证明 | C1 对角模型的精确形式近邻；q-Witt、Bockstein、非约化圆分商均非无人研究；不是反典范线丛推送定理 |
| P5 | Wagner, *q-Hodge complexes over the Habiro ring*, [arXiv:2510.04782v2](https://arxiv.org/html/2510.04782v2)，2025-10-08 | 初打开 v1 摘要与引言开头；随后按最新元数据读 v2 Definition 1.6、1.8–1.17，尤其 Theorems 1.11/1.15 陈述及 1.13 的原微分；未读 §3.2 证明 | 有指定 q-Hodge filtration 才有 Habiro descent；典范 smooth 构造需反转小素数。该理论不自动识别原相干上同调 |
| P6 | Joshi–Roffelsen, *Arithmetic dynamics of a discrete Painlevé equation*, [作者 v2](https://arxiv.org/html/2508.18578v2)，2026-01-16；已发表 DOI [10.1088/1751-8121/ae67bf](https://doi.org/10.1088/1751-8121/ae67bf) | 本轮读引言对象开头、§3.1 全段：Theorem 3.1、Remarks 3.2–3.5、原矩阵和证明。出版 DOI 本轮 robots 拒绝；不称已读出版全文 | 原圆分整数 $I_r$、原矩阵顺序、完整迹式和首项是已有输入；不是 C2 的相对完整 pencil 定理 |
| P7 | Vlasenko, *Higher Hasse–Witt matrices*, [arXiv:1605.06440v3](https://arxiv.org/html/1605.06440v3)，2018-04-17；Indag. Math. 29 (2018), 1411–1424，DOI 10.1016/j.indag.2018.07.004 | 本轮新核摘要、§1 定义 (1)–(4)、Theorem 1(i)–(iii)；旧差分另已核 Lemma 7，本轮不重称亲读 Lemma 7 证明 | C3 秩一 Hasse 乘积直接包含；(i) 不要求 ordinary，(ii)/(iii) 逆矩阵部分要求可逆 |
| P8 | Koroteev–Smirnov, *Quantum K-theory of quiver varieties at roots of unity*, [arXiv:2412.19383v4](https://arxiv.org/html/2412.19383v4)，2026-06-02；IMRN 2026(14), rnag153 | 本轮读摘要、§1.1、§5.2–5.3 指定归一化段、§5.5 完整公式及 §5.6 Theorem 5.4/证明；正式出版页本轮受限，旧件已核 2026-07-10 元数据 | 根单位首非零分歧项→p-curvature 已有；其 inverse product、equivariant 参数缩放与原 qPI 微分不相同 |
| P9 | Smirnov, *Frobenius intertwiners for q-difference equations*, [arXiv:2406.00206v2](https://arxiv.org/html/2406.00206v2)，2025-02-24 | 由旧件“仅摘要”增至本轮完整引言 §§1.1–1.6；另网页返回 Appendix A 的 Lemmas A.1–A.2/Proposition A.6 陈述，未读主证明 §5.7 | 明确假设 $|q-1|_p<1$、$h,a_i\in\mathbb Z_p$；特定 $T^*\mathbb P^{n-1}$ 系统与归一化，不是任意 qPI Lax 矩阵 |
| P10 | Bouis–Gazda, *The cyclosyntomic regulator of a number field*, [arXiv:2602.21894v1](https://arxiv.org/html/2602.21894v1)，2026-02-25 | 本轮新读元数据、摘要、引言至 Theorems A–C 陈述，未读后文证明 | $R=\mathcal O_K[\Delta_K^{-1}]$ 为 étale Z-algebra，单位的一阶 Chern／log 及 cyclotomic norms；不等于原 $dI_r$，也不保留全部坏素位 |
| P11 | Alonso–Suris–Wei, *Discrete Painlevé equations and pencils of quadrics in P3*, [arXiv:2403.11349v2](https://arxiv.org/html/2403.11349v2)，2025-06-06 | 本轮新读摘要和 §1 引言全段，未核七类构造的全部证明 | P3 中 quadrics pencil 的新表达，不能靠 pencil 同词直接判 C2 已含；不同系统归属仅留近邻 |
| P12 | Vlasenko, *Cohomology and congruences*（正文题名顺序相反），[arXiv:2412.13313v1](https://arxiv.org/html/2412.13313v1)，2024-12-17 | 本轮新读元数据、摘要／开头说明、目录与 §1 开头；未以目录标题声称已核后文 higher-condition 定理 | 2024 Dwork crystals 讲义线索；不是 C3 超奇异下一阶的现成无条件结论 |
| P13 | Franco–Hanson–Horn–Oliveira, *Fourier–Mukai transforms and normalisation of nodal curves*, [arXiv:2405.11860v2](https://arxiv.org/html/2405.11860v2)，2026-04-28 | 本轮重核 arXiv 日期／摘要；复用本代理旧读引言、Theorem A 完整陈述及 §2.1 开头 | 复数 integral nodal curve 的 compactified Jacobian；integral 是“整曲线”而非整数系数，非八分量边界／曲面推送 |
| P14 | Schuler, *The log-open correspondence for two-component Looijenga pairs*, Forum Math. Sigma 13 (2025), e102；[出版原文](https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/logopen-correspondence-for-twocomponent-looijenga-pairs/E895DF32C1450AFD55D0388F471B4B14) | 本轮 Consensus fetch；复用旧亲读摘要、§1.1 Assumption ★、Theorem 1.2、Corollary 1.3、Theorem 1.5 陈述 | 两分量／正性条件的 log/open GW、BPS 整性，不是八环相干上同调 |

P4/P9/P11 等 HTML 的网页分段读取不完整时，使用同一已可访问公开 URL 流式转为纯文本，
按指定引言范围回读；未保存本地 PDF、未绕过权限。第一次并行转文本因数学转换警告导致输出截断，
截断部分未算已读；随后静默转换重新读取必要引言。P5 一次错误段标题选择返回空文本，
未算已读，最终以 v2 的原网页定点段落核准上述范围。

以下旧扣除继续有效，但本轮不冒称新读原文：Di Vizio–Hardouin 的非约化 q-curvature，
Vargas-Montoya 的强 Frobenius 结构前提，Bai–Lee 的圆分完成／关联分级，
Achter–Howe v5 的 Cartier 半线性订正，Mellit–Vlasenko 的常数项机制，
Hesselholt–Madsen 的 Witt ghost 微分，以及 Pain 的 Dickson／Cayley–Hamilton 背景。
准确节号、版本和旧读范围仍以三份来源报告为准，不把不同前提拼成全 $mp^a$ 定理。

## 5. 每项 closest work、准确 delta 与层级候选

以下是提供给 Phase C 的来源映射候选，不是本件作出的最终新颖性分类。
“未直接包含”始终限制于表中实读陈述；不等于证明学科中没有该定理。

### 5.1 C1：几何分裂与既有 q-Hodge 模型必须分开

C1 的主张为
$$R\Gamma(S,L_n)\simeq R[0]\oplus\bigoplus_{j=1}^{n}[R\xrightarrow{1-q^j}R],$$
包括非约化基变换上的 $\operatorname{Ann}(1-q^j)$，而非只比较域上维数。

最近几何先例是 P1 的 Example 5.6 与 Construction 5.7：八个 $(-2)$ 圈及周期参数吹起族已有。
其复数条件不覆盖指定整数坏素位；边界周期也不单独给出曲面递增正合列的连接态射。
P2 的节点粘合、P3 的 perfectness／派生基变换均应扣除。

**新增模型层识别（本报告的比较推断）：**令 $B=\mathbb Z[q^{\pm1},\tau^{\pm1}]$，
取形式多项式变量 $T$，对 $n\geq1$ 定义有限自由复形（$K_0=B[0]$）
$$K_n=\left[B\langle1,T,\ldots,T^n\rangle
 \xrightarrow{\delta_q}B\langle dT,TdT,\ldots,T^{n-1}dT\rangle\right],$$
其中 $\delta_q(1)=0$、$\delta_q(T^j)=(q^j-1)T^{j-1}dT$。
按单项式配对立即得到 C1 右侧（各一项取负号）。这只是有限自由矩阵的比较，
而该微分正是 [P4 §1.6](https://arxiv.org/html/2410.23078v5#S1)／[P5 §1.13](https://arxiv.org/html/2510.04782v2#S1) 的既有 q-Hodge 形式。
P4 的实际同调比较在 $(q-1)$-完成及 framed smooth 情况；本处只对其明确多项式公式作有限截段，
不声称 P4 原文已经陈述未完成的原曲面同构。

因此，$K_n$ 的 kernel/cokernel、Fitting 乘积、圆分因子与坏素数对角块不是新一般机制。
尚未由 P1–P5 直接完成的是
$$R\Gamma(S,\mathcal O(nD))\ \longrightarrow\ K_n$$
所需的几何识别：原 $C_j$ 在整个 $R/(1-q^j)$ 上延拓、限制到边界为单位、
由此消除曲面推送中的扩张。P5 的 Habiro descent 也未提供这支箭头；
不能仅因 $S$ smooth 就将 $\mathcal O(nD)$ 的相干上同调改成其 q-de Rham cohomology。
P4 的 no-go 条件不反驳 U 的非典范固定选择，U 也不能据此宣称典范／过滤乘法兼容的新理论。

Phase C 可比较的层级：**原几何族上的整系数结构识别／分裂 finding 候选**，
不是 q-Hodge、Bockstein、任意基变换或一般 Smith 算法的 method novelty。
若存在相对 Halphen 通用整数分裂定理，准确映射后该剩余还会进一步缩减。

### 5.2 C2：完整平坦 pencil 与模结构的贡献计数

P6 Theorem 3.1 已给 $\mathbb Z[s]/\Phi_r(s)$ 上的原积分和原迹顺序；
Remark 3.2 已明确整系数、模素数可约化及首项不丢次数；Remark 3.5 还指向既有复数 Halphen pencil。
所以“根单位产生原积分”“圆分整数可约化”均不是新发现。
由重复块到 $\bar I_r=J^N$ 的矩阵 Frobenius 推导亦非新机制。

准确剩余应合并表述为：在同一完整光滑相对曲面上，原 $f_r$ 平坦且
$\bar f_r=\operatorname{Pow}_N\circ f_m$；有限几何纤维为 $N$ 倍小阶完整纤维，
无穷纤维是 $r\bar D$；原完整线性系的基变换像只有 $\kappa\langle1,J^N\rangle$，
在 $\kappa\langle1,J,\ldots,J^N\rangle$ 中余维 $N-1$。
这些不是仅在环面 Laurent 公式上出现的“次数下降”，必须保留末端例外线与概形重数。

此外，C1 的圆分特化给
$$H^1(\mathcal S,\mathcal L_r)\simeq\mathcal O\oplus
 \bigoplus_{j=1}^{r-1}\mathcal O/(1-s^j).$$
在通常圆分 uniformizer 归一化下，其扭子初等因子是
$$\bigoplus_{b=0}^{a-1}
 (\mathcal O/(\pi^{p^b}))^{\oplus(p-1)p^{a-b-1}}.$$
这强于总长度，但取得分裂以后只是同一结果的标准赋值展开，不另计独立方法。

P8/P9 的根单位 q-difference 理论不直接替代以上相对曲面陈述；
P11 的 quadrics pencil 则是不同几何表达，不能将其对其他 surface type 的公式当 qPI 身份。
Phase C 可比较的层级：**同一原 pencil 的完整整数特化结构 finding／application 候选**；
模分裂属于 C1 的消费者。没有从来源差额推出稳定／半稳定模型、野导子或所有能级提升结论。

### 5.3 C3：直接被含的 Hasse 乘子与未自动得到的原微分

固定原谱多项式
$$F(Z,\lambda)=\lambda^2-(T+hZ+Z^2)\lambda+\varepsilon Z^3.$$
其唯一内部整点为 $(1,1)$，因此 P7 的 higher Hasse–Witt 矩阵为秩一系数
$G_a=[Z^{N-1}\lambda^{N-1}]F^{N-1}$。
按照旧来源差分的透明识别，$G_a\bmod p$ 就是 D 的 $U_{N-1}$ 系数；
取 $\sigma(T)=T^p,\sigma(h)=h^p$ 后，Theorem 1(i) 直接给
$\bar G_a=H_p^{1+p+\cdots+p^{a-1}}$。
这里不要求 $H_p$ 可逆或曲线光滑；可逆限制属于 P7 的 (ii)/(iii)，不能移给 (i)。[准确原定理](https://arxiv.org/html/1605.06440v3#S1)

原 qPI 的待比差额是 $\overline{p^{-a}dI_r}=\bar G_a(t^m,J)dJ$ 的整数桥接、
在全 $\mathcal U$ 的正则性、四条末端线上的系数理想及公共阶恰为 $a v_\pi(p)$。
循环迹插入／Cayley–Hamilton／Cartier 半线性和理想乘法仍属一般机制。
公共阶与 C2 扭子长度／扭子模的零阶 Fitting 的对应可作为一个准确关系陈述供评价，
不是已经构造了典范模同构，也不能把相等数字再包装成第三个独立方法。

P8 §5.5 已有 $(\mathbf M^{-1}-1)/\pi^p\bmod\pi$ 的首非零项与 p-curvature；
它要求近单位归一化与 equivariant 参数同缩放，不是原 $p^{-a}dI_r$。
P9 §§1.3–1.6 还包含 $p^s$ 阶特化，故不能说已有研究仅有一次零阶约化。
P10 的除整数 cyclotomic logarithm 也不能仅凭外形替本题提供 Witt lift／norm 接口。

Phase C 可比较的层级：**原积分整除微分的全模型实例识别 finding 候选**；
Hasse 指数是直接已有，普通层几何解释是标准。
若正文称“实际泛 Jacobian 的 Hasse 不变量”，旧 T2 的原谱 Jacobian 身份证明仍须完整保留；
同一四次式不自动完成该证明。特征二必须保留 $H_2=h$ 的独立合法解释。
超奇异下一阶、逐闭点提升赋值、$\pi$-饱和与典范模同构不在已证明范围。

### 5.4 提交 Phase C 的紧凑对照

| Claim | Closest works／直接扣除 | 尚需评价的准确 delta | 候选层级，不是最终 verdict |
|---|---|---|---|
| C1 | GHK 八环／通用周期族；Friedman 周期粘合；Stacks 派生基变换；Wagner q-Hodge 对角模型 | 原整系数八截面曲面的 $R\Gamma L_n\simeq K_n$，特别是整个共振基上的单位截面和扩张消失 | 几何结构 finding；不是新一般 cohomology／q-Hodge 方法 |
| C2 | JR 原圆分积分；Halphen/Frobenius/平坦常规工具；C1 模分裂 | 原完整 pencil 的平坦降阶、重数、非完整特化像及同一扭子模 | C1 的几何消费者与完整模型 finding；初等因子不再独立计数 |
| C3 | Vlasenko 1(i) 直接含 Hasse 乘子；循环矩阵与 Cartier；KS/Smirnov 根单位高阶理论 | 原 $p^{-a}dI_r$ 的整数桥接、全开放空间延拓、精确统一阶及与 C2 的关系 | 实例识别 finding；尚无来源支持称一般机制突破 |

## 6. 明确保留的缺口与禁止外推

1. Scholar/S2 未成功取回搜索结果；arXiv 搜索网页部分失败。公开 primary 能读并不消除数据库覆盖缺口。
2. Looijenga 1981、历史 Halphen 原文与 STT 的既有全文缺口不因本轮而关闭；未系统穷尽一般相对反典范族的整系数扩张分类。
3. JR 已发表原输入保留；本轮出版全文访问失败，不以作者 v2 的局部核读冒称已覆盖发表版全部变化。
4. Di Vizio/Hardouin、André–Di Vizio、旧 Cartier 原始引用的访问和量词限制继续保留；本轮不将已有转述升格为亲读。
5. P4/P5 表明 q-Hodge/圆分根单位 cohomology 的理论远比简单术语联想丰富；本件未构造 qPI 到该理论的额外兼容结构，亦未据此添加新科学主张。
6. 其他 Painlevé、quantum quiver、Habiro regulator 对象只在来源机制比较中使用；跨系统猜想仅可记 `ROUND2_CLUE`，不并入原族结论。
7. 组合内 Papers1–29 的真正消费者／定理包含不是本件的完成项；Phase C/D、正式双份四门和自然 22–30 页容量要求均未由本件替代。
8. 检索无命中、来源前提不匹配、论文使用标准工具三者都不单独决定新意或价值；本件不给分数、不授权立项／写稿／出 PDF。

## 7. 输入哈希与交付

以下哈希在本轮读取后核对，冻结 Phase A 未变；此前三份报告保持原样。

| 输入 | SHA-256 |
|---|---|
| Phase A | `bb463d1e1c27f543e4a0fe1bda17b584ffce28148e49ab1e1f3c3b1fce6b7ad5` |
| D | `e2f032ff1197d415be611670e3d233efd7f6ead0d7dbe16b05f796ed42f43652` |
| G | `59b308f605832d82e00720c5a3a7871c862698e194503ff3b289da592ced28e0` |
| U | `a1e50c82c32f5411dce28a2bf2ff2b10bf4fdefdb8ac9b127de852de5e36c42b` |
| 圆分退化先例 | `1c7ba39e3c2d6d661626e736b16f6d9a9599e0a8d07c0b2ead9e41f798da0cf8` |
| 整除微分来源差分 | `8d24144c5e49ba30402a2749536ec0b66ca6170d6dcf9a85273330829c22a88f` |
| 整系数上同调先例 | `26e901d014f553773838f20b1b3ea46b607deffbcf9d73a503cab3ef24570450` |

本次唯一新写本文件；全文回读后另向主控报告行数与 SHA-256。
技能影响在于逐项关键词覆盖、最近来源原文检查、机制／finding 分层与访问缺口披露；
并未将完整研究流水线、外部通知或后续正式评价的动作权限带入本轮。
