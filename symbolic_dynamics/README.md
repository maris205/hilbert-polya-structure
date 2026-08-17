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
| [23-unary-holonomy-finite-fiber-rigidity](papers/23-unary-holonomy-finite-fiber-rigidity/README.md) | [PDF](papers/23-unary-holonomy-finite-fiber-rigidity/main.pdf) · [LaTeX/证明/实验/Route-A 记录](papers/23-unary-holonomy-finite-fiber-rigidity/) | canonical cofactor word $1^{k-1}2$ 上，任意固定有限状态响应最终周期，任意固定有限维矩阵响应是 LRS，因而不能精确选择无限 prime-only support；增长记忆虽可拟合任意有限目标，却完全不具算术选择性，且完整块行列式仍保留 $z^k$ 与阶乘 roof。 | **FINITE-FIBER RIGIDITY / FACTORIAL ROOF / ROUTE-A REJECTED / SD-C25** |
| [24-kraft-fredholm-log-code-trilemma](papers/24-kraft-fredholm-log-code-trilemma/README.md) | [PDF](papers/24-kraft-fredholm-log-code-trilemma/main.pdf) · [LaTeX/证明/实验/Route-A 记录](papers/24-kraft-fredholm-log-code-trilemma/) | 有限 alphabet 的可分 prime code 在总 roof $\log p$ 下被 Kraft 不等式强制出无界 cycle length，从而 whole adjacency 非紧；共享 trie/renewal 则产生 mixed primitive necklaces，唯一 clean trace-class escape 是 Paper 04 的 countable atom diagonal。 | **KRAFT–FREDHOLM TRILEMMA / ROUTE-A REJECTED / SD-C26** |
| [25-holomorphic-lefschetz-code-collapse](papers/25-holomorphic-lefschetz-code-collapse/README.md) | [PDF](papers/25-holomorphic-lefschetz-code-collapse/main.pdf) · [LaTeX/证明/实验/Route-A 记录](papers/25-holomorphic-lefschetz-code-collapse/) | holomorphic de Rham $0|1$ complex 在所有 repetitions 上精确抵消 affine-branch 分母并给出 honest graded determinant；但共享 renewal 保留 mixed necklaces，分离 components 又在 cohomology 上退化为任意 atom inventory。 | **LEFSCHETZ CANCELLATION / COHOMOLOGY COLLAPSE / SD-C27** |
| [26-pure-power-selector-atom-collapse](papers/26-pure-power-selector-atom-collapse/README.md) | [PDF](papers/26-pure-power-selector-atom-collapse/main.pdf) · [LaTeX/证明/实验/Route-A 记录](papers/26-pure-power-selector-atom-collapse/) | 单色词为 $1$、mixed 词为 $0$ 的逐词 cyclic selector 可精确实现，但任意有限维普通或 graded 实现的可见半单化都被强制为一颜色一块；radical 只能制造 determinant-invisible 的表示连通。 | **PURE-POWER SELECTOR / ATOM-BLOCK COLLAPSE / SD-C28** |
| [27-mobius-incidence-atom-compiler](papers/27-mobius-incidence-atom-compiler/README.md) | [PDF](papers/27-mobius-incidence-atom-compiler/main.pdf) · [LaTeX/证明/实验/Route-A 记录](papers/27-mobius-incidence-atom-compiler/) | 整数整除 source 的 covers 内生给出 atoms，Möbius-incidence idempotents 在迹之前消去 composite 与 mixed words，形成精确 atom Euler ledger；但可数 compiler 与坐标 atom table 有界相似，trace-class 域仍停在 $\Re s>1$。 | **SOURCE-DERIVED LEDGER / SIMILARITY COLLAPSE / SD-C29** |
| [28-chiral-incidence-metric-trilemma](papers/28-chiral-incidence-metric-trilemma/README.md) | [PDF](papers/28-chiral-incidence-metric-trilemma/main.pdf) · [LaTeX/证明/实验/Route-A 记录](papers/28-chiral-incidence-metric-trilemma/) | reflected incidence-chiral family 在临界线上紧自伴且第四矩精确随 $t$ 运动；但 $B\notin\mathcal S_2$，$\det_3$ 删去二阶项，正定 source-natural metric 会将对象正交化回独立 atoms，而原生 motion 被所有对照复制。 | **CHIRAL MOTION / METRIC TRILEMMA / SD-C30** |
| [29-functorial-chiral-counterterm-no-go](papers/29-functorial-chiral-counterterm-no-go/README.md) | [PDF](papers/29-functorial-chiral-counterterm-no-go/main.pdf) · [LaTeX/证明/实验/Route-A 记录](papers/29-functorial-chiral-counterterm-no-go/) | source-natural quadratic subtraction 能分离 $B^2$ 的 prime-harmonic divergence，但 leading-only 与 full-diagonal schemes 相差一个非零可和有限项，因而自然性不唯一固定 finite part；保留 baseline mixed residue 与消去同型 controls 分别强制 $\beta=0$ 和 $\beta=1$，排除 pair-local linear-Gram 选择器。 | **FINITE-PART CLASSIFICATION / LOCAL SELECTIVITY NO-GO / SD-C31** |
| [30-free-monoid-incidence-indistinguishability](papers/30-free-monoid-incidence-indistinguishability/README.md) | [PDF](papers/30-free-monoid-incidence-indistinguishability/main.pdf) · [LaTeX/证明/实验/Route-A 记录](papers/30-free-monoid-incidence-indistinguishability/) | 整数乘法整除 source 与形式自由交换/UFD clone 在 atoms、join/lcm、interval Möbius、cutoff、roof 与 Gram decorations 上同构；因此任意对此对象同构自然的局部或非局部 cumulant/mixed invariant 都被 clone 精确复制。有限三元统计虽分开四个 fixture，却无法给出算术选择性。 | **FREE-UFD INDISTINGUISHABILITY / BRANCH CLOSED / SD-C32** |
| [31-wilson-semiring-verifier-trichotomy](papers/31-wilson-semiring-verifier-trichotomy/README.md) | [PDF](papers/31-wilson-semiring-verifier-trichotomy/main.pdf) · [LaTeX/证明/实验/Route-A 记录](papers/31-wilson-semiring-verifier-trichotomy/) | alphabet sum 与 tensor product 确实击穿只保乘法的裸 UFD clone；但 matched semiring clone 精确复制全部 Wilson paths。Wilson recurrence 给每个素数一条长度 $p-1$ 的 cycle，却使 whole operator 非紧；first return 改写自由 marker，transient 版本又剪枝回 atom diagonal。 | **SEMIRING CLONE / PRUNING–DILUTION TRICOTOMY / SD-C33** |
| [32-projective-residue-recurrence-obstruction](papers/32-projective-residue-recurrence-obstruction/README.md) | [PDF](papers/32-projective-residue-recurrence-obstruction/main.pdf) · [LaTeX/证明/实验/Route-A 记录](papers/32-projective-residue-recurrence-obstruction/) | 非 terminal 的 $P^1(\mathbb Z/n\mathbb Z)$ recurrent grammar 在同一 uninduced object 上恢复了 $\Re s>2$ 的 trace-class Fredholm ownership；但 $S^2=R^3=1$ 对所有模数都成立，cusp coupling 又给出普适 composite diamonds，故 primitive ledger 在配权前已失败。 | **PROJECTIVE RECURRENCE OBSTRUCTION / BRANCH CLOSED / SD-C34** |
| [33-relation-homology-operator-non-descent](papers/33-relation-homology-operator-non-descent/README.md) | [PDF](papers/33-relation-homology-operator-non-descent/main.pdf) · [LaTeX/证明/实验/Route-A 记录](papers/33-relation-homology-operator-non-descent/) | 从 $S/R$ 轨道 incidence 施加的 Manin norm-polynomial quotient 消去预定 chain relations，diamond filling 也消去 cross $H_1$；但每个模数仍保留 cusp $R,S$ primitive survivor，character/supercharacter controls 均不筛素数，且原始 $S+R$ adjacency 在 $n=2$ 已不降到 quotient。 | **RELATION HOMOLOGY NO-GO / SEMIRING-RESIDUE FAMILY CLOSED / SD-C35** |
| [34-positive-recognition-recurrence-quadrilemma](papers/34-positive-recognition-recurrence-quadrilemma/README.md) | [PDF](papers/34-positive-recognition-recurrence-quadrilemma/main.pdf) · [LaTeX/证明/实验/Route-A 记录](papers/34-positive-recognition-recurrence-quadrilemma/) | 正标量 literal atom-only ledger 强制 declared cycles 分居 recurrent components；识别 DAG 对全部 power traces/Fredholm determinant 可剪枝，有限 alphabet 与总 roof $\log p$ 又强制 whole operator 非紧，而 first return 会把原始 $z^{\ell(p)}$ marker 改成 $z$。 | **POSITIVE COMPILER QUADRILEMMA / ROUTE-A REJECTED / SD-C36** |
| [35-affine-semigroup-object-firewall](papers/35-affine-semigroup-object-firewall/README.md) | [PDF](papers/35-affine-semigroup-object-firewall/main.pdf) · [LaTeX/证明/实验/Route-A 记录](papers/35-affine-semigroup-object-firewall/) | 正 affine Cayley source 有严格高度而无 recurrence；形式逆边制造 backtracks，Hashimoto reduction 又保留普适 affine relation cycles。Bost--Connes 的 $\zeta(\beta)$ 是另一 diagonal Gibbs 对象的首个 trace coefficient，不是同一 graph-step primitive determinant。 | **AFFINE OBJECT FIREWALL / ROUTE-A REJECTED / SD-C37** |
| [36-affine-cayley-chain-cancellation-no-go](papers/36-affine-cayley-chain-cancellation-no-go/README.md) | [PDF](papers/36-affine-cayley-chain-cancellation-no-go/main.pdf) · [LaTeX/证明/实验/Route-A 记录](papers/36-affine-cayley-chain-cancellation-no-go/) | 完整 affine Cayley relation filling 使复形契约并清空全部 recurrent homology，且不等长关系 $vu=u^rv$ 阻止原 unit-step marker 下降；同一 prequotient 的 trace-class damped Hashimoto determinant 仍严格看见 relation polygon，而标量 chain superlift 又以通用 $1-2+1=0$ 把所有 one-relator controls 一并消去。 | **CHAIN CANCELLATION / CLOCK NON-DESCENT / ROUTE-A REJECTED / SD-C38** |
| [37-local-coefficient-normal-closure-saturation](papers/37-local-coefficient-normal-closure-saturation/README.md) | [PDF](papers/37-local-coefficient-normal-closure-saturation/main.pdf) · [LaTeX/证明/实验/Route-A 记录](papers/37-local-coefficient-normal-closure-saturation/) | 普通可逆有限秩 local transport 不可能删去完整 primitive Euler factor；graded shear 虽能抵消直接 affine relator 及全部 repetitions，却在 mixed normal-closure products 上泄漏，而饱和到全部 mixed products 又会清空所有 closed-word ledger。 | **LOCAL-COEFFICIENT SATURATION / MIXED LEAKAGE / ROUTE-A REJECTED / SD-C39** |
| [38-bass-serre-tree-orbital-collapse](papers/38-bass-serre-tree-orbital-collapse/README.md) | [PDF](papers/38-bass-serre-tree-orbital-collapse/main.pdf) · [LaTeX/证明/实验/Route-A 记录](papers/38-bass-serre-tree-orbital-collapse/) | 对冻结 ascending-HNN splitting/presentation canonical 的 Bass--Serre full tree 没有正长度 reduced closed path，而其 full-edge Hashimoto operator 非紧且非迹类；转向 orbital conjugacy ledger 只得到对所有 ascending HNN controls 通用的 necklace 函数，且改变对象与 marker。 | **BASS–SERRE TREE / ORBITAL COLLAPSE / AFFINE BRANCH CLOSED / SD-C40** |
| [39-affine-obstruction-dag-closure-certificate](papers/39-affine-obstruction-dag-closure-certificate/README.md) | [PDF](papers/39-affine-obstruction-dag-closure-certificate/main.pdf) · [LaTeX/证明/实验/Route-A 记录](papers/39-affine-obstruction-dag-closure-certificate/) | 在 P35--P38 结果已知后，把其哈希化 outcome 组装成 checker-frozen 的 6-node/5-edge structural spine 与 22-node/28-edge typed proof DAG；14 类修复与 16 个请求 token 全部在精确有限域内归类，EXIT 不冒充失败，E22 不获 closure credit，跨 P36→P37 的四个候选状态字段全部 RESET。 | **RELATIVE AFFINE CLOSURE AUDIT / REGISTRY HANDOFF / ROUTE-A REJECTED / SD-C41** |
| [40-gauss-mayer-projection-firewalls](papers/40-gauss-mayer-projection-firewalls/README.md) | [PDF](papers/40-gauss-mayer-projection-firewalls/main.pdf) · [LaTeX/证明/实验/Route-A 记录](papers/40-gauss-mayer-projection-firewalls/) | 把普通 Gauss digit shift 与 two-digit pair return 通过 $\rho\iota=\iota\sigma^2$ 严格分型，并从 $K_s=\mathcal L_s^2$ 的 Fredholm traces 导出 intrinsic pair ledger；对且仅对 trace、order discriminant、expanding norm 三个投影，完整 rational-prime reciprocal-Euler conjunction 全部失败，而 pair ledger 与 same-space determinant 保留。严格 tuple 为 `(A0_WEAK_ARITHMETIC_RELATION,A1_PASS_ANALYTIC,A2_ANALYTIC_DETERMINANT,A3_PARTIAL_ANALYTIC_STRUCTURE,A4_FORMAL_HINT)`。 | **GO_MODULAR_PRIMITIVE_LEDGER / GO_SAME_OBJECT_MAYER_DETERMINANT / STOP_CANONICAL_INTEGER_PROJECTION / STOP_RATIONAL_INTEGER_CLOCK_REPETITION_CONJUNCTION / STOP_OPERATOR_VISIBLE_SELECTOR_NOT_OWNED / ROUTE_A_REJECTED / SD-C42** |
| [41-knauf-rooted-clock-non-descent](papers/41-knauf-rooted-clock-non-descent/README.md) | [PDF](papers/41-knauf-rooted-clock-non-descent/main.pdf) · [LaTeX/证明/实验/Route-A 记录](papers/41-knauf-rooted-clock-non-descent/) | 对冻结的 Knauf rooted label，trailing-zero stable quotient 上的 append-one 不下降；该 label 既非 cyclic clock 也不满足 temporal powers，literal Liouville scalar phase 同样不下降。state inventory 仍在 `Re(s)>2` 上拥有 diagonal Fredholm determinant，但不获得 binary primitive-return ownership。canonical replay 为 `24/24` 与 `25/25`，science SHA-256 为 `f9cbcde9a757896b976ad81a66f235d670029f727b6fda9b4e851846bac50bec`；严格 tuple 为 `(A0_ANALYTIC_ARITHMETIC_ORIGIN,A1_FAIL,A2_FAIL,A3_PARTIAL_ANALYTIC_STRUCTURE,A4_FAIL)`。 | **ROOTED CLOCK NON-DESCENT / INVENTORY DETERMINANT OWNERSHIP / ROUTE-A REJECTED / SD-C43** |

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

