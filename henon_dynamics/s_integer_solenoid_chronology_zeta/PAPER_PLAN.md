# Paper plan

**Working title:** Chronology Changes Analytic Type in a Dyadic-Solenoid
Skew Product

**One-sentence contribution:** We construct an explicit noncommuting
two-symbol automorphism cocycle on the dyadic two-solenoid for which two
primitive words with the same letter counts have rational and
natural-boundary return zeta functions, while the full switching zeta still
continues meromorphically and without zeros across its first convergence
circle.

**Paper type:** theorem-led arithmetic dynamics with exact computation

**Target:** standalone mathematical-dynamics preprint rather than an ML
conference template

**Date:** 2026-08-06

**Main-body budget:** 12--14 pages, with detailed proofs and reproducibility
material in an appendix

## Narrative decision

The paper tells one story: **chronological noncommutativity can survive all the
way to the analytic type of orbit-resolved zeta factors, yet global summation
can erase that obstruction at the leading circle.**  The Hilbert--Pólya
evaluation is a falsification layer, not the novelty claim.

The source paper *An Area-Preserving H\'enon-Map Model for the Riemann Zeros*
is used as the starting structural question.  Its durable premise is that a
candidate spectral host should be conservative and genuinely dynamical.  We
do not inherit its numerical zero comparison, continuum Hamiltonian, fitted
parameters, or claim that area preservation alone supplies an operator.
Instead, we change dynamical form: the smooth planar H\'enon family is replaced
by an autonomous chronological skew product of Haar-preserving compact-group
automorphisms, for which periodic weights and zeta functions are intrinsic and
exact.

## Claims--evidence matrix

| ID | Claim | Evidence | Status | Main location |
|---|---|---|---|---|
| C1 | Every chronological return has a finite intrinsic fixed group of order \(\operatorname{oddpart}(\det(I-M_w))\). | Expansion bound, Pontryagin duality, Smith localization; exact tests. | Proved | Sections 3 and A.1 |
| C2 | The words receiving a nontrivial dyadic correction are exactly the cyclic golden-mean language. | Complete mod-2 semigroup argument and exhaustive check through period 12. | Proved | Section 4 |
| C3 | Equal-Parikh primitive chronology can change zeta analytic type. | Exact period-five matrices; parity split; Bell--Miles--Ward applied separately to each return map. | Proved | Section 5 |
| C4 | The full switching zeta crosses its first convergence circle, has one simple pole and no zeros in a larger disk. | Exact rational archimedean comparison and \(\lim \Delta_n^{1/n}=8\varphi\). | Proved | Section 6 |
| C5 | Every fixed congruence depth admits a finite chronological transfer recurrence, whereas the exact odd-part weight requires the full depth tower. | Exact coefficient identity and finite-monoid/direct-enumeration agreement through depth 8. | First clause proved; minimality of an infinite-state realization not claimed | Section 4 and A.3 |
| C6 | The construction does not pass Route A as a Hilbert--P\'olya candidate. | No prime clock, Riemann divisor, functional equation, or discrete self-adjoint realization; formal evaluation record. | Scoped negative ruling | Section 7 |

## Section plan

### Abstract

- Open with the period-five analytic-type split, not generic RH background.
- State the phase space and fixed-point weight in one sentence.
- Give the two exact fixed counts \(30035\) and \(15021\).
- State the global continuation radius \((8\varphi)^{-1}>1/16\).
- End with the interpretation: local natural boundaries need not survive
  global chronological aggregation, and the resulting system is not an
  HP construction.

### 1. Introduction: from conservative H\'enon dynamics to exact orbit data

- Start from the concrete gap in the source H\'enon paper: conservativity is a
  useful gate, but numerical spectra do not identify an intrinsic periodic
  determinant.
- Explain the breadth-first pivot to an exact Haar-preserving solenoid cocycle.
- State the chronological convention before any result.
- Present four falsifiable contributions corresponding to C1--C4.
- Preview both sides of the result: the primitive analytic-type split and the
  global first-circle cancellation.
- State Route-A failure early enough to prevent an RH overclaim.

### 2. Background and positioning

- H\'enon/area-preserving motivation and why this paper changes dynamical
  category.
- Periodic points of \(S\)-integer and finite-dimensional solenoid
  automorphisms.
- Rational versus natural-boundary dynamical zeta functions in algebraic
  dynamics.
- Semigroup actions and full-shift skew products.
- Position the novelty as the exact combination, not any ingredient alone.

### 3. The chronological dyadic-solenoid system

- Define \(R=\mathbb Z[1/2]\), \(X_2=\widehat{R^2}\), the two matrices, and
  \(F(\omega,x)=(\sigma\omega,\alpha_{M_{\omega_0}}x)\).
