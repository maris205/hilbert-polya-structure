# Paper 29 候选：固定 Jacobian 的指定周期迹坐标——有界一手查新

日期：2026-09-05。性质：候选级文献/P18 碰撞审查，不是 Route A/B 评价，不是证明验收，不授权新建论文项目。只新增本文件；不修改 P18 冻结范围。

已完整阅读本次实际作者证明 [PROOF_V1](PAPER29_FIXED_JACOBIAN_TRACE_PROOF_V1_20260905.md)，核实 SHA-256 为 8307ce9e82a8066b91c9f7a751299d32941c93e45cc9cb7df164dbae840afd1e。以下最终比较针对该版本，不只是早期口头构想。它已有完整作者侧论证；“待验收”指独立证明/价值验收尚未由本报告承担，不表示作者没有写出统一性证明。

## 结论先行

本次检索未找到与下述完整量词相同的一手定理：**每个非零固定 Jacobian、任意预定的 $d-1$ 个正整数周期，在单因子 monic-centered Hénon 族中存在对应互不相交的简单精确周期元组，其 $d-1$ 个选定迹的全系数 Jacobian 可逆。** P18 明确没有覆盖这个结论。2026 年完整谱刚性结果也不能直接推出该指定周期选择结论。

但基础方法差分须从严扣除：固定有界 Jacobian、同一高逃逸区域、所有符号序列/所有周期的轨道延拓，早已属于反可积极限的经典收缩构造；一维多项式任意周期乘子独立，乃至在同一个 $z^d$ 基点为每个周期向量选到满秩元组，也已经存在。潜在新核是**指定 primitive words 的占比矩阵证书，与对周期一致的归一化谱参数导数估计相结合**，而不是收缩法、谱刚性或“同一基点”本身。

建议分两层：逐 $b$、逐周期向量的存在性，暂评为有真实量词差分但容易成为短应用；共同参数邻域、对所有周期向量同时成立的定量版本，值得完成一次有界独立证明审计。两层都不能仅凭“未搜到同题”认定达到独立论文价值门槛。

## 1. 精确候选与不覆盖事项

令 $r=d-1$，
\[
H_{b,p}(x,y)=(p(x)+by,x),\qquad
p(x)=x^d+\sum_{j=0}^{d-2}a_jx^j,\qquad d\ge2.
\]
本记号中 $\det DH=-b$，所以辛切片为 $b=-1$，而不是 $b=1$。以下全部在复数域讨论，不附加实轨道要求。

- **C1：固定切片存在性。** 对每个 $b\in\mathbf C^*$、每个 $\mathbf n\in\mathbf Z_{>0}^{r}$，存在某个 $p$ 与标号互异、两两不交、简单的 exact $n_i$-cycles，使 $\det(\partial\rho_i/\partial a_j)\ne0$，其中 $\rho_i=\operatorname{tr}DH^{n_i}$。据此在该元组所在分量上得 dominant、generically étale。
- **C2：显式证书。** 在 $p_A(x)=A^df(x/A)$、$\varepsilon=A^{1-d}$、$f_0(z)=z^d-1$ 的反可积极限，用仅一次出现锚符号的 primitive words，以及 Vandermonde 加秩一更新，得到非零的谱系数导数行列式。
- **C3：统一强化，已有作者证明、尚待独立验收。** 对每个 $d,B$，存在只依赖 $d,B$ 的 $A_0$ 和共同小的 scaled-coefficient 邻域，使每个 $|A|>A_0$、每个 $0<|b|\le B$、每个 $f$ 在该邻域中，以及每个周期向量，都能选到 C1 所需元组。实际 V1 对 $K_{ij}=(n_i\rho_i)^{-1}\partial_{u_j}\rho_i$ 明确给出统一条目上界和 $|\det K|\ge(d-1)!/(2^d d^{d/2})$；选根排列只依赖周期向量，不依赖 $A,b,u$。

