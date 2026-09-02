# Code

- `c289_magnetic_producer.py`: deterministic canonical evidence producer.
- `c289_magnetic_checker.py`: strict duplicate-rejecting JSON/YAML checker that rebuilds the raw Lorentz matrix, basepoint return equations, and never imports producer code.
- `c289_magnetic_sympy_crosscheck.py`: separate symbolic reconstruction.
- `c289_magnetic_replay.py`: two fresh-path byte replays.
- `c289_magnetic_mutation.py`: repaired-hash semantic/schema attacks, raw duplicate-key attack, and stale-hash control.
- `c289_release_manifest.py`: full evidence, manuscript, six-build, font/text/log, and ledger gate.

All scripts use only deterministic data.  Run `python3 code/c289_release_manifest.py` from any working directory.
