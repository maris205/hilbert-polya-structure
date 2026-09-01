# Test report

Commands are run from the package root.

```text
python3 -B code/c269_chebyshev_producer.py
C269_PRODUCER_PASS cases=121 vertices=1914 payload=e787db19f3646c68557f92fa0bfbc16cbf8466bd940fd6034a5cda40c32a4c37

python3 -B code/c269_chebyshev_checker.py
C269 independent checker: PASS (32499 assertions; mode=full)

python3 -B code/c269_chebyshev_sympy_crosscheck.py
C269_SYMPY_PASS (311 symbolic matrix/rank checks across 64 maps)

python3 -B code/c269_chebyshev_replay.py
C269 byte replay: PASS

python3 -B code/c269_chebyshev_mutation.py
C269 repaired-hash mutation gate: PASS 41/41
```

The checker imports no producer.  It verifies every field model's monicity, declared degree and irreducibility over `GF(p)`, and locks one identical model across every degree for fixed `q`.  The mutation gate repairs the outer payload hash after corrupting provenance, route decisions, field models, branch counts, periodic populations, image ranks or Koopman multiplicities, so its rejection is semantic.
