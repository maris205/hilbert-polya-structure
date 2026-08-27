# Test report

Commands and final counts are populated from direct runs:

- producer: `C207_PRODUCER_PASS`, 18 profiles and 108 moment cells;
- checker: `C207_CHECKER_PASS`, 3,462 assertions over 90 profile samples;
- SymPy: `C207_SYMPY_PASS`, 56 independent symbolic checks;
- replay: `C207_REPLAY_PASS`, byte exact;
- mutation: `C207_MUTATION_PASS`, 33 repaired-hash and one stale-hash
  rejection.

The checker imports no producer implementation.  It recursively freezes all
declaration schemas and values; closes the ordered, unique 9-by-2 case grid
and each exact `z`/`r` grid; reconstructs Beta masses, chemical constants,
profiles, moments, and every regime null rule; and requires 100 working
decimal digits plus 82 significant digits in every nonzero serialized decimal
field.  The audited decimal inventory is 424 fields: 382 nonzero 82-digit
strings and 42 canonical `0.0` strings.

The SymPy program separately verifies generic porous and fast integrated
profile laws and stationary chemical potentials, the Gaussian law, the two
transformed Beta mass integrals and their `C` exponents, generic moment Beta
integrals and exponents, the sharp threshold and `m=1/3` boundary, the
pressure/interface coefficient, and both free-energy first variations.  Its
parameterization avoids branch-sensitive simplification of rational powers.
