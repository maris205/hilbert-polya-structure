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
| [06-binary-parry-archimedean-factor](papers/06-binary-parry-archimedean-factor/README.md) | [PDF](papers/06-binary-parry-archimedean-factor/main.pdf) · [LaTeX/证明/实验/Route-A 记录](papers/06-binary-parry-archimedean-factor/) | 唯一最小 tensor atom $F_2$ 的 Parry 核把 Euler 与 Gaussian 通道统一到 $\operatorname{tr}H(z)^r=(\cosh z)^r$：$z=0$ 保留完整 prime-power ledger，扩散尺度给自对偶 Gaussian，其 Mellin 变换为 $\pi^{-s/2}\Gamma(s/2)$。这形成同源 Mellin–Fredholm 分解；但任意单侧 phase chiral ansatz 都沿临界线 gauge-equivalent，仍没有单一 completed determinant。 | **GO A3 / STOP GLOBAL COMPLETION / SD-C08** |
| [07-entropy-oriented-chiral-shift](papers/07-entropy-oriented-chiral-shift/README.md) | [PDF](papers/07-entropy-oriented-chiral-shift/main.pdf) · [LaTeX/证明/实验/Route-A 记录](papers/07-entropy-oriented-chiral-shift/) | 以 tensor-prime entropy 次序定义只向前的 successor coupling；其非对易 transfer 保留所有 $p^r$ traces 与 Euler determinant，同时 endpoint-symmetric chiral double 在临界线上产生严格、非 gauge 的谱运动和可解的两原子 crossings。运动位于 trace-invisible triangular radical，且任意 forward DAG 都能复制，尚未让同一个 determinant 的算术 divisor 运动。 | **GO A3 CHIRAL MOTION / STOP UNIFIED DIVISOR / SD-C09** |
| [08-positive-cone-recurrent-trace](papers/08-positive-cone-recurrent-trace/README.md) | [PDF](papers/08-positive-cone-recurrent-trace/main.pdf) · [LaTeX/证明/实验/Route-A 记录](papers/08-positive-cone-recurrent-trace/) | 在强连通的 tensor-prime base 上，directed-positive cocycle 用群迹精确消去全部 mixed closed words，使 recurrent base 仍给出 $1/\zeta$ 的局部解析 $\tau$-determinant；但 adjoint/chiral 反射会在二阶立即恢复 $gg^{-1}$ backtracking，而 $\det_3$ 只能通过删掉这一发散项才存在。 | **GO RECURRENT $\tau$-EULER / STOP UNIFIED DIVISOR / SD-C10** |
| [09-holomorphic-reflection-double](papers/09-holomorphic-reflection-double/README.md) | [PDF](papers/09-holomorphic-reflection-double/main.pdf) · [LaTeX/证明/实验/Route-A 记录](papers/09-holomorphic-reflection-double/) | 不取伴随的全纯反射 double 在 $1/3<\Re s<2/3$ 上有精确 $s\leftrightarrow1-s$ 对称，但 identity-visible 闭词强制 $p^{-s}p^{-(1-s)}=p^{-1}$，故整个 $\det_3$ 沿竖直方向完全不动；任何可见运动都需要 $p\ne q$ 的 mixed pairing 并破坏 Euler ledger。 | **REFLECTION RIGIDITY / STOP VERTICAL DIVISOR / SD-C11** |
| [10-entropy-paired-relative-determinant](papers/10-entropy-paired-relative-determinant/README.md) | [PDF](papers/10-entropy-paired-relative-determinant/main.pdf) · [LaTeX/证明/实验/Route-A 记录](papers/10-entropy-paired-relative-determinant/) | 相邻 entropy-rank 原子的 odd/even 配对使相对 transfer 对所有 $\Re s>0$ 都是 trace class，产生反射对称且可运动的相对行列式；但它是 zero-free 的 alternating Euler product，用符号帐本替换了目标正权 prime-power ledger，并被任意递增库存复制。 | **ROUTE-A REJECTED / PROVES TOO MUCH / SD-C12** |
| [11-unitary-fiber-moment-rigidity](papers/11-unitary-fiber-moment-rigidity/README.md) | [PDF](papers/11-unitary-fiber-moment-rigidity/main.pdf) · [LaTeX/证明/实验/Route-A 记录](papers/11-unitary-fiber-moment-rigidity/) | 对有限维 unitary/Bloch fiber，faithful positive normalized trace 中 $\tau(U)=1$ 已强制 $U=I$；非忠实状态或 graded 复制可隐藏谱运动，但 ordinary determinant 会看见它，而 Berezinian 又将它完全消去，recurrent finite-path 构造则总在某个重复阶数泄漏。 | **POSITIVE-MOMENT RIGIDITY / ROUTE-A REJECTED / SD-C13** |
| [12-fourier-null-haar-fiber](papers/12-fourier-null-haar-fiber/README.md) | [PDF](papers/12-fourier-null-haar-fiber/main.pdf) · [LaTeX/证明/实验/Route-A 记录](papers/12-fourier-null-haar-fiber/) | 所有正次 Fourier moments 都等于 $1$ 的有限正圆周测度唯一形如 $\delta_1+c\,m_{\rm Haar}$；这个无限维 diffuse escape 保留 Euler ledger，却被原标量全纯 trace-log determinant 完全消去。归一化、有限近似、selfadjointization 或 inverse coupling 都会分别破坏 ledger、迟发泄漏或产生 balanced mixed words。 | **HAAR ESCAPE / DETERMINANT INVISIBILITY / SD-C14** |
| [13-character-resolved-holonomy](papers/13-character-resolved-holonomy/README.md) | [PDF](papers/13-character-resolved-holonomy/main.pdf) · [LaTeX/证明/实验/Route-A 记录](papers/13-character-resolved-holonomy/) | positive-cone $\mathbb Z$-skew extension 把 reciprocal Euler product 精确放在 deck-neutral Fourier coefficient，并让同一 parent lift 的非零 Bloch modes 看见 recurrent mixed returns；但没有任何单独 character fiber 保持 Euler ledger，全部 nonprime/random controls 也会运动，而 inverse reversal 在二阶污染零模。 | **CHARACTER RESOLUTION / ROUTE-A REJECTED / SD-C15** |
| [14-tensor-bar-mobius-selector](papers/14-tensor-bar-mobius-selector/README.md) | [PDF](papers/14-tensor-bar-mobius-selector/main.pdf) · [LaTeX/证明/实验/Route-A 记录](papers/14-tensor-bar-mobius-selector/) | 函子性 Abelian charge 被严格分类为 atom valuations，divisor-category cocycle 全为 coboundary；转向全局 tensor-bar grammar 后，同一 signed symbolic determinant 在 $\Re s>1$ 的 endpoint completion 中精确给出 $1/\zeta$ 与 $\Lambda_\otimes=\mu_\otimes*h$。但该反演对任意 weighted inventory 都成立，且 primitive cycles 是 factorization necklaces 而非 primes。 | **TENSOR-BAR DETERMINANT / ROUTE-A REJECTED / SD-C16** |
| [15-bar-koszul-primitive-no-lift](papers/15-bar-koszul-primitive-no-lift/README.md) | [PDF](papers/15-bar-koszul-primitive-no-lift/main.pdf) · [LaTeX/证明/实验/Route-A 记录](papers/15-bar-koszul-primitive-no-lift/) | bar–Koszul squarefree subset shift 的标量 determinant 仍为 $\prod_p(1-x_p)$，但 $p^2q^2$ 的 primitive 账本为 $1^+$ 对 $2^-$，只能借低阶 $pq$ 轨道的二次重复抵消；$pqr$ 的残差为 $\mathbf1\oplus\mathrm{sgn}-\mathrm{Std}$，排除 $S_3$-自然的 sign involution。 | **PRIMITIVE NO-LIFT / ROUTE-A REJECTED / SD-C17** |
| [16-equivariant-cycle-index-determinant](papers/16-equivariant-cycle-index-determinant/README.md) | [PDF](papers/16-equivariant-cycle-index-determinant/main.pdf) · [LaTeX/证明/实验/Route-A 记录](papers/16-equivariant-cycle-index-determinant/) | Burnside/cycle-index ledger 精确保留 $pqr$ 的 character residual $(0,0,3)$，但算术权重 $x_p=p^{-s}$ 使固定 transfer 的置换 stabilizer 退化为恒等；等权恢复对称时非平凡 isotypes 全被 rank-one transfer 杀掉，而 diagonal equivariant lift 又引入 mixed-subset Euler factors。 | **FORMAL EQUIVARIANT LEDGER / ROUTE-A REJECTED / SD-C18** |
| [17-fiber-cocycle-artin-factor](papers/17-fiber-cocycle-artin-factor/README.md) | [PDF](papers/17-fiber-cocycle-artin-factor/main.pdf) · [LaTeX/证明/实验/Route-A 记录](papers/17-fiber-cocycle-artin-factor/) | 真正 commuting 的 $C_2$ fiber 在同一 subset shift 中给出 Artin blocks $D_+=1/\zeta(s)$、$D_-=\zeta(s)/\zeta(2s)$ 与 whole determinant $D_{\rm reg}=1/\zeta(2s)$；但 mixed primitive lifts 仍大量存在，全部 matched inventories 也精确复制该分解。 | **ARTIN FACTOR / ROUTE-A REJECTED / SD-C19** |
| [18-incidence-transition-holonomy](papers/18-incidence-transition-holonomy/README.md) | [PDF](papers/18-incidence-transition-holonomy/main.pdf) · [LaTeX/证明/实验/Route-A 记录](papers/18-incidence-transition-holonomy/) | subset-incidence transition rule 产生了真正非交换、非 one-letter-coboundary 的 $S_3$ holonomy；trivial/sign blocks 仍保留标量 Euler factor，但 faithful standard block 精确泄漏 mixed primitive coefficients，且全部 matched inventories 都复制该现象。 | **GENUINE TRANSITION HOLONOMY / ROUTE-A REJECTED / SD-C20** |
| [19-stationary-semiring-sieve-shift](papers/19-stationary-semiring-sieve-shift/README.md) | [PDF](papers/19-stationary-semiring-sieve-shift/main.pdf) · [LaTeX/证明/实验/Route-A 记录](papers/19-stationary-semiring-sieve-shift/) | full-shift alphabet-sum、tensor 与 order 可把无 factor oracle 的逐商试除编译成一个 trace-class 单边 Markov graph，并在 $\Re s>1$ 精确给出 $1/\zeta(s)$；但全部计算状态都属 transient DAG，剪枝后只剩 Paper 04 的 prime loops，而任意总可判定集合都能复制同型 Euler 子积。 | **SEMIRING VERIFIER / PRUNING EQUIVALENT / ROUTE-A REJECTED / SD-C21** |
| [20-recurrent-verifier-clock-dilution](papers/20-recurrent-verifier-clock-dilution/README.md) | [PDF](papers/20-recurrent-verifier-clock-dilution/main.pdf) · [LaTeX/证明/实验/Route-A 记录](papers/20-recurrent-verifier-clock-dilution/) | 把完整试除计算闭成 prime cycle 后，每圈仍精确携带 $\log p$，但验证长度 $\ell(p)\asymp p\log p$ 会把 clock 稀释到至少一条边权趋于 $1$；whole adjacency 因而 essential norm 为 $1$、非紧且没有 Fredholm determinant。$z=1$ 的 orbit product 虽仍是 $1/\zeta$，Poincaré return 却把系统收缩回 Paper 04 的 diagonal atom loops。 | **CLOCK DILUTION / FIRST-RETURN COLLAPSE / ROUTE-A REJECTED / SD-C22** |
| [21-successor-divisor-cycle-flood](papers/21-successor-divisor-cycle-flood/README.md) | [PDF](papers/21-successor-divisor-cycle-flood/main.pdf) · [LaTeX/证明/实验/Route-A 记录](papers/21-successor-divisor-cycle-flood/) | successor–divisor grammar $n\to d\iff d\mid n+1$ 给出强连通、mixing 的 genuine recurrent shift，且自然 whole adjacency 精确满足 $L_s\in\mathcal S_1\iff\Re s>1/2$；但它没有长度一轨道，并从每个长度 $k\ge2$ 都产生 canonical primitive cycle，所有自然 orbit norms 又是 composite squares。 | **SHARP FREDHOLM / ALL-LENGTH CYCLE FLOOD / ROUTE-A REJECTED / SD-C23** |
| [22-cofactor-holonomy-fredholm-trilemma](papers/22-cofactor-holonomy-fredholm-trilemma/README.md) | [PDF](papers/22-cofactor-holonomy-fredholm-trilemma/main.pdf) · [LaTeX/证明/实验/Route-A 记录](papers/22-cofactor-holonomy-fredholm-trilemma/) | successor–divisor edge 的 intrinsic cofactor $q=(n+1)/d$ 精确分类 closed-path holonomy；$Q=2$ 当且仅当轨道是 $C_k=(k,\ldots,2k-1)$。two-parameter adjacency 的 sharp domain 为 $\Re s>1/2$ 且 $\Re(s+u)>1/2$，但 pure cofactor 非紧、endpoint regularization 阶乘衰减、unitary character 只改相位。 | **HOLONOMY RESOLUTION / FREDHOLM TRILEMMA / ROUTE-A REJECTED / SD-C24** |

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

