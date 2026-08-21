# C97 code

- `c97_pair_orbit_quotient.py`: source-bound producer using maximal-order
  closure decoding.
- `c97_pair_orbit_quotient_checker.py`: independent exact reconstruction
  using inclusion-column closure decoding.
- `c97_sympy_crosscheck.py`: exact Burnside, orbit--stabilizer, and transpose
  checks.
- `c97_replay_checker.py`: clean deterministic evidence replay.
- `c97_mutation_test.py`: 14 hostile semantic mutations.
- `c97_release_manifest.py`: deterministic final file ledger.

Run with `PYTHONDONTWRITEBYTECODE=1`, `PYTHONHASHSEED=0`, `LC_ALL=C`, and
`TZ=UTC` for the recorded release environment.
