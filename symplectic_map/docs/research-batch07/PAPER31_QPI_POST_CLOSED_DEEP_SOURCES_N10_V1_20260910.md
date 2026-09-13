# Paper31 post-closed：N10 深查新来源账本 V1

项目日期：2026-09-10；本轮实际检索：2026-09-09 UTC。
对象：Phase A §5 的 N10-C1/C2/C3；模式：`novelty-check` Phase B，来源核查，不做数学诊断、证明、实例计算或评分。
来源席已接触旧 I08 及 N07–N10 首筛；不是 fresh blind、正式独立票或跨模型验证。

## 1. 输入、所有权与阅读边界

本人完整读取 [Phase A 主张件][PA]（92 行，SHA256 `8a8b9ba44f5e98e9ea6c31820c299dc69b81fe76b4f0ff8f67850f09a048a0a3`），只执行其中 N10。
消费本人已完成的 [N07–N10 首筛][QF]（180 行，SHA256 `b5b3129c0b46efa96cb7fdce7850f26309045812c987d52f839757ca2897db9c`）及其明确记录的读深，不重复扫旧构建树。
唯一新写文件是本件；未改旧接受件、失败件、索引、锁或项目正文，未建立 Paper31 项目。
本轮新来源阅读均由本席完成；下文 `PARTIAL` 表示仅指定范围读过，不把检索摘要、目录或他席读深冒充本文全文阅读。

固定原单位时间圆分设置 `q=s_a, r=mp^a, O_a`、实际 `z∈U(O_a)`、`c=I_r(z)` 和原回返 `Ψ=F_{s^{r-1}t}∘⋯∘F_t`。
只在原 Jacobian 好约化、实际指定 `P_c` 及原谱比较已建立的范围，才谈 `E_j=ker(E(O_a)→E(O_a/π^j))`。
本件既没有验证这些前提，也没有选定具体整状态；“原态点已知”不等于“所有谱比较或有限环作用已知”。

## 2. 逐项检索目标

| 主张 | 必须保持的原问题 | 不计入剩余贡献的内容 |
|---|---|---|
| N10-C1 | 原完整状态模型中，原 `Ψ` 及逆映射在选定整轨道／同余域的延拓；`L_N(z)` 是原状态模 `π^N` 的最小正周期 | 域上双有理共轭、特征 p 的完整状态算法、AGR、依点选择迭代次数；这些不能各自代签所有有限环上的可逆作用 |
| N10-C2 | 同一原谱映射与逆映射，双向比较原状态同余和 Jacobian 差的 `E_j` 过滤；明示深盘阈值、状态依赖与适用图 | 通用局部解析逆函数／小球估值定理；不得先设只需一个标量 `λ(z)` |
| N10-C3 | 固定原时间、已标记剩余能级数据后，检验原 `v_π 𝔠(p^{-a}d_state I_r)(z)` 是否足以决定 C2 信息及 `P_c` 同余阶到 `L_N` 的比较 | 形式群 `[p]` 估值、EDS 周期、已接受平移／有限域清单；不同椭圆曲线的普通／超奇异标签不是原同数据反例 |

未搜索“证明黎曼猜想”等外围主题；不以无关 ML 会议目录充当数学覆盖。
下文“未取得直接包含证据”只界定已读文献的结论，不是新颖性判决。

## 3. 本轮实际新查询

以下 24 条均在本轮实际执行；旧首筛查询不计入此表。
C1 有 7 条，C2 有 8 条，C3 有 9 条，分别超过每主张至少三种新查询的门槛。
同批 web 搜索可能合并返回结果，结果摘要按实际返回的相关来源归纳；不把其他查询返回的空缺解释成数据库无文献。

