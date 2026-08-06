# Experiment Plan

**Problem**: The certified four-state survivor of the area-preserving Hénon map has an exact finite-state symbolic model, but its unit-step clock has a vertically periodic divisor and cannot supply Riemann--von Mangoldt growth. Determine whether the intrinsic periodic instability lengths admit a positive roof that removes that lattice-periodicity obstruction and yields reproducible complex dynamical-determinant data.

**Method thesis**: On the certified survivor of
\[
H_6(x,y)=(1-6x^2-y,x),
\]
the roof \(\tau=\log J^u\) is positive, its primitive periods are \(T_p=\log|\Lambda_{u,p}|\), and its untwisted/orientation-twisted cycle determinants can be evaluated without prime tables, zero tables, parameter fitting, or planar Ulam discretization.

**Date**: 2026-08-05

## Claim Map

| Claim | Why it matters | Minimum convincing evidence | Linked blocks |
|---|---|---|---|
| C1: The instability spectrum has a positive Hölder representative, intrinsic up to coboundary, and is non-lattice on the certified survivor. | It is the smallest natural modification that can escape the exact vertical periodicity of the unit clock while retaining genuine Hénon orbit information. | Exact positivity bound; two explicit primitive periods with a proof of irrational ratio; exact repetition law. | B1, B2 |
| C2: The corresponding finite cycle sections have a preregistered cutoff-stable family of zeros, or else expose a reproducible obstruction. | Stable roots are required before any stronger spectral interpretation; drift is itself a useful negative result. | Independent primitive-product and trace-recursion implementations; frozen validation and sealed test cutoffs; numerical winding counts; precision and adversarial controls. | B3, B4, B5 |

Anti-claims to rule out:

- apparent roots are just the unit-clock lattice towers;
- roots arise from one finite Euler product rather than the stated degree-cutoff cycle section;
- roots are artifacts of one recurrence implementation, floating-point precision, or an incomplete orbit catalogue;
- stability persists equally under shuffled periods, shuffled lengths, random weights, or random phases;
- a stable dynamical resonance is a Riemann zero or a Hilbert--Pólya eigenvalue.

## Frozen Source Lock

- Candidate: the explicit local survivor \(\Lambda_*\) of \(H_6\) defined by the four-state adjacency matrix
  \[
  A=\begin{pmatrix}
  1&0&1&0\\
  1&0&0&0\\
  0&1&0&1\\
  0&1&0&0
  \end{pmatrix}.
  \]
- Scope: \(H_6|_{\Lambda_*}\), not the full Hénon nonwandering set.
- Clock: \(T_p=\log|\Lambda_{u,p}|\), with no affine rescaling or unfolding.
- Orientation character: \(\sigma_p=\operatorname{sgn}(\Lambda_{u,p})\); evaluate \(\kappa=0,1\) separately.
- Determinant convention:
  \[
  D_\kappa(s;z)=\prod_p\bigl(1-\sigma_p^\kappa e^{-sT_p}z^{n_p}\bigr),
  \qquad
  D_{\kappa,N}(s)= [D_\kappa(s;z)]_{\deg z\le N}\big|_{z=1}.
  \]
  This is one cycle-section ledger. It is not the finite Euler product at \(z=1\), the smooth Perron flat determinant, a Ulam determinant, or a completed xi function.
- Orbit precision: 80 decimal digits for production contraction/monodromy; float64 is an independent implementation check only.
- Determinant/root precision: float64 discovery followed by 80-decimal residual checks.
- Data split:
  - development: primitive periods \(1\le n\le8\);
  - frozen validation: \(9\le n\le12\);
  - sealed test: \(13\le n\le16\);
  - post-test robustness only: \(17\le n\le20\).
- Root-count rectangle:
  \[
  \mathcal R=\{s:-0.25\le\Re s\le0.30,\ |\Im s|\le20\}.
  \]
- Training root set: roots of \(D_{\kappa,8}\) in \(\mathcal R\) that match a \(D_{\kappa,7}\) root within \(2\times10^{-2}\) and lie at least \(10^{-2}\) from the contour.
- Frozen matching threshold: \(2\times10^{-2}\) in the complex plane.
- Argument-principle audit: contour sample counts \(4096,8192,16384\) must agree; report the minimum boundary modulus and maximum unwrapped phase step.
- Precision gate: every reported root must have 80-digit determinant residual below \(10^{-30}\), and the two coefficient implementations must agree below \(10^{-30}\) at high precision (with the float64 discrepancy also reported).
- Validation stability target: at least 90% of training roots retained; median matched drift below \(2\times10^{-3}\), 90th percentile below \(10^{-2}\).
- Sealed-test stability target: at least 90% of validation-retained roots retained; median matched drift below \(10^{-3}\), 90th percentile below \(5\times10^{-3}\).
- Leading real root target for \(\kappa=0\): \(|h_{12}-h_{10}|<10^{-5}\) on validation and \(|h_{16}-h_{12}|<10^{-5}\) on test. No target value was fitted.
- Allowed inputs: repository definitions of the certified survivor and its period-12 catalogue for development/validation cross-checks.
- Forbidden inputs: prime tables, primality labels, Riemann-zero tables, xi/zeta evaluations, target spectral fitting, test-set normalization changes.
- Random-control seeds: 20260805, 20260806, 20260807.
- Neighbor controls: \(a=5.9\) and \(a=6.1\), using the same symbolic words and numerical contraction; these are controls, not certified common-survivor theorems.

## Paper Storyline

- Main paper must establish the clock triage theorem and report the frozen root-stability result honestly.
- Appendix can contain enumeration proofs, exact algebraic calculations, argument-principle diagnostics, and full control tables.
- Explicitly cut: Riemann-zero matching, prime matching, learned roofs, parameter optimization, spatial Ulam matrices, and Route-B operator claims.

