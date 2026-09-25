# Scope card — ASFS-SCOUT-20260914-65

| Field | State |
| --- | --- |
| Carrier | nonnegative five-tuples | discrete order-five state |
| Update | `F(x1,x2,x3,x4,x5)=(x2,x3,x4,x5,pi(x1+x2+x3+x4+x5))` | fixed noninjective map |
| Initial state | `(1,1,1,1,1)` for the listed sequence | selected seed, not an arithmetic owner |
| Arithmetic mechanism | `pi(N)=#{p prime:p<=N}` explicitly called at every update | global prime oracle |
| Known recurrence | `(66,66,66,66,66)` is fixed because `pi(330)=66` | source-supported for named seed |
| Lineage | no sieve-symbolic admissibility, sequential deformation, or Hénon intertwiner | EXTERNAL |
| Roof/flow/zeta | NOT SUPPLIED | PRE-P0 stop |
| Route state | A0 scoped FAIL; A1 not used to rescue it; Route B NOT INVOKED | frozen boundary |
