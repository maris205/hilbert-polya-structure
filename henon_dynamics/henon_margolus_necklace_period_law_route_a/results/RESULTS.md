# C165 exact results

## Released theorem receipts

- For every `m>=1`, one full Margolus tick sends even sites by `+2` and odd
  sites by `-2` modulo `2m`.
- The pairing `(2j,1-2j)` conjugates the complete binary configuration map
  to cyclic rotation on `m` four-letter symbols.
- Therefore `#Fix(T^n)=4^gcd(m,n)` for every positive `m,n`.
- For every `d|m`, exact-period configurations and cycles are
  `P_m(d)=sum_(e|d)mu(d/e)4^e` and `C_m(d)=P_m(d)/d`.
- The complete source zeta is
  `product_(d|m)(1-z^d)^(-C_m(d))`.
- The uniform short-period estimate is
  `Pr(period<m)<=m/2^m`; at `m=1` the actual short probability is zero.
- Reflection reverses the full tick.  The finite counting-measure Koopman
  permutation owns the inverse source zeta and has an explicit antiunitary
  reversal.

## Finite exact sentinels

- 16 family rows, `1<=m<=16`.
- 136 fixed-time cells.
- 50 exact-period cells.
- 87,380 configurations directly enumerated through `m=8`.
- Boundary `m=1`: four fixed configurations and no short-period state.
- Boundary `m=2`: four fixed configurations and twelve configurations in
  six two-cycles.

The canonical evidence file has SHA-256
`70a7fc44fb48f5cd2b471e21df4e406c8f4cc928c928165f05ef71a3dcbef763`;
its self-declared canonical payload hash is
`37bc88bccaf4c09ef1200246a33cdc9cae282160fc0424ca8b0a84f2abc19165`.

Finite rows are regression sentinels, not proof by extrapolation.  The model
is not claimed to be chaotic or interacting, and no target or arithmetic
promotion is made.
