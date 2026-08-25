# C153 research question

## Question

For the source-locked open Walsh family

```text
B_k(v0 tensor ... tensor v_(k-1))
 =v1 tensor ... tensor v_(k-1) tensor A*v0,
A=F3^*diag(1,0,1),
```

what can be proved exactly as both the tensor length `k` and elapsed clock
time `n` vary?  In particular:

1. what is `rank(B_k^n)` for every `n,k`;
2. what rank-survival exponent appears at `n=floor(alpha*k)`;
3. what are all subsequential values of `Tr(B_k^n)` at fixed `n` as
   `k->infinity`;
4. does dimension normalization remove the gcd oscillation?

## Frozen interpretation

The invariant object is the exact surviving image dimension, normalized by
the ambient dimension `3^k`.  The trace is a separate complex observable with
ordinary finite-dimensional normalization.  No target data, spectral
rescaling, secular-limit completion, or alternate clock may enter after the
object is frozen.

## Answer boundary

The package proves a saturated rank escape law and a complete fixed-period
trace cluster classification.  It does not prove a growing-`k` full secular
determinant, a self-adjoint limit, a target match, or Route-B readiness.
