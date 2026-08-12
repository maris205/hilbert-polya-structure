# R400 Implementation Review and R200 Diagnosis

## Decision

**The classical-first R400 local-period smoke is approved and has passed.**
The broader quantum-trace production stage remains deferred.

## Why R200 peaks were not interpretable

R200 validated its finite-dimensional trace algebra but used second-order
spectra whose coarse/fine phase error was too large.  A weighted RMS
eigenvalue error \(\epsilon_\lambda\) limits a phase-controlled trace to

\[
 T_{0.25}=\frac{0.25}{\epsilon_\lambda}
\]

at \(\hbar=1\).  The audited values were approximately:

| Window center | R200 RMS \(|\delta\lambda|\) | 0.25-rad time |
|---:|---:|---:|
| 80 | 1.17–1.29 | 0.19–0.21 |
| 140 | 4.15–4.38 | 0.057–0.060 |
| 200 | 9.42–9.86 | 0.025–0.027 |

The previously inspected nonzero peaks at times around \(0.3\)–\(1.5\) lay
outside those phase budgets.  High magnitude correlation cannot repair a
wrong complex phase.

Existing fourth-order R107A spectra are much better, with audited weighted
RMS errors near \(0.004\), \(0.021\), and \(0.063\) at the same representative
energies.  They may support a later trace pilot after a matching radial
fourth-order and independent radial-ODE branch is built.

## R400 implementation reviewed

The current smoke deliberately solves the cheaper theorem-side problem
first:

- exact bottom Hessian and normal-mode oracle;
- reversible half-period shooting;
- independent full-period state/variational/action integration;
- period, action, monodromy, symplectic defect, and transverse determinant;
- a six-energy continuation toward the equilibrium;
- non-fitted intercept and first-slope checks;
- an independent checker that imports neither the production orbit module
  nor any archived state solver.

## Frozen numerical gates

Every orbit must satisfy:

- shooting residual below \(10^{-9}\);
- scaled closure below \(10^{-9}\);
- energy drift/excess below \(10^{-9}\);
- symplectic defect below \(10^{-8}\);
- real transverse determinant above 3;
- physical period in \([0.60,0.75]\).

The three smallest energy cells must recover the analytic intercepts and the
normal-form period/action slopes within the tolerances in
`R400_LOCAL_PERIOD_PROTOCOL.md`.

## Result

All gates passed.  Worst values over six cells were:

| Diagnostic | Worst value |
|---|---:|
| shooting residual | \(4.44\times10^{-14}\) |
| scaled closure | \(6.15\times10^{-15}\) |
| energy drift/excess | \(1.78\times10^{-13}\) |
| symplectic defect | \(8.12\times10^{-15}\) |

The independent checker passed 66 hash, oracle, raw-array, gate, and
independent-solve checks after the nonlinear-slope oracle was added.  Its
separate \(\delta=0.05\) solve agrees with production to rounding-scale
absolute errors.

## Attempt history

Three pre-final development archives are retained transparently:

1. `r400_local_period_smoke.attempt0-syntax-warning`: all scientific gates
   passed, but the report generator emitted Python invalid-escape warnings;
2. `r400_local_period_smoke.attempt1-checker-serialization`: the run passed,
   while the postchecker stopped before writing output because NumPy boolean
   scalars were not converted to JSON booleans.
3. `r400_local_period_smoke.attempt2-before-normal-form-slope`: the run and
   checker both passed the intercept-only protocol, but the archive was
   superseded prospectively when the analytic first period/action slopes were
   added as stronger non-fitted gates.

The first two defects were serialization/reporting issues; the third is a
valid but weaker prerevision.  The final result was regenerated from a fresh
directory after every source/protocol change; no archived scientific array
was edited in place.

## Historical deferred production route and resolution

The list below records the pre-R401 design state.  R401-SC is now complete.
It did not reuse R107A spectra: a method audit instead derived the exact
unitary coordinate change \(u=\Psi_a(q)\), used a form-domain-valid
transformed Galerkin solver, and retained the radial angular-momentum oracle.
The frozen eight-cell archive and independent checker both report `PASS`.

The next quantum stage should not reuse R200's second-order wave trace.  It
should:

1. reuse the converged R107A fourth-order warped spectra;
2. compute matching fourth-order radial spectra;
3. construct an independent radial angular-momentum Sturm--Liouville oracle;
4. use compactly supported energy bumps rather than Gaussian-tail claims;
5. freeze classical period/action templates before looking at a complex
   trace;
6. require an explicit eigenvalue phase budget at every retained time;
7. test an \(\hbar\)-ladder only after the classical and spectral instruments
   pass independently.

This stage was named **R401-SC**.  It was authorized only after the analytic
proof and phase reviews, and is documented in
`R401_FIXED_ENERGY_TRACE_PROTOCOL.md` and
`results/r401_fixed_energy_trace_smoke/`.
