# HCS-C29 test report

## Summary

```text
unittest cases                 38 / 38 PASS
independent checker gates      14 / 14 PASS
unimodular inverse fuzz       250 / 250 PASS
floating-point operations       0
external network calls          0
```

Command:

```bash
PYTHONDONTWRITEBYTECODE=1 \
python -m unittest discover \
  -s henon_dynamics/rauzy_groupoid_identity_determinant/code \
  -p 'test_c29.py' -v
```

## Positive regression coverage

- canonical payload and deterministic producer replay;
- complete independent 14-gate replay;
- exact C25 all/primitive/rotation/dihedral census separation;
- both primitive length-six identity witnesses;
- programmatically derived C26 braid and length-24 relation;
- `N_24 >= 48` lower-bound scope;
- identity and torsion repetition bookkeeping;
- `Log_0` determinant germ and common strict disc;
- natural-extension and Route-B firewalls;
- agreement of two independent exact matrix inversions on 250 random
  unimodular matrices;
- fail-closed runner and manifest refresh contract.

## Rehashed mutation coverage

Each semantic mutation below is followed by recomputation of the canonical
payload digest.  Passing envelope integrity is therefore not sufficient; the
independent semantic gate must reject the change.

| Mutation | Required rejecting gate |
|---|---|
| stale digest after candidate-name edit | G13 payload envelope |
| changed C25 source hash | G0 source lock |
| collapsed formal inverse into antiparallel edge | G3 formal inverse semantics |
| reversed chronology enum | G4 chronology |
| changed one C1 path token | G6 C25 witnesses/gauge |
| substituted primitive cycles for all determinant moments | G7 all/primitive census |
| changed one `Delta` matrix entry | G8 C26 relation |
| promoted `N_24 >= 48` to an exact total | G8 C26 relation |
| replaced `Theta(Delta^4)` by `Theta(Delta)^4` | G9 repetition/torsion |
| took the prime limit before fixing path length | G10 finite-Weil limit |
| called the germ an ordinary infinite-dimensional Fredholm determinant | G11 normalized determinant |
| claimed a global primitive Euler product | G11 normalized determinant |
| called the symmetric model the genuine AGY natural extension | G12 semantic firewalls |
| claimed an intrinsic reversible AGY roof | G12 semantic firewalls |
| inserted an unreviewed payload claim | G12 semantic firewalls |
| changed a JSON integer matrix entry to boolean `true` | G8 C26 relation |
| changed a JSON integer matrix entry to a float | G8 C26 relation |
| disabled the AI-disclosure material-passport field | G12 semantic firewalls |
| broadened odd-prime/fixed-length scope | G0 source lock |
| inserted a runtime working-directory field | G12 semantic firewalls |
| inserted unknown graph or witness fields | G3/G6 structural gates |

All mutations were rejected at the required gate.  Additional integration
tests prove path-free checker output, whole-project manifest discovery,
required-file failure on refresh, cache exclusion and protected-file change
detection.  They also lock the checker import graph through Python AST
inspection and exercise uncached CLI success and semantic-failure subprocesses.

## Performance and determinism

The producer and command-line checker use only the Python standard library,
exact integers and `Fraction`.  The release certificate is byte-identical
when generated from the repository root or an unrelated working directory.
The manifest discovers the whole project tree, fails if any required artifact
is missing, and excludes only declared Python/LaTeX caches.  The default
runner rebuilds into a private temporary directory, compares frozen JSON
byte-for-byte, and runs Python in isolated mode with an empty cache prefix.
