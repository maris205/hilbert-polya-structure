# Novelty Audit: Frozen PCF Quadratic Prime-Multiplier Obstruction

**Search boundary:** literature and preprints checked through 2026-08-13  
**Candidate:** `pcf_quadratic_prime_multiplier_obstruction_v1`  
**Audit state:** completed before candidate execution

## Verdict

`PROCEED AS A NARROW EXACT OBSTRUCTION NOTE; DO NOT CLAIM A NEW GENERAL THEORY`

The candidate-specific conclusion appears useful and clean: the inherited
nonlinear derivative clock has no rational multiplier whose absolute value
is a rational prime, at any period.  However, the mechanism is an elementary
algebraic-integrality argument.  Closely adjacent work already develops
dynatomic and multiplier polynomials, proves integrality properties for
unicritical families, and gives much stronger global rigidity results under
the hypothesis that *all* multipliers lie in a fixed arithmetic field.

Estimated novelty:

- general derivative-content theorem: **3/10** (likely a folklore-level
  corollary of standard algebraic-integrality facts);
- frozen all-period obstruction certificate: **5--6/10** as a sharply scoped
  finding in the present symplectic-map research program;
- cotangent-lift bridge: **1/10** (classical and explicitly not a contribution).

No checked source states the exact frozen conclusion for the real root of
$u^3-2u^2+2u-2$.  This negative search result is not evidence that the
general lemma is deep or previously unknown.

## Proposed contribution

For a monic polynomial $F\in\mathcal O_K[X]$ with $F'=mH$, show that every
rational period-$n$ multiplier lies in $m^n\mathbb Z$.  Applying this to
$g(z)=z^2-u$, with $u$ the selected algebraic-integer PCF parameter, excludes
all raw rational-prime multipliers exactly and at all periods.  The associated
regular cotangent map only transports the one-dimensional multiplier to a
reciprocal symplectic pair branchwise.

## Core claims and collision assessment

| Claim | Novelty | Closest boundary | Frozen positioning |
|---|---:|---|---|
| Rational period-$n$ multipliers of monic $F$ with $F'=mH$ lie in $m^n\mathbb Z$. | Low | Standard integrality of periodic points plus chain rule; multiplier-polynomial integrality in Murakami--Sano--Takehira and Huguin | Prove self-contained; call it an elementary divisibility lemma, not a literature-level breakthrough. |
| The frozen $g(z)=z^2-u$ has no raw rational-prime multiplier at any period. | Medium | No exact parameter-specific collision found; global rational/integer-multiplier rigidity is much broader but logically different | Candidate-specific exact obstruction certificate. |
| Odd exponent-prime clocks $|\lambda|=p^n$ are impossible for rational $\lambda$. | Low | Immediate $2$-adic corollary of the lemma | Supporting corollary only; leave $p=2$ open for $n\ge2$. |
| The nonlinear clock escapes finite-rank locally constant roofs. | Not new | Ji--Xie--Zhang prove infinite-dimensional characteristic-exponent span for non-exceptional rational maps | Context, not a new theorem. |
| Dynatomic/resultant computations audit periods $n\le4$. | None | Standard dynatomic and multiplier-polynomial machinery | Reproducibility and implementation audit only. |
| A cotangent construction gives reciprocal return eigenvalues $(\lambda,\lambda^{-1})$. | None | Classical cotangent lifts and weak-noise symplectic extensions | Bridge only, with singular/noninvertible caveats. |

## Closest prior work and exact boundaries

### Multiplier arithmetic and rigidity

