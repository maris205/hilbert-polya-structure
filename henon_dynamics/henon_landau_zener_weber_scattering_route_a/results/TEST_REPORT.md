# Test report

Run from the package root:

```text
python3 -B code/c224_landau_zener_producer.py
python3 -B code/c224_landau_zener_checker.py
python3 -B code/c224_landau_zener_sympy_crosscheck.py
python3 -B code/c224_landau_zener_replay.py
python3 -B code/c224_landau_zener_mutation.py
```

The producer and checker agree on the canonical payload.  The checker is
producer-independent and validates all 5 scattering and 15 finite-window
rows.  SymPy performs the generic scalar/Pauli/SU(2) checks; replay compares
clean-process bytes.  Mutation output records 20 repaired-hash rejections,
two unknown-key rejections, and one stale-hash rejection.  All scope flags are
false and Route B is disabled.
