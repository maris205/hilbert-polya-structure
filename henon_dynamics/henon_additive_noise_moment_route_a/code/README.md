# C123 code

```bash
python3 code/c123_noise_producer.py
python3 code/c123_noise_checker.py
python3 code/c123_sympy_crosscheck.py
python3 code/c123_replay.py
python3 code/c123_mutation.py
python3 code/c123_release_manifest.py
```

The apparent randomness is part of the frozen model law.  Enumeration and all
checks are deterministic and exact; the independent checker does not import
the producer.
