# HCS-C17 Claim-Driven Experiment Plan

**Candidate:** HCS-C17  
**Decision target:** decide whether the modular cusp denominator can serve as the exact clock of a primitive hyperbolic Euler product, and record the sharp obstruction if it cannot.  
**Frozen date:** 2026-08-07  
**Compute profile:** CPU only; exact integer arithmetic plus 80-decimal-place `mpmath` checks.

## 1. Decision statement

The experiment is not a search for Riemann zeros and is not an operator-construction exercise. It audits one source-locked implication:

\[
\text{oriented cusp channel }P g P
\xrightarrow{\ \tau_P=2\log |c(g)|\ }
\text{closed hyperbolic cycle clock}
\xrightarrow{\text{Euler/Fredholm determinant}}
\xi .
\]

The project succeeds as an obstruction if the first arrow is rigorously impossible for every nonzero final-denominator-only clock, the canonical stable repair is identified, and the scattering divisor cannot be reduced to a single entire \(\xi\) by an allowed zero-free normalization. A successful obstruction is a **Route-A rejection of this candidate**, not a Hilbert--Pólya construction.

## 2. Source lock and data policy

| Item | Frozen choice |
|---|---|
| Group and lifts | \(\Gamma=\mathrm{PSL}_2(\mathbb Z)\), with explicit \(\mathrm{SL}_2(\mathbb Z)\) lifts and trace \(t>2\) for hyperbolic formulas |
| Cusp subgroup | \(P=\Gamma_\infty=\langle T\rangle\) |
| Open object | Oriented nonidentity double cosets \(P\backslash\Gamma/P\), normalized by \(c>0\) |
| Proposed literal clock | \(\tau_P(PgP)=2\log c\), or more generally a total period \(F(|c(g)|)\) depending only on final monodromy denominator |
| Closed object | Primitive hyperbolic conjugacy classes with repetition axiom \(L(g^n)=nL(g)\) |
| Stable positive control | Selberg translation length \(\ell(g)=2\log\lambda(g)\) |
| Scattering normalization | \(\Phi(s)=\Lambda(2s-1)/\Lambda(2s)\), retaining the gamma factor |
| Double-coset cutoff | \(1\le c\le80\) for the finite audit only |
| Numeric precision | 80 decimal digits |
| Allowed data | Exact matrices, totients, recurrence identities, internally evaluated zeta/gamma functions, elementary tail bounds |
| Forbidden data | Prime tables, zeta-zero tables, fitted scales or offsets, target-derived weights |
| Producer | `code/modular_clock.py` |
| Primary artifacts | `results/*.csv`, `results/exact_certificates.json`, `results/summary.json` |

The finite censuses are proof audits. Universal claims are carried by the written matrix arguments and Cayley--Hamilton identities, not by sample size.

## 3. Claim map

| ID | Claim | Required evidence | Decision role |
|---|---|---|---|
| C1 | No nonzero \(F:\mathbb N\to\mathbb R\) can make \(F(|c(g)|)\) an exact homogeneous clock for every modular hyperbolic element; the square law already forces vanishing on the entry-positive subfamily. | Theorem using the positive matrix family \(\gamma_{m,n}\); exact certificates as audit. | Primary obstruction |
| C2 | Stable homogenization of \(2\log|c(g^n)|\) exists and equals \(\ell(g)\). | Chebyshev identity, exact defect formula, high-precision convergence audit. | Sharp positive closure |
| C3 | \(\Phi(s)\) has two shifted zeta divisors and no zero-free cusp normalization converts an affine copy of it into one entire \(\xi\). | Symbolic divisor map; physical-line scattering identities as controls only. | Supporting analytic obstruction |
| C4 | The totient ledger is correctly typed as an oriented open-channel coefficient, not a primitive closed-orbit census. | Exact double-coset classification, orientation convention, conjugacy/cyclic witnesses. | Source-fidelity control |
| C5 | HCS-C17 is rejected as a denominator-only Route-A candidate, while the scoped obstruction package is ready. | C1--C4 pass; claim boundary and exclusions are explicit. | Final ruling |

## 4. Experiment blocks

### E1 — Open-channel classification and typing

