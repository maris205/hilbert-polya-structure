# HCS-C215 — Kingman coalescent genealogy atlas

This package freezes the partition-valued Kingman `n`-coalescent for every
sample size `n>=1`.  Each unordered pair of extant blocks merges at rate one.
The block count is therefore a pure-death chain with
`lambda_k = binom(k,2)`.  One all-parameter theorem closes the
hypoexponential transition law, independent exponential holding times and
uniform merger choices, the MRCA Laplace transform and moments, and the total
branch-length Laplace transform, moments, and exact CDF
`(1-exp(-ell/2))^(n-1)`.

The projective coupling is explicit: restricting the `(n+1)`-sample partition
to `[n]` gives the `n`-sample process, so the coupled MRCA times increase to a
finite `T_infinity` almost surely.  Marginal sums are not silently treated as
one common coupling.  Any finite Markov determinant or trace-log is explicitly
not an Artin--Mazur zeta.

## Reproduce

```bash
python -B code/c215_kingman_producer.py
python -B code/c215_kingman_checker.py
python -B code/c215_kingman_sympy_crosscheck.py
python -B code/c215_kingman_replay.py
python -B code/c215_kingman_mutation.py
python -B code/c215_release_manifest.py
```

## Route-A boundary

```text
scope: NO_BAD_EULER_OR_ROOT_NUMBER
tuple: (A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)
overall: ROUTE_A_REJECTED
route_b_invocation_allowed: false
```

Genealogical rates and branch lengths have no intrinsic rational-prime carrier,
primitive orbit clock, arithmetic divisor, or natural Hilbert--Pólya lift.  No
target prime/zero table, local arithmetic, Euler factor, root number,
automorphy object, or Route-B input is used.

## Files

* `THEOREM_PACKAGE.md` — definitions, all-`n` theorem, coupling and evidence
  boundary.
* `code/` — independent producer/checker, symbolic audit, replay, mutation
  harness, and release manifest.
* `results/` — machine-readable certificate and audit reports.
* `paper/` — three substantive revision PDFs and final deterministic build.
* `evaluations/route_a/HCS-C215/` — evaluator tuple and artifact links.
