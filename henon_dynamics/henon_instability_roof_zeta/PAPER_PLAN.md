# Paper Plan

**Working title:** *A Non-Lattice Instability Clock on a Certified Hénon Survivor*  
**One-sentence contribution:** On an explicit hyperbolic survivor of the area-preserving Hénon map, we prove that unstable expansion supplies a positive non-lattice suspension clock, then show under a target-free frozen protocol that its cycle-section zeros stabilize through period 20 while the Hilbert--Pólya analytic requirements remain unmet.  
**Type:** mathematical research note with a reproducible numerical audit  
**Date:** 2026-08-05  
**Venue:** technical report; no venue-specific page claim

## Claims--Evidence Matrix

| Claim | Evidence | Status | Section |
|---|---|---|---|
| The unit clock has a vertically periodic divisor with linear zero-count growth in every bounded real strip. | Exact determinant `1-z-z^3-z^4`, substitution `z=e^{-s}`, compactness in one period strip. | PROVED | §4 |
| The stored generating-function action is not a positive roof. | Exact period-four orbit with total action zero. | PROVED | §4 |
| The instability clock is positive and non-lattice. | Inherited cone bound `J^u >= 773/224`; exact degree-four and degree-two multiplier polynomials; distinct-conjugate degree argument. | PROVED on the local survivor | §4, Appendix A |
| The finite cycle sections have a preregistered cutoff-stable family of zeros in the frozen rectangle. | Complete catalogues through period 20; two coefficient implementations; three-resolution numerical winding counts; 80-digit residuals; development/validation/sealed/robustness splits. | NUMERICAL_OBSERVATION | §6 |
| The observed coefficients exhibit structured cancellation relative to the frozen orbit-level controls. | Frozen random-weight, phase, length, shuffle, constant-roof, and neighboring-parameter controls. | NUMERICAL_OBSERVATION | §6 |
| The construction does not yet yield a Hilbert--Pólya structure. | No limiting determinant theorem, continuation, functional equation, Riemann--von Mangoldt count, prime correspondence, or self-adjoint operator. | OPEN / obstruction | §7 |

## Structure

### §0 Abstract

- State the positive non-lattice theorem first.
- Explain the target-free cycle-section test and its complete period-20 orbit ledger.
- Report the 43-root census, sealed drift, coefficient tail, and strongest control contrast.
- End with the negative Route-A conclusion.

### §1 Introduction

- Motivate clock selection as a prior obligation in dynamical Hilbert--Pólya programs.
- Separate the exact clock theorem from the numerical resonance audit.
- State three falsifiable contributions and the claim boundary.

### §2 Related context

- Dynamical zeta functions and suspensions.
- Cycle expansions and shadowing cancellations.
- Hénon periodic dynamics and the inherited certified local subsystem.
- Position this note as a clock/divisor audit, not a new global horseshoe theorem.

### §3 Certified survivor and determinant convention

- Define `H_6`, the four-state adjacency matrix, and the inherited conjugacy.
- Define the unstable Jacobian, orbit lengths, orientation character, and repetition law.
- Freeze the degree-in-`z` cycle section before setting `z=1`.

### §4 Clock triage theorem

- Prove the unit-clock periodicity obstruction.
- Reject the action roof with the exact period-four cycle.
- Prove positivity and non-lattice instability time.
- Explain precisely what non-lattice does and does not imply.

### §5 Reproducible experiment

- Describe exact necklace enumeration and contraction lifting.
- Give development, validation, sealed-test, and robustness periods.
- Explain independent determinant implementations, root discovery, argument counts, high-precision refinement, and frozen controls.

### §6 Results

- Catalogue and numerical gates.
- Root counts and cutoff drift for both orientation sectors.
- Positive real finite-section-zero convergence.
- Control and neighboring-parameter analysis.
- Distinguish numerical consistency from a theorem about a limiting divisor.

### §7 Route-A implications

- A1: exact local orbit ledger but no prime correspondence.
- A2: stable internal finite-section family, no Riemann target test.
- A3: failure due to missing global analytic structure and counting law.
- A4: suspension is formal dynamical structure, not an operator realization.

### §8 Conclusion

- The main positive output is the exact non-lattice roof.
- The main negative output is that strong finite-section stability is not an arithmetic signature.
- Name a cylinder-transfer determinant and a uniform Rouché tail bound as next tests.

### Appendix A: Exact algebra

- Period-four recurrence, action, monodromy, multiplier polynomial.
- Fixed-point multiplier polynomial and distinct-conjugate argument.
- Orientation-twisted unit-roof factorization.

### Appendix B: Reproducibility and artifact audit

- Full root and control tables.
- Hashes, software versions, and reproduction commands.

## Figure and Table Plan

| ID | Type | Content | Data source | Priority |
|---|---|---|---|---|
| Figure 1 | two-panel line/bar plot | Cutoff convergence of the positive root; log-scale cycle-tail ratios for valid controls. The contrast shows stable Hénon cancellation but also the stronger exact constant-roof cancellation. | `results/analysis_summary.json` | HIGH |
| Table 1 | mathematical comparison | Unit time, action, and instability time: positivity, lattice status, and consequence. | exact audit | HIGH |
| Table 2 | numerical audit | Root census, drift gates, residuals, and coefficient discrepancy. | `results/analysis_summary.json` | HIGH |
| Table 3 | controls | Root retention and tail ratios, including NOT_TESTABLE labels. | `results/control_summary.csv` | HIGH |

**Figure 1 caption draft:** The instability roof produces stable finite cycle sections, but stability alone is not arithmetic evidence. Left: the untwisted positive real zero stabilizes by cutoff 14. Right: valid randomized orbit controls have degree-9--16 coefficient tails between \(2.9\times10^4\) and \(3.2\times10^5\) times the Hénon tail, whereas the exact constant-roof parent is smaller still. No fitted curve or external arithmetic target is used.

## Citation Plan

- Ruelle's expanding-map/Anosov-flow zeta framework.
- Thermodynamic formalism for Hölder potentials and suspension flows.
- Cycle-expansion literature on shadowing cancellation.
- The original Hénon map and the companion local-survivor certificate.
- Recent marked-multiplier rigidity only as context, not as support for the theorem proved here.

Every external entry must be copied from a verified bibliography or fetched from a primary DOI/arXiv record. The companion survivor theorem is cited as an internal, hash-addressed dependency rather than given a fictional publication record.

## Review Questions

- Does the non-lattice proof justify degree preservation for every positive power of the fixed multiplier?
- Is every finite-section statement labeled numerical rather than limiting?
- Is the argument-principle audit clearly described as high-precision numerical evidence rather than interval certification?
- Does the discussion avoid implying a Riemann-zero or prime match?
