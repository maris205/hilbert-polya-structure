# Paper30：完整作用谱统一重构与最小周期截断的专项查新补充

日期：2026-09-06。`BOUNDED_NOVELTY_SUPPLEMENT`；非候选验收。
`route_applicability: NOT_APPLICABLE`。不评分、不授予容量或候选 PASS。

## 1. 结论先行

新的作者包已把问题从“低次数例子＋偶周期对称障碍”推进到明确的统一重构命题：
所有 $d\equiv1\pmod4$ 的二项 Hénon 族具有全参数、最小初始截止 $N=2$；
七次族的两周期全部纤维分类加三周期分离给出全参数、最小截止 $N=3$。
这是真正改变结论量词的增量，不能直接套用旧的“只有短偶周期对称”判断。
本报告只做先例核查；这些命题的数学验收由独立主控核查承担。

专项检索未定位到直接陈述上述完整作用量特征谱重构、同余次数族及精确最小
截止的原定理。这个“未定位到”有明确检索和访问边界，不是世界首创证明。
新增最接近的近期定理是 Cantat–Dujardin 2026 的 Hénon 第一、二周期**导数乘子**
有限纤维与一般参数唯一性；它要求的可观测量不同，也不是本题的全参数作用谱结论。

应充分扣除的工具包括 LL 有限性、完整零维代数的带重数迹、唯一分解中的
重数奇偶提取、单位根在互素剩余特征下的单射约化，以及 Gómez–Meiss 已有的
$\pm B/i$ 有限对称机制。三移位幂引理未找到同措辞的经典原定理，但其短证明
只需标准单位根约化与消元；不应靠它主张新的数论机制。
本轮既不因这些工具经典而否定尚未被覆盖的重构定理，也不因组合成立而自动
授予独立长文容量。

## 2. 冻结输入与本轮实际阅读

本轮全文读取以下两份作者输入，读取前核对行数与 SHA256 均与委派一致：

| 输入 | 实际阅读 | SHA256 |
| --- | --- | --- |
| [统一重构证明](PAPER30_ACTION_PARITY_RECONSTRUCTION_PROOF_20260906.md) | 全部 372 行，包括 A1–A10、三移位幂引理、全参数剥离、七次全部纤维、三行第三周期迹证书及限制。 | `2d7a84ce1478566153d0639222fec9995b70e4a9acd3c33a00f7913c55862bb3` |
| [二项族高次数探针](PAPER30_BINOMIAL_ACTION_HIGHER_DEGREE_PROBE_20260906.md) | 全部 390 行；特别核对依赖 Steps 1–3 的自由基、完整单周期谱、二周期统一因式分解与全参数延拓，不只读摘要。 | `804be063faf1b07371c51b5dd8ca80bcd6fb402abdf7c678e411643aad363125` |

复用此前已读的 [305 行先例预筛](PAPER30_GAUGE_ACTION_PRIOR_PREFLIGHT_20260906.md)
和 [254 行 A/M 分支报告](PAPER30_ACTION_PARITY_MATRIX_PRIOR_20260906.md) 的 LL、
Gómez–Meiss 及作用谱背景；不修改或重新评价这些冻结文件。
旧 478 行 `PAPER30_ACTION_INVERSE_FIRST_PROBE_20260906.md` 本轮未重新读取，
不复审其三次／四次证明或既有查新。主控通知的全中心三次重构、四次反例若作为
“多少完整周期作用谱足够”的低次数边界，在问题上与本轮同属一线；这不是
形式 gauge 或几何结果的拼接，但本轮也不据此判断篇幅门槛。

完整重读 `research-lit`、`novelty-check`，按其要求分核心、多措辞、查近期和原定理。
本轮明确限制覆盖技能中的评分／扩张建议。未调用子代理、外部评审、外部写入，
未下载 PDF、未新建文献库或正式项目。无可用 Zotero/Obsidian、跨模型评审端点或
`arxiv_fetch.py` 的既有检查结果沿用，使用 arXiv 定向网页检索；不宣称这些缺失步骤已执行。

## 3. 新 claim 的准确对象

