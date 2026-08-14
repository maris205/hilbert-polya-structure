# PREREGISTRATION — SD-C17

- Frozen date: 2026-08-14.
- Primary family: Symbolic Dynamics only.
- Source: tensor atoms of finite full shifts under
  `F_m tensor F_n = F_mn`; roof `h(F_n)=log n`.
- Finite alphabet: every nonempty subset `S` of a frozen finite atom set.
- Scalar edge weight: `epsilon(S)x_S`, with
  `epsilon(S)=(-1)^(|S|+1)`.
- Countable specialization: `x_(F_p)=p^(-s)`; analytic claims restricted to
  `Re(s)>1`.
- Primitive equivalence: cyclic rotation only; reflection is not quotiented.
- Temporal repetition: actual scalar power `w(gamma)^r` with trace-log factor
  `1/r`.
- Naturality: any pairing or contraction must commute with finite atom
  permutations, cyclic rotation, content, and temporal powers.
- Frozen decisive contents: `pq`, `p^2q^2`, and `pqr`.
- Frozen finite cutoffs: cyclic set partitions through `k=7`, Stirling
  certificate through `k=12`, scalar/supertrace powers through `r=8`.
- Frozen controls: 16 rational seeds at each `k=2,...,8`, presentation
  shuffles, and a true contractible even/odd block.
- Forbidden repairs: lexicographic pairing promoted as natural; fixed negative
  sign under powers; treating scalar sign as chain parity; discarding
  repetitions; fitting phases, pairings, or cutoffs after inspection.
- Riemann-zero data: prohibited and unused.
- Cross-family carrier: prohibited; record only as `ROUND2_CLUE`.
- Route B: locked.

Decision rules:

```text
GO_SCALAR_KOSZUL_DETERMINANT
  iff the formal and countable determinant theorems close.

STOP_PRIMITIVE_LEVEL_INVOLUTION
  if p^2q^2 cancellation crosses primitive and r=2 layers.

STOP_EQUIVARIANT_SIGN_REVERSAL
  if the pqr virtual S3 character is nonzero.

STOP_PARITY_SUBSTITUTION
  if scalar and odd-supertrace powers disagree at r=2.

STOP_ARITHMETIC_SELECTIVITY / PROVES_TOO_MUCH
  if arbitrary formal inventories satisfy the same determinant identity.
```
