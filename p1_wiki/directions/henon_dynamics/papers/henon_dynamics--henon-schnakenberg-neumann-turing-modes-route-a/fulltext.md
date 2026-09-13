---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-schnakenberg-neumann-turing-modes-route-a"
canonical_tex: "henon_dynamics/henon_schnakenberg_neumann_turing_modes_route_a/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_schnakenberg_neumann_turing_modes_route_a/paper/main.pdf"
source_sha256: "49bf64f73f30e4d841a89412e0f3e2cd94892c2d5cfc92a69b14baad0cba294b"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# An Exact Neumann-Mode Turing Atlas for the Schnakenberg Reaction--Diffusion System

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_schnakenberg_neumann_turing_modes_route_a>)
- [规范 TeX](<../../../../../henon_dynamics/henon_schnakenberg_neumann_turing_modes_route_a/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_schnakenberg_neumann_turing_modes_route_a/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_schnakenberg_neumann_turing_modes_route_a/README.md>)

## 转换器读取的文档元数据

```yaml
abstract: |
  For the Schnakenberg system on a finite interval we derive the unique positive constant equilibrium, its kinetic stability chamber, and the exact two-by-two dispersion matrix for every Neumann mode. \>0 Inside the kinetically stable chamber we prove an if-and-only-if continuous wavenumber window, an if-and-only-if finite-domain criterion, an exact strict integer count of unstable modes, and every domain-length entry and exit wall. \>1 Compact-resolvent closure and the homogeneous, equal-diffusion, double-wall, endpoint, and excluded zero-diffusion faces complete the linear theorem. Finite exact receipts test the formulas but do not replace their proof. All Route-A gates fail and Route B remains locked.
author:
- 'Route-A source-local certificate HCS-C350'
date: 3 September 2026
title: |
  An Exact Neumann-Mode Turing Atlas\
  for the Schnakenberg Reaction--Diffusion System
```

## Markdown 正文

suppressoptionalinfo 512 trailerid \[\<C3502026090300000000000000000000\>\<C3502026090300000000000000000000\>\]

# Frozen model and kinetic chamber

Let $a,b,d_u,d_v,L>0$ and consider, on $0<x<L$, $$\label{eq:pde}
 \begin{split}
 u_t&=d_u u_{xx}+a-u+u^2v,\\
 v_t&=d_v v_{xx}+b-u^2v,
 \end{split}
 \qquad u_x=v_x=0\quad\text{at }x=0,L.$$ Put $s=a+b$. A positive spatially homogeneous equilibrium must satisfy $u^2v=b$ and $a-u+b=0$. Thus the unique positive spatially homogeneous equilibrium is $$\label{eq:eq}
 (u_*,v_*)=(s,b/s^2).$$ The reaction Jacobian there is $$\label{eq:J}
 J=\begin{pmatrix}(b-a)/s&s^2\\-2b/s&-s^2\end{pmatrix},
 \qquad \tau:=\operatorname{tr}J=\frac{b-a}{s}-s^2,
 \qquad \det J=s^2.$$ Thus the kinetic equilibrium is asymptotically stable exactly when $\tau<0$. At $\tau=0$ its eigenvalues are $\pm \mathrm{i}s$; for $\tau>0$ it has positive spectral abscissa.

Expand perturbations in the normalized Neumann cosine basis. With $$\label{eq:mu}
 \mu_n=(n\pi/L)^2,\qquad n=0,1,2,\ldots,$$ the $n$th coefficient evolves under $$\label{eq:M}
 M(\mu)=J-\begin{pmatrix}d_u\mu&0\\0&d_v\mu\end{pmatrix}.$$ Direct expansion gives $$\begin{aligned}
 T(\mu)&=\operatorname{tr}M(\mu)=\tau-(d_u+d_v)\mu,\label{eq:T}\\
 D(\mu)&=\det M(\mu)=d_ud_v\mu^2-B\mu+s^2,
 &B&:=d_v\frac{b-a}{s}-d_us^2.\label{eq:D}\end{aligned}$$ Consequently the complete modal pair is $$\label{eq:lambdas}
 \lambda_{n,\pm}=\frac{T(\mu_n)\pm
 \sqrt{T(\mu_n)^2-4D(\mu_n)}}{2}.$$ The phrase *kinetic and modal dispersion closure* marks the baseline manuscript: no continuum-wavenumber test has yet been promoted to a finite interval claim.

\>0

# Continuous window and exact finite-domain selection

Define $$\label{eq:Q}
 Q=B^2-4d_ud_vs^2.$$

