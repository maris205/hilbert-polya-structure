---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-parallel-binary-partition-fragmentation-route-a"
canonical_tex: "henon_dynamics/henon_parallel_binary_partition_fragmentation_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_parallel_binary_partition_fragmentation_route_a/paper/main.pdf"
source_sha256: "6b782832e2e47dbeb9582efbd5a6ecc302773a486000443306fbc6c771dc1930"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Parallel Binary Refinement of Labelled Set Partitions: Exact Kernels, Spectrum, and the Last-Collision Threshold

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_parallel_binary_partition_fragmentation_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_parallel_binary_partition_fragmentation_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_parallel_binary_partition_fragmentation_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_parallel_binary_partition_fragmentation_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We solve a synchronous fragmentation chain on the labelled set partitions of $[n]$. At every step each label receives a fresh fair bit and each current block is refined by its two nonempty bit fibres. A coupling by binary words gives the full $t$-step kernel from every starting partition, the complete law of the number of blocks, and the exact absorption-time distribution. The transition matrix has eigenvalues $2^{k-n}$ with Stirling multiplicities $S(n,k)$. \>0 A refinement flag and a genuine lowering argument give a squarefree annihilating polynomial, closing the diagonalizability gap that triangularity alone would leave. The absorption window is the birthday window: $n^2/2^t\to\lambda$ gives the limit $e^{-\lambda/2}$, with its dyadic lattice boundary kept explicit. \>1 An exact, independently checked finite certificate accompanies the analytic proof. A hostile Route-A audit returns $(\mathrm{A0},\ldots,\mathrm{A4})=(\mathrm{FAIL},\ldots,\mathrm{FAIL})$; the finite Markov determinant is not promoted to arithmetic data.
author:
- 'Route-A Dynamics Working Note C301'
date: 2 September 2026
title: 'Parallel Binary Refinement of Labelled Set Partitions: Exact Kernels, Spectrum, and the Last-Collision Threshold'
```

## Markdown 正文

# The labelled parallel-fragmentation chain

Let $n\geq1$ and let $\mathfrak P_n$ be the set of labelled set partitions of $[n]=\{1,\ldots,n\}$. Write $\pi\preceq\sigma$ when $\sigma$ refines $\pi$. Starting from $\Pi_0=\pi$, every label independently receives a fresh bit in $\{0,1\}$. In each block of $\pi$, labels with equal bits stay together; empty fibres are deleted. The resulting partition is $\Pi_1$. Updates use fresh independent bits.

This is a synchronous chain: all blocks are marked in parallel. Labels are part of the state. In particular, quotienting by block sizes produces a different chain and different spectral multiplicities. Put $$(q)_{r}=q(q-1)\cdots(q-r+1),\qquad (q)_{0}=1,$$ and let $S(n,k)$ denote a Stirling number of the second kind. For $\pi\preceq\sigma$, let $r_B(\pi,\sigma)$ be the number of $\sigma$-blocks contained in $B\in\pi$.

# Complete law

[\[thm:main\]]{#thm:main label="thm:main"} For every $n\geq1$, $t\geq0$, and $\pi,\sigma\in\mathfrak P_n$, with $q=2^t$, $$\label{eq:t-kernel}
 K_n^t(\pi,\sigma)=
 \mathbf 1_{\{\pi\preceq\sigma\}}
 \prod_{B\in\pi}\frac{(q)_{r_B(\pi,\sigma)}}{q^{|B|}}.$$ Consequently, the one-step probability equals $2^{|\pi|-n}$ precisely when $\sigma$ refines $\pi$ and each $\pi$-block contains at most two $\sigma$-blocks, and equals zero otherwise.

From the one-block initial partition, for every $\sigma\in\mathfrak P_n$ and $1\leq k\leq n$, $$\begin{aligned}
 \Pr\{\Pi_t=\sigma\}&=\frac{(2^t)_{|\sigma|}}{2^{tn}},
 \label{eq:partition-law}\\
 \Pr\{|\Pi_t|=k\}&=S(n,k)\frac{(2^t)_{k}}{2^{tn}},
 \label{eq:block-law}\\
 \mathbb E|\Pi_t|&=2^t\bigl[1-(1-2^{-t})^n\bigr].
 \label{eq:mean-blocks}\end{aligned}$$ Let $T_n=\min\{t:\Pi_t\text{ is discrete}\}$. Then $$\begin{aligned}
 \Pr\{T_n\leq t\}&=\frac{(2^t)_{n}}{2^{tn}},
 \label{eq:cdf}\\
 \Pr\{T_n=t\}&=\frac{(2^t)_{n}}{2^{tn}}
 -\mathbf 1_{\{t\geq1\}}\frac{(2^{t-1})_{n}}{2^{(t-1)n}},
 \label{eq:mass}\\
 \mathbb ET_n&=\sum_{t\geq0}
 \left[1-\frac{(2^t)_{n}}{2^{tn}}\right].
 \label{eq:mean-time}\end{aligned}$$ The series converges. The characteristic polynomial, source spectral determinant, and power traces are $$\begin{aligned}
 \chi_{K_n}(x)&=\prod_{k=1}^n
    (x-2^{k-n})^{S(n,k)},\label{eq:charpoly}\\
 \det(I-zK_n)&=\prod_{k=1}^n
    (1-z2^{k-n})^{S(n,k)},\label{eq:det}\\
 \operatorname{tr}(K_n^t)&=\sum_{k=1}^nS(n,k)2^{t(k-n)}.
 \label{eq:trace}\end{aligned}$$ Moreover, $$\label{eq:annihilator}
 \prod_{k=1}^n(K_n-2^{k-n}I)=0,$$ so $K_n$ is diagonalizable over $\mathbb Q$.

Finally, if $n_j\to\infty$, $t_j$ are integers, and $n_j^2/2^{t_j}\to\lambda\in(0,\infty)$, then $$\label{eq:critical}
 \Pr\{T_{n_j}\leq t_j\}\longrightarrow e^{-\lambda/2}.$$ Thus $T_n$ has a tight $O(1)$ window around $2\log_2n$.

# Binary-word proof

After $t$ updates, attach to label $i$ the word formed by its successive bits. These words are independent and uniform in a set of size $q=2^t$. Inside each starting block $B$, two labels are together at time $t$ exactly when their words agree. To realize $r_B$ prescribed terminal fibres one must injectively assign words to those fibres. There are $(q)_{r_B}$ assignments. Starting blocks use disjoint label sets, hence their counts multiply, proving [\[eq:t-kernel\]](#eq:t-kernel){reference-type="eqref" reference="eq:t-kernel"}. Taking $t=1$ gives the stated one-step kernel.

For a one-block start, a fixed $k$-block partition has probability $(q)_{k}/q^n$. There are $S(n,k)$ such labelled partitions, yielding [\[eq:partition-law\]](#eq:partition-law){reference-type="eqref" reference="eq:partition-law"} and [\[eq:block-law\]](#eq:block-law){reference-type="eqref" reference="eq:block-law"}; the identity $\sum_k S(n,k)(q)_{k}=q^n$ also verifies normalization. Alternatively, $|\Pi_t|$ is the number of occupied boxes after $n$ independent throws into $q$ boxes. Summing the $q$ occupancy indicators proves [\[eq:mean-blocks\]](#eq:mean-blocks){reference-type="eqref" reference="eq:mean-blocks"}.

Absorption means that all $n$ words are distinct, which proves [\[eq:cdf\]](#eq:cdf){reference-type="eqref" reference="eq:cdf"}; differencing successive distribution functions gives [\[eq:mass\]](#eq:mass){reference-type="eqref" reference="eq:mass"}. The tail-sum formula gives [\[eq:mean-time\]](#eq:mean-time){reference-type="eqref" reference="eq:mean-time"}. A union bound gives $$\Pr\{T_n>t\}\leq \binom n2 2^{-t},$$ so the tail series converges. For $n=1$, all formulas reduce to $T_1=0$. The contract begins at $n=1$; the empty-set convention $n=0$ is not used.

\>0

# The spectral flag and its missing step

Order states by their number of blocks. Refinement makes $K_n$ triangular. A $k$-block state stays unchanged exactly when every block receives a constant bit; the $2^k$ successful assignments among $2^n$ have probability $\lambda_k=2^{k-n}$. Hence the diagonal rank-$k$ block is $\lambda_k I_{S(n,k)}$, proving [\[eq:charpoly\]](#eq:charpoly){reference-type="eqref" reference="eq:charpoly"}; [\[eq:det\]](#eq:det){reference-type="eqref" reference="eq:det"} and [\[eq:trace\]](#eq:trace){reference-type="eqref" reference="eq:trace"} follow once diagonalizability is closed.

Triangularity alone is not that closure. Let $V_k$ be the span of basis vectors indexed by partitions of rank at most $k$, with the conventional column action of the displayed transition matrix. The spaces $0\subset V_1\subset\cdots\subset V_n$ are invariant, and $(K_n-\lambda_k I)V_k\subseteq V_{k-1}$. Since all polynomial factors in $K_n$ commute, applying the factors in descending rank lowers this flag one step at a time. Their product kills $V_n$, proving [\[eq:annihilator\]](#eq:annihilator){reference-type="eqref" reference="eq:annihilator"}. The roots $\lambda_1,\ldots,\lambda_n$ are distinct, so the minimal polynomial is squarefree and $K_n$ is diagonalizable over $\mathbb Q$. This also justifies the trace formula without any hidden Jordan-block assumption.

# Birthday threshold and lattice boundary

Write $q_j=2^{t_j}$. Under the hypotheses of [\[eq:critical\]](#eq:critical){reference-type="eqref" reference="eq:critical"}, $n_j/q_j\to0$ and $$\begin{aligned}
 \log\frac{(q_j)_{n_j}}{q_j^{n_j}}
 &=\sum_{r=0}^{n_j-1}\log(1-r/q_j)\\
 &=-\frac{n_j(n_j-1)}{2q_j}
   +O\!\left(\frac{n_j^3}{q_j^2}\right)
 \longrightarrow-\lambda/2.\end{aligned}$$ Exponentiation proves [\[eq:critical\]](#eq:critical){reference-type="eqref" reference="eq:critical"}. The same product, together with the union bound above, yields tightness around $2\log_2n$.

There is an essential lattice qualification. Because $t$ is integer and $q=2^t$, the quantity $n^2/2^{\lfloor2\log_2n+c\rfloor}$ need not converge without controlling its dyadic phase. We therefore assert the limit only along sequences for which that ratio converges; no phase-free continuous law for $T_n-2\log_2n$ is claimed.

\>1

# Exact certificate and hostile boundary audit

The machine-readable certificate is not used to replace the proof. It enumerates all $278$ labelled partitions for $1\leq n\leq6$, reconstructs all $1{,}860$ nonzero transition cells independently, and checks $81$ exact time-law rows for $1\leq n\leq9$ and $0\leq t\leq8$. A separate SymPy implementation verifies characteristic polynomials, determinants, squarefree annihilators, eigenspace dimensions, and $t$-step kernels through $n=5$. Deterministic replay and a mutation suite protect the serialization, formula, scope, and evaluation contracts. These finite checks are regression evidence only; Theorem [\[thm:main\]](#thm:main){reference-type="ref" reference="thm:main"} is global because of the preceding word coupling and flag proof.

The closest source owner is the Hopf-power/rock-breaking framework of Diaconis, Pang, and Ram [@DPR]. Their unlabelled integer-partition rock-breaking chain and labelled-graph examples make clear that binary breaking, absorption, and Hopf diagonalization are established mechanisms. This note claims neither priority nor a new general Hopf-algebra theorem. Its closed contribution is a self-contained labelled-set-partition formulation with the complete kernel, occupancy law, exact last-collision distribution, elementary spectral-flag proof, and executable audit in one contract.

The Route-A tuple is $$(A0,A1,A2,A3,A4)=(\mathrm{FAIL},\mathrm{FAIL},\mathrm{FAIL},
 \mathrm{FAIL},\mathrm{FAIL}),
 \qquad \texttt{ROUTE\_A\_REJECTED}.$$ There is no arithmetic local datum or Euler factor (A0). Refinement has no nonconstant directed cycle---only self-loops---and therefore no primitive orbit repetition law (A1). Ordinary integer time and the scale $2^t$ are not an arithmetic logarithmic clock (A2). Although [\[eq:det\]](#eq:det){reference-type="eqref" reference="eq:det"} is exact, it is a finite source Markov polynomial, not a target completed determinant or functional equation (A3). Finally, rational diagonalizability is not a self-adjoint target-zero lift (A4). Route B is locked under the literal `NO_BAD_EULER_OR_ROOT_NUMBER` scope.

Three model mutations are outside the theorem: assigning one shared bit per block prevents splitting; biased label bits replace the uniform injection count; and quotienting by block sizes changes the state space and Stirling multiplicities. These are different systems, not harmless reparametrizations.

#### AI-use statement.

An AI assistant helped draft prose and executable checks. The formulas were rederived independently, finite claims were regenerated from exact arithmetic, and the final logical and scope assertions remain the responsibility of the release author.

1 P. Diaconis, C. Y. A. Pang, and A. Ram, "Hopf algebras and Markov chains: two examples and a theory," *Journal of Algebraic Combinatorics* (2014), doi:10.1007/s10801-013-0456-7; arXiv:1206.3620.
