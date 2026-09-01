# Exact code contract

- `c269_chebyshev_producer.py` evaluates the closed inversion-quotient formulas and writes the canonical evidence file.  Its finite-field iteration is retained only for a map digest and observed regression histogram.
- `c269_chebyshev_checker.py` imports no producer.  It independently checks prime characteristics, monic declared degrees, irreducibility over `GF(p)`, identical fixed-`q` models across all degrees, finite-field arithmetic, Chebyshev recurrence, orbit following, fixed sets, image ranks and tails.
- `c269_chebyshev_sympy_crosscheck.py` forms selected full composition matrices and checks characteristic polynomials and ranks exactly.
- `c269_chebyshev_replay.py` rebuilds the evidence in a fresh temporary directory and requires byte equality.
- `c269_chebyshev_mutation.py` repairs the outer hash after each semantic corruption and requires every corrupted artifact to fail the independent quick gate, including a reducible-polynomial model substitution.
- `c269_release_manifest.py` is the final 27-payload, deterministic-PDF and content-addressed release gate.

All commands use only exact integer, finite-field and symbolic arithmetic.  No target prime table, zero table, local datum or fitted parameter is read.
