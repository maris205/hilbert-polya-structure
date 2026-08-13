# Phase 2 Investigation：compact periodic packets 的 trace-formula 接口审计

**检索日期：** 2026-08-13  
**阶段边界：** 本文件只记录一手来源调查与适用性判断；不构造 packet groupoid，不提出下游论文论证，不做 Riemann 零点拟合。`MOD-RUELLE` 仅作为 isolated-orbit 系数基准。  
**主问题：** Deninger 的 compact periodic packet 能否凭其拓扑分解及 packet-base Haar 概率，直接获得 canonical trace mass / Lefschetz coefficient？

## 1. 结论先行

1. **正维闭轨族可以进入 trace formula，但“族”本身不够。** Duistermaat–Guillemin（DG）框架要求光滑辛相空间上的 Hamilton 流、光滑 clean fixed locus，以及
   \[
   T_z\operatorname{Fix}(\Phi^T)=\ker(d\Phi^T_z-I).
   \]
   族方向允许特征值 (1)，但不能在法向商空间中出现额外的 (1)-方向。首项是对每个 clean component 的 **DG canonical density** 积分；该密度由辛线性代数、算子的主/次主符号与 half-density/Maslov 数据共同决定，既不是“每个分量计数一次”，也不是先验概率测度。[DG, Definition 4.1, Lemmas 4.2–4.4, Theorem 4.5, printed pp. 59–61; local PDF pp. 22–24]

2. **contact/Morse–Bott 是另一套足够结构，不是纯拓扑条件。** Bourgeois 要求紧致光滑 contact 流形、contact form、离散 action spectrum；每个 (N_T=\{p:\phi^T p=p\}) 必须是闭光滑子流形，(\operatorname{rank}(d\alpha|_{N_T})) 局部常数，且 (T_pN_T=\ker(d\phi^T_p-I))。这说明连续闭轨族必须带可微、contact/辛及 clean 法向数据；其论文建立 contact-homology 的 Morse–Bott 接口，**本身不是一个 flow trace formula**。[Bourgeois, Definition 1 and §2.1, printed/local PDF p. 2]

3. **现有 Deninger packet 尚不能套用 clean-family 迹公式。** Deninger 证明的是拓扑悬挂系统中 packet 分解：
   \[
   \Gamma_{x_0}\simeq
   (\widehat{\mathbb Z}_{(p)}^\times/Nx_0^{\widehat{\mathbb Z}})
   \times_{p^{\mathbb Z}/\deg x_0}\mathbb R_{>0}/Nx_0^{\mathbb Z},
   \]
   每条轨道为周期 (log Nx_0) 的圆，packet 纤维化于 compact group，并由 Theorem 6.1 给出所有非平凡 isotropy 的分解。[Deninger, Introduction pp. 2–3; §6, printed/local PDF pp. 38–39, Theorem 6.1] 但该来源没有为 packet 给出：有限维光滑流形结构、导数 (d\phi^T)、clean tangent identity、辛/contact 法向丛、Hamilton/PDO/FIO propagator、principal symbol、Maslov 数据或可取 flat trace 的算子。故 **“topological packet + Haar”不能直接定义 DG density**（适用性否定，非“不存在任何未来扩充”的绝对否定）。

4. **foliated-flow 的最新严格公式也不覆盖 packet family。** Álvarez López–Kordyukov–Leichtnam（ALKL）要求 closed smooth manifold、横向定向的 codimension-one foliation、foliated smooth flow、simple closed orbits、transversely simple preserved leaves，并在切开 preserved leaves 后使用 conormal/dual-conormal leafwise currents、Witten perturbations、smoothing (b)-PDO 与 (b)-trace 的多重重整化。其“simple closed orbit”规定所有法向 return-map 特征值均不为 (1)，所以闭轨局部孤立、period set 离散；公式中的正维项是 **preserved leaves**，不是连续 closed-orbit packet。[ALKL, Abstract and §§1.3.1–1.3.10, local PDF pp. 5–14; §4.1.1, pp. 105–106 / printed pp. 99–100] 因而不能把其 isolated-orbit 项或 preserved-leaf 项未经新证明移植给 Deninger packet。

