---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-complete-graph-randomized-gossip-covariance-route-a"
canonical_tex: "henon_dynamics/henon_complete_graph_randomized_gossip_covariance_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_complete_graph_randomized_gossip_covariance_route_a/paper/main.pdf"
source_sha256: "dfcea325b6b19602b25e39dc838079844219d7a487dad7cd2a658ff0f0891c12"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Relaxed Randomized Gossip on the Complete Graph: Exact Covariance Spectrum and Sharp Consensus Law

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_complete_graph_randomized_gossip_covariance_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_complete_graph_randomized_gossip_covariance_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_complete_graph_randomized_gossip_covariance_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_complete_graph_randomized_gossip_covariance_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For uniform pairwise relaxed averaging on the complete graph, we derive the exact first moment and sharp mean-square disagreement law at every finite time. \>0 The entire second-moment transfer on $\operatorname{Sym}^2(\mathbf 1^\perp)$ splits into three explicit orthogonal blocks; all eigenvalues, multiplicities, projectors, and matrix-valued iterates are closed. \>1 This yields the exact statistical covariance, a finite-time tail bound, almost-sure consensus for $0<\eta<1$, and a complete treatment of $N=1,2,3$ and $\eta=0,1$. In particular, $\eta=1$ is a random-transposition boundary and not a consensus regime.
author:
- 'Route-A source-local certificate HCS-C333'
date: 3 September 2026
title: |
  Relaxed Randomized Gossip on the Complete Graph:\
  Exact Covariance Spectrum and Sharp Consensus Law
