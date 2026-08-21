# C86 reproducibility commands

```bash
python3 code/c86_effective_orbit_flip_chain.py
python3 code/c86_effective_orbit_flip_chain_checker.py
python3 code/c86_sympy_crosscheck.py
python3 code/c86_replay_checker.py
python3 code/c86_mutation_test.py
```

The producer uses the full generated group; the checker constructs orbit
components from generators.  Both verify strong lumpability, detailed
balance, repair flows, and the invariant Walsh spectrum.
