# C148 narrative report

## Outcome

C148 adds an open quantum-scattering subtype to Route A.  The family is not a
closed unitary walk: each tick shifts one qutrit through the rank-two gate
`A=F3^*P`.  Nevertheless its nonnormal contraction, exact left/right defect
projections, all-period traces, finite secular determinant, and complex
primitive paths are completely reproducible.

## The concrete advance

The key structural result is

```text
d=gcd(n,k)  =>  Tr(B_k^n)=Tr(A^(n/d))^d.
```

It turns a `3^k`-dimensional trace into a one-qutrit recurrence and gives exact
characteristic polynomials through `k=5`.  The family also supplies an escape
ledger that corrects a tempting but false statement: one step has rank
`2*3^(k-1)`, not `2^k`; only after `k` shifts does
`B_k^k=A^(tensor k)` have rank `2^k`.

## Controls that matter

Replacing `P` by `I` closes the opening and gives an exact unitary Walsh gate.
Moving the same projector from `F3^*P` to `P F3^*` changes the matrix geometry
but not any secular polynomial because the one-qutrit gates are unitarily
similar.  Moving the hole to coordinate zero preserves opening rank but changes
the linear secular coefficient.  These paired controls separate real spectral
sensitivity from a false order effect.

## Boundary

The primitive expansion consists of signed/complex basis-state path
amplitudes.  It is not a prime-like correspondence and is not an arithmetic
factorization.  Finite `k` is not a self-adjoint quantum limit, and no
semiclassical target comparison is performed.  The conservative tuple is
`(A1_WEAK,A2_FAIL,A3_FAIL,A4_UNITARY_OR_SCATTERING_CANDIDATE)`, overall
`ROUTE_A_EXPLORATORY`, with Route B disabled.
