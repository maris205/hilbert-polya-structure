# Paper Plan

**Working title:** *Rational Periodic Multiplier Moduli under Good Reduction:
A Hénon Certificate and Exact Audit*  
**One-sentence contribution:** For finite compositions of monic
area-preserving generalized Hénon maps over an (S)-integer ring, we prove
that every exactly rational periodic-multiplier modulus is a rational
(S)-unit, specialize the result to exclude every rational-prime modulus for
the frozen integral map (H_u), and audit the implementation through exact
period three against a sharp denominator control.  
**Format:** specialist mathematical-dynamics article, 11 pt, author--year
references  
**Type:** theorem plus exact implementation audit  
**Date:** 2026-08-14  
**Target length:** 9--11 pages of main text before references, with full proof
and reproducibility details retained in appendices  
**Section count:** seven main sections plus two appendices

The paper is not framed as a universal symplectic no-go theorem.  Its narrow
purpose is to package a standard good-reduction mechanism into a precise
rational-modulus support certificate and to apply that certificate to one
source-locked nonlinear polynomial symplectic candidate.

## Claims--Evidence Matrix

| Claim | Evidence | Status | Planned location |
|---|---|---|---|
| C1. Every finite complex periodic point of a monic generalized Hénon composition over ‎(mathcal O_{K,S}) is algebraic and (S)-integral. | Projective no-points-at-infinity argument and cyclic non-archimedean maximum lemma in `notes/PROOF_PACKAGE.md`; stable proof IDs in `results/proof_audit.json`. | Proved all periods | Sec. 3 |
| C2. Periodic return monodromies are integral special-linear matrices, so both multipliers are algebraic (S)-units. | Determinant-one derivative product and unit characteristic polynomial; exact products in `results/exact_period_ledger.json`. | Proved all periods | Sec. 3 |
| C3. If a multiplier modulus is exactly (q\in\mathbb Q_{>0}), then (q) is supported only at rational primes below (S); for integral (H_u), (q=1). | Galois-closure/conjugation proof in `notes/PROOF_PACKAGE.md`; scope definitions in the source lock. | Proved all periods | Secs. 3--4 |
| C4. The frozen (H_u(X,Y)=(X^2-u-Y,X)) has no exact rational-prime multiplier modulus at any finite complex periodic orbit, without assuming the multiplier is rational. | C1--C3 plus monicity of (u^3-2u^2+2u-2). | Proved all periods | Sec. 4 |
| C5. Exact period separation and multiplier algebra through (n=3) are internally consistent: five cycles, determinant one, reciprocal unit polynomials, no rational multiplier roots, and exact rational-modulus set ‎({1}). | `candidate_multiplier_audit.json`, `exact_period_ledger.json`, `exact_polynomials.json`; 39 tests. | Verified finite cutoff only | Sec. 5, App. B |
| C6. The good-reduction hypothesis is sharp at the level of allowed support: (a=-15/16) has the fixed multipliers (2,1/2), with coefficient denominator supported at (2). | `control_audit.json`; exact factorization ((L-2)(L-1/2)). | Verified exact control | Sec. 5 |
| C7. Geometry passes but the frozen prime-modulus clock fails A0; downstream zeta, determinant, zero comparison, quantization, and Route B remain closed. | `negative_result_ledger.json`, `run_summary.json`, `EXPERIMENT_RESULTS.md`. | Formal scoped decision | Secs. 6--7 |

## Evidence Boundaries

- The all-period result is deductive.  The period-(1,2,3) ledger is never
  cited as empirical support for an all-period absence.
- Exact rational modulus is not numerical proximity to a rational value.  A
  nonrational algebraic modulus is outside the support conclusion.
- Complex conjugation is not identified with the reciprocal eigenvalue.  The
  proof passes to a finite Galois closure and uses the conjugation-stable set
  of all places above the rational bad-prime support.
- The result does not bound irrational multipliers, spectral radii, singular
  values, or Lyapunov exponents; it does not decide whether (+1) or (-1)
  occurs for the frozen map.
- There is no external prime table, Riemann-zero dataset, zeta fit, or
  quantization stage.

## Structure

### Abstract (180--230 words)

- Begin with the exact theorem and candidate specialization, not generic Hénon
  background.
- Explain the three proof layers: algebraicity/integrality, unit monodromy,
  conjugation-stable rational support.
- Give the concrete finite-audit result: five cycles through period three,
  rational-modulus set ‎({1}), and 39 passing tests.
