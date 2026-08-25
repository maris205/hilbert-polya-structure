# HCS-C153: growing-system escape for the open Walsh gate

This package freezes the three-symbol gate

```text
A=F3^* diag(1,0,1),
B_k(v0,...,v_(k-1))=(v1,...,v_(k-1),A*v0),
```

with one application of `B_k` as one clock tick.  Its all-parameter theorem is

```text
rank(B_k^n)=2^min(n,k) 3^(k-min(n,k)),  k>=1, n>=0.
```

Consequently the rank-survival fraction at `n=floor(alpha*k)` has signed
logarithmic rate `min(alpha,1) log(2/3)` and positive escape exponent
`min(alpha,1) log(3/2)`.  At each fixed period `n`, the unnormalized traces
have the finite, equality-merged cluster set
`{Tr(A^(n/d))^d:d|n}`, while `3^(-k)Tr(B_k^n)` tends to zero.  Period two gives
an exact odd/even witness showing that an unnormalized limit need not exist.

The release includes 624 exact rank rows, 192 rational-slope macroscopic rows,
20 fixed-period cluster ledgers, an independent checker, SymPy reconstruction,
byte replay, hostile mutations, two genuine internal paper revisions, four PDF
artifacts, and a self-excluded content-addressed manifest.

Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.  Strict tuple:
`(A1_WEAK,A2_FAIL,A3_FAIL,A4_UNITARY_OR_SCATTERING_CANDIDATE)`, overall
`ROUTE_A_EXPLORATORY`; `route_b_invocation_allowed=false`.
