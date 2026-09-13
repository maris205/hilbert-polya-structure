---
p1_kind: "derived-fulltext-reading-copy"
route: "flow_systems"
logical_paper_id: "flow_systems--1-classical-flow"
canonical_tex: "flow_systems/papers/1-classical-flow/paper/manuscript.tex"
canonical_pdf: "flow_systems/papers/1-classical-flow/paper/paper.pdf"
source_sha256: "a49ceb0bfa13a68e4eeccbdf81b127ebab7785f707bfe4320c956198b088c7fd"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Arithmetic Periods versus Hyperbolic Trace Structure: A Route-A Baseline for Continuous Flows

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../flow_systems/papers/1-classical-flow>)
- [规范 TeX](<../../../../../flow_systems/papers/1-classical-flow/paper/manuscript.tex>)
- [关联 PDF](<../../../../../flow_systems/papers/1-classical-flow/paper/paper.pdf>)
- [支撑 Markdown](<../../../../../flow_systems/papers/1-classical-flow/README.md>)
- [BibTeX](<../../../../../flow_systems/papers/1-classical-flow/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We test a necessary classical layer of a Hilbert--Pólya programme: whether a continuous-time system can produce, without prime or zero fitting, primitive periods and repetition weights compatible with $\log p$ and $(\log p)p^{-r/2}$. The comparison reveals a sharp "two-halves" obstruction. Deninger's rational-Witt flow attached to $\operatorname{Spec}\mathbb{Z}$ has an intrinsic arithmetic clock: a rational prime indexes a compact packet of periodic orbits of period $\log p$. It does not yet provide a canonical isolated-orbit representative, packet multiplicity, monodromy, phase, or trace weight. Conversely, the modular geodesic flow has an analytic primitive/repetition ledger, exact Selberg and Ruelle products, transverse stability, and a natural Laplace spectral host. We prove that, for every hyperbolic $\gamma\in\operatorname{PSL}_2(\mathbb{Z})$ and every $r\ge1$, $\exp(r\ell_\gamma)\notin\mathbb{Q}$. Hence its repeated closed-orbit length support is disjoint from all rational-prime-power logarithms. We also isolate a deceptive intrinsic proxy $q=\operatorname{tr}(\gamma^2)=\exp(\ell)+\exp(-\ell)$: when $q$ is prime, $\log q-\ell=O(\exp(-2\ell))$, producing excellent but structurally false numerical matches. A two-phase, zero-free enumeration gives 8,798 oriented primitive modular classes through 16 symbolic blocks and verifies the exact Selberg/Ruelle amplitude relation. No frozen candidate passes both the arithmetic-origin and isolated-orbit gates; the smallest positive next problem is a canonical trace or measure on Deninger's prime packets.
author:
- |
  Liang Wang\
  School of Artificial Intelligence and Automation,\
  Huazhong University of Science and Technology, Wuhan 430074, P.R. China\
  `wangliang.f@gmail.com`
bibliography:
- references.bib
date: 13 August 2026
title: |
  **Arithmetic Periods versus Hyperbolic Trace Structure:**\
  A Route-A Baseline for Continuous Flows
```

## Markdown 正文

# Introduction

The periodic-orbit reading of the Riemann explicit formula asks for much more than a chaotic spectrum. In its cleanest form, a rational prime should index a primitive dynamical object, its powers should arise as repetitions, and the same intrinsic clock should produce $$p\longleftrightarrow\gamma_p,
  \qquad T_{\gamma_p}=\log p,
  \qquad
  A_{\gamma_p,r}\sim (\log p)p^{-r/2}.
  \label{eq:target}$$ The formal analogy is classical [@Weil1972; @BerryKeating1999]; its realization by a fixed dynamical and spectral object remains open. Agreement of unfolded spacings, a prime-orbit counting law, or a fitted list of zeros is not sufficient: those signals can survive in systems with no rational-prime origin.

This paper implements the first stage of a source-locked research programme. The question is deliberately narrower than constructing the final operator:

> To what extent can an explicitly defined continuous-time flow produce, without prime or zero fitting, primitive periods and repetition weights structurally compatible with rational-prime terms?

The answer is negative for the frozen candidates, but the negative result is informative rather than generic. Existing constructions split the required structure in two. Arithmetic-scheme flows possess the correct arithmetic periods at packet level [@Deninger2026; @Deninger2023]; hyperbolic geodesic flows possess the best exact orbit/trace/quantization architecture [@Selberg1956; @Hejhal1983; @PohlZagier2020]. Neither presently supplies the other half.

Our contributions are:

1.  a source lock and Route-A evaluation of arithmetic, modular, hyperbolic, suspension, and $xp$ flow candidates;

2.  an exact irrationality theorem showing that the modular repeated length support and rational-prime-power logarithmic support are disjoint;

3.  an arithmetic trilemma for norm-, trace-, and adjoint-trace-based relabellings, including a precise near-prime numerical false positive;

4.  an exact comparison of Selberg, Ruelle, and Weil repetition weights;

5.  a deterministic, two-phase orbit ledger that freezes the geometry before any rational-prime control is computed; and

6.  a critical inheritance audit of the preceding Logistic and Hénon line, separating exact geometry from conjecture, calibration, and fitting.

The claims are intentionally bounded. We do not prove that every smooth finite-dimensional flow must fail, nor that a canonical packet trace for the arithmetic flow cannot exist. We prove exact obstructions for specified objects with specified clocks.

# Decision framework and evidence boundary

## Two independent gates

We separate two obligations that are often conflated.

#### A0: arithmetic relevance.

The arithmetic source, prime mechanism, repetition mechanism, and weight must come from the candidate. Manually setting roof lengths to $\log p$, inserting von Mangoldt weights, selecting parameters by Riemann zeros, or offering GUE alone fails this gate.

#### A1: primitive-orbit structure.

The candidate must define primitive and repeated cycles, orientation, multiplicity, period, phase where applicable, and transverse monodromy. A finite enumeration must disclose missed-orbit risk and its cutoff convention. Packet-level periodic structure can be genuine while remaining weaker than a conventional isolated-orbit trace.

We use the verdict vocabulary in Table [1](#tab:verdicts){reference-type="ref" reference="tab:verdicts"}. 'OPEN' is an evidence status, not an A1 verdict. A candidate can therefore have proved packet structure and still receive `A1_WEAK`.

::: {#tab:verdicts}
  Verdict                Meaning in this paper
  ---------------------- --------------------------------------------------------------------------------------------------------------------

  ARITHMETIC\_ORIGIN     A theorem derives the arithmetic indexing and clock from the object.

  ARITHMETIC\_RELATION   The object is arithmetically defined, but the required rational-prime mechanism fails or is absent.
  `A0_FAIL`              No intrinsic rational-prime source is present.
  `A1_PASS_ANALYTIC`     Primitive/repetition data and stability are theorem-level.
  `A1_WEAK`              Genuine periodic structure exists, but the required ledger, isolation, multiplicity, or trace data are incomplete.
  `A1_FAIL`              The frozen object lacks the required nontrivial periodic structure.

  : Interpretation of the Stage-1 verdicts.
:::

## Exact, distributional, semiclassical, and heuristic statements

Four mathematically different claims must remain separate.

First, the Selberg trace formula is an exact identity for its specified surface, test functions, and full geometric/spectral terms [@Selberg1956; @Hejhal1983]. Second, the Duistermaat--Guillemin wave trace is an exact distributional and microlocal result: closed bicharacteristics control singular support and local coefficients, not automatically a globally convergent orbit sum [@DuistermaatGuillemin1975]. Third, the generic Gutzwiller trace expression is semiclassical [@Gutzwiller1971]. Fourth, the identification of a Riemann prime with a classical orbit is heuristic unless a candidate derives it [@BerryKeating1999].

For smooth Anosov flows, Ruelle-zeta continuation and Pollicott--Ruelle resonances are rigorous but generally non-self-adjoint structures [@GLP2013; @DyatlovZworski2016]. The 2022 erratum to @GLP2013 corrects a spectral-gap portion while leaving the meromorphic continuation result unaffected [@GLPErratum2022]. We do not use a resonance theorem as if it supplied a Hilbert--Pólya self-adjoint spectrum.

# Frozen candidates {#sec:candidates}

Table [2](#tab:candidates){reference-type="ref" reference="tab:candidates"} records the objects before testing. Class-wide rows are controls, not numerical candidates, unless a member is separately frozen.

::: {#tab:candidates}
  ID                   Frozen object and clock                                                                                                                                                                              Role
  -------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------
  `DEN-WITT-Z-FIN`     Deninger's rational-Witt flow for $\operatorname{Spec}\mathbb{Z}$, with an allowed finite-kernel admissibility condition, denoted here by $\mathcal E_{\rm fin}$; $\phi^t[P,u]=[P,\mathrm{e}^t u]$   strongest arithmetic-origin candidate
  `MOD-GEO`            unit-speed geodesic flow on $T^1(\operatorname{PSL}_2(\mathbb{Z})\backslash\mathbb H)$; hyperbolic arc length                                                                                        strongest isolated-orbit/exact-trace candidate
  `COMPACT-GEO`        unit-speed flow on a compact curvature $-1$ surface                                                                                                                                                  proves-too-much control
  `CONTACT-ANOSOV`     smooth contact Anosov flow class                                                                                                                                                                     analytic-zeta comparator
  `HENON-SUSP`         constant-roof mapping-torus suspension of the area-preserving Hénon map; roof independent of primes and zeros                                                                                        prior-lineage/geometric control
  `HYP-BILLIARD`       autonomous dispersing/hyperbolic billiard class with mechanical clock                                                                                                                                semiclassical comparator
  `BERRY-KEATING-XP`   unregularized $H=xp$ flow on $\mathbb{R}^2$, with no added boundary or cutoff                                                                                                                        counting/no-closed-orbit comparator

  : Candidate source locks and their roles.
:::

The modular and Deninger objects are not directly comparable as smooth manifolds: the latter is infinite-dimensional and topological. We therefore do not average their gate scores into a scalar. The useful comparison is an obligation matrix: which exact ingredients exist, and which are absent?

# The modular geodesic obstruction {#sec:modular}

Let $\gamma\in\operatorname{PSL}_2(\mathbb{Z})$ be hyperbolic and let an $\mathrm{SL}_2(\mathbb{Z})$ representative have absolute trace $t\ge3$. Its expanding eigenvalue, geodesic length, and standard Selberg norm are $$\lambda_\gamma=\frac{t+\sqrt{t^2-4}}{2},\qquad
 \ell_\gamma=2\log\lambda_\gamma,
 \qquad N_\gamma=\mathrm{e}^{\ell_\gamma}=\lambda_\gamma^2.
 \label{eq:modnorm}$$ Primitive hyperbolic conjugacy classes correspond to primitive closed geodesics; powers produce repetitions [@PohlZagier2020; @Sarnak1982].

[\[thm:irrational\]]{#thm:irrational label="thm:irrational"} For every hyperbolic $\gamma\in\operatorname{PSL}_2(\mathbb{Z})$ and every integer $r\ge1$, $N_\gamma^r\notin\mathbb{Q}$.

The characteristic equation gives $\lambda_\gamma+\lambda_\gamma^{-1}=t$, hence $$N_\gamma+N_\gamma^{-1}=t^2-2.
 \label{eq:normidentity}$$ The discriminant $t^2-4$ is not a square for $t\ge3$: if $t^2-u^2=4$, then $(t-u)(t+u)=4$, and the only nonnegative same-parity factorization gives $t=2$. Thus the nontrivial Galois conjugation sends $N_\gamma$ to $N_\gamma^{-1}$. If $N_\gamma^r\in\mathbb{Q}$, it is fixed by conjugation, so $N_\gamma^r=N_\gamma^{-r}$. This contradicts $N_\gamma>1$.

[\[cor:support\]]{#cor:support label="cor:support"} For all rational primes $p$ and positive integers $r,k$, $$r\ell_\gamma\ne k\log p.$$ Consequently the positive supports of the modular repeated-orbit measure and the rational-prime-power explicit-formula measure are disjoint.

Equality would imply $N_\gamma^r=p^k\in\mathbb{Q}$, contradicting Theorem [\[thm:irrational\]](#thm:irrational){reference-type="ref" reference="thm:irrational"}.

This is stronger than a failed finite search. It rules out an atom-by-atom identification under the frozen unit-speed clock. It does not rule out every possible role for arithmetic surfaces, nor every time change of every flow; those are different candidates requiring new source locks.

## The near-prime proxy trap

There is an intrinsic integer that can make the failed identification look numerically compelling: $$q_\gamma=t^2-2=\operatorname{tr}(\gamma^2)
 =N_\gamma+N_\gamma^{-1}.
 \label{eq:qproxy}$$ It satisfies $$q_\gamma-N_\gamma=N_\gamma^{-1},\qquad
 \log q_\gamma-\ell_\gamma=\log(1+N_\gamma^{-2})
 =N_\gamma^{-2}+O(N_\gamma^{-4}).
 \label{eq:proxyerror}$$ Thus, whenever $q_\gamma$ happens to be prime, $\ell_\gamma$ can appear to reproduce $\log p$ with rapidly improving accuracy.

This proxy cannot cover the rational primes. If $t$ is even then $t^2-2>2$ is even. If $t$ is odd and $q$ is prime then $q\equiv7\pmod 8$. Up to $X$, the constraint $p+2=t^2$ supplies at most $O(\sqrt X)$ candidates, hence at most $O(\log X/\sqrt X)$ of the primes. Whether $t^2-2$ is prime infinitely often is itself open and is not assumed here.

Every integer trace $t\ge3$ is actually represented by a primitive modular class. In the free-product code below, the word $1^{t-2}2$ is primitive and is projectively represented by $$\begin{pmatrix}1&1\\0&1\end{pmatrix}^{t-2}
 \begin{pmatrix}1&0\\1&1\end{pmatrix},$$ whose trace is $t$. Therefore the trace scan in Section [6](#sec:experiment){reference-type="ref" reference="sec:experiment"} is a dynamical proxy control, not a scan over impossible traces.

Table [3](#tab:proxyexamples){reference-type="ref" reference="tab:proxyexamples"} shows the trap at the first four prime values.

::: {#tab:proxyexamples}
    $t$   $N=\mathrm{e}^\ell$   $q=t^2-2$           $\log q-\ell$
  ----- --------------------- ----------- -----------------------
      3           6.854101966           7   $2.1063\times10^{-2}$
      5           22.95643924          23   $1.8957\times10^{-3}$
      7           46.97871376          47   $4.5300\times10^{-4}$
      9           78.98733974          79   $1.6027\times10^{-4}$

  : Intrinsic prime proxy $q=t^2-2$. The approximation improves, but $N\ne q$ exactly.
:::

## A trace--norm--proxy trilemma

Three natural relabellings fail in different ways.

1.  The standard norm $N=\mathrm{e}^\ell$ has the desired exponential scale, but Theorem [\[thm:irrational\]](#thm:irrational){reference-type="ref" reference="thm:irrational"} shows that it is never a rational integer.

2.  Setting a prime label equal to the integer trace, $p=t$, permits prime trace values but gives $N\sim t^2$, $\ell\sim2\log p$, and a decay scale $p^{-r}$, not $p^{-r/2}$.

3.  Setting $p=q=t^2-2$ restores an excellent scale approximation but reaches only the sparse family $p+2=t^2$, while retaining composite values and equal-trace multiplicity.

No one of these intrinsic labels gives prime coverage, the correct clock, and the correct exponent simultaneously.

# Selberg, Ruelle, and Weil repetition weights {#sec:weights}

Fix a Fourier convention and sum over primitive oriented hyperbolic conjugacy classes, retaining inversion. The hyperbolic coefficient for the $r$-th repetition is [@Selberg1956; @Hejhal1983; @Stromberg2012; @MageeNaudPuder2022] $$\begin{aligned}
 A^{\rm Sel}_{\gamma,r}
 &=\frac{\ell_\gamma}{2\sinh(r\ell_\gamma/2)} \\
 &=\frac{(\log N_\gamma)N_\gamma^{-r/2}}
 {1-N_\gamma^{-r}}.
 \label{eq:selweight}\end{aligned}$$ The numerator is the *primitive* length, not $r\ell_\gamma$. The repeated length belongs in the denominator and in the test function.

For constant curvature $-1$, the transverse multipliers of the repeated Poincaré map are $\mathrm{e}^{\pm r\ell_\gamma}$, so $$\sqrt{\left|\det(I-\mathcal P_\gamma^r)\right|}
 =2\sinh(r\ell_\gamma/2).
 \label{eq:monodromy}$$ The extra factor $(1-N^{-r})^{-1}$ is therefore exact stability data, not an adjustable normalization. Even the counterfactual substitution $N=p$ would leave $$\frac{A^{\rm Sel}_{\gamma,r}}
 { (\log p)p^{-r/2}}=\frac{1}{1-p^{-r}}.$$

There is a genuine partial repair. With the direct-product conventions $$\begin{aligned}
 Z_\Gamma(s)&=\prod_{\gamma_0}\prod_{m\ge0}
 (1-N_{\gamma_0}^{-s-m}),\\
 R_\Gamma(s)&=\prod_{\gamma_0}(1-N_{\gamma_0}^{-s})
 =\frac{Z_\Gamma(s)}{Z_\Gamma(s+1)},\end{aligned}$$ one obtains [@Fried1986] $$\frac{R_\Gamma'}{R_\Gamma}(s)
 =\sum_{\gamma_0}\sum_{r\ge1}
 (\log N_{\gamma_0})N_{\gamma_0}^{-rs}.
 \label{eq:ruelleweight}$$ At $\Re s=1/2$, this has the desired amplitude shape. It does not repair the disjoint support in Corollary [\[cor:support\]](#cor:support){reference-type="ref" reference="cor:support"}, equal-length multiplicities, or the fact that Pollicott--Ruelle resonances are not generally the real spectrum of a fixed self-adjoint operator. The Ruelle quotient is a legitimate next-stage clue, not a Stage-1 survivor by itself.

The modular surface also has cusp, elliptic, parabolic, Eisenstein, and scattering contributions in its complete trace formula [@Hejhal1983; @LuoSarnak1995]. Its spectral counting in the Laplace parameter is quadratic, whereas the Riemann-zero count is of order $T\log T$. Exactness for the Selberg divisor cannot be rebranded as exactness for the Riemann divisor.

# Zero-free computational audit {#sec:experiment}

## Symbolic convention

We use the free-product presentation $$\operatorname{PSL}_2(\mathbb{Z})=\langle S,R\mid S^2=R^3=1\rangle,
 \quad
 S=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad
 R=\begin{pmatrix}0&-1\\1&1\end{pmatrix}.$$ A cyclically reduced hyperbolic class has a representative $$SR^{e_1}SR^{e_2}\cdots SR^{e_m},\qquad e_j\in\{1,2\}.$$ We reject words that are proper powers and quotient cyclic rotations. Inversion is $(e_1,\ldots,e_m)\mapsto(3-e_m,\ldots,3-e_1)$. It is *retained* in the main ledger, matching the oriented conjugacy/flow convention; a separate inversion quotient is reported as a diagnostic.

The cutoff $m\le16$ is an $S$--$R$ block cutoff. It is not a geometric length cutoff. Consequently, equal-trace counts are lower bounds within the block cutoff, not complete class-number multiplicities. For example, a longer block word can have a trace already present in the ledger.

## Two-phase leakage barrier

Phase 1 uses only group generators and exact integer matrices. It writes the orbit ledger and a manifest containing SHA-256 hashes of the ledger, growth table, code, and frozen protocol. Phase 2 refuses to run if the ledger hash changes; only then does it generate rational primes for declared controls. This is a local reproducibility freeze, not an immutable third-party preregistration. No Riemann-zero table, `zetazero` call, fitted clock, or fitted arithmetic weight is used in either phase.

## Results

The main run produced 8,798 primitive oriented classes and 4,517 classes after quotienting inversion. There are 236 self-reverse classes, verifying $$8798=2\cdot4517-236.$$ The ledger contains 1,020 distinct traces. The largest trace multiplicity *within this cutoff* is 36; it is not a complete multiplicity theorem. Ten unit tests and six run-time invariants check the group relations, primitivity, orientation quotient, inverse pairing, determinant one, and hyperbolicity.

For repetitions $1\le r\le5$, the direct $\ell/[2\sinh(r\ell/2)]$ evaluation and the independent exponential form in Eq. [\[eq:selweight\]](#eq:selweight){reference-type="eqref" reference="eq:selweight"} agree to a maximum absolute ratio residual of $4.44\times10^{-16}$. The theorem-level counts of exact rational-norm hits and prime-power support collisions are both zero; these values come from Theorem [\[thm:irrational\]](#thm:irrational){reference-type="ref" reference="thm:irrational"}, not from floating-point equality tests.

The separate proxy scan uses every integer trace $3\le t\le5000$, hence $q\le24{,}999{,}998$. Among the 1,565,927 primes in this range, 639 have the form $t^2-2$, an observed fraction $4.08065\times10^{-4}$. A regression of $\log(\log q-\ell)$ on $\log N$ gives slope $-1.9999589$, agreeing with the exact asymptotic slope $-2$ in Eq. [\[eq:proxyerror\]](#eq:proxyerror){reference-type="eqref" reference="eq:proxyerror"}. This is a sanity check that demonstrates how a false positive strengthens with orbit length.

# Deninger's arithmetic packets {#sec:deninger}

For a normal finite-type arithmetic scheme, Deninger constructs a topological $\mathbb{R}$-dynamical system using rational Witt spaces and Frobenius maps [@Deninger2026]. For $X_0=\operatorname{Spec}\mathbb{Z}$, after explicitly freezing the allowed finite-kernel admissibility condition, which we denote by $\mathcal E_{\rm fin}$, the system has the form $$X_{0,\mathcal E}=
 \bigl(\check X_0(\mathbb C)_{\mathcal E}\times\mathbb{R}_{>0}\bigr)/\mathbb{Q}_{>0},
 \qquad
 \phi^t[P,u]=[P,\mathrm{e}^t u].
 \label{eq:denflow}$$ The periodic set decomposes as $$\operatorname{Per}(X_{0,\mathcal E})=\coprod_{p}\Gamma_p,
 \label{eq:packets}$$ where each $\Gamma_p$ is a compact packet of periodic orbits of period $\log p$, packets are disjoint, and every periodic orbit belongs to a closed point packet [@Deninger2023; @Deninger2026]. This is a theorem-level arithmetic origin: neither the prime label nor the clock is fitted.

The same source states the essential limitation. A closed point corresponds not to one periodic orbit but to a compact packet. The following are therefore distinct evidence statuses:

  -------------------------------------------- ----------------
  packet decomposition and exhaustion                  `PROVED`
  period $\log p$ and repetitions $r\log p$            `PROVED`
  unique individual orbit per rational prime          `REFUTED`
  canonical packet multiplicity/measure                  `OPEN`
  smooth transverse monodromy                    `NOT_TESTABLE`
  trace-derived packet phase and weight                  `OPEN`
  -------------------------------------------- ----------------

This calibration yields $$\texttt{A0\_ANALYTIC\_ARITHMETIC\_ORIGIN}
 \quad+\quad
 \texttt{A1\_WEAK}.$$ Declaring each packet to count once in an Euler product would reproduce the desired indexing, but without a canonical transverse measure or trace it would be a manual collapse of the very multiplicity problem under study. The raw unrestricted rational-Witt space is also not an acceptable rescue: Deninger explicitly notes that it has too many periodic orbits because its multiplicative data do not encode enough addition. The admissibility choice is therefore disclosed rather than hidden.

The smallest next positive problem is precise: construct on $\Gamma_p/\mathbb{R}$ a functorial canonical measure, or an appropriate groupoid or Lefschetz trace, and prove that the whole packet contributes exactly one intrinsic repetition weight. It must also explain phase and stability rather than inserting $(\log p)p^{-r/2}$ by definition.

# Adversarial controls and generic false positives

## Prime-orbit counting proves too much

For broad classes of topologically weak-mixing Axiom-A flows, primitive orbit counts satisfy $$\#\{\gamma:T_\gamma\le T\}\sim\frac{\mathrm{e}^{hT}}{hT}
 \label{eq:primeorbit}$$ [@ParryPollicott1983]. After the variable change $x=\mathrm{e}^{hT}$, this looks like $x/\log x$. Compact negatively curved surfaces and non-arithmetic suspensions can therefore reproduce the main counting shape without any rational-prime dictionary. Sorted-by-rank agreement is likewise expected to improve asymptotically. Counting shape is an A1 statistic, not A0 evidence.

The general Anosov architecture is mathematically strong [@Anosov1967; @Ruelle1976; @GLP2013; @DyatlovZworski2016]. That strength makes it a particularly important negative control: meromorphic zeta continuation, primitive cycles, and resonances cannot by themselves identify rational primes.

## Constant-roof suspensions

Let a map have a primitive cycle of discrete period $n$, and suspend it with a fixed roof $\tau>0$. The flow period is $n\tau$.

A fixed constant roof can equal $\log p$ for at most one distinct rational prime across all integer cycle periods.

If $n_p\tau=\log p$ and $n_q\tau=\log q$ for distinct primes, then $p^{n_q}=q^{n_p}$, contradicting unique factorization.

This applies equally to a Hénon, cat-map, or symbolic suspension. A variable roof is a different candidate. Assigning its orbit sums to $\log p$ by hand would fail A0 immediately.

## Unregularized $xp$

For $H=xp$, Hamilton's equations give $$x(t)=x_0\mathrm{e}^t,\qquad p(t)=p_0\mathrm{e}^{-t}.$$ Apart from the equilibrium at the origin, the frozen real flow has no nontrivial periodic orbit. Phase-space cutoffs or boundary identifications can recover a smooth counting heuristic, but each is a new model and clock. The unregularized object therefore receives `A1_FAIL`, consistent with the speculative status of the original proposal [@BerryKeating1999].

# What carries over from the prior Logistic--Hénon line? {#sec:prior}

The prior work is useful when read as a source of exact geometry and negative controls, not as an already established prime/zero isomorphism.

#### One-dimensional symbolic line.

The published Logistic/prime-sieve paper labels its central isomorphism a conjecture [@Wang2026Prime]. Its twin-prime-constant experiment sets a coupling using that target constant before reporting recovery, so it is a circular calibration, not an independent A0 result. The subsequent topology paper supplies valuable explicit MSS defects and a Parity--Gap implication [@Wang2026Bounds]; it also documents that the one-dimensional model loses mod-3 dependence and greatly overproduces adjacent gap-2 events. Our audit found that a printed even-gap proof reverses the stated kneading-order comparison, so its dependent decay claim is not used here. The reliable inheritance is the no-go lesson: a parity skeleton does not automatically carry the full residue memory required by primes.

#### Sequential averages.

The sequential Birkhoff result is conditional on uniform inducing and spectral-stability hypotheses [@Wang2026Birkhoff]. Its own scope statement notes that an ordinary Birkhoff average inherits a constant cylinder frequency rather than generating a $1/\log n$ envelope. It supplies neither a primitive closed-orbit ledger nor a returning autonomous clock.

#### Non-autonomous spectral fitting.

The non-autonomous Logistic spectral experiment chooses scale and couplings using target zeros [@Wang2026Logistic]. More basically, its central operator is a time average $T^{-1}\sum_tP_t$, not the time-ordered cocycle $P_T\cdots P_1$. Averaging erases return words and monodromy products and cannot substitute for an orbit trace.

#### Hénon geometry.

The area-preserving map $$F_a(x,y)=(1-ax^2-y,x)
 \label{eq:henon}$$ has $\det DF_a=1$ and is reversible under $(x,y)\mapsto(y,x)$ [@Wang2026Henon]. It also has the exact type-I generating function $$S(q,Q)=qQ-q+\frac{a}{3}q^3,
 \label{eq:gfunction}$$ because $p=-\partial_qS=1-aq^2-Q$ and $P=\partial_QS=q$. Hence a periodic cycle has an intrinsic discrete action $\sum_jS(q_j,q_{j+1})$ and monodromy $\prod_jDF_a(z_j)$. This exact conservative geometry is worth retaining.

What does not carry over is arithmetic. The prior continuum Hamiltonian is a finite-difference approximation with an added confining term, not an exact flow lift. Its spectral parameters were optimized on target zeros without a sealed holdout, and no semiconjugacy proves that Logistic prime coding survives in the Hénon map. A mapping-torus or kicked-Hamiltonian realization can faithfully inherit periods, actions, and monodromy; with a constant roof it is still ruled out arithmetically by the lemma above.

#### Finite-compression benchmark.

The project-provided 2026 manuscript on a Weil finite compression is only days old at the cutoff date, so we treat it as a provisional, not community-settled, result [@Claude2026]. Its useful structural standard is independent of its headline constants: the *same* Hermitian compression should be readable from the prime-power and spectral sides, with trace, second moment, rank, and inertia derived rather than fitted. A flow candidate should eventually produce the analogue of $$\sum_{p,r\ge1}(\log p)p^{-r/2}\delta_{r\log p}$$ from its own primitive/repetition ledger. No Stage-1 candidate does so.

# Route-A outcome

Table [4](#tab:outcome){reference-type="ref" reference="tab:outcome"} gives the calibrated decision. A later analytic or quantum strength cannot bypass an earlier arithmetic failure.

::: {#tab:outcome}
  Candidate            A0                                                           A1                                                         Overall use
  -------------------- ------------------------------------------------------------ ---------------------------------------------------------- ----------------------------------------------------------------------------
  `DEN-WITT-Z-FIN`     analytic arithmetic origin                                   weak: compact packets, no canonical isolated-orbit trace   `ROUTE_A_EXPLORATORY`
  `MOD-GEO`            weak arithmetic relation; rational-prime mechanism refuted   analytic pass                                              rejected as rational-prime HP candidate; retained as exact trace benchmark
  `COMPACT-GEO`        fail                                                         analytic pass (class level)                                proves-too-much control
  `CONTACT-ANOSOV`     fail                                                         analytic pass (class level)                                zeta/resonance control
  `HENON-SUSP`         fail                                                         weak at mixed-regime parameters                            geometry-only control
  `HYP-BILLIARD`       fail generically                                             not numerically testable until geometry is frozen          semiclassical control
  `BERRY-KEATING-XP`   fail                                                         fail                                                       rejected frozen object

  : Stage-1 obligation matrix. Later-layer entries are scoped architectural observations, not completed downstream stages.
:::

The decisive statement is not that continuous flows are impossible. It is that none of the frozen candidates simultaneously reaches a pass-level arithmetic gate and a pass-level isolated-orbit gate. Invoking a quantum operator search now would bypass the identified missing interface, so Route B is not authorized by this result.

# Limitations and next tests

The modular theorem concerns the standard arc-length clock on the modular surface. It does not exclude a different arithmetic flow, a nontrivial extension, or a newly justified time change. Any such modification must be frozen as a new object and cannot inherit the verdict automatically.

The finite modular ledger is complete only by symbolic block cutoff. It is not complete below its largest recorded geometric length, and its equal-trace multiplicities are lower bounds. The exact irrationality and support results do not depend on this ledger.

Deninger's global admissibility condition is not uniquely forced by current theory. We selected an explicitly permitted finite-kernel condition so that the candidate is testable and disclosed the choice. A result depending on a different condition requires versioned reevaluation.

Our literature review is targeted rather than exhaustive. Seventeen external mathematical sources were retained for direct theorem/identity support, and the six project papers were audited separately. DOI and venue metadata were checked against Crossref and publisher or journal pages. The Semantic Scholar batch endpoint returned HTTP 429 at the verification date; this degraded source was not treated as evidence. The local PDFs were readable and unencrypted, but a full `pypdf` preflight was unavailable, so physical page citations in the audit notes are advisory rather than a claim of complete PDF-object integrity.

The next tests, in increasing scope, are:

1.  seek a canonical, functorial measure or trace on each Deninger packet;

2.  derive repetition weight, sign, and phase from that same object;

3.  only if those succeed, test whether a packet-level dynamical zeta has a controlled divisor without inserting the arithmetic Euler product by hand;

4.  retain the modular Selberg/Ruelle ledger as the calibration standard for monodromy, orientation, repetitions, and extra spectral terms.

# Conclusion

The Stage-1 question has a definite outcome. Deninger's arithmetic flow derives $\log p$ periods but at compact-packet level; the modular geodesic flow derives isolated primitive orbits and exact trace weights but its norm and every power of that norm are irrational. The apparent bridge $\operatorname{tr}(\gamma^2)=t^2-2$ is especially instructive: it can make period and amplitude comparisons numerically excellent while covering only a sparse prime proxy and never changing the exact orbit norm.

This two-halves diagnosis narrows the research programme. The next genuine advance is not a better zero fit or another generic-chaos statistic. It is a mathematical interface that turns intrinsic arithmetic packets into a canonical trace contribution while preserving their arithmetic clock. Until that interface is constructed, the modular flow should be used as an exact calibration benchmark and the arithmetic flow as an exploratory A0 survivor, not as a completed Hilbert--Pólya system.

# Reproducibility and declarations {#reproducibility-and-declarations .unnumbered}

The complete source, tests, ledgers, checksums, evaluations, and audit notes are included in the Stage-1 project directory. From the `experiments/` directory, the run command is

    bash reproduce.sh

using Python 3.10.12. The manuscript is built from `paper/` with

    latexmk -pdf -interaction=nonstopmode -halt-on-error manuscript.tex

No human participants, personal data, or intervention are involved. The author declares no conflict of interest. Literature triage, computational implementation, and adversarial auditing were assisted by OpenAI Codex; the author remains responsible for the claims, source selection, and final text.

# Artifact map

  Relative path   Purpose
  --------------- ----------------------------------------------------------------------------------------------------------
  Relative path   Purpose
                  research question, source locks, preregistered tests, validity criteria, and Devil's Advocate checkpoint
                  targeted search method, evidence map, and synthesis
                  DOI/venue verification and degraded-source disclosure
                  exact proofs, proxy trap, and suspension obstruction
                  page-located inheritance and integrity audit of the six project PDFs
                  A0--A1 obligation matrix and decision boundary
                  two-phase deterministic enumeration and arithmetic audit
                  ten unit tests
                  local freeze hashes, cutoff, orientation, and completeness boundary
                  primitive oriented classes and exact matrix invariants
                  repetitions and amplitude comparisons
                  machine-readable headline results and data boundary
                  exact Route-A YAML verdicts for the two serious candidates
