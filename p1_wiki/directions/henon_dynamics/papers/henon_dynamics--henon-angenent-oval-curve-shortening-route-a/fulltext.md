---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-angenent-oval-curve-shortening-route-a"
canonical_tex: "henon_dynamics/henon_angenent_oval_curve_shortening_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_angenent_oval_curve_shortening_route_a/paper/main.pdf"
source_sha256: "7bf8de00c1f01710dd78b7a3d04e91bc04a7f739ab9a8148eb5b06ed2c68b34c"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The Angenent Oval under Curve Shortening: Exact Ancient Geometry and Two Grim-Reaper Ends

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_angenent_oval_curve_shortening_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_angenent_oval_curve_shortening_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_angenent_oval_curve_shortening_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_angenent_oval_curve_shortening_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the central component of $\cos x=e^t\cosh y$ in $|x|<\pi/2$, $t<0$, we give a convention-explicit proof of curve shortening, smooth embedded strict convexity, and exact curvature extrema. \>0 We close its width, height, area and elliptic length, identify the exact arrival-time foliation of the punctured strip, and prove both round extinction and the translated upper/lower Grim-Reaper limits. \>1 Independent symbolic, quadrature, replay and hostile-mutation evidence audits the formulas while preserving their classical ownership and strict Route-A boundary.
author:
- 'Route-A source-local certificate HCS-C314'
date: 3 September 2026
title: |
  The Angenent Oval under Curve Shortening:\
  Exact Ancient Geometry and Two Grim-Reaper Ends
