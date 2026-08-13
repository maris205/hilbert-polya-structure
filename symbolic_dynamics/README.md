# Symbolic Dynamics Research Program

本目录是 Hilbert–Pólya 研究计划的 Symbolic Dynamics 路线入口。唯一主系统族是
**Symbolic Dynamics**；几何、Hamiltonian、quantum graph、scattering 或外部
operator-algebra 想法只记为 `ROUND2_CLUE`，不在当前路线展开。

当前研究项目为 **Ra-1: Arithmetic Symbolic Dynamics**。`Ra-1` 表示
Route-A roadmap 的当前阶段；项目名称只在本 README 中维护，不再增加项目包装目录。
全部可共享论文直接位于根目录的 [`papers/`](papers/) 中。

## 论文与简明结论

| 论文项目 | 可共享论文 | 简明结果 | 状态 |
|---|---|---|---|
| [01-falsification-first-audit](papers/01-falsification-first-audit/README.md) | [PDF](papers/01-falsification-first-audit/main.pdf) · [LaTeX/实验/材料](papers/01-falsification-first-audit/) | 独立审计六个 symbolic 候选；没有一个同一对象通过 A0–A4，六项 Route B 均关闭。有限状态、有限记忆、有限维 cocycle determinant 的 divisor 计数为 $O(R)$，与完成 Riemann 函数的 $R\log R$ 量级不相容。 | **COMPLETE / FROZEN** |
| [02-wheel-sieve-stationarization-obstructions](papers/02-wheel-sieve-stationarization-obstructions/README.md) | [PDF](papers/02-wheel-sieve-stationarization-obstructions/main.pdf) · [LaTeX/证明/材料](papers/02-wheel-sieve-stationarization-obstructions/) | 证明 strict extension 不能产生周期点；forward-well-founded strong-bisimulation quotient 仍无环；保留 state-class exact-$q$ 标签的 quotient 继承严格分层；finite-alphabet fixed-window decoder 不能恢复无界精确 prime clock。 | **THEOREM SCREENING COMPLETE** |
| [03-wheel-sieve-periodic-clock-obstruction](papers/03-wheel-sieve-periodic-clock-obstruction/README.md) | [PDF](papers/03-wheel-sieve-periodic-clock-obstruction/main.pdf) · [LaTeX/证明/审稿](papers/03-wheel-sieve-periodic-clock-obstruction/) | 精确 autonomous clock decoder 强制 factor 纤维保持同一 level，因此 direct image 继承严格分层且无周期点；连续 closure decoder 在 lag-pair 与对角线分离时同样排除边界周期点。clock erasure 或 compactification 虽能制造周期点，却不能继承普通拓扑下的精确 $q/\log q$ clock。 | **COMPLETE / THEOREM STOP** |
| [04-tensor-prime-symbolic-euler-product](papers/04-tensor-prime-symbolic-euler-product/README.md) | [PDF](papers/04-tensor-prime-symbolic-euler-product/main.pdf) · [LaTeX/实验/Route-A 记录](papers/04-tensor-prime-symbolic-euler-product/) | 有限 full shifts 满足 $F_m\otimes F_n\cong F_{mn}$ 且 $h(F_n)=\log n$，所以 tensor atoms 内生地等于 $F_p$。其 canonical atom-loop shift 在 $\Re s>1$ 上满足 $\det(I-\mathcal L_s)=1/\zeta(s)$，并精确给出 prime-power/$\Lambda$ ledger；这是本项目第一条同对象 A0–A2 exact chain。 | **ROUTE-A ANALYTIC CANDIDATE** |
| [05-intrinsic-symbolic-grading-and-duality](papers/05-intrinsic-symbolic-grading-and-duality/README.md) | [PDF](papers/05-intrinsic-symbolic-grading-and-duality/main.pdf) · [LaTeX/证明/实验/Route-A 记录](papers/05-intrinsic-symbolic-grading-and-duality/) | tensor-divisor homology 内生给出 $\mu(n)$ 与 odd atom degree，因此 exterior supertrace 为 $1/\zeta$、odd Berezinian 为 $\zeta$，解决 A2 determinant orientation。honest Koszul resolution 却消去到 vacuum；reversal 只给 $s\mapsto s$，group inversion 只给 $s\mapsto-s$；首个临界带 $\det_3$ 虽对称却 zero-free 且删除 $r=1,2$。 | **GO A2 / STOP A3（当阶段未新编号）** |
| [06-binary-parry-archimedean-factor](papers/06-binary-parry-archimedean-factor/README.md) | [PDF](papers/06-binary-parry-archimedean-factor/main.pdf) · [LaTeX/证明/实验/Route-A 记录](papers/06-binary-parry-archimedean-factor/) | 唯一最小 tensor atom $F_2$ 的 Parry 核把 Euler 与 Gaussian 通道统一到 $\operatorname{tr}H(z)^r=(\cosh z)^r$：$z=0$ 保留完整 prime-power ledger，扩散尺度给自对偶 Gaussian，其 Mellin 变换为 $\pi^{-s/2}\Gamma(s/2)$。这形成同源 Mellin–Fredholm 分解；但 block-preserving chiral family 沿临界线完全等谱，仍没有单一 completed determinant。 | **GO A3 / STOP GLOBAL COMPLETION / SD-C08** |