### 论文 23：有限记忆只能最终周期，增长记忆又会拟合一切

Paper 23 在 Paper 22 已完全分类的 canonical cycles

$$
C_k=(k,k+1,\ldots,2k-1)
$$

上保留有序 cofactor word

$$
W(C_k)=1^{k-1}2.
$$

对任何固定有限群、有限半群、DFA 或 NFA，读这个 unary family 得到的响应都最终
周期，因此不可能在所有素数长度上响应、在所有合数长度上静默。对固定
$A,B\in M_d(\mathbb C)$，bilinear response 与 trace response

$$
u^{\mathsf T}A^{k-1}Bv,
\qquad
\operatorname{tr}(A^{k-1}B)
$$

都是线性递推序列；Skolem–Mahler–Lech 定理使其 exact zero/nonzero support 与固定
level support 最终周期。若让维数随 cutoff 增长，nilpotent shift 又能逐项记住 prime、
square、Fibonacci、random、hash 或任意 rational target，因而只能得到
`PROVES_TOO_MUCH` 的有限拟合。

论文同时修正了一个重要的 determinant 边界。令

$$
w_k=z^k\left(\frac{(2k-1)!}{(k-1)!}\right)^{-2s}.
$$

真正的 $d$ 维 local factor 是

$$
\det_{\mathbb C^d}(I-w_kBA^{k-1}),
$$

