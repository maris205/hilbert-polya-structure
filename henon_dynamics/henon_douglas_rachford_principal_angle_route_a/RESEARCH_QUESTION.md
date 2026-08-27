# Research question

For two linear subspaces `U,V` of a finite-dimensional real Hilbert space,
classify the full discrete dynamics of

```text
T_lambda = (1-lambda)I + lambda(I+R_V R_U)/2,
R_W = 2P_W-I,
```

uniformly over every real `lambda`.  In one theorem, determine the fixed
space, all invariant blocks, the exact convergence window and rate, the
optimal relaxation, the shadow limit, the endpoint recurrence/periodicity
boundary, and the finite trace/determinant law.

Then apply Route-A evaluator v0.2.0 without changing the owner, clock, or
normalization.  Does the exact orthogonal boundary create any intrinsic
prime-orbit, dynamical-Zeta, target-analytic, or natural quantization evidence?

## Success criterion

Success requires an all-parameter proof plus two algebraically independent
exact implementations.  A few sampled projection matrices, an asymptotic plot,
or a citation-only assertion of the Friedrichs-angle rate is insufficient.

## Frozen boundary

- Finite-dimensional real Hilbert space only.
- Linear subspaces through the origin; inconsistent affine feasibility is a
  separate owner.
- One update is one unit of time.
- No prime or target-zero data enter the definition or evidence.
- The `lambda=2` orthogonal map is not relabeled as a quantum operator.
