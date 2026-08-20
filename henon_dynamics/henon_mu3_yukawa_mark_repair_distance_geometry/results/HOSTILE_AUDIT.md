# C78 hostile audit

The hostile test keeps each mutated receipt valid JSON but changes a semantic
value.  It rejects all 19 cases:

```text
schema, status, scope, c77 authority, c77 manifest, c76 authority,
c76 manifest, c73 authority,
structural formula, pivot, block size, maximum distance, distance marginal,
retained-cardinality row, distance-three mask, coefficient, x marginal,
y marginal, exact-distance claim.
```

This checks that a plausible-looking but wrong convention (for example,
marking retained rather than deleted labels with `x`, or changing the pivot)
cannot pass.  The audit is an integrity gate, not an expansion of the
mathematical claim.  Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.