固定奇数 $d\ge3$，$p_{d,B}=x^d+Bx$，
$P_{d,B}=x^{d+1}/(d+1)+Bx^2/2$，$P(0)=0$。谱为整个
$R_{n,B}=\mathbb C[x_i]/(x_i^d+Bx_i-x_{i-1}-x_{i+1})_i$ 上的作用量
乘法特征多项式 $\chi_{n,B}$；短周期重复邻项及局部长度均保留。
它不是 $DH^n$ 的特征多项式、不是作用 Hessian、不是 Jordan 结构或周期环重构。

记 $q=(d-1)/2$、$m=q+1$、$\kappa=q/(q+1)$。本轮分三项核查：

1. **统一数据提取与完整逆定理。** $\chi_1$ 给出 $(B-2)^m$；二周期分解
   $\chi_2=TD_-^2D_+^2G_B^4$ 的重数模 $2$ 提取给出 $(B+2)^m$；新公式
   \[
   \operatorname{Tr}(m_{\mathcal A_{n,B}}^q)
   =-n(d-1)d^{n-1}(-\kappa/2)^q B^m,\qquad n\ge2,
   \]
   给出第三不变量 $B^m$。三个不变量在 $m$ 奇数时共同单射，故全部
   $d=5,9,13,\ldots$ 的完整 $\chi_1,\chi_2$ 唯一确定 $B$，且 $N=2$ 最小。
2. **辅助三移位幂引理。** 奇数 $m\ge3$ 时
   $z\mapsto(z^m,(z-2)^m,(z+2)^m)$ 在 $\mathbb C$ 上单射。
   这是重构的代数接口，不是另行建立一种新数论理论。
3. **七次全参数截止。** $d=7$ 的完整两周期谱仅有一个非平凡无序纤维
   $\{2i,-2i\}$；第三周期的第九矩非实值将它分开，所以全族最小 $N=3$。
   $N$ 指所用初始周期 $1,\ldots,N$，不是所用矩阶数。作者没有声称第九矩
   是所有可能分离矩中的最小阶数。

一般 $d\equiv3\pmod4$、$d>7$ 的奇周期分离和完整截止仍 OPEN。
原偶周期对称对任意参数成立，并不蕴含全部周期作用谱碰撞。

## 4. 实际检索角度与最新窗口

以下列本轮实际执行的代表查询，非后续计划。英文重音和无重音拼写交替使用。

| 核心 | 三种以上查询角度 | 定位结果 |
| --- | --- | --- |
| 完整作用谱逆问题 | `Hénon action spectrum reconstruction polynomial binomial`；`Henon action spectral period inverse`；`polynomial periodic action moments reconstruction`；`symplectic map action spectra inverse reconstruction` | 未定位同对象的统一二项族原定理。必须排除导数谱、Hénon–Heiles 连续模型、多重分形谱及波动方程的 action spectrum 同名结果。 |
| 迹提取与重数剥离 | `multivariate Newton sums trace`；`polynomial equations trace formula residue Sturmfels`；`trace Pham system Newton`；`action characteristic polynomial multiplicities Henon`；`period two action factorization polynomial` | 定位 D’Andrea–Jeronimo 的完整零维代数迹定理及 Briand–González-Vega 的 Newton sums 线索；未找到所锁定作用谱的 $2/4$ 重数剥离定理。 |
| 三移位幂注入 | `translated powers injective complex`；`polynomial map z^n (z+1)^n injective`；`three shifted powers complex injective`；`(x+1)^n (y+1)^n (x-1)^n` | 未检得直接同引理；若干“shifted powers”结果实际研究递推数列完美幂或多项式表示线性无关，不等于参数点分离。 |
| 单位根／余切改写 | `roots of unity cotangents arithmetic progression`；`cotangent arithmetic progression rational angles`；`cotangent rational multiples arithmetic progression`；`roots of unity reduction injective prime` | 互素阶单位根的单射约化是标准事实；未找到直接覆盖此三点配置的原始余切等差定理。不能把索引中的相关词当作等价命题已经发表。 |
| 七次与最小截止 | `Henon action spectrum minimal period cutoff`；`seventh degree Henon action trace`；`binomial Hénon spectra`；`periodic action minimal period polynomial` | 命中的是谱刚性／动力模型背景，没有精确的七次完整两周期纤维及最小第三周期定理。不能仅凭第九矩检索未命中主张该数字的新意。 |
| 2024–2026 | 上述 Hénon/action/reconstruction、translated powers/injective、roots of unity/AP、multivariate Newton sums/trace 查询加入 `after:2024-01-01 before:2026-09-07` | Cantat–Dujardin 2026 和 Li 2025 保留；检索器返回的旧文不冒算为近期文献。 |
| 最近六个月 | arXiv 定向 Hénon/period/rigidity、Hénon/action/reconstruction、roots of unity/injective/powers，使用 `after:2026-03-06 before:2026-09-07`，并用 `recency:184` 补检 | Cantat–Dujardin v1 的 2026-03-10 已核；没有定位到该窗口内直接覆盖新增作用谱重构的原文。前次已核 Bianchi–He 2026-06-28 的乘子 cocycle 工作仍只作旧背景，本轮不重做综述。 |

