# C77 hostile audit

The hostile audit is designed to catch plausible but mathematically wrong
releases.  Mutation families include:

```text
C76 authority hashes or schema/scope identifiers
subgroup order or subgroup-index ordering
label-containment counts n_H
one incidence relation K <= H
one Möbius coefficient
one cumulative exponent
one direct support total or support-size count
one exact-closure coefficient vector
the q variable convention or top factorization
```

Each mutated evidence object remains valid JSON but must be rejected by the
independent checker.  In particular, replacing the actual twenty-subgroup
poset by an abstract isomorphic ordering, or silently using a retained-label
probability in place of the deletion variable `q`, is a required rejection.

The implemented audit rejected 25/25 mutations, including all bound source hashes,
subgroup row semantics, incidence and Möbius entries, support totals,
polynomial coefficients, probability-grid metadata, and claim flags.

The audit does not broaden the claim: it only certifies semantic integrity of
the finite Möbius/reliability computation.  Scope firewall:
`NO_BAD_EULER_OR_ROOT_NUMBER`.
