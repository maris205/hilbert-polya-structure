# HCS-C299 — Lamb--Oseen radial self-similarity

This 28-file release package proves a complete theorem for the bounded-at-origin, finite-circulation, radial forward-self-similar class of the two-dimensional viscous vorticity equation.  It contains the analytic theorem, exact finite regression evidence, an independent checker, a symbolic cross-check, byte replay, hostile mutations, a strict Route-A YAML evaluation, three substantive manuscript revisions, and a closed-world release manifest.

## Reproduce

From this directory:

```bash
PYTHONDONTWRITEBYTECODE=1 TZ=UTC python -B code/c299_lamb_oseen_producer.py
PYTHONDONTWRITEBYTECODE=1 TZ=UTC python -B code/c299_lamb_oseen_checker.py
PYTHONDONTWRITEBYTECODE=1 TZ=UTC python -B code/c299_lamb_oseen_sympy_crosscheck.py
PYTHONDONTWRITEBYTECODE=1 TZ=UTC python -B code/c299_lamb_oseen_replay.py
PYTHONDONTWRITEBYTECODE=1 TZ=UTC python -B code/c299_lamb_oseen_mutation.py
PYTHONDONTWRITEBYTECODE=1 TZ=UTC python -B code/c299_release_manifest.py
```

The final command reruns every gate, performs two fresh deterministic LuaLaTeX builds for each of three rounds, and rewrites `C299_RELEASE_MANIFEST.json` only after all checks pass.

## Scope

The scope literal is `NO_BAD_EULER_OR_ROOT_NUMBER`.  The honest Route-A tuple is five failures; no target arithmetic data or Hilbert--Polya operator is claimed.
