# Test report

## Exact evidence

```text
C301 independent checker PASS (3570 assertions)
payload_sha256=1fcd7d727f3fd75ce99257c2ee69c6ecc7ff2332ad582628ad72ac9473043c10
route_tuple=A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL
```

The checker is independent of the producer.  It generates labelled set
partitions by block insertion rather than restricted-growth recursion and
derives nonzero transitions from the refinement predicate rather than fair-bit
enumeration.

## Symbolic cross-check

```text
C301 SymPy exact cross-check PASS (17910 symbolic/cell assertions)
verified: characteristic polynomials, determinants, squarefree annihilators,
eigenspaces, semigroup kernels, occupancy moments
```

## Replay and mutations

```text
C301 deterministic replay PASS (two fresh runs and archived bytes identical)
evidence_sha256=011f146e1fecfb88a6cc4a692d95a8267b9549cfefa43628083ab1aa21b06a03
C301 mutation suite PASS (57/57 semantic/parser mutations killed)
classes=metadata,formula,kernel,spectrum,absorption,lattice,route,scope,JSON,YAML
```

## Release-level gates

The final release audit additionally requires two fresh byte-identical builds
of each of the three distinct paper rounds, embedded fonts, no LaTeX layout or
reference warnings, exact Route-A YAML-tree equality, the scope firewall, and
the exact 27-payload/28-physical-file ledger.  Exact PDF and manifest hashes are
recorded in `paper/COMPILE_REPORT.md` and `C301_RELEASE_MANIFEST.json`.
