# C88 test report

```text
producer: PREFREEZE_G3_PASS
independent point-set/minimal-antichain checker: C88_INDEPENDENT_CHECK_PASS
SymPy exact-rational cross-check: C88_SYMPY_CROSSCHECK_PASS
clean deterministic replay: C88_REPLAY_PASS
hostile mutations: C88_MUTATION_TEST_PASS (40/40 rejected)
```

The producer enumerates `65536` support closures and twenty containment
up-sets.  It derives each of the `340` first-passage cells by both exact CDF
differences and pivotal-edge counting.  The independent checker first
enumerates all twenty subgroups from the 54-point group law, then expands
actual point sets, discovers all twenty minimal hitting-support antichains,
reconstructs each complete hit bitset by containment, and compares the entire
canonical receipt.

The SymPy route checks twenty normalized probability generating functions,
their exact derivative expectations, all CDF/survival identities, pivotal
polynomials, and all `102` stochastic-order pairs.  It independently rebinds
the final C83 evidence and compares the top law.
