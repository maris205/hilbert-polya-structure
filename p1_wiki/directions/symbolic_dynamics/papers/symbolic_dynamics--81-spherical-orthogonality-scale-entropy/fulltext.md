---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--81-spherical-orthogonality-scale-entropy"
canonical_tex: "symbolic_dynamics/papers/81-spherical-orthogonality-scale-entropy/main.tex"
canonical_pdf: "symbolic_dynamics/papers/81-spherical-orthogonality-scale-entropy/main.pdf"
source_sha256: "2af95a6c7ba3726e7fa0634dddbe58454a1c84fd01a8abce3409092f5dfb92d9"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Scale Entropy and Periodic Gluing in Spherical Orthogonality Shifts

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/81-spherical-orthogonality-scale-entropy>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/81-spherical-orthogonality-scale-entropy/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/81-spherical-orthogonality-scale-entropy/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/81-spherical-orthogonality-scale-entropy/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/81-spherical-orthogonality-scale-entropy/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For $d\geq3$, consider the compact-alphabet subshift $$X_d=\{x\in(\mathbb S^{d-1})^{\mathbb Z}:\langle x_j,x_{j+1}\rangle=0
         \text{ for every }j\}.$$ Every pair of endpoint vectors can be joined by an orthogonal path of every length at least two. Consequently $X_d$ is topologically mixing, and every finite word closes after inserting one symbol, so periodic points are dense. The manifold of $n$-blocks has dimension $n(d-2)+1$. For the exponentially weighted product metric, we prove the sharper dynamical statement $$h_\varepsilon(X_d)=(d-2)\log(1/\varepsilon)+O_d(1).$$ Thus the upper and lower metric mean dimensions both equal $d-2$, whereas the ordinary topological entropy is infinite. The upper bound uses a fixed spherical Voronoi net and counts only net points in an equatorial band, avoiding accumulated projection error. A homogeneous orthogonality Markov measure supplies the matching small-ball lower bound. We also identify this measure as the unique $O(d)$-invariant homogeneous one-step Markov law and record, as an owned harmonic-analytic input, the normalized Funk spectrum.
