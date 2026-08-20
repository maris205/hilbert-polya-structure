# C78 test report

The computational release gates are:

```text
producer: PREFREEZE_G3_PASS
independent checker: PASS (after direct C73/C75/C76/C77 authority lock)
SymPy cross-check: SYMPY_CROSSCHECK_PASS
clean replay: REPLAY_PASS (after direct C73/C75/C76/C77 authority lock)
hostile semantic mutations: MUTATION_TEST_PASS (19/19 rejected)
```

The checker independently verifies all inherited authority bytes, the
point-set closure transitions, 25 full-core minimal supports, the projective
block decomposition, every one of the 65536 deletion masks, both marginal
polynomials, and the exact coefficient table.  The replay preserves the
evidence digest in a fresh interpreter.  Mutation families include source
hashes, schema/scope/status, pivot and block sizes, formula and distance
counts, a distance-three mask, a coefficient, both marginals, and a claim
flag; all 19 mutations are rejected, including direct C76 evidence and
manifest bindings.

Canonical evidence SHA-256:
`728d6462b337e3b22fe267ae9388da476a0f6409cc64a17ca659f53f1a8126ae`.
Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.