论文 6 已完成这项测试，并把 SD-C08 推进到 A3 的 Archimedean factor；论文 7
随后构造了质量不对易但 ledger-exact 的 successor coupling。因而当前瓶颈已从
“能否产生谱运动”推进为“能否让同一个解析 determinant 同时看见 Euler divisor
与运动 sector”。

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

同时证明了一个更强的 gauge 定理：对任意有界 $K$，单侧相位族
$A_t=G^{1/2+it}K$ 的 chiral double 都与 $t=0$ 酉共轭；这一结论不需要
$[G,K]=0$。因此质量非对易本身不够，必须让相位从至少两个不能被同一个块酉
吸收的端点通道发生干涉。阶段结论为 **GO_A3_ARCHIMEDEAN_FACTOR /
STOP_GLOBAL_COMPLETION**，Route B 仍锁定；论文 7 已沿这个精确缺口前进。

### 论文 7：Euler 账本不动，临界谱开始运动

按 entropy 严格递增排列 tensor atoms，并令 $S e_n=e_{n+1}$。论文 7 冻结

$$
L_s=D_s+\frac12(D_sS+SD_s),
\qquad D_se_n=p_n^{-s}e_n.
$$

successor edges 永远不能回到原 level，所以它们不进入任何周期词。由此在
$\Re s>1$ 精确得到

