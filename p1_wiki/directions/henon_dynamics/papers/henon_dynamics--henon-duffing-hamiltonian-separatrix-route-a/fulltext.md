---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-duffing-hamiltonian-separatrix-route-a"
canonical_tex: "henon_dynamics/henon_duffing_hamiltonian_separatrix_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_duffing_hamiltonian_separatrix_route_a/paper/main.pdf"
source_sha256: "1303fe153acbcf2fad7f72d505087d96a603b12fc43aeb4def11b92765d945fe"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Energy Topology, Action, and the Homoclinic Boundary of the Duffing Flow

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_duffing_hamiltonian_separatrix_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_duffing_hamiltonian_separatrix_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_duffing_hamiltonian_separatrix_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_duffing_hamiltonian_separatrix_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We close an all-parameter phase-space atlas for the conservative Duffing oscillator $\dot x=v$, $\dot v=-\delta x-\beta x^3$ with $\beta>0$. The energy levels are classified for both the single-well and double-well regimes, including the two homoclinic loops at the barrier. Turning points are roots of an explicit quadratic in $x^2$; an endpoint-cancelled integral therefore gives the period and action on every regular oval, with the action derivative identity and center, quartic, and saddle limits. The ledger keeps the $\beta=0$ faces separate and treats the continuum of energy ovals as a source Hamiltonian family, not as isolated primitive cycles. Exact symbolic, independent numerical, replay, and hostile-mutation checks accompany the proof.
author:
- HCS Research Program
date: 29 August 2026(revision 2)
title: 'Energy Topology, Action, and the Homoclinic Boundary of the Duffing Flow'
```

## Markdown 正文

suppressoptionalinfo 611

# Model and invariant

Put $$\dot x=v,\qquad \dot v=-\delta x-\beta x^3,
 \qquad H(x,v)=\frac{v^2}{2}+V(x),\quad
 V(x)=\frac{\delta x^2}{2}+\frac{\beta x^4}{4},
 \label{eq:model}$$ where $\beta>0$ and $\delta\in\mathbb R$. The physical time is the common clock. Hamiltonian conservation follows immediately from $H_x\dot x+H_v\dot v=0$. For a regular connected oval with turning points $\ell<r$, define $$T(E)=\sqrt{2}\int_\ell^r\frac{dx}{\sqrt{E-V(x)}},\qquad
 I(E)=\frac1\pi\int_\ell^r\sqrt{2(E-V(x))}\,dx .
 \label{eq:quadrature}$$ The endpoint square roots are integrable; the executable ledger evaluates [\[eq:quadrature\]](#eq:quadrature){reference-type="eqref" reference="eq:quadrature"} after $x=(\ell+r)/2+(r-\ell)\sin\theta/2$.

[\[thm:atlas\]]{#thm:atlas label="thm:atlas"} Let $\beta>0$. If $\delta\geq0$, every $E>0$ is one smooth compact oval around the origin. If $\delta<0$, write $a=\sqrt{-\delta/\beta}$ and $V_{\min}=-\delta^2/(4\beta)$. Then $V_{\min}<E<0$ gives two ovals, $E=0$ gives two homoclinic loops to $(0,0)$, and $E>0$ gives one outer oval. The squared turning points are $$y_\pm=\frac{-\delta\pm\sqrt{\delta^2+4\beta E}}{\beta},\qquad y=x^2 .
 \label{eq:roots}$$ On each regular component, [\[eq:quadrature\]](#eq:quadrature){reference-type="eqref" reference="eq:quadrature"} is finite, $I'(E)=T(E)/(2\pi)$, and the period is positive. For $\delta=-\alpha^2<0$, the separatrices are $$x_h(t)=\pm\frac{\sqrt{2}\,\alpha}{\sqrt\beta}\,\operatorname{sech}(\alpha t),
 \qquad v_h=\dot x_h .
 \label{eq:homoclinic}$$ Moreover $T(E)\to2\pi/\sqrt\delta$ as $E\downarrow0$ when $\delta>0$, $T(E)\,E^{1/4}\beta^{1/4}$ is constant when $\delta=0$, and $T(E)$ diverges logarithmically as a regular energy approaches the saddle level.

The quartic potential is coercive, so regular compact components are the connected components described by the signs of the two roots in [\[eq:roots\]](#eq:roots){reference-type="eqref" reference="eq:roots"}. For $\delta<0$ the identity $$V(x)+\frac{\delta^2}{4\beta}=\frac\beta4\left(x^2+\frac\delta\beta\right)^2$$ locates the two minima and the barrier. Separation of variables gives [\[eq:quadrature\]](#eq:quadrature){reference-type="eqref" reference="eq:quadrature"}; the sine substitution removes endpoint singularities. Differentiating the action on a compact subinterval of regular energies and using the vanishing endpoint integrand gives $I'=T/(2\pi)$. At $\delta=0$, the scaling $x=E^{1/4}\beta^{-1/4}u$ proves the quartic law. The quadratic Taylor expansion at a nondegenerate center gives the center limit. Near the hyperbolic saddle, $E-V(x)$ has a nondegenerate quadratic zero, and comparison with $\int dx/\sqrt{\alpha^2x^2+|E|}$ gives the logarithmic divergence. Finally direct substitution of [\[eq:homoclinic\]](#eq:homoclinic){reference-type="eqref" reference="eq:homoclinic"} into $\ddot x-\alpha^2x+\beta x^3=0$ proves the separatrix formula.

# Linear faces and source boundaries

The origin has linear rates $\pm i\sqrt\delta$ for $\delta>0$ and $\pm\sqrt{-\delta}$ for $\delta<0$; the well equilibria $x=\pm a$ have rates $\pm i\sqrt{-2\delta}$. When $\beta=0$, the positive-$\delta$ face is the harmonic oscillator, the negative-$\delta$ face is inverted and has no compact positive-energy ovals, and $(\beta,\delta)=(0,0)$ is free motion. These lower-dimensional models are not silently folded into the quartic theorem. The two inner components and the outer component are separated in the ledger, so a period near the barrier cannot be mistaken for a center period.

\>0

# Action coordinates and evidence

On each regular component the action is strictly increasing because $I'(E)>0$; it is therefore a valid local action coordinate, while the homoclinic level is its logarithmic endpoint. The certificate contains five parameter cases and twenty energy rows, including both double-well components and the pure-quartic scaling control. A producer-independent checker makes 790 assertions, and SymPy verifies ten identities (conservation, factorization, turning polynomial, the profile residual, linear rates, and the action integrand). Clean replay is byte-for-byte and the hostile suite rejects twenty repaired-hash/schema mutations plus one stale-hash mutation (21/21 hostile checks).

\>1

# Route-A boundary

The Duffing flow is a natural one-degree-of-freedom Hamiltonian system, but its recurrent ovals are indexed by a continuum of real energies. Thus the source theorem supplies no intrinsic isolated primitive-orbit owner, logarithmic prime clock, or target divisor. The strict tuple is $$(\texttt{A0\_FAIL,A1\_WEAK,A2\_FAIL,A3\_FAIL,A4\_FORMAL\_HINT}),$$ with `ROUTE_A_REJECTED` and `route_b_invocation_allowed=false`. The action variable and a possible semiclassical lift are candidate-local formal hints only. No arithmetic target is inferred from the exact elliptic/quadrature structure.

# Source note and declarations {#source-note-and-declarations .unnumbered}

The phase-plane terminology follows Guckenheimer and Holmes [@GH1983]; period-function conventions follow Chicone [@Chicone2006]. The name Duffing is historical [@Duffing1918]; no priority claim is made. No prime or zero table, local arithmetic datum, Euler factor, root number, automorphy object, target functional equation, Hilbert--Pólya operator or Route-B input is used. Generative tools assisted drafting and code generation; the displayed claims are tied to the artifact chain. This is not external peer review. Scope literal: `NO_BAD_EULER_OR_ROOT_NUMBER`.

9 J. Guckenheimer and P. Holmes, *Nonlinear Oscillations, Dynamical Systems, and Bifurcations of Vector Fields*, Springer, 1983. DOI: 10.1007/978-1-4612-1140-2. C. Chicone, *Ordinary Differential Equations with Applications*, 2nd ed., Springer, 2006. DOI: 10.1007/0-387-35794-7. G. Duffing, *Erzwungene Schwingungen bei veränderlicher Eigenfrequenz*, Vieweg, Braunschweig, 1918.
