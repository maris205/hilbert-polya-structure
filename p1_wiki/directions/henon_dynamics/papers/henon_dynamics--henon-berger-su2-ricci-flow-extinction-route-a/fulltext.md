---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-berger-su2-ricci-flow-extinction-route-a"
canonical_tex: "henon_dynamics/henon_berger_su2_ricci_flow_extinction_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_berger_su2_ricci_flow_extinction_route_a/paper/main.pdf"
source_sha256: "27db2fd0bc3de37f646902145b8205a5b5b2c365866cf7cb6d9da04ac4cfb88e"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Exact Lifespans and Round Extinction for Berger Ricci Flow

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_berger_su2_ricci_flow_extinction_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_berger_su2_ricci_flow_extinction_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_berger_su2_ricci_flow_extinction_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_berger_su2_ricci_flow_extinction_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We give a maximal-interval classification of Ricci flow on the complete two-parameter Berger family of left-invariant metrics on $SU(2)$. A fixed Maurer--Cartan convention yields the curvature tensor and a planar metric equation. Its aspect ratio is monotone, while an anisotropy scale is exactly conserved. Two scalar charts integrate the squashed and stretched chambers: one produces an $\operatorname{atanh}$ lifetime and an ancient branch, and the other an $\arctan$ lifetime and a finite anisotropic backward endpoint. Every positive solution has finite forward Type-I extinction and becomes round with both metric coefficients asymptotic to four times the remaining time. The volume-normalized flow is forward complete and converges exponentially to the unique round metric on its volume leaf. Exact rational, symbolic, replay, and adversarial receipts audit the formulas without replacing the global proof. No literature-priority or arithmetic-target claim is made.
author:
- 'HCS-C360 source-local reconstruction'
date: 4 September 2026
title: |
  Exact Lifespans and Round Extinction\
  for Berger Ricci Flow