而不是 $1-w_k\operatorname{tr}(BA^{k-1})$。即使首个 trace 为零，高次重复仍可见；
$A=I_2$、$B=\operatorname{diag}(1,-1)$ 的精确控制给出
$\operatorname{tr}(B)=0$、$\operatorname{tr}(B^2)=2$ 与 local factor $1-w_k^2$。
即使另行假设一维 prime-oracle deletion，保留下来的仍是

$$
\prod_p\left(1-z^p
\left(\frac{(2p-1)!}{(p-1)!}\right)^{-2s}\right),
$$

而不是目标 Euler product。32/32 exact tests 审计了 4,095 个 canonical cycles、
8,390,655 条 edges、1,054,474 个 finite-state configurations 和完整的 block
determinant firewall；双跑的 31 个 artifacts 全部 byte-identical。

阶段结论是 **GO_FINITE_FIBER_RIGIDITY / STOP_PRIME_LENGTH_SELECTOR /
STOP_FACTORIAL_ROOF / PROVES_TOO_MUCH / ROUTE_A_REJECTED**。Paper 24 若继续这条
同族分支，必须放弃对 unary word 再叠一层有限 character，转而寻找一个
$O(\log n)$ symbolic length、总 roof $\log n$、在 primitive-orbit algebra 内部区分
prime/composite 且 whole operator trace class 的 source-derived recurrent grammar；
Route B 继续锁定。

### 论文 24：有限码、纯 primitive ledger 与 whole Fredholm 形成三难

Paper 24 直接测试了 Paper 23 留下的最强压缩义务。冻结有限可见 alphabet、正标量
edge weights、每个 prime 恰一条 primitive cycle 且无额外 primitive orbit，并要求

$$
T(\gamma_p)=\log p.
$$

正性与唯一分解首先强迫不同 prime cycles 顶点不交：若两圈共享 recurrent vertex，
拼接闭词的 primitive root 会给出 $pq=r^m$。有限可见码又强迫无穷子列满足

$$
\ell(p)\ge \frac{\log p}{4\log b}.
$$

因此每条长圈至少有一条 edge roof 不超过 $4\log b$。这些边来自互不相交的 sources，
其标准基向量弱收敛到零，但 whole adjacency 的像范数一致有正下界；算子对每个
$\sigma>0$ 都非紧，因而不属于任何有限 Schatten 类。

共享 prefix trie 或 renewal hub 虽节省状态，却使 determinant 变成
$1-\sum_n w_n$，其 connected logarithm保留所有 mixed primitive necklaces。
若要求标准 graph marker

$$
\det(I-zL_s)=\prod_p(1-zp^{-s}),
$$

比较 $z$ 的一次系数还会直接强迫 $\ell(p)=1$；这正退化为 Paper 04 的 countable
atom loops。35/35 exact tests、672 个正 roof 分配、共享 trie/renewal、factorization、
finite-prefix S-adic 与任意库存 controls 全部吻合该三难。阶段结论是
**GO_KRAFT_FREDHOLM_OBSTRUCTION / STOP_FINITE_SYMBOL_LOG_CODE /
STOP_LITERAL_RECURRENT_COMPRESSION / SELECTOR_TAUTOLOGICAL /
ROUTE_A_REJECTED**。这个 theorem 只锁 natural graph-coordinate space；Paper 25
继续检验 canonical holomorphic/de Rham graded transfer 能否修复 nuclearity 而不在
cohomology 上塌回 atom inventory。

### 论文 25：解析 nuclear escape 成功，但同调只留下 atom inventory

Paper 25 把 Paper 24 的 logarithmic binary code 编译成严格收缩的 affine inverse
branches。对单支 $\phi(z)=a+qz$ 与权 $w$，零形式 pullback 的重复迹为

$$
\operatorname{Tr}(wU_{\phi,0})^r=\frac{w^r}{1-q^r}.
$$

任何 scalar normalization 在匹配 $r=1$ 后都会在 $r=2$ 失败；普通 trace-class
tensor fiber 若想补出分子 $1-q^r$，其 Fredholm determinant 将被迫等于
$(1-t)/(1-qt)$，因有极点而不可能。

真正的正面突破来自 canonical holomorphic de Rham $0|1$ complex：

$$
\operatorname{Tr}W_0^r-\operatorname{Tr}W_1^r=w^r,
\qquad
\frac{\det(I-zW_0)}{\det(I-zW_1)}=1-zw.
$$

这在所有 repetitions 上精确成立，两边都是 $\Re s>1$ 中 honest trace-class
holomorphic operators；但不变量是 graded/relative determinant，不是普通 block
determinant。

共享 renewal assembly 的 cohomology 只有一个常数态，所以最终只得到

$$
1-z\sum_jw_j,
$$

全部 mixed primitive necklaces 仍然存活。把 branches 分离后虽得到
$\prod_j(1-zw_j)$，但每个 contractible analytic fiber 都约掉，只剩 supplied label
对应的一个 $H^0$ atom loop；primes、squares、Fibonacci、random、hash 与任意
inventory 全部同样成功。原始 digit marker 也仍是
$u^{\ell(n)}n^{-s}$，只有 first-return induction 才能改成每个 codeword 一个 $z$。

53/53 exact tests 验证了 4,095 个 code branches、完整 characteristic-polynomial
quotients、1,183 个 primitive necklaces（其中 1,174 个 mixed survivors）与 42 个
full-inventory controls。阶段结论是 **GO_HOLOMORPHIC_NUCLEARITY /
GO_CANONICAL_LEFSCHETZ_CANCELLATION / GO_FULL_GRADED_DETERMINANT /
STOP_SHARED_RENEWAL_MIXED_WORDS / COHOMOLOGY_COLLAPSE /
ATOM_INVENTORY_EQUIVALENCE / ROUTE_A_REJECTED**。Paper 26 转而让 grading 作用于
branch combinatorics 本身：若它仍需要一原子一颜色的记忆，就应证明 exact cyclic
selector 的 semisimple collapse；Route B 继续锁定。

### 论文 26：逐词 selector 精确成立，但有限可见部分必塌缩为颜色块

Paper 26 冻结非空词上的循环系数：单色词取 (1)，mixed 词取 (0)，并要求在
所有 repetitions 上逐词成立。reduced-support exterior Euler coefficient 与坐标
projectors 都能精确实现该规则；困难不在是否存在 selector，而在它能否避免存储
每个收到的颜色。

答案是一个严格的 character-rigidity 定理。对 $m$ 个颜色，determinant convention
下的 Hankel rank 与 observable syntactic algebra 分别为

$$
m,\qquad \mathbb C^m;
$$