| ID | 实际查询串 | 返回情况／用途 |
|---|---|---|
| C1-Q1 | `"Painlevé" "finite rings" reduction` | 进入 Kanki–Mada–Tokihiro 的有限域／AGR 线索；没有由标题命中得到原有限环作用定理 |
| C1-Q2 | `"space of initial conditions" "good reduction" arxiv` | 核初值空间与 good／almost good reduction 的区别 |
| C1-Q3 | `"q-Painlevé" "integral" model 2024 2025 2026` | 2024–2026 时间段补查；部分命中是积分表示而非整数模型 |
| C1-Q4 | `site:arxiv.org "Painlevé" "finite fields"`；`recency=184` | 返回含旧论文；不能把抓取日期当成近六个月发表日期 |
| C1-Q5 | `site:scholar.google.com "Painlevé" "reduction" "finite"` | 公开入口补查；未取得可用于 C1 的新 primary 正文 |
| C1-Q6 | `site:semanticscholar.org "Painlevé" "reduction" "finite"` | 返回含 PDE 对称约化的异题 PDF；未作为 C1 文献证据 |
| C1-Q7 | `site:arxiv.org "q-Painlevé" after:2026-03-10 before:2026-09-11` | 明示最近六个月日期窗；本轮未核得窗内直接处理原有限环作用的新文献 |
| C2-Q1 | `"p-adic" "analytic conjugacy" "elliptic"` | 通用局部解析比较线索；未发现可直接代签原谱映射的正文 |
| C2-Q2 | `"ultrametric" "inverse function theorem" "balls" Glöckner` | 命中小球像／完整导数矩阵的强通用先例 G |
| C2-Q3 | `"p-adic" "Jacobian property" 2024 2025 2026` | 年份补查；最新近邻包括不同系统的 Hénon-like 研究 |
| C2-Q4 | `site:arxiv.org "p-adic" "conjugacy"`；`recency=184` | 返回旧或异题工作，不以时间过滤器证明新文献覆盖完备 |
| C2-Q5 | `site:scholar.google.com "ultrametric" "inverse function theorem"` | 公开入口补查；未取得新增可用 primary |
| C2-Q6 | `site:semanticscholar.org "ultrametric" "inverse function theorem"` | 同上，不用聚合条目代替定理正文 |
| C2-Q7 | `"Glockner" "Lectures on Lie groups over local fields" arxiv` | 从线索定位作者 arXiv 版本 G，随后读取实际命题 |
| C2-Q8 | `site:arxiv.org "p-adic" "conjugacy" after:2026-03-10 before:2026-09-11` | 最近六个月补查；未核得直接原谱双向过滤先例 |
| C3-Q1 | `"formal group" "valuation" "division polynomials" Stange` | 命中 S，转读期刊原文，不采用 ResearchGate 年份 |
| C3-Q2 | `"p-adic" "period lifting" "critical" 2024 2025 2026` | 年份／临界提升补查；未取得原临界理想决定能力定理 |
| C3-Q3 | `site:arxiv.org "formal group" "dynamics"`；`recency=184` | 含旧 Hecke dynamics 等异题结果；不是原 q-PI 包含证据 |
| C3-Q4 | `"elliptic divisibility" "period" "prime powers"` | 进入 EDS 模素数幂周期线，结合已有 B 的明确读深 |
| C3-Q5 | `site:scholar.google.com "formal group" "division polynomials" "valuations"` | 公开入口补查；未取得新增可用 primary |
| C3-Q6 | `site:semanticscholar.org "formal group" "division polynomials" "valuations"` | 同上；检索不足不转成未发表判断 |
| C3-Q7 | `"Good reduction of periodic points" Hutz` | 定位 H 并读取模型假设／primitive period 定理 |
| C3-Q8 | `site:arxiv.org "elliptic" "period" "valuation" after:2026-03-10 before:2026-09-11` | 最近六个月补查，不将旧文的近期抓取时间算作新工作 |
| C3-Q9 | `site:arxiv.org "p-adic" "periodic points" 2024 2025 2026` | 新命中 PT（2026-05-06）及 2025 多项式周期点工作；选择与有限环提升最接近的 PT 深读 |

近 2024–2026 的直接原系统锚点是 JR（2025 初稿、2026-01-16 v2）；它不在 2026-03-10 至 2026-09-10 的最近六个月窗内。
最近六个月确证命中 PT（arXiv 2026-05-06）和 BCR（期刊 2026-09-08）；二者的科学对象不同，不能因此宣称 C1–C3 已有全覆盖。
三平台口径是“web 覆盖 arXiv／Scholar／Semantic Scholar 公开入口”；没有 Scholar 登录后全库、Semantic Scholar API、付费库或全部新近 arXiv 逐日目录的完整性保证。

## 4. Primary 来源、版本与实际读深

### JR：原 q-PI 的有限域完整状态模型

