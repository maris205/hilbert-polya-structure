# C134 results

- Scaled geometry: radius `3k`, image radii `21k/32,3k/4`, minimum gap
  `11k/16` for every `k>=1` and every branch permutation.
- Replay prefix: 284 rooted words and 40 primitive cycles through period eight.
- Recovery ledger: all twelve permutations for `k=1,6` decode exactly.
- Universal characteristic determinant:
  `1-(1/2)X^t0 z-(1/6)X^(t0+t1)z^2-(1/30)X^(t0+t1+t2)z^3`.
- `q=(3+4i)/5` is faithful and `q^(-2)=(-7-24i)/25`.
- `k=1` and `k=6` are completely aliased by the mod-five phase but separated
  by both Laurent and exact faithful-`q` receipts.
- Validation: checker 71, SymPy 64, byte replay PASS, mutations 48/48
  (`47` repaired-hash plus `1` stale-hash).  The expanded semantic suite now
  fixes the four clock/normalization/precision/cutoff source locks and all
  three stored Newton identities explicitly.

Evidence SHA-256:
`45fa45b4668464564abb79db54b0e76b76c3acab5ae163acadb81a31d7bdc21d`.

Final two-page PDF SHA-256:
`404b2618ff7e51c6018a7b9c007b0d683dd3ade8ac6af0484f3f782692d651d5`.

Strict verdict: `(A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`.
