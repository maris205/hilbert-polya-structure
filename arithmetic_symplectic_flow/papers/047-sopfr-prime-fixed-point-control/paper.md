# The sum-of-prime-factors map is an A0+A1 arithmetic fixed-point control

**Paper ID:** `047-sopfr-prime-fixed-point-control`  
**Record ID:** `ASFS-SCOUT-20260914-35`  
**Date / status:** `2026-09-14; EXTERNAL A0+A1 POSITIVE CONTROL — PRIME FIXED POINTS WITHOUT PRIOR-WORK GEOMETRIC LINEAGE`  
**Route state:** `No classical candidate; Route A not evaluated; Route B NOT INVOKED`

Define `A(n)=sum_i p_i` when `n=product_i p_i` is the prime factorization with multiplicity. Then `A(p)=p` for every prime. Also `A(4)=2+2=4`.

For a composite `n>4`, the sum of its prime factors is strictly smaller than their product. Hence `A(n)<n`. A periodic orbit containing such an `n` would have strictly decreasing values until the next iterate, impossible around a cycle. The complete periodic set is therefore exactly the prime fixed points and the exceptional fixed point `4`; each has primitive period one.

This is a genuine same-object arithmetic source and periodic-orbit classification. It is deliberately not promoted: the carrier is a discrete integer map with no prior-work prime-symbolic deformation, no Logistic/Hénon bridge, no positive-dimensional symplectic base, no positive roof, and no same-object dynamical zeta. A cotangent or disk lift would require a new full-ledger construction and cannot inherit credit.

| Gate | Status |
| --- | --- |
| A0 | external positive control only |
| A1 | external exact fixed-point/repetition control |
| A2 | `NOT EVALUATED` |
| Route B | `NOT INVOKED` |

**Decision: retain as external control.** It establishes that endogenous prime recognition and a complete primitive ledger can coexist in one map, while isolating the missing task: a lineage-preserving conservative/symplectic realization that does not replace arithmetic mechanism with an external encoding.
