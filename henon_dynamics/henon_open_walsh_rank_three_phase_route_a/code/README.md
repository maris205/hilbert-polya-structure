# C168 exact code

- `c168_rank_three_producer.py` emits the deterministic evidence JSON.
- `c168_rank_three_checker.py` independently reconstructs exact recurrences,
  counts, controls, scope flags, and nested-key closure.
- `c168_sympy_crosscheck.py` rebuilds the DFT matrices, spectra, tensor rank,
  phase algebra, moments, and antiunitary identities.
- `c168_replay.py` requires byte-identical evidence regeneration.
- `c168_mutation.py` runs repaired-hash semantic attacks plus a stale-hash
  attack.
- `c168_release_manifest.py` closes the 27 release payload files while
  excluding itself and transient build files.

Run all scripts from the package root with Python 3.  SymPy is required only
for the explicitly separate symbolic cross-check.  No network or target data
is used.
