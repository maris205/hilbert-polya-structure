# C163 code

- `c163_phase_producer.py`: freezes exact phase algebra, all-`k` theorem
  statements, binomial ledgers, Fourier-polynomial receipts, and controls.
- `c163_phase_checker.py`: independent strict-schema reconstruction with
  exact `Q(sqrt(37))`, binomial, recurrence, and finite-subgroup checks.
- `c163_sympy_crosscheck.py`: independently rebuilds the Walsh matrix,
  characteristic polynomial, primitive irreducible integer polynomial,
  monic rational minimal polynomial, Chebyshev recurrences, and moved-hole
  spectrum.
- `c163_replay.py`: requires byte-for-byte evidence reproduction.
- `c163_mutation.py`: requires rejection of repaired-hash semantic mutations
  and a stale-hash attack.
- `c163_release_manifest.py`: builds the self-excluded 27-file payload ledger.

The producer is never imported by either independent validator.
