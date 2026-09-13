# Paper30：F 全局形式 gauge 与 A 逆作用谱的分支独立先例预筛

日期：2026-09-06。状态：`BOUNDED_PRIOR_PREFLIGHT`，非候选验收。
`route_applicability: NOT_APPLICABLE`；未给新颖性分数或长文容量 PASS。

## 1. 结论与本轮边界

**F：未检得直接给出所锁定全局多项式全阶分类的定理；仍有实质数学缺口，但没有由此证明新颖。**
比已扣除的局部中性乘子正常形更接近的先例，是参数形式非交换共边界的
可解性与解析可解性定理，以及一般 Lie 变形的全阶 gauge/障碍框架。
它们分别缺少 Hénon 全局多项式系数条件、或缺少具体 Hénon 分类计算。
固定有限参数族的非有效有限阶性也有明确 Noetherian 先例，不能独立主张为新机制。
截至收尾，根任务已将具体作者 claim 收紧为全部 $c$、$\deg h\le3$ 的全阶分类，
并声称三阶截断充分且最小；这比单一二阶反例更具体，但仍须独立审证。

**A：单周期谱的全参数有限纤维已经由经典 Lyashko–Looijenga（LL）理论覆盖，
不只是“泛有限”。** 含碰撞的临界点/值分层、各层有限覆盖，以及加入标记
monodromy 后的完整重构也有强先例。剩余问题只能是：在固定势能常数规范下，
哪些 LL 残余纤维真正被较高周期的未标记作用谱区分，以及全部未区分点是否恰为
实际规范保持辛共轭。未检得直接回答这个固定次数 Hénon 问题的定理。
根任务另报 quartic 的完整 $\chi_1,\chi_2$ 同谱而不共轭参数对；本轮按待审
作者 claim 定位，不能从“两周期”升级为“全部周期”非刚性。

两分支不合并，不调用量子、wild 或几何周期检测结果补足篇幅；本轮也不评价
根任务正在进行的数学探针是否正确或是否足够成文。

### 实际输入与技能适配

已读 `AGENTS.md`、`docs/WORKFLOW.md`、当前批次接续，以及
[portfolio](PAPER30_PORTFOLIO_SCREEN_20260906.md) §§5–6、12；
[landscape](PAPER30_LITERATURE_LANDSCAPE_20260906.md) 只复用 formal-B 范围与先例边界。
未重扫旧 PDF/build 树。两个研究输入 SHA256：

```text
portfolio: 50c6972d975d27a905266c5418b529b634c00b7b6ea5e1855915ee5806b4ca11
landscape: a57c482c2b036538d9ef70f2d151a860f720d4dc00ab1b656969e1d4619c88d6
```

完整读取并采用 `research-lit`、`novelty-check`：先扣除本地组合，再分核心检索、
核对一手正文、写明 delta 和访问限制。工具中没有 Zotero/Obsidian 或外部模型
评审端点；未调用跨模型评审，不能宣称已做。未找到可用 `arxiv_fetch.py`，
依技能允许回退到 arXiv 定向网页检索；不下载 PDF，不另建文献库。
会议列表中的 ML venue 与本任务不匹配，不为覆盖率机械加入。

## 2. 问题合同：不能混淆的量词

### F：固定指数曲线是否一直位于共轭轨道

固定任意 $c\in\mathbb C$，$H_c=(x^2+c-y,x)$，

\[
 \sigma=H_c^*,\quad A=\mathbb C[x,y],\quad\{x,y\}=1,\qquad
 g=h-\sigma h,\quad U_\varepsilon=e^{\varepsilon\operatorname{ad}_g}\sigma.
\]

要求 $C_\varepsilon=e^{\operatorname{ad}_{\varepsilon h+\varepsilon^2h_2+\cdots}}$，
每个 $h_j\in A$，且

\[
 U_\varepsilon=C_\varepsilon\sigma C_\varepsilon^{-1}.
\]

核心 F1 是全阶必要充分分类；F2 是是否有非平凡高阶障碍结构或有效有限判据。
参数形式 $A[[\varepsilon]]$ 不等于 $\mathbb C[[x,y,\varepsilon]]$，
也不要求各阶空间次数有共同上界，更不声称解析收敛。

这里 $U_\varepsilon$ 本身已是全阶定义的扰动；待解的是它的**共轭平凡性**，
不是任意延拓一个一阶变形。若另选高阶项把扰动定义成

