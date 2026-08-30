# C245 reproducibility code

`c245_pulse_if_producer.py` emits the exact transformed-coordinate event,
avalanche, cluster, and synchronized-cycle receipt for the frozen (r,epsilon,N)
grid.  `c245_pulse_if_checker.py` independently reconstructs every row;
`c245_pulse_if_sympy_crosscheck.py` checks the rise inverse and event identities;
`c245_pulse_if_replay.py` checks byte equality in fresh trees; and
`c245_pulse_if_mutation.py` rejects 41 hostile repaired/stale-hash mutations.
`c245_release_manifest.py` closes the 28-file ledger and PDF checks.

All scripts are deterministic with `PYTHONDONTWRITEBYTECODE=1`; generated
bytecode and LaTeX sidecars are excluded.  The receipt is finite source-local
evidence and contains no target arithmetic data.
