# Final Review: HCS-C17 Modular Scattering Clock Obstruction

## Verdict

**READY AS A SCOPED OBSTRUCTION PROJECT — 52/60.**

The Route-A candidate itself is **rejected**: the modular cusp denominator cannot be the nontrivial exact clock of a primitive hyperbolic Euler/Fredholm product, its stable power closure is the classical Selberg length, and the completed scattering coefficient has a two-shift quotient divisor rather than one entire \(\xi\). This is not a Route-A success candidate and must not proceed to Route B.

The obstruction project is nevertheless ready on its stated mathematical scope. The main earlier objections have been resolved by a universal denominator-only rigidity theorem, an exact stable-homogenization theorem, a precise oriented double-coset convention, an explicit PSL cyclic witness, and a zero-free-normalization claim with the correct limited quantifier.

The distinction is essential:

- **External novelty is limited.** Modular scattering, denominator sojourn times, the totient Dirichlet identity, the scattering zeta ratio, Selberg translation length, and Mayer/Selberg transfer operators are established inputs. The work should not be sold as a new scattering theory or a Riemann-zero construction.
- **Route-A value is high.** The package gives a clean termination certificate for a tempting but invalid identification: an open cusp-channel coefficient cannot be promoted unchanged into a same-clock closed primitive-orbit determinant or Hilbert--Pólya candidate.

## Score

| Dimension | Score | Assessment |
|---|---:|---|
| Problem fidelity | 9/10 | The same-object/same-clock bottleneck, non-goals, data restrictions, and source lock are explicit. |
| Method clarity | 9/10 | Open double cosets, closed conjugacy classes, exact repetition, stable closure, and divisor normalization are now cleanly separated. |
| Contribution/newness | 6/10 | The scoped rigidity/closure synthesis is useful, but most endpoints and surrounding theory are classical. |
| Provability | 9/10 | The central claims reduce to exact matrix families, Cayley--Hamilton, and a symbolic divisor argument. |
| Validation quality | 10/10 | A non-importing checker independently verified all six evidence classes and 910 rows at 110 digits; 7/7 tests, including tamper rejection, pass. |
| Route-A value | 9/10 | The work decisively blocks a misleading route and records the positive Selberg closure. |
| **Total** | **52/60** | **Ready as an obstruction/synthesis result, not as a positive Riemann-dynamics candidate.** |

## Review of the theorem package

### 1. Open/closed typing is now correct

The proposal no longer calls \(Pg^nP\) an iteration of an open cusp channel. It uses powers only to test whether the final denominator descends to a closed hyperbolic total period. The normalization \(c>0\), \(d\bmod c\), \(\gcd(c,d)=1\) correctly produces \(\varphi(c)\) oriented algebraic channels at level \(c\). Geometric reversal is not conflated with this ledger.

The exact conjugacy and even-cyclic Gauss-word witnesses establish the intended type failure without relying on a PGL-only shift. This supports a narrow conclusion: a total period depending only on the final denominator is not a conjugacy-class function. It does not assert that every local roof or endpoint-extended cocycle must fail.

### 2. The primary no-go now has the needed quantifier

The strongest repair is Theorem B:

\[
F(|c(g^n)|)=nF(|c(g)|)\quad
\text{for all hyperbolic }g\text{ and }n
\quad\Longrightarrow\quad F\equiv0.
\]

This is materially stronger than showing only that \(2\log|c|\) fails at a few powers. The explicit matrix families cover all positive denominators and require no continuity, monotonicity, or logarithmic ansatz. The finite 400-row certificate is appropriately treated as an implementation audit, not as the proof of the universal statement.

The conclusion remains deliberately narrow: it concerns functions of the **final monodromy denominator alone**. It does not rule out local Birkhoff sums, cohomological corrections, full word chronology, endpoint variables, trace-dependent functions, or matrix-valued cocycles.

### 3. Stable homogenization supplies the sharp positive control

The Cayley--Hamilton identity

\[
c(g^n)=c(g)U_{n-1}(t/2)
\]

and the exact defect formula establish

\[
\lim_{n\to\infty}\frac{2\log|c(g^n)|}{n}=\ell(g).
\]

This prevents the paper from overstating a total disconnect between cusp denominators and closed geodesics. The correct statement is sharper: exact closure fails, while canonical power-stable closure returns to the already-known Selberg clock. Any homogeneous \(L\) with sublinear difference from the denominator powers is therefore fixed to \(\ell\).

### 4. The analytic obstruction is correctly secondary

Using the completed coefficient

\[
\Phi(s)=\frac{\Lambda(2s-1)}{\Lambda(2s)}
\]

