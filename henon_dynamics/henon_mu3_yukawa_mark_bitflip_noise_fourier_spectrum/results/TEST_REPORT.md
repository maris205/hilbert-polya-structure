# C82 test report

```text
producer: PREFREEZE_G3_PASS
independent Walsh/noise checker: C82_INDEPENDENT_CHECK_PASS
active-coordinate SymPy cross-check: C82_SYMPY_CROSSCHECK_PASS
clean replay: C82_REPLAY_PASS
hostile mutations: C82_MUTATION_TEST_PASS (13/13 rejected)
```

The checker re-evaluates the generation predicate and C78 distance-zero
boundary on every mask before recomputing the transform and autocorrelation.
