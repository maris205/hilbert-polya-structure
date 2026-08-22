# Test report

The release sequence is:

```text
producer       PREFREEZE_G3_PASS
checker        C110_CHECK_PASS
SymPy          C110_SYMPY_PASS (39 checks)
replay         C110_REPLAY_PASS
mutation       C110_MUTATION_PASS (10/10 rejected)
```

The checker rebuilds the finite ledger independently; SymPy rebuilds all three
8-by-8 matrices, trace powers, determinant polynomials, and Newton recurrences.
The replay verifies canonical JSON bytes and scope flags.  Mutation cases
cover schema, scope, words, monodromy, traces, decompositions, determinant,
assessment, and forbidden claims.