5. **Haar system、transverse measure、operator trace 是三个不同门槛。** Renault 的 Haar system 只在 second-countable locally compact groupoid 上给出连续不变的 (r)-fiber Radon-measure family，从而定义 (C_c(G)) convolution；群胚情形中 Haar system 的存在与唯一性均不自动成立。[Renault, §3, printed/local PDF pp. 7–8] Connes 则从另行选择的 holonomy-invariant transverse measure (\Lambda) 得到 foliation (C^*)-algebra 上的 trace；解析 index 本身可在不选择 (\Lambda) 时存在。[Connes, §§1–2 and §5, local PDF pp. 6–7, 16] 因而 **Haar system ⇒ convolution algebra**，不等于 **transverse measure ⇒ measured trace**，更不等于 **flow fixed-point/flat/Lefschetz trace**。

6. **Deninger §11 的卷积代数属于另一个对象。** 他令
   \(
   \overleftarrow K^{\times}=\varprojlim_N K^\times
   \)
   为局部紧拓扑**群**，以 compact open subgroup (T\mu_K) 归一 Haar 测度 (\mu(T\mu_K)=1)，并在 (C_c(\overleftarrow K^\times)) 上定义普通群卷积（105），再构造到 (\check X(\mathbb C)) 上连续函数的代数同态。[Deninger, §11, eqs. (104)–(114), printed/local PDF pp. 66–68] 文中没有把该群识别为 packet orbit/holonomy groupoid，也没有由它定义 (\phi^t) 的 fixed-point trace。因此此 Haar 归一仅固定该**群卷积**的尺度，不固定 packet-base、跨 packet 的 global mass 或 Lefschetz coefficient。

7. **最终可证边界是“三层归一化 + 一个独立算子门槛”。** 见 §3。当前一手来源只支持每个 compact group base 的 normalized Haar probability；其余层均未由 packet 构造给出。故主问题在当前对象上为 **OPEN / interface obstructed**，不是已构造 canonical trace。

## 2. 何时允许正维闭轨族进入 trace formula：必要性矩阵

| 门槛 | clean Hamiltonian/PDO | contact Morse–Bott | foliated/groupoid | Deninger packet 当前状态 | 判断 |
|---|---|---|---|---|---|
| 光滑环境与流 | compact boundaryless (C^\infty X)，smooth Hamilton flow on (T^*X\setminus0) | compact smooth contact (M)，Reeb flow | closed smooth (M)，smooth codim-1 foliation 与 foliated flow | topological、infinite-dimensional construction；未给有限维 smooth atlas | **缺失** |
| fixed family 是光滑子流形 | period-(T) fixed set 为 connected smooth components | (N_T) closed smooth | ALKL 的 periodic orbits 反而假设 simple/isolated | packet 是 compact topological fibration/bijection description | **缺失** |
| clean tangent identity | (T_zZ=\ker(d\Phi^T-I)) | (T_pN_T=\ker(d\phi^T-I)) | Kordyukov relative fixed set亦要求 clean fiber-product condition | 无 (d\phi^T) | **不可陈述** |
| normal return nondegeneracy | 族切向可有 (1)；normal quotient 不得有额外 (1)-核；孤立轨道化为 (I-P_\gamma) 可逆 | tangent equality排除额外法向 (1)-方向，并要求 (d\alpha|_{N_T}) constant rank | ALKL simple orbit 明定 normal map 无 eigenvalue (1) | 无 normal bundle/linearized return map | **不可陈述** |
| canonical density 的来源 | symplectic form + (I-d\Phi^T) 给 fixed tangent 的 intrinsic density；再结合 symbol/half-density/Maslov | contact form 与 (d\alpha) 提供 contact/symplectic 数据；但 Bourgeois 不提供 flow trace density | transverse density/measure 与 operator regularization均需明确选择 | compact-base Haar 概率只在 base 层 | **对象不匹配** |
| trace/propagator | elliptic positive self-adjoint PDO on half-densities；FIO clean composition | contact-homology chain/moduli package，非 trace operator | Kordyukov：transversally elliptic self-adjoint (A)、(R(k)\int f(t)e^{itP}dt) trace class；ALKL：smoothing (b)-PDO/b-trace | 无候选 Hilbert/Fréchet cohomology、generator domain 或 trace-class/flat-trace criterion | **缺失** |
| compactness/local finiteness | period support locally isolated；components 可积分 | discrete action spectrum | simple orbits使 compact period windows内有限；groupoid需 locally compact/second countable | 同一 (p) 有 compact packet，但跨 (p) 的局部有限性/trace summability未给 | **不足** |

