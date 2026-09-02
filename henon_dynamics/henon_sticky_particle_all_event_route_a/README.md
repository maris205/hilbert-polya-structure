# HCS-C292 — finite sticky-particle all-event dynamics

This package proves a complete forward theorem for arbitrary finite positive
point masses on the line.  Initial coincidences are premerged; binary,
multi-cluster, and disjoint simultaneous collisions use one maximal-block
rule.  Weighted isotonic projection and a cumulative-mass lower convex hull
give the same flow, with exact conservation, dissipation, and pressureless-
Euler weak closure.

Both the evidence JSON and the Route-A evaluation YAML are checked against
exact nested key/type/value contracts.  Duplicate keys are rejected before
deserialization, and the parsed evaluation is locked by a canonical semantic
SHA-256.

The result is `PROVABLE AS STATED`.  It closes source-dynamics obstruction
`HEN-O276`, but every Route-A axis fails: the verdict is
`ROUTE_A_REJECTED`, Route B is disabled, and the literal scope is
`NO_BAD_EULER_OR_ROOT_NUMBER`.

## Reproduce

Run from this directory:

```bash
python -B code/c292_sticky_producer.py
python -B code/c292_sticky_checker.py
python -B code/c292_sticky_sympy_crosscheck.py
python -B code/c292_sticky_replay.py
python -B code/c292_sticky_mutation.py
python -B code/c292_release_manifest.py
```

The last command reruns every gate, rebuilds all three retained manuscript
rounds twice in fresh directories, audits logs/fonts/pages/text/hashes, and
closes the exact 27-payload/28-physical-file ledger.
