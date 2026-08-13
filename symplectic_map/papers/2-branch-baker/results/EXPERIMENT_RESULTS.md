# Experiment Results

## Material Passport

- Origin skills: `experiment-bridge`, `analyze-results`, and the local
  `route-a-evaluator`
- Candidate: `pcf_markov_baker_v1`
- Evaluation date: 2026-08-13
- Verification status: `VERIFIED`
- Version: `pcf_markov_baker_results_v1`
- Source lock SHA-256:
  `20473ff34b1f9258281483f47b9db915eb2680d2a71e9e1e6e9f3cf3d6fc07c8`
- Frozen code-tree SHA-256:
  `ad7f6637a90e6f5cfc4933b89adc70c543c0d0f259f295ea84da10c6fa5f0b11`

## Outcome

The frozen three-rectangle PCF Markov--baker is a valid compact,
almost-everywhere invertible carrier that is piecewise affine and exact
symplectic on branch interiors.  Its exact symbolic ledger, its single
periodic-boundary quotient, and all six matched controls passed.

It nevertheless fails the mandatory Route-A arithmetic gate.  In the
canonical constant-slope realization, every primitive period \(2k\) orbit has

\[
|\Lambda_u|=2^k,\qquad \ell_\gamma=k\log 2.
\]

Consequently, the exact rational-prime multiplier ledger intersects the
primes only at \(2\).  More generally, the proved finite-memory theorem shows
that one fixed finite-state, finite-memory, locally constant scalar
multiplicative clock can contain only finitely many rational-prime logarithms,
not all of them.  The formal decision is therefore

```text
PRE_A0_STRUCTURAL_PASS
A0_FAIL / STRUCTURAL_ONLY
A1_WEAK (intrinsic structural ledger verified; no A0 arithmetic labels)
A2, A3, A4: STOP_SCOPED
Route B: FORBIDDEN
```

This is a successful falsification and obstruction result, not a Riemann
dynamical determinant or Hilbert--Pólya candidate.

## Protocol integrity

The design was source-locked before candidate execution.  Version 2 records
one transparent mechanical amendment: the development seed in version 1 did
not equal the seed-derivation rule and was corrected before any exact,
development, validation, or test run.  No scientific field and neither the
validation nor test seed changed.

Validation was sampled only after the code, analysis, proof package, source
lock, and development artifacts were hash-bound.  The sealed test was sampled
only after validation and a verification manifest were frozen.  The complete
unlock chain verifies after the test.  No external prime table, Riemann-zero
table, legacy sealed transport result, target fitting, or target unfolding was
accessed.

## Exact and certified results

| Check | Frozen target | Result | Status |
|---|---:|---:|---|
| Exact preflight gates | 6/6 | 6/6 | Pass |
| Unit/integration tests | 89 | 89 passed, 0 failed | Pass |
| Primitive SFT cycles, periods 1--20 | 226 | 226 | Exact match |
| Primitive-count vector | `0,2,0,1,0,2,0,3,0,6,0,9,0,18,0,30,0,56,0,99` | exact match by direct enumeration and Möbius inversion | Pass |
| Dyadic positive-control cycles, periods 1--12 | 747 | 747 | Pass |
| Periodic boundary collapses | exactly 1 | exactly 1 | Pass |
| Parent audit precision | 100 decimal digits | 100 decimal digits | Pass |
| Parent audit maximum periodic residual | below \(10^{-75}\) | \(9.706\times10^{-98}\) | Pass |
| Parent audit maximum inverse iterations | report | 293 | Diagnostic |
| Forbidden-data/static-isolation violations | 0 | 0 | Pass |

The high-precision parent audit is an independently implemented consistency
audit, not an interval-arithmetic certification.  It does not import the
exact cycle-ledger generator.

The exact determinant audit kept the following conventions separate:

\[
\zeta_A(z)=\frac{1}{1-2z^2},\qquad
\zeta_f(z)=\frac{1+z}{1-2z^2},
\]

\[
\det(I-zW)=1\quad(W^3=0),\qquad
\zeta_{\mathrm{Lef}}(z)=\frac{1}{1-z}.
\]

The frozen instability-clock product is

\[
Z_u(s)=\det\!\left(I-2^{-s/2}A\right)^{-1}
=\frac{1}{1-2^{1-s}}
=\frac{2^s}{2^s-2},
\qquad \operatorname{Re}s>1,
\]

followed by its elementary meromorphic continuation.  The corresponding
factor-orientation-weighted SFT multiplier product is \(1\).  After the
periodic-boundary quotient, the frozen parent factor-orientation object is

\[
D_{\mathrm{or,parent}}(z)=1-z,
\qquad
D_{\mathrm{or,parent}}(z)\ne
\zeta_{\mathrm{Lef}}(z)=\frac{1}{1-z}.
\]

The first displayed structural zeta is the unsigned SFT/baker zeta; the
second is the parent-core
Artin--Mazur zeta after replacing one symbolic period-two boundary ghost by
the fixed point \(d\).  The nilpotent \(W\) object uses inherited
one-dimensional factor-branch orientation and is neither two-dimensional
symplectic orientation nor a Maslov phase.  The Lefschetz convention is a
fourth, distinct object.

## Floating implementation stress

Each split used its independently derived frozen seed and sampled 65,536
interior points for 256 steps.  At each step the executed forward branch was
immediately composed with its identified inverse.  These are deterministic
implementation checks, not independent statistical observations and not a
claim of reversing a 256-step chaotic trajectory.

