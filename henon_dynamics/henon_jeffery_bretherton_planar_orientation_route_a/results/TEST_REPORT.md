# Test report

All commands were run with `PYTHONDONTWRITEBYTECODE=1` from the package root.

```text
C280_PRODUCER_PASS
C280 independent checker: PASS (8328 assertions; producer-independent reconstruction)
C280_SYMPY_PASS (39 symbolic identities; independent Cayley-Hamilton reconstruction)
C280 byte replay: PASS (625635 bytes)
C280 hostile mutation audit: PASS 25/25
```

Coverage includes all 625 points of the declared rational flow/shape grid,
eight curated generators across every regime, ten nonzero initial directions,
four times, reciprocal aspect ratios, head–tail versus oriented periods,
half/full strobes, marked-sphere/rod/disk limits, exact orbit/shear/strobe key
sets, full boundary semantics, scope flags, tuple locks, and hash integrity.

The checker is producer-independent.  SymPy uses a separately written
symbolic derivation.  Replay writes to a temporary directory.  Mutation tests
include repaired payload hashes, duplicate/drop-replace rows, and convention
attacks, so rejection cannot be attributed merely to stale integrity metadata.
