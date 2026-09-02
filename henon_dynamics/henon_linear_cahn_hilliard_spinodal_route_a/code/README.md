# C304 code lanes

- `c304_ch_producer.py` writes deterministic exact and high-precision receipts.
- `c304_ch_checker.py` independently reconstructs every theorem-facing row and the exact Route-A YAML tree; it imports no producer code and refuses optimized Python.
- `c304_ch_sympy_crosscheck.py` checks the Fourier, energy, tie, cutoff, and singular-face identities symbolically.
- `c304_ch_replay.py` runs two isolated producers and requires byte identity with the archive.
- `c304_ch_mutation.py` applies repaired-self-hash semantic attacks plus hostile JSON/YAML parser attacks.
- `c304_release_manifest.py` runs all gates, builds and audits each of the three round variants twice, verifies the final Round-2 alias, and closes the 27-payload manifest.

Run every command with ordinary `python -B`; the checker and release closer
explicitly reject optimized Python, and no `python -O` support is claimed for
the remaining lanes.
