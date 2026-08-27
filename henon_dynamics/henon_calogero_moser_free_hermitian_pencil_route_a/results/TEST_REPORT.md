# C196 test report

## Executable checks

- Producer: PASS -- 18 systems, 126 pencil rows, 417 exact Hermitian entries,
  417 commutator entries, and 99 trace/energy checks.
- Independent checker: PASS -- 2,210 assertions; no producer import and exact
  top/finite/case/pencil/scattering key-set closure.
- SymPy: PASS -- 1,200 exact checks.
- Replay: PASS -- 123,388 byte-exact bytes.
- Mutations: PASS -- 135 repaired-hash and one stale-hash rejection; five
  repaired-hash attacks inject unknown semantic keys at distinct schema levels.

## Independence and coverage

The producer uses exact Gaussian-rational matrix products and LAPACK
Hermitian eigenvectors.  The checker independently regenerates every datum,
realifies complex Hermitian matrices, runs a hand-written maximum-pivot Jacobi
solver, recovers intercepts as `Tr(QP_m)` from polynomial spectral projectors,
and checks velocities by centered differences.  SymPy separately verifies
all exact powers and characteristic polynomials, a generic three-particle
commutator/energy/force identity, and the inverse-atlas denominator sign.

Static semantic sections are individually content-addressed; the checker also
requires exact key sets at all unhashed finite-regression nesting levels, and
every finite row and aggregate is recomputed.  The numerical inverse sentinel
reconstructs positions; the full phase-space inverse atlas is analytic.  Finite spectra test conventions and code only;
they do not prove all-time simplicity or the all-`N` scattering theorem.
