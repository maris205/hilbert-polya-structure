---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-rayleigh-spherical-cavity-collapse-route-a"
canonical_tex: "henon_dynamics/henon_rayleigh_spherical_cavity_collapse_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_rayleigh_spherical_cavity_collapse_route_a/paper/main.pdf"
source_sha256: "5d3cebced53a07e71480b4ead6c9adad3c8ffcf7bc9aa12ec7a2d70b6cdddb6b"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Rayleigh Spherical-Cavity Collapse: Exact Beta Clock and the Terminal $2/5$ Singularity

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_rayleigh_spherical_cavity_collapse_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_rayleigh_spherical_cavity_collapse_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_rayleigh_spherical_cavity_collapse_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_rayleigh_spherical_cavity_collapse_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We give a source-local all-parameter atlas for the inviscid spherical-cavity Rayleigh equation with constant pressure difference. A weighted first integral closes the positive, zero, and negative pressure branches. On the physical collapse branch the lifetime is an exact Beta constant, while the terminal radius, wall speed, wall acceleration, volume, finite liquid kinetic energy, and $L^p$ thresholds follow from one endpoint expansion. The zero-radius face is kept outside the classical phase space. This is a hydrodynamic theorem and reproducibility certificate; it is not an arithmetic determinant or a Hilbert--Pólya construction.
author:
- HCS Research Program
date: 28 August 2026(revision 2)
title: 'Rayleigh Spherical-Cavity Collapse: Exact Beta Clock and the Terminal $2/5$ Singularity'
```

## Markdown 正文

suppressoptionalinfo 611

# Model and exact first integral

Let $R(t)>0$ be the radius of an empty spherical cavity in an ideal incompressible liquid. We freeze $$R\ddot R+\frac32\dot R^2=-\frac{\Pi}{\rho},
 \qquad R(0)=R_0>0,\quad \dot R(0)=0,
 \tag{1}$$ where $\rho>0$ and $\Pi=P_\infty-P_v$ is constant. The physical collapse sign is $\Pi>0$; the other signs are retained as mathematical controls. Multiplication by $2R^2\dot R$ gives $$R^3\dot R^2+\frac{2\Pi}{3\rho}R^3
 =\frac{2\Pi}{3\rho}R_0^3. \tag{2}$$

[\[thm:atlas\]]{#thm:atlas label="thm:atlas"} For $\Pi>0$, put $a=\sqrt{2\Pi/(3\rho)}$. The positive-radius forward solution is strictly decreasing until its finite collapse time $$T_c=\frac{R_0}{a}\int_0^1\frac{x^{3/2}}{\sqrt{1-x^3}}\,\mathrm dx
 =\frac{R_0}{3a}B\!\left(\frac56,\frac12\right)
 =0.914681356501962\ldots R_0\sqrt{\frac{\rho}{\Pi}}. \tag{3}$$ Writing $\delta=T_c-t$, $$R=C\delta^{2/5}(1+O(\delta^{6/5})),\quad
 \dot R=-\frac25C\delta^{-3/5}(1+O(\delta^{6/5})),\quad
 \ddot R=-\frac6{25}C\delta^{-8/5}(1+O(\delta^{6/5})),
 \tag{4}$$ where $C=R_0^{3/5}(5a/2)^{2/5}$. For $\Pi=0$, $R(t)=R_0$. For $\Pi<0$, the solution is strictly increasing, has no finite singular time, and $R(t)\sim\sqrt{2|\Pi|/(3\rho)}\,t$. Moreover, with $V=(4\pi/3)R^3$, $$K=2\pi\rho R^3\dot R^2=\frac{4\pi}{3}\Pi(R_0^3-R^3),\quad
 U=\frac{4\pi}{3}\Pi R^3,\quad E=K+U=\frac{4\pi}{3}\Pi R_0^3, \tag{5}$$ and near collapse $V\sim(4\pi/3)C^3\delta^{6/5}$. Finally, $$\dot R\in L^p(T_c-\varepsilon,T_c)\ \Longleftrightarrow\ p<\frac53,
 \qquad
 \ddot R\in L^p(T_c-\varepsilon,T_c)\ \Longleftrightarrow\ p<\frac58.
 \tag{6}$$

Equation (2) follows directly from (1). On the collapse branch its negative square-root sign gives $\dot R=-a\sqrt{(R_0/R)^3-1}$, and separation gives (3). The substitution $y=x^3$ produces $\frac13B(5/6,1/2)$. At the endpoint, $$\int_0^x\frac{u^{3/2}}{\sqrt{1-u^3}}\,\mathrm du
 =\frac25x^{5/2}+\frac1{11}x^{11/2}+O(x^{17/2}),$$ which inverts to (4). The same powers prove (6). The positive and negative signs in (2) give the monotonicity and the expansion asymptotic. Substitution of (2) into the kinetic term proves (5) and the volume statement.

# Lagrangian and geometric boundary

The equation is Euler--Lagrange on $R>0$ for $$L_{\rm phys}=2\pi\rho R^3\dot R^2-\frac{4\pi}{3}\Pi R^3. \tag{7}$$ Indeed its residual is $4\pi\rho R^2[R\ddot R+(3/2)\dot R^2+\Pi/\rho]$. Thus the wall speed diverges while the liquid kinetic energy tends to the finite value $4\pi\Pi R_0^3/3$, and the volume flux tends to zero. The dimensionless profile is an inverse incomplete-Beta function; this notation is exact but is not an elementary closed form. It is source-local explicit solvability only: the source Beta clock is not target continuation/divisor/counting law and is not an A3 analytic-structure match. The face $R_0=0$ is not a positive-radius initial state, so no continuation through $R=0$ is claimed.

\>0

# Boundary controls and reproducible ledger

The certificate samples five collapse rows, two equilibria, three expansion rows, and three zero-radius controls. The producer uses endpoint-stable quadratures; an independent checker uses hypergeometric primitives. SymPy verifies the first integral, Beta substitution, Euler--Lagrange residual, Puiseux coefficients, volume/energy identities, and both integrability thresholds. A byte replay and repaired/stale-hash mutation suite are part of the release contract.

\>1

# Route-A scope and audit

The strict tuple is

(A0\_FAIL, A1\_FAIL, A2\_FAIL, A3\_FAIL, A4\_FORMAL\_HINT).

Thus `overall=ROUTE_A_REJECTED` and `route_b_invocation_allowed=false`. The monotone collapse trajectory has no primitive periodic-orbit owner, arithmetic clock, target determinant, or same-clock self-adjoint lift. The incomplete-Beta branch and terminal Puiseux law are source-local explicit solvability only; the source Beta clock is not target continuation/divisor/counting law and is not an A3 target match. The registered scope is

NO\_BAD\_EULER\_OR\_ROOT\_NUMBER

No prime table, zero table, local factor, root number, automorphy statement, functional equation, or Hilbert--Pólya operator is introduced.

# Source note {#source-note .unnumbered}

The ideal empty-cavity equation originates with Rayleigh [@rayleigh1917]. The bubble-dynamics context is reviewed by Plesset and Prosperetti [@plesset1977]; the terminal $2/5$ singularity and physical correction mechanisms are discussed by Brenner, Hilgenfeldt, and Lohse [@brenner2002]. The dimensionless profile and collapse approximation are recorded by Obreschkow, Bruderer, and Farhat [@obreschkow2012]. These references are source metadata, not a priority or arithmetic claim.

9 Lord Rayleigh, "VIII. On the pressure developed in a liquid during the collapse of a spherical cavity," *The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science* 34(200), 94--98 (1917). DOI: [10.1080/14786440808635681](https://doi.org/10.1080/14786440808635681). M. S. Plesset and A. Prosperetti, "Bubble Dynamics and Cavitation," *Annual Review of Fluid Mechanics* 9, 145--185 (1977). DOI: [10.1146/annurev.fl.09.010177.001045](https://doi.org/10.1146/annurev.fl.09.010177.001045). M. P. Brenner, S. Hilgenfeldt, and D. Lohse, "Single-bubble sonoluminescence," *Reviews of Modern Physics* 74, 425--484 (2002). DOI: [10.1103/RevModPhys.74.425](https://doi.org/10.1103/RevModPhys.74.425). D. Obreschkow, M. Bruderer, and M. Farhat, "Analytical approximations for the collapse of an empty spherical bubble," *Physical Review E* 85, 066303 (2012). DOI: [10.1103/PhysRevE.85.066303](https://doi.org/10.1103/PhysRevE.85.066303).

# Declarations {#declarations .unnumbered}

**Scope.** `NO_BAD_EULER_OR_ROOT_NUMBER`; no target arithmetic or operator claim. **Data and code.** The theorem, ledger, independent checks, and build instructions are released with HCS-C219. **AI-use disclosure.** Generative tools assisted drafting and code generation; the internal artifact chain checked the displayed claims and metadata. This is not external peer review.