literal nonempty-language convention 则多一个 dormant mode，成为
$m+1$ 与 $\mathbb C^{m+1}$。任何有限 ordinary trace realization 的半单化都
含每色恰一个一维 character；任何 even $\mathbb Z/2$-graded realization 在
Grothendieck 群中也有同一净颜色类。额外自由只能是 dormant 模、偶奇配对模与
迹不可见 radical，因此完整 graded determinant 被强制为

$$
\prod_{i=1}^{m}(1-zx_i).
$$

这里不声称原矩阵同时对角化：非交换上三角扩张可以让 presentation 看似连通，
却不改变任何 cyclic trace 或 determinant。一个三颜色 exact adversary 还证明，
只检查 commuting pencil 的 aggregate power traces 不够；所有聚合检查可同时通过，
而两个反向 mixed words 仍分别留下 supertrace (+1) 与 (-1)。

把 selector 与 Paper 25 的 holomorphic de Rham sector 张量后，确有
$\Re s>1$ 上 honest degreewise trace-class graded ratio，但 countable color fiber
酉等价于 supplied labels 的 disjoint atom sum。58/58 tests、51,734 条 exact rows
与 27 个双跑 byte-identical artifacts 验证了 wordwise、Hankel、radical、graded、
de Rham、marker 与任意库存 firewalls。阶段结论是
**GO_EXACT_PURE_POWER_SELECTOR / GO_CHARACTER_RIGIDITY /
STOP_FINITE_RECOGNIZABLE_ESCAPE / SEMISIMPLE_ATOM_BLOCK_COLLAPSE /
PROVES_TOO_MUCH / ROUTE_A_REJECTED**。Paper 27 因而不再供应颜色投影，而从固定
integer factorization/divisibility source 内生编译 atom idempotents；Route B 继续锁定。

### 论文 27：source-derived atom ledger 通过，但 incidence compiler 有界相似于原子表

Paper 27 不再接收 prime list、颜色表或 prime-power coefficient table，而只冻结
整数对象的 divisibility poset。底元 $1$ 的 covers 从 source relation 内生给出
tensor atoms；若 $Z$ 是 incidence zeta、$M=Z^{-1}$、$E_n$ 是坐标 idempotent，则

$$
q_n=ZE_nM,\qquad q_nq_m=\delta_{nm}q_n.
$$

用 cover predicate 过滤 $q_n$ 后，每个非空 source word 的 trace 在且仅在它是同一
atom 的 temporal repetition 时等于 $1$；composite source letter、mixed word 与
错误 primitive necklace 都在取迹之前作为算子归零。Elias--gamma digit marker 也
严格保留为 $u^{r\ell(p)}p^{-rs}$，所以这不是 after-the-fact coefficient filtering。

在加权空间

$$
H_\eta=\left\{x:\sum_{n\ge1}n^{2\eta}|x_n|^2<\infty\right\}
$$

上，每个 $q_p$ 是 trace-one rank-one idempotent；当 $\eta>1$ 时，整族满足
$q_p=ZE_pZ^{-1}$，其中 $Z$ 与 $Z^{-1}$ 都是有界算子。因此 marked transfer 与
holomorphic de Rham graded ratio 都给出 honest atom Euler product，却与坐标
atom table 有界相似。特别在 $u=1$ 时，特征值 $p^{-s}$ 强制 trace-class 域恰停在
$\Re s>1$；scalar meromorphic continuation 不能冒充同一算子的 continuation。

61/61 tests、2,384 条 exact/control/comparison rows 与 30 个 fresh double-run
byte-identical artifacts 验证了 incidence inversion、cover atoms、逐词 selector、
necklaces、marker、weighted Hilbert formulas、bounded similarity、de Rham ratio 与
mutated-poset controls。阶段结论是 **GO_SOURCE_DERIVED_ATOM_ORBITS /
GO_EXACT_NECKLACE_LEDGER / A1_PASS_ANALYTIC /
STOP_INCIDENCE_SIMILARITY_COLLAPSE / STOP_CRITICAL_STRIP_CONTINUATION /
ROUTE_A_REJECTED**。Paper 28 因而只保留同一 incidence parent 的原生 Gram 几何，
检验其 chiral/adjoint completion 是否能在临界线产生非平凡、算术可选择的谱运动；
Route B 继续锁定。

### 论文 28：临界线谱确实运动，但正定自然度量与算术选择性形成三难

Paper 28 对 Paper 27 的同一 Möbius-incidence compiler 作一次 source-real 的
holomorphic reflected completion：

$$
\mathcal B_s=
\begin{pmatrix}
0&T_s\\
T_{1-s}^{\sharp}&0
\end{pmatrix}.
$$

由于 $T_s$ 与 atom diagonal 有界相似，严格的 Schatten 条件是

$$
\mathcal B_s\in\mathcal S_q
\quad\Longleftrightarrow\quad
\frac1q<\Re s<1-\frac1q.
$$

因此 $q=3$ 是第一个覆盖临界线的整数阶；在 $s=\tfrac12+it$ 上，
$\mathcal B_s$ 是 compact self-adjoint，但不属于 $\mathcal S_2$。原生 oblique
idempotents 的 mixed Gram coefficient 满足

$$
G_{pq}=C_\eta\,
\frac{(pq)^{-2\eta}}
{(1+p^{-2\eta})(1+q^{-2\eta})}>0,
$$

而 $\operatorname{Tr}\mathcal B_s^4$ 在频率 $2\log(q/p)$ 上有唯一正系数
$4G_{pq}^2/(pq)$。所以临界线上的谱运动不是数值幻觉或单边 gauge；
$\det_3(I-z\mathcal B_s)$ 的解析 germ 确实随 $t$ 变化。

这条正面结果同时给出更锋利的停止定理。二阶 mixed-Gram 项在 finite cutoff 中
已随 $t$ 运动，但 countable diagonal 部分含 $\sum_p p^{-1}$ 而发散；$\det_3$ 恰好删掉
幂次 $1,2$，首个诚实可见项只能到幂次 $4$。更重要的是，mutated divisibility、
composite-only atoms 与 seeded generic DAG 都复制同型运动，说明它是 generic
oblique-incidence geometry，而非 arithmetic selector。

若要求一个 bounded positive metric $G$ 使所有 active $q_p$ 自伴，则

$$
Z^*GZ
$$

必须在 active coordinates 上对角。相应 Hellinger/Löwdin 变换把整族酉化为独立
atom blocks，并把手征 determinant 压成

$$
\prod_p\left(1-\frac{z^2}{p}\right)e^{z^2/p},
$$

完全失去 $s,t$。61/61 tests、154 条 exact/control/comparison rows 与 30 个
fresh double-run byte-identical artifacts 验证了 Gram 公式、Schatten strip、
finite-$B^2$ firewall、唯一四阶频率、metric rigidity、phase-free product、marker
ownership 与三类 adversarial controls。阶段结论是 **GO_SCHATTEN3_CHIRAL_FAMILY /
GO_EXACT_FOURTH_MOMENT_MOTION / STOP_ARITHMETIC_SELECTIVITY /
STOP_POSITIVE_METRIC_COMPLETION / STOP_FIXED_HILBERT_POLYA_OPERATOR /
ROUTE_A_REJECTED**。Route B 继续锁定；下一批最小义务是分类 source-natural 的
$B^2$ counterterms，而不是再叠加任意 block completion。

### 论文 29：二阶反项可自然构造，但 finite part 不唯一且 mixed residue 无选择性

Paper 29 保留 Paper 28 的同一 incidence-chiral family，并分解 finite-cutoff 二次型

$$
Q_F(t)=2\sum_{p\in F}\frac{G_{pp}}p
+4\sum_{p<q\in F}\frac{G_{pq}}{\sqrt{pq}}
\cos\left(t\log\frac qp\right).
$$

对 $\eta>1$，mixed 项绝对可和，而 diagonal 项的唯一发散 germ 是
$2C_\eta\sum_pp^{-1}$。然而 leading-only 与 full-diagonal 两个同样自然的减法相差

