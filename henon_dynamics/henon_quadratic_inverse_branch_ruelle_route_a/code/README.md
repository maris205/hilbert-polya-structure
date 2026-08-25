# C141 exact computation code

- `c141_quadratic_ruelle_producer.py` constructs the period polynomials, exact quotient-algebra traces, Newton coefficients, and canonical evidence without importing SymPy.
- `c141_quadratic_ruelle_checker.py` is independent: it never imports the producer and recomputes the core traces with polynomial extended Euclid.
- `c141_sympy_crosscheck.py` supplies a third algebraic route using SymPy polynomial inversion and low-period resultants.
- `c141_replay.py` regenerates the evidence in a temporary directory and requires byte identity.
- `c141_mutation.py` repairs the payload hash after each semantic mutation, plus one stale-hash sentinel, and requires every mutation to be rejected.
- `c141_release_manifest.py` records the 27 payload files and excludes itself.

Run all commands from the package root with Python 3. No random input or floating-point arithmetic is used.
