# C262 executable evidence

- `c262_hill_producer.py` evaluates 900 all-sign closed-form transfers and six
  exact boundary witnesses.
- `c262_hill_checker.py` independently reconstructs transfers with entire
  power series and checks trace, determinant, class, and powers through 12.
- `c262_hill_sympy_crosscheck.py` proves determinant, discriminant,
  Cayley--Hamilton, Chebyshev, and Jordan identities.
- `c262_hill_replay.py` requires clean-process byte equality.
- `c262_hill_mutation.py` repairs payload hashes after attacks and requires
  every semantic corruption to be rejected.
- `c262_release_manifest.py` runs all gates and creates the self-excluded
  27-payload ledger.
