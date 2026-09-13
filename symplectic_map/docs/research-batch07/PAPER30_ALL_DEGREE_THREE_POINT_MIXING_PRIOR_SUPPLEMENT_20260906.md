# 全次数、全系数 Hénon 三点同步混合：有界先例增量补充

日期：2026-09-06。状态：`BOUNDED_PRIMARY_PRIOR_SUPPLEMENT`。
仅对同一三点问题的新加强做增量查新；实际执行者为 secondary xhigh 代理，
没有调用 GPT-5.4 MCP 或人类评审。本报告不是证明审查，不打候选分、不估容量。

基线为冻结的 [三点先例报告](PAPER30_HENON_THREE_POINT_MIXING_PRIOR_PROBE_20260906.md)。
本轮不改该文件，也不重新完整审查其中未变来源。

## 1. 结论先行

未找到直接覆盖下述完整合同的定理：对每个固定 `d≥2`，两个指定形式的 Hénon
生成元在所有 `p≥16d²` 素数及所有次数恰为 d 的 monic 多项式上，三点同词作用
均有只依赖 d 的统一正谱隙。这个未命中只有有限检索意义，不是“世界首次”或 PASS。

但新增的方法扣除很明确：

- 平移交换子给出有限差分、反复降次生成剪切，是已出现于多项式自同构群研究的
  明确技术，不应宣称为新原理。Edo–Lewis 和 Bardakov–Neshchadim–Sosnovsky
  的原文提供直接公式和降次论证。
- 有限域上按次数统一、与低阶系数无关的指数和界是标准强工具；He 的非线性
  Markov 链定理还直接给出对有界次数有理置换统一的混合估计，但速率和状态空间
  不同，不覆盖本题。
- 2026-08-01 的 Becker–Breuillard 新预印本已经实现旧报告所提的线性群续作
  方向。它仍允许稀薄异常素数，并非本题二维非线性三点谱隙的直接先例。

可保留的具体差异是：在两个指定 Hénon 动作及其逆中，统一于全部系数实现
只依赖 d 的短词仿射比较，并对该系统的面积／共线层得到系数统一的轨道间混合，
最后给出完整三点合同。这些步骤是否已被作者证明，本报告不作判断。

## 2. 新比较合同与旧问题的真实差别

令 `P(x)=x^d+a_{d-1}x^{d-1}+...+a_0∈F_p[x]`，并令
`H_{P,j}(x,y)=(P(x)+j-y,x)`，`j=0,1`。在
`X_p=Conf_3(F_p²)` 上逐点同时作用，采用同一规范

\[
\mathsf P_{p,P}=\tfrac12I+\tfrac18\sum_{j=0}^1
\bigl(\rho_3(H_{P,j})+\rho_3(H_{P,j}^{-1})\bigr).
\]

输入目标是：对每个整数 `d≥2`，存在 `δ_d>0`，使对每个素数 `p≥16d²`、
每个 monic 且次数恰为 d 的 P，都有 `gap(𝖯_{p,P})≥δ_d`。
这里允许全部 d 个低阶系数随 p 任意变化；中心化后剩 d−1 个自由系数。
`δ_d` 可以依赖 d，不声称对 d 也有统一正下界。

这比“先固定一个整数多项式，再对它的模素数约化证明扩张”更强：后者可能把
系数或高度依赖藏进谱隙常数及异常素数集合。随机选择 P 或“绝大多数 P”的结论
也不能覆盖这个全系数合同。三点同步并非三份独立随机词。

主控提供的新机制包括：中心化后反复有限差分提取
`S_{Δ^{d-1}P}=(x+d!y+c_d,y)`，`c_d=d!(d-1)/2`；非中心化情形通过对角
平移 `s=-a_{d-1}/d` 共轭，保留两个生成元之间的 j 差。面积增量的输入公式为

\[
R_{P,u,v}(x)=v(P(x+u)-P(x))-u(P(x+v)-P(x)).
\]

主控拟利用其在 `uv(u-v)≠0` 时的次数及首项，得到 Fourier、最大原子和共线
逃离估计；二次另用原 Jacobi 和。以上连同 `d=1` 的面积障碍均为比较输入，
不是本报告新做的代数验证、Weil 假设核验或商链谱隙证明。

## 3. 有限差分生成：直接方法先例

### 3.1 Edo–Lewis：明确的降次技术

