# Exact Audit Implementation

This directory implements the source-locked, CPU-only algebra audit for
`pcf_quadratic_prime_multiplier_obstruction_v1`.  It has no network, prime
table, Riemann-zero, floating-orbit, or GPU dependency.

Run the frozen workflow from the paper project root:

```bash
python code/scripts/run_exact_audit.py --max-period 4
pytest -q
```

The CLI enforces the declared order:

1. validate and hash `experiments/source_lock.json`, then statically audit the
   executable tree;
2. audit the proof boundary and run all three controls;
3. validate the parameter, exact conjugacy, and derivative content;
4. and only then compute candidate dynatomic and multiplier polynomials for
   the frozen periods `1,2,3,4`;
5. rerun the independent `f_u` coordinate pipeline and audit the branchwise
   cotangent relation.

The principal pure APIs are:

- `prime_multiplier.algebra`: cubic-field and polynomial primitives;
- `prime_multiplier.dynatomic`: formal dynatomic construction and repeated
  lower-period saturation;
- `prime_multiplier.resultant`: chain multipliers, point resultants,
  cycle-polynomial perfect-power verification, and simultaneous rational-root
  certification in the basis `1,u,u^2`;
- `prime_multiplier.controls`: the frozen `c=0,-2,-3/4` controls.

All exact outputs are serialized under `results/`.  The all-period conclusion
comes from the proof package; the finite audit is an implementation
certificate.  In particular, the code always preserves the status
`p=2 exponent-prime for n>=2: OPEN`.

