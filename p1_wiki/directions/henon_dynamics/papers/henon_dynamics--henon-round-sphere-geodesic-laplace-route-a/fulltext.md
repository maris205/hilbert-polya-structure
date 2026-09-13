---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-round-sphere-geodesic-laplace-route-a"
canonical_tex: "henon_dynamics/henon_round_sphere_geodesic_laplace_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_round_sphere_geodesic_laplace_route_a/paper/main.pdf"
source_sha256: "da71bd70a037f7244074ef03bfca4819b72e322c2018e6de2127490183b7df85"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Clean Geodesic Return and Exact Laplace Revival on Round Spheres

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_round_sphere_geodesic_laplace_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_round_sphere_geodesic_laplace_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_round_sphere_geodesic_laplace_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_round_sphere_geodesic_laplace_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For every round sphere $S_R^d$, $d\ge2$, we solve the unit tangent flow, identify its oriented-Grassmann orbit quotient, and prove that every orbit has least period $2\pi R$ with maximally clean identity return. \>0 We then derive the full Laplace spectrum and heat trace and prove exact scalar and identity revivals for the natural completed-square half-wave. \>1 Independent exact and adversarial evidence audits this classical/quantum alignment while keeping it strictly source-local.
author:
- 'Route-A source-local certificate HCS-C313'
date: 3 September 2026
title: Clean Geodesic Return and Exact Laplace Revival on Round Spheres
```

## Markdown 正文

trailerid \[\<C3132026090300000000000000000000\>\<C3132026090300000000000000000000\>\]

# Classical flow, orbit quotient, and clean return

Embed $S_R^d$ in $\mathbb R^{d+1}$ and write $$T^1S_R^d=\{(x,v):|x|=R, |v|=1, x\cdot v=0\}.$$

[\[thm:flow\]]{#thm:flow label="thm:flow"} The unit-speed geodesic flow is $$\label{eq:flow}
 \Phi_t(x,v)=\left(\cos(t/R)x+R\sin(t/R)v,
 -R^{-1}\sin(t/R)x+\cos(t/R)v\right).$$ Every orbit has least period $L=2\pi R$. More precisely, $$\label{eq:fix}
 \operatorname{Fix}(\Phi_t)=\begin{cases}T^1S_R^d,&t\in L\mathbb Z,\\
 \varnothing,&t\notin L\mathbb Z.
 \end{cases}$$ At every return $D\Phi_t=I$, so [\[eq:fix\]](#eq:fix){reference-type="eqref" reference="eq:fix"} is clean with the largest possible fixed manifold. The orbit space is the oriented Grassmannian $G_2^+(\mathbb R^{d+1})$; the unit tangent bundle is its principal circle bundle. The flow preserves Liouville measure and is reversed by $\iota(x,v)=(x,-v)$.

The two displayed vectors keep norms $R,1$, remain orthogonal, and the first derivative is the second; its second derivative is $-R^{-2}x(t)$, the round geodesic equation. On the oriented plane spanned by the orthonormal frame $(x/R,v)$, [\[eq:flow\]](#eq:flow){reference-type="eqref" reference="eq:flow"} is rotation through $t/R$. It fixes that frame exactly at multiples of $2\pi$, proving least period and [\[eq:fix\]](#eq:fix){reference-type="eqref" reference="eq:fix"}; the ambient rotation is then the identity, so is its differential. Quotienting oriented frames by this circle rotation gives $G_2^+$, of dimension $2d-2$. Hamiltonian geodesic flow preserves Liouville measure, and direct substitution gives $\iota\Phi_t\iota=\Phi_{-t}$.

\>0

# Laplace spectrum, heat trace, and exact revival

Let $-\Delta\ge0$ be the Laplace--Beltrami operator. Restrictions of homogeneous harmonic polynomials of degree $\ell$ form $\mathcal H_\ell$.

[\[thm:spectrum\]]{#thm:spectrum label="thm:spectrum"} For every $\ell\ge0$, $$\label{eq:spectrum}
 -\Delta|_{\mathcal H_\ell}=\frac{\ell(\ell+d-1)}{R^2},\qquad
 m_{d,\ell}=\dim\mathcal H_\ell
 =\frac{(2\ell+d-1)(\ell+d-2)!}{\ell!(d-1)!}.$$ The spaces $\mathcal H_\ell$ form a complete orthogonal decomposition of $L^2(S_R^d)$. Consequently, for $s>0$, $$\label{eq:heat}
 \operatorname{Tr}(e^{s\Delta})=\sum_{\ell=0}^\infty
 m_{d,\ell}e^{-s\ell(\ell+d-1)/R^2}<\infty.$$ Define by spectral calculus $$\label{eq:Q}
 Q_d=\sqrt{-\Delta+\frac{(d-1)^2}{4R^2}}.$$ Then $$\label{eq:revival}
 e^{-i2\pi RQ_d}=(-1)^{d-1}I,\qquad e^{-i4\pi RQ_d}=I.$$

The Euclidean polar decomposition of homogeneous polynomials gives the eigenvalue in [\[eq:spectrum\]](#eq:spectrum){reference-type="eqref" reference="eq:spectrum"}. Subtracting the degree-$\ell-2$ polynomials divisible by $|x|^2$ gives $m_{d,\ell}=\binom{\ell+d}{d}-\binom{\ell+d-2}{d}$, equal to the displayed factorial. Polynomial density gives completeness. Since $m_{d,\ell}=O(\ell^{d-1})$ and the eigenvalue is quadratic, [\[eq:heat\]](#eq:heat){reference-type="eqref" reference="eq:heat"} converges. Finally, $$\ell(\ell+d-1)+(d-1)^2/4=(\ell+(d-1)/2)^2,$$ so $Q_d$ has frequency $(\ell+(d-1)/2)/R$. Substitution proves both phases in [\[eq:revival\]](#eq:revival){reference-type="eqref" reference="eq:revival"}.

The shift in [\[eq:Q\]](#eq:Q){reference-type="eqref" reference="eq:Q"} is a source functional-calculus completion of the square. No exact revival is claimed here for the unshifted $\sqrt{-\Delta}$, and no target spectrum is attached to either operator.

\>1

# Evidence, collisions, and Route-A boundary

Dimensions $2$ through $12$ and degrees $0$ through $40$ give 451 exact spectral cells, 33 finite heat partials, and 30 coordinate or tilted-frame flow probes: 3,074 audited leaves. An independent checker performs 3,296 checks. SymPy closes 1,220 constraint, multiplicity, cumulative-count, completed-square and revival identities; replay is byte exact and 26 repaired-hash/parser attacks must fail. These cutoffs regress the implementation; Theorems [\[thm:flow\]](#thm:flow){reference-type="ref" reference="thm:flow"}--[\[thm:spectrum\]](#thm:spectrum){reference-type="ref" reference="thm:spectrum"} are untruncated.

C242 has two isolated coordinate Reeb orbits on an irrational ellipsoid, C275 includes billiard reflections and caustics, and C281 evolves product sphere metrics by Ricci flow. C313 instead owns one fixed round metric, its maximally clean great-circle fibration, and its full Laplace quantization.

Under `NO_BAD_EULER_OR_ROOT_NUMBER`, the strict tuple is $$(\mathrm{A0\_FAIL},\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},
 \mathrm{A3\_FAIL},\mathrm{A4\_NATURAL\_QUANTIZATION}).$$ All geodesics close, but in a positive-dimensional clean family rather than as isolated primitives (A1). Harmonic degree and continuous radius have no rational-prime owner (A0) or logarithmic-prime clock (A2); the heat/revival identities are not a target determinant or functional equation (A3). The source Laplacian is a natural self-adjoint quantization, but it has no target zero match and is not a Hilbert--Pólya operator (A4). Route A is rejected and Route B stays locked. No target Euler factor, root number, automorphy, divisor law, functional equation, or zero correspondence is asserted.

#### AI use.

A generative language model assisted drafting and code scaffolding. The analytic derivations, independent cells, adversarial tests, and deterministic artifacts define the audit record.

# Source lineage {#source-lineage .unnumbered}

9 Y. Colin de Verdière, "Spectrum of the Laplace operator and periodic geodesics: thirty years after," *Ann. Inst. Fourier* 57 (2007), 2429--2463. DOI: [10.5802/aif.2339](https://doi.org/10.5802/aif.2339).
