# C240 reproducibility code

`c240_contracted_rotation_producer.py` enumerates all primitive canonical
binary words through length 12 for three rational slopes.  It computes affine
return points, exact half-open parameter intervals, endpoint equality audits,
grouped carry-rotation components, and high-precision iteration probes.

`c240_contracted_rotation_checker.py` reimplements every calculation without
importing the producer.  It verifies 2241 word rows, 138 nonempty components,
and 295 direct probes.  `c240_contracted_rotation_sympy_crosscheck.py` checks
the generic identities and rational interval examples.  `c240_contracted_rotation_replay.py`
checks byte equality in two fresh output trees.  The mutation script repairs
the payload hash after 33 hostile edits and requires all of them to be
rejected.  `c240_release_manifest.py` closes the 28-file ledger and PDF checks.

All scripts are deterministic under `PYTHONDONTWRITEBYTECODE=1`; no generated
bytecode or LaTeX sidecar belongs to the release.  The receipt is source-local
finite-cutoff evidence and contains no target arithmetic data.
