# Code

`modular_orbits.py` implements the Stage-1 experiment in two strict phases:

1. `enumerate` builds a primitive, oriented cyclic-conjugacy ledger without
   importing or testing rational primes, then freezes it with SHA-256;
2. `audit` verifies that checksum before introducing rational primes solely as
   declared controls.

The code never reads Riemann-zero data. Its cutoff is S-R block length, not
geometric length; the generated manifest states that boundary. Trace
multiplicities are explicitly reported only within this block cutoff.

Run deterministic unit tests with `python3 test_modular_orbits.py`.
