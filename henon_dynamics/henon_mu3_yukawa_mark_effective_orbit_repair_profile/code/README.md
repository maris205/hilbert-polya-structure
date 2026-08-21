# C81 reproducibility commands

```bash
python3 code/c81_effective_orbit_repair_profile.py
python3 code/c81_effective_orbit_repair_profile_checker.py
python3 code/c81_sympy_crosscheck.py
python3 code/c81_replay_checker.py
python3 code/c81_mutation_test.py
```

The producer and checker independently reconstruct the effective action and
the finite closure.  The symbolic script checks weighted orbit enumeration
and the fixed-support identity.
