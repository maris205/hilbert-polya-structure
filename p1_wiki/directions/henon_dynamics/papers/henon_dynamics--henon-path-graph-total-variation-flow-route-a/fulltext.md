---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-path-graph-total-variation-flow-route-a"
canonical_tex: "henon_dynamics/henon_path_graph_total_variation_flow_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_path_graph_total_variation_flow_route_a/paper/main.pdf"
source_sha256: "3b4ed84a76dbe323c4c3ef859a5d3cd0f0383ed0b71621167bcd8b7ac918c33d"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact Coalescence and the ROF Semigroup Identity for Total-Variation Flow on a Finite Path

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_path_graph_total_variation_flow_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_path_graph_total_variation_flow_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_path_graph_total_variation_flow_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_path_graph_total_variation_flow_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We solve the Euclidean total-variation gradient flow on every finite unweighted path. =0 Maximal-monotone well-posedness, one-homogeneous dissipation, and a path Poincaré estimate give finite-time consensus at the initial mean. \>0 An explicit interpolation of edge flux across each constant block gives a piecewise-affine coalescence algorithm: blocks never split, simultaneous collisions merge jointly, and at most $n-1$ event times occur. \>1 The no-splitting invariant makes the time-averaged subgradient admissible at the final state, proving that the flow equals the Rudin--Osher--Fatemi minimizer for every time. Exact two-engine evidence audits the finite event implementation while a strict nonclaim separates this theorem from arithmetic determinants and Hilbert--Pólya.
author:
- 'Route-A source-local certificate HCS-C279'
date: 1 September 2026
title: |
  Exact Coalescence and the ROF Semigroup Identity\
  for Total-Variation Flow on a Finite Path
