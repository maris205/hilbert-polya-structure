# Prior-Work Audit for the Classical-Flow Baseline

页码均为 PDF 物理页。六份文件未加密并可逐页提取文本，但环境缺少 `pypdf`，所以 PDF preflight 记为 `UNAVAILABLE/advisory`，不表述为已通过完整对象完整性认证。

证据级别：`E4` 为可逐步核查的证明/代数恒等式；`E3` 为条件定理；`E2` 为未用目标量校准的可复现数值；`E1` 为启发式/有限相关/目标调参；`E0` 为循环校准、反例或关键证明缺口。Paper 6 因极新而以 `E4-P` 表示“形式化证据强但外部共识未形成”。

## Net inheritance table

| Prior paper | Reusable for Stage 1 | Must not be inherited as evidence |
|---|---|---|
| Paper 1, prime/logistic | arithmetic-symbolic seed and a parameter-leak negative control | “prime sieve--kneading isomorphism” is explicitly Conjecture A; twin-prime constant is circularly calibrated |
| Paper 2, topology bounds | finite MSS defects; natural-prime admissibility; Parity--Gap implication; explicit mod-3 failure | the printed even-gap proof has a direction error; geometric-decay theorem and \(\rho\to0\) are not established |
| Paper 3, sequential Birkhoff | conditional statistical theorem under uniform Young-tower assumptions | no primitive closed orbits; ordinary Birkhoff averages do not generate \(1/\log n\) |
| Paper 4, non-autonomous logistic spectrum | strong negative control for target leakage and chronology loss | zero-fitted scales/couplings and time-averaged transfer matrices cannot support an orbit trace |
| Paper 5, area-preserving Hénon | exact symplectic/reversible geometry, saddle, generating function, periodic action and monodromy interface | continuum Hamiltonian is approximate and patched; zero fit has no holdout; arithmetic coding is not proved to lift |
| Paper 6, Weil finite compression | structural benchmark: same finite Hermitian compression read from prime-power and spectral sides | manuscript is dated 2026-08-10 and not yet independently established; it is not itself a flow construction |

## Paper-by-paper findings

### Paper 1 — `1-The emergence of prime distribution from low-dimensional deterministic chaos.pdf`

- “prime sieve 与 band-merging Logistic kneading sequence 同构”在 p3--4、p7 被原文列作 conjecture，而非 theorem：`E1`。
- \(\mu_{LRL}\approx0.1037\)、Lyapunov/entropy/gap spectrum 等是模型内有限数值：`E2`，不能升级为算术同构。
- p14--16 先用 \(k=2C_2/\mu_{LRL}\approx12.73\) 设置系统，再把恢复 \(C_2\) 当验证；Paper 2 p21 也承认这会保证恢复常数：`E0` circular calibration。
- cylinder `LRL` 不是 primitive closed orbit，coupling equation 也不是 Gutzwiller/Selberg trace identity。

### Paper 2 — `2-Transient Chaos and Topological Bounds in Prime Dynamics.pdf`

- \(Q_3\) 在 \(n=31\)、\(Q_5\) 在 gap 113--127 的 MSS defect 可有限核验（p3--4）：`E4`。
- natural-prime sequence absolute admissibility 与 Parity--Gap implication（p4--7）是可用的结构负控；依赖 polylog maximal gap 的 eventual admissibility 必须标 `CONDITIONAL_THEOREM`。
- 扫到 \(k\le5000\) 仅见 3、5 两个 defect（p21--22）是 `E2`，不是渐近证明。
- 模型 \(P(2,2)\approx0.214\)，真实素数约 \(7\times10^{-6}\)，相差约 \(3\times10^4\)（原文量级约五位数量级，p21--23）；说明 1D skeleton 丢失 mod-3 等高模抑制。
- p9 “even-gap” lemma 把以 `L` 开头的 shift 相对以 `R` 开头的 kneading sequence 的次序方向写反；后续统一展开/谱隙/几何衰减链也未闭合。因此相关 theorem claims 不能作为已证结果。

### Paper 3 — `3-A Sequential Birkhoff Theorem.pdf`

