# C160 code

- `c160_sieve_producer.py` builds the exact maximal-subgroup inclusion--
  exclusion and Mersenne-prime cycle ledgers.
- `c160_sieve_checker.py` independently reconstructs all finite-field
  polynomial gcds, source-length factorizations, and Möbius checks.
- `c160_sympy_crosscheck.py` repeats the polynomial calculations in SymPy.
- `c160_replay.py` requires canonical byte equality.
- `c160_mutation.py` performs repaired-hash semantic and stale-hash attacks.
- `c160_release_manifest.py` builds the self-excluded release ledger.

Ordinary prime factors appearing here factor only the finite source clock
group.  The scripts use no external prime table, target zeros, arithmetic
local factors, or Route-B inputs.
