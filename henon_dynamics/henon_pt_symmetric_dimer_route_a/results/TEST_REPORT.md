# Test report — C297

Commands and settled results:

```text
python -B code/c297_pt_dimer_producer.py          PASS (168 + 8 cells)
python -B code/c297_pt_dimer_checker.py           PASS (6,475 assertions)
python -B code/c297_pt_dimer_sympy_crosscheck.py  PASS (516 checks)
python -B code/c297_pt_dimer_replay.py            PASS (2 fresh paths)
python -B code/c297_pt_dimer_mutation.py          PASS (52/52 attacks)
```

The checker is producer-independent and reconstructs the full grid by exact
integer and rational arithmetic.  The symbolic script independently verifies
the scalar square, characteristic polynomial, both metric intertwinings,
Riccati field, discriminant sign, and all three propagator ODEs.

The release gate additionally checks strict evaluation YAML, source/scope
locks, three distinct manuscript rounds, two fresh deterministic builds of
each round, embedded subset fonts, text sentinels, absence of build sidecars,
and the exact 27-payload / 28-physical-file ledger.

The strict evaluation semantic SHA-256 after freezing `HEN-O281` is
`fcee5ce61bdedc783e4827d3800d43aadee5d9549a3f092ebfc8b29c62527ea1`.
