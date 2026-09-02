# Code contract

- `c286_numbers_game_producer.py`: exact positive-coordinate firing simulator
  and canonical evidence writer.
- `c286_numbers_game_checker.py`: producer-independent positive-root, Weyl,
  inversion, longest-element, parabolic and quotient reconstruction, with an
  all-depth duplicate-rejecting JSON loader, exact contracts/schemas, strict
  types, and complete unique row grids.
- `c286_numbers_game_sympy_crosscheck.py`: symbolic reflection-matrix and root
  controls.
- `c286_numbers_game_replay.py`: two fresh-path byte-for-byte producer replays.
- `c286_numbers_game_mutation.py`: raw duplicate-key and repaired-hash
  semantic/schema/type/drop-replace attacks plus a stale-hash control.
- `c286_release_manifest.py`: exact evidence/YAML contract, ledger, all-round
  text, fresh-build PDF, font and settled-log release gate.

Run scripts with `python3 -B` so no bytecode sidecars enter the 28-file
physical ledger.  Only the producer writes the evidence receipt.  The checker
does not import the producer and does not validate branches by replaying the
stored firing simulation.
