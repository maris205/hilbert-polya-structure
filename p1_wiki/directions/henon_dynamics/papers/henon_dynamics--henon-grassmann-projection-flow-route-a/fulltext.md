---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-grassmann-projection-flow-route-a"
canonical_tex: "henon_dynamics/henon_grassmann_projection_flow_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_grassmann_projection_flow_route_a/paper/main.pdf"
source_sha256: "0f3b34f8d4e55c9818823c56964c4fccdae4aa9f83c2dcbc936a6d531693b329"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# An Exact Schubert and Morse--Bott Atlas for the Grassmann Projection Flow

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_grassmann_projection_flow_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_grassmann_projection_flow_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_grassmann_projection_flow_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_grassmann_projection_flow_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For a real symmetric matrix $A$, we solve the Grassmann projection equation $\dot P=[P,[P,A]]$ globally by $\operatorname{Ran}P(t)=e^{tA}\operatorname{Ran}P(0)$. =0 Exterior powers give exact Plücker scaling and the basic invariant-subspace limit. \>0 Without assuming distinct subset sums, we identify every simple-spectrum Schubert-cell limit and its actual-support exponential rate, all linear modes, and the complete repeated-spectrum product-Grassmann Morse--Bott atlas with associated-graded limits. \>1 A strict Lyapunov law excludes nonconstant recurrence, and an exact evidence certificate separates these source results from all target arithmetic and Hilbert--Pólya claims.
author:
- 'Route-A source-local certificate HCS-C298'
date: 2 September 2026
title: |
  An Exact Schubert and Morse--Bott Atlas\
  for the Grassmann Projection Flow
