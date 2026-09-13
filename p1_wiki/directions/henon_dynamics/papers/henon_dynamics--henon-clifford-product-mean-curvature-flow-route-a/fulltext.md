---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-clifford-product-mean-curvature-flow-route-a"
canonical_tex: "henon_dynamics/henon_clifford_product_mean_curvature_flow_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_clifford_product_mean_curvature_flow_route_a/paper/main.pdf"
source_sha256: "18eff2e0fc8e1be28b050ad7ccef05cf396cd933f4cecd3a161ae74ff2695581"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Ancient Clifford-Product Mean-Curvature Flow: Exact Lifespans, Focal Cylinders, and Minimal Stability

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_clifford_product_mean_curvature_flow_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_clifford_product_mean_curvature_flow_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_clifford_product_mean_curvature_flow_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_clifford_product_mean_curvature_flow_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For every $p,q\geq1$, we solve mean-curvature flow inside the unit sphere for the full parallel family $S^p(\cos\theta)\times S^q(\sin\theta)$. The affine coordinate $y=\sin^2\theta$ gives both ancient branches, their exact finite lifespans, and their focal collapses. \>0 We identify both Type-I round-cylinder blow-ups and prove exact area dissipation. \>1 At the minimal leaf we compute the entire separated Jacobi spectrum below and at zero, obtaining index $p+q+3$ and nullity $(p+1)(q+1)$.
author:
- 'Route-A source-local certificate HCS-C319'
date: 3 September 2026
title: |
  Ancient Clifford-Product Mean-Curvature Flow:\
  Exact Lifespans, Focal Cylinders, and Minimal Stability
