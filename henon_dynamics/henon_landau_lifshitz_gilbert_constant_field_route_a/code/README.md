# C234 code

`c234_llg_producer.py` writes the deterministic evidence receipt.
`c234_llg_checker.py` independently reconstructs it.  `c234_llg_sympy_crosscheck.py`
checks symbolic identities, `c234_llg_replay.py` checks byte determinism,
`c234_llg_mutation.py` runs 37 hostile tamper tests (including repaired-hash
boundary-row and citation semantics), and
`c234_release_manifest.py` closes the 27-payload manifest.

All commands are run with `python3 -B` and `PYTHONDONTWRITEBYTECODE=1`.
