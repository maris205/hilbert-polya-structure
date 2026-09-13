# Paper30 T 分支：小耦合 Ruelle 共振的一手文献有界预筛

日期：2026-09-06。性质：独立于已停止上同调问题的新查新预筛。
仅新增本文件；不创建项目、稿件、候选评分、容量估计或数值实验。

## 结论先行

**精确正弦族、Fourier–Bessel 矩阵、单模反馈机制及线性衰减尺度均已有直接先例。**
不能将这组对象和现象改名后当成新方向：

- Thiffeault–Childress（2003）的式 (2) 就是本次的映射，参数对应 $K=2\pi\kappa$。
  其 §IV 式 (14) 给出取模的单模衰减因子 $\mu=e^{-\epsilon}J_1(K)\sim K/2$，
  并识别 $(0,1)$ 模自反馈与较长 Fourier cycle 的高阶 Bessel 机制。
  [原文 §II、§IV](https://arxiv.org/pdf/nlin/0211036)
- Faure–Roy（2006）在一个与本映射线性共轭的精确正弦模型上，
  给出 Fourier 指数权共轭、迹类算子、共振逼近和周期迹公式的一般严格框架。
  [原文 §2.2，定理 6—8、命题 9](https://www-fourier.univ-grenoble-alpes.fr/~faure/articles/resonances_RP_06.pdf)
- Slipantschuk–Bandtlow–Just（2017，简称 SBJ）的 Blaschke 族与本族一阶相切，
  其完整谱已包含负的二重半单 leading 共振；但该族二阶起不是纯正弦族。
  [作者最终稿式 (1)—(5)、定理 1.1](https://webspace.maths.qmul.ac.uk/w.just/ms/nonl_16.pdf)

本次**没有找到直接完整证明**下述纯正弦族严格全谱 $O(|\kappa|)$、
两条带符号 $-\pi\kappa+o(\kappa)$ 共振以及所提归一化核的文献。
这只是当前有界检索结果，不是穷尽性新颖证明，也不意味着这些待核命题成立。
所剩若有增量，只能是已经有物理先例的现象之严格谱控制／归一化证明，
不能把“尚未核到完整严格定理”写成“发现新线性衰减机制”。

## 1. 对象与待核主张

固定面积保持族
$$
F_\kappa=A\circ S_\kappa,\qquad
A=\begin{pmatrix}2&1\\1&1\end{pmatrix},\qquad
S_\kappa(q,p)=(q,p+\kappa\sin(2\pi q)).
$$
故
$$
F_\kappa(q,p)=(2q+p+\kappa\sin(2\pi q),\ q+p+\kappa\sin(2\pi q)).
$$
只讨论充分小实参数下、对应面积／SRB 测度相关函数的 Ruelle–Pollicott 共振；
不是 $L^2$ 上酉算子的普通谱，也不是最大熵测度的另一套共振。
算子可采用拉回 $C_\kappa f=f\circ F_\kappa$；比较 Perron–Frobenius 文献时须核对
其适当对偶空间及谱约定，不将谱行列式零点与共振特征值混为一谈。

待核主张分为四项：

1. 精确本族与小参数非平凡共振存在性的研究是否已出现。
2. 全部非平凡共振的最大模是否严格满足 $r_{\rm nt}(\kappa)=O(|\kappa|)$。
3. 是否有按代数重数计的两条 leading 共振
   $\lambda_\pm(\kappa)=-\pi\kappa+o(\kappa)$。
   下标仅标记两支，不表示一正一负，也不预设有限非零参数下两支完全相等。
4. 用参数相关 Fourier 权及 $1/\kappa$ 谱缩放组织解析／核算子的办法是否已有直接先例。

第 2—4 项是本次请求提供的假设，不是本报告证明的结论。
普通 nuclearity、单个迹的一阶展开及有限矩阵的首项均不自动证明第 2—3 项。

## 2. 检索与执行范围

已全文读取 `idea-creator`、`research-lit`、`novelty-check` 三项技能。
最新任务指定只有这一项理论预筛，因而不执行技能模板中的 8—12 个新想法、排名、
项目生成或实验流程；纯理论条款用于跳过 pilot，本轮 GPU／实验用量为零。
纯理论待证关口不会被“需要 pilot”替代。

本地 `papers/` 文件名检查未发现与本题相关的公开先行文献 PDF；
`literature/`、`tools/` 不存在，未发现可用的本地 `arxiv_fetch.py`。
因此使用技能允许的官方 arXiv 网页检索降级；没有下载文献到工作区。
正文通过公开 arXiv、作者网站和期刊网站读取；搜索命中的聚合页只作寻路，不作为结论证据。

可调用工具中没有 `mcp__codex__codex` 或对应的 GPT-5.4 审查接口。
实际采用一名独立来源检查代理，核对 SBJ 及近期文献，并另行实际读取 TC03 的 §IV，
完成了 `actual secondary fallback`。没有将其记作 GPT-5.4 MCP 或跨模型指定审查。

检索覆盖基础文献、2024—2026 年，以及明确的最近六个月窗口
**2026-03-06 至 2026-09-06**。使用的查询包括：

- `Faure Roy Ruelle resonances analytic Anosov maps torus perturbation cat`；
- `perturbed cat map Ruelle resonances Bessel small perturbation leading eigenvalues sine`；
- `small coupling Arnold cat map Ruelle resonance linear perturbation spectrum`；
- `cat map Ruelle Bessel`、`perturbed cat J_1 resonance`；
- `Chaotic mixing in a torus map`、`The Strange Eigenmode in Lagrangian Coordinates`；
- `Generic non-trivial resonances for Anosov diffeomorphisms`；
- `small perturbations cat resonances`、`Ruelle nuclear rescaling torus`；
- `cat map linear leading resonances 2024 2025 2026`；
- `Ruelle resonances cat perturbation after:2026-03-06 before:2026-09-07`；
- 对 SBJ、Pollicott–Sewell、Jézéquel、Galli 和 2025 年预印本的题名及版本查询。

未命中查询不作为不存在性的证据；搜索抓取时间也不作为论文发表日期。

## 3. 已读一手来源与准确覆盖层级

| 一手文献 | 实际读取层级 | 与待核对象的关系 |
|---|---|---|
| Thiffeault–Childress，*Chaotic Mixing in a Torus Map*，Chaos 13 (2003), 502–507 | arXiv 最终版摘要、§II 式 (1)—(9)、§IV 式 (13)—(14) 及 cycle 段；主、次检查均读取 | **精确本族**；Bessel 矩阵、单模线性尺度及闭链机制的直接先例；严格性边界见下节。[原文](https://arxiv.org/pdf/nlin/0211036) |
| Thiffeault，*The Strange Eigenmode in Lagrangian Coordinates*，Chaos 14 (2004), 531–538 | 摘要、引言及模型式 (2.1)—(2.2) | 同正弦族的带扩散混合及 Lagrangian 分析；其“rescaling”是时间依赖坐标缩放，不是本次 $\kappa\to0$ 共振核归一化。[原文](https://arxiv.org/pdf/nlin/0403027) |
| Faure–Roy，*Ruelle–Pollicott resonances for real analytic hyperbolic maps*，Nonlinearity 19 (2006), 1233–1252 | 引言、§2.2 模型与定理 6—8、命题 9 | 共轭后的精确正弦模型；一般迹类及共振理论直接覆盖；未给本次参数首项。[作者全文](https://www-fourier.univ-grenoble-alpes.fr/~faure/articles/resonances_RP_06.pdf) |
| Adam，*Generic non-trivial resonances for Anosov diffeomorphisms*，Nonlinearity 30 (2017), 1146–1164 | 摘要、构造介绍、定理 4.3 及证明、§5 算子关系 | 零阶核性和非平凡共振存在；其导数检验可直接代入本族，见第 5 节。[原文](https://arxiv.org/pdf/1605.06493) |
| SBJ，*Complete spectral data for analytic Anosov maps of the torus*，Nonlinearity 30 (2017), 2667–2686 | 作者最终稿模型式 (1)—(4)、定理 1.1、推论 1.2；主、次检查均读取 | Blaschke 族的完整显式谱；与纯正弦族一阶相切，不是精确同族。[作者全文](https://webspace.maths.qmul.ac.uk/w.just/ms/nonl_16.pdf) |
| Pollicott–Sewell，*Explicit examples of resonances for Anosov maps of the torus*，Nonlinearity 36 (2023), 110–132 | 期刊／仓储摘要；独立检查读 Definition 2.1、Theorem 2.2 | 另一加权空间及 Blaschke 例子的简化／扩展；参数符号约定不同。[作者预印本全文](https://arxiv.org/html/2204.01511v1) |
| SBJ，*Resonances for rational Anosov maps on the torus*，2022 预印本 | 摘要、引言、Theorem 1.1—1.2；独立检查另读 Corollary 4.2 | general trace-class 与有理型显式谱部分分开；显式谱附加假设不覆盖当前指数因子。[全文](https://arxiv.org/html/2211.05925v1) |
| Yoshida–Yoshino–Shudo–Lippolis，*Eigenfunctions of the Perron-Frobenius operator and the finite-time Lyapunov exponents in uniformly hyperbolic area-preserving maps*，J. Phys. A 54 (2021), 285701 | 摘要、模型式 (1)—(3)、§4 式 (10)—(13) 及表 1 附近文字 | 其 $\nu=1$ 情形交换坐标后为本族负参数侧；Bessel／噪声谱数值研究，不是小参数全谱渐近定理。[原文](https://arxiv.org/pdf/2101.11701) |
| Blum–Agam，*The leading Ruelle resonances of chaotic maps*，Phys. Rev. E 62 (2000), 1977 | 摘要、模型式 (1)、扰动、式 (13)—(14) 的变分截断说明 | 线性部分为 $\left(\begin{smallmatrix}2&1\\3&2\end{smallmatrix}\right)$，扰动含两个余弦；不是本族；其四根近似不能套用。[原文](https://arxiv.org/pdf/nlin/0005030) |

## 4. 最直接的旧模型与旧机制：TC03

TC03 的映射为
$$
M(x)=\begin{pmatrix}2&1\\1&1\end{pmatrix}x+
\frac K{2\pi}(\sin(2\pi x_1),\sin(2\pi x_1)).
$$
取 $K=2\pi\kappa$ 即完全等于本次 $F_\kappa$，不需要近似或非线性共轭。
其 §II 已写 Fourier 转移矩阵的 Bessel 表示；§IV 识别能够映回自身的纵向模式，
在正小参数约定下以 $(0,1)$ 模得到 $\mu\sim K/2=\pi\kappa$。
文中 $\mu$ 是用于衰减的模长，方差乘子为 $\mu^2$，不是已判定符号的两支共振。
[TC03 式 (2)、(9)、(13)—(14)](https://arxiv.org/pdf/nlin/0211036)

§IV 随后的 cycle 段还明确讨论了多步返回链，并用较高阶 Bessel 项在小 $K$ 下较小
来排除其成为主要衰减机制。因而“从闭 Fourier 链代价找 leading 模”的总体想法也已有先例。
但实际读到的文本采用单模近似、机制论证及数值吻合，没有呈现对任意频率、任意链长的
统一算子／谱余项估计，也没有给出带符号双重共振与归一化核的定理。
[TC03 §IV，预印本第 5—6 页](https://arxiv.org/pdf/nlin/0211036)

本次判断是：**同模型和 leading 模长／机制直接覆盖；完整严格谱结论未核到直接覆盖。**
不能把取模的 $J_1$ 公式说成已证明 $-\pi\kappa$ 的符号、两支重数或所有其余谱的大小。

## 5. 一般核性及非平凡共振存在性应全部扣除

FR06 §2.2 式 (10) 的例子是
$$
M_\delta(q,p)=(2q+p,\ q+p+\tfrac\delta{2\pi}\sin(2\pi(2q+p)))
=S_{\delta/(2\pi)}\circ A.
$$
因此 $A^{-1}F_\kappa A=M_{2\pi\kappa}$。
这是依据文中模型公式得到的显式适用性核对：精确正弦族不是本轮新引入的研究对象。
定理 6 的 Fourier 指数权共轭给出指数衰减矩阵及迹类性；
定理 7 控制共振随**谱序号**趋近零，定理 8 是噪声趋零逼近，命题 9 是周期迹公式。
这些结论不能被改写成**耦合参数**趋零的 $O(|\kappa|)$ 定理。
[FR06 §2.2](https://www-fourier.univ-grenoble-alpes.fr/~faure/articles/resonances_RP_06.pdf)

Adam 的定理 4.3 不只在本题提供抽象的 generic 背景。
对 $\psi(q,p)=(\sin(2\pi q),\sin(2\pi q))$，其固定点导数泛函可直接计算：
$A$ 只有原点这个环面固定点，而
$$
(I-A)^{-1}=\begin{pmatrix}0&-1\\-1&1\end{pmatrix},\qquad
D\psi(0)=\begin{pmatrix}2\pi&0\\2\pi&0\end{pmatrix},\qquad
\operatorname{Tr}((I-A)^{-1}D\psi(0))=-2\pi\neq0.
$$
将它代入文中公式即满足非退化检验，故本族充分小非零参数的非平凡共振存在性
已经是该定理的直接应用。这是本报告的公式代入判断，不是源文单独命名的正弦族定理。
核性、非平凡共振存在、迹一阶都不能作为新的主体贡献；
一个迹的首项也不自动控制全部特征值或排除相互抵消。
[Adam 定理 4.3、§5](https://arxiv.org/pdf/1605.06493)

## 6. SBJ 的显式双首项：强旧先例，但不同精确族

SBJ 对实参数 $a$ 的 shear 是
$$
\psi_a(q)=\frac1\pi\arctan\frac{a\sin(2\pi q)}{1-a\cos(2\pi q)},
\qquad
T_a(q,p)=(2q+p+\psi_a(q),\ q+p+\psi_a(q)).
$$
定理 1.1 给出谱 $\{1,0\}\cup\{(-a)^n:n\ge1\}$，各非零幂在实参数下计重两次且半单。
因此其最大非平凡模为 $|a|$，leading 为二重 $-a$。
[SBJ 模型与定理 1.1](https://webspace.maths.qmul.ac.uk/w.just/ms/nonl_16.pdf)

从其公式展开得到
$$
\psi_a(q)=\frac a\pi\sin(2\pi q)+\frac{a^2}{2\pi}\sin(4\pi q)+O(a^3).
$$
取 $a=\pi\kappa$ 时两族一阶相切、二阶即不同。
这使所猜负双首项有非常接近的精确先例，但在零处退化的无限维共振问题中，
映射相差 $O(\kappa^2)$ 本身不是共振首项稳定的证明。
若后续证明成立，必须承认它是在把旧显式族和旧单模现象推广／严格化到纯正弦族。

SBJ 的 rational 后续文献也不能整体打包为本题的显式谱定理。
Theorem 1.2 的显式定位部分要求正逆映射延拓到指定内／外 bidisk；
Corollary 4.2 给出相应有理性要求。当前复化因子为
$$
E_\kappa(z)=\exp[\pi\kappa(z-z^{-1})],\qquad
F_\kappa(z,w)=(z^2wE_\kappa(z),zwE_\kappa(z)).
$$
对 $\kappa\neq0$，该因子在 $0,\infty$ 有本性奇点，不满足上述有理结构条件。
这是关于当前坐标表达式的适用性排除，不是宣称不存在任何其他共轭或后续方法。
其一般加权空间思想仍是应扣除的旧方法。
[SBJ rational 全文 Theorem 1.1—1.2、Corollary 4.2](https://arxiv.org/html/2211.05925v1)

## 7. 2024—2026 与最近六个月的实际核对

| 来源与日期 | 实际层级及边界 |
|---|---|
| Jézéquel，AHL 7 (2024), 673–726，2024-09-05 在线发表 | 主、次检查读期刊摘要；主检查另核引言定理摘要。研究 $r\to0$ 的计数 $N(r)=O(|\log r|^d)$ 及稠密最优性，不是本族 $\kappa\to0$ 的首共振。[期刊原页](https://www.numdam.org/articles/10.5802/ahl.208/) |
| Bandtlow–Just–Slipantschuk，*A numerical study of rigidity of hyperbolic splittings in simple two-dimensional maps*，Nonlinearity 37 (2024), 045007 | 主检查读官方摘要／元数据；独立检查读式 (2)—(3)。仍使用 arctan／Blaschke shear，研究双曲分裂，不改为纯正弦共振渐近。[原文](https://arxiv.org/html/2402.14770v1) |
| Galli，*A cohomological approach to Ruelle-Pollicott resonances and speed of mixing of Anosov diffeomorphisms*，arXiv:2405.17045v2，**2026-06-09 更新** | 独立检查读摘要、Theorem 1.2 与引言主结果；主检查核对官方记录。对象为最大熵测度及上同调外围共振，不能套作面积／SRB 共振的本族结论。[v2 原文](https://arxiv.org/html/2405.17045v2) |
| Blumenthal–Nisoli–Taylor-Crush，*A pseudospectral approach to rigorous numerical estimation of resonances of transfer operators*，arXiv:2507.09021v2，**2026-06-02 更新**，to appear FoCM | 独立检查读摘要、§1.2.1、§6.3；主检查核对官方记录。一般认证框架提及 Anosov，但实际实现是解析扩张圆映射，§6.3 保留 Anosov 可计算实现关口；不含本族首项。[v2 原文](https://arxiv.org/html/2507.09021v2) |
| Herwig–Colbrook–Junge–Koltai–Slipantschuk，arXiv:2507.16915v1，2025-07-22 | 独立检查读摘要及案例目录。transfer-operator 残差／无谱污染计算，示例为 Blaschke 与分子动力学，不提供指定正弦族渐近。[原文](https://arxiv.org/html/2507.16915v1) |

最近六个月的具体新命中是上表两个六月更新；没有把 2003、2006 年 PDF 的近期抓取日期
误记成 2026 年新论文。SBJ rational 的官方记录仍只列 2022-11-10 的 v1。
[官方版本记录](https://arxiv.org/abs/2211.05925)

## 8. 针对四项主张的减量与停止边界

| 主张 | 本次查新判断 |
|---|---|
| 精确正弦族、Fourier–Bessel 表示 | TC03 精确直接覆盖，FR06 线性共轭覆盖；已旧。 |
| 小参数非平凡共振存在 | Adam 的非零迹导数检验直接适用；已旧。 |
| leading 模长尺度 $\pi|\kappa|$、单模反馈／闭频率链机制 | TC03 已有同族分析和近似结果；不能当成新发现。 |
| 严格的全体非平凡共振 $O(|\kappa|)$ | 所读来源未提供可直接引用的同族完整定理；并未据此判定新颖或可证。 |
| 两条带符号 $-\pi\kappa+o(\kappa)$ | SBJ 有一阶相切族的精确二重先例；TC03 的取模公式不处理符号和重数。纯正弦版本未核到直接完整定理。 |
| 普通解析／迹类／nuclear 组织 | FR06、Adam、SBJ 及后续加权空间大量直接先例；已旧。 |
| 参数奇异加权后再除以 $\kappa$ 的归一化极限核 | 未核到与所提具体归一化完全同式的来源；仍须证明核范数控制、参数解析性及与真实共振的等谱关系，不能从普通核性自动获得。 |

主控提供的新 Fourier 边代价势不等式，在本报告中仅作为本轮理论输入记录：
它与 TC03 的闭链高阶机制方向一致。本次未找到完全同式的先行引理，
但没有因此为这条短整数不等式赋予新颖性认证，也没有替主控证明其后所有谱论步骤。
“闭链每步最低阶至少一”到“全部共振 $O(|\kappa|)$”之间，
还需要对无限频率及所有链长的统一控制；最高阶模式的系数增长不能由单项形式阶数掩盖。

尤其，除去常数后线性 cat 的非平凡谱退化于零，不代表对应算子本身为零。
所以直接把原核除以 $\kappa$ 并称其解析延拓没有依据；
任何参数相关权变换还须交代空间、可逆／等谱范围及算子理想中的收敛。
这些是可能的严格化关口，不是本报告已经完成的新理论结果。

独立 `actual secondary fallback` 的最终判断与上述一致：
TC03 已覆盖 leading 模长／反馈机制；SBJ 已提供非常接近的负二重精确谱先例；
可能剩下的是严格全谱控制与归一化证明缺口，而非新模型、新机制或一般核性。

## 9. 同轮追加的唯一查询：次谱簇与分数幂先例

主控随后仅授权补查：本正弦族在两条 leading 共振以下，是否已有
$|\kappa|^{3/2}$、Puiseux 或平方根分裂的严格／物理先例。
提供的三频率链及简化特征多项式
$\lambda^3+t\lambda^2-\tfrac23t^4$（$t=\pi\kappa$）只用于确定检索词。
其形式根不能证明完整算子的次谱簇存在、重数或首项系数；本报告不核准这一推断。

追加查询为 `cat map resonances Puiseux`、`perturbed cat eigenvalues 3/2`、
`cat map resonances square root`、`weakly nonlinear cat map spectrum`、
`perturbed cat second resonances Bessel`、`cat map subleading small spectrum perturbation`、
`Ruelle Puiseux Anosov`、`cat map resonances fractional`、
`perturbed cat map three halves`、`cat map eigenvalues K^{3/2}`、
`cat map resonances Puiseux 2024 2025 2026` 及 `sine Anosov resonances square-root`。
本次未命中本精确族的 $3/2$ 次谱簇直接严格定理或明确物理预测；此阴性检索仍非穷尽证明。

不过，“Anosov 共振具有参数分数幂”本身已有严格先例。
追加实际读取 Pollicott–Sewell 的 §3 Definition 3.1、Theorem 3.2 及 Lemma 3.7，
其族为
$$
T_a(z,w)=\left(\frac{z+a}{1+\overline a z}\,w,z\right),\qquad |a|<1,
$$
基点 $T_0(z,w)=(zw,z)$ 的整数矩阵是
$\left(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\right)$，行列式为 $-1$，
即反定向的 cat map 平方根。取 $a_1^2=a$，文中严格谱公式包含
$$
\{1,0\}\cup\{\omega a_1^m\overline{a_1}^{\,n}:
m,n\in\mathbb N_0,\ m+n\ge1,\ \omega\in\{1,-1\}\}.
$$
特别地，正实 $a$ 下其谱有 $\pm a^{j/2}$ 的层级，包括 $j=3$。
这是实际已证的异族先例，不是从论文题名推测出来的联系。
[Pollicott–Sewell §3，尤其 Lemma 3.7](https://arxiv.org/html/2204.01511v1)

该有理族既非本次保定向 $F_\kappa$，也不是纯正弦 perturbation。
$T_0^2=A$ 不能把整个参数族的共振及缩放律不加证明地移植过来；
其平方映射与谱平方还会改变谱指数。故这个先例扣除的是泛称“分数幂／平方根共振”的新颖性，
并不直接覆盖本族待核的次谱簇、$3/2$ 指数出现的位置或 $\sqrt{2/3}$ 首项系数。

主控另提供的参数相关核与有限秩零阶／幂零块只是新的待核理论输入；
本次没有检查或证明它们，也没有由一般有限维平方根分裂原理代替无限维谱控制。
尤其，任何带 $t^{3/2}$ 的最终陈述还需规定单侧实参数或复分支，不能在负参数处含混使用。

**处置：本轮有界查新及唯一追加查询至此停止。** 不追加小支撑或低阶试表，不运行 pilot，
不开展数值验证、稿件写作、候选评分或容量估计；所有尚待核实的谱假设不标记为已证。
本报告不修改已停止的上同调问题状态，也不将两个问题拼接为同一成果。
