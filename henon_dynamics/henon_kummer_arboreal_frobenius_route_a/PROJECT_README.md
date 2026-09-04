# Project readme

**Candidate:** HCS-C374 / HEN-O358

**Owner:** the basepoint-two Kummer arboreal entanglement theorem

**Source baseline:** `f58422d8f03235329863f946654981ecb5d4dc97`

**Scope:** `NO_BAD_EULER_OR_ROOT_NUMBER`

The project asks for the exact image of Galois on all iterated preimages of
`2` under `z -> z^2`.  The decisive step is not a level table: it is the
proof that

```text
Q(2^(1/2^n)) intersect Q(zeta_(2^n)) = Q(sqrt(2))
```

for every `n>=3`.  That intersection forces one parity relation between
the cyclotomic multiplier and Kummer translation, producing an index-two
affine image.  The paper then derives every restriction map, every possible
fixed-root multiplicity, and the exact Chebotarev density.

Three manuscript rounds make three theorem-scale advances: field/image
closure; fixed-root/density closure; inverse-limit, executable, and Route-A
closure.  Every final claim is labeled as analytic theorem, exact finite
regression, or explicit nonclaim.

Strict evaluator v0.2 records `A1_WEAK` and `ROUTE_A_EXPLORATORY`: the exact
affine/fixed-root theorems do not provide the required complete primitive
orbit, repetition, phase, stability, or prime-to-orbit package.  This rating
does not weaken any theorem above.
