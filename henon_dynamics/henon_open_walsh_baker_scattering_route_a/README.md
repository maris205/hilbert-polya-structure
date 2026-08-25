# HCS-C148: open Walsh--baker scattering gate

This release freezes `A=F3^*diag(1,0,1)` and the qutrit factor-shift family

```text
B_k(v0,...,v_(k-1))=(v1,...,v_(k-1),A*v0).
```

Its principal theorem gives `B_k^k=A^(tensor k)` and, for
`d=gcd(n,k)`, `Tr(B_k^n)=Tr(A^(n/d))^d` at every period.  A central escape
ledger corrects the one-step rank to `2*3^(k-1)`; `2^k` is the rank after
exactly `k` steps.  Both subunitarity defects are explicit rank-`3^(k-1)`
orthogonal projections.

The release contains exact characteristic-polynomial receipts for `k=1,...,5`,
an exact complex-amplitude primitive-path ledger, closed/unitary and opening
controls, an independent checker, SymPy reconstruction, byte replay, hostile
mutations, strict Route-A YAML, two internal review/fix rounds, four retained
PDFs, and a self-excluded content-addressed manifest.

Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.  Verdict:
`(A1_WEAK,A2_FAIL,A3_FAIL,A4_UNITARY_OR_SCATTERING_CANDIDATE)`, overall
`ROUTE_A_EXPLORATORY`; `route_b_invocation_allowed=false`.
