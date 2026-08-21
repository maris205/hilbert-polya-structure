# C80 test report

```text
producer: PREFREEZE_G3_PASS
independent target-antichain checker: C80_INDEPENDENT_CHECK_PASS
SymPy/cardinality cross-check: C80_SYMPY_CROSSCHECK_PASS
clean replay: C80_REPLAY_PASS
hostile mutations: C80_MUTATION_TEST_PASS (13/13 rejected)
```

The checker locks C75/C76/C78 evidence and manifests, rebuilds the 20 subgroup
rows and closure transition system, derives each target antichain, and checks
all 1,310,720 threshold entries plus distributions and cardinality tables.
