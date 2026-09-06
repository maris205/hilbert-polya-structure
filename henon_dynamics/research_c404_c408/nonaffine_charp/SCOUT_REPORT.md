# C404–C408：非仿射正特征 scout

日期：2026-09-06。基线 HEAD：`5b2a654c4f0b82b0e2d5158146b377ee6bf4e804`。

结论：检查三条方向，保留 **0 份论文契约**。这是选题门槛未通过，不是三类数学对象都不存在可研究问题；没有生成占位论文、分配候选编号、运行 evaluator、修改注册表或旧封存材料。

<a id="decision-table"></a>
## 1. 筛选结果

| Scout | 全量目标 | 结论 | 决定性理由 |
|---|---|---|---|
| A. 超奇异 isogeny 对应的非回溯素圈 zeta | 完整带 level 的 supersingular isogeny 图、所有圈长、正确 dual/diamond 约定 | `REJECT_FRAMEWORK_OWNED_NO_NEW_ARITHMETIC_LEMMA` | 定义及框架已有所有者；交叉审计发现来源的奇循环符号错误，故不认证印出的一般公式；本轮没有由此完成新算术引理 |
| B. 长度二 Witt 的非线性平移及 Frobenius twist | 所有奇素数、所有域扩张和迭代次数 | `REJECT_HIDDEN_GROUP_REDUCTION` | 写成多项式虽非仿射，实际正是 Witt 加法平移；twist 共轭于 Frobenius |
| C. 光滑 Markov 曲面的 Dehn twist + Frobenius | 所有奇素幂 q、κ∉{0,4}、整数 k、所有 n≥1 | `REJECT_INSUFFICIENT_INCREMENT` | 可给完整短证明，但结果只看 k 的奇偶；关键机制是经典圆锥纤维分解与 Lang 型一维方程，不足以支持高强度新论文 |

本轮先按 idea-creator 做对象/全量计数/既有所有权筛选，再按 proof-writer 检查 B、C 的真实量词与例外纤维。学术研究工作流只采用有界 primary-source scout 的问题定义、来源核验和反方检查部分；不是完整 Deep Research、外部专家审稿或全球查新认证。没有外传工作区资料、调用付费外部模型或启动长实验。

<a id="candidate-a"></a>
## 2. A：超奇异 isogeny 非回溯 zeta

精确范围取不同素数 p>3、ℓ，正整数 N 与 pℓ 互素，以及 B₁(N)⊆H⊆B₀(N)。顶点是代数闭包上 supersingular elliptic curves 连同 H-level structure 的同构类；边按目标自同构作商，dual 诱导的 reversal 必须连同 diamond 算子一起处理。对象是完整算术对应，不是抽取一个小邻接矩阵后的谱拟合。

