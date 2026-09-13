---
p1_kind: "derived-fulltext-reading-copy"
route: "symplectic_map"
logical_paper_id: "symplectic_map--1-symp-vs-diss"
canonical_tex: "symplectic_map/papers/1-symp-vs-diss/paper/manuscript.tex"
canonical_pdf: "symplectic_map/papers/1-symp-vs-diss/paper/paper.pdf"
source_sha256: "662af02746d12b55c47a00d0b344a5a2fd9a417a452f0a95271cd0f46181036b"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Transporting a Symbolic Parity Shadow through a Conformally Symplectic Hénon Homotopy: A Controlled Negative Result

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symplectic_map/papers/1-symp-vs-diss>)
- [规范 TeX](<../../../../../symplectic_map/papers/1-symp-vs-diss/paper/manuscript.tex>)
- [关联 PDF](<../../../../../symplectic_map/papers/1-symp-vs-diss/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../symplectic_map/papers/1-symp-vs-diss/README.md>)
- [BibTeX](<../../../../../symplectic_map/papers/1-symp-vs-diss/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  Can a symbolic pattern observed in a critical one-dimensional map survive a regular deformation to a conservative map? We study the frozen family $$H_{a,\rho}(x,y)=(1-a x^2-\rho y,x),\qquad 0\leq\rho\leq1,$$ at the post-critically finite parameter $a=u_{\mathrm c}=1.5436890126920763\ldots$. The family is singular at $\rho=0$, conformally symplectic for $0<\rho<1$, and symplectic at $\rho=1$. An elementary rank argument shows why a critical one-dimensional map cannot be a smooth-submersion factor of a local diffeomorphism across its critical fiber; the Hénon memory coordinate restores regularity by giving up that exact factor relation. We therefore test inheritance rather than assume it.

  A source-locked experiment follows a parent-derived ensemble and measures the parity polarity of return gaps to $x<0$, with trajectory-level bootstrap uncertainty, exposure gates, four neighboring-parameter controls, and a sealed test split. The parent fixture gives polarity $P=1$. At the symplectic endpoint, however, finite exposure is only $0.011724$, no trajectory survives the full horizon, and 9,988 gaps fall below the pre-test-declared minimum. The pre-escape conditional value is $P=-0.70665$, with 95% cluster-bootstrap interval $[-0.71625,-0.69679]$. All neighbors have $P>0.997$ at $\rho=0.10$ and $0.20$, and all reproduce the endpoint collapse, so the observed persistence on those tested cells is not specific to $u_{\mathrm c}$. An exact Jury threshold and a separate attractor diagnostic are consistent with an ordinary dissipative period-$8\to4\to2\to1$ skeleton. Periodic-orbit software independently recovers all 226 expected primitive binary necklaces through period 10 at the high-$a$ positive control, whereas the $u_{\mathrm c}$ ledger remains explicitly incomplete.

  The formal outcome is carrier unavailability for this frozen transport protocol, not a theorem excluding arithmetic structure from every bounded invariant set. In accordance with the stopping rule, no prime labels, Riemann zeros, dynamical determinant, or quantization were opened. The result is a reproducible boundary on one proposed route from critical symbolic dynamics to symplectic dynamics.
author:
- |
  Liang Wang\
  School of Artificial Intelligence and Automation\
  Huazhong University of Science and Technology (HUST)\
  `wangliang.f@gmail.com`
bibliography:
- references.bib
date: August 2026
title: |
  **Transporting a Symbolic Parity Shadow through a\
  Conformally Symplectic Hénon Homotopy:\
  A Controlled Negative Result**
```

## Markdown 正文

# Introduction

Periodic-orbit methods make conservative dynamics an attractive language for spectral and arithmetic analogies. They provide intrinsic primitive objects, repetitions, stability multipliers, actions, and, in suitable hyperbolic settings, transfer operators and dynamical determinants. None of those ingredients by itself establishes a connection to the rational primes. The distinction between a generic prime-orbit theorem and a rational-prime correspondence is essential in any dynamical approach to the Riemann zeros [@berry1999riemann; @rugh1996fredholm].

This study began from a much weaker inherited claim. Earlier one-dimensional work singled out the quadratic map $$f_a(x)=1-a x^2$$ at a post-critically finite parameter $u_{\mathrm c}$, and attributed arithmetic meaning to its symbolic dynamics. A repository audit found reproducible support only for an even-gap, or mod-2, fixture; it did not establish a rational-prime coding. Before comparing multipliers with primes or constructing a zeta function, one must ask whether even that weak symbolic carrier survives a regular deformation to a symplectic map.

The Hénon family is a natural matched laboratory for this question. Conservative--dissipative Hénon homotopies, anti-integrable continuation, and Hénon orbit ledgers are established tools rather than new constructions [@heagy1992physical; @sterling1998antiintegrable; @arai2025antiintegrability; @gallas2007counting; @sattari2017transport]. Canonical two-dimensional weak-noise extensions of the Logistic map and their singularities at $f'=0$ are also direct prior art [@fogedby2005weak; @demaeyer2009escape]. Our contribution is narrow: a frozen, falsifiable survival experiment at one inherited parameter, with explicit carrier gates and negative controls.

The main findings are:

1.  The family obeys an exact conformal-symplectic identity, while a standard rank obstruction proves that the critical parent cannot remain an everywhere regular smooth-submersion factor.

2.  The parent parity fixture and its near-unit small-dissipation continuation are reproducible, but the same pattern occurs at all four neighboring parameters. It is therefore not $u_{\mathrm c}$-specific.

3.  At $\rho=1$, the frozen parent-derived ensemble fails the carrier availability gates by a wide margin. The correct conclusion is *carrier unavailable*, not a survivor-conditioned success and not a universal arithmetic refutation.

4.  An exact fixed-point stability threshold explains the dissipative transition, and a high-$a$ periodic-orbit control separates a working implementation from an incomplete ledger at $u_{\mathrm c}$.

These results trigger the source-locked stop rule. No primes, zeros, or targeted spectral data are used anywhere in the candidate definition or experiment. A failed entry gate cannot be repaired by fitting a downstream dynamical determinant.

# The frozen family and its exact geometry {#sec:geometry}

## Parameter provenance and endpoints

We freeze $$H_{a,\rho}(x,y)=(1-a x^2-\rho y,x),\qquad
 a=u_{\mathrm c}=1.5436890126920763\ldots .
 \label{eq:map}$$ The value $u_{\mathrm c}$ is the positive real root of $$a^3-2a^2+2a-2=0.
 \label{eq:cubic}$$ It was inherited before inspecting any Hénon orbit multiplier, prime label, or Riemann zero. Equation [\[eq:cubic\]](#eq:cubic){reference-type="eqref" reference="eq:cubic"} gives the exact post-critical itinerary $$0\mapsto1\mapsto1-a\mapsto a-1\mapsto a-1$$ for $f_a$. The terminal fixed point is repelling, with multiplier $-2a(a-1)=-1.67857\ldots$. Exact parameter provenance prevents numerical target fitting, but it does not confer arithmetic specificity.

The derivative is $$DH_{a,\rho}(x,y)=
\begin{pmatrix}
 -2ax & -\rho\\
 1 & 0
\end{pmatrix},
\qquad
\det DH_{a,\rho}=\rho .
\label{eq:jacobian}$$ For $\Omega=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$, every real $2\times2$ matrix $A$ obeys $A^{\mathsf T}\Omega A=(\det A)\Omega$. Hence $$DH_{a,\rho}^{\mathsf T}\Omega DH_{a,\rho}=\rho\Omega.
\label{eq:conformal}$$ Thus $\rho=0$ is a singular parent reference, $0<\rho<1$ is conformally symplectic and dissipative, and $\rho=1$ is symplectic. For every period-$n$ orbit $\gamma$, $$\det M_\gamma=\rho^n.
\label{eq:monodromy}$$ Reciprocal multipliers at $\rho=1$ are geometric facts, not arithmetic evidence.

## Generating function at the symplectic endpoint

Write old coordinates as $(q,p)$ and new coordinates as $(Q,P)=H_{a,1}(q,p)$. Then $$Q=1-aq^2-p,\qquad P=q.$$ The type-1 generating function $$S_a(q,Q)=qQ-q+\frac{a}{3}q^3
\label{eq:generating}$$ satisfies $$p=-\partial_qS_a=1-aq^2-Q,\qquad P=\partial_QS_a=q.$$ Consequently, a periodic orbit has intrinsic discrete action $$\mathcal A_\gamma=\sum_{j=0}^{n-1}S_a(q_j,q_{j+1}).$$ We make no canonical-action claim for $\rho<1$, and we do not infer a quantization from the existence of [\[eq:generating\]](#eq:generating){reference-type="eqref" reference="eq:generating"}.

## Why inheritance must be tested

[\[prop:rank\]]{#prop:rank label="prop:rank"} Let $f:N\to N$ be a $C^1$ map of a one-dimensional manifold, $\pi:M\to N$ a $C^1$ submersion, and $F:M\to M$ a $C^1$ local diffeomorphism. If $\pi\circ F=f\circ\pi$, then no point in the image of $\pi$ can be a critical point of $f$.

At $z\in M$, differentiate the semiconjugacy: $$D\pi_{F(z)}DF_z=Df_{\pi(z)}D\pi_z.$$ The left-hand side is surjective because $DF_z$ is invertible and $D\pi_{F(z)}$ is surjective. At a critical point of a one-dimensional map, the right-hand side is zero. The ranks cannot agree.

In triangular coordinates, the same obstruction reads $$F(q,p)=(f(q),P(q,p)),\qquad \det DF=f'(q)\,\partial_pP.$$ A finite $C^1$ symplectic derivative cannot satisfy this identity at $f'(q)=0$. This elementary statement is consistent with the singular lines found in canonical weak-noise extensions [@fogedby2005weak; @demaeyer2009escape]. More generally, a smooth map defines a canonical relation, whereas an ordinary cotangent symplectomorphism needs stronger invertibility assumptions [@cattaneo2010microgeometry; @weinstein2010categories]. Inverse limits and branch-labeled extensions lie outside the proposition's regularity class [@berger2013inverse].

The Hénon map avoids the contradiction because its first coordinate depends on the memory variable $y$. It is not an exact projection semiconjugacy: $$\pi H_{a,\rho}(x,y)=1-a x^2-\rho y\neq f_a(\pi(x,y))
 \quad(\rho>0).$$ Thus regularity is restored by giving up exact inheritance. Any symbolic or arithmetic shadow must be measured anew.

## A fixed-point mechanism and an analytic negative control {#sec:fixed}

A fixed point satisfies $a x^2+(1+\rho)x-1=0$. At the positive fixed point, the characteristic polynomial is $$\lambda^2+2ax\,\lambda+\rho.$$ The Jury conditions give the flip boundary $$\rho_{\rm PD}(a)=\sqrt{\frac{4a}{3}}-1,
\qquad
\rho_{\rm PD}(u_{\mathrm c})=0.434660941450198\ldots .
\label{eq:jury}$$ At $\rho=1$, the determinant condition prevents any periodic orbit from being a sink.

The negative fixed point supplies a separate proves-too-much control. At $\rho=1$, its trace is $2+2\sqrt{1+a}$. Requiring its unstable multiplier to equal any selected $m>1$ gives $$a=\frac{(m-1)^4}{4m^2}-1.
\label{eq:tunable}$$ In particular, $a=1.56$ gives the exact multiplier $m=5$, while $a=u_{\mathrm c}$ gives $4.98936\ldots$. A single near-prime multiplier can therefore be produced by a one-parameter algebraic coincidence and is not evidence for a primitive-orbit/prime correspondence.

# Source-locked experimental design {#sec:protocol}

## Observable and carrier gates

We encode an iterate as $L$ when $x<0$ and $R$ otherwise. If $t_1<t_2<\cdots$ are consecutive visits to $L$ before escape, the return gaps are $g_j=t_{j+1}-t_j$. The primary statistic is $$P=\frac{N_{\rm even}-N_{\rm odd}}
         {N_{\rm even}+N_{\rm odd}}.
\label{eq:polarity}$$ The inherited parent prediction is $P=1$. This is a parity fixture, not a rational-prime statistic.

For every trajectory we stop recording after either coordinate becomes non-finite or has absolute value greater than 100. Exposure is the number of finite pre-escape iterates divided by $NT$. The confirmatory endpoint was interpretable only if $$\text{exposure}\geq0.80,\qquad N_{\rm gaps}\geq10{,}000.$$ Conditional polarity among a small number of escaping fragments could not override a failed carrier gate.

Success additionally required the lower endpoint of a 95% trajectory-cluster bootstrap interval for $P(1)$ to be at least $0.98$, and required $u_{\mathrm c}$ to outperform every $a\in\{1.50,1.52,1.56,1.58\}$ after a one-sided Holm family correction. The Holm quantities are bootstrap sign-tail diagnostics rather than exact randomized-treatment $p$-values; effect sizes and trajectory-level intervals are the primary comparisons.

## Ensemble, splits, and forbidden data

Each split uses $N=2048$ trajectories, a parent burn-in of 4096 iterations, and horizon $T=1024$. PCG64 draws $x_{-\mathrm{burn}}$ uniformly from $[-1,1]$; after burning the $\rho=0$ parent, consecutive states initialize $(x_0,x_{-1})$ for every $\rho$ arm. Common random numbers pair candidate and neighbor trajectories. We use 2,000 bootstrap replicates and resample whole trajectories.

The frozen grid is $$\rho\in\{0,0.02,0.05,0.10,0.20,0.50,1.00\}.$$ Development, validation, and test use seeds 20260812, 20260813, and 20260814. The candidate and all four neighbor test arms were opened as one batch after the analysis implementation and thresholds were frozen.

Forbidden Stage-1 data included prime labels, Riemann zeros, parameters selected to make multipliers close to integers or primes, target-fitted phases or scales, and manually inserted von Mangoldt weights. The stopping rule closed the prime-multiplier, zeta, and quantization branches if either the endpoint carrier failed or the weak shadow proved nonspecific.

## Protocol provenance

The protocol is source-locked, but it was not frozen before all exploratory work. Source-lock version 2 followed development-only smoke tests. Before the full frozen validation run, one small validation smoke $(N,T,\text{bound})=(512,512,10^6)$ was written to a temporary directory and excluded. The full frozen validation was then run once. The manifest was amended after validation analysis, but before any test artifact existed, to hash the paired-analysis implementation and list all four already-declared neighbor commands. All five test arms were then opened together. At the time, the session root was not a Git worktree, so provenance relied on hashes and the single-use access log. These limitations weaken any claim of a fully prospective protocol but do not alter the large endpoint gate failure.

## Periodic-orbit implementation control

For period $n$, the code solves $H^n(z)-z=0$, canonicalizes cyclic shifts, rejects shorter repetitions, and computes the ordered monodromy product. Primitive binary necklaces seed the $(a,\rho)=(6,1)$ control. Their expected number is $$B_n=\frac{1}{n}\sum_{d\mid n}\mu(d)\,2^{n/d}.
\label{eq:necklace}$$ An independent implementation refines each found cycle using 80-digit arithmetic and rechecks residuals, determinants, and primitiveness. This is a high-precision residual audit, not interval certification.

The same solver is applied exploratorily at $(u_{\mathrm c},1)$ through period 8. No completeness claim is allowed there without root isolation or a covering argument. Passing the $a=6$ software control cannot transfer hyperbolicity or completeness to the mixed, escaping $u_{\mathrm c}$ regime.

# Results {#sec:results}

## Small-dissipation persistence is nonspecific

Development, validation, and sealed test all reproduce $P(0)=1$ with full exposure. Table [1](#tab:test){reference-type="ref" reference="tab:test"} gives the complete frozen-parameter test grid. At $\rho=0.02$ through $0.20$, every trajectory survives and polarity remains near one. The carrier then changes sharply: $\rho=0.50$ has exposure $0.7346$, while $\rho=1$ has exposure only $0.011724$.

::: {#tab:test}
    $\rho$   Exposure   Survival        Gaps                       $P$ \[95% CI\]
  -------- ---------- ---------- ----------- ------------------------------------
         0   1.000000   1.000000     460,189                    $1.000000\ [1,1]$
      0.02   1.000000   1.000000     613,935      $0.999567\ [0.999495,0.999632]$
      0.05   1.000000   1.000000     717,873      $0.999382\ [0.999306,0.999457]$
      0.10   1.000000   1.000000     522,987      $0.998776\ [0.998657,0.998899]$
      0.20   1.000000   1.000000   1,041,094      $0.998907\ [0.998811,0.998996]$
      0.50   0.734622   0.732422       2,723   $-0.904517\ [-0.919610,-0.888528]$
      1.00   0.011724          0       9,988   $-0.706648\ [-0.716253,-0.696785]$

  : Sealed-test results at $a=u_{\mathrm c}$. Confidence intervals resample whole trajectories. The $\rho=1$ polarity is descriptive because the availability gate fails.
:::

![Frozen symbolic transport across the homotopy. Panel (a) reports return-gap parity polarity and panel (b) reports finite exposure. Development, validation, sealed-test, and neighboring-$a$ curves are overlaid in the two panels. All four neighbors reproduce near-unit parity at $\rho=0.10$ and $0.20$, while the parent-derived carriers collapse near the symplectic endpoint. The endpoint $P$ is conditional on rare pre-escape fragments and cannot pass the exposure gate.](<../../../../../symplectic_map/papers/1-symp-vs-diss/paper/figures/fig1_final_shadow_transport.pdf>){#fig:transport width="\\linewidth"}

The neighbor panel in Fig. [1](#fig:transport){reference-type="ref" reference="fig:transport"} is the decisive specificity control. In both validation and test, every neighbor has $P>0.997$ at $\rho=0.10$ and $0.20$. At $\rho=1$, every neighbor has approximately one-percent exposure, zero full-horizon survivors, and negative polarity. All four endpoint Holm-adjusted directional diagnostics equal 1.0. Thus the small-dissipation persistence is generic across the tested parameter neighborhood under this partition and protocol, not a feature isolated at $u_{\mathrm c}$. This is the source-locked *proves-too-much* outcome.

## The symplectic endpoint fails the carrier gate

At $\rho=1$, the sealed test yields $$\text{exposure}=0.0117239952,\qquad
\text{survival}=0,\qquad
N_{\rm gaps}=9{,}988.$$ Both availability requirements fail. The conditional pre-escape value $$P=-0.70664798,\qquad
\mathrm{CI}_{95\%}=[-0.71625339,-0.69678543]$$ also fails the polarity requirement, but decision precedence assigns the more basic label $$\boxed{\texttt{A0\_SHADOW\_FAIL\_CARRIER\_UNAVAILABLE}}.$$ This means that the frozen parent-derived ensemble cannot support the planned endpoint comparison. It does not say that all bounded invariant sets of $H_{u_{\mathrm c},1}$ are empty or arithmetically featureless.

## A dissipative mechanism explains the transition

After confirmatory analysis, a distinct diagnostic used 256 trajectories for each of five $a$ values and a denser $\rho$ grid. Its purpose was mechanism identification, not a new confirmatory test. At $u_{\mathrm c}$, the resolved sequence was $$\text{unresolved/high period}\ \longrightarrow\
8\longrightarrow4\longrightarrow2\longrightarrow
\text{positive fixed point}.$$ The period-2/fixed-point switch lies between $\rho=0.43$ and $0.44$, bracketing [\[eq:jury\]](#eq:jury){reference-type="eqref" reference="eq:jury"}. Each neighbor switches on the adjacent grid cells around its own analytic threshold.

![Post-validation mechanism diagnostic. Resolved periods and escape fractions follow the fixed-point flip threshold $\rho_{\rm PD}(a)=\sqrt{4a/3}-1$ at the frozen parameter and its neighbors. At $\rho=1$, all 256 trajectories in the $u_{\mathrm c}$ diagnostic escape. Counts describe this ensemble, not the whole phase space.](<../../../../../symplectic_map/papers/1-symp-vs-diss/paper/figures/fig3_dissipative_attractors.pdf>){#fig:attractors width="\\linewidth"}

At $\rho=0.50$, 183 of 256 $u_{\mathrm c}$ diagnostic trajectories approach the positive fixed point and 73 escape. At $\rho=1$, all 256 escape. Equation [\[eq:monodromy\]](#eq:monodromy){reference-type="eqref" reference="eq:monodromy"} supplies the structural reason that a periodic sink cannot persist at the area-preserving endpoint. The observed transition is consistent with an ordinary dissipative attractor skeleton; unresolved cells at $\rho=0.02$ and $0.05$ preclude a stronger full-grid mechanism claim.

## The orbit finder passes its control, but the main ledger is incomplete

At $(a,\rho)=(6,1)$, the implementation recovers $$(B_1,\ldots,B_{10})=(2,1,2,3,6,9,18,30,56,99),$$ exactly matching [\[eq:necklace\]](#eq:necklace){reference-type="eqref" reference="eq:necklace"}. All 226 cycles refine in the independent 80-digit audit; the maximum cyclic residual is $7.04\times10^{-61}$, and the maximum determinant error is $7.42\times10^{-68}$.

At $(u_{\mathrm c},1)$, binary seeds find only $$2,0,2,2,2,3,4,5$$ primitive cycles through period 8, versus the binary-necklace reference $$2,1,2,3,6,9,18,30.$$ All 20 found cycles pass the high-precision residual audit, with maximum residual $3.79\times10^{-61}$, but that certifies only the cycles found. It does not bound missed cycles.

![Periodic-orbit implementation audit. The $a=6,\rho=1$ positive control matches exact primitive binary-necklace counts through period 10 (left). The frozen $u_{\mathrm c},\rho=1$ exploratory ledger is visibly incomplete (right). High-precision residual refinement is not an interval-completeness certificate.](<../../../../../symplectic_map/papers/1-symp-vs-diss/paper/figures/fig2_orbit_ledger.pdf>){#fig:ledger width="\\linewidth"}

Figure [3](#fig:ledger){reference-type="ref" reference="fig:ledger"} makes the evidence boundary visible. The positive control shows that the routines can recover and audit a declared complete ledger in a suitable regime. The main parameter lies far from that regime. It therefore cannot support a cycle expansion, Fredholm determinant, or multiplier-enrichment experiment.

# Discussion {#sec:discussion}

## What the negative result does and does not say

Three statements are often collapsed in an unsuccessful transport experiment:

1.  the parent observable is absent;

2.  the observable changes under the homotopy;

3.  the chosen endpoint ensemble does not provide an adequate carrier.

Here the first is false: the parent parity fixture is reproduced across all three splits. Small-$\rho$ parity is present, but neighbor controls show that it is nonspecific. At $\rho=1$, the third statement is decisive because the exposure gate fails. The descriptive negative pre-escape polarity is consistent with shadow loss, but it cannot be promoted to a claim about every bounded endpoint orbit.

The narrow conclusion is nevertheless useful. The proposed route required a frozen parent-derived carrier to reach the conservative endpoint before any arithmetic orbit mechanism could be tested. That prerequisite fails. A new compact invariant set, branch-labeled natural extension, different partition, or altered initialization would define a new candidate and need a new source lock; it cannot retroactively repair this result.

## Why symplecticity is insufficient

Symplecticity guarantees area preservation, reciprocal multipliers, and an intrinsic action convention for [\[eq:map\]](#eq:map){reference-type="eqref" reference="eq:map"}. It does not guarantee that a critical parent remains a factor, that a noncompact ensemble is recurrent, that an orbit ledger is complete, or that a rational-prime weight emerges. The Hénon literature already contains sophisticated symbolic ledgers and spectral determinants [@gallas2007counting; @sattari2017transport; @rugh1996fredholm]; repeating that machinery without an arithmetic source would not cross an arithmetic relevance gate.

A provisional unstable-multiplier product, $$Z_u(s)=\prod_\gamma
\left(1-|\Lambda_{u,\gamma}|^{-s}\right)^{-1},$$ would have a prime-like repetition expansion only under convergence and an independently established correspondence between primitive multipliers and rational primes. Neither is supplied here. Moreover, a two-dimensional symplectic semiclassical stability factor is $$\frac{1}{|\det(M_\gamma^r-I)|^{1/2}}
=\frac{|\Lambda_{u,\gamma}|^{-r/2}}
{|1-\Lambda_{u,\gamma}^{-r}|},$$ not simply the weight in that provisional product. We do not mix a Ruelle-type Euler product with a Gutzwiller denominator.

## Novelty boundary

The rank obstruction in Proposition [\[prop:rank\]](#prop:rank){reference-type="ref" reference="prop:rank"} is elementary, and the singularity of canonical extensions at the critical line is known [@fogedby2005weak; @demaeyer2009escape]. Conservative--dissipative Hénon continuation and periodic-orbit enumeration are mature [@heagy1992physical; @sterling1998antiintegrable; @arai2025antiintegrability; @gallas2007counting; @sattari2017transport]. The title phrase *arithmetical signatures of the Hénon map* also has prior use for algebraic orbit structure rather than rational-prime coding [@endler2002arithmetical].

Accordingly, the contribution is not a new Hénon family, lift, or zeta formalism. It is the controlled audit of one exact inherited parameter: freezing the weakest reproducible symbolic claim, separating exposure from conditional statistics, checking neighbors, validating the orbit implementation in a positive-control regime, and stopping when the entry gate fails.

## Limitations

-   The experiment concerns one noncompact polynomial family, one parent-derived initialization, one partition, and finite time. It is not exhaustive over invariant measures or bounded sets.

-   The inherited parent claim is only a parity fixture. The study cannot refute a rational-prime mechanism that was never independently established.

-   The $u_{\mathrm c}$ periodic-orbit ledger lacks a completeness certificate. High-precision residuals are not interval root isolation.

-   The source lock followed development work, and the manifest was amended after validation but before the sealed test. A small disclosed validation smoke was excluded.

-   The cluster bootstrap quantifies trajectory-level sampling variability under the frozen ensemble. It does not resolve structural uncertainty from the escape box, partition, or finite horizon.

These limitations narrow the conclusion; they do not justify ignoring the stop rule.

## Requirements for a new candidate

A successor would need to change the mathematical object, not tune the failed one after seeing the outcome. Two possibilities remain open: a branch-labeled natural extension that treats the critical point explicitly, or a genuinely compact/invariant symplectic carrier with an arithmetic source defined before prime or zero data are opened. Either must predeclare its phase space, invariant measure, observable, orbit clock, completeness logic, arithmetic controls, and failure rules. Higher dimension alone does not address the rank, carrier, or specificity obstructions.

# Conclusion

The conformally symplectic Hénon homotopy provides a clean geometric bridge but not a transparent inheritance principle. At the frozen post-critically finite parameter, the parent parity fixture persists for small dissipation, yet all nearby parameters do the same on the tested $\rho=0.10,0.20$ cells. An exact Jury threshold and an independent diagnostic are consistent with an ordinary dissipative attractor sequence. At the symplectic endpoint, the parent-derived carrier has roughly 1.17% exposure, no full-horizon survivors, and too few return gaps to support the pre-test-declared comparison.

The negative statement is precise: this frozen carrier does not deliver a specific weak symbolic shadow to the conservative endpoint under the declared protocol. It is neither an arithmetic success nor a universal arithmetic impossibility theorem. Because the entry gate failed and the main periodic-orbit ledger is incomplete, prime matching, dynamical determinants, Riemann-zero comparisons, and quantization remain unopened. The value of the study is the boundary it establishes and the reproducible stopping decision it enforces.

# Data and code availability {#data-and-code-availability .unnumbered}

The source lock, access log, raw artifacts, cluster-aware analysis, figures, tests, periodic-orbit ledgers, and high-precision audits are distributed in the [project repository](https://github.com/maris205/hilbert-polya-structure/tree/main/symplectic_map). The paper directory is `papers/1-symp-vs-diss/`. No prime or Riemann-zero dataset is needed to reproduce the reported results.

# Artifact hashes and reproduction boundary {#app:repro}

The three central frozen hashes are:

    7d81c30863c0e27ba0e5494c9ad76b148a9e0edbdc213adbc233794b713d6d0e
      experiments/source_lock.json
    b8186fcd6e323d2e6d2e7e5c05f5f18b98cdf92475675bce25d74e0d158e3cf8
      experiments/confirmatory_manifest.json
    a8c272161bd38e37e140c0ad72511461e4fb837edf2bf7880ba21014b89705c5
      results/analysis/transport_test_analysis_v1.json

Raw sealed-test and neighbor hashes are in . From the paper-project root (the directory named ), the following commands check the software and reproduce analyses under new names:

    cd code
    PYTHONPATH=. pytest -q
    python scripts/run_ledger.py --preset positive-control --max-period 10 \
      --output /tmp/ledger_positive_a6_rho1_n10_reproduction.json
    python scripts/audit_ledger.py \
      /tmp/ledger_positive_a6_rho1_n10_reproduction.json \
      --output /tmp/ledger_positive_a6_rho1_n10_audit80_reproduction.json \
      --digits 80
    cd ..
    python code/scripts/analyze_transport.py --split test \
      --output-stem transport_test_analysis_reproduction_YYYYMMDD

The sealed trajectory generator should not be rerun under the original test label. Any new seed, threshold, partition, or endpoint is a post-confirmatory experiment and cannot alter the archived decision.

# Evidence labels

Exact identities [\[eq:jacobian\]](#eq:jacobian){reference-type="eqref" reference="eq:jacobian"}--[\[eq:monodromy\]](#eq:monodromy){reference-type="eqref" reference="eq:monodromy"}, the generating function, the rank obstruction, the Jury threshold, and identity [\[eq:tunable\]](#eq:tunable){reference-type="eqref" reference="eq:tunable"} are proved statements. The transport and attractor findings are numerical observations under frozen finite protocols. The $a=6$ ledger is numerically certified only for its declared cutoff and regime. The $u_{\mathrm c}$ ledger is exploratory and incomplete. Claims about a rational-prime correspondence, a Riemann dynamical determinant, analytic continuation, quantization, or Riemann zeros are stop-scoped and were never tested.