$$
2C_\eta\sum_pp^{-1-2\eta},
$$

这是一个非零、绝对可和且 atom-local 的 finite scheme shift。因而自然性与收敛性
只能固定发散 germ，不能唯一固定 finite part。

更强的负结论是 pair-local linear-Gram 选择器的精确二择一：保留
divisibility baseline 的 mixed pair 强制 $\beta=0$，而消去同一 transported local type
的 controls 则强制 $\beta=1$。因此不存在同时满足两者的局部自然反项。

602/602 independent checks、23/23 tests、76 个 baseline mixed/$B^4$ pairs、四类 controls 与
49 组预注册系数网格共同验证了这一分类。把 finite part 补回 $\det_3$ 只会乘上
zero-free quadratic exponential；它是新的 scheme-dependent functional，不是 ordinary Fredholm
determinant 或 $\det_2$，也不改变辅助变量的 divisor。阶段结论是
**GO_SCOPED_RENORMALIZATION_RIGIDITY / STOP_CANONICAL_FINITE_PART /
STOP_PAIRWISE_ARITHMETIC_SELECTIVITY / ROUTE_A_REJECTED**。非局部 filtered-tower invariant
尚未被这个定理覆盖；Paper 30 只测试这一剩余漏口，Route B 仍锁定。

### 论文 30：整除 incidence 的全部自然统计都被自由 UFD clone 复制

Paper 30 将 Paper 29 留下的非局部漏口扩展到完整的 join、Möbius 与 connected-cumulant
数据。唯一分解给出 source-preserving 同构

$$
(\mathbb N_{\ge1},\mid,\operatorname{lcm},\mu)
\cong
(\mathbb N^{(\mathcal P)},\le,\vee,\mu_{\rm prod}),
$$

并同时运输 atom covers、有限 cutoff、entropy roof 和 admissible Gram decoration。因此，
任何在这一 decorated source 的同构下自然的 pair、triple、任意固定 arity 或全局
filtered-tower functional，都不可能在整数 baseline 非零而在所有 formal free/UFD controls
上为零。

精确实验展示了这个边界为何必须由定理关闭：Boolean-join connected triple statistic
在三个整数 baselines 上非零，并在 mutated-cover、composite-only、generic-DAG 与 random
有限 fixtures 上为零；但 transported free-commutative 与 polynomial-UFD clones 逐项复制
全部 pair/triple、31 个 predicate masks、markers 与 analytic auxiliary determinant。28/28 tests、
1616/1616 independent checks 和 17 个双跑工件均通过。

这不是系数选择失败，而是可见 source 数据的同构不可能性。阶段结论为
**GO_FREE_UFD_CLONE_THEOREM / STOP_INCIDENCE_CUMULANT_SELECTOR /
CLOSE_CHIRAL_INCIDENCE_COUNTERTERM_BRANCH / ROUTE_A_REJECTED**。Route B 继续锁定；
Paper 31 只有在先引入并证明一个不被 valuation 同构运输的 source-derived 非乘法操作
（例如加法–乘法兼容结构）后才允许建立新候选。

### 论文 31：加法击穿裸 clone，但 matched semiring、剪枝与 clock dilution 封路

Paper 31 把 finite full shifts 的 alphabet sum 与 Cartesian tensor 同时纳入 source，
从而重建 characteristic-zero semiring。这个扩展确实比 Paper 30 更强：普通 polynomial-UFD
monomial clone 已在 $1+1$ 处失败。但只要 control 也运输完整的
$y_m\boxplus y_n=y_{m+n}$ 与 $y_m\otimes y_n=y_{mn}$，全部 Wilson residue paths、
周期、roof 与 marker 又逐项一致。

无 primality table 的 Wilson stationary grammar 对每个素数 $p$ 产生唯一长度 $p-1$ 的
primitive cycle，形式周期积为

$$
\prod_p\left(1-z^{p-1}p^{-s}\right).
$$

它只在 $z=1$ 退化为 $1/\zeta(s)$。更关键的是，把总 roof $\log p$ 分配到
$p-1$ 条边会强制近单位权边，因此原始 recurrent adjacency 非紧且不属于任何有限
Schatten 类。Poincaré first return 虽在 $\Re s>1$ trace class，却把 marker
$z^{p-1}$ 收缩为 $z$；transient verifier 则从 power traces 中完全剪除计算状态。

cutoff 4096 的 564 个素数全接收，3531 个合数和 13 个 Fermat 伪素数全拒；
matched clone 的 169 项运算与全部 paths 精确复制。26620/26620 independent checks、
direct 与 isolated runner 各 18/18、完整树可重复 integrity audit 和 16 个双跑工件
均通过。阶段结论为 **GO_BARE_CLONE_SEPARATION / STOP_MATCHED_SEMIRING_SELECTIVITY /
STOP_WHOLE_FREDHOLM / CLOSE_TERMINAL_SEMIRING_VERIFIER_BRANCH /
ROUTE_A_REJECTED**。Paper 32 必须改用无 accept/reject terminal 的共享 recurrent grammar。

### 论文 32：共享 residue recurrence 获得 Fredholm ownership，但普适关系淹没 primitive ledger

Paper 32 将 terminal verifier 替换为真正共享状态的非终止系统。每个模数
$n$ 使用

$$
X_n=P^1(\mathbb Z/n\mathbb Z),\qquad
S[a:b]=[-b:a],\quad R[a:b]=[-b:a+b],
$$

并以双向 cusp maps 连接 $n,2n,3n$。这个 uninduced graph-step operator 在
$\Re s>2$ 上 trace class 且 trace-norm holomorphic，因此普通
$\det(I-zB_s)$ 确实属于同一 recurrent object；Paper 31 的 whole-operator
ownership 缺口被实质修复。

然而 primitive ledger 在任何 roof 之前已经失败。projective action 恒满足

$$
S^2=R^3=1,
$$

所以 primes、prime-power composites 与 mixed composites 都具有同型 recurrent
cycles。更强地，每个 $n\ge2$ 都产生非回溯 primitive diamond

$$
c_n\to c_{2n}\to c_{6n}\to c_{3n}\to c_n,
$$

其顶点 $6n$ 必为合数。静态等式
$|P^1(\mathbb Z/n\mathbb Z)|=n+1$ 虽精确刻画素数，但用它删减 blocks 就是把
完成的 field/primality test 重新作为 terminal gate，违反 source lock。

cutoff $2\le n\le192$ 的 191 个模数中，全部 148 个合数都有 recurrent support，
31/31 cusp diamonds 顶点为合数，48/48 random $C_2*C_3$ actions 复制普适 recurrence，
191/191 matched finite-semiring clones 逐项运输完整加乘表与 projective graph。
4,819,026/4,819,026 independent checks、13/13 assertions、16 个 fresh double-run
工件均通过。阶段结论为 **GO_NONTERMINAL_SHARED_RECURRENCE /
GO_SAME_OBJECT_FREDHOLM / STOP_PRIMITIVE_LEDGER /
STOP_PROVES_TOO_MUCH / CLOSE_EUCLIDEAN_PROJECTIVE_RESIDUE_RECURRENCE_BRANCH /
ROUTE_A_REJECTED**。Paper 33 只允许在同一 object 上测试 source-natural
cycle-level quotient/twist；若它不能在 chain level 同时消去 $S^2$、$R^3$ 与 cusp
diamonds，整个 semiring-residue family 即关闭。

### 论文 33：Manin quotient 杀掉普适关系，但 operator 不下降并关闭 residue family

Paper 33 执行 Paper 32 留下的唯一合法 continuation：保持同一
$P^1(\mathbb Z/n\mathbb Z)$ recurrent object、同一 cusps/roofs/marker，只在
chain level 取

$$
M_n=\mathbb Q[P^1(\mathbb Z/n\mathbb Z)]/
\bigl(\operatorname{im}(1+S)+\operatorname{im}(1+R+R^2)\bigr)
$$