- 主结果建立在 uniform inducing scheme、uniform spectral gap、Keller--Liverani stability 等 Assumption 1.1 上；a.e. convergence 还要 \(|u_n-u_c|=O((\log n)^{-\beta})\)、\(\beta>1\)（p2）：`E3`。
- p7 明确说明普通 Birkhoff average 只收敛到常数 cylinder frequency，不会产生 \(1/\log n\) envelope；envelope 需另加 shrinking target/weighted thinning/aging。
- monotone aging 升维为 autonomous skew product 时，clock 通常不回返，反而不利于闭轨层 A1。

### Paper 4 — `4-riemann_logistic_v4_fixed.pdf`

- \(\mu_c\) 由第一零点锚定（p3）；\(\epsilon\) 对前六零点优化（p6--9）；\(k_1,k_2\) 对目标谱做 Differential Evolution（p4、p19--20、p35）：全部属于目标泄漏，`E0/E1`。
- 参数随 \(N\) 显著漂移且无 sealed holdout。
- 核心对象 \(\bar P=T^{-1}\sum_tP_t\)（p6、p27）不是 time-ordered cocycle \(P_T\cdots P_1\)。它抹掉 chronology、return word 与 monodromy product，不能作为闭轨 trace 的证据。

### Paper 5 — `5-An Area-Preserving Henon-Map Model.pdf`

可继承的 exact geometry：

\[
F_a(x,y)=(1-ax^2-y,x),\qquad \det DF_a=1,
\]

且以 \(R(x,y)=(y,x)\) 有 \(RF_aR=F_a^{-1}\)。负支固定点是 hyperbolic saddle。一个 exact type-I generating function 为

\[
S(q,Q)=qQ-q+\frac a3q^3,
\]

因此 period-\(n\) cycle 有离散作用量 \(\sum_jS(q_j,q_{j+1})\) 和 monodromy \(\prod_jDF_a(z_j)\)：这些都是 `E4`，适合作为几何桥。

数值 tangency \(a_c\approx1.00561\) 是 `E2`，不是 uniform-hyperbolicity certificate。所谓 continuum Hamiltonian 使用二阶差分近似并人为加入 \(0.05q^4\)；\(\hbar_{\rm eff}\) 与 \(a_{\rm start}\) 对 100 个零点全局优化、没有 holdout；Floquet phase GUE-like 而重构能谱近 Poisson。最关键的是，没有证明 Logistic arithmetic coding 半共轭或嵌入到 Hénon。

最忠实的 flow bridge 是 exact suspension 或 kicked/stroboscopic Hamiltonian realization，而不是 continuum approximation。constant roof 能继承 primitive cycle、period、action 与 monodromy，但全部 period 仍为 \(n\tau\)，A0 被精确阻断。

### Paper 6 — `6-zeta-two-thirds.pdf`

其结构 benchmark 是

\[
p^r\le X\longrightarrow \Lambda(p^r)p^{-r/2}
\longrightarrow \text{same finite Hermitian compression }G
\longrightarrow \operatorname{tr}G,\operatorname{tr}(G^2),\text{ inertia}.
\]

这要求 flow analogue 在同一个对象内同时产生 primitive/repetition ledger 与 spectral readout，而不能比较两套分别拟合的矩阵。稿件日期为 2026-08-10，公开 Lean 仓库声称无 `sorry`/自定义 axiom，但外部复核时间仅数日；且 PDF Lemma 3.2 的 equality case 有打印错误（inequality/application 据称不受影响）。Stage 1 因而只把它列作 `E4-P` provisional benchmark，不把 headline 常数当已形成学界共识的定理。

## Consequence for Stage 1

旧路线没有提供通过 A0+A1 的 continuous-time survivor。可继承的是几何和失败模式：Hénon 的 exact symplectic orbit machinery 可以进入 suspension；Logistic 系列则作为 mod-3 缺失、目标校准、非自治平均和统计量冒充闭轨的负控。任何新 flow lift 都必须另证 arithmetic label preservation，而不能从“保面积”“混沌”或“GUE”推断。
