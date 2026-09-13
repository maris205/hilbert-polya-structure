---
p1_kind: "derived-fulltext-reading-copy"
route: "henon_dynamics"
logical_paper_id: "henon_dynamics--henon-instability-roof-zeta"
canonical_tex: "henon_dynamics/henon_instability_roof_zeta/paper/main.tex"
canonical_pdf: "henon_dynamics/henon_instability_roof_zeta/paper/main.pdf"
source_sha256: "18b6c192c2dcabbb551b8175b8136f093522beeac0dce9794e769687b607425a"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Non-Lattice Instability Clock on a Certified Hénon Survivor

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../henon_dynamics/henon_instability_roof_zeta>)
- [规范 TeX](<../../../../../henon_dynamics/henon_instability_roof_zeta/paper/main.tex>)
- [关联 PDF](<../../../../../henon_dynamics/henon_instability_roof_zeta/paper/main.pdf>)
- [支撑 Markdown](<../../../../../henon_dynamics/henon_instability_roof_zeta/README.md>)
- [BibTeX](<../../../../../henon_dynamics/henon_instability_roof_zeta/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We isolate a clock-selection question that precedes any dynamical Hilbert--Pólya comparison. On a previously certified local hyperbolic survivor of the area-preserving Hénon map $H_6(x,y)=(1-6x^2-y,x)$, we prove that the unstable-expansion lengths $T_p=\log\left|\Lambda_{u,p}\right|$ have a positive Hölder roof representative and are non-lattice. The proof combines the uniform bound $J^u\ge 773/224>1$ with two exact primitive multipliers whose logarithms have irrational ratio. By contrast, unit map time forces a $2\pi\mathrm{i}$-periodic divisor, while the stored generating-function action vanishes on an explicit primitive period-four orbit.

  We then freeze a target-free cycle-section experiment before opening periods 13--20. Complete symbolic enumeration produces 2,170 primitive cycles through period 20. In the rectangle $-0.25\le\Re s\le0.30$, $\left|\Im s\right|\le20$, every tested untwisted section has 43 located zeros; all 39 preregistered untwisted zeros survive the sealed test with median drift $1.76\times10^{-6}$. Independent coefficient recursions, 80-digit residuals, numerical winding audits, randomized orbit-level controls, and neighboring-parameter controls audit and contextualize the finding. The exact constant-roof parent is even more stable. Thus the experiment detects structured finite-section cancellation, not an arithmetic signature: no limiting determinant, functional equation, Riemann--von Mangoldt law, or self-adjoint operator is obtained.
author:
- Anonymous research note
bibliography:
- references.bib
date: 5 August 2026
title: 'A Non-Lattice Instability Clock on a Certified Hénon Survivor'
```

## Markdown 正文

# Introduction {#sec:introduction}

A dynamical zeta function cannot be compared meaningfully with the Riemann zeta function until its clock has been fixed. For a discrete map, integer iteration time is natural, but composing a one-variable map determinant with $z=\mathrm{e}^{-s}$ makes its divisor periodic in the imaginary direction. Such a divisor has linear zero-count growth in a bounded real strip, whereas the Riemann--von Mangoldt count has order $T\log T$ [@MontgomeryVaughan2007]. Changing orbit weights without changing this integer clock does not cure that exact mismatch.

This note asks a narrower question on a strong pre-existing dynamical object: does the unstable expansion of an explicit hyperbolic Hénon survivor provide a positive non-lattice clock, and do the resulting finite cycle sections have reproducible complex zeros? The survivor belongs to $$H_6(x,y)=(1-6x^2-y,x)$$ and is conjugate to a four-state subshift of finite type. We inherit that local conjugacy and its cone bounds; we do not claim a Markov partition for the full Hénon plane.

The exact answer to the clock question is positive. An adapted unstable Jacobian $J^u$ is uniformly larger than one, and its periodic sums equal $\log\left|\Lambda_{u,p}\right|$. A fixed orbit and an explicit period-four orbit have algebraic multipliers of incompatible power degrees. Their instability lengths therefore have irrational ratio, so the roof is non-lattice. This removes the unit-clock lattice-periodicity obstruction and nothing more.

The computational question is evaluated without prime tables, Riemann-zero tables, zeta or xi evaluations, parameter fitting, or post-validation rescaling. The object, determinant convention, complex rectangle, matching tolerance, precision, random seeds, and period splits were frozen before the sealed periods were opened. Our contributions are:

1.  We prove a three-way clock triage: unit time has an exact periodicity obstruction, the stored action is not a positive roof, and instability time is positive and non-lattice.

2.  We enumerate all 2,170 primitive symbolic cycles through period 20 and evaluate a precisely defined degree-in-symbolic-period cycle section by two independent coefficient constructions.

3.  We report a preregistered family of finite-section zeros that survives validation and sealed testing, together with controls showing both strong structured cancellation and its lack of arithmetic specificity.

The final qualification is part of the result. Each fixed section is an exponential polynomial. We prove no uniform tail theorem as the section order tends to infinity, no analytic continuation or functional equation, and no operator realization. The Route-A outcome is consequently exploratory rather than a Hilbert--Pólya candidate.

# Related context {#sec:related}

#### Symbolic Hénon dynamics.

The Hénon family is a standard source of low-dimensional stretching and folding [@Henon1976]. Rigorous shift descriptions exist in suitable parameter regimes [@DevaneyNitecki1979], while subshifts of finite type provide the finite combinatorial models used to enumerate periodic points [@LindMarcus1995]. Those general results do not by themselves certify the particular four-state survivor used here. Our geometric input is instead the companion repository certificate: explicit rational state rectangles, transition exclusions, a signed square-root contraction, and cone hyperbolicity at $a=6$. This note treats that certificate as a hashed local dependency and restricts every theorem to its survivor $\Lambda_*$. Precisely, the R058 covering proof supplies survivor existence, exact transition exclusions, and cone hyperbolicity; the R059 contraction proof upgrades the symbolic factor to a conjugacy and proves uniqueness for each admissible itinerary. These are inherited premises, not results reproved in this note. Their repository paths and full digests are recorded in Appendix [10](#app:reproducibility){reference-type="ref" reference="app:reproducibility"}.

#### Dynamical zeta functions and roofs.

Ruelle's zeta functions for expanding maps and Anosov flows organize primitive periodic data into analytic objects under hyperbolicity and regularity hypotheses [@Ruelle1976]. Thermodynamic formalism associates Hölder potentials and suspension roofs with transfer operators and pressure [@Bowen1975; @Ruelle1978]. These theorems explain why $\log\left|\Lambda_u\right|$ is a natural geometric potential. They do not identify an arbitrary finite cycle section with a Fredholm determinant on a specified Banach space. We therefore define our sections algebraically and reserve transfer-operator language for a future limiting construction.

#### Cycle expansions.

Cycle expansions group long periodic orbits with shorter shadowing combinations; correlated weights can yield rapidly decreasing curvature coefficients [@ArtusoAurellCvitanovic1990]. This motivates the coefficient-tail diagnostics below. The orbit-level randomizations in our control panel are deliberately destructive, however, and need not arise from a Hölder potential. Smaller coefficients relative to those controls establish structured cancellation, not its unique mechanism. Locally constant and finite-memory roof controls would be needed to isolate shadowing more sharply.

#### Multiplier data.

Unstable multipliers are geometric marked data, not arbitrary orbit labels. Recent work shows strong rigidity of the complete saddle multiplier spectrum for complex Hénon maps [@CantatDujardin2026]. Our result is different in scale and purpose: we use two exact real multipliers to prove that one local roof is non-lattice, and a finite multiplier catalogue to build numerical sections. We make no parameter-rigidity claim.

#### Hilbert--Pólya boundary.

A Hilbert--Pólya program needs more than a visually stable resonance set. At minimum, the dynamical object must supply a coherent global divisor with the right counting law and symmetry; an operator formulation must additionally specify a Hilbert space, domain, and self-adjoint or antiunitary structure. The present work is a falsification-oriented prerequisite audit. Its negative analytic conclusions are as important as its positive clock theorem.

# Certified survivor and determinant convention {#sec:setup}

## Inherited local dynamics

Let $$H_a(x,y)=(1-a x^2-y,x).$$ The Jacobian $$DH_a(x,y)=
  \begin{pmatrix}-2ax&-1\\1&0\end{pmatrix}$$ has determinant one. At $a=6$, the companion certificate supplies a compact local survivor $\Lambda_*$ and a conjugacy with the subshift $\Sigma_A$ whose adjacency matrix, in state order $--,-+,+-,++$, is $$A=
 \begin{pmatrix}
 1&0&1&0\\
 1&0&0&0\\
 0&1&0&1\\
 0&1&0&0
 \end{pmatrix}.
 \label{eq:adjacency}$$ In particular, every primitive admissible cyclic word labels exactly one primitive orbit in $\Lambda_*$. The statement is local: neither the full nonwandering set of $H_6$ nor the finite-resolution open domains studied in prior work enter the present determinant.

The signed recurrence used to lift a cyclic sign word $\varepsilon_i\in\{-1,1\}$ is $$q_i=\varepsilon_i
  \sqrt{\frac{1-q_{i-1}-q_{i+1}}{6}}.
  \label{eq:sqrt-recurrence}$$ On the certified boxes, its sup-norm Lipschitz constant is at most $2/\sqrt{17}<1$. Banach iteration therefore produces the unique orbit and the a posteriori error estimate $$\left\lVert q-q^\star\right\rVert_\infty
 \le \frac{\left\lVert\mathcal T_\varepsilon q-q\right\rVert_\infty}
 {1-2/\sqrt{17}}.$$

## Instability roof

The cone certificate uses normalized tangent coordinates $$u=\frac{\delta x}{7/48},\qquad
 v=\frac{\delta y}{41/256},\qquad
 r=\frac{41/256}{7/48}=\frac{123}{112}.$$ Writing the invariant unstable line as $$E_z^u=\{(u,m^u(z)u):u\in\mathbb{R}\},\qquad \left|m^u(z)\right|\le\frac12,$$ the standard graph-transform regularity theorem applies: $H_6$ is $C^\infty$, and the compact set $\Lambda_*$ is uniformly hyperbolic, so $E^u$, hence $m^u$, is Hölder on $\Lambda_*$ [@Hasselblatt1994]. Because the argument below is uniformly bounded away from zero, the resulting roof is Hölder as well. Define the adapted unstable Jacobian and roof by $$J^u(z)=\left|-12x-rm^u(z)\right|,\qquad
 \tau(z)=\log J^u(z).
 \label{eq:roof}$$ For a primitive orbit $p$, let $$T_p=\sum_{z\in p}\tau(z)=\log\left|\Lambda_{u,p}\right|,
 \qquad
 \sigma_p=\mathop{\mathrm{sgn}}(\Lambda_{u,p}).$$ The periodic data $T_p$ are intrinsic. Changing the norm on $E^u$ by a positive Hölder factor $c(z)$ replaces $\tau$ by $$\tau'(z)=\tau(z)+\log c(H_6z)-\log c(z),$$ so the representative changes by a Hölder coboundary but all periodic sums remain fixed.

## One frozen cycle-section ledger

Introduce a symbolic-degree marker $z$, distinct from phase-space points. For $\kappa\in\{0,1\}$, define formally $$D_\kappa(s;z)=
 \prod_{p\in\mathcal{P}}
 \left(1-\sigma_p^\kappa \mathrm{e}^{-sT_p}z^{n_p}\right),
 \label{eq:two-variable}$$ where $\mathcal{P}$ is the set of primitive orbits in $\Lambda_*$. The computed object is $$D_{\kappa,N}(s)=
 \left[D_\kappa(s;z)\right]_{\deg z\le N}\big|_{z=1}.
 \label{eq:section}$$ Degree truncation occurs before $z=1$ is substituted. Equation [\[eq:section\]](#eq:section){reference-type="eqref" reference="eq:section"} is not the finite primitive Euler product evaluated at $z=1$, a smooth Perron flat determinant, an Ulam determinant, a completed xi function, or a proved Fredholm determinant.

# Clock triage {#sec:clock}

[\[thm:clock\]]{#thm:clock label="thm:clock"} The certified Hénon survivor has the following three clock properties.

1.  The unit-clock determinant is $2\pi\mathrm{i}$-periodic in $s$ and has $O(T)$ zeros in every bounded real strip up to height $T$.

2.  The stored generating-function action is not a strictly positive roof.

3.  The instability roof in [\[eq:roof\]](#eq:roof){reference-type="eqref" reference="eq:roof"} is positive, its periodic sums obey $T_{p^r}=rT_p$, and it is non-lattice.

For unit time, direct calculation from [\[eq:adjacency\]](#eq:adjacency){reference-type="eqref" reference="eq:adjacency"} gives $$\det(I-zA)=1-z-z^3-z^4.
 \label{eq:unit-z}$$ Thus $$D_{\rm unit}(s)=1-\mathrm{e}^{-s}-\mathrm{e}^{-3s}-\mathrm{e}^{-4s}$$ is invariant under $s\mapsto s+2\pi\mathrm{i}$. A nonzero exponential polynomial has finitely many zeros in a compact fundamental rectangle. Translating that rectangle proves the $O(T)$ bound. In fact, $$1-z-z^3-z^4=-(z^2+1)(z^2+z-1),$$ so the vertical towers can be written explicitly.

For the action clock, put $q=1/\sqrt6$ and consider $$(q_0,q_1,q_2,q_3)=(-q,-q,q,q).$$ It satisfies the Hénon recurrence and is an admissible primitive period-four orbit inside the certified rectangles. For the generating function $$S_6(q_i,q_{i+1})=q_iq_{i+1}-q_i+2q_i^3,$$ each of $\sum_iq_iq_{i+1}$, $\sum_iq_i$, and $\sum_iq_i^3$ vanishes. Its total action is therefore zero, excluding strict positivity.

On $\Lambda_*$, the certificate gives $\left|x\right|\ge1/3$ and $\left|m^u\right|\le1/2$. Hence $$J^u(z)\ge12\left|x\right|-r\left|m^u(z)\right|
 \ge4-\frac{123}{224}=\frac{773}{224}>1.
 \label{eq:positive}$$ The roof is positive. Invariance of the unstable graph gives $u_{j+1}=a_ju_j$, where $a_j=-12x_j-rm^u(z_j)$. Around a periodic orbit, $$\prod_{j=0}^{n_p-1}a_j=\Lambda_{u,p}.$$ Taking logarithms of absolute values proves the periodic-sum identity and the repetition law.

A Hölder roof is called *lattice* if it is Hölder-cohomologous to $c k$ for some $c>0$ and integer-valued $k$; in particular, every periodic sum then lies in $c\mathbb Z$. It remains to rule this out. The negative fixed point $$q_*=-\frac{1+\sqrt7}{6}$$ has unstable multiplier $L_1>1$ with minimal polynomial $$P_1(X)=X^4-4X^3-22X^2-4X+1.
 \label{eq:p1}$$ The explicit period-four orbit has trace $578$ and multiplier $$L_4=289+24\sqrt{145},
 \qquad
 P_4(X)=X^2-578X+1.$$ The four conjugates of $L_1$ have distinct absolute values. Consequently, the four conjugates of $L_1^m$ remain distinct for every $m\ge1$, and $[\mathbb{Q}(L_1^m):\mathbb{Q}]=4$. Every $L_4^n$ lies in $\mathbb{Q}(\sqrt{145})$ and has degree at most two. An equality $\log L_4/\log L_1=m/n\in\mathbb{Q}$ would imply $L_1^m=L_4^n$, a contradiction. Two periodic lengths therefore have irrational ratio, which rules out a common lattice. The exact algebra and power-degree argument are expanded in Appendix [9](#app:algebra){reference-type="ref" reference="app:algebra"}.

Non-lattice time removes the exact vertical periodicity forced by unit map time. It does not imply a meromorphic continuation, a functional equation, a Riemann--von Mangoldt law, or an operator spectrum. Those are separate Route-A obligations.

# Frozen computational experiment {#sec:experiment}

## Source lock and splits

The protocol was serialized before the sealed periods were generated. Its SHA-256 digest is

`0c284a1b3610a3d772aa00c6a8b33161a8bc6814957a9968d5c80fb618eec399`.

The object is $H_6|_{\Lambda_*}$; the clock, scale, and offset are fixed as $T_p=\log\left|\Lambda_{u,p}\right|$, scale one, offset zero. The complex rectangle is $$\mathcal{R}=\{s\in\mathbb{C}:-0.25\le\Re s\le0.30,\ \left|\Im s\right|\le20\}.$$ Periods 1--8 form development, 9--12 validation, 13--16 the sealed test, and 17--20 post-test robustness. The matching tolerance is $0.02$. The training family contains cutoff-8 zeros that match cutoff 7 within this tolerance and lie at least $0.01$ from the contour.

Prime tables, primality labels, Riemann-zero tables, evaluations of zeta or xi, target spectral fitting, and post-validation rescaling were forbidden. This firewall makes the experiment a self-consistency test of one dynamical candidate, not a goodness-of-fit exercise.

## Complete orbit ledger

Every primitive closed $A$-word is enumerated exactly up to cyclic rotation. Equation [\[eq:sqrt-recurrence\]](#eq:sqrt-recurrence){reference-type="eqref" reference="eq:sqrt-recurrence"} then lifts it at 80 decimal digits. For each orbit, the ledger stores its canonical state and sign words, coordinates, recurrence residual, a posteriori contraction bound, monodromy, unstable multiplier, orientation, instability length, and generating-function action. The catalogue is complete within the symbolic survivor at every stated cutoff.

The two neighboring catalogues $a=5.9,6.1$ reuse the same words as numerical continuations only. On the common boxes, their contraction diagnostic uses $$\kappa(a)=\frac{2}{\sqrt{17}}\sqrt{\frac6a}.$$ No common-survivor theorem is inferred from their convergence.

## Two coefficient constructions

Primitive-factor multiplication gives the coefficients of [\[eq:section\]](#eq:section){reference-type="eqref" reference="eq:section"} directly. An independent trace recursion uses $$F_j^{(\kappa)}(s)=
 \sum_{\substack{p\in\mathcal{P}\\n_p\mid j}}
 n_p\,\sigma_p^{\kappa j/n_p}\mathrm{e}^{-s(j/n_p)T_p},
 \label{eq:traces}$$ followed by $$d_0(s)=1,\qquad
 d_n(s)=-\frac1n\sum_{j=1}^nF_j^{(\kappa)}(s)d_{n-j}(s),
 \qquad
 D_{\kappa,N}(s)=\sum_{n=0}^N d_n(s).
 \label{eq:cumulant}$$ Both constructions use the same complete orbit ledger but independent algebraic paths. Agreement is tested at fixed complex probes and at every reported zero.

## Zeros and numerical winding audit

Float64 discovery combines grid-cell phase windings and local modulus minima, then applies bounded Newton refinement. Each located zero is refined at 80 decimal digits and checked with both coefficient constructions. The sampled argument change around $\partial\mathcal{R}$ is evaluated at 4,096, 8,192, and 16,384 contour points. We record agreement across resolutions, the minimum sampled boundary modulus, and the maximum phase step.

These winding counts are numerical diagnostics, not interval certificates. Even when all three grids agree and every sampled phase step is below $\pi$, an analytic derivative bound or interval enclosure would be required to rule out unresolved behavior between samples.

## Controls

The frozen control panel contains global period and length shuffles, same-density random lengths, positive random factor weights, random phases, an exact constant-roof parent, and numerical continuations at $a=5.9,6.1$. For the exact parent, every step has length $\ell_*=\log L_1\simeq1.96734662909421$, the negative fixed-orbit length, so $T_p=n_p\ell_*$ and its determinant is $\det(I-z\mathrm{e}^{-s\ell_*}A)$; coefficients above degree four vanish exactly. Random controls use seeds 20260805--20260807. Root retention is measured from cutoff 8 to 16. A second statistic is the degree-9--16 coefficient $\ell^1$ tail at the common Hénon cutoff-16 positive zero. Since the randomized orbit data need not define Hölder potentials, this panel diagnoses non-generic cancellation but cannot alone identify its mechanism.

# Results {#sec:results}

## Orbit and numerical gates

The primitive catalogue sizes are $$\begin{array}{c|rrrr}
\text{maximum period}&8&12&16&20\\\hline
\text{primitive cycles}&17&79&402&2170.
\end{array}$$ Every count agrees with the exact symbolic enumeration. At period 20, the largest recurrence residual is $1.94\times10^{-65}$, the largest a posteriori contraction bound is $1.94\times10^{-65}$, and the smallest hyperbolicity margin $\left|\mathop{\mathrm{tr}}M_p\right|-2$ is $5.29$. A 120-digit reconstruction from persisted coordinates gives determinant error below $2.0\times10^{-90}$ in the producer audit. An independent implementation gives $5.8\times10^{-70}$. The raw 80-digit hyperbolic matrix product loses digits through cancellation and has maximum displayed error $4.28\times10^{-50}$; it is reported rather than rounded to zero.

All 79 period-at-most-12 words match the companion catalogue. The largest relative multiplier difference is $4.44\times10^{-65}$.

## Finite-section zeros

Table [1](#tab:counts){reference-type="ref" reference="tab:counts"} gives the located-root and sampled-winding census for both orientation sectors.

::: {#tab:counts}
   $\kappa\backslash N$     7    8   10   12   14   16   18   20
  ---------------------- ---- ---- ---- ---- ---- ---- ---- ----
            0              43   43   43   43   43   43   43   43
            1              45   45   43   43   43   43   43   43

  : Numerical zero census in the frozen rectangle. Each sampled winding count agrees at 4,096, 8,192, and 16,384 contour points and equals the located root count. The equality is a numerical consistency result, not an interval certificate.
:::

The largest high-precision determinant residual over all reported roots in Table [1](#tab:counts){reference-type="ref" reference="tab:counts"} is $8.35\times10^{-65}$, and the largest high-precision coefficient discrepancy is $7.46\times10^{-75}$. The largest float-to-80-digit root shift is $1.68\times10^{-10}$.

Table [2](#tab:stability){reference-type="ref" reference="tab:stability"} reports the frozen one-to-one retention tests.

::: {#tab:stability}
   $\kappa$  stage                    retained   fraction           median drift        90th percentile
  ---------- ---------------------- ---------- ---------- ---------------------- ----------------------
      0      validation $8\to12$         39/39      1.000   $1.873\times10^{-4}$   $2.535\times10^{-3}$
      0      sealed $12\to16$            39/39      1.000   $1.759\times10^{-6}$   $3.113\times10^{-5}$
      0      robustness $16\to20$        43/43      1.000   $8.116\times10^{-9}$   $1.928\times10^{-6}$
             validation $8\to12$         43/43      1.000   $1.166\times10^{-4}$   $2.481\times10^{-3}$
      1      sealed $12\to16$            43/43      1.000   $8.097\times10^{-7}$   $3.674\times10^{-5}$
      1      robustness $16\to20$        43/43      1.000   $6.349\times10^{-9}$   $7.382\times10^{-7}$

  : Preregistered root retention. Drifts are complex distances under one-to-one matching with tolerance $0.02$.
:::

Four untwisted zeros are outside the boundary-filtered training family but are present in the complete census; they are reported as extras relative to the tracked set, not as missing roots. The twisted family includes the exact root $s=0$, where all length weights disappear, plus 42 nonzero tracked zeros; the sign-cocycle derivation is in Appendix [9.3](#app:orientation-control){reference-type="ref" reference="app:orientation-control"}.

Let $h_N$ denote the positive real zero of $D_{0,N}$. The values $$\begin{aligned}
h_{10}&=0.27798298859371395,\\
h_{12}&=0.27798298173371744,\\
h_{16}&=0.27798298167628965,\\
h_{20}&=0.2779829816761890234883231168318\ldots
\end{aligned}$$ have $h_{16}-h_{20}\simeq1.01\times10^{-13}$; thus their first 12 decimal places agree. Later digits displayed for $h_{20}$ are high-precision digits of the cutoff-20 section, not evidence of cutoff convergence. We do not call $h_N$ a pressure root: no convergence to the pressure zero of a limiting transfer operator has been proved.

Figure [1](#fig:stability-controls){reference-type="ref" reference="fig:stability-controls"} places that cutoff comparison beside the coefficient-tail controls.

![Finite-section stability is structural evidence, not arithmetic evidence. (a) The untwisted positive real root approaches its displayed cutoff-20 value rapidly; the cutoff-20 point is plotted at a numerical floor because it defines the displayed reference, not because a limiting zero has been certified. (b) Valid randomized orbit controls have degree-9--16 coefficient tails between $2.9\times10^{4}$ and $3.2\times10^{5}$ times the Hénon tail. The exact constant-roof parent is smaller still. No fitted curve or external arithmetic target is used.](<../../../../../henon_dynamics/henon_instability_roof_zeta/paper/figures/figure1_stability_controls.pdf>){#fig:stability-controls width="\\textwidth"}

## Controls and mechanism boundary

The valid root-retention controls and their tail ratios are collected in Table [3](#tab:controls){reference-type="ref" reference="tab:controls"}.

::: {#tab:controls}
  control                         retained fraction           median drift           tail / Hénon
  ----------------------------- ------------------- ---------------------- ----------------------
  Hénon instability roof                      1.000   $1.891\times10^{-4}$                      1
  constant roof (exact)                       1.000                      0   $1.72\times10^{-10}$
  positive random weights                     0.084   $1.348\times10^{-2}$       $1.14\times10^5$
  random phases                               0.028   $1.215\times10^{-2}$       $3.20\times10^5$
  same-density random lengths                 0.042   $1.073\times10^{-2}$       $2.86\times10^4$

  : Cutoff-8-to-16 controls at the common Hénon probe. Random rows are mean values over three frozen seeds. The constant-roof tail is a numerical floor; its exact coefficients vanish beyond the finite parent determinant.
:::

At the common probe, the true cycle tail is $6.866\times10^{-7}$. The valid orbit-level randomizations have tails between $2.86\times10^4$ and $3.20\times10^5$ times larger and retain few cutoff-8 zeros. The data show structured cancellation. They do not prove that symbolic shadowing is the unique cause, because the random controls have different natural spectral scales and need not come from local potentials.

The global period and length shuffles are retained as failed numerical controls. Their high-frequency exponential terms make the three frozen contour resolutions disagree, so the sampler does not resolve their root counts. The functions themselves are not mathematically *untestable*.

Finally, the $a=5.9$ and $a=6.1$ continuations each retain all cutoff-8 zeros at cutoff 16, with median self-drifts $3.75\times10^{-4}$ and $4.08\times10^{-4}$. Only $5/39$ Hénon training zeros match either neighbor within the frozen tolerance. Internal stability is therefore not specific to $a=6$, although no common hyperbolic parameter interval has been certified.

# Route-A implications {#sec:route-a}

The experiment is evaluated against the repository's Route-A criteria rather than against visual resemblance to a target spectrum. The resulting tuple is $$\bigl(
 \texttt{A1\_WEAK},
 \texttt{A2\_FROZEN\_VALIDATION\_PASS},
 \texttt{A3\_FAIL},
 \texttt{A4\_FORMAL\_HINT}
 \bigr),$$ with overall status `ROUTE_A_EXPLORATORY`.

#### A1: orbit correspondence is weak.

The local orbit ledger is unusually strong: symbolic conjugacy proves completeness at every finite cutoff, primitive cycles and repetitions are separated, orientations are retained, and instability lengths are intrinsic periodic data. A1 nevertheless remains weak because there is no natural prime-like correspondence, no logarithmic-prime length law, and no von-Mangoldt repetition amplitude. Calling a symbolic primitive orbit *prime* would be terminology, not arithmetic evidence.

#### A2: frozen validation passes internally.

Both orientation sectors retain every tracked zero on validation and sealed test; the located-root census, three sampled winding grids, and independent coefficient constructions agree. This verdict describes the candidate's own finite-section stability. Errors relative to the Riemann divisor are `NOT_TESTABLE`, because no Riemann data were allowed or used. Four untwisted zeros lie outside the boundary-filtered tracked family, and two shuffled controls defeat the frozen contour sampler. The exact constant-roof parent is more stable than the geometric roof.

#### A3: global analytic structure fails.

For every fixed $N$, $D_{\kappa,N}$ is an exponential polynomial and has linear zero-count growth in height. A $T\log T$ law cannot be inferred by choosing $N=N(T)$ unless a uniform tail theorem justifies that moving order. No such theorem is present. There is also no functional equation, gamma factor, trivial-zero structure, analytic continuation, or completed determinant. Non-lattice time removes one exact obstruction but does not supply these missing structures.

#### A4: only a formal operator hint.

Area preservation, reversibility, and a positive suspension roof are legitimate dynamical inputs. They do not specify a Hilbert space, a densely defined operator, a domain, boundary conditions, self-adjointness, or an antiunitary symmetry. Route B is therefore not authorized.

Here reversibility is concrete: for $R(x,y)=(y,x)$, direct substitution gives $R H_a R=H_a^{-1}$. This classical symmetry alone does not construct the missing operator data.

The smallest promotion test is a uniform cycle-tail bound on a fixed contour around the positive real finite-section zero. A Rouché comparison that persists as $N\to\infty$ would establish one limiting zero without invoking any arithmetic target. A complementary construction should approximate the same Hölder roof by cylinder-memory transfer matrices and compare their determinants with the orbit sections.

# Conclusion {#sec:conclusion}

The instability spectrum of the certified $H_6$ survivor supplies a natural way to leave integer map time. Its periodic lengths are positive, obey the correct repetition law, and include two incommensurable exact values. The resulting roof is non-lattice, so the exact $2\pi\mathrm{i}$-periodicity of the unit clock no longer applies.

Complete enumeration through period 20 also reveals a reproducible finite-section phenomenon. A preregistered family of complex zeros survives validation and sealed testing. The positive real roots $h_{16}$ and $h_{20}$ agree in their first 12 decimal places, with difference about $1.01\times10^{-13}$; later displayed digits describe $D_{0,20}$, not proved cutoff stability. Its degree-9--16 coefficient $\ell^1$ tail at the common cutoff-16 positive-zero probe is far smaller than in the valid randomized orbit-level controls. The constant-roof parent and nearby parameters show why these observations must be interpreted structurally rather than arithmetically.

The negative conclusion is decisive for the present Route-A classification. No limiting determinant, global counting law, functional equation, prime correspondence, or self-adjoint operator has emerged. The project therefore delivers an exact clock theorem, a carefully bounded numerical candidate, and a current A3 blocker. The next work should target a fixed-contour Rouché bound, finite-memory Hölder roof controls, and a cylinder transfer operator for the same local survivor.

# Exact algebra {#app:algebra}

## The period-four orbit

Let $q=1/\sqrt6$ and $$\mathbf q=(-q,-q,q,q).$$ Because $6q_i^2=1$, the Hénon recurrence becomes $q_{i+1}=-q_{i-1}$, which the sequence satisfies. Its cyclic state word is a rotation of $$(--,\,+-,\,++,\,-+),$$ and all four points lie strictly inside the corresponding certified rectangles. The three components of the action satisfy $$\sum_iq_iq_{i+1}=0,\qquad
 \sum_iq_i=0,\qquad
 \sum_iq_i^3=0.$$ Thus $\sum_iS_6(q_i,q_{i+1})=0$.

Up to cyclic conjugacy, its exact monodromy is $$M_4=
 \begin{pmatrix}
 601&-48\sqrt6\\
 48\sqrt6&-23
 \end{pmatrix},$$ with trace 578 and determinant one. Hence $$L_4=289+24\sqrt{145},\qquad
 L_4^2-578L_4+1=0.$$

## Degree of powers of the fixed multiplier

For $q_*=-(1+\sqrt7)/6$, the trace is $t_+=2+2\sqrt7$ and $$L_1+L_1^{-1}=t_+.$$ Eliminating $\sqrt7$ gives the reciprocal polynomial $$P_1(X)=X^4-4X^3-22X^2-4X+1.$$ To prove irreducibility, work over $K=\mathbb{Q}(\sqrt7)$. The discriminant of the quadratic for $L_1$ is $$t_+^2-4=28+8\sqrt7.$$ Its norm to $\mathbb{Q}$ equals $336$, which is not a rational square. The discriminant is therefore not a square in $K$, so $$[K(L_1):K]=2.$$ Moreover, $\sqrt7=(L_1+L_1^{-1}-2)/2\in\mathbb{Q}(L_1)$, hence $K\subset\mathbb{Q}(L_1)$ and $K(L_1)=\mathbb{Q}(L_1)$. The tower law now gives $[\mathbb{Q}(L_1):\mathbb{Q}]=4$.

Set $$U(t)=\frac{t+\sqrt{t^2-4}}2\quad(t>2),\qquad
 M=U(2\sqrt7-2).$$ The conjugates of $L_1$ are $$L_1,\ L_1^{-1},\ -M,\ -M^{-1}.$$ Since $$L_1>M>1>M^{-1}>L_1^{-1}>0,$$ their absolute values are distinct. Raising them to any positive integer power preserves distinctness, including when the signs of the last pair coincide. Thus $[\mathbb{Q}(L_1^m):\mathbb{Q}]=4$ for all $m\ge1$. Since $L_4^n\in\mathbb{Q}(\sqrt{145})$, an equality $L_1^m=L_4^n$ is impossible.

## Orientation-twisted unit control {#app:orientation-control}

At $s=0$, the instability lengths disappear from the orientation-twisted section. From [\[eq:positive\]](#eq:positive){reference-type="eqref" reference="eq:positive"}, the one-step unstable factor $a_j=-12x_j-rm^u(z_j)$ has sign $-\mathop{\mathrm{sgn}}x_j$. Thus $$\sigma_p=(-1)^{n_p}\prod_{j=0}^{n_p-1}\mathop{\mathrm{sgn}}x_j.$$ In the state order $--,-+,+-,++$, this sign character weights the outgoing states by $B=\operatorname{diag}(1,1,-1,-1)A$. Direct expansion gives the exact symbolic determinant $$\det(I-zB)=1-z+z^3-z^4=(1-z^2)(1-z+z^2).$$ It has the tautological root $z=1$, corresponding to $s=0$, and only cyclotomic-looking roots. This finite-state sign control is a warning: elementary symbolic characters can produce superficially arithmetic patterns without a prime correspondence.

# Reproducibility and artifact audit {#app:reproducibility}

All newly generated code and data live under the project directory . Three repository-local inputs outside it are hash-locked below: two proof premises and the required period-12 comparison bridge. The standalone checker audits all three. From the repository root, the complete pipeline is

    bash henon_instability_roof_zeta/code/run_all.sh

The period-20 root and randomized-control stages dominate runtime. No GPU or external dataset is used.

The exact theorem inherits the following repository-local premises; full paths, roles, and SHA-256 digests are generated from :

-   \
    role: exact rectangle covering, transition exclusion, cone hyperbolicity, and survivor existence;\
    full SHA-256: .

-   \
    role: signed square-root contraction, coding uniqueness, and conjugacy;\
    full SHA-256: .

-   \
    role: period-at-most-12 comparison catalogue used by the numerical bridge audit;\
    full SHA-256: .

::: {#tab:hashes}
  artifact              abbreviated SHA-256
  --------------------- ---------------------
  frozen protocol       `0c284a1b...ec399`
  period-20 catalogue   `37fefa48...4d08e`
  period-20 roots       `840d63ae...0ea2a`
  controls              `311c1de1...8f306`
  analysis summary      `a555a6e5...7de8f`
  independent check     `7cbd4179...207b9`

  : Deterministic primary source locks, generated after the independent audit.
:::

The independent checker does not import the producer module. It reconstructs primitive counts, recurrence and monodromy diagnostics, parameter-dependent neighbor contraction bounds, trace and product coefficients, and all 16,384-point contour values from the persisted catalogue. It then obtains the coarser winding grids by exact subsampling. The final audit passes 38 of 38 checks, and the unit-test suite passes seven of seven tests.

The software environment used for the recorded run is Python 3.12 with NumPy 2.4.4, SciPy 1.16.1, SymPy 1.14.0, mpmath 1.3.0, Matplotlib 3.10.5, PyYAML 6.0.2, and pytest 9.0.3. Exact versions are recorded in .

Generated JSON timestamps are pinned to the frozen protocol epoch, Matplotlib PDF metadata are normalized, and the complete script exports `SOURCE_DATE_EPOCH`; scientifically identical reruns therefore do not acquire fresh wall-clock bytes.

The enclosing workspace is not a Git worktree, so no commit identifier is available. The repository handoff therefore uses file hashes and a generated manifest rather than inventing source-control provenance.
