---
p1_kind: "derived-fulltext-reading-copy"
route: "symplectic_map"
logical_paper_id: "symplectic_map--3-prime-multiplier-obstruction"
canonical_tex: "symplectic_map/papers/3-prime-multiplier-obstruction/paper/manuscript.tex"
canonical_pdf: "symplectic_map/papers/3-prime-multiplier-obstruction/paper/manuscript.pdf"
source_sha256: "d434e52e797567f33e9e9aac230b120241aa7a4dc05ae19c978f2ee6d4e2bd25"
render_method: "pandoc --from=latex --to=markdown+tex_math_dollars"
render_status: "generated-from-latex"
---

# Raw Rational-Prime Multipliers at a Frozen PCF Quadratic: Divisibility Obstruction and Exact Audit

[← 返回论文卡](index.md)
## 阅读副本说明

此文件是为检索和导航生成的 Markdown 副本。原始 TeX/PDF、结果、代码、审计与冻结收据仍是唯一的 source of truth。
转换不重新验证数学、引文、构建或路线状态，也不会提升任何 Hilbert–Pólya、零点或 RH 主张。

## 原始入口

- [原始 package](<../../../../../symplectic_map/papers/3-prime-multiplier-obstruction>)
- [规范 TeX](<../../../../../symplectic_map/papers/3-prime-multiplier-obstruction/paper/manuscript.tex>)
- [关联 PDF](<../../../../../symplectic_map/papers/3-prime-multiplier-obstruction/paper/manuscript.pdf>)
- [支撑 Markdown](<../../../../../symplectic_map/papers/3-prime-multiplier-obstruction/README.md>)
- [BibTeX](<../../../../../symplectic_map/papers/3-prime-multiplier-obstruction/paper/references.bib>)

## 转换器读取的文档元数据

```yaml
abstract: |
  An exact arithmetic clock for a periodic-orbit model must survive repetition, not merely reproduce a prime-like count. We audit such a clock at a frozen postcritically finite quadratic. For a monic polynomial $F\in\mathcal O_K[X]$ whose derivative has coefficient content $F'=mH$, every rational multiplier at a point fixed by $F^n$ lies in $m^n\mathbb Z$. Applied to $g(z)=z^2-u$, where $u$ is the real root of $u^3-2u^2+2u-2=0$, this divisibility and a separate fixed-point calculation exclude rational multipliers of raw prime modulus at every period. The result does not exclude a nonrational complex multiplier having prime modulus, and it leaves the rational target $|\lambda|=2^n$ open for periods $n\ge2$. Exact dynatomic, resultant, quotient-ring, and coordinate-conjugacy audits through period four recover four multiplier polynomials with no rational roots. Three adversarial controls recover allowed $2^n$ multipliers, the Chebyshev boundary, an odd prime multiplier, and a formal-period collision that vanishes after exact saturation. Finally, the cotangent formula carries regular zero-section multipliers to reciprocal symplectic pairs, but is singular at the quadratic critical point, noncompact, and not globally invertible. The outcome is therefore an all-period candidate obstruction, not a prime-orbit construction.
author:
- Liang Wang
bibliography:
- references.bib
date: 'August 13, 2026'
title: |
  Raw Rational-Prime Multipliers at a Frozen PCF Quadratic:\
  Divisibility Obstruction and Exact Audit
```

## Markdown 正文

# Introduction {#sec:introduction}

Periodic-orbit analogies with arithmetic become restrictive once the desired weights are stated term by term. In the standard prime-orbit motivation, a primitive label $p$ and its $r$-fold repetition should supply the same basic clock at lengths proportional to $\log p$ and $r\log p$, rather than only a generic prime-orbit counting law [@berry1999riemann]. This paper asks a deliberately smaller question: can the genuine derivative cocycle of a frozen quadratic supply exact rational prime multipliers without importing a prime table?

The parameter and arithmetic motivation are inherited from earlier work on the Logistic family $f_u(x)=1-ux^2$ [@wang2026prime]. That genealogy does not transfer the earlier paper's prime-sieve claims into the present experiment. We freeze only the autonomous algebraic map and its parameter, do not read any prime or Riemann-zero dataset, and treat the arithmetic clock as a new falsifiable obligation.