```

## Markdown 正文

trailerid \[\<C2982026090200000000000000000000\>\<C2982026090200000000000000000000\>\]

# Projection dynamics and the exact quotient

Let $A=A^T\in\mathbb R^{n\times n}$ and $1\le k\le n-1$. We realize $\operatorname{Gr}(k,n)$ as the rank-$k$ orthogonal projections $$\mathcal P_{k,n}=\{P:P^T=P,\ P^2=P,\ \operatorname{tr}P=k\}$$ and consider $$\label{eq:flow}
 \dot P=[P,[P,A]]=AP+PA-2PAP.$$ The sign in [\[eq:flow\]](#eq:flow){reference-type="eqref" reference="eq:flow"} selects the high-eigenvalue subspaces forward in time. The generator $A$ is fixed; the state is the subspace represented by $P$.

[\[thm:global\]]{#thm:global label="thm:global"} Let $Q_0\in\mathbb R^{n\times k}$ have full column rank and $\operatorname{Ran}Q_0=\operatorname{Ran}P_0$. For every $t\in\mathbb R$, set $$\label{eq:projector}
 Y(t)=e^{tA}Q_0,\qquad
 P(t)=Y(t)\bigl(Y(t)^TY(t)\bigr)^{-1}Y(t)^T.$$ Then [\[eq:projector\]](#eq:projector){reference-type="eqref" reference="eq:projector"} is the unique global solution of [\[eq:flow\]](#eq:flow){reference-type="eqref" reference="eq:flow"}; in particular, $$\operatorname{Ran}P(t)=e^{tA}\operatorname{Ran}P_0.$$ If $Ae_i=\lambda_i e_i$ in an orthonormal eigenbasis, its projective Plücker coordinates obey $$\label{eq:plucker}
 p_I(t)=e^{t\lambda_I}p_I(0)\quad\hbox{up to one common scale},
 \qquad \lambda_I=\sum_{i\in I}\lambda_i.$$

The matrix $e^{tA}$ is invertible, so $Y(t)$ has full column rank and its Gram matrix is positive definite for all real $t$. Formula [\[eq:projector\]](#eq:projector){reference-type="eqref" reference="eq:projector"} is therefore the orthogonal projector onto $e^{tA}\operatorname{Ran}P_0$. Since $Y'=AY$ and $A=A^T$, differentiation of the Gram inverse gives $$\dot P=AP+PA-2PAP=[P,[P,A]].$$ Smooth finite-dimensional ODE uniqueness identifies it with the solution. On $\bigwedge^k\mathbb R^n$, the induced map sends $e_{i_1}\wedge\cdots\wedge e_{i_k}$ to $e^{t(\lambda_{i_1}+\cdots+\lambda_{i_k})}$ times itself, proving [\[eq:plucker\]](#eq:plucker){reference-type="eqref" reference="eq:plucker"}.

This quotient identity is the subspace power-flow mechanism neighboring Oja's principal-component dynamics and the continuous Grassmann flows of Absil, Sepulchre, and Mahony. We derive every statement needed below and make no priority claim for that classical mechanism.

# Simple spectrum: every Schubert cell and its rate

Assume in this section $$\label{eq:simple}
 \lambda_1<\lambda_2<\cdots<\lambda_n,
 \qquad F_j=\operatorname{span}(e_1,\ldots,e_j).$$ For a $k$-plane $V$, write $$\mathcal B(V)=\{I\subset\{1,\ldots,n\}:|I|=k,\ p_I(V)\ne0\}.$$ These are the bases of the representable matroid determined by the rows of any frame for $V$.

[\[lem:greedy\]]{#lem:greedy label="lem:greedy"} Distinct element weights $\lambda_1,\ldots,\lambda_n$ give a unique maximum-weight basis $I_+(V)$ and a unique minimum-weight basis $I_-(V)$ in $\mathcal B(V)$, even when two arbitrary $k$-subset sums coincide.

Run the matroid greedy algorithm in decreasing element weight. To see uniqueness directly, suppose two optimal bases differ and take the largest-weight element in their symmetric difference. Strong basis exchange inserts that element into the basis missing it while removing a strictly lower-weight element, producing a heavier basis. This contradiction proves the maximum statement; reverse the weights for the minimum.

For $I=(i_1<\cdots<i_k)$, let $\Omega_I$ be the Schubert cell characterized by $$\label{eq:schubert}
 \dim(V\cap F_j)=\#\{a:i_a\le j\}\quad(1\le j\le n).$$ Equivalently, $I$ is the lexicographically greatest nonzero Plücker index, hence the greedy maximum in Lemma [\[lem:greedy\]](#lem:greedy){reference-type="ref" reference="lem:greedy"}.

[\[thm:cells\]]{#thm:cells label="thm:cells"} If $V_0\in\Omega_I$, then $$\lim_{t\to+\infty}P(t)=P_I,$$ the coordinate projection onto $E_I=\operatorname{span}\{e_i:i\in I\}$. The opposite Schubert cell indexed by $I_-(V_0)$ gives the backward limit.

If $V_0\ne E_I$, define $$\label{eq:gap}
 \rho_2(V_0)=\max_{J\in\mathcal B(V_0),\,J\ne I}\lambda_J,
 \qquad \Delta_+(V_0)=\lambda_I-\rho_2(V_0)>0.$$ Then $$\label{eq:rate}
 \lim_{t\to+\infty}-\frac1t
 \log\lVert P(t)-P_I\rVert_F=\Delta_+(V_0).$$ The analogous backward rate uses the actual second-smallest nonzero Plücker weight. For an equilibrium the error is zero and its gap is declared infinite.

By Lemma [\[lem:greedy\]](#lem:greedy){reference-type="ref" reference="lem:greedy"}, $I$ is the unique maximum supported weight despite possible ambient subset-sum ties. Factor $e^{t\lambda_I}$ from the Plücker vector in [\[eq:plucker\]](#eq:plucker){reference-type="eqref" reference="eq:plucker"}. Every other supported coordinate decays, giving the coordinate-plane limit. The nonzero sum of all weight-$\rho_2$ coordinate vectors is the first surviving transverse term, so projective distance is $\Theta(e^{-t\Delta_+})$. The Plücker embedding and the orthogonal-projector chart are smooth local embeddings with equivalent norms; the logarithmic rate is therefore [\[eq:rate\]](#eq:rate){reference-type="eqref" reference="eq:rate"}. Apply the argument to $-A$ for backward time.

\>0

#### Why the support qualifier matters.

Simple eigenvalues do not imply distinct $k$-fold sums; for example $0+4=1+3$. Zero Plücker coordinates remove subsets from the orbit, and ties may remain at subleading weights. Lemma [\[lem:greedy\]](#lem:greedy){reference-type="ref" reference="lem:greedy"} proves only the needed top supported uniqueness, while [\[eq:gap\]](#eq:gap){reference-type="eqref" reference="eq:gap"} measures the first term that is actually present.

# Equilibria, modes, and Schubert dimensions

Relative to $\operatorname{Ran}P\oplus\ker P$, write the off-diagonal block of $A$ as $B$. Then $[P,[P,A]]$ has off-diagonal blocks $B$ and $B^T$. Thus $$\label{eq:equilibria}
 \dot P=0\quad\Longleftrightarrow\quad[P,A]=0
 \quad\Longleftrightarrow\quad\operatorname{Ran}P\text{ is }A\text{-invariant}.$$ For simple spectrum these are exactly the $\binom nk$ coordinate projections.

At $P_I$, a tangent graph component from selected $e_i$ to unselected $e_j$ has linearized equation $$\label{eq:mode}
 \dot x_{ji}=(\lambda_j-\lambda_i)x_{ji}.$$ Consequently $$\begin{aligned}
 d_s(I)&=\#\{(i,j):i\in I,j\notin I,\lambda_j<\lambda_i\},\\
 d_u(I)&=\#\{(i,j):i\in I,j\notin I,\lambda_j>\lambda_i\}.\end{aligned}$$ If $I=(i_1<\cdots<i_k)$, then $d_s(I)=\sum_{a=1}^k(i_a-a)=\dim\Omega_I$ and $d_s(I)+d_u(I)=k(n-k)$.

# Repeated spectrum: associated grade and Morse--Bott strata

Let the distinct eigenvalues be $\mu_1<\cdots<\mu_s$, with eigenspaces $E_\alpha$ of dimensions $m_\alpha$, and put $F_\alpha=\bigoplus_{\beta\le\alpha}E_\beta$. For an initial plane $V$, define $$\label{eq:graded}
 G_\alpha=\pi_\alpha(V\cap F_\alpha)\subset E_\alpha,
 \qquad
 k_\alpha=\dim(V\cap F_\alpha)-\dim(V\cap F_{\alpha-1}),$$ where $\pi_\alpha$ is orthogonal projection to $E_\alpha$.

Every initial plane has the basis-independent limit $$\label{eq:gradedlimit}
 \lim_{t\to+\infty}e^{tA}V=\bigoplus_{\alpha=1}^sG_\alpha.$$ For every feasible occupancy vector $0\le k_\alpha\le m_\alpha$, $\sum_\alpha k_\alpha=k$, the corresponding equilibrium component is exactly $$\label{eq:critical}
 \mathcal C_{\boldsymbol k}=\prod_{\alpha=1}^s\operatorname{Gr}(k_\alpha,E_\alpha).$$ It is Morse--Bott. Its critical, stable-normal, and unstable-normal dimensions are, respectively, $$\begin{aligned}
 d_0&=\sum_\alpha k_\alpha(m_\alpha-k_\alpha),\label{eq:dims}\\
 d_s&=\sum_{\beta<\alpha}k_\alpha(m_\beta-k_\beta),\\
 d_u&=\sum_{\beta>\alpha}k_\alpha(m_\beta-k_\beta),\end{aligned}$$ and $d_0+d_s+d_u=k(n-k)$.

Choose a basis of $V$ adapted to the filtration $V\cap F_\alpha$. When a basis vector first appears at level $\alpha$, its $E_\alpha$ component is nonzero; these leading components are independent and span $G_\alpha$. Under $e^{tA}$ every lower component decays relative to that leading one, which proves [\[eq:gradedlimit\]](#eq:gradedlimit){reference-type="eqref" reference="eq:gradedlimit"}. Equivalently, the entire highest-weight component of the decomposable Plücker vector survives. We do not choose one coordinate from a tied block. The descending eigenflag gives the backward limit.

Equation [\[eq:equilibria\]](#eq:equilibria){reference-type="eqref" reference="eq:equilibria"} and self-adjoint spectral decomposition show that every invariant plane splits as $\bigoplus V_\alpha$ with $V_\alpha\in\operatorname{Gr}(k_\alpha,E_\alpha)$, proving completeness of [\[eq:critical\]](#eq:critical){reference-type="eqref" reference="eq:critical"}. Within-block graph modes have rate zero and are precisely tangent to this product. Every cross-block mode has the nonzero rate $\mu_\beta-\mu_\alpha$; counting its sign gives [\[eq:dims\]](#eq:dims){reference-type="eqref" reference="eq:dims"}. Thus the Hessian is nondegenerate normal to the critical product, which is the Morse--Bott condition. The dimension closure counts every selected-to- unselected graph coordinate exactly once.

# Strict Lyapunov law and recurrence

Define $\Phi(P)=\operatorname{tr}(AP)$. Cyclicity of trace and $P^2=P$ give $$\label{eq:lyapunov}
 \frac{\mathrm d}{\mathrm dt}\Phi(P(t))
 =\operatorname{tr}\bigl(A[P,[P,A]]\bigr)
 =\lVert[P,A]\rVert_F^2\ge0.$$ Equality holds exactly at the invariant projections. If a nonconstant orbit returned arbitrarily close to its initial point, continuity of $\Phi$ would force its values back toward $\Phi(P_0)$ after strict increase, contradicting monotonicity. Hence no nonconstant recurrent or periodic trajectory exists. The explicit limits above are stronger than this obstruction.

\>1

# Exact evidence and boundary audit

The evidence archive contains eight simple-spectrum frames, including tied ambient subset sums and a proper Schubert cell; six repeated-spectrum frames, five with multi-coordinate top-weight components; and four complete Morse--Bott occupancy atlases. It records 80 simple and 37 repeated nonzero Plücker cells, 50 linear modes, and 22 critical components. Each initial projector and Lyapunov derivative is rational.

An independent checker imports no producer code and recomputes maximal minors, basis exchange, flags, projectors, gaps, modes, and dimensions. A separate SymPy lane differentiates the exact solution and checks exterior powers and Lyapunov identities. Byte replay, repaired-hash hostile mutations, strict JSON/YAML parsing, and six fresh fixed-epoch builds close the digital audit. Finite cases remain regression evidence only.

#### Collision with C185.

The classical double-bracket framework of Brockett neighbors both packages, but their systems differ. C185 moves a full symmetric matrix on a fixed isospectral orbit toward a separate ordered target. Here $A$ is fixed and the state is a rank-$k$ projection; the exact motion is the induced linear action [\[eq:projector\]](#eq:projector){reference-type="eqref" reference="eq:projector"}. Product-Grassmann equilibrium manifolds and associated-graded subspace limits are specific to the present state space.

# Route-A verdict, reproducibility, and nonclaims

The frozen tuple is $$\begin{gathered}
 (\mathrm{A0\_FAIL},\mathrm{A1\_FAIL},\mathrm{A2\_FAIL},
 \mathrm{A3\_FAIL},\\
 \mathrm{A4\_FORMAL\_HINT}).
 \end{gathered}$$ There is no arithmetic local datum (A0), nonconstant primitive-orbit bridge (A1), arithmetic clock (A2), or target completion (A3). A fixed symmetric generator is only a formal spectral hint (A4): the flow is dissipative, and $A$ is not a Hilbert--Pólya operator. The overall verdict is `ROUTE_A_REJECTED`; Route B is locked under `NO_BAD_EULER_OR_ROOT_NUMBER`.

No target Euler factor, root number, automorphy, target divisor law, target functional equation, zero correspondence, or target spectral realization is claimed. Nor is literary priority claimed for Oja, Brockett, Grassmann, Schubert, Plücker, or Morse--Bott mechanisms.

#### Reproducibility statement.

The producer, duplicate-rejecting checker, symbolic lane, replay, mutation suite, three-round deterministic paper build, and self-excluding manifest are all archived. Exact source, scope, evaluator, and epoch identifiers occur in both machine-readable contracts.

#### AI-use statement.

A generative language model assisted with drafting and verification-code scaffolding. The theorem, proofs, exact outputs, source boundaries, and release artifacts were checked under independent scripted lanes; final responsibility remains with the authors.

# Source lineage {#source-lineage .unnumbered}

Oja owns the principal-component learning-flow neighborhood; Brockett owns the double-bracket sorting framework; Absil, Sepulchre, and Mahony directly treat continuous-time subspace flows related to the symmetric eigenproblem. The entries below are ownership citations, not claims of literature priority for this package.

9 E. Oja, "Simplified neuron model as a principal component analyzer," *Journal of Mathematical Biology* 15 (1982), 267--273. DOI: [10.1007/BF00275687](https://doi.org/10.1007/BF00275687).

R. W. Brockett, "Dynamical systems that sort lists, diagonalize matrices, and solve linear programming problems," *Linear Algebra and its Applications* 146 (1991), 79--91. DOI: [10.1016/0024-3795(91)90021-N](https://doi.org/10.1016/0024-3795(91)90021-N).

P.-A. Absil, R. Sepulchre, and R. Mahony, "Continuous-time subspace flows related to the symmetric eigenproblem," *Pacific Journal of Optimization* 4 (2008), 179--194. Institutional record: [hdl:2078.5/90452](https://hdl.handle.net/2078.5/90452).