- Give the sharp control: denominator support ‎({2}) realizes (2,1/2).
- End on the boundary: a good-reduction certificate and candidate rejection,
  not a universal symplectic obstruction.

### 1. Introduction (1.2--1.5 pages)

- Motivate exact periodic multiplier clocks as a stricter obligation than
  generic orbit growth.
- Introduce the global polynomial symplectic Hénon candidate and its arithmetic
  advantage over a singular branch lift.
- State the one-sentence contribution before technical history.
- Present three falsifiable contribution bullets: all-period support theorem,
  frozen no-prime corollary, exact audit plus sharp control.
- Place Figure 1 immediately after the contribution bullets.
- State the A0 failure and scope boundary in the Introduction.

### 2. Arithmetic Hénon context and novelty boundary (1.0--1.3 pages)

Organize by methodological family rather than paper chronology:

1. polynomial automorphism/Hénon normal forms;
2. heights, good reduction, and non-archimedean filtrations;
3. arithmetic periodic points and family questions;
4. multiplier and rigidity results in complex Hénon dynamics.

The section explicitly calls periodic-coordinate integrality and algebraic
unit arguments standard/elementary.  The contribution is their source-locked
rational-modulus support packaging, not a priority claim for those tools.

### 3. The good-reduction rational-modulus certificate (2.0--2.5 pages)

- Define (H_i(X,Y)=(p_i(X)-Y,X)), (F=H_m\circ\cdots\circ H_1),
  (R=\mathcal O_{K,S}), and finite periodic multipliers.
- State the general theorem.
- Main-text proof contains every logical step:
  1. polynomial inverse and determinant one;
  2. projective algebraicity of the cyclic recurrence;
  3. non-archimedean cyclic maximum contradiction;
  4. integral ‎(mathrm{SL}_2) monodromy and reciprocal integrality;
  5. Galois closure and rational (S)-unit support.
- Include a boxed warning that ‎(overline\lambda) need not equal
  (lambda^{-1}).
- Use Figure 1 to make the proof dependency and two support regimes legible.

### 4. Frozen integral Hénon specialization (1.0--1.3 pages)

- Freeze (P(U)=U^3-2U^2+2U-2), the real isolating interval, and
  (H_u).
- Verify global polynomial inverse, determinant one, and algebraic-integral
  parameter.
- State the no-rational-prime-modulus corollary.
- Explain why this is stronger than a rational-eigenvalue statement but
  narrower than an instability or spectral-radius theorem.
- Record Figure 3's Route-A decision and nonclaims.

### 5. Exact implementation audit and controls (1.7--2.0 pages)

- Explain source lock, exact arithmetic, controls-first gate, and the separation
  of formal from exact period.
- Give a compact table for period (1,2,3): points, cycles, trace polynomial,
  multiplier polynomial, rational roots, exact rational moduli.
- Figure 2 visualizes the five-cycle ledger and independent exact checks.
- Present the denominator-(2), integral-(a=0), nonunit-Jacobian, cat-map,
  floating-input, and reporting controls.
- State the 39-test result, CPU-only timing, and memory.

### 6. Interpretation and limits (0.9--1.1 pages)

- Separate what the theorem closes from what remains open.
- Explain the design lesson: a finite bad set cannot supply an unrestricted
  exact rational-prime modulus clock unless those primes are already inserted
  into the coefficients/Jacobian data.
- Discuss why the result is not multiplier rigidity, a general spectral
  theorem, a prime-orbit correspondence, or a quantization result.
- State the formal Route-A stop.

### 7. Conclusion (0.4--0.6 pages)

- Rephrase the exact certificate and frozen rejection.
- Retain the strongest positive point: a genuine global nonlinear polynomial
  symplectic map was audited, and the obstruction survives without assuming a
  rational multiplier.
- Name one admissible next direction: a separately locked mechanism with
  infinite/non-good-reduction support or a genuinely nonalgebraic clock.

### Appendix A. Full proof dependency and (S)-integral boundary

- Restate assumptions in valuation language.
- Record why leading coefficients and Jacobian coefficients outside the unit
  group must be added to the bad set.
- Spell out algebraicity-before-integrality and the Galois-closure repair.

### Appendix B. Exact low-period records and reproducibility

- Display branch decompositions and exact polynomials.
- Give commands, software versions, hashes, tests, compute footprint, and
  forbidden-data declaration.

## Figure and Table Plan