```

## Markdown 正文

trailerid \[\<C3332026090300000000000000000000\>\<C3332026090300000000000000000000\>\]

# Frozen stochastic owner

Fix $N\geq2$ and $0\leq\eta\leq1$. Independently at every integer time, choose an unordered pair $\{i,j\}$ uniformly from the edges of $K_N$ and set $$\label{eq:update}
 x_{t+1}=W_{ij}x_t,
 \qquad W_{ij}=I-\eta d_{ij}d_{ij}^{\mathsf T},
 \qquad d_{ij}=e_i-e_j.$$ Thus the selected entries become $(1-\eta)x_i+\eta x_j$ and $\eta x_i+(1-\eta)x_j$. The endpoint $\eta=1/2$ is ordinary pairwise averaging, while $\eta=1$ merely swaps the two entries. The initial vector is deterministic.

Put $$P=I-\frac1N\mathbf 1\mathbf 1^{\mathsf T},\qquad
 \bar x=\frac1N\mathbf 1^{\mathsf T}x_0,\qquad y_t=Px_t=x_t-\bar x\mathbf 1.$$ Every $W_{ij}$ is symmetric, fixes $\mathbf 1$, and commutes with $P$. The basic complete-graph identity is $$\label{eq:laplacian}
 \sum_{i<j}d_{ij}d_{ij}^{\mathsf T}=NP.$$

[\[thm:energy\]]{#thm:energy label="thm:energy"} The sample mean is invariant on every realization. With $$\label{eq:mu-rho}
 \mu=1-\frac{2\eta}{N-1},\qquad
 \rho=1-\frac{4\eta(1-\eta)}{N-1},$$ one has, for every $t\geq0$, $$\label{eq:first-energy}
 \mathbb Ey_t=\mu^t y_0,
 \qquad
 \mathbb E\|y_t\|^2=\rho^t\|y_0\|^2.$$

Equation [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"} fixes $\mathbf 1^{\mathsf T}x$ pathwise. Since $K_N$ has $N(N-1)/2$ edges, averaging [\[eq:update\]](#eq:update){reference-type="eqref" reference="eq:update"} and using [\[eq:laplacian\]](#eq:laplacian){reference-type="eqref" reference="eq:laplacian"} gives $$\mathbb EW=I-\frac{2\eta}{N-1}P,$$ which acts by $\mu$ on $\mathbf 1^\perp$. Independence of the new edge from the past proves the first identity by iteration. Since $(d_{ij}d_{ij}^{\mathsf T})^2=2d_{ij}d_{ij}^{\mathsf T}$, $$W_{ij}^2=I-2\eta(1-\eta)d_{ij}d_{ij}^{\mathsf T}.$$ Conditioning on $y_t$, applying [\[eq:laplacian\]](#eq:laplacian){reference-type="eqref" reference="eq:laplacian"}, and iterating gives the second identity. It is an equality for every initial vector, hence its rate is sharp whenever $y_0\ne0$.

The phrase *sharp energy owner* records the content added in the original paper round: no spectral conclusion is needed for Theorem [\[thm:energy\]](#thm:energy){reference-type="ref" reference="thm:energy"}.

\>0

# Three invariant covariance blocks

Let $$\mathscr H_N=\{A\in\mathbb R^{N\times N}:A=A^{\mathsf T},\ PAP=A\}$$ with Frobenius inner product. For $N\geq3$ define $$\begin{aligned}
 \mathscr V_0&=\operatorname{span}\{P\},\\
 \mathscr V_1&=\{P\operatorname{diag}(u)P:\mathbf 1^{\mathsf T}u=0\},\\
 \mathscr V_2&=\{A\in\mathscr H_N:\operatorname{diag}A=0\}.\end{aligned}$$ For $N=3$, $\mathscr V_2=\{0\}$. For $N=2$, only $\mathscr V_0=\mathscr H_2$ remains.

[\[lem:projectors\]]{#lem:projectors label="lem:projectors"} For $N\geq3$ and $A\in\mathscr H_N$, set $$\begin{aligned}
\label{eq:projectors}
 \Pi_0A&=\frac{\operatorname{tr}A}{N-1}P,\qquad R=A-\Pi_0A,\nonumber\\
 u&=\frac{N}{N-2}\operatorname{diag}R,\qquad
 \Pi_1A=P\operatorname{diag}(u)P,\qquad
 \Pi_2A=A-\Pi_0A-\Pi_1A.\end{aligned}$$ Then $\Pi_r$ are the orthogonal projectors onto $\mathscr V_r$, and $$\label{eq:dimensions}
 \dim\mathscr V_0=1,\qquad \dim\mathscr V_1=N-1,\qquad
 \dim\mathscr V_2=\frac{N(N-3)}2.$$

The first residual has trace zero, so $\mathbf 1^{\mathsf T}u=0$. For such $u$, $$\operatorname{diag}(P\operatorname{diag}(u)P)
 =\frac{N-2}{N}u.$$ Hence $\Pi_1A$ has the same diagonal as $R$, and $\Pi_2A$ has zero diagonal. Centered matrices with zero diagonal are Frobenius orthogonal to both $P$ and every centered diagonal pattern. This proves orthogonality and the projector formulas. The map $u\mapsto P\operatorname{diag}(u)P$ is injective on $\mathbf 1^\perp$ for $N>2$. Subtracting dimensions from $\dim\mathscr H_N=N(N-1)/2$ proves [\[eq:dimensions\]](#eq:dimensions){reference-type="eqref" reference="eq:dimensions"}.

Define the second-moment transfer $$\label{eq:transfer}
 \mathcal T_\eta(A)=\frac{2}{N(N-1)}\sum_{i<j}W_{ij}AW_{ij}.$$

[\[thm:spectrum\]]{#thm:spectrum label="thm:spectrum"} The three spaces in Lemma [\[lem:projectors\]](#lem:projectors){reference-type="ref" reference="lem:projectors"} are orthogonal invariant blocks of $\mathcal T_\eta$ for every $0\leq\eta\leq1$. The restrictions to the present nonzero blocks are scalar, with respective values $$\begin{aligned}
 \lambda_0&=1-\frac{4\eta(1-\eta)}{N-1},\label{eq:lambda0}\\
 \lambda_1&=1-\frac{4\eta-2\eta^2}{N-1},\label{eq:lambda1}\\
 \lambda_2&=1-\frac{4\eta}{N-1}
              +\frac{4\eta^2}{N(N-1)}.\label{eq:lambda2}\end{aligned}$$ Absent low-dimensional blocks are omitted. If $\eta>0$, the values attached to the present blocks are pairwise distinct, so those blocks are precisely the corresponding full eigenspaces. If $\eta=0$, then $\mathcal T_0=I$: the only eigenvalue is one, its eigenspace is all of $\mathscr H_N$, and its multiplicity is $N(N-1)/2$.

For centered $A$, expansion of [\[eq:transfer\]](#eq:transfer){reference-type="eqref" reference="eq:transfer"} gives $$\label{eq:Texpand}
 \mathcal T_\eta(A)=(1-\frac{4\eta}{N-1})A
 +\frac{2\eta^2}{N(N-1)}\mathcal S(A),
 \quad
 \mathcal S(A)=\sum_{i<j}(d_{ij}^{\mathsf T}Ad_{ij})d_{ij}d_{ij}^{\mathsf T}.$$ If $A=P$, every scalar coefficient in $\mathcal S$ is two, so $\mathcal S(P)=2NP$. If $A=P\operatorname{diag}(u)P$ with $\mathbf 1^{\mathsf T}u=0$, then $d_{ij}^{\mathsf T}Ad_{ij}=u_i+u_j$. The off-diagonal and diagonal entries give $\mathcal S(A)=NA$. Finally, for $A\in\mathscr V_2$, $d_{ij}^{\mathsf T}Ad_{ij}=-2a_{ij}$; its zero row sums then give $\mathcal S(A)=2A$. Substitution in [\[eq:Texpand\]](#eq:Texpand){reference-type="eqref" reference="eq:Texpand"} yields the three displayed eigenvalues. For $\eta>0$, $$\lambda_0-\lambda_1=\frac{2\eta^2}{N-1}>0,
 \qquad
 \lambda_1-\lambda_2=\frac{2\eta^2(N-2)}{N(N-1)}>0,$$ where the second comparison is used only when $\mathscr V_2$ is present. Together with the orthogonal decomposition, this proves the full-eigenspace statement. At $\eta=0$ every $W_{ij}=I$, which proves the asserted merger.

[\[thm:second\]]{#thm:second label="thm:second"} Let $A_0=y_0y_0^{\mathsf T}$ and $M_t=\mathbb E[y_ty_t^{\mathsf T}]$. For $N\geq3$, $$\label{eq:Mt}
 M_t=\lambda_0^t\Pi_0A_0+\lambda_1^t\Pi_1A_0
       +\lambda_2^t\Pi_2A_0,$$ where the last term is absent at $N=3$. At $N=2$, $M_t=\lambda_0^tA_0$.

The newly selected edge is independent of the past, hence $M_{t+1}=\mathcal T_\eta(M_t)$. Apply Theorem [\[thm:spectrum\]](#thm:spectrum){reference-type="ref" reference="thm:spectrum"} and iterate. Taking traces recovers Theorem [\[thm:energy\]](#thm:energy){reference-type="ref" reference="thm:energy"}, because the two trace-free blocks do not contribute.

\>1

# Covariance and probabilistic closure

The disagreement second moment $M_t$ is not, in general, the statistical covariance: $\mathbb Ey_t=\mu^ty_0$ need not vanish. The exact covariance is therefore $$\label{eq:covariance}
 \operatorname{Cov}(x_t)
 =M_t-\mu^{2t}y_0y_0^{\mathsf T}.$$ Both terms annihilate the consensus direction.

[\[thm:as\]]{#thm:as label="thm:as"} If $N\geq2$, $0<\eta<1$, $\varepsilon>0$, and $y_0\ne0$, then $$\label{eq:tail}
 \Pr\{\|y_t\|\geq\varepsilon\|y_0\|\}
 \leq\frac{\rho^t}{\varepsilon^2}.$$ For every initial vector, including $y_0=0$, one has $x_t\to\bar x\mathbf 1$ almost surely and in mean square.

Here $0\leq\rho<1$. Markov's inequality and Theorem [\[thm:energy\]](#thm:energy){reference-type="ref" reference="thm:energy"} give [\[eq:tail\]](#eq:tail){reference-type="eqref" reference="eq:tail"}; division by $\|y_0\|$ is legitimate under the stated hypothesis. If $y_0=0$, every update fixes the initial consensus vector. Otherwise, for each positive rational $\varepsilon$, the probabilities in [\[eq:tail\]](#eq:tail){reference-type="eqref" reference="eq:tail"} are summable in $t$. Borel--Cantelli, followed by a countable intersection, gives $\|y_t\|\to0$ almost surely. Mean-square convergence is already the exact energy identity.

# Complete boundary atlas

For $N=1$ there is no edge to sample; by definition the process is static. For $N=2$ the disagreement line is one-dimensional and its difference is multiplied by $1-2\eta$ at every step. Hence $\eta=1/2$ reaches consensus in one update. For $N=3$, the third block has dimension zero, so inserting a $\lambda_2$ multiplicity would be spurious.

At $\eta=0$, all $W_{ij}$ and $\mathcal T_0$ are the identity. The three invariant summands therefore merge into the eigenvalue-one eigenspace $\mathscr H_N$, of total multiplicity $N(N-1)/2$; they must not be called three distinct eigenspaces at this endpoint. At $\eta=1$, each $W_{ij}$ is the transposition of coordinates $i$ and $j$, and $\rho=1$; non-consensus data cannot converge to consensus because their disagreement norm is constant. This is the precise random-transposition boundary, not an extension of the interior convergence theorem. Constant initial vectors are fixed for every parameter. Values $\eta\notin[0,1]$, nonuniform edge laws, and noncomplete graphs lie outside the frozen owner.

# Evidence, collisions, and Route-A boundary

The exact certificate contains 56 spectral rows, six projector receipts, 48 exhaustive-word rows, and 2,966 scalar leaves. It enumerates all 4,242 edge words in its declared small-time grid. A producer-independent checker performs 1,392 checks, while the SymPy lane closes 350 exact identities. Two isolated producer runs are byte-identical, and 140 repaired-hash, parser, theorem, boundary, and evaluator attacks are rejected. The finite grid is regression evidence; the preceding theorems are analytic for every declared $N$ and $\eta$.

The closest registered systems are C183, which owns the permutation-valued random-transposition chain; C203, deterministic signed-Laplacian consensus; C312, state-dependent Hegselmann--Krause averaging; and C322, Kac's continuous-angle collision operator. None owns the interior relaxed random product and its full second-moment decomposition.

The phrase *probability boundary and route firewall* records the final revision. Under `NO_BAD_EULER_OR_ROOT_NUMBER`, the Route-A tuple is $$(\mathrm{A0\_FAIL},\mathrm{A1\_FAIL},\mathrm{A2\_FAIL},
  \mathrm{A3\_FAIL},\mathrm{A4\_FORMAL\_HINT}).$$ Pair maps and the moment transfer are symmetric on natural source spaces, but this is only a formal lift hint. Random pair words are not deterministic isolated prime-labelled cycles, and interaction count is not a logarithmic prime clock. There is no orbit zeta, target Fredholm determinant, functional equation, Weil compression, target divisor, target-zero match, or natural same-clock unitary quantization. Route A is rejected and Route B remains locked. No target arithmetic local data, Euler factors, root number, automorphy, or Hilbert--Polya operator is claimed.

#### AI use.

A generative language model assisted proof organization, code scaffolding, and manuscript drafting. The displayed derivations, independent exact checker, symbolic lane, hostile tests, and deterministic artifacts define the audit record.

9 S. Boyd, A. Ghosh, B. Prabhakar, and D. Shah, "Randomized gossip algorithms," *IEEE Transactions on Information Theory* 52 (2006), 2508--2530. DOI: [10.1109/TIT.2006.874516](https://doi.org/10.1109/TIT.2006.874516).

The source establishes the randomized-gossip owner and network setting. The complete-graph formulas above are derived directly for the frozen model; no literature-priority claim is made for them.
