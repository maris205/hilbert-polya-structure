# Test report

Expected commands from the package root:

    python3 code/c219_rayleigh_producer.py
    python3 code/c219_rayleigh_checker.py
    python3 code/c219_rayleigh_sympy_crosscheck.py
    python3 code/c219_rayleigh_replay.py
    python3 code/c219_rayleigh_mutation.py
    python3 code/c219_release_manifest.py

The checker uses an independent hypergeometric/incomplete-Beta path.  It
tests first-integral and Lagrangian text locks, every pressure sign, collapse
and expansion clocks, endpoint coefficients, energy and volume formulas,
boundary nulls, and all scope flags.  The symbolic script checks the same
claims from a separate SymPy derivation.
The checker also locks the Route-A failure boundary: the source Beta clock is
not target continuation/divisor/counting law and is not an A3 analytic match.
It also enforces recursive exact-key closure for evaluator, frozen object,
theorem, regression, route, scope, identity, citation, case, and sample
objects; the hostile suite passes 15/15, including a repaired unknown nested
key.
