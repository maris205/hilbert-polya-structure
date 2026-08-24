# Test report

```text
python3 code/c131_odd_metaplectic_producer.py  PASS
python3 code/c131_odd_metaplectic_checker.py   PASS (25,313 Egorov cases)
python3 code/c131_sympy_crosscheck.py          PASS (50,670 exact checks)
python3 code/c131_replay.py                    PASS
python3 code/c131_mutation.py                  PASS (30/30 rejected)
```

The producer and checker share no imports.  The checker reconstructs every
case digest, matrix receipt, action window, phase convention, nonclaim, route
label, and scope flag.  The mutation total is 29 repaired-hash cases plus one
stale-hash checksum case.  The original 25 repaired-hash semantic cases are
retained; four new repaired-hash cases close top-level, check-map, scope-map,
and certified-receipt schema blind spots.