\[
 e^{\varepsilon\operatorname{ad}_h}\sigma
 e^{-\varepsilon\operatorname{ad}_h},
\]

就改掉了锁定曲线，不能回答问题。
初始有限探针合同为 $\deg h\le4$、全部 $c$；收尾时根任务选择先审
$\deg h\le3$ 的完整分类，不将未完的四次分类设成本轮义务。可能的更大分类

\[
 h=aX_i+b,\qquad X_i=\sigma^i x
\]

在不限制 $\deg h$ 的范围仍是待证明方向，本报告不把它写成必要性结论。

### A：完整周期环上的特征多项式，而非导数谱

令 $p$ monic centered、次数 $d$，$P'=p$、$P(0)=0$。采用

\[
 \mathcal A_{P,n}=\sum_{i\bmod n}(x_ix_{i+1}-P(x_i)),\qquad
 R_{P,n}=\mathbb C[x_0,\ldots,x_{n-1}]/
 (p(x_i)-x_{i-1}-x_{i+1})_i,
\]

以及 $\chi_{P,n}(T)=\det(T-m_{\mathcal A_{P,n}}\mid R_{P,n})$。
短周期的两个邻项仍要重复计入。谱包含完整周期环的局部长度重数，
但**不记录乘法算子的全部 Jordan 结构**；不能把特征多项式叫作完整 scheme 重构。

核心 A1 是固定点临界值纤维的精确扣除；A2 是显式有限 $N(d)$ 的全参数重构
和全部残余同谱分类。P5 的代数作用量/P15 的导数迹有限纤维均不直接是此逆问题，
但不能借它们的对象不同忽略外部 LL 先例。

## 3. 实际检索角度与时间覆盖

每个核心采用至少三个措辞角度。以下记录实际使用的代表查询，而非拟议检索。

| 分支/核心 | 实际查询角度 | 命中及作用 |
| --- | --- | --- |
| F1 全局分类 | `Hamiltonian polynomial automorphism formal conjugacy deformation cohomology Hénon`；`"polynomial" "symplectic" "formal deformation" conjugacy coboundary`；`"Hamiltonian" "formal conjugacy" "polynomial automorphisms"` | 未命中锁定全局分类；很多结果其实为局部正常形或 Hénon–Heiles 连续系统，排除。 |
| F2 全阶障碍 | `"formal" "conjugacy" "coboundary" Lie group`；`"symplectic" "coboundary" "formal" deformation`；`"Hamiltonian" "gauge" "mapping cone" deformation automorphism` | 命中 de la Llave–Saprykina、Fiorenza–Manetti；分别定向读主定理。 |
| F2 有限阶性补检 | `"polynomial" "formal conjugacy" "Noetherian"`；`"Hamiltonian" "linearizability" "Noetherian"`；`"polynomial automorphisms" "conjugacy" "obstruction" "formal"` | 纳入 F-P3/F-P4：有限参数障碍理想稳定是明确既有技术；未命中锁定的 Hénon 全局多项式共轭判据。 |
| 最新窄 claim 补检 | `"Hénon" "Hamiltonian" "conjugacy" "cubic" formal obstruction`；`"polynomial" "coboundary" "third order" Hamiltonian`；`"Hénon" "action" "isospectral" quartic` | 未命中 $\deg h\le3$ 的全 $c$ 分类/最小截断 3，或锁定完整 $\chi_1,\chi_2$ 的 quartic 非共轭反例；Hénon–Heiles、量子化和轨道坐标和结果不等于这些 claim。 |
| A1 完整临界值纤维 | `"Lyashko Looijenga" polynomial critical values finite covering roots unity`；`"polynomials" "critical values" "reconstruction" Lyashko Looijenga Zvonkin Lando`；`"Multiplicities of the Lyashko-Looijenga map on its strata"` | 命中完整有限映射、退化分层和 multiplicity 文献，不限于 generic locus。 |
| A2 逆作用谱 | `"Henon" "action spectrum" inverse`；`"symplectic maps" "action spectrum" "inverse"`；`"Hénon" "action" "spectral rigidity"`；`"Hénon" "action spectra" reconstruction` | 未命中固定次数完整 Hénon 逆定理；命中经典 Anosov 引用链及 2025 标准映射部分同谱变形。 |
| 2024–2026 | `"Hamiltonian" "Hénon" deformation conjugacy after:2024-01-01 before:2026-09-07`；`"Lyashko Looijenga" "critical values" after:2024-01-01 before:2026-09-07`；`"Hénon" "action spectrum" after:2024-01-01 before:2026-09-07` | 2024 LL 分层论文与 2025 作用谱非刚性论文纳入；不按抓取日期当发表日期。 |
| 最近六个月 | `site:arxiv.org "Hénon" "formal" after:2026-03-06 before:2026-09-07`；同时间窗 `"Lyashko"`、`"symplectic" "action spectrum" "rigidity"`；另以 arXiv 域和 `recency:184` 检索两分支 | 最初返回旧论文/邻近题目；后按新有限阶 claim 核实 F-P3 发表日期为 2026-07-20，纳入六个月窗口。其主题相邻但不直接覆盖 Hénon 分类。检索未命中不构成不存在证明。 |