```

## Markdown 正文

trailerid \[\<C3192026090300000000000000000000\>\<C3192026090300000000000000000000\>\]

# Exact phase portrait and lifespan

Put $n=p+q$, and write $$\Sigma_\theta=S^p(\cos\theta)\times S^q(\sin\theta)
 \subset S^{n+1},\qquad 0<\theta<\frac\pi2.$$ For $x\in S^p$, $z\in S^q$, choose $\nu=(-\sin\theta\,x,\cos\theta\,z)$. Our scalar convention is $\partial_tF=H\nu$; this is the negative area gradient for the signs below.

[\[thm:phase\]]{#thm:phase label="thm:phase"} The principal curvatures are $\tan\theta$ with multiplicity $p$ and $-\cot\theta$ with multiplicity $q$. Hence $$H=p\tan\theta-q\cot\theta,
 \qquad y'=2(ny-q),\qquad y=\sin^2\theta.$$ The unique stationary leaf has $y_*=q/n$. Every other solution is ancient, $$\label{eq:solution}
 y(t)=\frac qn+\left(y_0-\frac qn\right)e^{2nt},$$ and has one finite forward endpoint. If $y_0<q/n$, then $$T_-=\frac1{2n}\log \frac q{q-ny_0},\qquad y(t)\downarrow0,$$ and the $S^p$ factor survives as the focal submanifold. If $y_0>q/n$, then $$T_+=\frac1{2n}\log \frac p{ny_0-q},\qquad y(t)\uparrow1,$$ and the $S^q$ factor survives. In both cases $y(t)\to q/n$ as $t\to-\infty$.

Differentiating $F=(\cos\theta\,x,\sin\theta\,z)$ gives $\partial_\theta F=\nu$. The two shape eigenvalues follow by differentiating $\nu$ along each factor. Thus $\theta'=H$, and multiplication by $2\sin\theta\cos\theta$ yields the affine equation for $y$. Solving it gives [\[eq:solution\]](#eq:solution){reference-type="eqref" reference="eq:solution"}; imposing $y=0$ or $y=1$ gives the stated times. Their logarithm arguments exceed one on the corresponding branches. Backward convergence, uniqueness of the stationary leaf, and the focal labels now follow directly.

The faces $y=0,1$ are focal submanifolds, not regular product hypersurfaces. The cases $p=0$ or $q=0$ are excluded degenerate sphere/double-cover geometries. The backward endpoint is at infinite time, not an added slice.

\>0

# Type-I focal-cylinder geometry

The exact curvature and area density (up to the constant sphere volumes) are $$\begin{aligned}
 |A|^2&=p\frac y{1-y}+q\frac{1-y}y,\label{eq:A2}\\
 \mathcal A(y)&=(1-y)^{p/2}y^{q/2}.\label{eq:area}\end{aligned}$$

[\[thm:typeI\]]{#thm:typeI label="thm:typeI"} Every nonstationary solution of Theorem [\[thm:phase\]](#thm:phase){reference-type="ref" reference="thm:phase"} satisfies $$\frac d{dt}\log\mathcal A=-H^2<0.$$ At a left collapse, $y=2q(T_--t)+O((T_--t)^2)$ and $$(T_--t)|A|^2\longrightarrow\frac12,\qquad
 \text{blow-up cylinder }S^q(\sqrt{2q})\times\mathbb R^p.$$ At a right collapse, $1-y=2p(T_+-t)+O((T_+-t)^2)$, the same residue is $1/2$, and the cylinder is $S^p(\sqrt{2p})\times\mathbb R^q$.

Taking the logarithmic derivative of [\[eq:area\]](#eq:area){reference-type="eqref" reference="eq:area"} and substituting $y'$ gives $$\left(\frac q{2y}-\frac p{2(1-y)}\right)2(ny-q)
 =-\frac{(ny-q)^2}{y(1-y)}=-H^2.$$ Linearising the exact affine solution at either finite endpoint gives the two expansions. Equation [\[eq:A2\]](#eq:A2){reference-type="eqref" reference="eq:A2"} then gives the Type-I residues. Under parabolic rescaling by $(T-t)^{-1/2}$, the collapsing sphere has squared radius $2q$ on the left and $2p$ on the right; the noncollapsing factor becomes its Euclidean tangent space. This proves the ordered cylinder statements.

\>1

# Jacobi index, nullity, and Route-A boundary

At the stationary leaf the radii are $\sqrt{p/n}$ and $\sqrt{q/n}$, $|A|^2=n$, and the normal Jacobi operator is $J=\Delta+|A|^2+n=\Delta+2n$. We fix the second-variation convention $\mathcal Q(f,f)=-\int_{\Sigma}fJf$.

[\[thm:spectrum\]]{#thm:spectrum label="thm:spectrum"} For spherical-harmonic degrees $\ell,m\geq0$, the eigenvalue of $-\Delta$ is $$\lambda_{\ell m}=\frac{n\ell(\ell+p-1)}p
 +\frac{nm(m+q-1)}q.$$ Exactly the sectors $(0,0),(1,0),(0,1)$ lie below $2n$, and only $(1,1)$ equals $2n$. Therefore, for the quadratic-form convention associated to $J$, the Morse index is $n+3$ and the nullity is $(p+1)(q+1)$.

Separation of variables on the two round factors gives $\lambda_{\ell m}$. For one factor, $\ell(\ell+p-1)/p$ equals $0$ at $\ell=0$, equals $1$ at $\ell=1$, and exceeds $2$ for $\ell\geq2$; the same holds for $m,q$. Thus the stated four sectors exhaust the values at or below $2n$. Their harmonic multiplicities are $1,p+1,q+1$, and $(p+1)(q+1)$, proving the counts.

#### Finite evidence.

The content-addressed atlas records 100 dimension pairs, 600 branch rows, and 3,600 spectral cells: 25,858 scalar leaves. An implementation-independent checker performs 22,738 checks, including independent normalized-area and dissipation calculations; SymPy closes 1,204 identities. Isolated replay is byte exact and 39 repaired-hash/parser mutations are rejected. These grids are regressions; Theorems [\[thm:phase\]](#thm:phase){reference-type="ref" reference="thm:phase"}--[\[thm:spectrum\]](#thm:spectrum){reference-type="ref" reference="thm:spectrum"} are analytic for all declared parameters.

#### Collision boundary.

C281 treats intrinsic homogeneous Ricci flow, while the present evolution is extrinsic spherical mean-curvature flow. C314 concerns planar curve shortening, whereas the present theorem closes a higher-dimensional isoparametric hypersurface family and its minimal Jacobi spectrum.

#### Route-A result and nonclaims.

Under `NO_BAD_EULER_OR_ROOT_NUMBER`, the strict tuple is $$(\mathrm{A0\_FAIL},\mathrm{A1\_FAIL},\mathrm{A2\_FAIL},
  \mathrm{A3\_FAIL},\mathrm{A4\_FORMAL\_HINT}).$$ The model supplies no arithmetic-prime owner, primitive-orbit Euler ledger, Euler product, target functional equation, counting law, or target-zero match. The Jacobi operator is source-local and only a formal spectral hint; it is not a Hilbert--Pólya operator. Route A is rejected and Route B stays locked. No classification beyond the two-factor family, target local data, root number, or automorphy is claimed.

#### AI use.

A generative language model assisted drafting and code scaffolding. The displayed proofs, independent recomputation, hostile tests, and deterministic artifacts define the audit record.

# Source lineage {#source-lineage .unnumbered}

9 F. dos Reis and K. Tenenblat, "The mean curvature flow by parallel hypersurfaces," *Proceedings of the American Mathematical Society* 146 (2018), 4867--4878. DOI: [10.1090/proc/14178](https://doi.org/10.1090/proc/14178).

H.-L. Liu and C.-L. Terng, "The mean curvature flow for isoparametric submanifolds," *Duke Mathematical Journal* 147 (2009), 157--179. DOI: [10.1215/00127094-2009-009](https://doi.org/10.1215/00127094-2009-009).
