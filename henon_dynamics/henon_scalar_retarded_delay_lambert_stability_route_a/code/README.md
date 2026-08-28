# C210 executable contract

Run from this directory or the repository root:

```text
python3 code/c210_delay_producer.py
python3 code/c210_delay_checker.py
python3 code/c210_delay_sympy_crosscheck.py
python3 code/c210_delay_replay.py
python3 code/c210_delay_mutation.py
python3 code/c210_release_manifest.py
```

The checker is producer-independent and enforces exact recursive key closure,
case/time uniqueness, source formulas, scope flags and the Route-A tuple.
The mutation suite repairs hashes for semantic attacks and separately retains
one stale-hash attack.
