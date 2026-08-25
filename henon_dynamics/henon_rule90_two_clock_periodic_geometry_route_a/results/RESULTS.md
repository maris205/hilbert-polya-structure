# C145 results

- All-size theorem:
  `#Fix(F_L^n)=2^deg gcd(x^L+1,(x^2+1)^n+x^n)` over `F_2`.
- Exact two-clock ledger: 576 cells for `1<=L,n<=24`.
- Ledger sums: 488,334 fixed points; 283,758 exact-period points; 24,474
  primitive temporal cycles.
- Full positive-domain first area witness: area 3, `(1,3)` versus `(3,1)`.
- Nondegenerate `L,n>=2` first area witness: area 6, `(2,3)` versus `(3,2)`.
- First nondegenerate area witness with nonzero exact-period content: area 12,
  with `(6,2)` contributing 12 exact points and six cycles.
- Same fixed-count control: `Fix(5,3)=Fix(5,6)=16`, but five versus zero
  primitive cycles at the displayed times.
- Independent checker: 6,520 assertions.
- SymPy: 1,177 exact checks.
- Mutation audit: 42 repaired-hash plus one stale-hash mutation rejected.

The evidence and PDF hashes are bound by the release manifest.
