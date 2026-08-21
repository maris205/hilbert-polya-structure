# C84 test report

```text
producer: PREFREEZE_G3_PASS
independent point-set closure checker: C84_INDEPENDENT_CHECK_PASS
SymPy/finite-graph cross-check: C84_SYMPY_GRAPH_CROSSCHECK_PASS
clean replay: C84_REPLAY_PASS
hostile mutations: C84_MUTATION_TEST_PASS (18/18 rejected)
```

The independent checker rebuilds all 65536 C75 closure values, enumerates
minimum restoration subsets in increasing size for every deletion mask,
matches each direct family to the proposed matroid bases, and checks every
basis-exchange obligation.  It also expands the seven C76 effective-label
orbits and obtains exact equality in the all-deleted case.
