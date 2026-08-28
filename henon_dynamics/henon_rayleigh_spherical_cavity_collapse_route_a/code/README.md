# C219 verification code

`c219_rayleigh_producer.py` writes thirteen high-precision rows using stable
endpoint quadratures.  `c219_rayleigh_checker.py` does not import the
producer: it recomputes clocks with hypergeometric primitives and validates
all sign and boundary branches.  `c219_rayleigh_sympy_crosscheck.py` checks
the first integral, Lagrangian, Beta substitution, Puiseux coefficients,
energy, volume, and `L^p` identities.  Replay checks byte identity and the
mutation harness checks repaired/stale hashes, semantic fields, unknown keys,
route, and scope tampering.  The scope lock treats the inverse-Beta expression
as source-local explicit solvability only: the source Beta clock is not target
continuation/divisor/counting law and is not an A3 analytic match.
The checker applies exact-key closure recursively to every serialized object,
including the theorem and frozen-system metadata.