并填入每个 $n,2n,6n,3n,n$ cusp diamond。这个 quotient 正是 classical
Manin-symbol relation module；精确公式为

$$
\dim M_n=|P^1(\mathbb Z/n\mathbb Z)|-o_S(n)-o_R(n)+1.
$$

它虽然杀掉 universal chain relations，却仍对每个 $n\ge2$ 保留
$[1:0]\xrightarrow{R}[0:1]\xrightarrow{S}[1:0]$ 的 primitive nonbacktracking
survivor。cross diamonds 被填充后，cross grid contractible，只剩
$H_1=\bigoplus_n M_n^\*$；ordinary $H^1$ 是 product，项目只使用 finite-support
ledger $L_{\rm fs}=\bigoplus_n M_n$。character firewall 也封死：0/6 honest
characters 杀 identity cycle words，2/6 能杀 both Manin chain norms，但 cusp
$SR$ 仍是非零相位；15/15 zero-superdimension differences 杀 identity words，
其中 2/15 杀 both chain norms，但全部保留 cusp $SR$。

最强 analytic obstruction 是 operator non-descent。原始 graph-step adjacency
$S+R$ 不保持 Manin relation subspace，$n=2$ 三状态块已给出反例；因此
$\bigoplus_n n^{-s}I_{M_n}$ 虽在 $\Re s>2$ trace class，也只是 scalar homology
comparison，不是同一 free-marker graph-step determinant。cutoff $2\le n\le192$
中 191/191 relative quotient nonzero、148/148 composite survivors、0/191
adjacency descents、64/64 random controls residual nonzero；source-only 21/21、
prototype bridge 25/25、independent reconstruction 8349/8349、authority
unit/integration 1932/1932 与 fresh double-run 20/20 均通过。完整 source/results
账本为 40 条，SHA-256 为
`0cb14d9b25e313f6c34d53983fb01a869175838461cd7e2ca9f27fd0b29d8f30`。
阶段结论为 **GO_RELATION_HOMOLOGY_NO_GO_PAPER /
STOP_OPERATOR_NON_DESCENT / STOP_PROVES_TOO_MUCH /
CLOSE_SEMIRING_RESIDUE_FAMILY / ROUTE_A_REJECTED**。下一批不应继续
projective-residue/Manin quotient，而应转向一个 primitive recurrence 在
block projector 之前已内生生成 Euler factors 的 global arithmetic source。

### 论文 34：正标量识别编译器在 recurrence、Fredholm 与时钟之间四重封路

Paper 34 把此前分散在 terminal verifier、有限码与 clock-dilution 分支中的停止条件
统一为一个 quantifier-clean 的同对象定理。对 one-sided、正标量、有限
orbit-separating alphabet 的 countable Markov graph，若每个 arithmetic atom $a$
具有精确 primitive cycle、总 roof $log N(a)$，并保留原始 graph-step marker $z$，
则 literal atom-only ledger 强制这些 cycles 落在彼此分离的 recurrent components。
若两条 declared cycles 属于同一 strongly connected component，任取双向连接路径
$\alpha,\beta$ 后，闭词

$$
W=\gamma_a\alpha\gamma_c\beta
$$

的 primitive root 同时使用两圈的边，因此产生额外 mixed primitive orbit。这里不再
要求连接路径的 interiors 避开两圈；预注册中这一过强 normal form 被精确反例否定，
而修正后的 SCC 命题得到完整验证。

如果 whole vertex operator 属于 trace class，全部非循环识别边都从每个 power trace
与 Fredholm determinant 中剪除；计算层对 determinant 不可见。另一方面，有限局部
可分离性与 primes 的多项式增长迫使无穷子列满足

$$
\ell(p)\ge \frac{\log p}{4\log b}.
$$

把总 roof $\log p$ 分到这些长圈上，必产生一致远离零的 edge weights；原始 whole
operator 即使有界也非紧，更不属于任何有限 Schatten 类。Poincaré first return 虽把
循环压成 trace-class diagonal，却同时把
$1-z^{\ell(p)}p^{-s}$ 改成 $1-zp^{-s}$；二者只在 $z=1$ 遗忘时钟后相等。

完整 $n\le4$ 的 66,066 个图与 64 个确定性 seeded controls 共审计
844,544 个修正后 mixed-root constructions，全部通过；同时公开保留原 C2 normal
form 的 18,272 个反例。76/76 tests、85/85 integrity checks、20/20 scientific
checks，以及 fresh/cold/idempotent 双跑均通过。阶段结论为
**GO_QUANTIFIER_CLEAN_NO_GO_SYNTHESIS / STOP_POSITIVE_LITERAL_COMPILER /
STOP_WHOLE_FREDHOLM / STOP_MARKER_CHANGING_FIRST_RETURN /
CLOSE_POSITIVE_RECOGNITION_COMPILER_BRANCH / ROUTE_A_REJECTED**。
signed、matrix、nonpositive、infinite-hidden-alphabet 与 nondeterministic cancellations
均明确留在定理范围之外；Paper 35 转向 affine-semigroup/Bost--Connes object firewall，
不把这些边界误报成已关闭。

### 论文 35：affine source 的 acyclicity、relation cycles 与 Gibbs object firewall

Paper 35 冻结全正 affine semigroup
$P=\mathbb N_0\rtimes\mathbb N^\times$ 的 right Cayley source，并用有限生成切片
$P_r=\langle u,v\mid vu=u^rv\rangle^+$ 给出自然 whole-operator benchmark。正向边使
$h(b,a)=b+a$ 严格增加，所以源图没有闭路；加形式逆边后，每条边都产生两步
backtrack。Hashimoto reduction 虽删除 immediate reversals，却保留长度 $r+3$ 的
primitive relation word

$$
vu\bar v\bar u^r.
$$

这些关系环对 prime、composite 与 prime-power 的 $r$ 一视同仁。有限 congruence
quotients 同时保留 relation word 并新添 $U_q^q$ translation cycles，因此不会忠实
下降完整 primitive ledger。有限生成切片上的 positive、symmetric 与 Hashimoto
operators 虽有界，却都由平移正交列证明非紧；full all-$n$ adjacency 甚至具有无穷
outdegree，不能在一个 basis vector 上定义为 $\ell^2$ 向量。

Bost--Connes diagonal Gibbs operator 则是另一个诚实 trace-class 对象：

$$
\operatorname{Tr}(D_\beta)=\zeta(\beta),\qquad
-\log\det(I-zD_\beta)=\sum_{m\ge1}\frac{z^m}{m}\zeta(m\beta).
$$

所以 partition trace 只是 connected Fredholm logarithm 的 $[z]$ 系数；prime-Fock
Euler product又从一开始使用 prime-indexed one-particle basis。exact audit 含
699,040 个 frozen words、126,553 个 admissible words、88 个 primitive cyclic-NB
classes 与 48 个 quotient fixtures；84/84 tests、10/10 independent gates 及 23 个
fresh/cold scientific artifacts 全部通过。阶段结论为
**STOP_POSITIVE_AFFINE_RECURRENCE / STOP_RELATION_CYCLE_POLLUTION /
STOP_PARTITION_TRACE_IDENTIFICATION / CLOSE_AFFINE_SEMIGROUP_PARTITION_IDENTIFICATION_BRANCH /
ROUTE_A_REJECTED**。Paper 36 只允许在同一 uninduced symbolic object 上测试
source-natural chain cancellation，并必须同时保留原 marker 与非零 recurrent sector。

### 论文 36：完整 relation filling、marker non-descent 与 prequotient determinant 分离

Paper 36 在 Paper 35 的同一 affine presentation family

$$
M_r=\langle u,v\mid vu=u^rv\rangle^+
$$

