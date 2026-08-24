# C135 research question

Can the nonlattice suspension of C130 be made sensitive to edge transitions,
rather than only symbol populations, while retaining an exact finite-matrix
determinant and all-period primitive product?

## Certified answer

Yes.  On the full binary shift use

```text
tau = [[1,sqrt(2)],[sqrt(3),sqrt(6)]].
```

The four roof values form the rational basis of `Q(sqrt(2),sqrt(3))`, so roof
time is injective on directed-edge-count vectors.  The period-six words
`000111` and `001011`, which collide under C130's symbol-count roof, have edge
vectors `(2,1,1,2)` and `(1,2,2,1)` and therefore distinct times.

The refinement is not orbit-injective.  The primitive nonrotations `001011`
and `001101` share `(1,2,2,1)`.  More generally every closed binary word obeys
`N01=N10`, so periodic data see only `tau01+tau10` and cannot recover
`tau01-tau10`.

No target divisor, arithmetic Euler factors, global target structure, natural
self-adjoint lift, or Route-B readiness is claimed.
