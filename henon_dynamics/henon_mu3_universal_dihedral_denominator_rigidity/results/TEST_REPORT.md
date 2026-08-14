# HCS-C54 release test report

The independent checker passes all **36/36 semantic gates** on the canonical
certificate.  The Python unit suite exercises the valid certificate, strict
JSON parsing/schema/type locks, targeted theorem mutations, independent
semantic rejections with both payload and schema locks rebound, a sweep of
every semantic scalar leaf, an exhaustive scalar classification inventory,
and the local atomic update protocol.  The final code/results
release-candidate suite passes
**93/93 tests**.

The certificate has exactly **1,078 scalar leaves**.  Of these, **198** are
individually value-locked and mutation-tested after both digest locks are
rebound, **876** lie in five narrow subtrees that the checker independently
regenerates and compares exactly, and exactly **4** are explicitly allowlisted
chronology-only hashes of unpackaged notes that are neither sources nor theorem
inputs.  The test suite fails on every missing, overlapping, or unclassified
scalar path.

Core exact replays include:

- recurrence enumeration and presentation checks for the universal group;
- an independent brute-force phase scan at `n=2,3,4`;
- semilinear generator transport and both fixed-point congruences;
- separate pure-rail ranks, the `n | 24` reduction, complete divisor table,
  and the `n=3` total-rank false-positive control;
- the 27-monomial, rank-7 Cayley quotient with the mandatory
  `det(M_g)/det(A_g)` residue orientation and scalar-lift replay;
- exact `Dih(C9)` characters and the coefficient-field orbit block
  `{U1,U2,U4}`;
- the fixed-coefficient-prime semisimplification passage, the nonzero virtual
  kernel class `1-chi_(K/Q)`, its finite-dimensional compatible-system
  `K0_ss` category scope, and the split/degree-one density distinction.
- the C53 Route loaded from provenance commit `9d509d3b...`, its exact committed
  byte hash, and its parsed implementation/certificate/payload/check/manifest
  release tuple; no live-Route substring participates in the source lock.

Hostile mutations include wrong edge parity, group order `2n`, generator
order `n`, arbitrary quadric scale, wrong semilinear transport, rotations-only
Reynolds averaging, merged denominators, a falsely certified `n=5` row,
source semisimplicity, exponent `2/n`, total-rank acceptance at `n=3`, retained
`n=8`, inverted residue ratio, altered character traces, split rational orbit
blocks, a zero/generic kernel example, absolute-density-one wording, virtual
restriction injectivity, each committed C53 Route provenance component, and
every forbidden global analytic claim.

The checker and producer also reject optimized Python (`-O` or
`PYTHONOPTIMIZE=1`) before any certificate can be blessed.  Failure removes an
exact pre-existing stale output; successful writes use a same-directory
temporary followed by replacement.

The atomic tests pass rollback after moves 1, 2, 3, and 4, a pre-existing
missing target, a missing source, duplicate targets, and a successful commit.
This is rollback atomicity / exception safety for the tested four-artifact
local protocol; it is not a claim of power-loss atomicity.

Canonical replay command:

```bash
./code/run_c54.sh
```

The persistent scoped baseline has **11/11 manifest entries**: seven release
code files and four release result files, excluding both manifests.  The frozen
full-project baseline has **44/44 manifest entries**, including that scoped
manifest.  The default executable is `./code/run_c54.sh`; it regenerates the
certificate and independent check under a temporary directory, compares them
byte-for-byte with the release copies, checks byte identity of the root and
archived Route-A records, and verifies both inventories without modifying
stable bytes.