```

## Markdown 正文

trailerid \[\<C3142026090300000000000000000000\>\<C3142026090300000000000000000000\>\]

# Exact ancient solution and curvature

We use the convention that a convex curve has positive curvature $\kappa$ with respect to its outward normal $n$, and curve shortening has outward normal velocity $V_n=-\kappa$. Put $r=e^t\in(0,1)$ and $$F(x,y,t)=\cos x-r\cosh y,\qquad
 \Gamma_t=\{F=0,\ |x|<\pi/2\}.$$

[\[thm:core\]]{#thm:core label="thm:core"} For every $t<0$, the central component $\Gamma_t$ is a smooth embedded strictly convex closed curve. It evolves by $V_n=-\kappa$, where $$\label{eq:kappa}
 \kappa(x,y,t)=\frac{\cos x}{\sqrt{1-e^{2t}}},\qquad
 \frac{e^t}{\sqrt{1-e^{2t}}}\leq\kappa\leq
 \frac1{\sqrt{1-e^{2t}}}.$$ It is ancient on $(-\infty,0)$ and contracts to the origin as $t\uparrow0$.

The central component consists of the two graphs $$y=\pm\operatorname{arcosh}(r^{-1}\cos x),\qquad |x|\leq\arccos r.$$ On this level, $$\label{eq:cancellation}
 |\nabla F|^2=\sin^2x+r^2\sinh^2y=1-r^2>0,
 \qquad D^2F=-\cos x\,I.$$ Thus the level is smooth and compact. For $n=-\nabla F/|\nabla F|$, the implicit curvature formula and [\[eq:cancellation\]](#eq:cancellation){reference-type="eqref" reference="eq:cancellation"} give [\[eq:kappa\]](#eq:kappa){reference-type="eqref" reference="eq:kappa"}, which is positive because $r\leq\cos x\leq1$. Differentiating $F=0$ along a moving point yields $V_n=F_t/|\nabla F|=-\cos x/\sqrt{1-r^2}=-\kappa$. The displayed graphs shrink to $(0,0)$ as $r\uparrow1$ and exist for every $r>0$, proving the temporal statements and the sharp extrema. The unrestricted zero set of $F$ is the disjoint union $\bigsqcup_{k\in\mathbb Z}(\Gamma_t+(2\pi k,0))$; it is not one compact curve.

\>0

# Global geometry, arrival time, and two asymptotic regimes

Write $K(k)=\int_0^{\pi/2}(1-k^2\sin^2\phi)^{-1/2}\,d\phi$; here $k$ is the elliptic *modulus*.

[\[thm:global\]]{#thm:global label="thm:global"} The horizontal width $W$, vertical height $H$, enclosed area $A$ and length $L$ are $$\begin{aligned}
 W(t)&=2\arccos(e^t),& H(t)&=2\operatorname{arcosh}(e^{-t}),\label{eq:spans}\\
 A(t)&=-2\pi t,&
 L(t)&=4\sqrt{1-e^{2t}}\,
 K\!\left(\sqrt{1-e^{2t}}\right).\label{eq:area-length}\end{aligned}$$ The negative-time curves foliate $(-\pi/2,\pi/2)\times\mathbb R\setminus\{(0,0)\}$ exactly once. Their arrival time $$\label{eq:arrival}
 T(x,y)=\log\cos x-\log\cosh y$$ satisfies, away from the origin, $$\label{eq:arrival-pde}
 -|\nabla T|\,\operatorname{div}\!\left(\frac{\nabla T}{|\nabla T|}\right)=1.$$ Moreover, $$(-2t)^{-1/2}\Gamma_t\longrightarrow S^1
 \quad\hbox{smoothly as }t\uparrow0.$$ If $y_+(x,t)=\operatorname{arcosh}(e^{-t}\cos x)$ and $h(t)=\operatorname{arcosh}(e^{-t})$, then $$\label{eq:grim}
 y_+(x,t)-h(t)\longrightarrow\log\cos x$$ smoothly on compact subsets of $(-\pi/2,\pi/2)$ as $t\to-\infty$; the lower tip has the reflected limit.

The extrema of the two graphs give [\[eq:spans\]](#eq:spans){reference-type="eqref" reference="eq:spans"}. On the upper graph, $$y_x=-\frac{\sin x}{\sqrt{\cos^2x-r^2}},\qquad
 ds=\frac{\sqrt{1-r^2}}{\sqrt{\cos^2x-r^2}}\,dx.$$ The substitution $\sin x=\sqrt{1-r^2}\sin\phi$, followed by the two graph and two half-curve symmetries, proves the length formula. Directly differentiating the area integral (the endpoint value is zero) gives $$A'(t)=-4\int_0^{\arccos r}
 \frac{\cos x}{\sqrt{\cos^2x-r^2}}\,dx=-2\pi.$$ Since $A(t)\to0$ as $t\uparrow0$, the area formula follows.

On the open strip, $T\leq0$, with equality only at the origin, and $T=t$ is equivalent to the oval equation. This proves the precise punctured-strip foliation. Setting $a=-\tan x$, $b=-\tanh y$ in the divergence of $(a,b)/\sqrt{a^2+b^2}$ reduces the left side of [\[eq:arrival-pde\]](#eq:arrival-pde){reference-type="eqref" reference="eq:arrival-pde"} to $$\frac{\sec^2x\,\tanh^2y+\operatorname{sech}^2y\,\tan^2x}
 {\tan^2x+\tanh^2y}=1.$$

In tangent-angle coordinates (up to an angle shift), $$\label{eq:pressure}
 \kappa^2(\theta,t)=\frac1{1-e^{2t}}-\sin^2\theta.$$ After scaling, $(-2t)\kappa^2\to1$ with every angular derivative. Symmetry fixes translation, so the fundamental theorem for strictly convex plane curves gives the smooth circular limit. Finally, $\operatorname{arcosh}z=\log(2z)+O(z^{-2})$ with differentiated uniformity away from the strip edges. Apply it to $z=e^{-t}\cos x$ and to $z=e^{-t}$ to obtain [\[eq:grim\]](#eq:grim){reference-type="eqref" reference="eq:grim"}; reflection gives the lower statement.

\>1

# Evidence, collisions, and Route-A boundary

Twenty rational $r$ rows, 220 curve points, eight extinction scales and 35 translated-tip samples give 2,639 audited evidence leaves. An independent checker performs 2,632 checks; SymPy closes nine identity groups; isolated replay is byte exact; and 44 repaired-hash, stale-hash, strict-parser and optimized-Python attacks must fail. Finite rows regress formulas, while Theorems [\[thm:core\]](#thm:core){reference-type="ref" reference="thm:core"}--[\[thm:global\]](#thm:global){reference-type="ref" reference="thm:global"} are analytic and untruncated.

C281 evolves homogeneous product metrics by Ricci flow, C299 is a radial Navier--Stokes vortex, and C304 is a periodic linear Cahn--Hilliard semigroup. C304's idea report reserved the noncompact Grim translator but did not package it. None owns a compact ancient curve, its exact strip arrival time, elliptic length, and two-tip asymptotics.

Under `NO_BAD_EULER_OR_ROOT_NUMBER`, the strict tuple is $$(\mathrm{A0\_FAIL},\mathrm{A1\_FAIL},\mathrm{A2\_FAIL},
  \mathrm{A3\_FAIL},\mathrm{A4\_FAIL}).$$ The continuous geometric data have no prime owner or logarithmic clock; strict shrinking supplies no primitive periodic ledger; and no dynamical determinant, Weil compression, or natural unitary quantization is defined. Route A is rejected and Route B remains locked. No target local data, Euler factors, root number, automorphy, divisor/counting law, functional equation, zero match, or Hilbert--Pólya operator is asserted.

#### AI use.

A generative language model assisted drafting and code scaffolding. The displayed proofs, independent reconstruction, hostile tests and deterministic artifacts define the audit record.

# Source lineage {#source-lineage .unnumbered}

9 S. B. Angenent, "Shrinking Doughnuts," in *Nonlinear Diffusion Equations and Their Equilibrium States, 3*, Birkhäuser, 1992, 21--38. DOI: [10.1007/978-1-4612-0393-3\_2](https://doi.org/10.1007/978-1-4612-0393-3_2). P. Daskalopoulos, R. Hamilton, and N. Šešum, "Classification of compact ancient solutions to the curve shortening flow," arXiv:[0806.1757](https://arxiv.org/abs/0806.1757). T. Bourni, M. Langford, and G. Tinaglia, "Convex ancient solutions to curve shortening flow," arXiv:[1903.02022](https://arxiv.org/abs/1903.02022).
