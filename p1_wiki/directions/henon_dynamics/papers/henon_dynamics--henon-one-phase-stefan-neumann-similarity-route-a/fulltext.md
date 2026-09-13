---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-one-phase-stefan-neumann-similarity-route-a"
canonical_tex: "henon_dynamics/henon_one_phase_stefan_neumann_similarity_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_one_phase_stefan_neumann_similarity_route_a/paper/main.pdf"
source_sha256: "7e34aa783708d48f82c9a6d87f57f45b8f8914fa97c7bf85b84c992406876b95"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# The One-Phase Stefan Problem: A Closed Neumann Root, Lambert-W Endpoints, and an Exact Energy Ledger

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_one_phase_stefan_neumann_similarity_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_one_phase_stefan_neumann_similarity_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_one_phase_stefan_neumann_similarity_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_one_phase_stefan_neumann_similarity_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We give a source-local theorem for the dimensionless one-phase Stefan problem. The Neumann similarity ansatz reduces the moving boundary to the strictly increasing equation $F(\lambda)=\sqrt\pi\lambda e^{\lambda^2}\operatorname{erf}\lambda=\mathrm{Ste}$. This proves a unique positive root, supplies a five-term small-$\mathrm{Ste}$ inverse series and a two-sided large-$\mathrm{Ste}$ Lambert-$W$ enclosure, and closes the wall/interface flux partition. Integrating the heat equation over the moving interval gives an exact sensible-plus-latent energy ledger. Zero superheat, zero diffusivity, and zero latent heat are labelled singular rescalings. The result is hydrodynamic/free-boundary analysis, not an arithmetic determinant or a Hilbert--Pólya construction.
author:
- HCS Research Program
date: 29 August 2026(revision 2)
title: 'The One-Phase Stefan Problem: A Closed Neumann Root, Lambert-W Endpoints, and an Exact Energy Ledger'
```

## Markdown 正文

suppressoptionalinfo 611

# Frozen model and similarity reduction

We scale the wall superheat, melting temperature, and thermal diffusivity to one. The liquid occupies $0<x<s(t)$ and satisfies $$u_t=u_{xx},\qquad u(0,t)=1,\qquad u(s(t),t)=0,
 \qquad \beta s'(t)=-u_x(s(t)^-,t),\qquad s(0)=0,
 \label{eq:model}$$ where $\beta=\mathrm{Ste}^{-1}>0$ is the inverse Stefan number. With $\eta=x/(2\sqrt t)$, the Neumann form is $$s(t)=2\lambda\sqrt t,\qquad
 u(x,t)=1-\frac{\operatorname{erf}(\eta)}{\operatorname{erf}(\lambda)}.
 \label{eq:profile}$$ The interface derivative is $-u_x(s(t)^-,t)=e^{-\lambda^2}/(\sqrt{\pi t}\operatorname{erf}\lambda)$. Consequently the Stefan condition is equivalent to $$F(\lambda):=\sqrt\pi\lambda e^{\lambda^2}\operatorname{erf}\lambda=\mathrm{Ste}.
 \label{eq:root}$$

[\[thm:main\]]{#thm:main label="thm:main"} For every $\mathrm{Ste}>0$, equation [\[eq:root\]](#eq:root){reference-type="eqref" reference="eq:root"} has exactly one $\lambda>0$. Indeed, $F(0)=0$, $F(\lambda)\to\infty$, and $$F'(\lambda)=\sqrt\pi e^{\lambda^2}\operatorname{erf}\lambda(1+2\lambda^2)+2\lambda>0.
 \label{eq:derivative}$$ The corresponding profile [\[eq:profile\]](#eq:profile){reference-type="eqref" reference="eq:profile"} solves [\[eq:model\]](#eq:model){reference-type="eqref" reference="eq:model"} for $t>0$. Writing $z=\mathrm{Ste}$, its small-$z$ inverse is $$\lambda^2=\frac z2-\frac{z^2}{6}+\frac{7z^3}{90}-\frac{79z^4}{1890}
 +\frac{689z^5}{28350}+O(z^6),
 \label{eq:small}$$ and, for $z>1$, $$\frac12W\!\left(\frac{2z^2}{\pi}\right)<\lambda^2<
 \frac12W\!\left(\frac{2(z+1)^2}{\pi}\right).
 \label{eq:large}$$ Thus $\lambda^2\sim\tfrac12W(2z^2/\pi)$ as $z\to\infty$.

Substitution of [\[eq:profile\]](#eq:profile){reference-type="eqref" reference="eq:profile"} into the heat equation uses $\frac{\,\mathrm d}{\,\mathrm d\eta}\operatorname{erf}\eta=2e^{-\eta^2}/\sqrt\pi$; the two Dirichlet values are immediate. Differentiating $F$ gives [\[eq:derivative\]](#eq:derivative){reference-type="eqref" reference="eq:derivative"}, while its endpoint limits follow from the standard limits of $\operatorname{erf}$. Expanding $$F(\sqrt x)=2x+\frac43x^2+\frac8{15}x^3+\frac{16}{105}x^4
 +\frac{32}{945}x^5+O(x^6)$$ and formal reversion gives [\[eq:small\]](#eq:small){reference-type="eqref" reference="eq:small"}. Finally, for $\lambda>0$, $0<\operatorname{erfc}\lambda<e^{-\lambda^2}/(\sqrt\pi\lambda)$, so $$z<\sqrt{\pi\lambda^2}e^{\lambda^2}<z+1.$$ The function $x\mapsto\sqrt{\pi x}e^x$ is increasing, and inversion with the principal Lambert branch proves [\[eq:large\]](#eq:large){reference-type="eqref" reference="eq:large"}.

\>0

# Flux partition and the moving-domain energy identity

The wall and interface fluxes have a common $t^{-1/2}$ singularity: $$J_{\rm wall}(t)=-u_x(0,t)=\frac{1}{\sqrt{\pi t}\operatorname{erf}\lambda},
 \qquad
 J_{\rm int}(t)=-u_x(s(t)^-,t)=e^{-\lambda^2}J_{\rm wall}(t).
 \label{eq:flux}$$ Thus $J_{\rm int}/J_{\rm wall}=e^{-\lambda^2}$ exactly. Integrating $u_t=u_{xx}$ on the moving interval (the boundary value $u(s(t),t)=0$ removes the Reynolds endpoint term) gives $$\int_0^tJ_{\rm wall}(\tau)\,\mathrm d\tau
 =\int_0^{s(t)}u(x,t)\,\mathrm dx+\beta s(t).
 \label{eq:ledger}$$ The elementary antiderivative $\int_0^\lambda\operatorname{erf}\eta\,\mathrm d\eta
=\lambda\operatorname{erf}\lambda+(e^{-\lambda^2}-1)/\sqrt\pi$ therefore yields $$\begin{aligned}
 S(t)&:=\int_0^{s(t)}u\,\mathrm dx
 =\frac{2\sqrt t(1-e^{-\lambda^2})}{\sqrt\pi\operatorname{erf}\lambda},\\
 L(t)&:=\beta s(t)=2\beta\lambda\sqrt t
 =\frac{2e^{-\lambda^2}\sqrt t}{\sqrt\pi\operatorname{erf}\lambda},\\
 I(t)&:=\int_0^tJ_{\rm wall}(\tau)\,\mathrm d\tau
 =\frac{2\sqrt t}{\sqrt\pi\operatorname{erf}\lambda}=S(t)+L(t).
 \label{eq:energy}\end{aligned}$$ This is an exact sensible-plus-latent energy ledger, not a fitted numerical balance. The eight rational probes in the accompanying receipt cover both terms and the Lambert enclosure.

\>1

# Singular limits, source boundary, and audit

As $\beta\to\infty$ (small $\mathrm{Ste}$), $\lambda\to0$ by [\[eq:small\]](#eq:small){reference-type="eqref" reference="eq:small"}; the normalized interface speed vanishes. As $\beta\to0^+$ (large $\mathrm{Ste}$), $\lambda\to\infty$ with [\[eq:large\]](#eq:large){reference-type="eqref" reference="eq:large"}. Zero superheat makes the chosen normalization undefined, and zero dimensional diffusivity $\kappa=0$ collapses the similarity length $2\lambda\sqrt{\kappa t}$ (here $\kappa$ denotes the dimensional diffusivity before the displayed scaling). The zero-latent limit $L=0$ is $\mathrm{Ste}=\infty$ and requires a separate rescaling, as emphasized in the small-latent-heat analysis of Addison--Howison--King [@addison]; no finite-$\lambda$ Stefan interface is claimed. These boundaries are distinct from the fixed-domain Barenblatt and KPP families (C207 and C202): here the defining advance is a moving boundary and the exact ledger [\[eq:energy\]](#eq:energy){reference-type="eqref" reference="eq:energy"}.

(A0\_FAIL, A1\_FAIL, A2\_FAIL, A3\_FAIL, A4\_FORMAL\_HINT).

Hence `overall=ROUTE_A_REJECTED` and `route_b_invocation_allowed=false`. The source heat clock is not target continuation/divisor/counting law and is not an A3 analytic-structure match. The scope lock is

NO\_BAD\_EULER\_OR\_ROOT\_NUMBER.

No target prime or zero table, Euler factor, root number, automorphy statement, functional equation, or Hilbert--Pólya operator is introduced.

# Source note {#source-note .unnumbered}

The classical free-boundary setting and small-latent-heat asymptotics are documented by Addison, Howison, and King [@addison]; phase-change and Neumann conventions are treated in Gupta [@gupta]; two-phase stability background is given by Rubinstein [@rubinstein]. These references are source metadata, not a priority or arithmetic claim.

9 J. A. Addison, S. D. Howison, and J. R. King, Ray methods for Free Boundary Problems, Oxford author manuscript (2005), [smallstefan.pdf](https://people.maths.ox.ac.uk/howison/papers/smallstefan.pdf). S. C. Gupta, *The Classical Stefan Problem: Basic Concepts, Modelling and Analysis*, Elsevier, North-Holland Series in Applied Mathematics and Mechanics, Volume 45 (2003), ISBN 978-0-444-51086-0. L. I. Rubinstein, Global Stability of the Neumann Solution of the Two-phase Stefan Problem, *IMA Journal of Applied Mathematics* 28(3), 287--299 (1982). DOI: [10.1093/imamat/28.3.287](https://doi.org/10.1093/imamat/28.3.287).

# Declarations {#declarations .unnumbered}

**Scope.** `NO_BAD_EULER_OR_ROOT_NUMBER`; no target arithmetic or operator claim. **Data and code.** The theorem, ledger, independent checks, and build instructions are released with HCS-C226. **AI-use disclosure.** Generative tools assisted drafting and code generation; the internal artifact chain checked displayed claims and metadata. This is not external peer review.
