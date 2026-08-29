# C236 code

`c236_sine_gordon_producer.py` writes the deterministic evidence receipt.
`c236_sine_gordon_checker.py` independently reconstructs it without importing
the producer.  `c236_sine_gordon_sympy_crosscheck.py` checks exact symbolic
identities, `c236_sine_gordon_replay.py` checks byte determinism,
`c236_sine_gordon_mutation.py` runs hostile tamper tests (including citation
issue/DOI, all boundary-row semantics, and nested unknown/stale-hash attacks),
with repaired payload hashes for semantic edits, and
`c236_release_manifest.py` closes the 27-payload manifest.

Run all Python commands with `python3 -B` and
`PYTHONDONTWRITEBYTECODE=1`.
