# Test report

```text
C282_PRODUCER_PASS
C282 independent checker: PASS (4487 assertions; producer-independent root and transform reconstruction)
C282_SYMPY_PASS (15 symbolic identities; independent Gerber-Shiu reconstruction)
C282 byte replay: PASS (349745 bytes)
C282 hostile mutation audit: PASS 26/26
```

Coverage includes all 36 small rational loading triples, seven named model
cases, four reserves, four discounts, four deficit penalties, both finite
conditional-first-mean formulas, critical infinite mean, no claims, zero reserve,
adjustment roots, supremum atom/tails, source/evaluator/epoch/scope locks, and
all forbidden claim flags.

The checker imports no producer code.  SymPy reconstructs the coefficient
equations separately.  Replay uses a new temporary path.  Twenty-five
semantic mutations receive repaired hashes, so rejection exercises meaning
rather than only integrity metadata; one stale-hash control checks ordinary
integrity.
