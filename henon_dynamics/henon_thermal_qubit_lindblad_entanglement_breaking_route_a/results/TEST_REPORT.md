# Test report

The canonical run passes:

```text
C303_PRODUCER_PASS (124 audited rows)
C303 independent thermal-qubit checker: PASS (strict JSON/YAML exact tree)
C303 SymPy cross-check: PASS
C303 byte replay: PASS
C303 hostile mutation suite: PASS 35/35
```

The checker is source-independent from the producer and reconstructs every
rational Choi, Liouvillian, contraction, and semigroup row.  Threshold roots
are enclosed by opposite signs in intervals narrower than `1e-70`; their
dimensionless times and residual bounds are separately checked.  Type attacks
include Python's `bool`/`int` trap.  Raw attacks include duplicate keys and
nonfinite JSON.  Semantic attacks have their payload hashes repaired before
checking so that rejection cannot be attributed only to a stale digest.

The final release script also performs two isolated, two-pass LuaLaTeX builds
for each of three paper rounds, checks byte identity, settled warning logs,
embedded/subset fonts, extractable text, rasterizability, final/round-2
identity, exact file count, and manifest closure.