- **Claim tested:** C4.
- **Task:** enumerate normalized representatives through \(c=80\); verify that the keys are \((c,d\bmod c)\) with \(\gcd(c,d)=1\), that left/right parabolic actions preserve the key, and that the count at level \(c\) is \(\varphi(c)\).
- **Exact witnesses:** recompute an \(S\)-conjugacy example with different \(|c|\), and the even-shift positive Gauss word witness
  \[
  A_1A_1A_1A_2\sim A_1A_2A_1A_1,
  \qquad |c|=3\text{ versus }4,
  \]
  with an \(\mathrm{SL}_2(\mathbb Z)\) conjugator.
- **Pass criteria:** all 80 counts match; all normalized keys are unique; all tested parabolic actions preserve the key; both conjugacy witnesses are exact integer identities.
- **Failure implication:** repair the PSL/orientation convention before making any clock claim.
- **Artifact:** `results/double_coset_counts.csv`, double-coset and witness sections of `results/exact_certificates.json`.
- **Status:** passed in the current producer run.

### E2 — Universal denominator-only repetition rigidity

- **Claim tested:** C1.
- **Analytic task:** retain the quantified theorem
  \[
  F(|c(g^n)|)=nF(|c(g)|)\quad\forall g\text{ hyperbolic},\ n\ge1
  \quad\Longrightarrow\quad F\equiv0.
  \]
  The proof must state its domain, fixed cusp scaling convention, and matrix families explicitly; it may not infer universality from a census.
- **Audit task:** regenerate the exact positive-family certificates and verify every multiplication and repetition relation in integer arithmetic.
- **Pass criteria:** the symbolic proof covers every positive integer denominator without regularity assumptions on \(F\); all 400 current rigidity-family rows pass exactly; no prime or zero data are read.
- **Failure implication:** any nonzero universal counterexample overturns the primary obstruction. A finite coding bug blocks the numerical certificate but does not by itself refute a correct proof.
- **Artifact:** `results/exact_certificates.json`, `results/summary.json`.
- **Status:** theorem present and producer audit passed.

### E3 — Cayley--Hamilton identity and stable closure

- **Claims tested:** C2 and the closed-clock positive control.
- **Task:** for frozen hyperbolic samples and powers, verify exactly
  \[
  c(g^n)=c(g)U_{n-1}(t/2),
  \]
  then evaluate
  \[
  2\log|c(g^n)|
  =n\ell(g)+2\log\frac{|c(g)|}{\sqrt{t^2-4}}
   +2\log(1-\lambda^{-2n}).
  \]
- **Compared systems:** literal denominator height; its power-normalized value; exact Selberg length.
- **Metrics:** exact recurrence equality; maximum formula residual; terminal \(|2\log|c(g^n)|/n-\ell(g)|\) at \(n=24\).
- **Pass criteria:** all 48 exact Chebyshev rows pass; the 80-digit defect residual is below \(10^{-60}\); each frozen sample has terminal error below \(0.12\); the analytic limit proof is present.
- **Failure implication:** an exact recurrence failure is fatal; slow finite-\(n\) convergence is reported rather than fit away.
- **Artifact:** `results/homogenization.csv`, `results/summary.json`.
- **Status:** passed; current maximum formula residual is approximately \(2.70\times10^{-79}\), and the largest terminal error is approximately \(0.1015\).

### E4 — Scattering normalization and divisor obstruction

- **Claim tested:** C3.
- **Task:** retain the complete coefficient \(\Phi(s)=\Lambda(2s-1)/\Lambda(2s)\); prove symbolically that a nontrivial zero \(\rho\) contributes a pole at \(\rho/2\) and a zero at \((1+\rho)/2\), with no cancellation; classify cusp-rescaling factors as zero-free exponentials.
- **Numerical controls:** at frozen points with \(\Re s>1\), compare finite totient sums to the zeta ratio using an explicit elementary tail bound; on \(s=1/2+it\), check unitarity and the functional equation at \(t=0.7,2,7\).
- **Pass criteria:** every Dirichlet error lies below its declared tail bound; maximum physical-line residual below \(10^{-70}\); no zero list is loaded; the no-go is limited to zero-free normalization and affine reparametrization.
- **Failure implication:** a normalization with zeros/poles is a different determinant factorization and must be source-derived rather than silently absorbed.
- **Artifact:** `results/dirichlet_convergence.csv`, `results/summary.json`.
- **Status:** passed; current maximum functional-equation/unitarity residual is approximately \(2.11\times10^{-81}\).