$$
\operatorname{Tr}L_s^r=\sum_p p^{-rs},
\qquad
\det(I-zL_s)=\prod_p(1-zp^{-s}),
$$

同时 $L_s$ 真正混合不同 entropy blocks。将两个端点反射成

$$
\mathcal B_s=
\begin{pmatrix}0&L_s\\L_{1-s}^{\mathsf T}&0\end{pmatrix}
$$

后，$\mathcal B_{1/2+it}$ 自伴，$\det_3(I-z\mathcal B_s)$ 在
$1/3<\Re s<2/3$ 具有精确 $s\leftrightarrow1-s$ 对称，而且其第四 Schatten
trace 随 $t$ 严格运动。两原子截断甚至给出零数据、零拟合的 crossing 公式

$$
\det(I-L_t^*L_t)
=\frac{3-2\sqrt6\cos(t\log(3/2))}{24}.
$$

但这个突破同时暴露出新的唯一瓶颈：任意只向前的 DAG、随机 endpoint phases、
shuffled/composite/random inventories 都可保留全阶 triangular ledger 并产生奇异谱
运动。运动属于 determinant 看不见的 radical；Euler Fredholm determinant 与
moving chiral $\det_3$ 仍是两个解析对象。故阶段结论为
**GO_A3_CHIRAL_MOTION / STOP_UNIFIED_DIVISOR**，Route B 继续锁定。

