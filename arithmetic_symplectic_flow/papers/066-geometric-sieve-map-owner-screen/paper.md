# A finite geometric sieve embedding is not an arithmetic dynamical carrier

**Paper ID:** `066-geometric-sieve-map-owner-screen`  
**Record ID:** `ASFS-SCOUT-20260914-44`  
**Date / status:** `2026-09-14; PRE-P0 STOP`  
**Route state:** `No Route-A coordinate; Route B NOT INVOKED`.

## Source object

The inspected geometric-sieve construction fixes a prime `p`, embeds the integers from `1` through `p^2` into the plane using remainders and quotients modulo `p`, and introduces focal lines. Its stated divisibility result is that an integer in the displayed range lies on the appropriate focal line exactly when it is a multiple of a relevant divisor. The complement of those marked intersections represents primes in the finite interval `(p,p^2)`.

This retains a legitimate, but limited, source arrow:

```text
finite sieve divisibility -> planar arrangement / symbolic-geometric display.
```

## Ownership audit

The construction begins by fixing the prime `p`; `f_p`, the domain size `p^2`, the focal-line slopes, and the finite complement are all defined after that selection. Consequently it is not a rule that produces its own next prime or a state that evolves through sieve stages. Replacing `p` by a different selected prime defines a different finite arrangement.

More fundamentally, no self-map of the arrangement is specified. A family of lines and a static finite point set has neither an iterate relation nor an intrinsic return, so it cannot own primitive periodic points or repetitions. A planar picture is not automatically a symplectic phase space: no two-form, area-preserving map, Hénon relation, roof, mapping torus, transfer operator, or determinant is part of this source.

Adding any such dynamics afterwards would make a new candidate. Selecting the finitely many displayed points or focal intersections as its periodic set would repeat the external-packet failure of 017 and 033.

## Gate assessment

| Gate | Evidence | Status |
| --- | --- | --- |
| A0 | finite divisibility display after a selected prime parameter | scoped FAIL for endogenous all-prime source |
| A1 | no action/iteration or orbit convention | NOT TESTABLE / stop |
| A2 | no same-object operator or zeta | NOT EVALUATED |
| Route B | no Route-A-ready object | NOT INVOKED |

**Decision: `stop/fork`.** Retain the source only as a geometric visualization control. A future geometric candidate must define one autonomous action that internally produces its arithmetic state and its returns before any symplectic thickening is considered.

## Evidence index

- Alexandru Iosif, [*A Geometric View of the Sieve of Eratosthenes*](https://arxiv.org/abs/1112.5796)
- [017 finite-wheel Hénon control](../017-finite-wheel-henon-control/paper.md)
- [033 wheel-packet thickening boundary](../033-wheel-packet-symplectic-thickening-screen/paper.md)
