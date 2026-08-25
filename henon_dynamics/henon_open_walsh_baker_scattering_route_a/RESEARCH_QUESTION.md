# C148 research question

Can a finite-dimensional, genuinely open Walsh quantum gate provide an exact
Route-A scattering subfamily with a closed unitary parent, an all-period trace
formula, an exact primitive complex-amplitude product, and reproducible secular
polynomials---while exposing rather than hiding the difference between a
one-step opening and the full tensor opening after one symbolic cycle?

The frozen candidate uses `P=diag(1,0,1)`, the unitary normalized three-point
DFT `F3`, `A=F3^* P`, and

```text
B_k(v0 tensor ... tensor v_(k-1))
 =v1 tensor ... tensor v_(k-1) tensor A*v0.
```

The answer is exact but deliberately limited.  `B_k` is a norm-one
contraction of rank `2*3^(k-1)`, whereas `B_k^k=A^(tensor k)` has rank `2^k`.
The source-side traces, determinants, and complex-amplitude primitive paths are
closed exactly.  No finite-`k` gate is promoted to a self-adjoint
quantization, no semiclassical target matching is attempted, and Route B is
not authorized.

Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.
