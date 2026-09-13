---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-dyadic-odd-affine-parity-renewal-route-a"
canonical_tex: "henon_dynamics/henon_dyadic_odd_affine_parity_renewal_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_dyadic_odd_affine_parity_renewal_route_a/paper/main.pdf"
source_sha256: "c5191b0367e9e031353a8ffffffdd0ffa3f1cf8b70f669bb7296aa419e459e3e"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact Renewal and Clock Recovery for Odd-Affine Parity Maps on the 2-Adic Integers

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_dyadic_odd_affine_parity_renewal_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_dyadic_odd_affine_parity_renewal_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_dyadic_odd_affine_parity_renewal_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_dyadic_odd_affine_parity_renewal_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For odd integers $a,b$, consider the parity map on the 2-adic integers that sends an even $x$ to $x/2$ and an odd $x$ to $(ax+b)/2$. Classical parity coding conjugates this family to the one-sided binary shift; we use that conjugacy as prior foundation, not as a novelty claim. We derive an exact first-return renewal description on the odd coset. The return time is $\tau(x)=v_2(ax+b)$ with conditional Haar law $2^{-k}$, and the return map is a countable full shift with roof $r(k)=k$. Its ordinary Artin--Mazur series is unavailable because it has infinitely many fixed points, but the roof recovers the original clock: $(1-\sum_{k\ge1}z^k)^{-1}=(1-z)/(1-2z)$, and restoring the zero orbit gives $(1-2z)^{-1}$. Moreover both the unweighted fixed counts and reciprocal 2-adic derivative stability sums are independent of every odd parameter pair. Exact solvability therefore supplies a parameter-blindness obstruction, not an arithmetic target model.
author:
- 'Route-A structural certificate HCS-C174'
title: |
  Exact Renewal and Clock Recovery for\
  Odd-Affine Parity Maps on the 2-Adic Integers
