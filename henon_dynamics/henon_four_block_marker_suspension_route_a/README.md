# HCS-C139: four-block marker suspension

This release freezes a full binary suspension whose roof refines the directed
edge clock by the cyclic marker `0011` with coefficient `sqrt(5)`.  Its exact
eight-state determinant is

```text
1-x00-x11-x01*x10+x00*x11+(1-y)*x00*x01*x10*x11.
```

The new theorem is a coding-relative minimal-memory result: the primitive
words `001011` and `001101` have identical cyclic block populations through
width three but different `0011` counts.  The refinement is not orbit
injective; `0101111` and `0110111` retain the same complete clock vector.

Release contents include the complete proof package, exact evidence, an
independent standard-library checker, an independent SymPy reconstruction,
byte replay, repaired- and stale-hash hostile mutations, strict Route-A YAML,
two internal review→fix rounds, four retained PDFs, and a self-excluded
content-addressed manifest.

Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.  The strict verdict is
`(A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`, overall `ROUTE_A_EXPLORATORY`; Route B is
not authorized.
