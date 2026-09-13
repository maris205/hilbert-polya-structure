---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-heisenberg-subriemannian-cut-locus-route-a"
canonical_tex: "henon_dynamics/henon_heisenberg_subriemannian_cut_locus_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_heisenberg_subriemannian_cut_locus_route_a/paper/main.pdf"
source_sha256: "aa159aeea002049899f43f9a945dff41f8878f4c236e1cf7c7dc0dacd0c2056a"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Cut and First-Conjugate Geometry of the Standard Heisenberg Group: A Complete Hamiltonian and Distance Atlas

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_heisenberg_subriemannian_cut_locus_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_heisenberg_subriemannian_cut_locus_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_heisenberg_subriemannian_cut_locus_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_heisenberg_subriemannian_cut_locus_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the standard real Heisenberg group we integrate every unit-speed normal sub-Riemannian geodesic and close the global minimizing geometry, rather than stopping at an explicit orbit formula. We exclude nonconstant abnormal extremals, compute the exponential Jacobian, prove equality of the first cut, conjugate, and rotational Maxwell times, and determine the cut locus from the identity. A strictly monotone implicit angle gives the Carnot--Carathéodory distance, including both degenerate endpoint faces. All signs and factors are frozen to one frame convention; no extension to arbitrary Carnot groups is claimed.
author:
- HCS Research Program
date: 1 September 2026
title: |
  Cut and First-Conjugate Geometry of the Standard Heisenberg Group:\
  A Complete Hamiltonian and Distance Atlas
