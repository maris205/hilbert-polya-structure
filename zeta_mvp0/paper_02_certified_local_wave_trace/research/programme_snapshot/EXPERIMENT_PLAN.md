# Claim-Driven Experiment Plan

## Claim map

| Claim | Primary test | Control | Pass condition |
|---|---|---|---|
| The centered \(a=1.02\) Hamiltonian flow is active | R000/R001 FTLE and SALI | exact radial \(a=0\), high-distortion \(a=6\) | nonlinear plateau with SALI collapse; radial exponent decays and SALI remains order one |
| The signal is not a Verlet artifact and survives \(B=1\) | R106 DOP853 | same frozen physical states at \(a=0\) and \(1.02\) | drift, flag, and cross-integrator ratio gates pass |
| The scalar spectrum is orthogonal-like in the tested window | R100--R102 adjacent ratios and CDFs | grid sequence, radial degeneracy, \(a=6\) failure control | level and ratio convergence before class language |
| Fixed magnetic coupling produces a resolved response | R103/R104 frozen field grid | \(B=0\), coarse/fine recomputation | all new fields above baseline and convergence gates pass |
| The result is not second-order dispersion | R107/R107A fourth-order covariant stencil | archived FD2 extrapolation | level, mean-ratio, correlation, residual, and orthogonality gates pass |
| The relative spectrum may host stable nonzero-time structure | R200-S implementation passed; production not run | mesh/box/window/smoothing changes and radial families | current smoke peaks fail grid stability; only future stable, orbit-verified features may survive |
| The warped well has an isolated local period/action carrier | R400 near-bottom Lyapunov continuation | exact Hessian, normal-form slopes, radial off-integer window, independent solver | all classical gates pass before any quantum trace is viewed |

## Completed production runs

- R000: classical zero-input screen (the frozen \(a=1.02\) parameter itself
  has an earlier zero-exposed lineage).
- R001: time-length convergence.
- R100: initial quantum grid comparison; failed the 1% gate.
- R101: third grid and post-hoc spacing-stability diagnostic.
- R102: fourth core grid and \(h^2\) extrapolation.
- R103: preregistered magnetic scan.
- R104: second-grid crossover check.
- R105: residual, orthogonality, gauge, sign, and rerun audit.
- R106: independently implemented adaptive magnetic dynamics.
- R107: fourth-order stencil; physical gates passed but residual gate failed.
- R107A: frozen guard-mode remediation; all original gates passed.

## Completed independent-discretization smoke: R108-S

R108-S tested the same Hénon-warped quantum operator with a genuinely different
polygonal-domain triangular weak-form discretization. It loaded neither archived
FD spectra nor primes or zeros, and it does not evaluate RMT claims.

Required controls:

1. fixed 256-vertex Hénon-preimage boundary;
2. P1 meshes at (h_u=0.060,0.045);
3. (B=0,1) with consistent mass and weak magnetic matrix;
4. direct quadrature without a potential clip;
5. generalized residual, (M)-orthogonality, (B\leftrightarrow-B), and
   coarse/fine gates;
6. no FD archive, RMT, prime, or zero comparison.

All per-cell integrity, quadrature, time-reversal, and independent-checker
controls passed. The first-60 coarse/fine median relative changes were 2.712%
at B=0 and 2.883% at B=1, failing the frozen <2% gates. Consequently R108-P,
R200-A production, R200-B/C, classical orbit matching, and all arithmetic
interpretation remain blocked.

## Terminated resolution remediation: R108-C0

R108-C0 prospectively froze a same-polygon, same-triangulation complex-P2
order-isolation test. Its algebraic oracles, development sanity, preparation,
and four P1-q7 controls passed. The first P2 cell at h=0.060 and B=0 then
failed the predeclared all-96 equation and mass-dual residual gates at the
outer guard mode 96. The cell was quarantined, the remaining cells were not
run, and the exact ten-cell comparison never existed.

The terminal status is `INVALID_OR_INCOMPLETE`, with formal C0 decision
`NOT_EVALUATED`; it is neither an order-isolation PASS nor a valid scientific
FAIL. R108-C1 is not authorized, and no claim about P2 convergence follows.
The intact archive and read-only audit are documented in
`research/R108C_PRODUCTION_TERMINAL_REPORT.md`.

## Submission-level extensions

- magnetic \(P_2\) finite elements or sine-Galerkin on a fixed domain;
- 500--1000 eigenvalues and multiple high windows;
- a symmetry-sector radial calculation;
- a broad microcanonical magnetic census and QR Lyapunov spectrum.

## Route A4 theorem-first continuation

R400 has superseded direct interpretation of the grid-sensitive R200 peaks.
It certifies the fast one-step \(a=1.02\) Lyapunov family near the unique well
bottom and matches exact period, action, and stability intercepts plus the
first nonlinear slopes.  The full package is in
`research/route_a_wave_trace/`.

A4.4--A4.9 now close the fixed-energy theorem gate: the normal form,
Lyapunov branch, radial exclusion, whole-shell warped uniqueness, and
eigenvalue-only finite-time CRR specialization have all been written and
independently audited.  A4.10 now fixes the positive-time CRR phase to \(+i\)
(\(\sigma=1\bmod4\)) and the project Fourier normalization to
\(T/(2\pi\sqrt D)\).

R401-SC has now completed its prospectively frozen eight-point
decreasing-\(\hbar\) sequence.  Every spectral, nested-basis, radial-oracle,
Fourier-quadrature, and independent-checker gate passed.  The finest cell
has

\[
 Z_{4\times10^{-5}}=1.0065230645+0.0133004473i,
 \qquad |Z-1|=0.0148139.
\]

The first five cells remain in the report because they show large
pre-asymptotic oscillations also present in the exact harmonic oracle.  R402
may extend the ladder and implement the separable analytic Galerkin assembly
or a compact-domain FD4 anchor, but it may not refit the phase or promote
this fixed-energy result to the arithmetic P gate.
