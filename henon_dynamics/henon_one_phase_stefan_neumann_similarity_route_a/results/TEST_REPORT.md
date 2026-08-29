# Test report

Expected commands from the package root:

    python3 code/c226_stefan_producer.py
    python3 code/c226_stefan_checker.py
    python3 code/c226_stefan_sympy_crosscheck.py
    python3 code/c226_stefan_replay.py
    python3 code/c226_stefan_mutation.py
    python3 code/c226_release_manifest.py

The checker uses an independent bracketed evaluation of the Neumann root. It
tests exact-key closure, every positive-Stefan row, strict root monotonicity,
the small-series coefficients, Lambert-W bounds, flux ratio, energy ledger,
and all three singular labels. The symbolic script verifies the PDE,
boundary conditions, series reversion (including the lambda-factor
reversion), and moving-domain integral.

Replay checks byte identity and the hostile suite passes 22/22 repaired/stale
hash and semantic mutations, including citation metadata and an unknown nested theorem key;
the erfc upper-bound inequality is checked numerically for every root. The
fixed-epoch PDF and self-excluded manifest are checked by
code/c226_release_manifest.py.