### 论文 8–12：recurrent mixing 的三重两难

第二批五篇把 Paper 07 的“trace-invisible motion”逐步压缩成一个更明确的
Symbolic-Dynamics 障碍：

- conical cocycle 或 forward radical 可以让 recurrent/mixed grammar 保留精确 Euler
  ledger，但它们的运动被目标 holomorphic determinant 屏蔽；
- adjoint、inverse labels 或任何真正可见的 recurrent return 会重新产生
  $gg^{-1}$ / balanced mixed words，立即污染 prime-power ledger；
- $s\leftrightarrow1-s$ 反射、relative pairing 或有限 unitary fibers 可以制造对称、
  运动或延迟泄漏，但不能同时保留 all-positive ledger 和可见 divisor。

当前最强的正面结论仍是 SD-C08/09/10 累积的 A0–A3 局部结构：同一
tensor-prime 源已内生给出 Euler ledger、Gamma shadow、$1/2$ center、反射对称
和非 gauge 谱运动；尚缺的只是一个**同一解析不变量**，能让运动 sector
真正改变 Euler divisor，又不引入 mixed composite orbits。

### 论文 13：character resolution 成功，单 fiber completion 失败

论文 13 已执行上述 character-resolved 测试。令 $U$ 为 deck shift，并冻结

$$
\widetilde L_s=D_s\otimes1+A_s\otimes U,
\qquad L_s(w)=D_s+wA_s.
$$

在 $\Re s>1$，每个 Bloch fiber 都是 trace class，parent lift 对
$\operatorname{Tr}\otimes\tau_{\mathbb Z}$ 是 semifinite trace class；而且

$$
[w^0]\det(I-zL_s(w))=\prod_p(1-zp^{-s}).
$$

这是真正的同 parent-object 推进：Paper 12 中被 Haar 平均删除的 sector 现在在
非零 character modes 中可见。但精确 target 只属于 deck-neutral conditional
expectation；对任何 $|w|=1$，二阶 trace 已含 mixed return。最小两原子式

$$
\det(I-zL(w))=(1-zx)(1-zy)-z^2a^2w^2
$$

同时证明了可见性和 `PROVES_TOO_MUCH`：composite、shuffled、random-increasing
以及全部 32 个 positive-random-charge controls 都有非零响应。把反向 charge 改为
inverse 又会把该项移回 $w^0$，在 $r=2$ 破坏 Euler ledger。因此结论是
**GO_EQUIVARIANT_EULER_LEDGER / GO_CHARACTER_RESOLUTION / STOP_UNIFIED_BLOCH_FIBER /
STOP_ARITHMETIC_SELECTIVITY / STOP_TIME_REVERSAL**，Route B 继续锁定。

下一步仍只在 Symbolic Dynamics 内，但不再盲扫 character：应分类所有能由
tensor multiplication、entropy grammar 与有限描述 transition rule 函子性产生的
integer cocycles。只有当某个 cocycle 的首个非零 Fourier coefficient能在运行前证明
对 composite/shuffled/random inventories 消失、而对 tensor-prime atoms 非零时，才值得
建立下一候选；纯 adjacency、positive charge、rank 或 entropy coboundary 规则已经被
Paper 13 定理级排除。

### 论文 14：局部 character 关闭，全局 tensor-bar determinant 成立

Paper 14 完成了 Paper 13 留下的 character 分类。对 full-shift tensor monoid，任意
Abelian monoidal charge 都唯一写成

$$
q(F_n)=\sum_p v_p(n)q(F_p).
$$

若它在所有 composite 上为零，则 $2q(F_p)=3q(F_p)=0$ 强制
$q(F_p)=0$；thin tensor-divisor category 上的 coherent cocycle 也全部是 coboundary。
因此有限局部、有限状态或普通 character holonomy 不能同时选出 tensor atoms、保留
prime-power repetitions 并对 matched controls 消失。完整枚举中，18 个预注册规则、
256 个 radius-one truth tables 与 260 个一至二状态 transducers 的 robust pass 均为零。

正面逃生口是一个真正全局的 reduced tensor-bar code。令边为非空 ordered tensor
words，clock 为 entropy sum，ordinary scalar sign 为 $(-1)^{k+1}$。在
$\Re s>\sigma_{\rm bar}$、$\zeta(\sigma_{\rm bar})=2$ 时，raw edge transfer 为

$$
F_{\rm bar}(s)=\frac{\zeta(s)-1}{\zeta(s)},
\qquad
D_{\rm bar}(s,z)=1-zF_{\rm bar}(s).
$$

按 tensor endpoint 先分组后，公式在 $\Re s>1$ 绝对收敛，并满足

$$
D_{\rm bar}(s,1)=\frac1{\zeta(s)},
\qquad
\frac{d}{ds}\log D_{\rm bar}(s,1)
=\sum_n\Lambda_\otimes(n)n^{-s},
\qquad \Lambda_\otimes=\mu_\otimes*h.
$$