**结论的精确强度。** 上表证明的是：现有 clean/Morse–Bott/foliated trace 定理的假设不能在当前 Deninger packet 上核验，故不可直接套用。它不证明某种新建 smooth/groupoid/operator enrichment 不可能存在。

## 3. canonical probability 与 global trace mass：三层归一化

### N1：packet-base invariant probability（局部、可成立）

Deninger 的每个 packet 纤维化于 compact group
\(
B_p=\widehat{\mathbb Z}_{(p)}^\times/p^{\widehat{\mathbb Z}}.
\)
对 compact group，Haar measure 归一为总质量 (1) 后唯一。因此 (B_p) 有 canonical normalized Haar probability。这里“canonical”仅指**给定 compact-group structure 后的组内归一**。

### N2：从 base 到 packet 的 lift/disintegration（未给）

由 (\pi_p:\Gamma_p\to B_p) 与 (m_{B_p}) 不能唯一推出 (\Gamma_p) 上的测度。仍需明确：

- 沿圆轨道的 conditional measures（弧长是否由流参数、primitive period 或概率方式归一）；
- 条件族的可测性/连续性；
- isotropy、重复覆盖与 quotient 的兼容性；
- 所得测度对流/holonomy 是否不变。

Deninger §6 给 fibration 与周期，不给这种 disintegration theorem 或 canonical lift。因此 N1 不推出 N2。此为基于来源缺项的 **OPEN/interface inference**，不是“不存在 lift”的定理。

### N3：跨 (p)/closed points 的 global component masses（未给）

即便对每个 (p) 得到质量 (1) 的 packet measure，仍需在离散分量指标上另给权重 (w_p)。逐 packet 概率完全不决定 (w_p/w_q)，也不保证
\(
\sum_p w_p K_p(t)
\)
是分布、迹或 log-determinant 的系数。复制一个 packet、或把某个 component weight 乘常数，而保持每个 base 的 normalized Haar probability 不变，即可看出 N1 对 N3 无约束。

### 独立的 O-gate：operator trace / Lefschetz coefficient（未给）

即使 N1–N3 均补齐，也还必须指定 operator/cohomology、domain、kernel wavefront 条件、trace-class 或 flat/(b)-trace 的定义及其重整化。ALKL 特别指出 (b)-trace 并非真正 trace、一般不消去 commutator，某些 (delta_0) 项可随 auxiliary choices 改变；这直接反驳“有 measure 就自动有 canonical trace”的跳步。[ALKL, §1.3.5, local PDF p. 13; §1.3.6, p. 14]

## 4. 卷积迹与 flow fixed-point trace 的分层