| ID | Type | Description | Frozen data source | Priority |
|---|---|---|---|---|
| Figure 1 | Hero certificate diagram | Left-to-right implication chain from cyclic recurrence to (S)-integral coordinates, ‎(mathrm{SL}_2) monodromy, algebraic-unit multipliers, and rational support; bottom comparison contrasts the integral candidate ((S_\mathbb Q=\varnothing\), (q=1)) with the planted denominator control ((S_\mathbb Q=\{2\}), (q=1/2,2)). | `source_lock.json`, `proof_audit.json`, `control_audit.json`, `negative_result_ledger.json` | HIGH |
| Figure 2 | Exact audit matrix | Periods 1--3 as rows; exact points/cycles and pass markers for recurrence, separation, determinant, cyclic trace, unit norm, rational-root, and exact-modulus checks; a side panel classifies the five cycles in the selected real embedding. | `candidate_multiplier_audit.json`, `exact_period_ledger.json` | HIGH |
| Figure 3 | Boundary/decision map | Compare frozen candidate, planted bad-prime control, nonunit-Jacobian control, and cat-map scope control across geometry, good reduction, exact rational modulus, and permissible conclusion; terminate in the formal Route-A decision. | `control_audit.json`, `scope_audit.json`, `negative_result_ledger.json` | HIGH |
| Table 1 | Theorem/prior-boundary comparison | Good reduction/height work vs. present sparse exact-modulus support question; avoid novelty inflation. | verified bibliography and `NOVELTY_AUDIT.md` | HIGH |
| Table 2 | Exact low-period polynomial ledger | Compact manuscript-readable version of the exact JSON records. | `exact_polynomials.json`, `candidate_multiplier_audit.json` | HIGH |

**Figure 1 draft caption.** The certificate separates the theorem from its
sharp control.  Algebraicity and a cyclic non-archimedean maximum make
periodic coordinates (S)-integral; determinant-one monodromy makes both
multipliers (S)-units; a conjugation-stable Galois closure then restricts an
exact rational modulus to the declared rational bad-prime support.  The
frozen integral map has empty finite support and hence only modulus one,
whereas the denominator-(2) control realizes (1/2) and (2).

## Citation Plan

- **Introduction / normal form:** Friedland--Milnor (1989), Silverman (1994).
- **Arithmetic heights and good reduction:** Kawaguchi (2006, 2013), Ingram
  (2014), Allen--DeMark--Petsche (2018).
- **Arithmetic automorphisms and periodic families:** Marcello (2003),
  Hsia--Kawaguchi (2018), Kim--Krieger--Postolache--Szeto (2024/2025 preprint).
- **Galois/modulus and multiplier boundary:** Dujardin--Favre (2017),
  Cantat--Dujardin (2026 journal article; 2026 multiplier-rigidity preprint).
- No source is cited as prior art for the exact frozen theorem unless its
  primary text supports that statement.  The negative search is described as
  a boundary, never as proof of priority.

## Plan Self-Review

- **Logical flow:** one story: good reduction constrains rational multiplier
  moduli, the frozen integral map is rejected, and the exact audit verifies
  the implementation.
- **Claim/evidence alignment:** every theorem claim maps to the proof package;
  every finite claim maps to a frozen JSON artifact; the controls test each
  assumption boundary.
- **Missing experiments:** none within the source lock.  Higher-period
  enumeration cannot strengthen the all-period theorem and would add cost
  without changing the decision.
- **Positioning:** the plan concedes low standalone novelty and avoids
  competing with height theory or multiplier rigidity.
- **Length feasibility:** the proof receives the largest allocation; exact
  ledger details move to Appendix B if the main text exceeds 11 pages.
- **Front-matter strength:** title, abstract, introduction, and Figure 1 all
  state both the exact conclusion and the denominator-control boundary.

## Production Checklist

- [x] Verify every bibliography record against DOI, publisher, or arXiv.
- [x] Generate three PDF vector figures and PNG review copies from frozen JSON.
- [x] Draft the complete LaTeX manuscript with author--year citations.
- [x] Compile without undefined references/citations or box warnings.
- [x] Create `CLAIM_MANIFEST.json`, `EXPERIMENT_PASSPORT.json`,
  `FIGURE_PACKAGE.json`, `PAPER_CONFIGURATION.md`, `PIPELINE_STATE.json`, and
  `INTEGRITY_PRE_REVIEW.md`.
- [x] Preserve a `paper_pre_review.pdf` snapshot for independent review.