```

## Markdown 正文

**Revision certificate.** =0 Round zero curvature reduction and first integral closure. =1 Round one exact lifespan and Type I extinction closure. Round two normalized convergence, evidence, and Route A closure.

# Convention and complete atlas

Choose left-invariant one-forms satisfying $$d\sigma_1=2\sigma_2\wedge\sigma_3,
 \qquad d\sigma_2=2\sigma_3\wedge\sigma_1,
 \qquad d\sigma_3=2\sigma_1\wedge\sigma_2,$$ and consider the positive Berger cone $$g=A(\sigma_1^2+\sigma_2^2)+C\sigma_3^2,
 \qquad A,C>0.                                      \label{eq:metric}$$ Changing every sign in (1) changes orientation but none of the curvature or flow formulas below. Put $r=C/A$.

[\[thm:atlas\]]{#thm:atlas label="thm:atlas"} The cone (2) is invariant under unnormalized Ricci flow, and $$A'=-8+4r,\qquad C'=-4r^2,
 \qquad r'=\frac{8r(1-r)}{A}.                       \label{eq:flow}$$ Every positive solution has a finite forward endpoint $T$, satisfies $$r(t)\longrightarrow1,\hspace{1em}
 A(t)\sim C(t)\sim4(T-t),\qquad
 (T-t)R(t)\longrightarrow\frac32,                 \label{eq:asymptotic}$$ and becomes extinct in a round Type-I singularity. The round and squashed branches are ancient. Every stretched branch has instead a finite backward endpoint at which $A\to0$ and $C\to\infty$.

Under volume-normalized Ricci flow every positive solution is forward complete, preserves $A^2C$, and converges exponentially to the unique round metric with that volume.

# Curvature and reduction

Let $X_i$ be dual to $\sigma_i$ and let $e_1=X_1/\sqrt A$, $e_2=X_2/\sqrt A$, $e_3=X_3/\sqrt C$. The Koszul formula in this orthonormal Milnor frame gives $$\begin{aligned}
 K_{12}&=\frac{4A-3C}{A^2}, &
 K_{13}=K_{23}&=\frac{C}{A^2},                       \label{eq:sectional}\\
 \operatorname{Ric}(e_1,e_1)=\operatorname{Ric}(e_2,e_2)&=\frac4A-\frac{2C}{A^2}, &
 \operatorname{Ric}(e_3,e_3)&=\frac{2C}{A^2}.                    \label{eq:ricci}\end{aligned}$$ Indeed, inserting the three rescaled structure constants into Koszul's identity $2\langle\nabla_XY,Z\rangle=\langle[X,Y],Z\rangle-
\langle[Y,Z],X\rangle+\langle[Z,X],Y\rangle$ and then into the curvature definition yields (5); summing the two planes through each $e_i$ gives (6). Consequently $$R=\frac{8A-2C}{A^2}.                               \label{eq:scalar}$$ Since $\operatorname{Ric}(X_1,X_1)=A\operatorname{Ric}(e_1,e_1)$ and $\operatorname{Ric}(X_3,X_3)=C\operatorname{Ric}(e_3,e_3)$, the equation $g'=-2\operatorname{Ric}$ is precisely (3). Direct differentiation gives its ratio equation.

[\[lem:first\]]{#lem:first label="lem:first"} Off the round ray, the positive quantity $$k=\frac{C}{\sqrt{|1-r|}}           \label{eq:first}$$ is constant along every trajectory.

It is enough to square (8). In the chamber $r<1$, $$\frac{d}{dt}\frac{C^2}{1-r}
 =\frac{2CC'}{1-r}+\frac{C^2r'}{(1-r)^2}=0$$ after substitution from (3). Replacing $1-r$ by $r-1$ and changing the second sign gives the same cancellation above the round ray.

Equation (3) now already determines the phase portrait: $r$ increases below one and decreases above one. A nonround trajectory never crosses the round ray because its constant $k$ would otherwise force $C$ to vanish there.

\>0

# Exact clocks and maximal intervals

In the squashed chamber set $u=\sqrt{1-r}\in(0,1)$. Lemma [\[lem:first\]](#lem:first){reference-type="ref" reference="lem:first"} and (3) become $$A=\frac{ku}{1-u^2},\qquad C=ku,
 \qquad u'=-\frac4k(1-u^2)^2.                       \label{eq:u}$$ Thus the remaining forward time is $$T-t=\frac{k}{8}\left(\frac{u}{1-u^2}
                    +\operatorname{atanh}u\right). \label{eq:utime}$$ The primitive follows by differentiation. It is finite at $u=0$ and diverges at $u=1$. Hence the future endpoint has $u\to0$, whereas backward time is infinite and $u\to1$, $A\to\infty$, $C\to k$.

For the stretched chamber set $v=\sqrt{r-1}>0$. Then $$A=\frac{kv}{1+v^2},\qquad C=kv,
 \qquad v'=-\frac4k(1+v^2)^2.                       \label{eq:v}$$ Its forward and backward remaining times are respectively $$\begin{aligned}
 T-t&=\frac{k}{8}\left(\frac{v}{1+v^2}+\arctan v\right),
                                                               \label{eq:vfuture}\\
 t-T_-&=\frac{k}{8}\left(\frac\pi2-\frac{v}{1+v^2}
                                      -\arctan v\right).     \label{eq:vback}\end{aligned}$$ Both are finite. At $T_-$ one has $v\to\infty$, so (11) gives $A\to0$ and $C\to\infty$. These two chart exhaustions, together with the round solution $A=C=A_0-4t$, prove every maximal-interval assertion in Theorem [\[thm:atlas\]](#thm:atlas){reference-type="ref" reference="thm:atlas"}.

As $z\to0$, either bracket in (10) or (12) equals $2z+O(z^3)$. Therefore $z=4(T-t)/k+O((T-t)^3)$, and (9) or (11) yields $$A=4(T-t)+O((T-t)^3),\qquad
 C=4(T-t)+O((T-t)^3).$$ This proves (4). Equations (5) show $|\operatorname{Rm}|=O((T-t)^{-1})$. In fact the same substitution gives $(T-t)K_{13}\to1/4$ and $(T-t)R\to3/2$. Thus curvature actually diverges, and the endpoint is a genuine Type-I singularity rather than merely a degenerate metric-cone boundary.

\>1

# Volume normalization and geometric walls

Adding $(2/3)Rg$ to the unnormalized equation gives $$A'=\frac83(r-1),\qquad
 C'=\frac{16}{3}r(1-r),\qquad
 r'=\frac{8r(1-r)}A.                                \label{eq:normalized}$$ A calculation gives $(A^2C)'=0$. On a fixed-volume leaf write $K=(A^2C)^{1/3}$; then $$A=Kr^{-1/3},\qquad C=Kr^{2/3},\qquad
 r'=\frac8K r^{4/3}(1-r).                            \label{eq:scalar-norm}$$ The scalar right-hand side points toward one, so a positive solution remains in the compact interval between $r(0)$ and $1$. Formula (15) then keeps $A,C$ in a compact subset of the metric cone and proves forward completeness. Monotonicity gives a limit; (15) forces that limit to be one. Its derivative there is $-8/K$, proving exponential convergence.

The exact curvature wall is richer than a single "positive curvature" label. Mixed sectional curvature is always positive; horizontal sectional curvature changes sign at $r=4/3$, horizontal Ricci curvature at $r=2$, and scalar curvature at $r=4$. All positive ratios nevertheless flow forward toward $r=1$. The faces $A=0$ and $C=0$ are degenerate tensors rather than Riemannian metrics. The local calculation also descends to a finite left quotient whenever the metric descends; no classification of all quotients is needed here.

# Evidence, sources, and Route-A boundary

The finite certificate contains 12 curvature rows, 14 anisotropy-chart rows, 18 lifespan rows, 12 normalized-flow rows, and seven boundary rows. An independent implementation reconstructs all entries and strict serialization contracts; a separate symbolic derivation checks 26 identities; two isolated replays agree byte for byte; and 60 repaired-hash or parser attacks are rejected. These are algebra and implementation receipts. They do not prove maximality, endpoint asymptotics, or normalized convergence; Sections 3--4 do.

Hamilton supplies the foundational Ricci-flow setting [@hamilton]; Isenberg and Jackson give homogeneous-flow context [@isenbergjackson]. The coefficients and classification above are rederived in the convention (1), and no priority claim is made.

The strict Route-A tuple is $$(\mathrm{A0\_FAIL},\mathrm{A1\_FAIL},\mathrm{A2\_FAIL},
  \mathrm{A3\_FAIL},\mathrm{A4\_FAIL}).$$ Continuous metric coefficients furnish neither intrinsic rational-prime objects nor a prime-power repetition law or logarithmic-prime clock. There is no target determinant, analytic bridge, or natural target-zero quantization. Route A is rejected and Route B is locked. No target arithmetic local data, Euler factors, bad-prime data, root number, automorphy, target divisor or counting law, target functional equation, target-zero match, or Hilbert--Pólya operator is claimed.

The theorem is intentionally limited to the two-axis Berger cone. It does not classify three unequal left-invariant axes, continue weakly through extinction, or assert convergence of Laplace spectra.

9 R. S. Hamilton, "Three-manifolds with positive Ricci curvature," *J. Differential Geom.* 17 (1982), 255--306. [doi:10.4310/jdg/1214436922](https://doi.org/10.4310/jdg/1214436922).

J. Isenberg and M. Jackson, "Ricci flow of locally homogeneous geometries on closed manifolds," *J. Differential Geom.* 35 (1992), 723--741. [doi:10.4310/jdg/1214448265](https://doi.org/10.4310/jdg/1214448265).