允许元组的符号排列依赖周期向量；不声称所有元组或所有 incidence 分量满秩，不声称任意给定 Hénon 映射都具此性质，不声称全局单射/重构，不声称不同周期向量共享同一有限轨道集合。

## 2. 一手碰撞矩阵

| 来源与核查位置 | 已有结果/方法 | 与候选的准确关系 |
|---|---|---|
| I. Gorbovickis, *Algebraic independence of multipliers of periodic orbits in the space of polynomial maps of one variable*, arXiv:1305.0867；ETDS 36 (2016)。已核 Theorem 1.6、Lemma 2.1、Lemma 3.1 及相关定义。 | 一维 monic-centered 多项式中，任意允许长度的正周期向量及系数子列，存在满秩乘子微分；Lemma 2.1 的全部见证点可以位于同一个 $p_0=z^d$。 | 是“指定周期乘子独立”最近的直接前身；非零 Jacobian Hénon 不在该定理中。不可把同一基点全周期作为新发现。[原文](https://arxiv.org/html/1305.0867v1) |
| I. Gorbovickis–J. Taflin, *Independence of multipliers in several variables complex dynamics*, arXiv:2411.12856v2，2025-01-08 修订的预印本；已核 Theorem 1.1、参数空间定义和相关 monodromy 结论。 | 可延拓为射影空间端同态的 regular polynomial endomorphisms，足够高周期的若干特征值独立。 | Hénon 多项式自同构不是该参数族；不能直接限制其定理到固定 $b$。也不能移植其 marked-space 不可约性。候选包含周期 1、2。[原文](https://arxiv.org/html/2411.12856v2) |
| S. Cantat–R. Dujardin, *Multiplier rigidity for complex Hénon maps*, arXiv:2603.09445v1，2026 预印本；已核 Theorems A–D、3.7、4.2、Example 4.3。 | 完整迹谱/不稳定乘子谱给有限刚性；还处理固定 multidegree、multi-Jacobian。存在统一的有限周期截断。单因子 Jacobian 不等于 $-1$ 时，完整周期 1、2 数据已有更强重构性质。 | 完整无标号谱不等于任意预定周期的 $d-1$ 个选定迹。有限谱纤维不能指定哪几个周期坐标形成满秩子矩阵。其 Jacobian $-1$ 例外对应本项目 $b=1$，**不是**辛切片 $b=-1$。[原文](https://arxiv.org/html/2603.09445v1) |
| D. Sterling–J. D. Meiss, *Computing periodic orbits using the anti-integrable limit*, Phys. Lett. A 241 (1998), 46–52；已核 §2 Theorem 1 及证明。 | 二次 Hénon 的每个双无限符号序列，在同一 $\lvert\varepsilon\rvert(1+\lvert b\rvert)<0.649839\ldots$ 区域延拓为唯一轨道；使用 $\ell^\infty$ 逆分支收缩，其阈值不依赖周期。 | C3 的统一轨道延拓机制已有。该文没有候选的任意次数全系数谱 Jacobian 非退化定理。注意论文与本项目的 $b$ 符号约定不同。[原文](https://arxiv.org/html/chao-dyn/9802014) |
| Z. Arai–Y.-C. Chen, *More on the Concept of Anti-integrability for Hénon Maps*, arXiv:2505.15346v1，2025 预印本版本；已核导论、基本缩放和主构造范围。 | 回顾固定 Jacobian 下的经典反可积极限；新研究还允许耦合参数随逃逸尺度变化，出现非零有效耦合的极限。 | 再次确认固定 $b$ 的 AI 机制不是本候选的新方法。未见其宣称指定周期元组的全系数迹坐标。外部检索显示另有期刊版本，但本次未从官方期刊页完成核实，故只按已读 arXiv 版引用。[原文](https://arxiv.org/html/2505.15346v1) |
| F. Bianchi–Y. He, *A thermodynamic path metric for complex Hénon maps*, arXiv:2606.29363v1，2026-06-28 预印本；已核导论、Theorem 1.1、§§2–4 的相关表述。 | 在双曲分量中将不稳定乘子表示为复乘法 cocycle，研究参数微分的协方差半正定型；借完整谱刚性使诱导路径距离分离点。 | 周期归一化对数乘子及其 cocycle 微分是已有框架。路径距离非退化不等于每点张量正定，更不推出任意指定 $d-1$ 个周期的微分独立。[原文](https://arxiv.org/html/2606.29363v1) |
| V. Huguin, *Moduli spaces of polynomial maps and multipliers at small cycles*, arXiv:2412.19335，2024 预印本；已核摘要和主结果定位。 | 一维多项式模空间的完整周期 1、2 乘子映射有限且双有理到像。 | 这是完整低周期谱重构，不是非零 Jacobian 的指定标号有限谱坐标；主要作为 Cantat–Dujardin 的前置比较。[摘要](https://arxiv.org/abs/2412.19335) |
| 本地 P18：*Marked Trace Coordinates and Scheme-Theoretic Ramification at the Polynomial Boundary of Generalized Hénon Maps*；已读 RQ、novelty note，复核 PDF 前三页。 | 从 $b=0$ 的 Gorbovickis 点得到总参数空间上的 trace+$-b$ 坐标，以及某个未指定非空开集 $U\subset\mathbf G_m$ 上的 fixed-$b$ 结论。 | RQ4、A3、A4 明确不覆盖每个非零 $b$ 或指定 $b=-1$。新 C1 的量词真正超出 P18；incidence、cyclic quotient、generic étaleness 转译不是新核。[冻结问题](../../papers/18-marked-henon-scalar-boundary/notes/RESEARCH_QUESTION.md) |

## 3. 哪些推论不成立

**P18 的非空开集不能替代任意切片。** 从 $J(b,a)\not\equiv0$ 或在 $b=0$ 有非零点，只能排除泛型退化；仍可能有整个特定切片被零集包含。必须在每个预定 $b$ 自己构造见证点。新证明若成立，应明确写成不同于 P18 的非零 Jacobian 构造，而不是改写 P18 的原结论。

**完整谱刚性不能选择任意周期。** 即便完整谱映射有限，特征零下也至多支持某些有限谱函数在某处给足秩；无法凭此让选中函数的周期等于外部指定的 $n_1,\ldots,n_r$，也无法得到对所有 $\mathbf n$ 一致的邻域。相反，候选的选定迹坐标也远不等于完整谱重构。

**“统一”必须说明统一对象。** 经典 AI 收缩已统一于符号序列与周期。Gorbovickis 已在一维给共同基点。C3 若有新意，统一的是“指定周期迹的完整系数微分非退化”，并需同时控制轨道、参数导数和 trace 相对不稳定乘子的修正。若只逐个有限周期向量调用有限维隐函数定理，所得阈值可依赖 $\mathbf n$，并没有证明 C3。

## 4. 已独立核对的候选代数证书

本节是对给定公式的独立代数核对，不代替周期一致的分析证明。取 $f_c(z)=z^d-1+\sum_{j=0}^{d-2}c_jz^j$，根 $\alpha_1,\ldots,\alpha_r,\alpha_d=1$。根的隐式微分给出
\[
\left.\partial_{c_j}\log f'_c(\alpha_i(c))\right|_{c=0}
=-\frac{d-1-j}{d}\alpha_i^j.
\]
令 $v_i=(1,\alpha_i,\ldots,\alpha_i^{d-2})$，$V$ 以非锚根的 $v_i$ 为行，$K=\operatorname{diag}(-(d-1-j)/d)$。单位根恒等式给
\[
v_d=-\sum_{i=1}^{r}\alpha_i v_i.
\]
当 $n_i=1$ 取单字 $i$；当 $n_i>1$ 取 $i^{n_i-1}d$。后者锚字恰出现一次，所以是 primitive；不同 $i$ 的循环字彼此不同。令 $s_i=1$（$n_i=1$）或 $s_i=n_i-1$（$n_i>1$），则归一化主项矩阵 $M$ 满足
\[
\det M
=\left(\prod_{i=1}^{r}\frac{s_i}{n_i}\right)
\det(VK)
\left(1-\sum_{n_i>1}\frac{\alpha_i}{n_i-1}\right).
\]
在非锚根的排列上平均，最后括号的平均值为
\[
1+\frac1r\sum_{n_i>1}\frac1{n_i-1}\ge1.
\]
故存在一个排列使该括号模至少为 1，且
\[
|\det M|\ge2^{-r}|\det(VK)|>0.
\]
这给出了与 $\mathbf n$ 无关的候选主项下界。根的排列只改变 Vandermonde 行列式的符号，不改变其模。全系数扰动必须保留，不能只沿单参数 $x^d-A^d$ 曲线求导。

实际 V1 已针对下列五项写出论证；独立证明审计应核验这些论证，而不是仅凭主项行列式宣告 C3：

1. 在共同 scaled-coefficient 邻域内，轨道及其系数导数的偏差对所有周期为 $O(|\varepsilon|)$。
2. 周期 Riccati 方程 $v_{k+1}=f'(z_k)+b\varepsilon^2/v_k$ 的解及参数导数有周期一致的分母下界和误差估计。
3. 对 $n^{-1}\,\partial_c\log\rho$ 而非仅 $\rho$ 本身，得到统一误差，并由 $\rho=\lambda_u+(-b)^n/\lambda_u$ 控制 trace 修正；对数只需局部分支，其微分才是实际对象。
4. 统一排除 $\det(DH^n-I)=0$，保留 exactness 和 disjointness；处理 $n=1,2$ 循环索引重合。
5. 说明 $a_0=A^d(c_0-1)$、$a_j=A^{d-j}c_j$（$j\ge1$），所以 $da_j=A^{d-j}dc_j$ 是每个 $A\ne0$ 下可逆的参数微分变换；从见证点只推出其所在分量的 generic étaleness。

上述 1–5 是证明验收任务，不是通过文献空缺自动获得的结果。V1 使用 $u$ 而非本节的 $c$ 表示同一 scaled-coefficient 扰动，Riccati 变量写作 $w_k=a_k+b\epsilon^2/w_{k-1}$，其索引由显式二维向量恒等式固定。

### 对实际 V1 的逐模块新意扣除

- §§1–2：有限个根附近的共同逆分支、sup-norm 收缩、统一轨道延拓。这是经典 AI 工具的任意次数复参数实现；不宜作为独立创新计数。
- §3：第二个周期收缩得到 Riccati 线；由 $\rho=\epsilon^{-n}\prod w_k(1+\theta)$ 导出精确因子 $(1-\theta)/(1+\theta)$，从而控制 $n^{-1}\partial_u\log\rho$。这是候选所需的具体谱微分桥梁，确实比只知轨道存在更强；构成它的收缩、Cauchy 估计和二维单值矩阵代数仍是标准工具。
- §4：指定单锚 primitive words、根排列平均和显式 $c_d$ 下界。它直接回答外部指定全部周期的选择问题，是现有检索中未找到同式的主要有限代数证书。
- §5：归一化各行是有限斜率导数向量的凸组合，故统一误差可在同一个邻域内保留行列式间隙。V1 的确在此证明同一开区域覆盖所有周期向量；不是仅声称逐向量的开性。不过这一步本身是由前两项定量估计得出的有限维扰动推论，不能再次计为一个独立大型结果。
- §6：从简单元组得到 incidence 局部系数坐标，循环商后在所在分量上得到 dominant、generically étale。这是标准代数后果，并与 P18 大量方法重合。V1 正确没有把该分量认作 P18 的标量边界分量。

因此按实际证明而非提案措辞判断：新意核心仍是“统一谱微分估计 + 指定 primitive words 的满秩证书”的组合，不能把六节依赖链拆算成六个创新。完整 V1 已足以进入独立证明审计，但长度与工具深度仍支持对长论文价值保持保留。

## 5. 新意、价值与建议定位

| 主张 | 新意暂评 | 最接近前身 | 本次建议 |
|---|---|---|---|
| C1：每个固定非零 $b$ 的任意指定周期 trace 满秩见证 | 中等；确有 P18 量词差分 | Gorbovickis + P18 + 经典 AI | 若没有 C3，优先作为短应用/续篇引理评估，不宜用重复 incidence 包装拉成长论文。 |
| C2：primitive words + occupancy/Vandermonde 秩一证书 | 中等，具体证书未检得同式 | 指定周期导数独立的既有问题与 AI 符号构造 | 是应交给独立审查的真正有限代数步骤；不能称 AI 方法本身新颖。 |
| C3：共同高逃逸参数区上，对任意周期向量的归一化谱 Jacobian 一致非退化 | 中等偏上，条件性 | 经典统一轨道收缩 + 既有周期 cocycle 微分框架 | V1 已确实写成定理并给出作者证明；可以继续一次有界独立证明审计，不能自动换成价值 PASS。 |

按技能要求提供主观尺度：C1 单独约 **5.5/10**；若 C3 的所有量词与常数依赖被独立证明核实，整体新意可暂估 **6.5–7/10**。这不是数学真值，也不是正式 value 分数；本查新**不给 8/10 或独立长论文 PASS**。建议为 **PROCEED WITH CAUTION，仅限候选的有界证明/价值审计**。

适当定位是：“在每个非零固定 Jacobian 切片，用高逃逸构造给出指定周期迹坐标的统一定量见证。”不适当定位包括“首次以乘子作为动力系统坐标”“首次对 Hénon 用反可积极限”“完整谱刚性的新证明”“全部 marked components 上的重构定理”。

如果最终统一估计只是短篇标准扰动引理，剩余核心可能仍只有一个漂亮的占比行列式；这时独立 22–24 页文章的价值风险仍高，应由后续价值审查明说，不能拿 P18 已有的有限自由、Fitting、循环商等材料补足页数。

## 6. 检索范围与可追溯性

采用 `research-lit` 与 `novelty-check`；可用来源为本地 P18 与公开一手原文。未配置 Zotero、Obsidian 或技能指定的交叉模型 MCP；因此没有伪造 cross-model review。未新增下载 PDF；arXiv 工具脚本不可用，改用 arXiv 摘要及公开 HTML。没有投稿、联系作者、外部存储写入或付费操作。

针对 C1 的主要查询包括 `Henon fixed Jacobian multipliers algebraic independence`、`Hénon maps multipliers local coordinates fixed determinant`、`Henon periodic traces prescribed periods independent Jacobian`，并分别加 2024–2026 或最近六个月限制。针对 C2 查询 `Henon antiintegrable limit multipliers independent traces`、`generalized Henon maps antiintegrable limit arbitrary degree periodic orbits multipliers`、`anti-integrable spectral Jacobian`。针对 C3 查询 `Hénon multipliers uniform independence`、`Hénon multipliers escape locus`、`anti-integrable derivatives multipliers`、`polynomial multipliers coordinates shift locus`、`Hénon Riccati multipliers`、`multiplier coordinates escape polynomial`，以及带 2026-03-05 至 2026-09-05 窗口的 Hénon multiplier/trace independence 查询。

最近六个月的直接相关命中主要是 Cantat–Dujardin（arXiv 首次提交 2026-03-10）和 Bianchi–He（2026-06-28）。另核 Arai–Chen 2025 与 Gorbovickis–Taflin 的最新可见版本。检索中出现的大量 Hénon–Heiles 迹公式、三维 Hénon-like 分岔、数值 Lyapunov 指标不等于本问题，未用于支持任何结论。机器学习会议名录与本纯数学问题无关，不为满足技能模板而混入。

阅读层级已在表内逐项注明：除标明的 theorem/section 之外，不声称对每篇长文完成逐行证明审查。未检得精确重合只是有界公开检索结果，不能保证绝对首创、未公开手稿不存在或所有其他命名下的文献都被穷尽。
