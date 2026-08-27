# Hostile audit

The mutation harness does not merely corrupt hashes.  It repairs the payload
hash after each of 33 semantic/schema attacks and requires the
producer-independent checker to reject all of them.  The frozen attacks are:

1. source commit, evaluator hash, and scope-literal corruption;
2. unknown top-level and nested-theorem keys;
3. expansion of the frozen profile class;
4. corruption of the porous, pressure, rescaled, free-energy, dissipation,
   and uniqueness theorem fields;
5. `mass_beta=0` and a joint chemical-constant/all-sample corruption;
6. duplicate or missing cases, a corrupt case id, an expanded `m` grid,
   duplicate `z`, and duplicate `r`;
7. working-precision, serialized-precision, and decimal-format corruption;
8. fast-support, heat-Beta, and porous-exterior-chemical null-rule attacks;
9. moment-status and finite-coefficient/null corruption;
10. Route tuple and strongest-positive promotion, a forbidden scope flag,
    citation corruption, and a cleared nonclaim list.

A separate changed-headline attack retains its stale payload hash and is also
rejected, for 34 total hostile rejections.  Passing this declared audit is not
a general security proof.