author:
- Anonymous
bibliography:
- references.bib
date: 'Internal Stage 2 draft, 27 August 2026'
title: Scale Entropy and Periodic Gluing in Spherical Orthogonality Shifts
```

## Markdown 正文

# Introduction

A closed relation on a compact alphabet defines a subshift by requiring each successive pair to lie in the relation. This point of view goes back to Friedland's entropy theory for graphs and closed relations [@Friedland1991]; recent work develops metric mean dimension for such compact-type subshifts in considerable generality [@Pessil2025]. Orthogonality on a sphere gives a particularly symmetric, non-finite-state example. It is at once a path space of the continuum orthogonality graph and a stationary Markov space.

Random homomorphisms into orthogonality graphs and their natural Markov law have already been studied in depth by Kunszenti-Kovács, Lovász, and Szegedy [@KunszentiEtAl2024]. In particular, the associated Funk operator and its spherical-harmonic spectrum are not new ingredients here. Our question is different: how many orbit names are visible at metric scale $\varepsilon$? The answer loses one dimension per time step from the full sphere shift. More precisely, its scale entropy has leading coefficient $d-2$, exactly the dimension of a successor equator.

There is a small technical trap in the upper bound. Repeatedly projecting an approximate successor onto the next approximate equator accumulates error. Instead we quantize every coordinate with one fixed spherical net. Given a net symbol, every legal next symbol lies in a band of width $O(\varepsilon)$ about its equator. The band contains only $O(\varepsilon^{-(d-2)})$ net points, which gives the correct exponent without a recursive approximation.

# The orthogonality shift and finite blocks

Let $\mathbb S^{d-1}=\{u\in\mathbb R^d:\|u\|_2=1\}$, with $d\geq3$, and define $$X_d=\{x=(x_j)_{j\in\mathbb Z}\in(\mathbb S^{d-1})^{\mathbb Z}:
       x_j\perp x_{j+1}\text{ for all }j\}.$$ The left shift is denoted by $\sigma$. For $n\geq1$, its legal block space is $$\mathcal M_{d,n}=\{(x_0,\ldots,x_{n-1})\in(\mathbb S^{d-1})^n:
          x_i\perp x_{i+1},\ 0\leq i<n-1\}.$$

[\[prop:manifold\]]{#prop:manifold label="prop:manifold"} The space $\mathcal M_{d,n}$ is a compact, connected smooth manifold of dimension $$\dim\mathcal M_{d,n}=n(d-2)+1.$$ Every legal finite block extends to a point of $X_d$.

Choose $x_0\in\mathbb S^{d-1}$ freely. Once $x_i$ is fixed, the successor $x_{i+1}$ lies on the unit sphere in $x_i^\perp$, which is a copy of $\mathbb S^{d-2}$. More formally, forgetting the last coordinate realizes $\mathcal M_{d,n+1}\to\mathcal M_{d,n}$ as the unit-sphere bundle of the rank-$(d-1)$ vector bundle whose fiber at a block is $x_{n-1}^\perp$. Induction gives smoothness and $$(d-1)+(n-1)(d-2)=n(d-2)+1.$$ The base and fiber are compact and connected for $d\geq3$, proving the same for the total space. Repeatedly choosing any unit vector in the orthogonal complement of the current endpoint extends a block in both directions.

# All-length bridges and periodic closure

[\[lem:bridge\]]{#lem:bridge label="lem:bridge"} For any $u,v\in\mathbb S^{d-1}$ and every integer $L\geq2$, there are $y_0,\ldots,y_L\in\mathbb S^{d-1}$ with $y_0=u$, $y_L=v$, and $y_i\perp y_{i+1}$ for all $i$.

For $L=2$, choose a unit vector in $u^\perp\cap v^\perp$, whose dimension is at least $d-2\geq1$. For $L=3$, first choose $y_1\perp u$, then choose a unit $y_2\in y_1^\perp\cap v^\perp$. Finally, any bridge can be lengthened by two by inserting $y_i,w,y_i$ at one endpoint, where $w\perp y_i$. The cases $L=2,3$ therefore generate every $L\geq2$.

[\[thm:gluing\]]{#thm:gluing label="thm:gluing"} The system $(X_d,\sigma)$ is topologically mixing. Moreover, every legal $n$-block occurs in a periodic point of period at most $n+1$; in particular, periodic points are dense.

Two nonempty cylinder sets prescribe finite legal blocks, up to arbitrarily small open perturbations. For every sufficiently large separation, the right endpoint of the first block and the left endpoint of the second are joined by [\[lem:bridge\]](#lem:bridge){reference-type="ref" reference="lem:bridge"} with exactly the required number of edges. This is the cylinder criterion for topological mixing.

Given a legal block $(x_0,\ldots,x_{n-1})$, choose a unit vector $z\in x_{n-1}^\perp\cap x_0^\perp$. The periodic concatenation of $(x_0,\ldots,x_{n-1},z)$ is legal and contains the original block. Cylinder sets form a basis, so these periodic points are dense.

# Scale entropy

Fix $\rho>1$ and equip $X_d$ with $$D_\rho(x,y)=\sup_{j\in\mathbb Z}\rho^{-|j|}\|x_j-y_j\|_2.$$ The $n$-step Bowen metric is $D_{\rho,n}(x,y)=\max_{0\leq t<n}D_\rho(\sigma^tx,\sigma^ty)$. If $N(X_d,D_{\rho,n},\varepsilon)$ is the least number of open $D_{\rho,n}$-balls of radius $\varepsilon$ needed to cover $X_d$, set $$h_\varepsilon(X_d,D_\rho)
 =\limsup_{n\to\infty}\frac1n
   \log N(X_d,D_{\rho,n},\varepsilon).$$ The lower and upper metric mean dimensions are the corresponding lower and upper limits of $h_\varepsilon/\log(1/\varepsilon)$ as $\varepsilon\downarrow0$ [@LindenstraussWeiss2000].

We first record two elementary uniform estimates. For $0<\delta<1/10$, a maximal $\delta$-separated set $P_\delta\subset\mathbb S^{d-1}$ has $$\label{eq:net-size}
 |P_\delta|\leq C_d\delta^{-(d-1)}.$$ For each $p\in P_\delta$, the number of $q\in P_\delta$ satisfying $$\label{eq:band}
 |\langle p,q\rangle|\leq2\delta$$ is at most $C_d\delta^{-(d-2)}$. Indeed, disjoint spherical balls of radius $\delta/3$ around such $q$ lie in an $O(\delta)$-thick equatorial band. The band has surface measure $O_d(\delta)$, while each ball has measure bounded below by $c_d\delta^{d-1}$.

[\[lem:upper-block\]]{#lem:upper-block label="lem:upper-block"} For the coordinate supremum metric on $\mathcal M_{d,N}$, $$N(\mathcal M_{d,N},\|\cdot\|_\infty,2\delta)
 \leq C_d\delta^{-(d-1)}
       \left(C_d\delta^{-(d-2)}\right)^{N-1}.$$

Assign each spherical coordinate to a nearest point of $P_\delta$, breaking ties once and for all. If an orthogonal pair $(u,v)$ receives the names $(p,q)$, then $$|\langle p,q\rangle|
 \leq\|p-u\|_2+\|q-v\|_2\leq2\delta.$$ Thus the first coordinate has at most the number of choices in [\[eq:net-size\]](#eq:net-size){reference-type="eqref" reference="eq:net-size"}, and every later name has at most the equatorial-band number in [\[eq:band\]](#eq:band){reference-type="eqref" reference="eq:band"}. Two legal blocks with the same name are within $2\delta$ in every coordinate. In fact the inequality is strict. Equality for two distinct sphere points assigned to the same net point $p$ would force equality in both triangle inequalities and hence three distinct collinear points of the unit sphere, which is impossible. Since a block has finitely many coordinates, its coordinate supremum distance from a representative of its name class is strictly less than $2\delta$. Selecting one representative from every nonempty name class therefore gives the asserted open-ball cover.

For the lower bound, let $\nu_d$ be normalized surface measure on $\mathbb S^{d-1}$ and let $K_d(u,\cdot)$ be normalized surface measure on the equator $u^\perp\cap\mathbb S^{d-1}$. The edge law $\nu_d(du)K_d(u,dv)$ is symmetric under exchanging $u$ and $v$; hence $\nu_dK_d=\nu_d$, and the stationary two-sided Markov law with marginal $\nu_d$ and transition $K_d$ exists. It is denoted $\mu_d$. Uniform spherical-cap estimates give, for $0<\varepsilon<1/4$ and every legal block $x$, $$\label{eq:small-ball}
 \mu_d\{y:\|y_i-x_i\|_2<\varepsilon,\ 0\leq i<n\}
 \leq C_d^n\varepsilon^{(d-1)+(n-1)(d-2)}.$$ The estimate is uniform because the intersection of any ambient $\varepsilon$-ball with any successor equator has normalized $(d-2)$-dimensional measure at most $C_d\varepsilon^{d-2}$. Applying this bound successively through the Markov disintegration proves [\[eq:small-ball\]](#eq:small-ball){reference-type="eqref" reference="eq:small-ball"}.

[\[thm:scale\]]{#thm:scale label="thm:scale"} As $\varepsilon\downarrow0$, $$h_\varepsilon(X_d,D_\rho)
 =(d-2)\log(1/\varepsilon)+O_d(1).$$ Consequently $$\underline{\operatorname{mdim}}_{M}(X_d,D_\rho,\sigma)
 =\overline{\operatorname{mdim}}_{M}(X_d,D_\rho,\sigma)=d-2,$$ and $h_{\mathrm{top}}(X_d,\sigma)=\infty$.

A $D_{\rho,n}$-ball of radius $\varepsilon$ forces its coordinates $0,\ldots,n-1$ to lie in the corresponding coordinate balls of radius $\varepsilon$. Hence [\[eq:small-ball\]](#eq:small-ball){reference-type="eqref" reference="eq:small-ball"} bounds the $\mu_d$-measure of every such Bowen ball. Any cover has total measure one, so $$N(X_d,D_{\rho,n},\varepsilon)
 \geq C_d^{-n}\varepsilon^{-n(d-2)-1}.$$ After taking $n^{-1}\log$ and then the limsup, this is $$h_\varepsilon\geq(d-2)\log(1/\varepsilon)-\log C_d.$$

For the reverse inequality, the Bowen metric has the exact coordinate form $$D_{\rho,n}(x,y)
 =\sup_{j\in\mathbb Z}\rho^{-\operatorname{dist}(j,[0,n-1])}\|x_j-y_j\|_2.$$ Choose $m=m(\varepsilon)$ so that $2\rho^{-(m+1)}<\varepsilon/2$, and put $\delta=\varepsilon/4$. Apply [\[lem:upper-block\]](#lem:upper-block){reference-type="ref" reference="lem:upper-block"} to the extended block of coordinates $-m,\ldots,n-1+m$. Extend one representative of each nonempty block-name class to a point of $X_d$, using [\[prop:manifold\]](#prop:manifold){reference-type="ref" reference="prop:manifold"}. Equal names give coordinate error at most $2\delta=\varepsilon/2$ inside the extended block, while coordinates outside it contribute less than $\varepsilon/2$. These representatives form a $D_{\rho,n}$ cover. With $N=n+2m$, $$N(X_d,D_{\rho,n},\varepsilon)
 \leq C_d\delta^{-(d-1)}
       (C_d\delta^{-(d-2)})^{N-1}.$$ For fixed $\varepsilon$, $m$ is independent of $n$. Divide by $n$, let $n\to\infty$, and absorb $\delta=\varepsilon/4$ into the constant to obtain the matching upper estimate. Dividing by $\log(1/\varepsilon)$ gives both metric mean dimensions. Finally $h_\varepsilon\to\infty$, and the standard metric characterization of topological entropy gives infinite entropy.

# The homogeneous Markov law and an owned spectral input

The kernel $K_d$ above is the normalized Funk transform. Its role in orthogonality Markov spaces, including its full spectrum, belongs to the existing theory [@KunszentiEtAl2024]; classical background on the Funk transform is in @Helgason1999.

[\[prop:unique\]]{#prop:unique label="prop:unique"} The measure $\mu_d$ is the unique stationary one-step Markov law on $X_d$ whose one-coordinate marginal is $O(d)$-invariant and which admits an $O(d)$-equivariant transition kernel, modulo the usual $\nu_d$-almost- everywhere identification of kernels. This is not a uniqueness statement among all $O(d)$-invariant stationary measures.

An $O(d)$-invariant probability on $\mathbb S^{d-1}$ must be $\nu_d$. Fixing $u$, equivariance makes the conditional successor law invariant under the stabilizer of $u$. That stabilizer acts transitively on $u^\perp\cap\mathbb S^{d-1}$, so its unique invariant probability is $K_d(u,\cdot)$. These data determine the stationary Markov law.

For contrast, sample a Haar orthonormal pair $(u,v)$ and repeat $\ldots,u,v,u,v,\ldots$ with a uniform phase. This gives an $O(d)$-invariant stationary law on $X_d$, but it is not Markov: the coordinate two steps back determines the next coordinate.

For completeness, the known spherical-harmonic diagonalization is $$\lambda_{2k}=(-1)^k\frac{(1/2)_k}{((d-1)/2)_k},\qquad
 \lambda_{2k+1}=0.$$ It yields the absolute spectral gap $$1-\sup_{\ell\geq1}|\lambda_\ell|=\frac{d-2}{d-1},$$ while the right, or Poincaré, gap is $$1-\sup_{\ell\geq1}\lambda_\ell
 =1-\frac{3}{(d-1)(d+1)}.$$ These are cited consequences of the normalized Funk spectrum, not novelty claims of this note.

# Deterministic controls and claim boundary

The companion exact-arithmetic control checks three finite shadows: all signed-coordinate endpoint pairs admit bridges of lengths $2$ through $12$; the constraint Jacobian has rank $2n-1$ for $3\leq d\leq10$ and $1\leq n\leq12$; and Gegenbauer evaluations agree with the displayed Funk eigenvalues through degree $24$. These controls audit fragile algebraic inputs and do not replace the geometric proofs.

The general compact-relation framework is credited to @Friedland1991 [@Pessil2025], and the natural orthogonality Markov law and Funk spectrum to @KunszentiEtAl2024. A bounded search through 27 August 2026 found no exact collision with the scale-entropy asymptotic and all-length periodic-gluing package proved here. This is not a worldwide priority claim. The manuscript remains on external-release hold.
