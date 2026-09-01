# Executable evidence plan

## Claims under test

1. Character conductors have the stated multiplicities and cumulative count.
2. On every finite quotient, the DFT multiplier equals the independent
   conditional-expectation reconstruction.
3. Heat traces agree with direct high-precision shell summation.
4. The geometric zeta formula, full pole lattice, residues, and determinant
   differentiation use the frozen exponent convention.
5. Exact staircase ratios approach the two different envelopes.
6. The strict Schatten inequality and equality divergence are encoded without
   endpoint drift.
7. Every degenerate face and every Route-A nonclaim survives semantic mutation.

## Grid

- Primes: 2, 3, 5, 7.
- Fractional exponents: 1/2, 1, 2.
- Finite quotients: twelve \((p,N)\) pairs, through orders 4096, 3125, 2401,
  and 2187.
- Heat parameters: \(\mu\in\{0,1/3\}\), \(t\in\{1/8,1,8\}\).
- Zeta samples: \(\alpha s\in\{3/2,2,3\}\), plus pole indices -3 through 3.
- Counting shells: 1 through 6; spectral shells: 1 through 8.
- Schatten grid: \(\sigma,q\in\{1/2,1,2\}\).
- Proves-too-much controls: branching numbers 4, 6, and 10.

This gives 438 stored cells.  Finite grids certify conventions; quantified
claims are proved in `THEOREM_PACKAGE.md` and `paper/main.tex`.

## Independence and attacks

The producer uses high-precision `mpmath` for analytic values and NumPy FFTs
for finite characters.  The checker is a separate program with independent
double-precision sums and its own residue-class averaging implementation.
SymPy builds exact rational conditional-expectation matrices on small
quotients and differentiates the zeta formula symbolically.  Replay writes to
a fresh temporary path and requires byte equality.  Mutation repairs the
payload hash before altering source locks, scope flags, Route-A tuple,
normalization, a DFT value, analytic cells, endpoint flags, and the schema.

## Acceptance

All five scripts must pass with `PYTHONDONTWRITEBYTECODE=1`; the paper must
compile twice identically per revision with fixed epoch; text, font, log, and
visual audits must pass; and the release manifest must find exactly its 27
payload files plus itself.
