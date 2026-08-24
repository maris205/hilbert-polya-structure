# Test report

```text
python3 code/c132_mobius_bergman_producer.py  PASS
python3 code/c132_mobius_bergman_checker.py   PASS (2,046 exact word receipts)
python3 code/c132_sympy_crosscheck.py         PASS (2,561 exact checks)
python3 code/c132_replay.py                   PASS
python3 code/c132_mutation.py                 PASS (37/37 rejected)
```

The independent checker does not import the producer.  It reconstructs disk
geometry, every word matrix and case digest, primitive counts, trace sums,
anagram matrices, route labels, exact receipt schemas, and scope flags.  SymPy separately verifies
fixed-point equations, discriminants, multiplier/derivative relations, trace
weights, exact bounds, and the non-cyclic control.  All 36 semantic mutations
has its payload hash repaired before validation; one final mutation attacks
the unrepaired hash itself.
