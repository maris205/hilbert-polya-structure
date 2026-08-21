# C86 test report

```text
producer: PREFREEZE_G3_PASS
independent component-orbit checker: C86_INDEPENDENT_CHECK_PASS
SymPy radial and invariant-spectrum cross-check: C86_SYMPY_CROSSCHECK_PASS
clean-process replay: C86_REPLAY_PASS
hostile semantic mutations: C86_MUTATION_TEST_PASS (20/20 rejected)
```

The producer generates all `1920` faithful label permutations explicitly.
The independent checker instead discovers support-orbit components using only
the five named generators.  It then rebuilds every quotient row, verifies
strong lumpability on all `65536` supports, recomputes both repair-flow
matrices, and compares the complete canonical receipt byte for byte.

The symbolic check proves the 17 radial eigenvalues directly from the
tridiagonal cube operator and verifies palindromicity, dimension, and the
first two spectral moments of the invariant multiplicity polynomial.
