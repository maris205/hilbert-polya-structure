# C231 test report

Commands and expected settled outputs:

```text
python3 -B code/c231_allen_cahn_producer.py
  C231_PRODUCER_PASS; epsilon_rows=5; speed_rows=5; profile_rows=5
python3 -B code/c231_allen_cahn_checker.py
  C231 independent checker: PASS (204 assertions)
python3 -B code/c231_allen_cahn_sympy_crosscheck.py
  C231 SymPy cross-check: PASS (13 symbolic identities)
python3 -B code/c231_allen_cahn_replay.py
  C231 byte replay: PASS
python3 -B code/c231_allen_cahn_mutation.py
  C231 hostile mutations: PASS 21/21
```

The checker is producer-independent.  Mutation coverage includes front and
spectral values, theorem text, route tuple, scope flags, citation metadata,
nested unknown keys, a missing row, and a stale payload hash.

Settled receipt SHA-256: `c1325b24b9e2d5bf96d68b0a5db193e2125b733860a36b8bf34e30c858c1af2f`.
Release PDF SHA-256: `65c3b37e47c36442fa9faebc694eaf4c3b59fd31831a89d50b66d71c3d9f578f`.
