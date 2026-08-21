# C81 test report

```text
producer: PREFREEZE_G3_PASS
independent effective-group checker: C81_INDEPENDENT_CHECK_PASS
weighted-orbit/Burnside arithmetic check: C81_SYMPY_CROSSCHECK_PASS
clean replay: C81_REPLAY_PASS
hostile mutations: C81_MUTATION_TEST_PASS (14/14 rejected)
```

The checker rederives the effective group from C75 generators, reconstructs
all closure/profile values, and compares every orbit representative and size.