- Freeze later-symbols-on-the-left multiplication.
- Prove uniform expansion and positivity of \(D_w\).
- Prove the fixed-point index formula over the localized PID.
- Derive the rational archimedean comparison without replacing chronology by
  an averaged orbit.

### 4. Symbolic parity and the congruence transfer tower

- Reduce the generators modulo 2 to \(J\) and \(E\).
- Prove the cyclic no-\(aa\) iff theorem and Lucas count.
- Derive the odd-part layer identity.
- Define the finite monoid recurrence at each modulus \(2^k\), including both
  residue-state counts and integer matrix sums.
- Include a compact table of the first ten periodic counts and corrected-word
  counts.

### 5. Chronology changes analytic type

- Establish the primitive-necklace factorization and correct repetition law.
- State the trace-parity dichotomy for an arbitrary primitive return.
- Give the two period-five witnesses in a side-by-side table.
- Apply Bell--Miles--Ward only to the odd-trace return automorphism.
- Prove the repetition valuation law.
- Emphasize that equal letter incidence cannot recover orbit-resolved analytic
  type.

### 6. The full zeta crosses its first circle

- Define \(N_n^{(\infty)}\), \(N_n^{(2)}\), and \(\Delta_n\).
- Prove \(\lim \Delta_n^{1/n}=8\varphi\).
- Factor \(Z_2=Z_\infty e^{-G}\) and locate all divisors in the proved disk.
- State the exact conclusion: one pole at \(1/16\), no zeros for
  \(|z|<(8\varphi)^{-1}\).
- State what remains open at the secondary circle.  Do not infer a global
  natural boundary from individual primitive factors.

### 7. Hilbert--P\'olya evaluation and conclusion

- Evaluate the frozen object under Route A:
  \((\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},\mathrm{A3\_FAIL},
  \mathrm{A4\_FORMAL\_HINT})\).
- Separate the proved arithmetic-dynamics contribution from the rejected HP
  interpretation.
- Identify one theorem-sized continuation question and one genuinely different
  fallback system: a nonabelian congruence voltage-graph/Ihara tower with the
  trivial sector removed.

### Appendix

- Full Smith-localization and expansion proofs.
- Full parity-language proof and finite-monoid recurrence.
- Natural-boundary hypothesis audit.
- Exact algorithms, independent implementation, Dold checks, and artifact
  hashes.

## Main tables and visual summary

The paper will use tables rather than a decorative figure because the decisive
comparison is exact and two-column:

1. **Table 1 (front-matter summary):** source H\'enon model versus the present
   solenoid skew product: phase space, conservation law, clock, periodic
   weights, operator status, and epistemic status.
2. **Table 2:** the period-five equal-Parikh witnesses, including matrices,
   traces, dyadic valuations, fixed counts, and analytic types.
3. **Table 3:** periodic counts \(N_n^{(\infty)}\), \(N_n^{(2)}\),
   \(\Delta_n\), and Lucas active-word counts for \(1\le n\le10\).
4. **Table 4:** Route-A verdict with strongest evidence and failure for each
   gate.

## Citation plan

- Introduction: the local source PDF; H\'enon's original area-preserving map;
  a restrained Hilbert--P\'olya context citation.
- Background/setup: Chothi--Everest--Ward, Lind--Ward, Miles, and the
  rank-two treatment of Ha--Lee.
- Analytic-type theorem: Bell--Miles--Ward, with theorem and scope checked
  against the primary manuscript.
- Broader fixed-count/zeta framework: Byszewski--Cornelissen--Houben, while
  explicitly separating their FAD setting from the switching theorem here.
- Skew-product positioning: Carvalho--Rodrigues--Varandas.
- Only cited, independently verified entries will enter `references.bib`.

## Claim boundaries frozen before drafting

- The full switching zeta is not proved rational or nonrational.
- No natural boundary is proved at \(|z|=(8\varphi)^{-1}\).
- A natural boundary for one primitive return factor does not imply one for
  the infinite primitive product.
- The finite-prefix recurrence screen is evidence only.
- No Riemann zeros, primes, or fitted spectral data enter the construction.
- Haar-preserving compact-group dynamics is not identified with smooth planar
  area preservation, and neither property alone supplies a Hilbert--P\'olya
  operator.

## Review gate before release

- Independent algebra/code rerun with exact artifact comparison.
- Adversarial theorem review of the continuation disk and BMW hypotheses.
- Primary-source bibliography audit, including the source H\'enon PDF.
- Compile with zero undefined references/citations and no unreviewed claim
  markers.