512 个 formal coefficients、960 个 incidence rows、trace-log 至 repetition 256
全部通过 exact 或高精度检查；但 10 组 generic/composite/random/synthetic inventories
也全部精确反演。更关键的是，负号是 ordinary scalar edge weight，重复时变成
$\epsilon^r$；它不是 odd supertrace parity。Euler ledger 因而可能跨 primitive 与
repetition 层抵消，尚未形成 $p\leftrightarrow\gamma_p$ 的 orbitwise 对应。阶段结论是
**GO_TENSOR_MOBIUS_INCIDENCE_DETERMINANT / STOP_ARITHMETIC_SELECTIVITY /
STOP_ORBITWISE_PRIME_CORRESPONDENCE**。Paper 15 已直接审计 primitive 层的
sign-reversing reduction，而没有重新扫描局部 character。

### 论文 15：标量 Euler 恒等式不能提升为自然的逐 primitive 消去

Paper 15 把 Paper 14 的 ordered bar code 做标准 bar–Koszul reduction。对有限
tensor-atom 集 $P$，临界字母不是只有 atoms，而是所有非空 squarefree subsets
$S\subseteq P$，其标量符号为 $(-1)^{|S|+1}$。因此 one-vertex signed shift 仍满足

$$
1-\sum_{\varnothing\ne S\subseteq P}(-1)^{|S|+1}x_S
=\prod_{p\in P}(1-x_p),
$$

并在 $x_p=p^{-s}$、$\Re s>1$ 时给出 $1/\zeta(s)$。但这个标量恒等式没有
orbitwise lift。两原子 $p,q$ 的 content $p^2q^2$ 只有一个正 primitive necklace，
却有两个负 primitive necklaces；完整 logarithmic coefficient 之所以为零，是因为
content $pq$ 的两个 primitive cycles 的二次重复各再贡献 $1/2$。抵消必然跨越
primitive/repetition 层。

自然性给出第二个独立障碍。content $pqr$ 的正、负 $S_3$-sets 的轨道大小分别为
$1\sqcup2$ 与 $3$，其 virtual character 为

$$
\mathbf1\oplus\mathrm{sgn}-\mathrm{Std},
\qquad \chi(e,(12),(123))=(0,0,3).
$$

所以不存在 $S_3$-equivariant sign-reversing involution。honest bar/Koszul
quasi-isomorphism又必须保留 $\Lambda^{\ge2}V$ 的 mixed homology；若把额外 recurrence
放进 equivariantly contractible pairs，其全部 power supertraces 为零、superdeterminant
为 $1$，因而对目标 determinant 完全不可见。10/10 exact tests、112/112 随机有理
inventory controls 均通过，进一步确认该恒等式是通用组合机制而非 arithmetic selector。

阶段结论为 **GO_BAR_KOSZUL_SQUAREFREE_REDUCTION /
STOP_PRIMITIVE_BEFORE_REPETITION / STOP_NATURAL_SIGN_INVOLUTION /
PROVES_TOO_MUCH**。下一步 Paper 16 只追踪尚未被 scalar augmentation 看见的
Burnside/representation-valued cycle-index residual，检验它能否成为同一算术
Fredholm object 的 character mode；Route B 继续锁定。

### 论文 16：等变 residual 成立，算术 fixed-fiber symmetry 失败

Paper 16 将 Paper 15 的 $pqr$ residual 提升到 Burnside/representation-valued
cycle index。其正、负 primitive $S_3$-sets 给出

$$
R_{pqr}=[S_3/S_3]+[S_3/C_3]-[S_3/C_2],
$$

对应 character 与 subgroup marks 分别为

$$
\chi(e,(12),(123))=(0,0,3),
\qquad (\phi_{\{e\}},\phi_{C_2},\phi_{C_3},\phi_{S_3})=(0,0,3,1).
$$

由于 $pqr$ 是 squarefree multidegree，任何 $r>1$ Adams/power 项都不能消掉这个
residual；formal species/cycle-index ledger 因而是真正的正结果。

但它不能成为算术 fixed-operator 的 character Fredholm decomposition。若
$A_x$ 是 subset-edge transfer，则

$$
\rho(g)A_x\rho(g)^{-1}=A_{g\cdot x}.
$$

在 $x_p=p^{-s}$、$\Re s>0$ 时，各权重模严格不同，固定 $A_x$ 的 permutation
stabilizer 只有恒等元。令所有权重相等虽恢复 $S_n$，rank-one transfer 的像却只在
trivial isotype，所有非平凡 resolved determinants 都等于 $1$。改用保留 subset
表示的 diagonal lift 又得到

$$
\operatorname{sdet}(I-D_x)
=\prod_{\varnothing\ne S}(1-x_S)^{(-1)^{|S|+1}},
$$

从两原子起便多出 $(1-x_px_q)^{-1}$ 等 mixed factors。17/17 tests、4,008 个
$C_2$ sign-power checks、56 个 ghost checks 和 455/455 controls 全部支持这一
incompatibility triangle：**exact Euler augmentation、nontrivial character motion、
commuting arithmetic symmetry** 在当前 canonical lifts 中不能同时成立。

