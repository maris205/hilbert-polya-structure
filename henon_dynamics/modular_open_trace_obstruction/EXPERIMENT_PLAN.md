# HCS-C18 claim-driven experiment plan

## Source lock

- Group: \(\Gamma=\mathrm{PSL}_2(\mathbb Z)\), cusp stabilizer
  \(P=\operatorname{Stab}(\infty)\).
- Endpoint groupoids: \(\Gamma\ltimes\mathbb P^1(\mathbb Q)\) and
  \(\Gamma\ltimes\mathbb P^1(\mathbb R)\).
- Open positive control: unoriented scattering geodesics and the convention of
  Pujahari--Satpathy, with a sufficiently large geometric compact-core
  parameter \(T_0>1\).  The coefficient code uses \(T_0=1\) only as an
  analytic normalization.
- Multi-cusp control: standard width/Atkin--Lehner normalized scattering
  matrices of squarefree \(\Gamma_0(N)\) with trivial nebentypus.
- Levels: \(N\in\{2,6,30,210\}\), hence dimensions \(2,4,8,16\).
- No Riemann-zero or prime tables, no fitted scale, and no averaged transition
  matrices are permitted.

## Claims, tests, and falsifiers

| ID | frozen claim | test | falsifier |
|---|---|---|---|
| C1 | \(n_q=(\varphi(q)+s_q)/2\) and the stated open series formula | exact enumeration through \(q=2000\), Euler-factor identities, high-precision partial sums | parity failure, coefficient mismatch, or analytic residual beyond frozen tolerance |
| C2 | \(P\backslash\Gamma/P\) has no representative-independent multiplication | exact \(S,ST^n\) witnesses | both representative products land in the same double coset for every tested \(n\) |
| C3 | the displayed rational projective-section cocycle is an algebraic coboundary | primitive-vector and affine-section exact ledger | any primitive arrow has \(|j|\ne1\) or affine value differs from endpoint gauge difference |
| C4 | nonzero full-boundary automorphy periods are signed Selberg lengths | analytic fixed-point classification and eigenvalue/length proof | a non-parabolic/non-hyperbolic real loop or a period mismatch |
| C5 | squarefree scattering tensor factorization and Walsh diagonalization hold | direct Kronecker construction, channel formulas, determinant | direct matrix and reconstructed matrix disagree |
| C6 | the frozen bare product at different spectral parameters is permutation-invariant | multiply matrices before comparing all parameter permutations | any commutator or permutation residual exceeds tolerance |
| C7 | endpoint projectors can restore assignment/path sensitivity | compare projected traces after a parameter-to-edge reassignment and after changing the path | all source-locked projected witnesses remain equal |
| C8 | physical-line unitarity and functional equation hold | 80-digit matrix checks | residual exceeds tolerance |
| C9 | local factors cannot cancel transported nontrivial-zeta divisors | symbolic zero/pole real-part classification | a local zero/pole occurs in the relevant open strip |

## Numerical protocol

- Producer precision: 80 decimal digits.
- Independent checker: at least 100 decimal digits and no producer import.
- Matrix norm: maximum absolute entry.
- Frozen analytic tolerance: \(10^{-60}\) for producer checks and a separately
  computed checker threshold.
- Spectral parameters must avoid poles and include at least three points on
  \(\Re s=1/2\) plus two off the physical line.
- Frozen-product comparisons use direct multiplication in the recorded order.  Sorting,
  histogramming, or averaging steps before multiplication is forbidden.

## Decision rule

The proposed rational ordinary trace clock is rejected if C3 holds; the
full-boundary extension is classified at the level of periods by C4, without
asserting a determinant identity.  C5 and C6 reject only a conditional model
that tries to encode successive steps by bare \(\Phi_N(s_j)\) factors; no
claim identifies \(s\) with time.  C7 is reported as an open positive scope
boundary, but it is not promoted without a primitive-object and Fredholm
theorem.  A failed positive branch is not repaired by changing a cutoff.

## Scope exclusions

The plan does not test nontrivial nebentypus, nonsquarefree ramification,
Bianchi class-group blocks, inserted noncommuting internal cocycles,
Kloosterman/modular-symbol twists, general groupoid \(C^*\)-traces, or a
separately derived self-adjoint Hilbert--P\'olya operator.
