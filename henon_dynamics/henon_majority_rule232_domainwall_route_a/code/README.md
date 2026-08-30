# C251 executable evidence

All scripts are target-blind and use `python3 -B` with
`PYTHONDONTWRITEBYTECODE=1`.

- `c251_majority_producer.py` writes the exact JSON evidence: all-size fixed
  formula rows, parity-twisted run traces, exhaustive state summaries through
  (n=14), and replay trajectories.
- `c251_majority_checker.py` reconstructs the rule, wall map, transfer
  matrices, and every stored row without importing producer functions.
- `c251_majority_sympy_crosscheck.py` independently factors the pair-graph
  characteristic polynomial and verifies all transfer traces.
- `c251_majority_replay.py` checks a clean-process byte-identical producer
  replay.
- `c251_majority_mutation.py` applies 40 semantic, stale-hash, unknown-key,
  provenance, and scope mutations; every one must be rejected.
- `c251_release_manifest.py` reruns all gates and closes the 27-file payload
  ledger after PDF compilation.

No script reads target primes/zeros or any arithmetic local data.
