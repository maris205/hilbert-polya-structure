# Stage 1 Literature Review

检索截止日：2026-08-13。本文采用**目标导向的范围综述**，不是声称穷尽全部文献的系统综述；因此不伪造数据库总命中数或 PRISMA 流程数。检索入口包括出版社/期刊主页、arXiv、MathNet、Numdam、Crossref 元数据，以及项目提供的六份 PDF。核心纳入条件是：来源必须直接定义候选流、证明闭轨/Zeta/trace 结构，或给出能区分 exact identity、distributional theorem、semiclassical asymptotic 与 heuristic analogy 的原始结果。

## Search concepts and selection rules

组合检索词包括：`arithmetic scheme flow periodic orbit log norm`、`PSL2Z primitive hyperbolic geodesic length trace`、`Selberg trace formula hyperbolic term`、`Ruelle Selberg quotient`、`Anosov dynamical zeta meromorphic continuation`、`Axiom A prime orbit theorem`、`wave trace periodic bicharacteristics`、`Gutzwiller exact versus semiclassical`、`xp no periodic orbit`。对会影响结论的公式，优先核对原始论文或权威专著；综述只用于定位，不单独承担关键定理。

排除项：只报告零点拟合、只报告 GUE、没有冻结时钟/归一化、把 “prime geodesic” 偷换成有理素数、把局部波迹奇性写成全局收敛迹公式、或把一般 Gutzwiller 渐近写成 exact identity 的材料。

## Evidence map

