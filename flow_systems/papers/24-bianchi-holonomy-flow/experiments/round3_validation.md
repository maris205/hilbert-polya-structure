# P24 Round-3 validation report

## Material Passport

- Origin Skill: experiment-agent
- Origin Mode: run + validate
- Origin Date: 2026-08-27
- Verification Status: VERIFIED
- Version Label: p24_round3_validation_v1

## Reproducibility verdict

- Determinism class: deterministic exact Gaussian-rational core outputs with
  deterministic floating transcendental evaluation under the recorded Python
  runtime.
- Verdict: `REPRODUCIBLE`.
- Core-output combined SHA-256:
  `3fa2c5df0093a89da7fe92234c7cbfe900e641caf72ced8019e5240073f81d8a`.
- The generator compares two independent in-process payload builds before
  writing.  The full nine-test suite was executed twice, and the frozen files
  were independently checked with `--verify-existing`.

## Executed commands

```bash
PYTHONDONTWRITEBYTECODE=1 python3 code/test_round3_schottky_control.py -v
PYTHONDONTWRITEBYTECODE=1 python3 code/round3_schottky_control.py
PYTHONDONTWRITEBYTECODE=1 python3 code/test_round3_schottky_control.py -v
PYTHONDONTWRITEBYTECODE=1 python3 code/round3_schottky_control.py
PYTHONDONTWRITEBYTECODE=1 python3 code/round3_schottky_control.py --verify-existing
```

All commands exited `0`.  Each test execution reported `9/9` passing.  No
stall, crash, timeout, or output anomaly was observed.

## Exact checks

- Closed paired round disks: 8.
- Exact pairwise closed-disk inequalities: 28/28 positive.
- Minimum exact squared separation gap: `10201/10101`.
- Exact forward/inverse conjugacy identities: 8/8.
- Exact boundary modulus identity: passed.
- Freely reduced words including identity: 22,409.
- Unique exact projective matrices: 22,409.
- Oriented cyclic classes: 4,148.
- Primitive / repetition classes: 4,092 / 56.
- Orientation pairs / self-inverse classes: 2,074 / 0.
- Maximum trace-invariant reconstruction relative residual: `1.097e-14`.
- Forbidden target data used: `false`.

## Core file hashes

- `results/round3_metrics.json`:
  `01206991460e3d2e6167710b1f2283d0aeb2ca1a25a004487de6b3723ad2132e`
- `results/schottky_conjugacy_ledger_round3.csv`:
  `1926823966272165d5dfdd4e1c6028a894755f07fa02e97ee1a2cf88d3339337`
- `results/schottky_holonomy_shuffle_round3.csv`:
  `4265765acd632af1d6fcf1c5818462037303428518a593b12d03c4c5f35202ff`
- `results/schottky_ping_pong_domains_round3.csv`:
  `9e471fd20e3e7dcd982189332d63f4519542ffb0b0515652ff94c2d6cb1396bb`

## Claim boundary

`[PROVED]` applies to the explicit paired-round-disk certificate and its
classical-Schottky consequences.  `[NUMERICALLY_CERTIFIED]` applies to the
finite serialized ledger, deterministic counts, and complex-length residual.
`[NUMERICAL_OBSERVATION]` applies to the intrinsic phase/length scores.

The control is complete only as a marked-word enumeration through length 5.
It is an infinite-volume convex-cocompact non-lattice, not a finite-volume or
cusp-matched Bianchi manifold.  Its possible containment in a larger arithmetic
ambient group is `[OPEN]`.  The arithmetic-hypothesis verdict is `[OPEN]`, the
formal Route-A tuple is `UNASSIGNED`, A2--A4 are `NOT_EVALUATED`, and Route B is
`NOT_RUN` with invocation disallowed.
