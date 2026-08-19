# C70 exact certificate code

- `c70_direct_factor_orbit.py` binds C66/C69 and produces the automorphism,
  stabilizer, orbit, mass, and counterexample certificate.
- `c70_direct_factor_orbit_checker.py` independently counts automorphisms from
  endomorphism blocks and verifies every field.
- `c70_group_crosscheck.py` uses a second block calculation, SymPy prime
  factorization, and GAP's exact `Aut(D)` computation.
- `c70_direct_factor_orbit_replay_checker.py` performs a clean-process replay.
- `c70_mutation_test.py` requires rejection of hostile semantic changes.
