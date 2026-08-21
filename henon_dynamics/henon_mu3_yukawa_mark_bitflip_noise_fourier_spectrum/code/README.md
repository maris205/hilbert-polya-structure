# C82 reproducibility commands

```bash
python3 code/c82_bitflip_noise_fourier.py
python3 code/c82_bitflip_noise_fourier_checker.py
python3 code/c82_sympy_crosscheck.py
python3 code/c82_replay_checker.py
python3 code/c82_mutation_test.py
```

The wrong-path cross-check is intentionally absent; all C82 code lives under
this directory.  The checker and the symbolic script use independent routes.