预想增量是：正确处理半环、自同构权重和 reversal 不是无不动点 involution 的情形，得到全部 primitive non-backtracking cycles 的 zeta，并与模曲线 Hasse–Weil zeta 相连。Lau–Morrison–Orvis–Scullard–Zobernig 已提出这些对象、定义和证明框架；不能再把“首次引入这种 graph/zeta”当成本轮贡献。[S1 原始正文](https://arxiv.org/html/2509.15214v1)

最廉价的反例检查首先是定义检查：若 Jy=y，该一边闭路带 tail，不能作为长度一素圈；带 level 时 dual 的目标还会发生 diamond 位移。把普通 Ihara involution 硬套到全部参数会数错对象。访问论文定义 4.1–4.4、5.1–5.3 及其证明框架后，本轮不再把这一对象修正当成新贡献。未声称已解决 p=2,3 的额外情况，也未提出该例外范围的新契约。

**交叉审计后的重要限定：不能直接信任 S1 印出的一般循环乘积。** arithmetic scout 指出 Lemma 4.11 对奇长度 k>1 把 det(I+sP_k) 写成 1−sᵏ，而正确值是 1−(−s)ᵏ；本 lane 已独立复核 HTML、PDF 第 12–13 页和 k=3 反例。因此定理 4.12、6.9 中由该引理展开的奇循环因子不能在不校正/补充假设的情况下引用。详细的单顶点三环反例见 [SOURCE_AUDIT.md](SOURCE_AUDIT.md)。它证明抽象公式需要修正，但没有建立新的实际 supersingular 图的全族算术定理；简单循环矩阵符号修正也不满足本批论文准入标准。A 的最终拒绝依据是“框架所有权且没有新算术引理”，不是“该来源所有印出公式均已被认证正确”。

<a id="candidate-b"></a>
## 3. B：Witt 非线性为何不合格

对奇素数 p 定义整系数多项式

\[
C_p(X,U)=\frac{(X+U)^p-X^p-U^p}{p},\qquad
S_p(x,y)=(x+1,y-C_p(x,1))\pmod p.
\]

S_p 的坐标次数为 p−1≥2，不能凭这一点认为摆脱了群模型。它恰是 W₂ 的加法群上平移 (1,0)。Witt 加法由标准 ghost 方程定义；截断结构也是经典构造。[S2 §5.9–5.14、§7.1](https://arxiv.org/pdf/0804.3888)

完整结论在 [PROOF_PACKAGE.md](PROOF_PACKAGE.md) B 中证明：S_p^p(x,y)=(x,y+1)，S_p^{p²}=id，因此未 twist 的普通几何周期点数在 n=p² 已不是有限数。对 q=pᵃ、a≥1、k∈Z，若 F=S_p^k∘Fr_q，则对每个 n≥1，

\[
\#\operatorname{Fix}(F^n)(\overline{\mathbb F}_p)=q^{2n},
\qquad Z_F(z)=(1-q^2z)^{-1}.
\]

这是群平移的 Frobenius 共轭消去；也可由两层 Artin–Schreier 方程直接证明。相关一般 surjectivity 是经典 Lang–Steinberg 定理，Byszewski–Cornelissen–Houben §4.4.5–4.4.6 清楚标明其来源。[S3 正文](https://arxiv.org/pdf/2209.00085v2) 因而不保留为非群型算术新论文。

<a id="candidate-c"></a>
## 4. C：Markov 抛物 twist 的可证但过薄结果

固定奇素幂 q、κ∈F_q\{0,4}，令

\[
X_\kappa:x^2+y^2+z^2-xyz=\kappa,
\quad T(x,y,z)=(y,zy-x,z),\quad F=T^k\circ\mathrm{Fr}_q,
\quad k\in\mathbb Z.
\]

计数对象是整个 X_κ 的代数闭包上 F^n 的几何不动点，不是只数 F_q 上的 permutation，也不是去掉特殊纤维后重新命名成完整问题。令 ε=χ_q(κ−4)、η=χ_q(κ)，均为 ±1。对所有 n≥1，有限约化不动点集的大小是

\[
N_n=q^{2n}+1+2(q\varepsilon)^n+
\bigl(q(-1)^k\varepsilon\bigr)^n+
(q\varepsilon\eta)^n,
\]

因此

\[
Z_F(z)^{-1}=(1-q^2z)(1-z)(1-q\varepsilon z)^2
\bigl(1-q(-1)^k\varepsilon z\bigr)(1-q\varepsilon\eta z).
\]

完整推导见 [PROOF_PACKAGE.md](PROOF_PACKAGE.md) C：z=t∈F_{qⁿ}；分别计数 split/nonsplit 光滑圆锥、t²=κ 的相交直线和 t=±2 的平行直线。这些特殊纤维全部纳入，没有把 n 不能被 p 整除等限制偷偷加回来。k 可以为负数；有限测试只取正 k。

Goldman–Neumann 已给出该圆锥纤维分解及复数域上的有限商同调作用。[S4 §4 与 Theorem 1](https://www.math.columbia.edu/~neumann/preprints/wmgwdn2.pdf) **该文不是有限域公式的直接出处**；本轮证明是显式有限域计算，不能把复同调结论当作未经核验的正特征 Lefschetz 定理。拒绝理由是已知简单机制下的增量不足，**不是**已经确认文献中逐字存在上述公式。

九个独立构造 literal fixed equations 的 Gröbner 商环检查全部与公式一致，包括 q=3,n=2 的长度 118。商环方法计算的是代数闭包上的 scheme length；约化性由证明另行保证。结果不是九次“全周期验证”。

| p | κ | k | n | 商环长度 = 公式 |
|---|---|---|---|---|
| 3 | 2 | 1 | 1 | 10 |
| 3 | 2 | 2 | 1 | 16 |
| 3 | 2 | 1 | 2 | 118 |
| 5 | 1 | 1 | 1 | 16 |
| 5 | 1 | 2 | 1 | 6 |
| 5 | 2 | 1 | 1 | 26 |
| 7 | 1 | 1 | 1 | 64 |
| 7 | 2 | 1 | 1 | 36 |
| 7 | 3 | 2 | 1 | 36 |

要特别避免两种叙事越界：(i) 普通 T 的某些迭代有正维不动集，不等于整个 Markov 家族不可研究；(ii) 当前 parabolic+Frobenius 公式没有解决 hyperbolic Markov automorphism 的最长 F_p-轨道问题。Cerbu–Gunther–Magee–Peilen 的 Theorem 1.5 与 Conjecture 1.10 明确研究后一类不同对象。[S5 正文](https://arxiv.org/pdf/1610.07077) 本轮没有做足以确认该猜想截至 2026 年全部进展的专项查新。

<a id="audit"></a>
## 5. 去伪与复现边界

反方检查按三个时点完成：选题时先挑战“坐标非线性即非群型”；查文献时挑战“老报告没有包含即目前仍为空缺”；结案时挑战“算对九个例子即可把所有 n 和论文创新性一起认证”。A 的原始定义所有权、B 的显式群还原、C 的全例外纤维计算分别响应这些风险。随后另一 AI scout 作只读交叉审计，发现并触发了上面的 S1 引用限定；这不是独立人类专家共识，也不应继续沿用修订前的“字面定理直接覆盖”表述。

复现命令（在本目录）：`python -B exact_probe.py`。保存的 [exact_probe_results.json](exact_probe_results.json) 来自成功退出的本轮运行，Python 3.12.3 / SymPy 1.14.0。代码只用标准库与 SymPy，输出 stdout，不读取旧结果、不写注册表、不拟合目标谱。小算例不能替代本目录内的逐案证明；证明成立也不能替代创新性门槛。

详细来源访问范围、版本日期警告、检索边界在 [SOURCE_AUDIT.md](SOURCE_AUDIT.md)。最终建议仍是 **0 retained contracts**，不建议根代理因本批目标数量而把 B 或 C 扩成占位 PDF。
