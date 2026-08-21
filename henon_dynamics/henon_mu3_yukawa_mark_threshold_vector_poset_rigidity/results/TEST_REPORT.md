# C85 test report

```text
producer: PREFREEZE_G3_PASS
independent point-set/antichain checker: C85_INDEPENDENT_CHECK_PASS
SymPy and finite-lattice cross-check: C85_SYMPY_LATTICE_CROSSCHECK_PASS
clean replay: C85_REPLAY_PASS
hostile mutations: C85_MUTATION_TEST_PASS (23/23 rejected)
```

The independent checker reconstructs the twenty actual subgroups from the
54-point group law, all `65536` closures, every target-minimal antichain, and
all `1,310,720` threshold entries.  It then compares the complete canonical
receipt, including source hashes, support classes, vector rows, fibre data,
poset matrices, cover relations, checks, and nonclaim flags.
