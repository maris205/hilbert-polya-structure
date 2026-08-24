# Test report — C120

Run from the package root:

```text
python3 code/c120_variational_period3_producer.py
python3 code/c120_variational_period3_checker.py
python3 code/c120_sympy_crosscheck.py
python3 code/c120_replay.py
python3 code/c120_mutation.py
```

Release results:

- producer: `PREFREEZE_G3_PASS`;
- independent checker: `C120_INDEPENDENT_CHECK_PASS`;
- direct SymPy cross-check: `29` exact checks passed, including the canonical
  tuple and prime/A2/divisor boundary;
- canonical replay: byte-identical evidence;
- hostile mutation audit: `21/21` mutations rejected.

The checker independently implements the source map, inverse, Jacobian,
action, controls, and evaluator boundary and does not import the producer.