Eric Edo、Drew Lewis，*Co-tame polynomial automorphisms*，
International Journal of Algebra and Computation 29(5) (2019), 803–825，
DOI [10.1142/S0218196719500292](https://doi.org/10.1142/S0218196719500292)。
直接在线读取 [作者稿](https://arxiv.org/pdf/1705.01120) 引言、Definition 2、
Lemma 4 和 Theorem 7 的证明；期刊信息交叉核对作者公开 CV。

Definition 2 定义平移产生的有限偏差分；Lemma 4 给出降一次数。
Theorem 7 重证 Bodnarchuk 2002 的三角自同构结果，其证明直接把平移交换子
写成含 `-ΔP` 的剪切，并对 P 的次数反复下降。

分类：`DIRECT_METHOD_PRIOR, NOT_SPECTRAL_THEOREM`。
不能把“取交换子消去最高次，继续降次”包装成新机制。原文全局设置为特征零，
co-tame 结论在 `n≥3`；不能把该主定理直接改成二维有限域结论。
原文也未给本题两个 Hénon 生成元的全系数统一谱隙。

### 3.2 Bardakov–Neshchadim–Sosnovsky：直接的交换子公式

Valeriy G. Bardakov、Mikhail V. Neshchadim、Yury V. Sosnovsky，
*Groups of triangular automorphisms of a free associative algebra and a polynomial
algebra*，Journal of Algebra 362 (2012), 201–220，
DOI [10.1016/j.jalgebra.2011.03.038](https://doi.org/10.1016/j.jalgebra.2011.03.038)。
直接在线读取 [作者稿](https://arxiv.org/pdf/1007.2711) 引言、Lemma 2 及
Theorem 2 的证明。

Lemma 2 讨论差分方程 `g(...,x_j,...)=f(...,x_j+h,...)-f(...,x_j,...)`；
Theorem 2 的证明把这种差直接实现为初等自同构交换子。
分类同上。原文设置为特征零的整个单位三角群，不是当前固定有限生成集的扩张。

对于主控的加强，中心化后低阶项被高阶差分消去、monic 首项留下阶乘，是这类
经典差分代数的具体运用。尚未找到文献已经把主控给出的两个 Hénon 词、
固定 `d!` 剪切以及全系数的谱比较结论连成与本题相同的定理。
这里的“尚未找到”不能升级为对这个词构造单独授予新颖性。

### 3.3 Maubach–Willems：有限域生成／模拟不等于统一词长

Stefan Maubach、Roel Willems，*Polynomial automorphisms over finite fields:
Mimicking tame maps by the Derksen group*，Serdica Mathematical Journal 37 (2011),
305–322。[正式 PDF 的摘要](https://www.math.bas.bg/serdica/2011/2011-305-322.pdf)
可由索引读取，后续在线取全文超时；改读题名稍长的
[作者预印本](https://arxiv.org/pdf/0912.3387) 引言、Definition 2.3、Theorem 5.1
及相关构造设置，不混用两个版本的定理编号。

作者预印本 Theorem 5.1 在 `n≥3` 给出 Derksen 子群和 tame 群在各有限扩域上的
置换像相同；该 Derksen 生成集中加入特定非线性映射，其次数依赖特征。
分类：`GENERATION_PRIOR_ONLY`。它不是对任意 P 的二维两元组扩张定理；
在有限集合上可以模拟某个置换，也不提供独立于 p 的原生成元词长。

## 4. 全系数的非线性混合与 Weil 工具

### Jimmy He，2022

*Markov chains on finite fields with deterministic jumps*，Electronic Journal of
Probability 27 (2022), paper 28，DOI [10.1214/22-EJP757](https://doi.org/10.1214/22-EJP757)。
直接读取 [作者 v3](https://arxiv.org/pdf/2010.10668v3) 引言、Theorem 1.2、
Remarks 1.3–1.6 及 Lemma 3.1。

Theorem 1.2 对所有有界次数非线性有理置换 `f∈B(p,d)`，研究 lazy 的
`x↦f(x)±γ` 链，给出形如 `exp(-C(ε,d)n/p^{1+ε})` 的总变差上界。
常数只依赖 ε、d，而不是各个系数。原文 Remark 1.4 还允许任意两点噪声支撑。

分类：`UNIFORM_COEFFICIENT_MIXING_PRIOR, DIFFERENT_RATE_AND_ACTION`。
它说明“有界次数、系数统一的非线性有限域混合”这个广义表述已有实质定理；
但底层是单点 `F_p`，要求 f 为有理置换，速率不是统一常数谱隙，也不是本题
始终可逆的二阶 Hénon 同步三点作用。不能把单变量 P 非置换当成本题的障碍。

Lemma 3.1 及其应用还明确把 Weil 型指数和常数取为只依赖次数。
“首项非零、次数受控，因此完全指数和统一于低阶系数”应扣作标准工具。
主控所给特殊余核的首项、例外 `u,v` 质量、共线层转移及商链拼接，仍须作者
具体证明，不能由通用 Weil 界自动授予。Weil 的历史来源为
[*On Some Exponential Sums*, PNAS 34 (1948), 204–207](https://pmc.ncbi.nlm.nih.gov/articles/PMC1079093/)；
本次只成功读取其出版元数据，PDF 遇验证页后停止，没有冒称全文读取。

### Tao：全次数集合扩张不是当前谱隙

Terence Tao，*Expanding polynomials over finite fields of large characteristic, and
a regularity lemma for definable sets*，[作者摘要／v4 记录](https://arxiv.org/abs/1211.2894)，
2012 首投、2013 v4。本次仅核查作者摘要。
该文按有界次数研究二维多项式像集的扩张及加法／乘法结构例外。
分类：`DIFFERENT_EXPANSION_NOTION`。不能把其集合大小结论读作四动作的
三点 Markov 算子谱隙；即使借其估计，也仍需明确的转移核比较。

## 5. 必须更新的 2026 年新文

Oren Becker、Emmanuel Breuillard，*Uniform expansion in finite groups of Lie type*，
[arXiv:2608.00755v1](https://arxiv.org/pdf/2608.00755v1)，2026-08-01，预印本。
直接在线读取引言、Theorems 1.1/1.2 及其后说明。

Theorem 1.1 给出有界秩、有限扩域次数受控的有限单 Lie 型群的全生成集扩张，
但可以排除一个稀薄素数集合；Theorem 1.2 则把潜在坏生成对控制到很少的
共轭类。作者明确说明其方法尚不能排除所有这些异常。

分类：`NEW_STRONG_LINEAR_PRIOR, NOT_DIRECT_COVER`。
旧三点报告引用 2512.15364 时所说的“续作方向”，现在已有这篇实际续作，
故不能在新稿中继续写成尚无该方向结果。这个时效性更新只记在本补充，旧稿冻结。

该文并未给出当前非线性置换作用的有界秩线性模型；全生成集量词也不能消除
它保留的异常素数。故不能据此直接覆盖所有 `p≥16d²`、所有 monic P 的目标。
对主控已经抽取到的固定仿射剪切，旧报告的 Bourgain–Gamburd 与
Lindenstrauss–Varjú 仍是强工具；本轮没有重读它们。

## 6. 与冻结报告的最小差异台账

| 比较对象 | 冻结报告中的归属沿用／本轮增量 |
| --- | --- |
| Caprace–Kassabov 2023 | 显式多项式交错群扩张强先例沿用；变成任意 d、任意系数仍未产生二维指定生成集的统一词长桥，本轮不重读 |
| Cassidy 多元组定理 | 随机置换生成元的量词差异不变；本轮不重读 |
| 仿射扩张与通用 Markov 分解 | 标准强工具归属不变；本轮不重读 |
| 有限差分生成 | 本轮新增直接一手方法先例，必须扣除原理性新颖性 |
| 全系数非线性混合 | 本轮新增 He 的统一有界次数定理，但速率、维数及同步作用不同 |
| Becker–Breuillard | 本轮发现 2608.00755 实际续作；更新时效性，不改原报告 |

最稳妥的潜在定位是“固定次数 Hénon 族的系数一致三点扩张”，而不是
“新有限差分方法”“首次非线性扩张”或“任意多项式置换的全群 Cayley 扩张”。
这只是查新后的论题边界，不是推荐进入写作或科研验收决定。

## 7. 有界检索与限制

完整读取并使用 `research-lit` 与 `novelty-check`。按三个新增断言分别换用
至少三组表述：`arbitrary/monic polynomial + spectral gap`、
`coefficients + Schreier/nonlinear/finite-field mixing`；
`finite differences + polynomial automorphisms`、`translations + commutator + degree`、
`co-tame + degree reduction`；以及 `triangle areas + exponential sums`、
`polynomial + orbit + Markov + Weil`、`polynomial + uniform expansion + coefficients`。
另用 Hénon/Henon、Feistel 等别名，并加入 2024–2026 和最近 180 天检索。

外部结论只依赖上述一手论文或作者资料；第三方搜索结果仅用于定位。
没有新可用的 Zotero、Obsidian 或指定 Codex reviewer 接口；未虚构交叉模型调用。
本地只做文件名级定位，没有读取旧构建产物正文、没有重做旧构建验证。
arXiv 使用公开页面与在线 PDF 回退，不本地下载；没有外部写入、实验或新增代理。
技能中的通用会议扫描与评分因本任务明确范围而跳过。

置信边界：未命中直接覆盖的把握为中等，特别是专门的伪随机置换、群生成与
有限域动力学文献可能存在术语不同的结果。没有找到，并不证明不存在。
本补充不审查主控正在推导的证明，不授予数学正确性或新颖性 PASS。
仅新增本文件；到此停止专项检索。