[\[thm:turing\]]{#thm:turing label="thm:turing"} Assume $\tau<0$. A nonempty open interval of unstable positive squared wavenumbers exists if and only if $$\label{eq:windowcond}
 B>0,\qquad Q>0.$$ When these inequalities hold, set $$\label{eq:roots}
 \mu_\pm=\frac{B\pm\sqrt Q}{2d_ud_v}.$$ Then $0<\mu_-<\mu_+$ and the finite Neumann interval has a genuine linear Turing instability if and only if some $n\geq1$ satisfies $$\label{eq:strictmode}
 \mu_-<\mu_n<\mu_+.$$ Writing $r_\pm=(L/\pi)\sqrt{\mu_\pm}$, the exact number of unstable modes is $$\label{eq:count}
 N_{\rm unst}=\max\{0,\lceil r_+\rceil-\lfloor r_-\rfloor-1\}.$$ For fixed $n\geq1$, its precise domain-length chamber is $$\label{eq:length}
 \frac{n\pi}{\sqrt{\mu_+}}<L<\frac{n\pi}{\sqrt{\mu_-}}.$$ Equality at either wall is neutral rather than unstable.

Because $\tau<0$, equation [\[eq:T\]](#eq:T){reference-type="eqref" reference="eq:T"} is negative for every $\mu\geq0$. A real two-by-two matrix with negative trace has positive spectral abscissa exactly when its determinant is negative. Indeed, a negative determinant gives two real eigenvalues of opposite signs, whereas a positive determinant and negative trace put both eigenvalues in the open left half-plane.

The polynomial $D(\mu)$ has positive leading and constant coefficients. It is negative somewhere on the positive axis precisely when its vertex is positive and its minimum is negative, which is exactly [\[eq:windowcond\]](#eq:windowcond){reference-type="eqref" reference="eq:windowcond"}. The two roots are [\[eq:roots\]](#eq:roots){reference-type="eqref" reference="eq:roots"}; their sum and product are positive, so both are positive and $D<0$ precisely between them. This proves the continuous criterion and [\[eq:strictmode\]](#eq:strictmode){reference-type="eqref" reference="eq:strictmode"} after restricting to the actual Neumann spectrum.

Taking positive square roots of [\[eq:strictmode\]](#eq:strictmode){reference-type="eqref" reference="eq:strictmode"} gives $r_-<n<r_+$. The number of positive integers in this strict interval is exactly [\[eq:count\]](#eq:count){reference-type="eqref" reference="eq:count"}; the ceiling and floor conventions delete integer endpoints. Solving the same strict inequalities for $L$ yields [\[eq:length\]](#eq:length){reference-type="eqref" reference="eq:length"}.

At a window endpoint $D=0$ and $T<0$, so the two modal eigenvalues are $0$ and $T$: the zero eigenvalue is simple. The phrase *strict interval mode-count closure* marks the first substantive revision: continuous dispersion, discrete mode selection, multiplicity, and length walls now form one if-and-only-if theorem.

\>1

# Operator closure and all frozen boundaries

Let $$\label{eq:A}
 \mathcal A=\operatorname{diag}(d_u\partial_{xx},d_v\partial_{xx})+J,
 \qquad \mathcal D(\mathcal A)=H_N^2(0,L)^2$$ on $L^2((0,L);\mathbb R^2)$. The diagonal Neumann diffusion operator has compact resolvent; the constant matrix $J$ is bounded. Hence $\mathcal A$ also has compact resolvent. After complexification, the cosine basis gives an orthogonal direct sum of the blocks $M(\mu_n)$, so [\[eq:lambdas\]](#eq:lambdas){reference-type="eqref" reference="eq:lambdas"} exhausts its spectrum with algebraic multiplicity. Since $\mu_n\to\infty$, no further spectral component is hidden beyond the modal list.

The boundary atlas is exact.

-   The homogeneous mode $n=0$ is precisely $J$, so a Turing claim always requires kinetic stability and a distinct unstable mode $n\geq1$.

-   If $d_u=d_v=d$, then $B=d\tau<0$ in the kinetic chamber; equal diffusion cannot create a Turing window.

-   If $B>0$ and $Q=0$, then $D$ has a double zero as a polynomial in $\mu$. It never becomes negative. A discrete mode exactly at the contact has a simple zero temporal eigenvalue and a negative companion; there is no open unstable window.

-   If $Q>0$, an equality $\mu_n=\mu_-$ or $\mu_n=\mu_+$ is a neutral tie. Strict inequalities are essential in both [\[eq:count\]](#eq:count){reference-type="eqref" reference="eq:count"} and [\[eq:length\]](#eq:length){reference-type="eqref" reference="eq:length"}.

-   The faces $d_u=0$ or $d_v=0$ are excluded. They are not obtained by dividing [\[eq:roots\]](#eq:roots){reference-type="eqref" reference="eq:roots"} by zero, and no degenerate-parabolic extension is claimed.

Exact rational receipts contain nine chambers, 63 modal rows, and 20 length-wall polynomials. Separate modes land exactly on the lower and upper window endpoints, and each open-window chamber records the strict floor/ceiling count. The receipts verify equilibrium, Jacobian, determinant, state classification, both endpoints, and double walls without floating point. They do not prove the continuum theorem; the argument above does.

The named kinetics trace to Schnakenberg's 1979 paper [@schnakenberg1979]; the reaction--diffusion instability lineage traces to Turing's 1952 paper [@turing1952]. These citations establish source and terminology boundaries, not priority for the present finite-interval assembly. Nearby owners treat a Brusselator ODE Hopf normal form, scalar Cahn--Hilliard shells, a nonlocal Kuramoto probability PDE, and scalar Fisher--KPP fronts. None owns this unequal-diffusion Schnakenberg Neumann mode atlas.

All Route-A coordinates are FAIL: there is no arithmetic carrier, primitive orbit ledger, target determinant, analytic target bridge, or natural unitary lift. This is a source-local dissipative PDE calculation. No target arithmetic, local data, Euler factors, root number, automorphy, target zero match, Hilbert--Polya operator, or Route-B invocation is claimed. The phrase *operator, boundary, and route closure* marks the second substantive revision.

The result is a complete *linear* stability classification of the positive homogeneous equilibrium. It is not a theorem on nonlinear patterned branches, nonlinear global well-posedness, attractors, or pattern selection.

9 J. Schnakenberg, *Simple chemical reaction systems with limit cycle behaviour*, Journal of Theoretical Biology 81 (1979), 389--400. [doi:10.1016/0022-5193(79)90042-0](https://doi.org/10.1016/0022-5193(79)90042-0).

A. M. Turing, *The chemical basis of morphogenesis*, Philosophical Transactions of the Royal Society B 237 (1952), 37--72. [doi:10.1098/rstb.1952.0012](https://doi.org/10.1098/rstb.1952.0012).
