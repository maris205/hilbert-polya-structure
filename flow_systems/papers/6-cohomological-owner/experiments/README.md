# Reproduction entry point

`reproduce.sh` is the canonical one-command reproduction script for Paper 6.
It first regenerates the deterministic outputs through degree/power 24 and
then runs the ten-test suite with an explicit `PYTHONPATH` that avoids the
Python standard-library `code` module name collision.

Run from this directory:

```bash
bash reproduce.sh
```

or from the workspace root:

```bash
bash papers/6-cohomological-owner/experiments/reproduce.sh
```

Expected terminal result:

```text
Ran 10 tests
OK
```

The run writes five generated artifacts under `../results/` and refreshes
`manifest.sha256.json`.  It is deterministic and offline.
