---
p1_kind: "derived-fulltext-reading-copy"
route: "symbolic_dynamics"
logical_paper_id: "symbolic_dynamics--12-fourier-null-haar-fiber"
canonical_tex: "symbolic_dynamics/papers/12-fourier-null-haar-fiber/main.tex"
canonical_pdf: "symbolic_dynamics/papers/12-fourier-null-haar-fiber/main.pdf"
source_sha256: "fc06a292fc8b76ec4ef53daf0cd0d26ff3c56d7416b00dbe6b22968ba083ac28"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Fourier-Null Haar Fibers over Tensor-Prime Symbolic Loops: The Unique Positive Diffuse Escape and Determinant Invisibility

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symbolic_dynamics/papers/12-fourier-null-haar-fiber>)
- [规范 TeX](<../../../../../symbolic_dynamics/papers/12-fourier-null-haar-fiber/main.tex>)
- [关联 PDF](<../../../../../symbolic_dynamics/papers/12-fourier-null-haar-fiber/main.pdf>)
- [支撑 Markdown](<../../../../../symbolic_dynamics/papers/12-fourier-null-haar-fiber/README.md>)
- [BibTeX](<../../../../../symbolic_dynamics/papers/12-fourier-null-haar-fiber/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  We classify the infinite positive fibers that preserve every tensor-prime repetition coefficient and ask whether they create visible dynamical phase. For a finite positive measure $\mu$ on the unit circle, the conditions $\int z^r\,d\mu(z)=1$ for all $r\ge1$ hold exactly when $\mu=\delta_1+c m_{\rm H}$ with $c\ge0$ and normalized Haar measure $m_{\rm H}$. Thus the Haar component is the unique positive diffuse escape from finite-support moment rigidity. SD-C14 realizes it by $\mathcal A=\mathbb C\oplus L(\mathbb Z)$, $W=1\oplus u$, and the trace $\Phi_c(a\oplus x)=a+c\tau(x)$. For $c>0$ this trace is faithful but not normalized: $\Phi_c(1)=1+c$, whereas $\Phi_c(W^r)=1$ for every nonzero integer $r$. The associated scalar trace-log determinant is nevertheless $D_c(q)=1-q$, independent of $c$. Fuglede--Kadison magnitude sees $c$ only through the nonholomorphic factor $\max(1,|q|)^c$; self-adjointization obeys $H^2=I$ and erases the phase; recurrent inverse coupling produces balanced mixed words. Finite cyclic approximants leak at their dimension, perturbed Haar densities leak at the first nonzero Fourier mode, and arbitrary positive atom inventories reproduce the construction. A deterministic audit found the exact first leak for every cyclic order $2\leq N\leq64$, all $64$ preregistered density perturbations leaked at their prescribed mode, and all nine prime/composite/random inventory controls had exactly zero determinant difference and phase range. The result is a sharp determinant-invisibility theorem and a scoped stop, not an arithmetic divisor or spectral realization.
author:
- Anonymous Authors
bibliography:
- references.bib
date: 'August 13, 2026'
title: |
  Fourier-Null Haar Fibers over Tensor-Prime Symbolic Loops:\
  The Unique Positive Diffuse Escape and Determinant Invisibility
```

## Markdown 正文

# Introduction {#sec:introduction}

Finite positive unitary fibers are rigid. If a normalized matrix trace sees one unitary moment equal to one, faithfulness forces the unitary to be the identity. An infinite diffuse trace changes that conclusion: a Haar unitary $u$ satisfies $$\tau(u^r)=0\qquad(r\in\mathbb Z\setminus\{0\}).                 \tag{1.1}$$ The tensor-prime loop could therefore carry a trivial visible component and an arbitrary amount of Fourier-null Haar mass without changing any nonzero repetition moment. SD-C14 tests whether this exact escape also supplies the missing determinant-visible phase.

The measure theorem is stronger than an example. Let $\mu$ be any finite positive measure on the unit circle. We prove $$\int_\mathbb Tz^r\,d\mu(z)=1\quad(r\ge1)
 \quad\Longleftrightarrow\quad
 \mu=\delta_1+c\,m_{\rm H},\quad c\ge0.                  \tag{1.2}$$ Haar mass is the only positive diffuse freedom. A normalized state has total mass one, so it forces $c=0$ and recovers finite moment rigidity. Exactness with $c>0$ therefore depends on a nonnormalized finite positive trace.

The escape is real but spectrally sterile for the frozen scalar determinant. On the fiber $$\mathcal A=\mathbb C\oplus L(\mathbb Z),\qquad
 W=1\oplus u,\qquad
 \Phi_c(a\oplus x)=a+c\tau(x),                             \tag{1.3}$$ all nonzero power traces equal one. Hence the trace-log germ is $$\exp\Phi_c\bigl(\log(1-qW)\bigr)=1-q,                    \tag{1.4}$$ exactly the determinant with no Haar sector. The ghost is not merely hard to detect; it is deleted coefficient by coefficient from this holomorphic observable.

Other observables do not repair the loss while retaining the same data type. The Fuglede--Kadison determinant is $$|1-q|\max(1,|q|)^c,                                      \tag{1.5}$$ so it remains blind in the Euler disk and becomes $c$-sensitive only through a positive radial factor. Natural self-adjointization squares to the identity and collapses the Haar phase to $\{\pm1\}$. Adding both $u$ and $u^{-1}$ as recurrent edges creates trace-visible balanced words such as $uu^{-1}=e$, which are new mixed closed paths rather than pure $p^r$ repetitions.

The paper establishes four conclusions.

1.  Equation (1.2) gives the complete positive-measure classification.

2.  SD-C14 realizes every $c\ge0$ but is normalized only at $c=0$.

3.  Its analytic determinant is exactly Euler-ledger preserving and exactly Haar-sector blind.

4.  Finite approximants, density perturbations, matched inventories, and recurrent coupling expose delay, instability, proves-too-much, and mixed-word boundaries.

The accompanying deterministic audit evaluates cyclic orders $N=2,\ldots,64$ through repetition $128$, Haar weights $c\in\{0.25,1,3\}$ at twelve complex points, and $64$ signed Fourier-density perturbations. It also compares three $128$-atom inventories at the same three Haar weights. Every predicted first leak occurs at the frozen mode; the maximum Fuglede--Kadison quadrature residual is $4.45\times10^{-16}$, while all nine inventory controls have exactly zero analytic-determinant difference and phase range. These computations audit the formulas but do not supply target-zero evidence.

All statements remain within Symbolic Dynamics. Operator-algebraic tools describe the symbolic fiber and its trace; they do not launch a separate operator-realization program. No analytic continuation, functional equation, divisor count, or fixed self-adjoint generator is claimed.

# Symbolic group extensions and determinant precedents {#sec:related}

Unitary and group-valued symbolic extensions are established constructions. @adachisunada1987 connect twisted Perron--Frobenius operators with dynamical $L$-functions, while @parrypollicott1990 [Chapter 8] treat unitary representation characters on periodic holonomy over subshifts of finite type. Isometric extensions can substantially change zeta functions [@ward1999]. These sources rule out any novelty claim for adding a unitary or compact-group fiber.

Infinite amenable group extensions and periodic graph determinants are also well developed. @sharp2020 studies convergence of zeta functions for amenable extensions of shifts. Periodic graph frameworks use group traces and analytic determinants [@guidoisolalapidus2008]. Most directly, @clair2009 treats graph zeta functions with $\mathbb Z$ actions. Under Fourier transform, the canonical $L(\mathbb Z)$ trace is Haar integration on the circle and extracts the zero Fourier coefficient. The averaging mechanism behind SD-C14 is therefore not new.

The operator-algebraic tools have distinct scopes. Fuglede--Kadison theory provides a positive determinant in finite factors [@fugledekadison1952]. Trace-associated Banach-algebra determinants carry path and quotient information beyond the scalar germ used here [@delaharpeskandalis1984]. We consequently freeze the trace-log germ at $q=0$ and do not call every determinant convention equivalent. The existence of Haar unitaries is tied to diffuse traces [@thiel2024]; SD-C14 uses a canonical example rather than claiming a new Haar-unitary construction.

The paper's contribution is the source-locked synthesis. We isolate the complete positive-measure escape from the tensor-prime repetition ledger and prove that this escape is invisible to the very scalar holomorphic determinant that preserves the ledger. The literature supports each surrounding tool, not a Riemann divisor conclusion.

# The unique positive diffuse escape {#sec:classification}

Write $m_{\rm H}$ for normalized Haar measure on $\mathbb T$ and $$\widehat\mu(r)=\int_\mathbb Tz^r\,d\mu(z),\qquad r\in\mathbb Z.     \tag{3.1}$$

[\[thm:classification\]]{#thm:classification label="thm:classification"} Let $\mu$ be a finite positive Borel measure on $\mathbb T$. Then $$\widehat\mu(r)=1\quad\text{for every }r\ge1              \tag{3.2}$$ if and only if there is a unique $c\ge0$ such that $$\mu=\delta_1+c\,m_{\rm H}.                              \tag{3.3}$$ Here $c=\mu(\mathbb T)-1$.

The reverse implication follows from $\widehat m_{\rm H}(r)=0$ for $r\ne0$. Conversely, positivity gives $$\widehat\mu(-r)=\overline{\widehat\mu(r)}=1,
 \qquad r\ge1.                                            \tag{3.4}\label{eq:negative-moments}$$ Put $M=\mu(\mathbb T)$. Since $1=|\widehat\mu(1)|\le M$, the number $c=M-1$ is nonnegative. Define the finite signed measure $$\nu=\mu-\delta_1-cm_{\rm H}.                             \tag{3.5}$$ Its zeroth Fourier coefficient is $M-1-c=0$; the hypothesis together with [\[eq:negative-moments\]](#eq:negative-moments){reference-type="eqref" reference="eq:negative-moments"} shows that every nonzero coefficient also vanishes. Integration against $\nu$ therefore vanishes for every trigonometric polynomial. Such polynomials are uniformly dense in $C(\mathbb T)$, so integration against $\nu$ vanishes for every continuous function. The Riesz uniqueness theorem yields $\nu=0$. The formula $c=M-1$ proves uniqueness.

[\[cor:boundary\]]{#cor:boundary label="cor:boundary"} Under the hypotheses of [\[thm:classification\]](#thm:classification){reference-type="ref" reference="thm:classification"}:

1.  if $\mu(\mathbb T)=1$, then $\mu=\delta_1$;

2.  if $\mu$ has finite support, then $\mu=\delta_1$.

Normalization makes $c=0$. If finite support held with $c>0$, the right side of [\[thm:classification\]](#thm:classification){reference-type="ref" reference="thm:classification"} would have the nonzero nonatomic component $cm_{\rm H}$, a contradiction.

Positivity is load-bearing. It recovers negative coefficients from positive ones in [\[thm:classification\]](#thm:classification){reference-type="ref" reference="thm:classification"}. For an arbitrary complex measure, the positive Fourier coefficients alone do not supply that implication.

The theorem also quantifies finite approximations. If $m_N$ is uniform measure on the $N$th roots of unity, then $$\widehat m_N(r)=
 \begin{cases}1,&N\mid r,\\0,&N\nmid r.
 \end{cases}                                               \tag{3.6}$$ Thus $\delta_1+cm_N$ passes repetitions $1,\ldots,N-1$ but leaks mass $c$ at repetition $N$. No fixed finite fiber realizes the all-order escape.

A small density perturbation is equally diagnostic. For $$d\mu_\varepsilon(z)
 =d\delta_1(z)+c\bigl[1+2\varepsilon\cos(k\theta)\bigr]
   \frac{d\theta}{2\pi},\quad z=e^{i\theta},                \tag{3.7}$$ with $|\varepsilon|\le1/2$, positivity is preserved but the $k$th moment becomes $1+c\varepsilon$. Exact invisibility is a precise Haar condition, not a generic continuous-spectrum effect.

# SD-C14 and its determinant data types {#sec:determinants}

Let $F_p$ be the tensor-prime full-shift atom with entropy $\log p$. Its primitive loop $\gamma_p$ and repetitions $\gamma_p^r$ remain the base grammar. The fiber is $$\mathcal A=\mathbb C\oplus L(\mathbb Z),\qquad W=1\oplus u,                 \tag{4.1}$$ where the canonical group trace satisfies $\tau(u^r)=0$ for $r\ne0$. For a frozen $c\ge0$, put $$\Phi_c(a\oplus x)=a+c\tau(x).                             \tag{4.2}$$ For $c>0$ this is a faithful finite positive trace, but $$\Phi_c(1)=1+c,\qquad \Phi_c(W^r)=1\quad(r\ne0).
 \tag{4.3}\label{eq:power-moments}$$ The normalized trace $\widetilde\Phi_c=\Phi_c/(1+c)$ instead gives $\widetilde\Phi_c(W^r)=1/(1+c)$, so normalization and the exact one-copy ledger are incompatible when $c>0$.

## The analytic trace-log

For $|q|<1$, norm functional calculus defines $$D_c(q)=\exp\Phi_c\bigl(\log(1-qW)\bigr).                 \tag{4.4}$$

[\[thm:blindness\]]{#thm:blindness label="thm:blindness"} For every $c\ge0$ and $|q|<1$, $$D_c(q)=1-q.                                               \tag{4.5}$$ More generally, two scalar trace-log germs agree near $q=0$ if and only if their aggregated positive power traces agree at every order.

The logarithm series and the moment identity in [\[eq:power-moments\]](#eq:power-moments){reference-type="eqref" reference="eq:power-moments"} give $$\log D_c(q)
 =-\sum_{r\ge1}\frac{q^r}{r}\Phi_c(W^r)
 =-\sum_{r\ge1}\frac{q^r}{r}=\log(1-q).                  \tag{4.6}$$ Equality of germs is equivalent to equality of their Taylor coefficients, which are the power traces divided by $r$.

On the tensor-prime direct sum, take $q=zp^{-s}$ at atom $p$. For $\operatorname{Re}s>1$ and $|z|\,2^{-\operatorname{Re}s}<1$, absolute convergence yields $$D_c(s,z)=\prod_pD_c(zp^{-s})=\prod_p(1-zp^{-s}),         \tag{4.7}$$ independently of $c$. This is an exact analytic determinant and an unchanged Euler ledger. It contains no new Haar-fiber information.

## Magnitude and normalized spectral distribution

The Fuglede--Kadison determinant answers a different question.

[\[prop:fk\]]{#prop:fk label="prop:fk"} For $q\in\mathbb C$, $$\Delta_{\Phi_c}(1-qW)
 =|1-q|\max(1,|q|)^c.                                     \tag{4.8}$$

Spectral calculus and Jensen's circle formula give $$\begin{aligned}
 \log\Delta_{\Phi_c}(1-qW)
 &=\log|1-q|+c\int_\mathbb T\log|1-qz|\,dm_{\rm H}(z)\\
 &=\log|1-q|+c\log^+|q|.                                 \tag{4.9}\end{aligned}$$ Exponentiation proves the formula.

Inside $|q|<1$, [\[prop:fk\]](#prop:fk){reference-type="ref" reference="prop:fk"} is as blind as the analytic determinant. Outside the disk it detects $c$ through radial magnitude, but is positive real rather than a holomorphic oriented divisor. With the normalized trace, the normal unitary $W$ has probability spectral distribution $$\frac1{1+c}\delta_1+\frac{c}{1+c}m_{\rm H}.              \tag{4.10}$$ It sees the continuous circle spectrum only after diluting the base atom coefficient. These coordinates cannot be spliced into [\[thm:blindness\]](#thm:blindness){reference-type="ref" reference="thm:blindness"} as a single Route-A determinant.

# Self-adjointization, coupling, and controls {#sec:controls}

The most natural self-adjoint block erases rather than reveals Haar phase. Set $$H=\begin{pmatrix}0&W\\W^*&0\end{pmatrix}.$$ Then $$H^2=I.                                                    \tag{5.1}$$ Its spectrum is contained in $\{-1,1\}$, independent of the circle-valued phase of $u$. The weighted block $$H_q=\begin{pmatrix}0&qW\\\overline qW^*&0\end{pmatrix}$$ satisfies $H_q^2=|q|^2I$ and introduces $\overline q$, so it is not the frozen holomorphic $s$-determinant.

Recurrent symbolic coupling makes the phase trace-visible only by creating the wrong closed words. Consider two vertices joined by directed edges with formal scalar weights $x,y$ and fiber labels $u,u^{-1}$: $$\mathcal L=\begin{pmatrix}0&xu\\yu^{-1}&0\end{pmatrix}.         \tag{5.2}$$ The balanced words $uu^{-1}=u^{-1}u=e$ give $$\Phi_c^{(2)}(\mathcal L^2)=2(1+c)xy.                             \tag{5.3}$$ This is a mixed two-cycle. It is neither a pure $p^2$ repetition nor Fourier-null. A nonbacktracking grammar can delete immediate reversal, but then the grammar and determinant have changed; it does not rescue the self-adjoint block.

[\[thm:trilemma\]]{#thm:trilemma label="thm:trilemma"} Within SD-C14, a scalar coupling has exactly three possible outcomes:

1.  it changes some positive trace coefficient and corrupts the Euler ledger;

2.  all new trace coefficients cancel, in which case the scalar trace-log determinant remains blind to the coupling;

3.  it is detected only by a normalized spectral, magnitude, chiral, or other observable that is not the same holomorphic Euler determinant.

No outcome supplies determinant-visible Haar motion while retaining the frozen all-order ledger.

By [\[thm:blindness\]](#thm:blindness){reference-type="ref" reference="thm:blindness"}, the scalar germ is determined coefficientwise by all aggregated positive traces. If a coefficient changes, the ledger changes. If none changes, the germ is identical. The remaining case changes the observable, as the explicit formulas above demonstrate.

The frozen adversarial controls sharpen this theorem.

0.98L0.22X L0.24 Control & Exact outcome & Interpretation\
$c=0$ & $W$ reduces to the rigid visible point mass & Paper11 baseline\
cyclic $N$-fiber & first defect at $r=N$ & finite dimension only delays leakage\
perturbed Haar density & first nonzero Fourier mode changes that repetition & invisibility is nongeneric\
normalized trace & moment becomes $1/(1+c)$ & state normalization fails ledger\
composite/random clocks & same factor $1-za_n$ for every positive inventory & no arithmetic selectivity\
inverse recurrent edges & balanced word contributes at power two & coupling pollutes grammar\

The finite audit realizes these controls without fitted parameters. For every $N=2,\ldots,64$, checked through $r=128$, the cyclic control first leaks at exactly $r=N$. Frequencies $1,\ldots,16$ at four signed amplitudes leak at the preregistered frequency in all $64$ cases. For $c\in\{0.25,1,3\}$ and twelve complex $q$-values, the largest numerical residual in the Fuglede--Kadison formula is $4.440892098500626\times10^{-16}$. Finally, tensor-prime, composite-only, and seeded random-increasing inventories, each truncated to $128$ atoms, give analytic-determinant difference and phase range exactly zero for all nine inventory--$c$ combinations. Thus the strongest numerical result is a *PROVES\_TOO\_MUCH* control, not evidence for a target divisor.

The inventory control is decisive. For any positive atom weights $(a_n)$ in the convergence domain, $$\prod_nD_c(za_n)=\prod_n(1-za_n).                          \tag{5.4}$$ Nothing in [\[thm:blindness\]](#thm:blindness){reference-type="ref" reference="thm:blindness"} distinguishes primes from composites or random increasing clocks. The mechanism therefore proves too much as an arithmetic selector.

# Route outcome and conclusion {#sec:route}

The source-locked Route-A evaluation is

0.98L0.08L0.25X Layer & Verdict & Strongest evidence and failure\
A0 & analytic arithmetic origin & tensor-prime atoms and entropy clock are inherited exactly; the Haar mechanism itself is not prime-selective\
A1 & pass analytic & pure atom loops and every repetition retain coefficient one under $\Phi_c$; coupling creates wrong mixed cycles\
A2 & analytic determinant & the trace-log is exact on $\operatorname{Re}s>1$, but equals the old ghost-blind Euler determinant\
A3 & fail & no continuation, reflection, Gamma completion, counting law, Weil compression, or divisor mechanism\
A4 & fail & self-adjointization erases phase; no fixed generator or compatible spectral determinant is defined\

The canonical tuple is

  -----------------------------------------------------
   `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_PASS_ANALYTIC,`
      `A2_ANALYTIC_DETERMINANT, A3_FAIL, A4_FAIL).`
  -----------------------------------------------------

The A1 and A2 passes certify the unchanged base ledger and determinant. They do not certify the proposed Haar phase as a visible arithmetic mechanism. Matched inventories trigger the adversarial stop, so the overall outcome is $$\boxed{\texttt{ROUTE\_A\_REJECTED}.}                      \tag{6.1}$$

Route B is not invoked. SD-C14 defines no densely specified fixed self-adjoint operator, canonical boundary condition, compact-resolvent mechanism, intrinsic $T\log T$ law, von-Mangoldt trace formula, or completed xi determinant. In evaluator notation, $$\mathtt{route\_b\_invocation\_allowed=false}.             \tag{6.2}$$

The positive theorem is still useful. It closes the finite-to-diffuse gap sharply: the only positive mass that can be added without changing any nonzero repetition moment is Haar mass, and that same mass is deleted from the scalar holomorphic trace-log. Visibility requires keeping more than the Haar average.

The next smallest same-family obligation is therefore character-resolved. One may retain an $L(\mathbb Z)$-valued or character family before averaging and demand that its zero Fourier mode recover the Euler ledger while a transverse response is intrinsic to the entropy grammar and disappears for matched composite and random inventories. A uniform phase fails this test immediately. No such candidate is constructed here.

# Supplementary proof details and scope audit {#app:proofs}

## Fourier uniqueness in the classification theorem

If a finite signed measure $\nu$ has all Fourier coefficients zero, then it annihilates every trigonometric polynomial. For $f\in C(\mathbb T)$, choose trigonometric polynomials $P_n$ with $\|f-P_n\|_\infty\to0$. Finite total variation gives $$\left|\int f\,d\nu\right|
 \le \left|\int P_n\,d\nu\right|
     +\|f-P_n\|_\infty\,\|\nu\|_{\rm TV}\longrightarrow0.$$ Thus $\nu$ annihilates $C(\mathbb T)$ and is zero. No moment-determinacy theorem beyond compact Fourier uniqueness is needed.

## Faithfulness and normalization

For $c>0$, if $a\oplus x\ge0$ and $\Phi_c(a\oplus x)=0$, then $a=0$ and $\tau(x)=0$. Faithfulness of the canonical group trace gives $x=0$. Nevertheless $\Phi_c(1)=1+c$, so the word "faithful" does not imply "state." This distinction is the price of the diffuse escape.

## Jensen boundary cases

For $|q|<1$, the circle average in [\[prop:fk\]](#prop:fk){reference-type="ref" reference="prop:fk"} is zero. For $|q|>1$, factor $1-qz=-qz(1-q^{-1}z^{-1})$; the second factor has zero mean logarithm, leaving $\log|q|$. At $|q|=1$, the integrable logarithmic singularity follows by radial limiting. Hence the formula holds on all of $\mathbb C$ with determinant zero at $q=1$ because of the scalar point mass.

## What is not proved

The classification does not rule out complex signed measures with the same positive moments, non-scalar operator-valued determinants, or character families before Haar averaging. None of those variants may inherit the Route-A tuple without a new source lock, determinant convention, and matched arithmetic controls. Cross-family geometric or operator constructions are recorded only in `ROUND2_CLUES.md`.
