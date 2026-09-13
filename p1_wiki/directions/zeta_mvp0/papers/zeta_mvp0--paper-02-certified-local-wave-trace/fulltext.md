---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--paper-02-certified-local-wave-trace"
canonical_tex: "zeta_mvp0/paper_02_certified_local_wave_trace/manuscript/paper/main.tex"
canonical_pdf: "zeta_mvp0/paper_02_certified_local_wave_trace/manuscript/paper/main.pdf"
source_sha256: "22244a53417b834bf613bf9a7d7801458bc92f5cc1c1783d66470abb2c38fb89"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# A Local Relative Gutzwiller Trace and a Certified Fast Branch for a Clock-Preserving Hénon Schrödinger Pair

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/paper_02_certified_local_wave_trace>)
- [规范 TeX](<../../../../../zeta_mvp0/paper_02_certified_local_wave_trace/manuscript/paper/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/paper_02_certified_local_wave_trace/manuscript/paper/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/paper_02_certified_local_wave_trace/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/paper_02_certified_local_wave_trace/manuscript/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We establish an eigenvalue-only, one-orbit relative Gutzwiller term for a clock-preserving pair of two-dimensional Schrödinger operators, and we separately certify the distinguished orbit branch over an explicit parameter interval. The pair is formed by the radial exponential well $2\pi e^{\pi|q|^2}$ and its pullback by a centered, area-preserving Hénon automorphism at $a=1.02$. Although the two wells have exactly the same classical phase-volume clock, isolating a nonzero-time spectral fluctuation requires a complete model-specific audit of short returns, transverse nondegeneracy, Fourier normalization, and the removal of eigenfunction observables. A blow-up of the entire shrinking energy shell shows that, for every fixed sufficiently small excess $0<\delta<\delta_{\rm tr}$, one primitive fast Lyapunov orbit is the only warped return up to time $0.75$, while the radial reference has none. The resulting relative trace has the explicit positive-time coefficient $$i\widehat g(T_+)\frac{T_+}{2\pi\sqrt{|\det(I-P_+)|}}e^{iS_+/\hbar}
   +O(\hbar).$$ Independently, 202 validated CAPD/MPFR jobs and exact-rational proof-object replays certify one connected primitive local branch for $0\le\epsilon\le0.101$, $\delta=\epsilon^2$, together with the uniform gap $\det(I-D\Pi_\epsilon)>3$. A separately frozen 102-tree complement archive then excludes every other reduced root in the declared local box on all 51 parameter slabs: 52,790 interval nodes and 158,782 independent checks close with zero failures. The analytic threshold $\delta_{\rm tr}>0$ remains nonquantitative; consequently, the separate calculation at $\delta=0.01$ is a diagnostic rather than a theorem-domain validation. No prime-time or zeta-zero identification is claimed.
author:
- |
  Liang Wang$^{1,*}$\
  $^1$School of Artificial Intelligence and Automation,\
  Huazhong University of Science and Technology, Wuhan 430074, P.R. China\
  $^*$Corresponding author: `wangliang.f@gmail.com`
bibliography:
- references.bib
date: August 2026
title: |
  A Local Relative Gutzwiller Trace and a Certified Fast Branch\
  for a Clock-Preserving Hénon Schrödinger Pair
```

## Markdown 正文

# Introduction {#sec:introduction}

A self-adjoint operator, a prescribed mean counting law, and a nonzero-time periodic-orbit fluctuation are three different mathematical achievements. The first gives a real discrete spectrum. The second controls its averaged density. Only the third begins to expose geometry beyond the mean. Keeping these levels separate is especially important in Hilbert--Pólya-motivated model building, where a well-designed Weyl law can otherwise be mistaken for an arithmetic spectral mechanism.

This paper studies the local fluctuation problem for an explicit pair of semiclassical Schrödinger operators $$P_{a,\hbar}=-\frac{\hbar^2}{2}\Delta+
 2\pi\exp\!\left(\pi|\Psi_a(q)|^2\right),
 \qquad
 P_{0,\hbar}=-\frac{\hbar^2}{2}\Delta+2\pi e^{\pi|q|^2},
 \label{eq:intro-pair}$$ where $\Psi_a$ is a centered, determinant-one Hénon automorphism and the flagship parameter is $a=1.02$. The configuration change preserves area, so the two classical Hamiltonians have the same exact sublevel volume. That identity fixes a common mean clock but does not force the quantum spectra to coincide. The published deterministic-chaos study supplies the broader prime-distribution motivation [@Wang2026PrimeChaos], while the specific area-preserving Hénon/operator construction and the value $a=1.02$ were introduced in the subsequent Hénon preprint [@Wang2026HenonPreprint]. The present work asks a narrower question: can one isolate, with proofs and auditable numerical certificates, a nonzero-time relative spectral term belonging to a specific classical orbit?

The difficulty is not the formal Gutzwiller expression. Rigorous fixed-energy trace formulas are established [@DuistermaatGuillemin1975; @BrummelhuisUribe1991; @PaulUribe1995; @CombescureRalstonRobert1999]. The model-specific work is to verify that every stationary point allowed by the chosen time cutoff has been accounted for. A competing warped orbit, a radial family, a repeated return, or a transverse degeneracy would change the coefficient or invalidate the isolated-orbit formula. An inserted microlocal observable would make isolation easier, but it would also make the left-hand side depend on eigenfunctions. Our target is instead a finite-rank relative trace determined only by the two eigenvalue lists.

The central conclusion has two deliberately separate parts. Analytically, for each fixed sufficiently small positive energy excess $\delta=E-2\pi$, a blow-up of the complete energy shell leaves one primitive fast Lyapunov return in the positive-time window and no radial return. This produces an eigenvalue-only relative Gutzwiller coefficient. Quantitatively, a computer-assisted proof certifies the same distinguished local branch and its transverse determinant on $0\le\epsilon\le0.101$, where $\delta=\epsilon^2$. The second result now includes an independently checked exclusion of every other reduced root in the declared local box. It still does not quantify the small-energy threshold in the first result because the phase/flow-box and global return covers remain incomplete.

Our contributions are as follows.

1.  We express the energy-localized relative propagator trace as an ordinary finite sum and as an exact Stieltjes functional of the relative counting staircase. No first-resolvent trace-class assumption is needed.

2.  We compute the bottom normal form of the Hénon well, identify the fast Lyapunov family, and derive its limiting period, action slope, transverse determinant, and first nonlinear period coefficient. At $a=1.02$, $$T_+^0=0.6638439766792985,\qquad
     D_+^0=3.8627220445155035.$$

3.  We prove that there is a nonquantitative $\delta_{\rm tr}>0$ such that, for every fixed $0<\delta<\delta_{\rm tr}$, one primitive fast orbit supplies the positive-time relative trace term $$i\widehat g(T_+)\frac{T_+}{2\pi\sqrt{|\det(I-P_+)|}}
     e^{iS_+/\hbar}+O(\hbar).$$ The absence of an observable makes this coefficient recoverable from the two spectra alone.

4.  We certify one connected real-analytic primitive full-return branch, unique inside the frozen local boxes for $0\le\epsilon\le0.101$, by 51 primary slabs and 50 guarded bridges at each of 128 and 256 MPFR bits. The proof archive contains 202 successful validated-flow/Krawczyk jobs and 202 exact-rational Krawczyk replays.

5.  On that local branch, we prove the exact reduction $\det(I-D\Pi_\epsilon)=4-\operatorname{tr}M_\epsilon$ without assuming semisimplicity of the unit multipliers, and validate the uniform inequality $\det(I-D\Pi_\epsilon)>3$.

6.  We close the local root complement on all 51 slabs at 128 and 256 MPFR bits. The 102-tree archive contains 52,790 interval nodes, and an independent exact-rational replay completes 158,782 checks with zero failures. Together with the protected-box theorem, this gives pointwise reduced-root uniqueness throughout the frozen local box.

The numerical spectral calculation at $\delta=0.01$ is reported for a different purpose. Its finest normalized value, $1.0065230645+0.0133004473i$, is consistent with the analytic amplitude and phase convention. It is not evidence that $0.01<\delta_{\rm tr}$, because the latter inequality has not been proved. We retain the larger pre-asymptotic deviations in the same frozen ladder rather than fitting them away.

The evidence layers in [\[fig:architecture\]](#fig:architecture){reference-type="ref" reference="fig:architecture"} govern the language of the paper. We call an exact algebraic or functional-calculus statement an identity, a hand proof a theorem or proposition, the validated local result a computer-assisted theorem, and the frozen finite-dimensional computation a numerical diagnostic. The open arithmetic gate is not softened by any of these labels.

The paper is organized as follows. positions the result against fixed-energy trace formulas, Lyapunov families, relative spectral containers, and validated periodic-orbit continuation. build the exact spectral object and the bottom oracle. proves the nonquantitative one-orbit theorem. states and analyzes the explicit local-branch and monodromy certificates. reports the frozen spectral diagnostic, and [8](#sec:scope){reference-type="ref" reference="sec:scope"} records what is still absent from a Hilbert--Pólya route. The appendices give the proof and reproduction details.

# Related work and novelty boundary {#sec:related}

#### Wave traces and fixed-energy Schrödinger formulas.

The connection between wave-trace singularities and periodic bicharacteristics originates in the compact elliptic theory of @DuistermaatGuillemin1975. For Schrödinger operators on Euclidean space, energy localization and compact regular energy surfaces lead to fixed-energy semiclassical expansions; relevant formulations include @BrummelhuisUribe1991, the wave-packet approach of @PaulUribe1995, and the coherent-state derivation of @CombescureRalstonRobert1999. The last reference gives the isolated nondegenerate-orbit coefficient used here and explicitly accommodates smooth Schrödinger wells on compact energy surfaces below the limiting potential at infinity. Thus neither the general Gutzwiller coefficient nor the stationary-phase framework is new. Our contribution is to discharge its short-time hypotheses for one explicit exponential Hénon well, to subtract an equimeasurable radial reference, and to remove the microlocal observable without introducing unproved global long-time assumptions.

Continuous fixed sets require different bookkeeping from isolated orbits. Rotational symmetry can produce clean families whose contribution depends on the fixed-set dimension rather than the isolated-orbit determinant [@GuilleminUribe1989; @Cassanas2007]. This distinction matters because the reference well is radial. We avoid a mixed clean-family subtraction by selecting a positive-time interval in which the radial shell has no return at all. The result is consequently not a general relative trace formula between an integrable and a nonintegrable system; it is a local theorem tied to an audited time window.

#### Lyapunov families and nonlinear normal modes.

Hamiltonian normal modes near an elliptic equilibrium have a classical existence theory [@Weinstein1973]. We use the Lyapunov-centre criterion in the concrete form recorded by @AlligoodYorke1986: the selected imaginary pair is simple and the ratios of all other eigenvalues to it are not integers. These hypotheses are elementary to verify after the exact singular-value decomposition of the centered Hénon derivative. The model-specific content lies in the resulting closed formulas, the audited Poincaré--Lindstedt coefficient, and the global shrinking-shell argument that turns a local family into the only return below the chosen time bound. We do not claim a new Lyapunov-centre theorem.

#### Relative spectral objects.

Relative spectral-shift theory offers several containers for comparing two operators. Generalized spectral-shift functions can be defined under odd-resolvent-power trace-class hypotheses [@Yafaev2005], and Schatten criteria for functions of Schrödinger operators are developed in regimes such as those studied by @FrankPushnitski2019. The difference of the present exponential wells is unbounded in both relative directions, and we do not assert first-resolvent trace-class comparability. Instead, the compact energy cutoff makes each propagator trace finite rank. This simpler object has an exact representation through the two discrete counting functions and is sufficient for the fixed-energy orbit calculation. The trade-off is explicit: the theorem concerns a compact regular band and a fixed energy before $\hbar$ tends to zero.

#### Validated periodic-orbit continuation.

Interval Newton and Krawczyk operators are standard tools for enclosing nonlinear zeros [@Krawczyk1969; @Neumaier1990; @MooreKearfottCloud2009; @Rump2010]. Rigorous global search requires an exhaustive declared domain rather than one local inclusion [@Kearfott1996]. Validated integration has a longer IVP and wrapping-control lineage [@Lohner1987; @NedialkovJacksonCorliss1999], and $C^1$ integration controls both the flow and first variations [@Zgliczynski2002]. CAPD::DynSys implements rigorous flows, variational equations, parameters, and Poincaré maps [@KapelaMrozekWilczakZgliczynski2021; @KapelaWilczakZgliczynski2022]. There is direct prior art for coupling validated Poincaré maps with parameter-uniform interval Newton tests to continue locally unique elliptic periodic-orbit branches [@WilczakZgliczynski2009; @BarrioRodriguez2014; @WilczakBarrio2017]. Accordingly, CAPD plus Krawczyk continuation is not presented as a methodological novelty.

The proof architecture here adds model-specific layers that those citations cannot supply: the exact harmonic anchor, the reduced four-equation return system, recovery of the omitted coordinate from energy monotonicity, guarded bridges that identify 51 primary cells, a separate primitive-period argument, and an invariant-quotient proof of the determinant identity. The software produces validated flow and derivative enclosures; the return formulation, interval inclusion, and analytic arguments together prove the stated local orbit theorem. Moreover, local Krawczyk uniqueness is not global uniqueness. The A4.12 inclusion certificate by itself left the complement of the protected boxes open. The separate A4.15 exhaustive cover now excludes that complement inside the declared reduced box $B_{\mathrm{loc}}$ on every frozen slab, as stated in [\[thm:all-slab-complement\]](#thm:all-slab-complement){reference-type="ref" reference="thm:all-slab-complement"}. It does not cover the missing phase, flow-box, full energy shell, or global phase space.

#### Proof objects and reproducibility.

The producer uses correctly rounded MPFR arithmetic, whose implementation and semantics are documented by @FousseEtAl2007. General reproducibility guidance motivates publishing code, data, versions, and tests [@StoddenEtAl2016]. IEEE floating-point and interval-arithmetic standards provide relevant normative vocabulary [@IEEE7542019; @IEEE1788_2015], but we do not claim conformance without a separate conformance audit. Our exact-decimal protocol goes beyond those generic statements but is not advertised as an external standard: stored outward endpoints are parsed as exact rationals, and independent scripts replay the finite Krawczyk and determinant inequalities. These scripts do not independently integrate the ODE. The two precision runs are a strong implementation-consistency check, not two logically unrelated proofs.

#### Hilbert--Pólya boundary.

Periodic-orbit formulas have long motivated comparisons between quantum spectra and arithmetic explicit formulas [@Gutzwiller1971]. The author's preceding deterministic-chaos study provides programme-level prime-distribution motivation [@Wang2026PrimeChaos]; the Hénon preprint supplies the specific $a=1.02$ map/operator proposal [@Wang2026HenonPreprint]. The present theorem does not derive periods $r\log p$, von-Mangoldt weights, an Euler product, or zeta zeros. An isolated local orbit term is a necessary kind of structure for a dynamical trace programme, but it is not an arithmetic explicit formula. Within the audited primary-source corpus, we found no direct treatment of this exponential equimeasurable Hénon pair and its certified near-bottom branch. This is a scoped literature-search conclusion, not an absolute priority claim.

::: {#tab:prior-boundary}
  Ingredient                   Use in this paper                          What is not inherited from the citation
  ---------------------------- ------------------------------------------ --------------------------------------------------------------------
  Fixed-energy trace formula   Isolated-orbit coefficient at fixed $E$    Short-time orbit census and nondegeneracy for this well
  Lyapunov-centre theory       Existence of the fast local family         Whole-shell uniqueness and quantitative continuation
  Krawczyk/interval Newton     One root in each frozen box                Full return, primitivity, bridge identity, or complement exclusion
  Validated $C^1$ flow         Enclosures of state and variational flow   Correctness of this vector field, build, or release archive
  Exact-rational replay        Audit of stored finite inequalities        Independent regeneration of the ODE enclosures

  : Prior tools and the model-specific work performed here. The final column is a boundary, not a weakness hidden in the proof.
:::

# The model and the exact relative spectral object {#sec:model-trace}

## Centered Hénon geometry

For $a>-1$, let $$r_a=\frac{1}{1+\sqrt{1+a}},
 \qquad
 c_a=2ar_a=2(\sqrt{1+a}-1).
 \label{eq:ra-ca}$$ Translating the positive fixed point $(r_a,r_a)$ of the area-preserving Hénon map gives the centered polynomial automorphism $$\Psi_a(x,y)=(-c_ax-ax^2-y,x).
 \label{eq:centered-henon}$$ Its inverse and derivative are $$\Psi_a^{-1}(u,v)=(v,-c_av-av^2-u),
 \qquad
 D\Psi_a(x,y)=
 \begin{pmatrix}-c_a-2ax&-1\\1&0\end{pmatrix}.
 \label{eq:henon-inverse-jac}$$ In particular, $\det D\Psi_a=1$. At $a=0$, $\Psi_0(x,y)=(-y,x)$, so $|\Psi_0(q)|=|q|$.

Define $$V_a(q)=2\pi\exp\!\left(\pi|\Psi_a(q)|^2\right),
 \qquad
 h_a(q,p)=\frac{|p|^2}{2}+V_a(q),
 \label{eq:potential-hamiltonian}$$ and let $P_{a,\hbar}$ be the Friedrichs realization on $L^2(\mathbb{R}^2)$ of $$P_{a,\hbar}=-\frac{\hbar^2}{2}\Delta+V_a.
 \label{eq:semiclassical-operator}$$ Properness of the polynomial automorphism implies $V_a(q)\to\infty$ as $|q|\to\infty$. The quadratic form is therefore closed below after completion, and its Friedrichs operator has compact resolvent. We write its eigenvalues, repeated with multiplicity, as $\lambda_{a,k}(\hbar)$.

[\[prop:regular-shells\]]{#prop:regular-shells label="prop:regular-shells"} For every $a>-1$, the Hamiltonian $h_a$ has one critical point, $(q,p)=(0,0)$, at energy $2\pi$. Every $E>2\pi$ is a regular value, the surface $h_a^{-1}(E)$ is compact, and the flow is complete on compact energy bands.

Differentiation gives $$\nabla V_a(q)=2\pi V_a(q)D\Psi_a(q)^T\Psi_a(q).$$ The derivative of $\Psi_a$ is invertible, and $\Psi_a(q)=0$ only for $q=0$. Thus $V_a$ has one critical point. The momentum derivative of $h_a$ is $p$, proving the critical-point assertion. Properness gives compact sublevels, and a smooth vector field confined to a compact energy band is complete.

## The exact common classical clock

At a fixed configuration point, the momentum disk below energy $E$ has area $2\pi(E-V_a(q))_+$. The determinant-one change $u=\Psi_a(q)$ then gives the following exact identity.

[\[prop:shell-volume\]]{#prop:shell-volume label="prop:shell-volume"} For $E\ge2\pi$, $$\begin{aligned}
 \operatorname{vol}\{h_a<E\}
 &=2\pi E\log\frac{E}{2\pi}-2\pi E+4\pi^2,
 \label{eq:phase-volume}\\
 \int_{h_a=E}\frac{\,\mathrm{d}\Sigma}{|\nabla h_a|}
 &=2\pi\log\frac{E}{2\pi}.
 \label{eq:shell-measure}\end{aligned}$$ Both quantities are independent of $a$.

Using $u=\Psi_a(q)$, polar coordinates, and $R(E)^2=\pi^{-1}\log(E/2\pi)$, one obtains $$\begin{aligned}
 \operatorname{vol}\{h_a<E\}
 &=2\pi\int_{|u|<R(E)}(E-2\pi e^{\pi|u|^2})\,\mathrm{d}u\\
 &=4\pi^2\int_0^{R(E)}(E-2\pi e^{\pi r^2})r\,\mathrm{d}r,\end{aligned}$$ which evaluates to [\[eq:phase-volume\]](#eq:phase-volume){reference-type="ref" reference="eq:phase-volume"}. Differentiating with respect to the regular energy gives [\[eq:shell-measure\]](#eq:shell-measure){reference-type="ref" reference="eq:shell-measure"} by the coarea formula.

The adjective *clock-preserving* refers only to [\[eq:phase-volume,eq:shell-measure\]](#eq:phase-volume,eq:shell-measure){reference-type="ref" reference="eq:phase-volume,eq:shell-measure"} and the associated mean Weyl terms. It does not assert a unitary equivalence. The configuration change does not preserve the Euclidean kinetic energy, and the two quantum spectra need not agree.

## Finite-rank relative wave trace

Let $N_{a,\hbar}(E)$ and $N_{0,\hbar}(E)$ be the two counting functions and fix the sign convention $$\xi_\hbar(E)=N_{0,\hbar}(E)-N_{a,\hbar}(E).
 \label{eq:relative-staircase}$$ Choose $\chi\in C_c^\infty((2\pi,\infty);\mathbb{R})$. Since both operators have compact resolvent, $\chi(P_{j,\hbar})$ has finite rank. Thus $$W_{\mathrm{rel},\hbar}^{\chi}(t)
 =\operatorname{Tr}\!\left[
 \chi(P_{a,\hbar})^2e^{-itP_{a,\hbar}/\hbar}
 -\chi(P_{0,\hbar})^2e^{-itP_{0,\hbar}/\hbar}
 \right]
 \label{eq:relative-wave}$$ is an ordinary finite sum for every $t$, rather than a regularized difference of two divergent traces.

[\[prop:staircase-identity\]]{#prop:staircase-identity label="prop:staircase-identity"} The finite-rank trace satisfies $$\boxed{
 W_{\mathrm{rel},\hbar}^{\chi}(t)
 =\int_\mathbb{R}
 \left[(\chi^2)'(E)-\frac{it}{\hbar}\chi(E)^2\right]
 e^{-itE/\hbar}\xi_\hbar(E)\,\mathrm{d}E.}
 \label{eq:staircase-wave}$$ In particular, it is determined by the two eigenvalue lists.

For $f_t(E)=\chi(E)^2e^{-itE/\hbar}$, spectral calculus gives $W_{\mathrm{rel},\hbar}^{\chi}(t)=\int f_t\,\mathrm{d}(N_{a,\hbar}-N_{0,\hbar})$. Since $f_t$ is compactly supported, Stieltjes integration by parts and $N_a-N_0=-\xi_\hbar$ give $\int f_t'(E)\xi_\hbar(E)\,\mathrm{d}E$, which is exactly [\[eq:staircase-wave\]](#eq:staircase-wave){reference-type="ref" reference="eq:staircase-wave"}.

We freeze the Fourier convention $$\widehat g(t)=\int_\mathbb{R}e^{-its}g(s)\,\mathrm{d}s,
 \qquad
 g(s)=\frac{1}{2\pi}\int_\mathbb{R}e^{its}\widehat g(t)\,\mathrm{d}t.
 \label{eq:fourier-convention}$$ For $g\in\mathcal{S}(\mathbb{R})$, define the energy-localized relative density $$\begin{aligned}
 \rho_{\mathrm{rel},\hbar}(E;g)
 =\operatorname{Tr}\!\bigg[&\chi(P_{a,\hbar})^2
 g\!\left(\frac{E-P_{a,\hbar}}{\hbar}\right)\notag\\
 &-\chi(P_{0,\hbar})^2
 g\!\left(\frac{E-P_{0,\hbar}}{\hbar}\right)\bigg].
 \label{eq:relative-density}\end{aligned}$$ Fourier inversion yields the exact relation $$\boxed{
 \rho_{\mathrm{rel},\hbar}(E;g)
 =\frac{1}{2\pi}\int_\mathbb{R}
 \widehat g(t)e^{itE/\hbar}W_{\mathrm{rel},\hbar}^{\chi}(t)\,\mathrm{d}t.}
 \label{eq:density-wave}$$ If $0\notin\operatorname{supp}\widehat g$, every distribution supported only at zero time is removed exactly. This support condition is stronger than seeking a numerical cancellation of the two large zero-time contributions.

## Hypotheses still needed for a one-orbit formula

For a fixed regular energy, the periodic-orbit trace theorem requires a compact energy band, a finite collection of geometric periodic orbits modulo time translation over the Fourier time support, transverse nondegeneracy of each orbit, and a convention for action and Maslov phase [@CombescureRalstonRobert1999]. records how the later sections discharge these assumptions. The table also shows why the quantitative branch certificate is not, by itself, the trace theorem: local existence inside selected boxes does not exclude other roots in their complement.

::: {#tab:trace-hypotheses}
  Requirement                     Model-specific discharge                                                       Domain/status
  ------------------------------- ------------------------------------------------------------------------------ -----------------------------------------------------------
  Compact regular band                                                                                           Every fixed $E>2\pi$
  No radial return                Radial blow-up and period bound                                                Small $\delta$; one component explicit through $0.010201$
  Complete warped return census   Whole-shell blow-up, limiting return classification, and Poincaré uniqueness   $0<\delta<\delta_*$, $\delta_*>0$ nonquantitative
  Transverse nondegeneracy        Harmonic limit and continuation                                                $0<\delta<\delta_{\rm nd}$, threshold nonquantitative
  No zero-time term               $0\notin\operatorname{supp}\widehat g$                                         Exact support statement
  Observable-free spectral side   Set the symbol equal to one after the complete short-time census               Eigenvalue-only finite-rank trace

  : Hypotheses for the eigenvalue-only fixed-energy trace and their authorized domains.
:::

# Bottom normal form and the fast Lyapunov oracle {#sec:normal-form}

The unique equilibrium in [\[prop:regular-shells\]](#prop:regular-shells){reference-type="ref" reference="prop:regular-shells"} is elliptic. Its exact linear structure both selects the orbit used in the trace and supplies analytic limits against which the validated computation can be audited.

## Singular values, frequencies, and periods

At the origin, $$A_a=D\Psi_a(0)=
 \begin{pmatrix}-c_a&-1\\1&0\end{pmatrix},
 \qquad
 D^2V_a(0)=4\pi^2A_a^TA_a.
 \label{eq:bottom-hessian}$$ Let $0<s_-<s_+$ be the singular values of $A_a$. Since $\det A_a=1$, direct diagonalization gives $$s_+s_-=1,
 \qquad
 s_\pm=\frac{\sqrt{c_a^2+4}\pm|c_a|}{2}.
 \label{eq:singular-values}$$ In orthonormal configuration coordinates $(Q_-,Q_+)$ aligned with the eigenvectors of $A_a^TA_a$, the quadratic Hamiltonian is $$K_0=\frac12\left(P_-^2+\omega_-^2Q_-^2
                      +P_+^2+\omega_+^2Q_+^2\right),
 \qquad \omega_\pm=2\pi s_\pm.
 \label{eq:harmonic-normal-form}$$ We use the signs to label frequency, so the fast mode is $+$. Its period and the slow period are $$T_+^0=s_+^{-1}=s_-,
 \qquad
 T_-^0=s_-^{-1}=s_+.
 \label{eq:linear-periods}$$ Set $$\rho_a=\frac{\omega_+}{\omega_-}=\frac{s_+}{s_-}=s_+^2>1.
 \label{eq:frequency-ratio}$$

[\[prop:lyapunov-branch\]]{#prop:lyapunov-branch label="prop:lyapunov-branch"} For every $a>-1$, $a\ne0$, a periodic family $\gamma_+(E)$ emanates from the fast normal mode as $E\downarrow2\pi$. It can be parameterized by every sufficiently small positive energy excess, and $$T_+(E)\longrightarrow T_+^0.
 \label{eq:period-limit}$$ The reduced transverse multipliers tend to $e^{\pm2\pi i/\rho_a}$, so the family is transversally nondegenerate for all sufficiently small positive excesses. Moreover, $$\begin{aligned}
 D_+^0
 &:=\lim_{E\downarrow2\pi}|\det(I-P_+(E))|
 =4\sin^2\frac{\pi}{\rho_a},
 \label{eq:det-limit}\\
 S_+(E)
 &:=\oint_{\gamma_+(E)}p\,\mathrm{d}q
 =T_+^0(E-2\pi)+o(E-2\pi).
 \label{eq:action-limit}\end{aligned}$$

The linearized Hamiltonian vector field has the two simple pairs $\pm i\omega_-$ and $\pm i\omega_+$. For the fast pair, the other frequency ratios are $\pm\omega_-/\omega_+=\pm1/\rho_a\notin\mathbb Z$. The Lyapunov-centre theorem therefore produces a one-parameter family [@AlligoodYorke1986; @Weinstein1973]. If $A$ is the fast normal-coordinate amplitude, then $E(A)-2\pi=\tfrac12\omega_+^2A^2+O(A^3)>0$ for small $A>0$, so energy indexes the positive branch. The multiplier and determinant limits follow from the slow rotation during one fast period. Finally, the standard action identity $\,\mathrm{d}S_+/\,\mathrm{d}E=T_+$, with $S_+(2\pi)=0$, gives [\[eq:action-limit\]](#eq:action-limit){reference-type="ref" reference="eq:action-limit"}.

## First nonlinear period coefficient

The leading harmonic limits are insufficient to audit a finite positive energy. Let $$C_{ijk}=\partial_{Q_iQ_jQ_k}V_a(0),
 \qquad
 D_{ijkl}=\partial_{Q_iQ_jQ_kQ_l}V_a(0)
 \label{eq:tensors}$$ in the fixed orthonormal normal-coordinate convention. Define, for $j\in\{-,+\}$, $$b_{j0}=-\frac{C_{++j}}{4\omega_j^2},
 \qquad
 b_{j2}=-\frac{C_{++j}}{4(\omega_j^2-4\omega_+^2)},
 \label{eq:b-coefficients}$$ and $$\nu_+=\frac{1}{2\omega_+}
 \left[
 \frac{D_{++++}}{8}
 +\sum_{j\in\{-,+\}}C_{++j}
 \left(b_{j0}+\frac12b_{j2}\right)
 \right].
 \label{eq:nu-plus}$$

[\[prop:period-slope\]]{#prop:period-slope label="prop:period-slope"} With the tensors and coordinates above, $$\left.\frac{\,\mathrm{d}T_+}{\,\mathrm{d}E}\right|_{2\pi+}
 =-\frac{2T_+^0\nu_+}{\omega_+^3}.
 \label{eq:period-slope}$$ For $a=1.02$, the deterministic coordinate convention gives $\nu_+=17.52709598189346$ and hence $$\begin{aligned}
 T_+(2\pi+\delta)
 &=0.6638439766792985
   -0.0274450756283701\,\delta+o(\delta),
 \label{eq:period-expansion}\\
 \frac{S_+(2\pi+\delta)}{\delta}
 &=0.6638439766792985
   -0.0137225378141851\,\delta+o(\delta).
 \label{eq:action-expansion}\end{aligned}$$

The proof is a Poincaré--Lindstedt solvability calculation. Its key point is that the constant and second harmonics induced at order $A^2$ feed the resonant $A^3\cos\tau$ equation. Omitting that feedback changes the period slope. We give the calculation in [11](#app:nonlinear-period){reference-type="ref" reference="app:nonlinear-period"}.

## Numerical specialization at $a=1.02$

The exact formulas give $$T_+^0=0.6638439766792985,
 \qquad
 T_-^0=1.5063780573896775,
 \qquad
 D_+^0=3.8627220445155035.
 \label{eq:oracle-numbers}$$ In particular, $$T_+^0<0.75<\min(2T_+^0,T_-^0).
 \label{eq:window-separation}$$ This strict ordering is the limiting return classification behind the whole-shell theorem in [5](#sec:analytic-trace){reference-type="ref" reference="sec:analytic-trace"}. The limiting geometric amplitude is $$\frac{T_+^0}{\sqrt{D_+^0}}=0.3377686126427769,
 \qquad
 \frac{T_+^0}{2\pi\sqrt{D_+^0}}=0.0537575443233896,
 \label{eq:limiting-amplitudes}$$ where the second value matches the Fourier normalization in [\[eq:fourier-convention\]](#eq:fourier-convention){reference-type="ref" reference="eq:fourier-convention"}.

A nonvalidated continuation run at six positive excesses served as a formula and convention audit. The extrapolated values and analytic oracles are shown in [3](#tab:r400-oracle){reference-type="ref" reference="tab:r400-oracle"}. These comparisons do not prove the branch or the trace theorem; those statements come from the analytic and validated arguments below.

::: {#tab:r400-oracle}
  Quantity                                                   Fitted            Analytic    Absolute difference
  --------------------------------------------- ------------------- ------------------- ----------------------
  $T_+^0$                                         0.663843973386761   0.663843976679299    $3.29\times10^{-9}$
  $\,\mathrm{d}T_+/\,\mathrm{d}E$                  -0.0274445154485    -0.0274450756284    $5.60\times10^{-7}$
  $\lim S/\delta$                                 0.663843975854219   0.663843976679299   $8.25\times10^{-10}$
  $\,\mathrm{d}(S/\delta)/\,\mathrm{d}\delta$      -0.0137223974763    -0.0137225378142    $1.40\times10^{-7}$
  $D_+^0$                                          3.86272204305148    3.86272204451550    $1.46\times10^{-9}$

  : Small-energy continuation audit. "Fitted" means a deterministic extrapolation of the archived nonvalidated orbit data; the analytic column is independent of the fit.
:::

# The analytic one-orbit theorem at nonquantitative small energy {#sec:analytic-trace}

We now isolate the fast branch in the time window $(0,0.75]$. The proof has three parts: remove radial returns, classify all warped returns on the complete shrinking shell, and specialize the fixed-energy trace formula. The resulting energy threshold is positive but not numerically bounded.

## Radial exclusion

Write $E=2\pi+\delta$. For the radial Hamiltonian, rescale $q=\sqrt\delta Q$ and $p=\sqrt\delta P$. The energy shell becomes $$K_\delta^{\rm rad}(Q,P)
 =\frac{|P|^2}{2}
 +\frac{2\pi}{\delta}\left(e^{\pi\delta|Q|^2}-1\right)=1.
 \label{eq:radial-blowup}$$ Because $e^x-1\ge x$, all such shells lie in a common compact set. Their vector fields converge in $C^1$ to $$F_0(Q,P)=(P,-4\pi^2Q),
 \label{eq:radial-limit-field}$$ the isotropic oscillator of period one.

[\[prop:radial-exclusion\]]{#prop:radial-exclusion label="prop:radial-exclusion"} For every $T_{\max}<1$, there is $\bar\delta(T_{\max})>0$ such that the radial shell $h_0=2\pi+\delta$, $0<\delta<\bar\delta(T_{\max})$, has no return with $0<|T|\le T_{\max}$.

If a contradicting sequence has $\delta_n\downarrow0$ and return times bounded away from zero, compactness and flow convergence give a nonzero return of [\[eq:radial-limit-field\]](#eq:radial-limit-field){reference-type="ref" reference="eq:radial-limit-field"} before time one. If instead $T_n\to0$, then $$0=\frac{1}{T_n}\int_0^{T_n}
 F_{\delta_n}(\Phi_{\delta_n}^s(Z_n))\,\mathrm{d}s
 \longrightarrow F_0(Z_*),$$ which is impossible on the normalized energy-one shell. Both alternatives contradict the assumed returns.

The radial part alone can also be made quantitative. If $\|\nabla^2V\|_{\rm op}\le L$ on a convex domain containing a periodic trajectory, the periodic Wirtinger inequality gives $T\ge2\pi/\sqrt L$. On the radial shells through $\delta=0.010201$, this yields $$T_{\rm radial}>
 \frac{2\pi}{\sqrt{(2\pi+0.010201)(2\pi+0.020402)}}
 >0.99.
 \label{eq:radial-explicit-bound}$$ Thus $\bar\delta(0.75)\ge0.010201$. This explicit bound controls only the radial factor in the eventual minimum defining $\delta_{\rm tr}$.

## Complete-shell warped return classification

For the Hénon well, put $\epsilon=\sqrt\delta$, $q=\epsilon Q$, $p=\epsilon P$, and $$K_\epsilon(Q,P)
 =\frac{h_a(\epsilon Q,\epsilon P)-2\pi}{\epsilon^2}.
 \label{eq:normalized-hamiltonian}$$ The exact decomposition $$\Psi_a(\epsilon Q)
 =\epsilon(A_aQ+\epsilon B_a(Q)),
 \qquad B_a(Q)=(-aQ_x^2,0),
 \label{eq:normalized-henon}$$ gives $$K_\epsilon
 =\frac{|P|^2}{2}
 +\frac{2\pi}{\epsilon^2}
 \left[e^{\pi\epsilon^2|A_aQ+\epsilon B_a(Q)|^2}-1\right].
 \label{eq:normalized-k}$$ The apparent singularity at $\epsilon=0$ is removable, and the extension has the harmonic value [\[eq:harmonic-normal-form\]](#eq:harmonic-normal-form){reference-type="ref" reference="eq:harmonic-normal-form"}. The rescaling leaves physical time unchanged.

[\[thm:whole-shell\]]{#thm:whole-shell label="thm:whole-shell"} Fix $a=1.02$. There exists $\delta_*>0$ such that, for every $0<\delta<\delta_*$, $$h_a(z)=2\pi+\delta,\qquad 0<T\le0.75,\qquad \Phi_a^T(z)=z
 \label{eq:short-return-system}$$ holds if and only if $z$ lies on the fast Lyapunov orbit $\gamma_+(2\pi+\delta)$ and $T=T_+(2\pi+\delta)$. This return is primitive, and the geometric orbit is unique modulo time translation.

The proof must control the complete shell, not only a shooting tube. The original energy equation gives $$|p|\le\sqrt2\epsilon,\qquad
 |\Psi_a(q)|^2\le\frac1\pi
 \log\left(1+\frac{\epsilon^2}{2\pi}\right).$$ Using the exact inverse in [\[eq:henon-inverse-jac\]](#eq:henon-inverse-jac){reference-type="ref" reference="eq:henon-inverse-jac"} shows $|q|=O(\epsilon)$ uniformly on the entire shell. Hence the normalized shells $\Sigma_\epsilon=\{K_\epsilon=1\}$ lie in a common compact set and the vector fields converge in $C^1$ on a neighborhood of them.

Any sequence of returns with $\epsilon_n\downarrow0$ and $0<T_n\le0.75$ has a convergent subsequence. The averaged-vector-field argument excludes $T_n\to0$. At a positive limiting time, the harmonic classification [\[eq:window-separation\]](#eq:window-separation){reference-type="ref" reference="eq:window-separation"} forces $T_n\to T_+^0$ and the limiting state onto the fast phase circle.

At the positive fast turning point, use the local section $$\mathcal{S}_\epsilon=\{K_\epsilon=1,\ P_+=0,\ Q_+>0\}.$$ The energy gradient and event slope are nonzero at $\epsilon=0$. In normalized slow coordinates, the derivative of the limiting return map is the rotation $R_{2\pi/\rho_a}$, so $$\det(I-D\Pi_0)=4\sin^2(\pi/\rho_a)>0.$$ The implicit-function theorem gives one local fixed point. A proper iterate would converge to a fractional return of the fast harmonic circle, which is impossible; thus the nearby return is primitive. Finally, a hypothetical second sequence of orbits converges uniformly, after phase alignment, to the fast circle. Transverse $C^1$ convergence gives exactly one oriented crossing of a sufficiently small section neighborhood per primitive circuit; that crossing is consequently a fixed point of the local first-return map and contradicts local uniqueness. gives the detailed compactness, crossing-stability, iterate, and globalization steps.

The explicit warped Hessian estimate gives a useful but weaker quantitative fact. Every warped orbit for $0<\delta\le0.010201$ lies in $|x|<0.02274$, $|y|<0.042427$, where $\|\nabla^2V_a\|_{\rm op}<103$. Therefore $$T_{\rm warped}>\frac{2\pi}{\sqrt{103}}>0.60.
 \label{eq:warped-period-floor}$$ This period floor reduces a future exhaustive cover to $[0.60,0.75]$; it does not exclude additional returns in that interval and does not quantify $\delta_*$.

## Finite-time trace localization

The trace integral [\[eq:density-wave\]](#eq:density-wave){reference-type="ref" reference="eq:density-wave"} only samples the time support of $\widehat g$. The following finite-time form of the fixed-energy theorem is the precise bridge we need.

[\[lem:finite-time-crr\]]{#lem:finite-time-crr label="lem:finite-time-crr"} Suppose $\operatorname{supp}\widehat g\subset[-T_0,T_0]$, the energy is regular and compactly localized, the geometric periodic orbits with $0<|T_\gamma|\le T_0$ form a finite collection modulo time translation, and every such orbit is transversally nondegenerate. Equivalently, at a relevant period the associated flow-orbit component of the fixed set is clean in the transverse directions. Then the nondegenerate-orbit expansion of @CombescureRalstonRobert1999 requires no hypothesis on returns with $|t|>T_0$.

In the coherent-state proof, the time variable is integrated against $\widehat g(t)$. The integrand vanishes identically outside its support. Periodic-orbit discreteness modulo the flow direction and the transverse stationary-phase reductions are therefore invoked only for $|t|\le T_0$. The remaining symbol and regular-energy hypotheses are unchanged. This is a support restriction of the proof, not a new long-time trace formula.

Set $$\delta_{\rm tr}
 =\min\{\delta_*,\bar\delta(0.75),\delta_{\rm nd}\},
 \label{eq:delta-tr}$$ where $\delta_{\rm nd}>0$ is a sufficiently small transverse- nondegeneracy threshold from [\[prop:lyapunov-branch\]](#prop:lyapunov-branch){reference-type="ref" reference="prop:lyapunov-branch"}. Both $\delta_*$ and $\delta_{\rm nd}$ are positive but currently nonquantitative.

[\[thm:relative-gutzwiller\]]{#thm:relative-gutzwiller label="thm:relative-gutzwiller"} Fix $0<\delta<\delta_{\rm tr}$ and put $E=2\pi+\delta$. Choose $\chi\in C_c^\infty(\mathbb{R};\mathbb{R})$, equal to one near $E$, with support in a small compact regular band. Let $$\widehat g\in C_c^\infty((0,0.75)),
 \qquad
 \operatorname{supp}\widehat g\ \text{concentrated near }T_+(E),
 \qquad
 \widehat g(T_+(E))\ne0.
 \label{eq:g-choice}$$ Then, with the Fourier convention [\[eq:fourier-convention\]](#eq:fourier-convention){reference-type="ref" reference="eq:fourier-convention"}, $$\boxed{
 \rho_{\mathrm{rel},\hbar}(E;g)
 =i\widehat g(T_+(E))
 \frac{T_+(E)}{2\pi\sqrt{|\det(I-P_+(E))|}}
 e^{iS_+(E)/\hbar}
 +O_{\delta,\chi,g}(\hbar).}
 \label{eq:main-trace-formula}$$ The left-hand side is determined only by the eigenvalue lists of $P_{a,\hbar}$ and $P_{0,\hbar}$.

Fix $\delta$ first and then let $\hbar\downarrow0$. By [\[thm:whole-shell\]](#thm:whole-shell){reference-type="ref" reference="thm:whole-shell"}, the warped flow has one primitive geometric orbit in the Fourier time range; by [\[prop:radial-exclusion\]](#prop:radial-exclusion){reference-type="ref" reference="prop:radial-exclusion"}, the radial flow has none. Transverse nondegeneracy holds after taking the minimum in [\[eq:delta-tr\]](#eq:delta-tr){reference-type="ref" reference="eq:delta-tr"}. and the confinement of the well verify the regular compact energy hypotheses. Apply [\[lem:finite-time-crr\]](#lem:finite-time-crr){reference-type="ref" reference="lem:finite-time-crr"} separately to the warped and radial traces and subtract.

The single-orbit positive-time coefficient in the project Fourier convention is $$\widehat g(T_+)
 \frac{T_+}{2\pi\sqrt{|\det(I-P_+)|}}
 e^{i(S_+/\hbar+\pi\sigma_+^{\rm CRR}/2)}.$$ The exact harmonic trace fixes $e^{i\pi\sigma_+^{\rm CRR}/2}=i$; nondegenerate continuation keeps this phase constant. Because no microlocal observable occurs, the exact identities in [\[prop:staircase-identity\]](#prop:staircase-identity){reference-type="ref" reference="prop:staircase-identity"} apply and make the spectral side eigenvalue-only.

[\[rem:quantifier-order\]]{#rem:quantifier-order label="rem:quantifier-order"} The theorem states: first choose a fixed $0<\delta<\delta_{\rm tr}$, then choose the cutoffs, and finally let $\hbar\to0$. It does not state a uniform joint limit $(\delta,\hbar)\to(0,0)$.

At the harmonic limit, the Abel-regularized transverse sum is $$\sum_{m\ge0}e^{-i(2\pi/\rho_a)(m+1/2)}
 =-\frac{i}{2\sin(\pi/\rho_a)}.$$ Poisson summation in the fast quantum number supplies $-1/\omega_+=-T_+^0/(2\pi)$. Their product has positive phase $+i$ after the positive determinant factor is removed. This also locks the single factor $T_+/(2\pi)$: multiplying by another period would double count the longitudinal orbit measure.

Nothing in [\[thm:relative-gutzwiller\]](#thm:relative-gutzwiller){reference-type="ref" reference="thm:relative-gutzwiller"} identifies a prime. Its return period varies smoothly from $0.6638\ldots$, whereas an arithmetic explicit formula would require an endogenous family organized by prime powers and the corresponding amplitudes. We return to this distinction in [8](#sec:scope){reference-type="ref" reference="sec:scope"}.

# Certified local branch and transverse stability {#sec:certified-branch}

The analytic theorem supplies a positive but unspecified energy interval. This section asks a separate quantitative question: can the distinguished fast branch itself be enclosed over a visible range of the blow-up parameter? The answer is yes, locally in frozen root boxes. The certificate does not exclude other returns elsewhere on the energy shell, so it cannot replace [\[thm:whole-shell\]](#thm:whole-shell){reference-type="ref" reference="thm:whole-shell"} on an explicit interval.

## Reduced return equations

Fix $$a=\frac{51}{50},
 \qquad 0\le\epsilon\le0.101,
 \qquad \delta=\epsilon^2,
 \label{eq:validated-domain}$$ and use the normalized Hamiltonian [\[eq:normalized-k\]](#eq:normalized-k){reference-type="ref" reference="eq:normalized-k"}. After the fixed orthogonal normal-coordinate change, take $$x=(Q_-,Q_+,P_-,T),
 \qquad
 z_0(x)=(Q_-,Q_+,P_-,0).
 \label{eq:shooting-unknowns}$$ The validated residual is $$F(x,\epsilon)=
 \begin{pmatrix}
 K_\epsilon(z_0)-1\\
 Q_-(T)-Q_-\\
 P_-(T)-P_-\\
 P_+(T)
 \end{pmatrix}.
 \label{eq:validated-residual}$$ The first row fixes energy and the last row imposes the return to the event hyperplane $P_+=0$. The equation $Q_+(T)=Q_+(0)$ is recovered analytically below rather than added as a fifth equation.

For a root box $X$, parameter interval $E_\epsilon$, center $\bar x$, and numerical preconditioner $C$, define the parameterized Krawczyk image $$\mathcal{K}(X,E_\epsilon)=
 \bar x-CF(\bar x,E_\epsilon)
 +\bigl(I-C[D_xF(X,E_\epsilon)]\bigr)(X-\bar x).
 \label{eq:krawczyk-operator}$$ Every accepted job proves both $$\mathcal{K}(X,E_\epsilon)\Subset X,
 \qquad
 \|I-C[D_xF(X,E_\epsilon)]\|_\infty<1.
 \label{eq:krawczyk-gates}$$ Under the validated residual and full-box Jacobian enclosures, these gates give one zero in $X$ for every fixed parameter in the slab [@Krawczyk1969; @MooreKearfottCloud2009]. The energy row is evaluated on the complete root box; in particular, $$_{0,2}=X_{P_-},
 \label{eq:energy-jacobian-row}$$ not the zero derivative obtained from the midpoint $P_-=0$.

## Branch theorem

[\[thm:validated-branch\]]{#thm:validated-branch label="thm:validated-branch"} For the parameter range [\[eq:validated-domain\]](#eq:validated-domain){reference-type="ref" reference="eq:validated-domain"}, there is a real-analytic family of nonconstant primitive periodic orbits $$\epsilon\longmapsto
 \gamma_\epsilon=
 (Q_-(\epsilon),Q_+(\epsilon),P_-(\epsilon),0;T(\epsilon))
 \label{eq:validated-family}$$ on $K_\epsilon=1$, with $$0.66<T(\epsilon)<0.67.
 \label{eq:validated-period-box}$$ For each of the 51 primary parameter slabs, this branch is the unique zero inside the corresponding frozen root box. The 50 guarded bridge hulls identify adjacent representatives as one branch. At $\epsilon=0$, it is anchored to the exact fast harmonic orbit.

Validated $C^1$ flow integration encloses the residual and the full Jacobian in [\[eq:validated-residual\]](#eq:validated-residual){reference-type="ref" reference="eq:validated-residual"}; each primary and bridge job passes [\[eq:krawczyk-gates\]](#eq:krawczyk-gates){reference-type="ref" reference="eq:krawczyk-gates"}. For adjacent primary slabs with overlap $B_i$, the guarded bridge box is the rationally padded hull $$Y_i=\operatorname{hull}(X_i\cup X_{i+1})
       +[-10^{-18},10^{-18}]^4.
 \label{eq:bridge-hull}$$ Both primary zeros lie in $Y_i$, and its Krawczyk certificate gives only one zero for each parameter in $B_i$. Induction over the 50 overlaps identifies all 51 pieces.

At every root, the archived enclosures prove $Q_+(0),Q_+(T)\in[0.10,0.18]$ and $\partial_{Q_+}K_\epsilon>0$ on the connecting phase interval. The other position, both momenta, and the energy agree at the two endpoints. Exact energy conservation and strict monotonicity in $Q_+$ force $Q_+(T)=Q_+(0)$, so the reduced root is a full-state return.

The first root box contains the exact harmonic fast orbit. Analyticity of $F$ through $\epsilon=0$, nonsingularity of $D_xF$, and the analytic implicit-function theorem make the glued family real analytic and identify it with the fast continuation. For $\epsilon>0$, a proper repetition would have primitive period below $0.335$, contradicting the full-shell period floor [\[eq:warped-period-floor\]](#eq:warped-period-floor){reference-type="ref" reference="eq:warped-period-floor"}; primitivity at $\epsilon=0$ is exact harmonic dynamics.

The word "unique" in [\[thm:validated-branch\]](#thm:validated-branch){reference-type="ref" reference="thm:validated-branch"} is qualified by the frozen boxes and bridge hulls. The next certificate extends that uniqueness to the declared local box, but not to the full energy shell.

## All-slab local-complement certificate

Let $$B_{\rm loc}=[-0.02,0.02]\times[0.12,0.17]\times[-0.08,0.08]
 \times[0.64,0.69]
 \label{eq:local-complement-box}$$ in the ordered reduced coordinates $(Q_-,Q_+,P_-,T)$. For each primary slab $E_j$, let $P_j$ be the protected L1 root box from [\[thm:validated-branch\]](#thm:validated-branch){reference-type="ref" reference="thm:validated-branch"}.

[\[thm:all-slab-complement\]]{#thm:all-slab-complement label="thm:all-slab-complement"} For every $j=0,\ldots,50$ and every $\epsilon\in E_j$, $$Z(F(\,\cdot\,,\epsilon))\cap
 \bigl(B_{\rm loc}\setminus\operatorname{int}P_j\bigr)=\varnothing.
 \label{eq:all-slab-complement}$$ Consequently, when combined with the L1 existence-and-uniqueness certificate, $$Z(F(\,\cdot\,,\epsilon))\cap B_{\rm loc}
 =\{x_j(\epsilon)\}.
 \label{eq:all-slab-uniqueness}$$

The frozen scheduler decomposes $B_{\rm loc}\setminus\operatorname{int}P_j$ into eight exact closed coordinate shells. It bisects every nonterminal box at an exact rational midpoint. Across 51 slabs and two MPFR precisions, all 102 resulting trees close: every one of the 26,803 terminal leaves is either an energy exclusion or a necessary-return exclusion, and no unresolved or root-candidate leaf remains. The archive contains 52,790 evaluated nodes, of which 25,987 are internal splits.

The independent checker reconstructs every shell and parent--child relation with exact rational arithmetic, replays every archived exclusion, and checks the canonical 102-entry manifest root. Its 158,782 checks have zero failures, and the 128- and 256-bit domain decisions agree. This proves [\[eq:all-slab-complement\]](#eq:all-slab-complement){reference-type="ref" reference="eq:all-slab-complement"}. The unique L1 zero in $P_j$ then gives [\[eq:all-slab-uniqueness\]](#eq:all-slab-uniqueness){reference-type="ref" reference="eq:all-slab-uniqueness"}.

## Invariant quotient and determinant gap

Let $$M_\epsilon=D_z\Phi_\epsilon^{T(\epsilon)}(z_\epsilon)
 \label{eq:monodromy}$$ be the four-dimensional fixed-time monodromy matrix, and let $D\Pi_\epsilon$ denote the return derivative on the two-dimensional intersection of $K_\epsilon=1$ with $P_+=0$. The certified positive phase slope makes this section regular and transverse.

[\[prop:quotient-identity\]]{#prop:quotient-identity label="prop:quotient-identity"} Along the full-return branch, $$\chi_{M_\epsilon}(t)=(t-1)^2\chi_{D\Pi_\epsilon}(t),
 \qquad
 \det(I-D\Pi_\epsilon)=4-\operatorname{tr}M_\epsilon.
 \label{eq:quotient-identity}$$ No semisimplicity assumption on the two unit multipliers is required.

At a periodic point, set $\alpha=dK_\epsilon$, $v=X_{K_\epsilon}$, and $L=\operatorname{span}\{v\}$. Flow covariance gives $M_\epsilon v=v$, while differentiated energy conservation gives $\alpha\circ M_\epsilon=\alpha$. Hence $$0\subset L\subset\ker\alpha\subset T_z\mathbb{R}^4
 \label{eq:invariant-flag}$$ is an invariant flag. The first quotient $L$ and the last quotient $T_z\mathbb{R}^4/\ker\alpha$ both carry the identity. The middle quotient $\ker\alpha/L$ is canonically conjugate to the energy-section return derivative. Characteristic polynomials therefore factor as in the first identity even if a unit Jordan block is present.

The symplectic form descends to a nondegenerate form on $\ker\alpha/L$, and the Hamiltonian flow preserves it. Thus $\det D\Pi_\epsilon=1$. For a two-by-two matrix $A$, $\det(I-A)=1-\operatorname{tr}A+\det A$. Combining this with $\operatorname{tr}M_\epsilon=2+\operatorname{tr}D\Pi_\epsilon$ proves the second identity.

[\[thm:monodromy-gap\]]{#thm:monodromy-gap label="thm:monodromy-gap"} On the branch in [\[thm:validated-branch\]](#thm:validated-branch){reference-type="ref" reference="thm:validated-branch"}, $$\boxed{
 \det(I-D\Pi_\epsilon)
 =4-\operatorname{tr}M_\epsilon>3,
 \qquad 0\le\epsilon\le0.101.}
 \label{eq:gap-theorem}$$

For each accepted transcript, outward exact-rational evaluation gives $$[D_M]=\left[4-\sum_{j=0}^3M_{jj}^{+},
              4-\sum_{j=0}^3M_{jj}^{-}\right].$$ All 101 intervals at each precision have lower endpoint above three. The rigorous directional minima are $$3.835992606647717183\quad(128\text{ bits}),
 \qquad
 3.850741968945794693\quad(256\text{ bits}).
 \label{eq:gap-minima}$$ The primary slabs cover the complete parameter interval, while the bridges identify all local representatives. turns the validated trace inequality into [\[eq:gap-theorem\]](#eq:gap-theorem){reference-type="ref" reference="eq:gap-theorem"}.

## Certificate accounting

separates producer work, proof-object replay, and mathematical post-processing. CAPD is pinned at official commit `731079217a92…895effe7f`; the full identifier is recorded in [16](#app:reproducibility){reference-type="ref" reference="app:reproducibility"}. The file `CAPDVersion.txt` at that commit reports 6.1.0. We do not call this a "6.1.0 release," because no such official tag is part of the audited provenance.

::: {#tab:certificate-accounting}
  Gate                                128 bit         256 bit Result
  --------------------------------- --------- --------------- ---------------
  Primary slabs                            51              51 all pass
  Guarded bridges                          50              50 all pass
  Validated flow/Krawczyk jobs            101             101 202/202 pass
  Exact-rational Krawczyk replays         101             101 202/202 pass
  Determinant replays                     101             101 202/202 pass
  Phase-slope replays                     101             101 202/202 pass
  Aggregate branch checks                       zero failures
  Aggregate monodromy checks                    zero failures
  Directed-decimal payloads                          all pass
  Local-complement trees                   51              51 102/102 close
  Evaluated complement nodes           28,054          24,736 52,790 total
  Energy-exclusion leaves               1,731           1,637 3,368 total
  Return-exclusion leaves              12,500          10,935 23,435 total
  Independent complement checks                 zero failures

  : Accepted A4.12--A4.15 proof-object accounting. The precision columns are producer replicas; the independent scripts replay stored finite-dimensional inequalities but do not rerun the ODE integrator.
:::

The smallest strict Krawczyk margins are $9.323437289176983\times10^{-6}$ and $9.328825112522987\times10^{-6}$ at 128 and 256 bits. The maximum contraction bounds are $0.033989409766443$ and $0.029013314518191$. The smallest certified phase-slope lower endpoint is $8.955040964476345874$. These are directed enclosures, not confidence intervals.

Two failed predecessors are retained in the archive. One evaluated the energy-gradient row only at a midpoint and therefore did not enclose the full Jacobian. A later run passed its local inclusions but constructed unpadded bridge hulls whose separately rounded decimal endpoints missed literal containment by one final printed decimal unit. The accepted version froze the rational $10^{-18}$ padding before production and reran both precisions. No post-hoc tolerance promoted either predecessor.

[\[rem:nonpromotion\]]{#rem:nonpromotion label="rem:nonpromotion"} prove a primitive branch, determinant gap, and pointwise root uniqueness only in the frozen local reduced chart. The phase cover, full shell cover over $[0.60,0.75]$, independent event-projected return derivative, and a separate Taylor-residual gate remain open. Consequently, these theorems do not prove $\delta_{\rm tr}\ge0.010201$ and do not license [\[eq:main-trace-formula\]](#eq:main-trace-formula){reference-type="ref" reference="eq:main-trace-formula"} at $\delta=0.01$.

# The spectral coefficient and a frozen numerical diagnostic {#sec:spectral-diagnostic}

Inside the analytic domain of [\[thm:relative-gutzwiller\]](#thm:relative-gutzwiller){reference-type="ref" reference="thm:relative-gutzwiller"}, define the predicted positive-time coefficient $$\rho_{\rm pred}(\hbar;E)
 =i\widehat g(T_+(E))
 \frac{T_+(E)}{2\pi\sqrt{|\det(I-P_+(E))|}}
 e^{iS_+(E)/\hbar}.
 \label{eq:rho-pred-general}$$ The asymptotic statement is $\rho_{\mathrm{rel},\hbar}/\rho_{\rm pred}=1+O(\hbar)$ for fixed admissible data, provided the leading coefficient is nonzero. Classical orbit quantities occur on the right, while the left is evaluated from the two energy-localized eigenvalue lists. The relation is therefore a spectral recovery statement, not an equality between a classical orbit census and a separately fitted signal.

The frozen R401-SC computation tests this normalization at $\delta=0.01$. Its immutable classical inputs are $$T=0.6635697917937936,
 \qquad
 S=0.006637068399523644,
 \qquad
 D=3.863271395157721,
 \label{eq:r401-inputs}$$ and the test function is normalized so that $\widehat g(T)=1$. Thus $$\rho_{\rm pred}(\hbar)=i\frac{T}{2\pi\sqrt D}e^{iS/\hbar}.
 \label{eq:r401-oracle}$$ The energy cutoff, time cutoff, phase, scale, and eight-point $\hbar$ ladder were fixed before the production archive. No prime, zero, peak time, phase offset, or amplitude was fitted.

::: {#tab:r401-ladder}
               $\hbar$              $Z_\hbar$   $|Z_\hbar-1|$
  -------------------- ---------------------- ---------------
    $4.0\times10^{-4}$   $0.344728+0.367872i$          0.7515
    $3.0\times10^{-4}$   $1.448682+0.095288i$          0.4587
    $2.0\times10^{-4}$   $0.317529+0.242788i$          0.7244
    $1.5\times10^{-4}$   $1.403014-0.489353i$          0.6339
    $1.0\times10^{-4}$   $0.843838-0.354104i$          0.3870
    $7.5\times10^{-5}$   $0.785322+0.054500i$          0.2215
    $5.0\times10^{-5}$   $1.047705+0.011489i$          0.0491
    $4.0\times10^{-5}$   $1.006523+0.013300i$          0.0148

  : Frozen R401-SC normalized coefficient $Z_\hbar=\rho_{\mathrm{rel},\hbar}/\rho_{\rm pred}(\hbar)$ at $\delta=0.01$. The nonmonotone early values are retained. This table is an A4.10-guided numerical diagnostic, not a validation that $0.01<\delta_{\rm tr}$.
:::

The warped calculation is performed after the exact unitary coordinate change $u=\Psi_a(q)$. In those coordinates, the potential has radial quadratic-exponential tails and the kinetic energy becomes a polynomial divergence-form operator. This choice is essential: original-coordinate Hermite functions have tails incompatible with the warped $e^{c x^4}$ direction and were rejected at the protocol stage. The radial reference is checked by an independent angular-momentum Laguerre decomposition.

The archive contains nested-basis checks, phase-budget checks, quadrature checks, a radial oracle, a guard mode, internal residuals, and an independent recomputation that does not import the production trace code. The latter passes 58 checks. At the finest point, $$Z_{4\times10^{-5}}
 =1.0065230645+0.0133004473i,
 \qquad
 |Z_{4\times10^{-5}}-1|\approx0.0148.
 \label{eq:finest-z}$$ The corresponding exactly soluble harmonic calculation, under the same finite windows, exhibits comparable pre-asymptotic oscillations; at the finest point the nonlinear and harmonic normalized values differ by $0.002051$.

The final two points are consistent with the amplitude and phase in [\[eq:main-trace-formula\]](#eq:main-trace-formula){reference-type="ref" reference="eq:main-trace-formula"}. They do not estimate an $O(\hbar)$ constant: eight nonmonotone values over one short ladder cannot support that inference. More fundamentally, the computation does not close the theorem-domain gap. The analytic result provides an unknown positive $\delta_{\rm tr}$, and the local-box certificate controls one branch but not every possible return. Consequently, the correct logical statement is $$\boxed{\text{R401-SC tests the A4.10 coefficient at }\delta=0.01;
 \quad \text{it does not prove }0.01<\delta_{\rm tr}.}
 \label{eq:diagnostic-boundary}$$

# What has and has not been built {#sec:scope}

The strongest result of the paper is local in energy and semiclassical in $\hbar$. Its input is a fixed regular energy $E=2\pi+\delta$, followed by $\hbar\downarrow0$. A Hilbert--Pólya programme ultimately asks for one fixed operator, normally at physical $\hbar=1$, whose high-energy spectrum has an arithmetic identification. These regimes are not interchangeable.

## Gate ledger

records the authorized status of each step. The labels are bookkeeping devices, not implications between unrelated properties.

::: {#tab:gate-ledger}
  Gate                  Question                                                 Present result                                                                    Excluded inference
  --------------------- -------------------------------------------------------- --------------------------------------------------------------------------------- ---------------------------------------------------------
  $Q$                   Self-adjoint operator with discrete real spectrum?       Closed for each fixed $a$ and $\hbar>0$                                           No zeta-zero identification
  $W$                   Common mean spectral clock?                              Exact classical shell clock; preceding work supplies the quantum mean programme   No individual-level correspondence
  $S_{\rm op}$          Is the warp spectrally active?                           Established in the preceding operator analysis                                    No arithmetic content by itself
  $P^*_{\rm loc}$       Eigenvalue-only nonzero-time orbit term?                 Closed for each fixed $0<\delta<\delta_{\rm tr}$                                  $\delta_{\rm tr}$ is not quantitative
  $C_{\rm loc}$         Unique reduced root in the declared local box?           Closed on all 51 frozen slabs at 128 and 256 bits                                 No phase/flow-box or global-shell conclusion
  $P^*_{\rm loc,num}$   Frozen coefficient diagnostic?                           Passed at $\delta=0.01$                                                           No theorem-domain promotion
  $P_0$                 Endogenous prime-power times and weights?                Open                                                                              No prime trace or Euler product
  $Z$                   Spectral fluctuation equals the zeta explicit formula?   Unauthorized before $P_0$                                                         No zero comparison
  RH                    Does the construction prove RH?                          No claim                                                                          None of the earlier gates substitutes for $P_0$ and $Z$

  : Claim ledger. "Closed" always means closed only at the domain stated in the middle column.
:::

The relative trace in [\[thm:relative-gutzwiller\]](#thm:relative-gutzwiller){reference-type="ref" reference="thm:relative-gutzwiller"} is a meaningful spectral bridge: a classical orbit coefficient is recoverable from two eigenvalue lists after a nonzero-time cutoff. It does not provide the arithmetic data required by an explicit formula. In particular, it does not produce a family indexed by primes and repetitions with $$T_{p,r}\sim r\log p,
 \qquad
 A_{p,r}\sim C(\log p)p^{-r/2},
 \label{eq:prime-target}$$ nor does it derive the signs and phases that accompany those weights. A single smooth Lyapunov branch cannot be renamed an arithmetic family.

## Why fixed-energy semiclassics is not yet the fixed operator

For the radial system at high energy, set $$L_E=\log(E/2\pi),
 \qquad
 R_E=\sqrt{L_E/\pi},
 \qquad
 \tau_E=R_E/\sqrt E,
 \qquad
 h_E=(R_E\sqrt E)^{-1}.
 \label{eq:high-energy-scales}$$ The spatially rescaled operator has the schematic form $$\frac{P_{0,1}}{E}
 =-\frac{h_E^2}{2}\Delta_Q
 +e^{L_E(|Q|^2-1)}.
 \label{eq:hard-wall-limit}$$ Thus $E\to\infty$ at physical $\hbar=1$ is a simultaneous semiclassical and hard-wall limit. A fixed physical time becomes a growing rescaled time, well outside the bounded-time theorem proved here. The Hénon inverse in [\[eq:henon-inverse-jac\]](#eq:henon-inverse-jac){reference-type="ref" reference="eq:henon-inverse-jac"} can additionally stretch an allowed direction quadratically in the radial scale. A uniform high-energy orbit theorem for the warped well is therefore a separate problem, not a corollary of the near-bottom branch. Existing refined trace and Weyl results for homogeneous or harmonic-oscillator perturbations provide useful contrasts [@PushnitskiSorrell2006; @DollGannotWunsch2018; @DollZelditch2020], but the audited hypotheses of those works do not cover the simultaneous exponential hard-wall and Hénon-metric limit in [\[eq:hard-wall-limit\]](#eq:hard-wall-limit){reference-type="ref" reference="eq:hard-wall-limit"}.

## Remaining theorem engineering

The next quantitative objective is to prove $\delta_{\rm tr}\ge0.010201$. The radial bound and the warped period floor already reduce the missing return interval to $[0.60,0.75]$, while [\[thm:validated-branch,thm:monodromy-gap\]](#thm:validated-branch,thm:monodromy-gap){reference-type="ref" reference="thm:validated-branch,thm:monodromy-gap"} control the distinguished branch. A4.15 and [\[thm:all-slab-complement\]](#thm:all-slab-complement){reference-type="ref" reference="thm:all-slab-complement"} now close the local root complement on all 51 slabs at both precisions. The remaining steps are:

1.  cover phase along the orbit so that the section represents all time-translated returns;

2.  cover the remaining global energy shell and reject every other return in $[0.60,0.75]$;

3.  independently compute the event-projected $D\Pi$ and close the separate Taylor-residual gate.

Only after these steps can the analytic coefficient be licensed at the explicit R401 energy. The later arithmetic problem is independent: one must find an endogenous growing-complexity carrier before comparing periods with $\log p$. Neither finite-window random-matrix agreement nor fitting known zeros would supply that carrier.

## Claim-boundary summary

::: {#tab:evidence-layers}
  Layer                        Authorized statement                                                                                             Boundary
  ---------------------------- ---------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------
  Analytic theorem             One eigenvalue-only fast-orbit term for every fixed $0<\delta<\delta_{\rm tr}$                                   $\delta_{\rm tr}>0$ is not numerical; no joint limit
  Computer-assisted theorem    One primitive local branch, $\det(I-D\Pi)>3$, and one reduced root in $B_{\rm loc}$ for $0\le\epsilon\le0.101$   Local reduced chart only; phase/global cover open
  Implementation certificate   Six representative complement trees close at 128 and 256 bits                                                    Historical A4.14 engine gate; subsumed in coverage by A4.15
  Numerical diagnostic         Frozen coefficient is approached at $\delta=0.01$ over the reported $\hbar$ ladder                               No assertion that $0.01<\delta_{\rm tr}$; no fitted remainder law

  : Four evidence layers that must not be merged.
:::

This separation is also the principal methodological outcome. It makes the local spectral success useful without burdening it with a conclusion it cannot support.

# Conclusion {#sec:conclusion}

For an explicit radial/Hénon pair with the same exact phase-volume clock, we have isolated a nonzero-time spectral difference. The analytic result is an eigenvalue-only relative Gutzwiller term from one primitive fast Lyapunov orbit at every fixed sufficiently small positive energy excess. The phase, normalization, action, and stability factor are explicit, and the removal of the microlocal observable follows from a complete-shell short-return theorem.

A separate computer-assisted theorem makes the distinguished branch quantitative. Validated flow and Krawczyk enclosures, guarded bridge boxes, and exact-rational replay give one connected primitive local branch over $0\le\epsilon\le0.101$. An invariant-quotient argument and validated monodromy enclosures prove $\det(I-D\Pi_\epsilon)>3$ on that branch. The all-slab complement certificate then excludes every other reduced root in the declared local box on all 51 parameter slabs. Its 102 trees contain 52,790 interval nodes, and 158,782 independent exact-rational checks close with zero failures. This gives pointwise reduced-root uniqueness in the frozen local chart, not uniqueness on the full energy shell. The representative spectral computation at $\delta=0.01$ is a separate numerical evidence layer: it tests the coefficient but does not establish that the energy lies in the current analytic theorem domain.

Two next steps are concrete. First, a phase/flow-box and global-shell cover should quantify $\delta_{\rm tr}$ and connect the analytic and validated domains. Second, any Hilbert--Pólya continuation must search for an endogenous arithmetic carrier at fixed physical $\hbar$, without loading prime times or zeta zeros into the construction. The present paper supplies a rigorously controlled local trace component for that search; it does not supply the arithmetic bridge.

# Functional calculus and Fourier conventions {#app:foundations}

This appendix records details used in [\[sec:model-trace,sec:analytic-trace\]](#sec:model-trace,sec:analytic-trace){reference-type="ref" reference="sec:model-trace,sec:analytic-trace"}. They make clear which relative objects require trace-class comparison and which do not.

## Compact resolvent

The closed quadratic form associated with [\[eq:semiclassical-operator\]](#eq:semiclassical-operator){reference-type="ref" reference="eq:semiclassical-operator"} is $$\mathfrak p_{a,\hbar}[u]
 =\frac{\hbar^2}{2}\|\nabla u\|_2^2
 +\int_{\mathbb{R}^2}V_a(q)|u(q)|^2\,\mathrm{d}q.
 \label{eq:quadratic-form}$$ It is densely defined and lower bounded. If $(u_n)$ is bounded in its form norm, then for any $M>0$, $$\int_{\{V_a>M\}}|u_n|^2
 \le \frac{1}{M}\int_{\mathbb{R}^2}V_a|u_n|^2.
 \label{eq:tail-compactness}$$ Choose $M$ so that the right side is uniformly small. The sublevel $\{V_a\le M\}$ is compact by properness, and Rellich compactness applies there. A diagonal argument gives a convergent subsequence in $L^2(\mathbb{R}^2)$, proving compact resolvent for the Friedrichs realization.

## Finite-rank cutoff identities

For $f\in C_c^\infty(\mathbb{R})$, spectral calculus gives $$f(P_{a,\hbar})=
 \sum_k f(\lambda_{a,k}(\hbar))
 |\psi_{a,k}\rangle\langle\psi_{a,k}|.
 \label{eq:spectral-calculus}$$ Only finitely many summands are nonzero. Hence every trace in [\[eq:relative-wave,eq:relative-density\]](#eq:relative-wave,eq:relative-density){reference-type="ref" reference="eq:relative-wave,eq:relative-density"} exists separately. We never deduce trace class of $(P_{a,\hbar}-z)^{-1}-(P_{0,\hbar}-z)^{-1}$, and no such statement is needed.

If $N_j$ counts eigenvalues with multiplicity, then $$\operatorname{Tr}f(P_j)=\int_\mathbb{R}f(E)\,\mathrm{d}N_j(E).
 \label{eq:stieltjes-spectral}$$ Subtracting, using $\xi=N_0-N_a$, and integrating by parts proves $$\operatorname{Tr}[f(P_a)-f(P_0)]=\int_\mathbb{R}f'(E)\xi(E)\,\mathrm{d}E.
 \label{eq:compact-relative-identity}$$ Compact support removes all endpoint terms.

## Fourier factors and orientation

Substituting [\[eq:fourier-convention\]](#eq:fourier-convention){reference-type="ref" reference="eq:fourier-convention"} into each spectral summand gives $$g\!\left(\frac{E-P}{\hbar}\right)
 =\frac{1}{2\pi}\int
 e^{it(E-P)/\hbar}\widehat g(t)\,\mathrm{d}t,
 \label{eq:functional-fourier}$$ which proves [\[eq:density-wave\]](#eq:density-wave){reference-type="ref" reference="eq:density-wave"}. A positive-time cutoff returns the complex coefficient in [\[eq:main-trace-formula\]](#eq:main-trace-formula){reference-type="ref" reference="eq:main-trace-formula"}. For a real test with symmetric positive and negative time supports, the negative-time orbit contributes the complex conjugate.

Let $\theta_0=2\pi/\rho_a\in(0,2\pi)$. Abel regularization gives $$\lim_{r\uparrow1}\sum_{m=0}^\infty
 r^m e^{-i\theta_0(m+1/2)}
 =\frac{e^{-i\theta_0/2}}{1-e^{-i\theta_0}}
 =-\frac{i}{2\sin(\theta_0/2)}.
 \label{eq:abel-transverse}$$ Poisson summation of the fast quantum number at its first positive recurrence contributes $-1/\omega_+$. Since $2\sin(\theta_0/2)=\sqrt{D_+^0}>0$, the combined phase is $+i$, and $1/\omega_+=T_+^0/(2\pi)$. This locks the normalization used throughout.

## Support-localized stationary phase

After coherent-state insertion, the trace phase is stationary only at pairs $(z,t)$ satisfying $$h(z)=E,
 \qquad \Phi^t(z)=z,
 \qquad t\in\operatorname{supp}\widehat g.
 \label{eq:stationary-set}$$ When $\operatorname{supp}\widehat g\subset[-T_0,T_0]$, no fixed point outside that time interval occurs in the integral. Compactness of the energy band makes the remaining stationary analysis local in phase space. The short-return classification in [\[thm:whole-shell\]](#thm:whole-shell){reference-type="ref" reference="thm:whole-shell"} therefore suffices; no assertion about longer trajectories is silently imported.

# Normal-coordinate tensors and nonlinear period {#app:nonlinear-period}

Expand the potential in the orthonormal normal coordinates of [\[eq:harmonic-normal-form\]](#eq:harmonic-normal-form){reference-type="ref" reference="eq:harmonic-normal-form"}: $$V_a(Q)=2\pi+\frac{1}{2}\sum_j\omega_j^2Q_j^2
 +\frac{1}{6}\sum_{ijk}C_{ijk}Q_iQ_jQ_k
 +\frac{1}{24}\sum_{ijkl}D_{ijkl}Q_iQ_jQ_kQ_l
 +O(|Q|^5).
 \label{eq:potential-taylor}$$ Use the strained time $\tau=\Omega t$ and the ansatz $$\begin{aligned}
 Q_+(t)&=A\cos\tau
 +A^2(b_{+0}+b_{+2}\cos2\tau)+O(A^3),
 \label{eq:pl-fast}\\
 Q_-(t)&=A^2(b_{-0}+b_{-2}\cos2\tau)+O(A^3),
 \label{eq:pl-slow}\\
 \Omega&=\omega_++\nu_+A^2+O(A^3).
 \label{eq:pl-frequency}\end{aligned}$$ There is no order-$A$ slow component because the branch is tangent to the fast eigenspace.

At order $A^2$, $\cos^2\tau=(1+\cos2\tau)/2$ separates the constant and second-harmonic equations. Solving them yields $$b_{j0}=-\frac{C_{++j}}{4\omega_j^2},
 \qquad
 b_{j2}=-\frac{C_{++j}}{4(\omega_j^2-4\omega_+^2)}.
 \label{eq:pl-b-proof}$$ At order $A^3$, the resonant $\cos\tau$ coefficient must vanish: $$-2\omega_+\nu_+
 +\frac{D_{++++}}8
 +\sum_{j\in\{-,+\}}C_{++j}
 \left(b_{j0}+\frac12b_{j2}\right)=0.
 \label{eq:resonance-solvability}$$ This proves [\[eq:nu-plus\]](#eq:nu-plus){reference-type="ref" reference="eq:nu-plus"}. Since $$E-2\pi=\frac12\omega_+^2A^2+o(A^2),
 \qquad T=\frac{2\pi}{\Omega},
 \label{eq:energy-amplitude}$$ differentiation gives [\[eq:period-slope\]](#eq:period-slope){reference-type="ref" reference="eq:period-slope"}. Integrating $\,\mathrm{d}S/\,\mathrm{d}E=T$ gives the factor one-half between the linear correction in [\[eq:period-expansion\]](#eq:period-expansion){reference-type="ref" reference="eq:period-expansion"} and the correction to $S/\delta$ in [\[eq:action-expansion\]](#eq:action-expansion){reference-type="ref" reference="eq:action-expansion"}.

The normal basis has a deterministic sign convention in the archive. Reversing one eigenvector changes individual cubic tensors but leaves the final period slope invariant. The reported $\nu_+$ is quoted to reproduce the frozen coordinate convention, not as a coordinate-free observable.

# Quantitative period bounds {#app:period-bounds}

Let $q(t)$ be a nonconstant $T$-periodic solution of $$q''=-\nabla V(q)
 \label{eq:newton-equation}$$ contained in a convex set on which $\nabla V$ is $L$-Lipschitz. Write $\bar q=T^{-1}\int_0^Tq(t)\,\mathrm{d}t$. Periodic integration by parts gives $$\begin{aligned}
 \int_0^T|q'|^2\,\mathrm{d}t
 &=\int_0^T(q-\bar q)\cdot\nabla V(q)\,\mathrm{d}t\\
 &=\int_0^T(q-\bar q)\cdot
 [\nabla V(q)-\nabla V(\bar q)]\,\mathrm{d}t\\
 &\le L\int_0^T|q-\bar q|^2\,\mathrm{d}t.
 \label{eq:lipschitz-energy}\end{aligned}$$ The periodic Wirtinger inequality yields $$\int_0^T|q-\bar q|^2\,\mathrm{d}t
 \le\left(\frac{T}{2\pi}\right)^2
 \int_0^T|q'|^2\,\mathrm{d}t.
 \label{eq:wirtinger}$$ Cancelling the nonzero kinetic integral proves $$T\ge\frac{2\pi}{\sqrt L}.
 \label{eq:universal-period-bound}$$

For $V_0(q)=2\pi e^{\pi|q|^2}$, direct differentiation gives $$\|\nabla^2V_0(q)\|_{\rm op}
 \le E\left(2\pi+4\pi\log\frac{E}{2\pi}\right).
 \label{eq:radial-hessian-bound}$$ Using $\log(1+x)\le x$ through $E=2\pi+0.010201$ proves [\[eq:radial-explicit-bound\]](#eq:radial-explicit-bound){reference-type="ref" reference="eq:radial-explicit-bound"}.

For the warped potential, the energy equation and the exact inverse $\Psi_a^{-1}(u,v)=(v,-c_av-av^2-u)$ enclose every allowed configuration in $$|x|<0.02274,
 \qquad |y|<0.042427.
 \label{eq:warped-config-box}$$ Outward rational estimates for $D\Psi_a$, $\Psi_a$, and the exponential factor give $$\|\nabla^2V_a\|_{\rm op}<102.494<103.
 \label{eq:warped-hessian-bound}$$ The box is convex, so [\[eq:universal-period-bound\]](#eq:universal-period-bound){reference-type="ref" reference="eq:universal-period-bound"} proves [\[eq:warped-period-floor\]](#eq:warped-period-floor){reference-type="ref" reference="eq:warped-period-floor"}. The result is only a period floor; it does not count returns above the floor.

# Complete-shell blow-up and observable removal {#app:whole-shell}

We expand the proof of [\[thm:whole-shell\]](#thm:whole-shell){reference-type="ref" reference="thm:whole-shell"}. The main issue is uniformity over the full energy surface. Local convergence near the harmonic orbit would not rule out a second family that approaches the bottom along a different configuration direction.

## Uniform compactness

On $h_a=2\pi+\epsilon^2$, positivity of the kinetic and potential excesses gives $$|p|\le\sqrt2\epsilon,
 \qquad
 |\Psi_a(q)|^2
 \le\frac{1}{\pi}\log\left(1+\frac{\epsilon^2}{2\pi}\right).
 \label{eq:whole-shell-basic-bound}$$ Write $(u,v)=\Psi_a(q)$. The inverse formula yields $$q=(v,-c_av-av^2-u).
 \label{eq:inverse-bound-use}$$ Both $u$ and $v$ are $O(\epsilon)$, hence $q=O(\epsilon)$ uniformly over the entire shell. Therefore the scaled states $(Q,P)$ lie in a fixed compact set. The removable extension of [\[eq:normalized-k\]](#eq:normalized-k){reference-type="ref" reference="eq:normalized-k"} is smooth on a neighborhood of that set, and $$K_\epsilon\to K_0\quad\text{in }C^2,
 \qquad
 X_{K_\epsilon}\to X_{K_0}\quad\text{in }C^1.
 \label{eq:flow-convergence}$$ Bounded-time flows and their first derivatives consequently converge uniformly.

## Limiting returns

Suppose $Z_n\in\{K_{\epsilon_n}=1\}$, $\epsilon_n\downarrow0$, and $\Phi_{\epsilon_n}^{T_n}(Z_n)=Z_n$ with $0<T_n\le0.75$. Compactness gives $Z_n\to Z_0\in\{K_0=1\}$ and $T_n\to T_*\in[0,0.75]$ after a subsequence. If $T_*=0$, then $$0=\frac{\Phi_{\epsilon_n}^{T_n}(Z_n)-Z_n}{T_n}
 =\frac{1}{T_n}\int_0^{T_n}
 X_{K_{\epsilon_n}}(\Phi_{\epsilon_n}^s(Z_n))\,\mathrm{d}s
 \longrightarrow X_{K_0}(Z_0).
 \label{eq:no-small-return}$$ The harmonic vector field vanishes only at the origin, which is not on $K_0=1$; therefore $T_*>0$.

The slow harmonic component has first return $T_-^0>0.75$, and the fast component has returns at the multiples of $T_+^0$, with $T_+^0<0.75<2T_+^0$. Hence $$T_*=T_+^0,
 \qquad
 Z_0\in\Gamma_0:=\{K_0=1,Q_-=P_-=0\}.
 \label{eq:limiting-fast-circle}$$ The set $\Gamma_0$ is one phase circle, not a family of geometrically different fast orbits.

## A phase-fixed local return

At the positive fast turning point $$z_*=(Q_-=P_-=P_+=0, Q_+=\sqrt2/\omega_+),
 \label{eq:fast-turning-point}$$ one has $$\partial_{Q_+}K_0(z_*)=\sqrt2\omega_+\ne0,
 \qquad
 \dot P_+(z_*)=-\sqrt2\omega_+\ne0.
 \label{eq:turning-transversality}$$ The first inequality solves the energy equation for $Q_+$, and the second makes $P_+=0$ a transverse event. The varying sections can therefore be identified by $(Q_-,P_-)$. In normalized slow coordinates $$x_-=\sqrt{\omega_-}Q_-,
 \qquad y_-=P_-/\sqrt{\omega_-},
 \label{eq:normalized-slow}$$ the limiting derivative is the rotation $$D\Pi_0(z_*)=R_{2\pi/\rho_a}.
 \label{eq:limiting-return-rotation}$$ Its fixed-point derivative is invertible because $4\sin^2(\pi/\rho_a)>0$. The parameter-dependent implicit-function theorem gives one nearby fixed point for every sufficiently small $\epsilon$.

[\[lem:unique-local-crossing\]]{#lem:unique-local-crossing label="lem:unique-local-crossing"} There are a section neighborhood $U$ of $z_*$, a number $\eta>0$, and $\epsilon_0>0$ with the following property. Let $0<\epsilon_n<\epsilon_0$, and let primitive periodic trajectories $z_n(t)$ have periods $T_n\to T_+^0$. If, after phase alignment, $z_n\to z_0$ in $C^1$ over one period, where $z_0$ parametrizes $\Gamma_0$ and $z_0(0)=z_*$, then $z_n$ has exactly one intersection per primitive circuit with $$U\cap\{K_{\epsilon_n}=1,\ P_+=0,\ Q_+>0\},$$ and the event has the same orientation as at $z_*$.

Parametrize the limiting circle on the cyclic interval $[ -\eta,T_+^0-\eta]$. Since $P_+$ has a simple zero at the positive turning point, choose $\eta$, $c>0$, and $U$ so that $\dot P_+\le-c$ on the part of $\Gamma_0$ in $U$, the values of $P_+$ at times $-\eta$ and $\eta$ have opposite signs, and the remaining compact arc of $\Gamma_0$ is disjoint from the closure of the local section in $U$. Bounded-time $C^1$ convergence preserves the two endpoint signs and gives $\dot P_+\le-c/2$ whenever $z_n(t)\in U$. The intermediate-value theorem supplies one local zero, strict monotonicity supplies at most one, and uniform position convergence excludes another intersection on the complementary arc. Identifying the endpoints of the period interval counts the crossing only once.

## Primitivity and globalization

Suppose a sequence of the returns above is an $m_n$-fold iterate of a primitive period $\tau_n$. If $m_n\to\infty$, then $\tau_n\to0$, contradicting [\[eq:no-small-return\]](#eq:no-small-return){reference-type="ref" reference="eq:no-small-return"}. Along a subsequence with $m_n=m$, flow convergence would give $$\Phi_0^{T_+^0/m}(Z_0)=Z_0.
 \label{eq:fractional-return}$$ On $\Gamma_0$, this is possible only for $m=1$. The return is therefore primitive.

If a second geometric orbit existed for every member of a sequence $\epsilon_n\downarrow0$, the limiting classification and first-derivative flow convergence would make its phase-aligned trajectory converge uniformly in $C^1$ to $\Gamma_0$ over one period. By [\[lem:unique-local-crossing\]](#lem:unique-local-crossing){reference-type="ref" reference="lem:unique-local-crossing"}, it has exactly one oriented crossing of the local section neighborhood per primitive circuit. Its return after that circuit is therefore the next local return, so the crossing is a fixed point of $\Pi_{\epsilon_n}$. The implicit-function theorem provides only the continued fast fixed point. The contradiction proves complete-shell uniqueness.

The globalization step is exactly what permits the symbol in the trace formula to be $A=1$. Before this step, an observable supported near the fast orbit would isolate a legitimate microlocal term, but the spectral sum would contain matrix elements $\langle\psi_k,A_\hbar\psi_k\rangle$. After the full return classification, the observable is unnecessary and the result becomes eigenvalue-only.

# Computer-assisted proof details {#app:cap}

The accepted branch archive composes a validated ODE layer with a finite interval-operator layer. The distinction is important for interpreting the independent checker.

## Validated flow and variational equations

The normalized Hamiltonian equations are integrated together with the first variational system $$\dot z=X_{K_\epsilon}(z),
 \qquad
 \dot Y=DX_{K_\epsilon}(z)Y,
 \qquad Y(0)=I.
 \label{eq:variational-system}$$ The parameter $\epsilon$ is enclosed over each slab. A validated $C^1$-Lohner set controls both the image of the initial root box and the derivative needed for $D_xF$ [@Lohner1987; @NedialkovJacksonCorliss1999; @Zgliczynski2002; @KapelaMrozekWilczakZgliczynski2021]. This layer provides interval enclosures. It does not, by itself, assert a periodic shooting root.

The source is pinned to CAPD commit `731079217a9254ea2948d742df2b170895effe7f`, whose `CAPDVersion.txt` reports 6.1.0. MPFR/GMP and compiler details are bound into the release manifest. The accepted producer runs the identical logical matrix at 128 and 256 MPFR bits.

## Parameterized root inclusion

For each fixed $\epsilon$ in a slab, the interval object $D_xF(X,E_\epsilon)$ encloses every point Jacobian. The strict inclusion and contraction in [\[eq:krawczyk-gates\]](#eq:krawczyk-gates){reference-type="ref" reference="eq:krawczyk-gates"} imply existence and uniqueness of a zero within the declared box. The full-box energy derivative in [\[eq:energy-jacobian-row\]](#eq:energy-jacobian-row){reference-type="ref" reference="eq:energy-jacobian-row"} is a mathematical requirement, not a numerical refinement. A midpoint derivative would fail to enclose the family of Jacobians and cannot license the Krawczyk theorem.

The 51 primary slabs cover $[0,0.101]$ exactly. The 50 bridge parameter intervals are the adjacent overlaps, while each state-space bridge is the pre-frozen padded hull [\[eq:bridge-hull\]](#eq:bridge-hull){reference-type="ref" reference="eq:bridge-hull"}. The checker verifies literal containment using the actual printed endpoints. Since the bridge has one root, the two primary roots agree throughout the overlap.

## Full-return recovery

At a zero of [\[eq:validated-residual\]](#eq:validated-residual){reference-type="ref" reference="eq:validated-residual"}, the initial and terminal values agree in $Q_-$, $P_-$, and $P_+$. Both endpoints lie on the same energy. On the validated interval $Q_+\in[0.10,0.18]$, the archive proves $$\partial_{Q_+}K_\epsilon\ge
 8.955040964476345874>0.
 \label{eq:phase-slope-min}$$ For fixed values of the other three coordinates, energy is strictly increasing in $Q_+$. Equal energies therefore force equal $Q_+$, recovering the omitted equation. Hamiltonian energy conservation is exact at the mathematical level; the validated integrator supplies the endpoint enclosures needed to place both values in the monotonicity interval.

## Exact-rational proof-object replay

Every outward decimal endpoint is parsed by the checker as a rational number. The checker reconstructs the preconditioner $C$, the interval matrix $I-CJ$, the Krawczyk image, the contraction bound, bridge containment, and cross-precision intersections. A second checker reconstructs the phase-slope and $4-\operatorname{tr}M$ intervals. These scripts do not import the production analyzers.

The replay begins from stored interval endpoints. It does not regenerate the CAPD flow or prove that arbitrary decimals are outward enclosures; that obligation belongs to the pinned producer and interval library. Conversely, the two producer precisions do not replace strict inclusion. The theorem is the composition of valid interval generation, strict interval gates, and the analytic branch/full-return arguments.

## Failure-preserving audit trail

The archive preserves two non-licensing predecessors. The first used the midpoint energy gradient in the Krawczyk Jacobian. The second used bridge hulls formed independently from rounded decimal displays and failed exact containment at one final decimal unit. In the accepted run, bridge padding was frozen as an exact rational construction before any production job. Preserving these attempts prevents a successful status from obscuring why a seemingly small implementation detail was mathematically material.

## Local versus global uniqueness

The protected root boxes do not by themselves fill the four-dimensional local search box. Accordingly, A4.12 establishes one branch in those boxes but, taken alone, does not exclude a second reduced root outside them. A4.15 performs the required exhaustive interval search on the declared complement: for every frozen slab it excludes all reduced roots in $B_{\mathrm{loc}}\setminus\operatorname{int}P_j$. Combining the two certificates therefore gives the pointwise uniqueness statement in [\[thm:all-slab-complement\]](#thm:all-slab-complement){reference-type="ref" reference="thm:all-slab-complement"} throughout $B_{\mathrm{loc}}$.

This closure remains confined to the frozen $P_+=0$ reduced chart. Phase alignment, a flow-box cover of the complete orbit, and the global energy-shell cover are separate tasks. Those open domains are why neither A4.12 nor A4.15 licenses a global or final conclusion.

# Invariant-quotient monodromy proof {#app:monodromy}

We give the linear-algebra argument behind [\[prop:quotient-identity,thm:monodromy-gap\]](#prop:quotient-identity,thm:monodromy-gap){reference-type="ref" reference="prop:quotient-identity,thm:monodromy-gap"} in a form that includes possible Jordan blocks at the unit multiplier.

Fix a periodic point $z$ and abbreviate $$V=T_z\mathbb{R}^4,
 \qquad \alpha=dK_\epsilon(z),
 \qquad v=X_{K_\epsilon}(z),
 \qquad L=\operatorname{span}\{v\},
 \qquad M=M_\epsilon.
 \label{eq:flag-notation}$$ Since $dK(X_K)=0$, $L\subset\ker\alpha$. Flow covariance at the full return gives $$Mv=D\Phi^{T}(z)X_K(z)=X_K(\Phi^T(z))=v.
 \label{eq:flow-vector-fixed}$$ Differentiated energy conservation gives $$\alpha\circ M=\alpha.
 \label{eq:covector-fixed}$$ Therefore $0\subset L\subset\ker\alpha\subset V$ is an invariant filtration. The induced map on $L$ is the identity by [\[eq:flow-vector-fixed\]](#eq:flow-vector-fixed){reference-type="ref" reference="eq:flow-vector-fixed"}; the induced map on $V/\ker\alpha$ is the identity by [\[eq:covector-fixed\]](#eq:covector-fixed){reference-type="ref" reference="eq:covector-fixed"}.

Variations tangent to the energy shell belong to $\ker\alpha$. Changing the event time changes a variation by a multiple of $v$. Event transversality therefore identifies the derivative of the two-dimensional return with the induced map on $\ker\alpha/L$. Characteristic polynomials multiply over invariant subspaces and quotients, so $$\chi_M(t)=(t-1)^2\chi_{D\Pi}(t).
 \label{eq:flag-factorization-app}$$ No eigenbasis has been introduced. The argument remains valid if the two unit multipliers have a nontrivial Jordan block, or if their algebraic multiplicity is four.

With the Hamiltonian sign convention used here, $\ker\alpha=L^\omega$. The symplectic form descends to a nondegenerate two-form on $L^\omega/L$. Since $M$ is symplectic, its induced map preserves this form, and $$\det D\Pi=1.
 \label{eq:return-area}$$ Taking traces in [\[eq:flag-factorization-app\]](#eq:flag-factorization-app){reference-type="ref" reference="eq:flag-factorization-app"} gives $\operatorname{tr}M=2+\operatorname{tr}D\Pi$. Hence $$\det(I-D\Pi)
 =1-\operatorname{tr}D\Pi+\det D\Pi
 =4-\operatorname{tr}M.
 \label{eq:det-identity-app}$$

The stored four-dimensional physical diagonal entries have flattened indices $0,7,14,21$; augmented parameter and period coordinates are not included. For each transcript the directed interval is $$=
 \left[4-\sum_{j=0}^{3}M_{jj}^{+},
       4-\sum_{j=0}^{3}M_{jj}^{-}\right].
 \label{eq:directed-det-interval}$$ The exact-fraction lower endpoints exceed three for all 202 jobs. Their 18-place downward displays are those in [\[eq:gap-minima\]](#eq:gap-minima){reference-type="ref" reference="eq:gap-minima"}. Maximum interval widths are $0.054493101512001146$ and $0.025036862429395394$ at 128 and 256 bits. These widths suffice for the strict inequality but do not satisfy the separate, still-open Taylor-identity residual target.

# Protocols, provenance, and reproduction {#app:reproducibility}

The source, frozen inputs, accepted proof objects, invalidated attempts, and independent checkers are distributed with the paper package. The following paths are relative to the Paper 02 project root.

::: {#tab:proof-records}
  Claim                                 Human-readable authority   Result archive
  ------------------------------------- -------------------------- ------------------------------------------------
  Whole-shell small-energy uniqueness                              analytic proof; no production archive required
  Contiguous local branch
  Local monodromy gap
  Representative local complement
  All-slab local complement
  Spectral diagnostic                   , Section 9

  : Principal citable proof records.
:::

The L1 branch release-provenance file has SHA-256

6c3a23e38bf2bd3b66a152c1 dc6590881bc52baf51818fd988d3200b

and the monodromy-gap release-provenance file has SHA-256

c7ab2ba0935f275e8810804bf8acff44 ac76a7bc01a7ddabb6367e163bea10df

These identifiers bind the release records; the manifests inside those records bind the detailed source and result objects.

The representative-complement release-provenance file has SHA-256

5b7397bac1d577014551e6c03f708b1a 729146b8cbe306f3756fafdbfedd5ad0

and binds the six frozen trees, their exact transcripts, the release-bound CAPD executable, the independent checker, and the A4.14 scope certificate. The six trees contain 3,016 evaluated nodes and 1,532 terminal leaves; all leaves are energy or necessary-return exclusions. The independent replay performed 89,962 exact-decimal checks with zero failures. This is an implementation certificate on three parameter slabs, not an all-slab theorem.

The all-slab release-provenance file has SHA-256

9d4965645c717735d18286e766103676 8038cbd42596f04b8a2b08bc1925c4c1

and binds 19 compact roles, including the A4.15 certificate, formal freezes, aggregate objects, independent checker, and postcheck. The accepted archive contains 102 trees and 52,790 evaluated nodes. Its 3,368 energy-exclusion leaves and 23,435 necessary-return-exclusion leaves exhaust the complement, and 158,782 independent checks pass with zero failures. The canonical archive-generation digest is .

From the Paper 02 project root, the accepted release hashes can be audited without rewriting the archives by running

    python scripts/audit_release_hashes.py

When the bulk A1 tree archive is available locally, the complete release DAG can be replayed without writing by running

    PYTHONDONTWRITEBYTECODE=1 python \
      scripts/build_r401_val_l2_a1_release_provenance.py \
      --project-root "$PWD" --verify-only

The focused contract tests can be run with

    PYTHONDONTWRITEBYTECODE=1 pytest -q -p no:cacheprovider \
      tests/test_r401_val_l1_contract.py \
      tests/test_r401_val_l2_s0_contract.py \
      tests/test_r401_val_l2_a1_release_provenance.py

The L2 contract tests alone do not promote an implementation run. The separately sealed A4.14 release licenses the stated three-slab smoke, while the A4.15 release extends only the local reduced-root certificate to all 51 slabs.

Rebuilding the validated executable requires the separately pinned CAPD, MPFR, GMP, compiler, and flag configuration under `validated/`. The official CAPD source is identified by a commit. Exact executables bound by authoritative release manifests are mirrored for fresh-clone hash replay; binaries from invalid or superseded attempts and LaTeX auxiliary files are excluded from version control.

The compact A4.15 certificate, aggregate, checker, postcheck, and release objects are mirrored in Git. Its 1.2-GiB raw-node directory and bulk tree payloads/manifests are intentionally excluded from ordinary Git. A fresh clone can audit the compact 19-role release, but complete raw-node replay and the deep A1 command above require a separately transferred immutable bulk archive.

For audit transparency, failed and superseded attempts remain in `results/` with explicit non-licensing markers. They must not be cited as proof objects. The release labels , , and all carry ; none of them means that the global R401-VAL theorem-domain programme is complete.
