---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--paper-01-clock-preserving-henon"
canonical_tex: "zeta_mvp0/paper_01_clock_preserving_henon/manuscript/main.tex"
canonical_pdf: "zeta_mvp0/paper_01_clock_preserving_henon/artifacts/paper_01_analytic_v3_round2_final.pdf"
source_sha256: "b36cf28446b6dad07cb38be3a33b3e5b3cee79b481a9d7cb53ab52c4b2dbc09b"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Clock-Preserving Hénon Warps of an Exponential Schrödinger Operator: Strict One-Step Ground-State Ordering and Relative Heat Asymptotics

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/paper_01_clock_preserving_henon>)
- [规范 TeX](<../../../../../zeta_mvp0/paper_01_clock_preserving_henon/manuscript/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/paper_01_clock_preserving_henon/artifacts/paper_01_analytic_v3_round2_final.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/paper_01_clock_preserving_henon/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/paper_01_clock_preserving_henon/manuscript/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We construct a zero-input family of self-adjoint Schrödinger operators in which area-preserving Hénon warps retain a prescribed mean spectral clock. Within its centered one-step nonmagnetic subfamily, the warp is proved to change the spectrum: $$\mathcal{H}_{a,n,B}=\frac12(-\mathrm{i}\nabla-A_B)^2+
   2\pi\exp\!\left(\pi|\widetilde H_a^n(q)|^2\right).$$ Here $\widetilde H_a$ is centered and area preserving, and $A_B$ is a constant-field vector potential. Every proper determinant-one configuration warp gives the exact classical count $$\mathcal{N}_{\mathrm{cl}}(E)=\frac{E}{2\pi}\log\frac{E}{2\pi}
   -\frac{E}{2\pi}+1.$$ For fixed $a>-1$, $a\neq0$, iterate $n$, and field $B$, we prove compact resolvent and the two-growing-term quantum law $$N_{a,n,B}(E)=\frac{E}{2\pi}\log\frac{E}{2\pi}
   -\frac{E}{2\pi}+
   O_{a,n,B}\!\left(E^{3/4}(\log E)^{1+2^{n-1}}\right).$$ Equal mean counts do not make the warp spectrally inert. For the centered one-step nonmagnetic subfamily, put $$\mathsf H_{a,\hbar}
   =-\frac{\hbar^2}{2}\Delta+
   2\pi e^{\pi|\widetilde H_a(q)|^2}.$$ For every fixed $a>-1$, $a\ne0$, and $\hbar>0$, symmetric rearrangement proves $$\lambda_1(\mathsf H_{a,\hbar})>\lambda_1(\mathsf H_{0,\hbar}).$$ Moreover, if $L=\log(1/(2\pi t))$, then the relative heat trace satisfies $$\operatorname{Tr}(e^{-t\mathsf H_{a,\hbar}})-\operatorname{Tr}(e^{-t\mathsf H_{0,\hbar}})
   =-\frac{a^2}{24\pi}
   \left[L^2+\bigl(2(1-\gamma)+4\pi r_a^2\bigr)L+\kappa_a\right]
   +O_{a,\hbar}(tL^4),$$ where $\gamma$ is Euler's constant, $r_a=(1+\sqrt{1+a})^{-1}$, and $\kappa_a$ is explicit. For this one-step scalar pair, the low-energy and high-temperature invariants independently prove genuine nonisospectrality. The radializing coordinate change also exposes a variable determinant-one kinetic metric, while a nonzero field removes the standard reflected-conjugation repair for the centered $n=1,2$ cases. Frozen classical and 140-level quantum calculations provide supporting diagnostics of sampled classical chaos and a finite-window orthogonal-to-unitary response. No prime or zero array enters the operator, theorems, or present runs; $a=1.02$ is inherited from an earlier zero-exposed programme and is not selected by the new theorems. Thus the family is a Hilbert--Pólya-motivated testbed with an exact mean clock and a rigorously nonisospectral centered one-step scalar subfamily, but no endogenous prime-power trace, zeta-zero identification, or claim toward the Riemann hypothesis.
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
  Clock-Preserving Hénon Warps of an Exponential Schrödinger Operator:\
  Strict One-Step Ground-State Ordering and Relative Heat Asymptotics
```

## Markdown 正文

# Introduction {#sec:introduction}

The Hilbert--Pólya idea asks for more than a real sequence that resembles the ordinates of the nontrivial zeros of the Riemann zeta function. At minimum, one seeks one fixed self-adjoint object, the correct Riemann--von Mangoldt mean count, genuine spectral structure beyond that mean, and an endogenous explanation of the prime-power explicit formula [@Riemann1859; @TitchmarshHeathBrown1986; @BerryKeating1999]. These requirements live at different logical levels. Self-adjointness makes a real spectrum possible; a Weyl law fixes only its smooth density; a nonisospectrality theorem shows that a deformation is quantum mechanically active; chaotic statistics constrain local fluctuations; and an Euler-product trace would have to encode the arithmetic phases $r\log p$. No earlier layer automatically supplies a later one.

The mathematical question addressed here is deliberately narrower but structural: can a centered one-step area-preserving Hénon deformation leave an entire prescribed mean clock unchanged and nevertheless be proved to change the true scalar quantum spectrum? Equal configuration-sublevel measures make the leading phase-space data identical, so a variable-metric representation alone does not answer this question; accidental abstract isospectrality would remain possible. For this one-step nonmagnetic subfamily, we close that gap in two complementary regimes. A rearrangement argument strictly separates the ground states, while a Brownian-bridge argument produces an explicit nonzero short-time relative heat invariant. The result is "same clock, unequal spectra" for this subfamily, not merely a numerical indication that the warp is active.

The starting potential is $$V_0(q)=2\pi e^{\pi|q|^2}.$$ Its four-dimensional classical phase volume evaluates to $$\frac{E}{2\pi}\log\frac{E}{2\pi}-\frac{E}{2\pi}+1.$$ We compose the radius with a centered, determinant-one Hénon iterate $\Psi_{a,n}=\widetilde H_a^n$, and add a constant magnetic field: $$\mathcal{H}_{a,n,B}
 =\frac12(-\mathrm{i}\nabla-A_B)^2+
 2\pi e^{\pi|\Psi_{a,n}(q)|^2}.
 \label{eq:intro-operator}$$ The configuration warp preserves every sublevel area, while the vector potential translates every momentum fiber. Consequently both deformations preserve the complete classical phase-volume function, not merely its leading coefficient.

The parameter $a=1.02$ has a specific and limited status. The author's published work gives the broader low-dimensional deterministic-chaos and prime-distribution context [@Wang2026PrimeChaos]; the Hénon-specific choice $a=1.02$ was fixed in a separate preprint [@Wang2026HenonPreprint], before [\[eq:intro-operator\]](#eq:intro-operator){reference-type="ref" reference="eq:intro-operator"} and before the numerical gates in this work were defined. It is therefore a useful prior-frozen nonlinear candidate rather than a value selected by the present Weyl theorem or reoptimized in the present runs. The earlier programme was RH-motivated and had been exposed to finite zero comparisons, so the value is not claimed to be statistically blinded. No prime or zero array enters the present operator, theorem, or computations. In fact, the mean clock below is independent of $a$. The value $a=6$ is retained as a deliberately severe high-distortion control, not as the flagship nonlinear test case.

The main contributions are as follows.

1.  We prove a general phase-volume identity: every proper determinant-one configuration warp, with any vector potential, preserves an exact classical comparator carrying the two growing Riemann--von Mangoldt terms.

2.  For every fixed $a>-1$, $a\neq0$, fixed iterate $n$, and fixed constant field $B$, we construct a Friedrichs operator with compact resolvent and prove the two-growing-term quantum asymptotic $$N_{a,n,B}(E)=\frac{E}{2\pi}\log\frac{E}{2\pi}
     -\frac{E}{2\pi}+
     O_{a,n,B}\!\left(E^{3/4}(\log E)^{1+2^{n-1}}\right).$$

3.  For the centered one-step nonmagnetic pair, symmetric rearrangement gives the strict spectral ordering $\lambda_1(\mathsf H_{a,\hbar})>\lambda_1(\mathsf H_{0,\hbar})$ for every fixed $a>-1$, $a\ne0$, and $\hbar>0$. Thus equal sublevel areas and equal growing Weyl terms do not produce isospectrality.

4.  For the same pair we prove a uniform small-time relative heat expansion with leading term $-a^2\log^2(1/(2\pi t))/(24\pi)$. The proof cancels the common classical term pointwise and controls the noncompact Brownian remainder.

5.  We retain the broader geometry, symmetry, and numerical audit. The warp becomes a variable determinant-one kinetic metric, the centered $n=1,2$ potentials admit no standard reflected-conjugation repair at nonzero field, and frozen classical and finite-window quantum diagnostics survive independent numerical checks. These supporting computations are not chaos or random-matrix universality theorems.

![image](<../../../../../zeta_mvp0/paper_01_clock_preserving_henon/figures/rendered/fig1_clock_preserving.pdf>){width="98%"}

The present construction and runs are zero-input: no zeta ordinate or prime table enters the operator, theorem, classical screen, or spectral discretization. This is an input audit rather than a claim that the inherited parameter lineage was statistically blinded. It prevents a smooth clock or a random-matrix statistic from being promoted into an arithmetic conclusion. We establish a canonical relative counting shift and higher-resolvent spectral-shift framework for the general radial/warped pair. For the special one-step scalar pair, the new relative heat theorem gives a nonzero analytic invariant inside that container. It closes operator spectral activity, not the arithmetic bridge: no family of periods $r\log p$, no von-Mangoldt amplitude, and no identification of individual zeros is derived. The result is thus best read as a Hilbert--Pólya- motivated testbed for separating a prescribed mean count and genuine spectral deformation from an Euler-product trace. The missing bridge remains visible rather than hidden in a fit.

The paper is organized as follows. positions the construction against mean-count engineering, rearrangement theory, noncompact heat asymptotics, magnetic Weyl laws, Hénon quantization, and quantum-chaos symmetry. proves the exact classical invariant, and [4](#sec:quantum-weyl){reference-type="ref" reference="sec:quantum-weyl"} proves the quantum two-term law. proves strict one-step spectral activity and the relative heat asymptotic before auditing the broader geometry and antiunitary symmetry. report frozen classical and quantum tests. Finally, [8](#sec:arithmetic-boundary){reference-type="ref" reference="sec:arithmetic-boundary"} gives the gate ledger, relative spectral container, and hard boundary on arithmetic interpretation.

# Closest work and novelty boundary {#sec:related}

## Spectral approaches to the zeta zeros

The Hilbert--Pólya programme is commonly separated into mean-count, symmetry-statistics, and trace-formula questions. The semiclassical $xp$ picture explains why an $E\log E-E$ phase volume is natural [@BerryKeating1999], while noncommutative and absorption-spectrum interpretations place the explicit formula at the centre [@Connes1999]. Self-adjoint realizations and regularizations of $xp$-type models have been developed in several settings [@Sierra2008; @SierraTownsend2008; @SierraRodriguezLaguna2011; @EndresSteiner2010; @GiordanoNegroTateo2023]. Other proposals engineer one-dimensional potentials, quantum graphs, or operator transforms to reproduce a counting law or finite spectral data [@WuSprung1993; @SchumayerVanZylHutchinson2008; @KuipersHummelRichter2014; @Yakaboylu2024]. These works show both the productivity and the weakness of mean-count matching: many non-equivalent objects can share the leading density. Broad critical discussions include @SchumayerHutchinson2011, @Lagarias2009, @Rahm2022, and @Crehan1995.

The statistical evidence for a unitary symmetry class originates in pair correlation and high-zero computations [@Montgomery1973; @Odlyzko1987; @RudnickSarnak1996]. Katz--Sarnak families and characteristic-polynomial results place those observations in a wider symmetry framework [@KatzSarnak1999Zeros; @KatzSarnak1999; @KeatingSnaith2000]. Random-matrix agreement remains a statistical constraint, not a replacement for an Euler product.

## Weyl laws, magnetic fields, and symmetry

Classical Weyl asymptotics for confining Schrödinger and pseudodifferential operators are well established [@Rozenblum1974; @HelfferRobert1982; @Tachizawa1992; @Ivrii2016]. Magnetic self-adjointness and spectral asymptotics have likewise been studied under broad hypotheses [@LeinfelderSimader1981; @AvronHerbstSimon1978; @Tamura1987; @Matsumoto1991; @DimassiDuong2014]. Accordingly, the statement that a fixed magnetic field leaves the principal phase volume unchanged is not claimed as a new general phenomenon. The specific contribution here is an explicit warped exponential family for which the entire classical comparison function is exact and both growing quantum coefficients are retained with a direct fixed-iterate remainder.

The threefold symmetry classification goes back to @Dyson1962. The Bohigas--Giannoni--Schmit conjecture and periodic-orbit theory connect classical chaos with local spectral statistics [@BohigasGiannoniSchmit1984; @Gutzwiller1971; @Gutzwiller1990; @Berry1985; @Haake2010]. Orthogonal--unitary crossover under broken time reversal is itself a standard quantum-chaos phenomenon [@PandeyMehta1983; @SaitoEtAl2009]. We claim only its controlled realization, at finite spectral resolution, inside a family whose mean clock is analytically held fixed. The scalar magnetic model has no $T^2=-1$ spin structure and therefore does not implement a GSE transition.

## Rearrangement and noncompact heat traces

Symmetric rearrangement orders Dirichlet energies and potential integrals through the Pólya--Szegő and Hardy--Littlewood inequalities [@LiebLoss2001]. Equality is substantially more rigid than the weak inequality: the Brothers--Ziemer classification identifies when equality in Pólya--Szegő forces a function to be a translate of its symmetric decreasing rearrangement [@BrothersZiemer1988]. Multiple-integral rearrangement inequalities also underlie finite-product heat-kernel comparisons [@BrascampLiebLuttinger1974]. We do not claim these principles as new. Their role here is to turn equimeasurability of a concrete Hénon-warped potential into a strict ground-state ordering after the equality case is excluded by its quartic geometry.

Heat-trace expansions on unbounded domains require global control that is absent from a compact-set diagonal expansion. Resummed expansions have been developed for polynomially confining potentials [@Fucci2018], while Brownian bridges and Feynman--Kac formulae provide a direct functional- integral route [@Simon2005FunctionalIntegration; @BoldtGueneysu2023]. The potentials here are exponential, the radial and warped members differ in both unbounded relative directions, and the effective spatial region grows as $t\downarrow0$. The relative heat theorem below is therefore not quoted from a local heat-kernel expansion. Its uniform remainder follows from common-coordinate cancellation, a Taylor expansion in Brownian amplitude, and a moving main/tail decomposition specialized to one Hénon warp.

## Hénon dynamics and geometric deformation

Area-preserving quadratic Hénon maps provide a classical laboratory for mixed and hyperbolic dynamics [@Henon1969; @DevaneyNitecki1979]. They have also been quantized as maps [@FornaessWeickert2000], within the broader quantum-map tradition [@BerryEtAl1979]. Hénon--Heiles Hamiltonians and magnetic perturbations supply related autonomous examples [@HenonHeiles1964; @BrackEtAl1993; @BrackEtAl1995]. The present operator is different from a quantized Hénon map and from the Hénon--Heiles polynomial potential: a fixed Hénon iterate warps the radius inside a static exponential potential, while the Euclidean kinetic term remains in physical coordinates.

Equal sublevel measures do not generally imply equal spectra. Isospectral potential and metric constructions require additional mechanisms [@GordonSchueth2003; @DharEtAl2003]. In our family, a unitary coordinate change sends the potential to the radial one but introduces a nonconstant determinant-one kinetic metric. That identity alone would not exclude accidental abstract isospectrality. For the centered one-step nonmagnetic pair, the strict ground-state and relative-heat theorems do: rearrangement orders the ground energies, its equality case is excluded by the quartic Hénon geometry, and a second invariant separates weighted full spectra.

## Precise novelty claim

The elementary general identity $$|\det D\Psi|=1
 \quad\Longrightarrow\quad
 |\{V_0\circ\Psi<E\}|=|\{V_0<E\}|$$ is not presented as a new principle. Nor are generic GOE--GUE crossover or generic magnetic Weyl theory. The paper's contribution is their controlled combination:

1.  an explicit Hénon-warped, self-adjoint exponential family with an exact classical comparator carrying the two growing Riemann--von Mangoldt terms;

2.  a direct fixed-iterate, fixed-field two-growing-term quantum theorem;

3.  a strict ground-state nonisospectrality theorem and an explicit uniform relative heat asymptotic for the one-step nonmagnetic pair;

4.  the general variable-metric representation and the centered $n=1,2$ reflected-conjugation obstruction; and

5.  frozen classical and cross-stencil quantum controls that test the active-deformation premise without zero or prime input.

We therefore describe the construction as an *iso-Weyl laboratory with a preserved spectral clock*. Its centered one-step nonmagnetic subfamily has a prescribed mean count and rigorously unequal spectra, while the broader family supplies geometric deformation and antiunitary-symmetry diagnostics. It is a Hilbert--Pólya-motivated testbed, not a Hilbert--Pólya solution, and it does not yet contain the prime-power explicit formula.

# Centered Hénon warps and the exact classical clock {#sec:model-clock}

The construction begins with a radial potential whose classical phase volume can be evaluated exactly. A determinant-one configuration map then changes the force field without changing configuration volume. This section isolates that elementary invariant before any quantum or statistical interpretation is introduced.

## The operator family

For $a>-1$, define the positive fixed point $$r_a=\frac{1}{1+\sqrt{1+a}}$$ of the area-preserving Hénon map $$H_a(x,y)=(1-ax^2-y,x).$$ Translation by $(r_a,r_a)$ gives the centered conjugate $$\widetilde H_a(x,y)=(-c_ax-ax^2-y,x),
 \qquad c_a=2ar_a=2(\sqrt{1+a}-1).
 \label{eq:centered-henon}$$ Its inverse and Jacobian are $$\widetilde H_a^{-1}(u,v)=(v,-c_av-av^2-u),
 \qquad
 D\widetilde H_a(x,y)=
 \begin{pmatrix}-c_a-2ax&-1\\1&0\end{pmatrix},$$ so $\det D\widetilde H_a=1$. Both the map and its inverse are polynomial. Every fixed iterate $\Psi_{a,n}=\widetilde H_a^n$ is therefore a proper, area-preserving polynomial automorphism. When $a\ne0$, its degree and the degree of its inverse are $D=2^n$.

Let $$V_{a,n}(q)=2\pi\exp\!\left(\pi|\Psi_{a,n}(q)|^2\right),
 \qquad
 A_B(x,y)=\frac{B}{2}(-y,x),
 \label{eq:potential-vector}$$ and consider the Friedrichs realization on $L^2(\mathbb{R}^2)$ of $$\boxed{
 \mathcal{H}_{a,n,B}
 =\frac12(-\mathrm{i}\nabla-A_B)^2+V_{a,n}.}
 \label{eq:main-operator}$$ The parameter $B\in\mathbb{R}$ is fixed. Three values of $a$ have distinct roles. The limit $a=0$ gives $\widetilde H_0(x,y)=(-y,x)$, hence the exactly radial integrable control $V_{0,n}(q)=2\pi e^{\pi|q|^2}$. The value $a=1.02$ was fixed by an earlier Hénon study before the present operator was proposed; it is the primary nonlinear test case, not a parameter selected by the theorem below. The value $a=6$ is retained as a high-distortion and independently motivated hyperbolic control.

## A general clock-invariance theorem

The Hénon formula is not needed for the classical identity. The invariant is the pushforward of configuration area.

[\[thm:classical-clock\]]{#thm:classical-clock label="thm:classical-clock"} Let $\Psi:\mathbb{R}^2\to\mathbb{R}^2$ be a proper $C^1$ diffeomorphism with $|\det D\Psi|=1$, and set $V_\Psi(q)=2\pi e^{\pi|\Psi(q)|^2}$. For any vector potential $A(q)$, assumed measurable, the classical symbol $$h_{\Psi,A}(q,p)=\frac12|p-A(q)|^2+V_\Psi(q)$$ has normalized phase volume $$\mathcal{N}_{\mathrm{cl}}(E)
 :=\frac{1}{(2\pi)^2}
 \operatorname{vol}\{(q,p):h_{\Psi,A}(q,p)<E\}
 =\frac{E}{2\pi}\log\!\frac{E}{2\pi}-\frac{E}{2\pi}+1
 \label{eq:exact-classical-clock}$$ for $E\ge2\pi$. For $E<2\pi$, the phase volume is zero.

At fixed $q$, the momentum translation $p'=p-A(q)$ preserves Lebesgue measure. The momentum disk has area $2\pi(E-V_\Psi(q))_+$, so $$\mathcal{N}_{\mathrm{cl}}(E)=\frac{1}{2\pi}\int_{\mathbb{R}^2}(E-V_\Psi(q))_+\,\mathrm{d}q.
 \label{eq:momentum-reduction}$$ The change $u=\Psi(q)$ preserves configuration measure. Writing $L(E)=\log(E/2\pi)$ and $R(E)=\sqrt{L(E)/\pi}$, polar integration gives $$\begin{aligned}
 \mathcal{N}_{\mathrm{cl}}(E)
 &=\frac{1}{2\pi}\int_{|u|<R(E)}
       \left(E-2\pi e^{\pi|u|^2}\right)\,\mathrm{d}u \\
 &=\int_0^{R(E)}\left(E-2\pi e^{\pi r^2}\right)r\,\mathrm{d}r
 =\frac{E}{2\pi}L(E)-\frac{E}{2\pi}+1.\end{aligned}$$

Equivalently, if $\Phi_\Psi(q)=\pi|\Psi(q)|^2$, then for $t\geq0$, $$A_{\Phi_\Psi}(t)
 :=|\{q:\Phi_\Psi(q)<t\}|=t.
 \label{eq:sublevel-invariant}$$ For $t<0$, the sublevel area is zero. The exact identity is independent of the geometry of individual level sets. It also does not require the momentum translation to be a global canonical transformation. For a magnetic vector potential with nonzero curl, it generally is not; only the fiberwise measure statement is used.

The $+1$ in [\[eq:exact-classical-clock\]](#eq:exact-classical-clock){reference-type="ref" reference="eq:exact-classical-clock"} belongs to the exact classical comparison function. The quantum remainder proved in [4](#sec:quantum-weyl){reference-type="ref" reference="sec:quantum-weyl"} is much larger than a constant. No quantum $7/8$ term, and no analogue of the oscillatory $S(T)$ term, is inferred from this identity.

displays the preimages of two radial circles. The domains differ sharply in shape while their area remains exactly $L(E)$, as required by [\[eq:sublevel-invariant\]](#eq:sublevel-invariant){reference-type="ref" reference="eq:sublevel-invariant"}.

![image](<../../../../../zeta_mvp0/paper_01_clock_preserving_henon/figures/rendered/fig2_equal_area_geometry.pdf>){width="96%"}

# Quantum two-term Weyl law at fixed magnetic field {#sec:quantum-weyl}

The identity in [\[thm:classical-clock\]](#thm:classical-clock){reference-type="ref" reference="thm:classical-clock"} is a phase-volume statement, not a quantum asymptotic. We now show that it survives quantization at the two growing orders of the Riemann--von Mangoldt clock. Throughout this section, the Hénon parameter $a$, the iterate $n$, and the magnetic field $B$ are fixed while $E\to\infty$.

## The confining magnetic operator

On $C_c^\infty(\mathbb{R}^2)$, consider $$\mathfrak h_{a,n,B}[u]
 =\frac12\|(-\mathrm{i}\nabla-A_B)u\|_2^2
  +\int_{\mathbb{R}^2}V_{a,n}(q)|u(q)|^2\,\mathrm{d}q .
 \label{eq:magnetic-form}$$ The form is closable; we use its closure and denote the corresponding Friedrichs operator by $\mathcal{H}_{a,n,B}$.

[\[prop:compact-resolvent\]]{#prop:compact-resolvent label="prop:compact-resolvent"} For every fixed $a>-1$, $n\geq1$, and $B\in\mathbb{R}$, the form in [\[eq:magnetic-form\]](#eq:magnetic-form){reference-type="ref" reference="eq:magnetic-form"} is densely defined, closable, and lower semibounded. Its closure is a closed form, and the associated Friedrichs realization is self-adjoint and has compact resolvent.

The polynomial automorphism $\Psi_{a,n}$ is proper, so $V_{a,n}(q)\to\infty$ as $|q|\to\infty$. On a fixed compact set the linear vector potential $A_B$ is bounded; hence a form-norm bounded family is bounded in the ordinary local $H^1$ norm. Rellich compactness controls the family on that compact set, whereas $$\int_{\{V_{a,n}>M\}}|u|^2
 \leq M^{-1}\int_{\mathbb{R}^2}V_{a,n}|u|^2
 \label{eq:potential-tail}$$ controls the tail uniformly as $M\to\infty$. The full argument is given in [10.2](#app:compactness){reference-type="ref" reference="app:compactness"}; see also the standard magnetic-form framework in [@Kato1995; @LeinfelderSimader1981; @BravermanMilatovicShubin2002; @MazyaShubin2005].

Let $$N_{a,n,B}(E)=\#\{k:\lambda_k(\mathcal{H}_{a,n,B})\leq E\},
 \label{eq:quantum-count-definition}$$ with multiplicity.

[\[thm:magnetic-weyl\]]{#thm:magnetic-weyl label="thm:magnetic-weyl"} Let $a>-1$, $a\neq0$, and let $n\geq1$ and $B\in\mathbb{R}$ be fixed. Put $D=2^n$. Then $$\boxed{
 N_{a,n,B}(E)
 =\frac{E}{2\pi}\log\frac{E}{2\pi}
  -\frac{E}{2\pi}
  +O\!\left(E^{3/4}(\log E)^{1+D/2}\right) }
 \label{eq:quantum-weyl}$$ as $E\to\infty$. The implied constant may depend on $a,n,B$. In particular, $$N_{a,n,B}(E)
 =\frac{E}{2\pi}\log\frac{E}{2\pi}
  -\frac{E}{2\pi}+o(E).
 \label{eq:two-growing-terms}$$

For the radial control $a=0$, the map $\Psi_{0,n}$ is orthogonal and the same argument applies with effective degree one; for example, it gives the safe bound $$N_{0,n,B}(E)
 =\frac{E}{2\pi}\log\frac{E}{2\pi}
  -\frac{E}{2\pi}
  +O\!\left(E^{3/4}(\log E)^{3/2}\right).
 \label{eq:radial-magnetic-weyl}$$ No optimality is asserted for either remainder.

## Proof architecture

We record the estimates that determine the stated error and defer their proofs to [\[app:poly-geometry,app:magnetic-count,app:weyl-assembly\]](#app:poly-geometry,app:magnetic-count,app:weyl-assembly){reference-type="ref" reference="app:poly-geometry,app:magnetic-count,app:weyl-assembly"}. Write $$L=\log(E/2\pi),\qquad R=\sqrt{L/\pi},\qquad
 \Omega_E=\{q:|\Psi_{a,n}(q)|<R\}.
 \label{eq:allowed-domain}$$ Area preservation gives $|\Omega_E|=L$. Because both $\Psi_{a,n}$ and its inverse are degree-$D$ polynomial maps, $$\operatorname{length}(\partial\Omega_E)
 =O_{a,n}(L^{D/2}),
 \qquad
 \sup_{\Psi_{a,n}^{-1}(B_{R+1})}|\nabla\Phi_{a,n}|
 =O_{a,n}(L^{D/2}),
 \label{eq:allowed-geometry}$$ where $\Phi_{a,n}=\pi|\Psi_{a,n}|^2$.

Tile $\mathbb{R}^2$ by squares $Q$ of side $$\ell=E^{-1/4}.
 \label{eq:square-scale}$$ For strict local counts, with the count set equal to zero at nonpositive energy, Dirichlet--Neumann bracketing gives $$\sum_Q n_{B,D,Q}(E-V_Q^+)
 \leq N_{<}(E)
 \leq\sum_Q n_{B,N,Q}(E-V_Q^-).
 \label{eq:dn-bracketing}$$ Here $V_Q^-$ and $V_Q^+$ are the extrema of $V_{a,n}$ on $Q$, and the Neumann operator uses the covariant boundary condition $\nu\cdot(-\mathrm{i}\nabla-A_B)u=0$.

The magnetic field does not change the leading local count. On a square centered at $c_Q$, a local gauge removes $A_B(c_Q)$, leaving a residual of norm $O_B(\ell)$. Min--max comparison with the free square therefore gives, uniformly for $0\leq A\leq E$, $$n_{B,D/N,Q}(A)
 =\frac{\ell^2 A}{2\pi}+O_B(\ell\sqrt E+1).
 \label{eq:local-magnetic-count}$$ The number of squares entering the upper sum is $$M(E)=O_{a,n}\!\left(
 \frac{L}{\ell^2}+\frac{L^{D/2}}{\ell}+1\right).
 \label{eq:relevant-squares}$$ Consequently, the accumulated local lattice error is contained in $O_{a,n,B}(E^{3/4}L^{1+D/2})$.

The remaining issue is the potential variation on a boundary square. A first-exit bootstrap shows that every square meeting $\Omega_E$ is mapped into $B_{R+1}$ for sufficiently large $E$. The second estimate in [\[eq:allowed-geometry\]](#eq:allowed-geometry){reference-type="ref" reference="eq:allowed-geometry"} then yields $$V_Q^+-V_Q^-=O_{a,n}(E\ell L^{D/2}).
 \label{eq:potential-oscillation}$$ The relevant-square union has area $O_{a,n}(L)$, so the gap between the upper and lower principal Riemann sums is $$O_{a,n}(E\ell L^{1+D/2})
 =O_{a,n}(E^{3/4}L^{1+D/2}).
 \label{eq:riemann-sum-error}$$ The common principal integral is precisely the classical quantity in [\[thm:classical-clock\]](#thm:classical-clock){reference-type="ref" reference="thm:classical-clock"}. Finally, $N_{<}(E)\leq N_{\leq}(E)\leq N_{<}(E+1)$; the change of the comparison function over this unit interval is $O(\log E)$. This proves [\[thm:magnetic-weyl\]](#thm:magnetic-weyl){reference-type="ref" reference="thm:magnetic-weyl"}. General Weyl results for confining and magnetic Schrödinger operators provide context, but the explicit remainder here comes from the preceding bracketing estimates [@Rozenblum1974; @HelfferRobert1982; @Tachizawa1992; @Ivrii2016].

[\[rem:mean-resolution\]]{#rem:mean-resolution label="rem:mean-resolution"} Equation [\[eq:quantum-weyl\]](#eq:quantum-weyl){reference-type="eqref" reference="eq:quantum-weyl"} resolves the coefficients of $E\log E$ and $E$. The exact classical comparison function in [\[eq:exact-classical-clock\]](#eq:exact-classical-clock){reference-type="ref" reference="eq:exact-classical-clock"} contains $+1$, but it is intentionally not displayed as a quantum term because the quantum error is much larger than a constant. The theorem therefore determines neither the Riemann counting constant $7/8$ nor an analogue of the oscillatory term $S(E)$ [@TitchmarshHeathBrown1986]. It also gives no uniform result when $a=a(E)$, $n=n(E)$, or $B=B(E)$.

Identical growing counting terms do not imply identical spectra. The next section proves this distinction for the centered one-step scalar pair: its ground state is strictly displaced and its relative heat trace has a nonzero uniform asymptotic.

# Analytic spectral activity, geometry, and antiunitary symmetry {#sec:active}

The preceding theorem fixes a mean clock for an entire family. This would be dynamically uninformative if the Hénon map disappeared under the same change of variables that proves clock invariance. Instead, the warp moves from the potential into the kinetic tensor. For the centered one-step nonmagnetic subfamily, we now prove more: every admissible nonzero parameter $a$ strictly raises the ground-state energy relative to the radial control and produces an explicit nonzero relative heat invariant. The magnetic parameter acts in a different direction: it leaves the clock unchanged but modifies the standard geometric time-reversal test. None of these facts supplies the missing arithmetic trace.

## The warp becomes a variable kinetic metric

Let $\Psi:\mathbb{R}^2\to\mathbb{R}^2$ be a proper $C^1$ diffeomorphism with $|\det D\Psi|=1$, and define the unitary map $$(U_\Psi f)(u)=f(\Psi^{-1}u).
 \label{eq:configuration-unitary}$$ Write $\mathcal{H}_{\Psi,0}=-\frac12\Delta+2\pi e^{\pi|\Psi(q)|^2}$. If $g=U_\Psi f$, the chain rule and the determinant condition give $$\int_{\mathbb{R}^2}|\nabla_q f|^2\,\mathrm{d}q
 =\int_{\mathbb{R}^2}\nabla_u g(u)^T G_\Psi(u)\nabla_u g(u)\,\mathrm{d}u,
 \label{eq:metric-form}$$ where $$G_\Psi(u)
 =D\Psi(\Psi^{-1}u)D\Psi(\Psi^{-1}u)^T,
 \qquad \det G_\Psi(u)=1.
 \label{eq:metric-tensor}$$ Thus, at $B=0$, $$U_\Psi\mathcal{H}_{\Psi,0}U_\Psi^{-1}
 =-\frac12\nabla_u\!\cdot G_\Psi(u)\nabla_u
  +2\pi e^{\pi|u|^2}
 \label{eq:unitary-metric}$$ in the quadratic-form sense. The potential is radial in $u$, but a nonlinear Hénon warp leaves a position-dependent determinant-one kinetic metric. For the smooth maps used here, if $G_\Psi\equiv I$, then $D\Psi$ is orthogonal everywhere and Euclidean rigidity makes $\Psi$ an affine isometry. Hence the specific volume-preserving coordinate change does not reduce a nonlinear warp to the Euclidean radial operator. The metric identity alone does not exclude an unrelated accidental isospectrality; equal sublevel volume is much weaker than equality of spectra. The next two theorems exclude isospectrality for the centered one-step nonmagnetic pair, at the bottom of the spectrum and through a weighted full-spectrum invariant. No corresponding all-iterate or magnetic ordering is claimed. Metric details are in [10.5](#app:metric-symmetry){reference-type="ref" reference="app:metric-symmetry"}.

## Strict spectral activity for one centered warp {#sec:strict-ground-state}

To state the analytic activity theorems without changing the normalization of the full magnetic family, define the auxiliary one-step scalar operators $$\mathsf H_{a,\hbar}
 =-\frac{\hbar^2}{2}\Delta+V_{a,1},
 \qquad a>-1,\quad \hbar>0.
 \label{eq:scalar-hbar-family}$$ Thus $\mathsf H_{a,1}=\mathcal{H}_{a,1,0}$, while $\mathsf H_{0,\hbar}$ is the radial equimeasurable control.

[\[thm:strict-ground-state\]]{#thm:strict-ground-state label="thm:strict-ground-state"} For every fixed $a>-1$, $a\neq0$, and $\hbar>0$, $$\lambda_1(\mathsf H_{a,\hbar})
 >\lambda_1(\mathsf H_{0,\hbar}).
 \label{eq:strict-ground-state}$$ Consequently, the two operators are not isospectral, despite having identical configuration-sublevel measures. At the paper normalization $\hbar=1$, they also have the same two-growing-term Weyl law proved in [\[thm:magnetic-weyl\]](#thm:magnetic-weyl){reference-type="ref" reference="thm:magnetic-weyl"}; for general fixed $\hbar$, both members acquire the same corresponding semiclassical rescaling.

Because $\det D\widetilde H_a=1$, the potential $V_{a,1}$ is equimeasurable with $V_{0,1}(q)=2\pi e^{\pi|q|^2}$, and the latter is its symmetric increasing rearrangement. If $f^*$ denotes symmetric decreasing rearrangement, Pólya--Szegő and the layer-cake form of Hardy--Littlewood give $$\frac{\hbar^2}{2}\int|\nabla |f|^*|^2
 +\int V_{0,1}(|f|^*)^2
 \le
 \frac{\hbar^2}{2}\int|\nabla f|^2
 +\int V_{a,1}|f|^2
 .$$ See @LiebLoss2001 for the rearrangement inequalities. The Rayleigh principle gives the weak ground-state ordering. If equality held, the kinetic and potential rearrangement deficits would be nonnegative with zero sum, so equality would hold in Pólya--Szegő. The Brothers--Ziemer equality classification would then force the positive analytic warped ground state to be a translate of the radial one [@BrothersZiemer1988]. Subtracting their eigenvalue equations would make $V_{a,1}$ radial about the same point. This is impossible because the degree-four homogeneous part of $$\pi^{-1}\log\frac{V_{a,1}(x,y)}{2\pi}
 =x^2+(c_ax+ax^2+y)^2$$ is $a^2x^4$, whereas a degree-four polynomial radial about a point has leading part proportional to $(x^2+y^2)^2$. The form-domain and equality- case details are proved in [11.1](#app:strict-ground-state){reference-type="ref" reference="app:strict-ground-state"}.

At $a=0$, the centered map is the rotation $(x,y)\mapsto(-y,x)$, and equality holds. The theorem orders only the ground state; it does not order every higher eigenvalue or assert an all-time heat-trace ordering. The independent short-time heat statement is proved next.

## Uniform relative heat activity {#sec:relative-heat-activity}

The ground-state theorem is a low-energy certificate. A complementary weighted full-spectrum certificate appears at high temperature. Put $$\Theta_{a,\hbar}(t)=\operatorname{Tr}(e^{-t\mathsf H_{a,\hbar}}),
 \qquad
 I_a(t)=\int_{\mathbb{R}^2}e^{-tV_{a,1}(q)}
 |\nabla V_{a,1}(q)|^2\,\mathrm{d}q,
 \label{eq:heat-activity-definitions}$$ and, for $k=1,2$, $$A_k(\lambda)=\int_\lambda^\infty
 we^{-w}\left(\log\frac{w}{\lambda}\right)^k\,\mathrm{d}w.
 \label{eq:Ak-definition}$$

[\[thm:relative-heat-activity\]]{#thm:relative-heat-activity label="thm:relative-heat-activity"} Fix $a>-1$ and $\hbar>0$, and put $L=L(t)=\log(1/(2\pi t))$. Let $\gamma$ denote Euler's constant. As $t\downarrow0$, $$\Theta_{a,\hbar}(t)-\Theta_{0,\hbar}(t)
 =-\frac{t^2}{48\pi}\bigl(I_a(t)-I_0(t)\bigr)
 +O_{a,\hbar}(tL^4),
 \label{eq:relative-heat-carrier}$$ where the first-gradient carrier is exactly $$I_a(t)-I_0(t)
 =\frac{2a^2}{t^2}
 \left[A_2(2\pi t)+4\pi r_a^2A_1(2\pi t)\right].
 \label{eq:exact-gradient-carrier}$$ Consequently, $$\begin{aligned}
 \Theta_{a,\hbar}(t)-\Theta_{0,\hbar}(t)
 =-\frac{a^2}{24\pi}\Bigg[&L^2+
 \bigl(2(1-\gamma)+4\pi r_a^2\bigr)L
 \notag\\
 &+\frac{\pi^2}{6}-2\gamma+\gamma^2
 +4\pi r_a^2(1-\gamma)\Bigg]
 +O_{a,\hbar}(tL^4).
 \label{eq:relative-heat-full-asymptotic}\end{aligned}$$ In particular, for $a\ne0$, $$\lim_{t\downarrow0}
 \frac{\Theta_{a,\hbar}(t)-\Theta_{0,\hbar}(t)}{L^2}
 =-\frac{a^2}{24\pi}<0.
 \label{eq:relative-heat-leading-limit}$$

For $a=1.02$, the explicit form is $$\Theta_{a,\hbar}(t)-\Theta_{0,\hbar}(t)
 =-0.0137987335661
 \left[L^2+2.98907358486L+1.72992096098\right]
 +O_{\hbar}(tL^4).
 \label{eq:a102-relative-heat}$$ This value illustrates the prior-frozen flagship parameter; the theorem holds for every fixed admissible $a$ and therefore does not select $a=1.02$ arithmetically.

Write $Q_a=\widetilde H_a^{-1}$, $W(z)=2\pi e^{\pi|z|^2}$, and $\varepsilon=\hbar\sqrt t$. The diagonal Brownian-bridge Feynman--Kac formula [@Simon2005FunctionalIntegration; @BoldtGueneysu2023] and the area-preserving variable $z=\widetilde H_a(q)$ give $$\Theta_{a,\hbar}(t)=\frac1{2\pi\hbar^2t}
 \int_{\mathbb{R}^2}\mathbb E\exp\!\left[-t\int_0^1
 V_{a,1}(Q_a(z)+\varepsilon\mathbf b_s)\,\mathrm{d}s\right]\,\mathrm{d}z.$$ At zero Brownian amplitude, the integrand is $e^{-tW(z)}$, independently of $a$, so the complete classical heat term cancels pointwise. Bridge symmetry removes odd amplitude orders; its covariance produces the second- order coefficient in [\[eq:relative-heat-carrier\]](#eq:relative-heat-carrier){reference-type="ref" reference="eq:relative-heat-carrier"}, and angular integration gives [\[eq:exact-gradient-carrier\]](#eq:exact-gradient-carrier){reference-type="ref" reference="eq:exact-gradient-carrier"}. For the remainder, split paths at $\sup_s|\mathbf b_s|=\delta/(\hbar\sqrt tL)$ and space at $\pi|z|^2=L+8\log L$. Normalized Hénon derivative estimates bound the integrated fourth amplitude derivative by $O_a(L^4)$ on the good event; Gaussian bridge tails, pathwise Jensen, and incomplete-Gamma decay control the complement without multiplying a small probability by infinite spatial volume. The resulting pre-prefactor remainder is $O_{a,\hbar}(t^2L^4)$, which proves [\[eq:relative-heat-carrier\]](#eq:relative-heat-carrier){reference-type="ref" reference="eq:relative-heat-carrier"}. The full argument, including dominated differentiation on the bad event, is in [11.2](#app:relative-heat-proof){reference-type="ref" reference="app:relative-heat-proof"}.

The theorem is restricted to one centered warp, zero magnetic field, and fixed $\hbar>0$. The leading coefficient is independent of fixed $\hbar$ in two dimensions because the first-gradient factor $\hbar^2$ cancels the free heat-kernel prefactor $\hbar^{-2}$. The proof does not cover a varying $\hbar(t)$, a magnetic Feynman--Kac--Itô phase, or higher Hénon iterates without a new derivative audit. It proves spectral activity, not a prime-power trace.

![image](<../../../../../zeta_mvp0/paper_01_clock_preserving_henon/figures/rendered/fig8_relative_heat_asymptotic.pdf>){width="96%"}

## The standard geometric time-reversal audit

Let $\mathcal C$ denote complex conjugation. Since the potential and the chosen vector potential are real, $$\mathcal C\mathcal{H}_{a,n,B}\mathcal C=\mathcal{H}_{a,n,-B}.
 \label{eq:conjugation-flips-B}$$ At $B=0$, $\mathcal C$ is an internal antiunitary symmetry and $\mathcal C^2=+1$, the standard scalar orthogonal-class structure [@Dyson1962]. At a fixed $B\neq0$, bare conjugation is not an internal symmetry. An orientation-reversing Euclidean isometry preserving the potential could still repair it: the reflected conjugation $U_S\mathcal C$ also reverses the magnetic pseudoscalar.

[\[lem:no-reflection\]]{#lem:no-reflection label="lem:no-reflection"} Let $a>-1$, $a\neq0$, and $n\in\{1,2\}$. No orientation-reversing Euclidean isometry $S$ satisfies $$|\widetilde H_a^n(Sq)|^2=|\widetilde H_a^n(q)|^2
 \quad\text{for every }q\in\mathbb{R}^2.
 \label{eq:no-reflection-condition}$$ Consequently, at fixed $B\neq0$, the operator has no time-reversal repair of the standard reflected-conjugation form $U_S\mathcal C$.

The proof in [10.5.1](#app:reflection-proof){reference-type="ref" reference="app:reflection-proof"} uses both the highest homogeneous term and the quadratic Taylor form at the unique potential minimum. The scope is exact: the lemma covers the centered production cases $n=1,2$, but it does not rule out every abstract nonlocal antiunitary and does not claim a result for all $n\geq3$. The radial control $a=0$ retains reflections, and the uncentered one-iterate Hénon potential has an accidental $x\mapsto-x$ reflection. Centering therefore matters to this symmetry audit. Finally, a scalar magnetic model supplies an orthogonal-to-unitary test family; it has no spin-$1/2$ antiunitary with $T^2=-1$, so it is not a symplectic/GSE construction.

The signed relative-spectrum container and the prime-power gate are kept together in [8](#sec:arithmetic-boundary){reference-type="ref" reference="sec:arithmetic-boundary"}. In particular, the heat invariant proved above is a short-time Laplace-weighted certificate of nonisospectrality; it is not promoted here to a fixed-time orbit trace or an arithmetic explicit formula.

# Zero-input classical diagnostics {#sec:classical-dynamics}

[\[sec:classical\]]{#sec:classical label="sec:classical"}

The clock theorem does not imply that the Hamiltonian flow is chaotic: an area-preserving warp can preserve phase volume while changing the force field in many dynamically inequivalent ways. We therefore screened the classical flow directly, without loading a prime table, a Riemann-zero ordinate, or a spectral fitting target. The experiments in this section test only whether the centered nonlinear members display stable chaotic diagnostics at the sampled states and energies. They do not test ergodicity, mixing, or the measure of a chaotic component.

## Frozen sampling and diagnostics

For the nonmagnetic flow, the natural time used throughout the numerical study is $$t_{\mathrm{nat}}(E)
 =\sqrt{\frac{\log(E/2\pi)}{E}}.
 \label{eq:natural-time}$$ This scale balances a typical speed of order $E^{1/2}$ against the radial size $\log(E/2\pi)^{1/2}$ of the allowed domain in $u=\Psi_{a,n}(q)$ coordinates. Dimensionless integration time is $\tau=t/t_{\mathrm{nat}}$, and all finite-time Lyapunov exponents below are reported per unit $\tau$.

Initial conditions were generated from an unscrambled three-dimensional Sobol sequence. The first two coordinates were mapped to uniform area in the disk in $u$-space, with radius truncated to $0.88$ of the allowed radius; the third fixed the momentum angle. The inverse Hénon iterate then gave $q=\Psi_{a,n}^{-1}(u)$, and the momentum magnitude was chosen from the microcanonical constraint. This construction is deterministic and gives uniform configuration density in the truncated region, but the small frozen seed sets used here are not a phase-space census.

The primary integrator was velocity Verlet together with its analytic tangent map. Two tangent vectors were normalized in coordinates scaled by the configuration and momentum extents. If $w_1,w_2$ denote the normalized vectors, we recorded $$\lambda_T=\frac{1}{T}\log\frac{\|w_1(T)\|}{\|w_1(0)\|},
 \qquad
 \mathrm{SALI}(T)=
 \min\{\|\widehat w_1+\widehat w_2\|,
        \|\widehat w_1-\widehat w_2\|\}.
 \label{eq:ftle-sali}$$ R000 used the frozen joint flag $\lambda_T>0.05$ and $\mathrm{SALI}<10^{-4}$. The longer R001 and independent R106 audits used the stricter SALI threshold $10^{-8}$. A positive finite-time exponent by itself was never counted as a chaotic flag; this matters for the radial control, where finite-time shear produces a small positive exponent while SALI remains of order one.

## Failure-first calibration and the R000 screen

The initial common-resolution smoke run was not numerically adequate for the whole parameter grid. In particular, $a=6$ with $n=2,3$ produced extreme preimage anisotropy and nonfinite trajectories at the smoke resolution. We retain those cases as failed high-distortion branches. The calibrated R000 production cells were $(a,n)=(0,1),(1.02,1),(1.02,2),(6,1)$, at $E=100$ and $1000$, with eight primary Sobol states per cell and 80 natural-time units. The primary resolutions were respectively 2048, 4096, 8192, and 8192 steps per natural-time unit; the first two seeds in every cell were recomputed at twice that resolution.

All 80 primary and refinement records completed with relative energy drift below $10^{-4}$. At each energy the radial control had zero joint flags, whereas all eight primary states in each of the three nonlinear production families were flagged. For example, at $E=1000$ the median dimensionless FTLE/SALI pairs were $0.0592/0.951$ for the radial control, $0.7116/1.17\times10^{-15}$ for $(1.02,1)$, $1.0842/5.12\times10^{-15}$ for $(1.02,2)$, and $0.7304/1.88\times10^{-14}$ for $(6,1)$.

Fifteen of the sixteen primary/refined FTLE pairs met the frozen resolution rule. The exception was $a=6,n=1,E=1000$, seed 1, whose exponent changed from $0.6515$ to $1.0661$. This failure, together with the smoke-run stiffness at larger iterates, prevents a blanket numerical-convergence claim for the $a=6$ branch. It does not affect the separately refined $a=1.02$ core.

## Time-length convergence

R001 followed four frozen states in every production family to 160 natural units at $E=1000$, using a resolution equal to or finer than the R000 refinement. The median checkpoints are reported in [1](#tab:classical-time-convergence){reference-type="ref" reference="tab:classical-time-convergence"}. The radial FTLE decreases from $0.1777$ at $\tau=20$ to $0.0355$ at $\tau=160$, while its final median SALI is $0.768$. The nonlinear medians remain of order one and all twelve nonlinear trajectories satisfy the joint flag at $\tau=160$. Their frozen plateau ratios $\lambda_{160}/\lambda_{80}$ are $0.991$, $1.007$, and $0.890$, inside the acceptance interval $[0.6,1.4]$. All sixteen trajectories completed; the largest relative energy drift was $4.17\times10^{-6}$.

::: {#tab:classical-time-convergence}
  $(a,n)$        $\lambda_{20}$   $\lambda_{40}$   $\lambda_{80}$   $\lambda_{160}$           SALI$_{160}$   flags
  ------------ ---------------- ---------------- ---------------- ----------------- ---------------------- -------
  $(0,1)$                0.1777           0.0942           0.0569            0.0355                  0.768     0/4
  $(1.02,1)$             0.7568           0.7609           0.7560            0.7489   $3.52\times10^{-16}$     4/4
  $(1.02,2)$             1.2902           1.1069           1.2178            1.2262   $4.34\times10^{-15}$     4/4
  $(6,1)$                1.1846           1.1087           1.1073            0.9860   $5.45\times10^{-15}$     4/4

  : R001 time-length convergence at $E=1000$. Entries are medians over four frozen Sobol states. A joint flag at $\tau=160$ requires $\lambda_{160}>0.05$ and $\mathrm{SALI}_{160}<10^{-8}$.
:::

## Independent adaptive audit and the magnetic branch

R106 addressed two narrower concerns: dependence on the original Verlet implementation and survival of the classical signal at the field $B=1$ used in the core quantum comparison. It read the exact four R001 initial states for $a=0$ and $a=1.02,n=1$ at $E=1000$, then independently reimplemented the potential jet and integrated the physical-velocity system $$\dot q=v,
 \qquad
 \dot v=
 \begin{pmatrix}0&B\\-B&0\end{pmatrix}v-\nabla V_{a,1}(q)
 \label{eq:magnetic-velocity-flow}$$ with DOP853, relative tolerance $10^{-10}$, absolute tolerance $10^{-12}$, and tangent renormalization every $0.5$ natural unit. The audit covered 80 natural units and did not import the Verlet stepper.

::: {#tab:adaptive-magnetic-classical}
     $a$   $B$   $\lambda_{80}$                   SALI   flags             max. drift
  ------ ----- ---------------- ---------------------- ------- ----------------------
       0     0         0.056855                1.15149     0/4   $1.37\times10^{-10}$
       0     1         0.056616                1.18108     0/4   $4.95\times10^{-11}$
    1.02     0         0.751261   $2.11\times10^{-15}$     4/4   $9.12\times10^{-11}$
    1.02     1         0.613215   $6.15\times10^{-15}$     4/4    $1.97\times10^{-9}$

  : R106 independent adaptive audit at $E=1000$ and $\tau=80$. Values are medians over the four frozen R001 states; the drift column is the maximum within each group.
:::

Every R106 gate passed. For the nonlinear nonmagnetic cell, the ratio of the DOP853 median FTLE to the R001 Verlet median at the same duration is $0.9937$. The magnetic force lowers the sampled nonlinear median FTLE from $0.7513$ to $0.6132$, but all four states remain jointly flagged. Both radial groups remain unflagged. Thus the classical signal supporting the $B=1$ spectral branch is neither an artifact of the original integrator nor erased by that field. Four trajectories at one energy still do not establish a positive-measure chaotic sea, a Lyapunov spectrum, or asymptotic hyperbolicity.

summarizes the time-length and independent- solver checks. The distinction visible there is the one used in the rest of the paper: sampled active nonlinear dynamics versus an integrable radial control, not a global theorem about the flow.

![image](<../../../../../zeta_mvp0/paper_01_clock_preserving_henon/figures/rendered/fig3_classical_convergence.pdf>){width="98%"}

# Finite-window quantum spectra and magnetic crossover {#sec:quantum-spectra}

The Weyl theorem fixes the smooth count but says nothing about local spectral fluctuations. We therefore performed a zero-input finite-window screen of the centered $a=1.02,n=1$ operator and its magnetic deformation. The outcome is a convergence-supported orthogonal-like to unitary-like response in the available window. It is not a proof of random-matrix universality, an arithmetic selection of $B$, or evidence for any individual Riemann zero.

## Discretization and frozen observables

The primary discretization uses a Cartesian Dirichlet grid and Peierls links $$U_{ij}=\exp\!\left(-\mathrm{i}\int_{q_i}^{q_j}A_B\cdot\,\mathrm{d}q\right)
 \label{eq:peierls-link}$$ on each nearest-neighbor edge. Straight-link integration is exact for the linear symmetric and Landau gauges used here. The rectangle encloses the preimage of the contour $V=100E_{\mathrm{target}}$, with three nominal mesh steps of padding; $E_{\mathrm{target}}=450$, so the nominal wall energy is $45000$. We computed 180 low eigenvalues by deterministic shift-invert Hermitian Lanczos. Every reported local statistic uses sorted modes 25--164 inclusive: 140 levels, 139 gaps, and 138 adjacent-gap ratios.

For consecutive gaps $s_j=E_{j+1}-E_j$, the unfolding-free observable is $$\widetilde r_j=
 \frac{\min(s_j,s_{j+1})}{\max(s_j,s_{j+1})},
 \qquad
 \langle\widetilde r\rangle=\frac{1}{138}\sum_j\widetilde r_j.
 \label{eq:adjacent-ratio}$$ The reference means used descriptively are $0.38629$ for Poisson, $0.53590$ for GOE, and $0.60266$ for GUE [@AtasEtAl2013]. We also unfolded with the analytic clock $$\xi_j=\mathcal{N}_{\mathrm{cl}}(E_j)
 =\frac{E_j}{2\pi}\log\frac{E_j}{2\pi}
  -\frac{E_j}{2\pi}+1.
 \label{eq:exact-clock-unfolding}$$ No fit is involved in this transformation. Because adjacent ratios from one spectrum are dependent and the 140-level window was not sampled as an i.i.d. ensemble, empirical CDF sup distances below are deterministic discrepancy measures; we assign no $p$-values.

## The failed first grid comparison

The first production run, R100, compared nominal spacings $h=0.04$ and $0.03$. It failed the frozen one-percent median level-change gate in every cell: on the unified 25--164 window the changes ranged from $1.20\%$ for the radial control to $1.67\%$ for the $a=6$ cells, with the $a=1.02$ scalar and magnetic cells at $1.23\%$ and $1.21\%$. Consequently, R100 alone supports no random-matrix-class interpretation.

R101 was specified after that failure and added $h=0.0225$. Relative to $h=0.03$, all five cells then passed the original level gate, with median changes between $0.66\%$ and $0.93\%$. A post-hoc check compared each fine-grid mean ratio with a two-grid $h^2$ extrapolation. The differences were $0.0120$ and $0.0045$ for $a=1.02$ at $B=0$ and $1$, but $0.0404$ and $0.0347$ for $a=6$. Thus the high-distortion $a=6$ branch remains inconclusive and is assigned no spectral symmetry class. R102 froze a fourth grid, $h=0.0175$, only for the surviving $a=1.02$ core. The full failure-first sequence is shown in [\[fig:quantum-convergence\]](#fig:quantum-convergence){reference-type="ref" reference="fig:quantum-convergence"}.

![image](<../../../../../zeta_mvp0/paper_01_clock_preserving_henon/figures/rendered/fig4_quantum_convergence.pdf>){width="98%"}

## Converged core window

On the unified 25--164 window, the R102 $0.0225\to0.0175$ audit gave median relative level changes of $0.347\%$ and $0.346\%$ for $B=0$ and $1$. The fine-grid and new $h^2$-extrapolated mean ratios are listed in [3](#tab:core-quantum-window){reference-type="ref" reference="tab:core-quantum-window"}. Fine-to-extrapolated ratio differences are $0.00242$ at $B=0$ and $0.00035$ at $B=1$; the correlations between the two pointwise ratio arrays are $0.960$ and $0.974$. The exact-clock extrapolated mean spacings are $0.99915$ and $0.99903$, providing a finite-window check of the analytic mean density.

::: {#tab:core-quantum-window}
  Diagnostic                                             $B=0$      $B=1$
  ------------------------------------------------- ---------- ----------
  median level change, $0.0225\to0.0175$                0.347%     0.346%
  fine-grid $\langle\widetilde r\rangle$              0.532251   0.587617
  $h^2$-extrapolated $\langle\widetilde r\rangle$     0.529831   0.587270
  extrapolated mean unfolded spacing                  0.999151   0.999027
  fine CDF distance to GOE                              0.0448     0.1140
  fine CDF distance to GUE                              0.1526     0.0614

  : R102 core results over 140 interior levels. CDF entries are sup distances to the ratio surmises and are descriptive; no $p$-values are attached.
:::

The scalar ratio is close to the GOE reference, consistent with the $T^2=+1$ symmetry identified in [5](#sec:active){reference-type="ref" reference="sec:active"}. At $B=1$, the mean and the empirical CDF move toward the GUE reference. We call these spectra *GOE-like* and *unitary-leaning* only at this finite-window, descriptive level. The 138-ratio CDFs are displayed in [1](#fig:ratio-cdfs){reference-type="ref" reference="fig:ratio-cdfs"}.

![Empirical adjacent-ratio distributions over the frozen 138-ratio interior window. The scalar spectrum is closer to the GOE surmise, while $B=1$ moves toward the GUE surmise. Sup distances are deterministic descriptive diagnostics, not i.i.d. goodness-of-fit tests.](<../../../../../zeta_mvp0/paper_01_clock_preserving_henon/figures/rendered/fig5_ratio_cdfs.pdf>){#fig:ratio-cdfs width="72%"}

The radial member cannot serve as an untreated Poisson baseline. On the R101 fine grid its mean ratio is $0.045$, and approximately $39\%$ of the retained gaps are near-degenerate. These values reflect the continuum $m/-m$ angular-momentum doublets and their finite-grid $D_4$ remnants. A symmetry-sector decomposition would be required for a meaningful integrable-spacing comparison. Here the radial member is used only as a degeneracy and classical-integrability control.

## Frozen magnetic response

R103 fixed $B\in\{0,0.25,0.5,1,2,4\}$ before execution and evaluated all fields on the same $h=0.0225$ grid and interior window. The mean-ratio sequence was $$0.5292,\quad0.5439,\quad0.5768,\quad0.5874,\quad0.6229,
 \quad0.5980.
 \label{eq:magnetic-ratio-sequence}$$ Every nonzero field lies above the scalar baseline, so the preregistered retention gate passed. The response is not monotone. In particular, the largest value at $B=2$ is not promoted as an optimum or assigned arithmetic meaning. R104 recomputed the four new fields on the $h=0.03$ grid; median level changes were $0.677$--$0.685\%$, and coarse/fine mean-ratio differences were $0.0022$--$0.0079$, passing both frozen gates. The scan therefore supports a resolved field response rather than a single fortuitous value at $B=1$, while remaining a low-window crossover rather than an asymptotic universality result.

![image](<../../../../../zeta_mvp0/paper_01_clock_preserving_henon/figures/rendered/fig6_magnetic_crossover.pdf>){width="94%"}

## Gauge, solver, and independent-order checks

R105 repeated the $a=1.02,h=0.03$ calculation with a deterministic Lanczos initial vector. The maximum relative eigen-residual was $5.99\times10^{-10}$, and the maximum orthogonality defect was $8.04\times10^{-13}$. The $B=1$ spectra in symmetric and Landau gauges agreed to relative $2.51\times10^{-14}$; the $B=1$ and $-1$ spectra were identical at stored precision; and reruns agreed with the archived R100 arrays within $3.64\times10^{-14}$. Matrix-level tests also checked Hermiticity, Peierls plaquette flux, zero-field reality, and lattice gauge covariance.

R107 then changed the leading kinetic truncation error by using nearest- and next-nearest-neighbor Peierls links in a fourth-order covariant finite- difference stencil. Its initial run passed every cross-stencil level and ratio gate but failed the preregistered maximum-residual gate: median Ritz residuals were already near $5\times10^{-12}$, while a few edge pairs reached $1.9\times10^{-6}$ at $B=0$ and $5.0\times10^{-6}$ at $B=1$. The failure remains part of the audit record.

R107A was frozen only after that failure and changed one eigensolver guard: it requested 200 instead of 180 Ritz pairs, tightened the ARPACK tolerance from $2\times10^{-10}$ to $10^{-12}$, sorted them, and retained the lowest 180. No physical parameter, grid, box, field, analysis window, statistic, or threshold changed. The retained fine-grid maximum residuals fell to $4.65\times10^{-10}$ and $6.86\times10^{-11}$. All original R107 gates then passed, with the quantitative comparison in [4](#tab:fourth-order-check){reference-type="ref" reference="tab:fourth-order-check"}.

::: {#tab:fourth-order-check}
  Diagnostic                                                                $B=0$                  $B=1$
  -------------------------------------------------------- ---------------------- ----------------------
  fourth-order coarse/fine median level change                           0.04072%               0.04029%
  fourth-order fine vs. second-order extrap. median                      0.01943%               0.01894%
  fourth-order fine $\langle\widetilde r\rangle$                         0.534773               0.590890
  second-order extrapolated $\langle\widetilde r\rangle$                 0.529831               0.587270
  mean-ratio difference                                                  0.004942               0.003620
  pointwise ratio correlation                                            0.997432               0.995218
  fourth-order mean unfolded spacing                                     0.998484               0.998364
  max. retained fine residual                                $4.65\times10^{-10}$   $6.86\times10^{-11}$

  : R107A fourth-order finite-difference check. The reference is the archived R102 second-order $h^2$ extrapolation.
:::

R107A is an *independent-order finite-difference check*, not a second independent discretization family. Both stencils use a Cartesian grid, Peierls links, a point-sampled potential, an adapted rectangular wall, and the ARPACK eigensolver. Their physical rectangles also differ slightly with nominal spacing because the geometry includes three mesh steps of padding. The agreement rules out the simplest explanation based on second-order kinetic dispersion, but a fixed-domain magnetic finite-element or sine- Galerkin calculation remains open.

Finally, [\[fig:smooth-clock\]](#fig:smooth-clock){reference-type="ref" reference="fig:smooth-clock"} shows the exact-clock unfolding. Its near- unit mean spacing checks only the smooth density already proved in [\[thm:magnetic-weyl\]](#thm:magnetic-weyl){reference-type="ref" reference="thm:magnetic-weyl"}; the residual staircase fluctuations are not compared with zeta ordinates.

![image](<../../../../../zeta_mvp0/paper_01_clock_preserving_henon/figures/rendered/fig7_smooth_clock.pdf>){width="94%"}

Across R100--R107A, the defensible conclusion is limited: within 140 interior levels, the centered scalar spectrum is GOE-like and the fixed-field family exhibits a converged response toward the unitary class. The data do not establish GOE/GUE universality, high-energy window stability, or an endogenous prime-power trace [@BohigasGiannoniSchmit1984; @Haake2010; @PandeyMehta1983; @SaitoEtAl2009]. No prime or zero arrays were loaded in R100--R107A; the inherited, zero-exposed parameter lineage is disclosed in [1](#sec:introduction){reference-type="ref" reference="sec:introduction"}.

# Hilbert--Pólya ledger and the missing arithmetic bridge {#sec:arithmetic-boundary}

We use the present construction to illustrate a prospective breadth-first RH discovery protocol: generate structurally distinct candidates, kill them at explicit gates, and close analytic bridges only for survivors. The protocol was formalized after parts of this family had already been explored and is not a preregistered history of its selection. Its value here is prospective and methodological: it separates the proved self-adjoint/Weyl statements from sampled diagnostics and from the still-missing arithmetic bridge.

## Gates and side diagnostics

  Label                Question                                                                Present status                                                                                                                                                                                       Excluded inference
  -------------------- ----------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------
  Q                    Is there one fixed self-adjoint operator with real discrete spectrum?   Pass: Friedrichs operator with compact resolvent.                                                                                                                                                    Self-adjointness alone does not associate its spectrum with zeta zeros.
  W                    Does its count have the two growing Riemann--von Mangoldt terms?        Pass: [\[thm:magnetic-weyl\]](#thm:magnetic-weyl){reference-type="ref" reference="thm:magnetic-weyl"}, for each fixed $a,n,B$.                                                                       The remainder does not resolve $7/8$, $S(E)$, or individual ordinates.
  S$_{\mathrm{op}}$    Is the clock-preserving warp spectrally active?                         Pass for $n=1,B=0$: strict ground-state ordering and explicit relative heat asymptotics.                                                                                                             No all-iterate or magnetic ordering, higher-level ordering, chaos theorem, prime trace, or zero identification.
  S$_{\mathrm{dyn}}$   Is the classical deformation dynamically active?                        Sampled numerical support from R000--R001 and independent R106.                                                                                                                                      No theorem of positive-measure chaos, ergodicity, or mixing.
  R                    Do frozen finite windows respond in the expected symmetry direction?    Descriptive support: adjacent-ratio CDFs and magnetic response.                                                                                                                                      R is not a Hilbert--Pólya gate; finite-window GOE/GUE proximity implies no Euler product, universality, or zero identification.
  C                    Are signed relative spectral objects analytically admissible?           Pass at the individual-summability level: relative staircase, heat trace, tempered wave distribution, and the $m=3$ generalized SSF framework; the special one-step scalar heat trace is explicit.   No pairwise cancellation, closeness, first-resolvent comparability, or periodic-orbit trace formula is proved.
  P                    Does an endogenous prime-power trace occur?                             Open. No $r\log p$ periods or von-Mangoldt amplitudes are derived.                                                                                                                                   RMT agreement cannot manufacture an Euler product or explicit formula.
  Z                    Does a signed spectral fluctuation carry the explicit formula?          Not tested and not authorized before P.                                                                                                                                                              No individual-zero comparison or zero-level claim is made.
  RH                   Does the construction prove the Riemann hypothesis?                     No claim.                                                                                                                                                                                            Q, W, S, R, or C cannot substitute for the open P and untested Z gates.

The split S status is essential. The analytic theorems prove that the one-step scalar warp changes the quantum spectrum. They do not upgrade the stronger dynamical question, which continues to have sampled support only.

The exact formula for the zeta zero count contains an arithmetic oscillation whose explicit-formula dual is organized by prime powers [@Riemann1859; @TitchmarshHeathBrown1986]. A viable P gate would therefore need, without loading primes, closed structures with asymptotic times and amplitudes $$T_{\gamma_{p,r}}(E)\longrightarrow r\log p,\qquad
 A_{\gamma_{p,r}}(E)\longrightarrow
 C\,(\log p)p^{-r/2},
 \label{eq:prime-target}$$ including the correct repetition, sign, and phase laws. Neither the GOE-like scalar ratios nor their magnetic response implies [\[eq:prime-target\]](#eq:prime-target){reference-type="ref" reference="eq:prime-target"}.

## A rigorous relative spectral container {#sec:relative-container}

To isolate what remains after the common mean clock, fix $a>-1$, $a\neq0$, $n$, and $B$, and write $$\begin{aligned}
 H_0&=\mathcal{H}_{0,n,B},& H_1&=\mathcal{H}_{a,n,B},\\
 R_j(z)&=(H_j-z)^{-1},& z&\notin\mathbb{R},\\
 N_j(E)&=\#\{k:\lambda_k(H_j)\leq E\},&
 (V_0,V_1)&=(V_{0,n},V_{a,n}).
 \end{aligned}
 \label{eq:relative-pair}$$

[\[prop:relative-container\]]{#prop:relative-container label="prop:relative-container"} For the pair in [\[eq:relative-pair\]](#eq:relative-pair){reference-type="ref" reference="eq:relative-pair"}:

1.  $R_j(z)\in\mathcal{S}_p$ exactly for $p>1$, and $R_1(z)-R_0(z)\in\mathcal{S}_p$ for every $p>1$;

2.  $R_1(z)^m-R_0(z)^m\in\mathcal{S}_1$ for every integer $m\geq2$. In particular, the odd choice $m=3$ admits the generalized resolvent-power spectral-shift framework of @Yafaev2005;

3.  the canonical discrete relative staircase $$\xi(E)=N_0(E)-N_1(E)
      \label{eq:relative-staircase}$$ satisfies, for $f\in C_c^\infty(\mathbb{R})$, $$\operatorname{Tr}\bigl(f(H_1)-f(H_0)\bigr)
      =\int_\mathbb{R}f'(E)\xi(E)\,\mathrm{d}E;
      \label{eq:relative-trace-compact}$$

4.  $e^{-tH_1}-e^{-tH_0}$ is trace class for every $t>0$, while the relative spectral-propagator trace $\operatorname{Tr}(e^{-\mathrm{i}tH_1}-e^{-\mathrm{i}tH_0})$, called the relative wave trace here, is canonically defined as a tempered distribution.

The proof and precise wave-trace definition are given in [10.6](#app:relative-container){reference-type="ref" reference="app:relative-container"}. The trace-class assertions for $m\geq2$ and for the heat semigroups follow because each operator separately has the corresponding summability; they assert admissibility, not pairwise cancellation or closeness. Yafaev's abstract weighted spectral-shift function is determined up to an additive constant, whereas [\[eq:relative-staircase\]](#eq:relative-staircase){reference-type="ref" reference="eq:relative-staircase"} is the separately chosen pure-point representative normalized below both spectra.

The first resolvent is a crucial boundary: pairwise membership of $R_1(z)-R_0(z)$ in $\mathcal{S}_1$ is *not* established. Indeed, the absolute principal-symbol diagnostic diverges for every $c>0$: $$\int_{\mathbb{R}^2}\!\int_{\mathbb{R}^2}
 \left|
 \frac{1}{|p|^2/2+V_1(q)+c}
 -\frac{1}{|p|^2/2+V_0(q)+c}
 \right|\,\mathrm{d}p\,\,\mathrm{d}q=\infty.
 \label{eq:first-resolvent-obstruction}$$ This diagnostic disfavors, but does not prove failure of, the ordinary first-resolvent Krein hypothesis. The $m=3$ statement must not be promoted to first-resolvent comparability. Likewise, standard short-range perturbation assumptions do not apply because $V_1-V_0$ is unbounded in both relative directions [@FrankPushnitski2019].

The common Weyl theorem gives only $$\xi(E)=O_{a,n,B}\!\left(
 E^{3/4}(\log E)^{1+2^{n-1}}\right).
 \label{eq:relative-staircase-bound}$$ This signed container is far too coarse to identify an explicit-formula fluctuation. For the special one-step nonmagnetic pair, the ordinary relative heat trace is more than admissible. At the paper normalization $\hbar=1$, [\[thm:relative-heat-activity\]](#thm:relative-heat-activity){reference-type="ref" reference="thm:relative-heat-activity"} gives $$\Theta_{\mathrm{rel}}(t)
 =-\frac{a^2}{24\pi}
 \left[L^2+\bigl(2(1-\gamma)+4\pi r_a^2\bigr)L+\kappa_a\right]
 +O_a(tL^4),
 \label{eq:ledger-relative-heat}$$ where $L=\log(1/(2\pi t))$, $\gamma$ is Euler's constant, $r_a=(1+\sqrt{1+a})^{-1}$, and $$\kappa_a=\frac{\pi^2}{6}-2\gamma+\gamma^2+
 4\pi r_a^2(1-\gamma).$$ This explicit nonzero invariant proves spectral activity, but it neither improves the pointwise bound on $\xi(E)$ nor supplies a fixed nonzero-time wave-trace singularity.

## The prime-time obstruction and death conditions {#sec:prime-time-obstruction}

The high-energy well has radius and natural period scales $$R_E\asymp\sqrt{\log E},\qquad
 \tau_E\asymp\sqrt{\frac{\log E}{E}}.$$ A dimensional scaling estimate suggests that fixed-complexity orbit families live on times tending to zero, up to polylogarithmic distortion, whereas [\[eq:prime-target\]](#eq:prime-target){reference-type="ref" reference="eq:prime-target"} requires fixed nonzero times $r\log p$. We do not prove a uniform period theorem: this is a warning against a naive fixed-orbit identification, not a no-go result. Orbit complexity could grow with $E$. An energy-dependent rescaling is not a solution unless it arises from one fixed self-adjoint generator and retains the proved mean clock.

Thus [\[prop:relative-container\]](#prop:relative-container){reference-type="ref" reference="prop:relative-container"} passes the signed-container test, not the arithmetic prime-power gate. In particular, the high-temperature limit $t\downarrow0$ does not generate fixed nonzero wave-trace times $r\log p$, and its $L^2$ coefficient is not a von-Mangoldt amplitude.

The arithmetic branch is killed if primes must be entered term by term, if $a,B,n$ are selected from zero fits, if apparent peaks move with box, mesh, or window, or if small zero-input perturbations destroy the association. It passes only after an energy-localized relative trace theorem links stable nonzero-time singularities to independently computed periodic structures and then derives [\[eq:prime-target\]](#eq:prime-target){reference-type="ref" reference="eq:prime-target"} endogenously [@DuistermaatGuillemin1975; @CombescureRalstonRobert1999; @Gutzwiller1971].

This separation is the principal value of the present Hilbert--Pólya- motivated testbed. It shows that Q, a designed but exact W, proved operator-level spectral activity, sampled classical dynamics, and a finite- window magnetic response can coexist in one zero-input family; it also exposes why none of these ingredients substitutes for the arithmetic bridge.

# Conclusion {#sec:conclusion}

We have constructed a family in which clock-preserving deformations remain nontrivial at several distinct logical levels. A proper determinant-one Hénon warp and a fixed magnetic field leave the exact classical phase volume equal to $$\frac{E}{2\pi}\log\frac{E}{2\pi}-\frac{E}{2\pi}+1.$$ For every fixed $a>-1$, $a\neq0$, iterate, and field, the corresponding Friedrichs operator has compact resolvent and preserves the two growing terms quantum mechanically with an explicit $o(E)$ remainder.

The new analytic conclusion is that this common clock does not make the one-step scalar warp spectrally inert. For every fixed $a>-1$, $a\ne0$, and $\hbar>0$, its ground-state energy is strictly larger than that of the radial equimeasurable control. At the opposite, high-temperature end, put $L=\log(1/(2\pi t))$. Its relative heat trace obeys the complete asymptotic $$\Theta_{a,\hbar}(t)-\Theta_{0,\hbar}(t)
 =-\frac{a^2}{24\pi}
 \left[L^2+\bigl(2(1-\gamma)+4\pi r_a^2\bigr)L+\kappa_a\right]
 +O_{a,\hbar}(tL^4),$$ where $r_a=(1+\sqrt{1+a})^{-1}$ and $\kappa_a=\pi^2/6-2\gamma+\gamma^2+4\pi r_a^2(1-\gamma)$. The strict ground-state ordering and the weighted full-spectrum heat invariant are independent certificates of genuine nonisospectrality. More generally, the warp becomes a variable determinant-one kinetic metric under radializing coordinates, and at fixed $B\neq0$ the centered $n=1,2$ magnetic members lose the standard reflected-conjugation repair.

The numerical evidence is narrower but independently checked. Sampled Hamiltonian trajectories for the prior-frozen $a=1.02$ member retain order-one FTLE and roundoff-scale SALI under both symplectic and adaptive integration. Its finite scalar spectrum is orthogonal-class-like, and a fixed magnetic field produces a stable response toward the unitary class under both second- and fourth-order gauge-covariant stencils. These are finite-sample and finite-window results, not chaos or RMT universality theorems.

The arithmetic boundary remains decisive. A canonical relative counting shift, the explicit scalar relative heat asymptotic, a tempered relative wave trace, and a higher-resolvent spectral-shift framework now coexist in one model. The general trace-class admissibility still follows from individual summability and implies no pairwise closeness; the special heat theorem proves spectral activity but is a $t\downarrow0$ invariant, not a fixed-time orbit trace. No endogenous $r\log p$ periods or von-Mangoldt amplitudes have been derived. The next high-value task is therefore structural: an energy- localized relative wave-trace theorem with explicit period/action control, not merely a larger zero comparison or a wider random-matrix window. Until the prime-power gate is crossed, the construction remains a Hilbert--Pólya- motivated testbed with an exact mean clock and a rigorously nonisospectral centered one-step scalar subfamily, rather than a model of the zeta zeros or a claim toward the Riemann hypothesis.

# Theory details for the clock-preserving family {#app:theory}

This appendix proves the geometric, magnetic-bracketing, symmetry, and relative-spectrum statements used in [\[sec:quantum-weyl,sec:active\]](#sec:quantum-weyl,sec:active){reference-type="ref" reference="sec:quantum-weyl,sec:active"}. All constants below may depend on fixed $a,n,B$, but never on $E$.

## Polynomial geometry of a fixed Hénon iterate {#app:poly-geometry}

Recall $$\widetilde H_a(x,y)=(-c_ax-ax^2-y,x),
 \qquad c_a=2(\sqrt{1+a}-1).
 \label{eq:app-centered-map}$$ Its Jacobian and inverse are $$D\widetilde H_a(x,y)=
 \begin{pmatrix}-c_a-2ax&-1\\1&0\end{pmatrix},
 \qquad
 \widetilde H_a^{-1}(u,v)=(v,-c_av-av^2-u).
 \label{eq:app-centered-inverse}$$ Hence every fixed iterate $\Psi=\widetilde H_a^n$ is a proper polynomial automorphism with $\det D\Psi=1$. For $a\neq0$, both $\Psi$ and $\Psi^{-1}$ have degree $D=2^n$.

[\[lem:allowed-domain-geometry\]]{#lem:allowed-domain-geometry label="lem:allowed-domain-geometry"} Let $a\neq0$ and $n$ be fixed. For $R\geq1$, set $\Omega_R=\Psi^{-1}(B_R)$ and $\Phi(q)=\pi|\Psi(q)|^2$. Then $$\begin{aligned}
 |\Omega_R|&=\pi R^2, \\
 \operatorname{length}(\partial\Omega_R)&=O_{a,n}(R^D),
 \label{eq:app-boundary-length}\\
 \sup_{\Psi^{-1}(B_{R+1})}|\nabla\Phi|&=O_{a,n}(R^D).
 \label{eq:app-gradient-bound}\end{aligned}$$

The area identity follows from $\det D\Psi=1$. Parametrize the boundary by $$q(\theta)=\Psi^{-1}(R\cos\theta,R\sin\theta).$$ The derivative of the degree-$D$ polynomial $\Psi^{-1}$ is bounded by $C_{a,n}(1+R)^{D-1}$ on $B_R$. Since the circle velocity has norm $R$, integration over $0\leq\theta\leq2\pi$ proves [\[eq:app-boundary-length\]](#eq:app-boundary-length){reference-type="ref" reference="eq:app-boundary-length"}.

For $q=\Psi^{-1}(u)$, $$\nabla\Phi(q)=2\pi D\Psi(q)^Tu.
 \label{eq:app-phi-chain}$$ Moreover, $D\Psi(q)=D\Psi^{-1}(u)^{-1}$. A $2\times2$ matrix of determinant one has inverse norm bounded by a fixed multiple of its norm, and $D\Psi^{-1}(u)=O_{a,n}((1+|u|)^{D-1})$. Multiplication by $|u|\leq R+1$ proves [\[eq:app-gradient-bound\]](#eq:app-gradient-bound){reference-type="ref" reference="eq:app-gradient-bound"}.

[\[lem:first-exit-control\]]{#lem:first-exit-control label="lem:first-exit-control"} Let $L=\log(E/2\pi)$, $R=\sqrt{L/\pi}$, and $\ell=E^{-1/4}$. If a lattice square $Q$ of side $\ell$ meets $\Omega_E=\Psi^{-1}(B_R)$, then, for all sufficiently large $E$, $$\Psi(Q)\subset B_{R+1}
 \quad\text{and}\quad
 \operatorname{osc}_Q V_{a,n}
 =O_{a,n}(E\ell L^{D/2}).
 \label{eq:app-first-exit-conclusion}$$

Choose $q_0\in Q\cap\Omega_E$, $q\in Q$, and let $q_t=q_0+t(q-q_0)$. Suppose that $u_t=\Psi(q_t)$ first reaches $\partial B_{R+1}$. Up to that time, the inverse-polynomial estimate used in the preceding proof, together with $\det D\Psi=1$, gives $$\|D\Psi(q_t)\|\leq C_{a,n}(1+R)^{D-1}.$$ Consequently, $$|u_t-u_0|
 \leq C_{a,n}\ell(1+R)^{D-1}=o(1).
 \label{eq:app-first-exit-small}$$ Reaching $\partial B_{R+1}$ from $B_R$ requires displacement at least one, contradicting [\[eq:app-first-exit-small\]](#eq:app-first-exit-small){reference-type="ref" reference="eq:app-first-exit-small"}. The conclusion uses that $D$, and therefore $n$, is fixed.

On $Q$, [\[lem:allowed-domain-geometry\]](#lem:allowed-domain-geometry){reference-type="ref" reference="lem:allowed-domain-geometry"} gives $|\nabla\Phi|=O_{a,n}(L^{D/2})$. In addition, $\ell L^{D/2}\to0$. Choose $q_0\in Q\cap\Omega_E$. Integrating the gradient bound along the segment from $q_0$ to any $q\in Q$ gives $$\Phi(q)\leq \Phi(q_0)+O_{a,n}(\ell L^{D/2})
 <L+o(1).$$ Thus $V(q)\leq E e^{o(1)}=O(E)$ throughout the square. The mean-value theorem now gives the oscillation estimate in [\[eq:app-first-exit-conclusion\]](#eq:app-first-exit-conclusion){reference-type="ref" reference="eq:app-first-exit-conclusion"}.

The preimage $\Omega_E$ is a smooth Jordan domain of area $L$ and perimeter $O_{a,n}(L^{D/2})$. The elementary square-cover estimate for a rectifiable Jordan domain therefore gives $$\#\{Q:Q\cap\Omega_E\neq\varnothing\}
 =O_{a,n}\!\left(
 \frac{L}{\ell^2}+\frac{L^{D/2}}{\ell}+1\right).
 \label{eq:app-square-cover}$$

## Friedrichs realization and compact resolvent {#app:compactness}

The form in [\[eq:magnetic-form\]](#eq:magnetic-form){reference-type="ref" reference="eq:magnetic-form"} is initially defined on $C_c^\infty(\mathbb{R}^2)$, where it is finite because $A_B$ and $V_{a,n}$ are smooth. It is closable: if $u_k\to0$ in $L^2$ while $$\bigl((-\mathrm{i}\nabla-A_B)u_k,V_{a,n}^{1/2}u_k\bigr)\to(F,G)$$ in $L^2(\mathbb{R}^2;\mathbb{C}^2)\oplus L^2(\mathbb{R}^2)$, distributional testing on compact sets gives $F=0$, while closedness of the multiplication operator $V_{a,n}^{1/2}$ gives $G=0$. Its nonnegative closure therefore defines the Friedrichs realization. To prove compactness of the form-domain embedding, let $(u_j)$ be bounded in the form norm. Properness of $\Psi$ makes $K_M=\{q:V_{a,n}(q)\leq M\}$ compact. Since $A_B$ is bounded on a neighborhood of $K_M$, $$\|\nabla u_j\|_{L^2(K_M)}
 \leq C_{M,B}\bigl(
 \|(-\mathrm{i}\nabla-A_B)u_j\|_{L^2(K_M)}+
 \|u_j\|_{L^2(K_M)}\bigr).$$ Rellich's theorem therefore yields an $L^2(K_M)$-convergent subsequence. Outside $K_M$, [\[eq:potential-tail\]](#eq:potential-tail){reference-type="ref" reference="eq:potential-tail"} makes the $L^2$ norm uniformly small as $M\to\infty$. A diagonal subsequence is Cauchy in $L^2(\mathbb{R}^2)$, proving compact embedding and hence compact resolvent.

## Local magnetic square counts {#app:magnetic-count}

Let $Q$ be a square of side $\ell$ and center $c_Q$. Multiplication by $$\exp\!\bigl(\mathrm{i}A_B(c_Q)\cdot q\bigr)$$ removes the constant vector potential on $Q$. The residual $$a_Q(q)=A_B(q)-A_B(c_Q)$$ satisfies $$\alpha_Q:=\|a_Q\|_{L^\infty(Q)}
 \leq \frac{|B|}{2\sqrt2}\ell.
 \label{eq:app-residual-gauge}$$

[\[lem:local-magnetic-count\]]{#lem:local-magnetic-count label="lem:local-magnetic-count"} For either the Dirichlet realization or the covariant Neumann realization of $\frac12(-\mathrm{i}\nabla-A_B)^2$ on $Q$, the strict counting function, defined to vanish for nonpositive arguments, obeys $$n_{B,D/N,Q}(A)
 =\frac{\ell^2A}{2\pi}+O_B(\ell\sqrt E+1),
 \qquad 0\leq A\leq E,
 \label{eq:app-uniform-local-count}$$ when $\ell=E^{-1/4}$.

After the preceding gauge, let $k_{B,Q}$ and $k_{0,Q}$ denote the magnetic and free kinetic forms on the common Dirichlet form domain $H_0^1(Q)$, or on the common covariant-Neumann form domain $H^1(Q)$. For $0<\varepsilon<1$, Cauchy's inequality gives $$\begin{aligned}
 (1-\varepsilon)k_{0,Q}[u]
 -\frac{\alpha_Q^2}{2\varepsilon}\|u\|^2
 &\leq k_{B,Q}[u],
 \label{eq:app-form-lower}\\
 k_{B,Q}[u]
 &\leq(1+\varepsilon)k_{0,Q}[u]
 +\frac{1+\varepsilon^{-1}}{2}\alpha_Q^2\|u\|^2.
 \label{eq:app-form-upper}\end{aligned}$$ The min--max principle compares the magnetic eigenvalues with scaled and shifted free-square eigenvalues. The strict free Dirichlet and Neumann counts satisfy the uniform lattice estimate $$n_{0,D/N,Q}(A)
 =\frac{\ell^2A}{2\pi}+O(\ell\sqrt A+1),
 \qquad A\geq0.
 \label{eq:app-free-square-count}$$ Choose $\varepsilon=\ell$. By [\[eq:app-residual-gauge\]](#eq:app-residual-gauge){reference-type="ref" reference="eq:app-residual-gauge"}, the induced energy shift is $O_B(\ell A+\ell)$. Its contribution to the area term in [\[eq:app-free-square-count\]](#eq:app-free-square-count){reference-type="ref" reference="eq:app-free-square-count"} is $O_B(\ell^3A+\ell^3)$, which is $O_B(\ell\sqrt E+1)$ for $A\leq E$ and $\ell=E^{-1/4}$. The boundary lattice error has the same bound. This proves [\[eq:app-uniform-local-count\]](#eq:app-uniform-local-count){reference-type="ref" reference="eq:app-uniform-local-count"}. Using strict counts and setting them to zero at $A\leq0$ prevents the Neumann zero mode from entering a forbidden square.

## Assembly of the Weyl estimate {#app:weyl-assembly}

We now complete the proof of [\[thm:magnetic-weyl\]](#thm:magnetic-weyl){reference-type="ref" reference="thm:magnetic-weyl"}. Dirichlet--Neumann form bracketing with potential extrema yields $$\sum_Q n_{B,D,Q}(E-V_Q^+)
 \leq N_{<}(E)
 \leq\sum_Q n_{B,N,Q}(E-V_Q^-).
 \label{eq:app-bracket}$$ Only squares meeting $\Omega_E$ enter the upper sum. Combining [\[eq:app-square-cover,eq:app-uniform-local-count\]](#eq:app-square-cover,eq:app-uniform-local-count){reference-type="ref" reference="eq:app-square-cover,eq:app-uniform-local-count"}, the sum of the local lattice errors is $$\begin{aligned}
 O_{a,n,B}\!\bigg[&
 \left(\frac{L}{\ell^2}+\frac{L^{D/2}}{\ell}+1\right)
 (\ell\sqrt E+1)\bigg]
 \notag\\
 &=O_{a,n,B}(E^{3/4}L^{1+D/2}).
 \label{eq:app-total-lattice-error}\end{aligned}$$ This envelope is deliberately safe; several displayed contributions are smaller.

The principal parts of the two sums in [\[eq:app-bracket\]](#eq:app-bracket){reference-type="ref" reference="eq:app-bracket"} are lower and upper Darboux sums for $$\frac1{2\pi}\int_{\mathbb{R}^2}(E-V_{a,n}(q))_+\,\mathrm{d}q.
 \label{eq:app-phase-integral}$$ By [\[lem:first-exit-control\]](#lem:first-exit-control){reference-type="ref" reference="lem:first-exit-control"}, their difference is bounded by the area of the relevant-square union times the maximal potential oscillation. The union has area $$O_{a,n}(L+\ell L^{D/2})=O_{a,n}(L),$$ because $D$ is fixed. Hence the Darboux-sum gap is $$O_{a,n}(E\ell L^{1+D/2})
 =O_{a,n}(E^{3/4}L^{1+D/2}).
 \label{eq:app-darboux-gap}$$ The integral in [\[eq:app-phase-integral\]](#eq:app-phase-integral){reference-type="ref" reference="eq:app-phase-integral"} equals the exact classical clock by [\[thm:classical-clock\]](#thm:classical-clock){reference-type="ref" reference="thm:classical-clock"}. Equations [\[eq:app-total-lattice-error\]](#eq:app-total-lattice-error){reference-type="eqref" reference="eq:app-total-lattice-error"} and [\[eq:app-darboux-gap\]](#eq:app-darboux-gap){reference-type="eqref" reference="eq:app-darboux-gap"} prove the theorem for $N_{<}(E)$. The exact classical integral contains the constant $+1$; it is absorbed into the displayed quantum remainder and is not asserted as a resolved quantum constant. Finally, $$N_{<}(E)\leq N_{\leq}(E)\leq N_{<}(E+1),$$ and the classical comparison function changes by $O(\log E)$ between $E$ and $E+1$. This cost is absorbed by the stated remainder.

For $a=0$, $\widetilde H_0(x,y)=(-y,x)$, so every iterate is an orthogonal linear map. Repeating the proof with $D=1$ gives [\[eq:radial-magnetic-weyl\]](#eq:radial-magnetic-weyl){reference-type="ref" reference="eq:radial-magnetic-weyl"}.

## Coordinate metric and centered reflection audit {#app:metric-symmetry}

For $g=U_\Psi f$, one has $f(q)=g(\Psi(q))$, and therefore $$\nabla_q f(q)=D\Psi(q)^T\nabla_u g(\Psi(q)).$$ Changing variables $u=\Psi(q)$ proves [\[eq:metric-form,eq:metric-tensor\]](#eq:metric-form,eq:metric-tensor){reference-type="ref" reference="eq:metric-form,eq:metric-tensor"}. The associated divergence-form operator is [\[eq:unitary-metric\]](#eq:unitary-metric){reference-type="ref" reference="eq:unitary-metric"}. If $G_\Psi=I$, then $D\Psi(q)$ is orthogonal at every point. A local Euclidean isometry of the connected, complete plane is the restriction of an affine Euclidean isometry, which proves the rigidity statement used in the main text.

### Proof of the no-reflection lemma {#app:reflection-proof}

Set $F_n(q)=|\widetilde H_a^n(q)|^2$. Since $\widetilde H_a^n$ is bijective and fixes the origin, $F_n$ has the unique zero $q=0$. A Euclidean isometry preserving $F_n$ must therefore fix the origin and is represented by an orthogonal matrix $S$.

For $n=1,2$, the highest homogeneous part of $F_n$ is a nonzero multiple of $x^{2^{n+1}}$. Preservation of that term forces the first row of $S$ to be $(s,0)$, $s=\pm1$. If $S$ reverses orientation, it must have the form $$S=\operatorname{diag}(s,-s).
 \label{eq:app-diagonal-reflection}$$ Let $$A=D\widetilde H_a(0)=
 \begin{pmatrix}-c_a&-1\\1&0\end{pmatrix}.$$ The quadratic Taylor form of $F_n$ at zero is $q^T(A^n)^TA^nq$. The off-diagonal entries of $A^TA$ and $(A^2)^TA^2$ are, respectively, $$c_a\quad\text{and}\quad c_a^3.$$ Conjugation of either quadratic form by the diagonal reflection in [\[eq:app-diagonal-reflection\]](#eq:app-diagonal-reflection){reference-type="ref" reference="eq:app-diagonal-reflection"} changes the sign of its off-diagonal entry. Since $a\neq0$ implies $c_a=2(\sqrt{1+a}-1)\neq0$, the Taylor form cannot be invariant. This contradiction proves the lemma.

For completeness, in symmetric gauge an orientation-reversing orthogonal map reverses the constant magnetic two-form. Thus, if such an $S$ preserved the potential, $U_S\mathcal C$ would intertwine the two sign changes and restore a standard geometric antiunitary. The lemma excludes exactly this repair for the stated $a,n$; it says nothing about a nonlocal antiunitary unrelated to a Euclidean isometry.

## Relative spectral objects and the first-resolvent boundary {#app:relative-container}

We prove [\[prop:relative-container\]](#prop:relative-container){reference-type="ref" reference="prop:relative-container"}. From [\[eq:quantum-weyl,eq:radial-magnetic-weyl\]](#eq:quantum-weyl,eq:radial-magnetic-weyl){reference-type="ref" reference="eq:quantum-weyl,eq:radial-magnetic-weyl"}, $$N_j(E)\asymp E\log E,
 \qquad
 \lambda_{j,k}\asymp\frac{k}{\log k}.
 \label{eq:app-eigenvalue-growth}$$ For $z\notin\mathbb{R}$, the singular values of the resolvent therefore satisfy $$s_k(R_j(z))\asymp\frac{\log k}{k}.
 \label{eq:app-resolvent-singular-values}$$ It follows that $$R_j(z)\in\mathcal{S}_p\quad\Longleftrightarrow\quad p>1.
 \label{eq:app-resolvent-threshold}$$ Since $\mathcal{S}_p$ is a linear ideal, $R_1(z)-R_0(z)\in\mathcal{S}_p$ for $p>1$. No conclusion at $p=1$ follows from this subtraction. For an integer $m\geq2$, however, $$R_j(z)^m\in\mathcal{S}_1,$$ so $R_1(z)^m-R_0(z)^m$ is trace class without invoking cancellation. For every nonreal $z$, the odd case $m=3$ meets the hypothesis of the resolvent-power invariance-principle construction in @Yafaev2005. The resulting abstract weighted spectral-shift function is determined up to an additive constant. The staircase below satisfies the compact-test trace identity and, by [\[eq:relative-staircase-bound\]](#eq:relative-staircase-bound){reference-type="ref" reference="eq:relative-staircase-bound"}, for example $$\int_\mathbb{R}\frac{|\xi(E)|}{(1+|E|)^4}\,\mathrm{d}E<\infty.$$ Thus it has the required $m=3$ weighted integrability. In this pure-point setting it may therefore be taken as the normalized representative, with the additive constant fixed by requiring it to vanish below both spectra.

Because each spectrum is discrete and bounded below, for $f\in C_c^\infty(\mathbb{R})$ both $f(H_j)$ have finite rank. Stieltjes integration and integration by parts give $$\begin{aligned}
 \operatorname{Tr}(f(H_1)-f(H_0))
 &=\int f(E)\,\mathrm{d}\bigl(N_1(E)-N_0(E)\bigr)\\
 &=\int f'(E)\bigl(N_0(E)-N_1(E)\bigr)\,\mathrm{d}E,\end{aligned}$$ which is [\[eq:relative-trace-compact\]](#eq:relative-trace-compact){reference-type="ref" reference="eq:relative-trace-compact"}. The Weyl remainders yield [\[eq:relative-staircase-bound\]](#eq:relative-staircase-bound){reference-type="ref" reference="eq:relative-staircase-bound"}.

Each heat semigroup is trace class for $t>0$, and $$\Theta_{\mathrm{rel}}(t)
 :=\operatorname{Tr}(e^{-tH_1}-e^{-tH_0})
 =-t\int_0^\infty e^{-tE}\xi(E)\,\mathrm{d}E.
 \label{eq:app-relative-heat}$$ In particular, the available bound on $\xi$ gives the safe estimate $$\Theta_{\mathrm{rel}}(t)
 =O_{a,n,B}\!\left(
 t^{-3/4}(\log(1/t))^{1+2^{n-1}}\right),
 \qquad t\downarrow0.
 \label{eq:app-relative-heat-bound}$$ The unitary propagators themselves are not trace class. Their spectral propagator traces are nevertheless tempered distributions: for $\varphi\in\mathcal S(\mathbb{R})$, define $$\langle W_j,\varphi\rangle
 =\sum_k\widehat\varphi(\lambda_{j,k}).
 \label{eq:app-wave-distribution}$$ The series converges absolutely by [\[eq:app-eigenvalue-growth\]](#eq:app-eigenvalue-growth){reference-type="ref" reference="eq:app-eigenvalue-growth"}, and $W_{\mathrm{rel}}=W_1-W_0\in\mathcal S'(\mathbb{R})$. Equivalently, it is the distributional boundary value as $\varepsilon\downarrow0$ of the ordinary trace $$\operatorname{Tr}\!\left(e^{-(\varepsilon+\mathrm{i}t)H_1}
             -e^{-(\varepsilon+\mathrm{i}t)H_0}\right).
 \label{eq:app-damped-wave}$$ We call this the relative wave trace in the manuscript; this convention means the spectral-propagator trace of $e^{-\mathrm{i}tH}$, not the alternative $e^{-\mathrm{i}t\sqrt H}$ convention used in parts of spectral geometry.

We finish by recording why none of these statements proves ordinary Krein comparability. At $B=0$, the principal resolvent symbols at a negative spectral parameter $-c$, $c>0$, are $$r_j(q,p)=\frac{1}{|p|^2/2+V_j(q)+c}.$$ The momentum integral of their absolute difference is $$\int_{\mathbb{R}^2}|r_1(q,p)-r_0(q,p)|\,\mathrm{d}p
 =2\pi\left|\log\frac{V_1(q)+c}{V_0(q)+c}\right|.
 \label{eq:app-symbol-diagnostic}$$ For a non-isometric Hénon polynomial warp, the spatial integral of the right-hand side diverges. Indeed, $$\log\frac{V_1(q)+c}{V_0(q)+c}
 =\pi\bigl(|\Psi(q)|^2-|q|^2\bigr)+O(1).$$ For a non-isometric Hénon warp the polynomial in parentheses is nonzero, and the absolute value of a nonzero polynomial is not integrable over $\mathbb{R}^2$. The same diagnostic is unchanged at fixed $B$, because $p\mapsto p-A_B(q)$ is a fiber translation. Equation [\[eq:app-symbol-diagnostic\]](#eq:app-symbol-diagnostic){reference-type="eqref" reference="eq:app-symbol-diagnostic"} is an obstruction diagnostic, not an operator-theoretic lower bound; it does *not* prove $R_1(z)-R_0(z)\notin\mathcal{S}_1$. Accordingly, first-resolvent trace class remains unproved, while the $m=3$ resolvent-power framework is rigorous. An eventual periodic-orbit interpretation would additionally require an energy-localized trace theorem and control of the continuous orbit families in the radial reference [@DuistermaatGuillemin1975; @CombescureRalstonRobert1999].

# Analytic spectral activity of one Hénon warp {#app:analytic-activity}

This appendix proves the two one-step, nonmagnetic activity theorems in [\[sec:strict-ground-state,sec:relative-heat-activity\]](#sec:strict-ground-state,sec:relative-heat-activity){reference-type="ref" reference="sec:strict-ground-state,sec:relative-heat-activity"}. Throughout, $$\Psi_a(x,y)=(-2ar_ax-ax^2-y,x),
 \qquad
 r_a=\frac1{1+\sqrt{1+a}},
 \label{eq:app-activity-warp}$$ $$V_a(q)=2\pi e^{\pi|\Psi_a(q)|^2},
 \qquad
 \mathsf H_{a,\hbar}=-\frac{\hbar^2}{2}\Delta+V_a.
 \label{eq:app-activity-operator}$$ The Friedrichs realization and compact resolvent were established in [10.2](#app:compactness){reference-type="ref" reference="app:compactness"}. The constants below may depend on fixed $a>-1$ and $\hbar>0$, but not on $t$.

## Strict ground-state ordering {#app:strict-ground-state}

Let $f^*$ denote the symmetric decreasing rearrangement of $|f|$. The area identity $\det D\Psi_a=1$ implies, for every $s\ge2\pi$, $$A_s:=\{V_a\le s\},
 \qquad
 A_s^*:=\{V_0\le s\},
 \qquad
 |A_s|=|A_s^*|.
 \label{eq:app-equimeasurable-sets}$$ Thus $V_0$ is the symmetric increasing rearrangement of $V_a$.

[\[lem:app-rayleigh-rearrangement\]]{#lem:app-rayleigh-rearrangement label="lem:app-rayleigh-rearrangement"} For every $f$ in the form domain of $\mathsf H_{a,\hbar}$, $$Q_{0,\hbar}[f^*]\le Q_{a,\hbar}[f],
 \qquad \|f^*\|_2=\|f\|_2,
 \label{eq:app-rayleigh-rearrangement}$$ where $$Q_{a,\hbar}[f]
 =\frac{\hbar^2}{2}\int|\nabla f|^2\,\mathrm{d}q
 +\int V_a|f|^2\,\mathrm{d}q.$$

The diamagnetic inequality for the ordinary gradient followed by Pólya--Szegő gives $$\int|\nabla f^*|^2
 \le\int|\nabla|f||^2
 \le\int|\nabla f|^2.
 \label{eq:app-polya-szego}$$ For the unbounded increasing potential it is useful to keep the layer-cake direction explicit. The set form of Hardy--Littlewood and [\[eq:app-equimeasurable-sets\]](#eq:app-equimeasurable-sets){reference-type="ref" reference="eq:app-equimeasurable-sets"} give $$\int_{A_s}|f|^2\,\mathrm{d}q
 \le\int_{A_s^*}(f^*)^2\,\mathrm{d}q.$$ Subtracting from the common total $L^2$ norm reverses this inequality on the complements. Since $$V_a=2\pi+\int_{2\pi}^{\infty}
 \mathbf1_{\{V_a>s\}}\,\mathrm{d}s,$$ Tonelli's theorem yields $$\int V_a|f|^2\,\mathrm{d}q
 \ge\int V_0(f^*)^2\,\mathrm{d}q.
 \label{eq:app-increasing-potential-rearrangement}$$ The right-hand side of [\[eq:app-increasing-potential-rearrangement\]](#eq:app-increasing-potential-rearrangement){reference-type="ref" reference="eq:app-increasing-potential-rearrangement"} is finite whenever $f$ lies in the form domain of $\mathsf H_{a,\hbar}$; together with [\[eq:app-polya-szego\]](#eq:app-polya-szego){reference-type="ref" reference="eq:app-polya-szego"}, this also proves that $f^*$ lies in the form domain of $\mathsf H_{0,\hbar}$. The assertion follows, with monotone truncation justifying the layer-cake argument for the unbounded potential [@LiebLoss2001].

Compact resolvent gives a normalized ground state $\phi_a$. The scalar heat semigroup is positivity improving on the connected space $\mathbb{R}^2$; hence the lowest eigenvalue is simple and $\phi_a$ may be chosen strictly positive [@ReedSimon1978IV]. Smooth elliptic regularity applies, and the real-analytic potential $V_a$ makes $\phi_a$ real analytic by analytic elliptic regularity [@MorreyNirenberg1957]. If equality is assumed below, $\phi_a^*$ is the ground state of the analytic radial problem and is analytic as well.

The preceding lemma and the Rayleigh principle first give $$\lambda_1(\mathsf H_{0,\hbar})
 \le\lambda_1(\mathsf H_{a,\hbar}).$$ If equality held, then $$\lambda_1(\mathsf H_{0,\hbar})
 \le Q_{0,\hbar}[\phi_a^*]
 \le Q_{a,\hbar}[\phi_a]
 =\lambda_1(\mathsf H_{0,\hbar}).
 \label{eq:app-ground-equality-chain}$$ Consequently $\phi_a^*$ attains the Rayleigh infimum for $\mathsf H_{0,\hbar}$ and is its radial ground state. Because $\phi_a>0$, the difference between the right- and left-hand sides of [\[eq:app-rayleigh-rearrangement\]](#eq:app-rayleigh-rearrangement){reference-type="ref" reference="eq:app-rayleigh-rearrangement"} is the sum of the two nonnegative deficits $$\frac{\hbar^2}{2}\left(
 \int|\nabla\phi_a|^2-\int|\nabla\phi_a^*|^2\right)
 \label{eq:app-kinetic-deficit}$$ and $$\int V_a\phi_a^2-\int V_0(\phi_a^*)^2.
 \label{eq:app-potential-deficit}$$ Their sum is zero by [\[eq:app-ground-equality-chain\]](#eq:app-ground-equality-chain){reference-type="ref" reference="eq:app-ground-equality-chain"}; hence both vanish, and in particular equality holds in Pólya--Szegő.

The positive superlevel sets of $\phi_a^*$ have finite measure because $\phi_a^*\in L^2$. Moreover, the Brothers--Ziemer exceptional set $$\left\{q:0<\phi_a^*(q)<\operatorname*{ess\,sup}\phi_a^*,\
 \nabla\phi_a^*(q)=0\right\}
 \label{eq:app-bz-exceptional-set}$$ has measure zero. Indeed, it is contained in the critical set of the nonconstant real-analytic function $\phi_a^*$; if that critical set had positive measure, each analytic first derivative would vanish on a positive-measure set and hence identically, forcing $\phi_a^*$ to be constant. The Brothers--Ziemer equality classification therefore gives a point $q_0\in\mathbb{R}^2$ such that $$\phi_a(q)=\phi_a^*(q-q_0).
 \label{eq:app-ground-translate}$$

The function in [\[eq:app-ground-translate\]](#eq:app-ground-translate){reference-type="ref" reference="eq:app-ground-translate"} solves both the warped ground-state equation and the translate of the radial equation. Subtracting them and using $\phi_a>0$ gives $$V_a(q)=V_0(q-q_0)\quad\text{for every }q.
 \label{eq:app-potential-radial-contradiction}$$ This is impossible for $a\ne0$. Indeed, $$\frac1\pi\log\frac{V_a(x,y)}{2\pi}
 =x^2+(2ar_ax+ax^2+y)^2
 \label{eq:app-quartic-nonradiality}$$ has degree-four homogeneous part $a^2x^4$. Translation does not change the highest homogeneous part, whereas the degree-four part of a polynomial radial about any point must be $C(x^2+y^2)^2$. Its missing $y^4$ coefficient would force $C=0$, contradicting the nonzero $x^4$ coefficient. Equality in [\[eq:app-ground-equality-chain\]](#eq:app-ground-equality-chain){reference-type="ref" reference="eq:app-ground-equality-chain"} is excluded, which proves the strict inequality [@BrothersZiemer1988].

## Brownian-bridge proof of the uniform relative heat remainder {#app:relative-heat-proof}

Set $$Q_a=\Psi_a^{-1},\qquad
 Q_a(u,v)=(v,-2ar_av-av^2-u),
 \qquad W(z)=2\pi e^{\pi|z|^2},
 \label{eq:app-heat-QW}$$ and let $\mathbf b=(\mathbf b_s)_{0\le s\le1}$ be a standard two-dimensional Brownian bridge with $$\mathbb E[b_i(s)b_j(r)]
 =\delta_{ij}\bigl(\min(s,r)-sr\bigr).
 \label{eq:app-bridge-covariance}$$ Write $\varepsilon=\hbar\sqrt t$, $M=\sup_s|\mathbf b_s|$, and $E_1(\lambda)=\int_\lambda^\infty e^{-w}\,\mathrm{d}w/w$.

[\[lem:app-common-heat-coordinate\]]{#lem:app-common-heat-coordinate label="lem:app-common-heat-coordinate"} For every $t>0$, $$\Theta_{a,\hbar}(t)
 =\frac1{2\pi\hbar^2t}\int_{\mathbb{R}^2}
 F_a(\varepsilon,z)\,\mathrm{d}z,
 \label{eq:app-common-heat-coordinate}$$ where $$F_a(\theta,z)=\mathbb E\exp\!\left[-t\int_0^1
 V_a(Q_a(z)+\theta\mathbf b_s)\,\mathrm{d}s\right].
 \label{eq:app-Fa-definition}$$ Moreover, $$F_a(0,z)=e^{-tW(z)},
 \label{eq:app-pointwise-classical-cancellation}$$ independently of $a$.

The diagonal Brownian-bridge Feynman--Kac formula gives $$K_{a,\hbar}(t;q,q)=\frac1{2\pi\hbar^2t}
 \mathbb E\exp\!\left[-t\int_0^1
 V_a(q+\hbar\sqrt t\,\mathbf b_s)\,\mathrm{d}s\right]$$ [@Simon2005FunctionalIntegration; @BoldtGueneysu2023]. The heat semigroup is trace class; for example, Golden--Thompson and area preservation give $$\Theta_{a,\hbar}(t)
 \le\frac1{2\pi\hbar^2t}\int e^{-tV_a(q)}\,\mathrm{d}q
 =\frac{E_1(2\pi t)}{2\pi\hbar^2t}<\infty.
 \label{eq:app-GT-heat-bound}$$ Integrate the diagonal and change variables $q=Q_a(z)$. Since $V_a(Q_a(z))=W(z)$, both assertions follow.

The following explicit bounds provide the required global domination. Set $$\Phi_a=\log\frac{V_a}{2\pi}=\pi|\Psi_a|^2,
 \qquad \sigma=\pi|z|^2.
 \label{eq:app-heat-Phi-sigma}$$ For $z=(u,v)$ and $w=(\xi,\eta)$, direct substitution gives $$\Psi_a(Q_a(z)+w)
 =\bigl(u-2a(r_a+v)\xi-a\xi^2-\eta,\ v+\xi\bigr).
 \label{eq:app-exact-henon-displacement}$$ Consequently, $$|\Phi_a(Q_a(z)+w)-\sigma|
 \le C_a(1+\sigma)(|w|+|w|^2).
 \label{eq:app-Phi-displacement-bound}$$ Because $\Phi_a$ is quartic, Faà di Bruno gives, for $1\le k\le4$, $$\|D^kV_a(Q_a(z)+w)\|
 \le C_{a,\delta,k}V_a(Q_a(z)+w)(1+\sigma)^k
 \label{eq:app-normalized-heat-derivatives}$$ whenever $|w|\le\delta/L$ and $L$ is sufficiently large. The same calculation gives, for nonzero multi-indices $\beta_j$ and $N=\sum_j|\beta_j|$, $$\int e^{-tV_a(q)}\prod_{j=1}^m
 |\partial^{\beta_j}V_a(q)|\,\mathrm{d}q
 \le C_{a,\boldsymbol\beta}t^{-m}(1+L)^N.
 \label{eq:app-weighted-heat-derivatives}$$ Indeed, radial integration in $z$, followed by $w=tW(z)=2\pi t e^\sigma$, reduces the bound to $$\int_{2\pi t}^{\infty}e^{-w}w^{m-1}
 \left(1+\log\frac{w}{2\pi t}\right)^N\,\mathrm{d}w
 =O_{m,N}((1+L)^N).
 \label{eq:app-gamma-derivative-bound}$$

Freeze a sufficiently small $\delta>0$ and define the symmetric good event $$G_t=\left\{M\le\frac{\delta}{\hbar\sqrt t\,L}\right\}.
 \label{eq:app-good-bridge-event}$$ The Gaussian bridge maximum satisfies $$\mathbb P(G_t^c)\le C_{\hbar}
 \exp\!\left(-\frac{c_{\hbar}}{tL^2}\right).
 \label{eq:app-bridge-tail}$$ For every continuous deterministic path $w_s$, convexity of $x\mapsto e^{-tx}$, followed by translation invariance, yields the pathwise integral bound $$\int_{\mathbb{R}^2}e^{-t\int_0^1V_a(q+w_s)\,\mathrm{d}s}\,\mathrm{d}q
 \le\int_{\mathbb{R}^2}e^{-tV_a(q)}\,\mathrm{d}q
 =E_1(2\pi t).
 \label{eq:app-pathwise-jensen}$$ This order of integration prevents a small bridge probability from being multiplied by the infinite volume of $\mathbb{R}^2$.

[\[lem:app-fourth-amplitude\]]{#lem:app-fourth-amplitude label="lem:app-fourth-amplitude"} Let $$\mathcal A_a(\theta,z,\mathbf b)
 =t\int_0^1V_a(Q_a(z)+\theta\mathbf b_s)\,\mathrm{d}s,
 \qquad f_a=e^{-\mathcal A_a}.$$ Then $$\int_{\mathbb{R}^2}\sup_{|\theta|\le\varepsilon}
 \mathbb E\!\left[
 \mathbf1_{G_t}|\partial_\theta^4f_a(\theta,z,\mathbf b)|
 \right]\,\mathrm{d}z
 \le C_aL^4.
 \label{eq:app-fourth-amplitude-bound}$$

For $1\le k\le4$, $$\mathcal A_a^{(k)}(\theta)
 =t\int_0^1D^kV_a(Q_a(z)+\theta\mathbf b_s)
 [\mathbf b_s,\ldots,\mathbf b_s]\,\mathrm{d}s,$$ and direct differentiation gives $$\partial_\theta^4e^{-\mathcal A}
 =e^{-\mathcal A}\left[(\mathcal A')^4
 -6(\mathcal A')^2\mathcal A''+3(\mathcal A'')^2
 +4\mathcal A'\mathcal A'''-\mathcal A^{(4)}\right].
 \label{eq:app-fourth-exponential-derivative}$$ On $G_t$, $|\theta\mathbf b_s|\le\delta/L$. Split at $\sigma_*=L+8\log L$. On $0\le\sigma\le\sigma_*$, set $Y=e^{\sigma-L}$. Equations [\[eq:app-Phi-displacement-bound\]](#eq:app-Phi-displacement-bound){reference-type="eqref" reference="eq:app-Phi-displacement-bound"}-- [\[eq:app-fourth-exponential-derivative\]](#eq:app-fourth-exponential-derivative){reference-type="eqref" reference="eq:app-fourth-exponential-derivative"} imply $$|\partial_\theta^4f_a|
 \le C_aM^4(1+\sigma)^4
 \sum_{m=1}^4Y^me^{-cY}.
 \label{eq:app-fourth-main-bound}$$ Since $\mathbb E[M^4]<\infty$ and $\,\mathrm{d}\sigma=\,\mathrm{d}Y/Y$, its spatial integral is $O_a(L^4)$; no extra factor of $L$ appears because every summand contains at least one $Y$.

For $\sigma>\sigma_*$, put $$\alpha_L=C_a\left(\frac\delta L+\frac{\delta^2}{L^2}\right).$$ The lower path potential is bounded by $$tV_a(Q_a(z)+\theta\mathbf b_s)
 \ge \exp\bigl[-L+(1-\alpha_L)\sigma-\alpha_L\bigr].$$ After the corresponding change of variables, the lower endpoint is at least $L^7$, the upper potential is a power $p_L=(1+\alpha_L)/(1-\alpha_L)=1+O(L^{-1})$ of the lower one, and the Jacobian factor $(1-\alpha_L)^{-1}$ is bounded. The tail is therefore a finite sum of integrals $$C_{a,\delta}\int_{L^7}^{\infty}
 (1+L+\log y)^4y^{mp_L-1}e^{-cy}\,\mathrm{d}y,
 \qquad1\le m\le4,$$ which is $O_{a,N}(L^{-N})$ for every fixed $N$. Combining the two regions proves the lemma.

[\[lem:app-uniform-amplitude-expansion\]]{#lem:app-uniform-amplitude-expansion label="lem:app-uniform-amplitude-expansion"} For fixed $a$ and $\hbar$, $$\int_{\mathbb{R}^2}\left|F_a(\varepsilon,z)-F_a(0,z)
 -\frac{\varepsilon^2}{2}\partial_\theta^2F_a(0,z)\right|\,\mathrm{d}z
 \le C_{a,\hbar}t^2L^4.
 \label{eq:app-uniform-amplitude-expansion}$$

On $G_t$, invariance under $\mathbf b\mapsto-\mathbf b$ makes the restricted expectation even in $\theta$. Taylor's theorem, [\[lem:app-fourth-amplitude\]](#lem:app-fourth-amplitude){reference-type="ref" reference="lem:app-fourth-amplitude"}, and $\varepsilon=\hbar\sqrt t$ bound the integrated remainder by $C_{a,\hbar}t^2L^4$.

The bad event is exponentially smaller. Equations [\[eq:app-bridge-tail\]](#eq:app-bridge-tail){reference-type="eqref" reference="eq:app-bridge-tail"} and [\[eq:app-pathwise-jensen\]](#eq:app-pathwise-jensen){reference-type="eqref" reference="eq:app-pathwise-jensen"} bound its zeroth term by $$C_{\hbar}E_1(2\pi t)e^{-c_{\hbar}/(tL^2)}.
 \label{eq:app-bad-event-zero}$$ It remains to justify two derivatives through this expectation. For fixed $z,t,\theta_0$, the exact polynomial displacement gives, uniformly for $|\theta|\le\theta_0$, $$\begin{aligned}
 \frac{\|DV_a(Q_a(z)+\theta\mathbf b_s)\|}
 {V_a(Q_a(z)+\theta\mathbf b_s)}
 &\le C_{a,z,\theta_0}(1+M)^4,\\
 \frac{\|D^2V_a(Q_a(z)+\theta\mathbf b_s)\|}
 {V_a(Q_a(z)+\theta\mathbf b_s)}
 &\le C_{a,z,\theta_0}(1+M)^8.\end{aligned}$$ Thus, with $\mathcal A=\mathcal A_a(\theta,z,\mathbf b)$, $$|\mathcal A'|\le C(1+M)^5\mathcal A,
 \qquad
 |\mathcal A''|\le C(1+M)^{10}\mathcal A.$$ Since $xe^{-x}$ and $x^2e^{-x}$ are bounded, $$\sup_{|\theta|\le\theta_0}|f_a''(\theta,z,\mathbf b)|
 \le C_{a,z,\theta_0}(1+M)^{10}.
 \label{eq:app-bad-event-dominator}$$ The bridge maximum has Gaussian tails, so this is integrable and dominated differentiation is valid. At $\theta=0$, $$\begin{aligned}
 f_a''(0)=e^{-tV_a}\Bigg[&t^2
 \left(\nabla V_a\cdot\int_0^1\mathbf b_s\,\mathrm{d}s\right)^2
 \notag\\[-1mm]
 &-t\int_0^1D^2V_a[\mathbf b_s,\mathbf b_s]\,\mathrm{d}s\Bigg].\end{aligned}$$ The weighted bound [\[eq:app-weighted-heat-derivatives\]](#eq:app-weighted-heat-derivatives){reference-type="eqref" reference="eq:app-weighted-heat-derivatives"} and a Gaussian tail moment give an integrated bad-event contribution $$O_{a,\hbar}\!\left(L^2e^{-c_{\hbar}/(2tL^2)}\right).$$ After multiplication by $\varepsilon^2$, this and [\[eq:app-bad-event-zero\]](#eq:app-bad-event-zero){reference-type="ref" reference="eq:app-bad-event-zero"} are smaller than $t^2L^4$. The lemma follows.

[\[lem:app-second-amplitude\]]{#lem:app-second-amplitude label="lem:app-second-amplitude"} For every fixed $a$, $$\frac1{2\pi\hbar^2t}\frac{\varepsilon^2}{2}
 \int_{\mathbb{R}^2}\partial_\theta^2F_a(0,z)\,\mathrm{d}z
 =-\frac{t^2}{48\pi}I_a(t).
 \label{eq:app-second-amplitude-coefficient}$$

The bridge covariances are $$\mathbb E\!\left[\left(\int_0^1b_i(s)\,\mathrm{d}s\right)
 \left(\int_0^1b_j(s)\,\mathrm{d}s\right)\right]=\frac{\delta_{ij}}{12},
 \qquad
 \int_0^1\mathbb E[b_i(s)b_j(s)]\,\mathrm{d}s=\frac{\delta_{ij}}6.$$ Hence $$\partial_\theta^2F_a(0,z)
 =e^{-tV_a(Q_a(z))}\left[
 \frac{t^2}{12}|\nabla V_a(Q_a(z))|^2
 -\frac t6\Delta V_a(Q_a(z))\right].$$ Changing back to $q$ and inserting the prefactor gives $$\frac{t^2}{48\pi}I_a(t)
 -\frac{t}{24\pi}\int e^{-tV_a}\Delta V_a\,\mathrm{d}q.$$ The weighted derivative bounds justify cutoff integration by parts, yielding $$\int e^{-tV_a}\Delta V_a\,\mathrm{d}q
 =t\int e^{-tV_a}|\nabla V_a|^2\,\mathrm{d}q=tI_a(t).$$ Combining the two terms proves the claim.

Apply [\[lem:app-uniform-amplitude-expansion\]](#lem:app-uniform-amplitude-expansion){reference-type="ref" reference="lem:app-uniform-amplitude-expansion"} to $a$ and $0$, insert both expansions into [\[eq:app-common-heat-coordinate\]](#eq:app-common-heat-coordinate){reference-type="ref" reference="eq:app-common-heat-coordinate"}, and subtract. The zeroth terms cancel by [\[eq:app-pointwise-classical-cancellation\]](#eq:app-pointwise-classical-cancellation){reference-type="ref" reference="eq:app-pointwise-classical-cancellation"}; [\[lem:app-second-amplitude\]](#lem:app-second-amplitude){reference-type="ref" reference="lem:app-second-amplitude"} gives $$\Theta_{a,\hbar}(t)-\Theta_{0,\hbar}(t)
 =-\frac{t^2}{48\pi}\bigl(I_a(t)-I_0(t)\bigr)
 +O_{a,\hbar}(tL^4),
 \label{eq:app-relative-heat-remainder-final}$$ because the common heat prefactor turns the integrated $O_{a,\hbar}(t^2L^4)$ amplitude remainder into $O_{a,\hbar}(tL^4)$.

It remains to compute the carrier. In the coordinate $z=(u,v)=\Psi_a(q)$, $$I_a-I_0
 =\int e^{-tW(z)}(2\pi W(z))^2
 \left(|D\Psi_a(q)^Tz|^2-|z|^2\right)\,\mathrm{d}z.$$ At $q=Q_a(z)$, direct multiplication gives $$|D\Psi_a(q)^Tz|^2-|z|^2
 =-4a(r_a+v)uv+4a^2(r_a+v)^2u^2.$$ All terms odd in $u$ or $v$ vanish against the radial weight, leaving $$I_a-I_0=4a^2\int e^{-tW}(2\pi W)^2
 (r_a^2u^2+u^2v^2)\,\mathrm{d}u\,\mathrm{d}v>0
 \label{eq:app-positive-carrier-integral}$$ for $a\ne0$. Polar coordinates, followed by $s=\pi|z|^2$ and $w=2\pi te^s$, use $$\int_0^{2\pi}\cos^2\theta\,\mathrm{d}\theta=\pi,
 \qquad
 \int_0^{2\pi}\cos^2\theta\sin^2\theta\,\mathrm{d}\theta=\frac\pi4$$ to give the exact identity $$I_a(t)-I_0(t)
 =\frac{2a^2}{t^2}
 \left[A_2(2\pi t)+4\pi r_a^2A_1(2\pi t)\right].
 \label{eq:app-exact-carrier-final}$$

Finally, the Gamma moments $$\begin{aligned}
 \int_0^\infty we^{-w}\log w\,\mathrm{d}w&=1-\gamma,\\
 \int_0^\infty we^{-w}(\log w)^2\,\mathrm{d}w
 &=\frac{\pi^2}{6}-2\gamma+\gamma^2\end{aligned}$$ give the polynomial in [\[eq:relative-heat-full-asymptotic\]](#eq:relative-heat-full-asymptotic){reference-type="ref" reference="eq:relative-heat-full-asymptotic"}. The lower-tail correction can also be retained explicitly. With $\lambda=2\pi t$, $$\begin{aligned}
 A_1(\lambda)&=L+1-\gamma+\frac{\lambda^2}{4}+O(\lambda^3),\\
 A_2(\lambda)&=L^2+2(1-\gamma)L
 +\frac{\pi^2}{6}-2\gamma+\gamma^2
 -\frac{\lambda^2}{4}+O(\lambda^3).\end{aligned}$$ Thus, if $$\mathcal B_a(t)=A_2(2\pi t)+4\pi r_a^2A_1(2\pi t),
 \qquad
 P_a(L)=L^2+\beta_aL+\kappa_a,$$ then $$\frac{\mathcal B_a(t)-P_a(L)}{t^2}
 \longrightarrow\pi^2(4\pi r_a^2-1).
 \label{eq:app-carrier-scaled-limit}$$ This is the independently derived dashed limit in [\[fig:relative-heat-carrier\]](#fig:relative-heat-carrier){reference-type="ref" reference="fig:relative-heat-carrier"}. Equations [\[eq:app-relative-heat-remainder-final\]](#eq:app-relative-heat-remainder-final){reference-type="eqref" reference="eq:app-relative-heat-remainder-final"} and [\[eq:app-exact-carrier-final\]](#eq:app-exact-carrier-final){reference-type="eqref" reference="eq:app-exact-carrier-final"} complete the proof of [\[thm:relative-heat-activity\]](#thm:relative-heat-activity){reference-type="ref" reference="thm:relative-heat-activity"}.

# Numerical protocols and reproducibility {#app:numerics}

This appendix records the numerical definitions and the order in which the tests were frozen. Its purpose is to make later refinements distinguishable from the evidence frozen at each stage. Each run's archived metadata or summary records `zero_data_loaded=false` and `prime_data_loaded=false`: these fields are in the R000--R001 metadata and in the R100--R107A summaries. None of the calculations in [\[sec:classical,sec:quantum-spectra\]](#sec:classical,sec:quantum-spectra){reference-type="ref" reference="sec:classical,sec:quantum-spectra"} used zeta ordinates, prime tables, or a fitted spectral target.

## Classical initial states and tangent dynamics

Let $L=\log(E/2\pi)$, $R=\sqrt{L/\pi}$, and let $(s_0,s_1,s_2)$ be the fixed unscrambled Sobol point associated with an integer seed. The R000--R001 initial state was $$\begin{aligned}
 \rho&=0.88R\sqrt{s_0},
 &\theta&=2\pi s_1,
 &u&=\rho(\cos\theta,\sin\theta),\\
 q&=\Psi_{a,n}^{-1}(u),
 &\varphi&=2\pi s_2,
 &p&=\sqrt{2(E-V_{a,n}(q))}(\cos\varphi,\sin\varphi).
 \label{eq:classical-seed-map}\end{aligned}$$ The configuration transform has unit determinant, so this samples uniform area within the truncated $u$-disk. The radial truncation was fixed before the production run; it avoids launching directly against the exponential wall and is not a posteriori rejection.

For $B=0$, velocity Verlet advances both the orbit and two copies of the linearized system. If $D^2V(q)$ is the analytic Hessian, the tangent half-kick, drift, and second half-kick use the same Hessians as the orbit. Tangent norms are evaluated after scaling both configuration coordinates by $q_{\mathrm{scale}}$ and both momentum coordinates by $p_{\mathrm{scale}}=\sqrt{2E}$. The first tangent vector starts along a scaled configuration direction and the second along a scaled momentum direction; both are renormalized eight times per natural-time unit. Energy drift is evaluated at the same blocks. The implementation also records the initial state, step size, angular-momentum range, Poincaré crossings, and a coarse section occupancy, although the final decision uses only completion, energy drift, FTLE, and SALI.

::: {#tab:r000-full}
     $a$   $n$    $E$   median $\lambda_{80}$            median SALI   flags
  ------ ----- ------ ----------------------- ---------------------- -------
       0     1    100                  0.0558                  0.842     0/8
       0     1   1000                  0.0592                  0.951     0/8
    1.02     1    100                  0.5088   $2.46\times10^{-15}$     8/8
    1.02     1   1000                  0.7116   $1.17\times10^{-15}$     8/8
    1.02     2    100                  0.7326   $1.09\times10^{-15}$     8/8
    1.02     2   1000                  1.0842   $5.12\times10^{-15}$     8/8
       6     1    100                  0.7914   $4.40\times10^{-15}$     8/8
       6     1   1000                  0.7304   $1.88\times10^{-14}$     8/8

  : R000 primary groups. Every entry is a median over eight frozen states; "flags" uses $\lambda_{80}>0.05$ and $\mathrm{SALI}_{80}<10^{-4}$.
:::

R000 contained 64 primary and 16 refinement records. An independent checker that did not import the production package reconstructed every group summary, verified all 80 initial energy identities to maximum relative error $2.84\times10^{-16}$, found 15 stable and one unstable resolution pair, and confirmed the absence of prime and zero inputs. The unstable pair was the retained $a=6,n=1,E=1000$, seed-1 record described in the main text.

R106 used the same frozen initial $(q,v)$ values but independently reimplemented the potential gradient and Hessian. It integrated [\[eq:magnetic-velocity-flow\]](#eq:magnetic-velocity-flow){reference-type="ref" reference="eq:magnetic-velocity-flow"} and its full variational equation in segments of $0.5t_{\mathrm{nat}}$ with DOP853. The reported drift maximum is over segment endpoints, not every internal Runge--Kutta stage. Only $B=0,1$, four states per group, one energy, one tolerance pair, and 80 natural-time units were audited. A magnetic time-convergence series, QR computation of the full Lyapunov spectrum, and a broad microcanonical census remain open.

## Second-order covariant lattice operator

For an interior grid point $i$, the primary kinetic discretization is $$(K_h\psi)_i
 =\sum_{\alpha\in\{x,y\}}
 \left[
 \frac{1}{h_\alpha^2}\psi_i
 -\frac{1}{2h_\alpha^2}
 \left(U_{i,i+e_\alpha}\psi_{i+e_\alpha}
      +U_{i,i-e_\alpha}\psi_{i-e_\alpha}\right)
 \right].
 \label{eq:fd2-covariant}$$ Missing neighbors are assigned the Dirichlet value zero. In symmetric gauge, the positive-link phases are $$U_x=\exp(\mathrm{i}Byh_x/2),
 \qquad
 U_y=\exp(-\mathrm{i}Bxh_y/2),
 \label{eq:symmetric-link-phases}$$ with conjugates on reversed links. In Landau gauge $A=(0,Bx)$, they are $U_x=1$ and $U_y=\exp(-\mathrm{i}Bxh_y)$. These choices implement the link definition in [\[eq:peierls-link\]](#eq:peierls-link){reference-type="ref" reference="eq:peierls-link"} and give a Hermitian matrix.

The contour $V=45000$ was pulled back by the centered Hénon inverse. Its boundary was sampled at 8192 angles to form an adapted rectangle, which was then padded by three nominal grid steps. The potential was point-sampled; an overflow guard clipped only values far beyond the nominal wall. The retained eigenvalues lie well below the wall energy. For each 180-mode solve, the deterministic Lanczos starting vector was built from fixed sine and cosine sequences and normalized before shift-invert iteration.

The mode window was never adjusted by inspecting the spacing data. Sorting the spectrum and discarding 25 low and 15 upper modes leaves the 140 levels used throughout. The CDF comparison contains 138 ratios, and all reported CDF distances are sup norms between deterministic empirical and reference curves. No standard error, confidence interval, or $p$-value based on an i.i.d. spacing assumption is reported.

## Failure-first quantum protocol chain

separates the initial questions, repairs, and post-hoc diagnostics. R101 was authorized only after R100 failed; R102 was frozen only after the R101 spacing-stability comparison separated the $a=1.02$ and $a=6$ branches. The latter comparison is labeled post hoc rather than retrospectively promoted to an R100 gate.

::: {#tab:quantum-protocol-chain}
  Run     Frozen change                                                                   Recorded decision
  ------- ------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  R100    FD2, $h=0.04,0.03$; five physical cells                                         Every cell failed the 1% median level-change gate (1.20--1.67%); no class conclusion.
  R101    Add $h=0.0225$ after R100 failure                                               All level gates passed (0.66--0.93%). Post-hoc fine/extrapolated ratio stability passed for $a=1.02$ and failed for both $a=6$ cells.
  R102    Add $h=0.0175$ only for the surviving $a=1.02,B=0,1$ core                       Both frozen level and ratio gates passed on the common 140-level window.
  R103    Freeze $B=0,0.25,0.5,1,2,4$ at $h=0.0225$                                       All five nonzero fields exceeded the scalar baseline; no field was optimized or selected.
  R104    Add $h=0.03$ for the four new R103 fields                                       All level and coarse/fine ratio gates passed.
  R105    Deterministic rerun, two gauges, and $B\leftrightarrow-B$                       All residual, orthogonality, gauge, sign, and reproducibility gates passed.
  R107    FD4 at $h=0.03,0.0225$, compared with archived FD2 extrapolation                All physical cross-stencil gates passed, but the formal maximum Ritz- residual gate failed; the run is retained as a failure.
  R107A   After R107 only: request 200 Ritz pairs, tighten tolerance, retain lowest 180   The residual gate and every unchanged original gate passed. This is a solver-guard remediation only.

  : Chronological quantum audit. "FD2" and "FD4" denote the second- and fourth-order gauge-covariant finite-difference stencils.
:::

The original run summaries retained a historical edge-aggregation mismatch for the level-change fields. The versioned audit recomputes every comparison directly from the archived NPZ arrays on the same 25--164 window used for spacing statistics; the raw spectra and original summaries remain unchanged. On that authoritative window, the R100 median level changes are $1.195\%$ for the radial cell, $1.233\%$ and $1.215\%$ for $a=1.02,B=0,1$, and $1.667\%$ and $1.655\%$ for $a=6,B=0,1$. After R101, the corresponding changes are $0.661\%$, $0.681\%$, $0.677\%$, $0.930\%$, and $0.926\%$. All original pass/fail decisions are unchanged. Passing this level-position gate did not rescue the $a=6$ spacing result: its fine/extrapolated mean-ratio changes remained $0.0404$ and $0.0347$, so that branch is inconclusive rather than a positive or negative RMT control.

The radial spectrum is likewise not interpreted through the usual Poisson mean. Its unresolved $m/-m$ doublets and Cartesian $D_4$ remnants yield a mean ratio near $0.045$ and approximately 39% near-degenerate gaps on the fine grid. Desymmetrization by angular-momentum sectors is necessary before it can be used as an integrable spacing baseline.

## Fourth-order independent-order check

R107 replaces [\[eq:fd2-covariant\]](#eq:fd2-covariant){reference-type="ref" reference="eq:fd2-covariant"} by the one-dimensional stencil, summed over both axes, $$-\frac12D_h^2\psi_i
 =\frac{5}{4h^2}\psi_i
 -\frac{2}{3h^2}
  \left(U_{i,i+1}\psi_{i+1}+U_{i,i-1}\psi_{i-1}\right)
 +\frac{1}{24h^2}
  \left(U_{i,i+2}\psi_{i+2}+U_{i,i-2}\psi_{i-2}\right).
 \label{eq:fd4-covariant}$$ Links over two grid spacings use the exact straight-line integral of the same linear gauge. Zero extension supplies the remote Dirichlet closure. The frozen reference was the already archived R102 second-order $h^2$ extrapolation, not a reference recomputed after seeing R107.

The first R107 solve requested exactly 180 pairs at tolerance $2\times10^{-10}$. Its median relative residuals were about $5\times10^{-12}$, but a few retained edge pairs gave maxima $1.88\times10^{-6}$ and $4.97\times10^{-6}$ on the two fine cells. The recorded global decision was therefore failure even though all level and spacing comparisons passed. R107A's sole allowed change was to compute 200 pairs at tolerance $10^{-12}$, sort, and keep the lowest 180. It did not change the four spectra's physical definitions or the 25--164 window. The remediated fine maxima are $4.65\times10^{-10}$ and $6.86\times10^{-11}$, below the unchanged $10^{-8}$ gate.

Both kinetic schemes remain members of the same broad numerical family. They share Cartesian grids, Peierls phases, sampled potentials, adapted rectangular walls, Dirichlet closure, and ARPACK. R107A is therefore called an independent-order finite-difference check. It is not described as a finite-element replication, a spectral-method replication, or a second fully independent discretization family.

## Numerical integrity and execution environment

::: {#tab:quantum-integrity}
  Check                                    Maximum or difference
  -------------------------------------- -----------------------
  R105 maximum relative eigen-residual      $5.99\times10^{-10}$
  R105 maximum orthogonality defect         $8.04\times10^{-13}$
  symmetric vs. Landau gauge, $B=1$         $2.51\times10^{-14}$
  $B=1$ vs. $B=-1$                         0 at stored precision
  deterministic rerun vs. R100 archive      $3.64\times10^{-14}$
  R107A FD4 fine residual, $B=0$            $4.65\times10^{-10}$
  R107A FD4 fine residual, $B=1$            $6.86\times10^{-11}$
  R107A FD4 fine orthogonality defect       $6.95\times10^{-13}$

  : Numerical-integrity checks. Relative spectral differences use like-indexed sorted eigenvalues.
:::

The recorded production environment used Python 3.12.3, NumPy 2.4.4, SciPy 1.16.1, and Linux 5.4.0 on a 32-vCPU AMD EPYC 9654 allocation with 60 GB of memory. R105 stored SHA-256 hashes for the second-order operator and its audit script, and every solver audit stored its deterministic-initial-vector flag. Machine-readable per-run JSON/NPZ/CSV files accompany the protocols; failed gates and remediation records are kept beside successful runs.

The remaining numerical requirements are substantive rather than cosmetic: a genuinely different fixed-domain discretization, 500--1000 eigenvalues with multiple disjoint windows, a desymmetrized radial comparison, and a broader magnetic classical census. Until those checks are available, the quantum conclusion remains explicitly finite-window and the arithmetic P gate remains open, while Z remains untested and unauthorized before P.

# Discovery protocol and reproducibility boundary {#app:reproducibility}

The prospective research process treats Hilbert--Pólya as an unknown-object search. Route B generates structurally different candidates, applies cheap fatal tests, and promotes only replicated signals with a plausible analytic carrier. Route A begins with a survivor and asks for the shortest bridge chain $$Q\longrightarrow W\longrightarrow S\longrightarrow P\longrightarrow Z.$$ The gates denote a fixed quantum object, the two-growing-term mean clock, active dynamics, an endogenous prime-power trace, and an admissible signed zero-level fluctuation, respectively. Operator-level spectral activity is a separate analytic check within S: it prevents a clock-preserving coordinate warp from being spectrally inert, but it does not prove global classical chaos. A failed later gate cannot be replaced by a high score at earlier gates.

Every candidate advances through $$\text{generated}\to\text{screened}\to\text{replicated signal}
 \to\text{analytic survivor}\to\text{paper candidate}.$$ Failed future candidates remain in the death log with their obstruction. The protocol was formalized after parts of the present family had already been explored and is not a preregistered history of its selection. Retrospectively, the family supports a paper for the partial statement proved here: Q and W pass analytically; one-step operator spectral activity is proved by the strict ground-state and relative-heat theorems; stronger dynamical S claims retain frozen sampled support only. R records finite-window symmetry diagnostics, C records relative-container results, P remains open, and Z is not tested or authorized before P.

All production computations used a 32-vCPU AMD EPYC 9654 allocation with 60 GB of memory. The archived environment records Python 3.12.3, NumPy 2.4.4, SciPy 1.16.1, SymPy 1.14.0, and pytest 9.0.3. Protocols, source code, machine-readable arrays, summaries, failure records, and independent checks accompany the manuscript. The production scripts contain neither a zeta-zero array nor a prime table. The flagship $a=1.02$ value is inherited from an earlier RH-motivated, zero-exposed programme, so its lineage is not statistically blinded. The smooth Riemann--von Mangoldt mean was an explicit design target of the operator from the outset. Prime-time and explicit-formula targets enter only as forward bridge criteria and are not fitted to discrete prime or zero data.

The complete discovery rules and active candidate portfolio are distributed as and . These process documents are not part of the mathematical proof; they record hindsight controls and prevent a numerically attractive symmetry diagnostic from being promoted into an arithmetic claim.
