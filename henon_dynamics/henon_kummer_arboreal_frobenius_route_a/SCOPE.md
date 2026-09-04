# Scope firewall

Literal lock: `NO_BAD_EULER_OR_ROOT_NUMBER`.

## In scope

- the fields `K_n=Q(2^(1/2^n),zeta_(2^n))`;
- their exact finite and inverse-limit Galois images;
- compatible restriction maps;
- Frobenius fixed roots of `x^(2^n)-2` at odd primes;
- Chebotarev densities inside these source fields;
- finite permutation/Koopman realizations;
- exact regression and hostile validation of the formulas.
- evaluator controls at A0: neighboring basepoint 3, the uncut full affine
  parent, and a composite-label decomposition that retains prime powers as
  Frobenius repetitions and rejects only mixed composites as single-prime
  labels.

## Out of scope

- target arithmetic local data or target Euler factors;
- root numbers or automorphy;
- a target functional equation, divisor, counting law, or zero match;
- a global trace-class or determinant-class operator;
- a Hilbert--Pólya operator;
- Route B.

Every corresponding machine-readable flag is `false`.

The exact fixed-root law does not by itself satisfy the v0.2 primitive-orbit
requirements: completeness for primitive/repeated cycles, orientation,
phase, stability, intrinsic prime/period weights, and mandatory A1 controls
are missing.  The rating is therefore `A1_WEAK` and
`ROUTE_A_EXPLORATORY`.