### 论文 1 的候选分离结论

- `SD-C05` 是最强 endogenous rational-prime generator，但其 level shift 无周期轨道。
- `SD-C04` 有最自然的 Fredholm determinant，但 primitive species 是 modular/
  quadratic-irrational orbit，不是 rational primes。
- `SD-C06` 有最强的精确 zeta-quotient 碰撞，但没有同一对象的 primitive-orbit
  Fredholm ledger；Liouville sign 仍是额外 arithmetic observable。
- 三者的优点不能 coordinatewise 拼接成一个候选。

### 论文 3 的 theorem stop

对“周期 target 逐点、单值、自治地继承 levelwise wheel prime clock”这一分支，
Paper 03 给出 `THEOREM_STOP`；继续增大 cutoff 或搜索 quotient cycle 已无意义。
仍开放的同族方向只能是一个**不同的、target-intrinsic arithmetic invariant**，
而不是对原 exact clock 的保真 factor。它必须重新 source-lock：冻结 phase space、
transition rule、arithmetic decoder、clock、primitive/repetition ledger 和 function
space，并从 A0 重新审计；不自动继承 `SD-C05` 的 arithmetic credit。论文 4 已按
这一规则启用一个全新的内生不变量，而没有继承 wheel-sieve credit。

### 论文 4：第一条 A0–A2 同对象链

`SD-C07` 不再把素数看成 sieve level 的输出，而把它们看成有限 full shifts 在
Cartesian tensor 下的不可分解对象。这个选择同时内生给出：

- $F_p$ 作为 tensor atom；
- $F_p^{\otimes r}=F_{p^r}$ 作为重复结构；
- $h_{\rm top}(F_p)=\log p$ 作为 clock；
- atom-loop suspension 的 genuine primitive orbit；
- $\ell^2(\operatorname{At})$ 上的 trace-class transfer operator；
- $Z_\otimes=\zeta$、$D_\otimes=1/\zeta$ 和精确 von Mangoldt ledger。

有限 opaque registry 在 $N=32,64,128,256$ 全部精确通过；$N=256$ 恢复
54/54 个 tensor atoms，并使 $\zeta$、$\mu$、$\Lambda$ 系数前缀全部为 1.000
准确。additive、64 组 matched-random、shifted-law 与 28 组 free-mixing controls
均按预注册逻辑失败。特别地，任何正的 cross-atom mixing 都在 $pq$ 处产生错误的
$\Lambda(pq)>0$ 项，因此 diagonal recurrent core 是精确正权 Euler ledger 的结构
要求，而不只是方便的建模选择。

当前 tuple 为

```text
(A0_ANALYTIC_ARITHMETIC_ORIGIN,
 A1_PASS_ANALYTIC,
 A2_ANALYTIC_DETERMINANT,
 A3_PARTIAL_ANALYTIC_STRUCTURE,
 A4_FAIL)
```

A3 的缺口非常具体：ungraded $\mathcal L_s$ 只在 $\Re s>1$ trace class，
没有内生 Gamma factor、函数方程或 Weil compression，而且不可能作为 holomorphic
trace-class family 穿过 zeta 零点。论文 5 已按 source lock 完成分级与 duality
审计：determinant orientation 可以内生解决，但临界带 completion 不能由朴素
Koszul、reversal 或 group completion 获得。

