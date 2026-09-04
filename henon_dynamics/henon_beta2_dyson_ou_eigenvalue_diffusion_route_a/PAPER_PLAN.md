# Paper plan

## One-sentence contribution

We prove a normalization-locked all-$N$ equivalence among Hermitian OU
eigenvalues, a conservative Vandermonde transform of killed independent OU
particles, and a complete partition-indexed Hermite spectrum with sharp gap
$1/2$.

## Claims--evidence matrix

| claim | analytic evidence | executable evidence |
|---|---|---|
| matrix OU gives the stated Coulomb SDE | trace-basis covariance plus second-order eigenvalue perturbation | dimension and convention ledger |
| the Doob kernel is conservative and noncolliding | reflection formula, $\mathcal L_0h=-dh/2$, Andréief identity | 12 independent high-precision determinant checks |
| ordered GUE is reversible | logarithmic gradient and scalar detailed balance | detailed-balance residual controls |
| the spectrum is complete | exterior Hermite basis and unitary Vandermonde map | 16,602 explicit partition/Slater/norm rows |
| gap and trace are sharp | partition degrees and the center-of-mass eigenfunction | 1,040 exact multiplicity rows and 350 SymPy checks |

## Three substantive manuscript rounds

1. **Round 0:** matrix radialization, exact GUE density, and covariance-locked
   gap scale.
2. **Round 1:** killed determinant, shifted Doob transform, conservativity,
   detailed balance, and no-collision boundary.
3. **Round 2:** complete Slater-quotient spectrum, norms, partition
   multiplicities, sharp Poincaré inequality, heat trace, source determinant,
   oscillator conjugacy, and strict Route-A closure.

Each round is a theorem extension rather than a prose-only revision.