```

## Markdown 正文

trailerid \[\<C2792026090100000000000000000000\>\<C2792026090100000000000000000000\>\]

# Frozen path flow

Let $P_n$ be the path with vertices $1,\ldots,n$, where $n\geq1$. On $\mathbb{R}^n$ with its Euclidean inner product define $$\label{eq:J}
 (Dx)_i=x_{i+1}-x_i,\qquad
 J(x)=\lVert Dx\rVert_1=\sum_{i=1}^{n-1}|x_{i+1}-x_i|.$$ We study the maximal-monotone clock $$\label{eq:flow}
 x'(t)\in-\partial J(x(t)),\qquad x(0)=x^0.$$ This freezes unit edge weights and the ordinary vertex norm. It is neither an Euler time step nor a continuum limit. Maximal-monotone semigroups provide the general existence framework [@Brezis1973]; graph total-variation flow and its finite-time stabilization are treated in a broader setting by Mazón, Solera, and Toledo [@MST2020].

For $a\in\mathbb{R}$, let $\operatorname{Sgn}(a)=\{\operatorname{sign}a\}$ if $a\ne0$ and $\operatorname{Sgn}(0)=[-1,1]$. The chain rule for [\[eq:J\]](#eq:J){reference-type="eqref" reference="eq:J"} gives $$\label{eq:subgrad}
 \partial J(x)=\{D^{\mathsf T}z:z_i\in\operatorname{Sgn}((Dx)_i)\}.$$ Since $J$ is finite, continuous, and convex, $\partial J$ is maximal monotone; there is a unique global absolutely continuous solution of [\[eq:flow\]](#eq:flow){reference-type="eqref" reference="eq:flow"}.

Write $\bar x=n^{-1}\sum_i x_i^0$ and $\rho(t)=\lVert x(t)-\bar x\mathbf1\rVert_2$. Every $D^{\mathsf T}z$ is orthogonal to $\mathbf1$, so the mean is preserved. One-homogeneity implies $\langle g,x\rangle=J(x)$ for $g\in\partial J(x)$. With $g=-x'$ and the convex chain rule, $$\label{eq:dissipation}
 \frac{d}{dt}\frac{\rho^2}{2}=-J(x),\qquad
 \frac{d}{dt}J(x)=-\lVert x'\rVert_2^2$$ almost everywhere.

[\[lem:consensus\]]{#lem:consensus label="lem:consensus"} The solution reaches $\bar x\mathbf1$ by a time $T$ satisfying $$\label{eq:Tbound}
 T\leq\sqrt n\,\lVert x^0-\bar x\mathbf1\rVert_2,$$ and remains there.

For each $i$, path telescoping and averaging give $$|x_i-\bar x|\leq\frac1n\sum_j|x_i-x_j|\leq J(x).$$ Hence $\rho\leq\sqrt n J(x)$. While $\rho>0$, the first identity in [\[eq:dissipation\]](#eq:dissipation){reference-type="eqref" reference="eq:dissipation"} yields $\rho'=-J(x)/\rho\leq-1/\sqrt n$. Integration proves [\[eq:Tbound\]](#eq:Tbound){reference-type="eqref" reference="eq:Tbound"}. At a constant vector the minimal subgradient is zero, so uniqueness keeps the state constant.

\>0

# Exact block dynamics and joint collisions

A maximal constant block $B=[\ell,r]$ has size $m=r-\ell+1$. Define its exterior signs $$s_{\ell-1}=\begin{cases}\operatorname{sign}(x_\ell-x_{\ell-1}),&\ell>1,\\0,&\ell=1,
 \end{cases}\qquad
 s_r=\begin{cases}\operatorname{sign}(x_{r+1}-x_r),&r<n,\\0,&r=n.
 \end{cases}$$

[\[lem:flux\]]{#lem:flux label="lem:flux"} On the zero-jump edges internal to $B$, set $$\label{eq:flux}
 z_{\ell+k-1}=s_{\ell-1}+\frac{k}{m}(s_r-s_{\ell-1}),
 \qquad k=1,\ldots,m-1.$$ Together with the exterior signs, this is an admissible subgradient flux and every coordinate in $B$ has velocity $$\label{eq:velocity}
 v_B=\frac{s_r-s_{\ell-1}}{m}.$$

The interpolation [\[eq:flux\]](#eq:flux){reference-type="eqref" reference="eq:flux"} stays in $[-1,1]=\operatorname{Sgn}(0)$, so it is admissible in [\[eq:subgrad\]](#eq:subgrad){reference-type="eqref" reference="eq:subgrad"}. Consecutive flux differences are all $(s_{\ell-1}-s_r)/m$ on $B$. Thus $D^{\mathsf T}z$ is constant there and $-D^{\mathsf T}z$ equals [\[eq:velocity\]](#eq:velocity){reference-type="eqref" reference="eq:velocity"}. The same interpolation uniquely minimizes the sum of squared consecutive flux differences with the two boundary values. Once the exterior nonzero-edge signs are fixed, $\lVert D^{\mathsf T}z\rVert_2^2$ is the sum of these contributions over the maximal plateaus, so the global minimization separates blockwise. Thus the local discrete Dirichlet minimizer is exactly the minimal-norm subgradient selected by the right derivative of the flow.

[\[thm:atlas\]]{#thm:atlas label="thm:atlas"} The solution of [\[eq:flow\]](#eq:flow){reference-type="eqref" reference="eq:flow"} is piecewise affine. Between events each maximal block moves with [\[eq:velocity\]](#eq:velocity){reference-type="eqref" reference="eq:velocity"}. Blocks never split. At an event, every connected string of adjacent blocks whose affine heights agree is replaced by its union; disjoint simultaneous collisions are handled at the same time. Every event lowers the block count, so there are at most $n-1$ distinct event times, after which consensus holds.

While adjacent heights are unequal, all exterior signs and block sizes are fixed. Lemma [\[lem:flux\]](#lem:flux){reference-type="ref" reference="lem:flux"} therefore produces constant velocities and an affine curve satisfying [\[eq:flow\]](#eq:flow){reference-type="eqref" reference="eq:flow"}; uniqueness identifies it with the semigroup solution. A current plateau has one common velocity and cannot split before the first adjacent equality.

At equality, union each maximal connected string of equal heights and apply Lemma [\[lem:flux\]](#lem:flux){reference-type="ref" reference="lem:flux"} to the union. It again has one velocity; uniqueness forbids a later split. Joint union makes the result independent of any artificial ordering among simultaneous collisions. Each event removes at least one block, proving the event bound. If several blocks remained forever without another equality, their affine solution would contradict finite consensus from Lemma [\[lem:consensus\]](#lem:consensus){reference-type="ref" reference="lem:consensus"}; hence the construction closes.

If current blocks have heights $h_j$ and velocities $v_j$, the next event is the least positive number among $$\tau_j=\frac{h_{j+1}-h_j}{v_j-v_{j+1}}.$$ All quantities are rational whenever $x^0$ is rational. The formula also covers endpoint blocks through the missing-flux value zero. For $n=1$ or constant data there are no events.

\>1

# The all-time ROF identity

The denoising model of Rudin, Osher, and Fatemi [@ROF1992] motivates the finite path resolvent $$\label{eq:rof}
 R_t(x^0)=\underset{y\in\mathbb{R}^n}{\operatorname{argmin}}
 \left\{\frac12\lVert y-x^0\rVert_2^2+tJ(y)\right\}.$$ The relationship between graph ROF and graph TV flow requires care: the full one-dimensional equivalence does not persist on arbitrary graphs without additional hypotheses [@KSS2019]. Space-discrete one-dimensional flow--regularization equivalence was proved by Steidl et al. [@Steidl2004], and fused-lasso fusion paths have direct algorithmic precedent [@Hoefling2010]. We claim only the self-contained path certificate below, not priority for equivalence or monotone fusion.

[\[thm:rof\]]{#thm:rof label="thm:rof"} For every $t\geq0$ and every $x^0\in\mathbb{R}^n$, $$x(t)=R_t(x^0).$$ This includes collision times and all post-consensus times.

Fix $t>0$ and write $-x'(s)=D^{\mathsf T}z(s)$ with $z_i(s)\in\operatorname{Sgn}((Dx(s))_i)$ almost everywhere. If $(Dx(t))_i\ne0$, edge $i$ has never entered a merged block: Theorem [\[thm:atlas\]](#thm:atlas){reference-type="ref" reference="thm:atlas"} would otherwise keep it zero. Continuity prevents its sign from changing without first vanishing, so $z_i(s)=\operatorname{sign}((Dx(t))_i)$ almost everywhere on $[0,t]$. If $(Dx(t))_i=0$, every $z_i(s)$ merely lies in $[-1,1]$.

For $\bar z=t^{-1}\int_0^t z(s)\,ds$, the two cases imply $\bar z_i\in\operatorname{Sgn}((Dx(t))_i)$. Integrating [\[eq:flow\]](#eq:flow){reference-type="eqref" reference="eq:flow"} gives $$\frac{x^0-x(t)}{t}=D^{\mathsf T}\bar z\in\partial J(x(t)),$$ or $0\in x(t)-x^0+t\partial J(x(t))$. This is the KKT condition for [\[eq:rof\]](#eq:rof){reference-type="eqref" reference="eq:rof"}; strict convexity of the quadratic term makes its minimizer unique. The case $t=0$ is immediate.

# Executable receipt, boundaries, and Route-A nonclaim

Two independent exact engines agree on all $19{,}530$ inputs in $\{-2,-1,0,1,2\}^n$, $1\leq n\leq6$, and five rational stresses of dimensions 8--12. The coordinate checker reports $1{,}010{,}097$ assertions; a separate SymPy reconstruction reports $3{,}707$ identities and inequalities; two fresh replays are byte identical; and 58/58 repaired-hash attacks plus a stale-hash control fail. These checks audit conventions and implementation; they do not prove the all-real theorems.

The theorem includes singletons, constant data, endpoint facets, rational states, and chained or disjoint simultaneous mergers. It does not assert the ROF identity for branched, cyclic, weighted, or differently normalized graphs.

Finite-time consensus leaves only constant fixed points as periodic orbits. There is no rational-prime owner, prime-power repetition, dynamical Euler product, target divisor, functional equation, or same-clock unitary lift. Under `NO_BAD_EULER_OR_ROOT_NUMBER`, the strict tuple is $$\begin{gathered}
 \texttt{(A0\_FAIL,A1\_FAIL,A2\_FAIL,}\\[-2pt]
 \texttt{A3\_FAIL,A4\_FAIL)},
 \end{gathered}$$ the overall verdict is `ROUTE_A_REJECTED`, and Route B is disabled.

9 H. Brezis, *Opérateurs maximaux monotones et semi-groupes de contractions dans les espaces de Hilbert*, North-Holland Mathematics Studies 5, 1973, MR0348562.

L. I. Rudin, S. Osher, and E. Fatemi, *Nonlinear total variation based noise removal algorithms*, Physica D **60** (1992), 259--268, [doi:10.1016/0167-2789(92)90242-F](https://doi.org/10.1016/0167-2789(92)90242-F).

C. Kirisits, O. Scherzer, and E. Setterqvist, *Invariant $\varphi$-minimal sets and total variation denoising on graphs*, SIAM Journal on Imaging Sciences **12**(4) (2019), 1643--1668, [doi:10.1137/19M124126X](https://doi.org/10.1137/19M124126X).

J. M. Mazón, M. Solera, and J. Toledo, *The total variation flow in metric random walk spaces*, Calculus of Variations and Partial Differential Equations **59** (2020), article 29, [doi:10.1007/s00526-019-1684-z](https://doi.org/10.1007/s00526-019-1684-z).

\>1 G. Steidl, J. Weickert, T. Brox, P. Mrázek, and M. Welk, *On the equivalence of soft wavelet shrinkage, total variation diffusion, total variation regularization, and SIDEs*, SIAM Journal on Numerical Analysis **42**(2) (2004), 686--713, [doi:10.1137/S0036142903422429](https://doi.org/10.1137/S0036142903422429).

H. Hoefling, *A path algorithm for the fused lasso signal approximator*, Journal of Computational and Graphical Statistics **19**(4) (2010), 984--1006, [doi:10.1198/jcgs.2010.09208](https://doi.org/10.1198/jcgs.2010.09208).