1. **Huguin, “Unicritical polynomial maps with rational multipliers,”
   Conformal Geometry and Dynamics 25 (2021), 79--87.**
   [DOI 10.1090/ecgd/359](https://doi.org/10.1090/ecgd/359).
   It proves that a unicritical polynomial with only rational multipliers is
   a power or Chebyshev map.  Our statement concerns the much weaker and
   different sparse-value question “does even one rational prime occur?” at
   one frozen nonexceptional parameter.

2. **Huguin, “Quadratic rational maps with integer multipliers,”
   Mathematische Zeitschrift 302 (2022), 949--969.**
   [DOI 10.1007/s00209-022-03076-7](https://doi.org/10.1007/s00209-022-03076-7).
   It develops dynatomic and multiplier polynomials and classifies quadratic
   rational maps under bounded-period arithmetic hypotheses.  Its formulas
   are a computation precedent; they do not give the frozen prime-value
   obstruction as stated here.

3. **Huguin, “Rational maps with rational multipliers,” Journal de l'École
   polytechnique --- Mathématiques 10 (2023), 591--599.**
   [DOI 10.5802/jep.227](https://doi.org/10.5802/jep.227).
   It classifies rational maps whose multipliers all lie in a given number
   field.  It does not classify isolated rational values within an otherwise
   nonrational spectrum.

4. **Ji and Xie, “Homoclinic orbits, multiplier spectrum and rigidity
   theorems in complex dynamics,” Forum of Mathematics, Pi 11 (2023), e11.**
   [DOI 10.1017/fmp.2023.12](https://doi.org/10.1017/fmp.2023.12).
   Multiplier and length spectra determine strong rigidity data outside the
   flexible Lattès family.  This is global spectral rigidity, not a
   prime-value divisibility theorem.

5. **Ji, Xie, and Zhang, “Space spanned by characteristic exponents,”
   Mathematische Annalen 394 (2026), article 62.**
   [DOI 10.1007/s00208-026-03361-4](https://doi.org/10.1007/s00208-026-03361-4),
   [arXiv:2308.00289](https://arxiv.org/abs/2308.00289).
   For a nonexceptional rational map, the $\mathbb Q$-span of finite
   characteristic exponents is infinite-dimensional.  Since
   in the standard notation $z^2+c$ the frozen parameter is $c=-u\ne0,-2$
   (equivalently, $u\ne0,2$ in our notation), so this result is the correct
   boundary against claiming that the nonlinear spectrum has finite rank.
   Infinite rank neither forces nor forbids exact rational-prime multipliers.

6. **Buff, Gauthier, Huguin, and Raissy, “Entire or rational maps with
   integer multipliers.”**
   [arXiv:2212.03661](https://arxiv.org/abs/2212.03661); published in
   *Algebraic, Complex, and Arithmetic Dynamics*, Simons Symposia, Springer
   (2026), pp. 307--317, volume
   [DOI 10.1007/978-3-032-04048-0](https://doi.org/10.1007/978-3-032-04048-0).
   This supplies another proof and an entire-map extension of global
   integer-multiplier rigidity.  It does not address a single prime value at
   the frozen quadratic.

### Dynatomic and multiplier-polynomial machinery

7. **Morton and Silverman, “Rational periodic points of rational
   functions,” International Mathematics Research Notices 1994(2),
   97--110.**
   [DOI 10.1155/S1073792894000127](https://doi.org/10.1155/S1073792894000127).
   This is a standard source for formal dynatomic cycles.  It also motivates
   the mandatory distinction between formal and exact period at multiplier
   roots of unity.

8. **Silverman, *The Arithmetic of Dynamical Systems*, GTM 241, Springer
   (2007).**
   [DOI 10.1007/978-0-387-69904-2](https://doi.org/10.1007/978-0-387-69904-2).
   This is background for dynatomic polynomials and arithmetic dynamics, not
   a novelty source for the candidate.

9. **Murakami, Sano, and Takehira, “Arithmetic properties of multiplier
   polynomials for certain polynomial maps” (2024).**
   [arXiv:2403.17315](https://arxiv.org/abs/2403.17315),
   [DOI 10.48550/arXiv.2403.17315](https://doi.org/10.48550/arXiv.2403.17315).
   It proves integrality statements for multiplier polynomials of
   $z^d+c$ and related families.  This is the closest algebraic collision.
   Our point-level $m^n$ divisibility proof is shorter and more specialized;
   it must not be marketed as the first integrality result for unicritical
   multipliers.

10. **Huguin, “Moduli spaces of polynomial maps and multipliers at small
    cycles” (2024).**
    [arXiv:2412.19335](https://arxiv.org/abs/2412.19335),
    [DOI 10.48550/arXiv.2412.19335](https://doi.org/10.48550/arXiv.2412.19335).
    It shows the current strength of period-one and period-two multiplier
    data on polynomial moduli.  Our $n\le4$ calculations are audits of a
    frozen map, not a moduli reconstruction claim.

11. **Levin, “Multipliers of periodic orbits of quadratic polynomials and
    the parameter plane,” Israel Journal of Mathematics 170 (2009),
    285--315.**
    [DOI 10.1007/s11856-009-0030-0](https://doi.org/10.1007/s11856-009-0030-0).
    This is adjacent analytic work on multiplier maps in the quadratic
    parameter plane; it does not target rational-prime multiplier values.

### Symplectic-extension precedent

12. **Fogedby and Jensen, “Weak noise approach to the logistic map,” Journal
    of Statistical Physics 121 (2005), 759--778.**
    [DOI 10.1007/s10955-005-5457-z](https://doi.org/10.1007/s10955-005-5457-z).
    It replaces a noisy one-dimensional map by an area-preserving
    two-dimensional map.  It is a direct warning that such an extension is
    classical rather than a new symplectic mechanism.

13. **Demaeyer and Gaspard, “Noise-induced escape from bifurcating
    attractors: Symplectic approach in the weak-noise limit,” Physical
    Review E 80 (2009), 031147.**
    [DOI 10.1103/PhysRevE.80.031147](https://doi.org/10.1103/PhysRevE.80.031147).
    It explicitly discusses the symplectic map associated with a
    one-dimensional noninvertible map and the consequences of
    noninvertibility.  Our cotangent formula is only a clean local bridge.

## What survives as the paper's delta

The defensible delta is the following chain, treated as one exact case study:

1. start from the already frozen PCF parameter, without inspecting prime or
   zero data;
2. move from a finite-memory constant clock to the genuine nonlinear
   derivative cocycle;
3. prove an all-period arithmetic obstruction before computing candidate
   cycles;
4. audit it at low periods with exact multiplier polynomials and explicit
   controls;
5. show that the classical symplectic extension inherits reciprocal
   multipliers but does not repair the arithmetic obstruction.

The contribution is therefore a **design certificate and no-go result**, not
a classification theorem for multiplier spectra and not a new symplectic
construction.

## Explicit nonclaims

- No claim that multiplier-polynomial integrality is new.
- No claim that no rational multiplier occurs; only raw rational-prime
  multipliers are excluded all-period.
- No claim that $|\lambda|=2^n$ is absent for $n\ge2$.
- No modulus-only claim for complex multipliers.
- No global, compact, or everywhere-defined symplectic lift.
- No prime-orbit correspondence, Riemann determinant, zero comparison,
  quantization, or Route-B readiness.
- No statistical evidence is used to establish the theorem.

## Query log and negative-search boundary

The audit used combinations of the following query families, with recent
2024--2026 variants included:

- `unicritical polynomial rational multiplier divisibility d^n`
- `quadratic polynomial rational prime multiplier periodic orbit`
- `arithmetic properties multiplier polynomial z^d+c`
- `multiplier polynomial integrality unicritical`
- `rational maps rational multipliers 2024 2025 2026`
- `space spanned characteristic exponents rational map 2026`
- `small cycle multipliers polynomial moduli 2024`
- `cotangent lift noninvertible map symplectic`
- `weak noise logistic map area preserving extension`

No checked title or abstract advertised the exact frozen theorem or an
all-period rational-prime multiplier audit at this PCF parameter.  Because
the proof is a three-step integrality argument, this search outcome supports
only narrow candidate novelty, not priority for the general lemma.

## Final recommendation

Proceed if the paper is written around the exact obstruction workflow and
the raw-versus-exponent distinction.  Abandon or merge it if the intended
headline becomes “a new integrality theorem for multiplier polynomials” or
“a new symplectic lift,” because those framings collide directly with the
literature above.