阶段结论为 **GO_FORMAL_EQUIVARIANT_LEDGER /
STOP_CHARACTER_FREDHOLM_FIBERS / STOP_STANDARD_SUPERTRACE_INTERPRETATION /
PROVES_TOO_MUCH**。Paper 17 已把群作用从 prime-label relabeling 移到真正 commuting
的 finite fiber，测试同一 symbolic skew extension 的 Artin factors；Route B 继续锁定。

### 论文 17：真正的有限 fiber 成立，但 Artin blocks 仍不选择算术

Paper 17 不再让群置换不同的 arithmetic roofs，而是在同一个 signed subset shift 上
加入 commuting 的 $C_2$ deck fiber。对非空 subset symbol $S$ 冻结
$\alpha(S)=|S|\bmod2$，则 regular transfer 的两个 character blocks 在 $z=1$ 精确满足

$$
D_+(s)=\prod_p(1-p^{-s})=\frac1{\zeta(s)},\qquad
D_-(s)=\prod_p(1+p^{-s})=\frac{\zeta(s)}{\zeta(2s)},
$$

而真正属于整个 skew extension 的 determinant 是

$$
D_{\rm reg}(s)=D_+(s)D_-(s)
=\prod_p(1-p^{-2s})=\frac1{\zeta(2s)}.
$$

因此这是一个合法的 same-object Artin decomposition，却不是把单个 block 的 divisor
偷换成 whole determinant。primitive 账本也保持了这一边界：若一个 $C_m$ cocycle
在 base primitive 上的总 charge 为 $c$，lift 要经过
$m/\gcd(m,c)$ 次 base traversal 才闭合，并分裂为 $\gcd(m,c)$ 个 lifted cycles。
prime singleton 的 clock 因而被 fiber order 放大，而 mixed subset primitives 在每个
非平凡 cutoff 仍可立即闭合。

更一般地，inclusion-compatible、relabel-natural 且 operator-coherent 的 atom-local
one-letter cocycle 必须形如 $\alpha(S)=a^{|S|}$；若 extension transitive，其有效像只能
是 cyclic。这关闭了 Paper 16 留下的 one-letter loophole，但不覆盖真正依赖 transition
的 cocycle。14/14 tests、300 个 repetition rows、350 个 $C_m$ character rows、
350 个 primitive/lift rows 与 72,079 张自然性表全部 exact；然而 64/64
composite、shuffled、random-rational controls 也全部通过，control margin 为零。

阶段结论为 **GO_GENUINE_FINITE_FIBER / GO_SAME_OBJECT_ARTIN_FACTORS /
STOP_PRIMITIVE_PRIME_MATCHING / STOP_ARITHMETIC_SELECTIVITY /
PROVES_TOO_MUCH**。Paper 18 已转向同一 tensor-subset grammar 上真正非交换的
transition holonomy，检验它能否逃出 cyclic degree rigidity；Route B 继续锁定。

### 论文 18：非交换 transition holonomy 成立，但 faithful block 精确泄漏

Paper 18 在同一 tensor-subset full shift 的完整 directed-edge presentation 上冻结
$G=S_3$。若 $S\subsetneq T$，edge label 为 $r=(12)$；若
$T\subsetneq S$，label 为 $t=(23)$；其余为恒等元。这个 cocycle 不是 Paper 17
的 one-letter degree cocycle加 vertex coboundary：三原子 incidence loops 已给出
不交换的 based holonomies，而 edge-marked 四步 commutator cycle 的 character gap
精确等于 $3$。

两原子 character blocks 展示了最清楚的 same-object 分裂。trivial 与 sign blocks
都精确等于

$$
D_{mathbf1}(x,y)=D_{mathrm{sgn}}(x,y)=(1-x)(1-y),
$$

但二维 standard block 为

$$
D_{mathrm{Std}}(x,y)
=(1-x)^2(1-y)^2+3xy(x+y)(xy+1)(x+y-1).
$$

因此真正看见非交换 holonomy 的 faithful factor 必然同时看见 mixed symbolic cycles：
$\Delta\log D$ 中 $x^2y$、$xy^2$ 的系数为 $-3$，$x^2y^2$ 为 $-6$；
未标记的 degree-six 聚合项 $x^3y^3=-9$ 与 edge-separated commutator certificate
被严格分账。有限穷举进一步给出
$S_3:36=36$、$D_4:64=64$、$Q_8:64=64$ 的
“all-irrep clean = gauge”计数；$Q_8$ 只看一维 characters 时却有 512 个假 survivors。
这些是 exact finite evidence，不被升格为一般 cohomology 定理。

解析上，trivial block 在 $\Re s>1$ 有 trace-class realization；包含对称 incidence
coupling 的 nontrivial blocks 只在 $\Re s>2$ 关闭。14/14 tests 与六类 inventory、
五个冻结种子的 30/30 controls 全部通过，但 control margin 仍为零。由此阶段结论是
**GO_GENUINE_TRANSITION_HOLONOMY / STOP_ARITHMETIC_SELECTIVITY /
STOP_COMPLETED_DIVISOR / PROVES_TOO_MUCH**，Route B 继续锁定。

这一批已经把“给 full-subset base 继续加 fiber/character/holonomy 装饰”的空间压缩得
很小。下一批最值得做的仍是 Symbolic Dynamics，但应把算术约束写进 allowed
transitions 本身：优先研究 constrained factorization、renewal 或 countable-Markov
grammar，并在任何解析延拓之前先证明它能区分 matched arbitrary inventories。

