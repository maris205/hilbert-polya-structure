# Code lanes

- `c336_crow_kimura_producer.py`: deterministic exact evidence.
- `c336_crow_kimura_checker.py`: independent reconstruction and strict JSON/
  YAML validation; it imports no producer code.
- `c336_crow_kimura_sympy_crosscheck.py`: direct symbolic characteristic and
  root-count lane.
- `c336_crow_kimura_replay.py`: two isolated byte-identical replays.
- `c336_crow_kimura_mutation.py`: repaired-hash mathematical and parser
  attacks.
- `c336_release_manifest.py`: full no-write release and 27-payload manifest
  gate.

Every executable refuses optimized Python because assertions are part of the
integrity contract.
