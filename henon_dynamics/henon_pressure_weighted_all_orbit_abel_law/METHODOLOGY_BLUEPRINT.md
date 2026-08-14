# Methodology blueprint

## Source lock

- one dynamical family: the certified area-preserving H6 survivor;
- source packets: HCS-P49 inversion-fixed half-cyclotomic integers;
- Banach assembly and pressure domain: HCS-P51;
- one-orbit Abel normalization: HCS-P52;
- no target prime or zero tables, fitted exponents, or post-hoc orbit cuts.

## Proof pipeline

1. Pair every multiplier conjugate with its inverse and identify the sum of
   expanding logarithms with the Mahler measure of the multiplier minimal
   polynomial.
2. Expand each cyclotomic value by Möbius inversion.
3. Bound off-circle conjugates geometrically and unit-circle conjugates by a
   two-logarithm lower bound.
4. Obtain an orbitwise
   \(\varphi(n)\mathcal H_\gamma/2+o(n)\) law.
5. Apply the totient Laplace limit from P52.
6. Dominate the boundary-normalized orbit terms by the P51 uniform
   period envelope; exchange the orbit sum and Abel limit.
7. Derive the joint pressure-height orbit law and Gamma scaled-index law.
8. Attack vector promotion with coordinate and mass functionals.

## Finite validation

The certificate uses the inherited exact primitive periods 1, 3 and 4.  A
separate reciprocal Salem polynomial, explicitly typed as non-H6, exercises
the unit-circle branch.  Exact norms, spectral heights, Abel rows and mixed
Laplace profiles are recomputed by an independent checker.

## Claim firewall

The finite checks do not enumerate all primitive orbits.  The proof of the
infinite exchange is the P51 summable majorant, not numerical convergence.
No scalar limit is renamed a determinant, trace formula, pressure pole or
operator spectrum.