Nalini Joshi、Pieter Roffelsen，*Arithmetic dynamics of a discrete Painlevé equation*；[arXiv 元数据](https://arxiv.org/abs/2508.18578)，[v2 正文](https://arxiv.org/html/2508.18578v2)，[v2 PDF](https://arxiv.org/pdf/2508.18578v2)。v1：2025-08-26；v2：2026-01-16。
本轮 `PARTIAL`：abstract、§1 全部正文、§2.1、§2.2 的 Definition 2.2／Algorithm 1、§3.1 Theorem 3.1 与 Remarks 3.2–3.5；PDF 首两页交叉核版本与主张措辞。
已包含：同一原方程的有限域初值图、`X_{t,s}→X_{st,s}` 同构陈述、精确状态编码；`I_r` 位于圆分整数系数 Laurent 环且在函数域中不变。上述分别不是所有 `O_a/π^N` 上可逆作用或原状态到 Jacobian 的整双向比较。
版本警示：本次 abs 页摘要措辞较强，但实际 v2 HTML／PDF 的 §1 仍称 Hasse／genus 内容为 Conjectures；本账本依实际正文编号，不依据 abs 文案提升定理等级。

### K：初值空间与 AGR 的定义边界

Masataka Kanki、Jun Mada、Tetsuji Tokihiro，*The space of initial conditions and the property of an almost good reduction in discrete Painleve II equations over finite fields*；[v4 原文](https://arxiv.org/pdf/1209.0223v4)，[元数据](https://arxiv.org/abs/1209.0223)。v4：2013-09-28；期刊 J. Nonlin. Math. Phys. 20:sup 1 (2013), 101–109，DOI `10.1080/14029251.2013.862437`。
本轮 `PARTIAL`：abstract、§1、§2 进入初值空间的设置及 Theorem 2.1 前后、§3 Definition 3.1 与 Proposition 3.1 的范围；未读全篇证明。
已包含的是 dPII 的有限域扩张定义域、qPII／相关映射的 AGR。Definition 3.1 允许迭代次数依初值和时刻而变，且结论是模 p 的比较；它不是本轮原 q-PI 在全部有限商上的同一个可逆作用。

### G：完整导数矩阵控制的超度量局部逆函数定理

Helge Glöckner，*Lectures on Lie groups over local fields*；[arXiv 元数据](https://arxiv.org/abs/0804.2234)，[v5 原文](https://arxiv.org/pdf/0804.2234v5)。v1：2008-04-14；实际所读 v5：2016-12-28。
本轮 `PARTIAL`：abstract、Introduction；§1 解析流形／Lie 群定义附近；完整读取 Props 1.11–1.13 及 Lemma 1.14／Remark 1.15 的陈述和所附解释、Prop 1.13 证明。未把讲义引用的证明文献冒充另已全文读过。
Prop 1.11 的输入是完备超度量域上的解析 `f:U⊂K^n→K^n` 及可逆 `f'(x)`；缩小后，子球像恰为 `f(y)+f'(x)B_s(0)`，限制为解析微分同胚。Prop 1.12 有局部参数统一版本；max norm 下线性等距群是 `GL_n(O)`。这是 C2 必须扣除的矩阵级通用机制，不预设单标量损失。

### HM：mixed-characteristic 的 Jacobian property

Raf Cluckers、Immanuel Halupczok、Silvain Rideau-Kikuchi、Floris Vermeulen，*Hensel minimality II: Mixed characteristic and a diophantine application*；[v2 原文](https://arxiv.org/html/2104.09475v2)，2023-09-07。由主控提供线索，本席重新读取下列范围。
本轮 `PARTIAL`：abstract、§1；Th 3.1.2、Cors 3.1.3–3.1.4 的定义／陈述与紧邻证明范围；§3.3 Th 3.3.6、Def 3.3.7、Th 3.3.8 及后附证明范围。没有通读 §2、全部 cell-decomposition 证明或 Part I。
在 1-h-minimal 假设下，一元可定义函数经合适划分有精确 valuative Jacobian property；高维 scalar-valued 函数另有 sup-Jac preparation。高维梯度误差界本身不提供向量值双射、逆谱图或原同余关系；故它加强通用分析扣除，而非替原谱桥验收。

### S：分歧域与例外项已经进入形式群／EDS 估值理论

Katherine E. Stange，*Integral Points on Elliptic Curves and Explicit Valuations of Division Polynomials*；[期刊原文](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/41542AA1CA680CB762422184B9DAE66C/S0008414X00004466a.pdf/integral_points_on_elliptic_curves_and_explicit_valuations_of_division_polynomials.pdf)，Canad. J. Math. 68(5) (2016), 1120–1158，DOI `10.4153/CJM-2015-005-0`；[arXiv 元数据](https://arxiv.org/abs/1108.3051) 的 v4 为 2014-12-29，本文定理编号取期刊版。
本轮 `PARTIAL`：abstract、Introduction 开头 pp.1120–1122 的已返回范围；§3 Theorem 3.3、§4 全部；§5 Lemma 5.1／Remark 5.2／Definition 5.3／Prop 5.4 与 Lemma 证明；§6 Theorem 6.1、Cors 6.2–6.4、Remark 6.5 及紧邻证明。
§4 允许有限 `K/Q_p`；Lemma 5.1 在一参数形式群中给乘法估值，保留分歧阈值和等值竞争例外项。最简 `v(W_n)=v(W_{n_P})+v(n/n_P)` 有额外条件；Remark 6.5 特别指出遗漏最小模型／深度假设的风险。这里的形式参数与系数不是原临界理想数据的已证函数。

### H：已有 K-有理周期点的 good-reduction 周期界

Benjamin Hutz，*Good reduction of periodic points on projective varieties*；[v3 原文](https://arxiv.org/pdf/0801.3645v3)，[元数据](https://arxiv.org/abs/0801.3645)，实际 v3：2010-03-12；期刊 Illinois J. Math. 53(4) (2009), 1109–1126。
本轮 `PARTIAL`：abstract、§1（含 Theorems 1–2、4）、§2 Definitions 5–6、Theorem 7／Corollary 9 及所附证明；未全文重证后续周期界。
在光滑射影整模型、整态射和已存在周期点假设下，primitive period 由约化周期、余切作用阶及 p 幂部分控制。其目标是 K-有理有限周期；不等同于非挠平移点在每个有限商中的周期序列，不能直接把该界当作 N10 的 `L_N` 公式。

### B：首筛已核的 Néron 过滤／EDS 先例（消费，不计新读）

Bhakta、Loughran、Rydin Myerson、Nakahara，*The elliptic sieve and Brauer groups*；[期刊原文](https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/plms.12520)，Proc. Lond. Math. Soc. 126(6) (2023), 1884–1922，2023-05-11。
首筛已读：metadata、完整 §2 Definitions 2.1–2.2／Lemmas 2.3–2.4 及证明／Remark 2.5；§3.3 仅周期性开头与 Prop 3.7 上下文。本轮不冒称重新 FULL。
已知过滤、分母估值和周期机制必须扣除；该处 `Q_p` 范围不能不加检查地替换成本题可能分歧的 `O_a`，也不提供原谱坐标整桥。S 是本轮针对这一范围差的加强来源。

### PT：最近六个月 arXiv 的有限环提升近邻

Chatchawan Panraksa、Aram Tangboonduangjit，*Fixed-point lifting and ghost periodic points for Chebyshev polynomials modulo odd prime powers*；[元数据](https://arxiv.org/abs/2605.04417)，[v1 原文](https://arxiv.org/html/2605.04417v1)，2026-05-06；截至所见版本为 v1。
本轮 `PARTIAL`：abstract、§1 的贡献／比较／假设表及组织；Prop 7.1 及证明；§11 的 Lemmas 11.6–11.8、Theorem 11.9 完整陈述和证明开头，未通读全部论证。
Th 11.9 在 `p≥5, p∤n` 的 Chebyshev 系统，以源点阶的 `cord` 塔组织有限环提升周期及重数；不是原 q-PI 的 Jacobian 平移／临界理想问题。它说明新近“有限环周期提升”文献确实存在，但不同商状态关系不能搬到 N10；没有在本件用其证明原对象的正负结论。

### BCR：最近六个月期刊近邻，按对象排除

Jéfferson L. R. Bastos、Danilo Caprio、Oyran Raizzaro，*Backward Julia Sets for a Class of p-adic Hénon-like Maps*；[期刊全文](https://link.springer.com/article/10.1007/s00025-026-02729-x)，Results Math. 81, 172 (2026)，DOI `10.1007/s00025-026-02729-x`；正式发表 2026-09-08。
本轮 `PARTIAL`：metadata、abstract、Introduction 的目标与模型范围；未读完整主定理证明。对象是 `f(x,y)=(xy+c,x)` 的 backward filled Julia set、有界性及 Haar 测度，不是原 q-PI 谱映射双向同余；不算 C2 的直接重合或新方法证明。

## 5. 已知包含与仍待原对象核验的逐项映射

| 主张 | 本轮核实应扣除的先例 | 文献尚未替本题完成的输入／输出 |
|---|---|---|
| C1 | JR 的原有限域状态空间／整数系数不变量；K 的初值空间与 AGR；H 的 good-reduction 整态射框架 | 同一原完整图在 `O_a` 上的所需延拓；原 `Ψ` 与逆映射共同稳定的轨道／同余邻域；与原状态等价关系一致的所有模 `π^N` 作用与最小正周期 |
| C2 | G 的矩阵级局部球像与解析逆；HM 的一元精确 Jacobian property／高维梯度准备；B 的现成群过滤 | 该原谱映射及逆映射实际存在于哪些整图；其局部导数与误差条件；原坐标同余和 `E_j` 双向阈值。尚未判定它是否仅为 G 的短应用 |
| C3 | S 的一般形式群乘法估值及分歧例外，B 的过滤／EDS 机制；H 的周期界只能按其对象使用；PT 是别系统的提升塔 | 候选原临界阶是否恢复 C2 所需信息及实际 `P_c` 余数阶。文献使用更多参数不构成原同数据不足的证明；必须在原锁定数据下另核正面决定关系或真实同数据反例 |

这一表是适用性差额，不是三个已获批创新点。
尤其 C2 的核心风险比“找到一个局部双向界”更强：G 已提供一般解析可逆坐标变换的完整球像结构；若原问题只剩验证单位换元并引用该定理，不应包装成长篇独立结果。
C3 也不能靠重写 S 的递推、增加“临界”术语，或并列两种形式群类型形成原不可决定性结论。
C1 与 C2 的前提不成立时，不能先在 Jacobian 上定义周期再将其称为原 `L_N`。

## 6. 访问与覆盖限制

本轮实际技术来源最终使用 arXiv 原文、Cambridge 期刊原文、Springer 原文；ResearchGate、CiteSeer／Semantic 聚合结果只作定位线索，不承担定理证据。
既有 403／429 不重试或绕过；没有获取登录凭据、付费资源或镜像规避访问限制。
本轮 JR PDF 的 web 文本含大量图形字元，截图第 3 页返回 internal error；其已成功开放的原 PDF 经只读 `curl | pdftotext` 检查首两页，未保存下载文件，未把图像解析失败称为全文读完。
Scholar／Semantic 的站点查询没有提供可用新增正文，不以此宣称两库完备；arXiv 的 recency 结果混有旧文，已用实际版本日期区分。
HM 的主控线索由本席打开 arXiv 复读；主控已记录的其他端点失败没有在本件重新测试，也没有继承未读证明。
未继续深读 2025 的一般多项式周期点计数、Hecke 动力学、PDE 相似约化及异题 integral representation；这些只是定位层命中，不进入包含／排除证据。

## 7. 来源阶段终态

N10-C1：**原有限环作用适用性未核**。已知原有限域模型很接近，但不能直接升级到所有有限环的原可逆回返。
N10-C2：**通用局部过滤机制已核，原谱桥适用性未核**。G 是必须正面处理的最强标准机制碰撞；不预设单标量，也不预判原桥长短。
N10-C3：**通用估值机制已核，原临界数据决定能力未核**。没有找到直接解决原固定数据充分／不足问题的已读来源，也没有制造原反例。

本轮交付仅支持下一阶段独立批评时准确扣除上述先例；没有 KEEP／STOP 重评分、选题排名或进入数学诊断的新增授权。
后续若另获诊断授权，仍须先固定真实原状态与完整图范围；不得把本件的来源缺口写成正定理、负定理或 pilot 成功。
保持 Papers27–30 接受状态、Batch07 为 4/5、P31 正文 22–30 页与完整证明／正式独立四门等要求不变。

[PA]: PAPER31_QPI_POST_CLOSED_SURVIVOR_CLAIMS_PHASE_A_V1_20260910.md
[QF]: PAPER31_QPI_POST_CLOSED_QUICK_FILTER_N07_N10_V1_20260910.md
