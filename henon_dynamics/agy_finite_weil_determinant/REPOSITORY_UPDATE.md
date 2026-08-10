# HCS-C27 repository update

## Added

- a new project directory `agy_finite_weil_determinant`;
- an exact Thomas-character producer and an implementation-independent
  checker;
- complete finite-fibre polynomials at p=3,5,7;
- the odd-prime/power chronology census and the complete p=43 period proof;
- the explicit C24-P076/P082 integral symplectic conjugacy certificate;
- the 150-branch Legendre-signature census;
- theorem, source-audit, experiment, narrative, paper, Route-A, and
  reproducibility documents.

## Parent registries

The following repository-wide documents now register HCS-C27:

- `henon_dynamics/README.md`;
- `henon_dynamics/docs/candidate_registry.md`;
- `henon_dynamics/docs/obstruction_registry.md`;
- `henon_dynamics/docs/related_programs/README.md`.

The reusable obstructions are HEN-O57 (integral-conjugacy collapse of every
class-function fibre) and HEN-O58 (complete p=43 nonseparation of the finite
Weil fibre polynomial).

## Claim boundary

The update proves a family of fixed-prime trace-class Fredholm determinants
and exact arithmetic character formulas. It does not construct a product or
direct sum over primes, identify a completed-zeta divisor, prove a functional
equation, or construct a self-adjoint Hilbert–Pólya operator.

The p=43 equality concerns only `det(I-T rho_43(g))`; the scalar AGY atoms
remain distinct. The P076/P082 cycles are C24 controls and are not relabeled
as branches of the C26 accelerated operator.

## Release command

```bash
cd henon_dynamics/agy_finite_weil_determinant
bash code/run_c27.sh
```

The intended release sequence is implementation commit, exact replay,
Route-A provenance update, tag, and SSH push.