窄查询多次返回无直接结果或误匹配，已按对象剔除；没有把检索失败当作不存在证明。
未通过受限全文、私人凭据或下载路径扩大访问；ML 会议目录不匹配本次数学主题，未机械填充。

## 5. 五个核心一手来源：新增核读与明确复用

“核读”仅指指定正文命题及必要设置，不等于独立审完各篇全部证明。

| ID | 一手来源与实际阅读 | 正确覆盖与剩余差额 |
| --- | --- | --- |
| P1 | M. Dougherty、J. McCammond，*Geometric Combinatorics of Polynomials II: Polynomials and Cell Structures*，arXiv:2410.03047v1 (2024)。复用已读 §7 Theorems 7.3/7.14、§11 Proposition 11.6。[作者正文](https://arxiv.org/html/2410.03047v1) | monic centered 多项式的 LL 映射全局有限，含碰撞的分层也有覆盖理论；加标记 monodromy 可重构。不给较高周期的未标记作用谱剥离或本题全参数单射。经典 LL 本身不归功于这篇 2024 论文。 |
| P2 | A. Gómez、J. D. Meiss，*Reversors and symmetries for polynomial automorphisms of the complex plane*，Nonlinearity **17** (2004)，975–1000。复用已读 Theorem 1、Proposition 8／Corollary 9、§5 Example 5.1。[作者发表版](https://amath.colorado.edu/faculty/jdm/papers/Reversors.pdf) | 奇 Hénon 的中心反射、有限旋转、$y^3\pm ay$ 与 $ip_2(iy)=p_1(y)$ 的平方根结构是强机制先例。应扣除共同偶次迭代对称；未给本题作用量谱的统一逆定理或七次截止。 |
| P3 | C. D’Andrea、G. Jeronimo，*Rational Formulas for Traces in zero-dimensional Algebras*，arXiv:math/0503721v2，2008-11-20；初稿 2005，v2 记录注明已获 AAECC 接收。新增核读 §1 与 §2.1 Theorem 2.1 及证明。[作者正文](https://arxiv.org/html/math/0503721v2)、[版本](https://arxiv.org/abs/math/0503721) | 特征零、任意零维理想、$r=p/q$ 的分母在商代数非零因子时，乘法迹由广义 Chow form 的对数方向导数表达；重数明确是局部代数维数。这个一般仿射版本包含非约化点和原点，不必误用需在 torus 中的后续版本。覆盖带重数迹与代数消元框架，不直接陈述本题 A1 或逆谱阈值。 |
| P4 | S. Cantat、R. Dujardin，*Multiplier rigidity for complex Hénon maps*，arXiv:2603.09445v1，2026-03-10，预印本。新增核读 Theorem A、§3.1–3.2、Theorem 3.7 及证明、Theorem 4.2 与 §4 相关证明。[作者正文](https://arxiv.org/html/2603.09445v1)、[版本](https://arxiv.org/abs/2603.09445) | 固定次数的单 Hénon 族具有统一有限周期／有限纤维界；Jacobian 不等于 $-1$ 时，周期 1、2 的导数乘子已给有限纤维，并在稠密 Zariski 开集上唯一至共轭。数据采用 formal-period 多重集。不是作用量谱，也不是任意参数唯一。本题 Jacobian 为 $+1$，不能以基族不适用为由忽略此先例。 |
| P5 | Y. Li，*Deformations of the Standard Map with Prescribed Actions and Lyapunov Exponents*，arXiv:2512.03865v1，2025-12-03，预印本。沿用旧定位，本轮定向重读 Theorems 1.1–1.3。[作者正文](https://arxiv.org/html/2512.03865v1) | 标准映射的非平凡解析势能族可以保持无限多条选定、随参数解析延拓的周期轨道作用量；构造利用趋向 Liouville 旋转数的周期轨道序列。不是固定次数复二项族，不保持每个周期的全部作用量多重集，不反驳本题低周期完整重构。 |

P4 的正式 arXiv 日期为 2026-03-10，而 HTML 中另有 2026-08-24 的 Date 字段；
按 submission history 计入六个月窗口，不把转换页面日期当成新版本。
P1 仍是 2024 v1，P5 仍是 2025 v1，均不伪计入最近六个月。

辅助访问限制：Briand–González-Vega，*Multivariate Newton Sums: Identities and
Generating Functions*，Communications in Algebra **30** (2002)，4527–4547，
[出版社索引](https://www.tandfonline.com/doi/abs/10.1081/AGB-120013337) 可见摘要及元数据；
大学公开仓储的两个正文入口均返回 internal error，未读到完整原定理，故不计入
上表已核正文来源，也不据索引声称其精确覆盖 A1。Warwick 作者数论讲义的索引
能见互素阶单位根约化陈述，初次打开返回 PDF 元数据，后续正文定位请求失败；
同样不作为已读原定理。P3 作者发表清单请求超时，故不猜其最终卷页。
旧报告中已未读的受限源本轮未再次尝试，也未绕过访问限制。

## 6. 各新核心的先例扣除与真实 delta

### 6.1 统一谱重数剥离与 $B^m$ 迹

P1 已覆盖 $\chi_1$ 对应的有限临界值纤维；P3 已明确覆盖完整零维代数中
$\operatorname{Tr}(m_f)=\sum_z\ell_zf(z)$ 的带重数信息和相应精确计算。
因此“使用完整有限代数”“从谱取矩”“允许非约化特殊化”不是新的母题。
单首首项 $x_i^d$ 的标准基、次数下降计数、特征多项式给出幂和也应扣除。

当前具体证明的作用在于把这些工具组织成一个全参数可提取接口：
$\chi_1\rightsquigarrow(B-2)^m$，二周期重数奇偶
$\rightsquigarrow(B+2)^m$，以及 A1 $\rightsquigarrow B^m$。
这里并不是普通“去重根”：普通 square-free radical 会留下 $G_B$ 中的根，
而作者使用的是因子赋值模 $2$，丢掉偶重数部分。其正确性依赖本族
$D_+=T^q+a$ 的结构以及 $a=0$ 的单独处理。

新读的 390 行依赖文本已给出非空简单参数开集、monic 除法与第四次根系数递推，
从而把因式恒等式延拓到全部参数；不应再把“尚须证明全参数延拓”照搬为当前
未解决缺口。独立证明是否严密由数学核查承担。本轮没有发现直接陈述这一
Hénon 作用谱分解／参数接口的外部原定理。

这项接口仍由标准工具构造；A1 的一般单次约化引理是短的基系数计算，不应
单独包装成新的普适迹理论。其价值应按它实际闭合的重构问题衡量。

### 6.2 三移位幂引理：精确出处未定位，标准证明机制充分扣除

作者将一个可能的碰撞编码为三个 $m$ 次单位根 $\zeta,\eta,\theta$，并得到

\[
2\zeta-\zeta\eta-\zeta\theta-\theta-\eta+2\eta\theta=0.
\]

当 $m$ 奇时，$X^m-1$ 在剩余特征 $2$ 下可分；在包含所有这些单位根的数域
整数环中取 $2$ 上方的素理想，约化因而在 $\mu_m$ 上单射。这是标准的
“与剩余特征互素的有限单位根不合并”事实，作者证明本身已给出其初等理由。
关系约化为 $(\bar\zeta+1)(\bar\eta+\bar\theta)=0$，再回到特征零的原等式
排除碰撞，属于这一经典事实的短应用。

专项检索未找到直接命名上述三移位幂注入的论文定理，也未找到余切等差改写
完全覆盖其量词的原始陈述。故不能说“已经查到同一个引理发表过”；同样不能
反向声称它是一项新的数论发现。稳妥定位是自包含的辅助代数引理，扣除单位根
可分约化、根单位比值编码与初等消元，不把其本身作为容量支柱。

某些偶数 $m$（如 $m=4$）的失败由作者给出的参数碰撞体现；只证明奇数 $m$ 足够当前
$d\equiv1\pmod4$ 合同，不据此宣称解决全部指数或所有平移配置。

### 6.3 完整全参数重构：不能混淆近期导数谱先例

P4 使“任意次数 Hénon 的第一、二周期谱能做刚性”这一笼统口号已有强先例。
但其可观测量是 $\operatorname{tr}(DH^n)$／乘子，作者使用的是 $m_{\mathcal A_n}$。
作用量值并不自动给出作用 Hessian 或导数乘子。P4 的环境稠密开集也不能在
没有检查的情况下限制成每个特定子族的所有参数结论。

本题实际上已有线性单射的固定点导数迹加权总和
$\mathcal D_d(B)=2d(d-1)-d(d-2)B$；若输入导数数据，单周期即能区分 $B$。
所以此处的 $N=2$ 或 $3$ 真正取决于**作用量这一不同可观测量**，不是复述
乘子刚性。最新先例未直接提供从完整作用量谱到三移位幂的接口，也未给出
同余次数族的全参数唯一性和最小性。

若独立数学核查通过，新度数统一结论应准确称为：固定零常数规范、完整局部
长度重数下，二项族 $d=5,9,13,\ldots$ 的最小两周期重构。它不由 LL 的有限性
直接推出，且量词明显强于孤立五次实例。这是当前可辨识的主要命题增量。

### 6.4 七次第三周期：闭合全部残余，而非孤立矩数值

作者先由三项四次幂提取证明 $B'=\pm B$，再证明唯一非平凡两周期纤维是
$\{2i,-2i\}$。在此之后，第三周期一个非实矩证书已足以闭合整个七次族；
不能把这一步描述成“只有某参数碰巧算出一个不同矩”。
作者给出的

\[
\operatorname{Im}\operatorname{Tr}(m_{\mathcal A_{3,2i}}^9)
=-\frac{5338324845}{2048}
\]

有三类满支撑单项式、基向量计数与 multinomial 和的手算接口；本报告读了该
证书及其 proper-support 论证，但没有另做算术复算，也未借诊断运行给数学 PASS。
Gómez–Meiss 的有限对称解释偶周期不能分离，不解释这个第三周期的完整残余
分离结论。P3 的一般迹计算框架也不直接断言此证书或该截止。

本轮未定位相同的七次全纤维分类与最小 $N=3$ 原定理。
这里值得定位的是从“必要有奇周期”到“第三周期已充分”的严格阈值变化，
不是上述有理数的位数，也不是把第九矩误称为最小矩阶数。

## 7. 交付判定与禁止外推

`TARGETED_PRIOR_SEARCH_COMPLETE`：新增统一逆谱、三移位幂和七次第三周期的
专项查新已完成。结论为“在已核一手来源中未定位直接覆盖的新完整定理”，
并已列出必须扣除的强先例与标准工具。

这不产生 `NOVELTY_PASS`、`CANDIDATE_PASS` 或长文容量 PASS。统一二项族仍是
一参数子族，不是任意 centered 多项式；大于七的 $d\equiv3\pmod4$ 问题仍未解。
旧偶周期短结果的评价保持原状态，新完整证明按新增量词单独评估，不篡改旧记录。

唯一新增工作区文件是本补充；所有旧输入、证明包、先例报告、正式项目、实验、
构建及账本均未修改。行数与 SHA256 由交付消息给出。
