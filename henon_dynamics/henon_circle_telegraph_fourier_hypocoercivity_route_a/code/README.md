# C213 executable contract

Run from the repository root:

```text
python3 -B code/c213_telegraph_producer.py
python3 -B code/c213_telegraph_checker.py
python3 -B code/c213_telegraph_sympy_crosscheck.py
python3 -B code/c213_telegraph_replay.py
python3 -B code/c213_telegraph_mutation.py
python3 -B code/c213_release_manifest.py
```

The checker is producer-independent and enforces recursive exact-key closure,
all parameter/mode/time uniqueness, 82-significant-digit nonzero fields,
source identities, scope flags and the Route-A tuple.  Mutation tests repair
hashes for semantic and schema attacks and retain a stale-hash attack.