### 论文 19：试除可以进入同一对象，但 Fredholm determinant 会剪掉全部计算

Paper 19 首次把 full-shift semiring 的 alphabet-sum、Cartesian tensor 与 additive
order 直接编译成 stationary countable Markov grammar。商搜索不是一步
“存在 $q$”的 oracle，而是显式状态 $Q_{n,d,q}$ 逐个推进；prime 输入进入
$A_p$ 自环，composite 输入进入单向 cemetery ray。对冻结的 entropy roofs，整个
vertex-adjacency 在 $\Re s>1$ 为 trace-class 全纯族，并满足

$$
\operatorname{Tr}L_s^r=\sum_p p^{-rs},
\qquad
\det(I-zL_s)=\prod_p(1-zp^{-s}).
$$

因此这是一个合法的 same-operator A1–A2 精确链，而不是把外部 prime table 与
determinant 拼接。13/13 exact tests 还验证了截止 512 的零支持错误、1,651 个实际
quotient states、十二阶 power traces 与独立有理 Bareiss determinant。

但正向意义被一个更强的定理关闭：所有输入、试除与 cemetery 状态都在 transient
feeding DAG；删除它们不改变任意 power trace 或 Fredholm determinant，recurrent
core 精确退化成 Paper 04 的独立 prime loops。更一般地，任意 total decider 都可用
accept-loop/reject-ray 包装编译

$$
\prod_{n\in S}(1-zn^{-s}),
$$

而 squares、powers of two、Fibonacci 与 hash controls 已全部精确复现。因此结论是
**GO_EXACT_SEMIRING_VERIFIER / STOP_RECURRENT_ARITHMETIC_ADVANCE /
SELECTOR_TAUTOLOGICAL / PRUNING_EQUIVALENT / PROVES_TOO_MUCH**。

Paper 20 不再允许完成判定后才附加 accept loop；它将直接把完整验证路径闭合为
recurrent cycle，并检验 Euler 总 clock $\log p$ 与紧性/Fredholm 性是否能够共存。
当前最小猜想是一个 clock-dilution obstruction：当验证长度远快于 $\log p$ 增长时，
周期上必有边权趋近 $1$，从而使 whole operator 非紧。

### 论文 20：计算路径成功进入 recurrence，但 exact clock 被状态细分稀释

Paper 20 把 Paper 19 的完整显式商搜索路径直接闭成 recurrent verifier cycle；不再在
判定结束后另接一个 accept loop。对每个 prime $p$，contracted cycle 的精确长度是

$$
\ell(p)=2+\sum_{d=2}^{\lfloor\sqrt p\rfloor}\left\lceil\frac pd\right\rceil
=\frac12p\log p+(\gamma-1)p+O(\sqrt p),
$$

且一圈的 total roof 被 source-lock 为 $\log p$。因此 raw primitive ledger 的确给出

$$
\prod_p\bigl(1-z^{\ell(p)}p^{-s}\bigr),
$$

并在 $z=1$、$\Re s>1$ 恢复 $1/\zeta(s)$。这是真正的 recurrent arithmetic
compiler 正结果，而不是 Paper 19 的 transient pruning。

但 exact total clock 与长计算路径不相容：任何非负 roof 分配都至少有一条边满足
$\tau_e\le \log p/\ell(p)\to0$，相应权重 $e^{-s\tau_e}\to1$。自然 whole
vertex-adjacency 的 essential norm 因而等于 $1$，算子非紧、不属于任何有限 Schatten
类，并且单位圆进入 essential approximate spectrum；$I-zL_s$ 在 $|z|=1$ 上不是
Fredholm。raw orbit product 不是这个 whole operator 的 Fredholm determinant。

Poincaré first return 虽给出 trace-class diagonal operator
$R_se_p=p^{-s}e_p$，却把整个验证过程收缩掉，并把 marker 从
$z^{\ell(p)}$ 改回 $z$，与 Paper 04 同构。564/564 个 prime cycles、12/12 tests、
1,651 个显式 quotient states 与四类 padded-decider controls 都通过，说明障碍既不是
factor oracle 伪影，也不具 arithmetic selectivity。阶段结论是
**GO_RECURRENT_VERIFIER_ORBIT_LEDGER / GO_CLOCK_DILUTION_THEOREM /
STOP_WHOLE_VERTEX_FREDHOLM / FIRST_RETURN_COLLAPSE / PROVES_TOO_MUCH**。

Paper 21 因而放弃“把一条越来越长的 verifier path 闭合”的方案，转向一个固定局部
successor–divisor grammar：它先检验 whole transfer 能否在更大的半平面成为真正
trace-class Fredholm family，再在选择 roof 之前审计其 primitive-cycle species。

### 论文 21：whole Fredholm 正则性成立，但 primitive species 全长度洪泛

Paper 21 在所有非平凡 full-shift objects 上冻结局部 transition

$$
n\longrightarrow d
\quad\Longleftrightarrow\quad d\ge2, d\mid n+1,
$$

并使用 endpoint roof $\tau(n,d)=\log n+\log d$。这个 countable Markov graph
不是 verifier wrapper：它本身强连通、aperiodic 且 mixing，算术 transition 真正进入
recurrent core。更强的是，column-source adjacency

