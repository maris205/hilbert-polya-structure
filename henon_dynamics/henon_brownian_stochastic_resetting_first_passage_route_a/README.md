# HCS-C214 — Brownian resetting first-passage atlas

This package freezes a one-dimensional Brownian motion with diffusivity
`D>0`, Poisson resets of rate `r>0` to the origin, and an absorbing target
`a>0`, started at the reset point.  It closes one source-level theorem: the
free (unkilled) renewal propagator and its stationary Laplace density, the
killed-search first-passage and survival transforms, the mean hitting time,
the unique positive optimal reset rate, and the singular parameter limits.

The free process and the killed search are separate realizations.  The
stationary density belongs only to the free process on `R`; after absorption
the killed process is sub-Markov and has no such stationary claim.  The
denominator in the first-passage transform is a renewal resolvent, never a
dynamical zeta or a Fredholm determinant.

## Reproduce

From this directory:

```bash
python -B code/c214_brownian_producer.py
python -B code/c214_brownian_checker.py
python -B code/c214_brownian_sympy_crosscheck.py
python -B code/c214_brownian_replay.py
python -B code/c214_brownian_mutation.py
python -B code/c214_release_manifest.py
```

The producer prints the canonical payload hash.  The release manifest records
the evidence, three deterministic manuscript PDFs, and every non-sidecar
file hash.

## Route-A boundary

```text
scope: NO_BAD_EULER_OR_ROOT_NUMBER
tuple: (A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)
overall: ROUTE_A_REJECTED
route_b_invocation_allowed: false
```

Resetting is a stochastic first-passage model with no intrinsic rational-prime
carrier, primitive periodic-orbit owner, arithmetic divisor, or natural
Hilbert–Pólya lift.  No target prime/zero table, local arithmetic, Euler
factor, root number, automorphy object, or Route-B input is used.

## Files

* `THEOREM_PACKAGE.md` — frozen definitions, theorem, proof/evidence boundary,
  and source attribution.
* `code/` — independent producer, recursive checker, symbolic audit, replay,
  hostile mutation harness, and release-manifest builder.
* `results/` — machine-readable evidence and audit reports.
* `paper/` — three substantive revision PDFs and the final deterministic build.
* `evaluations/route_a/HCS-C214/` — evaluator tuple and artifact links.
