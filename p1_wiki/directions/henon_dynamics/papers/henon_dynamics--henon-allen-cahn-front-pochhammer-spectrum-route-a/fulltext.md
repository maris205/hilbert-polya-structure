---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-allen-cahn-front-pochhammer-spectrum-route-a"
canonical_tex: "henon_dynamics/henon_allen_cahn_front_pochhammer_spectrum_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_allen_cahn_front_pochhammer_spectrum_route_a/paper/main.pdf"
source_sha256: "214f53daeb1ea0dfc7b8a4e07ff360f716171c6240c1a75935853124870e6493"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Equal-Well Allen--Cahn Fronts: Translation Uniqueness and a\newline Pöschl--Teller Spectral Atlas

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_allen_cahn_front_pochhammer_spectrum_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_allen_cahn_front_pochhammer_spectrum_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_allen_cahn_front_pochhammer_spectrum_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_allen_cahn_front_pochhammer_spectrum_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We close a source-local theorem for the one-dimensional equal-well Allen--Cahn reaction--diffusion equation. For $u_t=u_{xx}+\varepsilon^{-2}(u-u^3)$, every monotone heteroclinic from $-1$ to $+1$ is a translate of $\tanh(\xi/(\sqrt2\varepsilon))$, and the equal-well balance forces its travelling speed to be zero. The gradient-flow energy dissipates exactly, with interfacial energy $2\sqrt2/(3\varepsilon)$. Linearization is the factorized Pöschl--Teller operator: translation is the simple zero mode, the shape mode has eigenvalue $-3/(2\varepsilon^2)$, and the essential spectrum is $(-\infty,-2/\varepsilon^2]$. Singular scaling faces are stated explicitly. The front is heteroclinic, not a primitive periodic orbit, so this is a rigorous Route-A negative result rather than an arithmetic or Hilbert--Pólya claim.
author:
- HCS Research Program
date: 29 August 2026(revision 2)
title: 'Equal-Well Allen--Cahn Fronts: Translation Uniqueness and aPöschl--Teller Spectral Atlas'
```

## Markdown 正文

suppressoptionalinfo 611

# Frozen equation and the heteroclinic

We use the scaled family $$u_t=u_{xx}+\varepsilon^{-2}(u-u^3),\qquad \varepsilon>0,
 \label{eq:pde}$$ whose $\varepsilon=1$ member is the requested Allen--Cahn equation. Put $W(q)=(1-q^2)^2/4$; then [\[eq:pde\]](#eq:pde){reference-type="eqref" reference="eq:pde"} is the $L^2$ gradient flow of $$E_\varepsilon[u]=\int_{\mathbb R}\left(\frac12u_x^2+\varepsilon^{-2}W(u)\right)\,\mathrm dx.
 \label{eq:energy}$$ For a travelling ansatz $u(x,t)=U(\xi)$, $\xi=x-ct$, the profile equation is $$U''+cU'+\varepsilon^{-2}(U-U^3)=0,qquad
 U(-\infty)=-1,\quad U(+\infty)=1.
 \label{eq:tw}$$

[\[thm:front\]]{#thm:front label="thm:front"} Every nonconstant monotone $C^2$ solution of [\[eq:tw\]](#eq:tw){reference-type="eqref" reference="eq:tw"} has $c=0$ and, for some $\xi_0\in\mathbb R$, $$U(\xi)=U_\varepsilon(\xi-\xi_0):= anh\!\left(\frac{\xi-\xi_0}{\sqrt2\varepsilon}\right).
 \label{eq:tanh}$$ The reverse orientation is $-U_\varepsilon$. For the increasing orientation, $$\frac12(U_\varepsilon')^2=\varepsilon^{-2}W(U_\varepsilon),\qquad
 \int_{\mathbb R}(U_\varepsilon')^2\,\mathrm d\xi
 =E_\varepsilon[U_\varepsilon]=\frac{2\sqrt2}{3\varepsilon}.
 \label{eq:equip}$$

Multiply [\[eq:tw\]](#eq:tw){reference-type="eqref" reference="eq:tw"} by $U'$ and integrate from $-\infty$ to $+\infty$. The endpoint derivatives and $W(\pm1)$ vanish, giving $$c\int_{\mathbb R}(U')^2\,\mathrm d\xi=0.$$ Since a nonconstant front has positive integral, $c=0$. A first integral is then $(U')^2/2=\varepsilon^{-2}W(U)$. Monotonicity selects the positive square root, and separation of variables gives [\[eq:tanh\]](#eq:tanh){reference-type="eqref" reference="eq:tanh"} with one free translation. The identity $U_\varepsilon'=(\sqrt2\varepsilon)^{-1}\operatorname{sech}^2 y$, $y=(\xi-\xi_0)/(\sqrt2\varepsilon)$, and $\int_{\mathbb R}\operatorname{sech}^4y\,\mathrm dy=4/3$ prove [\[eq:equip\]](#eq:equip){reference-type="eqref" reference="eq:equip"}.

\>0

# Dissipation and the exact interface ledger

For smooth solutions with finite relative energy (subtracting the two pure well constants outside a bounded transition region), differentiation of [\[eq:energy\]](#eq:energy){reference-type="eqref" reference="eq:energy"} and integration by parts gives $$\frac{\,\mathrm d}{\,\mathrm dt}E_\varepsilon[u(t)]
 =\int_{\mathbb R}(-u_{xx}-\varepsilon^{-2}(u-u^3))u_t\,\mathrm dx
 =-\int_{\mathbb R}u_t^2\,\mathrm dx\leq0.
 \label{eq:dissipation}$$ Equality holds only for a stationary solution. Along the front, the equipartition in [\[eq:equip\]](#eq:equip){reference-type="eqref" reference="eq:equip"} splits the surface energy equally between gradient and potential terms. Fixing the zero crossing $U(\xi_0)=0$ removes the sole translation freedom, so the monotone profile is unique under that phase condition. This is an energy statement, not a claim of a global attractor or a quantitative nonlinear convergence rate.

The speed identity also explains why adding a nonzero $c$ by hand would change the model: equal wells have equal potential values, so a dissipative front cannot carry a net energy drop. A tilted potential can select a moving front, but it is not silently substituted for [\[eq:pde\]](#eq:pde){reference-type="eqref" reference="eq:pde"}.

\>1

# Pöschl--Teller linearization

Write $u=U_\varepsilon+v$ and $y=\xi/(\sqrt2\varepsilon)$. The linearized generator is $$L_\varepsilon=\partial_\xi^2+\varepsilon^{-2}(1-3U_\varepsilon^2)
 =\frac1{2\varepsilon^2}M,\qquad
 M=\partial_y^2-4+6\operatorname{sech}^2y.
 \label{eq:lin}$$ Its positive Schrödinger partner has the exact factorization $$-M=B^*B,\qquad B=\partial_y+2\tanh y,
 \qquad B^*=-\partial_y+2\tanh y.
 \label{eq:factor}$$

[\[prop:spectrum\]]{#prop:spectrum label="prop:spectrum"} On $L^2(\mathbb R)$ with domain $H^2(\mathbb R)$, $$\begin{aligned}
 \sigma_{\mathrm{disc}}(L_\varepsilon)&=\left\{0,-\frac3{2\varepsilon^2}\right\},
 &\ker L_\varepsilon&=\operatorname{span}\{U_\varepsilon'\},
 \label{eq:disc}\\
 \sigma_{\mathrm{ess}}(L_\varepsilon)&=\left(-\infty,-\frac2{\varepsilon^2}\right].
 \label{eq:ess}\end{aligned}$$ The second bound state is $\phi_1(y)=\operatorname{sech}y\tanh y$; the translation mode is $\phi_0(y)=\operatorname{sech}^2y$.

Direct differentiation gives $M\phi_0=0$ and $M\phi_1=-3\phi_1$. The factorization [\[eq:factor\]](#eq:factor){reference-type="eqref" reference="eq:factor"} makes the zero mode nonnegative for $-M$; $Bf=0$ has exactly the $L^2$ solution $f\propto\operatorname{sech}^2y$, proving simplicity. The standard Pöschl--Teller factorization chain (or the one-dimensional Sturm oscillation count) places the one-node $\phi_1$ as the second and last bound state. Since $6\operatorname{sech}^2y\to0$, Weyl's theorem compares $M$ with $\partial_y^2-4$, whose spectrum is $(-\infty,-4]$; rescaling by $1/(2\varepsilon^2)$ gives [\[eq:ess\]](#eq:ess){reference-type="eqref" reference="eq:ess"}.

# Singular faces and Route-A boundary

As $\varepsilon\downarrow0$, the width $\sqrt2\varepsilon$ collapses while the surface energy and the spectral scales diverge; this is a sharp-interface scaling, not a finite-width limiting eigenproblem. As $\varepsilon\to\infty$, reaction, the essential edge, and the discrete gap all collapse to zero and the front leaves every fixed compact scale. Setting the reaction coefficient to zero gives the linear heat equation and removes the heteroclinic ODE; setting dimensional diffusivity to zero removes the second derivative and likewise does not define a smooth tanh front. Equal wells exclude every nonzero-speed front in this model.

The object has a physical PDE clock but no primitive periodic orbit or cross-period repetition law. Therefore the strict Route-A record is

(A0\_FAIL, A1\_FAIL, A2\_FAIL, A3\_FAIL, A4\_FORMAL\_HINT),

with `overall=ROUTE_A_REJECTED` and `route_b_invocation_allowed=false`. The scope lock is

NO\_BAD\_EULER\_OR\_ROOT\_NUMBER.

No target prime or zero table, Euler factor, root number, automorphy statement, functional equation, or Hilbert--Pólya operator is introduced.

# Source note {#source-note .unnumbered}

The phase-field context is recorded by Allen and Cahn [@allen]; the travelling-front convergence context is recorded by Fife and McLeod [@fife]. The formulas, spectrum, and boundaries above are re-derived in this artifact; the references are contextual and do not enlarge the claim boundary.

9 S. M. Allen and J. W. Cahn, A microscopic theory for antiphase boundary motion and its application to antiphase domain coarsening, *Acta Metallurgica* 27(6), 1085--1095 (1979). DOI: [10.1016/0001-6160(79)90196-2](https://doi.org/10.1016/0001-6160(79)90196-2). P. C. Fife and J. B. McLeod, The approach of solutions of nonlinear diffusion equations to travelling front solutions, *Archive for Rational Mechanics and Analysis* 65(4), 335--361 (1977). DOI: [10.1007/BF00250432](https://doi.org/10.1007/BF00250432).

# Declarations {#declarations .unnumbered}

**Scope.** `NO_BAD_EULER_OR_ROOT_NUMBER`; no target arithmetic, periodic-orbit, or operator claim. **Data and code.** The exact front, energy ledger, independent checks, and build instructions are released with HCS-C231. **AI-use disclosure.** Generative tools assisted drafting and code generation; the internal artifact chain checked displayed claims and metadata. This is not external peer review.