$$
L_se_n=\sum_{d\mid n+1,\ d\ge2}(nd)^{-s}e_d
$$

满足 sharp theorem

$$
L_s\in\mathcal S_1\quad\Longleftrightarrow\quad\Re s>\frac12.
$$

因此 $det(I-zL_s)$ 在临界线右侧整个开半平面都是同一 whole symbolic object 的
honest Fredholm determinant；Paper 20 的 noncompactness 已被真正修复。

失败转移到了 orbit species。graph 没有自环，所以 $\operatorname{Tr}L_s=0$，而
目标 prime Euler determinant 的一阶 trace 非零。与此同时，对每个 $k\ge2$ 都有
simple primitive cycle

$$
C_k=(k,k+1,\ldots,2k-1),
$$

且其自然 norm 是 composite square
$\left(\prod_{n=k}^{2k-1}n\right)^2$。任何长度 $r$ 的闭路都被严格限制在
$\{2,\ldots,2r-1\}$，所以无限图的第 $r$ 阶 trace 可在 cutoff $2r-1$ exact
认证；这也排除了有限窗口伪影。19/19 tests 精确给出 $T_{32}=14{,}532{,}674$、
$P_{32}=454{,}021$，并在长度 16 内枚举 667 个 primitive classes。

最锋利的 control 只保留 quotient $q=(n+1)/d\in\{1,2\}$：这个极窄 spine 仍保留
强连通、mixing、全长度 $C_k$ 与相同 $\Re s>1/2$ trace-class 阈值；只保留
$q=1$ 才变成无环。故阶段结论是
**GO_SHARP_WHOLE_FREDHOLM / STOP_PRIME_ORBIT_LEDGER /
CYCLE_FLOOD / PRUNING_PERSISTS / PROVES_TOO_MUCH**。

Paper 22 不再改 base graph，而把 canonical quotient word 暴露为 holonomy，先精确
分类哪些 cofactor classes 对应哪些 primitive cycles，再检验 character resolution
能否在不牺牲 Fredholm 域的条件下隔离目标 orbit species。

### 论文 22：cofactor class 可精确解析，但三种解析实现互不兼容

Paper 22 在同一 successor–divisor graph 上暴露 edge factor witness

$$
q(n,d)=\frac{n+1}{d},
$$

并把闭路 holonomy 冻结为 $Q(\gamma)=\prod q$。闭路恒有
$Q(\gamma)=\prod_{n\in\gamma}(1+1/n)>1$，所以 regular group lift 的 neutral
sector 没有周期轨道；第一个非平凡 class 则完全可解：

$$
Q(\gamma)=2
\quad\Longleftrightarrow\quad
\gamma=C_k=(k,k+1,\ldots,2k-1),\qquad k\ge2,
$$

其中每个长度恰有一个 simple primitive class，且 temporal repetitions 不会污染
atomic holonomy。相应 connected coefficient 为

$$
\mathcal H_2(s,z)=\sum_{k\ge2}z^k
\left(\frac{(2k-1)!}{(k-1)!}\right)^{-2s}.
$$

对 two-parameter whole adjacency

$$
L_{s,u}e_n
=\sum_{d\mid n+1,\ d\ge2}(nd)^{-s}q(n,d)^{-u}e_d,
$$

论文证明了 sharp phase diagram

$$
L_{s,u}\in\mathcal S_1
\quad\Longleftrightarrow\quad
\Re s>\frac12
\quad\text{且}\quad
\Re(s+u)>\frac12.
$$

但这同时给出 Fredholm trilemma：只保留 cofactor roof 时，$q=1$ successor spine
使算子在有界时仍非紧；恢复 endpoint decay 虽得到 honest determinant，却给
$C_k$ 阶乘尺度的权；unitary character 仅赋共同相位 $\chi(2)$，不能删除任何
$C_k$。ordinary regular lift 又因无限 deck multiplicity 非紧，而独立的 semifinite
trace 虽在 $\Re s>1/2$ 可积，其 neutral determinant 恰为 $1$。

26/26 exact tests 审计了 30,626 条 source edges、164 条 $r\le8$ rooted cycles、
120 个 atomic witnesses、80 个 atomic trace coefficients，以及六类 positive-inventory
controls；所有 matched inventories 都保留同一个 $Q=2$ spine，selection margin 为零。
阶段结论是 **GO_EXACT_HOLONOMY_RESOLUTION / GO_SHARP_CHARACTER_FREDHOLM_DOMAIN /
STOP_NEUTRAL_SECTOR / STOP_PRIME_ORBIT_LEDGER / PROVES_TOO_MUCH**。

Paper 23 因而保留 $C_k$ 上完整、有序的 quotient word $1^{k-1}2$，检验 fixed
finite fiber 或 finite-dimensional recurrence 能否在不编译 prime table 的前提下选择
prime length；Route B 继续锁定。

## 目录

- [研究提案](propose-symbolic-dynamics.md)
- [Route-A evaluator](skills/route-a-evaluator.md)
- [Route-B evaluator](skills/route-b-evaluator.md)
- [prior-work 与共享文档](docs/)
- [二十二篇论文](papers/)

根目录不再设置项目包装层；每个论文项目各自使用 `PAPER_MANIFEST.sha256` 管理
完整性。本地 PDF/legacy 输入语料和运行缓存不进入 manifests。