## Experiment Blocks

### B1: Exact clock triage

- Claim tested: C1.
- Why: unit map time is lattice; a candidate suspension needs a positive non-lattice roof.
- Systems: unit roof, generating-function action, unstable-Jacobian roof.
- Metrics: positivity, repetition additivity, lattice/non-lattice status.
- Success criterion: prove \(\tau>0\) on \(\Lambda_*\) and prove two primitive instability periods have irrational ratio.
- Failure interpretation: if the instability periods are commensurable, the candidate retains the lattice obstruction.
- Target: main theorem/table.
- Priority: MUST-RUN.

### B2: Complete high-period orbit ledger

- Claim tested: C1 and the A1 prerequisites for C2.
- Why: the exact SFT permits complete primitive-necklace enumeration without full two-shift homotopy.
- Split: periods 1--8 / 9--12 / 13--16 / 17--20.
- Metrics: primitive counts, recurrence residual, contraction convergence, determinant-one error, hyperbolicity margin, period-12 word/multiplier agreement with the prior certified catalogue.
- Success criterion: exact symbolic counts, no duplicate rotations, all numerical roots converged and hyperbolic, period-12 bridge agrees to the frozen tolerance.
- Failure interpretation: no determinant result may be promoted if the orbit ledger fails.
- Target: main catalogue summary plus appendix CSV.
- Priority: MUST-RUN.

### B3: Untwisted and orientation-twisted cycle sections

- Claim tested: C2.
- Why: \(\kappa=0\) tests the geometric suspension; \(\kappa=1\) preserves the intrinsic unstable-orientation cancellation.
- Compared systems: \(D_{0,N}\), \(D_{1,N}\), and the exact constant-roof parent.
- Metrics: leading real root (when present), matched-root drift, retained fraction, root count in \(\mathcal R\), conjugation residual, contour diagnostics.
- Success criterion: pass the frozen validation/test stability thresholds, or record a precise cutoff obstruction.
- Failure interpretation: stable finite-period roots are absent; the candidate remains a useful negative clock result only.
- Target: main finite-section-zero table and complex-plane figure.
- Priority: MUST-RUN.

### B4: Independent implementation and precision audit

- Claim tested: C2.
- Why: primitive multiplication and trace/cumulant recursion must produce the same cycle section.
- Metrics: coefficient/determinant discrepancy at fixed complex probes and roots; 80-digit residuals; argument-principle count agreement under contour refinement.
- Success criterion: pass the frozen precision gate and reproduce every reported count.
- Failure interpretation: numerical result is NOT_TESTABLE.
- Target: reproducibility appendix.
- Priority: MUST-RUN.

### B5: Adversarial controls and nearby parameters

- Claim tested: anti-claims.
- Compared systems:
  - shuffled period labels;
  - globally shuffled instability lengths;
  - same-density random lengths;
  - positive random factor weights;
  - random complex phases;
  - constant-roof symbolic parent;
  - numerical continuations at \(a=5.9,6.1\).
- Metrics: retained-root fraction relative to the Hénon training roots, drift distribution, root count, conjugation failure where expected, and leading-root movement.
- Success criterion: report all controls, not only favorable ones. No requirement that Hénon outperform every control; the comparison diagnoses which stability comes from symbolic completeness versus the geometric roof.
- Failure interpretation: if random controls are equally stable, cutoff stability alone has little discriminating value.
- Target: control table/appendix.
- Priority: MUST-RUN.

## Run Order and Milestones

| Milestone | Goal | Runs | Decision gate | Cost | Risk |
|---|---|---|---|---|---|
| M0 | Exact and software sanity | B1 derivations; primitive counts through 8; two determinant implementations | Exact identities and unit tests pass | CPU minutes | sign/state convention error |
| M1 | Development | build periods 1--8; discover/freeze roots from 7--8 | training roots and contour are well separated | CPU minutes | contour too close to a root |
| M2 | Validation | open periods 9--12; compare prior catalogue | validation gates pass or negative result is recorded | CPU minutes | reused catalogue mismatch |
| M3 | Sealed test | first compute periods 13--16 after protocol hash is stored | frozen test gates evaluated unchanged | CPU minutes | new roots enter the contour |
| M4 | Robustness | extend to 20; run controls and neighbors | interpretations unchanged or explicitly revised | CPU minutes to under one hour | control computation dominates |
| M5 | Documentation | Route-A YAML, paper draft, manifest, tests | every number regenerates from one command | CPU minutes | provenance gaps because checkout has no `.git` metadata |

## Compute and Data Budget

- GPU hours: 0.
- CPU: expected below one hour for periods through 20 and all controls.
- External data: none.
- Biggest bottleneck: reliable complex-root census and boundary-safe argument counts, not orbit enumeration.

## Risks and Mitigations

- Finite cycle sections may show stable spurious roots: report the exact determinant convention and do not infer analytic continuation without a tail theorem.
- A root may lie near the frozen contour: report boundary modulus; do not move the contour after validation.
- Non-lattice does not imply Riemann-compatible zero growth: assess A3 separately and retain failure status.
- The neighbor maps are not certified on a common h-set family: label their evidence numerical only.
- The current workspace is not a Git worktree: store hashes and a repository-update manifest rather than inventing a commit ID.

## Final Checklist

- [x] Main claims and anti-claims frozen
- [x] Clock, determinant, precision, splits, contour, controls, and forbidden data frozen
- [x] Symbolic catalogue extended independently through period 20
- [x] Three-resolution numerical winding audits complete
- [x] Mandatory controls complete, including unresolved sampler failures
- [x] Route-A evaluation saved
- [x] Paper, project README, independent checker, and handoff complete
