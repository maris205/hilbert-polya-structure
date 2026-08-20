# C78 pilot report

Status: **PREFREEZE_G3_PASS**.

Using the C75 coordinates and C76 closure convention, an independent exact
enumeration of all 65536 masks gives

```text
rho_max = 3
rho distribution = {0: 30400, 1: 32704, 2: 2368, 3: 64}
P(x,1) = (1+x)^16
P(1,y) = 30400 + 32704 y + 2368 y^2 + 64 y^3
```

Here `x` marks deleted-label cardinality and `rho` is the minimum number of
deleted labels restored.  The complete coefficient table is in
`THEOREM_PACKAGE.md` and `results/RESULTS.md`; each row sums to
`binomial(16,k)`.

The producer, independent checker, algebraic cross-check, clean replay,
hostile mutation test, and deterministic paper builds all pass.  The hostile
 audit rejected 19/19 semantic mutations.  The canonical evidence SHA-256 is
`728d6462b337e3b22fe267ae9388da476a0f6409cc64a17ca659f53f1a8126ae`;
the final manifest is sealed only after the complete file set is hashed.

Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.