| 层 | 输入 | 产物 | 一手来源 | 对 packet 的状态 |
|---|---|---|---|---|
| A. algebraic convolution | second-countable locally compact groupoid + continuous invariant nonzero Haar (r)-system；群是单对象特例 | (C_c(G)) 的 convolution/* 与 (C^*)-completion | Renault §3 | Deninger §11 仅对另一局部紧**群**完成 |
| B. measured trace/weight | holonomy-invariant transverse measure (\Lambda)（及适当 measured/groupoid hypotheses） | foliation (C^*)-algebra 上依赖 (\Lambda) 的 trace/dimension map | Connes §§1–2, 5 | packet relation未被构造成此类 groupoid；无 global (\Lambda) |
| C. dynamical fixed-point trace | 明确 propagator/transfer/cohomology operator + trace-class 或 wavefront/renormalized trace + clean/nondegenerate fixed geometry | periodic-orbit/Lefschetz distribution | DG; Kordyukov; ALKL; Dyatlov–Zworski | 未给 operator 与 microlocal geometry |

**不可跨层推理：** Deninger §11 的 (\mu(T\mu_K)=1) 证明 A 层中一个群卷积的归一；它不构成 B 层的 packet transverse trace，更不证明 C 层的 flow trace formula。

## 5. MOD-RUELLE：仅用于 isolated-orbit coefficient benchmark

在 compact (C^\infty) Anosov flow 中，Dyatlov–Zworski 使用 flat trace
\(
\operatorname{tr}^{\flat}e^{-itP}=\pi_*\iota^*K_{e^{-itP}}
\)
并显式核验 diagonal pullback 的 wavefront 条件；Guillemin identity 为
\[
\operatorname{tr}^{\flat}e^{-itP}
=\sum_\gamma \frac{T_\gamma^{\#}\,\delta(t-T_\gamma)}{|\det(I-P_\gamma)|},\qquad t>0.
\]
这里 (P_\gamma) 在 stable/unstable normal bundle 上，Anosov 性保证 (I-P_\gamma) 可逆；(T_\gamma^\#) 是 primitive period。外幂迹的交替乘积再连接到 Ruelle zeta。[Dyatlov–Zworski, Theorem and eqs. (1.5)–(1.6), printed pp. 543–545 / local PDF pp. 3–5; §2.2 eqs. (2.4)–(2.5), pp. 548–549; Appendix B, pp. 565–566]

此基准只校准以下事实：repetition coefficient 来自 primitive period、normal determinant 和 operator trace identity；**不能**用来给正维 packet 设定“每 packet 质量 (1)”的系数。

Ruelle 1976 的原始 Fredholm 路线与现代推广同样建立在强动力学/算子结构上：原文要求 real-analytic Anosov flow 及 real-analytic stable/unstable foliations；GLP 将 entire-plane meromorphy扩展到 compact smooth (C^\infty) Anosov flows，使用 anisotropic currents/transfer operators。GLP 2022 erratum 修正 contact spectral-gap 部分，但明确声明 meromorphic-continuation 的第一部分不受影响。它们均处理 isolated hyperbolic periodic orbits，不覆盖 clean packet family。

## 6. 核心来源矩阵（逐源定位与证据等级）

数学定理的一手论文按 ARS 通用框架属于单项研究（design level VI），但对“定理的原始假设/结论”是本学科 gold standard；下列 Grade A 表示 claim fitness，而非临床式研究层级。

| ID | 一手/权威来源与稳定入口 | 精确定位 | 支持的命题 | 适用性/限制 | 等级 |
|---|---|---|---|---|---|
| DEN | C. Deninger, *Dynamical systems for arithmetic schemes*, Indagationes Math. 37 (2026), 25–136, DOI [10.1016/j.indag.2024.05.007](https://doi.org/10.1016/j.indag.2024.05.007); [arXiv:1807.06400v4](https://arxiv.org/abs/1807.06400) | Intro pp. 2–3; §6 pp. 38–39, Thm 6.1; §11 pp. 66–68, (104)–(114) | packet/fibration/period；§11 是 (\overleftarrow K^\times) group convolution | 未给 packet clean geometry、packet groupoid 或 flow trace | **PROVED A**（对象事实）；接口缺项 **OPEN** |
| DG | J.J. Duistermaat & V.W. Guillemin, *The spectrum of positive elliptic operators and periodic bicharacteristics*, Invent. Math. 29 (1975), 39–79, DOI [10.1007/BF01405172](https://doi.org/10.1007/BF01405172); [GDZ scan](https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0029/LOG_0010.pdf) | Def. 4.1; Lemmas 4.2–4.4; Thm 4.5, printed pp. 59–61 | clean fixed set、intrinsic positive density、component integral与孤立特例 | Hamilton/PDO/FIO 框架；非 topological packet theorem | **PROVED A** |
| BOU | F. Bourgeois, *A Morse-Bott approach to contact homology* (2002/2003), [author PDF](https://www.imo.universite-paris-saclay.fr/~frederic.bourgeois/papers/MorseBott.pdf) | Def. 1 and §2.1, p. 2 | contact Morse–Bott periodic family的精确条件 | contact homology，不是 trace formula | **PROVED A**（定义）；作接口证据 |
| KOR | Yu. Kordyukov, *The trace formula for transversally elliptic operators on Riemannian foliations*, [arXiv:math/0001182](https://arxiv.org/abs/math/0001182) | pp. 1–3 (A1–A2); Def. 5, pp. 5–6; Thm 6, p. 6 | foliated relative fixed sets仍需 smooth clean condition、transversally elliptic self-adjoint operator与regularized trace | 不从 Haar probability 自动生 trace | **PROVED A** |
| ALKL | J.A. Álvarez López, Yu.A. Kordyukov & E. Leichtnam, *A trace formula for foliated flows*, [arXiv:2402.06671](https://arxiv.org/abs/2402.06671); Springer LNM 2387 (2026), DOI [10.1007/978-3-032-15413-2](https://doi.org/10.1007/978-3-032-15413-2) | Abstract; pp. 1–8, Thms 1.3.7–1.3.10; pp. 99–100, §4.1.1 | 严格 Deninger-type foliated Lefschetz formula；simple isolated orbits；(b)-trace重整化 | 不覆盖 positive-dimensional periodic packets；preserved leaf不是 packet | **PROVED A** |
| CON | A. Connes, *A survey of foliations and operator algebras*, Proc. Symp. Pure Math. 38 (1982), 521–628, [author PDF](https://alainconnes.org/wp-content/uploads/foliationsfine.pdf) | local PDF pp. 6–7 (definition); p. 16 (transverse measure → trace) | transverse measure 是 holonomy-invariant σ-additive data；trace依赖 (\Lambda) | 权威原始综述；不提供 flow fixed-point trace | **PROVED A**（定义/对应） |
| REN | J. Renault, *Transverse properties of dynamical systems*, AMS Transl. Ser. 2 217 (2006), 185–199, [author PDF](https://www.idpoisson.fr/renault/pub/transverse.pdf) | §3, pp. 7–8 | groupoid Haar system hypotheses；存在/唯一性不自动；convolution/C*-completion | Haar system不等于 transverse trace或 flow trace | **PROVED A**（权威定理综述） |
| RS | D. Ruelle & D. Sullivan, *Currents, flows and diffeomorphisms*, Topology 14 (1975), 319–327, DOI [10.1016/0040-9383(75)90016-6](https://doi.org/10.1016/0040-9383(75)90016-6); [IHÉS scan](https://www.ihes.fr/~ruelle/PUBLICATIONS/%5B43%5D.pdf) | full article；并由 Connes §§1–3 明确重述 | oriented partial foliation + transverse invariant measure 给 closed current/homology class | 仍非 operator trace/fixed-point coefficient | **PROVED A**；通过 Connes 交叉核验 |
| RUE | D. Ruelle, *Zeta-functions for expanding maps and Anosov flows*, Invent. Math. 34 (1976), 231–242, [IHÉS PDF](https://www.ihes.fr/~ruelle/PUBLICATIONS/%5B45%5D.pdf) | Abstract and Intro I–II, pp. 231–232; Fredholm Theory pp. 233–236 | 原始 Ruelle/Fredholm determinant 的强 analytic/hyperbolic/operator 假设 | isolated Anosov benchmark；非 packet | **PROVED A** |
| DZ | S. Dyatlov & M. Zworski, *Dynamical zeta functions for Anosov flows via microlocal analysis*, Ann. Sci. ENS 49 (2016), 543–577, DOI [10.24033/asens.2290](https://doi.org/10.24033/asens.2290); [Numdam PDF](https://www.numdam.org/item/ASENS_2016__49_3_543_0.pdf) | pp. 543–545, (1.5)–(1.6); §2.2, (2.4)–(2.5); Appendix B | flat trace wavefront gate与 isolated-orbit coefficient | compact smooth Anosov、nondegenerate normal return | **PROVED A** |
| GLP+E | P. Giulietti, C. Liverani & M. Pollicott, *Anosov flows and dynamical zeta functions*, Ann. Math. 178 (2013), 687–773, DOI [10.4007/annals.2013.178.2.6](https://doi.org/10.4007/annals.2013.178.2.6); [erratum arXiv:2203.04917](https://arxiv.org/abs/2203.04917) | Abstract; §2, Thm 2.1/Cor. 2.2; erratum Abstract–§2 | (C^\infty) compact Anosov 全平面 meromorphy；transfer operator/anisotropic currents；erratum 边界 | contact spectral-gap 原结论须按 erratum 加强；meromorphy未受影响；非 packet | **PROVED A**（meromorphy）；受纠正部分 **CONDITIONAL** |

## 7. 检索策略与纳排记录

### 可复现策略

- **入口：** arXiv、Springer/Annals/Numdam/Elsevier 出版页、作者或 IHÉS/GDZ 机构档案；以 DOI/标题/作者交叉核验元数据。
- **查询族（逐字可复用）：**
  - `"clean fixed point set" Duistermaat Guillemin trace formula canonical density`
  - `"Morse-Bott" periodic orbits contact form ker(phi^T-I)`
  - `"trace formula for foliated flows" simple closed orbit Deninger`
  - `foliation transverse measure trace C* algebra Connes`
  - `groupoid Haar system existence uniqueness Renault convolution`
  - `Ruelle zeta Anosov Fredholm determinant original`
  - `dynamical zeta Anosov flat trace wavefront determinant Poincare`
  - `Deninger "Dynamical systems for arithmetic schemes" convolution Haar`
- **追溯：** 从 DG → Kordyukov clean-relative trace；从 Deninger/ALKL → simple foliated flows；从 Connes → Ruelle–Sullivan；从 Ruelle → GLP/Dyatlov–Zworski。未按“相似标题”扩展到一般 operator-algebra 分支。
- **时间/语言：** 无起始年限（基础定理不可施加现代窗口）；英语/法语元数据；最终只以可定位原文或权威作者综述支持关键结论。
- **记录方式：** 搜索服务不给稳定总命中数，故不虚报 PRISMA hit count；采用下列候选级 ledger。去重后 15 个作品级候选：核心纳入 11 组（GLP+erratum 合为一组），支持性纳入 2，排除 2。

### 纳入标准

1. 原创 theorem/definition 或作者级权威综述；
2. 能直接定位 smooth/clean/nondegenerate/Haar/operator hypotheses；
3. 能区分 measure/convolution trace/fixed-point trace；
4. 对 packet 接口或 MOD-RUELLE coefficient benchmark 有直接判别力。

### 排除/支持性 ledger

| 候选 | 决定 | 原因 |
|---|---|---|
| Álvarez López–Kordyukov–Leichtnam, *Simple foliated flows* (Tohoku Math. J. 74, 2022; arXiv:1906.06753) | 支持性纳入、本表不扩为核心行 | ALKL 2024/2026 已重述本次所需 simple/transversely-simple 条件；用于定义交叉核验 |
| D. Fried, *The zeta functions of Ruelle and Selberg I* (Ann. ENS 19, 1986) | 支持性纳入 | 精确 geodesic/Ruelle–Selberg benchmark，但 DZ/GLP 已覆盖本次 isolated coefficient 与现代 operator gate |
| Plante, *Foliations with measure preserving holonomy* (Ann. Math. 102, 1975) | 排除 | 主题相关但不直接解决 packet canonical mass、group convolution/flow trace 区分 |
| 一般 Rokhlin disintegration / homogeneous-space measure 文献 | 排除 | 一般存在定理不会从 base probability 选出 Deninger packet 的唯一 conditional family；避免制造未给结构 |
| 二手讲义、百科、搜索摘要 | 排除 | 只用于发现原文，不作为证据 |
| Connes 1999 Riemann-zero/noncommutative trace 分支 | 按协议排除 | 会越过 packet trace 接口并进入被禁止的一般 operator-algebra / zero-fitting 分支 |

## 8. 本地来源、完整性与定位说明

核心原文保存在 [`notes/sources/`](sources/)；主要文件如下：

- `deninger-dynamical-systems-arithmetic-schemes-v4.pdf` — SHA-256 `edd0bc8c…e1f82a09`
- `duistermaat_guillemin_1975.pdf` — `bf7dcd0a…fc4f2149`
- `bourgeois_2003_morse_bott.pdf` — `3128ecd7…be6262d`
- `kordyukov_2000_transversally_elliptic_trace.pdf` — `0d75baa5…25d71a9c`
- `alvarez_kordyukov_leichtnam_2024_trace_foliated_flows.pdf` — `b7037a1e…7e4ed49`
- `connes_1982_foliations_operator_algebras.pdf` — `b57aa0b7…990fa95`
- `renault_2013_transverse_properties.pdf`（实际出版 2006；文件名沿发现阶段保留）— `37f04016…b106c5`
- `ruelle_sullivan_1975_currents_flows.pdf` — `e2d64b7e…fb0209c`
- `ruelle_1976_zeta_anosov_flows.pdf` — `a4810542…d26652e`
- `dyatlov_zworski_2016.pdf` — `1ba0b0ea…e194ae`
- `giulietti_liverani_pollicott_2013.pdf` / `…_2022_errata.pdf` — `b9685ab6…e31598` / `254b9be8…09e40`

对上述 locally-read PDFs 已运行 ARS `pdf_read_preflight.py` 并保存同名 `.preflight.json`。当前环境缺 `pypdf`，sidecar verdict 为 `UNAVAILABLE`，故没有把 reader-derived page count 当成已验证锚点；页数以 `pdfinfo` 交叉核验，文本型 PDF 以 `pdftotext -f/-l` 核查，DG 与 Ruelle–Sullivan 扫描件以逐页图像核查。**注意：** `ruelle_sullivan_1974_preprint.pdf` 实为误下载的 HTML，未作为来源；可信扫描件是 `ruelle_sullivan_1975_currents_flows.pdf`。

## 9. Phase 2 stop decision

**停止扩搜，转交 Phase 3 no-go/interface audit。** 当前证据已饱和地支持以下窄结论：

- packet-base normalized Haar probability 可成立；
- 它不决定 packet lift/disintegration，不决定跨 packet global masses；
- Haar/group convolution 不等于 transverse measured trace，更不等于 flow fixed-point trace；
- 所有已定位的正维 clean-family trace theorem 均需要 Deninger 当前对象没有提供的 smooth/symplectic/operator 数据；
- 现有严谨 foliated-flow 公式保留 simple isolated closed orbits，不能作为 compact packet-family 公式；
- MOD-RUELLE 仅保留为 isolated coefficient control。

若下一阶段不能从 Deninger 对象本身补出 `(smooth/clean geometry) + (global transverse measure) + (operator trace class/renormalization)` 三组数据，则应把 paper 2 的结论写成**有条件接口定理/明确 no-go boundary**，而不是宣称已得到 canonical packet zeta。