上测试最直接的 chain-level repair。形式逆边与 Hashimoto rule 先删除 immediate
backtracks；随后在每个 vertex 填入定义关系的 Cayley $2$-cell。Gray--Steinberg 的
已知 contractibility 定理在这里适用，因此完整 filling 使 $K_r$ 契约，全部正次数
homology 与 primitive recurrent classes 同时消失。该拓扑结论不被冒充为新定理；
本文的新边界是它与原时钟及同对象解析所有权的组合不相容。

关系 cell 比较长度 $2$ 的 $vu$ 与长度 $r+1$ 的 $u^rv$。任何取值于 torsion-free
Abelian group 的 cell-invariant additive degree 都满足

$$
(r-1)\deg(u)=0,
$$

所以原始 unit generator-step marker 不可能下降。与此同时，在完整、未诱导的
oriented-edge space 上，source-coordinate damping
$T_{r,\theta}=D_\theta H_rD_\theta$ 是 trace class；长度 $r+3$ 的 affine relation
polygon 给出严格正的 $\operatorname{Tr}(T_{r,\theta}^{r+3})$。因此空 chain quotient
与该 ordinary Fredholm determinant 不是同一 determinant-bearing object。

标量 cellular superlift 虽在每个 power 上给出 $1-2+1=0$，但这一结果只读
cell-orbit multiplicity，任意 two-generator one-relator presentation 都同样通过，
故属于 **PROVES TOO MUCH**。canonical exact audit 中 source 与 prototype 各通过
33/33，独立 evaluator 通过 35/35，authority suite 通过 53/53；19 个科学 payload
在 fresh A/B 与 cache-free cold C 间逐字节一致，最终有 27 个 result files、74/74
integrity checks 与 43-entry immutable ledger；Route provenance 独立审计并在
metadata stage 配对绑定。阶段结论为
**STOP_TOTAL_RELATION_FILLING / STOP_MARKER_NON_DESCENT / STOP_OBJECT_MISMATCH /
STOP_GENERIC_SUPERCANCELLATION / ROUTE_A_REJECTED**。Paper 37 只允许在同一
unquotiented、same-marker Hashimoto object 上测试 source-derived non-flat
finite-rank local coefficients；不得转向 first return、KMS/GNS、prime basis、
有限 quotient 或另一个 determinant。

### 论文 37：direct-relator cancellation、mixed leakage 与 normal-closure saturation

Paper 37 保持 Paper 36 的同一 unquotiented affine Hashimoto path space、原始一步
marker 与 source-coordinate damping，只允许在边上传递一致有界的有限秩可逆
local coefficients。对单个 primitive orbit，完整 ordinary matrix Euler factor
消失当且仅当 holonomy 的全部幂迹为零；有限维情形这等价于 holonomy nilpotent，
因此真正可逆的 local system 连一个完整 primitive factor 都不能删除。

平衡 graded rank-two shear 可在所有 repetitions 上消去定义 relator 及其 conjugates，
但显式 primitive mixed word $M_r$ 满足

$$
\operatorname{Str}W(M_r)=-4r^4(r-1)\ne0 \qquad (r\ge2),
$$

所以只杀基本 relation cells 会发生 mixed leakage。若把取消义务扩展到整个
normal closure，则 affine Cayley $2$-complex 的单连通性把每条 closed word 都纳入
饱和类，最终 graded ledger 为空且 $Z_{\mathrm{gr}}(z)=1$。这给出“泄漏或全部清空”
的严格二择一，而不是选择性算术机制。

canonical exact audit 通过 131/131 个独立 source/evaluator assertions、32/32 个
authority integration tests 与 82/82 个 integrity checks；8/8 个 frozen affine
fixtures 均取消 direct factor 且 8/8 泄漏，random controls 中所有满足 direct
cancellation 的实例也都发生 conditional leakage。26 个 result files 与 39-entry
immutable ledger 完整闭合。阶段结论为
**STOP_LOCAL_COEFFICIENT_SATURATION / ROUTE_A_REJECTED / ROUTE_B_LOCKED**。
Paper 38 只允许测试对冻结 ascending-HNN splitting/presentation canonical 的
Bass--Serre tree geodesic shift 与其 canonical modular cocycle，并必须明确属于新对象；若 primitive ledger 为空、发散、
被 generic controls 复制或 marker 不兼容，则关闭整个 affine branch。

### 论文 38：满树空 ledger、orbital necklace 与 affine branch closure

Paper 38 按 Paper 37 的最后义务转到对冻结 ascending-HNN splitting/presentation
canonical 的 Bass--Serre tree，并明确声明这是新对象、不给 same-object
或 same-marker credit。满树本身是一棵树，所以没有任何正长度 reduced closed
path，geodesic primitive ledger 为空；其 full oriented-edge Hashimoto operator
在正则树上保留无穷个等范数正交列，因此非紧、非迹类，也不拥有 ordinary
full-tree Fredholm determinant。

tree-lattice determinant 的适用边界也被精确分案：当 $r\ge2$ 时作用忠实且其
$\operatorname{Aut}(T_r)$ 像非离散；当 $r=1$ 时平移像 $\mathbb Z$ 虽离散，原
$\mathbb Z^2$ 作用却有无限核 $\langle u\rangle$、非 proper 且稳定子无限。两种
情形都不满足 frozen finite-stabilizer tree-lattice hypotheses；商到忠实像会改变
作用群与 orbital ledger。

若另行抽取正 height 的 group-conjugacy classes，则 $r\ge2$ 只得到通用 necklace
计数

$$
P(1)=r-1,\qquad
P(k)=\frac1k\sum_{d\mid k}\mu(d)r^{k/d}\ (k>1),\qquad
Z_+(z)=\frac{1-z}{1-rz}.
$$

canonical modular specialization 是
$\bigl(1-r^{-s}z\bigr)/\bigl(1-r^{1-s}z\bigr)$；它只依赖 HNN index，
被 prime、composite 与 generic GBS controls 同样复制。$r=1$ 的 group-conjugacy
替代在每个正 height 都发散，而 Bass--Serre clock 又把旧 Cayley generator-step
marker 压缩成 signed tree height，故不是原对象的 continuation。

修正后的 canonical exact audit 通过 277/277 个 evaluator assertions、44/44 个
integration tests 与 96/96 个 integrity checks；fresh A/B 与 isolated cold C 的
source、science 和 Route 字节一致；隐藏全部 `/tmp` provenance 的 clean clone
保持 science、Route、report 与 integrity audit 字节一致；第二次 authority 全量
复跑的 changed paths 为零。最终有 28 个 result files 与 42-entry immutable
ledger。阶段结论为
**STOP_BASS_SERRE_TREE_BRANCH / CLOSE_ENTIRE_AFFINE_BRANCH /
ROUTE_A_REJECTED / ROUTE_B_LOCKED**。Paper 39 只允许形成 affine-branch closure
obstruction DAG 并把控制权交回全局 Symbolic Dynamics registry；不得再换一个
affine representation 重开候选。

### 论文 39：retrospective typed closure audit 与 registry handoff

Paper 39 不引入新的相空间、表示、算子、determinant、marker 或算术 source。它在
Papers 35--38 的结果已知之后，把这些 content-addressed outcomes 组装成一个只对
自身有限域负责、并在本轮 checker 运行前冻结的 typed audit。可执行 structural
spine 有 6 个节点与 5 条边；保留全部证明证据的 expanded DAG 有 22 个节点、28
条 typed edges 与 17 个 internal transition tags。二者之间是带显式 fibers 的
total many-to-one projection，而不是同构或可逆压缩。

冻结域恰含 14 个 repair classes 与 16 个 request tokens。类级 census 为
6 `OBSTRUCTED`、6 `EXIT_ONLY`、2 `MIXED`；token 级 census 为 8 obstruction、
8 EXIT。EXIT 只声明离开冻结对象类别，不计作 `Good` 的失败。E22 是域外历史
firewall，其 class/token fibers 为空且不给 closure credit；P36→P37 的 coarse
edge 则在 P37 source lock 下把 object、marker、operator owner 与 determinant
owner 四个候选状态字段全部 `RESET`，历史 provenance 仅作 non-state audit
metadata，不能偷渡 candidate identity。

