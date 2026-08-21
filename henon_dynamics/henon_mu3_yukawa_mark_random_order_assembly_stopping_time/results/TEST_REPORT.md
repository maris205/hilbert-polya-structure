# C83 test report

```text
producer: PREFREEZE_G3_PASS
independent pivotal-prefix checker: C83_INDEPENDENT_CHECK_PASS
SymPy stopping-polynomial cross-check: C83_SYMPY_CROSSCHECK_PASS
clean replay: C83_REPLAY_PASS
hostile mutations: C83_MUTATION_TEST_PASS (15/15 rejected)
```

The independent checker rebuilds all closure values and verifies every stored
cardinality, pivotal pattern, permutation count, probability, survival count,
and expectation entry.