| Source | Direct contribution to Stage 1 | Epistemic status |
|---|---|---|
| [Deninger, *Dynamical systems for arithmetic schemes*](https://doi.org/10.1016/j.indag.2024.05.007) | 从 rational Witt 空间构造无限维 \(\mathbb R\)-流；闭点与周期结构相联系 | peer-reviewed primary theorem |
| [Deninger, *Primes, knots and periodic orbits*](https://arxiv.org/abs/2301.11643) | 清楚陈述：\(\operatorname{Spec}\mathbb Z\) 中的 \((p)\) 对应周期为 \(\log p\) 的 compact packet，而非唯一轨道；全局 admissibility 尚非唯一 | author survey of the construction; exact theorem restatement |
| [Selberg 1956](https://doi.org/10.18311/JIMS/1956/16985) and [Hejhal 1983](https://doi.org/10.1007/BFb0061302) | 模曲面/余有限 Fuchsian 群的 exact trace formula；cusp、elliptic、parabolic、continuous spectrum 不可省略 | exact identity / authoritative derivation |
| [Pohl--Zagier](https://arxiv.org/abs/1906.01067) | primitive hyperbolic conjugacy classes、周期测地线与 transfer dynamics 的可读入口 | peer-reviewed mathematical survey |
| [Sarnak 1982](https://doi.org/10.1016/0022-314X(82)90028-2) | 模群闭轨、实二次单位与 indefinite binary quadratic forms/class-number multiplicity | exact arithmetic theorem |
| [Ruelle 1976](https://doi.org/10.1007/BF01403069) | primitive-orbit Euler product 的基础解析理论 | theorem under stated analytic hypotheses |
| [Fried 1986](https://doi.org/10.24033/asens.1515) | 固定 convention 下 \(R(s)=Z(s)/Z(s+1)\)，说明 Ruelle log derivative 消去 Selberg 稳定性分母 | exact identity |
| [Giulietti--Liverani--Pollicott 2013](https://doi.org/10.4007/annals.2013.178.2.6) | \(C^\infty\) Anosov flow 的 Ruelle zeta 全平面亚纯延拓 | exact theorem; spectral-gap claims须连同 [2022 erratum](https://arxiv.org/abs/2203.04917) 阅读 |
| [Dyatlov--Zworski 2016](https://doi.org/10.24033/asens.2290) | 光滑 Anosov flow 的微局部亚纯延拓与 flat-trace/PR resonance 架构 | exact microlocal/distributional theorem |
| [Parry--Pollicott 1983](https://doi.org/10.2307/2006982) | weak-mixing Axiom-A flow 的 primitive orbit count \(\sim e^{hT}/(hT)\) | exact asymptotic; proves-too-much control |
| [Mayer 1991](https://doi.org/10.1090/S0273-0979-1991-16023-4) | 模群 Selberg zeta 的 transfer-operator/Fredholm determinant 架构 | analytic theorem |
| [Duistermaat--Guillemin 1975](https://doi.org/10.1007/BF01405172) | fixed elliptic operator 的波迹奇性位于闭双特征长度，局部系数含 monodromy determinant | exact distributional/local theorem |
| [Gutzwiller 1971](https://doi.org/10.1063/1.1665596) | 孤立周期轨道的半经典谱密度贡献 | semiclassical asymptotic, not a generic exact trace identity |
| [Weil 1972](https://doi.org/10.1070/IM1972v006n01ABEH001866) | 数论显式公式的 prime-power 支撑与 \((\log p)p^{-r/2}\) 核心权重 | exact arithmetic identity |
| [Berry--Keating 1999](https://doi.org/10.1137/S0036144598347497) | \(T_p=\log p\) 的 Hilbert--Pólya/periodic-orbit 对照，以及未正规化 \(xp\) 的局限 | arithmetic formula exact; flow identification heuristic |
| [Anosov 1967](https://www.mathnet.ru/eng/tm2795) | 紧致负曲率流形的稳定/不稳定分解 | exact theorem;不能不加说明套到非紧模曲面 |
| [Luo--Sarnak 1995](https://doi.org/10.1007/BF02699377) | 模曲面离散 cusp spectrum、Eisenstein continuous spectrum 与量子遍历性 | exact theorem; QE 不约束零点位置 |

核心外部证据共 17 项，其中 15 项是同行评审原始论文或权威证明性专著；两项是作者/数学综述。数学研究不适合套用临床证据等级，本项目以“可逐步核查的定理/恒等式”为最高层，以条件定理、数值观察、启发式依次降级。

## Synthesis

### 1. Arithmetic-native flow: periods succeed, isolated-orbit trace does not yet

Deninger 的冻结对象取 \(X_0=\operatorname{Spec}\mathbb Z\)，并显式选择其论文允许的 finite-kernel admissibility condition；本文将该选择记为 \(\mathcal E_{\rm fin}\)。流为

\[
X_{0,\mathcal E}=\bigl(\check X_0(\mathbb C)_{\mathcal E}\times\mathbb R_{>0}\bigr)/\mathbb Q_{>0},
\qquad \phi^t[P,u]=[P,e^tu].
\]

定理把周期点集分成两两不交的 compact packets \(\Gamma_p\)，每个 packet 内所有轨道周期都是 \(\log p\)，且所有周期轨道都来自某个闭点。这个结果在 A0 上非常强：算术、时钟和 prime powers 都不是查表植入。然而作者明确指出 \(p\) 对应的不是一条轨道，而是一整个 compact packet；目前缺少 canonical transverse measure、单轨道重数、相位、光滑 monodromy 以及由真实 trace/Lefschetz 原理导出的 packet 权重。因此应记 `A0_ANALYTIC_ARITHMETIC_ORIGIN + A1_WEAK`，而不是声称已构造 Hilbert--Pólya flow。

### 2. Hyperbolic geodesic flow: isolated orbits and traces succeed, rational-prime support fails

对 \(\gamma\in\mathrm{PSL}_2(\mathbb Z)\) 的 primitive hyperbolic class，单位速测地流给出完整的 primitive/repetition、长度、方向、Poincaré multiplier 与 Selberg/Ruelle 架构。标准 norm 是

\[
N_\gamma=e^{\ell_\gamma}=\left(\frac{t+\sqrt{t^2-4}}2\right)^2,
\qquad t=|\operatorname{tr}\gamma|\ge3.
\]

但 \(N_\gamma+N_\gamma^{-1}=t^2-2\)，所以 \(N_\gamma\) 是实二次单位而非有理整数；本项目进一步证明任何 \(N_\gamma^r\) 都不可能是有理数。因此全体 repeated length support 与 \(k\log p\) 完全不相交。模曲面有真正的“算术”来源，但不是 Route A 要求的 rational-prime mechanism，故为 `A0_WEAK_ARITHMETIC_RELATION + A1_PASS_ANALYTIC`，作为 HP 主候选被拒绝、作为 exact trace calibration benchmark 保留。

### 3. Amplitude is not one formula

Selberg hyperbolic coefficient为

\[
\frac{\ell_\gamma}{2\sinh(r\ell_\gamma/2)}
=\frac{(\log N_\gamma)N_\gamma^{-r/2}}{1-N_\gamma^{-r}},
\]

其中分母正是 transverse stability。Riemann/Weil 目标为 \((\log p)p^{-r/2}\)。Ruelle quotient 的 log derivative 会消掉 \((1-N^{-r})^{-1}\)，这是 Stage 2 的真实线索；但它不改变长度支撑、class-number multiplicity，也不自动给自伴算子。Selberg exactness、Ruelle resonance theory、Duistermaat--Guillemin wave trace 与 Gutzwiller semiclassics 必须分层陈述。

### 4. Counting is a generic false positive

Parry--Pollicott 说明广泛的 weak-mixing Axiom-A flows 都有 \(e^{hT}/(hT)\) 的 primitive-orbit 计数。令 \(x=e^{hT}\) 就得到 \(x/\log x\) 外形；按秩把 orbit norms 和 rational primes 配对也会渐近接近。这种现象在无任何数论来源的 compact hyperbolic flow 仍存在，所以不能通过 A0。

### 5. Classical-to-quantum evidence boundary

模曲面 Laplacian 是 fixed self-adjoint host，Selberg trace 是 exact；但模曲面非紧，完整公式含连续谱和 scattering。一般 Gutzwiller 只是半经典渐近，Duistermaat--Guillemin 是分布意义的局部奇性定理，PR resonances 又来自各向异性空间上的非自伴生成元。三者都不能仅凭形式相似升级为 RH 所需的固定自伴谱恒等式。

## Residual gap and smallest next question

没有一个冻结候选同时达到 pass-level A0 与 A1。最小的正向问题不是继续拟合零点，而是：能否在 Deninger packet \(\Gamma_p/\mathbb R\) 上构造 functorial canonical measure，并从同一个动力学 trace/Lefschetz 对象推出每个 packet 对第 \(r\) 次重复只贡献一次正确归一化的权重？如果不能，Stage 1 的 two-halves obstruction 即是稳定负结论。
