# Code map

- `c127_uniform_horseshoe_producer.py`: deterministic exact evidence producer.
- `c127_uniform_horseshoe_checker.py`: independent invariant checker.
- `c127_sympy_crosscheck.py`: separate symbolic-algebra cross-check.
- `c127_replay.py`: byte-for-byte deterministic replay.
- `c127_mutation.py`: hostile evidence-mutation suite.
- `c127_release_manifest.py`: closed SHA-256 release ledger.

All scripts use exact integers or rational arithmetic for the frozen audit
grid.  SymPy is used only by the separate cross-check.