avoids confusing the bare totient Dirichlet series with the whole scattering coefficient. Its nontrivial divisor consists of poles at \(\rho/2\) and zeros at \((1+\rho)/2\). Multiplication by a zero-free cusp-normalization factor cannot merge that quotient into a single entire \(\xi\).

This does not exclude determinant factorizations containing additional source-derived factors with their own zeros or poles. Such a factorization would be a different construction and must be evaluated as one; it cannot be hidden in “normalization.”

## Evidence audit

On 2026-08-07 the producer was rerun into a temporary directory, leaving the project artifacts untouched. It exited successfully, and all six regenerated files matched the existing results byte-for-byte.

The frozen evidence includes:

- exact totient counts and unique keys for all \(1\le c\le80\);
- exact preservation of the double-coset key under tested parabolic actions;
- 400 exact rigidity-family rows and 48 exact Chebyshev rows;
- 274 audited Gauss words, with zero literal denominator-square-additivity passes and 259 cyclic denominator variations;
- maximum defect-formula residual \(2.70\times10^{-79}\) at 80-digit precision;
- all finite Dirichlet errors within their declared elementary tail bounds;
- maximum physical-line functional-equation/unitarity residual \(2.11\times10^{-81}\);
- no prime table, zeta-zero list, fitted scale, or fitted offset used.

These computations validate the implementation and normalization. They are not evidence for RH, nor are they a substitute for the exact proofs.

The previously missing independent validation is now complete. `results/independent_check.json` records `PASS`, confirms that the checker does not import the producer, and reports independent verification of six evidence classes at 110-decimal-digit precision. Its row counts are:

- 48 Chebyshev rows;
- 12 Dirichlet rows;
- 80 double-coset rows;
- 274 Gauss-word rows;
- 96 homogenization rows;
- 400 rigidity-family rows;
- **910 rows in total**.

The independent test suite was rerun during final review and passed **7/7** tests. This includes both a producer-import exclusion test and an adversarial tamper test showing that a modified artifact is rejected. Independent certification is therefore affirmative rather than merely a second execution of the producer.

## Route-A ruling

| Layer | Verdict | Reason |
|---|---|---|
| A1 primitive-orbit layer | **A1_FAIL / REFUTED** | The denominator labels oriented open channels but is not an intrinsic closed primitive period. |
| A2 dynamical-zeta layer | **A2_FAIL / REFUTED** | Every exactly homogeneous final-denominator-only clock is trivial; the stable repair changes the system to Selberg length. |
| A3 global analytic layer | **A3_FAIL / REFUTED** | \(\Phi\) has two shifted zeta divisors and is not a zero-free normalization of one entire \(\xi\). |
| A4 liftability layer | **A4_FAIL / NOT_TESTABLE** | No source-derived same-clock quantization, self-adjoint operator, or operator domain is defined. |
| Overall | **ROUTE_A_REJECTED** | Route B is not authorized. |

This negative tuple is exactly the intended output of an obstruction project. “READY” applies to the scoped negative result, not to the candidate’s progress through Route A.

## Remaining issues

There is **no hard mathematical blocker and no remaining computational-validation debt inside the stated final-denominator-only scope**. The promised independent checker has passed with a stronger precision margin than requested and with adversarial tamper rejection.

Release provenance is now frozen at source commit
`54839370e988dd419baafd9fcf8945e7c31d7ea6` and tag `hcs-c17-v1`.

The following are not unresolved defects because they are explicitly outside the theorem’s quantifier:

- endpoint-extended or local/coboundary roofs;
- functions using trace, complete word chronology, or matrix cocycles;
- subadditive pressure or open groupoid traces;
- multi-cusp or \(S\)-arithmetic systems;
- a separately derived self-adjoint operator.

Any one of these may be studied next, but it requires a new candidate definition and source lock. None should be described as already refuted by HCS-C17.

## Publication recommendation

Proceed as a narrowly framed obstruction/synthesis note, a rigorous negative-result section, or a reusable obstruction-registry entry. The strongest defensible contribution is:

> the modular final-denominator clock admits no nontrivial exact homogeneous closed-orbit descent, and its canonical stable closure is precisely Selberg length.

For a major standalone novelty claim, the current package is likely insufficient without either a demonstrably new broader rigidity theorem, a nontrivial extension beyond final-denominator functions, or a new operator/determinant construction. Do not add zero fitting or larger finite censuses to manufacture novelty; they would not address that gap.

**Final recommendation:** accept the project as **READY_AS_SCOPED_OBSTRUCTION**, archive the Route-A decision as **ROUTE_A_REJECTED**, and keep `route_b_invocation_allowed: false`.