```

## Markdown 正文

suppressoptionalinfo 611

**Keywords:** 2-adic dynamics; parity coding; first return; renewal shift; dynamical zeta; Koopman isometry.

chinese-simplified

中文摘要

对任意奇整数 $a,b$，本文研究二进整数环上的奇偶分支映射：偶点映为 $x/2$，奇点映为 $(ax+b)/2$。经典 [parity]{lang="en"} 编码把该系统共轭到单边二元 移位；本文把这一事实明确视为先验基础，而非新颖性主张。我们在奇数陪集上 推导精确首返 [renewal]{lang="en"}：返回时间为 $\tau(x)=v_2(ax+b)$，条件 [Haar]{lang="en"} 分布为 $2^{-k}$，首返映射是带屋顶 $r(k)=k$ 的可数字母满移位。加速映射因时间一 已有无限多个不动点而不存在普通 [Artin--Mazur]{lang="en"} 级数；但屋顶精确恢复原始时钟， 再补回零轨道即得 $(1-2z)^{-1}$。同时，无权不动点计数与二进导数稳定性权重 对所有奇参数都完全失明。因此，精确可解性给出的是参数盲性障碍，而非算术目标模型。

# Frozen family and ownership boundary

Fix odd $a,b\in\mathbb Z$ and normalized Haar probability $\mu$ on $\mathbb Z_2$. The one-tick map is $$\label{eq:T}
T_{a,b}(x)=
\begin{cases}
x/2,&x\equiv0\pmod2,\\
(ax+b)/2,&x\equiv1\pmod2.
\end{cases}$$ Oddness is structural: each numerator in the active branch is even. The parity vector $Q_{a,b}(x)=\sum_{j\ge0}\epsilon_j(x)2^j$, with $\epsilon_j(x)=T^j(x)\bmod2$, conjugates $T_{a,b}$ to the dyadic shift. Bernstein and Lagarias treated this conjugacy and its odd $ax+b$ generality [@bernstein-lagarias]. We claim no priority for it. The question here is what first-return acceleration does to clock and parameter information.

If $s_j=\sum_{i<j}\epsilon_i$, the inverse parity series is $$\label{eq:inverse}
Q_{a,b}^{-1}\!\left(\sum_{j\ge0}\epsilon_j2^j\right)
=-b\sum_{j\ge0}\epsilon_j2^j a^{-s_{j+1}}.$$ It also shows that $Q_{a,b}$ preserves congruence cylinders and hence Haar measure. Multiplication by $b$ conjugates $T_{a,1}$ to $T_{a,b}$.

# Fixed words and stability blindness

For a word $\epsilon=(\epsilon_0,\ldots,\epsilon_{n-1})$, put $$A_\epsilon=\sum_{j=0}^{n-1}\epsilon_j2^j a^{s_n-s_{j+1}}.$$ Branch induction gives $$\label{eq:iterate}
2^nT^n(x)=a^{s_n}x+bA_\epsilon.$$ Since $2^n-a^{s_n}$ is odd, every word has the unique fixed point $$\label{eq:fixed}
x_\epsilon=\frac{bA_\epsilon}{2^n-a^{s_n}}\in\mathbb Z_2.$$ The parity conjugacy makes all $2^n$ words admissible and distinct. Thus $$\label{eq:counts}
\#\operatorname{Fix}(T^n)=2^n,
\quad P(n)=\sum_{d\mid n}\mu(n/d)2^d,
\quad \zeta_{\rm AM}(z)=\frac1{1-2z}.$$ Here $P(n)$ counts exact-period points, so $P(n)/n$ counts primitive cycles.

The branch derivatives are $1/2$ and $a/2$. On the point with word $\epsilon$, $$(T^n)'=\frac{a^{s_n}}{2^n},\qquad
\left|1-\frac{a^{s_n}}{2^n}\right|_2=2^n,$$ because $2^n-a^{s_n}$ is odd. Consequently $$\label{eq:stab}
W_n:=\sum_{x\in\operatorname{Fix}(T^n)}|1-(T^n)'(x)|_2^{-1}=1,
\qquad \zeta_{\rm stab}(z)=\frac1{1-z}.$$ Equations [\[eq:counts\]](#eq:counts){reference-type="eqref" reference="eq:counts"} and [\[eq:stab\]](#eq:stab){reference-type="eqref" reference="eq:stab"} are all-parameter theorems: both invariants erase $a$ and $b$.

# First-return renewal and clock recovery

Let $O=1+2\mathbb Z_2$. For $x\in O$ with $ax+b\ne0$, define $$\label{eq:return}
\tau(x)=v_2(ax+b),\qquad R(x)=\frac{ax+b}{2^{\tau(x)}}.$$ The point $x_*=-b/a$ maps to zero and has infinite return time. More generally, let $E$ be the set of odd points whose parity strings contain only finitely many ones. Under the parity homeomorphism, $E$ is the union over all finite binary prefixes of one eventually-zero tail; it is therefore countable and Haar-null, and it contains $x_*$. Its complement $O_\infty=O\setminus E$ is invariant under successive returns and has full conditional Haar measure.

The affine map $x\mapsto ax+b$ sends $O$ bijectively and measure-preservingly onto $2\mathbb Z_2$. Hence the normalized Haar layers give $$\label{eq:law}
\mu_O(\tau=k)=2^{-k},\qquad k\ge1.$$ The parity block associated with $k$ is $10^{k-1}$. Concatenation gives a bijection from $O_\infty$ to $\{1,2,\ldots\}^{\mathbb N}$, conjugating $R$ to the left shift. Bernoulli independence of disjoint parity blocks then makes successive returns iid with the geometric product measure. The constant block $k$ has fixed point $$\label{eq:returnfixed}
x_k=\frac b{2^k-a}.$$ Thus $R$ already has infinitely many time-one fixed points and its ordinary Artin--Mazur series is undefined.

Return symbol $k$ represents $k$ original ticks. With roof $r(k)=k$, the first-return series and renewal zeta are $$\label{eq:roof}
F(z)=\sum_{k\ge1}z^k=\frac z{1-z},\qquad
\zeta_{\rm roof}(z)=\frac1{1-F(z)}=\frac{1-z}{1-2z}.$$ Indeed $\log\zeta_{\rm roof}=\sum_{n\ge1}(2^n-1)z^n/n$: these are exactly the original-clock periodic points whose binary words contain a one. The omitted all-zero fixed orbit contributes $(1-z)^{-1}$, and therefore $$\label{eq:recovery}
\zeta_{\rm roof}(z)(1-z)^{-1}=\frac1{1-2z}=\zeta_{\rm AM}(z).$$

# Operator boundary and Route-A decision

On $H=L^2(\mathbb Z_2,\mu)$, $Uf=f\circ T$ is an isometry. It is not surjective: under parity coding, its range consists of functions independent of the first digit. The tail intersection $\bigcap_{n\ge0}U^nH$ consists only of constants, while $H\ominus UH$ is an infinite-dimensional copy of the tail $L^2$ space. The Wold decomposition is therefore $$\label{eq:wold}
U\simeq I_{\mathbb C}\oplus S^{(\aleph_0)}.$$ In particular $\sigma(U)=\overline{\mathbb D}$ and $\sigma_p(U)=\{1\}$. The isometry is noncompact and lies in no finite Schatten class, so no ordinary Fredholm determinant $\det(I-zU)$ is available. The two-sided inverse-limit shift is a same-clock unitary extension, but it changes the phase space and is not a repair of the frozen candidate. Koopman methods have also been studied for the discrete positive-integer $3x+1$ system [@leventides-poulios]; we make no general priority claim for a Collatz Koopman lift.

  --------------------------------------------------------------------------------------------------------------------------------------------------
  Gate               Exact verdict and blocking reason
  ------------------ -------------------------------------------------------------------------------------------------------------------------------
  A0\_FAIL           Dyadic local arithmetic yields no rational-prime labels, prime-power repetition law, or von Mangoldt weight.

  A1\_WEAK           Primitive cycles are complete and reproducible, but have no intrinsic arithmetic labels or target amplitudes.

  A2\_FAIL           The three exact source zetas are elementary and parameter-blind; the accelerated map itself has infinitely many fixed points.

  A3\_FAIL           Rational continuation supplies no target functional equation, counting law, or natural Weil compression.

  A4\_FORMAL\_HINT   The natural lift is a proper non-Schatten isometry; same-clock unitarization changes phase space.
  --------------------------------------------------------------------------------------------------------------------------------------------------

Thus the tuple is $(\texttt{A0\_FAIL},\texttt{A1\_WEAK},\texttt{A2\_FAIL},
\texttt{A3\_FAIL},\texttt{A4\_FORMAL\_HINT})$. A0 failure forces `ROUTE_A_REJECTED`; later-layer exactness cannot override the arithmetic entry gate.

# Limitations and reproducibility

For $(a,b)=(3,1)$ the 2-adic word $100$ gives $1/5\mapsto4/5\mapsto2/5\mapsto1/5$. This legal $\mathbb Z_2$ cycle is not a positive-integer orbit, so the paper gives no progress on the positive-integer $3x+1$ conjecture. If exactly one of $a,b$ is even, the odd-branch numerator is odd and division by two leaves $\mathbb Z_2$; the theorem does not cross that boundary.

The release uses exact arithmetic only. A producer, independent checker, SymPy derivation, byte replay, semantic mutation suite, and content-addressed manifest are included. Finite ledgers are regression sentinels, not proofs. No prime table, target zero or divisor, arithmetic local factor, Euler factor, root number, automorphy, Hilbert--Pólya operator, Route-B authorization, external review, or acceptance rate is claimed. The scope literal is `NO_BAD_EULER_OR_ROOT_NUMBER`.

The final internal integrity pass separately cleared implementation bugs, citation identity and context, invented results, shortcut reliance, bug-as-insight reframing, methodology drift, and early-frame lock. This is an artifact-bounded audit, not a certificate of universal novelty or journal readiness. AI assistance was used for drafting and code generation; all claim-bearing formulas were reconstructed by independent exact code paths.

chinese-simplified 中文边界说明。 本文的精确结论限定于全体奇参数的 $\mathbb Z_2$ 动力学。经典 [parity]{lang="en"} 共轭属于先验工作；有限回归表不替代理论证明；$(3,1)$ 特例不推出正整数 [Collatz]{lang="en"} 结论。由于 [A0]{lang="en"} 缺少素数及素数幂来源，整体 [Route A]{lang="en"} 必须拒绝。

9 D. J. Bernstein and J. C. Lagarias, "The 3x+1 Conjugacy Map," *Canadian Journal of Mathematics* 48 (1996), 1154--1169. [doi:10.4153/CJM-1996-060-x](https://doi.org/10.4153/CJM-1996-060-x).

J. Leventides and C. Poulios, "Koopman operators and the $3x+1$-dynamical system," arXiv:2010.12987 (2020). [arxiv.org/abs/2010.12987](https://arxiv.org/abs/2010.12987).
