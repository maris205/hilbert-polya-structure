# Test report

Commands and final counts are populated from direct runs:

- producer: `C206_PRODUCER_PASS`, 675 Fourier cells, 54 composition cells;
- checker: `C206_CHECKER_PASS`, 9,646 assertions;
- SymPy: `C206_SYMPY_PASS`, 2,713 checks;
- replay: `C206_REPLAY_PASS`, byte exact;
- mutation: `C206_MUTATION_PASS`, 17 repaired-hash and one stale-hash
  rejection, including eight mathematical hostile mutations.

The checker imports no producer implementation. The SymPy path separately
reconstructs the Fourier PDE, completed square, strict quadratic curvature,
minimizer, and semigroup law. The checker separately locks the exact
norm-attainment boundary.

The checker and SymPy path also enforce `working_decimal_digits=100`,
`serialized_significant_digits=82`, and exactly 1,350 serialized decimal
fields; a repaired-hash precision-declaration mutation is rejected.