authority exact integration 通过 535/535 个 main assertions、278/278 个独立
evaluator assertions、两套 evaluator 各 29/29 个 adversarial mutations，以及
224/224 个 integrity checks。Fresh A/B、cold C、隐藏外部 provenance 的 clean
clone、模拟 sealed State B 与两次完整 runner 均字节稳定；State A 的 pending
triple/manifest-absent 审计和 State B 的 sealed triple/self-excluding manifest 审计
逐字节相同，11/11 个混合或伪造状态全部被拒绝。36 个 exact result files、39 个
managed outputs 与 65-entry immutable ledger 闭合。严格 Route tuple 为
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`，Route B locked。阶段结论为
**CLOSE_ENTIRE_AFFINE_BRANCH / ROUTE_A_REJECTED /
RETURN_CONTROL_TO_PREEXISTING_GLOBAL_CANDIDATE_REGISTRY**。这个 handoff 不排名、
不选择、也不授权 Paper 40；若继续，下一篇必须另行 source-lock 一个非 affine
候选。`STOP_NO_SOURCE_LOCKED_NON_AFFINE_SUCCESSOR` 只是在独立空 registry fixture
中执行过的条件 fallback，不是当前 realized terminal。

### 论文 40：two-digit Gauss--Mayer 的三投影与 ownership firewall

Paper 40 独立采用 literal six-card rule：historical card 必须同时具有非空的
intrinsic primitive/repetition ledger 与 exact proved verdict
`A2_ANALYTIC_DETERMINANT`。`SD-C01`、`SD-C02`、`SD-C04` 通过首层筛选，
`SD-C04` 再按冻结的 A3、A4 次序胜出；Paper 39 只提供 terminal-clean promotion
provenance，不参与排名、选择或授权。本文把 digit space $X=\mathbb N^{\mathbb N}$
上的 $\sigma$ 与 pair space $X_2=(\mathbb N^2)^{\mathbb N}$ 上的一对移位 $\rho$
分开，并用 grouping bijection $\iota$ 证明
$\rho\circ\iota=\iota\circ\sigma^2$。因此 `SigmaPrimitiveDigit`、
`RhoPrimitivePair` 与 `GeodesicPrimitiveClass` 始终是三个不同类型。

正向结果属于 pair object 自身。令 $K_s=\mathcal L_s^2$、
$D_{42}(s,u)=\det(I-u^2K_s)$，则在 Mayer nuclear half-plane 内、形式地关于
$u^2$（或充分小 $|u|$）有 intrinsic primitive-pair Fredholm regrouping；$u=1$
的 Selberg-zeta/Fredholm equality 只作为函数恒等式使用，不导入逐 orbit 的
pair/geodesic 对应。对冻结的三个标量投影

$$
P_t=t,\qquad P_\Delta=t^2-4,\qquad P_N=\lambda^2,
$$

本文逐列关闭 rational-prime ledger。$\Delta=(t-2)(t+2)$ 只在边界值
$(t,\Delta)=(3,5)$ 为素数，$\lambda^2$ 为无理数；trace 与 order discriminant
不保 temporal powers 或 derivative clock，norm 虽精确保 clock 与 powers 却不在
rational-integer support。trace $4$、$6$、$10$ 的三类 exact collision 关闭
one-to-one multiplicity，Mayer stability denominator 关闭 target amplitude，而冻结的
untwisted schema 没有声明任何 scalar-prime postselection 的 reducing owner。结论只对
这三个投影和这个 operator schema 成立，不是 twists、changed objects 或全部 dynamical
zeta constructions 的 universal no-go。

authority final integration 中，main 与 independent evaluators 分别通过 210/210、
208/208；scientific projection SHA-256 为
`340aff6f08e7cf9360d57d34ff9c66e99f9322343b3069fe37e5acc2f55aa7c5`。
integrity audit 通过 83/83，102/102-entry ledger、54 个 result files、2 个 evaluation
files 与 1 份 experiment report 闭合。两套 evaluator 各拒绝全部 164 个 packet
mutations；Route 的 422 次执行由 24 个 explicit 与 398 个 exhaustive recursive
mutations 组成，覆盖 409 个 distinct payloads，18/18 strict checks 通过；hidden
cold-copy 第二次完整运行的 changed paths 为零。

严格 Route tuple 为
`(A0_WEAK_ARITHMETIC_RELATION,A1_PASS_ANALYTIC,A2_ANALYTIC_DETERMINANT,`
`A3_PARTIAL_ANALYTIC_STRUCTURE,A4_FORMAL_HINT)`，Route B locked。阶段结论为
**GO_MODULAR_PRIMITIVE_LEDGER / GO_SAME_OBJECT_MAYER_DETERMINANT /
STOP_CANONICAL_INTEGER_PROJECTION /
STOP_RATIONAL_INTEGER_CLOCK_REPETITION_CONJUNCTION /
STOP_OPERATOR_VISIBLE_SELECTOR_NOT_OWNED / ROUTE_A_REJECTED**。两个 GO 只给予
intrinsic pair ledger 与 same-object Mayer determinant 正向 credit，不给予
rational-prime、digit-primitive 或 geodesic-primitive credit。

### 论文 41：rooted clock 不下降，inventory determinant 分型保留

Paper 41 只关闭冻结的 `SD-C06` rooted-label test。对
`h(w)=1^T M_w e_1`，trailing-zero relation 保留 source state，却不支持
right append-one 的 well-defined quotient action；ordinary rotations 与 word
powers 又分别破坏 cyclic clock 和 temporal-power law。literal
`lambda(h(w))` 同时失去 cyclic 与 repetition character。该结论不量化到
trace/eigenvalue clocks、扩大的 states、non-scalar cocycles、Farey/Gauss/
Selberg 或 adelic models。

另一方面，stable-state inventory 上的 diagonal `Q_s` 在 `Re(s)>2` 为
trace class，并拥有 `det(I-uQ_s)`；其 local trace-log 只在 `|u|<1`
使用。这个 marker 计数 inventory eigenvalue powers，不是 binary primitive
returns，因此不把 A2 或 A4 改成通过。严格 Route tuple 为
`(A0_ANALYTIC_ARITHMETIC_ORIGIN,A1_FAIL,A2_FAIL,A3_PARTIAL_ANALYTIC_STRUCTURE,A4_FAIL)`，
overall 为 `ROUTE_A_REJECTED`，Route B 为 false。

authority canonical replay 的 main/independent checks 为 `24/24` 与 `25/25`；
science SHA-256 为
`f9cbcde9a757896b976ad81a66f235d670029f727b6fda9b4e851846bac50bec`，integrity
audit 为 `51/51`、SHA-256
`cf16ba60ca4a45e3e31c5e48590c7cafd69d45694ab343cecf0076476f936d5e`，result
ledger 为 79 entries、SHA-256
`25f7aa42c6d55d7608509dbe1b66586bda6db98120ba450f5b59a5c6f3d19f99`。
selection、witness 与结果均为 retrospective；Paper 39 只提供 existence
provenance，不 ranking/authorize 本 successor，Paper 40 也不提供 selection
或 novelty credit。

## 目录

- [研究提案](propose-symbolic-dynamics.md)
- [Route-A evaluator](skills/route-a-evaluator.md)
- [Route-B evaluator](skills/route-b-evaluator.md)
- [prior-work 与共享文档](docs/)
- [四十一篇论文](papers/)

根目录不再设置项目包装层；每个论文项目各自使用 `PAPER_MANIFEST.sha256` 管理
完整性。本地 PDF/legacy 输入语料和运行缓存不进入 manifests。
