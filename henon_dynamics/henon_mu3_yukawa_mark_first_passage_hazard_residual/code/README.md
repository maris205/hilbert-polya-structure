# C94 code

- `c94_first_passage_hazard_residual.py`: canonical evidence producer.
- `c94_first_passage_hazard_residual_checker.py`: independent bitset and
  semantic reconstruction.
- `c94_sympy_crosscheck.py`: exact SymPy checks over the hazard and residual
  grids.
- `c94_replay_checker.py`: clean deterministic replay.
- `c94_mutation_test.py`: hostile semantic mutation suite.
- `c94_release_manifest.py`: deterministic file-hash ledger.

Run from this directory with `python -B <script>`.  All scripts are bound to
`NO_BAD_EULER_OR_ROOT_NUMBER` and the frozen C88 input hashes.
