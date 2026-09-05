# Code ownership and independent lanes

`c388_algebraic_producer.py` implements exact quotient matrices and its own
integer Euclidean Smith algorithm with left/right unimodular witnesses. SymPy
produces characteristic polynomials. `c388_algebraic_checker.py` uses neither
the producer nor SymPy: matrix identities, Bareiss determinants and
Faddeev--LeVerrier verify every declared certificate independently.

`c388_algebraic_sympy_crosscheck.py` supplies an independent library Smith
calculation and character-by-character Fourier products; its 90-digit special
value and integral checks are numerical controls only. Replay runs two fresh
working directories. Mutation checks repair payload hashes before arithmetic
attacks and test strict YAML separately. Smoke tests include the exact
index-three source counterexample. The release driver closes source/PDF/file
membership and preserves settled TeX logs as actual text artifacts.
