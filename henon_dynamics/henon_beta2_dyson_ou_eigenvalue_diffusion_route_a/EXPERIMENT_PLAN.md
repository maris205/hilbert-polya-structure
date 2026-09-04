# Exact verification plan

## Structural lane

For every $1\leq N\leq16$, record the real Hermitian dimension, Vandermonde
degree, Doob energy shift, chamber normalizer factor, filled ground-state
Slater indices, and frozen gap.

## Partition spectral lane

- Reconstruct every level multiplicity for $1\leq N\leq16$ and
  $0\leq k\leq64$.
- Enumerate every partition with at most $N$ parts for $1\leq N\leq8$ and
  $0\leq|\kappa|\leq24$.
- For every enumerated partition, check strict Slater indices, degree shift,
  eigenvalue, and exact factorial norm.

## Kernel lane

At $N=2,3,4$ and four rational contractions, evaluate the killed determinant
and Doob kernel to 50 significant digits. The independent checker uses a
Leibniz determinant instead of the producer's matrix determinant and enforces
reversibility residual below $10^{-75}$.

## Symbolic lane

Check scalar Hermite equations, Vandermonde harmonicity and homogeneity,
stationary logarithmic gradients, all small partition Slater quotients,
partition-product coefficients, and center-of-mass gap saturation.

## Release lanes

Run the canonical producer, code-independent checker, SymPy checker,
two-directory byte replay, repaired-hash hostile mutation suite, unittest
smoke tests, optimized-mode refusal, three twice-fresh wrapper PDF builds,
strictly increasing page counts, embedded Latin/CJK font and raster audits,
bilingual abstract/keyword isolation, warning scans, firewall scans, and
exact 38-payload manifest closure.

Finite computation is a regression receipt, not proof by sampling.