日期核对：Dougherty–McCammond 的 arXiv 摘要页仅列 2024-10-04 的 v1；
HTML 的 `Date: August 24, 2026` 与该 submission history 不一致，不能据此
宣称它是近六个月新版本。Li 的摘要页明确仅列 2025-12-03 v1，亦不伪计入六个月。

## 4. 八篇核心一手来源及实际阅读深度

“正文定理已读”只表示读到指定命题和相关设置，不等于独立审完该论文证明。

| ID / 来源 | 实际读取 | 覆盖结果与不覆盖部分 |
| --- | --- | --- |
| **F-P1** R. de la Llave, M. Saprykina, *Nonconmutative coboundary equations over integrable systems*, arXiv:2205.12356v1 (2022)。[正文](https://arxiv.org/html/2205.12356)、[版本](https://arxiv.org/abs/2205.12356)。本轮按预印本使用。 | §1，Definition 2、Theorem 3、Remark 4/6，§3 递推设置和 §4 群值扩展。 | 可积基映射 $f(\theta,I)=(\theta+I,I)$ 上，近单位解析 cocycle 的全周期乘积条件、参数形式解存在、解析解存在等价。原形式解不必自身收敛。不是全仿射平面上的多项式 Hamiltonian 自同构分类。 |
| **F-P2** D. Fiorenza, M. Manetti, *$L_\infty$ structures on mapping cones*, Algebra & Number Theory **1** (2007), 301–330，DOI 10.2140/ant.2007.1.301。[作者预印本正文](https://arxiv.org/html/math/0601312v3)。 | Introduction / Theorem 1，Theorem 5.5，§6 的 MC–gauge 识别，Theorem 7.4。 | 对 DGLA morphism 的 mapping cone 给出含 Bernoulli 高阶括号的结构及 gauge 等价描述。一般框架成熟；未算本题的 Hénon 全局多项式障碍，不推出任何 $h$ 分类。 |
| **F-P3** P. Mardešić, D. Novikov, L. Ortiz-Bobadilla, J. Pontigo-Herrera, *Noetherianity and Length of Melnikov Functions*, Bulletin of the Brazilian Mathematical Society, New Series (2026)，发表 2026-07-20，DOI 10.1007/s00574-026-00521-7。[出版社全文](https://link.springer.com/article/10.1007/s00574-026-00521-7)。 | 本代理直接读取 Theorems A/B 及 §2.1；并核对作者、日期。 | §2.1 明确指出有限维解析扰动族中首个非零 Melnikov 阶数有统一上界是简单 Noetherian 结论，并区别于有效复杂度问题。主定理涉及未固定扰动次数的轨道长度问题，不是本题全局 Hénon gauge 分类，不能转用。 |
| **F-P4** B. Arcet, J. Giné, V. G. Romanovski, *Linearizability of planar polynomial Hamiltonian systems*, Nonlinear Analysis: Real World Applications **63** (2022), 103422，DOI 10.1016/j.nonrwa.2021.103422。[出版社](https://www.sciencedirect.com/science/article/pii/S1468121821001346)。 | 出版社搜索索引公开了有限参数消元理想 $J_k$ 的稳定段落；直接全文打开 internal error，未完成全文阅读；未改用其他全文入口。 | 局部线性化问题中以 Hilbert basis theorem 得到 $J=J_{k_0}$；可见陈述给必要条件，不能升级为本题的充要条件。这个有限理想套路应扣除，局部空间形式级数不等于参数形式全局多项式共轭。 |
| **A-P1** M. Dougherty, J. McCammond, *Geometric Combinatorics of Polynomials II: Polynomials and Cell Structures*, arXiv:2410.03047v1 (2024)。[正文](https://arxiv.org/html/2410.03047v1)、[版本](https://arxiv.org/abs/2410.03047)。 | §7，尤其 Theorems 7.3/7.14、Remarks 7.6/7.7/7.15；§11 的 Proposition 11.6 及其证明。 | 明陈经典 LL 全局 finite map；含临界点与值碰撞的双分层上为有限覆盖；临界值多重集加相容的已标记 monodromy 唯一确定 monic centered 多项式。原文也将后两类结果与旧先例相连；不能将 monodromy 当成用户已提供的谱数据。 |
| **A-P2** M. Dougherty, J. McCammond, *Critical points, critical values, and a determinant identity for complex polynomials*, Proc. Amer. Math. Soc. **148** (2020), 5277–5289。[作者预印本](https://arxiv.org/html/1908.10477)。 | 引言 Theorems A–C 及常数为零的积分规范，§5 分层设置。 | 对规定临界点重数、monic derivative、常数零的多项式给临界值 Jacobian 显式分解与分层局部可逆性。局部条件含临界点互异且非零；不能删去非零条件，也不是较高周期 Hénon 同谱分类。 |
| **A-P3** D. Zvonkine, *Multiplicities of the Lyashko–Looijenga map on its strata*, C. R. Acad. Sci. Paris Sér. I Math. **324** (1997), 1349–1353，DOI 10.1016/S0764-4442(97)83573-2。[出版社](https://www.sciencedirect.com/science/article/pii/S0764444297835732)。 | 出版社索引摘要可见；直接打开 403，停止。未读原定理或公式。A-P1 Remark 7.15 的归因已读。 | 摘要明确研究各临界点/值分层的纤维数。它是不可忽略的强先例风险；本轮不独立引述其具体乘数公式，也不将二手归因升级成已核原证明。 |
| **A-P4** Yunzhe Li, *Deformations of the Standard Map with Prescribed Actions and Lyapunov Exponents*, arXiv:2512.03865v1 (2025)。[正文](https://arxiv.org/html/2512.03865v1)、[版本](https://arxiv.org/abs/2512.03865)。 | Theorems 1.1–1.3，随后常数规范说明，§2 逆谱定位。 | 标准映射的非平凡解析势能族可保持无限条选定周期轨道作用量；另一构造可保持文中称为 Lyapunov exponent 的指标。不是全部周期的完整未标记谱，也不是有固定次数的复多项式族；势能加法常数按其作用目标选定，不是本题 $P(0)=0$。 |

其他访问边界：已核 [de la Llave–Marco–Moriyón 的 1986 Annals 元数据](https://annals.math.princeton.edu/1986/123-3/p03)，
页面无摘要。检索到其 Anosov 同作用谱变形刚性的引用线索，但未直接读原 Theorem 1.3，
故本报告不把其精确假设/结论当作已核定理。
Guillemin–Melrose 1981 *A cohomological invariant of discrete dynamical systems*
的原 DOI 访问失败（[出版社链接](https://doi.org/10.1007/978-3-0348-5452-8_53)）；
只在 A-P4 §2 看到逆作用谱问题的历史归因，不宣称已读原章节。
另已见 Looijenga 1974 原始书目信息；本轮有限性所依赖的明确可读陈述为 A-P1 Theorem 7.3。
未绕过任何访问限制，也未使用 ResearchGate/自动综述的技术断言作为证明依据。

## 5. F 的精确 delta 与停止点

F-P1 表明“全阶形式非交换共边界问题”这一母题并不新。
但其 $\phi_\varepsilon(\theta,I)$ 是在固定基动力系统上的点值 cocycle gauge，
本题 $C_\varepsilon$ 是改变 $(x,y)$ 的 Hamiltonian 代数自同构；不能把两种乘法
和周期条件等同。尤其不能以解析解存在替代各阶系数为多项式。

F-P2 表明高阶括号、Bernoulli 系数、MC/gauge 术语并不能独立承担新意。
还有一个类型检查：$1-\sigma:A/\mathbb C\to A/\mathbb C$ 一般不是 Lie algebra
morphism，不能不加构造地把它直接代入 F-P2 的 $\chi$。若要使用
homotopy equalizer/graph–diagonal 模型，必须先证明该模型确实表示本题；
本报告没有构造或验收这种模型。

此前局部中性乘子正常形已在 landscape 扣除，本轮不重复打开。
它不能解决 parameter-adic global polynomial 分类，也不能反过来作为支持该分类的证据。

本题必须保留常数中心：

\[
 [\{h,\sigma h\}]=0\quad\text{in }A/((\sigma-1)A+\mathbb C)
\]

只是已扣除的二阶条件。若 $\{h,\sigma h\}\in\mathbb C$，相应 Hamiltonian
导子已经交换，给出的全阶充分性是短 BCH 事实，并不要求括号本身为零。
因此 $h=aX_i+b$ 的显然充分分支不能充作全阶分类的主要难点；真正价值在于
排除所有其余 $h$、找到首次高阶失败的非平凡核内类，或证明有效有限判据。

### 最新作者 claim 的先例扣除

根任务收尾通知的窄合同是：全部 $c$、所有 $\deg h\le3$，二阶核含两种
非坐标参数曲线族及 reversor 像；作者声称相应三阶证书分别有恒非零分量
$30$ 和 $14/9$，排尽非坐标分支，给出全阶分类。另称 $\deg h\le2$ 时
二阶足够，而三次合同的 cutoff $3$ 是最小的。本报告只定位这些明确量词，
没有复算证书，也没有独立验收分类或最小性。

若独立审证成立，增量是**全参数二阶核分层、第三阶确实排除的机制以及显式
最小截断阶数**；它不由 F-P1/F-P2 的一般形式框架、或 F-P3/F-P4 的非有效
Noetherian 原则直接推出。单个“过二阶、败三阶”例子本身比这个完整分类弱得多。
补检未找到直接同定理，但这仍不是全世界新颖性证明，也不是长文容量通过。
更高次数全部分类未完成，不可用 $\deg h\le3$ 推出不设次数界的必要性。
只在 generic $c$ 成立的除法论证，也不能回答这里的全部 $c$ 合同。

根任务另有[统一形式 gauge 作者论证](PAPER30_UNIFORM_FORMAL_GAUGE_PROOF_20260906.md)，
本轮读取的 SHA256 为
`052366584730be71cd4426fae0e5d5470fc7ffa1fb8928b1f5c4005bf40ee3a0`。
它使用 Paper29 轨道分裂、BCH、有限参数障碍理想与 Noetherian 性，
声称固定 $\deg p=d,\deg h\le D$ 时有统一但未给值的 $N(d,D)$，
并给共轭存在 locus 的代数性与逐阶递推。一般 BCH、障碍理想代数性、
Hilbert basis theorem 都须扣除；F-P3/F-P4 使“有限阶本身是新原则”的说法不可维持。
具体的参数正则全局多项式分裂与精确共轭充要量词，仍须另按实际证明评估。
作者文本本身已承认没有有效界、复杂度或可识别停止判据；连续几阶理想
不变不保证永久稳定。这不是任意更高阶扰动的 finite determinacy。
其唯一性对象是 tangent-to-identity 正式辛共轭，Hamiltonian 生成元逐阶加
常数的自由度只有在正规常数为零后才消除。这里仅查新定位，不重复数学审查。

## 6. A 的 LL 扣除与规范检查

以下为把已读先例落实到锁定对象的直接代数识别；不是另一个查新通过的主定理。
对当前 cubic/quartic 测试（一般 $d\ge3$），令 $m=d+1$，

\[
 Q(x)=m\bigl(P(x)-x^2\bigr).
\]

则 $Q$ monic centered、$Q(0)=0$，且

\[
 Q'=m(p-2x),\qquad \mathcal A_{P,1}=x^2-P(x)=-Q(x)/m.
\]

故 $\chi_{P,1}$ 恰记录 $Q$ 临界值多重集的统一缩放；非约化临界点的局部长度
与临界值重数一致。临界点不同而临界值相同则在特征多项式中合并重数。

A-P1 Theorem 7.3 所述完整 monic centered $m$ 次多项式空间上的 LL 映射
是 finite，generic degree 为 $m^{m-2}$。限制到闭切片 $Q(0)=0$ 仍是有限
映射到其像，因而**每个固定点作用谱的参数纤维都有限**。不能把完整空间的

\[
 m^{m-2}
\]

原样当成常数零切片的 generic 纤维数；更不能把有限性误写为唯一性。
含碰撞分层的有限覆盖也已覆盖，独立贡献不能只是“我们考虑了退化”。

若扩展到 $d=2$，$Q=3(P-x^2)$ 带二次项，不自动 centered；需固定变量平移
后重新记录常数，不能继续把同一个 $Q(0)=0$ 切片公式硬套过去。

### 单位根歧义不是自动允许的辛共轭

对 $\zeta^m=1$，$Q_\zeta(x)=Q(\zeta x)$ 保持单点临界值多重集及常数零。
其对应势能和映射多项式为

\[
 P_\zeta(x)=P(\zeta x)+(1-\zeta^2)x^2,\qquad
 p_\zeta(x)=\zeta p(\zeta x)+2(1-\zeta^2)x.
\]

因此 $P_\zeta$ 仍满足本轮规范且与 $P$ 固定点作用同谱。
但 $S_\zeta(x,y)=(\zeta x,\zeta y)$ 拉回辛形式为

\[
 S_\zeta^*(dx\wedge dy)=\zeta^2dx\wedge dy.
\]

一般单位根不可仅凭一维多项式预复合就商掉。
在允许的 $\zeta=-1$ 情形（$m$ 偶数）确有对角辛共轭；这里没有证明
所有可能的规范保持辛共轭只有这种形式。

直接代入还给出

\[
 \mathcal A_{P_\zeta,n}(z)-\mathcal A_{P,n}(\zeta z)
 =-\frac{1-\zeta^2}{2}\sum_{i\bmod n}(z_{i+1}-z_i)^2.
\]

右端在 $n=1$ 消失，说明单点歧义如何产生，也说明较高周期耦合为什么可能有用。
它**不证明**临界集合相互对应或未标记临界值谱已经分离，不能替代完整消元。
对 cubic $p=x^3+Ax+B$，$\zeta=i$ 对应

\[
 (A,B)\longmapsto(4-A,iB),
\]

而 $\zeta=-1$ 对应真正的辛对称 $B\mapsto-B$。
这只是可检验的单点同谱来源，不声称穷尽 cubic 特殊纤维。

### 仍可能有价值的 A 结果

1. 在所有 cubic 参数、尤其临界点/值碰撞处，完整列出
   $(\chi_1,\chi_2,\ldots)$ 同谱残余，并证明其恰是实际允许共轭；quartic 另作合同。
2. 对任意次数给出统一且显式的 $N(d)$，并解释作用耦合为何消去完整 LL 纤维的
   monodromy 歧义，而非只消去显然单位根。
3. 找到不由允许共轭解释的全部周期同谱反例，若真有，则须按原规范证明。

这些均为开放义务。A-P4 的无限**选定**周期轨道同作用变形不回答其中任何一项；
不能把“无限多”偷换成“全部”，也不能拼接作用量与导数数据的不同构造。
仅证明固定点有限纤维、重述 LL 分层，或完成少数低次数相减例子，应短闭合停止。

### 最新 quartic 负结果的准确边界

根任务收尾通知已找到 quartic 的完整 $\chi_1,\chi_2$ 相同而不由允许共轭
解释的参数对，并将补完整证明。本报告未读取该尚待交付的最终证明，也不把
先期计算自动改标为定理。若证明成立，它排除该次数上用前两周期唯一重构
的命题，比仅说明 LL 单周期纤维非平凡更进一步；但不排除 $N(4)>2$ 的有限
重构，更不推出全部周期同谱反例。补检未找到这个具体完整两周期反例的直接先例。
其“完整”必须继续包括周期环局部长度重数，而非只列数值不同的作用值，
非共轭也须排除合同内全部允许共轭，不仅显然对角变换。

## 7. 交付限制与下一步

本轮八篇核心来源足以排除明显重复，并定位两个不同增量；不足以支持“首次”、
“文献穷尽”、完整世界新颖性或 22–30 页容量判断。
F 当前应独立审查全 $c$、$\deg h\le3$ 分类与最小三阶截断，并单独衡量扣除
一般 Noetherian 原则后，统一定理的具体增量。A 则独立审查最新 quartic
完整两周期同谱而不共轭的证明，再判断是否存在更高周期的统一机制。
不为本轮强加四次 gauge 完整分类；两分支不相互补页，也不借旧候选例外取得立项。

本次仅新增本文件。未改冻结稿、锁或旧评审；未运行实验、下载 PDF、编译、
外发、上传或使用付费资源。正文定理已读、摘要级先例、访问失败与本报告自身
规范推断已分别标明；外部模型验证未执行。
