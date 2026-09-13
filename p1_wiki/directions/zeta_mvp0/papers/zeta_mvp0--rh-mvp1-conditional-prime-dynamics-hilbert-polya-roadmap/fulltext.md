---
p1_kind: "derived-fulltext-reading-copy"
route: "zeta_mvp0"
logical_paper_id: "zeta_mvp0--rh-mvp1-conditional-prime-dynamics-hilbert-polya-roadmap"
canonical_tex: "zeta_mvp0/papers/RH-MVP1-conditional-prime-dynamics-hilbert-polya-roadmap/main.tex"
canonical_pdf: "zeta_mvp0/papers/RH-MVP1-conditional-prime-dynamics-hilbert-polya-roadmap/main.pdf"
source_sha256: "b9451acd42136ab1d705a72401d5edbdc5f1ce45fea1ce76e7732664240b21e8"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Prime Dynamics Program, Volume I Foundations and a Conditional Hilbert--Polya Architecture RH-1--RH-160, Five Bold Interfaces, and a Conditional Spectral-Divisor Closure Theorem

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../zeta_mvp0/papers/RH-MVP1-conditional-prime-dynamics-hilbert-polya-roadmap>)
- [规范 TeX](<../../../../../zeta_mvp0/papers/RH-MVP1-conditional-prime-dynamics-hilbert-polya-roadmap/main.tex>)
- [关联 PDF](<../../../../../zeta_mvp0/papers/RH-MVP1-conditional-prime-dynamics-hilbert-polya-roadmap/main.pdf>)
- [支撑 Markdown](<../../../../../zeta_mvp0/papers/RH-MVP1-conditional-prime-dynamics-hilbert-polya-roadmap/README.md>)
- [BibTeX](<../../../../../zeta_mvp0/papers/RH-MVP1-conditional-prime-dynamics-hilbert-polya-roadmap/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  This first volume of a four-volume synthesis compresses one hundred and sixty RH-numbered papers that developed the prime-dynamics program from its original symbolic analogy into a collection of exact theorems, validated finite models, conditional all-level compositions, and sharp negative results. The volume of local work now obscures the global question: what is the shortest honest chain from the existing dynamical foundation to a Hilbert--Polya conclusion?

  We give a deliberately bold minimum viable proof architecture. Its rigorous foundation $F$ consists of the corrected sieve--kneading coordinate, parity-resolved deterministic trace geometry, the fixed-noise intrinsic regularized determinant, continuum bridges, and finite certification technology. Five additional interfaces are stated as hypotheses, not results: $A$, a canonical all-level pole-renormalized determinant; $B$, an order-sensitive canonical scattering completion; $C$, a self-adjoint generator with an intrinsic Riemann--von Mangoldt counting law; $D$, a target-independent prime-power trace formula with von Mangoldt weights; and $E$, a no-missing/no-spurious spectral-divisor completeness theorem.

  The analytic closure step is elementary but decisive. Write $\Xi(z)=\xi(\tfrac12+iz)$. If the self-adjoint determinant $D_H$ produced by $A$--$C$ and the arithmetic identity $D$--$E$ give $$\frac{D_H'(z)}{D_H(z)}=\frac{\Xi'(z)}{\Xi(z)}$$ on one nonempty pole-free domain, with one normalization value, then analytic continuation gives $D_H=\Xi$. Since zeros of a self-adjoint spectral determinant are real, every nontrivial zeta zero lies on the critical line. This is a conditional implication, not a proof that any of $A$--$E$ holds.

  An automated audit finds RH-1 through RH-160 exactly once, each with source and a PDF; 131 machine-readable verification archives expose 1,717 declared publication hashes, all of which match. It also records nine shortcuts already ruled out by the program. The unique architecture-relative proof debt is $\{A,B,C,D,E\}$; the immediate frontier is still $A$. The result is therefore a compact, falsifiable research contract for subsequent careful papers, not an unconditional Stage A, Hilbert--Polya operator, zeta identity, or proof of the Riemann Hypothesis.
author:
- Liang Wang
bibliography:
- references.bib
date: July 2026
title: |
  **Prime Dynamics Program, Volume I**\
  Foundations and a Conditional Hilbert--Polya Architecture\
  RH-1--RH-160, Five Bold Interfaces, and a Conditional Spectral-Divisor Closure Theorem
```

## Markdown 正文

**Keywords:** Hilbert--Polya program; transfer operator; regularized determinant; scattering; explicit formula; research roadmap; validated numerics.

# The four-volume series and the boundary of Volume I

The numbered corpus remains the atomic source of mathematical claims. The four synthesis volumes reorganize those sources by function; they do not concatenate proofs, change theorem status, or create a new numbered result. The partition is

   volume  source range     role
  -------- ---------------- ---------------------------------------------------------------------------------------------------------------------
     I     RH-1--RH-160     symbolic and fixed-noise foundations, finite certification, reset architecture, and the conditional interfaces A--E
     II    RH-161--RH-241   packet-to-Riesz assembly, temporal clouds, relative determinants, and the moving trace-envelope frontier
    III    RH-242--RH-281   deterministic numerator anchors, selectors, analytic tails, and counterloops
     IV    RH-282--RH-361   noisy heads, annular endpoints, first alias, and signed completion

Volume I stops at RH-160. RH-161 is an independent typed assembly theorem and is the first source of Volume II. Later volumes may sharpen the location of the active frontier, but they do not retroactively prove any of the five interfaces formulated here. In particular, the series organization carries no Gate A--E promotion.

# Purpose: replace 160 local layers by one research contract

The original project began with a numerical and symbolic correspondence between cumulative sieve words and a quadratic map. RH-1 made the first essential correction: ordered convergence to a kneading coordinate is unconditional, whereas universal finite-stage admissibility is false and equality of one itinerary does not imply topological conjugacy [@WangRH1; @WangPublished]. The subsequent sequence did not repair the old word "isomorphism" by rhetoric. It changed the object.

The durable spectral object is a nonselfadjoint, parity-renormalized transfer determinant. At fixed positive noise it is intrinsic and has rigorous continuum limits; its deterministic small-noise geometry contains genuine bulk poles. The noisy Markov operator itself is irreversible and cannot be declared to be a Hilbert--Polya operator [@WangRH7; @WangRH45]. Later papers developed directional Hardy/Stein bounds, packet reductions, outward-rounded certificates, correlated support cocycles, and spectral resets [@WangRH50; @WangRH100; @WangRH149; @WangRH160].

This paper intentionally changes altitude. It does not add a finer packet estimate. Instead it asks for the smallest chain of mathematical interfaces which, if proved in later papers, would turn the existing foundation into a complete spectral realization. "MVP" means *minimum viable proof*, not minimum numerical resemblance.

Three rules govern the synthesis.

1.  A finite certificate never becomes an eventual theorem by repetition.

2.  A conditional composition never proves its physical hypotheses.

3.  No zero ordinate, fitted map to height, or target spectral list may be inserted into the construction that is supposed to explain that list.

Throughout, *proved* means an analytic theorem in its stated scope, *certified* means a finite outward or exact-stored computation, *conditional* means a valid implication whose physical hypotheses are still open, and *open* means that even the required implication has not yet been constructed. A no-go result rejects only the route named in its statement. These labels are not interchangeable, and the audit never promotes one by numerical repetition.

# What the 160 layers actually established

Table [1](#tab:phases){reference-type="ref" reference="tab:phases"} compresses the sequence by mathematical function. The endpoints are not equal in logical strength: an analytic theorem, an exact stored-matrix certificate, floating evidence, a conditional theorem, and a no-go are different output types.

::: {#tab:phases}
    layers   phase                              durable conclusion and boundary
  ---------- ---------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
     1--3    symbolic foundation                ordered sieve--kneading convergence, inverse prime realization, and parity geometry; no natural topological conjugacy
    4--15    determinant hygiene                continuum response, irreversible $\det_2$, ordered traces, deterministic flat traces, postcritical zeta factors, and genuine bulk poles; no self-adjoint interpretation
    16--45   packet, Feshbach, validation       critical-branch packets, complete finite contour certificates, dyadic continuum bridges, and fixed-noise intrinsic determinant convergence; no zero-noise determinant theorem
    46--71   small-noise directional control    pole obstruction, directional Hardy--Stein reduction, phase-aware finite horizons, and a closed frozen production chain; family-uniform all-level control remains open
   72--100   Stage-A alternatives               validated assembly, effective-rank and Schur packet corridors, moving-cloud relative determinant target, and an audited completion frontier; Stage A and A5 remain unproved
   101--129  exterior support and recurrence    finite memory actions, fourth-cross/exterior support, adaptive certificates, and sharp conditional eventual-support theorems; physical all-level recurrence is absent
   130--149  gauge, viability, source closure   floor-free semidefinite theory, moving-frame tail recurrences, outward finite composition, source enclosures, and an inclusion-minimal three-interface conditional route
   150--160  reset dichotomy                    independent spectral resets, coherent transitions, a finite native support floor, exact contemporaneous-cross cancellation, complete lag-$\leq8$ finite cross closure, and a conditional all-level native/directional theorem

  : A functional compression of RH-1--RH-160.
:::

The strongest current all-level statement is RH-160's implication. Eventual overlap conditioning, weak-eigenvalue/tail separation, and selected spectral spread imply a uniform native floor; adding a bounded-lag fourth-cross law gives a directional seed. Every clause passes on the five frozen scales, but no clause is proved eventually. The gap between "120/120" and "all sufficiently large levels" is precisely the first macro interface below.

## Negative knowledge is part of the result

The sequence has closed several attractive shortcuts. They must not reappear inside an optimistic roadmap under new names:

1.  one shared kneading word does not give topological conjugacy (RH-1);

2.  the irreversible noisy Markov operator is not directly self-adjoint under a positive stationary weight (RH-7);

3.  $AB$ and $BA$ spectra do not record temporal orientation (RH-8);

4.  a plain entire small-noise determinant cannot cross the genuine deterministic poles without renormalization (RH-15, RH-46);

5.  noise-uniform fixed-step global complement contraction is impossible (RH-50);

6.  finite-anchor regression cannot prove an eventual scale law (RH-117);

7.  independent interval balls can destroy positivity retained by a correlated congruence (RH-153);

8.  a contemporaneous full-memory spectral reset sees only negative tail coupling in its recent cross action (RH-157);

9.  inverse prime encoding is not a target-independent von Mangoldt trace formula (RH-1--2).

These no-go results do not weaken the MVP. They make its interfaces narrow enough to be meaningful.

# The minimum viable objects

Let $$\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
 \qquad \Xi(z)=\xi\!\left(\frac12+iz\right).$$ The function $\Xi$ is entire and even, and the Riemann Hypothesis is equivalent to all its zeros being real [@Titchmarsh1986]. This notation is used only to state the target and to verify the final identity; $\Xi$ and its zero set are forbidden inputs to interfaces $A$--$D$.

The existing finite/noisy family will be denoted schematically by $K_{n,\sigma}$, after Perron/parity removal and the time-ordering required by the quadratic dynamics. Its exact implementation may evolve. The MVP requires only that each interface produce a canonical output for the next. Regularized determinant statements use the standard trace-ideal convention [@Simon2005]; a canonical-system realization is one possible, but not presupposed, implementation of the self-adjoint gate [@deBranges1968].

$F$ is the conjunction of results already proved in their stated scopes: the corrected symbolic coordinate and parity factor, intrinsic fixed-noise regularized traces/determinants, deterministic pole structure, continuum and finite-section bridges, and the finite certification toolkit. It does not include an eventual small-noise theorem.

The foundation is useful even if every later interface fails. It supports a standalone theory of nonselfadjoint transfer spectra.

# Five bold interfaces

The following are deliberately stronger than the presently proved results. They are hypotheses with exact success and failure tests.

## $A$: canonical all-level intrinsic determinant

There exist an admissible joint schedule $(n,\sigma)\to(\infty,0)$, an exact moving-cloud factor $C_{n,\sigma}$, and a zero-free normalization $Z_{n,\sigma}$ such that $$\mathcal D_{n,\sigma}(z)
 =Z_{n,\sigma}(z)
   \frac{\det{}_2\!\bigl(I-zK_{n,\sigma}^{\rm bulk}\bigr)}
        {C_{n,\sigma}(z)}
 \longrightarrow \mathcal D_{\rm dyn}(z)$$ locally uniformly on compacta after removable cloud zeros have been filled by the exact reducing factorization. Together with the explicitly tracked deterministic pole divisor, this defines the canonical meromorphic dynamical object. The residual limit is not identically zero, is independent of all admissible meshes, packet gauges, reset choices, and cutoffs, and preserves the required directed three/six-step trace data. The use of the actual cloud factor is forced by RH-80's fixed-factor no-go and exact relative determinant algebra [@WangRH80].

RH-160 suggests two possible internal realizations: a minimal native-reset route using the O/E/S interfaces, or a directional route adding bounded lag L. Both still require a typed all-level assembly. Gate $A$ fails if any required running margin tends to zero along an infinite scale sequence, if the normalization is target dependent, or if different admissible schedules give inequivalent limits.

## $B$: canonical order-sensitive scattering completion

The dynamical limit admits a unique, functorial completion to an inner or unitary scattering object $S_{\rm dyn}(z)$. Its determinant is related to $\mathcal D_{\rm dyn}$ by a proved factorization, its boundary values are unitary on a real axis, and its lifted phase retains a nonzero directed temporal trace. It is independent of arbitrary dilations and auxiliary channels.

A generic unitary dilation is insufficient: infinitely many dilations can share one compression while carrying arbitrary extra spectrum. Gate $B$ fails if all canonical completions erase temporal orientation or if uniqueness requires a fitted branch choice.

## $C$: self-adjoint generator and intrinsic counting

There is a canonical self-adjoint operator $H$ (or canonical system) whose scattering/regularized determinant $D_H$ is the completed object from $B$. Its domain, self-adjointness, spectral multiplicities, and completeness are proved. With multiplicity, set $$N_H(T)=\#\{\lambda\in\operatorname{spec}_{\rm disc}(H):0<\lambda\leq T\}.$$ Before using zeta ordinates, one derives from $H$ itself $$N_H(T)=\frac{T}{2\pi}\log\frac{T}{2\pi}
        -\frac{T}{2\pi}+O(\log T).$$ The precise lower-order form may be reached in stages, but the leading $T\log T$ law cannot be manufactured by fitting $T=T(\sigma)$. Gate $C$ fails if the only canonical object has bounded phase, logarithmic-only rank, a power-law Weyl exponent, uncontrolled extra spectrum, or wrong multiplicity.

## $D$: target-independent prime-power trace formula

For a separating test class $\mathcal T$ for which $h(H)$ is trace class, use the Fourier convention $$h(t)=\int_{\mathbb R}g(u)e^{itu}\,du.$$ The trace of $H$ is derived from the dynamics/arithmetic interface in the form $$\operatorname{Tr}h(H)
 =\mathcal W_\infty(h)
 -\sum_{m\ge2}\frac{\Lambda(m)}{\sqrt m}
   \bigl(g(\log m)+g(-\log m)\bigr),
 \qquad h\leftrightarrow g.$$ Here $\mathcal W_\infty$ contains the exactly matched archimedean, pole, and normalization terms. Prime powers and von Mangoldt weights must emerge from a proved transform; no zeta-zero data are permitted. The parallel TPC program may supply arithmetic lemmas only after a theorem matches variables, test functions, weights, and counterterms. A common use of the word "trace" is not an interface.

Gate $D$ fails if the weights have to be inserted by hand, if only primes but not prime powers occur, if the test class is too small to determine a divisor, or if a target-informed inverse parameter supplies the answer.

## $E$: spectral-divisor completeness

The trace identity from $D$, together with the classical explicit formula, is upgraded to an identity of meromorphic logarithmic derivatives on one nonempty common domain: $$\frac{D_H'}{D_H}=\frac{\Xi'}{\Xi}.$$ Every sector of $H$, every gamma/pole term, and every finite normalization is accounted for. A single reference value fixes the zero-free constant. Gate $E$ fails upon any missing or spurious level, hidden entire factor, multiplicity mismatch, or unmatched archimedean term.

Unlike a claim that "the spectra look alike", $E$ is a complete identity with a yes/no verification target. It is deliberately close to the final target and is expected to carry major proof debt; listing it as an interface does not make it plausible or inexpensive.

The arrows $A\to B\to C\to D\to E$ describe functional dependencies, not a license to hide target information upstream. Gates $A$--$D$ may use the sieve, the quadratic dynamics, and previously proved analytic constructions, but not values of $\Xi$ or its zeros. Gate $E$ is the first comparison with the completed zeta function. Finite prototypes of later gates may be run early as falsification tests, but they do not alter this proof order.

# The conditional closure theorem

The difficult work lies in proving $A$--$E$. Once they are available, the last analytic implication is short and rigorous.

[\[thm:closure\]]{#thm:closure label="thm:closure"} Let $H$ be self-adjoint and suppose it has an entire regularized spectral determinant $D_H$ whose zero divisor, with multiplicity, is exactly the discrete spectrum of $H$. Let $U\subset\mathbb C$ be a nonempty connected open set on which $D_H$ and $\Xi$ are nonzero. If $$\frac{D_H'(z)}{D_H(z)}=\frac{\Xi'(z)}{\Xi(z)}
 \qquad(z\in U)$$ and $D_H(z_0)=\Xi(z_0)$ at one $z_0\in U$, then $$D_H(z)=\Xi(z)\qquad(z\in\mathbb C).$$ Consequently every nontrivial zero of $\zeta$ lies on the critical line.

On $U$, the quotient $Q=D_H/\Xi$ obeys $Q'/Q=0$, so it is constant. The normalization gives $Q=1$ on $U$. Hence the entire function $D_H-\Xi$ vanishes on a nonempty open set. The identity theorem gives $D_H=\Xi$ on all of $\mathbb C$.

All zeros of a spectral determinant whose divisor is the spectrum of a self-adjoint operator are real. If $\Xi(z)=0$, then $\rho=\tfrac12+iz$ is a nontrivial zeta zero; real $z$ gives $\operatorname{Re}\rho=\tfrac12$.

[\[cor:mvp\]]{#cor:mvp label="cor:mvp"} Assume foundation $F$ and prove interfaces $A$--$E$ with the compatibility specified above. Then the construction satisfies the hypotheses of Theorem [\[thm:closure\]](#thm:closure){reference-type="ref" reference="thm:closure"}, and the Riemann Hypothesis follows.

$A$ supplies the canonical dynamical determinant, $B$ its canonical order-sensitive completion, and $C$ the self-adjoint determinant $D_H$. $D$ supplies the zero-free arithmetic trace identity without using zeros as input. $E$ proves completeness, upgrades that identity to the logarithmic derivative equality, and fixes normalization. Apply Theorem [\[thm:closure\]](#thm:closure){reference-type="ref" reference="thm:closure"}.

Corollary [\[cor:mvp\]](#cor:mvp){reference-type="ref" reference="cor:mvp"} is not evidence for any premise. In particular, assuming $E$ casually would merely assume the hardest spectral identity. Its value is architectural: every later paper can be judged by whether it proves a named part of $A$--$E$, finds a counterexample, or leaves the debt unchanged.

# Minimal proof debt and route alternatives

Treat the MVP as the monotone dependency formula $$\mathrm{MVP}=F\wedge A\wedge B\wedge C\wedge D\wedge E.$$ A proved leaf contributes no debt; a finite or conditional leaf contributes its name; a no-go leaf kills its branch. AND takes unions and OR takes the inclusion-minimal antichain of alternatives. This elementary recursion was used in earlier route reviews and is re-audited here.

With the statuses established after RH-160, the unique inclusion-minimal completion bundle for the full MVP is $$\boxed{\{A,B,C,D,E\}}.$$ The bundle required to reach a genuine Hilbert--Polya *candidate*, prior to arithmetic identification, is $\{A,B,C\}$. The current first missing gate is $A$.

$F$ is closed in its stated scope. The reset-support subroute inside $A$ has a conditional theorem and finite evidence, but its typed determinant assembly is absent, so $A$ itself is open. Gates $B$--$E$ are also open. The formula is a conjunction, so every nonclosed leaf is required. Removing $D$ or $E$ leaves a self-adjoint but non-arithmetic model; removing $C$ leaves no real spectral axis; removing $B$ leaves no canonical completion; removing $A$ leaves no all-level dynamical object.

This minimality is relative to the present architecture. A future theorem may prove two interfaces simultaneously. It may not silently omit their mathematical functions.

Inside $A$ there are two typed alternatives: $$A_{\rm native}\quad\text{or}\quad A_{\rm lagged}.$$ The native route assumes less and should be tried first if downstream assembly accepts compression support. If four directional images are essential, RH-159 proves that native positivity cannot replace them, and the adaptive-lag route is required. Failure of lagged cross support therefore does not automatically kill the native route.

![The minimum viable architecture, the 160-layer phase ledger, repository audit, and explicit downgrade rules.](<../../../../../zeta_mvp0/papers/RH-MVP1-conditional-prime-dynamics-hilbert-polya-roadmap/figures/conditional_mvp_roadmap.pdf>){#fig:roadmap width="\\textwidth"}

# A coarse but complete execution plan

The purpose of the MVP is to license bold exploration while keeping later verification local. The recommended sequence is:

1.  **Close or kill $A$.** Prove one eventual reset route and a typed all-level moving-cloud quotient assembly. The native O/E/S route is primary; bounded lag L is activated only if the assembly needs directional cross rank.

2.  **Prototype $B$ before polishing $A$ constants.** On the best finite models, search for a normalization-unique inner/scattering completion and test whether the RH-8 directed trace survives. A rigorous no-go here can save many all-level estimates.

3.  **Demand $C$ without ordinate fitting.** Construct the candidate self-adjoint domain and derive its counting law from phase or geometry. If the leading law is not $T\log T$, stop the Hilbert--Polya escalation.

4.  **Build $D$ as an arithmetic transducer.** Start from primitive dynamical traces and derive prime powers, von Mangoldt weights, and archimedean terms on one test class. Use TPC machinery only through an exact crosswalk theorem.

5.  **Prove $E$ last.** Compare logarithmic derivatives, close hidden sectors and zero-free factors, verify multiplicities, and invoke Theorem [\[thm:closure\]](#thm:closure){reference-type="ref" reference="thm:closure"} only after all inputs are independent of zero data.

The ordering is intentionally not "finish every estimate before asking if the next object exists". Cheap finite prototypes of $B$ and $C$ are useful falsification experiments. They do not promote those gates to theorems.

# Stopping rules and publishable downgrade outcomes

Each macro gate has a clean negative outcome.

::: {#tab:stopping}
   gate  decisive failure                                                                                  honest surviving result
  ------ ------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------
   $A$   all admissible all-level routes lose overlap, tail separation, spread, or schedule independence   rigorous nonselfadjoint fixed-noise and finite small-noise transfer-spectrum theory
   $B$   every canonical completion is orientation-blind or nonunique                                      a renormalized dynamical determinant with no Hilbert--Polya escalation
   $C$   no self-adjoint realization, or intrinsic counting differs from $T\log T$                         canonical scattering theory with the wrong spectral universality
   $D$   no target-independent von Mangoldt/prime-power transform                                          a self-adjoint dynamical model that is spectral but not arithmetic
   $E$   missing/spurious levels, hidden factors, or multiplicity mismatch                                 a partial explicit-formula correspondence with no zero-location conclusion

  : Failure does not erase earlier mathematics; it fixes the correct publication level.
:::

These rules are especially important for $C$--$E$. Numerical agreement of the first ordinates cannot compensate for a wrong counting law. A correct counting law cannot compensate for absent prime-power weights. A prime-weight resemblance cannot compensate for missing gamma terms or hidden spectrum.

# Repository audit and reproducibility

The automated audit discovers RH-1 through RH-160 by directory name rather than by a hand-written count. Every integer occurs exactly once. All 160 directories contain a README, a main TeX source, and at least one PDF; 131 contain machine-readable summaries and verification archives, and 156 have test directories. Replaying every declared publication hash in those 131 archives gives 1,717 matches and zero failures. Seventeen milestone inputs from RH-1, each decadal layer through RH-60, and the later route reviews are hashed into the present audit.

This verifies the recorded corpus, not every theorem in 160 papers. The classification still relies on the stated theorem boundaries in the source papers. It does, however, make accidental omission, duplicate numbering, archive drift, and silent promotion of macro gates machine-detectable.

# Claim boundary

RH-MVP1 proves two things: the spectral-divisor closure theorem and a status-aware synthesis of the existing program. It then makes five bold, separately falsifiable assumptions to show what a complete route would look like.

It does *not* prove the eventual reset interfaces, a joint small-noise determinant, a canonical scattering completion, a self-adjoint generator, a $T\log T$ counting law, a von Mangoldt trace formula, a completed-zeta determinant identity, or the Riemann Hypothesis. The current unconditional claim level remains the rigorous dynamical/fixed-noise spectral foundation.

The optimistic conclusion is nevertheless concrete. The maze no longer needs 160 simultaneous labels. It has five doors: $$\boxed{A\longrightarrow B\longrightarrow C\longrightarrow D\longrightarrow E.}$$ Later papers may carefully prove them, replace one with a genuinely stronger construction, or close the route by a no-go. Until then, the diagram is a research contract, not a theorem about zeta zeros.

# Atomic source index

The following machine-generated index lists every canonical numbered source in Volume I. It is a provenance locator, not a claim that all entries have the same theorem status.

    source canonical directory
  -------- -------------------------------------------------------------
    source canonical directory
      RH-1 `RH-1-rigorous-sieve-kneading-reformulation`
      RH-2 `RH-2-exact-prime-kneading-spectral-stability`
      RH-3 `RH-3-parity-resolved-band-merging-spectrum`
      RH-4 `RH-4-spectral-obstructions-renormalized-limits`
      RH-5 `RH-5-renormalized-gaussian-response`
      RH-6 `RH-6-continuum-spectral-double-limits`
      RH-7 `RH-7-irreversible-gaussian-cycle-spectrum`
      RH-8 `RH-8-time-ordered-cycle-curvature`
      RH-9 `RH-9-small-noise-cycle-localization`
     RH-10 `RH-10-parity-renormalized-long-cycle-determinant`
     RH-11 `RH-11-collet-eckmann-flat-trace-completion`
     RH-12 `RH-12-postcritical-weighted-zeta-factorization`
     RH-13 `RH-13-validated-reduced-sector-spectral-gap`
     RH-14 `RH-14-square-root-parity-boundary-layer`
     RH-15 `RH-15-parity-extracted-bulk-scattering`
     RH-16 `RH-16-endpoint-gaussian-resolution-rank`
     RH-17 `RH-17-time-ordered-boundary-monodromy`
     RH-18 `RH-18-branch-isolated-gaussian-return`
     RH-19 `RH-19-complement-excursion-self-energy`
     RH-20 `RH-20-sector-resolved-critical-branches`
     RH-21 `RH-21-peripheral-biorthogonal-branch-collapse`
     RH-22 `RH-22-dark-channel-schur-self-energy`
     RH-23 `RH-23-physical-packet-complement-feshbach`
     RH-24 `RH-24-contour-feshbach-root-count`
     RH-25 `RH-25-directional-rouche-closure`
     RH-26 `RH-26-primal-dual-directional-certificate`
     RH-27 `RH-27-outward-rounded-primal-dual-residuals`
     RH-28 `RH-28-arcwise-rational-arnoldi-enclosure`
     RH-29 `RH-29-deflated-complement-resolvent`
     RH-30 `RH-30-sparse-two-step-grushin-inverse`
     RH-31 `RH-31-sparse-threshold-inertia`
     RH-32 `RH-32-end-to-end-certificate-ledger`
     RH-33 `RH-33-certified-complement-resolvent-atlas`
     RH-34 `RH-34-interior-complement-pole-count`
     RH-35 `RH-35-exact-packet-pair-physical-count`
     RH-36 `RH-36-nested-grid-physical-count`
     RH-37 `RH-37-iterated-dyadic-physical-count`
     RH-38 `RH-38-dyadic-haar-block-decay`
     RH-39 `RH-39-uniform-gaussian-cutoff-bridge`
     RH-40 `RH-40-weighted-riesz-projector-bridge`
     RH-41 `RH-41-validated-parity-continuum-contour`
     RH-42 `RH-42-uniform-euclidean-parity-contour`
     RH-43 `RH-43-validated-weighted-riesz-parity-kernel`
     RH-44 `RH-44-validated-rank-two-peripheral-complement`
     RH-45 `RH-45-bulk-two-step-trace-norm-determinant`
     RH-46 `RH-46-small-noise-mesh-double-pole`
     RH-47 `RH-47-logarithmic-peripheral-conditioning`
     RH-48 `RH-48-intrinsic-riesz-identification`
     RH-49 `RH-49-directional-reduced-resolvent`
     RH-50 `RH-50-two-pole-hilbert-schmidt-hardy`
     RH-51 `RH-51-cyclic-rank-growing-horizon-stein`
     RH-52 `RH-52-intrinsic-peripheral-residue-transfer`
     RH-53 `RH-53-deterministic-hardy-tail-cutoff`
     RH-54 `RH-54-factor-aware-intrinsic-identification`
     RH-55 `RH-55-strong-weak-riesz-cutoff-transfer`
     RH-56 `RH-56-growing-horizon-hard-space-barrier`
     RH-57 `RH-57-mixed-haar-channel-overlap-budget`
     RH-58 `RH-58-time-ordered-schur-cross-gramian`
     RH-59 `RH-59-flag-adapted-schur-stein-metrics`
     RH-60 `RH-60-finite-horizon-phase-aware-tails`
     RH-61 `RH-61-directional-horizon-scaling-barrier`
     RH-62 `RH-62-krylov-residual-stein-tails`
     RH-63 `RH-63-nested-krylov-residual-closure`
     RH-64 `RH-64-weighted-terminal-residuals`
     RH-65 `RH-65-physical-family-metric-conditioning`
     RH-66 `RH-66-block-cross-column-krylov-gram`
     RH-67 `RH-67-physical-covariance-block-envelopes`
     RH-68 `RH-68-phase-coherence-block-depth-barrier`
     RH-69 `RH-69-adaptive-certificate-portfolio`
     RH-70 `RH-70-frozen-production-block-hardy-audit`
     RH-71 `RH-71-directional-tail-route-review`
     RH-72 `RH-72-validated-folded-gaussian-assembly`
     RH-73 `RH-73-validated-peripheral-rank-two-deflation`
     RH-74 `RH-74-validated-upstream-hardy-bridge`
     RH-75 `RH-75-log-square-block-contraction-law`
     RH-76 `RH-76-single-arc-phase-compression-barrier`
     RH-77 `RH-77-postblock-effective-rank-compression`
     RH-78 `RH-78-two-corridor-stage-A1-composition`
     RH-79 `RH-79-intrinsic-determinant-diagonal-transfer`
     RH-80 `RH-80-moving-cloud-relative-determinant`
     RH-81 `RH-81-stage-A-to-A5-route-review`
     RH-82 `RH-82-half-log-postblock-rank-clock`
     RH-83 `RH-83-optimal-endpoint-singular-factorization`
     RH-84 `RH-84-ky-fan-tail-majorization`
     RH-85 `RH-85-midblock-snapshot-packets`
     RH-86 `RH-86-trace-normalized-late-memory-packets`
     RH-87 `RH-87-rayleigh-injection-recursion`
     RH-88 `RH-88-predictor-corrector-energy-contraction`
     RH-89 `RH-89-rank-one-complement-ritz-correction`
     RH-90 `RH-90-schur-secular-subquarter-certificate`
     RH-91 `RH-91-schur-packet-route-review`
     RH-92 `RH-92-block-schur-contraction-budgets`
     RH-93 `RH-93-two-direction-recursive-ritz-refresh`
     RH-94 `RH-94-source-seeded-four-direction-horizon-refresh`
     RH-95 `RH-95-reduced-projected-cross-moment-factorization`
     RH-96 `RH-96-gap-weighted-weak-mode-quotient`
     RH-97 `RH-97-nonlinear-hybrid-horizon-budget`
     RH-98 `RH-98-projector-lipschitz-propagation-barrier`
     RH-99 `RH-99-two-gap-differential-ritz-envelope`
    RH-100 `RH-100-hundred-layer-route-review`
    RH-101 `RH-101-finite-memory-packet-gram-action`
    RH-102 `RH-102-stopped-hybrid-quotient-clock`
    RH-103 `RH-103-prefix-observability-power-ledger`
    RH-104 `RH-104-source-weighted-prefix-law`
    RH-105 `RH-105-observation-residual-cancellation-law`
    RH-106 `RH-106-uniform-gap-aware-quotient-law`
    RH-107 `RH-107-source-seeded-quotient-support-law`
    RH-108 `RH-108-finite-memory-fourth-cross-support`
    RH-109 `RH-109-exterior-power-fourth-cross-support`
    RH-110 `RH-110-finite-memory-three-mode-capacity`
    RH-111 `RH-111-tail-energy-exterior-concentration`
    RH-112 `RH-112-global-wedge-lipschitz-barrier`
    RH-113 `RH-113-right-frame-directional-wedge`
    RH-114 `RH-114-psd-rayleigh-directional-tail`
    RH-115 `RH-115-composite-directional-support-gate`
    RH-116 `RH-116-monotone-memory-depth-optimization`
    RH-117 `RH-117-finite-anchor-scale-law-barrier`
    RH-118 `RH-118-conditional-composite-exterior-route`
    RH-119 `RH-119-ten-layer-exterior-route-review`
    RH-120 `RH-120-gauge-covariant-rayleigh-transfer`
    RH-121 `RH-121-optimal-gram-gauge-pairing`
    RH-122 `RH-122-fixed-coordinate-gauge-obstruction`
    RH-123 `RH-123-defect-stable-rayleigh-recurrence`
    RH-124 `RH-124-spectral-normalization-capacity-transport`
    RH-125 `RH-125-combined-directional-support-transfer`
    RH-126 `RH-126-direct-margin-scale-recurrence`
    RH-127 `RH-127-outward-loewner-transport-guards`
    RH-128 `RH-128-conditional-eventual-directional-support`
    RH-129 `RH-129-ten-layer-gauge-recurrence-review`
    RH-130 `RH-130-floor-free-semidefinite-directional-audit`
    RH-131 `RH-131-singular-gram-support-rayleigh-theory`
    RH-132 `RH-132-canonical-partial-isometry-forcing-gauge`
    RH-133 `RH-133-dyadic-packet-transport-gauge`
    RH-134 `RH-134-moving-frame-memory-tail-recurrence`
    RH-135 `RH-135-relative-metric-affine-tail-recurrence`
    RH-136 `RH-136-metric-balanced-packet-gauge`
    RH-137 `RH-137-finite-horizon-young-tail-envelope`
    RH-138 `RH-138-outward-finite-directional-composition`
    RH-139 `RH-139-ten-layer-controlled-viability-review`
    RH-140 `RH-140-normalized-snapshot-enclosure`
    RH-141 `RH-141-gap-stable-spectral-packet-enclosure`
    RH-142 `RH-142-factorized-arb-snapshot-packet-closure`
    RH-143 `RH-143-threshold-branch-stability-radius`
    RH-144 `RH-144-backward-block-controlled-viability`
    RH-145 `RH-145-delayed-start-superunit-birth-isolation`
    RH-146 `RH-146-projective-gram-base-recurrence`
    RH-147 `RH-147-correlated-base-tail-viability-tube`
    RH-148 `RH-148-conditional-source-directional-support-composition`
    RH-149 `RH-149-ten-layer-source-support-review`
    RH-150 `RH-150-temporal-anchor-packet-transport-obstruction`
    RH-151 `RH-151-ky-fan-reset-packet-atlas`
    RH-152 `RH-152-reset-transition-overlap-coherence`
    RH-153 `RH-153-congruence-covariant-reset-transport`
    RH-154 `RH-154-half-horizon-delayed-reset-suffix`
    RH-155 `RH-155-native-spectral-reset-memory-pair`
    RH-156 `RH-156-native-reset-support-floor`
    RH-157 `RH-157-spectral-reset-cross-action-cancellation`
    RH-158 `RH-158-adaptive-lag-reset-cross-bridge`
    RH-159 `RH-159-ten-layer-reset-route-review`
    RH-160 `RH-160-conditional-all-level-reset-dichotomy`