| Split | Seed | Completed checks | Max roundtrip error | Edge mismatches | Boundary failures | Gate |
|---|---:|---:|---:|---:|---:|---|
| Development | 9296786003925294372 | 16,777,216 / 16,777,216 | \(1.388\times10^{-16}\) | 0 | 0 | Pass |
| Validation | 6299270948367439428 | 16,777,216 / 16,777,216 | \(1.388\times10^{-16}\) | 0 | 0 | Pass |
| Sealed test | 17469014571681933606 | 16,777,216 / 16,777,216 | \(1.388\times10^{-16}\) | 0 | 0 | Pass |

The observed maximum is approximately 0.0694% of the frozen
\(2\times10^{-13}\) threshold, or about 1,441 times smaller.  All three splits
gave the same maximum and the same zero-failure counts.  A post-test rerun of
the development split to a temporary path reproduced its formal JSON
byte-for-byte; both files had SHA-256
`d8f493078a62b533f9d8775d18bb6c8dc7020ba58c82a69e865cea9f1b62d378`.
The sealed test was not rerun.

## Controls

| Control | Observation | Interpretation |
|---|---|---|
| Dyadic baker | Symplectic inverse and 747-cycle ledger passed | Positive control for enumeration and inversion |
| Folded-tent baker | Stable and unstable coordinates reverse together; determinant remains \(+1\) | Positive control for decreasing branches |
| Matched dissipative map | Same future graph, determinant \(1/2\), non-surjective image | Separates symbolic coding from symplecticity |
| Label erasure | Distinct pasts map to one future | Shows why branch labels are required |
| Anti-symplectic branch | Determinant \(-1\) and rejected | Detects single-coordinate sign mistakes |
| All-positive-sign null | Unsigned graph unchanged but nilpotent orientation cancellation disappears | Shows the signed cancellation is convention-dependent, not an unsigned orbit effect |

## Findings

### 1. The compact carrier is internally consistent

- **Observation:** PCF algebra, Perron--Frobenius geometry, strip tiling,
  branchwise \(J^T\Omega J=\Omega\), determinant one, inverse relations, exact
  boundary tests, and all floating checks passed.
- **Interpretation:** The branch-history construction repairs the missing-past
  problem without a noncompact Hénon phase space.
- **Implication:** This is a reusable compact test platform for finite symbolic
  extensions.
- **Next step:** Preserve it as a structural positive control; do not promote
  it to a globally smooth symplectomorphism.

### 2. The factor is exact only after a declared boundary quotient

- **Observation:** The symbolic cycle \(1\leftrightarrow2\) is the sole
  periodic coding duplicate and collapses to the parent fixed point \(d\).
- **Interpretation:** The baker/SFT and interval parent do not have identical
  pointwise periodic ledgers on the boundary.
- **Implication:** Their zeta functions differ by the exact factor \(1+z\).
- **Next step:** Treat the correction as a reproduced baseline rather than a
  novelty claim.

### 3. Signed factor orientation cancels, but it is not a quantum phase

- **Observation:** \(W^3=0\), every positive-period signed trace vanishes, and
  \(\det(I-zW)=1\); the all-positive-sign null removes this cancellation.
- **Interpretation:** Cancellation is inherited from one-dimensional branch
  orientation.
- **Implication:** Replacing signs by absolute values after inspection would
  change the object and violate the source lock.
- **Next step:** Do not interpret this sign as symplectic orientation, a
  Maslov index, or evidence for A4.

### 4. The locally constant instability clock is structurally non-arithmetic

- **Observation:** Its complete clock lies in
  \(\mathbb Q\log 2\), while distinct rational-prime logarithms are linearly
  independent over \(\mathbb Q\).
- **Interpretation:** Exact termwise \(p\leftrightarrow\gamma_p\) coverage is
  impossible for this candidate; only \(p=2\) occurs.
- **Implication:** A0 fails by theorem, so zero fitting, dynamical-Zeta target
  comparison, quantization, and Route B would only add post-hoc machinery.
- **Next step:** Stop this candidate at A0 and report the obstruction.

### 5. The conclusion is split-stable

- **Observation:** Development, validation, and test produced identical gate
  decisions and floating diagnostics under different frozen seeds.
- **Interpretation:** The decision is not a best-seed artifact.
- **Implication:** The sealed test confirms the implementation and the frozen
  decision rule.
- **Next step:** No additional sampling is needed for this fixed candidate.

## Claim boundary and limitations

The result excludes an exact all-prime termwise ledger only for one fixed
finite graph with a finite-memory, locally constant scalar multiplicative
cocycle.  It does not exclude:

- point-dependent derivatives or Hölder roof functions;
- countable-state symbolic systems or growing sequences of finite models;
- matrix spectral radii or largest singular-value clocks;
- approximate, statistical, or density-only prime resemblance;
- analytic identities arising from signed cancellation in a common
  convergence domain;
- a different candidate with independently justified arithmetic structure.

The carrier is piecewise exact symplectic on branch interiors, not a global
\(C^1\) symplectomorphism.  Its parent determinant and boundary-discrepancy
mechanism have direct prior art.  The PCF parameter was deliberately selected
for exact finite Markov structure, so no conclusion is generalized to
arbitrary quadratic parameters or arbitrary symplectic maps.

## Final decision

`pcf_markov_baker_v1` is rejected as a primary Route-A arithmetic candidate
and retained as a verified structural control plus a narrow finite-clock
obstruction case study.  There is no further experiment inside the frozen
candidate.  Any variable-roof, point-dependent, countable-state, smoothed, or
higher-dimensional construction is a new candidate and requires a new source
lock and a fresh arithmetic-origin audit.