### E5 — Independent release audit

- **Claim tested:** reproducibility of C1--C4, not their discovery.
- **Task:** implement a clean checker that does not import the producer, shares no matrix or recurrence helpers with it, reads only the frozen source lock, and compares normalized JSON/CSV outputs.
- **Required checks:** exact double-coset counts; both PSL witnesses; rigidity-family relations; Chebyshev identities; defect formula; scattering controls; forbidden-data audit.
- **Pass criteria:** exact fields and integer certificates agree; high-precision fields agree to at least 60 decimal digits; any intentional ordering difference is normalized and documented.
- **Current status:** **PASSED**. The non-importing checker independently recomputed six evidence classes at 110 decimal digits and verified 910 rows: 48 Chebyshev, 12 Dirichlet, 80 double-coset, 274 Gauss-word, 96 homogenization, and 400 rigidity-family rows.
- **Adversarial control:** the test suite passed 7/7 tests, including explicit rejection of a tampered result artifact and a source check that rejects producer imports.
- **Artifact:** `results/independent_check.json`.
- **Decision effect:** the promised independent computational certification is complete; no validation debt remains for the scoped obstruction package.

## 5. Current evidence snapshot

A clean rerun on 2026-08-07 wrote only to a temporary directory and exited successfully. All six generated files matched the checked-in result artifacts byte-for-byte:

- `dirichlet_convergence.csv`
- `double_coset_counts.csv`
- `exact_certificates.json`
- `gauss_word_clock_audit.csv`
- `homogenization.csv`
- `summary.json`

The current snapshot records 80 double-coset levels, 400 rigidity-family rows, 48 Chebyshev rows, 274 Gauss-word rows, and no prime or zero tables. Of the 274 Gauss words, none passes literal denominator-square additivity; 259 show cyclic denominator variation. These counts illustrate the obstruction but do not establish its universal quantifier.

The independent checker subsequently passed at 110-decimal-digit precision. It verified all six artifact classes and all 910 recorded rows without importing the producer. The associated test suite passed 7/7 tests, including tamper rejection. The machine-readable report is `results/independent_check.json`.

## 6. Run order and stopping rules

1. Freeze source lock and hash/commit provenance.
2. Run E1 and reject the run immediately if orientation or representative normalization changes.
3. Check the written proof of C1, then run E2 as a certificate audit.
4. Run E3; an exact identity failure stops the evaluation.
5. Run E4 with the full completed scattering factor.
6. Run E5 before archival release; require a `PASS` report and successful tamper rejection. **Completed.**
7. Emit the Route-A YAML only from frozen artifacts and theorem statuses.

No randomized/shuffled-period control is decision-relevant here: there is no fitted orbit-to-zero match to stress-test, and the candidate is rejected analytically before spectral fitting. If a future candidate introduces fitted weights, target zeros, or approximate determinant matching, the full Route-A randomization suite becomes mandatory under a new source lock.

## 7. Explicit exclusions and follow-up boundary

The present plan does **not** test endpoint-extended roofs, matrix-valued cocycles, cohomological/local Birkhoff sums, subadditive pressure, open groupoid traces, multi-cusp systems, or separately derived self-adjoint operators. Any such proposal is a new candidate, not a repair silently covered by HCS-C17.

The next scientifically meaningful step is therefore not a larger cutoff or a zero fit. It is either:

1. replace the pending release-provenance placeholders, freeze the verified artifacts, and archive HCS-C17 as a proved negative structural prior; or
2. define one excluded extension with a new source lock and prove that its period sum, determinant convention, and analytic divisor belong to the same object.

## 8. Planned presentation

- **Main table:** claim-to-evidence matrix C1--C5 with theorem/numerical status.
- **Main figure (optional):** \(2\log|c(g^n)|/n-\ell(g)\) versus \(n\) for the four frozen examples, with the exact defect curve rather than a fitted asymptotic.
- **Main negative diagram:** open double-coset ledger \(\rightarrow\) failed denominator-only descent \(\rightarrow\) stable Selberg closure.
- **Claim language:** “scoped denominator-clock obstruction and stable closure,” never “new modular scattering theory,” “Riemann-zero construction,” or “Hilbert--Pólya operator.”