### 论文 5：分级成功，completion 定理停止

对 open tensor-divisor interval 的 order complex，论文 5 证明

$$
\widetilde H_j(\Delta_n;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&n\text{ squarefree},\ j=\omega(n)-2,\\
0,&n\text{ nonsquarefree}.
\end{cases}
$$

所以 tensor atoms 在 reduced degree $-1$ 中为 odd，homology supertrace 精确等于
$\mu(n)$。在 $\Re s>1$，

$$
\operatorname{Str}_{\Lambda^\bullet V}\Gamma_-(\mathcal L_s)=\frac1{\zeta(s)},
\qquad
\operatorname{Ber}_{V_{\bar1}}(I-\mathcal L_s)=\zeta(s).
$$

这一步真正修复了 A2 的 determinant orientation；$N\le512$ 的 511 个 complexes
全部 exact 通过 $\partial^2=0$、Euler、homology 和 coefficient ledger。

但 honest equivariant Koszul resolution 的 bosonic/fermionic factors 完全抵消，
只留下 $\operatorname{Str}T_s=1$。自然 symbolic reversal 保持 $s$，tensor-group
inversion 只产生 $-s$。即使暂时允许外加 $s\leftrightarrow1-s$ pairing，第一种
能覆盖临界线的 regularization 是

$$
D_3(s)=\det\nolimits_3(I-\mathcal L_s)
       \det\nolimits_3(I-\mathcal L_{1-s}),
\qquad \frac13<\Re s<\frac23,
$$

但它在该 strip 内 zero-free，而且 logarithm 从 $r=3$ 才开始，恰好删除 prime 和
prime-square traces。于是阶段结论为
**GO_A2_GRADED_ORIENTATION / STOP_A3_COMPLETION**；SD-C07 保留，不分配
SD-C08（限论文 5 当阶段），Route B 继续锁定。

论文 6 已完成这项测试，并把 SD-C08 推进到 A3 的 Archimedean factor。下一步
不再重复寻找 Gamma，而是直接攻击剩余的单点瓶颈：构造一个**质量不对易但
ledger-exact** 的 symbolic coupling，使同一非渐近 trace/determinant 同时容纳
tensor-atom repetitions 与 binary sign fluctuations。它必须内生消去所有 mixed
$pq$ cycles，并击败 biased-binary、radial $K_3/K_4$ 和 reversible-$\lambda$
controls；否则不进入新的候选编号。

### 论文 6：同一 tilted trace 的 Euler–Gamma 双通道

令 $K_2=J_2/2$、$Q=\operatorname{diag}(1,-1)$，并定义

$$
H(z)=e^{zQ/2}K_2e^{zQ/2}.
$$

则对每个 $r\ge1$，

$$
\operatorname{tr}H(z)^r=(\cosh z)^r.
$$

$z=0$ 给 $\operatorname{tr}K_2^r=1$，因而保持 Paper 04 的精确 Euler/Fredholm
ledger；$z=iu/\sqrt r$ 则趋向 $e^{-u^2/2}$。在 Fourier 自对偶归一化下，极限
Gaussian 的绝对 Mellin 变换精确为 $\pi^{-s/2}\Gamma(s/2)$。因此在
$\Re s>1$ 得到同源但非单行列式的

$$
\mathfrak Z_{\rm SD}(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s).
$$

同时证明了一个结构二难：只要 Hellinger chiral coupling 保持 atom blocks、与
tensor-mass 对易，它在 $s=1/2+it$ 上就与 $t=0$ 酉共轭，谱不随高度运动；若要
产生 spectral motion，就必须跨 atom 混合，而普通正混合会重新制造错误的 mixed
primitive cycles。阶段结论为 **GO_A3_ARCHIMEDEAN_FACTOR /
STOP_GLOBAL_COMPLETION**，Route B 仍锁定。

## 目录

- [研究提案](propose-symbolic-dynamics.md)
- [Route-A evaluator](skills/route-a-evaluator.md)
- [Route-B evaluator](skills/route-b-evaluator.md)
- [prior-work 与共享文档](docs/)
- [六篇论文](papers/)

根目录不再设置项目包装层；每个论文项目各自使用 `PAPER_MANIFEST.sha256` 管理
完整性。本地 PDF/legacy 输入语料和运行缓存不进入 manifests。
