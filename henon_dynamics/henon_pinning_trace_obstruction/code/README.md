# Code

- `certify_pinning_obstruction.py`: canonical exact-rational producer.
- `check_pinning_obstruction.py`: independent reconstruction and tamper
  checker; it does not import the producer.
- `PROTOCOL.md`: frozen obligations and expected-fail controls.

The scripts use only the Python standard library and print JSON to standard
output with `--json`.
