# SD-C14 implementation notes

- Entry point: `code/sdc14_haar_fiber_experiment.py`.
- Tests: `code/test_sdc14_haar_fiber_experiment.py` (9 deterministic tests).
- Python standard library, NumPy, and pytest only; no network or target data.
- Cyclic moments are evaluated by divisibility, not floating root sums.
- The Haar FK integral uses a 65536-point midpoint grid only as an independent
  check of the exact Jensen formula.
- Formal recurrent coefficients and all theorem formulas are serialized in
  `results/summary.json`; flat audit rows are duplicated in CSV.
- Random increasing inventory uses the single frozen seed embedded in code.
- Re-running the entry point deterministically overwrites only the seven
  generated result data files; checksums are frozen after the run.