A finite-state, locally constant clock can fail because its periodic lengths occupy a finite-dimensional rational span. The nonlinear derivative cocycle is point-dependent and need not have that defect. At the present candidate, however, it encounters a different obstruction: algebraic integrality forces every *rational* period-$n$ multiplier to contain a factor $2^n$. This is an exact all-period statement, not an inference from a finite orbit search.

Figure [1](#fig:theorem-certificate){reference-type="ref" reference="fig:theorem-certificate"} summarizes the certificate and its two boundaries. Our contributions are:

1.  a self-contained derivative-content divisibility lemma and its candidate-specific all-period exclusion of raw rational-prime multipliers;

2.  an exact period-one-through-four implementation audit with independent coordinate duplication and controls that detect both allowed positive cases and failure of a theorem assumption; and

3.  a convention-safe cotangent calculation showing exactly what the regular symplectic bridge transports, and why it does not produce a global symplectomorphism through the critical point.

![The source-locked certificate. (a) Monicity makes finite periodic points integral, while $F'=mH$ contributes $m^n$; rationality then forces the remaining factor into $\mathbb Z$. (b) The frozen quadratic has no raw rational-prime multiplier at any period, whereas the rational exponent-prime target with base $2$ remains open for $n\ge2$. The modulus of a nonrational complex multiplier is outside the theorem. (c) On regular zero-section cycles only, the cotangent relation transports $\lambda$ to $(\lambda,\lambda^{-1})$; the critical line prevents a global lift.](<../../../../../symplectic_map/papers/3-prime-multiplier-obstruction/paper/figures/fig1_theorem_certificate.pdf>){#fig:theorem-certificate width="\\textwidth"}

The general lemma is elementary and receives no priority claim. The defensible result is the complete, source-locked certificate chain for one candidate. In particular, we do not claim absence of every rational multiplier, absence of $|\lambda|=2^n$ at higher periods, a theorem about complex modulus without rationality of $\lambda$, a compact global symplectic lift, a Riemann determinant, or a quantization.

# Prior work and claim boundary {#sec:prior}

#### Arithmetic multiplier spectra.

Global constraints on multiplier spectra are substantially deeper and broader than the sparse-value question considered here. Huguin proves rigidity for unicritical maps whose multipliers are all rational [@huguin2021unicritical], for quadratic rational maps with integer-ring multipliers [@huguin2022quadratic], and for rational maps whose entire multiplier spectrum lies in a number field [@huguin2023rational]. Related integer-multiplier rigidity is treated by @buff2022integer. Multiplier and length spectra also determine strong moduli data outside exceptional families [@jixie2023homoclinic]. These are whole-spectrum rigidity results; none is attributed the pointwise divisibility certificate below.

For a nonexceptional rational map, the rational span of finite characteristic exponents is infinite-dimensional [@jixiezhang2026space]. In the standard notation $z^2+c$, our map has $c=-u\ne0,-2$, so it lies on the nonexceptional side of that theorem. Infinite rank is important context: it shows why a finite-rank clock argument cannot simply be recycled for the nonlinear derivative. It neither forces nor forbids an individual multiplier to be a rational prime.

#### Dynatomic and multiplier polynomials.

Formal dynatomic cycles and arithmetic periodic-point machinery are standard [@morton1994rational; @silverman2007arithmetic]. Multiplier-polynomial integrality is known for $z^d+c$ and related polynomial families [@murakami2024arithmetic]; low-period multiplier data have strong moduli content [@huguin2024moduli]; and quadratic multiplier maps have been studied analytically in parameter space [@levin2009multipliers]. Our period-four computation is therefore an implementation audit, not a new dynatomic method, an asymptotic experiment, or a moduli reconstruction.

#### Symplectic extensions of one-dimensional maps.

Area-preserving weak-noise extensions of the Logistic map predate this work [@fogedby2005weak]. The singular and noninvertible structures arising from such symplectic formulations were analyzed explicitly by @demaeyer2009escape. We use the classical cotangent formula only to track the multiplier pair on regular branches. Its failure at $g'(0)=0$ is a limitation, not a new global construction.

# Derivative-content divisibility {#sec:divisibility}

Let $K$ be a number field with ring of integers $\mathcal O_K$. All periodic points below are finite points in $\overline{\mathbb Q}$; the polynomial fixed point at infinity is excluded.

[\[thm:content\]]{#thm:content label="thm:content"} Let $F\in\mathcal O_K[X]$ be monic of degree at least two. Suppose $$F'(X)=mH(X),\qquad m\in\mathbb Z,\quad m\ge2,
 \quad H\in\mathcal O_K[X].
 \label{eq:derivative-content}$$ If $F^n(\alpha)=\alpha$ and $\lambda_{n,\alpha}=(F^n)'(\alpha)\in\mathbb Q$, then $$\lambda_{n,\alpha}\in m^n\mathbb Z.
 \label{eq:content-conclusion}$$ The integer $n$ need not be the least period.

Every iterate $F^n$ is monic with coefficients in $\mathcal O_K$. Consequently $F^n(X)-X$ is monic, and a finite root $\alpha$ is integral over $\mathcal O_K$. Since $\mathcal O_K$ is integral over $\mathbb Z$, transitivity makes $\alpha$ an algebraic integer. Each orbit point $F^j(\alpha)$ is then an algebraic integer as well.

The chain rule and [\[eq:derivative-content\]](#eq:derivative-content){reference-type="eqref" reference="eq:derivative-content"} give $$\lambda_{n,\alpha}
 =\prod_{j=0}^{n-1}F'\!\left(F^j(\alpha)\right)
 =m^n\underbrace{\prod_{j=0}^{n-1}
 H\!\left(F^j(\alpha)\right)}_{\displaystyle\beta}.
 \label{eq:chain-content}$$ The factor $\beta$ is an algebraic integer. If $\lambda_{n,\alpha}$ is rational, then $\beta=\lambda_{n,\alpha}/m^n$ is both rational and an algebraic integer. The identity $\mathbb Q\cap\overline{\mathbb Z}=\mathbb Z$ gives $\beta\in\mathbb Z$, proving [\[eq:content-conclusion\]](#eq:content-conclusion){reference-type="eqref" reference="eq:content-conclusion"}.

Each assumption has a distinct role. Monicity and algebraic-integer coefficients control periodic-point integrality; the coefficient-wise factor $m$ controls the repeated derivative content; and rationality of the final multiplier converts an algebraic integer to an ordinary integer. Dropping any of these hypotheses changes the conclusion. The power map $F(z)=z^2$ also shows sharpness: its nonzero exact period-$n$ cycles have multiplier $2^n$, so the factor $m^n$ cannot be improved in general.

Theorem [\[thm:content\]](#thm:content){reference-type="ref" reference="thm:content"} assumes $\lambda\in\mathbb Q$. An equality $|\lambda|=p$ with nonrational complex $\lambda$ does not make $\lambda/m^n$ rational and is not covered. We retain this distinction in every result label and figure.

# Frozen PCF specialization {#sec:frozen}

Let $u$ be the unique real root of $$P(U)=U^3-2U^2+2U-2.
 \label{eq:parameter-polynomial}$$ The polynomial is monic, so $u$ is an algebraic integer. Moreover, $P'(U)=3(U-2/3)^2+2/3>0$, proving uniqueness of the real root. The rational root test shows that $P$ is irreducible, so $1,u,u^2$ is a basis of $K=\mathbb Q(u)$.

The postcritical-finite label can be checked directly rather than inherited as an assumption. With $d=u-1$, the critical orbit of $f_u$ is $$0\longmapsto 1\longmapsto -d\longmapsto d\longmapsto d.
 \label{eq:critical-orbit}$$ Indeed, $f_u(1)=1-u=-d$, while $f_u(\pm d)=1-u(u-1)^2=d$ is equivalent to $P(u)=0$. This finite critical orbit supplies parameter provenance only; neither Theorem [\[thm:content\]](#thm:content){reference-type="ref" reference="thm:content"} nor the two multiplier corollaries uses postcritical finiteness.

Define $$g(z)=z^2-u,\qquad f_u(x)=1-ux^2,\qquad \phi(x)=-ux.
 \label{eq:maps}$$ Because $u\ne0$, $\phi$ is invertible, and direct substitution gives $$\phi\circ f_u=g\circ\phi.
 \label{eq:conjugacy}$$ Periodic multipliers are therefore identical in the two coordinates.

For an exact period-$n$ orbit with a rational multiplier $\lambda$:

-   a *raw rational-prime target* satisfies $|\lambda|=p$ for a rational prime $p$;

-   a *rational exponent-prime target* satisfies $|\lambda|=p^n$.

These definitions do not include a nonrational complex $\lambda$ having the same modulus.

[\[cor:raw-prime\]]{#cor:raw-prime label="cor:raw-prime"} No finite periodic orbit of $g$, and hence none of $f_u$, has a rational multiplier whose absolute value is a rational prime.

Since $g'(z)=2z$, Theorem [\[thm:content\]](#thm:content){reference-type="ref" reference="thm:content"} gives $\lambda\in2^n\mathbb Z$ whenever a point fixed by $g^n$ has rational multiplier $\lambda$. For $n\ge2$, no nonzero element of $2^n\mathbb Z$ has prime absolute value.

At $n=1$, the only possible prime modulus is $2$. If $2z=2$, then $z=1$, and the fixed-point equation $z^2-u=z$ forces $u=0$. If $2z=-2$, then $z=-1$, and the same equation forces $u=2$. But $P(0)=-2$ and $P(2)=2$, so neither value is the frozen parameter. The conjugacy [\[eq:conjugacy\]](#eq:conjugacy){reference-type="eqref" reference="eq:conjugacy"} transfers the result to $f_u$.

[\[cor:exponent-prime\]]{#cor:exponent-prime label="cor:exponent-prime"} If an exact period-$n$ multiplier is rational and $|\lambda|=p^n$, then $p=2$. At period one, $p=2$ is absent. For $p=2$ and $n\ge2$, existence remains open here.

Write $\lambda=2^n k$ with $k\in\mathbb Z$. If $p$ is odd, the two sides of $2^n|k|=p^n$ have incompatible 2-adic valuations. For $p=2$, the equality reduces only to $|k|=1$, which Theorem [\[thm:content\]](#thm:content){reference-type="ref" reference="thm:content"} does not exclude. The period-one case was excluded in the proof of Corollary [\[cor:raw-prime\]](#cor:raw-prime){reference-type="ref" reference="cor:raw-prime"}.

No finite-period null search may replace the word "open" in Corollary [\[cor:exponent-prime\]](#cor:exponent-prime){reference-type="ref" reference="cor:exponent-prime"}. Conversely, no higher-period computation is needed to strengthen the all-period raw-prime conclusion.

# Exact audit and adversarial controls {#sec:audit}

The computation in this section audits formulas and software paths. It is not the source of Corollaries [\[cor:raw-prime\]](#cor:raw-prime){reference-type="ref" reference="cor:raw-prime"}--[\[cor:exponent-prime\]](#cor:exponent-prime){reference-type="ref" reference="cor:exponent-prime"}. The source lock fixes periods $1\le n\le4$, the field $\mathbb Q[u]/(P(u))$, exact arithmetic only, and a prohibition on external prime or zero data. Formal dynatomic factors are repeatedly saturated by lower-period fixed equations; point resultants are grouped into cycles; multiplier polynomials are checked in the exact orbit quotient; and rational roots are certified by simultaneous vanishing of the $1,u,u^2$ components.

## Frozen candidate

Table [1](#tab:candidate-ledger){reference-type="ref" reference="tab:candidate-ledger"} gives the complete cutoff ledger. The pointwise resultant is the exact $n$th power of the per-cycle polynomial in each row. Direct chain products agree with derivatives of the complete iterate, quotient-ring substitution annihilates the multiplier polynomial, and an independently implemented $f_u$ calculation agrees with the $g$-coordinate result after monic normalization.

::: {#tab:candidate-ledger}
   $n$   Degree   Cycles  Per-cycle multiplier polynomial in $L$     Rational roots
  ----- -------- -------- ----------------------------------------- ----------------
    1      2        2     $L^2-2L-4u$                                     none
    2      2        1     $L-4+4u$                                        none
    3      6        2     $L^2+(-16+8u)L-64+64u$                          none
    4      12       3     $L^3+(-48+16u^2)L^2+(256+256u^2)L+4096$         none

  : Exact frozen multiplier ledger. "Degree" is the exact-period point degree; the cycle count is degree divided by $n$. Empty rational-root sets are finite-cutoff audits, not the proof of the all-period obstruction.
:::

## Controls

The three controls in Table [2](#tab:controls){reference-type="ref" reference="tab:controls"} test different failure modes. The integral power map recovers the sharp $2^n$ factor. The Chebyshev boundary recovers signed rational multipliers, including the fixed raw-prime residue. Finally, the nonintegral parameter $c=-3/4$ violates the theorem's coefficient hypothesis and produces the odd prime multiplier $3$. At that same control, two formal period-two factors are completely removed by exact saturation, leaving exact period degree zero. Thus the code detects a positive prime value and does not confuse formal with exact period.

::: {#tab:controls}
  Map         Assumption status              Rational multipliers at $n=1,2,3,4$     Diagnostic
  ----------- ------------------------------ --------------------------------------- -----------------------------------------------
  $z^2$       theorem applies                $\{0,2\};\{4\};\{8\};\{16\}$            sharp $2^n$ clock
  $z^2-2$     theorem applies                $\{-2,4\};\{-4\};\{-8,8\};\{-16,16\}$   signed boundary
  $z^2-3/4$   coefficient assumption fails   $\{-1,3\};\varnothing;                  prime $3$; formal $n=2$ factors fully removed
                                             \varnothing;\varnothing$

  : Matched controls. The listed multipliers are exact rational values at periods 1--4. The final row deliberately violates algebraic-integral coefficients.
:::

Figure [2](#fig:exact-audit-controls){reference-type="ref" reference="fig:exact-audit-controls"} separates the theorem-level decision from the finite implementation ledger and makes the contamination removal visible.

![Exact cutoff audit and controls. Candidate periods one through four have the frozen exact degrees and no rational roots in either coordinate implementation. Controls recover $2^n$, signed Chebyshev values, the odd raw prime $3$, and complete removal of the spurious formal period-two component at $c=-3/4$. Only the analytic divisibility chain supports an all-period inference.](<../../../../../symplectic_map/papers/3-prime-multiplier-obstruction/paper/figures/fig2_exact_audit_controls.pdf>){#fig:exact-audit-controls width="\\textwidth"}

The required workflow completed in about 16.06 seconds of measured block time with peak resident memory 771,460 KiB. These are engineering diagnostics, not evidence. All 37 tests passed. No random seed, fit, tolerance-based integer recognition, target prime list, Riemann-zero table, or conditional high-period real-orbit search entered the result.

# What the symplectic bridge does---and does not do {#sec:bridge}

Let $\theta=p\,dq$ be the canonical one-form. On the regular locus $q\ne0$, the local cotangent formula for the base map $g$ is $$\widehat g(q,p)=(Q,P)
 =\left(q^2-u,\frac{p}{2q}\right).
 \label{eq:cotangent-map}$$

[\[prop:cotangent\]]{#prop:cotangent label="prop:cotangent"} On each branch $q>0$ and $q<0$, the map $\widehat g$ preserves the canonical one-form exactly and hence is symplectic. If a period-$n$ base orbit lies on the zero section and avoids $q=0$, then the return derivative has eigenvalues $(\lambda,\lambda^{-1})$, where $\lambda=(g^n)'(q_0)$.

Pulling back the one-form gives $$\widehat g^{*}(P\,dQ)
 =\frac{p}{2q}\,d(q^2-u)=p\,dq=\theta.
 \label{eq:one-form}$$ Thus $\widehat g^*d\theta=d\theta$, and its branch Jacobian has determinant one. At $p=0$, the one-step derivative is diagonal: $$D\widehat g(q,0)=
 \begin{pmatrix}2q&0\\0&(2q)^{-1}\end{pmatrix}.
 \label{eq:zero-section-derivative}$$ Multiplication around a regular period-$n$ orbit yields $$D\widehat g^n(q_0,0)=
 \begin{pmatrix}\prod_{j=0}^{n-1}2q_j&0\\
 0&\left(\prod_{j=0}^{n-1}2q_j\right)^{-1}
 \end{pmatrix},
 \label{eq:return-pair}$$ and the first entry is exactly $(g^n)'(q_0)=\lambda$.

Proposition [\[prop:cotangent\]](#prop:cotangent){reference-type="ref" reference="prop:cotangent"} transports the arithmetic obstruction on a regular orbit: a rational prime eigenvalue cannot appear there when it is already absent from the base multiplier. It does not repair the geometry. The denominator in [\[eq:cotangent-map\]](#eq:cotangent-map){reference-type="eqref" reference="eq:cotangent-map"} vanishes at $q=0$, precisely the critical line carrying the PCF seed. The inputs $(a,r)$ and $(-a,-r)$ have the same output, the two branch images overlap, and the regular domain is noncompact. A critical cycle with zero base multiplier has no reciprocal lift. Figure [3](#fig:symplectic-scope){reference-type="ref" reference="fig:symplectic-scope"} records these limitations.

![Scope of the cotangent relation. Each regular branch preserves $p\,dq$ and carries a zero-section return multiplier to a reciprocal pair. The critical line $q=0$, overlapping branch images, and unbounded phase space rule out interpreting the formula as a global compact symplectomorphism.](<../../../../../symplectic_map/papers/3-prime-multiplier-obstruction/paper/figures/fig3_symplectic_scope.pdf>){#fig:symplectic-scope width="94%"}

# Discussion and stopping decision {#sec:discussion}

The nonlinear derivative escapes the finite-state rank-one clock obstruction, but at this frozen parameter it fails the exact raw-prime gate for a separate arithmetic reason. The distinction matters. Generic orbit complexity, infinite-dimensional characteristic-exponent span, reciprocal symplectic multipliers, and a large primitive-orbit ledger do not imply exact rational prime values.

The candidate decision is therefore negative and scoped: $$\begin{aligned}
&\text{raw rational-prime multiplier:}&&\text{absent by theorem},\\
&\text{odd rational exponent-prime base:}&&\text{absent by theorem},\\
&\text{base }2\text{ exponent-prime, }n\ge2:&&\text{open},\\
&\text{complex modulus without rational }\lambda:&&\text{outside theorem},\\
&\text{cotangent carrier:}&&\text{branchwise exact only}.
\end{aligned}
\label{eq:decision}$$ For the raw-prime candidate, this is an arithmetic entry-gate failure. We do not proceed to cycle-determinant fitting, Riemann-zero comparison, quantization, or any spectral Route-B claim.

Two mathematically legitimate questions remain. First, the rational equality $|\lambda|=2^n$ could be studied by a new all-period argument; extending the period cutoff would not settle it. Second, one could design a separately source-locked global symplectic carrier rather than forcing the singular cotangent relation through $q=0$. Neither question changes the conclusion for the present raw-prime clock.

# Conclusion

At the frozen PCF quadratic, the genuine nonlinear derivative cocycle does not produce rational multipliers of raw prime modulus. The proof is an all-period integrality and divisibility certificate; exact computations through period four verify its implementation and expose its boundaries. A classical cotangent formula adds reciprocal symplectic geometry only off the critical line and does not restore the missing arithmetic clock. The useful outcome is thus a precise design exclusion: replacing a locally constant clock by the nonlinear derivative changes the obstruction, but does not pass the exact arithmetic entry gate.

# Proof dependency and scope ledger {#app:proof-ledger}

Table [3](#tab:proof-scope){reference-type="ref" reference="tab:proof-scope"} separates hypotheses that are sometimes collapsed in informal multiplier arguments.

::: {#tab:proof-scope}
  Hypothesis                      Used for                                             If removed
  ------------------------------- ---------------------------------------------------- --------------------------------------------------
  $F$ monic over $\mathcal O_K$   finite periodic coordinates are algebraic integers   denominators can enter periodic coordinates
  $F'=mH$ in $\mathcal O_K[X]$    one exact factor $m$ at every iterate                no uniform $m^n$ content follows
  $\lambda\in\mathbb Q$           $\mathbb Q\cap\overline{\mathbb Z}=\mathbb Z$        rational modulus alone is insufficient
  finite periodic point           root of monic $F^n-X$                                the point at infinity is a different fixed point

  : Role of each hypothesis in Theorem [\[thm:content\]](#thm:content){reference-type="ref" reference="thm:content"}.
:::

The proof applies to a point fixed by $F^n$, even if its least period divides $n$. Exact-period language enters only when a multiplier is assigned to a primitive cycle. The zero multiplier is allowed by the theorem but is never a positive-prime target.

# Exact polynomial certificates {#app:polynomials}

Let $L$ denote the cycle multiplier. The frozen cycle polynomials are $$\begin{aligned}
 M_1(L)&=L^2-2L-4u,\\
 M_2(L)&=L-4+4u,\\
 M_3(L)&=L^2+(-16+8u)L-64+64u,\\
 M_4(L)&=L^3+(-48+16u^2)L^2+(256+256u^2)L+4096.\end{aligned}$$ For each $n$, the audit stores the formal dynatomic polynomial, the saturated exact-period polynomial, the derivative of the complete iterate, the point resultant, the per-cycle polynomial, its coefficients in the basis $1,u,u^2$, the rational-component greatest common divisor, and a quotient annihilation certificate. The point resultants have degrees $2,2,6,12$ and are respectively the exact first, second, third, and fourth powers of the displayed cycle polynomials. In every row, the simultaneous rational component gcd is one.

The coordinate-duplication audit separately forms the dynatomic components for $f_u$ and $g$, transforms by $z=-ux$, and compares monic normalizations. It also checks $\phi\circ f_u=g\circ\phi$ symbolically; there is no numerical orbit matching.

# Reproducibility passport {#app:reproducibility}

The project is rooted at ``. From that directory, the required commands are

    python code/scripts/run_exact_audit.py --max-period 4
    pytest -q

The recorded environment is Python 3.12.3, SymPy 1.14.0, and pytest 9.0.3 on Linux x86-64. No GPU is used. The source-lock SHA-256 is

    aab59e6d97e919bd9f11f74cf45d8163fc320560dfa74bee85401bd184d37842

and the proof-package SHA-256 is

    6d01f26b5832bd88923d4f4ba0bb5ed7010a571f17f46a0e75b6247499034e17

The official run produces eleven machine-readable JSON artifacts, including its run summary; a post-validation immutable convenience manifest indexes those outputs and the frozen code tree. A static protocol scan rejects filesystem or subprocess target access and post-hoc prime tolerances. The same scan and adversarial tests confirm that no external prime or Riemann-zero resource is opened. Small integer primality labels in the controls are derived internally from exact output values.

The formal period-two contamination in the $c=-3/4$ control is not silently discarded: the raw formal factor, two removed lower-period factors, zero exact degree, and zero resultant degree are all retained in the control audit. The conditional high-period real-orbit ledger specified in the plan was disabled and never executed because no verified claim needs it.

# Artifact map {#app:artifact-map}

The principal machine-readable evidence is:

-   `` for the twelve proof-boundary gates;

-   `` and `` for the exact cutoff ledger;

-   `` for independent coordinate duplication;

-   `` for positive and assumption-violating controls;

-   `` for the regular one-form, determinant, reciprocal-pair, singularity, overlap, and noncompactness checks;

-   `` for the all-period, open, and outside-theorem classifications; and

-   `` for code, source-lock, result, environment, and test hashes.

All scientific values in the three figures are read from these frozen JSON files. The plotting scripts assert the expected candidate ID, source-lock scope, open base-2 status, and negative geometry flags before rendering.