```

## Markdown 正文

# Frozen model

On $H^1=\mathbb R^3$ put $$X=\partial_x-\frac y2\partial_z,\qquad
 Y=\partial_y+\frac x2\partial_z,\qquad [X,Y]=\partial_z,$$ and make $X,Y$ orthonormal. The normal Hamiltonian is $$H=\frac12\left(p_x-\frac y2p_z\right)^2+
   \frac12\left(p_y+\frac x2p_z\right)^2.$$ Write $\lambda=p_z$ and impose $H=1/2$.

Every unit-speed normal geodesic from the identity has an angle $\phi$ and is, when $\lambda=0$, $$(x,y,z)=(t\cos\phi,t\sin\phi,0),$$ while for $\lambda\ne0$ it is $$\begin{aligned}
 x&=\frac{\sin(\phi+\lambda t)-\sin\phi}{\lambda},&
 y&=\frac{\cos\phi-\cos(\phi+\lambda t)}{\lambda},\\
 z&=\frac{\lambda t-\sin(\lambda t)}{2\lambda^2}.\end{aligned}$$ There are no nonconstant abnormal extremals. The first conjugate and cut times agree: $$t_{\rm conj}=t_{\rm cut}=\frac{2\pi}{|\lambda|}\quad(\lambda\ne0),$$ and the cut locus and first conjugate locus from the identity are both $\{(0,0,z):z\ne0\}$.

For $\rho=(x^2+y^2)^{1/2}>0$, let $\theta\in(-\pi,\pi)$ be the unique solution of $$\frac{4z}{\rho^2}=\frac{\theta-\sin\theta\cos\theta}{\sin^2\theta}.$$ Then $$d(0,(x,y,z))=\rho\frac{\theta}{\sin\theta}.$$ Continuously, $d=\rho$ when $z=0$, whereas $d(0,(0,0,z))=2\sqrt{\pi|z|}$ on the vertical axis.

# Hamilton integration and abnormal boundary

Set $h_1=p(X)$ and $h_2=p(Y)$. Hamilton's equations give $$\dot h_1=-\lambda h_2,\qquad \dot h_2=\lambda h_1,
 \qquad \dot\lambda=0.$$ Thus $(h_1,h_2)=(\cos(\phi+\lambda t),\sin(\phi+\lambda t))$; integrating $\dot x=h_1$, $\dot y=h_2$ and $\dot z=(-yh_1+xh_2)/2$ proves the displayed formulas. An abnormal covector annihilates $X,Y$ and, by differentiating these constraints, $[X,Y]$. Since these three vectors span $TH^1$, the covector vanishes, a contradiction.

# First singular and Maxwell times

For initial horizontal norm $r$, direct differentiation in $(r,\phi,\lambda)$ gives, with $s=\lambda t$, $$\det D\operatorname{Exp}_t=
 \frac{r^3t}{\lambda^4}\{2-2\cos s-s\sin s\}.$$ The brace factors as $4\sin(s/2)[\sin(s/2)-(s/2)\cos(s/2)]$. For $0<s<2\pi$ the first factor is positive; if $u=s/2$, the derivative of $\sin u-u\cos u$ is $u\sin u>0$. Hence the first zero is $s=2\pi$. At that phase $x=y=0$ and $z=\operatorname{sgn}(\lambda)\pi/\lambda^2$, independently of $\phi$. The conjugate time is therefore also the first rotational Maxwell time.

\>0

The determinant formula extends continuously to $\lambda=0$ with value $r^3t^5/12$. For $\lambda<0$ its first zero is still $2\pi/|\lambda|$, and the corresponding endpoint has negative $z$.

The expansion $2-2\cos s-s\sin s=s^4/12+O(s^6)$ gives the first assertion. The brace is even in $s$, whereas $(s-\sin s)/(2\lambda^2)$ is odd in $s$; this proves both remaining sign statements. Thus neither a hidden singular zero-momentum face nor a sign choice halves the conjugate time.

# Distance and minimality

The length of a horizontal curve equals the Euclidean length of its $(x,y)$ projection, while $$z=\frac12\int(x\,dy-y\,dx)$$ is signed planar area. Dido's problem says that a minimizing projected curve with fixed endpoint and signed area is a line or circular arc. Before a full turn the sub-full-turn Dido arc is unique; at a full turn its starting tangent is free. Writing its half-angle as $\theta$ yields $$\rho=\frac{2\sin\theta}{\lambda},\qquad
 z=\frac{\theta-\sin\theta\cos\theta}{\lambda^2},\qquad
 t=\frac{2\theta}{\lambda},$$ and hence the theorem. Moreover $$\frac{d}{d\theta}\frac{\theta-\sin\theta\cos\theta}{\sin^2\theta}
 =\frac{2(\sin\theta-\theta\cos\theta)}{\sin^3\theta}>0$$ on $(-\pi,\pi)$, proving angle uniqueness. The isoperimetric inequality for a closed planar curve gives $t^2\ge4\pi|z|$, with equality for a circle, proving the vertical formula and completing the cut-locus argument.

\>1

No geodesic segment with $|\lambda|t<2\pi$ loses global minimality, and every segment with $|\lambda|t>2\pi$ is nonminimizing.

The planar constrained-length Euler equation has constant signed curvature, so every nonstraight minimizer is a circular arc. Strict monotonicity of the implicit-angle map selects exactly one arc with half-angle in $(-\pi,\pi)$ for each nonvertical endpoint. Hence no competitor exists before the limiting full circle. At the full circle the isoperimetric equality gives a minimizing $S^1$ family. Past it, the same endpoint constraints select the unique sub-full-turn Dido arc whose half-angle lies in $(-\pi,\pi)$, so the continued geodesic is longer. This upgrades the visible Maxwell merger to the claimed global cut theorem.

The three endpoint faces fit without an extra normalization: $$\begin{array}{c@{\qquad}c@{\qquad}c}
z=0,\ \rho>0 & \rho>0,\ z\ne0 & \rho=0,\ z\ne0\\
\theta=0 & -\pi<\theta<\pi & \theta\to\operatorname{sgn}(z)\pi\\
d=\rho & d=\rho\theta/\sin\theta & d=2\sqrt{\pi|z|}.
\end{array}$$

# Evidence and claim boundary

The deterministic receipt contains 800 trajectory rows, 64 regular-distance rows, and 12 vertical rows (10,972 numeric cells, independently recounted from an explicit field schema). An implementation sharing no producer code passes 11,139 assertions; 20 symbolic identities, byte replay, and 27/27 repaired-hash hostile mutations also pass. These are regression checks: the global theorem is established by the analytic argument above.

\>1

  Receipt or gate                                        Result
  --------------------------------------- ---------------------
  Trajectory / distance / vertical rows             $800/64/12$
  Independent assertions                        $11{,}139$ PASS
  Symbolic identities                                 $20$ PASS
  Repaired-hash hostile mutations              $27/27$ rejected
  Evidence SHA-256                          `86bbae2b0610…dcaa`

The producer replay is byte-identical. The independent checker imports no producer code, while the symbolic checker derives the decisive identities from the frozen frame. Infinite-dimensional or global conclusions are therefore not inferred from a finite numerical grid.

Complete geodesics provide no periodic-orbit signal: $\lambda=0$ gives lines, while for $\lambda\ne0$ one horizontal period has nonzero vertical drift. Thus the A1 axis is conservatively failed. The theorem status is **PROVABLE AS STATED**. The Route-A tuple is

  ----------------------------------------------
      `(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL,`
   `A4_FORMAL_HINT)`, hence `ROUTE_A_REJECTED`.
  ----------------------------------------------

Route B is not invoked. The claim firewall is `NO_BAD_EULER_OR_ROOT_NUMBER`: no arithmetic local data, Euler factor, root number, automorphy, target divisor, or Hilbert--Pólya operator is claimed.

# Primary source {#primary-source .unnumbered}

B. Gaveau, "Principe de moindre action, propagation de la chaleur et estimées sous elliptiques sur certains groupes nilpotents," *Acta Mathematica* **139** (1977), 95--153. DOI: [10.1007/BF02392235](https://doi.org/10.1007/BF02392235). The citation records classical model lineage; no priority claim is made.
