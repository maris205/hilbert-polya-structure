# C164 two-round paper improvement log

## Round 0: determinant sketch

The first draft observed that a rank-one operator can have determinant
`1-F(z)`.  It did not yet separate source branch ownership from a scalar
tautology and only mentioned the standard `l2` adjacency informally.

## Round 1: proof and ownership audit

- Resolved `K_z` into one rank-one summand per frozen return branch.
- Added uniform trace-norm convergence on every compact subdisk and the full
  law `Tr(K_z^m)=F(z)^m`.
- Recorded exact gauge cancellation and the separate all-zero orbit block.
- Replaced a single-norm observation by the all-positive-weight compactness
  contradiction, including the bounded control `w_n=2^n`.
- Transferred C159's natural boundary through the continuous trace map.

## Round 2: hostile boundary and artifact audit

- Made “induced first-return family”, “uninduced time-one adjacency”, and
  “post-hoc scalar determinant” three explicitly different objects.
- Kept `A4_FAIL`: a nonunitary induced Fredholm owner is not a natural
  self-adjoint or Hilbert--Pólya lift.
- Exposed every claim-bearing field to repaired-hash mutation tests.
- Required independently phrased English/Chinese abstracts, deterministic
  PDF snapshots, embedded fonts, warning-free logs, and 27-file manifest
  closure.

Both reviews are internal artifact checks.  No external reviewer, acceptance
score, or unperformed computation is claimed.
